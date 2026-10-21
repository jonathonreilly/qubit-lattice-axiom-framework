<!-- Original PR9780 source SHA256 29ee99bba1a95e067eb2bed4e8cdc65287e374390bf79d60cf27ccb51991857c. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# A positive microscopic spectral window for the large neutral feature

Status: bounded-support. This is an asymptotic joint weak-coupling/growing-box theorem for the supplied Hamiltonian and original bond readout. It is not a full-H pole or isolated-band theorem. All calculations and controls are model development; there is no empirical fit or independent observation test.

## 1. Statement

Take the original one-qubit Hamiltonian H=-J sum(ZZ_z+lambda XX_x+lambda YY_y), J>0, lambda>0. Choose even periodic cubes of side L comparable to lambda^-4 as in MICROSCOPIC_GROUND_WINDOW_PROOF.md and fix 0<alpha<2/3. In the complete compact four-wall first-order graph choose Qx=Qz=0 and b=cos(Qy/2) below its derived threshold so its binding delta=Eh(b)-Eb(b) equals lambda^alpha. On the actual momentum mesh choose the nearest Qy. This is an explicitly selected momentum family, not a derived preparation or cosmological selector.

Define the physical normalized Fourier source

 C_Q=V^-1/2 sum_r exp(-iQ.(r+ez)) Z_r Z_(r+2ez).

For each exact microscopic ground vector gs of energy Eg, center q=(C_Q-<C_Q>)gs. Let P_I be the spectral projector of H-Eg onto the real interval I centered on J[8+lambda Eb(b)] with half-width J lambda delta/4. Then

 ||P_I q||² >= lambda² W0 delta log²(1/delta) [1-o(1)],

where W0 approximately .02574494409835 is the derived original-source constant in LARGE_BOUND_FEATURE_PROOF.md. The o(1) is uniform over exact ground vectors. Averaging yields the same bound for any ground density. Since C_Q is complex, this positive weight is <gs|(C_Q-<C_Q>)† P_I (C_Q-<C_Q>)|gs>, with C_Q†=C_-Q. It is not the C_Q C_Q correlator. The interval shrinks; it may contain other contributions and continuum-like finite-volume levels. No upper bound matching this weight or isolation of its contribution is asserted.

## 2. Quantitative inherited inputs

The local finite-order construction gives U H U†=J[B40+R40], B40=2N+sum_(j=1)^40 lambda^j Dj, with every Dj a finite sum of translation-covariant, connected, bounded-support interactions preserving N and plane Pauli symmetries. Termwise N filtering enlarges support only by incident vertical neighbors. These are exact identities plus controlled remainders, not an assumed effective interaction.

On these cubes, the unperturbed lowest subspace P0 consists of aligned columns s_xy=a_x b_y with all transverse plaquettes +1. B40 acts there as E_vac times the identity. The established form bound gives a positive spectral gap; the weaker lower bound c lambda^4 already suffices here. The global remainder is O(V lambda^41)=O(lambda^29), so every U gs lies within O(lambda^25) of P0. The prior theorem actually obtains the stronger O(lambda^29) projector estimate for its chosen L; using the weaker bound is conservative. Also |Eg/J-E_vac|=O(lambda^29). No claim that the true-ground projector has the full P0 rank is used.

The transformed original Fourier source has connected local Taylor coefficients through order40 and global tail O(sqrt(V) lambda^41)=O(lambda^35). Norm C_Q<=sqrt(V)=O(lambda^-6). Thus replacing U gs by its normalized P0 projection costs O(lambda^19) in the source vector, negligible below. Normalizing the projection does not alter this order.

## 3. Uniform native coefficient bound on the feature

Let chi be the normalized K1 bound vector at the chosen momentum, over all-up. Compact layer-even N4 configurations are exactly two columns flipped over the same finite interval of length ell. Host configurations have ell=1 and arbitrary transverse separation. The bound state's ray amplitude decays with ratio |sigma(Eb)|/2 tending approximately .51045, uniformly below .6 near threshold. Therefore every fixed moment of ell is bounded uniformly as delta tends to zero. The divergent transverse separation is not a divergent number of flipped sites in these states.

For a fixed-order term subtract its all-up diagonal value and include all incident z bonds in its support. If its support misses both down intervals, it sees all-up. A finite offdiagonal change there cannot preserve N: it would create walls and cannot reach the existing walls outside that enlarged support; a wall-free whole-column flip is longer than the fixed support. Hence the vacuum-subtracted term annihilates that configuration. At most Cj(ell+1) translated terms can act. Each term has bounded entries and finitely many outcomes, independent of the distance between the two columns. An allowed transition changes ell by at most a fixed Rj unless ell itself is at most Rj. The same count holds for incoming transitions because Dj is Hermitian.

