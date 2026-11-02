# A fixed source radius for the selected covariant Haar sector

**Author research unit; independent review required.** The result below removes
SA's condition `rho p^2 << 1` for its explicitly selected Haar sector. It keeps
its narrower coarse-curvature window and both exact complementary integrals.
It proves neither a logarithm for the full soft transform nor an interacting
multilevel induction. Continuum existence and the physical mass gap remain open.

The model input is [SA1–SA34](COVARIANT_SOURCE_ACTIVITY_ASTRA.md), SHA-256
`da22fc28cff8f822426ccd0458959dc24668f3d8854848f8ff83dbcda9f2ba54`, now with
an independent [scoped LAND](REVIEW_COVARIANT_SOURCE_ACTIVITY_ASTRA.md). Its
original-coarse-data atoms, actual finite-u critical point, full scalar colour
precision and local analytic phase are consumed unchanged. The predecessor
[CB](COVARIANT_SOFT_BACKGROUND_ASTRA.md) and its reviewed tree/Haar/gauge
conventions remain in force. [H20c/H24](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md)
provides a fixed positive relative-source radius for a different, pointwise
returned gas. Its reference integration is still not supplied by this note.

The new step is a weak quadratic forest expansion on an explicitly deformed
product contour, allowing bounded holomorphic many-coordinate decorations.
The hard-cube normalization and both end segments survive exactly. The forest
identity and all estimates used here are rebuilt locally; the primary sources
in §7 are attribution, not imported Yang–Mills theorems.

## 1. Actual coordinates and the result

Fix d=4, N>=2, odd L>=3, T>=2, u>=1, and kappa in a fixed compact
positive interval. Use SA's fixed internal block trees, free scalar HS coordinates, and normalized
internal tree-gauge volume one; the block-root gauge modes remain. Put `D=N^2-1`, `sigma^2=N/u` and
`d=D(3L^4+1)T^4`. All scalar colour coordinates, crossing links, four ordinary lattice harmonic directions with every colour,
and block-root degrees of freedom remain. There is no extra FP determinant.
The traceless chart has radius less than `min(inj radius,pi/sqrt(N))`.
Let F_epsilon be the EXACT phase in SA2: Wilson times the fixed-real-t,
normalized S4-prime kernel, with Haar log density absorbed once. Only the
original Wilson coefficients vary; `t=kappa u` is not varied with epsilon.

Fix a real admitted coarse V, including compatible non-small holonomies. Let

    b_e=b(V,epsilon), b_0=b(V,0), K_e=F_epsilon''(b_e),
    C_0=K_0^(-1/2), h_e=sigma^(-1) C_0^(-1)(b_e-b_0),
    Q_e=C_0^T K_e C_0=I+E_e.                               (FR1)

Transpose is bilinear analytic transpose. The fixed real selected sector is
`a=b_0+sigma C_0 W`, `W in [-p,p]^d`; it is exactly SA's sector. Translating
`z=W-h_e`, rather than changing this sector with the source, gives

    F_epsilon(b_0+sigma C_0 W)/sigma^2
      =F_epsilon(b_e)/sigma^2 + z^T Q_e z/2 + R_e(z),
    R_e(z)=sigma^(-2)[F_epsilon(b_e+sigma C_0 z)
                         -F_epsilon(b_e)]-z^T Q_e z/2.     (FR2)

There is no linear remainder: b_e is the actual finite-u critical point.
This would be false for a tree-phase critical point in place of b_e.

The conclusion is as follows. Fix a positive output rate mu in fixed R-box
units. There are strictly positive constants rho_*, c_*, h_*, independent of
u,T,p, such that, for `p>=1`,

    |epsilon_p|<=rho_* ,   delta_V<=min(delta_A,c_* sigma p),
    A_R sigma p^3 <= h_*,                                  (FR3)

and the explicit chart and good-event margins in §5, the ACTUAL selected
sector is zero-free on this fixed original-source polydisc. Its logarithm is
constructed in connected original-reader supports. The source-dependent
critical action is factored, with budget `C rho delta_V^2/sigma^2`; it is not
claimed small. The remaining source logarithm has rooted norm

    C rho + C rho exp(-p^2/64) + C sigma p^3.                 (FR4)

The first term is the complete Gaussian determinant. Constants may be very
large, but are fixed before u or volume. In particular `p=sqrt(log u)` is
allowed for all sufficiently large u, with fixed positive rho_*. No assertion
is made for a fixed nonzero curvature delta_V as u tends to infinity.

