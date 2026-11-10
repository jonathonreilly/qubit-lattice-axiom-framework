# Actual seven-edge marginal: frozen Gaussian producers

Author derivation, 2026-11-09; independent checking pending. Conditional
finite-model mathematics at assigned revision
`c0497327ec81143f6f8b5369c86583ad3387d785`. The supplied compact seven-edge
coercivity constant is a premise; its ancestry is not recertified here.
This establishes Gaussian and base-vertex producers, not the compact insertion
identity, its activity bound, or a full compact response theorem.

## 1. Exact law, stationary origin, and uniform precision

Fix odd L>=3, kappa>0, m>=3 and u>=1. J is the seven-edge union of two
adjacent distinct terminal plaquettes, O its complement, V_O=I. Use any
permitted terminal-root fine forest, retaining all non-tree fine links and
all intermediate links. The cell lattice is the four-dimensional m-torus. Throughout this note,
d is its periodic axial nearest-neighbor (l1) graph distance, so a shortest
axial path has exactly d edges. A reader-range bound supplied in periodic
l-infinity distance is converted to this metric by enlarging the range R
by at most a factor of four. The bound (2t+1)^4 still bounds l1 balls,
since every such ball lies in the corresponding l-infinity ball.
Put n=m^4(3L^8+1+4L^4), q=3n, k=3(3L^8+1+4L^4), sigma=u^(-1/2),
t=kappa u. Coordinates are U_e=exp(i a_e dot sigma_Pauli). Write

 Z(s)=integral exp(s w(Q))dQ, h(s)=log Z(s)-s, j(a)=(sin|a|/|a|)^2,
 Q_J=integral q_u K0 product_(c in O) k1,c(I|U1)dU0 dU1,
 q_u=Z_fine(u)^(-1)exp(-u W0),
 E_J=W0+kappa sum_(all level-0 c)(r_0,c-<U1,c,M0,c>)
          +kappa sum_(c in O)(r_1,c-<I,M1,c>).

The exact negative logarithm of the normalized quotient chart density is

 S_J(a)=log Q_J+log Z_fine(u)+n log(2pi^2)+u E_J(a)
       +sum_(all level-0 c)h(t r_0,c(a))
       +sum_(c in O)h(t r_1,c(a))-sum_e log j(a_e).       (1)

The gauge quotient has product probability Haar; root-fixed orbit variables
integrate to one. No forest determinant remains. Equation (1) includes every
K0 and every surviving terminal radial normalizer. It describes the original
normalized marginal law in its chart, not a chart-normalized probability.

Every local term has zero differential at identity. For a mean, write its
linear path tangents p_gamma, qbar=sum alpha_gamma p_gamma and
v_path=sum alpha_gamma|p_gamma|^2-|qbar|^2. Then
r=1-epsilon^2 v_path/2+O(epsilon^3), and its mismatch is
epsilon^2|b-qbar|^2/2+O(epsilon^3). Wilson and Haar terms also have zero
linear part. This proves DS_J(0)=0 for the actual nonperiodic coefficient
pattern; stationarity uses neither identical internal trees nor translation
symmetry. Equivalently each scalar local factor is conjugation invariant,
whose differential at the fixed origin has no SO(3)-invariant linear part.

Let B=Z'/Z, eta_u=kappa(1-B(t)), and V0,V1,O be the sums of these
path-variance forms. Direct differentiation of (1) gives exactly

 H:=u^(-1)D^2 S_J(0)=H_E,J+eta_u diag(V0,V1,O)+(2/(3u))I,
 <a,H_E,J a>=||d0 a0||^2+kappa||a1-Q0 a0||^2
                             +kappa||P_O Q1 a1||^2.     (2)

Symmetry w -> -w and w<=1 imply 0<=B(t)<=1. The supplied compact bound
E_J>=c_J sum_e(1-w(U_e)), expanded at identity, proves H_E,J>=c_J I.
Thus there are constants g=c_J>0, M,K_H<infinity and integer R>=1,
depending only on L,kappa, with

 g I<=H<=M I,  sup_i sum_j |H_ij|<=K_H,
 H_ij=0 when d(X(i),X(j))>R.                            (3)

