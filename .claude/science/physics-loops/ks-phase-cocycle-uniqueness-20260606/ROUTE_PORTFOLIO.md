# Route Portfolio

## Chosen Route: Clifford Cocycle

From scalarization

```text
T'(x + mu) = eta'_mu(x) gamma_mu T'(x)
```

the two paths around a plaquette force

```text
eta'_nu(x + mu) eta'_mu(x) =
  - eta'_mu(x + nu) eta'_nu(x).
```

The canonical KS phases satisfy this `-1` cocycle. The ratio between
any other admissible phase system and the canonical representative is
a closed Z2 one-cochain, hence exact on a simply connected `Z^3` box.
So every local solution is a Z2 gauge transform of the canonical KS
representative.

## Rejected Route: Citation-Only Construction

The older source phrasing effectively relied on the standard
Kawamoto-Smit construction for uniqueness. That is not enough for
the repo's audit discipline, so this branch makes the local proof
framework-native.
