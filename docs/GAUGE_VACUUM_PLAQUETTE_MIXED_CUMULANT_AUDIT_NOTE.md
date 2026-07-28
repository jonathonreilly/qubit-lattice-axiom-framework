# Gauge-Vacuum Plaquette Mixed-Cumulant Audit and First Nonlinear Coefficient

**Date:** 2026-04-16
**Type:** positive_theorem
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

## Theorem 1: a private plaquette link forces exact factorization

Let `q` be a plaquette in a mixed support and suppose at least one link `H` of
`q` appears in no other *distinct* support face. Hold all other link variables
fixed. The plaquette holonomy has the form `A H B` or `A H^dagger B`, where
`A` and `B` contain the remaining links around `q`.

Haar bi-invariance and invariance under inversion imply:

- `A H B` and `A H^dagger B` are Haar-distributed for every fixed `A,B`,
- their law is independent of every other face variable,
- the entire repeated family `X_q, X_q, ...` is therefore independent of the
  variables carried by the remaining distinct faces.

Therefore, for every polynomial `F` in the single plaquette variable `X_q`,

`E[F(X_q) | all other face variables] = c_F`

is a constant. A joint cumulant vanishes whenever its arguments split into two
independent nonempty families. Consequently:

> any mixed connected cumulant whose distinct support contains a face with a
> private link vanishes exactly, including arbitrary repeated copies of that
> face.

This is stronger than graph-leaf peeling: a face may meet several other faces
and still factorize if even one of its four links remains private.

## Corollary 1: only private-link-free distinct supports can contribute

After subtracting the local one-plaquette block, every surviving nonlocal term
must have a **private-link-free** distinct support containing the observed
plaquette.

So the onset problem is a finite distinct-support boundary classification
problem. Multiplicity changes how often a face variable occurs, but it cannot
remove a private link from the distinct support.

## Theorem 2: there is no nonlocal correction through order `beta^4`

At action order `n <= 4`, the observed insertion and the action supply at most
five distinct faces, even when some action insertions equal the observed
plaquette.

Two distinct hypercubic plaquettes share at most one link. A support with at
most four distinct faces therefore gives every chosen face at most three
shared links, so at least one of its four links is private and Theorem 1
applies.

It remains only to exclude a five-distinct-face support. If one observed edge
is not carried by another face, that edge is already private. Otherwise the
runner computes that a distinct non-observed plaquette carries at most one
observed edge, leaving exactly one action face on each of the four observed
edges. The runner exhaustively checks all

`5^4 = 625`

such supports and finds that every one still has at least `4` private outer
links. As an independent center-grading rejector, it also tests all `2^5`
orientation assignments and finds no exact `SU(3)` link-balance survivor.

So

`P_full(beta) - P_1plaq(beta) = O(beta^5)`.

## Theorem 3: the only distinct order-`beta^5` survivors are the four cube shells

At order `beta^5`, a distinct private-link-free support must still include one
action plaquette on each observed edge, plus one extra action plaquette.

The runner exhaustively checks every such local candidate support and finds:

- `34676` distinct edge-adjacent supports are tested,
- exactly `4` survive,
- they are precisely the four elementary cube shells through the observed
  plaquette.

Geometrically, the observed plaquette lies in four elementary `3`-cubes on the
accepted `3 spatial + 1 derived-time` hypercubic surface:

- positive and negative offset in transverse direction `2`,
- positive and negative offset in transverse direction `3`.

No other distinct order-`beta^5` support survives.

## Theorem 3b: every repeated or observed-copy sector factorizes

Theorem 3 covers supports whose five action insertions are five *distinct*
faces other than the observed face. Completeness must also include:

- every repeated-action multiplicity;
- action insertions equal to the observed plaquette;
- combinations of both.

The runner generates every integer partition of each action order `1` through
`5` and, for every partition, both absence and presence of the observed face
in the action support. This gives `36` structural classes.

There is exactly one class with six distinct total faces:

