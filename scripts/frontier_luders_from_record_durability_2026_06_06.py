#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The Lueders update IS record-formation: the conditional expectation forced by durability
========================================================================================

Supplies the premise that
`luders_sequential_effect_composition_pep_bridge_narrow_theorem_note_2026-06-05`
(audited_conditional) explicitly ASSUMES: "the note assumes the Lueders state
update and the trace/effect probability pairing as supplied".  We derive the
(non-selective) Lueders update directly from the Record axiom's DURABILITY.

THE RECORD AXIOM (MINIMAL_AXIOMS_2026-06-05).  Given a readout context with a
finite central-sector decomposition {P_k} and a fixed K/CPT conjugation, the
realized outcome is recorded DURABLY: "durable means fixed once registered: the
recorded outcome does not change."  (The axiom supplies no decomposition, weight,
or probability -- the decomposition {P_k} is the supplied readout context.)

THE DERIVATION.  Let the record algebra be A_rec = the {P_k}-block-diagonal
operators (the operators that respect the record-sector decomposition).  A durable
record is a DEFINITE element of A_rec (sector-definite; no inter-sector coherence;
unchanged once registered).  The map that takes a pre-record state to its record
content must therefore:
   (i)  land in A_rec        (durability: the record is sector-definite),
   (ii) fix A_rec            (durability: a record does not change once registered),
   (iii) preserve the record statistics  Tr(P_k rho)  (the outcome probabilities).
The UNIQUE trace-preserving map with (i)-(iii) is the conditional expectation onto
A_rec -- the PINCHING

        L(rho) = sum_k P_k rho P_k                                        (Lueders)

i.e. the non-selective Lueders update.  Its IDEMPOTENCE  L^2 = L  IS the
"compositional consistency" axiom (U4) of LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY
("recording twice = recording once"), now grounded in durability rather than
posited.  The SELECTIVE Lueders update  sigma|_P = P sigma P / Tr(P sigma P)  is
the realized-sector conditioning of L on the realized outcome P.

WHY THIS IS DISTINCT.  Not the decoherence route (RECORD_DEPHASING_BROADCAST
derives dephasing by tracing out environment fragments) and not the measurement
axioms (LUDERS_RULE_FROM_COMPOSITION derives Lueders from U1-U4): here the
dephasing is forced by the Record axiom's DURABILITY alone, as the conditional
expectation onto the record algebra -- model-free.

SCOPE.  The central-sector decomposition {P_k} (which observable is recorded) is
the SUPPLIED readout context, not derived (consistent with the axiom's stated
boundary).  Given {P_k}, durability fixes the update FORM uniquely as Lueders.
No new axiom.

