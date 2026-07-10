# Charged-Lepton Koide Value — Full Chain of Custody to the Open `r` Selector

**Date:** 2026-06-02
**Claim type:** open_gate
**Claim boundary:** chain-of-custody map from the framework baseline through the
exact relation `Q=1/3+(2/3)r` and the biconditional `Q=2/3 <=> r=1/2`.
The former `AC_phi_lambda` Tier-A slot has been retired, and its owner-governed
replacement explicitly supplies no value of `r`. The physical selection
`r=1/2` therefore remains open. Independent audit owns the row classification
and status.
**Runner:** `scripts/flavor_charged_lepton_value_full_chain_2026_06_02.py`
(nine local algebra/registry consistency checks; not a dependency audit).
**Purpose:** give downstream work one end-to-end map of the exact algebra and
the unresolved selector, so no consumer treats `Q=2/3` as physically selected.
**Premise-surface correction:** 2026-07-09 — the live Tier-A count is zero.
The owner-governed `AC_phi_lambda` boundary supplies occupancy/readout licenses
but explicitly no `r`, `delta`, or charged-lepton mass value. The old
"value modulo one Tier-A input" wording is withdrawn.
**Dependency-surface update:** 2026-07-05 — edge hygiene: open-gate and superseded-generation citations demoted to context handles / re-pointed to retained successors; no custody claim changed.
**Historical dependency-surface update (3):** 2026-07-05 — the then-current
Tier-A row was added as a direct dependency. This statement is superseded by
the 2026-07-09 correction above: the live Tier-A count is now zero and the
owner-governed replacement supplies no `r` value.
**Dependency-surface update (2):** 2026-07-05 — per the audited_conditional blocker: L4 re-pointed to the retained narrow successor [FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md), and the L4 cell restated at that successor's audited scope (carrier-type theorem only; the 2026-05-31 parent — which additionally bundles an open physical-locus bridge not consumed by this chain — demoted to a historical context handle). The 2026-04-25 Plancherel support citation demoted to a context handle (consistency-only edge). The L1 per-site su(2) and L7 finite spectral-asymmetry citations are unchanged (dep-ready audit targets). No other custody claim changed.

## The chain (framework baseline -> Q=2/3), every link tiered

