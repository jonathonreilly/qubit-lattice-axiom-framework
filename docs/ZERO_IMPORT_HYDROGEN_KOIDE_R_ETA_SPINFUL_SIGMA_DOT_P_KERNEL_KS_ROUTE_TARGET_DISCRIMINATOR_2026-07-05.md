# Koide R-Eta Spinful Sigma-Dot-P Kernel KS Route Target Discriminator

Date: 2026-07-05

**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_spinful_sigma_dot_p_kernel_ks_route.py`

Purpose: isolate the route-defined spinful `sigma.p` kernel subinput under the
spinful staggered kernel scalar-lift exclusion lane. This discriminator does
not derive or ratify
`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`, does not derive
`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`, does not derive
`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`, and does not
calculate retained hydrogen.

## Target

The target handoff is:

```text
SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED
```

Meaning: on the Kawamoto-Smit / staggered route, the spinful `sigma.p`
operator candidate is specified as the route object to be tested by the later
scalar-lift covariance-exclusion lane. It is a kernel-object handoff only. It
is not the scalar-lift exclusion theorem, not the KS physical spin-lift action
law, and not a physical matter-state law.

## Retention Contract

`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED` requires all of the
following inputs:

```text
SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TEXT_LOCK
SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED
SCALAR_KERNEL_COMPATIBILITY_ACCEPTED
STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED
KS_PHASE_FORCING_SURFACE_ACCEPTED
KINETIC_TWO_RAY_SURFACE_ACCEPTED
FINITE_SIGMA_DOT_P_NONCENTRALITY_CHECK
KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED
KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED
NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT
NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT
NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT
NO_KS_ROUTE_CLOSURE_INPUT
NO_PARENT_BRIDGE_OR_HW1_INPUT
NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT
NO_K1_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If the contract passes, the only retained consequence is:

```text
SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED
```

That consequence may feed the scalar-lift exclusion lane as one subinput, but
it cannot close `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`
without `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`, owner
ratification, and audit acceptance.

## Input Roles

| Input | Role |
|---|---|
| `SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TEXT_LOCK` | fixes this lane as the KS-route kernel-object handoff, not scalar-lift exclusion |
| `SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED` | consumes the source no-go that operator-frame/Clifford data do not force per-site `C^2` matter-state law |
| `SCALAR_KERNEL_COMPATIBILITY_ACCEPTED` | records that the spin-blind scalar kernel remains compatible with the trivial scalar lift |
| `STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED` | records the staggered/Kawamoto-Smit route as the live place where a spinful selector can enter |
| `KS_PHASE_FORCING_SURFACE_ACCEPTED` | consumes bounded KS phase/gauge-class support at its declared scope |
| `KINETIC_TWO_RAY_SURFACE_ACCEPTED` | consumes scalar-ray/Dirac-ray support while preserving the open selector residual |
| `FINITE_SIGMA_DOT_P_NONCENTRALITY_CHECK` | records the finite Pauli witness that `sigma.p` is noncentral and spinful |
| `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED` | supplies the retained route-defined momentum/link-phase input needed to name `p` on the KS route |
| `KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED` | supplies the retained theorem that the route object is exactly the spinful `sigma.p` kernel |
| `NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT` | prevents this lane from importing the sibling scalar-lift covariance-failure theorem |
| `NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT` | prevents this lane from importing the parent scalar-lift exclusion handoff |
| `NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT` | prevents this lane from spending the KS physical spin-lift action law |
| `NO_KS_ROUTE_CLOSURE_INPUT` | prevents importing the full KS child theorem as a premise |
| `NO_PARENT_BRIDGE_OR_HW1_INPUT` | prevents importing the parent state-law bridge, HW1 locus, carrier, or hydrogen as a premise |
| `NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT` | prevents importing Koide value/angle outputs |
| `NO_K1_K3_K4_OR_MASS_INPUT` | prevents importing electron-readout or mass-route closure |
| `NO_COMPARATOR_PROOF_INPUT` | prevents importing observed mass/hydrogen comparator matches |
| `NO_NEW_PRIMITIVE_OR_AXIOM` | prevents a silent primitive or axiom shortcut |
| `OWNER_RATIFICATION` | owner accepts this as the intended route-kernel handoff |
| `AUDIT_ACCEPTANCE` | independent audit accepts the retained consequence |

