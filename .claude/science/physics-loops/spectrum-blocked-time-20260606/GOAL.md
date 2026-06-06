# Goal

Repair the audited conditional blocker on
`axiom_first_spectrum_condition_theorem_note_2026-04-29`:

> missing_bridge_theorem: add an explicit blocked-time-spacing normalization bridge identifying a_tau as the two-step block spacing, or change H and m_gap to use 1/(2 a_tau), then align the runner with T_hat^2.

This branch takes the second route. It keeps `a_tau` as the single lattice
time spacing, treats `T := T_hat^2` as the two-step blocked object, and
therefore reconstructs `H` and `m_gap` with `1/(2 a_tau)`.
