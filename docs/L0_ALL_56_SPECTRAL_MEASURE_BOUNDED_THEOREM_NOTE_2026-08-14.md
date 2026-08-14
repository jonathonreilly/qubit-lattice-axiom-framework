---
claim_id: l0_all_56_spectral_measure_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "All 64 six-neighbor occupancy cells: 8 have n=0 and 56 are nonzero, splitting as 24+24+8 for k=|3n|^2 in {1,2,3}. For every nonzero cell the projectors P±=(√k I±H)/(2√k) are complementary and Tr(ρP+)+Tr(ρP−)=1 with ρ=(I+H/3)/2. Sample traces equal (3±√k)/6. Not Born, not a unique member, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l0_all_56_spectral_measure_2026_08_14.py
---

# `L0` Spectral Measure On All 56 Nonzero Cells

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `Q(√k)` PVM identities on every nonzero 6-NN
occupancy. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/l0_all_56_spectral_measure_2026_08_14.py`](../scripts/l0_all_56_spectral_measure_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Six occupancy bits give 64 cells. Each axis is balanced when
`c_{+μ}=c_{-μ}`, so `n=0` on 8 cells and nonzero on 56. Those
split as `24+24+8` for `k=|3n|^2∈{1,2,3}`.

For every nonzero cell, `H=aσ_x+bσ_y+cσ_z` with
`a,b,c∈{−1,0,1}` and

```text
P± = (√k I ± H) / (2√k),    ρ = (I + H/3)/2.
```

The runner checks `P++P−=I`, `P+P−=0`, and
`Tr(ρP+)+Tr(ρP−)=1` on all 56, and the sample traces
`(3±√k)/6` on one cell of each `k`.

This is a measure on every cell, not two displayed directions.
Not Born. Not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact complementary PVM on all 56 nonzero 6-NN cells."
trace_class: frontier_discovery
target_claim_id: l0_all_56_spectral_measure
target_blocker_text: "specpv only displayed two directions"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for all 56 nonzero occupancy cells"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name the 56-cell measure.

## Theorem 1 — census

64 cells, 8 with `n=0`, 56 nonzero: `24+24+8` for `k=1,2,3`.

## Theorem 2 — complementary PVM

On every nonzero cell, `P++P−=I` and `P+P−=0`.

## Theorem 3 — traces sum to 1

`Tr(ρP+)+Tr(ρP−)=1` on every nonzero cell. Sample cells
match `(3±√k)/6`.

## Theorem 4 — not a TOE

Quoted Qubit and Admissibility do not name the 56 cells.
Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “nonzero count is not 56” must fail.
2. Predicate “some cell has `P+P−≠0`” must fail.
3. Predicate “note adopts Born” must fail.

Identity gates: `cells`, `projectors`, `trace_sum`.

## Honest-auditor / Boundary

Finite Pauli algebra over `Q(√k)` on 56 cells. This note
authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Born derivation.
- Qubit remains `M_2(C)`.
