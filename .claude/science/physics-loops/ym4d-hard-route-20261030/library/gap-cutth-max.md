# FINISH row 910, gap-cutth-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone commit: f507af666db1226a845f5ef08583a75d7f984564 (/Users/jonreilly/ym4d-lead/clone, pulled 2026-11-13, already up to date).
Author: Claude Fable 5.2, max effort. Row 910. Labels: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE, OPEN.

## Target

The doubling hypothesis of the free-wall seed engine (Theorem C of row 907, as corrected by check 909).
The engine needs g(a, 2b) at most k g(a, b) on dyadic cubes and a seed s_0 below 1/(4 k^6).
Candidate forms: (CUT-TH) with the full or the centre-even ring sum; the thermal pair (H-W), (H-tau); or a corrected statement.
Task 1: decide which form survives the fact tests and state exactly what the engine needs.
Task 2: attack it for Wilson SU(2) at order one; prove it with explicit constants or reduce it to one named statement.
Task 3: say whether the engine with that target passes U(1), Z_2, frozen Q_8 and 2T.

## Plan (one step per response; each step appended before the next)

1. Read rows 907 and 909 (the engine, both doubling identities, the cut identity, the Q_8 failure). Record the exact statements used.
2. Read rows 898/902 (family Z(P: a; F: b, c, d), FW1-FW6) and 903/906 (free-field values). Record only what the attack needs.
3. Task 1: what the engine actually needs. Diagnose the Q_8 failure and state the corrected doubling target exactly.
4. Exact middle-term formula: the coupling integral of the cut energy. Derive it and its sign/monotonicity properties.
5. Attack A: reflection positivity in the periodic time direction (chessboard / Cauchy-Schwarz on the cut layer) toward the doubling bound.
6. Attack B: correlation inequalities or convexity for the cut layer; get explicit theta, k, ranges, or the one named statement where it stops.
7. Task 3: run the target through U(1), Z_2, frozen Q_8, 2T.
8. Assemble: what is proved, what is open, the RESULT line.

## Steps

### Step 1. What rows 907 and 909 give (READ; L = D/library/gap-fw-wilson-max.md, C = D/library/gap-fw-wilson-check-astra.md)

