# LOCOP — invariant curvature localization and the coefficient recursion

**The full EXTCONT E19 induction closure remains OPEN.** This note gives
an explicit local projector on the single-field, contractible, real
small-curvature sector; proves its covariance, moment matching and bulk
normalization; and proves a real Taylor benchmark with spatial-variation
variables. It does not identify that benchmark with the interacting
selected return in REALRGA's full norm.

| Requested item | Status at the scope proved here |
|---|---|
| Explicit gauge-compatible Loc | **PROVEN** finite-support tensor projector L5 and its scalar bulk reduction. Its assembly on all actual histories/readers is **OPEN**, LC1 below. |
| Dimension <= 4 and absence of a gluon mass | **PROVEN** for a local single connection with no untransformed exterior spurion. The blanket assertion for mixed fine/coarse activities is false: L3 is an exact counterexample to that assertion, not to gauge covariance. |
| Irrelevance contraction | **PROVEN** ideal real-jet bounds L9–L10, with dimension gain at least one. Actual next-scale H-bounds and the total E19 inequality are **OPEN**, LC2–LC3. |
| Coupling and other coefficient recursions | **PROVEN** exact conditional recursion L13 and AF bracket L15–L16. Uniform actual-model antecedents, causal tuning and other counterterm budgets are **OPEN**, LC4–LC6. |
| Soft-kernel/S4′ gauge breaking | **PROVEN** zero covariance defect for the exact normalized transfer, at every order. Covariance alone does not give local history-uniform derivative estimates. |

PROVEN labels an explicitly scoped statement or implication, not retained
status. No Yang–Mills existence, mass gap or all-route obstruction is
claimed. See [LOCOP_LOG.md](LOCOP_LOG.md) for evidence and fresh review.

