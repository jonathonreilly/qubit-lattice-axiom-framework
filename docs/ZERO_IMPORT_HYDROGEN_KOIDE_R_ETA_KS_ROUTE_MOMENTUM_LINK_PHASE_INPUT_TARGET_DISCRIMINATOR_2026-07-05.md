# Koide R-Eta KS Route Momentum Link-Phase Input Target Discriminator

Date: 2026-07-05

**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_ks_route_momentum_link_phase_input.py`

Purpose: isolate the route-defined momentum/link-phase subinput under the
spinful `sigma.p` KS-route kernel lane. This discriminator does not derive or
ratify `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`,
does not derive `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`,
does not derive `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`, and
does not calculate retained hydrogen.

## Target

The target handoff is:

```text
KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED
```

Meaning: on the Kawamoto-Smit / staggered route, the route supplies a
well-defined link-phase or equivalent momentum-covector input that can name the
`p` in the later spinful `sigma.p` kernel-object theorem. It is a route-input
handoff only. It is not the spinful kernel-object theorem, not scalar-lift
exclusion, not the KS physical spin-lift action law, and not a physical
matter-state law.

## Retention Contract

`KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED` requires all
of the following inputs:

```text
KS_ROUTE_MOMENTUM_LINK_PHASE_TEXT_LOCK
TWO_FLUX_CLASS_KINETIC_SURFACE_ACCEPTED
P_FLUX_WITHIN_SURFACE_SELECTION_ACCEPTED
KAWAMOTO_SMIT_LINK_PHASE_REPRESENTATIVE_ACCEPTED
FINITE_LINK_PHASE_AND_BLOCH_MOMENTUM_SUPPORT_CHECK
WRAP_HOLONOMY_BOUNDARY_LOCK
NO_FULL_KINETIC_SURFACE_RETIREMENT_INPUT
NO_SPINFUL_KERNEL_OBJECT_THEOREM_INPUT
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
KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED
```

That consequence may feed
`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED` as one subinput, but
it cannot close the spinful kernel-object theorem without
`KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED`, owner ratification, and
audit acceptance.

## Input Roles

| Input | Role |
|---|---|
| `KS_ROUTE_MOMENTUM_LINK_PHASE_TEXT_LOCK` | fixes this lane as the route momentum/link-phase handoff, not a spinful kernel theorem |
| `TWO_FLUX_CLASS_KINETIC_SURFACE_ACCEPTED` | records the licensed two-flux-class surface with `K0` and `K1` classes |
| `P_FLUX_WITHIN_SURFACE_SELECTION_ACCEPTED` | records the P-FLUX support row at its within-surface scope |
| `KAWAMOTO_SMIT_LINK_PHASE_REPRESENTATIVE_ACCEPTED` | records the `eta_1=1`, `eta_2=(-1)^x1`, `eta_3=(-1)^(x1+x2)` representative as the link-phase object |
| `FINITE_LINK_PHASE_AND_BLOCH_MOMENTUM_SUPPORT_CHECK` | records finite checks for uniform flux, Bloch spectra, and link-phase support |
| `WRAP_HOLONOMY_BOUNDARY_LOCK` | keeps finite-torus wrap/PBC/APBC convention data out of the local handoff |
| `NO_FULL_KINETIC_SURFACE_RETIREMENT_INPUT` | prevents this lane from claiming wholesale P-KIN retirement |
| `NO_SPINFUL_KERNEL_OBJECT_THEOREM_INPUT` | prevents this lane from importing the parent spinful `sigma.p` kernel-object theorem |
| `NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT` | prevents this lane from importing scalar-lift covariance failure |
| `NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT` | prevents this lane from importing scalar-lift exclusion |
| `NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT` | prevents this lane from spending the KS physical spin-lift action law |
| `NO_KS_ROUTE_CLOSURE_INPUT` | prevents importing the full KS child theorem as a premise |
| `NO_PARENT_BRIDGE_OR_HW1_INPUT` | prevents importing the parent state-law bridge, HW1 locus, carrier, or hydrogen as a premise |
| `NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT` | prevents importing Koide value/angle outputs |
| `NO_K1_K3_K4_OR_MASS_INPUT` | prevents importing electron-readout or mass-route closure |
| `NO_COMPARATOR_PROOF_INPUT` | prevents importing observed mass/hydrogen comparator matches |
| `NO_NEW_PRIMITIVE_OR_AXIOM` | prevents a silent primitive or axiom shortcut |
| `OWNER_RATIFICATION` | owner accepts this as the intended route-input handoff |
| `AUDIT_ACCEPTANCE` | independent audit accepts the retained consequence |

## Current Surface

| Surface | What it supplies | What it does not supply |
|---|---|---|
| `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` | two-flux-class surface; `K1` representative; P-SD discharged on `K1`; `K0` countermodel showing the specified constraints do not force `K1` | hydrogen-facing retained route-input handoff |
| `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md` | within-surface selection of `phi=-1` at the chain's stated grade | wholesale kinetic-surface retirement or this owner/audit handoff |
| `STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md` | retained geometry leg: `K1` satisfies (Z), `K0` violates it | no selection by itself; no thermal content |
| `AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md` | retained-bounded FSB-K supplier used by the P-FLUX composer | no route handoff without composition and acceptance |
| `GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md` | thermal `7/8` Stefan-Boltzmann currency context used by the P-FLUX support stack | no route handoff or flux selection by itself |
| `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md` | local `eta` phase law and scalarization iff on supplied `P-KIN/P-SD` surface | no full kinetic-surface retirement |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md` | records open #5011 as eta/Kawamoto-Smit covariant-walk context | no route-defined momentum/link-phase handoff |
| `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` | bounded synthesis context with explicit residuals | no unbounded physical state-action theorem |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md` | parent target that consumes this lane if retained | spinful kernel-object theorem itself |

The current retained, primitive, merged-PR, and open-PR surfaces therefore do
not supply `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`.
This target remains a live positive route, not a closed no-go.

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

| PR | queue signal | route momentum/link-phase effect |
|---|---|---|
| open `#5016` zero-import hydrogen retained lane bundle | carries this lane once pushed | not landed authority while open |
| merged `#5019` AC_phi_lambda decomposition chain | Koide form-layer rebase | no route momentum/link-phase handoff |
| merged `#5020` AC_phi_lambda value face | value-face/exactness relocation | no route momentum/link-phase handoff |
| merged `#5022` delta-eta chain repair | supplied-premise and K-orbit form authority | no route momentum/link-phase handoff |
| merged `#5023` Koide W4 audit-readiness repairs | record/species/custody/hw-complement hygiene | no route momentum/link-phase handoff |
| merged `#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | gate-readiness and audit-graph hygiene | no route momentum/link-phase handoff |
| open `#5021` primitive-retirement review | draft meta map; no retirements | no primitive shortcut |
| open `#5011` eta twisted walk family runner repair | eta/Kawamoto-Smit covariant-walk context via `ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md` | no route momentum/link-phase handoff |
| open `#5014` record-formation front domain wall | formation-front/domain-wall support | no route momentum/link-phase handoff |
| open `#5017` domain-wall edge anomaly inflow spectral flow | anomaly-flow support | no route momentum/link-phase handoff |
| open `#5018` domain-wall edge content vs SM chiral map | chirality/domain-wall map with named gaps | no route momentum/link-phase handoff |

