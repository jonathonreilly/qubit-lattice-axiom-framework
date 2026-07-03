# Route-2 Endpoint Active-Branch Eta-Floor Slopes: Step-Free Derivative of the Implemented Max-Abs Envelope

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Implemented finite Route-2 tensor-stencil endpoint observable
only: the active max-abs branch of `eta_floor[1]` at the two endpoint
backgrounds and two source directions named below. The row computes the
step-free active-branch derivative for that implemented envelope; it does not
claim a closed form, continuum tensor limit, exact algebraic endpoint-ratio
identity, or any change to the physical quark endpoint chain.
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:** [scripts/quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py](../scripts/quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py)
**Runner cache:** [logs/runner-cache/quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.txt](../logs/runner-cache/quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.txt)

## Result

For the implemented Route-2 eta-floor observable,

```text
eta_floor[1] = max_probe,max_i,j |G_ij^TF(phi(q))|,
```

the active max entry is unique at both endpoint backgrounds used by
`tensor_endpoint_data()`. It is the same entry in all four endpoint-direction
probes:

```text
probe0:xx = first shell-adjacent probe point, xx trace-free spatial entry
```

The module-step perturbations `q +/- 0.005 v` do not switch the argmax for
either endpoint or either direction. The active-branch derivative is therefore
the ordinary directional derivative of that max-abs branch:

```text
d eta_floor / dt = sign(E*) dE*/dt.
```

With the same anchor normalization as the live endpoint chain, the step-free
active-branch endpoint ratios are:

| quantity | active-branch value |
| --- | ---: |
| `|b_E/b_T|` | `2.621603909613` |
| `|a_T/a_E|` | `2.005383508584` |
| `|b_T/a_T|` | `1.000030809474` |

So the requested active-branch value is:

```text
t_balance = |b_T/a_T| = 1.000030809474
```

This is not a closed-form exact arithmetic claim. It is the source-step-free
derivative of the implemented finite tensor stencil; the remaining numerical
error is floating-point roundoff in the Green-column solve, interpolation, and
tensor assembly. Reassembling the final endpoint ratios with `mpmath` at 30
digits from the double-precision branch derivatives changes the ratios by at
most `4.441e-16`.

## Method

The durable boundary note
[`QUARK_ROUTE2_ETA_FLOOR_HF_BOUNDARY_NOTE.md`](QUARK_ROUTE2_ETA_FLOOR_HF_BOUNDARY_NOTE.md)
showed that the live object is a max-abs trace-free Einstein tensor envelope,
not a spectral floor. The finite-difference provenance note
[`QUARK_ROUTE2_ENDPOINT_T_BALANCE_FD_PROVENANCE_AND_STEP_STABILITY_BOUNDED_NOTE_2026-06-11.md`](QUARK_ROUTE2_ENDPOINT_T_BALANCE_FD_PROVENANCE_AND_STEP_STABILITY_BOUNDED_NOTE_2026-06-11.md)
established that the published endpoint values were central finite-difference
values at `EPS = 0.005`, with the `t_balance` stable band
`[1.0000260, 1.0000319]`.

This runner uses the corrected route for the actual implemented envelope:

- `q -> phi` is differentiated linearly with the existing `G0P @ v` columns.
- The base scalar tensor stencil used for `eta_floor[1]` is differentiated
  through the metric, inverse metric, Christoffels, Ricci tensor, Einstein
  tensor, and trace-free spatial projection.
- The coordinate interpolation and coordinate finite stencil remain part of the
  implemented observable. No finite difference in source amplitude `t` is used
  for the load-bearing slopes.

Live-module pointers consumed read-only:
`scripts/frontier_tensor_support_center_excess_law.py`,
`scripts/frontier_quark_up_amplitude_tensor_endpoint_bridge.py`,
`scripts/frontier_tensorial_einstein_regge_completion.py`,
`scripts/frontier_tensor_boundary_drive_two_channel.py`, and
`scripts/frontier_tensor_universal_kernel.py`.

## Argmax Audit

The active entry is unique at the two endpoint backgrounds. The relative
margin is the gap from the largest absolute entry to the second largest,
divided by the largest absolute entry.

