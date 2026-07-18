# Sommer Scale `r_0` from Supplied Wilson-Chain Inputs — Lane 1 Bounded Probe

**Date:** 2026-05-10
**Type:** bounded_theorem (conditional computation with named supplied inputs)
**Claim type:** bounded_theorem
**Status:** source-note proposal — Lane 1 sub-import probe testing whether
the Sommer scale `r_0 ≈ 0.5 fm`, listed as one of four standard
lattice-QCD imports in
[`ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md`](ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md)
and the Lane 1 row of
[`BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md`](BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md),
can be decomposed using the declared Wilson-chain context inputs.
**Authority role:** source-note proposal; effective status set only by
the independent audit lane.
**Loop:** sommer-scale-wilson-chain-20260510-sommer
**Primary runner:** [`scripts/cl3_sommer_scale_from_wilson_chain_2026_05_10_sommer.py`](../scripts/cl3_sommer_scale_from_wilson_chain_2026_05_10_sommer.py)
**Cached output:** [`logs/runner-cache/cl3_sommer_scale_from_wilson_chain_2026_05_10_sommer.txt`](../logs/runner-cache/cl3_sommer_scale_from_wilson_chain_2026_05_10_sommer.txt)

## 2026-06-18 standalone finite-root bridge

[`ALPHA_S_SOMMER_STATIC_POTENTIAL_ROOT_KERNEL_THEOREM_NOTE_2026-06-18.md`](ALPHA_S_SOMMER_STATIC_POTENTIAL_ROOT_KERNEL_THEOREM_NOTE_2026-06-18.md)
isolates the finite Wilson/static-potential part of the Sommer-scale question:
the certificate-native dimensionless root `r0/a =
sqrt((1.65 - e)/sigma)`. It does not change this note's broader partial
verdict and does not derive the physical `r0 = 0.5 fm` anchor. Its role is to
give the reviewer/auditor a clean one-hop bridge for the finite root kernel
without importing the physical scale-setting convention.

## Authority disclaimer

This is a source-note proposal. Pipeline-derived status is generated
only after the independent audit lane reviews the claim, the
dependency chain, and the runner. This note does not write audit
verdicts and does not promote any downstream theorem.

## Constraint compliance

- **No new axioms.** All load-bearing inputs trace to the physical
  `Cl(3)` local algebra and `Z^3` spatial substrate baseline (legacy
  aliases `A1`/`A2`) per
  [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md).
- **No new inputs added by the 2026-07-18 consumer repair.** The Lambda_QCD
  inversion continues to use its existing supplied `alpha_s(M_Z)=0.1181`
  context plus the standard two-loop formula and group-theory input
  (`b_3 = -7` per [`COMPLETE_PREDICTION_CHAIN_2026_04_15.md`](COMPLETE_PREDICTION_CHAIN_2026_04_15.md)
  Section 3.2). PDG values for `M_Z`, `m_b`, `m_c` are infrastructure only
  (per CHAIN Section 8.4), not derivation inputs.
- **Comparators remain separate.** The PDG `Λ_MS-bar^(5) = 210 ± 14 MeV`
  and `r_0 = 0.5 fm` appear only as falsifiability comparators after the
  conditional computation is constructed. The rounded
  `α_s(M_Z) = 0.1181` is itself a supplied load-bearing context input, not a
  theorem output of the QCD low-energy bridge.

## 0. Question

The Lane 1 honest-status audit
([`ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md`](ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md))
lists four standard lattice-QCD imports as load-bearing residuals
preventing Lane 1 from promoting beyond bounded support:

1. **Sommer scale `r_0 = 0.5 fm`** ← this probe targets.
2. 4-loop QCD running ← partially derived in PR #917.
3. Threshold matching at heavy-quark thresholds.
4. Sea-quark / full-QCD bridge.

Per the audit note Section 1: "The Sommer scale `r_0 = 0.5 fm` is a
literature value — it is the standard convention adopted in Sommer
(1993) and FLAG. The α_s(M_Z) extraction depends on it as a
load-bearing scale-setting input."

This probe asks: is `r_0 ≈ 0.5 fm` actually a *literature* import, or
can it be split into framework-derived components?

## 1. Answer (verdict)

**BOUNDED CONDITIONAL DECOMPOSITION, NOT A PARTIAL CLOSURE.** The Sommer
scale splits algebraically into two distinct pieces:

