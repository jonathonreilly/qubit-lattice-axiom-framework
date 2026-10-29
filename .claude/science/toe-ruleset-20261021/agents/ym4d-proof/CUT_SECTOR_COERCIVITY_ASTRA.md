# Local energy tails in the original cut measure

**Author unit; fresh independent review required.** This supplies an actual
normalized conditional tail estimate at fixed real coarse V, with a local
reference and its complete boundary cost. Its input is the original Wilson
measure with normalized paired S4-prime kernels. It does not replace that
measure by a Gaussian or by SA's selected sector.

The deterministic part controls the complete rooted-tree free field by Wilson
curvature and the kernel's own centered mismatch, on all compact fields.
The normalized part has two forms: an excess-energy tail above the actual
conditional minimum, and a local reference-cap comparison with a smaller
polynomial exponent.
The latter requires no additional smallness ceiling on the original interior
cut. It leaves a concrete coarse-curvature and exterior-reader cost, rather
than an unspecified denominator. The cost is not proved absorbable for all
boundaries of the complementary regions in SA32.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Original-law local energy coercivity and conditional tail bounds, with explicit localized reference/boundary payment; full connected normalized complement remains open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The antecedents are Bałaban's localization and large-field constructions and
Dimock's expositions. Consumed finite-dimensional steps are proved below.
Literature is attribution and scope comparison. Existing [STEP55](STEP55.md),
[its review](CODEX_REVIEW_STEP.md), [NODEA55](NODEA55.md),
[NODEA_RES55](NODEA_RES55.md), [H](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md),
[Sea](SOURCE_SEA_CONSTRUCTION_ASTRA.md), [CB](COVARIANT_SOFT_BACKGROUND_ASTRA.md),
[CC](COVARIANT_COMPLEMENT_ASTRA.md), and [SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md)
were inspected before selecting this producer. The exact read inventory is
[here](checks/cut_sector_coercivity_read_manifest.json). This author previously
reviewed CC; the CC source, checks and review remain immutable. This source
has not been independently reviewed by its author. CS1–CS29 are proved here
from the displayed model; CS30–CS33 are explicitly scoped implications using
the frozen SA, CB and H inputs, not upgrades to those inputs' standing.

## 1. Exact law and local variables

Fix d=4, SU(N), N>=2, odd L>=3, coarse torus side T>=2, u>=1, and
`0<kappa_-<=kappa<=kappa_+`. The fine torus has side LT, and its blocks are
`B_X=LX+{-h,...,h}^4`, with root LX and h=(L-1)/2. Count every positive
fine link and every unoriented elementary plaquette once. Fix epsilon_1>0;
the original cut chi_cut is the product, over blocks, of the indicators that
every plaquette entirely internal to that block has operator defect strictly
less than epsilon_1. No crossing-face plaquette or root mismatch is cut.
These geometry/action/kernel choices are supplied mathematical model data;
no claim derives them from the framework axioms or adopts a new physical
primitive. No observed value or fitted selector enters. Put D=N^2-1.
Norms without an operator subscript below use

    |A|_n=||A||HS/sqrt(N),   <A,B>_n=Re tr(A*B)/N,
    s(P)=1-Re tr(P)/N=|I-P|_n^2/2.                         (CS1)

Group distances used in caps are the UNNORMALIZED HS geodesic distance.
Every Haar measure is probability Haar. The source e is real, with
`|e_p|<=rho<1`; only original Wilson coefficients vary. The exact density is

    w_e(U,V)=exp[-u sum_p(1+e_p)s(U_p)] product_c k_t(V_c;M_c(U)),
    t=kappa u,   M_c=(24L^4)^(-1) sum_tau P_(c,tau)(U),
    m(M)=max_(Q in SU(N)) <Q,M>_n,
    psi_c=m(M_c)-<V_c,M_c>_n,
    Ntilde_t(M)=int exp[-t(m(M)-<Q,M>_n)]dQ,
    k_t(V;M)=exp[-t psi_M(V)]/Ntilde_t(M).                 (CS2)

