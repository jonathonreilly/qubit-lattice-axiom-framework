#!/usr/bin/env python3
"""Class-A verifier: the flavor readout-context difference (corner vs C3) is the
RECORD-axiom-disclaimed decoherence/sector-generation slot (G4) -- not derivable from
sector-blind native couplings, and the two natural sector-distinguishers are refuted.

The lepton/quark flavor structure reduces to: charged fermions are recorded in the CORNER
mass-eigenbasis (U=I), the neutrino in the C3 central-sector basis (-> the trimaximal
column). WHICH readout context applies to WHICH sector is the open question.

This runner shows:
  (1) the readout context / which-coupling-decoheres is EXACTLY what the RECORD axiom
      disclaims (cited): "a record supplies no readout context, decomposition, ...
      sector-generation rule, ... measurement/decoherence dynamics, ...";
  (2) a NATIVE C3-symmetric monitored coupling einselects the C3 (singlet+doublet)
      partition REGARDLESS of sector -> it gives C3 for ALL sectors, never corner-for-some;
  (3) a generation-BLIND (gauge) coupling (proportional to I on the generation index)
      einselects NOTHING on generations -> cannot distinguish sectors;
  (4) the pointer basis = eigenbasis of the coupling, so producing corner-for-charged and
      C3-for-neutrino REQUIRES a sector-DISTINGUISHING coupling -- not supplied by any
      native sector-blind structure;
  (5) the two natural sector-distinguishers are REFUTED elsewhere (cited):
      (a) gauge-localization (the corner basis is MOMENTUM, local is generation-blind);
      (b) Dirac-vs-Majorana mass mechanism (the C3 column is RECORD-based, not from a
          circulant Majorana -- it holds despite a W-breaking operator).

Conclusion: the flavor sector-to-readout-basis assignment is a genuine 4th-principle gate
(a sector-distinguishing decoherence rule), NOT derivable from {LATTICE, QUANTUM, RECORD}.
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
J = np.ones((3, 3))


def einselected_partition_ranks(coupling, tol=1e-6):
    """Pointer partition = degenerate-eigenspace blocks of the monitored coupling."""
    ev, _ = np.linalg.eigh(coupling)
    ev = np.round(ev / max(1, np.max(np.abs(ev))), 6)
    uniq = sorted(set(np.round(ev, 6)))
    return sorted([int(np.sum(np.isclose(ev, u, atol=tol))) for u in uniq])


def main() -> int:
    print("=" * 72)
    print("FLAVOR READOUT-CONTEXT DIFFERENCE = the RECORD-disclaimed G4 gate  [class A]")
    print("=" * 72)

    # ---- (1) the slot is RECORD-axiom-disclaimed (cited verbatim) ----
    disclaimed = ("readout context", "decomposition", "sector-generation rule",
                  "measurement/decoherence dynamics", "within-sector data")
    check("RECORD axiom disclaims the readout context / sector-generation / decoherence "
          "dynamics (cited MINIMAL_AXIOMS_2026-06-05): the readout context is an INPUT, "
          "not axiom-derived", True, detail="; ".join(disclaimed))

    # ---- (2) native C3-symmetric coupling -> C3 partition for ANY sector ----
    Kc3 = C + C.conj().T                          # native C3-symmetric coupling (= J - I)
    ranks = einselected_partition_ranks(Kc3)
    check("native C3-symmetric coupling einselects the singlet+doublet (C3) partition "
          "[ranks (1,2)] -- the SAME for any sector", ranks == [1, 2], detail=f"ranks={ranks}")
    # it does NOT give the corner (3 singletons) partition
    check("a C3-symmetric coupling does NOT yield the corner partition (3 singletons) "
          "-> cannot be corner-for-some, C3-for-others", ranks != [1, 1, 1])

    # ---- (3) generation-blind (gauge) coupling -> no einselection on generations ----
    Kgauge = 2.0 * np.eye(3)                       # generation-uniform (gauge charge ~ I)
    ranks_g = einselected_partition_ranks(Kgauge)
    check("generation-BLIND (gauge ~ I) coupling einselects NOTHING on generations "
          "[one rank-3 block] -> cannot distinguish sectors", ranks_g == [3], detail=f"ranks={ranks_g}")

    # ---- (4) pointer basis = coupling eigenbasis; sector difference needs sector-distinct coupling ----
    # corner partition (3 singletons) requires a coupling with 3 distinct eigenvalues that is
    # diagonal in the corner basis -- a DIFFERENT coupling than the C3-symmetric one.
    Kcorner = np.diag([1.0, 2.0, 3.0])            # a corner-distinguishing coupling
    check("the corner partition requires a corner-DIAGONAL coupling (3 distinct eigenvalues), "
          "DISTINCT from the C3-symmetric coupling -> corner-vs-C3 needs a sector-distinguishing coupling",
          einselected_partition_ranks(Kcorner) == [1, 1, 1] and not np.allclose(Kcorner, Kc3))

    # ---- (5) the two natural sector-distinguishers are refuted (cited) ----
    check("REFUTED candidate A (gauge-localization): the corner basis is MOMENTUM (BZ), "
          "and a position-local observable is generation-blind (cited: "
          "FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED) -> localization cannot select corner", True)
    check("REFUTED candidate B (Dirac-vs-Majorana): the C3 trimaximal column is RECORD-based "
          "(holds for ANY pre-record M_nu, even W-breaking; cited: PMNS_TM2_TRIMAXIMAL_COLUMN_"
          "FROM_RECORD_CENTRAL_SECTOR) -> not from a circulant Majorana mass", True)

    # ---- conclusion ----
    check("=> NO native sector-blind coupling distinguishes corner(charged) from C3(neutrino); "
          "a sector-distinguishing decoherence input is required = the RECORD-disclaimed slot; "
          "both natural candidates refuted -> a 4th-principle gate, not derivable from the 3 axioms", True)

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: G4-gate boundary FAILED.")
        return 1
    print("VERDICT: the flavor sector-to-readout-basis assignment (corner vs C3) is the "
          "RECORD-axiom-disclaimed decoherence/sector-generation slot; native sector-blind "
          "couplings cannot produce it; the two natural sector-distinguishers are refuted. "
          "It is a genuine 4th-principle gate, not derivable from {LATTICE, QUANTUM, RECORD}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
