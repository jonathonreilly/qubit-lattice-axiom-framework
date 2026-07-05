# Zero-Import Hydrogen: Koide R-Eta Readout Retirement Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide R-eta import-retirement handoff
**Status:** support-only. This note does not derive R-eta, does not derive
`delta = 2/9`, does not ratify `R_ETA_READOUT_IDENTIFICATION_RETAINED`, does
not ratify `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`, does not ratify
`K2_R_ETA_EXACTNESS_RETAINED`, does not derive the physical electron mass, and
does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_readout_retirement_target_discriminator.py`

## Scope

Merged PR #5022 made the R-eta situation sharper: the delta-eta chain is
conditional on a declared supplied R-eta readout-identification premise. The
older R-eta narrowing note already decomposes that supplied premise into the
single admitted residual:

```text
A_R-eta = h-class + h-unit.
```

This discriminator names the hydrogen-facing import-retirement target for that
residual:

```text
R_ETA_READOUT_IDENTIFICATION_RETAINED.
```

It is a sub-lane under the two-ninths/radian-readout target, not a replacement
for it and not full K2 exactness.

## Target Contract

`R_ETA_READOUT_IDENTIFICATION_RETAINED` requires all eleven inputs:

```text
R_ETA_RETIREMENT_TEXT_LOCK
FORM_LAYER_AND_K_ORBIT_AUTHORITY_ACCEPTED
FINITE_FIXED_LOCUS_ARITHMETIC_ACCEPTED
PHYSICAL_CARRIER_CONTEXT_RETAINED
R_ETA_H_CLASS_RETAINED
R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED
NO_R_K1_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

No proper subset supplies the handoff.

| input | role |
|---|---|
| R_ETA_RETIREMENT_TEXT_LOCK | fixes the object as R-eta readout-identification retirement only |
| FORM_LAYER_AND_K_ORBIT_AUTHORITY_ACCEPTED | accepts the formal `H(delta)` form/value split and K-orbit sign/registrability layer |
| FINITE_FIXED_LOCUS_ARITHMETIC_ACCEPTED | accepts the retained finite `L3(1,2) = 2/9` arithmetic as arithmetic only |
| PHYSICAL_CARRIER_CONTEXT_RETAINED | proves the physical charged-lepton carrier realizes the supplied `H(delta)` readout context |
| R_ETA_H_CLASS_RETAINED | proves the registered `|delta|` is in the AB/Lefschetz fixed-locus density class of the realized `C3[111]` cycle |
| R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED | proves the identity-radian reading, i.e. unit coefficient 1, rather than a `q*pi`, count-normalized, or rescaled conversion |
| NO_R_K1_K3_K4_OR_MASS_INPUT | excludes occupancy/counting, species, absolute scale, branch mass-map, and electron-mass inputs |
| NO_COMPARATOR_PROOF_INPUT | excludes fitted `Phi_PDG`, fitted `delta`, observed lepton masses, observed `m_e`, observed `alpha(0)`, and observed hydrogen |
| NO_NEW_PRIMITIVE_OR_AXIOM | keeps this as import retirement rather than adding a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | owner accepts this as the R-eta readout-retirement object |
| AUDIT_ACCEPTANCE | independent audit accepts the target and dependency consequences |

If this handoff is later accepted, it is the intended proof package for two
inputs of the existing two-ninths/radian-readout target:

```text
DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED
RADIAN_READOUT_LICENSE_RETAINED
```

The two-ninths packet still owns its own text lock, fold/branch domain lock,
owner ratification, and audit acceptance. This target does not double-count an
independent wall.

The h-unit identity-radian target discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md`
packages one subinput of this contract:
`R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`. If accepted, it can supply the
identity-radian unit coefficient only; this packet still needs h-class,
physical carrier context, owner ratification, and audit acceptance before
`R_ETA_READOUT_IDENTIFICATION_RETAINED` is available.
The h-unit current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that the current surface does not supply that subinput.

The h-class fixed-locus target discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md`
packages the matching subinput:
`R_ETA_H_CLASS_RETAINED`. If accepted, it can supply fixed-locus
class-membership and the single fixed-point readout bridge only; this packet
still needs h-unit, owner ratification, and audit acceptance before
`R_ETA_READOUT_IDENTIFICATION_RETAINED` is available.
The h-class current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that the current surface does not supply that subinput.

## Current Surface

