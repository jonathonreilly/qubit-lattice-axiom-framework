# Chiral Walk Layer Oscillation — Gravity Sign Depends on N

**Date:** 2026-04-09
**Status:** Diagnosed, not resolved
**Type:** bounded_theorem
**Primary runner:** scripts/frontier_chiral_layer_oscillation.py

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

The primary runner `scripts/frontier_chiral_layer_oscillation.py` imports
`evolve`, `probability_density`, and the module constant `THETA0` from the
canonical 3+1D chiral-walk implementation in
`scripts/frontier_chiral_3plus1d_converged.py`. To make the restricted
audit packet self-contained, the load-bearing functions are inlined here
verbatim from that file (provenance: `scripts/frontier_chiral_3plus1d_converged.py`,
top of file through `probability_density`).

```python
#!/usr/bin/env python3
"""
Frontier closure card: 3+1D chiral walk — CONVERGED regime (n=21, N=16).
10/10 property test + convergence verification.

Architecture: 6-component state on n^3 grid.
  Components: psi_{+y}, psi_{-y}, psi_{+z}, psi_{-z}, psi_{+w}, psi_{-w}
  Coin: symmetric Lorentzian [[cos th, i sin th],[i sin th, cos th]] per pair
  Shift: np.roll along each spatial axis
  theta(r) = theta0 * (1 - strength/(r+0.1))
  Periodic BCs, balanced source at center.
"""

import numpy as np
import time

# ── Parameters ──────────────────────────────────────────────────────
N_DEFAULT = 21       # grid size (converged regime n>=17)
L_DEFAULT = 16       # layers (converged regime N>=14)
THETA0 = 0.3
STRENGTH = 5e-4

def make_state(n):
    """Balanced source: equal amplitude on all 6 components at center."""
    psi = np.zeros((6, n, n, n), dtype=np.complex128)
    c = n // 2
    amp = 1.0 / np.sqrt(6.0)
    for k in range(6):
        psi[k, c, c, c] = amp
    return psi

def min_image_dist(n, mass_pos):
    """Minimum-image distance from each site to mass_pos on periodic grid."""
    c = np.arange(n)
    dy = np.abs(c[:, None, None] - mass_pos[0])
    dy = np.minimum(dy, n - dy)
    dz = np.abs(c[None, :, None] - mass_pos[1])
    dz = np.minimum(dz, n - dz)
    dw = np.abs(c[None, None, :] - mass_pos[2])
    dw = np.minimum(dw, n - dw)
    return np.sqrt(dy**2 + dz**2 + dw**2)

def apply_coin_and_shift(psi, n, theta_grid):
    """Apply Lorentzian coin to each pair then shift."""
    cos_t = np.cos(theta_grid)
    sin_t = np.sin(theta_grid)
    new_psi = np.zeros_like(psi)
    # Coin on each pair: (0,1)=+y/-y, (2,3)=+z/-z, (4,5)=+w/-w
    for pair_idx, (a, b) in enumerate([(0,1), (2,3), (4,5)]):
        pa = psi[a]
        pb = psi[b]
        new_psi[a] = cos_t * pa + 1j * sin_t * pb
        new_psi[b] = 1j * sin_t * pa + cos_t * pb
    # Shift: +y -> roll axis0 by -1, -y -> roll axis0 by +1, etc.
    shifts = [(-1, 0), (+1, 0), (0, -1), (0, +1), (0, -1), (0, +1)]
    axes  = [0, 0, 1, 1, 2, 2]
    out = np.zeros_like(new_psi)
    for k in range(6):
        out[k] = np.roll(new_psi[k], shifts[k][0] if axes[k] == 0 else shifts[k][1], axis=axes[k])
    # Correct: each component shifts along its own axis
    result = np.zeros_like(new_psi)
    # +y (comp 0): shift along axis 0 by -1
    result[0] = np.roll(new_psi[0], -1, axis=0)
    # -y (comp 1): shift along axis 0 by +1
    result[1] = np.roll(new_psi[1], +1, axis=0)
    # +z (comp 2): shift along axis 1 by -1
    result[2] = np.roll(new_psi[2], -1, axis=1)
    # -z (comp 3): shift along axis 1 by +1
    result[3] = np.roll(new_psi[3], +1, axis=1)
    # +w (comp 4): shift along axis 2 by -1
    result[4] = np.roll(new_psi[4], -1, axis=2)
    # -w (comp 5): shift along axis 2 by +1
    result[5] = np.roll(new_psi[5], +1, axis=2)
    return result

def evolve(n, n_layers, strength, mass_positions=None):
    """Evolve state for n_layers steps with given mass configuration."""
    psi = make_state(n)
    c = n // 2
    if mass_positions is None:
        mass_positions = [(c, c, c)]
    # Precompute theta grid (sum over all masses)
    theta_grid = np.full((n, n, n), THETA0)
    for mp in mass_positions:
        r = min_image_dist(n, mp)
        f = strength / (r + 0.1)
        theta_grid = theta_grid * (1.0 - f)  # multiplicative: each mass modifies
    # Re-derive: theta(r) = theta0 * prod_masses (1 - strength/(r_i + 0.1))
    # Actually per spec: theta(r) = theta0*(1-f), f = strength/(r+0.1)
    # For multiple masses, use additive f
    theta_grid = np.full((n, n, n), THETA0)
    total_f = np.zeros((n, n, n))
    for mp in mass_positions:
        r = min_image_dist(n, mp)
        total_f += strength / (r + 0.1)
    theta_grid = THETA0 * (1.0 - total_f)

    for _ in range(n_layers):
        psi = apply_coin_and_shift(psi, n, theta_grid)
    return psi

def probability_density(psi):
    """Total probability density at each site."""
    return np.sum(np.abs(psi)**2, axis=0)
```

