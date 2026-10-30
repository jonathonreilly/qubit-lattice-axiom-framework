# MIXGFF — mixtures, logarithmic composites, and a geometric witness

**Recommendation — ARGUED:** add the degree-one/two spatial Cesaro cluster
condition **CL2** below to COMBO's existing `W = AF-e AND K4 != 0`.
**PROVEN conditional separation:** this excludes every admissible probability
mixture of invariant elementary GFF states and finite canonical Wick-composite
states, without a uniform spectral envelope. It needs one additional family
of infrared estimates on the existing two- and four-point functions, not a
mass gap. The actual YM estimates are **OPEN**.

**PROVEN additional separation:** a two-geometry ratio excludes the class Q
of scalar quadratic Wick polynomials whose underlying GFFs share one scalar
covariance kernel, however nonhomogeneous its positive spectral measure.
Together with CL2 and W it excludes finite mixtures of Q with the preceding
classes. **PROVEN counterexample:** logarithmic GFF composites can cluster
and reproduce every collinear free-YM leading cumulant. **OPEN:** exclusion
of all Wick composites of arbitrary scalar/tensor GFFs. Neither logarithms,
clustering, nor the present Q theorem establishes that broader conclusion.

PROVEN means the printed mathematical implication or construction, not actual
YM realization, independent audit, or retained status. This research note uses
[PROCESS_LIGHT](PROCESS_LIGHT.md); its execution/review record is
[MIXGFF_LOG](MIXGFF_LOG.md). Balaban and Dimock are credited for the surrounding
constructive YM program. No result of theirs is silently imported here.

## 1. Fixed objects and comparator classes

Use [COMBO §1](COMBO.md) without changing its field or normalization:

    E_n = ^0 S(R^(4n)),       A_e = direct_sum_(n>=0) E_n,
    e_a(x) = (4a^4)^(-1) sum_(mu != nu) sum_(p in clover_mu,nu(x))
                                      [1 - Re tr(U_p)/N],
    ehat_a = e_a - E e_a,     Z(a) = 1,     N >= 2.

Every jet of an E_n test vanishes at every pair coincidence. Only admitted
separated products are used; `e(f)^4` with repeated overlapping supports is
not added. Reflection, translations, reality and scalar Euclidean covariance
are the same throughout. Cumulants are the finite partition polynomials in
separated moments, with component means retained until deterministic centring.

The **common reconstruction input ALG** is S0=1, E1/E2/E3, reality and the
single all-order estimate

    |S_n(F)| <= alpha (n!)^beta ||F||_(s n),1,
    ||F||_(k),1 = max_(|gamma|<=k) sup_X
                            (1+|X|^2)^(k/2) |partial^gamma F(X)|.    (1)

Here one finite s,alpha,beta works for all n, exactly as in
[REC_CONT §1](REC_CONT.md). REC_CONT/REC_LIB continuation, ordered matching
and uniqueness are named local mathematical inputs, not reproved in this
lane. Each actual YM use remains conditional on their hypotheses. In
particular the ordered Euclidean kernels are analytic away from collisions.
Their point values mean limits of separated compact bumps in this hierarchy.
No product of coincident distributions or additional OS reconstruction is
introduced. All conclusions concern equivalence preserving the named e field,
vacuum and spacetime action; they do not classify unmarked ambient free nets.

Retain COMBO's lambda_m=L^(-m), odd L>=3, fixed disjoint bumps f1,...,f4,
f1=theta f4, and its fixed-scale cumulant K4. In particular

    V_m = lambda_m^8 S_2^T(f_(1,lambda_m), f_(4,lambda_m)),
    AF-e: V_m -> 0 and lambda_m^(-eta) V_m -> infinity for every eta>0.
    W: AF-e AND one fixed separated K4 != 0.                        (2)

Definitions used below:

| Class | Exact meaning |
|---|---|
| G | Invariant affine Gaussian hierarchy on the scalar e generators, with an admissible positive tempered spectral covariance; permitted invariant Gaussian zero modes are not discarded by definition. Elementary GFF assignments are included. |
| F1 | WITNESS's finite canonical free-field Wick-polynomial scalar assignments, with finitely many derivatives, masses and species. Its precise propagator class is retained. |
| Q | `e=c+:psi^T A psi:`, A a finite real symmetric matrix, and `<psi_a(x)psi_b(y)>=delta_ab H(x-y)` after a constant change of basis. H is one admissible scalar GFF covariance, smooth and strictly positive off the diagonal. Each hierarchy satisfies ALG. A nonzero constant positive species matrix can be absorbed into A; null directions can be removed. No derivatives, linear admixture or position-dependent coefficients are included. |
| WGF | All admitted finite Wick composites of arbitrary GFFs, including unequal scalar spectra, tensors, derivatives and mixed degrees. This is the larger target; Q is a proper restricted subclass. |