## Current Surface

| Surface | What it supplies | What it does not supply |
|---|---|---|
| `CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md` | refutes the spinor-module escape; records scalar-kernel compatibility and identifies spinful `sigma.p` as the displayed selector that excludes the scalar | retained KS-route kernel-object theorem |
| `scripts/carrier_attachment_chirality_gate_consolidation_runner.py` | finite checks for scalar-kernel compatibility and spinful `sigma.p` noncentrality | owner/audit-retained route-defined kernel handoff |
| `KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md` | localizes matter attachment to KS/state-law or elementary state-law route | KS-route kernel-object theorem |
| `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md` | bounded KS phase/gauge-class support inside the declared kinetic class | retained `sigma.p` kernel-object handoff |
| `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` | two-flux-class and scalar/Dirac-ray support with named residuals | retained choice of the spinful `sigma.p` ray as the route kernel |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md` | records open #5011 as eta/Kawamoto-Smit covariant-walk context | no retained spinful `sigma.p` KS-route kernel theorem |
| `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` | bounded synthesis context with explicit residuals | unbounded physical state-action theorem or this retained kernel handoff |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md` | child target that can supply `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED` if retained | spinful kernel-object theorem, this target, or scalar-lift exclusion |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_RATIFICATION_DECISION_PACKET_2026-07-05.md` | owner/audit contract for the route momentum/link-phase input | decision acceptance here |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | records current non-supply of the route momentum/link-phase input | retained `sigma.p` kernel theorem |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_TARGET_DISCRIMINATOR_2026-07-05.md` | child target that can supply `KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED` if retained | route momentum/link phase, this target, or scalar-lift exclusion |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RATIFICATION_DECISION_PACKET_2026-07-05.md` | owner/audit contract for the KS-route spinful kernel-object theorem | decision acceptance here |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_CURRENT_SURFACE_NO_GO_2026-07-05.md` | records current non-supply of the spinful kernel-object theorem | retained `sigma.p` route handoff |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md` | parent scalar-lift target that consumes this lane if retained | route-defined spinful kernel theorem itself |

The current retained, primitive, merged-PR, and open-PR surfaces therefore do
not supply `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`. This
target remains a live positive route, not a closed no-go.

The approved primitive registry was checked. Registered primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. None is a
`ks_route_momentum_link_phase_primitive`,
`spinful_sigma_dot_p_kernel_primitive`,
`spinful_staggered_kernel_primitive`, `scalar_lift_exclusion_primitive`,
`ks_to_physical_matter_state_spinor_law_primitive`, or `hydrogen_primitive`.

## Open And Merged PR Alignment

PRs were refreshed on 2026-07-05 UTC. Lane-relevant PRs are queue/status
signals; clean/dirty/check labels are not proof inputs.

| PR | queue signal | sigma-dot-p KS-route effect |
|---|---|---|
| open `#5016` zero-import hydrogen retained lane bundle | carries this lane and the child momentum/link-phase lane once pushed | not landed authority while open |
| open `#5026` Koide custody L4 retained-successor re-point | charged-lepton custody citation repair | no route-defined spinful KS kernel theorem |
| merged `#5019` AC_phi_lambda decomposition chain | Koide form-layer rebase | no route-defined spinful KS kernel theorem |
| merged `#5020` AC_phi_lambda value face | value-face/exactness relocation | no route-defined spinful KS kernel theorem |
| merged `#5022` delta-eta chain repair | supplied-premise and K-orbit form authority | no route-defined spinful KS kernel theorem |
| merged `#5023` Koide W4 audit-readiness repairs | record/species/custody/hw-complement hygiene | no route-defined spinful KS kernel theorem |
| merged `#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | gate-readiness and audit-graph hygiene | no route-defined spinful KS kernel theorem |
| open `#5021` primitive-retirement review | draft meta map; no retirements | no primitive shortcut |
| open `#5011` eta twisted walk family runner repair | eta/Kawamoto-Smit covariant-walk context via `ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md` | no route-defined spinful KS kernel theorem |
| open `#5014` record-formation front domain wall | formation-front/domain-wall support | no route-defined spinful KS kernel theorem |
| open `#5017` domain-wall edge anomaly inflow spectral flow | anomaly-flow support | no route-defined spinful KS kernel theorem |
| open `#5018` domain-wall edge content vs SM chiral map | chirality/domain-wall map with named gaps | no route-defined spinful KS kernel theorem |

