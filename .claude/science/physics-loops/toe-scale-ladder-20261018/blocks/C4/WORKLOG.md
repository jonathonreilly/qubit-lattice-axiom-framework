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
