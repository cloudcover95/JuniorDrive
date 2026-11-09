# Drive slice: doc purpose map

Date: 2026-11-09 (America/Denver)
Lane: LLC bot (home-slice), write window 02:00 to 04:45 MT
Repo: cloudcover95/JuniorDrive
Prev tip: 6218288 (2026-11-06)

A docs-only map of what each existing file in this repo says, taken from
the files at tip 6218288. It adds no code, edits no existing file, and
runs nothing.

## Code

| File | What it holds |
|---|---|
| `core/router.py` | `PROFILES` dict with `T4_ship`, `T0_m6`, `T1_spark`, and `route(hardware="T4_ship")`, which falls back to `T4_ship` for unknown names. No 70B profile. |
| `lean_read.py` | Prints `~/.juniorhome/os/lean.json`, or `{"ok": false, "port": "JuniorDrive", "writes": 0}` if that file is missing. |

## Docs

| File | One-line purpose |
|---|---|
| `docs/ROUTER.md` | Table of the three router profiles and how `route()` is called. |
| `docs/LOCAL.md` | Local hook 127.0.0.1:8770 and i2sd 127.0.0.1:8767; no 0.0.0.0. |
| `docs/LEAN_READ.md` | Notes for `lean_read.py`. |
| `docs/GAIA_PROTOCOL.md` | Protocol id `goldend-osai-omega/1`; jobs Drive may emit; UE5 launch false, no model pull. |
| `docs/GAMMA.md` | Defines gamma as AbsMean / Junior winsor scale on lidar residuals; runtime lives in JuniorHome. |
| `docs/JUNIOROS_NATIVE.md` | Drive sim does not link libvulkan from Home; same protocol as Gaia. |
| `docs/ROBOTICS.md` | Points to JuniorHome `web3node/robotics/`; input is pose.json and/or depth.npy; no vendor SDK here. |
| `docs/architecture.md` | Short architecture bullet list (ternary core, router, sim-to-real, memory). |
| `docs/Coaching_CrossPollination.md` | Notes on reusing coaching ideas for robotics timelines and hardware maintenance. |
| `docs/AUDIT.md` | Audit dated 2026-09-13: no third-party code; ModelRouter 70B flipped. |
| `docs/slices/` | Dated home-slice records, one per Drive run. |

## Local-only reminders from existing files

- Local ports are 127.0.0.1 only (`docs/LOCAL.md`).
- Gaia identity is a local `gaia.json` (`docs/GAIA_PROTOCOL.md`).
- Runtime for robotics and gamma lives in JuniorHome, not here.

## Rotation

JuniorHome, JuniorDrive, JuniorFetch, then back. This run is JuniorDrive.
Next: JuniorFetch (2026-11-10).

No trit pack in this repo; rate 0.05 and the close rule do not apply.
Not a quant file. No .github, no remote scripts, no repo code run.