## 2. A product-contour lemma with all end segments

Here is the scalar estimate needed by the forest expansion. Set
`r=1/16`, `z_p=erf(p/sqrt(2))`. For `|eta|,|t|<=r`, put `h=pt`,

    q_p(eta,t)=(2pi)^(-1/2) integral_(-p-h)^(p-h)
                              exp[-(1+eta)z^2/2] dz.       (FR5)

The straight segment may be replaced EXACTLY, on a holomorphic integrand, by

    Gamma(h)=[-p,p]+[-p-h,-p]+[p,p-h].                      (FR6)

The signs in (FR6) are orientations, not absolute weights. At a side point
`|z-(+/-p)|<=rp`,

    Re[(1+eta)z^2] >= [1-2r-r^2-r(1+r)^2]p^2 >=3p^2/4.

For any entire f, or f holomorphic on `|z|<(1+r')p` with r'>r, the two
contours have the same integral by their common endpoints and Cauchy's theorem.
The same statement holds on a neighbourhood of the closed polydisc; no hard
indicator is analytically transported. On many coordinates it is applied
successively to the full holomorphic top form. Products of the three chains
retain every edge/corner side choice. Translation has Jacobian one.

The following elementary bounds fix a uniform branch:

    |q_p(eta,0)-z_p| <= |eta|/[2(1-|eta|)^(3/2)],
    |q_p(eta,t)-q_p(eta,0)|
                     <=2p|t| exp(-3p^2/8)/sqrt(2pi),
    z_p>=2 exp(-1/2)/sqrt(2pi),
    |q_p/z_p-1|<1/4,       |q_p|>1/4.                      (FR7)

The first inequality integrates the derivative in eta against a real
Gaussian. The second integrates the two oriented side segments in modulus.
Maximizing `p exp(-3p^2/8)` proves the last inequalities for every p>=1.
Thus `log(q_p/z_p)` is the branch zero at eta=t=0. Define the normalized
complex functional nu_i by dividing this scalar contour integral by q_p.
It is not a probability measure; its integral of one is exactly one.

We record a coefficient form of its moment estimate, to avoid using a
pointwise operator bound as a support estimate. Artificial variables eta,t
can be expanded at zero independently of any functions subsequently read
by the integral. Substitute connected atoms for eta_i and t_i. Let a_i be
the sum of their absolute weighted coefficients; assume `a_i<=r/4`. Let
`0<=s_i<=1/64`. There are universal constants C_0,B, for example enlarged
to `C_0=B=2^20`, such that the coefficient majorant of the contour functional,
acting on a holomorphic function bounded by `|z|^k exp(s_i|z|^2/2)`, obeys

    m_i(k,s_i) <= exp[C_0(a_i+s_i)] B^k k!,   k>=0.         (FR8)

At k=0, a_i=s_i=0 the bound is exactly one, not a fixed factor per mode.
The same coefficient estimate with one local atom marked costs at most an
additional `C_0` times its absolute marked weight, and at most two additional
moment legs. This includes marking the q_p denominator.

For clarity, these statements follow by elementary one-variable estimates.
On the real interval the zero-parameter functional is the positive truncated
Gaussian; its quadratic exponential moment is at most `(1-s_i)^(-1/2)`.
On the end segments the absolute integrand is bounded by a constant times
`p exp(-p^2/3)` after a small quadratic weight is inserted. An additional
`exp(|z|/16)` remains integrable, uniformly in p. More explicitly, on the
r-circles and for s_i<=1/64, its normalized absolute integral is at most
32: the real part is bounded by
`2 exp(1/[512(1-r-1/64)])/sqrt(1-r-1/64)`, the sides by
`2rp exp[-3p^2/8+(1+r)^2p^2/128+(1+r)p/16]/sqrt(2pi)`,
and (FR7) supplies the denominator factor at most four. Hence
`|z|^k<=k!16^k exp(|z|/16)` supplies all moments. Cauchy on the eta,t circles of radius r
bounds their nonconstant coefficients by a geometric sum, at most a constant
times a_i when a_i<=r/4. For k=0 this is `1+C a_i+C s_i`, absorbed by the
exponential in (FR8); for k>=1 a fixed prefactor is absorbed in B^k. Marking
one substituted coefficient differentiates one geometric sum; its ratio is
at most `(1-a_i/r)^(-2)`, with the fixed factors 1/r. These bounds are all
well below the deliberately enlarged C_0,B above. This proof works with an
arbitrary holomorphic reader of sup norm one multiplying the displayed
moments, not just with monomials. The nonconstant coefficients of the
functional can be bounded in that reader norm; the constant coefficient at
k=0 is the original probability integral.

