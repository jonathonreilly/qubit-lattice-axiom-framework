# FINISH row 913, gap-target-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone commit: bc7149dd9a822bc191600883b25a46c542b3b98b (branch claude/ym4d-hard-route, /Users/jonreilly/ym4d-lead/clone, read-only).
Author: Claude Fable 5.2, max effort. FINISH row 913. Date 2026-11-13.
Marks: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE, OPEN.

## Target statement (of this note)

Choose ONE target for the next Fable lane-hours on the crux of a mass gap for 4D SU(2) lattice Yang-Mills.
Rank the live attacks of row 912 by value per Fable hour. State the chosen target's crux lemma exactly.
Begin the attack with one real proof step. Say where it stops.

## Plan (one step per response; each step is appended here before the next starts)

1. Read D/library/gap-status-1113.md (row 912) in bounded ranges. Record the live attacks, walls and exact next statements. [READ]
2. Read D/library/gap-finishline-opus.md lines 110-160, the finish line (SEED-FP). Record it exactly. [READ]
3. Read the sources behind the two or three best-placed live attacks (the rows row 912 cites), only what the ranking needs. [READ]
4. Rank the attacks by value per Fable hour against the fact tests (U(1) Coulomb, Q_8 and 2T, no worst-case bound, no uniform layer bound above 1.0109, reaches order one). [ARGUED]
5. Choose one target. State its crux lemma, why it beats the others, its stop condition, and the work for Opus and Codex around it.
6. First proof step on the target: one lemma, by hand. [PROVED or where it stops]
7. Second stage of the same step if step 6 grows long; otherwise a hand check of step 6 against the fact tests.
8. Close: what is proved, what is open, the RESULT line.

## Step log

### Step 1. Row 912 read in full (D/library/gap-status-1113.md, lines 1-449). [READ]

What the note fixes, in the words the ranking needs.

1.1 The one missing input. READ L36-57: (SEED-FP) at one physical size, uniform in the cutoff. By Lemma SPLIT (rows 892, 893) it is two halves on one box: GLUE, S_ev(a; b^3) at most 1/10, and (CORE), Z^(v_12)/Z^0 at least 9/10 on one periodic torus (a,b,b,b), b at least 24a. No row proves either above beta_W 0.3609.

1.2 The proved range. READ L61-69: seed and volume-uniform gap for beta_W below 0.3609 (row 836, check 841). Band is 2.3 to 2.6 (GUIDE). Factor about 6.4 to 7.2 between them.

