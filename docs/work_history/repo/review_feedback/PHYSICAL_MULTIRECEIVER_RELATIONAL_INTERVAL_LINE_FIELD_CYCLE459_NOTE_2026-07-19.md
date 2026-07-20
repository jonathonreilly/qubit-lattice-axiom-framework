# Physical multi-receiver relational-interval line field — Cycle 459

Date: 2026-07-19

Authority: none

Audit: unset

Admission target: none

## Result

Cycle 459 constructs a bounded **physical multi-receiver relational-interval
line field**.  One central Q1 source preparation is spread coherently along a
finite nearest-neighbour line embedded in the framework's physical
three-dimensional cubic lattice.  Every noncentral field M2 controls one
complete local dual-clock comparator through **one identical local delay
circuit**.  One fixed size-indexed schedule contains all propagation, clock,
and response gates; there is no host Poisson solve, expectation feedback, or
per-receiver law selection.

Train radius is 3 and held radius is 5.  The physical source circuit prepares
the closed-form Q1 site-norm profile

```text
A_R = 1/(R+1)^2,
u_0 = A_R (R+1),
u_{+/-r} = A_R (R+1-r),  r=1,...,R.
```

Every reference clock advances four complete word cells.  On each coherent
basis branch, only the comparator at the occupied field site applies one
inverse sweep to its probe clock.  Thus that comparator has candidate interval
`3:4`; every other comparator has `4:4`.

The optional numerical readout

```text
F_x = 4 ||(1 - R_x) psi||^2
```

uses the local complete-word ratio operator `R_x`.  It gives `F_x=u_x` at all
receivers.  With the supplied zero boundary `F_{+/-(R+1)}=0`, it satisfies the
one-dimensional Dirichlet Green/Poisson-style recurrence

```text
F_{s(r-1)} - 2 F_{sr} + F_{s(r+1)} = 0,
s in {-1,+1}, r=2,...,R,

2 u_0 - F_-1 - F_+1 = 2 A_R.
```

The held per-ray prediction is exactly

```text
(F_1,F_2,F_3,F_4,F_5) = (5,4,3,2,1)/36,
u_0 = 6/36.
```

This is a one-dimensional Dirichlet Green/Poisson-style recurrence on one
supplied line.  It is not a three-dimensional Poisson law on the framework's
full spatial substrate.  It is not a physical lapse, metric, proper time,
energy/stress source, or gravity.  The update count is not time.  Authority
remains none, audit remains unset, and there is no axiom pressure.

Runner:

`scripts/physical_multireceiver_relational_interval_line_field_cycle459_2026_07_19.py`

## Reconnaissance and repaired boundaries

Cycle 204 gives a sharp conditional triangle: if an operational rest
coordinate equals inertia, if that coordinate generates an active source, and
if one common field/lapse couples to matter, then a passive acceleration ratio
can follow.  Its external gradient, active source map, and common lapse remain
supplied.  Cycle 459 constructs none of those identifications.

Cycle 243 separates compiler order, causal event order, Record formation,
named commit counts, calibrated relative clocks, lapse response, and rates.
It explicitly refuses to call gate layers, recurrence indices, or phases
time.  Cycle 459 consumes complete clock words and matched finite sidecars; it
does not use circuit depth as an interval.

Cycle 420 gives an exact seven-M2 source lift but its Cycle-213/216 dynamic and
static Poisson receivers remain host arrays/host solvers.  Cycle 459 does not
call those surfaces physical precedent.  Its field circuit is a new finite Q1
line preparation with an analytic profile and no matrix inversion at runtime.
The result is only the declared line recurrence, not physicalization of the
older 3D static solve.

Cycle 431 supplies the exact occupation-controlled fan/Fredkin/unfan clock
response used here.  Cycle 451 supplies the complete dual-clock relational
boundary: `4:4` control and `3:4` delay on common candidate event words.
Cycle 456 makes those complete signatures locally discriminable and keeps
norm readout, occurrence, Records, lapse, and proper time separate.  Cycle 459
uses the same complete-word semantics at several sites without importing law
selection or actualization.

