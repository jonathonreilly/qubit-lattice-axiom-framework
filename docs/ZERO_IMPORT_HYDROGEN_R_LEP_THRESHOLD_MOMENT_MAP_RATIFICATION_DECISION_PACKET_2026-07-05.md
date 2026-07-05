# Zero-Import Hydrogen: R-Lep Threshold-Moment Map Ratification Decision Packet

**Date:** 2026-07-05
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify R-Lep thresholds, does
not ratify the physical charged-lepton mass spectrum, does not derive
`alpha(0)`, does not derive static-source Rydberg, and does not claim hydrogen
is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_r_lep_threshold_moment_map_ratification_decision_packet.py`

## Purpose

The R-Lep thresholds lane consumes one map input:

```text
LEPTON_THRESHOLD_MOMENT_MAP_RETAINED.
```

The mass-spectrum packet can conditionally supply the physical `e`, `mu`, and
`tau` masses and species labels. It still does not say how Lane 2 is licensed
to turn those retained masses into the charged-lepton threshold moment
consumed by alpha0 transport. This packet packages that map as a separate
owner/audit decision object.

It is narrower than `R_LEP_THRESHOLDS_RETAINED`: R-Lep still needs the
retained mass triple, species labels, high-scale context, scale-reference
chain, comparator exclusion, owner ratification, and audit acceptance before
the map can be spent as a threshold handoff.

## Decision Object

The decision object is exactly:

```text
the charged-lepton one-loop threshold-moment map consumed by the zero-import
hydrogen R-Lep lane.
```

It has six clauses:

| clause | decision text |
|---|---|
| TM.1 | charge/count weights: the charged-lepton QED weights are `N_c(e)Q_e^2 = N_c(mu)Q_mu^2 = N_c(tau)Q_tau^2 = 1` |
| TM.2 | physical mass domain: the map domain is the retained physical `e`, `mu`, `tau` mass triple, not PDG masses or an unordered branch witness |
| TM.3 | reference scale interface: the logarithms are referenced to the retained high-scale context used by alpha0 transport |
| TM.4 | one-loop log map: the charged-lepton threshold moment is `T_lep = log(M_Z/m_e) + log(M_Z/m_mu) + log(M_Z/m_tau)` |
| TM.5 | scale-reference boundary: the approved scale-reference primitive is used only for units after dimensionless mass content is retained |
| TM.6 | comparator exclusion: observed lepton masses, fitted effective thresholds, observed `alpha(0)`, Rydberg, and hydrogen lines are not proof inputs |

The object deliberately excludes quark thresholds, hadronic vacuum
polarization, scheme/decoupling matching, the QED loop kernel, low-energy
`alpha(0)`, and final hydrogen.

## Ratification Decision Contract

This packet is decision-ready only if all twelve contract inputs are visible:

```text
LEPTON_THRESHOLD_MOMENT_MAP_TEXT_LOCK
CHARGED_LEPTON_QED_WEIGHT_ALGEBRA_RETAINED
PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_DOMAIN_LOCK
PHYSICAL_CHARGED_LEPTON_SPECIES_LABEL_DOMAIN_LOCK
ALPHA_MZ_REFERENCE_SCALE_INTERFACE_LOCK
ONE_LOOP_THRESHOLD_LOG_MAP_RETAINED
SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED
NO_THRESHOLD_VALUE_PROOF_INPUT
NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The contract means:

1. **LEPTON_THRESHOLD_MOMENT_MAP_TEXT_LOCK:** the TM.1-TM.6 text above is the
   full object being decided.
2. **CHARGED_LEPTON_QED_WEIGHT_ALGEBRA_RETAINED:** the lepton charge/count
   weights are retained as structural QED bookkeeping, not imported from
   threshold fits.
3. **PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_DOMAIN_LOCK:** the map is only
   applicable after the physical mass triple is supplied by Lane 6.
4. **PHYSICAL_CHARGED_LEPTON_SPECIES_LABEL_DOMAIN_LOCK:** the map domain is the
   physical charged-lepton species set, even though the one-loop lepton weights
   are equal.
5. **ALPHA_MZ_REFERENCE_SCALE_INTERFACE_LOCK:** the reference scale is the
   retained alpha0-transport high-scale context, not a fitted effective scale.
6. **ONE_LOOP_THRESHOLD_LOG_MAP_RETAINED:** the log-threshold functional is
   accepted for the R-Lep lane.
7. **SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED:** the approved scale-reference
   primitive supplies only physical-unit conversion for already-retained mass
   quantities.
8. **NO_THRESHOLD_VALUE_PROOF_INPUT:** PDG lepton masses, fitted effective
   thresholds, and observed mass products are excluded as proof inputs.
9. **NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT:** observed `alpha(0)`,
   Rydberg spectroscopy, and hydrogen lines are excluded as map proof inputs.
10. **NO_NEW_PRIMITIVE_OR_AXIOM:** the decision does not add an axiom, approved
    primitive, or Tier-A admitted numerical input.
11. **OWNER_RATIFICATION:** the owner explicitly accepts the threshold-map
    boundary or retained theorem boundary.
12. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the threshold
    map and its dependency consequences.

No proper subset of those twelve contract inputs is a retained R-Lep
threshold-moment map.

## Conditional Consequence

If all twelve contract inputs are accepted, the conditional consequence is:

```text
LEPTON_THRESHOLD_MOMENT_MAP_RETAINED.
```

That consequence is map support only. It does not by itself supply a retained
charged-lepton mass triple, retained species labels, `T_LEP_THRESHOLD_MOMENT_RETAINED`,
or `R_LEP_THRESHOLDS_RETAINED`. The full R-Lep threshold packet still requires:

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
AUDIT_ACCEPTANCE.
```

It also does not supply the QED loop kernel, R-Q-Heavy, R-Had-NP,
scheme/decoupling matching, alpha0 transport, static-source Rydberg, or
hydrogen.

## Finite Map Witness

The charged-lepton QED weights are:

```text
N_c(e) Q_e^2 = 1
N_c(mu) Q_mu^2 = 1
N_c(tau) Q_tau^2 = 1
sum_l N_c(l) Q_l^2 = 3
b_lep = (4/3) * 3 = 4.
```

The one-loop threshold moment is:

```text
T_lep(M_Z; m_e,m_mu,m_tau)
  = log(M_Z / m_e) + log(M_Z / m_mu) + log(M_Z / m_tau)
  = log(M_Z^3 / (m_e m_mu m_tau)).
```

For a common lepton threshold `m_*`, the map agrees with the common-threshold
beta-coefficient form:

```text
(2/(3*pi)) * 3 log(M_Z/m_*) = (b_lep/(2*pi)) log(M_Z/m_*).
```

Moving any one mass changes the moment by the negative log-ratio of that mass
change. Rescaling `M_Z`, `m_e`, `m_mu`, and `m_tau` together leaves the moment
unchanged. At one loop the three lepton weights are equal, so the numeric sum
is permutation-invariant, but the R-Lep handoff still requires physical
species labels to prevent an unordered branch witness from being spent as a
physical threshold package.

This finite algebra is a map witness only. It does not derive `m_e`, `m_mu`,
`m_tau`, `M_Z`, `alpha(0)`, or hydrogen.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC after `#5015` opened and after
`#5013` merged. The queue signal here is that a PR is opened and relevant to a
lane; clean/green status is not a prerequisite because reviewer cleanup and
landing happen outside this packet. No currently open PR supplies the
threshold-moment map:

| PR | queue signal | effect on this threshold-map packet |
|---|---:|---|
| `#5015` wave-collapse-block01 measurement-collapse gate | open | measurement/collapse work; no R-Lep threshold-moment map |
| `#5014` record-formation front/domain-wall chirality | open | chirality/domain-wall work; no R-Lep threshold-moment map |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no charged-lepton threshold map |
| `#5011` eta twisted walk family runner | open | runner stabilization; no threshold-moment map |
| `#5010` YT P1 I_s re-audit packet bridge repair | open | diagnostic repair; no charged-lepton threshold moment |
| `#5009` S3 spacetime tensor primitive runner | open | bounded S3 tensor context; no R-Lep threshold map |
| `#5008` quark mass-ratio CP probe repair | open | quark context; no lepton threshold map |
| `#5007` Koide native zero-section route guard repair | open | useful native-route context, not a threshold-moment theorem |
| `#5006` static-source I1 hygiene companion | open | final-lane hygiene; no R-Lep threshold map |
| `#4991` owner-governed Tier-A retirement | open | status progress for old atoms, not theorem closure |

Merge-state labels, branch ordering, and check status are moving review
metadata, not proof inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | names `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED` as an R-Lep input | current-surface non-supply boundary, not map closure |
| `ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional physical `e`, `mu`, `tau` mass triple and labels | no threshold-moment map |
| `frontier_atomic_alpha0_threshold_moment_no_go.py` | threshold-moment reduction and comparator-only target arithmetic | finite witness, not a retained R-Lep map |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | downstream alpha0 consumer contract | consumes R-Lep; does not derive threshold map |
| `ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md` | loop-kernel boundary | independent from threshold masses and map |
| `SCALE_REFERENCE_PRIMITIVE_NOTE.md` | physical-unit conversion primitive | zero dimensionless threshold content |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation | no threshold-moment-map primitive or R-Lep primitive |

The primitive registry was checked with the current origin-main methodology.
Registered primitives are approved premise nodes, but no primitive supplies a
lepton threshold-moment map primitive, an R-Lep thresholds primitive, or an
alpha0 primitive.

## What This Moves

| before this packet | after this packet |
|---|---|
| R-Lep named a threshold-moment map without a local handoff packet | `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED` has a twelve-input owner/audit decision contract |
| mass-spectrum closure could be overread as threshold-moment closure | the mass triple and the log-threshold map are explicitly separated |
| charge/count weights could be overread as threshold logs | the packet separates QED weights from mass-dependent logarithms |
| alpha0 target arithmetic could be overread as proof | comparator target arithmetic remains witness-only |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the R-Lep threshold
moment is retained" is not shipped. The narrowed claim is:

```text
the R-Lep threshold-moment map is packaged as a decision-ready ratification
contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full threshold-map contract | Accept all twelve contract inputs. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts the map. |
| mass-spectrum-only route | Treat retained `e`, `mu`, `tau` masses as already supplying the map. | ATTEMPTED. Masses are map inputs, not the log-threshold functional or alpha0-lane license. |
| charge/count-only route | Treat `b_lep = 4` as the threshold moment. | ATTEMPTED. Weights do not supply logarithms. |
| comparator target route | Fit an effective threshold moment to observed `alpha(0)`. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is target data, not proof input. |
| QED-loop route | Retain the QED loop kernel and call the lepton map closed. | ATTEMPTED. The loop kernel is independent of threshold masses and map domain. |
| open-PR shortcut | Treat the currently opened PR surface as threshold-map closure. | ATTEMPTED. The refreshed open PRs do not supply the R-Lep threshold-moment map. |
| PDG mass route | Use observed lepton masses to evaluate `T_lep`. | VALID RETAINED-WITH-IMPORT ROUTE. It is not zero-import threshold-map retention. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| charge/count weights <-> threshold log map | no in either direction | independent |
| mass-triple domain <-> threshold log map | no in either direction | independent |
| species-label domain <-> threshold log map | no in either direction | independent |
| high-scale interface <-> threshold log map | no in either direction | independent |
| scale-reference chain <-> dimensionless threshold values | no in either direction | independent |
| owner ratification <-> audit acceptance | no in either direction | independent |

