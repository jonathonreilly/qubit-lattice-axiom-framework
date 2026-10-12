---
claim_id: boost_quantitative_corrector_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "For the exact supplied globally normalized preparation, a physical approximate range corrector yields explicit L2 and H1 errors on growing effective-time windows. Combined with the conditional outgoing theorem, correction norms converge simultaneously for eta below 1/4; all nine normalized current residual means vanish for eta below 1/6. No exponent optimality, total-state occupation or physical covariance is asserted."
upstream_dependencies:
  - excluded_walk_boost_bracket_control_bounded_theorem_note_2026-10-11
  - boost_forced_outgoing_bounded_theorem_note_2026-10-12
runner: scripts/boost_quantitative_corrector_2026_10_12.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A quantitative range corrector for the actual X error

**Type:** bounded_theorem

Derivation dated 2026-10-11–12 by `boost_kernel_dynamics`, with root as
coauthor of the proposed mechanism. Status: conditional-support. This is a
separate extension of the frozen X and K sources. Selective review and its
exact evidence roles are recorded in the milestone packet; no audit verdict
or retained status is applied.

For exactly X's globally normalized B25–B30 preparation, let W_lambda and z
be its actual rescaled comparison correction and effective forced limit.
This note proves an explicit estimate, valid for every finite T>=0 and
0<lambda<=1/16:

    sup_(|tau|<=T) ||W_lambda(tau)-z(tau)||_(H1_kappa L2_q)
       <= C_* sqrt(lambda) (1+T)^3.                          (Q1)

The constant C_* is specified below in terms of the fixed envelope's L1
mass and elementary numbers. In particular the fixed-T rate is
O_T(sqrt(lambda)). The same estimate proves uniform H1 convergence on
T=lambda^(-eta) for every fixed 0<eta<1/6. A separate L2 bound permits
0<eta<1/4. Only after proving these growing-time estimates do we combine
the latter with K's effective outgoing result to obtain simultaneous
original-walk comparison-correction norm limits. The nine normalized current
expectations also tend uniformly to zero on every 0<eta<1/6 window, with
an explicit all-T bound proved in Section 7.

The new estimate exploits the actual longitudinal triplet residual. It
does not assume a gap of H_*, apply an inverse on its entire complement,
or differentiate zeta in q. K's forcing gap bounds this particular
effective solution; the distinct H_* estimate comes from the physical
singlet range corrector. The exponent 1/2 and the growing-time windows are
upper bound consequences, not optimality claims. The complete earlier
exponential estimate and logarithmic-window proof are preserved unchanged.

## 1. Exact source boundary and constants

S denotes the original research source collection, preserved losslessly in the
[complete milestone packet](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/433f641f24296b6d8e786930bb1327f434015162/.claude/science/physics-loops/toe-boost-quantitative-outgoing-20261012/). EVIDENCE_MAP.json maps the exact source identities below
to their preserved bytes. The [boost theorem](EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md)
is the in-branch B/E/X dependency; [K](BOOST_FORCED_OUTGOING_BOUNDED_THEOREM_NOTE_2026-10-12.md)
is published alongside this note and discloses its provisional memory import:

| Source relative to S | SHA-256 | Use |
|---|---|---|
| `ROOT_HSTAR_APPROXIMATE_CORRECTOR_LEAD.md` | `3ba9b713942b18e0562ca3b60c840676194b78132e797e088037953e6f808ec1` | Root's proposal, checked here rather than assumed |
| `ROOT_POLYNOMIAL_CORRECTOR_REFINEMENT.md` | `4466bde85ef219e0b20427d996aa5e3c8c4f75f52fc84aa8404ae8f05e6db78f` | Root's proposed refinement, separately checked below |
| `BOOST_CURRENT_EXPECTATION_PROBE.md` | `a7161d796001df4af243263acbd03e731d75d0eab2d93795f4b5960eff5acb68` | Exact physical space, preparation, X9–X13 and X18–X24 |
| `BOOST_CURRENT_EXPECTATION_REVIEW.md` | `0e17f9647141c200b1efcbe78f60ef6beedc1e249ce1b85544293dddbebe8690` | Existing source-bound X review; not review of this extension |
| `boost_expectation_review/PROOF_RECONSTRUCTION.md` | `04adc0b81d3865f4819b8441e25279ef084bda755e9c0a3206be7d314ea04f9f` | Complete X reconstruction |
| `BOOST_CURRENT_INVERSE_ENERGY_PROBE.md` | `76ed691c581d4da282041b99fa53da48d1461b47ddccb765b736969a191b4990` | Complete physical kernel and preserved norm obstruction |
| `EXCLUDED_WALK_BOOST_CURRENT_PROBE.md` | `903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923` | Supplied operators and exact B25–B30 preparation |
| `BOOST_KERNEL_EFFECTIVE_DYNAMICS_PROBE.md` | `1c314fc05a26ca27e0828a70ca8132a2bad269b60c127ea37a53e11e95e087c9` | K2/K8 for the refined weighted estimate; K9–K17 for simultaneous norm limits |
| `BOOST_KERNEL_EFFECTIVE_DYNAMICS_REVIEW.md` | `64cf08ea2c12f086d0efcc862d17ce0e394f53dfbcbfa5d48db73a10bb9652ca` | Selective independent check of the exact frozen K1–K19; does not cover this Q argument |

