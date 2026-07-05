# Zero-Import Hydrogen: Koide R-Eta Physical Carrier Context Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide R-eta carrier-context import-retirement handoff
**Status:** support-only. This note does not ratify
`PHYSICAL_CARRIER_CONTEXT_RETAINED`, does not ratify
`R_ETA_H_CLASS_RETAINED`, does not ratify
`R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`, does not ratify
`R_ETA_READOUT_IDENTIFICATION_RETAINED`, does not derive the physical electron
mass, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_physical_carrier_context.py`

## Scope

The R-eta readout-retirement packet names a shared upstream input:

```text
PHYSICAL_CARRIER_CONTEXT_RETAINED.
```

This discriminator packages that input as its own target. The target is not
h-class fixed-locus membership, not h-unit identity-radian selection, not
single fixed-point readout, not K1/K3/K4, not a branch mass map, and not
hydrogen.

The target sentence is:

```text
the physical charged-lepton carrier realizes the supplied finite
AC_phi_lambda / R-eta C3 circulant readout context.
```

It is a context-realization handoff only. It does not decide which fixed-point
local density is physically read, does not select `c = 1`, and does not derive
`delta = 2/9`.

## Target Contract

`PHYSICAL_CARRIER_CONTEXT_RETAINED` requires all thirteen inputs:

```text
PHYSICAL_CARRIER_CONTEXT_TEXT_LOCK
SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED
RECORD_REGISTRABILITY_CONTEXT_ACCEPTED
REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED
CARRIER_GATE_COLLAPSE_MAP_ACCEPTED
CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED
NO_SINGLE_FIXED_POINT_READOUT_INPUT
NO_H_UNIT_OR_R_ETA_VALUE_INPUT
NO_K1_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

No proper subset supplies the handoff.

| input | role |
|---|---|
| PHYSICAL_CARRIER_CONTEXT_TEXT_LOCK | fixes the object as carrier-context realization only |
| SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED | accepts the supplied three-sector Hermitian circulant / `H(delta)` context as the target context |
| RECORD_REGISTRABILITY_CONTEXT_ACCEPTED | accepts W2 finite Record-registrability for the supplied context |
| REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED | records that reduced-carrier determinant algebra is support, not physical identification |
| CARRIER_GATE_COLLAPSE_MAP_ACCEPTED | records that carrier identification, readout gate, and zero-section/basepoint are one live gate, not three independent closures |
| CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED | supplies the missing theorem that the physical charged-lepton carrier realizes the supplied context |
| NO_SINGLE_FIXED_POINT_READOUT_INPUT | excludes the later theorem that the registered datum reads one fixed-point density |
| NO_H_UNIT_OR_R_ETA_VALUE_INPUT | excludes identity-radian unit selection, `A_R-eta`, and exact value selection |
| NO_K1_K3_K4_OR_MASS_INPUT | excludes occupancy/counting, physical species, absolute scale, branch mass map, and electron mass |
| NO_COMPARATOR_PROOF_INPUT | excludes observed lepton masses, fitted `delta`, observed `m_e`, observed `alpha(0)`, and observed hydrogen |
| NO_NEW_PRIMITIVE_OR_AXIOM | keeps this as import retirement rather than adding a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | owner accepts this carrier-context handoff |
| AUDIT_ACCEPTANCE | independent audit accepts the target and dependency consequences |

If accepted, this handoff supplies exactly:

```text
PHYSICAL_CARRIER_CONTEXT_RETAINED.
```

It can feed the R-eta readout-retirement and h-class fixed-locus packets, but
it still does not supply `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`,
`R_ETA_H_CLASS_RETAINED`, `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`,
`R_ETA_READOUT_IDENTIFICATION_RETAINED`, K2 exactness, electron mass, alpha, or
hydrogen.

The hw1 physical generation-locus target discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md`
packages one immediate subinput beneath
`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`. Its ratification packet
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md`
and current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md`
make clear that current surfaces do not supply
`HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.

## Current Surface

