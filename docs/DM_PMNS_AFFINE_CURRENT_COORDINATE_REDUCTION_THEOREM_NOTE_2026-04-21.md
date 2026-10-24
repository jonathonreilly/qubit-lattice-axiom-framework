# Supplied affine current-coordinate reduction

**Type:** bounded_theorem
**Status:** conditional coordinate algebra; physical source selection open.
**Primary runner:** `scripts/frontier_dm_pmns_affine_current_coordinate_reduction_2026_04_21.py`

Supply the affine chart H=Hbase+m Tm+delta Tdelta+q_+ Tq and character current.
A supplied current value reconstructs q_+; mere nonzero current does not choose
its physical value. The delta direction and spectator m remain current-blind.

## 2. Exact affine current formula

Let the exact affine basis be

```text
T_m,
T_delta,
T_q.
```

Then the native nontrivial-character current on the affine chart satisfies

```text
J_chi(H_base) = -i/4,
J_chi(T_m) = 0,
J_chi(T_delta) = 0,
J_chi(T_q) = 1.
```

Therefore, by exact affine linearity on the chart,

```text
J_chi(H(m, delta, q_+))
  = J_chi(H_base) + m J_chi(T_m) + delta J_chi(T_delta) + q_+ J_chi(T_q)
  = q_+ - i/4.
```

This is the full chart formula.

So the native current does **not** read the whole affine pair `(delta, q_+)`.
It reads only the centered doublet-trace coordinate `q_+`, together with the
fixed base offset `-i/4`.

---


## Consequence and preserved counterexample

At fixed m,q_+, the two supplied points delta=.20 and1.10 have the same current
but different shifted imaginary K12 readouts. The graded-current companion
recovers delta from a second supplied current; an invertible coordinate change
does not select either current value. A physical source law remains open.
The old inherited scalar-closure claim is withdrawn; full original argument
and computation are preserved in Git and the review recovery package.

Definitions/context only:
- [chart](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md)
- [doublet readout](DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md)
- [graded coordinates](DM_PMNS_ORDERED_CHAIN_GRADED_CURRENT_DELTA_CLOSURE_THEOREM_NOTE_2026-04-21.md)
- [supplied chain](DM_PMNS_GRAPH_FIRST_ORDERED_CHAIN_NONZERO_CURRENT_ACTIVATION_THEOREM_NOTE_2026-04-21.md)
