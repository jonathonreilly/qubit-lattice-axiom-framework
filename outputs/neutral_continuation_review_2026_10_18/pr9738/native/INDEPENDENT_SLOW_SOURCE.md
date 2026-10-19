# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused slow-channel original-source check

Mathematical scope: the specified projected fast model and limiting source vector, with a logarithmic-remainder qualification. No native pole or complete slow closure is established.

## Physical-bit normalization

The independent scratch control reuses the5×5×9 physical-bit geometry and normalized translation orbits from neutral-bulk-source-normalization-independent.py. It constructs the one-step Q-space vectors and contracts them with the actual energy denominator8-E_intermediate. The resulting matrix elements are A2->e=-1, A2->d2=-1, D2->e=-2, D2->d2=0, to <1e-15. A2 combines the two axial-distance-two ell2 orbits with plus sign. D2 combines the two unordered diagonal orbits with plus sign and unit norm, equivalently four normalized even relative-coordinate positions. No extra factor sqrt(2) is needed.

The A2 projected identity is therefore v_A=P_F K2 A2=-d2-e=F d/2, reusing the independently checked full K1 action Fd=-2d2-2e. For D2, transverse hopping of either column gives two nearest-pair routes, yielding v_D=-2e. Its ell1 contraction paths cancel between mixed X/Y orderings. This does not remove the other K2 outputs in the slow ell2 host; these are projected fast vertices only.

The scratch code also checks every actual four-spin mask in A2 and D2 against the xor of every pair of physical native transverse edge masks. None can be reached from vacuum in two operations. Hence any second-order compressed observable built from the diagonal C and two transverse vertices has zero direct matrix element into these slow supports, including canonical normalization/folded contributions. Each longitudinal layer would otherwise need a single native edge joining two nonadjacent columns. The supplied first-order source remains -sqrt(2)lambda d for C/sqrt(Nphysical).

## Retarded elimination and sign

Let R(z)=(z-F)^-1, with fast kinetic energy scaled by Jz*lambda. For the arm hopping-2 its surface Green function has g(0+i0)=-i/2. The bare d host Green function G has a logarithmic van Hove divergence at zero, since its form factor is nonzero at the square-lattice saddles. Schur reduction gives

    Rdd=G/(1-4gG) -> -1/(4g)=-i/2,
    Red=-2gRdd -> +1/2.

Using FR=zR-I,

    <v_A|R|d>=(zRdd-1)/2 -> -1/2,
    <v_D|R|d>=-2Red -> -1.

The physical slow-fast vertex is Jz*lambda² v, while the fast resolvent contributes1/(Jz*lambda). Multiplying by the original source -sqrt(2)lambda d gives the limiting slow source

    lambda² (A2+2D2)/sqrt(2).

The sign is positive in the supplied d/e conventions. Reversing a basis-vector phase requires changing its vertex and source coefficient together.

## Remainder and scope

The zero-energy limit is a limiting-absorption/continued infinite-host statement. It is not obtained by setting z=0 in an arbitrary finite discrete host before taking its volume limit. At physical energies E-8Jz=O(Jz*lambda²), the scaled fast argument is z=O(lambda). Because G diverges logarithmically, Rdd and Red generally have corrections O(1/log|z|). The D2 source thus has a correction of orderlambda²/log(lambda), not an automatic O(lambda³) correction. The A2 identity contains an extra z and suppresses that particular sensitivity. The safe leading statement is lambda² times the displayed vector plus o(lambda²) within this partial fast model, with the nonanalytic correction retained if higher accuracy is needed.

Native changes to the fast operator, the other ell2 slow channels, slow eigenvector mixing and higher-order dressed-source terms are not controlled here. The result is not a proof that A2 alone is observable or isolated, not a total-width estimate, and not a physical scalar identification. No repository edits or formal audit were performed.

## SHA-256 identities

- `/private/tmp/neutral-slow-source-independent.py`: `f37d4e6cc5c8fb3185dd0a7686cc02603f070eba09bafa28eb69353b6279ebc3`

- `/private/tmp/neutral-slow-source-independent.json`: `82c27a2964bab36a9cc4a7f29aca9fc51265673bc271aa0b6556148dfff0453e`

- `/private/tmp/neutral-bulk-source-normalization-independent.py`: `68e509730d4411cbbf44a9c299fa26f2b68c15aecb0dbb4a0128b900ddfc105d`

- `/private/tmp/neutral-axial-two-channel-check.md`: `172103b3a5663989b5071d76d0a2992233d8c1630f3441bab6a233a2fb05da83`

- `/private/tmp/neutral_bulk_second_boundary.json`: `8ad010f53bc869c0227f9e3e6ce5e7fca68106b79d35929671303163aeb0a61c`

## Follow-up: confined fast-arm robustness

The previously derived source limit is STRICTLY a result of the unconfined-fast partial model unless additional limiting conditions are established. A native tension on the fast adjacent arm changes its endpoint Green function into a function with closely spaced poles and zeros; replacing it pointwise by -i/2 is not justified by the algebra below.

For arbitrary arm endpoint g(z), retaining the same bare host G(z) and coupling -2, the exact identities are

    Rdd=G/(1-4gG),
    Red=-2gG/(1-4gG)=(1-Rdd/G)/2.

The axial and diagonal effective-source amplitudes, before multiplying the common lambda², are respectively

    [1-z Rdd]/sqrt(2),
    sqrt(2)[1-Rdd/G].

Therefore the limiting vector (A2+2D2)/sqrt(2) holds along a specified sequence/regulator precisely when zRdd tends to0 and Rdd/G tends to0. Written without shorthand, these require zG/(1-4gG)->0 and 1/(1-4gG)->0. Convenient sufficient conditions are |gG|->infinity and |z/g|->0. Neither is automatic for a confined arm.

At an exact zero of g, Rdd=G and Red=0: provided zG->0, the axial coefficient still tends to1/sqrt(2), but the diagonal coefficient is zero instead ofsqrt(2). Near a hybrid pole where1-4gG is small, even the axial condition may fail. When g scales as1/G with a finite nonexceptional product, the diagonal coefficient generally approaches a different value. Thus confinement is not merely a harmless small correction to the source on every energy sequence.

The supplied fast turning length/level-spacing estimate suggests densely recurring exceptional energies as lambda decreases. It does not establish that their windows have negligible weight for a chosen observable or preparation. Such a claim needs quantitative zero slopes, pole residues, window measures, and a specified averaging/regulator/order of limits. A heuristic narrow-window estimate is not a uniform source theorem.

A regulator or energy average broad enough to wash out the fast discrete spacing may recover a smooth endpoint function, but this requires an independent limiting-absorption or averaging argument. In particular, if the fast spacing and the candidate slow width are both of physical orderJz*lambda^4, averaging over many fast levels need not preserve resolution of that slow width. One cannot silently use such averaging while claiming a pointwise native line shape or intrinsic width at the same scale.

Consequently the earlier logarithmic-correction statement and the response/residue calculation using this source remain conditional on the unconfined fast model (or on a separately demonstrated family satisfying the two exact limiting conditions). They are not established native leading-source coefficients. This caveat does not alter the finite Pauli normalization, zero direct second-order source, or projected K2 vertex identities.
