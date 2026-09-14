# Soft spin-2 collision invariants, common cones and lattice Ward boundaries

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author-proposed conditional mathematics; actual source status conditional-support.
Independent scientific review is pending. This is not a native gravity existence
proof, an empirical prediction or an axiom-forcing result.

Under the explicit collision, external-pole and closed metric Ward hypotheses
below, a self-coupled infrared graviton forces one quadratic cone for every
connected matter species, allowing conserved energy shifts and valley offsets.
The proof needs no continuous rotational symmetry of the hard matter bands.
An explicit finite-lattice collision, an analytic finite-band argument and an
Umklapp compatibility test delimit the exact claim. Constructive higher-range
approximations and a fully reconstructed Einstein-aether quadratic example
show why those boundaries do not exclude emergent approximate relativity.

Hertzberg–Sandora 1704.05071v2 supplies the prior soft-graviton universality
argument. No novelty claim is made for the equivalence principle or its
relativistic-dispersion conclusion. The review object is the explicit
collision/pole proof with affine offsets, its precise applicability to the
supplied native-band comparisons, and the checked surviving alternatives.

**Runner:** [self-contained primary](../scripts/soft_spin2_collision_invariants_common_cones_and_lattice_ward_boundaries_2026_09_14.py).
**Receipt:** [canonical cache](../logs/runner-cache/soft_spin2_collision_invariants_common_cones_and_lattice_ward_boundaries_2026_09_14.txt).
**Review:** [author record](../.claude/science/physics-loops/toe-charged-phase-20260914/deliveries/block8/REVIEW_HISTORY.md).

## Premises, obligations and imports

| Supplied premise or object | Proven consequence | Boundary or open obligation |
|---|---|---|
| C2 bands, C1 invariants, rich normal elastic collisions, noncollinear velocity images and connected species graph | Collision invariants are common energy/momentum combinations plus reaction charges | Actual amplitudes and domain coverage must be established in a native interacting theory |
| Real symmetric diagonal residues, simple poles, separated real pole vectors, all four metric gauge parameters and leading external-pole saturation | Each residue factors as g times zeta tensor zeta | Unresolved matrix residues, additional transforming fields and infrared dressing require their own analysis |
| Above premises plus nonzero hard-graviton coupling and isotropic linear infrared graviton | Exact common quadratic shell with species energy and valley shifts | No mass, coupling, cone value, clock normalization or nonlinear Einstein dynamics selected |
| Supplied finite-orbital Dirac/Wilson bands and a rich compatible scattering menu | Concrete exact collision defect and finite-band analytic obstruction | Interacting dispersions and approximate/continuum Ward identities are different obligations |
| Finite reaction stoichiometry and unwrapped reciprocal transfers | Exact criterion R K=G, including a successful intervalley Umklapp example | Physical reaction amplitudes are not supplied by a stoichiometric list |
| Central finite stencils and a finite-range XY spin chain | Controlled current errors and nonzero early tails with continuum suppression | Neither construction supplies a gravitational phase |
| Einstein-aether action and stated stable quadratic parameter example | Direct tensor/vector/scalar reduction, full gauge/constraint check and mixed source identity | No empirical fit, ultraviolet completion or native preferred-vector selection |

Every model Hamiltonian, scattering condition, source convention, field content
and background used here is supplied data. The ordinary implicit-function,
polynomial-identity and real-analytic identity theorems are mathematical
machinery whose relevant hypotheses are stated in the proofs. Literature is
prior art or an explicitly reconstructed comparator; no observed target value
is fitted or silently used as a selector. The collision-to-cone obligation
graph is proved in sections 1–4. Sections 5–10 independently test its domain
and escapes. No unmerged science conclusion is an input to the runner.

The strongest missing native lemma is a controlled interacting qubit-lattice
phase with the required spin-2 polarizations, source identity and scattering
residues, including self-coupling and the actual reaction menu. That lemma is
substantial physics, not a small remainder or a restatement supplied as proof.
The minimal axioms and admissibility context are checked against current main
`b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf`. The current TT comparison
`ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md`
supplies a scoped covariance construction, not the missing scattering theorem.
The Wilson symbol and smooth-source comparisons from PRs 8099 and 8095 are
restated directly where used; exact heads and reading limits are in the ledger.

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
epsilon_s=0, dividing the rank-one numerator by its pole denominator cancels
the original E_s/epsilon_s normalization, leaving the usual common-metric soft factor. The residue and
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