For the upper/row/range bounds, each factor has bounded reader arity and
bounded anchor incidence; all path lengths are <=5L-4. Its divided Hessian
at identity is bounded because 0<=eta_u<=kappa. Fine-tree substitutions
only remove slots. For fixed L there are finitely many tree patterns and
periodic slot identifications, counted with multiplicities; taking their
maximum supplies uniform constants. This is the actual coefficient matrix,
not a full-terminal proxy. Equations (1)-(3) hold for every u>=1.

## 2. Exponential inverse, positive core, symmetric pinned paths

Choose M'>M, rho=1-g/M' in (0,1), gamma=-log(rho)/R. The Neumann
series C=H^(-1)=M'^(-1)sum_(l>=0)(I-H/M')^l gives

 |C_ij|<=g^(-1)rho^ceil(d(X(i),X(j))/R)
        <=g^(-1)exp[-gamma d(X(i),X(j))].               (4)

Indeed earlier powers have zero relevant cell block and each later power
has operator norm <=rho^l. The cell count at distance t is bounded by
(2t+1)^4 uniformly on the torus. Define
M_beta(A)=sup_i sum_j exp(beta d(X(i),X(j)))|A_ij|.
Fix 0<beta<gamma and an integer R0>=1. Set

 P_ij=C_ij 1_(d<=R0), E_ij=C_ij 1_(d>R0).

These are symmetric. Moreover

 M_beta(E)<=k/g sum_(t>R0)(2t+1)^4 exp[-(gamma-beta)t].   (5)

Since C>=M^(-1)I and ||E||<=M_0(E), choose R0 so that
M_0(E)<=1/(2M). Then P>=p0 I with p0=1/(2M), and
P<=U I with U=1/g+1/(2M). Positivity follows from this quantitative
perturbation, not from a general positivity property of truncation.

For EACH UNORDERED scalar pair {i,j}, choose one shortest nearest-neighbor
path between its owner cells, with a deterministic ordering and tie rule.
Assign that same CELL SET Gamma_ij to both directions. Its edge length is
d(X(i),X(j)), and its number of cells is d+1. Define

 e_ij=exp(beta |Gamma_ij|)|E_ij|,
 e=sup_i sum_j e_ij,
 B_pin=sup_x sum_(i,j:x in Gamma_ij)e_ij.

With |Gamma| denoting cell count, e<=exp(beta)M_beta(E). If x is on a
length-t path, both endpoints are in the t-ball of x, so

 B_pin<=exp(beta)k^2/g sum_(t>R0)(2t+1)^8
                                      exp[-(gamma-beta)t].       (6)

This counts ordered scalar endpoints and overcounts path congestion safely.
Thus e and B_pin can simultaneously be made as small as any prescribed
positive tolerance, in particular e<=p0/4, uniformly in u,m,trees and J.
No symmetric-path premise is hidden in an ordered tie-breaking rule.
E need not be positive and is never used as an independent covariance.
C,P,E are independent of source parameters and local fields.

Optional inverse control is also uniform: for any scalar subset I,
P[I]>=p0 I. For W_ii=exp(theta d(X(i),X_*)), row and column sums of
WP[I]W^(-1)-P[I] are bounded by

 A(theta)=k/g sum_(t>=0)(2t+1)^4 exp(-gamma t)(exp(theta t)-1).

Choose theta>0 so A(theta)<=p0/2. The inverse perturbation bound gives
|(P[I]^(-1))_ij|<=2p0^(-1)exp[-theta d(X(i),X(j))], and summing gives
uniform absolute row bounds, also independent of R0 once its gap holds.
The same proof with C[I]>=M^(-1)I controls principal covariance inverses
of C. None of these inverses equals a principal restriction of H in general:
Gaussian marginalization gives C[I], not (H[I])^(-1).

## 3. Complete-action vertices with whole-cell bodies