An **admissible barycenter** `S=integral S_t dnu(t)` means a probability
mixture of individually invariant, normalized component hierarchies on these
same tests, each with its own OS construction; moment evaluations are
measurable and integrable and agree with the displayed integral. In particular
`integral S_t(Theta P P)dnu < infinity` for the positive-time P below. S itself
has ALG. A finite mixture with finite moments satisfies these integrability
requirements automatically. No decomposition into non-invariant states is
covered: arbitrary mixtures of such states are a different, much broader
notion than mixtures of vacuum GFFs.

## 2. Candidate (a): cumulant signs, ratios and their limits

### 2.1 Gaussian-mixture identities — PROVEN

Let the component means be a common deterministic mu and write C_t,ij for
their connected two-point values at four distinct tests. Expanding the three
Gaussian pairings and then subtracting the mixture's disconnected terms gives

    K4_mix(1,2,3,4) = sum_(ij|kl = 12|34,13|24,14|23)
                                      Cov_nu(C_t,ij, C_t,kl).       (3)

These are covariances of numbers indexed by components. They need not have
one sign for four different tests. For a common-covariance scale mixture
`e=sqrt(V) q`, V>=0 independent of a centred GFF q,

    Cij = E[V] Qij,
    K4 = Var(V) (Q12 Q34 + Q13 Q24 + Q14 Q23).                       (4)

At one *abstract* Gaussian coordinate, the further formulas are
`kappa4=3 Var(V)`, `kappa6=15 kappa3(V)` when Var(q)=1, and
`E[X^(2k)]/(2k-1)!!=E[V^k]`. Their Hankel moment matrices are positive:
`sum a_i a_j E[V^(i+j)] = E[(sum a_i V^i)^2]>=0`.
These familiar variance-mixture tests do not become repeated-e moment tests
on A_e. They are stated to identify the domain restriction, not used to
adjoin a coincident product. Formula (3), in contrast, is on A_e.

**Counterexample to a single positive ratio separator.** For any v>0 let
V take 0 and 1+v with probabilities v/(1+v) and 1/(1+v). Then E[V]=1 and
Var(V)=v. Thus at any tuple with all Qij>0, (4) attains any prescribed
positive `K4/C23^2` while leaving its two-point function fixed. This includes
the positive free-YM ratio in CUMUL. This is a deliberately calibrated
counterexample to that discriminator, not a prediction or a simultaneous
match to every YM correlation. Taking q with positive density
`s^2/log^2(e+s) ds` makes it obey AF-e, as in COMBO §3; its separated
covariance behaves as `r^-8/log^2(1/r)`. Positive finite mixtures preserve ALG.

Varying means defeats a negative-sign test as well. If e=q+T, with independent
T=+1 or -1 equally and unit-integral tests, then `Cij=Qij+1` and `K4=-2`.
The deterministic subtraction of the total mean does not remove T. The
additional term in V_m is lambda_m^8 and hence preserves AF-e. These are
actual invariant affine GFF mixtures on this hierarchy, not just four random
numbers. Their construction/growth is the atomic positive-spectral construction
of §3 below with density s^2/log^2(e+s); its Gaussian pairings have the same
power bound 4n. This rebuilds COMBO's relevant example.

**YM obligation:** an inequality involving genuinely separated moment data
that every chosen mixture class satisfies, plus a strict opposite YM margin
on one continuum sequence. Neither the single positive free-YM K4 nor the
same-coordinate Hankel inequalities establish it. Matching several geometries
can test restricted scale mixtures, but (4) is not an identity for arbitrary
covariance mixtures or mixtures with varying means.

### 2.2 A working geometric ratio for Q — PROVEN

Let h_ij=H(x_i-x_j), a2=tr(A^2)>0 and a4=tr(A^4). Wick contraction at
distinct points gives

    Cij = 2 a2 h_ij^2,
    K4 = 16 a4 [h12 h23 h34 h41 + h12 h24 h43 h31
                                      + h13 h32 h24 h41].           (5)

Proof of the coefficient: in a connected contraction each quadratic vertex
has two legs and degree two; the graph is a cycle. Each undirected four-cycle
has 2^4 labelled pairings. The species contraction is tr(A^4). For n=2
there are two pairings and the trace is tr(A^2). This also follows separately
by completing the square for a finite Gaussian vector and expanding
`-(1/2) tr log(I-2 C W)`; no infinite determinant is needed.

For a configuration Z of four distinct points with positive Cij define

    D(C;Z) = sum_(c=1234,1243,1324) sqrt(product_(ij in c) Cij),
    R(S;Z) = K4(Z)/D(C;Z).                                         (6)

Since H>0, substitution in (5) proves the exact identity

    R(S;Z) = 4 tr(A^4)/(tr(A^2))^2,       every Z, every scale.       (7)

This has no hypothesis of exact scaling or absence of logarithms. It includes
the COMBO product of two independent logarithmic GFFs. Null A cannot satisfy
AF-e and is excluded from division. Deterministic shifts and nonzero constant
rescalings of e leave (6) unchanged. The square root is applied to positive
point-kernel numbers, not to distributions or separately smeared propagators.

