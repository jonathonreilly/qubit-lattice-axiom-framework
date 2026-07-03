# Handoff

This branch adds a bounded theorem/no-go for the lensing finite-path blocker.

Core result: the detector-centroid `kubo_true` observable is a signed adjoint
edge functional with a nearly cancelled scalar-potential monopole and a live
signed dipole on the fixed `H=0.6`, `T_phys=15` harness.  A nonzero
nonnegative scalar-potential path/layer reduction cannot reproduce that
functional because it necessarily has a surviving `1/b` monopole.

Files:

- `docs/LENSING_CENTROID_MULTIPOLE_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`
- `scripts/frontier_lensing_centroid_multipole_no_go.py`
- `logs/runner-cache/frontier_lensing_centroid_multipole_no_go.txt`

Verification:

```text
python3 scripts/frontier_lensing_centroid_multipole_no_go.py
```

Expected result:

```text
TOTAL: PASS=8 FAIL=0
```

Reviewer focus:

- Check that the no-go is scoped only to nonzero nonnegative scalar-potential
  reductions of `kubo_true`.
- Check that the note does not claim retained/unbounded lensing.
- Decide whether this should redirect future lensing repair work toward the
  native signed adjoint-centroid bridge.