| surface | useful content | residual |
|---|---|---|
| merged `#5022` delta-eta audit repair | R-eta is explicit supplied premise; conditional implication is machine-checked | retained R-eta derivation absent |
| `ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md` | hydrogen-facing #5022 boundary | K2 conditionality only |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md` | target for `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`; identity-radian unit coefficient only | h-class, carrier context, owner/audit, and full R-eta retirement remain open |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current non-supply boundary for `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED` | identity-unit selection theorem and owner/audit remain open |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md` | target for `R_ETA_H_CLASS_RETAINED`; fixed-locus class membership only | h-unit, owner/audit, and full R-eta retirement remain open |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current non-supply boundary for `R_ETA_H_CLASS_RETAINED` | physical carrier, single fixed-point readout, and owner/audit remain open |
| `ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md` | decomposes R-eta into forced form layer plus `A_R-eta` | `A_R-eta` remains admitted, h-class plus h-unit |
| `ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md` | closes supplied finite-context registrability fragment | physical carrier realization and `A_R-eta` value remain open |
| `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md` | retained arithmetic plus R-eta conditional implication to `|delta| = 2/9` | R-eta is the named conditional input |
| `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md` | consolidates unit selector with R-eta and obstructs rescale shortcuts | identity-unit selector remains R-eta dependency |
| `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md` | normal form for cycle holonomy and delta representative | value wall remains R-eta in narrowed coordinates |
| `ACPHILAMBDA_CROSS_ARC_UNIT_CLASSIFICATION_WIRING_2026-07-02.md` | wires unit-classification arcs as context | no derivation of R-eta or `delta = 2/9` |
| `#5020` Koide R-eta value-face PR | value-face registration progress | exact readout retirement remains open |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation discipline | no phase selector, readout bridge, exact value, mass, alpha, or hydrogen |

The primitive registry was checked. The approved primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. They are premise nodes, not walls, but they do
not supply `R_ETA_READOUT_IDENTIFICATION_RETAINED`, h-class, h-unit, `delta =
2/9`, `m_e`, `alpha(0)`, or hydrogen.

## Hydrogen Effect

If accepted, this target moves the K2 branch by turning the #5022 supplied
premise into a retained readout-identification handoff. It would still be only
a Koide readout input. It would not derive K1 occupancy/counting, K3 physical
species, the native bridge, branch mass-map, K4 absolute scale, physical
electron mass, `alpha(0)`, static-source NR Coulomb limit, or retained
hydrogen.

The ratification decision wrapper for this target is
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md`.
It packages the same eleven-input contract for owner/audit handling and does
not claim the handoff is already retained.

The current-surface no-go companion
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `R_ETA_READOUT_IDENTIFICATION_RETAINED`; this target remains
needed.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "R-eta is retained" is not
shipped. The narrowed claim is:

```text
R_ETA_READOUT_IDENTIFICATION_RETAINED is the next import-retirement target
under the two-ninths/radian K2 subgate.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| #5022 supplied-premise route | Treat merged #5022's declared supplied premise as already retained. | ATTEMPTED. #5022 clarifies conditionality but says the premise is supplied, not derived. |
| forced form-layer route | Treat the formal `H(delta)` layer as selecting the value. | ATTEMPTED. The R-eta narrowing note says the form layer cannot select `A_R-eta`. |
| W2 registrability route | Treat finite Record-registrability context as physical carrier realization plus value selection. | PARTIAL ONLY. The W2 bridge closes finite-context algebra and leaves physical carrier plus `A_R-eta` open. |
| finite arithmetic route | Treat `L3(1,2) = 2/9` as the physical phase. | PARTIAL ONLY. Arithmetic is accepted context; h-class and h-unit remain the target. |
| unit-rescale route | Choose a conversion coefficient by count or rescaling. | RULED OUT BY PRIOR. The defect identity-unit obstruction consolidates this with R-eta and rejects count-normalized shortcuts. |
| value-face route | Use #5020 registered-angle standing as readout retirement. | PARTIAL ONLY. Value-face progress leaves exact readout retirement open. |
| comparator route | Use fitted `Phi_PDG`, fitted `delta`, or observed lepton masses. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |
| primitive shortcut | Treat approved primitives as supplying the phase selector. | ATTEMPTED. Registered primitives supply no selector, readout bridge, exact value, or mass. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| form/K-orbit layer <-> physical carrier context | no | independent |
| fixed-locus arithmetic <-> h-class | no | independent |
| h-class <-> h-unit | no | independent |
| h-unit <-> fold/branch domain lock | no | related but not identical; two-ninths packet owns domain lock |
| R-eta retirement <-> K2 value-face acceptance | no | independent K2 inputs |
| R-eta retirement <-> K1 occupancy/counting | no | independent downstream gate |
| R-eta retirement <-> K3 physical species bridge | no | independent downstream gate |
| R-eta retirement <-> K4 absolute scale | no | independent downstream gate |
| owner ratification <-> audit acceptance | no | independent |

