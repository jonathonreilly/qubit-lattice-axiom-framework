# PR backlog

PR preparation is deferred until the managed environment permits writes to the shared
Git metadata and network access. After review-loop passes, the recovery sequence is:

```bash
python3 scripts/vocab_lint.py --fix \
  docs/MESON_GAUGE_INVARIANT_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md \
  .claude/science/physics-loops/meson-same-matrix-four-field-repair-20260729/*.md
git add docs/MESON_GAUGE_INVARIANT_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md \
  scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py \
  scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py \
  scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py \
  logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt \
  logs/runner-cache/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.txt \
  logs/runner-cache/meson_os_transfer_source_packet_manifest_2026_06_06.txt \
  outputs/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.json \
  outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json \
  .claude/science/physics-loops/meson-same-matrix-four-field-repair-20260729/
git commit -m "[physics-loop] close meson same-matrix four-field audit gap"
git push -u origin HEAD
gh pr create --base main \
  --title "[physics-loop] meson same-matrix four-field repair — bounded theorem" \
  --body-file .claude/science/physics-loops/meson-same-matrix-four-field-repair-20260729/PR_BODY.md
```
