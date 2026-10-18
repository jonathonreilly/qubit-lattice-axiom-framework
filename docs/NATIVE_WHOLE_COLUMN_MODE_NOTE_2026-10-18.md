# Native many-spin light features and winding kinetics

Status: bounded-support. Large features involving whole columns can have
vanishing excitation energy in a controlled weak-coupling, growing-box family
of the supplied one-qubit Hamiltonian. The interaction already present also
generates their first offdiagonal kinetic term. No scalar or coupling is added.

For even cubes L~lambda^-p, 0<p<4, a large rectangle of flipped whole columns
changes Theta(L³) spins but costs only

    Delta = J L[lambda^4/16+O(lambda^5)].

The fixed-order local normal form constructs microscopic quasimodes at this
energy, with dimension-free error bounds. Their translation orbit supplies
transverse momenta only. At every prescribed algebraic accuracy the construction
is nearly flat; it does not establish a propagating isolated band.

The original connected bond readout has spectral weight below Eg+J smaller
than every algebraic power in this family. At nonzero longitudinal momentum,
that low response is exactly zero. This concerns the original readout and
actual ground states; it is not a prohibition on all detectors or preparations.

At fixed even column length L, the first native wall-free offdiagonal term is

    -gamma_L sum_<ij> Xbar_i Xbar_j,
    gamma_L = J lambda^L binomial(2L-2,L-1)/8^(L-1),
    Xbar_i = product_z X_(i,z).

The coefficient follows by summing native intermediate wall energies, with an
exact Catalan recursion. It is a fixed-L Taylor result, not a uniform claim
that this term dominates when L grows. Exact subset controls through L16 and
small fixed-L diagonalizations check the combinatorics and leading coefficient.

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md)
and [runner](../scripts/native_whole_column_modes.py) separate the actual
microscopic low-energy estimates from the finite-size kinetic coefficient.
The supplied Hamiltonian, weak regime, ground-state condition, measurement
operator and units remain assumptions. No observational fit or independent
empirical test is performed. A cosmological scalar and its measured source
and detector connection remain open.