1.3 The live attacks and their next statements (READ L347-408).
- A1 free-wall engine: (JOIN-TH_kappa), thermal excess of the joining free energy of two cold free-wall boxes at most kappa g(a;B). Needs also a seed on one cold box and the OPEN limit-state node to (GAP). Doubling is "not structural" (direct-sum counterexamples, check 911). Needs "a quantitative single-phase input".
- A2 transport: THERM-DI-beta (glue only, coupling path from 0.3609, constant C uniform in the box) and THERM-DI-pin (glue plus flux). No constant supplied on any subinterval. Lives on the bare Wilson window, not first passage.
- A3 (VAR-SLAB): flux half at one coupling from the gauge-invariant Langevin gap lambda and an L^2 force response (FR). lambda at order one sits behind wall W2. E|grad X|^2 not bounded below its trivial size.
- A4 EXC and (DRESS): an order-L_i lower bound on a boosted magnetic-cut response. Gives (E17), a rate the seed chain does not need. Margin thin (gamma about 0.010); R''(0) negative.
- A5 decoder: (SEED-DEC-U) with (S1), a local perimeter law for the equal-time 't Hooft functional; and (S2), a 3D +-J rigidity question. Filling-Peierls barrier 1/9 against GUIDE 0.33.
- A6 (KURT) floor: kappa at least 1.66 for the flux ground function at one SH box. Needs GLUE at a very strong level (Corollary K'). One tube has kappa 1.53 (GUIDE), so floor "must come from transverse extent".
- A7 glue half (GLUE-FP): (Z0) with (COUNT) (Lemma G5, constant 110592). "No tool is named for the glue half at order one."
- A8 others: EXIT (order-one hand-off), (E17-phys-CA), HA off the real axis, Theorem S1 on the thin torus, (SE), (KS-ZONE), (INC-FP).

1.4 The five walls and what each leaves open (READ L298-345). W1: background-uniform layer bounds false above 1.0109. W2: annealed (AN1) is the worst case. W3: clustering cannot give the flux half (conserved Z_2 charge on the torus). W4: path counting fails at real densities. W5: (KURT)/(WALL)_40 is the hard problem again. Shared assumptions SA1-SA5: unit lattice at one beta in bare variables; uniformity in a conditioning variable; absolute values where the truth is a signed likelihood ratio; the torus; one coupling. The joining reading: all five close ways to prove ONE comparison of two symmetric Gibbs laws at one plaquette (Proposition MIX, row 708).

1.5 Structural facts that bear on the ranking.
- Every attack lives at ONE bare beta_W in the band, except EXIT and (E17-phys-CA). The real object is first passage. A bare-window seed "does not replace" (SEED-FP) (L30). So A1-A7 each still need a hand-off or weight comparison after success. READ L30, L363.
- Remark UNTW (row 895, check 896): untwisted free energies determine S and never S_ev. Every proved seed proves both halves or neither.
- Checks overturned 33 claims. Negative claims were overturned as often as positive ones (rule 7). So "stopped" attacks are not dead.
- SA5 (one coupling) is broken only by prior lane work of row 708: Theorem D-shape, Lemma M, Proposition MIX, with open inputs (NOCRIT), (VIR-log), (BOOT_eps).

1.6 First observation for the ranking. ARGUED. The attacks split by what they would deliver per success:
- whole seed at one coupling: A1 (with seed on a cold box), THERM-DI-pin, EXIT.
- flux half only: A3, A4, A5, A6. Each then still needs GLUE, and A6 needs GLUE at 160^(-16)-type levels.
- glue half only: A7, THERM-DI-beta.
GLUE has no named tool. So a flux-half-only target cannot finish; a target that carries both halves, or the glue half itself, is worth more per success.

Stop of step 1: row 912 read. Next: the finish line text.

### Step 2. The finish line (D/library/gap-finishline-opus.md L100-160). [READ]

2.1 (SEED-FP). READ L113-117. Fix odd L, g at most gamma_H, first-passage data (K, beta), beta in W_K(g), bare spacing a_K = L^(-K). There are K_0, a physical size ell with ell/(2 a_K) an integer at least 3, and s_* below 1/5041 with
  S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) at most s_*  for every first-passage datum with K at least K_0.
S is the thermal sum of the BARE Wilson transfer operator on the periodic cube of physical side ell at physical time ell/2.

2.2 Two forms on the account's own tori. READ L119-124.
- (SEED-Delta): limsup of [log of the integral of rho_K on T_ell] - f_K (ell/a_K)^4 below 6.1e-4.
- (SEED-L): limsup of Phi_L = L^4 F_(K,ell,beta) - F_(K+1,ell,beta) at most phi_* below (L/2) log(13/10), about 0.131 L. By the dilation identity (Sussman and Alpoge, SA L6863-6869) this is "the defect of one more block step on one torus at one bare coupling".
- Lemma FL (L126-132) turns (SEED-L) into (SEED-FP) at the size 6^(k_1) L ell.

2.3 What the consumer uses. READ L111: Theorem S uses only (TM) (a positive trace-class transfer operator in each direction) and the invariance of Z under exchange of two axes. It "holds for every group and for every symmetric model with positive transfer operators".

2.4 Effective action or Wilson. READ L134-141. The seed must be on the actual measure (bare Wilson along first passage, equivalently the total masses of rho_K). A seed for a plain Wilson weight at the unit scale does not give (SEED-FP); the account bounds the difference only by e^(O(ell^4)). No comparison is known (OPEN).