End of inlined excerpt. The oscillation runner consumes `evolve` and
`probability_density` via the `shell_diff(n, n_layers, strength, mass_offset)`
proxy (defined in `scripts/frontier_chiral_layer_oscillation.py`), which
computes `(toward - away)` shell sums of `rho1 - rho0` over the mass-side
and opposite-side shells.

## Finding

The chiral walk's gravity sign is not invariant in the number of
propagation layers `N`. The current frozen runner checks the canonical
3+1D chiral-walk implementation at `n=15`, periodic boundary conditions,
`theta0=0.3`, strength `5e-4`, and mass offset `+3`; it observes both
signs across the finite sweep:

```
N=12: AWAY   (-2.89e-5)
N=14: TOWARD (+1.04e-5)
N=16: AWAY   (-1.82e-6)
N=18: TOWARD (+3.83e-5)
N=20: TOWARD (+2.55e-5)
```

The older inline table reported different exact signs and magnitudes for
some `N` values. Treat those historical numbers as unfrozen provenance;
the durable source claim is the bounded sign-noninvariance check above.

## Impact

This narrows the earlier `n=9` versus `n=15` discrepancy story: layer
count is a real finite-window variable, but the current frozen replay
does not by itself ratify the older exact `N=12`/`N=16` explanation.

This also blocks treating single-`N` 1+1D and 2+1D TOWARD cards as
universal gravity evidence without the corresponding multi-`N` check.

## Root-cause hypothesis

The chiral walk has a built-in oscillation period related to the coin
angle θ. The coin mixes ψ₊ and ψ₋ with period ~π/θ layers. Near mass,
θ is modified to θ(1-f), creating a phase mismatch that accumulates
differently at different N. At some N values the accumulated mismatch
produces TOWARD; at others, AWAY.

This is the chiral walk's analog of the transfer matrix's k-dependent
resonance: instead of oscillating with wavenumber k, the chiral walk's
gravity oscillates with propagation distance N.

The runner verifies the sign-noninvariance diagnostic. It does not prove
the mechanism hypothesis in this section.

## Implication

On this finite operating slice, the chiral walk does NOT produce a
gravity proxy that is independent of propagation distance. It produces
`N`-dependent sign changes, so this card cannot be used as a universal
Newtonian-gravity surface.

The paper must frame this honestly: the chiral walk produces gravity
that oscillates with distance, not Newtonian 1/r gravity.

## Open question

Is there a coin design where gravity doesn't oscillate with N?
The oscillation comes from the θ-dependent mixing period. If θ is
chosen so that the mixing period matches the lattice spacing, the
oscillation might average out. Or a different coupling mechanism
(not θ-modulation) might avoid the oscillation entirely.
