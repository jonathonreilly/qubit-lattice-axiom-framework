# Spectral ADM jets on a strict band, using the full finite canonical bracket

Author research result, 2026-09-30. No axiom, primitive, retained claim, or
audit status is changed. This report supplies a changed continuous canonical
comparator and proves a restricted coefficient identity. Independent checking
is required before downstream reuse. `CONTRACT.md` was frozen before calculation.

The construction works at the declared finite Taylor orders. Its decisive
ingredient is a coefficient-transfer lemma for full Poisson contraction trees,
not a projection of the bracket onto low modes. It also works, to the same
orders, with a separately supplied canonical scalar and all gravity--scalar
cross terms. It does **not** preserve a fixed band under evolution and is not
an exact first-class algebra on the full finite carrier. A real, seven-site
axial example below gives a nonzero full-zone GG defect.

## 1. Source and premise boundary

The selected procedural/scientific source is
`7146fe17a76de41badcaca3c3c7cac6d11eb2a00`; the refreshed main source is
`9d15f404c63ff5b9d877e2bdc06ea8713493ffb4`. Working HEAD is separate and is
recorded in `SOURCES.json`. Relevant baseline procedure, axiom, primitive,
block 62 and block 112 bytes are checked there. No continuous metric carrier,
ADM law, scalar matter, or spatial spectral derivative is inferred from the
minimal axioms or their three registered primitive bodies.

Closest prior arguments actually inspected:

* Main block 112 proves the flat-strain, momentum-linear lapse bracket for
  its specified staggered nearest-difference law. It does not prove its
  nonlinear completion. `NONLINEAR_CONTRACT.md` and
  `INDEPENDENT_SEED_CHECK.md` fix the positive spatial-Lie sign used here.
* Main `SOFT_SPIN2_COLLISION_INVARIANTS_COMMON_CONES_AND_LATTICE_WARD_BOUNDARIES_...`
  sections 6--7 prove an analytic periodic open-patch dispersion obstruction
  and controlled improved-stencil infrared errors. Their bounded periodic
  analytic symbol hypothesis is not imposed on the present spectral
  representative, and neither statement is an ADM constraint construction.
* The actual PR 9363 head
  `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`, viability-map A1, proposes
  fixed-seed local next-order closure and leaves nonlocal corrections open.
  Its expected failure is not a mathematical premise. Its harmonic finite-slot
  tensor argument is not a theorem about the carrier supplied here.
* A final open-proposal refresh also found PR 9394 at
  `d72d4713e07f7b255d8db1ec47c01288214ecc8b`. Its complete actual
  `FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_...` note was
  read. Its matrix-trace proof uses the supplied staggered linear
  generators, finite support and an exact mixed identity with a nonzero
  affine lapse moment. It explicitly leaves changed seeds and controlled
  infrared constructions open. The present derivative, spatial support and
  evaluation domain change those premises; no contradiction is hidden by a
  claim that a global periodic affine lapse exists.
* The pack's `decay-symbol-route/REPORT.md` leaves the nonlinear spectral/band
  escape open. `independent-discrete-route/REPORT.md` supplies exact cochain
  kinematics with extra carriers, not ADM normal generators.

This search supports a distinct route in this campaign, not a claim of
historical novelty. No external literature theorem is needed for the
self-contained bracket and transfer derivations below.

The mathematical family tuple is: odd finite cubic tori; six real canonical
metric/momentum entries per site; the collocated spectral derivative; ordinary
full-grid products; ADM density with constants a=1/(4 alpha)>0 and K>0;
strict low-band evaluation data; full-carrier canonical Poisson contractions;
Taylor order (CC,GC,GG,Jacobi)=(3,3,2,2). The optional seventh scalar pair is
an explicitly additional carrier. All zero modes are retained.

## 2. Carrier, volume, placements, and derivative

