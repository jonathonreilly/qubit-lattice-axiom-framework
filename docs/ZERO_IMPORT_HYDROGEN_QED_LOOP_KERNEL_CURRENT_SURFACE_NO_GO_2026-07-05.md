# Zero-Import Hydrogen: QED Loop-Kernel Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify the QED loop kernel, does
not derive `alpha(0)`, does not derive `m_e`, does not derive static-source
Rydberg, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_qed_loop_kernel_current_surface_no_go.py`

## Scope

The Lane 2 alpha0 transport package consumes one substrate-level input:

```text
QED_LOOP_KERNEL_RETAINED.
```

This is not the retained high-scale value `alpha_EM(M_Z)`, not the structural
above-threshold charge/count coefficient `b_QED = 32/3`, and not the threshold
moment `T_EM`. The QED loop-kernel handoff is the retained framework-substrate
vacuum-polarization kernel and charge insertion rule needed before threshold
transport can become more than textbook QED background.

The narrow result is not "the QED loop kernel cannot be retained." The narrow
result is that current retained, primitive, and open-PR surfaces do not supply
`QED_LOOP_KERNEL_RETAINED`.

## QED Loop-Kernel Contract

A future QED loop-kernel handoff needs all eleven inputs:

```text
QED_LOOP_KERNEL_TEXT_LOCK
FRAMEWORK_QED_PROPAGATOR_SURFACE_RETAINED
VACUUM_POLARIZATION_INTEGRAND_RETAINED
CHARGE_INSERTION_RULE_RETAINED
RENORMALIZATION_SUBTRACTION_RETAINED
WARD_IDENTITY_OR_CHARGE_CONSERVATION_RETAINED
THRESHOLD_DECOUPLING_INTERFACE_LOCK
NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If all eleven inputs are accepted, the conditional consequence would be:

```text
QED_LOOP_KERNEL_RETAINED.
```

That consequence is not supplied here. The current missing inputs include:

```text
FRAMEWORK_QED_PROPAGATOR_SURFACE_RETAINED
VACUUM_POLARIZATION_INTEGRAND_RETAINED
CHARGE_INSERTION_RULE_RETAINED
RENORMALIZATION_SUBTRACTION_RETAINED
WARD_IDENTITY_OR_CHARGE_CONSERVATION_RETAINED
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

This handoff is Lane 2 support only. It does not derive threshold masses, the
hadronic substrate, scheme/decoupling matching, `alpha(0)`, `m_e`, or
hydrogen.

## Finite Kernel Target Arithmetic

The alpha target uses the one-loop transport form:

```text
alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match

T_EM = sum_f N_c(f) Q_f^2 log(M_Z / m_f^eff).
```

The retained charge/count surface fixes only the weights:

```text
sum_f N_c(f) Q_f^2 = 8
b_QED = (4/3) * 8 = 32/3.
```

The loop-kernel target is the substrate rule that licenses the
vacuum-polarization integrand, charge insertion, subtraction, and Ward/charge
conservation discipline behind that transport. The coefficient arithmetic
does not supply the kernel. The threshold-moment arithmetic does not supply
the kernel. Comparator values for `alpha(0)` or the Rydberg do not supply the
kernel.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` | names `QED_LOOP_KERNEL_RETAINED` as an alpha0 transport input | current retained QED loop kernel |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | alpha0 owner/audit handoff consuming `QED_LOOP_KERNEL_RETAINED` | loop-kernel derivation |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | downstream alpha0 non-supply boundary | standalone loop-kernel closure |
| `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | R-Lep/R-Q-Heavy/R-Had-NP split and names the QED loop primitive as open | retained loop kernel |
| `ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md` | high-scale alpha alone does not determine alpha0 | loop kernel |
| `frontier_atomic_qed_threshold_bridge_firewall.py` | `b_QED` threshold-placement underdetermination | retained kernel |
| `frontier_atomic_alpha0_threshold_moment_no_go.py` | threshold-moment target arithmetic | retained kernel |
| `SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md` | structural above-threshold `b_QED = 32/3` support | loop integrand, subtraction, or threshold interface |
| `docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md` | retained high-scale `alpha_EM(M_Z)` surface | low-energy QED loop-kernel transport |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | QED propagator/action, loop integrand, charge insertion, subtraction, threshold decoupling, or alpha0 |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `qed_loop_kernel_primitive`,
`vacuum_polarization_primitive`, `charge_insertion_primitive`,
`renormalization_subtraction_primitive`, `ward_identity_primitive`, or
`alpha0_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and
green, but they do not close the QED loop-kernel handoff:

| PR | state at refresh | QED loop-kernel effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no QED loop kernel |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no QED loop kernel |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no QED transport kernel |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no QED loop kernel |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 tensor context; no QED loop kernel |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no alpha loop kernel |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | electron-readout route support, not QED loop transport |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | atomic hygiene context, not alpha0 transport |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | status progress for old `AC_phi_lambda` atoms; no QED loop kernel |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| alpha0 transport named `QED_LOOP_KERNEL_RETAINED` as a missing input | the standalone current-surface non-supply boundary for that input is explicit |
| retained `b_QED = 32/3` could be overread as the whole QED running bridge | coefficient support is separated from the loop-kernel theorem |
| alpha0 no-go carried the loop-kernel blocker only as one item in an eleven-input package | the QED loop target remains needed before alpha0 transport can spend QED substrate support |

## No-Go Discipline Gate

This section prevents overclaiming. The broad QED loop-kernel no-go is not
shipped. The narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
QED_LOOP_KERNEL_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full loop-kernel contract | Accept all eleven loop-kernel contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| `b_QED` coefficient route | Treat structural `b_QED = 32/3` as the loop kernel. | ATTEMPTED BY PRIOR. It supplies only above-threshold charge/count support, not the loop integrand or subtraction rule. |
| textbook QED import route | Reuse the standard QED vacuum-polarization formula as background. | VALID IMPORT ROUTE, NOT ZERO-IMPORT RETENTION. It needs explicit admission or retained derivation. |
| threshold-moment route | Use `T_EM` target arithmetic to infer the kernel. | ATTEMPTED. Threshold-moment bookkeeping presupposes a loop transport rule and does not derive it. |
| alpha0 packet shortcut | Treat the alpha0 transport decision packet as already accepting `QED_LOOP_KERNEL_RETAINED`. | ATTEMPTED. The packet packages the input; it does not ratify it. |
| primitive shortcut | Treat approved primitives as supplying QED propagation or vacuum polarization. | RULED OUT BY CURRENT METHODOLOGY. The registry supplies no such primitive. |
| open-PR shortcut | Treat the current clean open PR surface as loop-kernel closure. | ATTEMPTED. The refreshed PRs are theta, chirality, runner, YT/P1, S3, quark, Koide, static-source hygiene, and Tier-A status work. |
| comparator-fit route | Choose the kernel or finite subtraction to reproduce observed `alpha(0)` or Rydberg. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| framework QED propagator/action surface <-> vacuum-polarization integrand | no | independent on current surface |
| vacuum-polarization integrand <-> charge insertion rule | no | independent on current surface |
| charge insertion rule <-> Ward/charge-conservation discipline | no | independent on current surface |
| renormalization subtraction <-> threshold-decoupling interface | no | independent on current surface |
| no comparator proof input <-> owner ratification | no | independent controls |
| owner ratification <-> audit acceptance | no | independent controls |

The collapsed wall is the eleven-input contract above. It is not a claim that
each wall must be solved by a separate theorem; a future retained QED kernel
theorem could close multiple inputs together.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `standard QED` / `textbook` | import route, not retained background |
| `kernel` / `integrand` | explicit decision content |
| `charge insertion` | explicit decision content |
| `Ward` / `charge conservation` | explicit decision content |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `comparator` / `observed` / `Rydberg` | excluded as proof input |

