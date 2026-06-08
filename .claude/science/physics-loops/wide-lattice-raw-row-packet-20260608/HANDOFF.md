# Handoff

This branch repairs the audit packet for `wide_lattice_h2t_distance_law_note`.

The audit blocker was that the restricted packet lacked the raw distance and
`F~M` rows needed for an independent fit audit.  The note now embeds the frozen
raw rows, and the new manifest runner checks that the note rows match the
SHA-pinned frozen replay log.

Files:

- `docs/WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md`
- `scripts/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.py`
- `logs/runner-cache/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.txt`

Verification:

```text
python3 scripts/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.py
python3 scripts/wide_lattice_h2t_distance_replay.py
```

Expected summaries:

```text
RAW_ROW_PACKET PASS=25 FAIL=0
SCORECARD PASS=12 FAIL=0
```
