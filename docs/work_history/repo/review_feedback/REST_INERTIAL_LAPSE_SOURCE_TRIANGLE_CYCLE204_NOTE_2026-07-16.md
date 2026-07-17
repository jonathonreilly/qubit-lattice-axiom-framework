# Rest–inertial–lapse–source triangle — Cycle 204

Date: 2026-07-16

Status: source-grade conditional algebra plus deterministic finite trajectory
and field probes; audit unset; `partial-attempt-with-named-untested-routes`

Authority: none

Companion runner:
`scripts/rest_inertial_lapse_source_triangle_cycle204_2026_07_16.py`

This note and runner live only on the draft parking branch and draft PR #5389.
They change no foundation, axiom, primitive, registry, policy, audit, or queue
surface.

## Result up front

Cycles 201–203 supplied an operational inertial mass. Cycle 9 supplied a
conditional local Green field and common scalar lapse. Cycle 204 connects
those surfaces without calling the connection derived.

If a weak lapse `q(x)=1+Phi(x)` multiplies a rest generator, then a localized
positive-energy sector has potential

```text
V(x) = M_passive Phi(x),
```

where the passive charge is the sector's rest phase or rest energy under the
chosen operational clock map. If its independently measured inertial mass is
`M_inertial`, a weak uniform gradient gives

```text
acceleration / gravitational_gradient = M_passive / M_inertial.
```

Universal free fall therefore requires one universal ratio. Equality of the
two masses is the unit-normalized case. This is a conditional response theorem
of the common-lapse clause, not a derivation of that clause.

The finite results divide the live candidates sharply:

- For the finite-range Dirac Hamiltonian generator, rest energy and inertial
  mass are both `m`. Three independently evolved packets with `m=0.25,0.4,
  0.65` accelerate at the supplied gravitational gradient to within `0.24%`.
- For the strict paired-Weyl QCA under standard lattice coordinates, rest
  quasienergy is `asin(m)` while inertia is `m/sqrt(1-m^2)`. The predicted and
  measured passive/inertial ratios are approximately `0.979`, `0.943`, and
  `0.827`. The finite-lattice response is species dependent under that exact
  coordinate package, while the difference vanishes quadratically toward the
  small-`m` continuum.
- For the nonrelativistic bound composite, a common onsite energy
  normalization can make one chosen interaction sector satisfy rest/inertial
  equality, but not all five tested binding strengths. Sector-specific
  offsets can tune them individually, which demonstrates a live algebraic
  escape but supplies the desired answer by species.

This does not rule out the QCA, bound matter, or emergent gravity. It identifies
the exact clock/energy normalization that each route must derive rather than
hide.

## Passive response is now operational

The runner does not infer acceleration from the dispersion formula. It reuses
Cycle 202's localized two-component packets and applies an onsite phase
gradient whose strength is

```text
force = rest_charge * gravitational_gradient.
```

It then fits the packet trajectory. The results are:

| route | `m` | predicted `M_passive/M_inertial` | measured `a/g` |
|---|---:|---:|---:|
| Dirac generator | 0.25 | 1.0000 | 1.0024 |
| Dirac generator | 0.40 | 1.0000 | 0.9988 |
| Dirac generator | 0.65 | 1.0000 | 0.9985 |
| strict QCA | 0.25 | 0.9786 | 0.9808 |
| strict QCA | 0.40 | 0.9429 | 0.9422 |
| strict QCA | 0.65 | 0.8273 | 0.8268 |

These are weak local-lapse trajectories, not a curved-spacetime simulation.
More precisely, the trajectory implements the leading adiabatic rest-sector
potential of a slowly varying lapse. It does not implement or select the
Hermitian ordering of a fully position-dependent Hamiltonian scheduler, or a
strict inhomogeneous QCA rule that rescales both kinetic and rest terms. The
external gradient remains supplied and the same finite-range-versus-strict-
update distinction from Cycles 201–202 remains.

## The QCA clock-map escape is real

For the QCA, define the nonlinear operational energy

```text
E_op(omega) = tan(omega).
```

At rest this gives

```text
tan[asin(m)] = m/sqrt(1-m^2) = M_inertial.
```

