# Historical Headline Note: Newtonian Distance Law

**Date:** 2026-04-04  
**Status:** historical pointer note; use the bounded replay note instead
**Pointer repair:** 2026-06-08
**Raw-row inventory repair:** 2026-06-08

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

## Raw-row inventory for strict formula review

The audit blocker on this pointer row asked for the raw rows and verifier output
needed to recompute the `b^(-1.17)` finite-window fit. The source authority is
the SHA-pinned frozen log above; the raw replay rows are included here so this
pointer packet is self-contained enough for strict inventory review.

Frozen replay metadata:

| field | value |
|---|---:|
| nodes | `461,041` |
| layers | `49` |
| h | `0.25` |
| W | `12` |
| max_d | `12` |
| Born | `4.82e-15` |
| k=0 | `+0.000000` |

Raw no-barrier distance rows from
`logs/2026-04-04-valley-linear-wide-tail-replay.txt`:

| z | delta | direction |
|---:|---:|---|
| `2` | `+0.000208` | `TOWARD` |
| `3` | `+0.000259` | `TOWARD` |
| `4` | `+0.000267` | `TOWARD` |
| `5` | `+0.000232` | `TOWARD` |
| `6` | `+0.000185` | `TOWARD` |
| `7` | `+0.000157` | `TOWARD` |
| `8` | `+0.000137` | `TOWARD` |
| `9` | `+0.000118` | `TOWARD` |
| `10` | `+0.000101` | `TOWARD` |

Verifier recomputation from the raw rows:

- `TOWARD support: 9/9`;
- peak row `z = 4`;
- peak-tail fit from `z >= 4`: slope `-1.0723`, `R^2 = 0.9897`, `n = 7`,
  recorded as `b^(-1.07)`, `R^2 = 0.990`;
- far-tail fit from `z >= 5`: slope `-1.1685`, `R^2 = 0.9972`, `n = 6`,
  recorded as `b^(-1.17)`, `R^2 = 0.997`.

This pointer row is guarded by:

```bash
python3 scripts/newtonian_distance_law_confirmed_pointer_guard_2026_06_08.py
```

The safe wording is:

- the widened `W = 12`, `h = 0.25` replay gives a far-tail fit of `b^(-1.17)`
  on the tested `z >= 5` window
- that is a strong finite-lattice replay
- it is not, by itself, a universal theorem
