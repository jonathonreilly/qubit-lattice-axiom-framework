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

### Step 4. The ranking. [ARGUED throughout; the numbers in the last column are my judgement, not measurements]

4.0 Four tests I apply to every attack, beyond the brief's fact tests. Each comes from steps 2 and 3.
- BOTH: does the next statement carry both halves of the seed? A flux-only result needs GLUE, and GLUE has no tool (row 895). A glue-only result needs the flux half.
- SLACK: how sharp must the proved inequality be? "Unlimited" means any finite constant serves.
- KIND: is the missing statement structural (a proof may use symmetry, positivity, the Lie algebra) or quantitative in the weight (K7 and Proposition V forbid a structural proof)?
- LINE: does success reach (SEED-FP), or a bare-window lattice theorem only? By 2.5(ii) and 3c.3(iv) every one-coupling result is a lattice theorem. I count that as real value (no such theorem exists above strong coupling), and I say which is which.
One more search fact governs the last column: fresh framing has returned the inventory three times in this note (3d.2) and once in row 878. So "chance in a few lane-hours" is the chance that the attack's OPEN statement falls to work on the present inputs.

4.1 The table.

| # | Attack and its next statement | BOTH | SLACK | KIND | LINE | Fact tests | Cheaper model? | Chance of a checked order-one step in a few lane-hours |
|---|---|---|---|---|---|---|---|---|
| 1 | Coupling transport of the full thermal trace: (LEV_K)/(VIR-log), equivalently (T-avg) (rows 669, 708, 710; THERM-DI-beta of row 905 in its full-trace form) | yes | unlimited (any K; K of order log b is enough) | one order-one inequality; must use the Wilson weight (fails at any transition, so at K7's line) | lattice gap at every beta in the interval; not the continuum (3c.3(iv)) | pass by construction: fails for U(1), Z_2, Q_8, 2T at their transitions; no worst-case block or layer bound is asked | no; needs invention | under 1 in 100. Three Fable or astra passes found no handle (rows 669, 708, 710, 905). |
| 2 | EXIT / (PATH) with PIN-MIX: exact block steps from first passage into the zone O (rows 846, 861) | yes | zone radii are explicit (0.05 to 0.14) | quantitative; no small parameter in the crossover | the only attack on (SEED-FP) itself | passes only if the block step is not exterior-uniform; no candidate | no | under 1 in 1000. No object: the account gives no block law. |
| 3 | EXC / (DRESS): an order-L_i lower bound on the boosted magnetic-cut response (rows 872-890) | flux only | thin: theta below 1 against a margin gamma of about 0.010; R''(0) is about -20 gamma L_i (check 890) | structural, SU(2)-specific through the spin-5/2 filter (check 864) | lattice (E17) at one coupling | passes U(1), Q_8, 2T by the filter; the electric start is group-blind (check 881) | partly: astra max wrote rows 871, 875 | under 1 in 200, and then GLUE is still missing |
| 4 | (VAR-SLAB): flux half from the Langevin gap lambda and (FR) (row 899) | flux only; lambda is glue-type | (FR) needs eps about 9e-5 lambda^(1/2) | lambda quantitative; (FR) is the flux energy again (row 899, 7.4) | lattice, one coupling | passes; no supremum over slices | no | under 1 in 500. Two open inputs, one behind W2. |
| 5 | Decoder: (SEED-DEC-U) with (S1), and (S2) (rows 887, 892) | flux only | density 1/9 needed against GUIDE 0.33 | (S1) structural; (S2) group-blind combinatorics | lattice | selective by contraposition (check 891) | (S2) and RIG: yes, astra or Opus | under 1 in 500 |
| 6 | (KURT) floor 1.66 (rows 886, 894) | flux only, and needs GLUE at the Corollary K' level | floor 1.66 against one-tube GUIDE 1.53 | no mechanism for SU(2) (symmetry theorems need a circle of symmetries) | lattice | passes Q_8 (4), fails to separate SU(2) from 2T, 2O in 2D (all 2) | the small-box decision: yes, Opus | under 1 in 500 |
| 7 | (GLUE-FP): (Z0) with (COUNT) (row 895) | glue only | unlimited in the gap size (the box is free) | quantitative (K7); "no tool is named" | lattice | the frozen-group PASS verdict failed (check 896) | no | under 1 in 1000 |
| 8 | Free-wall engine: (JOIN-TH_kappa) on cold boxes (rows 898-911) | glue only by design (no flux on free walls); plus a seed on one cold box; plus the OPEN limit-state node | kappa any absolute constant | "a new input at every scale that the seed does not imply" (row 910): it trades the structural half for a quantitative statement at every scale | lattice, dyadic cubes; limit node OPEN | U(1) fails through the seed; the periodic Q_8/2T test does not apply | no | under 1 in 500 per scale, and every scale is needed |
| 9 | THERM-DI-pin (check 908) | yes | unlimited in K | quantitative near the Higgs end point | lattice, and only below the first-order Higgs line (RECALLED: near beta 2.73) | passes | no | under 1 in 500 |
| 10 | (BOOT_eps): a positivity certificate over the Wilson loop equations (row 708, C-E) | yes | eps about 3e-10 at a = 10 (row 899's arithmetic) | the only proof object that changes with the weight | lattice | passes all, K7 included | certificates: Codex with exact arithmetic could search; the owner's rule admits only hand-size certificates | under 1 in 1000 by hand |

4.2 What the table says.
(a) By what closing buys: 2 first (it is the finish line), then 1 (a gap at every coupling, both halves), then the rest. Attack 2 has no object to work on today, so its hours would be spent restating.
(b) By kind and slack: 1 stands alone. It is the one statement that is a single inequality of order one with unlimited slack and both halves. Its weakness is known and I repeat it: in every form found so far it is the conclusion in differential form (row 669), and its three failed proofs (pointwise, locality, convexity; row 708) are on record.
(c) Attacks 3 to 6 are flux-only. Even a proof leaves GLUE, which is quantitative and has no tool. I rank them below 1 for that reason alone. Among them 3 has the only proved SU(2)-specific inequality, and its margin is thin.
(d) Attack 8 removes the structural half and keeps the quantitative one at every scale. I rank it below 3.
(e) Order by expected value per Fable hour: 1, 3, 2, 9, 8, 4, 5, 6, 7, 10. The gaps between ranks are small against the common factor: none has a visible proof.

4.3 Three things the list misses. Each is for Opus or Codex, not for Fable.
- (ONE-K), ARGUED. (SEED-L) is an open condition on a pair of total masses. If the first-passage densities at consecutive cutoffs at one g satisfy, on T_ell and T_(L ell), log of the integral of rho_(K+1) minus log of the integral of rho_K = c_K vol + O(eps_K) with one constant c_K for both tori and the sum of eps_K finite, then (SEED-L) at one cutoff K_0 with margin gives (SEED-L) for every K at least K_0. Call the hypothesis (UNIV-K). It is a weak-coupling statement on the account's own objects, including large-field terms and vacuum factors, which row 904 found the account's universality leaves out. It would cut "uniformly over all first-passage data" down to one datum. It does not touch the crux.
- K7 as a standing fact test, with Proposition V of row 712 as its proved relative. Row 912 does not list it. It is what separates GLUE-type from flux-type statements (3b.3 P1).
- The bodies of the Lipschitz-transport papers. READ `library/gap-skeleton-max.md` L368: Shenfeld (arXiv:2205.01642) and Bauerschmidt, Bodineau and Dagallier (arXiv:2307.07619) were read as abstracts only; the criterion "is from memory". They are the one source of one-sided Hessian tools with slack that the lane has not read in the primary text. A luna reading row on their exact hypotheses is cheap.

Stop of step 4. Next: step 5, the choice.

### Step 5. The choice.

5.1 The target. Attack 1 of the table: transport of the full thermal trace along the Wilson coupling.

5.2 Its crux lemma, exactly. READ `library/gap-mid-max.md` L160-172 (row 708; its Theorem TR and Corollary TR1 are L118-158).
(VIR-log). For the Wilson SU(2) theory and each beta_1 > 0 there are beta_0 at most 1/25600 and an even b at least 256 such that, on the cube B = b^3, for every s in [beta_0, beta_1) and every real t on the characteristic curve t = t_0 E(s), t_0 = ceil(log_2 b), E(s) = exp(integral of K over [beta_0, s]):
   upper right derivative in s of G(t; B; s)  <=  - K(s) t (dG/dt)(t; B; s),
with K continuous, non-negative, and integral of K over [beta_0, beta_1] at most log(b/(2 ceil(log_2 b))).
Here G(t; B; s) = log Tr T_B(s)^t - t log lambda_0(B; s). At integer t the left side is 6 t |B| (abar_(inf,B) - abar_(t,B)), the shift of the mean plaquette action between infinite and finite time extent (Lemma 4.2 there). The right side is K t times the thermal mean of the energy.
Sufficient level form (Remark LEV there): (LEV_K), no ordered level of the box falls faster than at the logarithmic rate K. Consequence (Corollary TR1 there, PROVED GIVEN Theorem SH and the strong-coupling seed): S(b/2; b^3; beta_1) < 1/1650, a gap on every periodic cube at beta_1, at least 0.12/b on cubes of side at least 32 b.
I restate what kind of statement it is. K need not be bounded in b. Any bound of the form K_b at most (log b)/(beta_1 - beta_0) minus a little serves. Nothing small has to be proved.

5.3 Why it beats the others. ARGUED; from 4.2.
- It is the one attack whose next statement carries both halves, has unlimited slack, and holds on a whole interval of couplings. A proof with a terrible constant is a proof.
- Its fact tests are automatic. By Theorem TR read backwards, (VIR-log) fails on any interval that crosses a transition: U(1) near 1.01, Z_2, Q_8 and 2T at their freezing points, K7's line. A proof must therefore contain a step that uses the Wilson weight. No worst-case block or layer bound is asked for, so the caps 2/3, 0.775 and 1.0109 do not apply to the statement.
- Flux-only attacks (3 to 6) leave GLUE, and GLUE is the same kind of statement as (VIR-log) with less to offer. The free-wall engine (8) asks a quantitative input at every scale.
- EXIT (2) buys more and has no object.
- What it does NOT buy: the continuum gap. It gives the lattice gap at each coupling of the interval, with a box of side exp(integral of K). (SEED-FP) still needs the hand-off or a nearly exact rate at weak coupling (3c.3(iv)). I rank it first knowing this, because a gap for Wilson SU(2) through the band would be the first order-one theorem of the lane and would fix what the hand-off has to land on.

5.4 What is already known to fail, so that the next lane-hours do not repeat it. READ `library/gap-mid-max.md` L160-185, `library/gap-skeleton-max.md` L246-255, FINISH.md L787.
- A pointwise operator inequality for the electric and magnetic parts of a level: false at the published rates (K about 3.3 against 1/s about 0.4, GUIDE).
- Locality theorems with a gap-dependent constant C m^(-p): the bound ends at a finite coupling.
- Convexity in the coupling: bounds the wrong derivative; Ising is in the class.
- The pointwise Hessian bound (T) for the product transport: false in a solvable chain. For the gradient transport: undecided.
- Strong coupling (Theorem B of row 710): holds only for s at most 1/(10 b^3). The term that breaks is the vacuum subtraction.
- Row 708's verdict on a hand proof: it "needs an identity that produces the ratio"; the lattice has no dilation; the substitute is one block step at order one with relative errors of order one in every level.

5.5 Stop condition. Two lane-hours, or earlier at any of these.
(S-a) A box-uniform counterexample: a model in the lane's class WITH the Wilson one-plaquette weight structure used by the proof attempt (for example the exact loop equation of step 6) and with K_b growing faster than log b on an interval with no transition. Then the attempted mechanism is group-blind and stops.
(S-b) The attempt reduces again to (T-avg) or to (DEF_K) with no new term. Then it is the conclusion in differential form (row 669) and stops.
(S-c) Any step that needs a supremum over configurations of a non-local quantity (the Hessian of a corrector, a conditional covariance of a slice). That is SA2 again; stop and record the extremal configuration.
Continue only if one of these appears: an exact identity that expresses the action deficit of a level through its energy with a remainder of one sign; or a box-uniform bound on K on any interval that leaves the range of Theorem B of row 710.

5.6 Work around it for Opus and Codex.
- Codex astra xhigh: check step 6 of this note line by line (identities F1 to F4 and the anisotropic comparison). Recompute every constant.
- Codex luna (reading): the bodies of Shenfeld arXiv:2205.01642 and Bauerschmidt-Bodineau-Dagallier arXiv:2307.07619, and Luscher's trivializing-map paper; the question is the exact hypothesis of the multiscale criterion and whether it tolerates a one-sided bound that is integrable over scales. Also Araki, Lett. Math. Phys. 19 (1990), for the log-majorization used in 6.4 (I RECALL it; it must be read or rebuilt before it carries a step).
- Opus 5.5 high: rebuild Araki's inequality in the repo from Lowner-Heinz (it is short), so that 6.4 does not rest on a citation.
- Codex (GUIDE, one numeric worker): on 2^3 x t and 3^3 x t boxes with an exact-kernel or validated heat-bath sampler, measure the two sides of (VIR_K) through F4 of step 6 (plaquette shift against force-overlap shift) for beta from 0.3 to 2.6. This tests the identity and gives K_b on tiny boxes. It proves nothing.
- Opus 5.5 max: the two ARGUED links (c) and (e) of the chain from (SEED-FP) to (GAP), and the statement (ONE-K) of 4.3 with its account-side hypothesis (UNIV-K). These are on the critical path and need no invention.
- Not for any model now: a fifth fresh-framing pass on the inventory.

Stop of step 5. Next: step 6, the first step.

### Step 6. First step on (VIR-log): what is exact about the rate, and the exact place where it stops.

Setting. A periodic box B with periods at least 3. X = SU(2)^(spatial links of B), SU(2) the unit quaternions in R^4, <a, c> = Re(a conj(c)). W = sum over spatial plaquettes of (1 - x_p) >= 0. M_b = multiplication by exp(-b W), so 0 < M_b <= 1 and M_(theta b) = M_b^theta. K_b = convolution on every link by exp(b (x - 1)), restricted to gauge-invariant functions. With two couplings, T(b_t, b_s) = M_(b_s)^(1/2) K_(b_t) M_(b_s)^(1/2). The lane's transfer operator (READ `library/gap-wall-assume-max.md` L301: kernel e^(-(V(u)+V(v))/2) I(u, v)) is a positive scalar multiple of T(s, s). The centre flips commute with M and K, so every statement below holds in each electric-flux sector.

6.1 Lemma F (loop equation for the plaquette, in force form). PROVED.
(F1) On M = SU(2)^E with the product of unit round metrics, Delta x_p = -12 x_p.
(F2) For plaquettes p, q through a link e: <grad_e x_p, grad_e x_q> = x_(p v q) - x_p x_q, where x_(p v q) is the normalized trace of the six-link loop "p and q with e removed" (x_(p v p) = 1).
(F3) Let omega be any state with omega(Delta_e f) = b omega(<grad_e A_eps, grad_e f>) for smooth f and the four links e of p, where A_eps = sum over q of (1 - eps_q x_q), eps_q = +1 or -1. This holds for the Gibbs measure of weight exp(-b A_eps) on every torus, twisted or not, and for limits of such. Then
   12 omega(x_p) = b omega(Phi_p),  Phi_p = sum over e in p, q through e, of eps_q (x_(p v q) - x_p x_q).
(F4) So for two such states at the same b: omega(x_p) - omega'(x_p) = (b/12) (omega(Phi_p) - omega'(Phi_p)). Summed over p with eps = 1: sum of Phi_p = |grad A|^2. Hence the left side of (VIR_K) at integer t (Lemma 4.2 of row 708) is (s/12) times the shift of the mean squared force between the time-t torus and the infinite cylinder; the derivative of the twist ratio ((T1) of row 899) is (s/12) times the shift of the mean squared force between the twisted and the untwisted torus.
Proof. (F1) For e in p and the other three links fixed, x_p = <q_e, w> with w a unit quaternion (the staple). A linear function on R^4 restricted to the unit 3-sphere is a spherical harmonic of degree 1, with eigenvalue -3. The four links of p are distinct (periods at least 3), other links contribute 0. (F2) The gradient of q -> <q, w> on the sphere is w - <q, w> q. So the product is <w, w'> - <q, w><q, w'>, and <w, w'> is the normalized trace of staple times inverse staple. (F3) Apply the hypothesis to f = x_p, sum over e in p, use (F1), grad_e A_eps = - sum of eps_q grad_e x_q, and (F2). (F4) Subtract. QED
Checks by hand. Small b: omega(x_p) = b/4 + O(b^2) for one plaquette (I_2/I_1), and (b/12) Haar(Phi_p) = (b/12) 4 (1 - 1/4) = b/4. Large b in 4D: 12 (1 - 3/(4b)) on the left; on the right the diagonal term gives 4 b 2 (3/(4b)) = 6, so the twenty cross terms give the other 6.
Remarks. (i) This is the first Schwinger-Dyson equation of the Wilson weight; it is not new (the bootstrap papers start from it; the lane's (BOOT_eps) names the family). What I add is its use: it answers row 708's sentence "I found no inequality that uses this" with the one exact consequence of log-linearity, Delta A = 12 (N_p - A). (ii) K7. For the mixed weight exp(b_F x + b_A (4 x^2 - 1)/3) the adjoint term is a harmonic polynomial of degree 2 in each link (Delta_(R^4)(4 <q,w>^2 - |q|^2) = 8 - 8 = 0), with eigenvalue -8 per link, -32 per plaquette. So the action is no longer an eigenfunction plus a constant, and the scalar identity (F3) is replaced by a system with a second observable. The identity changes with the weight, as K7 demands. (iii) It holds for U(1) with 4 in place of 12. It is not selective between U(1) and SU(2).

6.2 Lemma KF (the level condition can be weakened to its Ky Fan form). PROVED.
Let D_i(s) = E_i(s) - E_0(s), i >= 1, be the ordered excitation energies of the box. If for some theta' in (0, 1] and all m >= 1
   D_1(s') + ... + D_m(s') >= theta' (D_1(s) + ... + D_m(s)),          (KF-LEV)
then S(t; B; s') <= S(theta' t; B; s) for every t > 0. So Theorem TR's conclusion follows from (KF-LEV) with theta' = exp(-integral of K), in place of (LEV_K) for each level.
Proof. Put x_i = D_i(s'), y_i = theta' D_i(s), phi(u) = e^(-t u), c_i = -phi'(x_i) >= 0. The x_i are non-decreasing and phi is convex, so the c_i are non-increasing. Convexity gives phi(y_i) - phi(x_i) >= c_i (x_i - y_i). Abel summation: the sum over i <= N of c_i (x_i - y_i) equals the sum over m <= N of (c_m - c_(m+1)) S_m with c_(N+1) = 0 and S_m = sum over i <= m of (x_i - y_i) >= 0. So the sum of phi(x_i) is at most the sum of phi(y_i). Let N grow. QED
Why it matters: Ky Fan sums are variational (the product of the top k eigenvalues is the supremum of det(P T P) over k-dimensional subspaces), single ordered levels are not.

6.3 Theorem ABS (absolute levels obey the electric rate, at every coupling, in every box and sector). PROVED GIVEN the Lowner-Heinz theorem (t -> t^theta is operator monotone for 0 <= theta <= 1; RECALLED, classical, to be rebuilt) and the monotonicity of Bessel ratios (RECALLED; the lane has checked Bessel lemmas in rows 843 and 854, which I did not re-read).
Notation. On one link, K_b acts on the spin-j sector as e^(-b) 2 I_(2j+1)(b)/b. Put eps_n(b) = log(I_1(b)/I_n(b)) >= 0 for n = 2j+1, and K^_b = K_b divided by its spin-0 value on every link, so 0 < K^_b <= 1 and K^_b = exp(-sum over links of eps_(n_l)(b)). Put T^(b_t, b_s) = M_(b_s)^(1/2) K^_(b_t) M_(b_s)^(1/2) <= 1, with eigenvalues lam_0 >= lam_1 >= ... in a sector, E^_i = -log lam_i >= 0, and the Ky Fan sums EE_k = E^_0 + ... + E^_(k-1). For b < b' put theta(b, b') = inf over n >= 2 of eps_n(b')/eps_n(b), in [0, 1].
(AN) For b_t < b_t', every b_s >= 0, theta = theta(b_t, b_t'), and every k >= 1: EE_k(b_t', theta b_s) >= theta EE_k(b_t, b_s).
(ABS) For s < s' and theta = theta(s, s'), on the isotropic line: EE_k(s') >= theta EE_k(s) for every k >= 1.
Proof. (1) eps_n(b') >= theta eps_n(b) for all n, so K^_(b_t') <= K^_(b_t)^theta (commuting spectral calculus). (2) Conjugate by M_(b_s)^(theta/2) = M_(theta b_s)^(1/2): T^(b_t', theta b_s) <= M^(theta/2) K^^theta M^(theta/2), with M = M_(b_s), K^ = K^_(b_t). For compact 0 <= Y_1 <= Y_2 the ordered eigenvalues satisfy lam_i(Y_1) <= lam_i(Y_2). (3) Araki's log-majorization: for positive A, B and 0 < theta <= 1, the product of the top k eigenvalues of B^(theta/2) A^theta B^(theta/2) is at most the theta-th power of that of B^(1/2) A B^(1/2). For k = 1 this is the Cordes inequality ||X^theta Y^theta|| <= ||X Y||^theta with X = A^(1/2), Y = B^(1/2): scale to ||X Y|| = 1; then Y X^2 Y <= 1, so X^2 <= Y^(-2), so X^(2 theta) <= Y^(-2 theta) by Lowner-Heinz, so Y^theta X^(2 theta) Y^theta <= 1 (non-invertible Y by approximation). For k > 1 apply the case k = 1 to the k-th antisymmetric tensor powers, which respect products and powers and whose norm is the product of the top k singular values. (4) Combine (2) and (3): (AN). (5) M_b decreases in b, so T^ decreases in b_s and every E^_i increases in b_s; since theta s <= s', (ABS) follows from (AN) at (b_t, b_s) = (s, s). QED
GUIDE (a run that guides only; one-plaquette model on class functions, 60 characters; script `guide/araki_guide.py` next to this file, a few seconds). (AN) held in six test cases with margin between 5e-3 and 0.23 for k up to 6. On the isotropic line of that toy the first gap falls at the rate K_1 = 0.19 at s = 2.3 against the electric rate 0.41, and rises again above s near 4. The toy has no running; it only confirms the direction of the inequality.
Content. (ABS) is (LEV_K) for the Ky Fan sums of ABSOLUTE energies, with the electric rate K_el(s) = sup over n >= 2 of (-d log eps_n/ds), at every coupling, for every compact group with its own eps (the proof is group-blind). It is the exact Wilson-operator form of the continuous-time fact 0 <= x de/dx <= e of 3c.3(ii).

6.4 The exact obstruction. PROVED (algebra).
Put Dfc_k(s, s') = EE_k(s') - theta(s, s') EE_k(s) >= 0, the defect of (ABS). For the excitation energies D_i = E^_i - E^_0 and any theta' <= theta:
   sum over i = 1..k-1 of [D_i(s') - theta' D_i(s)] = Dfc_k - k Dfc_1 + (theta - theta') sum over i = 1..k-1 of D_i(s).
So (KF-LEV) with theta' holds if and only if
   (SUPER-D)   k Dfc_1(s, s') - Dfc_k(s, s') <= (theta - theta') (D_1(s) + ... + D_(k-1)(s))   for all k >= 2.
In words: the vacuum's defect, counted k times, may exceed the defect of the lowest k levels by at most a multiple of their excitation energy. The defect has three non-negative sources, read off the proof of 6.3: the spread of the Bessel ratios over the spins (step 1), the non-commutativity of M and K^ (step 3), and the magnetic step from theta s to s' (step 5), which contributes (s' - theta s) times the magnetic action of each level. The third source is the magnetic deficit of row 708's Way 1: for an excited level it is below the vacuum's by about 3 times the energy (GUIDE, published rates). So (SUPER-D) is not a small correction to (ABS). It is the statement that this deficit is at most K times the energy.

6.5 Where the first step stops.
- PROVED here: Lemma F, Lemma KF, Theorem ABS given two classical inputs, the identity of 6.4. None is at order one in the sense of the crux; all hold at every coupling.
- The step from absolute energies to excitation energies is (SUPER-D). 6.4 shows that it is (DEF_K) of row 708 again, now exact for the Wilson operator and in Ky Fan form. No new term has appeared. By stop rule (S-b) of 5.5 this line of attack stops here.
- What a continuation would need, stated so that it can be tested: an exact identity or inequality in which the magnetic action of a level MINUS that of the vacuum appears with a remainder of one sign. (F3) gives such a difference as a difference of force overlaps (F4), which is an identity between two differences, not a bound on either. The Ky Fan variational form gives upper bounds on EE_k, hence on Dfc_k from above, which is the wrong side for the vacuum term k Dfc_1.
- So the first step ends at the known wall, in exact form. It adds no handle. I record this as the outcome, not as progress on the crux.

### Step 7. Hand check of step 6, and the fact tests on it. [mine; a re-derivation by the author is not an independent check]

7.1 Re-derived line by line.
- (F1): eigenvalue of a degree-1 harmonic on the unit S^3 is -k(k+2) = -3; four links; -12. Holds.
- (F2): <w - <q,w>q, w' - <q,w'>q> = <w,w'> - <q,w><q,w'>, using |q| = 1. Holds. A link traversed backwards gives Re(a conj(q_e) c) = <q_e, c a>, again linear with a unit covector.
- (F3): signs. L f = Delta f - b <grad A_eps, grad f>, grad_e A_eps = - sum of eps_q grad_e x_q, so L x_p = -12 x_p + b Phi_p and the mean of L x_p is 0. Holds. Small-b check with a twist sign: eps_p b/4 on both sides.
- (F4): sum over p of Phi_p (eps = 1) = sum over e of |sum over q through e of grad_e x_q|^2 = |grad A|^2. Holds.
- Lemma KF: Abel identity checked term by term; the last term uses c_(N+1) = 0 and c_N >= 0. The x_i must be the ordered levels at s'; the y_i need no order. Holds.
- Theorem ABS, the single-link eigenvalue: the Haar integral of e^(b cos th) chi_j is I_(2j)(b) - I_(2j+2)(b) = (2(2j+1)/b) I_(2j+1)(b). Divided by 2j+1 it is 2 I_(2j+1)(b)/b. Holds. K commutes with gauge transformations because the link kernel is a class function. Holds.
- CORRECTION to the wording of 6.3 step (5) and of "T^ decreases in b_s". M^(1/2) K^ M^(1/2) is not monotone in M in operator order. Its non-zero spectrum equals that of K^^(1/2) M K^^(1/2), which is monotone in M. So the ordered eigenvalues decrease in b_s. The conclusion (ABS) is unchanged. In the same way, step (2) conjugates the inequality K^_(b_t') <= K^_(b_t)^theta, which is legitimate as written.
- Araki step: the theta <= 1 form follows from the r >= 1 form by A -> A^theta, B -> B^theta, r = 1/theta, and a theta-th power. The Cordes step is three lines given Lowner-Heinz. Compactness: K^ is compact on gauge-invariant functions (finite multiplicities of spin networks), so the products are compact and the antisymmetric powers are legitimate. theta <= 1 uses that I_n/I_1 increases in b (RECALLED). If that monotonicity failed for some n the theorem would need theta replaced by min(1, theta); the GUIDE values are 0.19 to 0.89.
- 6.4: sum over i = 1..k-1 of D_i = EE_k - k EE_1. The identity follows by adding and subtracting theta EE. Holds.

7.2 Fact tests.
- U(1) Coulomb: (F3) holds with 4 for 12; Theorem ABS holds (the proof is group-blind). Neither gives a gap, and neither should: both concern absolute energies. The selective statement is (SUPER-D), which fails wherever levels collapse.
- Q_8 and 2T: Theorem ABS holds with their own kinetic eigenvalues (positive; for Q_8 they are (cosh b - 1)/4 on the sign characters and (sinh b)/4 on the doublet, by direct sum over the eight elements, before normalization). So nothing proved in step 6 distinguishes SU(2) from Q_8 or 2T. (F1) to (F4) have no meaning for finite groups (no Laplacian), which is the only place where step 6 uses the Lie group.
- K7: (F3) changes form for the mixed weight (6.1 remark ii). Theorem ABS does not: it holds for any positive-definite class weight with monotone ratios.
- Worst-case caps: no step uses a single-site, vertex-block or layer bound. Every inequality is an operator inequality valid at all couplings.
- Order one: nothing in step 6 reaches it. The step reduces nothing to a statement a known tool reaches. It locates the crux lemma of the chosen target exactly ((SUPER-D)) and shows that it is the known one.

7.3 What a checker should attack first. The direction of the log-majorization in 6.3 (3) (it is RECALLED and it carries (AN)); the claim that the kinetic operator of the lane's transfer operator is the link-wise convolution on gauge-invariant functions with the eigenvalues stated; the Bessel monotonicity; the convergence in Lemma KF.

### Step 8. Close.

8.1 PROVED in this note (by hand, by the author; not checked by another model).
- Lemma F (6.1): Delta x_p = -12 x_p; the force form 12 omega(x_p) = b omega(Phi_p) of the plaquette loop equation in every Gibbs state, twisted or not; hence every plaquette shift between two such states is (b/12) times a force-overlap shift.
- Lemma KF (6.2): the level condition of Theorem TR can be weakened to Ky Fan sums of excitation energies.
- Theorem ABS (6.3), GIVEN Lowner-Heinz and the monotonicity of Bessel ratios (both RECALLED): the Ky Fan sums of absolute energies of the Wilson transfer operator fall no faster than at the electric rate, at every coupling, in every box and flux sector; and its anisotropic form (AN).
- The identity of 6.4: (KF-LEV) is equivalent to (SUPER-D).
- The identity of 3d.3 (the transport corrector is A/12 minus (b/12) times the corrector of the squared force, in the unit round metric; the constants 3 written in 3d.3 belong to the metric of radius 2).

8.2 ARGUED, not proved.
- The ranking of step 4 and its three structural points (3b.3): GLUE-type statements are quantitative, flux-type can be structural; one-coupling results are lattice theorems; the tolerance point rests on RECALLED transition values.
- (ONE-K) of 4.3.
- The reading that every one of my fresh framings was already in the lane (3c.1, 3d.2).

8.3 GUIDE. The one-plaquette run of 6.3. It checks the direction of (AN) and nothing else.

8.4 OPEN.
- (VIR-log), in any of its forms: (LEV_K), (KF-LEV), (SUPER-D), (T-avg). Nothing in this note moves it at order one.
- An exact relation that bounds the magnetic action of a level minus that of the vacuum by its energy, with a remainder of one sign. This is the single missing object of the chosen target.
- Every order-one number of the lane, unchanged: (CORE), GLUE, (SEED-FP), EXIT.

8.5 Advice on the spend, from the outcome of the first step. ARGUED.
The chosen target is the best-shaped of the live attacks, and its first step ended at the known wall with no new term. So its stop rule (S-b) has already fired once. I advise: at most one more Fable lane-hour on it now, on the one question of 8.4; then hold Fable on the crux until one of the cheap rows of 5.6 returns a new input (the primary texts on Lipschitz transport along a flow, the GUIDE measurement of K_b and of the defects Dfc_k on small boxes, the check of step 6). No other live attack ranks above it, and the same holds for them: none has a visible proof on present inputs. The certain critical-path work (links (c) and (e), (ONE-K) with (UNIV-K)) needs no Fable.

RESULT: chosen target = transport of the full thermal trace along the Wilson coupling (attack 1 of step 4; it alone carries both halves with unlimited slack and automatic fact tests, but it gives a lattice gap, not (SEED-FP)); crux lemma = (VIR-log) of row 708, equivalently (SUPER-D) of 6.4: the vacuum's anisotropy defect counted k times exceeds that of the lowest k levels by at most K times their excitation energy, with the integral of K at most log(b/(2 ceil(log_2 b))); first step outcome = PROVED Lemma F (force form of the plaquette loop equation), Lemma KF (Ky Fan weakening of the level condition) and, given Lowner-Heinz and Bessel monotonicity, Theorem ABS (absolute levels obey the electric rate at every coupling), and it STOPS at the vacuum subtraction, which is row 708's (DEF_K) again in exact form: no handle at order one, nothing on the crux proved.
