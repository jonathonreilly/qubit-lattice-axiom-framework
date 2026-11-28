# Check of library/gap-solve9-astra62.md (FINISH row 1162)

Checker: Claude Opus 5.5, max effort, laptop subagent. Cross-provider check of
row 1161. Started 2026-11-19.

Note on the save protocol: the first tool call created this file with a header
only; the plan below was added by the second write, before any check work.

## Plan (eight steps)

1. Read the file under check in full (in ranges), the brief
   `library/gap-council-brief.md`, and the cited parts of rows 1153-1157
   (`library/gap-solve6-astra62.md`, `gap-solve7-astra62.md`,
   `gap-solve8-astra62.md`) and their checks.
2. Check the Pfaffian seed from one neutral trace and the two flux alternatives.
3. Check the selection criteria (13) giving (W).
4. Check the local criteria (26).
5. Check the unconditional level count (19).
6. Check everything else, statement by statement.
7. Numeric guide run, if useful (guide only; under 2 GB).
8. Verdict table and RESULT line.

## Step results

### Step 1. Reading record

- File under check: `library/gap-solve9-astra62.md`, lines 1-423, read in full in
  three ranges. The note pins checkout `263ef6074`; the file's last commit here is
  `34fd3b405`.
- Brief: `library/gap-council-brief.md`, read in full.
- Inputs, read in the cited parts:
  - Row 1157, `library/gap-solve8-astra62.md`, all 551 lines. Its check
    `library/gap-solve8-check-opus.md` (row 1160): 59 statements, all HOLD.
  - Row 1155, `library/gap-solve7-astra62.md`, L226-277 ((16)-(18)) and the
    section list; its check (`gap-solve7-check-opus.md`) ends HOLDS.
  - Row 1153, `library/gap-solve6-astra62.md`, L205-244, including (13); its
    check ends HOLDS.
  - Row 1158, `library/gap-paths-fable.md`, L205-314 (Lemmas F, J, T, T1,
    (TUN)). Its RESULT says it is checked by no one.
  - `library/gap-flux-exercise.md`, L107-170 (twists, sectors, (S1)-(S3), the
    kappa set) and L495-521 (Lemma W, Theorem S-w, Corollary EV).
  - `library/gap-seed-shape.md`, L43-144 (Lemma E2, Proposition B3, Theorem SH,
    thresholds 1/1650 etc.).
  - `library/gap-phys-seed.md`, L55-99, L249-284 (Lemma Z, Proposition Delta use,
    Corollary Z1) and Theorem ZD-c (L311-320).
  - `library/gap-channel-astra.md`, section 1.2 (L166-248, equations (5), (6),
    (6a)), and its check `gap-channel-check-opus.md` L36-48.
  - Row 1143, `library/gap-solve-astra62.md`, L17-46 and L82-109 ((1), (4)-(6)).
  - Row 1145, `library/gap-solve2-astra62.md`, L15-51 ((1)-(4)).
  - Row 1147, `library/gap-solve3-astra62.md`, L351-375 (section 11, (29)).
  - `library/gap-means-max.md`: Theorem R, (M5), Corollary R6, by search.
  - PR 10114 note at `f76f6c649c`, L106-169, by `git show`: the bound
    exp(-68 beta) is there (b = 4, p_B = 13).

Notation used below. U = F/||F|| on the periodic cube; x = (lambda/lambda_0)^n;
X_{m,q}(v) = Tr_q (F_m/lambda_0)^v; s(v) = X_{0,0}(v) - 1; (m, q) = (magnetic,
electric). S_per, S_full, S_kappa are the three sector sums of Theorem S-w; the
seed of Theorem S-w is S_w(N; (2N)^3) < 1/5041 (shape two, N = n/2).

### Step 2. The Pfaffian seed from one neutral trace, and the two flux alternatives

Checked first and line by line. Every inequality below was re-derived by hand.

**S1. Even multiplicity for Mq != 0 (L46). HOLDS.** Over F_2, Mq is the cross
product m x q, so ker M = {0, m} for m != 0 and six of eight q have Mq != 0.
By (6a) of the channel note (checked, HOLDS), S_i^{n_i} = prod_j C_j^{m_ij}, so
on sector q, D_i^{n_i} = (-1)^{(Mq)_i} = -I when (Mq)_i = 1. D_i is a composition
operator (translation and centre link flip), real and orthogonal, and it commutes
with F_m and with every C_j on gauge-invariant states. On a finite real
eigenspace E, det(D_i|E)^{n_i} = (-1)^{dim E}; with n_i even the left side is
nonnegative, so dim E is even.

**S2. (3) (L48-53). HOLDS.** X_{m,q} <= X_{m,0} is (S1) of the flux exercise by
Fourier inversion of nonnegative twisted integrals. X_{m,0} <= X_{0,0} is row
1157 (19) (H_m <= H_0, with H_m = 8 lambda_0^u X_{m,0}(u)); it needs u >= 3 for
the rotated frames. b_{m,q}^u <= 1 + s(u) for all u >= 3 and s(u) -> 0 give
b_{m,q} <= 1.

**S3. (4) (L55-63). HOLDS.** If the top level of a sector has multiplicity at
least two, 2 x_1^u <= X(u) <= 1 + s_0, so x_1^u <= d. The second level obeys
2 x_2^u <= 1 + s_0 in every sector. Spending v - u steps gives both lines. The
count 42 = 7 x 6 is right.