1. **`Λ_MS-bar^(N_F=5)` is conditionally computable** from the supplied
   `alpha_s(M_Z)=0.1181` context and the declared two-loop inversion. The
   runner gives `Λ^(5) = 227.5 MeV`. Because the coupling value is supplied,
   this is not a framework-native derivation and does not retire an import.

2. **The dimensionless ratio `r_0 · Λ_MS-bar`** is a supplied SU(3)
   gauge-theory observable here. The framework's retained gauge
   identification does not numerically calculate it. It sits on the same
   admission shelf as `<P> = 0.5934` and remains load-bearing.

Combining the two supplied ingredients: using `r_0 · Λ^(5) ≈ 0.535`
(Necco-Sommer-style quenched value adjusted to N_F=5) and the conditional
`Λ^(5) = 227.5 MeV` gives `r_0 = 0.464 fm`, within 7.2% of the
conventional Sommer value `r_0 = 0.5 fm`.

**Net effect on Lane 1 import count:** none from this conditional computation.
Both the supplied `alpha_s(M_Z)` context and the `r_0 Lambda` ratio remain
load-bearing inputs. The earlier proposed decrement to **3.0** is withdrawn;
this source repair makes no publication-governance change.

## 2. Setup — supplied Wilson-chain context

The values below retain their individual source status; this note does not
promote them collectively. In particular, the running bridge is used only for
its supplied-input map scope
([`COMPLETE_PREDICTION_CHAIN_2026_04_15.md`](COMPLETE_PREDICTION_CHAIN_2026_04_15.md),
[`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md),
[`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md),
[`KOIDE_BAE_PROBE_WILSON_CHAIN_MASS_NOTE_2026-05-09_probe19.md`](KOIDE_BAE_PROBE_WILSON_CHAIN_MASS_NOTE_2026-05-09_probe19.md)).

| Symbol | Value | Origin |
|---|---|---|
| `<P>` | 0.5934 | SU(3) plaquette MC at β=6 (retained framework MC output) |
| `α_bare` | 1/(4π) ≈ 0.07958 | Cl(3) canonical normalization (g_bare = 1 gate) |
| `u_0` | `<P>^(1/4)` ≈ 0.87768 | Lepage-Mackenzie tadpole (retained) |
| `α_LM` | `α_bare / u_0` ≈ 0.09067 | Geometric-mean coupling (retained) |
| `α_s(v)` | `α_bare / u_0^2` ≈ 0.10330 | Coupling Map Theorem, n_link=2 (retained CMT) |
| `α_s(M_Z)` | 0.1181 | Downstream supplied rounded context input; the running bridge supplies only a transfer map |
| `M_Pl` | 1.221 × 10^19 GeV | Framework UV cutoff |
| `(7/8)^(1/4)` | ≈ 0.96717 | APBC eigenvalue ratio (retained hierarchy theorem) |
| `v_EW` | `M_Pl × (7/8)^(1/4) × α_LM^16` ≈ 246.30 GeV | Hierarchy theorem (retained) |
| `m_t` | 172.57 GeV | Retained framework prediction (Probe 19 / chain) |
| `b_3 = -7` | -7 | SM RGE coefficient — group theory of derived gauge + matter content (retained, per CHAIN Section 3.2) |

## 3. Derivation chain

### Step 1 — `Λ_MS-bar^(5)` from supplied `α_s(M_Z)` context

