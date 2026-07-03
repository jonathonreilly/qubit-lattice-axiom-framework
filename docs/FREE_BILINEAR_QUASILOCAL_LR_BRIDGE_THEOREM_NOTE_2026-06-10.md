# Free Bilinear Exact-Log Quasilocal Lieb-Robinson Bridge

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** in the free (`U = 1`) bilinear staggered two-step sector,
the exact reconstructed Hamiltonian
`H = -log(T_hat^2)/(2 a_tau)` whose kernel is supplied by
[`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
obeys a finite-velocity quasilocal Lieb-Robinson envelope. If
`0 < d mu < eta < arcsinh(m)` and
`W_mu := sup_x sum_y ||Phi_{xy}|| exp(mu d_1(x,y))`, then
`W_mu < infinity` and, for one-site observables,

```text
    ||[alpha_t(A_x), B_y]||
      <= 2 ||A_x|| ||B_y|| exp(-mu d_1(x,y) + 4 W_mu |t|).
```

Equivalently the finite lightcone speed at this `mu` is
`v_mu = 4 W_mu / mu`. The strict finite-range `R <= 2` exact-log claim
remains false on this sector; the gauged/interacting exact-log locality and
full continuum microcausality are not claimed here.

**Status authority:** independent audit lane only. This source note does not
set or predict audit status.

**Primary runner:** [`scripts/free_bilinear_quasilocal_lr_bridge_2026_06_10.py`](../scripts/free_bilinear_quasilocal_lr_bridge_2026_06_10.py)
**Cache:** [`logs/runner-cache/free_bilinear_quasilocal_lr_bridge_2026_06_10.txt`](../logs/runner-cache/free_bilinear_quasilocal_lr_bridge_2026_06_10.txt)

## Why this note exists

The parent microcausality row asked for a finite-range or quasilocal
decomposition of the exact reconstructed logarithmic Hamiltonian
`H = -log(T)/a_tau`, and for the parent LR constant to be updated from the
stale `2 e r J` form to the overlap-weight convention of
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md).
The transfer-matrix log-quasilocality theorem supplies the missing exact-log kernel
and exponential tail, but deliberately leaves the quasilocal
Lieb-Robinson composition as a named next theorem. This note supplies exactly
that composition, still only on the free bilinear sector where the kernel is
currently proved.

## Inputs

1. **Exact-log kernel.** The transfer-matrix log-quasilocality theorem proves that,
   for the free bilinear two-step transfer matrix,

   ```text
       H = sum_{x,y} h(x-y) a_x^dag a_y,
       |h(z)| <= (1/a_tau) C_d(eta,m) exp(-eta ||z||_inf)
   ```

   for every `0 < eta < eta* := arcsinh(m)`, with explicit
   `C_d(eta,m) = sqrt(m^2 + (d-1) + cosh^2 eta)`, and translates this into a
   support-family kernel with finite unweighted per-site overlap
   `W_H = ||h||_1`.
2. **Overlap-weight LR convention.** The finite-range microcausality bridge
   proves the support-family LR lemma in the overlap-weight variables
   `(q, R, W)` and supersedes the parent row's stale `2 e r J` constant.
   This note reuses that path-counting convention but performs the
   exponentially weighted quasilocal path sum directly.
3. **One-site algebra.** The current
   [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
   finite one-qubit one-site operator algebra. No record, readout, species,
   gauge, or continuum bridge is consumed.

No empirical value, fitted parameter, PDG input, or observed comparator enters
the proof.

## Statement

Let `Phi_{xy}` denote the two-site hopping term associated with the exact-log
kernel and write `d_1(x,y)` for the lattice `l1` distance. For any
`mu > 0` define

```text
    W_mu := sup_x sum_y ||Phi_{xy}|| exp(mu d_1(x,y)).
```

**(B1) Finite weighted overlap.** If `0 < d mu < eta < arcsinh(m)`, then
`W_mu` is finite. Indeed, from the cited kernel bound and
`||z||_1 <= d ||z||_inf`,

```text
    W_mu <= (C_d(eta,m)/a_tau)
             sum_{r>=0} [(2r+1)^d - (2r-1)^d] exp(-(eta - d mu) r),
```

where the `r=0` shell is read as one site. The right-hand side converges
because `eta - d mu > 0`.

**(B2) Weighted-path LR bound.** For one-site observables `A_x`, `B_y` and
`alpha_t(A) = exp(i t H) A exp(-i t H)`,

```text
    ||[alpha_t(A_x), B_y]||
      <= 2 ||A_x|| ||B_y|| exp(-mu d_1(x,y) + 4 W_mu |t|).              (1)
```

Thus the sector has a finite quasilocal lightcone speed
`v_mu = 4 W_mu / mu`.

**(B3) Sector boundary.** This is not the strict finite-range parent
hypothesis. The exact log Hamiltonian on this sector has nonzero range-4
hops, so it must be read as quasilocal. The result is also not a theorem for
fixed-background gauge fields, interacting transfer matrices, or the
`m = 0` gapless boundary.

## Proof

### Step 1: weighted norm closure

The transfer-matrix log-quasilocality theorem gives
`|h(z)| <= C exp(-eta ||z||_inf)`. Since `||z||_1 <= d ||z||_inf`,

```text
    |h(z)| exp(mu ||z||_1)
      <= C exp(-(eta - d mu) ||z||_inf).
```

Summing over `l_inf` shells gives (B1). This is the only place where the
strict inequality `d mu < eta` is used.

### Step 2: weighted path expansion

Expand the Heisenberg evolution in nested commutators:

```text
    alpha_t(A_x) = sum_{n>=0} (i t)^n ad_H^n(A_x) / n!.
```

A nonzero contribution to `[ad_H^n(A_x), B_y]` is a chain of pair terms whose
supports connect `x` to `y`. Each commutator contributes a harmless factor
`2`, and the final commutator with `B_y` contributes another factor `2`.
For any path `x = x_0, x_1, ..., x_n = y`,

```text
    prod_j ||Phi_{x_{j-1} x_j}||
      <= exp(-mu d_1(x,y))
         prod_j (||Phi_{x_{j-1} x_j}|| exp(mu d_1(x_{j-1},x_j))),
```

by the triangle inequality. Summing over intermediate sites bounds the
weighted path sum by `exp(-mu d_1(x,y)) W_mu^n`. Therefore

```text
    ||[alpha_t(A_x), B_y]||
      <= 2 ||A_x|| ||B_y|| exp(-mu d_1(x,y))
         sum_{n>=1} (2 W_mu |t|)^n / n!.
```

Since `sum_{n>=1} u^n/n! <= exp(u)` and the bridge is intentionally
conservative, we record the weaker but simpler envelope (1) with
`4 W_mu |t|`. This proves (B2).

### Step 3: finite-speed reading

Equation (1) can be written

```text
    2 ||A_x|| ||B_y|| exp[-mu (d_1(x,y) - v_mu |t|)],
    v_mu = 4 W_mu / mu.
```

For fixed `mu`, this is a finite lattice lightcone. The constants are not
claimed optimal; their purpose is to close the existence and finite-speed
composition step from the cited exact-log kernel.

## Runner checks

The runner performs five checks:

1. computes `W_mu` from the cited `d = 1` exact-log kernel and verifies it
   is below the cited strip-bound shell sum;
2. computes a `Z^3` weighted overlap on a `64^3` kernel and verifies it is
   below the same shell-sum upper bound when `3 mu < eta`;
3. directly checks the weighted convolution path inequality on sampled
   path lengths;
4. builds a finite hard-core bilinear matrix Hamiltonian from the exact-log
   kernel and checks the commutator envelope against exact matrix evolution;
5. falsifies the theorem against a positive, gapped symbol with an algebraic
   Fourier tail, whose exponential weighted norm grows with cutoff.

Expected output:

```text
TOTAL: PASS=5 FAIL=0
```

## Boundaries

- **Free bilinear only.** The theorem consumes the translation-invariant
  exact-log kernel of the free two-step sector. It does not prove
  gauged/interacting log-transfer locality.
- **Mass gap required.** At `m = 0`, the transfer-matrix log-quasilocality theorem
  records power-law tails; then no positive `eta` is available and this
  bridge does not apply.
- **Continuum microcausality not automatic.** The theorem supplies a finite
  lattice lightcone. Any continuum spacelike-commutator statement must still
  cite a matching Lorentz scaling bridge and keep its sector assumptions
  explicit.
- **No new axiom.** This is a theorem-level consequence of the cited
  exact-log kernel and the current one-site algebra; it adds no primitive.

## Citations

- [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
  - exact-log kernel, exponential tail, support-family translation, and
  strict finite-range failure on the free bilinear sector.
- [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  - overlap-weight LR convention and finite-range path-counting template.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  - current Lattice/Quantum/Record premise node; only the finite one-site
  Quantum algebra and lattice metric are consumed.

## Changelog

- **2026-06-10** - initial bridge note and runner. Closes the quasilocal LR
  composition step for the free bilinear exact-log sector with explicit
  weighted-overlap constants and a conservative finite velocity.
