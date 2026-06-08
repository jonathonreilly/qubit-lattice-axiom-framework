# Historical Headline Note: Newtonian Distance Law

**Date:** 2026-04-04  
**Status:** historical pointer note; use the bounded replay note instead
**Pointer repair:** 2026-06-08

This file preserves the original headline wording from the branch import. It is
not the retained claim surface for a universal Newtonian law.

For the review-safe bounded read, use:

- [docs/VALLEY_LINEAR_WIDE_TAIL_NOTE.md](VALLEY_LINEAR_WIDE_TAIL_NOTE.md)
- [scripts/valley_linear_wide_tail_replay.py](../scripts/valley_linear_wide_tail_replay.py)
- [logs/2026-04-04-valley-linear-wide-tail-replay.txt](../logs/2026-04-04-valley-linear-wide-tail-replay.txt)
- [logs/runner-cache/valley_linear_wide_tail_replay.txt](../logs/runner-cache/valley_linear_wide_tail_replay.txt)

The frozen raw replay log SHA-256 is:

```text
2047f12a5143ac9501bacac31cc895fc278e47cf61372c8504d1ef1059a3d409
```

The registered verifier parses the frozen raw `z, delta, direction` rows and
recomputes the peak-tail and far-tail exponents from those rows:

```bash
python3 scripts/valley_linear_wide_tail_replay.py
```

Expected:

```text
SCORECARD PASS=9 FAIL=0
```

This pointer row is guarded by:

```bash
python3 scripts/newtonian_distance_law_confirmed_pointer_guard_2026_06_08.py
```

The safe wording is:

- the widened `W = 12`, `h = 0.25` replay gives a far-tail fit of `b^(-1.17)`
  on the tested `z >= 5` window
- that is a strong finite-lattice replay
- it is not, by itself, a universal theorem