Here is an explicit nonzero free-YM prediction for the difference of (6).
Let d=N^2-1, `q_u=u^-1 sum_(a,I) :F_I^a F_I^a:` with six unordered two-form
indices I. Differentiating `delta_mu,nu/(4 pi^2 |z|^2)` gives

    G(z) = J(z)/(pi^2 |z|^4),
    J(z) = Lambda^2 [I - 2 z z^T/|z|^2],
    Cij^q = 12d/(pi^4 u^2 |z_ij|^8),
    K4^q = 16d/(pi^8 u^4) sum_c tr(product_(ij in c) J(z_ij))
                                              product_(ij in c)|z_ij|^-4.
                                                                    (8)

For completeness the derivative used here is
`partial_mu partial_rho (1/(4pi^2 |z|^2))
= -delta_mu,rho/(2pi^2 |z|^4)+2 z_mu z_rho/(pi^2 |z|^6)`.
Antisymmetrizing its four terms in the curvature indices gives the
two-by-two minors defining J; the quartic z terms cancel. J is orthogonal,
so tr(J^2)=6. The cycle proof above with common colour gives (8), including
the factor 16. Thus the normalization is rebuilt, as in CUMUL §3.

Take planar configurations, with all other coordinates zero,

    A: (0,0), (1,0), (2,0), (3,0),
    B: (0,0), (1,0), (0,1), (2,1).                                (9)

Rotate B so time is `(3x+4y)/5`, then translate time by 1. Its ordered
time coordinates are 1,8/5,9/5,3. Rotate/translate A to ordered positive
times too. This puts all point limits inside the same ordered Euclidean
domain. Rotations and translations do not change any following value.

On A all J's are the same reflection on two-forms; every cycle trace is 6.
For B, a product of the four planar reflections is a planar rotation R_phi
and identity on the other two coordinates. Its exterior-square trace is
`2+4 cos(phi)`: there are the two area forms and two copies of R_phi.
Direct multiplication using

    H_x=diag(-1,1), H_y=diag(1,-1),
    H_(1,1)=[[0,-1],[-1,0]], H_(1,-1)=[[0,1],[1,0]],
    H_(2,1)=[[-3/5,-4/5],[-4/5,3/5]]

gives the following rational table.

| Cycle | cos(phi) | tr(product J) | product r_ij^-4 |
|---|---:|---:|---:|
| 1234 | 4/5 | 26/5 | 1/1600 |
| 1243 | 0 | 2 | 1/64 |
| 1324 | 3/5 | 22/5 | 1/400 |

The weights sum to 3/160 and their trace-weighted sum is 91/2000; the
weighted average is 182/75. Consequently

    R(q;A) = 2/(3d),       R(q;B) = 182/(675d),
    R(q;A)-R(q;B) = 268/(675d) > 0.                              (10)

Every Q state instead has difference zero by (7). This is a **PROVEN
separation at the free-leading/conditional-YM scope**. It does not assert
that a free Maxwell field is outside all free theories: Q is scalar,
derivative-free and has a shared kernel, whereas (8) has a tensor numerator.

**Same-algebra formulation.** For each fixed lambda and each point in (9),
take a normalized smooth bump of radius epsilon lambda; for sufficiently
small epsilon their time supports are disjoint. First take the common
continuum limit of all moments, then epsilon->0. ALG's ordered analytic
kernel supplies the point values in (6). This is a functional determined by
A_e, invariant under its field-preserving OS equivalence. It is not generally
the ratio of a finite list of fixed-width smeared moments. Replacing the
product of h_ij in (5) by a product of their separately smeared integrals
would be wrong. No unchanged finite-coordinate N5 contract is claimed.

**New YM obligation GEO:** on both configurations and compact collision-free
ordered neighborhoods, for one running u_m and one continuum hierarchy,

    lambda_m^8 u_m^2 C(lambda_m z_i,lambda_m z_j)
                         -> 12d/(pi^4 |z_i-z_j|^8),
    lambda_m^16 u_m^4 K4(lambda_m Z)
                         -> (16d/pi^8) sum_c tr(product J) product |z_ij|^-4.
                                                                    (11)

Uniform convergence on those neighborhoods is a sufficient formulation.
Every denominator has a positive leading value. Division therefore gives
(10) in the limit, and a nonzero difference at some fixed sufficiently small
lambda. It is enough to prove directly, at one fixed scale, that the sum of
the two ratio errors is less than `134/(675d)`. The running normalization
cancels but its common identification must still be proved. CUMUL's existing
one collinear smeared tuple does not supply (11); this requires new
two-/four-source matching and extension bounds for noncollinear data on the
original law. It uses no new observable, source axiom or reconstruction.

## 3. Candidate (b): logarithms and the composite counterexample

### 3.1 Exact homogeneity is a restricted class — PROVEN

