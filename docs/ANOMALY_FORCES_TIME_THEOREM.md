# Anomaly-Cancellation Consistency Bridge for 3+1 Spacetime

**Date:** 2026-04-24; current-surface repair 2026-05-30
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Current status:** standard-theorem bounded composition. The theorem closes
`d_t = 1` on the cited ABJ standard-theorem bridge and the single-clock
codimension-1 evolution surface. It is not an unbounded positive theorem from
A1+A2 alone.
**Primary runner:**
[`scripts/frontier_anomaly_forces_time_standard_abj_closure.py`](../scripts/frontier_anomaly_forces_time_standard_abj_closure.py)
**Legacy runner:** `scripts/frontier_anomaly_forces_time.py`

## Repair Summary

The older version of this note said that admission (i), the
Adler-Bell-Jackiw anomaly-to-inconsistency implication, had no successor route
after the earlier lattice Wess-Zumino/Fujikawa attempt closed without merge.
That is no longer the current repo surface.

The current surface is:

1. The ABJ implication is now routed through the cited standard-theorem bridge
   in
   [`ABJ_STANDARD_THEOREM_BRIDGE_FOR_ANOMALY_FORCES_TIME_NOTE_2026-05-30.md`](ABJ_STANDARD_THEOREM_BRIDGE_FOR_ANOMALY_FORCES_TIME_NOTE_2026-05-30.md).
   That bridge treats ABJ/Wess-Zumino/Fujikawa as a standard theorem of
   chiral gauge QFT, cites the primary theorem sources, and verifies in repo
   that the framework's left-handed matter content has nonzero perturbative
   anomaly traces.
2. The pure Clifford parity step is audit-ratified separately in
   [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md):
   a chirality operator anticommuting with all spacetime Clifford generators
   exists only in even total dimension. With `d_s = 3`, this is exactly the
   odd-time condition.
3. The one-clock exclusion of multi-time `d_t > 1` is carried by
   [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md).
4. The late-May U(1) Fujikawa/Jacobian work narrows the route toward
   fully framework-native ABJ closure but does not retire the standard theorem
   dependency. The current residual is that the standard finite even-torus
   staggered `epsilon` index cannot witness the needed nonzero index; the
   exact square-block no-go is recorded in
   [`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md`](ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md).

In the legacy admission numbering, admission (i) was the ABJ
anomaly-to-inconsistency premise and admission (iv) was the single-clock
codimension-1 exclusion of `d_t > 1`. This repair replaces the admission-(i)
load-bearing step with a cited standard-theorem bridge plus explicit
framework hypothesis checks.

This is therefore a repair from "stale bare admission" to "standard-theorem
bounded composition." It is a positive closure on that bounded surface; it is
not an unbounded A1+A2 derivation of ABJ.

## Theorem

Assume the framework's retained/bounded matter-content surface supplies the
left-handed chiral gauge content

```text
(2, 3)_{+1/3} + (2, 1)_{-1}
```

on the `Z^3` spatial substrate, and use the cited standard theorem:

```text
ABJ/Wess-Zumino/Fujikawa anomaly-to-inconsistency:
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

2. By the ABJ standard-theorem bridge, gauge consistency requires an
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
7. Therefore the only allowed time count on this bounded standard-theorem
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

The three non-zero traces are exactly the perturbative obstruction entries
consumed by the ABJ standard-theorem bridge.

### 2. ABJ standard theorem and chiral completion

The standard-theorem bridge cited above records the ABJ/Wess-Zumino/Fujikawa
anomaly-to-inconsistency implication as a cited theorem of chiral gauge QFT
and verifies the framework's nonzero-anomaly hypothesis. The present theorem
does not hide that dependency: the ABJ theorem is a bounded standard-theorem
bridge, not an A1+A2-native derivation. On that theorem, the non-zero anomaly
traces are not optional; consistency requires chiral completion.

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

This note closes the 3+1 spacetime bridge only on the current
standard-theorem bounded surface:

```text
ABJ standard-theorem bridge + chiral matter surface + retained Clifford parity
+ single-clock codimension-1 evolution -> d_t = 1.
```

It does **not** close:

- a first-principles derivation of the ABJ anomaly-to-inconsistency theorem
  from A1+A2 alone;
- a non-zero-index standard staggered `epsilon` witness on finite even tori;
- the audit of the single-clock theorem or any audit-pending upstream source;
- a route in which observed spacetime dimension is used as an input.

It also does not use PDG values, continuum dimensional fitting, the Wilson
plaquette, `alpha_LM`, Yukawa data, Planck data, or Monte Carlo measurements.

## Audit Handoff

```yaml
proposed_claim_type: bounded_theorem
actual_current_surface_status: standard-theorem bounded composition
standard_theorem_bridge:
  id: ABJ/Wess-Zumino/Fujikawa anomaly-to-inconsistency for chiral gauge theories
  route: docs/ABJ_STANDARD_THEOREM_BRIDGE_FOR_ANOMALY_FORCES_TIME_NOTE_2026-05-30.md
accepted_premise_packet_load_bearing: false
unbounded_positive_theorem_allowed: false
why_not_unbounded: >
  The ABJ anomaly-to-inconsistency implication is cited as a standard theorem
  rather than derived from A1+A2. The current finite-even-torus staggered
  epsilon-index route to internalizing it is pruned by a square-block no-go;
  other internal ABJ routes remain open.
audit_required_before_effective_status_change: true
```

The requested audit question is narrow: whether this repaired parent note is
now a clean bounded theorem / standard-theorem positive composition for
`d_t = 1`, with all remaining unbounded blockers named explicitly.
