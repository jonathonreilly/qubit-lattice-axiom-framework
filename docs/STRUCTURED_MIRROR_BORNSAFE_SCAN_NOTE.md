# Structured Mirror Corrected Born Slice Note

**Date:** 2026-04-03; corrected eight-term repair 2026-07-16
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.

## Claim

For the exact registered 32-configuration structured-mirror slice and the six
canonical seeds per configuration, the supplied fixed-graph strictly linear
propagator gives a corrected three-slit residual

```text
I3 = P(ABC) - P(AB) - P(AC) - P(BC)
     + P(A) + P(B) + P(C) - P(empty)
```

with maximum numerical `|I3|/P(ABC) = 1.816615e-15`. All `192/192`
configured executions are valid, so every configuration has `ok=6`.

Here `P(empty)` is computed by blocking every node in the selected barrier
layer. Every one of the eight terms uses the same detector convention: the
unnormalized sum of `|amplitude|^2` over the final-layer detector nodes.

This finite result reverses the earlier slice-only conclusion. The old
seven-term residual was not a corrected Sorkin statistic on this graph. It
measured the nonzero barrier-bypass background:

```text
legacy I3 = P(empty)
```

up to a maximum normalized floating-point mismatch of `1.776357e-15` over the
registered slice.

## Executable authorities

- **Primary runner:** [`scripts/structured_mirror_bornsafe_sliced_runner_2026_05_09.py`](../scripts/structured_mirror_bornsafe_sliced_runner_2026_05_09.py)
- **Primary runner cache:** [`logs/runner-cache/structured_mirror_bornsafe_sliced_runner_2026_05_09.txt`](../logs/runner-cache/structured_mirror_bornsafe_sliced_runner_2026_05_09.txt)
- **Shared corrected helper and full-grid source:** [`scripts/structured_mirror_bornsafe_scan.py`](../scripts/structured_mirror_bornsafe_scan.py)
- **Structured geometry:** [`scripts/structured_mirror_growth.py`](../scripts/structured_mirror_growth.py)
- **Strictly linear propagator:** [`scripts/mirror_born_audit.py`](../scripts/mirror_born_audit.py)

The graph construction is unchanged. In particular, the two-layer-back edges
remain present and can skip the chosen barrier layer. The repair subtracts
their measured `P(empty)` contribution; it does not silently convert the
geometry into a chokepoint.

## Why the corrected identity cancels

On this fixed forward DAG, a path can bypass the selected barrier layer or pass
through one of the three disjoint open slit groups, but it cannot revisit the
barrier layer. Strict linearity therefore decomposes each detector amplitude
as

```text
D + A + B + C,
```

where `D` is the barrier-bypassing amplitude and `A`, `B`, and `C` are the
three slit-group contributions. Expanding the quadratic detector probability
produces only terms of the form `z_i conjugate(z_j)`. The eight-mask
inclusion-exclusion coefficient of every such term is exactly zero.

The primary runner checks those coefficients as integers. It also checks that
the defective seven-term form leaves only the coefficient of
`D conjugate(D)`, namely `+1`, while a wrong-sign empty-term mutant leaves
coefficient `+2`.

This is the exact mathematical boundary of the cancellation statement:
fixed graph, disjoint barrier apertures, strictly linear amplitude propagation,
and quadratic detector probability. The measured `1e-15`-scale residuals are
finite floating-point evidence, not themselves an exact proof.

## Registered finite results

The registered slice is unchanged: the previously highlighted configuration,
grid corners, center configurations, a near-highlight neighborhood, and the
jittered slice. The seed protocol is unchanged:

```text
3, 10, 17, 24, 31, 38
```

The corrected runner reports:

| Quantity | Corrected finite result |
|---|---:|
| configured executions | `192/192` valid |
| `ok` per configuration | exactly `6` for all `32` |
| maximum corrected `|I3|/P(ABC)` | `1.816615e-15` |
| location of maximum | `N=25, npl_half=20, r=4.5, grid_spacing=1.50, jitter=0.30, seed=17` |
| maximum `|legacy/P - P(empty)/P|` | `1.776357e-15` |
| `d_TV` range over all executions | `[0.03354922, 0.7400326]` |
| `pur_cl` range over all executions | `[0.7141848, 0.9997359]` |
| `S_norm` range over all executions | `[0.0008930359, 0.8629478]` |
| gravity range over all executions | `[-2.734334, 7.563472]` |
| `k=0` gravity-control range | exactly `[0, 0]` in the run |
| configuration means with `pur_cl<0.95` and gravity `>0` | `11/32` |

The old highlighted configuration,
`N=40, npl_half=12, connect_radius=3.0, grid_spacing=1.25,
layer_jitter=0.0`, retains its previously measured ancillary diagnostics:

