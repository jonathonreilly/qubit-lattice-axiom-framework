Ruleset B: the mode split is supplied, and its spin and family readings fail

Date: 2026-10-22
Type: bounded theorem (exact finite group/representation checks) plus gate verdict
Runner: scripts/frame_split_spin_family_tests_ruleset_b_2026_10_22.py (20 PASS / 0 FAIL)
Target: agents/minimal-toe-b (site modes C^2 (+) C^3, Lambda(C^5), frame group S(U2xU3))

Claim scope
-----------
This note checks three calculations that ruleset B names as decisive. All three are finite,
exact checks.
(1) Does information minimisation (IM) force the split C^2 (+) C^3?
(2) Is the qubit SU(2) both the direction unit and weak isospin?
(3) Do the three record-axis sectors give three families with a rank-1 mass matrix?
The note does not dispute the known group theory. Lambda(C^5) under S(U2xU3) is one SM
family, and the Z6 quotient holds (Baez and Huerta 2010). The note decides only whether
ruleset B DERIVES these inputs or SUPPLIES them.

1. The mode split is not forced
-------------------------------
Each candidate is scored by three cost measures:
- Kst = log2 dim Lambda = the number of modes n (bits of site state).
- KfU = dim U(n) - dim G, the number of frame parameters the law fixes when it preserves the
  split.
- KfB = dim Spin(2n) - dim G, the same count measured against the full exclusion-preserving
  (Bogoliubov) group.
The rule-text cost is the number of tokens in the rule. "+" and "x" cost the same, so this
measure is a tie.
Exact results (integer Cartan weights, cubic and gravitational anomaly tensors):
- Theorem 1a. The even half is chiral iff n is odd, for every block split and for the tensor
  product. The frame group S(U(a) x U(b)) has the full rank of SU(n), so its Cartan torus is
  that of SU(n). Chirality and perturbative anomalies are therefore fixed by n alone: the split
  cannot be selected by consistency.
- The tensor C2xC3 (n = 6) and the oriented links C2+C6 (n = 8) are vectorlike. The block
  form C2+C3+C3 is also vectorlike.
- Several candidates are chiral and anomaly-free, so this property is not unique to the SM.
  Besides C2+C3 (SM), these are C1+C4 (SU(4)xU(1) content: 1+6+4+1+4bar), C5 unsplit (SU(5)
  content: 1+10+5bar) and C1+C6 (n = 7, U(6) content).
- Least information fixed (the IM reading "privilege no frames") picks C5 unsplit. Its cost
  is KfU = 1, against 13 for C2+C3. Against Bogoliubov, the IM optimum is Spin(10) itself:
  C2+C3 fixes 33 of the 45 parameters. So IM points to the GUT frame group, not to the SM.
- Least state bits (Kst) overall picks C1+C3. It is vectorlike, with 16 states.
- Inconsistent unit counting. C2 counts the qubit's LEVELS as exclusive modes, which makes
  Lambda(C^2) four states, the size of two qubits. C3 counts each binary link as ONE mode.
  Counting both kinds the same way gives C1+C3, which is vectorlike.
- "Owned forward links" is a lopsided convention. Its stabiliser in O_h has order 6 of 48:
  that is 3 bits of convention, with no reason given. The symmetric choice, all 6 links, gives
  n = 7 or 8, and neither is the SM.
- C2+C3 is the unique Kst minimum only after conditioning on three inputs: the qubit counts as
  2 modes, the site has 2 blocks (direct sum), and the content is chiral. Chirality is a
  measured fact, not a consistency requirement.
Result: the split is a structural CHOICE made to reach the SM. Under the gate it is FITTED-like.

2. Double use of SU(2): the reading fails against measurement
--------------------------------------------------------------
- Theorem 2a. The commutant of S(U2xU3) on Lambda(C^5) has dimension 14. Ten sectors appear
  once each, giving an abelian part. The other two sectors, (0,0) and (3,2), are both Y = 0
  singlets and are isomorphic, so they give an M2. That su(2) acts only on |0> and |full>, and
  it annihilates every charged sector. So no spin SU(2) exists inside the site space.
