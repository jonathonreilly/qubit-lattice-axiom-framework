# Handoff

This branch repairs the conditional audit on
`docs/FLAVOR_SO2_READOUT_FALSE_BINARY_NOTE_2026-05-30.md` by narrowing the
claim to the finite determinant/readout algebra.

Main changes:

- Removes the global claim that framework baseline plus inputs leave the count
  undetermined.
- Removes the claim that both readings are native physical readouts or that
  neither is forced.
- Keeps the S1-S4 algebra: C3 rephase obstruction, delta-blind Q, determinant
  versus block-product counting, and `delta=m*pi/3` degeneracy locus.
- Refreshes the cache after the narrowed runner verdict.

Verification commands:

```bash
python3 scripts/flavor_so2_readout_false_binary_2026_05_30.py
python3 scripts/cached_runner_output.py --check-only scripts/flavor_so2_readout_false_binary_2026_05_30.py
python3 -m py_compile scripts/flavor_so2_readout_false_binary_2026_05_30.py
git diff --check
```

Expected runner result: `SCORECARD PASS=4 FAIL=0`.