So one-particle equality can be restored without changing the QCA update.
That is why no QCA no-go is licensed. But the map is not additive under
ordinary phase composition:

```text
tan(omega_1+omega_2) != tan(omega_1)+tan(omega_2).
```

A physical use of this escape must derive its composition law, clock readout,
and multiparticle meaning. Merely choosing `tan` because it gives equality
would relocate rather than close the problem.

## The bound-composite normalization escape

For the Cycle-203 contact pair,

```text
rest gap       = 2 mu - sqrt(U^2+16J^2),
inertial mass  = sqrt(U^2+16J^2)/(4J^2).
```

With `J=0.5`, choose one common `mu` so the `U=1` sector has unit ratio. The
passive/inertial ratios for `U=(0.4,0.7,1,1.5,2)` are then approximately

```text
(1.193, 1.111, 1.000, 0.789, 0.581).
```

Choosing a different `mu(U)` for every sector makes each ratio one, but that
is sector-specific input. A relativistic interaction or a derived universal
vacuum normalization remains a live way to make the equality structural.

## Active source map

Cycle 9 derives a local stationary Green field from a maintained source
current, but explicitly leaves the physical mass-to-current map open. Cycle
204 compares two maps without promoting either:

```text
energy comparator:   source current proportional to operational rest energy;
archive comparator:  source current proportional to permanent record count.
```

The energy comparator makes the finite Green amplitude scale linearly with
the candidate source mass, adds under independent co-located sources, and is
unchanged by adding decoupled witness registers. It would close the active
side of the triangle if the microscopic law generated it.

Archive count fails the redundancy control in this tested source map: adding
two spectator witnesses triples the field even though Cycles 201–203 show no
change in inertia. Conversely, one archive count gives the same field to two
different candidate masses. This is a finite linear-source comparator result,
not a theorem against every history-, flux-, stress-, or record-derived
source law.

The active source map remains supplied. Calling the energy comparator
`T_00`, commit current, or stress does not derive its coefficient or show that
the record process generates it.

## What joins, conditionally

Under three explicit conditions,

1. the operational rest coordinate equals the independently measured inertial
   coordinate;
2. maintained source current is proportional to that same coordinate; and
3. one common local field/lapse couples to the full matter generator,

the scalar candidate gives

```text
source amplitude proportional to M_source,
probe force proportional to M_probe,
probe acceleration independent of M_probe.
```

The Dirac-generator candidate realizes condition 1 on its free sector.
Cycle 9 realizes the local field, attractive scalar sign, and finite-gap
universality conditional on conditions 2–3. No current construction derives
all three inside one microscopic law. The mass-to-gravity map remains
conditional.

## Cross-lane effect

### O — operational quantum

The passive response is computed from coherent packet trajectories with
generic complex phases. Complete records still have not been shown sufficient
to reconstruct the future packet state. The Cycle-200 equal-record-fibre test
remains the direct ontology discriminator.

### T — time

The clock map is now experimentally load-bearing. `omega`, `tan(omega)`, and a
Hamiltonian energy cannot be treated as interchangeable conventions because
they predict different finite-lattice free fall and different composition
rules. A successful time theorem must select the physical map through clocks
and composition.

### I — matter

The Dirac-generator free sector has an exact rest/inertial/passive equality,
and the contact pair has binding plus inertial response. The two results do
not yet coexist in one relativistic interacting object. That combined object
is now a concrete construction target rather than an undefined “mass” gap.

### G — gravity

The campaign now has an operational passive-mass test, a redundancy-safe
candidate active source map, a local cubic Green field, an attractive scalar
sign, and an exact statement of when probe mass cancels from acceleration.
Still open are derivation of the source and common coupling, reversible
microphysics, spatial/tensor response, light bending, self-coupling, and a GR
continuum limit.

### B — boundary

The maintained resource source/sink, matter packet, mass sector, and external
gradient remain prepared inputs. Cycle 10's closed-current work relocates the
reservoir to a supplied nonequilibrium affinity; it does not select the
cosmological boundary or source population.

## No-Go Discipline Gate

