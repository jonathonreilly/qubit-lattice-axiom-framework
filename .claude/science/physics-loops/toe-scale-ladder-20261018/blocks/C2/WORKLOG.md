# C2 worklog

- 18:50Z: Read SCIENCE_WORKFLOW §2, SCALE_LADDER_MAP C2, MINIMAL_AXIOMS_2026-06-29, SCALE_REFERENCE_PRIMITIVE_NOTE, KINETIC_ISOTROPY_PRIMITIVE_NOTE + registry node + irreducibility support, two-qubit Dirac walk note, Gaussian comparator note (10-01), and the prior Lorentz-RG notes (attractor 06-06, exchange matrix 06-18, B4 06-08, Poincaré free sector 06-09, naturalness gap 06-06). Found that the strict-license note scopes kinetic isotropy to "Matter sector only" and lists gauge plaquette anisotropy as a separate row. That fixes the K_m versus K_full split.
- Exploratory: did the fermion self-energy angular reduction by hand. The sympy shell integral gives `F = (eta^3+2eta^2+eta-4)/(6pi^2(eta+1)^2) = [eta - 4/(1+eta)^2]/(6pi^2)`. Checked that the Coulomb limit gives 2α_C/3π.
- Literature: arXiv and ar5iv are unreachable (DNS/403). A web search confirmed that Isobe–Nagaosa PRB 86 165127 exists and its abstract summary says c²v is almost unrenormalized; my flow reproduces that stationarity. Explicit coefficients were not compared.
- Runners:
  - witness_supplied_ingredients: the first run failed one check because the b0 scan range included points with no det G root (0.30, 0.43). Narrowed to [0.33, 0.40], which are all admissible, and added a monotonicity check: 10/0.
  - witness_os0_surface: replaced the diag-metric proxy with a direct plaquette-weight invariance test: 13/0.
  - rg_one_loop_analytic: 14/0.
  - rg_independent_numeric: run 1 failed 4 checks at ~2e-4 relative. The cause was IR truncation of the radial quadrature (ln r ≥ -4; the sanity integral was itself off by 1.9e-4). Extended to [-8, 4] with the tolerance unchanged: 11/0. The run-1 log is kept.
- run_all: TOTAL PASS=48 FAIL=0.
- Load-bearing step for independent review: the sign and normalisation of the fermion speed flow (`K_eff = K - Sigma~`), which both RG scripts share. A reviewer should redo it with a different convention, e.g. a Minkowski Hamiltonian / Hartree–Fock route, or by comparing with Isobe–Nagaosa's explicit equations.
- Review pass: applied every REVIEW.md finding to NOTE.md (§9 maps each finding to its fix). Added a runner check for the proper-O invariant counts (2, 3). Checked the e²δ²/(24π²) drift against my closed form. run_all: TOTAL PASS=49 FAIL=0.
