# Zero-Import Hydrogen: Alpha0 Transport Ratification Decision Packet

**Date:** 2026-07-04
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify `alpha(0)`, does not
derive `m_e`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_alpha0_transport_ratification_decision_packet.py`

## Purpose

The static-source hydrogen target needs the low-energy Coulomb coupling:

```text
E_H = m_e alpha(0)^2.
```

The repo already has retained high-scale electroweak support:

```text
alpha_EM(M_Z)^-1 = 127.67,
b_QED = 32/3.
```

The alpha QED loop-kernel target discriminator shows why this is not enough.
The running step from `alpha_EM(M_Z)` to `alpha(0)` also needs a QED loop
kernel, charged thresholds, hadronic vacuum-polarization content, and
scheme/decoupling matching. This packet packages that Lane 2 step as one
ratification decision object for zero-import hydrogen.

## Decision Object

The decision object is exactly:

```text
the zero-import alpha(0) transport package for the static-source hydrogen lane.
```

It has six content clauses:

| clause | decision text |
|---|---|
| A0.1 | high-scale input: retained `alpha_EM(M_Z)` is the starting coupling |
| A0.2 | loop kernel: the framework substrate supplies the QED vacuum-polarization kernel and charge insertion rule |
| A0.3 | charged thresholds: Lane 6 supplies R-Lep and Lane 3 supplies R-Q-Heavy without PDG mass proof input |
| A0.4 | hadronic substrate: Lane 1 supplies R-Had-NP from substrate `R(s)`, or the packet is explicitly downgraded to retained-with-import |
| A0.5 | scheme/decoupling: threshold placement, finite matching, and decoupling convention are retained |
| A0.6 | comparator exclusion: observed `alpha(0)`, Rydberg spectroscopy, PDG masses, fitted thresholds, or literature `R(s)` are not proof inputs on the zero-import branch |

The object deliberately excludes physical electron readout, the static-source
nonrelativistic Coulomb limit, and the final Rydberg substitution.

## Ratification Decision Contract

This packet is decision-ready only if all eleven contract inputs are visible:

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

The contract means:

1. **ALPHA0_TRANSPORT_TEXT_LOCK:** the A0.1-A0.6 text above is the complete
   object being decided.
2. **ALPHA_MZ_RETAINED:** the starting high-scale coupling is retained on the
   repo's electroweak surface.
3. **QED_LOOP_KERNEL_RETAINED:** the QED vacuum-polarization kernel and charge
   insertion rule are retained on the framework substrate.
4. **R_LEP_THRESHOLDS_RETAINED:** charged-lepton thresholds are retained
   downstream of Lane 6, not imported from PDG lepton masses.
5. **R_Q_HEAVY_THRESHOLDS_RETAINED:** heavy-quark thresholds are retained
   downstream of Lane 3, not imported from PDG quark masses.
6. **R_HAD_NP_RETAINED:** hadronic vacuum polarization is retained from Lane 1
   substrate `R(s)` rather than admitted literature `R(s)` data.
7. **SCHEME_DECOUPLING_MATCHING_RETAINED:** the threshold scheme, decoupling,
   and finite matching convention are retained.
8. **NO_COMPARATOR_PROOF_INPUT:** observed `alpha(0)`, Rydberg, PDG masses,
   fitted effective thresholds, and literature `R(s)` are excluded as proof
   inputs on the zero-import branch.
9. **NO_NEW_PRIMITIVE_OR_AXIOM:** the packet does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
10. **OWNER_RATIFICATION:** the owner explicitly accepts the transport package
    boundary or retained theorem boundary.
11. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the alpha0
    transport decision and its dependency consequences.

No proper subset of those eleven contract inputs is a retained alpha0
transport decision.

## Conditional Consequence

If all eleven contract inputs are accepted, the conditional consequence is:

```text
ALPHA0_TRANSPORT_RETAINED
ALPHA0_RETAINED
```

That consequence is Lane 2 support only. It does not by itself give retained
static-source hydrogen. The static-source hydrogen predicate still requires:

```text
STATIC_SOURCE_RYDBERG_RETAINED
  requires RETAINED_ELECTRON_MASS_PHYSICAL_UNIT
  + RETAINED_ALPHA0_LOW_ENERGY_COULOMB
  + RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT
  + ATOMIC_OPERATOR_HARNESS_VERIFIED
  + NO_RYDBERG_COMPARATOR_PROOF_INPUT
  + AUDIT_ACCEPTANCE.