The repaired emergent-metric note withdraws two earlier positive uses: a
Record-history time/rate no-go cannot supply an event order, and a sampled
one-particle group speed plus exponential tail cannot supply the exact causal
relation required for Lorentzian conformal rigidity.  Cycle 459 uses neither.
It supplies no common exact causal event set, Lorentzian manifold interface,
distinguishing/time-orientation hypothesis, volume-faithful Record density,
or conformal/scale theorem.

Givens rotations, finite-difference Green functions, controlled clock
permutations, and norm diagnostics are standard tools.  The repository-local
result is their dependency-tracked physical composition with complete
multi-receiver Cycle-451-style interval words and explicit source/profile
sidecars.  No global novelty is asserted.  No Thirring engine is used or
compared.

## Geometry and physical code

The framework supplies `Z^3`; Cycle 459 additionally supplies one finite
oriented line within it.  For radius `R`, field M2 occupy

```text
(-R,0,0),...,(-1,0,0),(0,0,0),(1,0,0),...,(R,0,0).
```

The central M2 is the initial source.  Every noncentral field site has a local
comparator column.  The live reference and probe clocks are complete
sixteen-M2 one-hot words.  A fifteen-M2 response rail implements the exact
Cycle-431 fan/Fredkin/unfan delay circuit.  Parallel local coordinate strips
hold complete start clocks and provenance sidecars.

Each receiver contains 112 M2:

| per receiver | M2 |
|---|---:|
| live reference/probe clocks | 32 |
| response rail | 15 |
| complete start reference/probe clocks | 32 |
| start/end event identities | 8 |
| epoch/profile | 6 |
| reference/probe device identities | 10 |
| source identity/calibration | 7 |
| event-ready/predecessor | 2 |
| **total** | **112** |

Train has seven field M2 plus six comparators, totaling 679 M2.  Held has
eleven field M2 plus ten comparators, totaling 1,131 M2.  The source identity
and calibration occur in every complete comparator sidecar and must match.
They are not inferred from a norm or radial coordinate.

The chosen line is not the whole spatial lattice and its reflection symmetry
is not 3D spherical symmetry.  Proper-cubic covariance means the complete
line/column apparatus is carried into each of 24 orientations; it does not
promote the line equation to an isotropic 3D field equation.

## Fixed source propagation

The source begins as one excitation at `x=0`.  Let

```text
W_ray = sum_{r=1}^R u_r.
```

Two source-neighbour Givens rotations first allocate `W_ray` to each ray while
leaving `u_0` at the source.  On each ray, successive adjacent Givens rotations
leave `u_r` at radius `r` and pass the remaining ray norm outward.  The angles
are closed-form square-root ratios of the declared `u_r`; no linear solver,
Poisson inversion, field expectation, detector result, or host branch enters a
gate.

The train and held circuits are generated from the same radius-indexed closed
formula.  Held coefficients are frozen before execution and are not fitted to
train or to the harmonic residual.  Changing the radius changes finite
capacity and the supplied zero boundary, so the normalized Green profile
changes exactly as the formula declares.

This preparation is a candidate source/propagation law.  The choice of the
linear Dirichlet profile and its Givens angles remains supplied.  Constructing
the circuit does not derive a mass-to-source map, energy density, stress, or
gravity coupling.

## Identical local dual-clock response

After propagation, every comparator executes exactly the same fixed schedule:

1. four complete forward sweeps of its reference clock;
2. four complete forward sweeps of its probe clock; and
3. one field-M2-controlled delay response using fifteen CNOT fan gates,
   fifteen connected Fredkin clock swaps, and fifteen inverse fan gates.

There is no receiver-specific response program, angle, strength, expectation,
or decoded-distance input.  Distance dependence enters only through the
coherent field norm generated by the common propagation circuit.  Every rail
returns exactly blank.

The four baseline sweeps are a supplied echo calibration inherited at the
word level.  Four gates, four sweeps, or any schedule depth are not four units
of time.  Only the complete start/end word comparison yields the dimensionless
candidate `4:4` or `3:4`.

## Exact bridge square and inverse

For radius `R`, `E_459` encodes the central Q1 source, blank rails, complete
start/live clock words, and all finite sidecars.  `G_coarse,459` directly forms
the analytic coherent Q1 profile, advances every reference/probe word four
cells, and delays only the occupied receiver's probe word.  The physical map
executes the adjacent Givens, clock-SWAP, and local response schedules.

The runner checks

```text
E_459 G_coarse,459 = G_physical,459 E_459
```

