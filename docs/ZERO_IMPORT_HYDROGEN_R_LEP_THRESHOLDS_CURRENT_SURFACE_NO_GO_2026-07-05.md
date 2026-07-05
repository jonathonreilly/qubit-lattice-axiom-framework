# Zero-Import Hydrogen: R-Lep Thresholds Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify charged-lepton thresholds,
does not derive `alpha(0)`, does not derive `m_e`, and does not claim hydrogen
is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_r_lep_thresholds_current_surface_no_go.py`

## Scope

The Lane 2 alpha0 transport package consumes one charged-lepton input:

```text
R_LEP_THRESHOLDS_RETAINED.
```

This is the leptonic threshold contribution to the QED running step from
`alpha_EM(M_Z)` to `alpha(0)`. It is narrower than the full alpha0 transport
package and narrower than the physical electron-mass handoff. It requires the
physical charged-lepton threshold content for `e`, `mu`, and `tau`, not just an
electron mass and not a fitted effective threshold.

The narrow current-surface result is:

```text
current retained, primitive, and open-PR surfaces do not supply
R_LEP_THRESHOLDS_RETAINED.
```

The R-Lep threshold target remains needed before alpha0 transport can spend
charged-lepton threshold support.

## R-Lep Threshold Contract

A future zero-import R-Lep handoff needs all eleven inputs:

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

1. **R_LEP_THRESHOLDS_TEXT_LOCK:** the decision object is exactly the
   charged-lepton threshold handoff consumed by Lane 2 alpha0 transport.
2. **ALPHA_MZ_SCALE_CONTEXT_RETAINED:** the threshold logs are referenced to
   the retained high-scale coupling context, not to a fitted scale.
3. **PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED:** the physical-unit mass
   content for `e`, `mu`, and `tau` is retained without PDG mass proof input.
4. **PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED:** the three retained
   masses are identified with the physical charged-lepton species rather than
   only an unordered Koide branch triple.
5. **LEPTON_THRESHOLD_MOMENT_MAP_RETAINED:** the map from the retained mass
   triple to the leptonic threshold moment is accepted for the alpha0 lane.
6. **SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED:** the approved scale-reference
   primitive is used only as units conversion after dimensionless mass content
   is retained.
7. **NO_PDG_LEPTON_MASS_PROOF_INPUT:** observed lepton masses are not proof
   inputs on the zero-import branch.
8. **NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT:** observed `alpha(0)`,
   Rydberg spectroscopy, fitted effective thresholds, and hydrogen lines are
   not proof inputs.
9. **NO_NEW_PRIMITIVE_OR_AXIOM:** the handoff does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
10. **OWNER_RATIFICATION:** the owner explicitly accepts the R-Lep threshold
    boundary or retained theorem boundary.
11. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the R-Lep
    handoff and its dependency consequences.

No proper subset of those eleven inputs is a retained R-Lep threshold handoff.

## Conditional Consequence

If all eleven inputs are accepted, the conditional consequence is:

```text
R_LEP_THRESHOLDS_RETAINED
T_LEP_THRESHOLD_MOMENT_RETAINED.
```

That consequence is Lane 2 support only. It does not by itself supply the QED
loop kernel, heavy-quark thresholds, nonperturbative hadronic vacuum
polarization, scheme/decoupling matching, `alpha(0)`, `m_e`, or hydrogen.

## Finite Threshold Algebra

At the one-loop target level, the charged-lepton part of the threshold moment is

```text
T_lep = log(M_Z / m_e) + log(M_Z / m_mu) + log(M_Z / m_tau)
      = log(M_Z^3 / (m_e m_mu m_tau)).
