# REALRGB — one real-derivative soft-kernel step, with a failed history and hole

**The uniform local RG step is OPEN.** Real positivity does close
nonvanishing, total variation one, and uniform *relative* fourth-derivative
bounds for the actual fixed-sector integrals. It also upgrades CHARGE's
filled-flux estimate to a small real fourth-jet estimate against the same
all-cut denominator, under explicit coupling/cut/source conditions.
It does not provide the local mixed-group smallness, selected-return
regularity, arbitrary-hole norm control, or extracted continuation needed
by the next step. These remaining issues already occur on real fields.

PROVEN means the mathematical assertion with its stated hypotheses below;
ARGUED means a proposed application; OPEN means an unmet actual-model
estimate. These are author statuses, not audit status or a Yang–Mills
existence/mass-gap claim. The supplied model is finite periodic SU(N),
N>=2, odd L>=3, probability Haar, and Decision 4's arithmetic contour mean.
No new physical axiom, kernel, or history convention is introduced.

Credit: Tadeusz Balaban for the large-field RG organization and Jonathan
Dimock for its exposition. No literature lemma or memory-only [m] assertion
carries weight here. The arguments used below are rebuilt, or explicitly
identified as conditional applications of the named local sources.
The source/read/check/review record is [REALRGB_LOG.md](REALRGB_LOG.md).

## 1. The actual step and the real norm

REALRGA.md was absent when this work began. The following is therefore an
explicit candidate norm, not an assertion of agreement with an unseen
parallel contract. The source window and the derivative weight are
different parameters.

Keep the original coefficient sources epsilon_p real, with
`|epsilon_p|<=rho`. All u_l and all RG kernels stay fixed under these
derivatives. Write each last output link as
`V_c=Vbar_c exp X_c`, with X_c anti-Hermitian traceless and
`||X_c||op<r_c`, for any fixed chart margin, for example r_c=1/4.
Take the supremum also over unitary Vbar. All earlier fields remain real
integration variables. For a direction v=(a,A), use original units:

    |v|_1 = sum_p |a_p| + sum_c ||A_c||op.
    |F|_(4,h) = sum_(m=0)^4 h^m/m! sup_(real domain) ||D^m F||_(1,...,1),
    ||K||_(mu,4,h) = sup_x sum_(X contains x) exp(mu |X|) |K_X|_(4,h).
                                                               (G1)

Here h>0 is a declared jet weight, mu>=0, and the multilinear operator
norm uses |v_i|_1<=1. The m=0 term is the value supremum. Derivatives at
closed source-window endpoints are defined on an open real neighbourhood;
the finite integrals below exist on every finite real source window.
The graph, connected supports, inactive roots, original source labels,
exterior readers and normalizer readers are exactly those of RD3/RD4.
No source is projected onto a new coarse shadow. Frozen local exterior
data eta are supremum parameters, **not differentiated** in the local
quotient theorem below. Their real differentiability is a separate issue.

Leibniz and `binom(m,l)/m!=1/(l!(m-l)!)` prove
`|FG|_(4,h)<=|F|_(4,h)|G|_(4,h)`: the truncated convolution is bounded
by the full product of two nonnegative sums. Triangle inequality and
termwise differentiation therefore extend the fixed-mask LIB1 resummation
to (G1). This does not assert any actual input activity bound.
An l-infinity norm on perturbations would introduce the number of source
or output coordinates in the estimates below. G1 bounds every labelled
mixed derivative, but provides no sum or decay in the derivative labels
without the separate full-support estimate. Four derivatives suffice for
the finite matching jets discussed by REALONLY; they do not imply the
all-order distribution estimates of its section 4.

For the concrete failed history take RD3 D1: two adjacent bad level-zero
blocks Y_0, size cutoff n_0=1, interior cuts one, and a level-one block
torus of side T>=7. Its inactive set and tested return block are

    H_1={-1,0,1}^4, |H_1|=81,
    A_1=Gamma_1 minus H_1, B={v_*}, v_*=(2,0,0,0).        (G2)

All hole fields are retained. Let Xi_h be the **complete** old failure
record, including absence of other failures, and set

    rho_(1,h)^epsilon(U_1)=int Xi_h exp(-S_0^epsilon) K_0 dU_0,
    R_h^epsilon(V)=int rho_(1,h)^epsilon(U_1) K_1(V,U_1)dU_1,
    A_h^epsilon=int rho_(1,h)^epsilon(U_1)dU_1,
    p_(2,h)^epsilon=R_h^epsilon/A_h^epsilon,
    Z_A(V)=int chi_(A_1)(U_1) b_1(U_1) K_1(V,U_1)dU_1,
    Q_h^epsilon=R_h^epsilon/Z_A,
    b_1=exp(-u_1 sum_p s(U_(1,p))), s(W)=1-Re tr(W)/N.   (G3)

R_h sums **all current** success/failure records, so Xi_h does not read V.
It still retains the specified earlier failure. A_h is the history mass;
Z_A is the different, bare bookkeeping all-cut reference, with no original
epsilon sources. Neither replaces the other. Kernel normalization gives
`int R_h dV=A_h` and `int p_(2,h)dV=1`. In an unconditioned history sum the
weight A_h/Z_0 stays outside p_(2,h), exactly once.

