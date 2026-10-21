# Exact collective-spin compression and native internal fluctuations

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_isotropic_collective.py](../scripts/native_isotropic_collective.py)

At equal native couplings, a large uniform-spin feature looks deceptively promising: projecting the one-qubit Hamiltonian onto total spin N/2 gives exactly -JN times the identity. The full calculation also determines the coupling outside this projected sector.

For every state in that symmetric sector, including entangled symmetric states, the Hamiltonian's leakage norm is at least asymptotically J sqrt(4N/3). On growing periodic grids with even Lx>=4, a native entangled-pair trial lowers the energy to -17JN/16. In that family these facts imply that every actual ground state's weight in the symmetric sector is O(1/N). These estimates concern this specified symmetric sector and ground-state family.

The calculation also derives where the first fluctuation goes: exactly into total spin N/2-2. Around the z-polarized state its spatial pair coefficient is cos(ky)-cos(kx), obtained from the existing XX and YY interactions. No oscillator or new coupling is inserted. This coefficient vanishes quadratically at small momentum; the norm in a small symmetric momentum ball scales as J²N kappa^7/(105 pi²). This is an initial fluctuation diagnostic, not a scalar dispersion or lifetime.

The proof (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9781/ISOTROPIC_COLLECTIVE_PROOF.md`) gives the exact quartic leakage operator, both norm bounds, variational energy, ground-weight bound, first fluctuation channel and local short-time magnetization. The runner checks native H actions on low-excitation Dicke vectors on 27 physical sites, coherent-state amplitudes, the pair trial and Fourier integral. It does not perform a full 27-qubit diagonalization.

The exact compression and fluctuation estimates apply to the specified maximal-spin chart. It leaves spatially structured lower-spin features and entangled collective phases open. The Hamiltonian and isotropic parameter choice remain assumptions; no empirical data or physical unit identification enter. The known quantum compass model is studied in [Oitmaa and Hamer](https://arxiv.org/abs/1010.3804); their high-temperature results are context, not a ground-state theorem imported into this calculation.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.

The exact collective-spin compression, leakage operator, finite-size inequalities, variational energy and conditional ground-weight estimate remain live mathematical results. Their use as a terminal exclusion of a physical scalar route is deferred pending the required negative-claim packet; the package does not exclude spatially structured or dressed sectors.
