# Complete normalized kernels: regional Haar mode and all-u chart bound

Author proof, 2026-11-09; independent checking pending. Conditional finite-model
mathematics at assigned base `fbdfb3c1b8852e5de302fab6f0f7cfc70ba04cac`
plus the provisional sources pinned below. This note establishes implications
from those sources, not their independent verification or retained status.
The complete-kernel-energy candidate was suggested in requested Fable approach
advice, communicated and inspected by the parent. That advice is credited as
an idea source, not a certificate. All arguments below are author checks.

## 1. Domain and exact energy

Use exactly the domain of `marginal-regional-relative-coercivity.md` §1:
odd L>=3, kappa>0 fixed, m>=3, actual two-layer paired-root path means,
the terminal-root fine forest with arbitrary permitted internal trees,
and the seven-edge J bounding two distinct adjacent elementary terminal
plaquettes. All surviving terminal outputs are I. All non-tree fine links
and all intermediate links are hidden. R is any set of terminal cells;
I_R comprises its owned hidden links. Select whole surviving kernels and
fine plaquettes having an interior hidden reader. B_R comprises all their
exterior hidden readers, including radial-normalizer readers. No terminal
kernel in J is selected. Use product probability Haar on these coordinates.

Write t=kappa u, Z(s)=integral exp(s w(Q))dQ, H(s)=exp(s)/Z(s), and
r=|M|<=1. For a unit quaternion v define

 Phi_u(v,M)=kappa(r-<v,M>)+[log H(t)-log H(tr)]/u
           =kappa(1-<v,M>)+[log Z(tr)-log Z(t)]/u.          (1)

Then the complete normalized kernel is exactly

 k(v|M)=H(t) exp[-u Phi_u(v,M)].                           (2)

Symmetry of w and w<=1 give 0<=B(s):=(log Z)'(s)<=1 for s>=0.
Thus 0<=(log H)'=1-B<=1; integrating between tr and t proves

 kappa(r-<v,M>)<=Phi_u(v,M)<=kappa(1-<v,M>).               (3)

In particular Phi_u>=0 and Phi_u(I,I)=0. Define Ehat_J,u as the sum
of all fine W_p and all surviving Phi_u; Ehat_R,u is its selected regional
sum with exterior z. Let k_R be the number of selected kernels. The exact
conditional Haar density p_R,u is proportional to

 H(t)^(k_R) exp[-u Ehat_R,u(a,z)].                         (4)

The constant H(t)^(k_R) cancels on normalization and in density ratios.
Equation (4) is exact at every z, including zero means. It does not contain
a Haar-coordinate Jacobian, since its reference measure is Haar.

## 2. Uniform global and local bounds for the u-indexed templates

The radial function G_u(M)=u^(-1)log Z(kappa u |M|) has, away from zero,

 grad_M G_u=kappa B(t|M|) M/|M|,  |grad_M G_u|<=kappa.

Z is even analytic, Z(0)=1, and Z'(0)=0. Hence log Z(t|M|) is smooth
at M=0 for each fixed u (its local series uses powers of |M|²), its gradient
there is zero, and the displayed global Lipschitz bound extends across zero.
Equivalently integrate the radial derivative and use reverse triangle
inequality. Formula (1) therefore gives

 |Phi_u(v,M)-Phi_u(v',M')|
                   <=kappa |v-v'|+2kappa |M-M'|            (5)

for unit v,v' and |M|,|M'|<=1. This does not claim globally uniform higher
derivatives near zero. Word telescoping, finite path lengths and positive
weights transfer (5) to a uniform global Lipschitz bound in all group
readers of each factor, including repeated word occurrences.

On the fixed all-reader identity chart of the nonlinear-chart source,
r>=1/2. With h(s)=log Z(s)-s, another form of (1) is

 Phi_u=kappa(r-<v,M>)+[h(tr)-h(t)]/u.                     (6)

The nonlinear-chart source §3 proves, by tilted moments of X=1-w,
|h^(q)(s)|<=C_q(1+s)^(-q) for each fixed q>=1. Its chain-rule argument
therefore bounds every fixed positive-order reader derivative of h(tr)
uniformly for u>=1. Dividing by u only improves that bound. The value
h(t) in (6) is independent of all readers; its possible growth is irrelevant.
Thus the Phi_u templates have uniform derivatives through order three
(and any fixed finite order) on that chart. This reasoning uses finite
geometric templates with u-indexed coefficients, not compactness of u.

