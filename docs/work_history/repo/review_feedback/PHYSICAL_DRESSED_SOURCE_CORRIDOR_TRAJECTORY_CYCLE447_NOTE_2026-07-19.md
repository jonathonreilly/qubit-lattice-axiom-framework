# Physical dressed-source corridor trajectory — Cycle 447

Date: 2026-07-19

Authority: none

Audit: unset

## Frozen question and construction order

Cycle 447 tests the smallest live Cycle-442 A2/corridor hybrid: can a supplied
mass-conditioned Cycle-425 dressed Q1 source drive a repeated physical M64
receiver corridor through one autonomous joint update, without converting the
field to a host array or applying a host force each update?

The joint update is constructed before preparation.  It consists of the
inverse-sign form of the already compiled Cycle-446 full NN functional source
gate, the Cycle-425 field coin and three-dimensional stream, the same
functional test-mass coin/recoil law, and a repeated Cycle-435/Cycle-319 M64
one-particle corridor.  Only afterward are source and test register eigenrays
used for supplied preparation and measurement.  The mass-conditioned dressed
state is supplied host preparation: its eigensolver, candidate selection,
normalization, and phase convention are not autonomous physical generation.

The receiver consumes the joint field amplitudes directly.  There is no
c-number field, no expectation-value control, and no per-update host force or
profile.  The source is not refreshed.  Field and receiver backreaction remain
inside the same evolving state.

## Frozen train, held, and fit contract

An explicit L9 pilot calibrated runtime and exposed a nonzero joint trace.  It
is retained as the L9/depth12 calibration geometry and is not called blind.
Before any L13 result, the campaign freezes the L13/depth18 blind held geometry.
Both use a radial 9- or 13-cell M64 corridor, packet center `x=3`, momentum
width `0.35`, source at the origin, the same preparation rule, and the same
factor order.  Boundary probability must remain below `0.25`, selected-band
weight above `0.80`, and norm/inverse residuals below the stated numerical
tolerances.

Two classifiers are reported independently:

- the raw classifier consumes every joint update;
- the two-update stroboscopic classifier consumes only even-update samples.

Both freeze BIC advantage greater than `6`, second-difference CV below `0.25`,
duration ratio within `25%` of `4`, curvature above `1000` times the `8e-13`
floor, and at least four same-sign nonzero second differences.  Strobing may
diagnose a QCA envelope but cannot erase or relabel a failed raw law.  A strict
sustained result requires both classifiers.

## Required controls

The runner keeps the Cycle446 NN source compiler separate from the larger
joined dynamics.  It checks both full Cayley and principal inverse schedules,
their exact post-construction projection to the Cycle425 source vertex, and
their two-M2 maximum primitive support.  The repeated physical M64 corridor
is separately checked for local E/G, inverse-by-adjoint, Gram, leakage,
constant per-cell support, and inherited bounded intercell FSWAP compilation.

The joint tournament reports source-only eigen residual, joined source drift,
backreaction residual, norm, inverse, boundary, selected-band, raw fit, and
stroboscopic fit.  Fixed-preparation source-vertex, test-recoil, field-stream,
matter-stream, mass-law, and dressed-preparation deletions remain distinct.  A
no-refresh autonomous update check requires zero source refreshes, zero host
forces, and zero c-number control invocations.  The local laws and the rotated
corridor family are checked in all 24 proper-cubic frames.  Cycle-219 mass and
Cycle-230 one-particle/full-code contact controls remain explicit.

## Prediction and semantic boundary

Cycle 204's Hamiltonian, strict-QCA, and bound-composite rows and Cycle 210's
three exact mass/forced-lapse rows are comparison contracts only.  They are
not silently reproduced by the Cycle-441 register masses.  The broad-gravity
inputs `L^-1=G_0`, `rho=|psi|^2`, and `S=L(1-phi)` remain underived and false
as closure flags.

The dressed eigenphase is not a rate, update count is not time, and the
coordinate centroid is not a clock.  Field occupation is not energy, stress,
or gravity.  There is no gravity, lapse, proper-time, no-go, minimum-content,
shared-obstruction, or axiom-pressure claim.  Pointer-free coherent weights
are not Born probabilities, occurrences, or Records.

## Supplied structure

Supplied structure includes two one-hot nine-M2 registers, their internal
orientation and Cayley/principal functions, the inverse source-sign choice,
coupling scale, host eigenpair selection/preparation, periodic field and
corridor layouts, packet preparation, source/receiver coordinates, factor
order, depths, fit thresholds, local identity completions, and diagnostic
readouts.  Primitive physical preparation, empirical law selection,
many-excitation autonomous recurrence, source energy/stress calibration,
metric dynamics, clocks/proper time, Records, Born/occurrence, and realized
history remain open.

## Result