After the hard-graviton alignment of section 4, the Ward invariants would
have f^0=kappa E+Q and spatial
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
in (18). The bound does not make those tails identically zero. This example
neither derives gravity nor prohibits it. It shows why a lattice locality estimate alone
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

The gauge choice is valid for k!=0: the variations of (h03,h13,h23,h33)
with respect to (xi0,xi1,xi2,xi3) form a triangular matrix with diagonal
(k,-k,-k,-2k), hence determinant -2k^4. The action determinant above supplies the full
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

## Proof and falsification coverage

| Argument | Different calculation path used to challenge it | Generality limit |
|---|---|---|
| Collision gradient and common-shell proofs | Finite gradient-constraint ranks in dimensions 2,3,4; symbolic anisotropic and shifted shell derivatives | Finite rank samples are falsifiers; noncollinear-anchor proof supplies the quantified result |
| Complex-null pole separation | Exact rational kernels with modular lower-rank certificates for massive and null four-leg collisions; independent numerical singular values | General separated-pole result rests on the divisor-spanning proof |
| Exact sine-band collision and charge-shift failure | Full four-component Dirac spectrum and projector velocities; symbolic nonconstant B/A coefficient | Supplied positive free bands, m>0 and explicit collision family |
| Analytic finite-band and valley compatibility | Full characteristic determinant, actual two-component Wilson eigenvalues, stoichiometric nullspace and inconsistent menu | Identity theorem gives open-patch statement; no general interacting spectrum theorem |
| Improved derivatives | Exact stencil moments plus symbolic current series and direct remainder evaluations | Family proof covers finite R; numerical instances R=1,...,5 |
| Lattice causal tails | Full seven-qubit evolution, separate one-particle evolution, exact shortest paths, Fourier sum versus Bessel function | All-distance early-time result follows from the shortest-path proof; continuum bound is analytic |
| Preferred-frame escape | Direct action Hessian, four exact gauge nulls, unreduced mode equations, positive pole weights and gauge-section determinant | Full finite-frequency census at c1=c2=1/10,c3=c4=0; no nonlinear stability theorem |

## No-Go Discipline Gate

### N1 — materially distinct routes

All entries are ATTEMPTED in this unit. Successful escapes are retained as such;
there is no claim that every route fails or that the available routes are exhaustive.

| Route | Attempt and result | Evidence |
|---|---|---|
| Collision geometry | Derive invariants from an actual rich collision manifold instead of assuming a conservation list; succeeds under noncollinearity, fails to classify sparse/collinear menus | ATTEMPTED; section 1 anchor proof and gradient-rank checks |
| Analytic finite-band continuation | Preserve an exactly quadratic cone on an open free-band patch; impossible for bounded globally analytic finite matrices | ATTEMPTED; section 6 determinant identity and reconstructed Dirac characteristic polynomial |
| Higher-range approximation | Improve a finite-range derivative while keeping a supplied band; succeeds with explicitly bounded power-law Ward residual, which remains nonzero at finite range | ATTEMPTED; section 7 interpolation/remainder proof and five ranges |
| Reaction and valley identification | Absorb reciprocal momentum transfers into node offsets; succeeds exactly iff the finite menu obeys R K=G, including a consistent Umklapp example | ATTEMPTED; section 8 left-nullspace criterion and both menus |
| Lattice causal limit | Use finite-range microscopic locality to obtain an exactly sharp cone immediately; XY amplitudes give a counterexample, while an explicit continuum tail bound succeeds | ATTEMPTED; section 9 full-spin evolution, path and contour arguments |
| Transforming preferred frame | Preserve a gapless tensor with different mode cones by changing the actual gauge/source content; a positive quadratic Einstein-aether example succeeds | ATTEMPTED; section 10 direct full Hessian and mixed Ward derivation |