Let the continuum comparison torus be `(R/2pi Z)^3`, with normalized mean
`<f>=(2pi)^-3 integral f`. Let n=2J+1, V=n^3, and x=2pi r/n for
r in `(Z/nZ)^3`. The full real phase space has

    {h_A(r),P_B(s)} = delta_AB delta_rs,   A=(11,22,33,12,13,23).

Set p_A=V P_A and define the symmetric matrix density pi by

    pi_ii=p_ii,    pi_ij=p_ij/2 (i<j),    g=I+h.

Then `(1/V)sum_r pi^ij delta h_ij=sum_(r,A)P_A delta h_A` exactly. In
Fourier convention `fhat(k)=V^-1 sum_r f(r) exp(-ik.x_r)`,

    {hhat_A(k),phat_B(l)}=delta_AB delta_(k+l=0 modulo n).             (1)

Thus no hidden volume factor enters a continuum normalized-mean bracket.
Reality means fhat(-k)=conjugate(fhat(k)); complex mode calculations mean
the complexification of this real bracket, not a new complex canonical law.

The full frequency representatives are Q_J={-J,...,J}^3, and

    (D_j f)hat(k)=i k_j fhat(k).                                    (2)

Products are pointwise on the full grid, equivalently convolution modulo n.
D is skew under the grid mean, but does not satisfy a global product rule.
For distinct indices on a one-dimensional grid its matrix is
`D_rs=(-1)^(r-s)/(2 sin(pi(r-s)/n))`; every off-diagonal entry is nonzero.
In three dimensions each component acts along whole coordinate lines.
This gives an explicit spatial support price, growing with the torus.
No projection to a smaller band occurs in either the Hamiltonians or (1).
All independently specified h, pi, lapses N,M,L and shifts X,Y,Z at which
the asserted coefficients are evaluated obey

    supp fhat subset Q_B,     B integer >=0,     5B <= J.            (3)

The same condition covers phi,p when the scalar is included. This is a
restriction on evaluations, not a reduced symplectic phase space. A high
mode set to zero can have a nonzero Hamiltonian derivative and is retained.

For comparison with block 62 placements, a slot whose physical offset is
s_A has a canonical rephasing of both coordinate and momentum by
`exp(-ik.s_A)`, with s_ii=0, s_ij=(2pi/n)(e_i+e_j)/2. The corresponding
shift offset is (2pi/n)e_j/2. Opposite k phases cancel in (1); odd n avoids
a self-conjugate Nyquist mode. This is real orthogonal spectral interpolation,
usually nonlocal in position space. The new constraints are **defined after**
that map with one common collocated lapse. Pulling them back does not give
the old four-corner lapse timing. Nor does ik equal the nearest-difference
symbol `2i sin(k pi/n)/(2pi/n)` away from zero. Even the linear finite-zone
seed is deliberately changed, although its smooth limit and canonical sign
are preserved. This report makes no claim to solve fixed-seed A1.

## 3. Full finite sampled functions and explicit jets

On a neighborhood of g=I with g positive definite, define finite analytic
functions using the full-grid operations:

    Gamma^k_ij = (1/2) g^kl (D_i g_jl + D_j g_il - D_l g_ij),
    R_D = g^ij (D_k Gamma^k_ij - D_j Gamma^k_ik
                 + Gamma^k_kl Gamma^l_ij - Gamma^k_jl Gamma^l_ik),
    C[N] = < N [a/sqrt(det g) {tr(g pi g pi)-tr(g pi)^2/2}
                                 -K sqrt(det g) R_D] >_grid,
    G[X] = < pi^ij [X^k D_k g_ij+g_ik D_j X^k+g_jk D_i X^k] >_grid. (4)

The curvature formula is a definition; no false discrete Leibniz rule is
used to rewrite it. Degree counts every h and pi as one, while all smearings
have degree zero. Define t=tr h, t2=tr(h^2), t3=tr(h^3), and

    s0=1,  s1=t/2,  s2=t^2/8-t2/4,
    s3=t^3/48-t t2/8+t3/6,
    u1=-t/2,    u2=t^2/8+t2/4.                                    (5)

