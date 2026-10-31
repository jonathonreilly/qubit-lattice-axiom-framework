# x7 criteria (session 8; written 2026-10-28 before checks/x7_*.py exists, after EXISTENCE §17.0)

Purpose: support or contradict the leading-order (g⁴) structure of the weak-coupling lower bound (WC) of §17 for the
simplest member of the class of level-(K - m_*) measures (SU(2) Wilson action on a fixed periodic torus, depth 0, no
polymers), including toron (flat, non-trivial holonomy) sectors. Informational support only; no counted item rests on x7.

Conventions. SU(2), action β Σ_p s(U_p), s = 1 - ½Re tr U, g² := 4/β. Leading order: U_p = exp(i Σ_a X^a σ^a/2), s ≈ |X|²/8,
per colour a Gaussian lattice Maxwell field with curvature covariance g²Π (Π = projector onto exact 2-forms; Π^φ in the
twisted sector with boundary phases φ = (φ_0..φ_3) for the charged complex component W = x¹ + i x²; neutral a = 3 is
untwisted in every toron background of the maximal torus).

## A (exact, deterministic)
- A1: twisted-momentum formula for Π^φ(p, p') against a dense pseudo-inverse d(d†d)^+d† on a 4⁴ torus, for φ = 0 and
  φ = (0.7, 1.3, 0, 2.1): max |difference| < 1e-10.
- A2: projector identities on the 8×4³ torus: Σ_{p'}|Π(p,p')|² = Π(p,p) to 1e-10 (φ = 0 and one generic φ); mean_p Π(p,p) =
  (3V - 3)/(6V) for φ = 0 and 1/2 for φ with all φ_μ ∉ 2πZ, to 1e-10.
- A3: on the 8×4³ torus, for slice-averaged spatial plaquettes at time distance d = 1 (adjacent slices, the link-reflection
  pair) compute Λ_0 := (1/|S|²)ΣΣ Π^0(p,p')² and Λ_ch(φ) := (1/|S|²)ΣΣ |Π^φ(p,p')|² on the grid φ_μ ∈ {0, π/2, π, 3π/2}
  (256 points). Leading order: g^{-4}C_LO(φ) = (Λ_0 + 2Λ_ch(φ))/32. Define LB := Λ_0/32 (neutral only, valid in every
  sector), UB := max_φ(Λ_0 + 2Λ_ch(φ))/32 + (range_φ h)²/256, h(φ) := mean_p(Π^0(p,p) + 2Π^φ(p,p)) (the second term bounds the
  sector-mixture variance (g⁴/64)Var(h)). A3 PASS iff LB > 0. Report min/max over the grid.

## B (Monte Carlo; SU(2) Wilson, T_0 = 8, T_s = 4, periodic; heatbath + 3 overrelaxation per sweep; cold start;
1000 thermalisation sweeps; 8000 measured sweeps; fixed seeds; β ∈ {8, 16, 32})
- Observable: Φ(t) := mean over the 3·4³ spatial plaquettes at time t of s(U_p). C(d) := mean_t Cov(Φ(t), Φ(t+d)), d = 1
  (OS norm for the link reflection; ≥ 0 by RP) and d = 2 (informational). SE by jackknife over 40 bins.
- R := C(1)/g⁴ = C(1)β²/16, with SE_R.
- B0 (sanity): at β = 32, |⟨s⟩β - 0.75| < 0.1 (weak-coupling value 3/(4β)).
- B PASS iff B0 holds and, for β = 16 and β = 32: C(1) > 5 SE and 0.5·LB ≤ R ≤ 1.5·UB.
- B FAIL iff at β = 32: R < 0.5·LB - 3SE_R, or R > 1.5·UB + 3SE_R, or C(1) < -3 SE.
- Otherwise B INCONCLUSIVE. β = 8 and d = 2: informational only.
- Expected sources of deviation (stated in advance): corrections of relative order g² (perturbative) and possibly larger,
  non-analytic ones from the constant (zero-momentum) modes, whose action is quartic; the tolerance 0.5-1.5 is not
  designed to absorb corrections larger than 50%.

## Resources
Under the numeric lock (mkdir; rmdir exactly once after the run; no trap), nice 10, OMP/OPENBLAS/MKL/VECLIB threads 1,
`python3` without -I, no `timeout`, load < 8 before start. Target < 15 min wall, < 500 MB.
