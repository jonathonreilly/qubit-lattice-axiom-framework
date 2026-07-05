# Zero-Import Hydrogen: Koide R-Eta Exactness Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify Koide K2 exactness, does
not derive `delta = 2/9`, does not derive the physical electron mass, does
not derive `alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_exactness_current_surface_no_go.py`

## Scope

The Koide/electron-readout lane now has an explicit K2 target:

```text
K2_R_ETA_EXACTNESS_RETAINED.
```

The target discriminator packages that handoff as a ten-input owner/audit
contract. The narrow result here is not "K2 exactness cannot be retained."
The narrow result is that current retained, primitive, merged-PR, and open-PR
surfaces do not supply `K2_R_ETA_EXACTNESS_RETAINED`.

## Exactness Contract

A future K2 exactness handoff needs all ten inputs:

```text
K2_EXACTNESS_TEXT_LOCK
REGISTERED_PHI_VALUE_FACE_ACCEPTED
DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED
RADIAN_READOUT_LICENSE_RETAINED
FOLD_AND_BRANCH_DOMAIN_LOCK
NO_K1_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If all ten inputs are accepted, the conditional consequence would be:

```text
K2_R_ETA_EXACTNESS_RETAINED.
```

That consequence is not supplied here. The current missing inputs include:

```text
REGISTERED_PHI_VALUE_FACE_ACCEPTED
DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED
RADIAN_READOUT_LICENSE_RETAINED
FOLD_AND_BRANCH_DOMAIN_LOCK
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The K2 R-eta exactness ratification decision packet
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the same ten-input owner/audit contract. It is not accepted on the
current surface and is not a retained consequence here.

The #5020 value-face PR is the closest live lane movement, but it explicitly
names exactness as residual. It can become one target input after adoption or
a successor review, not the full K2 exactness handoff.

The #5022 audit-repair PR has merged with audit success. It repairs the
delta-eta chain by treating R-eta as a declared supplied readout-identification
premise and reusing retained K-orbit form authority. That is useful landed
conditional machinery, but it is not a retained theorem deriving R-eta. The
dedicated impact discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md`
records the hydrogen-facing boundary.

The AC R-eta upstream cluster impact discriminator
`ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md`
records the 2026-07-05 `origin/main` R-eta cluster: `#4982` through `#4986`
were closed as PRs but their science commits landed on `main`, while `#4981`
remains open and lane-relevant. The later landed-main commits `89768b461c`
and `e2d1dec095` also prune the occurrence-axiom and measure-binary shortcuts.
The cluster sharpens h-class/h-unit, doublet-clock, occurrence, and measure
residuals; it does not supply `K2_R_ETA_EXACTNESS_RETAINED`.

The R-eta readout-retirement target discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md`
is the positive import-retirement path for the supplied R-eta premise. It
packages `R_ETA_READOUT_IDENTIFICATION_RETAINED` as h-class plus h-unit, and
if accepted can feed the exact theorem and radian-readout license inputs under
the two-ninths/radian subgate. It is not supplied on the current surface.

The R-eta readout-retirement current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `R_ETA_READOUT_IDENTIFICATION_RETAINED`.

The two-ninths/radian-readout target discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md`
packages the next sub-lane as
`KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`: exact pure `2/9` theorem,
radian-readout license, fold/branch domain lock, comparator exclusion, owner
ratification, and audit acceptance. It is a subtarget, not a retained result.

The two-ninths/radian-readout ratification decision packet
`ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages that subtarget as a nine-input owner/audit contract. It is still a
decision object, not a current retained K2 consequence.

The two-ninths/radian-readout current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that the current retained, primitive, merged-PR, and open-PR surfaces
do not supply `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md` | target for `R_ETA_READOUT_IDENTIFICATION_RETAINED`; h-class plus h-unit | current retained R-eta derivation or K2 exactness |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current non-supply boundary for `R_ETA_READOUT_IDENTIFICATION_RETAINED` | R-eta consequence or K2 exactness |
| `ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md` | landed-main/open-PR AC R-eta cluster boundary for #4981-#4986 plus `89768b461c`/`e2d1dec095` | h-class, h-unit, R-eta retirement, K1/K2 closure, electron mass, or hydrogen |
| `ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md` | #5022 supplied-premise conditionality boundary | retained R-eta derivation, `K2_R_ETA_EXACTNESS_RETAINED`, or hydrogen |
| `#5022` audit repair for the delta-eta chain | merged conditionality repair: R-eta as declared supplied readout-identification premise plus retained K-orbit form authority | retained R-eta derivation, `K2_R_ETA_EXACTNESS_RETAINED`, or two-ninths/radian handoff |
| `#5020` Koide R-eta value-face PR | merged value-face movement: registered-angle functional, counterfactual classification, law-freeness, unit-face dissolution, and named exactness residual | retained exact `2/9` theorem, radian-readout license, owner/audit acceptance |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md` | hydrogen-facing boundary for #5020 | `K2_R_ETA_EXACTNESS_RETAINED` |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md` | ten-input exactness target contract | current retained consequence |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_RATIFICATION_DECISION_PACKET_2026-07-05.md` | ten-input owner/audit decision packet | retained consequence; not accepted on the current surface |
| `ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md` | subtarget for exact `2/9`, radian readout, and fold/branch domain | current retained consequence |
| `ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md` | nine-input owner/audit decision packet for the subtarget | current retained consequence or full K2 exactness |
| `ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current non-supply boundary for `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED` | retained consequence |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md` | K1/K2/K3/K4 separation and phase-sensitive arithmetic | K2 exactness closure or physical electron mass |
| `LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md` | comparator/open-gate warning for `delta = 2/9` | retained phase/exactness theorem |
| `CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md` | bounded theorem under explicit Tier-A admission | zero-import K2 exactness from retained inventory alone |
| `#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged premise-hygiene and audit-readiness context | exactness theorem or electron mass |
| `#5021` primitive-retirement review draft | open/draft primitive meta review; reports no primitive retirement and no registry edit | K2 exactness, new primitive, or hydrogen closure |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | `Phi`, `delta`, exactness theorem, radian-readout license, species, scale, mass, `alpha(0)`, or hydrogen |

