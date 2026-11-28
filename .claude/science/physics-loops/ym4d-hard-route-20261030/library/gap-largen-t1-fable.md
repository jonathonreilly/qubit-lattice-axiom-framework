lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 18:22:53 UTC 2026. Author only, checked by no one.

# Row 1724: ladder THM-T, rung T1 (response equation on good regions), with T2 if needed

## 0. Plan (written first; steps are added below as they are done)

1. Read library/ladders/README.md, library/ladders/THM-T.md, row 1708 section 7 and Lemma 1, and row 1715 sections 5 and 6.
2. State the setting: 4D lattice SU(N) Wilson theory, a region with holes, fixed exteriors, the good event (finitely many short loop traces pinned near planar values).
3. Write the exact single-link Schwinger-Dyson identity (row 1708 Lemma 1) for a difference of two states (two boundary conditions, or with and without a second insertion).
4. Derive the response equation: a linear equation for the difference, with a source at the perturbation.
5. Bound each error term by a small multiple of the response, or state exactly which term cannot be bounded and why.
6. Answer the two diagnostics of row 1715 (zero planar moment and long words; common-sign perturbation).
7. Decide whether T1 needs T2 (long words). Build it or state it as one precise lemma.
8. Say what reads SU(N) and not U(N).
9. Ladder update. RESULT line.

Sources read in full: library/ladders/README.md, library/ladders/THM-T.md, library/gap-largen-build-fable.md (row 1708), library/gap-largen-build-fable-check-astra62.md (row 1715). Nothing else was read. No reference is cited in this file. Labels: PROVED, ARGUED, GUESSED, OPEN.

## 1. Verdict first

T1 is built in a form with a floor. It is not built floor-free.

| Item | Statement | Status |
|---|---|---|
| Lemma 1' | Single-link Schwinger-Dyson identity with one distinguished loop and an arbitrary spectator factor | PROVED (section 3); exact check on SU(2), SU(3), one plaquette, orders 0 to 3 in beta (fractions, guide) |
| Proposition E | Exact response equation in centred variables. Linear planar part, plus "up" terms, plus N^-2 terms, plus a source only at links where the perturbation acts | PROVED (section 4) |
| Proposition B | For sequences with at most L letters every error term is at most a small multiple of the weighted response. The constants do not depend on N, the region, the holes or the exterior | PROVED (section 5) |
| Theorem R | Under planar stability in the form (PS-Lip) and moment pinning, the response decays as exp(-m dist) down to a floor a^(-L/2), L of order N^(2/3) | PROVED as an implication (section 6). (PS-Lip) is not proved at any beta |
| (T2-N) | The one lemma that removes the floor: the N^-2 terms on rows with more than L letters | STATED, OPEN (section 8) |

Late input (row 1722, library/gap-largen-ps7-fable.md, author only, unchecked; I read its sections 1, 2.2, 3, 4, 5.2, 5.3): linear planar stability on bounded loop functions is reported false in the weak phase of the one-plaquette twin. So the hypothesis (PS-Lip) of Theorem R is expected to be false on the weak side. Lemma 1', Proposition E and Proposition B do not use it and stand. Section 11 gives the relation to (RESP) of row 1722, the form of Theorem R with a restricted class and a centre row, and one more open lemma (T1-C).

The two diagnostics of check 1715 are answered in section 7. Short form: the equation never divides by a planar moment and never uses a relative error; long words are not pinned and are paid by the length weight; a common-sign mode is not excluded by pinning but by planar stability, down to the floor.

## 2. Setting

Lattice Z^4, sup-norm distance. Links carry U_e in SU(N). Notation of row 1708 section 2 and section 3: tr = (1/N) Tr; a loop is a closed word (no reduction); eps_x, n_e, t_e, split, merge, l (+)_x p, l (-)_x p. For a loop l write |l| for its length; a nonempty loop has |l| >= 2.

S_e = N beta sum over the six plaquettes p that contain e of Re Tr U_p. d_a is the left derivative at the link e in the direction T_a (row 1708 section 3).

**Response functional.** rho is a finite signed measure on link configurations with rho(1) = 0. Two cases are meant:
- (second insertion) rho(F) = E_mu[F g] - E_mu[F] E_mu[g], g bounded;
- (boundary condition, or any change of the exterior or of the holes) rho = mu - mu'.
Here mu, mu' are any probability laws on configurations. Links outside the integrated set are random or fixed; it makes no difference.

**Definition (homogeneous link).** rho is SD-homogeneous at the link e if, for every smooth F,

  rho( sum_a d_a d_a F + sum_a (d_a F)(d_a S_e) ) = 0.      (H)

Lemma 0 (PROVED). (i) If the conditional law of U_e under mu, given all other links, is Z^-1 exp(S_e) dU_e, then E_mu[ sum_a d_a d_a F + sum_a d_a F d_a S_e ] = 0. (ii) So mu - mu' is SD-homogeneous at e if both laws have that conditional law at e. (iii) Cov_mu(., g) is SD-homogeneous at e if mu has that conditional law at e and g does not depend on U_e. (iv) If g depends on U_e, then

  rho( sum_a d_a d_a F + sum_a d_a F d_a S_e ) = - E_mu[ sum_a (d_a F)(d_a g) ].     (Src)

