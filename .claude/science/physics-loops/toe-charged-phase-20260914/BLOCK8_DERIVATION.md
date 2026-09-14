# Soft spin-2 consistency: collision invariants and lattice domains

Working derivation. Author-proposed conditional mathematics, not independent
review, native spin-2 existence, an empirical prediction or an axiom wall.
Hertzberg–Sandora 1704.05071v2 supplies the prior soft-graviton universality
argument. The purpose here is to make the collision and pole steps explicit,
avoid assuming full rotational symmetry of the hard matter bands, and
identify concrete finite-lattice compatibility tests. No novelty claim is
made for the general equivalence-principle or relativistic-dispersion result.

## 1. Elastic collision invariants without assuming Lorentz symmetry

Let a finite set of species s have connected open momentum domains U_s in
R^d, d>=2, C^2 energy E_s and velocity v_s=grad E_s. At least three velocities
of each species are noncollinear. A C^1 scalar f_s is an additive collision
invariant if f_s(p)+f_t(q) is unchanged in every allowed s+t -> s+t collision.
Assume rich elastic scattering: for every p,q with v_s(p)!=v_t(q), f is
constant on a neighborhood of (p,q) in the surface of fixed total momentum
and energy. It suffices that the physical amplitude be nonzero on a dense
subset of every such neighborhood, with the Ward identity continuous there.
This is a substantial scattering hypothesis, not a consequence of locality.
Self-collisions are included. Mixed elastic pairs form a connected species
graph. Momenta are additive real vectors in these domains, not merely
crystal momenta modulo a reciprocal lattice vector.

Fix p,q and vary them as p+delta,q-delta. The energy constraint has nonzero
gradient v_s(p)-v_t(q), so the implicit-function theorem gives every tangent
delta orthogonal to that difference. Differentiating f conservation gives

    grad f_s(p)-grad f_t(q)
        = lambda_st(p,q) [v_s(p)-v_t(q)].                 (1)

For one species choose p1,p2,p3 with noncollinear velocities v1,v2,v3. Put
F_i=grad f(p_i). Adding the three difference equations gives

    (lambda_12-lambda_13)(v1-v2)
      +(lambda_23-lambda_13)(v2-v3)=0.

The two vectors are linearly independent, so all three lambda agree, beta.
Then F_i=beta v_i+gamma. For any p, at least two of the anchor differences
v(p)-v_i are nonparallel (or p coincides in velocity with an anchor and the
other two suffice). Equation (1) forces

    grad f(p)=beta grad E(p)+gamma.

Connectedness integrates this to f(p)=beta E(p)+gamma.p+alpha. This argument
needs no convexity, inverse Hessian or open velocity image; a spherical
massless velocity image is allowed. Collinear/one-dimensional or sparse
collision systems are outside the stated theorem.

For a mixed species edge, substitute the two species forms into (1). For
fixed w in the target velocity image,

    [(beta_s-beta_t)w+(gamma_s-gamma_t)]
        is parallel to every v-w in the source image.

Its three noncollinear source velocities force this bracket to vanish.
Two different target velocities then imply beta_s=beta_t and gamma_s=gamma_t.
Connectedness of the species graph makes beta,gamma universal, leaving only
alpha_s species constants. For reactions, conservation further requires
sum_in alpha_s=sum_out alpha_s. Thus alpha is exactly in the nullspace of
the supplied reaction stoichiometry; no claimed completeness of the actual
physical reaction menu is implied.

## 2. A precise soft-residue hypothesis and factorization lemma

For positive-energy simple external poles define

    zeta_s(p)=(E_s(p), E_s(p) grad E_s(p)).

A normalization of each pole to (p0)^2-E_s(p)^2 is permissible locally for
E_s>0; wavefunction normalization belongs in the effective emission vertex.
For spin or degenerate bands assume the leading residue is diagonal in the
stated external channel and represented by a real symmetric matrix T_s^{mu nu}(p),
after stripping a common vertex phase in a Hermitian diagonal-source convention.
From this section onward there are three spatial dimensions. The effective
residue is C^1 in hard momentum on each stated channel domain.
Matrix-valued band mixing is not silently covered.

