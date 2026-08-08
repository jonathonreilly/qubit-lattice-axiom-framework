# Physical quantum-source / density-interface tournament — Cycle 473

Date: 2026-07-19

Authority: none

Audit: unset

Admission target: none

## Result

Cycle 473 asks a narrow but load-bearing cross-lane question.  The weak-field
gravity science identifies the candidate local quadratic source density
`rho_x=|alpha_x|^2`, while Cycles 465 and 468 physically implement coherent
source-position branches that control distinct fields.  Can one linear,
single-copy physical isometry instead append one deterministic pure mean field
built from those squared amplitudes?

The tested target is a **single-copy deterministic pure mean-field product
compiler**; it is not the definition of every possible density interface.

On actual Cycle-465/468 physical source fields, the answer is exact for the
declared train and held families:

1. erasing the source and outputting only the deterministic pure mean field
   fails Gram preservation;
2. retaining the source unchanged and appending that field as a pure product
   also fails Gram preservation for nonorthogonal states with different
   densities;
3. branch-controlled sourcing is constructive and preserves the complete
   source Gram matrix;
4. a dephased Stinespring route is constructive but exports a mixed branch
   ledger after its environment is ignored, not one deterministic pure mean
   field;
5. a finite multi-copy estimator route is unbiased but has nonzero finite-copy
   variance; and
6. a Record-conditioned route can prepare a branch field if an actualized
   Record is supplied, but it does not derive occurrence or the mean density.

Thus the licensed negative is only:

> **Scoped single-copy product-interface no-go: PASS** on the declared
> physical train/held state families and linear-isometry output contract.

The broader gate is deliberately rejected:

> **Broad P1, Born, probability, gravity, or framework no-go: FAIL.**

`rho=|psi|^2` is a supplied candidate source functional in this probe.  Norm
weight is not probability.  No occurrence, frequency law, Record formation,
mass normalization, universal coupling, or empirical gravity is derived.
There is no axiom pressure.

Runner:

`scripts/physical_quantum_source_density_interface_tournament_cycle473_2026_07_19.py`

## Why this matters

The two repository shores use similar notation but different physical maps.

The weak-field source-response theorem first assumes a local, diagonal,
positive, phase-invariant quadratic functional and translation covariance,
then derives the unique normalized expression

```text
rho_psi(x) = |psi(x)|^2.
```

That theorem identifies the functional once its operational class is granted.
It does not construct a reversible physical interface that takes one unknown
pure source state to a classical or pure-field representation of the
functional.

Cycles 465 and 468 implement a different, fully linear map:

```text
sum_x alpha_x |x,r>_S |0>_F
  -> sum_x alpha_x |x,r>_S |F_x>_F.
```

This is coherent operator/branch sourcing.  It can entangle source and field,
and then field and test matter.  It does not replace the joint state by a
single field generated from the expectation weights `|alpha_x|^2`.

Cycle 473 reconnoiters this exact gap rather than calling one shore the other.

## Frozen train and held states

The train family uses the actual Cycle-468 R1 source menu with three physical
M64 Q1 source cells and the associated Cycle-463/Cycle-464 Q1 field states.
The held family uses the R2 menu with four source cells, including the unseen
off-axis position `(1,1,0)`.

For each menu the runner uses:

- every source-position basis state;
- `A=(|0>+|1>)/sqrt(2)`;
- `B=(|0>+|last>)/sqrt(2)`, where held `last` is the unseen off-axis branch;
- `A_i=(|0>+i|1>)/sqrt(2)`.

`A` and `B` are nonorthogonal but have different exact density words.  `A`
and `A_i` have the same density and different phase.  The frozen candidate
mean profile is

```text
u_rho(y) = sum_x |alpha_x|^2 u_x(y),
```

followed by the existing Cycle-464 neighbor-direction lift and Q1 amplitude
preparation.  This target is a supplied nonlinear compile-time constructor,
not a physically derived update and not a Born rule.

