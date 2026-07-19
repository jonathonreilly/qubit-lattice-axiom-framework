# Physical test-matter recoil receiver and multiedge prediction bridge — Cycle 429

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is edited or proposed.

Companion runner:

```text
scripts/physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19.py
```

## Result up front

Cycle 429 turns the Cycle-426 two-cell source/recoil seam into a bounded
three-cell/two-edge shared-middle installation. A prepared reservoir at A
emits into literal directional hard-core field sites; ordinary edge-bit SWAPs
carry the excitation across A--B and B--C; and the distinct physical M64 cell
at C absorbs through the same recoil vertex. The A/B/C roles can be exchanged,
giving the reciprocal C-to-A process.

The declared logical code is

```text
Cycle-319/396 988-state n<=3 three-cell matter shell
tensor
complete Q=1 sector of 21 hard-core M2,

dimension = 988 x 21 = 20748.
```

Each cell has one reservoir M2 and six directional field M2. The shared B
matter cell, field star, coin, source vertex, and contact factor occur once.
The two field edges use the distinct middle rails `B,-x` and `B,+x`, so their
SWAPs commute exactly. The two inherited matter FSWAPs also commute on this
straight path because they exchange those distinct modes. Reversing the
listed edge order changes no operator, while the nonduplicated shared-middle
factorization remains explicit.

On train L5 and held L6, for both A-to-C and C-to-A roles, the runner checks

```text
E_429 G_429 = G_physical,429 E_429
```

with maximum forward residual `1.3847389753136969e-14`, maximum inverse
residual `1.71582756244221e-14`, and maximum norm drift below
`3.8e-13`. A translated held L6 origin passes all six matter-factor Gram
tests at `7.771561172376096e-16`.

This is the first physical test-matter receiver in this campaign whose
readout is produced by the same local matter/field recoil law as its emitter.
The readout is an operational reservoir occupation and a
matter-direction/recoil observable. It is not a force, physical momentum,
energy, stress, gravitational source, gravity observable, probability, or
Record.

The certified controls include a reciprocal source/receiver role swap, a
one-edge and two-edge no-refit response, and held L=6 origins.

## Fixed three-cell law

Cycle 429 uses the fixed Cycle-426 local source law

```text
H_rec = sum_d [
    a^dagger_bar(d) a_d sigma_R^- sigma_d^+
  + a_d^dagger a_bar(d) sigma_R^+ sigma_d^-
],

V_rec = exp(+i theta H_rec),
theta = 0.8 m = 0.3627245233399082.
```

The prepared-source calibration, sign, zero, and blank field remain supplied.
The source and receiver use exactly the same finite vertex; no occupation
expectation, branch query, or fitted distance coefficient selects a gate.

For an A-to-C role, one update is:

1. one onsite Cycle-219 matter coin on A, B, and C;
2. one full six-direction field coin on each literal field star;
3. the A, B, and C recoil vertices, each once;
4. the two Cycle-319 matter FSWAPs, AB and BC;
5. the two ordinary directional field-bit SWAPs, AB and BC; and
6. one Cycle-230 contact layer.

The C-to-A role lists the cell and edge factors in reverse. Because the local
sources and the two distinct-rail edge factors commute, the role exchange is
an exact member of the same covariant family. The adjoint reverses every
factor. Steps are not time, and scheduled adjoint return is not autonomous
recurrence.

No expectation controls a gate.

## Source, transport, and physical receiver

The initial A-to-C preparation is one occupied A reservoir, blank B/C
reservoirs, all eighteen field M2 blank, and the frozen Cycle-396 three-cell
matter column. The role-swapped preparation uses the corresponding C
reservoir and arm-exchanged matter column. Total field/reservoir `Q` is one.

With the angle and schedule frozen once, the readouts are:

| role | one-edge B response after two steps | two-edge endpoint response after three steps |
|---|---:|---:|
| A to C | `0.000243452351055388` | `0.00013490525789067813` |
| C to A | `0.00024345235105538803` | `0.00013490525789067805` |

The one-edge reciprocity residual is below `6e-20`; the two-edge residual is
`8.131516293641283e-20`. No coupling, angle, coin, contact, or readout
coefficient is refit between one and two edges. The smaller two-edge value is
an output of this fixed finite schedule, not a continuum distance law.

The first-update adjoint residuals are
`3.0668100551278036e-15` and `2.917103987852459e-15`. Norm after three forward
updates is one within `1.8e-15` on the logical code.

## Matter-direction/recoil observable

At the receiver vertex, Cycle 429 evaluates only after the gate the local
coordinate

```text
D_rec = D_matter + 2 D_field.
```

For A-to-C absorption, the receiver changes by

```text
Delta D_matter,C =
(+1.53739423e-4, +1.78496065e-19, +9.79129173e-20),

2 Delta D_field,C =
(-1.53739423e-4, 0, 0).
```

