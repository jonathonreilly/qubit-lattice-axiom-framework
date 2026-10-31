# checks/bb10c_criteria.md — pre-registered criteria for check bb10c (BFT lane B, session 10)

Written after bb10 ran (13:14-13:15 UTC, ALL PASS) and **before any bb10c script exists**. bb10c is **not** a rerun of
bb10: bb10 stands as written, with its criteria, output and script unaltered, and no criterion of bb10 is retuned or
reinterpreted here. bb10c is a **new check at k = 3**, added for two reasons stated before it runs:
1. bb10 ran at k = 2, where the cascade has only i = 0, 1 and where Lemma DF-cc (ii)'s exchange of the double sum has a
   single inner term. The load-bearing algebra deserves a case with three levels.
2. bb10's test A8 compared the coarse sizes of the regrouped and the naive funnel and found the ratio 1. **That is not a
   k = 2 artefact**: under (CC-0), ξ_i = −ψ_i exactly, so the two are the same vector at every k. What differs between the
   two groupings is **which bound is available** — Σ_{l'≤i} (Lemma FT (ii), with the L^{−(d−1)(i−l')} contraction) against
   Σ_{l>i} (with an L^{(d−1)(l−i)} penalty). bb10c measures **the two bounds**, not the two vectors. This correction to
   bb10's reading is entered in BFT_B.md §37.4 and is written here before bb10c exists.

Model: the operator construction of `checks/bb9b_rtcc.py`, copied with **one** change, stated in the script header:
**K = 3** in place of K = 2. So d = 2, L = 3, k = 3, κ_0 = 1, κ_1 = 2 (κ_2 unused — no solve), roots = block centres, axial
order 0 then 1, top side T = 1, level sides 27, 9, 3, 1. **Part A only: no solve, no Hessian.** Exact `Fraction` arithmetic,
no numpy, no BLAS, single thread, `python3 -I`, `nice -n 10`; exempt from the numeric lock by DRIVE_BRIEF rule 6.

At T = 1 the level-3 lattice has one site, so a root-supported function of total 0 vanishes: **every source built here
satisfies (CC-0) automatically**, and the root-charge branch of Lemma DF-cc (ii) is **not** tested by bb10c (bb10's A5
tests it at k = 2, T = 2). Pre-registered as a scope limitation.

## Tests

**C1 (the cascade identity at three levels).** For 6 constructed plain collections (j_0, j_1, j_2) with D(S) = 0 and
d*j_l ≠ 0 for at least two levels: ψ_i (from ev^{(0→i+1)T}ψ_i = Ψ_i) and ξ_i = Σ_{l>i}ev^{(i+1→l)T}d*j_l satisfy
**ξ_i = −ψ_i for i = 0, 1, 2**.
- PASS: exact equality for every i and every collection, with ψ_0 ≠ 0 and ψ_1 ≠ 0 in at least one collection (printed).
- FAIL: any discrepancy, or no instance with two nonzero levels (then C1 is reported as untested).

**C2 (Lemma DF-cc (ii) at k = 3).** C(j) := Σ_{l≤2}(Q^{(0→l)})^Tj_l equals Σ_{l≤2}(Q_str^{(0→l)})^Tĵ_l with
ĵ_l = j_l + h_l^Tψ_l (ψ_2 = 0 at T = 1).
- PASS: exact equality for every collection, with at least one h_l^Tψ_l ≠ 0 for an l ≥ 1 (printed; this is what k = 2
  could not exercise inside a three-level cascade).
- FAIL: any discrepancy. A FAIL refutes Lemma DF-cc (ii) and is to be reported as a refutation, not patched.

**C3 (d*C(j) = D(S) = 0).** For the same collections, d*C(j) = 0 exactly.
- PASS: exact. FAIL: otherwise.

**C4 (the two bounds, which is the point of bb10c).** With π_l(v) := L^{(d−1)(k−l)}max|v|, compute for each collection and
each i: the true value V_i := π_0((Q_str^{(0→i)})^Th_i^Tψ_i), the **FT bound**
B^ψ_i := 2d·Σ_{l'≤i}L^{−(d−1)(i−l')}π_{l'}(j_{l'}), and the **ξ bound** B^ξ_i := 2d·Σ_{l>i}L^{(d−1)(l−i)}π_l(j_l).
- PASS requires both: (a) **V_i ≤ B^ψ_i for every i and every collection** (this is the bound Proposition COF-size uses);
  and (b) **B^ξ_0 > B^ψ_0 in at least one collection** (so that the two available bounds are genuinely different at k = 3
  and the ψ-bound is the one that does not grow with the level).
- FAIL: (a) violated anywhere — that would refute Proposition COF-size's arithmetic; or (b) never satisfied — then the
  claim that the regrouping is what supplies the k-uniform bound is **not supported at k = 3** and must be reported as
  unsupported. All values are printed whatever the verdict.

**C5 (control).** For 4 **random** collections (no (CC-0) constraint, so Ψ_i is in general not root-supported): the
construction of ψ_i must fail the root-support test, and C2's identity must fail for at least one of them.
- PASS: root support fails for at least one collection **and** C2's identity fails there.
- FAIL: otherwise (then the hypothesis of Lemma DF-cc (ii) is not shown to be load-bearing at k = 3).

## Global verdict rule
`VERDICT bb10c (C1..C5): ALL PASS` only if every criterion returns PASS on its own terms. Any FAIL is reported as a FAIL
in BFT_B.md §37.4 with the output and the script kept unaltered.