The tested local quotient is the actual RD3 D4 expression

    D_h=a_B(eta) int chi_B rho_(1,h)^epsilon product_(c in C(B)) k_c,
    N_h=a_B(eta) int zeta_B rho_(1,h)^epsilon product_(c in C(B)) k_c,
    r_h=N_h/D_h,
    a_B=exp(u_1 sum_(p notin P_1(B)) s(U_(1,p))).         (G4)

Integrals in G4 run over I(B); |C(B)|<=8. The factor a_B cancels in r_h,
but belongs to D_h. The full conditional convention multiplies D_h by
the exterior factor `O_(1,B)=a_B^-1 product_(c notin C(B))k_c`.
Every statement about a denominator specifies which convention it uses.
No chart determinant or kernel normalizer is discarded.

## 2. Positive normalizers and a relative-jet lemma — PROVEN

### G-POS: actual positivity, including the failed history

In each of the two old blocks put `g=diag(-1,-1,1,...)` on the interior
direction-one link at within-block coordinates (1,1,1,1); set every other
old link to I. All plaquettes reading either marked link are interior to
its block and have distance two from I. Other plaquettes are I. On the
product of open operator balls of radius delta=1/16 about these links,
four-factor telescoping changes a plaquette by less than 1/4. Hence the
bad set is exactly Y_0, and its size forces failure independently of U_1.
This cap has positive Haar mass; all finite real Wilson and soft factors
are strictly positive. Consequently rho_(1,h)^epsilon(U_1)>0 for every
real U_1 and every finite real epsilon, including the entire window G1.

The all-identity cap for the current interior links satisfies chi_B,
independently of eta, since its cut reads only interior plaquettes.
Thus D_h>0 on every eta,V in this example. A current marked-link cap also
gives N_h>0. A cap for **all** current links satisfies chi_A for every
fixed active set, even with holes, so Z_A>0. R_h and A_h are positive.
For a general old history, positivity holds on its admitted nonzero
support/fibres; zero-mass histories remain zero summands and are never
conditioned on. A local good fibre can be empty for a different history;
it is not declared positive merely because the whole history has mass.

For an explicit finite cap bound, normalized Haar assigns an operator
ball of radius zeta<=1 at least `(1+4N/zeta)^(-2N^2)`. Subdivide the
2N^2 real matrix-entry coordinates into cells of side zeta/(2N); two
matrices in one cell have Frobenius distance at most zeta/sqrt(2).
Representatives give a cover by translates of a zeta-ball, and Haar
invariance proves the bound. With n_j current lattice sites,
b=L^4, t_j=kappa u_j, and 4 zeta below every retained cut, this gives

    Z_(j,A)(V) >= exp[-(48u_j zeta^2
                         +8N^2 log(1+4N/zeta)) n_j
                      -8kappa u_j n_(j+1)].             (G5)

Indeed `s(U_p)<=8zeta^2`, there are 6n_j plaquettes and 4n_j links,
and `exp(-2t)<=k_t<=exp(2t)` since `|h_M|<=1`.
This retains the actual normalizers. G5 is extensive; it supplies
positivity, not a volume-independent inverse bound or a local log.
Every positive integral divided by its own mass defines a probability
of total variation exactly one.

### G-JET: a positive-integral estimate with no rare-mass inverse

Let `Z(q)=int_E w_0(y) exp H(q,y) dy>0`, where E and w_0>=0 do not
depend on q. Suppose differentiation through order four is dominated,
and for 1<=m<=4

    |D^m H(q,y)[v_1,...,v_m]| <= B product_i |v_i|_1.    (G6)

B is the same nonnegative bound for those four orders. Let Pi_m denote
set partitions of {1,...,m}; empty-order quantities are specified below.
Repeated differentiation, assigning each new derivative to its block or
to a new block, gives

    M_0=1, M_m(B)=sum_(pi in Pi_m) B^|pi|,
    ||D^m Z||/Z <= M_m(B),
    L_m(B)=sum_(pi in Pi_m) (|pi|-1)! product_(C in pi) M_|C|(B),
    ||D^m log Z|| <= L_m(B),                            (G7)
    I_0=1, I_m(B)=sum_(pi in Pi_m) |pi|! product_(C in pi) M_|C|(B),
    Z ||D^m(1/Z)|| <= I_m(B).

For the first inequality divide the differentiated integral by Z and
use its positive probability law. For the last two, Taylor-expand
`log(Z+dZ)` and `(Z+dZ)^-1` to degree four at a fixed real point. The
coefficient of m distinct nilpotent direction labels has respectively
`(-1)^(|pi|-1)(|pi|-1)!` and `(-1)^|pi| |pi|!`. Taking absolute values
and applying the first inequality gives G7. This is finite real algebra;
no complex log or Cauchy estimate is used. It includes derivatives of the
normalized measure, rather than silently holding that measure fixed.

If positive N and D separately satisfy G6 with the same upper B, then
Leibniz and G7 give, for F=N/D,

    ||D^m F|| <= F C_m(B),
    C_m(B)=sum_(l=0)^m binom(m,l) M_l(B) I_(m-l)(B),
    |F|_(4,h) <= P_4(h,B) sup F,
    P_4(h,B)=sum_(m=0)^4 h^m C_m(B)/m!.                 (G8)

These are **relative** estimates. A nonnegative numerator with a fixed
zero support is identically zero and satisfies the absolute statement
trivially. A signed connected coefficient does not satisfy this positive
lemma merely because its parent partition function does.

The explicit polynomials are useful for keeping the derivative bill:

| m | M_m | L_m (m>=1) | I_m | C_m |
|---|---|---|---|---|
| 0 | 1 | — | 1 | 1 |
| 1 | B | B | B | 2B |
| 2 | B+B^2 | B+2B^2 | B+3B^2 | 2B+6B^2 |
| 3 | B+3B^2+B^3 | B+6B^2+6B^3 | B+9B^2+13B^3 | 2B+18B^2+26B^3 |
| 4 | B+7B^2+6B^3+B^4 | B+14B^2+36B^3+26B^4 | B+21B^2+78B^3+75B^4 | 2B+42B^2+156B^3+150B^4 |

If `h<=1/(1+B)`, each monomial `h^m B^l`, l<=m, is at most one.
Thus `P_4(h,B)<=P_4(1,1)=117/4`, and the derivative-only log sum
`sum_(m=1)^4 h^m L_m(B)/m!<=63/8`. A normalized log difference still
needs its m=0 bound: integrating its first derivative along a path can
cost the l1 length of that path, which grows with a full source box.
The jet rescaling is explicit; original derivatives cost h^-m again.

### G-SOFT: application to the actual fixed-sector step

For V=Vbar exp X the q-dependent part of the logarithm of the opened
integrand is

    H(q,y)=-u_0 sum_p epsilon_p s(U_(0,p))
              +t_j sum_c Re tr(exp(-X_c) Vbar_c^* M_c(U_j))/N. (G9)

All previous normalized kernels, their M-dependent normalizers, cuts,
history absences and hole variables remain in w_0. The last kernel's
normalizer also remains there, because it is independent of its output V.
For Z_A the source term is absent. For A_h the terminal term is absent.

Here is the needed matrix derivative bound. Differentiate the ODE
`d exp(sX)/ds=X exp(sX)` by variation of constants. Repeating m times
expresses D^m exp(X) as the sum over m! orders of A_1,...,A_m integrated
over the ordered unit simplex, with unitary exponential factors between
them whenever X and the directions are anti-Hermitian. That simplex has
volume 1/m!, so

    ||D^m exp(X)[A_1,...,A_m]||op <= product_i ||A_i||op.

Trace duality and ||M||<=1 apply to G9. At first order its bound is
`2u_0 sum|a_p|+t_j sum||A_c||`. At higher orders the source term is
zero and `sum_c product_i ||A_(i,c)|| <= product_i sum_c ||A_(i,c)||`.
Consequently G6 holds with

    B_j=max(2u_0,t_j),                                  (G10)

independently of volume, history depth, hole sizes, source base point,
real exterior data, and real output base point. The constant depends
on the displayed couplings; it is not a weak-coupling small parameter.
Compact integration domains, fixed bounded predicates and finite kernels
justify differentiation by domination on compact real parameter sets.

G7 therefore bounds all positive-order log derivatives of R_h,A_h,Z_A,
and the local D_h,N_h at fixed eta. G8 bounds Q_h,p_(2,h),r_h and
positive reference-normalized versions of those objects. In G4 a_B is
q-independent and cancels from the relative derivative calculation.
For the full conditional normalizer O_(1,B)D_h retain the explicit
exterior kernel logs; their derivatives have the same t_j-type bound.

This is a genuine one-step derivative estimate on the failed/hole
example, and on every fixed-sector positive integral of the displayed
form. It does **not** estimate sup Q_h or sup r_h by a small number.
For example RD3's cap calculation gives only

    sup r_h^0 <= m_delta^(-n_I) (u_h/l_h) exp(4t_1 |C(B)|),
    n_I=4L^3(L-1),
    l_h=m_delta^|E_0| exp(-2u_0 P_0-2t_0|E_1|),
    u_h=exp(2t_0|E_1|),
    m_delta=(1+4sqrt(2)N/delta)^(-2N^2).                (G11)

It follows by using the old witnessed cap for the denominator, the
current good cap, and the uniform kernel bounds. The entry-cover proof
for this more conservative m_delta is the same as for G5. G11 grows with
the surrounding volume. Multiplying it by P_4 does not close a returned
activity budget. This is failure of an available upper majorant, not a
lower bound on the optimal activity or an impossibility result.

## 3. What positivity does not close on the real section

**PROVEN diagnostic; actual local estimate OPEN.** Differentiation of G3
or G4 under its complete conditioned positive law gives

    partial_(epsilon_p) log R_h=-u_0 E_(h,V) s_p,
    partial_(epsilon_p) partial_(epsilon_q) log R_h
                      =u_0^2 Cov_(h,V)(s_p,s_q).         (G12)

The same identity holds for D_h at fixed eta; Z_A has no epsilon term.
Since 0<=s<=2, `Var(s)<=E(s-1)^2<=1` and Cauchy–Schwarz gives
`|Cov(s_p,s_q)|<=1`. Thus G12 is uniform pointwise, but has no distance
decay or summability. A local fourth-jet logarithm with budget k_* and
fixed source/block incidence would in particular imply a bound of the
form

    sup_p sum_q |partial_p partial_q log R_h| <= C_(jet,mu,incidence) k_*,
                                                               (G13)

where C may depend on the jet weight h and fixed block incidence,
not on the history.
For example if each block contains at most c_p source labels, G1 bounds
the left side by `2 c_p h^-2 sup_(n>=1) n exp(-mu n) k_*` for mu>0:
only supports containing p and q contribute, and each has at most
c_p |X| such q. This demonstrates an actual consequence of the desired
norm. G12's separate covariance bound does not establish it.

