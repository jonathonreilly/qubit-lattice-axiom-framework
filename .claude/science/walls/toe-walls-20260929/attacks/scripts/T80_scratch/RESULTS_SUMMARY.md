# T80 scratch summary (Claude Sonnet 5.5; same-family checks)

Files: PREREGISTER.md (with two addenda written after partial results), vacgas.c / vacgas2.c (heat-bath MC; vacgas2 adds the helicity modulus),
validate_small.py (exact enumeration of the 2x2x2 two-valued gas and an independent Metropolis for the sphere menu), exact_checks.py (E1 loop-gas identity,
E2 counting identity, E3 mass-channel finite difference, MC-C closed forms; output exact_checks.out), rate_vs_blind.py (c0 formation-rate spread),
analyze.py (Binder tables from results_A1.csv), collapse.py (collapse.out), stiffness.py (stiffness.out), proofgap.py (proofgap.out),
results_A1.csv / results_DE.csv / outF/ (raw MC rows; columns: menu L beta z g c rho var(N) kurt(rho) m2 m2err U Uerr cold).

Deviations from the pre-registration (honest list)
- L = 16 was dropped (machine load 30-50); all crossings use L = 8 and 12.
- MC-D and MC-F were added after the first ~55 rows were read (addenda say so).
- Pre-registered matched points rho = 0.90 (and 0.95 at beta 1.5) could not be evaluated for the c = 1 family: it has no ordered state below rho ~0.93 (density gap 0.29 -> 0.98 at beta 1.5, z 0.2 -> 0.4). The comparison was made at every matched rho where both families are ordered (0.934-0.998).
- z = 1 (neutral): the Binder crossing method fails because the transition is a steep density jump (rho 0.585 at beta 1.3 -> 0.82 at 1.4); hot and cold starts agree at all four betas.
- Not tested: moving-record kinetics (only the equilibrium of the supplied static law with annealed contents), lower densities (rho < 0.9) beyond the phase-boundary scan, other menus (six-axis), sizes above 12.
