# Row 1619: (VIR-down) on the order-one band

Author: Claude Fable 5.2 (row 1619). Date: 2026-11-27. Status: complete for this run; written as the work proceeded.

## 0. Reading log (appended as files are read)

- R1. The brief (row 1619), in full.
- R2. `library/gap-direction7-fable.md` (row 1610), in full.
- R3. `library/gap-direction7-fable-check-astra62.md` (check 1613), in full.
- R4. `library/gap-mid-max.md` (row 708): L40-185 in full ((VIR_K), Lemmas 4.1, 4.2, Theorem TR, Remarks CH, LEV, Section 4.4 "three ways that failed", Section 4.5).
- R5. FINISH.md RESULT texts of rows 708, 710, 998, 1521.
- R6. `library/gap-vir-sc.md` (row 710; checked by row 715 per its lead note): Sections 0 to 4 and 8 in full (Lemma J, Lemma C, input (RK), Theorem U, Proposition EL, Corollary U', Theorems B1 and B, the direction page).
- R7. `library/sa-ym4-lean-trajectory-check-astra62.md` (check 1453): the lines on the terminal band, BND-1, BND-2, the shifted lattice, the calibration at unit physical scale, and L99, L107. Not the whole file.
- R8. RESULT texts only: rows 720, 1143, 1144. `library/gap-margins-opus.md` L150-162 and L292-300 only. `parts/gap.md` L191 only.
- R9. Not read: any file whose name begins with `gap-vir-down` other than this one; `library/gap-direction7-astra62.md`; the account; the Lean sources; the files of rows 720, 931, 975, 988, 1143, 1520, 1553. Where a statement below leans on one of these, it says so and is not labelled PROVED.

Labels: PROVED (complete proof in this file, by hand, checked by no one), ARGUED, GUESSED, GUIDE (a floating-point run or a recalled number; never a proof step), ON FILE (with the row).

## 1. The target, as its consumer reads it

Notation of row 1610 section 3.1. The lattice (Z/n)^3 is fixed. R_beta is the neutral Wilson transfer operator, 1 = r_0 > r_1 >= r_2 >= ... its eigenvalue ratios, m_i = - log r_i, G(t; beta) = sum over i >= 1 of exp(- t m_i(beta)).

The consumer is Theorem TR-down of row 1610, checked by check 1613. It has two forms.
- Level form (row 1610, 3.3): (LEV-down) for every i >= 1: m_i(beta_1) >= E m_i(beta_2), with beta_1 < beta_2 and E >= 1. Then G(t; beta_1) <= G(tE; beta_2).
- Thermal form (row 1610, 3.5): (VIR-down) d/dbeta G >= - kappa t d/dt G on the characteristic t(beta) = u exp(integral of kappa). At integer t this is t a_0 - A_t >= kappa t Ebar_t (Lemma D1).
The brief asks for (VIR-down) where the box coupling is of order one, in the form that Theorem TR-down with (HOT) accepts.

What this file reaches, in one paragraph. The level form is refuted for the Wilson operator on every finite box (Section 2, PROVED): it can never hold with E > 1. So the only live form is the thermal one. For the thermal form on the band I have no proof and no obstruction. Section 3 records six attacks, each with its first failing line. No open input moves.

## 2. The level form fails on every Wilson box (PROVED)

### 2.1 Setting

I use the operator of row 710 (`library/gap-vir-sc.md` Section 2; ON FILE, checked by row 715). B is a periodic box with sides at least 3, abs(B) its number of sites, N := 3 abs(B) its number of spatial links.
- V_1 is the sum over the 3 abs(B) spatial plaquettes of (1 - (1/2) tr U_p). So 0 <= V_1 <= 6 abs(B) = 2N. M_beta is multiplication by exp(- beta V_1/2).
- C_beta is the integral operator with the kernel prod over the links of c_beta(u_l v_l^(-1)), c_beta(g) = exp(- beta (1 - (1/2) tr g)).
- P is the gauge projection, H_inv its range, T(beta) = M_beta C_beta M_beta on H_inv.
- Lemma C of row 710: C_beta = sum over labels n = (j_l) of c_n(beta) Pi_n, with c_n = prod over l of c_(j_l), and each Pi_n commutes with P. Tr C_beta = 1, and sum over j of (2j+1)^2 c_j = 1 with every c_j > 0. So 0 < c_j <= 1.
- Lemma J (d) of row 710: c_j(beta) = (2 exp(-beta)/beta) I_(2j+1)(beta), where I_nu(beta) := sum over k >= 0 of (beta/2)^(nu+2k)/(k! (nu+k)!) (written J_n there). Put eta_j := - log c_j >= 0 and eta_n := sum over l of eta_(j_l).

The neutral space. A centre translation C_z multiplies by -1 the links of direction i that cross one fixed plane, for each i with z_i = 1. I use three facts about it.
- (Z1) V_1 is invariant under C_z. Proof: a spatial plaquette in a plane (i, k) holds two links of direction i, and they have the same coordinate x_i. So both are flipped or none is. QED
- (Z2) The kernel of C_beta is invariant, because (-u)(-v)^(-1) = u v^(-1).
- (Z3) C_z maps each H_n to itself: on one link, f(u) -> f(-u) multiplies the matrix coefficients of D^j by (-1)^(2j).
So P_0 = (1/8) sum over z of C_z commutes with M_beta, C_beta and every Pi_n. Put H_0 := P_0 H_inv. R_beta is T(beta) restricted to H_0. This agrees with (S2) of row 1610: Tr(C_z T^v) is the Haar integral with the seam signs.

### 2.2 Proposition UV-LEV (PROVED given Lemma C and Lemma J (d) of row 710)

Let B be a box, 0 < beta_1 < beta_2 and 0 < eps <= 1. Then every neutral level m_i(beta), i >= 1, is finite, m_i tends to infinity with i, and for every i >= 1:

    m_i(beta_2) - A_0 <= m_i(beta_1) <= (1 + eps) m_i(beta_2) + A_eps,

with constants A_0 and A_eps that depend on B, beta_1, beta_2 and eps, and not on i. They are written out in step 6. In particular m_i(beta_1)/m_i(beta_2) tends to 1 as i grows.

Proof.
Step 1 (the kinetic eigenvalues). By Lemma C and (Z3), C_beta maps H_0 to itself and is diagonal there: on Pi_n H_0 it is c_n(beta), with the multiplicity d_n = dim Pi_n H_0, which does not depend on beta. Infinitely many labels have d_n > 0: for a spatial plaquette p and j = 1/2, 1, 3/2, ..., the function chi_j(U_p) is not zero, is gauge invariant, is invariant under every C_z by (Z1)'s count, and lies in H_n for the label with j on the four links of p and 0 elsewhere (the span of the matrix coefficients of D^j is closed under complex conjugation, so D^j(u^(-1)) has its coefficients in H_j). Let nu_0(beta) <= nu_1(beta) <= ... be the numbers eta_n(beta), each repeated d_n times, in increasing order. The list exists because the c_n are the eigenvalues of a trace-class operator. So mu_i := exp(- nu_i) are the ordered eigenvalues of C_beta on H_0, and all are positive.
Step 2 (the sandwich). On H_0 put X := C_beta^(1/2) M_beta. Then T = X* X, and X X* = C^(1/2) M^2 C^(1/2). Because exp(- 2 beta N) <= M^2 <= 1,

    exp(- 2 beta N) C_beta <= X X* <= C_beta   on H_0.

X* X and X X* have the same positive eigenvalues with the same multiplicities. By the min-max principle the ordered eigenvalues lambda_0 >= lambda_1 >= ... of R_beta satisfy exp(- 2 beta N) mu_i <= lambda_i <= mu_i for every i >= 0. So every lambda_i is positive, and

    nu_i(beta) <= - log lambda_i(beta) <= nu_i(beta) + 2 beta N.

Since m_i = - log lambda_i + log lambda_0, with C_1(beta) := nu_0(beta) + 2 beta N:

    abs(m_i(beta) - nu_i(beta)) <= C_1(beta)   for every i >= 1.

nu_i tends to infinity (trace class), so m_i does.
Step 3 (one link, two-sided bounds). Put nu = 2j + 1 >= 1 and U_j(beta) := beta + log(beta/2) + log(nu!) - nu log(beta/2). The series of I_nu gives (beta/2)^nu/nu! <= I_nu(beta) <= ((beta/2)^nu/nu!) exp(beta^2/4): the lower bound is the term k = 0, and the upper bound uses (nu+k)! >= nu!. Since eta_j = beta + log(beta/2) - log I_nu(beta):

    U_j(beta) - beta^2/4 <= eta_j(beta) <= U_j(beta).

Step 4 (one link, two couplings).
(lower) eta_j(beta_2) - eta_j(beta_1) <= U_j(beta_2) - U_j(beta_1) + beta_1^2/4 = (beta_2 - beta_1) + (1 - nu) log(beta_2/beta_1) + beta_1^2/4 <= C_a := (beta_2 - beta_1) + beta_1^2/4, because nu >= 1.
(upper) eta_j(beta_1) - eta_j(beta_2) <= U_j(beta_1) - U_j(beta_2) + beta_2^2/4 = (beta_1 - beta_2) + (nu - 1) log(beta_2/beta_1) + beta_2^2/4 <= nu log(beta_2/beta_1) + beta_2^2/4.
Put nu_* := the least integer at least (e beta_2/2)(beta_2/beta_1)^(1/eps). For nu >= nu_*: log nu - 1 - log(beta_2/2) >= (1/eps) log(beta_2/beta_1). With log(nu!) >= nu log nu - nu, Step 3 gives eta_j(beta_2) >= nu (log nu - 1 - log(beta_2/2)) + beta_2 + log(beta_2/2) - beta_2^2/4. So nu log(beta_2/beta_1) <= eps (eta_j(beta_2) + abs(log(beta_2/2)) + beta_2^2/4). For nu < nu_*: nu log(beta_2/beta_1) <= nu_* log(beta_2/beta_1), and eps eta_j(beta_2) >= 0. In both cases

    eta_j(beta_1) <= (1 + eps) eta_j(beta_2) + C_b,   C_b := (1 + eps) beta_2^2/4 + eps abs(log(beta_2/2)) + nu_* log(beta_2/beta_1).

Step 5 (all links, then the ordered lists). Sum Step 4 over the N links: eta_n(beta_2) - N C_a <= eta_n(beta_1) <= (1 + eps) eta_n(beta_2) + N C_b for every label n. Rearrangement: if x_n <= phi(y_n) for every n, with phi non-decreasing, and the two lists carry the same multiplicities d_n, then the ordered lists satisfy x_(i) <= phi(y_(i)); indeed the i + 1 entries with the smallest y all have x <= phi(y_(i)). Apply it twice:

    nu_i(beta_2) - N C_a <= nu_i(beta_1) <= (1 + eps) nu_i(beta_2) + N C_b   for every i >= 0.

Step 6. By Steps 2 and 5: m_i(beta_1) <= nu_i(beta_1) + C_1(beta_1) <= (1 + eps)(m_i(beta_2) + C_1(beta_2)) + N C_b + C_1(beta_1), and m_i(beta_1) >= nu_i(beta_1) - C_1(beta_1) >= m_i(beta_2) - C_1(beta_2) - N C_a - C_1(beta_1). So the claim holds with A_0 := C_1(beta_1) + C_1(beta_2) + N C_a and A_eps := C_1(beta_1) + 2 C_1(beta_2) + N C_b. Divide by m_i(beta_2), which tends to infinity, and let eps tend to 0. QED

### 2.3 Corollary LEV-FAIL (PROVED)

For every box B, every pair beta_1 < beta_2 and every E > 1, (LEV-down) fails: with eps = min(1, (E - 1)/2), it fails at every i with m_i(beta_2) > 2 A_eps/(E - 1), and there are infinitely many such i. The pointwise form of the remark in row 1610, 3.3 (every level falls at least at the logarithmic rate kappa) fails for every kappa >= 0 whose integral over [beta_1, beta_2] is positive, because it implies (LEV-down) with E = exp(integral of kappa).
Proof. If m_i(beta_1) >= E m_i(beta_2), Proposition UV-LEV gives (E - 1 - eps) m_i(beta_2) <= A_eps. QED

Consequences for the consumer of row 1610.
- Theorem TR-down in the level form is true and has no application to the Wilson operator with E > 1. With E = 1 it gives nothing.
- Corollary B was stated for (LEV-down). Its hypothesis needs E >= 512 [t_0/n + ...] > 1 whenever the box is not already cold. So for Wilson it is usable only through the thermal form, as its last sentence allows.
- The warning in row 1610, 3.3 ("too strong to be true", ARGUED there with momentum levels of a gapped theory; called "a model argument" by check 1613) is now a theorem, and for a different reason: the high levels are kinetic, and the kinetic eigenvalues at two couplings differ by a bounded amount per unit of spin against a size of order spin times log spin.
- The mirror statement of row 708 is not touched: (LEV_K) asks that no level falls faster than a rate K >= 0, and a ratio that tends to 1 is consistent with it.

Selectivity. The proof uses the form T = M C M, the bound 0 <= V_1 <= 2N and the power series of the link weights. It holds in the same way for every compact gauge group, every dimension and every bounded spatial weight (for U(1) with I_k(beta)/I_0(beta) in place of the SU(2) weights; I did not write that case out). So it reads the algebra of the kinetic operator only. By Lemma ALG of row 1553 (not re-read) such a statement is never an input. It is a negative about one form of the target, and it is used as nothing else.

Weight of the result (my reading). It is small. The failing levels lie at energies far above every physical scale: the convergence in Proposition UV-LEV is logarithmic (GUIDE, Section 2.5). No cold thermal sum sees them. What the corollary settles is the wording: a supplier for (T-down) must aim at the thermal form or at a truncated form with a thermal tail. The next proposition shows what a truncated form costs.

### 2.4 Proposition TRUNC (a truncated level form; PROVED)

Let beta_1 < beta_2, E >= 1, I >= 1 and t >= 2. Assume m_i(beta_1) >= E m_i(beta_2) for 1 <= i <= I. Then

    G(t; beta_1) <= G(tE; beta_2) + exp(- (t - 1) E m_I(beta_2)) G(1; beta_1),   and G(1; beta_1) <= exp(12 beta_1 abs(B)) - 1.

Proof. For i <= I the terms compare as in Theorem TR-down. For i > I: m_i(beta_1) >= m_I(beta_1) >= E m_I(beta_2), so exp(- t m_i(beta_1)) <= exp(- (t - 1) E m_I(beta_2)) exp(- m_i(beta_1)); sum over i > I. For the last bound: 1 + G(1) = Tr R/lambda_0, Tr R <= Tr(M C M) <= Tr C = 1, and lambda_0 >= exp(- 12 beta abs(B)) (row 710 Section 2, from `gap-transfer.md`; ON FILE). QED
Reading. On the cube n^3 at t = n/512 the tail is below a fixed tolerance only if E m_I(beta_2) is at least about 6144 beta_1 n^2 in lattice units. So the levels that must obey the rate reach an energy of order beta n^2. That is an energy per site of order beta/n, which tends to zero in lattice units and to infinity in physical units along the trajectory. So the truncated form asks the rate of states that are not cold. It does not replace the thermal form. (The bound on G(1) is crude; a better count of states would lower the threshold, and I did not look for one.)

### 2.5 Guide run for Section 2 (floating point; not a proof step)

File `vd1619/guide.py` in the scratch folder of this session, outside the repository; pure Python, one process, a few megabytes. It found 0 violations of the bounds of Step 3 (five couplings, 43 spins each) and 0 violations of the two difference bounds of Step 4 (beta_1 = 3, beta_2 = 8, 429 spins). In the model with one link and no spatial term the ratio (eta_j(3) - eta_0(3))/(eta_j(8) - eta_0(8)) was 2.84, 2.44, 2.04, 1.40, 1.22, 1.14, 1.11, 1.09 at 2j = 1, 4, 10, 10^2, 10^3, 10^4, 10^5, 10^6. So the limit 1 is reached only logarithmically, and the low levels of the electric model show the ratio beta_2/beta_1 = 2.67 of a rate 1/beta.

Note to Step 1 of 2.2. Off the closed span of the H_n the operator C_beta is zero (Lemma C of row 710; by the Peter-Weyl theorem that complement is {0}). So the positive eigenvalues of C_beta on H_0 are exactly the listed c_n, and there are infinitely many of them. The ordered list mu_0 >= mu_1 >= ... of the min-max principle is then the list of Step 1.

## 3. The thermal form on the band: six attacks, each with its first failing line

No statement in this section is a proof of (VIR-down). Each attack was written down, searched for in the folder, and pushed until one line failed. I record the line.

### 3.0 The size of the rate that the band must supply (ARGUED, with GUIDE numbers)

Exact, ON FILE: on an analytic branch of a level, - beta m_i' = Delta<N - beta R>_w - beta Delta<V_1> and m_i = Delta<eta>_w + Delta D (row 710, Theorem U (ii), (iii) and Section 8 item 1; Delta is "the level minus the vacuum", D a relative entropy). The first formula needs no restriction to beta < 4: it uses only the first equality of Lemma J (e).
- The electric part alone gives a rate close to 1/beta (row 710 Section 8 item 3; row 708 Section 4.4 Way 1). GUIDE, my run `vd1619/guide2.py`: in the model without spatial plaquettes, beta times the rate of the levels 2j = 2, 4, 6, 20 is 0.85, 0.72, 0.64, 0.44 at beta = 2.3; 1.02, 0.92, 0.85, 0.58 at beta = 5; 1.02, 1.01, 1.00, 0.89 at beta = 20. So the electric rate is not capped by 1/beta exactly (it exceeds it by about 2 percent at beta = 5), and it is 1/beta to that accuracy.
- The rate the consumer needs is of order one, not of order 1/beta. The budget of Corollary B is an integral of kappa of about log 512 plus a constant (row 1610 2.3: "near 7", GUIDE). The window in beta that covers the band and the cold range has a length of order one: the one-loop slope is 11/(3 pi^2) = 0.371 per unit of log size (the constant of BND-2 in check 1453, L107), so a factor 512 in size is 2.3 units of beta, and row 708 Section 4.5 counts "an interval of couplings of length about 2.5". So kappa must be about 1/0.37 = 2.7 on average there, while beta_K tends to infinity with K.
- Therefore every bound of the kind "kappa >= c/beta" is worth an integral of at most c log(beta_h/beta_K) over the window. For a window of bounded length that tends to zero as K grows.
- In field terms: with kappa beta = 1 + theta, the exact formulas give Delta D + beta Delta<V_1> + (electric remainder) = - theta m_i. The band needs theta of order beta_K: the magnetic and entropy parts of a level must lie below the vacuum's by a multiple of the level's energy that grows with the cutoff. Row 708 Way 1 has this with the GUIDE numbers of the bare crossover (about 3 times the energy at beta 2.3 to 2.6).
A longer window does not help (ARGUED; the small-box scaling is a GUIDE, belief I33 as quoted in row 1386 2.1). Beyond the band the box is small. Its low levels scale like the box coupling to the power 1/3 over the side. Their rate is about 1/(3 beta), and the cooling time at the hot end grows like beta_h^(1/3). The two cancel. Row 1610 2.5 says the same ("perturbative drift alone never meets the budget").

### 3.1 Attack 1: signs of the electric and magnetic parts

Idea. If the magnetic part of every level lay at or below the vacuum's, and the entropy part too, the formulas of 3.0 would give kappa >= about 1/beta with no further work.
First failing line. Two lines fail. (a) Neither sign is proved for any level at any coupling of order one; this is the mirror of row 708 Way 1, with the inequality reversed. (b) By 3.0 the sign is worth log(beta_h/beta_K), which is not the budget. A proof must bound the size of the deficit, not its sign.
On file: row 708 Section 4.4 Way 1; row 710 Section 8. Nothing new here except the remark (b) for the downward direction.

### 3.2 Attack 2: monotonicity in the period by a covering argument

Idea. t a_0 - A_t is the sum over the plaquettes of (the mean of (1/2) tr U_p on the torus of period t) minus (the same in the vacuum of the box). The identity log(1 + G(t)) = - sum over j >= 0 of 2^(-(j+1)) log P(2^j t), with P(v) = Z_+(2v)/Z_+(v)^2 the purity, follows from log P(v) = F(2v) - 2 F(v) and F(2^j t) -> 0 (PROVED, two lines; F = log(1 + G)). So t a_0 - A_t = - sum over j of 2^(-(j+1)) d/dbeta log P(2^j t; beta), and d/dbeta log P(v) = 2 A_v - A_(2v). So the sign form of (VIR-down), kappa = 0, follows if the mean action of the connected double cover of a torus is at least that of the disconnected one, at every period 2^j t.
First failing line. For groups with a Griffiths or Ginibre inequality one can compare a torus with its quotient by adding couplings that tie a configuration to its translate. The quotient then carries twice the coupling: the torus of period t at beta is the constrained torus of period 2t at beta/2, not at beta. So even for Z_2 and U(1) this does not compare A_(2t) with 2 A_t at one coupling. For SU(2) no such inequality is known (row 708 Section 2, first remark: these tools exist for the two groups for which the seed is false). And the statement reached would be the sign form, which Section 3.0 shows is not enough.

### 3.3 Attack 3: the exact structure of the Wilson weight

Idea. Row 708 Section 2 notes that the Wilson weight is the exponential of a function that is linear on R^4, restricted to the sphere SU(2), and that no inequality on file uses this. I tried to use it. With x = (1/2) tr g and the Laplacian normalised by Delta x = -(3/4) x, the weight w = exp(beta x) satisfies Delta w = (beta^2 (1 - x^2)/4 - 3 beta x/4) w, and so beta^2 w_(beta beta) + 3 beta w_beta + 4 Delta w = beta^2 w: beta is the radial variable of R^4, and the link multipliers I_(2j+1)(beta)/beta solve the matching Bessel equation.
What it gives (PROVED, by one integration by parts on each link; it is the first loop equation, (SD_s) of row 708 C-E): 3 times the sum over the plaquettes of <(1/2) tr U_p> equals beta times the sum over the links of <|grad_l S|^2>. Hence, exactly,

    t a_0 - A_t = (beta/3) [ sum over the links of the period-t torus of <|grad_l S|^2>_t  -  t (the same sum for one slab in the vacuum of the box) ].

Here S is the action with the seam signs of each twist sector, the means are those of the neutral ensemble (the mixture over z with the weights Z^z), and the vacuum term is the limit of the same sum per slab as the period grows. So the left side of (VIR-down) is the thermal excess of the mean squared force.
First failing line. This is one more identity for the left side. The right side, the energy, has no local expression: the same wall as row 708 Section 4.5 and row 710 Section 8 item 4 (a second identity is missing; the candidate is the anisotropy response, whose coefficients are themselves unknown at order one). The radial structure gives a dilation in the coupling of each plaquette. It gives no dilation of the lattice.

### 3.4 Attack 4: the physical form (the cooling aspect)

Idea. Let tau(beta) be the time at which the thermal sum of the fixed lattice equals 4/21. By Proposition EQ-down of row 1610 (corrected by check 1613), (T-down) along the level curve says that tau is non-decreasing in beta. In physical units this reads: the cooling aspect rho(L) := (cooling time)/(side L) does not increase with the side L, and the budget says that it falls from order one in a small box to 1/512 at the seed box. I looked for a general reason for such a monotonicity.
First failing line. There is none in the class. A free massless field has constant rho. The Ising model in its ordered phase refutes the matching size statement (MONO-Delta) (row 720 RESULT, a guide run there). So the monotonicity is a property of the model, with a rate that must be bounded below across the band. In the size direction this is (CAS) and (MONO-Delta) of rows 708 and 720, "the target in steps" (row 998). The coupling direction changes the bookkeeping (no (A1), no (R12), as row 1610 says) and not the content.
On file: rows 708 (CAS), 720 (MONO-Delta, Proposition MB), 931 (ANOM, through row 1610), 998. I add nothing.

### 3.5 Attack 5: a free sign from a first passage

Idea. Check 1613 shows that the existential form of (T-down) at K is exactly: G(u; beta_K) <= 4/21, and G(u; .) is non-decreasing on a right neighbourhood of beta_K. A sign at a first passage is free. On the fixed lattice put F(beta) = G(u; beta) on [beta_K, infinity). If F tends to infinity with beta, F has a last global minimiser betahat >= beta_K, and there F(betahat) <= F(beta_K) and F >= F(betahat) to the right. So whenever the thermal seed holds at (n_K, beta_K), both hypotheses of the existential (T-down) hold on the same lattice at the coupling betahat.
Standing. ARGUED, not PROVED: the growth of F needs the fixed-lattice asymptotics of row 1143 (statements (4), (11) as its RESULT text gives them: the plain periodic log-sum grows like (3/2) log beta), together with 1 + G >= (1/8)(1 + the plain thermal sum), which holds because every Z^z is positive. I did not read the file of row 1143.
First failing line. betahat is not the calibrated root. The pair (n_K, betahat) lies on no trajectory with one l and one g_0. And the statement is on the statement side: it assumes the seed. It shows only that the monotonicity half of (T-down) costs nothing at a shifted coupling, so the whole content of (T-down) at the calibrated root is the seed there plus the sign of F' at that one point.

### 3.6 Attack 6: the kinetic sandwich

Idea. Step 2 of Proposition UV-LEV compares R_beta with the kinetic operator, whose spectrum is explicit and whose levels fall at a rate close to 1/beta at every coupling.
First failing line. The comparison costs exp(2 beta N) per time step, a factor that is extensive in the box. A cold thermal sum is exponentially small in t m with m of order 1/n, so the sandwich loses it at once. It controls the levels far above every physical scale only. That is what Section 2 uses it for.

### 3.7 What a supplier for the band would have to be (ARGUED)

By 3.0 to 3.6 the thermal (VIR-down) on the band is a lower bound of order one on the lattice beta function, read from the cold thermal sum of a box whose coupling is of order one. Every exact formula on file writes it as a cancellation between an electric and a magnetic part that are each larger than the energy by a factor of order beta_K. Sign arguments reach 1/beta. Kinetic comparisons reach the far ultraviolet levels. Neither reads the band. I found no method, and I agree with row 1610 2.2 and 2.6 (C4: NONE) and with check 1613. The inputs that could supply it are the ones row 1386 names: (K-II), a renormalization step at order-one effective coupling, or a (K-I) carry whose sign is tied to a size. I did not find a new one.

## 4. The questions the brief asks

**Where does the argument fail for the free photon and for weak 4D compact U(1), and what does the failure read?**
- Proposition UV-LEV and Corollary LEV-FAIL do not fail for them. They hold for every compact group and every dimension (Section 2.3, Selectivity; the U(1) case is not written out). They read the algebra of the kinetic operator. They are a negative about the level form and are not an input.
- I have no positive argument for the thermal (VIR-down) on the band, so there is no line of mine that could fail for the photon. For the attacks of Section 3: Attack 1 fails for a Gaussian field at the line "the magnetic part lies below the vacuum's": for harmonic modes the electric and magnetic parts of every level are equal, the rate is zero, and that reads the law (a quadratic weight), not the algebra or the dimension. Attack 2 would give the sign form, which holds with equality for the photon and gives no rate. For weak 4D compact U(1) the verdict of check 1613 stands and I add nothing: failure for the three half-turns given the cited Villain inputs; the fully projected case open.
- 5D SU(2): nothing added; conditional, as in check 1613.

**Is the statement equivalent to (PUR-io)?** I propose no new sufficient statement. The thermal (VIR-down) with (HOT) keeps the standing of check 1613: for Wilson it implies (PUR-io) over the allowed sides by enlargement; the converse and strictness are open; its existential form at K is the thermal seed at K plus a one-sided sign at the calibrated root. Attack 5 adds (ARGUED) that this sign is free at a shifted coupling on the same lattice. Corollary LEV-FAIL is not equivalent to anything about the seed: it is true whether or not the seed holds.

**What is selective here?** Nothing. No statement of this file reads a property of typical four-dimensional SU(2) fields.

## 5. Notes for the lead (I edited nothing but this file)

1. The trigger of row 1610 section 4 can stay as it is worded (it names the thermal quantity t a_0 - A_t). Where the consumer is cited, cite the thermal form only: the level form of Theorem TR-down and the (LEV-down) hypothesis of Corollary B have no application to the Wilson operator with E > 1 (Corollary LEV-FAIL).
2. A supplier brief for the band should say that a sign is not enough: bounds of the kind kappa >= c/beta are worth c log(beta_h/beta_K), which tends to zero on a bounded window (Section 3.0, ARGUED).
3. Under the owner's rule of 2026-11-13 the hand proofs of Section 2 need a compute or Lean record before they land as a proof note. They are elementary (a power series bound, min-max, a rearrangement). I wrote no Lean; there is none on this machine. The guide run is not such a record.
4. A check of this row should read Section 2.2 line by line, and in particular: (Z1) to (Z3) against the lane's definition of C_z and P_0; the use of Lemma C of row 710 on H_0; Step 4 (upper), the case split at nu_*; the rearrangement in Step 5 with multiplicities.

## 6. Labels

| Statement | Label | Anchor |
|---|---|---|
| The setting of 2.1: the operator, Lemma C, Lemma J (d), lambda_0 >= exp(-12 beta abs(B)) | ON FILE (row 710, checked by row 715; read) | 2.1 |
| (Z1), (Z2), (Z3): P_0 commutes with M, C and every Pi_n | PROVED here, for the centre translations as described in 2.1 | 2.1 |
| Proposition UV-LEV | PROVED here given Lemma C and Lemma J (d) of row 710; by hand, checked by no one | 2.2 |
| Corollary LEV-FAIL: (LEV-down) fails on every box for every E > 1 | PROVED here, same standing | 2.3 |
| "The same holds for every compact group and dimension" | ARGUED (the U(1) case is not written out) | 2.3 |
| Proposition TRUNC | PROVED here given the two bounds cited from row 710 | 2.4 |
| "The truncated form asks the rate of states that are not cold" | ARGUED (a reading of the threshold; the bound on G(1) is crude) | 2.4 |
| The purity series for log(1 + G) and its derivative in beta | PROVED here (two lines) given Lemma D1 and a_0 = lim A_v/v (check 1613) | 3.2 |
| The force identity for t a_0 - A_t | PROVED here (one integration by parts); it is the first loop equation, ON FILE in substance (row 708 C-E) | 3.3 |
| The size of the needed rate; "a sign is worth log(beta_h/beta_K)"; "a longer window does not help" | ARGUED, with GUIDE numbers | 3.0 |
| The electric rate table | GUIDE (floating point) | 3.0 |
| Attack 5: the hypotheses of the existential (T-down) hold at a shifted coupling | ARGUED; leans on row 1143, whose file I did not read | 3.5 |
| The first failing lines of Attacks 1 to 6 | ARGUED (records of attempts, not theorems) | 3.1 to 3.6 |
| (VIR-down), thermal form, on the band | OPEN; not proved, not refuted, no first lemma | 3.7 |
| (HOT), (PUR-io), (K-I), (K-II), (R10), (R11), (R12), the gap | OPEN, untouched | |

Not done in this row: no Lean; no numeric run inside the repository; no web search; no check by another model; the files listed in R9 were not read. I did not prove (VIR-down) at any coupling. I did not write out Proposition UV-LEV for U(1).

Provenance: Claude Fable 5.2, laptop subagent of the lead session, 2026-11-27. Author only; checked by no one. Hand proofs. Two floating-point guide runs outside the repository (`vd1619/guide.py`, `vd1619/guide2.py` in the session scratch folder; pure Python, one process each, a few megabytes; the second ran about two minutes). Nothing committed, pushed or posted. No other file in the repository written. No file whose name begins with `gap-vir-down` was read other than this one.

RESULT: Row 1619 (Claude Fable 5.2; author only, checked by no one; no Lean; two float guide runs outside the repo). Target: (VIR-down) on the band.
Outcome: NONE for the target in the form its consumer accepts (the thermal form): not proved, not refuted, no first lemma. No open input moves.
(c), for the other form of the consumer only: PROVED by hand, Proposition UV-LEV: on every finite Wilson box and for all beta_1 < beta_2, the ordered
neutral levels satisfy m_i(beta_2) - A_0 <= m_i(beta_1) <= (1 + eps) m_i(beta_2) + A_eps for every i, so m_i(beta_1)/m_i(beta_2) -> 1. Corollary
LEV-FAIL: the level hypothesis (LEV-down) of Theorem TR-down fails for every E > 1 on every box, for every pair of couplings. The failing levels are
kinetic and far above every physical scale; the statement is algebraic (any compact group, any dimension) and is not an input. Also PROVED:
Proposition TRUNC (a truncated level form needs the rate up to energies of order beta n^2), the purity series for log(1 + G), and the force identity
t a_0 - A_t = (beta/3) x (thermal excess of the mean squared force), which is the first loop equation.
ARGUED: the band needs a rate of order one (about 2.7) while sign arguments on the electric and magnetic parts reach only about 1/beta, worth
log(beta_h/beta_K) -> 0; six attacks (signs, covering, the R^4 form of the Wilson weight, the cooling aspect, a first-passage sign, the kinetic
sandwich) each fail at a named line. Nothing here is selective. (T-down) keeps the standing of check 1613. Open: (VIR-down) on the band, (HOT),
(PUR-io), the gap.
