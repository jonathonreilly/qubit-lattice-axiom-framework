# Dirac Observable Panel Note

**Status:** bounded - bounded or caveated result note
**Claim type:** bounded_theorem
**Date:** 2026-04-10  
**Scope:** one Dirac 3+1D harness, many gravity readouts.

**Audit-conditional perimeter (2026-05-03; panel cert inlined 2026-05-18):**
The current generated audit ledger records this row `audited_conditional` with
`auditor_confidence = high`, `chain_closes = false`, and `claim_type =
bounded_theorem`. The audit chain-closure explanation is exact: "The
dependency now closes for retained bounded core results, including
multi-observable gravity under primary readouts, but the supplied
runner output does not report the observable-panel-specific readouts
listed in this note. The missing step is a panel run or retained
summary tying centroid, peak, first-arrival, early accumulation,
current, and shell imbalance to the stated default sweep and sign-
alignment questions." This rigorization edit only sharpens the
boundary of the conditional perimeter; nothing here promotes audit
status. The supported content of this note is the bounded
methodological framing: the panel of readouts, the interpretation
rules, and the default sweep are all auditable framings, not
numerical claims.

The panel-specific runner
`scripts/frontier_dirac_walk_3plus1d_observable_panel.py`
(sha256 `a83db7…0ce834e`) has now been executed on the default sweep
`n=21, offset=3, layers=10,12,14,16,18,20, mass=0.3, strength=5e-4`
and its full stdout deposited at
`logs/runner-cache/frontier_dirac_walk_3plus1d_observable_panel.txt`
(exit_code=0, elapsed≈1.41s). The cache reports all six listed
readouts (centroid shift, peak shift, first-arrival, early shell
accumulation, directional current, and shell imbalance) on the stated
sweep. This inlines the panel cert; what the panel data itself
**does not** support is a sign-locked statement about gravity: across
the six layer counts the panel returns three `ALL` rows
(`A0AA, A0AA, A0AA` at N=10,12,14) and three `MIX` rows
(`T0AA, T0TA, TATA` at N=16,18,20), with the centroid flipping sign
between N=14 and N=16 while peak remains zero or `-3` only at N=20.
The honest reading is that the panel exhibits a recurrence- and
readout-driven sign split on the default sweep, exactly the
diagnostic the methodological framing was designed to detect. The
note therefore remains `bounded_theorem` as a methodological card
plus a registered panel run; the framing is auditable and the runner
is reproducible, but no sign-locked gravity claim is made from the
panel output.

The current Dirac work has reached the point where the main question is not
just whether a sign is `TOWARD` or `AWAY`, but whether the sign survives under
different physically plausible readouts.

This panel is the early bottleneck test for that question.

## What The Panel Measures

On the same `frontier_dirac_walk_3plus1d_v3.py` harness, the panel compares:

- centroid shift
- peak shift
- first-arrival layer for mass-side accumulation
- early mass-side accumulation
- directionally projected current
- mass-side shell imbalance

The point is to separate:

- geometric transport
- packet-shape effects
- recurrence / boundary effects
- readout-specific artifacts

from each other before they become a paper-level claim.

## Why It Matters

The branch already shows that a single gravity readout can be misleading.
Different observables can disagree even when they come from the same lattice,
same coupling, and same propagation law.

The panel is designed to answer three questions:

1. Do all readouts agree on sign in the same basin?
2. Do disagreements appear only near recurrence windows?
3. Is the remaining non-monotonicity geometric, or just a readout artifact?

## Interpretation Rules

- If centroid, peak, current, and shell imbalance agree, the sign is probably
  geometric.
- If peak disagrees but the others agree, the readout is too wave-sensitive.
- If the sign flips only at large `N`, boundary recurrence is still active.
- If first-arrival and early accumulation disagree with the final observables,
  the panel is telling us the transport is not settling before the detector
  window.

## Core-Card Connection

This panel is the concrete implementation target for the historical multi-readout
panel row later absorbed into the audited Dirac-core discussion in
[DIRAC_CORE_CARD_NOTE.md](./DIRAC_CORE_CARD_NOTE.md):

- first-arrival
- peak
- current
- centroid
- torus-aware centroid

If the architecture cannot keep these readouts aligned on a clean operating
point, the gravity story is not yet stable enough for promotion.

## Default Run

The default sweep is intentionally modest:

- `n=21`
- `offset=3`
- `layers=10,12,14,16,18,20`
- `mass=0.3`
- `strength=5e-4`