- Theorem 2c. Under R2's reading (qubit SU(2) on the levels (+) SO(3) vector on the links), the
  rotation generators lie inside s(u2 (+) u3). Rotations would then be frame (gauge) changes.
  The resulting spin content is nu^c 0, e^c 0, Q {1/2, 3/2}, u^c 1, d^c 1 and L 1/2. Every
  measured SM fermion has spin 1/2, so the double-use reading is FALSIFIED, not merely open.
  The decisive case: e_R is a weak singlet with spin 1/2.
- Finite diagnostic 2e. A separate spin does exist on the 2^3 cell x qubit space (16 dims).
  It is the left-Clifford su(2), with j = 1/2, and it commutes with the qubit SU(2). It brings
  a 4-fold taste multiplicity: 16 = 2 spin x 4 taste x 2 qubit. Spin must therefore come from
  the cell, which means R2's "qubit = direction unit" literature route (Mueller and Masanes)
  cannot also supply isospin. The remaining "3 = 3" (Bloch axes = lattice axes) is a count,
  not a derivation of SU(2)_L.
- Finite diagnostic 2g. Suppose link mode i is the mode that transports along axis i. Then the
  axis-labelled transport on Z_3^3 breaks colour SU(3) to its Cartan torus:
  |[H, lambda_1]| = 14.7, while [H, lambda_3] = 0. Colour survives only if the update never
  uses which link a mode is. In that case the "3 = owned links" origin becomes decorative.

3. Families: the claim fails
----------------------------
- Theorem 3a. Rotating the record axis is an SU(2)_qubit frame change. The three
  "record-axis families" span 32 states, not 96: they are the same family written in three
  gauge-equivalent bases. No 3x3 family space exists.
- Theorem 3c. Suppose three copies are supplied by hand. A cubic rotation permutes the axes
  once for all fields, so the symmetry is the diagonal S3, not S3_L x S3_R. The invariant
  mass matrices under diagonal S3 are aI + bJ, a 2-dimensional space. A generic matrix in it
  has rank 3, with two degenerate light families. Rank 1 (democratic) needs a = 0, which is
  an extra rule. The S3_L x S3_R invariant space, by contrast, is 1-dimensional (J only).
  So "rank-1 democratic at leading order" does not follow from the ruleset.

Gate verdict (anti-smuggling)
-----------------------------
R4 FAILS the gate. Its mode split is not forced by IM. The IM readings that are actually
computed prefer C5/Spin(10), or C1+C3, and chirality enters as an observed selector. The
split is therefore a FITTED-like structural choice.
The spin/isospin double use is FALSIFIED against measured spin.
The family rule R5c FAILS: it gives no new states, and the rank-1 matrix is not forced.
Ruleset B does NOT survive the gate as a derivation of the SM.
What does survive is the known exact statement that Lambda(C^5) with the S(U2xU3) split gives
one SM family with Z6. That statement is valid only as a supplied-split identity.

Repairs worth testing (UNTESTED)
--------------------------------
(a) Derive the frame group as Spin(10) or SU(5), the IM optimum. The breaking to S(U2xU3)
    would then have to come from dynamics, which is where the qubit/link distinction belongs.
(b) Take spin from the 2^3 cell, with 4 tastes, and require that the taste structure, not the
    record axis, carries the family question.
(c) Make the update link-label-blind, so that colour is exact.

Smuggling review
----------------
Supplied:
- the qubit counted as 2 modes;
- the direct sum;
- the owned-forward orientation;
- chirality as a selector;
- three family copies;
- S3_L x S3_R in place of the diagonal S3.
Forced (exact): chirality iff n is odd; anomaly freedom for odd n >= 5; the commutant; the
spin content under R2; the span rank 32.
The only measured input is the spin 1/2 of the SM fermions.
