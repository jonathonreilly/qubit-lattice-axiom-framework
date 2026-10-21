---
claim_id: block_tick_has_no_exact_copy_su2_and_only_a_sublattice_axial_remnant_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied two-partition block tick with the spin-3/2 corner action: six anticommuting Hermitian involutions built from the tick generate all 8x8 matrices, so the K-independent block-local commutant is span{1, eps} at mu = 0 and the scalars for mu > 0; the long-wavelength Dirac algebra read from the tick gives C^8 = Dirac(4) x copy(2) with an emergent U(2) that the lattice breaks at O(k^2); the only exact remnant is the sublattice sign eps = gamma5 sigma3; a block-local inversion flips gamma5, so the content is vector-like; the copy doublet is the E irrep of the cube group; and the w = pi sector holds two massless copies at K = pi(1,1,1). No chirality, weak SU(2), copy symmetry or physical species is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/block_tick_has_no_exact_copy_su2_and_only_a_sublattice_axial_remnant_2026_10_21.py
---

# The block tick has no exact copy SU(2), only a sublattice axial remnant

Claim type: bounded_theorem.
Primary runner: `scripts/block_tick_has_no_exact_copy_su2_and_only_a_sublattice_axial_remnant_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its block tick has 8 modes per block, which at low energy form two Dirac copies. This note asks whether an SU(2) acts on those copies, whether anything selects a chirality, and what the mass breaks. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the ticks used.

## The hidden Clifford algebra

The Bloch form U(K) = D^dag W D W reproduces the 6^3 lattice spectrum at mu = 0.3 to 8.9e-16. Define Gamma_a = sqrt(3) W_a and Gamma_(a+3) = i Gamma_a tau_a with tau_a = diag(2 c_a - 1). These are six anticommuting Hermitian involutions on C^8 (7.3e-15). The odd-block hop is D^dag Gamma_a D = cos K_a Gamma_a + sin K_a Gamma_(a+3), so the massless tick is a product of two unit 6-vectors. The product Gamma_1 ... Gamma_6 equals -i eps, where eps = (-1)^(x+y+z) is the sublattice sign.

## The block-local commutant

- At mu = 0 the K-independent commutant of {U(K)} has dimension 2 and equals span{1, eps}, so the group is U(1)_V x U(1)_eps.
- At mu = 0.05, 0.3 and 1.0 it is the scalars, so the group is U(1)_V alone.
- eps anticommutes with W and with the mass-free hop, and eps W(mu) eps = -W(-mu).
- The rotations fix eps for the E, C2face and C3 classes and send it to -eps for C4 and C2edge, so the commutant with rotations is the scalars.
- At one generic K the pointwise commutant is 32 = 16 + 16, a U(4) x U(4) on the two fourfold bands. It restates the degeneracy and changes with K.
- For any block-local Y, X_Y = sin^2(w) Y - (U - U^dag) Y (U - U^dag)/4 commutes with U (1.3e-14). These are range-1 conserved bilinears and form no group.

## The continuum Dirac algebra read from the tick

U(0) = exp(i mu beta) with beta = (Gamma_1 + Gamma_2 + Gamma_3)/sqrt(3) = W. The velocity matrices alpha_a = sqrt(3) dH/dK_a = i Gamma_(a+3) beta (8.3e-11) give speed 1/sqrt(3) and, with beta, the Dirac Clifford algebra. gamma5 = i alpha_1 alpha_2 alpha_3 is a Hermitian involution that commutes with alpha and anticommutes with beta. The commutant of {beta, alpha} has dimension 4, so C^8 = Dirac(4) x copy(2) with an emergent U(2). sigma3 = eps gamma5 lies in the copy algebra, and sigma1, sigma2, sigma3 obey the Pauli algebra (2.2e-15). In the massless continuum the commutant of {alpha} has dimension 8, giving U(2)_L x U(2)_R. The lattice remnant eps = gamma5 sigma3 is +1 on (L, copy+) and (R, copy-) and -1 on the other two.

## How the lattice breaks the emergent symmetry

At |k| = 0.02 the commutators [sigma_i, U(k)] are 8.29e-5, 1.01e-4 and 1.44e-4 at mu = 0.3, all with fitted slope 2.00, so the copy generators are broken at O(k^2). At mu = 0, sigma3 is broken at O(k^2) while eps is exact, and the chiral generators P_L sigma_i are broken at O(k^2). At mu = 0.3, P_L sigma1 is broken at O(mu) (0.213 as k -> 0). Exactly, ||[P_L sigma1, U(0)]|| = sin mu (0.296 at mu = 0.3): the mass breaks SU(2)_L x SU(2)_R to SU(2)_V and breaks U(1)_eps. Whether a K-dependent, multi-block dressing could make the copy generators exact is not settled.

## Rotations, inversion, particle-hole and species

- L(R) U(K) L(R)^dag = U(RK) for the 24 corner actions (3.6e-15), and each factorises as L(R) = S_(1/2)(R) rho(R) with rho(R) in the copy U(2).
- The copy doublet carries |chi| = (2, 2, 0, 1, 0) on (E, C2face, C4, C3, C2edge): the E irrep of the cube group, which factors through the axis permutations S3. rho is irreducible, so only scalars in the copy U(2) commute with all 24 rotations.
- A one-dimensional block-local inversion, the corner map s -> 1 - s, satisfies P U(K) = U(-K) P and flips gamma5 and eps, so the matter content is left-right symmetric (vector-like).
- A block-local particle-hole map M U(K) = U(-K)* M exists, with solution dimension 2 at mu = 0 and 1 at mu = 0.3.
- The w = 0 sector is gapped by mu at K = 0 (two Dirac copies). The w = pi sector is massless at K = pi(1,1,1) with speed cos(mu/2)/sqrt(3) (0.5709 at mu = 0.3).
- Every band is exactly fourfold; no threefold degeneracy appears anywhere sampled.

## Checks

The runner prints `TOTAL: PASS=32 FAIL=0`. Its PASS lines cover the Bloch form, the six involutions, the hop decomposition, the product identity, the commutant at mu = 0 and mu > 0, eps under W and rotations, the pointwise commutant, the conserved bilinears, the Dirac algebra, gamma5, the copy algebra and its Pauli matrices, the chiral commutant, the remnant's signs, the O(k^2) and O(mu) breaking, the mass identity, rotation covariance and factorisation, the copy irrep and its irreducibility, inversion and its action, particle-hole, the species count and fourfold bands.

## Supplied and boundary

Supplied: the j = 3/2 rotation action (the S3 copy representation depends on it), the left-right sign convention, and the choice to count only block-local matrices as internal. beta and alpha are read from the tick, and the copy algebra is their commutant. As estimates, measured parity violation in the weak interaction and the LEP count N_nu = 2.984 +- 0.008 are not reproduced by a vector-like doublet with no chiral SU(2). The massless w = pi copies would be an observable mismatch unless removed. No chirality, weak SU(2), copy symmetry or physical species is established.
