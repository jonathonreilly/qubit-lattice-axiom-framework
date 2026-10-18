# The native grid selects internal fluctuations, not a protected uniform spin

**Status:** bounded-support.
**Primary runner:** [scripts/native_isotropic_collective.py](../scripts/native_isotropic_collective.py)

At equal native couplings, a large uniform-spin feature looks deceptively promising: projecting the one-qubit Hamiltonian onto total spin N/2 gives exactly -JN times the identity. The full calculation shows why this projection cannot supply a scalar mode by itself.

For every state in that symmetric sector, including entangled symmetric states, the Hamiltonian's leakage norm is at least asymptotically J sqrt(4N/3). On growing periodic grids with even Lx>=4, a native entangled-pair trial lowers the energy to -17JN/16. In that family these facts imply that every actual ground state's weight in the symmetric sector is O(1/N). Increasing the number of sites therefore does not make this particular collective description valid.

The calculation also derives where the first fluctuation goes: exactly into total spin N/2-2. Around the z-polarized state its spatial pair coefficient is cos(ky)-cos(kx), obtained from the existing XX and YY interactions. No oscillator or new coupling is inserted. This coefficient vanishes quadratically at small momentum; the norm in a small symmetric momentum ball scales as J²N kappa^7/(105 pi²). This is an initial fluctuation diagnostic, not a scalar dispersion or lifetime.

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_COLLECTIVE_PROOF.md) gives the exact quartic leakage operator, both norm bounds, variational energy, ground-weight bound, first fluctuation channel and local short-time magnetization. The runner checks native H actions on low-excitation Dicke vectors on 27 physical sites, coherent-state amplitudes, the pair trial and Fourier integral. It does not perform a full 27-qubit diagonalization.

This rules out supplying protection merely by choosing a large fully symmetric feature. It leaves spatially structured lower-spin features and entangled collective phases open. The Hamiltonian and isotropic parameter choice remain assumptions; no empirical data or physical unit identification enter. The known quantum compass model is studied in [Oitmaa and Hamer](https://arxiv.org/abs/1010.3804); their high-temperature results are context, not a ground-state theorem imported into this calculation.