**S4. (5) (L67-79). HOLDS.** The basis change e_i -> e_i + e_j fixes the static
matrix of frame i and adds its j-row to the temporal star (checked from
B'(e_k, e_l)). The signs that change are those with (Mq)_j = 1: zero or four of
eight. Each such X_{M,q}(v_i) <= h by (4), since v_i/u_i >= K; the denominator
is at least one; so one addition moves f_Q by at most 8h. Normal form: a swap is
three additions; two swaps put a one at (1,2); e_k + B_{2k} e_1 + B_{1k} e_2
(k = 3, 4) clears the pairings in at most four more additions; total at most
ten per form, 20 x 8h = 160h. (Guide: a breadth-first search over all 64 forms
in Step 7 finds the largest distance to the normal form of the same rank.)

**S5. The two alternatives (L85-99). HOLDS.** Re-derived: 1 <= I_v(0) <= 16;
|I_v(B) - I_v(B')| <= 16 x 160h < eta for equal rank two; the mean of the seven
purely temporal I_v is 1 + s(v) - c_v; s(t) <= h; |Y_t - y| <= eta,
Y_{2t} >= 1 - c_t - eta >= y - 2 eta, Y_{2t} <= Y_t^2; hence
y(1 - y) <= 2 eta + 2y eta + eta^2 <= 5 eta (y <= 1 + h). Second alternative
(y <= 1/2, y <= 10 eta): rank-two I_t <= 11 eta; rank four has m != 0 and
I_t(m,e) <= I_t(m,0); I_t(0) = 8(1 + s(t)) - 7y >= 8 - 70 eta; X_{0,q}(t) >=
(8 - 147 eta)/8 >= 1 - 19 eta; top weight >= 1 - 20 eta after the tail h.
First alternative (1 - y <= 10 eta): c_t <= 11 eta; s(t) + 7 c_t <= 78 eta;
a_m^t >= (1 - 12 eta)/(1 + 2 eta) >= 1 - 14 eta; Y_t - a_m^t <= 16 eta;
I_t(m,e) >= 2 a_m^t - Y_t >= 1 - 30 eta (simple positive magnetic vacuum is
even); (1 - 30 eta)/(1 + 78 eta) >= 1 - 108 eta.

**S6. (7) (L101-105). HOLDS.** S_kappa = s + sum_{m != 0} X_{m,m}: the kappa
weight w(k) = (1/8)(-1)^{Pf(k)} has Pf = m.e in the frame with time 4, so its
sector set is chi = m (flux exercise C5). First alternative: each X_{m,m} <= 16
eta; second: <= 11 eta; plus s(t) <= h. So S_kappa(t) <= 113 eta. The use of
Theorem S-w (seed S_kappa(N;(2N)^3) < 1/5041 with N = t) and Corollary EV for
the centre-blind algebra is as stated in the flux exercise L507-517.

**S7. Transverse requirement (L107). HOLDS.** A slice perpendicular to a spatial
axis carries three twist bits; 56 of 64 twists restrict to nonzero bits. In the
second alternative each has probability at most f(B) <= 11 eta, so the total is
at most 616 eta. The first alternative gives the periodic shape-two seed
78 eta < 1/1650, hence (PHYS-SEED) and (W) by Theorem ZD-c (row 720).

**S8. (8)-(10) and "one periodic cube suffices" (L113-144). HOLDS.** This is
the central positive claim. Checks:
- Limits: b_{m,q}^{n_k} -> a_{m,q} on a subsequence; (4) with v_k/u_k -> infinity
  gives X_{m,q}(v_k) -> a_{m,q}^r; Mq != 0 gives a_{m,q} = 0.
- Positivity: H_{i,c,q}(r) is the limit of a frame-i sector trace on the torus
  (n,n,n,v_k) divided by the positive lambda_k^{v_k}; so H >= 0 for all r > 0.
  This uses only (TM-tw) on rectangles (sides >= 3), no neutral bound.
- At r = 1 the torus is n^4 and every frame has the same cube n^3 and the same
  lambda_k, so (4) gives H_{i,c,q}(1) = 0 for M_i q != 0. H is a finite sum of
  exponentials, so H'(1) = 0 at this interior minimum.
- Under e_i -> e_i + e_j only coefficients with M_i q != 0 change sign, so
  I(1, .) and d_r I(1, .) are constant on each rank.
- Seven purely temporal twists have rank two: a_{0,q} = b for q != 0 and
  I(r,(0,e)) = 1 - b^r. A purely spatial m has I(r,(m,0)) = A_m^r + C_m^r with
  A_m >= C_m (positive magnetic vacuum, or (3) in the limit).
- (10): A + C = 1 - b and A log A + C log C = -b log b. Left terms <= 0, right
  side >= 0, so b, A, C are in {0, 1}; b = 0 gives I, b = 1 gives II; Fourier
  inversion gives the table (9). Only top levels survive by (4).
- S_kappa(rn) -> 0 on the whole sequence: s -> 0 and a_{m,m} = 0 in both cases.

**S9. One finite aspect (L146). HOLDS.** The contradiction argument is valid:
counterexamples with K -> infinity have n_K >= 3K -> infinity and satisfy (8);
a further subsequence with a fixed offending index and v/n -> r in J contradicts
(9). It is an existence statement for K; no K value is claimed here.

**S10. Consumer (L148). HOLDS.** S_kappa(n/2) <= epsilon + 7 epsilon = 8 epsilon
< 1/5041. In II every B != 0 has weight <= epsilon over a denominator >= 1, so
the 56 nonzero transverse twists carry <= 56 epsilon < 1/10. In I the periodic
excited sum is <= 8 epsilon, the periodic seed.

**S11. Necessity over physical sizes (L150). HOLDS.** B3 with p = q = 1, a = b/2,
B = b^3, H = n^3 gives multiplier (n/b)^3 x 8 = (2n/b)^3; time monotonicity
needs floor(n/K) >= b/2 = n/2^{d+1}, true for 2^d >= K. The transverse limit 7/8
follows from row 1157 (24). For the Pfaffian converse, B3 is applied to W_kappa;
B3 rests on Lemma E2, which uses only Lemma A (a), Lemmas K, X and the transfer
in each frame; Theorem S-w and Lemma W supply these for W_w. s <= S_kappa holds
term by term.

**S12. Explicit aspect K = 512, n >= 2^70 (L215-227). HOLDS.** Every constant was
recomputed:
- Second derivative: z^2 e^{-zs} <= z^2 e^{-z/4} e^{-zu/n} for s >= 1/2,
  u/n <= 1/512; sup z^2 e^{-z/4} = 64 e^{-2} <= 64; sum x^{u/n} = X(u) <= 3/2;
  so 96 per sector trace and 768 for I and for every H.
- h = (3/2)(3/4)^{511} < 2^{-169}, using (3/4)^3 < 1/2.
- r = ceil(n 2^{-70})/n lies in [2^{-70}, 2^{-69}] for n >= 2^70; 1 +- r are
  integer periods; H(1 +- r) >= 0 by frame-i positivity; Taylor gives
  |H'(1)| <= h/r + 384 r <= 2^{-99} + 3 x 2^{-62} < 2^{-59}.
- Twenty additions: values within 160h; derivatives within 160 x 2^{-59} < 2^{-51}.
- -x log x <= sqrt x and (4) at n/2 give U_N <= (3/2)(3/4)^{255} < 2^{-84}.
  The mean of the seven temporal derivatives is -U_N + U_C; the magnetic one is
  -U_M; so U_C + U_M < 2^{-51} + 2^{-84} < 2^{-50}; one level has -x log x
  <= 7 U_C < 2^{-47}; x(1 - x) <= -x log x gives x <= 2^{-46} or >= 1 - 2^{-46}.
- Charged top weights differ by <= 120h + 2h <= 162h (the note's 160h for the
  traces is a valid upper bound; the count here gives 120h), so they lie on one
  side.
- Small side: S_per(n/2) < 7 x 2^{-23} + 8 x 2^{-84} < 2^{-19}. The magnetic
  trace at s = 1 lies within 2^{-46} + 161h of one; exactly one of the two
  aligned top weights is large, and it is the vacuum in (m,0); so
  S_kappa(n/2) < 2^{-19}.
- Large side: magnetic traces <= 2^{-46} + 161h < 2^{-45}; X_{m,0}(n/2) <=
  2^{-22.5} + 2^{-84}; S_kappa <= S_full < 2^{-18}; each B != 0 has weight
  < 2^{-18}; 56 x 2^{-18} ~ 2.1 x 10^{-4} < 1/1000.

Step 2 verdict: all positive statements S1-S12 HOLD. No correction is needed.
The RESULT line's phrase "neutral trace at most 3/2 by time floor(n/512)" omits
the range 4 | n, n >= 2^70 stated at L215; on the cutoff trajectory n -> infinity
this is harmless.

### Step 3. Selection of the periodic branch: (13) giving (W), and the one-period test

**S13. (13) is sufficient (L171-183). HOLDS.** Fix a large j and suppose the
one-cube neutral input holds there. Choose epsilon < 1/(8 x 5041), so
q_* = 5041 x 8 epsilon < 1. If alternative II holds at this j, then
S_full(n/2; n^3) = s + sum_{m != 0} X_{m,0} <= 8 epsilon, a shape-two seed for
W_full with N = n/2. Theorem S-w gives, for D = 2^{k+1} N = 2^k n <= b < 2D,
S_full(D/2; b^3) <= q_*^{2^k}/71. Rotating the elementary twist to a static m
(hypercubic symmetry of b^4), the denominator Z_0/lambda_0^b >= 1 and (3) give
zeta(b) <= 8 X_{m,0}(b; b^3); time monotonicity and b >= D/2 give
X_{m,0}(b; b^3) <= S_full(D/2; b^3); and 2^k > b/(2n) gives (14). Hence
liminf -log zeta(b)/b >= log(1/q_*)/(2n) > 0, so (13) fails at this j. So (13)
at every large j forces I at every large j, and I gives the periodic seed
<= 8 epsilon < 1/5041 with a bound independent of j. This is (PHYS-SEED), hence
(W) by Theorem ZD-c. The sizes b in (13) are lattice sizes at the fixed bare
coupling, as the note says.

**S14. (13) is necessary under (W) (L183). HOLDS.** (W) gives (PHYS-SEED), so
for all large j a periodic seed holds at n_j = l/a_j. At that fixed beta_j,
Theorem S gives S_per(D/2; b^3) -> 0, and S_per(b; b^3) <= S_per(D/2; b^3).
In the temporal frame the vacuum is even, so 1 - zeta(b) =
2 sum_{q.e=1} X_{0,q}(b)/sum_q X_{0,q}(b) <= 2 S_per(b; b^3) -> 0. So the
liminf in (13) is zero. The stated equivalence "(W) iff one-cube neutral test at
one size and (13) at all large j" follows from S11, S13 and this.

**S15. Version with the variables of row 720 (L185-190). HOLDS.** Proposition
Delta (the count behind Lemma Z) gives g(T_0; n^3) <= (n/T_0)^3 D(T_0) for the
ordinary trace; with T_0 = n/(2K) this is log Tr U^{n/(2K)} <= (2K)^3
D_j(n/(2K)). Keeping only excited neutral levels and evolving n/(2K) more steps
gives the displayed bound on s_j(n/K). With D^+(L/(2K)) <= D_0 (needs
L/(2K) >= L_0) and z_+^-(L) > 2K[(2K)^3 (D_0 + 1) + log 2 + 1], the exponent's
limsup is below -(2K)^3 - log 2 - 1, so s_j(n/K) < 1/2 eventually. With K a power
of two at least 512, u = n/K <= n/512 meets the explicit test.

**S16. One-period test (11)-(12) (L154-165). HOLDS.** In the temporal-twist
mixture on n^3 x u, summing the seam gives one K_{u/2} and one orbit-averaged
k_{u/2}; orbit averaging makes the orbit pair density q_{u/2}^2/D relative to
pi x pi, with D = X_{0,0}(u) = Tr(P_+ P^u). Its rectangle affinity is
Tr(P_+ P^{2u})/D^2 = X_{0,0}(2u)/D^2 <= 1/D (largest normalized level is one).
Fourier inversion: sum_e Z_e = 8 lambda^u D and Z_0 = lambda^u Z, so
Z = 8 theta_0 D. Then s(u) <= (1/2 + delta)^{-1} - 1 < 1 and
Z <= 8 (A_+ - delta)/A_+ <= 8(1 - delta). With epsilon < delta/2 and s_0 equal
to that bound, alternative II would give 8 - epsilon <= Tr U^{n/2} <= Tr U^u = Z
<= 8 - 8 delta, a contradiction (u = 2 floor(n/(2K)) <= n/K <= n/2). The
alpha-variant is the same argument.

**S17. Raw collar version and converse (L167). HOLDS, given the checked rows
1155 and 1157.** The upper comparison A_obs <= 1/D + o(1) and theta-hat_0 =
theta_0 + o(1) are row 1157 (10) and its proof with T replaced by the period u;
the recovery collars need radius r with C n^4 e^{-c beta r} -> 0, which fits in
collars of width of order u/4 = n/(4K) at fixed K. The converse uses the lower
bound of row 1157 (10) with 2d >= u/2 and the shape enlargement of S11; theta_0 =
Z/(8D) -> 1/8. P(m = 0) >= 1/8 in the all-twist law is H_0 >= H_m (row 1157
(19)).

Step 3 verdict: S13-S17 HOLD. No correction.

### Step 4. The local criteria (26)

**S18. Inequality (26) (L379-387). HOLDS.** Hypotheses: K = 512, n = Kb, b even,
b/2 >= 3. Proposition B3 (checked) with p = q = 1, a = b/2, B = b^3, H = n^3:
qa = b/2 < b; |H|/|B| = K^3 and Pi = (b/(b - b/2))^3 = 8, so the multiplier is
8K^3 = (2K)^3 on g = log Tr U^{b/2}. By (3) at time b/2 >= 3, the full periodic
trace on b^3 is sum_q X_{0,q}(b/2) <= 8 X_{0,0}(b/2) = 8(1 + s(b/2; b)). Hence
Tr U_n^{b/2} <= [8(1 + s(b/2; b))]^{(2K)^3}. Then
s(b; n) = sum x_i^{b/2} x_i^{b/2} <= e^{-(b/2) m_+(n)} Tr U_n^{b/2}, and
(b/2) m_+ = n m_+/(2K). Finally e^{-n m_+/2} is one term of s(n/2; n), so
e^{-n m_+/(2K)} <= s(n/2; n)^{1/K}. Both inequalities hold at every coupling.
No free-energy subtraction or neutral-only shape comparison is used, as stated.

**S19. Equivalence over physical sizes (L389-400). HOLDS.**
- (i) or (ii) implies the seed: with S^+_ev(L/K) <= C_0, the cutoff limsup of
  the right side of (26) is at most [8(1 + C_0)]^{(2K)^3} times
  exp(-z_+^-(L)/(2K)), or times S^+_ev(L)^{1/K}. Choosing L with z_+^-(L) large,
  or S^+_ev(L) < (2[8(1+C_0)]^{(2K)^3})^{-K} (possible since the lower limit is
  zero), makes s_j(n/512; n) < 1/2 eventually. The explicit test (S12) then
  gives S_kappa(n/2) < 2^{-18} < 1/5041 for all large j: a cutoff-uniform
  Pfaffian seed with strict margin. The integrality needs (b even, 4 | n,
  n >= 2^70) hold after dyadic enlargement and for large j.
- Seed implies (iii) and (i): Theorem S-w gives S_kappa(L/2; L^3) <= q^{2^k}/71
  at L = 2^{k+1} N, uniformly in j for a uniform q < 1, and s <= S_kappa; the gap
  bound m >= log(1/q)/N gives n m_+ >= 2^{k+1} log(1/q), linear in L.
- (iii) implies (ii) directly.
The note correctly limits this to the finite-volume seed and states that (13)
must be added for the periodic wall.

Step 4 verdict: S18-S19 HOLD. No correction.

### Step 5. The unconditional level count (19), with (17), (18), (20)

**S20. Gram bound (L237-246). HOLDS.** A stride-four grid gives M >= c n^3
12-plaquettes at mutual distance >= 3; one chosen spatial link per plaquette on
one slice; no plaquette (spatial or temporal) holds two chosen links. Given the
rest, each chosen quaternion has density proportional to exp(k.v), |k| <= 6beta
(six plaquettes, twisted signs included), independently. With t = v.k-hat,
Var(a.v) = alpha^2 Var(t) + |a_perp|^2 E(1 - t^2)/3 (zero cross covariance).
For |k| >= 8 the density of x = |k|(1 - t) is proportional to
e^{-x} sqrt(x(2 - x/|k|)) (checked), with normalizer <= int e^{-x} sqrt(2x) and
mass bounded below on [1,2] and [3,4]; so Var(t) >= c/|k|^2 and
E(1 - t^2) >= c/|k|. Total variance, then the long-cylinder limit (trace-norm
convergence to the vacuum projector), give the bound for pi.

**S21. (18) (L248-261). HOLDS.** F = DCD with D a bounded invertible
multiplication and C = tensor of electric convolutions; Dpsi = h >= 0,
D^{-1}psi = Ch/lambda, lambda = <h, Ch>. The inverse form of DCD is
||C^{-1/2} D^{-1} v||^2 by the variational formula with w = Dz. So
<f psi, U^{-1} f psi> = lambda^{-1} ||C^{-1/2} f C h||^2. Checks:
- Multiplier of C_e on degree l: from e^{beta cos theta} =
  (2/beta) sum (l+1) I_{l+1}(beta) chi_{l/2}, it is (2/beta) I_{l+1}, so
  r_l = I_{l+1}/I_1.
- Riccati: R = I_{k+1}/I_k has R' = 1 - (2k+1)R/beta - R^2 (re-derived from
  I_k' = I_{k+1} + k I_k/beta and I_{k+1}' = I_k - (k+1) I_{k+1}/beta); at R = 1,
  R' < 0; so R < 1. Upward: I_k/I_{k+1} = 2(k+1)/beta + I_{k+2}/I_{k+1} <=
  1 + 2(k+1)/beta. So r_l/r_{l+1} <= C(1 + l/beta) at beta >= 1.
- Block bound: <= 81 x 4 x C^4 sum_alpha prod_{e in p}(1 + alpha_e/beta)
  ||v_alpha||^2, and 1 + x <= 2(1 + x^2) gives the (1 - Delta_e/beta^2) form.
- Kernel: (1 - Delta/beta^2) e^{beta z} = e^{beta z}(z^2 + 3z/beta), from
  Delta z = -3z and |grad z|^2 = 1 - z^2; |z^2 + 3z/beta| <= 4. With h >= 0 the
  form is <= 4^4 lambda. So C_1 = 81 x 4 x 16 C^4 x 4^4, absolute.
- Gauge-invariant restriction: DCD commutes with the gauge action, so the
  invariant subspace reduces it and the inverse form agrees there.

**S22. (17) from (18) (L263). HOLDS.** V^*V >= c(1+beta)^{-2} I (covariance
matrix), Tr(V^* U^{-1} V) <= C_1 M; with W = V(V^*V)^{-1/2},
Tr(W^* U^{-1} W) <= ||(V^*V)^{-1}|| C_1 M. At most M/2 eigenvalues of this
compression exceed twice the mean bound; min-max for U^{-1} on the excited
neutral sector (compact U, vectors in the form domain) gives >= M/2 eigenvalues
of U at least 1/[C(1+beta)^2]. The consequence for beta = O(log n) and
u = o(log n/log log n) is right.

**S23. Fluctuating observable, c_0 = 1/4 (L273-281). HOLDS.** Density of the
tilted law against Haar <= e^s/Z(s) <= C(1+s)^{3/2}. div(e^{st} grad t) with
Delta t = -3t gives s E|grad t|^2 = 3 E t <= 3. For theta = arccos(a.v),
p(theta) = (2/pi) sin^2(theta) rho(theta); differentiating gives
int |p'| <= 2 E|cot theta| + s E|grad t|. Off the caps 1/sin <= sqrt(1+s);
inside, density bound times int_cap sin = O((1+s)^{-1}) gives O((1+s)^{1/2});
Cauchy-Schwarz gives s E|grad t| <= sqrt(3s). Integration by parts with
sin(l pi) = 0 gives |E cos(l theta)| <= C sqrt(1+s)/l. With A >= 8C sqrt(7),
both |E cos(d theta)|, |E cos(2d theta)| <= 1/8 for s <= 6beta, beta >= 1, and
Var cos(d theta) >= 1/2 - 1/16 - 1/64 = 27/64 >= 1/4.

**S24. (20) (L283-306). HOLDS.** Bands of width d: multiplying by a polynomial
of degree <= d moves a harmonic degree by at most d, so each output band meets at
most three input bands per link. Worst ratio: at most 3d upward factors, each
<= 1 + 2(l + 3d + 2)/beta, so <= exp(6d(l + 3d + 2)/beta) <= exp(C_A + C_A
l/sqrt(beta)) with d <= (A+1) sqrt(beta). Cauchy-Schwarz over <= 3^b inputs and
||f|| <= 2 give C_A^b <h, C prod exp(C_A l_e/sqrt(beta)) h>. Positive kernel:
for g in SU(2), V H_y V^{-1} = cosh y + sinh y (n.sigma), and
Re (1/2) tr(g n.sigma) = 0, so |c_beta(g V H_y V^{-1})| = exp(beta cosh(y)
tr g/2), giving the bound c_beta(g) e^{beta(cosh y - 1)}. Schur averaging gives
multiplier r_l chi_{l/2}(H_y)/(l+1) = r_l m_l(y); keeping j <= l/4 gives
m_l >= e^{ly/2}/4 (floor(l/4) + 1 >= (l+1)/4). With y = 2C_A/sqrt(beta),
e^{ly/2} = exp(C_A l/sqrt(beta)) <= 4 m_l(y), and beta(cosh y - 1) <=
cosh(2C_A) - 1. So the form is <= (const)^b lambda, uniformly in the volume.

**S25. (19) (L267-271, L308). HOLDS.** g_S = prod T_d(W_p) has degree <= d in
each of 4k links (Chebyshev; disjoint plaquettes). Given the exterior, write
g_p = mu_p + gamma_p with gamma_p independent and centred, Var >= 1/4. In
sum_{|S|=k} t_S (g_S - E g_S) the part with all k factors centred is orthogonal
to every other part (some centred factor appears once), so the conditional
variance is >= 4^{-k} sum t_S^2. Then Tr(compressed inverse form) <=
binom(M,k) (C_A^4 4)^k; at least half the eigenvalues of the compression are
<= 2(4 C_A^4)^k; min-max gives at least (1/2) binom(M,k) excited neutral levels
with -log(lambda/lambda_0) <= log 2 + k log(4 C_A^4) <= Ck. The constants do not
depend on beta >= 1 or n. The k = 1 case gives s(u) >= (M/2) e^{-Cu}.

**S26. Range of the obstruction (L310). HOLDS.** binom(M,k) >= (M/k)^k with
k = floor(M e^{-Cu}/2) gives a contribution >= 2^{k-1}; u = o(log n) or
u <= epsilon log n with C epsilon < 3 forces s(u) -> infinity.

**S27. Credit sentence at L235. HOLDS AFTER CORRECTION (credit only).** The
paragraph names PR 10114 (exp(-68 beta), confirmed) and row 1147 section 11
(products of plaquette trial states with single-boundary couplings removed,
confirmed at L357-370 of `gap-solve3-astra62.md`) and then says that
(17)-(20) "keep every Wilson coupling". Row 1153 (13) (`gap-solve6-astra62.md`
L224-230), in the chain this row builds on, already gives a lower count of the
actual homogeneous Wilson spectrum at every coupling, floor(c_1 sqrt(beta))^l
levels with energy at most C(1 + beta) l, by a cut-transfer eigenvalue
comparison. The note never cites row 1153. Correction: name row 1153 (13) in
this credit list. (19) is still new: its energies Ck do not grow with beta, and
its count is (1/2) binom(M, k). No mathematical statement changes.

Step 5 verdict: S20-S26 HOLD; S27 HOLDS AFTER CORRECTION (credit only).

### Step 6. Everything else

**S28. Repo search and credits (L3, L5). GUIDE; consistent where spot-checked.**
`git show` at `a2f6a430e2` shows a constrained-field estimate at `fp1.md`
L302-315; `f76f6c649c` holds the PR 10114 witness. The outline and CA-I line
ranges were not re-fetched; they match those checked in row 1157.

**S29. (1) and its A = 2 corollary (L17-29). HOLDS.** I_R(2t) = int p_t(x,y)
p_t(x,Ry) by symmetry, R-invariance and composition; int (q_t - 1)^2 =
Tr(P_+ P^{2t}) - 1. On q_t <= A, p_t(x, gy) <= 8 q_t <= 8A, so the product is
<= 8A min. On {q_t > A}, orbit averaging, pairing g with Rg and
sum_pairs a_g a_{Rg} <= (sum_g a_g)^2/4 give 4 q_t^2; and
q^2 <= (A/(A-1))^2 (q - 1)^2 there. At A = 2, (A/(A-1))^2 = 4, so
I_R <= 16 tau_R + 16 s_+, and Tr P^{2t} >= 1 gives the stated overlap bound.

**S30. (2) and its corollary (L31-38). HOLDS.** For a real unit eigenfunction h
in a character odd under R: Var|h| <= (1 - b^u)/(1 - rho^u) by contraction and
the neutral Poincare inequality of the positive P^u. With sigma = sign h
(equivariant signs exist off a null set), P^t sigma(x) = (1/2) int sigma
(p_t(x,.) - p_t(x,R.)), so |P^t sigma| <= 1 - tau_t(x) and ||P^t sigma||^2 <=
1 - tau_R(t); projection on h gives ||P^t sigma||^2 >= b^{2t} (int|h|)^2.
With u = 2t and b^{2t} <= 1: 1 - b^{2t} >= (1 - rho^{2t}) tau_R/(2 - rho^{2t}).
The overlap tau_R(t) is row 1158's taubar_t; since tau >= tau^2 and
1 - rho^{2t} >= 1 - rho^t, this improves Lemma F as claimed.

**S31. OPEN at L40, L109, L192, L339. HOLD as statements of scope.** L109: the
proof needs u <= n/K; compactness at fixed cutoff gives s(u) < 1 only for long
times. L192: row 1143 (6) has an O(V) error, so it fixes b. L339: if
[0, beta] lies in N, connectedness and (22) put it in P, and then (13) holds at
those couplings; this implication is correct and is labelled OPEN only for its
input.

**S32. GUIDE comparisons (L44, L81, L333). HOLD.** Theorem R and Corollary R6 of
`gap-means-max.md` do assume (ES), a small even thermal sum and a small
vacuum-energy additivity defect; row 1157 (23) controls all twists through one
transverse zero-class probability near 1/8.

**S33. (15) (L196-200). HOLDS.** Row 1143 (6), valid on every rectangle with
sides >= 3 and beta >= 2, gives -log zeta = (3/2) log beta + log log beta +
O(n^4), so zeta -> 0 at fixed n; zeta = 1 at beta = 0; continuity gives
beta_n. If zeta stays in [alpha, 1 - alpha] and liminf X_{0,0}(u) < 2 for some
u = o(n), a subsequence satisfies (8), and (9) at r = 1 gives zeta -> 0 or 1.

**S34. (16) (L202-207). HOLDS.** gamma^{n_i} = -1 gives ord(gamma^2) >=
2^{nu_2(n_i)}. D_i fixes the simple positive magnetic vacuum psi_m (a
composition operator commuting with F_m), so it is unitary on L^2(pi_m) and
z = phi/psi_m has D_i z = gamma z. w_l = |z| e^{2il arg z} is neutral and has
phase gamma^{2l}; distinct phases give orthonormality. The d-Lipschitz bound
follows from (r - r')^2 + 4 r r' sin^2(d alpha/2) and |sin(dx)| <= d|sin x|.
So <w_l, P_m^u w_l> >= [1 - (2l)^2 (1 - (b/a)^u)]_+, and the trace over the
neutral sector, times a^u, is X_{m,0}(u) <= X_{0,0}(u).

**S35. Bounded-count version of (9) (L209-211). HOLDS.** With H = floor(C) + 1
<= 2^{nu_2(n)} <= ord(gamma^2), a misaligned level with b^n bounded below gives
a^u, (b/a)^u -> 1 and contradicts (16). Levels beyond the first floor(C) in a
sector have u-th power <= C/(floor(C) + 1) < 1. With w = ceil(n/sqrt(min(n,
n m_+))), w/n -> 0 and w m_+ -> infinity; row 1157 (1) gives b_2^w <=
(3 + e^{-w m_+})/4, so b_2^n -> 0 in each periodic charged sector. The
derivative identity now has finitely many magnetic levels, each a log a <= 0,
so each weight is 0 or 1, and the magnetic vacuum dominates; this gives (9).

**S36. (21) (L314-323). HOLDS.** H_i flips sign under C_i only; its zero set is
Haar-null because it is affine and nonconstant in one link quaternion; pi is
absolutely continuous. K_{c,M} = sum_S c^{|S|} M_{h_S} Q M_{h_S}; each term maps
character S to itself because Q = P P_+; on the neutral sector K = Q, so all
centre-invariant correlations are the Wilson ones. The character-S spectrum is
that of c^{|S|} Q^{1/2} M_{h_S^2} Q^{1/2} (AA^* versus A^*A); the positive
difference from Q has trace -> 0 by dominated convergence, so traces of powers
converge and Fourier cancellation sends twist ratios to zero. At c = 0 they are
one. (2) applies to K and makes the overlap small.

**S37. (22) (L327-335). HOLDS.** Continuity of W_w and of lambda_0 in beta makes
P and M open in [0, infinity); 0 is in P (rank-one transfer, S_per = 0). The
explicit test (S12) gives N inside P union M and a Pfaffian seed on N. A seed in
P, M or the kappa class propagates at fixed beta (Theorem S-w); B3 for W_w from
b^3 to (512b)^3 at time b/2 has a fixed multiplier 1024^3, then time b; so
s(b; (512b)^3) -> 0 and beta is in N (n = 512b >= 2^70, 4 | n). P and M are
disjoint: P gives zeta -> 1, M gives (14).

**S38. beta_* (L337). HOLDS.** [0, beta_1] cannot be the disjoint union of two
nonempty relatively open sets, so some beta_* in (0, beta_1) lies outside N. At
that fixed coupling, any sequence with liminf X_{0,0}(u) < 2 would give (9) and
hence a periodic or all-magnetic seed at a finite size.

**S39. (23) (L343-351). HOLDS.** Lower links of a plaquette start at residue s,
upper ones at s + 1 (p even, so parity is well defined); only one residue is
even and the four sets A_mu are disjoint; so no face has two selected links.
Each straight circuit meets every residue at least once, hence >= m = floor(p/8)
selected links; each link is on one circuit. Row 1145 (1) bounds each
multiplier by e^{-(d-1)/b_beta}; Peter-Weyl gives the per-line density error
eta(m/B_beta); conditional independence gives the product bound.

**S40. (24) and the TV consequence (L353-358). HOLDS.** On one slice, residues
mod n are split among three directions, m' = floor(n/6), N' = 3n^2; temporal
plaquettes hold one chosen spatial link each. A character-matched f(Y_0) has
Haar mean zero (flip all windings of an odd direction); so
|E(f | exterior)| <= delta ||f||_{L^2(Haar)}; the next slice is exterior-
measurable; the one-slice density >= 1 - delta converts Haar norms to pi norms;
<f, P h> = b <f, h>. Two laws each within the sup-norm density error of Haar are
within that error in TV.

**S41. (25) (L362-371). HOLDS, given row 1157 (28)-(29) (checked).**
D(P||Q) >= P(E) log(1/Q(E)) - log 2 for Q of mass <= 1 (log-sum inequality).
Failure event under L(A) x mu_0 has mass <= C' e^{-c_1 M}, and
D(L(A,U) || L(A) x mu_0) = I_in, so P(failure) <= (I_in + log 2)/(c_1 M - C).
The chain rule D(L(A,Y) || L(A) x mu~_B) = I_out + D(nu || mu~_B) holds for a
finite reference measure. The optimum D(mu_B || mu~_B) = -log zeta is right.

**S42. Sign-product comparison (L375). HOLDS.** The two-state kernel has
eigenvalues 1 and e^{-C}; the tensor power has binom(M,k) levels e^{-Ck}; its
excited trace at u is (1 + e^{-Cu})^M - 1 <= exp(M e^{-Cu}) - 1 -> 0. One added
level e^{-1/n^2} makes it tend to one. Both models satisfy the full count.

**S43. Finite neutral moment tests (L404-413). HOLDS.** t = F(W_p) is
continuous and uniform (no atoms: {W_p = c} is Haar-null). w_d has mean zero,
norm independent of d, and tends weakly to zero (step-function approximation of
E(g | t)); ||Pi_V w_d||_inf -> 0 by a continuous orthonormal basis of V. The
kernels 1 and 1 + c k(x)k(y) are strictly positive Markov kernels with spectra
{1, 0} and {1, c||k||^2, 0}; both send V to constants, so strings at distinct
times factor identically; both kill charged functions, so all twist ratios are
one.

**S44. Framing lines L9, L11, L13, L415, L419, L421. HOLD.** L13 calls rows 1157
and 1158 unchecked; at this checkout row 1157 has the check of row 1160 (all
hold), and row 1158 is still unchecked. No step here depends on row 1158: (2)
is proved directly. L419 and L421 state the open items correctly.

**S45. RESULT line (L423). HOLDS as a summary**, with the range 4 | n,
n >= 2^70 and the cutoff-uniformity at one admissible cube left implicit (both
are stated in the body).

Step 6 verdict: S28-S45 HOLD (S28 as GUIDE). No FAILS.

### Step 7. Guide run (GUIDE only; no step above depends on it)

Two pure Python and numpy scripts in the session scratchpad (not kept in the
repository), run with `python3 -E -P`; peak memory about 200 MB.
- Arithmetic of S5 and S12: all stated constants confirmed (log_2 h = -211.5;
  h/r + 384 r < 2^{-59} on [2^{-70}, 2^{-69}]; 56 x 2^{-18} = 2.1 x 10^{-4}).
- All 64 alternating 4 x 4 forms over F_2: ranks 0/2/4 occur 1/35/28 times.
  Breadth-first search with e_i -> e_i + e_j needs at most 4 additions to reach
  the normal form of the same rank (the proof's bound 10 is safe). Each addition
  changes 0 or 4 of the 8 electric signs. 56 twists restrict to nonzero bits on a
  transverse three-torus. Every rank-4 twist has a nonzero static part.
- (1) and (2) on 60 random and 300 slowly mixing finite reversible chains with a
  free Z_2^3 action (33390 cases): no violation; smallest slack 0.16 for (1)
  (largest lhs/rhs 0.28) and 4 x 10^{-6} for (2).
- The map z -> |z| e^{i d arg z}: largest ratio to d|z - z'| is 1.000000.
- Bessel ratios, the Schur multiplier bound m_l(y) >= e^{ly/2}/4 and
  |z^2 + 3z/beta| <= 4 hold on the tested grids.
- c_0: with d = ceil(A sqrt(beta)) and tilt 6 beta, the smallest variance of
  cos(d theta) over beta in {1, 4, 16} and three directions is 0.012 (A = 1),
  0.100 (A = 2) and 0.280 (A = 4). This agrees with "a sufficiently large fixed
  A"; the proof's A is not computed and need not be.

### Step 8. Verdict table

| # | Statement (lines of `gap-solve9-astra62.md`) | Verdict |
|---|---|---|
| S1 | Even multiplicity when Mq != 0; six of eight characters (L46) | HOLDS |
| S2 | (3): sector order, b_{m,q} <= 1 (L48-53) | HOLDS |
| S3 | (4): misaligned and higher-level bounds (L55-63) | HOLDS |
| S4 | (5): equal-rank twist weights within 160h (L67-79) | HOLDS |
| S5 | Two alternatives on Q_t, Q_{2t}, (6) (L85-99) | HOLDS |
| S6 | (7): S_kappa <= 113 eta in either alternative (L101-105) | HOLDS |
| S7 | Transverse floor 616 eta selects I; (W) (L107) | HOLDS |
| S8 | (8)-(10): one periodic cube gives the dichotomy (9) (L113-144) | HOLDS |
| S9 | One finite aspect K (existence, order of choices) (L146) | HOLDS |
| S10 | Consumer: Pfaffian seed 8 epsilon; floor 56 epsilon (L148) | HOLDS |
| S11 | Necessity over physical sizes; Pfaffian converse (L150) | HOLDS |
| S12 | Explicit test K = 512, n >= 2^70 (L215-227) | HOLDS |
| S13 | (13) suffices for (W), with (14) (L171-183) | HOLDS |
| S14 | (13) necessary under (W); the equivalence (L183) | HOLDS |
| S15 | Row 720 variables: (BDD-Delta) and z_+ give the neutral test (L185-190) | HOLDS |
| S16 | One-period test (11)-(12) (L154-165) | HOLDS |
| S17 | Raw-collar version and converse (L167) | HOLDS (given checked rows 1155, 1157) |
| S18 | (26) (L379-387) | HOLDS |
| S19 | Three neutral conditions equivalent to the Pfaffian seed (L389-400) | HOLDS |
| S20 | Gram bound c(1+beta)^{-2} (L237-246) | HOLDS |
| S21 | (18): local inverse moment, absolute C_1 (L248-261) | HOLDS |
| S22 | (17) by min-max (L263) | HOLDS |
| S23 | Fluctuating observable, c_0 = 1/4 (L273-281) | HOLDS |
| S24 | (20): inverse moment at degree d = ceil(A sqrt beta) (L283-306) | HOLDS |
| S25 | (19): (1/2) binom(M,k) neutral levels with energy <= Ck (L267-271, L308) | HOLDS |
| S26 | Range: u = o(log n) excluded (L310) | HOLDS |
| S27 | Credit list for (17)-(20) (L235) | HOLDS AFTER CORRECTION (credit only) |
| S28 | Repo search and credits (L3, L5) | GUIDE; consistent at spot checks |
| S29 | (1) and the A = 2 overlap bound (L17-29) | HOLDS |
| S30 | (2) and its corollary; comparison with Lemma F (L31-38) | HOLDS |
| S31 | OPEN paragraphs (L40, L109, L192, L339) | HOLD as scope statements |
| S32 | GUIDE comparisons (L44, L81, L333) | HOLD |
| S33 | (15) (L196-200) | HOLDS |
| S34 | (16) (L202-207) | HOLDS |
| S35 | Bounded-count version of (9) (L209-211) | HOLDS |
| S36 | (21): one-frame neutral obstruction (L314-323) | HOLDS |
| S37 | (22): N = P disjoint-union M, open, 0 in P (L327-335) | HOLDS |
| S38 | A fixed beta_* with neither seed (L337) | HOLDS |
| S39 | (23): all straight windings nearly Haar (L343-351) | HOLDS |
| S40 | (24) and the TV consequence (L353-358) | HOLDS |
| S41 | (25): randomized trial law cost (L362-371) | HOLDS (given checked row 1157 (28)-(29)) |
| S42 | Sign-product limit of the counting input (L375) | HOLDS |
| S43 | Finite neutral moment tests (L404-413) | HOLDS |
| S44 | Framing lines (L9, L11, L13, L415, L419, L421) | HOLD |
| S45 | RESULT line (L423) | HOLDS as a summary |

Counts: 45 statements; 44 HOLD (S28 as GUIDE); 1 HOLDS AFTER CORRECTION
(S27, credit only); none FAILS.

The one correction. L235 should also name row 1153 (13)
(`library/gap-solve6-astra62.md` L224-230): a lower count of actual Wilson
levels at every coupling, floor(c_1 sqrt(beta))^l levels with energy at most
C(1 + beta) l. The new count (19) differs in having energies Ck independent of
beta. No threshold, constant or conclusion changes.

Notes for the lead (no verdict changes):
- The central theorem is (9). It needs the neutral bound on the single cube
  n^3 only, plus positivity of sector traces on rectangular tori. I found no gap
  in the derivative argument at r = 1.
- The explicit K = 512 test is a hand argument with all constants checked. Its
  range is 4 | n, n >= 2^70; the RESULT line leaves this range implicit.
- Row 1157 has now been checked (row 1160, all hold). Row 1158 is still
  unchecked, but nothing here depends on it.
- Open, as the note says: the physical neutral bound s_j(floor(n/512); n) <= 1/2
  on one admissible cube, the flux-branch choice ((13) or a transverse floor),
  (W), and the mass gap.

Committed file paths here are repository-relative. No commit, push, checkout or
stash was run.

RESULT: HOLDS AFTER CORRECTION (credit only) - check of row 1161 (`library/gap-solve9-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1162, positive claims first: 45 statements, 44 HOLD, 1 HOLDS AFTER CORRECTION (L235 must also credit row 1153 (13), a lower count of actual Wilson levels with energies C(1+beta)l; no mathematics changes), none FAILS; in particular the one-cube dichotomy (9) with the Pfaffian seed and the explicit K = 512, n >= 2^70 test, the selection by (13) with (14) and its necessity under (W), the local criteria (26) and their equivalences, and the beta-independent count (19) via (17), (18), (20); guide runs (about 200 MB, pure Python and numpy) agree and prove nothing; the physical neutral bound, the flux-branch choice, (W) and the four-dimensional SU(2) mass gap remain OPEN.