These are the needed coefficients of sqrt(det g) and its inverse. To give
all curvature coefficients without suppressed derivative placements, put

    H_r=(-h)^r,
    Gamma_r^k_ij=(1/2)H_(r-1)^kl(D_i h_jl+D_j h_il-D_l h_ij),
    L_r,ij=D_k Gamma_r^k_ij-D_j Gamma_r^k_ik,
    Q_rs,ij=Gamma_r^k_kl Gamma_s^l_ij-Gamma_r^k_jl Gamma_s^l_ik.

All r,s in Gamma,L,Q below are positive. The explicit coefficients are

    R1 = delta^ij L_1,ij,
    R2 = delta^ij(L_2,ij+Q_11,ij)-h^ij L_1,ij,
    R3 = delta^ij(L_3,ij+Q_12,ij+Q_21,ij)
           -h^ij(L_2,ij+Q_11,ij)+(h^2)^ij L_1,ij,
    R4 = delta^ij(L_4,ij+Q_13,ij+Q_22,ij+Q_31,ij)
           -h^ij(L_3,ij+Q_12,ij+Q_21,ij)
           +(h^2)^ij(L_2,ij+Q_11,ij)-(h^3)^ij L_1,ij.             (6)

For example R1=D_i D_j h_ij-D_k D_k tr h. Formulas (5)--(6) are finite
polynomials in the declared full-grid operations. They require no expansion
by integration by parts and remain defined for arbitrary lapse.

Let

    A0=tr(pi^2)-tr(pi)^2/2,
    A1=2tr(h pi^2)-tr(pi)tr(h pi),
    A2=tr(h pi h pi)-tr(h pi)^2/2.

The density coefficients of C are

    C1 = -K R1,
    C2 = a A0-K(R2+s1 R1),
    C3 = a(A1+u1 A0)-K(R3+s1 R2+s2 R1),
    C4 = a(A2+u1 A1+u2 A0)-K(R4+s1 R3+s2 R2+s3 R1).             (7)

In (7), C_d[N] means the grid mean of N times the displayed density.
In particular the nonlinear lapse dependence is supplied, not fixed by the
old uniform quadratic potential alone. The spatial generator is exactly

    G1[X]=2<pi^ij D_i X_j>,
    G2[X]=<pi^ij(X^k D_k h_ij+h_ik D_j X^k+h_jk D_i X^k)>,
    G3=0 and every higher G coefficient=0.                        (8)

Set s=aK and v_j=N D_j M-M D_j N. The structure jets are

    F0^i=s v_i,    F1^i=-s h^ij v_j,    F2^i=s(h^2)^ij v_j,
    U(X,N)=X^j D_j N,
    V(X,Y)^i=X^j D_j Y^i-Y^j D_j X^i.                            (9)

Thus there are no h corrections to U,V in this supplied family. C4 cannot
be omitted at the target order: {G1,C4} has degree three, and a nested
bracket of degrees (4,1,1) has degree two. Equations (6)--(7) specify C4
explicitly, rather than presuming a cubic truncation suffices for Jacobi.

## 4. Continuum bracket derivation, including the sign

In this section only, replace D by the ordinary torus derivative, products
by ordinary products, and the mean by the continuum mean. The canonical
matrix pairing remains exactly that of section 2.

G is the cotangent generator of the positive spatial Lie action:

    {g_ij,G[X]}=X^k partial_k g_ij+g_ik partial_j X^k+g_jk partial_i X^k,
    {pi^ij,G[X]}=partial_k(X^k pi^ij)
                       -pi^kj partial_k X^i-pi^ik partial_k X^j.  (10)

