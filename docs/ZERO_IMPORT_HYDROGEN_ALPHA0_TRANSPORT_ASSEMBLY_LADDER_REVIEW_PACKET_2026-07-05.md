# Zero-Import Hydrogen: Alpha0 Transport Assembly Ladder Review Packet

**Date:** 2026-07-05
**Type:** support / review-compression packet
**Status:** review support only; this packet does not ratify `alpha(0)`
**Verifier:** `scripts/frontier_zero_import_hydrogen_alpha0_transport_assembly_ladder_review_packet.py`

## Result

This packet compresses the direct alpha0 transport dependency ladder into one
reviewable surface. It does not supply `ALPHA0_TRANSPORT_RETAINED`,
`ALPHA0_RETAINED`, or `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`; it records how the
already-open high-scale alpha, QED loop-kernel, R-Lep, R-Q-Heavy, R-Had-NP,
and scheme/decoupling rows sit under the parent alpha0 transport handoff.

The useful grouped lane is:

```text
ALPHA_MZ_RETAINED
  + QED_LOOP_KERNEL_RETAINED
  + R_LEP_THRESHOLDS_RETAINED
  + R_Q_HEAVY_THRESHOLDS_RETAINED
  + R_HAD_NP_RETAINED
  + SCHEME_DECOUPLING_MATCHING_RETAINED
  + alpha0 owner/audit contract
  -> ALPHA0_TRANSPORT_RETAINED
  -> ALPHA0_RETAINED
  -> RETAINED_ALPHA0_LOW_ENERGY_COULOMB
```

This is the largest scientifically coherent next bundle because all six
middle rows are direct inputs to the parent alpha0 transport contract. It
would be premature to bundle physical electron mass, static-source Rydberg
closure, or full hydrogen into the same claim: those are downstream or sibling
lanes, not direct alpha0 transport closure clauses.

## Parent Alpha0 Contract

The parent decision object remains the eleven-input handoff in
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md`:

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

No proper subset of those eleven contract inputs is treated here as a retained
alpha0 transport handoff. If the parent contract is accepted with all inputs,
it conditionally supplies `ALPHA0_TRANSPORT_RETAINED` and `ALPHA0_RETAINED`.
The static-source lane consumes the corresponding low-energy Coulomb coupling
as `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`. This packet does not perform that
acceptance.

## Direct Ladder Rows

| Row | Existing packet or surface | Role in alpha0 transport | Boundary preserved |
| --- | --- | --- | --- |
| A0.0 | `ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` | names the alpha0 transport target and finite target arithmetic | target support only; not retained alpha0 |
| A0.1 | `docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md` | retained high-scale electroweak support, including `alpha_EM(M_Z)^-1 = 127.67` | not low-energy `alpha(0)` |
| A0.2 | `ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface boundary for `QED_LOOP_KERNEL_RETAINED` | no retained loop kernel |
| A0.3 | `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md` | packages the parent charged-lepton threshold handoff | no QED loop kernel, no heavy-quark thresholds, no hadronic substrate, no alpha0 |
| A0.3 no-go | `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface boundary for `R_LEP_THRESHOLDS_RETAINED` | current retained, primitive, and open-PR surfaces do not supply R-Lep thresholds |
| A0.4 | `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | separates R-Lep, R-Q-Heavy, R-Had-NP, and QED loop kernel | dependency split only; no retained thresholds |
| A0.5 | `frontier_atomic_qed_threshold_bridge_firewall.py` | shows `b_QED = 32/3` plus high-scale alpha underdetermines threshold placement | firewall only; no retained matching |
| A0.6 | `frontier_atomic_alpha0_threshold_moment_no_go.py` | threshold-moment target arithmetic | no retained `T_EM` or `Delta_match` |
| A0.7 | `ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md` | high-scale alpha alone does not determine low-energy alpha | boundary only |
| Parent | `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | packages the eleven-input alpha0 transport handoff | no `m_e`, no static-source Rydberg, no hydrogen |
| Parent no-go | `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary | no retained alpha0 transport or low-energy Coulomb coupling |

