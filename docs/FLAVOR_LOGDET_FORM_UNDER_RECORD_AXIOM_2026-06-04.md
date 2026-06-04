# Flavor — the observable generator FORM W = c·log|det| follows from the Record axiom (additivity) plus the det multiplicative-character; the Record axiom closes the additivity factor of the log-det form

**Date:** 2026-06-04
**Claim type:** a form theorem — the additive + multiplicative-character factors of the log-det generator FORM are closed (additivity by the new Record axiom, the form by the det character). Not a value derivation; the source/action coupling is a separate residual.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not re-cite, edit, or promote any existing dependent row.
**Runner:** `scripts/flavor_logdet_form_under_record_axiom_2026_06_04.py` (SCORECARD 6/6).
**Depends:** `minimal_axioms` (the Record axiom, `docs/MINIMAL_AXIOMS_2026-06-04.md`) for finite scalar record additivity.

## Statement
Let an observable generator `W` be (i) a finite scalar record functional additive over disjoint
collections — the **Record axiom** — and (ii) built from a multiplicative character on the local
operator algebra. Then the FORM is fixed:

> **W = c · log|det|**,  with the scale `c` set by the additive-baseline convention.

## Why — the two factors
- **Multiplicative-character factor (det).** `det` is a multiplicative character: `det(AB)=det(A)det(B)`
  (verified; `Tr` is not). The multiplicative-character family is exactly `det^k` (verified for several
  `k`), and `det` is multiplicative over a **direct sum** of disjoint blocks: `det(A⊕B)=det(A)det(B)`.
- **Additivity factor (the Record axiom).** Over disjoint blocks, `|det|^p` *multiplies* for every `p`
  (verified), and **only** the `p→0` image `log|det|` is **additive**: `log|det(A⊕B)| =
  log|det A| + log|det B|` (verified over 2 and 3 disjoint blocks). The Record axiom *is* this
  additivity, so it selects `log|det|` out of the `|det|^p` family. The residual scale `c` is the
  axiom's explicit additive-baseline convention.

Equivalently, `log|det H| = Σ_modes log|λ_mode|` (verified) — the additive functional over the disjoint
spectral/record mode decomposition.

## What this closes, and what it does not
- **Closes (FORM):** the additive + multiplicative-character factors of the `log|det|` generator FORM.
  The additivity half — previously the open/no-go content (`observable_principle_p1_exponent_fixing`
  proved it underivable from below; `observable_principle_p1_bridge_extensivity_primitive`'s two-slope
  hole) — is now supplied axiomatically by Record. The det-character half is the multiplicative-form
  factor.
- **Does not close (VALUE / coupling):** the **source/action coupling** `D+J` and its local derivative
  algebra `dW/dj_x = Re Tr[(D+J)^{-1} P_x]` is a *separate* factor the Record axiom explicitly does not
  supply, and remains the residual for the log-det-dependent rows (companion provenance note). The Koide
  **value** (the within-C³ weight) is likewise untouched — Record excludes Born weights and `AC_φλ`.

## Relation to the active dependency-rewrite audit
The 2026-06-04 dependency audit (`RECORD_P1_DEPENDENCY_AUDIT_NOTE`) found that all 91 direct dependents
of the old observable-principle parent need broader content than additivity (0 rewrite / 0 split / 91
leave), with the **log-det generator the dominant blocker (59 rows)**. This note is **complementary and
non-overlapping**: it does not re-cite or move any of those rows (that surface is owned by the audit and
the independent audit lane); it supplies the *positive* form theorem — that the additivity factor of the
`log|det|` form is now axiom-closed — which the companion provenance note uses to reduce the 59-row
blocker to its precise residual.

## Provenance (verified 2026-06-04)
- `det` multiplicative / `Tr` not; `det^k` family; `det(A⊕B)=det(A)det(B)`; `|det|^p` multiplicative for
  all `p` while only `log|det|` additive; additivity over 3 disjoint blocks; `log|det H| = Σ log|λ|`:
  verified directly (runner 6/6).
- This note sets no audit status; it states the form theorem and its precise scope.
