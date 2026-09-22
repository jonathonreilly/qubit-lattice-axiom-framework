# Exact inhomogeneous initial current and its nonlinear Euler derivative

**Status:** proposed conditional initial-time theorem; controls and independent
check pending. **Date:** 2026-09-21. **Dependencies:** the actual routed rates
in `DIMER_ROUTED_RECORD_TRANSPORT.md` and the flux definitions in
`DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md`.

Fix an even torus side N>=8 with the winding matching from every black site
u to the white site u+e_1. All records remain permanent, pair colors are
immutable, and only the existing routed color-exchange dynamics is used.
Take k0>|gamma|. At time zero draw independent colors at black anchors with
probabilities p(u/N), where p is a fixed C^3 periodic profile in the interior
of the fourteen-color simplex. This is a supplied inhomogeneous preparation;
it is not asserted to be produced by the earlier birth law.

For a direction delta in {+/-e_i}, the owner route has displacement

    a_delta=delta-e_1.

The +e_1 route is fixed and has no exchange. For the five other directions,
the four distinct contexts are at u-a_delta,u,u+a_delta,u+2a_delta. Let their
probabilities be p_l,p_u,p_w,p_r. Set

    S_delta(a,b)=(gamma/2)delta.[e_a cross b_b+e_b cross b_a],
    s=S_delta(p_l+p_r),
    mu_u=p_u.s,        mu_w=p_w.s.

The actual channel rate is k0/2+h/4, where
h=S(l,a)+S(a,r)-S(l,b)-S(b,r). Summing over the four independent initial
colors gives the **exact** expected outgoing color-current vector

    J_delta^N(u)
      =(k0/2)(p_u-p_w)
        +(1/4)[(p_u+p_w) elementwise s
                         -p_u mu_w-p_w mu_u].       (1)

Its fourteen entries count color moving from u toward its route successor;
their sum is zero. This calculation uses independence only at time zero.
It does not replace later joint laws by products.

All current sums below run over the five nonfixed directions. The final
tensor identity can also include +e_1 because its displacement is zero.

For I_(u,a) the indicator that anchor u carries color a, the Markov generator
therefore gives exactly

    d/dt E I_(u,a)(t)|_(t=0)
       =sum_delta [J_delta^N(u-a_delta)-J_delta^N(u)]_a. (2)

Incoming and outgoing routes are counted once, with their actual half-rate
normalization. At a homogeneous p, (1) reduces to

    J_delta(p)=F_delta(p)/2,

where F_delta=delta.F and F is equation(1) of the nonlinear-flux note.
Although this homogeneous current has zero divergence, its profile derivative
is nontrivial.

For the smooth profile, (1) is a polynomial in a fixed finite stencil of p.
Taylor expansion, including its first spatial derivative, gives uniformly

    J_delta^N(x)=F_delta(p(x))/2+N^-1 R_delta^N(x),
    sup_N ||R_delta^N||_(C^1) < infinity.            (3)

The symmetric k0 term is included in R; no large-scale diffusion term is
silently identified with zero at finite N. Bounds depend on the fixed
profile, k0 and gamma. Applying the finite difference in (2) to (3), and
Taylor expanding its first term once more, yields

    N sum_delta [J_delta^N(u-a_delta)-J_delta^N(u)]
      =-(1/2) sum_delta (a_delta.grad)F_delta(p(u/N))+O(N^-1).

Finally

    (1/2)sum_delta a_delta tensor delta
       =(1/2)sum_delta(delta-e_1) tensor delta=I.

Thus the exact microscopic initial expectation satisfies the uniform bound

    sup_(black u) |N [d/dt E I_u(t)]_(t=0)
                         +div F(p)(u/N)| <= C_p/N.  (4)

The constant is finite for the declared fixed smooth profile and rates. This
is a nonlinear, inhomogeneous **initial-derivative** result for the existing
local stochastic dynamics. It strengthens the connection between its exact
current and the candidate nonlinear conservation law without asserting a
finite-time hydrodynamic limit, preservation of local equilibrium, or shock
control. The finite-N k0 correction and all higher color moments remain
present in the exact formula (1).
