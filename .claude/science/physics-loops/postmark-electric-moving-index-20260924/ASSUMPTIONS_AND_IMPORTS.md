# Assumptions and imports

The proof candidate is conditional on the supplied six-site one-vacancy construction and its 15-residue integer-spin link table in `docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md` and `docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md`. Their exact main-revision hashes are pinned in the scientific notes and runners; current main at campaign start was `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`.

| Input | Status | Consequence if absent or changed | Check |
|---|---|---|---|
| Integer-spin path (I_S=[-5S,5S-4]) and hop factors | Supplied condition | Changes the Jacobi coefficients, path reflection, and asymptotic estimates | Exact coefficient reconstruction in paired runner; source hash pin |
| First-mark preparation \(|0\rangle\) in the selected winding component | Supplied physical identification | Changes initial spectral amplitudes and the scalar (q_S) | Upstream fast-vacancy and zero-mode notes |
| Generator (G_S=N_S^2-CN_S), (C=S(S+1)) | Supplied dynamics plus exact algebraic reduction | Changes the fast phase (tCN_S) and prepared profile | Small dense exponential check and exact factorization |
| Period-three readout (O=(I+V+V^*)/3) | Supplied observable | A different readout selects a different Fourier mode | Exact projector-character identity in runner |
| Integer (S\to\infty), fixed (t=1/4) | Target domain | Shrinking-time or moving-time results do not answer the question | Goal contract |
| Strong profile \(\eta_S\to\eta_\infty\) | Proved upstream at fixed time; strengthened here to explicit (O(S^{-2})) bound | Without it, scalar reduction has only qualitative (o(1)) error | Weighted tridiagonal difference estimate and Duhamel proof |
| Jacobi spectral theorem, Fourier Parseval, Cauchy contour shift, Duhamel formula | Standard mathematics under their stated hypotheses | Omitted hypotheses could invalidate quantitative bounds | Full proof in exact-side note; finite dense checks corroborate identities |

The four framework axioms and registered primitives do not supply the quantum state space, this Hamiltonian, its spin realization, or this preparation. No import is retired, and no axiom or primitive change is proposed on present evidence.
