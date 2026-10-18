# C4 worklog

## 2026-10-18 start
- Read SCIENCE_WORKFLOW s2, SCALE_LADDER_MAP C4, the 2026-10-16 freeze note, the 2026-10-17 stabilizer note,
  the 2026-09-22 soldering menu note, and the 10-17 runner's action convention (Q(M,action), label a -> column a of Q).
- Plan: (1) all Clifford-valued homs O -> O (on-site Clifford mod phase = signed perms det 1), classify up to
  conjugacy (expect 5 classes: menu 4 + the transposition-type C2 twist); (2) linear covariance subspace for
  (v_X, v_Z) on the 27-cell, quadratic symplectic conditions, exhaustive enumeration, then phases;
  (3) dynamics via trace: Cayley-Hamilton, Newton polytope light cone, glider no-go from O-invariance of tr.

## progress 1 (~1h)
- scripts/c4lib.py (shared), c4_01_actions.py (PASS=34): 58 homs O->O, 5 Clifford classes = menu 4 + 'sign-f'
  (C2 via sign character realised by a face-diagonal half turn; SO(3)-conjugate to sign, not Clifford-conjugate).
- c4_02_classify_O.py radius 1 (PASS=41): O-covariant unsigned/signed counts:
  trivial 132/528, sign 132/176, sign-f 16/32, axis 1/1, full 1/1 (identity only).
  All trivial/sign solutions = C1 E(g) C2 (one covariant CZ/S layer between on-site Cliffords); 84 have
  nonconstant trace (spreading). sign-f: all trace 0 (involutions). Twisted pairs: no signed solutions between
  inequivalent actions. TR-twist: axis/full still on-site only; sign-f TR-twist gives 28 spreading ones.
- Next: subgroups (T, D4, D3, D2) via split enumerator; dynamics script (trace trichotomy, Newton cone,
  glider no-go); radius 2 for axis/full (dim 25).

## progress 2 (~1h45)
- Proved (pen): trace trichotomy for any 1-qubit TI Clifford QCA with det 1 in any dimension:
  tau const -> periodic; tau = x^r + x^-r -> glider; else no finite Pauli ever maps to a translate of itself
  (Galois/Dickson argument on eigenvalue lambda), and tr(M^n) = D_n(tau) gives ballistic front n*vert(Newt tau).
  Covariance makes tau H-invariant, so O/T forbid gliders at ANY range and any action.
- c4_03 running (T done: no gliders; D4/trivial: 6 gliders along z). c4_04 dynamics, c4_05 independent
  recount, c4_06 radius-2 (axis/full/sign-f) written, to run sequentially (1 core).
- lib: selforth_mask early-elimination filter added (used by split enumerator; brute force keeps forms_batch).

## progress 3 (~2h30)
- c4_03 T/D4/D3 done PASS=63 FAIL=0. Soldered (axis/full): no glider/spreading for T, D4, D3; D4 full 64 periodic
  entangling (32 phase-valid); D3 full: identity + one entangling involution. Unsoldered D4/D3: gliders along axis.
- NOTE.md drafted with placeholders RADIUS2_RESULT, INDEPENDENT_RESULT, DYNAMICS_NUMERICS, D2_ROWS.
- Queue running (1 core): c4_04 -> c4_05 -> c4_06 -> c4_03 D2.

## progress 4 (~3h15)
- c4_04 PASS=21: Dickson, vertex front, cone, no-glider on all 168 spreading matrices (n<=8); numerics n<=32:
  front radius = n at every step for all 28 reps; support log-log slope 1.9-2.7 (<3, sparse).
- c4_05 independent recount (Pauli-matrix route) PASS=7: 528/176/32/1/1 matches c4_02.
- r2 run was too slow (~1h/action); added vectorised dK=0 fast path (form_eq_mask), validated at r1 vs earlier
  brute-force-checked counts (O 1, T 3, D4 64, D3 2 for axis/full). Queue2: r2 -> D2 -> rerun 02, 03 with final lib.

## progress 5 (~4h)
- c4_06 r2 (TOTAL PASS=5 FAIL=2): PREDICTION FALSIFIED. Under O with axis or full soldering at radius 2 there are
  4 unsigned / 4 signed solutions: identity + 3 entangling, all constant trace (periodic). sign-f r2: 1024 unsigned,
  all periodic. The 2 FAILs are the identity-only predictions; log kept as is.
- D2 (PASS=15): trivial/sign/sign-f/axis restrict to trivial action on D2 (4020 unsigned; 18 gliders along 3 axes);
  full: 2680 signed; with valid phases 382 periodic, 288 spreading, 0 gliders.
- c4_07 (analysis of r2 soldered solutions) queued after 02/03 reruns.