Gate result: **FAIL for any broad impossibility claim; artifact demoted to
`partial-attempt-with-named-untested-routes`.** This is the intended safety
result. The tested packages are discriminated, but live alternative clock,
interaction, source, and tensor routes prevent a broad no-go.

### N1 — Alternative route enumeration

The candidate broad claim would be “the present substrate cannot close one
mass across rest, inertia, and gravity.” It is not licensed.

| route | marker | result against the broad claim |
|---|---|---|
| finite-range Dirac generator + common lapse | `ATTEMPTED` | conditional success: rest, inertia, and passive response share `m` in the tested free sector (Cycles 201, 202, and this runner) |
| strict QCA + standard phase energy | `ATTEMPTED` | finite-spacing mismatch, matching the algebraic shape already exposed for a retained free two-step band in `MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md` |
| strict QCA + nonlinear `tan(omega)` energy | `ATTEMPTED` | one-particle equality succeeds; ordinary additive composition does not, leaving a live deformed-composition route |
| strict QCA continuum limit | `ATTEMPTED` | mismatch vanishes quadratically, so finite mismatch does not foreclose continuum equivalence |
| contact composite + one common vacuum offset | `ATTEMPTED` | equality holds for one tuned sector but not the other four tested interactions |
| contact composite + sector-specific offsets | `ATTEMPTED` | algebraic equality succeeds but the sector-dependent input is not derived |
| energy-current source versus archive-count source | `ATTEMPTED` | energy source passes mass scaling and record redundancy conditionally; archive count fails those finite controls |

There are more than five distinct routes, and at least three are conditional
successes. Moreover, none of the new Cycle-201–204 draft surfaces is retained
authority. Those facts themselves prohibit a broad no-go.

### N2 — Wall-independence audit

After collapsing downstream phrasings, the triangle has three independent
conditions:

- `E`: operational rest/energy normalization equals the inertial coordinate;
- `S`: active source current is generated from that same coordinate; and
- `F`: one physical field law couples commonly to matter and supplies its
  spatial/tensor completion.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `E,S` | no | no | yes |
| `E,F` | no | no | yes |
| `S,F` | no | no | yes |

Vacuum offset and QCA clock-map language are part of `E`, not extra walls.
Commit-current naming and mass normalization are part of `S`. Lensing,
nonlinear response, and reversible field microphysics are downstream parts of
`F`, not inflated into independent mass-triangle conditions here.

### N3 — Hidden-wall scan

The note was searched for the gate phrases. “Conditional,” “supplied,” and
“prepared” clauses name `E`, `S`, or `F` explicitly. “Standard lattice
coordinates” names the tested QCA coordinate package rather than an
unacknowledged physical identification. “Common lapse” is candidate-law
condition `F`. No “obvious,” “naturally,” “standard QFT,” “framework
provides,” “registered,” or “canonical” phrase is load bearing. The record
and energy factors used in source comparisons are labelled comparators, not
derived observables.

### N4 — Residual matching

| witness | witness residual | residual used here | match? |
|---|---|---|---:|
| `MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md:42,55-59,75` | retained bounded rest-gap/curvature relation on a supplied free two-step band; no acceleration or gravity | analogous finite-spacing energy/curvature distinction only | yes, narrow algebraic analogy; not trajectory authority |
| `EQUIVALENCE_PRINCIPLE_NOTE.md:41-42,77-78` | meta retraction and open mass-equality derivation gap | packaging target and explicit missing source/response normalization | yes as meta boundary, not positive authority |
| `OPERATIONAL_MASS_COORDINATE_TOURNAMENT_CYCLE201_NOTE_2026-07-16.md:44-46,68,170-171` | draft rest/curvature coordinates | condition `E` inputs | yes; draft only |
| `LOCAL_FORCE_INERTIAL_MASS_BRIDGE_CYCLE202_NOTE_2026-07-16.md:19,48-56,103-104` | draft force/acceleration mass | operational inertia input | yes; draft only |
| `LOCALLY_BOUND_COMPOSITE_MASS_BRIDGE_CYCLE203_NOTE_2026-07-16.md:31-41,166-172` | draft bound-pair inertia and free rest offset | composite part of `E` | yes; draft only |
| `LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md:25,71-74,283,311,347` | draft local field/common lapse with open mass-to-current map | conditions `S` and `F` | yes; draft only |