Replacing nu_i by the normalized full real Gaussian of precision 1+eta_i
changes this moment bound by at most

    C_0 exp(-p^2/64) B^k k!.                               (FR9)

Indeed the difference is the two real tails and the two end segments, plus
the difference of scalar normalizers. Insert half of their Gaussian decay
before the exponential-moment bound just used. Cauchy at the SAME fixed
eta,t circles retains this factor. For bounded 1<=p<=4, enlarge C_0; for
p>=4 the tail integrals directly give it. In particular
`log q_p + (1/2)log(1+eta)-log z_p` has zero constant coefficient and a
nonconstant coefficient majorant `C_0 a_i exp(-p^2/64)`.

## 3. Gaussian forests with bounded decorations

We give the exact sufficient library statement and proof. The index set I
is any finite collection of scalar coordinates, each assigned to one box of
a finite graph. A reader label is a nonempty connected box set. Matrix atoms
E_ij;S include both endpoint boxes; vector atoms h_i;S include the i box.
They read only the original data in S. Symmetrize the E atoms with their
transposes if necessary. Write, with weight exp(beta|S|),

    M(E)=max{max_i sum_(j,S)|E_ij;S|_beta,
             max_j sum_(i,S)|E_ij;S|_beta},
    B(E)=sup_v sum_(i,j,S:v in S)|E_ij;S|_beta,
    V(h)=max{max_i sum_S |h_i;S|_beta,
             sup_v sum_(i,S:v in S)|h_i;S|_beta},
    delta=M(E)+B(E)+V(h)/p.                                (FR10)

Suprema include the stated original-source product disc and admitted real V.
No product disc of arbitrary coarse link values is assumed. All scalar
colours and every scalar endpoint are counted before these sums.

Let `U=sum_X U_X(z_X)` have connected reader labels X, and be holomorphic
on a neighbourhood of `|z_i|<=(1+r)p`. Its uniform reader norm is

    h_U=sup_v sum_(X:v in X) exp(beta|X|) sup |U_X|.          (FR11)

A reader includes every integrated coordinate used, and every original
coefficient read. Define the EXACT normalized integral

    Z_p(E,U,h)=z_p^(-|I|)(2pi)^(-|I|/2)
       integral_(product Gamma(h_i))
          exp[-z^T(I+E)z/2-U(z)] product_i dz_i.            (FR12)

For beta=mu+8 there are universal constants delta_0,h_0,C>0, independent of
p, graph size and coordinates per box, such that delta<=delta_0 and
h_U<=h_0/2 imply a zero-free integral and connected reader logarithms

    log Z_p(E,0,h)=-1/2 Tr log(I+E)+sum_Y T_(p,Y),
    ||T_p||_mu <= C delta exp(-p^2/64),
    log Z_p(E,U,h)-log Z_p(E,0,h)=sum_Y J_(p,Y),
    ||J_p||_mu <= C h_U.                                   (FR13)

Both expansions are holomorphic in the ORIGINAL sources. `T_p(0,0)=0`
and `J_p(E,0,h)=0` coefficientwise. The weights are support SIZE, not
coordinate diameter. Arbitrarily many modes in a box are allowed only
because (FR10) pays their full incidence sums.

Here is a construction and quantitative smallness recipe. Put
`A=2^20(1+C_0+B)^20` and, if desired, take

    delta_0=h_0=min{r/256,1/(2^20 A)}.                      (FR14)

Any further decrease is harmless. The estimates below give constants bounded
by fixed multiples of A. These intentionally conservative choices are not
being certified by the finite numerical examples.

First split E into its diagonal eta_i and off-diagonal pairs. Factor
`product_i q_p(eta_i,h_i/p)/z_p` and use the normalized functionals nu_i.
Expanding `exp(-U_X)-1` and grouping overlap-connected families gives
bounded decorations a_Y(z), with disjoint core labels Y, exactly as the first
Mayer step of [CX-R](RECOVERY_CLUSTER_ASTRA.md). Its proof is the expansion
of the finite product, grouping each subset into its overlap components.
The rooted-tree recursion for absolute coefficients, with one unit of
support weight for attachments, gives

    sup_v sum_(Y contains v) exp((beta-1)|Y|)||a_Y||<=2h_U.  (FR15)

