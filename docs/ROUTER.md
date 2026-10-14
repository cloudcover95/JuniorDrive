# ModelRouter profiles (`core/router.py`)

Flipped ModelRouter. No 70B profile (see README).

| Profile | Precision | Max |
|---|---|---|
| `T4_ship` (default) | ternary-1.58 | ticket |
| `T0_m6` | ternary-1.58 | kernel+local-gguf |
| `T1_spark` | fine-tune-latch | not-70B-pretrain |

```python
from core.router import route
route()           # T4_ship
route("T0_m6")
route("unknown")  # falls back to T4_ship
```

Matches README flow: T4 ticket → T0 adapters → Spark train latch off.

Related: `lean_read.py` prints `~/.juniorhome/os/lean.json`, or
`{"ok": false, "port": "JuniorDrive", "writes": 0}` if missing.
Local ports: see `docs/LOCAL.md` (127.0.0.1 only).
