# Landau-Peierls Prefactor Native Derivation

Date: 2026-06-13
**Claim type:** bounded_theorem
**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome and does not edit audit-owned registry, ledger, queue,
or publication-status surfaces.

Primary runner:

```bash
python3 scripts/frontier_landau_peierls_prefactor_native_derivation_2026_06_13.py
```

Runner cache:

```text
logs/runner-cache/frontier_landau_peierls_prefactor_native_derivation_2026_06_13.txt
```

## Claim

Within the supplied magnetic Peierls/Moyal expansion for a smooth single-band
lattice dispersion `E(k_x,k_y)`, the Landau-Peierls orbital-response integrand

```text
chi_LP = -(1/12) integral_BZ f'(E) det Hess(E) dk / (2 pi)^2
```

does not require an imported numerical prefactor. The `-1/12` is obtained from
the `B^2` Peierls/Moyal star-expansion of the one-band grand potential and is
then checked against direct finite-lattice Peierls diagonalization.

The convention used by the runner is explicit.  If

```text
Omega(B) = Omega(0) + c_2 B^2 + O(B^4),
```

then the centered second-difference orbital response is

```text
chi = Omega''(0) = 2 c_2.
```

The symbolic derivation gives `c_2 = -(1/24) integral f'(E) det Hess(E)`;
therefore the response prefactor is exactly `-1/12`.

2026-06-18 source-side dependency use: this packet is now the explicit
prefactor companion for
`docs/D3_ORBITAL_RESPONSE_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md`.
The D3 runner imports this runner's symbolic derivation and uses the returned
exact rational as its Landau-Peierls normalization. This note remains a source
proposal until the independent audit lane grades it; it does not set its own
effective status or the D3 note's effective status.

## Native symbolic derivation

The runner starts from the magnetic star product

```text
a star b = ab + (iB/2){a,b} - (B^2/8)Lambda^2(a,b) + O(B^3),
```

and recursively computes the `B^2` term in `G_star(E)` for a generic polynomial
grand-potential test function.  Sympy reduces the result to

```text
local c_2 density =
  -(1/8) G''(E) D - (1/24) G'''(E) Q,
```

where

```text
D = E_xx E_yy - E_xy^2,
Q = E_x^2 E_yy - 2 E_x E_y E_xy + E_y^2 E_xx.
```

The non-determinant term is removed only by a separately checked periodic
divergence identity:

```text
div V = G'''(E) Q + 2 G''(E) D.
```

On the Brillouin torus, the divergence integrates to zero, so
`integral G'''(E) Q = -2 integral G''(E) D`.  Thus

```text
c_2 = -(1/24) integral G''(E) det Hess(E),
chi = 2 c_2 = -(1/12) integral f'(E) det Hess(E).
```

The runner gates the exact rational `-1/12` with Sympy and also verifies that a
nearby wrong prefactor (`-1/11`) leaves a nonzero residual.

## Independent Peierls Reference

The numerical reference is not computed from the LP formula. It builds the
periodic square-lattice Hofstadter Hamiltonian

```text
E(k) = -2(cos k_x + cos k_y)
```

with quantized flux `B = 2 pi n / L^2`, diagonalizes the finite matrix directly,
and forms the centered grand-potential curvature

```text
[Omega(B) + Omega(-B) - 2 Omega(0)] / B^2 / L^2.
```

Frozen gate point:

```text
T = 0.5
mu = -0.9
```

Final runner output:

```text
LP kgrid 48: -1.54931076443342586e-02
LP kgrid 96: -1.54931076443342274e-02

exact L=24, nflux=1: -1.54902341388942245e-02
exact L=24, nflux=2: -1.54924629021433169e-02
exact L=24, nflux=3: -1.54929624911126183e-02

exact L=20, nflux=1: -1.54820823062741322e-02  err=1.103e-05
exact L=24, nflux=1: -1.54902341388942245e-02  err=2.874e-06
exact L=28, nflux=1: -1.54932179874453253e-02  err=1.103e-07
derived LP thermodynamic value: -1.54931076443342274e-02

TOTAL: PASS=8 FAIL=0
```

## Scope

Bounded theorem note, single-band two-dimensional lattice case under the
supplied Peierls/Moyal star-product expansion. The `-1/12` response prefactor
is derived inside that expansion and survives an independent exact
finite-lattice Peierls diagonalization reference. No scalar prefactor is fitted
to the diagonalization data.

This packet is meant to retire the raw-textbook-scalar role, not to claim a
full continuum-QFT theorem or a thermodynamic-limit theorem for every
single-band model. The standard Landau-Peierls and magnetic-Moyal literature
can be cited in parallel as context, but the load-bearing scalar used by the
D3 source packet is the runner-derived rational plus the finite Peierls
diagonalization cross-check recorded here.
