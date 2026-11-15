# w6 criteria (lane H session 6; written BEFORE any w6 script)

Informational, never a proof. Three parts: G (exact shadow geometry on Z^4), A (exact decimal arithmetic of the ceilings),
N (the negative control HW §29 promised for check (ii) and never ran).

**Rule-2 compliance (binding, and the session-5 lesson [RHW5-fix W5-1]).** Every constant appearing below is either
(i) structural (a power of L = 3, of 2d, or of a neighbourhood radius: 81 = 3^4, 16 = 2^4, 625 = 5^4, 2401 = 7^4, 6561 = 9^4),
or (ii) recorded BEFORE session 6: c_att(rho) = 1 + 153664*rho and 6561 (HW l.1501, session 5); 38416, 38417 (HIST H-geo (iv));
531441 = 6561*81, b_n/b_D's session-5 forms, 4.898e-97, 9.991e96 (HW §30.6 / REVIEW_HW_S5 S5-12); 258 and 193 (the maximum
excess per Y-cube recorded in REVIEW_HW_S5 S5-14/S5-24); 1e-94 ((RLF-delta)), 2.7e-91 (n_H ceiling), 2.5e-152/C_Omega (DX',
REVIEW_SF_S7 l.335); 82 (PLD §18.4's ring price, another lane's file, landed before this session); a = 1.0e-86, beta_- = 0.186,
L = 3, a_ret = 2.0e-91 (RLARGE l.612, PLD §16.8). **No constant derived in session 6 appears in this file**: in particular the
session-6 values of b_n, b_D, c_att', the multiplicative constant of the sharpened attachment lemma, the sharpened per-level
shadow constants and the session-6 ring price are NOT written here, and no PASS band is drawn around any of them.
**Each criterion is labelled PRE-REGISTERED (its outcome is not known as this file is written) or CONFIRMATORY (it re-computes
a quantity derived earlier in the session; it tests reproduction, not truth).** An OVERALL line reports the conjunction and
must name A3's and G3's substantive content rather than hiding it behind the word PASS.

Definitions (HIST §7.1): pi(X) = coordinatewise floor division by L = 3; N_t(X) = l-infinity radius-t neighbourhood;
Sigma(X) := N_1(pi(X)); sh_{j+r}(X) := Sigma^r(X); ||X||_sh^{(M)} := |X| + sum_{r=1..M} |sh_{j+r}(X)|.
Samplers (seeded, exact integer arithmetic, pure Python, no numpy, no BLAS, single thread, no numeric lock needed):
- S-rand: P a random *-connected set of 1-6 level-j cubes at a random base point; Y attached one cube at a time, each at
  l-infinity distance in [1, rho] from a random earlier cube of P u Y, |Y| in 1..8; rho = 8; at least 200 samples.
- S-adv (positions, not directions): the same shapes but with the base point placed on the ALL-ONES base-3 orbit, i.e. every
  coordinate equal to (3^(M+1) - 1)/2, so that pi maps the cube to the centre of its parent block at every level.
- Depths M in {5, 10, 20, 30} for S-rand; M in {2,...,30} for the deterministic family of G3.

## G. Exact shadow geometry

- **G1 (PRE-REGISTERED; the shadow radius).** For every sampled X (S-rand and S-adv, P u Y) and every 1 <= r <= M, test
  the three containments Sigma^r(X) subset N_t(pi^r(X)) for t = 1, 2, 3. PASS iff: t = 3 has 0 violations (HIST H-geo (i),
  confirmatory of a prior lemma); **t = 2 has 0 violations**; and **t = 1 has at least one violation** (which would show that
  radius 2 is the smallest radius with this property, i.e. that H-geo (i) is improvable but not below 2). Any other pattern
  is a FAIL and is to be reported as one.
- **G2 (PRE-REGISTERED; translate coverings).** For every sampled set A: test the three set identities
  N_2(A) = union over t in {-1,1}^4 of (N_1(A) + t); N_3(A) = union over t in {-2,0,2}^4 of (N_1(A) + t);
  N_4(A) = union over t in {-3,0,3}^4 of (N_1(A) + t). PASS iff all three hold with exact set equality on every sample AND
  the corresponding 2-translates-per-coordinate statement for N_3 fails on some sample (so that 3^4 translates is minimal
  for radius 3 and 2^4 for radius 2).