on train radius 3 and held radius 5.  Reversing every local response gate,
clock SWAP, and Givens rotation returns the central source and every clock,
rail, identity, epoch, profile, device, source, calibration, event, and
predecessor bit.  Q1 number, norm, clock one-hot code, sidecars, and blank
rails are checked.

No open-system erasure, measurement, expectation feedback, or host state
query appears in the map.  The source remains one branch of the exact global
coherent state; no receiver occurrence is selected.

## Interval-contrast field and discrete relation

For a local complete-word ratio `R_x`, the optional numerical diagnostic is

```text
F_x = 4 ||(1-R_x) psi||^2.
```

`R_x=1` on `4:4` branches and `R_x=3/4` on the one branch where the local
field M2 is occupied.  Therefore `F_x` equals the coherent field-sector norm
`u_x`.  The circuit does not calculate `F_x`, feed it back, or use it to
choose a response.  The norm functional and factor four are supplied
readout structure.

On each ray, the linear closed-form profile has zero second difference for
`r=2,...,R`, including the supplied zero boundary at `R+1`.  The central graph
defect is `2A_R`.  This is exactly the Green relation for the declared finite
one-dimensional path with its boundary convention.

It is not the cubic 3D Laplacian, `1/r` Green field, Newtonian potential,
Einstein constraint, field stress, lapse equation, or metric dynamics.  The
source defect is a dimensionless finite normalization, not physical mass or
energy.

## Held geometry prediction

The no-refit held profile is reflection symmetric:

| radius | each-ray interval contrast |
|---:|---:|
| 1 | `5/36` |
| 2 | `4/36` |
| 3 | `3/36` |
| 4 | `2/36` |
| 5 | `1/36` |

The source retains `6/36`; the two rays together contain the remaining
`30/36`.  All norms sum to one.  The train radius-3 profile is independently
`u_0=4/16` and `(F_1,F_2,F_3)=(3,2,1)/16` on each ray.  Both use the same
formula and no fitted exponent, continuum limit, or host static solver.

Calling this “radial” means equal dependence on `|x|` on the two-sided line.
It does not mean Euclidean 3D spherical shells.

## Locality and proper-cubic covariance

Every Givens and clock SWAP acts on two adjacent M2.  Each fan CNOT acts on an
adjacent field/rail or rail/rail pair.  Each Fredkin support consists of a
rail control adjacent to one member of an adjacent probe-clock pair, hence a
connected three-M2 path.  Maximum support is three.

The train schedule has 996 gates; held has 1,660.  Every receiver contributes
the same 120 baseline clock SWAPs plus 45 response gates.  The only size-
dependent gates are the analytic nearest-neighbour source/ray Givens.

The full geometry and every primitive support are rotated together through
all 24 proper-cubic frames.  Adjacency and the decoded field are unchanged.
The construction therefore has carried covariance for this finite line
apparatus, not a proof of full cubic isotropy or a 3D field law.

## Deletion and lawful-domain controls

The runner tests:

- source deletion, which leaves every comparator at `4:4` and makes all
  interval contrasts zero;
- deletion of one held outward Givens, which changes the physical profile and
  breaks the frozen profile/harmonic fixture;
- deletion of the paired identical response fan/unfan coupling at receiver
  `+1`, which makes that local contrast zero without changing the source
  field; deleting only one member instead leaves a dirty response rail and is
  detected;
- deletion of one reference-clock SWAP, which makes that complete interval
  decoder undefined on affected branches;
- mutation of start identity, end identity, epoch, profile, reference device,
  probe device, source identity, and source calibration;
- deletion of event-ready and predecessor; and
- wrong widths, wrong Q sectors, malformed clocks/rails, and undeclared radii.

Metadata failures return undefined, never zero lapse or zero time.  Source,
propagation, response, clock comparison, identity, and interpretation remain
distinct load-bearing interfaces.

## Empirical, Record, metric, and gravity firewall

The physical coherent state and complete local words exist before any
occurrence.  An empirical field additionally needs actualized typed/permanent
events, matching identities/profiles/devices, registered source calibration,
and a justified numerical/statistical readout.  Cycle 459 supplies none of
those as a selection law.