For the general inference, condition m independent fair signs on their
all being equal. The resulting positive probability has log-MGF
`log cosh(sum_i z_i)`, with every mixed second derivative equal to one
at zero. Its rooted covariance sum is m. This proves that positivity,
extraction of the rare conditioning mass, and bounded relative derivatives
do not imply a uniform G13. It is not a counterexample to G13 for the
Wilson law. For Q_h the source-free denominator cannot cancel its bulk
source response; any boundary comparison must keep a bulk contribution.

**OPEN — moving current selectors.** The actual selected child contains
`I_(a|h)(U,V)` and may have the completion minimum in that predicate.
G9 applies after summing current outcomes, or on a patch where the
selected predicate is fixed for the differentiated coordinates. It cannot
differentiate a moving indicator as zero. Even the positive integral
`int_0^1 1_(y<=|x|)dy=|x|` near zero is not C^1. This diagnostic does not
prove a singularity of the actual child; it shows why a fixed-sector
representation or estimates for its boundary terms are required.
RD3's eta=I successful patch for G4 is legitimate: the identity completion
has `e_flat<=max_(c in C(B))||V_c-I||`, below its positive threshold.
Across other completion boundaries no C^4 theorem is supplied.

**PROVEN — hole transfer in the real jet norm.** For G2, fixed-mask
saturation adds at most 81 vertices. Its closed face-neighbourhood has
`81+8*27=297` vertices. An active output root already lies in the input
support; an inactive root can be charged to an input vertex in this
neighbourhood. Triangle inequality, also for every derivative, gives

    ||K_inactive plus K'||_(mu,4,h)
                   <= (1+297 exp(81mu)) ||K||_(mu,4,h). (G14)

For hole sizes <=M, the same proof as LIB1 gives
`(1+9M)||K||_((1+8M)mu,4,h)`: at most 8|X| holes touch X, and an
inactive root has at most 9M input-root witnesses. These implications
need an actual bound on the fully integrated input K.

There is no arbitrary-hole operator constant for this saturation map
at a fixed mu>0. On a block torus let the sole active vertex be v and
use one constant input activity a>0 supported at {v}. The complement
is connected: from any nonzero vertex keep one nonzero coordinate while
setting another to one, then set all coordinates to one. Thus saturation
maps {v} to the whole torus. The exact full-norm ratio is
`exp(mu(|Gamma|-1))`, unchanged by adding derivatives because this
activity is constant. This refutes only the unrestricted norm-transfer
inequality for that map, already diagnosed by LIB1. Actual history
weights, a bounded-hole class, or a different compatible norm may pay
the cost. Real restriction alone cannot pay it.

## 4. Large fields: the price and its derivative bill

**PROVEN raw real pricing.** Original Wilson fractions may be allocated
only once. A distinct owned plaquette at distance >=epsilon supplies
`theta u_0 epsilon^2/(2N)` with fraction theta. Overlap multiplicity m
requires fraction theta/m. In rescaled units epsilon=g p this is
`theta p^2/(2N)`, as in LFPRICE, not an extra factor 1/g^2. At higher
levels b_j J_h=rho_(j,h); charging b_j alone without its compensating
J_h does not price the inherited law. TC remains a named input for a
general original-law local charge under the correct matched reference.

For the actual soft kernel, set `psi_M(V)=max_W h_M(W)-h_M(V)`.
A 1/t cap about a maximizer and the bound
`|h_M(V)-h_M(W)|<=||V-W||op` give, for t>=1,

    P_K(psi_M>=a) <= min(1,exp(-q_gap)),
    q_gap=t a-1-2N^2 log(1+4Nt).                        (G15)

The proof lower-bounds `int exp(-t psi)` by
`exp(-1)(1+4Nt)^(-2N^2)` and upper-bounds its tail by exp(-ta).
This includes Z_t(M), works for short means, and reproduces JMBRB B-GAP.
For distinct output links the conditional kernels multiply. Integrating
the latest selected outputs first proves multiplication of newly earned
gap prices at past-adapted steps. It does not reprice an old event.

For geometric coarse badness JMBRB's sufficient smooth-input branch
can be rebuilt by sweeping a straight leg across at most
`A_L=3L(L-1)/2` fine plaquettes. Telescoping unitary products gives
`||M_c-S_c||<=A_L eta` and
`||I-V_P||<=L^2 eta+sum_(c in boundary P)||V_c-S_c||`.
Also `psi_M(V)>=||V-S||op^2/(2N)-2||M-S||`. Hence with

    eta_1=min(epsilon/(2L^2),epsilon^2/(512 N A_L)),
    a_epsilon=epsilon^2/(256N),                         (G16)

a coarse bad plaquette has either a fine reader rougher than eta_1,
or one of four boundary links with gap at least a_epsilon. At most six
plaquettes use one link, so n specified bad plaquettes on this smooth
branch have conditional probability at most `4^n p_gap^(n/6)` (capped
at one). For `epsilon=u^((delta_c-1)/2)`, 0<delta_c<1, this price grows
like a positive multiple of u^delta_c after its logarithmic cap costs.
The rough-input branch does not earn that gap price. Its threshold-only
bare bound is of order u^(2delta_c-1); this calculation cannot give a
diverging price when delta_c<=1/2. It does not bound the optimal estimate.

**PROVEN derivative transfer, conditional on the correct scalar object.**
If a fixed-sector positive, normalized regional F_G=N_G/D_G has
`sup F_G<=exp(-nu n)` and its complete integrands satisfy G6 with B_G,
then G8 gives

    |F_G|_(4,h)<=P_4(h,B_G) exp(-nu n).                  (G17)

