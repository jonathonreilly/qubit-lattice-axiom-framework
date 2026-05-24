# Exact 2D Mirror Validation Note

**Date:** 2026-04-03 (registered-dependency citation tightened 2026-05-10 per audit `missing_dependency_edge` repair target).
**Status:** bounded review-safe exact 2D mirror coexistence pocket; no gravity-law promotion.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/mirror_2d_validation.py`](../scripts/mirror_2d_validation.py) — load-bearing 2D exact mirror linear propagator on three-slit Sorkin.
**Primary runner cache:** [`logs/runner-cache/mirror_2d_validation.txt`](../logs/runner-cache/mirror_2d_validation.txt) — load-bearing registered cached stdout (`exit_code=0`, `status=ok`) backing every row in the bounded table below.
**Imported authority:** [`scripts/mirror_born_audit.py`](../scripts/mirror_born_audit.py) — load-bearing dependency; provides `gen_2d_mirror` (exact 2D mirror generator) and `propagate_LINEAR` (strictly linear propagator) imported by the primary runner.
**Imported authority cache:** [`logs/runner-cache/mirror_born_audit.txt`](../logs/runner-cache/mirror_born_audit.txt) — load-bearing dependency registered cached stdout (`exit_code=0`, `status=ok`) verifying the imported generator and propagator on the strict mirror Born family.

This note freezes the exact 2D mirror validation lane. Both the primary
runner and the imported `mirror_born_audit.py` authority are recorded as
direct registered dependencies (one-hop), so the load-bearing exact-2D
mirror generator and linear propagator can be verified from the supplied
audit packet without delegating to a non-registered companion script.

Log:
[`logs/2026-04-03-mirror-2d-validation.txt`](../logs/2026-04-03-mirror-2d-validation.txt)

The exact 2D family uses the strict linear propagator only. Born safety is
verified on the same family via the corrected three-slit Sorkin audit.

## Setup

- exact 2D mirror generator from `scripts/mirror_born_audit.py`
- `npl_half = 12` (`24` total nodes per layer)
- `yr = 10.0`
- `connect_radius = 2.5`
- `8` seeds
- `k`-band: `[3, 5, 7]`
- `N = 25, 40, 60, 80, 100`

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

Source of truth: `scripts/mirror_born_audit.py` at commit b179c2d2c.

The three load-bearing definitions from the imported authority are pasted verbatim
below so the restricted audit packet is self-contained without requiring the full
helper file:

```python
def _topo_order(adj, n):
    in_deg = [0] * n
    for nbs in adj.values():
        for j in nbs:
            in_deg[j] += 1
    q = deque(i for i in range(n) if in_deg[i] == 0)
    order = []
    while q:
        i = q.popleft()
        order.append(i)
        for j in adj.get(i, []):
            in_deg[j] -= 1
            if in_deg[j] == 0:
                q.append(j)
    return order


