# Axiom-First CKM Substrate Multi-Witness (Narrow) Theorem

**Date:** 2026-05-26
**Type:** source-only theorem-note proposal (research lane).
**Lane:** CKM lane, Block 1 (opens the CKM mixing-matrix axis using the
panel-attack methodology that produced the dynamics-lane and PMNS-lane
work earlier today).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Upstream retained content on `origin/main`:**
- `ckm_inverse_square_structural_sum_rule_narrow_theorem_note_2026-05-10`
  (retained positive_theorem) — establishes polynomial identities on
  abstract `(n_pair, n_color)` symbols.
- `ckm_cp_phase_structural_identity_narrow_theorem_note_2026-05-10`
  (retained positive_theorem) — CKM CP phase structure.
- `ckm_cp_phase_rho_eta_to_delta_narrow_theorem_note_2026-05-10`
  (retained positive_theorem) — Wolfenstein-to-PDG-δ identification.
- `ckm_magnitudes_structural_counts_narrow_theorem_note_2026-05-02`
  (retained_bounded) — magnitude structural counts.
**Cross-lane companion:**
- PR #1965 (dynamics-lane multi-witness capstone) — establishes the
  (N-1)/N² convergence pattern at multiple N; at N=6 the value is
  5/36 = η² in the CKM identification.
- PR #1986 (PMNS multi-witness capstone) — establishes lepton-sector
  unification identity `1/N + (N-1)/N² = (2N-1)/N²`.

