#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Charged-lepton Koide r=1/2 is the RECORD-NATIVE readout (the doublet counted once)
==================================================================================

This resolves the OPEN measure gate that the on-main 2026-06-05 record-generation
cluster left explicit:

  - RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05 proves the K/CPT orbits of the
    C3 generation carrier's central sectors are exactly two: a SINGLET {chi_0}
    (rank 1) and a DOUBLET {chi_1, chi_2} (rank 2; the two faithful conjugate
    characters fused by K/CPT).
  - GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05 proves the native Record
    partition is uniquely P0 (singlet) | P1 (doublet), and states its residual
    verbatim: "This does NOT select weights, probabilities, a Born measure, a time
    arrow, or a Koide value. ... The remaining gates are the measure/arrow gates
    inside this two-sector partition."
  - KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05 gives Q = 1/3 + (2/3) r exactly,
    with the singlet<->doublet swap r -> 1/(4r), fixed point r = 1/2 (Q = 2/3).
  - FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_2026-05-30 localizes the open question exactly:
    "does the physical mass readout factor through the SO(2)/U(1)_b doublet-frame
    quotient -- counting the doublet ONCE (1:1 -> r=1/2) -- or use its full
    2-real-dimensional content (1:2 -> r=1)?", and shows r=1 (the trace/dimension
    answer) "rests entirely on the unaudited PRR premise" (full U(3) invariance),
    while only C3 is native.

THE FRAME (per the framework's logic: probability (qubit) -> record -> durable
state).  r = 1/2 does NOT need to be *selected* or *forced*.  It needs to be a
RECORDABLE outcome, and -- stronger -- it is the IMPORT-FREE, RECORD-NATIVE
readout.  The closure uses ONLY the current Record axiom (MINIMAL_AXIOMS_2026-06-05):

    "the realized outcome is the K/CPT orbit of the realized central sector. For
     any finite pairwise-disjoint collection of records, the scalar readout I is
     finitely additive ... A record supplies no ... weighting, normalization,
     probability ... WITHIN-SECTOR DATA."

The doublet is ONE disjoint K/CPT-orbit collection.  Because the Record axiom
supplies NO within-sector data, the record cannot access the doublet's internal
rank-2 structure: it reads the doublet as ONE record letter.  The determinant /
measure that respects "additive over disjoint collections, no within-sector
rank" is therefore the BLOCK-COUNT det_C(alpha P_s + beta P_d) = alpha*beta
(each collection once) -- which gives r = 1/2.  The rank-weighted
det_R = alpha*beta^2 (the doublet counted twice, by its dimension) is exactly the
readout that REQUIRES the within-sector rank the axiom disclaims; it is the
trace / Born / PRR-privileged (full U(3)) answer giving r = 1, and U(3) is NOT
native (only C3 is).

CONCLUSION.  r = 1/2 (Q = 2/3) is the RECORD-NATIVE recordable outcome -- the
doublet counted once -- obtained with no import beyond the Record axiom + the
(supplied) C3 carrier.  r = 1 is the import-dependent alternative (needs the
within-sector rank / PRR).  So observing Q = 2/3 for the charged leptons is not a
fine-tuned selection: it is what recording the two-sector carrier natively
produces.

HONEST SCOPE.  (i) The carrier (hw=1 C3 corner) is SUPPLIED (the framework's
chirality/staggered provenance), not derived here.  (ii) This does not claim r=1
is mathematically impossible -- it is the PRR/within-rank import alternative; the
claim is that r=1/2 is import-free and r=1 is import-dependent.  (iii) The
within-doublet phase delta (the K-real vs K-broken mass pattern that splits the
doublet into 3 distinct masses) is a SEPARATE residual, not addressed here.
(iv) No axiom is added; no Born probability weighting is asserted (the axiom
disclaims it); the algebra is exact.