```

This packet supplies only the alpha side of that predicate if accepted.

## Finite Target Algebra

The one-loop target surface used by the alpha discriminator is:

```text
alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match,

T_EM = sum_f N_c(f) Q_f^2 log(M_Z / m_f^eff).
```

The retained charge/count support fixes the total charge weight:

```text
sum_f N_c(f) Q_f^2 = 8,
b_QED = (4/3) * 8 = 32/3.
```

Comparator bookkeeping, not proof input:

```text
alpha_EM(M_Z)^-1 = 127.67
alpha(0)^-1 comparator = 137.035999084
Delta inverse alpha = 9.365999084
T_EM_target = 44.136...
common log = T_EM_target / 8 ~= 5.517
M_eff ~= M_Z * exp(-common log) ~= 0.37 GeV
```

This shows the scale of the missing threshold/matching content. It does not
derive `T_EM`, `Delta_match`, hadronic `R(s)`, or `alpha(0)`.

The QED loop-kernel current-surface no-go
`ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`QED_LOOP_KERNEL_RETAINED`; the QED loop target remains needed before this
packet can spend QED substrate support.

The R-Lep thresholds current-surface no-go
`ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`R_LEP_THRESHOLDS_RETAINED`; the R-Lep threshold target remains needed before
this packet can spend charged-lepton threshold support.

The alpha0 transport current-surface no-go
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`ALPHA0_TRANSPORT_RETAINED`, `ALPHA0_RETAINED`, or
`RETAINED_ALPHA0_LOW_ENERGY_COULOMB`. It preserves this packet as the positive
owner/audit route while keeping the QED loop kernel, charged-lepton thresholds,
heavy-quark thresholds, hadronic substrate, scheme/decoupling, owner, and
audit inputs explicit.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was written.

| PR | audit status | effect on this alpha0 transport decision packet |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `SUCCESS` | theta gauge-side work; no alpha0 transport package |
| `#5012` chirality domain-wall free-field note | `SUCCESS` | adjacent chirality science; no alpha0 transport package |
| `#5011` eta twisted walk family runner | `SUCCESS` | runner stabilization; no QED threshold transport |
| `#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS` | YT/P1 diagnostic repair; no alpha0 transport package |
| `#5009` S3 spacetime tensor primitive runner | `SUCCESS` | bounded S3 tensor support context; no alpha0 bridge |
| `#5008` quark mass-ratio CP probe repair | `SUCCESS` | quark CP-area context; no QED threshold moment |
| `#5007` Koide native zero-section route guard repair | `SUCCESS` | electron-readout route support, not alpha0 transport |
| `#5006` static-source I1 hygiene companion | `SUCCESS` | atomic hygiene context, not retained static-source hydrogen |
| `#4991` owner-governed Tier-A retirement | `SUCCESS` | status progress for old `AC_phi_lambda` atoms; no alpha0 bridge |

