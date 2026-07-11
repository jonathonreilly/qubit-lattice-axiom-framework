# Primitive Retirement Review After the Four-Axiom Reset

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-07-05
**Claim type:** meta
**Type:** meta
**Purpose:** primitive-retirement gate map
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, demote, or apply any audit verdict.
**Current-main posture (2026-07-11):** the approved scale-reference,
kinetic-isotropy, and realized-state primitives remain intact. This historical
retirement gate map neither changes them nor treats an open derivation
obligation as a premise.
**Primary runner:**
[`scripts/primitive_retirement_review_after_four_axiom_reset_2026_07_05.py`](../scripts/primitive_retirement_review_after_four_axiom_reset_2026_07_05.py)
**Cached runner output:**
[`logs/runner-cache/primitive_retirement_review_after_four_axiom_reset_2026_07_05.txt`](../logs/runner-cache/primitive_retirement_review_after_four_axiom_reset_2026_07_05.txt)

## Question

After the 2026-06-29 four-axiom reset and the 2026-07-02 through 2026-07-04
axiom clarifications, can any currently registered framework primitive be
retired from the premise surface?

The current registered premise surface is:

- `minimal_axioms`: Lattice, Qubit, Admissibility, and Record;
- `scale_reference_primitive`;
- `kinetic_isotropy_primitive`;
- `realized_state_primitive`.

## Verdict

No primitive is presently retireable from the updated axiom surface.

The updates sharpen the firewall around unfixed choices and state-blind laws,
but they do not supply any of the three registered primitive contents as
derived theorem content. No registry edit is warranted by this review.

| primitive | current verdict | reason |
| --- | --- | --- |
| `scale_reference_primitive` | keep | the four axioms still carry no dimensionful number; the scale note supplies only one units anchor and no dimensionless physics |
| `kinetic_isotropy_primitive` | keep, but targetable | the updated axioms do not supply a time-space metric swap, OS0/B-W normalization rule, realized strict tick, or single-tick normalization-placement theorem |
| `realized_state_primitive` | keep | the updated axioms now explicitly define states as record configurations and say laws privilege no states; that strengthens the separation between lawful evaluation and realized-state selection |

## Scale-Reference Primitive

The scale-reference primitive remains irreducible under the updated axioms.

The four axioms specify a structural lattice, site possibility algebra, local
admissibility, and fixed record readout. They still do not contain a
dimensionful number. The scale-reference source note declares exactly one
dimensionful reference, `a^{-1} = M_Pl`, as a units conversion only. It supplies
no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or
empirical fit, and it explicitly does not assert `a/l_P = 1` as a derived
theorem.

A future gravity self-consistency theorem may derive that the framework's
natural unit equals the Planck length. That would be important, but it would
not follow merely from the present four axioms. Until a retained derivation or
owner-approved reclassification exists, the single units anchor remains an
approved primitive rather than a retired theorem.

## Kinetic-Isotropy Primitive

Kinetic isotropy is the only serious future retirement lane among the three
registered primitives, but it does not retire now.

The new Lattice and Qubit no-privilege clauses, the Admissibility covariance
clause, and the Qualification sentence forbidding laws from depending on an
unfixed choice all improve the audit discipline around this primitive. They
rule out hidden coordinate choices and hidden law-level selectors. They do not,
however, add a time metric, a positive-transfer normalization rule, a
time-space exchange generator, or a realized strict-tick dynamics.

Existing kinetic support and no-go surfaces line up with that reading:

- the kinetic irreducibility support runner exhibits a family in which positive
  transfer, reflection positivity, single-clock product structure, and
  nearest-neighbor reachability all hold while `xi = c_t/c_s` varies;
- the `B4`/`S4` transitivity no-go shows that treating the four Euclidean axes
  as already time-space equivalent assumes the target equality;
- the B-W/OS0 interface no-go shows that unit real-time strict-tick slope does
  not by itself determine the Euclidean OS0 kinetic-form coefficient;
