# Goal

Repair the active `staggered_backreaction_live_capture_packet_note_2026-05-29`
conditional packet blocker by making the primary live capture packet runner
verify the complete transitive helper source packet inline.

The target is exact support for re-audit. This block must not set or edit an
audit verdict.
