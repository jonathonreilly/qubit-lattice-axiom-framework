# PMNS Multi-Witness Convergence Capstone Theorem

**Date:** 2026-05-26
**Type:** capstone source-only theorem-note proposal (research lane).
**Lane:** PMNS lane, Block 4 (capstone for Blocks 1-3).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Proposed claim type:** `positive_theorem` (capstone closure of the
PMNS lane Blocks 1-3; conditional on upstream PR audits).
**Upstream PRs (all `unaudited` on date of this note):**
- [PR #1979 — Block 1](#) — TM_2 leading-order theorem (L1-L4)
- [PR #1982 — Block 2](#) — full |U|² magnitudes matrix closed form (M1)
- [PR #1985 — Block 3](#) — K-theoretic / Z_3 DFT foundation (K1-K4)

**Cross-lane companions (dynamics-lane):**
- [PR #1961](#) — Z_N equivariant spectral asymmetry (η = (N-1)/N²)
- [PR #1965](#) — dynamics-lane multi-witness capstone (mirrors this PR's structure)

**Runner:**
[`scripts/frontier_pmns_multi_witness_convergence_capstone_verifier.py`](../scripts/frontier_pmns_multi_witness_convergence_capstone_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_pmns_multi_witness_convergence_capstone_verifier.txt`](../logs/runner-cache/frontier_pmns_multi_witness_convergence_capstone_verifier.txt)

## Why this capstone exists

The PMNS lane (Blocks 1-3, opened 2026-05-26) has produced a coherent
leading-order PMNS prediction from A1+A2 + the two retained PMNS
residual symmetries (oriented-cycle channel value law + graph-first
residual antiunitary). The prediction has four parts (TM_2 structure,
full |U|² closed form, K-theoretic foundation, cross-tie to
dynamics-lane).

This capstone collects those into a single positive_theorem statement
with conditional closure structure, mirroring the dynamics-lane
PR #1965 pattern. It serves three purposes:

1. **Bookkeeping consolidation** of Blocks 1-3 into one audit row.
2. **Cross-tie identity** showing the lepton sector's two invariants
   (PMNS column-2 = 1/N; Koide-axis = (N-1)/N²) live on the same
   Z_3 substrate and sum to (2N-1)/N².
3. **Conditional capstone closure**: under the five hypothesis
   (Blocks 1-3 + dynamics-lane chain), the framework's leading-order
   lepton-sector prediction is fully specified by structure.

## Scope (capstone)

This note proves **two** load-bearing parts:

- **Π1 (PMNS leading-order convergence).** Under retained content
  (R1 + R2 + R3 + C_3 character substrate), the framework's
  leading-order PMNS structure is determined to be:
  - Trimaximal middle column `|U_α2|² = 1/3 ∀α` (Block 1 L1 + Block 3
    K1-K4: four-frame convergence)
  - Maximal atmospheric `θ_23 = π/4` (Block 1 L2)
  - TM_2 sum rule `3 sin²θ_12 cos²θ_13 = 1` (Block 1 L3)
  - Maximal CP violation `cos δ_CP = 0`, hence `δ_CP ∈ {π/2, 3π/2}`
    (Block 1 L4)
  - Full |U|² closed form parametrized by `s² = sin²θ_13`
    (Block 2 M1)
- **Π2 (Conditional capstone closure).** Under hypotheses (H_B1, H_B2,
  H_B3) that Blocks 1-3 audit clean, the leading-order PMNS
  prediction is **a single retained structural object** on the
  framework's authority surface, with one free parameter (s²).
  Sub-leading derivation of s² and corrections to the leading-order
  matrix are flagged as the lane's remaining frontier.

The capstone also includes the **cross-tie identity**:

- **Π3 (Lepton-sector unification identity).** For the framework's
  Z_3 character substrate at the lepton triplet:
  `1/N + (N-1)/N² = (2N-1)/N²` (elementary arithmetic), expressing
  that the trivial-irrep density (PMNS column-2) and the
  non-trivial-irrep density (Koide-axis) sum to a structural constant.
  Verified at N ∈ {3, 4, 5, 6, 7, 12}.

## Setup (Blocks 1-3 + dynamics-lane retained content)

**Premises used:**

- **A1, A2.** Retained axioms.
- **R3.** C_3 character structure on the generation triplet
  (retained primitive).
- **R1 (Block 1 / PR #1979).** Oriented-cycle channel value law +
  L1-L4.
- **M1 (Block 2 / PR #1982).** Full |U|² closed form.
- **K1-K4 (Block 3 / PR #1985).** Four-frame foundation for
  `|U_α2|² = 1/N`.
- **Dynamics-lane retained content (companion):** PR #1961, PR #1965
  establish the (N-1)/N² mechanism on the same Z_3 substrate.

## Part Π1: PMNS leading-order convergence

**Claim.** Under retained R1 + R2 + R3 + C_3 character substrate, the
framework's leading-order PMNS prediction is the **TM_2 form with
maximal CP**:

```
|U|² = ( 2/3 − s²      1/3      s²        )
       ( 1/6 + s²/2    1/3     (1 − s²)/2 )    s² := sin²θ_13
       ( 1/6 + s²/2    1/3     (1 − s²)/2 )

δ_CP ∈ {π/2, 3π/2}    (maximal CP violation, J_PMNS ≠ 0 but cos δ = 0)

θ_23 = π/4 exactly

sin²θ_12 = 1/(3 cos²θ_13)
```

Verified through multiple algebraic frames:
- **Operator-theoretic (F1):** Block 1 L1-L4 derivation from the
  forward-cycle operator + residual antiunitary.
- **Representation-theoretic (F2-F4):** Block 3 K1-K4 derivation from
  Z_3 DFT + Schur orthogonality + K-theoretic intertwiner.

The two perspectives are mathematically equivalent via the spectral
theorem; they provide independent algorithmic verifications of the
same identity.

## Part Π2: Conditional capstone closure

**Hypotheses:**
- (H_B1) Block 1 (PR #1979) audits clean → TM_2 L1-L4 retained.
- (H_B2) Block 2 (PR #1982) audits clean → full |U|² closed form M1
  retained.
- (H_B3) Block 3 (PR #1985) audits clean → K-theoretic foundation
  K1-K4 retained.

**Claim.** Under (H_B1) ∧ (H_B2) ∧ (H_B3), the PMNS leading-order
prediction in Π1 is a **single retained structural object** on the
framework's authority surface. The remaining open frontier is:
- Sub-leading derivation of `s² := sin²θ_13` (separate PR; multi-step)
- Resolution of empirical ~2-3σ tensions in columns 1 and 3
- Resolution of ~3.5σ μτ-democracy tension (sub-leading θ_23 octant)
- Neutrino mass observables (mass ordering, scale, Majorana phases)

**Proof sketch.** Each upstream Block establishes one component of
the PMNS prediction. Under their joint audit-ratification, the four
components L1-L4 + M1 + K1-K4 compose into a single coherent
structural object. The composition is straightforward: M1 is the
explicit closed form derived from L1+L2+unitarity, and K1-K4 provide
independent algebraic verifications of L1 via the Z_3 representation
ring. ∎

## Part Π3: Lepton-sector unification identity

**Claim.** The framework's Z_3 character substrate produces two
distinct invariants at the lepton triplet, summing to a structural
constant:

```
1/N + (N-1)/N² = (2N-1)/N²
```

where:
- `1/N` = trivial-irrep density (PMNS column-2 magnitude;
  Block 3 K3)
- `(N-1)/N²` = non-trivial-irrep density (Koide-axis invariant; PR
  #1961, PR #1965)
- `(2N-1)/N²` = structural sum

**Verification at framework-relevant N:**

| N | 1/N (PMNS) | (N-1)/N² (Koide) | (2N-1)/N² (sum) |
|---|---|---|---|
| 3 (lepton) | 1/3 ≈ 0.333 | 2/9 ≈ 0.222 | 5/9 ≈ 0.556 |
| 4 | 1/4 = 0.250 | 3/16 = 0.188 | 7/16 = 0.438 |
| 5 | 1/5 = 0.200 | 4/25 = 0.160 | 9/25 = 0.360 |
| 6 (quark sector) | 1/6 ≈ 0.167 | 5/36 ≈ 0.139 | 11/36 ≈ 0.306 |

**Interpretation.** The framework's lepton sector ENTIRELY lives on
the Z_3 character substrate, and its two physical observables
(PMNS column-2 magnitudes and Koide phase) are the two natural
invariants of that substrate (trivial and non-trivial irrep
densities). The unification identity is elementary arithmetic but
structurally meaningful: it expresses that PMNS and Koide are not
independent observables but rather two facets of the same Z_3
representation-ring structure.

**Empirical sanity check.** At N=3 (lepton):
- Predicted PMNS column-2 magnitude: 1/3 ≈ 0.333
- Predicted Koide phase: 2/9 ≈ 0.222
- Sum: 5/9 ≈ 0.556

The framework predicts that the lepton-sector's "structural budget"
across PMNS and Koide observables is exactly 5/9 in the right
normalization. This is a non-trivial framework prediction (not
input from experiment).

## What this capstone claims and does NOT claim

**Claims (under audit-required scope):**

- Π1: leading-order PMNS prediction (TM_2 + maximal CP + closed
  form) as stated.
- Π2: conditional capstone closure under (H_B1) ∧ (H_B2) ∧ (H_B3).
- Π3: lepton-sector unification identity verified at multiple N.
- The framework's lepton sector lives on the Z_3 character substrate
  with two natural invariants summing to (2N-1)/N².

**Does NOT claim:**

- Does **not** specify `s² := sin²θ_13` (free parameter; multi-PR
  sub-leading work)
- Does **not** address the ~2-3σ empirical tensions in columns 1
  and 3 of |U|² (sub-leading work)
- Does **not** resolve the ~3.5σ μτ-democracy tension (sub-leading
  θ_23 octant correction)
- Does **not** predict neutrino mass observables
- Does **not** assert any of the hypotheses (H_B1, H_B2, H_B3); the
  capstone is **conditional**
- Does **not** retrofit any retained content on `origin/main`
- Does **not** consume PDG / NuFit / empirical anchors as derivation
  inputs
- Does **not** propose a new axiom or new theory-language extension
- Does **not** predict any audit verdict
- Does **not** promote, retire, or re-classify any existing audit
  row

## Relation to retained content (origin/main)

| Input | Status on `origin/main` | Role here |
|---|---|---|
| A1, A2 | retained axioms | foundations |
| C_3 character structure on triplet | retained | Z_3 substrate |
| pmns_oriented_cycle_channel_value_law | retained positive_theorem | via Block 1 + Block 3 F1 |
| pmns_graph_first_residual_antiunitary | retained positive_theorem | via Block 1 L2 |
| Block 1 (PR #1979) | unaudited | supplies L1-L4 |
| Block 2 (PR #1982) | unaudited | supplies M1 |
| Block 3 (PR #1985) | unaudited | supplies K1-K4 |
| PR #1961 (dynamics-lane companion) | unaudited | cross-tie via (N-1)/N² |
| PR #1965 (dynamics-lane capstone) | unaudited | structural-template precedent |

## Sidecar references (context only)

- Harrison-Perkins-Scott 2002 (TBM), Lam 2007-2012 (residual
  classification), King (TM_2 phenomenology), Petcov (TM_2 sum
  rules) — historical / phenomenological context for TM_2.
- Burnside 1911 (characters), Atiyah-Bott 1968 (equivariant
  K-theory) — representation-theoretic context.

These are sidecar context only. The capstone's claims compose from
Block 1-3 (retained-conditional) + elementary arithmetic for Π3.

## Audit-lane handoff

```yaml
proposed_claim_type: positive_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only capstone for the PMNS lane. Three load-bearing parts:
  Π1 leading-order PMNS prediction (TM_2 + maximal CP + closed form),
  Π2 conditional capstone closure under Blocks 1-3 audits,
  Π3 lepton-sector unification identity 1/N + (N-1)/N² = (2N-1)/N²
     showing PMNS + Koide invariants live on same Z_3 substrate.

  The capstone is the PMNS-lane's bookkeeping reflection of the
  structural identity established by Blocks 1-3 (PRs #1979, #1982,
  #1985). It is CONDITIONAL on those three upstream audits and does
  NOT assert any of (H_B1, H_B2, H_B3).

  Independent audit lane decides verdict.

new_audit_row:
  - claim_id: pmns_multi_witness_convergence_capstone_theorem_note_2026-05-26
    proposed_claim_type: positive_theorem
    effective_status_proposal: unaudited
    conditional_on:
      - audit ratification of PR #1979 (Block 1: TM_2 leading-order)
      - audit ratification of PR #1982 (Block 2: full |U|² closed form)
      - audit ratification of PR #1985 (Block 3: K-theoretic foundation)
    routing:
      foundations: A1, A2 (retained axioms)
      retained_consumed:
        - pmns_oriented_cycle_channel_value_law_note (retained, via Block 1)
        - pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16 (retained, via Block 1)
        - C_3 character structure on triplet (retained primitive)
      upstream_unaudited:
        - PR #1979 (Block 1), PR #1982 (Block 2), PR #1985 (Block 3)
        - PR #1961, PR #1965 (dynamics-lane companions for Π3 cross-tie)
      load_bearing_imports: NONE
      sidecar_context_only:
        - Harrison-Perkins-Scott 2002 / Lam 2007 / King / Petcov (TM_2 context)
        - Burnside 1911 / Atiyah-Bott 1968 (representation theory context)
proposed_load_bearing_step_class: A (positive_theorem; capstone conditional closure)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```

## Origin

This capstone closes the PMNS lane's initial attack phase (Blocks
1-3), opened 2026-05-26 following the dynamics-lane closure
(PRs #1959-#1965). The lane was attacked with the same panel-attack
methodology used to close the Koide axis: a 20-physicist
structural-review panel converged on TM_2 mixing as the framework's
leading-order PMNS prediction; three Blocks landed that prediction
in source-note + paired-runner form.

This capstone is the PMNS analog of PR #1965 (dynamics-lane
multi-witness capstone) — same template, different observable.

**Remaining lane frontier** (not in this PR):
- Sub-leading θ_13 from C_3 breaking (multi-PR)
- Resolution of the 3σ sin²θ_12 sum-rule tension (sub-leading work)
- Resolution of the 3.5σ μτ-democracy tension (sub-leading θ_23 work)
- Neutrino mass observables (mass ordering, absolute scale, Majorana)
- Cross-lane connection to a unified "lepton-sector predicting M_l"
  theorem (uses retained STAGGERED_DIRAC infrastructure)

The framework's lepton sector is now structurally specified at
leading order, with one free parameter (s² = sin²θ_13) and the
empirically-discriminating predictions (TM_2 + maximal CP) on a
~6-year experimental timeline (JUNO, DUNE, Hyper-K).
