# Physical quadrupole transfer factor and matched receiver — Cycle 458

Date: 2026-07-19

Authority: none

Audit: unset

## Frozen question and decomposition

Cycle 458 diagnoses Cycle 453's four-row quadrupole mismatch before attempting
one bounded repair.  The declared decomposition is frozen before fitting:

```text
named width response
  = source normalization
  x finite physical propagation kernel
  x receiver functional
  compared with legacy host Green/width normalization.
```

The source normalization remains the exact Cycle420 coordinate
`p_route = route_strength / 5e-5`.  The finite physical propagation kernel is
the derivative at `p=0` computed from the fully evolved physical Q0 and Q1
endpoint operator moments.  The receiver functional is the physical packet's
position and second-moment effect.  The legacy host Green/width normalization
is computed independently as the analytic tangent of the exact
`multipole_tidal_response_probe.py` propagation and detector functional.

Only one train-derived receiver scale is allowed:

```text
lambda_R = K_legacy(a=1) / K_physical(a=1).
```

It rescales the physical pointer coordinates `Z -> lambda_R Z` and
`Z2 -> lambda_R^2 Z2`.  It is then frozen for the train coefficient-two row
and both held `a=2` rows.  There are no per-row scale factors, no held refit,
and no geometry-dependent correction.

## Frozen geometry, thresholds, and resources

Cycle 458 preserves Cycle 453's train L13/a1/depth4 and held L13/a2/depth4
geometries exactly.  Both use the same receiver cells and depth; only source
separation changes.  The exact Cycle420 comparison rows and numeric tolerance
`5e-10` are unchanged.

The analytic legacy tangent is checked against a symmetric finite difference
with step `1e-4`.  Physical finite-row departures from the endpoint tangent
must remain below `2e-9`.  Pure-Q1 boundary probability remains below `0.10`.

The entire executable has a predeclared 600-second wall cap enforced with a
process timer and a 4 GiB RSS cap.  It does not retry the Cycle453 L13 physical
shell.  The new two-M2 matched receiver is a bounded local pointer compiler;
the inherited source/matter/field factors are checked through their logical
inverse, mass/contact, and all 24 proper-cubic frames.  The L13 physical M64
shell remains open and is not silently replaced by an L7/L9 result.

## Analytic transfer construction

For the physical endpoint packet, let `w0`, `c0`, and `s0` be the Q0 width,
centroid, and second moment, and let `c1,s1` be the corresponding pure-Q1
values.  Orthogonality of Q0 and Q1 makes the finite effect weights affine in
`p`.  The operator tangent is

```text
d variance / dp = (s1-s0) - 2 c0 (c1-c0)
K_physical      = (d variance / dp) / (2 w0).
```

No route strength or legacy target enters this derivative.

For the legacy ordered-lattice propagator, the exact edge factor at source
coefficient `p` is `exp(i K L (1+p f_edge))`.  At `p=0`, the tangent propagates
by the product rule:

```text
d(A exp(i K L p f))/dp at p=0
  = (dA/dp + i K L f A) exp(i K L).
```

The detector probability, normalized centroid, second moment, and width are
then differentiated explicitly.  This supplies `K_legacy(a)` from operator
data rather than by fitting the four published rows.

## Matched receiver compiler

Three packet-position labels `(-,0,+)` embed isometrically into the first
three computational labels of two pointer M2; `|11>` is unused.  Reflection
swaps `-` and `+` and fixes the other two labels.  The runner tests Gram, E/G,
inverse, and leakage for that physical reflection.  It also checks

```text
E^dagger Z_physical(lambda_R) E  = lambda_R Z_logical,
E^dagger Z2_physical(lambda_R) E = lambda_R^2 Z2_logical.
```

The unused label receives identity completion.  The scale changes only the
fixed receiver coordinate assignment.  It never queries the runtime state,
an expectation, a width, or a branch.  There is no host scalar-profile join,
no expectation feedback, no source refresh, and no per-update force.

## Result

The first immutable cold run returned `11 PASS / 2 FAIL`, exit status 1, and

```text
RESULT PHYSICAL_QUADRUPOLE_TRANSFER_FACTOR_MATCHED_RECEIVER_NOT_CERTIFIED
```

The independently differentiated legacy width tangents agree with symmetric
finite differences:

| separation | analytic `K_legacy` | finite difference | residual | source-profile norm |
|---:|---:|---:|---:|---:|
| a=1 | `4.460639183320581e-05` | `4.460638969305819e-05` | `-2.1401476172299393e-12` | `0.0011371555555553553` |
| a=2 | `8.796394412317128e-05` | `8.796393835552863e-05` | `-5.767642656875904e-12` | `0.0013189922060456015` |

The physical endpoint construction gives
`K_physical(a=1)=3.230220999270172e-05` and
`K_physical(a=2)=2.9160963194979544e-05`.  Thus the sole train-derived
receiver scale is

```text
lambda_R = 1.3809083602417316.
```

The exact no-refit named-row predictions are:

| row | raw physical shift | matched shift | legacy target | named residual | disposition |
|---|---:|---:|---:|---:|---|
| a1/unit | `4.846405341762949e-07` | `6.692441653560643e-07` | `6.692829912502418e-07` | `-3.8825894177548765e-11` | PASS |
| a1/coefficient-two | `2.443868502649549e-06` | `3.374758446640204e-06` | `3.3757457469363317e-06` | `-9.873002961275463e-10` | FAIL |
| a2/unit | `4.375114864563212e-07` | `6.041632693493211e-07` | `1.3197896109318208e-06` | `-7.156263415824997e-07` | FAIL |
| a2/coefficient-two | `2.2062155826257923e-06` | `3.0465815425435393e-06` | `6.656001151128521e-06` | `-3.609419608584982e-06` | FAIL |

The table contains three failed named rows but only two failed aggregate
controls: the three-row no-refit prediction control and the held-ordering
control.  No held row passes.  The scalar receiver preserves the physical
source-strength ratios (`5.042641566915566` at a1 and
`5.042646081124201` at a2, versus supplied source ratio
`5.042687988984066`).  The finite endpoint nonlinear residual is at most
`2.8063323464355146e-11`, so finite-strength curvature cannot account for the
held discrepancy.

The decisive decomposition is instead the separation dependence:

```text
K_physical(a=2) / K_physical(a=1) = 0.9027544307825409
K_legacy(a=2)   / K_legacy(a=1)   = 1.9720031257423813.
```

An overall receiver coordinate scale cannot reverse that ordering.  Cycle458
is therefore `partial-attempt-with-named-untested-routes`: it constructively
repairs the a1/unit normalization and isolates a propagation-kernel/packet
matching target, but it does not certify the four-row bridge.  This is not a
propagation, source, gravity, or compiler no-go.

## Required controls and semantics

The runner reports source, receiver, field-stream, packet-stream,
receiver-normalization, and contact deletions.  It retains the Cycle-219 mass
fixture and Cycle-230 contact, and reruns the local factor covariance in all
24 proper-cubic frames.  It reports boundary, logical payload, process RSS,
wall time, lawful-domain rejection, and exact named-row residuals.

The pointer coordinate is not a Record.  Phase is not physical energy.  A
generator element is not a rate, update count is not time, the receiver is not
an occurrence, coherent weight is not a Born frequency, and the source is not
gravity or calibrated stress-energy.

## Dependency ledger

| factor | supplied | derived here | open |
|---|---|---|---|
| source normalization | Cycle420 route strengths and `5e-5` host normalization | exact Q1 coefficients retained from Cycle453 | autonomous preparation and physical source calibration |
| physical kernel | Cycle435 local update and Cycle453 L13 geometries | Q0/Q1 endpoint tangent and finite nonlinear residual | alternate packet/depth and a matched legacy-like carrier |
| receiver | three packet effects and one train calibration | two-M2 scaled effect compression, E/G, inverse, leakage | physical pointer coupling/inverse and operational detector units |
| legacy kernel | exact host Green/profile/packet program | analytic width tangent at `a=1,2` | physical compiler of that carrier |
| named prediction | four Cycle420 rows | no-refit residuals after one scale | closure unless all predicted rows pass |
| TOE semantics | none | none | energy/stress source, metric, time, Records, Born/occurrence, realized history |

`C_local` can advance through the two-M2 receiver normalization but remains
open at the L13 M64 shell and pointer coupling.  `C_num` advances if the train
normalization predicts held rows; otherwise its exact kernel residual remains.
`C_ref` stays open because calibration and preparation are supplied.  `C_wrap`
stays open because phase is not time/energy.  `C_int` stays open without a
selected physical coupling/source law.  `C_source` stays open without
energy/stress normalization and recurrence.

## No-Go Discipline Gate

Gate status: **FAIL for any broad quadrupole, gravity, receiver, or source
no-go**.  Any failed row is restricted to one train-normalized scalar receiver
on the frozen finite program.  The licensed classification is
`partial-attempt-with-named-untested-routes`.

### N1 — alternative route enumeration

| route | honesty marker | disposition |
|---|---|---|
| one train-tangent scalar receiver normalization | `ATTEMPTED` | this runner predicts three no-refit rows |
| separation-dependent matched propagation kernel derived as a local law | `UNTESTED` | may reproduce the legacy `a` dependence without per-row fitting |
| source-vertex angle normalization | `UNTESTED` | strength enters a gate angle rather than Q1 occupation |
| coherent many-Q source normalization and recurrence | `UNTESTED` | can change finite response scale and separation dependence |
| physical Cycle-213 retarded carrier joined to the M64 packet | `UNTESTED` | targets the legacy dynamic kernel directly |
| reversible Cycle-216 static approximation | `UNTESTED` | targets the static Green kernel by a different local program |
| alternative physical packet/receiver functional | `UNTESTED` | can change the kernel without changing source encoding |
| train-one/holdout-three coupling calibration | `UNTESTED` | tests a single physical interaction coefficient rather than receiver units |
| physical impact-parameter route | `UNTESTED` | independent named positive-source surface |