X and the root lead were reread completely for this dispatch. The unchanged
mathematical sources and applicable instructions were read completely in
the immediately preceding K task and are reused at their exact identities.
K's source/evidence receipt has SHA-256
`8767499b08e7721cf1133930fcd9e0a5c703536b46aba5eacd98b81b688d7352`.
The full new K review and its receipt were read before this note's freeze.
Its receipt SHA-256 is
`6ecec5f7e9831fde22922d2ff6f5b7db4a31059ca82cf4b550a058a3a1aff7ce`;
all fourteen artifact bindings match. That source-bound review requires no
K correction and supports its conditional reuse. It does not check Q1–Q34
or confer retained status; no re-review of all its underlying artifacts is
claimed by this worker.
Copies, read scope, instructions and the current recovery checkpoint are in
`boost_hstar_quantitative_corrector/`. No global priority claim is made.

All supplied-model premises remain: sine-Pauli Hamiltonian, antisymmetric
pair sector, contact exclusion, momentum coordinates, clock, symmetric
energy placement and exact preparation. No framework primitive supplies
or changes these choices. The root lead's suggested estimates are proposals;
their valid versions and the sharper mean-subtraction estimate are derived
below.

Every relative inner product uses normalized full-torus measure
dmu=dq/(2pi)^3. Total rescaled momentum uses Lebesgue dkappa. Put

    c0=(2pi)^(-3/2),   m=integral f(x)dx,
    L=192/7,   S0=203m/4,   M=8 c0 S0,
    c_x=pi/4,
    c_e=sqrt(pi/2)+pi sqrt(6)/4,
    K_R=2c_x+c_e,
    C_*=M(30K_R+7).                                        (Q2)

Here f is exactly X's positive radial L2-normalized smooth bump on
5/8<|x|<3/4. Cauchy–Schwarz gives
`0<m<=sqrt(91pi/384)<1`. The exact F has ||F||_2=1,
||partial_j F||_2<=L and support |kappa|<=65/512<1/4. Bounds are proved
on the enclosing ball |kappa|<=1/4; sections vanish outside the support of
F and its derivatives. We use
`||u||_(1,Sigma)=||u||_2+sum_j||partial_j u||_2`, which dominates the
usual H1 norm. Q1 is proved with this stronger sum norm.

## 2. Physical residual and an explicit approximate range vector

Let s=sin q, epsilon=|s|, n=s/epsilon, c be the constant unit singlet,
T_j=sigma_(1,j)c and P=I-|c><c|. Singlet coefficients are even in q;
triplet coefficients are odd. A physical singlet alpha c has integral
alpha dmu=0. The supplied K=0 operator satisfies exactly

    H_*(alpha c)=2epsilon alpha n,
    I0=integral dmu/(4epsilon^2),
    zeta=n/(2epsilon sqrt(I0)),
    Pi=F_tr+|zeta><zeta|,   Q=I-Pi,
    F_tr u=(I-nn^T)u on triplets,
    1/12<=I0<=pi sqrt(3)/8.                                (Q3)

The constant singlet is excluded. No singlet belongs to this physical
kernel. The n expression is used only away from the null set of cone zeros.

For any physical odd triplet u, its complementary projection is

    Qu=beta n,
    beta=n dot u-<zeta,u>/(2epsilon sqrt(I0)),
    integral beta/(2epsilon)dmu=0.                         (Q4)

The last equality is global, not pointwise, and is precisely orthogonality
to zeta. beta is even. If |beta|<=C/epsilon almost everywhere, then its
weighted integral in Q4 is absolutely convergent.

For 0<delta<=1 define the linear corrector on such longitudinal residuals:

    m_delta=integral [beta/(2epsilon)]1_(epsilon>=delta)dmu,
    alpha_delta=[beta/(2epsilon)]1_(epsilon>=delta)-m_delta,
    x_delta=alpha_delta c.

It is an even mean-zero physical singlet. Direct substitution gives

    r-H_*x_delta=beta n 1_(epsilon<delta)+2epsilon n m_delta,
    m_delta=-integral [beta/(2epsilon)]1_(epsilon<delta)dmu.
                                                               (Q5)

Both the constant subtraction in x_delta and its contribution in Q5 are
essential. There is no q derivative of the sharp cutoff.

The cone constants can be proved directly. For integrands depending on
epsilon, fold the eight sine cells into [-pi/2,pi/2]^3. Normalized measure
becomes pi^(-3) times Euclidean volume there, and with r=|q|,
`(2/pi)r<=epsilon<=r`. Thus

    integral_(epsilon<delta) epsilon^(-2)dmu
      <=pi^(-3)(pi^2/4) integral_(r<pi delta/2) r^(-2)dq
      =(pi/2)delta,
    integral_(epsilon>=delta) epsilon^(-4)dmu
      <=pi^(-3)(pi^4/16) integral_(r>=delta) r^(-4)dq
      =pi^2/(4delta).                                     (Q6)

Enlarging the first region to its ball and the second to the entire
exterior of its ball only raises their positive radial bounds. Also
integral epsilon^2 dmu=3/2. These facts prove

    |m_delta|<=C pi delta/4,
    ||x_delta||_2<=c_x C delta^(-1/2),
    ||r-H_*x_delta||_2<=c_e C sqrt(delta).                  (Q7)

