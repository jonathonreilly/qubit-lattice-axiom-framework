# Wide-Lattice h^2+T Distance-Law Note

**Date:** 2026-04-05  
**Verifier repair:** 2026-06-07
**Status:** bounded frontier replay on an independent wide-lattice replay of
the ordered 3D `1/L^2` family; independent audit lane sets effective status

## Artifact chain

- [`scripts/wide_lattice_h2t_distance_replay.py`](../scripts/wide_lattice_h2t_distance_replay.py)
- Frozen replay log: [`logs/2026-04-05-wide-lattice-h2t-distance-replay.txt`](../logs/2026-04-05-wide-lattice-h2t-distance-replay.txt)
- Registered runner cache: [`logs/runner-cache/wide_lattice_h2t_distance_replay.txt`](../logs/runner-cache/wide_lattice_h2t_distance_replay.txt)
- Raw-row packet manifest: [`scripts/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.py`](../scripts/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.py)
- Raw-row packet cache: [`logs/runner-cache/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.txt`](../logs/runner-cache/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.txt)

The registered runner defaults to a verifier for the frozen replay log above;
use `--recompute` to run the original slow wide-lattice replay.

## 2026-06-08 restricted-packet raw-row exposure

The audit blocker after the verifier repair was not a formula failure.  It was
packet visibility: a second auditor needed the raw distance and `F~M` rows in
the restricted packet, or an equivalent recompute artifact, to independently
check the fits.  This section embeds the frozen raw rows directly and adds a
manifest runner that verifies these tables match the SHA-pinned frozen log.

Frozen raw replay log SHA-256:

```text
2faf31bf9b1015df87adaadbfa8393c4a26e100abdc6ccaf6daf70308a30e024
```

Barrier sanity:

| quantity | value |
| --- | ---: |
| Born | `4.82e-15` |
| `k=0` centroid shift | `+0.000000` |

Distance rows:

| `z` | `delta` | direction |
| ---: | ---: | --- |
| 2 | `+0.000188` | TOWARD |
| 3 | `+0.000232` | TOWARD |
| 4 | `+0.000245` | TOWARD |
| 5 | `+0.000220` | TOWARD |
| 6 | `+0.000183` | TOWARD |
| 7 | `+0.000159` | TOWARD |
| 8 | `+0.000142` | TOWARD |
| 9 | `+0.000124` | TOWARD |
| 10 | `+0.000108` | TOWARD |
| 11 | `+0.000093` | TOWARD |

Fit rows recomputed by the verifier from the table above:

| fit | slope | `R^2` | `n` |
| --- | ---: | ---: | ---: |
| peak tail from `z >= 4` | `-0.9579` | `0.9801` | 8 |
| far tail from `z >= 5` | `-1.0578` | `0.9904` | 7 |

`F~M` sweep rows:

| `s` | `delta` | direction |
| ---: | ---: | --- |
| `1e-06` | `+4.636762e-06` | TOWARD |
| `2e-06` | `+9.273526e-06` | TOWARD |
| `5e-06` | `+2.318384e-05` | TOWARD |
| `1e-05` | `+4.636775e-05` | TOWARD |
| `2e-05` | `+9.273579e-05` | TOWARD |
| `5e-05` | `+2.318416e-04` | TOWARD |

The verifier recomputes the mass-scaling exponent from these six rows:

```text
alpha = 1.000003, R^2 = 1.000000, n = 6.
```

The raw-row packet manifest reports:

```text
RAW_ROW_PACKET PASS=25 FAIL=0
```

## 2026-06-07 verifier repair

The audit blocker asked for either a completed recompute cache or a full
SHA-pinned frozen replay log with all distance and `F~M` rows plus an
independent tail-fit check from those raw deltas. This note takes the frozen
raw-row verifier route:

- frozen raw replay log SHA-256:
  `2faf31bf9b1015df87adaadbfa8393c4a26e100abdc6ccaf6daf70308a30e024`;
- the verifier parses all ten raw distance rows and recomputes the peak row,
  peak-tail fit, and far-tail fit from the parsed deltas;
- the verifier parses all six `F~M` sweep rows and recomputes the mass-scaling
  exponent from the parsed deltas;
- because the frozen log stores deltas at six decimal places, the recomputed
  tail slopes are checked within a tight `0.02` exponent tolerance of the
  full-replay printed values;