These are the arithmetic means of the actual paired root-leg/straight/root-
leg words, with the same coordinate order at both endpoints. Their lengths
are at most p_L=5L. The original `exp[-t(1-<V,M>)]` kernel and its original
normalizer give CS2 by canceling the identical `exp[-t(1-m)]`; no field-
dependent factor is deleted. In particular the tree energy is centered:

    E^e(U,V)=sum_p(1+e_p)s(U_p)+kappa sum_c psi_c.          (CS3)

Its nonnegative terms are not the complete finite-u negative log density;
the remaining `sum_c log Ntilde_t(M_c)` is kept below.

Use the pinned axial tree in every block B_X: the parent of a nonroot site
moves its highest nonzero coordinate towards the root. There is a unique
root-pinned transform setting every tree edge to I. Given the vertex group
variables on that tree, left/right Haar invariance transforms each remaining
edge independently to its tree-gauge value W_e. Successive leaf integrations
therefore give exactly

    product_links dU=product_(nonroot vertices)dg
                     product_(free positive links)dW,
    m0=3L^4+1,       number of free links=m0 T^4.           (CS4)

Indeed each block owns 4L^4 positive fine links and has L^4-1 tree edges.
Every source, kernel and original interior-plaquette cut is invariant under
these root-pinned transformations. Thus CS4 pushes the original measure to
product Haar on the free links with integrated tree volume one. Root degrees
of freedom and all winding information remain in W. There is no metric-
slice determinant. A conditional in W is expressly not being identified with
a conditional obtained by fixing the ungauged fine exterior links.

The reference U0(V) has internal links I and each positive crossing link
through face c equal to V_c. Every actual P_(c,tau)(U0)=V_c. Its only
nontrivial fine plaquettes lie at double faces and are the corresponding
coarse plaquettes. Thus arbitrary real holonomies are retained. Set
`delta_V=max_P ||I-V_P||op`.

For a nonempty set R of coarse blocks, let J_R be ALL free positive links
whose starting fine vertex lies in R. Thus |J_R|=m_R=m0|R|. Let

- P_R be every fine plaquette reading a link of J_R;
- C_R be every coarse kernel whose actual paired words read J_R;
- K_R be the coarse blocks containing endpoints of links in J_R.

Read sets include inverse occurrences; cancellation is not assumed. Every
free fine link reads six plaquettes. An internal link can enter only kernels
with its own block as an endpoint; a crossing link enters its one coarse
face kernel. Consequently

    |P_R|<=6m_R,   k_R:=|C_R|<=8|R|,
    K_R subset N_1(R),   |K_R|<=5|R|.                     (CS5)

Here N_1 uses coarse sup distance. The full field/coefficient reader of P_R
and C_R lies in N_1(R), at most 81|R| blocks, including wrapping labels.
K_R's sharper count uses the four positive outgoing neighbors. The source
reader is exactly P_R; coarse links read by C_R are retained as such.

Fix all free variables outside J_R to z. An admissible exterior has its
outside-block interior cuts satisfied. The remaining cut chi_R consists
exactly of the interior plaquette cuts in blocks R. A crossing link is in no
such cut. The conditional law of the original measure is

    nu_R^e(dW|z,V)=D_R(z,V,e)^(-1) chi_R exp[-u E_R^e(W|z,V)]
                  product_(c in C_R) Ntilde_t(M_c)^(-1) product_(e in J_R)dW_e,
    E_R^e=sum_(p in P_R)(1+e_p)s(U_p)+kappa sum_(c in C_R)psi_c.  (CS6)

Every action/kernel factor outside these readers cancels exactly. D_R is
positive. No power of the total lattice volume has entered CS6. Statements
about conditionals are almost everywhere; the explicit local formula also
defines an extension for every admissible real z,V.

## 2. Nonabelian curvature allocation on actual words

A lifted block or two-block brick carries only the faces inside that lift.
For a coarse link c, its brick contains its two endpoint blocks and their
single common face. The extra far seam of the torus-induced graph at T=2
is excluded. Every actual paired transporter for c and its root-straight
path S_c lies in this brick.

Here is a useful filling construction without logarithms. Inside a rectangular
box choose coordinate-order paths rho_x from one base vertex to each vertex.
In `rho_x e rho_y^(-1)` for an edge e:x->y, commute the last edge step past
later-coordinate steps and cancel adjacent inverses. Each interchange is one
conjugated elementary plaquette; at most the sum of box widths is used.
Negative steps and zero coordinates obey the same operation. Multiply these
dressed-edge identities along a closed path; all intermediate tree paths
cancel. Thus a loop of length ell is a product of at most ell times the
width sum conjugated plaquettes, with repetitions retained.

