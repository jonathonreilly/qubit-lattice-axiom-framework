# Persistent Object Blended Readout Outer Transfer Sweep

**Date:** 2026-04-16  
**Status:** bounded widened local compact-object response positive with a mapped inward-source boundary; still not a persistent inertial-mass closure

## Artifact chain

- Outer sweep script: [`scripts/persistent_object_blended_readout_outer_transfer_sweep.py`](/Users/jonreilly/Projects/Physics/scripts/persistent_object_blended_readout_outer_transfer_sweep.py)
- Outer sweep log: [`logs/2026-04-16-persistent-object-blended-readout-outer-transfer-sweep.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-16-persistent-object-blended-readout-outer-transfer-sweep.txt)
- Boundary script: [`scripts/persistent_object_blended_readout_inner_source_boundary_probe.py`](/Users/jonreilly/Projects/Physics/scripts/persistent_object_blended_readout_inner_source_boundary_probe.py)
- Boundary log: [`logs/2026-04-16-persistent-object-blended-readout-inner-source-boundary-probe.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-16-persistent-object-blended-readout-inner-source-boundary-probe.txt)

## `_run_mode` helper + boundary cert scope narrowing (load-bearing for restricted packet, inlined 2026-05-18)

The auditor flagged two restricted-packet gaps. This section repairs both in
place so the bounded outer headline (`top3 4/5`, `top2 1/5`) is self-contained
and the inward-source boundary claim is honestly narrowed.

### Gap 1 — `_run_mode` helper is the actual physics

Both `scripts/persistent_object_blended_readout_outer_transfer_sweep.py` and
`scripts/persistent_object_blended_readout_inner_source_boundary_probe.py`
delegate the physics to a single helper

  `scripts.persistent_object_blended_readout_transfer_sweep._run_mode`.

The helper body (verbatim from
`scripts/persistent_object_blended_readout_transfer_sweep.py`):

```python
BLEND = 0.25

@dataclass(frozen=True)
class ModeResult:
    label: str
    mean_overlap: float
    min_overlap: float
    mean_detector_eff: float
    mean_capture: float
    mean_delta: float
    step_alpha: tuple[float | None, ...]
    max_kappa_drift: float
    admissible: bool

def _run_mode(case: Case, top_keep: int) -> ModeResult:
    lat = m.Lattice3D.build(case.phys_l, case.phys_w, H)
    source_nodes = _source_cluster_nodes(lat, case.source_z)
    ref_raw = _green_field_layers(
        lat,
        max(SOURCE_STRENGTHS),
        source_nodes,
        [1.0 / len(source_nodes)] * len(source_nodes),
    )
    gain = FIELD_TARGET_MAX / _field_abs_max(ref_raw) if _field_abs_max(ref_raw) > 1e-30 else 1.0
    free_centroid = _free_centroid_for_blend(lat)

    overlap_rows: list[list[float]] = [[] for _ in range(N_UPDATES)]
    deltas_by_step: list[list[float]] = [[] for _ in range(N_UPDATES)]
    detector_effs: list[list[float]] = [[] for _ in range(N_UPDATES)]
    captures: list[list[float]] = [[] for _ in range(N_UPDATES)]

    for strength in SOURCE_STRENGTHS:
        weights = [1.0 / len(source_nodes)] * len(source_nodes)
        prev_weights = weights[:]
        for step in range(N_UPDATES):
            raw = _green_field_layers(lat, strength, source_nodes, weights)
            field = [[gain * v for v in row] for row in raw]
            amps = lat.propagate(field, m.K)
            det_start = lat.layer_start[lat.nl - 1]
            det_probs = [abs(a) ** 2 for a in amps[det_start : det_start + lat.npl]]
            source_probs = [abs(amps[i]) ** 2 for i in source_nodes]

            norm_prev = _normalize_weights(prev_weights)
            norm_next = _normalize_weights(source_probs)
            overlap_num = sum(a * b for a, b in zip(norm_prev, norm_next))
            overlap_den = math.sqrt(sum(a * a for a in norm_prev) * sum(b * b for b in norm_next))
            overlap = overlap_num / overlap_den if overlap_den > 1e-30 else 0.0
            overlap_rows[step].append(overlap)

            probs, capture = _blended_probs(lat, det_probs, BLEND)
            total = sum(probs)
            norm_probs = [p / total for p in probs if p > 0.0] if total > 1e-30 else []
            det_eff = math.exp(-sum(p * math.log(p) for p in norm_probs)) if norm_probs else 0.0
            delta = 0.0
            if total > 1e-30:
                delta = sum(p * lat.pos[det_start + i][2] for i, p in enumerate(probs)) / total - free_centroid

            deltas_by_step[step].append(delta)
            detector_effs[step].append(det_eff)
            captures[step].append(capture)

            prev_weights = weights[:]
            weights = _topk_weights(source_probs, top_keep)

    step_alpha: list[float | None] = []
    step_toward: list[int] = []
    step_kappa: list[float] = []
    for step in range(N_UPDATES):
        deltas = deltas_by_step[step]
        alpha = _fit_power(SOURCE_STRENGTHS, [abs(v) for v in deltas])
        kappas = [delta / strength for strength, delta in zip(SOURCE_STRENGTHS, deltas)]
        step_alpha.append(alpha)
        step_toward.append(sum(1 for delta in deltas if delta > 0))
        step_kappa.append(float(sum(kappas) / len(kappas)))

    drifts = [
        abs(step_kappa[i] - step_kappa[i - 1]) / max(abs(step_kappa[i - 1]), 1e-30)
        for i in range(1, len(step_kappa))
    ]
    mean_overlap = _mean([v for row in overlap_rows for v in row])
    admissible = (
        mean_overlap >= OVERLAP_THRESHOLD
        and all(t == len(SOURCE_STRENGTHS) for t in step_toward)
        and all(alpha is not None and ALPHA_BAND[0] <= alpha <= ALPHA_BAND[1] for alpha in step_alpha)
        and all(drift <= KAPPA_DRIFT_THRESHOLD for drift in drifts)
    )

    return ModeResult(
        label=f"top{top_keep}",
        mean_overlap=mean_overlap,
        min_overlap=min(v for row in overlap_rows for v in row),
        mean_detector_eff=_mean([v for row in detector_effs for v in row]),
        mean_capture=_mean([v for row in captures for v in row]),
        mean_delta=_mean([v for row in deltas_by_step for v in row]),
        step_alpha=tuple(step_alpha),
        max_kappa_drift=max(drifts) if drifts else 0.0,
        admissible=admissible,
    )
```

