# Claim Status Certificate — Cluster-Decomposition Block 02 (real operator-theoretic redo)

## Cycle metadata

- **slug**: cluster-decomposition-block02-real-2026-05-19
- **branch**: physics-loop/cluster-decomp-delta-t-real-proof-2026-05-19
- **base**: origin/main
- **note**: docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md
- **runner**: scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py
- **cache**: logs/runner-cache/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.txt
- **parent row**: docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md (candidate 2)
- **redo of**: closed PR #1531 (the 4×4 finite-dim toy was rejected as not applicable to continuous SU(3) link variables)

## Status fields

```yaml
goal: real operator-theoretic proof of Δ_T > 0 finite-Λ on canonical SU(3) staggered+Wilson
target_claim_type: bounded_theorem
actual_current_surface_status: candidate-bounded-theorem-grade
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  Operator-theoretic proof from primitives (heat-kernel positivity,
  trace-class via character expansion, abstract spectral-gap lemma proved
  inline) composed with retained framework Leg A (det(D+m) > 0).
  Runner verifies on actual SU(3) integral operator (heat-kernel mesh on
  maximal torus, character-series convergence, single-link spectrum,
  2-site truncated-character-basis spectrum, sampled Leg A determinant
  positivity).
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## V1-V5 Promotion Value Gate

| # | Question | Pass/Fail |
|---|----------|-----------|
| V1 | Specific obstruction closed? | PASS — parent row's candidate 2 (Perron-Frobenius for transfer matrix) on finite Λ, now with the actual operator-theoretic content rather than a 4×4 toy |
| V2 | New derivation? | PASS — abstract operator-theoretic spectral-gap theorem proved inline from spectral-theorem primitives (no Krein-Rutman black box), composed with retained Leg A det(D+m)>0 to extend the gap to staggered+Wilson on finite Λ |
| V3 | Could audit lane already do this? | PASS — the abstract operator-theoretic spectral-gap theorem proved inline plus its composition with retained Leg A is new framework-specific content; audit lane has not previously packaged this composition |
| V4 | Non-trivial? | PASS — the heat-kernel strict-positivity proof, trace-class derivation via character series, and §5 spectral-gap theorem from primitives constitute genuine operator-theoretic content; the runner exhibits each step on the ACTUAL SU(3) integral operator |
| V5 | One-step variant of prior cycle? | PASS — different mechanism from closed PR #1531; that PR exhibited Perron-Frobenius on a 4×4 toy, this PR exhibits operator-theoretic content on L²(SU(3)^E) |

All five gate questions pass.

## Runner result

```
PASS=8  FAIL=0  (runtime: ~1.2 s)
```

8 verifications on the actual SU(3) integral operator on L²(SU(3)^|E(Λ)|, dU_Haar):

| # | Verification | Status |
|---|----|----|
| V1 | K_τ > 0 strictly on SU(3) maximal torus | PASS |
| V2 | Character-series trace-norm converges | PASS |
| V3 | K_τ is a probability kernel (∫ K_τ = 1) | PASS |
| V4 | Single-link operator simple top + strict gap | PASS |
| V5 | Heat-equation consistency | PASS |
| V6 | 2-site Λ truncated transfer strict gap | PASS |
| V7 | Leg A det(D + m I) > 0 sampled on SU(3) | PASS |
| V8 | Composition T_W · det(D+mI) > 0 pointwise | PASS |

## Honest scope (read-first)

- **Finite Λ only.** No thermodynamic limit. No uniformity-in-Λ. NOT the Yang-Mills mass gap.
- **Status authority:** independent audit lane only. The source note's `bounded_theorem` label is a source-side claim-boundary declaration; effective status is the audit lane's call.
- **Leg A is retained input.** `det(D + m I) > 0` cited from `docs/STRONG_CP_THETA_ZERO_NOTE.md`; not re-derived here.

## Dependencies

- (D1) Retained Leg A from `docs/STRONG_CP_THETA_ZERO_NOTE.md` (effective retained)
- (D2) Spectral theorem for compact self-adjoint operators (functional analysis primitives — invoked, not cited as authority)
- (D3) Parabolic strong maximum principle on connected manifolds (basic PDE — invoked, not cited as authority)

## Target for parent row

Replaces the parent's "Δ_T > 0 admitted on a SU(3) integral operator" with "Δ_T > 0 closed on finite Λ via this source note + retained Leg A composition", subject to audit-lane ratification. Composing with the retained bridge note `CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09` gives a closed finite-Λ temporal clustering theorem for the canonical staggered + Wilson Hamiltonian.

## Out-of-scope anti-overclaim list (from source note §8)

- X1: Thermodynamic limit `Λ → Z³` — open
- X2: Uniformity in Λ — open
- X3: Yang-Mills mass gap (Clay) — out of scope (continuum, infinite-volume problem)
- X4: Gauge-invariant restriction — automatic from commutation (handled in §8)
- X5: Continuum limit `a → 0` — open
- X6: Spatial cluster decomposition — open (requires separate retained argument)
- X7: Permanently retained — no; source-side label is bounded_theorem and effective status is the audit lane's call