The second formula treats pi as a contravariant tensor density of weight
one. The same displayed formulas, with D and its unexpanded product,
give the exact full-grid Hamiltonian action of (4), because D is skew.
In the continuum, the Lie-commutator identity and scalar-density variation
therefore give

    {G[X],G[Y]}=G[[X,Y]],       {G[X],C[N]}=C[X.partial N].         (11)

For clarity the nontrivial CC identity can be derived directly. Put
pi_g=g_ij pi^ij and lower the two indices of pi with g. Then

    delta C[N]/delta pi^ij
       =2a N/sqrt(g) (pi_ij-g_ij pi_g/2),
    delta <N sqrt(g)R>/delta g_ij
       =sqrt(g)[-N Einstein^ij+nabla^i nabla^j N-g^ij Delta_g N]. (12)

The latter follows from delta sqrt(g)=sqrt(g)g^ij delta g_ij/2,
delta Gamma^k_ij=g^kl(nabla_i delta g_jl+nabla_j delta g_il
-nabla_l delta g_ij)/2, and two integrations by parts on the torus.
There is no boundary assumption beyond periodicity. The kinetic--kinetic
bracket is zero by ultralocality and antisymmetry in NM. The curvature--
curvature bracket is zero. The Einstein-tensor terms in the two cross
brackets cancel by the same NM antisymmetry. Finally in dimension three,

    (pi_ij-g_ij pi_g/2)
       (nabla^i nabla^j N-g^ij Delta_g N)=pi^ij nabla_i nabla_j N.

Consequently

    {C[N],C[M]}=2s<pi^ij(N nabla_i nabla_j M-M nabla_i nabla_j N)>
               =G[s g^ij(N partial_j M-M partial_j N)].          (13)

The first-derivative cross term in G on the last line vanishes against
symmetric pi. This fixes the sign. At h=0, C1=-K R1 gives
`2s<pi^ij(N partial_i partial_j M-M partial_i partial_j N)>`, equal
to G1[+s(N partial M-M partial N)]. No shift sign is selected merely to
make a calculation agree.

## 5. Full-carrier coefficient-transfer lemma

Consider homogeneous polynomial local continuum functionals built from
fields, derivatives, contractions and one external smearing per functional.
Use their identical expression trees with full-grid D and products. A
functional of field degree d has d field leaves and one smearing leaf.
Ordinary full variation removes one field leaf; it is NOT first restricted
to the low-band subspace. Thus its evaluated gradient can have support dB,
including modes absent from the input data.

Expand one or a nested sequence of canonical Poisson brackets by the
product rule for functional differentiation. Each term is a graph whose
vertices are original functionals and whose edges are canonical contractions.
For a nested bracket of t original functionals, this graph is a tree with
t-1 edges: a new bracket joins a new functional to one of the previous
vertices. The canonical Poisson tensor is constant, so differentiating it
does not create additional vertices or loops. An ordinary derivative on a
field or on a product supplies the Fourier momentum on that expression-tree
edge; its multiplier is checked in the same way as a contraction edge.

If the final field degree is r, the number of surviving external leaves is

    r+t = sum_v d_v -2(t-1)+t.                                   (14)

Each leaf is an original evaluated field or an original independent
smearing, so has componentwise momentum bounded by B. To see why an
apparently high internal contraction is not being discarded, cut that
edge of the tree. Momentum conservation at its vertices fixes its
unwrapped momentum to the signed sum of the surviving external leaves
on either component. All momenta in every differentiated product subtree
are likewise sums of a subset of leaves. Hence every such momentum has
componentwise absolute value at most (r+t)B.

If `(r+t)B<=J`, each required unwrapped internal momentum exists among the
FULL finite carrier modes, every spectral multiplier equals the continuum
multiplier, and no partial convolution wraps. There is no extra free loop
momentum to sum over. The final grid mean and continuum mean also agree:
the total external momentum has size at most J<n, so equality to zero
modulo n means equality to zero. Coefficients, tensor-index sums and
canonical contraction normalizations agree by (1). Therefore the value
of the entire homogeneous nested bracket equals its continuum value.

