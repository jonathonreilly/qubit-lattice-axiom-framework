# Handoff

This branch repairs the exact-source audited-conditional row
`plaquette_beta6_strong_coupling_character_narrow_theorem_note_2026-05-27`.

The useful science is the explicit source-boundary split:

- load-bearing: finite rational Padé/Borel-Padé algebra over the displayed
  supplied tuple;
- not load-bearing: the SU(3) coefficient table, beta=6 to `u=1/3`, and the MC
  comparator.

Verification:

```bash
python3 scripts/frontier_plaquette_beta6_strong_coupling_character_narrow.py
python3 scripts/cached_runner_output.py scripts/frontier_plaquette_beta6_strong_coupling_character_narrow.py --check-only
git diff --check
```

Expected runner result: `TOTAL: PASS=26 FAIL=0`.

No `docs/audit/**` files are changed.

