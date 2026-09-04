# Bounded diagnosis of the self-consistent beta finite-size caveat

**Date:** 2026-07-26; narrowed by review-loop 2026-07-28
**Type:** bounded_theorem
**Status:** bounded diagnostic proposed for independent audit; not an audit verdict
**Parent construction:** [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
**Primary runner:** [`scripts/physical_poisson_self_consistent_beta_caveat_bounded_diagnostic_2026_07_26.py`](../scripts/physical_poisson_self_consistent_beta_caveat_bounded_diagnostic_2026_07_26.py)

## Exact bounded result

For the parent transfer-propagator implementation at
`k=5.0`, `G=0.5`, `sigma=2.0`, mixing `0.3`, tolerance `10^-4`, and
`N in {16,20,24,28,32,40,48}`:

1. all 21 Poisson, biharmonic, and local fixed-point runs used below converge;
2. the two declared least-squares models for the finite Poisson `beta` table,
   `b_inf+c/N` and `b_inf+c/N+d/N^2`, give intercepts `1.2747` and
   `1.1578`, not the caveat's displayed target `1.0`;
3. the two models disagree on the asymptotic Poisson-versus-biharmonic ranking,
   so these fits do not determine such a ranking;
4. every converged propagated density has exactly uniform x-layer mass `1/N`,
   and therefore x-direction RMS extent
   `sqrt((N^2+2)/12)` for the even sizes used here;
5. the parent's `beta` fit includes radii through the source interior rather
   than using a source-exterior-only window; and
6. the script cited by the caveat computes ray deflection in a prescribed
   `f=s/r` field, not the self-consistent field's raw `beta`.

The specific sentence claiming that the cited distance-law script demonstrates
continuum convergence of this self-consistent `beta` is therefore unsupported
by that script and is withdrawn in the parent note. This result does **not**
prove that every continuum construction, source prescription, fit window, or
extrapolation family fails.

## The exact layer-marginal obstruction

The load-bearing statement is visible directly in the parent propagator. It
normalizes the two-dimensional wavefunction on each x-layer before recording
that layer's density. It records each of the `N` layers exactly once and then
normalizes the full three-dimensional density. Hence, whenever the propagated
layer norms are nonzero,

```text
sum_{y,z} rho(x,y,z) = 1/N
```

for every x-layer, independently of `phi`. For even `N` with source coordinate
`N/2`,

```text
RMS_x^2
  = (1/N) sum_{x=0}^{N-1} (x-N/2)^2
  = (N^2+2)/12.
```

Thus this particular propagated density spans the full box in x. Increasing
`N` in the parent protocol does not turn it into a fixed-extent three-dimensional
point source. This is an implementation theorem, not a claim about a modified
propagator or a source normalized only once globally.

The runner confirms the identity on every converged Poisson density:

| N | 16 | 20 | 24 | 28 | 32 | 40 | 48 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `RMS_x` | 4.637 | 5.788 | 6.940 | 8.093 | 9.247 | 11.554 | 13.862 |
| max `abs(layer mass-1/N)` | `2.8e-17` | `1.4e-17` | `2.1e-17` | `1.4e-17` | `1.4e-17` | `6.9e-18` | `1.0e-17` |

## Finite beta tables

The parent raw estimator fits the field along one axis at radii
`2,...,N/2-3`. The runner obtains:

| N | 16 | 20 | 24 | 28 | 32 | 40 | 48 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Poisson `beta` | 1.2509 | 1.2799 | 1.2861 | 1.2843 | 1.2795 | 1.2672 | 1.2550 |
| Poisson `R^2` | 0.9490 | 0.9240 | 0.9063 | 0.8920 | 0.8799 | 0.8602 | 0.8446 |
| biharmonic `beta` | 0.8830 | 0.8762 | 0.8669 | 0.8573 | 0.8482 | 0.8319 | 0.8182 |
| biharmonic `R^2` | 0.9117 | 0.8556 | 0.8152 | 0.7840 | 0.7588 | 0.7200 | 0.6910 |

For Poisson:

| descriptive model | fitted intercept | OLS standard error under that model |
|---|---:|---:|
| `b_inf+c/N` | 1.2747 | 0.0177 |
| `b_inf+c/N+d/N^2` | 1.1578 | 0.0012 |

These are descriptive fits of seven finite values, not a proof that either
ansatz is the asymptotic expansion. From `N=24` to `N=48`, Poisson `beta`
changes by `-0.0311`; the original branch reported the sign backwards.

The difference

```text
abs(beta_poisson-1) - abs(beta_biharmonic-1)
```

is positive on all seven tested grids but decreases from `0.1562` at `N=20`
to `0.0732` at `N=48`. Its fitted intercept is `+0.0706` under the linear
`1/N` model and `-0.1040` under the quadratic model. The selected fits
therefore do not decide one continuum ranking.

## Fit-window relation to the converged source

The fit uses radii `2,...,N/2-3`. At its outer radius, the fraction of the
converged Poisson density enclosed in the corresponding ball is:

| N | 16 | 20 | 24 | 28 | 32 | 40 | 48 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| outer fit radius | 5 | 7 | 9 | 11 | 13 | 17 | 21 |
| enclosed source fraction | 0.5067 | 0.6160 | 0.6840 | 0.7307 | 0.7643 | 0.8117 | 0.8449 |

This is not a source-exterior-only fit. More exactly, the uniform x-layer
marginal puts at least five complete layers, with total mass `5/N`, beyond the
outer fit radius for every listed even `N`. It does not imply that the field
has no exterior; it shows only that the parent diagnostic mixes source-interior
and outer radii.

## Cited-observable mismatch

The caveat cites `scripts/frontier_distance_law_definitive.py`. That script
states the convention

```text
deflection delta(b) ~ 1/b^alpha
```

and cross-checks a prescribed point-source field `f=s/r`. It neither imports
the parent construction nor calls its `check_field_physics` beta estimator.
A future theorem could bridge the two observables, but the cited script itself
is not that bridge.

## Claim ledger

| ID | bounded claim | support | boundary |
|---|---|---|---|
| P0 | the imported parent runner matches the reviewed SHA-256 | runner P0 | source-hash pin only |
| P1 | all 21 table-producing fixed points converge | runner P1 | declared sizes and tolerance |
| S1 | the two selected Poisson fits have intercepts above `1.1` | runner S1 | no exhaustive extrapolation claim |
| S2 | biharmonic `abs(beta-1)` increases across the tested sizes | runner S2 | finite monotone table only |
| S3 | the two selected ranking fits disagree in sign | runner S3 | no claim about other fit families |
| S4 | single-power-law `R^2` decreases across the tested sizes for both matrix operators | runner S4 | no asymptotic inference |
| S5 | the converged Poisson densities have exact uniform x-layer mass and the stated x-RMS | analytic identity plus runner S5 | parent propagator only |
| S6 | the declared fit is not source-exterior-only | runner S6 | does not deny a field exterior |
| S7 | the cited script computes a different observable in a prescribed field | source inspection plus runner S7 | a future bridge remains open |
| S8 | local-operator beta stays farther than `4` from `1` on the tested sizes | runner S8 | no divergence or limit claim |

## Imports and support boundary

- **Supplied construction:** the parent transfer propagator, operator menu,
  parameters, Dirichlet boundary, finite sizes, and raw beta estimator.
- **Explicit comparison convention:** the point-source response sign is chosen
  once per operator before the fixed-point run.
- **Standard machinery:** sparse LU, least squares, and finite sums.
- **Computed support:** every table entry is produced by the primary runner.
- **Not used:** measured constants, fitted observations, a selector, a new
  framework axiom, or a framework primitive.

The primitive-registry check finds no relevant approved primitive: none grants
a field operator, source normalization, beta estimator, or observable bridge.

## No-Go Discipline N1-N8

The original `no_go` framing failed N5 and N7 because it inferred a universal
nonlocalization/continuum failure from finite data and left fixed-source and
alternative-fit routes open. Review-loop demoted it to the bounded statements
above. The remaining negative implication is only that the **existing cited
script and parent protocol do not establish the caveat's claimed continuum
bridge**.

### N1 — Alternative routes

| route family | marker | result |
|---|---|---|
| citation/observable inspection | ATTEMPTED | the cited script computes deflection in prescribed `f=s/r`, not the parent beta |
| exact algorithmic invariant | ATTEMPTED | per-layer normalization gives x-layer mass `1/N` for every propagated density |
| fixed-point validity | ATTEMPTED | all 21 fields used in the tables converge at the declared tolerance |
| statistical-model sensitivity | ATTEMPTED | the two declared extrapolation families disagree on the operator ranking |
| source/window geometry | ATTEMPTED | the beta fit includes source-interior radii on every tested converged Poisson density |
| alternative-operator table | ATTEMPTED | biharmonic and local finite sequences were computed rather than inferred |

These routes differ in object, mechanism, and terminal obligation. None is used
to claim that a modified source, window, observable bridge, or fit family fails.

### N2 — Wall independence

The collapsed result has two independent facts: W1, the cited-observable
mismatch; and W2, the exact uniform x-layer marginal. The finite fit and window
tables diagnose consequences of the implemented protocol and are not counted
as extra independent walls.

### N3 — Hidden-wall scan

The supplied parameters, boundary condition, source-sign convention, fit
families, estimator, and finite sizes are explicit. “Exact” refers only to the
layer-normalization identity. “Continuum” appears only in the quoted caveat or
in explicit non-claims.

### N4 — Residual matching

The only authority under correction is the linked parent note's finite-size
caveat. The cited distance-law script is inspected directly. No open pull
request, predecessor cycle, or unaudited sibling is used as authority.

### N5 — Rhetoric audit

The numerical statements are per listed size and operator. The layer identity
holds per x-layer and for every nonzero propagated layer under this
implementation. No statement is made for a modified propagator, every
extrapolation family, or an infinite-volume physical field.

### N6 — Partial-closure paths

A fixed localized source, a source-exterior fit, or a theorem bridging the
deflection and beta observables could support a repaired parent statement.
Those are ordinary construction/bridge routes, not requests for a new axiom or
primitive.

### N7 — Steelman

The strongest objection is that another extrapolation family or a fixed-source
observable could approach `beta=1`, and a derived bridge could make the
distance-law calculation relevant. That objection lands. It defeats the
original universal no-go, which is why this note keeps only the exact parent-code
invariant, finite tables, and current citation mismatch. It does not defeat the
claim that the existing citation does not perform the needed computation.

### N8 — Cross-cycle echo

Current-main finite-volume work already shows strong beta-window and additive
offset sensitivity, while separate self-consistent well-depth work uses a
different eigenstate-density source and explicitly does not close the parent
transfer-propagator bridge. Those routes reinforce the need for narrow scope;
neither retires the exact layer-marginal or citation-mismatch findings here.

**No-Go Discipline result:** the original broad `no_go` fails; the demoted
bounded diagnostic passes with all stronger repair routes left open.

## Parent repair and audit boundary

The parent row's current repair target remains:

> missing_bridge_theorem: compare susceptibility with the matched point-to-point
> inverse-Laplacian kernel, normalize alternative-operator source signs
> consistently, and revise the note to the resulting finite numerical scope
> before re-audit.

This landing corrects the finite-size caveat and creates source hash drift so
the parent can re-enter independent review. It does not supply the missing
susceptibility bridge or close the full repair target. Review-loop applies no
audit verdict.

## Verification

```bash
python3 scripts/physical_poisson_self_consistent_beta_caveat_bounded_diagnostic_2026_07_26.py
```

Expected result: `TOTAL: 10 PASS / 0 FAIL`.
