# Original-law boundary layers for the fixed-coarse-field cut sea

Author unit, Astra/max, 29 October 2026. **The actual level-zero cut Haar
measure at every fixed real coarse field has uniform local boundary-layer
bounds, with a polynomial cost in the bare inverse coupling.** The proof
keeps all colours, all normalized S4-prime kernels and the original sources.
The bound survives the completion-good returned gas and arbitrary retained
failure weights whose complete readers avoid the integrated variables.

This is a bounded producer awaiting fresh independent review. It controls
thin boundaries of actual plaquette and root-path tests. It does not bound
the whole hard-cut complement, the boundary of the optimized completion
minimum, or a normalized complex-source logarithm. Four-dimensional continuum
existence and a physical continuum mass gap remain **OPEN**.

## 1. Exact reference, source radius and dependency boundary

Use d=4, SU(N), N>=2, D=N^2-1, odd L>=3, T>=2, u>=1 and fixed
0<kappa_-<=kappa<=kappa_+. Fine sites form the periodic torus of side LT;
blocks are LX+{-h,...,h}^4, h=(L-1)/2. Positive fine links carry probability
Haar. The HS norm is unnormalized, ||A||HS^2=Re tr(A*A). Put

    s(P)=1-Re tr(P)/N,
    Z_t(M)=int_SU(N) exp[t Re tr(W^-1 M)/N] dW,
    k_t(V;M)=exp[t Re tr(V^-1 M)/N]/Z_t(M),
    w_epsilon(U;V)=exp[-u sum_p (1+epsilon_p)s(U_p)]
                     product_c k_(kappa u)(V_c;M_c(U)).       (CC1)

M_c is the arithmetic mean of the actual 24 L^4 paired S4-prime words,
using the same coordinate permutation at both ends. Every word stays in the
two endpoint blocks and has length at most p_L=5L-4. The kernel coupling
does not change with epsilon. Formula CC1 equals H1/CB1: the common exp(-t)
in numerator and normalizer has only been canceled algebraically.

Let I(Q) be the n_l=4L^3(L-1) links with both endpoints in Q, and keep

    chi_Q=product_(p wholly inside Q) 1{||I-U_p||op<epsilon_1},
    chi=product_Q chi_Q,
    Z_cut^epsilon(V)=int chi w_epsilon dU.                  (CC2)

The cut epsilon_1 is not a source. A crossing link belongs to no I(Q) and
is read by no factor chi_Q. For real sources define the positive probability
law nu_cut^epsilon=chi w_epsilon dU/Z_cut^epsilon. The denominator is positive
for every real V: internal links close to I satisfy every interior cut, and
all remaining factors are strictly positive. It need not have a
volume-independent lower bound.

The boundary theorem first permits real |epsilon_p|<=R, where R is any
fixed finite number. To combine with the successful gas, use exactly H20c:

    |epsilon_p|<=rho+lambda/u,  rho<a/(4 n_P),
    a=epsilon_1^2/(4N),  n_P=6 n_l,
    a_eff=a-4 rho n_P>0,  lambda>=0 fixed,                  (CC3)

and u above H21a for its chosen support rate mu. This gives R=rho+lambda
in the estimates below. In particular rho can be fixed as u grows.
All H constants, its epsilon_loc restriction and its u threshold refer to
this SAME chosen epsilon_1; numerical constants for a larger cut are not
reused after imposing CC7.

The [SA packet](COVARIANT_SOURCE_ACTIVITY_ASTRA.md), frozen source
SHA-256 `da22fc28cff8f822426ccd0458959dc24668f3d8854848f8ff83dbcda9f2ba54`,
was still under independent review when this construction began. Its
selected-sector results are not premises of CC4-CC19 below. SA30-SA33 identify
the downstream problem. Their sufficient smallness condition
`A sigma p^3+A_src rho p^2<=1/4` does not supply CC3 at fixed rho when p grows.
No quadratic-source resummation is claimed here. The reviewed
[H source](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md) and
[H review](REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md) supply H23-H25 only for
the tilt in section 5. CB1-CB4 supply a comparison of conventions, not an
all-field nonlinear inverse. [Sea11-Sea16](SOURCE_SEA_CONSTRUCTION_ASTRA.md)
integrate V with its specified coarse reference; they are not used as
fixed-V estimates. [SOFTHARD R2](REVIEW_SOFTHARD_R2.md) also forbids returning
a next-level indicator while its entire next-level field is fixed.

