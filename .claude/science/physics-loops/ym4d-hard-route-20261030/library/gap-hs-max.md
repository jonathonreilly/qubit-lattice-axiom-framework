# FINISH row 860, gap-hs-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone: /Users/jonreilly/ym4d-lead/clone, branch claude/ym4d-hard-route, commit 2b6acd1732dde4e18293f0fe0e2814edbca36da3 (pulled 2026-11-12, already up to date).
Author: Claude Fable 5.2 (max effort), FINISH row 860. No subagents. No repository file edited.
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.

## Target (as given in the brief; exact text of (HS), (LS) is quoted in Step 1 below once read)

- (HS): the high-spin rarity bound of D/library/gap-q8test-opus.md (row 843), lines 270-320.
- (LS): the low-spin odd-sector bound of the same file.
- Decide first whether (HS) is true at order one, and what the right notion of rarity is.
- Then: does the low-spin charged filter (Theorem 3.4, Corollary 3.7, Section 4 of that file) plus (HS) force the odd-sector bound that the consumer (E17) needs?

## Plan (at most eight steps; one step per response; each appended before the next)

1. READ: gap-q8test-opus.md lines 270-320, Theorem 3.4, Corollary 3.7, Section 4. Quote (HS), (LS), the filter, and the consumer (E17) exactly.
2. READ: the first-passage action (gap-finishline-opus.md lines 110-160, (SEED-FP)) and the fact-test rows (786, 838, 839, 843, 845) as far as they bound this target.
3. DECIDE: is (HS) true at order one? Compute the spin law of a plaquette / link in the one-slice law by hand (character expansion). State the right notion of rarity.
4. PROVE or REFUTE (HS): the strongest form reachable by hand (chessboard / reflection positivity in the one-slice law, or character-expansion counting), with explicit constants. GUIDE run only if it can refute.
5. Replacement statement: what the filter actually needs, if (HS) is false or the wrong target.
6. ATTACK (LS): does filter + (HS or replacement) force the odd-sector bound of (E17)? Can spin-1/2 flux lines avoid the filter?
7. Fact tests: U(1) Coulomb must fail; Q_8 and 2T must fail where they would pass; compare with the 2/3, 0.775, 1.0109 caps and (AN1).
8. Summary table (PROVED / READ / ARGUED / GUIDE / OPEN) and the RESULT line.

## Log

### Step 1 (READ). The target, quoted. Q = D/library/gap-q8test-opus.md (row 843, unchecked).

- READ Q:249. Transfer: L_m = z^|E| K^(1/2) B_m K^(1/2) on the gauge-invariant space H = L^2(SU(2)^E)^(SU(2)^V); K = (x)_e C_beta; C_beta = Sum_j r_j Pi_j; r_j = I_(2j+1)(beta)/I_1(beta); Z^m = Tr L_m^t; Z^m - Z^(m+v) = 2 Tr(P_- L_m^t); P_- = (1 - Theta_omega)/2. (Q cites EX:95-152; I read EX in Step 2.)
- READ Q:261-267 (4.1 (c)). Pi = (x)_e Pi_(S_e) commutes with K, the gauge projection and Theta_omega. For Q = P_- Pi: 0 <= Tr(Q L_m^t) = ||L_m^(t/2) Q||_HS^2, and the parts sum to Tr(P_- L_m^t). "The same holds in the even sector."
- READ Q:285-291, (HS), OPEN there. "There are an order-one interval I reaching above 2.15 (for example [2.15, 2.5]), a density eta(beta) < 1 and c > 0 such that, uniformly in the admissible tori (a, a, c, d), the twists m and beta in I, under the nonnegative one-slice law of 4.1 (c) in the even sector, Tr(P_+ Pi_{N_(>=2)(0) >= eta|E|} L_m^t)/Tr(P_+ L_m^t) <= e^(-c|E|), where N_(>=2)(0) counts the spatial edges at time 0 whose spin is at least 2 (...for 2T use spin at least 3)."
- READ Q:293. Q says the naive one-edge bound fails: Tr(Pi_e K X) <= r_(5/2) Tr((Pi_e (x) K_rest) X), and "the right side carries no kinetic factor at e".
- READ Q:295, (LS), OPEN there. "On the low-spin part (fewer than eta|E| high-spin edges at time 0) the odd-sector fraction must satisfy the consumer bound (E17), Tr(P_- Pi_low L_m^t) <= C a^p eta_*^(a/2) Tr(L_m^t). (LS) is where the spin-1/2 flux line of 4.3 lives, so it is as hard as the original problem unless the low-spin restriction gives a usable finite-spin structure."
- READ Q:191-207 (Theorem 3.4) and Q:219 (Corollary 3.7). The filter: r_(5/2)(beta) <= M(beta) < r^2T_V(beta) <= r^Q8_V(beta) and M(beta) < I_1/I_0 for every beta > 0; on V (x) Sym^4 V the SU(2) norm is r_(3/2), also below all three.
- READ Q:275 (4.2 (c)). Plaquette character law w_j(beta) = (2/beta) d_j^2 I_(2j+1)(beta) e^(-beta); "a single-plaquette count, not the law of 4.1 (c)".
- READ Q:279 (4.3). (G20)-(G21): a flat wrapping plane of spin-1/2 plaquettes contributes 2 r_(1/2)^A to Z^m - Z^(m+v) with no edge above spin 1/2. So exposure of the filter is not mandatory term by term.
- READ Q:336. Q's own note: "(HS)... its G-analogue fails at every beta, also where G confines, so (HS) passes the binding test cheaply and does not by itself locate the confining mechanism; that is left to (LS)."

Reading of the statement (mine). (HS) asks only for SOME eta < 1. It is a large-deviation statement about the count of high-spin edges in one slice. It does not say the density of high-spin edges is small.

First idea, recorded so it is not lost (to be proved carefully in Steps 3-4). An electric-energy bound. On the range of the projection {N_(>=j0) >= eta|E|} one has K <= r_(j0)^(eta|E|), so Pi <= r_(j0)^(eta|E|) K^(-1). And K^(-1/2) L^t K^(-1/2) = z^(2|E|) B K^(1/2) L^(t-2) K^(1/2) B, bounded by (sup B) times L^(t-1) in trace. So the ratio is at most r_(j0)^(eta|E|) (sup B_m / lambda_+) times a t-correction, and sup B/lambda_+ <= e^(beta|P_s|) by Jensen (trial vector 1). With |P_s| = |E| the bound is (r_(j0)^eta e^beta)^|E|. At beta = 2.3: r_2 = I_5/I_1 = 0.00993 and e^beta = 9.97, product 0.099 < 1 with eta = 1; any eta > beta/|log r_2| = 0.499 works. This is group-blind (it holds for U(1) too). So (HS) looks TRUE and soft. Check the exact definitions of B_m, the tori and t in EX before claiming it.

