# Zero-Import Hydrogen: KS State-Law Two-Input Review Packet

**Date:** 2026-07-05
**Type:** grouped KS state-law review packet / adjacent parent-input bundling
**Status:** support-only. This packet does not ratify
`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`, does not ratify
`KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`, does not ratify
`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`, and does not derive
retained hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_ks_state_law_two_input_review_packet.py`

## Scope

This packet consolidates the two adjacent retained inputs that sit directly
under the KS-to-physical matter-state spinor-law lane:

```text
SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED
KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED
```

They are scientifically adjacent because the parent
`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED` handle needs both:
one input excludes the trivial scalar lift on the spinful staggered kernel
route, and the other supplies the physical faithful spin-lift action law for
the KS-reconstructed matter state.

The purpose is review compression only. A reviewer can inspect and, if
accepted, promote the two parent inputs as one grouped science unit without
requiring a chain of small PRs. This packet does not itself perform that
promotion. The two handles can be reviewed together because they are siblings
under the same KS state-law route handoff.

## Two-Input Bundle

| input handle | support stack already explicit | current live wall | downstream use |
|---|---|---|---|
| `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED` | carrier-attachment scalar-vs-spinful boundary, KS/chirality route support, route-defined `sigma.p` target, trivial scalar-lift covariance-failure target, grouped `sigma.p` child-handle review packet | `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`, `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`, owner ratification, and audit acceptance | supplies the scalar-lift exclusion input consumed by the KS-to-physical state-law route |
| `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED` | matter attachment to KS reduction, operator-frame/Pauli/Cl31 support, KS/Grassmann/chirality support, finite SU(2) double-cover and adjoint-blindness checks, grouped faithful-KS selector child-handle review packet | `FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED`, owner ratification, and audit acceptance | supplies the physical action-law input consumed by the KS-to-physical state-law route |

The individual target, decision, and current-surface packets remain the source
of truth:

```text
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md
```

The lower-level grouped review packets already carried on this branch are:

```text
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md
ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md
```

## What This Would Unlock

If both input handles are later retained, the parent KS route can spend them as
two inputs:

```text
SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED
KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED
  -> supports KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED
```

That parent KS state-law handle would still require its own text lock, fixed
support inputs, no-import guardrails, owner ratification, and audit acceptance.
It is not automatically retained by this packet.

After the KS route theorem is retained, the parent physical matter-state law
bridge still needs:

```text
PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED
```

The sibling elementary route remains separate:

```text
ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED
```

Therefore this bundle moves the KS child route closer to review, but it does
not reach the physical matter-state bridge, HW1, carrier context, R-eta
exactness, electron mass, alpha, or hydrogen.

## Current Open PR Alignment

| PR | queue signal | two-input effect |
|---|---|---|
| `#5016` zero-import hydrogen retained lane bundle | open; carries this packet once pushed | grouped review surface only |
| `#5033` reflection-positivity runner scope cleanup | open, audit-successful at refresh | audit-scope cleanup only; no KS state-law handoff |
| `#5030` multisite Pauli finite-carrier provenance | open, audit-successful at refresh | finite carrier-provenance context only |
| `#5014`, `#5017`, `#5018` chirality/domain-wall stack | open, audit-successful at refresh | chirality/domain-wall support; no retained KS state-law input |
| `#5021` primitive-retirement review | open draft, audit-successful at refresh | no primitive shortcut |
| `#5023`, `#5024`, `#5026`, `#5027` Koide W4/custody repairs | merged with audit success | adjacent hygiene/custody support only |

Open or green PR metadata is not proof input. It is queue context for which
science surfaces the reviewer may see at the same time.

## Review Compression Boundary

| possible overread | boundary |
|---|---|
| two input handles accepted together | would only provide two inputs to the parent KS state-law route |
| grouped `sigma.p` child-handle packet | support for the scalar-lift side, not scalar-lift exclusion closure |
| grouped faithful-KS selector child-handle packet | support for the action-law side, not action-law closure |
| parent KS route after both inputs | still needs parent owner/audit acceptance |
| physical matter-state bridge after parent KS route | still needs parent bridge fixed inputs and acceptance |
| hydrogen | still needs HW1, carrier context, R-eta, electron mass, alpha, and static-source Rydberg closure |

The approved primitive registry was checked. Registered primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. None is a
`spinful_staggered_kernel_scalar_lift_exclusion_primitive`,
`ks_spin_lift_physical_action_primitive`,
`ks_to_physical_matter_state_spinor_law_primitive`,
`physical_matter_state_law_primitive`, or `hydrogen_primitive`.

## No-Go Discipline Gate

Gate target: grouped current-surface non-supply and review-compression
boundary. The checked claim is:

```text
The current retained, primitive, merged-PR, and open-PR surfaces do not yet
supply the two KS state-law inputs as retained consequences, but the two
handles are adjacent enough to review as one KS state-law route bundle.
```

