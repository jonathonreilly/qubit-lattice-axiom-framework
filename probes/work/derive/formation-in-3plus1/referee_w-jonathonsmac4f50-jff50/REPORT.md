# Referee report: J:derive:formation-in-3plus1:a3

**Referee:** w-jonathonsmac4f50-jff50 (claude-opus-5).

Two attempts were logged under this task id, both by grok-4.6:
- **j4249:** w-macbookpro90c72-j4249, sha `67d01ead`: mean-field threshold, linear envelope, and a chessboard no-go.
- **jb4a1:** w-macbookpro90c72-jb4a1, sha `7776d289`: the return sum `G_2`, `det M`, and the continuum prefactor.

This report referees both. `check.py` in this directory re-verifies every finite fact with independent code (sympy, exact
rationals).

## Attempt j4249

**Step 1 (`A(κ)/κ` decreasing): holds.** `h(u) = 4cosh u − 4 − u² − u sinh u` has `h(0) = h'(0) = h''(0) = h'''(0) = 0`
and `h'''' = −u sinh u`. The identity `κ² + κ sinh κ cosh κ − 2sinh²κ = −h(2κ)/4` makes `h < 0` on `(0, ∞)` equivalent to
`(A/κ)' < 0` (F1).

**Step 2 (mean-field threshold): holds.**
- `A(κ) = κ/3 − κ³/45 + O(κ⁵)`, so `m = A(4βm)` has slope `4β/3` at 0 and `β_c = 3/4`.
- There is exactly one positive root for `β > 3/4`. Uniqueness follows from Step 1 because `A(4βm)/m` is decreasing.
- F2 checks this at `β = 1, 2, 5`, with roots `0.5998`, `0.8536` and `0.9472`.

**Step 3 (linear envelope): holds.** The four-predecessor covariance is `M = I/4 − 11ᵀ/16`, with eigenvalues `1/16` (once)
and `1/4` (twice). So `4/|k|² ≤ 1/(kᵀMk) ≤ 16/|k|²` (F3). This bounds only the linear kernel's small-`k` form, as the
attempt says.

**Step 4 (chessboard no-go): does not follow.**
- The step rests on the claim that the formation law "is not the marginal of such a Gibbs measure".
- That claim is false. On any finite window the law is `Π_x K(s_x | predecessors)`, a product of positive local factors,
  which is a Gibbs measure (block 10's recorded-set Gibbs theorem).
- F6 checks this on a small binary formation window. The one-site conditional of a level-0 site does not depend on a record
  outside its recorded-set neighbourhood.
- A chessboard no-go would have to show that no reflection makes the law reflection positive. The attempt does not examine
  that. Coordinate permutations such as `x₁ ↔ x₂` preserve the predecessor structure, so the question is open.

**Verdict on j4249: first failing step 4.** Steps 1–3 hold.

## Attempt jb4a1

**Step 1 (`G_2`): holds.** `G_2 = 25/24`, both by the Fourier sum on `(Z/2)³`, where `1 − |φ|² ∈ {3/4, 1}`, and by the
real-space Lyapunov solve (F4).

**Step 2 (`det M`): holds.** `det M = 1/256`, with eigenvalues `1/16`, `1/4` and `1/4`. `1 − |φ|² = kᵀMk + O(k⁴)` along
three directions (F3).

**Step 3 (prefactor): holds.** `1/(4π√(det M)) = 4/π` (F5). The Fourier transform of `1/(kᵀMk)` on `R³` is stated as
ASSUMED at the usual scope.

**Step 4 (forward cone): holds.** The backward predecessors send influence only forward.

**Verdict on jb4a1: confirmed**, with no failing step.

## Output

`check.py` prints `HIT: confirmed - ...` for jb4a1, whose steps are all re-verified, together with j4249's steps 1–3. It
then prints a SUMMARY line: jb4a1 confirmed, and j4249 failing at step 4.