One can obtain this directly by the recursion `T_X<=|f_X|
exp(sum_(X' intersects X)T_X')` and `|f_X|<=2||U_X||`, since
`h_U` is smaller than 1/16. Each a_Y includes its complete original reader.

Fix a disjoint decoration family. Make one object from ALL coordinates in
its reader Y, with reader a_Y; every remaining scalar coordinate is a
singleton object. Keep all quadratic pairs internal to an object in its
exponent. Between distinct objects A,B put
`u_AB=-sum_(i in A,j in B) E_ij z_i z_j`. Use the following exact forest
identity, with t_F(A,B) the minimum along a forest path, or zero if there is
no path:

    exp(sum_(A<B) u_AB)
      =sum_forests F integral_[0,1]^F product_(AB in F)u_AB
                         exp(sum_(A<B)t_F(A,B)u_AB) dt.    (FR16)

A local proof is short. For a fixed monomial with edge multiplicities n_e,
multiply its coefficient by product_e n_e!. A forest must span each
component of the nonzero-edge graph. Its integral is
`integral product_(e in F)n_e t_e^(n_e-1)
 product_(e notin F)(min_path t)^(n_e) dt`.
Give edge e an independent variable with distribution function x^(n_e).
The integrand is the probability density that F is its unique maximum
spanning forest: every omitted edge has value at most the minimum on its
forest path. These disjoint possibilities exhaust probability one.
This proves every coefficient; finite-dimensional entire convergence gives
(FR16). No positivity of the complex u_AB is used.

Expand a selected forest edge into its actual scalar endpoint pair. Expand
all original-reader atoms, including internal/interpolated quadratic terms
and the scalar functional coefficients. Any product label is connected:
a decoration core is connected, every pair label contains its endpoints,
and every scalar coefficient attaches at its coordinate. Non-tree pair
labels attach inside the same object-tree component. Thus the expansion is
in actual ORIGINAL readers, not in a solved field treated as new local data.

For the bound work at alpha=beta-3. Weight all pair and scalar atoms at
alpha, and write `a_Y^*=exp(alpha|Y|)||a_Y||`. Then (FR15) gives
`sup_v sum_(Y contains v)a_Y^* exp(2|Y|)<=2h_U`. Let e_ij be the
positive pair majorant at this rate and set `s_i=sum_(j!=i)e_ij`. Quadratic stability is elementary:
`sum_(i<j)e_ij |z_i z_j|<=sum_i s_i |z_i|^2/2`.
All forest interpolation coefficients are between zero and one, including
internal pairs. Apply (FR8), with
`epsilon_i=C_0(a_i+s_i)` for the scalar measure-parameter weight a_i. The
crucial counts, for every reader Y, are

    sum_(i in I(Y))(a_i+s_i)<=delta |Y|,
    sum_(i in I(Y),j)e_ij<=delta |Y|.                       (FR17)

Each atom counted on the left contains the box of i, so these follow from
B(E) and the incidence part of V(h)/p. There is NO uniform constant per
unhit scalar coordinate. An object with Gaussian endpoint multiplicities
k_i has moment bound

    a_Y^* exp(sum_(i in I(Y))epsilon_i)
                       product_i B^(k_i) k_i!.            (FR18)

For a bare singleton omit a_Y^*. The diagonal/mean coefficients and their
normalizers have already been included in this bound.

For completeness the summation of the object trees is explicit. A planted
object has one incoming scalar endpoint i. Distribute its children among
coordinates k, say with counts l_k. The multinomial for this distribution
and the labelled-tree child factorial cancel to `product_k 1/l_k!`.
Multiplying (FR18) leaves 1 at an unmarked coordinate and l_i+1 at the
incoming one. Write `x_i=B^2 sum_j e_ij T_j`. The positive planted-tree
iteration is consequently bounded by

    T_i <= exp(epsilon_i)(1-x_i)^(-2)
       [1+sum_(Y: i in I(Y)) a_Y^*
          exp(sum_(k in I(Y), k!=i)epsilon_k)
          product_(k in I(Y),k!=i)(1-x_k)^(-1)].             (FR19)

