# Referee report: J:derive:no-waves-under-positive-formation:a2

- **Author:** w-macbookpro90c72-j80c2 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j153a (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j80c2__ec547912__20260919T014531Z`.

**Disclosure.** This referee's model family has already refereed three other attempts of this problem:

| Attempt | Referee directory | Finding |
|---|---|---|
| a1 | `referee_w-jonathonsmac4f50-jadef` | the two-level negative-weight wave route |
| a3 | `referee_w-jonathonsmac4f50-j40e2` | — |
| a4 | `referee_w-jonathonsmac4f50-jdb84` | — |

`check.py` is independent code: exact sympy for every finite fact, and numpy for the random scans.

## The claim

The attempt's multiplier is `λ(k) = Σ_{z∈F} w_z e^{ik·z}`, with `w_z > 0`, `Σ w_z = 1` and `F ⊂ Zᵈ` finite. That is, one earlier level. It
claims the following.

1. **The bound.** `|λ| ≤ 1`. Equality at `k ≠ 0` holds iff `e^{ik·z}` is constant on `F`. The attempt glosses this as "the collinear
   exception: `F` lies in a coset of a hyperplane `k·z = const`".
2. **Small `k`.** `λ = 1 + i v·k − ½ kᵀE[zzᵀ]k + O(k³)`. The Hessian of `|λ|²` at 0 is `−2 Cov(z)`, "so the mode is drift plus diffusion,
   never a wave `|λ| = 1` with `arg λ = c|k|`".
3. **Stencil numbers.**
   - The 7-stencil has `λ(π,0,0) = 3/7`, series `1 − k₁²/7` and Hessian `−4/7`.
   - The drift is `i/4`.
   - `2 − e^{ik}` has `|λ|² = 9` at `π`.
4. **HIT and SUMMARY.** "Waves `|λ|=1` with `arg=c|k|` require dropping positivity or adding a conserved unitary structure", and "no
   propagating wave under positivity".

## Step by step

**Step 1 (Jensen): the inequality and the iff hold. The reading of the equality set does not.**

What holds (R1):
- The inequality: `max |λ|` is `1` to 15 digits over 400 random positive stencils in `d = 1..3`.
- The gradient `i v` and the Hessian `−2 Cov(Z)` at 0, exact on 12 random rational stencils.

The attempt then reads "`e^{ik·z}` constant on `F`" in two ways that fail:

- **(a) Not only collinear supports.** A support inside a proper sublattice also reaches `|λ| = 1` at `k ≠ 0`, even when it spans the plane
  affinely (R2a).
  - `F = {±e₁, ±e₂}` (the four-neighbour average) has `λ(π,π) = −1`.
  - Yet `k·z` takes both values `π` and `−π` on `F`, so `F` lies in no hyperplane `k·z = const`.
  - In `d = 1`, `F = {0, 2}` has `λ(π) = 1`.

  These staggered modes do not propagate. But the stated characterization of the equality set is false.

- **(b) The collinear case contains exact waves under positivity.** Suppose `F` lies in an affine hyperplane `n·z = c` with `c ≠ 0`. Then
  `λ(κn) = e^{iκc}` exactly.
  - R2b: `F = {e₁, e₂}` with weights ½ gives `λ(κ,κ) = e^{iκ}`, so `|λ| = 1` and `arg λ = |k|/√2` along `(1,1)`.
  - This is a wave in the task's sense, `|λ| = 1` with `arg λ = c|k|`, along one direction. It has positive weights and no unitary
    structure.
  - The attempt's only exhibited exception, `F = {0, e₁}`, is the static case: its hyperplane passes through 0 and `λ = 1` on the null line.

  So statement (1)'s "NSD Hessian, so … never a wave" does not follow in the null directions. The HIT's "waves … require dropping
  positivity or adding a conserved unitary structure" and the SUMMARY's "no propagating wave under positivity" are false. Section (3)'s
  weaker statement, that the exception "is not an isotropic light cone", is true.

**Step 2 (7-stencil): holds.** R3: `λ(π,0,0) = 3/7`, axis series `1 − k₁²/7`, Hessian of `|λ|²` equal to `−4/7`.

**Step 3 (collinear example): holds as a finite fact.** `|λ|² = (1 + cos k₁)/2` equals 1 on `k₁ = 0`. As said under step 1, this is the
static case only.

**Step 4 (negative weight): holds as arithmetic.** R3: `|2 − e^{ik}|² = 5 − 4 cos k`, which is 9 at `π` and greater than 1 for every
`k ≠ 0`. This is amplification, not a wave, so it does not supply the "weakest change that would give waves" the task asks for.

**Step 5 (drift): holds.** R3 gives `i/4` for `(1 + Σ e^{ik_j})/4`, which is the stencil the attempt actually uses. Calling it "backward" is a
naming matter.

**Scope.** The task has two parts the attempt leaves out.
- **Several earlier levels.** The task asks for positive weights over finitely many earlier levels. The attempt treats one level and
  mentions more only under (4).
  - R4a supports the extension: every characteristic root of 300 random positive two- and three-level models has `|λ| ≤ 1` (max
    `0.999999999`).
  - It is not proved in the attempt.
- **The wave-giving change.** The task asks for the weakest change that would give waves, and its cost.
  - One weight `−1` on the second earlier level does it. The leapfrog model, with level-`t` weights `2 − 4c²` at 0 and `c²` at `±eᵢ`,
    gives `|λ| = 1` on the whole zone for `c² ≤ ½` and `arg λ = c|k| + O(|k|³)` (R4b). This is an isotropic wave, bought by giving up
    positivity.
  - The attempt exhibits no wave-giving change.

## Verdict

**Fails at step 1, in its reading of the equality set.** Two things go wrong:
- sublattice supports are missed (`λ(π,π) = −1` for `{±e₁, ±e₂}`);
- the collinear case off the origin is an exact wave under positive weights (`λ(κ,κ) = e^{iκ}` for `{e₁, e₂}`).

Both contradict the HIT's "waves require dropping positivity" and the SUMMARY's "no propagating wave under positivity".

What survives:
- the Jensen bound;
- the expansion with Hessian `−2 Cov`;
- the numbers `3/7`, `−1/7`, `−4/7`, `i/4` and `9`.

Not covered: several levels, and the wave-giving change.

`check.py` prints `SUMMARY: fails at step 1 - ...` with no HIT line.
