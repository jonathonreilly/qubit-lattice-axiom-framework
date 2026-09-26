# Independent Euler-limit task and source boundary

Use the specific seven-state context-exchange generator and homogeneous
currents independently checked in ../independent_context_exchange/REPORT.md.
On the periodic N by N by N lattice, fix u,E and the strictly positive
exchange floor independently of N, and accelerate the microscopic generator
by N. The alphabet is vacancy 0 and six immutable occupied labels +/-e_i;
every exchange, including an exchange between different occupied labels,
is allowed at the stated positive floor.

For the four collinear states (l,a,b,r), the rate is either

    h_i = u(f_i(a)-f_i(b))
          + E[(f_i(a)-f_i(b))(n(l)+n(r))
               +(n(a)-n(b))(f_i(l)+f_i(r))],
    c_i = K+h_i/2, K>|u|+2|E|,

or c_i=kappa0+max(h_i,0), kappa0>0. Here f_i(a)=v_a dot e_i.

Given a C^2 periodic interior solution p(t,X) of the six-density Euler system
with this generator's exact product currents, with all seven probabilities
bounded below on [0,T], and initial relative entropy o(N^3) against the
inhomogeneous product with parameter p(0,x/N), determine whether relative
entropy remains o(N^3) and empirical profiles converge. Reconstruct the
local-equilibrium step for the four-site, three-dimensional generator rather
than importing a theorem with unverified endpoint-only or one-dimensional
hypotheses. Also assess the optional microscopic birth rate epsilon/N per
label at vacancies, giving generator N H + epsilon B in Euler time. Fixed
microscopic epsilon under that same time scaling is a different question.

No new primary Euler derivation, primary context note, simulation, or its
outcome may be read before sealing. Only this assigned directory may be
written. No Git, PR, audit, external-message, or delegation actions.
