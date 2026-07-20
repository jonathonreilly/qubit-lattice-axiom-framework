# Physical relaxed cubic field / passive M64 backreaction — Cycle 464

Date: 2026-07-19

Authority: none

Audit: unset

## Frozen question and claim boundary

Cycle464 asks whether a finite three-dimensional relational field can drive a
bounded passive response and reciprocal backreaction in actual repeated
physical M64 test matter without a host per-step force or control.  It imports
the final Cycle463 locally relaxed word field by executable module/function,
not by copying its result table.  Cycle461 is comparator only; its supplied
rational orbit profile is not consumed by the Cycle464 update.

The train R1/padR2/depth4 geometry uses the Cycle463 field on `[-1,1]^3`
inside a one-shell-padded matter cube `[-2,2]^3`.  The held R2/padR3/depth6
geometry uses the no-refit Cycle463 field on `[-2,2]^3` inside
`[-3,3]^3`.  Both use the same mass, coin, same 42-dimensional local vertex,
neighbor rule, Q1 normalization rule, hard-wall matter stream, and readouts.

The allowed positive claim is a bounded passive response/backreaction fixture.
It is not sustained acceleration, a universal equivalence law, a metric
response, or derived gravity.  The local vertex and the prepared directional
field are supplied force-like controls.  Their physical execution is tested;
their empirical selection and gravitational interpretation are not derived.

Cycle464 is a `partial-attempt-with-named-untested-routes` at framework scale,
even if every bounded executable check passes.

## Frozen upstream field and exact boundary

Cycle463 is frozen at runner SHA-256
`3ae259060c7d7f9e13088197cf022eef845241af20972e5496cede6b4344e9ad`
and note SHA-256
`833faec147b30d6de61de7b3a3b47afc7b7f01d97f18240f0a29e435b0c78e89`.
Its final cold run has `11 PASS / 0 FAIL`.  Cycle464 calls exactly:

```text
item     = domain(radius)
initial  = encode(initial_coarse(item))
physical = physical_forward(initial,item)
values   = history_values(physical,ITERATIONS)
u_x      = Fraction(values[i],DENOMINATOR).
```

Thus the field words come from one reversible 96-layer six-neighbor rule with
a central source bit and blank Dirichlet shell.  Cycle463 verifies an exact
reversible word-block relaxation, not an enumerated Toffoli/CNOT/NN arithmetic
gate trace.  Cycle464 preserves that declared boundary.

The Cycle463 word field is positive but is not a normalized Q1 amplitude
state.  Cycle464 therefore explicitly supplies one global word-to-Q1
normalization and amplitude-preparation compiler.  This is a remaining
reference/preparation import, not an inferred Born rule, mass density, or
energy normalization.

## Locally derived directional lift

The scalar field words do not themselves name a force direction.  Cycle464
does not insert host direction bits.  At every active site `x`, it reads the
same six final neighbor words and computes

```text
d_e(x) = max(u_(x+e)-u_x,0),
q_e(x) = d_e(x)/sum_e d_e(x).
```

At an exact zero-gradient site the fixed fallback is the cubic-invariant
uniform six-direction vector.  Directional Q1 amplitudes are
`sqrt((u_x/sum_y u_y) q_e(x))`.  The neighbor-word positive differences are
derived locally from the Cycle463 output and transform by direction
permutation under all 24 proper-cubic frames.

The comparison/square-root amplitude-preparation circuit is still supplied;
Cycle464 tests the resulting physical Q1 vector, not a bit-level reversible
compiler for that preparation.  The local difference rule and the
word-to-Q1 normalization and amplitude-preparation compiler are therefore
inventoried separately.  Deleting the directional lift while retaining the
same site weights gives a uniform-direction comparator.

## Actual M2/M64 matter and reciprocal update

