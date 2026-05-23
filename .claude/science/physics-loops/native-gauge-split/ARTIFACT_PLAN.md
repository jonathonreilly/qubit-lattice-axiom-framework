# Artifact Plan

## Source Artifacts

- Rewrite `docs/NATIVE_GAUGE_CLOSURE_NOTE.md` as the narrow nonabelian
  positive-theorem candidate.
- Update `scripts/frontier_non_abelian_gauge.py` so it checks only the
  nonabelian scope and retained graph-first nonabelian dependencies.
- Add `docs/NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`
  to preserve the abelian eigenvalue calculation as bounded.
- Add `scripts/frontier_native_gauge_left_handed_abelian_surface_bounded_2026_05_23.py`
  for the bounded abelian split.

## Generated Artifacts

Run the audit pipeline and commit regenerated audit/publication effective
status views, because the native gauge source hash changes and downstream
status must not remain stale.