The vector-ledger residual is below `3.5e-18`. Under source/receiver role
swap,

```text
Delta D_matter,A =
(-1.53739423e-4, -1.62365244e-18, -4.43048148e-19),
```

and its field leg cancels locally to below `4e-18`. The sum of the two
role-swapped matter-direction changes is below `7.1e-18`. Receiver reservoir
gain at the exposed vertex is the two-edge response to rounding.

The source generator's complete Q1 sparse operator has zero Hermiticity
residual and zero commutator with all three components of `D_rec`. Each edge
SWAP has an exact cell-current identity: left change plus right change is zero,
the nonincident cell change is zero, and total Q change is zero. Direction
current is not force, momentum, energy, stress, or gravity.

## Deletions

The forward two-edge baseline is `0.00013490525789067813`. Independent fixed
deletions give:

| deletion | C-reservoir response |
|---|---:|
| source A coupling | `0.0` |
| receiver C coupling | `0.0` |
| first transport edge AB | `0.0` |
| second transport edge BC | `0.0` |
| blank source preparation | zero output norm |
| middle B coupling | `0.00013721258943103526` |
| contact | `0.00012992082665171258` |

The middle and contact deletions are visible rather than silently declared
necessary. Source coupling, receiver coupling, transport, and contact
deletions are all kept distinct.

## Physical compiler, support, frames, and held origins

The physical encoding is

```text
E_429 = E_319/396 tensor I_Q1.
```

Each projected matter factor uses its inherited identity completion off the
code; the 21 field coordinates are literal hard-core sites. Matrix-unit
completion and primitive synthesis remain supplied/open, as in Cycle 396.

Exact physical tests:

| L / role | Gram maximum | E/G | inverse |
|---|---:|---:|---:|
| L5 A-to-C | `7.77e-16` | `1.3847389753136969e-14` | `1.71582756244221e-14` |
| L5 C-to-A | `7.77e-16` | `1.3833392341783028e-14` | `1.7144221053039546e-14` |
| held L6 A-to-C | `7.77e-16` | `1.3847389753136969e-14` | `1.71582756244221e-14` |
| held L6 C-to-A | `7.77e-16` | `1.3833392341783028e-14` | `1.7144221053039546e-14` |

The held translated origin `(3,2,1)` uses cells
`(3,2,1),(4,2,1),(5,2,1)`. All six factor orders remain isometric. The fixed
origin matter union is 118 M2; this translated held union is 122 M2. Including
the three-M2 S3 role register and 21 literal field M2 gives tested patch sizes
142 and 146 M2. These are bounded patch counts, not minima. The homogeneous
installation remains 29 matter plus seven reservoir/field M2 per cell, or 36
M2 per coarse cell. A local recoil vertex has an 18-M2 matter union plus its
seven-M2 star, support 25.

The factor family passes all 24 proper-cubic frames. The inherited matter
schedule has zero maximum covariance residual, zero failures in 576 frame
group-law tests and 4,096 translations, and exact arm exchange. The new
two-edge stream has maximum frame residual `0.0`; the source-vertex maximum is
`8.807749891993861e-16`.

L3 remains the Cycle-396 rejecting wrap control and is not used as a physical
isometry. L5 is training and L6 is held. The held coupling, schedule, path,
and readout are unchanged.

## Mass and contact fixture

The same common code retains:

```text
Cycle-219 mass                  0.4534056541748851
three-cell rest mass           0.4534056541748851
one-particle eigen residual    3.534751832054436e-16
Cycle-230 contact columns      645 nontrivial.
```

The receiver direction observable is generated by the recoil vertex, while
the mass fixture and contact remain separately visible factors. No contact
work law, dressed inertial mass, or binding theorem is inferred.

## Cycle-420 typed prediction map

Cycle 420 marked every named legacy surface's physical source E/G and physical
test-matter readout false because its densities, profiles, packets, centroids,
widths, and fits were host objects. Cycle 429 adds a bounded near-side seam,
but it does not connect that seam by exact E/G to any named Cycle-420 host
pipeline:

| Cycle-420 surface | bounded near-side source seam | bounded receiver seam | Cycle-420 physical source E/G | Cycle-420 physical test-matter readout | host profile join | host packet join |
|---|---:|---:|---:|---:|---:|---:|
| causal ratio | true | true | false | false | false | false |
| impact parameter | false | false | false | false | false | false |
| quadrupole width | false | false | false | false | false | false |

For the causal interface, the two near-side “true” entries mean only that a
positive prepared reservoir now emits, traverses one/two bounded edges, and
changes a distinct physical receiver under one E/G law. The named Cycle-420
surface flags remain false because there is no E/G into its host density
profile, detector centroid, continuum causal ratio, or clock. The old typed
contract is narrowed but not satisfied.

The current path is collinear, so it does not earn the transverse
impact-parameter geometry. The current preparation is one positive source,
so it does not earn the signed `(+1,-2,+1)` quadrupole profile or a packet
width. Host packet/profile joins remain false for every row. No named legacy
prediction surface is closed.

