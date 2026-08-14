---
claim_id: l0_spectral_projectors_k2_k3_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "For L0 occupancies with two or three unbalanced axes, n has k=|3n|^2 in {2,3}. The unique rank-1 spectral projectors of ρ=(I+n·σ)/2 are constructed over Q(√k) as P±=(√k I ± H)/(2√k) with H=aσx+bσy+cσz. They are complementary, idempotent, and Tr(ρ P±)=(3±√k)/6. This makes the comparator a probability measure on those projectors, not a k-label. Not Born, not a unique member, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l0_spectral_projectors_k2_k3_2026_08_14.py
---

# `L0` Spectral Projectors For `k=2` And `k=3`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `Q(√2)` and `Q(√3)` projector identities for the
displayed `L0` comparator. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/l0_spectral_projectors_k2_k3_2026_08_14.py`](../scripts/l0_spectral_projectors_k2_k3_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `n = (a,b,c)/3` with `a,b,c ∈ {−1,0,1}` not all zero and
`k = a^2+b^2+c^2 ∈ {1,2,3}`. Let `H = a σ_x + b σ_y + c σ_z`.
Then `H^2 = k I` and the spectral projectors of
`ρ = (I + n·σ)/2` are

```text
P_± = (√k I ± H) / (2 √k).
```

The runner builds these over `Q(√k)` for a `k=2` occupancy
`(+x,+y)` and a `k=3` occupancy `(+x,+y,+z)`. It checks
`P_+ + P_- = I`, `P_+ P_- = 0`, `P_±^2 = P_±`, and
`Tr(ρ P_±) = (3 ± √k)/6`.

That is a probability measure on two rank-1 projectors. It is not
Born, not a unique member, and not axiom text.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Q(√k) identities construct the L0 spectral PVM for k=2,3."
trace_class: frontier_discovery
target_claim_id: l0_spectral_projectors_k2_k3
target_blocker_text: "k-label is not a measure"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for displayed k=2,3 occupancies"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name `P_±` or `√k`.

## Theorem 1 — `H^2 = k I`

For `(a,b,c) = (1,1,0)` one has `k=2`. For `(1,1,1)` one has `k=3`.
Pauli products give `H^2 = k I` exactly.

## Theorem 2 — complementary projectors

`(√k I + H)(√k I − H) = k I − H^2 = 0`, so `P_+ P_- = 0`.
`P_+ + P_- = I`.

## Theorem 3 — Born-form traces without adopting Born

`Tr(ρ P_±) = (3 ± √k)/6`. Sum is `1`. Both are positive.

## Theorem 4 — not a TOE

The projectors are the instrument of a displayed comparator.
Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “`P_+ P_- ≠ 0`” must fail.
2. Predicate “`Tr(ρ P_+) + Tr(ρ P_-) ≠ 1`” must fail.
3. Predicate “note adopts Born” must fail.

Identity gates: `pauli_H(a,b,c)`, `projectors(a,b,c)`, `trace_rho_p(a,b,c)`.

## Honest-auditor / Boundary

Finite Pauli algebra over `Q(√2)` and `Q(√3)`. This note authors no
audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Born derivation.
- Qubit remains `M_2(C)`.