| # | link | current dependency standing (informational; audit lane authoritative) | anchor |
|---|---|---|---|
| L1 | one-qubit operator algebra at each lattice site carries the unique j=1/2 `su(2)` module | **dep-ready audit target** | [PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md) |
| L2 | `Z^3` spatial substrate locality gives the equal-time Lieb-Robinson tensor-locality bound | **retained_bounded** | [LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md) |
| L3 | 3 generations = the hw=1 BZ-corner C₃ triplet (irreducible M₃(ℂ), count 3) | **retained** | [THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md), [THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md](THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md), [THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md), [THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) |
| L4 | carrier **momentum-type**: flavor-separating readout is supplied by the momentum/BZ factor, not local position observables (distinct joint translation characters on the corner triplet; spectral theorem on the commuting translations, tested representative class) | **retained_bounded**; `FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31` (superseded-generation historical context handle; the retained 2026-06-15 carrier-type split covers the consumed momentum-type theorem — its open physical-locus bridge is not consumed here, the hw=1 locus is carried by L3's retained rows — not a citation-graph dependency) | [FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md) |
| L5 | C₃-equivariant circulant mass operator `H=aI+bC+b̄C²` (3 dof: a,\|b\|,δ) | **retained_bounded** | [GENERATION_AXIOM_BOUNDARY_NOTE.md](GENERATION_AXIOM_BOUNDARY_NOTE.md) |
| L6 | exact `Q = 1/3 + (2/3)r`, `r=\|b\|²/a²` (κ/Frobenius isotype split) | **retained** | [KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md), [KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md) |
| L7 | C₃ channels (scale/ratio/phase) + topological asymmetry `δ=2/9 = L₃(1,2)` Atiyah-Bott density | **dep-ready audit target** | [AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md), [KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md](KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md) |
| L8 | endpoint exclusion: `r=0 -> [1,1,1]` degenerate, `r=1 -> [0,0,3]` two massless; charged leptons forced interior | **bounded candidate (this PR)** | [FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md) |
| L9 | `r=1/2` = HS **2-sector equipartition** (`‖aI‖²=‖bC+b̄C²‖²`) = max-2-sector-entropy **stationary point** | **bounded candidate (this PR)**; kappa/isotype algebra re-pointed to [KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md); `KOIDE_KAPPA_TWO_ORBIT_DIMENSION_FACTORIZATION_NOTE_2026-04-19` (superseded-generation historical context handle; retained 2026-05-10 kappa/isotype algebra row covers the consumed algebra, not a citation-graph dependency) | [FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md), [FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md) |
| L10 | `Q=2/3 <=> r=1/2` (Koide-cone biconditional) | **retained** | [CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) |
| **OPEN SELECTOR** | **choose the physical interior value `r`; `Q=2/3` requires `r=1/2`** | no live Tier-A target; the owner-governed `AC_phi_lambda` boundary explicitly supplies no value of `r` | [TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md](TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md), [ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md) |

The runner reproduces representative local algebra for the chain and checks the
live selector registries. It does not prove the cited source claims, audit their
dependencies, or turn the assembled chain into a physical value derivation.

## The structure/value split
- **Structural formulas — ASSEMBLED subject to the named dependency closures**
  (L1–L9, on retained/retained_bounded anchors, dep-ready audit targets, and
  bounded bridge candidates):
  the carrier and 3-generation count, the momentum-type, the C₃-equivariant circulant form, the **exact**
  `Q=1/3+(2/3)r`, the channel decomposition and the topological `2/9`, the endpoint exclusion (leptons
  forced interior), and `r=1/2` as the **2-sector-equipartition / balance stationary point**.
- **Value — OPEN** (the selection of `r=1/2` over the other interior values):
  the retired Tier-A slot and its owner-governed replacement do not supply a
  value of `r`. The following historical candidate pieces remain explicit
  selector hypotheses rather than accepted premises:
  1. **K-reality** (time-reversal-reality of the generation coupling / δ=0 / transpose `b=c̄`) — selects
     the **2-block partition** over the 3-mode one (else r=0). *Posited*: emergent-time is conjugation-even.
  2. **det_C / equal-power-per-block** (block-counting measure) — selects `r=1/2` over `r=1` within the
     2-block structure. *The Born/dimension measure gives r=1*; r=1/2 is the equal-power-per-block reading.
  Prior obstruction portfolio for this unresolved selector:
  [KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md) (retained_no_go — singlet:doublet ratio free),
  [KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md](KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md) (retained_no_go — no canonical zero-section),
  [KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) (retained_bounded). These match the literature: Koide's own
  Z₃ parametrization (arXiv:1301.4143) likewise leaves the per-sector ratio a free fit.

## Honest standing (a claim description, not an audit grade)
The chain is an algebraic/checkable custody map to an open physical selector.
It does not claim `Q=2/3` is selected by the four axioms, the retired Tier-A
slot, or the owner-governed replacement. The exact structural formulas remain
useful; the charged-lepton value does not close until a separate `r=1/2`
selector is derived or explicitly approved.

## For downstream consumers of Q=2/3
Cite **this chain note** as the map to the open selector, plus the endpoint
biconditional
[CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md).
Charged-lepton mass ratios, Brannen relations, and every `Q=2/3`-dependent
result inherit the unresolved `r=1/2` selection and must not cite this row as a
retained value source.

**Named downstream consumers (the dependency graph this chain anchors):**
- `KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20` (superseded-generation downstream context handle; retained structural rows in this chain carry the consumed `H` and `Q=1/3+(2/3)r` content, not a citation-graph dependency) — the Brannen circulant √m parametrization (the δ-phase reduction) reads off this chain's `H` and `Q=1/3+(2/3)r`.
- [CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) (retained) — the L10 endpoint biconditional `Q=2/3 <=> r=1/2`; this chain is its framework-baseline provenance.
- `LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26` (open-gate row located for orientation; context handle, not a citation-graph dependency) — the δ=2/9 open gate; this chain supplies its structural L7 (topological `2/9`) while leaving the physical `r` selector open.
- `lanes/open_science/06_CHARGED_LEPTON_MASS_RETENTION_OPEN_LANE` — the charged-lepton mass-retention lane; this chain is its upstream value-anchor (the masses `m_k = λ_k²` follow once the scale `S` and the lane `r=1/2` are fixed).
- `KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25` (support-layer row located for orientation; consistency-only — the consumed L6/L9 content is carried by this chain's retained anchors — context handle, not a citation-graph dependency), [BRANNEN_AMPLITUDE_EQUIPARTITION_BAE_RENAME_META_NOTE_2026-05-09.md](BRANNEN_AMPLITUDE_EQUIPARTITION_BAE_RENAME_META_NOTE_2026-05-09.md) — the BAE/Plancherel support layer, consistent with this chain's L6/L9.

Each of these inherits the **open `r=1/2` selector** from this chain; none
should claim `Q=2/3` is physically selected.

## The three Koide lanes (for completeness / sibling-sector retention)
The same exact line `Q=1/3+(2/3)r` carries three distinguished points (this session's lane map): **Q=1/3**
(r=0, S₃-degenerate / unbroken — neutrino-like), **Q=2/3** (r=1/2, balanced — charged leptons, this
chain), **Q=1** (r=1, maximal hierarchy — det_R/Born default). They are distinct physics on one structure,
algebraic points on one structure; this note documents the open `Q=2/3`
selection lane without assigning any point to a physical sector.

## Provenance (verified 2026-06-02)
- Nine representative local algebra/registry checks pass. They are consistency
  evidence only and do not substitute for source-claim or dependency audits.
- The live Tier-A registry contains zero targets; the owner-governed
  `AC_phi_lambda` boundary supplies no value of `r`.
- This note assembles retained/retained_bounded rows, explicitly named dep-ready audit targets, and this session's bounded bridge candidates into one citable chain. It does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