### Step 2a (READ). The transfer and the consumer, from EX = D/library/gap-expose-astra.md.

- READ EX:88-103, (E1). Time direction r, period t, spatial three-torus Q with edge set E and plaquette set P. "Every period is at least three." z = Int e^(beta tr g/2) dg. K = (x)_e C_beta, C_beta = Sum_j r_j Pi_j. B_m(U) = exp(beta Sum_(p in P) eta_(m,p) x(U_p)), eta_(m,p) = +-1 a time-independent spatial sign cocycle. L_m = z^|E| K^(1/2) B_m K^(1/2) on H = L^2(SU(2)^E)^(SU(2)^V(Q)). Z^m = Tr L_m^t. L_m is positive, injective, trace class.
- READ EX:113-151, (E2)-(E3). J_e flips the sign of one spatial edge. Theta_omega = Prod_e J_e^(omega_e) for a closed one-cochain omega; it commutes with B_m, K, L_m. Z^(m+v) = Tr(Theta_omega L_m^t); Z^m - Z^(m+v) = 2 Tr(P_- L_m^t).
- READ EX:575-599, (E16)-(E17). p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr L_m^a = (1 - R_m(v_(1i)))/2; Q_F = max over m_2 = 0, i = 3, 4. The time period is t = a. Consumer (FQ): 8 Q_F <= K(a) sqrt(S_ev(a)), Q_F < 1/192. Sufficient: (E17) Q_F <= C a^p eta_*^(a/2), 0 < eta_* < 1. "Neither (E17) nor (FQ) is proved here."
- READ EX:601-617, (E18). e^(-beta|P|) <= B_m <= e^(beta|P|) gives p_(m,i)(t) <= e^(2 beta|P|t) Tr(P_- K^t)/Tr K^t; "an extensive cost"; useless for (E17).

Consequences for my bound (PROVED from these definitions; three lines each).
(i) sup B_m <= e^(beta|P|). (ii) The constant function 1 lies in H, Theta_omega 1 = 1, K^(1/2) 1 = 1 (r_0 = 1). By Jensen, <1, B_m 1> >= exp(beta Sum_p eta_(m,p) Int x(U_p) dU) = 1, because each U_p is Haar distributed (periods >= 3: four distinct links). So lambda_+ := ||L_m P_+|| >= z^|E|. (iii) |P| = |E| = 3|V(Q)| on a three-torus. (iv) Tr_H K <= Tr_(L^2(SU(2)^E)) K = k_beta(1)^|E| = (e^beta/z)^|E|, since k_beta(1) = Sum_j d_j^2 r_j = e^beta/z.

### Step 2b (READ). The finish line and the fact tests. FLN = D/library/gap-finishline-opus.md; FIN = D/FINISH.md (row n at line n + 77 in this clone).

- READ FLN:117-121, (SEED-FP). "There are K_0, a physical size ell ... and a number s_* < 1/5041 such that, for every first-passage datum (K, beta) at g with K >= K_0, S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_*, the thermal sum of the bare Wilson transfer operator of the periodic cube of physical side ell at physical time ell/2." The real object is the bare Wilson measure along first passage (FLN:138), equivalently the total masses of the Sussman-Alpoge effective densities (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Balaban for the effective-action estimates the account uses).
- READ FLN:108-109. The consumer form: (FQ) 8 Q_F <= K(a) sqrt(S_ev), Q_F < 1/192; (E17) "suffices at fixed coupling".
- READ FLN:149. (E17) is a fixed-coupling statement; along the trajectory the constant must be bounded in physical units.
- READ FIN:863 (row 786). (U-tor): for periodic Villain U(1) at every fixed beta >= 2^14 the gauge-invariant Langevin gap on (Z/M)^4 tends to 0. A group-blind proof of a uniform gap is ruled out by a written theorem (unchecked there; check row 794).
- READ FIN:915 (row 838). Q_8 freezes near 1.15, 2T near 2.15, 2I near 5.7 (GUIDE, Hartung et al.). "A tool at the crossover must see spin 2 or 3."
- READ FIN:916 (row 839). Proposition TB2: every background-uniform layer twist bound is false above 4 G_3 = 1.0109 at the flat background (via Frohlich-Simon-Spencer).
- READ FIN:922 (row 845). Theorem AG, the annealed condition (AN); OPEN (SP-ext). Periodic Villain U(1) at beta >= 2^14 fails (AN).
- READ FIN:937 (row 860). This row: "first decide whether (HS) is the right notion of rarity at order one and state the replacement the spin-5/2 filter needs if not."

What these fix for my target. The consumer reads p_(m,i)(a) = Tr(P_- L_m^a)/Tr L_m^a at time period t = a, spatial torus of sides (a, c, d), omega across direction 3 or 4. An exact rewriting I will use (PROVED in Step 6, Proposition P1): 1 - 2 p = E_m[(-1)^(N_h(cut))], the parity of the number of half-integer edges crossing the cut in the one-slice law.

### Step 3 (DECIDE, then PROVED). (HS) is true at order one. It is an electric-energy bound.

Notation. L = L_m, B = B_m, sigma in {+, -}. For a set A of spin assignments (j_e)_(e in E) put Pi_A = Sum_(j in A) (x)_e Pi_(j_e). Pi_A commutes with K, the gauge projection and Theta_omega (READ Q:261). N_(>=j0)(j) = #{e : j_e >= j0}. r_j = I_(2j+1)/I_1 is strictly decreasing in j and r_0 = 1 (READ Q:159, Lemma 3.1 (a)). lambda_+ is the largest eigenvalue of L on P_+ H.

**Theorem HS (PROVED here; not checked by another model).** Let beta > 0, j0 in {1/2, 1, 3/2, ...}, 0 < eta <= 1, t >= 2, any spatial three-torus Q with all periods >= 3, any twist m, any closed omega, sigma in {+, -}. With A = {N_(>=j0) >= eta|E|},

```math
\frac{\operatorname{Tr}(P_\sigma\Pi_A L_m^t)}{\operatorname{Tr}(P_+L_m^t)}\ \le\ \exp\Big(-|E|\Big[\eta\log\frac1{r_{j_0}(\beta)}-\beta-\frac{2\beta-\log z(\beta)}{t-1}\Big]\Big).
```

The bound does not depend on Q, m or omega.