The relevant loops have length <6L and brick width sum <5L. Fix

    B=30L^2.                                               (CS7)

For a word P_(c,tau) versus S_c, let n_(c,tau,p) be the multiplicities in this
explicit filling and set a_(c,p)=average_tau n_(c,tau,p). They are nonnegative,
supported on the brick, and `sum_p a_(c,p)<=B`. For any product of q unitaries,
telescoping and Cauchy--Schwarz give

    |product_j Q_j-I|_n^2 <= q sum_j |Q_j-I|_n^2.

Conjugation and inversion preserve this norm. Hence, with
`q_c=average_tau |P_(c,tau)-S_c|_n^2`,

    q_c<=2B sum_p a_(c,p)s(U_p)
        <=2B^2 sum_(p in brick(c))s(U_p).                 (CS8)

No curvature smallness, chart, or commutativity is required. Each fine
plaquette belongs to at most eight such labelled bricks: an internal
plaquette is in the eight bricks incident to its block; a single-face
plaquette has its one face label; a double-face plaquette is in none.
This remains true at T=2, where opposite face labels are distinct.

For comparison with CC23, the exact Hilbert-space identity gives

    v_c:=1-|M_c|_n^2=average_tau |P_(c,tau)-M_c|_n^2<=q_c,
    |M_c|_n^2<=m(M_c)<=|M_c|_n<=1.                        (CS9)

The first bound in the second line follows by averaging the admissible
competitors P_(c,tau). In particular the kernel's cancellation of the
variance term is harmless for CS8: Wilson curvature pays it explicitly.
A useful sharper route to the root mismatch is to put d=|S_c-V_c|_n. Since
`m(M_c)>=<S_c,M_c>_n`,

    d^2/2=<S_c-V_c,S_c>_n
          <=psi_c+d |S_c-M_c|_n<=psi_c+d sqrt(q_c).

Using `d sqrt(q)<=d^2/4+q` proves

    |S_c-V_c|_n^2<=4psi_c+4q_c
                   <=4psi_c+8B^2 sum_(p in brick(c))s(U_p). (CS10)

There is no polar maximizer, nondegeneracy assumption, or N-dependent sign
error in this inequality. In particular it does not invoke STEP55's GMI
coefficient, whose all-N sign needs the additional condition in its review.

For an internal free edge, its tree loop is filled in its block. For a
crossing free edge e on face c, fill its dressed root-to-root path against
S_c in the same brick. CS7 and the squared triangle inequality give

    |W_e-I|_n^2<=2B^2 sum_(p in B_X)s(U_p)              (internal),
    |W_e-V_c|_n^2<=20B^2 sum_(p in brick(c))s(U_p)+8psi_c (crossing). (CS11)

The crossing constant is `2(2B^2)+2(8B^2)=20B^2`. Summing with multiplicities,
there are fewer than 4L^4 internal free links per block and exactly L^3
crossing links per positive coarse face. Therefore

    sum_free |W_e-U0_e|_n^2<=C_F sum_p s(U_p)+C_psi sum_c psi_c,
    C_F=8B^2 L^3(L+20),   C_psi=8L^3,
    E^e>=c_link sum_free |W_e-U0_e|_n^2,
    c_link=min((1-rho)/C_F,kappa_-/C_psi)>0.               (CS12)

This is absolute nonlinear energy coercivity, uniformly in volume and in
arbitrary real V. It does not assert convexity, a fluctuation covariance, or
coercivity of `E-E(U0)`.

The local version has an exact support qualification. Let I consist of
internal free links of blocks R and crossing links whose BOTH endpoint
blocks belong to R. Their block/brick fillings belong to P_R and their
kernel labels to C_R; each elementary plaquette of such a brick has a free
edge in J_R. Thus CS12 holds with E_R, the sum over any subset I, and the
same constants. More generally the same proof works when these complete
filling/phase supports are contained in P_R,C_R; no truncated brick is used.