For finitely many exactly homogeneous GFF kernels and their finite
derivatives, a finite Wick polynomial has a finite sum of homogeneous terms
in its separated scalar two-point function. If nonzero, it has leading
`c r^-gamma`, c>0, with a real exponent gamma. Positivity of c follows by
testing reflected points. If gamma>=8, V_m cannot tend to zero. If gamma<8,
choose `0<eta<8-gamma`; then lambda_m^-eta V_m tends to zero, violating AF-e.
A null kernel violates the lower clause. Thus AF-e excludes that restricted
class. The analogous finite canonical massive class has nonnegative powers
of log r as well; the E-CAN argument recalled in §4.3 covers it.

Arbitrary GFFs need not be homogeneous. The statement in the brief that
their composites have exact dimensions with no logarithms is false for that
larger class. The following construction also answers the clustering escape.

### 3.2 A logarithmic clustering composite — PROVEN

Use mass squared s and define, at r>0,

    G_s(r) = (16pi^2)^-1 integral_0^infinity
                         t^-2 exp(-r^2/(4t)-s t) dt,
    H(r) = integral_1^infinity G_s(r) ds/log(e+s),
    e_*(x) = 2 sum_(a=1)^p :psi_a(x) chi_a(x):,  p=3d,             (12)

where all 2p GFFs are independent with covariance H. The cutoff s>=1 is
part of this comparator; it changes no YM input. It makes clustering
particularly transparent. The fixed field factor 2 is not scale dependent.
The common spectral density is positive and polynomially bounded. The choices
p=3d and factor 2 construct a counterexample with a specified trace spectrum;
they are not derived YM parameters or fitted predictions.

The heat integral gives

    0 < H(r) <= integral_0^infinity G_s(r)ds = 1/(pi^2 r^4).

Let ell_lambda=log(lambda^-2). Scaling s=σ/lambda^2 in (12) yields

    ell_lambda lambda^4 H(lambda r) -> 1/(pi^2 r^4)              (13)

uniformly for r in compact subsets of (0,infinity). Here is the limiting
argument, rather than a regular-variation citation. In the scaled integral
σ>=lambda^2. On `[lambda^2,lambda]`, the integrand is bounded by
ell_lambda G_0(r), so that part is O(lambda ell_lambda). On σ>=lambda,
`ell_lambda/log(e+σ/lambda^2)<=2`; for every fixed σ>0 this ratio tends to 1.
The integrable dominating function is `2G_σ(r_min)` on a compact radial
interval. The same bound on the supremum of the error proves uniformity.
Finally integrating the heat kernel over σ gives the displayed constant.

For p=1, independent contraction gives `C_* =4H^2` and
`K4_*=32 sum_c product_(ij in c) H_ij>0`. For p independent copies,
both cumulants multiply by p. Consequently (13) proves AF-e and K4>0
for the COMBO nonnegative separated tests, with the precise inverse-square
logarithm of its proposed YM behavior. More generally density
`log(e+s)^(-alpha)` produces the inverse log power 2alpha in the composite
two-point function for every alpha>0, by the same split with bound 2^alpha.
An anomalous log exponent alone therefore does not distinguish WGF.

**Clustering.** Since the density is at most one and supported on s>=1,

    H(r) <= (16pi^2)^-1 integral_0^infinity
                               t^-3 exp(-r^2/(4t)-t)dt
         <= 4 exp(-r/2)/(pi^2 r^4).                           (14)

For the last inequality use `r^2/(8t)+t/2 >= r/2`, then drop the remaining
factor exp(-t/2) and integrate t^-3 exp(-r^2/(8t)). In a Wick expansion of
two compact separated polynomial blocks translated far apart, terms with
no cross-block edge give exactly the product of expectations. Every other
term contains an H edge tending to zero by (14); there are finitely many
terms at each order and intrablock separations are fixed. Dominated
integration over these supports proves ordinary clustering, and in
particular CL2 below. This supplies a counterexample to `W AND clustering`
as an exclusion of arbitrary GFF composites.

**All collinear leading cumulants match.** Regard e_* as a quadratic form
with p blocks `A=[[0,1],[1,0]]`. Its even trace powers are 2p=6d and its
odd trace powers vanish. At collinear distinct points the Maxwell J is the
same involution with three +1 and three -1 eigenvalues, so
`d tr(J^n)=6d` for even n and zero for odd n. For each n>=3, connected
pairings are the undirected n-cycles, with coefficient `2^n tr(A^n)`;
for n=2 use `2 tr(A^2)`. Equation (13) therefore gives exactly the
free-Maxwell leading connected kernels at every fixed collinear n-tuple,
with u=ell_lambda in (8). Partitioning into connected blocks gives the
same statement for moments. This is a leading-kernel statement, not an
equality at finite lambda or at arbitrary fixed-width noncollinear bumps.
It shows why merely adding more collinear leading cumulant ratios is
insufficient. The B geometry in (10) distinguishes this example.

### 3.3 Admissibility on A_e, including reconstruction — PROVEN

