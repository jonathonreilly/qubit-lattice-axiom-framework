# Coarse-Grained Exterior Law Helper Module

**Date:** 2026-04-14 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded helper-module wrapper for the shell-averaging
plus radial-harmonic projection of the finite-rank exterior field onto
the `phi_eff(r) = a / r` unique radial-harmonic law.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding helper module.
**Primary runner / module:** `scripts/frontier_coarse_grained_exterior_law.py`

## Purpose

This wrapper note documents the coarse-grained exterior law helper module
so downstream notes (notably
[FINITE_RANK_SOURCE_TO_METRIC_THEOREM_NOTE.md](FINITE_RANK_SOURCE_TO_METRIC_THEOREM_NOTE.md))
can register a one-hop dependency rather than carry the helper as an
unattributed Python `SourceFileLoader` import.

## What this module provides

The helper module takes the exact finite-rank exterior field
`phi(x)` produced by the
[FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md](FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md)
and applies the shell-averaging plus radial-harmonic projection map

```
phi_eff(r)  :=  shell_average(phi, r)  ->  a / r
```

with the projection coefficient `a` determined by best-match radius
selection across the radial scan. The module exposes:

- `build_finite_rank_phi_grid()` — assembles the `phi(x)` field grid
  from the upstream finite-rank exterior field construction.
- `analyze_family(...)` — runs the shell-averaging plus radial-harmonic
  projection and reports the coarse-grained metric residual at each
  scan radius.

## What this produces

The bounded coarse-grained metric residual on the finite-rank family is
verified in the companion runner of the downstream theorem note:

- best matching radius in current scan: `R_match = 5.0`
- direct same-source metric residual: `1.039e-02`
- coarse-grained radial-harmonic residual: `7.028e-06`
- improvement factor: `~1.48e3`

So the coarse-graining map provides a clean scalar/isotropic exterior
metric architecture with multi-order improvement on the residual.

## Boundary

This wrapper note records the bounded helper-module character of the
coarse-grained exterior law module. It does not claim:

- a framework-level derivation of the shell-averaging or radial-harmonic
  projection as physically forced;
- a tensorial `3 + 1` lift from the scalar exterior law to the full
  lapse-shift-spatial metric;
- closure of the downstream finite-rank source-to-metric theorem
  beyond the bounded coarse-grained residual it already reports.

Its only function is to provide a citeable one-hop authority for the
shell-averaging plus radial-harmonic projection construction so
downstream notes register the import cleanly instead of carrying it as
a `SourceFileLoader` runner import without a wrapper.
