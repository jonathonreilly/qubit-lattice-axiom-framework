# Block25 preflight witnesses

No target overlap census or commutator has been executed in this packet.

## Exact imported shape

For a tip `t=(x,f,b)`, the sharp input control constrains

- the 26 pointer factors of the current block at `x` to `Locked(f,b)`;
- all 32 live/pointer factors of the selected block at `x+9f` to the radial
  Blank product; and
- no current live factor and no lateral candidate block.

The current and selected blocks are disjoint within one tip. Across two tips,
their constrained physical sites can coincide with different block-relative
radial one-qubit factors. Geometry-only overlap is therefore insufficient;
commutation must be computed from the literal physical factors.

## Registered adversarial pair families

1. two disjoint current Records sharing exactly one target center;
2. two disjoint current Records whose target centers differ by a nearest
   lattice displacement;
3. partial current/current overlap;
4. current/target overlap;
5. target/target overlap; and
6. disjoint footprints as the factorization control.

For product projections `P,Q`, collapse their shared constrained factors to the
exact product fidelity `q`. The registered algebraic screen is

```text
q = 0 or 1  -> the sharp product projections commute;
0 < q < 1   -> their commutator is nonzero, with certificate q(1-q) > 0.
```

The shifted-target family is an adversarial candidate, not a preregistered
result. The source must derive its relative displacement, shared physical
sites, Bloch factors, and exact rational/radical overlap without a target
table.

If Stage A is green, the arbitrary-graph proof must still establish Kraus
completeness, arbitrary-reference CP, singleton equality, disjoint
factorization/order independence, Record QND, exact Blank debit, covariance,
and finite-window padding consistency.
