# Goal

Repair the helper-source artifact blocker for
`poisson_backreaction_live_threshold_packet_note_2026-05-29`.

The audited conditional row requested the full `scripts/backreaction_poisson.py`
helper source and a fresh cache so the restricted packet can audit the build,
external-field, propagation, self-field, escape, and deflection computations.
The source packet already exposes the helper, but the primary runner used an
import form missed by `scripts/audit_packet_script_deps.py`. This branch makes
the helper detectable and refreshes the affected caches/JSON.