The collapsed decision wall is exactly the twelve-input contract above.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `one-loop` | explicit scope lock, not full QED transport |
| `threshold` / `log` | explicit map input |
| `M_Z` / reference scale | explicit high-scale interface input |
| `standard` / `QED` | charge/count bookkeeping only unless the map is ratified |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `observed` / `PDG` / `fitted` / `Rydberg` | excluded as proof input |

No threshold value, reference scale, physical mass, comparator, or audit rule
is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| R-Lep no-go | `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED` is an unsupplied input | threshold-map handoff | yes |
| mass-spectrum packet | physical mass triple and labels | upstream map domain | yes |
| alpha0 threshold-moment runner | threshold/matching moment is load-bearing | finite map witness only | yes as guard |
| alpha0 transport packet | consumes R-Lep | downstream consumer | yes |
| QED loop-kernel no-go | loop kernel is separate | independence guard | yes |
| scale-reference primitive | physical-unit conversion | no threshold values | yes as guard |

Non-matching surfaces are not used as map closure evidence.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "this packet does not ratify the
R-Lep threshold moment."

| resolution | tested? | outcome |
|---|---:|---|
| lepton charge/count weights | yes | gives weights, not logs |
| one-loop log map | named, not closed | explicit decision object |
| retained mass spectrum | kept separate | upstream domain input only |
| alpha0 transport | kept separate | still needs QED kernel, quark/hadron thresholds, and matching |
| full precision running | out of scope | not claimed |

No universal no-go against future threshold-map retention is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained QED charge/count bookkeeping authority | `CHARGED_LEPTON_QED_WEIGHT_ALGEBRA_RETAINED` |
| retained one-loop threshold-map theorem or owner/audit adoption | `ONE_LOOP_THRESHOLD_LOG_MAP_RETAINED` |
| retained high-scale alpha context | `ALPHA_MZ_REFERENCE_SCALE_INTERFACE_LOCK` |
| owner/audit acceptance of this packet | `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED` after all inputs are present |
| full R-Lep packet after mass spectrum and map closure | `R_LEP_THRESHOLDS_RETAINED` |

These are live import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that the one-loop threshold map is standard QED
bookkeeping, and once the mass triple is retained there is nothing left but
evaluating logarithms. That is the strongest positive route. The narrow reply
is that zero-import retained alpha0 cannot spend "standard QED bookkeeping" as
implicit background: the map, its scope, its reference-scale interface, and its
comparator exclusions must be explicit before R-Lep can consume the masses.

### N8 - Cross-Cycle Echo

This echoes the alpha0 threshold-moment runner: finite arithmetic can expose
the target but cannot promote threshold/matching content to retained status by
itself. The disciplined move is to keep charge/count weights, mass-spectrum
inputs, threshold-log map, QED loop kernel, quark/hadron thresholds, and final
alpha0 transport separate until each handoff is accepted.

**Gate result:** broad threshold-moment-retention claim fails; narrowed
threshold-moment-map handoff packet passes.

## Explicit Non-Claims

- No derivation or ratification of `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED`.
- No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.
- No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.
- No derivation or ratification of a physical charged-lepton mass triple.
- No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.
- No derivation or ratification of the QED loop kernel.
- No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.
- No derivation or ratification of `ALPHA0_RETAINED`.
- No derivation of static-source Rydberg or retained hydrogen.
- No use of observed `alpha(0)`, Rydberg, PDG lepton masses, fitted
  thresholds, or hydrogen spectroscopy as proof input.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_r_lep_threshold_moment_map_ratification_decision_packet.py
```
