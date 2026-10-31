# Net-tier gate report: upper-chain.md Text 10 and T1-net

Provenance. Opus 5.5 at high effort, checking text written by Opus 5.5 at max effort. This is a same-model check, not an independent one. Snapshot c3242879df. Nothing in the repo was edited or committed.

## Overall verdict

The mathematics of Text 10 is mostly right. I found no fatal error in Lemma 10.1, in Theorem 10.2 or in the Gaussian constant. Theorem 10.7 is a correct implication once its clauses are repaired, and the clauses as written do not match their own derivation.

T1-net as worded should not be accepted as a non-triviality statement. Every clause of it, including (WIT), (NF1) and (NF2), holds for a static classical random constant field with H = 0 (D1). The main term of the witness is the value for three free Maxwell copies (D2). A skeptical expert would call T1-net a compactness floor plus UV stability with fixed coupling at a physical scale. That is a substantial statement if proved, but it is not non-triviality, and it is not a Haag-Kastler net (D4).

| Item | Verdict | Right? | Hypotheses smaller? | Consumer delivered |
|---|---|---|---|---|
| Lemma 10.1 | ADVANCE | Yes. Exact tests pass. | None needed. | Theorem 10.2(e), exactly. |
| Theorem 10.2 | ADVANCE, floor only | Yes, with small fixes D10, D11, D13. | Non-witness clauses of T1-net need no input. | Those clauses of T1-net. Nothing toward non-triviality: the product law of Prop 10.4 satisfies all of it. |
| Blocked-net paragraph (line 477) | WRONG in two phrases | "each bounded measurable" (D10), "Haag-Kastler" (D4). | No. | The net is fine for a countable family of continuous F. |
| Prop 10.3 | WRONG as quantified, then CORRECT-NO-ADVANCE | "any finite window" is false (D9). The corrected form is right. | No. | No consumer: the witness runs on the hard core's trajectory, and "no degeneration" is vacuous (D3). |
| Prop 10.4 | CORRECT-NO-ADVANCE | Yes. Overreach in one sentence (D12). | No. | A valid no-go. |
| (WIT) paragraph (lines 491-493) | CORRECT-NO-ADVANCE | The spectral argument is right. The conclusions drawn from it are too strong (D1). | No. | None. |
| Lemma 10.6 | ADVANCE, conditional | The implication is right, and the arithmetic is checked. | CT4 and torus comparison are removed. | Moments for Theorem 10.7, but (FF_j) as stated is not what its derivation gives (D5). |
| Lemma 10.9 | CORRECT-NO-ADVANCE for (OS_j)(c) | Right in its own setting. | No. | Does not deliver (c) on G (D6). |
| Theorem 10.7 | ADVANCE, conditional | Constant and implication right. Clause repairs D5, D7 needed. | Sources and counterterms are gone. FF and OS remain. | (WIT) as literally defined. |
| Corollary 10.8 | ADVANCE, conditional | Right given uniformity in j (D8) and the flow (T1-T3 of hard-core--independent 8.4). | Same. | (WIT), (NF2). (NF1) carries no force (D2). |
| T1-net (line 101) | Reject as non-triviality | See D1 to D4. | n/a | n/a |

## Defects, most severe first

**D1. T1-net's clauses are all satisfied by a law with no dynamics (line 101; lines 491-493).** Failing case, checked exactly in `checks/gate_net_check_static_toy.py`. Pick one of the 6 coordinate planes (mu, nu) uniformly. Set all mu links to exp(i a rho sigma_1 / 2), all nu links to exp(i a rho sigma_2 / 2), and all other links to 1. Act on gauge-invariant functions, as Prop 10.4 does.
- Reflections: reversing axis mu sends sigma_1 to -sigma_1, which is a global conjugation by exp(i pi sigma_2 / 2). So F(rU) = F(U) for every gauge-invariant F, and Theta F . F = |F|^2 on each point mass. So RP holds, for any plane. Translation and hypercubic invariance are exact. The same holds for F o M, since F o M is a gauge-invariant function of the fine links.
- Numerics: sup |F(rU) - F(U)| = 0 on 108 loops, with a generic constant field as control at 2.5e-3. The RP Gram matrix has minimum eigenvalue -4e-14 and rank 6.
- The condition e_r0 = e_* is met by tuning rho, for e_* in (0, 1/3). The limit is neither flat nor Haar.
- (WIT): Cov(s_p, s_q) = s^2 (1/6 - 1/36) is non-zero at every separation.
- (NF1): <s([W_1, W_2])> > 0.
- (NF2): e_r ~ (r rho)^4 / 48 -> 0 as r -> 0, because s_p/(r rho)^4 -> 1/8. I computed this with straight products. For the actual M I rely on expansion and continuity at flat, and did not run M.
- OS space: dimension at most 6, H = 0, S_c(Theta B, tau_t B) constant in t. Line 493's "T_t != P_Omega" holds, with T_t = 1.