Merge-state labels and branch ordering are moving review metadata, not proof
inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` | alpha transport target and closure inputs | target support only, not retained alpha0 |
| `ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for the QED loop kernel | `QED_LOOP_KERNEL_RETAINED` |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for charged-lepton thresholds | `R_LEP_THRESHOLDS_RETAINED` |
| `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | R-Lep/R-Q-Heavy/R-Had-NP split | reduction/firewall only |
| `ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md` | high-scale alpha alone does not determine alpha0 | boundary only |
| `frontier_atomic_qed_threshold_bridge_firewall.py` | `b_QED` plus high-scale alpha underdetermines threshold placement | firewall only |
| `frontier_atomic_alpha0_threshold_moment_no_go.py` | threshold-moment target arithmetic | no retained threshold moment |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | final static-source predicate | needs alpha0 plus electron mass and NR limit |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation | no QED loop kernel, thresholds, hadronic `R(s)`, matching convention, or alpha0 value |

The primitive registry was checked with the current origin-main methodology.
Registered primitives are approved premise nodes, but they do not supply the
alpha0 transport package.

## What This Moves

| before this packet | after this packet |
|---|---|
| alpha0 was named as a Lane 2 blocker | alpha0 has an eleven-input owner/audit decision contract |
| `b_QED = 32/3` could be overread as low-energy alpha | the packet separates coefficient support from threshold/matching transport |
| admitted `R(s)` and zero-import substrate `R(s)` could be conflated | the packet keeps admitted literature `R(s)` as retained-with-import, not zero-import |
| alpha0 could be confused with final hydrogen | the packet keeps electron mass, NR Coulomb limit, and Rydberg audit downstream |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "`alpha(0)` cannot be
derived" is not shipped. The narrowed claim is:

```text
the Lane 2 alpha0 transport package is packaged as a decision-ready
ratification contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full alpha0 contract | Accept all eleven contract inputs. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts zero-import alpha0 transport. |
| high-scale alpha route | Use retained `alpha_EM(M_Z)` directly as atomic `alpha(0)`. | ATTEMPTED BY PRIOR. The Rydberg and alpha firewalls show the low-energy shift is load-bearing. |
| `b_QED`-only route | Use structural `b_QED = 32/3` to run down without thresholds. | ATTEMPTED BY PRIOR. Threshold placement and finite matching remain undetermined. |
| Lane 6-only route | Retain charged-lepton thresholds and call alpha0 done. | ATTEMPTED AS COMPLETE ALPHA ROUTE. R-Q-Heavy, R-Had-NP, loop kernel, and scheme matching remain. |
| Lane 6 plus Lane 3 route | Retain lepton and heavy-quark thresholds. | PARTIAL ONLY. Nonperturbative hadronic vacuum polarization remains. |
| admitted `R(s)` route | Use literature hadronic `R(s)` data. | VALID RETAINED-WITH-IMPORT ROUTE. It is not the zero-import branch packaged here. |
| comparator-fit route | Choose `T_EM`, `Delta_match`, or `M_eff` to reproduce observed alpha0. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is not proof input. |
| open-PR shortcut | Treat the current clean open PR surface as alpha0 closure. | ATTEMPTED. The refreshed PRs are theta, chirality, runner, YT/P1, S3, quark, Koide, static-source hygiene, and Tier-A status work, not alpha0 transport. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| high-scale alpha <-> QED loop kernel | no in either direction | independent |
| QED loop kernel <-> R-Lep | no in either direction | independent |
| QED loop kernel <-> R-Q-Heavy | no in either direction | independent |
| QED loop kernel <-> R-Had-NP | no in either direction | independent |
| R-Lep <-> R-Q-Heavy | no in either direction | independent |
| R-Lep <-> R-Had-NP | no in either direction | independent |
| R-Q-Heavy <-> R-Had-NP | no in either direction | independent |
| threshold content <-> scheme/decoupling matching | no in either direction unless a future theorem derives both together | independent on current surface |
| OWNER_RATIFICATION <-> AUDIT_ACCEPTANCE | no in either direction | independent |

The collapsed decision wall is the eleven-input contract above.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `alpha_EM(M_Z)` | explicit retained starting input, not alpha0 |
| `QED loop kernel` | explicit transport input, not standard background |
| `threshold` / `matching` / `decoupling` | explicit transport inputs |
| `R(s)` / `hadronic` | explicit Lane 1 substrate or retained-with-import branch |
| `registered` / `primitive` | registry checked; approved primitives do not supply alpha0 transport |
| `observed` / `fitted` / `comparator` | excluded as proof input |

