"""Pytest suite for task_tracker.py.

Each test runs in its own tmp_path (via the `isolated_cwd` fixture) so
tasks.json never touches the real repo file.
"""

import json

import pytest

import task_tracker as tt


@pytest.fixture
def isolated_cwd(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path


def read_tasks(tmp_path):
    return json.loads((tmp_path / "tasks.json").read_text())


# --- add ---------------------------------------------------------------

def test_add_creates_task(isolated_cwd, capsys):
    tt.main(["add", "Write lab report"])
    tasks = read_tasks(isolated_cwd)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Write lab report"
    assert tasks[0]["status"] == "pending"
    assert tasks[0]["id"] == 1
    assert "added task 1" in capsys.readouterr().out


def test_add_increments_id(isolated_cwd):
    tt.main(["add", "first"])
    tt.main(["add", "second"])
    tasks = read_tasks(isolated_cwd)
    assert [t["id"] for t in tasks] == [1, 2]


def test_add_rejects_empty_title(isolated_cwd):
    with pytest.raises(SystemExit):
        tt.main(["add", "   "])


def test_add_rejects_missing_title(isolated_cwd):
    with pytest.raises(SystemExit):
        tt.main(["add"])


# --- list ----------------------------------------------------------------

def test_list_missing_tasks_json(isolated_cwd, capsys):
    """No tasks.json on disk at all should be treated as an empty list."""
    assert not (isolated_cwd / "tasks.json").exists()
    tt.main(["list"])
    out = capsys.readouterr().out
    assert "no tasks yet" in out


def test_list_shows_tasks(isolated_cwd, capsys):
    tt.main(["add", "task one"])
    tt.main(["add", "task two"])
    tt.main(["done", "1"])
    capsys.readouterr()
    tt.main(["list"])
    out = capsys.readouterr().out
    assert "[x]" in out and "task one" in out
    assert "[ ]" in out and "task two" in out


def test_list_rejects_arguments(isolated_cwd):
    with pytest.raises(SystemExit):
        tt.main(["list", "extra"])


# --- done ------------------------------------------------------------------

def test_done_marks_task_complete(isolated_cwd, capsys):
    tt.main(["add", "task"])
    capsys.readouterr()
    tt.main(["done", "1"])
    tasks = read_tasks(isolated_cwd)
    assert tasks[0]["status"] == "done"
    assert "task 1 marked done" in capsys.readouterr().out


def test_done_unknown_id_fails(isolated_cwd):
    tt.main(["add", "task"])
    with pytest.raises(SystemExit):
        tt.main(["done", "999"])


def test_done_non_integer_id_fails(isolated_cwd):
    with pytest.raises(SystemExit):
        tt.main(["done", "abc"])


# --- delete ------------------------------------------------------------------

def test_delete_removes_task(isolated_cwd, capsys):
    tt.main(["add", "task one"])
    tt.main(["add", "task two"])
    capsys.readouterr()
    tt.main(["delete", "1"])
    tasks = read_tasks(isolated_cwd)
    assert [t["id"] for t in tasks] == [2]
    assert "task 1 deleted" in capsys.readouterr().out


def test_delete_unknown_id_fails(isolated_cwd):
    tt.main(["add", "task"])
    with pytest.raises(SystemExit):
        tt.main(["delete", "999"])


# --- missing / corrupt tasks.json -------------------------------------------

def test_load_tasks_missing_file_returns_empty(isolated_cwd):
    assert tt.load_tasks() == []


def test_load_tasks_empty_file_returns_empty(isolated_cwd):
    (isolated_cwd / "tasks.json").write_text("")
    assert tt.load_tasks() == []


def test_load_tasks_corrupt_json_fails(isolated_cwd):
    (isolated_cwd / "tasks.json").write_text("{not valid json")
    with pytest.raises(SystemExit):
        tt.load_tasks()


def test_load_tasks_non_list_json_fails(isolated_cwd):
    (isolated_cwd / "tasks.json").write_text(json.dumps({"id": 1}))
    with pytest.raises(SystemExit):
        tt.load_tasks()


# --- main dispatch ----------------------------------------------------------

def test_main_no_command_fails(isolated_cwd):
    with pytest.raises(SystemExit):
        tt.main([])


def test_main_unknown_command_fails(isolated_cwd):
    with pytest.raises(SystemExit):
        tt.main(["frobnicate"])
