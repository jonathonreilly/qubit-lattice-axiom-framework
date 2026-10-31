# REFMATCH — local real reference comparison and paid normalizer jets

**A local comparison theorem is PROVEN under an explicit product-reference
identity and a differentiated polymer budget. Its identification with every
actual inherited history is OPEN.** REALRGA's H-hypotheses alone do not
supply that identity in the form asserted by the author brief. The result
below isolates the additional input, cancels the distant reference volume,
and includes normalizer derivatives. It also pays MIXSMALL's SU(2) witness
through fourth order, with an extension through the six field derivatives
needed by the RG contract. The final one-step theorem is conditional.

| Requested item | Status |
|---|---|
| Transfer from product law to inherited reference | **PROVEN** for the explicitly matched, small, differentiated tilt in RM1–RM13; **OPEN** identification and uniform production for the actual all-history reference. |
| Normalizer derivatives | **PROVEN** finite-order prices RM14–RM24, original-level witness payment and short-mean regulated payment; **OPEN** the joint inherited-law charge/regulator certificate for the general mixed family. |
| Complete real RG step | **PROVEN** conditional implication in section 6; **OPEN** its listed model hypotheses. LOCOP.md was absent in this snapshot. |

PROVEN means the written assertion with its displayed hypotheses; ARGUED
means a proposed construction; OPEN means an unmet estimate. None denotes
an audit verdict, a completed Yang–Mills construction or a mass gap.
Source identities, review and checks are in [REFMATCH_LOG.md](REFMATCH_LOG.md)
and [the source manifest](checks/refmatch_sources.json). The candidate
revision is `1079134633504cbb62a9f52aa3cb4fa097300254`.

