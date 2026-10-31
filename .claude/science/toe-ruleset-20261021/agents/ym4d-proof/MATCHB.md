# MATCHB — an interacting ancestry reference and the price of its correlations

**The exact positive interacting reference is constructed below. The
history-uniform pinned estimates and regeneration of their constants are
OPEN.** Absorbing the inherited action removes that action from the small
tilt, but transfers its correlations to the reference. A local conditional
law does not supply the independent-cell factorization in REFMATCH §2.
The replacement connected expansion in §6 is an exact gas of joint
cumulants, with a sufficient quantitative criterion proved here.

| Brief item | Disposition |
|---|---|
| Define actual interacting cells on the numerator variables | **PROVEN**, (MB1)–(MB5), including the separate all-cut comparison factor. |
| Positivity and TV one, including pins | **PROVEN** on positive fibers; zero fibers are not normalized. |
| Finite range | **PROVEN** conditional locality in the complete factor blanket. A uniform bound on that blanket for actual histories is **OPEN**. Independence at finite separation does not follow; (MB12) refutes that general inference. |
| Derivatives and local ratios | **PROVEN** finite fixed-support bounds with explicit score and replacement costs, (MB6)–(MB10). Uniform paid bounds for the full actual history family are **OPEN**. |
| Replace RM7–RM13 | **PROVEN** exact marginal identity and the conditional estimates in §5; **PROVEN** nonproduct cumulant-gas theorem in §6. Their actual uniform input estimates remain **OPEN**. |
| Regeneration with the same constants | **PROVEN** exact ancestry recursion, (MB25). Quantitative regeneration (MB29) is **OPEN**, not supplied by normalization. |

PROVEN labels the displayed assertion with its stated hypotheses; ARGUED
labels a proposed application; OPEN labels an unmet estimate. These are
author statuses, not audit verdicts or a Yang–Mills existence/mass-gap result.
The finite sign examples test general implications, not the SU(N) model.
There is no claim that interacting references are impossible.

The inputs are [REFMATCH](REFMATCH.md), its
[review](REVIEW_REFMATCH.md), [MIXSMALL](MIXSMALL.md),
[REALRGA](REALRGA.md), [REALRGB](REALRGB.md), [JMBRA](JMBRA.md) and
[LIB1](LIB1.md). Source identities and verification are in
[MATCHB_LOG.md](MATCHB_LOG.md). Credit belongs to Tadeusz Balaban and
Jonathan Dimock for the large-field organization described in those
sources. No literature theorem or memory-only [m] assertion carries a
step of the argument below; the needed finite identities are rebuilt.

## 1. Identical variables and an exact reference

Use the supplied finite periodic four-dimensional SU(N) model, N>=2,
odd L>=3, probability Haar, positive prescribed couplings and Decision 4's
actual arithmetic contour mean. Put t_l=kappa u_l and
`k_l(V_c;M_c)=exp(t_l Re tr(V_c* M_c)/N)/Z_(t_l)(M_c)`.
Every normalizer and its full contour reader is retained.

At fixed terminal V, let x=(U_0,...,U_j) denote **all** the numerator's
integrated ancestry. Let y contain V, original sources J, and any genuinely
retained exterior fields. With a complete earlier history h, define

    w_(h,y)(x)=Xi_h(x) exp[-sum_p (u_0+J_p)s(U_(0,p))]
                         product_(l=0)^j K_l(U_(l+1),U_l),
    U_(j+1)=V,   R_h(y)=int w_(h,y) dx,
    dnu_(h,y)=w_(h,y) dx/R_h(y),              R_h(y)>0.       (MB1)

Xi_h includes failures and absences. All current outcomes are summed in
(MB1), as in JMBRA A2; selecting a current child requires inserting its
actual predicate as well. For a local partially integrated representation,
use its retained coordinates in y and its actual remaining factors in w.
This construction concerns a positive history weight at real sources.
Signed extracted activities are insertions, not probability densities.

Lift the actual denominator to exactly these same coordinates:

    w_(A,y)(x)=chi_A(U_j)b_j(U_j)K_j(V,U_j),
    Z_A(y)=int w_(A,y)(x) dx.                                (MB2)

The dummy earlier Haar integrals have mass one. This introduces no
equality between b_j and the inherited density. No division by a hard cut
is made. The two densities may have different supports. For every integrable
insertion F on this same space,

    int F w_h dx/Z_A = C_(h/A)(y) E_(nu_h) F,
    C_(h/A)=R_h/Z_A.                                        (MB3)

