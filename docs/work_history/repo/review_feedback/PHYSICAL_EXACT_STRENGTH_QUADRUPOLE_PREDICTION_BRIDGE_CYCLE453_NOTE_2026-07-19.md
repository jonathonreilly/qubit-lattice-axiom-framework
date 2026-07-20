# Physical exact-strength quadrupole prediction bridge — Cycle 453

Date: 2026-07-19

Authority: none

Audit: unset

## Frozen question

Can the existing physical `(+1,-2,+1)` phase quadrupole be normalized by the
exact Cycle-420 far-side source coefficients and propagated into a physical
M64 test-matter packet so that the four named quadrupole-width rows are
reproduced without a host scalar-profile join, expectation feedback, source
refresh, or per-update force?

The answer is tested as a direct compiler bridge.  It does not identify the
source with gravity, an occupation with energy/stress, a phase with energy, an
update step with time, a receiver effect with a Record, or a coherent weight
with a Born frequency.

## Predecessor and far-side reconstruction

Cycle 420 freezes two distinct relevant far-side types.  Its quadrupole-width
surface uses the signed host scalar profile `(+1,-2,+1)`, separations `a=1,2`,
the scalar normalization `SOURCE_STRENGTH=5e-5`, and a host ordered-lattice
packet width.  Its impact-parameter surface instead uses a positive
`strength/r` source at realized `b=(5,6,7,8,10)` and a no-refit log-log fit.
Those source and readout types are not interchangeable.

Cycle 432 compiles two phase-coded source cells, a physical receiver effect,
the full Q1 cubic field, E/G, inverse, mass/contact, and all-frame covariance.
It explicitly leaves both named far-side surfaces false.  Cycle 435 advances
the quadrupole route: it supplies a physical `(+1,-2,+1)/sqrt(6)` phase column,
two disjoint physical three-M64 blocks, a spatial M64 packet, physical centroid
and second-moment effects, and train/held width rows.  Its occupations
`0.15864554811791431` and `0.8` preserve only the route ratio; they are not
derived from the far-side normalization, and the held response does not obey
the named stronger-`a=2` ordering.

The exact far-side quadrupole runner builds its field at `5e-5` and multiplies
that field by `route_strength / 5e-5`.  Cycle 453 therefore freezes the same
dimensionless coefficients as physical Q1 occupations:

```text
p_route = route_strength / 5e-5
p_unit  = 0.015003358529489008
p_two   = 0.07565725585107586
p_two / p_unit = 5.042687988984065
```

The remaining occupation is the invariant Q0 branch.  Within Q1, source
amplitudes are `(+1,-2,+1)/sqrt(6)` and occupations are `(1,4,1)/6`; there is
no negative occupation.  The sign is relative phase carried by the physical
source/field state, not a negative number operator value.

## Frozen train, held, and acceptance contract

The geometry was frozen before any interacting Cycle453 result.  Both rows
use the same L13 cube, receiver cells, source-to-receiver axial displacement,
depth, field update, packet program, and readout.  Only source separation
changes.

| role | source cells | receiver cells | depth |
|---|---|---|---:|
| train L13/a1/depth4 | `(4,6,5),(4,6,6),(4,6,7)` | `(6,6,5),(6,6,6),(6,6,7)` | 4 |
| held L13/a2/depth4 | `(4,6,4),(4,6,6),(4,6,8)` | `(6,6,5),(6,6,6),(6,6,7)` | 4 |

The centered coordinates avoid using the periodic seam as part of the source
layout.  Pure-Q1 probability on any coordinate boundary must remain below the
frozen boundary ceiling `0.10`.  Maximum logical payload is capped at `4 GiB`.

The named prediction criteria are frozen as follows:

1. absolute centroid shifts below `3e-13`;
2. all four width shifts above the resolved-signal floor `5e-10`;
3. coefficient-two width greater than unit width at fixed separation;
4. held `a=2` width greater than train `a=1` at fixed strength;
5. physical response-strength ratio within `1%` of
   `5.042687988984065` at each separation;
6. each exact Cycle-420 numeric row reproduced within the numeric row
   tolerance `5e-10`.

The exact Cycle-420 comparison rows are:

| separation/route | width shift |
|---|---:|
| a1/unit | `6.692829912502418e-7` |
| a1/coefficient two | `3.3757457469363317e-6` |
| a2/unit | `1.3197896109318208e-6` |
| a2/coefficient two | `6.656001151128521e-6` |

