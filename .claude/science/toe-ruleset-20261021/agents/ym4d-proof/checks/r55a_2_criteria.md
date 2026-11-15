# r55a_2 — criteria (written BEFORE the script). Reviewer: claude-opus-5-5, batch C6 (REVIEW55_ARS.md)

Exact rationals throughout (fractions.Fraction), plain python3 -I, no floats, no numpy/BLAS. Every log10 is a
RIGOROUS RATIONAL ENCLOSURE [lo, hi] (atanh series with an explicit remainder bound; ln10 = 3ln2 + ln(5/4)); every
square root is an integer-isqrt enclosure. "REPRODUCES" means the whole enclosure lies within the stated tolerance of
the quoted figure. Tolerance = half a unit in the last quoted digit (e.g. 82.1406 -> 5e-5; -15.617 -> 5e-4).

## Inputs (located by string; line numbers as found today)
- A_d(L) = (d-1)L(L-1)/2 = 9 at d=4, L=3 — RLARGE "A_d(L) := (d - 1)L(L - 1)/2 (= 9 for d = 4, L = 3)".
- eta_RS := min{eps/18, eps^2/(4608N)} — RLARGE l.64 / l.976 / l.1009 ("eta_1 := min{...}").
- eta_q := min{eps/18, eps/(2304N), delta_0/9}, delta_0 := min{1/(640N), 2/N^3} — HIST "Lemma PM", "Lemma RS-lin".
- eta_KN := eps/117 (c_1 = 1/(2(L^2+5.5A_d))) — EXISTENCE "Corollary KN-step".
- a_eta(eta) := eta^2/(2N) (bare value) — RLARGE l.981 (R5), l.1026; a_RS := min{a_eta, kappa eps^2/(256N)} — RLARGE l.1020.
  kappa: symbolic in RLARGE; example values 1 and 1/4 (SYMBOLS §6.5 citing PROOF). Default kappa = 1, as all batch files use.
- c_RS = 625 (RLARGE l.1021, RS greedy); RS-joint c_RS = 81 (RLARGE l.435; HIST "c_RS = 81 against 5^4 = 625").
- DX' = 2.456e-152/C_Omega (REVIEW_SF_S7 l.203 "DX'-1 reproduced ... (iii)") and the rounded 2.5e-152/C_Omega
  (RLARGE l.618; REVIEW_SF_S7 l.335). C_Omega = 1 as in every batch file. Ceiling convention g^2 <~ a/10^2 (RLARGE l.617).
- eps values: 6.7e-40 (RLARGE l.71-72 "TB-1: ~ 6.7e-40"), 9.52e-40 (RLARGE l.71), 8.95e-40 and 1.27e-39 (RLARGE l.611 row),
  proposed 9.38495112638e-45 (EPS1_SWEEP l.455, as quoted in ARS_FIX/KN_ADOPT; owner-gated).
- live a = theta * a_bad, a_bad = c_pr*eps^2 (eps < t_pr, RLARGE l.93), c_pr = c_flat/C'^2 = (1/640)/53^2 (RLARGE l.90-91),
  theta < 1/24 strictly (RLARGE l.88 CAP-1; l.612 "theta < 1/24"): evaluated at the supremum theta = 1/24.

## Checks and pre-registered verdicts
- G1 GAIN = 2 log10(4608N/(117 eps)) (kappa-free while the plaquette branch is active in both forms) at
  (6.7e-40, N=2) vs 82.1406 & 82.141; (6.7e-40, N=3) vs 82.4927; (9.38495112638e-45, N=2) vs 91.8478 & 91.848;
  (proposed, N=3) vs 92.2000.  Each: REPRODUCES / DISAGREES.  Also the direct form log10(a_RS^lin/a_RS^quad)
  computed from the min-formulas (not the closed form) must equal the closed form exactly: CLOSED-FORM-EXACT / FAIL.
- G2 margin log10((a_RS^quad/100)/DX') at eps=6.7e-40, N=2, kappa=1: with DX'=2.456e-152 vs ARS_FIX -15.617;
  with DX'=2.5e-152 vs ARS_BIND A6 -15.62479. With the c_RS=625 divisor (DX'=2.456e-152) vs -18.413.
  Linear form vs +66.523 / +63.728.  Each: REPRODUCES / DISAGREES.