- current verifier scorecard: `SCORECARD PASS=12 FAIL=0`.

## 2026-06-08 raw-row inclusion repair

The latest audit pass still treated the restricted packet as missing the raw
distance and sweep rows. This revision includes those rows directly in the
source note, while keeping the SHA-pinned frozen log as the authoritative raw
artifact. The verifier now checks both:

1. the frozen log SHA and recomputed fits; and
2. presence of these exact raw-row tables in this note.

Frozen replay metadata:

| field | value |
|---|---:|
| `h` | `0.25` |
| `W` | `12` |
| `L` | `12` |
| `max_d` | `12` |
| `Born` | `4.82e-15` |
| `k=0` | `+0.000000` |

Raw distance rows from `logs/2026-04-05-wide-lattice-h2t-distance-replay.txt`:

| `z` | `delta` | direction |
|---:|---:|---|
| `2` | `+0.000188` | `TOWARD` |
| `3` | `+0.000232` | `TOWARD` |
| `4` | `+0.000245` | `TOWARD` |
| `5` | `+0.000220` | `TOWARD` |
| `6` | `+0.000183` | `TOWARD` |
| `7` | `+0.000159` | `TOWARD` |
| `8` | `+0.000142` | `TOWARD` |
| `9` | `+0.000124` | `TOWARD` |
| `10` | `+0.000108` | `TOWARD` |
| `11` | `+0.000093` | `TOWARD` |

Raw `F~M` sweep rows:

| source strength `s` | `delta` | direction |
|---:|---:|---|
| `1e-06` | `+4.636762e-06` | `TOWARD` |
| `2e-06` | `+9.273526e-06` | `TOWARD` |
| `5e-06` | `+2.318384e-05` | `TOWARD` |
| `1e-05` | `+4.636775e-05` | `TOWARD` |
| `2e-05` | `+9.273579e-05` | `TOWARD` |
| `5e-05` | `+2.318416e-04` | `TOWARD` |

The verifier recomputes:

- peak tail from `z >= 4`: slope `-0.9579`, `R^2 = 0.9801`, `n = 8`,
  matching the frozen printed `b^(-0.95)`, `R^2 = 0.980`;
- far tail from `z >= 5`: slope `-1.0578`, `R^2 = 0.9904`, `n = 7`,
  matching the frozen printed `b^(-1.05)`, `R^2 = 0.990`;
- mass-scaling exponent: `1.000003`, `R^2 = 1.000000`, `n = 6`,
  matching the frozen printed `F~M exponent: 1.000`.

## Question

Does the source-side wide-lattice `h^2+T` distance-law claim survive an
independent replay on `main` when we keep the same ordered 3D `1/L^2`
geometry family but freeze the wider `W = 12`, `h = 0.25` slice?

This note is intentionally narrow:

- one wide-lattice ordered 3D family
- valley-linear action
- `1/L^2` kernel with `h^2` measure
- distance tail plus the minimal sanity checks needed to promote it

## Frozen result

Independent wide replay at `h = 0.25`, `W = 12`, `L = 12`:

- Born: `4.82e-15`
- `k=0`: `0.000000`
- distance support: `10/10` TOWARD
- peak-tail fit from `z >= 4`: `b^(-0.95)`, `R^2 = 0.980`, `n = 8`
- far-tail fit from `z >= 5`: `b^(-1.05)`, `R^2 = 0.990`, `n = 7`
- `F~M` exponent: `1.000`

The important qualitative read is:

- the wide-lattice replay is cleanly attractive on all tested distance rows
- the far tail stays close to Newtonian
- the mass scaling remains linear
- the result is independently reproduced on `main`, not just borrowed from the
  branch summary

## Safe read

The strongest honest statement is:

- the wide-lattice `h^2+T` replay is a bounded frontier replay on `main`
- it is a strong finite-lattice replay with near-Newtonian far-tail behavior
- it is **not** yet a universal theorem or continuum-limit proof

## What this is not

- It is not a proof that the far-tail exponent is exactly `-1.00`.
- It is not a continuum theorem.
- It is not a replacement for the already-retained compact grown-geometry
  frontier.

The review-safe wording is:

- the wide-lattice replay strengthens the 3D `h^2+T` distance-law story
- the far tail is now independently reproducible on `main`
- the source-side wide-lattice claim is no longer just exploratory

## Final Verdict

**bounded frontier replay; independent audit required for effective status**
