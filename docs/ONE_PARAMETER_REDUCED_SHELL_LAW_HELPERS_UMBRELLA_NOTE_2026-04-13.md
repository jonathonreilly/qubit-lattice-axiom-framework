# One-Parameter Reduced Shell Law Helpers — Umbrella Wrapper

**Date:** 2026-04-13 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded umbrella wrapper for the five frontier helper
modules consumed by the runner
`scripts/frontier_one_parameter_reduced_shell_law.py`.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding helper modules.
**Runner:**
[`scripts/frontier_one_parameter_reduced_shell_law.py`](../scripts/frontier_one_parameter_reduced_shell_law.py)
**Runner cache:**
[`logs/runner-cache/frontier_one_parameter_reduced_shell_law.txt`](../logs/runner-cache/frontier_one_parameter_reduced_shell_law.txt)

## Source boundary (2026-06-12)

**Boundary:** renaming / helper-wrapper support only. Effective status is
audit-derived; this source records only the claim boundary.

The load-bearing move is the creation of a citeable umbrella handle for five
helper modules. This note may be cited only as a helper-wrapper registry. It
may not be cited as a derivation of the helper modules, the exterior projector,
the source-family constructors, the sewing-shell projection, the radial DtN
kernel, or the parent shell-law theorem.

Promotion beyond wrapper support requires separate retained wrapper notes or
complete helper-runner sources for the helper modules whose behavior is meant
to be load-bearing.

## Citation/use firewall (2026-06-18)

Direct citations to this note are allowed only for its helper-wrapper registry
function: it names the five helper modules consumed by
`scripts/frontier_one_parameter_reduced_shell_law.py` and supplies the
one-hop dependency handle that keeps those runner imports visible to the
citation graph.

Direct citations to this note may not be used as:

- a derivation of any helper module;
- a derivation of the parent one-parameter reduced shell law;
- a derivation of the exterior projector, source-family constructors,
  sewing-shell projection, radial DtN kernel, or nonlinear tensor / GR
  completion;
- an authority for moving any helper, parent shell-law, tensorial matching, or
  publication row to a stronger status.

The companion runner now checks the source tree for direct citations that lack
this helper-wrapper / one-hop-registry qualifier. This is a source-side
firewall only; independent audit remains responsible for any effective-status
movement.

## Purpose

This wrapper note documents the five frontier helper modules that the
runner of `ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md`
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

## Retarget: shell-helper surface now sourced by the lattice identity (2026-06-16)

The exterior / shell-localization helper surface this note rests on (shell-mean
profile equality, exterior projector `Pi_R^ext`, sewing-band shell source
`sigma_R = H Pi_R^ext`, radial-DtN kernel, one-parameter reduced-shell law) is
now represented by
[`LATTICE_LAPLACIAN_SHELL_LOCALIZATION_IDENTITY_BOUNDED_THEOREM_NOTE_2026-06-16.md`](LATTICE_LAPLACIAN_SHELL_LOCALIZATION_IDENTITY_BOUNDED_THEOREM_NOTE_2026-06-16.md),
which derives that shell identity from the Lattice axiom's `Z^3`
nearest-neighbor adjacency plus the existing cubic `O_h` lift (runner-verified
`TOTAL: PASS=14 FAIL=0`). This replaces the imported `_frontier_loader` helper
surface for that shell content only. Independent re-audit must decide whether
this row can move; no audit status, effective status, or `bounded -> retained`
verdict is asserted here. Any non-shell residual (a GR / tensor completion or
the lattice-Green `1/r` Maradudin asymptotic) is out of scope and unaffected.