For original coefficient derivatives only, a source-independent selected
gap event can also stay inside the integral. For terminal-field
derivatives the current gap/completion indicator is moving and needs
the treatment just described; G15 is not by itself a C^4 activity bound.
Sources in return operators or inserted activities require their own
product/derivative estimates. Signed mixed atoms need bounds on their
complete differentiated integrals, not G17 applied to a signed ratio.

There are two additional bills even on the real section. First, a future
reader H>=0 changes K to `K^H(x,dy)=K(x,dy)H(y)/KH(x)`, and

    K^H(x,E)<=P_K(x,E) sup H / KH(x).                   (G18)

Choosing H=1_E gives conditional probability one. Thus the same-reference
tilt and its derivatives must be priced; positivity only sets TV=1 for
the changed normalized law. Second, replacing P plaquettes and C complete
kernels on the same hard support costs at most
`2u P+4kappa u C` in logarithmic real comparison, including Z_t changes.
This follows by comparing each exponential inside its normalizer as well
as its numerator. A nonzero boundary bill of order u defeats the crude
u^delta_c threshold majorant for delta_c<1. A matched cancellation of
local logarithms could reduce it, but those logarithms are an OPEN input.

For a genuine next-step gap lineage with all matching/reader costs paid,
the real derivative version of JMBRB's per-step test is

    theta_gap=sup_j B_(reader,j) P_4(h,B_(score,j))
                                exp(-q_(matched,j)) <1. (G19)

The geometric lifetime sum is theta_gap/(1-theta_gap). G19 is a PROVEN
implication, not an evaluated actual-model bound. Polynomial score costs
give only O(log u) logarithmic debits when B_score=O(u), so a genuinely
matched positive c u^delta_c price can pay them. G18, complete readers,
and the coherent rough branch remain OPEN. Neither a fresh kernel price
nor a fourth-derivative estimate removes those requirements.

## 5. Persistent flux: the real fourth-jet creation bound — PROVEN

This subsection gives an actual positive-sector result, not an operator
contraction on arbitrary insertions. Use CHARGE R1/RENEW's even compatible
tori and the four fields

    g=diag(-1,-1,1,...),
    U_1(x)=g^(x_2+a), U_2(x)=g^d, U_3=U_4=I,
    a,d in {0,1}.                                      (G20)

Each 12 plaquette is g; the others are I. In Decision 4's actual paired
contours the translated axial legs cancel for direction one; in direction
two their exponent is the signed number of direction-one steps. Since
`sum_(r=0)^(L-1)(-1)^r=1`, their means are
`M_1=g^(X_2+a)P, M_2=g^(d+(L-1)/2)P, M_3=M_4=I`, where
`P=diag(1/L,1/L,1,...)`. If M=WP with P>0, expansion gives
`h_M(W)-h_M(V)=tr[(I-W^*V)^*P(I-W^*V)]/(2N)`.
Thus the unique maximizing outputs repeat this rough family, with zero
fresh gap. The restoring force is toward a rough centre.

For completeness its non-null persistence has the following scope.
A contour has at most p_L=5L-4 links. At fixed finite horizon R choose
small terminal tube radius delta_R, then
`delta_j=delta_(j+1)^2/(8NLp_L)`. Within its input tube, an output outside
the next tube has gap at least `delta_(j+1)^2/(4NL)`, by the preceding
positive-P identity and two mean errors. G15 and a union bound over all
output links give

    P(all tubes through R | input tube)
      >=1-sum_(j<R) |E_(j+1)| e(1+4Nt_j)^(2N^2)
                            exp[-t_j delta_(j+1)^2/(4NL)]. (G21)

At fixed R and finite compatible volume this tends to one as the
couplings grow; cuts below two remain failed if the radii are sufficiently
small. Fresh positive gap thresholds with t_j a_j dominating log t_j
occur with probability tending to zero. This is RENEW's finite-horizon
statement, not an interchange with an infinite-depth limit. It prevents
a coupling-uniform plain-forward curvature-return margin on all inputs.

Let E_delta be a **fixed original** tube, 0<delta<1/4, about G20, or the
union of those tubes without counting overlaps repeatedly. On it,

    S_0>=c_delta u_0 n_0,
    c_delta=(2-4delta)^2/(2N)>0.                         (G22)

This follows from the n_0 distinct 12 plaquettes and telescoping; no
general local coercivity theorem is asserted. The single original reserve
can be divided using `alpha_l=(1-b^-1)b^-l`, b=L^4, whose finite sum is
less than one. Its lth fraction is at least
`(1-b^-1)c_delta u_0 n_l` on this filled family. These allocations are
an alternative to the single final allocation below, never an additional
price multiplied into it.

Define the complete numerator through the next step and the same actual
all-cut denominator by

    R_(E,j)^epsilon(V)=int E_delta exp(-S_0^epsilon)
                                    product_(l=0)^j K_l dU_0...dU_j,
    Q_(E,j)^epsilon=R_(E,j)^epsilon/Z_(j,A)(V).           (G23)

A subset of previous histories can be included if its selector reads only
integrated fields, not the terminal V. The sum of disjoint such histories
is included before taking a supremum or a jet norm. There is no inference
bounding a sum of separate history suprema from the supremum of their
sum. A current moving persistent-field selector has a pointwise value
bound, but not the derivative assertion until its boundary is handled.

