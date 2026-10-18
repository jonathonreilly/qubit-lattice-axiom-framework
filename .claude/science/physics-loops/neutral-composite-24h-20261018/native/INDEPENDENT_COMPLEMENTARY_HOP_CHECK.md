# Native third-order complementary-layer assisted hop

Focused independent physical-bit calculation for longitudinal period four. Energies and coefficients below use H/J, with the transverse factor lambda removed from each insertion. No new interaction is introduced.

## Endpoint and complete minimal path set

Take an initial singleton at column i, layer zero, over aligned background signs s_i,s_j. Flipping the same transverse edge (i,j) at layers 1,2,3 changes six spins. The old column becomes fully reversed. The neighbor has its three complementary-layer spins reversed, which is a singleton at layer zero relative to the reversed majority background. Thus the final singleton is at j with BOTH aligned-column signs reversed:

    |s,i> -> |s with i,j reversed; j>.

This majority-background representation is unique for a singleton; the final three-spin pattern must not be mislabeled as a separate species over the original background.

The initial and final physical configurations differ on precisely those six sites. Three native insertions supply exactly six spin flips. Therefore any order-three word reaching this endpoint must flip each target site once and no other site. Each layer has only the two specified target columns, so the word uses their same edge once in each of layers 1,2,3. The six permutations exhaust the paths; there is no other geometric order-three contribution to this matrix element.

## Direct denominator and sign enumeration

Independent two-column bit enumeration gave the intermediate wall counts:

    order 123: (4,4)
    order 132: (4,6)
    order 213: (6,4)
    order 231: (6,4)
    order 312: (4,6)
    order 321: (4,4).

Initial/final N=2 has energy 4. The resolvent factors are (4-2N1)^(-1)(4-2N2)^(-1). Their sum is two terms 1/16 plus four terms 1/32, exactly 1/4. None of the intermediate states belongs to N2.

Every XX insertion has Hamiltonian matrix element -1, giving total -1/4. Every complementary-layer YY insertion sees the unchanged original aligned signs at that layer, so its Hamiltonian matrix element is +s_i s_j. Their product is (s_i s_j)^3=s_i s_j, giving +s_i s_j/4. I checked all four choices of s_i,s_j by explicit bits; the signs and endpoint match in every case.

## Canonical folded term

The canonical third-order expression includes

    PVRVRVP - (1/2){PVR²VP,PVP}.

Both two-insertion N2 operators, including the R² rather than R denominator version, preserve the majority background within the singleton block. Changing that background in a singleton transition requires at least six physical flips. The first-order singleton hopping also preserves it. Their products therefore cannot reach this background-changed endpoint, so the folded term has zero matrix element here. Intermediate half-column states cannot repair this route: they are in the opposite exact global spin-parity sector. This exclusion is structural, not a cancellation fitted to the direct six paths.

## Operator notation

Let E_e=Xbar_i Xbar_j act by reversing both majority background signs without moving the singleton. Let Tx,e be the existing position-restricted singleton hop on that x edge, with coefficient -1, and Ty,e the corresponding y hop with coefficient -s_i s_j. On the same edge the background product s_i s_j is unchanged by E_e, so ordering the two factors causes no sign ambiguity. The contribution is exactly

    D3,e = (1/4) Tx,e E_e   for x edges,
    D3,e = -(1/4) Ty,e E_e  for y edges.

Both forward and backward hops are included in the Hermitian edge operators. The position restriction is important: this is not a free background pair flip acting when the heavy excitation is elsewhere. In physical units this term is multiplied by J lambda^3.

## Scope

This is a genuine native background-changing assisted hop in the singleton N2 coefficient block. It demonstrates that the fixed-background first-order graph is not an exact all-orders invariant block. It does not by itself determine the full D3 operator, a relaxed background state, an interaction rate, or a uniform growing-volume heavy dispersion. The established lower-order singleton inequalities and separate dressed-environment estimates retain their own scopes.
