# Referee report: J:derive:lightcone-formation:a6

- **Author:** w-macbookpro90c72-j0029 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jdb2a (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `f67a3bd3`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (exact integers, sympy, mpmath, and numpy
for one spectrum).

## The claim

The attempt claims a partial result made of five parts:
- (a) reversibility of the symmetric 7-stencil law with respect to `π ∝ Π_x Z(β|S_x|)`, which fails for the backward
  stencil;
- (b) `π` is the marginal of a Heisenberg ferromagnet on a doubled graph `Γ` whose Laplacian spectrum is `{E, 14 − E}`;
- (c) the linear kernel `7σ²/(2E(1 − E/14))`, "the Green-function kernel `1/E` times a bounded factor
  `7/(2(1 − E/14)) ∈ [7/4, 7/2]`";
- (d) a linearised Dobrushin threshold `β = 3/7`, with the global Lipschitz bound of the mean map marked ASSUMED;
- (e) the small-`β` interaction differs from the static pair.

## Step by step

**Steps 1–3 (pairing, reversibility, backward no-go): hold.**
- K1 checks the 7-stencil pairing on 200 random six-axis configuration pairs of `(Z/3)³`.
- The backward stencil fails the pairing on unit-vector configurations: all `+z` except one `+x` site each, giving `102`
  against `100`. The author's counterexample uses zero vectors, which are not records of the menu. Bilinearity makes that
  harmless, and K1 exhibits a genuine one.

**Step 4 (doubled graph): holds.** The Bloch Laplacian `[[7, −a], [−a, 7]]`, with `a = 7 − E`, has eigenvalues `E` and
`14 − E`. The Laplacian of the doubled graph over `(Z/3)³` has exactly this spectrum over its 27 momenta (K2).

**Step 5 (linear kernel): the identity holds; the stated range of the prefactor is wrong.**
- The identity holds: `1/(1 − φ²) = 49/(E(14 − E)) = 7/(2E(1 − E/14))` (K3).
- The prefactor `7/(2(1 − E/14))` increases from `7/2` (at `E → 0`) to `49/2` (at `E = 12`). Its range on `(0, 12]` is
  `[7/2, 49/2]`.
- The attempt states `[7/4, 7/2]` in both (c) and Step 5. The value `7/4` would need `E = −14`.
- The qualitative statement, a bounded factor times `1/E`, survives with the correct constants. Attempt a5 states them
  correctly.

**Step 6 (Dobrushin): the linearised coefficient holds; the conditional uniqueness does not follow.**
- `A'(0) = 1/3 = lim A(κ)/κ`, so the mean map has Jacobian `(β/3) I` at `S = 0`, and the linearised coefficient is
  `7β/3`.
- The step then says that under the ASSUMED global bound `‖Cov_vMF‖ ≤ 1/3` "the PCA is unique for `β < 3/7`". Section (4)
  adds that proving `A' ≤ 1/3` "would make `β < 3/7` a theorem".
- Neither follows. The Dobrushin/Wasserstein influence of a predecessor is the Wasserstein-1 Lipschitz constant of
  `S ↦ vMF(βS)`, not the mean map's.
- At `κ = 3` the 1-Lipschitz function `f = −|s − n|` has `Cov(f, s·n) = 0.113646 > A'(3) = 0.101147` (K4).
- `A' < 1/3` and `A/κ ≤ 1/3` hold for all `κ` (K4 on a grid; attempt a5 proves them), yet the gap remains. What is missing
  is `sup over 1-Lipschitz f of Cov_κ(f, u·s) ≤ 1/3`.

**Step 7 (static against this law): holds.** `log(sinh κ/κ) = κ²/6 − κ⁴/180 + O(κ⁶)` (K5, where the `κ⁶` coefficient is
`1/2835`). The comparison drawn from it holds.

**Step 8 (FSS): not claimed**, as stated.

## Classic failure modes

- *A finite fact stated wrongly.* The prefactor range in Step 5.
- *An outside principle beyond its hypotheses.* A Lipschitz mean map is read as a Wasserstein contraction in Step 6.
- *A counterexample outside the configuration space.* The zero vectors of Step 3, repaired in K1.

## Verdict

**First failing step: 5.** The stated range of the kernel prefactor is wrong; the true range is `[7/2, 49/2]`.

Step 6's conditional uniqueness and its remedy also do not follow.

What holds, re-verified:
- reversibility, and its failure for the backward stencil;
- the doubled-graph spectrum;
- the kernel identity;
- the linearised coefficient `7β/3`;
- the small-`β` series.

`check.py` prints `SUMMARY: fails at step 5 - ...` and no `HIT: confirmed` line.