The primitive registry was checked. The registered primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. They are approved premise nodes, not walls,
but no registered primitive supplies `K2_R_ETA_EXACTNESS_RETAINED`,
`REGISTERED_PHI_VALUE_FACE_ACCEPTED`,
`DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED`,
`RADIAN_READOUT_LICENSE_RETAINED`, `FOLD_AND_BRANCH_DOMAIN_LOCK`, `delta`,
`m_e`, `alpha(0)`, or hydrogen.

## Open PR Alignment

PRs were refreshed on 2026-07-05 UTC. Merged and opened lane-relevant PRs are
tracked as dependency-state signals; clean/green status is not a proof input.

| PR | queue signal | K2 exactness effect |
|---|---:|---|
| `#5022` audit repair: delta-eta chain R-eta supplied premise | merged, audit success | conditional repair only; no retained R-eta derivation or K2 exactness |
| `#5021` primitive-retirement review: meta gate map, no retirements | open draft | primitive-boundary context only; no registry edit, no K2 exactness |
| `#5020` Koide R-eta value-face registered-angle/exactness relocation | merged | value-face progress; exactness residual remains open |
| `#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged | premise-hygiene context; no exactness theorem |
| `#5018`/`#5017` chirality/domain-wall stack | open | above-C3 context only; no K2 exactness or electron mass |
| `#5016` zero-import hydrogen retained lane bundle | open | carries this current-surface no-go once pushed |

Merge-state labels, branch ordering, draft status, and check state are review
metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| K2 had a target contract but no current-surface non-supply boundary | the non-supply boundary is explicit |
| #5022 could be overread as deriving R-eta | #5022 is merged conditional supplied-premise repair, not a retained R-eta derivation |
| #5020 could be overread as exactness closure | #5020 is value-face progress only until exactness and readout inputs are accepted |
| primitive-retirement review could be overread as a shortcut | #5021 is primitive-boundary context only while open/draft and no-registry-edit |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "K2 exactness cannot be
retained" is not shipped. The narrowed claim is:

```text
the current retained, primitive, merged-PR, and open-PR surfaces do not supply
K2_R_ETA_EXACTNESS_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full K2 exactness contract | Accept all ten contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| #5022 supplied-premise route | Treat the audit repair as deriving R-eta. | ATTEMPTED. #5022 states R-eta as a declared supplied premise and checks conditional implication, not a retained derivation. |
| #5020 value-face route | Treat registered `Phi` standing as exactness. | ATTEMPTED. #5020 explicitly leaves exactness as residual. |
| exact `2/9` theorem route | Prove the distinguished registered value is exactly `2/9`. | OPEN POSITIVE ROUTE. No retained theorem is supplied on the current surface. |
| radian-readout route | License the pure number as charged-lepton `delta`. | OPEN POSITIVE ROUTE. The readout license remains a named input. |
| Tier-A conditional route | Use `AC_phi_lambda` bounded standing. | VALID CONDITIONAL, not zero-import from retained inventory alone. |
| primitive shortcut | Treat approved primitives or #5021 primitive review as already supplying K2 exactness. | ATTEMPTED. Registered primitives supply no phase, selector, exactness, or readout license; #5021 reports no registry edit. |
| physical electron route | Treat K2 exactness as `m_e`. | RULED OUT. K1, K3, native bridge, branch mass-map, K4 scale, owner, and audit remain separate. |
| empirical comparator route | Use fitted `Phi_PDG`, observed lepton masses, fitted `delta`, or closeness to `2/9`. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| value-face acceptance <-> exact `2/9` theorem | no | independent |
| exact `2/9` theorem <-> radian-readout license | no | independent |
| radian-readout license <-> fold/branch domain lock | no | independent |
| K2 exactness <-> K1 occupancy/counting | no | independent downstream gate |
| K2 exactness <-> K3 physical species bridge | no | independent downstream gate |
| K2 exactness <-> K4 absolute scale | no | independent downstream gate |
| owner ratification <-> audit acceptance | no | independent |

The collapsed wall is the ten-input exactness contract, with current pressure
on value-face acceptance, exactness theorem, readout license, domain lock,
owner ratification, and audit acceptance.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `registered Phi` | value-face data standing, not exactness |
| `2/9` | explicit theorem target or comparator, not a derived value here |
| `radian` / `delta` | explicit readout-license wall |
| `fold` / `branch` | explicit domain-lock wall |
| `primitive` | registry checked; approved primitives supply no exactness shortcut |
| `draft` / `open PR` | queue signal only, not proof authority |
| `observed` / `fitted` / `PDG` | comparator data, excluded |

No exact value, phase readout, domain convention, primitive shortcut,
comparator input, owner decision, or audit decision is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| R-eta readout-retirement target | positive h-class/h-unit import-retirement target | target only, no closure evidence | yes |
| #5022 audit-repair PR | conditional R-eta bookkeeping and retained K-orbit form authority | no retained R-eta derivation or audit acceptance | yes as guard |
| #5022 impact discriminator | hydrogen-facing #5022 boundary | no K2 or hydrogen closure evidence | yes |
| #5020 value-face PR | registered-angle/value-face classification | value-face input only | yes |
| #5020 impact discriminator | hydrogen-facing #5020 boundary | exactness remains residual | yes |
| K2 exactness target discriminator | ten-input exactness handoff | current consequence absent | yes |
| Koide electron-readout firewall | K1/K2/K3/K4 separation | prevents K2 from becoming mass | yes |
| Brannen delta open gate | comparator phase warning | prevents comparator exactness | yes |
| Tier-A bounded theorem | conditional admission route | not zero-import current-surface closure | yes as guard |
| primitive registry / #5021 draft | primitive status boundary | no shortcut primitive | yes as guard |

Non-matching surfaces are not used as exactness closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`K2_R_ETA_EXACTNESS_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| value-face registration | yes | support only |
| exact `2/9` theorem | yes | open |
| radian-readout license | yes | open |
| fold/branch domain lock | yes | open |
| primitive shortcut | yes | not supplied |
| physical electron mass | kept separate | still downstream |
| final hydrogen lane | kept separate | still needs `m_e`, `alpha(0)`, static-source NR Coulomb, harness, and audit |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| landed/audited #5020 or successor | `REGISTERED_PHI_VALUE_FACE_ACCEPTED` |
| accepted two-ninths/radian-readout subtarget | exact `2/9` theorem, radian-readout license, and fold/branch domain lock |
| retained exactness theorem | `DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED` |
| retained radian/readout license | `RADIAN_READOUT_LICENSE_RETAINED` |
| retained fold/branch domain convention | `FOLD_AND_BRANCH_DOMAIN_LOCK` |
| owner/audit acceptance of the target packet | `K2_R_ETA_EXACTNESS_RETAINED` after all inputs are present |

These are live import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that #5020 has already dissolved the hard part:
`Phi` is a registered-state functional, the unit-face concern is gone, and the
remaining numerical exactness residual is so small that the exact value should
be treated as the retained finite density already visible elsewhere in the
Koide stack. This is the strongest positive route. The boundary is that the
repo still distinguishes registered data, exactness theorem, and radian
readout license; current surfaces do not yet supply the owner/audit accepted
handoff.

### N8 - Cross-Cycle Echo

This echoes the exact-source `1/256` lane: finite arithmetic and cleaner
classification reduce the residual, but the result becomes spendable only
after the physical readout convention, comparator exclusion, owner acceptance,
and audit path are explicit. K2 exactness now has the same discipline.

**Gate result:** broad K2-exactness no-go fails; narrowed current-surface
non-supply claim passes.

## Explicit Non-Claims

- No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.
- No derivation or ratification of `REGISTERED_PHI_VALUE_FACE_ACCEPTED`.
- No derivation or ratification of `DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED`.
- No derivation or ratification of `RADIAN_READOUT_LICENSE_RETAINED`.
- No derivation or ratification of `FOLD_AND_BRANCH_DOMAIN_LOCK`.
- No claim that PR `#5020`, PR `#5021`, merged PR `#5022`, open PR `#4981`,
  landed-main `#4982`-`#4986`, or landed-main `89768b461c`/`e2d1dec095`
  supplies K2 exactness.
- No derivation of `AC_phi_lambda`, `delta = 2/9`, `rho_e(delta)`, or `a_l^2`.
- No derivation or ratification of K1 occupancy/counting, K3 physical species
  bridge, K4 absolute scale, native bridge, branch mass-map, or physical
  electron mass.
- No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`,
  observed `m_e`, observed `alpha(0)`, or observed Rydberg as proof input.
- No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_r_eta_exactness_current_surface_no_go.py
```

The verifier checks the current-surface boundary, exactness contract
predicate, primitive registry, open PR alignment, no-go discipline markers,
and explicit non-claims.
