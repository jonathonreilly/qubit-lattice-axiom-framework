# Uniform analytic evolution of the actual sampled spectral ADM Hamiltonian

Author proof candidate, 2026-09-30. Focused independent checking is pending.
This is a supplied continuous/nonlocal comparator. It changes neither current
axioms nor their status. The finite Hamiltonian is exactly the one in
spectral-nonlinear-route, with unit lapse and zero shift. No continuum equation
is substituted for its finite canonical gradient.

## 1. Statement and norm

Use an odd n=2J+1 grid on the normalized three-torus, all six canonical metric
pairs, p_A=n^3 P_A, pi_ii=p_ii and pi_ij=p_ij/2. D_j has multiplier ik_j on
representatives Q_J. Finite products mean ordinary grid products. Define
H_J=C_J[1] from the literal Christoffel curvature, not a chain-rule rewrite.
Constants a,K are positive. The continuum comparison H uses ordinary partials.

For scalar Fourier series use |f|_rho=sum_k |fhat(k)|exp(rho |k|_1).
For a matrix sum its entry norms, counting both off-diagonal entries. For
independent canonical p coordinates sum their six component norms. Sum these
norms over every component of an augmented vector. Write N_rho(f) for the
same sum with an extra |k|_1. Finite norms use Q_J; infinite ones use Z^3.
All reality conditions are retained.

Fix sigma0>0 and real analytic initial g0=I+h0,p0 with
|h0|_(2sigma0)<=1/8 and |p0|_(2sigma0)<infinity. The supplied initial finite
coordinates are actual samples I_J g0,I_J p0. There are T>0,C<infinity,
independent of J, such that the actual finite Hamiltonian solutions exist on
[0,T] with a uniform analytic norm bound. They converge to a continuum ADM
solution in radius sigma0/4 with error at most C exp[-sigma0(J+1)/8]. If the
continuum initial scalar and all three momentum densities vanish, the actual
finite densities on [0,T] have the same exponential rate in radius sigma0/8,
with possibly another constant. Constants depend on a,K,sigma0 and the input
bounds. The construction below specifies finite majorant rules and choices;
no useful numerical lower bound for T is asserted by a trajectory plot.

This is local analytic control, not Sobolev stability, long-time convergence,
exact finite first-class closure or a physical time/source selection theorem.

## 2. Exact first-order augmentation

Let B^ij(g)=sqrt(det g)g^ij, q_l,A=D_l g_A, r_l,ij=D_l B^ij.
Gamma(g,q) is the Christoffel expression with q substituted for Dg. Define

 V(g,q,r)=K sum_ijk [r_k,ij Gamma^k_ij-r_j,ij Gamma^k_ik]
       -K sum_ijkl B^ij[Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik].

Treat r_ij as nine local slots while varying; actual r is symmetric. All
canonical g variations use the six independent coordinates with their exact
matrix placement. Let T(g,p) be the kinetic density. Skew summation by parts
on the finite grid gives H_J=mean[T+V(g,Dg,D B(g))] EXACTLY. In particular,
D B(g) has not been replaced by B_g Dg. Put A_A=T_(p_A). The augmented system is

 gdot_A=A_A,
 pdot_A=-T_(g_A)-V_(g_A)+sum_l D_l V_(q_l,A)
                         +sum_l,ij B^ij_(g_A) D_l V_(r_l,ij),
 qdot_l,A=D_l A_A,
 rdot_l,ij=D_l(sum_A B^ij_(g_A) A_A).                         (1)

The Hamiltonian variation in the r term is V_r D(B_g delta g); moving D by
skew-adjointness gives -B_g D V_r in H_g, hence its positive sign in pdot.
The factor n^3 in {g,p} cancels the normalized mean, producing (1) with no
extra volume factor. Direct time differentiation gives (q-Dg)dot=0 and
(r-D B(g))dot=0. Thus actual consistent initial data stay consistent exactly.
These variables are analysis devices and add no canonical/physical carrier.
The same derivation and invariants hold with continuum partials.