This gate does not say the two input handles are impossible.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| grouped two-input promotion | Accept both individual input contracts with owner/audit acceptance. | OPEN POSITIVE ROUTE. This would supply both inputs, but this packet does not perform acceptance. |
| scalar-lift side only | Accept `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED` alone. | PARTIAL ONLY. It excludes the scalar lift but does not supply the physical KS action law. |
| action-law side only | Accept `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED` alone. | PARTIAL ONLY. It supplies the state action law but does not exclude the scalar-lift sibling. |
| parent KS state-law route | Treat the two input packets as parent KS theorem closure. | ATTEMPTED. Parent text lock, support inputs, guardrails, owner, and audit remain separate. |
| child-bundle shortcut | Treat the grouped `sigma.p` or faithful-KS selector packets as the parent inputs. | ATTEMPTED. They are lower-level review surfaces only. |
| chirality/domain-wall route | Treat #5014/#5017/#5018 as these inputs. | ATTEMPTED. They are support context only. |
| multisite Pauli provenance route | Treat #5030 as state-law or scalar-lift closure. | ATTEMPTED. It is finite carrier-provenance context only. |
| primitive shortcut | Spend an approved primitive. | ATTEMPTED. Registry check found no such primitive. |

### N2 - Wall-Independence Audit

The grouped live wall set is:

```text
OWNER_RATIFICATION for the scalar-lift exclusion input
AUDIT_ACCEPTANCE for the scalar-lift exclusion input
OWNER_RATIFICATION for the KS spin-lift physical action-law input
AUDIT_ACCEPTANCE for the KS spin-lift physical action-law input
```

Each input also has its own lower-level physics dependencies. The `sigma.p`
child bundle can help the scalar-lift side, and the faithful-KS selector child
bundle can help the action-law side, but neither automatically closes its
parent input. Accepting one parent input does not automatically accept the
other, and neither owner decision automatically supplies independent audit
acceptance.

### N3 - Hidden-Wall Scan

Phrases checked: `accepted`, `support`, `finite`, `KS`, `Grassmann`,
`chirality`, `sigma.p`, `scalar`, `faithful`, `SU(2)`, `state-law`, `open PR`,
`merged PR`, `registered`, and `primitive`. They are status or support words
only. The packet does not convert them into retained inputs, parent KS route
closure, parent physical bridge closure, or hydrogen input.

### N4 - Residual Matching

| witness | residual it attacks | residual here | match? |
|---|---|---|---|
| scalar-lift exclusion packet | needs route-defined spinful kernel plus trivial-scalar covariance failure | scalar-lift input remains open | yes |
| action-law packet | needs faithful KS state-action selector plus acceptance | action-law input remains open | yes |
| grouped `sigma.p` two-handle packet | groups child handles under the scalar-lift side | scalar-lift parent input remains open | yes |
| grouped faithful-KS selector packet | groups child handles under the action-law side | action-law parent input remains open | yes |
| KS state-law target packet | consumes both parent inputs if retained | parent KS route remains open | yes |
| physical matter-state bridge packet | consumes the KS route theorem if retained | parent bridge remains open | yes |

### N5 - Rhetoric Audit

The negative claim is scoped to current non-supply of the two parent inputs and
the downstream nonclosure boundary. It does not say the KS route fails, that
spinful scalar-lift exclusion is unavailable, or that faithful spin action is
unavailable.

### N6 - Partial-Closure Path Scan

| candidate path | what it would close |
|---|---|
| owner/audit acceptance of spinful staggered kernel scalar-lift exclusion | `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED` |
| owner/audit acceptance of KS spin-lift physical action law | `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED` |
| parent KS state-law acceptance after both inputs | `KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED` |
| physical matter-state bridge acceptance after retained KS route or elementary route | `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED` |
| HW1/carrier/R-eta route after parent bridge | downstream K2 physical generation and readout support |

### N7 - Steelman

A strong reviewer could argue that the two parent inputs should be accepted
together now: the scalar-lift side has carrier-attachment and `sigma.p` route
support, while the action-law side has finite SU(2), adjoint-center, and
faithful-KS selector support. This packet preserves that positive reading by
grouping the review target. It does not mark the handles retained because
owner/audit acceptance must happen at the exact parent-input handles.

### N8 - Cross-Cycle Echo

This repeats the repo's support-vs-retained-handoff rule: strong finite and
route support can make a compact review unit, but it becomes spendable only
after the retained handle is explicit, owner-accepted, and audit-accepted.
That is the same rule used by the scalar-lift, action-law, KS child, physical
matter-state bridge, and hydrogen packets.

**Gate result:** broad KS state-law or route-closure claim fails; grouped
two-input review packet passes as a scoped support and review-compression
artifact.

## Explicit Non-Claims

- No derivation or ratification of
  `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.
- No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.
- No derivation or ratification of
  `KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.
- No derivation or ratification of
  `FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED`.
- No derivation or ratification of
  `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.
- No derivation or ratification of
  `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.
- No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.
- No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.
- No derivation or ratification of
  `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.
- No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.
- No R-eta, h-class, h-unit, K1/K2/K3/K4, Koide electron readout, `m_e`,
  `alpha(0)`, static-source Rydberg closure, or retained hydrogen consequence.
- No new axiom, primitive, Tier-A admission, empirical import, or audit status
  is introduced.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_r_eta_ks_state_law_two_input_review_packet.py
```

The verifier checks the grouped review boundary, parent-input nonclosure,
KS state-law dependency logic, primitive-registry boundary, and explicit
hydrogen non-claims.
