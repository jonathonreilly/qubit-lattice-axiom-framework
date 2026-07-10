# Charged-Lepton Koide Value — Full Chain of Custody to the Open `r` Selector

**Date:** 2026-06-02
**Claim type:** open_gate
**Claim boundary:** chain-of-custody map from the framework baseline through the
abstract positive-spectrum Hermitian-circulant relation
`Q_H=1/3+(2/3)r` and the biconditional `Q_H=2/3 <=> r=1/2`.
The former `AC_phi_lambda` Tier-A slot has been retired, and its owner-governed
replacement explicitly supplies no value of `r`. The physical selection
`r=1/2` therefore remains open. Identifying `Q_H` with the physical
charged-lepton Koide ratio is not supplied by this row. Independent audit owns
the row classification and status.
**Runner:** `scripts/flavor_charged_lepton_value_full_chain_2026_06_02.py`
(nine local algebra/registry consistency checks; not a dependency audit).
**Purpose:** give downstream work one end-to-end map of the exact algebra and
the unresolved selector, so no consumer treats `Q=2/3` as physically selected.
**Premise-surface correction:** 2026-07-09 — the live Tier-A count is zero.
The owner-governed `AC_phi_lambda` boundary supplies occupancy/readout licenses
but explicitly no `r`, `delta`, or charged-lepton mass value. The old
"value modulo one Tier-A input" wording is withdrawn.
**Dependency-surface update:** 2026-07-05 — edge hygiene: open-gate and superseded-generation citations were demoted to context handles or re-pointed to current narrow authorities; no custody claim changed.
**Historical dependency-surface update (3):** 2026-07-05 — the then-current
Tier-A row was added as a direct dependency. This statement is superseded by
the 2026-07-09 correction above: the live Tier-A count is now zero and the
owner-governed replacement supplies no `r` value.
**Dependency-surface update (2):** 2026-07-05 — L4 was re-pointed to the narrow carrier-type authority [FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md), and the L4 cell was restated at that carrier-only scope. The 2026-05-31 parent, which additionally bundles an open physical-locus bridge not consumed by this chain, is now only a historical context handle. The 2026-04-25 Plancherel support note is likewise a consistency-only context handle. The L1 per-site `su(2)` and L7 finite spectral-asymmetry citations are unchanged. No other custody claim changed.

## The chain (framework baseline -> open `Q=2/3` selector), every link scoped

| # | link | role in this chain | anchor |
|---|---|---|---|
| L1 | the one-qubit local operator algebra carries the Pauli `j=1/2` `su(2)` module; no physical matter-spin identification is consumed | one-site algebraic authority | [PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md) |
| L2 | operators on distinct raw tensor factors commute at equal time; no dynamical Lieb-Robinson lightcone is claimed | raw tensor-locality authority | [LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md) |
| L3 | the supplied `hw=1` three-corner carrier has an irreducible `M₃(ℂ)` observable algebra and count three; physical-species semantics are not supplied | finite algebraic carrier authorities | [THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md), [THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md](THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md), [THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md), [THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) |
| L4 | on the supplied finite `hw=1` character carrier, momentum projectors separate the three labels while position-diagonal weights do not; no physical generation locus or readout is selected | supplied-carrier character authority; `FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31` is historical parent context, not a citation-graph dependency | [FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md) |
| L5 | abstract Hermitian-circulant coordinates `H=aI+bC+b̄C²`, with `a in R` and `b in C` | abstract circulant algebra authority; no mass identification | [KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) |
| L6 | for the spectral ratio `Q_H := Tr(H²)/(Tr H)²`, exact `Q_H = 1/3 + (2/3)r`, `r=\|b\|²/a²`; interpreting the eigenvalues as positive square-root masses is a separate physical bridge | abstract algebra plus conditional coordinate bridge | [KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md), [KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md) |
| L7 | the finite `C₃` cyclotomic local-density expression satisfies `L₃(1,2)=2/9`; neither authority identifies that number with the circulant phase `delta` or a charged-lepton observable | local-density arithmetic authorities | [AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md), [KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md](KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md) |
| L8 | on the positive-spectrum surface, distinct positive components imply `0<r<1`; at `r=0` the spectrum is degenerate, while at `r=1` positivity forces `cos(3 delta)=1` and hence the boundary spectrum `[0,0,3a]` up to cyclic ordering | algebraic boundary checked here; no physical assignment | [FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md) |
| L9 | `r=1/2` characterizes HS **2-sector equipartition** (`‖aI‖²=‖bC+b̄C²‖²`) and the maximum of the supplied two-sector entropy; it does not select that coarse-graining physically | two-sector characterization authorities; `KOIDE_KAPPA_TWO_ORBIT_DIMENSION_FACTORIZATION_NOTE_2026-04-19` is historical parent context, not a citation-graph dependency | [FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md), [FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md) |
| L10 | on the abstract positive three-vector Koide cone, `Q=2/3 <=> r=1/2`; no charged-lepton mass-square-root assignment is supplied | positive-cone algebraic equivalence | [CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) |
| **OPEN SELECTOR** | **choose the physical interior value `r`; `Q=2/3` requires `r=1/2`** | no live Tier-A target; the owner-governed `AC_phi_lambda` boundary explicitly supplies no value of `r` | [TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md](TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md), [ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md) |

