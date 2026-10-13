# Conditional regular three-field limit of the new potential

Parent /root derives this consequence of the new exponential action. It is
separate from the old u=k²v singular scaling. Keep fixed bounded u,x,y and
their velocities, with the same supplied gas/calibration. Divide all scalar
Euler–Lagrange equations by k. The limit is the ordinary curved-metric system

    g=exp(-u) diag(1/4,4/(9D0),1/(3D0)),
    W=3(1-exp(-u))²/2+exp(-2u)(x²/2+y²/3+nu u²/2),
    B=H_GR²=1+2R0 rho_J/3, h=-R0(rho_J+P_J)/B,
    phi'=p,
    p_i'=-(3+h)p_i-[C_i+(W_i+delta_iu exp(-u)R0 tau_J/2)/B]/g_i,
    C_i=p_i sum_j(partial_j g_i)p_j
            -(1/2)sum_j(partial_i g_j)p_j².

Primes here use N_J, whose limit equals the Einstein e-fold clock. The
matter trace force survives: alpha_B/k tends to exp(-u)/2 even though the
physical expansion tends to the supplied GR reference. In particular, the
u degree of freedom remains dynamical. Its finite amplitude is not discarded.

For use with the already supplied gas let L=log(T_initial/T). Divide the
equations by c_T(L)>0 and transform x,y and their velocities with the known
smooth factors xi0 exp(-3N_J/2),yi0 exp(-2N_J). The initial scaled state is
[0,1,1,0,-3/2,-2], with xi0²=R0 rho_dust,initial and
yi0²=R0 rho_gas,initial. This is an explicit chosen initial condition.

## What now permits a conditional history theorem

For fixed finite L interval and smooth positive c_T, smooth supplied fluids,
and fixed nu>0, the full new-action vector field extends C1 to k=0 on compact
finite-state sets. To see this, multiply the F denominators by k as in the
coefficient derivation: K=k g(k), U=3/2+k W(k), alpha_B=k a_B(k), with g(0)
positive and g,W,a_B smooth; C_B is smooth with C_B(0)=1. Every lowered scalar
force and metric derivative carries k, which cancels its kinetic denominator.
The constraint denominator tends to3, its numerator stays positive, and the
physical-clock rate tends to1. No residual 1/k force remains. The scaled
initial condition and calibration are smooth in k.

Assume a limiting solution exists on the whole fixed interval and stays in
a compact finite-state region. Choose a slightly larger compact neighborhood.
For sufficiently small positive k, the full vector fields there have a common
Lipschitz constant and differ by at most M k; the initial data differ by O(k).
The integral equations and Gronwall inequality bound the state difference by
(initial difference + M k times interval length) exp(Lipschitz times length).
A standard exit-time continuation then keeps the finite-k solution inside
that larger region and proves O(k) uniform convergence on this fixed interval.
This argument is conditional on the bounded limiting solution and fixed fluid
model. It gives no useful numerical error constant for the physical history,
no global-in-time theorem and no quantum or inhomogeneous stability result.

Smooth readouts consequently yield the previously derived instantaneous
first coefficient C_exp evaluated along the limiting solution, with
H_J²/(H_v² B)=1+k C_exp[limit]+O(k²) on such an interval. Numerical integration
is supporting evidence for the specified history, not a proof of its global
existence or of an explicit rigorous remainder bound.

## Frozen computation

Integrate the full six-state limiting system twice: DOP853 at rtol1e-10,
atol1e-12,max L step.0125 and Radau at rtol2e-10,atol2e-12,max step.025,
both using the fixed256-node gas. Compare all241 temperature sites within
3e-7 scaled-state discrepancy. Evaluate C_exp along the limit. Compare all
three previously completed refined finite-k new-action histories at their
same stored L and natural smooth calibration. Report state differences and
the residual (Hratio²-1)/k-C_exp, without imposing a post-hoc empirical or
convergence acceptance threshold. Do not use any old-action trajectory.
