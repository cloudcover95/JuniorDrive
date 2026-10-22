# Drive doc index slice 2026-10-22

JuniorHome Builder LLC slice. Additive only. cloudcover95. JuniorCloud LLC.
Docs-only. A reading map of every tracked file in JuniorDrive at the tip, plus which `docs/architecture.md` items have code in this repo. Nothing else is edited.

| Field | Value |
|---|---|
| When | 2026-10-22 ~02:20 MT (inside LLC write window 02:00–04:45) |
| Bot | JuniorHome Builder |
| Repo | cloudcover95/JuniorDrive |
| Rotation | JuniorHome → JuniorDrive → JuniorFetch (this run: JuniorDrive; prior JuniorHome 09da50a5c27adb91c00ef8ef911e9493a8f17682) |
| Next | JuniorFetch |
| Tip at clone | cce58d1ff8879259c2a989a4bcc472afabd4695f |
| Tip subject | docs: add 2026-10-19 drive consistency slice for JuniorDrive rotation |
| Tip date | 2026-10-19 02:23 MT (not recent; path free) |
| Tracked files at tip | 15 (240 lines) |
| Trit pack | none at tip; rate / close rule N/A here |
| Flags | mint false, socket false, layer_one false, fetch false, ue5_launch false |
| .github / Actions / Copilot / Dependabot | none at tip, none added |

## File map (tip cce58d1)

| File | Lines | What it says |
|---|---|---|
| `README.md` | 9 | Robotics / sim-to-real on JuniorHome rails. Not galkreiser1/juniordrive-backend. Not AGI_SDK 70B ModelRouter. Live entry is JuniorHome `web3node/drive_bridge.py`. |
| `core/router.py` | 9 | `PROFILES` (`T4_ship`, `T0_m6`, `T1_spark`) and `route()`, default and fallback `T4_ship`. |
| `lean_read.py` | 4 | Prints `~/.juniorhome/os/lean.json` or the fallback `{"ok": false, "port": "JuniorDrive", "writes": 0}`. |
| `docs/AUDIT.md` | 6 | Audit 2026-09-13: AGI_SDK 9607432 70B flipped; JuniorHome 93ea080 dist_pipe; galkreiser1 ignored. |
| `docs/Coaching_CrossPollination.md` | 5 | Four bullets: training timelines, hardware maintenance tracking, benchmarks; names JuniorAGI_SDK TimelineEngine. |
| `docs/GAIA_PROTOCOL.md` | 7 | Protocol id `goldend-osai-omega/1`; jobs dash-viewport, gaia-spine, agi-capsule; UE5 launch false; handshake in JuniorLLM `ports.gaia_proto`. |
| `docs/GAMMA.md` | 4 | gamma means AbsMean / winsor scale on lidar residuals; crispy-mouse HID; runtime JuniorHome `web3node/drive_gamma.py`. |
| `docs/JUNIOROS_NATIVE.md` | 1 | Drive sim does not link libvulkan from Home; same protocol id. |
| `docs/LEAN_READ.md` | 28 | Behavior and limits of `lean_read.py`. |
| `docs/LOCAL.md` | 6 | Hook 127.0.0.1:8770, i2sd 127.0.0.1:8767, "No 0.0.0.0." |
| `docs/ROBOTICS.md` | 3 | Use JuniorHome `web3node/robotics/`; input pose.json `{x,y,z,yaw}` and/or depth.npy; no vendor SDK here. |
| `docs/ROUTER.md` | 22 | Profile table and `route()` examples for `core/router.py`. |
| `docs/architecture.md` | 9 | Five design bullets (see below). |
| `docs/slices/2026-10-16-home-slice.md` | 60 | Earlier rotation slice. |
| `docs/slices/2026-10-19-drive-consistency.md` | 67 | Code-vs-docs check, bind check, outbound pointers. |

## Suggested reading order

1. `README.md`
2. `docs/architecture.md`
3. `docs/ROUTER.md` with `core/router.py`
4. `docs/LEAN_READ.md` with `lean_read.py`
5. `docs/LOCAL.md`
6. `docs/GAIA_PROTOCOL.md`, `docs/JUNIOROS_NATIVE.md`
7. `docs/GAMMA.md`, `docs/ROBOTICS.md`
8. `docs/AUDIT.md`, `docs/Coaching_CrossPollination.md`
9. `docs/slices/`

## architecture.md items vs code in this repo

| Item (as written) | Code in JuniorDrive at tip |
|---|---|
| Ternary x 3.0 inference core | none; `core/router.py` only labels profiles `ternary-1.58` |
| MCP + BitNet-Intel agentic layer | none |
| Sim-to-real pipeline | none here; README and ROBOTICS point at JuniorHome |
| Hardware-aware ModelRouter | `core/router.py` (`PROFILES`, `route()`) |
| Second Brain TDA memory | none |

"none" means no file in this repo implements it. It is not a claim about other repos. The line "Integrated with JuniorClimbs, Swift app, and full ecosystem" is quoted as written and not verified.

## Guards read (JuniorHome, one read-only fetch; not rewritten)

- docs/LLC_GUARDS.md
- docs/DUAL_AUTONOMY.md
- docs/BOT_FIRST.md
- docs/LANES.md
- docs/ROSTER.md

## Status

One new file. One commit. One push. No repo code run. No model pull. No UE5 launch. No remote script downloaded or executed.

## Self-check

Every row was read from the tip clone at cce58d1. Line counts come from `wc -l` on the clone. Pointers into JuniorHome and JuniorLLM are quoted from JuniorDrive docs and not checked in those repos. No existing file edited. Not a quant file. Inside LLC window.