### N2 — pairwise relation and collapse

The diagnoses are: exact unchanged finite-band compatibility; reaction-menu
compatibility; inference from lattice locality; and omitted transforming-source
content. They are not four independent axiom walls.

| Pair | Dependence and disposition |
|---|---|
| Finite band / reaction menu | Both may invalidate an exact soft completion, but a normal collision already witnesses the former without Umklapp; a menu constraint can occur for ideal cone valleys. Keep distinct tests. |
| Finite band / locality inference | The analytic spectrum theorem uses a free finite matrix; the XY tail witness concerns causal support of a local many-qubit system. Neither supplies the other's hypothesis. |
| Finite band / transforming source | An extra transforming source changes the closed Ward premise before the finite-band consequence follows. Treat it as an escape, not an additional wall. |
| Reaction menu / locality inference | Stoichiometric offsets and early-time tails concern different objects. Locality alone supplies neither the amplitude menu nor its charges. |
| Reaction menu / transforming source | Additional sources can change the invariant being conserved. The R K=G test applies only after the metric-only common-cone premises survive. |
| Locality inference / transforming source | Both attack the inference that a tensor mode plus microscopic locality already supplies the closed metric Ward identity. Collapse that overbroad inference into one unproved physical-identification step. |

The explicit sine collision and analytic finite-band continuation are two
witnesses of one exact free-band compatibility boundary, not two counted walls.
The claimed result is a conditional theorem and architectural tests, with zero
claimed axiom-forcing conclusions.

### N3 — hidden conditions

The proof's assumed collision richness, self-scattering, connected domains,
velocity noncollinearity, pole simplicity, C1 real diagonal residues, separated
velocities, leading-pole saturation and all four metric gauge parameters are
explicit premises. Hard-graviton participation and its isotropic infrared law
are additional conditions in section 4. Periodicity, boundedness, finite matrix
dimension and global real analyticity belong only to section 6. Gauge reduction
divisors and the preferred-vector background belong only to section 10. The
standard expanded Einstein quadratic action is supplied comparator machinery
and checked directly against gauge nulls; it is not derived from the axioms.
No use of “native,” “background,” “standard” or “by construction” promotes these
conditions into retained framework premises.

### N4 — source/witness matching

| Citation or internal witness | Residual actually addressed | Closure claimed | Match |
|---|---|---|---|
| Hertzberg–Sandora 1704.05071v2, all six pages | Prior soft-graviton dispersion/universality argument | Prior art and comparison only; our conditional steps are written here | yes |
| Hertzberg–Litterer–Sandora 2005.01744v2, main pages 1–10 | Restricted local continuum exchange/source conditions | Context for distinguishing a source Ward law from a lattice locality bound | yes |
| Spohn math-ph/0605069v1, all four pages | Periodic phonon collision invariants | Prior art for the normal/Umklapp distinction; no imported measurable theorem | yes |
| Jacobson 0801.1547v2, action pages 2–3 and mode pages 5–6 | Einstein-aether action, mode speeds and energy conditions | Supplied comparator reconstructed in section 10; no native or empirical claim | yes |
| Sections 1–4 (this source:62) and primary collision/pole/shell families | Explicit conditional common-shell chain | Quantified implication under its full stated premises | yes |
| Sections 5–8 (this source:272) and primary band/stencil/menu families | Unchanged free-band exactness and approximate/offset escapes | Stated finite-band theorem, explicit collisions and linear menu test | yes |
| Sections 9–10 (this source:444) and primary spin-chain/action families | Overbroad inference from local tensor behavior to one closed source identity | Concrete counterexamples to that inference, with their field/domain scope | yes |

The reading ledger records exact PDF hashes and repository revisions. These
witnesses are not used to claim any wider framework wall or a selected vacuum.

### N5 — resolution and rhetoric

Per element, symbolic residue, matrix, polynomial and stencil identities are
checked. Per site, the complete seven-qubit XY Hamiltonian is constructed.
Per mode, actual Dirac/Wilson bands and the unfixed aether Hessian are examined.
Per block, exact four-leg collisions, finite reaction menus and full gauge-
section determinants are checked. Lattice-wide family claims come only from
the stated proofs; no infinite-volume interacting gravity phase is simulated
or established. Finite examples do not prove full lattice universality.

