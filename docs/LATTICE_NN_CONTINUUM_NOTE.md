# Nearest-Neighbor Lattice Refinement Note

**Date:** 2026-04-03  
**Type:** bounded_theorem
**Status:** bounded finite-spacing computational theorem; independent re-audit
required after this source edit

**Claim scope:** raw nearest-neighbor lattice refinement is Born-clean through
`h = 0.25`; `h = 0.125` and the continuum question remain open.

This note freezes the canonical raw nearest-neighbor lattice refinement run.
It is intentionally narrow:

- it does **not** claim a full continuum limit
- it does **not** use fan-out normalization or layer normalization
- it keeps the standard linear propagator only
- it treats `h = 0.125` as an unresolved gate, not as part of the
  finite-spacing window

Artifacts:

- [`scripts/lattice_nn_continuum.py`](../scripts/lattice_nn_continuum.py)
- [`logs/runner-cache/lattice_nn_continuum.txt`](../logs/runner-cache/lattice_nn_continuum.txt)

## Claim Boundary

The load-bearing claim is exactly the finite-window statement

```text
H_finite = {2.0, 1.0, 0.5, 0.25}
```

for the raw nearest-neighbor runner. A row belongs to this window only if the
same harness returns finite values for the gravity, `k=0`, `MI`, classical
purity, total-variation, and Born checks. The next requested spacing,
`h = 0.125`, is a gate row: because the raw runner reports `FAIL (overflow)`,
it is not part of `H_finite` and cannot be used for a continuum or
finer-spacing claim.

## Canonical Finite Window

The raw NN lattice is Born-clean through the last successful spacing:

| `h` | nodes | gravity | `k=0` | `MI` | `1-pur` | `d_TV` | Born |
|---|---:|---:|---:|---:|---:|---:|---:|
| `2.0` | `441` | `-0.775486` | `0.00e+00` | `0.5558` | `0.4215` | `0.7498` | `3.16e-16` |
| `1.0` | `1681` | `-0.116678` | `0.00e+00` | `0.5022` | `0.4229` | `0.7455` | `2.95e-16` |
| `0.5` | `6561` | `+0.138226` | `0.00e+00` | `0.7420` | `0.4844` | `0.9072` | `5.07e-16` |
| `0.25` | `25921` | `+0.077415` | `0.00e+00` | `0.9470` | `0.4989` | `0.9878` | `3.64e-16` |

Safe read:

- gravity flips sign and becomes positive by `h = 0.5`
- the two finest successful rows have `MI = 0.7420, 0.9470`
- the same rows have `1-pur = 0.4844, 0.4989`
- the same rows have `d_TV = 0.9072, 0.9878`
- Born stays at machine precision on the finite window
- `k=0` is exactly zero on every finite-window row

## Bounded Finite-Window Proposition

For the exact constants and functions in the canonical runner, let

```text
R(h) = measure_full(h)
```

and let `finite(R)` mean that each of `gravity`, `k=0`, `MI`, `pur_cl`,
`d_TV`, and `Born` is a finite real number. The runner-backed proposition is

```text
for every h in H_finite:
  finite(R(h))
  and Born(R(h)) < 1e-10
  and k=0(R(h)) = 0

gravity(R(0.5)) > 0 and gravity(R(0.25)) > 0
R(0.125) is unresolved by the raw kernel
```

This is an exhaustive statement about a four-element tested set, not an
induction in `h` and not an asymptotic statement. In particular, “positive”
refers only to the gravity response at the two finest successful rows; it does
not assert monotonicity of gravity or of any other observable.

## Finite-Window Derivation Chain

The closure is computational and bounded, not asymptotic:

1. `generate_nn_lattice(h)` fixes the raw family: each interior node has the
   same three forward nearest-neighbor edges, with physical `W`, `L`, slit
   location, mass location, `K_PHYS`, `BETA`, and `LAM` held fixed by the
   runner.
2. `measure_full(h)` applies the same propagator and observable definitions to
   every requested spacing. No row in `H_finite` uses fan-out normalization, layer
   normalization, a fitted selector, or an observed target value.
3. `certify_finite_window(rows)` makes the proof obligations executable. For
   every `h` in `H_finite`, it requires all six reported observables to be
   finite, `k=0 = 0` exactly, and Born residual `< 1e-10`; it also requires
   positive gravity on `h = 0.5, 0.25`. Any violation makes the runner exit
   nonzero instead of printing a successful certificate.
4. The cached run passes that certificate. Its worst finite-window Born
   residual is `5.07e-16`, and all displayed `k=0` responses are zero.
5. The positive statement is therefore only the finite-row sign check shown
   in the table: the rows `h = 0.5` and `h = 0.25` have positive gravity
   response. The displayed `MI`, `1-pur`, and `d_TV` values are finite-row
   diagnostics, not evidence for monotone or asymptotic limits.
6. The same certificate requires the raw runner to report `FAIL (overflow)`
   at `h = 0.125`. That failure blocks
   extending the window, so the derivation stops at `H_finite` and leaves the
   continuum question open.

Thus the auditable implication is:

```text
raw NN harness + finite runner rows through h = 0.25
  => Born-clean finite-spacing refinement window H_finite
raw NN harness + FAIL at h = 0.125
  => open finer-spacing/continuum gate
```

## Unresolved Point

The raw kernel overflows at `h = 0.125` in the canonical run.

That means:

- the finite-window certificate passes on the four stated rows
- the next finer point is not yet frozen
- a full continuum claim is not review-safe yet

## Safe Conclusion

The correct wording is:

- the nearest-neighbor lattice has a **Born-clean finite tested window through
  `h = 0.25`**, with positive gravity on its two finest successful rows
- the raw kernel **overflows at the next tested spacing `h = 0.125`**
- the continuum question remains open

Do **not** promote this note to a full continuum theorem.

The audit ledger, not this note, decides whether the edited bounded packet is
effectively `retained_bounded` after independent re-audit.