## Relation to Cycles 396, 425, and 426

Cycle 396 supplied the nonduplicated physical three-cell matter shell and a
global-Q1 abstract carrier response. Cycle 429 replaces that carrier label by
three literal seven-M2 hard-core stars and exposes a same-law receiver
matter-direction change. It uses only the coefficient-two route; no claim is
made that the distinct Cycle-396 unit-weight auxiliary inventory is thereby
represented.

Cycle 425 supplied a full cubic Q1 coin--vertex--stream update and a common
transient/stationary source-centered branch, but matter/contact were
spectators and stationary eigenpair preparation remained host-supplied.
Cycle 429 uses the same physical field-factor pattern on a finite two-edge
path and replaces the scalar spectator vertex by the matter-controlled recoil
law. It neither imports nor extends the host-selected stationary eigenpair or
shifted-Green comparison.

Cycle 426 supplied the exact two-cell Q<=2 recoil/field seam. Cycle 429 widens
its spatial light cone to two edges and introduces a distinct physical M64
receiver, while narrowing the executed field sector to complete global Q1.
Thus Cycle 429 adds distance, overlap, receiver, and typed-prediction evidence;
it does not supersede Cycle 426's two-source Q2 result.

## Supplied, derived, and open

Supplied:

1. the Cycle-319/396 `n<=3` three-cell matter shell, local checks/Wilson
   sector, S3 role register, two path FSWAPs, and identity completion;
2. the Cycle-426 coefficient-two hard-core recoil vertex and `theta=0.8m`;
3. three reservoir M2, eighteen directional field M2, and complete global-Q1
   preparation;
4. the Cycle-425/426 coin--source--stream pattern specialized to two ordinary
   path-edge bit SWAPs;
5. prepared endpoint reservoir/matter columns, path boundary, role family,
   frames, train/held origins, and readouts.

Derived:

1. same-law source emission and distinct physical M64 receiver absorption
   across two edges;
2. a nonzero receiver matter-direction change with exact local
   coefficient-two balance;
3. reciprocal A/C role swap and one-edge/two-edge no-refit response;
4. physical E/G and inverse, total-Q/current, mass/contact, deletion,
   covariance, overlap, and held-origin controls; and
5. a typed Cycle-420 causal/impact/quadrupole interface update with all host
   named-surface E/G/readout flags and host joins left false.

Open:

1. complete Q2 and higher three-cell histories and a homogeneous full cubic
   matter/source/receiver network;
2. primitive synthesis replacing inherited matrix-unit completion and
   autonomous source preparation/recurrence;
3. a signed quadrupole source, transverse impact geometry, local replacement
   for host profiles, packet observables, and empirical prediction
   calibration;
4. contact work, a physical clock, actual Records, Born law, physical
   energy/stress/source selection, metric dynamics, and gravity.

There is no global Jordan--Wigner order, parity string, nonlocal parity
service, host branch, or expectation-derived gate. The global Q1 sector and
input preparation are supplied explicitly.

## Six-wall ledger effect

| wall | Cycle-429 effect | still open |
|---|---|---|
| `C_ref` | unchanged; the finite readout needs no host feedback | source preparation, coupling normalization, empirical reference/calibration |
| `C_num` | exact global Q1 and edge-current ledgers on a three-star physical network | Q2+ multiedge execution and physical energy/stress interpretation |
| `C_wrap` | L5/held-L6 path response is separated from the rejected L3 shortcut | event equivalence, physical clock, interval/rate calibration |
| `C_int` | a distinct receiver's matter direction responds through the emitter's same recoil law while contact stays active | contact work, dressed inertial response, autonomous recurrence |
| `C_local` | advances from a two-cell patch to a nonduplicated three-cell/two-edge physical E/G compiler with held origins | primitive synthesis and homogeneous full cubic network |
| `C_source` | a prepared local reservoir produces reciprocal one-/two-edge physical receiver coordinates | physical source selection, signed/transverse profiles, prediction and tensor/metric calibration |

The main advance is in `C_int`, `C_local`, and the operational near side of
`C_source`. No wall is declared closed.

## Scientific disposition

This is a positive construction. The no-go-discipline guardrail was applied
only to prevent unfinished Q2, cubic-network, prediction, clock, and metric
work from being mislabeled as obstruction evidence. No broad negative is
offered for N1--N8 certification.

No no-go, minimum-content, shared-obstruction, or axiom-pressure claim is
made. Authority remains none and audit remains unset.

## Verification

```bash
python3 -m py_compile \
  scripts/physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19.py

python3 -u \
  scripts/physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19.py
```

Expected cold result:

```text
RESULT PHYSICAL_TEST_MATTER_RECOIL_RECEIVER_MULTIEDGE_PREDICTION_CERTIFIED
```
