# Alternative Coupled-Field Probe

**Date:** 2026-04-05  
**Status:** bounded positive for an edge-carried minimal coupled-field architecture on the exact 3D lattice

## Artifact chain

- [`scripts/alternative_coupled_field_probe.py`](/Users/jonreilly/Projects/Physics/scripts/alternative_coupled_field_probe.py)
- [`logs/2026-04-05-alternative-coupled-field-probe.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-05-alternative-coupled-field-probe.txt)

## Question

Can an alternative minimal coupled-field architecture, distinct from the
telegraph-style source-driven field, preserve exact zero-source reduction while
still keeping the weak-field TOWARD sign and near-linear mass scaling?

This note is intentionally narrow:

- one family: exact 3D lattice
- one field rule: edge-carried forward transport
- one comparison: edge-carried field vs instantaneous `1/r` field
- one reduction check: zero-source field should recover free propagation

## Frozen result

The frozen probe uses:

- exact 3D lattice with `h = 0.5`, `W = 6`, `L = 30`
- source strengths `s = 0.001, 0.002, 0.004, 0.008`
- edge-transport calibration gain `1.427390e-46`
- transport decay `0.72`
- transport exponent `0.85`

Reduction check:

- zero-source dynamic shift: `+0.000000e+00`

Frozen readout:

| `s` | instantaneous deflection | edge-carried deflection | ratio | max `|f_edge|` |
| --- | ---: | ---: | ---: | ---: |
| `0.0010` | `+2.702607e-03` | `+3.021738e-05` | `0.011` | `1.0e-02` |
| `0.0020` | `+5.393344e-03` | `+5.996921e-05` | `0.011` | `2.0e-02` |
| `0.0040` | `+1.073461e-02` | `+1.182387e-04` | `0.011` | `4.0e-02` |
| `0.0080` | `+2.122358e-02` | `+2.311300e-04` | `0.011` | `8.0e-02` |

Fitted exponents:

- instantaneous `F~M`: `0.99`
- edge-carried `F~M`: `0.98`

## Safe read

The strongest bounded statement is:

- the alternative edge-carried architecture preserves exact zero-source
  recovery
- it keeps the weak-field TOWARD sign on the retained family
- it stays essentially linear in source strength

## Honest limitation

The edge-carried field is much weaker than the instantaneous comparator on this
exact lattice replay.

- the retained ratio is only about `1.1%` of the instantaneous deflection
- this does not yet give a stronger self-consistent field sector
- it is still useful because it shows a distinct architecture can preserve the
  weak-field lane without using the telegraph-style recurrence

## Branch verdict

Treat this as a real bounded positive:

- it is not the full moonshot field theory
- but it is a distinct coupled-field architecture that survives the strict
  reduction check and preserves the weak-field sign / mass-scaling readout

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

The primary runner `scripts/alternative_coupled_field_probe.py` imports the
lattice, propagation, constants, and centroid-readout helpers from
`scripts/minimal_source_driven_field_probe.py` via:

```python
from scripts.minimal_source_driven_field_probe import (
    H,
    K,
    Lattice3D,
    _centroid_z,
)
```

For the restricted audit packet to be self-contained, the imported symbols
are inlined verbatim below. Source of truth:
[`scripts/minimal_source_driven_field_probe.py`](/Users/jonreilly/Projects/Physics/scripts/minimal_source_driven_field_probe.py).

```python
# --- begin verbatim excerpt from scripts/minimal_source_driven_field_probe.py ---

from __future__ import annotations

import math
from dataclasses import dataclass


BETA = 0.8
K = 5.0
MAX_D_PHYS = 3.0
H = 0.5


@dataclass
class Lattice3D:
    h: float
    nl: int
    hw: int
    max_d: int
    npl: int
    n: int
    pos: list[tuple[float, float, float]]
    nmap: dict[tuple[int, int, int], int]
    layer_start: list[int]
    offsets: list[tuple[int, int, float, float]]
    nw: int

    @classmethod
    def build(cls, phys_l: int, phys_w: int, h: float) -> "Lattice3D":
        nl = int(phys_l / h) + 1
        hw = int(phys_w / h)
        max_d = max(1, round(MAX_D_PHYS / h))
        nw = 2 * hw + 1
        npl = nw * nw
        n = nl * npl
        pos: list[tuple[float, float, float]] = []
        nmap: dict[tuple[int, int, int], int] = {}
        layer_start = [0] * nl

        idx = 0
        for layer in range(nl):
            layer_start[layer] = idx
            x = layer * h
            for iy in range(-hw, hw + 1):
                for iz in range(-hw, hw + 1):
                    pos.append((x, iy * h, iz * h))
                    nmap[(layer, iy, iz)] = idx
                    idx += 1

        offsets: list[tuple[int, int, float, float]] = []
        for dy in range(-max_d, max_d + 1):
            for dz in range(-max_d, max_d + 1):
                dyp = dy * h
                dzp = dz * h
                L = math.sqrt(h * h + dyp * dyp + dzp * dzp)
                theta = math.atan2(math.sqrt(dyp * dyp + dzp * dzp), h)
                offsets.append((dy, dz, L, math.exp(-BETA * theta * theta)))

        return cls(h, nl, hw, max_d, npl, n, pos, nmap, layer_start, offsets, nw)

    def propagate(self, field_layers: list[list[float]], k: float) -> list[complex]:
        amps = [0j] * self.n
        src = self.nmap[(0, 0, 0)]
        amps[src] = 1.0

        for layer in range(self.nl - 1):
            ls = self.layer_start[layer]
            ld = self.layer_start[layer + 1]
            sa = amps[ls : ls + self.npl]
            if max(abs(a) for a in sa) < 1e-30:
                continue
            sf = field_layers[layer]
            df = field_layers[min(layer + 1, self.nl - 1)]
            for dy, dz, L, w in self.offsets:
                ym = max(0, -dy)
                yM = min(self.nw, self.nw - dy)
                zm = max(0, -dz)
                zM = min(self.nw, self.nw - dz)
                if ym >= yM or zm >= zM:
                    continue
                for yi in range(ym, yM):
                    for zi in range(zm, zM):
                        si = yi * self.nw + zi
                        ai = sa[si]
                        if abs(ai) < 1e-30:
                            continue
                        di = (yi + dy) * self.nw + (zi + dz)
                        lf = 0.5 * (sf[si] + df[di])
                        act = L * (1.0 - lf)
                        amps[ld + di] += ai * complex(math.cos(k * act), math.sin(k * act)) * w / (L * L)
        return amps


def _centroid_z(amps: list[complex], lat: Lattice3D) -> float:
    det_start = lat.layer_start[lat.nl - 1]
    det_nodes = range(det_start, det_start + lat.npl)
    total = 0.0
    weighted = 0.0
    for d in det_nodes:
        p = abs(amps[d]) ** 2
        total += p
        weighted += p * lat.pos[d][2]
    return weighted / total if total > 1e-30 else 0.0

# --- end verbatim excerpt ---
```

The constants `H = 0.5` and `K = 5.0`, the `Lattice3D` dataclass with its
`build` constructor and `propagate` method, and the `_centroid_z` detector
readout are the directly load-bearing imports for the primary runner. The
`BETA`, `MAX_D_PHYS` module constants are included because `Lattice3D.build`
references them. No other helper from the source file is referenced by
`alternative_coupled_field_probe.py`.

---

**Audit requeue note, 2026-05-17:** the previous
`audited_conditional` verdict cited an incomplete restricted packet with
missing helper-script imports. The audit ledger now records
`helper_runner_paths` for this row, so the next audit packet should
include `scripts/minimal_source_driven_field_probe.py` alongside the
primary runner and cache. This note changes no science content; it makes
the re-audit hash drift explicit.