### N6 — constructive partial closure

Energy and valley shifts can change the identification of generators by
conserved charges; section 8 explicitly preserves consistent Umklapp. Increasing
stencil range or taking a controlled continuum limit can reduce the displayed
residuals. A transforming medium changes the relevant Ward identity. These are
live mathematical alternatives within supplied constructions. They do not
require an axiom update, and no absence of an approved primitive is asserted.
The minimal-axiom scope and current native-band/source comparisons remain the
context; this note changes no primitive, axiom, interpretation stance or prompt.

### N7 — strongest surviving alternative

A hostile reviewer should insist that the actual emergent excitations need
not keep the bare finite-band spectrum: interactions can reorganize poles,
continuum limits can remove irrelevant lattice errors, and extra gapless order
parameters can enter the source law. The explicit improved stencils, continuum
XY bound and positive Einstein-aether quadratic example support this objection.
It is convincing against any universal lattice or axiom no-go, so that broader
claim is rejected here. The remaining native task is to construct the actual
phase and its complete source/soft limit, not to assume that it retains the
bare band or has only a metric source.

### N8 — cross-cycle echo and marginal value

The current main TT covariance note already warns that its finite construction
is not physical spin-2 closure. Unmerged PR 8095 gives conditional smooth-source
consistency and PR 8099 computes node derivative metrics; neither claims the
interacting exact Ward law. This unit tests that missing bridge directly.
Earlier campaign common-metric logarithms and compact tensor Hamiltonians
address different mechanisms, and are not imported to close it. Approximation
and added source fields are considered explicitly here; no prior retired wall
is relabelled as a fresh universal obstruction. The new reviewable obligation
is the collision/pole/common-shell chain and its exact lattice application,
not another fitted cone or numerical match.

## Sources and reproduction

Primary sources are [Hertzberg and Sandora](https://arxiv.org/abs/1704.05071v2),
[Hertzberg, Litterer and Sandora](https://arxiv.org/abs/2005.01744v2),
[Spohn](https://arxiv.org/abs/math-ph/0605069v1) and
[Jacobson](https://arxiv.org/abs/0801.1547v2). The committed reading ledger records
which pages and exact source revisions were read. The aether paper's remaining
phenomenology, the locality paper's appendices and historical repository
runners are not claimed as fully rederived or replayed evidence.

Run the paired primary with Python 3, NumPy, SciPy, SymPy and mpmath. It reads
no scientific files and contains all model definitions. General mathematics is
proved above; eight check families supply bounded falsifiers through different
representations. Canonical execution uses the declared 90-second envelope and
records source hash, stdout, stderr and elapsed runtime. Load-bearing mutations
and their full source/output receipts are preserved in the author packet.

## Review record

The author cold-read the complete proof and primary, clarified the real
residue convention, null-hard-pole separation, conserved valley offsets,
nonzero gauge-reduction divisors and scope of the full aether mode census.
The source-contraction check compares an expanded zero difference; an earlier
expanded-versus-factored symbolic equality was a test-form issue, preserved in
the campaign history and corrected before the canonical run. These are author
checks, not independent scientific review.

Focused syntax, cache/hash, local-link, vocabulary, whitespace, N5 and mutation
checks are recorded in the packet. The citation manifest is regenerated by its
owning tools. Full pipeline, strict global lint and combined changed-evidence
validation remain deferred under conformance section 12 to the exact integrated
current-main candidate; they are not reported as passed. There is no author
main merge, scientific audit verdict or effective-retention update.

## Claim-status certificate

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Construct a native interacting spin-2 phase with the complete source identity and actual matter/graviton scattering residues.
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: Independently check collision and pole separation; construct or falsify the complete source Ward law in an explicit native phase.
conditional_surface_status: Supplied scattering, diagonal poles, source identity and model Hamiltonians; exact conditional implications with native existence open.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Explicit conditional common-cone proof and scoped lattice/medium compatibility tests; no universal lattice or axiom no-go.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
