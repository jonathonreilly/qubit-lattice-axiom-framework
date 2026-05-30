# Audited Symmetry Synthesis Note

**Date:** 2026-04-03 (scope narrowed 2026-05-26)
**Status:** bounded synthesis candidate on registered finite authority
surfaces only; no unified mirror or `Z₂ × Z₂` family theorem.
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after independent review.

This note consolidates the symmetry-program results after a direct audit of the
current code and saved artifacts. The goal is to separate the claims that are
solid enough to synthesize now from the ones that are still one step short.

## Scope narrowing (2026-05-26)

This revision takes the audit-requested narrowing path. The synthesis claim is
only the conjunction of the registered finite surfaces cited below:

- exact mirror strict-card chokepoint: the default `NPL_HALF=25`,
  `connect_radius=4.0`, `layer2_prob=0.0` card at `N=15` and `N=25` in
  [`docs/MIRROR_CHOKEPOINT_NOTE.md`](MIRROR_CHOKEPOINT_NOTE.md).
- dense mirror boundary card: the separate `NPL_HALF=60`,
  `connect_radius=5.0`, `layer2_prob=0.0` boundary certificate through
  `N=100` in
  [`docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md`](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md).
- mirror MI diagnostic: the separate mid-`N` information-theoretic diagnostic
  in
  [`docs/MIRROR_MUTUAL_INFORMATION_CHOKEPOINT_NOTE.md`](MIRROR_MUTUAL_INFORMATION_CHOKEPOINT_NOTE.md).
- exact 2D mirror: the registered exact-2D validation packet in
  [`docs/MIRROR_2D_VALIDATION_NOTE.md`](MIRROR_2D_VALIDATION_NOTE.md).
- `Z₂ × Z₂`: only the SHA-pinned 16-seed registered cache for
  `N=25,40,60,80` in
  [`logs/runner-cache/higher_symmetry_joint_validation.txt`](../logs/runner-cache/higher_symmetry_joint_validation.txt)
  and
  [`docs/HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md`](HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md).

No dense `Z₂ × Z₂` `N=120` promotion, whole-window mirror MI advantage,
single-surface mirror-family theorem, or asymptotic symmetry law is part of
this synthesis claim.

## Primary Artifacts

- exact mirror / bounded coexistence:
  [`docs/MIRROR_CHOKEPOINT_NOTE.md`](MIRROR_CHOKEPOINT_NOTE.md)
- dense mirror boundary card:
  [`docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md`](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md)
- higher-symmetry joint validation:
  [`docs/HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md`](HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md)
  [`logs/runner-cache/higher_symmetry_joint_validation.txt`](../logs/runner-cache/higher_symmetry_joint_validation.txt)
- higher-symmetry gravity follow-up:
  [`docs/HIGHER_SYMMETRY_GRAVITY_PROBE_NOTE.md`](HIGHER_SYMMETRY_GRAVITY_PROBE_NOTE.md)
- exact 2D mirror validation:
  [`docs/MIRROR_2D_VALIDATION_NOTE.md`](MIRROR_2D_VALIDATION_NOTE.md)
  [`../scripts/mirror_2d_validation.py`](../scripts/mirror_2d_validation.py)
  [`../logs/runner-cache/mirror_2d_validation.txt`](../logs/runner-cache/mirror_2d_validation.txt)
- structured-growth reproduction:
  [`../logs/2026-04-03-structured-mirror-growth.txt`](../logs/2026-04-03-structured-mirror-growth.txt)
- structured-growth Born audit:
  [`../scripts/structured_mirror_born_audit.py`](../scripts/structured_mirror_born_audit.py)
  [`../logs/2026-04-03-structured-mirror-born-audit.txt`](../logs/2026-04-03-structured-mirror-born-audit.txt)

## What Is Solid Now

### 1. Exact symmetry really matters

The cited exact-mirror authorities are already narrowed to finite registered
surfaces. The current safe statement is still:

- random growth tends toward the CLT / rank-1 ceiling
- exact discrete symmetry can delay or prevent that convergence in bounded
  windows
- approximate or heuristic symmetry is not enough to inherit the same benefit

