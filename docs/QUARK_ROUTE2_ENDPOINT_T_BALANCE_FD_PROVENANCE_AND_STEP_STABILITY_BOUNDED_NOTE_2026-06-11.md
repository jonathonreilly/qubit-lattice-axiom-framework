# Endpoint `t_balance` Near-Miss: Finite-Difference Provenance and Step-Stability

**Date:** 2026-06-11
**Type:** bounded_theorem
**Claim scope:** Three bounded statements about the live Route-2
support-tensor endpoint readout ratios, all verified by the primary runner
on the current live modules. (P1, provenance) The current live
endpoint-resolution runner values
`|b_E/b_T| = 2.621602843782`, `|a_T/a_E| = 2.005383530819`,
`|b_T/a_T| = 1.000030814262` are central-finite-difference values of the
eta-floor chain at the module derivative step `EPS = 0.005`; the runner
reproduces all three to the printed digits (worst residual `3.6e-13`) by
re-running the live chain at that step. (P2, step-stability) The
`t_balance` near-miss `|b_T/a_T| - 1 ≈ 3.1e-5` is not explained by the
tested `O(eps^2)` finite-difference truncation model: over the stable step window
`eps ∈ [2e-4, 2e-3]` the value stays inside the narrow band
`[1.0000274, 1.0000317]`, Richardson extrapolation (which cancels the
leading `O(eps^2)` term in the smooth-error model) stays inside
`[1.0000259, 1.0000319]`, and the raw stable-window band excludes
`1` by more than six times the observed window spread (`2.74e-5` vs
`4.3e-6`). (P3, noise floor) Below `eps ≈ 1e-4` the central differences
leave the band at the `1e-4` scale — the chain's internal noise floor —
which bounds the honest precision of any finite-difference statement about
these ratios. No exact symbolic value for any ratio is claimed; no
endpoint-triple derivation is claimed; the parent gate is untouched.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:** [`scripts/quark_route2_endpoint_t_balance_fd_provenance_step_stability_2026_06_11.py`](../scripts/quark_route2_endpoint_t_balance_fd_provenance_step_stability_2026_06_11.py)
**Runner cache:** [`logs/runner-cache/quark_route2_endpoint_t_balance_fd_provenance_step_stability_2026_06_11.txt`](../logs/runner-cache/quark_route2_endpoint_t_balance_fd_provenance_step_stability_2026_06_11.txt)

## Question

The endpoint-resolution row
([`QUARK_UP_AMPLITUDE_TENSOR_ENDPOINT_RESOLUTION_NOTE_2026-04-19.md`](QUARK_UP_AMPLITUDE_TENSOR_ENDPOINT_RESOLUTION_NOTE_2026-04-19.md),
Stage A) names the live endpoint readout ratios, and its current runner
produces the `t_balance` value `1.000030814262`. That value has stood as a near-miss of the
not-yet-derived endpoint-triple magnitude `1` (the `(−1, −2, 21/4)` readout
target named by the s3-time gate; plain-text context pointer:
`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`). Under the repo's
no-coincidences discipline, the first question about a `3e-5` near-miss is
mundane: is it real structure of the live surface, or numerical error of
the chain that produced it?

This note answers the error half of that question. Two facts about the
live chain make it non-trivial:

1. the slopes `beta_E`, `beta_T` entering the ratios are computed by
   CENTRAL FINITE DIFFERENCES of the eta-floor functional at the module
   step `EPS = 0.005` (`gamma_pair` in
   `scripts/frontier_tensor_support_center_excess_law.py`, plain-text
   pointer) — so every current live ratio inherits an `O(eps^2)` truncation
   error of a priori size comparable to `3e-5`;
2. the eta floor itself is evaluated through a `15³` Green-function solve
   and a spectral-floor extraction
   (`scripts/frontier_tensor_boundary_drive_two_channel.py`, plain-text
   pointer), so the chain has an internal noise floor that small steps
   amplify.

A `3e-5` near-miss produced at a step whose truncation error is naturally
`O(2.5e-5)` could have been pure derivative-step artifact. The runner
tests exactly that.

