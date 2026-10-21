# Exact internal dynamics and large-column tunneling

Claim type: bounded_theorem.
Primary runner: [native_large_column_dynamics.py](../scripts/native_large_column_dynamics.py).


**Type:** bounded_theorem

**Status:** conditional-support with exact finite coordinate and symmetry identities; unaudited.

Runner: [native_large_column_dynamics.py](../scripts/native_large_column_dynamics.py). Detailed derivations: internal factorization (`outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/EXACT_INTERNAL_FACTOR.md`) and large-column process (`outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/STRONG_COLUMN_FEATURE.md`).

The supplied one-qubit compass Hamiltonian can be rewritten exactly on each positive-parity four-site rung as a protected two-state coordinate coupled to a four-state internal coordinate. These are tensor factors of existing states, not additional physical qubits. The internal Hamiltonian is -IZ-XI-YY-ZX and the original longitudinal operators become YZZ, XIY, -ZYZ, -IXY. The identity holds at every interaction ratio. The internal ground expectation of each vertex is zero, yet virtual internal excitation generates the previously derived collective XY exchange. An independent symbolic projector contraction fixes its coefficient without adding an interaction.

A complementary limit produces a genuinely large feature: two aligned columns of L physical sites. Their reversal first occurs at transverse order L, with amplitude

-Jperp^L/(2Jz)^(L-1)

for open longitudinal boundaries and small Jperp/Jz. A minimum-spin-flip argument identifies every contributing path; an explicitly derived Ising/Majorana subproblem proves the coefficient for every finite L. Exact rational subset sums check L2..16. Physical Y-edge phases retain an even/odd length dependence. Native finite spectra at L2..5 approach the resulting eight-state band spectrum as the ratio decreases. No uniform-size or equal-coupling control is claimed.

The readout calculation constructs the commutative plane-and-square invariant algebra on the aligned band for both length parities. For its isolated equivariant spectral projector P, PHP and POP belong to that algebra. O need not preserve the band. The separate terminal intraband inelastic exclusion is preserved with its full compression proof and hypotheses as deferred scientific source pending its promotion packet; it is not an active promoted conclusion here. The odd-length plane-only algebra remains noncommutative, so the square action is essential to the displayed constructive algebra.

The finite algebra and numerical readout controls retain their explicit matrices and measured weights. All calculations are exposed model development. Geometry, microscopic H, parity, anisotropy, state and physical identification remain conditional. A separate frozen32site diagnostic in the detailed internal note finds substantial internal excited-state probability at equal coupling; it is not reproduced by this self-contained runner and is not used in the exact proofs. No observational fit, cosmological bridge or TOE closure is claimed.

The next constructive route is the neutral domain-wall excitation band above these aligned states, where original bonds generate both motion and inter-feature effects. The low-band readout obstruction does not cover that band.

## Source and promotion boundary

The protected/internal factorization, finite tunneling coefficient and invariant-algebra calculation are constructive results. For the isolated equivariant band projector P, the compressions PHP and POP lie in the same commutative symmetry algebra. O need not preserve the band. Promotion of the resulting distinct-energy intraband exclusion is packet-pending; out-of-band and degenerate transitions remain allowed.

Full supporting mathematics and provenance are indexed in `outputs/neutral_composite_continuation_review_2026_10_18/INPUT_CLOSURE.json`. The scope register is `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. The primary binds literal source/input identities, stages owning-head helpers and frozen inputs in a temporary directory, and captures their diagnostics. Frozen expensive producers are provenance only and are not rerun. Historical reports and executions do not supply a fresh verdict.

The supplementary `stationary_2x2x8_plus.npz` is unavailable. Its derived occupation JSON is historical context, not a reproduced calculation or premise of the exact proofs.
