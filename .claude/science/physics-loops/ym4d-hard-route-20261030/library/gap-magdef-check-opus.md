# Check of rows 1646/1647 (magnetic action deficit), FINISH.md row 1648

Checker: Claude Opus 5.5 (row 1648, laptop subagent). Files checked: `library/gap-magdef-astra62.md` (row 1646, gpt-6.2-astra max, 242 lines) and `library/gap-magdef-neon.md` (row 1647, gemini-4-neon-xhigh, 405 lines). Checked by hand, line by line. No computation was run (no float guide, no Lean). Status: complete (2026-11-27).

## 0. Reading log

- FINISH.md rows 1641, 1646, 1647 (briefs and RESULT texts), read in full; RESULT texts of rows 1642, 1644, 1645, 1230.
- Both author files, read in full.
- Check 1639 (`library/gap-vir-down-e1band-check-opus.md`) and check 1640 (`library/gap-vir-down-e1band-neon-check-opus.md`), read in full.
- Row 710 section 8 (`library/gap-vir-sc.md` L186-203), read in full.
- Check 1630 (`library/gap-vir-down-twoside-check-opus.md`) section 1 (L20-69), read in full.
- Registry row VIR-DOWN (`library/open-registry.md` L1028).
- `library/prior/gap-trace-anomaly-lit-luna.md` (row 1645), read in full.
- Row 1227 (`library/gap-solve25-astra62.md`) L1-100 (the one-vertex model, (1)-(8)), read in full, because row 1647 Theorem 2 rests on it.
- Row 1386 (`library/gap-mech-direction2-fable.md`) L340-350 (K-I, K-II, K-III) and its RESULT; row 1553 (`library/gap-mech-direction4-fable.md`) L172-193 ((P-law), (P-scale), Lemma ALG, tests (g1)-(g6)).

Notation. b = -dm/dbeta (isotropic), b^E, b^M the temporal and spatial partial slopes, b^M = F(<V>_Omega - V)F (check 1640 section 1), a^an = beta(b^E - b^M), so b = a^an/beta + 2 b^M. Thermal sums: A = sum a^an e^(-tm), M = sum b^M e^(-tm), W = sum m e^(-tm). Then (1/t) d_beta G = A/beta + 2M (row 1647 (1.1); check 1640 (1.1)-(1.3)). (VIR-down) at rate kappa: (1/t) d_beta G >= kappa W. (MAG-def) at rate c_M: M >= c_M W.

## 1. Row 1646 (`gap-magdef-astra62.md`), line by line

**(1), uniform spatial susceptibility. HOLDS.** Redone.
- Ball restriction: radius B^(-1/2) balls have Haar mass >= c B^(-3/2); a plaquette with four links within B^(-1/2) of 1 has action <= 8/B; sS + BE <= C NM for s <= 2B. So F(1) >= -C NM (1 + log B). Convexity and F(0) = 0 give -E(sS + BE) = F'(1) >= F(1). With s >= B/2 and the symmetries, (2) follows. Correct.
- Selected links (direction 1, x_2 + x_3 + x_4 even): a (1, j) plaquette holds two direction-1 links whose bases differ by e_j, so of opposite parity; (j, k) plaquettes hold none. So no plaquette meets two selected links, and given the rest they are independent with densities exp(q_e . X_e). Correct.
- Pr(|H_e| < 3) <= 4 C'(1 + log B)/B: if |H_e| < 3 the four incident spatial actions sum to 4 - X_e . H_e > 1; Markov. Correct.
- One-link variance c |v|^2/(1 + |q|)^2: both regimes check (density >= e^(-8) Haar at |q| <= 4; the y = k(1 - z) density and two intervals at |q| >= 4). Correct.
- Var(S) >= E Var(S | rest) = sum over the NM/2 selected links. The time limit and centre invariance of the top vector (simple Perron vector) are correct. The sandwich lambda_0^M <= Tr <= lambda_0^(M-1) sum lambda_i is correct.
- Small point: |q_e| <= 6B at s = B (4 spatial staples times s, 2 temporal times B), and <= 8B after the shift h H_e with h <= B/2 in (7). The file's "10B" is a safe overcount. No effect.
Standing: the method is PR 10134 Theorem 3 (Var of the total action, cited by the file); new here only in the spatial-only source with the infinite-time vacuum. It is the extensive vacuum curvature of row 710 section 8 item 5 in quantitative form.

**(3), separate secants fail at a cold point. HOLDS.** Redone.
- Convexity of p_t for real t >= 1: the spectra of T_(s+d) = D*D and T_s^(1/2) e^(-dV) T_s^(1/2) = DD* agree; Tr K^t >= sum <psi_i, K psi_i>^t (t >= 1, Jensen on each spectral measure); <psi_i, K psi_i> = lambda_i <e^(-dV)>_i >= lambda_i e^(-d v_i); Jensen in the weights. So p_t(s + d) >= p_t(s) - d <V>_t at every s: convex. The trace-norm continuity of T_s^t gives p_t' = -<V>_t. Correct.
- First inequality: (p_t(s) - p_t(s-h))/h <= p_t'(s) and (a(s+h) - a(s))/h >= a'(s). Correct.
- Second: with delta = p_t - a = t^(-1) log(1 + G) >= 0, h L_h = -[a(s+h) - 2a(s) + a(s-h)] + delta(s) - delta(s-h) <= -gamma h^2 + delta(s). Correct, and the threshold for L_h < 0 is h^2 > (1+B)^2 log(1+G)/(c n^3 t). At t >= n/512 this is h >> (1+B)/n^2. Correct.
Standing: an obstruction to one proof technique (bounding the two pressures by separate fixed-width secants). It holds for U(1) and 5D SU(2) as well (file section 6, checked below). New as stated; small content.

