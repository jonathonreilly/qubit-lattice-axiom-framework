# Zero-Import Hydrogen: R-Lep Thresholds Ratification Decision Packet

**Date:** 2026-07-05
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify charged-lepton
thresholds, does not derive `alpha(0)`, does not derive `m_e`, and does not
claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_r_lep_thresholds_ratification_decision_packet.py`

## Purpose

The Lane 2 alpha0 transport packet consumes one charged-lepton threshold
input:

```text
R_LEP_THRESHOLDS_RETAINED.
```

The charged-lepton mass-spectrum packet can conditionally supply the physical
`e`, `mu`, `tau` mass triple and species labels. The R-Lep threshold-moment
map packet can conditionally supply the one-loop log-threshold map. Neither
packet by itself gives alpha0 transport a spendable charged-lepton threshold
handoff.

This packet packages the parent R-Lep threshold handoff as a separate
owner/audit decision object. It is downstream of the mass-spectrum and
threshold-map packets, and upstream of alpha0 transport.

## Decision Object

The decision object is exactly:

```text
the charged-lepton threshold handoff consumed by the zero-import alpha0
transport lane.
```

It has six clauses:

| clause | decision text |
|---|---|
| RL.1 | high-scale interface: threshold logs are referenced to the retained `alpha_EM(M_Z)` context used by alpha0 transport |
| RL.2 | physical mass content: the physical `e`, `mu`, `tau` mass triple is retained without PDG mass proof input |
| RL.3 | physical species labels: the retained masses are labeled as `e`, `mu`, and `tau`, not only an unordered Koide branch triple |
| RL.4 | threshold-moment map: the accepted one-loop map sends the retained mass triple to `T_lep` |
| RL.5 | scale-reference boundary: the approved scale-reference primitive is used only as units conversion after dimensionless mass content is retained |
| RL.6 | comparator exclusion: observed lepton masses, fitted effective thresholds, observed `alpha(0)`, Rydberg, and hydrogen lines are not proof inputs |

The object deliberately excludes the QED loop kernel, heavy-quark thresholds,
hadronic vacuum polarization, scheme/decoupling matching, low-energy
`alpha(0)`, physical electron readout, static-source Rydberg, and final
hydrogen.

## Ratification Decision Contract

This packet is decision-ready only if all eleven contract inputs are visible:

```text
R_LEP_THRESHOLDS_TEXT_LOCK
ALPHA_MZ_SCALE_CONTEXT_RETAINED
PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED
PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED
LEPTON_THRESHOLD_MOMENT_MAP_RETAINED
SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED
NO_PDG_LEPTON_MASS_PROOF_INPUT
NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The contract means:

1. **R_LEP_THRESHOLDS_TEXT_LOCK:** the RL.1-RL.6 text above is the full object
   being decided.
2. **ALPHA_MZ_SCALE_CONTEXT_RETAINED:** the threshold logs are referenced to
   the retained high-scale coupling context, not to a fitted effective scale.
3. **PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED:** the physical-unit mass
   content for `e`, `mu`, and `tau` is retained without PDG mass proof input.
4. **PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED:** the three masses are
   identified with the physical charged-lepton species rather than only an
   unordered branch witness.
5. **LEPTON_THRESHOLD_MOMENT_MAP_RETAINED:** the map from retained physical
   masses to the leptonic threshold moment is accepted for the alpha0 lane.
6. **SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED:** the approved
   scale-reference primitive is used only for units conversion after
   dimensionless mass content is retained.
7. **NO_PDG_LEPTON_MASS_PROOF_INPUT:** observed lepton masses are not proof
   inputs on the zero-import branch.
8. **NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT:** observed `alpha(0)`,
   Rydberg spectroscopy, fitted thresholds, and hydrogen lines are not proof
   inputs.
9. **NO_NEW_PRIMITIVE_OR_AXIOM:** the decision does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
10. **OWNER_RATIFICATION:** the owner explicitly accepts the R-Lep threshold
    boundary or retained theorem boundary.
11. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the R-Lep
    handoff and its dependency consequences.

No proper subset of those eleven contract inputs is a retained R-Lep
threshold handoff.

## Conditional Consequence

If all eleven contract inputs are accepted, the conditional consequence is:

```text
R_LEP_THRESHOLDS_RETAINED
T_LEP_THRESHOLD_MOMENT_RETAINED.
```

That consequence is Lane 2 support only. It does not by itself supply
`QED_LOOP_KERNEL_RETAINED`, `R_Q_HEAVY_THRESHOLDS_RETAINED`,
`R_HAD_NP_RETAINED`, `SCHEME_DECOUPLING_MATCHING_RETAINED`,
`ALPHA0_TRANSPORT_RETAINED`, `ALPHA0_RETAINED`,
`RETAINED_ALPHA0_LOW_ENERGY_COULOMB`, physical electron mass,
static-source Rydberg, or retained hydrogen.

## Finite Threshold Witness

The charged-lepton QED weights are:

```text
N_c(e) Q_e^2 = 1
N_c(mu) Q_mu^2 = 1
N_c(tau) Q_tau^2 = 1
sum_l N_c(l) Q_l^2 = 3
b_lep = (4/3) * 3 = 4.
```

The one-loop charged-lepton threshold moment is:

```text
T_lep(M_Z; m_e,m_mu,m_tau)
  = log(M_Z / m_e) + log(M_Z / m_mu) + log(M_Z / m_tau)
  = log(M_Z^3 / (m_e m_mu m_tau)).
```

For a common lepton threshold `m_*`, this agrees with the
common-threshold beta-coefficient form:

```text
(2/(3*pi)) * 3 log(M_Z/m_*) = (b_lep/(2*pi)) log(M_Z/m_*).
```

Moving any one mass changes `T_lep`. Rescaling `M_Z`, `m_e`, `m_mu`, and
`m_tau` together leaves `T_lep` unchanged. At one loop the three lepton
weights are equal, so the numeric sum is permutation-invariant, but the
zero-import handoff still requires physical species labels so an unordered
branch witness cannot be spent as physical thresholds.

This finite witness is not a mass derivation, a threshold-value derivation,
or an `alpha(0)` calculation.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was written.
The queue signal here is that a PR is open and lane-relevant; clean/green
status is not a prerequisite because reviewer cleanup and landing happen
outside this packet. No currently open PR supplies the R-Lep threshold
handoff:

| PR | queue signal | effect on this R-Lep packet |
|---|---:|---|
| `#5033` reflection-positivity runner-scope cleanup | open | mechanical/scoping cleanup; no charged-lepton thresholds |
| `#5030` finite multisite Pauli carrier provenance | open | carrier-provenance support; no R-Lep threshold handoff |
| `#5021` primitive-retirement review | open draft | no registry edit and no R-Lep primitive shortcut |
| `#5018` domain-wall edge content vs SM chiral map | open | chirality/domain-wall context; no charged-lepton thresholds |
| `#5017` domain-wall anomaly inflow spectral flow | open | chirality/domain-wall context; no alpha0 R-Lep closure |
| `#5016` zero-import hydrogen retained lane bundle | open | carries this support packet if merged; not an owner/audit-retained R-Lep consequence by itself |
| `#5015` wave-collapse-block01 measurement-collapse gate | open draft | measurement/collapse work; no charged-lepton thresholds |
| `#5014` record-formation front/domain-wall chirality | open | chirality context; no charged-lepton thresholds |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no R-Lep threshold package |
| `#5007` Koide native zero-section route guard repair | open | useful native-route context, not a retained charged-lepton threshold spectrum |
| `#4991` owner-governed Tier-A retirement | open | status progress for old atoms; no charged-lepton threshold theorem |