Each padded cell contains seven field M2 and one six-M2 matter block carrying
the one-particle sector of an actual repeated physical M64.  The joint local
code has `7 x 6=42` states.  The Cycle447 reciprocal field/matter vertex at
the Cycle219 mass coordinate acts identically at every cell and has maximum
support 13 M2.  The physical identity completion is checked for Gram, E/G,
inverse, leakage, and unitarity.

One update is:

1. the same common mass coin at every M64 cell;
2. the same reciprocal 42-state field/matter vertex at every cell; and
3. one nearest-neighbor matter stream, with an onsite direction reflection at
   the supplied finite boundary.

The field is a component of the joint state.  It is not refreshed, decoded,
or converted to a c-number control during the update.  The reciprocal vertex
can change its mode weights and entangle it with matter.  There is no source
refresh, expectation feedback, or host per-step force or control.

No host per-step force or control is used.  The word-to-Q1 normalization and
amplitude-preparation compiler are supplied.  This is not derived gravity.

The train packet starts at `(1,0,0)` and the held packet at `(2,0,0)`, in the
inward `-x` direction.  The start, direction, padding, reflecting boundary,
depths, coordinate centroid, radial second moment, and diagnostic thresholds
are supplied trajectory/readout structure.  They are not derived free-fall
initial data.

## Frozen classifier and resources

Before the final train/held table, Cycle464 freezes:

- passive matter response above `1e-6` in either x-centroid or radial second
  moment for both train and held;
- reciprocal field-weight change above `1e-6`;
- joint-product residual and leading Schmidt tail above `1e-5`;
- norm and one-step inverse residual below `2e-10`;
- post-initial boundary weight below `0.75`;
- zero source refresh, expectation feedback, and host per-step force/control;
- deletion visibility above `1e-6`; and
- a 600-second wall cap and 4 GiB RSS cap, including imported Cycle463 word
  generation and the passive evolution.

The joint-product residual is evidence of interaction/backreaction, not a
failure.  The leading Schmidt tail separately tests non-product structure.
No threshold is changed after the held row.

## Result

The first complete cold science body returned nine passes and one audit
failure because it incorrectly compared two distinct supplied mass fixtures.
The Cycle442 selected common passive-mass coordinate is
`2.51729889353184`; the inherited Cycle435/Cycle219 three-cell rest-mass
fixture is `0.4534056541748851`.  Neither predecessor identifies them.  The
corrected audit preserves and reports both separately rather than changing
the law, response thresholds, geometry, or result rows.

The frozen passive rows are:

| quantity | train R1/padR2/depth4 | held R2/padR3/depth6 |
|---|---:|---:|
| maximum absolute x-centroid response | `0.000575408929097021` | `0.0001822136594233914` |
| maximum absolute radial-second response | `0.001150817858194042` | `0.0007287924752654718` |
| final x-centroid response | `0.00041038755237285396` | `0.00006202855753312253` |
| final radial-second response | `-0.0005469394140553696` | `-0.0007287924752654718` |
| field-weight backreaction | `0.0008919380060133912` | `0.0002419465967721767` |
| joint-product residual | `0.03243339101636976` | `0.020752842992302224` |
| leading Schmidt tail | `0.030883773071145294` | `0.019854481498312065` |
| one-step inverse residual | `5.523909826757273e-16` | `5.222405491652415e-16` |
| maximum norm error | `4.440892098500626e-16` | `1.7763568394002505e-15` |
| maximum post-initial boundary weight | `0.39457334067309013` | `0.3309486767395572` |

The train and held Cycle463 word digests are respectively
`0124251bd62a38d75db81ead948a8b4e638d7561d2343f67b07c68e1a51a8722`
and
`4d6be929da9d122d11f0e74edba43876705cc1360b4104356ce48bfe4acbb459`.
The generated-word residuals are `4.440892098500626e-16` and
`5.5933003103895076e-08`; source-defect residuals are
`8.881784197001252e-16` and `7.45773374718601e-08`.