| q | direction | active entry | active abs | second abs | abs gap | relative gap | `q-0.005v` active | `q+0.005v` active |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| `e0` | `E_x` | `probe0:xx` | `7.007177027199e-05` | `3.503588513600e-05` | `3.503588513600e-05` | `5.000000000000e-01` | `probe0:xx` | `probe0:xx` |
| `e0` | `T1x` | `probe0:xx` | `7.007177027199e-05` | `3.503588513600e-05` | `3.503588513600e-05` | `5.000000000000e-01` | `probe0:xx` | `probe0:xx` |
| `s/sqrt(6)` | `E_x` | `probe0:xx` | `4.608047364021e-05` | `3.399500544104e-05` | `1.208546819918e-05` | `2.622687495258e-01` | `probe0:xx` | `probe0:xx` |
| `s/sqrt(6)` | `T1x` | `probe0:xx` | `4.608047364021e-05` | `3.399500544104e-05` | `1.208546819918e-05` | `2.622687495258e-01` | `probe0:xx` | `probe0:xx` |

Top-five entries for the four endpoint-direction probes:

| q | direction | rank | entry | signed value | abs value | `dE/dt` | margin to next |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| `e0` | `E_x` | 1 | `probe0:xx` | `-7.007177027199e-05` | `7.007177027199e-05` | `+3.072011837258e-05` | `3.503588513600e-05` |
| `e0` | `E_x` | 2 | `probe0:yy` | `+3.503588513600e-05` | `3.503588513600e-05` | `-1.536005918629e-05` | `0.000000000000e+00` |
| `e0` | `E_x` | 3 | `probe0:zz` | `+3.503588513600e-05` | `3.503588513600e-05` | `-1.536005918629e-05` | `1.046321897465e-05` |
| `e0` | `E_x` | 4 | `probe1:xy` | `-2.457266616134e-05` | `2.457266616134e-05` | `-8.673792781692e-06` | `0.000000000000e+00` |
| `e0` | `E_x` | 5 | `probe1:yx` | `-2.457266616134e-05` | `2.457266616134e-05` | `-8.822295523490e-06` | `6.815628270627e-06` |
| `e0` | `T1x` | 1 | `probe0:xx` | `-7.007177027199e-05` | `7.007177027199e-05` | `-2.736190582996e-05` | `3.503588513600e-05` |
| `e0` | `T1x` | 2 | `probe0:yy` | `+3.503588513600e-05` | `3.503588513600e-05` | `+1.368095291498e-05` | `0.000000000000e+00` |
| `e0` | `T1x` | 3 | `probe0:zz` | `+3.503588513600e-05` | `3.503588513600e-05` | `+1.368095291498e-05` | `1.046321897465e-05` |
| `e0` | `T1x` | 4 | `probe1:xy` | `-2.457266616134e-05` | `2.457266616134e-05` | `-3.462895251465e-05` | `0.000000000000e+00` |
| `e0` | `T1x` | 5 | `probe1:yx` | `-2.457266616134e-05` | `2.457266616134e-05` | `-3.482260334098e-05` | `6.815628270627e-06` |
| `s/sqrt(6)` | `E_x` | 1 | `probe0:xx` | `-4.608047364021e-05` | `4.608047364021e-05` | `+1.637317210303e-05` | `1.208546819918e-05` |
| `s/sqrt(6)` | `E_x` | 2 | `probe1:xy` | `-3.399500544104e-05` | `3.399500544104e-05` | `-9.182235996104e-06` | `0.000000000000e+00` |
| `s/sqrt(6)` | `E_x` | 3 | `probe1:yx` | `-3.399500544104e-05` | `3.399500544104e-05` | `-9.277713349834e-06` | `1.095476862093e-05` |
| `s/sqrt(6)` | `E_x` | 4 | `probe0:yy` | `+2.304023682011e-05` | `2.304023682011e-05` | `-8.186586051510e-06` | `0.000000000000e+00` |
| `s/sqrt(6)` | `E_x` | 5 | `probe0:zz` | `+2.304023682011e-05` | `2.304023682011e-05` | `-8.186586051517e-06` | `5.355900460560e-06` |
| `s/sqrt(6)` | `T1x` | 1 | `probe0:xx` | `-4.608047364021e-05` | `4.608047364021e-05` | `-3.283448931862e-05` | `1.208546819918e-05` |
| `s/sqrt(6)` | `T1x` | 2 | `probe1:xy` | `-3.399500544104e-05` | `3.399500544104e-05` | `-3.865271323633e-05` | `0.000000000000e+00` |
| `s/sqrt(6)` | `T1x` | 3 | `probe1:yx` | `-3.399500544104e-05` | `3.399500544104e-05` | `-3.876646384396e-05` | `1.095476862093e-05` |
| `s/sqrt(6)` | `T1x` | 4 | `probe0:yy` | `+2.304023682011e-05` | `2.304023682011e-05` | `+1.641724465931e-05` | `0.000000000000e+00` |
| `s/sqrt(6)` | `T1x` | 5 | `probe0:zz` | `+2.304023682011e-05` | `2.304023682011e-05` | `+1.641724465931e-05` | `5.355900460560e-06` |

