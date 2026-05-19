# Wave Static Fixed-Beam Boundary Sensitivity — H = 0.5 Default Run (Binding)

**Date:** 2026-04-08 (scope narrowed 2026-05-17 per audited_conditional `runner_artifact_issue` repair: binding scope is the H = 0.5 default run only; the H = 0.35 medium-H rows are out of scope until the H = 0.35 completed stdout / cache is supplied)
**Status:** bounded H = 0.5 fixed-beam boundary-sensitivity probe;
the H = 0.35 medium-H persistence rows and the
`wave_retardation_continuum_limit` dependency reuse are
**out-of-binding-scope** in this revision until separately registered.

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `runner_artifact_issue`, stating: *"supply the full
`wave_retardation_continuum_limit` dependency or retained direct
authority plus completed stdout/cache for all claimed rows, especially
the H = 0.35 medium-H run."*

This revision takes the narrowing path. The binding evidence of this
note is exactly the **H = 0.5 default-run rows** from
`scripts/wave_static_fixed_beam_boundary_sensitivity.py` (the field
`PW_phys = 6.0` vs `9.0` comparison at fixed beam `PW_phys = 6.0`,
frozen source `z_phys = 3.0`, at `H = 0.5`).

The following are **demoted to out-of-binding-scope** of this note:
- the **`H = 0.35` medium-H persistence rows** — no completed stdout
  / cache is currently registered at `H = 0.35` in the restricted
  packet, so the claim that the boundary sensitivity persists at
  medium H is not supported by an audit-lane-visible cached artifact;
- reuse of the **`wave_retardation_continuum_limit`** dependency,
  whose module-level wave / beam / propagation / readout / constants
  imports are delegated upstream and are not registered as a direct
  retained authority for this row. Promoting either requires the
  separately registered artifact or retained-authority chain the
  audit verdict names.

This probe isolates the boundary question more carefully than the
previous field-box test:

> Keep the beam DAG fixed at the baseline beam box, enlarge only the
> field/static solve box, then crop the enlarged field back to the
> baseline beam box before propagation.

That removes the most obvious confound in the earlier boundary test:
changing `PW` changed both the field solve and the beam geometry.

## Results

The binding retained probe used a fixed beam `PW_phys = 6.0`, frozen
source `z_phys = 3.0`, and compared `field PW_phys = 6.0` vs `9.0`.

### Shared `H = 0.5`

| quantity | `field PW = 6.0` | `field PW = 9.0` | move |
| --- | ---: | ---: | ---: |
| `dM` | `+0.009857` | `+0.010629` | `7.26%` |
| `dS` | `+0.009507` | `+0.013637` | `30.29%` |
| `rel_MS` | `3.56%` | `22.06%` | `83.88%` |
| static residual | `1.998e-10` | `1.996e-10` | stable |

The historical `H = 0.35` rows are kept below as out-of-binding
background only. They are not part of this note's retained claim until
the separately registered completed stdout / cache is supplied.

### Shared `H = 0.35` (out-of-binding background)

| quantity | `field PW = 5.95` | `field PW = 9.10` | move |
| --- | ---: | ---: | ---: |
| `dM` | `+0.008380` | `+0.008428` | `0.57%` |
| `dS` | `+0.010863` | `+0.014721` | `26.21%` |
| `rel_MS` | `22.86%` | `42.75%` | `46.52%` |
| static residual | `1.997e-10` | `1.998e-10` | stable |

## Honest read

The binding `H = 0.5` fixed-beam probe still shows material boundary
sensitivity.

- at shared `H = 0.5`, enlarging only the field/static solve box from
  `6.0` to `9.0` moves `dS` by `30.29%` and `rel_MS` by `83.88%`
- at shared `H = 0.35`, the historical out-of-binding row moves `dS`
  by `26.21%` and `rel_MS` by `46.52%`, but that row awaits the
  separately registered completed artifact named by the audit verdict
- `dM` is much less sensitive than the comparator:
  `7.26%` move at `H = 0.5`, and only `0.57%` at `H = 0.35`