Assume the leading soft emission factor is the sum of external poles, with
all internal/contact contributions subleading under the gauge variation:

    W^nu(q)=sum_legs eta_a q_mu T_a^{mu nu}/(q.zeta_a)=0. (2)

Here eta is + for outgoing and - for incoming, q_mu=(c_g |q|,-q), and
c_g>0 is the infrared spin-2 speed. Equation (2) is an exact leading-soft
Ward identity at every hard momentum in the declared domains. Merely
having a transverse-traceless quadratic covariance does not supply it.
This can be read as a tree-level consistency theorem. Beyond tree level,
infrared-dressed scattering and control of its leading soft residue are
additional obligations, not results of the present lattice construction.

For a given hard process, suppose the real pole vectors zeta_a have
pairwise distinct projective classes, equivalently distinct group velocities.
Require that every hard momentum under discussion occurs in such a process,
or is a continuity limit of covered momenta. A completely unresolved
same-velocity pole group cannot be separated by this argument.

Here is a direct polynomial proof of the needed pole separation. Clear all
denominators in (2). Its components are homogeneous polynomials in soft q.
A rational stereographic parametrization of the real null directions has
spatial components proportional to (2u,2v,1-u^2-v^2) and temporal component
c_g(1+u^2+v^2). Vanishing on a real open set implies the substituted
polynomial vanishes identically for complex u,v. This parametrization is
dense in the complex null quadric Q(q)=Omega^2/c_g^2-|q_spatial|^2=0, so
the cleared identity holds there. No real subluminal pole was assumed.

Restrict Q to the three-dimensional complex hyperplane l_a(q)=q.zeta_a=0.
Its rank is at least two. Here nullness of zeta refers to the dual form
c_g^2(zeta^0)^2-|zeta_spatial|^2.
If zeta_a is not null, the rank is three and the
zero set is an irreducible quadratic cone spanning that hyperplane. A
nonproportional l_b cannot vanish on it. If zeta_a is null, the restriction
has rank two: in real Lorentz coordinates its zero set consists of two
complex-conjugate planes. A real l_b vanishing on one must vanish on the
other too, and hence on their span, contradicting nonproportionality.
Thus deleting every other pole hyperplane still leaves a set spanning
ker l_a. These assertions follow also by diagonalizing the nondegenerate
Lorentz form and its one-hyperplane restriction.

Multiply (2) by all denominators and restrict to that unshared set. Every
other summand vanishes, leaving q_mu T_a^{mu nu}=0. Its linear functional
therefore vanishes on ker l_a and is proportional to l_a for every nu.
Consequently T_a=zeta_a tensor b_a. Symmetry of T_a and nonzero zeta_a give
b_a=g_a zeta_a:

    T_a^{mu nu}=g_a zeta_a^mu zeta_a^nu.                  (3)

This includes null hard poles in four spacetime dimensions. Continuity
extends it to covered exceptional hard configurations. Matrix-valued
unresolved pole groups still require a different argument. The all-four-
parameter metric Ward identity is part of the premise; adding an arbitrary
trace tensor invisible in a TT gauge does not automatically provide a
completion satisfying that stronger identity.

Substituting gives four additive collision invariants f_s^mu=g_s zeta_s^mu.
The coefficient g may be a smooth function of hard momentum and species at
this point. No universal coupling has been assumed.

## 3. Symmetry of the residue yields a common quadratic shell

Continuous rotations, cubic symmetry, convexity and boost invariance of the
matter dispersion are unnecessary for this step. Write the four collision
invariants in their general forms, with universal coefficients:

    f_s^0 = kappa E_s + b.p + Q_s,
    f_s^i = beta_i E_s + A_ij p_j + a_si.                 (4)

Species constants Q_s and a_s are constrained by the actual reaction menu.
Since f^i=f^0 partial_i E, let L=kappa E+b.p+Q. Differentiate this equation
in p_j, subtract the result with i,j interchanged and use Hessian symmetry:

    (b_j+beta_j) v_i-(b_i+beta_i) v_j = A_ij-A_ji.        (5)