Merge-state labels, branch ordering, and check status are moving review
metadata, not proof inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary and eleven-input future contract | no retained R-Lep consequence |
| `ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional physical `e`, `mu`, `tau` mass triple and labels | no threshold-moment map or R-Lep closure |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional one-loop log-threshold map | no physical mass spectrum or R-Lep closure |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | downstream alpha0 consumer contract | consumes `R_LEP_THRESHOLDS_RETAINED`; does not derive it |
| `ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md` | QED loop-kernel boundary | independent from charged-lepton thresholds |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | selected electron-mass handoff | not full `e`, `mu`, `tau` thresholds |
| `SCALE_REFERENCE_PRIMITIVE_NOTE.md` | physical-unit conversion primitive | zero dimensionless threshold content |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation | no R-Lep thresholds primitive, threshold-map primitive, mass-spectrum primitive, alpha0 primitive, or hydrogen primitive |

The primitive registry was checked with the current origin-main methodology.
Registered primitives are approved premise nodes, but no primitive supplies an
R-Lep thresholds primitive, a lepton threshold-moment primitive, a
charged-lepton mass-spectrum primitive, an alpha0 primitive, or a hydrogen
primitive.

## What This Moves

| before this packet | after this packet |
|---|---|
| R-Lep had a current-surface no-go and two child handoff packets | the parent `R_LEP_THRESHOLDS_RETAINED` handoff has an eleven-input owner/audit decision contract |
| mass-spectrum closure could be overread as R-Lep closure | the parent packet requires both mass-spectrum and threshold-map consequences |
| threshold-map closure could be overread as R-Lep closure | the parent packet requires physical masses, labels, high-scale context, and anti-comparator gates |
| R-Lep could be overread as alpha0 closure | the packet keeps QED loop, heavy-quark, hadronic, and scheme/matching inputs downstream |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "charged-lepton thresholds
are retained" is not shipped. The narrowed claim is:

```text
the R-Lep threshold handoff is packaged as a decision-ready ratification
contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full R-Lep contract | Accept all eleven contract inputs. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts `R_LEP_THRESHOLDS_RETAINED`. |
| mass-spectrum-only route | Treat the physical mass triple and species labels as already supplying R-Lep. | ATTEMPTED. The threshold-moment map, high-scale context, and anti-comparator gates are still inputs. |
| threshold-map-only route | Treat the log-threshold functional as R-Lep closure. | ATTEMPTED. The map needs retained physical masses and labels before it can be spent. |
| electron-mass-only route | Use retained `m_e` as the whole charged-lepton threshold contribution. | ATTEMPTED. R-Lep also needs `mu`, `tau`, and the full threshold moment. |
| charge/count-only route | Treat `b_lep = 4` as the threshold moment. | ATTEMPTED. Weights do not supply logarithms. |
| QED-loop route | Retain the QED loop kernel and call the lepton thresholds closed. | ATTEMPTED. The loop kernel is independent from threshold masses and threshold placement. |
| comparator route | Fit thresholds to observed lepton masses, observed `alpha(0)`, Rydberg, or hydrogen lines. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is target data, not proof input. |
| primitive shortcut | Treat approved primitives as already supplying R-Lep. | RULED OUT. The registry supplies no R-Lep, mass-spectrum, threshold-map, alpha0, or hydrogen primitive. |
| open-PR shortcut | Treat the currently opened PR surface as R-Lep closure. | ATTEMPTED. The refreshed open PRs do not supply an owner/audit-retained R-Lep consequence. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| high-scale context <-> physical mass triple | no in either direction | independent |
| physical mass triple <-> physical species labels | no in either direction on current surface | independent |
| mass-spectrum handoff <-> threshold-moment map | no in either direction | independent |
| threshold-moment map <-> high-scale context | no in either direction | independent |
| scale-reference chain <-> dimensionless threshold values | no in either direction | independent |
| comparator exclusion <-> owner ratification | no in either direction | independent |
| owner ratification <-> audit acceptance | no in either direction | independent |

