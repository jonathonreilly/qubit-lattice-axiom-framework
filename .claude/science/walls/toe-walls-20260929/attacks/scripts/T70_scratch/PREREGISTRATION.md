# T70 pre-registration (written before any test script was run)

Wall: T70 = L14-W11 + L16-W1 + L15-W5: "Newton's constant in lattice units
(a = l_P) is not derived".  Attacker: Claude Sonnet 5.5 (same family as the
supervisor; same-family checks only).

## Test 1 - what the wall asks of the supplied member (in-model arithmetic + solve)

Question: in the supplied static model (blocks 55-56: rates w = phi^2,
F = (2/gamma) sum (phi_x - phi_y)^2, bodies of bare energy m at rest, walls
phi = 1), which Newton constant does gamma give, and so which K does a = l_P
ask for?

Method: solve the linear system ((1-A)+D) phi = walls on a 41^3 box (sparse),
one body and two bodies at weak field.  Read (i) the far field of phi and of
w = phi^2, (ii) the pair ledger deficit versus separation.

Predictions written now:
- P1a: 1 - phi -> gamma m /(8 pi r)  (the entry's number).
- P1b: the static interaction energy of two bodies, i.e. the ledger deficit,
  -> gamma m1 m2 /(4 pi r); so G_lat = gamma/(4 pi), a factor 2 above the
  entry's gamma/(8 pi), because the clock rate is w = phi^2, not phi.
- P1c: with gamma = 1/(4K) (block 55 Corollary, quoted in the 2026-09-21
  curvature-member note, line 75) G_lat = 1/(16 pi K), the same K that the
  comparator's kinetic coefficient c_k = -6K = -6/(16 pi G) (ADM) would give.

Reading:
- PASS of the entry (G_lat = gamma/(8 pi)): pair deficit coefficient within 3 % of
  gamma/(8 pi).
- FAIL of the entry (factor 2 correction stands): pair deficit coefficient within
  3 % of gamma/(4 pi).
- Anything else: the mapping G <-> gamma is not a clean number; report as such.

## Test 2 - does a lattice-regulated Sakharov route give one definite G_lat?

Model: free minimally coupled massive scalar on Z^3 (Hamiltonian, continuous
time), coupled to a static slowly varying metric
ds^2 = -N^2 dt^2 + g_ij dx^i dx^j (diagonal, depending on z only), with
H = sum [ (N/(2 sqrt g)) pi^2 + (1/2) N sqrt g g^{ij} d_i phi d_j phi + (1/2) m^2 N sqrt g phi^2 ].
Vacuum energy E0 = (1/2) sum omega by exact diagonalisation in supercells of p
sites, second order in the amplitude.  Three sectors:
TT (g_xx = 1+h c, g_yy = 1-h c), conformal (g_ij = psi^4 delta, psi = 1 + p c),
lapse (N = 1 + n c), c = cos(k z).
Continuum Einstein-Hilbert values (verified symbolically in the script):
  TT:       E2/V = k^2 h^2 /(64 pi G)
  (n,p):    E2/V = -(k^2/(4 pi G)) (p^2 + n p)   [no n^2 term]
Also the k = 0 (uniform) response, compared with the covariant expectation
E2/V(k=0) = -(rho0/2) h^2 for TT (rho0 = vacuum energy per site at h = 0).

Three ways to put the smooth metric on the z-bonds (the lattice does not fix
this): V0 = evaluate at the bond midpoint, V1 = arithmetic mean of the two site
values of the stiffness, V2 = harmonic mean (bonds in series).

Predictions written now (I expect the route NOT to be well-posed):
- P2a: k = 0 TT response differs from -rho0/2 by an O(1) fraction (a Planck-scale
  shear stiffness of the lattice), i.e. a graviton mass term unless tuned.
- P2b: the k^2 coefficient of the TT response differs among V0, V1, V2 by more
  than 10 %, because a redefinition h -> h (1 + c k^2) moves it by 2 c Pi_0.
- P2c: the sector relations do not close: G from TT, G from the conformal sector
  and the n^2 coefficient (should be 0) disagree by more than 10 %.

Reading:
- "Route (a) is well posed" (a definite G per species exists on the fixed
  lattice) requires ALL of: (i) |Pi_0^TT - covariant| < 5 % of |rho0/2|;
  (ii) V0, V1, V2 agree on the TT k^2 coefficient within 10 %;
  (iii) G_TT and G_conf agree within 10 % and |A_nn| < 10 % of |A_pp|.
- Otherwise: "not well posed": the number is a property of the coupling
  prescription and of tuned counterterms, not of the field on the lattice.
- Whatever the outcome, report N_eff* = species count that would give G_lat = 1
  from the TT number (per V), and whether it is near a natural integer
  (1, 2, 4, 8, 16).

## Test 3 (only if time) - Jacobson relation on the lattice

For the same scalar, entropy per plaquette across a plane cut (exact corner-transfer
matrix formula per transverse mode, checked against a finite-chain correlation-matrix
computation).  Prediction: 1/(4 c_ent) differs from G_TT by more than 10 % (the
Susskind-Uglum / Jacobson equality S = A/(4G_ind) is a heat-kernel statement, not a
lattice one).  Pass reading (relation holds on the lattice): within 10 %.
