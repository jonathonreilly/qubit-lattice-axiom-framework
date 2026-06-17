# Handoff

This PR targets `one_parameter_reduced_shell_law_note`.

The prior audit blocker said the row's runner output depended on opaque helper
imports rather than an independently inspectable operator/source chain. This
branch adds a self-contained replay runner that inlines the finite Dirichlet
Laplacian, point-Green columns, local `O_h` source constructor, finite-rank
source constructor, exterior projection, shell source, radial averaging, and
shell-mean readout.

The scientific boundary is unchanged: bounded reduced-shell support only. The
PR does not edit audit data, does not promote status, and does not claim full
nonlinear gravity closure.

Verification:

- `python3 scripts/frontier_one_parameter_reduced_shell_law.py` -> `PASS=7
  FAIL=0 TOTAL=7`.
- `python3 scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py`
  -> `PASS=10 FAIL=0 TOTAL=10`.
- `python3 -m py_compile scripts/frontier_one_parameter_reduced_shell_law.py scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py`
  passed.

Exact next action for reviewer/auditor: run
`python3 scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py`
and decide whether this closes the artifact-opacity blocker or whether retained
helper authority notes are still required.
