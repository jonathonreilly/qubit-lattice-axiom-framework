lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T06:34Z

# Gate: Lemma EX and Lemma EX2 (`library/sector-values.md` 3A, 3B), SU(2), d = 4

**Provenance.** Model anthropic/claude-opus-5-5, effort high, commit 7c12c6981, mapped side. A same-model check is not independent in model and is not an audit. Verdicts steer research and grant no status. DRAFT: sections below are being filled; numerics still running, verdicts provisional.

## Established so far

Criteria were registered before any run: `checks/gate_ex/CRITERIA.md`. Solver: true constrained SU(2) minimiser in d = 4, comb block map (`checks/gate_ex/ex_core.py`). V1 covariance 8e-16. V3 abelian e/E against Fourier: 1.45466 v 1.45455, 0.80007 v 0.80000, 1.84937 v 1.84919.

Reduction R1 (proved here): for W = 1, V^*(V') lies in the fibre of V', so e_j(V') >= e^(1)(V') at every j with the same f, E, I. The unweighted Lemma EX at all levels follows from level one.

X1, X3, X4 on constant links: no violation. sup C_eff (N' = 1, L = 3, three seeds agreeing to four digits) = -0.401, -0.386, -0.379 at f = 0.08, 0.032, 0.0128. X6: c_e = (1/9)(1 - L^-2) at L = 3, 5 by optimiser, infimum at P -> 0 along (1,1,1,0).

Numerics paused at the 50 percent memory gate at 20:50Z; free memory 48 to 49 percent, held by processes that are not this job's.
