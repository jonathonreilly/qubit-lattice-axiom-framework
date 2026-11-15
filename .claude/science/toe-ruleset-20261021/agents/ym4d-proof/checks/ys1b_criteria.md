# ys1b criteria — written 2026-10-28 15:06 UTC, BEFORE `ys1b_power.py` exists

**This is a RE-RUN under a new id.** `checks/ys1_criteria.md` is **untouched**, and `ys1_funnel.py`,
`ys1_out.txt`, `ys1_err.txt` are kept unaltered with their two FAILs (A2 clause (c); A4 (V-other)).
ys1b re-runs **only the two failed clauses**, with the defects repaired. Every ys1 clause that passed
(A0, A1, A2 (a)+(b), A2′ sup clause, A3, A5, A6, A7) stands on ys1 and is **not** re-run.

The two defects, named before the new criteria are written:
- **D1 (A2 clause (c)).** The criterion asserted the **equality** ‖K_i‖_1 = L^i·L^{−d}Σ_{y∈B}|y − c_X|_1.
  Only "≤" is derivable (one Q_str^T step satisfies ‖Q_str^Tψ‖_1 ≤ L‖ψ‖_1, with equality **iff** no two
  level-i links of opposite sign have overlapping fine stencils — which is false, because the composite
  longitudinal stencil overhangs the block by L^i − 1). The analytic bound of YSUP uses only "≤" and the
  **sup** clause (b), which passed at every i tested. The repaired criterion is the inequality.
- **D2 (A4).** Two causes: (i) the L-adic staircase test field understates the true profile by up to a
  factor L^3 at individual radii, and the understatement is not uniform, so the measured ratios carry a
  staircase artefact; (ii) i ≤ 3 is too few levels for an asymptotic ratio, and the i = 0 → 1 ratio is not
  asymptotic at all (at i = 0 the "block" is a single link and there is no averaging to measure). The
  repair is the **exact** profile (1 + s)^{−3} and i up to 6, with the band test applied to the
  **asymptotic** ratios only, declared here in advance.

Environment, as for ys1: exact `fractions.Fraction`/Python ints, plain `python3 -I`, `nice -n 10`, all
thread variables = 1, no numpy, no BLAS, single thread, **no numeric lock**. d = 4, L = 3.

## Objects (unchanged definitions, exact profile)

Test field **v(b) := (1 + |b − p|_∞)^{−3}** exactly (the admissible profile of BFT_A §38.7 with C_0 = 1,
no staircase). p := c_X + e_0.
- **LI_i** := (Q_str^{(0→i)}v)(Y_i, 0), the block-averaged axial line integral at the level-i link nearest p
  (Y_i the level-i avatar of c_X).
- **LImax_i** := max over **all** level-i links in the level-(i+1) block of c_X of |Q_str^{(0→i)}v| — this is
  the object the analytic bound of YSUP target Y2 actually uses.
- **BA_i** := n_i^{−d}Σ_{|z−p|_∞≤(n_i−1)/2}v(z), n_i = L^i, the full normalised block average.

## Checks and pre-registered verdicts

**B1 (repaired A2 (c)).** For i = 0,…,4: **PASS** iff ‖K_i‖_1 ≤ L^i·L^{−d}Σ_{y∈B}|y − c_X|_1 for every i,
and the sup clause max_b|K_i(b)| ≤ L^{i(1−d)} continues to hold. **FAIL** if either is violated at any i.
*Power:* **MEDIUM.** The inequality is the derivable statement; a violation would refute the one-step
ℓ¹ and ℓ^∞ gains on which YSUP's level-i bound rests. It can fail.

**B2 (repaired A4 — THE DISCRIMINATING CHECK).** Compute LI_i, LImax_i, BA_i exactly for i = 0,…,6.
Form ρ^X_i := −log_L(X_{i+1}/X_i). The band test is applied **only to i = 3, 4, 5** (the three highest
available ratios); i ≤ 2 is reported but excluded, for the reason given in D2 (ii) and fixed here before
any number is seen. Bands, applied separately to LI, LImax and BA:
- **(V-2)** if all three ρ lie in **[1.5, 2.5)**;
- **(V-3)** if all three lie in **[2.5, 3.5)**;
- **(V-other)** otherwise — criteria again inadequate, and the analytic claim reported as unsupported.
Pre-registered expectation (YSUP §1.2, YS-F1): **LI and LImax → (V-2)**, **BA → (V-3)**.
**The check can come out either way.** If LI lands in (V-3) the averaging gains one more power than
expected and this session's verdict on the brief's question reverses.

**B3 (the scaled-constant form, an independent read of the same data).** Report LI_i·n_i^2, LImax_i·n_i^2
and BA_i·n_i^3. **PASS** iff LI_i·n_i^2 and BA_i·n_i^3 are each monotone-convergent to a finite nonzero
limit over i = 3…6, within 15% between i = 5 and i = 6. **FAIL** otherwise. This is a stricter and more
informative statement than the band test and is reported alongside it, not instead of it.
*Power:* **HIGH.** A wrong power shows up as a drift by a factor L per level, which 15% cannot absorb.

**B4 (does the funnel series terminate for the compactly supported witness?).** ys1 found φ_3 = 0 exactly
for u = ⅛d*δ_p at k = 3 (**that number is from ys1 and is quoted, not assumed**). Compute φ_4 and φ_5 at
k = 5 for the same u. **PASS** iff φ_1, φ_2 at k = 5 again equal their k = 2 values divided by 8
(covariance), **whatever** φ_3, φ_4, φ_5 turn out to be; the values of φ_{≥3} are reported as COMPUTED and
carry no PASS/FAIL. **FAIL** if covariance fails.
*Power:* **MEDIUM-HIGH for the covariance clause** (a wrong off(5) fails it); the φ_{≥3} values are
measurements, not gates, and are labelled so.

**B5 (DESIGNED-FAIL CONTROL, repeated for the new pipeline).** Recompute B2's LI_1 with the longitudinal
multiplicity of the composite Q_str stencil replaced by the constant 1 (i.e. forgetting that an axial line
integral **sums** rather than averages along its direction). **PASS of the control** iff it gives a value
differing from B2's LI_1. If it agrees, the new pipeline is insensitive to the one feature the whole
argument turns on and B2 is void.
*Power:* this check **is** the power measurement for the new pipeline.

## What ys1b cannot test (unchanged from ys1, restated)

1. Nothing nonabelian; the model is scalar and complete only for fibre-componentwise statements at the
   trivial background (BFT_B §24.0, §16.1 (f)).
2. No response field is computed; v and u are stand-ins for the **profile class**, and whether Y^p_{*,0}
   has that core is a named input (BFT_A §38.7).
3. k ≤ 5; no level-count statement, and nothing here bears on the upstream factor k of RS10-1.
4. λ^E is not computed; the box-dipole face stays ARGUED.
