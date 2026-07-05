# Zero-Import Hydrogen: Koide R-Eta H-Unit Identity-Radian Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide R-eta h-unit import-retirement handoff
**Status:** support-only. This note does not derive R-eta, does not ratify
`R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`, does not ratify
`R_ETA_READOUT_IDENTIFICATION_RETAINED`, does not derive `delta = 2/9`, does
not ratify `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`, does not ratify
`K2_R_ETA_EXACTNESS_RETAINED`, does not derive the physical electron mass, and
does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_h_unit_identity_radian_target_discriminator.py`

## Scope

The R-eta readout-retirement target decomposes the admitted `A_R-eta` atom into
h-class plus h-unit. This discriminator attacks only the h-unit side:

```text
R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED.
```

The target is the identity-radian conversion coefficient:

```text
fixed-locus density value 2/9  ->  charged-lepton phase value 2/9 rad
with conversion coefficient 1.
```

It is a sublane under `R_ETA_READOUT_IDENTIFICATION_RETAINED`. It is not
h-class, not physical carrier realization, not full R-eta retirement, not the
two-ninths/radian subgate, and not K2 exactness.

## Target Contract

`R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED` requires all eleven inputs:

```text
R_ETA_H_UNIT_TEXT_LOCK
DEFECT_IDENTITY_UNIT_NORMAL_FORM_ACCEPTED
ANGLE_SIDE_RIGIDITY_ACCEPTED
TYPE_B_TO_RADIAN_RESIDUAL_ALIGNMENT_ACCEPTED
IDENTITY_UNIT_SELECTION_THEOREM_RETAINED
NO_COUNT_NORMALIZATION_SHORTCUT
NO_H_CLASS_CARRIER_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

No proper subset supplies the handoff.

| input | role |
|---|---|
| R_ETA_H_UNIT_TEXT_LOCK | fixes the object as h-unit identity-radian retirement only |
| DEFECT_IDENTITY_UNIT_NORMAL_FORM_ACCEPTED | accepts the finite additive normal form `I_c(R) = c * |R| * L`, `L = 2/9` |
| ANGLE_SIDE_RIGIDITY_ACCEPTED | accepts that the retained angular side has no continuous unit freedom beyond the stripped sign |
| TYPE_B_TO_RADIAN_RESIDUAL_ALIGNMENT_ACCEPTED | aligns this target with the standing Type-B rational-to-radian residual |
| IDENTITY_UNIT_SELECTION_THEOREM_RETAINED | supplies the missing rescale-breaking or angle-native theorem that pins `c = 1` |
| NO_COUNT_NORMALIZATION_SHORTCUT | excludes the bare count route, which pins `c = 9/2`, and excludes "one atom reads L" as a restatement |
| NO_H_CLASS_CARRIER_OR_MASS_INPUT | excludes h-class, carrier realization, K1, K3, K4, branch mass-map, and electron-mass inputs |
| NO_COMPARATOR_PROOF_INPUT | excludes fitted `Phi_PDG`, fitted `delta`, observed lepton masses, observed `m_e`, observed `alpha(0)`, and observed hydrogen |
| NO_NEW_PRIMITIVE_OR_AXIOM | keeps this as import retirement rather than adding a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | owner accepts this as the h-unit identity-radian object |
| AUDIT_ACCEPTANCE | independent audit accepts the target and dependency consequences |

If accepted, this handoff supplies exactly one input to the R-eta
readout-retirement target:

```text
R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED.
```

It still does not supply `R_ETA_H_CLASS_RETAINED`,
`PHYSICAL_CARRIER_CONTEXT_RETAINED`, owner/audit acceptance for full R-eta
retirement, or any downstream electron-mass or hydrogen input.

## Current Surface