**(10). HOLDS.** a(s) - a(s-h) <= h a'(s) - gamma h^2/2 from the supporting quadratic of (1) at s; delta(s-h) >= 0. Correct.

**(4)-(5), the interval estimate. HOLDS.** Redone.
- (5): T_s >= lambda |psi><psi| gives T_(s/2) = e^(sV/4) T_s e^(sV/4) >= lambda |e^(sV/4) psi><e^(sV/4) psi|, so lambda <e^(sV/2)>_psi <= ||T_(s/2)|| <= ||C_B|| <= 1 (kernel e^(-B(1-w)) <= 1, Haar normalised). Jensen gives <V>_psi <= (2/s)(-log lambda_0 + m), and -log lambda_0 <= C N (1 + log B) by the ball estimate and the time limit. Correct.
- Good event: within one slice every spatial plaquette meets at most one selected link (x_2 + x_3 even); sum over selected (4 - X_e . H_e) <= V(X_0); Markov gives the bad-event bound C[(1 + log B)/B + m/(BN)]. Correct.
- Total variation: the affinity of P_psi and Q_psi is E|f(X_-) f(X_0)| >= |E conj(f(X_-)) f(X_0)| = r; Hellinger gives TV <= sqrt(1 - r^2). Correct.
- Under Q_psi, given F, the selected links have the vacuum conditional law (the weight |f(X_-)|^2 is F-measurable), that is independent one-link Wilson laws with staples from X_-, X_+ and the exposed part of X_0. The concentration-function bound C d/sigma with sigma^2 >= c N/(1+B)^2 on the good event is the standard Esseen argument; the kernel k and the bound 1 - cos v >= v^2/4 on |v| <= 1 check. Correct.
- Uniformity: tm <= A and t >= n/512 give m <= 512 A/n -> 0; B ~ log n gives (1 + log B)/B -> 0. Correct.

**Visible thermal mixture. HOLDS.** Averaging (4) over a basis of J with weights r^t/G_J; sqrt(1 - e^(-2m)) <= sqrt(2m) and Jensen. Basis independence: correct.

**(6). HOLDS.** If Pr(|V - v_psi| <= w_0) <= 1/2 then Var >= w_0^2/2 and E|V - v_psi| >= w_0/2; the two positive parts of a centred variable are equal. Correct.
Standing: anti-concentration of the slice magnetic action at scale sqrt(N)/(1+B) in every low state. It says the sought O(m) difference sits under fluctuations of size sqrt(N)/B. New; non-selective (file section 6; I re-checked the U(1) density y^(-1/2) and the 5D counts 6 and 5).

**(7)-(8). HOLDS.** Redone.
- Vacuum Rayleigh quotient on T_s^(1/2) e^(-hV) T_s^(1/2): a(s+h) - a(s) >= log E_0 e^(-hV). Correct.
- (9): given F, V = c(F) - sum_e H_e . X_e with independent X_e, so log E_0[e^(-hV) | F] = -h E_0[V | F] + R_h(F) exactly. Jensen on the outer log gives a(s+h) - a(s) >= -h v_0 + R_h. Correct.
- R_h >= c_5 N h^2/(1+B)^2: second-order Taylor of Phi with the Hessian Cov_q X, on the vacuum good event (probability >= 1/2). Correct.
- q_J(h) >= h v_J + sum (r^t/G_J) log E_psi e^(h(V - v_psi)): Jensen on the diagonal of the compressed operator, then Jensen in the weights. Each correction >= 0. Correct.
- (8): e^x >= 1 + x + (x_+)^2/2, E[h(V - v)] = 0, Cauchy-Schwarz and (6) give E e^(h(V-v)) >= 1 + h^2 w_0^2/32. Correct.
- What (7)-(8) give. The vacuum curvature lost in a(s) - a(s+h) is about (h^2/2) Var_0 V, extensive. R_h returns (h^2/2) E Var_0(V | F), extensive. The state-side correction (8) returns only log(1 + h^2 w_0^2/32), which is logarithmic in N. So the residual numerator still carries an unsigned extensive difference, about (h^2/2)[Var_J V - Var_0(E_0[V | F])]. The file says so ("A remaining difference of finite-source measurements still needs a sign"). Correct as labelled: a partial piece, not a lower bound.

**Removal in the transfer insertion. HOLDS.** Conditional on the end slices and the exposed middle links, integrating the selected links turns V into E_0[V | F] = Vbar in the kernel of T_s V T_s. Contraction with an eigenvector gives lambda^2 v_psi in both. Correct; this is a conditional expectation inside a path integral.

**(11) and the mean identity. HOLDS.** Redone.
- Densities: r^2 + (1/2)|f_- - f_+|^2 >= 0 and (1/2)(|f_-|^2 + |f_+|^2) >= 0; both integrate to 1 since E|f_+-|^2 = 1 and E conj(f_-) f_+ = r^2 (two steps). Difference density r^2 - Re conj(f_-) f_+. Correct.
- E[conj(f_-) f_+ Vbar] = E[conj(f_-) f_+ V(X_0)] (f_+- are F-measurable) = r^2 E[|f(X_0)|^2 V(X_0)] = r^2 v_psi (reversible chain, E[f(X_+-) | X_0] = r f(X_0)). So E_+ Vbar - E_- Vbar = r^2 (v_0 - v_psi). Correct.
- Mixing with r^(t-2)/G_(J,t-2) gives G_J D_J = G_(J,t-2) int (Q_+ - Q_-) du; Jensen gives (11). Correct. The optimality of the comonotone coupling and the loss bound (e^x <= 1 + x + x^2 e^|x|/2) check, but (11) itself needs only Jensen.

