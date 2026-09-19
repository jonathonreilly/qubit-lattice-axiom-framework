# no-waves-under-positive-formation, attempt 2 (worker w-macbookpro90c72-j80c2, model grok-4.6)

## (1) The statement attempted

**Theorem.** Let `λ(k) = Σ_{z ∈ F} w_z e^{ik·z}` with `w_z > 0`, `Σ w_z = 1`, `F ⊂ Z^d` finite
(gain-one linear formation from a finite positive predecessor set). Then
`|λ(k)| ≤ 1` for all `k`, with equality at `k ≠ 0` if and only if `e^{ik·z}` is
constant on `F` (the *collinear exception*: `F` lies in a coset of a hyperplane
`k·z = const`). Near `k=0`, `λ(k) = 1 + i v·k − (1/2) k^T (E zz^T) k + O(|k|^3)`
with `v = E[z]`, and the Hessian of `|λ|^2` at `0` is negative semidefinite
(equal to `−2 Cov(z)`), so the mode is drift plus diffusion, never a wave
`|λ|=1` with `arg λ = c|k|`.

**Exception (collinear).** Two-point `F={0,e_1}`, `w=1/2`:
`|λ|^2=(1+cos k_1)/2`, equal to `1` for all `k` with `k_1=0`.

**Negative weights.** `λ=2−e^{ik_1}` has `|λ|^2=9` at `k_1=π` (amplification).
Positivity of overlap weights is the axiom cost of ruling this out.

**7-stencil.** `λ=1−E/7`, Hessian of `|λ|^2` at `0` is `−4/7` on each axis.
Backward 4-stencil has drift `∂λ/∂k_j|_0 = i/4`.

## (2) Steps

**Step 1 — Jensen (PROVED).** `λ(k)=E[e^{ik·Z}]` for a random `Z` with law `w`.
`|E e^{ik·Z}| ≤ E 1 = 1`, equality iff `e^{ik·Z}` is a.s. constant.

**Step 2 — 7-stencil (CHECKED as E0, E2, E4).** `λ=1−E/7`; at `(π,0,0)` equals
`3/7`; series `1 − k_1²/7 + O(k^4)`; Hessian of `|λ|^2` at `0` is `−4/7`.

**Step 3 — collinear exception (CHECKED as E1).** Two-point formula;
`|λ|=1` on the plane `k_1=0`.

**Step 4 — negative weights (CHECKED as E3).** `2−e^{ik}` at `π` has modulus `3`.

**Step 5 — drift of the backward stencil (CHECKED as E2d).** `i/4`.

## (3) First failing step of a wave claim under positivity

Step 1: `|λ|≤1` forbids a propagating pole on the unit circle except the
collinear exception, which is not an isotropic light cone (`arg λ = c|k|`).

## (4) What would finish it

A spinor/unitary overlap (complex weights with `|Σ w|=1` and `|λ|=1` on a cone)
costing real records and positivity; or a second earlier level with a
*positive* weight that is not a convex combination of one-level hops (still
`|λ|≤1` by the same Jensen if all weights are a probability on spacetime
points). Conserved quantities do not by themselves produce `|λ|=1` off `k=0`
unless they force the collinear exception.

Nothing here edits notes or runners.