This law is not a Wilson measure, so it does not refute any theorem. It shows the listed properties do not separate an interacting theory from no theory. The missing clause is that H is not zero on the part of B orthogonal to Omega, or clustering. Clustering at D >> a_K is out of reach of the hard core. The cheap repair is below, under "Recommended wording".

**D2. The witness is Gaussian, and (NF1) is kinematics (lines 493, 553, 563).** The main term (3/2) g^4 P^2 is exactly what three independent free Maxwell copies give for the composite s. The proof uses no vertex.
- (NF1) is proved by a computation with colour-diagonal Gaussian b. I find c = 12 (P_11^2 - P_12^2), sampling-checked. It holds equally for the exponential of a 3-colour lattice Proca field, which is reflection positive for site planes. It also holds for the product law of Prop 10.4, which has no correlators at all. So (NF1) tests that the target group is non-abelian, and nothing else.
- omega_L(g) has no rate, so Theorem 10.7 cannot see the order-g effect of the three-gluon vertex.
- (NF2) is the only clause with force. It does exclude reflection-positive Gaussian vector fields, by an argument the text does not give. With a Kallen-Lehmann form, p^2 D(p^2) = int rho(m^2) p^2 / (p^2 + m^2) is nondecreasing in p, so e_r is nondecreasing as r -> 0. It also excludes the product law, where e_r grows like r^-2 under path averaging. But (NF2) is the asymptotic freedom of the trajectory restated in gauge-invariant form, and D1 shows that without a dynamics clause it can still be met.
- The phi^4 comparison at line 493 ("its analogue is false for phi^4") therefore rests on the coupling x_j of the hard core. That is not a property of the limit net.

Repair: a test that vanishes for Gaussian fields, for example the odd combination (1/2) Tr(W_1 W_2 W_3) - (1/2) Tr(W_1 W_3 W_2), proportional to eps_abc b_1^a b_2^b b_3^c. It should be of relative order g from the vertex (expected; I did not compute the coefficient). It needs omega(g) = o(g), and the first-order term of Lemma 10.9's Step 1 evaluated rather than bounded.

**D3. "No degeneration" in Prop 10.3 is vacuous (lines 479-483).** The conclusion "neither flat nor Haar" holds for the convex mixture (1 - e_*) delta_flat + e_* Haar. That is reflection positive, invariant, and made of two degenerate states. It also has (WIT), with constant connected correlator.
- Nothing in Theorem 10.2 or Prop 10.3 uses d = 4, SU(2) or the coupling flow. In d = 5, the Wilson theory is believed to have a first-order bulk transition (numerics, recalled). There the intermediate value theorem would place beta_i at the finite-volume pseudo-critical point, and the limit is believed to be exactly such a mixture. So the trajectory has no connection to asymptotic freedom or to scaling. The text says part of this ("nothing here shows that this trajectory is the hard core's"), but line 483's "non-degeneracy is free" overstates it.
- If e_i(beta) has a jump in the limit in d = 4, which is not excluded by anything here, the same applies. The clause should be dropped from what is claimed for T1-net unless a cluster or single-phase statement is added.

**D4. "Haag-Kastler" is not what this is (lines 101, 477).** The blocked net is a commutative algebra of bounded functions with an RP state. OS reconstruction gives vectors A Omega, not operators. A function with thick time support has no bounded action on H, and Theorem 10.2(d) does not claim one. There is no Minkowski algebra. There is no microcausality, since that comes from O(4) plus symmetry and only the hypercubic group is present. There are no boosts. As I recall, the known passage from a Euclidean net to a Haag-Kastler net (Schlingemann) assumes the full Euclidean group (recalled, not checked). Prop 10.4 and D1 are both "nets" in the sense of line 477. The sentence offered to the skeptic at line 101 should be withdrawn. Say instead: a reflection-positive Euclidean state on a local commutative algebra.