2.5 My reading of the finish line for the ranking. ARGUED.
(i) In bare terms (SEED-L) is a plain finite-size statement at ONE bare beta: with N = ell/a_K sites per side,
   0 <= Phi_L = L^4 log Z_N(beta) - log Z_(LN)(beta) <= 0.131 L.
   (The lower bound is the reflection-positivity monotonicity behind Lemma Z'.) Since Phi_L(beta = 0) = 0 and d/d beta of log Z is the plaquette sum,
   Phi_L(beta) = 6 (LN)^4 times the integral over [0, beta] of [e_N(b) - e_(LN)(b)] db,  e_M = mean plaquette on the torus M^4.
   So the seed is the coupling integral of the finite-size shift of ONE local mean. This is the (PATH) form (row 861) and it breaks SA5.
(ii) The seed is needed for every large bare beta at N of order 20 correlation lengths of that beta. The "band 2.3 to 2.6" is where a Wilson weight would have order-one effective coupling at the unit scale. A one-coupling result in the band is therefore never the finish line by itself. Every attack A1-A7 of step 1 shares this. Only EXIT and the (PATH)/transport family touch the uniformity in beta.
(iii) The consumer is group-blind (2.3). So all SU(2) content must enter through the seed.

Stop of step 2. Next: read the sources of the best-placed attacks: the transport family (rows 708, 905, 908), the hand-off (rows 846, 861) and (VAR-SLAB) (row 899).

### Step 3a. Sources behind the transport family (FINISH.md rows 708, 710, 711 RESULT text). [READ, with my reading ARGUED]

3a.1 READ FINISH.md L785 (row 708, `library/gap-mid-max.md`, unchecked there; check = row 709). Theorem TR and Corollary TR1: if on one cube b^3 the thermal quantity G falls along the coupling no faster than a logarithmic rate K ((VIR_K)), with the integral of K over [beta_0, beta_1] at most log(b/(2 ceil(log_2 b))), the strong-coupling seed at beta_0 is carried to beta_1. Remark LEV: the same from (LEV_K), no ordered level falls faster than the rate K. Theorem CRIT: the set of couplings with a seed is open; at a finite first end no size has a seed. What failed: (VIR_K), three ways. "The natural bound gives K about 0.4 where published values need about 3.3" (GUIDE). New test K7: a mixed fundamental and adjoint SU(2) weight has a first-order line (RECALLED, Bhanot and Creutz) and shares group, centre, reflection positivity, curvature and one-loop coefficient with Wilson. "So a proof at every coupling must use the Wilson weight itself (its loop equations), not the group."

3a.2 READ FINISH.md L787 (row 710, `library/gap-vir-sc.md`, unchecked). Theorem U: s d(log lambda)/ds = electric number of the state minus s times its spatial action and a correction. "Theorem U is the lattice action sum rule at every coupling; at order-one coupling (VIR_K) becomes a statement about magnetic and entropy deficits of an excited state, and before any constant it contains the locality of an excitation against the vacuum." So the transport route does not avoid the mixing input.

3a.3 My reading. ARGUED.
(i) The level form of THERM-DI-beta is: for every level i of every box, -d log(E_i - E_0)/d beta at most C. By the action sum rule this bounds the lattice beta function, -d log a/d beta at most C. Asymptotic freedom predicts C near 6 pi^2/11 = 5.38 for SU(2). The box must grow like exp(C beta). A transport constant uniform on [0.36, infinity) is therefore the WHOLE lattice gap at every beta, hence (SEED-FP) itself with no hand-off. On a bounded interval it is a bare-window result only.
(ii) K7 is the sharpest fact test in the lane and row 912's brief does not list it. The mixed action has a critical endpoint at order-one (beta_F, beta_A). There the 0++ mass vanishes. Wilson at beta 2.2 to 2.3 sits an order-one distance from that endpoint in a space of actions that share every structural property the lane's tools use. So a seed at bare Wilson beta in the band is a QUANTITATIVE statement about one action. No structural inequality (reflection positivity, centre symmetry, group moments, curvature) can decide it.
(iii) The same holds for the true object. At first passage the effective weight is not Wilson (step 2.4), and at order one nothing places it relative to the endpoint. So order-one attacks A1 to A7 inherit K7 twice: once for the bare window, once for the comparison.
(iv) The strong-coupling series in the character coefficient has a finite radius set by the complex singularities of the crossover near beta 2.2 (RECALLED, not read; GUIDE only). So no expansion that is analytic in beta on a disc centred at 0 reaches the band. The proved range 0.3609 is inside that disc; the band is outside. This agrees with check 870: HA fails in background-uniform form.

Partial stop (response length). Left for step 3b: the hand-off (EXIT) sources (rows 846, 861) and Proposition MIX of row 708; then (VAR-SLAB) (row 899).

### Step 3b. The hand-off sources and what they imply for the ranking (rows 846, 861 RESULT text; `library/gap-mid-max.md` L44-97). [READ, with my reading ARGUED]

3b.1 READ FINISH.md L923 (row 846) and L938 (row 861). EXIT: exact block steps past first passage must land the last-scale density in an explicit open zone O (zone radii of order 0.05 to 0.14 at beta 1/9 to 1/4). Row 861: a soft step gives the per-link size for free (Proposition FREE); the vacuum constant of any exact step is F_T - log Z_T (Proposition VAC), so soft step plus HO is circular; PIN-MIX is proved only for beta below 0.0384. "No quantity monotone along exact steps and not group-blind was found." "The account gives no block-law statement (CA-I L2555-2561)."

3b.2 READ `library/gap-mid-max.md` L46-49 (row 708, Fable max). "The Wilson weight differs in one exact point: it is the exponential of a function that is linear on R^4, restricted to the sphere SU(2) (log-linear in x; the adjoint term makes it log-convex in x). I found no inequality that uses this." And C-E (L79-86): the loop equations (SD_s) with (SYM) are the only candidate whose proof object must change when the weight changes.

3b.3 Three structural points for the ranking. ARGUED (mine; none is a theorem here).

(P1) The two halves differ in kind.
- The GLUE half is the bulk mass gap. It is exposed to K7: at the K7 end point the scalar mass vanishes with every structural property intact, and the lane has a proved relative of K7 (Proposition V of row 712, after van Enter and Shlosman). So no proof of GLUE at order one can be structural. It must be quantitative in the weight.
- The FLUX half is confinement of electric flux. On the K7 line both phases confine (RECALLED), so K7 does not obstruct it. It must fail for U(1) Coulomb and for frozen finite groups, which a proof can arrange by using the Lie algebra (integration by parts) and non-commutativity. So a structural proof of the flux half is not excluded by any fact test. It is the old confinement problem; any positive tension, however small, serves (E17).

(P2) Tolerance. RECALLED (not read; GUIDE only): the binary tetrahedral gauge theory freezes near beta 2.24, 2O near 3.2, 2I near 5.8; U(1) has its transition near 1.01; the SU(2) fundamental-Higgs (pin) model has a first-order line ending near (beta, kappa) = (2.73, 0.71); the K7 end point is near (1.5, 0.9). The band 2.3 to 2.6 sits between 2.24 and 2.73. Hand majorants in this lane lose a factor 5 or more in beta (0.3609 against a true range with no end). So on the bare window a hand proof must be exact (an identity or a sharp inequality), not a majorant. This applies to A1, A2, A3 (through lambda), A6, A7 in full.

(P3) What reaches the finish line. (SEED-FP) is uniform in the cutoff at a fixed PHYSICAL size. A lattice gap at every bare beta with a non-sharp rate gives a seed size b(beta) = exp(integral of K) that outgrows the correlation length if K exceeds the true rate, so the physical gap bound tends to 0. So even "a gap at every beta" by transport does not give (SEED-FP) unless the rate is asymptotically exact. The only forms that carry the uniformity for free are those on the account's own objects: by the dilation identity every first-passage datum is one unit-lattice effective density at one coupling g. There the seed size is 20 xi(g), of order exp(c/g^2) units. No small parameter exists at that size.

3b.4 A layer identity, recorded because it sharpens W1. ARGUED, short proof sketch; equivalent in content to row 839's Proposition TB with the supremum removed.
Let Lambda_k be the links in direction 3 between heights k and k+1, and eta all other links. Given eta, the links of Lambda_k form a three-dimensional O(4)-type spin model in the background (A, B) of the two adjacent slices. Put r_k(eta) = (its partition function with the spins antiperiodic in direction 0) / (the same, periodic). Then for every k,
   Z^tw_(03) / Z^0 = E[r_k(eta)]   (expectation in the untwisted torus measure),
because the twist sheet can be placed inside layer k and the two Boltzmann weights differ only on plaquettes of the layer model. W1 is the statement that inf over eta of r_k is small above 1.0109 (flat eta). (CORE) is the statement that the MEAN of r_k is at least 9/10. The gap between the two is the law of eta, which is the full measure. This is the average-case form the walls leave open (SA2).

Partial stop (response length). Left for step 3c: read the flux-half attacks' exact next statements in their sources (EXC check 881; (VAR-SLAB) Step 7 of row 899), then rank.

### Step 3c. The flux-half reductions already in the lane, and the shape of the transport crux. [READ and ARGUED]

3c.1 READ `library/gap-wall-assume-max.md` L253-355 (row 899; check 901 holds its lemmas). The lane already has: (T1) d/d beta log r = sum over p of (<x~_p>_tw - <x_p>_0); (T3) Var_w(rho) = 4p(1-p) at the half torus; (T6) (VAR-SLAB). Its ranked idea 4 is my 3b.4: "a quenched layer bound on a good set with a chessboard bound for the bad set. Needs a decay tool for frustrated O(4) layers at beta 2.3, which does not exist". Its 7.4 stop: the route "returns the flux energy". So my layer identity is known in content. Fresh thought on the same inventory re-derives the inventory (row 878's lesson holds for me too).

3c.2 Literature coverage, a grep count over library/ and FINISH.md (files that mention the name): Tomboulis 50, Mack 41, Yaffe 40, Chatterjee 33, step-scaling 20, toron 19, Luscher 18, Tanizaki 13, hierarchical 35, Griffiths 33, Ginibre 30, two-scale 40, log-Sobolev 30, Dobrushin-Shlosman 26, Kadanoff 27. So the standard tools were met. A new input will not come from a name on that list.

3c.3 The transport crux in its sharpest elementary form. ARGUED here; (i)-(ii) are two-line computations, written for the Kogut-Susskind form to show the structure (the Wilson transfer form is Theorem U of row 710).
(i) Take h(lam, x) = lam K_E + x W, K_E = (1/2) sum of link Casimirs >= 0, W = sum over spatial plaquettes of (1 - x_p) >= 0. Every level e_i(lam, x) is homogeneous of degree 1. With Feynman-Hellmann, for the gap D_i = e_i - e_0:
   x dD_i/dx = D_i - lam (<K_E>_i - <K_E>_0).
So the logarithmic rate is K_i := - d log D_i / d log x = (electric excess of the state)/(its energy excess) - 1.
(LEV_K) is the statement: the electric-energy excess of every level is at most (1 + K) times its energy excess. Equivalently, its magnetic excess is not more negative than -K D_i.
(ii) Absolute levels satisfy 0 <= x de_i/dx <= e_i, from K_E >= 0 and W >= 0. The whole difficulty is the vacuum subtraction, as row 710 found: the excesses are differences of extensive positive quantities.
(iii) What the no-critical-point conclusion needs. If K_i <= c (1 + log(1/m)) whenever the box has gap at least m, then m' >= -c m (1 + log(1/m)) and m stays positive at every finite coupling. A critical point with exponent nu has K of order m^(-1/nu). Asymptotic freedom has K bounded in the plaquette normalization. A tunnelling splitting in a double well has K of order log(1/D). So the target is an inequality of order one with one logarithm of room. This is why row 708 called it "an inequality of order one. No small number has to be proved."
(iv) Its limit. A lattice gap at every beta by transport reaches (SEED-FP) only if the rate is nearly exact at weak coupling: the seed size is exp(integral of K) and the irrelevant-operator suppression buys only a fixed power of the cutoff. So transport gives a LATTICE theorem (no phase transition, a gap at every beta), not the continuum gap. The same is true of every one-coupling attack. Only the hand-off (EXIT) is on the continuum finish line, and it has no tool (3b.1).

3c.4 Position before ranking. ARGUED.
- No live attack has a visible proof at order one. I put the chance of a checked proof of any listed next statement at order one, in a few lane-hours, below 1 percent each. I do not hide this.
- The attacks differ in what a proof would be: GLUE-type statements must be quantitative (P1, P2); flux-type statements can be structural; transport needs one order-one inequality with a logarithm of room and carries both halves.
- So the ranking turns on three questions: does the statement carry both halves; is it structural or quantitative; is there a first step that is a theorem and not a restatement.

Stop of step 3 (three parts). Next: step 4, the ranking table.

### Step 3d. A repo check that changes how I rank: the lane already owns the transport-map form. [READ]

3d.1 While preparing the ranking I derived three "new" forms of the transport crux: (a) the log-rate of a gap equals 2x times the difference of the means of the Poisson corrector U = (-L)^(-1)(W - <W>) under two probability laws attached to the eigenstate; (b) a volume-uniform one-sided Lipschitz transport of the Gibbs measure along the coupling carries every Langevin eigenvalue (rate K = 2 sup lambda_max(Hess U)); (c) the Langevin gap, uniform over tori, gives the transfer gap on every periodic box without the seed. Before writing them as a first step I searched the lane (grep counts: "transport map" 8 files, "Lipschitz transport" 1, "Poisson equation" 14, "Polchinski" 17, "Bauerschmidt" 25).

3d.2 READ `library/gap-skeleton-max.md` L107-111, L207, L240-255, L317-321, L482-483, L520-535 (row 669, Claude Fable 5.2 max; not checked by another model per its own table). The lane has all three:
- "CRUX (T). There is c < infinity, independent of Lambda and of b >= b_0, such that Hess phi_b(U) >= -c for all U, where L_b phi_b = A - mu_b(A)." (L107)
- "(T-avg) <Hess phi_b(grad f_b, grad f_b)> >= -c <|grad f_b|^2>" is "the form that is necessary and sufficient" (L240, L255).
- "(T), pointwise, is false for the product transport in a solvable model, and (T-avg) is the conclusion in differential form. B1 keeps its exact identities and loses its handle." (L317) For the gradient transport the pointwise bound "holds to first order in that model ... it is not decided" (L433, L483).
- "How it dies": the second derivative of the Poisson equation has the source "b grad^3 A . grad phi ... the cubic vertex contracted with the field; it has no sign, and the inverse on the left is infrared-singular" (L111).
READ `library/gap-transport-check.md` L183: the Lipschitz transport literature (Kim-Milman and others) was "not tried", recalled as needing a bounded perturbation.
So (a)-(c) are re-derivations. I do not present them as steps. This is the third time in this note that fresh thought returned the inventory (3c.1, 3c.3, here). It is evidence for row 878's rule and it bears on the choice: a target must bring a NEW INPUT, not a new framing.

3d.3 One exact Wilson identity I use below. PROVED (two lines; I did not find it stated in this form in the files read, which is a search result, not a novelty claim).
Let A = sum over plaquettes of (1 - x_p) on M = SU(2)^E with the bi-invariant metric in which the fundamental character has Laplace eigenvalue -3/4 per link, and L_b = Delta - b grad A . grad. Each x_p is a product of four fundamental matrix elements, one per link, so Delta x_p = -3 x_p and Delta A = 3 (N_p - A). Hence L_b A = 3 (N_p - A) - b |grad A|^2. Taking the mean: N_p - <A> = (b/3) <|grad A|^2>. Subtracting:
   A - <A> = -(1/3) L_b A - (b/3) ( |grad A|^2 - <|grad A|^2> ).
So the transport corrector is phi_b = -A/3 - (b/3) chi_b with L_b chi_b = |grad A|^2 - <|grad A|^2>. The first part has a bounded Hessian. So (T) for the Wilson weight is exactly a one-sided bound on the Hessian of the corrector of the squared force. The identity uses that the Wilson weight is an eigenfunction of the Laplacian plus a constant. It fails for the mixed weight of K7 (the adjoint character has another eigenvalue), so it passes K7 in kind. It holds for U(1) with 4 in place of 3, so it is not selective between U(1) and SU(2).

Stop of step 3. Next: step 4, the ranking, written short.
