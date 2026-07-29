# Wilson `mu^2` Distance Sweep Note

**Date:** 2026-04-11; audit-artifact repair 2026-07-29
**Status:** bounded finite-grid calibration and finite diagnostic certificate
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only
**Primary runner:** [scripts/frontier_wilson_mu2_distance_sweep.py](../scripts/frontier_wilson_mu2_distance_sweep.py)

## Claim scope

This note makes two bounded, executable claims.

1. On the declared open-Wilson grid
   `side in {11,13,15}`, `G=5`, `d in {3,4,5,6}`, and
   `mu^2 in {0.22,0.05,0.01,0.005,0.001}`, the shared-minus-self
   early-centroid-acceleration observable is attractive and clean in all
   `60/60` rows. The five log-log distance fits soften strictly from
   `alpha=-3.315` to `alpha=-1.871`.
2. On the separate declared `4 x 4` mass grid at `side=15`, `G=5`,
   `mu^2=0.001`, and `d=5`, one early-centroid momentum proxy does not
   pass its declared slice-linearity,
   grid-normalization, or signed-balance criteria.

The second item is a result about this finite diagnostic only. It is not a
no-go for Newton closure, does not exhaust other readouts or parameter
surfaces, and is not load-bearing for the positive distance-sweep result.

## Executable evidence

Primary distance-sweep evidence:

- [runner](../scripts/frontier_wilson_mu2_distance_sweep.py)
  (SHA-256 `3bf54d77aa1ec158d6efe5076a7c71e7bf463dd21db277d6217cd704988f6fe1`)
- [complete SHA-pinned cache](../logs/runner-cache/frontier_wilson_mu2_distance_sweep.txt)
- [open-Wilson helper](../scripts/frontier_wilson_two_body_open.py)
  (SHA-256 `4bdf0c25421509b987b4424ce9dc6befa6281d8a4e50be49578fc60e5b01ae4f`)

Finite both-masses diagnostic evidence:

- [runner](../scripts/frontier_newton_both_masses.py)
  (SHA-256 `bcf8d594e021e9df08c1f65813e08d613b794840ae19806f670135e2cf238359`)
- [complete SHA-pinned cache](../logs/runner-cache/frontier_newton_both_masses.txt)

Both cache bodies fit the audit transport without head/tail clipping. The
distance certificate block reports `TOTAL: PASS=6 FAIL=0`; the standalone
diagnostic cache ends with `TOTAL: PASS=9 FAIL=0`. Explicit
value checks in each runner bind the displayed source tables. These execution
totals do not relabel the finite diagnostic nonpass as a runner failure.

No long parent note is a load-bearing authority for this claim. The model,
observable, thresholds, fit, and scope needed to read the two finite
certificates are stated below and implemented in the linked sources.

## Distance-sweep construction

The helper constructs an open three-dimensional cubic lattice with the
nearest-neighbor Laplacian. Its fixed numerical parameters are Wilson
diagonal/hopping parameter `MASS=0.30`, `r=1`, time step `DT=0.08`, Poisson
regularizer `REG=1e-3`, `20` evolution steps, unit source weights, and
Gaussian width `sigma=1`. For each row it:

1. places two normalized Gaussian packets at the declared separation;
2. solves the screened discrete Poisson equation with the displayed
   `G` and `mu^2`;
3. evolves the two packets with the displayed Wilson hopping and diagonal
   potential in `SHARED` and `SELF_ONLY` modes;
4. forms the early-time mutual centroid acceleration
   `a_mut = a_SHARED - a_SELF_ONLY`;
5. averages indices `2..10` of the `21`-point acceleration series, defines
   `SNR=|mean(a_mut)|/(std(a_mut)+1e-12)` on that window, and labels a row
   `ATTRACT` when `a_mut < -1e-6` and `CLEAN` when `SNR > 2`.

For each `mu^2`, the primary runner fits all twelve clean attractive rows
(three sides times four distances) by ordinary least squares in log space:

```text
log |a_mut| = alpha log d + intercept.
```

Thus the theorem is a finite computation under an explicitly supplied model
and observable. It is not an asymptotic, continuum, or universal distance-law
theorem.

## Distance-sweep results