Distinctness, disjointness and forbidden repeated coordinates are dropped
ONLY in this positive upper bound. With T<=2, (FR17) gives
`sum_(k in I(Y))x_k<=2B^2 delta |Y|`. For x<=1/4,
`-log(1-x)<=2x`. Thus the attachment product costs at most
`exp[(C_0+4B^2)delta |Y|]`, paid by one support-weight unit in (FR15).
The choices (FR14) map the interval 1<=T<=2 into itself; differentiation
of (FR19), using a further unit for `|Y|`, has row sum <1/2. Monotone
iteration therefore sums every planted tree. This also shows why bounding
every mode by a fixed M>1 would have been the wrong estimate: it would
produce M^(number of coordinates in Y), absent from (FR18).

Here are the full support-root marks, including readers remote from their
integration endpoints. A mark is on (i) a decoration Y, (ii) a pair atom,
or (iii) a scalar-functional atom. In case (i), root at that object; its
summed cost is `2h_U` times the same attachment exponential. A tree-pair
mark cuts an edge into two planted trees, costing at most `4B^2 B(E)`.
An internal or interpolated pair mark inserts `|z_i z_j|`, bounded by
`(|z_i|^2+|z_j|^2)/2`; root at the corresponding endpoint. Two extra legs
replace the root series `(1-x)^(-1)` by `2B^2(1-x)^(-3)`. Its endpoint
sum is B(E), not an operator norm or a volume. Case (iii) uses the marked
geometric sum in (FR8) and the incidence part of V(h)/p and B(E). Choosing
a decorated object at the marked coordinate costs the bracket in (FR19).
Column sums are retained for the oppositely rooted edge. Extra markings of
a child reader use the differentiated recursion, of inverse norm at most
2. These three cases bound the rooted majorant of the resulting nontrivial
component polymers, at rate beta-3, by `A(delta+h_U)`. They also cover
marks on the q_p denominator. An isolated undecorated coordinate contributes
one exactly and produces no polymer, since nu_i(1)=1 coefficientwise.

Compatibility in this gas is actual disjointness of OCCUPIED coordinates
and of the decoration cores; it is not disjointness of all external readers.
The latter may overlap without preventing factorization. Every incompatibility
implies intersection of reader labels, so it can be overcounted by reader
intersection in the bound. The repulsive hard-core connected-graph expansion
therefore converges: assigning an auxiliary size |Y| to a polymer, its
incompatible child sum is at most `A(delta+h_U)|Y|<|Y|/4` after one more
support unit. The graph-to-tree inequality here follows by ordering the actual
incompatibility edges and partitioning connected subgraphs by their unique
Kruskal minimum spanning tree. The extra-edge interval has signed sum
`(+/-1)(1-1)^k`, of modulus at most one. The same child recursion, with
auxiliary weight exp(|Y|), therefore bounds the connected graph series.
It gives a connected logarithm of norm at most `2A(delta+h_U)`. The finite gas identity
near zero, followed by analytic continuation in interaction multipliers,
identifies its exponential with (FR12). This proves nonvanishing before
any division. The scalar q_p logs are added with their original-reader
Taylor series; their rooted norm is bounded by a fixed multiple of delta.
All identities extend to countable atom families by their absolute bounds.

To obtain the second estimate of (FR13), multiply U by a scalar lambda.
The construction is uniform for `|lambda|h_U<=h_0`. Cauchy coefficient
extraction on radius `h_0/h_U` gives, coefficientwise in reader labels,

    ||log Z(E,U,h)-log Z(E,0,h)||_mu
       <= C(delta+h_0) h_U/(h_0-h_U) <=4C h_U.              (FR20)

The slack between beta-3 and mu pays all reader marks. This proves a
multi-reader connected estimate, not just an estimate for one insertion.

For the first estimate of (FR13), set U=0 and compare each scalar functional
and its normalizer to the full real Gaussian. Telescope one vertex change
at a time and use (FR9). Every nontrivial Gaussian tree has an E pair; its
changed-vertex count is absorbed by a differentiated planted-tree series.
Thus the connected difference is `C delta exp(-p^2/64)`. The scalar
normalizer difference has the same bound and zero constant coefficient.
The full Gaussian integral equals `det(I+E)^(-1/2)`: diagonalize a real
positive perturbation, then analytically continue on `M(E)<1`; its branch
is one at E=0. The trace series itself has reader bound
`B(E)/[2(1-M(E))]`. Its 1/k cancels the k possible support marks in a
closed walk, with all scalar modes still present. This identifies the first
term in (FR13). The subtraction of log z_p per coordinate in (FR12) is why
the cutoff correction is exactly zero at E=h=0, rather than an omitted
extensive normalization.