The ultraviolet spectral integral at coincidence is not used as a Euclidean
random-field product. Approximate H by finite positive atomic sums: truncate
[1,infinity) at L, partition into intervals of mesh 1/L, use each right
endpoint s_j and weight `integral_(I_j) ds/log(e+s)`. Since G_s decreases
in s, `0<=H_L(r)<=H(r)`, and H_L(r)->H(r) for r>0 by compact-interval
Riemann convergence and the integrable tail. Each H_L is a finite sum of
canonical scalar covariances. Apply (12) with independent species at this
finite level.

Every n-point Wick term has n edges and at most two legs at each insertion;
at most `(2n-1)!! <= 2^n n!` labelled pairings occur, with an additional
fixed constant to the n from species and coefficients. Set S0=1 and S1=0
separately. For n>=2, with
`delta=min_(i<j)|x_i-x_j|`, uniformly in L,

    |S_n,L(X)| <= C^n n! min(delta,1)^(-4n).                   (15)

A flat test has all jets zero at a nearest pair-coincidence plane. Taylor's
formula to order 4n along the displacement of that pair gives, for small
delta,

    |F(X)| <= C0^n delta^(4n)/(4n)! ||F||_(9n),1
                                            (1+|X|^2)^(-5n/2).

The displacement has norm O(delta), so the weight changes only by a constant
to the n. For delta bounded below use the weighted zeroth derivative.
The remaining weight is bounded by
`product_i (1+|x_i|^2)^(-5/2)`, whose integral is a fixed constant to the n.
Together with (15) this proves

    |S_n,L(F)| <= D^n n! ||F||_(9n),1
              <= exp(D) (n!)^2 ||F||_(9n),1,               (16)

and an integrable dominating function for passage to the limit on every E_n.

For each scalar atom reflection positivity follows explicitly from

    integral d^3k/[(2pi)^3 2sqrt(k^2+s)]
         |integral_(t>0) exp(-t sqrt(k^2+s)) fhat(t,k)dt|^2 >=0.

Gaussian Wick forms are symmetric tensor Gram forms of this positive
one-particle form. The composite forms are restrictions to their polynomial
vectors. Each admitted OS form is a finite sum of separated moments; its
limit remains nonnegative. Euclidean invariance, reality, permutation
symmetry and S0=1 pass to the limit too. Bound (16) gives ALG, so the same
REC_CONT/REC_LIB interface applies. No OS4 assumption was needed to make
the construction; clustering was separately proved in (14).

One can retain psi, chi and e_* jointly: every mixed insertion has at most
two legs and the same bounds apply, with a larger D. Splitting the unlike
species in each product by a small positive-time displacement creates no
self-contraction. On compact strictly ordered supports all other and all
reflected cross contractions stay separated. Their limits show that the
split vectors are Cauchy in the OS norm and converge to the composite
vectors. Repeating for each insertion and using the common continuity bound
identifies the e_*-cyclic space as a subspace of the joint Gaussian space.
Thus (12) has an actual GFF-composite realization, not just a proposed
two-point function with a chosen fourth moment.

**YM obligation for a better OPE route — OPEN:** derive an observable
relation involving multi-geometry/OPE coefficients that cannot occur for
the specified entire comparator class, and prove that relation for the
same e hierarchy. A beta-function formula for a renormalized operator must
also identify that operator with this fixed Z(a)=1 e, including mixing,
contacts and normalization. No such identification or arbitrary-WGF
classification is supplied by the existence of logarithms.

## 4. Candidate (c): a minimal cluster test for mixtures

### 4.1 CL2 on the existing algebra

Let P range over a countable dense determining family of complex compact
positive-time tests containing either one e insertion or two insertions
with strictly ordered disjoint time supports. Include their finite rational
complex linear combinations within each degree, keeping the family countable.
Write Theta P for the reflected conjugate
word, tau_a for spatial translation by a in R^3, and

    B_R=[-R,R]^3,
    CL2: lim_(R->infinity) (1/|B_R|) integral_(B_R)
                   S(Theta P tau_a P) da = |S(P)|^2.       (17)

All products in (17) are admitted separated two- or four-point tests:
reflection places the first word at negative time and the second at positive
time for every a, and intraword time gaps remain positive. No same-time
or repeated coincident product is taken. Integrating a over a finite cube
is also an admitted smooth compact test: derivatives act on the original
smooth P, while a lies in a finite set. Time supports stay separated.

Ordinary clustering for these words implies (17): the integrand is bounded
by the OS norm and an average of a bounded function tending to its limit
has the same limit. No decay rate is required. CL2 does **not** assert full
extremality for arbitrary non-Gaussian states. Its determining degree is
chosen because a Gaussian hierarchy is fixed by its first two moments.

### 4.2 Variance lemma for invariant mixtures — PROVEN

For any admissible barycenter and any P in (17), let v_t=[P]_t in the
component OS Hilbert space, Omega_t its vacuum, and U_t(a) its spatial
translation unitary. These unitaries follow from covariance of the OS form;
strong continuity follows first on test vectors and then by density. Put
`M_R,t=|B_R|^-1 integral_(B_R) U_t(a)da`.