For distinct fine plaquette labels A subset P_R and distinct coarse-link
labels C subset C_R with every plaquette of each full brick in P_R, define
the event

    D_(A,C): ||I-U_p||op>=delta_f (p in A),
             ||S_c-V_c||op>=eta (c in C),
    H_(A,C)=[delta_f^2|A|+eta^2|C|]/N,
    c_def=min((1-rho)/(2+64B^2),kappa_-/4).                (CS13)

On this simultaneous event, CS1, CS8–CS10 and the eight-brick count give

    H_(A,C)<= (2+64B^2) sum_(p in P_R)s(U_p)
                       +4 sum_(c in C_R)psi_c,
    E_R^e>=c_def H_(A,C).                                 (CS14)

The labels need not be independent or disjoint in space. Their shared
readers were paid by the explicit multiplicity. Connected labels are
allowed, but CS14 alone is not a connected logarithm estimate.

## 3. The actual compact normalizer, including degenerate means

Let `r_H=min(1,pi/(2sqrt(N)))`. The exp map on an HS ball of that radius is
injective. Its differential has Cartan determinant one and a sinc-squared
factor on each real root plane. The root half-angle is at most r_H; hence
its Jacobian is bounded below by
`j_H=(sin(r_H)/r_H)^(N(N-1))`. With v_D the Euclidean unit-ball volume and
Vol_HS the Riemannian SU(N) volume, put

    c_H=j_H v_D/Vol_HS(SU(N)).

The exponential image of an HS ball of radius r<=r_H has probability Haar
mass at least c_H r^D and lies in the group geodesic ball of radius r. These
are original group volumes, not an angular proxy.

For any arithmetic mean M of SU(N) matrices, choose an actual maximizing
Q_max in SU(N). It exists by compactness, even when it is not unique. For
A in su(N), the real function `f(s)=<exp(sA)Q_max,M>_n` has f'(0)=0 and
`|f''(s)|<=||A||HS^2/N`, since `||M||op<=1`. Taylor's integral formula yields
`0<=m(M)-f(1)<=||A||HS^2/(2N)`. Integrating the cap of radius
`r_H/sqrt(1+t)` at this maximizer proves

    c_* (1+t)^(-D/2)<=Ntilde_t(M)<=1,  t>=0,
    c_*=c_H r_H^D exp[-r_H^2/(2N)]>0.                     (CS15)

No derivative of the maximizer is taken. The bound includes M=0. Thus, with
`C_norm=max(1,c_*^(-1) max(1,kappa_+)^(D/2))`,

    1<=Ntilde_(kappa u)(M)^(-1)<=C_norm (1+u)^(D/2).         (CS16)

The scalar prefactor C_norm and its polynomial remain in every estimate
below. Its D/2 exponent comes from stationarity at an actual compact maximum, not from replacing the group
integral by a Gaussian.

## 4. Uniform conditional excess-energy tail

This subsection additionally assumes the explicit CC7 cut ceiling. Write
`A_cut=3(L-1)/2` and require

    0<epsilon_1<=min(1/4,1/(32A_cut),1/(384A_cut^2),pi/(8NA_cut)). (CS17)

Only the interior-plaquette cut uses epsilon_1. Define the exact conditional
minimum on its closed compact domain,

    e_R(z,V,e)=min_(closed chi_R) E_R^e.                   (CS18)

A cap construction inside the open cut follows directly from its actual
geometry. In tree gauge, sliding an off-tree edge through its later-coordinate
suffix uses at most A_cut interior plaquettes. Thus
`||I-W_e||op<=A_cut epsilon_1` and its principal logarithm a_e is traceless,
with `||a_e||op<=2A_cut epsilon_1`; the eigenangle sum is a multiple of 2pi
of absolute value <pi. Set tree logs to zero. For each interior plaquette
`P(t)=product_4 exp(±t a_e)`, the logarithm satisfies

    ||log P(t)-t log P(1)||op
          <=192 A_cut^2 epsilon_1^2 t(1-t).

Indeed the sum of the four log norms is at most 8A_cut epsilon_1<=1/4;
`||P'||<=s`, `||P''||<=s^2`, and the matrix-log series bounds its second
derivative by 6s^2. The zero-endpoint Green kernel gives the displayed
half-factor. Write theta=2arcsin(epsilon_1/2). CS17 bounds the error
coefficient by theta/2. Thus `||log P(t)||op<=theta[1-(1-t)/2]`. On [0,theta] the derivative
of `2sin(x/2)` is at least 1/2. Since theta>=epsilon_1, the plaquette defect
is at most `epsilon_1-epsilon_1(1-t)/4`.

