# Physical cubic-shell relational-interval field — Cycle 461 note (2026-07-19)

**Authority: none. Audit: unset.**

## Claim

Cycle 461 constructs a **physical cubic-shell relational-interval field** on
the actual integer lattice.  The train cube `[-1,1]^3` has 27 field sites and
26 noncentral receivers.  The held cube `[-2,2]^3` has 125 field sites and 124
noncentral receivers.  A central Q1 excitation is prepared by a fixed
nearest-neighbour physical M2 circuit.  Four identical local clock sweeps and
one identical local delay-response circuit then act at every receiver.  On the
declared code space the executable tests

\[
  E G_{\rm coarse}=G_{\rm physical}E
\]

together with the inverse, norm, Q1, corridor, rail, decoder, deletion,
held-domain, and resource controls.

The construction is a finite supplied three-dimensional response fixture.  It
is **not lapse, metric, proper time, energy/stress, backreacting gravity, or a
derived universal source law**.  Its update count and circuit depth are not
time.  Its norm-weighted readout is not named probability.  No phase is named
energy and no generator is named a rate.

It is not a derived universal source law.

## Frozen domains and exact target

For a cube of radius `R`, values outside the cube are exactly zero.  The frozen
criterion is checked with `Fraction` arithmetic at every declared site:

\[
  6u(x)-\sum_{|e|_1=1}u(x+e)=0\quad(x\ne0),
\]

while the central row is an explicit positive source defect.  This is a
discrete six-neighbour Dirichlet/harmonic criterion, not a continuum equation.
The executable checks all 26 train nonsource rows and all 124 held nonsource
rows; it does not check only orbit representatives.

The complete supplied orbit profile is:

| cube | sorted absolute orbit | exact value | central defect |
|---|---:|---:|---:|
| train | `(0,0,0)` | `11/42` | `17/14` |
| train | `(0,0,1)` | `5/84` |  |
| train | `(0,1,1)` | `1/42` |  |
| train | `(1,1,1)` | `1/84` |  |
| held | `(0,0,0)` | `68/577` | `297/577` |
| held | `(0,0,1)` | `37/1154` |  |
| held | `(0,0,2)` | `11/1154` |  |
| held | `(0,1,1)` | `75/4616` |  |
| held | `(0,1,2)` | `29/4616` |  |
| held | `(0,2,2)` | `13/4616` |  |
| held | `(1,1,1)` | `6/577` |  |
| held | `(1,1,2)` | `21/4616` |  |
| held | `(1,2,2)` | `5/2308` |  |
| held | `(2,2,2)` | `5/4616` |  |

Both tables are separately normalized.  The held table is compiled without a
fit to train output.

## Physical compiler

Each coarse coordinate `x` is embedded at physical coordinate `40 x`:
**supercell scale 40**.  The scale is supplied structure.  The deterministic
spanning-tree parent reduces the first nonzero coordinate in x-y-z order by
one toward zero.  The tree is intentionally asymmetric.

For each tree edge, an exact subtree fraction `q` fixes one supplied Givens
angle by

\[
  \sin^2\theta=q.
\]

The child endpoint is routed through 39 adjacent SWAPs, the Givens acts on two
adjacent sites, and the route is restored through 39 SWAPs.  Thus every coarse
tree edge compiles to 79 support-two primitives.  There are 26 exact train
ratios/angles and 124 exact held ratios/angles.  The runner emits the full
ordered inventory `(tree-edge label, exact q, theta to 17 digits)` plus its
SHA-256 digest.  This deterministic emitted list—not an unstated numerical
optimizer—is the complete supplied angle inventory.  Removing an angle/table
entry is an explicit deletion control.

Every noncentral origin has the same geometry and program:

- complete 16-M2 reference, probe, start-reference, and start-probe one-hot
  clock words;
- one blank 15-M2 response rail;
- one identical four-sweep reference/probe baseline;
- one identical 45-primitive fan / controlled inverse sweep / unfan delay;
- start/end event identity, epoch, profile identity, unique reference/probe
  device identities, source identity/calibration, event-ready, and predecessor
  sidecars.

No per-site response program exists.  The supplied field appears only in the
single source-preparation angle inventory.  Propagation restores all route
corridors before receiver responses, so the reused positive-z response rail is
blank at its declared boundary.

There is **no host Poisson solve during update**.  The runner contains no
linear-system solver.  The rational orbit tables, zero exterior, scale 40,
tree rule, exact angle ratios, finite clock design, sidecars, delay law,
source identity/calibration, and norm-weighted interval readout are all
supplied structure.