Cycle 447 is a `partial-attempt-with-named-untested-routes`.  Two independent
facts prevent certification:

1. the frozen `0.25` finite-volume boundary control fails for the L9
   train-sector-1 row, which reaches `0.26877389587476075`; and
2. all six traces fail both the raw and two-update-stroboscopic sustained
   classifiers under the frozen thresholds.

The second fact is not inferred from the first.  The three held rows pass the
boundary, band, norm, source-eigen, backreaction, and inverse controls but
remain transient or oscillatory at the tested resolution.

| law/test/geometry | final free-subtracted centroid | raw BIC advantage | raw second CV | raw duration ratio | strobe BIC advantage | strobe second CV | strobe duration ratio |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cayley train-1 L9 | `-0.00759156197047961` | `13.30154642251144` | `1.4247025358931868` | `3.4653362718633387` | `8.49612523533644` | `1.366384242161217` | `3.4653362718633387` |
| Cayley train-2 L9 | `-0.02577498230710118` | `15.51006614949585` | `2.7380762222950827` | `5.980177552398715` | `10.27125608776128` | `2.5323891334663924` | `5.980177552398715` |
| Cayley train-3 L9 | `-0.055368509182318615` | `38.00126564998734` | `1.9330540433256134` | `4.532827873427511` | `28.08826834924368` | `0.3985665938866696` | `4.532827873427511` |
| Cayley train-2 L13 | `-0.048439634151937305` | `41.28956710188683` | `6.96577387640263` | `5.513661354112355` | `27.11669335606175` | `2.2564999028858077` | `6.123680901265709` |
| Cayley held alias L13 | `0.16400617791800087` | `16.74582801538983` | `39.64131417398674` | `3.045090517208613` | `8.45679724173259` | `8.701442076637793` | `3.030209344838329` |
| principal held alias L13 | `-0.00873986807576621` | `64.21031296597986` | `2.1662549526884822` | `6.559382913817233` | `41.54868083556019` | `0.6007833393731985` | `10.447412021877154` |

Thus there are `0/6` raw genuine-acceleration rows, `0/6` stroboscopic
genuine-acceleration rows, and `0/6` strict sustained rows.  The BIC columns
show that a quadratic fit often wins; the CV and duration columns show why
that win is not promoted over the exact finite-step trace.

The maximum norm error is `1.6964207816272392e-13`, the maximum one-step
inverse residual is `2.0398656168204793e-15`, and the maximum source-only
eigen residual is `3.816553791308641e-15`.  Held selected-band weights are at
least `0.9453101371729516`, and held boundary probability is at most
`0.12817603166280017`.  Joined source reservoir drift ranges from
`-0.008127112555884053` to `-0.057566579878281454` on held rows, while the
final backreaction residual ranges from `0.09138866978219919` to
`0.4133889759619333`.  This distinguishes an initially stationary source from
the nonstationary joined source/receiver state.

Test-recoil and mass-law deletions reduce the maximum centroid effect below
`7.2e-14`.  Source-vertex, field-stream, matter-stream, and dressed-preparation
deletions change the intact trace by respectively
`0.00034146087757788506`, `0.009404748836725004`,
`0.041037516214339`, and `0.03497143294191739`.  No source refresh or
per-update host force occurs.

## No-Go Discipline Gate

Gate status: **FAIL for any broad passive-trajectory or gravity no-go**.  The
result is demoted to `partial-attempt-with-named-untested-routes`.  The only
licensed negative is that the frozen L9/L13 dressed-source/corridor candidate
does not certify a strict sustained trajectory and also violates one declared
training boundary control.

### N1 — alternative route enumeration

| route | truth marker | disposition |
|---|---|---|
| supplied source-only dressed preparation plus L9/L13 repeated M64 corridor | `ATTEMPTED` | all six raw/stroboscopic classifiers fail; one L9 row also violates the boundary control |
| wider L17/L25 physical corridor with a narrower band packet | `UNTESTED` | may reduce finite-volume and QCA micromotion; frozen as a separate future cycle, not a repair |
| eigenstate or quasistationary preparation of the full joined source/receiver update | `UNTESTED` | could reduce the immediate backreaction drift introduced by the product preparation |
| many-Q coherent field with autonomous reservoir recurrence | `UNTESTED` | could sustain the profile while distributing depletion across more than one Q1 excitation |
| Cycle-213 retarded field compiled on physical M2 and joined to the corridor | `UNTESTED` | would test finite-speed sustained sourcing without a c-number adapter |
| finite reversible Cycle-216 static-exchange compiler joined to physical matter | `UNTESTED` | could supply a different autonomous approximation to the static response |
| carried or distributed dressed source with recoil | `UNTESTED` | could remove the fixed point-defect preparation and test reciprocal source motion |
| alternative local packet/readout macrocycle beyond two-update strobing | `UNTESTED` | could distinguish a longer QCA microperiod without changing the underlying update |

