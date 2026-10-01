import todo


def test_add_done_remove(tmp_path, monkeypatch):
    monkeypatch.setattr(todo, "DB", tmp_path / "tasks.json")
    todo.add("write code")
    assert todo.load() == [{"title": "write code", "done": False}]
    todo.done(1)
    assert todo.load()[0]["done"] is True
    todo.remove(1)
    assert todo.load() == []
