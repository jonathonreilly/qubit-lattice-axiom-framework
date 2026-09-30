# T75 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks).

Split of the wall into what can and cannot be tested in about 45 minutes:
- KINEMATIC half: on a SUPPLIED rate profile, does the framework's clocked walker
  (H_w = Phi H Phi, Phi = sqrt(rate); block 54 / 56 clocks) give a thermal state at
  T = kappa/(2 pi), with the right sign? This is L15-W7's own "cheapest test", done
  with the framework's own hopping-type clock (not an on-site potential).
- DYNAMICAL half: does the record dynamics (blocks 53-56, the only landed rate-field
  statics) produce a stopped clock at finite mass, and if it does, what is the
  surface gravity kappa of the exterior lapse?

Notation: rate w = phi^2, clock/lapse N = w, hopping between neighbours = phi_x phi_y.
Ambient rate 1. Chain hopping t = 1 has Fermi speed v = 2 t.

## Test A (script A_kinematic_kms.py)
Model: half-filled tight-binding chain; exact infinite-chain vacuum correlations
C_ij = sin(pi (i-j)/2)/(pi (i-j)), C_ii = 1/2. Wedge = sites j = 1..M (M = 1500),
horizon at the stopped site j = 0 (w_0 = 0, so the bond (0,1) has hopping 0).
Entanglement Hamiltonian h = ln((1-C)/C) on the wedge. Framework clock profile
w_j = a j (linear zero): H_R bond (j, j+1) has hopping a sqrt(j (j+1)).
Prediction: local speed v(j) = 2 a j, kappa = dv/dj = 2a, T = kappa/2pi = a/pi, i.e.
h = beta H_R with beta a / pi = 1 (Bisognano-Wichmann on the lattice).
Fit beta by least squares over bonds j <= 100 (away from the far truncation).
- PASS (kinematic Hawking/Unruh law holds on the clocked walker): beta a/pi in
  [0.97, 1.03], relative residual ||h - beta H_R|| / ||h|| < 0.05 on the window, beta > 0
  (right sign), for each of a = 0.02, 0.05, 0.1.
- FAIL: beta a/pi outside [0.90, 1.10], or residual > 0.15, or beta < 0.
Controls (expected to fail; shown so the pass is not a fitting artefact):
- C1 on-site version: same profile entering as an on-site potential a j n_j.
  Prediction: residual > 0.5 (no thermal fit).
- C2 double zero: w_j = (a j)^2, hopping a^2 j (j+1) (what the stopped-ball exterior
  looks like, see Test B). Prediction: local beta_j = h_{j,j+1}/t_j is NOT constant:
  varies by more than a factor 5 over j = 2..100 (roughly as 1/j), so no single
  temperature; consistent with kappa = 0.

## Test B1 (script B1_stopped_ball.py)
3D box 41^3, walls phi = 1, ball of stopped sites (phi = 0 on all sites within
radius R of the centre), simplest bond energy of block 56 (phi harmonic outside,
linear problem). Validation: ledger for R = 6 must reproduce the note's 192.32
(gamma = 1) within 0.5%. Then exterior profile phi_n along the axis at distance n
from the ball surface, n = 1..6; local lapse exponent p = d ln w / d ln n.
- Prediction (Hopf lemma): phi_n / n constant within 10% for n = 1..4, so w ~ n^2,
  p in [1.8, 2.2] on n = 2..5: a double zero, kappa = 0 at scales >> 1.
- FAIL of the prediction: fitted p <= 1.3 (a linear zero would exist).

## Test B2 (script B2_second_bond_energy.py)
The lane's own "cheapest next step" for L15-W6: second bond energy of block 56,
F2 = (1/gamma) sum_bonds (w_x - w_y)^2 / (w_x + w_y), a single body of bare energy m
at the centre of a 41^3 box (walls w = 1), gamma = 1, so 18/gamma = 18.
Analytic prediction: at w_0 = 0 the body's equation reads m = 18/gamma whatever the
neighbours, and near it 18/gamma - m = (8/gamma) w_0 sum_y (1/w_y) (linear vanishing).
Newton continuation in m from 0.
- PASS (a stopped clock exists at finite mass): w_0 < 1e-3 reached with m within 1%
  of 18, and (18 - m)/w_0 within 5% of 8 sum_y(1/w_y) there.
- FAIL: branch folds at m_fold < 0.95 * 18 with w_0(fold) > 0.05.

## Test B3 (script B3_exponent_1d.py)
1D half-space, w_0 = 1e-9 (stopped), w_N = 1, N = 400, weight-one bond energies
F1 = (phi_x - phi_y)^2, F2 as above, F3 = (w_x - w_y)^2 / sqrt(w_x w_y); solve the
empty-site stationarity d F / d w_x = 0 by Newton. Local exponent p(n) = d ln w / d ln n.
- Prediction: p(n) -> 2 for n >> 1 for all three (any smooth weight-one bond energy
  has the gradient form (grad phi)^2 at large scales); differences only in the first
  few layers.
- Contrast: scale-covariance-breaking energy F_w = (w_x - w_y)^2 (weight two) gives
  p = 1 exactly (harmonic in w), which is the only route to a linear zero found.
- FAIL of the prediction: any weight-one energy with p(n = 20) < 1.7.

## Reading rules
- A pass in A with the passes/fails above moves only the kinematic half (W7's
  "cheapest test"); it is not a derivation of a horizon.
- B1 + B3 passing means: in the landed rate-field statics every large stopped region
  is extremal (kappa = 0, T_H = 0).
- B2 passing means: the finite-mass clock stop exists for the second bond energy at
  m* = 18/gamma (the lane's deferred claim), but it is one site, not an area.
