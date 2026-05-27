# Goal

Repair `wilson_action_surface_selector_real_positive_theorem_note_2026-05-25` so it can be re-audited without importing a stronger beta/Wilson-matching authority than its cited dependency supplies.

The audit blocker said the note treated `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03` as retained authority for `beta = 6`, `g_bare^2 = 1`, and Wilson matching, while that upstream row is only a conditional rescaling lemma over an assumed Wilson matching relation.

This branch chooses the narrow repair: keep the Wilson selector as a bounded theorem over explicitly scoped `beta = 6` and standard Wilson small-`a` matching premises, remove the markdown dependency edge to the G-bare row, and preserve the finite SU(3) selector checks.
