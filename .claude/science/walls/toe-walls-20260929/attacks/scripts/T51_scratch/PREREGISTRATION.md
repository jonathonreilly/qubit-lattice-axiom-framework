# T51 pre-registration (written before any T51 script ran)

Wall: mass pattern beyond the atmospheric gap (L10-W4). Constants as in
L10_scratch/diag_benchmark.py: alpha_LM = 2*0.045333918, M_Pl = 1.22089e19 GeV,
v = 246.3 GeV, y = 6.66e-3, light masses m = y^2 v^2 / M_R (universal Y, so
m_nu proportional to M_R^{-1}). Windows quoted by the repo itself
(PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION note:94-97): dm2_21 in
[6.92,8.05]e-5, |dm2_31| in [2.451,2.578]e-3, ratio in [0.0268,0.0328];
DESI-2024 Sigma m < 72 meV (NEUTRINO_RETAINED_OBSERVABLE_BOUNDS:150).

## Test A (closed form, S1): the lane's own Z3 texture M(r)=[[A,0,0],[0,rB,B],[0,B,rB]]
With U_e = I the singlet e1 is nu_e, so the solar pair contains the singlet
and R(r) = (m2^2-m1^2)/(m3^2-m1^2), m1=alpha*mB, m2=mB/(1+r), m3=mB/(1-r).
Claim to test (route R3, "misframed"): R(r) is monotone decreasing and enters
[0.0268,0.0328] only for a NON-perturbative doublet split r > 0.5.
 PASS (claim confirmed): window lies at r > 0.5 and R(r<=0.2) >= 0.4.
 FAIL: any window point with r <= 0.2.
Also test the IO branch (route R1): singlet = nu3, solar pair = the doublet.
 PASS: some r in the natural set {c*alpha^n} puts BOTH the doublet gap in
 [6.92,8.05]e-5 and the singlet gap in [2.451,2.578]e-3.
 WOUNDED if that holds but Sigma m > 72 meV (it will, ~100 meV).
 FAIL: no natural r does both.

## Test B (staircase-family scan, S2): the cheapest decisive test for the lane vocabulary
Enumerate RH spectra mu_i = c_i alpha^{k_i} M_Pl, k_i in 6..10, three states;
strict family c_i = 1 with the retained doublet factor (1 +- alpha/2) or
(1 +- alpha^2) allowed on one pair; loose family c_i in {1/2,1,2}.
Criteria (NO labels, lane accounting): atm dm2_31 in box, ratio in box,
Sigma < 72 meV.
 PASS for the lane vocabulary: >=1 strict-family spectrum meets all three.
 FAIL (wall stands in-vocabulary): 0 strict spectra meet all three; then
 report loose-family hits and the null hit-rate for log-uniform random
 triples with the same count of choices (look-elsewhere factor).

## Test C (outside route, S3): random-matrix ("anarchy") ensemble for M_R
Complex symmetric Gaussian M_R, Y = y0 I, m ~ singular values of M_R^{-1},
normalise m3 = sqrt(2.5e-3).
 Report P(R in window), P(R in window and Sigma<72 meV).
 R2 survives as a numerical statement if P(R in window) >= 1%; regardless of
 the number, it needs a measure on M_R, which realized_state_primitive
 (REALIZED_STATE_PRIMITIVE_NOTE:45) says is not supplied (no typicality claim):
 verdict capped at PRICED-at-a-primitive.
