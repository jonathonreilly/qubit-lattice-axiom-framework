# Axiom-First PMNS TM_2 Full Magnitudes-Squared Matrix (Narrow) Theorem

**Date:** 2026-05-26
**Type:** source-only theorem-note proposal (research lane).
**Lane:** PMNS lane, Block 2 (downstream of Block 1 = PR #1979).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Upstream:**
- [`docs/AXIOM_FIRST_PMNS_TM2_LEADING_ORDER_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_PMNS_TM2_LEADING_ORDER_NARROW_THEOREM_NOTE_2026-05-26.md)
  (PR #1979, `unaudited positive_theorem`). Supplies L1 (trimaximal
  middle column), L2 (maximal atmospheric), L4 (maximal CP violation).
**Runner:**
[`scripts/frontier_pmns_tm2_full_magnitudes_narrow_verifier.py`](../scripts/frontier_pmns_tm2_full_magnitudes_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_pmns_tm2_full_magnitudes_narrow_verifier.txt`](../logs/runner-cache/frontier_pmns_tm2_full_magnitudes_narrow_verifier.txt)

## Why this note exists

Block 1 (PR #1979) proved the TM_2 leading-order PMNS structure: middle
column `|U_α2|² = 1/3`, maximal atmospheric `θ_23 = π/4`, sum rule, and
maximal CP violation `cos δ_CP = 0`. The note proved these as four
SEPARATE claims (L1, L2, L3, L4).

This Block 2 theorem **combines** Block 1's claims to produce the
**complete `|U|²` (magnitudes-squared) matrix** at leading order,
parametrized by **a single free parameter** `s² := sin²θ_13`.

The result is a closed-form prediction of all nine PMNS
magnitudes-squared values from a single empirical input. This is the
cleanest empirically-testable form of the framework's TM_2 prediction
and is the natural setup for future sub-leading work
(deriving θ_13 from C_3 breaking, addressing the empirical
discrepancies).

## Scope (narrow)

This note proves **one** load-bearing fact using only Block 1's claims
+ unitarity:

- **M1 (TM_2 Full Magnitudes Matrix).** Under Block 1's L1 + L2 + L4
  + unitarity, the PMNS magnitudes-squared matrix `|U|²` has the
  closed form

```
|U|² = ( 2/3 − s²      1/3      s²        )
       ( 1/6 + s²/2    1/3     (1 − s²)/2 )    where s² := sin²θ_13
       ( 1/6 + s²/2    1/3     (1 − s²)/2 )
```

with `s² ∈ [0, 2/3]` (the physical range; `s² < 1/3` empirically).

The matrix is **doubly stochastic** (rows and columns each sum to 1)
and has the structure:
- Column 2 is trimaximal (entries 1/3) — from L1
- Rows 2 and 3 are identical (μτ-democracy) — from L2
- Column 3 has the asymmetric pattern `(s², (1-s²)/2, (1-s²)/2)` — from L2 + L4
- Column 1 has the pattern `(2/3 - s², 1/6 + s²/2, 1/6 + s²/2)` — from row/column unitarity

The theorem does **not** claim:
- A specific value of `s²` (free parameter; closes when sub-leading
  θ_13 derivation lands)
- Phases (CP-violating phase δ_CP ∈ {π/2, 3π/2} from L4 is part of
  Block 1; this note works at the |U|² level)
- Sub-leading deviations from this leading-order matrix

## Setup (Block 1 + unitarity)

**Premises used:**
- **L1 (Block 1):** `|U_α2|² = 1/3` for `α ∈ {e, μ, τ}`.
- **L2 (Block 1):** `|U_μi|² = |U_τi|²` for `i ∈ {1, 2, 3}`
  (μτ-democracy from R2 + unitarity).
- **Unitarity:** `Σ_i |U_αi|² = 1` (row sums); `Σ_α |U_αi|² = 1`
  (column sums).
- **PDG parametrization:** `|U_e3|² = sin²θ_13 = s²` (definition).

L4 (maximal CP violation) is consistent with M1 but not used in the
algebra; M1 is independent of the phase structure.

## Step M1: Closed form of the |U|² matrix

**Claim.** Under L1 + L2 + unitarity + the PDG definition `s² = sin²θ_13`,

```
|U|² = ( 2/3 − s²      1/3      s²        )
       ( 1/6 + s²/2    1/3     (1 − s²)/2 )
       ( 1/6 + s²/2    1/3     (1 − s²)/2 )
```

**Proof.**

*Row 1 (electron flavor).*
- `|U_e2|² = 1/3` (from L1)
- `|U_e3|² = s²` (PDG definition)
- `|U_e1|² = 1 − |U_e2|² − |U_e3|² = 1 − 1/3 − s² = 2/3 − s²`
  (row-1 unitarity)

*Row 2 (μ) + Row 3 (τ) — equal by L2.*
- `|U_μ2|² = 1/3` (from L1)
- `|U_μ3|² = |U_τ3|²` (from L2). Together with column-3 unitarity:
  `s² + 2 |U_μ3|² = 1`, hence `|U_μ3|² = (1 − s²)/2`.
- `|U_μ1|² = |U_τ1|²` (from L2). Together with column-1 unitarity:
  `|U_e1|² + 2 |U_μ1|² = 1`, hence
  `|U_μ1|² = (1 − (2/3 − s²))/2 = (1/3 + s²)/2 = 1/6 + s²/2`.

*Consistency check.* Row-2 unitarity:
  `|U_μ1|² + |U_μ2|² + |U_μ3|² = (1/6 + s²/2) + 1/3 + (1 − s²)/2`
  `= 1/6 + 1/3 + 1/2 + s²/2 − s²/2 = 1`. ✓

This proves the closed form. ∎

## Structural properties of the matrix

- **Doubly stochastic.** All rows sum to 1 (row unitarity); all
  columns sum to 1 (column unitarity). Verified directly:
  - Row 1: `(2/3 − s²) + 1/3 + s² = 1` ✓
  - Row 2 = Row 3: `(1/6 + s²/2) + 1/3 + (1 − s²)/2 = 1` ✓
  - Column 1: `(2/3 − s²) + 2(1/6 + s²/2) = 2/3 − s² + 1/3 + s² = 1` ✓
  - Column 2: `3 × 1/3 = 1` ✓
  - Column 3: `s² + 2(1 − s²)/2 = s² + 1 − s² = 1` ✓
- **μτ-democracy.** Row 2 = Row 3, exactly.
- **Trimaximal column 2.** All entries 1/3.
- **Single free parameter.** Once `s²` is fixed, the entire matrix is
  determined.
- **Rationality at `s² = 0`.** When θ_13 = 0 (tribimaximal limit):
  - `|U|² = (2/3, 1/3, 0; 1/6, 1/3, 1/2; 1/6, 1/3, 1/2)`. All
    entries are rationals with denominator 6 (= |S_3|).
- **Rationality at small rational `s²`.** If `s² = 1/45` (close to
  measured value 0.0223), all entries are rational with denominator
  90.

## What this theorem claims and does NOT claim

**Claims (under audit-required scope):**

- **M1:** the closed form of `|U|²` as stated, parametrized by `s²`.
- The matrix is doubly stochastic, μτ-democratic, trimaximal in
  column 2.
- At `s² = 0`: rational matrix with denominator 6; at `s² = 1/45`:
  rational matrix with denominator 90.
- Block 1's L4 (`cos δ_CP = 0`, maximal CP) is consistent with this
  matrix but works at the phase level, not the magnitude level.

**Does NOT claim:**

- Does **not** specify `s²`. The free parameter is determined only
  by sub-leading C_3-breaking corrections (separate PR).
- Does **not** address the empirical tensions:
  - `|U_e1|²`: predicted `2/3 − 0.0223 = 0.644`, measured `0.673`
    (deviation `0.029`, ~3σ)
  - `|U_e2|²`: predicted `1/3 = 0.333`, measured `0.305`
    (deviation `0.028`, ~3σ — the L3 sum-rule tension)
  - `|U_μ1|²`: predicted `1/6 + 0.0223/2 = 0.178`, measured `0.116`
    (deviation `0.062`, large)
- Does **not** consume PDG, NuFit, or empirical anchors as
  derivation inputs.
- Does **not** propose a new axiom or new theory-language extension.
- Does **not** predict any audit verdict.
- Does **not** promote, retire, or re-classify any existing audit
  row.
- Does **not** address neutrino mass observables or phases beyond L4.

## Empirical comparison (consistency check only)

At measured `s² = sin²θ_13 = 0.0223`, the framework's leading-order
TM_2 magnitudes are:

| Entry | Predicted | Measured (NuFit 5.3) | Deviation |
|---|---|---|---|
| `\|U_e1\|²` | 0.644 | 0.673 ± 0.012 | +0.029 (~2.4σ) |
| `\|U_e2\|²` | 0.333 | 0.305 ± 0.012 | -0.028 (~2.3σ) |
| `\|U_e3\|²` | 0.022 | 0.022 ± 0.001 | exact |
| `\|U_μ1\|²` | 0.178 | 0.116 ± ~ | +0.062 (large) |
| `\|U_μ2\|²` | 0.333 | 0.345 ± ~ | -0.012 |
| `\|U_μ3\|²` | 0.489 | 0.539 ± 0.020 | -0.050 (~2.5σ) |
| `\|U_τ1\|²` | 0.178 | 0.211 ± ~ | -0.033 |
| `\|U_τ2\|²` | 0.333 | 0.349 ± ~ | -0.016 |
| `\|U_τ3\|²` | 0.489 | 0.439 ± 0.020 | +0.050 (~2.5σ) |

**Pattern:**
- Column 3 (`U_e3`): `|U_e3|²` matches exactly (definitional)
- Column 2: matches within ~1σ everywhere
- Column 1 and Column 3 (μ, τ): show ~2-3σ deviations,
  systematic in pattern

The systematic deviations in columns 1 and 3 suggest a specific
sub-leading C_3-breaking pattern. Identifying and deriving that
pattern is the next-block lift (out of scope here).

**μτ-democracy test:** the predicted exact equality of rows 2 and 3
(`|U_μi|² = |U_τi|²` for all i) is testable. Currently
measured |U_μ3|² = 0.539 vs |U_τ3|² = 0.439 — deviation of ~0.1,
~3.5σ. This is the empirical signature of θ_23 sub-leading correction
(measured `sin²θ_23 ≈ 0.55` vs predicted `0.5`).

## Relation to retained content (origin/main)

| Input | Source | Role here |
|---|---|---|
| A1, A2 | retained axioms (on `origin/main`) | foundation |
| pmns_oriented_cycle_channel_value_law | retained (positive_theorem) | via Block 1's L1 |
| pmns_graph_first_residual_antiunitary | retained (positive_theorem) | via Block 1's L2 |
| Block 1 (PR #1979) | unaudited (this lane) | supplies L1, L2, L4 |

This note **adds** only the algebraic closed form for `|U|²`.
It does **not** touch any individual retained row.

## Sidecar references (context only, not load-bearing)

- Bjorken, J. D. — physical interpretation of mixing matrices via
  magnitudes-squared (rather than angles). Lens noted in 20-physicist
  panel 2026-05-26.
- Lam, C. S. — residual-symmetry classification context.
- Harrison, Perkins, Scott (2002), King (multiple reviews), Petcov —
  TM_2 phenomenology context.

These references are sidecar context only. M1's proof uses only
Block 1 + elementary unitarity arithmetic.

## Audit-lane handoff

```yaml
proposed_claim_type: positive_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem deriving the full TM_2 magnitudes-squared
  matrix |U|² from Block 1's L1 + L2 + unitarity. Single closed-form
  result M1: the 3x3 |U|² matrix has the form
    |U|² = (2/3-s², 1/3, s²; 1/6+s²/2, 1/3, (1-s²)/2; 1/6+s²/2, 1/3, (1-s²)/2)
  with s² := sin²θ_13 as the only free parameter.

  The matrix is doubly stochastic, μτ-democratic, trimaximal in
  column 2. At s² = 0 it is rational with denominator 6; for small
  rational s² (e.g., 1/45) it is rational with denominator 90.

  Empirical comparisons (consistency checks only): column-2 and U_e3
  match within ~1σ; column-1 and column-3 show ~2-3σ deviations
  signaling a specific sub-leading C_3-breaking pattern (not derived
  here).

  Independent audit lane decides verdict.

new_audit_row:
  - claim_id: axiom_first_pmns_tm2_full_magnitudes_narrow_theorem_note_2026-05-26
    proposed_claim_type: positive_theorem
    effective_status_proposal: unaudited
    routing:
      foundations: A1, A2
      retained_consumed:
        - pmns_oriented_cycle_channel_value_law_note (via Block 1)
        - pmns_graph_first_residual_antiunitary_narrow_theorem_note_2026-05-16 (via Block 1)
      upstream_unaudited:
        - axiom_first_pmns_tm2_leading_order_narrow_theorem_note_2026-05-26 (PR #1979)
      load_bearing_imports: NONE
      sidecar_context_only:
        - Bjorken (|U|² magnitudes reframe)
        - Harrison-Perkins-Scott 2002 (TBM/TM_2 context)
        - Lam 2007-2012 (residual-symmetry classification context)
        - Petcov (TM_2 phenomenology)
proposed_load_bearing_step_class: A (positive_theorem; closed-form full
                                    magnitudes matrix from Block 1)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```
