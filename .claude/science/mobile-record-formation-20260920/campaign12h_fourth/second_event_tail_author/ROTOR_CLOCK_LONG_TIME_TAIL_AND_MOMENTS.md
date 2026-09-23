# Rare long waits in the exact eight-site rotor clock

Primary-author extension of the frozen independent second-event calculation,
2026-09-23. This argument was written before its new controls. The exact block
law is an explicit dependency, independently authored in
../second_event_independent/REPORT.md (PRE seal
e710cf956b2cff69afc8241757901c040a4c2f6b23516f09968cb372975bd734).
This is the supplied unit-rotor effective model, not the joint spin limit.

## Statement and preparation

Let kappa>0, delta fixed, and a=eta-4 delta !=0. Start immediately after
the specified first ring mark with any fixed normalizable initial field
having angle density g(theta), normalized with dtheta/(2 pi). The previously
derived exact survival is

 S(t)=1/2 exp(-4 kappa t)
      +1/4 integral g(theta) sum_(j=0)^5 b_j(theta)
             [f_(a s_+(alpha_j))(t)+f_(a s_-(alpha_j))(t)] dtheta/(2 pi),

 alpha_j=(4 theta+2 pi j)/6,
 s_+/-^2=4+/-4 cos(alpha_j/2),
 b_j^resolved=1/6,
 b_j^coherent=[1+cos(theta-alpha_j)]/6.

The two-state function f_omega is the squared norm from initial (1,0) under

 K_omega = [[-2 kappa, i omega],[i omega,0]].

Here g refers to the field before the normalized first mark; the known word
weights and common first field translation are already accounted for.
This preserves the actual first output, rather than preparing a spectral band.

For g=1 (a single circulation basis state), the mean waiting time is finite,
3/(8 kappa), but its second moment and variance are infinite at every finite
a!=0. More precisely, for either first instrument,

 S(t) ~ [1/(32 sqrt(2 pi kappa) |a|)] t^(-3/2).             (1)

Thus the exponential mixture obtained when eta tends to infinity describes
each fixed-time distribution, even uniformly in t in absolute error, while
it does not preserve the second moment. This is not a failure of that
checked convergence statement.

If g is continuous, put E={0,pi/2,pi,3pi/2} and

 b_*(theta_*)=1/6 (resolved),
 b_*(theta_*)=(1+cos(theta_*))/6 (coherent).

Whenever the sum below is positive, the more general leading coefficient is

 S(t) ~ [3 sum_(theta_* in E) g(theta_*) b_*(theta_*)
          /(64 sqrt(2 pi kappa) |a|)] t^(-3/2).           (2)

If that sum vanishes, (2) with a positive leading term is not asserted.
No tail or moment statement is inferred for arbitrary merely L1 densities
without inspecting their behavior at E.

At a=0 every bright pair decouples, S(t)=exp(-4 kappa t);
both its mean and second moment differ from their nonzero-a behavior.
This exceptional finite-eta parameter must not be silently omitted.

## Second moment by an exact finite-matrix identity

For omega !=0, the positive mean-time matrix X solves
K* X+X K=-I and has

 X11=1/(2 kappa), X12=-i/(2 omega),
 X22=1/(2 kappa)+kappa/omega^2.

The second-moment matrix Y=2 integral_0^infinity t exp(tK*) exp(tK) dt
solves K*Y+YK=-2X. Its lossy-coordinate entry is

 Y11=1/(2 kappa^2)+1/(2 omega^2).                       (3)

These are finite-dimensional convergent integrals for omega!=0.
At omega=0 the initially unpopulated lossless coordinate decouples and
the relevant second moment is instead 1/(8 kappa^2).

Tonelli applies to the nonnegative survival integrals. The flat half
contributes 1/(16 kappa^2), and the bright weights yield

 E[T^2] = 5/(16 kappa^2)
      + [1/(16 a^2)] integral g(theta)
            sum_j b_j(theta)/sin^2(alpha_j(theta)/2)
               dtheta/(2 pi),                          (4)

where the integral may be infinite. Null exceptional angles are ignored
in this integral; neighborhoods of those angles cannot be ignored.
The algebra uses 1/s_+^2+1/s_-^2=1/[2 sin^2(alpha/2)].
Near each relevant theta_*, the singular summand is a positive constant
times g(theta)/(theta-theta_*)^2, unless the corresponding b_* vanishes.
For g=1 the resolved singularities are all positive, and the coherent
one at theta=0 is positive, so (4) diverges. This proves the infinite
second moment without relying on numerical tail fitting.

For comparison, the limiting equal exponential mixture has
E[T^2]=5/(16 kappa^2). Pointwise or uniform absolute convergence of
survival functions alone does not justify interchanging this weighted
infinite-time integral and the eta limit.

## Tail coefficient

For |omega|<kappa put w=sqrt(kappa^2-omega^2). The slow no-event
amplitude has exponent -kappa+w=-omega^2/(kappa+w).
Its squared norm coefficient from the lossy initial coordinate is

 A_slow(omega)=
   [(1-kappa/w)^2+omega^2/w^2]/4
   =omega^2/(4 kappa^2)+O(omega^4).

All other terms decay exponentially at a rate bounded away from zero
on a sufficiently small fixed omega neighborhood. Therefore

 f_omega(t) has slow part
  [omega^2/(4 kappa^2)+O(omega^4)]
  exp[-(omega^2/kappa+O(omega^4))t].

At each theta_* exactly one singular branch vanishes and

 s_min(theta)=2 sqrt(2) sin(|theta-theta_*|/6),
 s_min(theta)^2=(2/9)(theta-theta_*)^2+O((theta-theta_*)^4).

Outside fixed small neighborhoods all relevant two-state generators
decay uniformly exponentially (the critically damped case has only a
polynomial factor). Inside, set
y=|a| (sqrt(2)/3) sqrt(t/kappa) (theta-theta_*).
The scaled integrand is bounded by a constant times y^2 exp(-c y^2)
plus an exponentially small remainder. Continuous bounded g and the
smooth branch weights permit dominated convergence. Using
integral_R y^2 exp(-y^2) dy=sqrt(pi)/2 gives (2), including the
first-output factor 1/4 and angle measure 1/(2 pi).
For g=1, sum b_*=2/3 for both instruments, yielding (1).

The slowly decaying component has small initial probability: near a
vanishing singular frequency its norm weight is O(omega^2).
That suppression makes the mean finite, but not the second moment.
This statement concerns a continuum of normalizable physical field
preparations, not an exceptional sharp-angle eigenstate.

## Checks and boundary

The controls solve both Lyapunov identities symbolically. A stable two-state
survival implementation agrees with complete 2-by-2 matrix exponentials in
36 cases, with maximum discrepancy 1.16e-15. The exact ring formula is
integrated with resolution concentrated near each exceptional angle for
t=100,1000,10000,100000 and three normalizable field densities, using both
instruments. At the last time the six scaled-tail coefficients differ from
(2) by about 1.1e-5 relatively. Excision of neighborhoods of decreasing
radius also agrees with the exact divergent-moment coefficient. Full values,
quadrature error estimates, source hashes and command streams are retained.
These are corroboration; (3)-(4) and the local asymptotic argument carry the result.

No spatially extensive renewal process, indefinite record production,
finite-spin tail law, microscopic conditioned-history convergence or native
theory selection follows here. A long-time limit and a fixed laboratory-time
microscopic approximation require different error control.
