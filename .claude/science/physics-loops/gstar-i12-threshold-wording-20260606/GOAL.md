# Goal

Repair the audited conditional blocker on
`sm_gstar_i12_nur_thermal_exclusion_bounded_note_2026-05-29` without touching
audit verdict files.

The specific repair is source-level: correct the 100 GeV numerical margin and
state the `g_* = 112` route as the true thermalization threshold
`y_nu >= y_thr`, keeping `y_nu ~ O(1)` only as a stronger excluded steelman.

This branch does not change the effective audit status. It prepares the source
for reviewer extraction and independent re-audit.