As in the two supplied regional/chart proofs, finite reader arity, incidence,
cell range r0, internal-tree patterns and periodic slot identifications give
uniform absolute derivative row sums. All constants hereafter depend only
on L,kappa; multiply local derivative bounds by the finite slot/incidence
counts. In particular they are uniform in m,R,J position/orientation,
permitted trees and u>=1. Periodic coincident readers add multiplicities.

Put c_g=C(L,kappa)^(-1)>0 from the compact seven-edge theorem. Equation (3)
and that theorem give

 Ehat_J,u(a)>=E_J(a)>=c_g sum_hidden [1-w(a_e)].           (7)

All identity-baseline factors vanish. Extending a regional q by I outside
I_R makes every unselected factor zero, so

 Ehat_R,u(q,I)>=c_g sum_(e in I_R)[1-w(q_e)].              (8)

No recovery detour is required to stay inside R. The actual identity
Hessian, with no Haar term, is alternatively obtained from the exact
normalizer calculation:

 Hhat_J,u=H_E,J+kappa[1-B(kappa u)] diag(V0,V1,O)>=c_g Id. (9)

Each V is the sum of actual positive path-variance forms. Every identity
factor has zero differential. Regional Hessians H_R,u are precisely the
principal restrictions of Hhat_J,u. The uniform row bounds just proved
supply a common M>c_g with c_g Id<=H_R,u<=M Id and common finite range r0.
This checks the inputs to the regional construction for the whole family.

## 3. Regional theorem, stationary field and compact relative bound

There exist epsilon_*,alpha,C,c,C_Q,rho_Q>0, independent of u>=1 and of
all other listed variable geometry, such that if d(z_e,I)<=epsilon<=epsilon_*
for every e in B_R, there is a continuous stationary a*_(R,u)(z) satisfying

 |log a*_e|<=C epsilon exp[-alpha dist(owner(e),R^c)],     (10)
 Ehat_R,u(a*q,z)-Ehat_R,u(a*,z)
                       >=c sum_(e in I_R)[1-w(q_e)]      (11)

for every compact q in SU(2)^(I_R). It is the unique global minimum and
hence the unique mode of the density relative to product Haar. If every
d(q_e,I)<=rho_Q, also

 0<=Ehat_R,u(a*q,z)-Ehat_R,u(a*,z)
                       <=C_Q sum_(e in I_R)d(q_e,I)².    (12)

Here a*q is componentwise right multiplication. Full R has a*=I and
infinite distance to R^c; empty R is the empty configuration. The field is
jointly continuous in (u,z) for finite u>=1 and therefore jointly measurable.
No Lebesgue-chart mode is claimed.

For clarity, here is the regional mechanism with the uniform inputs checked
in §2. Use cell blocks of the fixed number of real hidden coordinates.
Choose M'>M, rho=1-c_g/M', and replace r0 by max(1,r0). The Neumann series
for H_R,u^(-1) has kth term range at most k r0 and norm at most
rho^k/M'. Consequently its XY block is bounded by
c_g^(-1)rho^ceil(dist(X,Y)/r0). Choose alpha>0 with
exp(alpha)rho^(1/r0)<1. Summing against the polynomial four-dimensional
shell bound (2r+1)^4 proves a common inverse bound A in the block norm

 ||x||_w=max_(X in R) exp(alpha dist(X,R^c)) |x_X|.

This uses ambient torus distance and works for holes, disconnected regions
and wrapped regions. Define F_u(x;y)=Ehat_R,u(exp(ix),exp(iy)), where y
are collar logs, and expand its interior gradient as

 grad_x F_u(x;y)=f_u(y)+H_R,u x+N_u(x;y),  N_u(0;y)=0.