The collapsed target wall set is: physical carrier context, h-class, h-unit,
owner ratification, and audit acceptance, with form and arithmetic as accepted
support inputs.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `supplied premise` | explicit import to retire, not a retained derivation |
| `forced form` | formal finite algebra support, not value selection |
| `registered` | realized-state discipline, not universal selector |
| `fixed-locus arithmetic` | finite arithmetic support, not physical readout |
| `identity-radian` / `unit` | explicit h-unit wall |
| `physical carrier` / `context` | explicit carrier-context wall |
| `primitive` | registry checked; approved primitives supply no shortcut |
| `PDG` / `observed` / `fitted` | comparator data, excluded |

No exact value, carrier realization, h-class, h-unit, owner decision, audit
decision, primitive shortcut, or comparator input is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| #5022 impact discriminator | supplied-premise conditionality boundary | target is premise retirement | yes |
| R-eta narrowing note | forced form layer vs `A_R-eta` residual | h-class/h-unit target | yes |
| W2 registrability bridge | supplied finite-context algebra | physical carrier plus `A_R-eta` still open | yes |
| delta-eta chain | conditional implication under R-eta | R-eta premise remains target | yes |
| defect identity-unit obstruction | unit selector shortcuts | h-unit remains same R-eta dependency | yes |
| cycle holonomy normal form | holonomy/delta normal coordinates | value wall remains R-eta | yes |
| #5020 value-face PR | registered-angle value face | not readout retirement | yes as guard |
| primitive registry notes | primitive boundary | no shortcut primitive | yes |

### N5 - Rhetoric Audit

The negative phrase is narrow: "R-eta is not retained here."

| resolution | tested? | outcome |
|---|---:|---|
| forced form layer | yes | support only |
| fixed-locus arithmetic | yes | support only |
| h-class | yes | target |
| h-unit | yes | target |
| two-ninths/radian subgate | kept separate | still needs packet-level domain/owner/audit |
| K2 exactness | kept separate | still downstream |
| physical electron mass | kept separate | still downstream |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained physical carrier/context realization | `PHYSICAL_CARRIER_CONTEXT_RETAINED` |
| retained proof that registered `|delta|` is the AB/Lefschetz fixed-locus density of the realized `C3[111]` cycle | `R_ETA_H_CLASS_RETAINED` |
| retained classification of identity-radian conversion coefficient 1 | `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED` |
| owner/audit acceptance of this packet | `R_ETA_READOUT_IDENTIFICATION_RETAINED` after all inputs are present |
| two-ninths/radian packet acceptance | spend this handoff into the K2 subgate |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that the combination of #5022, #5020, the formal
R-eta narrowing, the W2 bridge, and the cycle-holonomy/identity-unit campaign
has already made the R-eta premise effectively inert: the only remaining atom
is a naming convention for the value that the framework keeps rediscovering.
That is the strongest positive reading. The boundary is that the repo still
marks `A_R-eta` as admitted, separates h-class from h-unit, and has not owner
or audit accepted a retained physical readout-identification handoff.

### N8 - Cross-Cycle Echo

This echoes the lepton `1/256` and theta-retirement lanes: after a residual is
narrowed to a named atom, the next correct move is a retirement target with
explicit owner/audit gates. It is not a new primitive, and it is not a retained
result until that target is accepted.

**Gate result:** broad R-eta-retained claim fails; narrowed readout-retirement
target discriminator passes.

## Explicit Non-Claims

- No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.
- No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.
- No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.
- No derivation of R-eta from the current retained inventory alone.
- No derivation of `delta = 2/9` as a retained physical phase.
- No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.
- No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.
- No claim that PR `#5020`, PR `#5021`, or merged PR `#5022` supplies R-eta
  retirement.
- No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed
  `m_e`, observed `alpha(0)`, or observed hydrogen as proof input.
- No derivation of K1 occupancy/counting, K3 physical species bridge, K4
  absolute scale, physical electron mass, `alpha(0)`, or hydrogen.
- No new axiom, primitive, Tier-A admission, or empirical import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_r_eta_readout_retirement_target_discriminator.py
```

The verifier checks the target contract, R-eta source boundaries, primitive
registry boundary, downstream K2/electron-mass/hydrogen separation, no-go
discipline markers, and explicit non-claims.