The physical electron mass and static-source packets are downstream consumers,
not proof inputs for this assembly:

- `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md`
  groups the direct `m_e` lane separately.
- `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md`
  consumes `RETAINED_ALPHA0_LOW_ENERGY_COULOMB` only after it is retained, and
  still also needs retained `m_e`, retained static-source nonrelativistic
  Coulomb limit, the atomic operator harness, and audit acceptance.
- `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md`
  groups that final static-source Rydberg consumer surface. It can spend
  `RETAINED_ALPHA0_LOW_ENERGY_COULOMB` only after the parent alpha0 transport
  contract is accepted; it is not a retained alpha0 proof input.

## Finite Witness Carried Forward

The finite arithmetic reviewed by this packet is only target bookkeeping:

```text
alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match
T_EM = sum_f N_c(f) Q_f^2 log(M_Z / m_f^eff)
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

The witness makes two boundaries visible:

- `b_QED = 32/3` is above-threshold charge/count support, not threshold
  placement, finite matching, hadronic vacuum polarization, or `alpha(0)`.
- The comparator-matching `T_EM_target` reconstructs observed `alpha(0)` by
  construction; it is not proof input on the zero-import branch.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was added. The
queue signal here is that a PR is open and lane-relevant; clean/green status
is not a prerequisite because reviewer cleanup and landing happen outside this
packet. No currently open PR supplies the alpha0 transport assembly handoff:

| PR | queue signal | effect on this alpha0 assembly |
| --- | ---: | --- |
| `#5033` RP two-step runner scope cleanup | open, clean | runner-scope cleanup; no QED loop kernel, thresholds, matching, or alpha0 |
| `#5030` finite multisite Pauli carrier provenance | open, clean | finite carrier provenance support; no alpha0 transport package |
| `#5021` primitive-retirement review | open draft, dirty | no registry edit and no alpha0 primitive shortcut |
| `#5018` domain-wall edge content vs SM chiral fermions map | open | chirality/domain-wall context; no QED threshold transport |
| `#5017` domain-wall anomaly inflow spectral flow | open | chirality/domain-wall context; no alpha0 transport |
| `#5016` zero-import hydrogen retained lane bundle | open | carries this review packet if merged; not owner/audit retention by itself |
| `#5015` wave-collapse-block01 measurement-collapse gate | open draft | measurement/collapse work; no alpha0 transport |
| `#5014` record-formation front/domain-wall chirality | open | chirality context; no low-energy Coulomb coupling |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no alpha0 |
| `#5007` Koide native zero-section route guard repair | open | useful electron-route context, not alpha0 transport |
| `#4991` owner-governed Tier-A retirement | open | governance context for old atoms; no alpha0 theorem closure |

Merge-state labels, branch ordering, and check status are moving review
metadata, not proof inputs here.

## Primitive Registry Check

The primitive registry was checked through
`docs/audit/data/axiom_premise_nodes.json` and the current primitive notes.
Registered premise nodes are:

- `minimal_axioms`
- `scale_reference_primitive`
- `kinetic_isotropy_primitive`
- `realized_state_primitive`

Those nodes chain-satisfy only their declared scopes. They do not supply a QED
loop kernel, R-Lep thresholds, R-Q-Heavy thresholds, R-Had-NP hadronic
substrate, scheme/decoupling matching, alpha0 transport, physical electron
mass, static-source Rydberg closure, or hydrogen spectroscopy.

No node named `alpha0_primitive`, `qed_loop_kernel_primitive`,
`r_lep_thresholds_primitive`, `r_q_heavy_thresholds_primitive`,
`r_had_np_primitive`, `scheme_decoupling_matching_primitive`,
`electron_mass_primitive`, or `hydrogen_primitive` is registered.

## Distance To Hydrogen

This packet moves review distance, not retained physics distance. After this
packet, the hydrogen calculation still needs:

1. Alpha0 closure: retained QED loop kernel, R-Lep thresholds, R-Q-Heavy
   thresholds, R-Had-NP substrate, scheme/decoupling matching, comparator
   exclusion, and parent owner/audit acceptance.
2. Physical electron mass closure: accepted native zero-section bridge,
   physical electron species bridge, retained K4 scale, Koide branch mass-map,
   scale-reference chain, comparator exclusions, and parent owner/audit
   acceptance.
3. Static-source Rydberg closure: retained `m_e`, retained `alpha(0)`,
   retained static-source nonrelativistic Coulomb limit, verified atomic
   operator harness, no Rydberg comparator proof input, and audit acceptance.

So the framework is closer in organization and reviewability, but this packet
does not make hydrogen one audit step away.

## No-Go Discipline Gate

The negative claim gated here is narrow: current retained, primitive, and
open-PR surfaces do not supply retained alpha0 transport merely because the
direct assembly ladder is now review-compressed. The full alpha0 transport
contract remains an open positive route.

### N1 - Alternative Route Enumeration

| Route | Attempt | Outcome |
| --- | --- | --- |
| Full parent alpha0 contract | Accept all eleven alpha0 transport inputs and owner/audit acceptance. | OPEN POSITIVE ROUTE. This packet does not reject it; it is the path to retained alpha0 transport. |
| High-scale-alpha-only closure | Treat retained `alpha_EM(M_Z)` as atomic `alpha(0)`. | ATTEMPTED BY PRIOR. The Rydberg and alpha firewalls show the low-energy shift is load-bearing. |
| `b_QED`-only closure | Treat structural `b_QED = 32/3` as the full transport bridge. | ATTEMPTED. It omits threshold placement, hadronic content, and finite matching. |
| QED-loop-only closure | Treat `QED_LOOP_KERNEL_RETAINED` as alpha0. | ATTEMPTED. It omits R-Lep, R-Q-Heavy, R-Had-NP, and scheme matching. |
| R-Lep-only closure | Treat `R_LEP_THRESHOLDS_RETAINED` as alpha0. | ATTEMPTED. It omits the QED loop kernel, heavy-quark thresholds, hadronic substrate, and matching. |
| Retained-with-import `R(s)` route | Use admitted literature hadronic data. | VALID IMPORT ROUTE. It is not the zero-import branch packaged here. |
| Comparator-fit route | Choose `T_EM`, `Delta_match`, or `M_eff` to reproduce observed alpha0. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |
| Open-PR shortcut | Treat newly opened runner, primitive-review, chirality, or hydrogen PRs as retained alpha0. | ATTEMPTED. The refreshed open PR queue supplies no spendable alpha0 transport input. |

### N2 - Wall-Independence Audit

| Pair | Does first close second? | Does second close first? | Independent for alpha0 spending? |
| --- | --- | --- | --- |
| high-scale alpha / QED loop kernel | no | no | yes |
| QED loop kernel / R-Lep thresholds | no | no | yes |
| QED loop kernel / R-Q-Heavy thresholds | no | no | yes |
| QED loop kernel / R-Had-NP substrate | no | no | yes |
| R-Lep thresholds / R-Q-Heavy thresholds | no | no | yes |
| R-Q-Heavy thresholds / R-Had-NP substrate | no | no | yes |
| threshold content / scheme-decoupling matching | no | no | yes |

The collapsed alpha0 surface is one parent contract with six load-bearing
direct input rows plus comparator-exclusion, owner, and audit clauses.

### N3 - Hidden-Wall Scan

| Phrase scanned | Classification |
| --- | --- |
| `support` | non-load-bearing review role; not a retained claim |
| `current` / `current surfaces` | cited to current-surface no-go packets and open PR refresh |
| `registered` / `primitive` | tied to the explicit primitive registry check above |
| `context` | used only for open PR alignment or sibling science, not as proof input |
| `contract` | explicit parent alpha0 or child-packet owner/audit input set |
| `assembly` / `ladder` | review compression only, not an added axiom or retained consequence |
| `comparator` / `observed` / `fitted` | excluded as proof input |