**Section 5.1, the three-state family. HOLDS.** Redone.
- T g = g, T = r on g-perp; v_0 = sum pi_i V_i = 1/5 + 2(2/5 + m/2) = 1 + m; v_J = (3 - v_0)/2 = 1 - m/2; D_J = 3m/2; G = 2 r^t = 2/32 = 1/16 on the curve; W = mG; G_J D_J/W = 3/2; -m' = 3m gives (VIR-down) at rate 3; P >= (16/17)^2 = 256/289 > 457/625. Isotropic slope 6m against twice the magnetic slope 6m: A = 0. Correct.
- Limits: mu_+ -> pi = (2/5, 1/5, 2/5) and mu_- -> (1 - pi_i)/2 = (3/10, 2/5, 3/10). Quantiles: Q_+ = 0, 1, 2 on [0, .4), [.4, .6), [.6, 1]; Q_- = 0, 1, 2 on [0, .3), [.3, .7), [.7, 1]; Q_+ - Q_- = -1 on [.3, .4), +1 on [.6, .7), 0 elsewhere. int e^(-h(Q_+ - Q_-)) -> 4/5 + (1/5) cosh h > 1. Correct.
- So the right side of (11) is about -(G/h) log(4/5 + cosh(h)/5), negative and of order G, while G_J D_J = (3/2) m G is positive and of order mG. The fixed-width paired test fails by a wide margin in a family on the bounded-anisotropy branch (A = 0) where every target rate holds. Correct.
Standing: an abstract positive family, as the file says. It shows the fixed-width paired test is strictly stronger than (MAG-def), (VIR-down) and the numerical seed in that class.

**Section 6.** The sufficient set of three bounds: Sum r^t Tr(F b) = Sum r^t Tr(J(2 b^M + a/B)) + Sum r^t Tr((F - J) b) >= (kappa_0 + 2 eps - C/B - eps) W. HOLDS; ON FILE in substance (check 1640 section 2; row 1638 Theorem 1(3)). The photon and compact-Gaussian paragraph: ON FILE (checks 1639 section 5, 1640 section 2, 1644). Scope of the fluctuation estimate (U(1): y^(-1/2) density; 5D: N = n^4, six spatial and two temporal staples, constants 6, 5): HOLDS. The 5D paragraph is ARGUED/GUESSED as labelled. Spectator check: f_+- depend only on the spectator, so both score laws equal the vacuum marginal; HOLDS; ON FILE ((g4), rows 1553, 1628, 1631).

**Row 1646 verdict.** Every PROVED item HOLDS. No line fails; no correction needed (one constant overcount, harmless). The RESULT text is a fair summary. What it is: two obstructions to proof techniques ((3)/(10): separate secants; 5.1: fixed-width paired test), one anti-concentration estimate ((4)-(6)), and one partial lower bound ((7)-(9)) whose residual is an unsigned extensive variance difference. None gives a sign for the magnetic deficit.

## 2. Row 1647 (`gap-magdef-neon.md`), line by line

### 2.1 Theorem 1

**Notation (0.2), (1.1). HOLDS.** G = sum e^(-t m_i) gives (1/t) d_beta G = sum b_i e^(-t m_i) = A/beta + 2M. The forms M = ((1+G)/t)(t a_0^sigma - A_t^sigma) and A = (1/t) d_xi G check against Lemma D1. ON FILE (row 1618 Theorem 4(1), row 1638 Theorem 1(1), check 1640 section 1).

