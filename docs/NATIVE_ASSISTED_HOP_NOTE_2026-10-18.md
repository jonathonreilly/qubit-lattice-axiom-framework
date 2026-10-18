# Native defect motion changes the collective background

Status: bounded-support. Three virtual spin-flip interactions in the original
one-qubit Hamiltonian move a defect and reverse both neighboring column
backgrounds. No new interaction or assigned fluctuating field is needed.

The [complete nearest-hop calculation](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ASSISTED_HOP_PROOF.md)
includes the canonical normalization terms. For an x-edge, the resulting
Hamiltonian block is

    Hji/J = -lambda I + lambda³(I/8 - X_i X_j/4) + O(lambda^4).

The column-pair operator is already part of the neutral collective model.
Its vacuum variance has a positive analytic lower bound. A matched dressed
preparation therefore has a nonzero infinitesimal neutral vertex with
squared weight proportional to J²lambda^6, with the coefficient calculated
from native paths. This is not a finite-time emission rate or a derived
detector, and the effective matrix block is gauge dependent.

Relaxed defects still require a separate calculation. Their nearby loop
fluctuations are suppressed by the derived environment backreaction; those
loop operators must not be confused with the column-pair vertex above.
The distinction prevents assuming that a prepared vacuum probe already
represents the coupling of an energy-minimizing matter feature.

[Replay](../scripts/native_assisted_hop.py) checks all-background symbolic
third-order coefficients, complementary-layer paths, and the variance
constants. All controls are exposed model development. No observed scalar,
three-dimensional fermion, or universal gravitational coupling is claimed.
