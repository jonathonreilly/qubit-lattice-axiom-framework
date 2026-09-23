# Formation capacity and exact terminal counts — review unit

This unit is based on the local compensated volume target in PR #8852.
Read `formation_capacity_review/SYNTHESIS.md` first, then the author and
independent arguments, the exact terminal-count theorem, and
`formation_capacity_review/ROOT_REVIEW.md`. `SCOPE_CHALLENGES.md` records
the narrow negative boundary without asserting a formal no-go or audit
verdict. The author's capacity draft retains its historical statement that
volume comparison was pending; PR #8852 subsequently closed that premise.

The independent capacity PRE was frozen before author comparison. A distinct
post-PRE exact implementation and source authentication completed, but the
checker hit a usage limit before writing a FINAL narrative. Root reviewed
its code and output. The exact terminal-count theorem is root work using
the independent PRE physical matrix and a separate rotor-path calculation.
It has no checker-authored final review. These limits are part of the handoff.

Run `verify_formation_capacity_publication.py` to verify the selected
artifact identities and exact source files in this PR. The portable
`terminal_path_author/terminal_path_structural_check.py` uses only the
standard library. `terminal_path_exact.py` uses SymPy 1.14. To rerun without
rewriting committed result files, set `TERMINAL_PATH_OUTPUT_DIR` to a scratch
directory before invoking either script. The original runs, stdout/stderr,
receipts and exact result JSON are included. The independent PRE scripts
write their result files at top level and should also be rerun in a copy.

The exact path result is conditional on this finite supplied Hamiltonian,
formation instrument and Gauss sector. It proves count probabilities, not a
continuum limit, microscopic-volume exchange, energy source, empirical
prediction or TOE closure. This branch is a review proposal; no merge or
formal audit application is requested.
