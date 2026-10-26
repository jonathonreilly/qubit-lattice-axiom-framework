# Supplied cyclic three-dimensional algebra: phase maps and conjugation

**Date:** 2026-10-24
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** conditional finite algebra; former universal continuum-limit exclusion withdrawn
**Primary runner:** [exact finite controls](../scripts/cl3_koide_a1_probe_continuum_limit_2026_05_09_probe15.py)
**Cache:** [bounded capture](../logs/runner-cache/cl3_koide_a1_probe_continuum_limit_2026_05_09_probe15.txt)

## Supplied domain

Let C be a unitary 3 by 3 matrix with C^3=I and three distinct eigenvalues
1, omega, omega^2, where omega=exp(2 pi i/3). The supplied cyclic permutation
matrix is one realization. Thus I,C,C^2 are linearly independent and
A=span_C{I,C,C^2} is a unital commutative *-algebra. No framework derivation
of this carrier or its identification with matter is assumed.

For |z|=1 define the complex-linear map phi_z on A by
phi_z(I)=I, phi_z(C)=z C, phi_z(C^2)=z^-1 C^2.
It preserves adjoints, and phi_z phi_w=phi_(zw), so these maps constitute
a continuous linear U(1) action. This construction alone is not a physical
symmetry or a selector of the BAE amplitude ratio |b|^2/a^2=1/2.

## Exact finite lemma and proof

The map phi_z is multiplicative if and only if z^3=1. Necessity follows
by comparing phi_z(C^2)=z^-1 C^2 with phi_z(C)^2=z^2 C^2; C^2 is invertible,
so equality forces z^3=1. Conversely, if z^3=1, substitution C -> z C
preserves the relation C^3=I in C[t]/(t^3-1), and sends C^2 to z^2 C^2
=z^-1 C^2. It defines exactly phi_z on the basis, hence is multiplicative.
Its inverse is phi_(z^-1), making it a unital *-automorphism in this case.

If a unitary U implements phi_z by U X U^*=phi_z(X) for all X in A,
then C and zC must have the same eigenvalue multiset. Their characteristic
polynomials are respectively t^3-1 and t^3-z^3. Equality forces z^3=1.
For z^3=1 the diagonal unitary diag(1,z,z^2) implements C -> zC for the
supplied cyclic permutation C e_j=e_(j+1 mod 3). Unitary conjugation of this
construction gives the same conclusion for any C satisfying the hypotheses.
Thus the condition is necessary and sufficient for this finite implementation.

Any unitary diagonal in the C eigenbasis commutes with C and every polynomial
in C, so its conjugation fixes A pointwise. In particular conjugation by C
itself is trivial on A. This is different from the character automorphism
C -> omega C, which is nontrivial and implemented by a different unitary.
No uniqueness of a continuous unitary extension is asserted.

## Counterexample to the former cardinality argument

For n>=0 let G_n={exp(2 pi i k/(3*2^n)): 0<=k<3*2^n}. Each is a finite
cyclic subgroup of U(1), contains C3, and is included in G_(n+1), by replacing
k with 2k. Their union is countable but its closure is U(1). Indeed for any
angle theta in [0,2 pi), choose k=floor(3*2^n*theta/(2 pi)); the angular
error is less than 2 pi/(3*2^n), and the chordal error is at most that error.
It tends to zero. Thus closure can enlarge cardinality. Applying phi_z gives
a continuous action on the fixed finite-dimensional vector space A as well;
finite dimension does not forbid a continuous linear action.

This counterexample refutes the former mathematical exclusion mechanism.
It neither establishes nor excludes the physical admissibility of these
subgroups, their closure, a nonmultiplicative projection, or an emergent action
in the framework. Establishing that admissibility remains an open obligation.
The finite conjugation lemma does not exclude general continuum, thermal,
renormalization, scaling or nonmultiplicative limiting constructions.

## Execution scope and historical disposition

The runner checks exact symbolic basis multiplication, characteristic
polynomials and discrete implementations, plus selected finite phase/grid
illustrations. The proof above, not sampled grids, establishes density.
There is no site, physical momentum mode, lattice-volume sequence, kinetic
model or infinite-volume execution. No broad N1-N8 PASS is asserted.

The old nine-route universal verdict, literal-True scores, inaccurate claimed
infinite-volume execution, all numerical fixtures and previous cache are
preserved exactly in `../archive/source-history/koide-probe15-universal-limit-withdrawal-2026-10-24/`.
They are withdrawn as current proof of a general physical exclusion.
The filename is retained for citation continuity; this is a substantive
replacement with the finite lemma, not a renamed universal negative claim.

The [conditional Stefan theorem](AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md)
remains contextual only: supplied continuum thermal mathematics grants no
physical authority to the former limit exclusion or to this finite lemma.
No empirical amplitude, new physical primitive or audit verdict is introduced.