Subtract (5) at three noncollinear velocities. The fixed vector b+beta must
be parallel to two nonparallel velocity differences, so beta=-b and A=A^T.
Integrating the remaining gradient equation over a connected domain gives

    kappa E_s^2+2(b.p+Q_s)E_s
        = p^T A p+2 a_s.p+B_s.                           (6)

This is one common quadratic energy-momentum form, with species affine
offsets. The statement comes from differentiating the actual energy shell;
it does not assume a common metric before deriving it.

For the simpler rotationally invariant scalar-channel case (or proper cubic
covariance with each species preserved), the invariant representation has
no fixed vector and the vector commutant is scalar. Thus b=beta=0, a_s=0
and A=a I. This recovers the earlier equation kappa E_s^2+2Q_s E_s=a|p|^2+B_s.
If kappa=0 and a!=0, a coupled matter species with Q_s!=0 has the Galilean
branch E_s=a|p|^2/(2Q_s)+B_s/(2Q_s). That matter-only consistency solution
has not been promoted to a full propagating spin-2 theory.

## 4. Hard graviton participation fixes the cone, not the constants

Suppose a hard graviton belongs to the same connected rich-scattering domain,
and E_g(r n)=c_g r+o(r) as r decreases to zero along every unit direction n,
with c_g>0. This supplied infrared graviton law must be verified in a native
construction. Inserting it in (6) first gives B_g=0 and then

    Q_g c_g = a_g.n  for every n,

hence Q_g=0 and a_g=0. The quadratic term gives

    kappa c_g^2+2c_g b.n = n^T A n.

Comparing n and -n gives b=0, and A=kappa c_g^2 I follows. A nonzero hard-
graviton coupling excludes kappa=0, because that would make its complete
f_g and T_g vanish. The exact equations over the declared hard domains are

    E_g^2=c_g^2 |p|^2,
    [E_s+Q_s/kappa]^2=c_g^2 |p-K_s|^2+mu_s^2,            (7)
    K_s=-a_s/(kappa c_g^2),
    mu_s^2=B_s/kappa+(Q_s/kappa)^2-c_g^2 |K_s|^2.

Every species has the same cone about its allowed momentum center K_s.
Neither full rotation symmetry of the hard matter bands nor the absence
of Weyl-node offsets was assumed. This is the form relevant to a valley
construction. If a stable continuation reaches p=K_s with real shifted
energy then mu_s^2>=0; domains excluding the center need an additional
stability assumption for that sign. The energy shift is explicitly

    epsilon_s=E_s+Q_s/kappa,    pi_s=p-K_s.

For real-additive momentum reactions these shifts preserve energy/momentum
conservation only when their species constants satisfy the reaction charge
conditions. They change generators by internal charges. Operational clock
or frequency identifications do not disappear as notation.

In these variables g_s zeta_s=kappa(epsilon_s,c_g^2 pi_s). Away from
epsilon_s=0, dividing the rank-one numerator by its pole denominator cancels the original E_s/epsilon_s
normalization, leaving the usual common-metric soft factor. The residue and
physical dispersion statements are therefore consistent under the explicit
energy normalization change.

No value of kappa, c_g, particle mass or charge is selected. A photon shares
the cone only if it belongs to the connected scattering sector. Decoupled
sectors, nonlinear constraint closure, higher interactions, cosmology and
microscopic spin-2 formation remain outside this proof.

## 5. Exact normal-collision defect for a supplied lattice Dirac band

Take lattice spacing and hopping speed one and the positive dispersion

    E(p)=sqrt(m^2+sum_i sin(p_i)^2),  m>0.                (8)

It is the positive spectrum of H(p)=m beta+sum_i alpha_i sin(p_i), with
alpha_i=X tensor sigma_i and beta=Z tensor I. These four Hermitian matrices
anticommute and square to I. H is a bounded finite-range, four-orbital Bloch
Hamiltonian. It is a supplied band, not an assertion about an interacting
native spectrum.

