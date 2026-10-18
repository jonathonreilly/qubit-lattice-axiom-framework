# R5 (code-distance exponents) pre-registration — written before any run, 2026-10-18

Same-family worker (Opus 5.5). Nothing here is refereed.

## T1  Leakage exponent depends on the protection reading (small codes, exact)
Codes: bit-flip repetition code n = 3, 5, 7 (distance d = n against X errors); [[5,1,3]] code.
Readings, per rung:
 (a) Hamiltonian: H = -sum(stabilisers) + eps * sum_j h_j (X fields for repetition; random single-qubit fields for [[5,1,3]]).
     Observable: ground-doublet splitting. Prediction: slope d.
 (b) Coherent rung + decoder: U = exp(-i eps sum X_j), then syndrome measurement and minimum-weight correction.
     Observable: logical transfer-matrix eigenvalues lambda = |lambda| e^{i theta}. Prediction: theta ~ eps^d, 1-|lambda| ~ eps^{d+1}.
 (c) Pauli (stochastic) rung + decoder: independent X flips with probability p. Prediction: theta = 0 exactly; 1-lambda ~ p^{ceil(d/2)}.
 (d) Passive (no decoder per rung), N rungs of (c) then one decode. Prediction: failure ~ (N p)^{ceil(d/2)}, so no constant per-rung exponent.
Readout: fitted slopes at small eps / p. PASS if slopes are within 0.15 of predictions.

## T2  Data test of code-natural fixed exponent patterns, random control, parameter count
Masses: the three recalled sets used by HIER-2 (MZ, GUT, MIX); CKM |V_us| = 0.225, |V_cb| = 0.041, |V_ub| = 0.0037 (recalled).
Menu of code-natural patterns (exponents light -> heavy), fixed now:
  LIN  (3,2,1)  distance proportional to an integer size (L, 2L, 3L)
  CAT2 (4,2,1)  concatenation, d = 2 coherent or d = 3 decoded (2^r)
  CAT3 (9,3,1)  concatenation, d = 3 coherent (3^r)
  ODD  (5,3,1)  consecutive odd orders (chirality-odd mass rule)
Models:
  A  one pattern for all sectors, one continuous eps, per-sector scale Lambda_f: 4 continuous params, 4-way discrete choice, 9 data.
  B  per-sector pattern and per-sector eps_f and Lambda_f: 6 continuous params, 4^3 discrete choices, 9 data.
Fit: minimise max |ln m_fit - ln m_obs| (Chebyshev).  Readout factor F = exp(max dev).
Control: 2000 random spectra; per sector the heaviest mass is kept, the two lighter log-masses are drawn uniform in
  [ln(1e-6 m_heavy), ln m_heavy] and sorted.  p = fraction of random spectra with F_random <= F_data.
CKM (FN reading, doublet distances a = pattern): |V_12| ~ eps^{a1-a2}, |V_23| ~ eps^{a2-a3}, |V_13| ~ eps^{a1-a3},
  with eps free; report the best max factor over the three entries for each pattern.
Readings:
  R5-SUPPORT: some pattern fits all 9 within x3 under model A AND its CKM within x3 AND p <= 0.05.
  R5-NO-POWER: data fit, but p >= 0.2 (random spectra fit as well).
  R5-FAIL: no menu pattern fits under model A within x3.
  OPEN otherwise.

## T3  Data processing as a c-function (Q1), finite-dimensional illustration
 (i) qubit channel = amplitude damping (gamma) after a z-rotation (phi): check complex eigenvalue pair with |lambda| < 1
     and monotone D(Phi^n rho || sigma) along the orbit (an attracting spiral is consistent with DPI).
 (ii) qubit (x) qubit channel: unitary rotation by 2 pi / 5 on a protected qubit, depolarising on the other:
     check peripheral eigenvalues e^{+-2 pi i/5}, a period-5 cycle of states, DPI equality along the cycle.
 (iii) 200 random channels with full Kraus rank: check no peripheral eigenvalue except 1 (no cycles).

## Dated addendum (after the runs)
- T1: for n = 7 the Pauli p-grid was moved to [2e-3, 1e-2] after the first run, because 1 - lambda ~ 1e-15 at p = 1e-4 sat at machine precision (first slope 4.33, rerun 3.99). Readings unchanged.
- T2b (t2b_ckm_split.py) was added after seeing T2: the CKM in the left-right symmetric split (a_L = a_R = p/2) at the mass-fit eps.
- Disclosure: while reasoning before this PREREG was written I had computed the observed shape statistic R
  (about 2.1, 1.8, 2.9 for up, down, leptons). The menu was chosen on code grounds, but its p-values are not blind.