For the middle bound, mean subtraction is the orthogonal projection P, so
its L2 norm cannot exceed the uncentered cutoff norm. This improves the
root proposal's extra +delta term; no cancellation is assumed in the
last bound. Its two contributions are
`C sqrt(pi delta/2)` and `C pi sqrt(6) delta/4`; use delta<=sqrt(delta).

The map r->x_delta is linear. Whenever time or kappa derivatives of r are
longitudinal, orthogonal to zeta and weighted-bounded in this same sense,
the construction commutes with those derivatives, with Q7 applied to
each one. The cutoff and Pi are independent of both parameters.

## 3. Weighted evolution bounds for the actual residual and its derivatives

On odd triplet fields define

    ||u||_w=ess sup_q epsilon(q)|u(q)|,
    ||u||_W=(integral ||u(kappa,.)||_w^2 dkappa)^(1/2).

The embedding `||u||_2<=2sqrt(I0)||u||_w` is continuous. The rank-one
projection has weighted norm at most one: its bound is
`(4I0)^(-1) integral epsilon^(-2)dmu=1`. The transverse and longitudinal
pointwise projections each have weighted norm one. Consequently

    ||Pi||_w<=2,    ||Q||_w<=2 on triplets,
    ||B_kappa||_w<=|kappa|,
    ||A_kappa||_w<=2|kappa|<=1/2,
    ||partial_j A_kappa||_w<=2 on ker H_*.                 (Q8)

Here B_kappa u=i d cross u with d_j=kappa_j cos q_j,
A_kappa=Pi B_kappa Pi restricted to the kernel, and kernel inputs satisfy
Pi u=u. The same operators have Hilbert bounds ||A||<=1/4 and
||partial_j A||<=1. Weighted bounds and Hilbert unitarity are different
estimates; no weighted unitarity is asserted.

The generic Banach-space exponential bound exp(|t|/2) is valid and supplied
the earlier theorem preserved in the evidence packet. The following
stronger estimate uses the actual source and exact transverse block,
rather than applying that generic growth bound. All constructions below
use bounded operators and kappa/time derivatives, with no q-Sobolev
assumption.

The limiting source is exactly X7:

    y_+=x+kappa/2, y_-=x-kappa/2,
    e=|y_+|+|y_-|,
    w=[1+y_+ dot y_-/(|y_+||y_-|)]/4,
    a(t,kappa)=F(kappa)/Z0 integral f(x)w exp(-it e)dx,
    g=c0 h0 a,   h0=2s,
    Pi g=c0 zeta a/sqrt(I0).                              (Q9)

Z0 is one global scalar in [1/2,1/sqrt(2)]. On the enclosing support,
`|y_+|,|y_-|>=1/2`, `e<=7/4`, `|partial_j e|<=1`,
`w<=1/2`, and `|partial_j w|<=1/2`. Differentiating the integral, including
the phase, gives for |t|<=T:

    ||a||_2<=m,                  ||a_t||_2<=7m/4,
    ||a_j||_2<=m(L+1+T),
    ||a_jt||_2<=m(7L/4+11/4+7T/4).

The first two are <=S0 and the last two are <=S0(1+T). Since
`||h0||_w=6` and `||Pi h0||_w=1/(2I0)<=6`, all source bounds obtained
by multiplying these by 6c0 are dominated by M and M(1+T), respectively.

The actual effective equation and its parameter derivative are

    i z_t=A z-Pi g,        z(0)=0,
    i (z_j)_t=A z_j+A_j z-Pi g_j,       z_j(0)=0.          (Q10)

Here is a quantitative extraction from K8 at each individual kappa; it
does not infer pointwise bounds from an integrated Sobolev estimate. Put
`d0=c0/(Z0 sqrt(I0))`, `R=(e-A)^(-1)`. On the actual source support,
e-sigma(A)>=1, ||R||<=1 and ||partial_j R||<=2. K8 reads

    z(t,kappa)=d0 F(kappa) integral f w R
                   [exp(-itA)-exp(-ite)]zeta dx.

The bracket has norm at most 2 and its j derivative norm at most 2|t|.
Using |w_j|<=1/2, the derivative of the integral is bounded by
`m(1+2+|t|)`: these are the weight, resolvent and exponential terms.
Consequently, for every kappa in the enclosing ball,

    ||z(t,kappa)||_2<=d0 m |F(kappa)|,
    ||z_j(t,kappa)||_2
       <=d0 m[|F_j(kappa)|+(3+|t|)|F(kappa)|].

In particular alpha=<zeta,z> and alpha_j obey these same scalar bounds.
The K2 block, including its full transverse multiplicity, is

    A=[D             g_bath],
      [<g_bath|          0 ],
    D=omega J,  omega=d dot n,  J=i n cross,
    g_bath=i(d cross n)/(2epsilon sqrt(I0)).

Write z=u+alpha zeta with u in F_tr. Its transverse equation contains no
direct source, since Pi g is proportional to zeta. It gives exactly

    u(t)=-i integral_0^t exp[-i(t-s)D]g_bath alpha(s)ds.

