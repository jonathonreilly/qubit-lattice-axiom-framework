# Koide Orbit-Occupancy Gaussian Moments and the Aggregate Equipartition-Granularity Fork

**Date:** 2026-06-09
**Repair update:** 2026-07-12
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This note does not set or
predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py`](../scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt`](../logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt)
(`SUMMARY: PASS=27 FAIL=0`)

The filename is retained for citation stability. The repaired claim is narrower
than the historical title encoded in that filename.

> **Bounded claim.** For the explicitly enumerated local channel-bookkeeping
> surface below, the honest Gaussian moment gives `r = 1`. The alternative
> endpoint `r = 1/2` follows only after imposing the aggregate
> per-outcome-cell condition `E_s = E_d`. Two constructed aggregate conditions
> share the checked carrier, channel energy, symmetry, outcome indexing, and
> `Q` dictionary and differ by one supplied integer, the doublet counting unit.
> This is a conditional algebraic fork and a source-text nonselection boundary,
> not a formal model-theoretic independence theorem for the full lattice axioms
> and not a derivation or adoption of the per-outcome-cell condition.

## Repair finding and disposition

The 2026-07-10 independent review identified the decisive arithmetic error:

> “The holomorphic Gaussian integral does not yield the claimed one-slot
> equipartition moment: with `Z=pi/g` and `g=6 beta`, it gives
> `<|b|^2>=1/(6 beta)`, hence `r=1`, not `1/2`. The runner obtains `r=1/2` by
> hard-coding a per-slot quantum rather than deriving it from that integral.”

The finding is correct. The repair makes four changes.

1. It derives every Gaussian moment directly and removes the hard-coded
   `per_slot_quantum`.
2. It withdraws the former map `r = 1/(2 rho)` and every inference from a
   partition-function ratio to an `r` ratio.
3. It states `r = 1/2` only as the consequence of an explicit aggregate
   per-outcome-cell equal-energy condition.
4. It removes the componentwise fixed-basis equation
   `3a^2 = 6x^2 = 6y^2` from the witness claim. That equation is not invariant
   under the checked `Z_3` rotation. The surviving real-dimension horn is only
   the invariant aggregate relation `E_d = 2E_s`.

## Explicitly checked surface

The bounded result uses only the following named content.

| element | role |
|---|---|
| carrier `(a,b) in R_{>0} x C` | local generation-channel parametrization; `a>0` makes `r` well-defined |
| `E_s = 3a^2`, `E_d = 6|b|^2` | channel-energy bookkeeping |
| `Q = (1+2r)/3`, `r=|b|^2/a^2` | exact circulant trace dictionary, rederived in the runner and algebraically adjacent to [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) |
| Lattice, Qubit, Admissibility, Record | approved foundation in [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) |
| pointwise realized-state interface | approved [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md); it supplies no state-contingent `r` value |
| outcome cells `{e_0}` and `{e_1,e_2}` | supplied K/CPT orbit indexing, conditional on the [`K/CPT orbit-constancy supplied-context bridge`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md) |

The supplied K/CPT context is a bounded condition. It is not generic Record
axiom content. The Gaussian density used below is a diagnostic assumption, not
a premise that selects the per-outcome-cell condition.

## Honest Gaussian moment

Take the stated diagnostic density

```text
exp[-beta (3a^2 + 6|b|^2)],   beta > 0.
```

For the singlet coordinate,

```text
<a^2> = 1/(6 beta).
```

For `b = x+iy`, either Cartesian integration or the polar measure
`d^2b = rho d rho d theta` gives

```text
Z_b = pi/(6 beta),
<|b|^2> = 1/(6 beta),
r_moment = <|b|^2>/<a^2> = 1.
```

Equivalently, with `g = 6 beta`, `Z_b = pi/g` and `<|b|^2> = 1/g`.
A multiplicative normalization of the same measure cancels between numerator
and denominator. The Cartesian and polar calculations are coordinate forms of
the same density and give the same partition integral and moment.

The expectation values obey

```text
<3a^2> = <6x^2> = <6y^2> = 1/(2 beta),
<E_d> = 2 <E_s>.
```

Thus this Gaussian realizes the real-coordinate count in expectation and does
not yield `<E_d> = <E_s>`. No Gaussian result in this note derives `r = 1/2`.

## Decoupled partition-cell arithmetic

The runner also reproduces four older integral/kernel facts:

```text
real two-coordinate Gaussian kernel:  Z = 2 pi/g
Majorana two-by-two Pfaffian kernel:    Z = 2 pi/g
polar complex Gaussian kernel:         Z = pi/g
one-by-one complex Berezin kernel:      Z = pi/g
```

These cells use different quadratic kernels or determinant powers. They are
not two coordinate presentations of the identical diagnostic density above.
Their factor-two ratio is therefore kept only as decoupled
quadratic-kernel/determinant-power arithmetic. The values alone contain no
equation for `r`. The former definitions

