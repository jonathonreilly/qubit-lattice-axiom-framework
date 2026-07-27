# Gauge-Vacuum Plaquette First-Sector Completed Triple Sampled-Grid Boundary

**Date:** 2026-04-19 (originally); 2026-05-03 (dense-grid certificate
added); 2026-05-10 (scope narrowed); 2026-05-16 (continuous-box Lipschitz
certificate added); 2026-05-27 (finite-grid scope repair); 2026-07-27
(numerical predicate and No-Go Discipline packet completed)
**Type:** no_go
**Claim type:** no_go
**Status:** finite numerical no-go on the explicit sampled runner surface;
independent re-audit required
**Primary runner:** [`scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py`](../scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py)
**Cached output:** [`logs/runner-cache/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.txt`](../logs/runner-cache/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.txt)
**Companion runner:** [`scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py`](../scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py)

## Scope Repair

The continuous-box version of this row depended on empirical 2.5x
sampled-gradient Lipschitz constants. Finite gradient sampling does not
certify a global Lipschitz bound over the whole continuous parameter box.

This repair removes the continuous-box no-go from the binding claim. The row
now claims only the exhaustive finite numerical predicate supported by the
primary dense runner: all 1440 returned float64 gaps are finite and exceed the
declared numerical-zero threshold `10^-6`.

No new axiom, analytic Lipschitz theorem, or interval-arithmetic certificate is
introduced.

## No-Go Discipline Gate

This gate is `PASS` only for the finite runner predicate stated below. It is
`FAIL` for an exact-arithmetic or unconditional continuous-family no-go, and
neither stronger claim ships here.

### N1 — five distinct attacks on the finite numerical no-go

| Attack route | Canonical route class | Marker | Concrete falsifier | Why it fails on the claimed surface |
|---|---|---|---|---|
| Direct counterexample search over parameter tuples | `numerical_or_finite_case` | `ATTEMPTED` | Find one of the stated Cartesian tuples whose returned gap is non-finite or at most `10^-6`. | The primary runner performs the finite numerical scan over all `6 x 6 x 5 x 8 = 1440` unique tuples; the minimum is `7.791551... x 10^-3`. |
| Optimal-scalar escape | `algebraic_rearrangement` | `ATTEMPTED` | Show by algebra or direct solution that a different scalar `c` makes a sampled witness realize the target. | `gap_at` uses the least-squares identity `c_best=(Zhat·Zmin)/(Zhat·Zhat)`, and the runner checks the algebraic projection identity `Zhat·(c_best Zhat-Zmin)=0` at every tuple to `10^-12`. |
| Grid-boundary definition escape | `boundary_or_initial_condition` | `ATTEMPTED` | Show that a listed boundary endpoint, Cartesian combination, or grid point was skipped or duplicated. | The runner checks the four boundary-endpoint pairs, total cardinality, and uniqueness of the complete Cartesian product before accepting the result. |
| Target-readout drift escape | `alternate_observable_or_readout` | `ATTEMPTED` | Show that the sweep used an alternate target readout rather than the completed triple printed in this note. | The target readout is rebuilt by `completed_sector_data()` and checked componentwise against the listed triple to `10^-12`; the companion runner independently checks the same upstream reconstruction. |
| Dependency/provenance escape | `dependency_or_registry_reclassification` | `ATTEMPTED` | Show that an undeclared mutable premise or stale runner output supplied the reported minimum. | The runner checks its dependency manifest names the note and all three helper runners; the cache fingerprint covers those premises, while `min_gap`/`min_pt` are selected from freshly computed gaps before regression comparison. |

These routes differ in primary object and terminal falsifier: evaluated tuple,
scalar projection, domain enumeration, target vector, and execution provenance.
Off-grid minimizers and alternate transfer families are not counted among the
five because they attack stronger claims that this note explicitly does not
make.

### N2 — wall-independence audit

The finite predicate has no named open wall: its domain, evaluator, target,
threshold, and quantifier are all part of the claim contract and are checked.
Therefore there is no pairwise wall table to inflate. An exact-arithmetic
certificate and a continuous-box certificate are two stronger successor
targets, not independent walls hidden inside this claim.

### N3 — hidden-wall scan

The proof and runner were scanned for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.
There is no load-bearing hit. Uses of "box" describe only the bounds from
which the explicit grids are generated. Uses of "continuous" occur only in
scope exclusions. "Canonical" labels the audit gate's route-class column and
is non-load-bearing. No hidden condition is promoted to a wall.

### N4 — residual matching

No prior no-go is used as a witness. The only load-bearing residual is the
freshly computed numerical predicate

```text
min_{p in G_1440} gap_at_float64(p) > 10^-6.
```

The older boundary-face diagnostic and empirical continuous-box Lipschitz
runner address different residuals and are explicitly non-load-bearing.

### N5 — rhetoric audit

The tested resolution is one whole parameter tuple at each point of the
finite grid. Per-site, per-mode, per-block, lattice-wide, exact-arithmetic,
and continuous-parameter resolutions are not tested and are not claimed.
Accordingly the conclusion is always qualified as an "explicit sampled
runner surface" or "finite numerical predicate", never as a no-go for the
continuous family or the full framework packet.

