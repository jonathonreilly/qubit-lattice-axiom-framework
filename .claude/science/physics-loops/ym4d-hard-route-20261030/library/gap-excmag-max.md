# FINISH row 888, gap-excmag-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone commit: c71f9498b5e32bae683db3ca593d7786a623f9be (clone /Users/jonreilly/ym4d-lead/clone, pulled 2026-11-13, already up to date).
Author: Claude Fable 5.2 at max effort. Row 888. Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Marks: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE (numeric, never discharges), OPEN.

## Target (as given in the brief; exact objects to be fixed in step 1 from rows 872, 873, 875, 881)

The magnetic bound that would prove the crux lemma EXC. Row 875 reduced EXC exactly to a magnetic residual (its identity (22)). Sharpest open statement (row 881): an order-L_i lower bound, at least -theta gamma_min L_i with theta < 1, uniform over tori, twists and b, on the boosted-minus-unboosted, odd-minus-all magnetic-cut plaquette response integrated over b in [0, beta]. Available bound: 4 beta n, of order a^3.

Task: prove that bound (explicit constants), or the strongest form reachable, or show it fails.

## Plan (one step per response; each step appended here before the next)

1. Read rows 872, 873, 875, 881. Record the exact objects: EXC, identity (22), the magnetic residual, gamma, the 4 beta n bound. No new mathematics.
2. Plausibility of order L_i. Write the response as a covariance of the cut-plaquette count with the odd-sector indicator. Decide what could make it extensive in the cut length and not in the volume or the cut area.
3. Exact small or degenerate cases by hand (strong coupling in the magnetic coupling b; one-plaquette and abelian reference cases) to fix signs and the true order in L_i, n, b.
4. Attack A: condition on the slice (electric data), then a correlation or monotonicity inequality for the magnetic plaquettes given the electric data.
5. Attack B: reflection positivity across the cut (chessboard or Cauchy-Schwarz form) for the odd-minus-all, boosted-minus-unboosted difference.
6. Fact tests on whatever survives: must fail for Coulomb U(1); must use something Q_8 and 2T lack; compare with the 2/3, 0.775, 4 G_3 caps and (AN1).
7. If the bound looks false: build the counterexample or the obstruction (GUIDE numerics allowed, small, labelled).
8. Final statement: what is PROVED, what is OPEN, constants, and the RESULT line.

## Step log

### Step 1a. Objects, from rows 875 and 881 (both read in full)

READ `D/library/gap-exc-astra.md` 1-419 (row 875, OpenAI Codex gpt-6-astra) and `D/library/gap-exc-check-opus.md` 1-168 (row 881, Claude Opus 5.5). Objects, in their notation:

- Spatial torus, periods (L_2, L_3, L_4) = (a, c, d), a >= 3, c, d in {a, 2a}. Time period t = a. n = 3acd spatial edges; also n spatial plaquettes. (875:59, 881:27, 881:71.)
- x(g) = (1/2) tr g. One-link kinetic kernel e^{beta x}/z, z = 2 I_1(beta)/beta. Eigenvalue on spin j: r_j = I_{2j+1}(beta)/I_1(beta). K_1 = product over spatial edges. (875:150-155, 881:111-115.)
- H_e = projection on half-integer spins >= 5/2 at edge e. N = sum_e H_e. K_s = s^N K_1. (875:61-63.)
- M(U) = sum over spatial plaquettes of eta_{m,p} x(U_p), eta = twist signs. B_b = exp(b M). (875:367, 875:361.)
- Kinetic cut: L_{s,b} = z^n K_s^{1/2} e^{bM} K_s^{1/2}. Magnetic cut: A_{s,b} = z^n e^{bM/2} K_s e^{bM/2}. Same nonzero sector spectra. (875:369-376.)
- P_- = odd sector for the cut pairing in direction i (i = 3, 4; twists with m_2 = 0). p_{s,b} = Tr(P_- A_{s,b}^a)/Tr(A_{s,b}^a). (875:66-71, 881:128-130.)
- J = (1/a) log(p_S/p_1). EXC: J >= c_0 > 0 uniformly; consumer needs c_0 >= -log(eta_0)/2. (875:73-85.)
- d^mag_{s,b} = Tr(P_- M A^a)/Tr(P_- A^a) - Tr(M A^a)/Tr(A^a), and d/db log p_{s,b} = a d^mag_{s,b}. (875:369-376.)
- Identity (22): J_beta = J^el + int_0^beta (d^mag_{S,b} - d^mag_{1,b}) db. (875:378-381.)
- Electric reference (b = 0): (1/(a L_i)) log(p^el_S/p^el_1) -> gamma = log(r_V^{2T}/r_{1/2}) > 0; q_1 = r_{1/2}, q_S = r_V^{2T} = S r_{5/2}. Two-sided bound (19): q_s^{a L_i}/(1+eps_s(a))^n <= p^el_s <= binom(n, L_i) (C q_s^a)^{L_i} (1+eps_s(a))^n. (875:301-350.)
- Target (881:156-163): R := int_0^beta (d^mag_{S,b} - d^mag_{1,b}) db >= -theta gamma_min L_i, theta < 1, uniform. Available: |R| <= 4 beta n.

GUIDE decimals at beta = 2.3 (my hand Bessel sums; not premises): I_1 = 2.0978, r_{1/2} = 0.479, r_1 = 0.1665, r_{3/2} = 0.0450, r_2 = 0.0099, r_{5/2} = 0.00185, r_{7/2} = 0.00004. With r_V^{2T} = 0.4841 (881:75): S = r_V^{2T}/r_{5/2} is about 262. The boost is large: it lifts spin 5/2 from 0.0018 to 0.484, just above spin 1/2 at 0.479. -log r_{1/2} = 0.735.

### Step 2 (first part). What the residual is; is order L_i plausible?

**PROVED (one line from 875's own derivative).** For each s, integrate d/db log p_{s,b} = a d^mag_{s,b}:

  int_0^{b'} d^mag_{s,b} db = (1/a) log( p_{s,b'} / p^el_s ).                         (M1)

So R(b') := int_0^{b'} (d^mag_{S,b} - d^mag_{1,b}) db = (1/a) [ log(p_{S,b'}/p^el_S) - log(p_{1,b'}/p^el_1) ].   (M2)

