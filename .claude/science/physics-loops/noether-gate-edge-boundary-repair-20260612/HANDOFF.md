# Handoff

This PR repairs a source-boundary issue on
`axiom_first_lattice_noether_theorem_note_2026-04-29`.

## What Changed

- The parent `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` is now a
  plain-text registered target, not a markdown one-hop dependency.
- The retained substep-1 Grassmann theorem remains the load-bearing markdown
  dependency.
- Runner exhibit E8 enforces the boundary.

## Boundaries

- No audit data edited.
- No retained promotion claimed.
- Full staggered carrier derivation remains upstream.

## Verification

- `PYTHONPATH=scripts python3 scripts/axiom_first_lattice_noether_check.py`
  -> `PASSED: 9/9`
