# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Finite physical-bit bulk source normalization check

Mathematical scope: the specified uniformly polarized reference, zero momentum, and first-order source-connected block. This is an explicit finite Pauli-action control; no higher-order channel closure is claimed.

Scratch implementation: neutral-bulk-source-normalization-independent.py/json. The control uses a periodic5×5×9 array with225 actual spin bits, represented sparsely by Python integers. It does not use a projected rung Hamiltonian, assumed relative-coordinate matrix, or a positive four-column parity reduction. The longitudinal energy is computed directly as twice the number of physical broken ZZ bonds, and every transverse native bond is applied as a physical bit flip. -XX contributes -1; -YY contributes +(-1)^(number of currently down endpoint spins). Destinations are retained exactly when their physical longitudinal excitation energy is8Jz.

Normalized orbit states are built by enumerating all225 spatial translations of each unordered two-column interval, taking a set of actual bitstrings, then dividing by the square root of its cardinality. This explicitly handles physical rather than ordered-pair normalization. The chosen interval lengths avoid longitudinal folding and wrapping aliases. The finite transverse torus is included in the independent host comparison.

The following full-vector equalities pass (reported differences zero after a1e-13 floating cancellation threshold):

- K1 d equals the independently constructed even relative-coordinate square-lattice host action with nearest-neighbor hopping-2, plus -2E2.
- K1 E2=-2d-2E3.
- K1 E3=-2E2-2E4.
- A length3 interval on columns separated by two transverse steps has zero K1 action in the energy8 band.

Here E_l=(|x,l>+(-1)^l|y,l>)/sqrt(2), and d=E1. The relative-coordinate representation of d is (|ex>+|-ex>-|ey>-| -ey>)/2. The normalized even relative basis maps each physical unordered-pair orbit to (|r>+|-r>)/sqrt(2). Thus the host hopping and interval coupling require no extra sqrt(2). The frozen vector is an explicit reminder that this source block is not the whole energy8 manifold.

## Original source

For each of the450 transverse bonds applied to the all-up vacuum, the exact physical distance-two longitudinal observable C=sum_(x,y,z) Z_(x,y,z)Z_(x,y,z+2) changes by-8. The corresponding intermediate energy is8Jz, so first-order ground dressing is -V|0>/(8Jz). After the connected expectation subtraction, multiplication by Delta C gives

    C_eff|0> = V|0>/Jz + higher orders.

This relation is a transition-source statement at first order, not an all-orders operator identity. At the chosen source normalization C/sqrt(Nphysical), each of the two bond orientations has Nphysical translates. The normalized source is therefore

    -lambda |x,1> +lambda |y,1> = -sqrt(2)lambda d.

The scratch code evaluates Delta C using actual physical bitstrings and explicitly constructs this dressed source. Its difference from -sqrt(2)d is zero numerically, and its coefficient-vector norm squared is2. Hence the leading total source variance is2lambda² in this convention. The thin2×2 value2lambda is not the normalization of this large-array C/sqrt(Nphysical) source.

The relative X/Y sign follows from native Pauli phases on the uniformly polarized reference. Other aligned-column backgrounds can change the hopping flux and source signs; uniformity is a supplied preparation premise, not implied by strong Jz or plane parity. The first-order equalities do not prove stability under higher orders, uniform thermodynamic perturbation bounds, a pole, a physical scalar, or a detector coupling. No repository edits or formal audit were performed.

## SHA-256 identities

- `/private/tmp/neutral-bulk-source-normalization-independent.py`: `68e509730d4411cbbf44a9c299fa26f2b68c15aecb0dbb4a0128b900ddfc105d`

- `/private/tmp/neutral-bulk-source-normalization-independent.json`: `0089401c59badd488f354c211f51984325199cb7deb4d7367f94dba22361d61f`

- `/private/tmp/neutral-bulk-two-wall-channel-check.md`: `7066c3c0b6f41e4e4f0342f5337711719632413613088900d26a6e0b569ea1e5`
