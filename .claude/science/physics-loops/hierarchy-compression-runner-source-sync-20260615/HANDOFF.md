# Handoff

This PR repairs the source/runner drift on the hierarchy dimensional-compression
audited-scope companion.

Changed:

- Runner source-firewall now reads
  `docs/HIERARCHY_DIMENSIONAL_COMPRESSION_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md`.
- Companion verification text now expects `SCORECARD: 7 pass, 0 fail out of 7`.
- Companion text explicitly says the result remains a bounded numerical
  diagnostic and does not derive the D=4 bridge.

Do not include local generated audit outputs in this PR.