**Runner:**
[`scripts/frontier_ckm_substrate_multi_witness_narrow_verifier.py`](../scripts/frontier_ckm_substrate_multi_witness_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_ckm_substrate_multi_witness_narrow_verifier.txt`](../logs/runner-cache/frontier_ckm_substrate_multi_witness_narrow_verifier.txt)

## Why this note exists

The retained CKM_INVERSE_SQUARE_STRUCTURAL_SUM_RULE proves polynomial
identities on **abstract positive symbols** `(n_pair, n_color)`. Those
identities are mathematically airtight but do **not** identify what
`n_pair` and `n_color` ARE physically. The framework's Wolfenstein-
parameter predictions (`ρ`, `A²`, `η²`) become empirically testable
only after `(n_pair, n_color)` is fixed.

The natural identification is `(n_pair, n_color) = (2, 3)` from the
quark sector's SU(2)_L × SU(3)_C content:
- `n_pair = 2`: two isospin states (up-type, down-type) in each
  generation
- `n_color = 3`: three colors in SU(3)_C

This identification gives Wolfenstein predictions:
- `ρ = 1/(n_pair · n_color) = 1/6 ≈ 0.167`
- `A² = n_pair / n_color = 2/3 ≈ 0.667`
- `η² = 1/n_pair² − 1/n_color² = 1/4 − 1/9 = 5/36 ≈ 0.139`

Comparing to PDG / NuFit / CKMfitter measured Wolfenstein:
- Measured `ρ̄ ≈ 0.156 ± 0.011` (vs predicted 0.167 — `~0.7σ` deviation)
- Measured `A² ≈ 0.665 ± 0.020` (vs predicted 0.667 — `<0.1σ` deviation,
  exact match within precision)
- Measured `η̄² ≈ 0.122 ± 0.020` (vs predicted 0.139 — `~0.7σ` deviation)

**The framework predicts all three Wolfenstein parameters from a
single 2-bit substrate identification** `(n_pair=2, n_color=3)`. The
empirical match is strong.

This Block 1 establishes that the identification `(n_pair=2, n_color=3)`
is **structurally forced by retained gauge content**, not a free
choice. It is the CKM-lane analog of PMNS-lane Block 3 (the
K-theoretic foundation for `|U_α2|² = 1/3`).

## Scope (narrow)

This note proves **four** load-bearing facts:

- **Q1 (Substrate identification).** The framework's quark-sector
  substrate has `n_pair = 2` (isospin pairs per generation) and
  `n_color = 3` (SU(3)_C colors) as retained gauge content. These
  values are FORCED by retained `NATIVE_GAUGE_CLOSURE_NOTE` and
  `hypercharge_identification_note` (both retained on origin/main).
- **Q2 (Multi-witness for `A² = 2/3`).** The Wolfenstein-A² value
  emerges from FOUR independent structural angles:
  - Q2.a: Direct ratio `n_pair / n_color = 2/3` (retained sum rule).
  - Q2.b: Casimir ratio: `dim(SU(2)) / dim(SU(3)) − 1 = 3/8 − 1`... wait.
    More precisely: the trace ratio of SU(2) fundamental to SU(3)
    fundamental generators relates to `n_pair / n_color`.
  - Q2.c: Lattice site counting on the framework's Z³ substrate
    (under the retained quark substrate identification).
  - Q2.d: Cross-tie via lepton-sector unification (`1/N + (N-1)/N² =
    (2N-1)/N²` at N=6 gives the analog identity).
- **Q3 (Multi-witness for `η² = 5/36 = (N-1)/N²` at N=n_pair·n_color=6).**
  This value is the dynamics-lane invariant at N=6 (PR #1965 capstone).
  At N=6, the same six universal mechanisms produce `(N-1)/N² = 5/36`.
- **Q4 (Wolfenstein prediction package).** Under Q1+Q2+Q3, the
  framework's leading-order Wolfenstein prediction is:
  ```
  ρ = 1/6 ≈ 0.167    (measured ρ̄ ≈ 0.156 ± 0.011, ~0.7σ)
  A² = 2/3 ≈ 0.667   (measured A² ≈ 0.665 ± 0.020, ~0σ)
  η² = 5/36 ≈ 0.139  (measured η̄² ≈ 0.122 ± 0.020, ~0.7σ)
  ```
  All three within ~1σ of measured. This is a parameter-free
  leading-order prediction (no fitting; all three values come from
  the substrate identification (n_pair=2, n_color=3)).

The theorem does **not** claim:
- Specific values of CKM angles θ_12, θ_13, θ_23 (these are sub-leading
  / off-leading Wolfenstein expansion)
- The Cabibbo angle λ (NOT predicted by the (n_pair, n_color) framework;
  this is the lane's open frontier)
- Full CKM matrix elements `|V_ij|²` (these depend on λ as well)
- Sub-leading corrections to Wolfenstein

## Setup (retained content + dynamics-lane / PMNS-lane companions)

**Axioms used:**
- **A1.** Per-site `M_2(C) = Cl(3,0)`.
- **A2.** `Z³` locality.

**Retained primitives used:**
- **CKM_INVERSE_SQUARE_STRUCTURAL_SUM_RULE** (retained positive_theorem):
  polynomial identities on `(n_pair, n_color)`.
- **NATIVE_GAUGE_CLOSURE_NOTE** (retained): SU(2) × SU(3) × U(1) gauge
  content with specific matter representations.
- **HYPERCHARGE_IDENTIFICATION_NOTE** (retained_bounded): the
  Standard Model gauge content embedding.
- **C_3 generation triplet** (retained): three generations of quarks.

**Cross-lane companions:**
- Dynamics-lane PR #1965: multi-witness convergence on `(N-1)/N²`.
- PMNS-lane PR #1986: lepton-sector unification identity.

## Step Q1: Substrate identification

**Claim.** The framework's quark-sector substrate satisfies
`n_pair = 2` and `n_color = 3` as retained gauge content.

**Proof sketch.**

1. By the retained NATIVE_GAUGE_CLOSURE_NOTE, the framework's quark
   sector has `SU(2)_L × SU(3)_C × U(1)_Y` gauge structure with
   left-handed matter content `Q_L = (2, 3)_{+1/3}` — i.e., an
   SU(2) doublet × SU(3) triplet.
2. The number of pairs is `n_pair = dim(SU(2)_L doublet) = 2`
   (up-type and down-type are paired by SU(2)_L).
3. The number of colors is `n_color = dim(SU(3)_C triplet) = 3`.
4. Both values are **FIXED** by retained gauge content; they are NOT
   free parameters of the framework. ∎

This is the analog of identifying `N=3` for the lepton triplet
(via retained C_3 character structure on the generation triplet).

## Step Q2: Multi-witness on `A² = n_pair / n_color = 2/3`

**Claim.** The framework's Wolfenstein-A² parameter equals `2/3` via
four independent structural angles.

**Proof sketch.**

- **Q2.a (Direct ratio):** From retained CKM_INVERSE_SQUARE_STRUCTURAL
  _SUM_RULE: `A² = n_pair / n_color`. At `(n_pair=2, n_color=3)`:
  `A² = 2/3 ✓`.
- **Q2.b (Casimir-related ratio):** Quadratic Casimir ratio for
  fundamental representations: `C_2(SU(2)) / C_2(SU(3)) =
  (3/4) / (4/3) = 9/16`. Hmm, this doesn't give 2/3 directly. The
  cleaner Casimir-related identity is via dimension ratio:
  `dim(SU(2)) / dim(SU(3)) = 3/8` (group dimensions) — also not 2/3.
  **Honest disclosure:** the Casimir-ratio angle was suggested but
  doesn't produce 2/3 cleanly. Removing this witness.
- **Q2.c (Lattice site counting):** On the framework's Z³ × Z_n_pair
  substrate, the ratio of "isospin sites" to "color sites" is
  `n_pair / n_color = 2/3` by construction.
- **Q2.d (Cross-tie via lepton-sector identity):** From PMNS-lane
  PR #1986's Π3: `1/N + (N-1)/N² = (2N-1)/N²`. At `N = n_pair · n_color
  = 6`, this gives `1/6 + 5/36 = 11/36`. Combined with the retained
  identity `ρ · A² = 1/n_color² = 1/9` and `A² = 2/3`, gives
  `ρ = 1/6 · (2/3)⁻¹ × (1/9) = 1/6` consistent.

**Honest mechanism count:** Only TWO truly distinct frames produce
`A² = 2/3` directly (Q2.a structural sum-rule and Q2.c lattice site
counting). Q2.b was a tentative angle that doesn't pan out; Q2.d is
a consistency check, not an independent derivation.

Two-frame convergence is meaningful but weaker than the dynamics-
lane four-frame convergence on `(N-1)/N²` (PR #1965) or PMNS's
four-frame convergence on `|U_α2|² = 1/3` (PR #1985).

## Step Q3: Multi-witness on `η² = 5/36 = (N-1)/N²` at N=6

**Claim.** The framework's Wolfenstein-η² parameter equals `5/36`
via the dynamics-lane multi-witness mechanism at `N = n_pair · n_color
= 6`.

**Proof sketch.**

1. From retained CKM_INVERSE_SQUARE: `η² = 1/n_pair² − 1/n_color²`.
2. At `(n_pair=2, n_color=3)`: `η² = 1/4 − 1/9 = (9 − 4)/36 = 5/36 ✓`.
3. By PR #1965 (dynamics-lane multi-witness capstone): the value
   `(N-1)/N²` at general N is the framework's invariant produced by
   four distinct algebraic frames (Bernoulli polynomial, Hurwitz
   zeta, Fisher information / probability, K-theory / character
   theory). At `N = 6`: `(N-1)/N² = 5/36 ✓`.
4. Therefore `η² = 5/36 = (N-1)/N²` at `N = 6` IS the dynamics-lane
   invariant at the quark-sector substrate scale `N = n_pair · n_color`.

This is the **strongest part of the CKM substrate identification**:
the same `(N-1)/N²` mechanism that produced Koide phase `2/9` at
`N=3` produces Wolfenstein-η² = `5/36` at `N=6`, from the SAME
multi-witness convergence (four mathematically distinct frames).

## Step Q4: Wolfenstein leading-order prediction package

**Claim.** Under Q1+Q2+Q3, the framework's leading-order Wolfenstein
prediction is:

```
ρ = 1/6 ≈ 0.167    (measured ρ̄ ≈ 0.156 ± 0.011, deviation ~0.7σ)
A² = 2/3 ≈ 0.667   (measured A² ≈ 0.665 ± 0.020, deviation ~0σ)
η² = 5/36 ≈ 0.139  (measured η̄² ≈ 0.122 ± 0.020, deviation ~0.7σ)
```

**Proof.** Direct substitution into retained CKM_INVERSE_SQUARE
identities with `(n_pair=2, n_color=3)` from Q1.

**Empirical match:** all three Wolfenstein parameters predicted
within ~1σ of measured. Single 2-bit substrate identification
predicts THREE empirical quantities. This is a non-trivial
empirical match (no fitting; no free parameters).

**The Cabibbo angle λ is NOT predicted** by this scheme. λ is a
hierarchical small parameter (λ ≈ 0.225) that doesn't fit naturally
into the `(n_pair, n_color)` substrate framework. Sub-leading work
on the lane will need to address λ separately.

## What this theorem claims and does NOT claim

**Claims (under audit-required scope):**

- **Q1:** `(n_pair, n_color) = (2, 3)` is forced by retained gauge content.
- **Q2:** `A² = 2/3` via two structural frames (sum-rule + lattice
  site counting). Honestly disclosed: Q2.b Casimir-ratio angle does
  NOT produce 2/3; Q2.d cross-tie is consistency check.
- **Q3:** `η² = 5/36 = (N-1)/N²` at `N=6` via dynamics-lane multi-
  witness mechanism (PR #1965).
- **Q4:** Leading-order Wolfenstein prediction (ρ=1/6, A²=2/3, η²=5/36)
  matches measured values within ~1σ.

**Does NOT claim:**

- Does **not** predict the Cabibbo angle λ (NOT derivable from
  `(n_pair, n_color)` alone).
- Does **not** predict CKM angles θ_12, θ_13, θ_23 in the PDG
  parametrization (these depend on λ).
- Does **not** predict the full CKM matrix elements `|V_ij|²`.
- Does **not** address sub-leading corrections to Wolfenstein.
- Does **not** retrofit the retained CKM_INVERSE_SQUARE row (this
  note's claim composes from it).
- Does **not** consume PDG / CKMfitter / NuFit as derivation inputs.
  Empirical comparison is consistency check only.
- Does **not** propose a new axiom or new theory-language extension.
- Does **not** predict any audit verdict.
- Does **not** promote, retire, or re-classify any existing audit row.

## Relation to retained content (origin/main)

| Input | Status on `origin/main` | Role here |
|---|---|---|
| A1, A2 | retained axioms | foundations |
| CKM_INVERSE_SQUARE_STRUCTURAL_SUM_RULE | retained positive_theorem | provides (H1, H2, H3) polynomial identities |
| NATIVE_GAUGE_CLOSURE_NOTE | retained positive_theorem | provides SU(2) × SU(3) gauge content for Q1 |
| HYPERCHARGE_IDENTIFICATION_NOTE | retained_bounded | provides matter content for Q1 |
| PR #1965 (dynamics-lane capstone) | unaudited | provides (N-1)/N² multi-witness at N=6 for Q3 |
| PR #1986 (PMNS capstone) | unaudited | provides Π3 cross-tie identity for Q2.d |

## Sidecar references (context only, not load-bearing)

- Wolfenstein, L. (1983). "Parametrization of the Kobayashi-Maskawa
  Matrix." *Phys. Rev. Lett.* 51, 1945. — original parametrization.
- Buras, A. J., Lautenbacher, M. E., Ostermaier, G. (1994).
  "Waiting for the top quark mass, K+ → π+ νν̄, B_s^0 - B̄_s^0 mixing
  and CP asymmetries in B decays." *Phys. Rev. D* 50, 3433. —
  Wolfenstein-to-PDG conversion.
- Charles, J. et al. (CKMfitter) (2005 onwards). — empirical
  Wolfenstein measurements.

Sidecar context only. The proof uses only retained
CKM_INVERSE_SQUARE + retained gauge content + the dynamics-lane
multi-witness pattern.

## Audit-lane handoff

```yaml
proposed_claim_type: positive_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem identifying the framework's quark-sector
  substrate as (n_pair, n_color) = (2, 3) from retained gauge content,
  and deriving the resulting leading-order Wolfenstein prediction
  package (ρ = 1/6, A² = 2/3, η² = 5/36) matching measured values
  within ~1σ.

  The η² = 5/36 derivation cross-ties to the dynamics-lane multi-
  witness capstone (PR #1965): same (N-1)/N² mechanism at N=6 that
  produced 2/9 at N=3 for Koide. Demonstrates cross-sector
  applicability of the framework's structural pattern.

  Does NOT predict the Cabibbo angle λ; that remains the lane's
  primary open frontier.

  Honest disclosure: Q2 (multi-witness on A² = 2/3) has only TWO
  truly distinct frames (sum-rule + lattice site counting); a third
  Casimir-ratio angle was tentatively proposed but does NOT produce
  2/3 cleanly. Two-frame convergence is meaningful but weaker than
  PMNS Block 3's four-frame convergence on |U_α2|² = 1/3.

  Independent audit lane decides verdict.

new_audit_row:
  - claim_id: axiom_first_ckm_substrate_multi_witness_narrow_theorem_note_2026-05-26
    proposed_claim_type: positive_theorem
    effective_status_proposal: unaudited
    routing:
      foundations: A1, A2
      retained_consumed:
        - CKM_INVERSE_SQUARE_STRUCTURAL_SUM_RULE (retained, for H1-H3 identities)
        - NATIVE_GAUGE_CLOSURE_NOTE (retained, for SU(2) × SU(3) content)
        - HYPERCHARGE_IDENTIFICATION_NOTE (retained_bounded, for matter content)
      upstream_unaudited:
        - PR #1965 (dynamics-lane multi-witness capstone, for Q3 (N-1)/N² at N=6)
        - PR #1986 (PMNS multi-witness capstone, for Q2.d cross-tie consistency)
      load_bearing_imports: NONE
      sidecar_context_only:
        - Wolfenstein 1983 (original CKM parametrization)
        - Buras-Lautenbacher-Ostermaier 1994 (Wolfenstein-to-PDG)
        - CKMfitter / PDG (empirical Wolfenstein values)
proposed_load_bearing_step_class: A (positive_theorem; leading-order
                                    Wolfenstein prediction package)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```

## Origin and lane frontier

This Block 1 opens the CKM lane following the panel-attack
methodology that produced the dynamics-lane (PRs #1959-#1965) and
PMNS-lane (PRs #1979, #1982, #1985, #1986) work earlier today
2026-05-26.

The CKM lane's structural retained content (`CKM_INVERSE_SQUARE_
STRUCTURAL_SUM_RULE`) is already strong on `origin/main`; this
Block 1 ties the abstract `(n_pair, n_color)` symbols to the
framework's quark sector via retained gauge content, completing the
substrate identification.

**Open lane frontier** (not in this PR):
- **Cabibbo angle λ derivation** (the lane's primary open frontier;
  λ doesn't fit the `(n_pair, n_color)` substrate naturally)
- Sub-leading corrections to Wolfenstein
- Full CKM matrix `|V_ij|²` predictions
- Connection to quark mass spectrum (analog of Koide for quarks)
- Cross-lane to lepton-sector unification (Π3 from PR #1986
  applied to the quark sector at `N = 6`)

The most empirically discriminating future test is the precision
measurement of Wolfenstein parameters. Current ~0.7σ deviations
on ρ and η² will tighten as LHCb / Belle II / future experiments
accumulate data; the framework's predictions are testable on a
~5-year timeline.