The runner reproduces representative local algebra for the chain and checks the
live selector registries. It does not prove the cited source claims, audit their
dependencies, or turn the assembled chain into a physical value derivation.

## The structure/value split
- **Structural formulas — ASSEMBLED subject to the named dependency closures**
  (L1–L9, on the cited authorities and explicitly identified bridge
  candidates):
  the finite three-label carrier, its momentum-character separation, the
  abstract C₃-equivariant circulant form, the **exact** spectral-ratio line
  `Q_H=1/3+(2/3)r`, the separate local-density arithmetic `L₃(1,2)=2/9`,
  the positive-spectrum endpoint boundary, and `r=1/2` as the supplied
  **2-sector-equipartition / balance stationary point**. These ingredients do
  not by themselves identify charged-lepton species, masses, or phase.
- **Value — OPEN** (the selection of `r=1/2` over the other interior values):
  the retired Tier-A slot and its owner-governed replacement do not supply a
  value of `r`. The following historical candidate pieces remain explicit
  selector hypotheses rather than accepted premises:
  1. **K-reality** (time-reversal-reality of the generation coupling / δ=0 / transpose `b=c̄`) — selects
     the **2-block partition** over the 3-mode one (else r=0). *Posited*: emergent-time is conjugation-even.
  2. **det_C / equal-power-per-block** (block-counting measure) — selects `r=1/2` over `r=1` within the
     2-block structure. *The Born/dimension measure gives r=1*; r=1/2 is the equal-power-per-block reading.
  Prior obstruction portfolio for this unresolved selector:
  [KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md) (singlet:doublet ratio free),
  [KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md](KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md) (no canonical zero-section), and
  [KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) (the stated equivariant anticommutation boundary). These match the literature: Koide's own
  Z₃ parametrization (arXiv:1301.4143) likewise leaves the per-sector ratio a free fit.

## Honest standing (a claim description, not an audit grade)
The chain is an algebraic/checkable custody map to an open physical selector.
It does not claim `Q=2/3` is selected by the [four framework axioms](MINIMAL_AXIOMS_2026-06-29.md), the retired Tier-A
slot, or the owner-governed replacement. The exact structural formulas remain
useful; the charged-lepton value does not close until a separate `r=1/2`
selector is derived or explicitly approved.

## For downstream consumers of Q=2/3
Cite **this chain note** as the map to the open selector, plus the endpoint
biconditional
[CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md).
Charged-lepton mass ratios, Brannen relations, and every `Q=2/3`-dependent
result inherit the unresolved `r=1/2` selection and must not cite this row as a
physical value source.

**Named downstream consumers (the dependency graph this chain anchors):**
- `KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20` (superseded-generation downstream context handle; the current structural anchors in this chain carry the consumed `H` and `Q=1/3+(2/3)r` content, not a citation-graph dependency) — the Brannen circulant √m parametrization (the δ-phase reduction) reads off this chain's `H` and `Q=1/3+(2/3)r`.
- [CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) — the L10 endpoint biconditional `Q=2/3 <=> r=1/2`; this chain is its framework-baseline provenance.
- `LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26` (open-gate row located for orientation; context handle, not a citation-graph dependency) — the δ=2/9 open gate; this chain supplies its structural L7 (topological `2/9`) while leaving the physical `r` selector open.
- `lanes/open_science/06_CHARGED_LEPTON_MASS_RETENTION_OPEN_LANE` — the charged-lepton mass-retention lane; this chain is its upstream value-anchor (the masses `m_k = λ_k²` follow once the scale `S` and the lane `r=1/2` are fixed).
- `KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25` and `BRANNEN_AMPLITUDE_EQUIPARTITION_BAE_RENAME_META_NOTE_2026-05-09.md` (support-layer rows located for orientation; consistency-only context handles, not citation-graph dependencies) — the BAE/Plancherel support layer is consistent with this chain's L6/L9.

Each of these inherits the **open `r=1/2` selector** from this chain; none
should claim `Q=2/3` is physically selected.

## The three Koide lanes (for completeness / sibling-sector retention)
The same exact abstract line `Q_H=1/3+(2/3)r` carries three distinguished
algebraic points: `Q_H=1/3` (`r=0`, degenerate), `Q_H=2/3` (`r=1/2`,
two-sector balanced), and `Q_H=1` (`r=1`, the positivity boundary). Historical
lane labels such as neutrino-like, charged-lepton-like, or hierarchy-like are
candidate interpretations only. This note documents the open `Q=2/3`
selection lane without assigning any point to a physical sector.

## Provenance (verified 2026-06-02)
- Nine representative local algebra/registry checks pass. They are consistency
  evidence only and do not substitute for source-claim or dependency audits.
- The live Tier-A registry contains zero targets; the owner-governed
  `AC_phi_lambda` boundary supplies no value of `r`.
- This note assembles the cited source authorities and explicitly named bridge candidates into one citable chain. It does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