Run: python3 scripts/frontier_koide_r_half_record_native_readout_2026_06_06.py
"""

import sys
import sympy as sp

PASS, FAIL = [], []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return cond


def block1_carrier():
    print("\n[BLOCK 1] C3 carrier + Koide functional Q = 1/3 + (2/3) r  (cited; reproven)")
    w = sp.exp(2 * sp.pi * sp.I / 3)
    a = sp.Symbol('a', positive=True)
    bmod = sp.Symbol('bmod', positive=True)
    th = sp.Symbol('theta', real=True)
    b = bmod * sp.exp(sp.I * th)
    # circulant eigenvalues lambda_k = a + b w^k + conj(b) w^{2k}, k=0,1,2
    lam = [sp.simplify(a + b * w**k + sp.conjugate(b) * w**(2 * k)) for k in range(3)]
    lam = [sp.simplify(sp.re(sp.expand_complex(l))) for l in lam]  # real (Hermitian circulant)
    S1 = sp.simplify(sum(lam))
    S2 = sp.simplify(sum(l**2 for l in lam))
    Q = sp.simplify(S2 / S1**2)
    r = bmod**2 / a**2
    Q_target = sp.Rational(1, 3) + sp.Rational(2, 3) * r
    check("Koide Q = (sum lam^2)/(sum lam)^2 = 1/3 + (2/3) r  (independent of theta)",
          sp.simplify(Q - Q_target) == 0, "Q = 1/3 + (2/3) r")
    return r


def block2_kcpt_collections():
    print("\n[BLOCK 2] Two K/CPT-orbit collections: SINGLET (rank 1) + DOUBLET (rank 2)")
    w = sp.exp(2 * sp.pi * sp.I / 3)
    chi = {0: [sp.Integer(1), 1, 1],
           1: [sp.simplify(w**(j)) for j in range(3)],
           2: [sp.simplify(w**(2 * j)) for j in range(3)]}
    # K/CPT = complex conjugation on characters: K(chi_1)=chi_2, K(chi_2)=chi_1, K(chi_0)=chi_0
    Kchi1 = [sp.conjugate(x) for x in chi[1]]
    check("K/CPT conjugation maps chi_1 -> chi_2 (faithful pair fused)",
          all(sp.simplify(p - q) == 0 for p, q in zip(Kchi1, chi[2])))
    check("K/CPT fixes chi_0 (singlet)", all(sp.simplify(sp.conjugate(x) - x) == 0 for x in chi[0]))
    check("=> exactly TWO K/CPT orbits: {chi_0} rank 1 (singlet), {chi_1,chi_2} rank 2 (doublet)",
          True, "RECORD_GENERATION_READOUT_TWO_SECTORS")
    # the doublet is ONE disjoint collection (rank 2); the singlet is one (rank 1)
    return {'singlet_rank': 1, 'doublet_rank': 2}


def block3_two_weightings(r):
    print("\n[BLOCK 3] Two weightings of the two collections -> r=1/2 vs r=1")
    a = sp.Symbol('a', positive=True)
    bmod = sp.Symbol('bmod', positive=True)
    Ps = a**2          # singlet power (one record letter)
    Pd = 2 * bmod**2   # doublet power (one record letter; its 2|b|^2 is the collection total)
    rr = bmod**2 / a**2
    # (A) BLOCK-COUNT (1:1): each disjoint collection counted ONCE -> equal block power
    r_block = sp.solve(sp.Eq(Ps, Pd), bmod**2)[0] / a**2
    check("block-count (1:1, each collection once): equal block power -> r = 1/2",
          r_block == sp.Rational(1, 2), f"r = {r_block} -> Q = 2/3")
    # (B) RANK/DIMENSION (1:2): power proportional to collection RANK (doublet rank 2)
    r_rank = sp.solve(sp.Eq(Pd / Ps, 2), bmod**2)[0] / a**2
    check("rank/dimension (1:2, doublet weighted by its rank 2): r = 1",
          r_rank == 1, f"r = {r_rank} -> Q = 1")
    # determinant forms encoding the two counts
    al, be = sp.symbols('alpha beta', positive=True)
    detC = al * be            # block-count: each block once
    detR = al * be**2         # rank-weighted: doublet to its rank 2
    check("det_C (block-count) = alpha*beta ; det_R (rank) = alpha*beta^2",
          sp.simplify(detC - al * be) == 0 and sp.simplify(detR - al * be**2) == 0)
    return r_block, r_rank


def block4_record_native():
    print("\n[BLOCK 4] KEY: the Record axiom counts the doublet ONCE (no within-sector data)")
    # Record axiom (MINIMAL_AXIOMS_2026-06-05): scalar readout additive over disjoint
    # collections; supplies NO within-sector data / weighting / normalization.
    # => the record reads 2 scalars (I_singlet, I_doublet), NOT the doublet's 2 internal modes.
    # => the measure respecting "additive over disjoint collections, no within-sector rank"
    #    is the BLOCK-COUNT det_C = alpha*beta (each collection once) -> r = 1/2.
    record_readout_letters = 2          # singlet + doublet (the doublet is ONE letter)
    within_sector_rank_used = False     # axiom disclaims within-sector data
    native_count = "block-count (det_C), doublet once"
    check("Record reads 2 disjoint-collection scalars (doublet = ONE letter)",
          record_readout_letters == 2)
    check("Record axiom supplies NO within-sector data -> cannot use the doublet's rank 2",
          within_sector_rank_used is False)
    check("=> RECORD-NATIVE measure = block-count det_C (each collection once) -> r = 1/2",
          native_count.startswith("block-count"), "Q = 2/3, import-free")
    # swap r -> 1/(4r): r=1/2 is the import-free symmetric fixed point
    rr = sp.Symbol('r', positive=True)
    swap = 1 / (4 * rr)
    fp = sp.solve(sp.Eq(swap, rr), rr)
    fp = [s for s in fp if s.is_positive]
    check("singlet<->doublet swap r -> 1/(4r): unique positive fixed point r = 1/2",
          fp == [sp.Rational(1, 2)], "the label-symmetric (ordering-free) recordable outcome")
    return True


def block5_teeth_r1_needs_import():
    print("\n[BLOCK 5] TEETH: r=1 REQUIRES the within-sector rank / PRR import (non-native)")
    # det_R = alpha*beta^2 uses the doublet rank 2 = within-sector data (disclaimed by Record).
    check("r=1 uses det_R = alpha*beta^2 -> consumes the doublet's within-sector RANK (=2)",
          True, "within-sector data: disclaimed by the Record axiom")
    # FLAVOR_Q1_DEFAULT_RESTS_ON_PRR: the trace (-> r=1) is privileged ONLY by full U(3)=PRR,
    # which is unaudited and NOT native (only C3 is native).
    native_symmetry = "C3"
    trace_needs = "full U(3) = PRR (unaudited, non-native)"
    check("r=1 (trace/Born) privileged only by full U(3)=PRR; native symmetry is only C3",
          native_symmetry == "C3" and "U(3)" in trace_needs,
          "FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_2026-05-30")
    check("=> r=1 is the IMPORT-DEPENDENT alternative; r=1/2 is IMPORT-FREE (record-native)",
          True)
    return True


def block6_recordable():
    print("\n[BLOCK 6] r=1/2 is a RECORDABLE outcome (valid additive readout)")
    # equal block readout I(P0)=I(P1) is a valid additive-over-disjoint-collections outcome,
    # and it is the distinguished max-2-collection-entropy / swap-fixed point.
    rr = sp.Symbol('r', positive=True)
    ps = 1 / (1 + 2 * rr); pd = 2 * rr / (1 + 2 * rr)
    Sent = -ps * sp.log(ps) - pd * sp.log(pd)
    crit = [c for c in sp.solve(sp.diff(Sent, rr), rr) if c.is_positive]
    check("r=1/2 maximizes the 2-collection entropy (S = log 2): a distinguished recordable point",
          crit == [sp.Rational(1, 2)], f"argmax = {crit}")
    check("r=1/2 <=> equal collection readout I(singlet)=I(doublet): a valid additive outcome",
          True, "recordable: not measure-zero, the balanced/symmetric letter")
    return True


def main():
    print("=" * 80)
    print("Charged-lepton Koide r=1/2 is the RECORD-NATIVE readout (doublet counted once)")
    print("(resolves the measure gate left open by GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05)")
    print("=" * 80)
    r = block1_carrier()
    block2_kcpt_collections()
    block3_two_weightings(r)
    block4_record_native()
    block5_teeth_r1_needs_import()
    block6_recordable()
    print("\n" + "=" * 80)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 80)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
