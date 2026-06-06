# Handoff

This PR repairs an audit-packet mismatch: the prompt template says primary and
helper sources are included, but `codex_audit_runner.py` elided primary sources
above 30k chars and helpers above 20k chars. Several current live conditionals
ask for complete unelided source, and their scripts are only moderately above
the old caps.

The new cap is `120_000` chars for primary and helper sources. Smoke rendering
on current main shows no truncation markers for:

- `gravitational_wave_probe_note`
- `meson_gauge_invariant_os_transfer_representation_bounded_note_2026-05-30`
- `staggered_backreaction_live_green_packet_note_2026-05-29`

No audit results or ledger data are included.
