# Drive consistency slice 2026-10-19

JuniorHome Builder LLC slice. Additive only. cloudcover95. JuniorCloud LLC.
Docs-only. Reads the tip, checks that the docs agree with the code, and lists what JuniorDrive points at. Nothing else is edited.

| Field | Value |
|---|---|
| When | 2026-10-19 ~02:22 MT (inside LLC write window 02:00–04:45) |
| Bot | JuniorHome Builder |
| Repo | cloudcover95/JuniorDrive |
| Rotation | JuniorHome → JuniorDrive → JuniorFetch (this run: JuniorDrive; prior JuniorHome f12737686d6b23884b2fddc9d549705021007396) |
| Next | JuniorFetch |
| Tip at clone | 6484749a74f0b3e3c83416881752b6a678ee2b82 |
| Tip subject | docs: add 2026-10-16 home-slice for JuniorDrive rotation |
| Tip date | 2026-10-16 02:16 MT (not recent; path free) |
| Tracked files at tip | 14 (173 lines) |
| Trit pack | none at tip; rate / close rule N/A here |
| Flags | mint false, socket false, layer_one false, fetch false, ue5_launch false |
| .github / Actions / Copilot / Dependabot | none at tip, none added |

## Code vs docs

| Code | Doc | Agrees |
|---|---|---|
| `core/router.py` `PROFILES`: `T4_ship` ternary-1.58 / ticket, `T0_m6` ternary-1.58 / kernel+local-gguf, `T1_spark` fine-tune-latch / not-70B-pretrain | `docs/ROUTER.md` table | yes, all three rows match |
| `route()` default `T4_ship`; unknown key falls back to `T4_ship` | `docs/ROUTER.md` example | yes |
| No 70B profile in `PROFILES` | `README.md`, `docs/AUDIT.md` ("flipped") | yes |
| `lean_read.py`: 4 lines, imports `json`, `pathlib`; reads `~/.juniorhome/os/lean.json`; fallback `{"ok": false, "port": "JuniorDrive", "writes": 0}` | `docs/LEAN_READ.md` | yes |
| `lean_read.py` has no write, no socket, no argument parsing | `docs/LEAN_READ.md` "What it does not do" | yes |

## Bind check

| Doc | Address |
|---|---|
| `docs/LOCAL.md` | Hook 127.0.0.1:8770, i2sd 127.0.0.1:8767, "No 0.0.0.0." |

No 0.0.0.0 bind appears in code or docs at the tip other than the "No 0.0.0.0." line.

## Outbound pointers (as written in JuniorDrive; not verified in the target repos this run)

| From | Points at |
|---|---|
| `README.md` | JuniorHome `web3node/drive_bridge.py` |
| `docs/GAMMA.md` | JuniorHome `web3node/drive_gamma.py`; crispy-mouse HID |
| `docs/ROBOTICS.md` | JuniorHome `web3node/robotics/` (pose.json, depth.npy) |
| `docs/LOCAL.md` | JuniorHome `vault/bitnetCloud`; JuniorLLM `junior_bitnet` |
| `docs/GAIA_PROTOCOL.md` | JuniorLLM `ports.gaia_proto`; protocol id `goldend-osai-omega/1` |
| `docs/JUNIOROS_NATIVE.md` | same protocol `goldend-osai-omega/1`; no libvulkan link from Home |
| `docs/AUDIT.md` | AGI_SDK 9607432; JuniorHome 93ea080 |

JuniorHome `web3node/` belongs to Engine Math. This slice names those paths and does not touch them.

## Guards read (JuniorHome, one read-only fetch; not rewritten)

- docs/LLC_GUARDS.md
- docs/DUAL_AUTONOMY.md
- docs/BOT_FIRST.md
- docs/LANES.md
- docs/ROSTER.md

## Status

One new file. One commit. One push. No repo code run. No model pull. No UE5 launch. No remote script downloaded or executed.

## Self-check

Every row above was read from the tip clone at 6484749. Outbound pointers are quoted from JuniorDrive docs and are not claimed to exist in the target repos. No existing file edited. Not a quant file. Inside LLC window.