This proves transfer of the full contracted coefficient, even when high
input modes are zero but their functional derivatives are not. It does
not infer equality of full gradients from equality of restricted values.
In particular one must apply the lemma afresh to a nested bracket; taking
a Poisson bracket of an identity known only on the band would be invalid.

For CC or GC through r=3, t=2 gives at most five leaves. For nested Jacobi
through r=2, t=3 again gives at most five. GG has r<=2,t=2 and is covered
as well. The expressions on the proposed right sides have respectively
the same number of field and original smearing leaves; composed shifts
F,U,V are not reset to band B. For example F2 can have support 4B, and
G1[F2] still has only five original leaves. This explains the conservative
common bound (3) and includes arbitrary permitted zero modes and all
permitted lapse/shift combinations. It is sufficient, not advertised as
optimal.

Applying the lemma to (11)--(13) proves the finite statements

    [{C_<=4[N],C_<=4[M]}-G[F0+F1+F2]]_degree<=3=0,
    [{G[X],C_<=4[N]}-C_<=4[X.DN]]_degree<=3=0,
    {G[X],G[Y]}-G[[X,Y]]=0                                     (15)

at every evaluation (3), using the full finite bracket. In the last line
the polynomial has degree at most two, so no degree projection is needed.

## 6. Jacobi, field-dependent shifts, and analytic remainder

Canonical Jacobi is exact on the full finite phase space for any finite
smooth functions, regardless of (3) or constraint closure. The additional
claim here is consistency of the **substituted structure expressions**
through degree two. Apply the t=3 transfer lemma, rather than differentiating
a band-restricted equality. C4 includes every possible vertex degree at
this order. Continuum covariance and its canonical bracket then give the
GCC, GGC and GGG structure identities with their field-dependent arguments.

The CCC case makes the often omitted term explicit. In the continuum,

    {{C[N],C[M]},C[L]}
       =C[F(N,M).partial L]+G[{F(N,M),C[L]}],
    {F^i(N,M),C[L]}
       =-2 a s L/sqrt(g) (pi^ij-g^ij pi_g/2)
                          (N partial_j M-M partial_j N).         (16)

The cyclic sum of the C smearings vanishes by symmetry of g^ij. The cyclic
sum of the G smearings vanishes because
`sum_cyclic L(N partial_j M-M partial_j N)=0`. Thus the metric dependence
of F is differentiated; it is not silently frozen. The same low-order
coefficient statement follows on the grid by the tree lemma. For the mixed
Jacobi identities the transformation of g^{-1} follows from (10), while
N is an independent scalar smearing; the ordinary tensor Lie identity
supplies precisely the additional shift variation. Together with (11),
this is a direct continuum cotangent/covariance derivation, not a supposition
that a projected Lie algebra has Jacobi.

More explicitly, with delta_X F={F,G[X]} and fixed independent N,M, the
GCC shift identity is

    F(X.partial N,M)+F(N,X.partial M)-[X,F(N,M)]+delta_X F(N,M)=0.

Indeed v=N dM-M dN is a covector and the first two terms equal
`s g^{-1} L_X v`, while the final two equal its negative by
`delta_X g^{-1}=L_X g^{-1}`. The GGC scalar identity is

    [X,Y].partial N-X.partial(Y.partial N)+Y.partial(X.partial N)=0.

GGG is `sum_cyclic [[X,Y],Z]=0`. These identities plus (16) list all
Jacobi types. On the finite grid, delta_X g^{-1} is always computed as
`-g^{-1} {g,G[X]} g^{-1}`; replacing it by the continuum tensor-Lie formula
is justified only for the coefficients transferred under (3), not globally.