Every component of (1) is a finite sum of the form

 F(U)=F0(U)+sum_l P_l(U) D_(j_l) Q_l(U),                     (2)

where all local maps are algebraic analytic functions of U=(h,p,q,r).
This includes D V_q, B_g D V_r, D A and D(B_g A). It is a single spatial
loss, despite the second derivatives in the original metric-only equations.

## 3. Uniform norm and constant construction

For both ordinary and circular convolution,
|fg|_rho<=|f|_rho |g|_rho and
N_rho(fg)<=|f|_rho N_rho(g)+N_rho(f)|g|_rho.
This follows from |wrap(k+l)|_1<=|k|_1+|l|_1 and is valid without a discrete
Leibniz identity. Also |D_j f|_rho'<=|f|_rho/[e(rho-rho')].

Here is an explicit finite procedure for the constants used below. Form the
local maps and their ordinary component derivatives from (1). Bound their
norms by the triangle/product rules, treating each constant matrix and each
coordinate injection literally. For z=|h|<1, the additional primitive bounds are

 |(I+h)^-1| <=3+z/(1-z),
 N((I+h)^-1) <= N(h)/(1-z)^2,
 |sqrt(det(I+h))|, |1/sqrt(det(I+h))| <=(1-z)^(-1/2),
 N(sqrt(det(I+h))), N(1/sqrt(det(I+h)))
                         <= N(h)/[2(1-z)^(3/2)].             (3)

The inverse follows from its Neumann series. For the last two, expand
exp[+/-tr log(I+h)/2]; |tr h^m|<=|h|^m and the product seminorm rule prove
both bounds. These series converge in either Wiener algebra. Local component
derivatives of inverse and square root are expressed by
 delta g^-1=-g^-1 delta g g^-1 and
 delta sqrt(g)=sqrt(g) tr(g^-1 delta g)/2,
then bounded by the same rules, including the norm of each symmetric basis
matrix (at most2). This recursively determines upper bounds for all finite
maps in (2), their Lipschitz constants and their N seminorm coefficients.
No mesh size enters this procedure; only sums over the displayed fixed tensor
indices occur. It is acceptable to increase any resulting constant.

On the ball |h|<=1/4, |U|<=M, choose resulting constants C0,C1,C_h such that

 |F_J(U)|_rho<=C0+C1 N_rho(U),  |A(g,p)|_rho<=C_h.             (4)

For example C0 may be the bound for |F0|, C1 the sum of m_(P_l) times
the seminorm coefficient for Q_l, and
C_h=3a(3+1/4)^2(1-1/4)^(-1/2)M
is a permissible direct bound for the metric velocity. The latter uses
|pi|<=|p| and its literal matrix kinetic derivative. All sums and products
are finite except the explicitly summed elementary majorants in (3).

Let L0,L_P,L_Q be the similarly constructed local Lipschitz bounds, and
m_P,m_Q the local norm bounds on that ball. Taking

 C=1+sigma0 L0+sum_l(m_P L_Q+L_P m_Q)/e                     (5)

gives |F_J(U)-F_J(V)|_rho'<=C |U-V|_rho/(rho-rho') for
0<=rho'<rho<=sigma0, whenever the segment stays in the same ball. This is
also valid for the continuum map. The second product term is bounded by
|P(U)-P(V)| times |D Q(V)|; no spatial chain rule is inserted.

## 4. Bootstrap for every actual finite evolution

The sampling map contracts the Wiener norm. For its derivative,
|D_J I_J f|_sigma0<=N_sigma0(f)<=|f|_(2sigma0)/(e sigma0).
Since B(I_J g0)=I_J B(g0) at the grid points, initial augmented norms are
uniformly bounded by, for example,

 M0=|h0|_(2sigma0)+|p0|_(2sigma0)
           +[|h0|_(2sigma0)+|B(g0)-I|_(2sigma0)]/(e sigma0).

