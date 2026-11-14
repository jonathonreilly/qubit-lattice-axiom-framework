D4 gauged zoom rungs n = 1, 2, 3 from a Wilson seed in supplied U(1) backgrounds: on small tori the measured decay rate does not fall with roughness, and the Ginsparg-Wilson residual of one source column falls slowly with n; exact GW and the n -> infinity limit in a background are open

Date: 2026-10-26
Claim type: bounded_theorem (exact identities plus finite diagnostics for a supplied free model in supplied abelian backgrounds)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: [`scripts/d4_gauged_zoom_fixed_point_fermion_stays_exponentially_local_in_rough_u1_backgrounds_2026_10_26.py`](../scripts/d4_gauged_zoom_fixed_point_fermion_stays_exponentially_local_in_rough_u1_backgrounds_2026_10_26.py). AUDIT_TIMEOUT_SEC = 120, seeded; it exits nonzero on any failed check.
  Its cache [`logs/runner-cache/d4_gauged_zoom_fixed_point_fermion_stays_exponentially_local_in_rough_u1_backgrounds_2026_10_26.txt`](../logs/runner-cache/d4_gauged_zoom_fixed_point_fermion_stays_exponentially_local_in_rough_u1_backgrounds_2026_10_26.txt) holds the current output and counts. The source run (68 s, 703 MB peak) had 8 checks;
  the 2026-11-14 repair added the solver checks 0c and S.
Pre-registration: criteria_pre_run.txt, written before any computation.
Labels: [T] exact or theorem; [F] finite diagnostic; [A] supplied literature theorem; [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Question
A working decision, cited here as "the revised decision (PR #10111)", takes the exact D4 zoom fixed point as matter's
working weight, with one condition: revisit it if the fixed point's exponential locality fails in the interacting theory.
That decision is a proposed candidate with no premise weight here, and its text is not in the exported #10111 note (see
conflict entry 1 of [the consolidation](D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md)). This note tests the locality condition at finite rung n in a
background U(1) gauge field. This is "interacting" only in the background-field sense: no dynamical links, no loops.