For `|epsilon_p|<=rho`, positivity and 6n_0 original plaquettes give
`exp(-S_0^epsilon)<=exp(12rho u_0 n_0) exp(-S_0)`.
Strip only the last kernel's upper bound, integrate all earlier outputs,
and use G22. Divide by the actual cap lower bound G5. Uniformly in all
real terminal fields and in every fixed hole/active set,

    Q_(E,j)^epsilon <= exp[-(c_delta-12rho)u_0 n_0+d_j(zeta)n_j],
    d_j(zeta)=48u_j zeta^2+8N^2 log(1+4N/zeta)
                                       +16kappa u_j/b. (G24)

This rebuilds CHARGE C9 with its source debit; the denominator still has
no original sources. No history mass has been divided out.

Supply precisely CHARGE C10's conditions: `4<=u_*<=u_j<=u_0`, the
retained cuts satisfy `epsilon_cut,j sqrt(u_j)>=8`, and j>=j_* with

    16kappa b^(-(j_*+1))<=c_delta/4,
    b^(-j_*) sup_(u>=u_*)
      [48+8N^2 log(1+4N sqrt(u))]/u <=c_delta/4.         (G25)

These are coupling/cut hypotheses, not a derived flow. Put zeta=u_j^-1/2;
G25 implies `d_j n_j<=c_delta u_0 n_0/2`. If
`0<=rho<=c_delta/48`, G24 and G8 therefore yield the new real-jet estimate

    |Q_(E,j)|_(4,h) <= P_4(h,B_j) exp(-c_delta u_0 n_0/4).
                                                               (G26)

The bound holds for four mixed original-source/terminal-coarse derivatives,
not only four copies of a common scalar source. With
`h<=1/(1+B_j)` its prefactor is at most 117/4. It holds for every real
terminal V, arbitrary holes in A, and any retained positive cuts meeting
G25. The finitely many j<j_* retain G24, not an asserted small bound.
RD3's illustrative cuts need not meet G25 at every coupling.

There is also a fixed-original-unit version, avoiding a hidden shrinking
jet weight. Put c=max(2,kappa). Since u_0>=1 and B_j<=c u_0, the positive
coefficients of P_4 give `P_4(h,B_j)<=P_4(h,c)u_0^4`.
The maximum of `u^4 exp(-c_delta u/8)` is
`[32/(e c_delta)]^4`, obtained by differentiation. Using n_0>=1 gives

    |Q_(E,j)|_(4,h) <= C_h exp(-c_delta u_0 n_0/8),
    C_h=P_4(h,c)[32/(e c_delta)]^4.                     (G27)

h is now any fixed positive constant independent of coupling, volume,
depth and holes. This absorbs the derivative polynomial once by spending
half of the remaining exponential price, as LFPRICE requires.

For a filled ancestor of a terminal n_R>=1, n_0=b^R n_R. If **separately
justified** complete support/type costs are at most exp(s n_0), and
`lambda=c_delta u_*/8-s>0`, a fixed further lineage bill B^R has envelope

    C_h B^R exp(-lambda b^R n_R).                       (G28)

The ratio of successive terms at fixed n_R is
`B exp[-lambda(b-1)b^R n_R]`, tending to zero; replacing n_R by one
gives a uniform summable envelope. Early levels outside G25 need their
own finite estimates. G28 concerns the stated filled family with the
stated paid costs, not a proved sum over every localized birth/history.
One cannot spend the same original reserve again as a contraction of
an arbitrary insertion conditioned on the flux tube.

For a localized core of m charged witnesses in a large torus, the same
method leaves instead

    |Q_core|_(4,h) <= P_4(h,B_j) exp(-tau m+d_j n_j).    (G29)

The extensive d_j n_j is not a bound by local readers. G29 fails to
certify a volume-uniform small local weight when n_j/m grows. It is not
a lower bound on Q_core. The distinction between G27 and G29 is the
remaining local matching problem, shared with the complex construction.

## 6. The output the next step actually needs

**PROVEN conditional real cluster implication; actual antecedents OPEN.**
After exact reader integration, suppose every selected atom set I has
the complete integrated coefficient
`A_I(q)=c_I(q) int product_(i in I) a_i(q,y) dnu_q(y)`, with A_empty=1.
Every coefficient, differentiated measure, prefactor and fixed-sector
Jacobian is included. Require C^4 regularity, exact factorization over
disjoint **complete** overlap components, and

    |A_I|_(4,h)<=product_(i in I) alpha_i,
    Q_4=sup_x sum_(i:x in H_i) exp((mu+2)|H_i|)alpha_i<=1/4. (G30)

Parameter readers outside H_i are forbidden by the support assertion.
A signed mixed coefficient is bounded here in its own jet norm; scalar
positive ratios from G8 or G27 cannot replace these joint hypotheses.
Any empty-support constant has a separate positive/nonzero normalization
and log-derivative budget. A parameter-dependent bulk term is not an
empty-support constant.

