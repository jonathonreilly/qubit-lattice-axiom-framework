# F1 check C1 — pre-registration (written 2026-10-14 13:39Z, before running)

**Question.** On the framework's two free carriers —
(S) the 3D Hamiltonian staggered field, one complex mode per site, K2a conventions
(`candidate-law-20261008/checks/k2a_selector_momentum_space.py`), and
(W) the site-qubit walker H = Σ_a σ_a sin p_a (two complex modes per site) —
which exact lattice translations act on the IR Weyl content as a Spin-Z4 generator
(g² = (−1)^F on the zero modes, either directly or after multiplying by i^F, which
needs fermion number conserved mod 4), and what is the Z16 index
ν_g = Σ_(left-handed Weyl) q_g (mod 16), q_g ∈ {±1}, on

1. the whole carrier (an LSM-type lattice anomaly if nonzero);
2. candidate mirror sectors:
   - (S) K2a split: mirror = one Weyl chirality at K = 0 (2 Weyl per field);
   - (W) "three generations" split: light = hw=1 corners, mirror S = {hw0, hw2, hw3};
   - (W) chirality split: mirror = {hw0, hw2}.

for internal multiplicity d ∈ {1, 2, 4, 8, 15, 16}?

**Fixed readings.**
- **INVALID** if the control fails: the whole staggered carrier must give |ν_Z| = 4 per field mod 16
  (reproducing the known "multiples of four staggered fields" count: Catterall–Pradhan(–Samlodia)
  arXiv:2501.10862; TW-3 report `C5_TW3_report.md:31,203-205`).
- **COUNT-16** if, for every candidate mirror sector, every ν_g vanishes mod 16 at d = 16 and at least one
  fails at d = 15. Reading: a translation-preserving mirror gapping on the native carrier needs ν_R
  (16 per generation); the mod-16 gate passes for 16 and is not what blocks the route.
- **COUNT-OBSTRUCTS** if some ν_g on a candidate mirror sector is nonzero mod 16 at d = 16
  (name g and the sector): the route as constructed is anomaly-obstructed.
- Report separately whether each obstruction needs Z4^F (fermion number mod 4) or only (−1)^F.

**Scope.** Necessary conditions only (one cyclic Spin-Z4 subgroup at a time; mixed anomalies with time
reversal, Spin(10) or non-abelian translation structure are not computed). A pass is not existence of a
symmetric gapped phase.