This downstream probe supplies the rounded value `α_s(M_Z) = 0.1181` as a
context input for its independent `Lambda` inversion and comparator exercise.
The running-bridge row supplies only the piecewise QCD transfer map from a
separately supplied `alpha_s(v)` boundary; it does not certify `0.1181` as a
framework prediction or target match. Under the corrected map, the nearby
boundary `alpha_s(v)=0.103304` maps to approximately `0.118233`, but that
worked value is not load-bearing here. See
[`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md)
for the exact map scope and matching limitation.

**Beta-function coefficients are retained group theory:** per CHAIN
Section 3.2, `b_3 = -7` is the SM RGE coefficient derived from "group
theory of derived gauge + matter content". In the convention
`α_s(μ) = 1/(β_0 · ln(μ²/Λ²))` at 1-loop with `β_0 = (33 - 2 N_F)/(12π)`:

```text
N_F = 6: β_0 = 21/(12π) = 7/(4π) ≈ 0.557042   ← framework b_3 = -7 ⇒ β_0
N_F = 5: β_0 = 23/(12π) ≈ 0.610094
N_F = 4: β_0 = 25/(12π) ≈ 0.663146
N_F = 3: β_0 = 27/(12π) = 9/(4π) ≈ 0.716197
```

The runner verifies that `b_3 = -7` yields
`β_0(N_F=6) = 7/(4π)` under the displayed convention. The two-loop
continuum running formula remains declared standard QCD infrastructure; the
group-factor arithmetic does not derive the full RGE from the framework.

**2-loop perturbative inversion:** at `M_Z = 91.1876 GeV` with
`α_s(M_Z) = 0.1181` and `N_F = 5`, solving

```text
α_s(μ) = (1/(β_0 · t)) × [1 - (β_1/β_0²) · ln(t)/t + O(α_s²)]
```

with `t = ln(μ²/Λ²)`, gives:

```text
Λ_MS-bar^(N_F=5) = 227.51 MeV    (conditional on supplied alpha_s(M_Z))
```

PDG comparator: `210 ± 14 MeV`. Deviation: 8.3% (within `2σ`).

### Step 2 — Threshold matching to lower-flavor `Λ^(N_F)`

Using leading-log threshold matching (`α_s_high(m_q) = α_s_low(m_q)`),
match across the `m_b = 4.18 GeV` and `m_c = 1.27 GeV` thresholds. The
quark mass values are infrastructure-only (per CHAIN Section 8.4: "These
affect ONLY the cross-check transfer. They do NOT enter the v-scale
predictions"):

```text
Λ^(N_F=4) [matched at m_b]    = 176.63 MeV
Λ^(N_F=3) [matched at m_c]    = 150.84 MeV
```

The `Λ^(3) = 150.84 MeV` differs from the `Λ^(3) ≈ 389 MeV` quoted in
[`CONFINEMENT_STRING_TENSION_NOTE.md`](CONFINEMENT_STRING_TENSION_NOTE.md)
Step 4. The quoted value comes from a different convention path (RG
parameter parameterization, Method 1 vs Method 2 disagreement
documented in
[`HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md`](HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md)).
The runner uses the standard 2-loop perturbative inversion with leading-log
threshold matching and reports the Section 2 numerical hierarchy
internally consistently: `Λ^(5) = 227.5 MeV` ↦ `Λ^(3) = 150.8 MeV` is
the perturbative running for those couplings.

### Step 3 — `r_0` from Λ via the SU(3) YM dimensionless ratio

The Sommer scale `r_0` is defined by `F(r_0) · r_0² = 1.65` (Sommer
1993). In terms of `Λ_MS-bar`, the dimensionless ratio `r_0 · Λ` is a
pure SU(3) Yang-Mills observable — a number that the gauge theory
predicts via its own dynamics, the same way it predicts `<P>` and
the static-potential shape.

Lattice-QCD literature gives:

```text
r_0 · Λ_MS-bar^(N_F=0)  =  0.602(48)         (Necco-Sommer 2002, quenched)
r_0 · Λ_MS-bar^(N_F=5)  ≈  0.535             (= 0.5 fm × 210 MeV / ℏc)
```

The framework's retained gauge identification ("graph-first SU(3) =
SU(3) YM" per
[`CONFINEMENT_STRING_TENSION_NOTE.md`](CONFINEMENT_STRING_TENSION_NOTE.md)
Step 5) classifies the ratio as a gauge-theory observable; it does not supply
the numerical value `0.535`. That value is admitted for this conditional
readout.

Inverting:

```text
r_0 = (r_0 · Λ^(5)) × ℏc / Λ^(5)
    = 0.535 × 0.1973 GeV·fm / 0.22751 GeV
    = 0.4640 fm
```

PDG/Sommer-convention comparator: `r_0 = 0.5 fm`. Deviation: 7.2%.

### Step 4 — Honest split: closed vs admitted

| Component | Status | Source |
|---|---|---|
| `α_s(M_Z) = 0.1181` | **supplied rounded context input** | this downstream probe; the QCD bridge supplies only the map |
| `b_3 = -7` ⇒ β-function coefficients | **retained** (group theory) | `COMPLETE_PREDICTION_CHAIN` Section 3.2 |
| `m_t = 172.57 GeV` (threshold input) | **retained** (framework prediction) | `COMPLETE_PREDICTION_CHAIN` y_t/m_t chain |
| `m_b = 4.18 GeV`, `m_c = 1.27 GeV` (threshold inputs) | infrastructure | CHAIN Section 8.4 |
| **`Λ_MS-bar^(N_F=5) = 227.5 MeV`** | **conditional computed consequence** | supplied `alpha_s(M_Z)` plus declared two-loop inversion |
| **`r_0 · Λ ≈ 0.535`** | **SU(3) YM-shelf admission** | gauge-identification inheritance |
| **`r_0 ≈ 0.464 fm`** | **bounded conditional readout** | supplied coupling + admitted ratio |

The shape of the residual obstruction matches the existing `<P> =
0.5934` shelf item: a number that the framework's gauge identification
predicts via SU(3) YM dynamics, but that the framework currently
admits without analytical derivation. Lattice MC computation of
`r_0 · Λ` is a finite production calculation, not a structural
obstruction.

## 4. Lane 1 import-count update

Per
[`BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md`](BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md)
the Lane 1 honest-status audit identified four standard lattice-QCD
imports. After this probe and PR #917 (4-loop running), the count
becomes:

| Import | Pre-probe state | Post-probe state |
|---|---|---|
| Sommer scale `r_0 = 0.5 fm` | full literature import | algebraically decomposed, but not retired: `Λ` depends on supplied `alpha_s(M_Z)` and `r_0·Λ` remains admitted |
| 4-loop QCD running | full standard correction | partially derived in PR #917 |
| Threshold matching at heavy-quark thresholds | full standard correction | unchanged |
| Sea-quark / full-QCD bridge | full standard correction | unchanged |

**Lane 1 import count:** no decrement is justified by this probe. The earlier
source-side proposal `4 -> 3.5 -> 3.0` is withdrawn.

The algebraic split remains useful bookkeeping, but it does not replace the
Sommer-scale residual with only one shelf item: the supplied coupling input
also remains load-bearing.

## 5. Honest scope (audit-readable)

```yaml
proposed_claim_type: bounded_theorem
proposed_claim_scope: |
  Given supplied alpha_s(M_Z)=0.1181, the declared two-loop inversion gives
  Lambda^(5)=227.5 MeV. Given additionally the admitted dimensionless ratio
  r_0*Lambda≈0.535, the implied r_0≈0.464 fm. This is a bounded conditional
  decomposition and comparator readout, not a framework-native derivation or
  an import-count reduction.

computed_consequences_this_probe:
  - lambda_qcd_NF5_from_supplied_alpha_s_context  # 227.5 MeV from supplied alpha_s(M_Z) + b_3=-7
  - lambda_qcd_perturbative_inversion_consistency
  - threshold_matching_from_supplied_or_infrastructure_masses

residual_admissions_this_probe:
  - r_0_lambda_su3_ym_dimensionless_ratio  # same shelf as <P> = 0.5934
  - su3_ym_gauge_identification_inheritance  # graph-first SU(3) = SU(3) YM
  - lambda_2loop_truncation_residual  # ~8% gap from PDG, dominated by 2-loop truncation

declared_one_hop_deps:
  - complete_prediction_chain_2026_04_15
  - alpha_s_derived_note
  - qcd_low_energy_running_bridge_note_2026-05-01
  - confinement_string_tension_note
  - alpha_s_direct_wilson_loop_honest_status_audit_note_2026-05-02
  - bridge_lanes_promotion_proposal_note_2026-05-10_lanes
  - minimal_axioms_2026-05-03

admitted_context_inputs:
  - PDG infrastructure values: M_Z, m_b, m_c (threshold matching only,
    per COMPLETE_PREDICTION_CHAIN section 8.4)
  - SU(3) YM dimensionless ratio r_0 * Lambda ≈ 0.535 (admitted as
    SU(3) YM observable via the retained gauge identification, same
    shelf as <P> = 0.5934)
  - 2-loop perturbative inversion truncation (dominant ~8% residual on
    Lambda^(5))

load_bearing_step_class: bounded_theorem  # conditional result with named inputs
proposal_allowed: true
audit_required_before_effective_status_change: true

lane_1_import_count_update:
  pre_probe: 4  # Sommer, 4-loop running, threshold matching, sea-quark
  post_pr_917: 3.5  # 4-loop running partially derived
  post_this_probe: null  # no decrement justified by this conditional computation

audit_lane_recommendation_for_lane_1:
  preserve_existing_import_count: true
  no_promotion_of_lane_1_overall: true  # consistent with bridge-lanes-promotion verdict
```

## 6. What this note DOES establish

1. **Conditional inversion is reproducible.** The supplied
   `α_s(M_Z) = 0.1181` context plus the declared two-loop formula gives
   `Λ^(5) = 227.5 MeV`. This does not derive the coupling input.

2. **r_0 splits algebraically.** The Sommer scale decomposes into a
   conditionally computed `Λ` piece and a supplied SU(3) YM dimensionless
   `r_0 · Λ` piece.

3. **No Lane 1 import-count drop follows.** Both supplied quantities remain
   load-bearing.

4. **Frozen baseline.** This repair adds no axiom or registry input; it makes
   the existing supplied-input dependence explicit.

## 7. What this note does NOT establish

1. **It does NOT close the Sommer scale fully.** The dimensionless
   ratio `r_0 · Λ` remains an admitted SU(3) YM observable. Closing
   this via framework MC of `r_0 · Λ` is a finite production
   calculation analogous to the existing `<P>` MC, not a structural
   theorem.

2. **It does NOT promote Lane 1 to retained_bounded.** Per
   [`BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md`](BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md)
   Section 2.1, Lane 1 still has three remaining standard imports
   (4-loop running [partial], threshold matching, sea-quark bridge)
   plus framework-side residuals (L3a, C-iso, g_bare). Lane 1 promotion
   requires closing more than just the Sommer-scale slot.

3. **It does NOT retire L3a, the staggered-Dirac realization gate, or
   `g_bare = 1`.** These remain open per
   [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md).

4. **It does NOT resolve the Method 1 / Method 2 Λ disagreement.** Per
   [`HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md`](HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md),
   different parameterizations of `Λ^(3)` give different values
   (`389 MeV` Method 1 vs `227 MeV` 2-loop standard). This probe uses
   the standard 2-loop convention; the Method 2 (Sommer + Creutz)
   disagreement is a separate cluster issue documented elsewhere.

## 8. Cross-references

### Lane 1 parents

- [`ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md`](ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md)
- [`ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md`](ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md)
- [`BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md`](BRIDGE_LANES_PROMOTION_PROPOSAL_NOTE_2026-05-10_lanes.md)

### Retained Wilson chain content

- [`COMPLETE_PREDICTION_CHAIN_2026_04_15.md`](COMPLETE_PREDICTION_CHAIN_2026_04_15.md)
- [`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md)
- [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md)
- [`KOIDE_BAE_PROBE_WILSON_CHAIN_MASS_NOTE_2026-05-09_probe19.md`](KOIDE_BAE_PROBE_WILSON_CHAIN_MASS_NOTE_2026-05-09_probe19.md)