So the earlier boundary negative was not just a beam-geometry confound.
Fixing the beam DAG helps isolate the problem, but it does not remove it.
The exact discrete static comparator is still box-dependent at this shared
resolution in the binding `H = 0.5` row; the medium-`H` background row
points the same way but remains out of binding scope until its artifact
is supplied.

## Artifact chain

- [`scripts/wave_static_fixed_beam_boundary_sensitivity.py`](../scripts/wave_static_fixed_beam_boundary_sensitivity.py)

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named
by a prior conditional audit so the audit citation graph can track
them. It does not promote this note or change the audited claim scope.

The H = 0.5 default runner imports the following symbols from
`scripts/wave_retardation_continuum_limit.py` (constants
`K_PER_H`, `PW_PHYS`, `S_PHYS`, `SRC_LAYER_FRAC`, `T_PHYS_LAYERS`,
and helper functions `cz`, `grow`, `prop_beam`, `solve_wave`). Those
imports are documented as a one-hop dependency via the source note
for the upstream module:

- [WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md](WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md) — source note for `scripts/wave_retardation_continuum_limit.py`, documenting the wave solver `solve_wave`, the lattice growth helper `grow`, the beam propagator `prop_beam`, the comparator helper `cz`, and the physical-parameter constants `K_PER_H`, `PW_PHYS`, `S_PHYS`, `SRC_LAYER_FRAC`, `T_PHYS_LAYERS`.

This link registers the wave-retardation source note as the one-hop
authority for the H = 0.5 default-run imports above. The note's
binding-scope claim still rests only on the H = 0.5 default-run rows
listed in §Results above; the H = 0.35 medium-H rows remain
out-of-binding-scope until separately registered cached artifacts are
supplied.

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

Inlined here so the restricted audit packet is self-contained. Source of
truth: `scripts/wave_retardation_continuum_limit.py` at commit `b179c2d2c`.
The primary runner `scripts/wave_static_fixed_beam_boundary_sensitivity.py`
imports the constants `K_PER_H`, `PW_PHYS`, `S_PHYS`, `SRC_LAYER_FRAC`,
`T_PHYS_LAYERS` and the helper functions `solve_wave`, `grow`, `prop_beam`,
`cz` from that module. The helper `solve_wave` itself calls the small
private helper `laplacian_yz`, which is also inlined here. The module-level
constant `BETA` is consumed by `prop_beam` and is also inlined. No other
symbols from the upstream module are load-bearing for the H = 0.5
default-run rows of this note.

