lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T06:34Z

# Gate: Lemma EX and Lemma EX2 (`library/sector-values.md` 3A, 3B), SU(2), d = 4

Pinned at 7c12c6981. Mapped-side firewall observed. In progress.

Working notes, replaced by the final report: criteria are in `checks/gate_ex/CRITERIA.md`, registered before any run. Solver: true constrained SU(2) minimiser in d = 4 (`checks/gate_ex/ex_core.py`), comb block map, passes V1 (covariance 8e-16) and V3 (abelian e/E against Fourier: 1.45466 v 1.45455, 0.80007 v 0.80000, 1.84937 v 1.84919). Running: constant non-commuting links.

Reduction noted by hand: for W = 1, V^*(V') lies in the fibre of V', so e_j(V') >= e^(1)(V') for every j, with the same f, E, I. So the unweighted Lemma EX at all levels follows from the one-level statement. Only the weighted form and Lemma EX2 can depend on the level.
