# Zero-Import Hydrogen: Alpha0 Transport Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify `alpha(0)`, does not
derive `m_e`, does not derive static-source Rydberg, and does not claim
hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_alpha0_transport_current_surface_no_go.py`

## Scope

The static-source Rydberg lane consumes one Lane 2 low-energy coupling input:

```text
RETAINED_ALPHA0_LOW_ENERGY_COULOMB.
```

The alpha0 transport decision packet packages that input through the
conditional consequence:

```text
ALPHA0_TRANSPORT_RETAINED
ALPHA0_RETAINED.
```

Current Lane 2 surfaces supply retained high-scale electroweak support,
structural charge/count support, target arithmetic, and a decision contract.
They do not supply the retained low-energy Coulomb coupling. The narrow result
is not "`alpha(0)` cannot be retained." The narrow result is that current
retained, primitive, and open-PR surfaces do not supply
`ALPHA0_TRANSPORT_RETAINED`, `ALPHA0_RETAINED`, or
`RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.

## Alpha0 Transport Contract

A future zero-import alpha0 transport handoff needs all eleven inputs:

```text
ALPHA0_TRANSPORT_TEXT_LOCK
ALPHA_MZ_RETAINED
QED_LOOP_KERNEL_RETAINED
R_LEP_THRESHOLDS_RETAINED
R_Q_HEAVY_THRESHOLDS_RETAINED
R_HAD_NP_RETAINED
SCHEME_DECOUPLING_MATCHING_RETAINED
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If all eleven inputs are accepted, the conditional consequence would be:

```text
ALPHA0_TRANSPORT_RETAINED
ALPHA0_RETAINED
RETAINED_ALPHA0_LOW_ENERGY_COULOMB.
```

That consequence is not supplied here. The current missing inputs include:

```text
QED_LOOP_KERNEL_RETAINED
R_LEP_THRESHOLDS_RETAINED
R_Q_HEAVY_THRESHOLDS_RETAINED
R_HAD_NP_RETAINED
SCHEME_DECOUPLING_MATCHING_RETAINED
```

Retained `alpha_EM(M_Z)` and structural `b_QED = 32/3` are real support for
the alpha lane, but they do not supply threshold placement, hadronic vacuum
polarization, finite matching, or the low-energy value.

## Target Arithmetic

The one-loop target surface is:

```text
alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match

T_EM = sum_f N_c(f) Q_f^2 log(M_Z / m_f^eff)
```

The retained charge/count surface fixes only the total weight:

```text
sum_f N_c(f) Q_f^2 = 8
b_QED = (4/3) * 8 = 32/3
```

Comparator bookkeeping, not proof input:

```text
alpha_EM(M_Z)^-1 = 127.67
alpha(0)^-1 comparator = 137.035999084
Delta inverse alpha = 9.365999084
T_EM_target = 44.139...
common log = T_EM_target / 8 ~= 5.517
M_eff ~= M_Z * exp(-common log) ~= 0.37 GeV
```

This shows the size of the missing threshold/matching content. It does not
derive `T_EM`, `Delta_match`, hadronic `R(s)`, or `alpha(0)`.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` | alpha transport target inputs and finite target arithmetic | retained alpha0 transport |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | eleven-input owner/audit handoff | current retained consequence |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` | review compression for the direct alpha0 transport rows | no retained alpha0 transport or low-energy Coulomb coupling |
| `ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for the QED loop kernel | `QED_LOOP_KERNEL_RETAINED` |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for charged-lepton thresholds | `R_LEP_THRESHOLDS_RETAINED` |
| `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | R-Lep/R-Q-Heavy/R-Had-NP split | retained threshold package |
| `ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md` | high-scale alpha alone does not determine alpha0 | low-energy alpha bridge |
| `ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md` | direct `alpha_EM(M_Z)` substitution is load-bearing wrong for Rydberg | alpha0 derivation |
| `frontier_atomic_qed_threshold_bridge_firewall.py` | threshold-placement underdetermination with `b_QED` support | retained threshold placement |
| `frontier_atomic_alpha0_threshold_moment_no_go.py` | threshold-moment target arithmetic | retained threshold moment |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | downstream consumer predicate | alpha0 derivation |
| `docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md` | retained `alpha_EM(M_Z)` surface | retained `alpha(0)` |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | QED loop kernel, thresholds, hadronic `R(s)`, scheme matching, or alpha0 value |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `alpha0_primitive`,
`qed_loop_kernel_primitive`, `r_lep_thresholds_primitive`,
`r_q_heavy_thresholds_primitive`, `r_had_np_primitive`, or
`scheme_decoupling_matching_primitive`.

The QED loop-kernel current-surface no-go
`ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`QED_LOOP_KERNEL_RETAINED`; the QED loop target remains needed before alpha0
transport can spend QED substrate support.