The `5e-10` row tolerance is `1000` times Cycle 435's independently reported
`5e-13` numerical/covariance/E-G floor.  It was not fitted to a Cycle453 row.
The named surface is certified only if every criterion and every physical
compiler/control gate passes.

## Fixed physical program and controls

The fixed program is inherited without a runtime host branch:

1. Cycle-219 matter coins on source and receiver M64 blocks;
2. Cycle-425 field coin;
3. three Cycle-426 source recoil vertices and three receiver recoil vertices;
4. two local receiver-packet FSWAP edges;
5. Cycle-425 nearest-neighbor field stream;
6. Cycle-230 contacts.

Each strength state is prepared once as

```text
sqrt(1-p_route)|Q0> + sqrt(p_route)|Q1,quadrupole>.
```

No later gate queries `p_route`, an occupation, an expectation, a measured
width, or a branch.  The receiver consumes the common field amplitudes.  No
host scalar-profile join occurs, no expectation feedback occurs, there is no
source refresh, and there is no per-update force.

The runner requires train and held E/G, Gram, inverse, code-space leakage,
norm, bounded support, and locally inherited Cycle-269/319 check/Wilson
constraints.  It reruns the physical position/second-moment dilation and all
24 proper-cubic frames.  It preserves the Cycle-219 one-particle mass and
Cycle-230 contact fixtures.  Source, receiver, field-stream, packet-stream,
coherence, sign, and contact deletions are separate; contact must remain
visible on the full declared code even if inactive on this prediction sector.

## Result

Cycle 453 is a `partial-attempt-with-named-untested-routes`.  The direct bridge
constructs an exact-normalized positive-occupation phase source and obtains
centered, resolved physical packet-width responses, but it does not reproduce
the named far-side rows or stronger-`a=2` order.

| row | physical width shift | Cycle420 width shift | physical minus Cycle420 | physical/Cycle420 |
|---|---:|---:|---:|---:|
| a1/unit | `4.846405339820059e-7` | `6.692829912502418e-7` | `-1.8464245726823592e-7` | `0.724119005439959` |
| a1/coefficient two | `2.4438685030658824e-6` | `3.3757457469363317e-6` | `-9.318772438704492e-7` | `0.7239492207859027` |
| a2/unit | `4.3751148665061024e-7` | `1.3197896109318208e-6` | `-8.822781242812106e-7` | `0.3315009324415812` |
| a2/coefficient two | `2.20621558276457e-6` | `6.656001151128521e-6` | `-4.449785568363951e-6` | `0.3314626203738723` |

The physical coefficient-two/unit response ratios are
`5.042641569796182` at `a=1` and `5.042646079202074` at `a=2`, within the
frozen `1%` tolerance of the supplied source ratio `5.042687988984065`.
Thus strength linearity survives.  The held/train ratios are instead
`0.9027546314705375` and `0.9027554387631037`: the held response is about
`9.7%` smaller, whereas the named far-side response is stronger at `a=2`.

All centroid shifts are below `3.7e-33`.  Pure-Q1 maximum boundary
probability is `3.8378057042741635e-5`, far below `0.10`; the maximum executed
strength-row boundary probability is `2.9035784807499303e-6`.  Maximum norm
error is `1.9984014443252818e-14`.  Therefore the numerical mismatch is not
attributed to centering, boundary leakage, norm loss, host feedback, or source
refresh.

The first physical-shell sweep exposed a separate contract defect: the runner
had frozen a `4 GiB` memory cap but no wall-time cap.  It was terminated during
the first L13 source-block multi-order encoding after `862.84` seconds, with
maximum RSS `1504165888` bytes and peak footprint `3892677920` bytes.  Its
disposition is `L13-PHYSICAL-SHELL-RESOURCE-REFUSED`, not an E/G failure.  The
finite packaged runner reruns Cycle435's L7/L9 local E/G, inverse, Gram, and
leakage bounds only as inherited evidence, checks the complete L13 logical
inverse directly, and leaves L13 physical-shell E/G and the L13 pointer shell
open.  L7/L9 is never counted as an L13 substitute.

The inherited local compiler rerun has maximum E/G/leakage upper bound
`1.0447478123408826e-14`, maximum physical inverse residual
`3.734602017277068e-15`, maximum Gram residual
`7.771561172376096e-16`, and maximum matter support `132 M2` per block.  The
complete L13 train and held logical updates each have inverse residual
`3.939469297057449e-15` and output-norm error
`2.220446049250313e-16`.  These values establish a sound local predecessor
and sound L13 logical evolution; they do not fill the absent L13 physical
intertwiner.