Fix A>5/2, p=[log(2+u)]^A and a=sigma x. There is a fixed u_dagger such
that for u>=u_dagger the scalar cube |a_i|<=sigma p lies inside the
supplied fixed identity chart, all path means satisfy r>=1/2, and sigma p^3
is as small as prescribed. This asymptotic statement is not claimed for
u=1: the Gaussian bounds above hold for all u>=1, whereas these shrinking-
chart producers use u>=u_dagger.

Decompose (1) into its coordinate-independent normalization and local
terms s_v: each u W_p, each COMPLETE surviving kernel
u kappa(r-<output,M>)+h(t r), and each -log j(a_e).
Keep every syntactic reader, including hidden outputs and radial readers.
Let T_v be a connected cell envelope of those readers, of uniformly bounded
size/diameter. Let D_v be the union of the complete owner-cell coordinate
bodies for the actual reader cells. This distinction keeps connecting
geometry separate from activated scalar coordinates.

On the fixed all-reader chart, the supplied moment argument proves
|h^(j)(s)|<=C_j(1+s)^(-j) for j=1,2,3. Each chain-rule term has
 t^j h^(j)(t r), bounded by C_j 2^j since r>=1/2. Word/radial derivatives
and arity are bounded there. Thus sup||D^3 s_v||<=C u, uniformly in v
and u>=1. This is a local chart bound only; no C3 estimate at M=0 is used.
Each Ds_v(0)=0. Set on its reader cube

 R_v(x)=s_v(sigma x)-s_v(0)-(sigma^2/2)D^2s_v(0)[x,x].

Integral Taylor remainder gives |R_v|<=C sigma p^3. Now define on the
ENTIRE real coordinate space

 W_v(x)=1_{all scalars in D_v have |x_i|<p}
                     [exp(-R_v(x))-1],                 (7)

interpreting the bracket only on that cube and setting the function to zero
elsewhere. Thus ||W_v||inf<=exp(C sigma p^3)-1<=C' sigma p^3.
Even if R_v ignores some scalars, (7) includes their cell-body indicators.
This is a bounded measurable extension; no cutoff differentiability is
asserted or needed. On Box_p, product_v(1+W_v)=exp[-sum_v R_v] exactly.
The quadratic sum is exactly x^T H x/2, including normalizers and Haar.

## 4. Four fixed normalized sources

Take X_1=F, X_2=G, X_3=A_c, X_4=A_d, where F,G are fixed bounded
local quotient observables with complete reader sets of fixed cardinality
and diameter. Choose positive ell_F>=||F||inf and ell_G>=||G||inf for
nonzero observables. For distinct c,d in O and fixed output tangent vectors
v_c,v_d at I, the scores of the ACTUAL marginal are

 A_c=kappa u <D V_c|_I,M1,c>,
 A_d=kappa u <D V_d|_I,M1,d>.

The radial normalizers do not depend on their output, so contribute no
score derivative; they remain in (1). Since |M|<=1 and |D V|=|v|,
choose ell_c=kappa u |v_c|, ell_d=kappa u |v_d|. Zero observables or zero
tangent vectors produce no vertex and zero associated mixed derivative.
For nonzero labels put f_l=X_l/ell_l, so ||f_l||inf<=1. The physical
source parameters t_l are related to normalized ones by zeta_l=ell_l t_l:
exp(sum t_l X_l)=exp(sum zeta_l f_l). No source changes the covariance.

For each nonconstant label let D_l contain every complete owner-cell body
of its actual syntactic readers, including quotient pullback readers where
present. Fix a connected envelope T_l of these cells. For |zeta_l|<r,

 W_l^src(x;zeta_l)=1_{Box_p on D_l}
                   [exp(zeta_l f_l(sigma x))-1],
 ||W_l^src||inf<=exp(r)-1<=exp(1)r, 0<r<=1.            (8)

This is bounded and holomorphic in zeta, requiring no field derivatives of
F,G. It is defined only by the actual quotient functions, with no integrated
orbit replacement. Its readers are whole cells even where the numerical
function happens to be constant in some coordinates. The source supports
and envelopes are independent of source values and positions up to the
uniform reader size/diameter hypothesis.

