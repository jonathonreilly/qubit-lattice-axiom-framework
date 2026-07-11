# Record Additivity Does Not Fix the R-eta Unit Calibration

**Date:** 2026-07-04; countermodel repair 2026-07-11
**Type:** no_go
**Claim type:** no_go
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.py`](../scripts/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.txt`](../logs/runner-cache/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.txt)

## Narrow no-go claim

Grant the R-eta h-class hypothesis: a three-record charged-lepton cycle is to
be read through a fixed local scalar `h`. Even with that grant, the
[four axioms](MINIMAL_AXIOMS_2026-06-29.md) do not entail the identity
calibration

```text
Phi = 3h.
```

They admit a real one-parameter family of readouts

```text
I_beta(R) = beta h N(R),
```

where `N(R)` is the number of records in a finite pairwise-disjoint record
collection. Every real `beta` satisfies empty-zero, record-content
determination, and finite additivity. The target is `beta=1`; `beta=2` is an
explicit countermodel with the same axiom structure and the same granted `h`.

This is a no-go for the direct inference from Record additivity to the R-eta
h-unit. It is not a claim against a future same-observable holonomy theorem,
an owner-approved calibration convention, or a stronger physical readout law.

## Countermodel family

Keep the Lattice, Qubit, and Admissibility structures fixed. Let a state carry
finite-support records, each locking one admissible local possibility as the
Record axiom requires. For a finite record collection `R`, define `N(R)` as
its cardinality. Because cardinality depends on record content and not on a
site label, it is invariant under translations, proper cubic rotations, and
permutations of the three cycle positions.

For any real `beta`, set

```text
I_beta(empty) = 0,
I_beta(R disjoint-union S) = I_beta(R)+I_beta(S),
I_beta(R) = beta h N(R).
```

The first two equations follow directly from cardinality. For a three-record
cycle `C`,

```text
I_beta(C) = 3 beta h.
```

When `h=2/9` is granted, `beta=1` gives `2/3` and `beta=2` gives `4/3`.
Both models obey the stated axiom requirements. Therefore those requirements
do not entail `beta=1`.

The countermodel is real and hence even under complex conjugation. Adding a
K/CPT-evenness requirement does not remove the free coefficient.

## Scope

The result grants the h-class association for the sake of the argument. It
therefore proves a narrower and stronger residual statement than a joint
h-class/h-unit discussion: h-unit remains unentailed after h-class has been
supplied.

The result does not derive or refute the physical R-eta identification. It
does not set `h`, `delta`, `r`, or a charged-lepton mass, and it does not force
`r=1/2`. It changes no axiom, approved primitive, owner-governed premise,
registry, or audit verdict.

The live governance target is recorded in
`docs/audit/data/owner_governed_premise_nodes.json` as AC(ii), the R-eta
h-class/h-unit readout license. That registry identifies the target; it is not
used as a proof premise here.

## No-Go Discipline Gate

### N1 — alternative route enumeration

| Route tested against the countermodel | Marker | Result and authority/check |
|---|---|---|
| Record empty-zero | ATTEMPTED | `I_beta(empty)=0` for every real `beta`; Record clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Part A. |
| Record finite additivity | ATTEMPTED | Cardinality is additive on disjoint unions, so every `I_beta` is additive; Record clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Parts A and C. |
| Record-content determination | ATTEMPTED | `I_beta` depends on the finite record collection through `N(R)` and the granted scalar, with no site label; Record clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Part B. |
| Lattice and cycle symmetry | ATTEMPTED | `N(R)` is invariant under translations, proper cubic rotations, and cycle-position permutations; Lattice clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Part B. |
| K/CPT-even real readout | ATTEMPTED | Real `beta` and real `h` make `I_beta` unchanged by complex conjugation; this is an extra grant checked in runner Part B, not axiom content. |
| Pointwise realized-state evaluation | ATTEMPTED | Evaluating the same realized record state leaves the law-level coefficient `beta` free; [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) boundary plus runner Parts A–C. |

The runner checks all six routes. Their authority boundary is the current
minimal axiom memo plus the explicit family above; no prior negative row is
used as a witness.

### N2 — wall independence

The scoped claim carries one wall: `W_unit`, the coefficient `beta=1`.
h-class is granted, not counted as a second wall. No pairwise wall table is
needed after this collapse.

### N3 — hidden-wall scan

The proof text was scanned for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| granted h-class and `h` | explicit hypothesis that strengthens the countermodel |
| `registered` in the mass-coordinate and governance discussions | non-load-bearing route/target description |
| scan terms appearing in this checklist sentence | audit metadata, not proof steps |

No other scan hit is used in the proof.

### N4 — residual matching

No prior no-go row is cited as evidence.

| Prior negative witness | Witness residual | Current residual | Match/disposition |
|---|---|---|---|
| none | n/a | h-unit face of AC(ii): identity reading of the fixed local scalar as cycle angle | direct countermodel; no witness citation to drop |

### N5 — rhetoric and resolution audit

The countermodel is checked for the empty collection, a single record, finite
disjoint collections, a three-record cycle, and arbitrary finite cardinality.
It supports the statement that the named finite-record axioms do not entail
`beta=1`. It makes no claim about an added dynamical action, continuum limit,
or future same-observable theorem.

### N6 — partial-closure paths

| Candidate path | Current status | What it would address |
|---|---|---|
| owner-approved `beta=1` coordinate calibration | not approved as a separate convention | h-unit by governance ratification, not axiom derivation |
| same-observable determinant-line/holonomy theorem | no retained theorem on the current ledger surface | h-class and h-unit by physical derivation |
| `ACPHILAMBDA_R_ETA_VALUE_FACE_REGISTERED_ANGLE_FUNCTIONAL_EXACTNESS_RELOCATION_NOTE_2026-07-05.md` | unaudited source context | registered value face; does not identify the physical fixed-locus observable |

These paths remain compatible with the result. Neither is present in the four
axioms or the approved primitive registry. This note does not classify them as
impossible and does not propose a new primitive.

### N7 — steelman

The strongest objection is that angles are already measured in radians, so
`beta=1` may be a coordinate convention rather than new physics. That
objection succeeds after the fixed-locus scalar and the physical holonomy have
been proved to be the same observable in the same coordinate. The current
axioms name neither object and contain no such identity. Thus the objection
identifies a viable ratification or theorem path while leaving the present
non-entailment countermodel intact.

### N8 — cross-cycle echo

| Similar mechanism | Was its wall retired? | Applicability here |
|---|---|---|
| scale-reference primitive | calibration made explicit by owner approval | an analogous h-unit primitive would be a premise, not a derivation of `beta=1` |
| registered mass-coordinate reconstruction | phase reconstructed after state data are supplied | does not establish the h-unit identity for the physical fixed-locus observable |

Both mechanisms have been considered and do not refute the narrow
current-surface claim.

**Gate result: PASS.** N1–N8 support the finite-record, current-surface
non-entailment statement above.

## Verification

Run:

```bash
python3 scripts/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.py
```

Expected result: `PASS=35`, `FAIL=0`.