An actual same-species normal elastic collision has incoming momenta
(k,0,0), (0,0,0), and outgoing (k/2,y,0), (k/2,-y,0). Set E_k=sqrt(m^2+sin(k)^2),
E_h=(E_k+m)/2 and choose

    sin(y)^2=E_h^2-m^2-sin(k/2)^2.                       (9)

For every sufficiently small nonzero k, the right-hand side is between zero
and one, since it is k^2/4+O(k^4). Thus the collision conserves energy and
unwrapped momentum exactly and exists arbitrarily close to the band minimum.
No numerical root-finding is needed to select y.

After the hard-graviton alignment of section 4, the Ward invariants would have f^0=kappa E+Q and spatial
f=(kappa+Q/E) sin(2p)/2. The outgoing-minus-incoming x component is

    Delta f_x=kappa A(k)+Q B(k),
    A(k)=sin(k)-sin(2k)/2,
    B(k)=sin(k)/E_h-sin(2k)/(2E_k).                      (10)

The temporal, y and z components vanish. For Q=0 this has the exact nonzero
factor A=sin(k)[1-cos(k)]. It is k^3/2+O(k^5), so it survives at each fixed
nonzero hard k when only the emitted graviton momentum tends to zero.

Nor can a conserved number-energy shift repair all these collisions:

    B(k)/A(k)=1/m+1/(2m^3)
              -[5/(8m^3)+1/(2m^5)]k^2+O(k^4).          (11)

The displayed nonzero coefficient proves this ratio is not constant on any
small open k interval. Consequently (10) cannot vanish for every such k
unless kappa=Q=0. This is an explicit same-band Ward inconsistency under
the stated pole and rich-scattering assumptions, not merely a Taylor fit or
an assumed failure of a preferred vertex. For Q=0 it also gives a controlled
IR residual that decreases cubically with hard momentum; an approximate IR
Ward identity is a live possibility.

For the supplied two-orbital Wilson symbol used in the earlier native matter
comparison, the same distinction is visible without any collision solver:

    h0(k)=sin kx sigma1+sin ky sigma2
             +(2+zeta-cos kx-cos ky-cos kz)sigma3,
    0<zeta<1, K=(0,0,acos zeta).

Along k=K+(0,q,0), the full matrix is sin(q)sigma2+[1-cos(q)]sigma3, so
its exact positive energy squared is 4sin(q/2)^2=q^2-q^4/12+O(q^6).
The linear node metric is exact as a derivative at the node; the quadratic
shell is not exact on a surrounding open patch. This restates the supplied
matrix directly and does not reuse an unmerged interacting theorem. The
prior native source constructions assert smooth-test-field consistency,
not the exact interacting soft Ward identity examined here.

## 6. Periodic analytic finite-band Hamiltonians cannot have an exact cone patch

Let H(p) be a finite-dimensional Hermitian matrix, periodic and real analytic
in every momentum, with a uniform bound on its norm. Finite-range Bloch
Hamiltonians satisfy these hypotheses. Suppose on a nonempty open patch it
has an eigenvalue

    E(p)=-mu+sigma sqrt(M^2+c^2 |p-K|^2),
    c>0, M^2>=0, sigma=+1 or -1.                           (12)

Choose a line through that patch with fixed transverse components giving a
strictly positive radicand for all real line coordinates x (possible in d>=2,
even when M=0). The function det[E(x) I-H(x)] is real analytic on the entire
real line, and vanishes on an interval. The identity theorem makes it vanish
for every real x. But |E(x)| becomes unbounded while the spectrum of H(x)
remains uniformly bounded, a contradiction. Eigenvalue crossings do not
stop this argument, since it uses the full characteristic determinant, not
analytic continuation of an isolated eigenvector.

This excludes an exactly relativistic open momentum patch of a bounded
analytic finite-orbital continuous-time free Bloch Hamiltonian. It does not
exclude asymptotically linear nodes, a continuum limit, interacting pole
energies with nonanalytic self-energies, infinitely many energy branches,
nonanalytic spatial couplings or Floquet quasienergies. In particular a
one-dimensional shift has an exactly linear locally unwrapped quasienergy;
the bounded-Hamiltonian argument cannot be transplanted to that problem.