| surface | useful content | residual |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md` | target for `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED` | charged-lepton carrier realization theorem and physical carrier context remain open |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md` | hw1 locus owner/audit decision packet | no retained locus consequence unless accepted |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current non-supply boundary for `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED` | physical matter-state-law bridge and owner/audit remain open |
| `ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md` | closes the supplied finite-context Record-registrability algebra | physical charged-lepton carrier realization |
| `KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md` | blocks over-promoting reduced determinant algebra into physical carrier/readout identification | retained physical carrier/coarse-graining theorem |
| `FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md` | collapses readout gate, carrier identification, and zero-section/basepoint into one named gate | retained closure of that gate |
| `FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md` | blocks bare-character and equivariance-only carrier/basepoint shortcuts | physical carrier and basepoint remain open |
| `KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md` | proves exact finite facts for a supplied tracial standard-form carrier | framework-native physical carrier/scoring selection |
| `KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md` | localizes carrier-locus imports and the Hodge-orientation bit | physical matter operator/locus realization |
| `CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md` | refutes the spinor-module escape and locates the live KS/physical-state-law route | retained physical-state-law bridge |
| merged `#5023` Koide W4 audit-readiness repairs | dependency hygiene for record/species/custody/hw-complement surfaces | physical carrier-context theorem |
| open `#5024` Koide W4 gate-note premise minimization and substep1 rebase | `AC_phi_lambda` gate-readiness and substep1 hygiene | physical carrier-context theorem |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation discipline | carrier selector, physical readout context, value, mass, alpha, or hydrogen |

The primitive registry was checked. The approved primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. They are premise nodes, not walls, but their
source notes do not supply `PHYSICAL_CARRIER_CONTEXT_RETAINED`,
`SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`, h-class, h-unit, R-eta, `m_e`,
`alpha(0)`, or hydrogen.

The companion current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `PHYSICAL_CARRIER_CONTEXT_RETAINED`. This target remains a positive
import-retirement route, not a retained consequence.

## Hydrogen Effect

If accepted, this target retires one shared R-eta carrier-context input. It
would move both the full R-eta readout-retirement packet and the h-class
fixed-locus packet closer to decision-readiness. Hydrogen would still need the
single fixed-point readout theorem, h-class owner/audit acceptance, h-unit,
full R-eta owner/audit acceptance, two-ninths/radian and K2 exactness, K1, K3,
K4, physical electron mass, `alpha(0)`, and the static-source NR Coulomb
limit.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim
"physical carrier context is retained" is not shipped. The narrowed claim is:

