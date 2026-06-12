# Off Particle-Hole Symmetry There Is Still No Uniform Flux-Response N-Sequence on the Tested Doping Grid: the Alternation-Fate Table — Three Author Hypotheses Refuted in Sequence on Exact Data (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (the named μ_ch ≠ 0 follow-on of the parity-averaged note, in review — cross-referenced, not cited as graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_doped_flux_response_alternation_fate_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_doped_flux_response_alternation_fate_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=12 FAIL=0` — exact
analytic second derivatives (the validated perturbation-theory machinery; no finite
differencing in any claim).

## Three hypotheses, three refutations — the wall now has a precise name

Three hypotheses — **all the author's own working hypotheses, none landed claims** —
died in sequence on exact data: (1) a uniform sign at fixed filling
(parity-resolved instead); (2) a uniform sign after parity averaging (N-alternation
survives); and now (3) a uniform sign off particle-hole symmetry: on the tested
doping grid (`μ_ch ∈ {0.25, 0.5, 1.0, 1.5}` × `N ∈ {8..16}` × `m ∈ {0, 0.4}` ×
`T ∈ {0.3, 0.6}`), **no uniform N-sequence exists at any tested grid point**
(gated on the tested slice — a finite-grid statement, not a continuum region
claim). The
alternation-fate table is the datum: some dopings go *mixed-nonalternating*
(`−+−++` at `μ_ch = 0.25`), others remain *sign-alternating* with a shifted phase
(`+−+−+` at `μ_ch = 0.5`); magnitudes are non-monotone in `μ_ch` (reported).

## Findings (runner `PASS=12`)

Analytic-vs-FD validation at resolvable instances (one at `μ_ch = 0.5`); the full
exact table printed; per-doping alternation-fate classifications computed first and
then gated to the observed patterns — **a determinism/regression gate that freezes
the observed fingerprint, not an independent refutation** (stated); the
particle-hole relation
`Ω″(μ_ch) = Ω″(−μ_ch)` exact at `10⁻¹⁰`; the `μ_ch = 0` column cross-checks two entries
against the in-review predecessor's values (a spot check, stated as such); gauge invariance exact; `T = 50` kills the response.

## What this buys, honestly

The finite-ring program for the matter screening sign now has a precise tested-slice
statement: **the exact finite-ring orbital response sign is
commensuration-structured at every tested point — fixed filling, parity-averaged,
and doped — with no uniform N-sequence on the tested grids.** A uniform matter screening sign, if the framework
derives one, must come from a different object (the named follow-ons: thermodynamic
extrapolation with exact bounds, or the continuum/heat-kernel surface). The
Peskin–Schroeder import `(X3)` is used nowhere; the gauge self-energy remains the
named gap.

## Scope

Abelian `U(1)` flux, free rings, finite `T`, the tested doping grid; the
alternation-fate table is the datum. Not claimed: `b₃` or any β-number; non-abelian
content; thermodynamic-limit asymptotics; `d = 3`. Standard math (method only):
grand-canonical traces; perturbation theory.

No new axiom, primitive, measure, or weight; `r` untouched. The audit lane grades.
