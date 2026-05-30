# Decoherence is Action-Independent

**Date:** 2026-04-04
**Status:** Confirmed on the frozen 3D `1/L^2` replay — exact numerical identity across actions
**Claim type:** bounded_theorem

**Audit-conditional perimeter (2026-05-10):**
The current generated audit ledger records this row `audited_conditional` with
`auditor_confidence = high`, `chain_closes = false`, and `claim_type =
bounded_theorem`. The audit chain-closure explanation is exact: "The
packet does not provide retained definitions of the two action laws
or the imported propagation harness needed to verify the zero-field
reduction. The runner also has no completed stdout, but the timeout
is not used as the terminal reason." This rigorization edit only
sharpens the boundary of the conditional perimeter; nothing here
promotes audit status. The supported content of this note is the
exact-identity table at h ∈ {1.0, 0.5, 0.25} reproduced verbatim from
the frozen 2026-04-04 log; the broader interpretation in §"Why" and
§"Implications" depends on the imported valley-linear and spent-delay
action definitions plus the propagation harness, which are not in the
restricted packet. The frozen log
[`logs/2026-04-04-decoherence-action-independence.txt`](../logs/2026-04-04-decoherence-action-independence.txt)
is the load-bearing artifact for the table; the runner
[`scripts/decoherence_action_independence.py`](../scripts/decoherence_action_independence.py)
is the registered re-derivation harness.

## Finding

On the frozen 3D `1/L^2` lattice replay, the decoherence observables
(d_TV, MI, CL bath purity, S_norm) are EXACTLY IDENTICAL for the
valley-linear and spent-delay actions at every tested lattice spacing.

Primary artifact:

