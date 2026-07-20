# Physical discrete source-law tournament — Cycle 490

Date: 2026-07-20
Authority: none
Audit: unset

## Frozen-before-output contract

Cycle 490 isolates the source-law wall after the positive Cycle487 local
physical compiler result. The compiler is not changed. The train boundary is
L13/a1/depth4 and the held boundary is L13/a2/depth4. Held rows never refit.
The terminal obligation is both (i) all four absolute rows within the numeric
tolerance 5e-10 and (ii) stronger-a2 order for both strengths.

The three executable routes were frozen before outputs:

1. **A — analytic source-word law.** Q1 occupation is one for both target
   strengths. Source strength is carried only by the uniform B20 word
   `round(256 sqrt(p_route))`; the square-root is fixed because the prior
   small-signal response is quadratic in source amplitude. Receiver word 256
   and one source pass remain fixed. There are no fitted parameters.
2. **B — two coherent source passes.** The original `p_route` occupations and
   word 256 remain, but the three local source vertices are executed twice
   before the fixed receiver vertices at every macro-step. The continued
   unitary state supplies the second pass; renewal count zero. The schedule
   has no fitted parameter and makes no many-Q claim.
3. **C — one train-only common source word.** The original `p_route`
   occupations remain. One common integer source word in `[1,1023]` is chosen
   using both a1 rows only, by a bounded scalar search (maximum 40 optimizer
   iterations, `xatol=0.25`) followed by the fixed integer neighborhood
   `+/-2`; ties choose the smaller word. There is one model parameter.
   Receiver word 256 remains fixed. Held values enter neither search nor
   selection.

All routes execute the same four declared coordinates. Q1 occupation is not
source strength. No route introduces source renewal, expectation feedback,
or a host force. Word choice, repeated schedule, and calibration remain
supplied candidate law structure.

The tournament reports coefficient rounding, compiler/product/angle
residuals, physical E/G and leakage separately from source-law/prediction
residuals. It also reports the pure-response held/train geometry ratio for
each route. A train-only global normalization can change absolute scale but
cannot repair stronger-a2 order when that pure-response ratio remains below
one. Normalization freedom and geometry/propagation freedom are therefore
not conflated.

## Controls and ceiling

The logical predictions use the declared L13 state exactly. The already
proved local Cycle487 seam is rerun for every distinct word and supplies a
depth/factor state ceiling. This is not a complete L13 physical-shell
execution. All 24 proper-cubic frames, inverse/code return, one-particle mass,
Cycle-230 contact, boundary norm weight, source/receiver/field-stream/
packet-stream/contact/repetition deletions, and malformed domains remain
explicit.

Response is not gravity. Phase is not energy. A generator is not a rate.
Depth is not time. Norm weight is not probability. Pointer state is not a
Record.

## Result boundary

The output section is populated only after the above model complexity,
selection rule, and terminal obligation are frozen. A failed route remains a
route-specific source-law result. An unfinished physical shell remains an
implementation boundary. Neither is constitutional evidence.

## N1 — alternative route enumeration

The attempted families are analytic source-word normalization, repeated
local source excitation, and one train-only calibrated coupling. Distinct
live families retained outside this cycle are nonlinear/saturating word maps,
true coherent many-Q sources, an explicit renewable reservoir, the Cycle213
retarded field, the Cycle216 static exchange, and the Cycle425 common
transient/stationary update.

## N2 — pairwise wall-independence audit

Word normalization does not imply repeated excitation. Repetition does not
imply train calibration. Calibration does not fix propagation/geometry or
the incomplete L13 shell. None of these supplies an energy-stress identity,
metric law, or gravity interpretation.

## N3 — hidden-wall trigger scan

The analytic square-root map, integer rounding, P8/Suzuki4/B20 primitives,
fixed receiver word, pass count and order, zero renewal, optimizer bounds and
neighborhood, state preparation, factor order, packet observable, geometries,
targets, and tolerances are supplied.

## N4 — exact residual matching

Local compiler residuals close only the local E/G seam. Four row residuals
and held ordering test the source law plus finite propagation. The L13 shell
is separate. The runner prints these residual classes separately.

## N5 — scope and rhetoric audit

Any negative is bounded to three frozen laws, two strengths, L13/depth4, a1
train, and a2 held. It is not a universal lattice, source-law, gravity,
minimum-content, or impossibility result.

## N6 — live partial-closure paths

Nonlinear word maps, true many-Q execution, explicit renewal, retarded/static/
dressed field joins, alternative domains, and the complete shell remain live.

## N7 — steelman

A hostile reviewer can fit a two-parameter analytic source law on the two
train rows, then test it without refit at held a2; or add a locally conserved
renewable source reservoir while leaving the Cycle487 compiler unchanged.
Either mechanism can change more than a global scale and directly attacks
the still-open geometry/order residual.

## N8 — cross-cycle echo and claim gate

Cycles432-to-435 and 447-to-450 retired finite residuals by enlarging or
composing constructions. Cycles213, 216, and 425 already expose distinct
field mechanisms. Therefore the allowed claim is a bounded source-law
tournament only. Broad no-go, shared-obstruction, minimum-content, and
axiom-pressure claims all fail their promotion gates; there is no axiom
pressure.

## Outputs

The frozen runner completes with `12 PASS / 0 FAIL`. The final cold execution
took `25.1532040001 s`, with peak RSS `931.6875 MiB`.

Route C selected uniform source word `304` from ten train-only word
evaluations. The normalized train objective was
`1.3341547357162572e-5`; held values used in selection were zero.

### Four-row results

The rows below are `(predicted width shift, prediction minus Cycle420
target)`.