## No-Go Discipline Gate

Gate target: narrow current-surface non-supply only. The claim checked here is
that the current retained, primitive, merged-PR, and open-PR surfaces do not
supply `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`. The gate
does not assert that this route-defined kernel can never be supplied.

### N1 - Alternative Route Enumeration

| Route | Attempt | Result |
|---|---|---|
| full sigma-dot-p KS-route contract | Accept all fixed/support inputs plus the retained route-defined momentum/link-phase input, retained spinful kernel-object theorem, and owner/audit acceptance. | OPEN POSITIVE ROUTE. This would close the target, but the missing inputs are not supplied here. |
| carrier-attachment source route | Treat the carrier-attachment sharpening note as the retained route-defined kernel theorem. | ATTEMPTED. It names the spinful selector and support boundary, but it does not prove the KS/Grassmann physical-state-law bridge or ratify this route object. |
| finite runner route | Treat the existing finite `sigma.p` matrix check as audit-retained closure. | ATTEMPTED. It computes noncentrality and scalar compatibility, but it is not owner/audit ratification of the KS-route object. |
| KS phase route | Treat KS phase forcing as the kernel-object theorem. | ATTEMPTED. It supplies bounded phase/gauge-class support under declared premises, not this retained handoff. |
| kinetic two-ray route | Treat the scalar/Dirac-ray classification as this kernel-object theorem. | ATTEMPTED. It is support with named residuals; it does not force the `K1` Dirac branch or this handoff. |
| chirality/domain-wall route | Treat `{epsilon,D}=0`, #5014, #5017, or #5018 as the route-defined kernel. | ATTEMPTED. They are chirality/domain-wall support only. |
| W4/value/custody route | Treat open #5026 or merged #5019/#5020/#5022/#5023/#5024 as this kernel theorem. | ATTEMPTED. They are custody/R-eta/value-face/W4 readiness only. |
| primitive shortcut | Spend an approved primitive as the spinful kernel theorem. | ATTEMPTED. The primitive registry was checked; no such primitive is registered. |

### N2 - Wall-Independence Audit

The collapsed live wall set is:

