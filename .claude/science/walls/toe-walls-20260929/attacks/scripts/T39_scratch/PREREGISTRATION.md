# T39 pre-registration (written BEFORE running test1_classes.py and test2_joint_point.py)

Wall: derive delta = 2/9 as a bare radian in the Brannen form sqrt(m_k) = a(1 + 2 sqrt(r) cos(delta + 2 pi k/3)).

## Test 1 (misframing test): is 2/9 rad the only low-complexity "native" angle in the data window?
Question it answers: the wall says "exact rational -> radian". The MISFRAMED alternative says:
"maybe the true delta is a lattice-native algebraic angle (arg of an algebraic number, or arccos of a
small rational, or a q*pi angle) that merely sits near 2/9". Lindemann-Weierstrass makes those angles
never equal to 2/9, so if any of them fits the data as well as 2/9 at lower or equal complexity, the
wall is optional/misframed; if none does, 2/9 (bare rational) is singled out and the wall is real.

Data: charged-lepton pole masses, two vintages (note-era PDG2020, PDG2024). delta_fit and sigma from
a 20000-draw Monte Carlo on the mass errors (as the lane did). Fundamental domain of delta:
[0, pi/3] (symmetries delta -> -delta, delta -> delta + 2pi/3).
Classes (complexity = height bound): A: (p/n)pi; B: bare rationals p/q; C1: arctan(y/x) (Gaussian integers);
C2: arccos(p/q), arcsin(p/q); C3: arg(x + y*omega) (Eisenstein integers, the C3 lattice);
C4: arccos(sqrt(p/q)); C5: (1/3) arccos(p/q) i.e. cos(3 delta) = p/q rational (the only spectral invariant).
For each class: smallest height with a hit inside 1 sigma and 3 sigma, number of candidates up to the height of
2/9 (height 9), and null-expected hits = (number of candidates) x (window width)/(pi/3).

PASS reading (wall real, 2/9 singled out): 2/9 is a 1-sigma hit; NO other class has a 1-sigma hit with height <= 9;
the null-expected number of 1-sigma hits from all classes together at height <= 9 is < 0.1.
FAIL reading (wall optional / MISFRAMED): some non-bare-radian class (A, C1..C5) has a 1-sigma hit with height <= 9
(comparable complexity), so 2/9 is not singled out by simplicity.
INCONCLUSIVE band: classes hit only at height 10-30.

## Test 2 (joint point): do the two Brannen numbers select the same natural point of one family?
Family (from AC_RETA source-response note 2026-09-02 and the Frobenius isotype note 2026-04-21):
A = a_s P_s + a_d P_d (positive, K-even, C3-equivariant). Typing 1 (AM-GM equipartition of the B_{alpha,beta} block
energies, Frobenius note): r = (a_s/a_d)/2. Typing 2 (source response): Phi = tau(A^-1 P_d) = 2/(3 a_d), delta = Phi/3
(i.e. delta = 2/(9 a_d)). Data window: (r, delta) from the lepton Monte Carlo.
Question: is the natural point A = I (a_s = a_d = 1; det A = 1 and Tr A = 3) inside the 1-sigma joint region, and is it the
ONLY point with all-small-rational (a_s, a_d) (numerator, denominator <= 12) inside the 3-sigma region?
PASS reading: A = I is in the 1-sigma region and is the unique small-rational point in the 3-sigma region.
FAIL reading: the region excludes A = I, or contains other small-rational points (then the "one natural point" reading has
competitors).
Also record (not a pass/fail): quark sectors (r_u, r_d at M_Z) against the sector-extended predictions of the same typings
under three normalisation rules (a_d = 1, det A = 1, Tr A = 3).

## AMENDMENT (still before running test1/test2; made after running common.py and estimators.py, which are data summaries, not the tests)
estimators.py showed the "within 1 sigma" window depends on the estimator: with r = 1/2 imposed and (a, delta) fitted to
(m_e, m_mu) (both known to ~1e-8) delta = 2/9 - 1.75e-7 (PDG2020 and PDG2024 alike); e-tau and mu-tau estimators give
-1.4e-6, +1.2e-5 (note era) and -6e-7, +4.3e-6 (PDG2024); the r-free three-mass fit gives +7.4e-6 (note-era) / +2.5e-6 (PDG2024)
with MC sigma 8.3e-6 / 6.2e-6. So Test 1 uses THREE windows for delta around 2/9 (half-widths):
  W_tight = 1.0e-6   (r=1/2 fixed, e-mu estimator and e-tau estimator both inside)
  W_mid   = 2.5e-5   (3 sigma of the r-free PDG2024 fit; contains every estimator except mu-tau note-era)
  W_lane  = 5.3e-5   (the lane's own 1-sigma, r=1/2 fixed, a = sum/3 estimator)
Centre of the windows: delta_c = 0.2222222 + (offsets are all inside the widths) -> centre taken at 2/9 itself is NOT allowed
(that would be circular); centre = delta_fit(e,mu | r=1/2, PDG2024) = 0.22222205.
Pass/fail readings as above, applied per window. Expected: because Lindemann-Weierstrass forbids algebraic-arg = 2/9,
"PASS" means only that 2/9 is singled out by simplicity, not that it is derivable.

## Test 2b (added before running): determinant-power fork
Second typing of the T38 bit: the once/twice bit is the determinant exponent p on the doublet (det_C = p 1/2 of det_R; p = 1 default
KD realisation gives r = 1, p = 1/2 gives r = 1/2). The 09-02 response is the log-derivative of that same determinant:
delta = p * 2/(9 a_d) (p=1: rank-2 log-derivative 2/a_d; p=1/2: 1/a_d). Table over p in {1, 1/2}, a_d in {1/2, 1, 2}.
Prediction (algebra): only p/a_d = 1 gives delta = 2/9; with p = 1/2 (needed for r) that forces a_d = 1/2, so the 09-02
"A = I" (a_d = 1) route and a count-once T38 do NOT meet in this typing. PASS = the table shows exactly that; FAIL = another
(p, a_d) with r = 1/2 also reproduces the data. Also added: scale-free variant Phi = Tr(A^-1 P_d)/Tr(A^-1) = 4r/(1+4r).