For `r<=epsilon_1/64`, choose `t=1-32r/epsilon_1`. Contract only the interior
free links in each block of R and leave its crossing centers unchanged.
Every interior plaquette has slack at least 8r. The center moves each
interior link by HS geodesic distance at most `C_g r`, with
`C_g=64sqrt(N) A_cut`. Independent radius-r balls on ALL m_R free links lose
at most 4r on a plaquette, so their product stays in chi_R. All tree links
remain I. This is a cap in the exact Haar quotient of CS4, not a claim that
CC13's original-link density had a smaller dimension.

Take `r_*=min(r_H,epsilon_1/64,1)`, `r=r_* /(1+u)`. On this cap each link is
within `(C_g+1)r` of the minimizing configuration. Since m is one-Lipschitz
in operator norm, psi is two-Lipschitz in M. Word telescoping gives

    |E_R^e(W)-E_R^e(W_min)|<=Lambda |R| (C_g+1)r,
    Lambda=24(1+rho)m0+16kappa_+ p_L.                     (CS19)

All adjacent action and kernel readers are present in this estimate.
The denominator in CS6 is at least

    D_R>=exp[-u e_R-b_cap|R|](c_H r_*^D)^(m_R)(1+u)^(-D m_R),
    b_cap=Lambda(C_g+1)r_* .                               (CS20)

Here the inverse centered normalizers are bounded below by one. On the event
`E_R^e>=e_R+Delta`, the numerator is at most
`C_norm^(k_R)(1+u)^(D k_R/2)exp[-u(e_R+Delta)]`, since its remaining Haar mass
is at most one. Therefore for every Delta>=0,

    nu_R^e(E_R^e>=e_R+Delta |z,V)
       <=min(1, Pi_R(u) exp[-u Delta]),
    Pi_R(u)=exp[b_cap|R|](c_H r_*^D)^(-m_R) C_norm^(k_R)
                       (1+u)^(D(m_R+k_R/2)).             (CS21)

In particular `log Pi_R<=[c_pref,0+c_pref,1 log(1+u)]|R|` with finite constants
independent of T,R,z,V,u. This is a normalized original-law estimate for
arbitrary real exterior data. Its center is the actual CONDITIONAL minimum;
an exterior that forces a large minimum is not asserted to concentrate near
U0 or the selected critical field. No extra convexity hypothesis is used.

## 5. A concrete local reference pays the denominator

There is a useful alternative that needs only epsilon_1>0, not CS17. Define
W^R(z,V) by replacing every free link of J_R by U0_e(V), leaving every exterior
free link z unchanged. Its interior plaquettes in R are I, so it lies strictly
inside chi_R. Define the nonnegative comparison phase

    phi_c=1-<V_c,M_c>_n=average_tau |P_(c,tau)-V_c|_n^2/2,
    A_R^e(W)=sum_(p in P_R)(1+e_p)s(U_p)+kappa sum_(c in C_R)phi_c,
    A_ref=A_R^e(W^R),      E_R^e<=A_R^e.                  (CS22)

The last inequality is m<=1. A_R is used to lower-bound the denominator on
a cap, not substituted for the original density or for the tree energy.
All field-dependent centered normalizers remain bounded as in CS15–CS16.

Fix zeta>0 and `s_*=min(r_H,epsilon_1/8,1)`. Put
`r=s_*/sqrt(1+u)`. On the product of radius-r HS balls around W^R, chi_R=1:
its formerly identity interior plaquettes move by at most 4r<=epsilon_1/2.
For every p or actual word, telescoping gives an increase of its normalized
chord distance by at most 4r or p_L r, respectively. Applying
`(x+y)^2<=(1+zeta)x^2+(1+1/zeta)y^2` term by term proves

    E_R^e(W)<=A_R^e(W)
       <=(1+zeta)A_ref+C_zeta |R| r^2,
    C_zeta=(1+1/zeta)[48(1+rho)m0+4kappa_+ p_L^2].        (CS23)