Even granting an empirical dimensionless interval-contrast field does not
make it lapse, metric, proper time, energy/stress, or gravity.  Separate laws
would have to identify the source with physical matter/stress, establish a
3D field equation and common matter coupling, generate a faithful causal event
set, and prove the continuum/metric interface.  Deleting occurrence, Records,
numerical readout, source calibration, lapse law, metric law, or gravity law
separately makes the promoted object undefined while leaving the physical
candidate circuit intact.

Squared norms are not called probabilities.  No sampler, Born rule, frequency
theorem, empirical corpus, or actual receiver branch is selected.

## Wall and RSS caps

The cold runner measures elapsed wall time and process maximum resident set
size.  Frozen caps are 30 seconds and 768 MiB.  It materializes only the
`2R+1` nonzero Q1 branches, never a dense `2^M2` state or a global field
inverse.  The caps are implementation guards, not physical time, memory
axioms, resource costs, or complexity lower bounds.

## Supplied, derived, and open

Supplied:

1. the finite 1D line embedded in `Z^3`, radius, orientation, reflection
   symmetry, and zero Dirichlet boundary;
2. central Q1 source identity/preparation, analytic linear target profile,
   Givens angles, and propagation order;
3. one global delay-response candidate, four-cell clock calibration, complete
   clock starts, event IDs, epoch, profile, devices, predecessor, and source
   calibration;
4. norm-based interval-contrast functional, finite train/held split,
   tolerance, frame maps, wall/RSS caps, and observation harness; and
5. at any later promotion: occurrence, Record typing/permanence, empirical
   corpus/statistics, source-to-energy/stress identification, 3D field law,
   common coupling, metric/lapse/proper-time, and gravity interpretation.

Derived:

1. nearest-neighbour preparation of the analytic coherent line profile from
   one physical central source;
2. simultaneous complete `4:4`/`3:4` dual-clock words from identical local
   response circuits at every receiver;
3. exact E/G, full inverse, norm/Q1/rail/code/sidecar ledgers, all-frame
   locality, deletions, and resource bounds;
4. exact train/held reflection symmetry, held profile, one-dimensional
   harmonic residual away from the source, and central defect.

Open:

1. derivation or empirical selection of the source profile, global response
   law, zero boundary, and calibration;
2. a 3D isotropic/cubic Green field, physical mass-to-source map, common
   passive coupling, backreaction, field energy/stress, or nonlinear dynamics;
3. occurrence, Record formation, actual history, probability/Born law,
   sampler, frequency theorem, and empirical data;
4. autonomous event/profile/device/epoch/source identity genesis and renewal;
5. exact causal event-set construction, Lorentzian manifold/regularity
   interface, lapse, metric, proper time, continuum/boost theorem, or gravity.

## N1–N8 no-go-discipline stress test

Cycle 459 ships one positive bounded 1D construction.  The full stress test
prevents either the success or its limitations from being promoted to a
gravity theorem or substrate obstruction.

### N1 — Alternative route enumeration

| route | status | disposition |
|---|---|---|
| analytic reversible two-sided line propagation | ATTEMPTED / positive | this cycle |
| Cycle-420 host 3D static/dynamic receivers | ATTEMPTED / diagnostic | not physical-M2 Poisson compilers |
| local relaxation/fixed-point 3D solver | NOT TESTED / OPEN | Cycle 9 precedent is conditional |
| unitary quantum-walk/mediator 3D Green response | NOT TESTED / OPEN | could avoid this analytic line preparation |
| tensor/spin-2 or stress-mediated response | NOT TESTED / OPEN | not reduced to scalar line field |
| autonomous profile/epoch and actualized Record clocks | NOT TESTED / OPEN | time/Records bridge remains live |
| causal-density Lorentzian reconstruction | NOT TESTED / OPEN | repaired metric note keeps exact bridges open |
| empirical source/clock law discrimination | NOT TESTED / OPEN | requires actual events and statistical law |

The menu is non-exhaustive and several 3D routes remain open.

### N2 — Wall-independence audit

Source generation/calibration, 3D propagation, common matter coupling,
actuality/Records, numerical/statistical interpretation, and metric/continuum
reconstruction are distinct contracts.  Cycle 459 proves no general logical-
independence theorem among them and does not inflate them into independent
constitutional walls.

### N3 — Hidden-wall scan

