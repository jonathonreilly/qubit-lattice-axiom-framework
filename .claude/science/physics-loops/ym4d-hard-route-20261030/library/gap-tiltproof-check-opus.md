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

Numerics: the machine's numeric lock was held by row 976 (`gap-escape-976`, until 2026-11-15T03:31Z) when I tried at 23:58Z. So every number in this check is hand arithmetic (a few closed-form evaluations, each shown); no lattice sum was run.

## Step 2. Lemma D1 (note lines 175-200)

Line by line.
- l.181 (i). The tangent space of the orbit at phi is {X.phi}, (X.phi)_l = X_u phi_l - phi_l X_v for l = (u, v). phi^Lam_l = 0 on direction-1 links, so every tangent vector vanishes there. Any z supported on direction-1 links is orthogonal to the orbit. HOLDS.
- l.182 (ii). m is gauge invariant (V is, Haar is, and Omega is the unique top eigenfunction of a gauge-covariant T_0); <g x h^(-1), g w h^(-1)> = <x, w>; a transverse link has both ends in one plane x_1 = k, and <1, g x g^(-1)> = (1/2) tr x. So J_(b,phi^Lam) is invariant under plane-wise g(k). g(k) = -1 sends x_l to -x_l on the direction-1 links k-1 -> k and k -> k+1 and fixes every transverse link. So E q~_k(y) = 0. HOLDS.
- l.183 (iii), proof l.190-191. k' not in {k-1, k}: g(k) = -1 flips q~_k and q~_(k-1) only. k' = k-1: g(k+1) = -1 flips q~_(k+1), q~_k and not q~_(k-1) (needs k-1 != k+1, so S >= 3). k' = k+1: g(k) = -1 (needs k+1 != k-1). Same plane: M(y, y') := E[q~_k(y) (x) q~_k(y')] satisfies M = R M R^T for R(q) = g q h^(-1), g = g(k), h = g(k+1) independent; these R fill SO(4), whose commutant on R^4 is R, so M = (1/4) tr M Id_4 (M need not be symmetric; the commutant argument does not need it). For Q_8 and 2T the same holds: Q_8 spans H, so the commutant of left and right multiplication is R. HOLDS.
- l.184 (iv). E<z, q~> = 0 by (ii); Var = sum a(y) a(y') e^T M(y, y') e = (1/4) sum a a' G(y, y'); |z| = 1. HOLDS.
- l.185-187 (v), proof l.192-194. With Haar product reference, J_(b,phi^Lam) = F (nu_Lam (x) Haar_dir1)/norm, where F = m-density(x) m-density(w) e^(b<x,w>) is continuous and positive on the compact M x M, and nu_Lam is the normalised product of e^((Lam/s)<1,x_l>) e^((Lam/s')<1,w_l>) over transverse links. nu_Lam -> point mass at 1 weakly, so the integral of g F against nu_Lam (x) Haar converges for every continuous g, and the normaliser tends to a positive limit. <z, q~> is bounded and continuous, so Var converges. For each Lam, z on direction-1 links is admissible by (i), so kbar_(s,t) >= Var_Lam for all Lam, hence >= the hard-pinned value. HOLDS.
- l.195-197 (remark, generic points). Stabiliser of phi^Lam = plane-wise constant g(k) (each plane is connected by transverse links). A gauge-invariant function has a stabiliser-fixed gradient there, and v -> g v h^(-1) fixes no non-zero v, so the gradient vanishes on direction-1 links. Approach along phi^Lam + eps eta, eta generic: the limit of the orbit tangent spaces is spanned by g.phi^Lam (zero on direction-1 links) and h.eta (h the stabiliser algebra); <z_p, X.eta> = <e, X(k) E_p - E_p X(k+1)> (2/A)^(1/2) with E_p := sum over y of cos(p y) eta_k(y), which is 0 under the stated condition. So z_p lies in the limit horizontal space, and continuity of Cov gives the bound. HOLDS (one line in the note; the step is as I wrote it here). Not needed for (TILT-COV-sup) as stated, which already admits phi^Lam.
- l.199. G(y, y) = E|q~|^2 = 1/s^2 + 1/s'^2 + 2 tau/(s s'), tau := E<P_k(y), P'_k(y)> in the tilted law (depends on Lam and b; it is not the tau_b of Lemma Z unless Lam = 0). HOLDS with that reading.

**Verdict Lemma D1: HOLDS** (all five clauses, for S >= 3; the note asks S >= 4 even). The proof is complete as written; the only unwritten step is the weak-convergence detail of (v), supplied above.

