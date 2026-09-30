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

