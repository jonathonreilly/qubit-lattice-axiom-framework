# Exact plane-symmetry selection rule for fixed local features

The proposed rule is correct as a statement about two-point functions and linear response in a state invariant under the relevant plane symmetries. Stationarity alone, or membership in a commuting CSS sector, is insufficient.

## Symmetry and local charge

For H=−J sum_(x,a) sigma_x^a sigma_(x+ea)^a, define the plane operation P_(a,k) as the product of sigma^a on sites with x_a=k. A bond along a commutes with it even when only one endpoint meets the plane, since its Pauli type is a. Every other-direction bond has zero or two endpoints in that plane and therefore also commutes. Thus [H,P_(a,k)]=0 on the ordinary finite open or periodic compass graph.

On an infinite lattice the infinite product need not be a Hilbert-space operator. The appropriate formulation is its conjugation automorphism alpha_(a,k) acting on finite-support observables; this is well-defined and commutes with the local Hamiltonian dynamics. All conclusions below can be expressed in terms of these automorphisms and an invariant state.

For a finite Pauli string F, write

alpha_(a,k)(F)=(−1)^s_(a,k)(F) F,

where s counts modulo two the sites in that plane carrying a Pauli type different from a. Identity factors contribute zero. A finite string has only finitely many nonzero syndrome entries. F dagger has the same syndrome.

## Exact correlation selection

Assume rho is invariant under each plane operation invoked: P rho P=rho, or omega(alpha(A))=omega(A) in infinite volume. Since alpha commutes with time evolution, F(t) has the same syndrome as F. Applying a symmetry to an expectation gives

<F_r(t) F_0 dagger> = (−1)^[s_(a,k)(F_r)+s_(a,k)(F_0)] <F_r(t) F_0 dagger>.

If any syndrome differs, the expectation is exactly zero. The same proof applies to the reverse ordering, the commutator, symmetrized correlation, connected correlation, and retarded linear response. Stationarity is useful for time-difference spectral interpretation but is not needed for this basic cancellation if the state is invariant and the symmetry is preserved by dynamics.

The different plane operators may anticommute as Hilbert-space operators; this does not invalidate applying each conjugation separately. No simultaneous eigenbasis for all plane operators is assumed.

## Single-site Pauli rule

For F=sigma_x^b, the syndrome is one on plane (a,x_a) for each a different from b, and zero for a=b. Hence a correlator or response between sigma_x^b and sigma_y^b can be nonzero only if

x_a=y_a for both transverse axes a different from b.

Thus the support of this particular two-point channel is confined to the b-axis line. This is a necessary condition, not proof of propagation or any particular dispersion along that line.

## Rigid translations of a finite feature

Let S_a={k:s_(a,k)(F)=1}. Under translation r, the syndrome support becomes S_a+r_a. If S_a is a finite nonempty subset of the integers, equality S_a+r_a=S_a implies r_a=0, for example by comparing minima. Therefore a fixed finite feature charged under any a-plane symmetry has a zero translated-feature two-point function whenever its translation has a nonzero a component. If it has nonempty syndromes in multiple axis families, the restrictions combine.

This rules out unrestricted three-dimensional two-point propagation of a rigidly translated, fixed plane-charged feature in the invariant state. It is not a theorem that all information, energy, probabilities, or composite excitations are immobile. Neutral features, changes of operator dressing, and other observables require their own analysis. Nor is it an argument against a neutral scalar channel: each native energy bond and the central C distance-two same-axis pair are plane-neutral, so this selection rule does not restrict their spatial two-point support.

Here “neutral” means neutral under these discrete plane symmetries, not electromagnetic neutrality or a derived physical particle assignment.

## State and geometry qualifications