At coefficient-two strength, source, receiver, and field-stream deletions
return the free width `0.10641106458149928` within `4.5e-16`; deleting packet
stream gives width zero.  Erasing source coherence gives
`0.10641350830311519`, while changing the phase column to `(+1,+2,+1)` gives
`0.10641350815622846`, both visibly distinct from the signed intact width
`0.10641350845000234` above the `5e-12` deletion floor.  Contact deletion is
inactive on this prediction sector but changes a declared two-particle code
state by `0.36789306705608243`; the full code retains 645 nontrivial contact
columns.  The Cycle-219 mass remains `0.4534056541748851` with eigen residual
`3.534751832054436e-16`.

There is no gravity, no-go, minimum-content, shared-obstruction, or
axiom-pressure claim.  The three negative coordinates are strictly scoped:
the frozen Q1-occupation normalization misses the four numbers, its fixed
geometry misses held ordering, and the L13 shell compilation is unfinished.

## Dependency ledger

| coordinate | supplied | derived by this attempt | remains open unless all gates pass |
|---|---|---|---|
| physical source | phase-column isometry, Q0/Q1 preparation, Cycle420 strengths and `5e-5` normalization | exact-normalized positive-occupation quadrupole state | autonomous preparation, source recurrence, energy/stress calibration |
| field/update | Cycle425 coin/stream and Cycle426 vertices | no-refresh amplitude propagation | many-Q/large-volume recurrence and empirical law selection |
| matter/readout | physical M64 packet, FSWAPs, centroid/second effects | L13 logical train/held width rows | L13 physical shell, local pointer coupling/inverse, and operational detector calibration |
| named prediction | Cycle420 four numeric rows and thresholds above | direct residual for every row | exact reproduction if any residual exceeds `5e-10` |
| impact parameter | exact positive-source `b=(5,6,7,8,10)` contract | reconnaissance only | physical source family, detector centroid, and no-refit exponent |
| TOE semantics | none | none | gravity/source identification, physical time, Records, Born/occurrence, realized history |

The six-wall ledger changes narrowly.  `C_local` advances at the logical
source-to-packet seam but does not close because L13 physical-shell E/G is
resource-refused.  `C_num` remains open: all four exact rows and the held order
fail.  `C_ref` remains open because preparation and effect functionality are
supplied.  `C_wrap` remains open because phase is not energy/time.  `C_int`
remains open without a calibrated interaction/source identification.
`C_source` remains open without energy/stress normalization and recurrence.

## No-Go Discipline Gate

Gate status: **FAIL for any broad gravity, quadrupole, compiler, or source
no-go**.  If the direct bridge misses a named row, only that frozen
normalization/program is disposed.  The cycle remains a
`partial-attempt-with-named-untested-routes`.

### N1 — alternative route enumeration

| route | truth marker before result | disposition boundary |
|---|---|---|
| exact far-side-normalized Q0/Q1 physical quadrupole, fixed-depth centered geometry | `ATTEMPTED` | this runner reports its four rows |
| direct L13 physical-shell multi-order compiler | `RESOURCE-REFUSED` | missing initial wall cap was exposed; first encoding terminated at `862.84 s` |
| cached/localized or precomputed L13 physical shell | `UNTESTED` | may close E/G without rebuilding the full reducer during every run |
| source-vertex angle encoding of strength rather than Q1 occupation | `UNTESTED` | distinct physical normalization map |
| many-Q coherent source whose mean occupation carries the coefficient | `UNTESTED` | can change response scale and recurrence |
| physical Cycle-213 retarded scalar field joined to M64 packet | `UNTESTED` | targets the legacy propagation law directly |
| reversible Cycle-216 static field approximation joined to M64 packet | `UNTESTED` | separate static-response construction |
| variationally calibrated but held-out physical coupling map | `UNTESTED` | could train on a1/unit and predict the other three rows |
| physical impact-parameter source/detector family | `UNTESTED` | different positive-source named surface |
| larger packet, depth, and nonperiodic held family | `UNTESTED` | tests finite-volume/readout dependence |

N1 fails any broad negative because multiple routes remain untested.  They are
not relabeled `ATTEMPTED` or `RULED OUT BY PRIOR`.

### N2 — wall-independence audit

The collapsed route conditions are `N`, physical normalization/calibration;
`D`, propagation/geometry; `C`, scalable L13 physical-shell compilation; and
`R`, physical effect/readout realization.

