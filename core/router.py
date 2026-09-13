"""Flipped ModelRouter. No 70B profile."""
PROFILES = {
    "T4_ship": {"precision": "ternary-1.58", "max": "ticket"},
    "T0_m6": {"precision": "ternary-1.58", "max": "kernel+local-gguf"},
    "T1_spark": {"precision": "fine-tune-latch", "max": "not-70B-pretrain"},
}

def route(hardware="T4_ship"):
    return PROFILES.get(hardware, PROFILES["T4_ship"])
