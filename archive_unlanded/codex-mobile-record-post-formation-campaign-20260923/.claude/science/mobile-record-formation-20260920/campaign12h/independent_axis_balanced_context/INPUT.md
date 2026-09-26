# Supplied model and independent source boundary

This is a bounded pre-source derivation for the cubic seven-state lattice:
vacancy 0 has n=0,v=0; occupied immutable labels are +/-e_i and have n=1.
For direction i define f_i(a)=v_a dot e_i, q_i(a)=f_i(a)^2, and
s_i(a)=A n(a)+B q_i(a). On each positive-i edge, let (l,a,b,r) be the states
at x-e_i,x,x+e_i,x+2e_i. The endpoints exchange at rate

    h_i = u(f_i(a)-f_i(b))
          + E[(f_i(a)-f_i(b))(s_i(l)+s_i(r))
               +(s_i(a)-s_i(b))(f_i(l)+f_i(r))],
    c_i = kappa0 + max(h_i,0), kappa0>0,

or c_i=K+h_i/2 with fixed sufficiently large K. Torus periods are at least
four; the infinite graph is Z^3. All parameters are fixed when densities
are differentiated.

Determine stationary product laws, exact currents, nonlinear entropy
compatibility, the complete six-density directional current linearization
at p_a=rho/6, and the conditions for a nonzero direction-independent acoustic
pair at every interior density. Examine the particular fixed choice
u=0,E=1/2,A=2,B=-3. Check rates, cubic covariance, extra modes, uniform births,
and each needed hypothesis of the previously sealed smooth-profile Euler
proof. Only the two earlier independent current/Euler reports may be reused;
no primary new derivation, fluctuation calculation, simulation, or its
outcome may be read before sealing. Write only in this assigned directory;
no Git, PR, audit, external messages, or delegation.