```text
PHYSICAL_CARRIER_CONTEXT_RETAINED is the next shared import-retirement target
for the Koide R-eta and h-class lanes.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full carrier-context contract | Accept all thirteen contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| W2 registrability route | Treat supplied finite-context Record-registrability as physical carrier realization. | PARTIAL ONLY. W2 closes supplied context algebra, not physical realization. |
| reduced-carrier determinant route | Treat reduced determinant algebra and `D_red = I_2` as the physical charged-lepton carrier. | RULED OUT BY PRIOR. The reduced-carrier obstruction leaves the physical carrier/readout bridge open. |
| readout-gate collapse route | Treat the gate-collapse map as closure. | PARTIAL ONLY. It identifies one gate; it does not retain it. |
| tracial standard-form route | Treat the supplied tracial carrier as framework-native physical selection. | PARTIAL ONLY. It proves supplied-carrier algebra and leaves physical scoring/carrier selection open. |
| carrier-locus route | Treat finite Hamming-shell bookkeeping as physical locus selection. | PARTIAL ONLY. The physical matter operator/locus realization and Hodge bit remain open. |
| W4 PR route | Treat #5023/#5024 audit-readiness repairs as physical carrier closure. | ATTEMPTED. They improve dependency readiness but do not supply the charged-lepton carrier realization theorem. |
| primitive shortcut | Treat approved primitives as supplying carrier context. | ATTEMPTED. Registered primitives supply no carrier selector, physical readout context, value, mass, alpha, or hydrogen. |
| comparator route | Use observed lepton or hydrogen data. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| supplied context registrability <-> physical carrier realization | no | W2 algebra does not prove Nature realizes that context |
| physical carrier context <-> single fixed-point readout | no | carrier realization does not choose the readout functional |
| physical carrier context <-> h-class | no | h-class also needs fixed-locus class membership and readout theorem |
| physical carrier context <-> h-unit | no | carrier realization does not select the identity-radian coefficient |
| physical carrier context <-> K3 physical species bridge | no | R-eta carrier context is not the downstream electron-species bridge |
| owner ratification <-> audit acceptance | no | independent |

The collapsed target wall set is the retained charged-lepton carrier
realization theorem, owner ratification, and audit acceptance, with W2,
reduced-carrier obstruction, gate-collapse, tracial, locus, and W4 surfaces as
support rather than closure.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `supplied context` / `Record-registrable` | algebraic support, not physical realization |
| `physical charged-lepton carrier` | explicit target wall |
| `reduced carrier` / `D_red = I_2` | support plus obstruction, not physical identification |
| `single gate` / `zero-section` | gate localization, not retained closure |
| `tracial standard form` | supplied finite carrier support, not physical selection |
| `registered` / `realized-state` | evaluation discipline or data classification, not selector |
| `primitive` | registry checked; approved primitives supply no shortcut |
| `open PR` / `audit success` / `audit in progress` | queue/status signal only |
| `observed` / `fitted` | comparator data, excluded |

No carrier selector, physical realization theorem, owner decision, audit
decision, primitive shortcut, or comparator input is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| W2 registrability bridge | supplied finite-context Record-registrability | physical carrier realization still open | yes |
| reduced-carrier obstruction | physical reduced carrier/readout and `D_red = I_2` normalization | physical carrier context | yes |
| gate-collapse map | readout/carrier/basepoint as one gate | retained closure of that gate | yes |
| bare-character carrier note | bare character and equivariance shortcuts | physical carrier/basepoint still open | yes |
| tracial standard-form note | supplied finite carrier algebra | physical carrier/scoring selection | yes |
| carrier-locus decomposition | matter operator and orientation residuals | physical carrier realization | yes |
| chirality-gate sharpening | spinor-module escape and KS route boundary | retained physical-state-law bridge | yes |
| #5023/#5024 | W4/gate dependency readiness | no physical carrier theorem | yes |
| primitive registry | primitive boundary | no shortcut primitive | yes as guard |

Non-matching surfaces are not used as carrier-context closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "this target does not retain physical carrier
context here."

| resolution | tested? | outcome |
|---|---:|---|
| supplied finite C3/circulant algebra | yes | support only |
| Record registrability | yes | support only |
| reduced determinant carrier | yes | obstruction/support only |
| gate-collapse map | yes | localization only |
| physical charged-lepton realization | yes | target |
| single fixed-point readout | kept separate | still separate |
| h-class / h-unit / R-eta | kept separate | still downstream |
| K2/electron mass/hydrogen | kept separate | still downstream |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained theorem that the physical charged-lepton carrier realizes the supplied AC_phi_lambda/R-eta C3 circulant context | `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED` |
| retained coarse-graining/source-unit theorem connecting the physical carrier to the reduced scalar carrier without importing comparator data | part of the carrier realization theorem |
| retained KS/physical-state-law bridge that excludes the scalar lift on the relevant carrier route | carrier-locus support input |
| owner/audit acceptance of this packet after the realization theorem exists | `PHYSICAL_CARRIER_CONTEXT_RETAINED` |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that the physical carrier context is close:
W2 closes supplied-context registrability, the reduced-carrier obstruction
names the exact missing bridge, the readout-gate map collapses duplicate gates,
the tracial standard-form carrier supplies strong finite algebra, and #5023/#5024
improve W4 gate readiness. That is real progress. The boundary is that none of
those surfaces proves the physical charged-lepton carrier realizes the supplied
C3/circulant context; they locate the target rather than retain it.

### N8 - Cross-Cycle Echo

This echoes earlier carrier/readout walls that were narrowed from "many
obstacles" to one import-retirement target. The mechanism that can retire this
wall is a retained carrier-realization theorem plus owner/audit acceptance, not
a new primitive and not a comparator fit.

**Gate result:** broad physical-carrier-retained claim fails; narrowed
carrier-context target passes.

## Explicit Non-Claims

- No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.
- No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.
- No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.
- No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.
- No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.
- No derivation of `delta = 2/9` as a retained physical phase.
- No derivation of the physical electron species bridge, branch mass map,
  physical electron mass, `alpha(0)`, or hydrogen.
- No new axiom, primitive, Tier-A admission, empirical import, or audit status
  change.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_r_eta_physical_carrier_context.py
```
