# Nonlinear chart activities at the actual finite-u critical field

This unit proves weak, distinct-vertex Mayer bounds under the **actual
critical Gaussian** on a centered auxiliary chart, including complex
original sources and coarse data, complete coefficient readers, and local
chart failures. It also proves a connected logarithm for a separately
defined **finite-range covariance-core integral**. Restoring the actual
covariance tails to that latter integral is an open interface here.

The actual finite-u critical field, its joint parameter domain and its
covariance decomposition are the already reviewed FU results. IC already
proves the fixed-u parity mechanism and small interacting logarithm in its
own source-free whitened selected sector. Neither result is renamed as a
new discovery. The new steps below are the unwhitened local-vertex envelopes,
active Gaussian marginal estimate, and the stated core integral.

These are bounded one-step results for the supplied Wilson / normalized
paired-S4-prime model. They do not establish the full original-cut return,
arbitrary failure histories, an effective-level identity, multiscale
iteration, four-dimensional continuum existence, or a positive physical
continuum mass gap. Both ultimate physical targets remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual-critical-Gaussian distinct-vertex estimates and a separate finite-range covariance-core chart logarithm with complete readers."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Exact reused inputs and domains

[CB9](COVARIANT_SOFT_BACKGROUND_ASTRA.md) bounds the actual local
vacuum-subtracted Wilson, normalized-kernel and Haar vertices on a fixed
joint analytic chart, uniformly for real u>=1 and fixed real t=kappa u.
The compact normalizer's centered logarithm is included in that proof.
[SA10, SA17](COVARIANT_SOURCE_ACTIVITY_ASTRA.md) give the local Cauchy
majorant and its root / background / fluctuation marking argument.
[IC14--IC20](INTERACTING_SELECTED_CORE_ASTRA.md) hold the actual u, phase,
critical field and Gaussian fixed while introducing an auxiliary Taylor
parameter; their coefficientwise parity argument is reused. IC's product
truncated white law and its exact moment constants are **not** the law
used below. The present correlated marginal estimate is proved in section 5.

Use [FU1--FU28](FINITE_U_CRITICAL_FIELD_ASTRA.md), SHA256
`ecace773f964a18fe6e5c14d46d38913dc52f95afbd2c8763e4766f0c286377d`.
Its [fresh scoped review](REVIEW_FINITE_U_CRITICAL_FIELD_ASTRA.md), SHA256
`fc16733dd459d8915611fb80326d9a523d7cca0c8c85814ff79dd33ceaf9a108`,
accepts the source unchanged and retains its consumer limits. In particular,
replacing delta_hat by delta_V is only a **fixed real-V slice** bound.
All suprema on the joint complex coarse tube below retain
`delta_hat=delta_*+8 eta`. A flat real center does not make its entire
complex neighborhood force-free.

Fix N>=2, D=N^2-1, odd L>=3, T>=2, the admitted compact positive kappa
interval, real u>=N and sigma^2=N/u. Let m0=3L^4+1, n=m0 T^4 and d=Dn.
All d scalar coordinates of the pinned-tree quotient remain; the integrated
tree gauge volume is one. The full phase is

    F_epsilon=F_0+sum_p epsilon_p W_p,
    F_0=sigma^2[-log w_0-sum_free e log j_N(a_e)],
    W_p=tr(2I-U_p-U_p^-1)/2,
    b=b_*(V,epsilon), F_epsilon'(b)=0,
    K_*=F_epsilon''(b), C_act=K_*^-1.                       (NC1)

The normalized Haar constant h_N is outside F. Every compact kernel
normalizer and Haar logarithm remains inside F exactly once. Negative
complex edges use inverses, with the separate forward and backward means;
no complex conjugation or inverse of an arithmetic mean is substituted.

The original parameters vary independently on FU3,
`V_c=exp(v_c)Vbar_c`, max ||v_c||HS<eta, |epsilon_p|<rho, with real Vbar
in FU's curvature class. Retain all FU18--FU19 smallness conditions. There
is a complete-reader atom family for b with V_beta(b)<=tau and

    beta=(16R)^(-4), R fixed independently of u,T,
    alpha=3c0/4, U=c0+d_core+e_lift+t_crit,
    Re C >=alpha I, ||C||op<=U, a_G=alpha/U^2>0,            (NC2)