To prove the implication, integrate each selected overlap component
jointly, obtaining its weight on the union of its full supports. Exact
factorization gives a hard-core gas before any log. Work in the
submultiplicative finite-jet norm G1. Put
`v_i=exp((mu+1)|H_i|)alpha_i`, `b_i=exp((mu+2)|H_i|)alpha_i`.
The positive rooted-tree recursion
`T_i=v_i exp(sum_(j:H_j meets H_i) T_j)` has supersolution b_i:
the child sum is at most Q_4 |H_i|<=|H_i|. Marking a constituent through
the output root bounds the integrated gas at exponent mu+1 by Q_4.
For its connected logarithm, order incompatibility edges and group
connected graphs by their Kruskal spanning tree. The allowed extra
edges form an interval; their alternating sum has modulus at most one.
The second tree bound spends the other unit of support exponent and
gives `||log gas||_(mu,4,h)<=Q_4`. An auxiliary atom multiplier z allows
absolute convergence for |z|<2. The formal exponential identity near zero
then holds at z=1; real coefficients give a positive gas and its real
logarithm. The C^4 series converges in G1. This auxiliary complex counting
variable does not assume complex physical sources or coarse fields.

If the two **fully integrated** numerator and reference have supported
prefactor/log budgets b_R,q_R and b_A,q_A in this real norm, respectively,
their source-normalized logarithmic ratio has

    ||K_ratio||_(mu,4,h)<=2(b_R+q_R+b_A+q_A).            (G31)

Subtract their logs and then restrict the same difference to epsilon=0,
with the coarse field X still an argument. The restriction map
`F(epsilon,X) -> F(0,X)` has jet norm at most one, so the factor two
follows; its pure coarse derivatives are retained, not set to zero.
Normalization instead at a fixed full base point has the same bound.
All original support labels are retained. Apply G14 afterward for the
81-block hole, or a separately verified full-hole bound. In particular
the required output budget k_* demands

    2(1+297 exp(81mu))(b_R+q_R+b_A+q_A)<=k_*            (G32)

on this example. Neither G7 nor G30's abstract theorem supplies its
actual four input budgets. G31 concerns R_h/Z_A after the sea integral,
not log of an unintegrated conditional integrand. The distinct terminal
reference-weighted integral gives A_h/Zbar_A, with
`Zbar_A=int chi_A b_j`; it needs its own local estimates.

The real large-region ledger, if the G30 joint construction exists, is

    nu_4=tau-c_ref-c_partial b_partial-d_jet,
    r_4=A_type exp((mu+2)c_s-nu_4),
    exp(h_sf)h_sf+r_4/(1-r_4)<=1/4, r_4<1.              (G33)

d_jet is any proved per-core bound for the differentiated integral costs,
for example `log P_4(h,B_G)/n` where G17 truly applies. Real TV and polar
continuation costs are zero on this positive real reference; c_ref,
boundary comparison and derivative costs are not. The geometry must bound
the **full** support by c_s n and summed type multiplicity by A_type^n,
or be replaced with JMBRA's proved weighted-reader contract. Scalar
history bounds under different laws do not instantiate G33.

**OPEN — actual extracted map.** A next-step theorem must also supply a
stable real history/chart domain, all current selected-sector derivatives,
a symmetry-compatible extraction of vacuum/coupling and every required
relevant or marginal term, and its real coefficient recursions. In one
fixed full norm it needs, for example,

    x_(j+1)<=(lambda_ret+B_reader s_j+eta_j)x_j+C x_j^2+B_reader e_j,
    theta=lambda_ret+B_reader s_*+eta_*+C M<1,
    B_reader e_*<=(1-theta)M, 0<=x_0<=M.                (G34)

Then x_j<=M follows by `x_j^2<=M x_j`. eta_j includes every remaining
coherent-input, chart and completion failure, including small failed
singletons; G19 controls only properly matched newly priced pieces.
RENEW's alternative requires a full-norm m-window continuation bound
`||C_(j+m-1)^irr ... C_j^irr||<=theta_win<1`, prefix bound B_0, and return
bound D_ret, yielding lifetime sum mB_0/(1-theta_win). These are operator
estimates after extraction, not consequences of G21 or G27.

A second viable alternative is a common creation-map envelope

    ||C_(j+r-1)^irr ... C_j^irr A_j||_(mu,4,h)<=a_r,
    sum_(r>=0) a_r<infinity, uniformly in j and admitted data. (G35)

It bounds both each birth's lifetime and accumulation from all past births
at one terminal level. A per-birth summability assertion without a common
lag envelope does not imply the latter. G28 is a benchmark for one filled
family; constructing G35 for all localized mixed creations remains OPEN.

There is no automatic loss of derivative order in multiplication, the
positive integral estimate, or the conditional cluster construction.
Whether the actual extraction/fluctuation/coordinate-change maps preserve
this C^4 norm at an invariant h and support rate is OPEN. In particular
G10's dependence on u_0 cannot silently be replaced by the current u_j
when old original sources are still differentiated. No degree-four norm
is advertised as proving the all-n reconstruction seed.

## 7. Clause disposition and the precise failures

| Real restatement of LF-JMBR | Status on the actual model | What closes here and exact remaining inequality |
|---|---|---|
| 2: one-use charge, matched reference, boundary, differentiated regional weights | **OPEN**, with **PROVEN** filled-family C^4 instance | G27 pays the actual all-cut reference for its filled tubes. General mixed G17/G30/G33 is unproved; G29 retains d_j n_j rather than a local reader cost. |
| 3: positive references, TV, local log and derivative accounting | **PROVEN** positivity/TV and fixed-sector relative/log derivatives; **OPEN** full local clause | G5–G10 hold with explicit coupling constants. G13, G31's local prefactors, and moving-sector boundary derivatives are not supplied. No complex nonvanishing theorem is claimed. |
| 4: integrate complete overlaps before logs, exact disjoint factorization, full rooted jet sums | **PROVEN** finite algebra and conditional theorem; **OPEN** quantitative model clause | Reader elimination multiplies every incident factor before integration. G30 is still missing on the actual interacting matched law; G14 is only a norm transfer after an input exists. |
| 5: every return/failure, relevant extraction and admissible next output | **OPEN** | G32–G35 and the selected-sector C^4/invariant-domain hypotheses remain unmet. G27 prices creation, not the homogeneous coherent-continuation operator. |