This is an identity, not a bound on C_(h/A). At F=1 the complete original
quotient is still C_(h/A). Thus choosing the numerator as its own normalized
reference does not solve its comparison with the all-cut denominator.
Original source derivatives of this factor include bulk response; it cannot
be renamed a source-free constant or confined to the failed core. History
masses also remain once in an unconditioned history sum. Zero histories
are zero summands; no conditional law is assigned to them.

For specificity one can apply (MB1) at j=1 to REALRGB G2/G3: the specified
two adjacent old bad blocks give the actual 81-block hole. The old marked
link cap of radius 1/16 has exactly that failure list; its finite Wilson
and kernel weights are positive at every fixed real V. Hence R_h>0 there.
This verifies that the construction has an actual failed-history instance.
It does not prove that every local conditional fiber of that instance is
positive: each such fiber is tested separately below.

## 2. The actual conditional cell and all its pins

Partition the integrated coordinates into block cells C by a fixed owner
rule, retaining their level and original reader labels. An ancestry cell
may contain many levels. Write z=x_(C^c). Its actual conditional law is

    Z_C^full(y,z)=int w_h(y,x_C,z) dx_C,
    gamma_C(dx_C|y,z)=w_h(y,x_C,z) dx_C/Z_C^full(y,z),
                                 only if Z_C^full(y,z)>0.    (MB4)

This formula is the definition of the adapted interacting cell. It
contains the Wilson action, all read soft kernels, all read ancestral
factors, and the complete history, rather than a product of bare kernels.
It is directly on the numerator variables. For a positive joint marginal
at fixed pins x_S, use the same construction with C=S^c. For pins P within
a cell, restrict (MB4) to x_P and renormalize its remaining coordinates.
All conditional statements use these explicit positive-fiber versions;
values on zero fibers have no probabilistic meaning.

**PROVEN — positivity and TV.** The real weight is nonnegative and its
nonzero factors are positive. On a positive fiber the integral of gamma_C
is one, so its total variation is one. It is strictly positive only on its
allowed support. This proof works after every admissible pin; it supplies
no uniform lower bound on Z_C^full and does not remove hard zeros.

For locality, factor the opened weight into its actual factors f_a with
reader sets R_a. The complete-history product in JMBRA A6 is one finite
such representation; completion and absence factors keep their full sets.
On a positive fiber, factors not reading C cancel between numerator and
denominator of (MB4). Consequently gamma_C reads only

    B(C) = union_(a:R_a meets C) R_a, including y readers.    (MB5)

More explicitly, let q_C be the product of all incident factors and
F_ext the product of all other factors. Then
`w_h=F_ext q_C`, `Z_C^loc=int q_C dx_C`,
`Z_C^full=F_ext Z_C^loc`, and `gamma_C=q_C/Z_C^loc` on a positive fiber.
The exterior factor cancels only in gamma_C. Its y derivatives remain
in the full normalizer, and its full original readers and source dependence
remain in comparisons such as (MB3).

This is an exact **conditional** locality statement. Every interaction
between coordinates inside C remains unexpanded. A bound on the diameter
or size of B(C) is an additional geometric/factor hypothesis. Complete
failure predicates may have arbitrarily large readers; a contracted
ancestry cell also contains its original source labels. Neither the fact
that each soft contour has two endpoint blocks nor the finiteness of a
particular lattice supplies a common bound over depth and histories.

In particular, (MB4) is a compatible family of conditionals of nu_h,
not a prescription to multiply those conditionals. Their product is in
general a different, unnormalized law. Successive one-sided conditionals
do give a chain-rule product, but their readers include the messages
created by marginalization and need not be bounded.

## 3. Pinned derivatives and local comparisons

Use exactly REALRGA RGA3, total field order p=6 and original-source order
q=4, or RGA4 with all four labels. Directions and their weights are fixed
while differentiating. Thus words of total order ten occur. No change to
REALRGB's weaker l1 norm, no source-dependent field transport and no
derivative acquisition from a value bound is used.

**PROVEN — fixed-support relative jets.** Suppose, on the stated open y
domain and at fixed exterior/pins, the reduced incident weight q_C can be written
`w0(x_C,z) exp H_C(y,x_C,z)`, with fixed nonnegative w0, compact-set
dominated derivatives, and weighted ordered score bounds

    |D_I H_C| <= b_(C,r),                    1<=r<=10.     (MB6)

Choose these bounds uniformly over whichever pins are claimed. A concrete
finite bound is the sum of the score bounds of every incident smooth
factor after the cancellation in (MB5). Its dependence on ancestry,
couplings and reader count must be retained. A Wilson factor contributes
its actual coefficient and plaquette directions. A kernel contributes
both `t_l h_M` and `-log Z_(t_l)(M)`; the path-occurrence and positive
integral calculation of MIXSMALL MS8/MS9 gives finite bounds for both.
Original-source differentiation keeps all prescribed kernels fixed.

