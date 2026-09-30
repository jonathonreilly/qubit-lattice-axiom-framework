# T48 pre-registration (written before any test script was run)

Attacker: Claude Sonnet 5.5 (same vendor family as supervisor). Date 2026-09-29.

Wall: one flavour carrier for lepton masses, quark masses, small CKM, large PMNS.
Known before testing (read from repo): shared-C3 circulants commute => CKM is a permutation
(NP-CKM note); the repo already says theta_C, theta_13 are C3-breaking order parameters and that
the GST texture (sin theta = sqrt(m_l/m_h)) is the residual; the sieve note keeps two operators on
the triplet: corner-diagonal mass M and C3 coupling K = |K|(J-I).

Route under test (R1): the two "mechanisms" are two factors of one object, a SHARED seed on the
triplet plus SECTOR-DEPENDENT diagonal weights (the only thing allowed to differ between u, d, e, nu is
the diagonal, i.e. the masses). Two forms:
  (mult) M_s = D_s R D_s, R a sector-independent Hermitian unit-diagonal seed, D_s positive diagonal,
         eigenvalues of M_s (in absolute value) = m_s^p.  [GST / Froggatt-Nielsen form]
  (add)  H_s = diag(m_s^p) + kappa K0, K0 = circulant with zero diagonal, off-diagonal b = e^{i phi} (phi=0 is J-I).
         [the sieve note's mass + K, with one universal kappa]
Inputs used only as comparators: rounded running quark/lepton masses (two scheme sets), p in {1, 1/2},
repo's CKM comparators |V_us|=0.22500 |V_cb|=0.04210 |V_ub|=0.00370 J=3.08e-5, theta_e = 12.16 deg
(THETA13 note: sin theta13 = sin theta_e/sqrt2 with sin^2 theta13 = 0.0222).

## Test A (mult form, quarks): does a C3-symmetric seed reproduce CKM?
A1 unconstrained seed R (|R12|,|R23|,|R13|, one phase; 4 unknowns for 4 observables): solve exactly.
   Reading: C3-symmetric iff |R23|/|R12| and |R13|/|R12| both within [0.75, 1.33].
   PASS (route survives at this step): both ratios inside the window for at least one of the
   4 (mass set, p) combinations.  FAIL: outside in all 4.
A2 circulant seed R (R12=R23=R31=rho e^{i phi}; 2 unknowns): minimise the worst relative error over
   (|V_us|,|V_cb|,|V_ub|) and J (J compared on log scale).
   PASS: worst error <= 25% for |V| and factor 2 for J in at least one combination.
   FAIL: worst error > 50% in all 4 combinations.
A3 lepton prediction: with the seed fixed by A1 or A2, compute the charged-lepton 1-2 rotation theta_e
   from D_e (masses e, mu, tau). PASS: within 25% of 12.16 deg. FAIL otherwise.

## Test B (add form): one universal kappa
B1 fit kappa (phi=0 and a scan of phi) to |V_us| with quark masses; predict |V_cb|, |V_ub|, J.
   PASS: |V_cb| within 30%, |V_ub| within a factor 2.  FAIL otherwise.
B2 with that kappa, predict the charged-lepton rotation theta_e (from e, mu, tau masses).
   PASS: within 25% of 12.16 deg.
B3 neutrino scale: the eigenvalues of K itself are (2,-1,-1) kappa; with p=1/2 the implied
   neutrino mass scale is kappa^2 (units MeV if kappa in sqrt(MeV)). PASS: <= 100 x 0.05 eV. FAIL otherwise.
   (If the neutrino operator is K-dominated, as the sieve note requires, its masses are set by kappa.)

## Test C (outside route: residual-symmetry / discrete flavour group, Lam 2008; Blum-Hagedorn-Lindner 2008)
Take the finite group acting on the hw=1 triplet used by T52 test D (S3, and O_h = signed permutations).
Enumerate all mixing matrices V = U_a^dagger U_b with U_a, U_b joint eigenbases of abelian subgroups with
non-degenerate spectrum, over all column matchings.  PASS: some V is CKM-like (all off-diagonal |V| <= 0.30,
largest off-diagonal in [0.18, 0.28]).  FAIL: none, i.e. discrete misalignment cannot give a Cabibbo angle.

## Outcome logic
If A2 and B both FAIL and C FAILs: the single-carrier meeting is not available from the retained C3 structure;
outcome PRICED/STANDS with the price stated as the numerical size of the non-circulant seed (A1) or the scale
contradiction (B3).  If A2 PASSes: PASSED-conditional (a shared circulant seed exists) with cost stated.