No QED action, propagator, loop integrand, subtraction scheme, threshold
interface, owner decision, or audit decision is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| alpha QED loop-kernel target discriminator | names loop kernel as alpha transport input | QED loop-kernel handoff | yes |
| alpha0 transport packet | consumes `QED_LOOP_KERNEL_RETAINED` | downstream dependency | yes |
| alpha0 current-surface no-go | alpha0 package non-supply | downstream blocker | yes |
| Lane 2 QED running firewall | QED loop primitive remains textbook/input-side | loop-kernel non-supply | yes |
| QED threshold bridge firewall runner | `b_QED` alone underdetermines low-energy alpha | coefficient-only shortcut | yes |
| alpha0 threshold-moment runner | target moment arithmetic presupposes transport | threshold-moment shortcut | yes |
| structural beta-coefficient note | `b_QED = 32/3` support | coefficient, not kernel | partial support only |
| current open PR surface | moving review context | loop-kernel closure | no closure; context only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`QED_LOOP_KERNEL_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| structural coefficient `b_QED = 32/3` | yes | support only |
| one-loop target arithmetic | yes | target bookkeeping only |
| textbook QED running formula | yes | import route unless retained |
| full framework QED kernel derivation | not closed | left open as a positive route |
| all-order alpha0 transport | not closed | downstream of this and threshold/matching inputs |

No universal no-go against future QED loop-kernel retention is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained framework QED propagator/action theorem | framework substrate surface |
| retained one-loop vacuum-polarization theorem | integrand and charge insertion |
| retained Ward/charge-conservation theorem for the loop insertion | gauge/charge discipline |
| retained subtraction and threshold-interface theorem | matching to `T_EM` and decoupling |
| explicit admitted textbook-QED bridge | retained-with-import alpha lane, not zero-import |
| owner/audit acceptance of a QED loop-kernel packet | `QED_LOOP_KERNEL_RETAINED` after all inputs are visible |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that this note is too conservative: ordinary QED
vacuum polarization is a mathematical theorem of a supplied gauge-field
substrate, and the repo already uses textbook running language in the Lane 2
firewall. If the framework has retained electroweak gauge content and retained
charge assignments, the one-loop kernel might be treated as standard
downstream calculation rather than a separate owner/audit handoff. This note
preserves that route, but it cannot spend textbook QED, a subtraction scheme,
or a propagator/action surface as zero-import retained content until the
framework-substrate theorem or explicit import boundary is accepted.

### N8 - Cross-Cycle Echo

This echoes the prior alpha firewalls: direct high-scale substitution failed,
`b_QED`-only running was underdetermined, and threshold-moment fitting was
exposed as comparator bookkeeping. The same mechanism applies here: retain
the structural coefficient as real support, but do not spend it as the QED
loop-kernel theorem.

**Gate result:** broad QED loop-kernel no-go fails; narrowed current-surface
non-supply claim passes.

## Explicit Non-Claims

- No derivation or ratification of `QED_LOOP_KERNEL_RETAINED`.
- No derivation or ratification of a framework QED propagator/action surface.
- No derivation or ratification of the vacuum-polarization integrand.
- No derivation or ratification of the charge insertion rule.
- No derivation or ratification of the renormalization subtraction rule.
- No derivation or ratification of the threshold-decoupling interface.
- No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.
- No derivation or ratification of `ALPHA0_RETAINED`.
- No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.
- No derivation of threshold masses, hadronic `R(s)`, `T_EM`, or
  `Delta_match`.
- No derivation of `m_e`, static-source Rydberg, or full hydrogen.
- No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or
  literature `R(s)` as proof input.
- No new axiom, primitive, Tier-A admission, or empirical import.
- No audit status change for any cited row.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_qed_loop_kernel_current_surface_no_go.py
```