Here is the required calculus, including the normalization. For an array
b=(b_1,...,b_10), define

    M_0=I_0=1,
    M_r(b)=sum_(pi partition [r]) product_(B in pi) b_|B|,
    I_r(b)=sum_pi |pi|! product_(B in pi) M_|B|(b),
    L_r(b)=sum_pi (|pi|-1)! product_(B in pi) M_|B|(b),
    C_r(b)=sum_(s=0)^r binom(r,s) M_s(b) I_(r-s)(b).

Repeated differentiation of exp H assigns each ordered position to a
partition block. Integration and division by Z_C^loc bound its derivative by
M_r. Differentiating log and reciprocal gives the coefficients
`(-1)^(k-1)(k-1)!` and `(-1)^k k!`; Leibniz gives C_r. Therefore

    |D_I Z_C^loc|/Z_C^loc <= M_r(b_C),
    |D_I log Z_C^loc| <= L_r(b_C),
    |D_I gamma_C(x_C)| <= gamma_C(x_C) C_r(b_C),
    T^(6,4)(gamma_C) <= P_C gamma_C,
    P_C=sum_(a+b<=6,c<=4) C_(a+b+c)(b_C)/(a!b!c!).       (MB7)

Order inside each word is preserved. The labelled version distributes
distinct source subsets instead of c!; its weights are already in the
scores. Differentiation at zeros of fixed w0 gives zero and requires no
log w0. Pinning restricts the domain of the score supremum, so the SAME
array b_C works on every positive pinned fiber covered by (MB6). There
is no inverse rare-sector mass in this relative estimate.

The first two bounds are for Z_C^loc. For the original full normalizer,
`log Z_C^full=log F_ext+log Z_C^loc`; its extra exterior derivatives must
be retained, and Leibniz applies to `Z_C^full=F_ext Z_C^loc`. For example,
an exterior factor exp(A y) gives gamma_C independent of y but contributes
A to the full logarithmic derivative. It cannot be estimated by an
incident-only zero score array.

This is not a uniform derivative theorem for the complete actual family.
If a selector moves with y, w0 is not fixed: its boundary derivatives
must be supplied by FR/SEL or the alternatives summed first. If ancestry
is integrated out before taking a conditional, its induced log density
also requires score estimates; it is not just the last kernel. Even for
one actual kernel, MIXSMALL MS14 has a normalized fine second derivative
growing with u, and REFMATCH RM21 a fourth derivative growing with u^2.
Those witnesses concern individual normalizers, not a lower bound on the
complete cell estimate. They forbid treating such costs as automatically
O(1). Paid regulator/charge bounds and their joint moments remain inputs.

**PROVEN — a same-support local ratio.** If two complete incident weights
have the same fixed support and satisfy `q_C^+=q_C^- exp Delta_C`, then

    Z_C^(loc,+)/Z_C^(loc,-) = E_(gamma_C^-) exp Delta_C,
    min Delta_C <= log(Z_C^(loc,+)/Z_C^(loc,-)) <= max Delta_C,
    exp(-osc Delta_C) <= gamma_C^+/gamma_C^-
                                         <= exp(osc Delta_C). (MB8)

The first identity follows by division, the second by integrating the
pointwise exponential bounds, and the last by subtracting the same log
normalizer from Delta_C. Supports that differ require a separate sector
decomposition, not this ratio. For score arrays b^+,b^- as in (MB6),
Leibniz also gives

    |D_I (Z_C^(loc,+)/Z_C^(loc,-)) <= (Z_C^(loc,+)/Z_C^(loc,-))
       sum_(s=0)^r binom(r,s) M_s(b^+) I_(r-s)(b^-).     (MB9)

Thus both the scalar local price and its derivative bill are explicit.
This bound does not infer small derivative differences from a small
zeroth-order Delta_C.
For full normalizer ratios, multiply by `F_ext^+/F_ext^-` and retain its
derivatives and readers separately. Unequal exterior factors do not cancel.

For example, changing P complete Wilson factors of coefficients c_p and
C complete kernels, with the same couplings and hard support, gives the
valid crude bound

    |Delta_C| <= 2 sum_(changed p)|c_p|
                            +4 sum_(changed kernel c)t_level(c). (MB10)

Here 0<=s<=2, and each normalized kernel has log between -2t and 2t.
Include all changed incident factors and all their ancestors; changed
exterior factors belong to the separate exterior ratio. The counts
are not automatically one-step block counts. An unchanged factor cancels
before this estimate. The O(u) bound in (MB10) is finite but too costly
to certify a net `c u^delta-O(log u)-A u>0` when A>0 and 0<delta<1.
That is failure of this crude majorant, not a lower bound on the optimal
matched ratio. Uniform local matched cancellations remain OPEN.

