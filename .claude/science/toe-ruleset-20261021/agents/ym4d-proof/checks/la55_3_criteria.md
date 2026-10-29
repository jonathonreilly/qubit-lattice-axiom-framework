# la55_3 — exact rational interval check of LINEAR_PACKAGE Theorem 4.2's strip conditions at the printed pairs (criteria first)
Written 2026-10-29 UTC before checks/la55_3_strip.py exists. Plain python, fractions.Fraction; no floats in any verdict.

Source: PROOF_session16_snapshot.md "Lemma EXP-strip (complex perturbation bounds)" (P1)-(P7) and "Theorem N2-exp" (definition of
eta_*): conditions rho_beta <= 1/2, e_Psi <= Psi_U/2, br_V >= (1/2)/((1+rho_beta)Gamma), and (4eta^2/psi_0 + 4eta/sqrt(psi_0))cosh(eta) <= 0.15,
with the quantities exactly as printed there (eps = e^eta - 1, eps' = (pi^2/4)eps, e_5 = (1+eps')^5 - 1, lambda, e_Z, c_Z, e_R, rho_beta, Psi_U,
e_Psi, psi_0 = 4r_0^2/pi^2 (so sqrt(psi_0) = 2r_0/pi exactly), br_V; Rbar = 1 + khat/(L^2-1) + kappa/9, b_* = min(kappa, 24/pi^2),
Gamma = max(pi^2/4, Rbar)).
Rigorous enclosures: pi in [314159265358979/10^14, 314159265358980/10^14]; e^eta and cosh(eta) by Taylor partial sums to degree 20 with a
remainder 2 eta^21/21!; every quantity is evaluated with the endpoint that makes the tested inequality hardest (monotone bookkeeping:
each of eps, e_5, c_Z, e_R, rho_beta, e_Psi is increasing in e^eta, cosh(eta) and pi; Psi_U is computed with lower bounds; br_V with lower
bounds; Gamma = pi^2/4 or Rbar taken at the upper pi when it enters a lower bound of br_V).

PASS criteria (pre-registered): at L = 3, for each printed pair
  (kappa=1, khat=1, eta=111/10000, r_0=57/100), (kappa=1/4, khat=1, eta=77/10000, r_0=37/100), (kappa=4, khat=1, eta=117/10000, r_0=65/100),
  (kappa=1/4, khat=16, eta=37/10000, r_0=1/4), (kappa=4, khat=16, eta=82/10000, r_0=3/5):
  S1: rho_beta_up <= 1/2; S2: e_Psi_up <= Psi_U_lo/2; S3: br_V_lo >= (1/2)/((1+rho_beta_lo)Gamma_up) [the right side is decreasing in rho_beta,
      Gamma, so its upper value uses rho_beta_lo, Gamma_lo — corrected to the hardest case: RHS_up = (1/2)/((1+rho_lo)*Gamma_lo)];
  S4: f0cond_up <= 15/100.
  The pair PASSES iff S1-S4 all hold. Expected (from the source's 30-digit claim): all five pairs PASS.
- CONTROL (designed to FAIL): the pair (kappa=1, khat=1, eta=200/10000, r_0=57/100) — at roughly twice the printed eta at least one of
  S1-S4 must fail; if it passes, the harness is not discriminating and the run is reported INVALID.
Exit 0 iff all five printed pairs pass and the control fails.
