# p5 criteria (lane E, session 5; written 2026-10-28 ≈11:33 UTC, AFTER PLD.md §17.0 (pre-statement, 11:22:35 UTC) and the
[RPLD4-fix] edits, BEFORE any written session-5 derivation in PLD.md and BEFORE checks/p5_pld.py exists)

Order disclosure: the session-5 derivations exist only as an unwritten sketch when this file is written (exact law conversion
under HW's (E1) law; a kernel-centre form of DIL-1; a split of (J-NS^dir) by defect type; a dilution constant of the S4' centre
map). Part B is a computation whose outcome is NOT known when this file is written; its decision rule is fixed here. No
criterion is edited after the run; any change is disclosed in p5_time.txt.
Scope: geometry and linear algebra of the S4' map (abelian linearisation), elementary SU(2) inequalities, arithmetic. Nothing
here tests (CLS-min), (SF-cap), (LCR), (SC)_k, the R-operated representation or any lattice measure.
"Exact" = rational arithmetic (fractions.Fraction); "numerical" = floating point with the stated tolerance; "evidential" =
sampled.

## Geometry (fixed)
d = 4, L = 3. Fine lattice Z⁴; block B(X) = 3X + {0,1,2}⁴, centre c_X = 3X + (1,1,1,1). Coarse plaquette P = (X = 0; μ = 1st axis,
ν = 2nd axis), coarse links c_1 = (0, e_μ), c_2 = (e_μ, e_μ + e_ν), c_3 = (e_ν, e_μ + e_ν), c_4 = (0, e_ν);
F_P := A_{c_1} + A_{c_2} - A_{c_3} - A_{c_4}. S4' family of a coarse link c = (X, X + e_α) (PROOF S4'): for every order σ of the 4
axes and every y ∈ B(X): T^σ_y = P^σ(c_X → y)·(3 straight steps from y along α)·P^σ(c_{X+e_α} → y + 3e_α)^{-1}, P^σ the complete
axial path moving the coordinates in the order σ. Linearisation: A_c := (1/(24·81))Σ_{σ,y}Σ_{steps of T^σ_y} ±A_e (sign by the
traversal direction). W := the vector of coefficients of F_P on the fine links (F_P = Σ_e W_eA_e), computed exactly.
f_c(e) := (1/1944)·Σ_{σ,y}(number of traversals of e by T^σ_y); F_c := Σ_e f_c(e)²; F_* := max_{c∈∂P}F_c.
int x := the fine links with both endpoints in the block x. Plaquette curvature (abelian) φ_p(A) := Σ_{e∈∂p}±A_e.

## B. Dilution of the linearised S4' centre plaquette (the T14 (B) computation)
- B1 (exact) Gauge invariance: for every fine site s, Σ_{e out of s}W_e - Σ_{e into s}W_e = 0. PASS iff 0 at every site.
- B2 (exact) Locality: W_e ≠ 0 only for links e with both endpoints in B(X') ∪ B(X'') for some c = (X', X'') ∈ ∂P.
- B3 (exact, positive control) Uniform field in the (μ,ν)-plane, A_μ(x) := -b·x_ν, all other components 0 (φ_p = b on every
  (μ,ν)-plaquette, 0 on all others): F_P = 9b exactly (b = 1). PASS iff equal.
- B4 (exact, negative control) Ten random integer gauge functions χ supported on the sites of one corner block, A = dχ:
  F_P(A) = 0 exactly. PASS iff all ten give 0.
- B5 (numerical; reported) For each corner block x of P separately and for the union U4 of the four corner blocks:
  - R_∞(x) := max{W·A : A supported on int x, |φ_p(A)| ≤ 1 for every fine plaquette p containing a link of int x} (LP,
    scipy HiGHS); reported together with the dual objective; PASS iff primal and dual agree to 1e-7 relative (numerical
    certificate of optimality) and the maximiser satisfies the constraints to 1e-9;
  - R_2(x) := max{W·A : A on int x, Σ_pφ_p(A)² ≤ 1} = ||P_x W||, computed by least squares (W restricted to int x must lie in
    the row space of the curvature map; residual reported, PASS iff ≤ 1e-9·||W||);
  - max_{e∈int x}|W_e|, and F_* (exact).
- B6 (decision rule, fixed now; evaluated on R_∞(U4), the response to a perturbation supported on all four corner blocks):
  - R_∞(U4) < 1/4: "simple split viable" (a defect of max curvature X moves the centre plaquette by ≤ X/4 at linear order);
  - 1/4 ≤ R_∞(U4) < 1 - 1/√24 - 0.05 (≈ 0.746): "refined split only" (thresholds (τ, s) of the §17 derivation needed);
  - R_∞(U4) ≥ 0.746: outcome (NP-F5) of §17.0 MET at linear order (no dilution in the needed sense).
  The rule is reported, not "PASS/FAIL"; B6 cannot fail.
- B7 (negative control for B5's LP; must behave as stated, else FAIL) Replacing W by the indicator of a single straight
  transporter's links between two block centres (a functional that is NOT gauge invariant) makes the LP unbounded or gives a
  value ≥ 10 (no curvature bound controls it). PASS iff unbounded or ≥ 10.

## C. Elementary SU(2) statements of §17 (sampled)
- C1 (evidential; 300 samples) DIL-L (i): for the actual S4' family of c_1 and random SU(2) fields U on the links of B(0) ∪ B(e_μ)
  (half Haar, half within 0.3 of 1), and U° := U with a random subset E of the links replaced by independent random elements:
  ||M̄_{c_1}(U) - M̄_{c_1}(U°)||_op ≤ Σ_e f_{c_1}(e)||U_e - U°_e||_op + 1e-12. PASS iff 0 violations.
- C1n (negative control; must FAIL somewhere) the same with f_{c_1}/2 in place of f_{c_1} is violated in some sample.
- C2 (evidential; 20000 samples) KS (a) identity used by DIL-L (iii): for M = rŴ (Ŵ Haar, r ∈ (0, 1]) and V Haar,
  r - ½Re tr(V^{-1}M) = r||V - Ŵ||²_op/2 to 1e-12.
- C3 (evidential; 20000 samples) the centre-moving arithmetic of §17: for unitaries Ŵ_i, Ŵ°_i (i = 1..4),
  | ||1 - Ŵ_1Ŵ_2Ŵ_3^{-1}Ŵ_4^{-1}|| - ||1 - Ŵ°_1Ŵ°_2Ŵ°_3^{-1}Ŵ°_4^{-1}|| | ≤ Σ_i||Ŵ_i - Ŵ°_i|| + 1e-12.

## A. Arithmetic (exact where stated)
- A1 (exact) 5/256 = (5/8)·(1/16)/2 (the threshold constant of the centre-moving criterion).
- A2 (numerical) With F_* from B5, r_* = 1/2, λ = 1/2, c_pr = 1/1797760 (exact), θ = 1/24: κ_eg := the least κ with
  λκ·r_*·(5/256)²/(2F_*) ≥ θc_pr; reported.
- A3 (numerical) With R = R_∞(U4) from B5: for τ ∈ {0.05, 0.1, 0.2} and s = 1/√24, the threshold-growth factor
  γ(τ) := (1 - τ - s)/R; reported (a value > 1 means a centre-moving defect must exceed ε_1 by the factor γ).