Here is the needed mean-ergodic argument. M_R,t is a contraction and is
identity on invariant vectors. On a vector `(I-U_t(b))w` its norm is at most
`|B_R symmetric_difference (B_R+b)|/|B_R| * ||w||`, which tends to zero.
The orthogonal complement of the closed span of these differences consists
exactly of vectors invariant under every U_t(b). Thus contraction and density
give strong convergence to the orthogonal projection E_t onto that subspace.
Omega_t belongs to it. Consequently

    lim_R average_(B_R) S_t(Theta P tau_a P)
        = ||E_t v_t||^2 >= |<Omega_t,v_t>|^2 = |S_t(P)|^2.

The integrable domination `|<v_t,U_t(a)v_t>|<=||v_t||^2` allows the same
limit inside the barycenter. Subtracting |S(P)|^2 gives the exact identity

    lim_R average S(Theta P tau_a P) - |S(P)|^2
      = integral ||E_t v_t - S_t(P) Omega_t||^2 dnu
                                + integral |S_t(P)-S(P)|^2 dnu.     (18)

The two terms are nonnegative. CL2 therefore implies S_t(P)=S(P) almost
surely. Intersect the full-measure sets for the countable determining family;
individual test-space continuity extends this equality to all its degree-one
and degree-two ordered compact tests. Euclidean invariance extends it to
all separated pairs: each unequal pair has a neighborhood that can be
rotated to strict time order and translated to positive times; use a
partition of unity. Means are fixed by translation invariance. Thus every
component has the same first moment and connected two-point function as S.

This argument does not assume the components already cluster and does not
silently remove a zero mode. Distinct labels representing the same component
state are harmless. For components in G, the equal first two moments fix
all separated Wick moments, so S itself is Gaussian. A nonzero K4 is then
impossible. Hence

    ALG + CL2 + K4 != 0 excludes every admissible barycenter of G.   (19)

### 4.3 Addition of the canonical and quadratic classes — PROVEN

For clarity, the free-side F1 ingredient is the precise E-CAN statement
in [WITNESS §2](WITNESS.md): a nonnull scalar finite canonical Wick
polynomial has leading separated covariance
`c r^-gamma |log r|^j`, c>0, gamma integer, j a nonnegative integer.
Its proof uses the heat kernel in (12): for positive mass set
`G=Y(mr)/(4pi^2 r^2)`, whence `z^2Y''-zY'-z^2Y=0`. The coefficients of
`Y=a0+sum_(n>=1)(a_n+b_n log z) z^(2n)` satisfy

    b1=a0/2,
    4n(n-1)b_n=b_(n-1),
    4n(n-1)a_n+(4n-2)b_n=a_(n-1) (n>=2).

They converge on punctured compact intervals; derivatives and finitely many
Wick products preserve integer powers bounded below and bounded log degree.
Scalar covariance makes the surviving leading term radial; RP fixes its
positive sign. A null series gives a null separated kernel. After the fixed
positive reflected smearing, gamma>=8 violates the upper AF clause, while
gamma<=7 gives `lambda_m^(-1/2) V_m ->0`, violating its lower clause.
This is the same repaired finite-propagator class as WITNESS, not an
assumption about arbitrary spectral measures.

Now let components belong to F1 union G. By (18) all component covariances
equal S's. If S satisfies AF-e, any F1 component on that full-measure set
would itself satisfy AF-e, contradicting the preceding proof. Thus F1 has
zero weight. The remaining Gaussian components have identical means and
covariances, hence identical hierarchies, and K4=0. We have proved

    W + ALG + CL2 excludes all admissible barycenters of F1 union G. (20)

No common ENV bound on component ultraviolet asymptotics was used. Equality
of their covariances, supplied by CL2, replaces such an envelope. The actual
YM condition remains unproved; (20) does not itself establish existence.

There is a further finite-mixture extension if GEO is available. In a finite
mixture of F1 union G union Q, CL2 again fixes every component mean and C;
AF eliminates F1. Gaussian components have K4=0. Every Q component satisfies
`K4_t(Z)=r_t D(C;Z)` with r_t independent of Z by (7). Since the component
means and C are common, taking the fourth cumulant commutes with this finite
mixture: all disconnected subtractions are the same. Therefore

    R(S;Z) = sum_t p_t r_t,     with r_t=0 on G,

is independent of Z. Any nonzero difference between A and B contradicts
that identity. Thus W+ALG+CL2+GEO excludes every such finite mixture. This
extension is stated for finite mixtures only; no interchange of arbitrary
point-limit derivatives with an unbounded mixing measure is implicit.

### 4.4 Exact new YM cost and strength — OPEN on YM

For every P in the determining family, the minimal extra input is (17)
for the same limiting hierarchy already used in COMBO. A sufficient
original-law producer is convergence of the finite-R, spatially integrated
separated moments on one sequence j, together with

    limsup_(j->infinity) | average_(B_R)
          [S_j(Theta P tau_a P) - |S_j(P)|^2] da | <= delta_P(R),
    delta_P(R) -> 0.                                           (21)