Proof. Left invariance of Haar measure on the fibre of U_e gives the integral of sum_a d_a( (d_a F) G exp(S_e) ) = 0 for G = 1 and G = g. Expand the derivative. For (iii) g is constant on the fibre. For (iv) subtract E[g] times the case G = 1. QED.

Only the conditional law of the one link e is used. So (H) holds in a region with holes, with any fixed or random exterior, and with any law in the holes. The right side of (Src) is the source. It is zero unless the perturbation reads the link e.

**Planar solution.** W is a function on loops with |W| <= 1, W(empty) = 1, and W(l) = F^e_beta(W)(l) for every loop l and every link e of l, with F^e_beta as in row 1708 line 163. No positivity, symmetry or uniqueness of W is used in sections 3 to 6. Centred variable: x_l = tr U_l - W(l). So |x_l| <= 2 and x_empty = 0. For a sequence s = (l_1,...,l_k): x_s = prod x_{l_i}.

## 3. Lemma 1' (distinguished loop, spectator). PROVED

**Lemma 1'.** Let rho be SD-homogeneous at e. Let l_1 be a loop, n = n_e(l_1), t_1 = t_e(l_1). Let Y = prod_{i=2..k} y_i, where each y_i is tr U_{l_i} plus a constant. Write t_i = t_e(l_i) and Y_i for Y without the factor i. Then

  n rho(tr l_1 Y) = (t_1^2/N^2) rho(tr l_1 Y)
     - sum_{x != y in l_1} eps_x eps_y rho( tr l' tr l'' Y )
     + (beta/2) sum_x eps_x sum_p rho( [tr(l_1 (-)_x p) - tr(l_1 (+)_x p)] Y )
     + (beta/2) t_1 sum_p rho( tr l_1 [tr p - tr p^-1] Y )
     - N^-2 sum_{i>=2} sum_{x in l_1, y in l_i} eps_x eps_y rho( tr m_xy Y_i )
     + N^-2 sum_{i>=2} t_1 t_i rho( tr l_1 tr l_i Y_i ).            (SD')

Here (l', l'') is split_{xy}(l_1) and m_xy is merge_{xy}(l_1, l_i). For U(N) the first, fourth and last terms are absent.

Proof. Put F = tr l_1 Y in (H). By row 1708 (3) with one loop, sum_a d_a d_a tr l_1 = -N n tr l_1 + (t_1^2/N) tr l_1 - N sum eps eps tr l' tr l''. By row 1708 (4), sum_a (d_a tr l_1)(d_a S_e) = (N beta/2) sum_x eps_x sum_p [ tr(l_1 (-)_x p) - tr(l_1 (+)_x p) + tr l_1 (tr p - tr p^-1) ]. d_a is a derivation and kills constants, so d_a Y = sum_i (d_a tr l_i) Y_i. By the third relation of row 1708 (2), sum_a (d_a tr l_1)(d_a tr l_i) = N^-2 sum_{x,y} eps_x eps_y [ -Tr(merge) + (1/N) Tr l_1 Tr l_i ] = -N^-1 sum eps eps tr m_xy + N^-1 t_1 t_i tr l_1 tr l_i. Insert in (H) and divide by N. For U(N) the term (1/N) delta delta of the completeness relation is absent. QED.

Relation to Lemma 1 of row 1708 (PROVED): the sum of (SD') over the choice of the distinguished loop is (SD), because sum_{i,j} t_i t_j = t_e^2. (SD') is finer. Its left coefficient is n_e(l_1), not n_e(s), and no split of a spectator appears.

Exact check (guide only). /private/tmp/claude-501/largen-t1/check_lemma1p.py, python3 -I, fractions. One-plaquette model, N = 2 and 3, law Haar times exp(N beta Re Tr V). Loops are powers V^k. The identity (SD') is expanded in beta and each of the orders 0, 1, 2, 3 is evaluated exactly by Weyl integration. Twelve instances (k_1; Y) per N, with both orientations, mergers that cancel letters, and three spectators. All vanish exactly. Three mutations (sign of the last term; sign of the beta terms; no t_1^2/N^2 term) are detected in 14, 25 and 24 of the 25 instances.

## 4. Proposition E (exact response equation). PROVED

Define, for a function delta on loops, a loop l and a link e of l (n = n_e(l), t = t_e(l)):

  (D^e delta)(l) = (1/n) [ - sum_{x != y} eps_x eps_y ( W(l') delta(l'') + W(l'') delta(l') )
        + (beta/2) sum_x eps_x sum_p ( delta(l (-)_x p) - delta(l (+)_x p) )
        + (beta/2) t sum_p ( W(l) [delta(p) - delta(p^-1)] + [W(p) - W(p^-1)] delta(l) ) ].

This is DF^e_beta(W), the linearised planar operator of row 1708 (PS), with the term that check 1715 section 4 restores when W(p) is not real.

**Proposition E.** Let rho be SD-homogeneous at e. Let s = (l_1, Y) with Y = prod_{i>=2} x_{l_i}, and e a link of l_1. Put delta_Y(l) = rho(x_l Y). Then

  delta_Y(l_1) - (D^e delta_Y)(l_1) = E_up + E_N ,                         (R)

  E_up = (1/n) [ - sum_{x != y} eps_x eps_y rho( x_{l'} x_{l''} Y ) + (beta/2) t_1 sum_p rho( x_{l_1} (x_p - x_{p^-1}) Y ) ],

  E_N = (1/(n N^2)) [ t_1^2 rho(tr l_1 Y) - sum_{i>=2} sum_{x,y} eps_x eps_y rho( tr m_xy Y_i ) + sum_{i>=2} t_1 t_i rho( tr l_1 tr l_i Y_i ) ].

If rho = Cov_mu(., g) and g reads U_e, the right side has one more term, the source N^-1 n^-1 E_mu[ sum_a (d_a tr l_1) Y (d_a g) ].

Proof. In (SD') write tr l = x_l + W(l) in the first slot everywhere: tr l' tr l'' = x' x'' + W' x'' + x' W'' + W' W'', and tr l_1 (tr p - tr p^-1) = x_1 (x_p - x_{p^-1}) + x_1 (W(p) - W(p^-1)) + W(l_1)(x_p - x_{p^-1}) + W(l_1)(W(p) - W(p^-1)). The terms with no x in the first slot add to rho(Y) times [ n W(l_1) - n F^e_beta(W)(l_1) ] = 0, by the planar equation. The terms with one x are n D^e delta_Y. The rest is E_up and E_N. QED.

Remarks.
1. (R) is exact at every N. It is linear in rho.
2. No bias bound is used. The centring constant W(l) need not be near the mean of tr U_l: a constant in a slot gives rho(Y) times the planar equation, and for k = 1 it gives rho(1) = 0. Check 1715's corrected (LD) needs a bias bound for the event; the equation does not.
3. E_N in centred variables: rho(tr l_1 Y) = rho(x_1 Y) + W(l_1) rho(Y); rho(tr m Y_i) = rho(x_m Y_i) + W(m) rho(Y_i); tr l_1 tr l_i Y_i gives the four terms rho(x_1 Y), W(l_1) rho(Y), W(l_i) rho(x_1 Y_i), W(l_1) W(l_i) rho(Y_i). So E_N has terms with k, k-1 and k-2 loops. The terms with k loops add to the diagonal term (t_1 t_e(s)/(n N^2)) rho(x_1 Y), with t_e(s) the total current. This term is SU(N) only.

## 5. Proposition B (relative size of every error term). PROVED

Parameters: a > 1, m >= 0, 0 < eta <= 1. lambda is a 1-Lipschitz function Z^4 -> [0, infinity); lambda(s) is its maximum over the sites of s. Weight:

  w(s) = eta^(k-1) prod_i ( a^|l_i| / |l_i|^2 ) exp( m lambda(s) ),    k = number of loops of s.

Constants: c_q = sup_{h>=2} h^q a^(-h/2) for q = 2, 3; C_up = 106 + (3/8) beta a^4 e^m; C_N = 5 + (c_2 + c_3 + c_2 c_3)/4.

**Proposition B.** Let psi be any function on sequences with psi(empty sequence) = 0, and Psi = sup_s |psi(s)|/w(s) finite. Replace rho(x_s) by psi(s) in E_up and E_N (written in centred variables, Remark 3). Then for every row (s; l_1, e) with |s| <= L, L >= 2:

  |E_up| <= C_up eta w(s) Psi ,      |E_N| <= C_N L^3 N^-2 eta^-2 w(s) Psi .

The bound on E_up holds for every |s|.

Proof. Each term is a coefficient times psi(s'). The bound is the sum of |coefficient| w(s')/w(s). lambda(s') <= lambda(s) except where a plaquette is added, where lambda(s') <= lambda(s) + 1. Write h = |l_1|, h_i = |l_i|.

Quadratic split. s' = (l', l'', Y) with lengths j, j'. If a piece is empty its x is 0. Else w(s')/w(s) <= eta a^(j+j'-h) h^2/(j j')^2. If the signs are equal, j + j' = h and h^2/(j j')^2 = (1/j + 1/j')^2 <= 4/min(j,j')^2. If they are opposite, h = j + j' + 2 <= 2(j + j') and the ratio is at most 16/min(j,j')^2. Fix x. Two occurrences y of the same sign are at different letters, so they give different j. So at most 4 occurrences y have min(j,j') = mu (two signs; j = mu or j' = mu). The sum over y is at most 64 zeta(2) eta < 106 eta. The average over x keeps this bound. This is where the polynomial factor |l|^-2 is used: without it the row sum is (n - 1) eta.

Current up-term. 12 terms (six p, two orientations), coefficient (beta/2)|t_1|/n <= beta/2, ratio eta (a^4/16) e^m. Sum (3/8) beta a^4 e^m eta.

E_N. Use n <= h, |t_i| <= n_e(l_i) <= h_i, |W| <= 1, h^2 a^-h <= c_2, h^3 a^-h <= c_3, sum_i n_e(l_i) <= L, k - 1 <= L/2.
- (t_1^2/(n N^2)) psi(s): at most L/N^2. (t_1^2/(n N^2)) W(l_1) psi(Y): ratio h^2 a^-h/eta, so at most c_3/(eta N^2).
- Merger, psi(m, Y_i): n_e(l_i) terms after division by n; |m| >= h + h_i - 2 >= (h + h_i)/2; ratio a^(|m|-h-h_i) h^2 h_i^2/(eta |m|^2) <= 4 h_i^2/eta. Sum at most 4 L^3/(eta N^2).
- Merger, W(m) psi(Y_i): ratio h^2 a^-h h_i^2 a^-h_i/eta^2. Sum at most (L/2) c_2 c_3/(eta^2 N^2).
- Current term: L/N^2 + L c_2/(eta N^2) + (L/2) c_3/(eta N^2) + (L/2) c_2 c_3/(eta^2 N^2).
With eta <= 1 and L >= 2 (so L <= L^3/4, 1 <= L^3/8) the total is at most C_N L^3/(N^2 eta^2). QED.

The constants are not optimised. The power L^3 comes from the merger with a long spectator under the polynomial weight.

## 6. Theorem R (decay of the response to a floor). PROVED as an implication

**Hypothesis (PS-Lip)(beta; m, a, kappa).** There is a planar solution W such that for every 1-Lipschitz lambda >= 0 and every bounded delta on loops with delta(empty) = 0:

  sup_l |delta(l)| |l|^2 a^-|l| e^(-m lambda(l)) <= kappa sup_{l, e in l} |delta(l) - (D^e delta)(l)| |l|^2 a^-|l| e^(-m lambda(l)).

It differs from (PS) of row 1708 in two points: the factor |l|^2, and the family of Lipschitz weights in place of the one weight r(l). It is a statement about one deterministic operator on single loops. It is not proved here at any beta. By row 1722 it is expected false on the weak side; see section 11, where the class of delta is restricted and a centre row is added.

**Good region.** G is a set of links. K >= 4. The pinned list is P_K = { loops l inside G with |l| <= K }. G0 is the set of links e in G such that rho is SD-homogeneous at e and all links of the six plaquettes at e are in G. V is the set of end sites of the links not in G0. So V holds the perturbation, the holes, the exterior, the unpinned regions, and a collar of width one.

**Hypothesis (AP)(eps, K, Q, tau), a priori pinning.** For all sigma <= Q, all l_1,...,l_sigma in P_K and all bounded F: |rho(F prod x_{l_i})| <= tau sup|F| eps^sigma.

Lemma AP (PROVED). (AP) holds with tau = 2 sup|g| for rho = Cov_mu(., g), and with tau = 2 for rho = mu - mu', if the laws satisfy the moment pinning E|x_l|^Q <= eps^Q for every l in P_K. Proof: Hoelder with exponent sigma for each factor, then E|x|^sigma <= (E|x|^Q)^(sigma/Q). QED.
Moment pinning is a statement about the full law. No cutoff and no conditioning on a good event is used, so the cutoff term of check 1715 item 6.1 does not appear. A single-loop deviation bound P(|x_l| > eps/2) <= exp(-c N^2) gives E|x_l|^Q <= (eps/2)^Q + 2^Q exp(-c N^2) <= eps^Q for Q <= c N^2 / ln(4/eps) (PROVED, one line). Such a bound around W needs the bias bound of check 1715 section 5; that is not built here.

**Theorem R.** Assume (PS-Lip)(beta; m, a, kappa) with m > 0. Put

  eta = 1/(4 kappa C_up),   L = the integer part of ( N^2 eta^2 / (4 kappa C_N) )^(1/3),   N0 = 16 (kappa C_N)^(1/2) / eta,   C_A = 4 c_3 + 36 beta c_2.

Let N >= N0 (so L >= 4). Let eps <= eta/c_2, let K >= 4 be such that 2 h^2 a^(-h/2) <= eta for all h > K, and let Q >= L/2 + 1. Let G, G0, V be as above and assume (AP)(eps, K, Q, tau). Then for every sequence s_0 inside G with at most Q loops in P_K, and with R = dist(s_0, V):

  |rho(x_{s_0})| <= kappa C_A tau eta^(k-1) prod_i ( a^|l_i| / |l_i|^2 ) max( e^(-m R), a^(-L/2) ).

For one loop: |rho(tr U_l)| <= kappa C_A tau (a^|l|/|l|^2) max( e^(-m R), a^(-L/2) ). The constants kappa, C_A, eta, N0 depend on (beta, m, a, kappa) only. They do not depend on N >= N0, on G, on the holes, on the exterior, or on the perturbation.

Proof. Let D be the set of sequences inside G with at most Q loops in P_K. Put psi(s) = rho(x_s) for s in D, psi = 0 otherwise. Put lambda(x) = max(0, R - dist(x, V)) and w as in section 5.

(a) A priori bound. For s in D bound each long factor by 2 and use (AP) for the pinned factors: |psi(s)| <= tau prod b(l_i), b = eps on P_K, b = 2 on loops longer than K. The conditions on eps and K give b(l) <= eta a^(|l|/2)/|l|^2. So |psi(s)| <= tau eta w(s) a^(-|s|/2) and Psi <= tau eta is finite. In the same way |psi(l*, Y)| <= 2 tau B_Y for every loop l*, with B_Y = prod over Y of b <= eta^(k-1) prod_Y a^(h_i/2)/h_i^2 (if (l*,Y) is not in D the left side is 0).

(b) Equation rows: s inside G, e in G0, |s| <= L. Then k <= L/2, every sequence in (R) is inside G (the plaquettes at e are in G) and has at most k + 1 <= Q loops. So (R) holds with psi in the place of rho(x_.), and Proposition B gives |psi(s) - D^e psi_Y(l_1)| <= ( C_up eta + C_N L^3 N^-2 eta^-2 ) w(s) Psi <= w(s) Psi/(2 kappa).

(c) All other rows. If Y is not in D as a sequence then psi(l*, Y) = 0 for all l* and the residual is 0. Else every psi in the residual is at most 2 tau B_Y in modulus, and the absolute coefficients of 1 - D^e add to at most 1 + 2(n - 1) + 6 beta + 12 beta: |residual| <= tau B_Y (4 h + 36 beta). Divide by w(s) = eta^(k-1) (a^h/h^2) prod_Y(a^h_i/h_i^2) e^(m lambda(s)): the weighted residual is at most tau (4h + 36 beta) h^2 a^-h a^(-|Y|/2) e^(-m lambda(s)) <= C_A tau a^(-|s|/2) e^(-m lambda(s)).
A row that is not an equation row has |s| > L, or e not in G0, or a link of s not in G. In the last two cases a site of s is in V, so lambda(s) = R. So the weighted residual is at most C_A tau max( a^(-L/2), e^(-mR) ).

(d) Fix Y and apply (PS-Lip) to delta(l) = psi(l, Y) with the 1-Lipschitz function max(lambda, lambda(Y)). The weight of (PS-Lip) times the constant eta^(1-k) prod_Y(h_i^2 a^-h_i) is 1/w((l,Y)). So Psi <= kappa max( Psi/(2 kappa), C_A tau max(a^(-L/2), e^(-mR)) ). Psi is finite, so Psi <= kappa C_A tau max(...). At s_0, lambda(s_0) = 0. QED.

What the theorem is. Rows with at most L letters carry a true response equation: linear planar operator, errors a small multiple of the response. The source is the set of rows that touch V, discounted by e^(-mR). The floor a^(-L/2) = exp(-c N^(2/3)) is the price of the rows with more than L letters, where only the a priori bound is used.

What it is not. It is not floor-free. Rung T5 needs floor-free clustering. So Theorem R does not yet feed T5.

Against Theorem Q of row 1708: Q needs stability on sequences (TPS), where the split term amplifies (Proposition N). Theorem R needs stability on single loops only. The quadratic split term costs eta because the variables are centred and the weight is eta per loop. The pinning pays for that weight through (AP). Q's floor is a^(-N^2/(4 kappa)); R's is weaker in the exponent and has the factor tau.

## 7. The diagnostics of check 1715

**(a) A planar moment is zero.** Check: pinning gives an absolute error k eps for a product, and no relative error when W(l) = 0. Answer (PROVED by Proposition E): the response equation uses the additive identity tr l' tr l'' = W'W'' + W'x'' + x'W'' + x'x''. It never divides by W. A zero planar moment gives a zero coefficient in D^e, nothing else. The smallness of the product term is not "x'x'' is small against W'W''". It is "rho(x'x''Y) has one more centred factor than rho(x_1 Y), and the weight gives it a factor eta". The weight is legitimate because (AP) bounds each pinned factor by eps <= eta/c_2.

**(b) Long words; the roots-of-unity example.** Check: the first j - 1 power traces can agree while the j-th differ by 1. Answer (PROVED inside Theorem R): no long word is assumed near its planar value. A loop longer than K has b = 2, the trivial bound, and the example shows that this is the right bound. Long words enter in three ways. (1) As W(l') in D^e: this is the value of the planar solution, not of the configuration. (2) In the quadratic split of a long loop into two long loops: paid by the weight eta a^|l|/|l|^2, which needs only 2 h^2 <= eta a^(h/2) for h > K, that is K of order (2/ln a) ln(1/eta). (3) In rows with more than L letters: not controlled. This is the floor. So pinning of finitely many short traces is enough for the equation rows, and T2 is needed only in the form (T2-N) below.

**(c) Common-sign perturbation.** Check: X_x = W_x + Z min(eps/2, 1/N) with one symmetric sign Z is good everywhere and has constant covariance. Answer. The family is pinned, so pinning cannot exclude it; Theorem R does not use pinning for that. Take g = Z. Then rho(x_l) = c = min(eps/2, 1/N) for every l, and tau = 2. Two facts (PROVED from Theorem R): (1) a law with this response cannot be SD-homogeneous on a deep good region where (PS-Lip) holds, once kappa C_A (a^4/8) max(e^(-mR), a^(-L/2)) < c. The floor exp(-c' N^(2/3)) is below 1/N for large N, so the diagnostic mode at size 1/N is excluded at depth R of order (1/m) ln N. (2) What excludes it is the linear hypothesis: a common mode is a bounded, non-decaying delta with zero residual on the equation rows, and (PS-Lip) with m > 0 forbids that. In this example the level-two response rho(x'x'') = c^2 Cov(Z^2, Z) is zero, so the error terms do not help or hurt. A common mode of size below the floor is not excluded. That is the same gap as the floor.

## 8. T2: the one lemma that removes the floor. OPEN

Where the proof of Theorem R loses. On a row with |s| > L the term E_up is still at most C_up eta w(s) Psi (Proposition B). Only E_N is not small. Its coefficients are of order n_e(s)/N^2:
- the diagonal term (t_1 t_e(s)/(n N^2)) rho(x_1 Y), SU(N) only;
- the mergers of l_1 with each spectator, both groups.
An exact degenerate row (PROVED): s = N^2 copies of one plaquette p, l_1 one copy, e in p. Then n = 1, t_1 = 1, t_e(s) = N^2, and the diagonal coefficient is 1: (R) has no diagonal term left. This is the row (tr p)^(N^2); in Lemma 1 it is n_e - t_e^2/N^2 = 0. The exact check of section 3 includes this row at N = 2. For U(N) the row is not degenerate.

**Lemma (T2-N), needed, not proved.** In the setting of Theorem R with Q = infinity there are theta < 1/(4 kappa) and C, depending on (beta, m, a, kappa) only, such that for every row (s; l_1, e) with s inside G, e in G0 and |s| > L:

  |E_N(s; l_1, e)| <= theta w(s) Psi + C tau w(s) e^(-m R).

With (T2-N) every row inside G0 is an equation row, step (c) keeps only the source rows, and the conclusion of Theorem R holds with max(e^(-mR), a^(-L/2)) replaced by e^(-mR) (ARGUED: same proof; Q = infinity means pinning of all moments, which the full Wilson law does not have, so the passage from finite Q is a second part of the lemma). I do not know if (T2-N) is true in this weighted norm. On the degenerate row it says that the response of (tr p)^(N^2) is small against the weight. GUESSED: a proof must use that the density of rho on a deep box has little content at polynomial degree above N^2 beta in the matrix entries, because the box sees the perturbation only through exp(N beta Re Tr) on its boundary plaquettes.

A weaker form does not work (PROVED by the row count): a bound |rho(x_s)| <= theta w(s) sup_{|s'|<=L} |rho(x_s')|/w(s') for |s| > L is not enough. A row with |s| just above L has linear split targets with at most L letters and coefficients that add to an order-one constant, so its residual is not small. The lemma must be about E_N.

## 9. What reads SU(N) and what does not

In (SD') and (R) three terms are SU(N) only:
1. In D^e: (beta/2) t ( W(l)[delta(p) - delta(p^-1)] + [W(p) - W(p^-1)] delta(l) ). Order one. Zero on even variations when W(p) is real. This is inside the hypothesis (PS-Lip).
2. In E_up: (beta/2) t_1 rho( x_1 (x_p - x_{p^-1}) Y ). Relative size (3/8) beta a^4 e^m eta. It is an error term, not a mechanism.
3. In E_N: the diagonal term t_1 t_e(s)/(n N^2). Small on equation rows. It makes the degenerate row of section 8.

Theorem R itself does not read the group (PROVED by inspection): drop the three terms, replace D^e by its U(N) form, and the same proof gives the same statement for U(N) under the U(N) form of (PS-Lip). So the U(N) twin of Theorem R passes. All reading of SU(N) is in the hypothesis (PS-Lip), in its odd sector, and in (AP). Theorem R does not show that the hypothesis holds for one group and fails for the other.

U(1) twin test (README rule). At N = 1 the theorem is empty: N >= N0 = 16 (kappa C_N)^(1/2)/eta > 1 fails, because the terms E_N have no small factor. So the theorem proves nothing false for U(1). It also proves nothing for SU(2) unless N0 <= 2, and N0 >= 64 (eta <= 1/4, kappa C_N >= 1 in any use; ARGUED). Rung T1 as built claims to read large N, not SU(2).

## 10. Open items by name

- (PS-Lip) at any beta. Its relation to (PS): the factor |l|^2 and the Lipschitz family of weights.
- (T2-N).
- Moment pinning around W up to order Q >= L/2 + 1 in a deep region: needs a single-loop deviation bound and the bias bound of check 1715 section 5.
- The constants C_up, C_N, C_A and the exponent 2/3 are not optimised and not checked by a second reader.
- The use of Theorem R inside an expansion over bad regions (rung T3): V is allowed to be any set, and tau is the only data of the perturbation, but no expansion is written.

## 11. Relation to row 1722: (C), (PS') and (RESP)

Added after a note from the lead. Row 1722 is the work of one author and is not checked. I use its statements as reported there.

### 11.1 What row 1722 changes for this file

1. Row 1722 reports (PROVED there in the one-plaquette twin only) that a linear lower bound for 1 - DF(W) fails in a weak phase: on bounded loop functions, and also on differences of positive solutions (the atom family: distance alpha, defect alpha^2 l1). (PS-Lip) is a bound of that kind. So on the weak side Theorem R is an implication whose hypothesis is expected false. Theorem R stays a correct implication. It can have content on the strong side only, or in the restricted form of 11.3.
2. The same atom family is consistent with Proposition B (ARGUED). For such a pair of states the single-loop residual alpha^2 is the term E_up of (R), the level-two response rho(x'x''Y). Proposition B bounds it by C_up eta w Psi, where Psi holds the level-two response with weight eta. So the exact equation and its relative error bounds are true there. What fails is the inversion. This agrees with row 1722 section 5.2 step 3: "the bad direction is paid for by the measure, not by an inverse".
3. The SU(N) term of D^e, (beta/2) t W(l)[delta(p) - delta(p^-1)], has an odd kernel direction in the twin (the tangent of the winding family of row 1722 section 2.2). The centre equation (C) removes it. So section 9 item 1 must be read with this: the last term does not select the state; (C) does.

### 11.2 T1 against the response equation of (RESP)

(RESP) of row 1722 section 5.3 is a statement at N = infinity about chi = lim N^2 Cov(tr U_l, Re(c tr U_l')). Its equation has two lines:
 (line 1) chi - DF0^e(W) chi (l) = sigma^e_l'(l), zero unless e is a link of l';
 (line 2, Maxwell) beta sum_{p contains e} Im chi(p) = - t_e(l') Im(c W(l')).
Row 1722 derives it formally ("when the derivative exists and factorisation holds to first order").

**Line 1 is Proposition E at k = 1 (PROVED, exact at every N).** Take rho = N^2 Cov_mu(., g) with g = Re(c tr U_l'). At a link e that is not in l', (R) reads delta - D^e delta = E_up + E_N with E_N = (t^2/(n N^2)) rho(tr l). At a link e of l' the source of Proposition E is, by the proof of Lemma 1',

  N^-1 n^-1 N^2 E[ sum_a (d_a tr l)(d_a g) ] = n^-1 Re_c [ - sum_{x in l, y in l'} eps_x eps_y E tr m_xy + t_e(l) t_e(l') E( tr l tr l' ) ],

where Re_c means: the real part is taken on the l' factor before the merger (the two orientations of l' with weights c/2 and its conjugate). The first term is the set of deformations of l by l' at e, with total modulus at most n_e(l')/n_e(l), as row 1722 states. The second term is SU(N) only and is absent in row 1722's line 1. It is of order one: t_e(l) t_e(l') W(l) Re(c W(l')) / n at leading order. It is the same central correction that gives the last term of (SD). (ARGUED: row 1722 works with F0 and (C), where this term is moved to line 2.)
The operator: D^e is DF^e(W). On a delta with delta(l^-1) = conj delta(l) and sum_{p contains e} Im delta(p) = 0, and W(p) real, the last line of D^e is zero and D^e = DF0^e(W). So line 1 of (RESP) is (R) at k = 1 plus the linear centre row.
The errors that (RESP) drops, with their sizes on rows of at most L letters (Proposition B): E_up, at most C_up eta times the weighted response; E_N, at most C_N L^3 N^-2 eta^-2 times it. So T1 supplies, at finite N and with bounds uniform in the region, the statement that row 1722 marks "formal".

**Line 2 is not supplied with a relative error. One exact identity is (PROVED).** Let z = exp(2 pi i/N) and let T be the map U_e -> z U_e. If rho is SD-homogeneous at e in the sense that its laws have the conditional density exp(S_e) at e (Lemma 0 (ii), (iii)), then for every bounded F

  rho( (F o T) exp(S_e o T - S_e) ) = rho(F),   S_e o T - S_e = N^2 beta sum_{p contains e} [ (cos(2 pi/N) - 1) Re tr U_p - sin(2 pi/N) Im tr U_p ].     (Z-lin)

Proof: Haar measure on the fibre is invariant under T. QED. This is the linear form of Lemma Z of row 1722 (which applies Jensen to one law). With F = 1, W(p) real, and Theta = N^2 beta sum_p [ (cos - 1) Re x_p - sin Im x_p ]:

  beta sum_p rho(Im x_p) = - tan(pi/N) beta sum_p rho(Re x_p) + ( N^2 sin(2 pi/N) )^-1 sum_{j>=2} rho(Theta^j)/j! .

The first term on the right is small: a factor pi/N on the response. The second is not small in the weights of section 5 (PROVED by the count): Theta is of size 2 pi N beta sum |x_p|, so the term j is a response of level j times (2 pi beta N)^j / N, against the weight eta^(j-1). The ratio is of order (N eta)^(j-1). It is small only if the pinning scale times N is small, and the true fluctuation of tr U_p is of order 1/N. So the centre row for the response is not a perturbation of its linear form at finite N. It is a tilt by exp(Theta) with Theta of order one.
Lemma Z itself gives only an absolute bound: for two laws, |beta sum_p Im (w(p) - w'(p))| <= 12 beta tan(pi/N). Used as a residual it gives a floor of order tau/N, with no factor e^(-mR). That is worse than the floor of Theorem R.

### 11.3 Theorem R with a restricted class and a centre row. PROVED as an implication (same proof)

Let Cl be any class of bounded functions on loops that contains every function l -> rho(x_l Y) 1[(l,Y) in D] that occurs in the proof of Theorem R. Replace (PS-Lip) by

**(RESP-Lip)(beta; m, a, kappa; Cl).** For every 1-Lipschitz lambda >= 0 and every delta in Cl:
  sup_l |delta(l)| |l|^2 a^-|l| e^(-m lambda(l)) <= kappa max( sup_{l, e in l} |delta(l) - (D^e delta)(l)| |l|^2 a^-|l| e^(-m lambda(l)) , sup_e |beta sum_{p contains e} (delta(p) - delta(p^-1))/(2i)| 16 a^-4 e^(-m lambda(e)) ).

Then the conclusion of Theorem R holds with max( e^(-mR), a^(-L/2) ) replaced by max( e^(-mR), a^(-L/2), Z_rho/(C_A tau) ), where

  Z_rho = sup over Y and e of |beta sum_{p contains e} Im psi((p), Y)| / w((p), Y)

is the weighted centre defect of the response. Proof: step (d) of the proof of Theorem R, with one more entry in the maximum. QED.
This is the finite-N, region-uniform form in which T1 can be joined to (RESP): the class restriction of (RESP) (no weight outside the spectrum of W) is a choice of Cl, and line 2 is the centre row. Two things are then missing, and both are outside T1a:
- **(T1-C), OPEN.** A bound Z_rho <= theta Psi + C tau e^(-mR) with kappa theta < 1/2. By 11.2 it does not follow from (Z-lin) in the weights of section 5. For U(N) the centre row is the loop equation in the trace direction and is linear and exact; for SU(N) it is the tilt (Z-lin). So this is the place where the response equation reads SU(N) against U(N), and it agrees with row 1722's remark that the Maxwell line is where the groups must differ. GUESSED: the proof needs pinning of N sum_p Im x_p at scale one, that is a large-deviation statement for the U(1)-like variable, not a loop-equation estimate.
- That the responses of Theorem R are in the class of (RESP). Row 1722 argues this from an (LD)-type bound (eigenvalues outside the spectrum cost exp(-cN)). Not built here. The atom family shows that without it the linear bound fails.

### 11.4 Summary of the relation

(RESP) is a hypothesis about decay of solutions of a sourced linear equation at N = infinity. T1a (Lemma 1', Propositions E and B) is the proof that the finite-N response satisfies line 1 of that equation, with an explicit SU(N) source term, and with all remaining terms a small multiple of the weighted response on rows of at most L letters. T1 does not prove (RESP), and (RESP) at N = infinity does not give Theorem R: the Lipschitz, weighted, region-uniform form (RESP-Lip) is what the proof uses. Line 2 at finite N is (Z-lin); its relative control is (T1-C), open.

## Ladder update

| Rung | Change |
|---|---|
| T1 | SPLIT. T1a: exact response equation (Lemma 1', Proposition E) and relative error bounds on rows with at most L ~ N^(2/3) letters, uniform in N >= N0, region, holes, exterior (Proposition B). Status: PROVED by the author; needs the cross-provider check. T1a is line 1 of the (RESP) equation of row 1722 at finite N, with one more SU(N) source term. T1a': decay to the floor a^(-L/2) from a linear stability hypothesis (Theorem R; section 11.3 with a class and a centre row). Status: PROVED as an implication; the hypothesis (PS-Lip) is expected false on the weak side (row 1722), so use the form (RESP-Lip). T1b: floor-free form. Open; needs (T2-N). T1c (new): relative control of the centre row for the response, (T1-C). Open; the exact identity is (Z-lin) |
| T2 | RESTATED. Pinned short traces are enough for the equation rows; long words are paid by the weight a^|l|/|l|^2. The remaining long-word statement is (T2-N): the N^-2 merger and current terms on rows with more than L letters, with the degenerate SU(N) row (tr p)^(N^2) as the first test |
| T3 | Input now fixed: the response functional may be any signed measure that is SD-homogeneous link by link; holes and exteriors enter only through the set V and the number tau. Moment pinning replaces a hard cutoff, so no cutoff term appears in T1 |
| T4 | New data for the rank count: N0 = 16 (kappa C_N)^(1/2)/eta from T1 alone; Q >= L/2 + 1 moments |
| T6 | The linear operator of the response equation is D^e on single loops with a spectator factor. (R) at k = 1 with rho = N^2 Cov(., Re(c tr U_l')) is the finite-N equation of the planar connected response; its source is the merger with l' plus the SU(N) term t_e(l) t_e(l') E(tr l tr l')/n (section 11.2) |
| PS ladder | PS9 (RESP): add the Lipschitz, weighted form (RESP-Lip) of section 11.3 as the form that T1 consumes; add the SU(N) source term to line 1; line 2 at finite N is (Z-lin). The rung "(PS-Lip)" is not opened: by row 1722 it is expected false on the weak side |

RESULT: T1 built with a floor, not floor-free. PROVED (author only): a distinguished-loop single-link Schwinger-Dyson identity with spectators (exact check SU(2), SU(3)); the exact centred response equation, source only at links the perturbation reads; every error term a small multiple of the weighted response on sequences of at most L ~ N^(2/3) letters, uniformly in N >= N0, region, holes, exterior. This is line 1 of row 1722's (RESP) equation at finite N, with one extra SU(N) source term. Decay to a floor exp(-c N^(2/3)) follows from a linear stability hypothesis, which row 1722 makes doubtful on the weak side; restated with a class and a centre row (RESP-Lip). Diagnostics answered by additive centring and weights. Open: (T2-N) high-multiplicity N^-2 terms (degenerate SU(N) row (tr p)^(N^2)); (T1-C) the centre row, an order-one tilt (Z-lin), where SU(N) differs from U(N).
