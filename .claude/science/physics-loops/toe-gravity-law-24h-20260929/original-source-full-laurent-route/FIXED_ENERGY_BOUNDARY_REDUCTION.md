# Generic mixed protected modes reduce to fixed Dirichlet energies

A separate analytical continuation, with the exact residual rows retained. This is not full protected-union observability. Keep the supplied actual rotor H2, fixed finite physical W=1 sector and B charge pattern chi. Use L divisible by four and L>=12 for the forest-dependent final matrix reduction. The disjoint-edge spectral argument itself only needs the previously established protected-column identity and one-polarity exclusion. No enumeration or new numerical result is used.

## 1. Actual disjoint edge parameters

Write P=P_++P_- for the protected union at this chi, and

    E_sigma=P_sigma H P_sigma,
    F_sigma=(I-P) H P_sigma.                             (1)

There is no P_+ H P_- term: a protected output of a protected input retains its polarity on the shared B. The complete protected-column formula uses a single shared B of charge sigma, with coefficient exp(i sigma(A_hb-A_ab)), or the sum of the two such paths for a diagonal displacement. The only same-hole term is 6. All negative same-hole terms are blocked, and the canceled distant terms have already been removed in the actual H identity.

In an edge-connection representation, E_+ therefore depends ONLY on the variables u_e=exp(i A_e) on edges incident to B+ sites. E_- depends ONLY on v_e=exp(i A_e) on edges incident to B- sites (with inverse powers from the negative charge). These are disjoint sets of ACTUAL physical edges. B-vacancy edges occur in neither protected block. Different completed A backgrounds produce finite direct sums but do not introduce any other edge variables.

This representation is legitimate despite Gauss gauge redundancy. Starting from any fixed Gauss field section, conjugate matter coordinates by its connection phases. Actual field shifts then have the displayed exp(i A dot Delta E) coefficients. A vertex gauge change is a diagonal matter-basis conjugation preserving P_sigma and hence preserving the spectra in (1). We use redundant independent edge-connection parameters, not independent configuration-path weights. Any gauge-invariant almost-everywhere conclusion can subsequently be pushed down to the physical cycle torus.

## 2. A specialization lemma with disjoint variables

Let p_+(t;u)=det(t-E_+(u)) and p_-(t;v)=det(t-E_-(v)). They are finite monic polynomials in t with Laurent-polynomial coefficients. Define

    Lambda_sigma={c in C: p_sigma(c;variables) is identically zero}.
                                                               (2)

Each Lambda_sigma is finite: it is contained in the root set after any one specialization. Such constants are real and in [0,36], since E_sigma is a direct sum of principal K_sigma* K_sigma blocks on the physical torus. No emptiness of this set is assumed.

For two monic polynomial families in disjoint variable sets, outside a proper algebraic subset of (u,v), every common root lies in

    Lambda=Lambda_+ intersection Lambda_-.               (3)

Here is an elementary proof, without an independent-random-spectrum assumption. Remove from EACH polynomial all of its fixed factors (t-c) belonging to c in Lambda, with their maximal constant multiplicity in that polynomial. Call the results q_+,q_-. Their sets of constant roots are disjoint. Choose u_0 so that q_+(c;u_0)!=0 for every constant root c of q_-. This is possible because each of those finitely many evaluation polynomials is nonzero. The specialized q_+(t;u_0) has finitely many roots r. None is a constant root of q_-, so every q_-(r;v) is a nonzero Laurent polynomial. Choose v_0 outside the union of their zero sets. Then q_+(t;u_0) and q_-(t;v_0) have no common root.

Their resultant is consequently a NONZERO Laurent polynomial in (u,v). Away from its zero set the original common roots can only be the removed constants in (3). The witness may be chosen in the complex parameter torus; nonzeroness implies that the resultant cannot vanish identically on the physical unit torus. Its zero set there has Haar measure zero. Constant polynomials and an absent polarity are handled trivially.

Apply this lemma to (1). The property of having a common eigenvalue outside Lambda is gauge invariant, even if the displayed resultant changes its representation. Its edge-Haar null set therefore descends to a null set of physical cycle phases: Haar measure pushes forward under the edge-to-cycle quotient, and the inverse image of this invariant bad set is precisely the redundant-gauge bad set. No independent cycle assignment for different many-body paths is used.

## 3. Consequence for actual protected-union eigenvectors

The checked one-polarity theorem removes, on a common full-measure phase set, every eigenvector wholly in P_+ or wholly in P_-. A union-supported eigenvector must therefore have both components nonzero. Projecting its true H equation onto P_sigma gives

    E_sigma u_sigma=lambda u_sigma.                     (4)

Combining (3)-(4), at almost every physical phase its energy MUST belong to the finite, phase-independent set Lambda for this chi. There are finitely many chi at fixed volume/count, so the same assertion holds with the finite union of these sets and a finite union of exceptional phase sets.