## 4. Instantiating the lemma with the actual normalized soft phase

Choose SA's construction at input rate beta=mu+8 (its rate can be any fixed
positive value), then choose its fixed R, analytic radii and small-curvature
constants. There is no choice beta proportional to R^4. SA23 and the full
row/column/marked composition imply finite constants C_E,C_h such that

    M(E_e)+B(E_e)<=C_E rho,
    V(h_e)/p <=C_h rho delta_V/(sigma p).                   (FR21)

For example use `E_e=C_0^T(K_e-K_0)C_0`, the source Cauchy bound on the
localized Hessian, and `h_e=sigma^-1 C_0^-1(b_e-b_0)` with SA23 and
`C_0^-1=K_0 C_0`. Both endpoints and all matrix/force read connectors are
retained in these products. Subtracting the same atom families at zero
source makes E_e,h_e vanish there coefficientwise. This uses the finite-u
spread and Haar terms in K_e; no classical Hessian is substituted. The uncut
complex Gaussian covariance in a coordinates is `sigma^2 K_e^(-1)`, with
`K_e^(-1)=C_0 Q_e^(-1) C_0` and `Q_e^(-1)=sum_(n>=0)(-E_e)^n`.
Its atoms keep both endpoints and all readers. The truncated Gaussian is
not identified with this covariance: its cutoff correction T_p remains.

Choose any fixed c_*>0, reducing it if desired, and set

    rho_* <= min{rho_0/2, delta_0/[2(C_E+C_h c_*)],
                  a_H/(8 n_P)}.                            (FR22)

The last term is H20d's fixed relative-source radius, with a_H its positive
Peierls exponent. It is a domain match, not an invocation of sea integration.
This choice is strictly positive, independent of p,u,T. Equation (FR21)
then supplies the Gaussian hypotheses. Re Q_e is positive since its operator
perturbation is bounded by M(E_e), but nonvanishing of the CUT integral has
been proved by the expansion, not inferred from this fact.

The actual local Taylor remainder in (FR2) is a bounded holomorphic
reader decoration. Subtract the Taylor polynomial through degree two separately from every
bare local vertex. The linear pieces sum to zero by criticality, and the
quadratic pieces sum to the actual Q_e; individual vertices need not be
stationary. Expand the original Wilson, kernel and
Haar vertices at zero before substituting the SA b_e and C_0 atoms. The
three possible reader marks lie at the root vertex, a background factor,
or a fluctuation factor. The same scalar Cauchy majorant as SA17, now with
`|z_i|<=(1+r)p`, gives

    ||R_e||_beta <= A_R sigma p^3,                          (FR23)

uniformly on the original fixed rho_* disc. More explicitly, with SA's f,T_3,d_0,s, put
`t=C_b delta_V`, `x=sigma(1+r)p M_C`, `y=sigma(1+r)p B_C`. The
majorant is
`(1+rho_0) sigma^(-2)d_0 exp(beta s)
[T_3(t,x)+t partial_t T_3(t,x)+y partial_x T_3(t,x)]`.
Thus `A_R=(1+rho_0)(1+r)^3 A_0` is sufficient with SA17's common
M_C,B_C for C_0 and its unchanged background-incidence term.
This is not SA19's quadratic source estimate: the entire source Hessian and
source force have already been put into Q_e and b_e. The local remainder
starts at degree three even at complex epsilon. The sufficient analytic
margin is `C_b delta_V+sigma(1+r)p M_C<a_SA/2`, together with SA's
critical-point radii and the traceless chart condition. The finite-u
single-normalizer theorem is used only at fixed real t; its field-dependent
normalizer and Haar logarithm remain in F_e throughout.

Taking `A_R sigma p^3<=h_0/2`, (FR13) now gives a zero-free integral for the
ACTUAL nonlinear selected sector. Its raw formula, including all constants,
is

    Z_sec(V,epsilon)=h_N^n(2pi sigma^2)^(d/2) det(C_0) z_p^d
        exp[-F_epsilon(b_e)/sigma^2]
        det(Q_e)^(-1/2) exp(sum_Y[T_(p,Y)+J_(p,Y)]),
    n=(3L^4+1)T^4.                                         (FR24)

