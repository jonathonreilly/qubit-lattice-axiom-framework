# Finite corner-code centrality and conditional quadratic identities

**Type:** bounded_theorem
**Status:** conditional-support; finite controls and supplied-model identities, without a physical scalar or interaction selection. No empirical data are used.

## Supplied model and actual premises

Use the graph and Pauli definitions of the [corner code](CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md). Its [fine-site embedding](CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md) distributes48 active qubits over125 fine sites with77 decoupled frozen spectators. These are supplied block constructions; no uniform fine-site Hamiltonian completion is asserted. The [native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) supplies the hopping/flux context.

The conditional Hamiltonian considered is `H = encoded(c† h c) + F(W,R) + H_spectators`, with commuting loop W and repetition R constraints, a constraint-preserving number-conserving quadratic lift and decoupled spectators. F depends on central constraints. Linear charge terms use B_i=1−2n_i; products B_iB_j are separate matter interactions. The full fine-site lift/locality bounds of a supplied one-particle matrix are not constructed by this note. Coefficients and physical state remain supplied.

## Finite centrality and syndrome certificate

The primary reads only the definition prefix of the current corner runner. At periodic L=4, flux bits1011, it constructs3072 qubits,768 vertices,2304 edges,2624 listed loops and768 distinct repetition constraints. Independent binary symplectic parity gives the following exact finite pair counts:

| Pairs | Tested | Anticommuting |
|---|---:|---:|
| loop/hop |6045696|0|
| loop/charge |2015232|0|
| repetition/hop |1769472|0|
| repetition/charge |589824|0|
| loop/repetition |2015232|0|

A selected charge anticommutes with its six incident hops, a positive control for nontrivial dynamics. Products and linear combinations inherit commutation with W/R. Other sizes require the matching graph-algebra argument or a separate construction; these exhaustive counts are L4 only.

For a joint constraint projector P, Q=1−P and [H,P]=0, multiplication gives PHQ=0. Consequently `PHQ(E−QHQ)^−1QHP=0` on the Q-space resolvent domain. This is a conditional operator identity; mechanism-exhaustion and all-orders physical exclusion interpretations are deferred.

All3072 single-Z probes have nonempty flux-syndrome columns. The2304 distinct columns form1536 singleton classes and768 classes of two, with maximal coarse-cell periodic Manhattan diameter1. The latter are paired repetition halves. These are finite combinatorial data. For involutions W_a commuting with rho and H, and W_a O_i W_a=s_ai O_i, trace conjugation gives `Tr(rho O_i(t) O_j)=s_ai s_aj Tr(rho O_i(t) O_j)` and the corresponding identity in reversed order. The state commutation hypothesis includes sector-diagonal mixtures; coherent off-sector preparations require a different argument. Transport exclusions and exhaustion of microscopic field channels are not promoted here.

## Quadratic and resolvent identities

Canonical anticommutation relations give `[c† A c,c† B c]=c†[A,B]c`. Unitary diagonalization of h expresses the free Fock Hamiltonian as a sum of occupation energies. Restricting to a fixed fermion-parity sector restricts the allowed occupations. An encoded physical subspace must be matched to that representation before interpreting these spectra. No Wick assumption on an arbitrary prepared state is needed for these operator identities.

For a low/high one-particle block split, when the high inverse and relevant full inverse exist, block Gaussian elimination gives `G_LL(z)=[z−h_LL−h_LH(z−h_HH)^−1h_HL]^−1`. The effective matrix depends on z. These algebraic statements do not establish a physical scalar action, pole normalization or coupling. No-new-interaction and universal representation exclusions from the original are deferred.

The runner checks the commutator identity, additive two-particle energies and Schur formula on an explicit four-mode fixture. These numerical controls test the identities; they are not a corner-model spectrum or an infinite-volume result. It also checks a direct-sum sector projector and an explicitly added .37 density interaction as controls. Fresh errors are reported in the output, without treating older printed floating values as new evidence.

## Explicit diagnostic density family

Consider only as a diagnostic `H_V=H+V sum_edges n_i n_j`, with `n_i n_j=(1−B_i)(1−B_j)/4`. Each added term acts as zero on vacuum and one-fermion states. For real V it is a Hermitian finite-range encoded operator commuting with the loop/repetition constraints. Uniform summation preserves the supplied graph's charge-permuting rotations/translations and number twist; this is a statement about block geometry, not fine-site translation symmetry.

On the full two-particle Fock sector, for V>0 the sum is positive semidefinite with positive trace on a nonempty graph, so its trace contribution is strictly positive. The four-mode control separately exhibits a shifted two-particle spectrum. Neither V nor this term is adopted into the working theory. Interpretations as an identifiability obstruction or a completed route exclusion remain in historical recovery rather than the live claim.

## Reproduction and boundaries

Primary: `python3 scripts/microscopic_flux_interaction.py`. Fresh output: `outputs/microscopic_flux_interaction/result.json`. The14 checks test finite Pauli enumeration, an added electric positive control, syndrome data, finite Fock/Schur identities and an added density control. Five resolution summaries distinguish executed finite controls from supplied/general statements. These checks do not establish a selected microscopic Hamiltonian, physical state, bulk scalar or cosmological/source-detector coupling.

All16 original path versions, including original arguments, independent check sources and failed/old authority narratives, remain recoverable through `archive/microscopic_flux_review_2026_10_18/MANIFEST.json`. Negative promotions require their own honest N1–N8 completion; no count of nominal routes is substituted for that work. This note applies no audit verdict.