The local 13-M2 compiler has E/G residual
`5.776915683787074e-17`, inverse `7.764219979630248e-17`, and zero leakage.
Source and reciprocal-coupling deletion collapse the maximum response to
`5.551115123125783e-17` and `8.881784197001252e-16`; their field-weight
changes are `4.440892098500626e-16` and `1.121817653647657e-16`.
Direction-lift, mass-coin, matter-stream, and initial-cell-vertex deletion
trace residuals are respectively `0.002805270758229449`,
`0.00850822458552623`, `0.001888271428439396`, and
`0.0018455575820655456`.

All 24 frame rows have zero profile, direction, and locality residual.  The
corrected immutable rerun returned `10 PASS / 0 FAIL`, exit status 0, and

```text
RESULT PHYSICAL_RELAXED_CUBIC_FIELD_PASSIVE_M64_BACKREACTION_CERTIFIED
```

It completed in `112.33 s` external wall time (`15.400541750015691 s` inside
the Cycle464 body, including Cycle463 word generation).  The 600-second timer
did not fire.  Runner-reported and external maximum resident set size was
`1019314176` bytes and peak memory footprint was `1661667008` bytes.  Maximum
dense joint-state payload was `79093056` bytes,
the held apparatus used 4,459 physical M2, and local vertex support was 13 M2.

## Required deletions and covariance

The runner deletes separately:

- the source/profile by selecting the physical field vacuum;
- the reciprocal field-to-matter vertex;
- the neighbor-derived direction lift, replacing it with equal directions at
  unchanged site weights;
- the common mass coin;
- the matter stream; and
- the local vertex at the initial matter cell.

Source and coupling deletion must collapse both passive response and
field-weight backreaction.  The other deletions must change the trace above
the frozen visibility floor.  These are route-local necessities, not
minimum-content claims.

The generated word field, neighbor-direction vector, padded matter cube,
nearest-neighbor/reflection stream, and identical local vertex are carried
through all 24 proper-cubic frames.  Cycle219 mass and Cycle230 contact are
retained.  Carried-apparatus covariance does not derive cubic isotropy of a
continuum force law.

## Exact three-part weak-field boundary

The repository's weak-field bridge has three separate inputs:

The second input is written literally as `rho_psi=|psi|^2/local mass source`;
Cycle464 does not construct it.

| input | Cycle464 disposition |
|---|---|
| physical `-Delta` response | the finite reversible word-block response/profile-table import closes on the declared domains; a physical `-Delta` law and primitive arithmetic gate trace remain supplied/open |
| `rho_psi=|psi|^2` / local mass source | **open**: the source is a supplied central bit; word-to-Q1 normalization is supplied and no matter-density, energy, or stress map is constructed |
| passive test-matter response | **bounded positive target**: actual repeated M64 matter responds and changes the reciprocal field state under one supplied common local coupling in train and held geometries |

These rows are not interchangeable.  Closing the third finite fixture cannot
supply the absent second bridge or promote the first finite relaxation to a
universal gravitational law.

Cycle442 used a no-refresh dressed Q1 source and L7/L11 physical corridors,
then correctly refused sustained acceleration because its held traces were
transient/oscillatory.  Cycle464 does not repeat that claim or classifier.  It
uses a full cubic locally relaxed field, a padded 3D matter domain, and a
short bounded response/backreaction criterion.  It does not call a short
visible displacement acceleration.

## Supplied, derived, and open inventory

Supplied:

1. Cycle463 central bit, finite cubes/shells, 96-layer word rule, precision,
   and word-block compiler;
2. global word-to-Q1 normalization, square-root amplitude preparation, and
   zero-gradient uniform convention;
3. Cycle219 mass coordinate, common coin, Cycle447 local reciprocal vertex,
   factor order, and identity completions;
4. initial matter cell/direction, padded domains, reflecting boundary,
   depths, centroid/radial/field/Schmidt diagnostics, thresholds, and caps;
