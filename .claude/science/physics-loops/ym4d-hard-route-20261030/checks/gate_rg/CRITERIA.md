# Criteria for gate repair-gate at 105283f2c, written before any run

All runs: SU(2), double precision, one job under the numeric lock, self-stop above 2 GB RSS.
Pass and fail are fixed here. A run can refute a claim or fail to refute it. It proves no bound.

## R1, counterexample, `r1_copy_parent.py`

Field of `library/paid-inputs-frozen-energy.md`, section 2, on the comb block map of `checks/gate_ex/ex_core.py`, d = 4.

- R1a. L = 5, 7, torus side 2L; four axis orders (identity, reversed, two others); a = 0.01, 0.1, 0.19. Max |log parent link| below 1e-12 for every order and a.
- R1b. Exactly 12 plaquettes have angle a within 1e-12 and all others are below 1e-12; Wilson action with tr 1 = 1 equals 12 (1 - cos a) within 1e-12.
- R1c. Copies in two adjacent blocks and in two blocks along direction 1: parent still below 1e-12.
- R1d. Controls that must fail, else the test is void: one link only, and the pair with equal signs. Each must give parent above a/20 somewhere at a = 0.1. An off-centre pair, at offsets +1 and -2, must also give parent above 1e-3.

## R2, Lemma (FR), `r2_derivative.py`

Lift of `checks/excess/v10_lift_su2.py`, L = 3, read as the map B in Psi_V(Y).

- R2a. At V = 1 and at a random pure-gauge V, d = 2 (Np = 8), d = 3 (Np = 8), d = 4 (Np = 4): central difference with eps = 1e-4 along a random Z with entries of size 1. Sup |D Psi Z - Z| below 1e-6. This reads every parent link, gauge directions included.
- R2b. Control that must fail: the same with the block gauge e^-phi removed. Sup error above 1e-2.
- R2c. d = 2, Np = 8, smooth V at three amplitudes each half the last. Full Jacobian by central differences. Row sum of ||D Psi - I|| over f: the three values agree within a factor 2, and the row sum falls by at least 1.5 per halving.
- R2d. Same Jacobian. Record the largest parent distance with an entry above 1e-8. Claim fails if it exceeds 68. The value is read, not bounded: on a torus of Np = 8 it can be at most 4 in sup distance, so this says nothing about range beyond the torus.

## R3, the inverse on squared flux, `r3_tail.py`

d = 2, Np = 16 if time allows, else 12, L = 3. A smooth bump of flux supported near one parent. Solve Psi_V(Y) = 0 by Picard to 1e-13.

- R3a. Picard converges, and M T(V) = V to 1e-12.
- R3b. Report max |Y| on shells in sup distance, against f^2. No pass criterion beyond |Y| <= f^2 times a constant stable under halving f, within a factor 2.

## R4, hierarchical weights, `r4_weights.py`

One-dimensional exact recursion for the compatible down-average: tent factor tau(z - y)/L in a plane direction, box factor 1[|z - y| <= r] in a transverse one. Top weight exp(nu y), L = 3, 5, 7, nu = 0.1, depth m = 1 to 6.

Claim under test, `library/excess-finite-range-repair.md` line 56: for orientation weights from one scalar top profile, W^+ <= exp(C nu_local) W with nu_local about nu L^-m.

- R4a. Let rho(m) be the largest log ratio of W_m^q(z') to W_m^q'(z), over orientations q, q' (box or tent in this direction) and neighbours |z - z'| <= 1. The claim holds if rho(m) L^m stays bounded over m (within a factor 2 from m = 2 to m = 6). It is refuted if rho(m) stays above nu/10 at m = 6.
- R4b. Fraction of level-m sites with log ratio above nu/10: reported.
- R4c. Control: the scalar interpolated profile, W_m(z) = exp(nu z L^-m), must have rho(m) = nu L^-m to 1e-12.

## Declared after the first runs

- R2d crashed on its first run: no block norm exceeded 1e-3 at that flux, so the threshold selection was empty. R2a to R2c had already printed, see `r2_first.log`. The same section was rerun as `r2d_range.py` with the empty case handled. Criterion unchanged.
- R1d, third control, failed as registered (off-centre pair, parent 1e-18). The expectation was wrong, not the field: the block weights are uniform in the transverse coordinate, so reflection is not needed. No rerun; the failure stands in `r1.log`.
- R3c, added after reading R3: fixed 10 Picard steps at the same three amplitudes, and the power p in max|Y| ~ f^p on each shell. The old tail of `parts/hard-core--excess.md`, Theta-tilde squared, asks p >= 2 + 2 s at s cells beyond the support of m. Refuted for this map if p is near 2 + s at s = 1. Indicative only: d = 2, L = 3, one field, and the code's window truncates the kernels.