- order `5`, multiplicity `1 + 1 + 1 + 1 + 1`, with the observed plaquette
  absent from the action faces.

That is precisely the distinct sector of Theorem 3. If any action face is
repeated, or if an action insertion equals the observed plaquette, the total
distinct support has at most five faces. The private-link exhaustion in
Theorem 2 then applies, so the whole repeated family factorizes from the rest
and the mixed connected cumulant is zero. This also covers the local-support
case in which every action insertion equals the observed face; that case is
subtracted as part of `P_1plaq`.

As an independent finite rejector, the runner still enumerates the largest
non-observed repeated sector explicitly: the `2 + 1 + 1 + 1` sector has `2500`
distinct multisets, each tested over all `2^6` independent orientation signs,
and has `0` center-balanced survivors. A doubled face carries net center charge
`+2`, `0` or `-2`; the nonzero branches reduce modulo `3` to the excluded
single-copy condition, while the zero branch leaves its observed edge
unbalanced.

Thus Theorem 3 is complete for every action-face multiplicity through order
`beta^5`, including copies of the observed plaquette.

## Theorem 4: each cube shell contributes exactly `1 / 18^5`

Every factor below is computed by the runner from the shell's own geometry;
none of them is inserted by hand.

- **Connected-cumulant subtraction.** The runner enumerates all
  `2^6 - 2 = 62` nonempty proper subsets of the six shell faces. Every proper
  subset has a private link, so its block moment is zero by Theorem 1 and the
  zero first Haar moment. Every proper set partition in the moment-cumulant
  formula therefore contains a zero block. The connected six-face cumulant is
  exactly the raw six-face moment computed below.
- **Taylor ordering.** The five action faces in each surviving shell are
  distinct. The ordered action sum therefore contains exactly `5!`
  permutations of that shell, canceling the `1/5!` Taylor prefactor in the
  Setup. No additional symmetry factor remains.
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
  genuine Haar-random `SU(3)` matrices, one per link, returns the real part
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

- the mixed repeated-plaquette audit through the first nonlocal order, across
  all action multiplicities and both absence and presence of the observed face
  through order `beta^5`
- the connected-cumulant subtraction on each surviving shell, rather than only
  its raw moment
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
- finite-volume wrapping or boundary-identification modifications of the local
  non-wrapping cubical patch

The current live boundary is therefore:

> the onset of the full-vacuum reduction law is now exact, but the
> nonperturbative continuation to the framework point `beta = 6` is still open.

## No-Go Discipline Gate for the finite vanishing statements

The negative content here is narrow: only mixed connected cumulants on the
stated local Wilson cubical surface through action order `5` are classified.
There is no claim about higher orders or nonperturbative continuation.

### N1 — alternative routes

| Attack route | Disposition | Evidence |
|---|---|---|
| A support through order `4` might survive with the maximum five distinct total faces. | `ATTEMPTED`: all `625` only-possible five-face boundary candidates have at least four private links; the separate orientation scan also has zero survivors. | Theorem 2 and the runner's private-link and order-`beta^4` gates. |
| A repeated non-observed action face might evade the distinct-face scan. | `ATTEMPTED`: every repeated class has at most five distinct total faces and factorizes; independently, all `2500` maximal `2+1+1+1` multisets fail center balance. | Theorem 3b and its explicit repeated-sector gate. |
| An action insertion equal to the observed face might evade the one-observed-edge bound. | `ATTEMPTED`: observed-face placement is enumerated for every partition; every mixed observed-copy class has at most five distinct faces and a private link. | Theorem 3b structural-class gate. |
| A five-distinct-action support other than a cube shell might survive. | `ATTEMPTED`: `34676` unique edge-adjacent supports are tested and exactly the four expected cube shells survive. | Theorem 3 distinct-sector gate. |
| Proper moment-cumulant subtraction, a different orientation, or a different color pairing might change the cube weight. | `ATTEMPTED`: all `62` proper shell subsets have a private link, exactly two coherent orientations survive, and explicit index contraction plus two rejectors fixes `N^(8-12)`. | Theorem 4 subset, orientation, index-class, and rejector gates. |

