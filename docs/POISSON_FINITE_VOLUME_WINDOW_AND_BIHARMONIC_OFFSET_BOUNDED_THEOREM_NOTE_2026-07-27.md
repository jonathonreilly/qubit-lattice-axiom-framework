# Finite-volume window dependence and the additive-offset failure of a raw biharmonic exponent fit

**Date:** 2026-07-27; corrected 2026-07-28

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Supplied parent construction:**
[`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)

**Primary runner:**
[`scripts/frontier_poisson_finite_volume_window_and_biharmonic_offset_2026_07_27.py`](../scripts/frontier_poisson_finite_volume_window_and_biharmonic_offset_2026_07_27.py)

## Bounded result

For the exact finite protocols below, the raw log-log exponent estimator is
strongly window- and offset-dependent:

1. On periodic nearest-neighbor `Z^3` lattices with the zero mode removed, a
   fixed radius window `r=4,...,10` gives a Poisson exponent that decreases
   from `2.329` to `1.126` as `N` grows from `32` to `192`, while
   `4 pi r G(r)` at `r=10` increases from `0.190` to `0.855`.
2. On the same finite-volume operator, the scaling window
   `r=max(3,floor(N/16)),...,floor(N/4)` instead gives a stable exponent near
   `1.66`; its outer-edge normalization is near `0.327`, not `1`.
3. The parent construction's raw exponent estimator uses the scaling window
   `r=2,...,N/2-3`. On its own Dirichlet Poisson and biharmonic matrices, for
   `N=16,20,24,32,40`, that estimator assigns the biharmonic profile a score
   closer to the target exponent `1` at every tested size.
4. The periodic biharmonic inverse has a box-size-dependent additive infrared
   offset. Fitting `abs(G_N(r))` directly makes the raw exponent tend toward
   zero, but that does **not** establish a flat potential. The
   constant-shift-invariant chord slope approaches `-1/(8 pi)`, consistent
   with a linear continuum fundamental solution modulo an additive constant.

These are finite computational and analytic diagnostic statements. They do
not recover the parent note's operator-selection claim, establish a
self-consistent localized source, prove a Dirichlet infinite-volume limit, or
compare the full operator family in the parent note.

## Exact supplied protocols

| item | supplied choice |
|---|---|
| lattice operator | nearest-neighbor graph Laplacian |
| periodic inverse | discrete Fourier inverse with the zero mode removed |
| Dirichlet inverse | the parent runner's interior sparse matrix |
| source for Green-function rows | unit point source |
| fixed window | integer radii `4,...,10` |
| scaling window | integer radii `max(3,floor(N/16)),...,floor(N/4)` |
| periodic sizes | `N=32,48,64,96,128,192` |
| Dirichlet sizes | `N=16,20,24,32,40` |

The point source, boundary conditions, finite sizes, and fit windows are
conditions of this bounded result. They are not derived from the framework.

## Finite Poisson window comparison

The runner obtains:

| `N` | 32 | 48 | 64 | 96 | 128 | 192 |
|---:|---:|---:|---:|---:|---:|---:|
| fixed-window `beta` | 2.329 | 1.642 | 1.427 | 1.259 | 1.189 | 1.126 |
| fixed-window `4 pi r G`, `r=10` | 0.190 | 0.432 | 0.568 | 0.709 | 0.782 | 0.855 |

For the scaling window, the last three exponents agree within `0.02` near
`1.66`, while the outer-edge normalization is

| `N` | 96 | 128 | 192 |
|---:|---:|---:|---:|
| `4 pi r G`, `r=N/4` | 0.3269 | 0.3267 | 0.3266 |

The stable finite-volume number is not the continuum target `1`. The result
does not infer an infinite-volume convergence rate from these six sizes; it
shows that the two declared finite estimators give materially different
answers.

## Parent-window finite counterexample

The parent runner defines `mid = N // 2`, samples
`for dy in range(1, mid - 2)`, and fits only radii `r>1`. Its resulting window
is therefore `2,...,N/2-3`.

Applying that exact raw estimator to the parent runner's own Dirichlet
matrices gives:

| `N` | 16 | 20 | 24 | 32 | 40 |
|---:|---:|---:|---:|---:|---:|
| Poisson `beta` | 1.849 | 1.819 | 1.796 | 1.764 | 1.742 |
| biharmonic `beta` | 1.065 | 1.031 | 1.005 | 0.969 | 0.943 |

Thus, on these five finite grids, proximity of this raw exponent to `1` does
not identify the Poisson member even within the two-operator comparison. This
is a counterexample to using that finite score by itself as an
operator-selection certificate. It is not a theorem about every estimator,
every lattice size, or the full family of operators.

## Why the raw biharmonic fit is invalid

Let

```text
lambda(k) = 6 - 2 sum_i cos(k_i)
```

and let the mean-zero periodic biharmonic inverse be

```text
B_N(r) = N^-3 sum_{k != 0} exp(i k.r) / lambda(k)^2.
```

For fixed low Fourier modes, `lambda(k)=|k|^2+O(|k|^4)`. Their contribution
to `B_N(0)` scales as `N^-3 N^4=O(N)`, and the runner directly observes

| `N` | 32 | 48 | 64 | 96 | 128 | 192 |
|---:|---:|---:|---:|---:|---:|---:|
| `B_N(0)/N` | 0.010973 | 0.010854 | 0.010794 | 0.010733 | 0.010702 | 0.010670 |

An additive constant is immaterial to `Delta^2` but dominates a raw
`abs(B_N(r))` fit on a fixed window. A constant-shift-invariant comparison is
the chord slope

```text
[B_N(10)-B_N(4)] / 6.
```

Its normalized magnitude `8 pi abs(slope)` rises monotonically from `0.585`
to `0.938` over the same sizes. The sign is negative.

The standard continuum distribution identities

```text
Delta r = 2/r,
Delta(1/r) = -4 pi delta,
Delta^2[-r/(8 pi)] = delta
```

give the independent sign and factor check. Accordingly, the bounded evidence
is consistent with a linear biharmonic fundamental solution modulo an
additive constant. No lattice asymptotic theorem is claimed here.

## Claim ledger

| ID | bounded claim | direct support | falsifier |
|---|---|---|---|
| P1 | the fixed and scaling Poisson windows give materially different finite results | runner checks 1 and 2 | the two windows agreeing within the declared tolerance |
| P2 | the parent source uses the stated scaling window | source pin in runner check 3 | any pinned source line changing |
| P3 | on the five tested Dirichlet grids, the raw score is closer to `1` for biharmonic than for Poisson | runner check 4 | Poisson scoring at least as close on any tested grid |
| P4 | the periodic biharmonic raw fit is offset-contaminated, while the chord slope tends toward the continuum `-1/(8 pi)` comparator | runner check 5 and the independent distribution identity above | bounded `B_N(0)` or a chord slope inconsistent in sign/trend/factor |

## Imports and support boundary

- **Framework-derived:** only the nearest-neighbor `Z^3` graph structure
  supplied by the registered Lattice axiom.
- **Supplied conditions:** the parent operator definitions, point source,
  boundary conditions, fit windows, and finite lattice sizes.
- **Standard mathematical machinery:** discrete Fourier diagonalization,
  sparse linear solves, and the continuum Poisson/biharmonic distribution
  identities.
- **Computed support:** every table entry is produced by the primary runner.
- **Not present:** measured or fitted physical parameters, observational
  comparators, scale-setting imports, or a new framework primitive.

The continuum identity checks the sign and normalization of the comparator;
it is not promoted into a proof of lattice convergence.

## Negative-claim discipline

The negative boundary is deliberately narrow: the specified raw estimator is
not, by itself, an operator-selection certificate on the tested grids. At
least five distinct routes remain outside this claim:

1. a constant-shift-invariant force or difference estimator;
2. a proved infinite-volume lattice asymptotic;
3. larger Dirichlet grids with a fixed physical window;
4. a susceptibility calculation matched to the point-to-point kernel;
5. a sign-normalized comparison of every member of the parent family; and
6. a nonzero-field self-consistent source construction.

None is declared impossible. There is one finite estimator limitation rather
than multiple independent walls. All boundary conditions and normalizations
are explicit, no prior pull request is used as authority, and no claim is made
that a new axiom or primitive is required. The strongest objection is that a
different invariant estimator or a proved limit could support the parent
conclusion; that objection is left open and is exactly why this note does not
claim parent closure.

## Parent repair target remains open

The current parent-row repair target is:

> missing_bridge_theorem: compare susceptibility with the matched
> point-to-point inverse-Laplacian kernel, normalize alternative-operator
> source signs consistently, and revise the note to the resulting finite
> numerical scope before re-audit.

This bounded note supplies none of those three closure steps. It therefore
does not request parent re-audit or claim that the target is closed. The
parent row remains governed by its existing audit status. This new row, if
landed, remains `unaudited` until the independent audit lane reviews it.

## Explicit non-claims

- No recovery or promotion of the parent claim.
- No uniqueness claim over the parent operator family or over all local
  operators.
- No statement that the biharmonic potential is flat.
- No self-consistency or localized-source theorem.
- No transfer of periodic finite results to a Dirichlet infinite-volume
  theorem.
- No audit verdict or expected audit outcome.
