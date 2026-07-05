# Koide R-Eta Trivial Scalar-Lift Covariance Exclusion Target Discriminator

Date: 2026-07-05

**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_trivial_scalar_lift_covariance_exclusion.py`

Purpose: isolate the finite covariance-failure theorem that the spinful
staggered kernel scalar-lift exclusion lane still needs:
`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`. This discriminator does
not derive or ratify
`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`, does not derive
`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`, and does not
calculate retained hydrogen.

## Target

The target handoff is:

```text
TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED
```

Meaning: once a route-defined spinful `sigma.p` kernel has been retained, the
trivial scalar lift `V(R)=I_2` fails the spinful kernel-covariance test. The
faithful spin lift rotates `sigma_x` to `sigma_y` for a quarter-turn about the
`z` axis; the trivial scalar lift leaves `sigma_x` fixed. This is a finite
covariance-failure handoff only. It is not the parent scalar-lift exclusion
handoff, not the KS physical spin-lift action law, and not a physical
matter-state law.

## Retention Contract

`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED` requires all of the
following inputs:

```text
TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TEXT_LOCK
SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED
SCALAR_KERNEL_COMPATIBILITY_ACCEPTED
STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED
SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED
FINITE_FAITHFUL_SPIN_LIFT_COVARIANCE_CHECK
FINITE_TRIVIAL_LIFT_COVARIANCE_FAILURE_CHECK
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
TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED
```

That consequence can feed the parent scalar-lift exclusion lane as one input,
but it cannot close
`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED` without the parent
text lock, support inputs, a separately retained
`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED` handle, owner
ratification, and audit acceptance.

## Input Roles

| Input | Role |
|---|---|
| `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TEXT_LOCK` | fixes this lane as the finite trivial-lift covariance-failure theorem, not the parent scalar-lift handoff |
| `SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED` | consumes the source no-go that operator-frame/Clifford data do not force the per-site state law |
| `SCALAR_KERNEL_COMPATIBILITY_ACCEPTED` | records that the spin-blind scalar kernel remains compatible with the trivial scalar lift |
| `STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED` | records the staggered/Kawamoto-Smit route as the live place where a spinful selector can enter |
| `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED` | supplies the retained route-defined spinful kernel to test |
| `FINITE_FAITHFUL_SPIN_LIFT_COVARIANCE_CHECK` | records the finite Pauli witness that a faithful spin lift co-rotates `sigma.p` |
| `FINITE_TRIVIAL_LIFT_COVARIANCE_FAILURE_CHECK` | records the finite Pauli witness that the trivial scalar lift does not co-rotate the spinful kernel |
| `NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT` | prevents importing the parent scalar-lift exclusion handoff |
| `NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT` | prevents spending the KS physical spin-lift action law |
| `NO_KS_ROUTE_CLOSURE_INPUT` | prevents importing the full KS child theorem as a premise |
| `NO_PARENT_BRIDGE_OR_HW1_INPUT` | prevents importing the parent state-law bridge, HW1 locus, carrier, or hydrogen as a premise |
| `NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT` | prevents importing Koide value/angle outputs |
| `NO_K1_K3_K4_OR_MASS_INPUT` | prevents importing electron-readout or mass-route closure |
| `NO_COMPARATOR_PROOF_INPUT` | prevents importing observed mass/hydrogen comparator matches |
| `NO_NEW_PRIMITIVE_OR_AXIOM` | prevents a silent primitive or axiom shortcut |
| `OWNER_RATIFICATION` | owner accepts this as the intended trivial scalar-lift covariance-exclusion handoff |
| `AUDIT_ACCEPTANCE` | independent audit accepts the retained consequence |

## Current Surface

| Surface | What it supplies | What it does not supply |
|---|---|---|
| `CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md` | refutes the spinor-module escape; records scalar-kernel compatibility and identifies spinful `sigma.p` as the displayed selector excluding scalar | owner/audit-retained trivial scalar-lift covariance-failure theorem |
| `scripts/carrier_attachment_chirality_gate_consolidation_runner.py` | finite checks that scalar kernels remain compatible while spinful `sigma.p` is noncentral | owner/audit acceptance of this target handle |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md` | parent child target that can supply `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED` if retained | this trivial scalar-lift covariance-failure theorem |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | decision shape for the route-defined spinful kernel | scalar-lift covariance-failure acceptance |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md` | records current non-supply of the route-defined spinful kernel handoff | this target handle |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md` | parent scalar-lift target that consumes this lane if retained | this child theorem itself or the route-defined spinful kernel handle |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md` | KS child route that can consume the parent scalar-lift handoff | this finite covariance-failure theorem |

The current retained, primitive, merged-PR, and open-PR surfaces therefore do
not supply `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED` as a retained
handle. This target remains a live positive route, not a closed no-go.

The approved primitive registry was checked. Registered primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. None is a
`trivial_scalar_lift_covariance_exclusion_primitive`,
`spinful_sigma_dot_p_kernel_primitive`,
`spinful_staggered_kernel_primitive`,
`ks_to_physical_matter_state_spinor_law_primitive`,
`physical_matter_state_law_primitive`, or `hydrogen_primitive`. The
kinetic-isotropy primitive supplies only structural OS0 kinetic-form isotropy
`c_t = c_s`; it does not supply a dynamics theorem, Lorentz-closure theorem,
selector, readout bridge, spinful kernel theorem, or scalar-lift exclusion
theorem.

## Open And Merged PR Alignment

PRs were refreshed on 2026-07-05 UTC. Lane-relevant PRs are queue/status
signals; clean/dirty/check labels are not proof inputs.

| PR | queue signal | trivial scalar-lift effect |
|---|---|---|
| open `#5016` zero-import hydrogen retained lane bundle | carries this lane once pushed | not landed authority while open |
| open `#5026` Koide custody L4 retained-successor re-point | charged-lepton custody L4 rewire to retained-bounded momentum-type successor; Plancherel edge demotion | no trivial scalar-lift covariance-failure theorem |
| merged `#5019` AC_phi_lambda decomposition chain | Koide form-layer rebase | no trivial scalar-lift covariance-failure theorem |
| merged `#5020` AC_phi_lambda value face | value-face/exactness relocation | no trivial scalar-lift covariance-failure theorem |
| merged `#5022` delta-eta chain repair | supplied-premise and K-orbit form authority | no trivial scalar-lift covariance-failure theorem |
| merged `#5023` Koide W4 audit-readiness repairs | record/species/custody/hw-complement hygiene | no trivial scalar-lift covariance-failure theorem |
| merged `#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | gate-readiness and audit-graph hygiene | no trivial scalar-lift covariance-failure theorem |
| open `#5021` primitive-retirement review | draft meta map; no retirements | no primitive shortcut |
| open `#5014` record-formation front domain wall | formation-front/domain-wall support | no trivial scalar-lift covariance-failure theorem |
| open `#5017` domain-wall edge anomaly inflow spectral flow | anomaly-flow support | no trivial scalar-lift covariance-failure theorem |
| open `#5018` domain-wall edge content vs SM chiral map | chirality/domain-wall map with named gaps | no trivial scalar-lift covariance-failure theorem |

