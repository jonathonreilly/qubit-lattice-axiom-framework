# An orbit-averaged all-24 coframe carrier: the uniform average over the 24 proper rotations is exactly O-equivariant, and one-coset partial averages only conjugate D3 — Cycle 701

Date: 2026-08-01

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no axiom, foundation, Qualification, primitive, registry, policy, queue, audit-status, or PR-control surface. No new axiom or primitive is proposed or adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every such object is named as supplied.

Runner: `scripts/physical_orbit_averaged_all24_carrier_cycle701_2026_08_01.py`
(36 PASS / 0 FAIL, exit 0).

## What this cycle establishes

Let `P` be the Cycle-696 single-complex coframe pipeline — source domain, then
response `eps`, then metric/coframe field `h` — and let `O` be the group of the
24 proper cubic rotations. Define the orbit-averaged carrier

    X(rho) := (1/24) sum_{g in O} g^{-1} . P(g . rho),

where `g . rho` rotates the source domain and `g^{-1} . ( )` is the matrix-field
pullback.

**Theorem 1 (orbit-averaged carrier).** `X` is exactly `O`-equivariant for any
source `rho`: `X(h . rho) = h . X(rho)` for every `h` in `O`.

Proof. `X(h . rho) = (1/24) sum_g g^{-1} . P(g h . rho)`. Substitute `k = g h`;
as `g` runs over `O` so does `k`, and `g^{-1} = h k^{-1}`, so the sum equals
`(1/24) sum_k h . (k^{-1} . P(k . rho)) = h . X(rho)`. The argument is a change
of variables in a finite group sum. It uses only that the 24 frames form a group
and that pullback and pushforward implement the group action, so it holds for
every source, edited or not, and it makes no demand whatever on `P`.

The uniform weight `1/24` is the one determined by the group itself: it is the
reciprocal of the group order, fixed by counting each element of `O` once. No
new supplied constant enters this cycle.

**Theorem 2 (conjugation law for partial averages).** The Cycle-696 pipeline is
`D3`-covariant, which is its landed scope. Write `t_g := g^{-1} . P(g . rho)`
for the individual terms and fix a frame `g0`. For the right coset
`C = D3 g0` and any `d` in `D3`,

    t_{d g0} = (d g0)^{-1} . P(d g0 . rho)
             = g0^{-1} . d^{-1} . P(d . (g0 . rho))
             = g0^{-1} . d^{-1} . d . P(g0 . rho)
             = g0^{-1} . P(g0 . rho)
             = t_{g0},

the third line being exactly `D3`-covariance of `P` applied to the source
`g0 . rho`. All six terms of one coset therefore coincide; a one-coset average
equals the single term `t_{g0}`; and that term is equivariant exactly under the
conjugate subgroup `g0^{-1} D3 g0`, a subgroup of the same order six. A
one-coset average relocates `D3` by conjugation; it does not enlarge it. Of the
averages gated in this cycle, the full orbit average — equivalently a four-term
transversal average, one term per right coset — is the one that reaches `O`.

The price is stated in the same breath as the theorem. The averaged carrier is
honestly a four-complex mixture: a mean of four pulled-back copies of the landed
pipeline, one per right coset of `D3` in `O`. It is not a single-complex
construction.

## The wall this addresses

Cycle 700's contract row:

> | real-space all-24 carrier | PARTIAL (two-carrier split) | B5–B6: prediction carrier all-24; coframe carrier exactly D3; the energy scalars are re-pinned to a stated convention and one reference row is withdrawn |

Cycle 700's scope identification:

> The Cycle-696 compiler's well-posed covariance scope of six frames is exactly the body-diagonal stabilizer D3, isomorphic to S3: the six frames are `[1, 4, 9, 15, 18, 23]`, they are closed under product and inverse, their orders are `{1:2, 4:2, 9:2, 15:3, 18:3, 23:1}`, and over all 24 frames the existence of a variable permutation is equivalent both to preservation of the seven spatial direction classes up to sign and to fixing `(1,1,1)` up to sign.

