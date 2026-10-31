# checks/p6_criteria.md — PRE-REGISTERED criteria for check p6 (PLD lane E, session 6)

Written 2026-10-28, BEFORE checks/p6_pld.py exists. Every input below is a constant RECORDED in another file or in an
earlier session of this file; **no constant derived in session 6 appears in any criterion**. Sources are named inline.

Scope: exact integer / rational arithmetic (`fractions.Fraction`) and elementary float arithmetic in plain python 3,
single thread, no numpy, no BLAS, no linear algebra, no sampling. Per the session-24 brief ("Exact rational/symbolic
arithmetic in plain python (no BLAS) is cheap and does not need the lock") the numeric lock is NOT taken; the run is
recorded (nice, threads, load, timing) in checks/p6_time.txt all the same.
Nothing here tests (CLS-min), (LCR), (CEM^COL), (CEM-1), (CEM-2), (E2^F), (J-NS^cd), Theorem CRC-2T, the lattice measure,
or any nonabelian statement. Every verdict is arithmetic about recorded numbers and about the bounds PLD/HW already state.

## Recorded inputs (quoted, not re-derived)
- c_pr = 1/(640·53²) (RLARGE l.90: c_pr = c_b/C'², c_b = 1/640, C' = 53 at N = 2, L = 3); a_bad = c_pr·eps_1².
- eps_1 = 6.7e-40 (RLARGE §0 / l.839, the (TH-ch'') admissible threshold; g-independent).
- g_K^2 = 1e-94 (PLD §16.8's (RLF-delta) ceiling, quoted by HW §30.6 l.1635).
- a = theta·a_bad = 1.0e-86 (HW §30.6 l.1634; RLARGE l.94 "a <~ 1e-86").
- theta ceiling 1/24 from max{6theta,24theta}(1+2Rg_K^2) < 1 (HW CAP-1); lambda = 1/2 (PLD §16.5's fixed choice).
- n_int = 216 (PLD §16 index convention); L = 3, d = 4; 3 = dim su(2).
- HW §30.4 constants: b_n = 531441·38418·c_plus + 38417·c_U; b_D = 38416·(531441·c_plus + c_U); c_att(8) = 1229313;
  g2_CRC = a/(b_n + a·R + log(12800·C_ell)) (HW §30.6 l.1639).
- HW §30.6 recorded value: g2_CRC ~ 4.9e-97/c_plus; "b_n ~ 2.04e10·c_plus"; n_sharp growth factor ~1e10.
- Delta_sh = 3073361 and its formula 81 + 2401·32·80·sum_{m>=1}3^{-m} (PLD §16.6 (b), §16.7, p4 E4); p4 D2b measured
  per-cube excess 256.
- Detached-cube shadow growth: 81 at the first level, 256 per level thereafter (PLD §16.6 (b), HW §30.2 Reading).
- a_ret/a_bad = 8.03e-7 (PLD §16.8, p4 E); lambda_min candidates 3.17e-3 (PLD §16.8, RLARGE §0) and 6.6e-10
  (REVIEW_PLD_S3 fix L0-1 via Proposition RW-l2, PROOF l.5322-5325).

## Criteria (each with its PASS/FAIL verdict fixed here)

**A1 (rigorous, exact rational).** c_pr = Fraction(1, 640·53²) and kappa_min := 256·c_pr/(24·lambda) at lambda = 1/2.
PASS iff c_pr == Fraction(1,1797760) AND kappa_min == Fraction(1,84270) AND float(kappa_min) < 1.2e-5. Else FAIL.

**A2 (rigorous identity + recorded value).** Claim of PLD §18.7.2: with u = 1/g_K^2, the quantity u·eps_1² equals
(eps_1/g_K)² identically, and at the recorded g_K^2 = 1e-94, eps_1 = 6.7e-40 it lies in [4.0e15, 5.0e15].
PASS iff |u·eps_1²/(eps_1/g_K)² - 1| <= 1e-12 AND u·eps_1² in [4.0e15, 5.0e15]. Else FAIL.

**A3 (negative control for A2).** At eps_1 := g_K (i.e. eps_1 = 1e-47) the same quantity must equal 1 exactly, so the
"gap" of A2 is the gap and not an artefact of the formula. PASS iff |value - 1| <= 1e-12. Else FAIL.

**B1 (rigorous, exact integer).** HW's b_n, b_D at (c_plus, c_U) = (1,1) and at (82,82) (the one-extra-R-free-ring cost
of PLD §18.4: c_plus = c_A + c_U becomes c_A + 82·c_U). PASS iff b_n(1,1) == 20416938755 exactly, AND
floor(b_n(1,1)/1e10) == 2 (i.e. HW's "~2.04e10" is reproduced), AND b_n(82,82)/b_n(1,1) <= 82, AND
b_D(82,82)/b_D(1,1) <= 82. Else FAIL.

**B2 (rigorous arithmetic against a recorded value).** g2_CRC := a/b_n with a·R and log(12800·C_ell) set to 0 (HW keeps
them symbolic), c_plus = c_U = 1. PASS iff |g2_CRC/4.9e-97 - 1| <= 0.10 (HW's recorded 4.9e-97/c_plus reproduced), AND
g2_CRC(c_plus=1)/g2_CRC(c_plus=82) in [81, 83]. Else FAIL.

**B3 (rigorous).** Non-bindingness of log c_lcr: shift(x) := (b_n(1,1) + x)/b_n(1,1). PASS iff shift(1e9) <= 1.05. Else FAIL.
**B3n (negative control).** PASS iff shift(1e11) >= 5 (so B3's inequality is not vacuous). Else FAIL.

**C1 (rigorous, exact rational).** lambda·kappa·eps_1²/256 >= theta·a_bad at lambda = 1/2 iff kappa >= kappa_min of A1.
PASS iff the inequality holds with EQUALITY at kappa = kappa_min and STRICTLY at kappa = 1, and fails at
kappa = kappa_min/2 (all as exact rationals, eps_1 cancelling). Else FAIL.

**C2 (rigorous, exact rational).** a_A/a_bad = min{lambda·kappa/(256·c_pr), 6·theta} at lambda = 1/2, kappa = 1,
theta = 1/24; and kappa_crit := 256·6·theta·c_pr/lambda (the kappa above which the 6·theta·a_bad entry binds).
PASS iff a_A/a_bad == Fraction(1,4) exactly AND kappa_crit == Fraction(1,14045). Else FAIL.

**C3 (rigorous).** The 2-branch assembly of PLD §18.7: if b1, b2 <= (C_A/2)·x then prod over |S| cubes of (b1+b2)
<= (C_A·x)^|S|. PASS iff no violation over |S| in 1..20 and (b1,b2) ranging over all pairs from
{0, C_A/4, C_A/2} with C_A = 7 (an arbitrary recorded-free test value) and x = 1/3, exact rationals. Else FAIL.

**D1 (rigorous + informational).** dof := 3·n_int·81 and log c_1 := (dof/2)·ln(1/(1-lambda_f)) at lambda_f = 1/2.
PASS iff dof == 52488 AND log c_1 in [1.8e4, 1.85e4] AND log c_1 <= 1e9 (the side condition PLD §18.8 (ii)(5) states).
Else FAIL. (Informational as physics: it is the Gaussian heuristic's value, not a proven constant.)

**D2 (informational, conditional consequence).** r := 3.17e-3/6.6e-10 and (a_ret/a_bad)/r with a_ret/a_bad = 8.03e-7.
REPORT both; PASS iff r in [4.7e6, 4.9e6] AND (a_ret/a_bad)/r in [1.6e-13, 1.75e-13]. Else FAIL. No claim is attached:
whether REVIEW_PLD_S3's L0-1 governs PLD §16.8's lambda_min is explicitly left to the SF/PROOF owners.

**E1 (rigorous, exact integer).** sum_{r=1..i} L^{k-r} == (L^k - L^{k-i})/(L-1) and < L^k/(L-1) == L^k/2 at L = 3.
PASS iff the identity holds exactly and the strict bound < L^k holds, for all L = 3, k in 1..30, i in 1..k. Else FAIL.
**E1n (negative control).** At L = 2 the bound sum < 2^k/2 must FAIL for some (k,i), showing L >= 3 is load-bearing.
PASS iff a violation is found at L = 2 with i >= 2. Else FAIL.

**F1 (rigorous arithmetic, informational).** The detached-cube union-form shadow sum 1 + 81 + 256·(K-j-2) is linear in
the depth K-j. PASS iff the value for K-j = 2..10 equals 82 + 256·(K-j-2) exactly and is strictly increasing in K-j.
Else FAIL.

**F2 (rigorous, exact rational).** Delta_sh: 81 + 2401·32·80·sum_{m>=1}3^{-m} == 3073361, and the p4 D2b measured
per-cube excess 256 <= Delta_sh. PASS iff both hold exactly. Else FAIL.

**G1 (rigorous arithmetic about recorded numbers).** PLD §18.5 (e): m_star := log(2/eps_1)/(2·log L) at eps_1 = 6.7e-40,
L = 3; and the coherent one-level price exponent 6·L^4·a/g_K^2 at a = 1.0e-86, g_K^2 = 1e-94.
PASS iff m_star in [41, 42] AND 6·81·a/g_K^2 in [4.5e10, 5.0e10] AND 6·81·a/g_K^2 > m_star·ln(324)
(i.e. the price beats the 324-per-level count over the whole admissible chain depth). Else FAIL.

## Overall
SUMMARY line prints "ALL PASS" iff every criterion above passes, else "FAIL: <ids>". A FAIL is reported as a FAIL in
PLD.md §18.10 and in PLD_LOG, with no edit to any criterion and no re-run after seeing a result; any probe added after
seeing output is labelled post-hoc.
