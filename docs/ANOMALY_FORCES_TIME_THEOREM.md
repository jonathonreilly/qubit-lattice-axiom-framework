# Anomaly-Cancellation Consistency Bridge for 3+1 Spacetime

**Date:** 2026-04-24; current-surface repair 2026-05-30
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Current status:** action-surface positive theorem candidate. The theorem
closes `d_t = 1` using the framework-action ABJ derivation and the
single-clock codimension-1 evolution surface. It is not audit-retained until
the independent audit lane reviews this note and its non-ABJ dependencies.
**Primary runner:**
[`scripts/frontier_anomaly_forces_time_action_abj_closure.py`](../scripts/frontier_anomaly_forces_time_action_abj_closure.py)
**Legacy runner:** `scripts/frontier_anomaly_forces_time.py`

## Repair Summary

The older version of this note said that admission (i), the
Adler-Bell-Jackiw anomaly-to-inconsistency implication, had no successor route
after the earlier lattice Wess-Zumino/Fujikawa attempt closed without merge.
That is no longer the current repo surface.

The current surface is:

1. The ABJ implication is now routed through the framework-action theorem
   in
   [`ABJ_FROM_FRAMEWORK_ACTION_U1_CUBIC_THEOREM_NOTE_2026-05-30.md`](ABJ_FROM_FRAMEWORK_ACTION_U1_CUBIC_THEOREM_NOTE_2026-05-30.md).
   That theorem derives the U(1)^3 ABJ obstruction directly from the local
   physical 3+1 framework action: action Dirac operator, heat-kernel spin
   trace, exact `Tr_LH[Y^3] = -16/9`, and the 3+1 abelian no-counterterm
   enumeration.
2. The pure Clifford parity step is audit-ratified separately in
   [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md):
   a chirality operator anticommuting with all spacetime Clifford generators
   exists only in even total dimension. With `d_s = 3`, this is exactly the
   odd-time condition.
3. The one-clock exclusion of multi-time `d_t > 1` is carried by
   [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md).
4. The late-May finite-even-torus `epsilon` index route remains a useful
   negative boundary, but it is no longer the active ABJ route. That route
   cannot witness a nonzero index; the exact square-block no-go is recorded in
   [`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md`](ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md).

In the legacy admission numbering, admission (i) was the ABJ
anomaly-to-inconsistency premise and admission (iv) was the single-clock
codimension-1 exclusion of `d_t > 1`. This repair replaces the admission-(i)
load-bearing step with the action-surface ABJ theorem above.

This is therefore a repair from "stale bare admission" to "framework-action
positive composition." The ABJ step is no longer bounded by an admitted or
cited theorem import.

## Theorem

Assume the framework's retained/bounded matter-content surface supplies the
left-handed chiral gauge content

```text
(2, 3)_{+1/3} + (2, 1)_{-1}
```

on the `Z^3` spatial substrate, and use the framework-action ABJ theorem:

```text
Framework-action U(1)^3 ABJ anomaly-to-inconsistency:
  a chiral gauge theory with non-zero perturbative gauge anomaly traces
  does not close as a unitary quantum gauge theory unless the anomalies are
  cancelled by the completed chiral matter content.
```

Then:

1. The left-handed content has non-zero anomaly traces:

   ```text
   Tr[Y^3]       = -16/9
   Tr[SU(3)^2 Y] =  1/3
   Tr[SU(3)^3]   =  2
   ```

2. By the framework-action ABJ theorem, gauge consistency requires an
   opposite-chirality completion.
3. Opposite chirality requires a chirality operator on the carrying spacetime
   Clifford representation.
4. The retained Clifford volume theorem forces total spacetime dimension
   `d = d_s + d_t` to be even when such chirality exists.
5. Since the spatial substrate is `d_s = 3`, chirality forces

   ```text
   d_t in {1, 3, 5, ...}.
   ```

6. The single-clock codimension-1 evolution theorem excludes `d_t > 1`.
7. Therefore the only allowed time count on this framework-action positive
   surface is

   ```text
   d_t = 1,
   ```

   so the spacetime signature is `(3,1)`.

## Proof

### 1. Anomaly arithmetic

For the left-handed matter content, the multiplicities are:

```text
Q_L: 2 weak states x 3 colours = 6 states with Y = +1/3
L_L: 2 weak states x 1 colour  = 2 states with Y = -1
```

The exact rational traces are:

```text
Tr[Y]       = 6*(1/3) + 2*(-1)       = 0
Tr[Y^3]     = 6*(1/3)^3 + 2*(-1)^3   = -16/9
Tr[SU(3)^2Y]= 2*(1/2)*(1/3)          = 1/3
Tr[SU(2)^2Y]= 3*(1/2)*(1/3) + (1/2)*(-1) = 0
Tr[SU(3)^3] = 2
```

The cubic U(1)^3 trace is already sufficient for the ABJ obstruction derived
from the framework action. The mixed and nonabelian traces are retained as
parallel consistency checks of the same left-handed matter surface.

### 2. ABJ from the framework action and chiral completion

The framework-action ABJ theorem cited above derives the U(1)^3 chiral gauge
anomaly from the physical 3+1 local action. Its runner verifies the
Wick-rotated local gamma algebra, nonzero heat-kernel spin trace, Gaussian
coefficient, `Tr_LH[Y^3] = -16/9`, and the absence of a 3+1 abelian local
counterterm whose BRST variation cancels `c F wedge F`.

The present theorem therefore does not use an ABJ admitted packet or standard
theorem import. On the framework action, the non-zero anomaly trace is not
optional; consistency requires chiral completion.

### 3. Chirality parity

The Clifford volume theorem proves the algebraic parity statement:

```text
gamma_5 exists with gamma_5^2 = I and {gamma_5, gamma_mu} = 0 for all mu
  iff total spacetime dimension d is even.
```

With `d = d_s + d_t` and `d_s = 3`, this means `d_t` is odd.

### 4. Single-clock exclusion

The single-clock codimension-1 theorem supplies one Hamiltonian clock and one
codimension-1 initial surface for arbitrary admissible local data. Multi-time
continuum theories with `d_t > 1` require nonlocal compatibility constraints
on such data. Those constraints are incompatible with the graph-local
arbitrary-data surface. Therefore `d_t > 1` is excluded on the single-clock
surface.

### 5. Intersection

The ABJ/chirality half gives:

```text
d_t in {1, 3, 5, ...}.
```

The single-clock half gives:

```text
d_t <= 1.
```

Physical time evolution requires `d_t >= 1`. The intersection is exactly:

```text
d_t = 1.
```

## Claim Boundary

This note closes the 3+1 spacetime bridge on the current framework-action
surface:

```text
ABJ from framework action + chiral matter surface + retained Clifford parity
+ single-clock codimension-1 evolution -> d_t = 1.
```

It does **not** close:

- independent audit of this new action-surface ABJ theorem;
- independent audit of the staggered-Dirac/action realization gate;
- independent audit of the physical hypercharge/matter-surface chain;
- the audit of the single-clock theorem or any audit-pending upstream source;
- a route in which observed spacetime dimension is used as an input.

It also does not use PDG values, continuum dimensional fitting, the Wilson
plaquette, `alpha_LM`, Yukawa data, Planck data, or Monte Carlo measurements.

## Audit Handoff

```yaml
proposed_claim_type: positive_theorem
actual_current_surface_status: action-surface positive theorem candidate
framework_action_abj_theorem:
  id: ABJ from framework action U(1)^3 cubic theorem
  route: docs/ABJ_FROM_FRAMEWORK_ACTION_U1_CUBIC_THEOREM_NOTE_2026-05-30.md
abj_import_retired_on_framework_action_surface: true
standard_theorem_bridge_load_bearing: false
accepted_premise_packet_load_bearing: false
framework_native_abj_derivation_closed: true
unbounded_positive_theorem_allowed: true
why_not_effective_retained_before_audit: >
  The source note now proposes a positive theorem rather than a bounded
  ABJ-import composition. Effective retained status still requires independent
  audit of this note and the non-ABJ dependencies, including the action
  realization/matter surface and single-clock theorem.
audit_required_before_effective_status_change: true
```

The requested audit question is narrow: whether this repaired parent note is
now a clean action-surface positive theorem for `d_t = 1`, with the ABJ import
retired and all remaining non-ABJ blockers named explicitly.
