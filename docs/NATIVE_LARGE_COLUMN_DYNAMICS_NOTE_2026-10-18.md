# Exact internal dynamics and large-column tunneling

**Type:** bounded_theorem

**Status:** conditional-support with exact finite coordinate and symmetry identities; unaudited.

Runner: [native_large_column_dynamics.py](../scripts/native_large_column_dynamics.py). Detailed derivations: [internal factorization](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/EXACT_INTERNAL_FACTOR.md) and [large-column process](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/STRONG_COLUMN_FEATURE.md).

The supplied one-qubit compass Hamiltonian can be rewritten exactly on each positive-parity four-site rung as a protected two-state coordinate coupled to a four-state internal coordinate. These are tensor factors of existing states, not additional physical qubits. The internal Hamiltonian is -IZ-XI-YY-ZX and the original longitudinal operators become YZZ, XIY, -ZYZ, -IXY. The identity holds at every interaction ratio. The internal ground expectation of each vertex is zero, yet virtual internal excitation generates the previously derived collective XY exchange. An independent symbolic projector contraction fixes its coefficient without adding an interaction.

A complementary limit produces a genuinely large feature: two aligned columns of L physical sites. Their reversal first occurs at transverse order L, with amplitude

-Jperp^L/(2Jz)^(L-1)

for open longitudinal boundaries and small Jperp/Jz. A minimum-spin-flip argument identifies every contributing path; an explicitly derived Ising/Majorana subproblem proves the coefficient for every finite L. Exact rational subset sums check L2..16. Physical Y-edge phases retain an even/odd length dependence. Native finite spectra at L2..5 approach the resulting eight-state band spectrum as the ratio decreases. No uniform-size or equal-coupling control is claimed.

The readout test changes the interpretation. On this aligned band, plane and square symmetries have a commutative invariant-operator algebra. The uniform longitudinal neutral composite and H therefore commute within any isolated symmetry-preserving continuation of the band. Its small tunneling splittings cannot appear as intraband inelastic poles in that scalar readout. This does not exclude transitions out of the band, other observables, or the broader neutral-composite route. For odd L, plane neutrality alone is insufficient; square invariance is essential to this statement.

The independent algebra checks pass, and numerical inelastic weights are consistent with the exact selection rule. All calculations are exposed model development. Geometry, microscopic H, parity, anisotropy, state and physical identification remain conditional. A separate frozen32site diagnostic in the detailed internal note finds substantial internal excited-state probability at equal coupling; it is not reproduced by this self-contained runner and is not used in the exact proofs. No observational fit, cosmological bridge or TOE closure is claimed.

The next constructive route is the neutral domain-wall excitation band above these aligned states, where original bonds generate both motion and inter-feature effects. The low-band readout obstruction does not cover that band.
