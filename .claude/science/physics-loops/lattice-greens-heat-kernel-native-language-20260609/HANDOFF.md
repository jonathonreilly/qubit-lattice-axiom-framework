# Handoff

## Target

Clean up the heat-kernel Green-function row after the native Maradudin reroute
landed on `main`.

## Science Move

The source note no longer describes the leading `1/(4 pi r)` Green asymptotic
as an accepted-premise textbook import. It routes the row through the stronger
framework-native lattice-correction theorem for the same exact `Z^3`
heat-kernel/Bessel Green kernel.

Textbook sources remain parallel references only. The direct local-CLT route is
kept open as an alternate proof route, so the branch avoids overclaiming.

## Files

- `docs/LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`
- `scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py`
- `logs/runner-cache/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.txt`
- `.claude/science/physics-loops/lattice-greens-heat-kernel-native-language-20260609/`

## Verification

- `python3 scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py`
- `python3 -m py_compile scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py`
- `git diff --check`
- `git diff --name-only -- docs/audit`

## Audit Boundary

No audit result files were changed. Independent audit/review must decide any
effective retained status movement.