| `mu^2` | fitted `alpha` | `R^2` | attractive | clean | minimum SNR |
|---:|---:|---:|---:|---:|---:|
| 0.22 | -3.315 | 0.9960 | 12/12 | 12/12 | 8.12 |
| 0.05 | -2.392 | 0.9978 | 12/12 | 12/12 | 6.13 |
| 0.01 | -1.992 | 0.9984 | 12/12 | 12/12 | 5.67 |
| 0.005 | -1.927 | 0.9985 | 12/12 | 12/12 | 5.61 |
| 0.001 | -1.871 | 0.9986 | 12/12 | 12/12 | 5.56 |

The fitted exponent softens strictly across the sampled grid:

```text
-3.315 < -2.392 < -1.992 < -1.927 < -1.871.
```

The scan passes through a near-`d^-2` fit at `mu^2=0.01`. The last two
sampled exponents continue to soften past `-2`; the data therefore establish
monotonic softening and strong screening-parameter dependence, not monotonic
convergence to exactly `-2`.

All sixty sampled rows remain attractive and clean. This retains the bounded
mutual-channel calibration while avoiding any universality claim.

## Finite both-masses diagnostic

The second runner uses:

- `side=15`, `G=5`, `mu^2=0.001`, `d=5`;
- `M_A,M_B in {0.5,1.0,2.0,3.0}`;
- Wilson parameter `r=1`, `DT=0.08`, `REG=1e-6`, `18` evolution steps,
  Gaussian width `sigma=1`, and early velocity-difference indices `2..7`;
- each declared mass parameter as a Poisson source weight and as a constant
  Wilson-diagonal term;
- early-window centroid-velocity differences between `SHARED` and
  `SELF_ONLY`.

The diagonal mass term is spatially constant. Under exact unitary evolution
it would supply only a global phase; its parameter dependence in this runner
is specific to the finite-step Crank--Nicolson update. Multiplication by
`M_A` or `M_B` below is imposed as part of the proxy, not derived from a
momentum operator. The runner therefore does not establish a physical
inertial-mass law and evaluates only these declared diagnostic quantities:

```text
P_A^mut = M_A <v_A^shared - v_A^self>
P_B^mut = M_B <v_B^self - v_B^shared>
balance = P_A^mut - P_B^mut
```

The complete `4 x 4` output gives:

| diagnostic | computed result | declared pass criterion | outcome |
|---|---:|---:|---|
| `P_A^mut` vs `M_B` at `M_A=1` | `R^2=0.944530` | both anchor `R^2>0.95` | nonpass |
| `P_B^mut` vs `M_A` at `M_B=1` | `R^2=0.940033` | both anchor `R^2>0.95` | nonpass |
| `P_A^mut/M_B` over the grid | `CV=35.382%` | both CVs `<15%` | nonpass |
| `P_B^mut/M_A` over the grid | `CV=37.501%` | both CVs `<15%` | nonpass |
| signed-balance proxy `|P_A^mut-P_B^mut|/(|P_A^mut|+|P_B^mut|)` | `0/16` pass; mean and max imbalance `100%` | mean `<10%`, max `<25%` | nonpass |

With inward motion defined as positive separately for each body, every sampled
row gives `P_A^mut < 0` but `P_B^mut > 0`. Converting the B proxy back to a
signed x-coordinate and adding it to A is therefore equivalent here to
`P_A^mut-P_B^mut`, whose magnitude equals the denominator and produces the
displayed `100%` imbalance. This exposes a one-sided coordinate response of
this proxy; it says nothing by itself about conservation of a physical
momentum operator. Consequently this sampled centroid proxy does not establish
full Newton closure. That sentence reports failure to satisfy the runner's
displayed finite criteria; it does not prove that another observable or
another surface cannot close them.

## Negative-claim boundary

No route-exhaustion result is claimed. In particular, this note leaves open:

- a local momentum-flux readout through a separating surface;
- a directly antisymmetrized impulse observable;
- weaker-coupling or lighter-mass windows;
- larger-volume and continuum-controlled surfaces;
- an analytic Ward/flux or action-reaction theorem.

Accordingly, no independent exhaustive walls, hidden-wall clearance, witness
matching, partial-closure exclusion, steelman defeat, or cross-cycle no-go
closure is asserted. The only negative content is the displayed finite
criterion nonpass.

## Conclusion

The complete executable packet supports a bounded calibration: across the
five sampled screening values, the fitted exponent softens monotonically from
`-3.315` to `-1.871`, and every sampled mutual-channel row is attractive
and clean. The same packet also records that one separate finite centroid
proxy does not establish both-masses Newton closure.

This note should be cited as a finite Wilson screening calibration plus a
scoped diagnostic nonpass, never as a universal Newton law or a no-go theorem.