Pointwise on the transverse plane D is Hermitian. D and D_j are scalar
multiples of the same J and commute there; ||D_j||<=1. Thus its propagator
has pointwise norm one and its j derivative norm at most |t-s|. This uses
the parity-preserving D, not J as a separate global odd-triplet operator.
Put q0=1/(2sqrt(I0)). Then
`||g_bath||_w<=q0/4`, `||(g_bath)_j||_w<=q0`, and `||zeta||_w=q0`.
Differentiate the displayed integral in all three places: the propagator,
g_bath and alpha. Applying the pointwise kappa bounds above and Minkowski
gives, with `J0=12c0 m>=q0 d0 m`,

    sup||z||_W<=J0(1+T/4)<=M(1+T),
    sup||z_j||_W
       <=J0[L+3+(2+(L+3)/4)T+T^2/4]
       <=2M(1+T)^2,
    sup||z_t||_W<=J0(1+T)<=M(1+T),
    sup||z_jt||_W<=4M(1+T)^2.                            (Q11)

The derivative polynomial comes from q0 alpha_j, the propagator integral
with T^2/8, the g_bath derivative integral with T, and the alpha_j integral
with `(L+3)T/4+T^2/8`. Here q0 d0 m=c0m/(2Z0 I0)<=12c0m and
12(L+3)<406=M/(c0m); coefficient comparison proves the displayed bound.
The z_t bound uses Q10, ||A||_w<=1/2, the first sharper Q11 bound and
`||Pi g||_W<=6c0m=J0/2`. The mixed time derivative follows from Q10,
retaining A_j z and Pi g_j. All three differentiated integral terms have
an integrable fixed-time weighted bound, so differentiation and the
pointwise representation are legitimate in W and L2. Negative times use
oriented integrals and the same absolute-time bounds.

The exact X residual is r=Q(Bz-g). B preserves triplets; z and g are
triplets. Thus Q4 applies to r and to all four types of derivatives needed:

    r_t=Q(B z_t-g_t),
    r_j=Q(V_j z+B z_j-g_j),
    r_jt=Q(V_j z_t+B z_jt-g_jt),   V_j=partial_j B.

Using ||V_j||_w<=1, Q8 and Q11 gives the following convenient common
bounds, always uniform over |t|<=T:

    ||r||_W, ||r_t||_W <= R0(T):=3M(1+T),
    ||r_j||_W, ||r_jt||_W <= R1(T):=6M(1+T)^2.            (Q12)

These are precisely the source/time bounds needed in Q7. They establish
their hypotheses for the actual residual rather than for arbitrary
complement vectors. In the ordinary Hilbert norm, unitarity and Q10 give
the elementary polynomial estimates

    sup||z||_2<=MT,       sup||z_j||_2<=MT(1+T).            (Q13)

## 4. Uniform source and generator approximation, with all time factors

Let 0<lambda<=1/16. Write u_lambda(y)=sin(lambda y)/lambda and
nu_lambda(y)=u_lambda(y)/|u_lambda(y)|. This local unit vector is distinct
from X's global normalization n_lambda below.
For 1/2<=|y|<=7/8, elementary sine remainders give

    |u_lambda-y|<=lambda^2/6,
    ||D_y u_lambda-I||<=lambda^2/2,
    |u_lambda|>=|y|/2>=1/4,
    |nu_lambda(y)-y/|y||<=2lambda^2/3,
    ||D_y nu_lambda-D_y(y/|y|)||<=26lambda^2/3.            (Q14)

For the last inequality write the derivative as
`(I-nu_lambda nu_lambda^T)D_yu_lambda/|u_lambda|`. Splitting its difference
from `(I-nn^T)/|y|` gives the bounds
`16lambda^2/3`, `2lambda^2`, and `4lambda^2/3` for the projection,
Jacobian and reciprocal-radius terms. This verifies every denominator
and derivative constant without a numerical grid.

The exact e_lambda,w_lambda are X5's expressions with u_lambda(y_+),
u_lambda(y_-). Q14, with each y derivative carrying 1/2, implies

    |e_lambda-e|<=lambda^2/3,
    |partial_j(e_lambda-e)|<=7lambda^2/6,
    |w_lambda-w|<=lambda^2/3,
    |partial_j(w_lambda-w)|<=5lambda^2/2.                 (Q15)

Also `e_lambda<=7/4`, `|partial_j e_lambda|<=1`,
`|partial_j w_lambda|<=1`, and the inherited exact bound is
1/4<=w_lambda<=1/2. The global constants satisfy

    |Z_lambda-Z0|<=lambda^2/3,
    |Z_lambda^(-1)-Z0^(-1)|<=4lambda^2/3,
    n_lambda^2=1-c0^2 lambda^3 ||a_lambda(0)||_2^2,
    n_lambda>=1/2,
    |n_lambda^(-1)-1|<=2c0^2 m^2 lambda^3.                (Q16)

The first line follows from the exact Z-squared integrals and
Z_lambda,Z0>=1/2. The last two use ||a_lambda(0)||_2<=m. Neither global
constant has a kappa derivative.

For clarity about large times, `|exp(-it e_lambda)-exp(-it e)|`
is bounded by `|t|lambda^2/3` for every real t; no smallness assumption on
lambda^2 T is used. Applying Q15 and the product rule inside X5 yields

    ||a_lambda||_2<=m,
    ||partial_j a_lambda||_2<=m(L+2+T)<=S0(1+T),
    ||a_lambda-a||_2<=2m lambda^2(1+T),
    ||partial_j(a_lambda-a)||_2
                    <=C_a lambda^2(1+T)^2,
    C_a=2m(L+3)<=2S0.                                    (Q17)