Method credit: Bauerschmidt, Brydges and Slade's
[real-norm RG framework](https://arxiv.org/abs/1907.05474v2), and specifically
Brydges and Slade's [local polynomial localization](https://arxiv.org/abs/1403.7253v2).
We use the idea of matching a finite set of tests and reconstructing their
dual local polynomials; their scalar/fermion localization theorem is not
imported into this gauge problem. The construction and bounds used here
are rebuilt below. Credit also Tadeusz Balaban's gauge RG organization and
Jonathan Dimock's [exposition of large fields](https://arxiv.org/abs/1212.5562v2),
whose displayed application is scalar phi-four in d=3. No [m] assertion
is used. External links provide attribution, not premises of a proof.

## 1. Contract, sources and what the word local means

Use REALRGA §§1–4, probability Haar, SU(N), N>=2, odd L>=3, and the actual
normalized Decision-4 kernel. Write anti-Hermitian fields, with

    <A,B> = -tr(AB)/N,   <t_a,t_b> = delta_ab,
    W(U) = sum_p [1-Re tr(U_p)/N],   h_j = sqrt(N/u_j).

W has quadratic form (1/2)sum_p |dA(p)|^2 in these coordinates. Engineering
dimension means [A]=1, [F]=2, [covariant spatial derivative]=1. It is not
ordinary degree in link logarithms, and not a statement that every finite
lattice function is a polynomial.

Loc below acts on **additive action activities** after an exact local
logarithm has been obtained. If K denotes a gas weight, that representation
and its exact re-exponentiation must come first; subtracting a polynomial
from each multiplicative weight does not implement action extraction.

For the explicit construction let X be a finite nonwrapping cubical
container, containing all links read by a C^(6,4) gauge-invariant activity
K_X(U;J). There is just one retained connection in this construction.
All source coefficients J multiply gauge-invariant observables and stay
fixed under gauge transformations. There is no fixed nontransforming
external frame. Functions are defined on an orbit-invariant real domain
containing the trivial field. Require each plaquette used below to have
principal eigenangles of magnitude < pi/N. Its logarithm is then
anti-Hermitian and traceless: the sum of angles is an integer multiple of
2pi with magnitude < pi. The domain is open; use smaller closed evaluation
sets with declared positive margins for bounds.

Choose a nonempty set I_X of interior vertices whose four oriented unit
plaquettes in every coordinate plane lie in X. Use all such vertices,
with weights 1/|I_X|. These choices commute with translations and the full
signed permutation group B_4. A smaller input may first be put in such a
container, but the entire enlargement remains in its support and its cost
must be paid. Wrapping supports, holes, frozen exterior readers and mixed
old fields are not silently brought under this assumption.

REALRGA's derivative sum has field order six and source order four,
including mixed words of total order ten and all original source labels.
Its full rooted norm includes inactive roots and all readers. REALRGB G1
instead has total order four and l1 directions with frozen exterior data;
it cannot supply this contract by inclusion. FR, KR and TC of REALRGA §1
remain the named coordinator inputs for domains, finite-coupling
interaction estimates, and original-law charges/tails. This lane does
not redo or upgrade their results.

## 2. Exact covariance, and two different meanings of a mass term

### L1. The normalized kernel has zero gauge defect — PROVEN

For a link b=(x,y), U_b^g=g_x U_b g_y^-1. Each S4′ contour T_y^sigma
starts at c_X and ends at c_Y. Multiplication cancels every interior g,
including reversed links, so

    T_y^sigma(U^g)=g_(c_X) T_y^sigma(U) g_(c_Y)^-1,
    M_c(U^g)=g_(c_X) M_c(U) g_(c_Y)^-1.               (L1)

The second identity holds for the arithmetic average, without taking a
polar part or choosing a logarithm. Paired axial orders are preserved.
An axis permutation relabels sigma; a block-preserving reflection
relabels the offsets and oriented contours, reversing a coarse link when
required. Averaging all orders and offsets therefore preserves B_4 and
coarse translations. Translations that move the chosen blocking origin
are not symmetries of a fixed block partition.

For t=kappa u and h_M(V)=Re tr(V* M)/N, let
Z_t(M)=int exp(t h_M(W))dW and k_t=exp(t h_M(V))/Z_t(M).
For a,b in SU(N), h_(aMb^-1)(aVb^-1)=h_M(V). The substitution W=aW'b^-1
in probability Haar proves Z_t(aMb^-1)=Z_t(M). Thus

    k_t(V^(g|roots); M(U^g))=k_t(V; M(U)).            (L2)

The normalizer is strictly positive on real fields and has the same exact
covariance. If rho(U) is gauge invariant, a fine gauge extending any
specified root gauge, followed by Haar substitution, proves that
int rho(U) K(V,U)dU is gauge invariant as a function of V. The same holds
for a selected density only when its complete selector is invariant, or
covariant together with every reader/history label. A chart-dependent
selector with omitted complementary terms is not covered.

Differentiating the exact identities wherever the derivatives exist gives
zero defect at every order. No low-order cancellation test is being used
as a substitute for this identity. This proves exclusion of breaking by
the prescribed kernel, not regularity across a moving sector boundary.

### L2. The single-field local Ward test excludes a mass — PROVEN

Constant gauge transformations fix U=1. The differential DK_X(1) is an
invariant linear functional on each copy of su(N), hence zero: invariance
implies it vanishes on commutators, and matrix commutators span su(N).
Differentiating local gauge invariance once more at 1 gives

    H_X(d omega,A)=0,   H_X=D^2 K_X(1),              (Ward)

for every vertex function omega and link field A on the box. A term
(m^2/2)sum_b |A_b|^2 alone fails this identity for every m^2 != 0.

There is also a constructive local curvature factorization. Fix a
spanning tree in the box and set lambda(v) equal to the line sum of A
along the tree path to v. Then A-d lambda vanishes on tree edges. On a
nontree edge its value is the circulation around its fundamental loop.
Fill that loop by a finite integer sum of unit plaquettes inside the
box: commuting adjacent coordinate steps changes a word by a plaquette;
after commuting and canceling inverse steps a closed box word is empty.
This supplies an explicit linear map R with A-d lambda=R dA. Consequently

    H_X(A,B)=H_X(R dA,R dB)=:h_X(dA,dB).

The map R is finite, but its norm can grow with the box; no uniform bound
is inferred. For the nonlinear dimension statement, fix the tree links
to 1 by a gauge transformation. The remaining links are fundamental loop
holonomies, all based at the tree root. K becomes a smooth function of
these matrices invariant under simultaneous conjugation; its linear
Taylor functional at the identity vanishes by the same commutator test.
For a smooth connection sampled at spacing epsilon, a finite closed-loop
product is 1+epsilon^2 times its oriented-area contraction with F at the
root, plus O(epsilon^3). This follows by expanding the finite link product:
the constant-connection linear terms cancel on a closed path; the next
terms are its first spatial differences and pair commutators. Commuting
adjacent steps groups them into the elementary plaquette curvature.
Thus the first possible nonconstant scalar has two curvatures and
engineering dimension four. Its coefficient is precisely the quadratic
constant-curvature test in §3. There is no invariant linear curvature
(dimension two), nor a connection mass. This is finite-patch power
counting, not a uniform estimate on arbitrary rough lattice fields.
The same argument applies to an exponentially summable bulk Hessian:
its analytic symbol satisfies Pi(p)d(p)=0, which implies Pi(0)=0 by
taking p=t v, dividing by t and letting t go to zero for each v.
A transverse nonanalytic mass projector would evade that last step and
is outside the stated locality class.

### L3. Retained relative fields and chart Jacobians — PROVEN diagnostics

The preceding theorem is about a single connection. The actual soft
joint function has two fields. Set fine U=1, so M=1, and V=exp(z t_a).
Exactly,

    -log k_t(exp(z t_a);1)
       = const + t[1-Re tr exp(z t_a)/N]
       = const + (t/2)z^2 + O(z^4).                 (L3)

Thus joint covariance permits a nonzero quadratic term in a relative
fine/coarse connection. At the normalized tree level it is
(kappa u/2)|Q A-B|^2; Qd=d ev makes the linearized residual gauge
invariant. At finite coupling additional fine-only normalizer terms must
be retained; L3 itself is exact at fixed fine identity. This is not a
gauge-breaking gluon mass in the final single-field action. It shows why
gauge symmetry cannot delete all quadratic mixed-field counterterms in
REALRGA's retained fine/coarse state.

Similarly the local chart U=exp(A)Ubar has
log j(A)=(N/12)tr A^2+O(|A|^4), as SF §3.2 records. To check the
coefficient without an import, the derivative of exp gives
j=det[(1-exp(-ad A))/(ad A)]; log of the bracket is
-ad A/2+(ad A)^2/24+O((ad A)^4). Its linear trace is zero, and on
traceless matrices tr_ad((ad A)^2)=2N tr A^2, by writing ad A as
A tensor 1 minus 1 tensor A^T. This gives the coefficient above.
For SU(2), A=i z sigma_3 gives j=(sin z/z)^2 and log j=-z^2/3+O(z^4).
The contribution -log j to the chart action is positive quadratic.
It is a coordinate-measure contribution, not independently a physical
mass counterterm. A background-covariant fluctuation transforms by
conjugation, so its norm square is allowed. Retain Haar, FP, reference,
action and normalization contributions together when using Ward identities.

## 3. A specified projector, including the tensor sector

### L4. Constant-curvature tests and colour structure — PROVEN

Let a index the six unoriented planes and D=N^2-1. For a constant
su(N)-valued antisymmetric tensor F define the affine link field

    A_mu^F(x)=(1/2)sum_nu (x_nu-o_nu) F_(nu,mu),
    U_b(t,F)=exp(t A_b^F),   dA^F=F.

Only finite-box derivatives at t=0 are used; no nonperiodic constant
magnetic field is imposed on a torus. Set A^(a,c)=A^F for F_a=t_c and
all other components zero, and

    C_X,ab(J)=(1/D)sum_(c=1)^D
                   H_X(J)[A^(a,c), A^(b,c)],
    b_X(J)=tr_plane C_X(J)/6,   a_X(J)=K_X(1;J).     (L4)

The Hessian's colour blocks are multiples of <.,.>. Here is the needed
algebra. Represent an invariant bilinear form by a map T using this
nondegenerate inner product. Invariance says T commutes with all ad H.
After complexification, commuting with diagonal matrices makes each
root line C E_ij an eigenspace. The identities
T[X,Y]=[X,TY]=[TX,Y], applied to E_ij,E_jk and E_ij,E_ji, equate their
eigenvalues and determine T on the traceless diagonal subspace.
All root lines are connected by these relations (for N=2 the single
pair and its diagonal already suffice). Thus T is scalar; reality makes
its scalar real. Hessian symmetry makes C_X symmetric. Hence

    (1/2)H_X(A^F,A^F)
                    =(1/2)sum_(a,b) C_X,ab <F_a,F_b>.

Changing o changes A^F by a constant link field, which is an exact
gradient on the box, so Ward makes L4 independent of o. A geometric
symmetry maps these affine potentials to the transformed ones, up to
such a gradient. Thus C_X transforms as a tensor on two-forms; its trace
is invariant. All source derivatives through four commute with these
finite linear tests, at fixed kernels and u.

### L5. Reconstruction, covariance and idempotence — PROVEN

Write P_(x;s mu,t nu) for the oriented elementary loop starting at x,
then moving s mu, t nu, -s mu, -t nu, where s,t are +/-1. Define the
clover field, extended antisymmetrically in its indices, by

    Fcal_(mu,nu)(x)=(1/4)sum_(s,t=+/-1)
                                      s t log U(P_(x;s mu,t nu)),
    W_X^cl(U)=(1/(2|I_X|))sum_(x in I_X,a) |Fcal_a(x)|^2.

Every loop is based at x. Thus Fcal transforms by Ad(g_x), with no
unrecorded parallel transport. Signed permutations act on it as on a
two-form, exactly. The plaquette domain of §1 makes every logarithm
single-valued and covariant. These are local **polynomials in the declared
lattice field strength**, not global polynomial functions of link logs.

Define

    Loc_X^ten K = a_X
        +(1/(2|I_X|))sum_(x in I_X,a,b) C_X,ab <Fcal_a(x),Fcal_b(x)>,
    Loc_X^sc K = a_X + b_X W_X^cl.                    (L5)

For the affine test U(t,F), Fcal=tF+O(t^2); in a single commuting colour
direction this is exactly tF near zero. Therefore applying L4 to either
reconstruction recovers its coefficient tensor, and its value at 1 is
a_X. Both maps are linear idempotents on the fixed-container space.
They commute with lattice symmetries as maps between the corresponding
containers. On their gauge-invariant domain the input and output are
invariant under arbitrary local gauge transformations; this is the
precise gauge-commutation statement. The formula does not purport to
commute on arbitrary gauge-variant chart pieces.

In the gauge-invariant sector, Loc^ten matches **all** constant-curvature
quadratic tests. For a B_4-invariant bulk translation family, reflection
in an axis contained in one of two distinct planes but not the other
kills each off-diagonal coefficient. Axis permutations make the six
diagonals equal. Thus the aggregate C is b times the identity. This
also excludes the orientation-odd tr(F dual F) term. Apart from the
vacuum, the dimension-four bulk polynomial is exactly tr F^2. The
tensor form must precede this symmetry reduction for a nonsymmetric
individual activity, a source insertion or a selected history.

An explicit warning is useful: take C=diag(1,-1,0,0,0,0) in L5. This is
a local gauge-invariant curvature polynomial with Loc^sc K=0. Under
ideal constant-curvature dilation L^4 K(L^-2 F) it is unchanged. Thus
scalar extraction alone cannot contract every gauge-invariant activity.
Its B_4 orbit average vanishes; that cancellation is usable only in a
representation retaining the complete orbit, not at fixed exterior data.

### L6. Agreement with FLOW, and the scheme conversion — PROVEN / OPEN

For a translation family choose one density representative per translation
orbit and sum its translates with that convention. The uniform weights
on I_X sum to one, so L5 contributes b_X W^cl per site; the total bulk
coefficient is b=sum_X b_X. Assume absolute summability of the Hessian
moments through order two and of these tests, as required in FLOW §3.
The finite curvature factorization in L2 gives
Pi(p)=d(p)^* h(p)d(p). Its degree-two momentum term is determined by
the constant-curvature quadratic test. After B_4 symmetrization that
term is b(|p|^2 delta_(mu,nu)-p_mu p_nu). With FLOW's link-coordinate
Fourier convention the 12 component has derivative -b at zero, while
direct differentiation of sum_z exp(i p.z)Pi_12(z) gives
-sum_z z_1 z_2 Pi_12(z). Therefore

    beta[K_bulk]=sum_z z_1 z_2 Pi_12(z)=b.            (L6)

Finite supports prove this directly; absolute moment summation justifies
the infinite sum and differentiation. Boundary and wrapping terms are
not redefined as a torus-dependent coupling. W^cl and the Wilson W
both have b=1. In a convention using unnormalized -tr F^2, a coefficient
c_bar has b=2N c_bar, as in FLOW F-id.

FLOW evolves the normalized-kernel **tree functional** W_(j+1)^tree,
with beta[W^tree]=1, not necessarily W^cl or the bare Wilson sum.
One may compute b by L4 and transfer b W^cl to b W^tree by the exact
identity b W^cl=b W^tree+b(W^cl-W^tree). The last term has beta zero,
but its real remainder norm and contraction still require LC2. For
N>=3 use the SU(N) maximizer tree exponent kappa u phi_M, as corrected
in FLOW §3.1. The U(N) polar deficit cancels in the normalized kernel;
its degree-six difference cannot be omitted from a C^6 contract.

### L7. Finite real coefficient estimate — PROVEN

Let H_X^T=sup_D T^(6,4)(K_X), in the coordinate version with a single
field species weighted by h. Put
A_X=max_(a,c,b) ||A_b^(a,c)||op; it is finite and at most
(sqrt(N)/2) times the coordinate radius of X about o. The field-order-two
term of T has divisor 2!, so for every included source derivative,

    sum_(r=0)^4 |D_J^r b_X|/r!
                      <= 2 A_X^2 h^-2 H_X^T.        (L7)

Use the same weighted source directions on both sides. The labelled
version has the identical bound. Each tensor entry obeys this bound
too, by the mixed bilinear test. This is an actual finite C^2 estimate,
not a value-to-derivative or Cauchy estimate. Domain and chart conversion
constants, summed supports, and conversions from group derivatives remain
explicit when changing norms. In particular h_j^-2=u_j/N: an O(1/u_j)
weighted activity bound alone gives only an O(1) coefficient estimate.
Obtaining an O(1/u_j) coefficient error requires the corresponding
unweighted Hessian bound, or a sufficiently stronger weighted estimate.

## 4. Real irrelevance: the spatial part cannot be skipped

### L8. Why constant matching needs spatial regularity — PROVEN

In the finite Hessian factorization, write a quadratic curvature term
as (1/2)sum_(p,q) h_pq <F(p),F(q)>. Subtract its constant test at an
owner o. Each difference is the sum of terms

    <F(p)-F(o),F(q)> + <F(o),F(q)-F(o)>.

Along a nearest-neighbour path of length r, telescoping bounds
|F(p)-F(o)| by r sup |nabla F|. Thus its engineering degree is at least
five when a spatial derivative has dimension one. For nonabelian fields
the comparisons require specified transports, with their reader sets
and derivatives; this elementary linear estimate does not supply those
uniform bounds. Arbitrary lattice fields have no small spatial difference
just because their amplitude is small. This explains the extra input
needed beyond beta[(1-Loc)K]=0.

### L9. A full Taylor-sum bound with variation variables — PROVEN

The following is an independent finite-dimensional real lemma. Let f
denote curvature variables (dimension two), z spatial-variation variables
(dimension three), and J the untouched sources. On convex product unit
balls use exactly sum_(a+b<=6,c<=4) |D_f^a D_z^b D_J^c G|/(a! b! c!),
with the supremum outside the sum. All statements also hold for labelled
sources. Suppose identically in J

    G(0,J)=0,  D_(f,z)G(0,J)=0,  D_f^2 G(0,J)=0.

This is the ideal remainder of the complete tensor marginal projection,
with no invariant linear curvature/variation terms. For
D_L G=L^4 G(L^-2 f,L^-3 z,J),

    ||D_L G||_T <= (4 L^-1+8 L^-2)||G||_T.           (L9)

Proof. Split G=P_2 G+R using ordinary field Taylor degree two. The
only surviving terms in P_2 G are fz and zz. Their dilation factors
are L^-1 and L^-2. Reconstruction of a degree-two Taylor coefficient
costs at most sum_(r=0)^2 binom(2,r)=4 in this full norm, so
||D_L P_2 G||_T<=4L^-1 T_(0,J)(G), followed by the domain supremum.

For R, the jets through degree two vanish, and all its derivatives of
degree >=3 equal those of G. Put S=diag(L^-2,L^-3); its two component
contractions are at most s=L^-2. Apply radial Taylor's integral formula
to the derivatives of R at S(f,z). At orders r=0,1,2 it costs respectively
binom(3,r)L^4 s^3; summing gives 7L^-2 sup_T(G). The binomial identity
follows by distributing the radial derivatives over the two species:
sum_(a+b=r) binom(i,a)binom(j,b)=binom(3,r), i+j=3.
All orders 3 through 6 are evaluated at the same S(f,z); their factors
L^4 s^r are <=L^-2, so their entire sum costs only L^-2 sup_T(G).
No factor ||(1-P_2)G|| is needed. This proves L9 without a seventh
field or fifth source derivative, and with the prescribed supremum order.

This is O(L^-1), with an explicit constant; its displayed factor is <1
for odd L>=7. It is >1 at L=3 and L=5 and certifies no contraction at
those values. If there are no z variables and all degree <=2 field jets
vanish, the polynomial part is absent and the same proof gives

    ||D_L G||_T <= 8 L^-2 ||G||_T,                  (L10)

which is <1 already at L=3, reproducing EXTCONT E5. Neither claim
assigns dimension three to actual retained old fields by declaration.

### L10. What the actual return must prove — OPEN

An actual construction must transport (1-Loc)K to this kind of curvature
and variation representation with bounded real derivatives and original
source labels, and control its nonlinear remainder. A sufficient comparison
on the *same full rooted norm* is

    ||B_j^irr|| <= C_tr(4 L^-1+8 L^-2),
    ||D_K R_j(0)-B_j^irr|| <= d_*,
    lambda_q <= D_q[C_tr(4 L^-1+8 L^-2)+d_*].        (L11)

Use L10's 8L^-2 only if its stronger zero-jet hypothesis is actually met.
D_K is a derivative with respect to an inserted activity, not a field
derivative. D_q includes any separately charged selected-return, support,
hole and weight costs exactly once. No volume factor L^4 is added again.
Even these inequalities do not suffice without

    theta_q=lambda_q+B_q s_*q+eta_*q+C_q M_q < 1,
    B_q e_*q <= (1-theta_q) M_q,                     (L12)

and a quadratic nonlinear bound C_q||K||^2. These are precisely the
remaining EXTCONT E19 requirements. Constants, support reserve mu+2 and
coefficient budgets must be regenerated at each step. No estimate in
LINEAR_PACKAGE's linear action contraction, REALRGB's fixed-sector G1,
or BFT_B's one-step lift-pinned decomposition supplies L11 for all histories.
BFT_B §2.4 proves covariant pieces under its pinned-branch hypotheses;
its general-depth extension is explicitly withdrawn. BFT_A §§7.1,8.0
retains composite gauge directions and relative residuals; it does not
remove L3's mixed terms.

## 5. Coefficient recursion and asymptotic-freedom bounds

### L11. Exact action extraction and signs — PROVEN conditional algebra

Assume a complete positive output with an exact local action
S'_(j,h)=u_j W_(j+1)^tree+F_(j,h), including all prefactors and additive
complements before the logarithm, and a translation-invariant bulk at
J=0 admitting L6. Decompose F_bulk=Gamma_j+R_j^other, where Gamma is
the complete one-loop contribution. Define

    b_j=-beta[Gamma_j],   r_j=beta[R_j^other],
    u_(j+1)=u_j-b_j+r_j=u_j-b_j-rho_j,
    rho_j=-r_j,
    G_(j,h)=F_(j,h)-(u_(j+1)-u_j)W_(j+1)^tree.       (L13)

This is exact by linearity. The coupling comes from the source-free bulk,
independently of h and the torus. All anisotropic, boundary, source and
wrapping differences remain explicit. In FLOW's RLF convention the
returned marginal term is -delta beta_j, so it contributes +delta beta_j
to rho_j. One must include higher fluctuations, inherited terms, Haar,
FP, normalizers and references exactly once in Gamma or R^other.
The local counterterm functions are C'_(j,h)=Loc G_(j,h), with tensor
L5 where applicable and additional mixed/boundary components where required;
K'=G-C' is an exact split, not yet a bound.

For standard Hermitian generators tr(T^a T^b)=delta_ab/2,
s(exp(i a^2 F^a T^a))=a^4 sum_a(F^a)^2/(4N)+higher powers of a.
Summing unoriented planes gives u/(8N) times the ordered plane sum.
Matching 1/(4g_std^2) yields

    u=2N/g_std^2,
    beta_0'=2N (2b_0)=11N^2/(12pi^2),
    b_0=11N/(48pi^2) in FLOW's standard convention.   (L14)

This proves the conversion of FLOW's stated coefficient. It does not
derive universality for the present kernel. FLOW's older g_lattice obeys
g_lattice^2=1/u; it is not g_std. Forward coarse graining lowers u when
b_j+rho_j is positive.

### L12. Keep FP-exact and T-tel before estimating — PROVEN identities

At an admissible critical Gaussian background let Gamma map gauge
parameters injectively into the field space, Delta'=Gamma*Gamma,
Q Gamma=0 with Q positive on the orthogonal gauge quotient S, and let
chi=(h,chi_2), chi Gamma invertible, h onto. Put H=ker h and
O=Q+chi_2*chi_2. The orbit-coordinate change A=s+Gamma omega has Jacobian
det(Delta')^(1/2). Changing orbit variables to chi A, integrating the
h delta function and the chi_2 Gaussian, and comparing with coarea for
hA=0 gives

    Delta_FP=|det(chi Gamma)| det(hh*)^-1/2,
    (1/2)log det_H O-log Delta_FP
             =(1/2)log det_S Q-(1/2)log det Delta'.  (FP)

The powers of 2pi cancel because dim H=dim S+dim(range chi_2).
This rebuilds the finite algebra in FLOW §52. A field-independent
replacement for Delta_FP would change the coefficient. This is a linear
Gaussian quotient identity with the displayed criticality, positivity
and admissibility conditions, not a global nonlinear gauge-fixing theorem.

For T-tel use FLOW §94(W3)'s common determinant subspaces and invertibility
hypotheses, with the specified zero modes removed. In this paragraph
log det means log|det|, reducing to the ordinary logarithm on positive
Gaussian sectors; no continuation across a zero eigenvalue is asserted.
The covariant linearization satisfies T_k D_k=D_(k+1)ev.
With P_k the projector perpendicular to Ran D_k,
P_(k+1)T_k=P_(k+1)T_k P_k. The transverse covariance recursion is closed.
For an orthonormal frame V of the longitudinal subspace, the block Schur
determinant identity gives
det(V*Y^-1 V)=det_perp(PYP)/det Y. It cancels the longitudinal log det Y
term in the complete critical Gaussian expression. Write Ytilde_k=P_kY_kP_k
on the transverse subspace, Phi_k^T=log det Ytilde_(k+1)-log det Ytilde_k,
and G_(gh,n)=(1/2)log det(D_n*D_n)-(1/2)log det Delta_U in those quotient
conventions. Starting with the inverse transverse Hessian at level zero,
telescoping the transverse log determinants gives FLOW §96's expression

    total_n=(1/2)sum_(k<n) Phi_k^T+G_(gh,n).         (T-tel)

There is no omitted level remainder. These facts fix what enters Gamma;
they do not estimate its marginal coefficient uniformly. FLOW §§105–107
also requires the exact phase-weighted Cartan derivative and projection
at the current U. The naive contour average and projection frozen at 1
are not substitutes. Its C-part estimates cover orders <=2 and assume
Pi-loc; the M-part and the full C^(6,4) return remain outside that scope.

### L13. Uniform flow bracket, with its exact antecedents — PROVEN

Let b_*=beta_0' log L>0. Suppose, uniformly in the desired cutoff and
volume family,

    B_n=sum_(j<n) b_j,   |B_n-n b_*|<=R_0,
    |rho_j|<=C/u_j,   u_j>=u_min>0,
    C/u_min <= b_*/2.

The first is a separate one-loop partial-sum theorem; neither T-tel nor
FP-exact proves it. Set b_-=b_*-C/u_min and b_+=b_*+C/u_min. Telescoping
L13 and subtracting the two bounded defects proves for every j<n

    b_-(n-j)-2R_0 <= u_j-u_n
                           <= b_+(n-j)+2R_0.        (L15)

In particular |u_(j+1)-u_j|<=b_*+2R_0+C/u_min, uniformly in depth.
This does not assert that u_j itself is bounded in the ultraviolet or
that every step decreases u; the additive defect can permit early
nonmonotone steps. If U=u_n-2R_0>0, the lower bracket gives
u_k>=U+b_-(n-k). Since the reciprocal is decreasing, comparison with
its integral over [0,n-j] yields the sharper bound

    |u_j-u_n-(n-j)b_*|
        <=2R_0+(C/b_-) log(1+b_-(n-j)/U).            (L16)

The constants are uniform; the allowed deviation grows logarithmically
with the number of UV steps. This is arithmetic on an admitted trajectory,
not existence or tuning of that trajectory. Existence additionally needs
FLOW's causal finite-step continuity and small-bare-coupling limit, with
all steps in the same stable class. FI-1 requires estimates at step j to
use only the chain's own flow through j, not a future terminal coupling.

L7 explains the extra actual-model task: prove the summed unweighted
Hessian error |beta[R_j^other]|<=C/u_j on this trajectory. The numerical
value of a weighted activity norm is not that estimate. When changing
field weights, h_j/h_(j+1)=sqrt(u_(j+1)/u_j) and the inverse conversion
must both be accounted for in the actual map; a per-step bounded ratio
does not license an unbounded product of conversion losses.

### L14. Other coefficients and source functions — PROVEN conditional form

The exact recursion is projection of the complete output, not just L13.
If an explicitly specified nonvacuum coefficient vector/function v has
v'=A_j v+f_j+r_j(K), then

    ||A_j|| V_*+||f_j||+sup_(||K||<=M_q)||r_j(K)||<=V_*

is a sufficient invariant-ball condition. The norms include every
original-source derivative and all tensor/mixed/boundary labels retained
by the representation. This inequality is an additional estimate. A
vacuum density e_j per level-j site obeys e_(j+1)=L^4 e_j+a_j when all
new vacuum terms are assigned to a_j; it needs an additive growth budget,
not the irrelevant-activity contraction. Source-dependent vacuum terms
are functions and stay in H6. No finite-dimensional homogeneous bulk
classification by itself closes these coefficient recursions.

## 6. Exact remaining sublemmas and disposition

| Name | Required statement and current status |
|---|---|
| LC1 — actual representation | **OPEN.** On an explicitly stable all-history real domain, obtain the complete additive action activities with invariant pieces or covariant reader-labelled families. Classify and retain mixed-field, source, boundary and holonomy terms. Apply L5 only to its single-field sector. Prove exact regrouping and complementary-sector bookkeeping. |
| LC2 — spatial localization | **OPEN.** Give bounded nonabelian curvature/transport coordinates or an equivalent real moment estimate on complete supports, with six field/four source jets and actual link weights. Bound the tensor-zero spatial quadratic remainder, nonlinear higher terms and W^cl-W^tree. Establish the coordinate/scaling dictionary for L9 rather than inferring it from beta=0. |
| LC3 — extracted return | **OPEN.** Prove L11 after SEL/HOLE costs in EXTCONT, a quadratic activity remainder, regenerated support reserve, and the numerical inequalities L12. L9 is only an ideal benchmark. A window contraction in the same norm is an alternative requiring its own proof. |
| LC4 — bulk flow coefficient | **OPEN.** Supply a volume-independent bulk Hessian moment limit and |B_n-n beta_0' log L|<=R_0, plus the real summed higher-order/returned bound C/u_j. FLOW §110 retains L-loc2 and Pi-loc as ARGUED, T-a1-M, T-a3, T-b and T-c as OPEN, and the rate/causality items. Its exact identities do not discharge them. |
| LC5 — actual AF trajectory | **OPEN.** Establish the stable positive-coupling trajectory, continuity/tuning inputs and causal FI-1 with constants fixed before induction. Conditional bracket L15 cannot assume its own input estimates. |
| LC6 — remaining coefficients | **OPEN.** Prove the explicit projected recursion bounds for all nonbulk and source coefficients and vacuum/source prefactors, compatible with H0–H6 and the same extraction. Their allowed counterterms include L3 in mixed coordinates. |

The proposal to assemble the tensor projector, its bulk reduction and
covariant spatial Taylor estimates into LC1–LC3 is **ARGUED**. The finite
projector itself and the ideal lemmas are **PROVEN**. The actual all-history
operator is **OPEN**, so this note does not mark EXTCONT's EXT, COEFF or
E19 closed. Exact gauge covariance excludes a symmetry-breaking physical
gluon mass at the final local single-field level; it neither deletes
mixed residual terms nor supplies a decay estimate.

The highest-value next test is a complete selected spatial-quadratic
return: retain its tensor coefficients, normalizer, all original readers
and differentiated selector, perform FP/T-tel cancellations where their
hypotheses apply, and bound its constant-test-zero remainder in RGA7.
This directly tests LC2–LC3. The finite regressions in
[checks/locop_criteria.md](checks/locop_criteria.md) only check algebra and
normalization. Their outcomes and the fresh same-family hostile review
are recorded in the log.
