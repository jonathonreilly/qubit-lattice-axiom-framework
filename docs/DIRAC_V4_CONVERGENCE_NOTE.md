# Dirac v4 Convergence Note

Date: 2026-04-10 (synced 2026-05-23)
**Type:** bounded_theorem
**Status authority:** independent audit lane only

This note records the larger-lattice attack in
[`scripts/frontier_dirac_walk_3plus1d_v4_convergence.py`](../scripts/frontier_dirac_walk_3plus1d_v4_convergence.py).

The headline tables below are the **default-mass cached run** (`mass0 = 0.300`,
`strength = 5e-4`), which is the canonical artifact in
[`logs/runner-cache/frontier_dirac_walk_3plus1d_v4_convergence.txt`](../logs/runner-cache/frontier_dirac_walk_3plus1d_v4_convergence.txt)
that the audit lane reads. The runner also accepts `--mass0` and `--strength`
for off-cache diagnostics; those alternative invocations are out-of-scope for the
audited claim of this note and are listed below only as carry-forward pointers.

## Setup

- Architecture: 4-component Dirac walk
- Gravity coupling: reversed, `m(r) = m0 * (1 + f(r))`
- Boundary comparison: periodic vs open/absorbing
- Lattice sizes: `n = 17, 21, 25, 29`
- N-sweep target: `n = 29`
- Distance-law target: `n = 29`, `N = 16`
- Cached invocation: default args (`mass0 = 0.300`, `strength = 5e-4`)

## Cached-Run Results (mass0 = 0.300)

### Baseline periodic closure mass check

- `n = 17, N = 12` -> `6/10` (rows `PPPPFFPPFF`), `gravity_bias = -4.7460e-09`

### Larger-lattice periodic closure sweep

The closure score is flat at `6/10` across the larger lattice sweep:

- `n = 17, N = 12` -> `6/10`, `gravity_bias = -4.7460e-09`, `dist_R2 = 0.2680`
- `n = 21, N = 12` -> `6/10`, `gravity_bias = -4.0447e-09`, `dist_R2 = 0.3106`
- `n = 25, N = 12` -> `6/10`, `gravity_bias = -4.0447e-09`, `dist_R2 = 0.3107`
- `n = 29, N = 12` -> `6/10`, `gravity_bias = -4.0447e-09`, `dist_R2 = 0.3105`

The score does not improve with larger `n`.

### Gravity monotonicity over N

At `n = 29`, `offset = 3`, sweeping `N = 8..24`:

- Periodic: sign flips across the sweep, **no monotone increasing TOWARD bias**
- Open/absorbing: same qualitative pattern, **no monotone increasing TOWARD bias**

The open boundary does not remove the N oscillation.

### Distance law over offset

At `n = 29`, `N = 16`, sweeping offsets `2..6`:

- Periodic: **0/5 TOWARD**, all biases negative; power-law fit `alpha = 2.451`,
  `R^2 = 0.3954`
- Open/absorbing: **0/5 TOWARD**, all biases negative; power-law fit
  `alpha = 2.452`, `R^2 = 0.3955`

The non-periodic boundary does not cure the offset-law failure.

## Interpretation

The larger-lattice Dirac walk in this default-mass diagnostic is not rescued by
simply going bigger. Closure stays at `6/10` across the entire `n = 17..29`
sweep, and the gravity-monotonicity and distance-law failures persist on both
boundaries.

The periodic and open runs agree on the qualitative point: the remaining
default-mass Dirac failures are not just a periodic-torus artifact. They
survive the boundary change and look structural in the current factorized
4-component implementation at this mass setting.

## Off-Cache Diagnostics (not in cached run)

The runner accepts `--mass0` to vary the mass parameter. A `mass0 = 0.10`
invocation is *not* part of the canonical cached artifact this note's audited
claim rests on; it is reproducible by running

```
python3 scripts/frontier_dirac_walk_3plus1d_v4_convergence.py --mass0 0.10
```

The earlier draft of this note carried a `m0 = 0.10` headline (closure `7/10`,
distance-law `3/5 TOWARD`). Those numbers are not in the cached default-mass
artifact and have therefore been **demoted to a carry-forward pointer**, not a
load-bearing claim of this note. Future work that promotes a non-default
operating point to a ratifiable result must register a corresponding artifact
(e.g. a frozen log or a separate runner) so the audit lane can read it.

## Carry-Forward

- Treat the headline tables above (default `mass0 = 0.300`) as the audited
  scope of this note.
- Treat the gravity-monotonicity and distance-law failures at default mass as
  structural until a coupled Dirac coin or a different observable changes them.
- Use this script as the large-lattice baseline for the next attack round.
- An off-cache `--mass0 0.10` probe exists as a diagnostic tool but does not
  carry an independently audited claim in this note.