One can verify the last bound before multiplying by F/Z. For
I_lambda=integral f w_lambda exp(-it e_lambda), the derivative difference
is at most
`m lambda^2[5/2+13|t|/12+t^2/6]`. The terms are, respectively, the
projector derivative difference, its phase difference plus the e_j
difference, and the phase difference in the clock derivative. Hence it is
at most `(5m/2)lambda^2(1+T)^2`. The F_j and reciprocal-Z terms add at
most `2mL+2m/3`, giving `2mL+17m/3<=C_a`. The source phase derivative
has therefore not been omitted.

The exact Hamiltonian has the decomposition

    G_lambda=H(lambda kappa)/lambda=H_*/lambda+B+E_lambda,
    V_lambda=B+E_lambda,
    ||E_lambda||<=lambda/32,
    ||partial_j E_lambda||<=lambda/4,
    ||V_lambda||<=1,       ||partial_j G_lambda||<=1.      (Q18)

Indeed the difference-spin symbol contributes at most
`lambda |kappa|^2/4`, and the total-spin sine remainder at most
`lambda^2 sum_j|kappa_j|^3/24` to ||E_lambda||. Differentiation bounds
the j term by `lambda|kappa_j|/2+lambda^2 kappa_j^2/8`.
Compression by P cannot increase these norms. The last bound follows
directly by differentiating the original two-spin symbol, each term
carrying 1/2; H_* is independent of kappa.

Similarly the exact h(lambda kappa)=2sum_j cos(lambda kappa_j/2)s_j T_j
satisfies

    ||h(lambda kappa)||_2<=sqrt(6),
    ||h(lambda kappa)-h0||_2<=lambda^2/64,
    ||partial_j h(lambda kappa)||_2<=lambda^2/8.

Combining this, Q16 and Q17 with the exact source
`g_lambda=c0 h(lambda kappa)a_lambda/n_lambda` gives

    ||g_lambda||_2<=M,
    ||partial_j g_lambda||_2<=M(1+T),
    ||g_lambda-g||_2<=M lambda^2(1+T),
    ||partial_j(g_lambda-g)||_2<=2M lambda^2(1+T)^2.        (Q19)

For explicit coefficient checks, the last two differences are bounded
respectively by lambda^2(1+T) times
`c0 m[1/32+4sqrt(6)+2sqrt(6)c0^2m^2]` and lambda^2(1+T)^2 times
`c0 m/4+c0 S0/32+2sqrt(6)c0 C_a+2sqrt(6)c0^3m^2 S0`.
Use m<1, c0<1, S0=203m/4 and C_a<=2S0 to obtain Q19.

Finally unitarity in X9 and its exact derivative, including the propagator
derivative, gives for all lambda under consideration

    sup||W_lambda||_2<=MT,
    sup||partial_j W_lambda||_2<=MT(1+T).                 (Q20)

The derivative integral has both `(partial_j U_lambda)g_lambda` and
`U_lambda partial_j g_lambda`, with `||partial_j U_lambda(t)||<=|t|`.
Q19 retained the h, projector, phase and envelope derivatives explicitly.

## 5. Corrector integration by parts and the full differentiated error

For a longitudinal residual f(s) satisfying the conditions of Q4, let
x_delta(s) be Q5 and eta_delta=f-H_*x_delta. Put
U_lambda(t)=exp(-itG_lambda). The exact identity is

    integral_0^t U_lambda(t-s)f(s)ds
      =-i lambda[U_lambda(t-s)x_delta(s)]_(s=0)^(s=t)
       +i lambda integral_0^t U_lambda(t-s)partial_s x_delta(s)ds
       -lambda integral_0^t U_lambda(t-s)V_lambda x_delta(s)ds
       +integral_0^t U_lambda(t-s)eta_delta(s)ds.           (Q21)

It uses H_*=lambda(G_lambda-V_lambda) and
`partial_s U_lambda(t-s)=iU_lambda(t-s)G_lambda`. Both endpoint
correctors occur, including the nonzero initial one. No commutation of
V_lambda with H_*, the cutoff or x_delta is used.

Apply the fiberwise Q7 bounds and then the L2_kappa norm. If
`sup_(|s|<=T)(||f(s)||_W,||f_s(s)||_W)<=R`, unitarity and Q18 give

    sup_(|t|<=T)||integral_0^t U_lambda(t-s)f(s)ds||_2
      <=R[c_x lambda delta^(-1/2)(2+2T)+c_e sqrt(delta)T].

Taking delta=lambda, with lambda<=1/16, yields

    sup||integral_0^t U_lambda(t-s)f(s)ds||_2
                        <=K_R R sqrt(lambda)(1+T).       (Q22)

No differentiation of this convergence estimate is needed. Instead use
X's exact error equations on the full physical Hilbert space:

    D_lambda=W_lambda-z,
    i(D_lambda)_t=G_lambda D_lambda+r+e_lambda,
    e_lambda=E_lambda z+g-g_lambda,     D_lambda(0)=0,
    i(partial_j D_lambda)_t=G_lambda partial_j D_lambda
            +(partial_j G_lambda)D_lambda+r_j+partial_j e_lambda,
    partial_j D_lambda(0)=0.                              (Q23)

