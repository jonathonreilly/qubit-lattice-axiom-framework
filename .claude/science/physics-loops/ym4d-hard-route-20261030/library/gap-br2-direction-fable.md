lead: Claude Opus 5.5 (lead session), dispatched 2026-11-17
row: 1108

Written by Claude Fable 5.2, effort high, laptop subagent. Direction row. No mass gap is claimed.

Marks used: argued, guide, reading, open.

## Plan (six steps; one step per response; each result is appended below)

1. Read `parts/gap.md` in full, and the statements of (W), C_beta, PHYS-SEED, T_JW-lat where `parts/gap.md` and `library/open-registry.md` point. Record the exact statements.
2. Read the bridge sources: `gap-bridge-exercise-opus.md` section 7 and its checks' RESULT lines; `gap-descent-mc-astra.md`. Record what (MON-L) is and what the failed control is.
3. Read the face-leg sources: `gap-face-exercise-fable.md` step 9; the two checks (S10, S12); `gap-pinu-ev.md` and its check; `prior/gap-face-alt-read-luna.md`. Record the reduced face statement.
4. Task (1): cost of each open input ((MON-L), face leg, (W) direct): first lemma, nearest false model, evidence for and against.
5. Task (2): does BR-2, fully proved, give (W) or T_JW-lat, for which beta, and the exact missing step.
6. Tasks (3) and (4): two recommended proof rows (statement, model tier, stop rule, what each changes); the row not to run; RESULT line.

Status: all six steps done 2026-11-17. RESULT line at the end.

## Step 1 result: the statements (reading; every line cites its source)

Read in full: `parts/gap.md` (278 lines, at commit 40ebd1721). Read at the lines named: `library/gap-crux-exercise3-max.md` L111-160; `library/gap-phys-seed.md` L303-318; `library/gap-wall-assumptions-opus.md` L478-490; `library/gap-aniso-check-astra.md` L178-188; `library/gap-ladder-max.md` L85-101, L242-243, L283; `library/gap-bridge-exercise-opus.md` 2.2. `library/open-registry.md` has no row for (W), C_beta, PHYS-SEED or T_JW-lat (grep, 0 hits for the four names in gap context). So the statements below come from the files that `parts/gap.md` points to.

**S1. (W), the wall** (`parts/gap.md` L18-23; repaired form of `gap-zd-astra.md` item 18). Wilson SU(2), periodic tori, along the account's trajectory (a_j, beta_j) with first-passage data. D^+(L) is the upper limit over j of the Casimir free energy D_j(L/a_j). z^-(L) is the lower limit over j of (L/a_j) m_j((L/a_j)^3), the gap of the periodic cube times its side. (W): there are a bound (L_0, D_0) of (BDD-Delta) and a physical size L in P, L at least 4 L_0, with z^-(L) > 256 D_0 + 30. Two properties matter for this row. (a) (W) is uniform in the cutoff j at one physical size. (b) (W) is a torus statement with all flux sectors (`gap-crux-exercise3-max.md` L138-151: a zero-flux-sector statement does not count "unless the flux part of (Z-UNB) is supplied too").

**S2. (PHYS-SEED) and its equivalents** (`gap-phys-seed.md` L311-318, Theorem ZD-c; cross-provider checked, HOLDS conditionally). (PHYS-SEED) iff (BDD-Delta) and (Z-UNB) iff (Z-SEED). (W) iff (PHYS-SEED).

**S3. The fixed-coupling form** (`parts/gap.md` L24-26). Sufficient for (W): the seed (SEED) at each beta of the window 2.3 to 2.6, with a carry to finer cutoffs. The carry is open: row 978's RESULT (`gap-ladder-max.md` L283) says no carrier was found; the carry is (NOCRIT) of row 709 plus a climb at the asymptotic-freedom rate; it is false for compact U(1), for frozen groups and on K7 lines; and "beta 2.3 is not a lattice of the account's family". This is set-aside method 23 of `parts/gap.md` L62.

**S4. C_beta** (`gap-aniso-check-astra.md` L178; `gap-bridge-exercise-opus.md` L321). Every isotropic infinite-volume limit state of W(beta, beta, beta) clusters exponentially on the allowed gauge-invariant local observables. It is a statement at one lattice coupling, hence at one cutoff. Check 1070 (L180-184): C_beta does not contain T_JW-lat, which needs a common physical rate at all fine cutoffs; and C_beta does not control the finite-torus flux sectors, so it does not give (SEED).

**S5. T_win** (`gap-bridge-exercise-opus.md` 2.2). C_beta for every beta in [2.3, 2.6]. This is the conclusion that the bridge routes aim at.

**S6. T_JW-lat** (`gap-wall-assumptions-opus.md` L485). There are c > 0 and a physical length l such that, for all large j, every infinite-volume limit state of the cutoff-j theory clusters at rate c/l in physical units, on a total set of local observables. With T0's (H2) and (TOT) it gives the Jaffe-Witten gap (argued there; corrected by check 1054: only limit states of admissible periodic cubic tori). Relation to (W) (`parts/gap.md` L151): (W) implies the flux bound (Lemma FLUX-W, one way). "T_JW-lat is weaker than (W) by exactly the flux clause" FAILS as an equivalence (check 1055). The frozen-group tests do not bind T_JW-lat. No finite-size criterion for T_JW-lat is on record.

**S7. BR-2** (`gap-bridge-exercise-opus.md` 7.3, L406-420; checks 1074, 1075). Model W(beta_L, beta_M, beta_T) on Z^2 x Z^2. Step (i): (FACE-SG), clustering at the face point (infinity, beta, beta), reached from the anchor (infinity, beta, 0) along beta_T. Step (ii): (MON-L) in rate form, m(beta_L, beta, beta) >= m(infinity, beta, beta) for beta_L in [beta, infinity). Steps (i) and (ii) give C_beta. The covariance form of (ii) is false (Lemma MON-L-cov FALSE, HOLDS in both checks). Check 1075's verdict: BR-2 is stronger than the target C_beta, wounded at the face step and blocked at (MON-L). Check 1074: the class refutation of (MON-L) FAILS as written; it stays at guide grade.