### N6 — partial-closure paths

The stronger continuous target remains approachable through analytic
derivative/operator bounds, interval arithmetic, a proof-producing global
optimizer, or an analytic monotonicity theorem. Those are ordinary theorem or
certificate routes, not new axioms or primitives. None is needed for the
finite predicate and none is silently imported into it.

### N7 — steelman

A hostile reviewer should object that float64 evaluation with a declared
threshold cannot prove exact non-equality of the underlying real-valued
function, and that a finite grid cannot exclude an off-grid zero. That is the
strongest objection to the earlier wording, but it does not refute the present
claim: the present quantified object is exactly the runner's 1440 float64
outputs and its explicit `10^-6` predicate. The exact-arithmetic and
continuous-family conclusions are both disclaimed. Thus no concrete unclosed
mechanism remains against the claim that actually ships.

### N8 — cross-cycle echo

The structurally similar prior failure was this note's own empirical
continuous-Lipschitz extension: sampled gradients were overread as a global
bound. The successful retirement mechanism was claim separation, not a new
axiom. The same mechanism is applied here by keeping the archived continuous
runner as scouting only and binding this row solely to the finite numerical
predicate.

**No-Go Discipline result:** `PASS` for the finite sampled runner predicate;
`FAIL` for any exact-arithmetic or continuous-family extrapolation.

## Claim

On the explicit `1440`-point dense grid covering the listed parameter box

```text
tau_transfer  in [10^-4, 5e-2]   (6 log-spaced points)
tau_boundary  in [0.5, 4.0]      (6 linearly-spaced points)
asym_decay    in [10^-8, 10^-4]  (5 log-spaced points)
linear_decay  in [0.05, 1.0]     (8 linearly-spaced points)
```

at the explicit `beta = 6` `spatial_pair` witness, every float64 result
returned by `gap_at` after its analytic optimal-scalar fit is finite and
greater than the declared numerical-zero threshold `10^-6` for the completed
first-sector target

```text
Z^min = (0.135165279562..., 0.374012880009..., 0.543843858544...).
```

The minimum runner-evaluated gap is

```text
||c_best Z^hat_best - Z^min||_2 = 7.791551e-03,
```

attained at the sampled grid point

```text
(tau_transfer = 1e-4, tau_boundary = 4.0, asym_decay = 1e-8, linear_decay = 0.3214).
```

This is a finite numerical sampled-grid no-go. It is neither an
exact-arithmetic equality theorem at those coordinates nor a
continuous-parameter exclusion theorem.

Equivalently, under this declared numerical predicate, no sampled grid point
realizes the completed first-sector triple; this is a finite sampled-grid no-go
in that numerical sense only.

## Evidence

The primary runner exhaustively evaluates the listed finite grid and reports:

```text
swept 1440 grid points
  minimum runner-evaluated gap = 7.791551e-03
  median gap                  = 2.039034e-01
  max gap                     = 2.856130e-01
  minimum / numerical-zero threshold = 7791.551
argmin grid point:
  tau_transfer = 1.0000e-04
  tau_boundary = 4.0000
  asym_decay   = 1.0000e-08
  linear_decay = 0.3214
```

The older boundary-face reference fit is not load-bearing for this repaired
row, because its optimized `linear_decay` value is not the sampled-grid
minimizer. The finite-grid claim uses the runner's reported `min gap` over the
listed 1440 sampled points.

## What This Claims

- A finite numerical no-go on the stated `6 x 6 x 5 x 8 = 1440` sampled
  grid, using the primary runner's float64 evaluator and `10^-6`
  numerical-zero threshold.
- The sampled-grid argmin and positive sampled minimum gap reported by the
  primary runner.
- The sampled-grid result is scoped only to the explicit `beta = 6`
  `spatial_pair` witness family, explicit `Z^min`, and optimal scalar fit
  routine used by `gap_at`.

## What This Does Not Claim

- It does not prove a continuous-box no-go over unsampled parameter values.
- It does not prove exact real-arithmetic non-equality even at the sampled
  coordinates.
- It does not certify analytic or interval Lipschitz constants.
- It does not prove the sampled argmin is the true continuous minimum.
- It does not rule out a smaller gap or exact realization between grid points.
- It does not close the full framework-point packet.
- It does not add a new axiom.

## Future Work

Upgrading beyond sampled-grid scope requires one of:

- interval arithmetic over `gap_at` on the full continuous box;
- analytic operator-norm/subspace Lipschitz bounds tight enough to certify a
  positive lower bound;
- a deterministic global optimizer with a proof-level certificate; or
- an analytic monotonicity/global-minimum theorem.

The archived empirical continuous-box Lipschitz runner may remain useful as a
scouting artifact, but it is not load-bearing for this repaired row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py
```

Expected:

```text
gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03  SUMMARY: PASS=6, FAIL=0
```

Optional companion context:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py
```