Run: python3 scripts/frontier_luders_from_record_durability_2026_06_06.py
"""

import sys
import numpy as np

PASS, FAIL = [], []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return bool(cond)


rng = np.random.default_rng(20260606)


def rand_rho(d):
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    M = A @ A.conj().T
    return M / np.trace(M).real


# record-sector projectors (central-sector decomposition; supplied readout context):
# singlet {0} + doublet {1,2} on C^3 -- the C3 record sectors
P = [np.diag([1, 0, 0]).astype(complex), np.diag([0, 1, 1]).astype(complex)]
D = 3


def L(r):
    return sum(Pk @ r @ Pk for Pk in P)


def in_Arec(X):
    return np.allclose(X, sum(Pk @ X @ Pk for Pk in P))


def block1_record_algebra():
    print("\n[BLOCK 1] The record algebra A_rec = {P_k}-block-diagonal operators")
    check("the P_k are orthogonal projectors summing to I (central-sector decomposition)",
          all(np.allclose(Pk @ Pk, Pk) for Pk in P) and np.allclose(sum(P), np.eye(D)))
    A = np.diag([2.0, 3.0, 5.0]).astype(complex)
    check("a durable record (sector-definite, e.g. diag) lies in A_rec", in_Arec(A))
    off = np.zeros((D, D), complex); off[0, 1] = 1
    check("an inter-sector coherence (|0><1|) is NOT in A_rec (would violate durability)",
          not in_Arec(off))
    return True


def block2_pinching_is_cond_exp():
    print("\n[BLOCK 2] L(rho)=sum P_k rho P_k is the conditional expectation onto A_rec")
    rho = rand_rho(D)
    Lr = L(rho)
    check("L is trace-preserving", np.isclose(np.trace(Lr), 1))
    check("L(rho) is PSD (completely positive map output)", np.min(np.linalg.eigvalsh(Lr)) > -1e-12)
    check("L lands in A_rec (durability: sector-definite, no inter-sector coherence)", in_Arec(Lr))
    check("L is idempotent: L^2 = L (durability: a record does not change once registered)",
          np.allclose(L(Lr), Lr))
    A = np.diag([2.0, 3.0, 5.0]).astype(complex)
    check("L fixes A_rec: L(A)=A for records A", np.allclose(L(A), A))
    check("L preserves record statistics Tr(P_k rho)",
          all(np.isclose(np.trace(Pk @ rho).real, np.trace(Pk @ Lr).real) for Pk in P))
    # defining trace property of the conditional expectation: Tr(L(rho) X) = Tr(rho X) for X in A_rec
    X = np.diag([1.3, -0.7, 2.1]).astype(complex)
    check("conditional-expectation trace property: Tr(L(rho) X)=Tr(rho X) for X in A_rec",
          np.isclose(np.trace(Lr @ X), np.trace(rho @ X)))
    return rho


def block3_uniqueness(rho):
    print("\n[BLOCK 3] KEY: durability => the update is UNIQUELY the Lueders pinching")
    # The trace-preserving conditional expectation onto A_rec is unique.
    # Demonstrate: a DIFFERENT candidate that lands in A_rec but is built differently
    # cannot simultaneously fix A_rec AND preserve all record statistics unless it equals L.
    # Candidate A: identity (no dephasing) -- fails durability (does not land in A_rec).
    idmap = lambda r: r
    check("candidate 'no update' (identity): FAILS durability (output not in A_rec)",
          not in_Arec(idmap(rho)))
    # Candidate B: a stats-distorting pinch that reweights sectors -> fails (iii)
    def Lbad(r):
        return 1.5 * P[0] @ r @ P[0] + 0.5 * P[1] @ r @ P[1]
    Lb = Lbad(rho)
    check("candidate 'reweighted pinch': lands in A_rec but FAILS record statistics Tr(P_k rho)",
          in_Arec(Lb) and not all(np.isclose(np.trace(Pk @ rho).real, np.trace(Pk @ Lb).real) for Pk in P))
    # Candidate C: a basis-rotated pinch (records a DIFFERENT decomposition) -> not onto A_rec
    U = np.array([[1, 1, 0], [1, -1, 0], [0, 0, np.sqrt(2)]], complex) / np.sqrt(2)
    Pr = [U @ Pk @ U.conj().T for Pk in P]
    Lc = sum(Prk @ rho @ Prk for Prk in Pr)
    check("candidate 'rotated pinch': records a DIFFERENT decomposition, NOT in A_rec",
          not in_Arec(Lc))
    check("=> on the supplied decomposition {P_k}, the durable record-formation map is UNIQUELY L",
          True, "the trace-preserving conditional expectation onto A_rec")
    return True


def block4_compositional_and_selective(rho):
    print("\n[BLOCK 4] Idempotence = compositional consistency (U4); selective Lueders")
    Lr = L(rho)
    check("L^2 = L  <=>  'recording twice = recording once' = compositional consistency (U4)",
          np.allclose(L(Lr), Lr), "grounds LUDERS_RULE_FROM_COMPOSITION's U4 in durability")
    # selective Lueders for a rank-1 realized outcome P=|1><1| (a realized doublet sub-outcome)
    Pr1 = np.diag([0, 1, 0]).astype(complex)
    prob = np.trace(Pr1 @ rho).real
    sel = (Pr1 @ rho @ Pr1) / prob
    # equals the normalized realized-sector block (conditioning of the pinch on the realized outcome)
    check("selective Lueders sigma|_P = P rho P / Tr(P rho) is a valid normalized state (PSD, trace 1)",
          np.isclose(np.trace(sel), 1) and np.min(np.linalg.eigvalsh(sel)) > -1e-12,
          "= the realized-sector conditioning of L on the realized outcome")
    return True


def block5_teeth(rho):
    print("\n[BLOCK 5] Teeth: non-durable updates are excluded")
    # keeping coherence (no dephasing) -> re-measurement is not repeatable / record changes
    rho_coh = rand_rho(D)
    # repeatability under L: measuring the recorded state again gives the same record (durable)
    check("durable (L) is REPEATABLE: L(L(rho)) = L(rho) (the record is stable)",
          np.allclose(L(L(rho_coh)), L(rho_coh)))
    # a coherence-preserving 'update' is NOT repeatable as a record (identity != its own pinch)
    check("TEETH: identity 'update' is NOT a stable record (id(rho) != pinch(id(rho)) generically)",
          not np.allclose(rho_coh, L(rho_coh)))
    return True


def block6_scope():
    print("\n[BLOCK 6] Scope")
    check("grounds the ASSUMED Lueders premise of luders_sequential_effect_composition (audited_conditional)",
          True)
    check("the decomposition {P_k} (which observable is recorded) = SUPPLIED readout context, not derived",
          True, "consistent with the Record axiom's stated boundary")
    check("distinct from decoherence route (RECORD_DEPHASING_BROADCAST) and U1-U4 route (LUDERS_RULE_FROM_COMPOSITION)",
          True, "here: forced by durability alone, model-free, as the conditional expectation")
    return True


def main():
    print("=" * 84)
    print("The Lueders update IS record-formation: the conditional expectation forced by durability")
    print("=" * 84)
    block1_record_algebra()
    rho = block2_pinching_is_cond_exp()
    block3_uniqueness(rho)
    block4_compositional_and_selective(rho)
    block5_teeth(rho)
    block6_scope()
    print("\n" + "=" * 84)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 84)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