Cycle 700 asked for a real-space all-24 carrier and reported a two-carrier
split, with the coframe carrier sitting at exactly `D3`. The orbit-averaged
carrier `X` is a real-space all-24 coframe carrier, at the stated price: it is
built from four pulled-back copies of the landed single-complex pipeline rather
than from one. The `D3` identification quoted above is not weakened here. It is
precisely what makes Theorem 2's coset collapse exact, and it remains the
correct scope statement for the single-complex pipeline.

## Construction

`X(rho)` is assembled entirely from landed machinery. For each of the 24 frames
the source domain is rotated by the compiler's own decorated action, the landed
response and metric/coframe steps produce `h`, and the resulting matrix field is
pulled back under the pinned convention

    out[x] = R.T @ h_rotated[rotate_site(x, frame, L)] @ R,

with `R` the frame matrix and `rotate_site` the rotation of lattice sites about
the lattice centre `(L-1)//2`. That convention is pinned rather than chosen
freely: rotation about a centre is geometric only when the centre is itself a
lattice site, which is why the gates run at odd `L`, namely `L = 3` and
`L = 7`. The 24 rotated complexes are conjugates of the landed complex by
lattice-axiom rotations, so nothing outside the framework is brought in; the
average runs over objects the lattice already contains.

Two sources are used. The physical, unedited source is `O`-invariant, measured
exactly `0.0` at both sizes, which isolates the carrier's transformation law
from any source asymmetry. The edited sources — a single link relabel adjacent
to the anchor at each size — are deliberately not `O`-invariant, and they are
what makes the equivariance gates discriminating: on them the unaveraged
single-complex carrier fails by a wide margin while the averaged carrier does
not fail at all.

## Measured results

| gate | measured |
|---|---|
| covariance scope frames and orders (a2) | `[1, 4, 9, 15, 18, 23]`, orders `{1: 2, 4: 2, 9: 2, 15: 3, 18: 3, 23: 1}` |
| single-carrier positivity scan and boundary (a3, a4) | one onset; `s_pd = 0.422836427078498` |
| positivity failures just above the boundary (a5) | `[[0,1,1], [1,0,1], [1,1,0], [1,1,2], [1,2,1], [2,1,1]]` |
| single-carrier log-volume orbit spreads (a6) | `[0.33489977962932677, 0.20202937219367642, 0.12752360963188508, 0.07130325023123454]` |
| right cosets of `D3` in `O` (s1) | 4 cells of 6; `cell0 = [0, 6, 10, 12, 19, 21]`; one body diagonal per cell |
| union of the four rotated direction copies (s2) | 13 classes, `O`-invariant, census `{(1,4): 3, (2,2): 6, (3,1): 4}`, incidence 28 |
| quadratic-form recovery from 7 directions (s3) | rank 6, min singular value `0.874032`, recovery below `1e-12`; identical for each rotated copy |
| axes-only readout, rejector (s4) | rank 3, deviation `7.000000e-03` |
| source invariance at `L = 3` and `L = 7` (h1, l1) | `0.0` exactly |
| unaveraged single-complex violation, frames 0, 2, 3 (h2) | `0.4581`, `0.367`, `0.4581` |
| orbit-averaged equivariance defect (h3) | `2.220e-16` |
| within-coset term spread (h4) | `1.456e-11` |
| transversal reduction (h5) | `3.640e-12` |
| inter-coset tension at amplitude `0.40`, rejector (h7) | `4.823389e-01` |
| averaged-carrier spread collapse, physical source (p1) | `7.105e-15`, `2.359e-16`, `0.000e+00`, `1.110e-16` |
| averaged spread on the edited source, rejector (p2) | `0.6817013` |
| averaged-carrier `lambda_min` at amplitude `0.40` (d1) | `0.03227752380131965` |
| averaged positivity boundary and margin (d2) | one onset; `s_avg = 0.42303983651076393`; margin `+2.034094e-04` |
| `L = 7` single-carrier spread (l2) | `0.4146141008085868` |
| `L = 7` averaged-carrier spread (l3) | `3.539e-16` |
| `L = 7` edited source (l4) | averaged defect `2.220e-16`; unaveraged violation `1.3036` |