```python
# --- module-level constants ---
T_PHYS_LAYERS = 30 * 0.5    # 15.0 physical "time" units
PW_PHYS = 6.0               # 6.0 physical transverse half-width
SRC_LAYER_FRAC = 1.0 / 3.0  # source becomes active at NL/3
S_PHYS = 0.004              # field source strength (dimensionless)
K_PER_H = 5.0 * 0.5         # k_phase * H product (= 2.5 phase per edge step at the reference)
BETA = 0.8                  # propagator angular weight (dimensionless)


# --- DAG growth ---
def grow(seed, drift, restore, NL, PW, max_d_phys, H):
    """Build a grown DAG with explicit lattice spacing H."""
    rng = random.Random(seed)
    hw = int(PW / H)
    md = max(1, round(max_d_phys / H))
    pos = []
    adj = {}
    nmap = {}
    pos.append((0.0, 0.0, 0.0))
    nmap[(0, 0, 0)] = 0
    for layer in range(1, NL):
        x = layer * H
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                if layer == 1:
                    y, z = iy * H, iz * H
                else:
                    prev = nmap.get((layer - 1, iy, iz))
                    if prev is None:
                        continue
                    _, py, pz = pos[prev]
                    y = py + rng.gauss(0, drift * H)
                    z = pz + rng.gauss(0, drift * H)
                    y = y * (1 - restore) + (iy * H) * restore
                    z = z * (1 - restore) + (iz * H) * restore
                idx = len(pos)
                pos.append((x, y, z))
                nmap[(layer, iy, iz)] = idx
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                si = nmap.get((layer - 1, iy, iz))
                if si is None:
                    continue
                for dy in range(-md, md + 1):
                    for dz in range(-md, md + 1):
                        di = nmap.get((layer, iy + dy, iz + dz))
                        if di is not None:
                            adj.setdefault(si, []).append(di)
    return pos, adj, nmap


# --- transverse Laplacian (private helper of solve_wave) ---
def laplacian_yz(f, nw):
    lap = [[0.0] * nw for _ in range(nw)]
    for iy in range(1, nw - 1):
        for iz in range(1, nw - 1):
            lap[iy][iz] = (
                f[iy - 1][iz] + f[iy + 1][iz] + f[iy][iz - 1] + f[iy][iz + 1]
                - 4.0 * f[iy][iz]
            )
    return lap


# --- explicit retarded wave solve ---
def solve_wave(NL, PW, H, strength, iz_of_t, src_layer):
    hw = int(PW / H)
    nw = 2 * hw + 1
    f_prev = [[0.0] * nw for _ in range(nw)]
    f_curr = [[0.0] * nw for _ in range(nw)]
    history = [
        [[0.0] * nw for _ in range(nw)],
        [[0.0] * nw for _ in range(nw)],
    ]
    h2 = H * H
    for t in range(2, NL):
        if t >= src_layer:
            iz_now = iz_of_t(t)
            sy = nw // 2
            sz = nw // 2 + iz_now
        else:
            sy = sz = -1
        lap = laplacian_yz(f_curr, nw)
        f_next = [[0.0] * nw for _ in range(nw)]
        for iy in range(nw):
            for iz in range(nw):
                src = strength if (iy == sy and iz == sz) else 0.0
                f_next[iy][iz] = (
                    2.0 * f_curr[iy][iz] - f_prev[iy][iz]
                    + h2 * (lap[iy][iz] + src)
                )
        f_prev = f_curr
        f_curr = f_next
        history.append([row[:] for row in f_curr])
    return history


# --- field sampler (private helper of prop_beam) ---
def field_at(history, NL, PW, H, layer, iy, iz):
    hw = int(PW / H)
    nw = 2 * hw + 1
    sy = iy + nw // 2
    sz = iz + nw // 2
    if 0 <= layer < NL and 0 <= sy < nw and 0 <= sz < nw:
        return history[layer][sy][sz]
    return 0.0


# --- beam propagator on the grown DAG ---
def prop_beam(pos, adj, nmap, history, k_phase, NL, PW, H):
    n = len(pos)
    hw = int(PW / H)
    field = [0.0] * n
    if history is not None:
        for layer in range(NL):
            for iy in range(-hw, hw + 1):
                for iz in range(-hw, hw + 1):
                    idx = nmap.get((layer, iy, iz))
                    if idx is not None:
                        field[idx] = field_at(history, NL, PW, H, layer, iy, iz)
    order = sorted(range(n), key=lambda i: pos[i][0])
    amps = [0j] * n
    amps[0] = 1.0
    h2 = H * H
    for i in order:
        if abs(amps[i]) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            f = 0.5 * (field[i] + field[j])
            phase = k_phase * L * (1.0 - f)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            amps[j] += amps[i] * complex(math.cos(phase), math.sin(phase)) * w * h2 / (L * L)
    return amps


# --- weighted-z readout on the last beam plane ---
def cz(amps, pos, NL, PW, H):
    hw = int(PW / H)
    npl = (2 * hw + 1) ** 2
    n = len(pos)
    ds = n - npl
    weights = [abs(amps[i]) ** 2 for i in range(ds, n)]
    zs = [pos[i][2] for i in range(ds, n)]
    total = sum(weights)
    if total <= 0:
        return 0.0
    return sum(w * z for w, z in zip(weights, zs)) / total
```

Cache revalidation (2026-05-18): the H = 0.5 default-run cache at
`logs/runner-cache/wave_static_fixed_beam_boundary_sensitivity.txt`
reports `dM = +0.009857` / `dS = +0.009507` / `rel_MS = 3.56%` /
`residual = 1.998e-10` for `field PW = 6.0` and `dM = +0.010629` /
`dS = +0.013637` / `rel_MS = 22.06%` / `residual = 1.996e-10` for
`field PW = 9.0`, with field-box moves `dS = 30.29%`, `rel_MS = 83.88%`,
`dM = 7.26%`. These match the §Results "Shared `H = 0.5`" row in this
note exactly; no sync was applied.
