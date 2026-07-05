# Zero-Import Hydrogen: Koide R-Eta Exactness Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide K2 exactness handoff
**Status:** support-only. This note does not ratify Koide K2 exactness, does
not derive `delta = 2/9`, does not derive the physical electron mass, and does
not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_exactness_target_discriminator.py`

## Scope

The open `#5020` value-face PR separates two pieces of Koide K2:

```text
registered Phi-value standing
exactness of the distinguished number
```

That separation is useful only if the second piece becomes an explicit target.
This discriminator defines the hydrogen-facing target for spending K2
exactness later without smuggling in comparator data, species identity, or
scale.

The target is not "Koide is true" in one undifferentiated phrase. It is the
specific retained handoff:

```text
K2_R_ETA_EXACTNESS_RETAINED.
```

## Target Contract

`K2_R_ETA_EXACTNESS_RETAINED` requires all ten inputs:

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

The clauses mean:

| clause | content |
|---|---|
| K2_EXACTNESS_TEXT_LOCK | the object being decided is only the R-eta exactness/readout part of K2 |
| REGISTERED_PHI_VALUE_FACE_ACCEPTED | the value-face registration from `#5020` or a landed successor is accepted as a lawful registered-state input |
| DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED | a retained theorem forces the distinguished registered value to the exact pure number `2/9` without using PDG lepton data |
| RADIAN_READOUT_LICENSE_RETAINED | the pure-number value is licensed as the charged-lepton `delta` phase rather than only a comparator density |
| FOLD_AND_BRANCH_DOMAIN_LOCK | the `Phi = (1/3) arccos(cos 3delta)` fold, branch, and nondegenerate-domain conventions are fixed without empirical selection |
| NO_K1_K3_K4_OR_MASS_INPUT | the K2 decision does not consume counting, physical species, absolute scale, branch mass-map, or electron-mass inputs |
| NO_COMPARATOR_PROOF_INPUT | observed lepton masses, fitted `delta`, fitted `Phi_PDG`, observed `m_W`, observed `m_e`, `alpha(0)`, and Rydberg data are excluded as proof inputs |
| NO_NEW_PRIMITIVE_OR_AXIOM | the decision does not add a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | the owner accepts this as the K2 exactness object |
| AUDIT_ACCEPTANCE | the normal independent review/audit path accepts the target and dependency consequences |

No proper subset of those ten inputs supplies K2 exactness.

The two-ninths/radian-readout target discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md`
packages the sub-handoff `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.
If ratified, it supplies the exact `2/9` theorem, radian-readout license,
and fold/branch domain-lock inputs for this K2 target, but not full K2
exactness by itself.

The two-ninths/radian-readout current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that the current retained, primitive, and open-PR surfaces do not
supply that sub-handoff.

The #5022 audit-repair PR is live conditional Koide progress: it declares
R-eta as a supplied readout-identification premise and checks the implication
from retained arithmetic to `|delta| = 2/9`. It is not a retained derivation of
R-eta, does not close this K2 exactness target, and does not supply the
two-ninths/radian-readout sub-handoff.

## Dependency Boundary

| object | if this target is accepted | still not supplied |
|---|---|---|
| K2 R-eta exactness | `K2_R_ETA_EXACTNESS_RETAINED` | K1 occupancy/counting |
| native Koide bridge | gains the K2 exactness input | Z1-Z3 native bridge acceptance still separate |
| physical electron readout | still blocked | K3 species bridge, branch mass-map, K4 scale |
| physical electron mass | still blocked | `NATIVE_ZERO_SECTION_BRIDGE_RETAINED`, `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`, `KOIDE_BRANCH_MASS_MAP_RETAINED`, `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED` |
| hydrogen | still blocked | retained `m_e`, retained `alpha(0)`, static-source NR Coulomb limit, harness, and audit |

This target can move the Koide K2 lane. It cannot close Lane 6 by itself.

## Current Surface Classification

| surface | classification |
|---|---|
| `#5020` value-face PR | K2 value-face progress; exactness residual named, not closed |
| `#5019` premise-hygiene PR | decomposition-chain context; no exactness theorem |
| approved primitives | premise discipline only; no `delta`, `Phi`, selector, mass, or hydrogen value |
| `LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md` | comparator/open-gate warning for `delta = 2/9` |
| Koide electron-readout firewall | K1/K2/K3/K4 separation; no mass closure |
| physical electron mass packet | downstream consumer after native bridge, species, branch map, scale, owner, and audit inputs |

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but no primitive supplies `K2_R_ETA_EXACTNESS_RETAINED`,
`delta = 2/9`, `m_e`, `alpha(0)`, or hydrogen.

## What This Moves

| before this note | after this note |
|---|---|
| #5020 exposed an exactness residual | the residual has an explicit ten-input target contract |
| K2 value registration could be overread as K2 closure | value-face standing and exactness are separated into spendable predicates |
| hydrogen had no named successor path for #5020 | the next K2 lane is `K2_R_ETA_EXACTNESS_RETAINED` |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the #5020 value-face
movement closes Koide K2" is not shipped. The narrowed claim is:

```text
K2 exactness is a named ten-input target after #5020, not a retained result.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| #5020 value-face route | Treat registered `Phi` standing as exact `2/9`. | ATTEMPTED. #5020 names exactness as residual, so value-face standing is insufficient. |
| retained exactness route | Require a theorem that the registered value is the distinguished pure number `2/9`. | TARGETED. This is the positive target, not supplied here. |
| radian-readout shortcut | Treat finite density `2/9` as charged-lepton phase without a readout license. | RULED OUT. The target requires `RADIAN_READOUT_LICENSE_RETAINED`. |
| comparator route | Use fitted `Phi_PDG`, observed lepton masses, or closeness to `2/9`. | RULED OUT. Comparator data is target data, not proof input. |
| primitive shortcut | Treat realized-state registration as value selection. | RULED OUT. The realized-state primitive supplies evaluation discipline, not state content or exact numbers. |
| electron-mass route | Treat K2 exactness as `m_e`. | RULED OUT. K3, native bridge, branch map, K4 scale, owner, and audit inputs remain separate. |
| hydrogen route | Treat K2 exactness as retained hydrogen. | RULED OUT. Hydrogen also needs retained `m_e`, retained `alpha(0)`, static-source NR Coulomb limit, harness, and audit. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| value-face registration <-> exactness theorem | no | independent |
| exactness theorem <-> radian-readout license | no | independent |
| K2 exactness <-> K1 occupancy/counting | no | independent |
| K2 exactness <-> K3 physical species bridge | no | independent |
| K2 exactness <-> K4 absolute scale | no | independent |
| K2 exactness <-> physical electron mass | no | independent downstream gate |
| K2 exactness <-> alpha(0) | no | independent |

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `registered Phi` | lawful data standing, not exactness |
| `2/9` | target exact pure number unless theorem supplied |
| `radian` / `delta` | readout-license wall |
| `fold` / `branch` | domain convention wall |
| `observed` / `fitted` / `PDG` | comparator data, excluded |
| `primitive` | premise discipline, not value selector |
| `owner` / `audit` | required retained-status gates |

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| #5022 audit-repair PR | conditional R-eta bookkeeping and retained K-orbit form authority | not retained R-eta derivation or K2 closure | yes as guard |
| `#5020` body | value-face registration and exactness split | value-face input only | yes |
| #5020 impact discriminator | hydrogen-facing K2 boundary | names exactness residual | yes |
| two-ninths/radian-readout target | K2 subgate for exact value, radian license, and domain lock | subtarget only | yes |
| two-ninths/radian-readout current-surface no-go | current non-supply boundary for `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED` | no closure evidence | yes |
| Koide electron-readout firewall | K1/K2/K3/K4 separation | K2 target only | yes |
| physical electron mass packet | downstream mass composition | guard only | yes |
| primitive registry notes | primitive boundary | guard only | yes |

The K2 exactness current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`K2_R_ETA_EXACTNESS_RETAINED`; the target remains needed.

### N5 - Rhetoric Audit

The negative phrase is narrow: "K2 exactness is not retained here."

| resolution | tested? | outcome |
|---|---:|---|
| value-face registration | yes | prerequisite only |
| exactness theorem | yes | target, not supplied |
| radian-readout license | yes | target, not supplied |
| physical electron mass | kept separate | still downstream |
| alpha/static-source hydrogen | kept separate | still downstream |

### N6 - Partial-Closure Path Scan

Legitimate follow-ups remain:

| path | what it could close |
|---|---|
| landed/audited #5020 or successor | value-face acceptance input |
| retained exactness theorem | `DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED` |
| retained radian/readout license | `RADIAN_READOUT_LICENSE_RETAINED` |
| owner/audit acceptance of this target | `K2_R_ETA_EXACTNESS_RETAINED` after all inputs are present |
| K1/K3/K4 packets | physical electron mass path after K2 is improved |

### N7 - Steelman

A strong positive reading is that #5020 leaves very little value-face work:
`Phi` is a functional of registered state data, unit-face concerns are removed,
and exact inversion is available on the nondegenerate stratum. That is real
progress. The remaining retained-status burden is the exactness theorem and
readout license, because hydrogen needs a spendable electron-mass dependency,
not only a cleaner classification of a Koide phase.

### N8 - Cross-Cycle Echo

This mirrors the source-side `1/256` work: a clean finite scaffold becomes
spendable only after the physical readout convention, comparator boundary,
owner acceptance, and audit path are explicit. K2 now has the same discipline.

**Gate result:** broad K2-closure claim fails; narrowed exactness target
discriminator passes.

## Explicit Non-Claims

- No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.
- No derivation of `AC_phi_lambda`.
- No derivation of `delta = 2/9`.
- No adoption or landing claim for PR `#5020` or PR `#5022`.
- No derivation or ratification of K1 occupancy/counting, K3 physical species
  bridge, K4 absolute scale, native Z1-Z3 bridge, or Koide branch mass-map.
- No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.
- No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_r_eta_exactness_target_discriminator.py
```

The verifier checks the target contract, #5020 boundary, primitive boundary,
downstream mass/hydrogen separation, and explicit non-claims.