## 4. What factorization survives

**PROVEN — conditional independence across a retained separator.** Suppose
a set B of retained integration coordinates separates interiors C_i in
the complete factor graph, including selectors. At fixed eta=x_B no
factor meets two interiors. Then exactly

    dnu(x)=lambda(deta) product_i gamma_(C_i)(dx_(C_i)|eta),
    lambda(deta)=Z^-1 w_B(eta) product_i Z_(C_i)(eta) deta. (MB11)

Multiply the actual factors and integrate the disjoint interiors to prove
this formula. All intercell normalizers remain in lambda. Disjoint
interior insertions factor at fixed eta; after integrating eta their
covariance is the covariance, under lambda, of their conditional means.
The derivatives of lambda are also part of the subsequent integral.
This is a useful interacting-cell implementation of RM1 at **frozen**
separator data. It does not solve the interacting separator integral.

**PROVEN — local conditional specification does not imply finite-range
dependence.** On a path with signs x_0,...,x_m and 0<t<1, set

    nu_t(x)=2^(-(m+1)) product_(i=0)^(m-1)(1+t x_i x_(i+1)).
    E x_i=0,       E x_0 x_m=t^m>0.                    (MB12)

One can generate this law with a fair x_0 and independent increments
e_i=x_(i-1)x_i having mean t. This proves normalization and the displayed
moments directly. All weights are strictly positive. A one-site full
conditional reads only its nearest neighbors and has finite ratio and
score bounds at fixed t. Nevertheless separated endpoint functions do
not factor at any finite range. In particular, for g_0=a x_0, g_m=a x_m,

    E(g_0 g_m)-E(g_0)E(g_m)=a^2 t^m !=0.               (MB13)

This is the exact failed factorization equality in an attempted direct
replacement of the product law by local interacting conditionals. It
already fails at derivative order zero. It is not a Wilson-history
counterexample. Likewise a source tilt exp(y x_m) changes the endpoint
mean to `t^m tanh y`; its y derivative at zero is t^m. Marginal parameter
readers therefore need not be restricted to the one-site conditional
blanket. For fixed positive support rate sigma the series
`sum_(m>=1) exp(sigma(m+1)) t^m` diverges if exp(sigma)t>=1. Pointwise
decay at each t does not give an arbitrary fixed rate uniformly in t.

The alternatives are to retain the separator, keep complete connected
correlation readers, or group all mutually dependent cells. The last
choice is exact but can make a cell volume-sized. Its support weight and
original sources cannot be replaced by those of its small core. LIB1's
full-root bounds require a bounded-hole hypothesis and a stronger input
rate; its active-root estimate cannot supply this missing full norm.

## 5. RM7–RM12 on a nonproduct reference

Let nu_y be (MB1), or a stated positive marginal of it on the same variables.
Let Phi be a bounded real residual tilt, with the full required jets and
fixed supports, and write `nu^Phi=e^Phi nu/E_nu e^Phi`. For every positive
pin x_S define

    Z_Phi^S(y,x_S)=E_nu[e^Phi|x_S],
    Z_Phi^empty(y)=E_nu e^Phi,
    B_S=log Z_Phi^S-log Z_Phi^empty,
    E_(nu^Phi) F(x_S)=E_(nu_S)[F(x_S) exp B_S].        (MB14)

This follows by integrating the joint density outside S and then
normalizing. It is the exact RM8 replacement. Unlike RM4, the first
integral uses the conditional law of the unpinned coordinates, which
itself depends on x_S. The base marginal is nu_S, not a product of bare
kernels. If Phi=0, B_S=0: the strong action now costs zero as a *residual
tilt*. The costs of nu_S and C_(h/A) have not vanished.

There is no automatic RM7 cancellation on bare atom supports. For (MB12)
take S={0} and Phi=epsilon x_m. Direct conditioning gives

    Z_Phi^S=cosh epsilon+t^m x_0 sinh epsilon,
    Z_Phi^empty=cosh epsilon,
    partial_epsilon B_S at zero=t^m x_0.              (MB15)

The tilt is supported at m, disjoint from S, yet the difference is nonzero.
Any supported expansion must include the connecting reference reader.
Without localization, the always valid scalar bound is merely
`|B_S|<=osc Phi`, potentially extensive.

