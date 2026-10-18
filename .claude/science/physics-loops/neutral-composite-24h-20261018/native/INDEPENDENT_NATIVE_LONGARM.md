# Focused native long-arm structure check

Checked 2026-10-18 against `/private/tmp/neutral_native_longarm_structure.md`. The structural conclusion is valid for a fixed-order, translation-invariant, symmetry-preserving local coefficient construction and the stated compressed adjacent-x-column arm. It is not an invariance or full-pole theorem.

## Connected support and long-arm structure

The finite-order homological recursion can be organized into connected supports. Initial interactions are connected bonds; a nonzero commutator requires overlap, and its union is connected. The commuting longitudinal-bond filter enlarges a support only by incident longitudinal bonds, so connectedness is preserved. At fixed order these terms have uniformly bounded diameter/cardinality. This applies to individual Taylor coefficients; the exact exponential remainder is only quasi-local.

In the all-up compact four-wall sector with the preserved even parity per longitudinal plane, configurations consist of two columns sharing a finite interval. For a sufficiently long initial interval, changing the unordered column pair needs at least 2ell physical spin flips. A fixed local coefficient cannot do that. Retaining the same pair, a final interval differs only near its endpoints; a connected term cannot modify both distant endpoints. Thus every surviving deep-arm offdiagonal entry moves one endpoint by a bounded distance. Bulk translation invariance makes the amplitude independent of ell. Longitudinal COM zero adds the endpoint contributions and retains real amplitudes. Reality follows directly because H0 is real diagonal, the homological inverse divides real matrix entries by real energy differences, and the resulting generators are real antisymmetric. No x/y scalar identification is needed.

After subtracting the vacuum scalar, diagonal terms supported entirely away from the flipped columns give zero. Terms lying in the constant interior transverse pattern give a fixed difference per allowed longitudinal translate. Their count is affine in ell after the two endpoint neighborhoods separate. Terms near either endpoint give constant contributions. This proves affine diagonal plus finite-range Toeplitz hopping in the long arm. All short-length failures lie in a fixed finite endpoint block after enlarging it by the hop range.

The claim implicitly uses consistent translation-invariant coefficients and the stated symmetry-preserving four-wall/plane-parity sector. Arbitrary site-dependent gauge choices or arbitrary compression to a larger sector would not inherit it. Infinite-volume coefficients, or finite boxes with adequate margins and no wraparound, are essential to the stated exact long-length identity.

## Polynomial form and leading coefficients

A real symmetric finite-range Toeplitz operator is a polynomial in T=S+S dagger modulo a finite endpoint matrix. This follows from the full-line Chebyshev identity; half-line reflected paths supply only a bounded endpoint correction. Constant polynomial terms can be absorbed into the scalar offset.

For fixed order m>=4, the known adjacent-pair first-order hopping is -2 in fast units, and the fourth-order plaquette tension is lambda^3/16. As a direct check of that tension: an adjacent pair of columns changes the sign of four transverse elementary plaquettes per interior slice; the coefficient -Jz lambda^4 P/128 gives an energy cost 2/128 for each, hence Jz lambda^4/16 per length. The length-independent terms are separate. This establishes f_lambda=lambda^3/16+O(lambda^4)>0 at fixed truncation and small positive lambda, in the coefficient gauge in which the plaquette term has been established. For m<4 the stated positive tension cannot be inferred.

The uncoupled compressed arm begins with ordinary half-line adjacency. The host connection is outside this compression, so no order-one endpoint defect is silently included. Consequently F_lambda=O(lambda) follows for the compressed model. The general strip lemma applies to that arm when its coefficient and gauge hypotheses are met; compression alone says nothing about the effect of the excluded channels.

## Gauge transfer: a sufficient local lemma, not an unrestricted assertion

There is a useful precise condition under which the tension is invariant. Suppose two coefficient gauges through fixed order are related, within the preserved N and plane-parity sector, by a formal near-identity unitary whose generators themselves admit translation-invariant connected finite-support decompositions order by order. The preceding support argument applies to those generators too. Deep in this arm each has the form a*n plus a finite-range Laurent/Toeplitz operator (possibly imaginary/antisymmetric as appropriate), modulo endpoint terms. In the bulk,

    [a n+P(S,S^-1), b n+Q(S,S^-1)]
      = a[n,Q]-b[n,P],

because Laurent polynomials commute. This is again a constant-coefficient hopping operator, with no affine diagonal slope. Subsequent nested commutators also cannot produce an affine diagonal slope. Finite-support products cannot communicate between the deep arm and its short boundary at fixed order. Thus such a LOCAL block-diagonal gauge transformation cannot change the bulk tension coefficient.

This supplies a route to justify the stated transfer; it does not make it true for an arbitrary nonlocal effective-Hamiltonian gauge. To invoke it here, identify the relation between the previous canonical coefficient gauge and the new actual local normal form and verify that its block-diagonal intertwiner has the stated local, translation, and plane-parity properties. Formal homological uniqueness suggests this can be established recursively, but it is not established merely by naming both gauges 'canonical'. The draft's existing fallback—retain the known coefficient gauge and mark alignment with the actual remainder bound as required—is therefore scientifically appropriate until that intertwiner argument is recorded.

Conclusion: the affine-plus-Toeplitz long-arm structure is sound with the supplied background and local symmetry-preserving construction. Leading tension transfer is justified under the explicit local-gauge lemma above; otherwise keep it conditional. The result does not establish long-arm invariance, a whole-sector Green function, a full microscopic resonance, or a detector/cosmology identification.