The five routes differ respectively in support order, multiplicity, observed
face placement, distinct geometry, and terminal Haar/cumulant obligation.

### N2 — wall independence

There are no open walls inside this finite theorem. Private-link exhaustion,
distinct-support enumeration, connected-cumulant subtraction, and Haar
contraction are separate proof obligations, not an inflated list of
conditionals. Closing one does not silently label another as closed; each has
its own runner gate.

### N3 — hidden-wall scan

- `accepted ... surface` is the explicit theorem domain, not an inferred
  framework-wide consequence.
- `normalization`, `sector`, and `boundary` name objects defined in the Setup
  or finite searches; none imports an unstated result.
- `canonical` occurs only in the non-load-bearing list of results not closed.
- The note contains no `we assume`, `by construction`, `as is standard`,
  `the framework provides`, `bridge context`, `background`, `naturally`,
  `obviously`, `standard QFT`, or `registered` premise.

### N4 — residual matching

The dated prior witnesses below are entries in
`docs/audit/data/ledger/ga/gauge_vacuum_plaquette_mixed_cumulant_audit_note.json`.

| Prior witness | Witness residual | Residual closed here | Match |
|---|---|---|---|
| Audit row, `2026-07-18` | four-distinct-plus-one-repeat sector not enumerated; orientation/color factors inserted | explicit `2500`-multiset scan and geometry-derived Haar contraction | yes |
| Audit row, `2026-07-17` | action copies of the observed plaquette omitted | all partition/observed-placement classes through order `5` | yes |
| Audit row, `2026-07-15` | raw cube moment not proved equal to the connected cumulant | all `62` proper shell subsets have zero block moment | yes |

No different residual is used as a witness for these closures.

### N5 — rhetoric and resolution

- `per_element`: private-link Haar factorization and exact link charges are
  tested.
- `per_site`: the shell color classes are checked bijectively against all
  eight shell vertices.
- `per_mode`: no momentum-, spectral-, or mode-wide negative statement is
  made.
- `per_block`: every local support/multiplicity class through order `5` and
  every proper cube block are tested.
- `lattice_wide`: only translation of the same non-wrapping local marked-face
  calculation is intended; finite-volume wrapping, higher orders, and
  `beta = 6` continuation are explicitly outside scope.

Every vanishing phrase in the theorem is restricted to the tested
per-element/per-block surface.

### N6 — partial-closure paths

The result neither requests a new axiom nor says that no retained primitive
can supply a missing step. The fixed Wilson surface is an explicit domain
premise. The previously open finite routes are closed by exact enumeration and
Haar invariance; higher-order and nonperturbative routes remain ordinary
out-of-scope mathematics, not misclassified axiom walls.

### N7 — steelman

The strongest objection is that the observed plaquette itself is an allowed
action insertion, so it touches all four observed edges and defeats the
non-observed overlap count; moreover, even a correct raw cube moment need not
equal a connected cumulant. That objection was decisive against the earlier
packet. It is closed here without assuming either conclusion: observed-face
placement is included in the complete multiplicity table, where it forces at
most five distinct faces and hence private-link factorization, while the
runner separately checks every proper cube subset and makes every subtraction
term vanish.

### N8 — cross-cycle echo

The closest prior echo is the distinct-shell finite-geometry packet, which
isolated only the distinct cube boundary and explicitly did not close mixed
multiplicities. The current proof uses its finite geometry shape but adds the
missing private-link, observed-copy, and connected-cumulant routes rather than
promoting that older scope. Plaquette-loop ledgers warning that a finite
strong-coupling coefficient is not a `beta = 6` closure remain active and are
honored by the exclusions above; their nonperturbative residual does not match
this finite-order residual.

**No-Go Discipline status:** `PASS` for the scoped order-at-most-five
vanishing statements.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py
```

Expected summary:

- `THEOREM PASS=16 SUPPORT=2 FAIL=0`
