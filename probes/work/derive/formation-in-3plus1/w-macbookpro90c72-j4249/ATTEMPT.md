# formation-in-3plus1, attempt 3 (worker w-macbookpro90c72-j4249, model grok-4.6)

Plan, locked from the task: mean-field comparison via `A(κ)/κ` decreasing, and a
no-go for chessboard RP as a route to sphere LRO. Linear dichotomy is used only
as the IR envelope of `1/(kᵀ M k)`.

## (1) The statement attempted

Sphere formation on `Z^4` in level order, four predecessors. Langevin function
`A(κ) = coth κ − 1/κ`. Mean-field self-consistency `m = A(4 β m)`.

**Statement.**
- (MF) `A(κ)/κ` is strictly decreasing on `(0, ∞)`. The mean-field threshold is
  `β_c = 3/4` (`A(κ) ∼ κ/3`, so `1 = 4β/3`). For `β > 3/4` the MF map has a
  unique positive fixed point. This is not a proof of LRO.
- (envelope) With `M` of the linear law (eigenvalues `1/16`, `1/4`), one has
  `4 σ²/|k|² ≤ σ²/(kᵀ M k) ≤ 16 σ²/|k|²` for `k ≠ 0`. Linear two-sided IR
  bounds of the form asked in (b), for the linearized kernel only.
- (chessboard no-go) A chessboard / reflection-positivity argument in level
  time does not apply: the formation law is a causal product of kernels, not a
  Gibbs measure with a reflection-symmetric even action. That is the first
  failing step of route (a) via chessboard.

Sphere LRO is not claimed.

## (2) Steps

**Step 1: `A(κ)/κ` decreasing (PROVED; CHECKED as A1).**
Let `u = 2κ > 0` and `h(u) = 4 cosh u − 4 − u² − u sinh u`. Then
`h(0)=h'(0)=h''(0)=h'''(0)=0` and `h''''(u) = −u sinh u ≤ 0`, strictly `< 0`
for `u > 0`. Hence `h < 0` on `(0, ∞)`, which is equivalent to
`(A/κ)' < 0` (CHECK: sympy derivatives and the identity).

**Step 2: MF threshold (PROVED; CHECKED as A2).**
`A(κ) = κ/3 − κ³/45 + O(κ⁵)`. The linearization of `m = A(4β m)` is
`1 = 4β/3`, so `β_c = 3/4`. For `β > 3/4` the function `m ↦ A(4β m)` starts
with slope `> 1` and `A < 1`, so a unique positive root.

**Step 3: linear envelope (PROVED; CHECKED as B1).**
`kᵀ M k` lies between `λ_min |k|² = |k|²/16` and `λ_max |k|² = |k|²/4`.

**Step 4: chessboard (PROVED as a no-go).**
RP chessboard needs an even Gibbs weight, reflection-symmetric across a plane.
The formation kernel `K(s | s_{x−e_1}, …, s_{x−e_4})` is a conditional in a
causal order, not the marginal of such a Gibbs measure. The route stops here
for (a).

## (3) Where the route stops

Step 4 for LRO by chessboard. MF and the linear envelope stand and do not
imply `liminf E[m_t · e] > 0`.

## (4) What would finish it

Block 27's comparison lemma applied to the four-predecessor sphere; a Lyapunov
function for the plane average that uses `A(κ)/κ` decreasing.

Imports: Langevin `A` as the mean of the von Mises–Fisher / sphere kernel
(standard; derivative identities re-proved). Linear `M` as in the dichotomy
(eigenvalues CHECKED).