No hidden admission was promoted after the scan. The direct alpha0 inputs
remain explicit.

### N4 - Residual Matching

| Witness | Residual attacked | Residual used here | Match? |
| --- | --- | --- | --- |
| `ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md` | `QED_LOOP_KERNEL_RETAINED` non-supply | A0.2 input non-supply | yes |
| `ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | `R_LEP_THRESHOLDS_RETAINED` non-supply | A0.3 input non-supply | yes |
| `ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md` | R-Lep/R-Q-Heavy/R-Had-NP split | threshold content split | yes |
| `frontier_atomic_qed_threshold_bridge_firewall.py` | coefficient-only underdetermination | `b_QED` shortcut | yes |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | alpha0 transport non-supply | parent handoff boundary | yes |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | alpha0 as final hydrogen input | downstream boundary | yes |

Non-matching electron/static-source/hydrogen surfaces are not used as evidence
for alpha0 closure or non-closure.

### N5 - Rhetoric Audit

The phrase "alpha0 is not closed by X alone" is tested only at the
contract-input resolution:

- high-scale alpha alone;
- structural `b_QED = 32/3` alone;
- QED loop kernel alone;
- R-Lep thresholds alone;
- threshold target arithmetic alone;
- opened PR metadata alone;
- approved primitive registry alone.

The packet does not claim that the parent contract is impossible. It says that
the parent contract has not been accepted by current retained, primitive, or
open-PR surfaces.

### N6 - Partial-Closure Path Scan

| Partial closure | Can it be useful? | Why it is not final alpha0 |
| --- | --- | --- |
| High-scale alpha | yes | starting coupling only, not low-energy transport |
| QED loop kernel | yes | needed transport rule, but not thresholds or matching |
| R-Lep thresholds | yes | charged-lepton threshold input only |
| R-Q-Heavy thresholds | yes | heavy-quark threshold input only |
| R-Had-NP substrate | yes | hadronic vacuum-polarization input only |
| Scheme/decoupling matching | yes | convention and finite matching only |

Each partial closure remains a valid lane to pursue. This packet exists so
review can see them as one alpha0 assembly surface instead of many disconnected
notes.

### N7 - Steelman Positive Route

The strongest positive route is straightforward:

1. Ratify the QED loop kernel on the framework substrate.
2. Ratify R-Lep thresholds through the mass-spectrum and threshold-map inputs.
3. Ratify R-Q-Heavy thresholds without PDG mass proof input.
4. Ratify R-Had-NP from the Lane 1 substrate route, not literature `R(s)` data.
5. Ratify scheme/decoupling matching.
6. Accept the parent alpha0 contract with comparator-exclusion, owner, and
   audit gates.

If those steps are accepted, `ALPHA0_RETAINED` becomes available for the
static-source Rydberg lane. This packet does not claim that result now.

### N8 - Cross-Cycle Echo

The same boundary is echoed in the goal packet, alpha QED loop-kernel target,
alpha0 transport ratification packet, alpha0 transport current-surface no-go,
QED loop-kernel no-go, R-Lep thresholds packet, and static-source Rydberg
discriminator: alpha0 is a required hydrogen input, not a current retained
output.

## Explicit Non-Claims

- No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.
- No derivation or ratification of `ALPHA0_RETAINED`.
- No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.
- No derivation or ratification of the QED loop kernel.
- No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.
- No derivation or ratification of `R_Q_HEAVY_THRESHOLDS_RETAINED`.
- No derivation or ratification of `R_HAD_NP_RETAINED`.
- No derivation or ratification of `SCHEME_DECOUPLING_MATCHING_RETAINED`.
- No derivation or ratification of `T_EM` or `Delta_match`.
- No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or
  literature `R(s)` as proof input on the zero-import branch.
- No derivation of `m_e`, static-source Rydberg, or full hydrogen
  spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.
