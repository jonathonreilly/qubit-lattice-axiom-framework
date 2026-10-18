# Actual light neutral window from native column features

Status: bounded-support. The unchanged one-qubit Hamiltonian and original
bond readout produce positive spectral weight at a genuinely low excitation
energy in a fixed finite box. No collective oscillator or coupling is added.

For even column length L>=6, fixed even transverse side R>2L, and lambda tending
to zero with geometry fixed, the original ground-state readout has weight
in the window [0.9,1.1] Delta4, where

    Delta4 = J L lambda^4/16,
    W0 = 2 gamma_L²/(J² L) (A_L/2-3)² [1+O(lambda)],
    gamma_L = J lambda^L binomial(2L-2,L-1)/8^(L-1),
    A_L = 6(L-1)(L-2)/(2L-3).

The coefficient is positive. It includes the correction from ground-state
mixing; using the bare winding-source coefficient alone would give the wrong
answer. The result holds for every actual ground state, including selections
from the degenerate reference manifold. The relevant native strings change
2L physical spins, while the full window may contain many split states.

A momentum-resolved formula also derives the transverse readout form factor.
Nonzero longitudinal momentum is exactly dark in this low window. These are
response weights, not a three-dimensional scalar dispersion.

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/LIGHT_COLUMN_WINDOW_PROOF.md)
uses two controlled finite-dimensional block reductions and an exact edge-map
identity. The [runner](../scripts/native_light_column_window.py) checks discrete
geometry, Fourier factors and the required mixing subtraction. It does not
numerically diagonalize the full microscopic box.

The weight is very small, of order lambda^(2L). Fixed-box asymptotics do not
establish uniformity as L grows, an isolated pole, propagation, a cosmological
scale or a physical detector identification. All inputs and checks are exposed
model development; no observational fit or independent empirical test is claimed.
