# Claim Status Certificate

## Cycle metadata

- **slug**: wilson-action-surface-selector-real-positive-2026-05-25
- **branch**: physics-loop/wilson-action-surface-selector-real-positive-theorem-2026-05-25
- **base**: origin/main
- **note**: docs/WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md
- **runner**: scripts/frontier_wilson_action_surface_selector_real_positive_2026_05_25.py

## Status fields

```yaml
goal: derive Wilson action-surface selector real-positive form from primitives
target_claim_type: bounded_theorem
actual_current_surface_status: candidate-bounded-theorem-grade
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  Single-plaquette gauge-invariant scalar action functional uniqueness
  proof from retained primitives (Cl(3)⊗Z³ + canonical normalization
  via g_bare_rescaling_freedom_removal). P4 real-action constraint
  excludes imaginary-plaquette term at the action-functional level
  (not just dynamically). Runner exhibits the construction + rejection
  on actual SU(3) configurations. Discharges one of two missing bridge
  theorems flagged by Leg A clearance audit verdict.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependencies (one hop, declared)

| Authority | Audit-lane status | Role |
|---|---|---|
| [`docs/G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](../../../docs/G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) | retained | canonical normalization rigidity: `β = 2 N_c / g_bare² = 6` at canonical `Tr(T_a T_b) = δ_ab/2` |

Cl(3) and Z³ are framework axioms (A1)+(A2).

(P4), (P5) are standard QFT path-integral well-definedness conventions, named explicitly as conventions and **not** as new axioms or derived theorems.

## What this PR discharges

The judicial-panel audit verdict on `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19` (2026-05-25, `audited_conditional`) named **two** missing bridges:

1. **Real-positive Wilson action-surface selector** — discharged by this PR.
2. **Scalar-mass-only / positive-orientation boundary** — OUT OF SCOPE (overlaps with active in-flight RP / Case A determinant-positivity work by others).

## V1-V5 promotion value gate

| # | Question | Pass/Fail |
|---|----------|-----------|
| V1 | Closes/sharpens the first of two missing bridges from the Leg A judicial-panel verdict (real-positive Wilson action-surface selector derived from primitives) | PASS |
| V2 | New synthesis: Lemma 1 (gauge-inv reduction) + Lemma 2 (P4 reduction) + Lemma 3 (canonical-normalization match via R1) + Lemma 4 (action-functional-level iθ exclusion) — full uniqueness statement not in the audit-graph | PASS |
| V3 | Audit lane recognized the gap explicitly ("provide retained derivation of the real-positive Wilson action-surface selector") | PASS |
| V4 | Eight-route runner verification: gauge-inv enumeration, real-action exclusion (numeric+symbolic), continuum limit (sympy+numpy), bounded-below check, uniqueness enumeration across 8 candidate ansatzes, F~F-proxy rejection, retained-primitive composition. Substantive. | PASS |
| V5 | Different from 2026-05-19 parent (which TREATED the surface as admitted premise); different from 2026-05-16 no-go (which proved RP-half-alone cannot forbid CP-odd); different from in-flight RP / Case A work (which is the SECOND missing bridge, not this one). | PASS |

All five gate questions pass.

## Open imports

None new. The proof composes:
- (A1) Cl(3) algebra (framework axiom)
- (A2) Z³ substrate (framework axiom)
- (R1) retained canonical-normalization primitive
- (P4), (P5) standard QFT path-integral conventions (named explicitly)

## Forbidden-import discipline

- No external citations (Wilson 1974, Vafa-Witten, Leutwyler-Smilga, Osterwalder-Schrader) used as proof inputs.
- No SecondMissingBridge work consumed (scalar-mass-only / positive-orientation, in-flight RP / Case A).
- No PDG values consumed.
- No fitted selectors consumed.
- No same-surface family arguments.

## Review-loop disposition

`pass` (self-review). Independent audit-lane ratification still required. The note explicitly says so.

## What this cycle does NOT claim

- Does NOT derive canonical normalization `β = 6` from primitives (uses retained R1 primitive as input).
- Does NOT derive (P4) real-action or (P5) bounded-below conventions from Cl(3)⊗Z³ axioms; they are standard QFT path-integral conventions named explicitly as such.
- Does NOT extend to higher-loop functionals (clover, multi-plaquette, axion-coupled).
- Does NOT solve strong CP; the second missing bridge (scalar-mass-only / positive-orientation) is out of scope.
- Does NOT promote parent row `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19` beyond `audited_conditional`; whether the parent row upgrades is the audit lane's call.