The collapsed decision wall is exactly the eleven-input contract above.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `threshold` / `running` | explicit R-Lep input, not background |
| `M_Z` / high-scale context | explicit scale-context input |
| `charged-lepton mass triple` | explicit mass-spectrum input |
| `species labels` | explicit physical-label input |
| `standard QED` / `one-loop` | map scope only until owner/audit acceptance |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `observed` / `PDG` / `fitted` / `Rydberg` | excluded as proof input |

No lepton mass, species label, reference scale, threshold logarithm,
comparator value, primitive, or audit rule is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| R-Lep current-surface no-go | `R_LEP_THRESHOLDS_RETAINED` is not supplied by current surfaces | parent R-Lep handoff | yes |
| mass-spectrum packet | physical `e`, `mu`, `tau` mass triple and labels | upstream R-Lep input | yes |
| threshold-map packet | one-loop threshold-moment map | upstream R-Lep input | yes |
| alpha0 transport packet | consumes `R_LEP_THRESHOLDS_RETAINED` | downstream consumer | yes |
| QED loop-kernel no-go | loop kernel is separate | independence guard | yes |
| physical electron mass packet | selected electron branch | partial Lane 6 support only | yes as guard |
| scale-reference primitive | units conversion only | no dimensionless threshold content | yes as guard |

Non-matching surfaces are not used as R-Lep closure evidence.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "this packet does not itself ratify
charged-lepton thresholds."

| resolution | tested? | result |
|---|---:|---|
| lepton charge/count weights | yes | gives weight `3`, not logs |
| electron mass alone | yes | incomplete for `mu` and `tau` |
| mass-spectrum handoff | yes | input only unless combined with map and gates |
| threshold-map handoff | yes | input only unless combined with masses and gates |
| full alpha0 transport | kept separate | still needs QED kernel, quark/hadron thresholds, and matching |

No universal no-go against future charged-lepton threshold retention is
claimed.

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| owner/audit acceptance of the charged-lepton mass-spectrum packet | `PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED` and `PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED` |
| owner/audit acceptance of the threshold-moment map packet | `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED` |
| owner/audit acceptance of this packet after all inputs are present | `R_LEP_THRESHOLDS_RETAINED` and `T_LEP_THRESHOLD_MOMENT_RETAINED` |
| explicit PDG lepton-mass admission | retained-with-import R-Lep route, not zero-import |
| later alpha0 transport packet after R-Lep plus other alpha inputs | `ALPHA0_TRANSPORT_RETAINED` and `ALPHA0_RETAINED` |

These are import-retirement paths, not automatic new axioms.

### N7 - Steelman

A hostile reviewer can argue that once the mass-spectrum packet and the
threshold-map packet are accepted, this parent packet is bookkeeping: the
R-Lep consequence follows by direct composition. The reply is that a
zero-import retained lane must name the composition point where alpha0 is
allowed to spend the child consequences, and that point still needs the
high-scale context, comparator exclusions, owner ratification, and audit
acceptance. This packet supplies that composition target without claiming the
child inputs have already landed.

### N8 - Cross-Cycle Echo

This mirrors the previous zero-import hydrogen ladder packets: child support
can be real without being spendable by the parent. The same import-retirement
mechanism applies here. Keep mass-spectrum and threshold-map support as child
inputs, then retire the parent R-Lep import only after the eleven-input
contract is accepted.

**Gate result:** broad charged-lepton-threshold retention is not shipped;
narrowed R-Lep ratification decision packet passes.

## Explicit Non-Claims

- No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.
- No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.
- No derivation or ratification of a physical charged-lepton mass triple.
- No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.
- No derivation or ratification of the physical charged-lepton species labels.
- No derivation or ratification of `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED`.
- No derivation or ratification of the QED loop kernel.
- No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.
- No derivation or ratification of `ALPHA0_RETAINED`.
- No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.
- No derivation of static-source Rydberg or retained hydrogen.
- No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or
  hydrogen spectroscopy as proof input.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.
