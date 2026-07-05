# Primitive Retirement Review After the Four-Axiom Reset

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-07-05
**Claim type:** meta
**Type:** review / primitive-retirement gate map
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, demote, or apply any audit verdict.
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

## Hygiene Debt Noted

This review found two narrative/tooling hygiene items that should be repaired
separately from any science reclassification:

- the three primitive source notes still contain some historical references to
  the older three-axiom baseline; they should be narrative-scrubbed to cite the
  current four-axiom `minimal_axioms` surface without changing primitive
  content;
- `scripts/scale_reference_primitive_boundary_check.py` still expects the old
  Tier-A genuine-admitted-input count of two, while the current registry has
  already retired theta and reports one remaining admitted target,
  `AC_phi_lambda`.

These are hygiene issues, not retirement evidence. They do not justify changing
`docs/audit/data/axiom_premise_nodes.json`.

## No-Go Discipline Gate

Gate result: PASS for the narrow review claim that none of the registered
primitives is presently retired by the updated axiom text.

- **N1 alternative routes:** scale retirement by dimensional analysis, kinetic
  retirement by no-privilege/symmetry/RP/B-W/unit-slope routes, and realized
  state retirement by the new state/law wording were checked. Each leaves the
  corresponding primitive content outside axiom-derived theorem content.
- **N2 wall independence:** the three primitives protect distinct surfaces:
  dimensionful units, dimensionless kinetic-form graining, and pointwise
  realized-state evaluation.
- **N3 hidden-wall scan:** the review does not use policy prose as premise
  authority. Load-bearing checks cite the axiom text, primitive source notes,
  machine registry, and existing support/no-go source notes.
- **N4 residual matching:** the residuals match the primitive notes' declared
  boundaries: units anchor, `c_t=c_s`, and supplied realized-state slot.
- **N5 rhetoric audit:** this is not a universal no-go against future
  primitive retirement. It is a current-surface review.
- **N6 partial-closure scan:** kinetic isotropy has the most plausible future
  retirement path, but current notes still name bridge and placement residuals.
- **N7 steelman:** a future retained dynamics/metric-layer theorem could derive
  kinetic isotropy and retire that primitive. A future gravity self-consistency
  theorem could alter the status of the scale anchor. A future state-selection
  theorem could alter the realized-state interface. No such retained closure is
  present on the current front door.
- **N8 cross-cycle echo:** theta retirement succeeded by retained derivation
  and owner-approved registry update. This review does not have an analogous
  retained derivation for any primitive.

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