**D5. (FF_j) says constants free of L; its own derivation does not give that (lines 507, 512; hard-core--independent 3.1 item 6, 3.3(b), 4.6).**
- t_0 := min(c_A, c_F eps_0)/2 at line 512, and eps_0 <= c_1 L^-2, and small against C(L,R)^-1. So t_0 depends on L, at least like L^-2.
- C_2, C_3 contain C_E (line 512: "exp(C_E N ...)", "EE >= -C_E N"), and hard-core--independent 4.6 has C_E <= 2 E_0(L, M).
- Effect on Theorem 10.7, as written: <X_c> <= e^{C_4} / t_0, so E|phi_p||phi_q| <= C_s^2 L^(-2 kappa) * 16 e^{C_4(L)} / t_0(L). With t_0 at most order L^-2, this is at least of order L^(2 - 2 kappa) e^{C_4(L)}. There is no gain at kappa = 1, and no controlled gain at kappa = 2, because eps_0 may be smaller than any power of 1/L. "C_6, C_7 free of L" fails, and the step "L^(2 kappa) large against d^4" at line 553 has nothing to stand on.

Repair, plausible but not written:
- State (U) for the truncated exponent t x sum_I s_p 1_(f_p <= eps_0), at absolute t. Non-rough plaquettes are absorbed by energy, or by rough neighbours at t <= c_F, using that I has one plaquette per block.
- Use phi only on G, with eps_1 <= eps_0. The rough tail with t_0(L) goes into omega_L through G^c.
- Replace C_E by the second-order vanishing EE_Om(1) = 0, |EE| <= (E_0/alpha^2) sum f^2, absorbed by x large.

Without this repair the reduction at line 495 is not proved, although the Gaussian-level statement is certainly L-free.

**D6. (OS_j)(c) is not delivered by Lemma 10.9 (lines 528, 533-541).** Line 533 says that for hard-core--mapped (c) "is the following lemma". The lemma requires, on all of K, Hess(S) >= gamma/2 and |D_y R| <= eps Omega(y). (c) must hold uniformly on G, which only constrains W in B(D, R).
- Failing case: W with one rough plaquette far away. Since P(rough at a plaquette) > 0 at fixed g and the law is translation invariant, P(W regular everywhere) -> 0 as the volume grows, so the lemma's domain has vanishing measure.
- The mapped file itself says the fibre law is "a mixture over families of convex laws" (its 5.4), and the independent file's (EI) begins "Fix W regular" (its 4.6).
- C_W in (c) is also undefined as stated, since (a) defines V^* only near D.
- The missing step: condition on hole data, apply Lemma 10.9 to each conditional law, whose H differs from the global one by tails, and average using the polymer covariance. It looks doable. Line 102 is honest about this ("may not have written"), and line 533 is not.

Lemma 10.9 itself I checked: both steps are right given (C) and (M), and Step 2's telescoping over cells is uniform in the volume.

**D7. (OS_j)(d) has no tail term (line 529).** It says that sup over B(D,R) of |Psi_c(W)| = 0 forces |Gamma_pq(W)| = |Gamma_pq(1)|. Failing case: W flat on the ball with flux or non-trivial holonomy beyond it. The fibre covariance decays exponentially at rate c/L (hard-core--independent 7.3), and is not strictly local, so the left side is non-zero.
- Exact illustration of the holonomy effect, from `checks/gate_net_check_constants.py`: on a 2D SU(2) torus with V plaquettes, Cov(X_p, X_q) V^2 -> 1/2, not the 3/2 of Remark 3.3 with P_pq = -1/V. It reads 0.5046 at V = 4 and 0.5091 at V = 16, at beta = 2000. Var X -> (1/2)((1 - 1/V)^2 + 2), which reads 1.277 against 1.281 at V = 4, not (3/2)(1 - 1/V)^2 = 0.84. The reason is that generic flat moduli decouple only the Cartan colour from the zero mode. Remark 3.3's colour factor assumes the trivial holonomy.
- This does not hurt 10.7 at d << torus. It does show that the "flat background" in (d) needs care.