`det(C_0) det(Q_e)^(-1/2)=det(K_e)^(-1/2)` on the fixed analytic branch,
although the contour was translated with C_0 held fixed. The full colour
trace is used, not a repeated single-colour determinant. h_N is the same
normalized HS Haar constant as SA16. There is no second product of Haar
Jacobians: F_e already contains them once. Its common kernel vacuum
`4T^4 sigma^2 log Ntilde_t(I)` remains in the main action. The internal tree-gauge volume
one, explicit block-root modes and all four harmonic directions and colours have not been changed
by translation.

Consequently the exact source-normalized logarithm is

    log[Z_sec(V,epsilon)/Z_sec(V,0)]
       =-[F_epsilon(b_e)-F_0(b_0)]/sigma^2 -1/2 Tr log Q_e
         +sum_Y{T_(p,Y)(epsilon)+J_(p,Y)(epsilon)-J_(p,Y)(0)}. (FR25)

The critical-action difference has the connected SA budget
`C_main rho delta_V^2/sigma^2`, with `C_main=2 C_act/rho_0`
from SA's source Cauchy estimate. It can be O(rho p^2) on the admitted window;
it is explicitly factored. The determinant has norm O(rho), T_p has norm
`O(rho exp(-p^2/64))`, and the last difference has norm `O(sigma p^3)`.
Every summand is local in its original reader; source normalization makes
the full sum vanish at epsilon=0. This proves (FR4). None of these terms is
relabelled as H24's exponentially small returned-defect activity d_q.

## 5. The hard domain and the remaining return interface

The real sector is unchanged. In SA's notation set

    A_box=sqrt(D)[C_b delta_V+sigma p M_C].

Require strictly `A_box<r_ch`, `delta_V+4A_box<delta_f`, and
`5L A_box<eta`. Choose fixed positive delta_f,eta within Sea9's actual thresholds. Then the
whole fixed real sector lies in the strong all-fine-good/mismatch event G,
and G lies in the original interior-only cut. This remains a proper subset
of G in general. For `p=sqrt(log u)` and
`delta_V<=min(delta_A,c_* sqrt(N/u) p)`, all these margins and (FR3) hold
for sufficiently large u, with the SAME positive rho_*. No coarse data
outside this quantified window receive an estimate here.

Filling every R-box label converts the output rate to
`mu_block=mu/(2R)^4>0`, with the same rooted bound, exactly as in SA. This
is an exp(mu_block |X|) support-size norm in the original level-zero blocks.
Coarsening H24 in the other direction costs at most `(2R)^4 d_q`. One chooses
mu, then R, then this reduced block rate; no arbitrary larger original-block
rate is asserted and no diameter-only estimate is substituted.

For the ORIGINAL conditional soft transform the exact identity remains

    Z_cut=Z_sec
      + integral Haar chi_cut 1_(G minus Omega) w_epsilon
      + integral Haar chi_cut 1_(G^c) w_epsilon.             (FR26)

All fine-defect, mismatch and dirty histories in the last term remain.
No integrated kernel-normalization identity is used at fixed V. A retained
non-invariant history still requires its exact tree average. The full-source
logarithm still requires a connected zero-free bound on `1+B_comp`, where
B_comp is the last two terms divided by the now fixed-radius Z_sec.

The new mixed-decoration theorem accepts bounded HOLomorphic readers on the
complex polydisc. H24's pointwise activities contain hard real completion
indicators. Their pullbacks are not such readers: the exact plaquette
indicator `1_{2|sin(a/2)|<=delta_f}` jumps by one under arbitrarily small
remote shifts at its boundary. Therefore (FR13) cannot be applied to these
histories without a new measure-sensitive boundary/completion estimate.
The contour identity here keeps the selected cube's two ends; it does not
transport those additional indicators. Arbitrary holes, excluded coarse
fields, multilevel actions, continuum existence and the physical gap remain
open. The conditional optical precision gap is not a physical gap.

## 6. Checks and failed routes

