# Goal

Refresh PR #3787 as a narrow source-side repair for the remaining SM `g_*`
I12 audited-conditional row.

Latest main no longer needs the old Higgs-side accepted-premise edit from this
PR. The current target is only:

- `SM_GSTAR_I12_NUR_THERMAL_EXCLUSION_BOUNDED_NOTE_2026-05-29`

This branch does not perform an audit. It prepares a cleaner source packet for
independent review/audit by separating admitted small-neutrino-mass input from
the accepted thermalization comparator.
