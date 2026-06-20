# Goal

Continue the physics-loop audit-unblock campaign by converting source-side
claim-boundary defects into small review PRs.

Block112 targets
`quark_route2_exact_readout_map_note_2026-04-19`. The source note and runner
already expose an exact missing-map obstruction, but the generated audit row was
defaulting to `positive_theorem`. This block adds canonical `open_gate`
metadata and runner enforcement so the independent audit lane receives the
right source boundary.

No audit verdict is applied in this block, and no code is pushed to `main`.