No spin-2 exchange, historical beam-fit, or unrelated source-normalization
claim is used as support.

### N5 — Rhetoric audit

- “Archive count fails the redundancy control” is proved only for a finite
  linear source proportional to count, at the whole candidate-object field
  amplitude. It is not claimed for every per-event, flux, stress, history, or
  lattice-wide record-derived source law.
- “Standard-QCA response is not universal” is restricted to one positive
  paired-Weyl band, three finite masses, the standard phase/momentum reading,
  and one scalar lapse coupling. Other modes, blocks, energy maps, and
  multiparticle laws are not covered.
- “One common offset does not match the composites” covers five contact-pair
  sectors at fixed `J`. It is not a statement about all relativistic bound
  states or vacuum constructions.

All broader forms are expressly left untested, so the negative wording is
kept at the demonstrated per-band/per-comparator resolution.

### N6 — Partial-closure path scan

The live import-retirement paths are concrete:

1. derive a QCA operational energy and composition law; this could promote
   the `tan(omega)` escape from a fitted redefinition to a theorem;
2. derive a common physical vacuum normalization for interacting sectors;
   if it is genuinely a universal convention rather than species-dependent
   physics, its ratification is an import-retirement path, not a new axiom;
3. place the energy-current source comparator as an explicit condition in a
   bounded theorem, then test whether a deeper local law generates it; and
4. extend Cycle 9/10's local resource process so its source is the matter
   energy ledger and its scheduler acts on the same generated object.

The current open-PR scan found PR #5440 on defined electroweak mass algebra;
it does not close this operational source/response residual. Draft PR #5389 is
this parking campaign. No axiom change is inferred or requested.

### N7 — Steelman

A hostile reviewer should reject any no-go here: a reversible interacting QCA
may derive a deformed but associative energy-composition law whose one-body
readout is `tan(omega)`; a relativistic lattice interaction may make binding
energy contribute to both rest and inertia with no species offset; and the
conserved stress of that same law may source an emergent tensor field rather
than Cycle 9's scalar scheduler. Cycle 10 already shows how a seemingly
dissipative local step can acquire a unitary dilation when carrier scope is
enlarged. None of those routes is excluded. This steelman is decisive, so the
broad no-go fails and the result remains a conditional route discriminator.

### N8 — Cross-cycle echo

Cycle 9 is the key positive warning: an earlier nonlocal Poisson inverse became
a fixed-point theorem after a deeper local diffusion law was supplied. The
same mechanism could retire `E`, `S`, or `F`. Cycle 10 likewise turns a
one-step dissipative objection into a finite unitary dilation, while exposing
the all-time environment cost. The retained two-step mass note narrows a
rest/curvature mismatch without mistaking it for a physical inertia no-go;
Cycle 202 then closes the missing trajectory test on a different candidate.
The old equivalence-principle note was correctly demoted after unsupported
beam fits. This cycle repairs the force observable and inertial extraction but
does not pretend that the active-source and shared-action theorems have also
landed.

The cross-cycle lesson is to keep all three conditions as theorem imports and
attack their retirement through a deeper common law, not constitutional prose.

## Next construction

Two routes now dominate:

1. build a relativistic locally bound object whose rest energy, curvature,
   forced inertia, and binding ledger agree without a sector-specific offset;
2. make that ledger drive Cycle 9/10's local source current and then evolve a
   second object in the generated field, separating active and passive tests.

In parallel, the `tan(omega)` QCA route deserves a composition tournament:
does a local multiparticle/quasienergy law generate that nonlinear coordinate,
or does it require species/protocol lookup?

## Scope boundary

This is a leading-rest-sector conditional scalar weak-field mass triangle. It is not a retained
equivalence principle, gravitational source theorem, tensor metric,
self-gravity, light-bending result, empirical mass test, or GR limit. The
active source map remains supplied, the common coupling remains supplied, and
the rest-energy normalization is selected only in the Hamiltonian free
candidate. It makes no broad no-go or minimum-content claim and supports no
axiom conclusion.