The R-Lep thresholds current-surface no-go
`ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`R_LEP_THRESHOLDS_RETAINED`; the R-Lep threshold target remains needed before
alpha0 transport can spend charged-lepton threshold support.
The R-Lep thresholds ratification decision packet
`ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the parent R-Lep route for `R_LEP_THRESHOLDS_RETAINED` and
`T_LEP_THRESHOLD_MOMENT_RETAINED`; it does not by itself supply the remaining
alpha0 inputs or the current alpha0 retained consequence.

The alpha0 transport assembly ladder review packet
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md`
does not change this current-surface result. It compresses the direct Lane 2
rows into one review surface, but current retained, primitive, and open-PR
surfaces still do not supply `ALPHA0_TRANSPORT_RETAINED`,
`ALPHA0_RETAINED`, or `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and
green, but they do not close the alpha0 transport handoff:

| PR | state at refresh | alpha0 transport effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no alpha0 transport |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no alpha0 transport |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no QED threshold transport |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no alpha0 transport package |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 tensor context; no alpha0 bridge |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no QED threshold moment |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | electron-readout route support, not alpha0 transport |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | atomic hygiene context, not alpha0 closure |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | status progress for old `AC_phi_lambda` atoms; no alpha0 bridge |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| the alpha0 packet supplied a decision contract | the current-surface non-supply boundary is explicit |
| retained `alpha_EM(M_Z)` and `b_QED = 32/3` could be overread as low-energy alpha | high-scale/structural support is separated from threshold/matching transport |
| admitted `R(s)` and zero-import substrate `R(s)` could be conflated | the zero-import branch still requires retained Lane 1 substrate `R(s)` |

## No-Go Discipline Gate

This section prevents overclaiming. The broad alpha0-retention no-go is not
shipped. The narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
ALPHA0_TRANSPORT_RETAINED, ALPHA0_RETAINED, or
RETAINED_ALPHA0_LOW_ENERGY_COULOMB.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full alpha0 transport contract | Accept all eleven contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| direct high-scale route | Use retained `alpha_EM(M_Z)` as atomic `alpha(0)`. | ATTEMPTED BY PRIOR. The Rydberg firewall shows the low-energy shift is load-bearing. |
| `b_QED`-only route | Use structural `b_QED = 32/3` to run down without thresholds. | ATTEMPTED BY PRIOR. Threshold placement and finite matching remain undetermined. |
| QED loop-kernel-only route | Retain the vacuum-polarization integrand while leaving thresholds open. | ATTEMPTED. It does not determine `T_EM`, hadronic `R(s)`, or finite matching. |
| Lane 6 charged-threshold route | Retain charged-lepton thresholds and call alpha0 done. | ATTEMPTED AS COMPLETE ALPHA ROUTE. R-Q-Heavy, R-Had-NP, loop kernel, and scheme matching remain. |
| Lane 6 plus Lane 3 route | Retain charged-lepton and heavy-quark thresholds. | PARTIAL ONLY. Nonperturbative hadronic vacuum polarization remains. |
| admitted `R(s)` route | Use literature hadronic `R(s)` data. | VALID RETAINED-WITH-IMPORT ROUTE. It is not the zero-import branch. |
| comparator-fit route | Choose `T_EM`, `Delta_match`, or `M_eff` to reproduce observed alpha0. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |
| open-PR shortcut | Treat the current clean open PR surface as alpha0 closure. | ATTEMPTED. The refreshed PRs are theta, chirality, runner, YT/P1, S3, quark, Koide, static-source hygiene, and Tier-A status work, not alpha0 transport. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| high-scale alpha <-> QED loop kernel | no | independent |
| QED loop kernel <-> R-Lep | no | independent |
| QED loop kernel <-> R-Q-Heavy | no | independent |
| QED loop kernel <-> R-Had-NP | no | independent |
| R-Lep <-> R-Q-Heavy | no | independent |
| R-Lep <-> R-Had-NP | no | independent |
| R-Q-Heavy <-> R-Had-NP | no | independent |
| threshold content <-> scheme/decoupling matching | no | independent on current surface |
| owner ratification <-> audit acceptance | no | independent |

