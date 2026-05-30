# g_bare = 1 Dynamical Fixation L=4 Detector Obstruction

**Date:** 2026-04-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; this source note does not
set its own retained status.
**Primary runner:** `scripts/frontier_g_bare_critical_feature_scan.py`

## Claim

On the completed `L = 4`, `L_t = 4` Wilson-SU(3) + staggered-fermion scan,
none of the six registered framework-native scalar detectors gives a
localized, detector-loud non-smooth feature at `beta = 6` (`g_bare = 1`).

The retained-safe consequence is narrow:

> The completed L=4 detector surface does not provide a dynamical critical
> feature that fixes `g_bare = 1`.

This note does **not** claim a lattice-size-converged obstruction, an L=6
persistence result, or global closure of every Path 3 route.

## Evaluation Surface

The runner scans the retained `Cl(3) / Z^3` Wilson-SU(3) and staggered
fermion surface with:

- lattice: `L = 4`, `L_t = 4`;
- Wilson beta grid: `1.0` through `30.0`, with refinement around `beta = 6`;
- gauge sampling: Wilson-plaquette Metropolis updates with SU(3)
  near-identity proposals;
- fermion block: massless staggered Dirac operator with antiperiodic time
  boundary condition.

The six detectors are:

1. plaquette expectation `<P>(beta)`;
2. Polyakov loop magnitude `|<L>|(beta)`;
3. Grassmann log-det density `log |det D_stag[U]| / dim`;
4. smallest Dirac singular value `|lambda_min|(beta)`;
5. spectral gap near zero;
6. low-mode density `rho(0; beta)`.

The detector criterion is runner-defined and local to this row: a candidate
feature must be a localized residual, kink, extremum, jump, or curvature
feature at `beta = 6` above the runner threshold.

## Runner Witness

Cached runner:
`logs/runner-cache/frontier_g_bare_critical_feature_scan.txt`.

The runner reports:

```text
SUMMARY: PASS=6  FAIL=0
VERDICT: NO critical feature at beta = 6 in any scanned observable
```

The six PASS checks mean "no localized non-smooth feature at beta=6" for
the six detectors.  This is a negative bounded result, not a code failure.

## Detector Outcomes

At `L = 4`, all six detectors are smooth through `beta = 6` under the
runner's local feature criterion:

| detector | local outcome at beta = 6 |
|---|---|
| `<P>` | no localized beta=6 feature |
| `|<L>|` | no localized beta=6 feature |
| `log |det D| / dim` | no localized beta=6 feature |
| `|lambda_min|` | no localized beta=6 feature |
| spectral gap | no localized beta=6 feature |
| `rho(0)` | subthreshold kink/shoulder, not detector-loud localized closure |

The `rho(0)` row is the important caveat.  It shows a broad low-mode-density
shoulder near the beta=6 neighborhood on this small lattice, but the runner
does not classify it as a localized beta=6 fixation feature.  The shoulder is
therefore disclosed as finite-surface diagnostic content, not promoted into a
size-stable dynamical selection theorem.

## Scope Boundary

### In Scope

- The completed L=4 finite scan.
- The six listed detectors.
- The runner's beta=6 local feature criterion.
- The bounded negative result that this completed detector surface does not
  dynamically fix `g_bare = 1`.

### Out Of Scope

- L=6 persistence or cross-lattice convergence.
- Larger-volume singularities.
- Observables not included in the six-detector scan.
- Topological charge with smearing, chiral condensate at finite mass,
  Wilson-loop ratios, susceptibilities of non-plaquette source operators,
  anomalous dimensions, or any future Path 3.1 detector.
- The operator-algebra or normalization route to `g_bare = 1`.

## Negative-Claim Discipline

**N1 alternative routes.** The runner checks six distinct detector routes:
`<P>`, `|<L>|`, `log |det D| / dim`, `|lambda_min|`, spectral gap, and
`rho(0)`. Each route is tested only against the local L=4 beta=6 detector
criterion and none produces a detector-loud localized feature.

**N2 wall independence.** The collapsed walls are: W1 the L=4 finite scan,
W2 the six-detector set, W3 the runner's local beta=6 threshold, and W4
the finite sampling/cache. Closing W1 does not close larger volumes; adding
detectors does not change the six checked here; changing W3 or W4 would
require a separate runner/cache.

**N3 hidden-wall scan.** Terms such as "framework-native", "critical
feature", and "detector-loud" are local to the runner and not global
physics claims. The note now names the L=4, six-detector, threshold, and
finite-cache boundaries explicitly.

**N4 residual matching.** The residual closed here is only "no L=4
localized beta=6 feature in these six detectors." Older L=6,
cross-lattice, and broad Path 3 language does not match that residual and
is therefore excluded from the binding claim.

**N5 rhetoric audit.** The negative statement is not phrased as "no
dynamical route exists"; it is only "this completed L=4 detector surface
does not supply the feature." Larger-volume, unscanned-observable, and
normalization-route resolutions are out of scope.

**N6 partial-closure path scan.** Dedicated L=6/L>=12 scans, chiral
condensate at finite mass, topological charge with smearing, Wilson-loop
ratios, non-plaquette susceptibilities, and operator-algebra
normalization remain open paths. This note does not classify them as new
axioms or failed science.

**N7 steelman.** A hostile reviewer can fairly argue that a real
large-volume or different-observable beta=6 feature might be invisible in
the L=4 six-detector cache. That objection is accepted by narrowing the
claim to the completed L=4 detector surface.

**N8 cross-cycle echo.** The previous source version overclaimed
cross-lattice persistence and broad Path 3 closure from a runner cache
that only supports the L=4 detector result. This revision removes that
echo rather than repeating it.

## Relation To The g_bare Program

This result does not weaken `g_bare = 1` as a framework-normalization input.
It says only that this completed L=4 dynamical-detector scan does not derive
`g_bare = 1` as a critical feature.

The review-safe reading is:

> `g_bare = 1` remains a framework-normalization/evaluation input on this
> surface; this L=4 detector scan does not supply an independent dynamical
> fixation mechanism.

## Audit Handoff

Target claim id:
`g_bare_dynamical_fixation_obstruction_note_2026-04-18`.

The previous audit blocker was `scope_too_broad`: the old note included
L=6/cross-lattice persistence and broad Path 3 closure language beyond the
cached runner.  This revision intentionally narrows the source to the
completed L=4 detector result and keeps the rho-near-zero shoulder explicit.

No audit verdict is applied here; independent audit owns any re-audit
status after the pipeline sees the edited source.