The positive result supplies a finite line, boundary, closed-form amplitudes,
real Givens phases, exact source location, global delay sign, complete clocks,
event/profile/device fields, fresh finite capacity, noiseless gates, a norm
functional, and observation tolerance.  It does not test noise, indefinite
volume, renewal, generic source motion, multiple sources, recoil,
backreaction, 3D shells, or empirical calibration.

### N4 — Residual matching

Cycle 420's exact missing join is a local physical source-to-receiver update.
Cycle 459 partially matches it only on a one-dimensional analytic line with
dual-clock receivers.  It does not match Cycle 420's host-array 3D field,
signed profiles, static inverse, physical test-matter force, or detector
surfaces.  The residual is therefore narrower but not erased.

### N5 — Partial-closure path scan

The physical line circuit can be extended constructively to a small cubic
shell graph, to multiple central sources with explicit Q/resource accounting,
or to a local iterative relaxation/dilation law.  A Cycle-456 classifier and
Cycle-455 candidate corpus could be attached after separately supplied
actualization.  None requires axiom revision merely to test.

### N6 — Steelman

Grant the strongest result: one central physical source coherently drives ten
held dual clocks, all gates are nearest-neighbour and reversible, the complete
words define a radial held profile, and its finite second difference vanishes.
Even then, the profile and boundary were supplied analytically, the geometry
is a line, the readout is norm-based, and no event is actualized.  This is a
real physical interval-field construction and still not 3D gravity.

### N7 — Cross-cycle echo check

Cycle 204 keeps source/common-lapse coupling conditional.  Cycle 243 keeps
metric time downstream of physical event matching.  Cycle 420 exposes the
host-solver gap.  Cycle 431 closes a local response circuit; Cycle 451 closes
the shared dual-clock comparison; Cycle 456 closes local signature
classification.  Cycle 459 closes one multi-receiver line composition only.
Earlier progress repeatedly retired narrower imports, warning against both a
broad no-go and premature gravity language.

### N8 — Claim-gate result

Positive bounded line-field claim: **PASS** when all executable controls pass.

Broad gravity or no-go claim: **FAIL**.  The result is neither a 3D Poisson or
gravity law nor evidence that such a law is impossible.  Open constructive
routes, supplied profile/boundary structure, and absent actuality/metric
bridges forbid a minimum-content, shared-obstruction, or axiom-pressure claim.
No axiom pressure is asserted.

## Exact tests

The runner requires:

1. train/held exact `E_459 G_coarse = G_physical,459 E_459`, full propagation+
   response+clock inverse, norm, Q1, blank-rail, complete-clock, and sidecar
   controls;
2. exact analytic profile matching, reflection symmetry, held no-refit values,
   interior/boundary harmonic residual, and source defect;
3. maximum primitive support three, identical response gate counts at every
   receiver, and all-24 carried line covariance;
4. source, propagation, response, reference clock, start/end identity, epoch,
   profile, reference/probe device, source identity/calibration, event-ready,
   and predecessor deletions;
5. empirical/Record/numerical/lapse/metric/gravity semantic deletions;
6. lawful-domain refusal, exact physical inventory, and frozen wall and RSS
   caps; and
7. the complete supplied/derived/open and N1–N8 boundaries.

Bit, word, identity, inverse-permutation, and rational interval checks are
exact.  Floating tolerance is restricted to the analytic Givens state vector,
norm-derived interval contrast, and harmonic residual.  No norm is called a
probability.

Cold result: **8 passed, 0 failed**.  Maximum train/held E/G, inverse, norm,
Q1, or rail residual is `1.7772239894833365e-16`.  Maximum harmonic residual
is `1.249000902703301e-16`; maximum analytic-profile/source-defect residual is
`8.326672684688674e-17`.  The train source defect is exactly `1/8`; the held
source defect is exactly `1/18`.  All 24 frames have zero primitive-locality
failures.  The final frozen observed wall/RSS row is approximately `3.64 s /
62.34 MiB`, below the `30 s / 768 MiB` caps.

The train schedule SHA-256 is
`b5ec36142b0d16a6b0563d669116db2c23b70192b7816272b532ff9fc9a14992`;
the held schedule SHA-256 is
`16ac469c91ca17e5239fa52a0f886fafdb4dcdcaf0a1e369d4099b8c1c3a6671`.