The continuum limit j->infinity is taken at fixed R, then R->infinity.
Local uniform bounds or convergence for the integrated test supply the
first passage. A finite torus plateau or a diagonal limit R=R(j) is not a
substitute. Degree two P requires a separated four-point block-cluster
estimate; clustering of e's two-point function alone misses variance
mixtures with common mean. Source centring must be consistent in all terms.

This is weaker than requesting a quantitative physical mass gap: it needs no
exponential rate and no positive spectral threshold. For example the canonical
massless scalar GFF has `G0(r)=1/(4pi^2 r^2)` and no mass gap; the finite Wick
expansion just used proves CL2 from its decaying cross-block propagators.
The implication from a particular proposed YM gap theorem would still need
its proper cluster/reconstruction hypotheses. We do not use that implication.
Likewise (12) clusters while remaining a composite: CL2 is not a general
interaction test. A full extremality theorem would eliminate nontrivial
invariant mixtures but still would not eliminate a single clustering WGF.

## 5. Recommendation and obligation comparison

| Candidate | Exact disposition | Additional YM obligation beyond COMBO |
|---|---|---|
| Sign or one positive K4/C23^2 | **PROVEN counterexamples** (4) and random shifts; same-test positivity is not a separated four-test theorem. | A new admissible inequality with a strict violated margin; current leading sign supplies none. |
| AF logarithms versus WGF | **PROVEN counterexample** (12)–(16), including clustering and all collinear leading cumulants. Finite exactly homogeneous composites are excluded. | A class-wide multi-geometry/OPE obstruction and matched actual-e data, not just the beta function. |
| CL2 plus nonzero K4 | **PROVEN conditional exclusion** of all admissible invariant Gaussian barycenters. | Spatial averaged two-/four-point block clustering (21), on the same hierarchy. |
| W plus CL2 | **PROVEN conditional exclusion** (20), including arbitrary admissible mixtures of F1 and G. | The same single CL2 family; no mass gap or extra UV coefficient. |
| Two-geometry ratio | **PROVEN conditional exclusion** of Q for any common scalar spectral kernel. | GEO (11), or a strict ratio gap at one fixed scale; noncollinear two-/four-source control. |
| W plus CL2 plus GEO | **PROVEN conditional exclusion** of finite mixtures of F1, G and Q. | Both CL2 and GEO; neither is supplied here by the coordinator's local bounds. |
| Every WGF and its mixtures | **OPEN**. These rows do not prove a universal composite classifier. | New invariant or classification covering unequal spectra, tensors, derivatives and mixed degrees, plus its YM matching. |

The smallest supported upgrade is (20): reuse ALG, the one-sequence moment
limits, AF and nonzero K4 already required by COMBO; add CL2. This reaches
all admissible invariant probability mixtures of its previous literal union,
even without the old uniform envelope. This is an obligation-count comparison,
not a claim that proving infrared clustering is easy or cheaper than GEO in
practice. No proof of minimality among all possible witnesses is asserted.

If the target must also remove the explicit logarithmic composite, pursue
GEO: it tests the Maxwell tensor geometry in already familiar second/fourth
source derivatives and excludes a genuine arbitrary-spectral Q subclass.
Pair it with CL2 for the finite-mixture enlargement. WGF in its full generality
stays OPEN. The strongest conclusion with no new YM estimate is the existing
COMBO theorem; none of this note's conditional strengthening can be credited
to YM before its new estimates are proved.

ALG, common sequence, trajectory and original-law accounting are shared once.
GEO implies a nonzero K4 at small scale (the leading B and A coefficients
are positive), so that particular K4 obligation need not be proved twice.
GEO alone does not give AF without suitable growth of u_m. Neither GEO nor
CL2 is claimed to follow from the other. Fixed source radius, finite-coupling
kernel remainder and original-law coercivity/tails remain named coordinator
inputs, not substitutes for either global estimate. All witnesses are
properties of the same e hierarchy; no flow-time or sharp-time algebra is
substituted, and no finite-coordinate N5 equivalence is claimed.

## 6. No-Go Discipline Gate — scoped boundaries, no universal no-go

This is a **partial narrowing with live routes**, not a claim that exclusion
of WGF is impossible. The explicit no-commit/no-ledger assignment controls
delivery; no committed audit packet or packet PASS is claimed.

**N1 — distinct routes actually considered (ATTEMPTED).**

| Route | Mechanism and result |
|---|---|
| Scalar moment cone | Variance-mixture Hankel/sign identities; restricted by the separated domain and defeated by (4) at a positive single ratio. Higher valid separated inequalities remain live. |
| Spectral ultraviolet growth | Positive KL weights with inverse logs; (12) refutes the proposed no-log property of arbitrary GFF composites. |
| Spatial invariant sector | Cesaro projection detects variance of component one-/two-point expectations; (18) proves mixture separation. It succeeds, not a failed route counted as closed. |
| Tensor four-point geometry | Exterior-square traces differ between (9); (10) separates Q. Extension to the entire WGF class is unproved. |
| Higher collinear connected functions | All cycle traces match in (12); increasing collinear leading order alone does not remove that example. Noncollinear higher data remain live. |

