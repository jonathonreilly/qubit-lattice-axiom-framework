# Independent equilibrium fluctuation question

Received from the supervising author before access to their fluctuation argument.
This directory is the only permitted write location for this bounded check.

The inputs are the two conservative seven-label exchange generators independently
checked in `independent_context_exchange` and
`independent_axis_balanced_context`, with a fixed positive exchange floor,
bounded finite-range rates, a cubic periodic lattice of volume `N^3`, no births,
and a stationary homogeneous full-support product law. For the six occupied
indicators xi, set C = diag(p) - p p^T, A_i = D J_i(p), and K = 2 pi m for fixed
nonzero integer m. The fluctuation field is

    Y_N(K,t) = N^(-3/2) sum_x exp(-i K.x/N) [xi_x(Nt)-p].

The question is whether Y_N(K,t) - exp(-i sum_i K_i A_i t) Y_N(K,0)
converges to zero in L2, jointly for finitely many modes and times, and what
this implies for the stationary two-time covariance. A proof must reconstruct
the equilibrium current-replacement estimate for the actual nonreversible
context rates. The earlier smooth-profile hydrodynamic result is not sufficient
evidence. Required scope includes fixed time, fixed modes, density, extra
conserved fields and the interpretation of the tuned acoustic formula.

Permitted dependencies: my own sealed prior results, elementary mathematics,
and primary literature if needed. No new primary argument, simulation or
outcome may be read before sealing; specifically no
`CONTEXT_EXCHANGE_FLUCTUATION_DERIVATION.md`. No Git, PR, audit, delegation,
external messages or writes outside this directory. No external literature was
needed in the proof below.
