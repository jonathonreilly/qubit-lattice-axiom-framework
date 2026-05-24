# k_eff = k·h Continuum Limit Note

**Date:** 2026-04-09 (claim type corrected 2026-05-23; the note's
substantive content was already negative.)
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
usable window that looks convergent.

The gravity channel reinforces that read:

- `-1.6910 → +0.1374 → +0.5821`

That is not a monotone approach to a stable value. The last step delta
(`0.4447`) is smaller than the first (`1.8284`), but that is not enough to call
this convergent when the detector channel itself is already dying.

## Honest boundary

This is weaker than the fan-out falsification in one sense:

- `k_eff = k·h` does not explode at every point

But it is still a real negative:

- it never reaches a clean usable refinement lane
- it loses the detector observable completely by `h = 0.25`
- it does not preserve a stable gravity trend on the rows that do survive

So the dense-continuum candidate pool is now effectively exhausted:

1. nearest-neighbor branch: bounded through `h = 0.25`, but runtime-blocked finer
2. fan-out normalization: falsified
3. `k_eff = k·h`: detector-collapse negative

## No-Go Discipline (N1-N8)

This is a narrow no-go: only the dense-continuum scheme `k_eff = k·h` is
falsified as a refinement-lane candidate on this harness. Architecture changes
and the already-bounded nearest-neighbor branch are explicitly out of scope.

- **(N1) Alternative attack routes.**
  1. **Prune-artifact route (ATTEMPTED).** Treat the `h = 0.25` zero as only
     a 1e-30 prune artifact. Replaying without the prune gives
     `P_free ≈ 7e-75`, so the detector is nonzero only at a practically
     unusable scale.
  2. **Gravity-only route (ATTEMPTED).** Ignore detector probability and rely
     on gravity convergence. The surviving gravity rows
     `-1.6910 → +0.1374 → +0.5821` change sign and do not show a stable
     limiting trend.
  3. **Nearest-neighbor comparison route (RULED OUT BY PRIOR).**
     [`LATTICE_NN_CONTINUUM_NOTE.md`](LATTICE_NN_CONTINUUM_NOTE.md) is a
     separate bounded route through `h = 0.25`; it does not rescue this dense
     `k_eff = k·h` scheme.
  4. **Fan-out normalization route (RULED OUT BY PRIOR).**
     [`LATTICE_FANOUT_CONTINUUM_NOTE.md`](LATTICE_FANOUT_CONTINUUM_NOTE.md)
     records a different dense scheme as falsified, so it does not rescue this
     scheme.
  5. **Architecture-change route (NOT CLOSED; EXCLUDED FROM CLAIM).** Change
     architecture, geometry, measure factor, or detector observable. Those are
     legitimate future lanes, so this note excludes them instead of pretending
     this no-go closes them.

- **(N2) Wall-independence audit.** There are two load-bearing walls:
  detector starvation at `h = 0.25` and lack of stable gravity convergence on
  the surviving rows.

  | pair | closes automatically? | result |
  |---|---|---|
  | detector starvation → gravity convergence | no | a detector repair would still need a stable gravity trend |
  | gravity convergence → detector starvation | no | a smoother gravity trend would still leave the detector unusable at `h = 0.25` |

  The collapsed wall set is therefore the same two-wall set within the current
  harness.

- **(N3) Hidden-wall scan.** The assumptions are explicit: dense lattice
  geometry from the parent continuum-limit program, the inherited
  `ea = exp(i · (k·h) · act) · w / L · h²` measure factor being tested, and
  the detector observable used by the comparator
  [`CONTINUUM_LIMIT_NOTE.md`](CONTINUUM_LIMIT_NOTE.md). No hidden tuning or
  free parameter is used to suppress the detector at `h = 0.25`.

- **(N4) Residual matching.**

  | witness | residual attacked | residual claimed here | match |
  |---|---|---|---|
  | [`scripts/lattice_keff_continuum.py`](../scripts/lattice_keff_continuum.py), default run | detector probability at `h = 0.25` reports zero | detector starvation blocks this scheme's usable refinement lane | yes |
  | unpruned replay of the same propagation/readout | `P_free ≈ 7e-75` at `h = 0.25` | prune floor is not the only issue; the detector scale is still unusable | yes, support-only |
  | [`scripts/lattice_keff_continuum.py`](../scripts/lattice_keff_continuum.py), surviving rows | gravity sequence `-1.6910 → +0.1374 → +0.5821` | surviving rows do not establish continuum closure | yes |

- **(N5) Rhetoric audit.** The no-go is not phrased as "no continuum limit is
  possible." It is only "this dense `k_eff = k·h` scheme does not rescue the
  dense-continuum lane on this detector/harness." Per-site, per-mode, and
  architecture-level alternatives are not ruled out.

- **(N6) Partial-closure path scan.** A convention reframe cannot repair this
  row because the blocker is numerical detector starvation plus unstable
  gravity trend, not a naming or status-class issue. A future lane may still
  change the architecture, measure, detector observable, or return to the
  bounded nearest-neighbor branch.

- **(N7) Steelman.** The strongest counterargument is that the detector floor
  is a harness readout problem, not a physics problem: since the unpruned
  replay is nonzero on detector nodes, a logarithmic observable, rescaled
  amplitude representation, or different detector normalization might recover
  usable data. This does not overturn the current claim because the note's
  scope is the existing detector/readout scheme; it does define a valid future
  architecture-change lane.

- **(N8) Cross-cycle echo.** Similar prior failures in this repo often became
  bounded rather than universal negatives when a branch changed geometry,
  normalization, or detector observable. This note follows that pattern by
  limiting the no-go to the current dense `k_eff = k·h` scheme and leaving
  architecture changes outside the claim.

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
