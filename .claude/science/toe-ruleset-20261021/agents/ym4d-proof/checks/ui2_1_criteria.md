# ui2_1 — criteria (written 2026-10-29T06:42:08Z, BEFORE any ui2_1 script exists)

Object. The scalar IR integral of the super-marginal EOM bubble of UIR2_55 §1.4 (two massless scalar gauge lines Δ^{-2} with
one-derivative EOM vertices E·K, E ⊥ P):  I_1 := ∫_{R⁴} z_1² / (|z|⁴ |z + e_2|⁴) d⁴z.  Claim to test: I_1 = π²/2 (finite, nonzero).
Arithmetic: sympy exact (rationals, π symbolic) only; no floats in any verdict.

PASS conditions (all must hold):
- L1 (route R1, Feynman parameters): with 1/(A²B²) = 6∫_0^1 x(1−x)(xA + (1−x)B)^{-4}dx, shift z → z − x e_2, and the 4D radial
  formula ∫d⁴z f(z²) = π²∫_0^∞ t f(t)dt, sympy returns exactly π²/2.
- L2 (route R2, hyperspherical + Gegenbauer): I_1 = (4π/3)∫_0^∞ r J(r) dr with J(r) = ∫_0^π sin⁴θ (1 + 2r cosθ + r²)^{-2} dθ.
  (a) ∫_{-1}^{1} C_n^{(2)}(c)(1 − c²)^{3/2} dc = 0 exactly for n = 1, …, 8 and = 3π/8 for n = 0;
  (b) sympy's exact J(r) at r = 1/2, 1/3, 2, 3 equals 3π/8 (r < 1) resp. 3π/(8r⁴) (r > 1);
  (c) the assembled value (4π/3)(3π/8)(½ + ½) equals π²/2 exactly and equals L1's value.
- L3 (homogeneity used in the text): the substitution K = |P|z turns ∫d⁴K (E·K)²|K|^{-4}|K + P|^{-4} (E ⊥ P, |E| = 1) into |P|^{-2} I_1
  (checked symbolically on the integrand's scaling degree: 2 − 8 + 4 = −2).
Designed-FAIL controls (each must FAIL, i.e. the comparison it makes must come out false / the finiteness test must fail):
- Cc1: the same L2 assembly compared with the wrong target π²/4 → must FAIL.
- Cc2: the longitudinal numerator z_2² (vertex parallel to P): J_2(r) = ∫_0^π cos²θ sin²θ (1 + 2r cosθ + r²)^{-2} dθ evaluated exactly
  at r = 1 − 1/N, N = 10, 100, 1000; the finiteness test "N·J_2 stays bounded by 10·(first value)" must FAIL in the sense that
  (1 − r)J_2(r) tends to a nonzero constant (non-integrable 1/|1 − r| singularity ⇒ divergent I_2). PASS of the control = divergence seen.
- Cc3: the marginal analogue with one scalar line replaced by a 1-form line, ∫ z_1²|z|^{-4}|z + e_2|^{-2}: its large-|z| integrand
  is |z|^{-4}·(angular), so the radial integral to R grows like log R; the test "finite as R → ∞" must FAIL (checked exactly on the
  angular average at large r).
What this check cannot decide: anything about the lattice, the colour factor, or the sign of the full bubble; it decides only that
the super-marginal integral is finite and nonzero (so Term B contributes at order P² unless cancelled), and its exact value.