## 2. Compact normalized kernels: a genuine local modulus

For a real differentiable path of fine links write A_e=dot U_e U_e^-1.
For each c let m_(c,e) be the mean number of occurrences of the unoriented
fine edge e in its paired words. A repeated or inverse occurrence is counted;
no cancellation is needed. Unitary telescoping gives

    ||dot M_c||op <= sum_e m_(c,e) ||A_e||HS.

Differentiate the actual compact normalizer, on its positive real domain:

    d log k_t(V;M)
      =t Re tr(V^-1 dot M)/N
         -t E_(M,t)[Re tr(W^-1 dot M)/N],
    |d log k_t| <=2t ||dot M||op.                           (CC4)

The expectation is under the normalized SU(N) tilt. This uses every colour
and remains valid at degenerate M, with no selected maximizer, polar chart
or large-t approximation. Omitting log Z_t would change the derivative.

Each fine link occurs in six Wilson plaquettes. All kernels reading I(Q)
have an endpoint in Q, so there are at most eight, and
`sum_c m_(c,e)<=8 p_L`. Thus the exact local density w_Q^epsilon of H2,
with every touched Wilson/source term and all adjacent kernels retained,
obeys, for real sources,

    |log w_Q(U)-log w_Q(U')|
       <= u b_Q sum_(e in I(Q)) dist_HS(U_e,U'_e),
    b_Q=6(1+R)+16 kappa_+ p_L.                             (CC5)

Join coordinates successively by shortest group geodesics to integrate CC4.
The bound is uniform in every frozen fine link and every real coarse V.

A crossing edge has a sharper exact incidence. The only reading kernel is
the coarse link crossing that same face in that direction. Internal root
legs cannot cross the face. Of the L^4 offsets, precisely L have the three
specified transverse coordinates, and all 24 permutations contribute.
Every such word uses the edge once. Hence m=L^-3 and

    b_cross=6(1+R)+2 kappa_+ L^-3.                         (CC6)

This remains true across periodic faces at T=2: the lifted endpoint brick
uses its specified face, not the additional far seam of its induced torus
vertex graph. Other kernels and source-only factors are independent of this
edge and cancel in its conditional law only for that stated reason.

## 3. Simultaneous interior-cut caps in the original links

This is the new geometric step needed when interior links are integrated.
A cap about a single fixed flat configuration would give an exponential
energy comparison. We instead construct a cap close to EVERY admissible
configuration, including maximizers on the cut boundary.

Set A_L^int=3(L-1)/2=:A, and choose the actual H3 cut within the additional
explicit ceiling

    0<epsilon_1<=epsilon_*=
      min{1/4, 1/(32A), 1/(384 A^2), pi/(8NA)}.             (CC7)

H3 permits such a later chart ceiling. No claim here applies to a larger
preassigned epsilon_1 without another domain argument. The crossing-edge
result does not require CC7.

For an internal-link configuration U with all closed cut inequalities,
let Gamma_x be the rooted path taking coordinates in order 1,2,3,4. Its
union is the complete axial tree. Define g_x=U(Gamma_x), g_root=I, and

    W_(x,mu)=g_x U_(x,mu) g_(x+mu)^-1.

Tree links are I. An off-tree edge loop is filled by moving its single mu
step through the later-coordinate suffix of Gamma_x. Adjacent steps in
different directions exchange by one conjugated plaquette holonomy. There
are at most `sum_(nu>mu)|x_nu-LX_nu|<=3h=A` exchanges. Signed steps use
inverse plaquettes; all exchanged rectangles remain inside Q. Telescoping
the exact products of unitary conjugates gives

    ||I-W_e||op<=A epsilon_1,
    W_e=exp(a_e), a_e in su(N),
    ||a_e||op<=2A epsilon_1,
    ||a_e||HS<=2 sqrt(N) A epsilon_1.                      (CC8)

CC7 keeps the principal logarithm injective and traceless: the sum of its
eigenangles is a multiple of 2pi of absolute value less than 2pi. This
excludes the central-log branch issue for N>=3. This is an exact nonabelian
filling; no commuting Stokes formula was substituted.

Keep this particular g fixed and replace W_e by exp(t a_e), 0<=t<=1, on
every internal edge (a_e=0 on the tree). For any actual interior plaquette
put F_p(t)=log product_(its four oriented edges) exp(+-t a_e). With
s_p<=8A epsilon_1<=1/4, its product P(t) satisfies
`||P-I||op<=s_p`, `||P'||op<=s_p`, `||P''||op<=s_p^2` on the real segment.
The convergent matrix logarithm series gives
`||D log||<=1/(1-s_p)` and `||D^2 log||<=1/(1-s_p)^2`. Therefore

    ||F_p''(t)||op<=6 s_p^2<=384 A^2 epsilon_1^2,
    ||F_p(t)-tF_p(1)||op
                    <=192 A^2 epsilon_1^2 t(1-t).          (CC9)

The second bound is the elementary Dirichlet Green-function estimate for
the second derivative on [0,1]; its kernel has integral t(1-t)/2.
Let theta_1=2 arcsin(epsilon_1/2). The original cut says
`||F_p(1)||op<=theta_1`. By CC7 the error coefficient in CC9 is at most
theta_1/2, whence simultaneously for EVERY interior plaquette

    ||F_p(t)||op<=theta_1-theta_1(1-t)/2,
    ||I-P(t)||op<=epsilon_1-epsilon_1(1-t)/4.              (CC10)

The last step uses the exact relation 2sin(||log P||op/2) and
cos(theta_1/2)>=1/2. A tree order was chosen to prove the bound; the bound
is unchanged by unitary vertex gauges and holds for every block orientation.

Take 0<r<=epsilon_1/64 and t=1-32r/epsilon_1. Transform the contracted
links back by the SAME g, obtaining U^r. Then

    dist_HS(U_e,U_e^r)<=64 sqrt(N) A r,
    max_(interior p)||I-U_p^r||op<=epsilon_1-8r.            (CC11)

Every original-link product ball `dist_HS(U'_e,U_e^r)<r` lies in chi_Q=1:
each four-link word changes by at most 4r in operator norm. The ball is a
product of ordinary translated SU(N) Haar balls, including the tree links.
Thus no gauge variable is deleted and no gauge Jacobian is assumed. The
tree transform only constructs a centre. We never change variables in w_Q
or transform the frozen crossing links/coarse field. If one did parameterize
the tree separately, the familiar triangular Haar Jacobian is one, but that
identity is not needed for CC11 or the following volume calculation.

For completeness the single-group cap estimate is elementary. In an HS
orthonormal su(N) chart, `dHaar(exp a)=h_N j_N(a) da`, with h_N the
probability-Haar density at zero. The left-translated derivative of exp is
`X -> int_0^1 exp(-s a) X exp(s a) ds`. On a Cartan direction its determinant
is one; each real root two-plane contributes
`[sin((theta_i-theta_j)/2)/((theta_i-theta_j)/2)]^2`, where i theta_i are
the eigenvalues of a. Their product is j_N. Thus for
`r_H=min(1,pi/(2sqrt(N)))` and ||a||HS<=r_H it lies between
`[sin(r_H)/r_H]^(N(N-1))` and one. Define the explicit positive constant
`c_H=h_N [sin(r_H)/r_H]^(N(N-1)) vol_D(B_HS(1))`.
Translation invariance
then gives Haar(B_HS(W,r))>=c_H r^D for 0<r<=r_H. This keeps the full
D-dimensional Haar factor; there is no one-colour or flat-coordinate law.

## 4. Actual conditional-density and boundary theorems

Set r_0=min(epsilon_1/64,r_H/2), P_Q=D n_l, and

    C_Q= exp[b_Q n_l(64 sqrt(N) A+1) r_0]
                    (c_H r_0^D)^(-n_l).                  (CC12)

Fix every fine link outside I(Q) and all V. The conditional law under
nu_cut^epsilon is exactly `chi_Q w_Q^epsilon/D_Q^epsilon` with respect to
product Haar on I(Q). Other interior cuts are independent of these variables.
Choose a maximizer Umax of w_Q on the compact closed cut set. Its distance
to the cap in CC11, with r=r_0/(1+u), and CC5 imply

    D_Q^epsilon >=w_Q(Umax)
       exp[-b_Q n_l(64 sqrt(N)A+1)r_0] (c_H r_0^D)^(n_l)
                                            (1+u)^(-P_Q).

Consequently the actual conditional density satisfies

    d nu_cut^epsilon(U_I(Q)|U_out,V)/dHaar(U_I(Q))
                              <= C_Q(1+u)^P_Q.             (CC13)

This is a local polynomial with a large but fixed degree. It is uniform
in T, V, arbitrary real exterior data and all the real sources in CC3.
There is no division by Z_sec or lower estimate on the global Z_cut.

For a crossing edge, no cut restricts its variable. A cap about a maximizer
and CC6 directly give, with r_c=min(1,r_H/2),

    C_e=exp(b_cross r_c)/(c_H r_c^D),
    d nu_cut^epsilon(U_e|U_others,V)/dHaar(U_e)
                              <= C_e(1+u)^D.               (CC14)

The conditional law is legitimate even if the prescribed exterior does
not satisfy other cuts: CC13/CC14 can be defined by the positive local
denominator for all data; the global conditional statement is only needed
almost everywhere under nu_cut. Impossible outside histories retain zero
mass and are never divided by their mass.

Here is a full-colour Haar shell estimate. Choose
`delta_H=min(1,2sin(pi/(4N)))`. For 0<=tau, 0<eta and tau+eta<=delta_H,
Haar invariance and the traceless principal-log chart imply

    Haar{W: | ||I-W||op-tau |<=eta}
                         <= C_shell eta(tau+eta)^(D-1).   (CC15)

Indeed in a=log W coordinates the set lies between the two op-norm balls
of radii theta((tau-eta)_+) and theta(tau+eta), theta(x)=2arcsin(x/2).
Their Euclidean volumes are `v_op theta^D`, because the op-norm unit ball
in the REAL D-dimensional su(N) is homogeneous. On this compact chart
j_N<=j_+, theta(x)<=2x and theta'(x)<=2. For example
`C_shell=2^(D+2) D h_N j_+ v_op` suffices, including tau<eta. This proof
does not assume a differentiable operator norm or a regular eigenvalue.

An actual plaquette word contains any of its four fine edges once. The
straight root path S_c(U) contains its crossing edge once. After all other
variables in a word are fixed, the holonomy or mismatch is A U_e^(+-1) B
with A,B in SU(N), so its Haar shell is exactly of the form CC15.

For each elementary test alpha choose a witness integration set B_alpha:
a crossing edge if the word has one; otherwise I(Q) containing an edge of
its interior plaquette. Write (C_alpha,P_alpha)=(C_e,D) or (C_Q,P_Q).
Under the ORIGINAL fixed-V cut law,

    nu_cut^epsilon{ |f_alpha(U,V)-tau_alpha|<=eta }
       <= min{1,C_alpha C_shell(1+u)^P_alpha
                                      eta(tau_alpha+eta)^(D-1)},
    f_p=||I-U_p||op,   f_c=||V_c-S_c(U)||op.                (CC16)

For I(Q), integrate first the one edge in the product Haar shell and then
the other n_l-1 Haar variables; chi_Q<=1. CC13 supplies the density bound.
For crossing edges use CC14. This is a bound on strong-good plaquette and
ROOT-PATH faces, not a replacement of the latter by interior cuts. It covers
every actual fine plaquette, including seams, and every actual straight
coarse link. The elementary events are local; no law of V was invoked.

## 5. Returned gas, retained failures and exact complex envelopes

Fix a failure collection F from H13-H14. At real sources all H integrands
are positive, D_Y^0>0, and

    t_Y^epsilon=exp(delta S_Y(U)) N_Y^epsilon/D_Y^0>=0,
    a_Y^epsilon=h_Y t_Y^epsilon>=0,
    f_Y^epsilon=(1-h_Y)t_Y^epsilon>=0.

The ACTUAL finite hard-core gas G_ret,F is a sum of products of a_Y with
coefficient one and includes its empty product. Hence G_ret,F>=1; positivity
is not inferred from a formal complex logarithm. H23-H25 additionally give

    log G_ret,F^epsilon=sum_X V_X^F(epsilon;U_X,V_X),
    sup_x sum_(X contains x) exp(mu|X|) sup|V_X^F|<=d_q.    (CC17)

The terms are real at real sources. Their supports X are the COMPLETE
connected unions of H collars A(Y)=N_1(Y), not Y alone. If the integrated
variables B have endpoint blocks K_B, changing only B changes only terms
whose support intersects K_B. Thus the oscillation of log G is at most
2|K_B|d_q. Neither differentiability of h_Y nor locality in whitened
coordinates is needed. Multiplying any positive reference conditional law
by this positive gas and normalizing costs at most exp(2|K_B|d_q).

Let A_F=union_(Y in F) A(Y), R_F^epsilon=product_(Y in F)f_Y^epsilon, and
let R_out>=0 be any bounded measurable source-independent insertion
independent of B. If K_B is
disjoint from A_F, R_F is also independent of B: H23 keeps the entire fine
reader in A(Y). Define the exact raw history integral

    Z_F^epsilon[E;R_out](V)
      =int chi w_epsilon R_F^epsilon G_ret,F^epsilon
                                          R_out 1_E dU.   (CC18)

For E equal to the whole domain and R_out=1, this is exactly the H14
history numerator, not a substitute reference. For other E, CC18 is a
SEA-SIDE insertion in that exact representation. It is not automatically
the original pre-return event inserted in Z_epsilon[Xi_F]: if E reads an
interior replaced by a successful polymer, H8 requires it inside the joint
replacement integral. No such identification is made here.
If its real total mass is positive it defines a conditional
history law; if zero, the next raw inequality is simply 0<=0. Applying
CC16 conditionally and then integrating the unchanged exterior proves

    Z_F^epsilon[E_alpha(eta);R_out]
      <= exp(2|K_B|d_q) C_alpha C_shell(1+u)^P_alpha
              eta(tau_alpha+eta)^(D-1) Z_F^epsilon[1;R_out]. (CC19)

Here epsilon is real in CC3, |K_B|=1 for an interior block and <=2 for a
crossing edge. This includes arbitrary hard correlations in the exterior.
It does NOT condition on arbitrary hard events reading B. In particular,
an interior failure collar cannot be declared an independent hole, and
CC19 has not priced f_Y itself.

There is also an exact complex envelope, useful without claiming a complex
probability. Let epsilon be complex in the SAME CC3 polydisc and e=Re epsilon.
The original positive Haar integrals give, pointwise in real U,V,

    |N_Y^epsilon|<=N_Y^e,
    |t_Y^epsilon|<=t_Y^e,
    |a_Y^epsilon|<=a_Y^e, |f_Y^epsilon|<=f_Y^e,
    |G_ret,F^epsilon|<=G_ret,F^e,
    |w_epsilon|=w_e.                                      (CC20)

The source compensator exp(delta S_Y) is retained in the second line;
its modulus is exactly exp(delta S_Y^e). The gas inequality follows from
its actual finite polynomial, before any logarithm. Therefore CC19 implies

    |Z_F^epsilon[E_alpha(eta);R_out]|
      <= Z_F^e[E_alpha(eta);R_out]
      <= B_alpha(u,eta) Z_F^e[1;R_out],                    (CC21)

with precisely the displayed CC19 B_alpha and the same collar exception.
At fixed finite volume these raw integrals are entire in the original
Wilson coefficients; the real hard domains are independent of them. The
bound is relative to the ACTUAL positive real-source history mass. It does
not bound division by Z_F^epsilon or Z_cut^epsilon, nor prove either is
nonzero on a volume-uniform complex domain. Replacing the real envelope by
Z_F^0 incurs a source cost that has not been silently discarded.

All vacuum factors remain in CC18-CC21. For example at any fixed reference
Ustar the exact local identity is
`exp(-u sum epsilon_p s(Ustar_p))` times the integral of
`exp(-u sum epsilon_p[s(U_p)-s(Ustar_p)])` against the unchanged baseline.
The prefactor is not one. No source-only exterior term, Haar factor, finite-u
normalizer, or Gaussian determinant from a chart has been removed. There
is no Gaussian chart or determinant in this original-Haar theorem.

## 6. What this bounds in a hard localization, with actual support SIZE

Let S be a finite collection of the elementary tests in CC16 and let H be
any product of their good/bad indicators. If approximate REAL scalar tests
f_alpha^loc satisfy `|f_alpha^loc-f_alpha|<=eta_alpha` on the whole measured
domain, then the exact deterministic inclusion is

    |H_loc-H|<=sum_(alpha in S)
                     1{|f_alpha-tau_alpha|<=eta_alpha}.   (CC22)

Thus CC16, or CC19/CC21 with its stated witness/collar restrictions, controls
the L1 error by the sum of the corresponding B_alpha. For holonomy
approximations, operator-norm word error gives the scalar error by the
reverse triangle inequality. This is an integrated statement. The
supremum error of the two hard indicators can still be one for every eta>0.

The original local conditional w_Q reads P(Q), C(Q) and their full contour
links inside N_1(Q), at most81 original blocks. It reads at most n_P original
source coordinates. A crossing conditional reads its six plaquettes and its
one complete two-block kernel, all in N_1 of its two endpoint blocks (at
most162 blocks). The shell words themselves read their actual links and
coarse V. For a family S, take the UNION of these readers; do not count
overlaps as independent variables. If there are m witness blocks/edges, a
safe reader size is 162m blocks. CC22 costs the number of tests, explicitly;
for an entire volume that number is extensive. It is not replaced by one.

H24's tilt uses connected support SIZE in original L^4-site blocks. Its
local oscillation cost is controlled by |K_B| because those full readers
were already in X. In contrast, if f^loc uses a radius-R ball, the new
reader may contain O(R^4) blocks. An error e^(-mR), even after multiplication
by a fixed polynomial in u, does not pay exp(beta R^4). CC22 supplies no
connected-support cluster coefficient or forest argument. Nor may its
reference be replaced by nu_cut conditioned on SA's global Omega: that
conditioning reads all variables and can cost Z_cut/Z_sec, precisely the
uncontrolled ratio we avoided.

The optimized h_Y in H12 is the indicator of a minimum over an interior
completion, involving a MAX of collar curvatures plus a MAX of root-path
mismatches. It is neither an individual translated group word nor a product
of the elementary tests. CC15 therefore does not establish its boundary
anti-concentration. The hard h_Y is used only as a bounded local factor
inside the already reviewed H gas, or as an exterior failure factor.

For comparison, a useful pointwise identity retains both path variance and
alignment. With normalized HS norm, positive weights sum w_a=1, P_a in
SU(N), M=sum w_a P_a, m=max_G Re tr(G^-1 M)/N, put
v=sum w_a||P_a-M||_nHS^2=1-||M||_nHS^2 and
psi(V)=m-Re tr(V^-1 M)/N. Averaging the competitors P_a gives
`m>=||M||_nHS^2`; Cauchy gives `m<=||M||_nHS<=1`. Consequently

    v/2<=1-m<=v,
    v+2psi(V)<=sum_a w_a||P_a-V||_nHS^2<=2v+2psi(V).       (CC23)

If every P_a differs from an actual anchor S by a product of conjugated
plaquettes in a specified filling, exact unitary telescoping controls that
difference and hence v. This rebuilds the elementary variance/alignment
observation in the actual full-colour normalization. It does not supply a
normalization relative to Z_sec, abundance estimates for bad fillings, or a
localized return theorem. CC13's cap near each admissible configuration,
rather than CC23 alone, is what produces the new conditional measure bound.

## 7. Literature, evidence and the remaining interface

Balaban's local gauge constructions and Dimock's exposition inform the
tree and localization architecture. In [Dimock, arXiv:1410.2798v3](https://arxiv.org/html/1410.2798v3),
section 2.1 equations (4)-(11) and section 2.2 through Proposition 1 concern
abelian tree/averaged axial gauges, mainly d=3. They do not give this
nonabelian cut-domain cap or conditional law; CC8-CC15 rebuild the required
finite-dimensional statements. [Balaban, CMP116 (1988), pp1-2](https://doi.org/10.1007/BF01239022)
separates localization of the fluctuation action from exponentiation. The
original scanned introduction was read; no unread body theorem is imported.
[Dimock's large-field paper](https://arxiv.org/html/1212.5562v2) is a scalar
three-dimensional construction. Its holes/cluster machinery requires a
localized independent fluctuation representation and small interactions;
the original cut sea here has not acquired those hypotheses. These are
attributed comparisons, not imported Yang-Mills estimates. The existing
[literature register](LITERATURE_BRIDGES.md) and
[import register](ASSUMPTIONS_AND_IMPORTS.md) retain that distinction.

The [numerical criteria](checks/covariant_complement_criteria.md) precede
the new checker. Actual noncommuting SU(2)/SU(3) four-dimensional blocks,
paired words and a full-SU(2) Haar conditional integral are used only to
falsify normalization, gauge, sign and boundary claims. No finite test
proves the arbitrary-volume inequalities. The
[first completed run](checks/covariant_complement_01_results.json) is
**23/24**, including six detected mutations. Its source and full
[stdout](checks/covariant_complement_02_output.txt) are unchanged. At u=40
the shell widths .015 and .0075 gave mass ratio 2.463807379, outside the
prospective [1.85,2.15] interval. This disproves that auxiliary finite-width
expectation; CC16 only bounds the mass ABOVE by a u-dependent constant
times the width, and asserts no such ratio. The separately registered
[post-hoc narrower-shell probe](checks/covariant_complement_posthoc_criteria.md)
gave ratios 2.028365892 and 2.007083710, with its
[three predicates passing](checks/covariant_complement_posthoc_results.json).
It does not retroactively pass the first criterion or prove the uniform bound.

The actual open L=3 blocks have 216 links, 80 tree links and 216 interior
plaquettes. Both SU(2) and SU(3) recovered their large vertex gauges to
less than 5e-15 matrix error and retained every predicted cap margin.
Contracting ungauged principal logs instead created plaquette defect .1990
at a cut .00028935. Enumeration of all 64 coarse-link labels on T=2 gives
exactly one crossing reader, 72/1944=1/27. Direct noncommuting words agree
with the specialized six-plaquette action and kernel mean to 7e-14. Full
SU(2) Haar sphere integration agrees with analytic angular integration to
2e-14 relative error. Dropping the normalizer, full Haar measure, curved
plaquette or source vacuum changes the tested quantities. In particular
the exact source partition ratio .93886118 includes vacuum factor .94444227;
omitting it gives .99409060. These are non-interval finite diagnostics.
The epsilon=.1 fixture tests the unrestricted real-source conditional
theorem; it is not a numerical test of H24's much smaller successful-gas
radius or of a whole block/sea integral.

An earlier launcher failed before executing the mathematical program:
Darwin rejected the requested RLIMIT_RSS setting. Its
[stderr](checks/covariant_complement_01_stderr.txt) and passed resource gate
are retained. The replacement launcher kept the >=50% free-memory gate,
nice15, one numerical-library thread, a 90-second CPU/wall limit, and an
external 300 MiB RSS watchdog. The completed main run used about64 MiB
and the post-hoc run about53 MiB. Neither reached a resource limit.
The [read manifest](checks/covariant_complement_read_manifest.json) and
[receipt](checks/covariant_complement_receipt.json) bind the complete
owned packet, actual coverage and unchanged dependency bytes.

The next obligation is still the normalized source-sensitive integration
of the full H14 history sum, or equivalently a correctly matched estimate
for SA33's `log(1+B_comp)` on its required domain. CC19-CC22 give a genuine
original-law boundary producer away from retained failure readers. They do
not bound G\Omega, G^c, the entire optimized completion boundary, or the
change from nu_cut to the selected-sector reference. The fixed-rho complex
logarithm, support-size localization after whitening, failed-history costs,
higher-level action/source return, and nonlinear RG remain separate missing
steps. No covariance gap, Haar cap, or polynomial boundary bound is a
physical continuum mass gap.

In particular this does not discharge PLD9.4's (SC)_k, the actual normalized
sea logarithm, or LARGE55 I3/I5 with its E13/E14 corrections. The latter
requires a reference-region price and permits a small boundary cost; it
does not follow by calling a positive conditional denominator normalized.
HIST's joint-return variables at lines282-286 integrate the next-level
interiors. The fixed-V law here integrates the CURRENT fine links and
cannot perform that different return.

Process: [PROCESS_LIGHT](PROCESS_LIGHT.md) applies. Earlier current-main
methodology at ca2bc7ddf64790da96cd43d42017d000fbfe4808 is reused at its recorded
scope; stale local main is not authority. The coordinator owns the campaign
lock, Git/publication and independent review. This unit changes only this
source and checks/covariant_complement_*; all predecessor packets remain
immutable. No audit or whole-PR status is assigned.