```text
rho = (pi/g)/Z_d,
r = 1/(2 rho)
```

are withdrawn as an unsupported attribution of `r` to `Z_d`.

## Aggregate equipartition-granularity fork

Define one aggregate condition with a supplied doublet counting unit `n_d`:

```text
E_s = epsilon,
E_d = n_d epsilon.
```

Using `E_s = 3a^2` and `E_d = 6|b|^2` gives

```text
r = |b|^2/a^2 = n_d/2,
Q = (1+2r)/3 = (1+n_d)/3.
```

The two constructed extensions are:

```text
aggregate real-dimension count:  n_d = 2  ->  r = 1    ->  Q = 1
aggregate outcome-cell count:    n_d = 1  ->  r = 1/2  ->  Q = 2/3
```

“Real-dimension count” here is an aggregate channel-energy statement. It does
not assert equal realized energies in fixed Cartesian components `x` and `y`.
“Outcome-cell count” is conditional on the supplied orbit indexing. Neither
count is selected by the approved foundation or by the realized-state
primitive.

### Premise-surface parity

The comparison is deliberately small.

| element | real-dimension extension | outcome-cell extension |
|---|---|---|
| carrier | `(a,b) in R_{>0} x C` | same |
| channel energy | `E_s=3a^2`, `E_d=6|b|^2` | same |
| `Q` dictionary | `Q=(1+2r)/3` | same |
| checked symmetry | functions of `(a,|b|)`; invariant under `b -> omega b` and `b -> conjugate(b)` | same |
| supplied orbit indexing | `{e_0}`, `{e_1,e_2}` | same |
| aggregate condition form | `E_s=epsilon`, `E_d=n_d epsilon` | same |
| **doublet counting unit** | **`n_d=2`** | **`n_d=1`** |

The “one difference” statement is about these two explicitly constructed
extensions, not an exhaustion theorem over all possible dynamics or
readout laws. The runner includes a negative control that changes the channel
energy as well; the parity gate then detects two differences rather than one.

### Compatibility checks

For each `n_d in {1,2}`, the solution set

```text
|b|^2 = (n_d/2) a^2
```

is nonempty. Because it depends only on `|b|`, it is invariant under the
checked `Z_3` rotation and complex conjugation. On the two-cell outcome
algebra, assigning `I({s})=E_s` and `I({d})=E_d` gives a finite additive
readout; the runner checks every disjoint subset pair.

These checks establish compatibility with the enumerated local constraints.
They do not construct a full `Z^3` lattice model, a concrete Admissibility
rule, record-production dynamics, or a physical charged-lepton readout bridge.

## Proposed per-outcome-cell condition

The proposal is simply:

> On the supplied two-orbit outcome context, use one aggregate channel-energy
> unit per outcome cell, `E_s = E_d`.