Thus even an exact leading-soft identity restricted to an open hard-momentum
patch cannot be composed with an unchanged band of type (12). A successful
interacting lattice construction must show which premise changes. This is
an architecture/identification boundary and no qubit-lattice axiom update.

## 7. Higher-range derivatives give controlled approximate escapes

For integer range R>=1 define the antisymmetric central stencil

    d_R(x)=sum_(r=1..R) a_r sin(r x),
    a_r=2(-1)^(r+1)/r * (R!)^2/[(R-r)!(R+r)!].          (13)

Lagrange interpolation of the derivative at zero on nodes -R,...,R gives
sum_r a_r r=1 and sum_r a_r r^(2j+1)=0 for j=1,...,R-1. For an explicit
leading-error proof, apply the stencil to the node polynomial
x product_(r=1..R)(x^2-r^2), which vanishes at every node. Its linear
coefficient is (-1)^R(R!)^2. Therefore sum_r a_r r^(2R+1)=(-1)^(R+1)(R!)^2,
and the sine Taylor expansion gives

    d_R(x)=x-C_R x^(2R+1)+O(x^(2R+3)),
    C_R=(R!)^2/(2R+1)!,
    d_R(x)d_R'(x)=x-(2R+2)C_R x^(2R+1)+O(x^(2R+3)).      (14)

Replacing sin(p_i) in (8) by d_R(p_i) preserves finite-range Hermiticity
and moves the leading Q=0 Ward-current defect to order 2R+1. With lattice
spacing a use d_R(a p)/a: the defect is order a^(2R) p^(2R+1).
This improves a supplied approximate band; it does not produce an interacting
spin-2 completion or eliminate fermion doubling.

A uniform Taylor remainder is also available. Let A1=sum|a_r|r and
M_R=sum|a_r|r^(2R+1). The exact cancelled moments and ordinary sine/cosine
Taylor remainders imply, for real x,

    |d_R-x| <= M_R |x|^(2R+1)/(2R+1)!,
    |d_R'-1| <= M_R |x|^(2R)/(2R)!,
    |d_R d_R'-x| <= M_R[A1/(2R+1)!+1/(2R)!]|x|^(2R+1). (15)

For any exactly energy- and momentum-conserving collision, its Q=0 spatial
Ward residual is bounded by the sum of these per-leg errors. For R=1 the
sharper direct bound from |sin z-z|<=|z|^3/6 is

    ||Delta f|| <= (2/3)|kappa| c^2 a^2 sum_legs |p|^3.   (16)

Every fixed finite range still has a nonzero leading coefficient. An
asymptotic expansion with increasingly small errors is not an exact identity.

## 8. Umklapp and valley offsets require the actual reaction menu

The collision classification first applies on connected unwrapped momentum
domains with a rich normal elastic menu. For a further reaction j, define
R_js as the outgoing-minus-incoming multiplicity and G_j as its outgoing-
minus-incoming unwrapped total momentum. In a crystal G_j may be a reciprocal
lattice vector. The hard-graviton-aligned invariants require

    sum_s R_js Q_s=0,
    sum_s R_js K_s=G_j.                                  (17)

The second relation follows directly from sum eta f^i=kappa c^2
[sum eta p-sum eta K_s]. It would be wrong to require a separately conserved
valley-offset charge when the actual collision is Umklapp. Some intervalley
Umklapp processes conserve the shifted emergent momenta exactly.

For a finite specified reaction menu, offsets exist if and only if G lies
in the column space of its stoichiometric matrix R, coordinate by coordinate.
Equivalently, every left-null vector z of R must satisfy z^T G=0. This is an
exact finite linear-algebra consistency test, not a census of the physical
reaction amplitudes. A same-species Umklapp with R=0 and G!=0 immediately
fails. Conversely, pair conversion between valleys with K_+=pi/2 and
K_-=-pi/2 has R=(-2,2), G=-2pi and satisfies (17); that process alone is
not a common-cone obstruction. Two reactions with the same R but different
G provide a closed-menu obstruction which no offset can repair.