The collapsed wall is the eleven-input contract above, with current pressure
on loop kernel, threshold/matching content, hadronic substrate, and
scheme/decoupling inputs.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `alpha_EM(M_Z)` | retained starting input, not low-energy alpha |
| `QED loop kernel` | explicit missing transport input |
| `threshold` / `matching` / `decoupling` | explicit missing transport inputs |
| `R(s)` / `hadronic` | explicit Lane 1 substrate or retained-with-import branch |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `observed` / `fitted` / `comparator` | excluded as proof input |

No loop integrand, threshold mass, hadronic spectrum, matching convention, or
low-energy coupling value is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| alpha QED loop-kernel target discriminator | alpha transport target inputs | alpha0 transport non-supply | yes |
| alpha0 transport packet | owner/audit handoff contract | current-surface non-supply | yes |
| Lane 2 QED running firewall | R-Lep/R-Q-Heavy/R-Had-NP split | threshold content | yes |
| alpha0 running bridge boundary | high-scale alpha alone fails | high-scale shortcut | yes |
| QED threshold bridge firewall runner | `b_QED` and threshold placement underdetermination | `b_QED`-only shortcut | yes |
| alpha0 threshold-moment runner | one-loop threshold moment bookkeeping | finite target algebra | yes |
| static-source Rydberg discriminator | alpha0 as final hydrogen input | downstream boundary | yes |
| current open PR surface | moving review context | alpha0 transport closure | no closure; context only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply alpha0
transport."

| resolution | tested? | outcome |
|---|---:|---|
| direct high-scale substitution | yes | not alpha0; misses Rydberg scale |
| structural coefficient support | yes | gives `b_QED = 32/3`, not thresholds |
| one-loop threshold moment | yes | exposes missing `T_EM` and matching |
| admitted hadronic-data route | yes | useful retained-with-import route, not zero-import |
| all-order future framework alpha0 derivation | not closed | left open as a valid future route |

No universal no-go against future `alpha(0)` derivation is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained QED loop-kernel theorem | `QED_LOOP_KERNEL_RETAINED` |
| retained Lane 6 charged-lepton thresholds | `R_LEP_THRESHOLDS_RETAINED` |
| retained Lane 3 heavy-quark thresholds | `R_Q_HEAVY_THRESHOLDS_RETAINED` |
| retained Lane 1 substrate `R(s)` computation | `R_HAD_NP_RETAINED` |
| explicit admitted literature `R(s)` route | retained-with-import alpha lane |
| retained scheme/decoupling theorem | `SCHEME_DECOUPLING_MATCHING_RETAINED` |
| owner/audit acceptance of the existing alpha0 transport packet | `ALPHA0_TRANSPORT_RETAINED` after all inputs are present |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that this note over-polices standard physics:
once `alpha_EM(M_Z)`, charge weights, and charged masses are retained,
ordinary QED running plus decoupling should be infrastructure, not another
framework theorem. The strongest version says the loop kernel and threshold
scheme should be treated like the Bohr operator harness. This note preserves
that positive route, but zero-import retained hydrogen cannot import the
threshold masses, literature hadronic `R(s)`, observed `alpha(0)`, or finite
matching convention as background.

### N8 - Cross-Cycle Echo

This echoes prior alpha firewalls: direct high-scale substitution failed,
`b_QED`-only running was underdetermined, and threshold-moment fitting was
exposed as comparator bookkeeping. The same mechanism applies here: retain
the structural coefficient as real support, but do not spend it as the
low-energy Coulomb coupling.

**Gate result:** broad alpha0 no-go fails; narrowed current-surface
non-supply claim passes.

## Explicit Non-Claims

- No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.
- No derivation or ratification of `ALPHA0_RETAINED`.
- No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.
- No derivation or ratification of the QED loop kernel.
- No derivation or ratification of `T_EM` or `Delta_match`.
- No derivation or ratification of charged-lepton, heavy-quark, or hadronic
  thresholds.
- No derivation or ratification of hadronic `R(s)`.
- No derivation or ratification of the scheme/decoupling convention.
- No derivation of `m_e`, static-source Rydberg, or full hydrogen
  spectroscopy.
- No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or
  literature `R(s)` as proof inputs on the zero-import branch.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_alpha0_transport_current_surface_no_go.py
```

The verifier checks the current-surface boundary, alpha0 transport predicate,
finite threshold target arithmetic, primitive registry, open PR alignment,
No-Go Discipline markers, and explicit non-claims.