The last B norm is finite from (3). Let M=2M0+2 and use the constants of
section3 on this M ball. Set v=C1+1 and

 T0=min{(M-M0)/[2(C0+1)], 1/[16(C_h+1)], sigma0/(4v)}.       (6)

Along rho(t)=sigma0-vt, upper Dini differentiation of the finite Fourier
absolute values gives d|U|_rho(t)/dt<=C0. The extra radius derivative is
-v N(U), so (4) closes this estimate on the bootstrap ball. Separately,
d|h|_rho(t)/dt<=C_h because gdot=A is algebraic. For t<=T0 these imply
|U|<M, |h|<=3/16<1/4 and rho(t)>=3sigma0/4. The strict inequalities close
by continuity. Finite-dimensional ODE continuation then gives existence
through T0, with no inverse-metric singularity. Reality is preserved by the
real canonical Hamiltonian. These are bounds for the actual consistent
finite system because section2 proves exact preservation of q and r.

## 5. Construct the continuum solution and check uniqueness

Embed every finite state as its trigonometric interpolant E_J U_J. On any
fixed radius rho<3sigma0/4, (4) and the derivative-loss bound give uniform
time derivative bounds. The uniform stronger-radius bound makes Fourier tails
uniformly small in that radius. Finite coefficient Arzela–Ascoli followed by
a diagonal subsequence therefore yields convergence in C([0,T0],A_rho) for
each such rho. The limit obeys the same bounds at3sigma0/4 by Fatou.

Local products and all inverse/square-root series converge in these smaller
Wiener algebras. The difference between a sampled analytic product and its
interpolant is exponentially small on one smaller radius: all aliased terms
come from frequencies outside Q_J, and ordinary Fourier tail estimates apply.
The same is true with one derivative after reserving another positive radius
margin. Applying this to the finite expression (2), its integral equation
passes to the continuum limit in a still smaller radius. Initial data converge
to the consistent continuum data; (1) thus gives q=partial g and r=partial B
also in the limit by time differentiation. The resulting g,p solve the
continuum ADM Hamiltonian equations. No smooth-data existence theorem or
strong-hyperbolicity assertion was used.

For quantitative stability and uniqueness, fix rho1=sigma0/2, rho0=sigma0/4,
d=rho1-rho0=sigma0/4, and shorten time to

 T=min{T0,d/(2eC)}.                                        (7)

For any two bounded trajectories in the metric-safe convex ball, their
linearized difference operator has the scale bound (5). Iterate the Volterra
equation m times, allocating d/m to each of its m factors. Its norm is at
most (Cm/d)^m t^m/m! <=(eCt/d)^m. The final iterated remainder is at most
this factor times the common rho1 difference bound and tends to zero on [0,T].
The same estimates for the initial and forcing terms give

 |w(t)|_rho0 <= [|w(0)|_rho1+T sup_(s<=T)|R(s)|_rho1]
                                      /[1-eCT/d].          (8)

This argument works for time-dependent linearized coefficients; the simplex
volume is t^m/m!, with operator order retained. With zero initial difference
and zero source it gives uniqueness in this bounded analytic class. Thus every
subsequence above has the same limit. It is not a stability statement in an
unweighted finite Sobolev norm.

## 6. Exponential consistency and convergence

I_J is the actual sampling homomorphism: local products and analytic matrix
functions commute with it exactly while their series converge. A derivative
is the only failed operation. For delta=rho-rho'>0,

 |(D_J I_J-I_J partial_j)f|_rho'
       <=4/(e delta) exp[-delta(J+1)/2] |f|_rho.             (9)

The difference of representatives vanishes on Q_J. Outside Q_J,
|k|_1>=J+1 and |wrap(k)_j-k_j|<=2|k|_1. Bound
2|k|_1 exp(-delta|k|_1)<=4/(e delta) exp(-delta|k|_1/2)
to obtain (9). There is no discarded high-mode variational direction here.

