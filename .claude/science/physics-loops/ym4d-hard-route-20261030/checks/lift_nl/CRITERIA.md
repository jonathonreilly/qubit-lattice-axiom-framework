# Criteria for `lift_nl_kill.py`, written before any run

Item `lift-repair`, commit `e6028aa14`. A run can refute or guide. It discharges nothing.

Model: SU(2), d = 2, L = 3, levels j = 1, 2, fine periodic lattice of side 27. The actual all-lines block map with axis-ordered comb contours, and the contour-free chain N^(j) with base point at the identity, as in Section 2 of `library/lift-nonlinear.md`.

In d = 2 the operator bound of Lemma LW is 2^d = 4 in place of 2^4, and d H = Wh_2 T^-1 d h.

**T1, hand arithmetic.** The commutator square: half real trace equals 1 - 2 sin^4 t to 1e-12, for t in (0, pi/2). (FD) holds on it. Fail otherwise.

**T2, (FD) at random.** 2000 random pairs of fields on a 4 x 4 torus, near and far from 1. (FD) holds in every sample. One violation is a FAIL of Lemma FD, and of this file.

**T3, Lemma LW identity.** Q^o Wh_1 T^-1 h = h on the actual linear path operator, to 1e-10, at j = 1, 2. Fail otherwise: the operators in the script are then not those of the note, and T4 is void.

**T4, the kill test of (LIFT-NL).** Base field U = e^{i a} with a of l^4 norm eps, in three kinds: random bond noise; a smooth field; a sum of fine pairs (high frequency, zero block average). Displacement h on level-j bonds: a compact bump, an exact level-j gradient, and a random compact field. Amplitudes: eps in {0.02, 0.05}, ||h||_{l^4} in {0.01, 0.03}. Solve log N^(j)(e^{i (a + H)}) = log N^(j)(e^{i a}) + h by the iteration of the proof, with no term from Lemma AD.

- (a) The iteration converges to 1e-10, in at most 30 steps.
- (b) D := ||Theta(e^{i a}, e^{i (a + H)})||_2 obeys D <= 8 ||d h||_2 + 8 (eps + ||h||_4) ||h||_4, that is the statement with the constant 4 doubled and with C = 8 on the second-order term, in d = 2.
- (c) No growth with level: the worst ratio D / (||d h||_2 + (eps + ||h||_4) ||h||_4) at j = 2 is at most 1.5 times the worst at j = 1.
- (d) The bound of (FD), A(a + H) - A(a) <= N D + D^2/2, in every case.

Any failure of (a) to (d) is reported as a failure of the statement in that regime, not tuned away. The constants in (b) are guesses at d = 2, L = 3. A violation by a factor at most 2 is reported and does not refute an unspecified absolute constant. A growth with level in (c) is what would matter.

**What this cannot establish.** d = 2, L = 3, two levels, three kinds of field. The critical norm in d = 2 is l^2, not l^4, so the l^4 statement is not the scale-invariant one here, and the check in (b) reads the d = 4 form only by analogy. A pass says the mechanism has no gross failure, such as a term from contours or frames that the proof missed. It says nothing about constants in d = 4.