Credit: Tadeusz Balaban's large-field organization, Jonathan Dimock's
[large-field exposition](https://arxiv.org/abs/1212.5562),
Fernandez–Procacci's [tree-graph polymer methods](https://arxiv.org/abs/math-ph/0605041),
and Brydges–Slade's [normed algebras](https://arxiv.org/abs/1403.7244).
These are method attributions, not imported gauge-model theorems. Every
additional load-bearing lemma is proved here. No memory-only [m] item
carries weight.

## 1. The input that must actually match

Use the supplied finite periodic four-dimensional SU(N) model, N>=2,
odd L>=3, probability Haar, t_j=kappa u_j, and exactly the paired contours
in MIXSMALL MS1. In particular, retain the distinction

    R_h(V;J)=int rho_(j,h)(U;J) K_j(V,U)dU,
    Z_A(V)=int chi_A(U)b_j(U)K_j(V,U)dU,
    b_j=exp(-u_j sum_p s(U_p)),     Q_h=R_h/Z_A.

MIXSMALL MS17 instead integrates selected output variables W under
product_c k_t(W_c;M_c(U))dW_c at fixed U. These are different
integrations. A comparison must specify a common variable space and an
exact disintegration or change of representation before estimating it.
The inherited rho, all absences, all-cut support, source scalars and endpoint
normalizers cannot be dropped in that operation.

**OPEN identification.** REALRGA H3 (lines 424–433) supplies a small
integrated residual expansion relative to its stated reference. H0 and
H4 still retain the main action, selected sectors and relevant terms.
It does not say that this entire reference is a small pointwise tilt of
MS17's product law. Even a vanishing residual leaves the specified main
action and cuts present. Also, a small signed integrated coefficient does
not bound that coefficient after some of its variables are fixed. The
new theorem therefore explicitly requires the following stronger input.
This is a diagnosis of the available premises, not an obstruction theorem
against constructing such an input.

**MATCH(j), supplied input.** On a fixed positive fiber, identify the
actual normalized reference on variables W with

    dnu_y(W)=Z(y)^(-1) exp(Phi_y(W)) dmu_y(W),
    dmu_y=product_(c in C) n_c(y,W_c)dW_c,
    Phi=sum_X phi_X,     Z=int exp(Phi)dmu.                 (RM1)

Here y contains every retained parameter, including original sources;
n_c are normalized positive densities on fixed product cells, with their
full readers. In the MS17 application they are the actual soft kernels.
All functions have the included ordered real derivatives and compact-set
domination. Hard constraints must already have the same support on both
sides, or remain as explicitly estimated insertions. A bounded real Phi
cannot turn a strictly positive product density into a density vanishing
on a positive-measure hard-cut complement. This simple support check is
part of verifying RM1, not a permission to discard that complement.

The norm T is REALRGA RGA3 with p=6,q=4 or its four-label RGA4 version.
Original sources hold prescribed kernels and couplings fixed; all jet
weights are frozen during differentiation. There are words of total
order ten. The normalizer-only calculations of order four below are
diagnostics; they do not replace this (6,4) contract. A source-dependent
field transport needs the additional field hierarchy specified in
REALRGA/EXTCONT and is not silently used here.

Fix sigma>=0 and a block graph containing all integrated cells and retained
readers. Start with a finite atom family; countable families require the
same absolute majorants and follow by their convergent finite truncations.
Each interaction has nonempty connected complete support H_X, including
the readers of every product density on its integration cells C_X.
Suprema include the W coordinates and the stated open y domain. Supply

    T_y(n_c)<=P_c n_c, P_c>=1,
    sup_(y,W) T_y(a_X)<=s_X,     a_X=exp(phi_X)-1,
    alpha_X=s_X product_(c in C_X) P_c,
    eta_sigma=sup_v sum_(X:v in H_X)
                       exp((sigma+2)|H_X|) alpha_X <=1/4. (RM2)

The first inequality is pointwise relative to the fixed cell measure.
No W derivatives are claimed when W is an integrated variable; the y
derivatives and their original weights remain unchanged when W is pinned.
For example s_X=exp(sup T phi_X)-1 is sufficient. Section 4 computes P_c
for the actual kernel. All these quantities must be uniform over the
claimed histories/domains. RM2 includes product-density derivatives;
small bare phi jets or small already integrated residuals alone are not
RM2. A direct uniform pinned joint bound of the strength proved from RM2
below can replace this deliberately conservative pointwise certificate.

## 2. A uniform pinned cluster library — PROVEN

Ordered Leibniz distributes derivative positions between factors without
commuting them. The factorials in RGA3 turn the binomial convolution into
a product; RGA4 distributes disjoint label subsets. Therefore
T(FG)<=T(F)T(G) and T(exp F)<=exp(T(F)). These also hold after taking
suprema. Differentiation under a fixed integral gives

    T(int F n)<=int T(F)T(n).                              (RM3)

Let S be any subset of the integrated cells. Define, with W_S pinned,

    Z_barS(y,W_S)=int exp(Phi_y(W)) dmu_(y,C\S),
    Z_all(y)=int exp(Phi_y(W)) dmu_(y,C).                  (RM4)

The empty integral is allowed; Z_bar(empty)=Z_all. Expand each exponential
as 1+a_X. For any selected set I, integrate only its visited, unpinned
cells, integrating every other normalized density to one first. RM3 gives

    sup_(y,W_S) T int product_(X in I) a_X dmu_(visited\S)
              <=product_(X in I) alpha_X.                (RM5)

Indeed the density cost of the union of visited cells is at most the
product of their P_c, bounded by the product assigned to all atoms since
P_c>=1. Pinning removes some such costs and cannot worsen the majorant.
Disjoint complete overlap components factor exactly under the product
integration. Shared fixed parameters may conservatively join supports;
they do not invalidate this factorization of separate integrations.

Here is a proof of the cluster estimate, including a common majorant
independent of S. Group each selected set into its overlap components.
Their integrated weights make an exact hard-core polymer gas. For atoms
put v_X=exp((sigma+1)|H_X|)alpha_X and
b_X=exp((sigma+2)|H_X|)alpha_X. The positive tree recursion

    T_X=v_X exp(sum_(Y:H_Y meets H_X) T_Y)

has supersolution b_X, since its child sum is <=eta_sigma |H_X|<=|H_X|.
Iterating from zero sums all rooted trees, permitting repeated labels in
the positive majorant. Every connected selected set admits such a tree.
Root marking and |union H_X|<=sum |H_X| bound the integrated polymer
family at rate sigma+1 by eta_sigma.

For its logarithm, order incompatibility edges and assign each connected
graph its Kruskal tree. For a fixed tree the allowed extra edges are
exactly those later than every edge of their tree path. Their alternating
sum is a sign times (1-1) to the number of optional edges, of modulus at
most one. A second rooted-tree recursion, now for polymers and including
repeated polymer labels with 1/n!, spends the remaining support unit.
The same scalar majorants bound every pinned and unpinned coefficient.
Consequently, with supports K equal to unions of full atom supports,

    log Z_barS=sum_K F_K^S,    log Z_all=sum_K F_K^all,
    sup T F_K^S <= beta_K,     sup T F_K^all <= beta_K,
    sup_v sum_(K:v in K) exp(sigma |K|) beta_K<=eta_sigma. (RM6)

Here beta_K is the absolute tree/cluster majorant, not a supremum taken
separately over an uncontrolled family of pinned expansions. It was
constructed from the same alpha_X before choosing S. This distinction
permits all subsequent sums of suprema.

For completeness multiply a selected set of atoms by z^card(I). Both
tree series converge for real |z|<2, since 2eta_sigma<=1/2. Expanding
the exponential of the connected series partitions graphs into their
components and gives the finite gas as an absolutely convergent power
series. Thus the equality holds at z=1. This identifies its real log;
the original exponentials in RM4 are independently positive. Jet product
bounds give uniform convergence of all included derivatives on compact
subsets of the open domain. No complex physical-source continuation or
additional derivative order has been invoked.

## 3. Transfer of mixed groups, with all reference readers

### 3.1 Local normalized comparison — PROVEN

Let a connected complete core H contain S and the readers of a function
F(y,W_S), including those of the S kernels. Clusters with K disjoint
from H have exactly the same integrals in RM4, since none of their
variables is pinned. They cancel coefficient by coefficient. Define

    B_S=log Z_barS-log Z_all=sum_(K:K meets H) B_(S,K),
    B_(S,K)=F_K^S-F_K^all,       sup T B_(S,K)<=2beta_K.
    sup_(y,W_S) T B_S<=2eta_sigma |H|.                   (RM7)

The exact marginal identity, with no discarded denominator, is

    int F dnu=int F exp(B_S) dmu_S.                      (RM8)

This follows directly by Fubini and RM4. A volume-sized partition factor
does not appear: all clusters not reading the core canceled before the
absolute value. Neither the vacuum log nor its derivatives were estimated
separately by an extensive supremum.

Take MS17's fixed events on m distinct cells in S, with uniform gap a>0,
and small insertions f_i whose product reads S, with sup T f_i<=s_i.
Write F=product_i f_i product_c 1_(E_c). Fixed boundaries are in
integrated coordinates; they do not get differentiated. For actual soft
kernels t>=1, put ell=5L-4, lambda=ell sqrt(N/u), and

    q_gap=t a-1-2N^2 log(1+4Nt),
    D_p(d)=sum_(r=0)^p lambda^r C_r(d t)/r!.

The C_r polynomials are defined in RM14. The product law on S has relative
fine-jet bound D_p(|S|); it has no original-source or retained-output
parameter dependence. Using RM3, RM7 and the product-kernel gap probability
therefore gives, for q_gap>=0,

    sup T int F dnu <= w_G exp(2eta_sigma |H|),
    w_G=D_6(|S|) exp(-m q_gap) product_i s_i.             (RM9)

All source derivatives of Phi and f_i are present. This is MS17 with the
explicit local reference debit 2eta_sigma |H|. If |S|<=c m and
|H|<=c_H m, m>=1, MS18 gives the per-gap price

    q_matched=q_gap-log(2^6 D_6(c))-2eta_sigma c_H.       (RM10)

It is positive only when this displayed inequality is verified. If the
core size is controlled by r+m instead, retain that actual count in RM9;
do not assign every reader to one gap for free. Mandatory future events
that make a gap certain cannot satisfy these small-tilt hypotheses with
an unchanged, arbitrarily large positive q_matched.

RM9 does not assert that its result reads only H. Expand exp(B_S) into
products of the supported B_(S,K), assigning each term its full union
Y=H union K_1 union ... union K_n. Every such union is connected since
each K_l meets H. Denote the corresponding integrated contribution A_(G,Y).
The same proof with support weights gives the stronger per-core statement

    sum_Y exp(sigma(|Y|-|H|)) sup T A_(G,Y)
                         <= w_G exp(2eta_sigma |H|).    (RM11)

Products carry 1/n! and the support inequality; summing them gives the
exponential of the anchored beta sum. Thus distant parameter readers are
retained, not renamed as a small local scalar prefactor.

There is a full-root version for one common background majorant beta_K.
Suppose RM2 holds at sigma+1 with budget
eta<=1/4 and a supplied complete core family satisfies
`d=sup_v sum_(G:v in H_G) exp((sigma+1)|H_G|)w_G<infinity`.
Then the decorated family in RM11 obeys

    sup_v sum_(G,Y:v in Y) exp(sigma |Y|) sup T A_(G,Y)
                                      <=(1+2eta)d.      (RM12)

Proof: when v belongs to H_G, the attachment exponential costs at most
exp(2eta |H_G|), absorbed by the one spare core support unit. Otherwise
mark one attachment K containing v. Its 1/n! becomes 1/(n-1)!.
Sum cores touching K by rooting them at vertices of K, costing at most
|K|d, again using 2eta<=1. The remaining sum is bounded by
`d sum_(K:v in K) 2beta_K exp(sigma|K|)|K|<=2eta d`, using
|K| exp(-|K|)<=1 and RM6 at sigma+1. Overcounting several possible
marks only increases the upper bound. Add the core-root contribution.
This explicitly includes roots on reference tails. The extra support
reserve is a hypothesis, not an indefinitely repeatable loss.
Different history-dependent backgrounds require such a common majorant
or a joint bound on their complete summed family; a uniform bound on each
history separately is not sufficient for RM12.

### 3.2 Connected output and exact factorization — PROVEN conditional form

Separate expectations under nu do not factor merely because their bare
cores are disjoint. To construct the joint connected output, expand the
background atoms and ALL new atoms together under mu, before any log.
Suppose complete integrated coefficients of every such selection factor
on full overlap components and have joint majorants alpha_X for background
atoms and gamma_i for new atoms. Write their rooted budgets at mu+2 as
eta and d, with eta+d<=1/4 and eta<1/4. These are joint jet bounds,
not products of independently normalized nu expectations.

A sufficient elementary certificate is RM2 for background atoms and,
for each new atom i, a pointwise bound T(g_i)<=s_i times its fixed event
indicators, with specified distinct gap cells owned at most once across
the selected new atoms. Set
`gamma_i=s_i product_(c in C_i) P_c exp(-sum_owned q_c)`.
Product integration bounds the simultaneous events by the product of
their gap probabilities; the union density cost is no larger than the
assigned P products. This proves the required joint inequality also in
the presence of overlapping background atoms. More efficient grouped
MS17 bounds are permissible when proved jointly with the background,
not merely asserted from separate marginal estimates. No new gap price
is available for a reused mandatory event.

Apply the two-tree proof of section 2 to the augmented alphabet and to
the background alone. Subtract the two logs. Exactly the clusters
containing a new atom remain, with their complete supports. If d>0,
multiply the majorant of each new atom by R=(1/4-eta)/d>=1. The augmented
budget becomes 1/4; every remaining log cluster gains at least R.
The positive absolute majorant therefore proves

    ||log int product_i(1+g_i)dnu||_(mu,T)
                                      <= d/(1-4eta).   (RM13)

For d=0 every nonzero new coefficient vanishes and the conclusion is
zero. This scaling argument applies to the positive cluster majorants;
it need not realize a positive physical density at the scaled activities.
Unscaled positivity/nonvanishing follows from the convergent gas identity.
An independent empty-support scalar or the ratio of two differently
normalized references keeps its own log/jet budget. In particular RM13
does not by itself identify Q_h=R_h/Z_A with a probability expectation.

This construction, or the complete jointly bounded core version, is the
needed factorization mechanism. Applying RM9 independently to two
correlated groups and multiplying their answers would not be that mechanism.

## 4. Explicit derivative bill — PROVEN

For a positive fixed-domain integral Z=int w_0 exp H, with fixed w_0>=0,
assume the weighted ordered rth scores satisfy |D_I H|<=lambda^r t.
Define polynomials with M_0=I_0=C_0=1:

    M_r(t)=sum_(pi partition [r]) t^card(pi),
    L_r(t)=sum_pi (card(pi)-1)! product_(B in pi) M_|B|(t),
    I_r(t)=sum_pi card(pi)! product_(B in pi) M_|B|(t),
    C_r(t)=sum_(s=0)^r binom(r,s) M_s(t) I_(r-s)(t).    (RM14)

The log polynomial starts at r=1. Partitioning derivative positions in
exp H, and then in log Z or Z^-1, gives respectively the coefficients
1, (-1)^(n-1)(n-1)! and (-1)^n n!. Division by the positive Z and the
triangle inequality give

    |D_I Z|/Z<=lambda^r M_r,
    |D_I log Z|<=lambda^r L_r,
    Z|D_I Z^-1|<=lambda^r I_r,
    |D_I n|<=n lambda^r C_r,     n=w_0 exp(H)/Z.        (RM15)

Order within each derivative block is retained. Differentiating
Z Z^-1=1 independently gives
`I_r=sum_(s=1)^r binom(r,s) M_s I_(r-s)`; this checks the inverse
coefficient convention. Leibniz gives the last bound. No rare-sector
mass inverse has been introduced, and no signed activity is called positive.

The complete density polynomials through fourth order are

| r | C_r(t) |
|---|---|
| 1 | 2t |
| 2 | 2t+6t^2 |
| 3 | 2t+18t^2+26t^3 |
| 4 | 2t+42t^2+156t^3+150t^4 |

They dominate M_r,I_r,L_r coefficientwise. The actual mean contains
paths of at most ell=5L-4 unitary link occurrences. An ordered rth
fine derivative has at most ell^r choices of occurrences, each costing
h_j^r. Their average therefore has norm <=lambda^r with
lambda=ell sqrt(N/u). This verifies RM15 for every actual real field,
including M=0. Output derivatives of Z_t(M) and original-source
derivatives of the prescribed kernel vanish; output derivatives of its
numerator can be included with lambda replaced by ell h_j+h_(j+1).
Earlier kernels reading a retained variable must be counted separately.

An explicit logarithmic price for one ordered rth derivative is

    d_r(u)=log max(1,lambda^r C_r(kappa u)),
    P_<=k(u)=sum_(r=0)^k lambda^r C_r(kappa u)/r! .      (RM16)

Here d_r covers relative Z and reciprocal derivatives and positive-order
log derivatives as well as density derivatives. It is not an absolute
bound on Z or Z^-1, whose zeroth-order normalization stays in the exact
law. P_<=6 is a valid P_c in RM2 for a kernel depending only on fine y.
One pays the Taylor sum P_<=k once, not each of its summands again.

For u>=1 define
`A_r=ell^r N^(r/2) C_r(kappa)` and
`A_<=k=1+sum_(r=1)^k A_r/r!`. Since every monomial of C_r has degree
at most r,

    lambda^r C_r(kappa u)<=A_r u^(r/2),
    d_r<=log max(1,A_r)+(r/2)log u,
    P_<=k<=A_<=k u^(k/2).                              (RM17)

For k=4 the total polynomial bill is at most A_<=4 u^2; for k=6 it
is at most A_<=6 u^3. Source jets of the kernel are zero, so they do
not increase these orders. Source jets of an inherited density or Phi
still require their own full mixed RM2/RGA14 bounds through total order
ten. For d simultaneously read kernels the sharper joint version is
D_k(d) from RM9, rather than suppressing the reader count. If d<=cm,
its degree bound gives the per-event bill log(2^k D_k(c)) as in MS18.

## 5. Where the bill can be paid

### 5.1 Fresh gaps — PROVEN on the fixed-event forward class

A 1/t Haar cap at a maximizer has mass at least
(1+4Nt)^(-2N^2) and exponent loss at most one. This follows by covering
the 2N^2 real matrix coordinates with cubes of side 1/(2Nt), translating
group balls by Haar invariance, and using |h_M(V)-h_M(W)|<=||V-W||op.
Factor exp(t max h_M) out of both numerator and denominator, giving the
exact density exp(-t psi_M)/int exp(-t psi_M). Its event numerator is
at most exp(-ta), so the normalized probability is <=exp(-q_gap).
This rebuilds JMBRB B-GAP.

For a differentiated connected group, subtract log(2^k D_k(c)) and the
matched cost in RM10. A threshold a=a_0 u^(delta-1), 0<delta<1, gives
`q_gap=kappa a_0 u^delta-O(log u)`, whereas the derivative debit in
RM17 is at most (k/2)log u plus a constant. Hence the residual tends
to infinity for k=4 and k=6 at fixed reader constants. This is an
all-large-u assertion proved by log(u)/u^delta ->0, not a fitted cutoff.
Full support/type entropy is debited separately before claiming smallness.

The witness with M=0 has psi_M=0 everywhere. Its normalizer cannot be
paid from a positive fresh gap. The next two payments apply instead.

### 5.2 The SU(2) witness, including its fourth derivative — PROVEN

Take MIXSMALL MS11–MS13: theta=2pi/L^2,
U_1(x)=diag(exp(i theta x_2),exp(-i theta x_2)), other links identity,
on a torus with side a multiple of L^2. Its specified unit weighted
fine direction gives

    m(s)=L^-1 sum_(r=0)^(L-1) exp(2pi i r/L)
                                  exp(i s L h_j r/(L-1)),
    m(0)=0,
    |m'(0)|=L h_j/[2(L-1)sin(pi/L)].                    (RM18)

The paired axial paths cancel individually, so this is the actual contour
mean, not a freely assigned matrix. Write W=x_0 I+i x.sigma. Haar on
SU(2) is invariant under quaternion rotations. Thus E x_0^2=1/4.
If v=E x_0^4 and w=E x_0^2 x_1^2, rotation to (x_0+x_1)/sqrt(2)
gives v=3w, and (sum x_a^2)^2=1 gives 4v+12w=1. Consequently v=1/8.
Odd moments vanish. With q(s)=|m(s)|^2, expansion of this finite compact
integral and of its real log gives

    log Z_t(M(s))=t^2 q(s)/8-t^4 q(s)^2/384+O(s^6)
                        as a function of m near zero. (RM19)

More precisely the omitted terms are O(|m(s)|^6); all coefficients up
to degree four in s follow from the displayed terms. If a=m'(0),
b=m''(0), c=m'''(0), they give

    D^2 log Z=t^2 |a|^2/4,
    D^4 log Z=(3/4)t^2 |b|^2+t^2 Re(conj(a)c)
                                      -(t^4/16)|a|^4. (RM20)

For L=3 there is an independent convenient scalar reduction:
`q(s)=(1+2cos(2pi/3+(3h_j/2)s))^2/9`.
It gives q''(0)=3h_j^2/2 and q''''(0)=-81h_j^4/8.
Substitute h_j^2=2/u and t=kappa u:

    D^2 log Z=3kappa^2 u/8,
    D^4 log Z=-81kappa^2/16-9kappa^4 u^2/64.             (RM21)

Thus the second-order cost really grows as u and the fourth-order cost
as u^2. The polynomial budget in RM17 has the correct growth order for
these witnesses; fourth order has not been treated as a value estimate.

At the original level each 12 plaquette of this field has
s=1-cos(theta)>0. More generally let a supported sector have an actually
available original reserve D>=omega c u, c,omega>0, with u<=u_0 if u
is a later coupling. For r>0 and 0<z<=omega c, differentiation of
v^(r/2)exp(-zv) gives its maximum [r/(2e z)]^(r/2). Hence

    exp(-D) lambda^r C_r(kappa u)
       <= A_r [r/(e omega c)]^(r/2) exp(-omega c u/2),
    exp(-D) P_<=k(u)
       <= A_<=k [k/(e omega c)]^(k/2) exp(-omega c u/2).
                                                               (RM22)

These statements use u>=1 and k>0; the zeroth-order scalar reserve is
retained as part of the exact weight. In particular k=4 costs at most
`A_<=4 [4/(e omega c)]^2`, leaving half the exponential reserve; k=6
costs `A_<=6 [6/(e omega c)]^3`. This verifies affordability at every
u>=1 with explicit constants, not merely an asymptotic slogan.

For the exact original SU(2) witness take c=1-cos(theta) and one distinct
owned 12 plaquette per charged normalizer, or divide its fraction among
all readers sharing it. A neighborhood also works: if its link radius
is <=d_theta/8, d_theta=2sin(theta/2), telescoping gives plaquette
distance >=d_theta/2 and c=d_theta^2/(8N). Charges refer to the actual
original action. At j>0, current curvature is not itself original action;
the analogous D bound is a named ancestor-charge input. CHARGE C6's
geometric allocations are valid for its filled family, not a theorem
that every present rough cell has such an ancestor. Its extensive cap
comparison cannot be substituted for a local matched bound.

For several factors, choose fractions omega_(factor,p) whose sum,
including earlier gap, regulator and other uses, is <=1 on each original
plaquette. Then multiply the pointwise bounds with those fractions.
Alternatively use one group score polynomial and one joint reserve.
Never divide out the mandatory original mass and use it again. RM22
bounds the normalizer multiplier inside the charged integrand. Conversion
to a normalized inherited coefficient still needs the uncharged integral
and its matching denominator on that same law.

### 5.3 Large-field regulator and the general short-mean class — PROVEN

Let `delta_M=1-max_W h_M(W)`. For every output V the actual nonnegative
kernel energy in REALRGA RGA5 satisfies
`t(1-h_M(V))>=t delta_M`. If delta_M>=epsilon>0 on a sector,
an unused regulator allocation exp(a_reg E), a_reg>0, therefore gives

    sup_sector lambda^r C_r(kappa u)/exp(a_reg E)
       <= A_r [r/(2e a_reg kappa epsilon)]^(r/2),
    sup_sector P_<=k(u)/exp(a_reg E)
       <= A_<=k [k/(2e a_reg kappa epsilon)]^(k/2).      (RM23)

The same maximization proves this for u>=1. Here E includes the owned
kernel energy, and r,k>0. This is a regulated seminorm estimate; it does
not differentiate the regulator denominator or assert its integrability.
The Taylor norm includes its order-zero term already in P_<=k.

At the SU(2) witness M=0, delta_M=1, so RM23 pays the whole jet with
the actual kernel-energy term regardless of V. More generally
||M||op<=1-epsilon suffices. The SU(N) embedded means
`M=diag(m,conj(m),1,...,1)`, |m|<=1-epsilon, satisfy
`max h_M<=(N-2+2|m|)/N<=1-2epsilon/N`: use trace duality with the
sum of singular values, proved by diagonalizing M and bounding each
unitary diagonal entry by one. Thus RM23 applies with 2epsilon/N even
though the operator norm of this embedded M can equal one. These means
are realized by the embedded contour construction, including m=0.

For any more general sector with available energy E>=c u^delta,
c,delta>0, the same elementary optimization gives

    sup_(u>=1) u^(k/2) exp(-a_reg c u^delta)
       <= [k/(2delta e a_reg c)]^(k/(2delta)).          (RM24)

This states exactly the growth needed to pay the derivatives. It does
not assert an exhaustive uniform energy lower bound on unrestricted
fields. On the remaining low-energy sector one needs the appropriate
small-field kernel estimate, named KR, or another complete joint bound.

The regulator currency is not a fourth independent source of probability:
integrating it requires RGA14 on the same actual reference. Overlapping
factors add multiplicities, G_m G_n=G_(m+n). If original action pays those
moments, it consumes the original fractions in RM22 and cannot also be
counted as a second untouched reserve. Current kernel energy is not a
replacement for original-law coercivity. These joint moments and the
all-history coverage are **OPEN**, assigned to the matching/TC interface.

## 6. One complete real RG step — PROVEN conditional theorem

Fix the finite-q contract p=6,q=4, all original source weights, positive
coupling range, graph, support rate mu and real domain margins. Supply a
stable class of states and retain its complement. The following are
uniform over the stated finite volumes, depths and histories.

1. **Step-j state, used as input.** H0–H4 and the finite source-record
   part of H6 hold at j, with their exact unnormalized masses, reference,
   relevant data and x_j<=M. H1 supplies the current real derivatives;
   H2 supplies the actually unused charge/regulator allocations. H3's
   existing coefficients can be used as background only after their
   full readers and their norm conversion have been verified. No H3 at
   j+1 or future conditioned gap estimate is assumed in this step.
2. **MATCH and background production.** An explicit construction from
   that state gives RM1 on each used sector, including the main-action,
   hard-support, inherited/bare and endpoint normalization accounting.
   It gives RM2 at the support rate needed for the selected use of
   RM9–RM13. Prefactor and source-scalar logs have separate supplied
   budgets. The product-cell laws and all coefficients are those of
   the same integral. This is additional to the literal H(j).
3. **New joint atoms and payments.** Every fresh-gap and rough group
   has a complete joint majorant, with RM16–RM24 charged once. The
   augmented product expansion of section 3.2 has eta+d<=1/4; or a
   separately constructed exact, factorizing mixed representation has
   RGA16 with Q<=1/4. All types and histories occur in the rooted sum,
   including roots on tails. The same stronger representation/support
   reserves required of the next state are regenerated from the input
   ball; a spent reserve is not copied from the preceding step.
4. **SEL, HOLE and extraction.** Supply EXTCONT SEL and HOLE, including
   current selector boundaries, all required field jets and fixed-domain
   transports; arbitrary-hole costs require its joint differentiated
   E15 or a compatible alternative. Supply its physical EXT and COEFF:
   exact symmetry-compatible extraction, actual returned linear bound,
   quadratic activity remainder, all source/vacuum counterterm recursions
   and their admissible ranges. LOCOP may replace only a corresponding
   proved operator input when available; none is imported in this snapshot.
5. **Transition budget.** After ALL preceding losses, actual operators
   have nonnegative bounds lambda,B,C,s_j,eta_j,e_j such that

       x_(j+1)<=(lambda+B s_j+eta_j)x_j+C x_j^2+B e_j,
       theta=lambda+B s_*+eta_*+C M<1,
       B e_*<=(1-theta)M.                              (RM25)

   Require M>0 and the uniform upper bounds
   0<=s_j<=s_*, 0<=eta_j<=eta_*, 0<=e_j<=e_* at every admitted input.
   Here eta_j is a failure-operator bound, unrelated to the background
   budget eta in RM13. It includes every coherent, chart and completion
   failure. Fresh-gap creation probabilities cannot replace these
   homogeneous operator estimates.

**Conclusion.** Exact transfer, new supported real logarithms, complete
extraction and finite marked source records yield H0–H4 and finite H6
at j+1, with x_(j+1)<=M. RM25 verifies the required H5 transition for
this step. The conclusion includes the declared prefactor/relevant
budgets only because hypotheses 2 and 4 propagate them separately.

**Proof.** Use the exact matching identity before estimating. RM5 and the
augmented expansion give factorization and complete joint jets; the two
tree estimates give the local log. RM7–RM12 give the stated mixed-gap
comparison wherever that sharper version is used. SEL/HOLE preserve the
declared derivatives, supports and all complementary sectors. Exact
extraction preserves the generating function while COEFF records every
removed coefficient, including source-only scalars. Finally
`C x_j^2<=C M x_j` gives
`x_(j+1)<=theta M+B e_*<=M`. Original-source differentiation of this
exact identity carries all fifteen nonempty four-label subsets, including
the subsequent outer-cumulant terms. This proves the one-step assertion.
If the displayed construction and constants are reproduced at every
input state, ordinary induction applies to every finite depth.

This is a sufficient theorem, not a reduction to a manifestly weaker
remaining lemma. EXT/COEFF already include substantive RG operator work.
RENEW's extracted window bounds or a common summable creation-lag envelope
may replace the one-step continuation route with their additional nonlinear
and coefficient estimates. Its plain-forward rough orbit supplies neither.
The finite q=4 theorem supplies no all-order hierarchy, matching coefficient,
common continuum limit, Euclidean symmetry or spectral mass gap.

## 7. Remaining obligations and verification

| Obligation | Status and next discriminating work |
|---|---|
| Exact inherited-to-product reference, with fixed support and full main action | **OPEN.** Construct RM1 on an actual mixed history, or a nonperturbative cell version with the same pinned bounds. Preserve rho/b_j and all endpoint masses. |
| Differentiated background smallness and regeneration | **OPEN.** Establish RM2 or its uniform pinned joint substitute in the required fixed norm. Small integrated signed residuals alone do not supply it. |
| Fixed-gap comparison given these inputs | **PROVEN**, RM7–RM13. The local loss and complete tail supports are explicit. |
| Zero-mean/short-mean normalizer payment | **PROVEN** pointwise/regulated results, RM21–RM24. Original-level ownership is explicit. |
| Complete inherited-law rough-sector integration | **OPEN.** Show the same-law original-charge/regulator moment estimate with all overlaps, source jets, readers and history sums. |
| Current selections, arbitrary holes, extraction and coefficients | **OPEN** actual EXTCONT inputs. Their conditional composition is proved above; LOCOP is absent. |

**ARGUED next construction.** Start with one bounded mixed core on a fixed
positive sector. Open its inherited ancestry and write the actual paired
numerator/reference on identical variables. Absorb its nonperturbative main
action into an explicitly specified reference before testing RM2; any
nonproduct cells must have the uniform pinned estimates needed in section 2.
Retain a fine/coarse derivative and all four original source labels. On
the short-mean complement use RM23 with its joint moment, or RM22 with a
verified original reserve. Only then test the rooted augmented budget and
the operator inequality. This proposal is not claimed executed here.

No route-exhaustion, physical no-go or independent-wall count is asserted.
The live alternatives include an adapted interacting cell reference,
joint integration with cancellations, weighted readers, and charged or
extracted continuation. Their outstanding estimates overlap. The supplied
finite model is the mathematical premise; no framework axiom or primitive
has been added, rejected or identified as the missing analytic estimate.

The preregistered finite diagnostics are
[checks/refmatch_criteria.md](checks/refmatch_criteria.md). They check a
normalized three-cell calculation, the SU(2) fourth derivative and score
combinatorics, not the OPEN all-history hypotheses. Actual execution status,
fresh hostile review, fixes and final source hashes are recorded in the log.
