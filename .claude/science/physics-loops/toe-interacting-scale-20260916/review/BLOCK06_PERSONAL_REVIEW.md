# Personal review: bounded neutral matter dynamics

2026-09-16 UTC. Same-author review only. No independent review or audit.

The source is notes/BLOCK06_JOINT_BOUNDED_MATTER_DYNAMICS.md. It composes on
the provisional branch at6c7548b8e7d09a0aba9c6585a8cfdc802d40dc09.

The exact electric commutator includes the quadratic path term. The charged
fixture checks it with a two-link transfer; deleting that term gives a finite
discrepancy. The hopping comparison is separately built as the difference
between the actual flux-shifting closing link and the rooted free CAR
hopping. The total commutator agrees with electric plus compact-loop terms.
The direct finite-time vector comparison uses alpha_free(-t), and the
opposite sign is rejected. The fixture shares its explicit Gauss basis with
earlier work; it is a new challenge of the present commutator/dynamics, not
an independent numerical proof of the three-dimensional limit.

In the analytic argument, adjoint state norms are handled by moving the
electric operator, rather than equating annihilator and creator norms.
Polynomial residuals retain the extra path-overlap terms. Their linear
spatial weight follows from the Cauchy--Schwarz bound on two path vectors.
Weighted l1 control of free finite-range spreading keeps that coefficient
bound uniform under truncation. A separate l2 tail bound controls the CAR
operator norm and derivative truncation error.

Periodic wrapping is excluded by the explicit radius choice. The static
theorem is applied only after comparison with a FIXED-radius polynomial,
not directly to the growing radius R(L). Multi-time convergence uses norm
propagation on ground-created vectors, bounded CAR multiplication, and fixed
approximations in succession. It does not rely on a shrinking many-body gap.

The initial state is in the specified number sector, while neutral
number-changing observables evolve under the same Hamiltonian on the full
Gauss Hilbert space. Nonneutral CAR factors are auxiliary. No positivity of
the shifted Hamiltonian outside the initial sector is assumed. Operator
norms on the physical restriction need only be bounded by CAR norms; an
unneeded equality was weakened to that sufficient inequality. Alternative
finite path choices are extended by coordinate paths elsewhere, making the
weighted-growth premise explicit instead of assuming it for an arbitrary
infinite path system.

Disposition: complete provisional author argument for fixed bounded neutral
matter words at finitely many bounded times. Independent mathematical review
is pending. The theorem still sends g->0 and does not establish fixed-g
infrared weakening, full nonlinear gauge evolution or axiomatic law selection.
