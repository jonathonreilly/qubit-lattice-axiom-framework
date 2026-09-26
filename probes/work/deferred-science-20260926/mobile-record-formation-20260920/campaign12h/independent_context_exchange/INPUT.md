# Supplied specification and independence boundary

This is a bounded independent derivation from the task specification below.
No primary context-exchange, streaming, current-classification, or other new
author calculation was read or imported before this report and evidence seal.
No outside file was modified. No Git, PR, audit, delegation, or external
communication action was taken for this check.

The graph is Z^3 or a nearest-neighbor simple cubic torus whose coordinate
periods are at least four. The alphabet consists of vacancy 0, with n(0)=0 and
v_0=0, and six occupied immutable contents v_a in {+/-e_1,+/-e_2,+/-e_3}, with
n(a)=1. A positive-i edge (x,x+e_i) exchanges its endpoint states. For the
four states (l,a,b,r) at (x-e_i,x,x+e_i,x+2e_i), define f_i(a)=v_a dot e_i and

    h_i = u(f_i(a)-f_i(b))
          + E[(f_i(a)-f_i(b))(n(l)+n(r))
               +(n(a)-n(b))(f_i(l)+f_i(r))].

The two alternative exchange implementations are

    c_i = K + h_i/2,       K > |u| + 2|E|,
    c_i = kappa0 + max(h_i,0),       kappa0 > 0.

Requested targets: positivity and joint cubic covariance; stationarity of
every homogeneous product distribution; exact homogeneous species currents
and their six-variable Jacobian at occupied probabilities p_a=rho/6;
existence or obstruction for direction-independent nonzero propagation
eigenvalues of that Jacobian; the distinction between this current algebra
and microscopic waves/hydrodynamics; and the effect of adding independent
births of each of the six labels at rate epsilon at vacancies. Seek decisive
counterexamples or controls, and preserve the precise scope.