Here is an explicit sufficient replacement, not a claim that it has been
produced. Fix sigma>=0. Let H be a nonempty connected complete core containing
S and **all** original parameter readers of F and the base marginal density
n_(S,y), together with integrated ancestry readers required by the support
convention. If the natural union is disconnected, choose a connected hull
and pay its actual size throughout (MB18)–(MB21), including the input d.
Empty-support scalars keep their separate budgets. Supply, for every used
pin, supported expansions

    log Z_Phi^S=sum_K L_K^S,  log Z_Phi^empty=sum_K L_K^empty,
    L_K^S=L_K^empty if K misses H,
    sup T L_K^S, sup T L_K^empty <= beta_K,
    sup_v sum_(K:v in K) exp(sigma|K|) beta_K <= eta.   (MB16)

All K are complete connected supports. One common beta must work before
the pin/history sums. Equal primitive factors alone do not prove the
coefficient equality in (MB16). A cumulant construction as in §6 is one
possible source of these expansions, but its bounds and the matching of
pinned coefficients must then be verified. These are substantive inputs.

Under (MB16), subtraction and rooting at vertices of H prove
`T B_S<=2 eta |H|`, exactly the RM7 estimate. Suppose also
`T n_(S,y)<=P_G n_(S,y)` on a common fixed integration support and
`sup T f_i<=s_i`. For fixed events E_c on distinct owned cells, supply

    nu_y(intersection_c E_c) <= exp(-sum_c q_c), q_c>=0,
    w_G=P_G product_i s_i exp(-sum_c q_c).             (MB17)

These events and the insertions read S. Integrating Leibniz's inequality
against the SAME n_S in (MB14) gives

    sup T E_(nu^Phi)[product_i f_i product_c 1_Ec]
                                  <=w_G exp(2 eta |H|). (MB18)

This is RM9 with the **actual** marginal jet price P_G and actual joint
event price. The bare D_6 and q_gap of MS17 are not inherited for free.
An alternative proof of the joint event bound is a uniform bound
`nu(E_c|all other event-cell coordinates)<=exp(-q_c)` for every c:
condition on the other cells and peel the event indicators one at a time.
No independence is needed, but these conditional inequalities must hold
on all the positive conditioned fibers being used.

For m events of common price q, the explicit RM10 substitute is

    q_adapted=q-(log P_G)/m-2 eta |H|/m >0.            (MB19)

If P_G or |H| lacks the stated per-event control, retain (MB18); do not
divide an arbitrary reader bill among imaginary fresh gaps. In particular
if the reference has already conditioned on an event E of positive mass,
then nu(E)=1. A proposed fresh price q>0 demands the false inequality
`1<=exp(-q)`. Its creation mass stays once outside the conditional law.

Expanding exp B_S into supported factors gives the literal RM11 analogue

    sum_(Y superset H) exp(sigma(|Y|-|H|)) sup T A_(G,Y)
                                  <= w_G exp(2 eta |H|). (MB20)

Every Y is H union its attachments, so is connected. The support assertion
uses the complete readers of n_S already in H. If n_S reads the entire
volume, so does this H; (MB20) is not then a useful local estimate. A
weighted decomposition of that base dependence would be an alternative
additional input, not a reason to omit it.

For the full-root version take (MB16) at sigma+1, eta<=1/4, and a common
core family with each H_G satisfying this same connected complete-core
requirement and
`d=sup_v sum_(G:v in H_G) exp((sigma+1)|H_G|) w_G`.
Then

    sup_v sum_(G,Y:v in Y) exp(sigma|Y|) sup T A_(G,Y)
                                                <=(1+2 eta)d. (MB21)

For roots in H, the attachment exponential exp(2 eta |H|) is absorbed
by the spare support unit. For a root in a tail, mark one attachment K;
the exponential's 1/n! becomes 1/(n-1)!. Sum cores meeting K by their
vertices, at cost |K|d, and use
`sum_(K:v in K) 2 beta_K exp(sigma|K|)|K|<=2 eta`.
This proves (MB21), including inactive and tail roots. Different history
backgrounds require a joint majorant for their summed family, not merely
the same numerical bound for each separately. No reference independence
was used after the explicit hypotheses (MB16)–(MB17).

## 6. RM13 without cell independence: a cumulant gas

**PROVEN — exact nonproduct algebra and a conditional quantitative theorem.**
Let g_i, i in a finite label set I, be real insertions on the same normalized
reference nu (including the residual tilt if desired). Each has a nonempty
declared support H_i. All expectations and the following cumulants are
functions of the retained y, differentiated with their reference. Define

    m_B=E_nu product_(i in B)g_i,
    k_B=sum_(pi partition B)(-1)^(|pi|-1)(|pi|-1)!
                                  product_(A in pi)m_A.      (MB22)