For a globally smooth periodic single band and invariant on its connected
covering domain, the collision form f=beta E+gamma.p+alpha is periodic only
if gamma=0. Applying this to the four soft invariants, or directly to the
periodicity of (6), gives an additional global-domain obstruction for a
nonzero propagating graviton. Disconnected valleys, nonsmooth band crossings,
missing self-Umklapp channels and a restricted low-energy menu require their
own domain analysis. Spohn's phonon collision-invariant theorem is relevant
prior art for the distinction between momentum and crystal momentum; its
more general measurable-function hypotheses are not silently imported here.

## 9. A Lieb-Robinson bound does not itself supply the soft Ward hypothesis

The locality argument in the cited spin-2 papers removes instantaneous
long-range kernels under a continuum field/source ansatz with precisely two
propagating gravitational polarizations. That is not automatically the same
premise as a bounded finite-range Hamiltonian on qubits.

Consider the nearest-neighbor spin-1/2 XY chain

    H=-J sum_x (S_x^+ S_(x+1)^-+S_x^- S_(x+1)^+), J>0.

The vacuum is stationary. A single excitation created at site zero evolves
with amplitude to site r given, on an infinite chain, by

    U_r0(t)=i^r J_r(2Jt),

where the Bessel identity follows by Fourier transforming the one-particle
symbol -2J cos k. More elementarily, for r>0 on an open chain long enough
to contain the path, the first nonzero matrix-power term is

    <r|exp(-itH)|0>=(iJt)^r/r!+O(t^(r+2)).                (18)

There is one shortest hopping path. The missing order r+1 follows from
bipartite parity. Hence for every finite r, sufficiently small t>0 gives a
nonzero occupation change at r when the source site is changed from vacuum
to one excitation. The Hamiltonian is bounded locally and strictly finite
range, yet it has no exactly vanishing finite-speed causal cone. This does
not contradict a Lieb-Robinson estimate, which bounds small tails.

There is a constructive continuum suppression: set J=c/(2a), r=R/a integer,
and deform the Fourier contour by i s with s>0. Then

    |U_r0(t)| <= exp[-s r+2Jt sinh s].                    (19)

For fixed physical R>ct>0, the optimum is cosh s=R/(ct), giving

    |U_r0(t)| <= exp{-[R arcosh(R/(ct))-sqrt(R^2-c^2t^2)]/a}. (20)

The bracket is strictly positive, so tails vanish in this continuum limit
while the finite-spacing model has nonzero arbitrarily early tails as proved
in (18). The bound does not make those tails identically zero. This example neither derives
gravity nor prohibits it. It shows why a lattice locality estimate alone
cannot be used as a proof of the exact continuum soft-gauge premise in (2).
Actual source constraints, polarizations, scattering residues and their
limit must be constructed. No stronger microscopic axiom is added here.

## 10. A dynamical preferred frame changes the Ward identity

A concrete prior-art escape is Einstein-aether theory, not a claim that a
preferred vector is selected by the framework. The supplied local action is

    S=-(16 pi G)^-1 int sqrt(-g) [R+K^(ab)_(mn) nabla_a u^m nabla_b u^n]
         + int sqrt(-g) lambda(g_ab u^a u^b-1),
    K^(ab)_(mn)=c1 g^ab g_mn+c2 delta_a^m delta_b^n
                    +c3 delta_a^n delta_b^m+c4 u^a u^b g_mn.       (21)

Use signature +---, G>0 and a flat background with constant u=(1,0,0,0).
Ordinary minimally metric-coupled matter has limiting speed one. The action
and linear modes are established prior art (Jacobson, 0801.1547v2, sections
1 and 4). The following reproduces the relevant quadratic reduction rather
than treating a mode-speed table as independently verified evidence.

Set g=eta+h, u=ubar+v, so v^0=-h00/2. For one Fourier direction d=(omega,0,0,k),
let D_a^m=d_a v^m+Gamma^m_(a0), where

    Gamma^m_(a0)=eta^(mn)(d_a h_n0+omega h_na-d_n h_a0)/2.

The two quadratic pieces, omitting their common positive overall constant,
are the standard expanded Einstein action

    L_EH=[d^2(h_mn h^mn-h^2)-2(d_m h^mn)(d^l h_ln)
                         +2(d_m h^mn)d_n h]/4,

