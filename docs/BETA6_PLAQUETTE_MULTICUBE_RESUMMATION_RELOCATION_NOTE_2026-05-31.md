# Beta=6 SU(3) Plaquette: Cube-Cluster Sectors are K-Built Through β⁹; the Cube Singularity is a Multiplicity-Resummation Limit

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and effective
status.
**Status authority:** independent audit lane only. This source note does not
quote, set, or predict an audit outcome for any cited claim_id.
**Primary runner:** [`scripts/frontier_beta6_multicube_resummation_relocation.py`](../scripts/frontier_beta6_multicube_resummation_relocation.py)
**Closure outcome:** none. This relocates the `beta=6` obstruction from
coefficient extraction to the cluster/multiplicity RESUMMATION. It is NOT a
closure of `Delta` or of `beta=6` and asserts no value of `<P>(6)`.

## 0. What this extends

The cube-sector closed form
`BETA6_PLAQUETTE_CUBE_SECTOR_CLOSED_FORM_GENERATING_FUNCTION_NOTE_2026-05-31.md`
(PR #2440) showed the four-cube-shell sector of
`Delta(beta) = P_full - P_1plaq = sum_{n>=5} d_n beta^n` equals
`72 K''(K')^5`, `K = log J`, with `J` the single-plaquette character generating
function from the on-main retained character recurrence, and that its dominant
singularity is the nearest zero of `J` at `8.2052 e^{+- i 66.152 deg} > 6`. This
note answers the question that opened: **is every finite cube-cluster sector also
built from `K = log J` (hence analytic past `beta=6`), so that the conjectured
`~5.7 < 6` dominant singularity of the full `Delta` is a RESUMMATION effect
rather than a property of any sector?**

## 1. `K = log J` is the single-plaquette cumulant generating function

Reproven (runner): `kappa_m := m! [beta^m] K` equals the engine's `m`-fold free
connected plaquette cumulant, with

```text
kappa_2 = 1/18,  kappa_3 = 1/108,  kappa_4 = 0,  kappa_5 = -5/3888,
```

and `K'(beta) = beta/18 + O(beta^2)` (leading slope `1/18` framework-derived
from `a_2 = 1/36`, not the supplied `u = beta/18` convention). So a face
self-dressed by its full multiplicity tower contributes exactly the derivative
`K^{(r)}` of order `r` = its valence in the connected backbone.

## 2. K-built sectors and the Euler closed-surface law

A fixed cluster sector resums to a finite polynomial in `{K', K'', ...}` **iff
every link of the cluster meets at most 2 faces** — then each link carries the
balanced `(p,p)` content `N0(1,1)=1, N0(2,2)=2, ...` that `J` already generates,
and the per-face multiplicity sums separate into independent `K`-derivatives.
For any genus-0 closed plaquette surface of `F` faces the leading free cumulant
is `2 (1/6)^F 3^{V-E} = 18^{1-F}` (Euler `V-E = 2-F`): cube (`F=6`) → `1/18^5`,
two-cube box boundary (`F=10`) → `1/18^9` (both reproven).

- **The cube** is `72 K''(K')^5` (marked face → `K''`, 5 action faces → `K'`),
  exact through `d_8` (PR #2440).
- **The entire order-`beta^9` two-cube-overlap sector** (two cubes sharing a
  *non-marked* face) is a clean 2-face-per-link box surface containing `p0`,
  hence **K-built**. *Engine-probe corroboration (not recomputed in this note's
  runner):* all 48 such supports through `p0` have leading cumulant `1/18^9`,
  consistent with the Euler law above.

Therefore the cube sector and the full order-`beta^9` two-cube sector are
analytic on `|beta| < 8.2052 > 6` — **convergent at `beta=6`**.

## 3. The first obstruction is the SU(3) ε/baryon channel, at order β¹⁰

The K-built factorization fails at a `>= 3`-face link junction, which reaches the
**unbalanced `(3,0)` invariant** absent from `J`'s diagonal tower:
`N0(3,0) = #singlets in fund^{x3} = 1` (`3 x 3 x 3 = 1 + 8 + 8 + 10`), the
SU(3) ε/baryon contraction. Such a junction first appears when **two cubes share
the MARKED face** `p0` (its 4 links become 3-face junctions). *Engine-probe
corroboration:* that sector's leading cumulant is `3/18^10` (the `N_c = 3` ε
channel), an order-`beta^10` object. So the first place a sector can carry
non-`K` analytic content (and a potentially closer singularity) is `beta^10`.

## 4. The decisive fact: 8.2052 is itself a multiplicity-resummation limit

`K' = J'/J` resums the *infinite* tower of multiplicity insertions per face. A
finite-multiplicity ("bare") cube is entire; the `8.2052` branch point appears
**only** in the full resummation. Truncating `J` to degree `T` (keeping `T`
insertions) moves the nearest singularity (reproven by `mpmath` root-finding):

| `T` | 3 | 5 | 8 | 12 | 20 |
|---|---|---|---|---|---|
| nearest singularity | **5.74** | 6.36 | 7.39 | 8.13 | 8.205 |

The truncated singularity **migrates monotonically from `5.74` (below 6) up to
the full-tower limit `8.2052`**.

## 5. Statement and scope (honesty, non-negotiable)

> **Result.** Every cube-cluster sector of `Delta` through order `beta^9` is
> K-built (a polynomial in derivatives of `K = log J`), hence analytic on
> `|beta| < 8.2052 > 6` and convergent at `beta=6`. The K-built structure first
> breaks at order `beta^10` via the SU(3) ε/baryon channel. Consequently **every
> finite truncation of the connected series through `beta^9` sees only the
> `8.2052` singularity, never a singularity below `6`** — and that `8.2052` is
> itself a multiplicity-resummation limit (the bare cube is entire).

> **Relocation.** The conjectured full-`Delta` dominant singularity near
> `|beta_c| ~ 5.7 < 6` (the unproven complex-pair premise scoped in
> [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md))
> is therefore **not** a property of any individual cube-cluster sector; it is a
> RESUMMATION effect — of the per-face multiplicity tower (Section 4) and of the
> cluster proliferation over infinitely many sectors. This **explains** why every
> finite-order coefficient cycle has been unable to close `beta=6` (each finite
> computation only ever resolves the `8.2052` singularity).

**What is NOT claimed.** This note proves no value of `<P>(6)` or `Delta(6)`,
does not pin the exact `5.7`, and does not establish the cluster-proliferation
radius factorization (`R_full = 8.2052 / g`, `g` the inter-cluster growth) — that
factorization is a heuristic, the natural next target, and is **not** a result of
this note. The order-`beta^9` 48-support sum and the order-`beta^10` `3/18^10`
leading cumulant are engine-probe results cited as corroboration, not recomputed
in this runner. No Monte-Carlo value, fitted parameter, or imported literature
coefficient is used; the analytic core is reproven from the retained recurrence.

## 6. Audit consequence

```yaml
claim: beta6_plaquette_multicube_resummation_relocation
result: cube_cluster_sectors_K_built_through_beta9; first_break_epsilon_channel_beta10; 8.2052_is_a_multiplicity_resummation_limit
relocation: beta6_obstruction_is_a_resummation_effect_not_a_single_sector_singularity
import_free_core: true
exact_5p7_and_cluster_proliferation_factorization: open_heuristic   # NOT claimed
beta6_status: not_closed
forbidden_imports_used: false
audit_status_authority: independent audit lane only
```

## 7. Runner

```bash
python3 scripts/frontier_beta6_multicube_resummation_relocation.py
```

Expected: `SCORECARD: PASS=12 FAIL=0`. The runner reproves the `kappa_m`
cumulant identity, the Euler closed-surface law (`18^{1-F}`), the ε-channel
singlet count `N0(3,0)=1`, and the multiplicity-truncation migration
`5.74 -> 8.2052`, all in exact `Fraction`/`sympy`/`mpmath` arithmetic from the
retained recurrence.

## 8. Key files

- [`scripts/frontier_beta6_multicube_resummation_relocation.py`](../scripts/frontier_beta6_multicube_resummation_relocation.py)
- `BETA6_PLAQUETTE_CUBE_SECTOR_CLOSED_FORM_GENERATING_FUNCTION_NOTE_2026-05-31.md`
- [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)

This note is a bounded theorem (one structural result) and asserts no closure of
the `beta=6` lane.