## Exact Gram theorem

Let `F(rho_psi)` be the normalized pure Q1 field made by the supplied
constructor.

### Erased-source target

Assume a single-copy isometry has the action

```text
W |psi>_S |0>_F = |blank>_S |F(rho_psi)>_F.
```

An isometry must preserve every source inner product.  The phase pair `A` and
`A_i` has the same density and therefore the same field output, whose overlap
is one.  Their source overlap is not one.  The complete target Gram matrix
therefore differs from the source Gram matrix.

### Retained-source product target

Assume instead

```text
W |psi>_S |0>_F = |psi>_S |F(rho_psi)>_F.
```

For two nonorthogonal inputs `psi,phi`, preservation requires

```text
<psi|phi> = <psi|phi><F(rho_psi)|F(rho_phi)>.
```

The actual `A/B` field targets are distinct and do not have unit overlap, while
`<A|B>=1/2`.  The retained pure-product target therefore also fails the full
Gram condition.

This theorem does not assume that every density-source law must be a pure
product isometry.  It shows precisely why a deterministic nonlinear
expectation-valued field cannot be silently inserted into the present
single-copy reversible substrate.

## Constructive routes that remain

### Branch-controlled operator sourcing

The actual Cycle-465/468 map retains the orthogonal source-position label:

```text
W_branch |x,r>|0> = |x,r>|F_x>.
```

Linearity then defines the coherent map on every superposition.  Orthogonality
of the retained physical source cells makes the complete source Gram matrix
exactly preserved even when the branch fields overlap.  No host chooses a
runtime branch.

### Dephased Stinespring route

An additional environment label gives

```text
V |x,r>|0>|0> = |x,r>|F_x>|x>_E.
```

This is also an exact isometry.  Ignoring the environment removes source
off-diagonal terms and leaves a mixed branch ledger with weights
`|alpha_x|^2`.  A partial trace is algebra, not an occurrence or Record.  An
actual open-system law and operational reason to ignore or reset the
environment remain supplied structure.

### Finite multi-copy estimator route

With `n` identically prepared copies, a reversible occupation counter could
write finite counts.  The present runner freezes the exact count distribution
and register width, not a literal counter-gate trace.  For the half/half
fixture its estimator has exact mean
`1/2` and variance `1/(4n)`.  The runner freezes `n=2` on train and `n=5` on
held.  Both have nonzero variance, so neither provides the deterministic exact
single-run density.  A concentration/asymptotic theorem plus an operational
copy source remains open.

### Record-conditioned route

If an actualized, typed, permanent position Record is supplied, a controlled
compiler may prepare `F_x`.  Cycle 473 does not produce that Record, equate a
pointer with a Record, or derive the frequency of its values.

### Nonlinear mean-field law

A fundamental nonlinear update could directly compute `rho` from one state.
That route lies outside the linear-isometry contract tested here and must be
declared and checked for mixture ambiguity, signaling, covariance, inverse or
open-system semantics, and empirical consequences.  It is not excluded.

## Locality, covariance, and resources

The positive branch route uses the existing physical M64 Q1 source cells and
Cycle-463/464 field apparatus.  The dephased route adds one finite one-hot
environment label per menu position.  The copy route adds finitely many source
copies and a bounded counter.  These are finite resource statements, not a
claim of renewal or asymptotic availability.

For the supplied candidate mean profiles, the runner carries the source menu,
profile, cell coordinates, and six field directions through **all 24
proper-cubic frames**.  It rebuilds each carried Q1 field and compares it with
the explicitly permuted original.  The asymmetric source menus are carried,
not claimed invariant.

The runner also deletes the branch-distinct field response by replacing every
branch field with one common field.  The update stays isometric because the
source label is retained, but field distinguishability disappears.  Deleting
the retained source label instead destroys the branch-map Gram condition.
These are necessity checks inside the declared construction, not minimum-
content claims.

## Supplied, derived, and open

Supplied:

