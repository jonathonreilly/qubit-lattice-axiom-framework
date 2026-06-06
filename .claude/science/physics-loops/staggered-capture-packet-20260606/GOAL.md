# Goal

Repair the source-packet artifact blocker for
`staggered_backreaction_live_capture_packet_note_2026-05-29`.

The audited conditional row requested complete untruncated source for
`scripts/frontier_staggered_backreaction_prototype.py` and a rerun of the
restricted packet. The helper paths are already detected on main, but the note
lacked a source-packet verifier/certificate analogous to the green packet. This
branch adds that verifier, links all transitive helper sources/caches, and pins
the verifier cache/JSON.