## Slopes and Endpoint Ratios

The branch derivative of the max-abs observable is `sign(E*) dE*/dt`, so the
active entry signs turn the raw `dE/dt` values into the following endpoint
slopes.

| q | direction | `beta = d eta_floor/dt` | anchor | `gamma = beta/anchor` |
| --- | --- | ---: | ---: | ---: |
| `e0` | `E_x` | `-3.072011837258e-05` | `8.143540299590e-02` | `-3.772329630901e-04` |
| `e0` | `T1x` | `+2.736190582996e-05` | `8.143540299590e-02` | `+3.359952161265e-04` |
| `s/sqrt(6)` | `E_x` | `-1.637317210303e-05` | `8.143540299590e-02` | `-2.010571753891e-04` |
| `s/sqrt(6)` | `T1x` | `+3.283448931862e-05` | `8.143540299590e-02` | `+4.031967438077e-04` |

With `delta_A1(e0) - delta_A1(s/sqrt(6)) = 1/6`, the endpoint affine assembly is:

```text
gamma_E(delta) = -2.010571753891e-04 + (-1.057054726206e-03) delta_A1
gamma_T(delta) = +4.031967438077e-04 + (-4.032091660873e-04) delta_A1
```

The resulting ratios are the values reported above.

## Cross-Checks

The source finite differences at `eps = 1e-3` and `5e-4` are not used to compute
the active-branch slopes. They are only a consistency check. In every
endpoint-direction probe, the one-sided source slopes bracket the step-free
active-branch derivative at both steps.

| q | direction | eps | backward slope | forward slope | central FD | active beta | bracketed |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `e0` | `E_x` | `1e-3` | `-3.073331107777e-05` | `-3.070697787132e-05` | `-3.072014447454e-05` | `-3.072011837258e-05` | yes |
| `e0` | `E_x` | `5e-4` | `-3.072673036841e-05` | `-3.071346218095e-05` | `-3.072009627468e-05` | `-3.072011837258e-05` | yes |
| `e0` | `T1x` | `1e-3` | `+2.734150928695e-05` | `+2.738233044706e-05` | `+2.736191986701e-05` | `+2.736190582996e-05` | yes |
| `e0` | `T1x` | `5e-4` | `+2.735176136046e-05` | `+2.737210664147e-05` | `+2.736193400096e-05` | `+2.736190582996e-05` | yes |
| `s/sqrt(6)` | `E_x` | `1e-3` | `-1.638635401500e-05` | `-1.635998260706e-05` | `-1.637316831103e-05` | `-1.637317210303e-05` | yes |
| `s/sqrt(6)` | `E_x` | `5e-4` | `-1.637977455637e-05` | `-1.636659260780e-05` | `-1.637318358209e-05` | `-1.637317210303e-05` | yes |
| `s/sqrt(6)` | `T1x` | `1e-3` | `+3.281406728053e-05` | `+3.285490012457e-05` | `+3.283448370255e-05` | `+3.283448931862e-05` | yes |
| `s/sqrt(6)` | `T1x` | `5e-4` | `+3.282423784400e-05` | `+3.284480762597e-05` | `+3.283452273498e-05` | `+3.283448931862e-05` | yes |

The largest central-FD difference from the active-branch derivative is
`3.342e-11`. The active-branch `t_balance = 1.000030809474` lies inside the
finite-difference stable band `[1.0000260, 1.0000319]` from the provenance note.

## Caveats and Open Targets

This row replaces the source-amplitude finite difference in the endpoint
slopes with a direct active-branch derivative of the implemented envelope. It
does not claim a closed form for any endpoint ratio, does not change the
implemented finite coordinate stencil into a continuum tensor calculation, and
does not decide the exact algebraic status of the `3e-5` near-miss.

The named open target remains the exact identification of the active-branch
endpoint ratios beyond the current double-precision finite-stencil evaluation.

## Reproduction

```bash
python3 scripts/quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=11, FAIL=0
```

Cache regeneration:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
