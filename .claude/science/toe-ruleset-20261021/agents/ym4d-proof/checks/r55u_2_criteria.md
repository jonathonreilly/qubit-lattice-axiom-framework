# checks/r55u_2_criteria.md — Opus 5.5 reviewer (REVIEW55_TUNIF), written 2026-10-28T22:41:06Z UTC, BEFORE r55u_2_tu3poly.py exists

## What is tested
TUNIF.md Lemma TU-2 and Theorem TU-3 (twisted degree-2 division), by an implementation written independently of
checks/tu1_twisted.py (nothing imported from the lane). Unlike tu1 (numeric twists, z_1 = 1 + eps ladders), here z_1 and
z_2 are kept SYMBOLIC: every field is a bivariate polynomial in (Z1, Z2) with exact Fraction coefficients, z_3 (z_4)
are fixed rationals. So "the pole cancels" is tested as exact polynomial divisibility by (Z1 - 1), (Z2 - 1) — the
analyticity content of TU-1/TU-3 — not as a finite-epsilon growth rate. Twisted shift as in TUNIF §U4.1:
(D_mu g)(u) = f_mu(u) g(u + e_mu mod l) - g(u), f_mu = z_mu at u_mu = l - 1, else 1.

## Instances (fixed here)
d = 3 with l in {2, 3}; d = 4 with l in {2, 3}. z_3, z_4 drawn from {5/4, 3/7, 7/5, 1} (the value 1 = a resonant
transverse twist, included on purpose). Inputs F := D∧a with a a random 1-form whose entries are polynomials of degree
<= 1 in each of Z1, Z2 with random small rational coefficients (python random.Random(5555)); 6 instances per (d, l).
F is then exact, hence closed. The construction is never shown a.

## Construction (TU-3 as written)
Omega_b := E1 sigma_1(F_1b) (b >= 2); Phi := E2 sigma_2(Omega_2); mu := Theta_2(Omega_2) + sigma_2(Omega_2)/(Z2 - 1);
b_1 := -mu/l (independent of u_1); G_b := F_1b + D_b b_1; b_b := Theta_1(G_b) + sigma_1(G_b)/(Z1 - 1).

## Pre-registered verdicts
- r55u_2-R (removability = analyticity): every division by (Z2 - 1) and by (Z1 - 1) above is exact (zero remainder).
  PASS iff zero nonzero remainders over all instances.
- r55u_2-B (Lemma TU-2): Phi == 0 identically, D_b Omega_g == D_g Omega_b (b, g >= 2), and D_b mu == Omega_b (b >= 2),
  all as exact polynomial identities. PASS iff zero discrepancies.
- r55u_2-A (Theorem TU-3's equations): (D∧b)_{ab} == F_ab for all a < b, all sites, as polynomial identities. PASS iff
  zero discrepancies.
- r55u_2-C1 (designed-FAIL control: b_1 is load-bearing for analyticity). Same inputs with b_1 := 0: at least one
  instance must have a NONZERO remainder dividing sigma_1(F_1b) by (Z1 - 1). Fires iff so.
- r55u_2-C2 (designed-FAIL control: d >= 3 is load-bearing in TU-2). d = 2, l in {2, 3}, F_12(u) := 1 if u_1 = l-1
  else 0 (every 2-form is closed at d = 2; constant in p). Phi must be NONZERO (expected l). Fires iff so.
- r55u_2-C3 (designed-FAIL control: closedness is load-bearing). d = 3 and 4, l = 2: add 1 to F_12 at the origin of one
  exact instance. Must produce Phi != 0, or a nonzero remainder, or a discrepancy in A. Fires iff so.
- r55u_2-C4 (reporting only): the CONCENTRATED choice b_1 := -mu·1[u_1 = 0] also yields exact divisibility and exact
  equations (TUNIF says any b_1 with sigma_1(b_1) = -mu removes the pole; only the size differs). Reported either way.