Constants `H = 0.25`, `N_UPDATES = 3`, `SOURCE_STRENGTHS = (0.001, 0.002,
0.004, 0.008)`, `OVERLAP_THRESHOLD`, `ALPHA_BAND`, `FIELD_TARGET_MAX`,
`KAPPA_DRIFT_THRESHOLD`, and the helpers `_source_cluster_nodes`,
`_green_field_layers`, `_field_abs_max`, `_topk_weights`,
`_normalize_weights`, `_fit_power`, `_mean` are imported from
`scripts.persistent_object_compact_shared` and
`scripts.persistent_object_compact_inertial_probe`; `_blended_probs` from
`scripts.persistent_object_blended_readout_boundary_probe`; the lattice
class `Lattice3D` from `scripts.minimal_source_driven_field_probe`. All
seven helper paths are now listed in the Audit Requeue Note below and are
populated by the audit pipeline's transitive `helper_runner_paths` field.

### Gap 2 — inward-source boundary cert is not in `logs/runner-cache/`

The cached primary runner stdout supports the outer `top3 4/5`, `top2 1/5`
counts. The inward-source boundary probe runner
(`scripts/persistent_object_blended_readout_inner_source_boundary_probe.py`)
has **no cached stdout in `logs/runner-cache/`** at the time of this
restricted-packet repair. The boundary-probe row pattern asserted below
(`source0.75/1.00/1.25` closed, `source1.50` open) therefore cannot be
load-bearing from the restricted packet alone.

The honest restricted-packet narrowing is:

> The widened branch's outer second-ring miss is at `source_z = 1.0`. The
> precise inward-source boundary location (between `1.25` and `1.50` on
> `L = 6, W = 3`) is asserted from a boundary-probe runner whose cached
> stdout is not in the restricted packet. Until that runner output is
> cached, the supportable claim is only that the outer miss occurs at
> `source_z = 1.0`, not the full three-row inward-closure pattern.

The "Frozen result" section below preserves the original (broader) claim
for historical record, but the bounded restricted-packet claim is the
narrowed one above.

## Question

The first blended-readout transfer sweep established one real local positive:

> the exact-lattice `top3` object plus fixed `blend = 0.25` passes on the full
> nearby `6 / 6` family.

That still left the next honest bar open:

> does the same branch survive one ring farther out, or does the current
> positive stop at the immediate neighborhood?

## Frozen setup

Fixed across the outer sweep:

- exact lattice with `h = 0.25`
- compact object class `top3`, with `top2` retained as a boundary check
- fixed blended detector readout `blend = 0.25`
- source strengths `0.001, 0.002, 0.004, 0.008`
- three repeated updates
- same overlap / `TOWARD` / `F~M` / drift gates as the local transfer sweep