for every FU27 covariance C. In particular this holds for C_act and for
the core C_loc=c0 I+sum_A D_A(V). The small lift and critical tails are
omitted only in the definition of C_loc, not from the actual model.
The bounds are accretivity bounds on the complex tube, not claims of
positivity for complex coefficients. All radii may decrease below FU's
radii; no larger source/coarse domain or reader rate is asserted.

For precision, the used FU mechanism is: lift principal inverses are
uniformly bounded by weighted conjugation of their accretive finite-range
matrices; a fixed smooth partition gives the positive real whole-matrix
patches D_A and the small commutator tail. Comparing D_A(V) with its real
center costs <c0/8. Each of the lift and critical tails costs <=c0/16 in
the summed absolute row/column norm. Thus Re C>=3c0/4; the inverse identity
`Re C^-1=C^{-*}(Re C)C^-1` gives Re C^-1>=a_G. The full reader sums and
the critical-field source Hessian term were paid in FU, not dropped here.

## 2. Original vertices and their centered coefficient families

Let v run over the **original** local phase vertices: 6L^4 Wilson, four
normalized-kernel and m0 Haar vertices per original coarse block. Combine
the Wilson source with its own vertex, `(1+epsilon_p)W_p`; do not introduce
a second copy of its field stencil. A vertex reads a set L_v of free links;
I_v includes all D colours on those links. The actual counts from CB9 are

    |I_v|<=q=(8L^4+8)D,
    #{v:i in I_v}<=d_inc=15,
    v0=9L^4+5, s0=9^4, d0=v0 s0.                         (NC3)

The 15 counts six Wilson, eight kernel and one Haar term. Use a connected
radius-four original-block root label S_v containing every field endpoint,
coarse datum (both ends of each coarse link), and original source reader.
There are at most d0 root labels at a marked block. Periodic incidences and
all colours are counted; small tori reduce distinct labels, not coefficients.