An observable with genuinely empty support is constant. Carry its coupling
in V_vac(zeta)=sum_(empty-support l) zeta_l f_l instead of a primitive.
The factor exp(V_vac) is retained in every physical integral. It is linear
in these source labels, hence contributes no mixed derivative of order >=2.
A constant with a deliberately retained nonempty syntactic reader can
instead be a priced vertex (8). These choices are not mixed or double counted.

## 5. Exact Gaussian identity, including normalization

Let K_surv=|E1|+|O|=4L^4m^4+4m^4-7. At identity all energies and Haar
logs vanish and every surviving r equals one. Therefore

 S_J(0)=log Q_J+log Z_fine(u)+n log(2pi^2)+K_surv h(t).

Set

 B_J(u)=exp[-S_J(0)] u^(-q/2)(2pi)^(q/2)(det H)^(-1/2)
       =[Q_J Z_fine(u)]^(-1)(2pi^2)^(-n) exp[-K_surv h(t)]
                    u^(-q/2)(2pi)^(q/2)(det H)^(-1/2).   (9)

If C=H^(-1) and gamma_C is its normalized real Gaussian, the exact
source-weighted chart integral of rho_J is

 integral_chart exp(sum_l t_l X_l) d rho_J
   =B_J(u) exp(V_vac(zeta))
       E_gamma_C[1_Box_p product_v(1+W_v)
                              product_l(1+W_l^src)].    (10)

All products over l exclude labels placed in V_vac. The proof is direct
substitution of (1), stationarity, the full local quadratic Taylor sum,
da=u^(-q/2)dx, and the Gaussian normalization
exp(-x^T H x/2)dx=(2pi)^(q/2)(det H)^(-1/2)d gamma_C.
This proves (10) for complex sources too, since its bounded-domain
integrands agree pointwise. For an unnormalized marginal numerator multiply
both sides by Q_J, and change nothing else. For a chart-conditioned
expectation divide (10) by its own zero-source chart integral. Neither
operation discards Z_fine, Haar constants, h(t), Jacobian or determinant.
No lower bound on a full-volume chart probability is being assumed.
The constant B_J is source independent. No claim here extends (10) to the
compact complement without an exact insertion representation.

## 6. Verification of the forest base contract

Use the notation of zero-shift-marked-density-forest.md (F1)-(F6), taking
its B to be B_pin of (6), and its k as above. Fix R0 once using (5)-(6)
so e<=p0/4 and B_pin is a finite prescribed bound. Equations (3)-(6)
prove (F1)-(F2), including the required symmetric path sets. Its constants
c=p0/2, G=U+p0, a=1/G, b=1/c, D0=b^2/a+b/2,
L_f=max(1,sqrt(2 exp(1)D0)), K_g=max(1,sqrt(4/(a c)))
are finite and independent of u, volume, source positions and trees.
Here L_f is the forest constant, not the blocking integer L.

For an action or source vertex choose S_o=N_R0(T_o); for a bad cell X
choose S_bad=N_R0({X}). These bases are connected, nonempty, include all
activated and source readers, and are of uniformly bounded size. Disjoint
bases imply no cross P entry, because the reader distance then exceeds
R0. The whole-cell extensions (7)-(8) implement precisely the vertex
part of (F3) and its activation convention. With no compact labels, (10)
is the exact physical realization of Z_a. For proposed compact labels,
(F3)'s Z_* matching is an additional obligation, not a consequence of (10).

There are uniformly bounded numbers of action anchors within a fixed
radius of any cell and a fixed number of readers per anchor. Consequently
for fixed R0,beta,K_g there are constants C_weak,C_bad,C_src such that
the (F5)-(F6) positive sums obey

 h_weak<=C_weak sigma p^3,
 h_bad<=C_bad exp[-a p^2/8],
 h_src<=C_src r,  0<r<=1.                               (11)