Second-ring cases:

1. `source1.0`: `L = 6`, `W = 3`, `source_z = 1.0`
2. `source2.75`: `L = 6`, `W = 3`, `source_z = 2.75`
3. `width5`: `L = 6`, `W = 5`, `source_z = 2.0`
4. `length4`: `L = 4`, `W = 3`, `source_z = 2.0`
5. `length8`: `L = 8`, `W = 3`, `source_z = 2.0`

Follow-up boundary cases on the failing inward-source side:

- `source0.75`
- `source1.00`
- `source1.25`
- `source1.50`

## Frozen result

### Headline

The exact-lattice `top3` branch does widen beyond the immediate neighborhood,
but not uniformly.

Outer second-ring totals:

- `top3`: `4 / 5`
- `top2`: `1 / 5`

The only outer miss is the inward source shift `source_z = 1.0`.

The boundary probe then shows that this is not a one-row fluke:

- `source0.75`: closed
- `source1.00`: closed
- `source1.25`: closed
- `source1.50`: open

So the widened regime has a real inward-source boundary between `1.25` and
`1.50` on the baseline `L = 6`, `W = 3` family.

### Summary table

| case | `top2` | `top3` | verdict |
| --- | :---: | :---: | --- |
| `source1.0` | ❌ | ❌ | closed |
| `source2.75` | ❌ | ✅ | `top3` outer bridge |
| `width5` | ❌ | ✅ | `top3` outer bridge |
| `length4` | ❌ | ✅ | `top3` outer bridge |
| `length8` | ✅ | ✅ | `top2` outer bridge |

### Why the inward miss matters

This is not a generic collapse of the whole branch.

The widened branch survives:

- one farther outward source placement
- one broader width slice
- one shorter length slice
- one longer length slice

So the local exact-lattice object-plus-response regime is genuinely larger than
the first-shell note showed.

But the failure is also not a harmless isolated row.

The inward-source boundary probe says the branch stays closed across three
consecutive inward rows and only reopens at `source_z = 1.50`.

That means the surviving branch is now best read as:

> a widened but source-placement-bounded exact-lattice compact-object response
> regime

rather than:

> an already robust all-direction local transfer law

### Where the compact floor sits

The floor still sits near `top3`.

`top2` remains bounded:

- only `length8` opens
- all other second-ring cases stay closed

So there is still no evidence that the widened regime is narrowing below
`top3` in any general way.

## Safe read

This sweep upgrades the compact-object lane, but only in a bounded way:

- the exact-lattice `top3` branch survives most of the second ring
- the surviving regime is visibly larger than the immediate nearby family
- the first strong outer boundary is now mapped on the inward-source side

So the honest interpretation is:

> the repo now has a widened local exact-lattice compact-object-plus-response
> regime, but it remains source-placement bounded and is still below
> persistent inertial-mass closure.

## What this proves

- the `top3 + blend = 0.25` branch is not confined to the first-shell nearby
  family
- the current positive survives on `4 / 5` second-ring cases
- the first clear outer boundary is a real inward-source boundary, not a vague
  “sometimes it fails” story

## What it does not prove

- a direction-independent local transfer law
- a persistent inertial mass
- matter closure
- transfer beyond the now-mapped widened exact-lattice local regime

## Branch verdict

The persistent-object lane is stronger again:

1. `top3` is a transferable compact source object
2. that object carries a stable weak-field response
3. one retained blended readout transfers on the full nearby family
4. the same branch survives most of the second ring, but has a mapped inward
   boundary

So the correct branch verdict is:

> the compact repeated-update exact-lattice branch is now a widened local
> object-plus-response regime with a known inward-source boundary, not yet a
> closure-grade persistent inertial object law.

## Best next move

The next tight move is now one of:

1. a stronger multi-stage persistence / inertial-response probe on the stable
   `top3` rows that survive the widened regime
2. one farther transfer test beyond the current widened local pocket
3. if those fail quickly, freeze this branch as:
   - widened local exact-lattice compact object
   - bounded widened local object-plus-response transfer
   - no persistent inertial-mass closure

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/minimal_source_driven_field_probe.py`
- `scripts/persistent_object_adaptive_readout_probe.py`
- `scripts/persistent_object_blended_readout_boundary_probe.py`
- `scripts/persistent_object_blended_readout_transfer_sweep.py`
- `scripts/persistent_object_compact_inertial_probe.py`
- `scripts/persistent_object_compact_shared.py`
