# Goal

Repair `industrial_sdp_bootstrap_lattice_bracket_note_2026-05-03`, an
uncovered high-impact `open_gate` row whose audit blocker was that the displayed
lower bracket `p1 >= 0.4225` was admitted rather than SDP-derived.

The science move is to make the exact auditable content the no-upper-bound
obstruction: the encoded SDP constraints admit an explicit all-ones feasible
point with `p1 = 1`, so this surface cannot prove any nontrivial upper bound
without additional loop equations.
