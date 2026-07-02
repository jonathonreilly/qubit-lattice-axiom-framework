# Route-2 `t_balance`: Exact Finite Algebraic Active-Branch Value

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:** [scripts/quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.py](../scripts/quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.py)
**Runner cache:** [logs/runner-cache/quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.txt](../logs/runner-cache/quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.txt)
**Comparison authority:** [QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md)

## Result

With the active branch fixed to `probe0:xx`, the implemented Route-2
`t_balance = |b_T/a_T|` has the following 60-digit evaluation of the exact
finite algebraic-sum object:

```text
t_balance = 1.00003080948506836066836856179633336367619961694318329356352
```

and therefore

```text
|b_T/a_T| - 1 = 0.00003080948506836066836856179633336367619961694318329356352
```

This agrees with the tracked step-free double row
`1.000030809474` to `1.1068334e-11`, matching the conditioning of the
finite-stencil chain.

The exact representation is not a small rational, quadratic surd, or recognized
low-degree expression under the bounded searches run here. The source
representation is the exact finite algebraic sum below plus the high-precision
evaluation above.

## Exact-Sum Object

The implemented lattice has `SIZE = 15`, so the Dirichlet interior is
`13^3`, not `15^3`. For any interpolation point `xi`, the runner evaluates

```text
Phi_q(xi) =
  1/343 * sum_{a,b,c=1}^{13}
    L_a(xi_x) L_b(xi_y) L_c(xi_z) Q_abc
    / (6 - 2 cos(a pi/14) - 2 cos(b pi/14) - 2 cos(c pi/14)).
```

Here `Q_abc` is the sine transform of the seven-site star source `q`, and
`L_m` is the exact one-dimensional interpolation functional matching the live
`map_coordinates(order=3, mode="nearest")` contract: edge prepad by 12, a
rational tridiagonal cubic-spline coefficient solve, and rational cubic
B-spline weights. The runner checks this separable functional against SciPy on
sine modes with max error `3.497e-15`.

The active `probe0:xx` tensor stencil is then evaluated through the same
finite coordinate stencil `h = 0.04` used by the step-free runner, but with
the above exact-sum field samples instead of the sparse double Green columns.

Read-only implementation pointers: scripts/frontier_tensor_support_center_excess_law.py,
scripts/frontier_tensor_boundary_drive_two_channel.py,
scripts/frontier_tensorial_einstein_regge_completion.py,
scripts/frontier_quark_up_amplitude_tensor_endpoint_bridge.py.

## Endpoint Derivatives

The exact-sum active entry remains negative at both endpoint backgrounds, so
`beta = sign(G_xx^TF) dG_xx^TF/dt`.

| q | direction | `G_xx^TF(probe0)` | `dG_xx^TF/dt` | `beta` |
| --- | --- | ---: | ---: | ---: |
| `center/e0` | `E_x` | `-0.0000700717702532314624991441` | `+0.0000307201183725758190555301` | `-0.0000307201183725758190555301` |
| `center/e0` | `T1x` | `-0.0000700717702532314624991441` | `-0.0000273619058300807672167551` | `+0.0000273619058300807672167551` |
| `shell/s_sqrt6` | `E_x` | `-0.0000460804736769278915444017` | `+0.0000163731721029935923155957` | `-0.0000163731721029935923155957` |
| `shell/s_sqrt6` | `T1x` | `-0.0000460804736769278915444017` | `-0.0000328344893188385998612452` | `+0.0000328344893188385998612452` |

The four beta values agree with the tracked step-free double row with max drift
`2.1860303e-16`.

## Affine Assembly

The comparison authority supplies the endpoint support gap used here:

```text
delta_A1(center) - delta_A1(shell) = 1/6.
```

This note consumes that support gap from the comparison authority; it does not
rederive it.

The reduced-shell anchor is also evaluated as a finite algebraic Green
functional:

```text
A = 0.0814354029959012027063775747854
```

It is common to the center and shell endpoints to `1.9943192e-91` in the
90-digit run, so the exact affine endpoint row is

```text
gamma_E(delta) =
  -0.000201057175388665847480882
  + (-0.00105705472620828085655326) delta_A1

gamma_T(delta) =
  +0.00040319674381044349450291
  + (-0.000403209166094501534003488) delta_A1
```

For the requested T-side balance the common anchor cancels:

```text
t_balance =
  |6 (beta_T(center) - beta_T(shell)) / beta_T(shell)|
  = 1.00003080948506836066836856179633336367619961694318329356352.
```

## Recognition

The runner performs bounded recognition checks:

- `nsimplify` with `sqrt(2)`, `sqrt(3)`, `sqrt(6)`, and the natural `pi/7`
  cosine basis returns the high-precision Float, not a closed expression.
- PSLQ finds no minimal-polynomial relation through degree `6` with
  coefficients bounded by `1e7` at tolerance `1e-50`.

So this row does not recognize `|b_T/a_T| - 1` as a rational, a quadratic
surd, or a low-degree algebraic expression in the tested basis. The exact
finite sum is the source-side algebraic representation; compact recognition
remains an open target.

## Caveats

This is exact for the implemented finite object: the `15`-site Dirichlet box,
the fixed active `probe0:xx` branch, the live cubic interpolation contract, and
the finite coordinate tensor stencil. It does not replace that finite
implementation by a continuum tensor calculation, does not change the s3-time
gate status, and does not derive the endpoint triple.

## Reproduction

```bash
python3 scripts/quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=14, FAIL=0
```

Cache regeneration:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