def propagate_LINEAR(positions, adj, field, src, k, blocked):
    """STRICTLY LINEAR propagator. No normalization of any kind.
    This is the ONLY propagator used for Born claims on this branch."""
    n = len(positions)
    order = _topo_order(adj, n)
    amps = [0j] * n
    for s in src:
        amps[s] = 1.0 / len(src)
    for i in order:
        if abs(amps[i]) < 1e-30 or i in blocked:
            continue
        for j in adj.get(i, []):
            if j in blocked:
                continue
            if len(positions[i]) == 2:
                x1, y1 = positions[i]; x2, y2 = positions[j]
                dx, dy = x2-x1, y2-y1; dz = 0
            else:
                x1, y1, z1 = positions[i]; x2, y2, z2 = positions[j]
                dx, dy, dz = x2-x1, y2-y1, z2-z1
            L = math.sqrt(dx*dx + dy*dy + dz*dz)
            if L < 1e-10:
                continue
            lf = 0.5 * (field[i] + field[j])
            dl = L * (1 + lf)
            ret = math.sqrt(max(dl*dl - L*L, 0))
            act = dl - ret
            theta = math.atan2(math.sqrt(dy*dy + dz*dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            ea = cmath.exp(1j * k * act) * w / L
            amps[j] += amps[i] * ea
    return amps


# Generator 3: 2D mirror
def gen_2d_mirror(nl, npl_half, yr, cr, seed):
    rng = random.Random(seed); pos = []; adj = defaultdict(list); li = []; mm = {}; bl = nl // 3
    for layer in range(nl):
        x = float(layer); ln = []
        if layer == 0:
            pos.append((x, 0)); ln.append(len(pos)-1); mm[len(pos)-1] = len(pos)-1
        else:
            up, lo = [], []
            for _ in range(npl_half):
                y = rng.uniform(0.5, yr)
                iu = len(pos); pos.append((x, y)); up.append(iu)
                il = len(pos); pos.append((x, -y)); lo.append(il)
                mm[iu] = il; mm[il] = iu
            ln = up + lo
            lb = max(0, len(li) - (1 if layer == bl+1 else 2))
            for ci in up:
                cx, cy = pos[ci]
                for pl in li[lb:]:
                    for pi in pl:
                        px, py = pos[pi]
                        if math.sqrt((cx-px)**2+(cy-py)**2) <= cr:
                            adj[pi].append(ci); adj[mm[pi]].append(mm[ci])
        li.append(ln)
    return pos, dict(adj), bl
```

Module-level constants used by the helper code: `BETA = 0.8`, `N_SEEDS = 8`.

## Imported-authority cache excerpt (load-bearing, 2026-05-18)

The full registered cache file `logs/runner-cache/mirror_born_audit.txt` is
pasted verbatim below so the restricted audit packet contains the cached
stdout used to verify the imported generator and propagator on the strict
mirror Born family:

```
===== runner cache v1 =====
runner: scripts/mirror_born_audit.py
runner_sha256: ccbbc2f10c2187338017a1b7020815e452240f96245718fab15ea12d86a04270
timeout_sec: 120
exit_code: 0
elapsed_sec: 7.80
status: ok
----- stdout -----
================================================================================
BORN AUDIT: ALL MIRROR GENERATORS (LINEAR PROPAGATOR ONLY)
  8 seeds per generator
================================================================================

   3D chokepoint N=15 npl=25 r=4  mean=1.74e-16  max=4.84e-16  ok=3  PERFECT
   3D chokepoint N=25 npl=25 r=4  mean=1.32e-15  max=1.93e-15  ok=4  PERFECT
       3D hybrid N=25 npl=40 r=5  mean=1.67e-15  max=4.05e-15  ok=8  PERFECT
       3D hybrid N=40 npl=40 r=5  mean=1.44e-15  max=2.05e-15  ok=8  PERFECT
     2D mirror N=25 npl=12 r=2.5  mean=5.21e-16  max=7.79e-16  ok=8  PERFECT
     2D mirror N=40 npl=12 r=2.5  mean=6.53e-16  max=9.89e-16  ok=8  PERFECT

VERIFICATION: This script uses propagate_LINEAR which has
NO normalization of any kind. If Born passes here, the
linear propagator on these graph families is Born-clean.

----- stderr -----
```

## Retained Rows

The exact 2D mirror family is Born-clean and retains a strong bounded joint
coexistence pocket. The strongest retained row is `N = 60`.

| N | `MI` | `1-pur_min` | `d_TV` | gravity | Born `|I3|/P` | `k=0` |
|---|---:|---:|---:|---:|---:|---:|
| 25 | `0.502150` | `0.3029` | `0.6002` | `+2.7134` | `5.34e-16` | `0.00e+00` |
| 40 | `0.536689` | `0.3012` | `0.6217` | `+3.8891` | `7.75e-16` | `0.00e+00` |
| 60 | `0.756118` | `0.4420` | `0.8572` | `+2.5687` | `1.08e-15` | `0.00e+00` |
| 80 | `0.565264` | `0.3465` | `0.6740` | `+3.4065` | `2.60e-15` | `0.00e+00` |
| 100 | `0.346218` | `0.2865` | `0.5459` | `+1.8627` | `1.89e-15` | `0.00e+00` |

For comparison, the matched random chokepoint baseline at `N = 60` is much
weaker:

- `MI = 0.050745`
- `1 - pur_min = 0.0596`
- `d_TV = 0.1090`
- gravity `+0.7867`

So the exact 2D mirror family preserves substantially more which-slit
information and decoherence structure than the matched random baseline.

## Gravity Follow-Up

The same family was probed for a narrow gravity-side mass window and a
distance tail. Those fits are positive but not clean enough to promote as a
law.

### Fixed-Anchor Mass Window

- fit:
  - `delta ~= 0.8720 * M^0.132`
  - `R^2 = 0.167`

### Distance Sweep

- tail fit:
  - `delta ~= 0.3418 * b^0.320`
  - `R^2 = 0.075`

### Narrow read

- the exact 2D mirror family is review-safe for Born, MI, decoherence, and a
  positive gravity read
- the gravity-side fit quality is weak, so no mass-law or distance-law claim
  is promoted here
- the best retained statement is a **bounded exact 2D mirror coexistence
  pocket**, strongest at `N = 60`

## What this note does NOT claim

- A promoted 2D mirror gravity law (mass or distance).
- That the bounded coexistence pocket holds beyond the retained sweep
  `N ∈ {25, 40, 60, 80, 100}` at the stated parameter card.
- Any conclusion that depends on a non-registered companion script; the
  load-bearing computation closes from the primary runner cache plus the
  registered imported-authority cache (`mirror_born_audit.py`).

## Audit boundary (2026-05-10 — registered-dependency citation tightened)

This revision addresses the generated-audit repair target:

> missing_dependency_edge — add scripts/mirror_born_audit.py and its cached
> stdout as a direct audited dependency for this claim, then re-audit the
> bounded runner-backed pocket.

This revision lifts `scripts/mirror_born_audit.py` and its registered cache
`logs/runner-cache/mirror_born_audit.txt` into the note header as direct
load-bearing dependencies, so the audit packet has both one-hop authorities
on hand: the primary runner cache for the table rows, and the imported
generator/propagator cache for the exact-mirror linear-propagator premise.
The bounded-row table itself is unchanged.

## Registered runner artifacts

The 2D mirror validation lane uses the exact 2D mirror generator and linear
propagator from a registered companion script. Both runner sources and both
caches are present in the worktree as direct one-hop dependencies:

- Primary runner: `scripts/mirror_2d_validation.py` (registered runner whose
  cached stdout backs every bounded row in this note's table).
- Primary runner cache: `logs/runner-cache/mirror_2d_validation.txt`
  (registered cached stdout; `exit_code=0`, `status=ok`).
- Imported generator/propagator authority: `scripts/mirror_born_audit.py`
  (provides `gen_2d_mirror` and `propagate_LINEAR`, imported by the primary
  runner — load-bearing for the exact-2D mirror linear-propagator premise).
- Imported authority cache: `logs/runner-cache/mirror_born_audit.txt`
  (registered cached stdout; `exit_code=0`, `status=ok`).

Both authorities are registered in `logs/runner-cache/`. The bounded table
rows close from the primary runner cache; the exact-2D-mirror linear-
propagator premise closes from the imported-authority cache.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `MIRROR_PROGRAM_SYNTHESIS.md` (meta synthesis, bookkeeping-only — demoted from
  markdown-link form per the 2026-05-23 `audited_conditional` verdict noting
  that the cited authority was "a meta synthesis that expressly does not
  establish retained claims"; the load-bearing closure runs through the
  primary runner + cache + imported authority listed in the header).

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/mirror_born_audit.py`