- the composition-closure note reduces part of the primitive to a
  single-tick normalization-placement reading, but explicitly states that the
  placement reading is not derived.

Thus the primitive can be targeted, but not removed. A genuine retirement route
would need retained-grade closure of the missing kinetic bridge stack: a
framework derivation of the realized one-tick carrier, the relevant unitary or
positive-transfer normalization, the B-W/OS0 readout rule in the same tick/edge
units, and the placement of the OS0 normalization at the single-tick kernel
rather than a composite kernel. A route based only on spatial cubic symmetry,
reflection positivity, square geometry, scale choice, or no-privilege wording
is insufficient.

## Realized-State Primitive

The realized-state primitive also remains irreducible.

The updated axiom memo says that a state is a configuration of records and that
a law privileges no states. That does not select a state; it makes state
selection more explicitly unavailable from law content alone. The Record
sentence "Records form" supplies occurrence, while the open-gates list still
leaves formation rules, weights, rates, update laws, and which admissible
possibility locks downstream.

The realized-state primitive supplies only the interface for pointwise
evaluation at the supplied law-admissible realized state. It supplies no state,
state-selection rule, measure, typicality or genericity assumption, weighting,
probability rule, preferred/default state, boundary condition, normalization
rule, or value. The support runner's small examples remain aligned with the
updated axiom text: state-blind laws can have different law-admissible realized
record trajectories, and invariant-state families need not contain a canonical
dynamically selected representative.

A future retirement would require a retained state-selection theorem or an
owner-approved change to the premise surface. Adding a typicality, measure,
past-hypothesis, or boundary-condition assumption would not retire this
primitive; it would introduce stronger downstream input.

## Hygiene Repairs Verified On 2026-07-10

The two narrative/tooling hygiene items originally recorded by this review are
now repaired, separately from any science reclassification:

- the three primitive source notes now cite the current four-axiom
  `minimal_axioms` surface without changing primitive content;
- `scripts/scale_reference_primitive_boundary_check.py` now pins the current
  Tier-A genuine-admitted-input count of zero after the theta and
  `AC_phi_lambda` retirements.

These completed hygiene repairs are not retirement evidence. They do not
justify changing `docs/audit/data/axiom_premise_nodes.json`.

## No-Go Discipline Gate

Gate result: PASS for the narrow registry-snapshot claim that the updated axiom
text does not presently retire any registered primitive. This is not a
universal no-go against future retirement.

**N1 alternative-route enumeration.** Eight distinct attacks were checked:

| route | marker | why it does not retire a primitive on the current surface |
|---|---|---|
| derive the scale from the four axioms by dimensional analysis | `ATTEMPTED` | [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) contains no dimensionful number; [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) still declares the single units anchor as supplied. |
| derive kinetic isotropy from spatial no-privilege and cubic symmetry | `ATTEMPTED` | the minimal-axiom text is spatial, while [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) explicitly says `c_t = c_s` is supplied rather than derived. |
| derive kinetic isotropy from reflection positivity or positive transfer | `ATTEMPTED` | the approved kinetic source says reflection positivity is not used as a derivation; the irreducibility note supplies a current support-only varying-`xi` witness, not audit authority. |
| derive kinetic isotropy from four-axis transitivity | `ATTEMPTED` | the approved kinetic source supplies only the target equality; the cited B4/S4 note records the circularity check as current unaudited support. |
| derive OS0 kinetic normalization from a unit real-time tick | `ATTEMPTED` | the approved kinetic source does not supply a B-W/OS0 readout bridge; the cited interface note records that residual as current unaudited support. |
| derive the realized state from the state/law qualification | `ATTEMPTED` | the minimal axioms say laws privilege no states, and [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) supplies pointwise evaluation without selecting a state. |
| derive the realized state from `Records form` | `ATTEMPTED` | occurrence does not choose which law-admissible record configuration is realized; the realized-state source keeps selection, weighting, and boundary data outside the primitive. |
| retire a primitive by removing its explicit approval and registry entry | `ATTEMPTED` | no such approval has been withdrawn; all three primitive source boundaries remain current. |

