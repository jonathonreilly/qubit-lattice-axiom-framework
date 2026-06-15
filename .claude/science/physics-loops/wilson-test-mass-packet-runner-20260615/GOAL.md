# Goal

Register a primary audit packet for
`wilson_test_mass_continuum_note_2026-04-11` without changing its audited
status or widening its science.

The row was already `audited_clean` and `retained_bounded`, but its
`runner_path` was null. The fix is a source-side runner registration and cache
repair so the next audit packet can inspect the named Wilson evidence directly.