This condition is not in
[`axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json). It has zero
premise weight unless it is derived and independently audited, or explicitly
approved through a reviewed premise-registry update. This note does not make
that approval and does not treat the condition as an existing primitive.

## Import and support inventory

- **Approved foundation:** `minimal_axioms` and `realized_state_primitive`.
  These are registered premise nodes, not imports and not sources of bounded
  status.
- **Bounded supplied context:** K/CPT orbit indexing from the linked
  supplied-context bridge. It labels the two outcome cells but supplies no
  energy equality or `r` value.
- **Exact conditional algebra:** the channel-energy equations, Gaussian
  integrals, `r=n_d/2`, and `Q=(1+n_d)/3`.
- **Support-only arithmetic:** the four decoupled partition/kernel cells.
- **Observational comparator:** the 2026 Particle Data Group central masses
  `m_e=0.51099895069 MeV`, `m_mu=105.6583755 MeV`, and
  `m_tau=1776.93 MeV` give `Q_PDG=0.666664463403`, differing from `2/3` by
  `-2.2033e-6`. The values come from the
  [PDG 2026 lepton summary table](https://pdg.lbl.gov/2026/tables/rpp2026-sum-leptons.pdf).
  They are printed only, never thresholded, and never used on a derivation or
  PASS/FAIL path.

## No-Go Discipline Gate

The negative content is only the scoped statement that the enumerated checked
surface does not itself select `n_d`. It is not a universal derivation no-go.

### N1 — Alternative-route enumeration

1. **Minimal-axiom text — ATTEMPTED.** A direct check of the
   [`Qualification`](MINIMAL_AXIOMS_2026-06-29.md#qualification) asks whether
   Lattice, Qubit, Admissibility, or Record states an occupancy/equipartition
   count. The current Qualification instead leaves non-fixed structure
   conditional or open; it does not name `n_d`.
2. **Realized-state primitive — ATTEMPTED.** The
   [`realized-state interface`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md#the-primitive)
   might have been mistaken for a supplied realized `r`. Pointwise evaluation
   is allowed, but the primitive explicitly supplies no state-contingent value,
   so it does not choose either horn.
3. **`Z_3` and conjugation symmetry — ATTEMPTED.** The
   [paired runner](../scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py)
   verifies that both aggregate relations are invariant under the checked
   actions, so these symmetries do not distinguish
   `n_d=1` from `n_d=2` on this surface.
4. **Record finite additivity — ATTEMPTED.** The paired runner's exhaustive
   two-cell subset checks show additive readouts for both horns. Additivity
   alone does not fix their
   relative channel energies.
5. **Gaussian moment / measure normalization — ATTEMPTED.** The paired runner's
   honest integration gives `r=1` in both coordinate systems, and a
   multiplicative measure factor
   cancels. It supplies no `r=1/2` route.
6. **K/CPT orbit indexing — ATTEMPTED.** The
   [supplied-context bridge](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md#the-supplied-context)
   identifies two orbit cells and transfers record-content equality to
   orbit-constant
   readout. It explicitly does not supply weighting, probability, or an energy
   equality, so the cell labels alone do not choose `n_d=1`.

### N2 — Wall-independence audit

There is one selection residual after conditioning on the supplied orbit
context: the aggregate doublet counting unit `n_d`. Orbit indexing is an
explicit upstream condition, not a second independent wall. Supplying orbit
labels does not supply equal channel energy; imposing `n_d=1` presumes those
labels. The note therefore presents one residual rather than inflating the
count to two independent walls.

### N3 — Hidden-wall scan

- “supplied orbit indexing” is the explicit bounded condition linked above;
- the Gaussian density is diagnostic only;
- the `Q` dictionary is rederived in the runner;
- finite additivity is checked on constructed witness readouts only;
- PDG values are report-only observational comparators;
- no standard-QFT, probability, dynamics, normalization, or physical-species
  bridge is hidden in the conclusion.

### N4 — Residual matching

| cited source | source role | residual used here | match |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), lines 74–84 | names the supplied foundation and its non-supply boundary | whether the foundation states `n_d` | yes |
| [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md), lines 19–45 | pointwise evaluation without state-contingent content | whether the primitive supplies `r` | yes |
| [`KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md), lines 53–87 | orbit indexing and orbit-constant readout only | whether orbit labels also fix relative energy | yes |
| [`scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py`](../scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py), lines 84–109 | exact trace derivation plus independent numerical diagonalization | conversion from conditional `r` to `Q` | yes |

Historical PR numbers and failed campaign summaries are not used as
load-bearing witnesses.

### N5 — Rhetoric audit

The repair tests aggregate channel-energy relations only. It does not claim a
per-component, per-site, full-lattice, or dynamics-level no-go. The statement
that the former `rho` map does not derive `r` is restricted to the displayed
partition/kernel values alone; it does not rule out a future microscopic
measure or action theorem.

### N6 — Partial-closure path scan

The residual changes the conditional value of `Q`, so it is not a naming
convention. A future retained derivation from a concrete Admissibility rule or
dynamics could close it. Explicit owner approval plus a reviewed registry
update is another governance path for a proposed primitive, but no such
approval is inferred here. Existing registered primitives are not counted as
walls and do not supply the missing condition.

### N7 — Steelman

A concrete realization of the Admissibility rule, record-production dynamics,
or a physical readout/action bridge could distinguish the two aggregate horns.
The current runner does not test those routes and does not construct full
lattice models. That is a strong objection to any universal independence or
no-go wording, which is why the claim is limited to source-text nonselection
and compatibility on the explicitly enumerated local surface.

### N8 — Cross-cycle echo

Similar structural gaps have sometimes been resolved by explicit primitive
approval, as with kinetic isotropy, or clarified by a primitive that narrows
what may be evaluated, as with the realized-state interface. Those mechanisms
are considered here: the proposed condition is absent from the registry and
the realized-state primitive does not supply it. Historical admission language
is not reused because no admission premise class exists.

**No-Go Discipline result:** `PASS` for the narrow current-surface
nonselection boundary. The result would be `FAIL` for a universal claim that
`r=1/2` cannot be derived by future dynamics, Admissibility, or readout work;
this note makes no such claim.

## What this note does not claim

- no derivation or adoption of `r=1/2`;
- no componentwise fixed-basis equipartition law;
- no formal independence theorem for the full minimal-axiom model class;
- no physical charged-lepton mass prediction or spectrum-to-mass bridge;
- no inference from the partition-cell ratio to an `r` ratio;
- no new axiom, approved primitive, probability rule, or audit verdict.

## Reproduction ledger

The runner independently checks the circulant trace dictionary, the orbit
partition, both aggregate solution sets and symmetries, exhaustive finite
additivity, the Gaussian moments in Cartesian and polar coordinates,
multiplicative normalization cancellation, the two conditional endpoints, a
wrong-count discriminator, a parity-table mutant, the four decoupled
integral/kernel cells, and the report-only PDG arithmetic.

**No-promotion statement:** effective status remains pipeline-derived after
independent audit and dependency closure.
