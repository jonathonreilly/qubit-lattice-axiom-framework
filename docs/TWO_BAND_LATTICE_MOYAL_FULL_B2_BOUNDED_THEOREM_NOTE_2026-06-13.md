# Two-Band Lattice Moyal Full B2 Bounded Note

**Claim type:** bounded_theorem
**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome and does not edit audit-owned registry, ledger, queue,
or publication-status surfaces.
**Script:** `scripts/frontier_two_band_lattice_moyal_full_b2_2026_06_13.py`
**Runner cache:** `logs/runner-cache/frontier_two_band_lattice_moyal_full_b2_2026_06_13.txt`

**Status:** bounded miss, not closure. The audit lane grades.

## One-Hop Authority

- [FINITE_CELL_TWO_BAND_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-13.md](FINITE_CELL_TWO_BAND_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-13.md)
  for the supplied `Q=24`, `Ly=2`, `mu=1.7086`, `T=0.2` finite-cell response
  reference and the independent real-space Harper perturbation check.

## Claim

For the free two-band lattice Hamiltonian

```text
H(k) = -2 cos(kx) sigma_x - 2 cos(ky) sigma_y + m sigma_z,
```

the full lattice Moyal star-product expansion through order `B^2` was
implemented from the star-inverse equation for `G=(z-H)^{-1}_star`. The
implemented coefficient includes:

- the `Lambda(A,G1)` intra/inter cross contribution,
- the second-derivative `Lambda^2(A,G0)` contribution,
- the full lattice Hessians `A_xx` and `A_yy`; no continuum linearization is
  used.

The runner cross-checks that implemented `B^2` source matrix directly against
an independent finite-difference Moyal reconstruction at fixed `(kx, ky, m, z)`
samples. That reconstruction finite-differences `G0`, builds `G1` from the
order-`B` star-inverse equation, finite-differences `G1`, and then applies
`(i/2)Lambda(A,G1) - (1/8)Lambda^2(A,G0)` component by component. It is not
the old star-inverse residual identity `A*(-G*x_mat)+x_mat=0`.

The result does **not** close the supplied finite-cell response from the
one-hop finite-cell reference above. After fixing the single cell normalization
at the stated `m=0` reference, the independent masses leave a maximum relative
residual of `35.654%` at `m=0.5`.

## Reference And Normalization

The finite-cell reference values are recomputed by the landed finite-cell
closed-form runner:

| m | exact response |
|---:|---:|
| 0.0 | 0.042933687517 |
| 0.2 | 0.041273318495 |
| 0.3 | 0.039175811591 |
| 0.5 | 0.030744459999 |

The runner uses these references only as comparators. The single overall cell
normalization is fixed at `m=0`:

```text
raw Moyal response(m=0) = -1.919231499963e-01
target(m=0)             =  4.293368751700e-02
normalization           = -2.237024950759e-01
```

No per-mass normalization and no interband prefactor is fitted.

## Measured Results

```text
m    raw_full             raw_cross            raw_second           closed_form        exact              rel_dev
0.0 -1.919231499963e-01 -1.512796811380e-01 -4.064346885829e-02 +4.293368751700e-02 +4.293368751700e-02 0.000000e+00
0.2 -1.911159680716e-01 -1.511919018653e-01 -3.992406620630e-02 +4.275311890647e-02 +4.127331849500e-02 3.585368e-02
0.3 -1.900675977836e-01 -1.510512013202e-01 -3.901639646342e-02 +4.251859585729e-02 +3.917581159100e-02 8.532776e-02
0.5 -1.864358826837e-01 -1.503642275925e-01 -3.607165509114e-02 +4.170617212802e-02 +3.074445999900e-02 3.565427e-01
```

The mass trend is too flat. The remaining gap is therefore not an overall cell
normalization error; it is a mass-dependent finite-cell/full-PT correction not
captured by the order-`B^2` lattice Moyal symbol used here.

## Gates

The runner exits with:

```text
TOTAL: PASS=15 FAIL=0
```

Key gates:

- the finite-cell reference values are recomputed from the landed finite-cell
  closed-form runner and match the displayed reference values to full displayed
  precision,
- finite-difference Moyal `B^2` source-matrix check matches the implemented
  cross and second-derivative terms with `max_x_abs=5.590727e-07` and
  coarse-to-fine minimum convergence ratio `3.977` under tolerance `7.0e-07`,
- Berry/interband residue probe is zero at `m=0` and nonzero off `m=0`,
- 48-to-64 Gauss-Legendre drift is `4.254397e-05`, below the frozen
  `4.0e-3` tolerance,
- partial-fraction reconstruction residual is `2.903240e-12`, below the frozen
  `2.0e-8` tolerance,
- measured non-reference residual is honestly bounded by `0.38`.

## Scope

This note is scoped only to the free `d=2` staggered two-band model above at
`mu=1.7086`, `T=0.2`, and `m in {0, 0.2, 0.3, 0.5}`. It is not a closure claim.
It records that the complete lattice Moyal `B^2` term, as derived from the
star-product resolvent, still misses the exact finite-cell full-PT response.

## No-Go Discipline Gate

N1 alternative routes checked: missing Moyal cross term, missing second
derivative term, scalar normalization, quadrature/pole-fit error, and
finite-cell closed-form reference error. The first two are tested by
drop-term and finite-difference source-matrix gates; scalar normalization is
fixed at `m=0` and fails off-reference masses; quadrature and pole-fit errors
are bounded by the runner; the finite-cell reference is supplied by the landed
finite-cell closed-form note.

N2 wall independence: the remaining wall is single, not a wall stack. It is
the finite-cell/full-PT mismatch between the thermodynamic lattice-Moyal
symbol integral and the supplied finite-cell Harper response.

N3 hidden-wall scan: the load-bearing context is explicit: supplied model,
supplied finite-cell reference, one `m=0` normalization, and the implemented
Peierls/Moyal `B^2` source. No interaction, thermodynamic-limit closure, or
all-response no-go is claimed.

N4 residual matching: the claimed residual is only the measured mismatch on
the stated mass grid. It does not claim to rule out a finite-cell closed form;
that route is explicitly separated and supplied by the one-hop finite-cell
reference.

N5 rhetoric audit: "does not close" means "does not close below the frozen
2% finite-grid threshold after the stated one-point normalization" for this
model and mass grid, not a global statement about every Moyal, Harper, or
finite-cell route.

N6 partial-closure path scan: the finite-cell path is open and already has a
landed source reference. This note redirects to that path rather than
classifying it as a new axiom, primitive, or impossible route.

N7 steelman: a hostile reviewer should say that the finite-cell object is the
wrong target for a thermodynamic Moyal integral, and a finite discrete momentum
closed form could still explain the response. This note accepts that steelman:
it lands only the bounded negative for the continuum/Moyal comparator and
keeps finite-cell structure separate.

N8 cross-cycle echo: this has the same shape as other route-local comparator
misses in the repo: a continuum or thermodynamic approximation fails to close
a finite-cell target. The repair mechanism is not rejection of the target but
localizing the missing object to a finite-cell/full-PT calculation.