The product Haar cap and the lower bound one on every inverse centered
normalizer yield

    D_R>=exp[-(1+zeta)u A_ref-C_zeta s_*^2|R|]
                (c_H s_*^D)^(m_R)(1+u)^(-D m_R/2).        (CS24)

Consequently any event E with a pointwise lower bound `E_R^e>=Lambda_E` obeys

    nu_R^e(E|z,V)<=min(1, Pi_ref,R(u) exp[-u{Lambda_E-(1+zeta)A_ref}]),
    Pi_ref,R(u)=exp[C_zeta s_*^2|R|](c_H s_*^D)^(-m_R)C_norm^(k_R)
                       (1+u)^(D(m_R+k_R)/2).             (CS25)

The improved power comes from the reference cap's quadratic distance bound.
The cost A_ref is an actual function of the fixed exterior, the original local source and V. It
has not been discarded as a vacuum. This theorem holds for every admissible
exterior, including those for which its right side is one.

To exhibit the cost's support, let P_R^boundary be the plaquettes in P_R
reading a free link outside J_R; define C_R^boundary similarly using ALL
paired words. Let beta be the maximum of `|z_e-U0_e|_n` over those exterior
free readers, with beta=0 when there are none. Let
`partial_1 R={X in R:N_1(X) is not a subset of R}`. Every boundary reader
contains a J_R link owned by this inner collar, so

    |P_R^boundary|<=6m0|partial_1R|,
    |C_R^boundary|<=8|partial_1R|.                        (CS26)

For a nonboundary reader, W^R agrees with U0 on the entire word. Otherwise,
`|I-U_p(W^R)|_n<=delta_V+4beta` and
`|P_(c,tau)(W^R)-V_c|_n<=p_L beta`. Thus

    A_ref <= 2sum_(p in P_R)(1+e_p)s(U0_p)
          +[16(1+rho)|P_R^boundary|
                          +(kappa_+ p_L^2/2)|C_R^boundary|]beta^2
       <= a_bulk delta_V^2 |R|+a_boundary beta^2 |partial_1R|,
    a_bulk=6(1+rho)m0,
    a_boundary=96(1+rho)m0+4kappa_+ p_L^2.                 (CS27)

The first bulk term keeps the original source coefficients and reads only
the coarse plaquettes of these local double-face readers; replacing it by
`(1+rho)delta_V^2|P_R|` gives the second line.
All constants and reader collars are explicit. This is a LOCAL bulk and
boundary cost, not `exp(constant*u*delta_V^2*total_volume)`. For R equal to
the whole torus the boundary is empty and the bulk is extensive, as it must
be; that special use is not promoted to a localized reference comparison.
A relative-collar condition beta<=beta_0 is sufficient to insert beta_0 in
CS27. It is not a conclusion about an arbitrary exterior or about merely
excluding defect cores. Full boundary word readers matter.

For example, on D_(A,C), CS14 supplies `Lambda_E=c_def H_(A,C)`. If the
ACTUAL right side of `(1+zeta)CS27` is at most half this charge, then

    nu_R^e(D_(A,C)|z,V)<=Pi_ref,R(u) exp[-u c_def H_(A,C)/2].    (CS28)

One can absorb the polynomial only after lowering the exponential rate
again, or leaving it explicit. The condition just stated is a verifiable
boundary/reference budget, not a proved property of all complement regions.
Likewise, if I has the complete supports required after CS12 and
`|W_e-U0_e|_n>=r_0` for every e in I, use
`Lambda_E=c_link r_0^2|I|`. Overlapping readers are already included.

The useful integrated form needs no independence of exterior events. If
R_out>=0 is bounded and independent of J_R, then for any b>=0,

    E_(nu_cut^e)[R_out 1_(A_ref<=b) 1_E]
      <=Pi_ref,R(u)exp[-u{Lambda_E-(1+zeta)b}]
                    E_(nu_cut^e)[R_out 1_(A_ref<=b)].     (CS29)

This follows by disintegration in the exact conditional CS6. The source-only
terms outside P_R and their vacuum factors cancel inside the conditional;
they remain in both outside expectations. CS29 addresses the local
normalization that a bare pointwise energy price leaves unpaid. For a whole
source domain one may use the source-independent exterior event that the
last right side of CS27 is <=b. That expression uses the fixed bound rho,
so it dominates A_ref uniformly without changing the insertion with e. A
family using the varying indicator `1_(A_ref^e<=b)` is a real bound only;
no source holomorphy of that varying-indicator family is inferred.