**PROVED (upper bound, order L_i, each s).** p <= 1 and the lower half of (19) give, for every b' >= 0, every torus, every twist:

  int_0^{b'} d^mag_{s,b} db <= (1/a) log(1/p^el_s) <= L_i (-log q_s) + (n/a) eps_s(a).   (M3)

The last term is at most 12 a^2 C q^a, which tends to 0. So the integrated magnetic response of each s is at most (-log q_s) L_i + o(1). The upper side is of order L_i, not n, for free.

**What makes it extensive in L_i (ARGUED).** p_{s,b} is the probability of odd 't Hooft electric flux in direction i: p = (1 - Z_tw/Z)/2 with the centre twist in the (time, i) plane. The integrated response is a difference of flux free energies, (M1). It is of order L_i from below exactly when the model at b' does not suppress odd flux faster than an area law, p_{s,b'} >= exp(-C a L_i). So "order L_i" is the statement "finite string tension at b'", for s = 1 and for s = S. The covariance form hides this: the covariance of M with the odd indicator is a difference of two order-n means, and only the flux sheet's neighbourhood (a L_i temporal plaquettes) responds differently.

**Reading of the target (PROVED equivalence, from (M2) and (19)).** R(beta) >= -theta gamma L_i is, up to the o(L_i) errors of (20),

  log( p_{S,beta} / p_{1,beta} ) >= (1 - theta) gamma a L_i - o(a L_i).

Since p_{S,beta} <= 1 this implies p_{1,beta} <= exp(-(1-theta) gamma a L_i + o): an area law for the unboosted model at b = beta. So any proof of the target contains a proof of the area law in the window. Lower bounds on p_{1,beta}/p_{S,beta} refute it; upper bounds prove it.

OPEN at this point: the size of sigma_1 - sigma_S at b > 0 (sigma = flux free energy per unit a L_i). Next: second-order expansion in b by hand, for the vacuum, the spin-1/2 line and the spin-5/2 line. Expectation to test (ARGUED, to be checked in Step 3): the spin-1/2 sheet gains about 4 r_{1/2}(beta)^2 (b/2)^2 = 0.23 b^2 per unit area from bumps; the spin-5/2 sheet gains almost nothing (its bumps need spin-5/2 spatial plaquettes, weight about (b/2)^5/720, unboosted). If so the two carriers cross near b* = sqrt(gamma/0.23), about 0.2, far below beta. Beyond b* the boosted model's odd sector would be carried by the same spin-1/2 sheet as the unboosted one, and the electric gain gamma would be gone. (Step 3 corrects this first guess: the bump amplitude is (b/4)^2 per pair of spatial plaquettes, not (b/2)^2; the exact second-order coefficients give 0.049 b^2 and 0.055 b^2 with opposite signs, and b* = 0.31.)

### Step 1b. Rows 872 and 873, exact definitions

READ `D/library/gap-filter-ls-opus.md` 20-209 (row 872, Claude Opus 5.5): (E1) H = L^2(SU(2)^E)^(SU(2)^V), K = tensor of C_beta, L_m = z^|E| K^(1/2) B_m K^(1/2) (872:48-50); Theta = product of edge sign flips on the cut cochain, P_- = (1 - Theta)/2 (872:51-53); P1: P_- is the event that the half-integer cycle of the slice has odd winding in direction i (872:59-61, 100-103); EXP (872:128-150); EXC (872:170-175); Prop 3.2 (b): EXC holds iff p(1) <= e^{-c_0 a} p(s_*) (872:177-185). READ `D/library/gap-filter-ls-check-astra.md` 94-200 (row 873, OpenAI Codex gpt-6-astra): each unnormalized sector trace is nondecreasing in s, with no sign for Delta (873:104-107); the high indicator is 1{j_e in {5/2, 7/2, ...}} (873:121-127); the rate condition c_0 >= -log(eta_0)/2 (873:159-173); and the remark that an exponentially small p(1) can have p(s*) = p(1), so that EXC is an additional comparative condition (873:175-182). 875 and 881 apply exactly these corrections (881:14-32). No further object is needed.

### Step 3. Exact second-order magnetic response at b = 0 (PROVED), and what it shows

Setting. Fix s in {1, S}, a torus, a twist. Write w_j for the one-link kinetic eigenvalue (w_j = r_j, or S r_j on high j), w(j) = prod_e w_{j_e} for an edge-spin configuration j, Pi_j for the projection of H on configuration j, m(j) = rank Pi_j. K = sum_j w(j) Pi_j. Z_sigma(b) = Tr(P_sigma A_b^a), A_b = e^{bM/2} K e^{bM/2}, F_sigma = log Z_sigma. x_p = x(U_p).

**Lemma 3.1 (PROVED).** F_sigma'(0) = 0, so d^mag_{s,0} = 0. And

  F_sigma''(0) = a sum_{k=0}^{a-1} Tr(P_sigma M K^k M K^{a-k}) / Z_sigma(0)
             = (a / Z_sigma(0)) sum_p sum_{ {j,j'} , j in sigma} T_p(j,j') w(j)^a g_a(w(j')/w(j)),      (S1)

over unordered pairs, with T_p(j,j') = || Pi_{j'} x_p Pi_j ||_HS^2 = T_p(j',j) and g_a(x) = 1 + 2x + ... + 2x^{a-1} + x^a = (1+x)(1-x^a)/(1-x). The twist signs drop out.

*Proof.* d_b A = (MA + AM)/2. Cyclicity and [P, A] = 0 give d_b Tr(P A^a) = a Tr(P M A^a). Differentiate again: (a/2) sum_{i=0}^{a-1} [Tr(P M A^i M A^{a-i}) + Tr(P M A^{i+1} M A^{a-1-i})]. At b = 0 put c_k = Tr(P M K^k M K^{a-k}); c_0 = c_a by cyclicity; the sum is a sum_{k=0}^{a-1} c_k. Multiplication by a spin-1/2 matrix element of U_e maps the spin-j block of e into j +- 1/2. So Pi_j x_p Pi_{j'} = 0 unless j and j' differ by 1/2 exactly on the four edges of p. Hence Tr(P M K^a) = 0 (first derivative), and Pi_j x_p Pi_{j'} x_{p'} Pi_j = 0 unless p' = p (distinct plaquettes have distinct edge sets; periods >= 3). eta_p^2 = 1 removes the twist. Grouping the two orders of a pair gives w^a [sum_{k=0}^{a-1} x^k + sum_{k=1}^{a} x^k] = w^a g_a(x). QED

**Lemma 3.2 (PROVED; local amplitudes).** Let psi = chi_j(U_l) for a straight winding line l (unit vector), or psi = 1.
(a) p shares no edge with l (or psi = 1): x_p psi lies in one configuration, norm^2 = 1/4, weight ratio rho := r_{1/2}^4.
(b) p shares one edge e with l: x_p psi has two components, e in spin J = j - 1/2 or j + 1/2 (the three other edges of p in spin 1/2), with norm^2 T_J = (1/4) d_J/(2 d_j) and weight ratio x_J = (w_J/w_j) r_{1/2}^3.

*Proof.* (a) U_p and U_l are independent under Haar; int x^2 = 1/4. (b) Write U_l = U_e V, U_p = U_e W (orientation is immaterial: characters are real class functions). chi_{1/2}(gW) chi_j(gV) = tr[(D^{1/2}(g) x D^j(g))(D^{1/2}(W) x D^j(V))] = sum_J tr[D^J(g) C_J (D^{1/2}(W) x D^j(V)) C_J^*], C_J the Clebsch-Gordan partial isometry. The J-component has squared L^2(dg) norm (1/d_J) || C_J (W x V) C_J^* ||_HS^2. Average over independent Haar W, V: E[(W x V) P_J (W x V)^*] = (d_J/(2 d_j)) 1, so the mean is (1/d_J) d_J^2/(2 d_j) = d_J/(2 d_j). Multiply by 1/4 for x = chi_{1/2}/2. Check: (d_{j-1/2} + d_{j+1/2})/(2 d_j) = 1. QED

Values. j = 1/2: T_0 = 1/16 (the detoured line, x_0 = r_{1/2}^2), T_1 = 3/16 (x_1 = r_1 r_{1/2}^2). j = 5/2 at s = S: T_2 = 5/48 (x_2 = r_2 r_{1/2}^3/q_S), T_3 = 7/48 (x_3 = r_3 r_{1/2}^3/q_S). Integer spins 2, 3 are not boosted.

**Theorem 3.3 (PROVED).** Put v(x) = (1+x)/(1-x), r = r_{1/2}(beta), and

  D_{1/2} = (1/16) v(r^2) + (3/16) v(r_1 r^2) - (1/4) v(r^4),
  D_{5/2} = (5/48) v(x_2) + (7/48) v(x_3) - (1/4) v(r^4).

Along admissible tori with a -> infinity, uniformly in twists and in beta on a compact set:

  (1/a) d_b^2 log p_{1,b} at b=0  = 4 L_i D_{1/2} + o(1),
  (1/a) d_b^2 log p_{S,b} at b=0  = 4 L_i [ pi_5 D_{5/2} + pi_1 D_{1/2} ] + o(1),   pi_1/pi_5 = (r/q_S)^{a L_i} = e^{-gamma a L_i}, pi_1 + pi_5 = 1.

Hence d_b (d^mag_{S,b} - d^mag_{1,b}) at b = 0 equals 4 L_i pi_5 (D_{5/2} - D_{1/2}) + o(1), and

  D_{5/2} - D_{1/2} = (5/24) x_2/(1-x_2) + (7/24) x_3/(1-x_3) - (1/8) r^2/(1-r^2) - (3/8) r_1 r^2/(1 - r_1 r^2) < 0.

*Proof.* Vacuum sector: the dominant configuration is j = 0 (weight 1). Odd sector: the dominant configurations are the A_i straight lines in the carrier spin (weight w_c^{a L_i} each, m = 1); x_p never maps one straight line to another (they differ on 2 L_i >= 6 edges). Insert Lemma 3.2 in (S1): every plaquette gives (1/4) g_a(rho), except the 4 L_i plaquettes that contain a line edge (four per edge; each contains exactly one line edge since transverse periods are >= 3), which give sum_J T_J g_a(x_J). g_a -> v exponentially fast. The difference of the two sectors is 4 L_i D.
Error terms. Pairs with no dominant member: sum_k w'^k w^{a-k} <= a (w^a + w'^a) and sum_{j'} T_p(j,j') = Tr(Pi_j x_p^2 Pi_j) <= m(j) bound them by 2 a n W^nd, W^nd = sum over non-dominant j of m(j) w(j)^a. Vacuum sector: W^nd <= (1+eps)^n - 1 (875 (18)). Odd sector: at a vertex, dim Inv(V_1 x ... x V_6) <= product of all but any two of the d's (V_{j1} x V_{j2} is multiplicity free), and <= sqrt(product). Choose a simple odd cycle g inside the half-integer cycle. Then m(j) <= prod_{e not in g} d_{j_e}^2, with no factor on g. So W_- <= sum_g u^{|g|} (1+eps)^n with u = sum over half-integer j of w_j^a (no d^2). Orient a simple odd cycle with positive winding in direction i. It has at least L_i forward i-steps, so a cycle of length L_i + m has at most m other steps (5 kinds each), and m = 0 only for a straight line. Starting it at a forward crossing of the cut, there are at most A_i (m+1) binom(L_i+m, m) 5^m such cycles for m <= L_i, and at most A_i 6^{L_i+m} <= A_i 36^m for m > L_i. Since L_i u tends to 0 exponentially, the sum over m >= 1 of these counts times u^m is exponentially small. With u = w_c^a (1 + exponentially small), the non-dominant part is exponentially small relative to A_i w_c^{a L_i}, against polynomial factors a n^2. At s = S the spin-1/2 lines are kept as a second dominant class with relative weight e^{-gamma a L_i}; this gives the mixture. The sign: x_3 <= x_2 < r_2 r^2 (as q_S > r), and r_2 = I_5/I_1 <= (beta/2)^4/120 < 0.024 for beta <= 2.6; so the positive part is below (1/2)(0.024 r^2)/(1 - 0.024) < 0.0123 r^2 < (1/8) r^2 (5/24 + 7/24 = 1/2). QED

Numbers (hand Bessel sums; arithmetic, not premises of the proof):

| beta | r_{1/2} | q_S = r_V^{2T} | gamma | D_{1/2} | D_{5/2} | 4(D_{5/2} - D_{1/2}) |
|---|---|---|---|---|---|---|
| 2.3 | 0.47928 | 0.48414 | 0.01009 | +0.02432 | -0.02737 | -0.2068 |
| 2.6 | 0.52034 | 0.52820 | 0.01499 | +0.02827 | -0.03869 | -0.2678 |

Reading.
1. The second-order response is of order L_i exactly: all n - 4 L_i plaquettes off the flux line cancel between the odd sector and the full ensemble. This answers the "cut length, not volume" question at this order. The mechanism is locality of the flux carrier, not a property of the cut.
2. The sign is negative, and large against gamma. The spin-1/2 line gains from the magnetic term (its neighbours can detour the line, x_0 = r^2 = 0.23, more than the vacuum's rho = r^4 = 0.05). The boosted spin-5/2 line loses: a neighbouring plaquette turns its edge into integer spin 2 or 3, which is not boosted (x_2 = 0.002), so the line blocks the vacuum fluctuation of its 4 L_i neighbours.
3. To second order, sigma_{1/2}(b) = -log r - 2 D_{1/2} b^2 and sigma_{5/2}(b) = -log q_S - 2 D_{5/2} b^2 (flux free energy per unit a L_i; the same sigma_{1/2} for s = 1 and s = S, since no high spin occurs at this order). So R(b)/L_i = -2 (D_{1/2} - D_{5/2}) b^2 + higher order = -0.1034 b^2 at beta = 2.3.
4. ARGUED (second order extrapolated; the cluster expansion that would make it PROVED is not done here): the two carriers cross at b* = sqrt(gamma / (2(D_{1/2} - D_{5/2}))) = 0.312 at beta = 2.3 and 0.335 at beta = 2.6. For b > b* the boosted model's odd sector is carried by the spin-1/2 line, as in the unboosted model. Then J_b / L_i = sigma^{(1)}_{1/2}(b) - sigma^{(S)}_{1/2}(b) =: delta(b), and R(b) = -(gamma - delta(b)) L_i. The natural expansion parameter is small there (b^2/16 = 0.006), so fourth-order terms cannot move b* much.
5. Fixed-volume caveat. Theorem 3.3 is a statement about derivatives at b = 0 on each finite torus. The remainder of the Taylor expansion is not uniform in the volume. The limit function is not analytic at b* (a level crossing), so no Taylor argument reaches past b*.

GUIDE (arithmetic check of Step 3; script `scratchpad/lane888/scripts/guide_coeffs.py`, pure Python Bessel series, seconds). It reproduces the table. One decimal changes: gamma(2.3) = 0.01006 (q_S = 0.48413), not 0.01009. Full row set:

| beta | gamma | S | -2 D_{1/2} | -2 D_{5/2} | 4(D_{5/2} - D_{1/2}) | b* |
|---|---|---|---|---|---|---|
| 2.3 | 0.01006 | 262 | -0.0487 | +0.0547 | -0.2068 | 0.312 |
| 2.4 | 0.01158 | 226 | -0.0513 | +0.0619 | -0.2264 | 0.320 |
| 2.5 | 0.01322 | 196 | -0.0539 | +0.0694 | -0.2467 | 0.327 |
| 2.6 | 0.01499 | 171 | -0.0565 | +0.0774 | -0.2678 | 0.335 |

Remark on the o(1) of Theorem 3.3 (PROVED refinement). At s = S the crude bound u^{|g|} contains mixed assignments (some line edges in spin 1/2, some in 5/2) with relative weight L_i e^{-gamma a}, which is small only for very large a. They do not occur: at a vertex of g where the two g-edges carry different spins, Inv(V_j x V_j') = 0, so a third edge at that vertex is nonzero and brings a factor eps. With this the error is at most C a^k eps times (1 + e^{-gamma a})^{L_i} <= C a^k eps e^{2/(gamma e)}; the last factor is a constant. So the o(1) is exponentially small at the rate of eps (about 0.53^a), with a large constant.

### Step 4. Consequences at small b; the dressing response of the spin-1/2 line

**Corollary 4.1 (PROVED, per torus).** d^mag_{s,0} = 0 for both s. For every sufficiently large admissible torus there is b_0 > 0 (depending on the torus) with, for 0 < b < b_0:
(a) d^mag_{1,b} > 0 whenever r_{1/2}(beta)^2 <= 1/3 (in the window r^2 <= 0.271; the condition holds up to beta about 3.09, hand arithmetic). Indeed D_{1/2} = (1/8) r^2 (1 - 3 r^2)/(1 - r^4) + (3/8) r_1 r^2/(1 - r_1 r^2) > 0.
(b) d^mag_{S,b} < 0: D_{5/2} <= (1/2) [x_2/(1-x_2) - r^4/(1-r^4)] < 0 since x_3 <= x_2 < r^4 (x_2 < 0.024 r^2 and r^2 > 0.024).
(c) R(b) < 0. The magnetic residual is negative from the start, with R''(0) = 4 L_i (D_{5/2} - D_{1/2}) + o(1), about -0.21 L_i to -0.27 L_i in the window.
So the unboosted odd fraction grows with b near 0 and the boosted odd fraction falls. No monotonicity in b holds for the boosted model.

**Lemma 4.2 (PROVED; how many plaquettes it takes to make a high edge).**
(a) Let psi lie in one configuration j and let X = x_{p_1} ... x_{p_m}. Then X psi has components only in configurations j' with |j'_e - j_e| <= m_e/2 and 2(j'_e - j_e) = m_e mod 2, m_e = number of factors whose plaquette contains e. So a half-integer spin >= 5/2 on e needs m_e >= 5 from the vacuum, m_e >= 4 on an edge of a spin-1/2 line, m_e >= 5 on any other edge in the presence of that line.
(b) For a line edge e and its four plaquettes p_1..p_4: || H_e x_{p_1} x_{p_2} x_{p_3} x_{p_4} chi_{1/2}(U_l) ||^2 = 3/4096 > 0.
*Proof.* (a) Each factor moves each of its four edge spins by exactly 1/2. (b) With g = U_e: prod_i chi_{1/2}(g W_i) chi_{1/2}(g V) = tr[g^{x5} (W_1 x ... x W_4 x V)] on (C^2)^{x5}; W_1..W_4, V are independent Haar (the four plaquettes have disjoint remaining edges, none on l). Sym^5 occurs once; the spin-5/2 component is tr[D^{5/2}(g) P_S (xW) P_S], with squared norm (1/6) E ||P_S (xW) P_S||_HS^2 = (1/6)(36/32) = 3/16. Multiply by (1/4)^4. QED

**ARGUED (the dressing gain; perturbative, not uniform in the volume as written).** Take b above the crossing b* and small. The odd sector of both models is carried by the spin-1/2 line. The boost enters the line's free energy first at order b^8 (create four neighbours of one line edge, remove them), and the vacuum's first at order b^10 (Lemma 4.2 (a)). EXP at fixed b gives J_b = int_1^S Delta_b(s) ds/s with Delta_b(s) = C_8(s) b^8 L_i (1 + O(b^2)), C_8 > 0. The one-step channel of Lemma 4.2 (b) contributes s b^8 (3/4096) r_{5/2} r^{11} = 4.1e-10 s b^8 per line edge at beta = 2.3; channels with staggered creation times add a factor of a few. So

  delta(b) := lim J_b/L_i = c_8 b^8 (1 + O(b^2)),   c_8 of order 10^-7 to 10^-6 (order of magnitude only).

**The small-b picture (ARGUED from Theorem 3.3, Lemma 4.2).**

  J_b / L_i = max( gamma - 2 (D_{1/2} - D_{5/2}) b^2 + O(b^4),  delta(b) ),    R(b) = J_b - gamma L_i.

- For b < b* (about 0.31): the bound of row 881 holds with theta(b) = (b/b*)^2 (1 + O(b^2)).
- For b > b*: theta(b) = 1 - delta(b)/gamma, about 1 - 10^-7 at b = 1/2. The electric gain gamma is gone. What remains is a different quantity: the response of the spin-1/2 flux sheet's own free energy to the boost.
- The path in b from the electric reference crosses a level crossing of the boosted model's odd sector at b*. The limit of (1/(a L_i)) log p_{S,b} is not differentiable there. So no continuity or perturbative argument in b transports the reference gain to b = beta.

**PROVED (rearrangement of (22), (20)).** For every b: [R(b) >= -theta gamma L_i - o(L_i)] iff [J_b >= (1 - theta) gamma L_i - o(L_i)]. So a theta < 1 uniform over tori exists at b = beta iff liminf (1/(a L_i)) log(p_{S,beta}/p_{1,beta}) > 0. That is the area form EXC-W of row 872 with an unspecified rate; gamma only sets the unit in which theta is measured.

OPEN (the lemma that would turn the two ARGUED items into PROVED): a convergent expansion in the spatial coupling b at fixed temporal beta in the window, uniform in tori and twists, for the three flux free energies (spin-1/2 line at s = 1 and at s = S, spin-5/2 line at s = S), on an interval of b that contains b*. The reference at b = 0 is exactly solvable (875 (17)-(20)), and the expansion parameter at b* is about b^2/16 = 0.006 per plaquette pair, so convergence is expected; I did not prove it.

### Step 5. The three suggested attacks at general b: what each proves and where it stops

**5.1 Twist form (PROVED identity).** With rho_Theta = Tr(Theta A^a)/Tr(A^a) = 1 - 2p and <M>^tw = Tr(Theta M A^a)/Tr(Theta A^a) (p not 1/2):

  d^mag_{s,b} = ((1 - 2p)/(2p)) ( <M>_{s,b} - <M>^tw_{s,b} ).                              (A1)

*Proof.* P_- = (1 - Theta)/2 in numerator and denominator of <M>_-. QED
Reading: "d^mag of order L_i" says that the twist changes the total spatial plaquette energy by 2 p L_i O(1), an amount as small as p itself. Exponential clustering alone gives a change e^{-m a/2}, far larger than p. So order L_i is a statement about the flux sector, not about decay of correlations.

**5.2 Conditioning on the slice (PROVED identity and entropy bound).** The one-slice law at the magnetic cut is nu(dU) = Z^-1 e^{bM(U)} k'(U,U) dU, k' the kernel of K (e^{bM} K)^{a-1} on H; it is a positive law for both s, because K^{1/2} L^{a-1} K^{1/2} >= 0 has a continuous kernel. The odd part k'_- = P_- k' P_- satisfies 0 <= k'_-(U,U) <= k'(U,U). Put pi_-(U) = k'_-(U,U)/k'(U,U) in [0,1], the conditional odd probability given the slice. Then p = E_nu[pi_-] and

  d^mag_{s,b} = Cov_nu(M, pi_-)/p = E_{nu_-}[M] - E_nu[M],   d nu_-/d nu = pi_-/p.          (A2)

The relative entropy is H(nu_- | nu) = E_{nu_-}[log(pi_-/p)] <= log(1/p). The entropy inequality gives, for every t > 0,

  +-d^mag_{s,b} <= (1/t) [ log(1/p_{s,b}) + Lambda_+-(t) ],   Lambda_+-(t) = log E_nu exp(+-t (M - E_nu M)).   (A3)

Consequence (conditional). If M is sub-Gaussian under nu with variance proxy C n, then |d^mag| <= sqrt(2 C n log(1/p)). With an area-law lower bound p >= e^{-C' a L_i} this is O(a^{5/2}), between the trivial 2n = O(a^3) and the needed O(a). (A3) under this hypothesis gives no more than that: it uses the small entropy cost of the odd sector, not where the flux sits. What is missing is locality of the response, |E_{nu_-}[x_p] - E_nu[x_p]| <= C/A_i for each plaquette. Theorem 3.3 is exactly that statement at second order (only the 4 L_i neighbours of the line respond).

**5.3 Correlation inequalities (recalled, classical; and a PROVED failure).** For an abelian group with Wilson weights and no spatial twist (m = 0) the Ginibre inequality gives <M> >= <M>^tw term by term (the temporal twist flips the sign of some couplings and raises none), so by (A1) d^mag >= 0 for every b: the odd fraction grows with the magnetic coupling. I recall this from the literature; it is not used. No such inequality is known for SU(2). For the boosted kernel it is false: Corollary 4.1 (b) gives d^mag_{S,b} < 0 for small b on every large torus. The boosted temporal weight k_S is of positive type but not of the form exp(ferromagnetic), and it is negative near -I (875 (7)).

**5.4 Reflection positivity across the cut, and in time (PROVED tools; the missing step named).**
(a) PROVED. Let A >= 0 be trace class, [A, Theta] = 0, W bounded with Theta W = -W Theta, a even, G(tau) = Tr(W^* A^tau W A^{a-tau})/Tr(A^a). Then G is log-convex on [0, a], and

  p >= min( 1/2, G(a/2)^2/(8 ||W||^4) ),   G(a/2) >= G(0) (G(1)/G(0))^{a/2}.                 (A4)

*Proof.* In an eigenbasis of A adapted to the sectors, G(tau) Z = sum |<m, W n>|^2 lambda_m^tau lambda_n^{a-tau} over pairs in opposite sectors: a sum of exponentials in tau, so log-convex; convexity with tau >= 1 gives the second bound. For tau = a/2, Cauchy-Schwarz on each of the two sector orders gives G(a/2) Z <= 2 ||W||^2 (Z_+ Z_-)^{1/2}. If p <= 1/2 then Z_+ >= Z/2 and Z_-/Z_+ >= (G(a/2)/(2||W||^2))^2. QED
With W = chi_{1/2}(U_l), ||W|| = 2: the odd fraction is at least the square of the correlation of two winding Wilson lines at time distance a/2, over 128. So a lower bound p_{s,b} >= e^{-C a L_i} follows from a one-step survival bound G(1)/G(0) >= e^{-C L_i}.
(b) For s = 1 and no spatial twist the one-step bound is the classical reflection-positivity argument (Seiler: the area law is the fastest possible decay), with C = -log of the temporal plaquette expectation. Recalled, not re-proved here. With a spatial twist the transfer operator in direction i carries a symmetry insertion and the Jensen step of that argument needs care; I did not check it.
(c) For s = S that argument does not transfer as it stands. It uses reflections through site planes orthogonal to direction i. Those planes contain temporal plaquettes with weight k_S, which is not pointwise positive (875 (7)), so positivity of the transfer operator in direction i is not available (its multiplier part is not positive; I did not decide whether the operator is positive). Reflections through link planes still hold (the crossing weights are of positive type), but they do not anchor the convexity at length 0.
(d) PROVED (from (M2), p_{1,b} <= 1): R(b) >= (1/a) log p_{S,b} - J^el. So an order-L_i lower bound on R with some constant, R >= -(C + gamma) L_i - o(L_i), follows from p_{S,beta} >= e^{-C a L_i}: the boosted model has a finite flux tension. OPEN: that bound, uniformly in tori and twists. It would still be far from theta gamma (C is of order one, gamma is 0.01).
(e) Reflection across the cut (link planes) gives Z_tw <= Z, and for s = 1 log-convexity of the sector traces in L_i. It compares neither the two sectors' responses nor the two values of s.

**5.5 Verdict on the attacks.** None of them bounds R below at the scale theta gamma L_i. Conditioning plus entropy improves the exponent of a (conditionally) but not to 1. Correlation inequalities give a sign for abelian Wilson weights and fail for the boosted SU(2) kernel. Reflection positivity gives area-type lower bounds on p for s = 1 only.

### Step 6. Where the reference gain lives; fact tests

**Proposition 6.1 (PROVED; the electric-reference EXC integrand is a step).** At b = 0, for s in [1, S], with s_c := r_{1/2}/r_{5/2} = S e^{-gamma}:

  Delta_0(s) = <N>_{-,s} - <N>_{all,s} = L_i pi_5(s) + o(1),   pi_5(s) = (s/s_c)^{a L_i} / (1 + (s/s_c)^{a L_i}),

uniformly, as a -> infinity. So Delta_0 is exponentially small for s < s_c, equals L_i for s > s_c, and int_1^S Delta_0 ds/s = L_i log(S/s_c) + o(1) = gamma L_i + o(1), which is 875 (16).
*Proof.* K_s and N are diagonal in the spin configurations, so <N>_sigma = sum_{j in sigma} N(j) m(j) w_s(j)^a / sum_{j in sigma} m(j) w_s(j)^a. Use the two dominant classes and the error bound of Theorem 3.3 (the other half-integer eigenvalues r_{3/2} and s r_{7/2} are below both carriers by a fixed factor): the spin-5/2 lines have N = L_i and weight (s r_{5/2})^{a L_i}, the spin-1/2 lines have N = 0 and weight r_{1/2}^{a L_i}; N <= n multiplies the exponentially small remainder. In the full ensemble the vacuum has N = 0. QED

Reading. The reference gain of row 875 is not a response spread over the boost interval. It is a switch of the flux carrier from spin 1/2 to spin 5/2, and it is collected only for log s within gamma = 0.010 of log S: the last one per cent of the interval [1, S] in s. Step 3 then says how the magnetic term moves the switch: to second order log s_c(b) = log s_c(0) + 2 (D_{1/2} - D_{5/2}) b^2, about log s_c(0) + 0.103 b^2 at beta = 2.3 (ARGUED beyond b = 0). The switch leaves the interval [1, S] at b*. Extrapolated to b = beta the shift is 0.55 in log s (not reliable there, but 55 times gamma).

**Fact tests.**

| Test | Statement tested | Outcome |
|---|---|---|
| U(1), Coulomb phase | Lemma 3.1, Lemma 3.2 (with charges: a neighbour plaquette moves a charge-q line edge to q +- 1, norms 1/4 and 1/4), Theorem 3.3, Lemma 4.2, (A1)-(A4), Prop 6.1 | All are identities or reference-model facts; they hold verbatim and claim no area law. For a boosted odd charge q >= 3 the same blocking appears (q +- 1 are even, not boosted), and the charge-1 line keeps its detour channel. So the erasure of the reference gain at small b is group-blind. In the Coulomb phase p_1 stays of order one (row 786 for Villain), so J_beta <= log(1/p_min)/a -> 0 and R(beta) = -gamma L_i + o(1): the row-881 bound fails with every theta < 1, as it must. PASS (nothing here survives that should not). |
| Q_8 | same | Q_8 has one odd irrep, so there is no separate boosted carrier and no level crossing; the boost raises the carrier itself (875:142). No claim made. PASS. |
| 2T | same | Odd irreps V, V', V''. With V' or V'' boosted: V x V' = 1' + 3, so a neighbour plaquette (in V) moves a V'-line edge to 1' or 3, both unboosted and of weight below 1; the V-line keeps the free detour (V x V contains 1). Same blocking, same crossing. The magnetic term does not distinguish 2T from SU(2) at this order. PASS (no selection claimed). |
| Selection | "the magnetic bound must carry the selection or not destroy it" | PROVED at second order, ARGUED beyond: the magnetic term removes the reference gain in every one of these groups in the same way. No selection survives from the electric reference. If EXC selects SU(2), the selection sits in delta(beta), the dressing response of the spin-1/2 sheet at isotropic coupling. |
| Dobrushin caps 2/3, 0.775; 4 G_3 = 1.0109; (AN1) | hypothesis of the (A3) consequence | The sub-Gaussian hypothesis on M under the slice law would follow from a uniqueness condition of Dobrushin type. The caps (rows 839, 845) say such conditions are not available at isotropic coupling in the window. So the O(a^{5/2}) consequence of (A3) is conditional there. Recorded, not claimed. |
| Window, first passage | scope | Every statement here is at fixed bare beta in [2.3, 2.6] on the admissible tori. Nothing is claimed along the first-passage trajectory (SEED-FP), READ `D/library/gap-finishline-opus.md` 116-160. |

GUIDE (Monte Carlo check of the amplitudes; script `scratchpad/lane888/scripts/guide_cg.py`, numpy, 4e6 Haar samples, under a minute). Lemma 3.2 (b): j = 1/2: 0.2501(5) and 0.7515(21) against 1/4 and 3/4; j = 5/2: 0.4188(42) and 0.5870(60) against 5/12 and 7/12. Lemma 4.2 (b): 0.193(10) against 3/16. The run agrees with the hand formulas. It discharges nothing.

### Step 7. The obstruction, and the statement that is actually open

**7.1 The obstruction to the row-881 reading (PROVED parts and ARGUED parts kept apart).**
- PROVED: R(b) = J_b - J^el for every b ((22)); J^el = gamma L_i + o(L_i) is a carrier switch in the last one per cent of the boost interval (Prop 6.1); R(0) = R'(0) = 0 and R''(0) = 4 L_i (D_{5/2} - D_{1/2}) + o(1) < 0 on every large torus, every twist (Theorem 3.3, Corollary 4.1). In units of the gain: R''(0)/(gamma L_i) is about -20.6 at beta = 2.3 and -17.9 at beta = 2.6.
- ARGUED: the same expansion holds uniformly in the torus on an interval of b containing b* (the OPEN lemma of Step 4). Then theta(b) = (b/b*)^2 up to O(b^4) for b < b*, and theta(b) = 1 - delta(b)/gamma for b > b*, with delta(b) of order 10^-7 b^8.
- Hence (ARGUED): a bound R(b') >= -theta gamma L_i with one theta visibly below 1 for all b' in [0, beta] fails. At b' just above b* the surviving fraction 1 - theta is of order 10^-9.
- At b' = beta nothing here decides the sign of J_beta. The bound with some theta < 1 is equivalent to EXC-W (Step 4). So the magnetic bound is neither proved nor refuted at the isotropic point; it is the crux in other units, and the electric gain gamma gives no handle on it.

**7.2 The open statement, restated on the right object.** By EXP at b = beta, J_beta = int_1^S Delta_beta(s) ds/s, and Delta splits by carrier. If the spin-5/2 switch stays outside [1, S] at b = beta (ARGUED: it has left at b* and the second-order shift keeps growing), the whole of J_beta is the dressing response:

  (DRESS)  int_1^S sum_e [ P_{s,beta}(j_e high | odd) - P_{s,beta}(j_e high) ] ds/s >= kappa L_i,  kappa > 0, uniformly in tori and twists,

with the odd sector carried by the spin-1/2 sheet for every s in [1, S]. (DRESS) is EXC-W. Its integrand is the excess number of half-integer spin >= 5/2 temporal plaquettes that the fundamental flux sheet carries over the vacuum.

**7.3 Is (DRESS) plausible? (ARGUED, order of magnitude; the sign is not established at beta.)**
- Sign at small spatial coupling: positive. A sheet plaquette needs four more half-units to reach spin 5/2, a vacuum plaquette five (Lemma 4.2). The same counting holds in the full strong-coupling expansion.
- Scale in the window: READ 872:94-95 (GUIDE there: 8^4 heat bath, one seed, beta = 2.3): one-slice densities 0.327 (spin 1/2), 1.3e-3 (spin 3/2), below 6e-7 (odd spin >= 5/2). The unconditional high density is tiny, so the response should be linear in s up to S: J_beta is about (S - 1) Delta_beta(1). If the excess high density per unit sheet length at s = 1 lies between the 5/2 and the 3/2 vacuum densities (geometric mean 3e-5), then J_beta/L_i is of order 262 x 3e-5 = 8e-3, comparable with gamma = 0.010 by accident of the large S. This guess can be wrong by a factor of ten either way.
- What it would take: a local positive lower bound on the high-spin excess of a fundamental flux sheet at order-one coupling. That is a statement about the sheet in the true isotropic measure; it contains the area law (Step 2).
- A numeric GUIDE that would inform it (not run here; beyond a few minutes): the s = 1 density of high temporal plaquettes inside a large Wilson loop's flux sheet against the vacuum density. Twisted-minus-untwisted differences are of size p and cannot be measured directly.

**7.4 What the electric reference still gives.** The reference result (16) stands. It tests the scale of EXP's identity in an exactly solvable model. It does not seed a continuation in b: the carrier it relies on is rigid under the magnetic term (blocked neighbours, D_{5/2} < 0), the true carrier is flexible (D_{1/2} > 0), and the two cross at b* near 0.3.

GUIDE (check of formula (S1); script `scratchpad/lane888/scripts/guide_s1.py`, random positive diagonal K and symmetric M with zero diagonal, sizes 2, 5, 6, a = 3, 4, 7). Finite-difference second derivative of log Tr((e^{bM/2} K e^{bM/2})^a) at b = 0 against the trace formula and against the pair form with g_a: 3.79185 / 3.79185 / 3.79185; 54.8469 / 54.8473 / 54.8473; 54.2927 / 54.2930 / 54.2930. The formula with its factor a and g_a is right. Discharges nothing.

### Step 7b. An exact carrier dichotomy, valid at every b (PROVED)

Notation. Q_0 = 1{N = 0} (no high edge in the slice), Q_1 = 1 - Q_0. L = L_{S,b}. L(0) is the s = 0 operator of EXP (every high block removed); K(0) = K_1 Q_0, so Q_0 L_{S,b} Q_0 = Q_0 L_{1,b} Q_0 = L_{0,b}. Put

  t_1(S,b) := Tr( P_- (Q_1 L_{S,b} Q_1)^a ),

the odd trace of the boosted model with at least one high edge at every one of the a time steps.

**Proposition 7.5 (PROVED).** For every torus, twist, b >= 0, S >= 1:

  max( Z_-(0,b), t_1(S,b) ) <= Z_-(S,b) <= ( Z_-(0,b)^{1/a} + t_1(S,b)^{1/a} )^a <= 2^a max( Z_-(0,b), t_1(S,b) ),      (H1)

  e^{J_b} = (p_{S,b}/p_{1,b})^{1/a} <= 1 + ( t_1(S,b) / Z_-(1,b) )^{1/a}.                                              (H2)

Moreover, with tau_e(S,b) := Tr( P_- (H_e L_{S,b} H_e)^a ) (edge e high at all a time steps): t_1^{1/a} <= sum_e tau_e^{1/a}.     (H3)

*Proof.* Put Y_q = L^{1/2} Q_q L^{1/2} >= 0 for q = 0, 1; Y_0 + Y_1 = L; both commute with P_-. Then Tr(P_- L^a) = sum over words q in {0,1}^a of Tr(prod_i (Y_{q_i} P_-)). Hoelder's inequality for Schatten norms gives |Tr(X_1 ... X_a)| <= prod ||X_i||_a, and ||Y_q P_-||_a^a = Tr(P_- (L^{1/2} Q_q L^{1/2})^a) = Tr(P_- (Q_q L Q_q)^a) (the nonzero spectra of X X^* and X^* X agree). The q = 0 value is Tr(P_- L_{0,b}^a) = Z_-(0,b). Summing the words gives the middle bound of (H1). Lower bounds: L^{1/2} Q L^{1/2} <= L for a projection Q, and X <= Y implies Tr X^a <= Tr Y^a (eigenvalues are ordered by min-max); apply on the odd sector. For (H2): Z(S,b) >= Z(1,b) and Z_-(0,b) <= Z_-(1,b) (EXP (d)), so p_S^{1/a} <= (Z_-(S,b)/Z(1,b))^{1/a} <= p_1^{1/a} + (t_1/Z(1,b))^{1/a}; divide by p_1^{1/a}. For (H3): Q_1 = sum_e Q^{(e)}, Q^{(e)} the projection "e is the first high edge" in a fixed order; these are orthogonal projections below H_e, commuting with P_-. Repeat the Hoelder step with the Q^{(e)} and use the same compression bound, Tr(P_- (Q^{(e)} L Q^{(e)})^a) <= tau_e. QED

Reading.
- (H1) is the rigorous form of "the odd sector splits by carrier". Up to log 2 per time step, the boosted odd trace is either the trace that never uses a high spin (and that one is at most the unboosted odd trace) or the trace that uses one at every step.
- (H2) bounds the EXC gain at every b, including b = beta, by the always-high odd trace relative to the unboosted odd trace. At b = 0 it is sharp: t_1 is carried by the spin-5/2 lines, (t_1/Z_-(1,0))^{1/a} = e^{gamma L_i}(1 + o(1)), and (H2) returns J^el <= gamma L_i + log(1 + e^{-gamma L_i}) + o(1).
- With (H3): J_b <= log(1 + sum_e (tau_e/Z_-(1,b))^{1/a}). On one torus, a crude one-sided estimate tau_e(S,b) <= C^a Z_-(1,b) for each edge e would give J_b <= log(1 + C n) = O(log a). For the spin-5/2 line through e the estimate reads sigma_{5/2}(b) >= sigma_{1/2}(b) - (log C)/L_i: the crossing inequality, with room.
- Caution (PROVED remark). (H2) uses Z(S,b) >= Z(1,b), so t_1/Z_-(1,b) contains the vacuum's own boost response Z(S,b)/Z(1,b) = exp(a int_1^S n_all ds/s). That factor is extensive in n, with a tiny density. So the estimate above cannot hold with one C for all tori; it is a statement for tori on which n times the vacuum high density stays bounded. For a statement uniform in tori, compare inside one model. The same Hoelder step, divided by Z(S,b) >= Z(0,b), gives

  p_{S,b}^{1/a} <= p_{0,b}^{1/a} + ( t_1(S,b)/Z(S,b) )^{1/a},                                                    (H0)

with p_0 the odd fraction of the high-free model (s = 0). Then the level crossing, in the form J_b = O(log a) above b*, follows from two relative estimates: t_1(S,b)/Z(S,b) <= C^a p_{0,b} (odd always-high histories of the boosted model are at most C^a times as likely as odd histories of the high-free model) and p_{0,b} <= C^a p_{1,b}. Both are OPEN. Each bounds, at order one per time step, a difference of high-spin populations between the odd sector and the vacuum; this is the same relative control as the OPEN lemma of Step 4, one-sided and with exponential room in a.
- (H2) does not obstruct EXC-W at b = beta: when the flux sheet carries many high edges per slice (expected number of order L_i times a small density, large for large tori), t_1 is comparable to Z_-(S,b) and (H2) is trivial. It only says where a gain can come from.

### Step 8. Final statement

Plan note. Steps 4 and 5 of the plan (the two attacks) are merged in Step 5 of the log; Step 4 of the log holds the small-b consequences; Steps 7b, 9 and 9b were added. No subagent was used. No repository file was edited. Six small scripts, all GUIDE, sit in `scratchpad/lane888/scripts/` (guide_coeffs.py, guide_cg.py, guide_s1.py, guide_zn.py, guide_cross.py, guide_cross2.py).

Credits. The Bessel spectrum r_j = I_{2j+1}/I_1 of the one-link kernel and its factorial decay are GL3-GL4 of the Sussman-Alpoge account (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text), used here only as READ through rows 875 and 881; I did not open the account's sources. EXP, EXC and Prop 3.2 are row 872 (Claude Opus 5.5) with the corrections of row 873 (OpenAI Codex). Identity (22), the electric reference (14)-(20), the crude bound (21), the sign-changing kernel (7) and sector monotonicity are row 875 (OpenAI Codex), checked in row 881 (Claude Opus 5.5). No estimate of Balaban is used. The Ginibre and Seiler facts in Step 5 are recalled from the literature, marked as such, and carry nothing.

**What is PROVED here (by hand, one author, not checked by another model).**
1. (M1)-(M3): the integrated magnetic response of each s is (1/a) log(p_{s,b}/p^el_s); it is at most (-log q_s) L_i + o(1). R(b) = J_b - J^el.
2. Lemma 3.1, Lemma 3.2, Theorem 3.3: d^mag_{s,0} = 0; the second-order response is 4 L_i D_{1/2} + o(1) at s = 1 and 4 L_i (pi_5 D_{5/2} + pi_1 D_{1/2}) + o(1) at s = S, with D_{1/2} = (1/16) v(r^2) + (3/16) v(r_1 r^2) - (1/4) v(r^4) > 0 and D_{5/2} = (5/48) v(x_2) + (7/48) v(x_3) - (1/4) v(r^4) < 0, v(x) = (1+x)/(1-x). It is twist-independent and of order L_i exactly. So R(0) = R'(0) = 0 and R''(0) = 4 L_i pi_5 (D_{5/2} - D_{1/2}) + o(1): -0.207 L_i at beta = 2.3, -0.268 L_i at beta = 2.6, about -20 gamma L_i.
3. Corollary 4.1: on each large torus, for small b > 0, the unboosted odd fraction rises with b, the boosted one falls, and R(b) < 0. Lemma 4.2: a high edge costs four plaquettes on a spin-1/2 line and five in the vacuum; the four-plaquette amplitude is 3/4096.
4. Proposition 6.1: in the electric reference the EXC integrand is a step, L_i 1{s > s_c} with log(S/s_c) = gamma. The reference gain is a carrier switch in the last one per cent of the boost interval.
5. (A1), (A2), (A3), (A4): twist form; slice-conditional form and the entropy bound; the lower bound p >= min(1/2, G(a/2)^2/128) with log-convex G; R(b) >= (1/a) log p_{S,b} - J^el.
6. Proposition 7.5: the exact carrier dichotomy (H1) and the bounds (H2), e^{J_b} <= 1 + (t_1(S,b)/Z_-(1,b))^{1/a}, and (H0), p_{S,b}^{1/a} <= p_{0,b}^{1/a} + (t_1(S,b)/Z(S,b))^{1/a}, at every b.
7. The equivalence: a theta < 1 uniform over tori at b = beta exists iff liminf (1/(a L_i)) log(p_{S,beta}/p_{1,beta}) > 0 (EXC-W).

**What is ARGUED.**
- The level crossing: uniformly in the torus, sigma_{1/2}(b) = -log r - 2 D_{1/2} b^2 + O(b^4) and sigma_{5/2}(b) = -log q_S - 2 D_{5/2} b^2 + O(b^4), crossing at b* = 0.312 (beta = 2.3) to 0.335 (beta = 2.6). Beyond b* the boosted odd sector is carried by the spin-1/2 sheet and the electric gain is gone.
- The dressing response delta(b) = c_8 b^8 (1 + O(b^2)) with c_8 > 0 of order 10^-7 to 10^-6; so theta(b) = 1 - delta(b)/gamma just above b*.
- At b = beta the switch stays outside [1, S]; J_beta is the dressing response (DRESS). Its order of magnitude in the window may be 10^-3 to 10^-2 per unit area; its sign is not established there.
- Group-blindness of the erasure (U(1) with a boosted odd charge, 2T with V' or V'' boosted).

**What is GUIDE.** The decimals of the tables; the Monte Carlo check of the amplitudes; the finite-difference check of (S1); the Z_6 end-to-end check and the Z_6 level-crossing run (after Step 9b). None is a premise.

**What is OPEN.**
- The magnetic bound at b = beta, in any form with theta < 1. It is EXC-W; this note gives no bound for it and no counterexample.
- A uniform expansion in b near 0 through b*, or the two one-sided relative estimates of Step 7b (below (H0)). Either would make the level crossing PROVED.
- A finite flux tension of the boosted model, p_{S,beta} >= e^{-C a L_i}, which is what an order-L_i lower bound on R with any constant needs (5.4 (d)).
- (DRESS): a positive excess, of order L_i, of half-integer spin >= 5/2 temporal plaquettes on the fundamental flux sheet at isotropic coupling.

**Answers to the brief's questions.**
- Is order L_i plausible? Yes. The integrated response is a difference of flux free energies; it is bounded above by (-log q_s) L_i for free, and it is of order L_i at second order by locality of the flux carrier (only the 4 L_i neighbours of the line respond). Below, order L_i with some constant is the finite flux tension of the boosted model.
- Does the bound hold with theta < 1? Near b = 0 it holds with theta(b) = (b/b*)^2 at second order. The electric gain is used up at b* near 0.3, far below beta. After that the bound holds exactly when the spin-1/2 sheet's own dressing response is positive (ARGUED), and then with theta within 10^-7 of 1 at small b. At b = beta it is the crux itself.
- Selection. The magnetic term does not carry the SU(2) selection from the electric reference; it removes the reference gain in the same way for U(1) and 2T analogues. Selection, if any, sits in (DRESS).
- Why the boosted carrier loses: V_j x V_{1/2} contains the trivial representation only for j = 1/2. A fundamental plaquette can move a spin-1/2 line (detour channel, weight ratio r^2 = 0.23 to 0.27) but turns an edge of any higher half-integer line into an integer spin, which the boost does not reach. So every boosted half-integer carrier is rigid under the Wilson magnetic term, and it blocks the vacuum fluctuation of its neighbours.

(The RESULT line is at the end of the file, after Step 9, which was added after this summary.)

### Step 9 (added). Finite flux tension of the unboosted model, every twist, explicit constant (PROVED); the exact inequality missing for the boosted model

Fix a straight winding line l in direction i. Split M = M_l + M_notl: M_l is the sum over the 4 L_i spatial plaquettes that contain an edge of l (so |M_l| <= 4 L_i pointwise, whatever the twist signs), and M_notl does not involve the edges of l. Let H_0^l be the subspace of H of states that do not depend on the edges of l (spin 0 on l). K and e^{b M_notl} map H_0^l into itself. Put L^(l) = K^{1/2} e^{b M_notl} K^{1/2} restricted to H_0^l: the transfer operator of the lattice with l deleted. Z^(notl) = Tr (L^(l))^a, with sectors Z^(notl)_+-  for the flip of the remaining cut edges.

**Lemma 9.1 (PROVED; any s, any b >= 0, any twist).** For a carrier spin c (half-integer) with one-link weight w_c:

  Z_-(s,b) >= w_c^{a L_i} Z^(notl)_+(s,b).

*Proof.* W Psi = chi_c(U_l) Psi is an isometry from H_0^l into H (U_l is Haar and independent of the other edges). It anticommutes with the cut flip, so it maps the even part of H_0^l into P_- H. K^{1/2} W = w_c^{L_i/2} W K^{1/2} on H_0^l (each edge of l is in its spin-c block). For Phi in H_0^l: <W Phi, e^{bM} W Phi> = int |Phi|^2 e^{b M_notl} I, with I = int e^{b M_l} d nu and d nu = |chi_c(U_l)|^2 prod_{e in l} dU_e, a probability measure on the edges of l. Under nu each single edge of l is Haar distributed (L_i >= 2), so int x(U_p) d nu = 0 for each of the 4 L_i plaquettes of M_l, and Jensen gives I >= exp(b int M_l d nu) = 1, for every configuration of the other edges. So <W Psi, L W Psi> >= w_c^{L_i} <Psi, L^(l) Psi> on H_0^l. Compression and monotonicity of Tr X^a (as in Prop 7.5) give the claim. No factor is lost. QED

**Lemma 9.2 (PROVED; s = 1 only).** Z(1,b) <= e^{4 a b L_i} (1 + eps_1(a))^{L_i} Z^(notl)(1,b), and Z^(notl)_+(1,b) >= Z^(notl)(1,b)/2.

*Proof.* At s = 1 the trace is the integral of a positive density over spatial and temporal links. Bound each of the 4 a L_i spatial plaquette factors that touch l by e^b. The variables U_e(t), e in l, now occur only in the temporal plaquettes over e. Integrating them out is character algebra: for each e in l the chain around the time circle gives sum_j w_j^a chi_j(P_x) chi_j(P_y), with P_x, P_y the temporal holonomies at the endpoints of e; this is at most 1 + sum_{j>0} d_j^2 w_j^a = 1 + eps_1(a). What remains is the positive density of the lattice with l deleted. The second claim: Z_+ - Z_- of the deleted lattice is its twisted partition function, an integral of a positive density (k(-U) = e^{-beta x}/z > 0). QED

**Theorem 9.3 (PROVED).** For every admissible torus, every spatial twist, every b >= 0:

  p_{1,b} >= (1/2) (1 + eps_1(a))^{-L_i} ( r_{1/2}(beta) e^{-4b} )^{a L_i}.

Hence, with (M3) and (19):  -4 b L_i - 2 log(12 C a^3) - o(1) <= int_0^b d^mag_{1,b'} db' <= (-log r_{1/2}) L_i + o(1).

So the integrated magnetic response of the unboosted model is of order L_i on both sides, uniformly in tori and twists, with explicit constants. This is a two-sided bound of the right order; (21) gave 2 b n. It is the rigorous form, in the transfer picture and with twists, of "the area law is the fastest possible decay". The constant 4b is crude (Lemma 9.2 uses only |M_l| <= 4 L_i); the true shift is of order b^2 and has the other sign (Theorem 3.3).

**Consequence for R (PROVED).** R(b) <= J_b <= (1/a) log(1/p_{1,b}) <= (-log r_{1/2} + 4b) L_i + O(log a). This is the upper side. EXC needs the lower side.

**What is missing for the lower side (OPEN, named exactly).** By Lemma 9.1 with c = 5/2, Z_-(S,b) >= q_S^{a L_i} Z^(notl)_+(S,b). A bound p_{S,b} >= e^{-C a L_i}, and with it R(b) >= -(C + gamma) L_i - o(L_i), would follow from

  (VAC-S)   Z(S,b) <= C_1^{a L_i} Z^(notl)_+(S,b):   deleting one line costs the boosted partition function at most a factor C_1 per unit area.

At s = 1 this is Lemma 9.2, proved by pointwise positivity. At s = S the density is not positive (875 (7)). In operator form the proof needs "a sector with static charges at the vertices of l has trace at most a constant per charge times the neutral trace"; for a positive gauge-invariant operator this is false in general and true when the kernel is positive. So (VAC-S) is a genuine statement about the boosted model. It is the same obstruction as 5.4 (c).

Equivalent wording through EXP (PROVED rearrangement): J_b = int_1^S (1 - p_s)(n_-(s) - n_+(s)) ds/s at spatial coupling b. A bound n_-(s) - n_+(s) >= -C_2 L_i on [1, S] (the odd sector excludes at most C_2 L_i of the vacuum's high edges per slice) gives J_b >= -C_2 L_i log S, hence R(b) >= -(C_2 log S + gamma) L_i - o(L_i). EXC-W asks for the opposite sign on average, n_- - n_+ >= +kappa' L_i. Both say that the flux sheet changes the high-spin population only near itself, by an amount of order L_i: the first bounds the exclusion, the second asks for a net excess. Neither is proved at b = beta.

### Step 9b (added). The boosted lower bound reduced to a one-slice probability (PROVED reduction; the probability bound is OPEN)

**Proposition 9.4 (PROVED; every s, every b >= 0, every twist, every half-integer carrier c).** Let pi_0^+(s,b) := Tr(Pi_0^l P_+ L_{s,b}^a)/Tr(L_{s,b}^a), the probability in the one-slice law (a genuine probability law, 873:128-131) that every edge of the straight line l has spin 0 and the sector is even. Then

  p_{s,b} >= ( w_c^{L_i} e^{-4 b L_i} pi_0^+(s,b) )^a.                                            (FT)

*Proof.* Put Pi = Pi_0^l P_+, a projection. Hoelder: Tr(Pi L^a) = Tr((L^{1/2} Pi L^{1/2}) L ... L) <= [Tr((Pi L Pi)^a)]^{1/a} [Tr L^a]^{1-1/a}. So Tr((Pi L Pi)^a) >= (pi_0^+)^a Z. Next, Pi_0^l commutes with K and with e^{b M_notl}, and e^{bM} <= e^{4 b L_i} e^{b M_notl}; hence Pi L Pi <= e^{4 b L_i} P_+ L^(l) P_+ on H_0^l, and Tr((Pi L Pi)^a) <= e^{4 a b L_i} Z^(notl)_+. Lemma 9.1 gives Z_- >= w_c^{a L_i} Z^(notl)_+. Chain the three. QED

So a finite flux tension of the boosted model, and with it an order-L_i lower bound on R with some constant, follows from

  (EMPTY)   pi_0^+(S,beta) >= c_3^{L_i}:  in one slice of the boosted model, a given straight line is empty, in the even sector, with probability at least c_3 per edge.

Then p_{S,beta} >= (q_S e^{-4 beta} c_3)^{a L_i} and R(beta) >= -(log(1/c_3) + 4 beta - log q_S + gamma) L_i - o(L_i).

Status of (EMPTY). At s = 1 it holds with c_3 close to z e^{-beta} (about 0.18 at beta = 2.3): by Lemma OS (READ 872:57-58), P(l empty) = E[prod_{e in l} 1/k_beta(U_{p(e)})] >= (z e^{-beta})^{L_i}, a pointwise bound in a positive measure (and either p or pi_0^+ is at least half of that). At s = S it is OPEN. The same pointwise argument fails because the boosted density is signed; the kernel inequality 1 >= k_S/k_S(1) is true pointwise but is not an operator inequality (Pi_0 has rank one). (EMPTY) is a cleaner target than (VAC-S): it asks for a lower bound on the probability of one event in a probability law. It implies (VAC-S) by the Hoelder step above.

Ordering of the open statements (PROVED implications): (EMPTY) implies p_{S,beta} >= e^{-C a L_i}, which implies R(beta) >= -C' L_i. EXC-W (the row-881 bound with theta < 1) is strictly more: it needs the sign and size of (DRESS).

GUIDE (end-to-end check of the bookkeeping of Theorem 3.3 in an abelian analogue; script `scratchpad/lane888/scripts/guide_zn.py`, numpy, under 100 MB; 2 s for the 3 x 2 torus, 90 s for 4 x 2). Z_6 gauge theory on a two-dimensional spatial torus, electric basis (plaquette heights and windings), one-link weights w = (1, 0.48, 0.17, w_3, 0.17, 0.48), carrier charge 1, boosted charge 3, a = 14. The exact sum (S1) over all gauge-invariant configurations is compared with the dominant-class formula 2 L_x (pi_1 D_1 + pi_3 D_3) (two neighbour plaquettes per line edge in two dimensions; abelian amplitudes 1/4 and 1/4). Odd-minus-all values of (1/a) F'': 3 x 2 torus: +0.68406 / +0.68406 (w_3 = 0.0018), +0.34475 / +0.34475 (w_3 = 0.485, mixture pi_3 = 0.436), -0.14213 / -0.14213 (w_3 = 0.60); 4 x 2 torus: +0.91208 / +0.91208, +0.42236 / +0.42236, -0.18969 / -0.18969. Exact and predicted agree to five decimals. The unboosted carrier gains (D_1 = +0.114) and the boosted carrier loses (D_3 = -0.016 to -0.024), as in SU(2). This checks the counting, the factor g_a, the mixture and the signs; it discharges nothing.

GUIDE (the level crossing to all orders in b, in the abelian analogue; script `scratchpad/lane888/scripts/guide_cross2.py`, numpy, 6 s, under 50 MB). Same Z_6 model on the 3 x 2 torus, weights w = (1, 0.48, 0.17, w_3, 0.17, 0.48) with w_3 = 0.0018 (s = 1) or 0.485 (s = S), so gamma' = log(0.485/0.48) = 0.01036. In an abelian model the two carriers live in different winding sectors (charge 1 in m_x = 1, charge 3 in m_x = 3), so each tension is a ratio of top eigenvalues of L = K^{1/2} e^{bM} K^{1/2} (Lanczos, time period infinite): sigma_c = -(1/L_x) log(lambda_max(m_x = c)/lambda_max(0)).

| b | sigma_1 (s = 1) | sigma_1 (s = S) | sigma_3 (s = S) | second-order sigma_3 | J/L_x = sigma_1(1) - min(sigma_1, sigma_3)(S) | over gamma' |
|---|---|---|---|---|---|---|
| 0.00 | 0.73397 | 0.73397 | 0.72361 | 0.72361 | +0.010363 | 1.000 |
| 0.10 | 0.73255 | 0.73255 | 0.72376 | 0.72376 | +0.008789 | 0.848 |
| 0.20 | 0.72726 | 0.72726 | 0.72423 | 0.72424 | +0.003032 | 0.293 |
| 0.25 | 0.72276 | 0.72275 | 0.72457 | 0.72459 | +0.000003 | 0.0003 |
| 0.30 | 0.71689 | 0.71688 | 0.72499 | 0.72502 | +0.000007 | 0.0007 |
| 0.50 | 0.68028 | 0.68023 | 0.72729 | 0.72754 | +0.000053 | 0.005 |
| 1.00 | 0.55205 | 0.55127 | 0.73486 | 0.73934 | +0.000773 | 0.075 |
| 1.50 | 0.46588 | 0.46346 | 0.72005 | 0.75900 | +0.002419 | 0.234 |
| 2.30 | 0.41194 | 0.40720 | 0.59741 | 0.80683 | +0.004744 | 0.458 |

What the run shows, for the analogue only. (i) The boosted carrier's tension rises with b and follows the second-order formula -log w_3 - D_3 b^2 (D_3 = -0.0157) to four decimals up to b = 0.3. (ii) The charge-1 carrier's tension falls, faster than its second-order term on this small torus (whole-line hopping enters at order b^3 for L_x = 3). (iii) The carriers cross between b = 0.20 and 0.25 (second-order estimate 0.28). At the crossing the gain collapses from 0.29 gamma' to 0.0003 gamma'. (iv) Beyond the crossing J/L_x is the dressing response of the charge-1 carrier: positive, tiny at first, and growing with b to 0.46 gamma' at b = 2.3. In this analogue a boosted charge is two plaquettes away from the carrier (order b^4); in SU(2) spin 5/2 is four plaquettes away from spin 1/2 (order b^8), so the SU(2) dressing response starts much smaller. (v) The crossing is not undone at larger b: sigma_3 stays far above sigma_1. A dense finite-time run on the 2 x 2 torus (script `guide_cross.py`, a = 600) shows the same collapse, from 0.94 gamma' at b = 0 to 0.0001 gamma' at b = 0.20, and the same regrowth. This supports the ARGUED picture of Steps 4 and 7 and its group-blindness. It is a different model (abelian, two space dimensions, six sites) and discharges nothing for SU(2).

Remark (ARGUED, not written out). In Lemma 9.2 a two-block bound on each edge chain (constants against their complement, with off-diagonal norm of order b) should replace the factor e^{4b} per unit area by 1 + C b^2 for small b. The lower bound of Theorem 9.3 would then be quadratic in b. Its sign would still be the crude one.

### Final statement, updated after Step 9 (this replaces the lists of Step 8 where they differ)

Added to PROVED: 8. Lemma 9.1 (for every s, twist and b: Z_-(s,b) >= w_c^{a L_i} Z^(notl)_+(s,b), by an isometry and Jensen), Lemma 9.2 and Theorem 9.3: p_{1,b} >= (1/2)(1 + eps_1(a))^{-L_i} (r_{1/2} e^{-4b})^{a L_i} for every torus, twist and b >= 0. So the unboosted integrated response obeys -4 b L_i - O(log a) <= int_0^b d^mag_1 <= (-log r_{1/2}) L_i + o(1), and R(b) <= (-log r_{1/2} + 4b) L_i + O(log a).

Added to PROVED: 9. Proposition 9.4, p_{s,b} >= (w_c^{L_i} e^{-4 b L_i} pi_0^+(s,b))^a for every s, b, twist.

Added to OPEN: (EMPTY) for the boosted model (a given line is empty in one slice with probability at least c_3^{L_i}); it implies (VAC-S) and a lower bound R >= -C L_i. A sufficient alternative is the exclusion bound n_- - n_+ >= -C_2 L_i on [1, S]. The proofs at s = 1 use pointwise positivity of the density, which the boosted kernel lacks.

Status of the target in one table:

| Statement | Status |
|---|---|
| int_0^b d^mag_s db <= (-log q_s) L_i + o(1), each s, every b | PROVED (M3) |
| int_0^b d^mag_1 db >= -4 b L_i - O(log a), every b, every twist | PROVED (Theorem 9.3) |
| R(b) <= (-log r_{1/2} + 4b) L_i + O(log a) | PROVED |
| R(0) = R'(0) = 0, R''(0) = 4 L_i pi_5 (D_{5/2} - D_{1/2}) + o(1) < 0 | PROVED (Theorem 3.3), per torus as a -> infinity |
| R(b) >= -C L_i, some constant C, at b = beta | OPEN; follows from (EMPTY) by Prop 9.4 (PROVED reduction), or from (VAC-S), or from the exclusion bound |
| R(b) >= -theta gamma L_i, theta(b) = (b/b*)^2, for b < b* | ARGUED (second order; GUIDE support from the Z_6 analogue); needs the uniform expansion |
| R(b) >= -theta gamma L_i with a fixed theta visibly below 1, all b in [0, beta] | fails, ARGUED: theta(b) is within about 10^-7 of 1 for b between b* = 0.31 to 0.34 and 1/2 |
| R(beta) >= -theta gamma L_i, some theta < 1 (row 881) | OPEN; equivalent to EXC-W, that is to (DRESS) if the carrier switch stays outside [1, S] |

RESULT: OPEN at the isotropic point — the magnetic bound R(beta) >= -theta gamma L_i with theta < 1 is the area form EXC-W in other units (PROVED equivalence); it is neither proved nor disproved, and the reduction to a fraction of the electric gain does not survive (ARGUED from PROVED second-order data). PROVED: R(0) = R'(0) = 0 and R''(0) = 4 L_i pi_5 (D_{5/2} - D_{1/2}) + o(1) < 0, about -20 gamma L_i, twist-independent and of order L_i by locality; the electric gain is a carrier switch confined to the last one per cent of the boost interval; int_0^b d^mag_s <= (-log q_s) L_i + o(1) for each s; for s = 1 also >= -4 b L_i - O(log a) on every torus and twist (finite flux tension, p_{1,b} >= (1/2)(1+eps)^{-L_i}(r_{1/2} e^{-4b})^{a L_i}); the carrier dichotomy e^{J_b} <= 1 + (t_1(S,b)/Z_-(1,b))^{1/a} and the reduction p_{s,b} >= (w_c^{L_i} e^{-4 b L_i} pi_0^+)^a hold at every b. ARGUED: the spin-5/2 and spin-1/2 carriers cross at b* = 0.31 to 0.34 and the gain gamma L_i is erased there, in the same way for U(1) and 2T analogues; beyond b* the value of theta rests on the dressing response of the fundamental sheet (order 10^-7 b^8 at small b; sign and size unknown at beta). GUIDE: an exactly diagonalized Z_6 analogue shows the same crossing (gain 0.29 gamma' at b = 0.20, 0.0003 gamma' at b = 0.25) and a positive dressing response after it. OPEN: the uniform small-b expansion (or the two relative estimates below (H0)); (EMPTY) for the boosted model, which would give an order-L_i lower bound with some constant; and (DRESS), which is the crux.