*Proof.* (1) On the range of (x)_e Pi_(j_e) the operator K is the scalar Prod_e r_(j_e). If j is in A this scalar is at most r_(j0)^(eta|E|), because at least eta|E| factors are at most r_(j0) < 1 and the others are at most 1. So P_sigma Pi_A K <= r_(j0)^(eta|E|) P_sigma as commuting positive operators.
(2) Write L^t = K^(1/2) Y K^(1/2) with Y = z^(2|E|) B K^(1/2) L^(t-2) K^(1/2) B. Y is positive and trace class (for t = 2, Y = z^(2|E|) B K B). Since P_sigma Pi_A commutes with K^(1/2), Tr(P_sigma Pi_A L^t) = Tr(P_sigma Pi_A K Y) = Tr(Y^(1/2) P_sigma Pi_A K Y^(1/2)) <= r_(j0)^(eta|E|) Tr(P_sigma Y).
(3) P_sigma commutes with B, K and L (READ EX:135-136). By cyclicity Tr(P_sigma Y) = z^(2|E|) Tr(P_sigma L^((t-2)/2) K^(1/2) B^2 K^(1/2) L^((t-2)/2)). B is a positive multiplier with B <= e^(beta|P|), so B^2 <= e^(beta|P|) B and z^|E| K^(1/2) B^2 K^(1/2) <= e^(beta|P|) L. Hence Tr(P_sigma Y) <= z^|E| e^(beta|P|) Tr(P_sigma L^(t-1)).
(4) Tr(P_- L^s) <= Tr(P_+ L^s) for every integer s >= 1: the difference is Tr(Theta_omega L^s) = z^(s|E|) Tr(Theta_omega (KB)^s), an integral of a pointwise positive kernel (it is the twisted partition function Z^(m+v) at period s).
(5) Let f(s) = Tr(P_+ L^s) = Sum_i mu_i^s over the eigenvalues of L on P_+ H. Holder with exponents (t-1)/(t-2) and t-1 gives f(t-1) <= f(t)^((t-2)/(t-1)) f(1)^(1/(t-1)). With f(t) >= lambda_+^t: f(t-1)/f(t) <= lambda_+^(-1) (f(1)/lambda_+)^(1/(t-1)).
(6) lambda_+ >= z^|E| (Step 2a (ii): trial vector 1 and Jensen). f(1) <= Tr_H L <= z^|E| e^(beta|P|) Tr_H K <= z^|E| e^(beta|P|) (e^beta/z)^|E| (Step 2a (iv)).
(7) Multiply (2), (3), (4), (5), (6) and use |P| = |E|: the ratio is at most [r_(j0)^eta e^beta (e^(2 beta)/z)^(1/(t-1))]^|E|. QED

**Corollary HS-1 (the statement (HS) of Q:285, PROVED, with constants).** Use the majorant r_2(beta) <= (beta/2)^4/120 ((G3), READ Q:178). Let I = [2.15, 2.5] and t = a >= 9. Then for every beta in I, every admissible torus and twist, and both sectors,

Tr(P_sigma Pi_{N_(>=2)(0) >= eta|E|} L_m^t) <= e^(-c|E|) Tr(P_+ L_m^t), c = 3.895 eta - 3.125,

which is positive for eta > 0.803 (for example eta = 0.9, c = 0.38). Arithmetic: log(120/1.25^4) = log 49.15 > 3.895; beta <= 2.5; (2 beta - log z)/(t-1) <= 5/8. As t -> infinity the condition is eta > beta/log(1/r_2(beta)); with GUIDE decimals r_2(2.3) = 0.00993 this is eta > 0.499, and r_2(2.5) = 0.01305 gives eta > 0.576.

**Corollary HS-2 (range, PROVED).** In the limit t -> infinity the bound is [r_(j0)(beta)^eta e^beta]^|E|. For j0 = 2 it is nontrivial for some eta < 1 exactly when r_2(beta) e^beta < 1. This holds when beta^4 e^beta < 1920, in particular for all beta <= 3 (81 x 20.09 = 1627.3 < 1920; the left side is increasing). For j0 = 3 (the 2T variant of Q:291) use r_3 <= (beta/2)^6/5040: the condition beta^6 e^beta < 322560 holds for all beta <= 4 (4096 x 54.6 = 223642 < 322560).

**Decision.** (HS) as stated is TRUE on an order-one interval reaching above 2.15, uniformly in the tori and twists, and in both parity sectors. The proof is soft. It uses one number of SU(2), r_2(beta) < e^(-beta), and nothing else: not the filter at spin 5/2, not non-commutativity, not the vacuum. It beats a volume-order normalization cost e^(beta|P|) with a volume-order event. Q:293's one-edge attempt failed because one edge cannot pay that cost; eta|E| edges can.

### Step 4 (PROVED). The right notion of rarity: the one-slice law is doubly suppressed. The plaquette law w_j is the wrong law.

Setting. mu = mu_(m,t) is the Wilson measure on Q x Z/t with twist m (weight Prod_p e^(beta eta_p x(U_p))). For a spatial edge e, p(e) is the timelike plaquette over e between times 0 and 1. P_m(.) = Tr(Pi_(.) L_m^t)/Tr(L_m^t) is the one-slice law (nonnegative, READ Q:261-267).

**Lemma OS (the one-slice law in Lagrangian form; PROVED).** For S a set of edges and spins (j_e)_(e in S),

P_m(j_e = j_e for all e in S) = E_mu[ Prod_(e in S) d_(j_e) r_(j_e)(beta) chi_(j_e)(U_p(e)) / k_beta(U_p(e)) ].

*Proof.* Tr_H(Pi L^t) = z^(t|E|) Tr_H(Pi K B (KB)^(t-1)) by cyclicity. On L^2(SU(2)^E) the kernel of Pi_(j_S) K is Prod_(e in S) d_j r_j chi_j(U_e V_e^(-1)) Prod_(e not in S) k_beta(U_e V_e^(-1)), since C_beta Pi_j is convolution by d_j r_j chi_j. The gauge projection supplies the temporal links, which turn U_e V_e^(-1) into the plaquette holonomy. So the trace is the Wilson integral with k_beta replaced by d_j r_j chi_j on the plaquettes p(e), e in S. QED

Three exact consequences (PROVED).
(a) Sum_j d_j r_j chi_j = k_beta, so the weights sum to 1.
(b) Half-integer density: P_m(j_e half-integer) = (1 - E_mu[e^(-2 beta x(U_p(e)))])/2, because Sum over half-integer j of d_j r_j chi_j(g) = (k_beta(g) - k_beta(-g))/2.
(c) One edge: rho_j := P_m(j_e = j) = rho_0 d_j r_j(beta) E_nu[chi_j(U_p)], where nu is mu with the weight of the one plaquette p = p(e) deleted, and rho_0 = Z_(without p)/Z.

