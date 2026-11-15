# bb5 criteria (lane B session 5; written after BFT_B.md §15 and before checks/bb5_lift.py)

Purpose: test (R2) of REVIEW_BFT_B_S4 Part E numerically — does a linearised one-level refinement keep C^{1,α} bounds
(coarse units) across levels? — and exhibit Lemma CL-blk's mechanism in the linearised corner-lift + descent chain.
Model only: d = 2, abelian, one real component, L = 3, trivial background. No lane-A norm is computed exactly, no
k-uniform constant is tested; all quantities are proxies named below. No constant derived in this session enters any
threshold; the thresholds are predictions fixed here before the script exists.

## Model
- Top level: coarse torus side T = 6, spacing 1 (coarse units). Level l has spacing ρ = 3^{-m} at depth m, N = 6·3^m sites per
  axis. Roots: the fine root of coarse site i is fine site 3i (block of i = {3i-1, 3i, 3i+1}).
- Top data: (I) random 1-form B (iid N(0,1) per link, seed 20261028), divided by max|B| (so ||B||_∞ = 1); (II) pure gauge
  B = dμ, μ iid N(0,1) (seed 20261029), divided by max|dμ|.
- Pairs (Construction CP of BFT_B §15.0), 1D masks s (interpolatory at roots, reproducing constants):
  W = linear interpolation (Q1/Whitney pair); DD4, DD6, DD8 = ternary Lagrange interpolation on 4/6/8 nearest coarse
  points (Deslauriers-Dubuc type); CS = periodic cubic-spline interpolation (global). s^{[1]} derived via Δ_f s = s^{[1]} Δ_c
  (on the zero-mean part through a periodic potential; the mean part refined uniformly, i.e. each fine link gets 1/3).
  S_0 = s ⊗ s, S_1 on μ-links = s^{[1]} (direction μ) ⊗ s (other direction).
- Φ-chain: linear corner lift C (coarse link value on the 3 face-crossing fine links of its block pair, other fine links 0),
  then N = 18 steps of A ↦ A - τ P_c d*dA, τ = 0.1, P_c = 1 - Q_ax^T Q_ax/3 (orthogonal projection onto ker Q_ax).
- Q_ax: coarse link (I, μ) ↦ sum of the 3 fine μ-links on the straight line from fine root 3I to 3I + 3e_μ at the root row.

## Measured per depth m = 1..5 (coarse units: x^c = fine link value / ρ)
- P0 = max|x^c|; P1 = max|∇^c x^c| (forward differences / ρ, both components, both directions);
- P2 = Hölder proxy of ∇^c x^c at α = 1/4: max over components, difference direction, shift axis and shifts δ = ρ·3^t ≤ 1
  of max_z|G(z + δe) - G(z)|/δ^α (axis shifts, pointwise type; a lower-bound proxy of the pointwise Hölder seminorm);
- P3 = C^{1,1} proxy max|∇^c∇^c x^c| (second forward differences / ρ²);
- F0 = max|f^c| (curvature f^c = plaquette sum / ρ²), F1 = Hölder proxy of f^c (as P2) — gauge invariant.

## Criteria (verdict = all of B5-1..B5-5)
- **B5-1 (identities).** For W, DD4, DD6, DD8, CS, at every depth: max|S_1 dμ - d S_0 μ| ≤ 1e-11, max|ev S_0 μ - μ| ≤ 1e-11,
  max|Q_ax S_1 B - B| ≤ 1e-11 (relative to the input sup); for the Φ-chain: max|Q_ax A - B| ≤ 1e-11 at every level.
- **B5-2 (Q1 control, prediction CL-F3).** For W on input (I): P1(m = 5)/P1(m = 2) ≥ 10.
- **B5-3 (global spline bounded).** For CS on input (I): each of P0, P1, P2 satisfies 0.8 ≤ P(5)/P(3) ≤ 1.25.
- **B5-4 (a local C^{1,α} pair exists).** At least one of DD4, DD6, DD8 satisfies B5-3's condition on input (I).
- **B5-5 (CL-blk mechanism).** Φ-chain on input (II): max|Φ-chain(dμ) - d(C_0-chain μ)| ≤ 1e-11·max|dμ-chain| at every level
  (the descent does not touch the gauge part), and P1(m = 5)/P1(m = 2) ≥ 10.

## Informational (no verdict; predictions stated)
- DD4 alone (prediction CL-F2, a guess): its P2 grows (P2(5)/P2(3) > 1.25); DD6, DD8: bounded.
- Φ-chain on input (I): curvature F0, F1 per depth (guess: F1(5)/F1(3) ≤ 1.5, bounded curvature Hölder); P1 per depth.
- P3 per scheme per depth.

## Resources
One process, nice 10, single-threaded BLAS, < 1 GB, < 20 min, under the numeric lock; load < 8 and memory ≥ 30% free checked
before running.
