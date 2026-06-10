#!/usr/bin/env python3
"""Historical DM leptogenesis full-axiom-closure compatibility runner.

The original filename is retained for audit-runner hygiene, but the current
work-history notes explicitly record non-closure.  This runner therefore checks
the exact historical boundary and the present framework-native transport value
without promoting the lane to full theorem closure.
"""

from __future__ import annotations

from pathlib import Path

from dm_leptogenesis_exact_common import (
    C_SPH,
    D_THERMAL_EXACT,
    ETA_OBS,
    S_OVER_NGAMMA_EXACT,
    exact_package,
    kappa_axiom_reference,
)

ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return condition


def main() -> int:
    print("DM leptogenesis historical full-closure boundary compatibility")
    print("=" * 72)

    note_0415 = read("docs/work_history/dm/DM_LEPTOGENESIS_FULL_AXIOM_CLOSURE_NOTE_2026-04-15.md")
    note_0416 = read("docs/work_history/dm/DM_LEPTOGENESIS_FULL_AXIOM_CLOSURE_NOTE_2026-04-16.md")

    for date, note in (("2026-04-15", note_0415), ("2026-04-16", note_0416)):
        check(
            f"{date} note cites the legacy runner path",
            "`scripts/frontier_dm_leptogenesis_full_axiom_closure.py`" in note,
        )

    check(
        "2026-04-15 note records non-closure and retained transport boundary",
        "does **not** yet land at `FULL THEOREM CLOSURE`" in note_0415
        and "`T_rad(K)`" in note_0415
        and "eta / eta_obs = 0.557919848420251" in note_0415,
    )
    check(
        "2026-04-16 note records exact non-closure and H_rad boundary",
        "does **not** satisfy `FULL THEOREM CLOSURE`" in note_0416
        and "`H_rad(T)`" in note_0416
        and "eta/eta_obs = 0.18878592785084122" in note_0416,
    )

    package = exact_package()
    kappa_direct, kappa_formal = kappa_axiom_reference(package.k_decay_exact)
    eta_ratio = (
        S_OVER_NGAMMA_EXACT
        * C_SPH
        * D_THERMAL_EXACT
        * package.epsilon_1
        * kappa_direct
        / ETA_OBS
    )

    check(
        "exact package keeps the DI saturation ratio fixed",
        abs(package.epsilon_ratio - 0.9276209209197268) < 1.0e-14,
        f"epsilon/epsilon_DI={package.epsilon_ratio:.16f}",
    )
    check(
        "ODE and formal transport agree at the current boundary",
        abs(kappa_direct - kappa_formal) < 2.0e-9,
        f"direct={kappa_direct:.16e}, formal={kappa_formal:.16e}",
    )
    check(
        "framework-native exact transport reproduces the historical boundary value",
        abs(eta_ratio - 0.18878592785084122) < 2.0e-9,
        f"eta/eta_obs={eta_ratio:.16f}",
    )

    print("Result: historical compatibility only; no full-closure promotion.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