That is enough to expose the readout split without turning the panel into a
new sprawling campaign.

### Registered panel cert (2026-05-18)

Runner: `scripts/frontier_dirac_walk_3plus1d_observable_panel.py`
(sha256 `a83db713cce4556d432e324314a578e555c744898cc7b5dc56028d80e0ce834e`).
Helper runner (load-bearing): [`scripts/frontier_dirac_walk_3plus1d_v3.py`](../scripts/frontier_dirac_walk_3plus1d_v3.py).
Full stdout is cached at
`logs/runner-cache/frontier_dirac_walk_3plus1d_observable_panel.txt`
(exit_code=0, elapsed≈1.41s).

Default-sweep panel output (excerpted from the cache):

```
   N      centroid          peak  first+   early_shell       current         shell   sig  cons
--------------------------------------------------------------------------------------------
  10   -5.6732e-05   +0.0000e+00       6   -3.2937e-06   -1.3245e-06   -3.0502e-07  A0AA   ALL
  12   -3.5467e-05   +0.0000e+00       6   -1.3506e-06   -2.3064e-06   -4.0074e-07  A0AA   ALL
  14   -2.2252e-06   +0.0000e+00       6   +3.9628e-07   -2.6985e-06   -2.0704e-07  A0AA   ALL
  16   +1.2310e-05   +0.0000e+00       6   +1.2553e-06   -1.4828e-06   -9.4977e-08  T0AA   MIX
  18   +2.9339e-05   +0.0000e+00       6   +2.2711e-06   -2.2882e-06   +4.7059e-07  T0TA   MIX
  20   +2.9436e-05   -3.0000e+00       6   +1.9661e-06   -4.7811e-06   +1.7158e-06  TATA   MIX
```

Agreement summary (from the same cache):

- centroid vs peak: `0/6`
- centroid vs shell: `5/6`
- centroid vs current: `3/6`
- peak vs shell: `0/6`
- all-four agree: `3/6`
- mixed-sign cases: `3/6`

The six listed readouts (centroid shift, peak shift, first-arrival,
early shell accumulation, directional current, shell imbalance) are
each produced for every layer count on the default sweep. The panel
is registered as a methodological cert: the runner reproduces, the
columns are populated, and the answer to "do all readouts agree on
sign?" is recorded as a recurrence-driven `ALL/MIX` split, not as a
sign-locked claim. Interpretation rules above are framing only; no
gravity sign is asserted by this note.

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-24)

The panel runner `scripts/frontier_dirac_walk_3plus1d_observable_panel.py`
imports its load-bearing Dirac evolution and lattice primitives from the
helper runner [`scripts/frontier_dirac_walk_3plus1d_v3.py`](../scripts/frontier_dirac_walk_3plus1d_v3.py)
via:

```python
from frontier_dirac_walk_3plus1d_v3 import (
    gamma0,
    gamma3,
    min_image_dist,
    prob,
    step_zyx,
)
```

The same import line is visible in the panel runner source (top of
`scripts/frontier_dirac_walk_3plus1d_observable_panel.py`). The helper
primitives `gamma0`, `gamma3`, `step_zyx`, `prob`, and `min_image_dist`
are inlined verbatim below so the restricted-packet review can verify
that the panel computation is built on genuine framework primitives
(gamma matrices, split-step coin+shift Dirac evolution, probability
density, torus min-image distance) rather than hard-coded panel premises.
The load-bearing implementation lives in the helper file path above; the
inlined code is exactly the source the panel runner imports and uses.

Provenance: copied verbatim from
`scripts/frontier_dirac_walk_3plus1d_v3.py` at branch
`audit-repair/dirac-observable-panel-v3-runner-register-2026-05-24`,
2026-05-24.

### Gamma matrices and projectors

```python
import numpy as np

# ============================================================================
# Gamma matrices
# ============================================================================
gamma0 = np.diag([1, 1, -1, -1]).astype(complex)
gamma1 = np.array([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]], dtype=complex)
gamma2 = np.array([[0,0,0,-1j],[0,0,1j,0],[0,1j,0,0],[-1j,0,0,0]], dtype=complex)
gamma3 = np.array([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]], dtype=complex)
gammas_spatial = [gamma1, gamma2, gamma3]

def get_projectors(gp):
    evals, evecs = np.linalg.eigh(gp)
    Pp = sum(np.outer(evecs[:,i], evecs[:,i].conj()) for i in range(4) if evals[i] > 0)
    Pm = sum(np.outer(evecs[:,i], evecs[:,i].conj()) for i in range(4) if evals[i] < 0)
    return Pp, Pm

Px_p, Px_m = get_projectors(gamma0 @ gamma1)
Py_p, Py_m = get_projectors(gamma0 @ gamma2)
Pz_p, Pz_m = get_projectors(gamma0 @ gamma3)
```

