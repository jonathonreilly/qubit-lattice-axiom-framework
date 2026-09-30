# T01 test results (Claude Sonnet 5.5; same-family check)

Files: PREREGISTER.md (written before runs), x_checks.py/x_checks_results.json (exact), sim.c + analyze.py
(Monte Carlo), local_report.out, chi_report.out, phase_report.out, v1.out (validation), lemmaB_star.out.

V1 (plaquette MC vs exact, 8e7 samples): A 0.24854 vs 0.248543; E 0.249683 vs 0.249676; U 0.249045 vs 0.249029. PASS.
V2 (static heat bath): s = 0 within noise at all sizes; Q crossing p_c = 3.671 (L6/8), 3.666 (L8/12) in (3.5,3.8). PASS.

Local test (3,1,2), d=3 torus, L=12 (n=1e5): a1 U=0.244731 E=0.246495 A=0.243709 S=0.266717.
  U-E = -0.001765 (73 sigma), U-A = +0.001022 (40 sigma), U-S = -0.021986 (779 sigma).
  L=6 -> 12 ratio of U-E: 1.03; of U-A: 0.97. No decay. PASS (pre-registered).
  (5,2,4): U-E -0.000776 (30 sigma), U-A +0.000470 (19 sigma). (7,3,5): -0.000877 (35 s), +0.000528 (20 s).
  Calibration score s: U -0.0276, E -0.0248, A -0.0290, S 0.0000.

Phase test on (p,1,2), L = 8,12,16: NO crossing for U or E (Q stays at the Gaussian 5/3 up to p=20).
  chi = N<|m|^2> is L-independent for U and E at every p up to 1000; saturates at 17.4 (U) and 35 (E).
  Static orders at p_c = 3.67 (chi grows like L^3). The pre-registered crossing comparison of p_c(U), p_c(E),
  p_c(A) could not be evaluated (no crossings); reported as a deviation.