There is also an honest local Taylor-error statement for the full analytic
sampled functions (4). Fix low-band hbar,pibar and all smearings, and set
h=epsilon hbar, pi=epsilon pibar. In a sufficiently small complex disk
|epsilon|<R, every pointwise inverse and square root has its analytic branch
connected to g=I; a sufficient condition is
`R max_x ||hbar(x)||_op<1`. The CC and GC residuals of the full expressions
and full proposed structures are analytic and their coefficients through
epsilon^3 vanish by (15). For any smaller radius where the closed complex
circle is regular, Cauchy's bound gives

    |residual(epsilon)| <= M_R (|epsilon|/R)^4/(1-|epsilon|/R),
    M_R=max_(|z|=R)|residual(z)|.                                (17)

For the scalar, scale phi,p by epsilon too. This is a rigorous local
finite-system error bound, not an estimate uniform in changing n or in
unspecified norms. The exact polynomial coefficient identity (15) is the
stronger concrete output at the declared order. No exact closure of the
full rational/nonpolynomial sampled expressions is inferred.

## 7. An explicitly additional canonical scalar, with cross terms

Add phi(r),P_phi(r), {phi(r),P_phi(s)}=delta_rs and density p=V P_phi.
The added continuum and finite functions, with the same respective
operations, are

    C_m[N]=<N[p^2/(2 sqrt(g))
                  +s sqrt(g) g^ij D_i phi D_j phi/2
                  +m^2 sqrt(g) phi^2/2]>,
    G_m[X]=<p X^i D_i phi>,       s=aK.                           (18)

Take zero scalar background and count phi,p as degree one. Writing
phi_i=D_i phi, the explicit scalar density jets are

    M2=p^2/2+s phi_i phi_i/2+m^2 phi^2/2,
    M3=u1 p^2/2+s(s1 delta^ij-h^ij)phi_i phi_j/2
                                             +m^2 s1 phi^2/2,
    M4=u2 p^2/2+s(s2 delta^ij-s1 h^ij+(h^2)^ij)phi_i phi_j/2
                                             +m^2 s2 phi^2/2.   (19)

There is no scalar degree-one term and G_m is exactly degree two.

Here is why this is a common-action matter result for the supplied scalar,
not an omission of the difficult cross terms. In the continuum,

    delta C_m[N]/delta p=Np/sqrt(g),
    delta C_m[N]/delta phi
       =-s partial_i(N sqrt(g)g^ij partial_j phi)+N sqrt(g)m^2 phi.

Their bracket is `G_m[s g^{-1}(N partial M-M partial N)]` by direct product
expansion. The gravity curvature has no momentum, so its bracket with C_m
is zero. The gravity kinetic--scalar cross bracket is generally nonzero
before antisymmetrization; however delta C_m[N]/delta g is local in g and
proportional to N, and delta C_g[M]/delta pi is local and proportional to
M. Consequently the two cross terms cancel exactly in the antisymmetric
CC combination. This cancellation uses that (18) contains no derivatives
of g, and does not hold automatically for arbitrary matter couplings.

G_g+G_m generates Lie action on every field: delta phi=X.partial phi and
delta p=partial_i(X^i p), alongside (10). Therefore its mixed bracket
with C_g+C_m transforms the entire common scalar density, including the
metric factors. GG is the combined cotangent Lie generator. This proves
the continuum total algebra with exactly the same F,U,V, for all m^2
(m^2>=0 may be chosen without affecting this algebraic result).

The scalar and its cross terms have the same field-leaf counting, so the
transfer proof gives (15) and the Jacobi order for the total constraints
using (19). More generally kinetic coefficient b and gradient coefficient
c would require bc=aK for this normalization; this equality is supplied,
not derived from a walker speed. The scalar extension is not the original
walker, does not reproduce its finite-zone energy/current, and supplies no
record instrument or birth-energy mechanism. Those original-matter
obligations remain open.

## 8. Exact checks and a full-zone boundary witness

`check.py` implements sparse circular Fourier products over Q_J with exact
Gaussian rational coefficients, ordinary field-degree truncation and forward
directional differentiation of the Christoffel definition (4). It does not
use a continuum curvature variational formula in its tested brackets.

