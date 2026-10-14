# lean_read.py

Read-only status printer at the repo root. Four lines of Python, stdlib only
(`json`, `pathlib`).

## What it does

1. Builds the path `~/.juniorhome/os/lean.json` (`Path.home() / ".juniorhome" / "os" / "lean.json"`).
2. If that file exists, parses it as JSON and prints it back as compact JSON on one line.
3. If it does not exist, prints this fallback:

```json
{"ok": false, "port": "JuniorDrive", "writes": 0}
```

## What it does not do

- No writes. It never creates or edits `lean.json` or any other file.
- No network. No sockets, no fetch, no ports opened.
- No arguments, flags, or environment variables are read.
- No error handling beyond the exists check: a present but invalid
  `lean.json` raises `json.JSONDecodeError`.

## Notes

- `"port": "JuniorDrive"` in the fallback is a label for this repo, not a
  network port. Any local service ports are 127.0.0.1 only; see `docs/LOCAL.md`.
- Router flow is covered in `docs/ROUTER.md`; overall layout in `docs/architecture.md`.
