# Flavor J-Hunt Round 5: Corrected Central-State Boundary

**Date:** 2026-06-02; repaired 2026-06-06
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support source repair; independent
audit owns any effective status movement.
**Claim boundary:** finite `C3` central-state algebra only. The packet proves
that the equal-central-block state is admissible and `C3`-compatible, and that
it is not the continuous `U(1)_b` rephasing obstruction. It does not force that
state, derive the physical `Q=2/3` readout, or derive a trace default from
framework baseline axioms.
**Runner:** `scripts/flavor_find_J_round5_trace_vs_center_state_2026_06_02.py`
(SCORECARD PASS=10 FAIL=0).
**Cached runner output:**
`logs/runner-cache/flavor_find_J_round5_trace_vs_center_state_2026_06_02.txt`
**Runner JSON:**
`outputs/flavor_find_J_round5_trace_vs_center_state_2026_06_02.json`

## Repair Summary

The prior version made one false algebraic move: it treated

```text
E_old(A) = e0 A e0 + e1 A e1
```

as a conditional expectation onto the center. That is not true for a general
`3x3` operator. It is only block compression. The repaired runner includes an
explicit counterexample for which `E_old(A)` still fails to commute with the
`C3` generator. On elements already in `R[C3]`, the same map is just the
identity, so it cannot create an equal-central-block state from the group
algebra.

The corrected finite packet separates three operations:

- block compression: `A -> e0 A e0 + e1 A e1`;
- `C3` conjugation averaging: `A -> (A + C A C^-1 + C^2 A C^-2)/3`, which
  lands in the `C3` commutant but does not select state weights;
- center-valued block averaging:
  `A -> tau0(e0 A e0) e0 + tau1(e1 A e1) e1`, where `taui` is the normalized
  block trace.

## Closed Finite Algebra

Let `C` be the real cyclic shift and

```text
e0 = (I + C + C^2)/3,       e1 = I - e0.
```

The runner verifies that `e0,e1` are orthogonal central idempotents with ranks
`1` and `2`.

There is a one-parameter central-state simplex

```text
rho_p = p e0/Tr(e0) + (1-p) e1/Tr(e1),      0 <= p <= 1.
```

Every `rho_p` is positive, trace-one, and commutes with `C`. Two special
points are:

| state | central block masses |
| --- | --- |
| normalized trace `I/3` | `(1/3, 2/3)` |
| equal-central-block state | `(1/2, 1/2)` |

The equal-block state is therefore an admissible `C3`-compatible state. It is
not a continuous `C -> exp(i alpha) C` rephasing and does not violate `C^3=I`.
This preserves the useful round-5 science: the residual is not the old
`U(1)_b` wall.

## Boundary

The same finite algebra also proves the missing-selection point: `C3`
central-state admissibility alone does not choose `p=1/2`, `p=1/3`, or any
other central-block weight. The displayed local readout convention

```text
Q(r) = 1/3 + (2/3) r
```

still maps `r=1` to `Q=1` and `r=1/2` to `Q=2/3`, but this packet treats that
as a displayed convention, not as a derived physical readout theorem.

Accordingly, this repaired row should not be read as a retained derivation of
the charged-lepton value. Its bounded contribution is sharper:

> The non-tracial equal-central-block state is finite-algebraically admissible
> and `C3`-compatible, but its selection over the trace remains an independent
> state/readout/dynamics gate.

## Audit Repair Target

This source repair responds to the failed audit's algebraic blocker by
replacing the invalid `E_old` step with a correct center-valued/state-simplex
derivation. It also removes load-bearing claims that this restricted packet
derives the trace reference state, the Frobenius beta-family, the physical
`Q(r)` normalization, or the prior `U(1)_b` obstruction from one-hop retained
authorities.

No `docs/audit/**` status is updated by this packet. No new axiom is
introduced.