5. M2/M64 layouts, frame transport, and source/profile/receiver labels.

Derived here:

1. local six-direction weights from neighbor-word positive differences;
2. normalized physical Q1 state and its all-frame direction covariance;
3. bounded train/held M64 response, reciprocal field-weight change,
   non-product witness, inverse, deletion, and resource results;
4. the exact separation of the three weak-field inputs above.

Open:

1. autonomous Q1 amplitude preparation directly from the Cycle463 words;
2. a local `rho_psi`/mass/energy-stress source law and empirical coupling
   calibration;
3. sustained source recurrence, carried sources, multi-source response, and
   long trajectory/large-volume behavior;
4. a selected universal interaction, metric dynamics, clocks/proper time,
   Records, occurrence/Born law, and realized history.

## Dependency ledger

| wall | Cycle464 effect | residual |
|---|---|---|
| `C_ref` | local word generation and direction rule reduce table imports | Q1 normalization/preparation, mass/coupling, packet, boundary, and readout supplied |
| `C_num` | train/held response/backreaction tested with zero fit | finite sizes/depths only; no scaling/empirical number |
| `C_wrap` | none | phase is not energy; update count is not time |
| `C_int` | identical reciprocal vertex physically executes | law selection and physical calibration open |
| `C_local` | 13-M2 vertex and repeated physical M64/Q1 sectors | bit-level direction-preparation compiler and scalable apparatus generation open |
| `C_source` | central Cycle463 bit drives finite field words | no `rho_psi`, energy/stress normalization, recurrence, or autonomous material source |

## No-Go Discipline Gate

Gate status: **FAIL for any broad passive-gravity, source-law, trajectory,
minimum-content, or framework no-go**.  A failed row would apply only to the
frozen finite source normalization, direction lift, mass, vertex, packet,
boundary, depth, and readouts.  The licensed negative classification is
`partial-attempt-with-named-untested-routes`.  There is no gravity, no-go,
minimum-content, shared-obstruction, or axiom-pressure claim.

### N1 — alternative route enumeration

| route | honesty marker | disposition |
|---|---|---|
| Cycle463 word field + neighbor-derived Q1 directions + reciprocal M64 matter | `ATTEMPTED` | Cycle464 |
| bit-level reversible word-to-amplitude/direction preparation | `UNTESTED` | removes the remaining Q1 preparation import |
| many-Q recurrent relaxed field | `UNTESTED` | can sustain resources and distribute depletion |
| full joined field/matter eigenpacket or scattering preparation | `UNTESTED` | may support a longer stable response window |
| Cycle213 retarded carrier joined to 3D M64 matter | `UNTESTED` | tests causal propagation rather than a prepared field |
| Cycle216 reversible static exchange joined to matter | `UNTESTED` | distinct finite static-response route |
| carried/distributed reciprocal source | `UNTESTED` | tests active source recoil rather than one central bit |
| larger nonreflecting cubes and multiple packet preparations | `UNTESTED` | tests volume/boundary/readout dependence |
| local `rho_psi`/mass source compiler | `UNTESTED` | addresses the independent missing weak-field input |

At least eight distinct constructive routes remain untested.  None is labeled
failed or ruled out by this finite fixture.

### N2 — wall-independence audit

The live conditions are `S`, physical `rho_psi`/mass sourcing; `A`, autonomous
word-to-Q1 amplitude preparation; `I`, selected/calibrated reciprocal
interaction; and `V`, sustained large-volume dynamics.

| pair | closing first closes second? | reverse? | independent? |
|---|---:|---:|---:|
| S,A | no | no | yes |
| S,I | no | no | yes |
| S,V | no | no | yes |
| A,I | no | no | yes |
| A,V | no | no | yes |
| I,V | no | no | yes |

Passive response is the finite target, not an inflated fifth wall.  Metric,
time, and Records are downstream and are not counted in this narrower test.

### N3 — hidden-condition scan

