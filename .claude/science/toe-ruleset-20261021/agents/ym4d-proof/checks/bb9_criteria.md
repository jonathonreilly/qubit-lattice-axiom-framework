# checks/bb9_criteria.md — pre-registered criteria for check bb9 (BFT lane B, session 9)

Written 2026-10-28 12:32 UTC, **after §27 (PRE-STATED) and §29 and BEFORE checks/bb9_rtcc.py exists**.
No threshold below uses any constant derived in session 9; every bound quoted is from §27.2 (pre-stated) or from
BFT_B §18.1/§19.2 / BFT_A BL-2 (earlier sessions).

## What is tested
Lemma RT-cc (a)-(d) and Lemma FT (i)-(ii) of §27.2, on the smallest lattice in which they are not vacuous.

**Arithmetic.** Exact, `fractions.Fraction` and Python integers only. No numpy, no BLAS, single thread. No numeric
lock is taken (DRIVE_BRIEF rule 6: exact rational arithmetic in plain python is cheap and needs no lock). The script
must print the verdict word PASS or FAIL for every test id below and a final VERDICT line naming any failing id.

**Model.** d = 2; L = 3; k = 2; κ_0 = 1, κ_1 = 2; roots = block centres (c_X = L·X + 1·(1,1), §15.0 convention);
Q_l := Q_{str,l} - d∘h_l with Q_str and h_l as in BL-2 (b) (h_l(w)(X) = average over y in B(X) of the integral of w
along the axial path c_X → y, coordinate order 0 then 1). Energy
E_src(x) = ½|dx_0|² + Σ_{l=0,1}(κ_l/2)|r_l|² − Σ_l⟨s_l, r_l⟩ − Σ_l⟨G_l, dx_l⟩ − Σ_l⟨j_l, x_l⟩, with x_2 = 0.

- **Part A** (no solve): top side T = 2, i.e. level-0 torus side 18, level-1 side 6, level-2 side 2.
- **Part B** (exact solve): top side T = 1, i.e. level-0 torus side 9, level-1 side 3, level-2 side 1; 180 unknowns.

## Part A — operator identities and the cascade (T = 2)

- **A1 (root covariance).** Q_l(dλ) = d(ev^{(l→l+1)}λ) for every level-l function λ, l = 0, 1.
  PASS iff the two matrices agree in **every** entry exactly. FAIL otherwise.
- **A2 (divergence intertwining).** d*Q_l^T = ev^{(l→l+1)T}d* as matrices, l = 0, 1. PASS iff exact equality.
- **A3 (funnel split).** Q_l^T = Q_{str,l}^T − h_l^T d* as matrices, l = 0, 1. PASS iff exact equality.
- **A4 (Lemma FT (i)).** For l = 0, 1: (a) every column of h_l^T (i.e. every row of h_l) has at most one nonzero
  entry per output link, i.e. each level-l link receives a contribution from at most ONE block; (b) max over entries
  of |c(X, b)| ≤ 1; (c) h_l^Tψ vanishes on every block-crossing link, for ψ = each basis delta.
  PASS iff (a), (b), (c) all hold exactly. FAIL if any entry exceeds 1 in absolute value, or if any level-l link
  receives from two blocks, or if a crossing link is hit.
- **A5 (cascade support, Lemma RT-cc (a), source side).** Over a spanning set of composite-co-closed plain sources
  (a basis of Ker Ξ^T restricted to the plain slots, built by exact elimination): Ψ_0 = d*j_0 is supported on the
  level-1 roots, and Ψ_1 = Ψ_0 + ev^{(0→1)T}d*j_1 is supported on the level-2 roots.
  PASS iff every basis element satisfies both support statements exactly. FAIL if any element violates either.
- **A6 (control, non-vacuity of A5).** There exists a plain source with Ξ^TS ≠ 0 whose d*j_0 is NOT supported on the
  level-1 roots. PASS iff such a source is exhibited (so A5 is a real constraint, not automatic). FAIL if every
  source happens to satisfy the support claim.

## Part B — the critical point (T = 1, exact solve)

Source: G_0 = G_1 = 0, s_0 = s_1 = 0, B_2 = 0; plain currents j_0, j_1 chosen with small integer entries so that
(i) Ξ^TS = 0 and (ii) **d*j_0 ≢ 0** (the source is composite-co-closed but NOT level-wise co-closed). Solve
(H + ΞΞ^T)x = S exactly (this operator is invertible: Hx = 0 and Ξ^TΞΞ^Tx = 0 force x = Ξλ with λ constant).

