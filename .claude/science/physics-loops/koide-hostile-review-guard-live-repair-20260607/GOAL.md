# Goal

Repair the source-side blocker recorded for
`koide_hostile_review_guard_note_2026-04-24`: the guard must verify actual
stdout emissions from target no-go scripts, and those scripts must expose
negative `CLOSES` labels and residual labels on their live execution paths.

This block does not claim positive Koide closure. It preserves the no-go
boundary and only fixes the guard-hygiene artifact that was blocking re-audit.

