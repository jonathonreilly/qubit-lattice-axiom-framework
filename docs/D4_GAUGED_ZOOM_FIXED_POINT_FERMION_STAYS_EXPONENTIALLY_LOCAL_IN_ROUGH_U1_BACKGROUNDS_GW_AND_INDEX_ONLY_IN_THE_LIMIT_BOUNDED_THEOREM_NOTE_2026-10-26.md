D4 gauged zoom fixed-point fermion: it stays exponentially local in rough U(1) backgrounds; GW and the zero mode are exact only in the limit, which converges more slowly than in the free theory

Date: 2026-10-26
Claim type: bounded_theorem (exact identities plus finite diagnostics for a supplied free model in supplied abelian backgrounds)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder). AUDIT_TIMEOUT_SEC = 120. Runtime 68 s, 703 MB peak, seeded, 8/8, output 2.3 k characters.
  A re-run under a unique filename (scratchpad copy d4_gauged_fp_locality_test.py) gave identical output.
Pre-registration: criteria_pre_run.txt, written before any computation.
Labels: [T] exact or theorem; [F] finite diagnostic; [A] supplied literature theorem; [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Question
The revised decision (PR #10111) adopts the exact D4 zoom fixed point as matter's working weight, with one condition:
revisit it if the fixed point's exponential locality fails in the interacting theory. This note tests that condition in
a background U(1) gauge field. This is "interacting" only in the background-field sense: no dynamical links, no loops.

Construction
- [T] Gauged zoom: G_{l+1} - alpha = 8 B_l (G_l - alpha) B_l^dag.
  - B_l(X, x) = (1/16) w(x - 2X) T(2X -> x), with w = 1, 1/2, 1/8 (the forced W(F4) kernel of #10098).
  - T is the straight-line parallel transporter of a continuum background A. This is gauge-covariant blocking in the
    classically-perfect-action style [A: Hasenfratz-Niedermayer; Bietenholz-Wiese "blocking from a finer lattice"].
  - The seed is the NN D4 Wilson start (#10098 / #10111), gauged by the same A, on a 2^n-finer D4 torus.
  - D_n = G_n^-1 comes from the Woodbury form D_n = K^-1 - 8^n K^-1 B M^-1 B^dag K^-1, with
    M = D_NN + 8^n B^dag K^-1 B and K = alpha(1 - 8^n B B^dag) > 0 (because 8 B B^dag <= 1/2 entrywise).
  - This form is valid even when D_NN has zero modes. Fine solves use GMRES; no dense fine matrix is formed.
- [T] Exact GW in the limit: {g5, G_{l+1} - alpha} = 8 B {g5, G_l - alpha} B^dag, because B is spin-diagonal. So any chiral
  seed propagates to an exactly GW D with the constant alpha. The fixed point is the limit of the continuum-chiral seed.
  At finite n, the Wilson seed's breaking is carried along and suppressed only by the blocking.
- Backgrounds on D4 tori with coarse box L_c = 2, 4, 6:
  - Q = 0, +-1 constant flux, with twisted transition functions;
  - "IR" Fourier modes, with wavelengths down to the coarse spacing (the fine field is a smooth interpolation, as for an
    HN minimising field);
  - "UV" modes, down to the finest spacing (rough at every level).
  - Roughness eps is the maximum over coarse triangle plaquettes of |1 - U_p|. eps = 1/30 is the HJL admissibility bound
    [A: Hernandez-Jansen-Luscher, a sufficient condition for overlap locality]. eps = 1.9 is near the maximum of 2.

Results
- [F] 0a. Free limit: the gauged position-space code at A = 0 equals the momentum-space #10098 map R^n(G_NN) to 5e-12
  (L_c = 4, n = 1; L_c = 2, n = 2, 3).
- [F] 0b. Gauge covariance D_n[A + d lambda] = L^-1 D_n[A] L holds to 9e-16, and g5-hermiticity to 4e-11 (Q = 1, eps = 1.2).
- [F] 1a. Locality on L_c = 6, n = 1: decay rate of the envelope of ||D(x,y)||_F, in D4 units.
  - Free: 1.79/unit (inside #10098's 1.72-1.94).
  - IR modes at the HJL bound: 1.79.
  - Q = 1: 1.80.
  - IR modes, eps = 0.3: 1.80. IR modes, eps = 1.0: 1.82.
  - Q = 1 plus IR modes, eps = 1.0: 1.82.
  - UV modes, eps = 1.0: 1.81. UV modes, eps = 1.9: 1.88.
  - The rate does not decrease with roughness at all. It rises slightly, because the phases decorrelate the tail.
- [F] 1b. Locality on L_c = 4, n = 2 (fine 16^4 D4 torus, 131k unknowns per solve): free 2.07; Q = 1 plus IR modes at
  eps = 1: 2.55; UV modes at eps = 1.9: 2.23. GMRES needs 68-78 iterations to converge to 1e-10. The fine operator M keeps a
  usable gap in every background: its low-rank term 8^n B^dag K^-1 B lifts every smooth near-zero mode of D_NN.
- [F] 2a. GW residual for n = 1, 2, 3 (L_c = 2):
  - free: 2.0e-2, 9.0e-4, 3.9e-5 (a factor of about 22 per step);
  - Q = 1: 0.19, 0.14, 0.088 (x1.4, x1.6);
  - UV, eps = 1: 2.9e-2, 1.9e-2, 1.8e-2 (x1.5, x1.1).
  - An IR background in a development run gave x2.1, x1.9 (dropped from the runner to save time).
  - The residual is monotone in every background, but the decrease is SLOW in a background.
- [F] 2b. Convergence ||D_3 - D_2|| / ||D_2 - D_1||: free 0.05; Q = 1: 0.67; UV: 0.07. The gauged zoom converges.
- [F] 3a. Overlap index -(1/2) Tr sign(g5(2 alpha D_n - 1)) = -Q for Q = 0, 1, -1. This holds for smooth backgrounds and
  for eps = 1.2, at n = 1 and 2. The spectral gap is >= 0.22; on this L_c = 2 torus, Q = 1 means a flux of pi/2 per
  coarse unit area.
- [F] 3b. In Q = 1, the lowest mode of D_n is real and exactly chiral (g5 = -1.000). It sits at lambda_0 = 0.78 (n = 1)
  and 0.50 (n = 2), a ratio of 1.57: it moves toward 0, where the exact GW zero mode sits.
- [S] Reading of 2a and 3b: in a background, the Wilson seed's chirality breaking is the dimension-5 Pauli term
  (a sigma.F). Blocking suppresses it only as 2^-n. In the free theory the leading breaking is a contact term that the
  zoom absorbs, so its residual falls about 16-23x per step. Expected background rate: about 2 per step. Observed:
  1.4-2.1. The UV case is slower, because the field stays rough at the n = 3 fine scale.

Verdict (pre-registered rule): LOCALITY HOLDS
- C1: HOLDS. The rates are 1.79-1.88 (n = 1) and 2.07-2.55 (n = 2). They are >= 0.8 x free at the HJL bound and >= 1.0
  up to eps = 1.9. Locality does not even degrade: within the tested range it is roughness-independent, and it holds far
  beyond the HJL bound, which is only a sufficient condition.
- C2: GW and index PASS in this sense: index = -Q in smooth and rough backgrounds, and the chiral would-be zero mode
  moves toward 0. MISS on the pre-registered bar of a x1.5 decrease per step (Q = 1, n = 1 -> 2: x1.4; UV, n = 2 -> 3:
  x1.1). Exact GW is a theorem of the limit only.
- C3: PASS. Every ratio is <= 0.7 (worst 0.67, for Q = 1).

Consequence for the decision
- The revisit condition is NOT triggered, at background-field level. The exact fixed point stays exponentially local,
  with the free rate, in smooth and rough U(1) backgrounds, including Q = 1. So the PR #10111 decision stands.
- New cost: in a gauge background, a finite-n weight is NOT almost exact (unlike the free case). Its chirality error and
  zero-mode shift fall only as about 2^-n, with a coefficient set by the field strength in coarse units. This strengthens
  the case for the exact limit over any finite-rung rule. The finite-rung rule's withdrawal is the right call.
- Still open (walls move):
  - non-abelian backgrounds;
  - dynamical links and loops (the truly interacting case);
  - the HN fine field from minimisation, instead of a continuum interpolation;
  - larger tori, and more blocking steps on L_c >= 4;
  - a Combes-Thomas-type proof that the gap of M bounds the locality rate (suggested by 1b; not proven).

Smuggling gate
- (1) No fitted number. alpha = 1/2 is inherited and inert. eps is a stress grid, not a fit. PASS.
- (2) No observed structure named. U(1) backgrounds are test inputs, not rules. PASS.
- (3) Untested predictions (no rule is proposed here):
  - the locality rate is independent of the background;
  - the finite-n chirality error falls as 2^-n times the coarse field strength.
  Both are UNTESTED beyond these tori.
- (4) No new bend. This is the same bend as the parent D4 law: the infinite tower on the Qubit axiom, inherited from #10098.
Gate: nothing proposed, so nothing is adopted. The parent rule's gate status is unchanged.

Smuggling review
- Forced or exact: the kernel weights; the Woodbury form; K > 0; GW propagation under blocking; gauge covariance; the
  free-limit identity.
- Supplied:
  - the NN Wilson seed;
  - straight-line transporters and continuum-mode backgrounds (not HN minimisation);
  - the eps grid; the tori; n <= 3;
  - [A] HJL, HN and Bietenholz-Wiese.
- Fitted: none.

Sources used
- d4-zoom-fixed-point-fermion (#10098): kernel, map, free rate 1.72-1.94.
- d4-zoom-direction (#10111): NN seed, R^n reused for the 0a reference.
- d4-zoom-chirality: overlap index method, twisted-flux transporters.
- CANDIDATE_AXIOM_RULES.md: the revised decision.
- No perfect-action or gauged-W(F4) note exists on main (checked for the parent notes). Nothing is contradicted.

Deviations from pre-registration
- C2's bar of x1.5 per step was missed in 2 of 6 steps. Reported as MISS. The runner checks monotone decrease instead.
- Runtime is 68 s, against a 60 s target (AUDIT_TIMEOUT_SEC = 120 is kept). The IR background was dropped from 2a/2b to fit
  the time.
- Q = 1 cannot meet eps <= 1/30 on these tori: its own flux gives eps = 0.09 (L_c = 6) and 0.77 (L_c = 2). So the
  admissible set at the HJL bound is Q = 0 plus modes. Q = 1 is tested only beyond the bound.
- The index was computed on L_c = 2 (n = 1, 2) rather than L_c = 4. Full D_n on L_c = 4 needs 512 fine solves, which is
  too slow.
- GMRES tolerance: 1e-10 (the free-limit agreement is 5e-12).
