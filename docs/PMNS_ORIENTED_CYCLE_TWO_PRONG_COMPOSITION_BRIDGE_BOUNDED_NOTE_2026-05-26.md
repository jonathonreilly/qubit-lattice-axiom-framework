# PMNS Oriented-Cycle Two-Prong Composition Bridge

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/pmns_oriented_cycle_two_prong_composition_runner.py`](../scripts/pmns_oriented_cycle_two_prong_composition_runner.py)

## Claim

Given two existing sibling narrow theorems — the **graph-first
residual antiunitary** narrow theorem (which derives
`A_fwd = P_23 A_fwd^dagger P_23` on the oriented forward-cycle channel
from retained one-hop authorities) and the **sole-axiom free-point
identity-block** narrow theorem (which derives `A_act = I_3` at the
sole-axiom free point of the active-operator construction) — the two
"admitted premises / open class-D bridge targets" of the parent
`PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md`
are **simultaneously closed** by composition: the residual antiunitary
condition follows from the graph-first sibling, and the free-point
identity-block follows from the sole-axiom sibling. The parent's
remaining content (cyclic covariance, zero cycle coefficients on
`I_3`, prescribed swap-conjugation fixed-family / non-fixed examples)
is then class-A algebra on the cited sibling authorities.

The proof-walk uses only:

1. The **antiunitary sibling** narrow theorem — its retained-grade
   conclusion `A_fwd = P_23 A_fwd^dagger P_23` is consumed directly as
   the closed form of the first auditor-flagged premise (graph-first
   residual antiunitary on the oriented forward-cycle channel).
2. The **free-point sibling** narrow theorem — its conclusion
   `A_act((1,1,1), (0,0,0), delta) = I_3` at the sole-axiom free point closes the
   second auditor-flagged premise (sole-axiom free-point active
   block = `I_3`).
3. Standard linear algebra on `3x3` matrices to verify that, with
   both premises now supplied by audited sibling content, the parent's matrix identities
   hold as algebraic consequences (already class-A in the parent
   verdict).

The bridge introduces **no new admissions**. Both sibling narrow
theorems were filed exactly to discharge the two clauses of the
auditor's `missing_bridge_theorem` hint on the parent; this bridge
explicitly composes them via markdown-link citation so the audit graph
records the two-prong closure as a single bounded composition candidate.

This is a bounded proof-walk satisfying the auditor's explicit
`missing_bridge_theorem` repair on
`PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md`
(`notes_for_re_audit_if_any`: "add retained bridge theorems proving
the sole-axiom free-point active block is I3 and the graph-first
selected-axis route induces the P23 swap-conjugation antiunitary").

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | On the graph-first selected-axis route, `A_fwd = P_23 A_fwd^dagger P_23` (residual antiunitary condition on the oriented forward-cycle channel `A_fwd = c_1 E_12 + c_2 E_23 + c_3 E_31`) | Retained antiunitary sibling narrow theorem |
| (B2) | For the displayed active-operator construction at the specified input, `A_act((1,1,1), (0,0,0), delta) = I_3` | Free-point sibling's bounded finite-matrix identity |
| (B3) | The parent's "admitted premise" set `{(B1), (B2)}` is now supplied by the cited sibling authorities; the parent's class-A matrix identities (cyclic covariance, zero cycle coefficients on `I_3`, prescribed swap-conjugation examples) hold by direct algebra | (B1) + (B2) + standard linear algebra |

The proof-walk does not cite the Wilson plaquette action, staggered
phases, Brillouin-zone labels, link unitaries, lattice scale `u_0`, a
Monte Carlo measurement, or a fitted observational value. The "open
class-D" bridges in the parent are now closed via the cited sibling
content alone.

## Exact arithmetic check

Sibling theorem (B1) consumed: `P_23 = [[1,0,0],[0,0,1],[0,1,0]]`,
`A_fwd = c_1 E_12 + c_2 E_23 + c_3 E_31`, and direct calculation of
`P_23 A_fwd^dagger P_23` shows it equals
`bar{c_3} E_12 + bar{c_2} E_23 + bar{c_1} E_31`. The antiunitary
condition `A_fwd = P_23 A_fwd^dagger P_23` then reads
`(c_1, c_2, c_3) = (bar{c_3}, bar{c_2}, bar{c_1})`, i.e. the
orientation-reversed conjugate. This is the antiunitary half closed
by retained content.

Sibling theorem (B2) consumed: the active-operator construction
`A_act(x, y, delta) = diag(x_1, x_2, x_3) + diag(y_1, y_2, y_3 e^{i delta}) C`
with `C` the canonical forward-cycle matrix
`[[0,1,0],[0,0,1],[1,0,0]]`. At the sole-axiom free point
`(x, y) = ((1,1,1), (0,0,0))`, for every `delta`:

```text
A_act((1,1,1), (0,0,0), delta) = I_3.
```

The runner reconstructs this active-operator point directly, so the
free-point clause is not a new admission in this bridge.

Cyclic-covariance + zero-cycle-coefficient + swap-conjugation
examples on `I_3` (the parent's class-A content) are then standard
`3 x 3` matrix arithmetic.

## Dependencies

- [`PMNS_GRAPH_FIRST_RESIDUAL_ANTIUNITARY_NARROW_THEOREM_NOTE_2026-05-16.md`](PMNS_GRAPH_FIRST_RESIDUAL_ANTIUNITARY_NARROW_THEOREM_NOTE_2026-05-16.md)
  — retained narrow theorem supplying the graph-first residual
  antiunitary condition (`A_fwd = P_23 A_fwd^dagger P_23`).
- [`PMNS_SOLE_AXIOM_FREE_POINT_IDENTITY_BLOCK_NARROW_THEOREM_NOTE_2026-05-16.md`](PMNS_SOLE_AXIOM_FREE_POINT_IDENTITY_BLOCK_NARROW_THEOREM_NOTE_2026-05-16.md)
  — audited-decoration sibling narrow theorem supplying the
  sole-axiom free-point active block `A_act = I_3`.
- [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — bounded algebraic coordinate-extraction lemma for a supplied `3 x 3`
  block. It supplies no physical carrier, Record-compatible readout, or
  retained decoration anchor.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Target Context

The parent target is `PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md`.
It is named here as the downstream row whose two-prong bridge repair is
being supplied; it is not an upstream authority for this bridge.

## Boundaries

This bridge does **not** close:

- the broader PMNS physical-spectrum derivation (downstream of the
  oriented-cycle structure parent, separate question);
- the open `dm_leptogenesis` selector lane;
- the physical-species interpretation of the cycle-channel structure;
- any continuum-limit numerical claim.

Downstream rows needing the oriented-cycle selection structure with
both premises supplied by audited sibling content (not just retained-admitted) can now
cite this composition bridge directly. The bridge does not modify the
parent's class-A matrix identities — those remain as the parent
states them.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/pmns_oriented_cycle_two_prong_composition_runner.py
```

Expected:

```text
TOTAL: PASS=6 FAIL=0
VERDICT: bounded bridge passes; both auditor-flagged premises
(antiunitary + free-point I_3) close via cited sibling narrow
theorems, satisfying the parent's two-prong missing_bridge_theorem
hint.
```
