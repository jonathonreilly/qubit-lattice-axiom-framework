# Finite repeated formation: active motion and renewal on an even-leaf star

Working derivation by the root, 2026-09-22. Not yet independently checked or frozen.

Take m even leaves, a center A, hard-core q=0,+1,-1, total charge one, Gauss div E+1_A-q=0. E on each center-to-leaf edge is -q_leaf. Integer spin one normalized shifts already have unit amplitudes for every allowed record hop/birth in this physical sector. P is the occupied-center subspace, Q=1-P. A=QTP with T the signed center/leaf hopping; PTP=QTQ=0.

Every unscaled pair-birth J_j (coherent per edge or separately resolved charge) maps Q to P and raises record number by two. Their common loss is sum J†J = 2(m-N)Q. For m even, Q has odd N<=m-1, so every Q state can decay. Full-center/leaf P states at N=m+1 are absorbing.

Different scaling from the earlier fourth-order-field regime:
H'=delta Q/epsilon² +delta T/epsilon,
physical H=delta N_B/epsilon²+delta T/epsilon,
birth coefficient beta=kappa/epsilon², delta,kappa>0.
H-H'=delta(N-1)/epsilon², so the two give identical number-block-diagonal densities and marked histories from the declared initial conditions. The offset is not an energy supply.

Let D=delta Q-i kappa(m-N)Q on Q. Effective P-space operators:
H_eff=-(delta²/2) A†(D^-1+D^-†) A,
L_eff,j=sqrt(kappa) delta J_j D^-1 A.
The effect is finite motion plus finite creation, including successive births.
The quantum generator and bath are supplied; this does not derive time or Born probabilities.

Proof route without importing an adiabatic error theorem: write L_epsilon=epsilon^-2 L0+epsilon^-1 L1. For a Hermitian X supported in P define a linear embedding
E0 X=X,
(E1X)_QP=-delta D^-1 A X, with the adjoint PQ block,
(E2X)_QQ=delta² D^-1 A X A†D^-†, with other blocks zero.
Then L0 E0=0, L0 E1+L1 E0=0, and
L0 E2+L1 E1=E0 L_eff.
The last identity includes the recycling J(E2X)J† into P; omitting it loses the births.
Therefore L_epsilon E_epsilon-E_epsilon L_eff
=epsilon(L1 E2-E1 L_eff)-epsilon² E2 L_eff,
where E_epsilon=E0+epsilon E1+epsilon² E2.
All maps are bounded at fixed finite m, delta,kappa. Duhamel plus trace-norm contraction on Hermitian inputs gives O(epsilon)(1+T) for initial P densities on 0<=t<=T. E_epsilon need not be a positive embedding for this argument: its Hermitian defect is explicitly bounded, while both actual semigroups are CPTP. A normalized isometry embedding is optional, not needed.

Adding finite classical event-word/count registers to every microscopic/effective jump repeats the same proof. At a fixed set of time thresholds, piecewise register update rules give O(epsilon) convergence of joint marked event CDFs and conditional output densities. No all-time total-variation bound on complete paths is claimed from this argument.

Check m=2 recovers a single exponential birth clock with rate
4 kappa delta²/(delta²+kappa²), distinct from the earlier Delta~epsilon^-4 regime's 4kappa.
For m=4 the center can be vacated/refilled twice, with a nontrivial 29-dimensional P sector inside the full 45-state physical space. Check actual dimensions rather than assume.
Initial central plus, vacant leaves: total first-event effective rate should be
2m(m-1) kappa delta²/[delta²+kappa²(m-1)²].
A second event and coherent/resolved differences must be checked from the effective dynamics; do not assume a classical cascade.

Original energy/Delta has leading N-1 on P and can grow by two per formed pair. Delta diverges. There is no finite-resource reservoir, cubic-lattice field limit, photon coexistence, native-state preparation, or indefinite renewal theorem.