Clause 1 retains JMBRA's finite exact replacement identity: with
`dnu_A=chi_A b_j K_j dU/Z_A`, replace each bad component's good interiors
by fresh bad interiors divided by their good local mass C_Y, retaining
J_h=rho_h/b_j. The old good integrals cancel those masses exactly, and
summing B inserts `product_Q(chi_Q+zeta_Q)=1`. All untouched factors
match; every earlier failure/absence remains. This algebra does not make
nu_A a product reference or T_B J_h a product over components.

| Tested assertion / required inequality | Exact disposition | Real-specific or shared? |
|---|---|---|
| Conditioned required atom is small: `exp(beta card(S)) int abs(1_E/P(E))<=1/4` | **Fails**: the left side is exp(beta card(S))>=1. Extract the mass once or change the representation. | Shared; already a real zero-order failure. |
| The direct conditioned-Haar **pointwise supremum majorant** meets Q_sup<=1/4 | **Fails for this chosen majorant**: assigning `alpha_p=sup abs(exp(-u_0 s_p)-1)` (or its larger sup jet norm), a plaquette outside mandatory cells gives `Q_sup>=exp(mu+2)(1-exp(-4u_0/N))>1/4` above `u_0>-(N/4)log(1-exp(-(mu+2))/4)`. Set one integration link to g to lower-bound that supremum. | Shared zero-order failure of this bound. This is not a lower bound on G30's fully integrated coefficients or its optimal Q_4. Joint L1/jet estimates under the same reference, and adapted references, remain live. |
| Cap majorant certifies local return smallness | **Insufficient majorant**, G11/G29 grow with volume at fixed core size. No lower bound or actual-model impossibility follows. | Shared. |
| Positivity plus bounded relative jets implies G13/G30 | **False general inference**, by the conditioned-sign example; actual Wilson estimate **OPEN**. | Shared spatial problem; real positivity does not remove it. |
| Fixed-mu full support saturation has arbitrary-hole uniform constant | **Fails for that map**, ratio exp(mu(card(Gamma)-1)) when mu>0. | Shared zero-order geometry. |
| Plain-forward fixed-window curvature return has a coupling-uniform positive margin on all inputs | **Fails**, G20–G21; actual extracted G34/G35 remains **OPEN**. | Shared real kernel mechanism. |
| Real restriction automatically differentiates current hard selectors | **Unjustified**, G-JET requires fixed sectors or boundary estimates. No actual singularity is asserted. | A regularity obligation shared with the complex formulation; real C^4 is weaker than holomorphy but still substantive. |
| Real TV=1 licenses complex cancellation bounds | Not asserted: complex references need a separate nonzero/TV theorem. | Complex-only requirement removed from this real contract. |

**ARGUED next construction.** Use G-JET to carry derivatives of a genuinely
matched local real reference, and G27 to pay the filled coherent branch.
On the remaining localized mixed sectors, construct the joint differentiated
coefficients in G30, retaining the inherited-versus-bare bulk comparison and
every completion failure. Then test G33 and the extracted G34 or G35 in
one invariant full norm. FR, KR and TC remain named coordinator inputs at
their exact scopes: real fixed-domain/selector maps, full local interaction
and prefactor/remainder bounds, and joint original-law charges/tails with
their exterior/reference costs. None of their all-history extensions is
assumed here. The missing local bound overlaps clauses 2–4 and is a
substantial part of the target, not a weaker lemma renamed as closure.

## 8. Scope, checks and review boundary

The explored families were positive score/quotient calculus, same-reference
charging of filled flux, matched joint reader integration, and extracted
continuation. Their actual-model application remains partial. There is no
exhaustion claim or general no-go for real RG. The negative assertions above
are specific identities, counterexamples to general inferences, or failures
of identified majorants. They do not prove failure of the Yang–Mills model.

The requirements are not counted as independent walls: G30 can supply
local log estimates, while an invariant return requires those estimates at
its successive states. The derivative, support and reference obligations
overlap. Fixed-sector predicates, positive reference support, source units,
coupling/cut conditions, fixed original readers and explicit history sums
are all load-bearing hypotheses. The source material supplies this finite
model; no framework derivation or missing primitive is inferred.

The strongest positive result here is G27, a fixed-weight real fourth-jet
bound against the actual Z_(j,A) for the specified extensive flux family.
The strongest remaining one-step obligation is G30 with actual small local
coefficients on the same real reference, including selected-sector boundary
derivatives. Full iteration additionally requires G34 or G35 and relevant
coefficient control. A matched interacting real reference with paid readers
and an extracted creation envelope remains a live route around every
diagnostic in the table.

Exact polynomial/finite-geometry checks are preregistered in
[checks/realrgb_criteria.md](checks/realrgb_criteria.md). They verify
bookkeeping, not the open physical estimates. Their actual execution result
and the required fresh hostile review are recorded in REALRGB_LOG.md;
neither an unrun check nor author algebra is labelled independent review.