* Finite-temperature Gibbs density matrices and the normalized full ground-space projector are invariant because they are functions of H. Group-averaging a stationary density matrix also preserves stationarity and makes it invariant under the finite symmetry group.
* A selected pure ground state or excited eigenstate is not automatically invariant. In particular, on an odd 3x3x3 cube an X plane and a Z plane intersect on three sites and anticommute. No pure state can be invariant under both conjugations, since that would make it a simultaneous eigenvector of anticommuting operators. The chosen all-plus CSS sector uses commuting plane products, not all individual planes, and cannot silently supply the full invariance premise. Its available stabilizers can still yield weaker selection rules that must be derived separately.
* In the thermodynamic limit, symmetry-preserving Gibbs limits retain the rule, while symmetry-broken extremal states need not. A symmetric mixture and a symmetry-broken preparation are distinct physical assumptions.
* On a finite periodic lattice, a syndrome set can have a nontrivial cyclic translation stabilizer, so the infinite-line finite-set argument must not be transferred without checking wraparound. On a finite open graph, coordinate comparisons remain meaningful for features whose translated supports stay inside, but translation invariance of the state is not automatic. The cancellation itself only uses the plane symmetry, not spatial translation invariance.
* Ordinary open boundaries preserve the stated complete-plane compass symmetries. Modified boundary fields, extra couplings, truncated plane definitions, or preparation that breaks the symmetries can remove the premise; “boundary” alone is not sufficient reason to dismiss or assert the rule.

This is an exact symmetry selection statement for the supplied microscopic Hamiltonian and specified state class. It does not derive the physical state, a scalar pole, or a source/detector connection to a cosmological field.

## Constructive classification: complete Pauli centralizer of the bond set

The proposed open-rectangle classification is correct. Work over F2 and ignore overall Pauli phases. Write a string as binary fields (u,v), where u marks X support and v marks Z support, with Y represented by u=v=1.

Commutation with every x-directed XX bond imposes v(x,y,z)=v(x+1,y,z), so v=v(y,z). Commutation with every z-directed ZZ bond imposes u(x,y,z)=u(x,y,z+1), so u=u(x,y). Commutation with every y-directed YY bond imposes

u(x,y)+v(y,z)=u(x,y+1)+v(y+1,z).

Fix a reference y0. Then u(x,y)+u(x,y0)=v(y,z)+v(y0,z). The left side cannot depend on z, the right side cannot depend on x, and equality for all x,z forces this common value to depend only on y. Call it B(y), with B(y0)=0 in this gauge. Define A(x)=u(x,y0) and C(z)=v(y0,z). Every solution therefore has

u(x,y,z)=A(x)+B(y),
v(x,y,z)=C(z)+B(y).

Conversely these fields satisfy every bond constraint. Without fixing B(y0), the simultaneous shift A->A+1, B->B+1, C->C+1 leaves both u and v unchanged and is the sole parameter redundancy. Hence the solution dimension is Lx+Ly+Lz−1.

These are exactly products of X planes at fixed x, Y planes at fixed y, and Z planes at fixed z. There is one binary relation: the product of all planes of all three types is identity up to an overall phase. Actual phases can be chosen afterward; the dimension count refers to the Pauli-vector space, not a commuting-stabilizer rank. In particular the full plane group can be nonabelian up to phase.

Let B denote the F2 span of native bond Pauli vectors and P the span of all plane vectors. The argument proves B^perp=P under the nondegenerate Pauli symplectic form. Taking the double orthogonal yields

B=P^perp.

Therefore every Pauli string commuting with all plane generators is a product of existing native bond Paulis, up to phase. The native-bond rank is 2N−(Lx+Ly+Lz−1). This is valid for the full rectangular open grid with all dimensions at least two and the specified complete bond set; deleted bonds, holes or altered connectivity require a fresh classification.

Independent exact binary elimination on several rectangles confirms both ranks and all bond-plane pairings:

| Shape | N | Plane rank | Bond rank |
|---|---:|---:|---:|
| 2x2x2 | 8 | 5 | 11 |
| 3x3x3 | 27 | 8 | 46 |
| 2x3x4 | 24 | 8 | 40 |
| 3x4x5 | 60 | 11 | 109 |

This establishes generation in the associative Pauli operator algebra: products are allowed and may require a phase ±1 or ±i to recover a chosen Hermitian representative. It does NOT establish that every neutral string is a term in H, is generated by repeated commutators with H from a chosen initial operator, has an appreciable matrix element in a selected state, or is a propagating collective mode. The commutant of the whole Hamiltonian among arbitrary linear combinations of operators is a different and generally larger object than the Pauli strings commuting with every individual bond. Algebraic generation supplies a constructive search space for neutral features without adding microscopic Hamiltonian terms; dynamics and state selection remain separate work.