**Theorem 1(1), Kogut-Susskind. HOLDS.** Second derivation (mine, shorter): along (xi beta, beta/xi) the Hamiltonian is K/(xi beta) + (beta/xi) V = H(beta, beta)/xi exactly. So every gap is m/xi, and a^an = -d_xi m at xi = 1 is m on every eigenspace, which is (1.2). Then A^KS = W^KS and (1/t) d_beta G = W/beta + 2M, so (MAG-def) at c_M holds iff (VIR-down) holds at kappa = 2 c_M + 1/beta. The trace-class and differentiation steps (Kato type (A), Klein bounds, uniform tails) check. Standing: a guide model (the lane's object is the Wilson transfer). In substance ON FILE: row 710 section 8 item 4 ("the energy sum rule ... I see no reduction in strength"); new as a stated exact identity.

**Theorem 1(2), four-state heat-kernel family. HOLDS.** Redone.
- 2x2 block: e^(-L/(2 beta_t)) with L = w[[1,-1],[-1,1]] is (1/2)[[1+q, 1-q],[1-q, 1+q]], q = e^(-w/beta_t). As eta = e^(-beta v_wall) -> 0, lambda_+ -> a f(w/beta), d_(beta_s) log lambda_+ -> -v, d_(beta_t) log lambda_+ -> h(w/beta)/beta with h(x) = x/(e^x + 1). Correct.
- Vacuum in block A (V = v_A > 0), first excited in block B (V = 0): b^M = v_A > 0, b^E = (h(6) - h(2))/beta_0 < 0. My values: h(2) = 0.2384, h(6) = 0.0148, gamma_* = log(1.13534/1.00248) = 0.1245, so h(2) - h(6) - gamma_* = 0.099 > 1/12 (the file's rational bounds give 0.0879). b < 0. Correct.
- v_A > 2 c_M delta: 2 c_M delta <= 2 c_M/(30(1 + c_M beta_0)) < 1/(15 beta_0) < 0.0735/beta_0 < v_A. Correct. G -> e^(-t delta) <= e^(-4); purity >= (1+G)^(-2); 100 * 625 > 457 * 121. Correct. The epsilon > 0 perturbation by continuity: correct.
- Scope: here A/beta < -2M, and M/W -> v_A/delta, so |A|/W is at least 2 beta_0 c_M. The family lives on the unbounded-anisotropy branch, at one fixed coupling beta_0.

**Theorem 1(3), one-link Z_2 family. HOLDS AFTER CORRECTION (wording).** Redone.
- Tr = 1 + a, det = a(1 - c^2), cosh(m/2) = (1+a)/(2 sqrt(a(1-c^2))) = cosh(beta_s v/2)/sqrt(1 - e^(-4 beta_t)). (1.4) correct.
- (1.7): differentiating (1.4), b^M = -v sinh(u)/(sinh(m/2) sqrt(1-c^2)) < 0 and b^E = (4 e^(-4 beta_t)/(1 - e^(-4 beta_t))) coth(m/2) > 0. Correct.
- Bounds: u <= c/2 (v = e^(-2 beta_2)/beta_2 and e^(-2x)/x decreasing), c < sinh(m/2) < (6/5) c, (20/11) c < m < (12/5) c, b^E > (10/3) c > (25/18) m, -b^M < (11/(18 beta)) c < (121/720) m. So b > (7/6) m. Correct.
- Along t = t_0 e^(beta - beta_1): dG/dbeta = t (b - m) e^(-tm) > 0, G <= e^(-2) < 4/21, P >= (8/7)^(-2) = 49/64 > 457/625 (49 * 625 = 30625 > 29248). Correct.
- Correction: "(VIR-down), (HOT), (T-down) and (PUR-io) all hold" names lane statements about the calibrated Wilson SU(2) trajectory. In a two-state toy only their numerical shapes hold (a rate on one level, a small G at the right end, a purity number). Also A > (25/18) beta W: (VIR-down) is carried by the anisotropy, again on the unbounded branch, with |A|/W of order beta.

**Theorem 1(4). HOLDS (elementary); wording.** (1/t) d_beta G - kappa_0 W = A/beta + (2M - kappa_0 W). So (MAG-def) plus A >= beta(kappa_0 - 2 c_M) W gives (VIR-down); with |A| <= C W the two are equivalent up to C/beta. "If and only if" is right only in the sense the proof states (necessary when M = c_M W exactly). ON FILE in substance: check 1640 section 2 ("on the bounded-anisotropy branch (M-vis) is (E1) up to a rate shift O(C/beta): equivalent, not progress"); row 1646 section 6 says the same.

**Theorem 1 headline. HOLDS AFTER CORRECTION (scope).** "For discrete Wilson-type operators (MAG-def) and (VIR-down) are strictly incomparable" is proved only in abstract positive families of the form M C M (a 4-state heat kernel at one coupling; a one-link Z_2 model), and both examples need |A|/W of order beta or larger. For the Wilson SU(2) transfer on the band nothing is decided. On the bounded-anisotropy branch they are equivalent up to O(1/beta_K) (Theorem 1(4)). Row 1646 section 5.1 is the complementary fact: on that branch (A = 0) both rates hold together.

### 2.2 Theorem 2: the -1/3 limit, redone by hand

Setting (row 1227 (1), checked by check 1230, all items HOLD): one vertex, d links q_i = s_i + v_i in SU(2), V = 2 sum_(i<j) |v_i x v_j|^2, T = M_(B_s) (prod C_i,B_t) M_(B_s) on conjugation-invariant, centre-neutral functions. Put h = B^(-1/3), q_i = exp(h x_i).

*Derivation 1 (scaling).* The temporal increment z = exp(theta) has density e^(-B_t(1 - cos|theta|)), so theta has covariance I/B_t; in x it is h^(-1) theta, covariance 1/(h^2 alpha B) = h/alpha at B_t = alpha B. So 1 - C acts as (h/(2 alpha))(-Delta) + o(h). The spatial weight: v_i = sin(h|x_i|) xhat_i = h x_i + O(h^3), so B_s V = sigma B h^4 V_quart + O(h^3) = h sigma V_quart + O(h^3) at B_s = sigma B, with V_quart = 2 sum |x_i x x_j|^2. Hence h^(-1)(1 - T) -> L_(alpha,sigma) = -(1/(2 alpha)) Delta + sigma V_quart (row 1227 (6) at alpha = sigma = 1). Dilation x = gamma y: alpha^(-1) gamma^(-2) = sigma gamma^4 at gamma = (alpha sigma)^(-1/6), and the common factor is sigma gamma^4 = alpha^(-2/3) sigma^(1/3). So
  m_k(alpha B, sigma B) = B^(-1/3) alpha^(-2/3) sigma^(1/3) (eps_k - eps_0) (1 + o(1)).
Then b^M_k = -d_(B_s) m_k = -(1/B) d_sigma m_k |_(sigma=1) = -(1/3) m_k/B, and b^E_k = -(1/B) d_alpha m_k = +(2/3) m_k/B. So B b^M/m -> -1/3, b = b^E + b^M = m/(3B) (the toron rate 1/(3 beta_box) of checks 1630, 1639, there GUIDE), and a^an = B(b^E - b^M) = m: the toron sits on the bounded-anisotropy branch, as in Kogut-Susskind.

*Derivation 2 (virial; different route).* For -(1/2) Delta + V_quart with V_quart homogeneous of degree 4, an eigenfunction has 2 <kinetic> = 4 <V_quart>, so eps = 3 <V_quart>. And B <V>_psi = B h^4 <V_quart> (1 + o(1)) = h eps_k/3. So B b^M_k = B(<V>_Omega - <V>_psi) = -h(eps_k - eps_0)/3 = -m_k/3. Same constant. The -1/3 is the virial fraction of a quartic potential (for the free photon, a quadratic potential, the same computation gives b^M = -(1/beta) sum n tanh(omega/2), about -m/(2 beta) at small omega: fraction -1/2).

**Theorem 2(1). HOLDS (adaptation accepted as routine).** Only sigma near 1 at alpha = 1 is used in (2.6)-(2.7); the alpha-extension is unused. For d = 4: L_d >= 2|x_i| for every i (any j != i), so compact resolvent; the spherical-mean Harnack argument is dimension-free; the counting bound exponent 9d/2 and Tr T <= Tr prod C = I(B)^(-d) <= C B^(3d/2) (Tr(MCM) = Tr(C^(1/2) M^2 C^(1/2)) <= Tr C) check. The file writes the adaptation as "verbatim" and does not write it out; I accept it, since every step of row 1227 (2)-(8) uses one pair (i, j) at a time.

**Theorem 2(2), virial. HOLDS.** The cutoff dilation argument: d_a X_b = chi delta_ab + (x_a x_b/(R|x|)) chi', bounded on the annulus; potential term -2 int chi V phi^2 from x . grad V = 4V; limits by dominated convergence with finite form energy. Correct.

**Theorem 2(3). HOLDS AFTER CORRECTION (one quantifier).**
- Griffiths' lemma: correct as stated (convex, pointwise limit differentiable at s_0, s_n -> s_0).
- Convexity: the neutral trace is a sum over the 2^d twists of integrals with positive weights (c^prob > 0 everywhere), depending on sigma only through e^(-sigma B S); so f_B is convex. log lambda_0 is a limit of convex functions. phi_B(s) is convex in s by Hoelder. Correct.
- (2.8): -B^(4/3) <V>_Omega -> d_sigma(-sigma^(1/3) eps_0) = -eps_0/3. Correct.
- (2.9): f'(1) - g'(1) = -(tau/3)(<eps>_tau - eps_0). Correct. (2.10): t_B Ebar -> tau sum (Delta eps) e^(-tau Delta eps)/(1 + sum). Correct. Ratio: -1/3. Correct.
- (2.7): the Fatou upper bound (B^(4/3) V(exp(hx)) -> V_quart pointwise, strong L^2 limit is an eigenfunction at eps_k), the tail bound a_(B,k) <= eps_0 r_k^t (V >= 0), and the sum limit B^(4/3) M = (B^(1/3)/t_B)(1+G) B(t a_0 - A_t) -> sum a_k. The liminf argument with K_0 -> infinity is correct. Uniformity over any unit vector of a finite-B eigenspace: correct by the arbitrary choice of bases.
- Correction: (2.6) is proved for each fixed tau > 0, with t_B = ceil(tau B^(1/3)). The gloss "covering all cold points" claims a uniformity in tau (all t at least the cold time) that is not proved. It is true for each fixed cold tau.

**Theorem 2(4). First sentence HOLDS; the obstruction reading is ARGUED, not PROVED.** In the 4D one-vertex model there are cold traces with purity near 1, a proved gap eps_1 - eps_0 > 0, and M_B(t_B) < 0, B_M(psi_k) < 0 at large B. The step to "single-scale comparisons (such as row 1642 (2)) cannot carry a positive magnetic deficit without multi-scale running" (L170 and the RESULT, L404) is not a theorem: nothing in the file bounds what a comparison can carry, and a Hilbert-Schmidt comparison at one coupling carries no coupling derivative in the first place. Row 1642 (2) was proposed for (HOT), not for the deficit (check 1644).
Standing of Theorem 2. It is a fixed-lattice (one vertex), beta -> infinity statement. That is test (g5) of row 1553 (Remark STAB of row 1386): (MAG-def) at an order-one rate fails at a fixed lattice as beta grows. It fails there by size alone (b^M/m = O(1/B)); the sign is an extra. Identical in 4D and 5D. New: the anisotropic split of the toron rate (b^E, b^M) = (2/3, -1/3) m/B with a proof; the model is ON FILE (row 1227).

### 2.3 Theorem 3

**3(1). HOLDS.** On the isotropic n^D torus the hypercubic group makes every plaquette expectation equal; (D-1) n^D temporal and C(D-1, 2) n^D spatial plaquettes; at D = 4 the counts agree (3 and 3), at D = 5 they are 4 and 6. (3.1)-(3.4) follow by Lemma D1. Standing: a plane count. It reads the dimension only; Lemma ALG excludes it as a selective step (the file says so). New, elementary.

**3(2). HOLDS.** Delta_l(e^(-beta S)) = (-beta Delta_l S + beta^2 |grad_l S|^2) e^(-beta S) integrates to zero; Delta_l S = c_G sum_(p contains l) eps_p W_p (linear functions on S^c have eigenvalue -c). Summing over temporal links counts each temporal plaquette twice; over spatial links, temporal twice and spatial four times. (3.5)-(3.7) follow, with q_infinity from A_t/t -> a_0. Correct. The full force identity is ON FILE (rows 913, 934, 1618 Remark 4.1, 1619 section 3.3); the split is new, elementary. No sign.

**3(3). HOLDS.** (3.8): <w, (-Delta) w> = <M psi, (-Delta) M^(-1) psi> by C M psi = lambda M^(-1) psi; grad(M^(+-1) psi) = M^(+-1)(grad psi -+ (beta/2) psi grad V); the cross terms cancel. (3.9) by psi = Omega f and one integration by parts. (3.10): Delta V = 4 c_G (|P| - V); differentiate psi = lambda^(-1) M C(M psi). Correct. New, elementary identities; no sign.

### 2.4 Theorem 4

**4(1). HOLDS.** Inputs ON FILE (check 1622 section 2.1, row 1633 Theorem 2.1, row 1638 section 1.2 checked in check 1640): the flux energy 2 pi^2 beta_s |M|^2/n gives b^M = -2 pi^2 |M|^2/n; each photon mode gives -(1/beta) n tanh(omega/2) (a^2, (a^+)^2 compress to zero). So b^M <= 0, strictly unless the state is a pure rotor.

**4(2). HOLDS.** Coldness at t >= 3n, Q = 0: sin(k_j/2) >= 2|m_j|/n, arsinh(sqrt 3) = log(2 + sqrt 3) > 5/4, so omega >= (20/7)||m||/n and t omega >= 7.5 ||m||; the shell bound (26 r^2 vectors, r^2 <= e^(2(r-1))) gives log(1 + G_phot) < 1/15; the flux factor is below 1e-10; e^(1/15) <= 1 + 2/29 (tight but correct: 1.06894 against 1.06897). (4.3): tanh(x)/x decreasing, tanh(x_max) = sqrt3/2, so tanh(omega/2)/omega in (3/10, 1/2). Then -(1/beta) m <= b^M <= -(3/(10 beta)) m, and a^an in [3m/5, m]. Correct.
Standing: extends rows 1618, 1638 and check 1640 to magnetic fluxes and the full U(1)^3 projection. With Q = 0 the cold set is not empty (with the half-turn projection it is, check 1622 L79), so (MAG-def) fails at real cold points, by sign and by size O(m/beta). The model is the zero-monopole Gaussian, not interacting Wilson U(1).

**4(3).** ON FILE given the periodic Villain input (rows 1565, 1573, check 1644 section 1.6); the Q = 0 Wilson sign is ARGUED, as labelled.

### 2.5 Section 5 of row 1647

- 5.1 (one-loop Karsch running). ARGUED, as labelled. I redid the algebra: with beta_t^eff = xi(beta - Delta), beta_s^eff = (beta - Delta)/xi (overall coupling runs, anisotropy renormalises finitely), d_(beta_s) beta_t^eff = Delta/(2 beta_K) and d_(beta_s) beta_s^eff = (1 + B/beta_K)/2 at the isotropic point. So
  b^M_fine = (1/2)(1 + B/beta_K) b^M_ref + (Delta/(2 beta_K)) b^E_ref = m/(6B) - m/(2 beta_K),
  b^E_fine = (1/2)(1 + B/beta_K) b^E_ref + (Delta/(2 beta_K)) b^M_ref = m/(6B) + m/(2 beta_K),
  so b_fine = b^E_fine + b^M_fine = m/(3B) = b_ref exactly at this order.
  As Delta/beta_K -> 1, b^M_fine -> b_ref/2 and b^E_fine -> b_ref/2, and a^an_fine -> m. So in this picture the positive fine-lattice deficit is exactly half the box's isotropic rate, carried into the spatial coupling by the running of the overall coupling. The algebra is right; the premise (one-loop anisotropic running at a weak box) is GUESSED/RECALLED, not proved.
- 5.2 table, row (g2): "Reads the law (P-law), not the bare dimension" is not supported by anything proved: Theorem 2 gives the same sign and the same -1/3 in 4D and 5D. Correction: no 4D/5D separation is proved; the 5D fine-box failure is ARGUED. Row (g1): the proved U(1) failure (Theorem 4) is on growing tori and reads the photon dispersion and the flux energy, a property of the law; but the same O(m/beta) negative value holds in the 4D SU(2) one-vertex model (Theorem 2), so the proved items do not separate the two at any fixed size. Row (g3): ON FILE (row 1638 Theorem 1(4), check 1640): at strong coupling all three gapped models have B_M < 0, so (MAG-def) is not a property that reads the presence of a gap.
- 5.3: the equivalence verdict HOLDS as an elementary consequence of (1.1) (see section 3 below). The claim "On abstract Wilson-type transfer families, neither (MAG-def) nor (PUR-io) implies the other" HOLDS in abstract families only.
- 5.4: float guides only; not used.

**Row 1647 verdict.** No displayed inequality fails. Corrections: (i) the "strictly incomparable" headline is scoped to abstract M C M families on the unbounded-anisotropy branch; (ii) Theorem 1(3)'s lane names are numerical shapes only; (iii) (2.6) holds for each fixed tau, not uniformly over cold points; (iv) Theorem 2(4)'s obstruction for single-scale comparisons is ARGUED, not PROVED; (v) the (g2) cell of 5.2 claims a 4D/5D separation that nothing proved supports. The file's labels are otherwise honest, and the RESULT does not claim the band bound.

## 3. Question 2: is the reopen condition (VIR-down) restated?

**Kogut-Susskind form: yes, exactly.** Theorem 1(1) of row 1647 HOLDS (section 2.1; my derivation: H(xi beta, beta/xi) = H/xi). (MAG-def) at rate c_M holds at a point iff (VIR-down) holds there at rate 2 c_M + 1/beta. No reduction in strength.

**Wilson transfer on the band: equivalent up to O(1/beta_K) on the bounded-anisotropy branch; otherwise stronger, never weaker.** The exact identity is (1/t) d_beta G = A/beta + 2M (check 1640 section 1). So:
- (MAG-def) alone does not reach Theorem TR-down (row 1647 Theorem 1(2), an abstract family). The reopen condition "in the form that gives (VIR-down) through TR-down" is therefore (MAG-def) together with a lower anisotropy bound A >= -C W. That pair gives (VIR-down) at rate 2 c_M - C/beta_K.
- Conversely (VIR-down) at rate kappa_0 with A <= C W gives (MAG-def) at rate (kappa_0 - C/beta_K)/2.
- So with two-sided |A| <= C W the reopen condition and (VIR-down) are the same statement up to O(1/beta_K), with c_M = kappa_0/2. Without the upper bound, the usable reopen condition is strictly stronger than (VIR-down) (it asks the magnetic part and a lower anisotropy bound separately). It is never weaker.
- Which branch Wilson is on (GUIDE, not proved): a^an = m for the toron (section 2.2, from the scaling of (2.3)), a^an in [3m/5, m] for photons and fluxes (row 1647 Theorem 4), a^an -> m at one loop on the fine lattice (section 2.5). Both separating examples (row 1647 Theorems 1(2), 1(3)) need |A|/W of order beta or larger, that is an anisotropy response growing like log n. Nothing on file suggests that for Wilson.
Verdict: the reopen condition of row 1641 is (VIR-down) restated in magnetic variables, up to O(1/beta_K), on the expected branch. Equivalent is not progress. This was already the verdict of check 1640 section 2 on (M-vis); rows 1646 section 6 and 1647 Theorem 1(4) confirm it.

## 4. Question 3: does Theorem 2 force multi-scale running, and does (T-down) reduce to (K-II)?

**What Theorem 2 proves.** In the one-vertex Wilson model (no ultraviolet modes), at weak coupling, every cold excited level has b^M = -m/(3B)(1 + o(1)) < 0, in 4D and in 5D (redone twice in section 2.2). So a single-scale reference at weak coupling has the wrong sign and a vanishing rate b^M/m = O(1/B).

**What it does not prove.** It is not a theorem about all proofs. It does not show that every proof of the reopen condition must carry ultraviolet-to-infrared running. What follows rigorously is weaker and ON FILE: (MAG-def) at an order-one rate fails at a fixed lattice as beta grows (here by size alone; the sign is extra), so any proof must have content at lattice sizes growing with beta. That is test (g5) and property (P-scale) of row 1553, Remark STAB of row 1386.

**What the one-loop picture adds (ARGUED, section 2.5).** b^M_fine = (1/2)(1 + B/beta_K) b^M_ref + (Delta/(2 beta_K)) b^E_ref. The isotropic rate is single-scale at this order (b_fine = b_ref = m/(3B)), but the magnetic share is not: as Delta/beta_K -> 1 it moves from -m/(3B) to +b_ref/2. The positive deficit is the box's electric slope carried into the spatial coupling by the running of the overall coupling. In that picture the magnetic deficit on the fine lattice is half the isotropic rate, nothing more.

**Plain answer.** Yes in the sense the brief asks, with the label ARGUED: a positive magnetic deficit is a property of the bare-to-box running, not of any single-scale model, and on the band its size is half the order-one running rate. Proving it is proving how box energies respond to the bare coupling at order-one effective coupling, which is a renormalization step at order-one coupling: the (K-II) input of row 1386 ("the core of the open problem. No tool on file"). Theorem 2 itself proves only the one-vertex endpoint.

**Does the whole (T-down) line reduce to (K-II)? Yes, as a recorded judgement (not a theorem).** Grounds, each with its source:
- Theorem TR-down is proved and checked (checks 1613, 1630).
- (HOT) is supplied conditionally by row 1642 (2) (check 1644), and any fixed hot aspect is absorbed by the depth r (check 1630 section 1.3, check 1644).
- The one open input is (VIR-down) at a constant rate kappa_0 > 0 at the cold points of the window, from side L_h to L_h b^r (check 1630 section 1.4), subject to the running budget (RB).
- Every reformulation tried is equivalent to it up to O(1/beta_K) on the bounded-anisotropy branch, or stronger: loop tests (E1)/(E2) (checks 1634, 1635, 1639, 1640; row 1641), the magnetic deficit (section 3 here; check 1640). Two finer proof techniques for the deficit are proved too weak (row 1646 (3)/(10) and 5.1).
- Its content on the band is an order-one running statement; row 710 section 8 item 4 already said "no reduction in strength", and check 1639 section 3.4 called it "the K-II input of row 1386 itself".
There is no theorem that (VIR-down) needs a (K-II) step; the reduction is that no route on file reaches (VIR-down) on the band without one, and the two newest rows confirm the magnetic route is the same statement renamed.

## 5. Question 4: selectivity (Lemma ALG, row 1553)

No proved item in either file reads a property of 4D SU(2) that weak 4D U(1) and 5D SU(2) lack.
- Row 1646 (1)-(11): proved in the file for cosine U(1) (S^1 one-link law) and 5D SU(2) (N = n^4, six spatial staples); I re-checked the changes. They read the one-link Wilson law and lattice counting. 5.1 is an abstract family.
- Row 1647 Theorem 1: model-general (Kogut-Susskind; abstract M C M families).
- Row 1647 Theorem 2: identical in 4D and 5D SU(2); the photon analogue in U(1) has the same sign and size O(m/beta). It is a (g5) fixed-lattice statement.
- Row 1647 Theorem 3: identities valid for every group and dimension; 3(1) reads only the plane count (3:3 against 4:6), a dimension property that Lemma ALG excludes.
- Row 1647 Theorem 4: a U(1) computation. It shows the TARGET fails for (Q = 0) zero-monopole U(1) on growing tori at real cold points, reading the photon dispersion and flux energy (the law). That is target-level selectivity, half of it. The SU(2) half (a positive deficit on growing tori) is the open target, ARGUED only by one-loop running (section 2.5).
- (g3): at strong coupling all three gapped models have B_M < 0 (ON FILE, row 1638 Theorem 1(4), check 1640). So (MAG-def) does not read the presence of a gap; it reads the scaling region.

## 6. Question 5: new and on file

| Item | Verdict | Standing |
|---|---|---|
| 1646 (1) spatial susceptibility gamma = c n^3/(1+B)^2 | HOLDS | Method ON FILE (PR 10134 Theorem 3, total action; conditional one-link variance rows 1173, 1178); spatial-only form new |
| 1646 (3), (10) secant obstruction | HOLDS | New as stated; the extensive vacuum-subtraction wall is ON FILE in words (row 710 section 8 item 5) |
| 1646 (4)-(6) interval estimate, anti-concentration | HOLDS | New; tilt bound (5) from row 1236 (17); non-selective |
| 1646 (7)-(9) partial lower bound, exact removal | HOLDS | New; residual unsigned extensive term; no sign |
| 1646 (11) paired exterior-law test | HOLDS | New |
| 1646 5.1 three-state separation of (11) from the rates | HOLDS | New; abstract family on the bounded branch (A = 0) |
| 1646 section 6 sufficient bounds, photon, spectator, scope | HOLD | ON FILE (check 1640 section 2; checks 1639, 1644; rows 1553, 1628, 1631) |
| 1647 Thm 1(1) KS: a^an = m, (MAG-def) iff (VIR-down) | HOLDS | New as an exact statement; in substance ON FILE (row 710 section 8 item 4) |
| 1647 Thm 1(2), 1(3) abstract families | HOLD (scope/wording corrections) | New explicit families of the (A-vis) branch of check 1640 section 2 / row 1638 Thm 1(3) |
| 1647 Thm 1(4) consumer condition and equivalence | HOLDS | ON FILE (check 1640 section 2; row 1646 section 6) |
| 1647 Thm 2 toron b^M = -m/(3B), 4D and 5D | HOLDS (fixed-tau correction; obstruction reading ARGUED) | New proof; model ON FILE (row 1227, check 1230); toron rate 1/(3 beta_box) ON FILE as GUIDE (checks 1630, 1639); its use is test (g5) ON FILE (rows 1386, 1553) |
| 1647 Thm 3(1) plane-count reduction | HOLDS | New, elementary; dimension-only |
| 1647 Thm 3(2) magnetic Schwinger-Dyson split | HOLDS | Full identity ON FILE (rows 913, 934, 1618, 1619); split new |
| 1647 Thm 3(3) single-state identities | HOLDS | New, elementary |
| 1647 Thm 4 U(1) with fluxes, Q = 0 cold, M <= -3W/(10 beta) | HOLDS | Extends ON FILE photon/Gaussian results (rows 1618, 1638; checks 1622, 1640, 1644) |
| 1647 5.1 one-loop running mechanism | ARGUED (algebra checked) | New as a computation; premise RECALLED (Karsch-type one-loop anisotropic running) |
| This check: b^M_fine -> b_ref/2 reading; (T-down) reduces to (K-II) | ARGUED here | Builds on check 1639 section 3.4, check 1640 section 2, row 710 section 8 |

Independence: the two files are by two providers (gpt-6.2-astra, gemini-4-neon) and reached the same place by different routes (fluctuation estimates; identities and comparison models). My check is one more reader; my second derivations are the Hamiltonian rescaling for Theorem 1(1) and the scaling derivation of the -1/3 alongside the file's virial route. No computation was run.

What moved on the critical path: nothing. (MAG-def) on the band, (VIR-down), (HOT), (PUR-io) and the gap stay open.

## RESULT

Row 1646: every PROVED item ((1), (3)-(11), 5.1, scope, spectator) HOLDS; no line fails. It proves obstructions to two proof techniques
(separate secants; fixed-width paired test) and a partial lower bound whose residual is an unsigned extensive variance difference.
Row 1647: no displayed inequality fails. HOLDS AFTER CORRECTION: "strictly incomparable" only in abstract M C M families with |A|/W of
order beta; (2.6) for each fixed tau; Theorem 2(4)'s "single-scale comparisons cannot carry the deficit" is ARGUED, not PROVED;
the (g2) cell claims a 4D/5D separation nothing proved supports. The -1/3 redone two ways (scaling sigma^(1/3); quartic virial): HOLDS.
Equivalence: in Kogut-Susskind (MAG-def) is (VIR-down) exactly (rate 2c_M + 1/beta); for Wilson, with |A| <= C W, equivalent up to O(1/beta_K)
(check 1640 already said so); otherwise stronger, never weaker. Theorem 2 proves only the one-vertex endpoint, a (g5) fact ON FILE in kind.
One loop (ARGUED): the fine-lattice deficit is half the box's isotropic rate, carried by the running; so the route is the running input (K-II).
Selectivity: no proved item reads a 4D SU(2) property absent in weak 4D U(1) or 5D SU(2); Theorem 4 shows only that the target fails for U(1).
Recommendation: STOP the magnetic-deficit route, and record that the (T-down) line reduces to (K-II): TR-down is proved, (HOT) is absorbable,
and its one open input (VIR-down) on the band is an order-one renormalization statement with no method on file (row 1386).