This is a necessary generic fixed-energy restriction, not the exclusion of the surviving energies. In particular disjoint parameter dependence does not justify saying that the two spectra are generically disjoint; their constant Dirichlet eigenvalues can coincide, as the physical construction below demonstrates.

Using the frozen forest isometry R(theta), the remaining question now has the exact first-order form, for each c in Lambda,

    D_c(theta)=(H(theta)-c)R(theta),
    D_c(theta) z=0.                                     (5)

A nonzero maximal Laurent minor for EVERY c in Lambda would give generic protected-union exclusion. An identically deficient D_c supplies a generic protected mode at that constant energy. Equation (5) retains all protected spectral rows and all outgoing rows; it does not test only the mixed rows. Its columns are one per mixed tree. This reduces the former unknown-energy/Krylov criterion to finitely many fixed-energy Laurent rank questions. Those minors have NOT been proved nonzero here.

## 4. A genuine boundary-phase family at a surviving energy

Fix the base connection. Let a be an A site whose FULL B star contains both signs. Such a site cannot be a protected input hole. Change A_ab by phi_a on its incident B+ edges only, leaving its B- edges unchanged. Protected plus paths ending at hole a acquire exp(-i phi_a); protected minus paths do not change. There is no protected input at a to contribute the other endpoint factor. Therefore E_+ and E_- remain exactly unchanged. At other hole rows the coefficients are unchanged.

These are actual partial changes of the edge connection. Different matter rows at the SAME a receive the SAME phase. The parameters are not independent configuration-row weights, and combinations may be gauge redundant. Their action is nevertheless the exact stated physical family; no dimension of an independent parameter quotient is assumed.

Let X be the complete mixed-row selector and let C_sigma=(I-P-X)H P_sigma. At fixed c define the fixed spaces

    V_sigma(c)=ker(E_sigma-c) intersection ker C_sigma.  (6)

The kernels in (6) are unchanged by these boundary phases, since C_+ rows are merely multiplied by nonzero factors and C_- is unchanged. All that remains of the eigen equation on V_+ plus V_- is

    Z(phi) X F_+ u_+ + X F_- u_- =0,                    (7)

where Z repeats exp(-i phi_a) on every actual mixed row with hole a. At a generic base phase the maps X F_sigma restricted to V_sigma are injective: a vector in their kernel would be a forbidden one-polarity eigenvector. But injectivity separately does NOT prove that their two image spaces have trivial intersection after the correlated diagonal action Z. In particular a common value of all phi_a is absorbed by rescaling u_+; it cannot remove an intersection. Any usable phase-transversality proof must respect these repeated blocks and ineffective directions.

Thus (7) gives a precise residual boundary-space question at fixed energies, with full charge/configuration multiplicities and the real gauge correlations retained. A random-phase or generic-transversality assertion needs an actual rank argument for these spaces; none is assumed.

## 5. Actual common constant energy 6 is possible

Here is a physical Dirichlet control, not a dark eigenvector. Take L divisible by four, L>=80, n=L^3/2. Let h=(0,0,0), g=(9,1,0), and begin with B charges chi_b=(-1)^(b_x). Flip the two B sites h+/-e_x from minus to plus, the two sites g+/-e_x from plus to minus, and the eighteen sites

    f_j=(1,4j+2,0), j=0,...,17,

from minus to plus. Remove the B at v=(1,0,L/2), which was minus. All sites are distinct. Then NB=n-1 and the B-minus count is n/2-19. The only full uniform B stars are h with plus and g with minus.

To verify the last statement, at an even-x A site the unmodified star has four transverse pluses and two axial minuses; the only paired axial minus-to-plus flips are h+/-e_x. At an odd-x A site the only paired axial plus-to-minus flips are g+/-e_x. Creating the other uniform sign would require both transverse z-neighbors to be flipped, impossible because all flips have z=0. The vacancy creates no full star. The additional f_j are separated in y and have no axial partner at x=-1, so they create no further full-plus star.

Put minus A charges at the eighteen A sites in the radius-two A neighborhood of g excluding g, and plus on every other occupied A. There are two physical inputs: one has hole h, the other hole g. Their A-minus count is eighteen in either case. The total number of minuses is n/2-1=(NB-1)/2, so total charge is n and an integer Gauss flow exists. The vacancy is farther than three from h and g. The h input is protected plus and the g input protected minus.

For the completed background of the first input, the protected plus hole set is exactly {h}; for that of the second it is exactly {g}. The corresponding principal geometric blocks are both the scalar 6 at ALL edge phases. Therefore 6 belongs to BOTH constant Dirichlet spectra for this physical chi. The full H columns still have their nonzero actual outgoing rows; the input holes are far apart, so this is not a shared-row cancellation or a dark-mode construction. No Omega weight or actual preparation of these inputs is claimed.

The construction shows why (3) must retain common constants and why spectral disjointness alone cannot finish (5). The unresolved full protected-union module is now narrowed to the fixed-energy boundary cancellation, while the full unprotected dark module and actual source overlap remain separate open obligations.