**N2 wall-independence audit.** The collapsed residual set has three distinct
contents:

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| dimensionful scale / kinetic-form ratio | no | no | yes |
| dimensionful scale / realized-state slot | no | no | yes |
| kinetic-form ratio / realized-state slot | no | no | yes |

No raw wall is downstream of another; the review does not inflate the count by
splitting subclauses of a single primitive.

**N3 hidden-wall scan.** Phrase hits are classified explicitly:

| phrase class | classification |
|---|---|
| `registered` / `canonical source-of-truth` | cited machine-registry authority for the current snapshot |
| primitive content described as `supplied` | cited primitive-source boundary, not an inferred theorem or hidden admission |
| future gravity, dynamics/metric, and state-selection routes | non-load-bearing open paths, not assumptions used to prove the snapshot |

Policy prose is not used as premise authority. The load-bearing snapshot reads
the axiom text, primitive source notes, and machine registry directly. The
support/no-go notes are labelled current unaudited route witnesses and are not
promoted into retained authority.

**N4 residual matching.** Every cited route witness is matched to the residual
it actually tests:

| cited surface | residual it tests | current residual | match / use |
|---|---|---|---|
| kinetic-isotropy irreducibility support | variable `xi = c_t/c_s` under positive-transfer support conditions | derivation of the kinetic-form ratio | yes; support-only witness |
| B4/S4 transitivity no-go | circular use of time-space transitivity | derivation of the kinetic-form ratio | yes; support-only witness |
| B-W/OS0 interface no-go | missing real-time-to-Euclidean normalization bridge | derivation of the kinetic-form ratio | yes; support-only witness |
| kinetic composition closure note | single-tick normalization-placement residual | one subroute toward the kinetic-form ratio | partial; route map only, not a witness for the whole claim |
| scale-reference source | dimensionful units anchor | scale primitive content | exact |
| realized-state source | supplied pointwise evaluation slot | realized-state primitive content | exact |

**N5 rhetoric audit.** The claim is only that the updated axiom text and
current registries do not presently retire these primitives. It is not a
lattice-wide impossibility theorem or a universal no-go against future
derivations, governance decisions, or registry updates.

**N6 partial-closure scan.** Kinetic isotropy has the clearest derivational
route through a retained dynamics/metric and normalization-placement theorem.
Scale could move through a gravity self-consistency theorem, and the
realized-state interface through a state-selection theorem. Explicit owner
governance could also retire an admission without pretending it was derived.
None of those paths is recorded as complete for a primitive on current main.

**N7 steelman.** The strongest counterargument is that the new no-privilege
state/law wording, spatial symmetry, reflection positivity, and unit-tick
normalization nearly assemble the kinetic and realized-state bridges, while a
gravity self-consistency result could make the units anchor redundant. That is
a plausible research program, but the current sources still mark the required
time-space normalization, dimensionful self-consistency, and state-selection
steps as separate. This snapshot therefore keeps the primitives while leaving
those routes open.

**N8 cross-cycle echo.** Theta has a retained-derivation disposition, while the
AC statements are open obligations. Neither affects the approved primitives:
current main records no withdrawal or retained derivation making the scale,
kinetic-isotropy, or realized-state primitive redundant.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
- [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md)
- [KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md](KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md)
- [KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md](KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md)
- [KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
- [AXIOM_MINIMALITY_POLICY.md](audit/AXIOM_MINIMALITY_POLICY.md)
- [axiom_premise_nodes.json](audit/data/axiom_premise_nodes.json)
- [tier_a_admissions.json](audit/data/tier_a_admissions.json)

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency, primitive, or registry row. The independent
audit lane is the only status authority.