1. actual Cycle-465/468 physical Q1 source positions and branch fields;
2. finite train/held menus, source amplitudes, codes, tolerance, and resource
   caps;
3. the candidate source functional `rho_x=|alpha_x|^2`;
4. global density-weighted word addition, Cycle-464 normalization/direction
   lift, square roots, and Q1 amplitude preparation;
5. the single-copy linear-isometry and deterministic pure-product output
   contract used by the scoped theorem;
6. environment labels, multiple copies, counters, or Records only on their
   respective alternative routes.

Derived:

1. exact train/held Gram mismatch for erased and retained pure-mean-field
   targets;
2. exact Gram preservation for actual branch-controlled sourcing;
3. exact dephased Stinespring isometry and mixed reduced ledger;
4. finite-copy expectation and nonzero variance;
5. density/Q1-field covariance in all 24 carried frames and visible route
   deletions.

Open:

1. selection between operator/branch sourcing, semiclassical expectation
   sourcing, dephased/open-system sourcing, multi-copy estimation, a
   Record-conditioned law, or a declared nonlinear law;
2. physical derivation of the density functional's eligibility premises and
   mass normalization;
3. autonomous global word-to-Q1 amplitude preparation and inter-supercell
   word delivery;
4. environment genesis/reset, actual occurrence, Record formation, frequency,
   probability, and realized history;
5. universal coupling, physical time/rate, asymptotic potential, source recoil,
   two-body law, continuum scaling, and empirical gravity.

## Six-wall effect

- `C_ref`: the choice of source interface, `rho` functional, mean-field
  preparation, environment/copies/Records, mass scale, and coupling remain
  supplied.
- `C_num`: squared norms enter as exact density-functional inputs only.  Norm
  weight is not probability or frequency.
- `C_wrap`: unchanged.  Update count is not time; no generator element is a
  calibrated rate.
- `C_int`: branch-controlled interaction is constructive.  Mean-field law
  selection, calibration, and open-system semantics remain.
- `C_local`: the tournament uses actual bounded M2/Q1 source and field states.
  Mean-profile amplitude preparation and inter-supercell delivery remain.
- `C_source`: sharply narrowed.  The deterministic single-copy pure-product
  interface is excluded on the declared family, while branch/operator,
  dephased, multi-copy, Record-conditioned, and nonlinear routes remain live.

## N1 — Alternative route enumeration

| Route | Status | Terminal obligation |
|---|---|---|
| erase source, deterministic pure mean field | attempted / exact negative | preserve source Gram matrix |
| retain source, deterministic pure-product mean field | attempted / exact negative | preserve nonorthogonal source overlaps |
| coherent branch/operator sourcing | attempted / constructive | actual Cycle-465/468 E/G and inverse |
| dephased Stinespring route | attempted / constructive bounded | justify environment/open-system semantics |
| finite multi-copy estimator route | attempted / constructive bounded | copies plus concentration/operational readout |
| Record-conditioned branch preparation | open | derive occurrence, typing, permanence, and Record chain |
| declared nonlinear mean-field law | open | specify dynamics and test signaling/covariance/empirical effects |
| other density observables/source fields | open | eligibility, calibration, and physical compiler |

Because multiple materially distinct source interfaces remain live, the
scoped theorem cannot be promoted to a broad P1 or framework no-go.

## N2 — Wall-independence audit

Single-copy linearity, deterministic purity, the density functional, amplitude
preparation, environment semantics, copy resources, Records, mass calibration,
and gravity interpretation are separate contracts.  The two negative product
routes share the same Gram-preservation obligation and are not counted as
independent substrate walls.

## N3 — Hidden-wall scan

The probe supplies exact finite amplitudes, noiseless orthogonal source codes,
actual prepared branch fields, density-weighted global word addition, field
normalization, direction lift, amplitude synthesis, and numerical tolerance.
The pure-product theorem additionally supplies a deterministic normalized
field target.  Alternative routes expose their environment, copies, counters,
or Records explicitly.

