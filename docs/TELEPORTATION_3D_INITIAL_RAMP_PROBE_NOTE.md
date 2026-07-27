# Teleportation 3D Initial-State And Ramp Probe

**Date:** 2026-04-25
**Status:** open finite diagnostic; not a manuscript claim surface
**Type:** open_gate
**Runner:** `scripts/frontier_teleportation_3d_initial_ramp_probe.py`

The status line records author-side scope only. Independent audit remains the
authority for `audit_status` and `effective_status`.

## Scope

This note records a smallest-surface 3D pressure test for the teleportation
preparation lane. The audited geometry is three spatial lattice directions
plus one finite ramp-time diagnostic direction.

The staggered/Poisson Hamiltonian, `G_target=1000`, ramp schedule, runtime, and
thresholds below are supplied finite-model choices. This note derives no one
of them from the framework axioms. Its claim is only the reproducible outcome
of the listed runner under those choices.

Strict boundary: ordinary quantum state teleportation only. This artifact does
not claim matter transfer, mass transfer, charge transfer, energy transfer,
object transport, or faster-than-light signaling.

## Commands Run

```bash
python3 -m py_compile scripts/frontier_teleportation_3d_initial_ramp_probe.py
python3 scripts/frontier_teleportation_3d_initial_ramp_probe.py
```

Both commands completed successfully.

Default run:

- `dim=3`, `side=2`, `N=8`, two-species Hilbert dimension `64`;
- `mass=0`, `G_target=1000`;
- sampled ramp grid: `21` points in `s in [0, 1]`;
- finite-time ramp: `smoothstep`, `T=40`, `steps=320`, `dt=0.125`;
- resource threshold: best Bell overlap `>= 0.900`;
- target tracking threshold: `|<g_target|psi(T)>|^2 >= 0.990`;
- sampled ramp gap threshold: `>= 1e-3`.
- numerical degeneracy tolerance: `1e-9`.

## G=0 Initial State

The 3D side-2 `G=0` state is spectrally clean and product/separable, but it is
maximally delocalized in the native site basis.

| diagnostic | value |
| --- | ---: |
| single-species `H1` ground energy | `-3.000000` |
| single-species `H1` gap | `2.000000` |
| two-species `H(G=0)` ground energy | `-6.000000` |
| two-species `H(G=0)` degeneracy | `1` |
| two-species `H(G=0)` gap | `2.000000` |
| `|<g_G0 | g_H1 x g_H1>|^2` | `1.000000` |
| `|<g_G0 | uniform x uniform>|^2` | `1.000000` |

Separability diagnostics were numerical rank `1`; Schmidt weights below the
stated `1e-12` entropy tolerance were removed before reporting entropy:

| partition | entropy bits | purity |
| --- | ---: | ---: |
| species A / species B | `0` | `1.000000` |
| logical pair / environment pair | `0` | `1.000000` |
| single `H1` logical / single `H1` environment | `0` | `1.000000` |

The traced logical resource at `G=0` is not an entangled resource:

| quantity | value |
| --- | ---: |
| `Phi+` overlap | `0.500000` |
| best Bell overlap | `0.500000` (`Phi+` / `Psi+` exact tie) |
| best-frame average fidelity | `0.666667` |
| CHSH | `2.000000` |
| negativity | `0.000000` |

The exact product check identifies the reduced logical state as `|++>`. Since
`|++> = (|Phi+> + |Psi+>)/sqrt(2)`, its `Phi+` and `Psi+` overlaps are both
exactly `1/2`; no single Bell label is distinguished at `G=0`.

Native site support:

| state | basis dim | support | PR | `PR/dim` | max probability | site entropy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| single `H1` ground | `8` | `8` | `8.000000` | `1.000000` | `0.125000` | `3.000000` bits |
| two-species `G=0` ground | `64` | `64` | `64.000000` | `1.000000` | `0.015625` | `6.000000` bits |

Initial-state verdict: **unresolved gap**. The state is unique, gapped,
exactly product, and separable, but it is not native-basis localized under the
default `PR/dim <= 0.25` localization threshold.

## Ramp Diagnostics

Null control (`G_target=0`) stayed non-resource throughout the sampled path:

| quantity | value |
| --- | ---: |
| `||dH/ds||_2` | `0` |
| minimum sampled gap | `2.000000` |
| endpoint best Bell overlap | `0.500000` (`Phi+` / `Psi+` exact tie) |
| endpoint best-frame average fidelity | `0.666667` |
| endpoint CHSH | `2.000000` |
| endpoint negativity | `0.000000` |

The 3D Poisson target (`G_target=1000`) produced a high Bell-frame logical
resource on the side-2 lattice:

| `s` | gap | target overlap | best Bell | best frame fidelity | CHSH | negativity | invariant block diagnostic |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `0.000` | `2.000000` | `0.163630` | `0.500000` (`Phi+` / `Psi+` tie) | `0.666667` | `2.000000` | `0.000000` | `6.765823` |
| `0.250` | `0.355996` | `0.950303` | `0.969091` (`Psi+`) | `0.979394` | `2.742398` | `0.469091` | `0.089555` |
| `0.500` | `0.188053` | `0.993598` | `0.991220` (`Psi+`) | `0.994146` | `2.803703` | `0.491220` | `0.014460` |
| `0.750` | `0.126801` | `0.999265` | `0.995993` (`Psi+`) | `0.997329` | `2.817116` | `0.495993` | `0.004522` |
| `1.000` | `0.095490` | `1.000000` | `0.997724` (`Psi+`) | `0.998483` | `2.821998` | `0.497724` | `0.001945` |

Path summary:

- minimum sampled gap: `0.095490` at `s=1.000`;
- target gap: `0.095490`;
- maximum invariant eigenspace-block adiabatic diagnostic: `6.765823` at
  `s=0.000`, from the degenerate block of levels `7-21`, with gap `4.000000`
  and projected coupling norm `108.253175`;
- maximum conservative `||dH||/gap^2`: `3.312934e+04` at `s=1.000`.

The block diagnostic removes an ambiguity in the earlier output. For a
numerically degenerate excited-energy block `B`, the runner now evaluates

```text
A_B(s) = || P_B (dH/ds) |0(s)> ||_2 / Delta_B(s)^2,
```

where `P_B` is the block projector and `Delta_B` is the smallest numerical
gap in the `1e-9` cluster. This quantity is invariant under an arbitrary
orthonormal basis rotation inside `B`; the former maximum over individual
eigenvectors was not. At `s=0`, `108.253175 / 4^2 = 6.765823`. The diagnostic
is still schedule-free planning telemetry, not a runtime/error theorem.

The high-overlap Bell state is `Psi+`, not `Phi+`, so the direct `Phi+`-frame
average fidelity at the endpoint is low (`0.334850`). With the Bell-frame
choice made explicit, the best-frame average fidelity is `0.998483`.

## Finite-Time Diagnostic

The finite-time `smoothstep` ramp with `T=40`, `steps=320` remained close to
the 3D target ground state.

| case | target overlap | diabatic loss | energy excess | best Bell | best-frame fidelity | negativity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| null | `1.000000` | `0` | `0` | `0.500000` (`Phi+` / `Psi+` exact tie) | `0.666667` | `0.000000` |
| Poisson `G=1000` | `0.999954` | `4.578600e-05` | `0.002244` | `0.997444` (`Psi+`) | `0.998296` | `0.497451` |

The Poisson finite-time final state had native site-pair support:

| dim | support | PR | `PR/dim` | max probability | site entropy |
| ---: | ---: | ---: | ---: | ---: | ---: |
| `64` | `64` | `8.123775` | `0.126934` | `0.124043` | `3.077086` bits |

## Verdict

Null control: **clean**.

3D side-2 ramp resource check: **candidate**. The sampled 3D Poisson endpoint
and the finite-time `T=40` ramp both yield a high best-Bell-overlap logical
resource in the `Psi+` frame.

Combined preparation verdict: **unresolved gap**. The side-2 ramp is a useful
3D resource candidate, but the required `G=0` initial state is maximally
delocalized in the native basis and this artifact does not supply a scalable
preparation, control, noise, or readout proof.

## Open-Gate Closure Chain

The runner closes exactly the following finite chain:

1. The null path has `dH/ds=0`, best Bell overlap `0.500000`, negativity `0`,
   and best-frame average fidelity `0.666667`; it therefore fails the resource
   threshold and passes the null-control predicate.
2. The Poisson endpoint has best Bell overlap `0.997724 >= 0.900` and sampled
   minimum gap `0.095490 >= 0.001`. The finite-time final state has target
   overlap `0.999954 >= 0.990` and best Bell overlap `0.997444 >= 0.900`.
   These inequalities pass the runner's finite resource-candidate predicate.
3. The unique, gapped, separable `G=0` ground state has native-basis
   `PR/dim=1.000000 > 0.25`. It therefore fails the stated localization
   predicate even though its product-state checks equal one.

Their conjunction is the citeable open gate: under the supplied side-2 model,
the null is clean and the Poisson ramp is a high-`Psi+`-frame finite resource
candidate, while the tested `G=0` initializer is not native-basis localized.
The closure is deliberately not a scalable preparation theorem, a robustness
or readout theorem, or a claim that no alternative preparation route exists.

## Limitations

- Exact smallest 3D surface only: `side=2`, `N=8`, two-species dimension `64`.
- No `side=4` 3D dense diagonalization or scaling study was attempted.
- The finite-time result is one schedule and one runtime, not a runtime/error
  theorem.
- The conservative norm-bound diagnostic is large (`3.312934e+04`) despite the
  favorable exact finite-time result.
- No bath, cooling, calibration, control-noise, disorder, or readout model is
  included.
- The Bell resource is reported in the best Pauli frame; using the wrong fixed
  `Phi+` frame would not yield the stated fidelity.
- Scope remains ordinary quantum state teleportation only.
