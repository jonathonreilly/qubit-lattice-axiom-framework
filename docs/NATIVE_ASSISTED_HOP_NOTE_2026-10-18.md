# Native defect motion changes the collective background

Status: bounded-support. Three virtual spin-flip interactions in the original
one-qubit Hamiltonian move a defect and reverse both neighboring column
backgrounds. No new interaction or assigned fluctuating field is needed.

The complete nearest-hop calculation (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9793/NATIVE_ASSISTED_HOP_PROOF.md`)
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


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_assisted_hop.py`

The complete mathematical sources and owning-head helpers are portable literal inputs. The supplied Hamiltonian, geometry, state, observable and order of limits remain premises. The primary executes finite coefficient and algebra controls under one enforced aggregate cap, streams child diagnostics, and writes fresh isolated outputs. Analytic asymptotic and microscopic transfer results are supplied by the complete proofs, not numerically established by finite controls. Historical verdicts and saved numerical diagnostics confer no current authority.
