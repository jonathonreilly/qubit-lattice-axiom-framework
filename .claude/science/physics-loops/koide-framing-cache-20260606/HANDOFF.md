# Handoff

Branch: `physics-loop/koide-framing-cache-20260606`

Primary movement:

- Replaces stale cache failure
  `ModuleNotFoundError: No module named 'networkx'`
  with completed cache
  `logs/runner-cache/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.txt`.
- Adds the completed cache path to
  `docs/KOIDE_EMBEDDING_FRAMING_WRITHE_SO2_VS_SPIN_Z2_DECOUPLING_NARROW_NO_GO_NOTE_2026-06-02.md`.

Science boundary:

- The row remains a scoped abelian embedding-framing no-go.
- This branch does not derive fermion statistics, close a spinor-state route, or
  close second-quantized graded locality.
- The cache certificate records `SCORECARD: PASS=24 FAIL=0`.

Audit/result surfaces:

- `docs/audit/**` was not edited.

Next exact action:

- Reviewer/auditor can re-audit the row against the completed cache.