## 6. Exact relationship to both SA complementary sectors

The strong-good event G requires all fine plaquette defects <delta_f and all
actual root-straight mismatches <eta, with delta_f<=epsilon_1. A failure of G
has an actual plaquette or root-link witness. CS13–CS14 and CS25 price any
specified witness family whose complete supports are inside the region's
local readers, subject to the explicit CS27 cost. Taking an arbitrary
exterior to have small beta, replacing a brick by its core, or treating a
root-path condition as an interior cut would invalidate that application.

There is also a direct deterministic bridge for G minus Omega. Here and only
here consume SA's admitted real-V domain and SA15's actual fixed sector:

    a=b_0+sigma C_0 y,    sigma^2=N/u,
    C_0=K_*^(-1/2), K_*=F_0''(b_0),    |y_i|<=p.

The G-to-chart hypotheses of CB21–CB24 are retained, so every configuration
in G has the unique traceless link logs a in this chart. SA14 supplies a
volume-uniform scalar absolute row bound M_C on C_0. The actual precision
has a scalar row bound M_K: its finite-range Hessian vertices on the admitted
chart give one, or one may use `M(K_b)+Q(Delta_0)` from SA14. Consequently

    M_T:=max(1,M_K M_C)>=max_i sum_j |(K_* C_0)_ij|,
    K_* C_0=K_*^(1/2).                                    (CS30)

This is a matrix identity for the complete colour precision, not independent
whitening by colour or an operator-norm-to-row-norm substitution. If a point
of G lies outside Omega, `|y_i|>p` for some scalar coordinate. Hence
`max_j |a_j-b_0,j|>sigma p/M_T`. Since
`max_j |b_0,j|<=C_b delta_V`, the additional explicit curvature margin

    C_b delta_V<=sigma p/(2M_T)                           (CS31)

implies some free link has HS log norm greater than `sigma p/(2M_T)`.
The chart's eigenangles are in [-pi,pi], and
`|exp(A)-I|_n>=2||A||HS/(pi sqrt(N))`. Therefore

    G minus Omega subset union_(free e)
           {|W_e-U0_e|_n>r_p},
    r_p=p/(pi M_T sqrt(u)).                               (CS32)

This geometric implication concerns the actual SA cube and its real Haar
image. It keeps the background shift, the complete scalar matrix and all
holonomies. For each specified witness e, one block suffices if it is
internal and its two endpoint blocks suffice if it is crossing; the local
CS12 and CS25 then give charge
`u Lambda_E=c_link p^2/(pi^2 M_T^2)`. The boundary/reference term and local
polynomial still have to be paid.

For these fixed-size local regions, the polynomial's logarithm is O(log u).
Choosing, for example, `p=(log(2+u))^alpha` with alpha>1/2 would make p^2
dominate this particular entropy cost, while `u^(-1/2)p^3` still tends to
zero. This is compatible with SA's fluctuation smallness after its source
radius is also chosen as required there. It does not make the boundary term
small or produce a fixed source disc for growing p.

CS32 loses the location of the white-coordinate witness: the large free
coordinate could be elsewhere, since K_*^(1/2) has a tail. An all-volume
union has its extensive number of links, and it is not a bound in the
connected support norm needed for SA33. No support-size localization result
for this hard event is asserted. This is the precise remaining second
consumer after the local price has been constructed.

## 7. Returned histories and complex sources

For H's actual returned gas and its source/u/completion domain, the positive
real polynomial includes the empty term. Its logarithm has the H24 full-
collar expansion with rooted bound d_q. Changing only J_R affects clusters
whose full readers meet K_R; thus

    osc_(J_R) log G_ret,F^e<=2|K_R|d_q.                   (CS33)

If K_R is disjoint from the union of complete failure readers A(F), their
nonnegative factors are independent of J_R. The conditional tail bounds
CS21 and CS25 then acquire at most `exp(2|K_R|d_q)`. The same holds in CS29
with the exact real history mass on both sides. Non-invariant insertions
require their exact tree average or a statement at each fixed tree gauge;
for the latter the comparison is uniform before integrating those gauges.
An arbitrary insertion depending on J_R is not an exterior factor. Failure
readers intersecting K_R are outside this extension.