## No-Go Discipline Gate

Gate target: narrow current-surface non-supply only. The checked claim is that
the current retained, primitive, merged-PR, and open-PR surfaces do not supply
`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`. The gate does not assert
that this theorem can never be supplied.

### N1 - Alternative Route Enumeration

| Route | Attempt | Result |
|---|---|---|
| full trivial-lift covariance contract | Accept all fixed/support inputs plus the retained route-defined spinful kernel and owner/audit acceptance. | OPEN POSITIVE ROUTE. This would close the target, but the missing inputs are not supplied here. |
| sigma-dot-p retained route | Treat the parent spinful `sigma.p` route as also supplying this theorem. | ATTEMPTED. It would supply the kernel object to test, not the scalar-lift covariance-failure handoff by itself. |
| carrier-attachment source route | Treat the carrier-attachment sharpening note as the retained covariance-failure theorem. | ATTEMPTED. It names the boundary and support, but it does not ratify this child handle. |
| finite runner route | Treat the existing finite scalar/spinful check as audit-retained closure. | ATTEMPTED. It computes the support fact, but it is not owner/audit acceptance of this target. |
| scalar-kernel compatibility route | Treat scalar-kernel compatibility as exclusion. | ATTEMPTED. Compatibility keeps the scalar lift alive for spin-blind kernels; it does not prove the spinful-kernel covariance failure as a retained handoff. |
| KS phase or kinetic two-ray route | Treat KS phase forcing or scalar/Dirac-ray support as this theorem. | ATTEMPTED. These are support surfaces with named residuals, not this accepted handle. |
| chirality/domain-wall route | Treat `{epsilon,D}=0`, #5014, #5017, or #5018 as the covariance-failure theorem. | ATTEMPTED. They are chirality/domain-wall support only. |
| W4/value/custody route | Treat #5026 or merged #5019/#5020/#5022/#5023/#5024 as this theorem. | ATTEMPTED. They are Koide custody/value-face/W4 readiness only. |
| primitive shortcut | Spend an approved primitive as the theorem. | ATTEMPTED. The primitive registry was checked; no such primitive is registered. |

