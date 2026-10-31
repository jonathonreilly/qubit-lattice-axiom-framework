# checks/bb10_criteria.md — pre-registered criteria for check bb10 (BFT lane B, session 10)

Written **after** BFT_B.md §34 (the session-10 PRE-STATED section, mod 13:07:28 UTC) and **before** any bb10 script
exists. No constant below is derived in session 10: the model constants (d = 2, L = 3, k = 2, κ_0 = 1, κ_1 = 2, roots =
block centres, axial order 0 then 1) are bb9b's; the factor 2d and the ratio L^{-3} are Lemma FT (ii) of session 9; the
operator identities are BL-2's. Every verdict below is a verdict on an **exact rational** computation: PASS requires exact
equality of `fractions.Fraction` values (or the stated exact inequality), never a tolerance.

## Model and environment (fixed before the run)
- d = 2, L = 3, k = 2, κ_0 = 1, κ_1 = 2; level sides at top side T: 9T, 3T, T. Roots = block centres. Axial order 0 then 1.
- Operators (`d`, `d*`, `ev`, `Q_l`, `Q_str,l`, `h_l`, transposes, `Ξ`, `Ξ^T`) are **copied unaltered** from
  `checks/bb9b_rtcc.py`, which is not edited. The copy is stated in the script header.
- `python3 -I`, `PYTHONDONTWRITEBYTECODE=1`, `nice -n 10`, OMP/OPENBLAS/MKL/VECLIB threads = 1, `fractions.Fraction` and
  Python ints only, **no numpy, no BLAS** — so DRIVE_BRIEF rule 6 exempts the run from the numeric lock. Under 20 min,
  under 1 GB.
- Random data: a fixed, stated integer seed and the explicit generator of bb9b (`rnd`), values in [-3, 3].

## Part A — top side T = 2, no solve (algebra only)

**A1 (DF (ii) telescoping, load-bearing).** For 10 random chains Y = (Y_0, Y_1) and 10 random level-l currents j
(l = 0, 1): ⟨j, Y_l⟩ = ⟨(Q^{(0→l)})^Tj, Y_0⟩ − Σ_{m<l}⟨(Q^{(m+1→l)})^Tj, r_m(Y)⟩ with r_m(Y) := Q_mY_m − Y_{m+1}.
- PASS: exact equality in every one of the pairs.
- FAIL: any discrepancy. (A FAIL would refute the starting identity of the session-10 (CO-fun) proof and must be reported
  as such.)

**A2 (d*C(j) = D(S)).** For 10 random plain collections j = (j_0, j_1) (no co-closedness imposed):
d*[Σ_l(Q^{(0→l)})^Tj_l] = d*j_0 + ev^{(0→1)T}d*j_1 as level-0 functions.
- PASS: exact equality in all 10. FAIL: otherwise.

**A3 (the regrouped funnel function).** For the same 10 collections: ξ_0 := ev^{(1→1)T}d*j_1 = d*j_1 as a level-1 function,
and the claim to be tested is ξ_0 = R_1(D(S)) − ψ_0, where ψ_0 is the level-1 function with ev^{(0→1)T}ψ_0 = Ψ_0 = d*j_0
(when Ψ_0 is level-1-root supported) and R_1(D(S)) is the level-1 function whose placement is D(S)·1{level-2 roots}.
- The test is run on collections for which Ψ_0 **is** level-1-root supported (constructed, as in bb9b A5).
- PASS: exact equality for every constructed collection, and at least one of them has ψ_0 ≠ 0 and ξ_0 ≠ 0 (non-vacuity
  printed). FAIL: any discrepancy, or no non-vacuous instance (then A3 is reported as untested, not as a PASS).

**A4 (the regrouping identity of Lemma DF-cc (ii), the central test).** For every constructed source satisfying
**(CC-0)**, i.e. D(S) = 0 as a level-0 function: C(j) := Σ_l(Q^{(0→l)})^Tj_l equals Σ_l(Q_str^{(0→l)})^Tĵ_l with
ĵ_0 = j_0 + h_0^Tψ_0 and ĵ_1 = j_1 + h_1^Tψ_1.
- PASS: exact equality for every such source, with at least one instance having h_0^Tψ_0 ≠ 0 (printed).
- FAIL: any discrepancy. **A FAIL refutes Lemma DF-cc (ii) and therefore the session-10 proof of Theorem COF; it is to be
  reported as a refutation, not patched.**