No threshold mass, hadronic spectrum, matching convention, or low-energy
coupling value is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| alpha QED loop-kernel target discriminator | alpha transport target inputs | A0.1-A0.6 contract | yes |
| Lane 2 QED running firewall | R-Lep/R-Q-Heavy/R-Had-NP split | threshold content | yes |
| alpha0 running bridge boundary | high-scale alpha alone fails | high-scale shortcut | yes |
| QED threshold bridge firewall runner | `b_QED` and threshold placement underdetermination | `b_QED`-only shortcut | yes |
| alpha0 threshold-moment runner | one-loop threshold moment bookkeeping | finite target algebra | yes |
| static-source Rydberg discriminator | alpha0 as final hydrogen input | downstream boundary | yes |
| current open PR surface | moving review context | alpha0 transport closure | no closure; context only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The note avoids the broad phrase "`alpha(0)` cannot be derived." The tested
resolution is narrower:

| resolution | tested? | outcome |
|---|---|---|
| direct high-scale substitution | yes | not alpha0; misses Rydberg scale |
| structural coefficient support | yes | gives `b_QED = 32/3`, not thresholds |
| one-loop threshold moment | yes | exposes missing threshold/matching content |
| admitted hadronic-data route | yes | useful retained-with-import route, not zero-import |
| all-order future framework alpha0 derivation | not closed | left open as a valid future route |

### N6 - Partial-Closure Path Scan

There are legitimate partial-closure paths:

| path | what it could close |
|---|---|
| retained QED loop-kernel theorem | QED loop kernel |
| retained Lane 6 charged-lepton mass/readout package | R-Lep |
| retained Lane 3 heavy-quark threshold package | R-Q-Heavy |
| retained Lane 1 substrate `R(s)` computation | zero-import R-Had-NP |
| explicit admitted literature `R(s)` route | retained-with-import alpha lane |
| retained scheme/decoupling theorem | finite matching ambiguity |

These are import-retirement paths, not automatic new axioms.

### N7 - Steelman

A hostile reviewer can argue that this packet is too procedural: once the repo
has retained `alpha_EM(M_Z)`, retained charge weights, and future retained
charged masses, standard QED running is ordinary physics, not a separate
framework theorem. The strongest version says the loop kernel and decoupling
scheme should be treated as textbook infrastructure just like the final Bohr
formula. The narrow reply is that the user asked for zero-import retained
hydrogen. Standard running contains threshold masses, nonperturbative hadronic
vacuum polarization, finite matching conventions, and observed `R(s)` data in
ordinary practice. Those are precisely the imports this packet makes explicit.

### N8 - Cross-Cycle Echo

This mirrors the earlier atomic Lane 2 firewalls: direct high-scale alpha
substitution failed, `b_QED`-only running was underdetermined, and threshold
moment fitting was exposed as comparator bookkeeping. The same mechanism
applies here: retain the structural coefficient as real support, but do not
spend it as the low-energy Coulomb coupling.

**Gate result:** broad no-go fails; narrowed alpha0 transport decision packet
passes.

## Explicit Non-Claims

- No derivation or ratification of `alpha(0)`.
- No derivation or ratification of the QED loop kernel.
- No derivation or ratification of `T_EM` or `Delta_match`.
- No derivation or ratification of charged-lepton, heavy-quark, or hadronic
  thresholds.
- No derivation or ratification of hadronic `R(s)`.
- No derivation or ratification of the scheme/decoupling convention.
- No derivation of `m_e`.
- No derivation of the static-source nonrelativistic Coulomb limit.
- No retained hydrogen calculation.
- No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or
  literature `R(s)` as proof inputs on the zero-import branch.
- No new axiom, primitive, Tier-A admission, or empirical import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_alpha0_transport_ratification_decision_packet.py
```

The verifier checks the contract predicate, threshold-moment arithmetic,
authority boundaries, primitive registry, current open-PR alignment,
No-Go Discipline sections, and explicit non-claims.