So the density of spin j is the kinetic eigenvalue r_j(beta) times the j-th character coefficient of the environment of p. The plaquette law w_j = d_j^2 r_j/k_beta(1) of Q:275 is the special case where the environment pins U_p at 1 (E_nu chi_j = d_j). That is a frozen plaquette. It is the law of a frozen finite-group vacuum, not of SU(2) at beta = 2.3.

**Lemma DS (double suppression; PROVED here, not checked).** Let all periods be >= 3. Let S be a set of spatial edges, no two on a common spatial plaquette. Then for all spins (j_e)_(e in S),

P_m(j_e = j_e for all e in S) <= P_m(j_e = 0 for all e in S) x Prod_(e in S) d_(j_e)^2 r_(j_e)(beta) r_(j_e)(5 beta).

*Proof.* Let nu_S be mu with the weights of p(e), e in S, deleted. By Lemma OS the left side is (Z_(without S)/Z) Prod d_j r_j(beta) E_(nu_S)[Prod chi_(j_e)(U_p(e))], and Z_(without S)/Z is the probability of the all-zero assignment on S. Condition on every link except the time-0 links l_e, e in S. No plaquette contains two of these links (a timelike plaquette contains one time-0 spatial link). So under nu_S they are conditionally independent, and l_e has density proportional to exp(beta Sum_(i=1..5) eta_i x(U S_i)), where S_1..S_5 are the staples of its five remaining plaquettes. SU(2) is the unit quaternions and x(U A) is real-linear in the quaternion A, so Sum_i eta_i S_i = rho W with W in SU(2), 0 <= rho <= 5, and the density is k_(beta rho)(U W). Now U_p(e) = U S_p up to cyclic order, and Int k_(b)(g) chi_j(g h) dg = r_j(b) chi_j(h) (Schur; this is the eigenvalue r_j of C_b). So the conditional mean of chi_j(U_p(e)) is r_j(beta rho) chi_j(W^(-1) S_p), of absolute value at most d_j r_j(5 beta), because r_j is increasing in the coupling (READ Q:169, Lemma 3.2) and r_j(0) = 0 for j > 0. Multiply over e in S. QED

**Corollary DS-1 (one-edge densities, hand majorants, PROVED).** For beta <= 2.5: P_m(j_e >= 2) <= tau_2 := Sum_(j >= 2) d_j^2 r_j(beta) r_j(5 beta) <= 0.275, and P_m(j_e half-integer and >= 5/2) <= 0.041.
Arithmetic. r_j(2.5) <= 1.25^(2j)/(2j+1)!: 0.020345, 0.0042386, 0.00075689, 0.00011826, 0.000016426 for j = 2, 5/2, 3, 7/2, 4; Sum_(j>=2) d_j^2 x these <= 0.50863 + 0.15259 + 0.03709 + 0.00757 + 0.00133 + 0.00025 = 0.70746. r_j(12.5) <= r_2(12.5) <= U_1 U_2 U_3 U_4 (12.5) <= 0.8872 x 0.8198 x 0.7585 x 0.7028 < 0.3877 (U_n of Q:159). 0.3877 x 0.70746 < 0.275. For the half-integers >= 5/2: (0.15259 + 0.00757 + 0.00021) x 0.3877 x U_5(12.5) <= 0.16037 x 0.3877 x 0.6525 < 0.041.

**Corollary DS-2 (local product bound and (HS) at every t >= 3; PROVED).** For S plaquette-separated, P_m(j_e >= j0 for all e in S) <= tau_(j0)(beta)^|S|. Colour E by (direction, proper 3-colouring of each of the two transverse coordinates): 27 classes, each plaquette-separated, each of size >= |E|/75 (a cycle of length n >= 3 has a proper 3-colouring with classes >= floor(n/3) >= n/5). If N_(>=j0) >= eta|E| then some class E_i has at least eta|E_i| such edges. A union bound over subsets of E_i gives, for eta >= 1/2,

P_m(N_(>=j0) >= eta|E|) <= 27 exp(-(|E|/75)[eta log(1/tau_(j0)) - H(eta)]), H the binary entropy in nats.

With tau_2 <= 0.275 and eta = 0.8 the bracket is 1.032 - 0.500 > 0.53. This holds for every t >= 3, every beta <= 2.5, every torus and twist; for the P_sigma laws multiply by 2 (Tr L^t <= 2 Tr P_+ L^t, Step 3 (4)).

**The three notions, side by side (beta = 2.3; decimals GUIDE unless a hand bound is cited).**

| Notion | Statement | Spin >= 2 | Half-integer >= 5/2 |
|---|---|---|---|
| plaquette law w_j (Q:275) | frozen-environment law | 6.1% | 1.3% |
| large deviation (Theorem HS) | count >= eta|E| has probability e^(-c|E|) | eta > 0.50 | (spin 5/2: eta > 0.37) |
| one-edge density (Cor. DS-1, PROVED) | rho_j <= rho_0 d_j^2 r_j(beta) r_j(5 beta) | <= 0.275 | <= 0.041 |
| one-edge density, single-plaquette estimate (ARGUED: environment = e^(b x) with b fitted to <x_p> = 0.60, b about 1.1) | rho_j/rho_0 = d_j^2 r_j(2.3) r_j(1.1) | about 1e-4 | about 3e-6 |

