# T29 pre-registration (written BEFORE any production run)

Wall T29 = L06-W6 + L16-W4 + L07-W6: (B1) <P>(beta=6)=0.5934 is an admitted number, never certified;
(B3) the vertex power (alpha_LM = alpha_bare/u0 vs alpha_s(v) = alpha_bare/u0^2) is declared.

## Test 1 (B1): run the repo's own Stage-1 MC certification protocol, reduced
Source protocol: docs/PLAQUETTE_MC_CERTIFICATION_PROTOCOL_NOTE_2026-06-11.md section 3 (steps 1-9, bands A-D).
Never run before (L07-W6: "a plan, not a run"). The FSS note (L=3..8, Metropolis) gave 0.59400 +/- 0.00037.

Setup: SU(3), Wilson, beta = 6 exactly, periodic L^4, P = Re Tr U_p / 3.
Code: compiled C, Cabibbo-Marinari heatbath (Kennedy-Pendleton SU(2)) + 4 overrelaxation per sweep.
Independent algorithm for gate 1: Metropolis with symmetric SU(2)-subgroup proposals (same C file, mode 1).

Gates (all must pass before the production number is read):
 G1 algorithm cross-validation at L=6: HB+OR and Metropolis agree within 2 sigma (protocol step 1).
 G2 start-state gate at L=8: cold and hot start agree within 2 sigma (protocol step 4).
 G3 prior-code gate at L=4: HB+OR reproduces the repo smoke 0.59601(78) and probe-T31's 0.5970(4) within 2 sigma
    of the combined error (both are independent earlier codes on 4^4).
 G4 unitarity: max |U U^dag - 1| < 1e-10 after each sweep (checked in code).

Extrapolation: P_L = P_inf + c L^-4 fit over L in {6,8,12,16} (protocol step 6 form).
Fit quality gate chi2/dof < 2; plus |P_16 - P_12| reported.

Decision (repo bands, d = P_inf - 0.5934):  A |d|<=5e-5;  C 5e-5<|d|<=1e-4;  D |d|>1e-4.
My total error will be ~1-3e-5 (grade 4, not grade 5). Reading rule:
 - PASS-for-the-license (B1 admitted value survives) iff |d| <= 5e-5 at 2 sigma_total  [Band A].
 - FAIL (license broken, Band C/D) iff |d| - 2 sigma_total > 5e-5.
 - otherwise UNDECIDED at this grade.
My prediction, recorded before running (from memory of the literature value ~0.5937): Band D, d ~ +3e-4,
so v_cand = 246.28 GeV moves by ~ -0.2% (elasticity -4), i.e. the quoted 0.026% agreement is lost.
If the run instead lands in Band A, the prediction is wrong and B1 survives at grade 4.

## Test 2 (B3, power <-> scale dictionary): same configurations, Wilson loops W(R,T), R,T<=4
Question: alpha_bare/u0^n for n = 1, 2, 4 -- at what length r_n does the lattice's own static-force coupling
alpha_qq(r) = r^2 F(r) / C_F  equal that value?  Creutz ratios chi(R,R) give F at r ~ R - 1/2.
Pre-registered reading:
 - If alpha_qq(r=1.5a) (from chi(2,2)) > alpha_bare/u0^n for every n in {1,2,4}, then no power is fixed by any
   resolvable lattice observable: all n map to r_n < 1.5a via the one-loop pure-gauge dictionary, so the vertex
   power is a scale choice (B3 is B4/T30 in disguise). Predicted: this holds (alpha_qq(1.5a) ~ 0.2+).
 - If instead some n has alpha_bare/u0^n >= alpha_qq(1.5a) then n is tied to a resolvable scale (reading fails).
One-loop dictionary (nf=0): 1/alpha(q2) - 1/alpha(q1) = -(11/(2 pi)) ln(q2/q1)   [b0 = 11 for SU(3)].

## As-run deviations (added after the run; the readings above were not changed)
- L=16 ran at ~2.5 s/sweep under CPU contention; only one short chain (162 samples) finished, so FV control rests on my L=12 plus the repo's 16^3x32 and 24^3x48 ensembles (outputs/alpha_s_wilson_loop_production). Not L=24,32 of my own.
- Achieved grade 4 (stat 2e-5, FV systematic ~5e-5), not grade 5.
- Protocol step 6 (L^-4 fit) was run and reported; it fails its chi2 gate, so no ansatz was used for the decision. The decision uses the direct large-volume points.
- Prediction (Band D, d ~ +3e-4) was borne out: d = +3.3e-4.