Repair: add C(L) exp(-c R / L), and let R(g) -> infinity slowly in omega_L.

**D8. No uniformity in j in (OS_j) (lines 524-531, 567).** Corollary 10.8 sends j = K_i - m -> infinity at fixed m. (OS_j) states omega, C(L), R with no j-uniformity, and "fixed L, D, eps_1" does not mention j. Failing case consistent with the text: omega_j(g) = omega(g) + j g. Each Theorem 10.7 holds, and the Corollary fails at fixed scale. Add "uniform in j". Also, the main term needs liminf_i g_(K_i - m, i) > 0. That holds by (T1)-(T3) of hard-core--independent 8.4: x_(K-m) <= 2 gamma^-2 + m (2 b log L + 2 C_0). So (WIT) and (NF2) consume (8.2) with exact b > 0, all levels below j, and the flow. "Reduced to one step" at line 101 is true per level only, and asymptotic freedom is an input, not an output.

**D9. Prop 10.3's "any finite window" is false (line 479).** Failing case: a one-link or tree window. By gauge invariance the law is exactly Haar on it, for every beta, and it is vacuously flat. The proof covers only windows that determine c. Corrected statement: non-degenerate on every window containing the determining set of c. In addition, by translation, hypercubic invariance and a union bound, the single-plaquette marginal at scale r is not delta_flat, so e_r > 0 for r <= r_0. "Not Haar" for a small window at r < r_0 is not proved.

**D10. Uncountable family in a theorem with a countable hypothesis (line 477 against line 460).** "Each bounded measurable gauge-invariant function F" cannot lie in a countable B, and no single subsequence need work for all measurable F if the laws of V^(r) concentrate as i grows. Restrict to a countable sup-dense set of continuous F, and extend by density. All uses in Text 10 survive (s_p and word traces are continuous).

