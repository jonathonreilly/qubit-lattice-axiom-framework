# C4c WORKLOG

- Read C4b NOTE (Lemmas 2-3), C4 NOTE conventions, SCIENCE_WORKFLOW s2. Coordinator update: axis
  action pair walk is only T-covariant; 13 = 3+4+6 (62 at r=2); flat pairs != no transport.
- Plan: (i) single commuting layer freeze lemma; (ii) vertex lemma (U(1) commuting TI families are
  diagonal at conv-hull vertices of support) -> convex-position supports diagonal; (iii) products of
  such layers + covariant on-site gates are diagonal -> all sectors frozen; (iv) pair kinematics and
  monomial-QCA certificate; (v) numerical search for non-diagonal commuting U(1) families on
  non-convex supports (evidence only).
- Container restart killed first c4c_01 run (exit 137) and a 1D search; re-running with a faster
  candidate enumeration (images restricted to B_r(a) cap B_r(b)).
- c4c_01 rerun: r=1 T-covariant monomial freeze prediction FAILED (6 face-diagonal exceptions:
  symmetry-allowed pair step along the face normal); O (full) PASS. Kept FAIL.
- c4c_02 vertex lemma ingredients PASS=9 (first run had 2 FAILs from sympy dict-ordering in the
  comparison, not maths; fixed comparison to substituted matrices).
- c4c_03 numerical search: >8 min per restart, abandoned; no log; superseded by exact c4c_04.
- c4c_04 seg4 exact (sympy solve + Groebner) PASS=5: diagonal.
- c4c_05 forcing table + explicit covered-instance bands flat PASS=4.
- Tried by hand: caterpillar realisation of face-diagonal glider with emptiness-controlled
  involution layers -> boundary-shell conflict (argument only).
- NOTE.md written. Combined PASS=24 FAIL=1.