The exact mirror chokepoint lane remains the canonical parity-protected
strict-card result, but only on its registered default card:

- Born-clean at machine precision
- positive gravity
- decohering at `N=15` and `N=25` on the strict default card

That result is frozen in
[`docs/MIRROR_CHOKEPOINT_NOTE.md`](MIRROR_CHOKEPOINT_NOTE.md). The dense
`NPL_HALF=60`, `connect_radius=5.0` boundary card through `N=100` is a
separate finite authority in
[`docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md`](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md),
not a stitched extension of the strict-card note.

### 2. `Z₂ × Z₂` is a real bounded coexistence lane

The higher-symmetry joint validator survives as a registered finite
`Z₂ × Z₂` coexistence lane on the SHA-pinned 16-seed cache for
`N=25,40,60,80`. The cache records:

- Born-clean at machine precision
- `k=0` exactly zero
- positive band-averaged gravity on all four `Z₂ × Z₂` rows
- slower bounded decoherence decay than random on this finite cache

Bounded validated rows:

| N | `d_TV` | `pur_cl` | gravity-band | Born | `k=0` | ok |
|---|---:|---:|---:|---:|---:|---:|
| 25 | `0.893±0.034` | `0.616±0.032` | `+0.580±0.412` | `5.91e-16±1.53e-16` | `0.00e+00±0.00e+00` | `15` |
| 40 | `0.862±0.029` | `0.661±0.035` | `+0.706±0.576` | `3.85e-16±1.75e-16` | `0.00e+00±0.00e+00` | `15` |
| 60 | `0.698±0.050` | `0.682±0.036` | `+0.879±0.656` | `7.34e-16±2.10e-16` | `0.00e+00±0.00e+00` | `15` |
| 80 | `0.540±0.052` | `0.782±0.028` | `+1.996±0.542` | `1.80e-15±4.68e-16` | `0.00e+00±0.00e+00` | `15` |

Its bounded decoherence fit is:

- `1 - pur_cl ~= C * N^alpha`
- `alpha = -0.430`
- bootstrap `95% CI [-0.678, -0.199]`

So `Z₂ × Z₂` is synthesis-grade only as this finite registered
coexistence-lane packet. The dense `N=80/100/120` promotion remains out of
binding scope until the missing dense joint-validation log or registered cache
is supplied.

### 3. The higher-symmetry gravity law is still not clean

The gravity-side follow-up on dense `Z₂ × Z₂` remains useful but negative for
the stronger claim:

- mass windows are positive but weak / non-monotone
- distance sweeps show broad bumps rather than one registered law

So the safe summary is:

- `Z₂ × Z₂` is a real finite coexistence lane
- it is not yet a clean gravity-law lane

## What Does **Not** Survive Audit Yet

### 1. Structured mirror growth is not currently Born-safe

The geometry result is real: the current structured-growth script reproduces a
strong grown-graph pocket with substantial decoherence and strong positive
gravity. For example, the reproduced current rows are:

| config | N | `pur_min` | gravity |
|---|---:|---:|---:|
| `npl_half=15, d=2` | 25 | `0.7700` | `+1.454` |
| `npl_half=20, d=2` | 25 | `0.8123` | `+2.654` |
| `npl_half=30, d=2` | 30 | `0.8869` | `+3.966` |

But the current propagator in
[`../scripts/structured_mirror_growth.py`](../scripts/structured_mirror_growth.py)
uses explicit per-layer normalization, so Born cannot be assumed. The direct
audit in
[`../logs/2026-04-03-structured-mirror-born-audit.txt`](../logs/2026-04-03-structured-mirror-born-audit.txt)
finds:

- min `|I3|/P = 1.000000`
- median `|I3|/P = 1.000000`
- max `|I3|/P = 1.000000`

across all tested 3-slit combinations on the representative `N=25`,
`npl_half=15`, `d=2` lane.

So the current safe interpretation is:

- **geometry win:** yes
- **Born-clean grown successor:** no, not with the current layer-norm propagator

### 3. Exact mirror MI is now artifact-backed, but bounded

The mirror-specific MI chain is now frozen in:

- [`../scripts/mirror_mutual_information_chokepoint.py`](../scripts/mirror_mutual_information_chokepoint.py)
- [`../logs/2026-04-03-mirror-mutual-information-chokepoint-n60-r5p0.txt`](../logs/2026-04-03-mirror-mutual-information-chokepoint-n60-r5p0.txt)
- [`docs/MIRROR_MUTUAL_INFORMATION_CHOKEPOINT_NOTE.md`](MIRROR_MUTUAL_INFORMATION_CHOKEPOINT_NOTE.md)

On the separately scoped dense exact mirror boundary card, the mirror MI
diagnostic keeps a clear mid-`N` advantage over the matched random baseline,
but the comparison is not monotone and does not support a clean slower-decay
theorem:

- `N=40`: mirror MI `0.4295±0.068` bits vs random `0.1774±0.034`
- `N=60`: mirror MI `0.1973±0.041` bits vs random `0.0846±0.032`
- `N=80`: mirror MI `0.1385±0.021` bits vs random `0.0564±0.018`
- `N=100`: mirror MI `0.0408±0.011` bits vs random `0.0574±0.021`

The CL-bath purity stays in the same bounded pocket, but the MI and purity
orderings are not identical. The important synthesis point is:

- the dense mirror boundary card has a real, review-safe, bounded mid-`N` MI
  advantage at `N=40,60,80`
- the `N=100` MI row fails the mirror-advantage ordering
- the exponent fit is too noisy to claim a global asymptotic theorem

The canonical 3D mirror MI artifact remains useful too:

- `S4` mirror:
  - `N=25`: `0.7213±0.073` bits
  - `N=40`: `0.5956±0.067` bits
  - `N=60`: `0.5248±0.067` bits
  - `N=80`: `0.2559±0.047` bits

So the earlier “not artifact-backed” concern is resolved for both the
canonical 3D mirror MI chain and the new exact 2D mirror validation chain.
The exact 2D lane should be treated as the more review-safe family-level
confirmation, while the canonical `S4` lane remains the scalable MI lane.

### 3. The `Z₂`-breaking fragility curve is not registered as a repo artifact

The branch history contains a strong prose claim that controlled mirror-edge
dropout rapidly destroys the symmetry benefit. That claim is plausible and
scientifically interesting, but I did **not** find a registered script/log pair
for it in the current repo snapshot.

So the fragility story should be treated as:

- **interesting working claim:** yes
- **synthesis-grade registered artifact:** not yet

## Synthesis-Grade Story

The strongest bounded synthesis story this note proposes for re-audit is:

1. random growth fails by a rank-1 / CLT-type mechanism
2. exact discrete symmetry can preserve distinct sectors and delay that failure
3. exact mirror symmetry gives a finite strict-card coexistence pocket at
   `N=15` and `N=25`
4. exact 2D mirror gives a review-safe bounded coexistence pocket with strong
   MI and dTV separation on the same family
5. `Z₂ × Z₂` strengthens the decoherence side and remains Born-clean,
   `k=0`-clean, and gravity-band-positive on the registered 16-seed
   `N=25,40,60,80` packet
6. structured mirror growth shows that the geometry idea is not purely an
   imposed toy, but its **current** propagation rule is not Born-safe

So the program is not yet “fully mature” in the strongest sense. The accurate
statement is:

- **mature finite bounded symmetry program:** yes, across the registered
  authority surfaces named above
- **fully unified axiom-compliant grown Born+gravity+decoherence lane:** not yet

## Best Next Wins

The highest-value next steps are now sharply defined:

1. Replace or linearize the structured-growth propagator so the grown symmetry
   lane can be Born-audited cleanly.
2. Register the `Z₂`-breaking fragility curve with an actual script/log pair.
3. Keep `Z₂ × Z₂` as the strongest bounded coexistence lane while the grown
   lane is repaired.
4. Use exact 2D mirror as the family-level confirmation while the grown lane
   is repaired.

## Bottom Line

Proceed on solid ground by making exact 2D mirror, registered-cache
`Z₂ × Z₂`, the strict-card exact mirror pocket, and the separately scoped
dense mirror boundary/MI diagnostics the synthesis headline. Treat structured
mirror growth as a promising geometry result that still needs a Born-safe
propagator before it can become the canonical successor lane.
