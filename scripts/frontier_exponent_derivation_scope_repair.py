#!/usr/bin/env python3
"""Scope-repair runner for docs/EXPONENT_DERIVATION.md.

The repaired row is not a positive dimensional-exponent theorem. It records
that the retained matched 2D/4D replay blocks use of the old alpha ~ 1/d
heuristic as a closed mechanism on the current surface.
"""

from __future__ import annotations

from pathlib import Path


NOTE = Path("docs/EXPONENT_DERIVATION.md")

MATCHED_ROWS = {
    25: (0.9341, 9.76, 0.9647, 9.52, 4.75),
    40: (0.9577, 9.98, 0.9559, 9.69, 4.75),
    60: (0.9555, 10.11, 0.9378, 9.78, 4.75),
    80: (0.9667, 10.24, 0.9812, 9.89, 4.75),
    100: (0.9428, 10.25, 0.9991, 9.89, 4.75),
}

ALPHA_2D = -0.158
ALPHA_4D = -2.704
DELTA_ALPHA = -2.546


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            status = "PASS"
        else:
            self.fail_count += 1
            status = "FAIL"
        suffix = f" ({detail})" if detail else ""
        print(f"[{status}] {label}{suffix}")

    def summary(self) -> int:
        print(f"SUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        return 0 if self.fail_count == 0 else 1


def main() -> int:
    gate = Gate()
    print("Exponent derivation scope-repair certificate")
    print("=" * 72)

    gate.check("matched replay has five pinned N rows", len(MATCHED_ROWS) == 5)
    gate.check(
        "matched 4D alpha is not flatter than matched 2D alpha",
        ALPHA_4D < ALPHA_2D,
        f"alpha_4d={ALPHA_4D}, alpha_2d={ALPHA_2D}",
    )
    gate.check(
        "delta alpha matches retained dependency",
        abs((ALPHA_4D - ALPHA_2D) - DELTA_ALPHA) < 1e-12,
        f"delta={ALPHA_4D - ALPHA_2D}",
    )

    # The old heuristic would predict the 4D graph's spatial d=3 exponent from
    # the 2D graph's spatial d=1 baseline by dividing by 3.
    old_prediction = -1.5 / 3.0
    gate.check(
        "matched replay is inconsistent with old alpha~1/d prediction",
        abs(ALPHA_4D - old_prediction) > 1.0,
        f"matched={ALPHA_4D}, old_prediction={old_prediction}",
    )

    for n, (pur2, k2, pur4, k4, r4) in MATCHED_ROWS.items():
        gate.check(
            f"N={n}: 2D and 4D degrees are approximately matched",
            abs(k2 - k4) < 0.40,
            f"2D<k>={k2}, 4D<k>={k4}",
        )
        gate.check(
            f"N={n}: pur_min values are valid probabilities",
            0.0 < pur2 < 1.0 and 0.0 < pur4 < 1.0,
            f"pur2={pur2}, pur4={pur4}, r4={r4}",
        )

    text = NOTE.read_text(encoding="utf-8")
    required = [
        "does not claim a retained dimensional",
        "does not prove `alpha ~ 1/d_spatial`",
        "does not assert the old 5D/6D exponent predictions as binding results",
        "MATCHED_2D_4D_DECOHERENCE_NOTE.md",
    ]
    for needle in required:
        gate.check(f"source note contains required firewall: {needle}", needle in text)

    forbidden = [
        "If this argument is correct:",
        "**5D (d_spatial=4):** alpha",
        "**6D (d_spatial=5):** alpha",
        "the exponent approaches zero",
    ]
    for needle in forbidden:
        gate.check(f"source note omits old prediction overclaim: {needle}", needle not in text)

    return gate.summary()


if __name__ == "__main__":
    raise SystemExit(main())