For example each action term contributes at most
exp(beta |S_v|) K_g^(k |reader_cells(v)|) C' sigma p^3;
the finite anchor incidence bounds the sum through a marked cell. Bad
cells have the corresponding fixed collar count and K_g^k. There are at
most four source vertices, each with fixed bounded reader and base size,
so even coincident source positions obey the same C_src. The K_g factors
pay for all body coordinates, including unused scalar components. Empty-
support constants are priced separately in V_vac, not given zero cost in
this rooted norm. This establishes (F4)-(F6) for the base families.

Since sigma p^3 tends to zero and p tends to infinity,
h_weak+h_bad ->0 uniformly. Choose the forest threshold H_f>0 determined
by beta,k,L_f,e,B_pin, then choose r small enough that C_src r<=H_f/4
and u large enough that h_weak+h_bad<=H_f/4. Thus
h_base=h_weak+h_bad+h_src<=H_f/2 is met uniformly. This is the base half
of (F7), not its compact half. The unverified h_comp<=H_f/2 and the
exact compact insertion match remain outside this assignment. In
particular this note does not invoke the forest conclusion for the actual
full compact law by silently assuming those two premises.

## 7. Source coverage and recovery

The following five mathematical sources were read in full at this task's
snapshot. Paths are relative to this pack's `parts/` directory:

| Source | SHA-256 |
|---|---|
| marginal-nonlinear-chart-estimates.md | b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7 |
| marginal-normalized-regional-coercivity.md | bd3fa8b5eb989c7718ad5d760a913e33166f3e9edcf52b9f17f82cbd809ca255 |
| partial-terminal-normalizer-hessian.md | a17f372f928930bd9be6e81d68349a62232a027f17a13a7cd47e813f43584139 |
| frozen-gaussian-producers.md | ac4984909f5edbc5e79f9cb3ffd212862f43295d9a0537e0102fb4e38d0900c3 |
| zero-shift-marked-density-forest.md | d44adc900daf7ac665e502ac950230a8739b120d1a2be4940fd292ea9a09087f |

The first three supply the actual marginal action, compact-to-local gap and
uniform derivative estimates. The old Gaussian note supplies a method only;
its translated-tree/full-terminal law is not imported as this law's theorem.
The final note supplies the abstract contract; its later proof was also read,
but this assignment does not independently certify that forest theorem.
The parent's source instruction specifies mixed sources (F,G,A_c,A_d),
fixed bounded local quotient observables for F,G and distinct retained score
locations. Section 4 implements that instruction.

Repository operating sources read in full:

| Source | SHA-256 |
|---|---|
| AGENTS.md | 7def904fdd52d811e7aba87a0d3d859bfb017cccd59703125f4a53f2805aaab2 |
| docs/ai_methodology/SCIENCE_WORKFLOW.md | 1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca |
| docs/ai_methodology/skills/workhorse/SKILL.md | e3e3cea67ad1877e4e73e38c7d62f1561142a0dffc66abe991f2ad0250133ad8 |
| docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md | b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0 |

Parent attests these repo procedures match main
`bf92a1d763030836ed55631d5d7a7ef3b288f284`; no independent fetch was
performed under this bounded no-network assignment. Installed copies were
not used. Parent supplied preflight, science lease and the completed first
repo/literature search: the prior Gaussian/forest notes are closest;
APS/arXiv:0901.4756, Lohmann arXiv:1411.1107 and BKAR are methodological
comparators with differing analytic/interactions/insertion contracts, not
imported new-law theorems. This note relies on its displayed elementary
finite-matrix and Taylor arguments and on the pinned marginal suppliers.

Recovery checkpoint: (2) is the exact marginal Hessian; (5) preserves core
positivity by small norm; (6) bounds symmetric-path congestion; (7) retains
whole-cell bodies; (9)-(10) retain the entire physical prefactor; (11)
prices all base and mixed-source vertices. Only this assigned file was
written. No numerical job, Git mutation, network action, prompt edit,
audit/status action or subagent was used. All argument checks here are
author checks; the parent's decisive independent check is still required.
The only excluded downstream obligations are h_comp and the exact compact
insertion representation, and no success on either is presumed.
