# Zero-Import Hydrogen: Charged-Lepton Mass-Spectrum Ratification Decision Packet

**Date:** 2026-07-05
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify the physical
charged-lepton mass spectrum, does not ratify R-Lep thresholds, does not derive
`alpha(0)`, does not derive static-source Rydberg, and does not claim hydrogen
is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_charged_lepton_mass_spectrum_ratification_decision_packet.py`

## Purpose

The R-Lep thresholds lane consumes two Lane 6 inputs:

```text
PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED
PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED.
```

The physical electron mass packet is electron-facing. It can conditionally
yield the single hydrogen input
`RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`, but R-Lep needs the full physical
`e`, `mu`, and `tau` mass triple plus species labels before the threshold
logs can be spent.

This packet packages that broader Lane 6 handoff as a decision object. It is a
sibling of the physical electron mass packet, not a replacement for it. It
does not ratify the spectrum; it records exactly what must be accepted before
R-Lep can consume a zero-import charged-lepton spectrum.

## Decision Object

The decision object is exactly:

```text
the physical charged-lepton mass-spectrum handoff for the zero-import hydrogen
R-Lep and Lane 6 lanes.
```

It has six clauses:

| clause | decision text |
|---|---|
| CLS.1 | native route bridge: the accepted native zero-section bridge supplies the phase/readout route without observed lepton masses as proof input |
| CLS.2 | branch-to-mass map: the accepted Koide/Brannen map composes branch amplitudes into masses |
| CLS.3 | full species labeling: all three branches are identified with physical `e`, `mu`, and `tau`, not only a selected electron branch |
| CLS.4 | absolute charged-lepton scale: the accepted K4 assembly supplies the common `a_l^2` scale on its own graph |
| CLS.5 | physical-unit scale reference: the approved scale-reference primitive is used only after dimensionless mass content is retained |
| CLS.6 | threshold boundary: this spectrum handoff remains upstream of R-Lep; the threshold-moment map and high-scale context are separate inputs |

The object deliberately excludes observed charged-lepton masses, fitted
`a_l`, fitted `delta`, fitted A3 precision, observed `alpha(0)`, Rydberg
spectroscopy, and hydrogen lines as proof inputs.

## Ratification Decision Contract

This packet is decision-ready only if all eleven contract inputs are visible:

```text
CHARGED_LEPTON_MASS_SPECTRUM_TEXT_LOCK
NATIVE_ZERO_SECTION_BRIDGE_RETAINED
KOIDE_BRANCH_MASS_MAP_RETAINED
FULL_CHARGED_LEPTON_SPECIES_LABELING_RETAINED
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED
SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED
NO_LEPTON_COMPARATOR_PROOF_INPUT
NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The contract means:

1. **CHARGED_LEPTON_MASS_SPECTRUM_TEXT_LOCK:** the CLS.1-CLS.6 text above is
   the full object being decided.
2. **NATIVE_ZERO_SECTION_BRIDGE_RETAINED:** the native Z1-Z3 route is accepted
   on its own graph.
3. **KOIDE_BRANCH_MASS_MAP_RETAINED:** the branch-to-mass composition
   `m_k = a_l^2 [1 + sqrt(2) cos(delta + 2 pi k / 3)]^2` is accepted without
   importing observed lepton masses.
4. **FULL_CHARGED_LEPTON_SPECIES_LABELING_RETAINED:** all three retained
   branches are physically labeled as `e`, `mu`, and `tau`. The existing K3
   physical electron species bridge is electron-facing C3-grade support, not a
   full three-species labeling theorem by itself.
5. **ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED:** the common charged-lepton scale
   assembly is accepted on its own graph.
6. **SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED:** the approved scale-reference
   primitive supplies only physical-unit conversion for already-retained mass
   content.
7. **NO_LEPTON_COMPARATOR_PROOF_INPUT:** observed charged-lepton masses,
   observed `m_W`, fitted `a_l`, fitted `delta`, and fitted A3 precision are
   excluded as proof inputs.
8. **NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT:** observed `alpha(0)`,
   Rydberg spectroscopy, fitted threshold moments, and hydrogen lines are
   excluded as spectrum proof inputs.
9. **NO_NEW_PRIMITIVE_OR_AXIOM:** the decision does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
10. **OWNER_RATIFICATION:** the owner explicitly accepts the spectrum handoff
    boundary or retained theorem boundary.
11. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the spectrum
    decision and its dependency consequences.

No proper subset of those eleven contract inputs is a retained physical
charged-lepton mass spectrum.

## Conditional Consequence

If all eleven contract inputs are accepted, the conditional consequence is:

```text
PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED
PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED
CHARGED_LEPTON_MASS_SPECTRUM_RETAINED.
```

That consequence is Lane 6 spectrum support only. It does not by itself supply
the R-Lep threshold moment. The R-Lep threshold predicate still requires:

```text
ALPHA_MZ_SCALE_CONTEXT_RETAINED
LEPTON_THRESHOLD_MOMENT_MAP_RETAINED
SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED
NO_PDG_LEPTON_MASS_PROOF_INPUT
NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT
OWNER_RATIFICATION
AUDIT_ACCEPTANCE.
```