```text
KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED
KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

| Pair | Does the first close the second? | Does the second close the first? | Independent? |
|---|---:|---:|---:|
| route-defined momentum/link phase / spinful kernel object theorem | no | no | yes |
| route-defined momentum/link phase / owner ratification | no | no | yes |
| route-defined momentum/link phase / audit acceptance | no | no | yes |
| spinful kernel object theorem / owner ratification | no | no | yes |
| spinful kernel object theorem / audit acceptance | no | no | yes |
| owner ratification / audit acceptance | no | no | yes |

### N3 - Hidden-Wall Scan

Phrases checked: `accepted`, `support`, `bounded`, `finite`, `kernel`,
`spinful`, `sigma.p`, `KS`, `Kawamoto-Smit`, `chirality`, `domain-wall`,
`merged PR`, `open PR`, `registered`, and `primitive`. These are cited
support/status words only. No sentence converts them into the retained
KS-route kernel handoff. The two physics walls and two governance/audit gates
are explicit in N2.

### N4 - Residual Matching

| Witness | Witness residual | This target residual | Match? |
|---|---|---|---|
| carrier-attachment sharpening note | scalar kernel compatible; spinful selector location named; state-law bridge still open | retained route-defined spinful kernel object | yes |
| carrier-attachment runner | finite scalar vs spinful `sigma.p` check | retained KS-route object handoff | yes, as support/nonclosure boundary |
| matter-attachment reduction note | KS/state-law bridge still required | route-defined kernel subinput under KS route | yes, as upstream context |
| KS phase forcing note | bounded KS phase/gauge class under declared kinetic class | retained spinful kernel object | yes, as support/nonclosure boundary |
| kinetic class forcing note | scalar/Dirac-ray support with open selector residuals | retained spinful kernel object | yes, as support/nonclosure boundary |
| #5014/#5017/#5018/#5019/#5020/#5022/#5023/#5024 | adjacent support/hygiene/value-face status | route-defined spinful kernel object | yes |

### N5 - Rhetoric Audit

The negative language is scoped to the exact theorem handle
`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`. It is tested at the
kernel-object handoff level only. This note does not use broader phrases like
"spinful kernels cannot be retained" or "the KS route cannot define a
kernel."

### N6 - Partial-Closure Path Scan

| Candidate path | Status | What it would close |
|---|---|---|
| retained route-defined momentum/link-phase input | open positive route | `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED` |
| momentum/link-phase target packet using P-FLUX and Kawamoto-Smit support | open positive child route | same input after owner/audit acceptance; see `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md` |
| retained spinful kernel-object theorem | open positive route, now packaged by `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_TARGET_DISCRIMINATOR_2026-07-05.md` | `KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED` |
| owner/audit acceptance after both physics inputs | open governance/audit route | `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED` |
| retained trivial-scalar covariance failure theorem | separate open sibling input | can help close the scalar-lift exclusion lane, but not this target by itself |
| KS spin-lift physical action law | separate open sibling input | can help close the KS child route, but not this target by itself |
| future primitive registry update | absent now | could supply a primitive only after explicit owner/review update |

### N7 - Steelman

A hostile reviewer could argue that this subinput is already effectively
landed: the carrier-attachment note and runner explicitly display `sigma.p`
as the spinful selector, and the finite runner computes that it is noncentral.
This note treats that as strong support, not retained closure. The route still
needs an accepted KS-route momentum/link-phase input and an accepted kernel
object theorem before the scalar-lift lane can spend it.

### N8 - Cross-Cycle Echo

This is the same wall shape as the parent scalar-lift and KS child lanes:
support calculations do not automatically become a retained handoff. Prior
retirements of similar walls required explicit bridge theorem, accepted
convention, or approved primitive registration. None is present for this
target now.

Gate result: PASS for the narrowed current-surface non-supply claim. Broad
spinful-kernel impossibility is not shipped.

## Explicit Non-Claims

- No derivation or ratification of
  `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.
- No derivation or ratification of
  `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`.
- No derivation or ratification of
  `KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED`.
- No derivation or ratification of
  `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.
- No derivation or ratification of
  `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.
- No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.
- No derivation or ratification of
  `KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.
- No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.
- No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.
- No R-eta, h-class, h-unit, `K1`/`K3`/`K4`, Koide mass, electron mass,
  `alpha(0)`, Rydberg, static-source NR Coulomb, or retained hydrogen
  consequence.
- No new axiom, primitive, Tier-A admission, empirical import, or audit status
  is introduced.
- No claim that #5014, #5017, #5018, #5019, #5020, #5022, #5023, or #5024
  supplies the spinful `sigma.p` KS-route kernel theorem.
- No claim that #5026 supplies the spinful `sigma.p` KS-route kernel theorem.
