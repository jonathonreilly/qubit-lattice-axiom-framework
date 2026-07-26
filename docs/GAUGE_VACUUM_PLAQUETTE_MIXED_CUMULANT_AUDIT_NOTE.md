# Gauge-Vacuum Plaquette Mixed-Cumulant Audit and First Nonlinear Coefficient

**Date:** 2026-04-16
**Status:** exact first-nonlinear-coefficient theorem on the accepted Wilson
`3 spatial + 1 derived-time` surface
**Script:** `scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py`

## Question

After ruling out the naive constant-lift law, can the first genuine
higher-order coefficient of the full-vacuum reduction law be closed exactly?

## Answer

Yes, at small `beta`.

The mixed repeated-plaquette audit now closes the onset theorem

`P_full(beta) = P_1plaq(beta) + beta^5 / 472392 + O(beta^6)`

and therefore

`beta_eff(beta) = beta + beta^5 / 26244 + O(beta^6)`

on the accepted Wilson `3 spatial + 1 derived-time` surface.

This is the first exact nonlinear coefficient of the full-vacuum reduction law.
It is a real upgrade. It is **not** yet full analytic plaquette closure at
`beta = 6`.

## Setup

Write the plaquette observable as

`O = (1/3) Re Tr U_p`

and the Wilson action density as

`X_q = (1/3) Re Tr U_q`.

Then

`P_full(beta) = sum_(n >= 1) beta^n / n! * sum_(q1,...,qn) kappa(O ; X_q1, ..., X_qn)`

where `kappa` denotes the exact connected Haar cumulant at `beta = 0`.

The local one-plaquette block `P_1plaq(beta)` contains precisely the cumulants
with every `q_i = p`. The question is therefore:

> what is the first nonlocal connected cumulant, and what is its exact
> coefficient?

## Theorem 1: leaf plaquettes factorize exactly

Let `q` be a plaquette in a connected distinct-support graph that shares only
one link with the rest of the support. Let `U` denote that shared link and let
`A` be the ordered product of the other three links around `q`.

Those three nonshared links appear nowhere else in the support, so under the
Haar product measure:

- `A` is Haar-distributed,
- `A` is independent of `U` and of the rest of the support,
- `U A` is Haar-distributed for every fixed `U`.

Therefore for every polynomial `F` in the single plaquette variable `X_q`,

`E[F(X_q) | rest, U] = c_F`

is a constant independent of both `U` and the rest of the support.

So any repeated insertion carried by a leaf plaquette factors off exactly from
the rest of the support. Consequently:

> any mixed connected cumulant whose distinct-support graph is a tree vanishes
> exactly after iterative leaf peeling.

This is the missing repeated-plaquette mechanism: repeated leaves do not create
new connected nonlocal coefficients.

## Corollary 1: only leafless distinct supports can contribute nonlocally

After subtracting the local one-plaquette block, every surviving nonlocal term
must reduce to a **leafless** distinct support containing the observed
plaquette.

So the onset problem is a finite leafless-support classification problem.

## Theorem 2: there is no nonlocal correction through order `beta^4`

For order `n <= 4`, every nonlocal support must touch each of the four observed
edges at least once. The runner computes, over every local action plaquette
distinct from the observed one, the number of observed edges it carries, and
finds the maximum to be `1`. So a distinct non-observed plaquette can touch at
most one observed edge, and the only leafless size-`4` candidate class is:

- one distinct action plaquette on each observed edge.

The runner exhaustively checks all

`5^4 = 625`

such local supports and tests all `2^5` orientation assignments. None satisfies
the exact link-balance condition required for a nonzero `SU(3)` Haar integral.

So

`P_full(beta) - P_1plaq(beta) = O(beta^5)`.

## Theorem 3: the only distinct order-`beta^5` survivors are the four cube shells

At order `beta^5`, a distinct leafless support must still include one action
plaquette on each observed edge, plus one extra action plaquette.

The runner exhaustively checks every such local candidate support and finds:

- `37176` exact local candidates are tested,
- exactly `4` survive,
- they are precisely the four elementary cube shells through the observed
  plaquette.

Geometrically, the observed plaquette lies in four elementary `3`-cubes on the
accepted `3 spatial + 1 derived-time` hypercubic surface:

- positive and negative offset in transverse direction `2`,
- positive and negative offset in transverse direction `3`.

No other distinct order-`beta^5` support survives.

## Theorem 3b: the repeated-face sector at order `beta^5` is empty

Theorem 3 covers only supports whose five action insertions are five *distinct*
faces. A repeated insertion is a genuinely different object: two copies of the
same action face each carry their own orientation sign, so the sign space is
larger than the one already searched at order `beta^4`.

The multiplicity patterns of five insertions are the `7` partitions of `5`. A
pattern with `d` distinct faces reaches at most `d` observed edges, by the
maximum-overlap fact established in Theorem 2. Since all four observed edges
must be covered, the `5` patterns with `d < 4` are eliminated, leaving exactly
two sectors that can contribute at order `beta^5`:

- `1 + 1 + 1 + 1 + 1`, five distinct faces — treated in Theorem 3,
- `2 + 1 + 1 + 1`, four distinct faces with one of them repeated.

