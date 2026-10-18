# Eight-site feature-code native check

PASS for the kinematic isometry and for failure of native invariance of the particular numerical embedding produced in this replay. The embedding is not uniquely fixed by the six compressed ports; its dynamical diagnostics depend on choices inside degenerate eigenspaces. No general encoding no-go follows.

Read /tmp/neutral_feature_clifford_probe.py and replayed it with single-thread BLAS. Output is /tmp/neutral-feature-code-native-replay.json. Largest compression error is 1.60e−15 and isometry error 2.45e−15. No shared files edited.

## Analytic isometry and port map

The six Jordan-Wigner matrices obey {G_i,G_j}=2delta_ij I_8. For each sign vector s, A_s=sum_i s_iG_i/sqrt(6) squares to I, has trace zero and therefore has four eigenvalues of each sign. Let U_s contain an orthonormal positive-eigenspace basis. Its block U_s†/sqrt(32) has Gram (I+A_s)/64. Summing over all 64 sign vectors gives V†V=I. Weighting this sum by s_j gives G_j/sqrt(6). Thus compression of the six outcome-register Z operators is exactly the claimed Clifford generator, independently of each U_s basis choice.

The first six big-endian register bits index the sign vector, and the last two index the four block rows. The permutation uses every physical site once. With physical coordinates ordered lexicographically as (x,y,z), ports [0,7,4,3,2,5] lie respectively on x−,x+,y−,y+,z−,z+ faces, with axes [X,X,Y,Y,Z,Z]. The two remaining sites are [1,6]. HZH=X and (phase H)Z(phase H)†=Y, so rotating W, while leaving H fixed, maps each tested physical port observable to the desired original register Z. Face assignment is valid, though these are corner sites shared geometrically by several faces; the construction selects one port per designated face and establishes no face-normal localization beyond that choice.

## Native Hamiltonian and leakage

The code builds exactly four open bonds in each cube direction, with −XX, −YY, −ZZ respectively. H=lambda(Hx+Hy)+Hz is the supplied open 2×2×2 compass Hamiltonian with Jz=1 and positive transverse couplings. There are no periodic duplicate bonds, added code-projector terms or hidden interaction penalties. Local rotations change the chosen subspace W; they do not rotate or modify the Hamiltonian under test.

With h=W†HW and P=WW†, the residual is HW−Wh=(I−P)HW. Its operator norm vanishes exactly iff this subspace is H-invariant. In this replay its norms are 2.25497, 2.69405 and 3.79925 at lambda .1,.5,1. Hence this embedding fails invariance strongly in Jz units at all three sampled couplings. The norm describes the largest initial leakage amplitude rate over normalized code vectors; it does not bound every code state's leakage from below or directly give a long-time decay rate.

The code energy mean exceeds the mean of the lowest eight eigenvalues substantially, so this subspace is also not the lowest eight-state spectral subspace. The reported eighth/ninth gap is a property of H, not an error tolerance or protection gap for W. At lambda1 it is numerically zero (1.78e−15), so no isolated lowest-eight manifold is demonstrated there. Internal code spectral width alone says nothing about invariance or protection.

## Eigenspace gauge and scope

Each eigh positive eigenspace has a U(4) basis freedom, including arbitrary phases. Independently changing these bases changes the four ancilla output amplitudes conditional on the six register bits. It preserves all six compressed-port identities but generally changes P and therefore native leakage and energy diagnostics. Those numerical values are not invariants of the port POVM or Clifford algebra. In contrast, a single right-unitary reparameterization W→WU leaves P and the displayed spectral/leakage diagnostics unchanged.

The script reproducibly tests the basis returned by its current NumPy eigensolver, but does not define a platform-independent canonical embedding or search the admissible U(4)^64 freedom. If exact numerical values are to become frozen scientific data, save the resulting W (with a hash and conventions), or supply a deterministic explicit basis construction. Current assertions are legitimate for this particular generated embedding only; they are not established uniformly over that gauge family or unsampled couplings.

Finally, compression is not an algebra homomorphism: W†O_iO_jW need not equal (W†O_iW)(W†O_jW) for two ports in the same block. Physical ports on different sites commute even though their compressions anticommute, because projection discards leakage terms. Interactions between separately encoded blocks can factor under a tensor-product isometry, but autonomous effective Clifford dynamics still requires native subspace control. The probe is a useful kinematic construction plus a concrete negative dynamical test, not a no-go for all large-feature encodings, a protected code, or a derived many-feature Hamiltonian.