Set rho2=3sigma0/4 and delta=rho2-rho1=sigma0/4. The consistency source
R_J=F_J(I_J U)-I_J F(U) is a finite sum of P_l(I_J U) times the commutator
(9) applied to Q_l(U). Bounds m_P,m_Q at rho2 thus give
|R_J|_rho1<=K_R exp[-sigma0(J+1)/8] with
K_R=4 sum_l m_P m_Q/(e delta).
Initial g,p samples agree exactly; initial q,r differ from samples of their
continuum values by the same derivative commutator. Hence the initial
augmented difference is bounded by K_0 times that exponential, where
K_0=4[|h0|_rho2+|B(g0)-I|_rho2]/(e delta) suffices.

The compared sampled continuum trajectory may have q!=D_J g; that is harmless:
(1) is defined on the whole augmented ball, and its sampling defect is exactly
R_J. The actual finite trajectory is consistent. Apply (8) to get

 |U_J(t)-I_J U(t)|_rho0
       <=2(K_0+T K_R) exp[-sigma0(J+1)/8].                  (10)

This is an estimate against actual samples. Interpolant convergence to the
continuum function adds its exponentially bounded Fourier sampling tail.
The rate above is conservative and uniform in J; it is not asserted optimal.

## 7. Constraint propagation and its actual finite meaning

On the consistent augmented state, the actual finite densities are

 C_J=T-K B^ij[D_k Gamma^k_ij-D_j Gamma^k_ik
                         +Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik],
 J_(J),k=pi^ij q_k,ij-2 D_j(g_ik pi^ij).                    (11)

The second formula follows by exact finite summation by parts in G[X], so it
contains all three momentum components. These expressions have at most one
D acting on a local analytic map of U. They consequently have a scale
Lipschitz bound between rho0 and sigma0/8 and a sampling-consistency bound
of the form (9). Combining these with (10) bounds their difference from the
sampled continuum densities by C_constraint exp[-sigma0(J+1)/8], where the
same finite majorant rules determine C_constraint.

The complete continuum algebra was derived in spectral-nonlinear-route, with
a separate root check of sign, matrix pairing, scalar-density covariance and
field-dependent shifts. In vacuum at unit lapse/zero shift it gives directly

 Jdot_i=0,  Cdot=partial_j(aK g^ij J_i).                    (12)

Indeed {G[X],C[1]}=C[X.partial1]=0 and
{C[N],C[1]}=-G[aK g^-1 dN]. Arbitrary fixed analytic smearings separate the
analytic densities. Thus initially zero continuum constraints stay zero,
proving the claimed finite constraint-error bound from (11). This is not an
exact finite constraint ideal. It allows a small finite initial sampling
defect, accounts for later band growth, and does not restore full-zone closure.

## 8. Diagnostic and unresolved physics

The companion axial script uses a reflection-invariant diagnostic of the
full system: x dependence only and diagonal g,pi. Reflection of either
transverse coordinate reverses the corresponding off-diagonal tensor entries;
Hamiltonian invariance and uniqueness force those initially zero entries to
remain zero. Translation in transverse coordinates preserves x dependence.
Thus the six diagonal coordinate/momentum functions obey the actual full
Hamiltonian restriction, while the off-diagonal variations vanish by symmetry.
The original diagonal Christoffel expression and the independently varied
summation-by-parts formula are compared by a direct complex-step gradient.
A pulled-back Kasner solution provides an inhomogeneous analytic continuum
control; its coordinate stretch is separately supplied. Floating trajectories
are diagnostics only, and their chosen duration is not a certified value of(7).

The strongest gain, if independently confirmed, is a finite-time controlled
nonlinear escape beyond strict-band coefficient identities, including actual
constraint propagation error. It still imports analytic continuous initial
data, the spectral nonlocal law, unit lapse and a continuum comparison. It
neither obtains these from native M2/records nor couples the original walker
or identifies a record-energy source. It supplies no long-time/thermodynamic
phase theorem, stable generic numerical relativity algorithm, axiom amendment,
retained status, or completed TOE.