[The numerical registration](checks/fixed_source_radius_numeric_plan.md)
preceded the new checker. It completed 46/46 predicates, including fourteen
wrong-formula/omission controls, in 4.654 seconds. Peak RSS was 27,623,424
bytes, every free-memory reading was 54%, every load average was below 2.54,
niceness was at least ten and all five thread counts one. No scientific
predicate or resource gate failed in that run. A [supplemental registration](checks/fixed_source_radius_mixed_plan.md),
written after those results and before its new implementation, targets the
mixed-object step: 8/8 additional exact checks passed in 0.497 seconds.
They enumerate all 84 child distributions through degree six, verify the
parent-endpoint factorial and product generating function, and compare the
three-coordinate coefficient `[lambda E_23^2] log Z` by a direct exponential
series and the decorated-object forest. Treating two objects that share
coordinate 2 as compatible is detected. Across both runs the total is
54/54, with seventeen wrong-formula/omission controls; minimum reported free
memory was 53%, peak RSS 64,765,952 bytes and maximum load 3.415. No
threshold or scientific program was changed after an outcome. The actual
SU(2) conditional fibre uses
the already reviewed 72/1944 transporter fraction and freezes other links
and colours; no new geometry enumeration or full integral is claimed.

The exact rational forest probabilities sum to one for three different
multiplicity triples; replacing the minimum by the maximum or omitting a
tree fails. Complex scalar shifted-segment integrals agree with all oriented
ends, with the critical vacuum and z_p retained. The two-coordinate precision
keeps its complete determinant. Its mixed mean/pair coefficient is a nonzero
boundary term, so deleting the end contours is detected. A bounded quartic
reader's first two coefficients agree by Gaussian moment recurrence and
precision differentiation; the disconnected second-moment substitution is
rejected. The finite-u SU(2) fibre checks stationarity, exact Bessel/Haar
Hessian, scaled mean, source precision and the local critical Taylor
identity at three u values with the same complex source. These checks do
not certify the very small sufficient constants in (FR14) or prove uniformity.

Two analytic shortcuts were rejected before this construction. Integrating
in modulus along the shifted horizontal contour can cost
`exp((Im h)^2/2)` per coordinate; (FR6) avoids that estimate while retaining
its end terms. Bounding the quadratic interaction uniformly on the cube
costs `rho p^2`; the forest moments replace that supremum. The first draft
scope would have left the nonlinear reader interface open. The explicit
object-tree distribution (FR18)–(FR20) supplies that interface for bounded
holomorphic readers. It does not supply the hard-history interface in §5.
An initial source-reader command named a nonexistent `_actual_01.py`; the
correct frozen `_actual.py` was subsequently read. No predecessor file was
changed. All diagnostics and the read ledger are bound by the receipt.

## 7. Primary reading and authority

[Brydges–Kennedy's forest formula, as presented by Abdesselam–Rivasseau,
hep-th/9409094v1](https://arxiv.org/pdf/hep-th/9409094v1), §II pp.3–6,
provides the relevant combinatorial antecedent. Their §V.E pp.31–33 keeps
large-field restrictions and normalized Gaussian interpolation in a two-level
forest. Here (FR16) is proved coefficientwise and (FR17)–(FR20) supply the
actual scalar moment, mode-count and source-reader estimates. No probability
charge for Yang–Mills hard histories is supplied by that paper.

[Dimock, 1212.5562v2](https://arxiv.org/pdf/1212.5562v2), Appendix F pp.91–92,
requires independent variables and bounded local small interactions. The
original quadratic fluctuation source fails that sup-norm hypothesis when
rho is fixed and p grows. The quadratic forest expansion is the additional
step here; the later hard-core connected expansion is rebuilt with its exact
compatibility and reader labels. The d=3 scalar theorem is not a d=4 soft
Yang–Mills theorem. BFKT's source/contour discussion previously read in SA
also retains side and outside-domain terms; it supplies no new premise here.

The pinned versions were freshly checked and matching cached PDFs were read;
full external PDFs/text remain only under /tmp. [The read manifest](checks/fixed_source_radius_read_manifest.json)
records exact coverage, predecessor identities and the scalar diagnostic's
code exposure. [The freeze receipt](checks/fixed_source_radius_receipt.json)
binds this note and evidence for a NEW hostile review. This is an author
construction under PROCESS_LIGHT, not an audit, whole-PR review or
self-assignment of retained grade. No frozen SA/CB/UL, shared status, Git,
lock, reviewer or audit artifact was edited.