| Diagnostic | Six-seed mean |
|---|---:|
| corrected `|I3|/P(ABC)` | `7.978e-18` |
| legacy seven-term residual | `8.788e-03` |
| `P(empty)/P(ABC)` | `8.788e-03` |
| `d_TV` | `0.1208` |
| `pur_cl` | `0.9992` |
| gravity | `+0.3811` |

The full cache contains the per-configuration means for all 32 rows.

The `11/32` count is only the result of applying an author-defined finite
diagnostic screen (`mean pur_cl<0.95`, mean gravity `>0`) after correcting the
Born statistic. Neither threshold is derived from the framework or a physical
acceptance criterion. The count is not a claim that decoherence and gravity
physically coexist, is not a successor-lane designation, and does not establish
large-`N`, asymptotic, robustness, or phenomenological closure.

## Hostile controls

The primary runner includes controls designed to fail the old implementation:

1. A deterministic graph with a source-to-detector two-layer bypass has
   `P(empty)/P=1.406342e-01`. The legacy residual has the same value, while the
   corrected residual cancels to `1.095680e-16`.
2. A separately written eight-mask recomputation calls the propagator directly
   for every mask and agrees with the shared helper, with zero probability
   mismatch on the deterministic control.
3. Removing the bypass edge gives exactly `P(empty)=0`; the seven- and
   eight-term forms then agree.
4. A wrong-sign `+P(empty)` mutant produces `|I3|/P=2.812684e-01` and is
   rejected.
5. The integer coefficient check proves the corrected quadratic
   inclusion-exclusion coefficients vanish, while the legacy and mutant
   background coefficients are `1` and `2`.

## Aperture validity

The prior cached run silently skipped seed `38` for five jittered
configurations because the fixed `|y-center|<=2` window contained no middle
slit nodes. A nonempty original aperture remains valid even when it contains
fewer than three nodes, so the helper preserves every originally valid
upper/lower/middle selection exactly.

Only the five originally empty-middle executions invoke the finite-card
fallback:

| Configuration | Seed | Original `(upper, lower, middle)` counts |
|---|---:|---:|
| `(25, 8, 2.5, 1.25, 0.30)` | `38` | `(8, 8, 0)` |
| `(40, 12, 3.0, 1.25, 0.30)` | `38` | `(12, 12, 0)` |
| `(40, 20, 4.5, 1.25, 0.30)` | `38` | `(20, 20, 0)` |
| `(30, 16, 3.5, 1.25, 0.30)` | `38` | `(16, 16, 0)` |
| `(25, 20, 4.5, 1.50, 0.30)` | `38` | `(20, 20, 0)` |

For an empty middle only, the deterministic rule selects the nearest
positive-`y` and nearest negative-`y` barrier nodes as a two-node middle pair
and removes those nodes from the outer groups. This avoids a nearest-three
tie-break that would preferentially move a positive-side node into the middle.
The groups remain disjoint and sign-ordered, and the selector receives no
authority to alter nodes, positions, or graph edges. The runner prints and
hard-gates this exact five-execution inventory, repeats each fallback
measurement to check determinism, and verifies that every non-fallback choice
equals the original threshold selection.

These aperture conventions are load-bearing finite-card inputs: `slit_gap=2`,
at most three nodes retained per aperture after selection, and repository-fixed
seeds `3, 10, 17, 24, 31, 38`. They are not framework-derived continuum
prescriptions.

The registered runner treats a missing slit, zero denominator, NaN,
non-finite diagnostic, or any other invalid seed as a failure. It exits
successfully only when every row has exactly `ok=6`.

## Historical 540-configuration log

[`logs/2026-04-03-structured-mirror-bornsafe-scan.txt`](../logs/2026-04-03-structured-mirror-bornsafe-scan.txt)
is quarantined historical output and now carries a prominent pre-correction
banner. It was produced before the empty-mask repair:

- its column labeled `Born` is the defective seven-term residual;
- its `jitter=0.30` rows commonly report `ok=5`, because seed `38` was skipped;
- its `8.79e-03` and related values are legacy bypass-background readouts;
- it is not evidence for the corrected statistic and is not current support
  for this claim.

The full-grid source now implements the corrected eight-term statistic and
prints corrected, legacy, and empty-mask ratios separately. A corrected
full-grid run was not needed to close this repair, so no new 540-configuration
claim is made here. The durable numerical claim is restricted to the fully
rerun registered `32 x 6` slice.

## Boundaries

This note does not establish:

- a universal derivation of the Born rule;
- an exact result from floating-point cancellation alone;
- a result for nonlinear or layer-normalized propagators;
- corrected exhaustion of the historical 540-configuration grid;
- a structured-mirror successor architecture;
- generalization beyond the exact registered slice and supplied fixed-graph
  linear propagator.