For CC it uses the exact full-grid coordinate velocities
`delta g=2a N/sqrt(g)(g pi g-g tr(g pi)/2)` and, for the scalar,
`delta phi=Np/sqrt(g)`. Directionally differentiating C[N] in the coordinate
velocities of C[M], then subtracting the reverse term, is precisely the
full canonical bracket; it includes all generated Fourier modes. For GC/GG
it uses the exact grid cotangent action (10), preserving D(X pi) as a
product derivative. It retains all six symmetric components, even on an
axial evaluation. This prevents the common error of reducing the carrier
before taking derivatives. Coefficients a=2,K=3,s=6,m^2=5 are diagnostics;
the analytic proof retains arbitrary a,K and m^2.

`axial.json` and `mixed.json` give the sparse evaluations and all six vacuum
and total-scalar residual checks. They are exact checks of selected fields
and smearings, not exhaustive coefficient enumeration. The transfer proof
and continuum derivation establish the general identity. The matrix entries
and sine/cosine fields are reproducible directly from the script.

The all-zone failure has a short independent derivation. On n=7 (J=3),
take fields independent of y,z, h_yy=q, pi^yy=p, all other h,pi zero, and
X,Y along x. The relevant quadratic spatial generator is `<p X Dq>`;
the full linear-generator terms contribute zero on this evaluation. For
Fourier modes X=e^(iax),Y=e^(ibx),q=e^(icx),p=e^(idx), the coefficient of
the GG defect is

    -c [wrap(b+c)-wrap(a+c)-(b-a)]

when a+b+c+d=0 modulo 7. Choose real X=1, Y=cos(3x), q=cos x, p=cos(3x).
The two conjugate wrapped combinations (a,b,c,d)=(0,3,1,3) and
(0,-3,-1,-3) each contribute 7/8. Therefore

    {G[X],G[Y]}-G[X DY-Y DX]=7/4.                                (20)

With q,p multiplied by epsilon the defect is (7/4)epsilon^2. The script
checks (20) using the full tensor generator and canonical directional
variation, not only the reduced scalar formula. `alias.json` records it.
These modes violate (3); this is a boundary witness for the supplied law,
not a no-go for every spectral or nonlocal gravity construction.

## 9. What is obtained and what is still missing

This constructs explicit cubic and necessary quartic scalar coefficients,
the exact quadratic spatial generator and quadratic structure jet, with
CC/GC/GG and structure-Jacobi obligations at the specified next orders.
The finite carrier and its canonical bracket remain intact. Spectral
nonlocality and a strict evaluation band are the explicit price.

The band is not invariant: already the term X.Dh in (10) sends generic
band-B X and h to a 2B mode. For example an axial transverse h_yy=cos(Bx)
and X^x=sin(Bx) produce a nonzero cos(2Bx) contribution. Repeated evolution
need not remain in the domain in which (15) has been proved. The metric
inverse also has infinitely many Taylor orders and does not preserve finite
Fourier support. Simply deleting newly generated modes changes the bracket
problem; no projected-product or projected-generator Jacobi theorem is
assumed here.

The precise remaining nonlinear gravity obligation is an invariant domain
and an exact constraint ideal (or a quantitatively controlled continuum
evolution/constraint-error theorem) for the chosen full dynamics. Exact
finite-band preservation of these unmodified flows is already false by
the 2B example; another law, moving resolution, or a different state/domain
notion would have to be supplied and checked. Proving exact first-class
closure on such an invariant domain is comparable in strength to the
original nonlinear completion, not a routine corollary of this jet.

This leaves additional and separate physical obligations: obtain this
continuous/nonlocal carrier and law from allowed framework data if claimed
native, couple the actual walker and its conserved source/current, derive
actual readable records, and justify a continuum regime. A canonical scalar
comparison does not discharge those tasks. No interacting gravitational
phase, helicity-two-only theory at all scales, or TOE completion follows.