### N2 - Wall-Independence Audit

The collapsed live wall set is:

```text
SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

| Pair | Does the first close the second? | Does the second close the first? | Independent? |
|---|---:|---:|---:|
| route-defined spinful kernel / owner ratification | no | no | yes |
| route-defined spinful kernel / audit acceptance | no | no | yes |
| owner ratification / audit acceptance | no | no | yes |

The finite Pauli covariance checks are not counted as live walls here because
this packet reproduces them directly and verifies them in the companion
runner. The retained route-defined spinful kernel remains a wall because this
target cannot test an unretained route object as a spendable input.

### N3 - Hidden-Wall Scan

Phrases checked: `accepted`, `support`, `finite`, `kernel`, `spinful`,
`scalar`, `covariance`, `KS`, `Kawamoto-Smit`, `chirality`, `domain-wall`,
`merged PR`, `open PR`, `registered`, and `primitive`. These are cited
support/status words only. No sentence converts them into the retained
covariance-failure handoff. The route-defined kernel and governance/audit
gates are explicit in N2.

### N4 - Residual Matching

| Witness | Witness residual | This target residual | Match? |
|---|---|---|
| carrier-attachment sharpening note | scalar kernel compatible; spinful selector location named; state-law bridge still open | retained trivial scalar-lift covariance-failure theorem | yes |
| carrier-attachment runner | finite scalar-vs-spinful kernel check | retained covariance-failure handoff | yes, as support/nonclosure boundary |
| sigma-dot-p KS-route packet | route-defined spinful kernel still not retained on current surface | kernel input needed before this target can close | yes |
| scalar-lift parent packet | parent needs this theorem plus route-defined spinful kernel | this child theorem only | yes |
| #5014/#5017/#5018/#5019/#5020/#5022/#5023/#5024/#5026 | adjacent support/hygiene/value-face/custody status | retained covariance-failure theorem | yes |

### N5 - Rhetoric Audit

The negative language is scoped to the exact theorem handle
`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`. It is tested at the
child handoff level only. This note does not use broader phrases like
"all scalar lifts fail" or "the KS route cannot carry scalars."

### N6 - Partial-Closure Path Scan

| Candidate path | Status | What it would close |
|---|---|---|
| retained route-defined spinful `sigma.p` kernel | open positive route, packaged by the sigma-dot-p KS-route lane | `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED` |
| owner/audit ratification of this packet after the route kernel is retained | open positive route | `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED` |
| parent scalar-lift exclusion after both physics handles | downstream open route | `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED` |
| KS physical spin-lift action law | separate open sibling input | can help close the KS child route, but not this target by itself |
| future primitive registry update | absent now | could supply a primitive only after explicit owner/review update |

### N7 - Steelman

A hostile reviewer could argue that this child theorem is already effectively
landed: the carrier-attachment note says the spinful `sigma.p` kernel is the
displayed selector that excludes the scalar, and the runner computes the
finite scalar/spinful split. This note treats that as strong support, not
retained closure. The target still needs the route-defined kernel handle and
owner/audit acceptance before the parent scalar-lift lane can spend it.

### N8 - Cross-Cycle Echo

This is the same support-vs-retained-handoff wall shape as the parent
scalar-lift, sigma-dot-p, and KS child lanes. Prior retirements of similar
walls required an explicit bridge theorem, accepted convention, or approved
primitive registration. None is present for this exact target now.

Gate result: PASS for the narrowed current-surface non-supply claim. Broad
scalar-lift impossibility is not shipped.

## Explicit Non-Claims

- No derivation or ratification of
  `TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.
- No derivation or ratification of
  `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.
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
- No claim that #5014, #5017, #5018, #5019, #5020, #5022, #5023, #5024, or
  #5026 supplies the trivial scalar-lift covariance-failure theorem.
