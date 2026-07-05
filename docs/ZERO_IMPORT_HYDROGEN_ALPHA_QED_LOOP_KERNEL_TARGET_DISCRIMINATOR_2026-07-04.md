# Zero-Import Hydrogen: Alpha QED Loop-Kernel Target Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / alpha-running target support
**Claim type:** Lane 2 alpha transport dependency target
**Status:** support-only. This note does not derive `alpha(0)`, does not
derive `m_e`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_alpha_qed_loop_kernel_target_discriminator.py`

## Scope

The hydrogen Hartree scale needs:

```text
E_H = m_e alpha(0)^2.
```

The current repo has retained electroweak-scale coupling information, including
`alpha_EM(M_Z)`, and it has structural charge/count support for the
above-threshold QED coefficient `b_QED = 32/3`. That is not enough to close
the low-energy Coulomb coupling.

This discriminator isolates the smallest alpha-running target that is useful
for the zero-import hydrogen program:

```text
ALPHA0_TRANSPORT_TARGET =
  retained QED loop kernel
  + retained threshold/matching moment
  + retained Lane 6 charged-lepton thresholds
  + retained Lane 3 heavy-quark thresholds
  + retained Lane 1 hadronic vacuum-polarization substrate
  + retained scheme/decoupling boundary
  + no alpha(0) or Rydberg comparator as proof input.
```

It is a target discriminator, not a closure theorem.

## Source Dependencies

| source | supplies | boundary here |
|---|---|---|
| `ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md` | direct `alpha_EM(M_Z)` substitution misses the Rydberg scale by about 15 percent | names `alpha(0)` transport as load-bearing |
| `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | splits `alpha_EM(M_Z) -> alpha(0)` into R-Lep, R-Q-Heavy, R-Had-NP, and a QED loop primitive | does not retain the loop kernel or thresholds |
| `frontier_atomic_qed_threshold_bridge_firewall.py` | shows retained `b_QED = 32/3` plus `alpha_EM(M_Z)` underdetermines `alpha(0)` without threshold placement | firewall only |
| `frontier_atomic_alpha0_threshold_moment_no_go.py` | reduces one-loop alpha transport to a weighted threshold/matching moment | no retained threshold moment |
| `ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md` | earlier alpha-running boundary | guard only |
| `SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md` | structural `b_QED = 32/3` support above all SM thresholds | no threshold-resolved decoupling |
| approved primitives registry | scale reference, kinetic isotropy, realized-state evaluation, minimal axioms | no QED loop kernel, no threshold moment, no hadronic R(s), no `alpha(0)` |

The primitive registry was checked with the current origin-main methodology.
Approved primitives chain-satisfy their registered roles, but they do not
silently supply the QED loop kernel, threshold masses, hadronic matching,
scheme/decoupling rule, or the low-energy value `alpha(0)`.

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
packages the parent eleven-input handoff for `R_LEP_THRESHOLDS_RETAINED` and
`T_LEP_THRESHOLD_MOMENT_RETAINED`, while keeping QED loop, heavy-quark,
hadronic, scheme/matching, alpha0, and hydrogen closure downstream.

## Finite Target Algebra

At the one-loop target level, the threshold-moment form is:

```text
alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match,

T_EM = sum_f N_c(f) Q_f^2 log(M_Z / m_f^eff).
```

The retained charge/count surface fixes the weights:

```text
sum_f N_c(f) Q_f^2 = 8,
b_QED = (4/3) * 8 = 32/3.
```

It does not fix the logarithms, effective thresholds, or finite hadronic and
scheme matching term. Therefore `b_QED = 32/3` is necessary support for the
alpha lane, but it is not an `alpha(0)` bridge.

For scale only, using the existing comparator values:

```text
alpha_EM(M_Z)^-1 = 127.67,
alpha(0)^-1 comparator = 137.035999084,
Delta inverse alpha = 9.365999084.
```

The comparator-matching one-loop threshold moment would be:

```text
T_EM_target = (alpha(0)^-1 - alpha_EM(M_Z)^-1) * (3 pi / 2)
             = 44.139...
```

If all charged species shared one effective threshold, this would correspond
to:

```text
common log = T_EM_target / 8 ~= 5.517,
M_eff ~= M_Z * exp(-common log) ~= 0.37 GeV.
```

That number is comparator bookkeeping only. A zero-import result must derive
the threshold/matching content, not fit it to `alpha(0)`.

## Required Closure Inputs

For hydrogen purposes, alpha transport is closed only if all of these are
visible:

| input | meaning |
|---|---|
| `ALPHA_MZ_RETAINED` | the high-scale retained electroweak coupling is available |
| `QED_LOOP_KERNEL_RETAINED` | the vacuum-polarization loop kernel and charge insertion rule are retained on the framework substrate |
| `R_LEP_THRESHOLDS_RETAINED` | the charged-lepton threshold contribution is retained, downstream of Lane 6 |
| `R_Q_HEAVY_THRESHOLDS_RETAINED` | the perturbative heavy-quark threshold contribution is retained, downstream of Lane 3 |
| `R_HAD_NP_RETAINED` | the nonperturbative hadronic vacuum-polarization contribution is retained from Lane 1 substrate `R(s)`, not imported data |
| `SCHEME_DECOUPLING_MATCHING_RETAINED` | threshold scheme, decoupling, and finite matching conventions are retained |
| `NO_COMPARATOR_PROOF_INPUT` | observed `alpha(0)`, Rydberg, PDG masses, or fitted effective thresholds are excluded as proof inputs |

The admitted-observational `R(s)` route can make a useful retained-with-import
atomic lane, but it is not zero-import retained hydrogen. The zero-import lane
requires the Lane 1 substrate route for `R_HAD_NP_RETAINED`.

The alpha0 transport ratification decision packet
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md`
packages the next owner/audit handoff for this target:
ALPHA0_TRANSPORT_TEXT_LOCK, ALPHA_MZ_RETAINED, QED_LOOP_KERNEL_RETAINED,
R_LEP_THRESHOLDS_RETAINED, R_Q_HEAVY_THRESHOLDS_RETAINED,
R_HAD_NP_RETAINED, SCHEME_DECOUPLING_MATCHING_RETAINED,
NO_COMPARATOR_PROOF_INPUT, NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and
AUDIT_ACCEPTANCE. If accepted, `ALPHA0_TRANSPORT_RETAINED` and
`ALPHA0_RETAINED` follow conditionally. That is Lane 2 support only; it does
not derive `m_e`, the static-source nonrelativistic Coulomb limit, or
hydrogen.

The alpha0 transport current-surface no-go
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`ALPHA0_TRANSPORT_RETAINED`, `ALPHA0_RETAINED`, or
`RETAINED_ALPHA0_LOW_ENERGY_COULOMB`. This keeps retained `alpha_EM(M_Z)` and
`b_QED = 32/3` as support for the target, not as a current low-energy Coulomb
coupling.

The alpha0 transport assembly ladder review packet
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md`
compresses the direct alpha0 rows into one review surface: retained
high-scale alpha, QED loop kernel, R-Lep thresholds, R-Q-Heavy thresholds,
R-Had-NP substrate, scheme/decoupling matching, comparator exclusion, owner,
and audit. It is review support only; it is not retained alpha0, physical
electron mass, static-source Rydberg closure, or hydrogen.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-04 before this note was written:

| PR | status | alpha/hydrogen effect |
|---|---:|---|
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` | YT/P1 diagnostic repair; no `alpha(0)`, no QED loop-kernel target closure, no hydrogen |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` | bounded S3 tensor support context; no alpha-running bridge |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` | quark CP-area context; no QED threshold moment or alpha bridge |
| `#5007` Koide native zero-section route guard | `CLEAN` | electron-readout route guard; no alpha bridge |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | status progress for `AC_phi_lambda`/`theta`; no source-side F/L/P/R, no `alpha(0)` |

Merge-state labels are moving review metadata, not proof inputs.

## Dependency-Lane Verdict

This artifact moves the hydrogen goal by turning the alpha lane into an
auditable target:

```text
alpha_EM(M_Z) retained + b_QED = 32/3
  = support for alpha transport,
  not alpha(0).
```

The next internal alpha work is one of:

1. derive the QED vacuum-polarization loop kernel on the framework substrate;
2. derive the threshold/matching moment from retained Lane 6, Lane 3, and Lane
   1 substrate data;
3. prove a retained scheme/decoupling convention that makes the threshold
   moment unambiguous; or
4. explicitly choose a retained-with-import route by admitting `R(s)`, which is
   useful but no longer zero-import.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "`alpha(0)` cannot be
derived" is not shipped. The narrowed claim is:

```text
current retained hydrogen inputs do not close alpha transport unless the QED
loop kernel, threshold/matching moment, and R-Lep/R-Q-Heavy/R-Had-NP inputs are
also supplied.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| direct substitution | Use retained `alpha_EM(M_Z)` as atomic `alpha(0)`. | ATTEMPTED BY PRIOR. The Rydberg firewall shows the energy scale misses by about 15 percent. |
| `b_QED`-only route | Use retained charge/counts and `b_QED = 32/3` to run down. | ATTEMPTED BY PRIOR. Threshold placement is load-bearing and underdetermined. |
| QED loop-kernel-only route | Retain the vacuum-polarization integrand but leave thresholds open. | ATTEMPTED HERE. It does not determine `T_EM` or finite matching. |
| Lane 6-only route | Retain charged-lepton masses and close R-Lep. | RULED OUT AS COMPLETE ALPHA CLOSURE. R-Q-Heavy, R-Had-NP, and loop/matching remain. |
| Lane 6 + Lane 3 route | Retain charged-lepton and heavy-quark thresholds. | RULED OUT AS COMPLETE ALPHA CLOSURE. Nonperturbative hadronic vacuum polarization remains. |
| admitted `R(s)` route | Import literature hadronic `R(s)` data. | VALID NONZERO-IMPORT ROUTE. It is not zero-import retained hydrogen. |
| comparator-fit route | Choose `T_EM` or an effective threshold to reproduce observed `alpha(0)`. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is not proof input. |
| open-PR shortcut | Treat `#5010` through `#4991` as alpha closure. | ATTEMPTED. The live PR surface is YT/P1, S3, quark, Koide, and Tier-A status work, not alpha-running closure. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| QED loop kernel <-> R-Lep thresholds | no in either direction | independent |
| QED loop kernel <-> R-Q-Heavy thresholds | no in either direction | independent |
| QED loop kernel <-> R-Had-NP | no in either direction | independent |
| R-Lep <-> R-Q-Heavy | no in either direction | independent |
| R-Lep <-> R-Had-NP | no in either direction | independent |
| R-Q-Heavy <-> R-Had-NP | no in either direction | independent |
| threshold moment <-> scheme/decoupling matching | no in either direction | independent unless a future theorem derives both together |

