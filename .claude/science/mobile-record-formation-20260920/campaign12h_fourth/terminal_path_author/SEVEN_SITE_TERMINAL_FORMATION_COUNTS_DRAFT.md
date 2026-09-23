# Terminal formation counts on the seven-site path: analytic plan

Root personal follow-up, 2026-09-23. This is a pre-control draft. It uses the
independently constructed seven-site physical matrices in the sealed
`formation_capacity_independent/FINITE_PATH_RESULTS.json`, not the author's
capacity builder. Its question is whether the known one-third trapped
first-birth branch is the entire probability of ending with one birth.

Let `Omega` be the all-A-plus, B-empty physical word. The checked source has
`H Omega=-12 delta Omega`, `Gamma Omega=12 kappa Omega`, `D Omega=0`.
For `kappa>0`, a first event occurs almost surely and its conditional
post-event density, independent of its time, is

    J_Omega / 12 = (1/12) sum_mu B_mu |Omega><Omega| B_mu^*,

where the sum is over the actual resolved or coherent channels without an
extra normalization. Both conventions have total trace 12, but their
post-event coherences can differ. This takes no microscopic energy-selection
or field-only limit.

The N=5 sector is finite dimensional (30 physical words). Write its
Hamiltonian `H_5=K D_5+delta H4_5` and loss `Gamma_5=kappa Gamma0_5`.
The no-event generator is `G_5=-iH_5-Gamma_5/2`. The maximal unitary
subspace of this contraction is

    M = intersection_(j=0..29) ker(Gamma0_5 H_5^j).

Indeed a vector on an imaginary-axis eigenspace of G_5 has zero loss by
the norm derivative, hence is an H_5 eigenvector in ker Gamma_5. The converse
is immediate. In finite dimension all other spectral components decay; a
contraction cannot have a nontrivial Jordan block on the imaginary axis.
Thus for any first-event N=5 density, the terminal probability of exactly
one birth is `Tr(P_M J_Omega)/12`; that of two births is its complement.
This statement concerns the count limit, not a full density limit: H_5 can
rotate surviving dark coherences forever.

Compute M exactly via the stabilized row span of Gamma0, Gamma0 H_5, ...;
for K/delta ratios 0, 1/3, 1, 2, 5 and the delta=0 edge cases. Compare
the resolved and coherent J_Omega. Check all physical source hashes, sector
dimensions, first-rate normalization, projector equations and the known
one-third lower bound. Do not claim a formula beyond those exact cases
without a separate symbolic argument. Preserve any failure or singular
parameter set. A later interpretation must not extrapolate the finite path
to an infinite lattice or derive a native TOE source.
