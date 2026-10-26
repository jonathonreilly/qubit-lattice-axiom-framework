# PMNS Supplied-Line Finite Search Diagnostic

**Date:** 2026-04-20; scope corrected 2026-10-23
**Type:** open_gate
**Status:** supplied finite search trace and enumerated numerical comparisons.
**Primary runner:** `scripts/frontier_dm_pmns_supplied_line_finite_search_diagnostic_2026_04_20.py`

## Supplied model and inputs

The supplied Hermitian chart, flavor-axis basis, row permutation and historical
angle targets are defined by
[the conditional PMNS calculation](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md).
The targets are `(0.307, 0.0218, 0.545)`. They are comparison inputs, not
derived physical angles. This diagnostic evaluates that map on
`delta = q_+ = sqrt(6)/3`, with real m sampled as specified below.
The imported parity and curvature functions return those same constants.
Their agreement is evaluated, not an independent derivation of the local
selector premises or their physical realization. The eighteen helper source
bindings remain explicit. This consumer does not certify deferred parity,
Gaussian, microscopic, split-2 or selector claims.

## Executed finite procedure

The solar-coordinate search samples the central finite difference with
step `h=1e-4` at 4001 equally spaced m values on `[-2000,2000]`.
Adjacent sampled zero/sign-change brackets are refined using `brentq`
(maximum 200 iterations) and roots closer than `1e-3` are deduplicated.
This algorithm locates numerical zeros of a finite-difference approximation;
it does not enumerate exact derivative roots, certify extrema between grid
points, or determine behavior outside the sampled interval.

The unweighted squared residual
`chi2 = (s12sq-0.307)^2 + (s13sq-0.0218)^2 + (s23sq-0.545)^2`
is searched in the same way with 8001 grid points on `[-200,200]` and the
same finite-difference step. The name chi2 is historical notation, not a
statistical chi-square likelihood. Endpoint comparisons compare evaluated
values only; they do not establish a global minimum on either interval.

## Numerical observations retained from the trace

The solar search locates two numerical candidates near `-0.41013790` and
`4.36500535`. At the latter, the evaluated solar value is
`0.331582718643`, above the supplied target `0.307` by about 0.02458.
Its evaluated value is lower than the other located candidate and the two
endpoints. This is a comparison of these finitely evaluated values, not a
solar-angle floor on the line.

The residual search locates one candidate near `1.278322119585`, with
residual `0.011428083950` and angle triple approximately
`(0.37920275,0.05563746,0.47379695)`. The root count is the count returned
by this procedure, not an exact or exhaustive stationary-point count.

Five separately supplied points retain their previous calculations:

| label | (m,delta,q_+) | squared residual | largest angle error |
|---|---|---:|---:|
| Schur-Q | (0.5,0.8165,0.8165) |0.06280|0.25057|
| det-crit | (0.613,0.964,1.552) |0.03113|0.15544|
| Tr(H²) boundary | (0.385,1.268,0.365) |0.08696|0.21848|
| K12 character | (0,0.8,1) |0.25719|0.50457|
| F1 parity-mixing | (0.62854,1.14618,0.48682) |0.04655|0.20500|

The runner retains exact original point expressions, grid sizes, tolerances,
numerical predicates and failed-search evidence. Positive residuals describe
these evaluated points; no all-family or all-line exclusion follows.

## Evidence boundary and recovery

I5 is still open positively: no physical positive closure is established here.
The calculation does not establish exhaustive roots, a global minimum,
physical selection, an impossible local family, or necessary nonlocal laws.
This is a reproducible table/search trace, not a failed-route conclusion.

The old whole-line no-go and nonlocal-necessity argument is substantively
withdrawn as unproved. Its full note, executable and cache are byte-preserved
under `archive/notes/review_feedback/pr9844-local-selector-2026-10-23/` and
at base `b1bc0c6e1bc9c93a23566eb3bf28ea679018ae76` under the old paths.
Original PR recovery remains `3c90f9860c3bae63ee64949e7178290f789dd982`.
Those historical arguments and output confer no present negative theorem.

## Reproduction

```bash
python3 scripts/frontier_dm_pmns_supplied_line_finite_search_diagnostic_2026_04_20.py
```

The actual cap is 120 seconds. Documentary checks require the finite-search
boundary; former note-string requirements asserting necessary nonlocal
selection are replaced. Execution coverage is finite parameter sampling,
not a lattice/site/mode completeness certificate or an N1–N8 no-go packet.
