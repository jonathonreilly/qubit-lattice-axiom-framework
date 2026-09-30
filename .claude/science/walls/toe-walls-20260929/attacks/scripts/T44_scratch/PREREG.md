# T44 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family checks).

## What is tested
Wall T44 = L09-W3 + L09-W12: the CKM atlas's building blocks (lambda^2 = alpha_s/n_pair,
A^2 = n_pair/n_color, r^2 = rho^2+eta^2 = 1/n_quark, cos^2 delta = 1/n_quark, alpha_s(v) =
0.1033038) are supplied identifications, and the agreement with data (about 1%) cannot be scored.

Data (PDG 2024 CKM review, fetched 2026-09-29; local text copy pdg2024_ckm_review_text.txt):
s12 = 0.22501 +- 0.00068, s23 = 0.04183 (+0.00079 -0.00069), s13 = 0.003732 (+0.000090 -0.000085),
delta = 1.147 +- 0.026 rad, J = 3.12e-5. Wolfenstein: lambda = s12, A = s23/lambda^2,
r = sqrt(rho^2+eta^2) = s13/(s23 lambda) (exact from the standard definitions), delta.

## Tests and readings (fixed now)
S1 Scoring. Pull of the atlas (lambda, A, r, delta, |Vub|, |Vcb|, J) against PDG.
  Reading A: if the lambda pull > 3 sigma, the leading-order atlas is excluded as a formula with
  zero theory error, and any success must be stated with an explicit NLO/scheme error >= the
  observed lambda deviation (about 1%). If all pulls < 2 sigma, the atlas is scoreable and consistent.
S2 alpha_s scheme. alpha_s needed to hit lambda exactly; lambda predicted from MS-bar alpha_s(v)
  (2-loop run from alpha_s(M_Z) = 0.1180). Reading: if MS-bar alpha_s(v) gives lambda more than
  3% off, the fit depends on the lattice-scheme number 0.1033 (identification B4 does numerical work).
S3 Category swap. Put the 1+5 weight on the 3-dim generation space (n=3) instead of the 6-dim
  block; recompute |Vub|, delta. Reading: if |Vub| or delta move by more than 3 sigma, the
  6-block reading is numerically load-bearing (the lane's suggested test 1 is answered "yes").
S4 Look-elsewhere. Grammar: lambda^2 = alpha/a, A^2 = p/q, r^2 = 1/b, cos^2 delta = 1/c with integers
  from a set S. Grammars: S_SM = {2,3,6}; S_6 = {1..6}; S_12 = {1..12}. Slots independent; also a
  tied version (b = c, the atlas's own Thales tie). Tolerance: the same relative tau on lambda, A, r,
  delta (delta in degrees), tau in {1.5%, 3%, 5%}; variant with lambda tolerance 10% (scheme-unscoreable).
  Null: mock worlds from a prior fixed here: lambda log-uniform [0.05, 0.5]; A uniform [0.4, 1.4];
  r log-uniform [0.1, 1]; delta uniform [20, 90] deg. Second null: real values times log-uniform
  factors in [1/1.5, 1.5]. p = fraction of mock worlds where at least one grammar member hits all four
  (the trial-corrected chance probability); N = 400000 mocks, fixed seed 44.
  Readings on the tied S_SM grammar at tau = 3%: p < 0.01 -> the fit is evidence (about 2.5 sigma or
  more) worth deriving; 0.01 <= p < 0.1 -> weak; p >= 0.1 -> no evidence. Same reading for S_6, S_12.
  Also: real-data multiplicity (how many grammar members hit) per grammar.
S5 Commuting lemma. Random Hermitian H_u = f(K), H_d = g(K) (same eigenbasis) give |V| a permutation
  matrix; 1000 random cases, tolerance 1e-10. Reading: if any case gives a non-permutation, the
  MFV/flavour-blind kill of coupling-derived CKM is wrong.
S6 Runner inspection (no run): the 1/6 in the atlas runner is hard-coded as 1/QUARK_BLOCK_DIM.
  Reading: if the runner's CP weights are computed from the Green function delta_A1, the K_R
  machinery is load-bearing; if hard-coded, it is not.

Pass/fail is on the readings above. No reading is changed after seeing results; deviations are
recorded in RESULTS.md.
