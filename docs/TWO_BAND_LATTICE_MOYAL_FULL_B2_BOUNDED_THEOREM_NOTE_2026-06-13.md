# Two-Band Lattice Moyal Full B2 Bounded Note

**Script:** `scripts/frontier_two_band_lattice_moyal_full_b2_2026_06_13.py`

**Status:** bounded miss, not closure. The audit lane grades.

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

The result does **not** close the supplied finite-cell full-PT response. After
fixing the single cell normalization at the stated `m=0` reference, the
independent masses leave a maximum relative residual of `35.654%` at `m=0.5`.

## Anchor And Normalization

The external #3743 finite-cell full-PT anchors supplied in the prompt are:

| m | exact response |
|---:|---:|
| 0.0 | 0.042933687517 |
| 0.2 | 0.041273318495 |
| 0.3 | 0.039175811591 |
| 0.5 | 0.030744459999 |

The runner uses these anchors only as comparators. The single overall cell
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

- internal consistency replay of the spec-supplied #3743 anchors retains the
  in-file values to full displayed precision,
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
