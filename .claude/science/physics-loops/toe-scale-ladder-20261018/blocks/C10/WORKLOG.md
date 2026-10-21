# C10 worklog: burn-and-turn source tensor on the C7 two-qubit Dirac walk vs the C8 couplings

## Pre-registration (written 16:06Z, BEFORE any number was computed)

**Inputs treated as data / premises.**
- BT (other thread, branch `origin/claude/gravity-burn-turn-source-tensor-20261021`): the
  burn-and-turn rule. Domain as written there: "a lossless walk has components labelled by step
  directions d. Each tick a site coin mixes them, then each component moves one link along its d";
  U(k) = diag(exp(-i k.d)) C. Fronts follow the Born odds P_d = |u_d|^2 of a plane-wave
  eigenmode u; exchange flow 2 eps P_d P_d'/rho; burn adds eps d d; turn adds -(d'-d)(d'-d)/4.
- C7 walk (P1-P3): U(k) = f + i h.tau + i tau3 g.sigma on the 27-point cell, massive members
  U_theta = M U0 M; points b*, b_iso, b_gold.
- C8 couplings M1-M4 (P4 and variants), vertex at q = 0 between k and k.

**Prior exposure (disclosed).** Before computing I noted by hand: (i) the BT plane-wave identity
burns + turns = eps m m (m = mean step) is pure algebra and holds for ANY normalised weights;
so on any walk the only question is whether the mean step under the chosen odds is the group
velocity; (ii) for a Clifford generator the plane-wave expectation <alpha_i> = g_i / sin(omega)
is independent of the vector chosen in the (doubly degenerate) band; (iii) at continuum order
every metric-coupling stress tensor of a Dirac field with light speed s is E v v / s^2 in
lattice units, while BT gives eps v v; so I expect a factor s^2 at continuum order for s != 1.
These expectations are tested, not assumed.

**Step 0 (domain test, decisive for "exactly as defined").** The C7 walk is in the BT domain iff,
in some internal basis, U(k) = sum_n exp(-i k.n) A_n with each A_n = Pi_n C, Pi_n mutually
orthogonal projectors onto label subspaces (shift-coin form, one link per tick). Necessary
condition tested: A_n A_m^dag = 0 for all n != m among the nonzero hop matrices, and number of
nonzero A_n <= 4 (dim C^4) with unit-length n. If it fails, BT cannot be applied as defined and
every further step is a DECLARED EXTENSION (labelled as such).

**Declared extensions (both reduce to BT's odds on shift-coin walks; checked in the runner on the
1D and six-direction walks of the BT runner):**
- E-K (which-hop / Kraus odds): P_n = ||A_n u||^2, real, >= 0, sum 1 (from sum A_n^dag A_n = 1).
  Depends on u inside the degenerate band; report the range over the band.
- E-W (weak-value odds): w_n = exp(i omega) exp(-i k.n) <u|A_n|u>, sum 1, mean = group velocity
  exactly, but possibly complex/negative (then not a valid front flow; reported).
Turn flows 2 eps P_n P_n'/rho over hop vectors n in {-1,0,1}^3; |n|^2 in {0,1,2,3}.

**Stress tensors of the couplings (tree level, plane wave in the upper band, q = 0):**
T^X_ij := -2 d<u|delta H_X|u>/d h_ij, symmetrised, with delta H_X = -(1/2) h_ij V^X_ij.
M1: sym <alpha_i> rho g_j; M2: sym <alpha_i> g_j; M3: sym <alpha_i> s sin k_j;
M4: sym sin k_j <d_i H_a> = sym v_i sin k_j. Lattice units a = tau = 1.

**Comparison criteria (fixed now).**
C-exact: max_ij |T^BT - T^X| / max|T^X| < 1e-10 on a fixed momentum set (directions (100),
  (110), (111), (123), |k| = 0.05, 0.2, 0.5; massless and theta = 0.2 with chi = 0, pi/2).
C-cont: leading small-k tensor (k = kappa n, theta = kappa mu, kappa -> 0) equal, AS GIVEN
  (no rescaling). Secondary, labelled "shape": equal up to ONE constant fixed at continuum order.
C-a2: the O(kappa^2) relative correction tensor equal (as given and up to the continuum constant).
  The constant may never be fitted at O(a^2).
Outcome labels: selection = exactly one coupling meets C-a2 (shape) and the others fail;
non-selection = several meet it; incompatibility = none meets C-cont as given / C-a2.
Clock criterion: turn action per tick = m^2/eps within 1% at the declared momenta (as in BT),
  with m = theta; also the c = s relativistic form eps(1 - v^2/s^2), declared as a second target.
No fitting anywhere; c_G and a/l_P only quoted from C8.

## Log
- 16:40Z debug run of scripts/c10_numeric.py (output kept in the session scratchpad only, not a
  log; 25 PASS / 2 FAIL). Findings: (a) Step 0 fails: 27 nonzero hops, ranks sum 92, overlapping
  ranges => the C7 walk is NOT in the BT domain at any point; all further results are for the
  declared extensions. (b) E-K mean step is ~85% off v at every point (BT,K fails already at
  continuum order). (c) E-W weights are complex/negative (|Im w| up to 0.62), mean = v exactly.
  (d) UNEXPECTED: T^BT,W / s^2 equals T^M1 exactly on lattice axes for every b, and at b_iso to
  ~1e-12 at kappa = .005 (better than O(a^2)). My pre-guessed check "all couplings mismatch at
  O(a^2)" FAILED because of this. (e) My pre-guessed clock check "E-K fails by >5% everywhere"
  FAILED at one point: the E-K action rises with |k| while m^2/eps falls, so the curves cross.
  Revisions (made after seeing the debug output, disclosed): the C-a2 and clock checks are
  rewritten as tests of the exact statements derived next (c10_exact.py), with the axis
  direction separated; the clock check now tests the rest value and the k-trend. The comparison
  criteria themselves (C-exact, C-cont as given / shape, C-a2 with the constant fixed at
  continuum order) are unchanged.
- 16:50Z hand derivation (then checked in sympy): with D = -grad f, D - s g =
  sin k_1 [-3 beta (x2+x3) + C x2 x3] (x_a = 1 - cos k_a), beta = C7's k^4 anisotropy
  coefficient. Since T^BT,W = omega D D / sin^2 omega and T^M1 = omega g g / sin^2 omega
  exactly, the M1 shape mismatch at O(a^2) is proportional to beta. Massive: D_theta = lambda s g + ...
  with lambda = cos theta - sin theta (hhat.W)/s^2. E-W rest clock: <|n|^2>_W = 3 s^2 - 3 i hhat.W.