| route | a1 unit | a1 coefficient-two | a2 unit | a2 coefficient-two |
|---|---:|---:|---:|---:|
| A, analytic words 31/70 | `(4.941938135522017e-7, -1.750891776980401e-7)` | `(2.513490503119886e-6, -8.622552438164455e-7)` | `(4.462784972819600e-7, -8.735111136498608e-7)` | `(2.269748092600943e-6, -4.386253058527578e-6)` |
| B, two source passes | `(1.695821839675649e-6, +1.026538848425407e-6)` | `(8.551224973479820e-6, +5.175479226543489e-6)` | `(1.529556550042277e-6, +2.097669391104562e-7)` | `(7.712852357136257e-6, +1.056851206007736e-6)` |
| C, train-only word 304 | `(6.710896225115004e-7, +1.806631261258573e-9)` | `(3.384052440755236e-6, +8.306693818904698e-9)` | `(6.057515896246146e-7, -7.140380213072062e-7)` | `(3.054581118031030e-6, -3.601420033097491e-6)` |

No route meets the four-row `5e-10` obligation. Route A's maximum absolute
residual is `4.386253058527578e-6`; route B's is
`5.175479226543489e-6`; route C's is `3.601420033097491e-6`. Route C shows
that one train-only normalization can bring the a1 rows much closer, but the
integer word alone does not even close those two rows at the frozen numerical
tolerance and does not transfer to a2.

### Geometry/order result

The predicted held/train ratios are:

| route | unit | coefficient-two | stronger a2? |
|---|---:|---:|---|
| A | `0.9030434721029134` | `0.9030263252570890` | no |
| B | `0.9019559214633228` | `0.9019587697734963` | no |
| C | `0.9026388865285038` | `0.9026400067693169` | no |

The corresponding pure-response geometry ratios are A
`0.9030434721029134 / 0.9030263252570890`, B
`0.9020021134606610` for both labels, and C `0.9026570689720224` for both
labels. Word choice and repetition could have changed the nonlinear local
dynamics in principle. They did not change its geometry order here. Once
these pure ratios are observed below one, a further global output
normalization cannot reverse the ordering.

### Compiler and physical controls

The distinct physical words are `31`, `70`, `256`, and `304`. Their maximum
product-formula, discrete-angle, and total-compiler operator residuals are,
respectively, `3.471821048319696e-5`, `4.330514516947890e-5`, and
`4.329681046040419e-5`. The exact telescoping ceilings for the declared
depth-four factor counts are `4.986537632586810e-4` and
`7.382116803892657e-4` for A's two strengths, `6.559498645932462e-4` for B,
and `7.201421851959094e-4` for C. The maximum declared-route ceiling is
`7.382116803892657e-4`. These ceilings compare each discrete word with its
exact continuous word; the reported prediction rows execute the discrete
word itself, so this compiler residual is not used to repair or excuse a
source-law residual.

Across all used words, local physical E/G is at most
`1.5612511283791264e-16`, code leakage is at most
`2.5004485323718623e-15`, and the full 448-dimensional covariance residual is
exactly zero in all 24 proper-cubic frames. Train/held inverse residuals are
at most `3.933869567477795e-15`; norm error is at most
`2.220446049250313e-16`. Boundary norm-weight ceilings stay below the frozen
`0.10` bound.

At depth four, source, receiver, field-stream, packet-stream, and one-of-two
source-pass deletion residuals are `0.2563058947796694`,
`0.002827016515066671`, `0.302883434865584`, `0.17127287648667747`, and
`0.22054338667005016`. Contact deletion is zero on that particular lawful
one-source sector, while the dedicated two-particle contact fixture remains
nontrivial at `0.36789306705608243`; it retains 645 nontrivial columns. The
one-particle mass remains `0.4534056541748851`, with eigen residual
`3.534751832054436e-16`. Five malformed domains are refused.

Route B uses six local source-star actuations per macro-step rather than
three, while keeping three fixed receiver-star actuations. The continued
unitary state supplies the second pass; preparation/renewal count remains
zero. This is repeated actuation, not a many-Q construction.

### Disposition and next route

All three terminal obligations fail route-specifically. The common retained
signal is the approximately `0.902` pure geometry ratio across materially
different normalization and repetition choices. That is useful finite-domain
evidence directing the next campaign toward a geometry-changing carrier or
propagation law, not constitutional evidence. The highest-value distinct
next tournament is a frozen join from the Cycle487 local source compiler into
the Cycle213 retarded carrier, Cycle216 static-exchange carrier, and Cycle425
common transient/stationary update, each with the same a1-train/a2-held row
and order obligations. True many-Q and explicit renewable-reservoir source
routes remain independently live.

The complete L13 three-M64 physical shell is still open. The exact declared
logical prediction plus local physical seam and compiler ceiling is the
bounded result. Broad no-go, shared-obstruction, minimum-content, and
axiom-pressure claims fail their promotion gates; there is no axiom pressure.

## Verification

```text
python3 scripts/physical_discrete_source_law_tournament_cycle490_2026_07_20.py
```

An independent root cold run returned **12 pass / 0 fail** with an
instrumented probe-body time of `20.39872924995143 s` and peak internal RSS
of `1,173.859375 MiB`, inside the declared `900 s / 3,072 MiB` caps. Complete
process launch, dependency import, and execution took `99.47 s` with
`1,230,880,768` maximum resident-set bytes under `/usr/bin/time -lp`. The
packaged runner SHA-256 is
`47609253d3a868a0f736f0c9571a7a6a0878776590af6ddf24d4e6ca9fe80ff4`.