```

The charge/count weights are fixed:

```text
N_c(e) Q_e^2 = 1
N_c(mu) Q_mu^2 = 1
N_c(tau) Q_tau^2 = 1
sum_l N_c(l) Q_l^2 = 3
b_lep = (4/3) * 3 = 4.
```

This finite algebra shows why the charged-lepton threshold logs are
load-bearing. The weights are available as structure, but the logarithms are
not. Moving any one threshold changes `T_lep`; an unordered Koide triple
without physical species labels is not enough for a physical threshold handoff.

The algebra also shows why this is not an electron-only dependency. A retained
physical electron mass can help Lane 6, but R-Lep still needs the `mu` and
`tau` thresholds and the mass-triple-to-threshold map before alpha0 transport
can spend the charged-lepton contribution.

The charged-lepton mass-spectrum decision packet
`ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the full `e`, `mu`, `tau` mass-triple and species-label handoff as a
separate eleven-input owner/audit contract. If accepted, it can conditionally
supply `PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED` and
`PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED`, but it does not ratify
R-Lep thresholds or the threshold-moment map. The mass-spectrum target remains
needed before R-Lep can spend charged-lepton thresholds.

The R-Lep threshold-moment map decision packet
`ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the log-threshold functional itself as a separate twelve-input
owner/audit contract. If accepted, it can conditionally supply
`LEPTON_THRESHOLD_MOMENT_MAP_RETAINED`, but it does not supply the physical
mass triple, species labels, `T_LEP_THRESHOLD_MOMENT_RETAINED`, or
`R_LEP_THRESHOLDS_RETAINED`. The threshold-moment map target remains needed
before R-Lep can spend charged-lepton threshold logs.

The R-Lep thresholds ratification decision packet
`ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the parent eleven-input owner/audit route for
`R_LEP_THRESHOLDS_RETAINED` and `T_LEP_THRESHOLD_MOMENT_RETAINED`. It is the
positive import-retirement handoff for this target, not current retained
threshold supply.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | identifies R-Lep as blocked by Lane 6 | `R_LEP_THRESHOLDS_RETAINED` |
| `frontier_atomic_alpha0_threshold_moment_no_go.py` | threshold-moment reduction and comparator-scale arithmetic | retained charged-lepton threshold moment |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | alpha0 consumer contract | R-Lep closure |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | downstream alpha0 non-supply boundary | standalone R-Lep closure |
| `ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional full `e`, `mu`, `tau` mass-triple and label handoff | R-Lep threshold moment or current retained spectrum |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional log-threshold map handoff | mass spectrum, retained threshold moment, or R-Lep closure |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional parent R-Lep owner/audit handoff | current retained R-Lep consequence |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | physical electron mass handoff | `mu`/`tau` thresholds or full mass triple |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current electron-mass non-supply boundary | retained charged-lepton mass triple |
| `ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md` | conditional branch-to-mass map | phase, species labels, absolute scale, or retained thresholds |
| `ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | conditional K4 scale assembly | branch factors, species labels, or threshold moment |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation | charged-lepton masses, mass labels, threshold logs, or `alpha(0)` |

The primitive registry was checked with the current origin-main methodology.
Registered primitives are approved premise nodes, but they do not supply an
R-Lep threshold primitive, a charged-lepton mass-spectrum primitive, or an
alpha0 primitive.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC after `#5015` opened and after
`#5013` merged. The queue signal here is that a PR is opened and relevant to a
lane; clean/green status is not a prerequisite because reviewer cleanup and
landing happen outside this packet. No currently open PR supplies the R-Lep
threshold handoff:

| PR | queue signal | effect on this R-Lep threshold boundary |
|---|---:|---|
| `#5015` wave-collapse-block01 measurement-collapse gate | open | measurement/collapse work; no charged-lepton thresholds |
| `#5014` record-formation front/domain-wall chirality | open | chirality/domain-wall work; no charged-lepton thresholds |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no charged-lepton thresholds |
| `#5011` eta twisted walk family runner | open | runner stabilization; no alpha0 R-Lep threshold package |
| `#5010` YT P1 I_s re-audit packet bridge repair | open | diagnostic repair; no charged-lepton threshold moment |
| `#5009` S3 spacetime tensor primitive runner | open | bounded S3 tensor context; no charged-lepton mass spectrum |
| `#5008` quark mass-ratio CP probe repair | open | quark context; no R-Lep threshold handoff |
| `#5007` Koide native zero-section route guard repair | open | useful native-route context, not a retained charged-lepton threshold spectrum |
| `#5006` static-source I1 hygiene companion | open | atomic hygiene context, not alpha0 R-Lep thresholds |
| `#4991` owner-governed Tier-A retirement | open | status progress for old atoms; no charged-lepton threshold theorem |