| pair | closing first closes second? | reverse? | independent? |
|---|---:|---:|---:|
| N,D | no | no | yes |
| N,C | no | no | yes |
| N,R | no | no | yes |
| D,C | no | no | yes |
| D,R | no | no | yes |
| C,R | no | no | yes |

Exact numeric prediction is the target conditional on these conditions, not a
fourth wall.  Preparation autonomy and gravity semantics are downstream and
are not inflated into this narrower numeric attempt.

### N3 — hidden-condition scan

The note and runner are scanned for “we assume,” “by construction,” “as is
standard,” “framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  No hit supplies a
load-bearing premise.  Geometry, normalization, factor order, thresholds,
preparation, identity completion, and effects are explicit supplied inputs.
The omitted first-run wall-time cap was a genuine hidden resource condition;
it is promoted to `C`, the wall count above is revised, and the L13 compiler
claim is withdrawn rather than repaired by an after-the-fact threshold.

### N4 — residual matching

| witness | predecessor residual | residual tested here | exact match? |
|---|---|---|---:|
| Cycle 420 quadrupole width | no physical source E/G or physical packet readout for four signed-profile rows | physical exact-normalized source and packet plus four numeric residuals | yes |
| Cycle 435 quadrupole bridge | arbitrary occupation ceiling; exact strengths/numeric rows and a2 order open | replaces ceiling with far-side normalization and isolates a2 at fixed L/depth | yes |
| Cycle 432 transverse dipole | two sources, no three-source quadrupole or width | three-source quadrupole packet | no; substrate predecessor only |
| Cycle 420 impact parameter | positive strength/r b-family and log fit | no b-family in this runner | no; retained only as an untested alternative |
| Cycle 435 physical compiler | L7/L9 local block E/G and inverse | L13 physical shell | no; predecessor evidence only, never a held-size substitute |

Only exact residual matches may support the narrow route disposition.

### N5 — rhetoric audit

Any “not reproduced” statement applies only to the four frozen finite L13,
depth4, Q0/Q1-normalized rows.  Per-source sign encoding, L13 logical finite
propagation, and the four scalar readouts are tested.  L13 physical-shell E/G
is not tested to completion.  Other strength encodings, larger-Q states, other geometries,
continuum limits, impact-parameter surfaces, and gravity interpretation are
not tested.  No broader negative phrase is licensed.

### N6 — partial-closure path scan

No axiom edit is needed for the live routes.  A cached/localized L13 encoder,
a source-angle normalization, a many-Q preparation, a physical Cycle-213/216
compiler, or a train-one/holdout-three coupling calibration can be attempted with existing local primitives.
Cycle 435 already supplies the phase quadrupole, packet, effects, and physical
compiler; Cycle 420 supplies the exact far-side rows.  Their executable join
is an implementation/calibration problem, not axiom evidence.

### N7 — hostile steelman

A hostile reviewer should reject any broad negative from a mismatch.  Mapping
the scalar coefficient to Q1 occupation is only one supplied normalization;
the legacy far-side field is linear in signed source amplitude, whereas this
packet response can depend differently on occupation and local recoil angle.
A source-angle map, a coherent many-Q state, or a physical realization of the
Cycle-213/216 field could recover both absolute scale and held separation
ordering.  Fixing depth removes one Cycle435 confound but does not prove the
remaining finite packet matches the legacy detector.  This steelman is strong
and undefeated.

### N8 — cross-cycle echo

Cycle 432's two-source phase seam became Cycle 435's three-source physical
quadrupole and packet.  Cycle 447's apparent L9 boundary failure became an L17
boundary pass in Cycle 450 without changing the local law.  These are direct
examples of a residual being retired by enlarging or isolating the lawful
construction.  The same mechanism may retire a Cycle453 scale or numeric-row
residual, so no shared obstruction or axiom pressure is licensed.

## Reproduction

```bash
python3 -m py_compile \
  scripts/physical_exact_strength_quadrupole_prediction_bridge_cycle453_2026_07_19.py
python3 \
  scripts/physical_exact_strength_quadrupole_prediction_bridge_cycle453_2026_07_19.py
```

The expected result is
`PHYSICAL_EXACT_STRENGTH_QUADRUPOLE_PREDICTION_BRIDGE_NOT_CERTIFIED`.
The finite packaged cold run reports `13` passes and `3` intentional failures
in `569.23` seconds.  Its maximum RSS is `2029977600` bytes and peak memory
footprint is `4210380232` bytes.  The three failures are exactly the held
ordering, four-row numeric reproduction, and L13 physical-shell completion
gates.
No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit surface is edited by this cycle.
