# Handoff

## Current Status

This block is based on `origin/main` and targets the `g_bare` normalization
dependency on the staggered-Dirac realization gate.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2803

GitHub verification: open PR, base `main`, head
`physics-loop/staggered-gbare-normalization-bridge-20260606`, merge state
`UNSTABLE`.

## Intended Result

For `g_bare`, the load-bearing staggered input is the physical `V_3` trace
surface plus per-site-to-gauge SU(2) scale bridge. The later species-label
bijection is not load-bearing for the trace normalization.

## Boundaries

- Does not close the staggered-Dirac gate.
- Does not close the parent `g_bare` gate.
- Does not use observed masses or fitted selectors.
- Does not update authority surfaces.

## Next Action

Continue campaign: select the next live lane from the opportunity queue.

## Verification

- `python3 scripts/frontier_staggered_gbare_trace_surface_bridge_2026_06_06.py`
  - `PASS=65 FAIL=0`
- `python3 -m py_compile scripts/frontier_staggered_gbare_trace_surface_bridge_2026_06_06.py`
- `git diff --check`
- ASCII check for new note/runner
- targeted wording sweep for branch-local status overclaims