Merge-state labels, branch ordering, and check status are moving review
metadata, not proof inputs here.

## Authority Boundary

| source | boundary here |
|---|---|
| `ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` | R-Lep is one alpha0 input among several |
| `ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md` | loop-kernel closure is separate from threshold masses |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | consumes `R_LEP_THRESHOLDS_RETAINED`; does not derive it |
| `ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md` | packages `PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED` and `PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED`; does not derive threshold logs |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md` | packages `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED`; does not derive masses or R-Lep closure |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md` | packages the parent R-Lep threshold decision contract; does not itself ratify current threshold supply |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | final electron-mass consumer, not full `e,mu,tau` threshold spectrum |
| `SCALE_REFERENCE_PRIMITIVE_NOTE.md` | units conversion only; zero dimensionless lepton-mass content |

## What This Moves

| before this note | after this note |
|---|---|
| alpha0 named R-Lep as a missing input | R-Lep has a standalone current-surface non-supply boundary |
| the full mass-spectrum input had no local handoff packet | the mass-spectrum target remains needed and now has a separate decision contract |
| the threshold-moment map had no local handoff packet | the threshold-moment map target remains needed and now has a separate decision contract |
| electron mass could be overread as all charged-lepton thresholds | the note separates electron mass from the full `e,mu,tau` threshold moment |
| Koide branch triple could be overread as physical thresholds | the note requires species labels, scale, and the threshold-moment map |
| `b_QED` weights could be overread as threshold logs | the note separates charge/count weights from mass-dependent logarithms |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "charged-lepton thresholds
cannot be retained" is not shipped. The narrowed claim is:

```text
current retained, primitive, and open-PR surfaces do not supply
R_LEP_THRESHOLDS_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full R-Lep contract | Accept all eleven inputs. | OPEN POSITIVE ROUTE. It would close the R-Lep handoff, but this note does not accept it. |
| electron-mass-only route | Use retained `m_e` as the whole charged-lepton threshold contribution. | ATTEMPTED. R-Lep also needs `mu`, `tau`, and the threshold-moment map. |
| Koide branch-map route | Treat an abstract Koide branch triple as physical `e,mu,tau` thresholds. | ATTEMPTED. The branch map does not by itself supply species labels, phase, scale, or physical-unit masses. |
| absolute-scale-only route | Use K4 scale assembly as if it supplied thresholds. | ATTEMPTED. Scale alone does not supply branch factors or species labels. |
| `b_QED` weight route | Use the lepton charge/count weight `3` or `b_lep = 4` as R-Lep. | ATTEMPTED. Weights do not supply logarithms of threshold masses. |
| QED loop-kernel route | Retain the loop kernel and call the leptonic thresholds closed. | ATTEMPTED. The kernel is independent of the mass thresholds. |
| comparator-fit route | Fit an effective lepton threshold to observed `alpha(0)`. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is not proof input. |
| PDG mass route | Use observed `m_e`, `m_mu`, and `m_tau`. | VALID RETAINED-WITH-IMPORT ROUTE. It is not zero-import R-Lep retention. |
| open-PR shortcut | Treat the currently opened PR surface as charged-lepton threshold closure. | ATTEMPTED. The refreshed open PRs do not supply the R-Lep threshold handoff. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| high-scale context <-> physical charged-lepton mass triple | no in either direction | independent |
| physical mass triple <-> physical species labels | no in either direction on current surface | independent |
| physical mass triple <-> threshold-moment map | no in either direction | independent |
| species labels <-> threshold-moment map | no in either direction | independent |
| scale-reference chain <-> dimensionless mass content | no in either direction | independent |
| comparator exclusion <-> owner ratification | no in either direction | independent |
| owner ratification <-> audit acceptance | no in either direction | independent |

The collapsed wall set is the eleven-input contract above.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `threshold` / `running` | explicit R-Lep input, not standard background |
| `M_Z` / high-scale context | explicit scale-context input |
| `charged-lepton mass triple` | explicit mass-spectrum input |
| `electron-like` / branch sorting | insufficient until species labels are retained |
| `registered` / `primitive` | registry checked; approved primitives do not supply R-Lep |
| `PDG` / observed / fitted / comparator | excluded as proof input |

No lepton mass, species label, scale conversion, threshold logarithm, or
comparator value is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| Lane 2 QED running firewall | R-Lep blocked by Lane 6 | R-Lep threshold handoff | yes |
| alpha0 threshold-moment runner | threshold logs are load-bearing | lepton threshold moment | yes |
| alpha0 transport packet | consumes `R_LEP_THRESHOLDS_RETAINED` | downstream consumer | yes |
| physical electron mass packet | electron-mass handoff | partial Lane 6 input only | yes as guard |
| Koide branch mass-map packet | branch-to-mass map | support only, not threshold closure | yes as guard |
| scale-reference primitive | units conversion only | no dimensionless threshold content | yes as guard |

Non-matching surfaces are not used as R-Lep closure evidence.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "current retained, primitive, and
open-PR surfaces do not supply R-Lep thresholds."

| resolution | tested? | result |
|---|---:|---|
| lepton charge/count weights | yes | gives weight `3`, not logs |
| electron mass alone | yes | incomplete for `mu` and `tau` |
| charged-lepton mass triple | named, not closed | explicit input |
| physical species labels | named, not closed | explicit input |
| full alpha0 transport | kept separate | still needs QED kernel, quark/hadron thresholds, and matching |

No universal no-go against future charged-lepton threshold retention is
claimed.

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained physical charged-lepton mass-spectrum theorem | mass-triple input |
| retained physical species labeling theorem for `e,mu,tau` | species-label input |
| retained Koide branch map plus retained phase/species/scale | possible mass-spectrum route |
| owner/audit acceptance of the threshold-moment map packet | `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED` |
| owner/audit acceptance of an R-Lep threshold packet | `R_LEP_THRESHOLDS_RETAINED` after all inputs are present |
| explicit PDG lepton-mass admission | retained-with-import R-Lep route, not zero-import |

These are import-retirement paths, not automatic new axioms.

### N7 - Steelman

A hostile reviewer can argue that the Koide branch and physical electron-mass
stack already aim at the charged-lepton spectrum, so the R-Lep threshold
handoff is just bookkeeping: once Lane 6 gives the lepton masses, the QED
threshold logs are a standard calculation. The narrow reply is that zero-import
retained alpha0 cannot spend "standard calculation" as background. The current
surface has neither a retained physical `e,mu,tau` mass spectrum nor a retained
species-labeled threshold-moment map, and physical electron mass alone is not
the R-Lep contribution.

### N8 - Cross-Cycle Echo

This mirrors the prior Lane 2 firewalls: retained high-scale alpha and
charge/count coefficients are real support, but threshold placement remains
load-bearing. The same mechanism applies here at the charged-lepton sublane:
keep the lepton weights as support, but do not spend them as retained
threshold logarithms.

**Gate result:** broad charged-lepton-threshold no-go is not shipped; narrowed
current-surface R-Lep non-supply boundary passes.

## Explicit Non-Claims

- No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.
- No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.
- No derivation or ratification of a physical charged-lepton mass triple.
- No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.
- No derivation or ratification of the physical charged-lepton species labels.
- No derivation or ratification of the QED loop kernel.
- No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.
- No derivation or ratification of `ALPHA0_RETAINED`.
- No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.
- No derivation of static-source Rydberg or retained hydrogen.
- No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or
  hydrogen spectroscopy as proof input.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.