## Two different covariance checks

The output profile is exactly invariant under all 24 proper-cubic frames:
every transformed coordinate has the same supplied rational value.

This does not make the asymmetric tree invariant.  Separately, the executable
carries the whole spanning tree, routes, comparator blocks, and ordered
schedule through each of the all 24 proper-cubic frames and directly checks
the support of every carried primitive.  Physical compiled apparatus/schedule
covariance means covariance of that carried apparatus.  It is not inferred
from output invariance, and the tree itself is not claimed invariant.

## Decoder and deletions

For each receiver the decoded local object is a dimensionless relational
interval candidate from a shared start/end event pair.  The reference clock
advances four cells.  A branch occupying that receiver delays its probe to
three cells; all other branches advance four.  The derived field is the
norm-weighted quantity `4 ||(1-R_x) psi||^2`, numerically equal to the supplied
site weight.  Calling it a physical probability would require an additional
Born bridge.

The executable deletes or mutates:

- the central source (all receiver contrasts vanish);
- one preparation Givens (the target profile changes);
- one receiver response (that local contrast vanishes);
- one receiver reference sweep (the interval decoder refuses);
- every sidecar field in turn (the decoder refuses);
- a supplied orbit-table entry (compilation refuses);
- the declared train/held family (an undeclared radius refuses).

These controls distinguish necessity within this fixture from a derivation of
gravity or a general obstruction.

## Exact supplied/imported inventory

Supplied here:

1. train and held cube domains and zero exterior;
2. the fourteen rational orbit entries and two central defects above;
3. supercell scale 40 and the asymmetric x-y-z parent rule;
4. all exact subtree ratios and their Givens-angle conversion (fully emitted
   by the runner with stable inventory digests);
5. four baseline sweeps and the identical local delay law;
6. event/profile/source/device sidecar constants;
7. the norm-weighted interval-contrast readout;
8. wall cap 30 seconds and RSS cap 768 MiB.

Imported from Cycles 444/445/451:

- the 16-M2 one-hot clock word and reversible nearest-neighbour sweep;
- the 15-M2 fan / controlled-clock-swap / unfan delay response;
- the dual-clock relational-interval decoder boundary.

Not supplied or derived: occurrence, a physical Record, a Born rule, a
universal source law, energy/stress, lapse, metric, proper time, curvature,
backreaction, continuum/infrared behavior, or empirical calibration.  A Q1
source label is not a stress-energy tensor.  A copied pointer is not promoted
to a Record.

## N1–N8 stress test

### N1 — Alternative route enumeration

A dynamical source law, a local gauge route, a record-derived causal-geometry
route, and a continuum/infrared derivation remain open.  The present supplied
preparation is one constructive route only.

### N2 — Wall-independence audit

The Dirichlet table/boundary, preparation tree/angles, clock-response law,
norm readout, and source calibration are independent imports.  Closing one
does not close the others.

### N3 — Hidden-wall scan

Hidden walls include the finite zero boundary, scale-40 routing slack,
asymmetric scheduling apparatus, one-excitation sector, comparator design,
and assumed availability of the supplied rational profile.

### N4 — Residual matching

Exact zero Laplacian rows and small floating compiler residuals establish only
the declared finite rational fixture.  They do not establish a continuum or
universal source equation.

### N5 — Rhetoric audit

No wrapped phase is called physical energy, no generator element is called a
rate, update count is not time, pointer copying is not a Record, and this
coarse prepared field is not called a physical-site gravity compiler.

### N6 — Partial-closure path scan

The positive retained result is meaningful: a full three-dimensional finite
response profile, including a held cube, can be prepared and read through
bounded nearest-neighbour M2 neighborhoods with identical local receiver
logic and proper-cubic carried-apparatus covariance.

### N7 — Steelman

A stronger route would derive the table and preparation angles from one
universal local source rule, connect the source to operational matter or
energy/stress, derive clock response rather than supply it, and demonstrate
backreaction and an infrared geometric limit.

### N8 — Claim-gate result

**Broad gravity or no-go claim: FAIL.**  The constructive fixture survives,
but it does not support an impossibility, minimum-content, or universal-gravity
claim.  The remaining walls are separable imports.  Therefore there is **no
axiom pressure** from Cycle 461.

## Disposition

Cycle 461 is eligible only as a bounded constructive compiler/response result
if its executable freezes with zero failed tests and the declared wall/RSS
caps.  It is not axiom language, foundation text, Qualification, a registry or
policy change, queue movement, or an audit verdict.
