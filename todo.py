#!/usr/bin/env python3
"""Simple command-line todo manager. Tasks are stored in tasks.json."""
import argparse
import json
from pathlib import Path

DB = Path("tasks.json")


def load():
    return json.loads(DB.read_text(encoding="utf-8")) if DB.exists() else []


def save(tasks):
    DB.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def add(title):
    tasks = load()
    tasks.append({"title": title, "done": False})
    save(tasks)
    print(f"Added: {title}")


def list_tasks():
    tasks = load()
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. [{'x' if t['done'] else ' '}] {t['title']}")


def done(index):
    tasks = load()
    tasks[index - 1]["done"] = True
    save(tasks)
    print(f"Completed: {tasks[index - 1]['title']}")


def remove(index):
    tasks = load()
    removed = tasks.pop(index - 1)
    save(tasks)
    print(f"Removed: {removed['title']}")


def main():
    p = argparse.ArgumentParser(description="Simple todo CLI")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sub.add_parser("add").add_argument("title")
    sub.add_parser("done").add_argument("index", type=int)
    sub.add_parser("remove").add_argument("index", type=int)
    a = p.parse_args()
    if a.cmd == "add":
        add(a.title)
    elif a.cmd == "list":
        list_tasks()
    elif a.cmd == "done":
        done(a.index)
    elif a.cmd == "remove":
        remove(a.index)


if __name__ == "__main__":
    main()