Construction
- [T] Gauged zoom: G_{l+1} - alpha = 8 B_l (G_l - alpha) B_l^dag.
  - B_l(X, x) = (1/16) w(x - 2X) T(2X -> x), with w = 1, 1/2, 1/8 (the forced W(F4) kernel of #10098).
  - T is the straight-line parallel transporter of a continuum background A. This is gauge-covariant blocking in the
    classically-perfect-action style [A: Hasenfratz-Niedermayer; Bietenholz-Wiese "blocking from a finer lattice"].
  - The seed is the NN D4 Wilson start (#10098 / #10111), gauged by the same A, on a 2^n-finer D4 torus.
  - D_n = G_n^-1 comes from the Woodbury form D_n = K^-1 - 8^n K^-1 B M^-1 B^dag K^-1, with
    M = D_NN + 8^n B^dag K^-1 B and K = alpha(1 - 8^n B B^dag) > 0 (because 8 B B^dag <= 1/2 entrywise).
  - This form is valid even when D_NN has zero modes. Fine solves use GMRES; no dense fine matrix is formed.
- [T] GW propagation identity: {g5, G_{l+1} - alpha} = 8 B {g5, G_l - alpha} B^dag, because B is spin-diagonal. GW for
  D = G^-1 with constant alpha is the statement {g5, G - alpha} = 0. So a seed that already satisfies {g5, G_0 - alpha} = 0
  gives an exactly GW D_n at every n.
- The Wilson seed used here does NOT satisfy it. The identity carries its breaking X_0 = {g5, G_0 - alpha} along as
  X_n = 8^n B X_0 B^dag (B the composite blocking). Whether X_n -> 0 as n -> infinity in a background needs a uniform
  bound that this note does not supply. So exact GW for the Wilson-seeded limit in rough backgrounds is an OPEN
  obligation. The runner measures the residual only at n = 1, 2, 3 (2a).
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
  eps = 1: 2.55; UV modes at eps = 1.9: 2.23. GMRES needs 68-78 iterations to converge to 1e-10. [S] Reading, not computed:
  the low-rank term 8^n B^dag K^-1 B of M lifts the smooth near-zero modes of D_NN; the gap of M was not computed.
- [F] Solver status (repair 2026-11-14, finding 4 of the 2026-11-13 hold). The source runner ignored the GMRES `info`
  flag and suppressed warnings, so a cache could pass on an unconverged solve. The runner now records every fine solve,
  requires info == 0 and an independent residual ||M x - b|| / ||b|| <= 1e-9 for each, and makes every check that uses
  solves depend on that. In the regenerated cache all 512 recorded solves have info == 0, and the largest independent residual prints as 1e-10.
  Control 0c: a solve cut to 5 GMRES iterations is flagged (info 1, residual 0.18). The numbers in 0a-3b did not change.
- Scope of 1a/1b. Each rate is a fit of the envelope of ||D(x, y)|| from one source site y over a finite distance window
  (1.3 to 4.6 on L_c = 6; 1.3 to 3.1 on L_c = 4). It is a finite diagnostic at n = 1 and n = 2, not a uniform
  exponential-locality bound, and not a statement about n -> infinity.
- [F] 2a. GW residual ||(g5 D + D g5 - 2 alpha D g5 D) e_0|| / ||D e_0|| for n = 1, 2, 3 (L_c = 2), on ONE source
  block-column e_0 (the four spinor columns at coarse site 0), not the full matrix:
  - free: 2.0e-2, 9.0e-4, 3.9e-5 (a factor of about 22 per step);
  - Q = 1: 0.19, 0.14, 0.088 (x1.4, x1.6);
  - UV, eps = 1: 2.9e-2, 1.9e-2, 1.8e-2 (x1.5, x1.1).
  - An IR background in a development run gave x2.1, x1.9 (dropped from the runner to save time).
  - The residual is monotone in every background, but the decrease is SLOW in a background.
- [F] 2b. Column change ratio ||v_3 - v_2|| / ||v_2 - v_1|| with v_n = D_n e_0 (same source column): free 0.05; Q = 1: 0.67;
  UV: 0.07. Correction (2026-11-14): the source text called this the full-matrix ratio ||D_3 - D_2|| / ||D_2 - D_1||; the
  runner computed (||v_3 - v_2|| / ||v_3||) / (||v_2 - v_1|| / ||v_2||) for one column. The regenerated cache prints
  both column forms, which agree to the two digits shown. The full-matrix ratio was not computed. Three rungs do not show
  convergence as n -> infinity; that is OPEN.
- [F] 3a. Overlap index -(1/2) Tr sign(g5(2 alpha D_n - 1)) = -Q for Q = 0, 1, -1. This holds for smooth backgrounds and
  for eps = 1.2, at n = 1 and 2. The spectral gap is >= 0.22; on this L_c = 2 torus, Q = 1 means a flux of pi/2 per
  coarse unit area.
- [F] 3b. In Q = 1, the lowest mode of D_n is real and chiral to the printed precision (g5 = -1.000). It sits at
  lambda_0 = 0.78 (n = 1) and 0.50 (n = 2), a ratio of 1.57: it moves toward 0. Whether it reaches 0 as n -> infinity
  is not computed.
- [S] Reading of 2a and 3b: in a background, the Wilson seed's chirality breaking is the dimension-5 Pauli term
  (a sigma.F). Blocking suppresses it only as 2^-n. In the free theory the leading breaking is a contact term that the
  zoom absorbs, so its residual falls about 16-23x per step. Expected background rate: about 2 per step. Observed:
  1.4-2.1. The UV case is slower, because the field stays rough at the n = 3 fine scale.

Verdict (pre-registered rule, read for the measured cases only)
- C1: PASS at the measured rungs. The fitted rates from one source site are 1.79-1.88 (n = 1, L_c = 6) and 2.07-2.55
  (n = 2, L_c = 4). They are >= 0.8 x free at the HJL bound and >= 1.0 up to eps = 1.9. In this tested range the rate
  does not fall with roughness, including beyond the HJL bound (a sufficient condition only).
- C2: index PASS: index = -Q in smooth and rough backgrounds at n = 1, 2 on L_c = 2, and the chiral lowest mode moves
  toward 0. MISS on the pre-registered bar of a x1.5 decrease per step (Q = 1, n = 1 -> 2: x1.4; UV, n = 2 -> 3: x1.1).
  Exact GW is not established for the Wilson seed at any n or in the limit (see Construction).
- C3: PASS for the column analogue: every column ratio is <= 0.7 (worst 0.67, Q = 1). The pre-registered full-matrix ratio
  was not computed.

Consequence for the decision
- The measured finite-rung kernels (n = 1, 2) do not trigger the revisit condition at background-field level: their
  fitted decay rates do not fall with roughness. The exact fixed point (n -> infinity) in a background was NOT computed,
  so this note does not show that it is exponentially local, and it does not decide whether the cited decision stands.
- Observed cost at finite n [F]: in a gauge background the GW residual of one source column fell by x1.1 to x1.6 per
  step (n <= 3, L_c = 2), against about x22 in the free case. [S] The note reads this as about 2^-n with a coefficient set
  by the coarse field strength; that is an untested prediction, not a measured law. The source text's statements that
  the cited decision "stands" and that the finite-rung rule's withdrawal is "the right call" are withdrawn here: they
  rest on the uncomputed limit and on a decision text that is not in this PR.
- Still open (walls move):
  - non-abelian backgrounds;
  - dynamical links and loops (the truly interacting case);
  - the HN fine field from minimisation, instead of a continuum interpolation;
  - larger tori, and more blocking steps on L_c >= 4;
  - a Combes-Thomas-type proof that the gap of M bounds the locality rate (suggested by 1b; not proven);
  - the n -> infinity limit in a background: convergence, uniform locality, and whether the GW residual of the Wilson
    seed vanishes (the identity alone does not give it);
  - the full-matrix convergence ratio and the full-matrix GW residual (only one source column was measured).

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
- CANDIDATE_AXIOM_RULES.md: the revised decision. That file is on neither this branch nor `main`; the decision is
  recorded only through the [consolidation](D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md) conflict entry 1.
- Lane names above that are not links (d4-zoom-fixed-point-fermion, d4-zoom-direction, d4-zoom-chirality) are the notes
  [#10098](D4_ZOOM_FIXED_POINT_FERMION_HAS_ONLY_REAL_POSITIVE_POLES_BUT_SITE_POSITIVITY_NEEDS_A_ONE_SLICE_BUFFER_BOUNDED_THEOREM_NOTE_2026-10-26.md),
  [#10111](D4_ZOOM_DIRECTION_FINITE_RUNG_MATTER_WEIGHT_IS_AN_EVENT_KERNEL_LIV_SET_BY_THE_EVENT_RUNG_COUNT_BOUNDED_THEOREM_NOTE_2026-10-26.md)
  and [#10099](D4_ZOOM_FIXED_POINT_CHIRALITY_OVERLAP_INDEX_AND_DOMAIN_WALL_SLAB_BOUNDED_THEOREM_NOTE_2026-10-26.md) in this PR.
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