Then `m_B=sum_(pi partition B) product_(A in pi) k_A`.
To prove both identities, introduce distinct formal nilpotent labels t_i.
Expand `log E product_i(1+t_i g_i)` by the finite log series. A partition
with k blocks occurs k! times in the kth power and has coefficient
(-1)^(k-1)/k, giving (MB22). Exponentiating gives the inverse identity.
This proves each subset identity; it does not substitute 1 for a nilpotent
variable. Summing the subset identities now proves the ordinary identity

    E_nu product_i(1+g_i)
       = sum_(collections of pairwise label-disjoint nonempty B)
                                                product_B k_B. (MB23)

Assume an absolutely convergent decomposition `k_B=sum_K c_(B,K)` into
functions with complete connected supports K containing union_(i in B)H_i.
Let a_(B,K)=sup T c_(B,K), including all reference derivatives. For
sigma>=0, define

    Delta_sigma=sup_v sum_(B,K:v in K)
                         exp((sigma+1)|K|) a_(B,K) <=1/4.
    Then ||log E_nu product_i(1+g_i)||_(sigma,T)
                                                  <=Delta_sigma. (MB24)

The logarithm exists and is real under these hypotheses. A separate
factor C_(h/A) retains its separate log/jet budget.

Proof: expand each k_B in (MB23). The resulting gas has types (B,K),
compatible **exactly when their B label sets are disjoint**. Disjoint
labels may have overlapping spatial supports and must still be allowed.
Declaring all spatial overlaps incompatible would change (MB23).
Conversely incompatibility implies a spatial intersection, since both K
contain the nonempty support of a shared label. Thus every connected
incompatibility cluster has a connected union of full supports.

For type tau=(B,K), set v_tau=exp(sigma|K|)a_tau and
b_tau=exp((sigma+1)|K|)a_tau. The positive rooted-tree recursion
`T_tau=v_tau exp(sum_(tau' incompatible with tau) T_tau')` has
supersolution b_tau: its child sum is at most Delta_sigma |K|<=|K|.
This remains true when the identical type is repeated in a log cluster;
its nonempty B is incompatible with itself. Rooting at a physical vertex
and using `|union K|<=sum |K|` bounds the rooted tree series by Delta_sigma.

For completeness, order the incompatibility edges. The graphs with a
fixed Kruskal tree have optional extra edges precisely when that edge is
later than all edges on its tree path. Their alternating sum is a sign
times a product of (1-1), hence has absolute value at most one. This gives
the tree bound for the logarithm, with the factorial of unordered cluster
tuples. Marking a type through the physical root replaces 1/n! by
1/(n-1)!, matching the rooted-tree count. The jet norm is submultiplicative
by ordered Leibniz, so the same proof controls every included derivative.

Scale all type activities by one auxiliary scalar z. For |z|<2 the same
majorants converge, since 2 Delta_sigma<=1/2. Near zero, expansion of the
exponential of connected graphs reproduces the finite gas by partition
into connected components. Absolute convergence extends the identity to
z=1. It proves nonvanishing there and identifies the real logarithm.
Countable support decompositions follow by the same absolute majorant.
This auxiliary series is not complex continuation in physical sources.

The algebra is unconditional for finite moments. The smallness hypothesis
in (MB24) is **OPEN** on the actual reference. At second order it already
includes `k_{i,j}=Cov_nu(g_i,g_j)`, even when the insertions are far apart.
Hence setting the residual-background budget to zero does not set these
types to zero. The reference has absorbed the Wilson atom responsible for
MIXSMALL MS29/MS30, but now has to supply the entire differentiated
connected-correlation family. Higher orders include all original source
labels and normalization derivatives, not only pair covariances.

Compared with RM13, no factor 1/(1-4 eta) appears because the background
has already been integrated. The cost is hidden nowhere: Delta_sigma is
a new, explicit joint input. In a product-cell representation with small
seams, the augmented-atom proof of REFMATCH can instead bound the same
connected output by d/(1-4 eta). Neither bound makes the other method's
unverified input free. The cumulant criterion is a sufficient replacement
for the missing factorization mechanism, not a demonstration that the
actual analytic problem is weaker.

## 7. Regeneration: exact closure versus quantitative closure

**PROVEN — same exact ancestry form.** Before fixing its next endpoint,
append the actual kernel and selected-child predicate to the opened weight:

    w_(j+1,h a)(x,V;J)=w_(j,h)(x;J) K_j(V,U_j) I_(a|h)(x,V),
    rho_(j+1,h a)(V;J)=int w_(j+1,h a)(x,V;J) dx.       (MB25)