The residuals r,r_j are exactly those whose time derivatives and weighted
bounds were established in Q12. e_lambda can have a singlet component;
we estimate it in the full Hilbert space without a kernel restriction.
Q13, Q18 and Q19 imply

    sup||e_lambda||_2<=M lambda(1+T),
    sup||partial_j e_lambda||_2<=M lambda(1+T)^2.           (Q24)

For the derivative, the three coefficient bounds are
`M lambda T/4`, `M lambda T(1+T)/32` and
`2M lambda^2(1+T)^2`. Their sum is <=M lambda(1+T)^2 because
lambda<=1/16. The undifferentiated inequality follows in the same way
from `M lambda T/32+M lambda^2(1+T)`.

Apply Q22 to r using R0(T), and use the ordinary unitary estimate on
e_lambda. This gives

    sup||D_lambda||_2
       <=M(3K_R+1)sqrt(lambda)(1+T)^2.                    (Q25)

For each j apply Q22 to r_j using R1(T). The remaining first-derivative
equation contains the full D_lambda term multiplied by partial_j G_lambda;
Q18 bounds its integral by T times Q25. The integral of partial_j e_lambda
is bounded by T times Q24. Consequently

    sup||partial_j D_lambda||_2
       <=M(9K_R+2)sqrt(lambda)(1+T)^3.                    (Q26)

Summing Q25 and the three Q26 bounds proves Q1 with the explicit C_* in
Q2. All estimates hold for positive and negative t: the exact integral
identities remain valid with oriented integrals, and each norm estimate
uses their length |t|. This proof does not differentiate a qualitative
limit and does not replace the actual full error by its kernel projection.

## 6. Proved growing-time windows and simultaneous correction norms

For fixed eta>0 put T_win(lambda)=lambda^(-eta). Direct substitution in
the all-T bounds Q1 and Q25, with 1+lambda^(-eta)<=2lambda^(-eta), gives

    sup_(|tau|<=T_win(lambda))||W_lambda(tau)-z(tau)||_H1
      <=8C_* lambda^(1/2-3eta) ->0,        0<eta<1/6,
    sup_(|tau|<=T_win(lambda))||W_lambda(tau)-z(tau)||_2
      <=4M(3K_R+1)lambda^(1/2-2eta) ->0,  0<eta<1/4.     (Q27)

These are separate topology bounds. Neither reaches its displayed endpoint
exponent by this argument, and no failure outside these windows is implied.
Every fixed logarithmic schedule is also covered. There is no iterated-limit
argument or unquantified fixed-T substitution: the single all-T bounds
have the displayed constants and powers before T is chosen.

Now use the further outgoing statement in the frozen K result. With
exactly its constants,

    v(kappa)=c0 F(kappa)/(Z0 sqrt(I0)) chi_kappa(A_kappa)zeta,
    chi_kappa(E)=integral f(x)w(kappa,x)/(e(kappa,x)-E)dx,
    V=||v||_2^2,
    c0^2m^2/(64Z0^2 I0)<=V<=c0^2m^2/(4Z0^2 I0).

K9–K17 prove `||z(tau)||^2->V` and `||F_tr z(tau)||^2->V` as
|tau|->infinity, together with a uniform norm bound. They use the prior
source-measure absolute continuity; this spectral premise is needed for
the transverse limit, not for Q1–Q27.

Fix 0<eta<1/4. For any real tau_lambda with |tau_lambda|<=lambda^(-eta) and
|tau_lambda|->infinity, put t_lambda=tau_lambda/lambda. Then

    ||w_phys,lambda(t_lambda)||^2/lambda -> V,
    ||F_tr w_phys,lambda(t_lambda)||^2/lambda -> V.          (Q28)

In particular this applies to tau_lambda=+/-lambda^(-eta), at physical
time t_lambda=+/-lambda^(-1-eta). The proof uses the L2 part of Q27, the identity
`W_lambda=lambda^(-1/2)T_lambda w_phys,lambda`, the isometry of X4,
and that F_tr commutes with this K-only rescaling. For example the
difference of squared norms is bounded by
`||W_lambda-z||(2||z||+||W_lambda-z||)`. K's uniform norm bound and
Q27 make it vanish along the simultaneous schedule. The projected
estimate is identical. The exceptional kappa=0 fiber was already handled
in K's global theorem; no new uniform spectral decay near zero is assumed.

These are comparison-correction norms, not occupations or probabilities
of the total normalized state. The exact comparison remains
`P exp(-itH0)phi_lambda/n_lambda`, using the initial global n_lambda.
Cross terms with it have not been discarded for any total-state observable.
Q28 strengthens the earlier ordered norm limits on this specific proved
window while leaving their source and physical interpretation unchanged.

## 7. All nine actual current expectations on the H1 window