For complex epsilon, set e=Re(epsilon) and require its real coefficients to
satisfy the above coercive interval, as well as H's domain when H is used.
For the original density `|w_epsilon|=w_e`. The H numerator, compensator and
finite returned polynomial obey the corresponding absolute inequalities
at e. Thus CS29 gives a raw complex envelope with the actual positive
Re(epsilon) history integral on its right. It supplies no division by a
complex conditional normalization, no complex nonvanishing, and no bound
relative to the zero-source mass. Any total-volume source change remains
in that reference mass.

The same consumer distinction as CC18 applies. With no extra insertion the
H14 raw history integral is its original numerator. An event on the all-cut
sea that reads an interior subsequently replaced by H8 must itself be placed
inside H8's JOINT replacement integral to represent a pre-return event.
The estimates here apply to the stated all-cut law and do not remove that
replacement obligation.

## 8. Prior work, evidence and remaining construction

STEP55's linear curvature certificate and local charge allocation are
established prior work; its nonlinear chart price retains supplied BCH/BFT
inputs. Its review also preserves the conditional-density/chart distinction
and the all-N mismatch sign qualification. NODEA's Gaussian/convex-core
moment comparisons and fixed-volume Laplace bounds do not establish the
present original-law local denominator. In particular the actual hard cut
is not assumed to be a convex Euclidean set. Sea10 integrates the kernel in
its coarse variable given U, and Sea11–Sea16 use the integrated-V cut
reference. Neither operation is available when V is fixed here.

CB22 supplies the nonabelian good-event chart interface. CC supplies an
original-law cap near arbitrary closed-cut configurations and elementary
shells, but it did not give the local excess-energy tail or the U0 reference
comparison with a paid boundary. The new synthesis is CS12–CS14 with
CS21/CS25–CS29: actual nonlinear charge allocation, every local normalizer,
and an explicit conditional reference. CS32 identifies the remaining
whitening support issue for the other SA complement. It does not claim an
independent rediscovery of the underlying group filling or Haar-cap ideas.

[Bałaban, CMP122, printed355–357](https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf)
starts the large-field return by comparing the dangerous numerator and
denominator Wilson terms; its later connected localization domains and
activity bounds precede exponentiation. Its hard-block transformation,
minimizers, running-coupling assumptions and inductive densities are not
identified with this soft-kernel cut law. No numerical constant or theorem
from that paper is inserted here. [Dimock's large-field exposition](https://arxiv.org/html/1212.5562v2)
separates action penalties, coupling to the small region and sharper
localization after covariance square roots. Its scalar d=3 independent-
fluctuation/analytic-localization hypotheses are not asserted for the present
hard gauge complement. These readings motivate the separate local reference
and connected-support tasks rather than supplying either as an import.

No new numerical experiment was needed or run for this analytic unit.
Mechanical source/hash/link checks are recorded separately and are not
mathematical evidence. The existing CC diagnostics are unchanged and are
not reclassified as checks of CS1–CS33. In particular CC's original 23/24
result, its failed finite-width ratio, its post-hoc probe and its operational
failures remain exactly as frozen. No acceptance criterion was changed.

The next required construction is a connected bad-region organization that
pays CS27's boundary cost under the actual exterior law and preserves its
full reader set, together with a support-size localization of the hard
whitened-cube complement. A Gaussian reference ratio or a global
`exp(constant*u*delta_V^2*volume)` estimate cannot replace those tasks.
Even after those real estimates, complex nonvanishing and the connected
source logarithm of `1+B_comp` remain to be proved. This unit does not supply
arbitrary retained-failure prices, normalized higher-level returns, nonlinear
RG, continuum existence, or the physical continuum mass gap. Those are open
research obligations, not claimed impossibility results.

Process: [PROCESS_LIGHT](PROCESS_LIGHT.md), current-main methodology at
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`, and the coordinator's assigned
file boundary govern. Only this source and checks/cut_sector_coercivity_*
are authored. The [receipt](checks/cut_sector_coercivity_receipt.json) freezes exact inputs and the complete source for a new independent review.
No audit, ledger, axiom or shared-status file is edited.
