# Native compass commutators — independent exact check

Reviewed the root's current `native/compass_commutators.py` and JSON. Independently implemented Hermitian Pauli words using binary symplectic bit masks, rather than the root's site/axis multiplication table. Integer coefficients are retained exactly. Files: `/private/tmp/native-commutator-check/check.py` and `result.json`.

## Second moment by local counting

Take K=1 and a nonaliasing cubic lattice. C has 3N distinct length-two equal-axis Pauli bonds with coefficient1. Pauli words are orthonormal in normalized Hilbert-Schmidt inner product 2^(−N)Tr(A^dagger B), so

    ||C||_HS²=3N.

A C bond along axis a fails to commute only with an H bond that shares exactly one endpoint and has another axis b!=a. Count per C bond:

    2 endpoints x 2 choices b x 2 b-directions =8.

Each commutator contributes a three-site word with coefficient ±2 in J=i[H,C]. For a nonaliasing lattice these 8(3N)=24N words are distinct: the resulting three-site geometry identifies its distance-two a pair and length-one b pair. Thus

    ||J||_HS²=24N*4=96N,
    m2=||J||²/||C||²=32.

This is the infinite-lattice local counting result, with the extensive factor canceling. If restoring H=K H_1 while keeping C as the unscaled pair sum, m2=32K².

## Independent fourth-moment computation

Let K2=i[H,J]=−[H,[H,C]]. The independent implementation gives, for L=5,7,9,

    C: 3N words, coefficient magnitude1;
    J: 24N words, coefficient magnitude2;
    K2 two-site sector: 3N words, coefficient magnitude32;
    K2 four-site sector: 144N words, coefficient magnitude4;
    K2 four-site sector: 60N words, coefficient magnitude8.

Hence

    ||K2||²/N=3*32²+144*4²+60*8²=9216,
    m4=||K2||²/||C||²=3072,
    m4−m2²=2048.

The two-site part is −32C. Subtracting it leaves the four-site residual with norm²/N=6144, which independently gives residual ratio2048.

The implementation verifies these identities with exact integers on L=3,4,5,7,9. L=9 is a conservative nonwrapping local check for the infinite-lattice coefficients: starting from a distance-two C pair, two nearest-neighbor commutators produce support of coordinate diameter at most4. Relative coordinates lie in [−4,4], so mod9 cannot identify two different such relative vectors. This avoids inferring the infinite-lattice count solely from the already observed L4/L5 agreement. The computation supplies local enumeration, not a hand classification of all four-site geometries.

For general K in H=K H_1, m4=3072K^4 and squared-frequency variance2048K^4.

## Short-torus aliases

At L=3 the distance-two C bond equals a nearest-neighbor H bond after periodic relabeling, so C=H at K=1 and J=0 exactly.

At L=4, C has only3N/2 distinct words, each coefficient2. Thus ||C||²=6N, not3N. J has12N words with coefficient magnitude4, giving ||J||²=192N. The ratios m2=32 and m4=3072 happen to survive these aliases. It would be incorrect to quote the L4 raw counts as the infinite-lattice counts.

## Plane symmetries

For each axis a and plane coordinate c, let P_(a,c)=product_(x_a=c) sigma_x^a. An a-axis bond commutes with P because its Pauli component matches even when only one endpoint lies in the plane. A b!=a bond has either both endpoints in that plane or neither, producing either two Pauli anticommutations or zero. The same reasoning applies to the distance-two C bonds. Thus [P,H]=[P,C]=0; J and K2 preserve those sectors as well. This constrains transitions but does not make C conserved under H.

## Spectral meaning and restrictions

These normalized Hilbert-Schmidt moments are moments of the **maximally mixed dynamic structure measure** of C. In that state the measure is symmetric under omega->−omega. The positive squared-frequency variance2048 proves that its full weight is not exhausted by one absolute frequency |omega|. Equivalently the operator identity [H,[H,C]]=Omega² C fails for every Omega.

It does not exclude an isolated pole plus other weight, a single transition in a specially selected ground sector, or a thermodynamic scalar-like excitation. A ground-state structure factor has different weights and must be calculated separately. No state-independent pole exclusion follows from these HS moments.

At exactly maximal mixing, the retarded commutator expectation vanishes identically by cyclicity of trace, despite the nonzero structure measure and its moments. Do not identify m2,m4 with a nonzero infinite-temperature retarded response. Finite-temperature response requires the appropriate population weights and its own normalization.

The three-spin J is T-odd under the stated usual spin time reversal, consistent with i[H,C] when H and C are T-even and time reversal conjugates i. None of this identifies electromagnetic charge, Lorentz-scalar dynamics or universal matter coupling.