The load-bearing imports are explicit: Cycle463 fixed-point rule/precision,
global Q1 normalization, amplitude preparation, mass coordinate, coupling
scale, local vertex, initial cell/direction, padding, reflection, depths, and
readouts.  The neighbor-difference rule is displayed and tested.  “Physical”
does not hide the uncompiled amplitude-preparation circuit or promote the
compact Cycle463 word block to an enumerated primitive trace.

### N4 — residual matching

| witness | predecessor residual | Cycle464 target | exact match? |
|---|---|---|---:|
| Cycle442 | no-refresh finite source gives transient corridor response | distinct cubic short response/backreaction, no acceleration claim | yes for passive-response opening; no as repeated classifier |
| Cycle447/450 | reciprocal local vertex and actual M64 corridor; boundary/micromotion residuals | reuse identical vertex but move to padded 3D matter and finite response | yes for local interaction; no broad trajectory inference |
| Cycle459 | physical line interval field, no 3D common matter/backreaction | add 3D field plus actual reciprocal M64 matter | yes |
| Cycle461 | supplied cubic profile/table, no matter/backreaction | comparator only after Cycle463 retires its table | yes as prior residual, not update input |
| Cycle463 | locally generated finite 3D word field, no backreaction | direct executable field input | yes |
| weak-field source ledger | `rho_psi`/mass source missing | remains missing | yes; explicitly open |

Only the matching bounded residuals license the Cycle464 disposition.

### N5 — rhetoric audit

“Response” means a finite free-subtracted centroid/radial change.  It is not
called acceleration.  “Backreaction” means reciprocal vertex evolution with
field-weight change and a non-product joint state; it is not an Einstein
equation or stress-energy response.  “Held” means no refit of the shared
coupling/readout when moving from R1 to R2; both finite domains and depths are
declared program inputs.  No continuum, equivalence-principle, or gravity
word is inferred.

### N6 — partial-closure path scan

No axiom edit is needed.  The immediate constructive path is a reversible
local comparison/square-root compiler from Cycle463 words into Q1 amplitudes,
followed by a many-Q recurrent source or a joined scattering/eigenpacket
preparation.  Independently, a physical local matter-density source map can
address the still-open second weak-field input.  Larger nonreflecting cubes
can test boundary and duration scaling with the same vertex.

### N7 — hostile steelman

A hostile reviewer should grant at most that a supplied reciprocal unitary can
entangle a prepared field with matter and shift a short packet trace.  The
global normalization, amplitude preparation, coupling strength, mass mapping,
boundary, and readout are supplied; the field source is a bit, not local
matter density.  They should also note that Cycle442/447/450 already showed
short responses need not become sustained acceleration.  A positive
Cycle464 result therefore strengthens executability but cannot establish
gravity.  A negative result would remain vulnerable to every N1 route.

### N8 — cross-cycle echo

Cycle461's prepared table was replaced by Cycle463's local word rule, directly
showing that an explicit import can be retired constructively.  Cycle447's L9
boundary failure was removed by Cycle450's L17 enlargement while its separate
micromotion residual remained.  These echoes forbid treating a route-specific
miss as a shared obstruction.  Cycle464 can retire a bounded passive-response
join while leaving Q1 preparation, material sourcing, calibration, and scaling
open.  Broad no-go and axiom-pressure gates therefore fail.

## Reproduction

```bash
python3 -m py_compile \
  scripts/physical_relaxed_cubic_field_passive_m64_backreaction_cycle464_2026_07_19.py
python3 \
  scripts/physical_relaxed_cubic_field_passive_m64_backreaction_cycle464_2026_07_19.py
```

The reproduced token is
`PHYSICAL_RELAXED_CUBIC_FIELD_PASSIVE_M64_BACKREACTION_CERTIFIED` with exit
status 0.  No axiom, foundation, Qualification, primitive, registry, policy,
queue, or audit surface is edited.