The right notion (my answer to the brief's question). High spin is rare in the one-slice law because two small factors multiply: the kinetic eigenvalue r_j(beta) and the environment coefficient E_nu chi_j/d_j <= r_j(5 beta). "Not rare in the plaquette law" (6% at beta = 2.3) is a statement about w_j, which sets the second factor to 1. The estimate in the last row says the true density of spin >= 2 edges is near 1e-4 and of exposed filter edges (odd, spin >= 5/2) near 3e-6. Step 5 measures these (GUIDE).

### Step 5 (GUIDE; decides nothing). The measured one-edge law.

Script: /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane860/scripts/guide860.py (4D SU(2) heat bath, periodic, untwisted; numpy, one thread, under 100 MB). It measures rho_j by Lemma OS with one link integrated exactly: E[chi_j(U Sig) e^(-beta x(U Sig)) | rest] = z(b') r_j(b') chi_j(c)/z(b), b = beta|A|, b' = beta|A - Sig|, c = (A - Sig).Sig/|A - Sig|, A the staple sum, Sig the staple of p. (This identity is the computation in the proof of Lemma DS.)

Smoke test, 4^4, beta = 2.3, 10 configurations: <x_p> = 0.602(3); rho_0 = 0.637(11), rho_(1/2) = 0.327(10), rho_1 = 0.035(1), rho_(3/2) = 0.0012(4), rho_2 and above are below the noise (1e-5 to 1e-4); half-integer density 0.328(10). The weights sum to 1.000000. The full 8^4 runs are appended below when they finish.

**GUIDE results, 8^4, 200 configurations each (200 thermalization sweeps, 3 sweeps apart), output in `guide860.out` beside the script.** Errors are binned standard errors. rho_j is the one-edge one-slice density; w_j is the plaquette law of Q:275; e_j = E_nu[chi_j(U_p)]/d_j is the environment coefficient of Step 4 (c).

| beta | <x_p> | rho_0 | rho_(1/2) | rho_1 | rho_(3/2) | rho_2 | rho_(5/2) | half-integer density |
|---|---|---|---|---|---|---|---|---|
| 2.15 | 0.5519(4) | 0.7378(9) | 0.2452(9) | 0.01660(9) | 3.8(1)e-4 | 2(2)e-6 | below 3e-7 (noise) | 0.2456(9) |
| 2.3 | 0.6024(5) | 0.6373(12) | 0.3267(9) | 0.0347(3) | 1.26(3)e-3 | 2.1(3)e-5 | below 6e-7 (noise) | 0.3280(9) |
| 2.5 | 0.6527(2) | 0.5377(5) | 0.3940(3) | 0.0645(2) | 3.72(3)e-3 | 9.1(4)e-5 | 1.3(4)e-6 | 0.3977(3) |

| beta | w_(>=2) | measured rho_(>=2) | w(half-integer >= 5/2) | measured | e_(1/2) | e_1 | e_(3/2) | e_2 |
|---|---|---|---|---|---|---|---|---|
| 2.3 | 6.1e-2 | 2.1e-5 | 1.3e-2 | below 6e-7 | 0.267 | 0.036 | 0.0028 | 1.3e-4 |
| 2.5 | 7.4e-2 | 9.2e-5 | 1.6e-2 | 1.3e-6 | 0.361 | 0.071 | 0.0079 | 5.2e-4 |

Readings (GUIDE).
1. At beta = 2.3 the one-slice law sits on spins 0, 1/2, 1 with total weight 0.9987. Spin >= 2 has density 2e-5, not 6%. The filter-exposed edges (half-integer, spin >= 5/2) have density below 6e-7, not 1%. Q's sentence "exposure density about 1% per plaquette at the crossover" (Q:344, the RESULT line, from the w_j count of Q:275) overstates the exposure by more than four orders of magnitude.
2. The environment coefficient of spin 1/2 is 0.27 at beta = 2.3 and 0.36 at 2.5. The proved bound of Lemma DS is r_(1/2)(5 beta) = 0.87. A frozen vacuum has 1.
3. Half-integer edges have density 0.33 at beta = 2.3 and 0.40 at 2.5. This is above the bond-percolation threshold 0.2488 of the cubic lattice (recalled; independent bonds, so only a heuristic comparison). At beta = 2.15 it is 0.246. So in the window the half-integer edges of one slice form a dense, plausibly percolating set. A Peierls count of half-integer winding paths cannot work there.
4. The run is untwisted, 8^4, one seed. It guides; it proves nothing.

### Step 6 (PROVED identities; ARGUED verdict). The attack on (LS): the filter plus (HS) do not force it.

**Proposition P1 (the odd sector is a parity event of the one-slice law; PROVED).** Let cut = supp(omega). J_e acts on the spin-j block of edge e by (-1)^(2j) (READ Q:261), so Theta_omega = (-1)^(N_h(cut)), where N_h(cut) counts the half-integer edges in the cut, and P_- = Pi_{N_h(cut) odd}. Hence, with Lemma OS,

p_m(t) = Tr(P_- L_m^t)/Tr L_m^t = P_m(N_h(cut) odd) = (1/2)(1 - E_mu[exp(-2 beta Sum_(e in cut) x(U_p(e)))]).

The half-integer edges of a slice form a Z_2-cycle C (READ EX:127-131: E_b = 0 unless the boundary of b vanishes). So (E17) says: the omega-component of the class of C in H_1(Q; Z_2) is zero except with probability C a^p eta_*^(a/2).

**Proposition P2 ((LS) is (E17) up to e^(-c|E|); PROVED).** Let Pi_low project on {N_(>=2)(0) < eta|E|} with eta, c as in Corollary HS-1. Then

0 <= Tr(P_- L_m^t) - Tr(P_- Pi_low L_m^t) <= e^(-c|E|) Tr(P_+ L_m^t).

*Proof.* The difference is Tr(P_- Pi_A L^t) with A = {N_(>=2) >= eta|E|}; it is nonnegative (READ Q:263-267) and Theorem HS with sigma = - bounds it. QED
So (LS) holds if and only if (E17) holds, up to a term e^(-c|E|) with |E| = 3 a c d, which is far below C a^p eta_*^(a/2) on large tori. The split (HS)/(LS) removes nothing. "Fewer than eta|E| high-spin edges" with eta near 0.8 is no restriction: the measured count is about 2e-5 |E| (Step 5). The restricted trace is not the trace of a finite-spin model.

**Proposition P3 (Theorem HS and Lemma OS are group-blind; PROVED by the same proofs).** Let G be U(1) with x = cos(theta), z = I_0, r_n = I_n/I_0, or a closed subgroup of SU(2) acting irreducibly on V with x = tr/2 (Q_8, 2T, 2O, 2I). Then E_G x = 0, k^G_beta = e^(beta x)/z_G is positive definite with convolution eigenvalues 0 < r^G_rho <= 1, Tr C^G = k^G(1) = e^beta/z_G, and |P| = |E|. Every step of the proof of Theorem HS holds verbatim. So for every set R of irreducibles, with r_R = max over R of r^G_rho,

Tr(P_sigma Pi_{N_R >= eta|E|} (L^G)^t)/Tr(P_+ (L^G)^t) <= [r_R^eta e^beta (e^(2 beta)/z_G)^(1/(t-1))]^|E|.

Examples. U(1): I_n(beta)/I_0(beta) <= (beta/2)^n/n! <= (e/6)^(3 beta) < e^(-beta) for n >= 3 beta, so charges of size at least 3 beta are rare in the (HS) sense at every beta, in the Coulomb phase too. 2T at beta = 2.3: r_(V') e^beta = 0.095 x 9.97 = 0.95 < 1 (GUIDE decimals), so even V' and V'' edges obey an (HS) bound. Lemma OS is also verbatim for every G. Lemma DS is not: its step "Sum of staples = rho W with W in the group" uses that SU(2) is a sphere. For U(1) the same step works (complex numbers); for a finite group the staple sum is not a multiple of a group element, and at the flat background the environment coefficient is r^G_rho(5 beta), which for Q_8 and 2T is 1 - O(e^(-5 beta/2)) (READ Q:180, Lemma 3.3 (c), at coupling 5 beta): frozen.

**Verdict V1 (ARGUED; the U(1) fact test).** No argument whose inputs are (a) positivity of the one-slice law, (b) upper bounds on the kinetic eigenvalues of the non-trivial irreducibles, (c) rarity of high irreducibles in the sense of Theorem HS or Lemma DS, can prove (LS). Reason: U(1) satisfies (a), (b), (c) in its own irreducibles, by Proposition P3 and by Lemma DS (which holds for U(1)), and U(1) has a Coulomb phase with no gap (READ FIN:863, row 786: periodic Villain U(1) at beta >= 2^14, unchecked there; the classical Coulomb-phase theorems of Guth and of Frohlich-Spencer are recalled, not re-read, and row 786 records that the Wilson-cosine torus statement is not proved in the lane). Size of the coincidence (GUIDE decimals): U(1) at beta = 1.09 has kinetic eigenvalues 0.477, 0.124, 0.022 on charges 1, 2, 3; SU(2) at beta = 2.3 has 0.479, 0.166, 0.045, 0.0099 on spins 1/2, 1, 3/2, 2. The U(1) profile is below the SU(2) profile from the second entry on, and U(1) at 1.09 is believed Coulomb (critical coupling near 1.01, recalled numerics, GUIDE). So even the exact kinetic profile of SU(2) at 2.3, used as an upper bound, cannot decide confinement. The filter of Q's Theorem 3.4 is input (b). Its statement "M(beta) < I_1/I_0" compares SU(2) on V_(5/2) with U(1) on a weight vector of V_(5/2); it is an aliasing statement about U(1) inside SU(2). It is not a property that U(1) gauge theory lacks in its own charges. So the filter does not pass the U(1) test as an input to (LS).

**Verdict V2 (ARGUED, with the GUIDE numbers of Step 5). Can spin-1/2 flux avoid the filter? Yes, and it does not need to try.** In the one-slice law at beta = 2.3 the odd edges are spin 1/2 with density 0.327, spin 3/2 with density 1.3e-3 and spin >= 5/2 with density below 6e-7. The filter eigenvalue r_(5/2) acts on a set of edges of density below 1e-6. Proved form: Corollary DS-1 (density at most 0.041) and Theorem HS with j0 = 5/2 (count at most eta|E|, eta > 0.37, in both sectors). TR's (G20)-(G21) (READ Q:279) is the term-by-term form. No statement about the exposure of the filter can carry (E17): the exposure is all but absent from the measure (GUIDE).

**Where SU(2), 2T and U(1) actually differ in the one-slice law (PROVED formula, ARGUED reading).** By Step 4 (c), rho_j/rho_0 = d_j^2 r_j(beta) e_j with e_j = E_nu[chi_j(U_p)]/d_j.
- Against a frozen finite group. There e_rho is 1 up to O(e^(-5 beta/2)) and the law is w^G. For SU(2), e_j <= r_j(5 beta) < 1 (Lemma DS, PROVED: continuity of the group; 0.87 for spin 1/2 at beta = 2.3), and e_(1/2) = 0.27 measured. So the continuity of SU(2), not the filter, separates its vacuum from a frozen 2T vacuum; on the fundamental the kinetic factors agree to beta^5/7680 (READ Q:241).
- Against U(1). Kinetic profile, double suppression, (HS) and a dense half-integer (odd-charge) set are all shared. The difference must be non-abelian: in U(1) the flux through the cut is an integer-valued conserved charge and it spreads; in SU(2) only its parity is conserved, and two spin-1/2 lines fuse to spin 0 or 1. Nothing in this file, in the filter, or in (HS) uses that.

**The replacement (my answer to the brief).**
(R1) Replace (HS) by its proved forms: Theorem HS (both sectors, every twist and torus) and Lemma DS. They are theorems now. They are not the missing arrow; they cost nothing and they select nothing.
(R2) Drop the filter from the proof tree of (E17) at the crossover. It is a correct separation of one-plaquette operators. In the one-slice law it multiplies a density below 1e-6. Keep it as a test: any proposed mechanism that needs the SU(2) vacuum to expose spin >= 5/2 is refuted by Step 5.
(R3) The statement that carries (E17), in one-slice form (OPEN, and it is (E17) itself by P1): the dense Z_2-cycle C of half-integer edges (density 0.33 at beta = 2.3, plausibly percolating) has trivial omega-class except with probability C a^p eta_*^(a/2). A proof must (i) fail for U(1): use fusion 1/2 x 1/2 = 0 + 1, that is, parity and not integer flux (sharpened in the addendum below: parity alone is what Z_2 has); (ii) fail for frozen 2T: use e_(1/2) < 1 quantitatively, that is, continuity (a non-freezing bound such as Lemma DS, but at the typical value 0.27, not the worst case 0.87); (iii) work on a percolating set: no Peierls count of half-integer paths. The first input with property (ii) that this file proves is Lemma DS. I know no input with property (i) at order one.

**On reflection positivity and chessboard bounds (ARGUED).** Q:336 asks whether the one-slice projections are reflection-compatible. They are, for reflection planes that bisect links: by Lemma OS the projection Pi_j at edge e is the factor d_j r_j chi_j(U_p(e)) on a timelike plaquette. If e crosses the plane, then in the gauge where the crossing links are 1 this factor is Sum_(a,b) D_ab(T) conj(D_ab(theta T)) with positive coefficient, the same form as the Wilson weight itself. If e does not cross the plane, it is an observable on one side. So chessboard estimates apply to edge-spin events in the three spatial directions. I did not need them: the homogeneous pattern "all edges of one direction have spin >= j0" is bounded by the proof of Theorem HS by (r_(j0) e^(3 beta (t+1)/(t-1)))^(|E|/3), which is below 1 at beta = 2.3 only for j0 >= 3 (r_3 = 3.0e-4 against e^(-6.9) = 1.0e-3), while Lemma DS already gives the product bound for j0 = 2 with tau_2 <= 0.275 and no parity or evenness condition on the sides. A chessboard bound cannot reach (LS) either: the binding event there, half-integer spin, has homogeneous-pattern probability of order one (density 0.33).


### Step 7. Fact tests, ranges, and two by-products.

**Fact tests.**

| Test | Theorem HS | Lemma DS | Verdict V1/V2 and (R3) |
|---|---|---|---|
| Must fail for U(1) Coulomb | Does not fail: holds verbatim for U(1) (P3). So it is not a confining input, and I claim none. | Does not fail: holds for U(1) (staples are complex numbers). Same. | The verdict is the U(1) test applied to the tree: (HS) + filter cannot give (LS). |
| Must use something Q_8, 2T lack | Uses nothing they lack: holds verbatim in their own irreducibles (P3). | Uses that SU(2) is a sphere: the staple sum is a multiple of a group element. Fails for finite G; at the flat background their environment coefficient is r^G_rho(5 beta), frozen. | (R3) (ii) names this input; its typical value (0.27) is not proved. |
| Worst-case caps 2/3, 0.775, 1.0109 (rows 836, 839) | Not a contraction bound; a global Jensen bound on a volume-order event. No cap applies. | A worst-case one-link bound. It is used only where the worst case is small (spin >= 2: r_j(beta) r_j(5 beta) d_j^2). For spin 1/2 its worst case 0.87 says nothing, as the caps predict. | No claim above the caps. |
| (AN1) is the worst case in disguise (row 845) | Not used. | Not used. | Not used. |
| Order-one window 2.3 to 2.6 | Holds for all beta <= 3 at spin 2 (t -> infinity), beta <= 4 at spin 3. | tau_2 <= 0.275 for beta <= 2.5 and tau_2 <= 0.338 for beta <= 2.6 (hand majorants: Sum_(j>=2) d_j^2 1.3^(2j)/(2j+1)! <= 0.8401, U_1..U_4(13) product <= 0.4018). | (E17) stays open in the whole window. |
| The real object (SEED-FP) | A fixed-coupling theorem. Along first passage the threshold spin grows like 1.1 beta (2 j0 = c beta with c(log 2c - 1) = 1). | Same remark; the factor r_j(5 beta) tends to 1. | (SEED-FP) is not touched. |

**By-product B1 (electric-energy moment; PROVED).** The proof of Theorem HS shows more than the count bound. For t >= 2 and both sectors,

Tr(P_sigma K^(-1/2) L_m^t K^(-1/2)) <= [e^beta (e^(2 beta)/z)^(1/(t-1))]^|E| Tr(P_+ L_m^t),

that is, E[Prod_e r_(j_e)^(-1)] <= e^(beta|E|(1 + o(1))) in the one-slice law. In the ground state Omega_+ (t -> infinity) Jensen gives the mean electric energy per edge, (1/|E|) Sum_e E[log(1/r_(j_e))] <= beta. GUIDE check at beta = 2.3 from Step 5: 0.327 x 0.736 + 0.035 x 1.793 + 0.0013 x 3.10 = 0.31, against the bound 2.3. The bound is far from sharp; the missing factor is the vacuum energy of B that Jensen discards.

**By-product B2 (a correction to row 843's RESULT line; GUIDE).** "Exposure density about 1% per plaquette at the crossover" is the frozen-plaquette law w_j. The measured one-slice density of odd edges with spin >= 5/2 is below 6e-7 at beta = 2.3 and 1.3(4)e-6 at beta = 2.5; the proved bound is 0.041. Row 843's Theorem 3.4, Corollary 3.7 and its Section 4.1 are untouched; I did not re-check them. Its claim 4.4 (ii), that (HS) is SU(2)-selective, holds only in its labelling: the proof of (HS) is group-blind.

**What a checker should read first.** (i) Theorem HS, steps (2), (3) and (5): the factorization L^t = K^(1/2) Y K^(1/2), the inequality B^2 <= e^(beta|P|) B, and the Holder step. (ii) Step 2a (ii): lambda_+ >= z^|E|. (iii) Lemma DS: the conditional independence of the time-0 links of a plaquette-separated set, and Int k_b(g) chi_j(g h) dg = r_j(b) chi_j(h). (iv) The arithmetic of Corollary DS-1. (v) Proposition P1. (vi) Whether Verdict V1 states the U(1) test fairly: its rigorous leg is the large-beta Coulomb phase; the matched-profile comparison at beta = 1.09 is GUIDE.


**GUIDE re-check of the hand arithmetic (decides nothing).** A short script recomputed the majorant sums of Corollary DS-1 (0.70744 at beta = 2.5, 0.83972 at 2.6), the Amos products (0.3877 at 12.5, 0.4017 at 13), log(120/1.25^4) = 3.8949, and the true values: tau_2 = 0.148 at beta = 2.5 and 0.176 at 2.6 (hand bounds 0.275, 0.338); r_2 e^beta = 0.068, 0.099, 0.159, 0.463 at beta = 2.15, 2.3, 2.5, 3.0; the thresholds eta > beta/log(1/r_2) = 0.444, 0.499, 0.576, 0.796 at the same couplings; r_(1/2)(11.5) = 0.873.

**Addendum to Step 6 (one more comparison; GUIDE, recalled).** Z_2 gauge theory has one non-trivial irreducible, with kinetic eigenvalue tanh(beta), fusion 1 x 1 = 0, and no high irreducibles at all, so (HS) and a perfect filter hold trivially. Its self-dual point is tanh(beta_c) = sqrt(2) - 1 = 0.414, and it is deconfined above it (recalled; first-order transition at the self-dual point in the numerics). SU(2) at beta = 2.3 has r_(1/2) = 0.479 > 0.414. So three theories with the same or a smaller kinetic eigenvalue of the flux carrier sit on the deconfined side: Z_2 (frozen), 2T (frozen, r_V = 0.48), U(1) (Coulomb, 0.48 at beta = 1.09). This sharpens (R3). Input (i) must be read as: SU(2) has no integer-valued conserved flux AND is continuous; parity alone is what Z_2 has, and Z_2 freezes. Input (ii), non-freezing, is what U(1) has, and U(1) spreads its integer flux. A proof of (E17) at the crossover must use both at once. The filter is neither.


### Step 8. Summary.

**No mass gap is proved here. Nothing in this file is checked by another model.** (E17), (FQ), (SEED-FP) remain open.

**PROVED (by hand, by Claude Fable 5.2, not checked).**
1. Theorem HS: for every beta, spin threshold j0, eta, t >= 2, torus, twist and both parity sectors, Tr(P_sigma Pi_{N_(>=j0) >= eta|E|} L_m^t) <= [r_(j0)^eta e^beta (e^(2 beta)/z)^(1/(t-1))]^|E| Tr(P_+ L_m^t).
2. Corollary HS-1: the statement (HS) of row 843 on [2.15, 2.5], t = a >= 9: rate c = 3.895 eta - 3.125 > 0 for eta > 0.803. Corollary HS-2: nontrivial for spin 2 at every beta <= 3 and for spin 3 at every beta <= 4 (t -> infinity).
3. Lemma OS: the one-slice law is the Wilson expectation of Prod d_j r_j chi_j(U_p)/k(U_p) over the timelike plaquettes of one layer; half-integer density = (1 - E e^(-2 beta x_p))/2; rho_j = rho_0 d_j r_j(beta) E_nu[chi_j(U_p)].
4. Lemma DS (double suppression): on plaquette-separated sets, P(j_S) <= P(0_S) Prod d_j^2 r_j(beta) r_j(5 beta). Corollary DS-1: density of spin >= 2 at most 0.275 (beta <= 2.5; 0.338 for beta <= 2.6), density of odd spin >= 5/2 at most 0.041. Corollary DS-2: a product bound, and (HS) for every t >= 3 with eta = 0.8.
5. Proposition P1: P_- is the projection on {N_h(cut) odd}; p_m(t) = P_m(N_h(cut) odd). Proposition P2: (LS) is (E17) up to e^(-c|E|). Proposition P3: Theorem HS and Lemma OS hold verbatim for U(1), Q_8, 2T, 2O, 2I; Lemma DS holds for U(1) and fails for finite groups at its continuity step.
6. By-product B1: E[Prod_e r_(j_e)^(-1)] <= [e^beta (e^(2 beta)/z)^(1/(t-1))]^|E|, and mean electric energy per edge at most beta in the ground state.

**READ.** The definitions (E1)-(E3), (E16)-(E18) of EX; (HS), (LS), Theorem 3.4, Corollary 3.7 and Section 4 of Q; (SEED-FP) of FLN; rows 786, 838, 839, 845, 860 of FIN. I did not re-check Q's Theorem 3.4; nothing here depends on it.

**ARGUED.** Verdict V1: (HS) plus the filter cannot force (LS), by the U(1) test (rigorous leg: U(1) shares every input and has a Coulomb phase at large beta, recalled; matched-profile leg at beta = 1.09: GUIDE). Verdict V2: spin-1/2 flux avoids the filter without effort. The reading of where SU(2), 2T, U(1), Z_2 differ in the one-slice law. Reflection-compatibility of the one-slice projections for link-bisecting planes.

**GUIDE.** The 8^4 Monte Carlo table of Step 5 (one seed, untwisted); all decimals not tied to a hand bound; the percolation and critical-coupling numbers recalled from the literature (no paper opened, no download made).

**OPEN.** (E17) = (LS) = the parity statement (R3): the dense Z_2-cycle of half-integer edges has trivial omega-class except with probability C a^p eta_*^(a/2). A typical-value form of Lemma DS (environment coefficient near 0.27 rather than 0.87). Any order-one input that separates SU(2) from U(1) in the one-slice law.

**Answers to the brief, in order.**
- Is (HS) true at order one? Yes. PROVED, uniformly in tori and twists, on [2.15, 2.5] and beyond (to beta = 3), in both sectors.
- The right notion of rarity. Three proved forms: the large-deviation count (Theorem HS), the one-edge density and product bound (Lemma DS), the exponential moment of the electric energy (B1). The plaquette law w_j is the frozen-environment law and overstates high spin by a factor near 3000 at spin 2 and above 2e4 at odd spin >= 5/2 (GUIDE, beta = 2.3).
- Is (HS) the right target? No. Its proof is group-blind and it leaves (LS) equal to (E17).
- Does the filter plus (HS) force (LS)? No (ARGUED, U(1) test). The filter acts on a set of edges of measured density below 1e-6.
- The replacement: (R1) use Theorem HS and Lemma DS as free theorems; (R2) drop the filter from the tree at the crossover, keep it as a test; (R3) the carrying statement is the Z_2-homology statement above, and its proof needs continuity and the absence of an integer flux together.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the Wilson convolution facts and the half-kernel transfer, as read through EX and Q; the first-passage frame of (SEED-FP). Balaban: the effective-action estimates behind that frame (not used in any proof here). Codex gpt-6-astra max: EX (E1)-(E18) and the route-A text TR. Claude Opus 5.5: Q (row 843), FLN (row 837). The Amos-type bound U_nu is used as proved in Q, Lemma 3.1.

**Delivery.** Only this file was written, plus the GUIDE script and its output in /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane860/scripts/ (guide860.py, guide860.out; under 100 MB, about one minute per coupling). No repository file, registry, PR or post was touched. No subagent was used. No download was made.

RESULT: PARTIAL, by Claude Fable 5.2 (max effort), not checked — (HS) is PROVED and is the wrong target. Theorem HS: for every twist, torus, t >= 2 and both parity sectors the one-slice weight of {at least eta|E| edges of spin >= j0} is at most [r_(j0)^eta e^beta (e^(2 beta)/z)^(1/(t-1))]^|E| Tr(P_+ L_m^t) (an electric-energy bound: K^(-1) through one transfer step, Jensen on the trial vector 1); on [2.15, 2.5] with t = a >= 9 this is row 843's (HS) with c = 3.895 eta - 3.125 > 0 for eta > 0.803, and it holds for spin 2 up to beta = 3. Lemma DS (double suppression, one link integrated exactly): spin densities obey rho_j <= rho_0 d_j^2 r_j(beta) r_j(5 beta), so spin >= 2 has density at most 0.275 and odd spin >= 5/2 at most 0.041 for beta <= 2.5, with a product bound on plaquette-separated sets and (HS) at every t >= 3. GUIDE (8^4 heat bath): the true densities at beta = 2.3 are 2e-5 and below 6e-7; the plaquette law w_j (6% and 1.3%) is the frozen-environment law, not the one-slice law; half-integer edges have density 0.33. Consequences: (LS) equals (E17) up to e^(-c|E|) (PROVED); the odd sector is exactly the event that the half-integer Z_2-cycle of a slice has odd omega-class (PROVED); Theorem HS and the filter's kind of input hold verbatim for U(1) in its Coulomb phase, so the filter plus (HS) cannot force (LS) (ARGUED), and in the SU(2) vacuum the filter is exposed at a measured density below 1e-6 (GUIDE). OPEN: (E17) itself; it needs an input using continuity and the absence of an integer flux together, which neither the filter nor (HS) supplies.