| surface | useful content | residual |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md` | packages `R_ETA_READOUT_IDENTIFICATION_RETAINED` as h-class plus h-unit | this note supplies only the h-unit target |
| `ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md` | decomposes `A_R-eta` into h-class plus h-unit | h-unit remains admitted, not retired |
| `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md` | derives the `I_c` normal form, proves additivity is rescale-invariant, shows count pins `c = 9/2`, and localizes the wall at the density-to-angle junction | no retained theorem pins `c = 1` |
| `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md` | keeps Type-B rational-to-radian identification primitive and sharpens it to period-1-rad vs canonical period-2pi | no retained period-1-radian convention or source theorem |
| `KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md` | proves retained periodic phases are rational multiples of pi while `2/9` is a pure rational | no retained bridge maps pure rational to literal radian |
| `BRANNEN_DELTA_SPECTRAL_ASYMMETRY_CONVENTION_ISOLATION_NOTE_2026-05-31.md` | isolates finite `2/9` weight versus period-normalization boundary | does not ratify period-1-radian normalization |
| `PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md` | supplies native `U(1)` phase periodicity | does not choose this Koide selected-line value or period-1-radian reading |
| `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md` | co-identifies `W_cycle_holonomy_value`, `W_defect_identity_unit`, and R-eta junction coefficient | value wall remains the same h-unit junction input |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation discipline | no phase selector, readout bridge, exact value, mass, alpha, or hydrogen |

The primitive registry was checked. The approved primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. They are premise nodes, not walls, but they do
not supply `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`, `R_ETA_H_CLASS_RETAINED`,
`R_ETA_READOUT_IDENTIFICATION_RETAINED`, `delta = 2/9`, `m_e`, `alpha(0)`, or
hydrogen.

The companion current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`. This target remains a
positive import-retirement route, not a retained consequence.

## Hydrogen Effect

If accepted, this target retires one atom inside the Koide R-eta branch: the
identity-radian unit coefficient only. It would still be only a subinput to
R-eta readout retirement. Hydrogen still needs h-class, carrier realization,
R-eta owner/audit acceptance, the two-ninths/radian packet, K2
value-face/exactness, K1 occupancy/counting, K3 physical electron species, K4
absolute scale, physical electron mass, `alpha(0)`, and the static-source NR
Coulomb limit.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "h-unit is retained" is
not shipped. The narrowed claim is:

```text
R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is the next import-retirement target
for the identity-radian unit coefficient inside R-eta.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| Record additivity route | Derive `c = 1` from finite additive readout alone. | ATTEMPTED BY PRIOR. The defect identity-unit note proves the surface is rescale-invariant. |
| bare count route | Use "one locked atom reads 1" as the unit. | RULED OUT BY PRIOR. It pins `c = 9/2`, not `c = 1`. |
| count-in-density-units route | State "one locked atom reads L". | ATTEMPTED. This restates `c = 1` rather than deriving it. |
| angle-side convention route | Absorb `c` as an angular-unit convention. | RULED OUT BY PRIOR. The angle side is rigid beyond the stripped sign, so different `c` are different readouts. |
| retained periodic phase-source route | Use `Z_3`, Berry, Wilson, or finite periodic phases. | RULED OUT BY PRIOR. Retained periodic sources give `q*pi`, not literal pure rational `2/9` radians. |
| Type-B rational stacking route | Stack many exact `2/9` witnesses. | ATTEMPTED. The A1 audit says stacking rational witnesses leaves the same Type-B-to-radian map. |
| native `U(1)` phase route | Spend the native Hilbert phase unit as the Koide selected-line value. | PARTIAL ONLY. It supplies phase periodicity, not the selected-line period-1-radian reading. |
| primitive shortcut | Treat approved primitives as supplying the selector. | ATTEMPTED. Registered primitives supply no phase selector, readout bridge, exact value, or mass. |
| comparator route | Use fitted or observed charged-lepton masses. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| h-unit <-> h-class | no | independent components of `A_R-eta` |
| h-unit <-> physical carrier context | no | unit selection does not prove carrier realization |
| h-unit <-> R-eta owner/audit acceptance | no | target input versus packet acceptance |
| h-unit <-> two-ninths fold/domain lock | no | downstream packet owns domain lock |
| h-unit <-> K2 value-face acceptance | no | independent K2 input |
| h-unit <-> K1/K3/K4 gates | no | independent downstream gates |
| owner ratification <-> audit acceptance | no | independent |

The collapsed target wall set is: identity-unit selection theorem, owner
ratification, and audit acceptance, with normal form, angle rigidity, and
residual alignment as support inputs.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `normal form` / `I_c` | accepted support, not unit selection |
| `identity-radian` / `c = 1` | explicit target wall |
| `native U(1)` | phase periodicity support, not selected-line value |
| `period-1-rad` | explicit residual, not hidden convention adoption |
| `registered` | realized-state discipline, not universal selector |
| `primitive` | registry checked; approved primitives supply no shortcut |
| `PDG` / `observed` / `fitted` | comparator data, excluded |

No exact value, unit coefficient, owner decision, audit decision, primitive
shortcut, or comparator input is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| R-eta readout-retirement target | h-unit input inside `R_ETA_READOUT_IDENTIFICATION_RETAINED` | h-unit target | yes |
| R-eta narrowing note | `A_R-eta` split into h-class plus h-unit | h-unit target | yes |
| defect identity-unit obstruction | `c = 1` unit selector and rescale wall | h-unit target | yes |
| A1 radian bridge audit | Type-B rational-to-radian observable law | h-unit period-normalization residual | yes |
| Z3 qubit radian bridge no-go | pure rational to literal radian bridge | h-unit period-normalization residual | yes |
| Brannen convention isolation | finite `2/9` weight versus bare-radian assignment | h-unit residual | yes |
| native phase-unit boundary | phase periodicity without selected value | support only | yes |
| primitive registry notes | primitive boundary | no shortcut primitive | yes |

### N5 - Rhetoric Audit

The negative phrase is narrow: "h-unit is not retained here."

| resolution | tested? | outcome |
|---|---:|---|
| finite additive normal form | yes | support only |
| count normalization | yes | wrong member or restatement |
| angle-side rigidity | yes | support only |
| Type-B-to-radian bridge | yes | target |
| h-class | kept separate | still open |
| R-eta readout retirement | kept separate | still downstream |
| K2/electron mass/hydrogen | kept separate | still downstream |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained angle-native source theorem producing the charged-lepton phase directly as `2/9` radians | `IDENTITY_UNIT_SELECTION_THEOREM_RETAINED` |
| retained rescale-breaking readout theorem pinning singleton value `I({D}) = L` without restating it | `IDENTITY_UNIT_SELECTION_THEOREM_RETAINED` |
| owner/audit acceptance of this packet after a selection theorem exists | `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED` |
| R-eta readout-retirement packet acceptance after h-class and h-unit are both supplied | `R_ETA_READOUT_IDENTIFICATION_RETAINED` |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that the defect identity-unit note already does
most of the h-unit work: the normal form is fixed, the angle side is rigid, the
wrong count shortcut is excluded, and the residual is localized to one
coefficient. That is strong support. The boundary is that localization is not
selection: the retained surface still does not prove the coefficient is exactly
`c = 1`, and the A1/Z3 radian rows keep the period-normalization bridge open.

### N8 - Cross-Cycle Echo

This echoes the exact-source `1/256` and R-eta retirement lanes: once a large
admission is narrowed to a named atom, the right next move is a target packet
with owner/audit gates and comparator exclusion. It is not a new primitive, and
it is not retained until accepted.

**Gate result:** broad h-unit-retained claim fails; narrowed identity-radian
target discriminator passes.

## Explicit Non-Claims

- No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.
- No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.
- No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.
- No derivation of R-eta from the current retained inventory alone.
- No derivation of `delta = 2/9` as a retained physical phase.
- No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.
- No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.
- No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed
  `m_e`, observed `alpha(0)`, or observed hydrogen as proof input.
- No derivation of K1 occupancy/counting, K3 physical species bridge, K4
  absolute scale, physical electron mass, `alpha(0)`, or hydrogen.
- No new axiom, primitive, Tier-A admission, or empirical import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_r_eta_h_unit_identity_radian_target_discriminator.py
```

The verifier checks the h-unit target contract, source boundaries, primitive
registry boundary, downstream R-eta/K2/electron-mass/hydrogen separation,
no-go discipline markers, and explicit non-claims.
