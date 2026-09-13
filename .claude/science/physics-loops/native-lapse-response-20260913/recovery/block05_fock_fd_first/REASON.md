# Resolved finite-difference failure

The first three-cell checker failed its absolute2e-6 comparison at lambda=-20
in the fixed three-particle sector. Its five-point step0.001 differed from
the spectral Kato Hessian by3.7722e-6. Source and stderr are preserved here.

The separate45-digit diagnosis in CONVERGENCE.json gives arithmetic residuals
3.766297e-6,2.355046e-7,1.472077e-8 at steps0.001,0.0005,0.00025. Congruence
residuals have the same factor16 convergence. This resolves the mismatch as
the stated fourth-order finite-difference truncation, without changing the
Hamiltonian, source formula or tolerance. The primary uses step0.0005 for
the two magnitude20 probes. Its diagnostic reads the archived failed source,
not a moving future primary. No interacting infrared result is inferred.