The gamma matrices satisfy the standard Dirac anticommutation relations
`{gamma^mu, gamma^nu} = 2 eta^{mu nu}` in the chiral / Dirac basis used
throughout the v3 harness. The projectors `Px_p, Px_m, Py_p, Py_m, Pz_p,
Pz_m` are the spectral projectors of `gamma0 @ gamma_j` onto the +1 and
-1 eigenspaces; they govern the directional shift in `step_zyx`.

### Coin + shift split-step Dirac walk

```python
def coin_step(psi, mass_field, n):
    cm = np.cos(mass_field); sm = np.sin(mass_field)
    out = np.zeros_like(psi)
    out[0] = (cm + 1j*sm) * psi[0]
    out[1] = (cm + 1j*sm) * psi[1]
    out[2] = (cm - 1j*sm) * psi[2]
    out[3] = (cm - 1j*sm) * psi[3]
    return out

def shift_dir(psi, n, Pp, Pm, axis):
    out = np.zeros_like(psi)
    for c in range(4):
        pp = sum(Pp[c,d] * psi[d] for d in range(4))
        pm = sum(Pm[c,d] * psi[d] for d in range(4))
        out[c] += np.roll(pp, -1, axis=axis)
        out[c] += np.roll(pm, +1, axis=axis)
    return out

def step_zyx(psi, mf, n):
    psi = coin_step(psi, mf, n)
    psi = shift_dir(psi, n, Px_p, Px_m, 0)
    psi = shift_dir(psi, n, Py_p, Py_m, 1)
    psi = shift_dir(psi, n, Pz_p, Pz_m, 2)
    return psi
```

`step_zyx` is one full split-step Dirac evolution step at lattice site
mass `mf[i,j,k]`. The coin step applies `exp(i * mf * gamma0)` per-site
(the diagonal entries flip sign on the lower two components, matching
the `gamma0 = diag(1,1,-1,-1)` convention). Each shift then applies the
spectral projector decomposition of `gamma0 * gamma_j`: the `+`
eigenspace moves one step in `-axis`, the `-` eigenspace moves one step
in `+axis`. The composition of one coin and three directional shifts is
the load-bearing time step the panel reuses six times per layer count.

### Probability density and torus min-image distance

```python
def prob(psi):
    return np.sum(np.abs(psi)**2, axis=0)

def min_image_dist(n, mp):
    c = np.arange(n)
    dx = np.abs(c[:,None,None] - mp[0]); dx = np.minimum(dx, n-dx)
    dy = np.abs(c[None,:,None] - mp[1]); dy = np.minimum(dy, n-dy)
    dz = np.abs(c[None,None,:] - mp[2]); dz = np.minimum(dz, n-dz)
    return np.sqrt(dx**2 + dy**2 + dz**2)
```

`prob` is the spinor probability density: sum over the 4 Dirac
components of `|psi|^2` per lattice site. `min_image_dist` is the
torus-aware Euclidean distance from a site `mp` on an `n^3` periodic
lattice, used by the panel to build the gravity mass-field `m(1 + tf)`
with `tf = strength / (min_image_dist + 0.1)`. Neither function carries
panel-specific structure; both are generic framework primitives.

### Panel-runner import wiring

The panel runner uses exactly the inlined primitives plus one
gamma-matrix product:

```python
from frontier_dirac_walk_3plus1d_v3 import (
    gamma0,
    gamma3,
    min_image_dist,
    prob,
    step_zyx,
)

ALPHA_Z = gamma0 @ gamma3
```

`ALPHA_Z` is the z-direction alpha matrix used inside
`current_density_z(psi)` to compute the directionally projected current
`psi^dagger alpha_z psi` (real part). The panel-specific readouts
(centroid, peak, first-arrival, early shell accumulation, current,
shell imbalance) are then computed by the panel runner itself from
`prob(psi)` and `current_density_z(psi)` at each layer step; the
load-bearing Dirac evolution and lattice geometry come from the inlined
v3 primitives above.

This inlines the helper source the auditor flagged as absent in the
restricted packet. No numerical claim or audit status is changed by this
inline; the panel-cert content above is unchanged. The note remains
`bounded_theorem` and `audited_conditional` until the audit lane
re-evaluates.