- **B0 (criticality).** Hx = S and Ξ^Tx = 0 exactly. PASS iff both hold with zero residual in exact arithmetic.
- **B1 (non-vacuity).** d*j_0 ≠ 0 and ψ_0 = d*ρ_0 ≠ 0. PASS iff both are nonzero.
- **B2 (Lemma RT-cc (a)).** d*ρ_0 equals the level-1 function Z ↦ (d*j_0)(z_Z) on the level-1 roots, and
  ev^{(0→1)T}(d*ρ_0) = d*j_0 as level-0 functions. PASS iff exact equality in every entry.
- **B3 (Lemma RT-cc (b), (c)).** ρ_0 = Q_{str,1}^Tρ_1 − ĵ_1 with ĵ_1 = j_1 + h_1^Tψ_1, ψ_1 = d*ρ_1.
  PASS iff exact equality in every entry.
- **B4 (control, the funnel is load-bearing).** The same identity with the funnel dropped (ĵ_1 → j_1) must FAIL
  whenever ψ_1 ≠ 0, and must hold when ψ_1 = 0. Report which branch the model realises. PASS iff the reported
  branch is internally consistent (ψ_1 = 0 ⟹ identity holds; ψ_1 ≠ 0 ⟹ identity fails).
  *Pre-registered expectation, recorded before the run:* at T = 1 there is a single level-2 root and the composite
  divergence has total 0, so **ψ_1 = 0 is expected** and B4 is expected to report the ψ_1 = 0 branch. This is a
  known scope limitation of Part B, stated in §27.7; it does not make B3 vacuous (B3 still tests the straightening
  Q_1^T → Q_{str,1}^T at the critical point), but it means Part B does not exercise a nonzero funnel inside the
  ρ-recursion. A5 and A4 carry that part.
- **B5 (Lemma RT-cc (d)).** J_0 := j_0 − Q_0^Tρ_0 satisfies d*J_0 = 0 exactly, and d*dx_0 = J_0 exactly.
  PASS iff both hold exactly.
- **B6 (Lemma FT (i) at the solution).** max|h_0^Tψ_0| ≤ max|ψ_0| (raw values), and h_0^Tψ_0 vanishes on every
  block-crossing level-0 link. PASS iff both hold.
- **B7 (control, no critical point without composite co-closedness).** For a plain source S' with Ξ^TS' ≠ 0, the
  vector x' := (H + ΞΞ^T)^{-1}S' has Hx' ≠ S'. PASS iff Hx' ≠ S' (so B0's criticality is a consequence of
  composite co-closedness, not automatic). FAIL if Hx' = S'.

## Disclosure rules
- Any test that fails is reported as a FAIL in §33 and in BFT_B_LOG, with the printed numbers; the output file is kept
  as the record and is not regenerated after retuning a criterion.
- Any probe added after seeing an outcome is labelled post-hoc and carries no pre-registration weight.
- Runtime budget: under 20 minutes, under 1 GB. If Part B's exact solve exceeds the budget, the script must print
  "B: ABORTED (budget)" and Part A's verdicts stand on their own; that is reported as an incomplete check, not a pass.

## Amendment, 2026-10-28 12:34 UTC (appended BEFORE checks/bb9_rtcc.py exists; no script and no output has been produced)

Added after re-reading §27.7's scope note and before writing any script: one more pre-registered test, because tests A3
and A4 as written could in principle be satisfied by a vacuous funnel (h_l ≡ 0 would make Q_l = Q_{str,l} and the
identities trivial).

- **A7 (non-vacuity of the funnel).** At T = 2 exhibit a level-(l+1) 1-form ρ with d*ρ ≠ 0 for which
  h_l^T(d*ρ) ≠ 0, for l = 0 and l = 1, and report max|h_l^T(d*ρ)| / max|d*ρ|. PASS iff h_l^T(d*ρ) ≠ 0 for both l
  **and** the reported ratio is ≤ 1 (the pre-stated bound ||h_l^T||_{ℓ^∞→ℓ^∞} ≤ 1 of §27.2 Lemma FT (i)).
  FAIL if either h_l^T(d*ρ) = 0 for some l (the funnel would be vacuous and A3 uninformative) or the ratio exceeds 1.
