# One-Parameter Reduced Shell Law Helpers — Umbrella Wrapper

**Date:** 2026-04-13 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded umbrella wrapper for the five frontier helper
modules consumed by the runner
`scripts/frontier_one_parameter_reduced_shell_law.py`.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding helper modules.

## Purpose

This wrapper note documents the five frontier helper modules that the
runner of
[ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md](ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md)
loads via `_frontier_loader.load_frontier`, so the parent note can
register a one-hop dependency rather than carry the five helpers as
unattributed runner-internal imports.

## Helper modules covered

| Module | Role in the one-parameter reduced shell law |
| --- | --- |
| `frontier_star_shell_projector.py` | exterior projector and shell-mean operator on the truncated star at cutoff `R = 4`. |
| `frontier_same_source_metric_ansatz_scan.py` | exact source-family constructors: the exact local `O_h` family and the broader exact finite-rank family that are checked for machine-precision agreement with the reduced one-parameter law. |
| `frontier_coarse_grained_exterior_law.py` | coarse-grained exterior law on the truncated star (see also [COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md](COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md) for the shell-averaging plus radial-harmonic projection consumer). |
| `frontier_sewing_shell_source.py` | sewing-shell projection at cutoff `R = 4` producing the shell-density seven-vector that the one-parameter law constrains. |
| `frontier_radial_shell_matching_law.py` | exact radial DtN shell kernel `k_rad` and the radial-shell average operator. |

## What this umbrella covers

The runner-checked content of the parent one-parameter reduced shell
law is exact lattice arithmetic on the seven point-Green columns
carrying unit total charge to machine precision. That arithmetic is
independent of the registration status of the underlying helper
modules — the helpers supply input operators, the parent note
demonstrates linearity-from-identical-normalized-columns within those
operators. This umbrella wrapper records the helper-module roles so the
citation graph sees a single explicit one-hop edge to the helpers used.

## What this umbrella does NOT claim

- This is NOT a framework-level derivation of any of the five helper
  modules from `Cl(3)` on `Z^3` axioms.
- This is NOT a promotion of the helper modules to a stronger upstream
  tier.
- The bounded umbrella scope is the named one-hop dependency edge only.
- This wrapper does NOT close the parent's tensorial `3 + 1` matching
  blocker.

## Boundary

This wrapper note is a named-import-only bounded theorem covering the
five-helper umbrella. It does not claim:

- a framework derivation of the exterior projector, the lattice
  Laplacian, the source-family constructors, the sewing-shell
  projection, or the radial DtN kernel;
- closure of the parent shell-law theorem;
- closure of the full nonlinear `3 + 1` GR closure on the strong-field
  bridge surface.

Its only function is to provide a citeable one-hop authority for the
five helper modules so the parent note registers the cite-chain cleanly
instead of listing them as `_frontier_loader.load_frontier` runner
imports without an audit-lane handle.
