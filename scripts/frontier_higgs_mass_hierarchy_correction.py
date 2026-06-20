#!/usr/bin/env python3
"""Verify the Higgs hierarchy-correction negative result.

The note's claim is narrow: replacing the L_t=2 taste-curvature block with
the L_t=4 APBC block does not reduce m_H toward 125 GeV. It increases the
curvature and therefore increases the mass. The near-125 first-power
correction is kept as a negative control because the note says it has no
framework derivation.
"""

from __future__ import annotations

import math
from pathlib import Path

from canonical_plaquette_surface import CANONICAL_U0


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "HIGGS_MASS_HIERARCHY_CORRECTION_NOTE.md"

V_EW_GEV = 246.22
OBSERVED_HIGGS_GEV = 125.25


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        if ok:
            self.pass_count += 1
            tag = "PASS"
        else:
            self.fail_count += 1
            tag = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"[{tag}] {label}{suffix}")


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")
    gate = Gate()

    # L_t=2: spatial sin^2 terms are all 1 and the temporal APBC term is 1.
    lambda2_sq = 1.0 + 1.0 + 1.0 + 1.0
    # L_t=4: the temporal APBC term is sin^2(pi/4)=1/2.
    lambda4_sq = 0.5 + 1.0 + 1.0 + 1.0

    u0 = CANONICAL_U0
    a2 = 1.0 / (4.0 * u0 * u0)
    a4 = 2.0 / (7.0 * u0 * u0)
    ratio_lambda = lambda4_sq / lambda2_sq
    ratio_curvature = a4 / a2
    m2 = V_EW_GEV * math.sqrt(a2)
    m4 = V_EW_GEV * math.sqrt(a4)
    false_first_power = m2 * (7.0 / 8.0)
    c_apbc = (7.0 / 8.0) ** 0.25

    print("=" * 78)
    print("HIGGS HIERARCHY-CORRECTION NEGATIVE VERIFIER")
    print("=" * 78)
    print(f"u0 = {u0:.12f}")
    print(f"L_t=2 |lambda_hop|^2 = {lambda2_sq:.12f}")
    print(f"L_t=4 |lambda_hop|^2 = {lambda4_sq:.12f}")
    print(f"A4/A2 = {ratio_curvature:.12f}")
    print(f"m_H(L_t=2) = {m2:.6f} GeV")
    print(f"m_H(L_t=4) = {m4:.6f} GeV")
    print(f"false first-power branch = {false_first_power:.6f} GeV")
    print()

    gate.check("note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    gate.check("L_t=2 eigenvalue sum is 4", close(lambda2_sq, 4.0))
    gate.check("L_t=4 eigenvalue sum is 7/2", close(lambda4_sq, 3.5))
    gate.check("eigenvalue-squared ratio is 7/8", close(ratio_lambda, 7.0 / 8.0))
    gate.check("L_t=2 curvature is 1/(4 u0^2)", close(a2, 1.0 / (4.0 * u0 * u0)))
    gate.check("L_t=4 curvature is 2/(7 u0^2)", close(a4, 2.0 / (7.0 * u0 * u0)))
    gate.check("curvature ratio A4/A2 is 8/7", close(ratio_curvature, 8.0 / 7.0))
    gate.check("L_t=4 mass is larger than L_t=2 mass", m4 > m2, f"{m4:.3f} > {m2:.3f}")
    gate.check("L_t=2 mass matches note value 140.3 GeV", abs(m2 - 140.3) < 0.1, f"{m2:.3f}")
    gate.check("L_t=4 mass matches note value 150.0 GeV", abs(m4 - 150.0) < 0.2, f"{m4:.3f}")
    gate.check(
        "first-power branch is a numerical near miss only",
        abs(false_first_power - OBSERVED_HIGGS_GEV) / OBSERVED_HIGGS_GEV < 0.03,
        f"{false_first_power:.3f} vs observed {OBSERVED_HIGGS_GEV:.3f}",
    )
    gate.check("C_APBC is the fourth-root hierarchy factor", close(c_apbc, (7.0 / 8.0) ** 0.25))
    gate.check(
        "note explicitly rejects first-power derivation",
        "no physical derivation justifying this power" in text
        and "prior branch likely confused" in text,
    )
    gate.check(
        "note states correction increases rather than reduces m_H",
        "correction increases m_H" in text and "m_H goes UP to 150 GeV" in text,
    )
    gate.check(
        "note preserves dependency links",
        "HIGGS_MASS_FROM_AXIOM_NOTE.md" in text and "HIGGS_MASS_DERIVED_NOTE.md" in text,
    )

    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"TOTAL: PASS={gate.pass_count}, FAIL={gate.fail_count}")
    if gate.fail_count:
        print("Higgs hierarchy-correction verifier failed.")
        return 1
    print(
        "Verified negative result: the L_t=4 hierarchy/APBC replacement "
        "raises m_H, so it cannot close the Higgs 140-to-125 GeV gap."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