- **G3 (PRE-REGISTERED; THE DECISIVE TEST: is the multiplicative factor of Lemma SH-att removable?).** Deterministic family:
  P = {z}, Y = {z + 8*e_1} with z = (zeta, zeta, zeta, zeta), zeta = (3^(M+1) - 1)/2 (all base-3 digits 1); |Y| = 1 and Y is
  rho-attached to P at rho = 8. Let E(M) := ||P u Y||_sh^{(M)} - ||P||_sh^{(M)}. Verdicts, pre-registered:
  - the additive form ||P u Y||_sh <= ||P||_sh + c(rho)*|Y| with c independent of the number of levels is **REFUTED** iff
    E(M+1) - E(M) >= 1 for every M in 2..29 and E(30) > 258 (the largest per-Y-cube excess any prior run recorded);
  - it is **SUPPORTED** iff E(M) is constant for all M >= some M_0 <= 30 (which is what REVIEW_HW_S5 S5-14/S5-24 observed
    at random positions and conjectured to be general);
  - any other behaviour is reported verbatim as neither.
  Also report E(M)/M and ||P u Y||_sh/||P||_sh at M = 30, and the same two quantities for S-adv samples with |Y| > 1.
- **G4 (CONFIRMATORY; the sharpened attachment inequality).** For every sample of S-rand and S-adv, at every depth M, test
  ||P u Y||_sh <= 81*||P||_sh + c_att(8)*|Y| with the SESSION-5 constant c_att(8) = 1 + 153664*8, i.e. the session-5 lemma
  with its multiplicative factor 6561 replaced by the structural 81 = 3^4 and its additive constant left as recorded.
  PASS iff 0 violations. (This is a reproduction check of a statement proven earlier in the session, not a pre-registration.)
  Report also the session-5 inequality (factor 6561) for comparison: 0 violations expected.
- **G5 (informational, no verdict).** Report max over samples of (||P u Y||_sh - c_att(8)*|Y|)/||P||_sh, i.e. the smallest
  multiplicative factor the samples force, so that the looseness of the factor used in G4 is on the record.
- **G6 (PRE-REGISTERED; the price of one extra R-free ring, PLD §18.4).** For every sampled X and every 1 <= r <= M, test
  |sh_{j+r}(N_1(X))| <= 16*|sh_{j+r}(X)| (16 = 2^4) and |N_1(X)| <= 81*|X|. PASS iff 0 violations of both. Report
  max_r |sh_{j+r}(N_1(X))| / |sh_{j+r}(X)| over all samples and r >= 1, and the resulting ratio
  (sum_{r>=1} |sh_{j+r}(N_1(X))|) / (sum_{r>=1} |sh_{j+r}(X)|), to be compared with PLD §18.4's quoted ring price 82.
  (Outcome unknown as this file is written: PLD §18.4 proves 81 per level and this criterion asks whether 2^4 suffices.)

## A. Arithmetic of the ceilings (plain-Python Decimal, 120 digits; no mpmath, no BLAS, no lock)
Recorded inputs: a = 1.0e-86, beta_- = 0.186, L = 3, a_ret = 2.0e-91; node-A constants scanned symbolically,
c_A in {0, 1, 100}, C_l = C_A in {1, 1e6}, R in {0, 10}, c_U = 1; rho = 8.
- **A1 (CONFIRMATORY).** Recompute, from the session-6 formulas for b_n and b_D (whose values are NOT written in this file),
  g2_CRC := a/(b_n + a*R + log(12800*C_l)) and n_T := b_D/(a*beta_-*log L), with and without PLD §18.4's ring, and print
  them. PASS iff the printed values agree with the hand values stated in HW §35 to within 1% (a reproduction test).