Use exactly X25's complete bracket R_ab, with every B12–B13 rank term.
On the fixed rescaled support, X26–X29 give

    Q_lambda,ab=C_ab(lambda kappa)
                   +[A_b(lambda kappa)/lambda]partial_a,
    Q_0,ab=delta_ab H_*(L_b-I)+kappa_b[H_*,L_b]partial_a,
    L_b=P cos(2q_b)P+|v_b><v0|+|v0><v_b|,
    v_b=sin(q_b)T_b,    v0=sum_j sin(q_j)T_j,
    Q_0,ab z=H_* L_b partial_a(kappa_b z),
    <z,Q_0,ab z>=0.                                      (Q29)

The last pairing is exact for every time. It does not say the vector
Q_0,ab z vanishes. Both exact and limiting forms are symmetric on compact
H1 sections, by X27–X28; in particular this applies when a differs from b.
No input q derivative occurs in the bounded coefficient normal form.
Since ||H_*||<=2sqrt(3) and ||L_b||<=1+sqrt(3), its constant coefficient
has norm at most 6+4sqrt(3)<13, and its derivative coefficient on
|kappa|<=1/4 has norm at most 3+sqrt(3)<13. Therefore

    ||Q_0,ab u||_2<=13||u||_(1,Sigma),
    ||(Q_lambda,ab-Q_0,ab)u||_2
                              <=22lambda||u||_(1,Sigma). (Q30)

Here the second constant can be checked directly from the supplied
trigonometric formulas, rather than treating coefficient convergence as
an unquantified limit. For any unit K directions v,w, those formulas give
the global bounds

    ||H_D||,||H_Delta||,||h||<=4,
    ||partial_v H_D||,||partial_v H_Delta||,
       ||partial_v h||,||h_b||<=1,
    ||partial_v partial_w H_D||,||partial_v h_b||<=1/2,
    ||partial_v partial_w h_b||<=1/4.

Every directional K derivative of H0 of order n>=1 is bounded by 2^(1-n),
by the Pauli norm and the componentwise product bound. These inequalities
also apply to h=H0c and its derivatives; P is fixed and contractive.
For J_b in B9 they imply ||J_b||<=9, ||partial_v J_b||<=7 and
||partial_v partial_w J_b||<=6. Twice differentiating A_b=[H_D,J_b]
thus gives

    ||partial_v partial_w A_b||
          <=2[(1/2)9+7+7+4(6)]=85.

For C_ab, use the complete B13 normal form. The directional derivative of
its diagonal multiplier has norm <=6. The first two contact terms give
<=13/2. The H_D F_b,a term gives <=26, since ||F_b,a||<=6 and
||partial_v F_b,a||<=5. To check the remaining four ranks with no hidden
operator domain assumption, B7 only acts on its displayed smooth factors:

    ||partial_qa h||<=2,  ||partial_qa h_b||<=1,
    ||partial_qa partial_v h||<=1,
    ||partial_qa partial_v h_b||<=1/2.

It follows that (norm, first-K-derivative bound) for
L_a h_b, L_a h, L_a^dagger h, L_a^dagger h_b are, respectively,
(3,5/2), (8,6), (4,3), (2,3/2). Product differentiation of their four
ranks gives 13+10+5+8=36. Consequently
`||partial_v C_ab||<=6+13/2+26+36=149/2<75`, uniformly in all a,b.
All these are bounds for bounded fiber operators, since L_a and its
adjoint were applied only to known form factors. Taylor's formula along
K=lambda kappa, with A_b(0)=0 and
`D A_b(0)[kappa]=kappa_b[H_*,L_b]`, gives coefficient differences
at most 75lambda/4 and 85lambda/32. Their sum is 685lambda/32<22lambda,
proving Q30. The use of q derivatives in this finite list of smooth
form factors does not differentiate zeta or any input field.

Define the following fixed positive constants, all independent of T and
lambda:

    A0=d0 m=c0 m/(Z0 sqrt(I0)),
    Z1=A0(3L+10),
    C_D0=M(3K_R+1),
    C_mean=768(1+A0+C_D0)+26 C_D0 Z1+13 C_D0 C_*
                       +22(A0+C_D0)(Z1+C_*).             (Q31)

For s_T=1+T, the pointwise K8 estimates used in Section 3 imply
`sup||z||_2<=A0` and `sup||z||_(1,Sigma)<=Z1 s_T`. Q25 and Q1 imply
`sup||D_lambda||_2<=C_D0 sqrt(lambda)s_T^2` and
`sup||D_lambda||_(1,Sigma)<=C_* sqrt(lambda)s_T^3`.
Thus W_lambda=z+D_lambda has the corresponding sum of these bounds.

The exact X31 free-comparison estimate, including its contact subtraction,
eta_contact<=lambda^(3/2)/4, B_a<60 and n_lambda>=1/2, gives

    ||R_ab v_lambda(tau/lambda)||
                      <=384lambda^(3/2)s_T,
    ||v_lambda(tau/lambda)||<=2.                          (Q32)

Indeed its right side before rounding is
`8lambda^3+lambda^(3/2)(376+6T)`, which is <=384lambda^(3/2)(1+T)
for lambda<=1. The exact X33 pairing is valid at each finite lambda and
time; high Sobolev bounds need not be uniform. Applying it in X34, the
free expectation divided by lambda is bounded by 768sqrt(lambda)s_T,
and the two cross terms together by
`768lambda s_T[A0+C_D0 sqrt(lambda)s_T^2]`.

