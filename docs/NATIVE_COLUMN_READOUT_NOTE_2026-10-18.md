# Derived original-readout coupling to many-spin column features

Status: bounded-support. The same native interaction determines both the
static readout profile of a large column feature and its first winding
observable coefficient. No scalar field, detector interaction or adjustable
coupling is inserted.

For a large rectangle of whole columns in the controlled weak regime,

    Delta<C_0> = 3 Delta_4/(J sqrt(V)) [1+O(lambda)],
    Delta_4 = J L lambda^4/16.

The spatial contrast is concentrated near the four bad-plaquette corners.
Its leading Fourier factor is derived, including the lattice cosine factors.
This is the expectation-value contrast of a specified dressed feature relative
to an actual ground state, not an inelastic transition or gravitational charge.

For fixed even column length L, the first winding source term is

    -3 gamma_L (L-1)(L-2)/[J sqrt(V)(2L-3)] sum_<ij> Xbar_i Xbar_j,
    gamma_L = J lambda^L binomial(2L-2,L-1)/8^(L-1).

An exact marked-Catalan identity evaluates the native virtual paths. The
source coefficient includes the unitary-connection check required when
Hamiltonian derivatives are used to calculate observables. It is not inferred
from a fitted coupling or extrapolated to a growing-L kinetic theorem.

The static coefficient and winding coefficient disagree with a single regular
energy-proportional operator identification. This narrows the measurement
bridge still needed; it does not test gravity or exclude other observables.

See the [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md)
and [runner](../scripts/native_column_readout.py). Exact path, local Pauli and
virtual-dressing controls are exposed development checks. The physical scale,
cosmological state, detector identification and useful propagating scalar
remain open. The earlier low-energy inelastic darkness is consistent with a
nonzero static feature contrast.