**A5 (control: the root-charge defect, designed to show A4's hypothesis is load-bearing).** For constructed sources with
D(S) ≠ 0 but D(S) supported on the level-2 roots (composite-co-closed, not strictly):
C(j) − Σ_l(Q_str^{(0→l)})^Tĵ_l = −Σ_{i<k}(Q_str^{(0→i)})^Th_i^TR_{i+1}(D(S)) exactly, and the left side is **nonzero**.
- PASS: the identity holds exactly **and** the defect is nonzero (so that A4 genuinely needs (CC-0)).
- FAIL: the identity fails, or the defect vanishes for every constructed source (then the control is uninformative and is
  reported as such).

**A6 (coarse-size claims).** With π_l(v) := L^{3(k−l)}·max|v| in the own units of level l (d = 2 model keeps the exponent 3
of the d = 4 convention only as a bookkeeping factor; the inequality tested is the dimension-free one): for 10 random
level-1 currents v, max|(Q_str^{(0→1)})^Tv| ≤ L^{-3}max|v|; and for the constructed sources,
max|h_l^Tψ_l| ≤ max|ψ_l| ≤ 2dΣ_{l'≤l}max|d*j_{l'}|/(2d) · 2d, i.e. max|ψ_l| ≤ Σ_{l'≤l}max|d*j_{l'}|.
- PASS: both inequalities hold in every instance. FAIL: any violation.

**A7 (control: the naive, unregrouped funnel is not of the same coarse order).** For at least one constructed (CC-0) source,
the naive per-level funnel term of the expansion of (Q^{(0→1)})^Tj_1 — namely h_0^Tev^{(1→1)T}d*j_1 placed at level 0 with
no straight push-down — has max value **strictly larger** than L^{-3}max|ĵ_1|, while the regrouped term
(Q_str^{(0→1)})^Th_1^Tψ_1 does not.
- PASS: such an instance exists (the regrouping is load-bearing).
- FAIL: no such instance (then the claim that the regrouping is what supplies the coarse size is **not** supported by this
  model and must be reported as unsupported).

## Part B — top side T = 1, exact rational solve (as in bb9b Part B)

**B0 (criticality).** For a constructed (CC-0) source with d*j_0 ≠ 0: the solve returns x with Hx = S exactly and Ξ^Tx = 0.
- PASS: both exact. FAIL: otherwise.

**B1 (C(j) co-closed at (CC-0), and the assembled J_0).** At that solution, with G = s = 0:
(i) d*C(j) = 0 exactly; (ii) J_0 = C(j) − (Q_str^{(0→k)})^Tρ_{k−1} exactly, with J_0 := j_0 + d*G_0 − Q_0^Tρ_0 = d*dx_0 of
Lemma RT-cc (d) and ρ_l := κ_lr_l − s_l of §19.1.
- PASS: both exact. FAIL: either.

**B2 (declared scope limit, not a test).** At T = 1 the level-2 lattice has one site, so a level-2-root-supported function
with total 0 vanishes: the root-charge branch (A5) **cannot** be exercised inside the solve at T = 1. This is pre-registered
here; it is reported as a scope limitation whatever Part B's outcome, and A5 carries the root-charge algebra at T = 2.

## Global verdict rule
`VERDICT bb10 (A1..A7, B0, B1): ALL PASS` only if every criterion above returns PASS on its own terms. Any FAIL is reported
as a FAIL in BFT_B.md §37 with the output and the script kept unaltered as the record; a rerun, if any, is a new id (bb10b)
with the same criteria and no criterion retuned.

---

## AMENDMENT (appended 13:12:09 UTC, still **before any bb10 script exists**; disclosed in BFT_B.md §37)

Two corrections and one addition, all made before the script was written and none of them after seeing any output.

**(i) A6 and A7: the exponent of the one-step straight push-down is dimension-dependent.** The bound used in lane A's
Theorem PW-cc is |Q_str^Tj| ≤ L^{-3}||j||_∞ "exactly L terms of weight L^{-4}", i.e. L^{-(d-1)} with d = 4. In the bb10
model d = 2, so the correct inequality to test is **max|(Q_str^{(0→1)})^Tv| ≤ L^{-(d-1)}max|v| = L^{-1}max|v|**, and in A7
the comparison threshold is likewise L^{-(d-1)}max|ĵ_1|. A6 and A7 are to be run with L^{-(d-1)}; the printed exponent must
be stated in the output. (Had they been run as first written, with L^{-3}, A6 would have failed for a reason that is an
error in this criteria file and not a fact about the lemma.)

**(ii) A7's second half is expected vacuous at k = 2 and that is not a PASS by content.** Under (CC-0) at k = 2 one has
ψ_{k-1} = ψ_1 = 0, so the regrouped counterpart of the naive term is identically 0 and trivially under threshold. A7's
verdict is therefore to be reported as "PASS (second half vacuous at k = 2)" if that is what happens, never as support for
the size claim.

**(iii) New test A8 (the size claim in both groupings — this is the content A7 cannot carry at k = 2).** With the model's
coarse convention π_l(v) := L^{(d-1)(k-l)}·max|v| (own units of level l; the exponent d - 1 by (i)), for the constructed
(CC-0) family compute and print π_0(h_0^Tξ_0) and π_0(h_0^Tψ_0) together with π_0(j_0), π_1(j_1) and the ratio
π_0(h_0^Tξ_0)/π_0(h_0^Tψ_0).
- PASS: both of **π_0(h_0^Tψ_0) ≤ 2d·π_0(j_0)** (the regrouped grouping: the funnel at level 0 draws on level 0 only — the
  form of Lemma FT (ii)) and **π_0(h_0^Tξ_0) ≤ 2d·L^{(d-1)}·π_1(j_1)** (the naive grouping: the funnel at level 0 draws on
  level 1, with the L^{(d-1)(k-1)} = L^{(d-1)} penalty of the un-pushed-down funnel at k = 2) hold in every instance.
- FAIL: either inequality is violated. The ratio is reported as a measurement, with no pre-registered threshold.

The global verdict line becomes `VERDICT bb10 (A1..A8, B0, B1)`.