For the remaining pairing, use symmetry as in X35 and the zero Q29:

    <W,Q_0,ab W>=<D_lambda,Q_0,ab W>
                         +<Q_0,ab z,D_lambda>.

Q30 bounds this by
`26 C_D0 Z1 sqrt(lambda)s_T^3+13 C_D0 C_* lambda s_T^5`.
The coefficient-difference pairing is bounded by
`22lambda[A0+C_D0 sqrt(lambda)s_T^2]
          [Z1 s_T+C_* sqrt(lambda)s_T^3]`.
These inequalities use the smaller L2 error in the symmetric pairing;
they do not replace both factors by H1 bounds. Expanding the last product,
using lambda<=1 and s_T>=1, and collecting the displayed constants proves
for every a,b in {1,2,3}

    sup_(|tau|<=T) |<psi_lambda(tau/lambda),
                       R_ab psi_lambda(tau/lambda)>|/lambda
       <=C_mean[sqrt(lambda)(1+T)^3+lambda(1+T)^5].        (Q33)

This is O_T(sqrt(lambda)) after division by lambda, hence an actual
expectation bound O_T(lambda^(3/2)) at fixed rescaled T. For every fixed
0<eta<1/6, substitution of T=lambda^(-eta) gives the simultaneous result

    sup_(|tau|<=lambda^(-eta)) |<psi_lambda(tau/lambda),
                       R_ab psi_lambda(tau/lambda)>|/lambda
       <=C_mean[8lambda^(1/2-3eta)+32lambda^(1-5eta)] ->0. (Q34)

Both exponents are positive in the stated window. The result is uniform
in all nine components, and includes physical times up to
|t|=lambda^(-1-eta). It concerns the actual normalized total-state
expectation with its free, cross and correction terms all retained.
It does not strengthen Q34 to the wider L2 norm window eta<1/4, does not
claim the residual vector tends to zero, and does not assert a full boost
algebra or a covariance law.

## 8. Preserved failures, checks and limits

The full-inverse shortcut fails even for the actual initial residual.
At t=0, z=0 and, wherever a(0,kappa)!=0,

    r(0,kappa)=-c0 a(0,kappa)
                  [2epsilon-1/(2I0 epsilon)]n.

Any singlet coefficient producing this triplet under H_* would equal
`-c0 a(0,kappa)[1-1/(4I0 epsilon^2)]`. It is not L2, since near a cone
epsilon is comparable to |q| and the integral of epsilon^(-4) diverges.
Triplet input contributes only to the singlet output, so it cannot repair
this coefficient.
Thus this residual need not lie in ran H_* even though it lies in the
orthogonal complement of its kernel. Approximate range vectors, with
diverging norms and vanishing errors, are the operative construction.

The first root proposal's cone constants, mean-subtracted corrector and
noncommuting Duhamel route survive the derivation. The corrector norm is
improved by the orthogonal projection. Its complete original exponential
proof, with all prior controls, was preserved before the later refinement
was read: `boost_hstar_quantitative_corrector/EXPONENTIAL_BOUND_PRE_REFINEMENT.md`,
SHA-256 `50ceee39e4a7364bb2b616ce09b741101492a9639e91ad0a2776c66c8b7a4ce9`.
The later root proposal is realized here by a direct K8 fiber estimate and
the full transverse block integral, removing the exponential factor.
The source phase derivative, both corrector endpoints, x_s, V_lambda x,
the full differentiated error and both global normalizers are retained.
No q derivative of an input field or zeta appears. H_* remains gapless.

The preceding mixed-band counterexample, differential-bracket obstruction,
small fixed-time diagonal norm obstruction, cone-driven failure of
operator-norm averaging and finite-bath recurrence remain valid in their
stated scopes. Q1 exploits the particular residual's weighted regularity;
it is not a uniform theorem on the complementary Hilbert unit ball.
No optimal convergence exponent, full boost algebra, physical covariance,
Hamiltonian selection, Markovian law or total-state occupation is proved.

`boost_hstar_quantitative_corrector/AUTHOR_CHECK.md` records the distinct
algebraic arrangements, direct Pauli controls, analytic cone and source
constant checks, real executions and preserved failures. These are author
checks, not a fresh-context independent scientific review. Finite matrices
do not certify cone estimates or the continuum theorem. The proofs of
Q4–Q7 and Q8–Q34 are analytic and explicitly state their hypotheses.
The mathematical tools used are bounded-operator ODEs, elementary sine
remainders, Hilbert-space projection, radial integration, unitarity and
integration by parts; no niche external theorem is imported.

The selective source check addresses the global Q4 constraint, cone multiplicity,
corrected range identity, weighted derivative estimates, all source approximations,
both endpoints and the noncommuting term in Q21, the constants and limit order
in Q25–Q28, and the all-index coefficient bounds and complete expectation
decomposition in Q29–Q34. REVIEW_HISTORY.md records its final scope and verdict.
The [finite control](../scripts/boost_quantitative_corrector_2026_10_12.py)
contains all three complete original control sources in separate functions;
PUBLICATION_EDITS.json and PRIMARY_COMPOSITION.json recover every byte.
No Lean certificate, physical-axiom change, editable-prompt change, retained
status or applied audit verdict is claimed. Root is a coauthor, not the
independent reviewer. DELIVERY_CHECKS.md records publication verification.