Here w_(j,h) contains kernels only through j-1; this convention separates
the unfixed state in (MB25) from the fixed-terminal weight (MB1).
Fubini gives the next marginal. Since sum_a I_(a|h)=1, summing all children
and integrating V preserves the old mass by kernel normalization. Each
positive child has the conditional reference (MB4) for the extended
ancestry. This proves exact recursive form, including all absences and
endpoint masses. It proves no invariant reader, derivative or norm bound.

**PROVEN — the estimates generated by elimination contain correlations.**
On a fixed support write `W(y)=int w0(x) exp H(y,x) dx`, with its
normalized conditional law pi_y. Quotient differentiation gives

    D_a log W=E_pi D_a H,
    D_b D_a log W=E_pi D_b D_a H
                         +Cov_pi(D_a H,D_b H).         (MB26)

Thus even disjoint first-order scores create a cross term after integration.
For distinct source labels the full finite identity is total cumulance:
given a retained separator eta, the joint cumulant of F_i equals
`sum_(pi partition labels) kappa_outer(kappa_inner(F_i:i in B):B in pi)`.
It follows by applying the same nilpotent log/exp calculation as (MB22)
first conditionally and then to the outer expectation. Singleton inner
means and their outer cumulants remain. In particular conditional
independence inside (MB11) does not kill the outer covariance or the
four-label outer partition terms. Moving selectors require additional
boundary terms before (MB26) can be used.

A strictly positive bounded-degree example shows why even finite-range
**Markov** specifications are not automatically regenerated. Let hidden
signs z_1,...,z_m have the path law (MB12), and observations satisfy

    P(x_i|z_i)=(1+s x_i z_i)/2,             0<s,t<1.     (MB27)

The full graph has degree at most three and only nearest-level/path
factors. After eliminating the z's, at m=3 the observed density relative
to three fair signs is
`1+s^2 t(x_1 x_2+x_2 x_3)+s^2 t^2 x_1 x_3`.
Therefore

    Cov(x_1,x_3 | x_2=+1)=s^2 t^2(1-s^2)>0.           (MB28)

It cannot be a nearest-neighbor Markov law on x_1,x_2,x_3. More generally,
fix any observations x_2,...,x_(m-1). Let
`T_(z,z')=(1+t z z')/2`, `O_(x,z)=(1+s x z)/2`,
`D_x=diag_z O_(x,z)`, and `Pi=(1/2)I`.
The unnormalized 2-by-2 endpoint matrix is
`M=O Pi T D_(x_2) T ... D_(x_(m-1)) T O^T`.
Its determinant is
`s^2 t^(m-1)/4 * ((1-s^2)/4)^(m-2)>0` for m>=2.
This follows from det O=s, det T=t, det Pi=1/4, and
det D_x=(1-s^2)/4. All entries are positive. Two binary variables are
independent iff their joint matrix has determinant zero: a product law
has rank one, and a positive rank-one probability matrix is the product
of its marginals. Normalization does not change whether its determinant
vanishes. Hence the observed endpoints remain conditionally dependent
at arbitrary separation even with all intervening observations fixed.

This is an exact failure of automatic finite-range regeneration for
positive local ancestry plus positive local noisy kernels. It is not an
identification with Decision 4 or a no-go for its gauge-law reference.
Retaining all z variables restores the original factor graph, at the cost
of retaining ancestry; using weighted correlation readers is another
live route. Both still need uniform estimates in the consumer's norm.

To close MATCHB for the actual theory, one must construct an explicit
admissible state class and verify, at the NEXT step on every positive
fiber, with the same fixed p,q,mu and original source weights,

    sup_(j,h,allowed pins) [full paid cell-jet budget] <= P_*,
    sup_(j,h,allowed pins) [local comparison log budget] <= b_*,
    sup_(j,h,allowed pins) [common matched budget at required rate] <= eta_*,
    sup_(j,h,allowed pins) Delta_(j+1,mu) <= Delta_* <=1/4. (MB29)

The bracketed budgets must be the actual (MB7), (MB8)/(MB9), and (MB16)
quantities, with every charge/regulator allocation specified on the same
law. In these local budgets the normalizers are Z_C^loc. Any full fiber
normalizer or full ratio also retains F_ext and its own full-reader score
and log budget, as required after (MB7) and (MB9).
A declared polynomial-in-u envelope with fixed coefficients is
permitted if its cost is actually paid; P_* does not silently demand or
assert an unregulated coupling-independent kernel estimate. If histories
are summed, the needed rooted sums include that complete family before
suprema, or use one common summable envelope. Source/scalar logs, especially
C_(h/A), have their own budgets. Neither a fresh gap nor TV one implies
any of these inequalities. Their actual production is **OPEN**.

