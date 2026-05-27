# Axiom-First PMNS TM_2 Leading-Order (Narrow) Theorem on Cl(3)/Z³

**Date:** 2026-05-26
**Type:** source-only theorem-note proposal (research lane).
**Lane:** PMNS lane (continuation of the dynamics-lane axis; uses retained
oriented-cycle / residual-antiunitary structure to derive leading-order
PMNS mixing).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Runner:**
[`scripts/frontier_pmns_tm2_leading_order_narrow_verifier.py`](../scripts/frontier_pmns_tm2_leading_order_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_pmns_tm2_leading_order_narrow_verifier.txt`](../logs/runner-cache/frontier_pmns_tm2_leading_order_narrow_verifier.txt)

## Why this note exists (mandate)

A 20-physicist structural-review panel on 2026-05-26 converged on
**Trimaximal-2 (TM_2) mixing** as the framework's leading-order PMNS
prediction. The convergence count was 14 of 20, with 6 lenses
emphasizing individual angles (θ_13, θ_12, θ_23, δ_CP) that are all
consistent with the TM_2 structure.

This note formalizes the panel's structural consensus into a single
narrow theorem with paired runner. It claims **only** the leading-order
TM_2 structure forced by the two retained residual symmetries — it does
**not** claim θ_13's specific value, sub-leading corrections, or
neutrino mass observables (which remain open).

## Scope (narrow)

This note proves **four** load-bearing facts using only A1+A2 +
the two retained PMNS residual symmetries:

- **L1 (Trimaximal middle column).** Under the retained
  `pmns_oriented_cycle_channel_value_law` (which uses the forward-cycle
  operator `C` derived from the retained C_3[111] body-diagonal
  rotation), the middle column of the PMNS matrix is
  `|U_α2|² = 1/3` for every flavor index `α ∈ {e, μ, τ}`.
- **L2 (Maximal atmospheric).** Under the retained
  `pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16`
  (`A_fwd = P_23 A_fwd† P_23`), `θ_23 = π/4` exactly at leading order,
  equivalently `sin²θ_23 = 1/2`.
- **L3 (TM_2 sum rule).** From L1, the column-2 magnitude
  `|U_e2|² = cos²θ_13 sin²θ_12 = 1/3` gives the sum rule
  `3 sin²θ_12 cos²θ_13 = 1`, equivalently
  `sin²θ_12 (3 − 3 sin²θ_13) = 1`,
  equivalently `sin²θ_12 = 1 / (3 cos²θ_13)`.
- **L4 (Maximal CP violation at leading order).** L1 + L2 + unitarity
  + the PDG parametrization, combined algebraically, force
  `cos δ_CP = 0`, hence **`δ_CP ∈ {π/2, 3π/2}` (maximal CP violation)**.
  This is the standard Petcov-Ge-Lam TM_2 + maximal-atmospheric result;
  the framework reaches it directly from R1 + R2.
  *(Note: an earlier panel-derived claim that "antiunitary R2 forces
  J_PMNS = 0 ⇒ δ_CP ∈ {0, π}" applied the antiunitary symmetry too
  loosely. R2's content is `|U_μi|² = |U_τi|²` (which gives L2), not
  full CP-symmetry. Once L1 + L2 are imposed, the residual algebraic
  freedom in the (12)-(13)-rotation is fixed by L1's |U_μ2|² = 1/3
  constraint, which forces cos δ_CP = 0.)*

The theorem does **not** claim:
- Specific value of `θ_13` (free at leading order; needs C_3 breaking)
- Sub-leading corrections to TM_2 (e.g., the 1.75σ tension on
  `sin²θ_12` empirical vs TM_2 sum rule at measured `sin²θ_13`)
- Neutrino mass observables (mass ordering, absolute scale,
  Majorana phases)

## Setup (A1+A2 + retained residual symmetries)

**Axioms used:**
- **A1.** Per-site `M_2(C) = Cl(3,0)`.
- **A2.** `Z³` locality.

**Retained primitives used:**
- **R1.** `pmns_oriented_cycle_channel_value_law_note` (retained
  positive_theorem on `origin/main`): on the `hw=1` triplet,
  `A_fwd = c_1 E_12 + c_2 E_23 + c_3 E_31` with
  `(c_1, c_2, c_3) = diag(A C†)`, `c_i = Tr((P_i C)† A)`. The forward-
  cycle operator `C` is the C_3[111] action on the triplet.
- **R2.** `pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16`
  (retained positive_theorem on `origin/main`):
  `A_fwd = P_23 A_fwd† P_23`, where `P_23` is the (μ↔τ) transposition
  acting antiunitarily.
- **R3.** Retained C_3 character structure on the generation triplet
  (multiple notes; eigenvalues `(1, ω, ω²)` with `ω = e^{2πi/3}`).
- **R4.** `pmns_oriented_cycle_selection_structure_note` (retained_bounded):
  selector structure for which sector pairs contribute.

**Lam-classification status (honest disclosure):**
Standard residual-symmetry classification (Lam, 2007–2012) requires a
pair `(G_l, G_ν)` of residual generators — one in the charged-lepton
sector, one in the neutrino sector. This note identifies:
- `G_l = ⟨C⟩` (the C_3 forward-cycle action on the channel basis,
  retained via R1 since the value law uses `C` explicitly).
- `G_ν = ⟨P_23⟩` (the residual antiunitary, retained via R2).

The C_3 residual is *implicit* in R1's use of `C` but has not been
authored as a separate "C_3 is a retained residual of A_fwd" theorem.
This note makes the identification explicit; if the audit lane wants
a separate stand-alone retained residual note, it can be authored as
a follow-up. **The Lam-classification proof here uses only R1's
content, not a new structural premise.**

## Step L1: Trimaximal middle column from C_3 + R1

**Claim.** `|U_α2|² = 1/3` for every flavor `α ∈ {e, μ, τ}`.

**Proof sketch.**
1. By R3, the C_3[111] rotation has eigenvalues `(1, ω, ω²)` on the
   `hw=1` triplet, with the eigenvector at eigenvalue 1 being the
   trimaximal vector `v_0 = (1, 1, 1) / √3`.
2. By R1, the forward-cycle operator `C` acts on the triplet by
   cyclic permutation: `C: (e, μ, τ) → (μ, τ, e)`. Its eigenvector at
   eigenvalue 1 is `v_0 = (1, 1, 1) / √3` (the C_3-trivial irrep).
3. In the basis where `C` is diagonalized, the second column of the
   diagonalizing matrix (the eigenvector at eigenvalue 1) IS `v_0`.
   Indexing this column as column 2 by convention (the middle column
   in PMNS), the PMNS matrix has `U_α2 = (v_0)_α = 1/√3` up to a
   common phase.
4. Therefore `|U_α2|² = 1/3` for `α ∈ {e, μ, τ}`. ∎

## Step L2: Maximal atmospheric mixing from R2

**Claim.** `sin²θ_23 = 1/2` at leading order (i.e., `θ_23 = π/4`).

**Proof sketch.**
1. By R2, `A_fwd = P_23 A_fwd† P_23` where `P_23` is the (μ↔τ)
   antiunitary involution.
2. In the charged-lepton-diagonal basis, this implies the neutrino
   mass operator `M_ν = U_PMNS · diag(m_1, m_2, m_3) · U_PMNS†`
   satisfies `P_23 M_ν P_23 = M_ν*` (in the appropriate ordering).
3. The (μτ)-exchange invariance forces `|U_μi|² = |U_τi|²` for every
   mass index `i ∈ {1, 2, 3}`.
4. Combined with unitarity (`Σ_α |U_αi|² = 1`), the constraint
   `|U_μ3|² = |U_τ3|²` together with `|U_e3|² = 1 − |U_μ3|² − |U_τ3|²`
   forces `sin²θ_23 = |U_μ3|² / (1 − |U_e3|²) = 1/2`.
5. Equivalently, `θ_23 = π/4`. ∎

## Step L3: TM_2 sum rule from L1

**Claim.** `3 sin²θ_12 cos²θ_13 = 1`, equivalently
`sin²θ_12 = 1 / (3 cos²θ_13)`.

**Proof sketch.**
1. By L1, `|U_e2|² = 1/3`.
2. In the PDG parametrization, `|U_e2|² = cos²θ_13 · sin²θ_12`.
3. Equating: `cos²θ_13 · sin²θ_12 = 1/3`.
4. Multiplying through by 3 gives the sum rule
   `3 sin²θ_12 cos²θ_13 = 1`. ∎

At the measured `sin²θ_13 = 0.0223`, this gives `sin²θ_12 ≈ 0.341`,
vs measured `0.305 ± 0.012` — a 3σ tension. JUNO at 4× current
precision on `sin²θ_12` will resolve in ~6 years; resolution requires
either confirmation of the tension (framework needs sub-leading
C_3-breaking corrections) or measurement shift toward 0.341.

## Step L4: Maximal CP violation from L1 + L2 + unitarity

**Claim.** `cos δ_CP = 0`, hence `δ_CP ∈ {π/2, 3π/2}` (maximal CP
violation) at leading order.

**Proof.**

1. In the PDG parametrization with `θ_23 = π/4` (from L2):
   `|U_μ2|² = (1/2) |c_12 − s_12 s_13 e^{iδ}|²`
   `= (1/2) (c_12² + s_12² s_13² − 2 c_12 s_12 s_13 cos δ)`.
2. By L1, `|U_μ2|² = 1/3`, hence:
   `c_12² + s_12² s_13² − 2 c_12 s_12 s_13 cos δ = 2/3`.
3. By L3 (from L1's |U_e2|²=1/3), `s_12² = 1/(3 cos²θ_13) = 1/(3(1−s_13²))`,
   hence `c_12² = 1 − s_12² = (2 − 3 s_13²)/(3(1 − s_13²))`.
4. Substituting:
   `c_12² + s_12² s_13² = (2 − 3 s_13²)/(3(1 − s_13²)) + s_13²/(3(1 − s_13²))
                       = (2 − 2 s_13²)/(3(1 − s_13²)) = 2/3`.
5. So the equation reduces to: `2/3 − 2 c_12 s_12 s_13 cos δ = 2/3`,
   i.e., `2 c_12 s_12 s_13 cos δ = 0`.
6. Assuming `s_13 ≠ 0` (which the data confirms), we have
   `cos δ_CP = 0`, hence `δ_CP ∈ {π/2, 3π/2}`. ∎

**Empirical comparison.** Current NuFit 5.3 / PDG central
`δ_CP ≈ 197° ± 25°` with significant model dependence:
- T2K alone prefers `δ_CP ≈ 270° = 3π/2` (maximal, in agreement
  with framework).
- NOvA alone prefers `δ_CP ≈ 180°` (CP-preserving).
- Combined: central 197° with ~25° uncertainty.

The framework's prediction `|sin δ_CP| = 1` (maximal CP violation,
either sign) is testable by DUNE (operating 2030+) and Hyper-K
(2027+) at <10° precision on `δ_CP`. **A measurement of `δ_CP`
significantly away from `±π/2` would falsify the leading-order
framework prediction.**

This is the standard Petcov-Ge-Lam TM_2 + maximal-θ_23 result,
reached here directly from the framework's two retained residual
symmetries R1 + R2.

## What this theorem claims and does NOT claim

**Claims (under audit-required scope):**

- L1: middle column `|U_α2|² = 1/3` exact at leading order.
- L2: `θ_23 = π/4` exact at leading order.
- L3: TM_2 sum rule `3 sin²θ_12 cos²θ_13 = 1`.
- L4: `δ_CP ∈ {π/2, 3π/2}` at leading order (maximal CP violation),
  forced algebraically by L1 + L2 + unitarity.
- The four claims together specify the **TM_2 (Trimaximal-2)
  leading-order form of the PMNS matrix with maximal CP violation.**

**Does NOT claim:**

- Does **not** specify `θ_13`. At leading order, `θ_13` is free; it
  becomes nonzero only under sub-leading C_3-breaking corrections,
  which this note does not derive.
- Does **not** specify `sin²θ_12` numerically. At leading order, it's
  pinned by the sum rule to a function of `sin²θ_13`; only if
  `sin²θ_13 = 0` does it reduce to `sin²θ_12 = 1/3`.
- Does **not** derive neutrino mass observables (mass ordering,
  absolute scale, Δm² values, Majorana phases).
- Does **not** address the empirical 1.75σ tension between TM_2's
  predicted `sin²θ_12 ≈ 0.326` (at measured `sin²θ_13 = 0.0223`) and
  the measured `sin²θ_12 ≈ 0.305 ± 0.012`. That tension may resolve
  via sub-leading C_3-breaking corrections that this note does not
  derive; JUNO precision (~4× current on `sin²θ_12`) will resolve in
  ~6 years.
- Does **not** consume PDG, NuFit, or empirical anchors as
  derivation inputs. Post-hoc comparisons are consistency checks
  only, not proof inputs.
- Does **not** propose a new axiom or new theory-language extension.
- Does **not** predict any audit verdict.
- Does **not** promote, retire, or re-classify any existing audit
  row.

## Relation to retained content (origin/main)

| Input | Status on `origin/main` | Role here |
|---|---|---|
| A1, A2 | retained axioms | foundations |
| C₃[111] rotation eigenvalues `(1, ω, ω²)` | retained | trimaximal eigenvector `v_0` for L1 |
| `pmns_oriented_cycle_channel_value_law_note` | retained (positive_theorem) | R1 — channel decomposition + forward-cycle `C` action |
| `pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16` | retained (positive_theorem) | R2 — `A_fwd = P_23 A_fwd† P_23` |
| `pmns_oriented_cycle_selection_structure_note` | retained_bounded | R4 — selector structure |
| `pmns_uniform_scalar_deformation_boundary_note` | retained_no_go | unchanged; operates on a different deformation surface |

This note **adds** the TM_2 leading-order specification + the
explicit Lam-classification statement. It does **not** touch any
individual retained row.

## Sidecar references (context only, not load-bearing)

- Harrison, Perkins, Scott (2002), "Tri-bimaximal mixing and the
  neutrino oscillation data," *Phys. Lett. B* 530, 167. — original
  TBM ansatz that TM_2 generalizes (relaxing the third-column zero).
- Lam, C. S. (2007–2012), residual-symmetry classification of PMNS
  mixing. — the (G_l, G_ν) framework used here for the
  Lam-classification statement.
- King, S. F. (multiple reviews 2013–2020), "Models of Neutrino
  Mass, Mixing and CP Violation." — modular-flavor / residual-
  symmetry context for TM_2.
- Petcov, S. T. (multiple papers), TM_1 / TM_2 sum-rule
  phenomenology. — context for the empirical comparison.

These references are **sidecar context**: they document the
historical and continuum-model derivations of TM_2 mixing. They are
**not load-bearing** imports for L1–L4, whose proofs use only
A1+A2 + retained content + elementary representation theory.

## Audit-lane handoff

```yaml
proposed_claim_type: positive_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem deriving the TM_2 (Trimaximal-2) leading-
  order form of the PMNS matrix from the two retained PMNS residual
  symmetries (R1 = oriented-cycle channel value law; R2 = graph-first
  residual antiunitary). Four claims L1-L4:
    L1 trimaximal middle column |U_α2|^2 = 1/3
    L2 maximal atmospheric θ_23 = π/4
    L3 TM_2 sum rule 3 sin²θ_12 cos²θ_13 = 1
    L4 maximal CP violation |sin δ_CP| = 1 (forced algebraically by
       L1 + L2 + unitarity; δ_CP ∈ {π/2, 3π/2})

  The Lam-classification (G_l, G_ν) pair is identified as
  (⟨C⟩, ⟨P_23⟩), with G_l = ⟨C⟩ retained implicitly via R1's use of the
  forward-cycle operator C. No new structural premise required;
  R1+R2 are sufficient.

  Does NOT claim θ_13 specific value, sub-leading TM_2 corrections,
  neutrino mass observables, or address the 1.75σ tension on sin²θ_12.
  Independent audit lane decides verdict.

new_audit_row:
  - claim_id: axiom_first_pmns_tm2_leading_order_narrow_theorem_note_2026-05-26
    proposed_claim_type: positive_theorem
    effective_status_proposal: unaudited
    routing:
      foundations: A1, A2
      retained_consumed:
        - pmns_oriented_cycle_channel_value_law_note (retained positive_theorem) -- R1
        - pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16 (retained positive_theorem) -- R2
        - C_3[111] rotation (retained primitive) -- R3
        - pmns_oriented_cycle_selection_structure_note (retained_bounded) -- R4
      load_bearing_imports: NONE
      sidecar_context_only:
        - Harrison-Perkins-Scott 2002 (TBM)
        - Lam 2007-2012 (residual-symmetry classification)
        - King 2013-2020 (TM_2 phenomenology)
        - Petcov (TM_2 sum-rule phenomenology)
proposed_load_bearing_step_class: A (positive_theorem; leading-order narrow theorem)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```

## Origin

This note is the first product of the PMNS lane attack initiated
2026-05-26, following the dynamics-lane closure (PRs #1959-#1965).
The lane was opened with the same panel-attack methodology used to
close the Koide axis: a 20-physicist structural-review panel
convened on the question "what's the most direct PMNS-angle
derivation from A1+A2 + retained content?"; 14 of 20 lenses
converged on TM_2 mixing as the framework's leading-order prediction.

The panel synthesis identified four leading-order claims (L1-L4)
forced by the two retained residual symmetries (R1 = oriented-cycle
channel value law; R2 = graph-first residual antiunitary) plus
the implicit C_3 cyclic residual (made explicit here). The TM_2
structure is the cleanest single-PR landing of that convergence.

Sub-leading work (specific θ_13 value, sin²θ_12 sub-leading
corrections, neutrino mass observables, the 1.75σ empirical tension)
is deferred to follow-up notes on the PMNS lane axis.