Objects (READ L 29-48, 68-80).
- Free box: W(a, b) = Z(P: a; F: b, c, d) = Tr M_b^a = <v_a, R_a^(b-1) v_a>. g(a, b) = log(Tr M_b^a / lambda_0(b)^a) >= 0. e(b) = log lambda_0(b) = f b - D_inf + delta_e(b).
- Crossed channel: R_a = B_0^(1/2) K B_0^(1/2) on the slice (P: a; F: c, d), v_a = B_0^(1/2) 1, W = w_0(a) r_0(a)^(b-1) e^(gamma(b, a)), gamma >= 0 non-increasing in b.
- FW5: g(a, b) = (b-1) p(a) + c(a) + tau(a, b), tau = gamma(b, a) - a delta_e(b) -> 0 as b -> infinity. p(a) = log r_0(a) - a f >= 0, convex, non-increasing (C 68-91: HOLDS).
- Ring: P(a, n) = Tr R_a^n = Z(P: a, P: n; F: c, d), symmetric in (a, n). g_P(a; n) = log(P(a, n)/r_0(n)^a) = thermal log-sum at time a of the ring cross-section (P: n; F: c, d).
- (D2) a p(n) + g_P(a; n) = n p(a) + g_P(n; a). (D3) g_P(a; n) >= (n - a) p(a), n >= a. Lemma E: g_P(a; 2b) <= 2 g_P(a; b) + 2 a p(b) <= (2b/(b-a)) g_P(a; b). All three hold for the centre-even ring sum g_P^ev, P^ev = (P + P^tw)/2 (C 282-292: HOLDS).
- (CUT) (L 159-166; C 261-310 HOLDS): g_P^ev(a; n) - g(a, n) = F_cut^ev(a; n) - a phi_cut(n); F_cut^ev = log P^ev - log W = beta int_0^1 <X_cut>_(ev; a, n; s) ds; phi_cut(n) = eps(n) - e(n) = p(n) + D_inf - delta_e(n).
- (DBL-ID) g(a, b+h) = g(a, b) + h p(a) + tau(a, b+h) - tau(a, b). (DBL-ID2) g(a, 2b) = 2 g(a, b) + [p(a) - c(a)] + [tau(a, 2b) - 2 tau(a, b)], p - c = log(r_0/w_0) - a D_inf (C 150-169: HOLDS).
- Theorem C (L 219-227; C 365-386 HOLDS). Ladder a_j = 2^j a_0, b_j = 2^j b_0, a_0 >= 3. (H-DBL): each of the three steps (b,b,b) -> (2b,b,b) -> (2b,2b,b) -> (2b,2b,2b) at time a_j has g(after) <= k g(before). (H-SEED): s_0 = S(a_0; b_0^3) < 1/(4 k^6). Then s_j <= (B s_0)^(2^j)/B, B = 4 k^6, and m(b_j^3) >= log(1/(B s_0))/a_0.
- Sufficient conditions (L 229-236; C 388-408 HOLD as implications): (S1) (WALL-1)+(WALL-2); (S2) (WALL-1)+(CORNER); (S3) (CUT-TH), k = 4(1+theta')/(1-theta) (C 339-363: this constant, not the printed one); (S4) (H-W) p - c <= C_w g and (H-tau) tau(a, 2b) - 2 tau(a, b) <= C_tau g, k = 2 + C_w + C_tau.

Failures recorded by check 909 that bind this row.
- (C 312-327) Frozen Q_8: the ring's frozen transfer acts on class functions of the ring holonomy, classes {1}, {-1}, {+-i}, {+-j}, {+-k}. Even subspace has dimension 4. So g_P^ev -> log 4 and g -> 0. (RING-CMP-ev) and (CUT-TH) with fixed theta < 1 FAIL there, in both the full and the even form.
- (C 329-337) "Centre-even" is not "flux-free". For U(1) the flip at -1 keeps charge 2.
- (C 110-115) No theorem excludes every RP argument; only the monomial-word family was classified.
- (C 538-555) No uniform combined bound on C_w + C_tau in the real-multiplicity family; the two terms of (DBL-ID2) can cancel, so only their sum is intrinsic.
- (C 253-259) The crossed vector sum sees only wall-visible states.

Observation that drives Step 3 (mine, ARGUED here, made exact in Step 3). In (CUT-TH) the left object g_P^ev counts every state of the ring cross-section that is even under one central flip. For frozen Q_8 these are the four characters of Q_8/{+-1} of the ring holonomy: electric fluxes of trivial N-ality round the ring. The free box has no ring and no such state. The engine needs only (H-DBL), a statement about free boxes. So (CUT-TH) asks for more than the engine needs, and the surplus is a flux statement about the ring.

### Step 2. Rows 898/902 and 903/906: only what the attack needs (READ; N = D/library/gap-next3-max.md, G = D/library/gap-fw-gauss-opus.md, F = D/library/gap-finishline-opus.md)

- Setup (N 398-400). Weight prod_p exp(beta x_p), x_p = (1/2) tr U_p, Haar probability on links. Transfer M = B_0^(1/2) K B_0^(1/2), K = (gauge projection)(link-wise convolution by the weight) >= 0. Periodic time: Z = Tr M^(n_1). Free time: Z = <u, M^(n_1 - 1) u>, u = B_0^(1/2) 1.
- FW1 (N 402): across a free direction the flip of the crossing links is a gauge transformation. No centre sector, no twist, in a box with free space sides.
- FW2 (N 404): Z is super-multiplicative in a free side (Jensen; each crossing plaquette holds a Haar link). FW3 (N 406): e convex in the free side; D(b) = f b - e(b) in [0, beta N]; delta_e = D_inf - D >= 0 non-increasing. FW4 (N 408): S(a; B) >= (lambda_1/lambda_0)^a.
- Theorem S on tori (N 396): (K) Tr T^(jb) <= (Tr T^b)^j; (X) a kappa(b) + g(a, b) = b kappa(a) + g(b, a); (E) 1 + S(a; 2b) <= (1 + S(a; b))^(2b/(b-a)); squaring S(2n) <= S(n)^2. "Both rest on integer multiplicities."
- Free scalar, Neumann walls (G 62-86): g = sum over modes of F_a(omega_K), F_a(w) = -log(1 - e^(-a w)); p(a) = sum_T (1/pi) int_0^pi F_a(omega_T(theta)) d theta; c = p + W_N, W_N = (1/2) sum_T [F_T(0) - F_T(pi)] > 0; tau = 2b sum_T sum_(j>=1) hat F_T(2bj) > 0; g(a, 2b) <= 2 g(a, b) (mode pairing, C 196-198). GUIDE (L 271-277): (g - g_P)/g_P in [0.016, 0.30] on a <= b/2.
- The real object (F 114-124): (SEED-FP) is the thermal sum of the bare Wilson transfer operator of a cube of fixed physical side along first passage, with margin s_* fixed. So every constant of a doubling bound must be uniform along the first-passage trajectory to be of use. A bound at one bare beta in 2.3 to 2.6 is a model problem. (ARGUED from F 150-156.)

### Step 3a. Task 1, first part: the join identity. What the engine needs, with no ring in it (PROVED)

Setting. B a free space box, B|B the box of doubled side in one free direction, cut = the layer of plaquettes that contain a link crossing the middle plane. N_x := number of cut plaquettes per time step (space-like and time-like).
Definitions. F_join(a; B) := log W(a; B|B) - 2 log W(a; B). J_0(B) := e(B|B) - 2 e(B).
Facts. F_join(a; B) = log E[exp(beta X_cut)] under (two independent boxes) x (Haar crossing links), X_cut = sum of x_p over the cut (this is FW2's formula). So 0 <= F_join <= beta a N_x and 0 <= J_0 <= beta N_x. J_0(B) = lim_T F_join(T; B)/T.

Lemma J (join identity). g(a; B|B) - 2 g(a; B) = F_join(a; B) - a J_0(B).
Proof. g(a; .) = log W(a; .) - a e(.). Subtract. QED
Coupling form. Let W_s be the partition function of B|B with the cut plaquettes at coupling s beta, 0 <= s <= 1. W_0 = W(a; B)^2 (the crossing links are Haar and decouple), W_1 = W(a; B|B). The time transfer M_s is positive for every s (the cut weight exp(s beta x) has non-negative character coefficients). Put e_s := log lambda_0(M_s), g_s(a) := log Tr M_s^a - a e_s. Then g_0 = 2 g(a; B), g_1 = g(a; B|B), and
  (J-INT) g(a; B|B) - 2 g(a; B) = beta int_0^1 [ <X_cut>_(a; s) - a <x_cut>_(vac; s) ] ds,
where <x_cut>_(vac; s) = lim_T <X_cut>_(T; s)/T = (1/beta) d e_s/ds. (Same justification as C 304-310: a simple top eigenvalue, smooth in s.)
Relation to rows 907/909. Lemma J is (DBL-ID2) with its two terms added: F_join(a; B) = log(r_0/w_0) + gamma(2b, a) - 2 gamma(b, a) and a J_0 = a [D_inf + delta_e(2b) - 2 delta_e(b)]. Check 909 (C 538-555) showed that only the sum of the two terms of (DBL-ID2) is intrinsic. Lemma J is that sum. It contains no ring, no r_0, no w_0, no delta_e, no twist.

The target, exactly.
  (JOIN-TH_kappa) F_join(a; B) - a J_0(B) <= kappa g(a; B).
By Lemma J, (JOIN-TH_kappa) is EQUIVALENT to g(a; B|B) <= (2 + kappa) g(a; B). So (H-DBL) with constant k is (JOIN-TH_(k-2)) on the three rectangles of each ladder level. In words: joining two free boxes raises the thermal log-sum by at most kappa thermal log-sums of one box; the thermal excess of the joining free energy is at most kappa g.

Verdict on the listed forms.
- (CUT-TH), full ring sum: REJECTED as the target. It fails frozen Z_2 (L 293-295).
- (CUT-TH), centre-even ring sum: REJECTED as the target. It fails frozen Q_8 (C 312-327). Exact reason: by (CUT), F_cut^ev - a phi_cut = g_P^ev - g, and for frozen Q_8 this tends to log 4 = log(number of even characters of the ring holonomy). (CUT-TH) is (H-DBL) PLUS the statement that the ring cross-section has no light even state beyond those of the free box. That surplus is a flux statement about the ring (for SU(2): no light state of trivial N-ality carried by the ring holonomy). The engine does not use it. A proof of (CUT-TH) for SU(2) would have to use a property that Q_8 lacks; a proof of (JOIN-TH) need not.
- Thermal pair (H-W), (H-tau): a valid sufficient pair. It is not the target: the two terms can cancel (C 558-559), and each separately involves the crossed vacuum (r_0, w_0). Their sum is Lemma J.
- Corrected statement (mine): (JOIN-TH_kappa), restricted to the boxes the ladder really visits (Step 3b). Two more sufficient pairs stay available as routes: (WALL-1)+(CORNER) and (WALL-1)+(WALL-2).

### Step 3b. Task 1, second part: the engine needs the doubling bound only on boxes that are already cold (PROVED)

Theorem C' (restricted hypothesis). Keep the setting, the ladder and (H-SEED) of Theorem C: k >= 1, B = 4 k^6, s_0 = S(a_0; b_0^3) < 1/B. Replace (H-DBL) by
  (H-DBL-LT) for every j and each of the three steps at time a_j: IF S(a_j; before) <= 1/(3 k^4), THEN g(after) <= k g(before).
Then the conclusion of Theorem C holds unchanged.
Proof. Induction on j with the claim s_j <= s_0. Let x = s_j < 1/(4 k^6). The first "before" box is the cube: S = x <= 1/(3 k^4). So 1 + S_1 <= (1 + x)^k. By C 370-373, (1 + x)^A - 1 <= (4/3) A x when A x <= 1/4. Here k x <= 1/4, so S_1 <= (4/3) k x < 1/(3 k^5) <= 1/(3 k^4). The hypothesis applies to step 2: 1 + S_2 <= (1 + x)^(k^2), and k^2 x <= 1/4, so S_2 <= (4/3) k^2 x < 1/(3 k^4). The hypothesis applies to step 3: 1 + S_3 <= (1 + x)^(k^3). The rest is Theorem C: s_(j+1) <= S_3^2 <= (2 k^3 x)^2 = B x^2 < x. QED

Consequences.
- The target of Task 1 is (JOIN-TH_kappa) for cold boxes only: S(a; B) <= 1/(3 (2 + kappa)^4). On such a box m(B) >= log(3 k^4)/a (FW4). So the doubling hypothesis never speaks about a box with a light state on the scale 1/a. A model whose free boxes have a photon at the ladder shapes is outside the hypothesis; it fails at the seed.
- In the cold range g and S agree to a factor: S/(1 + S) <= g <= S. So the target may be read as S(a; B|B) <= k' S(a; B) with k' near 2 + kappa.

Statement of the target (answer to Task 1). For Wilson SU(2) at the given coupling there are kappa >= 0 and a ladder (a_j, b_j), a_0 >= 3, b_0 >= 2 a_0, such that for every j and each of the three rectangles B of level j with S(a_j; B) <= 1/(3 (2 + kappa)^4):
  (JOIN-TH_kappa) log W(a_j; B|B) - 2 log W(a_j; B) - a_j [e(B|B) - 2 e(B)] <= kappa g(a_j; B).
Then a seed s_0 < 1/(4 (2 + kappa)^6) gives m(b_j^3) >= log(1/(4 (2 + kappa)^6 s_0))/a_0 for all j. Nothing else is needed from the walls. Every object in (JOIN-TH) is a partition function of a free box or its zero-temperature rate.

### Step 3c. Task 1, third part: the doubling bound is not structural. Family 2P refutes (W'-ENG) in the class (PROVED; a re-read by the author only)

The class (READ N 412, N 431-437, L 196-198; C 210-225 accepted family T in it). Functions W(a; b, c, d), symmetric in (b, c, d), with
  (T) W = Tr M^a, M positive, integer multiplicities (time channel);
  (V) in each free variable n: W = sum_k w_k t_k^n, w_k >= 0, t_k >= 0, sum_k w_k <= 1 (a vector of norm at most one under a positive operator; for Wilson the vector is 1 and the operator is K^(1/2) B_0 K^(1/2), up to the factor c_0 per link);
  (FW2) super-multiplicative in each free variable, with a defect at most (constant) x a x (wall area).
Remark (PROVED). (V) implies (FW2): phi(n) = log W is convex on n >= 0 and phi(0) <= 0, so phi(n_1) + phi(n_2) <= phi(n_1 + n_2) + phi(0).

Family 2P (two phases, static oscillators). Fix f_A < f_B, D_B > D_A >= log 2, integers n_A, n_B >= 1, m_A > m_B > 0. Put DF = f_B - f_A, DD = D_B - D_A,
  E_X(b, c, d) := f_X bcd - D_X (bc + cd + bd),   W(a; b, c, d) := sum over X in {A, B} of exp(a E_X) (1 - e^(-a m_X))^(-n_X bcd).
Membership.
- (T): M = direct sum over X of exp(E_X - m_X N_X) on the Fock space of n_X bcd oscillators. Positive; every eigenvalue exp(E_X - m_X j) has an integer multiplicity.
- (V) in b (the same in c, d by symmetry): W = C_A t_A^b + C_B t_B^b, C_X = exp(-a D_X cd), t_X = exp(a f_X cd - a D_X (c + d)) (1 - e^(-a m_X))^(-n_X cd). C_A + C_B <= 2 e^(-log 2) = 1. Put the missing weight on the eigenvalue 0.
- (FW2): by the Remark. Defect: W(b_1 + b_2) <= max(1/C_X) W(b_1) W(b_2) = e^(a D_B cd) W(b_1) W(b_2).
So 2P is in the class. It is also a direct sum of two models of the class with different wall costs: the class is closed under that operation.

Data on cubes. E_A - E_B = b^2 (3 DD - DF b). Put b_* := 3 DD/DF. For b < b_* the vacuum is the A vacuum and
  1 + S(a; b^3) = (1 - e^(-a m_A))^(-n_A b^3) + e^(-a b^2 (3 DD - DF b)) (1 - e^(-a m_B))^(-n_B b^3).
For b > b_* the vacuum is the B vacuum, g(a; b^3) >= n_B b^3 F_a(m_B), and the gap is min(m_B, E_B - E_A) = m_B for b large.

Theorem 2P. For all absolute constants s' > 0, C with C s' < 1, and k >= 1:
 (i) (W'-ENG) (READ N 296) fails on the class: there is a member with S(a_0; b_0^3) <= s', b_0 = 2 a_0, and gap m_B < log(1/(C s'))/a_0 on every large cube.
 (ii) (H-DBL), (H-DBL-LT) and (JOIN-TH_(k-2)) fail on the class at a ladder level where S is as small as one likes on the box before the step.
Proof. (i) Fix a_0 >= 3, b_0 = 2 a_0, n_A = n_B = 1, m_B := log(1/(C s'))/(2 a_0), DF := 1. Take m_A with b_0^3 F_(a_0)(m_A) <= log(1 + s'/2). Take DD so large that 3 DD > b_0 and e^(-a_0 b_0^2 (3 DD - b_0)) (1 - e^(-a_0 m_B))^(-b_0^3) <= s'/2. Then S(a_0; b_0^3) <= s'. On cubes of side above b_* the gap is m_B. (ii) Fix a level, a = a_j, b = b_j, n_A = n_B = 1, a m_A >= log 2, and choose DD/DF with b/b_* in (1/2, 2/3). Then the boxes b^3, (2b, b, b), (2b, 2b, b) have the A vacuum (E_A - E_B equals b^2 (3 DD - DF b), b^2 (5 DD - 2 DF b), 4 b^2 (2 DD - DF b), all positive), and (2b)^3 has the B vacuum. With DF large, the other sector adds at most "tiny" := e^(-a (E_A - E_B)) (1 - e^(-a m_B))^(-vol) <= vol F_a(m_A) to g of each A box. So the first two ratios are near 2 and g(a; (2b, 2b, b)) <= 8 b^3 F_a(m_A) <= 16 b^3 e^(-a m_A), which is as small as one likes (m_A large): the box before the third step is cold. And g(a; (2b)^3) >= 8 b^3 F_a(m_B) >= 8 b^3 e^(-a m_B). The third ratio is at least (1/2) e^(a (m_A - m_B)). Choose a (m_A - m_B) > log(2k). The third step exceeds k. QED
GUIDE instance (arithmetic only; script and log in scratchpad/lane910/guide/guide_2p.py, guide_2p.log). f_A = 0, f_B = 1, D_A = log 2, D_B = D_A + 21 (b_* = 63), m_A = 2, m_B = 1, n = 1, a_0 = 20, b_0 = 40, k = 3. Seed s_0 = 2.7e-13 < 1/2916. Theorem C would give gaps >= 1.048. The gap of large cubes is 1.000. Step ratios at level 0: 2.000, 2.000, 9.7e8 (the vacuum changes at the third step). FW2 holds on the grid tested.

What this settles.
- Row 898's question (N 454: "(W'-ENG) is OPEN, neither proved nor refuted" in the class) and row 907's (L 202) are answered: REFUTED in the mixed class. Row 898's stop rule (N 487) names "a counterexample to (W'-ENG) in the class" as a stop. The Wilson statement is not refuted. Theorem C and C' stand; their doubling hypothesis cannot come from the class.
- Rows 898 and 907 searched single-sector forms with box-independent levels. 2P has two sectors and a box-dependent level: the second vacuum, at height b^2 (3 DD - DF b) above the first. It is invisible at the seed (e^(-a b^2 ...)) and it wins at b_*.
- The mechanism is physical: phase A is preferred by the free walls, phase B by the bulk, and B has the smaller mass. Small free boxes sit in A. The crossover scale b_* = 3 DD/DF is as large as one likes. On tori the same direct sum does no harm: no wall term reweights the sectors, the stable phase wins at every size, and Theorem S holds. So the free-wall engine trades the flux sectors of the torus seed for a new failure mode: wall-induced phase selection. The doubling hypothesis is exactly the statement that excludes it between b and 2b.
- Every sufficient condition fails in 2P at the crossover, as it must (PROVED by substitution): (WALL-1) fails (b p(a) = n_B bcd F_a(m_B) against g = n_A bcd F_a(m_A)); (WALL-2) fails (delta_e(b) = cd (DD - DF b) for the slab, of the order of the wall area); (H-tau) fails (tau(a, b) is about -b p(a)); (H-W) holds; (CUT-TH) fails in its lower half.
- No finite test at the seed scale detects b_* (the B sector enters S(a_0; b_0^3) only through e^(-a_0 b_0^2 (3 DD - DF b_0))). So in the class the free-wall engine needs one input per scale. This is the precise sense in which the doubling hypothesis is the whole content of the engine, not a lemma on the side.
- Limits of the example. Static oscillators: no relation between the time gap and the decay along the free axes, and the ring built from the same t_X is not symmetric in (a, n). Family T (L 196-200, accepted by C 210-237) has the same limit. ARGUED: replacing each phase by a Neumann scalar of mass m_X (a local reflection-positive model, row 903) keeps (T), (V), (FW2) and gives symmetric rings; the vacuum crossover is unchanged because it only uses E_X. Not written out.

### Step 4. The exact middle term of (JOIN-TH): four forms, and why the integrated form is the target

Notation of Step 3a: M_s, e_s, g_s(a), s in [0, 1]; rho_i(s) = lambda_i(s)/lambda_0(s); S_s(a) = sum_(i>=1) rho_i(s)^a. E(a; B) := g(a; B|B) - 2 g(a; B) = g_1(a) - g_0(a), the join excess.

4.1 Spectral form (PROVED; for simple eigenvalues, else read it in the sense of traces). d g_s/ds = a sum_(i>=1) rho_i^a (eps_i' - eps_0')/(1 + S_s(a)), eps_i = log lambda_i(s). So E(a; B) is the thermal average of the shift of the excitation energies m_i(s) = eps_0 - eps_i along the path: d g_s/ds = -a <m'>_(a; s). (JOIN-TH) says: when the cut is closed, the excitation energies come down by at most about kappa/a, in the thermal mean.

4.2 The first-order term vanishes at s = 0 (PROVED). At s = 0 every cut plaquette holds a Haar crossing link that nothing else sees. So <X_cut>_(a; 0) = 0 and <x_cut>_(vac; 0) = 0, and d g_s/ds = 0 at s = 0. The join excess starts at second order in s.

4.3 Flux form (PROVED from the READ convolution formula, L 96 and C 119-126). In the crossed channel let phi_b := B^(1/2) R^(b-1) v on the slice (P: a; F: c, d). The cut is one transfer step with couplings s beta: W_s = <phi_b, K_s phi_b>, K_s = (gauge projection)(tensor over slice links of the convolution k_(s beta)). k_t acts on the spin-j isotypic space as c_j(t) = 2 I_(2j+1)(t)/t. With P_J the projection on the spin assignment J = (j_l) to the slice links:
  W_s(a; B|B) = sum_J c_J(s beta) w_J(a; B),  c_J = prod_l c_(j_l),  w_J = |P_J phi_b|^2 >= 0,  w_0 = W(a; B)^2.
So pi_a(J) := c_J(beta) w_J/W(a; B|B) is a probability on the flux configurations of the cut, and exp(-F_join(a; B)) = pi_a(J = 0): the probability that no flux crosses the cut. J_0(B) is the rate of the same event in infinite time. (JOIN-TH) reads: -log pi_a(no flux) exceeds a times its infinite-time rate by at most kappa g(a; B).

4.4 Sum rule at s = 1 (PROVED). beta d g(a; B)/d beta = beta [<X_tot>_a - a <x_tot>_vac] = sum over all plaquettes of the box of the thermal shift of beta x_p. So the s-derivatives at s = 1 of all parallel cut positions, plus the thermal shifts of the in-slice plaquettes, add up to the beta-derivative of the thermal log-sum.
ARGUED consequence. In a massive phase g is about (volume) e^(-a m(beta)) and beta dg/d beta is about a beta |m'(beta)| g. One cut layer of the box of side 2b carries about 1/(4b) of it. So d g_s/ds at s = 1 is about (a/4b) beta |m'| g, of order g when a = b/2 and the lattice mass runs fast. But E(a; B) itself is much smaller: a layer at coupling s < 1 is a barrier, and the shift saturates when the barrier is opaque for thermal momenta, 1 - s of order 1/(beta |m'| sqrt(a m)). ARGUED size for a point particle and a hard wall: |E(a; B)|/g is of order sqrt(a/m)/b, at most 1/sqrt(2 m b) on a <= b/2.
Reading. A differential (Gronwall) form of the target, d g_s/ds <= kappa g_s for all s, is a valid sufficient condition (it gives k = 2 e^kappa). It is lossy by the factor beta |m'| sqrt(a m)/4. The integrated form (JOIN-TH) is the target.

4.5 Sign (PROVED at fixed sizes, small beta, from C 478-485). g(a, b) = n_s(b) u^(4a) (1 + O(u^2)) with n_s(2b) - 2 n_s(b) = (c-1) d + c (d-1) > 0. So E(a; B) > 0 for the Wilson weight at small beta: the free wall removes thermal weight (the Dirichlet sign), and k = 2 is not available; k = 2 + 1/(b-1) is, at leading order. For the Neumann scalar E <= 0 (C 196-198). No sign is structural.

4.6 The trivial bounds (PROVED). 0 <= F_join <= beta a N_x and 0 <= a J_0 <= beta a N_x give |E(a; B)| <= beta a N_x. Extensive in the cut. Every operator comparison between M_1 and M_0 that I tried (domination M_1 >= kappa_x M_0 with kappa_x = c_0^(links) e^(-beta N_sp); eigenvalue monotonicity of K^(1/2) B K^(1/2) in B and of B^(1/2) K B^(1/2) in K; Araki-Lieb-Thirring for Tr (B^(1/2) K B^(1/2))^a) loses the same extensive factor, because the vacuum energy itself moves by J_0 and the target is a ratio. Recorded as failed routes.

### Step 5. Task 2, attack A: reflection positivity in time and across the cut. What each tool gives, and the 2P test

5.1 Time direction: Hoelder for mixed patterns (PROVED). For sigma in {0, 1}^a let Z(sigma) := Tr prod_t M_(sigma_t). It is the partition function of B|B with the cut open exactly on the time steps with sigma_t = 1 (the space-like cut plaquettes between two steps get the coupling (sigma_t + sigma_(t+1)) beta/2). The M_s are positive, so by Hoelder's inequality for Schatten norms
  Z(sigma) <= W(a; B|B)^(|sigma|/a) W(a; B)^(2 (a - |sigma|)/a).
Equivalently Z(sigma)/W(a; B|B) <= exp(-(a - |sigma|) F_join(a; B)/a): closing the cut on a - |sigma| time steps costs at least that share of the joining free energy. This is the chessboard estimate in time. It bounds mixed patterns by pure ones. (JOIN-TH) needs the pure joined trace bounded ABOVE, relative to its own vacuum. Hoelder never does that.
5.2 Time direction: the window (PROVED). Let Omega_0 be the vacuum of M_0 (two separate boxes), o := <Omega_0, Omega_1> the overlap with the vacuum of the joined box, and F_win(a) := log(<Omega_0, M_1^a Omega_0>/lambda_0(0)^a) the free energy of opening the cut during a window of a steps in the vacuum. Then F_win is super-additive in a (Chebyshev's inequality for the spectral measure of Omega_0), F_win(a) <= a J_0, and a J_0 - F_win(a) increases to -log o^2. So the variational bound lambda_0(1)^a >= <Omega_0, M_1^a Omega_0> turns E(a; B) <= F_join(a) - F_win(a) into E <= E + (a J_0 - F_win(a)): true and empty. The defect is the corner free energy -log o^2. ARGUED orders of magnitude: it is of the order of the cut area c d in one phase. (In a two-phase model -log o^2 is of the order of the volume b c d: the two vacua are different phases. So a corner law for o^2 excludes the 2P mechanism. It does not give (JOIN-TH): the overlap sees only states that the cut emits.)
5.3 Across the cut and across parallel planes (READ L 82-91, C 98-115, and 4.3). Positivity of R gives the vector form, convexity in b, FW6, and Cauchy-Schwarz between cut words. Every such inequality is homogeneous in the wall count and has a non-negative zero-temperature defect (L 85-90). A thermal excess is (inequality at a) minus (a times its infinite-time rate). The difference of an inequality and its rate is not an inequality. Only identities that hold state by state survive: the squaring S(2a) <= S(a)^2 and trace sub-multiplicativity in a periodic direction. For a free direction the crossed channel is a vector, and there is no squaring.
5.4 The 2P test (PROVED for the first sentence; ARGUED for the second). Any argument that uses only (T), (V), (FW2), the bounded defect and the symmetry of the free family cannot prove (JOIN-TH), (H-DBL) or any of (S1)-(S4): family 2P has all of them and violates the conclusion (Theorem 2P). Arguments that also use mixed patterns, the s-family or rings are not covered by Theorem 2P as written; but a lattice gas of two phase labels with nearest-neighbour interface cost in space, frozen in time, with static oscillators on each site, is a local model, reflection positive in the space directions, with a positive diagonal time transfer, and it has the s-family, the mixed patterns and the wall-induced crossover (construction sketched, not written out).
5.5 Verdict of attack A. Not proved. Reflection positivity in the periodic time direction gives 5.1 and 5.2 and no bound on the join excess. The route does not stop at a missing estimate; it stops at a missing HYPOTHESIS: something that separates the Wilson weight from a two-phase system whose walls prefer the heavier phase.

### Step 6. Task 2, attack B: correlation inequalities, the closure lemma, and the reduction to one statement

6.1 Lemma DS (the class is closed under direct sums with wall costs; PROVED). Let W_A, W_B satisfy (T), (V), symmetry. Let D_A, D_B >= log 2. Then W := e^(-a D_A (bc + cd + bd)) W_A + e^(-a D_B (bc + cd + bd)) W_B satisfies (T), (V), symmetry, hence (FW2).
Proof. (T): direct sum of the two transfer operators, each multiplied by the positive number e^(-D_X (bc + cd + bd)). (V) in b: e^(-a D_X (bc + bd)) is an exponential in b and goes into the eigenvalues; e^(-a D_X cd) <= 1/2 multiplies the weights; the total weight is at most 1. Symmetry is clear. QED
Consequence. A property that survives Lemma DS cannot prove the doubling bound: by Theorem 2P the sum can change vacuum between b and 2b. Positivity of both channels, integrality, super-multiplicativity and every Cauchy-Schwarz or Hoelder inequality of the pure free family survive it.

6.2 Correlation inequalities for the cut layer.
- SU(2): I know no Griffiths or Ginibre type inequality for the Wilson plaquette field of a non-abelian group (not searched in this lane; a literature row could confirm). The positivity that exists is the character positivity of 4.3. It gives: W_s has non-negative Taylor coefficients in s, and <X_cut>_(a; s) >= 0 (PROVED: d/ds of a series with non-negative coefficients). The same holds in the vacuum. The join excess is the difference of the two. No sign.
- U(1), Z_2: Ginibre's inequality (recalled, not re-read here) makes <X_cut>_(a; s) and <x_cut>_(vac; s) non-decreasing in s. Again the excess is a difference. ARGUED test (the U(1) transition is reported near beta = 1.011 and weakly first order: web search of 2026-11-13, summaries only, pointers arXiv hep-lat/0011058 and hep-lat/0210010, primary texts not read): compact U(1) just above its confinement transition, and Z_2 just above its first-order point, satisfy all these inequalities; their free walls prefer the disordered phase; so their small free boxes are confined and cold while their large boxes are not in that phase. For U(1) the large boxes have a photon, so the doubling bound MUST fail at the crossover scale. Hence no argument that holds for U(1) at every coupling can prove (JOIN-TH). This is a fact test for the doubling half; it is sharper than the Coulomb-phase test (which the seed already meets).

6.3 An exact inequality that isolates the zero-temperature face (PROVED). From (DBL-ID2), tau(a, 2b) <= gamma(2b, a) <= gamma(b, a) and tau(a, b) = gamma(b, a) - a delta_e(b):
  E(a; B) <= [p(a) - c(a)] + 2 a delta_e(b) - gamma(b, a) <= [p(a) - c(a)] + 2 a delta_e(b).
So (H-W) p - c <= C_w g and (WALL-2) a delta_e(b) <= C_2 g give (JOIN-TH_kappa) with kappa = C_w + 2 C_2. In family 2P below the crossover, (H-W) holds (p = c in the B phase) and (WALL-2) alone fails: delta_e(b) = (E_A - E_B)(b, c, d) is the part of the vacuum energy of the box that has not reached its asymptotic affine form. So the hypothesis that the class lacks has a zero-temperature face: the vacuum energy of the free box at side b is converged up to thermally small terms. (It is sufficient, not necessary: L 120-131 has a wall source with a delta_e large and E unchanged.)

6.4 The reduction (answer to Task 2). For Wilson SU(2) at order-one coupling the doubling hypothesis is reduced to the single statement (JOIN-TH_kappa) on cold boxes (Step 3b). It is not proved. I have no proof of any of its sufficient pairs either: (H-W)+(WALL-2) (6.3), (WALL-1)+(WALL-2), (WALL-1)+(CORNER), (H-W)+(H-tau).
Exactly where it stops. (1) The left side of (JOIN-TH) is the thermal mean of the shift of the excitation energies when one layer is closed (4.1). Every available inequality bounds it by the number of plaquettes of the layer (4.6). (2) No inequality of the lane has the right form: all have a positive zero-temperature defect, and a thermal excess is not the excess of an inequality (5.3). (3) A proof must use a property that fails under Lemma DS: a quantitative statement that the free boxes of side b and 2b are in one phase. For the Wilson weight at one order-one coupling I know no such statement that is proved, and no soft source for one: absence of a bulk transition on the Wilson axis is itself not proved. ARGUED, from a web search of 2026-11-13 (result summaries only; no primary text was read, so this is a pointer, not a claim about those papers): the mixed fundamental-adjoint SU(2) action of Bhanot and Creutz is reported to have first-order bulk lines that end at a point inside the coupling plane, short of the Wilson axis; its location and nature are disputed (pointers: arXiv hep-lat/9610022, hep-lat/0404015). On the weak side of a first-order line of this kind the free walls should prefer the strong-coupling phase, which has the larger lattice mass. That is the sign pattern of Theorem 2P. So for a neighbouring action the doubling bound may fail at a finite scale, and a proof for the Wilson action must feel the difference.
What would count as progress (not done here): a proof of (JOIN-TH) from the gap of the two halves PLUS one explicit single-phase input (for instance (WALL-2) at the same level, or a corner law for the overlap o of 5.2, with a proof that it controls the join excess). In the class neither input follows from the seed.

6.5 Constants (PROVED arithmetic). The join route has k = 2 + kappa. The ring route has k = 4 (1 + theta')/(1 - theta) >= 4. Seed thresholds 1/(4 k^6): kappa = 0 gives 3.9e-3; kappa = 0.77 (Dirichlet scalar, GUIDE L 271-275) gives 5.5e-4; kappa = 1 gives 3.4e-4; the ring route gives at most 6.1e-5; Theorem S on tori has 1/5041 = 2.0e-4. ARGUED size in one massive phase: kappa of order 1/sqrt(m b) (4.4), so k tends to 2 along the ladder.

### Step 7. Task 3: the engine with target (JOIN-TH) against U(1), Z_2, frozen Q_8 and 2T

"Engine" = Theorem C' with (H-SEED) and (JOIN-TH_kappa) on cold boxes. "Passes" = it does not prove a false gap. Leading orders below are ARGUED (low-temperature or Gaussian counting, no remainder bound).

| Model | Seed on free cubes | (JOIN-TH) | Engine conclusion | (CUT-TH), even ring |
|---|---|---|---|---|
| U(1), deep Coulomb | FAILS: a photon of energy about pi/b at a <= b/2 gives g of order b^3/a^3 >= 8 (GUIDE, L 208) | holds at the Gaussian level with kappa near 0 (Maxwell with natural walls, GUIDE and ARGUED at L 207; never needed: the boxes are not cold) | none. Correct: no gap. | not needed |
| U(1), just above its transition | may HOLD on boxes below the crossover scale b_* (walls prefer the confined phase) | MUST FAIL at the level that contains b_* (6.2) | none beyond b_*. Correct. | fails there too |
| U(1), small beta | holds (confined) | expected, kappa = O(1/b) at leading order (4.5 with activity I_1/I_0) | gap on free cubes: TRUE | plausible |
| Z_2, frozen | holds | holds at leading order with kappa < 0 | gap on free cubes: TRUE | not excluded (one even flat class) |
| Z_2, just above its first-order point | may hold below b_* | can fail at b_* if the bulk phase is lighter; holds there if it is heavier | conditional, never false | fails |
| Q_8, frozen | holds | holds at leading order with kappa < 0 | gap on free cubes: TRUE | FAILS: g_P^ev -> log 4 (C 312-327) |
| 2T, frozen | holds | holds at leading order with kappa < 0 | gap on free cubes: TRUE | FAILS: g_P^ev -> log 4 (below) |
| family 2P | holds | FAILS at b_* (Theorem 2P) | none beyond b_*. Correct. | fails in its lower half |

Frozen finite groups, leading order (ARGUED). The free box has one flat class (FW1; C 312-325). The lightest excitations of the time transfer are single links on the EDGES of the space box: an edge link lies in 2 space plaquettes, a face link in 3, a bulk link in 4. So g(a; B) is about (number of edge links) x (number of non-trivial classes, weighted) x e^(-2 a beta Delta) at large beta, Delta the smallest plaquette cost. The number of edge links of (b, c, d) is 4 (b + c + d) - 12. Joining two boxes removes the eight edges round the joined faces: E(a; B) < 0. So kappa < 0, k = 2, and the thermal sums are wall-dominated ((WALL-1) holds trivially, p is much smaller than c). The same count holds for Z_2, Q_8 and 2T.
2T and the even ring (PROVED by counting). 2T = SL(2, 3) has 7 classes of sizes 1, 1, 6, 4, 4, 4, 4. Multiplication by -1 swaps {1} and {-1}, fixes the class of the six elements of order 4, and swaps the two classes of order 6 with the two classes of order 3. So the class functions even under the central flip have dimension 4 (the four characters of 2T/{+-1} = A_4), and the odd ones dimension 3. The frozen ring has g_P^ev -> log 4 and g -> 0, as for Q_8.

Answers.
- The engine with target (JOIN-TH) passes U(1): in the Coulomb phase the seed fails at every ladder shape; near the transition the doubling fails at the crossover. It proves nothing false.
- It passes Z_2, frozen Q_8 and frozen 2T in the other sense: it applies to them and its conclusion (a gap on free cubes) is true for them. It does not separate SU(2) from these groups and it must not: the conclusion is a glue statement. So a proof of (JOIN-TH) need not use anything that Q_8 or 2T lack. It must use something that family 2P lacks and that U(1) lacks just above its transition.
- None of this lane's statements is a worst-case single-site, vertex-block or background-uniform bound, and (AN1) is not used: the thermal sums are traces over the free-box states, with no conditioning.
- (CUT-TH) is different: its even form fails frozen Q_8 and 2T, its full form fails frozen Z_2. It is a legitimate ROUTE for SU(2) only with a flux input (no light even holonomy state on the ring), and that input is not needed by the engine.