It also does not by itself supply the QED loop kernel, R-Q-Heavy, R-Had-NP,
scheme/decoupling matching, `alpha(0)`, static-source Rydberg, or hydrogen.

## Finite Spectrum Witness

The finite branch witness is:

```text
r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3), k = 0,1,2
m_k = a_l^2 r_k(delta)^2.
```

The identities

```text
sum_k r_k(delta) = 3
sum_k r_k(delta)^2 = 6
```

give the signed Koide value `2/3` whenever the signed square-root readout is
licensed. They do not select a physical phase, a physical chamber, a physical
species labeling, or the absolute scale.

At the Brannen comparator phase:

```text
delta = 2/9
sorted r_k = 0.04034990821920668,
             0.5802119201475365,
             2.3794381716332564
sorted r_k^2 = 0.001628115093,
               0.336645849,
               5.661726036.
```

Those numbers are witness arithmetic, not imported masses. Changing `a_l^2`
rescales all three masses. Permuting branch labels preserves the unordered
triple but not the physical species labels. Selecting only the electron branch
does not close the full `e`, `mu`, `tau` spectrum.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC after `#5015` opened and after
`#5013` merged. The queue signal here is that a PR is opened and relevant to a
lane; clean/green status is not a prerequisite because reviewer cleanup and
landing happen outside this packet. No currently open PR closes the
charged-lepton mass spectrum:

| PR | queue signal | effect on this spectrum packet |
|---|---:|---|
| `#5015` wave-collapse-block01 measurement-collapse gate | open | measurement/collapse work; no charged-lepton mass spectrum |
| `#5014` record-formation front/domain-wall chirality | open | chirality/domain-wall work; no charged-lepton mass spectrum |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no Lane 6 spectrum closure |
| `#5011` eta twisted walk family runner | open | runner stabilization; no charged-lepton spectrum |
| `#5010` YT P1 I_s re-audit packet bridge repair | open | diagnostic repair; no spectrum handoff |
| `#5009` S3 spacetime tensor primitive runner | open | bounded S3 tensor context; no charged-lepton mass spectrum |
| `#5008` quark mass-ratio CP probe repair | open | quark context; no lepton spectrum |
| `#5007` Koide native zero-section route guard repair | open | useful native-route context, not a physical three-mass spectrum |
| `#5006` static-source I1 hygiene companion | open | final-lane hygiene; no Lane 6 spectrum closure |
| `#4991` owner-governed Tier-A retirement | open | status progress for old atoms, not theorem closure |

Merge-state labels, branch ordering, and check status are moving review
metadata, not proof inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | names the R-Lep need for a physical charged-lepton mass triple and labels | current-surface non-supply boundary, not spectrum closure |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | electron-mass handoff | selected electron branch only, not full `e`, `mu`, `tau` thresholds |
| `ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | conditional native Z1-Z3 bridge | route bridge only; no full physical spectrum |
| `ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md` | conditional branch-to-mass map | no physical phase/species/scale closure by itself |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | conditional K3 physical electron species bridge | electron-facing C3-grade bridge, not full three-species labeling |
| `ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | conditional K4 scale assembly | common scale only, not branch factors or labels |
| `SCALE_REFERENCE_PRIMITIVE_NOTE.md` | physical-unit conversion primitive | zero dimensionless lepton-mass content |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation | no mass-spectrum primitive, charged-lepton phase primitive, or R-Lep primitive |

The primitive registry was checked with the current origin-main methodology.
Registered primitives are approved premise nodes, but no primitive supplies a
charged-lepton mass-spectrum primitive, a full charged-lepton species-labeling
primitive, or an R-Lep threshold primitive.

## What This Moves

| before this packet | after this packet |
|---|---|
| R-Lep named a full charged-lepton mass triple without a local handoff packet | the mass-spectrum handoff has an eleven-input owner/audit decision contract |
| the physical electron mass packet could be overread as all R-Lep thresholds | electron-only and full-spectrum handoffs are explicitly separated |
| a Koide unordered branch triple could be overread as physical thresholds | full species labels and K4 scale remain separate contract inputs |
| the scale-reference primitive could be overread as a mass value | it remains units conversion after retained dimensionless mass content |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the physical
charged-lepton mass spectrum is retained" is not shipped. The narrowed claim
is:

```text
the physical charged-lepton mass-spectrum handoff is packaged as a
decision-ready ratification contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full spectrum contract | Accept all eleven contract inputs. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts the full physical mass-spectrum handoff. |
| electron-mass route | Treat `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT` as the full spectrum. | ATTEMPTED. It omits `mu`, `tau`, and full labels. |
| branch-map-only route | Treat `m_k = a_l^2 r_k^2` as physical masses without labels and scale authority. | ATTEMPTED. It omits species labeling and accepted scale. |
| native-bridge-only route | Treat native zero-section route support as the spectrum. | ATTEMPTED. It supplies route context only. |
| K3 electron species route | Promote the electron-facing K3 bridge to all three charged leptons. | ATTEMPTED. The existing K3 packet is electron-facing C3-grade support, not full labeling. |
| K4 scale-only route | Use the common scale as if it supplies all masses. | ATTEMPTED. It omits branch factors and species labels. |
| R-Lep threshold route | Treat threshold-moment algebra as mass-spectrum closure. | ATTEMPTED. Threshold algebra consumes masses; it does not derive them. |
| primitive shortcut | Treat approved primitives as already supplying the spectrum. | RULED OUT. The registry supplies no charged-lepton mass-spectrum primitive. |
| empirical comparator route | Use PDG charged-lepton masses, observed `m_W`, fitted `a_l`, fitted `delta`, observed `alpha(0)`, or Rydberg. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| native bridge <-> branch mass map | no in either direction | independent |
| branch mass map <-> full species labels | no in either direction | independent |
| branch mass map <-> absolute scale | no in either direction | independent |
| full species labels <-> absolute scale | no in either direction | independent |
| physical electron species bridge <-> full `e`, `mu`, `tau` labels | no in either direction on current surface | independent |
| spectrum handoff <-> R-Lep threshold moment map | no in either direction | independent |
| owner ratification <-> audit acceptance | no in either direction | independent |

The collapsed decision wall is exactly the eleven-input contract above.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `electron-like`, `muon-like`, `tau-like` | branch-order witness until physical labels are retained |
| `delta = 2/9` | comparator phase witness, not a derived phase |
| `a_l^2` / scale | explicit K4 input |
| `K3` / physical species bridge | electron-facing support unless broadened by owner/audit authority |
| `threshold` / `R-Lep` | downstream consumer, not spectrum derivation |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `observed` / `PDG` / `fitted` / `Rydberg` | excluded as proof input |

No phase, chamber, species-label, scale, unit, threshold, comparator, or audit
rule is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| R-Lep no-go | needs physical mass triple and labels | downstream consumer | yes |
| physical electron mass packet | selected electron branch | partial spectrum support only | yes |
| native bridge packet | route bridge | phase/readout input | yes |
| branch mass-map packet | mass-map composition | branch-to-mass input | yes |
| physical electron species bridge packet | K3 electron bridge | not full species labeling | yes as guard |
| K4 scale packet | common scale | scale input | yes |
| scale-reference primitive | physical-unit conversion | no dimensionless masses | yes as guard |

Non-matching surfaces are not used as spectrum closure evidence.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "this packet does not ratify the
physical charged-lepton mass spectrum."

| resolution | tested? | outcome |
|---|---:|---|
| electron mass | yes | single-species handoff only |
| unordered Koide branch triple | yes | lacks retained physical labels |
| common scale | yes | needed, not sufficient |
| full spectrum contract | yes | positive route remains open |
| R-Lep thresholds | kept separate | still need threshold moment, high-scale context, owner, and audit |

No universal no-go against future charged-lepton spectrum retention is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained native zero-section bridge or owner/audit adoption | `NATIVE_ZERO_SECTION_BRIDGE_RETAINED` |
| retained Koide branch mass-map theorem or owner/audit adoption | `KOIDE_BRANCH_MASS_MAP_RETAINED` |
| retained full charged-lepton species-labeling theorem | `FULL_CHARGED_LEPTON_SPECIES_LABELING_RETAINED` |
| retained K4 scale assembly or owner/audit adoption | `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED` |
| owner/audit acceptance of this packet | `PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED` and `PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED` after all inputs are present |
| retained R-Lep threshold packet after spectrum closure | `R_LEP_THRESHOLDS_RETAINED` |

These are live import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that the branch formula already yields three
numbers once `delta` and `a_l^2` are supplied, so this packet is redundant
bookkeeping. The strongest version is: the physical electron packet plus K4
scale plus Koide branch map almost names the full triplet.

The narrow reply is that R-Lep needs a retained physical `e`, `mu`, `tau`
threshold spectrum, not only a selected electron mass or an unordered branch
triple. Zero-import retained status requires explicit labels, scale authority,
comparator exclusion, and audit acceptance before alpha0 transport can spend
threshold logarithms.

### N8 - Cross-Cycle Echo

This mirrors the electron-mass and alpha0 packets: familiar algebra is kept as
support until its dependency graph, comparator boundary, and owner/audit
handoff are explicit. Here the same discipline separates electron mass, full
charged-lepton spectrum, R-Lep threshold moments, and final hydrogen.

**Gate result:** broad spectrum-retention claim fails; narrowed mass-spectrum
handoff packet passes.

## Explicit Non-Claims

- No derivation or ratification of the physical charged-lepton mass spectrum.
- No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.
- No derivation or ratification of the native Z1-Z3 bridge clauses.
- No derivation or ratification of the Koide branch-to-mass map.
- No derivation or ratification of full physical `e`, `mu`, `tau` labels.
- No derivation or ratification of the absolute charged-lepton scale.
- No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.
- No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.
- No derivation of `alpha(0)`, static-source Rydberg, or retained hydrogen.
- No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`,
  fitted `delta`, observed `alpha(0)`, Rydberg, or hydrogen spectroscopy as
  proof input.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_charged_lepton_mass_spectrum_ratification_decision_packet.py
```