N1 fails the broad negative because seven distinct constructive routes remain
untested.  The latest skill's closed-route honesty vocabulary cannot label
them `ATTEMPTED` or `RULED OUT BY PRIOR`; their explicit `UNTESTED` markers are
therefore themselves the failure evidence.

### N2 — wall-independence audit

After collapsing target-like wording, the open conditions are `R`, autonomous
source preparation/recurrence, and `P`, wide finite-volume packet resolution.
Sustained trajectory is the target conditional on them, not a third inflated
wall.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `R,P` | no | no | yes |

Energy/source calibration and a metric are downstream of a gravity claim and
are not counted as walls in this narrower trajectory attempt.

### N3 — hidden-condition scan

The note and runner were scanned for “we assume,” “by construction,” “as is
standard,” “framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  No hit supplies a
load-bearing step.  “Supplied,” “prepared,” “fixed,” and “conditional” clauses
are explicit program inputs belonging to `R` or `P`; they are not hidden
admissions.

### N4 — residual matching

| witness | witness residual | Cycle-447 residual | exact match? |
|---|---|---|---:|
| Cycle 442 A2 boundary | mass-conditioned dressed preparation and joined backreaction untested | directly attempted here | yes |
| Cycle 425 open list | eigenpair selection/preparation supplied; joined matter absent | preparation remains supplied and joined drift is measured | yes for the named inputs, not negative authority |
| Cycle 435 open list | three-cell packet width, no wide trajectory | repeated corridor compiler used here | yes as substrate predecessor, not negative authority |
| Cycle 446 scope | bounded source gate compiler, no passive trajectory | source compiler input used here | yes as compiler predecessor, not negative authority |
| Cycle 204/210 trajectories | supplied external force/lapse gives operational acceleration | no host force here | no; comparison-only and dropped as negative support |

Only the Cycle-447 rows support the frozen-route negative.  Positive
predecessors and host-force comparators are not counted as evidence against
other routes.

### N5 — rhetoric audit

“The candidate does not certify a sustained trajectory” applies to six
declared block/corridor rows at L9/L13 and the raw/two-update resolutions.  It
is not asserted per every local mode, every packet macrocycle, every larger
lattice, many-Q fields, or lattice-wide/continuum dynamics.  “No c-number
field controls the receiver” is checked at every executed joint update; it is
not a claim that c-number effective fields can never emerge.  “No gravity” is
a semantic scope statement that source calibration and metric response were
not constructed, not a negative theorem about gravity.

### N6 — partial-closure path scan

Concrete closures need no axiom prose: enlarge the corridor while retaining
the frozen law; construct a preparation for a quasistationary branch of the
joined update; execute a many-Q recurrent source; or compile the Cycle-213/216
field carriers on the same physical code.  Cycles 425, 435, 442, and 446 are
existing partial primitives for those paths.  No approved primitive is
misclassified as a wall, and no “new axiom required” statement is made.

### N7 — hostile steelman

A hostile reviewer should reject any broad negative.  The source-only dressed
state is deliberately multiplied by a receiver packet and immediately ceases
to be stationary, as the measured backreaction residual shows.  A dressed or
Floquet-like eigenpacket of the full joined update could suppress that drift;
a wider L17/L25 corridor could also reduce the exact boundary and micromotion
contamination while leaving the local Cycle446/Cycle435 factors unchanged.
Cycle 425 already proves stationary dressed branches exist for the source
update, and Cycle 210 proves wide packets accelerate under a sustained
supplied field.  Their combination is untested, so the steelman is strong and
the broad no-go fails.

### N8 — cross-cycle echo

Cycle 419's injected source orbit was nonstationary, but Cycle 425 enlarged
the preparation and found a stationary dressed eigenstate.  Cycle 429's
single direction readout became Cycle 435's physical packet, and Cycle 441's
dense controller became Cycle 446's NN physical compiler.  Each similar wall
was narrowed by enlarging the lawful construction rather than by adding an
axiom.  The same mechanism could turn the present product-preparation or
finite-volume residual into a positive result, so only the frozen-route
disposition is retained.

The post-gate cold runner reports `9` passes and `1` failure, with
`authority: none` and `audit: unset`.  The result is
`PHYSICAL_DRESSED_SOURCE_CORRIDOR_TRAJECTORY_NOT_CERTIFIED` because the frozen
train boundary control is intentionally preserved.

## Verification

```bash
python3 -m py_compile \
  scripts/physical_dressed_source_corridor_trajectory_cycle447_2026_07_19.py
python3 \
  scripts/physical_dressed_source_corridor_trajectory_cycle447_2026_07_19.py
```
