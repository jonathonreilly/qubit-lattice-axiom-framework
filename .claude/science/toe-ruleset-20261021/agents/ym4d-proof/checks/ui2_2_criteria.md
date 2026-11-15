# ui2_2 — criteria (written 2026-10-29T06:48:26Z, BEFORE any ui2_2 script exists)

Exact rational arithmetic only (fractions / sympy Rational); no floats.
Part A — Lemma VS (iv) linear algebra (UIR2_55 §1.1). Random rational SPD 𝒞 (n = 7), random rational D (7×3, rank 3), Π :=
𝒞^{-1} − 𝒞^{-1}D(DᵀC^{-1}D)^{-1}Dᵀ𝒞^{-1}, X := Π + DDᵀ, B a rational basis (columns) of E = ker Dᵀ; random rational M (7×5), H
(5×5 symmetric), G (5×5 symmetric PSD, the fine gauge-fixing stand-in).
- A1: ΠD = 0.  A2: X invertible and ΠX^{-1}Π = Π.  A3: det X · det(Bᵀ𝒞B) = det(DᵀD) · det(BᵀB)  (i.e. ½log det X = −½log det_E(P𝒞P)
  + ½log det′(DDᵀ)).  A4: with Z := H + MᵀΠM + G, Y := −MᵀΠ: Z − YX^{-1}Yᵀ = H + G.
- Designed-FAIL Ac1: the same A1 and A4 with Π replaced by 𝒞^{-1} must FAIL.
Part B — the exact gauge-row identity (UIR2_55 §1.4) for an off-shell gauge-invariant function. SU(2) as unit quaternions with
rational entries (Cayley parametrisation q = ((1 − |w|²), 2w)/(1 + |w|²), w ∈ Q³); 2D periodic lattice 2×2 (8 links, 4 plaquettes);
f(U) := Σ_p (1 − Re U_p); right-trivialised chart U_b e^{X_b}, X_b pure imaginary rational quaternions; H[X, Y] := ∂_t∂_s f(U e^{tX+sY})|_0,
F[Y] := ∂_s f(U e^{sY})|_0 (exact via truncated exponential series); (D_Uλ)_b := U_b^{-1}λ_xU_b − λ_y; λ̄_b := U_b^{-1}λ_xU_b + λ_y.
- B1: at a random (off-shell) U, for 3 random pairs (X, λ):  H[X, D_Uλ] = −½ F[[λ̄, X]]  exactly (commutator of quaternions,
  F applied linkwise).  B2: F ≠ 0 at that U (the configuration is off-shell), so B1 is not vacuous.  B3: at U = 1 both sides vanish.
- Designed-FAIL controls (each must FAIL): Bc1 the coefficient 1 in place of ½; Bc2 D_Uλ (a difference, i.e. a derivative vertex)
  in place of λ̄; Bc3 the on-shell form H[X, D_Uλ] = 0 at the off-shell U.
What it cannot decide: anything about the composite map, Π, the infrared matching or the lattice YM determinant; Part B decides only
that the EOM vertex on gauge rows exists, has coefficient ½, and couples λ WITHOUT a derivative (through λ̄), which is the input to the
power count of §1.4 and to the identification in §1.6.
