# bb1 criteria (BFT lane B; written before the script checks/bb1_decay.py)

Objects (d = 4, L = 3, κ ≡ 1 unless stated, one real colour component; the trivial background, level 0 → 1):
- C^0 := Õ_0^{-1} - (1 - Π), Bloch fibres as in checks/c37_kcurv.py (class Fib, imported unchanged).
- **a_S** := κC^0Q^T (Lemma SC1's representative of the branch tangent ∂U_0/∂V_1 at V = 1; c37 D2's "a'").
- **a_B** := J + x∘d_1, x := -C^0d^*ι (Lemma BR1's representative: lift plus displacement, CURV-lin (i)).
- **H_1** := -κ𝒦_ρd_1 = -κ(Qx)d_1 (Corollary H-fac: ∂²E_1^br at V = 1).
- Kernels k(S)[r, c] on the coarse side-T torus (fine link r of cell 0, coarse link c of cell S); P(s) := max |entry| over
  the cells S at coarse ℓ^∞ torus distance s; local rate r_s := log(P(s)/P(s + 1)).

Criteria (pre-registered):
- **A1 (gauge equivalence of the two representatives; not a tautology: two different formulas).** At T = 8, over all
  fibres: max|d(a_S - a_B)| ≤ 1e-6·max|a_B| and max|Q(a_S - a_B)| ≤ 1e-6·max|a_B| (fibre level, complex128 solves).
  (Both are tangents of the same branch; they may differ only by fluctuation-gauge directions D λ, λ(c_X) = 0, which d and Q
  annihilate.)
- **A2 (cross-check against c37 D2).** At T = 8: max row ℓ¹ sum of a_S = 2.848907 and max column ℓ¹ sum = 156.078934
  (c37D.out), each within 1e-4 relative.
- **A3 (exponential decay, torus-stable).** For each of a_S, a_B, H_1: at T = 10, r_2 ≥ 0.5 and r_3 ≥ 0.5; and for s ≤ 3,
  P_{T=8}(s) and P_{T=10}(s) agree within 10% relative. Recorded prediction (not a criterion): the rates approach ≈ 1 per
  coarse unit (LINEAR_PACKAGE §4 located rate 0.98-1.04 at κ = 1; c36 D3 H_1 ≈ 1.02).
- **B (informational).** κ = 0.25 and 4 at T = 8: r_2, r_3 for a_B and H_1, against the located rates 0.50 / 2.46. Weighted
  row sums N_μ(a_S), μ ∈ {0.5, 1.0}, coarse ℓ¹ distance of S, T = 10.

Limits: one job at a time under the numeric lock; nice 10; BLAS threads 1; peak memory < 1 GB; < 20 min.
