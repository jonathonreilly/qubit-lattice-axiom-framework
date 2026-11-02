# al55_ax — criteria (written before the script; ALIGN55.md §5.2, Proposition AX-SEAM)

Purpose: exact verification of the seam identity of the multiscale axial-in-blocks gauge and of the growth of its seam values for a field
of constant curvature. Python fractions/ints only; `python3 -I -B`; stdout only. One real component.

## Model
d = 2, L = 3, T = 1, k = 2, 3, 4 (level-0 sides 9, 27, 81). Λ_ax: λ_k := 0 at the level-k root; λ_l(y) := λ_{l+1}(Y) − τ_l(x_l)(Y, y) for y in
the level-l block of Y, τ_l the average over the 2 coordinate orders of the axial line integral of x_l inside the block (Dimock eq. (27)
transcribed to the chain). Chains: (a) x = Ξ_1ν (random ν ∈ Λ_0); (b) the constant-curvature chain: x_l(b) := ∫_b w (exact line integral over
the straight level-l link b) of the linear 1-form w = (0, F·u_1) in coarse coordinates u (curvature F = 1), restricted to a region that does
not touch the torus wrap seam used (the seams tested lie inside one level-(k−1) block of the central level-k cell).

## PASS criteria
- X1: Λ_axΞ_1ν = −ν (2 random ν), and ev^{(l)}Λ_axx depends only on x_l..x_{k−1} (random perturbation of x_0 leaves level-1 values unchanged).
- X2 (identity): for every level-0 link b = (y, y′) whose hierarchical paths share their top root at level s ≤ k − 1, the representative value
  (x + Ξ_1Λ_axx)_0(b) equals −(Φ_0(y′) − Φ_0(y) − x_0(b)) computed independently as a loop sum of x along the two hierarchical paths.
- X3 (growth): for the constant-curvature chain, on the level-0 link crossing the seam between the two central level-(k−2) blocks of the
  central level-(k−1) block (s = k − 1), the coarse representative value |rep^c| = |rep_own|/ρ_0 satisfies |rep^c|/L^{k−3} equal to the same
  nonzero rational for k = 3 and k = 4 (exact scaling ρ_{k−1}ρ_{k−2}/ρ_0 = L^{k−3}), and |rep^c| strictly increases from k = 3 to k = 4.

## Controls (must FIRE)
- XC1: for the pure-gauge chain (a), every seam value of the representative is 0 (the identity's right side vanishes) — i.e. the growth in X3
  is not produced by the code for a flat field; this control FIRES if the pure-gauge seam values are all exactly 0 while X3's are not.
- XC2: replacing the permutation average by order (1, 2) only changes the X3 value (the average matters), or leaves it unchanged — recorded
  either way as INFO; the control that must fire is XC1.

## What this check cannot decide
d = 4 constants; that the growth persists for every k (only k = 3, 4 are computed; the exact scaling is the proof's job); fields other than
the linear one.

## Amendment A1 (appended 2026-10-29, after the text above and BEFORE any al55_ax script exists)
Reason: X3's "same rational for k = 3 and k = 4" is not implied by the argument (the loop area is the top-fan area, which scales exactly,
plus lower-level descents, which do not scale exactly). X3 and the controls are replaced by:
- X3′: |rep^c(k = 4)| ≥ (L/2)·|rep^c(k = 3)| > 0 (exact rational comparison), on the link defined in X3; the values rep^c/L^{k−3} are printed
  for k = 2, 3, 4 as INFO.
- X4: for the pure-gauge chain (a), every level-0 seam value of the representative is exactly 0.
- XC1 (must FIRE): computing X2's loop sum with the order-(1, 2) axial path only (no permutation average) gives a different value from the
  averaged one for the curvature chain on at least one tested seam link (the identity is sensitive to the averaging, so X2 is not vacuous).
