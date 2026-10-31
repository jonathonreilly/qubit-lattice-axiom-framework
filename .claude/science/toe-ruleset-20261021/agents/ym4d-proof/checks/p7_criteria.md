# checks/p7_criteria.md — pre-registered criteria for check p7 (PLD lane E, session 7)

Written 2026-10-28 14:20 UTC, **BEFORE checks/p7_pld.py exists**. Exact arithmetic only (`fractions.Fraction`,
`decimal.Decimal` at 60 digits), plain python3 -I, single thread, no numpy, no BLAS, no sampling, **no numeric lock**
(the session-24 brief exempts exact rational/symbolic arithmetic in plain python).

**No constant derived in session 7 appears in a PASS/FAIL condition.** Every number quoted below is sourced inline to a
file and session EARLIER than session 7, or is a pure lattice geometry constant (d = 4, L = 3, powers of 3, 5, 2).
Per [RHW5-fix W5-1] every criterion is labelled **PRE-REGISTERED** (outcome genuinely unknown when written, or checked
against a value recorded in an earlier session) or **CONFIRMATORY** (a reproduction of hand arithmetic already written in
§19 of PLD.md earlier today, i.e. NOT a pre-registration).

Recorded inputs (all pre-session-7):
- ε_1 = 6.7·10⁻⁴⁰ and g_K² = 10⁻⁹⁴, u := 1/g_K² — RLARGE §0 / PLD §18.7.2 (α), p6 A2.
- p6 A2's recorded value of u·ε_1² = (ε_1/g_K)²: **4.489·10¹⁵** — PLD §18.10, session 6.
- p6 D1's recorded dof = 3·n_int·81 = **52488** and Gaussian/heuristic log value **18190.95** at λ_f = ½ — PLD §18.10.
- §18.8 (ii) clause 5's admissible ceiling **log c ≤ 10⁹** — PLD §18.8, session 6.
- θ = 1/24 and the fallback θ ≈ 8·10⁻⁷ — PLD §18.7 / §18.8 (iii), p6 C2.
- n_int = **216** — HW §0 / HW Lemma W-bad (links interior to a cube at d = 4, L = 3).
- HW Lemma RING's per-level factor **2^d** and §18.4's per-level factor **3^d** — HW §41 item 4, PLD §18.4.

## A. The event route's price (the 4.489·10¹⁵ identity, re-formed independently)
- **A1 [PRE-REGISTERED]** Form X := u·ε_1² and Y := (ε_1/g_K)² = ε_1²/g_K² as exact Fractions from ε_1 = 67/10⁴¹ and
  g_K² = 10⁻⁹⁴. **PASS iff X == Y exactly AND float(X) rounds to 4.489e15 at four significant digits** (p6 A2's recorded
  value). FAIL otherwise.
- **A2 [CONFIRMATORY]** M := (1 − λ_f)·X at λ_f = 1/2, and the log-miss ratio ρ := λ_f·X/10⁹ against §18.8 (ii) clause 5.
  **PASS iff M ∈ [2.2·10¹⁵, 2.3·10¹⁵] AND ρ ∈ [2.2·10⁶, 2.3·10⁶].** (Reproduces §19.6 (i)'s hand arithmetic; not a
  pre-registration.)
- **A3 [negative control, CONFIRMATORY of p6 A3]** Re-form X with ε_1 := g_K (i.e. ε_1² := g_K²). **PASS iff X == 1
  exactly.** If this fails, the identity of A1 is an artefact of the formula rather than of the thresholds.

## B. The equipartition identity against p6 D1's recorded heuristic value
- **B1 [PRE-REGISTERED]** Compute E(dof, λ) := (dof/2)·ln(1/(1 − λ)) in Decimal at 60 digits, at dof = 52488 and
  λ = 1/2. **PASS iff |E − 18190.95| < 0.01** (p6 D1's recorded value, session 6). This is the check that §19.4/§19.5's
  exact identity reproduces the lane's recorded "Gaussian heuristic" — if it fails, the identification in §19.5 is wrong.
- **B2 [negative control, PRE-REGISTERED]** **PASS iff E(52488, 0) == 0 exactly AND E(52488, 1 − 10⁻⁶) > 10⁵.** (The
  identity must vanish at λ = 0 and diverge as λ ↑ 1; if it does not, the λ-dependence is not the claimed one.)
- **B3 [PRE-REGISTERED]** The ceiling clause: with B := dof/(2(1 − λ)) at dof = 52488, λ = 1/2, check B against
  §18.8 (ii) clause 5's restated bound 10⁹/λ. **PASS iff B ≤ 10⁹/λ**, and report the number of decades of margin.

## C. The one-step coupling slack, and the level-0 window size
- **C1 [PRE-REGISTERED, with negative control]** For x ∈ {2⁻¹, 2⁻², …, 2⁻¹⁰} check the exact rational inequality
  1/(1 − x) ≤ 1 + 2x (the step of Lemma DOM, from RLARGE l.106). **PASS iff it holds for every such x.**
  **Negative control C1n: PASS iff the same inequality FAILS at x = 3/4** (so that x ≤ ½ is load-bearing).
- **C2 [CONFIRMATORY]** L := ((3·n_int − 3)/2)·ln(1/(1 − θ)) in Decimal at n_int = 216 (HW §0) and θ = 1/24 (p6 C2).
  **PASS iff L ∈ [13.0, 14.5].** (Reproduces §19.7 (iv)'s hand arithmetic for the level-0 window; not a
  pre-registration. The "− 3" is the single interior site of an L⁴ = 3⁴ block at L = 3, a geometry constant.)

## D. The outward-ring regress power count (indicative; never a proof)
- **D1 [PRE-REGISTERED]** At d = 4 form the exact rational partial sums T(M) := Σ_{r=1}^{M} r^{(d-1)-2(d-2)} = Σ r^{-1}
  for M = 10³, 10⁴, 10⁵. **PASS iff T(10⁴) − T(10³) and T(10⁵) − T(10⁴) are each within 1% of ln 10**, i.e. the sum
  diverges logarithmically. FAIL otherwise.
- **D2 [negative control, PRE-REGISTERED]** The same exponent formula at d = 5 (Σ r^{-2}). **PASS iff T_5(10⁵) is within
  10⁻³ of π²/6 = 1.6449340668…**, i.e. convergent. If D2 fails the exponent formula is mis-written and D1 means nothing.

## E. The colouring/Hölder price of route (ρ2)
- **E1 [PRE-REGISTERED]** With χ := 5^d at d = 4, compute θ_max := 1/(24χ) exactly. **PASS iff χ == 625 AND
  θ_max > 8·10⁻⁷** (the recorded fallback θ of §18.8 (iii)), i.e. route (ρ2)'s tightening still leaves θ above the
  previously-feared fallback. FAIL otherwise.

## F. The closed-column vs open-column ring price (Finding (BUF-CC))
- **F1 [PRE-REGISTERED]** At d = 4 compute 1 + 3^d and 1 + 2^d exactly. **PASS iff 1 + 3^d == 82 AND 1 + 2^d == 17**, so
  that §18.4's recorded ×82 is the closed-column price and HW §41 item 4's recorded ×17 is the open-column price, and the
  two differ by exactly 3^d/2^d = 81/16.

## Reporting rule
Any FAIL is reported AS A FAIL in PLD.md §19.9 and in PLD_LOG.md, the script and output are kept unaltered, and any
re-run is under a new id (p7b) with this criteria file untouched. Anything computed after seeing the output is labelled
post-hoc and is not counted as passed.