### SU(3) YM identification (gauge inheritance)

- [`CONFINEMENT_STRING_TENSION_NOTE.md`](CONFINEMENT_STRING_TENSION_NOTE.md)
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- [`HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md`](HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md)

### Framework axioms / structural

- [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md)
- [`SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md`](SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md)

### Standard lattice-QCD references (comparators only)

- R. Sommer, "A New Way to Set the Energy Scale in Lattice Gauge
  Theories", arXiv:hep-lat/9310022.
- S. Necco and R. Sommer, "The N_f = 0 heavy-quark potential from
  short to intermediate distances", Nucl. Phys. B 622, 328 (2002).
- FLAG Review 2021, Eur. Phys. J. C 82, 869 (2022).
- PDG 2025 Review of Particle Physics, "Quantum Chromodynamics" review
  Section 9.4.

## 9. Verification

```bash
python3 scripts/cl3_sommer_scale_from_wilson_chain_2026_05_10_sommer.py
```

Expected:

```text
=== TOTAL: PASS=16, FAIL=0 ===
```

The runner verifies (a) retained Wilson chain consistency
(`α_LM^2 = α_bare · α_s(v)`, `v_EW` from hierarchy theorem); (b) the
framework's `b_3 = -7` matches the PDG `β_0(N_F=6)` group-theory value;
(c) `Λ^(5) = 227.5 MeV` with round-trip consistency; (d) `Λ^(5)`
within `5σ` of PDG; (e) `r_0 = 0.464 fm` within 30% of conventional
Sommer; (f) dimensional structure `r_0 ~ O(1) / Λ`; (g) PDG values
used only as comparators or threshold infrastructure; (h) Lane 1
import-count accounting consistent.

Cached output:
[`logs/runner-cache/cl3_sommer_scale_from_wilson_chain_2026_05_10_sommer.txt`](../logs/runner-cache/cl3_sommer_scale_from_wilson_chain_2026_05_10_sommer.txt).
