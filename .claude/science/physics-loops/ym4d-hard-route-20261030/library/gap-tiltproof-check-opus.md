lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T11:52Z

# Check of `library/gap-tiltproof-max.md` (FINISH row 979)

Provenance: Claude Opus 5.5, max effort, Mac mini worker 2, branch `claude/ym4d-hard-route` at commit 2601b4afd. One line-by-line reading by one other model than the author (row 977 was written by Claude Fable 5.2). Not an audit. Check item: no extension of the results, no new attack.

## Plan (at most eight steps, one per response, each appended before the next)

1. Read the note's setup, Section 2.0 (ZERO-CEIL), and the ported-lemma statements it cites; check ZERO-CEIL.
2. Check Lemma D1 (Step 4).
3. Check Theorem D2 attack 5.2: reflection structure with two pinned slices, gauge-fixed crossing links, end weights, layer coupling b. State the hypotheses of the ported reflection-positivity lemma as used, and whether each use meets them.
4. Check Theorem D2: the Gaussian-domination step with shifts on sheet bonds only (FSS hypotheses as used), the sum rule 5.4, and the passage 5.5 from one slice to q~, with its hand arithmetic.
5. Check Corollary CAP (6.1).
6. Check Proposition QUOT-CAP (9.1) and the hand arithmetic of 10.1.
7. Verdict table per statement (HOLDS / HOLDS AFTER CORRECTION / FAILS, with the line), and the RESULT line.

## Step 1. Section 2.0, ZERO-CEIL (note lines 54-72)

Sources read: the note in full; `library/gap-avgcurv-max.md` 44-60 (objects, K_a) and 124-200 (FLOW, Lemma Z, Theorem POL-BR, Lemma NEC).

Line by line.
- l.55-56. At phi = 0 the gauge orbit is {0}, so every z is admissible, and Lemma Z gives Var = k0_(s,b_t)|z|^2. So kbar_(s,t) >= k0_(s,b_t). tau_b >= 0 holds: L tau_b = d/db log Z_b(0) is non-decreasing (convexity), it is 0 at b = 0 because E_m x_l = 0 (centre -1 at one end site), and tau_b is the same on every link (translations and axis permutations/reflections of the cube preserve V, hence Omega by uniqueness of the top eigenfunction, and <x^(-1), w^(-1)> = <x, w>). So k0 >= k00. HOLDS.
- l.57. Generic phi has a discrete stabiliser (SU(2) holonomies that do not commute), so the horizontal space has dimension 12|B| - 3|B| = 9|B|; Cov is smooth in phi on the compact M x M; a limit point of horizontal planes at phi -> 0 is a 9|B|-plane on which Var = k0. HOLDS (remark only).
- l.58. POL-BR returns alpha_s^thm := 1/(integral over [0, c] of exp(2 integral over [0, t] of kbar)). With kbar >= k00: alpha_s^thm <= 2 k00/(e^(2 k00 c) - 1). HOLDS.
- l.59-60. k00 = (beta^2/4)(1/lam^2 + 1/(1 - lam)^2); with p = lam(1 - lam): r = (1 - 2p)/p, r + 2 = 1/p, r(r + 2) = (1 - 2p)/p^2 = 1/lam^2 + 1/(1 - lam)^2; 2 k00 c = (beta/2) r (r + 2) p = beta r/2. HOLDS.
- l.61. d/dr log[r(r + 2)/(e^(beta r/2) - 1)] = 1/r + 1/(r + 2) - (beta/2) e^(beta r/2)/(e^(beta r/2) - 1) < 1/2 + 1/4 - beta/2 on r >= 2, <= 0 for beta >= 3/2. HOLDS.
- l.62-63. r = 2 gives 4 beta^2/(e^beta - 1); averaging over s in (0, 1/beta) with the factor 1/2 gives 2 beta/(e^beta - 1). At beta 2.3: e^2.3 - 1 = 8.97418, so 21.16/8.97418 = 2.3579 and 4.6/8.97418 = 0.51258 < K_30. K_30 = (12.51 + 3 log 30)/28 = 0.8112 (C_beta = 12.51 is row 960's value, unchecked there). HOLDS.
- l.64-65 (marked ARGUED). I recomputed the values at lam = 0.10, 0.40, 0.50 (0.00754, 2.1548, 2.3579): they agree. The trapezoid sum is 1.0778, as written. But a trapezoid sum is not a bound. The integrand is increasing in lam on (0, 1/2] (r decreases there, and the bound decreases in r), so the right-endpoint sum with the same nodes IS an upper bound: 2 x 0.05 x 11.9565 = 1.1957, so alpha^thm <= 0.260 (given upper bounds for the nine listed values). CORRECTION: 0.234 is an estimate, not a bound; the bound from these nodes is 0.260, and K_a <= 0.260 needs a >= 104 (K_103 = 0.2615, K_104 = 0.2592).
- l.66-68. K_49 = 0.5146 > 0.5126 > K_50 = 0.5051, so "a >= 50" HOLDS. "a >= 117" (K_116 = 0.2348, K_117 = 0.2330) is right for the number 0.234, which is not a bound (previous item): read "a >= 104 from the monotone sum". The remark on tau_b > 0 is qualitative (tau = 1 is not the true value); it carries no weight.
- l.69-70. "Counterexample to the use, not to the statement": correctly scoped. Q_8, 2T: left times right multiplication of Q_8 on H has commutant R (Q_8 spans H), so Cov_m = Id/4 holds. U(1): k00 doubles, 2 k00 c = beta r, cap 4 beta/(e^(2 beta) - 1) = 9.2/98.484 = 0.0934. HOLDS.
- l.71-72. "it is at least 117": rests on the ARGUED number. PROVED: at least 50; from the monotone sum: at least 104.

**Verdict 2.0 ZERO-CEIL: HOLDS** (the PROVED part: every admissible kbar >= k00_s, and POL-BR returns at most 2 beta/(e^beta - 1) = 0.513 < K_30 on the a = 30 box). The ARGUED refinement at l.65/67/72 HOLDS AFTER CORRECTION: 0.234 is a trapezoid estimate; the bound from the same nodes is 0.260 (a >= 104), not 0.234 (a >= 117).

