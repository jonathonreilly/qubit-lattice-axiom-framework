# Two neutral features and their original-source ladder

**Status:** bounded-support.
**Primary runner:** [scripts/native_two_feature_ladder.py](../scripts/native_two_feature_ladder.py)

The supplied one-qubit Hamiltonian and its original distance-two ZZ readout produce a first two-step excitation ladder in a specified weak-coupling limit. No oscillator, new interaction or adjustable source coefficient is added. The result concerns vectors in actual microscopic energy windows, not isolated eigenstates or stable particles.

Take even cubes with L proportional to lambda^-4 and the previously derived neutral bound feature with binding gap delta=lambda^alpha, 0<alpha<2/3. Select an allowed nonzero momentum near its threshold, using even COM mesh indices. For every actual ground vector, there are normalized vectors psi1 and psi2 in windows centered at J(8+lambda E) and J(16+2lambda E), respectively, with half-width J lambda delta/4. Their original-readout matrix elements satisfy

    |<psi1,C_Q ground>| ~ lambda sqrt(W0 delta) log(1/delta),
    |<psi2,C_Q psi1>|   ~ sqrt(2) lambda sqrt(W0 delta) log(1/delta),

where W0 is the previously derived coefficient, approximately .02574494410. The construction carries momentum transfers Q and 2Q relative to the ground. For a translation-eigenstate ground these are definite shifted momenta; for a coherent ground superposition no definite absolute momentum is asserted. These are existence statements for window vectors; they do not assert a unique field operator or a full bosonic Fock space.

## Derivation and decisive controls

The [combined proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_LADDER_PROOF.md) constructs the two-feature trial from products of native spin-lowering strings. An explicit eight-wall projection removes touching strings whose wall count fails to add. The projected native Hamiltonian acts additively away from contact; uniform translation and polynomial configuration-factorization counts bound the contact residual by O(V^-1/2). All fixed higher-order local coefficients have bounded action because the interval-length moments remain bounded even as transverse extent diverges.

The [spin calculation](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_SPIN_ALGEBRA.md) gives an exact hard-core correction to the two-pair norm. Full-string normalization tends to 2. Polarization of that identity gives the mixed source matrix element; flip-count selection eliminates the dangerous terms linear in the small long-interval component. The actual dressed source differs from its vacuum pair-creation extension only near the existing feature, with an explicitly bounded contact correction. This extension is a chosen mathematical representation, not a newly postulated physical interaction.

The [low-energy source bound](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/LOW_ENERGY_SOURCE_BOUND.md) proves ||C_Q P_low||=O(lambda), including its adjoint. This bound transfers the vertices to actual microscopic windows with error O(lambda^2/delta). Relative to the fading source amplitude, that error vanishes for alpha<2/3. Using the extensive global source norm here would not suffice.

The runner checks complex spin-pair identities, exact separated/contact projected-Hamiltonian actions on 432 physical bits, and the original dressed-source contact correction on 128, 256 and 384 physical bits. These are local configuration calculations, not full Hilbert-space diagonalizations or proofs of asymptotic estimates by numerical fitting. Independent algebra, Hamiltonian, source and low-energy-bound checks are preserved with the proof.

## Surviving assumptions and limits

The Hamiltonian, weak-coupling regime, ground preparation, selected momentum and growing-volume family remain premises. The large transverse feature contains two coherently separated flips; it is not yet a many-constituent fermion. Its energy remains near 8J, its motion is anisotropic, and its source strength fades near threshold. Two-feature states can overlap other breakup channels. Arbitrarily many rungs, finite-density stability, scattering amplitudes, lifetimes, a relativistic scalar, physical units and the cosmological/source-detector bridge remain open.

All numerical cases are exposed model development. No observed value was fitted and no independent observational test was performed. Composite normalization and entanglement are known prior-art themes: [Law](https://arxiv.org/abs/quant-ph/0411040) and [Tichy, Bouvrie and Molmer](https://arxiv.org/abs/1308.2896). Those works provide context, not a proof of this native-spin result.
