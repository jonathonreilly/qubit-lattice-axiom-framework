# ba4 criteria (BFT lane A, session 4). Written before checks/ba4_lrl.py exists and before any ba4 run.

Statements tested: BFT_A §16 (PRE-STATED, session 4): LRL (a), Lemma FC (i), Theorem XR. No constant derived in session 4
appears below: every threshold is an a-priori design number chosen to separate logarithmic growth from saturation
(reasons given), not a constant of a session-4 proof. Parameters fixed a priori: L = 3, α = 1/4 (§12.0), κ ≡ 1,
m' ∈ {0.25, 0.5}.

## Quantities
- Q_a (LRL (a) ratio) := [max over level-l links b of (1 + d(b, X_0))^5 |∇^cA^c(b)| + max over boxes B of
  (1 + d_max(B))^5 ρ_B^{-α} Osc_2(∇^cA^c; B)] / [max_z e^{m'd(z, X_0)}|F^c(z)| + max_B e^{m'd_max(B)} ρ_B^{-α} Osc_2(F^c; B)],
  components separately (16 gradient components, 6 plaquette orientations), boxes of lattice side 1..R (ρ_B = side/R),
  all corners; d_max(B) = the largest coarse ℓ¹ torus distance of a point of B to X_0. Numerator and denominator are
  each within a factor 2 of LRL (a)'s left side (over all b) and of Φ_{m'}(F) (sup of a sum vs sum of sups; a box
  containing b has d_max(B) ≥ d(b, X_0)), so Q_a ≥ (LRL (a)'s best constant)/2 on the tested F. A := d*Δ^{-1}F by FFT.
- Q_XR (Theorem XR ratio) := ||r(x(w))||_{X_s,Σ} / (L^{2(k-l)} sup|w|) (k = 1, l = 0: max|r_0| / (9 sup|w|)).
- Q_RP (reviewer's (RP) ratio, informational) := sup|g|/sup|w|, g = dΔ^{-1}w.

## Sanity (exact identities; PASS required)
- S1: FFT Coulomb potential: |dA - F|/|F| ≤ 1e-10 and |d*A|/|A| ≤ 1e-10 for every F used.
- S2 (duality, Lemma 6.6 as used in Theorem XR): |κr_0(X, μ) - ⟨w, B'_0⟩| ≤ 1e-8·|⟨w, B'_0⟩| + 1e-12·sup|w|, for the
  designed w (B' = source-free response to the unit datum at (X, μ)).
- S3 (Lemma FC (i) + roughness): ⟨w, Q_0^T𝔽^{(0→1)}A⟩ ≤ 1e-10·sup|w|·Σ|Q_0^T𝔽A| (A := Π_cc B'_0), and
  |d*𝔽A|/|𝔽A| ≤ 1e-10.

## Trend criteria (the tested claims: no growth with T or with depth)
Design reason: if a quantity behaves as a + b log T with b > 0, successive increments at T = 2 → 3 → 4 → 5 have ratios
log(4/3)/log(3/2) = 0.71 and log(5/4)/log(4/3) = 0.78; at T doubling (2 → 4 → 8) the increments are equal (ratio 1);
at R tripling (3 → 9 → 27) equal (ratio 1). Saturation of the form a - bT^{-p} with p ≥ 2 gives ratios ≤ 0.46
(T = 3 → 4 → 5). Threshold 0.5. A sequence passes if its last increment Δ_last obeys Δ_last ≤ 0.5·|Δ_prev| + 0.01·Q_first
(which also passes any non-increasing tail). A FAIL means "log growth not excluded", not "log growth shown".
- T1 (D1, LRL (a) on data responses, k = 1, l = 0, T = 2, 3, 4, 5; each m'): Q_a passes.
- T2 (D2, Theorem XR, k = 1, T = 2, 3, 4, 5): Q_XR passes for the XR-designed w (P_R sign(P_R B'_0)) and for the
  reviewer's RP-designed w (P_R sign(P_R K), rev3_probe P3).
- T3 (D3, LRL (a) on synthetic exact F by FFT): for each smooth or Hölder family (S-bump, S-cusp; definitions in the
  script docstring): Q_a at R = 3, T = 2, 4, 8 passes (doubling rule), and Q_a at T = 1, R = 3, 9, 27 passes (tripling
  rule).
- Informational (no criterion): Q_RP on both designed families (expected to grow, as the reviewer saw); D1 at
  (k, T) = (2, 2), l = 0, 1; S-jump (degree-0 discontinuous F, outside LRL (a)'s Hölder class in a k-uniform way) and
  S-noise; the Lemma FC (ii) ratio max|A - Q_str^T𝔽A| / (L·max|∇A|).

## Limits (stated in advance)
k ≤ 2 for chain responses; small tori; L = 3 only; finite-size trends from 3-4 points cannot prove uniformity. Jobs
< 20 min, < 1 GB, under the numeric lock.
