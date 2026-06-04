# Flavor — the log-det generator W = log|det(D+J)| decomposes into three factors; the Record axiom closes the additivity factor, reducing the 59-row log-det blocker to a precise residual (det-character + source-coupling)

**Date:** 2026-06-04
**Claim type:** a provenance decomposition / roadmap (converts the dominant log-det blocker into its precise remaining factors). Not a value derivation, not a row promotion.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not re-cite, edit, or promote any existing dependent row — that surface is owned by the dependency-rewrite audit and the independent audit lane.
**Runner:** `scripts/flavor_logdet_generator_three_factor_provenance_2026_06_04.py` (SCORECARD 5/5).
**Depends:** `minimal_axioms` (the Record axiom) for the additivity factor.

## Context
The 2026-06-04 dependency audit (`RECORD_P1_DEPENDENCY_AUDIT_NOTE`) found that of the 91 direct
dependents of the old observable-principle parent, **59 are blocked specifically on the log-det
generator** `W = log|det(D+J)|` (the dominant category; the next is the observable bridge, 18). The
narrow Record axiom does not move these rows because the log-det generator needs more than additivity.
This note makes "more than additivity" **precise**, so the blocker becomes an actionable residual rather
than a monolithic conditional parent.

## The three factors of W = log|det(D+J)|
| factor | content | status after the Record axiom |
|---|---|---|
| **1 — additivity** | `W` adds over disjoint record collections: `W = Σ_modes log\|λ\|`, and over a disjoint-site (block-diagonal) domain `W(K₁⊕K₂)=W(K₁)+W(K₂)` | **closed by the Record axiom** (`minimal_axioms`) |
| **2 — det multiplicative-character** | the per-block form is the det character (`det(AB)=det(A)det(B)`, `Tr` is not); only its additive image `log\|det\|` survives factor 1 | **det-character note** (`OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION`, currently unaudited) — separate target |
| **3 — source/action coupling** | the local source-derivative algebra `dW/dj_x = Re Tr[(D+J)⁻¹ P_x]` couples `W` to the source `J` | **admission** (source/action) — separate target |

All three verified numerically (runner 5/5): factor 1 as additivity over modes and over disjoint-site
blocks; factor 2 as det-multiplicativity (vs `Tr`); factor 3 as the exact match of
`dW/dj_x = Re Tr[(D+J)⁻¹ P_x]` against the numeric derivative.

## Consequence — the precise residual
**The Record axiom discharges exactly factor 1.** So the 59-row log-det blocker reduces to the residual
**{factor 2: det-character (needs audit), factor 3: source-coupling (admission)}** — and *not* to the
additivity that was the historical sticking point (the `p1_exponent_fixing` no-go and the
`extensivity_primitive` two-slope hole are both factor-1 content, now axiom-closed). Closing factor 2
(getting the det-character form to a clean audit-ready state) and pinning factor 3 (the source-coupling
admission) would convert `W` from a monolithic conditional parent into `[axiom ⊕ retained ⊕ admission]`,
the path to cascading the 59-row log-det category.

## Scope discipline
This is a positive provenance theorem on **new files only**. It does **not** touch the 91 dependents,
`observable_principle_from_axiom_note`, the axiom-premise allowlist, or any audit data file; it does not
re-cite or predict the status of any row. The dependency classification is owned by
`RECORD_P1_DEPENDENCY_AUDIT_NOTE`; all status is the independent audit lane's.

## The next paths this opens (not closing)
- **Factor 2:** harden `DET_UNIQUE_MULTIPLICATIVE` (det = unique multiplicative character up to power) to
  a clean audit-ready object (companion form theorem `FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM` supplies the
  Record-axiom side of the product).
- **Factor 3:** pin the source/action coupling — the `D+J` insertion and its local derivative — as a
  named retained authority or a scoped admission, separating it cleanly from the form.

## Provenance (verified 2026-06-04)
- `W = Σ_modes log|λ|`; disjoint-site block additivity; `det` multiplicative vs `Tr`;
  `dW/dj_x = Re Tr[(D+J)⁻¹ P_x]` vs numeric derivative (`max|Δ| < 1e-6`): verified directly (runner 5/5).
- This note sets no audit status; it decomposes the log-det blocker into its three factors and names the
  residual after the Record axiom.
