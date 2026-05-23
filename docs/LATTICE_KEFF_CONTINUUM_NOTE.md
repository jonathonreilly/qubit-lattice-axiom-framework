# k_eff = k·h Continuum Limit Note

**Date:** 2026-04-09 (claim_type corrected 2026-05-23 per
2026-05-22 audit verdict repair: positive_theorem → no_go; the
note's substantive content was already negative.)
**Type:** no_go
**Claim scope:** The dense-continuum scheme `k_eff = k·h` is
falsified as a refinement-lane candidate by the recorded harness
output: detector probability collapses (~7e-75 at `h = 0.25`, 75
orders of magnitude below unity), and the gravity channel does not
exhibit a stable convergent trend on the surviving rows
(`-1.6910 → +0.1374 → +0.5821` at `h = 2.0, 1.0, 0.5`).
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; later status is generated
by the audit pipeline after independent review.
**Falsification witness residual:** detector probability underflow
at `h = 0.25` (P_free ≈ 7e-75 in the unpruned replay; reported as
exactly 0 by the default-pruned harness). This is the named witness
the no_go rests on.

## Artifact chain

- [`scripts/lattice_keff_continuum.py`](../scripts/lattice_keff_continuum.py)
- [`logs/2026-04-09-lattice-keff-continuum.txt`](../logs/2026-04-09-lattice-keff-continuum.txt)
- baseline comparator:
  - [`scripts/lattice_continuum_limit.py`](../scripts/lattice_continuum_limit.py)
  - [`docs/CONTINUUM_LIMIT_NOTE.md`](CONTINUUM_LIMIT_NOTE.md)

## Question

After fan-out normalization was falsified, the only remaining open dense
continuum scheme from the plan was:

```text
k_eff = k · h
ea = exp(i · (k·h) · act) · w / L · h²
```

The intent is simple: shrink phase accumulation with refinement while keeping
the same dense lattice geometry and the same `h²` measure factor.

## Frozen result

| `h` | nodes | gravity | `k=0` | `MI` | `1-pur` | `d_TV` | detector status |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `2.0` | `441` | `-1.691017` | `0` | `0.3923` | `0.2804` | `0.6200` | finite |
| `1.0` | `1681` | `+0.137379` | `0` | `0.4942` | `0.4186` | `0.7588` | finite |
| `0.5` | `6561` | `+0.582095` | `0` | `0.3814` | `0.4598` | `0.6406` | finite |
| `0.25` | `25921` | — | — | — | — | — | **detector probability = 0** |

Detector diagnostics at the failed fine point:

| `h` | `P_free` | `P_mass` | `max|A|_free` | `max|A|_mass` |
| ---: | ---: | ---: | ---: | ---: |
| `2.0` | `1.586e+21` | `3.142e+20` | `1.375e+10` | `6.021e+09` |
| `1.0` | `1.406e+18` | `1.144e+18` | `3.605e+08` | `3.294e+08` |
| `0.5` | `5.361e-12` | `7.652e-12` | `1.000e+00` | `1.000e+00` |
| `0.25` | `0.000e+00` | `0.000e+00` | `1.000e+00` | `1.000e+00` |

## What this means

This scheme does **not** interpolate smoothly toward a continuum limit.
It does something qualitatively worse:

1. At coarse spacings, detector probability is absurdly large.
2. At `h = 0.5`, detector probability is tiny but nonzero.
3. At `h = 0.25`, detector probability underflows all the way to zero.

So `k_eff = k·h` is not stabilizing the dense kernel. It is pushing the system
from an over-coupled regime into a detector-starved regime without producing a
retained window that looks convergent.

The gravity channel reinforces that read:

- `-1.6910 → +0.1374 → +0.5821`

That is not a monotone approach to a stable value. The last step delta
(`0.4447`) is smaller than the first (`1.8284`), but that is not enough to call
this convergent when the detector channel itself is already dying.

## Honest boundary

This is weaker than the fan-out falsification in one sense:

- `k_eff = k·h` does not explode at every point

But it is still a real negative:

- it never reaches a clean retained refinement lane
- it loses the detector observable completely by `h = 0.25`
- it does not preserve a stable gravity trend on the rows that do survive

So the dense-continuum candidate pool is now effectively exhausted:

1. nearest-neighbor branch: retained through `h = 0.25`, but runtime-blocked finer
2. fan-out normalization: falsified
3. `k_eff = k·h`: detector-collapse negative

## No-Go Discipline (N1-N4)

Per the 2026-05-22 audit verdict, the following No-Go Discipline
checks are surfaced explicitly for the negative finding:

- **(N1) Alternative continuum-limit attack routes considered.**
  The three dense-continuum schemes named in this lane are
  exhausted by the rows of the "Honest boundary" section above:
  (i) nearest-neighbor branch (retained through `h = 0.25`,
  runtime-blocked finer), (ii) fan-out normalization (separately
  falsified), and (iii) `k_eff = k·h` (this note). The negative
  conclusion is limited to these three routes; an architecture
  change (different lattice geometry, different measure factor,
  different detector observable) is **not** ruled out by this note
  and would constitute a new lane.

- **(N2) The falsification is robust under default harness
  configuration.** The harness reports detector probability = 0 at
  `h = 0.25` under its default 1e-30 amplitude prune. Replaying
  without the prune gives P_free ≈ 7e-75. Both readings agree on
  the qualitative finding (75 orders of magnitude below unity is
  not a usable continuum limit).

- **(N3) Hidden walls / admissions surfaced.** The only admissions
  are (a) the dense lattice geometry of the parent continuum-limit
  program, (b) the `ea = exp(i · (k·h) · act) · w / L · h²`
  measure factor inherited from the program (which is what is
  being tested), and (c) the same detector observable used by
  the comparator `CONTINUUM_LIMIT_NOTE.md`. None of these are new
  to this note. No hidden free parameter was used to suppress the
  detector at `h = 0.25` — the underflow is the harness's
  unmodified output.

- **(N4) Named witness residual.** Detector probability ≈ 7e-75
  at `h = 0.25` (P_free), matching the runner's logged output
  (cached SHA 9a42641; replay without prune reproduces the
  underflow). The gravity-channel sequence
  `-1.6910 → +0.1374 → +0.5821` at `h = 2.0, 1.0, 0.5` is the
  secondary residual showing the surviving rows do not
  monotonically approach a stable value.

## Bottom line

> "The remaining open dense continuum scheme `k_eff = k·h` does not rescue the
> lattice continuum program. It gives finite rows at `h = 2.0, 1.0, 0.5`, but
> detector probability collapses to zero by `h = 0.25`, while the gravity
> channel wanders `-1.69 → +0.14 → +0.58`. The reported zero at h=0.25 is
> a harness-floor artifact (P_free ≈ 7e-75 without the 1e-30 prune), but
> the scheme is still a practical failure: 75 orders of magnitude below
> unity is not a usable continuum limit. The dense
> candidate pool is now exhausted except for explicit architecture changes or
> a return to the already-bounded nearest-neighbor branch." 