These are different objects/invariants, not five proofs that every route
fails. Prior research packets are not retained-authority substitutes; the
proofs here carry the scoped counterexamples. The global no-go submission
condition is not met, because multiple routes remain open.

**N2 — dependency relations.** ALG/one-sequence existence is the common
interface, not a separate interaction witness. On that interface compare
three additional conditions W, CL2 and GEO. W does not imply CL2: the
nontrivial scale mixture (4) has a positive invariant variance plateau.
CL2 does not imply W: a centred canonical massless GFF clusters and has K4=0.
GEO implies nonzero K4 but its printed limit without a growth condition on
u_m does not assert AF-e; the reverse W=>GEO is refuted by (12).
CL2=>GEO is refuted by (12). GEO=>CL2 is unresolved here. No count of
independent walls is asserted. Common reconstruction and producer accounting
are not counted repeatedly, and K4 is collapsed when supplied by GEO.

**N3 — hidden-premise scan.** The load-bearing qualifications are explicitly
ALG, invariant component states, integrable barycenters, first/two-moment
determining tests, positive point kernels for division, finite Q species and
one common scalar H, original-law matching, and the stated order of limits.
"Canonical" refers only to F1's finite-propagator definition; it is not a
claim that arbitrary GFFs have its asymptotics. Pointwise formulas are used
only through ordered analytic kernels and separated bump limits. Literature
and review verdicts provide no hidden closure.

**N4 — residual matching.** COMBO §3's mixture examples attack W alone;
§2.1 rebuilds exactly that residual. COMBO §4's product example attacks
WGF exclusion by W; (12) adds clustering and collinear data, not an assertion
that COMBO already proved those stronger facts. CUMUL §3's K3=0 and K4>0
concern free curvature and remain free coefficients; no YM matching result
is attributed to them. WITNESS §2's finite-propagator hypothesis is used
only for F1, not Q or WGF.

**N5 — resolution audit.** Exact statements concern separated continuum
hierarchies and explicitly identified invariant mixture components. No
per-site, per-block, modewise, or full-lattice YM estimate is claimed.
The prospective finite-matrix checker covers the free two-form numerator
and finite cumulant algebra only; its numerical execution is currently
blocked. The logarithmic limits, OS growth and Cesaro projection have
written proofs, not numerical certificates.

**N6 — partial-closure paths.** Restricting the comparator to G or Q gives
the useful precise theorems above but does not derive a broader physical
identification. Alternatively derive CL2 or GEO from the original law.
No new axiom is required or proposed; approved units, structural isotropy
and realized-state references are not substitutes for these correlation
estimates and are not declared missing primitives.

**N7 — steelman against a broad negative conclusion.** The failure of
logarithmic and collinear diagnostics is not failure of all correlation
tests. The free tensor numerator already yields (10), which escapes the
constructed counterexample. A classification of finite scalar/tensor Wick
diagrams compatible with the full free-YM multi-geometry scaling limit,
followed by a controlled nonleading connected coefficient, could exclude
much more of WGF. The terminal missing steps are that classification and
actual-e matching, not a theorem that they cannot exist. The broader claim
therefore remains OPEN rather than being declared impossible.

**N8 — prior-cycle comparison.** WITNESS's elementary GFF AF counterexample,
CUMUL's Gaussian-on-e restriction, and COMBO's composite/mixture examples
were checked at their actual scope. The present CL2 theorem removes the
mixture escape by an additional infrared condition; it does not erase the
composite escape. The geometric route addresses a different surviving
restriction. Targeted local-main/lane searches and incomplete remote
coverage are recorded in MIXGFF_LOG; no exhaustive novelty claim is made.

## 7. Verification, attribution and handoff

The derivations above are exact written arguments. The finite-algebra
[criteria](checks/mixgff_criteria.md) were registered before the checker.
The sandbox rejected `nice -n 10` with `Operation not permitted`, so numerical
checks are **NOT RUN**, with no claimed PASS counts. This is an execution
limit, not scientific evidence. The reviewer record and final source binding
are maintained in MIXGFF_LOG; no status is inherited from a review headline.

For attribution only: Duetsch and Rehren,
[Generalized free fields and the AdS-CFT correspondence](https://arxiv.org/abs/math-ph/0209035),
discuss Gaussian/KL fields separately from their conformal specializations.
Dolan and Osborn,
[Conformal Four Point Functions and the Operator Product Expansion](https://arxiv.org/abs/hep-th/0011040),
use four-point geometry and compare free scalar, fermion and vector theories.
The spectral, Wick-cycle and reflection calculations required here were
rebuilt above; those papers do not supply a YM theorem. The mean-ergodic
projection method is also proved directly in §4.2. No [m] memory item carries
argument weight.

The next scientific decision is whether to pursue CL2's infrared block
estimate or GEO's noncollinear source matching first. Both retain the actual
original-law remainder and continuum obligations. Full existence, arbitrary
WGF exclusion and the physical YM mass gap remain OPEN.
