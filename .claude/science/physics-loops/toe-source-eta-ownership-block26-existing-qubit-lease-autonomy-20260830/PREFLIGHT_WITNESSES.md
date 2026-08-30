# Block26 preflight witnesses

No Block26 target runner has been executed in this packet.

## Finite lease witness family

For an anchor `x`, use the literal Block24 carrier consisting of the current
block and all six candidate forward blocks. It has 224 sites. The local success
family sums over all fronts `f`, current labels `b`, and next outcomes `c`; its
STOP branch completes the orthogonal complement. A declared finite lease
family is admissible for the direct product only when these complete 224-site
carriers are pairwise disjoint. A denser 64-site map indexed by a supplied
typed `(f,b)` choice would be a different off-sector channel and may not be
reported as literal complete-Block24 tensorization.

## Symmetry witness candidate

Use the literal Block25 pair

```text
A: anchor (0,0,0),       front (-1,0,0)
B: anchor (-19,-1,0),   front ( 1,0,0)
```

and the affine proper-cubic map

```text
h(x,y,z)=(-x-19,-y-1,z).
```

The source must derive whether `h` exchanges anchors, fronts, targets, and
covariantly related stored labels; whether it has a lattice fixed point; and
what equivariance implies for two classical grant bits. Expected answers are
not accepted as stored booleans.

## Recorded-owner candidate

On two declared existing status qubits, compare

```text
rho_ind = I4/4
rho_one = (|10><10| + |01><01|)/2.
```

The source must derive normalization, positivity, equal one-site marginals,
swap covariance, exact-one probability, and a complete Kraus instrument from
the declared status-Blank input. It must then bind each owner outcome to only
one selected Block24 append family and prove that no branch double-writes.

## Transfer adversary

Test two initially disjoint full-anchor carriers at anchors `0` and `27 e1`
with inward fronts. After simultaneous append, their returned anchors are
`9 e1` and `18 e1`. Initial disjointness must not be promoted to a renewal
invariant unless the returned carriers pass the same certificate.