Only factors touching the collar contribute to f_u, at interior cells
within r0 of R^c. Uniform second derivatives give ||f_u||_w<=B epsilon.
Uniform third derivatives and range give

 ||N_u(x;y)-N_u(x';y)||_w
             <=K_alpha(s+epsilon)||x-x'||_w              (13)

on the weighted ball of radius s, inside a common small chart. Take
s=2AB epsilon and reduce epsilon_* until A K_alpha(s+epsilon)<=1/2
and all relevant logs remain in that chart. The contraction
x -> -H_R,u^(-1)[f_u(y)+N_u(x;y)] gives x*, (10), and group stationarity.
Its iterates from zero are jointly continuous in (u,z); convergence is
uniform with the same contraction bound. Continuity does not require a
compact parameter interval for u. The full/empty cases follow directly.

For the all-compact step, let h_f,u be one selected factor and S_f its
interior readers. Put b(q)=Im(q) and

 D_f,u(q)=h_f,u(a*q,z)-h_f,u(a*,z)-h_f,u(q,I),
 l_f,e=partial_(x_e at 0) D_f,u(exp(ix)).

Global Lipschitz (5) and |a*-I|,|z-I|=O(epsilon) give |D_f,u|<=K epsilon
on the whole compact product, including zero means. Local third derivative
bounds give |l_f,e|<=K epsilon and a Hessian bound O(epsilon) for D_f,u
on a fixed product cap: interpolate all background logs from zero to their
values and differentiate twice in x and once in those logs. Smooth group
multiplication has bounded derivatives there. Taylor's formula and
|x-b(exp(ix))|<=C|x|³ imply on that cap

 |D_f,u(q)-sum_(e in S_f) l_f,e dot b(q_e)|
                     <=K0 epsilon sum_(e in S_f)d(q_e,I)². (14)

Off the cap some reader has chord distance at least the fixed cap radius;
|D_f,u|<=K epsilon, |l_f,e|<=K epsilon, |b(q)|<=1 and bounded arity then
prove the same (14) after increasing K0. No derivative at a zero mean is
used in this complement argument.

For each interior e, sum_f l_f,e=0: it is the right-tangent derivative of
Ehat_R,u(a*q,z)-Ehat_R,u(a*,z)-Ehat_R,u(q,I) at q=I, and both relevant
energies are stationary there. The common proxy b(q_e) therefore cancels
exactly, also for large q. With D the common incidence bound, summing (14)
gives

 |Ehat_R,u(a*q,z)-Ehat_R,u(a*,z)-Ehat_R,u(q,I)|
                         <=D K0 epsilon sum_e d(q_e,I)². (15)

Since d(q,I)²=2[1-w(q)], choose 2D K0 epsilon_*<=c_g/2.
Equations (8),(15) prove (11) with c=c_g/2 and uniqueness. Finally choose
rho_Q so a*_e exp(i s log(q_e)), 0<=s<=1, remains in the smooth product
chart. Uniform Hessian row bounds yield a dimension-independent operator
bound there. Stationarity and integral Taylor remainder, with log/chord
comparability, prove (12). This proves the complete normalized extension
of the earlier regional mechanism rather than an assertion that a fixed-u
argument automatically has uniform constants.

The exact continuous representative of the Haar density consequently obeys

 p_R,u(a*q|z)/p_R,u(a*|z)
   =exp{-u[Ehat_R,u(a*q,z)-Ehat_R,u(a*,z)]}
   <=exp{-u c sum_e[1-w(q_e)]},                           (16)

and on the product cap is bounded below by
exp{-u C_Q sum_e d(q_e,I)²}. Right translation preserves product Haar.
In a Lebesgue log chart a Jacobian ratio would remain, so (16) is expressly
a Haar-density ratio. No rough-sector probability estimate is asserted.

## 4. Stronger fixed-chart corollary for every u>=1

For this section only, allow the small terminal-output chart of the nonlinear
source, V_c=exp(i v_c dot sigma) for c in O. Keep precisely its scalar
principal-coordinate cube D_I=(-delta,delta)^I and its requirement that all
frozen hidden readers and all terminal-output readers of factors touching I
have scalar coordinates of absolute value <=delta. I may have arbitrary
holes and may select individual components. This is not a compact theorem
for nonidentity terminal outputs.

In the source's notation write the exact negative log Lebesgue density as

 S(a;v)=u E_J,V(a)+N_u(a)+A(a)+constant,
 N_u=sum_surviving h(kappa u r),   A=-sum_hidden log j(a_e).

The source's full finite-template third derivative row estimates, including
mixed hidden/output slots where appropriate, give constants C_E,3,C_N,3,
C_A,3 independent of u>=1 such that throughout the smaller chart

 ||D_a² E_J,V(a)-H_E,J||<=C_E,3 delta,
 ||D² N_u(a)-D² N_u(0)||<=C_N,3 delta,
 ||D² A(a)-(2/3)Id||<=C_A,3 delta.                        (17)

These operator estimates follow by integrating each Hessian entry along
the simultaneous straight interpolation of all small reader coordinates,
then summing the absolute third derivatives in every varying slot. Symmetry
gives the column bound from the row bound. Coordinate dimension does not
enter. N_u is independent of terminal outputs; E uses the full mixed-slot
bound. The uniform estimates for N_u require the h moment bounds of §2,
not bounds on raw log Z derivatives with uncancelled powers of u.

At identity, H_E,J>=c_g Id and
D² N_u(0)=u kappa[1-B(kappa u)]diag(V0,V1,O)>=0 by the exact
complete-kernel calculation. Choose a fixed delta>0 within the source's
smooth chart so that

 C_E,3 delta<=c_g/2,
 (C_N,3+C_A,3)delta<=1/6.                                (18)

Then for every u>=1, without a lower threshold u_*,

 D² S(a;v)>=(u c_g/2+1/2)Id,
 sup_i sum_j |(D² S)_ij|<=u C_H.                         (19)

The second inequality uses the source's uniform second derivative row
bounds and u>=1. The gain over its earlier proof comes from retaining the
positive semidefinite normalizer Hessian at identity, subtracting only its
O(delta) variation, and retaining the Haar Hessian 2/3 at identity.

For a regional scalar restriction I, extend the nearby frozen readers to a
full small-chart field by setting unrelated coordinates to zero. Every
factor differentiated in I is unchanged, and the regional Hessian is the
principal submatrix of this full Hessian. Principal restrictions preserve
the lower bound, row bound and finite range. This proves (19) for the exact
regional conditional as well; fixing other components of a selected link
causes no exception. The analogous empty-coordinate statement is vacuous.

Conditionally on the supplied mixed-cube covariance theorem (nonlinear
source §§4-5), choose alpha>0 so C_H(exp(alpha R0)-1)<=c_g/4, with R0
the common finite reader range. Its weighted-resolvent proof applies to
M_u=u c_g/2+1/2, since the conjugation perturbation has norm at most
u c_g/4<=M_u/2. Thus for C¹ f,g on the closed conditional cube,

 |Cov(f,g)|<=[2/M_u] exp[-alpha d(A_f,A_g)]
                         ||grad_I f||_2 ||grad_I g||_2,  (20)

where A_f,A_g are actual derivative-support blocks, and all norms use the
exact restricted law. In particular 2/M_u<=4/(u c_g). Constants have zero
covariance. Exact surviving scores and the separate orbit covariance term
remain as specified in that source; no connected-four estimate follows.

## 5. Source identities and recovery

Sources below were read in full (the initial combined display clipped the
chart ending, which was read separately). Paths are relative to `parts/`:

| Source | SHA-256 | Dependency |
|---|---|---|
| marginal-nonlinear-chart-estimates.md | b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7 | Uniform h derivative/template bounds; mixed-cube covariance theorem for (20) |
| marginal-regional-relative-coercivity.md | 2d142414fb4992c2a1e907d42d15ca9f7164ee6e90c892d8c3d529b39e297385 | Exact regional conditioning geometry and perturbation/cancellation method reinstantiated here |
| partial-terminal-normalizer-hessian.md | a17f372f928930bd9be6e81d68349a62232a027f17a13a7cd47e813f43584139 | Exact finite-u identity Hessian, quotient Haar and complete kernel conventions |
| two-plaquette-compact-coercivity.md | b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e | Seven-edge compact coercivity and its uniform geometry |

The two first hashes were checked during authoring; the last two are refreshed
at completion. These provisional proofs and their ancestral dependencies are
not independently certified by this note. The parent reports independent
checks underway; no outcome from those checks is presupposed. No fifth
mathematical source was needed. The parent's recorded initial literature pass
is reused; this bounded worker performed no network search and imports no
external theorem beyond the explicitly identified supplied cube theorem.

Applicable repository AGENTS, SCIENCE_WORKFLOW, workhorse and its freshness
procedure were read at the assigned snapshot. The installed workhorse copy
was initially read, but the repository copy was then read and used as the
coherent source; no installed/model-default instruction overrides the parent's
explicit bounded-worker effort. Parent supplied preflight and active lease.
No numerical job, Git/network action, prompt edit, or edit of an existing
source occurred. Only this assigned note was written.

Recovery: (1)-(16) are the uniform normalized-energy regional implication;
(17)-(20) remove the chart u_* threshold. Remaining obligations are the
independent checks of these arguments and the pinned dependency chain, not
an unproved large-u cutoff within either statement. Compact conclusions use
identity surviving terminal outputs and a small hidden collar. The optional
terminal neighborhood belongs only to the chart corollary. This provides no
physical spectral gap, full compact covariance, connected-four response,
rough-collar theorem or probability of the chart. No counterexample was
found; no negative obstruction claim is made.