and directly -K^(ab)_(mn) D_a^m D_b^n with the background K. Products here
are Fourier bilinear symbols; the real sine/cosine average supplies the
same common factor in both pieces. No dispersion sign is read from an
unpaired complex plane-wave square.

For tensor polarization h11=-h22=t, all other fields zero, the result is

    L_T=[(1-c13)omega^2-k^2]t^2/2,   c13=c1+c3.           (22)

For one vector polarization take h13=h31=h and v1=v, with h0i=0. The result
before eliminating the metric component at nonzero frequency is

    L_V=(1-c13)omega^2 h^2/2+c14 omega^2 v^2-c1 k^2 v^2
                           +c13 omega k h v,            (23)
    c14=c1+c4.

At nonzero omega, solve h=-c13 k v/[(1-c13)omega]. Substitution gives

    L_V,red=[c14 omega^2
               -(2c1-c1^2+c3^2)k^2/(2(1-c13))]v^2.      (24)

For scalar polarization h00=n, h11=h22=s, h33=l, v3=0 and h0i=0, the
unreduced expression is

    L_S=-(omega^2/2)s^2-omega^2 s l+(k^2/2)s^2-k^2 n s
        +c14 k^2 n^2/4-c13 omega^2(2s^2+l^2)/4
                         -c2 omega^2(2s+l)^2/4.         (25)

For nonzero k,omega, eliminating n=2s/c14 and
l=-2(1+c2)s/c123, c123=c1+c2+c3, gives

    L_S,red=[(1-c13)(2+c13+3c2)omega^2/(2c123)
                         -(2-c14)k^2/(2c14)]s^2.        (26)

The reductions require nonzero c14, c123 and 1-c13, in addition to the
stated k,omega conditions. Reading a scalar speed also requires
2+c13+3c2!=0. The tensor, vector and scalar dispersion formulas are

    c_T^2=1/(1-c13),
    c_V^2=(2c1-c1^2+c3^2)/(2c14(1-c13)),
    c_S^2=c123(2-c14)/[c14(1-c13)(2+c13+3c2)].           (27)

For the explicit mathematical example c1=c2=1/10, c3=c4=0, all three reduced
kinetic and gradient coefficients are positive. The squared speeds are
10/9, 19/18 and 95/54, while minimally coupled matter has speed squared one.
For this parameter example the complete unfixed 13-field quadratic Hessian
has four exact gauge null directions. The check verifies every unreduced
representative tensor, vector and scalar equation and the positive pole
weights 9/10, 1/5 and 54/5. At k=1, the gauge section h03=h13=h23=h33=0
has determinant

    -(9 omega^2-10)^2(18 omega^2-19)^2(54 omega^2-95)/10^9.

The gauge choice is valid for k!=0. This exact determinant supplies the full
two-tensor/two-vector/one-scalar finite-frequency mode census for this
example; a discarded constraint equation has not been ignored. The general
parameter formulas above and this specific full-equation check have distinct
scopes. This is a positive quadratic, local generally covariant alternative;
no ultraviolet quantum completion, nonlinear global stability, empirical
fit, or native qubit realization is asserted.

The precise Ward escape is visible before solving any modes. Around the
constant-vector background an infinitesimal coordinate transformation acts as

    delta h_mn=partial_m xi_n+partial_n xi_m,
    delta v^m=-partial_0 xi^m.                            (28)

It preserves the linear unit constraint and gives delta D=0. For a linear
source coupling h_mn T^mn/2+v^m J_m, source invariance requires the mixed
identity

    q_m T^mn-q_0 J^n=0,                                 (29)

with the corresponding index-raising convention. Setting the aether source
term to zero is a new assumption, not a legitimate consequence of the two
TT polarizations. A metric-only gauge change at fixed v is not a gauge
transformation of this background. Accordingly the closed metric-only soft
identity (2) need not hold, and the theorem does not require the different
mode cones in (27) to coincide. A medium or another transforming order
parameter must likewise be included in the actual soft-source analysis.
