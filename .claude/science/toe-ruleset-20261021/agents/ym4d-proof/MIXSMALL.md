# MIXSMALL — real mixed groups, normalizer jets and their unpaid reader costs

**The all-history local mixed-group estimate is OPEN.** This note proves
finite-order local kernel/positive-integral bounds in REALRGA's derivative
units, a small mixed-group theorem for fixed gap events under the actual
conditional product kernel, and a full-order extension of the filled-flux
creation estimate. It does not identify that product law with the inherited
interacting reference. A concrete SU(2) field shows why an unpaid uniform
fine-field derivative bound for an individual kernel normalizer is false.
The fixed-hole transfer can also be sharpened without acquiring derivatives.

PROVEN means the displayed mathematical assertion under its stated
hypotheses, ARGUED a proposed construction, and OPEN an unmet model estimate.
These are author statuses, not audit status or a Yang–Mills existence/mass-gap
claim. The source revision and verification limits are in
[MIXSMALL_LOG.md](MIXSMALL_LOG.md); the primary input hashes are in
[the manifest](checks/mixsmall_input_sha256.txt).

Credit: Tadeusz Balaban's large-field organization, Jonathan Dimock's
[large-field exposition](https://arxiv.org/abs/1212.5562), and Brydges–Slade's
[normed-algebra methods](https://arxiv.org/abs/1403.7244). Literature is
attribution only. Every lemma used below is rebuilt; no memory-only [m]
statement carries proof weight.

## 1. Exact objects and quantified target

Use the supplied finite periodic four-dimensional SU(N) model, N>=2, odd
L>=3, probability Haar, u_j>0, t_j=kappa u_j and the actual paired contours:

    M_c=(24 L^4)^(-1) sum_(sigma,y in B(X))
          P^sigma(c_X,y) S_y P^sigma(c_(X+e_mu),y+L e_mu)^*,
    h_M(W)=Re tr(W* M)/N,
    Z_t(M)=int exp(t h_M(W))dW,  k_t(W;M)=exp(t h_M(W))/Z_t(M).       (MS1)

The same coordinate order is used in both P paths, c_X is the centred
root, and the straight leg S has L links. A contour has at most
ell=5L-4 link occurrences in the two endpoint blocks. Therefore ||M||<=1.
The actual RG numerator/reference remain

    R_h(V;J)=int rho_(j,h)(U;J) K_j(V,U)dU,
    Z_A(V)=int chi_A(U) b_j(U) K_j(V,U)dU,
    Q_h=R_h/Z_A,   b_j=exp(-u_j sum_p s(U_p)),
    s(W)=1-Re tr(W)/N.                                           (MS2)

rho contains the complete earlier chain, failures AND absences. It is not
b_j. Conditional history probabilities retain their original mass outside
them exactly once. Zero fibres are never divided by. All current outcomes
are summed unless a fixed-sector representation is explicitly stated.

Use REALRGA RGA3/RGA4: total fine-plus-coarse order p=6, source order q=4,
or the explicitly displayed finite q generalization; max-link direction
weights h_l=sqrt(N/u_l), fixed original-source weights r_a, ordered
derivatives, and complete connected original reader supports. Thus the
largest total order needed initially is ten, not four. No conversion from
REALRGB's l1 direction norm is made without its coordinate costs.
Sources here are original absolute action-coefficient increments J_p in
sum_p (u_0+J_p)s_p; all kernels/couplings are frozen when taking these
derivatives. For the relative coordinates epsilon_p of REALRGB,
J_p=u_0 epsilon_p and weights/derivatives transform by that exact map.

The target is the complete integrated coefficient bound

    sup_D T^(6,4)(A_I) <= product_(i in I) alpha_i,
    sup_x sum_(i:x in H_i) exp((mu+2)|H_i|) alpha_i <=1/4,           (MS3)

with exact overlap-component factorization on the SAME reference as MS2,
uniform in the declared volumes, depth, histories and holes. Smallness per
connected group is only one part of MS3: complete support/entropy and the
sum over types still have to be paid. FR, KR and TC supply only their
stated domain, interaction/prefactor and original-law interfaces; none is
extended here to arbitrary histories. Extracted continuation is EXTCONT's
task. No approved framework primitive supplies or is claimed to obstruct
these dimensionless analytic estimates.

## 2. Finite real jets of a positive integral — PROVEN

Let Z(y)=int_E w_0(x) exp(H(y,x))dx>0, with fixed nonnegative w_0 and fixed
measurable E. Assume dominated differentiation on compact subsets of the
open real parameter domain. Every direction below already includes its
REALRGA fine/coarse/source weight. Suppose, for all ordered derivative
words of length r<=p+q, |D_I H|<=b_r. This is an explicit score hypothesis,
not a consequence of positivity. Define nonnegative polynomials

    M_0=I_0=C_0=1,
    M_m(b)=sum_(pi partition [m]) product_(B in pi) b_|B|,
    L_m(b)=sum_pi (|pi|-1)! product_(B in pi) M_|B|(b),
    I_m(b)=sum_pi |pi|! product_(B in pi) M_|B|(b),
    C_m(b)=sum_(r=0)^m binom(m,r) M_r(b) I_(m-r)(b).                (MS4)

The logarithmic bound starts at m=1. Ordered differentiation gives

    |D_I Z|/Z <=M_m(b),  |D_I log Z|<=L_m(b),
    Z |D_I Z^-1|<=I_m(b),
    |D_I n_y(x)|<=n_y(x) C_m(b),  n_y=w_0 exp H/Z.                 (MS5)

Proof: differentiating exp H assigns each new position either to an old
block or a new block of a set partition; order inside a block is retained.
Dividing the integral by Z gives an expectation under its positive law.
For log and reciprocal derivatives the partition coefficients are
(-1)^(r-1)(r-1)! and (-1)^r r!, respectively. They follow inductively
from D log Z=DZ/Z and D(ZZ^-1)=0; no derivatives are commuted. Leibniz
then proves the density bound. At zeros of w_0 all derivatives vanish;
no log of w_0 is required. There is no inverse rare-sector mass in MS5.

For positive N,D satisfying the same score upper bounds, the same argument
gives |D_I(N/D)|<=(N/D) C_m(b). Different score arrays can be used in
the two factors of the convolution. Hence a separately proved scalar
bound sup N/D<=e^(-tau n) implies

    sup T^(p,q)(N/D) <= Q_(p,q)(b) e^(-tau n),
    Q_(p,q)(b)=sum_(a+b<=p,c<=q) C_(a+b+c)(b)/(a! b! c!).           (MS6)

The b used as a derivative count in this sum is distinct from the score
array b_r. For labelled sources replace the c sum by a sum over subsets
of the labels, using their exact weights and no 1/c! or 1/q!. MS4 with
word-specific bounds proves that version too. In particular all fifteen
nonempty subsets of four labels survive.

For signed insertions use the stronger direct integral statement, rather
than calling a signed connected coefficient positive:

    T_y int_E F_y n_y dx <= int_E T_y(F_y) T_y(n_y)dx.               (MS7)

Leibniz and the downward-closed Taylor index set prove the product
inequality in MS7, followed by differentiation under the integral and the
triangle inequality. Taking suprema after this step retains the
differentiated reference. Moving hard cuts are excluded: their boundary
derivatives must first be proved or the alternatives summed. These proofs
extend REALRGB G7/G8 to the necessary finite orders and ordered direction
units; they do not supply the scalar hypothesis or a spatial decay sum.

## 3. Local soft-kernel normalizers, including fine-input derivatives

**PROVEN, with explicit coupling dependence.** For unit fine directions
on the current level put lambda=ell h_j. Differentiating a path product
of at most ell unitaries gives at most ell^r terms for a word of length r,
each bounded by h_j^r. Inverse link occurrences obey the same bound;
repeated hits on one link retain their order. Averaging the actual
24L^4 paths does not multiply this bound. Consequently

    ||D_I M_c|| <=lambda^r,
    |D_I(t h_(M_c)(W))|<=t lambda^r.                              (MS8)

Write M_m(t), L_m(t), I_m(t), C_m(t) for MS4 with every b_r=t. Each is a
polynomial in t of degree at most m, with nonnegative coefficients. For
all real fine fields, including M=0, positivity and MS5 give

    |D_I log Z_t(M_c(U))|<=lambda^r L_r(t),
    |D_I log k_t(W;M_c(U))|<=lambda^r [t+L_r(t)].                  (MS9)

The support is precisely the full contour reader, independent of the
ambient volume. This is a local finite polynomial bound, not a small
coupling-uniform bound. Retained output derivatives can be included by
replacing lambda by ell h_j+h_(j+1) for the numerator; Z has no output
dependence. Original-source derivatives of a kernel are zero. Earlier
kernels, external plaquettes and inherited density factors have to be
included if they read the differentiated variables.

A fixed-sector local normalizer with a complete smooth exponent H obeys
MS5 with its ACTUAL b_r. For example, every external Wilson plaquette
with coefficient c contributes at most |c|(4h_max)^r; a source derivative
contributes its exact coefficient-direction sum, with the remaining field
derivatives paid on that plaquette. Each read kernel contributes MS9.
Unexpanded inherited densities require either their own score bound or
opening their full ancestry; its reader count is not replaced by a
one-step cell count. Thus D_h/N_h at frozen exterior data have finite
relative estimates, while all-history local prefactor budgets stay OPEN.

At first order one can also compare close real means directly:

    |log Z_t(M)-log Z_t(M')|<=t||M-M'||,
    |log k_t(W;M)-log k_t(W;M')|<=2t||M-M'||.                     (MS10)

The exponent difference is at most t||M-M'|| pointwise, so integrating
the two inequalities e^(-t||Delta||)<=exp(t h_M)/exp(t h_M')<=e^(t||Delta||)
proves the first; add the numerator difference for the second. The crude
bound 4t is recovered when both means have norm <=1. A small seam
comparison needs an actual small mean difference, not merely positivity.

### An actual rough field forbids an unpaid uniform MS9 bound — PROVEN

Fix SU(2), odd L>=3, a fine torus whose side is a multiple of L^2, and
theta=2pi/L^2. In lattice coordinates set

    U_1(x)=diag(exp(i theta x_2),exp(-i theta x_2)),
    U_2=U_3=U_4=I.                                               (MS11)

This is a well-defined periodic field. For a direction-one coarse link
from X=0, the two axial P factors in every paired contour are identical:
the link field is independent of x_1 and the translated paths have the
same ordered steps. Since the matrices commute they cancel. The straight
leg contributes exp(i theta L y_2) in the first diagonal entry. Thus

    M_1=diag(m,conj(m)), m=(1/L)sum_(r=0)^(L-1) exp(2pi i r/L)=0.   (MS12)

Take the fixed fine direction A_1(x)=i h_j ((x_2 mod L)/(L-1))sigma_3,
A_2=A_3=A_4=0. Its REALRGA max-link norm is one. Along U(s)=exp(sA)U,
the paired axial factors still cancel, and

    m(s)=(1/L)sum_(r=0)^(L-1) z^r exp(i s L h_j r/(L-1)),
    z=exp(2pi i/L),
    m'(0)=-i L h_j/((L-1)(1-z)),
    |m'(0)|=L h_j/(2(L-1)sin(pi/L)).                              (MS13)

Here sum r z^r=-L/(1-z), obtained by differentiating the finite geometric
sum before substituting z^L=1. The direction may be set to zero outside
this link's full reader without changing the calculation.

Write W=x_0 I+i sum_(a=1)^3 x_a sigma_a. The coordinates are real and
sum x_a^2=1. Multiplication by the unit quaternions permutes these
coordinates up to signs; Haar invariance therefore gives E x_a=0,
E x_a^2=1/4, and E x_a x_b=0 for a!=b (conjugation supplies the needed
pair sign reversals). For M=diag(m,conj m), h_M=Re(m)x_0+Im(m)x_3.
At M=0 the normalized law is exactly Haar. Twice differentiating Z
therefore gives

    D_A^2 log Z_t(M_1(U)) = t^2 |m'(0)|^2/4
       = kappa^2 u_j L^2/[8(L-1)^2 sin^2(pi/L)],   h_j^2=2/u_j.   (MS14)

The expectation of the term involving m'' is zero. MS14 diverges
linearly as u_j grows even in the prescribed normalized fine directions.
Also psi_M(W)=max h_M-h_M(W)=0 for all W at M=0: no fresh positive gap
can pay this normalizer on that field.

This is an obstruction only to a stand-alone O(1), unregulated normalizer
jet budget on unrestricted real input fields. Its support is a bounded
actual contour reader, not an abstract freely varying matrix. The field
has nonzero 12 plaquette curvature and positive action; one-use original
charges, regulators, integration and cancellations with other factors may
pay its polynomial derivative cost. No failure of MS3, of the actual
matched RG map, or of a small-field nondegenerate kernel theorem follows.

## 4. Actual fresh-gap mixed groups — PROVEN at conditional-kernel scope

Let C be a finite set of output links whose variables W_C are integrated
under the actual product law nu_U=product_(c in C) k_t(W_c;M_c(U))dW_c.
Unread output cells are first integrated to one. Let E_c be fixed measurable
sets on m distinct links of C, with, for every U in the open domain D,

    W_c in E_c implies psi_(M_c(U))(W_c)>=a>0.                    (MS15)

All event boundaries are in integrated variables; there is no derivative
of a parameter-dependent cut. Let f_1,...,f_r be smooth, possibly signed,
small insertions, with complete readers and sup_(U,W,other parameters)
T^(p,q)(f_i)<=s_i. Coarse parameters outside C and original sources may
be arguments of these f_i; they are not arguments of nu_U. Define the
complete conditional mixed coefficient

    A_G(U;J)=int product_i f_i product_(c selected) 1_(E_c)(W_c) dnu_U.

A probability Haar ball of radius zeta<=1 has mass at least
(1+4N/zeta)^(-2N^2): cover the 2N^2 real matrix entries by cubes of side
zeta/(2N), use an occupied representative in each cube, and translate
the resulting group balls using Haar invariance. Since h_M is 1-Lipschitz
in operator distance, a 1/t cap about a maximizer has exponent loss at
most one. For t>=1 this proves, including the complete normalizer,

    P_K(psi>=a)<=min(1,exp(-q_gap)),
    q_gap=t a-1-2N^2 log(1+4Nt).                                 (MS16)

Distinct output kernels are conditionally independent at fixed U, hence
the joint event has probability <=exp(-m q_gap) when q_gap>=0. No
independence of the fine fields is used. To differentiate, write the
product law as exp(H_C)/Z_C with H_C=t sum_(c in C) h_(M_c)(W_c).
Its ordered fine scores satisfy b_l=|C|t lambda^l by MS8. Consequently

    T_f^(p)(nu_U)/nu_U <= D_p(|C|,t,lambda),
    D_p(d,t,lambda)=sum_(l=0)^p lambda^l C_l(d t)/l!,
    sup_D T^(p,q)(A_G)
       <= D_p(|C|,t,lambda) exp(-m q_gap) product_i s_i.           (MS17)

This follows from MS7, the density part of MS5, and the product bound for
the f_i. It differentiates Z_C as well as exp H_C. nu_U is independent
of sources and retained coarse parameters, so their orders stay in the
insertions and do not increase D_p. All fine derivatives through six and
all mixed source derivatives through four are included. The labelled
source version follows by the same subset product argument.

For a group family with |C|<=c m, m>=1 and fixed integer c, the nonnegative
polynomials C_l have degree <=l, so
D_p(|C|,t,lambda)<=m^p D_p(c,t,lambda). Since m<=2^(m-1) and D_p>=1,
one may pay the explicit bill

    d_gap=log(2^p D_p(c,t,lambda)),
    sup T A_G <= product_i s_i exp[-m(q_gap-d_gap)].               (MS18)

For p=6, lambda=ell sqrt(N/u), t=kappa u, fixed N,L,kappa,c and u>=1,
D_p(c,t,lambda) is at most a constant times (1+u)^p; in fact its
monomials grow at most u^(p/2). Thus d_gap=O(log u). A genuine gap
price t a>=c_0 u^delta, delta>0, pays it at large u. If every s_i<=s,
then epsilon=max(s,exp[-q_gap+d_gap]) gives

    sup T A_G <=epsilon^(r+m).                                  (MS19)

This is a constructive mixed-group smallness theorem, uniform in volume
and in frozen input data on D. It is not a norm conversion from a scalar
price under a different law. If |C|<=c m is unavailable, retain MS17 with
the actual reader count; there is no automatic fixed per-event bill.
Here r+m counts atom labels. If a specified complete-support assignment
also proves |H_G|<=c_s(r+m) and epsilon<1, MS19 implies the block-size
bound (epsilon^(1/c_s))^|H_G|. The reader-size estimate and the rooted
type sum are additional requirements; atom-label smallness alone is not
the support-size assertion in the author brief.

The class is nonempty in the actual model. Fix E_c={||I-W_c||op>=d},
0<d<1, and take real fine fields in an open identity neighbourhood with
||M_c-I||<d^2/(8N). Then

    psi_M(W)>=s(W)-2||M-I||>=d^2/(4N) on E_c,

using 2N s(W)=||I-W||HS^2. A max-link identity neighbourhood of radius
less than d^2/(8N ell) suffices by telescoping. At the original step j=0,
for small smooth original source insertions f_i=exp(z_i s(U_(0,p)))-1, put
B_p=2+sum_(l=1)^p (4h_j)^l/l!. The product Taylor inequality gives
T f_i<=exp[(sup|z_i|+r_i)B_p]-1; choose the displayed source window and
fixed weight small enough for s_i<=s. Choosing all their output readers
in the bounded cells of the selected gap links realizes |C|<=c m.
Other small-field factors require their own proven s_i, not this source
example's bound. The domain may depend on the chosen threshold; no
invariant all-history domain or moving-selector theorem is asserted.

### What the inherited law still charges

JMBRA's exact elimination multiplies ALL factors reading a variable before
integrating it; if no factor reads a normalized output, its integral is
one and every derivative of that integral is zero. On the conditional
product law, disjoint complete reader components factor. Integrating
their shared fine ancestors against rho or chi_A b_j can destroy that
factorization. Enlarging a reader support records dependence but does not
make its joint coefficient small.

A nonnegative future reader H changes a single kernel to

    K^H(U,dW)=K(U,dW)H(W)/KH(U),
    K^H(U,E)<=K(U,E) sup H/KH(U).                               (MS20)

H=1_E makes the left side one whenever K(U,E)>0. Thus even an exponentially
small fresh gap can be mandatory under a later selection. For parameter-
dependent H its differentiated numerator and KH also belong to MS7.
MS18's d_gap is not a bound on these extra costs. In MS2 the missing bill
is the matched, jointly differentiated reader/reference ratio, not TV:
the real normalized law already has TV=1.

One-use original plaquette ownership remains exact. If ||I-U_p||>=d,
the fraction theta of its action gives theta u_0 d^2/(2N). Fractions
assigned to all events, regulators and other uses must sum to at most one
on each original plaquette. At later levels b_j(rho/b_j)=rho; pricing
b_j without its compensator changes the law. This is the precise point
where MS17 requires TC/matching input for a general inherited group.

## 5. Filled-flux creation at the full output jet order — PROVEN

This extends a specific CHARGE/REALRGB result; it does not replace a local
reader estimate. Use their fixed original tube E_delta, delta<1/4, about
the four fields g=diag(-1,-1,1,...), U_1(x)=g^(x_2+a), U_2=g^d,
U_3=U_4=I on compatible even tori. Each original 12 plaquette has distance
at least 2-4delta from I, hence S_0>=c_delta u_0 n_0, with
c_delta=(2-4delta)^2/(2N). Here n_0 is the original site count, not a
selector size cutoff; n_j=n_0/L^(4j).

Let Xi_h be any finite disjoint partition or subpartition of the complete
history through U_j, independent of the terminal V. Current outcomes are
summed. Put R_(E,h) in MS2 with E_delta Xi_h inserted. The common source
window is |J_p|<=rho u_0, rho<=c_delta/48. A product identity cap of radius
zeta, with 4zeta below all retained cuts, gives

    Z_A(V)>=exp[-(48u_j zeta^2+8N^2 log(1+4N/zeta))n_j
                       -8kappa u_j n_(j+1)].                    (MS21)

Indeed the cap has 4n_j link masses, s(U_p)<=8zeta^2 on each of 6n_j
plaquettes, and each of 4n_(j+1) kernels is >=exp(-2t_j). The same
normalizers remain present. Bound only the last kernels in R_(E,h) by
exp(2t_j) and define the nonnegative V-independent mass

    m_h=int E_delta Xi_h exp(-S_0) product_(l<j)K_l dU_0...dU_j.

Kernel normalization and disjointness imply sum_h m_h<=exp(-c_delta u_0 n_0).
The real source change costs at most 12rho u_0 n_0. Uniformly in V,

    R_(E,h)/Z_A <= m_h exp[12rho u_0 n_0+d_j n_j],
    d_j=48u_j zeta^2+8N^2 log(1+4N/zeta)+16kappa u_j/L^4.           (MS22)

Supply CHARGE's scalar coupling/cut restrictions: 4<=u_*<=u_j<=u_0,
epsilon_cut,j sqrt(u_j)>=8, zeta=u_j^(-1/2), and j>=j_* chosen so
d_j n_j<=c_delta u_0 n_0/2. This is a hypothesis on the supplied couplings
and depth, not a proved running-coupling flow. MS22 then leaves the
common exponential exp(-c_delta u_0 n_0/4) after summing m_h.

For the full output jet norm, additionally require a uniform upper bound
on h_(j+1), for example u_(j+1)>=u_*; this output-weight condition is
additional to the scalar comparison. Take p coarse derivatives and q
original source derivatives, with fixed sup r_p<=r_* and all earlier
fields integrated. The terminal exponent has coarse word bounds
4t_j n_(j+1) h_(j+1)^l; the original source score is <=12r_* n_0 at
first order and zero at higher pure-source orders. Mixed scores of this
opened exponent vanish. The source-free denominator has the same coarse
bound. Since h_(j+1)<=sqrt(N/u_*) and u_j<=u_0, MS6 bounds the common
jet multiplier by C_(p,q)(1+u_0 n_0)^(p+q). The constant depends on
N,L,kappa,u_*,r_*,p,q, not volume, history, holes or j. Therefore

    sum_h sup_D T^(0,p,q)(R_(E,h)/Z_A)
        <= C'_(p,q) exp(-c_delta u_0 n_0/8),   p=6, q=4.          (MS23)

For the last absorption, use (1+x)^k<=2^k x^k for x>=1 and
sup_(x>=0) x^k exp(-c_delta x/8)=[8k/(e c_delta)]^k.
This also proves the finite labelled-source version, with its fixed
label weights. There are no still-retained fine variables in MS23;
fine/exterior jets of a partly integrated local quotient are not covered.

The sum of history suprema is justified here by the shared m_h envelope,
not by interchanging a supremum and a sum. Weighted type/support costs
must still be bounded uniformly BEFORE this mass sum; an unweighted
history sum does not absorb arbitrary history-dependent readers. For a
localized charged core of m witnesses the same argument leaves
exp(-tau m+d_j n_j), which has an extensive reference debit. It does
not give a volume-uniform local alpha_i. The finite early levels j<j_*
retain MS22. No original charge is spent again as a continuation norm.

## 6. Fixed-hole transfer with real jets — PROVEN implication

Let Gamma have degree at most eight, Lambda be its fixed active set, and
R_Lambda(X) saturate connected X meeting Lambda by the inactive components
it meets or touches, as in LIB1. Regroup K'_Y=sum_(R(X)=Y)K_X, retaining
the inactive family separately. Supremum/triangle inequalities for every
included derivative prove exactly the same bounds for REALRGA jets as
for scalar coefficients. This requires already controlled input jets;
regrouping creates none and differentiating a moving mask is not allowed.

The published bounds remain valid: for holes of size <=M,

    ||K_inactive plus K'||_(mu,p,q)
         <=(1+9M)||K||_((1+8M)mu,p,q).                          (MS24)

At most 8|X| components enlarge X, so |R(X)|<=(1+8M)|X|. For an inactive
output root v, any contributing X meets the closed neighbourhood of its
component H_v, with at most 9M vertices; charge to those input roots.
For active roots the input root is unchanged. This proves MS24, including
the leading one for the unaltered inactive family.

For RD3's one hole H={-1,0,1}^4, its closed neighbourhood has 297 vertices,
and saturation adds at most 81 vertices. RD3 D22/D23 therefore give

    ||K_inactive plus K'||_mu <=730 ||K||_(649mu),
    ||K_inactive plus K'||_mu <=(1+297 exp(81mu))||K||_mu.         (MS25)

All these norms carry the same (p,q) indices. **The second inequality is
at input rate mu, not 649mu.** REALRGA's row 495 quotes it conservatively
at the larger rate; the updated carry-over row below preserves D23's
actual stronger statement.

There is a further sharpening. Every contributing connected X meeting
Lambda meets the EXTERNAL face boundary of H_v: if X meets H_v, follow
a path inside X to Lambda and take its first exit; if X only touches H_v,
the touching vertex is already external. Every external neighbour of an
inactive component is active. Thus only 216=8*3^3 root witnesses are
needed for the one hole, and at most 8M in general. Consequently

    ||K_inactive plus K'||_mu <=(1+216 exp(81mu))||K||_mu,
    ||K_inactive plus K'||_mu <=(1+8M)||K||_((1+8M)mu).            (MS26)

The first statement assumes T>=7 as RD3, so the faces do not identify.
The cases Lambda empty/full are handled by retaining the inactive family
or the identity map. No numerical count is needed for the proof: each
external face has one coordinate +/-2 and three coordinates in {-1,0,1}.

These constants do not become uniform for arbitrary holes. With one active
vertex v and a constant activity a on {v}, connectedness of Gamma\{v}
on a four-dimensional torus makes R({v})=Gamma. The full-norm ratio is
exp(mu(|Gamma|-1)), also for real jets since the activity is constant.
To see connectedness, translate v to zero. From any nonzero vertex retain
one nonzero coordinate while setting a different coordinate to one; keep
the latter nonzero while setting all the remaining coordinates to one.
This gives paths to the all-one vertex avoiding zero on tori of side >=3.
This rules out an arbitrary-coefficient fixed-mu bound for this saturation
map. It does not lower-bound any actual history activity; its mass or a
different support organization may pay the enlargement.

## 7. Failure classes, matching requirements and status of every H clause

### An integrated conditional-Haar failure on actual growing holes — PROVEN

This construction tests a specified expansion, not every matched
representation. Use RD R2/R3 with cut 1 and size threshold 1. For each
m>=1 take a level-one block torus of side T>=m+6 and let Y_m be all
level-zero blocks projecting to C_m={0,...,m-1}^4. In every old block of
Y_m put g=diag(-1,-1,1,...) on the interior direction-one link at local
coordinates (1,1,1,1); put I elsewhere. The incident plaquettes stay
inside their own block, are g or g^-1, and have distance two from I.
All other plaquettes are I. Varying every link by less than 1/16 changes
a plaquette by less than 1/4. Hence the bad set is exactly the connected
Y_m on a positive Haar cap. Its size (Lm)^4 exceeds the threshold,
independently of U_1, and there are no other failures. The actual mask is

    H_1=N_1(pi_0 Y_m)={-1,...,m}^4,  |H_1|=(m+2)^4.              (MS28)

All finite Wilson/kernel factors are positive on this cap. These are
actual positive-mass histories with unbounded holes, even after one step.

Now extract only RD4 C1's mandatory event E=b_(0,Y_m): badness of Y_m
and goodness of its radius-two old-block shell. The size failure makes
E independent of U_1. Its positive Haar mass is factored out once; all
avoidance factors are kept in the residual expansion. The shell projects
inside H_1 because L>=3. Choose the connected H_1 as one conditional
Haar cell, with singleton cells elsewhere, exactly as RD4 C4 permits.
This is a fixed source-free reference nu_E, not the Wilson law.

Choose Q in Y_m and group its interior plaquette action into

    S_Q=sum_(p interior to Q) s(U_p),
    f_Q=exp(-u_0 S_Q)-1,
    A_Q=int f_Q dnu_E.                                          (MS29)

All other Wilson, kernel and avoidance factors remain as their own exact
residual factors; selecting only f_Q gives precisely this coefficient.
Every configuration in E has a bad interior plaquette in Q, so
S_Q>=s_*=1/(2N). Since f_Q is nonpositive,

    A_Q<=-[1-exp(-u_0 s_*)]=-delta_u<0.                         (MS30)

This is a bound on an integrated coefficient, not on a supremum majorant.
Closing its support under the declared conditional cell assigns all of
H_1, so any MS3 majorant for this expansion obeys
Q_Mayer>=exp((mu+2)|H_1|)delta_u. It exceeds 1/4 for sufficiently large
m at every fixed u_0>0.

There is also an explicit mixed small-source reader version. Insert
g_Q(z)=exp(z S_Q)-1, an original coefficient source on this fixed old
block with all kernels held fixed. Its pointwise finite jet norm is as
small as desired when its source window and fixed source weight r are
small; S_Q and its required weighted derivatives are bounded on this
fixed-size block. The selected two-atom coefficient has

    A_(Q,g)(z)=int f_Q g_Q(z)dnu_E,
    -partial_z A_(Q,g)(0)>=s_* delta_u,
    T^[1](A_(Q,g))>=r s_* delta_u.                              (MS31)

Thus the small reader supplies no missing exponentially small cell-size
factor after mandatory conditioning. This is a mixed rough-cell/source
group of the specified exact expansion; g_Q is not asserted to be the
small-field remainder of an optimized RG reference. Absorbing S_Q into
that reference, retaining its unnormalized weight or changing the reader
organization changes MS29 and is not excluded. This is an obstruction to
this conditional-Haar construction's uniform smallness, not to MS3 for
all possible matched constructions.

| Class or attempted inference | Exact finding and scope |
|---|---|
| A required event is a new small atom after conditioning on it | PROVEN failure: for 0<P(E), the mandatory density 1_E/P(E) has L1 norm one. Adding a bounded small insertion f gives E[f\|E], with no second rare-event factor. A source example f=exp(z s_p)-1 on a refined bad-plaquette event s_p>=d^2/(2N) has derivative >=d^2/(2N) at z=0. Extract/charge the mandatory mass once. This refutes that representation's repeated price, not every mixed expansion. |
| Fresh gap prices survive an arbitrary future reader | PROVEN failure of that inference by MS20 with H=1_E; the modified law makes the event certain. Actual selected-reader bounds require the KH and differentiated-reader costs. |
| A one-link local normalizer has O(1) normalized fine jets on every real input | PROVEN false on the actual contour family, MS11–MS14. Polynomial bounds MS9 and a charged rough complement remain viable. |
| Bare direct-Haar supremum activities are small at large u | Technique failure already in JMBRA A23a/REALRGB: one free plaquette has sup\|exp(-u s_p)-1\|>=1-exp(-4u/N). This is a lower bound on that chosen supremum majorant, not on the optimal integrated coefficient. |
| Unabsorbed Wilson-block factors are small on mandatory conditional-Haar cells | PROVEN failure at the integrated level, MS28–MS31, including a small original-source reader. It concerns that exact reference and grouping; adapted interacting references remain live. |
| A whole-volume cap prices a localized mixed return | MS22 with local original charge leaves d_j n_j. The upper majorant is insufficient as volume/core ratio grows; no lower bound on the true activity follows. |
| Fixed-mu hole saturation has an arbitrary-hole uniform operator norm | PROVEN failure for that map on arbitrary activities, section 6. No conclusion about the actual weighted history family follows. |
| Every inherited rough branch earns a fresh gap on return | RENEW's actual coherent flux centres persist through every fixed finite horizon as couplings grow and can have zero new gap. Its original creation charge remains available once. This does not test extracted continuation. |

For a correctly matched local construction the real price must have the
form nu_R=tau-c_ref-c_boundary-d_jet-d_reader-d_regulator, with every
term proved on the same law and no double spending. For bounded full
supports |H|<=c_s n and type multiplicity <=A_type^n, the large-group
root sum is bounded by sum_(n>=1) r_R^n, where

    r_R=A_type exp((mu+2)c_s-nu_R),
    exp(h_sf)h_sf+r_R/(1-r_R)<=1/4,  r_R<1.                     (MS27)

The geometric series proves this sufficient arithmetic once its inputs
are supplied. Long readers instead require their actual summed weighted
supports, including tail roots as in JMBRA A14–A18. MS18 evaluates only
the fresh conditional-kernel derivative part of this bill. MS23 evaluates
one extensive creation family. Neither evaluates the general MS27 tuple.

| REALRGA hypothesis | Status of the actual clause after MIXSMALL |
|---|---|
| H0 exact state | OPEN as a uniform local representation; PROVEN finite replacement/reader integration carries, all scalars and zero fibres retained. MS2 is unchanged. |
| H1 smooth jets/domains | OPEN for selected current histories and invariant domains. PROVEN fixed-sector finite-order estimates in exact (6,4) units, MS4–MS9/MS17; no value-to-derivative or moving-cut inference. |
| H2 regulators/reserves | OPEN for actual mixed all-history integration. PROVEN one-use allocation and the fresh-gap/filled-family instances MS18/MS23; overlap regulator multiplicities and their simultaneous moments still need RGA14. |
| H3 local expansion | OPEN. MS17–MS19 prove a conditional-product-kernel class; no matching all-history factorization, full-reader price or local prefactor budget for MS2 has been supplied. MS14 excludes one unpaid normalizer shortcut. |
| H4 extracted output | OPEN, outside this lane's extraction assignment. The supplied input activity norm must precede MS24–MS26; fixed-hole regrouping does not construct it. |
| H5 transition | OPEN, assigned to EXTCONT together with the relevant operator construction. Fresh prices and creation envelopes are not homogeneous contraction estimates. Arbitrary-hole costs remain explicit. |
| H6 source/consumer records | OPEN for uniform/all-order consumers. Finite marked-jet identities and original-source units carry; the q=4 work supplies no all-n bound, matching coefficient or common continuum limit. |

## 8. Updated REALRGA carry-over rows for consumed results

These rows are replacements at the stated scopes, not edits to the source
files or promotions of their original OPEN clauses.

| Consumed result | Updated disposition and exact cost/obligation |
|---|---|
| REALRGA RGA-P/Z/I | CARRIES; MS4–MS9 instantiate all required finite derivative orders for fixed complete local integrands and kernel means. Positivity alone supplies no local rooted sum. |
| REALRGA RGA-C/H0–H6 | CARRIES as conditional contract. MS3/MS27 for the inherited matched law remain OPEN; no change to extraction/consumer hypotheses. |
| REALRGB G-POS/G-JET/G-SOFT | CARRIES at its frozen-exterior, four-derivative l1 scope. Full (6,4) ordered units require MS4–MS9, explicit local coordinate counts and fixed selectors; global l1 constants are not l-infinity bounds. |
| REALRGB G15–G19 | CARRIES; MS17–MS18 directly pay differentiated normalizers in a fixed-event product-kernel class. Future tilts, rough branches and matched reader ratios still NEED REWORK. |
| REALRGB G23–G29 | CARRIES; MS21–MS23 add full coarse/source order (6,4) and a justified unweighted sum of history suprema for the same filled family, with the displayed uniform output-weight bound. No retained fine/exterior jets or localized-core estimate is obtained. |
| CHARGE C5–C12 | CARRIES with its scalar coupling/cut/depth hypotheses and one original reserve. MS23 strengthens its output jets after all fine fields are integrated and with a uniform output-weight bound. |
| CHARGE C13–C14,C24–C26 | Local/matched joint prices and extracted/common-envelope clauses NEED REWORK. The extensive local-core debit and coherent versus creation distinction survive. |
| JMBRA A3–A12, clause 1 | CARRIES exactly before logs: multiply every reader, preserve rho/b_j, integrate unread normalized outputs first, and keep surviving local/reference denominators. No product structure of nu_A follows. |
| JMBRA A13–A18 | CARRIES as norm-algebra/weighted-reader implications with real jets. Actual joint weights, tail-root sums and two support-rate reserves NEED REWORK. |
| JMBRA A19–A23b | CARRIES at real/conditional scope. Kernel survival, boundary and bulk-source costs remain; MS10 is only a close-mean seam inequality. A23a refutes only its chosen direct-Haar supremum expansion. |
| JMBRB B-RB/B-MASS/B-GAP/B-GEOM | CARRIES. Old mass is invariant; fresh gap prices apply on the forward conditional law, with rough-input alternatives. MS17 provides a fixed-event finite-jet version, not automatic geometric-selector derivatives. |
| JMBRB B-SEAM/B-MATCH/B-JOINT/B-ITER | Real identities and sufficient arithmetic CARRY; complete matched reader and operator estimates NEED REWORK. Include 2 sum\|c_p\| for replaced source-dependent plaquettes and complete kernel costs, not a source-free 2uP when coefficients differ. |
| RENEW R-FLUX/R-TUBE/R-CAP/R-EXACT | CARRIES at finite-horizon/nonuniform-return/exact-algebra scopes. No plain-forward uniform renewal margin is inferred; current outcomes and original mass remain present. |
| RENEW R-WINDOW/R-GROUP | Conditional norm arithmetic CARRIES; actual matched jet continuation remains OPEN for EXTCONT. Creation charges cannot replace insertion-operator bounds. |
| RD3 sections 1–5,7–8 | Fixed positive fibres, exact transfer, mandatory-event diagnostic and matched comparison CARRY. Fixed-sector MS5 bounds relative derivatives; moving selectors, local supported logs and all-history reader prices remain OPEN. Complex germ/TV requirements are OBSOLETE for this real contract. |
| RD3 D22–D23 | CARRIES for already controlled real jets: 730 at input 649mu, OR 1+297 exp(81mu) at input mu, both output mu. MS26 improves the latter to 1+216 exp(81mu). No derivative acquisition or arbitrary-hole uniformity. |
| RD4 C1–C4,L1–L4 | CARRIES: mandatory mass once, positive cells, exact split and matched real ratio. TV=1 removes only the complex TV debit. MS28–MS31 exhibit actual integrated failure for a specified unabsorbed conditional-Haar expansion; the matched construction remains OPEN. |
| RD4 C6–C9,L6–L8,K1–K3,I1–I4 | Algebra CARRIES; actual real joint jets/reader prices and induction NEED REWORK. K2 gets the fixed-mask bounds MS25–MS26 only after its complete input is controlled. |
| LIB1 parts A–C,L3–L15 and full-root correction | CARRIES in real jet-valued spaces for fixed masks. Original cost 1+9M at rate (1+8M)mu is valid; MS26 sharpens to 1+8M with the same input rate. Inactive roots remain in the norm. |
| LIB1 L16 / RD3 Cauchy derivative acquisition | OBSOLETE as a real proof method; the estimate NEEDS REWORK unless input jets are supplied. Fixed regrouping commutes with existing jets but cannot produce them. |

## 9. No-Go Discipline Gate — diagnostic scope, no exhaustion certificate

N1: The distinct explored mechanisms are direct positive score calculus,
fresh-gap conditional integration, original-action creation charging,
matched ancestral integration, and support/mask regrouping. The first
three have the PROVEN scoped results above; the fourth remains OPEN and
the fifth transfers only supplied bounds. They are not five ruled-out
routes. Extracted continuation and localized interacting real references
remain live. This is partial support/narrowing, not a PASS certificate for
a general no-go or a claim of search exhaustion.

N2: There is no asserted count of independent walls. Let J be the complete
matched joint estimate, L the supported local-log budget, S the selected
regularity, and H the actual hole cost. J plus factorization and support
summability implies L by RGA-C; the converse is not established. S is a
premise of J's differentiated representation. H can be included in a
complete J budget or paid afterward when bounded-hole inputs are supplied.
Other non-implications are unresolved. Thus these are overlapping
obligations, not independent obstructions.

N3: Load-bearing hypotheses are explicitly fixed sectors, domination,
positive fibres, weighted score bounds, fixed original sources/readers,
MS15's uniform gap, |C|<=c m, the small insertion norms, the CHARGE
coupling/cut conditions, and fixed-mask connectivity. Inherited-to-product
matching, invariant selector regularity and regulator absorption are not
silently introduced as facts. No new physical axiom is proposed.

N4: Residual matching: RD3 D16 tests normalized mandatory atoms; MS28–MS31
test the specified integrated conditional-Haar block/source atoms; MS20 tests
future-conditioned gap prices; RENEW R-TUBE tests plain-forward fixed-window
curvature return; LIB1/MS26 tests the saturation operator on arbitrary
coefficients; MS14 tests an individual unregulated normalizer derivative.
None is cited as refuting an extracted, charged, fully integrated mixed
activity under the matched Wilson history law. The direct-Haar witness
tests its particular supremum majorant only.

N5: MS14 is per actual contour reader and already concerns a second
derivative; MS17 is per conditional connected group; MS28–MS31 concern
actual growing history cells in one specified expansion; the hole witness
is a full-support operator statement; MS23 is an extensive creation estimate.
No scalar local check is promoted to the lattice-wide all-history MS3.
Numerical controls were NOT RUN and provide no additional resolution.

N6: Retaining mandatory mass, changing a matched reference, integrating a
zero-mean rough sector with its original charge, or replacing the support
organization are mathematical alternatives requiring no new axiom. The
approved units/kinetic-form/realized-state primitives are not analytic
mixed-reader estimates and have not been classified as missing premises.

N7: The strongest live counter-route to any broad negative reading is a
real matched local reference that keeps original masses, absorbs polynomial
normalizer jets into disjoint rough-sector charges, and localizes the
complete differentiated ancestry before taking logs. Its exact terminal
obligation is MS3 with simultaneous reference, regulator and reader costs,
not another scalar gap estimate. RGA14–RGA16 and JMBRA's exact elimination
are compatible with that route. This note has not ruled it out.

N8: The searched source family already separated CHARGE's filled creation
from its extensive local-core debit, REALRGB's relative jets from its
spatial sum, and LIB1's active norm from the corrected full-root norm.
Those repaired distinctions are retained here. MS26 improves a finite
geometry constant, and MS23 legitimately sums a common history envelope;
neither retires the outstanding general matched-reader obligation.

## 10. Verification and the next concrete obligation

The written proofs above carry the author claims. The registered finite
controls are [criteria](checks/mixsmall_criteria.md),
[runner](checks/mixsmall_check.py), and [receipt](checks/mixsmall_result.json).
The sandbox refused `nice`; the runner observed niceness zero and performed
no mathematical checks. Its status is NOT RUN, with an empty check list.
No numerical result, mutation pass or independent computation is claimed.
Fresh hostile review and its exact final source hash are recorded in the
log. Author-assistance reports are not independent review evidence.

**ARGUED next construction:** instantiate MS7 for one bounded mixed core
on the actual all-cut reference, differentiating at least one retained
fine/coarse direction and all four original-source labels while retaining
every completion alternative. Prove a local matched ratio replacing the
extensive d_j n_j and pay its full inherited readers. The gap-only part
has the explicit MS17 bill; the rough zero-mean branch needs its own
one-use charge and reference comparison. Until those parts are joined on
the same law, H2/H3 remain OPEN and no uniform RG induction follows.
