# Next leverage: remove the affine-input dependency in a stronger scaling regime

Personal block11 design, 2026-09-14 after the conditional Maxwell milestone.
Proposed derivation, not yet checked or delivered. No workers. Deadline
remains 2026-09-15 01:30:44 UTC; about three hours remain.

The all-affine proof supports a generous scaling theorem, but its uniform
current-ensemble estimate is a substantial provisional dependency. A more
restrictive explicit weak-coupling sequence may admit a direct elementary
proof and control genuine charged Wilson loops, not just the neutral score.

Candidate route:

1. For the equal four-torus let S=im d and K=d Z^E. Integral cohomology has
   no torsion, so K=Z^P intersect S. Let Lambda_Q=(I-P_e)Z^P. Each coset of
   M_N=K+N Z^P modulo K is uniquely indexed by N Lambda_Q.
2. Both K* in S and Lambda_Q in S-perp have shortest nonzero vector at
   least 1/4. For K*, d* w is a nonzero integer vector and ||d||<=4. For
   Lambda_Q, either d_2 n is a nonzero integer vector and ||d_2||<=4, or
   n is closed and its nonzero integral two-cycle flux gives harmonic
   norm at least one on an equal four-torus. Check all cohomology details.
3. A rank-m lattice with separation lambda has shell count at most
   (2k+3)^m on k lambda<=||w||<(k+1)lambda. Therefore, if
   t lambda^2>=2m log5, its nonzero theta tail is at most
   2 exp(-t lambda^2/2). This is a crude dimension-dependent packing
   estimate, not a uniform finite-coupling phase argument.
4. Centered theta maximization on K bounds the mass of every nonexact
   coset by its perpendicular Gaussian. If beta>=16m log5/pi^2,
   Pr(z notin K)<=2 exp(-pi^2 beta/16), with m=3L^4+3.
5. Conditional on z in K, X=z/sqrt(beta_d) is an exact-lattice Gaussian.
   Poisson summation gives its characteristic function relative to
   exp(-||P_e h||^2/2). If beta_d>=32r log5/pi^2 and
   ||P_e h||<=pi sqrt(beta_d)/8, r=3L^4-3, the relative error is at most
   2 exp(-pi^2 beta_d/32). The source term is real in the dual theta sum.
6. Combining gives the candidate finite-volume bound

   |E exp(i h.X)/exp(-||P_e h||^2/2)-1|
     <=2 exp(-pi^2 beta_d/32)
       +4 exp(-pi^2 beta/16+||P_e h||^2/2).

   Check the factor, source radius and use of absolute versus relative
   errors. This eliminates AFF in this stronger parameter regime.
7. Choose beta=64 L^4, N=8 beta, any a->0 and aL->infinity with even
   L>=4. The dimension-dependent hypotheses hold. Repeat the physical
   score-noise and cell-average argument to obtain the Gaussian Maxwell
   field by an independent proof. It does not cover fixed beta, fixed N,
   or a selected native law.
8. For a contractible integer surface S_C with boundary current j_C,
   the genuine clock Wilson loop W_q(C)=exp(i q<j_C,theta>) equals
   exp(i h.X) for h=q S_C/sqrt(beta). The integer lift disappears
   exactly. Choose q_j nearest to g sqrt(beta_j). For fixed physical
   rectilinear loops with spanning area O(a^-2), the relative bound
   above tends to zero despite the self-energy divergence.
9. For two disjoint fixed physical rectangles, normalize the joint loop
   expectation by its two individual expectations. The self terms cancel
   and the proposed limit is

   exp[-g_1 g_2 integral_C1 dx_mu integral_C2 dy_mu
                    /(4pi^2 |x-y|^2)].

   Need a genuine off-diagonal discrete Green-function limit, with the
   finite periodic harmonic term controlled; no covariance-at-a-point
   extrapolation or presumed thin-loop continuity of distributions.
10. For two separated Euclidean-time rectangular dipole loops, the
    large-time logarithm per time yields the Coulomb interaction of
    their four external temporal lines. The exact time integral is

    [ (T/R) arctan(T/R) - 0.5 log(1+T^2/R^2) ]/(2pi^2),

    divided by T tending to 1/(4pi R). Return charges may be sent to
    infinity only in a stated subsequent limit. These are external
    charged probes; charged particle states and matter remain open.

The main analytic obligations are saturation of K, the quotient-lattice
shortest-vector bound, correct Poisson source control, and uniform
off-diagonal Green convergence. The field construction can be stated
without an AFF dependency if all four are proved directly. No claim of
a new finite-clock phase mechanism or of a native TOE follows.