For each original vertex define, with u held fixed,

    R_v(z)=sigma^-2[F_v(b+sigma z)-F_v(b)
                    -sigma F_v'(b)z-sigma^2 F_v''(b)[z,z]/2],
    J_v,l(z)=F_v^(l)(b)[z^l]/l!,
    R_v=sum_(l>=3) sigma^(l-2) J_v,l,                       (NC4)

on the common Taylor domain. The local first jets are generally nonzero;
only their sum vanishes. The sum of the second jets is exactly K_*.
Constants, first jets and second jets are subtracted in every vertex
before estimating it. Their values remain in the complete action and
Gaussian factor in section 8.

Let a,H be FU's common fine scalar analytic radius and vacuum-subtracted
vertex bound, with the separate Wilson bound included. Put
`f(t)=H(1-t/a)^(-q)`. Expand each original vertex at fine field zero before
substituting b's complete-reader atoms. This gives homogeneous polynomials
J_v,l;S of degree l, whose field variables are still only I_v and whose
coefficients read precisely their connected label S, including S_v. Let
j_v,l;S be the supremum of their absolute scalar monomial coefficient sum
on the projected joint original-data domain. Supremum is inside every sum.
The Cauchy and marking estimates are

    sup_v sum_S exp(beta|S|) j_v,l;S
       <=A_l:=(1+rho)exp(beta s0) f^(l)(tau)/l!,
    sup_x sum_(v,S containing x) exp(beta|S|) j_v,l;S
       <=B_l:=d0(1+rho)exp(beta s0)
                         [f^(l)(tau)+tau f^(l+1)(tau)]/l!. (NC5)

Here is the complete mark count. Cauchy's coefficient bound H a^-j and
the q-slot monomial count sum to f. A mark in S_v costs d0. A mark in an
attached b atom costs its full marked vector sum, at most tau; differentiating
the positive majorant chooses that attachment. For a fixed attached scalar
slot, at most 15 original vertices use it, and d0 overcounts this incidence.
This proves the second term in NC5 without treating b as independent data.
No whitening atoms occur: z still enters the original local field stencil.

Choose a fixed r0<=min(a/8,1), so tau+r0<a/2. For 0<r<=r0 define positive
coefficient families, grouped by complete reader union,

    a_v,S=sum_(l>=3) r^(l-3) j_v,l;S,
    o_v,S=sum_(odd l>=3) r^(l-3) j_v,l;S,
    e_v,S=sum_(even l>=4) r^(l-4) j_v,l;S.                 (NC6)

Uniform weighted masses and marked masses are bounded respectively by

    A3=(1+rho)exp(beta s0) f'''(tau+r0)/6,
    B3=d0(1+rho)exp(beta s0)
                         [f'''(tau+r0)+tau f''''(tau+r0)]/6,
    A4=(1+rho)exp(beta s0) f''''(tau+r0)/24,
    B4=d0(1+rho)exp(beta s0)
                         [f''''(tau+r0)+tau f'''''(tau+r0)]/24. (NC7)

Taylor's integral remainder bounds the positive sums in NC6 by these
derivatives. The odd family is bounded by A3,B3 and the even family by
A4,B4. Set A=max(1,A3,A4). All these constants are finite, uniform in u,T
and fixed before r is chosen. The labels and formulas are functions of
actual V,epsilon and agree on overlapping coarse charts.

## 3. A chart regulator and full-reader Mayer envelopes

Write p=r/sigma and take the centered product of complete colour balls

    D_p=product_free e {||z_e||HS<=p},
    chi_e=1_(||z_e||<=p), chi_v=product_(e in L_v) chi_e,
    P_k(v,z)=sum_(i in I_v)|z_i|^k.                       (NC8)

If chi_v=1, every monomial of degree l obeys
`sigma^(l-2)|z^nu|<=sigma r^(l-3) P_3(v,z)`. Therefore each R atom has
the envelope `sigma a_v,S P_3`. In particular

    |R_v|<=sigma A3 P_3(v,z),
    sum_v |R_v|<=A3 d_inc r sum_i |z_i|^2 on D_p.          (NC9)

NC5--NC7 also give its full weighted and marked coefficient envelopes.
These estimates include the finite-t normalizer and Haar vertices; they
are not estimates for a tree-phase substitute.

Define the zero-extended Mayer function
`f_v=chi_v[exp(-R_v)-1]`, and expand the exponential in the R atoms.
All atoms of f_v carry the same local cutoff chi_v. Products at one vertex
have connected reader unions because every factor contains S_v. Outside
chi_v's set define each atom to be zero; no analytic continuation in z
outside the local chart is used. Coefficient holomorphy in V,epsilon is
preserved because the cutoff and p are independent of those parameters.

For positive reader families, `*` denotes convolution with union of labels.
Repeated labels may be kept or summed. Define

    w_v=sum_(k>=1) a_v^(*k)/[k(2A)^(k-1)],
    W0=2A3, W1=2B3.                                      (NC10)

Then for every resulting label S,

    |f_v;S(z)|<=chi_v sigma P_3(v,z)
                         exp[2A sigma P_3(v,z)] w_v,S,
    sup_v sum_S exp(beta|S|) w_v,S<=W0,
    sup_x sum_(v,S containing x) exp(beta|S|) w_v,S<=W1.    (NC11)

To prove the individual envelope, set Y=sigma P_3 and use
`Y^(k-1)/(k-1)!<=(2A)^(-(k-1))exp(2AY)` in the k-th exponential term.
For its weighted mass, union weight is at most the product weight and
A3/(2A)<=1/2. For a support mark there are k choices of a factor; this
cancels the k in NC10 and gives the geometric sum <=2B3. Thus NC11 is
a sum of **individual coefficient suprema**, not a pointwise supremum of
an already summed expression. Every nonempty w label retains all readers.

## 4. Parity without varying u

Hold u, F_epsilon, b, K_*, the Gaussian and p fixed. Equivalently introduce
an auxiliary lambda in NC4 in place of sigma and evaluate lambda=+sigma
and -sigma on the same chart. The coefficients do not change with lambda.
Homogeneity gives `R_v(-lambda,z)=R_v(lambda,-z)`. This is IC's fixed-u
mechanism, now for the actual joint source/coarse coefficients without
whitening. It is not an expansion obtained by varying u through the center
or the finite-t normalizer.

Let R_o and R_e be the odd and even parts in z. On chi_v=1,
`|R_o;S|<=Y o_v,S`, `|R_e;S|<=Z e_v,S`, where
Y=sigma P_3 and Z=sigma^2 P_4. The Mayer parts are exactly

    f_v^o=-chi_v exp(-R_e) sinh(R_o),
    f_v^e=chi_v[exp(-R_e) cosh(R_o)-1].                   (NC12)

This identity holds atom by atom after grouping unions. Define

    r_o=sum_(k>=0) (o_v/(2A))^(*k),
    r_e=sum_(k>=0) (e_v/(2A))^(*k),
    omega_v=o_v*r_o*r_e,
    epsilon_v=sum_(k>=1)e_v^(*k)/[k(2A)^(k-1)]
                              +(o_v*o_v*r_o*r_e)/2.       (NC13)

The k=0 family is the scalar identity with empty label; every final family
in NC13 is nonempty and rooted at S_v. Directly expanding sinh and cosh,
using `1/(k+2)!<=1/(2k!)`, and the same exponential bound as NC11 gives

    |f_v;S^o|<=chi_v sigma P_3 exp[2A(Y+Z)] omega_v,S,
    |f_v;S^e|<=chi_v sigma^2(P_4+P_3^2)
                                   exp[2A(Y+Z)] epsilon_v,S. (NC14)

The individual positive envelope may overcount parity terms; the actual
coefficient on the left retains its exact parity. Safe weighted masses
and full marked masses are

    O0=4A3, O1=8B3+4B4,
    E0=2A4+2A3^2,
    E1=2B4+4A3 B3+2A3^2(B3+B4)/A.                       (NC15)

For example each geometric family has mass <=2 and marked derivative
<=2B_j/A. Marking o_v^2 gives 2A3 B3. Multiplying these bounds proves
E1; the same product rule gives O1. These are complete-reader bounds, not
only parity of the total extensive integral.

Since Z<=rY on chi_v's set, any product over DISTINCT original vertices
has regulator at most

    exp[eta_r sum_(i in I_W)|z_i|^2],
    eta_r=2A d_inc r(1+r).                               (NC16)

Choose r>0 small enough that r<=r0 and eta_r<=a_G/4. This is possible
because A was fixed using r0. This uses FU's interpolated precision a_G,
not the larger real lift precision from PS. The same regulator covers
NC11. Distinctness is essential: no coordinate belongs to more than 15
selected original vertices. Repeating an original vertex arbitrarily
would destroy this degree/incidence count; its own repetitions have
already been resummed in NC10 and NC13.

## 5. Normalized active Gaussian marginals, with determinant cost

Let C be any complex symmetric covariance satisfying NC2, including C_act.
Its normalized real-contour Gaussian is
`dmu_C=(2pi)^(-d/2)exp[-Tr Log C/2-z^T C^-1 z/2]dz`, with the accretive
branch continued from positive real matrices. For any active scalar set I,
integration over the other real variables gives exactly dmu_(C_I), where
C_I is the **principal covariance**, not the inverse of a principal precision.

For real positive C this is ordinary Gaussian completion of the square.
Both sides are holomorphic on the connected domain Re C>0: on compact
subsets, Re C^-1 has a positive lower bound and hence an integrable
Gaussian envelope. The real-matrix identity extends from a real open
polydisc to its complex polydisc and then throughout that domain. This
proves the complex marginal identity and its normalization. It does not
assert an interacting or globally conditioned marginal identity.

With k=|I|, principal compression preserves Re C_I>=alpha and ||C_I||<=U.
Every singular value is >=alpha, so |det C_I|>=alpha^k; also
Re C_I^-1>=a_G. After paying NC16,

    |dmu_(C_I)| exp[eta_r sum_(i in I_W)z_i^2]
       <=K0^k dnu_I,
    K0=max(1,sqrt(2/(alpha a_G))),
    nu_I=product_(i in I) N(0,2/a_G).                    (NC17)

Indeed the remaining exponent is at most -a_G|z|^2/4. All normalized
determinant and colour costs are in K0^k. No volume-sized determinant
bound or force square has been declared canceled.

Let H be a set of distinct free-link cut failures, h_e=1-chi_e. A product
with chi_v h_e vanishes when e is in L_v. Otherwise the active union of
W and H has at most q|W|+D|H| scalars. Under nu, each hard link costs

    nu(||z_e||>p)<=2^(D/2) exp[-a_G p^2/8],
    b_cut=K0^D 2^(D/2) exp[-a_G r^2/(8sigma^2)].           (NC18)

The bound follows by applying exp(a_G||z_e||^2/8) on the failure and
integrating it under N(0,2/a_G); the moment is 2^(D/2).

For all polynomial factors in NC11/NC14 the exponent at one scalar
coordinate is at most 6d_inc=90. In NC14 use
`P_3^2<=q P_6`. Define the fixed finite constants

    M=max_(0<=j<=90) E_(X~N(0,2/a_G)) |X|^j,
    C_NL=q(1+q)(K0 M)^q.                                (NC19)

Expanding a product of P_3 or P_4+qP_6 produces at most [q(1+q)]^|W|
monomials. Independence under nu bounds each by M^(q|W|). Thus for any
choice of one coefficient atom S_v at each distinct original vertex,

    integral |dmu_(C_I) product_(v in W) f_v;S_v
                                      product_(e in H) h_e|
       <=(C_NL sigma)^|W| b_cut^|H| product_v w_v,S_v.     (NC20)

The same bound for prescribed odd/even Mayer parts is

    <=C_NL^|W| sigma^(|W_o|+2|W_e|) b_cut^|H|
           product_(v in W_o) omega_v,S_v
           product_(v in W_e) epsilon_v,S_v.             (NC21)

These are absolute-integral estimates on the normalized **active**
Gaussian. Weighted and marked sums follow by multiplying the individual
envelopes and using NC10/NC15; union weights are submultiplicative and a
marked union is bounded by the sum of its factor marks. All original
coefficient readers survive. No background or source coefficient was
evaluated at a smaller real-data domain for these joint-tube bounds.

For the signed integral in NC21, an odd number |W_o| gives exactly zero:
simultaneously send z to -z. Every covariance Gaussian, ball cutoff and
hard failure is even, also for complex C. Consequently for sigma<=1,
after summing parity choices and coefficient labels one obtains

    |E_C product_(v in W) f_v product_(e in H) h_e|
       <=[2 C_NL max(O0,E0)]^|W|
                    sigma^(2 ceil(|W|/2)) b_cut^|H|.       (NC22)

For a single reader-labelled vertex only its even part remains and its
integrated bound is `C_NL sigma^2 epsilon_v,S`. In contrast, the absolute
integral of f_v is only O(sigma) in general. Parity does not improve that
absolute bound. No independence between distinct vertices is asserted.

## 6. The exact centered chart expansion and its current locality boundary

Because all chi_e are retained, there is an exact finite original-vertex
identity, with absolutely convergent reader sums,

    Z_main(C):=E_C[1_D_p exp(-sum_v R_v)]
       =E_C[product_e(1-h_e) product_v(1+f_v)]
       =sum_(W subset vertices,H subset free links)(-1)^|H|
                    E_C[product_(v in W) f_v product_(e in H) h_e]. (NC23)

On D_p every local cutoff is one and the products agree. Outside D_p
both first products are zero; the zero extensions are well-defined there.
This proves the identity without extending an undefined vertex off its
chart or omitting any cutoff reader. Expanding first, then using the
uncut active marginal, is legitimate. Replacing that marginal by the law
conditioned on every inactive chi_e would be a different operation.

NC20--NC23 apply to the actual covariance C_act. They do **not** yet make
their integrated coefficients functions of only union_v S_v: the principal
matrix (C_act)_I generally reads original data far outside that union.
FU gives complete-reader covariance atoms, but the all-order operation
that incorporates them into these integrals has not been done here.
An undifferentiated moment bound does not pay derivatives of its Gaussian,
normalizer, field cutoffs or moving boundaries. This is the precise
interface left to the covariance-tail return construction.

Without such connectedization, even NC20 only gives an extensive bound
of the form `(1+C_NL W0 sigma)^#{vertices}(1+b_cut)^n` on the absolute
expansion. It cannot be substituted for a volume-uniform connected
logarithm or nonvanishing theorem for the actual centered integral.

## 7. A separate, proved logarithm for the reader-local covariance core

There is a useful positive intermediate theorem without the preceding
locality gap. Define ONLY for this section

    C_loc=c0 I+sum_A D_A(V), Z_loc=Z_main(C_loc).            (NC24)

This is a normalized auxiliary Gaussian integral. Its critical field and
nonlinear vertices are still the actual b and F_v, including sources;
its covariance differs from C_act by both FU tails. We assert no equality
between Z_loc and Z_main(C_act), and no physical prefactor cancellation.

The actual D_A has field endpoints in supp chi_A and all coefficient
readers in the fixed patch S_A. For each vertex root block x_v set
`Q_v=N_(16R)(x_v)` in coarse sup distance, and for each cut link e set
`Q_e=N_(16R)(owner e)`. Replace a nonlinear reader S by S+=S union Q_v.
Use the fixed bounds

    s_c=(32R+1)^4, d_c=v0 s_c, d_h=m0 s_c.                (NC25)

Each Q is connected and has <=s_c blocks. It contains every S_A that
can contribute to a covariance entry with an endpoint in I_v (or in e).
Indeed the field stencil is within radius four of its root, supp chi_A
is within N_(R+1)(Q_A), Q_A has side <=2R, and
S_A=N_(2R+4)(Q_A). Their maximum displacement is <=5R+9<=16R. When
T<16R the allowed whole-torus patch is contained in Q_v and its cost is
still <=s_c. These enlargements are geometry-only, not data selections.

For any set of decorated objects `(v,S+)` and cut objects `(e,Q_e)`,
partition them by overlapping complete labels. Two different components
have zero cross covariance under C_loc: a contributing D_A would put
the same S_A in both Q labels and hence join them. Their active Gaussian
marginal is therefore a direct sum. Each of its entries reads only data
inside its own label union. Its exact normalized determinant, density and
integrals factor by those components. The nonlocal b coefficients cause
no exception: all their readers are already in S. This also handles a
diagonal covariance entry that reads remote original data.

Thus grouping NC23 by those overlap components gives an exact hard-core
polymer gas. A polymer activity w(P) sums connected sets of decorated
objects with union P, keeping the constraint that each original vertex
and cut link is selected at most once. This constraint is dropped only
in positive upper bounds. Disjoint polymers automatically use different
original vertices and links because their labels contain those roots.
Each w(P) is a holomorphic function of original V_P,epsilon_P. The
Gaussian principal marginal, rather than an inverse principal precision,
is crucial to this locality statement.

Set kappa_w=beta/4, a **support-weight margin**, unrelated to the model's
kernel stiffness kappa. The complete decorated-object budgets from NC20
and the single-vertex parity bound are

    h_v=C_NL sigma exp(beta s_c)(W1+d_c W0),
    h_2=C_NL sigma^2 exp(beta s_c)(E1+d_c E0),
    h_h=d_h exp(beta s_c) b_cut,
    h=h_v+h_h,
    h_P=h_2+h_h+h^2/kappa_w.                             (NC26)

The extra mark in Q_v accounts for d_c W0 or d_c E0; a mark in the
original S accounts for W1 or E1. The inflation exp(beta s_c) pays every
new covariance reader. The cut cost pays all free links, with full D
colours already in b_cut. No unit of weight is available for free.

Require `h<=kappa_w/2` and `h_P<=kappa_w/2`. These conditions hold for
all sufficiently large u, with all preceding constants and r fixed:
sigma tends to zero and b_cut is exp(-c/sigma^2) times a fixed constant.
No curvature restriction of the form delta<=sigma p was added. FU's
fixed joint domain, possibly narrowed for chart inclusion, remains.

Here is a proof of the two connected sums at this small rate. Give a
decorated object o its positive amplitude from NC20 and call its label S.
After weighting unions by exp((beta-kappa_w)|union|), bound a connected
collection by all its rooted overlap trees. Their positive recursion is

    T(o)<=v(o) exp[sum_(o' overlapping o) T(o')],
    v(o)=amplitude(o) exp((beta-kappa_w)|S|).              (NC27)

It follows by expanding the exponential into unordered children, with
their factorials; allowing repeated objects only enlarges the sum.
The bound T(o)<=amplitude(o) exp(beta|S|) is stable because the sum over
overlapping children is <=|S|h<=kappa_w |S|. Marking an object whose
label contains a fixed block bounds the rooted polymer sum by h. This
proves absolute convergence at rate beta-kappa_w=3beta/4.

For collections of at least two objects the sharper bound is h^2/kappa_w.
To see it, multiply every positive amplitude by t=kappa_w/h>=1. The
same recursion bounds the full rooted tree sum by kappa_w at t. Its
nonnegative homogeneous terms of degree at least two, at t=1, are at most
t^-2 times that sum. The h=0 case is trivial. Singleton nonlinear
activities instead have the actual signed parity bound h_2; singleton
cuts cost h_h. Consequently

    sup_x sum_(P containing x) exp(3beta|P|/4) |w(P)|<=h_P. (NC28)

For the logarithm, expand the finite hard-core partition function formally
near zero activities. Its coefficient on k polymers is the sum over
connected overlap graphs of (-1)^(number of edges), divided by k!.
Order the edges once. Group graphs by their Kruskal minimum spanning
tree. For a fixed tree, allowed extra edges form a Boolean interval:
an extra edge is allowed exactly when it is no smaller than every edge
on its tree path. Its alternating sum is zero or has modulus one.
Thus the coefficient is bounded by the number of spanning trees.
Apply NC27 a second time to polymers, now with input rate 3beta/4 and
output rate beta/2, spending the second kappa_w. NC28 makes that recursion
stable. Marking one polymer containing the root pays the factorial and gives

    Z_loc=exp[sum_Y H_Y(V_Y,epsilon_Y)],
    sup_x sum_(Y containing x) exp(beta|Y|/2) sup|H_Y|
       <=h_P <= C_loc,1 sigma^2+C_loc,2 b_cut.             (NC29)

The constants on the right are finite and independent of u,T; use
sigma<=1 and b_cut<=1 to absorb h^2. The convergent graph identity near
zero activities extends along their common multiplier to one within
these bounds, proving nonvanishing before taking the logarithm. Infinite
reader sums follow by dominated convergence of their finite truncations.
Uniform active-marginal envelopes prove holomorphy; every coefficient
retains its entire connected original-reader label. This is an O(1/u)
nonlinear core logarithm plus the explicit small but extensive chart-cut
vacuum, all measured in a rooted norm. It is not that theorem for C_act.

If fixed-order original-data derivatives are needed, restrict to half the
FU parameter radii and then to any rate beta'<beta/2. A label Y has at
most q_par|Y| scalar parameters, with q_par=4D+6L^4, and contains all of
their readers. Cauchy radius
`r_par=min(rho/2,eta/(4sqrt(D)))` gives, for k>=1, an anchored k-th
derivative sum bounded by

    k! r_par^-k q_par^(k-1)
       sup_(s>=1)[s^(k-1)exp(-(beta/2-beta')s)] h_P.       (NC30)

The derivative is zero if a requested original reader is outside Y.
Summing all k indices at a separate root mark costs q_par^k and s^k
instead. This is a fixed-order coefficient statement. It does not sum
derivative forests of Gaussian measures or hard surfaces.

## 8. Actual normalization, the translated chart, and open interfaces

Define the centered-contour auxiliary sector by a=b+sigma z, z in D_p.
For real admitted data it is a real sector. If inclusion in the original
cut is required, first impose positive fixed fine-chart and cut margins,
for example with A_box=sqrt(D)tau+r,

    A_box<r_ch, delta_V+4A_box<delta_f<=epsilon_1,
    (5L)A_box<eta_good.                                  (NC31)

These are the actual telescoping margins used by IC for strong-good
inclusion. Decrease FU's tau, curvature and coarse radius first if needed,
then choose r. The choices remain positive and independent of u,T.
For the weaker interior cut alone a sufficiently small fixed fine chart
already suffices as in PS. These are statements about an auxiliary
sector, not new definitions of G, Omega or the original cut.

The exact centered-contour identity is

    Z_cent=h_N^n (2pi sigma^2)^(d/2) det(K_*)^(-1/2)
                    exp[-F_epsilon(b)/sigma^2] Z_main(C_act). (NC32)

At complex original parameters this denotes the pulled-back holomorphic
top form on that specified contour. The full critical action, compact
kernel vacuum, Haar density and full colour/root/harmonic determinant
are retained. NC29 computes Z_loc, not the Z_main(C_act) in NC32.
No ratio of those Gaussian references has been canceled.

In particular a fixed physical original-a chart D_a has the FU30 domain
`(D_a-b)/sigma`, not D_p. At complex source b this is a contour with
boundaries; evenness of D_p does not transfer to it. The side/corner chains
that compare these domains require bounds using the actual b, original
readers, precision, source domain and the entire sweep. They have not
been estimated or summed in this unit. Nor has an original hard-history
indicator been transported or erased. Additional auxiliary complements
remain in the original one-step integral.

The source-dependent critical action still has its separate
O(rho delta_V^2/sigma^2) budget on a fixed real-V slice, and the full
normalization remains outside the nonlinear estimate. Joint tube
suprema use delta_hat. Stationarity removes the summed linear term
exactly, but cannot cancel a vacuum, determinant, component normalizer
or translated boundary.

The covariance-tail interface must restore both E_lift and T_crit while
retaining complete readers in each differentiated Gaussian and vertex.
FU's positive core makes real interpolation possible; its bounded
accretivity alone is not an all-order derivative-tree summation. The
current other author's unfinished Gaussian-return work is not a premise.
The available rate after the new core logarithm is beta/2 in ORIGINAL
blocks. This does not match RD's unchanged two-unit support loss or FR's
box margin. A separately proved consumer conversion is still required.

## 9. Rejected substitutions and provenance

The following tempting estimates are not used, and their failures remain
explicit evidence of the actual boundary:

1. On p=r/sigma a cubic remainder can be of size r^3/sigma^2; its Mayer
   supremum need not be small. A Gaussian-weighted estimate is essential.
2. Conditioning every inactive field on its chart does not leave the uncut
   normalized active Gaussian. NC23 retains local failures before taking
   marginals; it divides by no interacting or cut partition function.
3. Odd cancellation improves signed integrals, not E|f_v|. The O(sigma^2)
   singleton estimate is used only after even Gaussian integration.
4. Actual covariance entries generally read beyond their field endpoints.
   NC20 is not a local analytic activity for C_act with only vertex labels.
5. Treating sigma as varying u would differentiate the center, kernel and
   covariance and invalidate the parity argument as stated. They stay fixed.
6. Arbitrarily repeating a vertex loses bounded coordinate degree. The
   exponential is resummed at each original vertex before selecting W.
7. Dropping the translated domain or borrowing a larger support rate would
   change the consumer problem. Both obligations remain open.

Bałaban's constructions and Dimock's expositions are the architectural
antecedents. The existing SA/FU marked algebra and IC parity/overlap-tree
arguments are credited at their exact domains. The changed local Mayer,
complex marginal, reader enlargement and small-margin graph bounds are
derived here. No new external theorem or numerical experiment is imported.
The author read packet distinguishes exact fresh coverage from reused
same-revision coverage. All FU, PC and PS source/package bytes are immutable.

The mathematical source is frozen before packaging; a different fresh
reviewer must inspect this new unit. Requested Astra/max is a configuration
request, not backend attestation. No author-issued LAND, audit verdict,
retained promotion, Git operation, shared-front edit or other-agent edit is
performed. The coordinator owns integration into PR #10114. This is a
positive bounded construction with explicit outstanding interfaces, not a
no-go statement or a declaration that the full existence/gap route is closed.