## No-Go Discipline Gate

Gate target: narrow current-surface non-supply only. The claim checked here is
that the current retained, primitive, merged-PR, and open-PR surfaces do not
supply `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`. The
gate does not assert that this route-input handoff can never be supplied.

### N1 - Alternative Route Enumeration

| Route | Attempt | Result |
|---|---|---|
| full momentum/link-phase contract | Accept all support inputs plus owner/audit acceptance at this exact handoff. | OPEN POSITIVE ROUTE. This would close the target, but the handoff is not accepted here. |
| kinetic-class route | Treat the two-flux-class theorem as the retained route input. | ATTEMPTED. It supplies the two-class surface and `K1` representative but keeps the selector/surface grade boundaries explicit. |
| P-FLUX route | Treat the P-FLUX composer as this handoff. | ATTEMPTED. It selects within the licensed two-class surface at the chain's grade, but says it does not retire P-KIN wholesale or set this hydrogen-facing handoff. |
| Z-certificate route | Use the (Z) certificate alone. | ATTEMPTED. It computes `K1` geometry and `K0` violation but performs no flux selection and has no thermal content. |
| KS phase route | Treat the Kawamoto-Smit phase-forcing theorem as this handoff. | ATTEMPTED. It supplies local phase classification on declared premises, not this owner/audit handoff. |
| finite runner route | Treat finite link-phase/Bloch checks as retained closure. | ATTEMPTED. They support the handoff but do not set retained authority. |
| chirality/domain-wall route | Treat #5014, #5017, or #5018 as route-input closure. | ATTEMPTED. They are chirality/domain-wall support only. |
| W4/value-face route | Treat merged #5019/#5020/#5022/#5023/#5024 as this handoff. | ATTEMPTED. They are R-eta/value-face/W4 readiness only. |
| primitive shortcut | Spend an approved primitive as this route input. | ATTEMPTED. The primitive registry was checked; no such primitive is registered. |

### N2 - Wall-Independence Audit

The collapsed live wall set is:

```text
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The physics support stack is currently explicit but not promoted here:
two-flux-class surface, P-FLUX within-surface selection, K1 link-phase
representative, finite link/Bloch checks, and wrap-holonomy boundary lock. None
of those automatically supplies owner ratification or independent audit
acceptance for this exact hydrogen-facing handoff.

| Pair | Does the first close the second? | Does the second close the first? | Independent? |
|---|---:|---:|---:|
| owner ratification / audit acceptance | no | no | yes |
| P-FLUX support / owner ratification | no | no | yes |
| P-FLUX support / audit acceptance | no | no | yes |
| wrap-holonomy boundary / owner ratification | no | no | yes |
| wrap-holonomy boundary / audit acceptance | no | no | yes |

### N3 - Hidden-Wall Scan

Phrases checked: `accepted`, `support`, `bounded`, `within-surface`,
`retained_bounded`, `K1`, `K0`, `phi=-1`, `Kawamoto-Smit`, `link phase`,
`momentum`, `merged PR`, `open PR`, `registered`, and `primitive`. These are
cited support/status words only. No sentence converts them into the retained
route-input handoff. Owner/audit gates are explicit in N2.

### N4 - Residual Matching

| Witness | Witness residual | This target residual | Match? |
|---|---|---|---|
| kinetic-class forcing note | two-flux surface; `K1` selector residual | route-defined link-phase handoff | yes, as source surface |
| P-FLUX composer | within-surface `phi=-1` selection | route-input handoff | yes, as support/nonclosure boundary |
| Z certificate | K1 point-cone geometry and K0 violation | P-FLUX support, not handoff | yes, as source support |
| FSB-K row | thermal finite-species supplier for P-FLUX | P-FLUX support, not handoff | yes, as source support |
| KS phase forcing note | local `eta` phase law on declared premises | link-phase representative | yes, as support/nonclosure boundary |
| sigma-dot-p parent target | consumes this handle if retained | parent route-input residual | yes |
| #5014/#5017/#5018/#5019/#5020/#5022/#5023/#5024 | adjacent support/hygiene/value-face status | no route-input handoff | yes |

### N5 - Rhetoric Audit

The negative language is scoped to the exact theorem handle
`KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`. It is tested
at the route-input handoff level only. This note does not use broader phrases
like "K1 is not selected" or "the KS route has no link phase."

### N6 - Partial-Closure Path Scan

| Candidate path | Status | What it would close |
|---|---|---|
| owner/audit acceptance of this packet using the P-FLUX support stack at its stated scope | open governance/audit route | `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED` |
| future kinetic-surface audit that retires P-KIN wholesale | separate open route | strengthens the support stack but is not required to state the local handoff |
| retained spinful kernel-object theorem | separate parent input | can help close the sigma-dot-p parent, but not this target by itself |
| retained scalar-lift covariance failure theorem | separate sibling input | can help close scalar-lift exclusion, but not this target by itself |
| future primitive registry update | absent now | could supply a primitive only after explicit owner/review update |

### N7 - Steelman

A hostile reviewer could argue that this handoff should be accepted now: the
kinetic-class row narrows the surface to `K0`/`K1`, the P-FLUX composer selects
`phi=-1` within that surface at the chain's grade, and the KS phase note gives
the displayed Kawamoto-Smit `eta` representative. This note treats that as the
strongest support. It still requires explicit owner/audit acceptance of the
hydrogen-facing handoff because the cited source rows intentionally preserve
scope boundaries and do not name this route-input handle.

### N8 - Cross-Cycle Echo

This echoes the recurring support-vs-handoff wall: strong computed support does
not automatically become a new retained handle until the handle is stated,
accepted, and audited at its own scope. Prior lanes retired similar walls by
explicit theorem, accepted convention, or approved primitive registration. None
is present for this target now.

Gate result: PASS for the narrowed current-surface non-supply claim. Broad
K1/link-phase impossibility is not shipped.

## Explicit Non-Claims

- No derivation or ratification of
  `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`.
- No derivation or ratification of
  `KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED`.
- No derivation or ratification of
  `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.
- No derivation or ratification of
  `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.
- No derivation or ratification of
  `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.
- No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.
- No derivation or ratification of
  `KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.
- No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.
- No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.
- No full P-KIN wholesale retirement, no finite-torus wrap convention
  selection, and no physical matter-state action law.
- No R-eta, h-class, h-unit, `K1`/`K3`/`K4`, Koide mass, electron mass,
  `alpha(0)`, Rydberg, static-source NR Coulomb, or retained hydrogen
  consequence.
- No new axiom, primitive, Tier-A admission, empirical import, or audit status
  is introduced.
- No claim that #5014, #5017, #5018, #5019, #5020, #5022, #5023, or #5024
  supplies the route momentum/link-phase handoff.