## N4 — Residual matching

The witness matches the actual cross-lane residual: the weak-field theorem
identifies a candidate density functional while Cycles 465/468 implement
branch-controlled physical fields.  It does not match the separate residuals
of Born probability, occurrence, Newton normalization, universal coupling,
proper time, asymptotics, or empirical gravity.

## N5 — Rhetoric audit

The negative result is quantified over the declared train/held states and one
linear-isometry pure-product interface.  It is not quantified over arbitrary
open systems, nonlinear laws, multi-copy limits, Records, density observables,
or source theories.  “Physical” refers to the actual M2/Q1 states consumed,
not to a probability or gravity interpretation.

## N6 — Partial-closure path scan

The branch route is already positive.  A dephasing channel, actualized Record
instrument, or justified copy/concentration protocol could give an operational
density ledger.  A two-body operator source may bypass semiclassical P1
entirely for the branch-entangling prediction.  None requires an axiom edit at
this stage.

## N7 — Steelman

Grant the strongest objection: a deterministic `|psi|^2` mean field cannot be
appended reversibly from one unknown pure state under the tested contract.
That does not show density is impossible.  It shows the theory must state
whether density is an expectation observable, an open-system mixed ledger, a
many-copy estimate, a realized Record field, or a fundamental nonlinear
state-dependent law.  Each has different empirical and compositional content.

## N8 — Cross-cycle echo and claim gate

The weak-field source theorem fixes `|psi|^2` only after functional eligibility
premises.  Cycles 465/468 positively realize coherent branch sourcing and
explicitly leave probability/occurrence open.  Cycle 473 makes their interface
difference executable.

Scoped single-copy product-interface no-go: **PASS** only if the frozen Gram,
deletion, domain, held, and covariance tests pass.

Broad P1, Born, probability, gravity, or framework no-go: **FAIL**.

No minimum-content theorem, shared-substrate obstruction, or axiom-pressure
claim follows.  There is **no axiom pressure**.

## Interpretation firewall

- `rho=|psi|^2` is a supplied candidate source functional here, not a derived
  probability law.
- Norm weight is not probability, frequency, occurrence, or a Record.
- A partial trace is not an actualized event.
- A branch field is not a semiclassical mean field.
- A source response is not gravity.
- Update count is not time.
- A generator element is not a rate, and phase is not energy.

## Frozen execution

The final cold execution reports `RESULT pass=14 fail=0`.

| quantity | train | held |
|---|---:|---:|
| source Gram versus erased pure mean field | `2.7937554111603204` | `3.9077213027839273` |
| source Gram versus retained-source pure product | `0.5941953026558615` | `0.3877841204943804` |
| different-density mean-field distance | `0.7865676777730606` | `0.6621672660260057` |
| same-density phase-pair field distance | `0.0` | `0.0` |
| actual branch-map Gram residual | `1.9641850382783467e-15` | `4.961343107790912e-15` |
| dephased Stinespring Gram residual | `2.1006405424489063e-15` | `2.1487476809986495e-14` |
| finite-copy density variance | `1/8` at `n=2` | `1/20` at `n=5` |
| source-label deletion Gram residual | `3.0072587159255364` | `4.569479846622764` |

The `A/B` physical source overlap is `0.5` in both families.  Their mean-field
overlaps are `0.6906556441413474` and `0.7807672559018224`, so the retained
product contradiction is not a tolerance artifact.  Replacing every branch
field by one common field leaves an isometric source-only map but makes the
post-deletion field spread exactly zero.  The intact field-replacement
residuals are `1.1342034590405388` and `1.013900214843479`.

All 312 case/frame comparisons across all 24 proper-cubic frames have zero
residual.  Four malformed-domain probes are refused.  Including imports, the
runner takes `100.7450158749707` seconds and peaks at `783,892,480` bytes,
below the frozen 240-second and 3-GiB caps.  The external process measurement
is 102.24 seconds with the same maximum resident size.