The runner enumerates the second sector explicitly: `2500` distinct multisets,
each tested against the exact link-balance condition over all `2^6` independent
orientation signs. There are `0` survivors.

Structurally this is what the center grading forces. A doubled face carries the
net center charge `+2`, `0` or `-2`. The values `+2` and `-2` are congruent to
`-1` and `+1` modulo `3`, so those branches collapse exactly onto the
single-copy conditions already shown empty in Theorem 2, while the `0` branch
leaves one observed edge carried by the observed plaquette alone, at charge
`+1` or `-1`, which is not `0` modulo `3`.

So the enumeration in Theorem 3 is complete for order `beta^5`, and repeated
insertions contribute nothing at that order.

## Theorem 4: each cube shell contributes exactly `1 / 18^5`

Every factor below is computed by the runner from the shell's own geometry;
none of them is inserted by hand.

- **Face count and closure.** The support is `6` plaquette factors, one
  observed plus five action faces. The runner builds the abstract complex of
  the enumerated shell and reads `F = 6`, `V = 8`, `E = 12`, so
  `V - E + F = 2` and every link is shared by exactly two faces: the support is
  a closed surface.
- **Orientation factor.** Each face may be traversed in either sense. The
  runner solves the `2^6` sign assignments for the condition required for a
  nonzero link integral — every shared link traversed once forward and once
  backward — and finds exactly `2` solutions, the two global orientations of
  the closed surface.
- **Face normalization.** From the Setup, each plaquette density contributes
  `(Tr + Tr^dagger) / 6`, giving `(1/6)^6`, with the exponent taken from the
  computed face count rather than assumed.
- **Color contraction.** Each link appears exactly twice, once as `U` and once
  as `U^dagger`, so its integral is the exact second Haar moment

  `int dU U_ij conj(U)_kl = delta_ik delta_jl / N`.

  The runner labels the `24` color index slots of the six traces and applies
  that moment link by link as an identification of slots. The surviving free
  index classes are counted by union-find: exactly `8` classes on every shell,
  each summing to `N`, against `12` factors of `1/N` from the moment
  normalization. So the raw color contraction is

  `N^(8 - 12) = 3^(-4) = 1/81`.

- **Identification of the classes.** The count `8` is not asserted to be `V`.
  The runner checks that the slot-to-vertex map is constant on each union-find
  class and that the induced map from classes to lattice sites is a bijection
  onto the `8` vertices of the shell. The exponent is therefore `V - E` with
  the identification proved, not named.
- **Rejectors.** The contraction discriminates in two independent ways.
  Reversing any single face destroys the once-forward-once-backward pairing on
  its links and the contraction is then undefined: `0` of the `6` single-face
  flips remain coherent. Replacing the moment's row-to-column identification by
  a row-to-row one yields `4` classes instead of `8`, that is `N^(-8)` instead
  of `N^(-4)`.
- **Independent cross-check.** A fixed-seed Monte-Carlo integration over
  genuine Haar-random `SU(3)` matrices, one per link, returns
  `+0.011606 +- 0.000913` for the coherent shell against the exact
  `1/81 = 0.012346`, and rejects `1/27`, `1/243` and `0` at `27.9`, `8.2` and
  `12.7` standard errors. The same integration returns `+0.000429 +- 0.001127`
  for a shell with one face reversed, consistent with `0` and rejecting `1/81`
  at `10.6` standard errors. The sampler's own measure is checked first: its
  first Haar moment and both second moments reproduce the exact values.

So the exact per-shell contribution is

`2 * (1/6)^6 * (1/81) = 1 / 18^5`.

Since there are exactly `4` cube shells, the first nonlocal coefficient is

`4 / 18^5 = 1 / 472392`.

## Corollary 2: first nonlinear coefficient of the reduction law

The exact local one-plaquette slope is

`P_1plaq'(0) = 1 / 18`.

So if

`P_full(beta) = P_1plaq(beta_eff(beta))`

holds as a formal small-`beta` reduction law, then the first nonlinear term is
forced to be

`beta_eff(beta) = beta + (1 / 26244) beta^5 + O(beta^6)`.

Equivalently:

`P_full(beta) = P_1plaq(beta) + (1 / 472392) beta^5 + O(beta^6)`.

## What this closes

- the mixed repeated-plaquette audit through the first nonlocal order, in both
  multiplicity sectors that can cover the four observed edges at order `beta^5`
- the per-shell weight as a computed quantity: the orientation count is solved
  for, and the color factor is an index contraction under the exact second Haar
  moment whose free classes are shown to stand in bijection with the vertices
  of the closed surface
- the first exact nonlocal coefficient of the full-vacuum plaquette expansion
- the first exact nonlinear coefficient of the reduction law `beta_eff(beta)`

## What this does not close

- the full nonperturbative function `beta_eff(beta)` at `beta = 6`
- full analytic repinning of the canonical plaquette package
- repo-wide downstream migration from `<P> = 0.5934`

The current live boundary is therefore:

> the onset of the full-vacuum reduction law is now exact, but the
> nonperturbative continuation to the framework point `beta = 6` is still open.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py
```

Expected summary:

- `THEOREM PASS=14 SUPPORT=2 FAIL=0`