## Result

### (P1) Provenance

Re-running the live chain (same probe vectors `e0`, `s/√6`,
`ex = (√3·e1 + e2)/2`, `t1x`; same two-point affine endpoint law; same
anchor normalization) at the module step `EPS = 0.005` reproduces all
three current live endpoint-resolution runner ratios with worst residual
`3.6e-13`. These values are therefore identified as finite-difference values at
that specific step — not exact algebraic numbers of the surface.

### (P2) Step-stability: the near-miss survives

| `eps` | `\|b_E/b_T\|` | `\|a_T/a_E\|` | `\|b_T/a_T\|` |
| --- | --- | --- | --- |
| `2e-3` | `2.621602450715` | `2.005382281415` | `1.000031700607` |
| `1e-3` | `2.621618786852` | `2.005383630023` | `1.000027389214` |
| `5e-4` | `2.621595261381` | `2.005384143552` | `1.000030750230` |
| `2e-4` | `2.621583528384` | `2.005399375554` | `1.000030438902` |

Richardson extrapolants (leading `O(eps^2)` cancellation in the smooth-error model):
`1.000025952084` (from `eps = 2e-3`) and `1.000031870569` (from
`eps = 1e-3`). Everything stays inside `[1.0000259, 1.0000319]`.

The gap to `1` (`≥ 2.74e-5`) exceeds the full observed window spread
(`4.3e-6`) by more than a factor of six. If the near-miss were explained
by the tested leading `O(eps^2)` truncation model, it would shrink by `100×`
from `eps = 2e-3` to `eps = 2e-4` and the Richardson values would collapse
toward `1`; neither happens. The same table shows the second near-miss axis
`|a_T/a_E| − 2 ≈ 5.4e-3` is step-stable as well.

### (P3) Noise floor

At `eps = 1e-4` and `5e-5` the values leave the band at the `1e-4` scale
(`0.999941`, `0.999996`): the chain's internal evaluation noise dominates
central differences below `eps ≈ 1e-4`. The honest finite-difference
statement is therefore bounded by the stable-window band above; pushing
`eps` smaller cannot sharpen it.

## What this does and does not establish

- ESTABLISHED: the live-surface `t_balance` differs from `1` by
  `(2.7–3.2)e-5` as a step-stable property of the finite-difference
  chain; the tested derivative-step-error explanation does not account for
  the near-miss, so the no-coincidences question about it remains live.
- ESTABLISHED: the current live 12-digit endpoint constants are
  step-`0.005` finite-difference values, not exact surface constants;
  downstream consumers quoting more than ~5 stable digits of them are
  quoting step-specific digits.
- NOT established: any exact symbolic value of the ratios. The named
  route to the exact slope is the spectral-floor envelope
  (Hellmann–Feynman) derivative of the eta-floor functional — derivative
  of a simple floor eigenvalue evaluated as the expectation of the
  perturbed operator in the floor eigenvector — which would replace
  finite differences entirely. That derivation, and the exact algebraic
  status of `|b_T/a_T| − 1`, remain the open targets here.
- NOT established / not touched: the endpoint-triple derivation, the
  s3-time gate status, or any demotion of the `(−1, −2, 21/4)` readout
  target. The existing no-go on deriving the triple inside the restricted bright readout class
  ([`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md))
  is unaffected.

## Consequence for the T-side question (bounded)

The candidate reading "the live surface's `t_balance` is exactly `1` and
the `3e-5` is only the tested finite-difference step error" is excluded by
this bounded finite-difference test at the chain's own precision: the deviation is step-stable and an order of
magnitude above the observed jitter. What remains open is which exact algebraic number the live
surface assigns to `|b_T/a_T|` — the envelope-derivative computation is
the named next step, and only it can decide whether the deviation has a
closed form in the surface's atom algebra.

## Reproduction

```bash
python3 scripts/quark_route2_endpoint_t_balance_fd_provenance_step_stability_2026_06_11.py
```

Expected: `TOTAL: PASS=7, FAIL=0` with the tables above.