If (MB21) spends one support-rate unit, the next construction must produce
that unit again; if the product-cell two-stage argument is used, its two
units must likewise be regenerated. Repeatedly lowering mu is not (MB29).
For arbitrary holes one also needs a jointly paid hole bound or an
alternative to full-support saturation. REALRGA H4/H5 additionally need
extraction and continuation estimates; (MB29) does not prove those.

## 8. Exact comparison with RM1 and the failure boundary

| Operation | RM1 with product cells | Adapted interacting reference |
|---|---|---|
| Strong action and ancestry | Must be absorbed into cell factors or represented by controlled background atoms. | Included exactly in (MB1)/(MB4); the corresponding residual tilt can be zero. |
| Cell pinning | Product marginal and complementary product integral. | Actual marginal and conditional integral (MB14); neither is replaced by Haar. |
| Unvisited variables | Normalized unused cells integrate to one separately. | Only a full conditional integration or a reader-free directed elimination can do this; shared ancestors and lambda in (MB11) survive. |
| RM7 cancellation | Disconnected complete clusters agree. | Bare disjoint atoms can still respond to a pin, (MB15). Common full-reader matching (MB16) is needed. |
| RM9/RM10 prices | Bare-kernel D_6 and distinct product gaps, after matching. | Actual P_G and actual conditional/joint gap bounds (MB17)–(MB19). Mandatory events receive no new price. |
| RM11/RM12 supports | Background attachments and their tail roots. | The same estimates follow with (MB16), but native marginal readers must already be in H or have a paid decomposition. |
| RM13 | Joint atom integration factors over complete overlap components. | This factorization fails in general, (MB13); the label-disjoint cumulant gas (MB23)/(MB24) replaces it. |
| Return to Z_A | A separately checked inherited/bare matching identity. | C_(h/A) remains explicitly in (MB3); choosing nu_h cannot bound it. |
| Next step | RM2 and its extra support reserve must be reproduced. | Exact form reproduces by (MB25); reference cumulants, ratios, jets and support reserves must satisfy (MB29). |

The precise failures established here are (MB13)'s nonzero factorization
defect, (MB15)'s nonzero distant pin response, `1<=exp(-q)` for a supposed
fresh price of an already mandatory event, and (MB28)'s nonzero
conditional covariance after a local marginalization. They refute those
general shortcuts. For the **actual** adapted SU(N) construction, the
unproved inequality is (MB29), with its one-step joint input (MB24) and
paired-reference/pin requirements (MB16)–(MB19). No inequality for that
complete actual object is declared false on the strength of a sign model
or the crude upper bound (MB10).

**ARGUED next actual construction.** On a fixed bounded mixed core, retain
the opened ancestry and a separator as in (MB11), absorb its interior
Wilson and inherited factors, and compute the conditional cell and the
separator's induced factors together. Keep one fine/coarse derivative,
all four original-source labels and every completion alternative. Seek
the pair and higher joint coefficients c_(B,K), including roots on
separator tails, under the same all-cut comparison. FR supplies only its
proved fixed-sector/selector interface, KR its proved local remainder,
and TC its proved original-law charges; their all-history extensions are
not assumed. Evaluate (MB24) and then reproduce (MB29) at the next step.
This is substantial unresolved analytic work, not a smaller lemma renamed
as an accomplished induction.

## 9. Diagnostic scope and evidence

The negative-claim boundary is explicit. **N1:** actual conditional cells,
separator disintegration, and cumulant grouping were explored; no exhaustive
route count is asserted. **N2:** no independent-wall count is asserted;
the joint cumulant construction may also provide reference localization.
**N3:** positive fibers, fixed supports, full original readers, same-law
score bounds and common majorants are hypotheses, not consequences of a
name. **N4:** the sign examples target independence and regeneration
inferences, not the gauge remainder. **N5:** the diagnostics are finite
probability models and finite-order identities, not continuum estimates.
**N6:** retaining ancestry, paid weighted readers and a different compatible
cell partition require mathematics rather than new physical axioms.
**N7:** a successful matched, charged joint-cumulant construction remains
compatible with every example above. **N8:** JMBRA already identifies the
reader closure and interacting-cumulant alternative; REFMATCH supplies the
conditional product theorem and MIXSMALL its precise price boundaries.
This packet supplies the explicit nonproduct construction and cumulant-gas
bridge, without a global novelty or exhaustion claim.

The [registered finite criteria](checks/matchb_criteria.md) test only the
algebra and distinguish several omitted-normalizer/omitted-correlation
calculations. Execution status, resource guards and fresh hostile review
are recorded in the log. Neither a finite PASS nor a review LAND, if
obtained, supplies the OPEN actual-model estimates. No existing source,
axiom, audit or ledger is changed; no commit is made.