**D11. Theorem 10.2(e), two points (lines 470, 473).**
- Lemma 10.1 bounds one cut. Moving an interior A^k alone crosses two cuts in opposite directions, so "bounded analytic functions on a strip" is not supplied by what is written. An exact search on 3D Z_2 found no violation of the sup-norm bound: alternating maximisation over all F, A, G gave a maximum of exactly 1.000000 in the 68 parameter rows completed (beta up to 0.44; I stopped it to keep the machine free). So this is a proof gap, not a false claim. Repair: separate boundedness in each gap with the others real, then a separately-analytic theorem (Siciak), at the cost of the radius.
- C_i is piecewise constant, so it is not Lipschitz. The true bound is K (|y - y'| + a_i), which suffices for the Arzela-Ascoli step. The constant 4 n depends on the norm.

**D12. "Any witness must therefore use four dimensions" (line 487).** The 2D example shows only d > 2. Failing case: 3D SU(2), where separated correlators are expected. The first sentence, "must use the Wilson weight", should read "must use something beyond the listed properties".

**D13. Small wording items.**
- Line 468: "open half-space" should read "at positive distance from the plane", because O_A is only bounded and a_i-fattening can cross. Theorem 10 at line 440 has this right.
- Line 512: "G = 1 there" should be G >= exp(-small N), since G is a ratio with N(1)/N_good(1) (hard-core--independent 4.7).
- Line 512 and Lemma 10.6: "density against Haar" means normalized by r_j(1) = 1, not mass Z. With mass Z, (U) would be false for j >= 1 by counting N_0 against N_j.
- L has two meanings. "L is odd" at line 514 is the blocking factor. "log(1/g_j) <= L/a_j" on the same line is the torus side. Text 0 has L as torus side.
- Y_p is both the remainder (line 527) and the conditional mean (line 557).
- Line 520 drops the factor C_1^(-3 b^4 / T), which tends to 1, so this is harmless.

## Question by question

**1. Lemma 10.1.** Free and right, line by line. T_1 = K P with K >= 0 follows from positive type of exp((beta/2) Tr g), and Mercer gives trace class. The trace formula, the Cauchy-Schwarz step, convexity of A_F, the torus-length count 2h + N = T for A_F at integers, and the Cauchy estimate and its integral are all correct. For x in (0,1), the terms with lambda = 0 only lower A_F, so the bound at x = 0 still applies. Oscillating (doubler) behaviour is excluded by lambda >= 0, which is the actual content.

It is the standard fact c(t) = <F, e^{-tH} G> with ||F Omega|| <= ||F||_inf, in a form uniform on the torus. Uniformity is real: sup_E E exp(-E t) = 1/(e t) for any spectrum.

Exact tests:
- 2D SU(2) with Polyakov loops: worst |f| = 0.47, worst t |f'| = 0.09, over beta from 0 to 400 and various S, T.
- 3D Z_2 on 2 x 2 x T with thick slabs and a non-diagonal transfer matrix: worst |f| = 1.000000 (saturated when F is close to 1 at large beta, never exceeded), worst t |f'| = 0.004.

I could not break uniformity. The queued exact check can be considered done at this level. There is no useful negative control at beta < 0 on this lattice: closed loops have even length, so T_1 stays nonnegative there (min eigenvalue/max about -5e-16).

**2. Theorem 10.2 and Prop 10.3.** Everything claimed in (a)-(f) is obtained with no input, after D10, D11, D13. The limit object is a multilinear functional on formal sequences, along a subsequence, not shown unique.
- It can be trivial: beta_i = 0, the product law, or D1. The theorem holds for any compact gauge law with site-plane RP in any dimension. The real-translation claim holds exactly as stated on mollified observables. Sup-norm continuity there is a property of the mollifier, not of the physics. The non-trivial content is (e) at ordered configurations, and it is right.
- The trajectory of Prop 10.3 has no connection to asymptotic freedom (D3).

**3. Prop 10.4.** Right. I checked it: a conjugation-invariant nu on SU(2) is inversion-invariant, since traces agree, so site-plane RP holds. Independence on disjoint links needs no gauge invariance. The law is not gauge invariant unless nu is Haar, but it is used only on gauge-invariant functions. The intermediate value theorem works, with t in place of beta. It rules out a witness from RP, invariance, consistency and one-scale non-degeneracy. The 2D statement is right on the plane. See D12 for the overreach.

**4. Theorem 10.7, Lemmas 10.6, 10.9.**
- Gaussian constant recomputed. s = 1 - cos(|Psi|/2) = |Psi|^2/8 + O(|Psi|^4), the covariance of flux is 4 g^2 P, ||Gamma_pq||_HS^2 = 48 P^2, and Cov(|a|^2, |b|^2) = 2 ||Gamma||_HS^2. So 96/64 = 3/2.
- P_pp = 1/2, so <X> = 3/4 and 9/2 per site. Single plaquette exact: <X> and Var X -> 3/2 (1.4996 and 1.4992 at beta = 1000).
- The three-term split 3/2, 3, 3/2 is recomputed.
- The Maxwell tensor is rederived from <A A> = delta G, including the value 0.6/(100 pi^2 d^4) and the zero at (d,d,d,d).

Lattice P_{12,12}, exact via Bessel heat kernel:

| x | P | P / Maxwell | (3/2) P^2 |
|---|---|---|---|
| (1,1,2,2) | 4.598e-4 | 0.756 | 3.2e-7 |
| (2,2,4,4) | 3.568e-5 | 0.939 | 1.9e-9 |
| (6,6,12,12) | 4.662e-7 | 0.994 | 3.3e-13 |
| (12,12,24,24) | 2.927e-8 | 0.9985 | 1.3e-15 |

(d,d,d,d) vanishes to 1e-16. P(0) = 0.50000.

The size matters. With supports of about 2 cells, ordering along four axes needs d of about 6. So the main term is 3e-13, omega_L must be below that, and L^(2 kappa) must exceed about 1.4e6 C. That is finite, as the theorem says, but it is not "absolute and modest".

Range: d << L^(kappa/2), so D = d r stays below the next spacing L r. The witness never leaves one coarse cell.

Hypotheses:
- Lemma 10.6 is right given (FF), and Lemma 1.2' is right (the run-doubling argument is checked).
- The error stays below the main term along the trajectory only after D5, D7, D8.
- No other hidden assumption, apart from: reflection covariance of the blocking (requested at line 107, not yet supplied by hard-core--mapped; for hard-core--independent, I did not check the field-chosen base point); that V^* is the centre of the fibre law (mean of xi is order eps, which Lemma 10.9 covers); and the bound on (a) being with finitely many c near p.
- Inconsistency: (FF) free of L is inconsistent with its derivation as written (D5). I found no outright contradiction among (FF_j), (FF_(j+1)), (OS_j), x_j <= 2 x_(j+1). The last follows from (T2)-(T3).

The witness does survive the limit at fixed (m, d): Cov(s_p, s_q) >= (3/4) P^2 x_max(m)^-2 > 0, given the flow and D8. At fixed D with r -> 0 it gives nothing, as line 569 says correctly.

**5. T1-net as worded.** If every clause were proved, this is what would be established. There is a subsequential limit state along the hard core's trajectory, on continuous gauge-invariant functions of blocked fields at L-adic scales. It is reflection positive and hypercubic and translation invariant. Blocked plaquettes have fixed small energy at a_K. At scales r below a_K, the connected correlator of s has its Gaussian value at bounded lattice separation, and e_r -> 0 as r -> 0. That is UV stability with a fixed physical coupling, in a compact field formulation. It would be a major theorem.

What is missing compared with an existence and non-triviality statement:
- Any non-Gaussian quantity (D2). The clause "with a test against a free field" is not a mathematical statement yet.
- Clustering or uniqueness of the vacuum (D1, D3), and a mass gap.
- O(4), and so Wightman functions or any Minkowski locality (D4). This one is explicitly deferred by GOAL.md.
- A point-like field, as the text admits. Also a stress tensor.
- Any estimate above a_K.
- Uniqueness of the limit.
- A definition. GOAL.md's T1 says "non-trivial" and does not define it.

Would a skeptical expert accept the witness as non-triviality? No. They would accept "the limit is not a product state on these observables". They would note it is also not distinguished from a static mixture, and that its leading term is free. They would note, in fairness, that (NF2) excludes reflection-positive Gaussian vector fields, and that a fixed coupling at a physical scale is exactly what fails in phi^4. That part is real and worth keeping, but it should be labelled UV stability.

## Recommended wording, if the lead keeps the milestone

Rename it "T1-net (UV stability on the bounded net)" and drop "Haag-Kastler". Add:
- (WIT+) At fixed r, for two separations along one axis with supports ordered, S_c differs and matches (3/2) g_r^4 P(d)^2 within a stated tolerance. So H is not zero on the orthocomplement of Omega. This kills D1 at no new cost beyond Theorem 10.7 at two values of d.
- (NF2) with the flow named as an input.
- Non-Gaussian test: state it as open (D2), and define "non-trivial" in GOAL.md. A clause list that calls Gaussian values a witness would mislead.

Before the proposal goes further, ask hard-core for: D5 (truncated FF), D6 (hole mixture), D7 (tail), D8 (uniform in j).

## What was checked and how

Line by line: Text 0; Lemmas 1.1, 1.2'; Lemma 10.1; Theorem 10.2 (a)-(f); blocked-net paragraph; Props 10.3, 10.4; (WIT) paragraph; (FF_j) and its derivation against hard-core--independent 3.1-3.3, 4.6; Lemma 10.6; (OS_j); Lemma 10.9; library Steps 1-3 at step level (Steps 4-5 not used); Theorem 10.7 with proof and constants check; Corollary 10.8.

Only read: Lemma 1.2, Theorem 1, Corollary 1.3, Theorem 10, Prop 10.5, Theorem 9 (for the contraction argument), Prop 8.4 of hard-core--independent (statement and (T5) proof read, not rederived).

Not checked: clauses (a), (b), (c), (d) for either hard-core map; the (R3) and 9.4 lift bounds themselves; (FF_j) as a true statement; reflection covariance of either blocking; the actual M on the toy; any 4D non-Gaussian SU(2) numerics.

Scripts, all in the gate2 folder, run with nice -n 10 and BLAS threads 1:
- `checks/gate_net_check_lemma101.py`: strip bound, models A and B, about 6 s.
- `checks/gate_net_check_constants.py`: 2D torus, single plaquette, lattice P, about 18 s.
- `checks/gate_net_check_gaussian.py`: sampling of the Gaussian algebra, about 6 s. The three-term split reads 0.002599 against 0.002400, within sampling error of about 3e-4.
- `checks/gate_net_check_static_toy.py`: D1.
- `checks/gate_net_check_interior.py`: D11, stopped early, partial output in `checks/gate_net_check_interior.out`.