- **A2 (PRE-REGISTERED).** REVIEW_HW_S5 S5-12 found that at the session-5 constants the four quantities (S2)'s ceiling,
  REL-boot's r <= 1/2 ceiling at B_* = c_f + 1, HIST-sum's own condition at B_0 = c_f + 2, and (T) vs n_H(a, B_0) all
  coincide to 4-5 significant figures. Test whether that coincidence still holds at the session-6 constants, in two variants:
  (a) with HIST's recorded 38417/38416; (b) with the per-level shadow constants re-derived in session 6 (values not written
  here). PASS iff the outcome is reported for both variants with the agreeing/disagreeing pairs named; there is no
  pre-registered direction, because the answer is not known as this file is written.
- **A3 (PRE-REGISTERED; the substantive question).** Does g2_CRC exceed the recorded (RLF-delta) ceiling 1e-94? Report the
  answer, as a factor, in four scenarios: session-5 constants without the ring; session-5 constants with the ring;
  session-6 constants without the ring; session-6 constants with the ring. PASS iff all four factors are reported with their
  direction stated in words; the OVERALL line must say which scenarios breach 1e-94 and which do not.
- **A4 (CONFIRMATORY).** Recompute, from session 5's own recorded formulas, g2_CRC*c_+ and n_T/c_+ at the session-5
  constants. PASS iff they reproduce 4.898e-97 and 9.991e96 to 3 significant figures (REVIEW_HW_S5 S5-12).
- **A5 (PRE-REGISTERED).** Compute the largest c_+ for which g2_CRC(session 6, with ring) >= 2.5e-152/C_Omega at C_Omega = 1
  (DX', the binding programme ceiling), and the factor by which g2_CRC exceeds it at c_+ = 1. No band: report the number.
- **A6 (CONFIRMATORY).** Report c_f, B_* = c_f + 1 and the (S1) ceiling at the session-6 constants with and without the ring,
  against session 5's c_f = 531441*c_+.

## N. The negative control HW §29 promised for check (ii) and never ran
REVIEW_HW_S5 S5-25 (scope defect 1, binding): §29 l.1462-1464 pre-registered "(ii) ... with a negative control (activities
above the stated threshold, where the bound must fail or the expansion must diverge)", and no grid point of w5 Part C had
2*z^2 >= 1 (its maximum was 0.783). This part runs it, in the SAME toy, in exact Fraction arithmetic (no numpy, no floats).
Model, verbatim from w5_criteria.md Part C: level 0 a ring of 12 sites with i.i.d. Bernoulli(p) defects; level 1 a ring of 4
blocks; xi_X in {low, mid, high} with probabilities (q, q'-q, 1-q'); D1(X) = [xi_X = low] or [xi_X = mid and block X has a
level-0 defect]; R both levels constrained, B = {level-0 site 0}; z := q + (1 - (1-p)^3)*(q' - q); bound rho <= 1/(1 - 2*z^2).
Grid: at least three points with 2*z^2 >= 1 and at least one with 2*z^2 just below 1.
- **N1 (PRE-REGISTERED).** PASS iff at every grid point with 2*z^2 >= 1 the bound 1/(1 - 2*z^2) is vacuous (non-positive or
  undefined) while the exact ratio Z(R^{-B})/Z(R) computed by enumeration is finite, i.e. the pre-registered "the bound must
  fail or the expansion must diverge" is realised as the DIVERGENCE of the bound and not as a failure of the exact ratio.
  FAIL iff some point with 2*z^2 >= 1 has a finite positive bound that the exact ratio satisfies (which would show the
  threshold 2*z^2 < 1 is not where the bound's validity ends, i.e. that the stated threshold is not the real boundary).
- **N2 (PRE-REGISTERED).** Report the exact ratio at the near-threshold point and whether it stays bounded as 2*z^2 -> 1^-.
  PASS iff the ratio is reported together with the bound at the same point; no direction pre-registered.

Resource limits: exact integer / Fraction / Decimal arithmetic in plain Python, single thread, no BLAS, under 20 min and
under 1 GB in total; by the brief's rule 6 no numeric lock is needed or taken for exact arithmetic.
