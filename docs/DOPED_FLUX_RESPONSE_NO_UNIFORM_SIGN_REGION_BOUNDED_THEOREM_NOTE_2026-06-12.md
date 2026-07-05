# Off Particle-Hole Symmetry There Is Still No Uniform Flux-Response N-Sequence on the Tested Doping Grid: the Alternation-Fate Table — Three Author Hypotheses Refuted in Sequence on Exact Data (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_doped_flux_response_alternation_fate_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_doped_flux_response_alternation_fate_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=24 FAIL=0` — exact
analytic second derivatives (the validated perturbation-theory machinery; no finite
differencing in any claim).

## Three hypotheses, three refutations — the wall now has a precise name

Three hypotheses — **all the author's own working hypotheses, none landed claims** —
failed in sequence on exact data: (1) a uniform sign at fixed filling
(parity-resolved instead); (2) a uniform sign after parity averaging (N-alternation
survives); and now (3) a uniform sign off particle-hole symmetry: on the tested
doping grid (`μ_ch ∈ {0.25, 0.5, 1.0, 1.5}` × `N ∈ {8..16}` × `m ∈ {0, 0.4}` ×
`T ∈ {0.3, 0.6}`), **no uniform N-sequence exists at any tested grid point**
(gated on the tested slice — a finite-grid statement, not a continuum region
claim). The
alternation-fate table is the datum: some dopings go *mixed-nonalternating*
(`−+−++` at `μ_ch = 0.25`), others remain *sign-alternating* with a shifted phase
(`+−+−+` at `μ_ch = 0.5`); magnitudes are non-monotone in `μ_ch` (reported).

## Findings (runner `PASS=24`)

Analytic-vs-FD validation at resolvable instances (one at `μ_ch = 0.5`); the full
exact table printed; per-doping alternation-fate classifications computed first and
then gated to the observed patterns — **a determinism/regression gate that freezes
the observed fingerprint, not an independent refutation** (stated); the
particle-hole relation
`Ω″(μ_ch) = Ω″(−μ_ch)` exact at `10⁻¹⁰`; the `μ_ch = 0` column cross-checks two entries
against predecessor zero-doping values (a spot check, stated as such); gauge invariance exact; `T = 50` kills the response.

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

## No-Go Discipline Gate

This is a finite-grid obstruction to a uniform finite-ring `N` sign sequence,
not a continuum obstruction.

- **N1 alternatives.** Fixed filling, parity average, doped grid, particle-hole
  reflection, and high-temperature suppression were checked as distinct routes.
- **N2 wall independence.** Finite-grid alternation, thermodynamic extrapolation,
  continuum/heat-kernel replacement, gauge self-energy, and non-abelian extension
  are independent residuals; none is closed by another here.
- **N3 hidden-wall scan.** `tested grid`, `finite ring`, `free`, and `U(1)` are
  load-bearing scope restrictions and are stated in the claim and runner.
- **N4 residual matching.** The result attacks only the finite-grid matter
  screening sign route; it does not attack `b3`, gauge self-energy, non-abelian
  response, or thermodynamic-limit signs.
- **N5 rhetoric audit.** Negative wording is limited to the tested grid and the
  author's own working hypotheses; no landed claim is declared false.
- **N6 partial closure.** The exact table, particle-hole symmetry, gauge check,
  and high-temperature suppression are landed as useful data even though the
  continuum matter-sign route remains open.
- **N7 steelman.** A uniform sign could still emerge after a controlled
  thermodynamic limit, a continuum/heat-kernel replacement, or adding the missing
  gauge self-energy.
- **N8 echo.** This follows the finite-packet discipline from nearby flux-response
  work: exact finite tables can guide the route without being promoted to
  untested physical-region theorems.

Gate outcome: PASS for the finite tested-grid obstruction only.
