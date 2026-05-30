#!/usr/bin/env python3
"""
Bridge-gap attack, move 5: cross-sector test of the move-4 VEV/fluctuation
mechanism -- and an honest CORRECTION of its quark claim.

Move 4 claimed: leptons are light -> fluctuation-dominated -> block-count -> Q=2/3,
and 'heavier up-quarks are more VEV-dominated -> weaker Koide, consistent'. The
cross-sector test REFUTES the quark half:

OBSERVED Koide Q (charged sectors):
   charged leptons (pole): Q = 0.66666 ~ 2/3   (the clean block-count point)
   up quarks:   Q ~ 0.85-0.89  (ABOVE 2/3, toward 1)
   down quarks: Q ~ 0.73        (ABOVE 2/3)

MECHANISM PREDICTION: a positive uniform VEV a_VEV adds to the diagonal a,
DILUTING b/a = b_f/(a_VEV+a_f) -> r DOWN -> Q DOWN toward 1/3. So 'more VEV' can
only push Q BELOW 2/3. The quarks are ABOVE 2/3 -> the simple VEV-dilution
mechanism CONTRADICTS the quark data. (Also: 'heavy sector' != 'VEV-dominated';
VEV-dominated means ~degenerate, but the quarks are extremely HIERARCHICAL, the
opposite. The move-4 reasoning conflated the two.)

HONEST CONCLUSION:
 - The mechanism is LEPTON-SPECIFIC: it explains why the charged leptons CAN sit
   exactly at the covariant block-count point Q=2/3 (pure fluctuation, a_VEV~0).
 - It does NOT predict the quark sectors. Quark Q>2/3 means b/a>1/sqrt2 (MORE
   off-diagonal than equipartition / more hierarchical), which positive
   VEV-dilution cannot produce. The move-4 'consistent with quarks' claim is
   RETRACTED.
 - So the cross-sector pattern is NOT a confirmation; the lepton result stands on
   its own (leptons = block-count point), and the quarks remain a separate, harder
   problem (consistent with the long-standing finding that A1's grading does NOT
   propagate to quarks -- retained_no_go quark_c3_circulant_source_law_boundary).

This is a rigorous self-correction: the lepton-block-count result (moves 1-4) is
intact; the quark extrapolation was wrong and is removed.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q(masses):
    m = np.array(masses, float); return m.sum() / np.sqrt(m).sum() ** 2


def main():
    sep("observed Koide Q by sector (MeV)")
    lep = [0.5109989, 105.6584, 1776.86]
    print(f"  charged leptons (pole):  Q = {Q(lep):.6f}   (2/3 = {2/3:.6f})  -> block-count point")
    sets = {
        "up (m_t pole)":   [2.16, 1270, 172500],
        "up (m_t scale)":  [1.3, 630, 172500],
        "down (2 GeV)":    [4.67, 93.4, 4180],
    }
    for name, m in sets.items():
        q = Q(m)
        tag = "ABOVE 2/3 (contradicts VEV-dilution)" if q > 2 / 3 else "below 2/3"
        print(f"  {name:16s}:        Q = {q:.4f}   -> {tag}")

    sep("the prediction direction vs the data")
    print("  positive VEV a_VEV: b/a = b_f/(a_VEV+a_f) DECREASES -> r DOWN -> Q DOWN (toward 1/3).")
    print("  so the mechanism can only put sectors BELOW 2/3. Quarks are ABOVE -> NOT explained.")
    print("  (illustration: pure block-count b/a_f=1/sqrt2, add uniform VEV v:)")
    for v in [0.0, 0.5, 2.0]:
        a, b = v + 1.0, 1 / np.sqrt(2)
        ev = np.array([a + 2 * b, a - b, a - b])
        print(f"    v={v:.1f}: Q={(ev**2).sum()/ev.sum()**2:.4f}  (<= 2/3 always for v>=0)")

    sep("VERDICT (correction)")
    print("  Move-4 quark claim RETRACTED. The mechanism is LEPTON-SPECIFIC: it explains")
    print("  leptons sitting at the block-count point Q=2/3 (pure fluctuation, a_VEV~0). It does")
    print("  NOT predict the quarks (Q>2/3, b/a>1/sqrt2), which positive VEV-dilution cannot")
    print("  reach. The lepton result (moves 1-4) stands; the quark extrapolation was wrong.")
    print("  Consistent with retained_no_go quark_c3_circulant_source_law_boundary: A1's grading")
    print("  does not propagate to quarks -- they are a separate, harder problem.")


if __name__ == "__main__":
    main()