- [`scripts/decoherence_action_independence.py`](/Users/jonreilly/Projects/Physics/scripts/decoherence_action_independence.py)
- [`logs/2026-04-04-decoherence-action-independence.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-04-decoherence-action-independence.txt)

| h | d_TV (both) | MI (both) | Decoh (both) | S_norm (both) |
|---|-------------|-----------|--------------|---------------|
| 1.0 | 0.627 | 0.414 | 30.2% | 0.390 |
| 0.5 | 0.786 | 0.588 | 49.4% | 0.701 |
| 0.25 | 0.830 | 0.647 | 49.9% | 0.807 |

## Why

The decoherence test uses zero field (no mass). Both actions reduce
to S = L × const at zero field. The amplitude magnitude at each node
depends only on the kernel (1/L^2) and the angular weight (exp(-βθ²)),
which are shared by both actions. The action only changes the PHASE
(via exp(ikS)), and the CL bath measurement depends on amplitude
MAGNITUDES at intermediate layers.

## Implications

The model cleanly separates:
- **Gravity**: action-dependent (valley-linear → Newtonian, spent-delay → sqrt)
- **Decoherence**: geometry-dependent (lattice structure + slits)
- **Born rule**: linearity-dependent (both actions are linear)

This means the action can be optimized for gravity without affecting
decoherence on the tested family. The valley-linear action gives Newtonian
gravity AND the same decoherence as spent-delay here, so there is no
gravity/decoherence trade-off on the frozen replay.

## Convergence

The decoherence converges as h → 0 on the tested family:
- d_TV: 0.63 → 0.79 → 0.83 (approaching 1.0)
- MI: 0.41 → 0.59 → 0.65 (approaching ~0.7?)
- Decoherence: 30% → 49% → 50% (converged to 50%)
- S_norm: 0.39 → 0.70 → 0.81 (approaching 1.0)

This convergence is a property of the LATTICE, not the action, on the
frozen 3D `1/L^2` branch.

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

The primary runner `scripts/decoherence_action_independence.py` imports the
`Lattice3D` class (with its `propagate` method) and `setup_slits` plus the
shared constants (`K`, `LAM`, `N_YBINS`, `PHYS_L`, `PHYS_W`) from
`scripts/valley_linear_same_harness_compare.py`. The two action-mode
definitions (`spent_delay` and `valley_linear`) live inside
`Lattice3D.propagate`. Without that file in the restricted packet the audit
cannot verify (a) that the two action modes are genuinely implemented and
(b) that they reduce to the same phase at zero field. The excerpt below
inlines those load-bearing pieces verbatim from
`scripts/valley_linear_same_harness_compare.py` (commit at audit time;
the unabridged file remains the canonical source).

Provenance: copied verbatim from
[`scripts/valley_linear_same_harness_compare.py`](/Users/jonreilly/Projects/Physics/scripts/valley_linear_same_harness_compare.py)
on 2026-05-18 as part of the audited-conditional repair campaign for this
note's `missing_dependency_edge` restricted-packet repair. Lines 47-184 of
the canonical file.

```python
BETA = 0.8
K = 5.0
LAM = 10.0
N_YBINS = 8
PHYS_W = 10
PHYS_L = 12
H = 0.25
MAX_D_PHYS = 3
STRENGTH = 5e-5


class Lattice3D:
    def __init__(self, phys_l: int, phys_w: int, h: float):
        self.h = h
        self.nl = int(phys_l / h) + 1
        self.hw = int(phys_w / h)
        self.max_d = max(1, round(MAX_D_PHYS / h))
        nw = 2 * self.hw + 1
        self.npl = nw**2
        self.n = self.nl * self.npl
        self._hm = h * h
        self._nw = nw

        self.pos = np.zeros((self.n, 3))
        self.nmap = {}
        self._ls = np.zeros(self.nl, dtype=np.int64)
        idx = 0
        for layer in range(self.nl):
            self._ls[layer] = idx
            x = layer * h
            for iy in range(-self.hw, self.hw + 1):
                for iz in range(-self.hw, self.hw + 1):
                    self.pos[idx] = (x, iy * h, iz * h)
                    self.nmap[(layer, iy, iz)] = idx
                    idx += 1

        self._off = []
        for dy in range(-self.max_d, self.max_d + 1):
            for dz in range(-self.max_d, self.max_d + 1):
                dyp = dy * h
                dzp = dz * h
                L = math.sqrt(h * h + dyp * dyp + dzp * dzp)
                theta = math.atan2(math.sqrt(dyp**2 + dzp**2), h)
                w = math.exp(-BETA * theta * theta)
                self._off.append((dy, dz, L, w))

    def propagate(self, field: np.ndarray, k: float, blocked_set: set[int], action_mode: str) -> np.ndarray:
        amps = np.zeros(self.n, dtype=np.complex128)
        src = self.nmap.get((0, 0, 0), 0)
        amps[src] = 1.0

        blocked = np.zeros(self.n, dtype=bool)
        for b in blocked_set:
            blocked[b] = True

        for layer in range(self.nl - 1):
            ls = self._ls[layer]
            ld = self._ls[layer + 1]
            sa = amps[ls:ls + self.npl].copy()
            sa[blocked[ls:ls + self.npl]] = 0
            if np.max(np.abs(sa)) < 1e-30:
                continue

            sf = field[ls:ls + self.npl]
            df = field[ld:ld + self.npl]
            db = blocked[ld:ld + self.npl]

            for dy, dz, L, w in self._off:
                ym = max(0, -dy)
                yM = min(self._nw, self._nw - dy)
                zm = max(0, -dz)
                zM = min(self._nw, self._nw - dz)
                if ym >= yM or zm >= zM:
                    continue

                yr = np.arange(ym, yM)
                zr = np.arange(zm, zM)
                siy, siz = np.meshgrid(yr, zr, indexing="ij")
                si = siy.ravel() * self._nw + siz.ravel()
                di = (siy.ravel() + dy) * self._nw + (siz.ravel() + dz)
                a = sa[si]
                nz = np.abs(a) > 1e-30
                if not np.any(nz):
                    continue

                lf = 0.5 * (sf[si[nz]] + df[di[nz]])
                if action_mode == "spent_delay":
                    dl = L * (1 + lf)
                    ret = np.sqrt(np.maximum(dl * dl - L * L, 0))
                    act = dl - ret
                elif action_mode == "valley_linear":
                    act = L * (1 - lf)
                else:  # pragma: no cover - internal guard
                    raise ValueError(f"unknown action_mode={action_mode}")

                c = a[nz] * np.exp(1j * k * act) * w * self._hm / (L * L)
                c[db[di[nz]]] = 0
                np.add.at(amps[ld:ld + self.npl], di[nz], c)

        return amps


def setup_slits(lat: Lattice3D) -> tuple[list[int], list[int], set[int], int]:
    bl = lat.nl // 3
    bi = []
    for iy in range(-lat.hw, lat.hw + 1):
        for iz in range(-lat.hw, lat.hw + 1):
            idx = lat.nmap.get((bl, iy, iz))
            if idx is not None:
                bi.append(idx)
    sa = [i for i in bi if lat.pos[i, 1] >= 0.5]
    sb = [i for i in bi if lat.pos[i, 1] <= -0.5]
    blocked = set(bi) - set(sa + sb)
    return sa, sb, blocked, bl
```

### Zero-field reduction check (load-bearing for the audit verdict)

At zero field, `field = np.zeros(lat.n)`, so the per-edge field average
`lf = 0.5 * (sf[...] + df[...])` is identically `0`. Substituting `lf = 0`
into the two action branches inside `propagate`:

- `spent_delay`: `dl = L * (1 + 0) = L`, then
  `ret = sqrt(max(L*L - L*L, 0)) = 0`, so `act = dl - ret = L`.
- `valley_linear`: `act = L * (1 - 0) = L`.

Both branches deliver `act = L`, so the per-edge contribution
`c = a[nz] * exp(1j*k*act) * w * self._hm / (L*L)` is bit-identical between
the two modes at zero field — the magnitude factor `w * self._hm / (L*L)`
is shared and the phase `exp(1j*k*L)` is the same. The propagator,
its outputs `pa`, `pb`, and every downstream observable computed in
`measure_decoherence` (`d_tv`, `mi`, `pur_cl`, `decoh`, `s_norm`) are
therefore identical. This matches the §"Why" narrative and the exact-zero
delta table in the frozen log.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [valley_linear_action_note](VALLEY_LINEAR_ACTION_NOTE.md)

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/valley_linear_same_harness_compare.py`
