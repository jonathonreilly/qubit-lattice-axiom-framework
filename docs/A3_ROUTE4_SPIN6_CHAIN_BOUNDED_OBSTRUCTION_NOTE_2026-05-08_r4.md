# Supplied Spin(6) matrices, a selected 3+1 block, and cyclic invariance

**Type:** bounded_theorem
**Primary runner:** `scripts/cl3_a3_route4_spin6_chain_2026_05_08_r4.py`

## Supplied construction and scope

Work over C with six Hermitian Jordan-Wigner Clifford matrices on (C²)^⊗3,
γ₂k−1=Z^⊗(k−1)⊗X⊗I^⊗(3−k) and
γ₂k=Z^⊗(k−1)⊗Y⊗I^⊗(3−k). They obey {γi,γj}=2δij.
Their 64 ordered monomials span M₈(C). This explicitly supplied construction
realizes Cl₆(C); it is not an ordinary tensor product of two one-qubit
matrix algebras. M₂(C)⊗M₂(C)=M₄(C). Also
Cl₃(C)=M₂(C)⊕M₂(C), so its ordinary tensor square has four M₄(C) blocks,
not M₈(C). The Clifford factorization uses the graded tensor product.
No axiom derivation of this eight-dimensional carrier is supplied.

The bivectors γiγj/2 preserve the two four-dimensional chirality spaces.
Their restrictions span the 15-dimensional traceless anti-Hermitian algebra
on either chirality space. This is the finite Lie-algebra realization behind
Spin(6)≅SU(4). The volume element Ω=γ1⋯γ6 has Ω²=−I, Ω⁴=I and commutes
with bivectors: its four powers form a cyclic subgroup of order four.
The historical assertion Z₄=Z₂×Z₂ was false. Chirality −iΩ is an involution;
that does not make it the order-four volume element.

## Selected block, not a physical symmetry-breaking derivation

Choose C⁴=C³⊕C and embed su(3) in its first block. Its traceless Hermitian
centralizer in M₄(C) is spanned by Q=diag(1/3,1/3,1/3,−1).
The charge normalization is supplied. The block-preserving subgroup of SU(4)
is S(U(3)×U(1))≅(SU(3)×U(1))/Z₃; a direct product statement ignores the
kernel. Indeed (A,z)↦diag(zA,z⁻³) has kernel
{(z⁻¹I₃,z): z³=1}. Its Lie algebra is su(3)⊕u(1).

The defining four branches as 3_(1/3)⊕1_(-1). The exterior square branches
as 3bar_(2/3)⊕3_(-2/3), since Λ²3≅3bar via the invariant alternating tensor.
Q is scalar on the chosen three-block. This proves only that this supplied
central charge cannot distinguish its three basis vectors. It does not identify
those vectors simultaneously with physical colors and generations, or prove
a unique dynamically selected subgroup among all SU(4) subgroups.

## Cyclic control and the precise restriction

Let C cyclically permute three coordinate basis vectors. It is unitary with
determinant one, and represents a three-cycle in the Weyl group through the
normalizer of the diagonal torus. It is a group element, not a Lie-algebra
generator and not a derived physical generation transformation.

If [O,C]=0, then <e_j,Oe_j> is independent of j by cyclic transitivity.
But O need not be scalar. The full complex commutant is span{I,C,C²}.
For example H=C+C† is Hermitian, commutes with C, has equal diagonal entries
zero and eigenvalues {2,−1,−1}. Thus cyclic-invariant observables can
separate Fourier modes even though they cannot separate coordinate-basis
expectations. H is a linear combination of embedded su(3) generators.
The old assertion that every C₃-invariant polynomial reduces to Casimirs
was false. Full SU(3) invariance, a stronger hypothesis, does imply scalarity
on its irreducible defining three by Schur's lemma.

## Open obligations and recovery

No general generation no-go, unique physical Pati-Salam breaking pattern,
triality exclusion of all extensions, or closure of AC_phi follows.
Physical carrier, matter representation, dynamics, admissible observables
and generation interpretation remain open. Former uncomputed PASS narration
and random-matrix pseudo-proof are replaced by finite matrix checks. The
runner uses floating-point rank/residual checks, supporting the explicit
algebra above rather than proving physical identifications.

There are no repository scientific premises for this supplied finite model.
Earlier color, three-generation and AC_phi notes are historical motivation
only. Recover the original argument and runner at baseline
f24d17d97d372df977476e4a69674577f31af575 and their unchanged paths.
