# nr55_1 — pre-registered criteria (written BEFORE checks/nr55_1.py exists)

Owner: NODEA_RES55.md (Opus 5.5, claude-opus-5-5). Plain python, fractions.Fraction only for every verdict.
No float enters any PASS/FAIL condition. Each gate has a negative control that must FAIL as designed.

## G1 — Proposition GAUSS's arithmetic (NODEA55 C.2 (4); K6)
Compute exactly n_link := 4·8·9³ (level-(k-1) links with both endpoints in a 9⁴-site block), r := 3·n_link, h := r/2.
Enclose ln 2 rigorously by ln 2 = 2·atanh(1/3) = 2·Σ_{j≥0} 3^{-(2j+1)}/(2j+1), truncated after J terms, remainder bounded
by the geometric tail 2·3^{-(2J+1)}/((2J+1)·(1 − 1/9)).
PASS iff n_link = 23328, r = 69984, h = 34992, and the enclosure of h·ln 2 lies inside [24254.5, 24254.7].
Control G1n: the same enclosure computed with PLD §19.5's count h' := 3·n_int·81/2, n_int := 4·2·3³ = 216 (h' = 26244), must
NOT lie in [24254.5, 24254.7] (so the gate distinguishes the two published counts).

## G2 — NO-ONE (i): constant 1 fails for a symmetric strongly log-concave non-Gaussian law
Diamond D := {|x1| + |x2| ≤ 1}, slab K := {|x2| ≤ a}. Exact piecewise-polynomial integration (Fractions):
I0 := ∫∫_D 1, I2 := ∫∫_D x1², J0 := ∫∫_{D∩K} 1, J2 := ∫∫_{D∩K} x1² (inner x2-integral done exactly: section length
2·min(a, 1 − |x1|)).
PASS iff, at a = 1/2: (I0, I2, J0, J2) = (2, 1/3, 3/2, 5/16), Δ := J2/J0 − I2/I0 = 1/24 > 0, AND the weight certificate holds:
J2/J0 > U·(I2/I0) with U := 1 + x + x², x := 1/9 (U ≥ e^{1/9} on [0,1] since e^x − 1 − x ≤ x²(e − 2) ≤ x²).
[Meaning: for the law ∝ e^{−|x|²/18}·1_D (s = 3, Hessian ≥ I/9), d/dt log μ_t(K) at t = 0 under the tilt e^{t·x1²} is
≥ e^{−1/18}J2/J0 − e^{1/18}I2/I0 > 0.]
Controls (each must FAIL as designed):
- G2n-a: a = 1 (K ⊇ D): Δ must equal 0, so "Δ > 0" fails.
- G2n-b: x := 1/4 (s² = 4) with the LOWER bound L := 1 + x + x²/2 ≤ e^{1/4}: the certificate J2/J0 > L·(I2/I0) must fail.

## G3 — NO-ONE (ii): constant 1 fails in the Gaussian model with the n = 1 cluster allowance
Derivative-sign certificate (analytic derivation in NODEA_RES55 §3.3): for threshold ε and noise scale σ, the sign of
d/dσ P(both defective) is certified negative if  e^{−2ε²} > e^{−ε²/(2σ²)}·(1 + e^{−2ε²}).
Certify with rational bounds only: e^{y} ≥ 1 + y (y ≥ 0) and e^{−y} ≤ 1/(1 + y + y²/2) (y ≥ 0).
PASS iff at (ε, σ) = (1, 1/4) the certificate holds using LHS ≥ 1/e²-lower-bound and RHS ≤ upper bounds as above.
Control G3n: at (ε, σ) = (1, 1) the certificate must FAIL (RHS lower bound ≥ LHS upper bound).
Also G3g (exact grid, Fractions): for ε = 1 and all h, g on the grid {k/40 : |k| ≤ 120}, with |h| < ε:
[|g+h| ≥ ε and |g−h| ≥ ε]  ⟺  |g| ≥ ε + |h|. PASS iff no grid point violates it. Control G3g-n: the same identity with
"ε + |h|" replaced by "ε" must show ≥ 1 violation.
CONFIRMATORY (no verdict): float quadrature of P(both defective) at σ0 = 0.10 and σ0' = 0.15, ε = 1 (printed only).

## G4 — the nonabelian cubic vertex (no x ↦ −x symmetry), and the abelian control
SU(2), exact arithmetic in Q(i) with truncated exponentials e^{tX} = Σ_{m≤3} t^mX^m/m!. Plaquette U(t) :=
e^{tX1}e^{tX2}e^{−tX3}e^{−tX4}. Let c3 := [t³](tr U(t) − tr U(−t)).
PASS iff for X1 = iσ1, X2 = iσ2, X3 = iσ3, X4 = 0: c3 ≠ 0 (and [t¹], [t²] of the odd part vanish).
Control G4n: X1 = iσ3, X2 = 2iσ3, X3 = −iσ3, X4 = iσ3 (abelian): c3 must equal 0, so "c3 ≠ 0" fails.