The collapsed wall set is not "derive every alpha route." It is: provide a
complete alpha-transport package with loop kernel, threshold/matching content,
and no comparator proof input.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `QED loop kernel` | explicit target, not background |
| `threshold` / `matching` / `decoupling` | explicit alpha-transport inputs |
| `hadronic R(s)` | explicit Lane 1 substrate or admitted-import branch |
| `primitive` / `registered` | registry checked; approved primitives do not supply alpha transport |
| `comparator` / `observed` | forbidden as proof input |

No loop integrand, threshold, matching convention, hadronic spectrum, or
low-energy coupling value is left as "standard" background.

### N4 - Residual Matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md` | direct alpha substitution into hydrogen | yes, direct-substitution route |
| `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | R-Lep/R-Q-Heavy/R-Had-NP split and QED loop primitive | yes |
| `frontier_atomic_qed_threshold_bridge_firewall.py` | `b_QED`-only threshold underdetermination | yes |
| `frontier_atomic_alpha0_threshold_moment_no_go.py` | threshold/matching moment reduction | yes |
| `SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md` | structural `b_QED = 32/3` support | partial: coefficient only |
| open PRs `#5010` through `#4991` | moving review context | no alpha closure; review context only |

Only matching alpha-transport residuals are counted as support.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "the current retained surface does not
close alpha transport."

| resolution | tested? | result |
|---|---:|---|
| direct hydrogen substitution | yes | fails by about 15 percent |
| asymptotic charge/count coefficient | yes | gives `b_QED = 32/3`, not thresholds |
| one-loop threshold moment | yes | exposes missing `T_EM` and matching |
| full all-order QED/QCD/hadronic running | not closed | left open as future retained target |

No universal no-go against future `alpha(0)` derivation is claimed.

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained QED loop-kernel theorem | loop-kernel wall |
| retained Lane 6 charged-lepton thresholds | R-Lep |
| retained Lane 3 heavy-quark thresholds | R-Q-Heavy |
| retained Lane 1 substrate `R(s)` computation | zero-import R-Had-NP |
| admitted literature `R(s)` | nonzero-import atomic alpha route |
| retained scheme/decoupling theorem | matching ambiguity |

These are import-retirement paths, not automatic new axioms.

### N7 - Steelman

A hostile reviewer can argue that this packet is too conservative: the repo
already has retained `alpha_EM(M_Z)` and retained `b_QED = 32/3`, so only
ordinary threshold bookkeeping remains, and ordinary threshold bookkeeping is a
standard QED bridge. The narrow reply is that hydrogen is asking for
zero-import retained `alpha(0)`. Standard QED threshold bookkeeping contains
the exact masses, hadronic vacuum-polarization content, decoupling scheme, and
finite matching conventions that determine the low-energy value. Until those
are retained or explicitly admitted, the bridge is still load-bearing.

### N8 - Cross-Cycle Echo

This mirrors prior atomic Lane 2 firewalls: direct `alpha_EM(M_Z)` substitution
failed, `b_QED`-only running was underdetermined, and threshold-moment fitting
was exposed as comparator bookkeeping. The same mechanism applies here: keep
the structural coefficient as real support, but do not spend it as the
low-energy Coulomb coupling.

**Gate result:** broad no-go fails; narrowed alpha target discriminator passes.

## Explicit Non-Claims

- No derivation of `alpha(0)`.
- No derivation of the QED loop kernel.
- No derivation of `T_EM`.
- No derivation of charged-lepton, heavy-quark, or hadronic thresholds.
- No derivation of hadronic `R(s)`.
- No use of observed `alpha(0)` or Rydberg spectroscopy as proof inputs.
- No derivation of `m_e`.
- No retained hydrogen calculation.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_alpha_qed_loop_kernel_target_discriminator.py
```

The verifier checks the source paths, threshold-moment arithmetic, primitive
boundary, closure predicates, open-PR alignment, no-go discipline section, and
explicit non-claims.