- G3 live a and its margin: a at eps=6.7e-40 vs 1.040415e-86 (ARS_BIND A7; tolerance 5e-7 relative);
  margin with DX'=2.5e-152 vs +63.61927; with DX'=2.456e-152: report. ATTRIBUTION verdict on ARS_BIND §6's
  "the review carried -15.617 where the exact figure is -15.6248": the difference between the two -15.6x figures
  equals log10(2.5/2.456) to 1e-6 -> DIFFERENT-DX'-INPUT (ARS_BIND's attribution is wrong); else OTHER.
- G4 route ratios: (eta_KN/eta_q)^2 and (81/625)(eta_KN/eta_q)^2 at eps=6.7e-40 for N=2,3:
  vs 1551.148, 201.029, 3490.083, 452.315 (and log10 of the per-cube ratio vs 2.3033 / 2.6554).  REPRODUCES / DISAGREES.
- G5 eta ratios.  (a) eta_KN/eta_q at eps in {6.7e-40, 1e-3, 0.39, 2/5, 0.41, 1, 2}, N in {2,3}:
  EXACT-256N/13 iff value == 256N/13; the batch claim "ORDER-REVERSED by 512/13 (768/13) AT EVERY eps_1" is
  REFUTED-AS-UNIVERSAL if any tested eps in (0,2] gives a value != 256N/13; REVERSAL-HOLDS iff every value > 1.
  (b) RLARGE l.65 as written today: for every tested eps in (0,2], N in {2,3}: either eta_RS <= eta_q or the delta_0/9
  entry is the active entry of eta_q.  L65-TRUE-AS-WRITTEN iff this holds at every tested point; else L65-FALSE.
  Control: dropping the "unless delta_0/A_d binds" clause must produce a violation somewhere in (0,2] (else NO POWER).
- G6 branch of a_RS.  (a) post-adoption: a_eta(eta_KN) <= kappa eps^2/(256N) iff kappa >= 128/13689, for
  eps in {1e-40, 1e-3, 1/2, 2, 814, 815, 1000}, N in {2,3}, kappa in {128/13689*(1 -/+ 1/1000), 1/4, 1}:
  BOUNDARY-KAPPA-ONLY iff the active branch is decided by kappa alone at every tested (eps, N); and
  "814.587" is STALE iff at kappa = 1 no branch change occurs between eps = 814 and 815 (or anywhere tested).
  (b) pre-adoption (current eta_RS) at kappa = 1, N = 2: a_eta active at eps in {1, 511, 513, 700, 814, 815, 1000, 10^4}?
  ALWAYS-PLAQUETTE -> ARS_FIX §2.1's "active iff eps_1 < 814.587" is REFUTED-AS-IFF (immaterial at live eps).
  Control: at kappa = 1/100 (< 32/81) the pre-adoption branch MUST change somewhere in the tested set (else NO POWER).
- G7 Codex F4's re-centring-free linear threshold eta_F4 := min{eps/18, eps/(32 sqrt(N) A_d)} (kernel exponent
  kappa eps^2/(256N), same as RS and KN).  Report the enclosure of D := 2 log10(eta_KN/eta_F4) = 2 log10(288 sqrt(N)/117)
  at N = 2, 3 and of 2 log10(eta_F4/eta_RS) at eps = 6.7e-40.  Verdict RECENTRING-SHARE := D (decades of the 82.14 that
  need re-centring); pre-registered reading: if D < 1.5 at N=2 and N=3 -> "most of the gain does not need KN", else
  "KN needed for a material part".  (This is a report, not a PASS/FAIL; the algebra of F4 is checked by hand in the review.)
- G8 RS-lin joint per-cube exponent a_eta(eta_q)/81 at eps=6.7e-40, N=2 vs 6.52499e-89 (REVIEW_ARS_EPS_S1 RA-17) /
  6.524987e-89 (ARS_BIND A3); log10(a_live/that) vs ARS_BIND's 2.20263.  REPRODUCES / DISAGREES.
- G9 C_Omega at which the a_RS "breach" reverses: (a_RS^quad/100)/DX'(C_Omega=1)... i.e. 10^{-margin}: with DX'=2.456e-152
  vs REVIEW_ARS_EPS_S1 4.14e15; with 2.5e-152 vs ARS_BIND 4.2149e15 (relative tolerance 5e-4).
## Power
G2/G3 must separate the two DX' inputs by >= 0.005 decades (else the attribution test G3 has no power).
G5(b)'s control and G6's control are the designed-FAIL controls named above.