Three readings deserve naming. First, the spread collapse in p1 is a property of
the `O`-invariant physical source, not an artefact of averaging: with the edited
source the averaged carrier's log-volume orbit spread is `0.6817013`, so
averaging does not manufacture isotropy where the source has none. Second, the
averaged carrier's positive-definiteness domain is not smaller than the single
carrier's; the boundary moves outward by `2.034094e-04`, and the averaged
`lambda_min` at amplitude `0.40` is `0.03227752380131965`, comfortably positive.
Third, the axes-only rejector recovers only the diagonal of a synthetic
symmetric form and misses its off-diagonal content by exactly `7.000000e-03`,
which is what makes the seven-direction recovery rows discriminating rather than
automatic.

## Theorem 2 in numbers

Theorem 2 predicts that the one-coset average over
`cell0 = [0, 6, 10, 12, 19, 21]` — the right coset `D3 g0` with `g0` the frame
of index `0` — is equivariant exactly under the conjugate subgroup
`g0^{-1} D3 g0`. Computed from the frame matrices alone, that subgroup is
`[2, 4, 11, 13, 17, 23]`. Measured independently, the set of frames at which the
cell-`0` coset average has equivariance defect below `1e-9` is
`[2, 4, 11, 13, 17, 23]`; the two sets are compared for equality in both
directions and agree. The largest defect over all 24 frames is `0.4580971`,
attained at frame `8`, so the coset average is not accidentally equivariant
anywhere outside the predicted subgroup. The six terms of the coset agree to
`1.456e-11`, which is the Cycle-696 pipeline's own `D3`-covariance floor, and
the four-term transversal average differs from the full 24-term average by
`3.640e-12`. The conjugate subgroup has the same order as `D3` and is a
different subgroup: relocation, not enlargement.

The four coset representatives are not interchangeable. On the physical source
at amplitude `0.40` the four pulled-back terms differ pairwise by as much as
`4.823389e-01`, so the four-term average is a genuine mixture and its agreement
with the 24-term average at `3.640e-12` is the coset collapse doing the work,
not four copies of one field.

## What this does not establish

(a) The averaged carrier is not a single-complex construction. Cycle 690's
no-go quantifies over constructions repeating one fixed triangulation and is
untouched by this cycle; the average repeats four.

(b) Cycle 696's `achievable_covariance_scope = 6` rows are untouched and remain
correct for the single-complex pipeline. Nothing here re-scopes them.

(c) Improper rotations, of determinant `-1`, are out of scope. `O` here means
the 24 proper cubic rotations and nothing larger.

(d) Odd `L` only. The pullback convention is geometric about a lattice-site
centre, so even sizes are not covered by these gates.

(e) No dynamics, no coupling, and no readout claim is made beyond the carrier's
transformation law. The averaged carrier is a transformation-law object; this
cycle does not attach an action, an energy, or an observable to it.

(f) All cited dependency notes are landed and unaudited on main.

## Reproduction

`python3 scripts/physical_orbit_averaged_all24_carrier_cycle701_2026_08_01.py`
— 36 PASS / 0 FAIL, exit 0, measured wall time of roughly 7 seconds per run on
the executing machine (`6.4` seconds in the tracked cold-run receipt), well
inside the registered budget. The `--no-receipt` flag suppresses
the receipt write and leaves the printed transcript unchanged; invoked without
it, the runner additionally writes its cold-run receipt.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 690 proper-cubic covariance ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md)
- [Cycle 695 direction set versus triangulation](PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md)
- [Cycle 696 joined compiler tournament](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)
- [Cycle 700 executed source-response-readout chain](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)

Backticked context only, with no links: `PR #5661`,
`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`,
`physical_operational_source_response_readout_chain_cycle700_2026_07_25.py`, and
`PORT_CANONICAL_COMMON_COFRAME_PHYSICAL_M2_COMPILER_CYCLE710_BOUNDED_THEOREM_NOTE_2026-07-26.md`.
