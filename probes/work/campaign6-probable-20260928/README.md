# Campaign 6 (2026-09-28): probable work deferred to the backlog

Owner rule (2026-09-26): only validated science that moves the program forward goes into a PR; probable work goes on this backlog.

## 1. The ring component's energy per plaquette falls with the torus in the projector

The fixed-population projector (guide exp(0.2 N_flip), 960 walkers, resampling interval 0.015) gives energies per plaquette
u = 0.2885 (8^3), 0.2880 (12^3, 3840 walkers), 0.2868 (16^3), 0.2854 (24^3). Reptation (no population) gives 0.2932, 0.2893, 0.2886
on 4^3, 6^3, 8^3 (roughly a 1/L^4 approach), so a size-independent value near 0.2885 was expected. Checks that do NOT remove the
16^3 offset of -0.0017:
- population: 960 -> 3840 walkers moves u by +0.0004 (open PR 9358); 24^3 960 -> 1920 by +0.0004 (open PR 9365);
- projection time: [7.5, 30) vs [30, 60) moves u by +0.00006 (open PR 9369);
- per-generation weight spread: effective walker fraction 0.99 / 0.97 / 0.94 on 8^3 / 12^3 / 16^3 (`ess_probe.py`);
- starting state: canonical-state start and loop-VMC start agree (0.28682, 0.28678 vs 0.28691, 0.28683; `comp_probe.py`).
Open: a real size dependence of the zero-winding flip component, or a bias none of these probe (for example the guide's
long-wavelength content). A population-free value on 12^3 or 16^3 would decide it.

Added later on 2026-09-28/29:
- resampling interval: 0.015 -> 0.005 moves the 16^3 u by -0.00006 (open PR 9378);
- 24^3 projection to 60: u moves by -0.00004 (open PR 9372);
- population-control correction (`pc_probe.py`, the projector's product-of-mean-weights window Lc): on 16^3 (960 walkers, seeds 401,
  402) u rises from 0.28664/0.28665 (Lc 0) to 0.28736/0.28750 at Lc = 40 (0.6 time) and falls back to 0.28663/0.28696 at Lc = 640;
  on 8^3 the change is at most +0.0002. Non-monotone and short of 0.2883, so not a clean explanation.
- lineage collapse: the per-generation spread of the log mean weight is 0.0096 on 8^3 and 0.060-0.071 on 16^3 (about 7x, where
  volume scaling alone gives about 2.8x), and forward-walking lineages on 16^3 collapse to under 1% distinct ancestors by lag 1
  (open PR 9382). An effective population far below the walker count on 16^3 and larger tori is the leading suspect; a sampler with
  less weight spread (a better guide, or smaller branching noise) would test it.

## 2. Comparator touchings for J_x != J_y

For J_x = J_y the touchings lie on three closed-form families (open PR 9350). For J_x != J_y the line nodes (x, 1 - x, 0) persist,
but the four extra nodes leave both planes (J = (1, 0.8, 1), kappa = 0.45: (0.22300, 0.68644, 0.25024) and images; J = (1.2, 0.8, 1),
kappa = 0.3: (0.25506, 0.58995, 0.04264)), and no cosine combination tested is algebraic of degree <= 4 (`kc_aniso3.py` builds the
exact determinant with separate J_x, J_y, J_z). Existence therefore needs a topological or interval-Newton certificate (for
example Krawczyk on three independent 3x3 minors, or a certified chirality sum on a box boundary) instead of exact positions.