The weighted Schur estimate consequently gives

 ||(Dj-Ej,vac) psi|| <= Cj ||(ell+1) psi||

on this finite-excitation sector, with constants independent of transverse separation, COM delocalization and volume. Summing the fixed orders j>=2 on chi is O(lambda²). This is a vector bound, not a claim that Dj is bounded uniformly on all arbitrarily long intervals. Plane parity and N preservation ensure the complete compact sector remains the appropriate one locally.

## 4. Truncation and all ground backgrounds

Truncate chi to ell<L/4 and relative transverse separations less than L/4 before periodizing its COM. The ray tail is exponentially small in L. The host tail is a polynomial prefactor times exp(-c L sqrt(delta)): the explicit Fourier denominator at its quadratic minimum admits a complex shift of size c sqrt(delta), with energy cost O(shift²). This sharper scale uses the explicit host, not a generic gap-only resolvent bound. Since L sqrt(delta) grows as lambda^(-4+alpha/2), tails and any fixed-degree weighted tails are smaller than every power of lambda. Cutoff boundaries cost only the same negligible errors for each finite-range Dj.

Plane X/Y operations act transitively on P0 product backgrounds and commute with H, U, all Dj and C_Q. Define T Omega_g=U_g chi. Stabilizers, including fixed Pauli phases, act with the same character on the layer-even chi as on all-up. Thus T is well-defined. Distinct backgrounds give orthogonal chi images and orthogonal fixed-order residual supports: a difference of two intervals of length less than L/4 plus a fixed-order local change cannot implement a whole-column flip. Their union occupies less than L/2+O(j) along z. This establishes T†T=P0 and transfers the single-background residual bound to arbitrary normalized P0 superpositions without multiplying by the ground-space dimension.

The same disjoint-support and symmetry argument gives T† q_lead P0=a P0, where a is the derived source overlap in the bound fiber. In each fixed-order normalized source coefficient, distinct translates of a finite excitation pattern overlap only a bounded number of times. The finite-pattern Gram estimate makes the connected-source norm O(lambda) and the source remainder after its first coefficient O(lambda²) uniformly over P0. A nonzero Q excludes its constant vacuum component; proper finite supports cannot flip an entire column. The exact tail and O(lambda^19) ground-projection correction are negligible.

## 5. Residual, source overlap and positive spectral projection

For g=P0 U gs/||P0 U gs|| construct Xi=U† T g. It is normalized and, in physical units,

 ||[H-Eg-J(8+lambda Eb)] Xi|| <= C J lambda².

This uses the K1 eigenvalue equation, the uniform higher-coefficient bound, truncation, and the global microscopic remainder. The source satisfies ||q||=O(lambda) and

 |<Xi,q>|=lambda sqrt(W0 delta) log(1/delta) [1+o(1)]+O(lambda²).

Here the threshold asymptotic is uniform along the chosen b(lambda), and the O(lambda²) source error is smaller than the displayed amplitude. The spectral theorem gives

 ||(1-P_I)Xi|| <= C lambda/delta.

Cauchy-Schwarz then yields

 ||P_I q|| >= |<Xi,q>|-||(1-P_I)Xi|| ||q||
             >= lambda sqrt(W0 delta) log(1/delta)[1-o(1)]

because lambda/[delta^(3/2) log(1/delta)] tends to zero for 0<alpha<2/3. Squaring proves the positive weight lower bound. This avoids assuming an isolated microscopic eigenvalue or identifying a resonance residue with a positive weight.

The nearest allowed Qy changes b by O(lambda^4); the binding law gives d log(delta)/db=O(log²(lambda)), so the actual coefficient gap remains lambda^alpha[1+o(1)]. One may use the actual mesh gap throughout the interval definition. The width J lambda delta exceeds the O(J lambda²) residual scale in this joint limit; constants remain fixed-order asymptotic constants, not a practical numerical tolerance certified for a laboratory lambda.

## 6. Assumptions that survive

The state restriction is the actual ground family of a supplied anisotropic Hamiltonian on these even growing cubes. The selected momentum and joint limit are still supplied, as are the physical interpretation of C_Q and lattice units. The mode's internal separation grows, while its weight shrinks and its excitation energy remains near8J. No cosmological initial state, emergent Lorentz invariance, long-range gravitational force, universal source/detector coupling or empirical particle identification has been derived. The result is an actual microscopic spectral contribution with a calculated overlap, not a complete scalar theory.