**S8. What the record already says on the three open inputs** (`parts/gap.md` L156-169).
- (MON-L): false for frozen Q_8 on a small box (Example KIN-7, proved in a limit). False at guide grade for SU(2) on the one-transverse-plaquette box at beta_M at least 8.5 with beta_T at most 0.15 (row 1085). Positive at the window couplings on those boxes (rows 1089, 1090; the heat-kernel sign turns negative at equal couplings near 3.4 to 4.0, and the crossing moves down as n grows: 3.972, 3.592, 3.471, 3.429, 3.416). The 4D Monte Carlo of row 1101 neither kills nor validates it; one matched control failed.
- Face leg: reduced by rows 1077, 1091, 1096, 1099 to sign-cluster decay in a field on tori (PIN-U or PIN-2, plus the torus form of T2; or UNS plus block-field control) together with EV.
- (W) direct: no route near closure (`parts/gap.md` L200); the missing object is a selective inequality at each scale between first passage and the seed size.

One point for step 5, noted now (argued; it uses two recalled asymptotic formulas, neither rebuilt here). At the anchor the sheet rate is about exp(-pi beta) (the lane's X(beta), `gap-bridge-exercise-opus.md` 2.2). The 4D physical rate in lattice units is about exp(-(3 pi^2/11) beta) for SU(2) with beta = 4/g^2 (one-loop coefficient b_0 = 11/(24 pi^2)). Since pi > 3 pi^2/11 = 2.69, the anchor rate is smaller than the 4D physical rate by a factor about exp(-0.45 beta). So a lower bound of the form "isotropic rate >= face rate" is consistent with asymptotic freedom, but it is not a rate that is uniform in physical units, if the face rate at beta_T = beta scales like the anchor rate. Step 5 uses this.

## Step 2 result: the descent (MON-L), what is on file (reading, with two argued remarks)

Read: `library/gap-bridge-exercise-opus.md` 7.1-7.5 (L370-450) in full; the RESULT lines of `gap-bridge-exercise-check-astra.md` (L440) and `gap-bridge-exercise-check-opus.md` (L703); `library/gap-descent-mc-astra.md` L18-50, L92-160, L203-422 (all but the repo search, the source checks and the resource record). Read at the lines named, because (MON-L) cites them: `gap-bridge-vectors-max.md` L181-186 (Lemma KIN, (FLUX-EXC)); `gap-descent-sign.md` L102-145 (Lemma SC, Proposition DIL, Remark CUM, the three failed ways of step (S)).

**D1. The exact statement.** (MON-L): m(beta_L, beta, beta) >= m(infinity, beta, beta) for beta_L in [beta, infinity), m the common clustering rate. Its operator form (Lemma KIN, proved, every compact group): the transfer operator in direction 0 is S* D(beta_L) S, S* S is the face operator, and D is diagonal in the colour charge across cuts. In the heat-kernel form D = e^(-tN). By the Hellmann-Feynman identity KIN-5, the gap is non-decreasing in t iff (FLUX-EXC): the first excited vector has flux number <N> at least that of the ground vector, n_1 >= n_0, at every t. So (FLUX-EXC) is the derivative form of (MON-L). It is stronger than (MON-L) as written (check 1074).

**D2. What is proved.** Proposition DIL (any group, any box): the gap does not decrease while the vacuum is dilute, n_0 <= 3/4. Corollary N2-SMALL: (FLUX-EXC) at n = 2 for beta_M at most 3/2. Lemma SC: the sign follows from a single crossing, r(1) <= 1. Nothing is proved at a window coupling.

**D3. What fails.** Step (S) failed in three written ways (`gap-descent-sign.md` L123-126). Way 1 (DIL) loses a volume factor: the bound uses an operator norm, and n_0 grows with the box. Way 2 (SC) needs r(1) <= 1, which the run shows false for beta_M >= 8. Counter-models: frozen Q_8 on a small box (KIN-7, proved in a limit); abstract operators S* e^(-tN) S (KIN-6); SU(2) itself on the one-transverse-plaquette box at beta_M >= 8.5, beta_T <= 0.15 (row 1085, guide). At equal couplings the heat-kernel sign turns negative at 3.972, 3.592, 3.471, 3.429, 3.416 for n = 2 to 6 (row 1090, guide).

**D4. The Monte Carlo of row 1101 (guide).** 8^4 and 12^4, beta = 2.3, 2.4, 2.5. No Delta is below zero by three errors. The control at beta = 2.5 on 16^4 misses Teper's scalar mass by 3.36 errors. The file's own verdict: "MON-L is neither killed nor validated".

**D5. Remark A (argued by me from the file's own numbers; not checked).** The Monte Carlo cannot test (MON-L) at these sizes, in either direction. Reason: the file's O(4) controls give sheet correlation lengths 18.96, 25.31, 33.23 at couplings 2.3, 2.4, 2.5. These are the anchor's lengths. The face boxes have sheets of side 8 and 12. So each face sheet is two to four times smaller than the anchor's correlation length. A rate measured on such a box is a finite-size level spacing, not a clustering rate. The file reports face minima 0.48 to 0.64; the anchor's singlet rate in infinite volume is at most about 2/xi, that is 0.06 to 0.11 (two spin masses; a recalled fact for the O(4) model, not rebuilt). Whether the face rate at beta_T = beta is near the anchor value or near 0.5 is not known: no run and no theorem on file decides it. The file itself says the face minima "cannot rule out an unseen slower sector", and that 8^2 and 12^2 are small (its comparator table, Horsley-Pendleton-Wack row).

**D6. Remark B (argued; consequence of A).** If the infinite-volume face rate in the window is of the anchor's order (0.05 to 0.1), then (MON-L) in the window holds with a factor of about ten to spare, because the isotropic rate is about 0.66 to 1.0 there (Lucini-Teper, Teper, as cited in the file). Then the sign is not where a proof dies. The content of (MON-L) is then this: "the isotropic 4D rate is at least a small positive number". That is C_beta itself with a number in it. So (MON-L) as a theorem carries the whole 4D difficulty; the face supplies only the number. This agrees with check 1075 (BR-2 "blocked at (MON-L)") and with row 1076's verdict that (FLUX-EXC) "renames" the monotone form.

**D7. Scope of the small-box counterexamples (argued).** The negative signs of rows 1085 and 1090 are on boxes with one transverse plaquette. There the two rates do not follow the infinite-volume laws. In infinite volume and at large beta the anchor rate (about exp(-pi beta)) is below the 4D rate (about exp(-2.69 beta)), see step 1. So the small-box signs say nothing about the infinite-volume (MON-L) at large beta; they refute the all-boxes form only, as check 1088 already says. But they do bind every proof that works box by box with constants uniform in the box: such a proof is refuted at guide grade above beta 3.4.

## Step 3 result: the face leg and the end-point exercise, what is on file (reading, with one argued remark)

Read in full: `library/gap-face-exercise-fable.md` step 9 (L1337-1554); `library/gap-face-exercise-check-astra.md` verdict table and the sections on C14 and on the F4-KP reduction (L56-76, L324-588); `library/gap-face-exercise-check-opus.md` S10 and S12 (L540-624, L686-755); `library/gap-pinu-ev-check-opus.md` step 8 verdict table and RESULT (L188-236); `library/prior/gap-face-alt-read-luna.md` (87 lines). `library/gap-pinu-ev.md`: outline of all statements, then L79-90, L148-152, L186-190, L204-228, L249-271 (the open list, the answers, the limits, the RESULT); the proofs of Lemmas CR, FREE, LS, DA, W, J, BF were not re-read line by line, because check 1100 holds each of them. Read at the lines named, because the face leg cites them: `library/gap-face-stability.md` L32, L38, L165, L195, L227, L330; `library/gap-wall-vectors-max.md` L128-132, L164-179, L304.

**F1. The face statement that BR-2 needs.** (FACE-SG): exponential clustering of the G-invariant local observables at (infinity, beta, beta_T) for every beta_T in [0, beta] (`gap-wall-vectors-max.md` L128). BR-2 uses it at beta_T = beta.

**F2. What the reduction of rows 1077, 1091, 1096, 1099 reaches.** The target of row 1091 is (17) on an interval 0 <= beta_T <= eps_beta (`gap-face-stability.md` L32). Given the sheet input, the proved interval is 0 <= beta_T <= min(h_0/2, 1/(12 X e^a S_a)) (L330). The file's own reading (L195, guide): eps is of order 1/X, of order Xi(beta)^(-2); "This matches the region beta_T Xi^2 <= eps of row 1066". Higher orders in beta_T give no positive radius by that method (L227).

**F3. The exact remaining input of that reduction** (check 1100, RESULT). Sign-cluster decay in a field on tori, through PIN-U (equivalent to PIN-2 up to scale) for the pins that Lemma LS does not cover, plus the torus form of T2; or through UNS plus control of the outer block fields; together with EV. All open. UNS is OPEN, not ARGUED (Ding, Huang and Yang's Theorem 5.2 covers xy boundary data only). Lemma DA rests on an unwritten extension of OpenAI's (3.61) to annuli pinned on both layers. Step failures on file: Lemma W (wall monotonicity fails on one site); Pei's pinning monotonicity fails in a field (P1, A1); the Ginibre step and the amplitude association fail for a sheet in a field (G1, G2). The swap-cluster replacement (Proposition SW) does not decay at the window (guide: swap clusters fill 95 to 98 percent of the torus).

**F4. Remark C (argued; the main reading of this step).** The face leg has two parts, and the files reduce only the first.
- Part (i-a): the face near the anchor, beta_T in [0, eps_beta], eps_beta of order Xi^(-2). With Xi between 19 and 33 lattice units at the window (the controls of row 1101), eps_beta is of order 10^(-3). This part is the sheet problem of F3.
- Part (i-b): the face from beta_T = eps_beta to beta_T = beta, a range of order one in the coupling. No reduction is on file. Row 1077 names it "the rest of (FACE-SG-T)". Row 1053 gives its nature (`gap-wall-vectors-max.md` L164, L304, argued there): the stiffness of a block of b^2 sheets is marginal for two transverse dimensions, and (FACE-SG) is "the wall, with the frame problem in transverse form". Row 1077's Ising example (16) shows that a gap alone does not give stability, so (i-a) does not continue by itself.
So a full proof of PIN-U and EV gives clustering on a strip of width about 10^(-3) next to the anchor. It does not give the face point (infinity, beta, beta). The sentence "the face leg is reduced to coupled 2D O(4) sheets" is true for part (i-a) only.

**F5. The end-point exercise (rows 1103, 1105, 1106).** Step 9: stiff end-points among plane-dependent Wilson couplings are sheet systems (one frozen plane, or two opposite frozen planes); this rests on C14. Check 1106: C14 FAILS as an unconditional classification (frozen triangle with small couplings is a stiff end-point; the variance step lacks a reference measure and a volume-uniform bound). Check 1105, S10: C14 HOLDS AFTER CORRECTION at window-size couplings, GIVEN the belief that the ordered 3D O(4) model has no gap for invariant observables. So the answer "no other stiff end-point at window couplings" is a belief-grade statement. The floppy corner F4 = (0, beta, 0): check 1106 and S12 agree that the reduction to (F4-KP) fails as written (integer-spin supports, link-overlap factor 16 or 8, winding polymers, marked observables); a corrected conditional statement exists in each check. Step 9.2 item 5 of the exercise: "The carry is untouched." From a floppy start the rate must be shown not to fall to zero on the way: that is (LIN-path) or (NOCRIT), stronger than the target (BR-3's verdict, `gap-bridge-exercise-opus.md` 7.4).

**F6. Literature (row 1104's reading, `prior/gap-face-alt-read-luna.md`).** No rigorous source proves a gapped anisotropic or layered face with a controlled bridge to isotropic couplings near 2.2. No proved monotonicity of a non-abelian mass gap in one plane coupling. The OpenAI O(4) preprint states c sqrt(beta) e^(-pi beta) <= m_lat(beta) <= C sqrt(beta) e^(-pi beta) for beta >= beta_0, a two-sided bound. So the anchor's exponent pi (step 1, last paragraph) is a posted, unrefereed theorem, not only a recalled formula. No theorem covers O(4) sheets coupled to one another or in fields of arbitrary direction.

## Step 4 result, task (1): what each open input costs

Each block has: the cost in plain words; the statement as a theorem; the first lemma a proof row would attack; the nearest model where that lemma is false; the evidence for and against. Marks are on each line. Read at the lines named for this step: `gap-bridge-vectors-max.md` L226-231, L377-381 (GH2, P4, (SING)); `gap-checkerboard-singlet-astra.md` headers, L402-426, L590-606, RESULT (what row 1084 tried).

### 4.1 (MON-L), the descent

**Plain words.** One plane direction is frozen. Loosen it until it is as strong as the other five. The rate at which far measurements forget each other must not go down on the way. (reading)

**As a theorem.** m(beta_L, beta, beta) >= m(infinity, beta, beta) for beta_L in [beta, infinity), in infinite volume, for each beta in [2.3, 2.6]. At beta_L = beta this reads: the isotropic rate is at least the face rate. Given a gapped face, that is C_beta with a number. So (MON-L) carries the whole four-dimensional difficulty (step 2, D6; check 1075: "blocked at (MON-L)"). (argued)

**What is perturbative.** Only beta_L >= X(beta)^2/eps, the region R_eps (`gap-bridge-exercise-opus.md` 2.2), and there the seed (S) is open too. With X between 19 and 33, that is beta_L above 10^3. The descent from there to beta_L = 2.4 has no small parameter. (reading; the size is a guide)

**What a proof must use** (reading, from the files of step 2). The group is continuous (KIN-7 kills frozen Q_8). The form of N and of the face vector, not the structure S* e^(-tN) S alone (KIN-6). Infinite volume or a typical-box statement: a bound uniform over boxes dies at guide grade above beta about 3.4 (row 1090), and Proposition DIL loses a volume factor. The whole state space (products with a massless factor).

**First lemma a proof row would attack.** The descent in its first exact case: the model GH2_2 of row 1076 (Lemma CB-L). It is a two-dimensional SU(2) lattice gauge field with coupling beta_L and two S^3 fields with coupling beta_M. Statement (GH2-DESC): for beta_M in the window and every beta_L in (0, infinity), the gauge-invariant local observables cluster at a rate a(beta_M) > 0 that does not depend on beta_L or on the box. Both ends are proved given OpenAI's Theorem 3.1: beta_L = infinity is two free O(4) sheets; beta_L = 0 is Lemma DEC of row 1084. The interior is open: the weights are twisted, so they leave the class where the posted proof uses association. This is the lane's (SING) (`gap-bridge-vectors-max.md` L377). Row 1084 tried the interior only by an association port and wrote one counterexample to that step (GH-NA). (reading)

**Nearest model where the lemma is false.** Compact U(1) in the same model: the relative phase of the two fields stays massless at large beta_M (Gaussian level, argued in row 1076 L379; Kosterlitz-Thouless belief). So (GH2-DESC) is selective: a proof must use the non-abelian group. For the monotone form of (MON-L): frozen Q_8 on a small box (KIN-7, proved in a limit); SU(2) on the one-transverse-plaquette box at beta_M >= 8.5 (row 1085, guide). (reading)

**Evidence for.**
- Window couplings, small boxes: every sign positive, smallest Delta = +0.0926 (row 1089, guide).
- Large beta, infinite volume: the anchor rate (exponent pi, posted two-sided bound) is below the 4D rate (exponent 3 pi^2/11 = 2.69, recalled). (argued, step 1)
- Slack: if the face rate in the window is of the anchor's order, the isotropic rate exceeds it about ten times (step 2, D6). (argued)
- A mechanism near the face at beta_T = 0 (argued by me; physics reasoning; no file states it; not a proof). At the anchor a single sheet particle is not G-invariant: the sheet on the transverse link (x, x+e) carries colour at x and at x+e. The lightest G-invariant states are pairs on one sheet, so the anchor's invariant rate is the two-particle threshold 2m. A finite beta_L gives each transverse site a two-dimensional gauge field. A two-dimensional gauge field confines colour by a linear potential. A linear potential lifts a pair above its threshold. So the rate rises as beta_L comes down from infinity. In (GH2-DESC) this is the statement that gauging does not lower the neutral rate.

**Evidence against.**
- No mechanism on file for the sign: row 1076, "A proof of the sign has no mechanism". Step (S) failed in three written ways (row 1081).
- At equal couplings the heat-kernel sign turns negative at 3.416 for n = 6, and the crossing came down with n (row 1090, guide). Its limit is open. If it reaches the window, the derivative form (FLUX-EXC) fails there on those boxes.
- The Monte Carlo of row 1101 gives no support: it cannot resolve the face (step 2, D5). At each beta its 12^4 face minimum is below its 8^4 one (0.579 against 0.642; 0.506 against 0.635; 0.485 against 0.606), each within about one error. That is the pattern of a level that falls with the box. (guide)
- A gap is not monotone in a coupling in general (ordered Ising example; guide grade after checks 1074, 1075).

**Mark for (MON-L) at the window in infinite volume: open.** Likely true as a sign (argued). No mechanism. As a theorem it is not weaker than C_beta.

### 4.2 The face leg

**Plain words.** With one plane frozen the model is a stack of flat two-dimensional sheets. Each sheet alone is understood (posted proofs). The transverse plaquettes tie the sheets together. Part (i-a): show that a weak tie changes nothing. Part (i-b): show the same for a tie of full strength. (reading)

**As a theorem.** (FACE-SG) at (infinity, beta, beta_T) for beta_T in [0, beta], uniform in the transverse size. Part (i-a) is the strip beta_T <= eps_beta, eps_beta of order Xi^(-2), about 10^(-3) (guide). Part (i-b) is the rest, about a thousand times wider (step 3, F4). (argued)

**Cost of part (i-a).** One O(4) sheet in a small field of arbitrary direction must keep its mixing. Remaining input (check 1100): sign-cluster decay in a field on tori (PIN-U or PIN-2 for pins with mixed signs along a layer, plus the torus form of T2; or UNS plus control of the outer block fields), together with EV. Replacements on file: FST-P (a Dobrushin-Shlosman sum below 1 on one pinned square of the zero-field sheet), FST-T (tree bounds on cumulants at zero field); both open; FST-P gives FST-F. (reading)
- First lemma: PIN-2, the two-colour bound (plus and minus pin clusters both near one deep site). Second: EV, the neutral part.
- Nearest false models: Lemma W (the wall monotonicity fails on one site, every b > 0); P1 and A1 (pinning monotonicity fails in a field, three sites); G1, G2 (two-site XY, antiparallel fields); model 5.4 (EV does not follow from crossing bounds; not O(4)-invariant); the O(2) sheet at large coupling (no decay at all; Frohlich and Spencer, recalled); row 1077's Ising example (16) (a gap alone does not give stability).
- Evidence for: no counterexample for the sheet (rows 1096, 1099); PIN-U holds for one-signed layers (Lemma LS); EV holds at zero field for local pairs (Lemma EV0); in the guide run the sign clusters shrink with the size (0.376 at L = 24, 0.116 at L = 48, beta = 2.5).
- Evidence against: six proof routes stopped at named steps (row 1096); UNS is open; Lemma DA needs an unwritten extension; the amplitude piece of EV "has no lower-model form" (argued there); swap clusters fill the torus (guide).
- Mark: open; believed true; a two-dimensional problem with a toolbox. It is the easiest of the open inputs. Its yield is the strip only.

**Cost of part (i-b).** No reduction. The tie is of order one. Row 1053's reading: marginal in two transverse dimensions; "the wall, with the frame problem in transverse form".
- First lemma: (P4-MIX) at kappa of order one, neutral sector. P4 is four O(4) sheets with the on-site potential kappa (1/2) tr(Phi_1 Phi_2 Phi_3^(-1) Phi_4^(-1)); it is the face with half of the transverse plaquettes (Lemma CB-T). Its one-site neutral variable is the plaquette trace x_p. Minimal form: the covariance of x_p(0) and x_p(n) decays exponentially at kappa = beta_M in the window, uniformly in the box.
- Nearest false models: compact U(1) in P4 (three massless combinations, argued at Gaussian level, row 1076 L379); the product of an SU(2) face with a U(1) face (charged decay without a neutral gap, `gap-wall-vectors-max.md` L167); for uniform-pin forms the ordered three-dimensional O(4) slabs of Proposition CA-FAIL.
- Evidence for: at kappa = 0 it is the anchor; at large kappa the target is the constraint set Phi_1 Phi_2 = Phi_4 Phi_3, a compact homogeneous space with a non-abelian group acting, where a gap is the standard belief (my remark; belief, no source checked). The rigid group G survives every cut, so charged decay may port (Lemma RIG; (FACE-TW), parked).
- Evidence against: row 1084: three ports of the posted neutral step fail with exact counterexamples (P4-NA, P4-SIGN, P4-LIFT); "P4-MIX for kappa > 0 remains OPEN". No run resolves the face at beta_T = beta.
- Mark: open; no mechanism.

**One point for the lead (argued).** EV in (i-a), (SING) in P4 and (SING) in GH2 are one family: mixing of the neutral sector of a two-dimensional non-abelian system once the weight has a field, an invariant potential or a twist. The posted proofs reach the neutral sector only through association for the untwisted zero-field ferromagnet (row 1076 L377, from row 1009's reading). So the first cases of all three legs of BR-2 stop at the same step.

### 4.3 (W) directly

**Plain words** (row 998 9.1, `parts/gap.md` L32-34). On each doubling of the box, between the last small box and the first good box, a free energy shrinks by a fixed factor; in a model with a massless particle it never gets small.

**As a theorem.** (BDD-Delta) and (Z-UNB) (Theorem ZD-c); or (CAS) with theta < 1 and the base (TH); or (BDD-Delta) and no uniformly recurrent critical element (Theorem CR, (LIOU)). On periodic tori, all flux sectors, uniform in the cutoff, at one physical size.

**First lemma a proof row would attack.**
- The blind half: (BDD-Delta) at physical sizes beyond first passage. Its first open inputs on the supply side are (SV3) and (UV-Cas) (row 1058). It is true for compact U(1) and is not selective.
- The selective half, (Z-UNB) or (LIOU) or (CAS): no first lemma is on record. Row 998 9.4: "No mechanism for the selective step is on record". Rows 1004 to 1050 add none.

**Nearest models where it is false.** For the selective half: compact U(1) at weak coupling (theorem for Villain at beta >= 2^14); the free photon (S_2 >= 5.06; floor 17.04); a product with a massless factor (Lemma PT); the no-seed model of Proposition NP, in which D contracts by any theta on any J doublings. For (BDD-Delta): frozen Z_2 in the form (BL-c). (reading, `parts/gap.md` test table)

**Evidence for.** Measured physics (row 1063). Both ends are controlled: strong coupling by expansions, weak coupling up to first passage by the account. No model of the SU(2) class with first-passage data and no gap is known or believed (`parts/gap.md` L263-265). (reading)

**Evidence against.** None as a statement. As a proof target: every engine found is blind; 33 methods are set aside; "No route is near closure" (`parts/gap.md` L200). (reading)

**Mark: open.** The cost is one selective inequality at each scale between first passage and the seed size.

### 4.4 The three costs side by side (argued)

| Input | Has a mechanism on file? | Small parameter? | Yield if proved | Comparison with the target |
|---|---|---|---|---|
| Face (i-a) | yes (FST-BD, Pei's bonds, sign clusters) | yes, beta_T <= about 10^(-3) | a strip next to the anchor | far weaker; not on the path alone |
| Face (i-b) | no | no | the face point | not known comparable; "the wall in transverse form" (row 1053) |
| (MON-L) | no | no | C_beta, given the face | stronger than C_beta (check 1075) |
| (W) | no | no | the target | the target |

So after rows 1089-1107 BR-2 holds two statements with no mechanism in place of one. Its gain is not a cheaper target. Its gain is small exact models (GH2, P4) in which a selective step at order-one coupling can be tried in two dimensions.

## Step 5 result, task (2): what BR-2 gives if it is fully proved

**Answer.** BR-2, fully proved, gives C_beta for each beta in [2.3, 2.6]: exponential clustering of the gauge-invariant local observables in the isotropic infinite-volume limit states, at that one lattice coupling. It gives neither (W) nor T_JW-lat. (reading for the first sentence: `gap-bridge-exercise-opus.md` L410, check 1070 L178-184; argued for the rest)

"Fully proved" means here: (FACE-SG) at (infinity, beta, beta), both parts (i-a) and (i-b); and (MON-L) on [beta, infinity) in infinite volume. The range of beta is the range for which both are proved. The files state both for the window only.

By the lane's own rule this outcome does not count as closure: "A gap in lattice units that is not uniform in the cutoff" (`gap-crux-exercise3-max.md` L138-151, outcomes that do not count).

### 5.1 The exact missing steps to (W)

(W) is a statement on periodic cubes, with all flux sectors, at one physical size, uniform in the cutoff (step 1, S1). From C_beta at a window coupling three steps are missing.

1. **(P-GAP), the torus step.** A lower bound m(b^3) >= m_0 > 0 for the periodic cubes of all sides b >= b_0 at that beta, flux sectors included. C_beta does not control the electric-flux sectors of a finite torus (check 1070 L182). By Lemma FLUX-W the flux part is an unbroken-centre statement on tori. (reading)
2. **(D-SUB), sublinear Casimir free energy.** The lower limit of D(a)/a is below m_0/64. With (P-GAP) this gives the seed at that coupling, by Corollary Z2 of `gap-phys-seed.md` L305-306 (proved given Theorem ZD). (reading)
3. **The carry.** A seed at beta = 2.3 "is a theorem about one lattice theory. It enters the continuum statement only through the carry" (`gap-ladder-max.md` L243). The carry is (NOCRIT) of row 709 plus a climb at the asymptotic-freedom rate, in the form (CARRY-AF): sup over beta >= beta_0 of n(beta) a_T0(beta) is finite. It is open. It is false for compact U(1), for the frozen groups and on K7 lines. It is set-aside method 23. (reading)

Step 3 is the wall again: (NOCRIT) "gives the gap of all cubes at every coupling" (`gap-mid-max.md` L207). So BR-2 would supply the base of an induction whose step is the open selective inequality. (argued)

### 5.2 The exact missing steps to T_JW-lat

T_JW-lat asks, for all large j, for a clustering rate c/l in physical units, that is a lattice rate at least c a_j/l at the coupling beta_j, with beta_j tending to infinity (step 1, S6). Two ways from BR-2; each has one missing step.

**Way A: the window, then a carry.** Missing: the carry of step 3 above, in clustering form (no flux clause is needed for T_JW-lat). Same status: open, no mechanism, method 23.

**Way B: BR-2 at every beta >= beta_0.** Then m_iso(beta) >= m_face(beta) for all large beta. Missing: **(FACE-SCALE)**, m(infinity, beta_j, beta_j) >= c a_j/l for all large j. No file studies it. Three remarks (argued).
- At the anchor (beta_T = 0) the analogue of (FACE-SCALE) is false. OpenAI's posted two-sided bound gives the anchor rate the size sqrt(beta) e^(-pi beta) up to constants. The two-loop law gives a_j/l the size beta_j^(51/121) e^(-(3 pi^2/11) beta_j) up to constants (recalled; I did not open the account for the exact form of its trajectory). Since pi > 3 pi^2/11, the anchor rate times l/a_j tends to zero like e^(-0.45 beta_j). A lower bound by the anchor rate is a positive lattice rate at every coupling and zero in physical units. The lane has met this pattern before (Route Z: "a lattice mass of order a^2, zero in physical units", `gap-ladder-max.md` L225).
- At the face point (beta_T = beta) the scaling law of the rate is unknown. The face is not an anisotropic discretization of the same continuum theory: that needs beta_L beta_T = beta_M^2 at tree level, and the face has beta_L infinite with beta_T = beta_M. So no universality argument gives the face the four-dimensional exponent.
- (MON-L) at every beta and (FACE-SCALE) pull against each other. Put r(beta) = m_face(beta) l/a(beta). (MON-L) with the expected upper bound m_iso <= C a/l gives r <= C. (FACE-SCALE) is r >= c. Both hold only if the face rate has the four-dimensional scaling law exactly. If r tends to zero, Way B gives no physical rate. If r is unbounded, (MON-L) fails at large beta.
Also on Way B: (MON-L) at large beta has guide evidence against every box-uniform proof (row 1090: the crossing near 3.4).

**Further clauses of T_JW-lat that C_beta does not carry** (reading, check 1070 L180 and check 1055): a common rate for a total set of observables with constants that depend on the observable only; matched observables across cutoffs; the limit states of the admissible periodic cubic tori (check 1054). With T0's (H2) and (TOT) these pass to the Jaffe-Witten form.

### 5.3 Summary of task (2)

| From BR-2 fully proved | Result | For which beta | First missing step |
|---|---|---|---|
| C_beta | yes | each beta in [2.3, 2.6] where both legs hold | none |
| (SEED) at fixed coupling | no | - | (P-GAP) with flux sectors, then (D-SUB) |
| (W) | no | - | the carry (CARRY-AF) = (NOCRIT) plus the asymptotic-freedom climb, after (SEED) |
| T_JW-lat | no | - | the carry in clustering form (Way A), or (FACE-SCALE) with BR-2 at all large beta (Way B) |

Marks: the first row is a reading; the others are argued from the cited lines; (FACE-SCALE) is open and is named here for the first time (grep of the lane folder for "FACE-SCALE": no hit before this file).

## Step 6 result, tasks (3) and (4): the next two proof rows, and the row not to run

### 6.1 How the choice was made (argued)

The rule: go where the proof could die first, not where it is easiest.

- The easiest open input is the face near the anchor (i-a). It has a toolbox. Its yield is a strip of width about 10^(-3) in beta_T (4.2).
- Three inputs have no mechanism: the face at order-one beta_T (i-b), the descent (MON-L), and the carry. The carry is set-aside method 23 and is the wall itself (5.1); a row on it would be a row on (W).
- The two BR-2 inputs with no mechanism each have a smallest exact case on file, from row 1076: P4 for (i-b) and GH2 for (MON-L). Each is two-dimensional, has finitely many fields per site, has proved ends (given the posted O(4) theorems), is false for compact U(1), and has no small parameter in its interior. So each is a selective statement at order-one coupling in the smallest model where BR-2 needs one.
- Both stop today at one step: mixing of the neutral sector without association (4.2, last paragraph). Row 1084 closed the association ports with exact counterexamples. It tried nothing else.

So BR-2 dies first at this step, in these two models. If the step cannot be done there, neither mechanism-free leg of BR-2 has a first case, and the easy work on (i-a) has no consumer. If it can be done, BR-2 gets its first selective mechanism at order-one coupling, and the lane gets a candidate for the wall's selective step from the two-dimensional side.

Order: row 1 below first. (MON-L) holds the four-dimensional difficulty, and without it the face has no consumer.

### 6.2 Recommended row 1: `gap-descent-first-case`, the statement (GH2-DESC)

**Statement.** Model GH2_2(beta_L, beta_M) of row 1076 (Lemma CB-L with n = 2; `gap-bridge-vectors-max.md` L226, L354-367): a two-dimensional SU(2) lattice gauge field with Wilson coupling beta_L, and two S^3 fields with covariant nearest-neighbour coupling beta_M. For every beta_M in [2.3, 2.6] and every beta_L in (0, infinity):
- weak form: for gauge-invariant local Lipschitz F and H at distance n, abs(Cov(F, tau_n H)) <= C_(F,H) e^(-a n), with a = a(beta_M) > 0 independent of beta_L and of the box (free subgraphs and tori with all sides at least L_0);
- monotone form (the two-dimensional case of (MON-L)): the rate at beta_L is at least the rate at beta_L = infinity.
The row proves one form, or refutes the monotone form, and says which.

**Why this is where the proof could die.** 4.1: (MON-L) has no mechanism and contains C_beta. This is its smallest exact case. Both ends are theorems given OpenAI's Theorem 3.1 (two free sheets; Lemma DEC of row 1084). The interior has twisted weights, outside the association class (counterexample GH-NA, row 1084).

**Order of work** (three named ways, none by association).
1. Lemma KIN in this model: T(beta_L) = S* D(beta_L) S, with S* S the two free sheets. Replace the operator-norm step of Proposition DIL, which loses the volume factor (`gap-descent-sign.md` L123), by a bound per unit length in infinite volume.
2. Integrate the two-dimensional gauge field exactly (axial gauge, independent plaquette variables). Write the result as a weight on the colour flux across cuts. Test whether it acts on the neutral pair states only by lifting them (the reasoning of 4.1, "A mechanism near the face", made exact or refuted).
3. Interpolate between the two proved ends in the kinetic variable w = e^(-t/4), where T(w) has a power series with non-negative operator coefficients (Corollary KIN-D).

**Tests that any proof must pass.** Compact U(1) in GH2_2 at large beta_M (the statement is false there; the proof must stop); frozen Q_8 (KIN-7); Example KIN-6; a product with a massless factor; GH-NA.

**Stop rule.** A proof; or a counterexample by hand (for the monotone form: one beta_L where the neutral rate is below the rate at infinity; for the weak form: a vanishing rate); or one named step that failed in three written ways, the association ports of row 1084 not counted. No computer-assisted step. Lean-formalizable in principle.

**Model tier.** The lane's hard-proof author tier, by the provider that wrote rows 1081 and 1085 (it holds Lemma KIN and step (S)). One cross-provider check at the lane's check tier. The settings file decides the model names.

**What it changes.**
- Proved: the first selective step at an order-one twist. (MON-L) gets a mechanism. The whole leg beta_T = 0 from the anchor toward the corner F4 becomes a proof target, and the F4 proof row (W3 of row 1103) gets a consumer.
- Refuted or stopped: the descent has no first case. The registry entry for BR-2 goes from "provisional (wounded)" to blocked-local at (SING), and the face rows lose their consumer.

### 6.3 Recommended row 2: `gap-face-order-one`, the statement (P4-MIX) at kappa of order one

**Statement.** Model P4(beta_M, kappa) of row 1076 (Lemma CB-T): four O(4) sheets Phi_1..Phi_4 on Z^2 with coupling beta_M and the on-site potential kappa (1/2) tr(Phi_1 Phi_2 Phi_3^(-1) Phi_4^(-1)). For every beta_M in [2.3, 2.6] and every kappa in (0, beta_M]: G-invariant local Lipschitz observables cluster at a rate a(beta_M, kappa) > 0, uniform in the box (free subgraphs and tori with sides at least L_0), locally uniform in kappa. Minimal form, to be done first: the covariance of the plaquette trace x_p at 0 and at distance n is at most C e^(-a n) at kappa = beta_M.

**Why this is where the proof could die.** 4.2: part (i-b) of the face is first in chain order, has no reduction and no mechanism. P4 is the face with half of the transverse plaquettes and one neutral variable per site. Row 1076's ranking: "A 'no' at P4 kills BR-2 at its first step."

**Order of work** (three named ways, none by association).
1. Use the orbit structure. G acts transitively on the level sets of x_p at one site (Lemma P4-ORB). Condition on the field x = (x_p(u)). Decide whether the conditional law has charged-type decay from the rigid group (Lemma RIG; the posted estimate (3.61) as a cited input), and what effective law x itself has.
2. Start from the large-kappa end: the constraint set Phi_1 Phi_2 = Phi_4 Phi_3 and its first correction in 1/kappa.
3. Condition on three sheets: the fourth is an O(4) sheet in a field of norm kappa and varying direction ((M1) of row 1091). Apply the averaged block criterion FST-BD (checked by row 1094) on blocks large against Xi, with the field of order one.

**Tests that any proof must pass.** Compact U(1) in P4 at large beta_M (three massless combinations; the proof must stop); the product of an SU(2) face with a U(1) face; row 1077's Ising example (16); the three closed ports P4-NA, P4-SIGN, P4-LIFT.

**Stop rule.** As in 6.2: a proof; a counterexample by hand (a kappa in (0, beta_M] where the x_p covariance has no exponential bound uniform in the box); or one named step that failed in three written ways, the three ports of row 1084 not counted.

**Model tier.** The lane's hard-proof author tier, by the provider that wrote row 1084 (it holds the P4 counterexamples and the reading of OpenAI's Section 3.11). One cross-provider check at the lane's check tier.

**What it changes.**
- Proved: a mechanism for the neutral sector at order-one coupling. EV of part (i-a) is the small-field member of the same family (4.2), so the sheet line of rows 1096-1100 can then be taken up with a method instead of a search. The full face (all transverse plaquettes) becomes the next statement.
- Refuted or stopped: the face point (infinity, beta, beta) is out of reach of the two-dimensional methods on file; BR-2 is retired at its first step; the sheet line has no consumer on the gap path.

### 6.4 One guide run beside the two rows (guide; not a proof row)

One serial job, cheap, before or beside rows 1 and 2. It tests each statement for an early death and it calibrates (MON-L).
- GH2_2 on L^2 with L at least 128: the neutral rate against beta_L, at beta_M = 2.3, 2.4, 2.5 (a dip below the value at infinity would refute the monotone form at guide grade).
- P4 on L^2 with L at least 128: the x_p correlation against kappa in (0, beta_M].
- The reduced face with long sheets: longitudinal sides at least four anchor correlation lengths (128 to 192), transverse sides 4 and 6, beta_T from 0 to beta. This replaces the face column of row 1101, whose sheets of side 8 and 12 are smaller than the anchor's length (step 2, D5). It says whether the face rate at beta_T = beta is near the anchor's, and so how much slack (MON-L) has.
Control: at beta_T = 0 the O(4) lengths of Borisenko and Skala, as in row 1101. Machine rule: one numeric worker.

### 6.5 Task (4): the row I would not run

**A proof row on PIN-2 or EV now** (the continuation of rows 1096 to 1100; route S1 of row 1103). Reasons (argued).
1. It is the easiest open input, and the rule says not the easiest.
2. Its yield is clustering on the strip beta_T <= eps_beta, about 10^(-3) wide (step 3, F4). The face point needs beta_T = beta. The stretch between has no reduction.
3. Its consumer is the face leg, whose consumer is (MON-L); neither has a mechanism. A proved strip would sit unused.
4. Its hardest part, EV, is the small-field member of the neutral-sector family. Row 2 attacks that family where it has no small parameter. If row 2 finds a method, EV comes after it with that method.
Reopen: when row 2 ends with a proof; or if the owner wants the strip as a result of its own (it would be a first clustering theorem for a four-dimensional coupled SU(2) system at a window sheet coupling, not a step to the gap).

Also not now, for the same kind of reason, in one line each: the F4 proof row (W3 of row 1103) before row 1 gives it a consumer, since from a floppy start the carry is (LIN-path), stronger than the target; and a repeat of the 4D Monte Carlo at 8^4 and 12^4, since it cannot resolve the face.

### 6.6 Limits and strong words, read against this file

- Nobody has checked this file. It is a direction row. It proves nothing. No run was made.
- "Cannot test" (step 2, D5): at the sizes 8^4 and 12^4, if the face length is at least of the anchor's order. If the transverse coupling shortens the face length to a few lattice units, the row 1101 table does resolve the face. No file decides this; 6.4 would.
- "About 10^(-3)" for eps_beta: from the guide reading eps of order Xi^(-2) in `gap-face-stability.md` L195; check 1093 gives a smaller guide value (a^2/X). It is not a proved size.
- "Factor ten of slack": the anchor's neutral rate 2/xi against published isotropic scalar masses; both recalled or cited from row 1101's tables; a guide.
- The exponent comparison pi against 3 pi^2/11: the first number is from a posted, unrefereed theorem; the second is the recalled one-loop coefficient; the account's exact trajectory was not opened.
- "A mechanism near the face" (4.1) is physics reasoning. It is not a lemma.
- "No mechanism" means: none found in the files read. It is not a statement that none exists.
- "One family" (4.2): a reading of three stated obstacles; no implication between them is proved.
- Not read: the proofs inside `gap-pinu-ev.md` step 4 to 6 line by line (check 1100 holds them); `gap-face-exercise-fable.md` steps 0 to 8; the two checks of row 1103 outside the sections named; rows 1089, 1090 beyond their lines in `parts/gap.md`; OpenAI's, Pei's and Ding, Huang and Yang's papers.
- Files changed: this file only. No commit, no push.

Credits: T. Balaban, and E. Sussman and L. Alpoge (with Claude and Codex as authors of their text) for the account that the target serves; the authors of the OpenAI preprints on the two-dimensional O(n) and O(4) models; J. Ding, F. Huang and P. Yang; Y. R. Pei; W. Bardeen, R. Pearson and E. Rabinovici for the transverse-lattice picture behind the leg beta_T = 0; M. Creutz, A. Kennedy and B. Pendleton, B. Lucini and M. Teper, O. Borisenko and P. Skala for the numbers cited through row 1101; in this lane rows 978, 998, 1052, 1053, 1066, 1072, 1076, 1077, 1081, 1084, 1085, 1089, 1090, 1091, 1096, 1099, 1101, 1103, 1104 and their checks.

RESULT: Row 1108 (Claude Fable 5.2 high, laptop subagent; direction row, checked by no one, no run, no mass gap claimed): BR-2 fully proved gives C_beta for beta in [2.3, 2.6] at one cutoff, and neither (W) nor T_JW-lat (ARGUED); missing to (W): the torus step (P-GAP) with flux sectors, (D-SUB), and the carry ((NOCRIT) plus the asymptotic-freedom climb, set-aside method 23); missing to T_JW-lat: that carry, or the new open statement (FACE-SCALE) with BR-2 at all large beta, whose anchor analogue fails because pi > 3 pi^2/11. Costs (ARGUED): the face leg has two parts, and the reduction to sheets (PIN-U or PIN-2, T2 on tori, EV) covers the strip beta_T <= about Xi^(-2), about 10^(-3), while the face from there to beta_T = beta has no reduction; (MON-L) in the window is likely true as a sign, with about a factor ten of slack if the face rate is of the anchor's order, but as a theorem it contains C_beta and has no mechanism; the Monte Carlo of row 1101 cannot test it at 8^4 and 12^4 if the face length is of the anchor's order (19 to 33), because its sheets are smaller; (W) direct has no first lemma on file for its selective half. The first cases of the three BR-2 legs stop at one step, neutral-sector mixing without association ((SING), EV). Recommended proof rows: (1) `gap-descent-first-case`, (GH2-DESC), the descent in the two-field gauged two-dimensional model at every beta_L; (2) `gap-face-order-one`, (P4-MIX) at kappa of order one in the neutral sector; with one serial guide run on long sheets beside them. Row not to run now: a proof row on PIN-2 or EV, the easiest input, whose yield is the strip. OPEN: (MON-L), (FACE-SG) beyond the strip, (FACE-SCALE), the carry, (W).
