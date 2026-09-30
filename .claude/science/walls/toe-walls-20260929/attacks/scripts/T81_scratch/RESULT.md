# T81 raw results (scripts in this folder; outputs A_out.txt, B_*.txt)

Provenance: Claude Sonnet 5.5, same-family checks.

A (exact/float arithmetic, A_certificates.py):
- block 30 T4 rows (4165,1,2) (2085,1,1) (8330,2,4) (6247,1,3): dominate exactly; eps1*Rbar = 7.69e-8, 7.24e-8, 7.69e-8, 6.48e-8 (< 1e-7).
- refinement-history H1 (probe a3): (84,1,2) sigma=161/5000 Zbar=5119922891/1e9 passes exactly; same triple fails at 83;
  optimum-sigma feasibility boundary p = 83.607; ceiling eps2 < 1/27 at p >= 57.02.
- block-30 tree recursion (float iteration): bounded from p ~ 4165-4170.

B (simulation, sim.py / scan.py; torus LxL, start all-a / all-zero; blow-up = dissent density > 0.9 (eta') or > 0.5 (actual)):
- eta' (dominating two-level automaton), L=128/256/384, T up to 12000:
  p=16 blow-up at ~300 levels (same at L=128, 256: not area-limited), 17 ~740, 18 ~2000 (8/8 blow up, L=256),
  19: mixed (3/8 at L=256, 2/3 at L=384), 19.25/19.5/19.75/20/22/24: ordered (rho~0.009, 4/4 at L=384, T=12000).
  => p*(eta') = 19 to 19.5 (finite size; may drift slightly up with L).
- actual six-state law, L=128 (T=3000) and L=192 (T=6000): p=10.5 blow-up (~500 levels); p=10.75 blow-up (3000-5000 levels, 3/3);
  p=11, 11.25 ordered (rho ~ 0.16, 0.12).  => p*(actual) in (10.75, 11].
- box with all-ones outside (boxbound.py): fills completely at every p in {25,...,150}, L in {8,...,64}.

Pre-registered readings: R-T holds (p*(eta') <= 30); sanity holds (p*(actual) in [8.5,13]).