N1 fails a broad negative because eight constructive routes remain untested.
They are not relabeled attempted or ruled out.

### N2 — wall-independence audit

The collapsed conditions are `S`, physical source normalization; `K`, matched
propagation kernel; `R`, receiver calibration/coupling; and `C`, scalable L13
physical-shell compilation.

| pair | closing first closes second? | reverse? | independent? |
|---|---:|---:|---:|
| S,K | no | no | yes |
| S,R | no | no | yes |
| S,C | no | no | yes |
| K,R | no | no | yes |
| K,C | no | no | yes |
| R,C | no | no | yes |

The four numeric rows are the target, not additional walls.  Gravity, clocks,
Records, and Born semantics are downstream and not counted in this narrower
attempt.

### N3 — hidden-condition scan

The note and runner are scanned for “we assume,” “by construction,” “as is
standard,” “framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  No phrase supplies
a load-bearing premise.  The one fit row, tangent formula, finite-difference
step, geometry, thresholds, effect labels, identity completion, and resource
caps are explicit.  Cycle453's omitted wall cap is not repeated.

### N4 — residual matching

| witness | predecessor residual | Cycle458 residual | exact match? |
|---|---|---|---:|
| Cycle453 | direct physical rows are about `0.724` of legacy at a1 and `0.331` at a2 | a1/unit residual is `-3.8825894177548765e-11`, while held a2 residuals remain `-7.156263415824997e-07` and `-3.609419608584982e-06` | yes |
| Cycle435 | arbitrary strength ceiling and weaker a2 response | physical kernel ratio is `0.9027544307825409`, versus legacy `1.9720031257423813` | yes for a2 ordering and normalization; not an L13 shell witness |
| Cycle420 | exact signed-profile widths at two strengths/separations | same four rows and unchanged tolerance | yes |
| Cycle432 | two-source signed contrast, no width surface | three-source width normalization | no; substrate predecessor only |
| Cycle420 impact parameter | positive source and log-fit residual | not attempted | no; live alternative only |

Only the first three exact matches may support the narrow route disposition.

### N5 — rhetoric audit

“Scalar receiver normalization does not predict the held rows” means only the
two finite L13 geometries, two source strengths, one packet, one depth, and one
train-derived scale tested here.  The per-label receiver compiler and finite
logical lattice are tested; different local propagation kernels,
source-angle/many-Q encodings, packets, larger lattices, and continuum
behavior are not.  No untested resolution is absorbed into the negative.

### N6 — partial-closure path scan

No axiom edit is needed.  The operator decomposition itself gives the next
constructive target: compile the ratio between the legacy and physical
separation kernels as one local propagation law, then train once and hold out
the remaining rows.  Source-angle, many-Q, Cycle213/216, and alternate packet
routes use existing candidate primitives.  L13 shell caching/localization is
an implementation route, not a new axiom.

### N7 — hostile steelman

A hostile reviewer should reject any broad negative because a scalar pointer
unit can only correct an overall normalization.  Cycle453 already shows that
the source-strength ratio is right while the `a=2/a=1` kernel ratio is wrong;
therefore the strongest repair should alter the physical propagation kernel
or receiver packet, not rescale every pointer coordinate.  The exact legacy
tangent ratio `1.9720031257423813` derived here, against the physical ratio
`0.9027544307825409`, supplies a concrete matching target for a local
Cycle213/216-like carrier.  That route is live and could recover the held
ordering without any per-row scale.

### N8 — cross-cycle echo

Cycle432's phase dipole became Cycle435's physical quadrupole/packet, and
Cycle447's boundary failure became Cycle450's boundary pass after isolating
finite volume.  Cycle453 then preserved strength scaling while exposing a
separation-kernel mismatch.  Each step retired part of a wall by decomposing
the program more finely.  The same method can replace the scalar Cycle458
normalization with a matched local kernel; no shared obstruction or axiom
pressure follows.

## Reproduction

```bash
python3 -m py_compile \
  scripts/physical_quadrupole_transfer_factor_matched_receiver_cycle458_2026_07_19.py
python3 \
  scripts/physical_quadrupole_transfer_factor_matched_receiver_cycle458_2026_07_19.py
```

The expected token is
`PHYSICAL_QUADRUPOLE_TRANSFER_FACTOR_MATCHED_RECEIVER_NOT_CERTIFIED` with exit
status 1.  The run completed normally in `86.17 s` external wall time
(`5.1297942500095814 s` inside the Cycle458 body after inherited imports).
The 600-second timer did not fire.  The runner-reported RSS was
`970539008` bytes; `/usr/bin/time` reported maximum resident storage
`976470016` bytes and peak memory footprint `1001080032` bytes, all below the
4 GiB cap.  Maximum logical payload was `52254720` bytes.  No axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit
surface is edited.

There is no gravity, no-go, minimum-content, shared-obstruction, or
axiom-pressure claim.
