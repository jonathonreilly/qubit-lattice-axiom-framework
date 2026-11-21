# Direction row 1115: attack (SING) directly, or move the effort back to (W)

Written by Claude Fable 5.2, reasoning effort high (FINISH row 1115, `gap-sing-direction-fable`).
This is a direction file. It proves nothing. No mass gap is claimed.
Marks used: argued, guide, reading, open.

## Plan (six steps; each step appends its result below)

1. State the Jaffe-Witten target and the lane's crux (W) with its equivalents, from `library/open-registry.md` and `parts/gap.md`. Read the sources named in the brief.
2. Task (1): place (SING) against C_beta at window couplings; name the nearest model where (SING) is false.
3. Task (2): for each way in, give the first lemma, where it could die, and what closure would change.
4. Task (3): read row 1111's face endpoint records; say what follows for (MON-L), (FACE-SG) and BR-2; judge the longer endpoint run.
5. Task (4): compare with a direct return to (W); name the first (W) lemma.
6. Tasks (5) and (6): recommend the next two rows, name the row not to run, and write the RESULT line.

Status: all six steps done 2026-11-17. RESULT line at the end.

## Step 1 result: the target, the crux, and what was read

### 1.1 The target, in my words (argued; the standard statement, not a lane file)

**Jaffe-Witten target.** For the gauge group SU(2), a quantum Yang-Mills theory exists on R^4 and satisfies the Osterwalder-Schrader (or Wightman) axioms. Its Hamiltonian has a mass gap: the spectrum is 0 together with a part above a number Delta greater than 0. In lattice words: the Wilson SU(2) theories at couplings beta_j tending to infinity have a limit. In that limit the gauge-invariant local observables forget each other at an exponential rate. The rate is positive in physical units. It does not vanish as the cutoff is removed.

Two properties matter for every row below. (a) The rate must be uniform in the cutoff. (b) Every observable is gauge invariant, so every observable is a singlet. Apart from the centre, no rigid group is known that would give a four-dimensional proof a charged sector to start from.

### 1.2 The crux and its relatives (reading; sources: `parts/gap.md` L13-50, L101-112, L271-282; `library/gap-br2-direction-fable.md` step 1, S1-S7)

`library/open-registry.md` has no row for C_beta, PHYS-SEED or T_JW-lat (grep: 0 hits for each name). It has one row named W at L892 that points to t0-tree section 2. I did not open t0-tree and I do not identify that row with the gap wall. So the statements below come from `parts/gap.md` and from row 1108's record of the files it points to.

- **(W), the wall.** Take Wilson SU(2) on periodic cubes along the trajectory of the account of Sussman and Alpoge, which rests on Balaban's renormalization group. Fix one physical size L. Let z^-(L) be the lower limit over cutoffs of side times gap. Let D_0 bound the Casimir free energy from size L/4 on. (W) says: z^-(L) > 256 D_0 + 30 for some L at least four times the base size. It is uniform in the cutoff. It includes all flux sectors.
- **(PHYS-SEED).** Equivalent to (W) (Theorem ZD-c, row 720, cross-provider checked, conditional). It is also equivalent to (BDD-Delta) together with (Z-UNB). (CAS) with theta below 1 on a bounded range, with an extensive base, is sufficient.
- **C_beta.** At one lattice coupling beta, every isotropic infinite-volume limit state clusters exponentially on the gauge-invariant local observables. It is a statement at one cutoff. It does not contain (W): it has no flux clause and no carry to finer cutoffs (check 1070).
- **T_JW-lat.** There are c > 0 and a physical length l such that, for all large j, the limit states of the admissible periodic cubic tori cluster at rate c/l in physical units on a total set. With T0's (H2) and (TOT) it gives the Jaffe-Witten gap (check 1054). (W) implies its flux bound one way; the two are not equivalent (check 1055). No finite-size criterion for T_JW-lat is on file.

A correction of wording. The brief calls C_beta and T_JW-lat equivalents of (W). On the record only (PHYS-SEED) is equivalent. C_beta is weaker in kind (one cutoff). T_JW-lat is the clustering form of the target.

**In plain words.** Between the last scale that the account controls and the first good box, one selective inequality is missing at each scale. Selective means: false for a model with a massless factor. `parts/gap.md` L46-50 names two kinds of input: (K-one), a property at one scale with a number in it; (K-flow), a statement carried from first-passage data through the band.

### 1.3 Where BR-2 stands before this row (reading)

- BR-2 fully proved gives C_beta for beta in [2.3, 2.6] at one cutoff. It gives neither (W) nor T_JW-lat (row 1108, argued, unchecked).
- Row 1108 named two first cases: (GH2-DESC) for the descent and (P4-MIX) for the face at order-one coupling. It wrote down beforehand what a stop would mean: "the descent has no first case", BR-2 becomes "blocked-local at (SING)", and "the sheet line has no consumer on the gap path" (its 6.2 and 6.3).
- Row 1109 stopped at (INT-CMP). Check 1113 (same provider): stop VALID.
- Row 1110 stopped at NR. Check 1114 (cross-provider): stop VALID; NR is the minimal target restated; the obstruction is (SING) of row 1076.
- Row 1111 (guide, unchecked) resolves no neutral comparison.

So both rows ended in the branch that row 1108 had declared in advance.

### 1.4 Read for this row

Read in full: `parts/gap.md` L1-100, the entries of rows 1076, 1081, 1084, 1101, 1103, 1106, 1108-1111 (L161-173), and L177-282; `library/gap-br2-direction-fable.md` (301 lines); `library/gap-descent-first-case.md` (231 lines); `library/gap-descent-first-case-check-opus.md` (542 lines); `library/gap-face-order-one-astra.md` (855 lines); `library/gap-face-order-one-check-opus.md` (524 lines); `library/gap-long-sheet-guide-astra.md` (418 lines); `library/prior/gap-gauged-sigma-read-luna.md` (54 lines); `library/gap-bridge-vectors-max.md` L355-400 (one stretch inside L373-377 was cut by my first read command; I read L373-378 again in a second call).

Read at the lines named, because steps 3 to 5 use them: `library/gap-short-step-max.md` L83-134 and L318-353 (the forms (T-per), (T-pin), (T-vor); Lemma CHAIN; (FL), (DEC)); `library/gap-pinned-cell-gauge-max.md` L480-500 ((N1)-(N3)); `library/gap-o2-extension.md` L286-296, L340-346; `library/gap-checkerboard-singlet-astra.md` L49-186 (row 1084's reading of the posted singlet step). `parts/gap.md` L113-160 was read with each line cut at 1100 characters.

Records read (small JSON files in `runs/gap-long-sheet-guide-astra/`): the twelve analysis files of the P4 and face runs, for the pooled covariances, errors, autocorrelation times and mean values. No run was made in this row. No paper was opened.

Status: step 1 done. Step 2 next.

## Step 2 result, task (1): is (SING) at window couplings as hard as C_beta?

### 2.1 The members of (SING) (reading; row 1076 L377, row 1108 4.2)

(SING) is one statement with four instances on file.
- (S-a) GH2_2: gauge-invariant mixing for beta_L in (0, infinity), b = beta_M in the window. Twisted weights.
- (S-b) P4: mixing of corner singlets for kappa in (0, b]. An invariant on-site potential.
- (S-c) The full face: (FACE-SG) for beta_T in (0, beta], uniform in the transverse size.
- (S-d) EV: the neutral part for one sheet in a small field (the strip next to the anchor).
The posted proofs reach singlets only through association for the untwisted zero-field ferromagnet (row 1084's reading of OpenAI Section 3.11: "This restriction is essential"). All four instances leave that class.

### 2.2 Answer

**Not comparable, and not cheaper.** In detail:

1. **No implication either way is on file.** (reading) C_beta says nothing about P4 or GH2. (S-a) and (S-b) do not give C_beta: BR-2 needs (S-c) and (MON-L) as well.
2. **It is the same kind of statement as C_beta.** (argued, 2.3) Three comparison models bind it. A proof must read the group, the shape of the weight, and the whole state space. C_beta has the same three tests (`parts/gap.md` test table: compact U(1), Proposition V, the product with a massless factor).
3. **At the window it lives at longer lengths than C_beta.** (guide, 2.4) C_beta at beta 2.3 to 2.6 has a length of about one lattice unit. The anchor sheet has 19 to 33. P4 at kappa = b and the face at beta_T of order one have more than the anchor.
4. **(S-c) contains the four-dimensional difficulty.** (reading) Row 1053: the face is "the wall, with the frame problem in transverse form". Check 1075: BR-2 is stronger than its target C_beta.
5. **One half is easier.** (reading) The charged half is a conditional theorem at every coupling: (O5) of row 1110 and Proposition CB-CH of row 1076, both given OpenAI's (3.61). Four dimensions have no such half on file: no rigid group is known on the link variables (Lemma CEN+ of row 1016; its check holds that the absence of every other rigid group is not proved).

So (SING) is a second wall of the same kind. It stands in two dimensions. It is not on the path from the target: BR-2 fully proved stops at C_beta.

### 2.3 The nearest models where (SING) is false, and what each forces

**A. Compact U(1) in the same model, at the same couplings (nearest: only the group changes).**
- P4 for U(1): three combinations stay massless at Gaussian level (row 1076 L379; row 1110 (U1)). Check 1114 item 10 adds, at guide grade: beyond Gaussian order the covariance of x itself likely has a tail like distance^(-4), and the U(1) form of the constrained law (K4) has a neutral covariance with the same tail.
- GH2_2 for U(1), at beta_L = 0: the relative phase is a rotator with bond weight I_0(2b abs(cos(delta/2))) (row 1076). Its stiffness at alignment is (b/2) I_1(2b)/I_0(2b). At b = 2.4 that is about 1.07, next to the Kosterlitz-Thouless value of the standard rotator, about 1.1. (guide; two recalled numbers; the side is not decided)
- Forces: a step that fails for U(1). On file only the bracket of OpenAI's (3.7) does, and it acts on charged observables.
- Grade: belief at the window; theorem (Frohlich and Spencer, recalled) only for the standard rotator at very large coupling.

**B. A non-abelian sheet with a sharply peaked weight (nearest that keeps the group).**
- Van Enter and Shlosman prove first-order transitions for vector and gauge models with a sharply peaked interaction, in two dimensions too. The lane cites this as the source of Proposition V (`parts/gap.md` test table, row "w_p at its transition coupling"). I did not open the paper.
- At the transition coupling the energy has two values. In the symmetric finite-volume state the covariance of two bond energies does not decay. Both phases keep the rotation symmetry in two dimensions.
- So this is a two-dimensional model with a non-abelian rigid group and no box-uniform singlet mixing bound at one coupling. (argued; the charged decay in both phases is a belief)
- Forces: a proof of (SING) must read the shape of the weight, that is a number. The group and the dimension are not enough. (NO-1ST) of row 1109 is therefore a necessary part of (SING). It is not an artefact of the interpolation method.
- For an on-site peaked potential in P4 the same picture is a belief (the four sheets pull neighbouring sites to lock together); no theorem.

**C. A product with a massless factor; coupled XY layers (charged decay without neutral decay).**
- Row 1110 5.2: an SU(2) face times a U(1) face. Row 1112: Bighin and co-authors report one-body decay with power-law two-body correlations in two coupled XY layers (numerics and renormalization group, read by gpt-6-luna).
- Forces: the whole state space. (O5) and CB-CH cannot give (SING) alone.

**D. Frozen Q_8, for the monotone form only.** Example Q8-INF (row 1109; check 1113: holds at leading order for the K-neutral form).

Models A and B together say what row 998 says of the wall: the order-one input is "a number, not a qualitative property".

### 2.4 The lengths (guide; my reading of stored records of row 1111 and of numbers on file; errors are those of the records; not a result)

One exact fact first (argued by hand). At kappa = 0 the four sheets are independent and each is invariant under left and right rotations. By Schur's lemma E[q(u)_ab conj(q(v)_cd)] = (c(u - v)/2) delta_ac delta_bd, with c the sheet's two-point function E[Re(q(u) q(v)^(-1))]. Insert this in tr(H_u) tr(H_v): every index sum closes and gives 16 (c/2)^4. So
  Cov(x_u, x_v) = c(u - v)^4 / 4 at kappa = 0.
Check at u = v: 1/4, the variance of the real part of a Haar element. So at small kappa the trace x is a four-particle observable (rate 4m), and the bond energies are two-particle observables (rate 2m). Row 1111 (b) at kappa = 0.024 fits this: x_p candidate 0.26, E16 candidate 0.096.

| Object | Length or rate | Source |
|---|---|---|
| Isotropic 4D, beta 2.4 and 2.5 | scalar rate 0.95 to 0.98, and 0.66: length 1 to 1.5 | Lucini-Teper, Teper, as cited in row 1101 |
| Anchor sheet, b = 2.3, 2.4, 2.5 | second-moment length 19, 25, 33 | Borisenko-Skala; controls of rows 1101, 1111 |
| P4, b = 2.4: sheet two-point values c(4), c(8), c(16) | kappa 0.024: 0.377, 0.251, 0.142. kappa 2.4: 0.487, 0.397, 0.317 | mean values of E4, E8, E16 in the P4 analysis files |
| Face, b = 2.4, T = 4: c(8), c(32), c(64) | beta_T 0: 0.250, 0.058, 0.023. beta_T 0.24: 0.353, 0.243, 0.219. beta_T 1.2: 0.467, 0.366, 0.342. beta_T 2.4: 0.516, 0.416, 0.392 | mean values of E8, E32, E64 in the face analysis files; T = 6 agrees within one percent at beta_T above 0 (0.353, 0.243, 0.219; 0.467, 0.364, 0.339; 0.516, 0.414, 0.389) |
| GH2_2, beta_L = b and 4b | no finite-beta_L channel passes the gates; in the one example printed (beta_L = b = 2.3) E1 is resolved at distance 2 and not at 3 | row 1111 (a) |

Reading.
- The rigid corner groups act on one link field Phi by Phi -> g Phi g'^(-1). So E[Phi] = 0. If the state clusters, c(r) tends to 0 at distances far above the charged length.
- At the anchor c(64) = 0.023. With the transverse coupling on, c(64) is 0.22 to 0.39 at half the box. So on the face at beta_T at least 0.24 the box of side 128 is not far above the charged length. The transverse coupling makes the sheets stiffer. It does not make them shorter. (guide)
- P4 shows the same trend: at kappa = b the two-point values fall by a factor 0.80 from distance 8 to 16, against 0.57 at kappa = 0.024.
- This agrees with (O5): its rate is c/s(2b), the scale of a sheet at coupling 2b. It agrees with row 1053's remark that the stiffness of a block of sheets is marginal.
- GH2_2 goes the other way. The two-dimensional gauge field at beta_L = 2.4 has string tension -log(I_2(2.4)/I_1(2.4)) = 0.71 per plaquette (hand series: I_1 = 2.298, I_2 = 1.134). The sheet mass squared is about 0.0016. So at beta_L of order b the colour is bound at one lattice unit, and the gauge-invariant field rho has stiffness below b/2 (Lemma GH2-0). No tail is seen there. A short length, or a small overlap; the run cannot tell which.

So the two legs of BR-2 differ at the window. The face leg runs into a regime that is deeper than the anchor. The descent leg is short at its isotropic end and deep at its frozen end. C_beta itself is short. BR-2 trades a one-scale problem for multi-scale ones.

One more number (guide). The first-order parameter of an expansion in kappa is kappa chi_x, with chi_x the sum over v of c(v)^4/4. The slice sums of row 1111 at kappa = 0.024 give chi_x between 1 and 2. So kappa chi_x is 2 to 5 at kappa = 2.4. Row 1110 found 3/kappa above 1 for the expansion from the other end. The window sits where neither expansion has a small parameter.

Status: step 2 done. Step 3 next.

## Step 3 result, task (2): each way in, its first lemma, where it could die, what closure would change

One remark covers all of them (argued). Every way ends at the same object: the dependence of a neutral mean on far boundary data, with no association. Ward identities exist for rotations only. So they bound charged responses and collective twists. They do not bound a neutral response.

### 3.1 Way 1: joint four-sheet blocks (named by row 1110 5.4 and by check 1114)

- **The criterion.** FST-BD of row 1091 (checked by row 1094), with blocks that hold all four sheets on a square of side l. The inter-sheet terms are then inside the block. Only pin terms stay: Gamma_l(a) = l^(-2) sum over w in the square and y on its outer boundary of e^(a abs(w - y)) p(y, w).
- **First lemma (J4-PIN).** There are a > 0 and P finite with: for every l, every pin configuration of the four sheets on the outer boundary, and every boundary site y, the sum over w of e^(a abs(w - y)) p(y, w) is at most P. The boundary has 4 l sites, so Gamma_l is at most 4 P / l, below 1 for l above 4 P. (argued arithmetic)
- **Its base case is already open.** At kappa = 0 the four sheets are independent. Then (J4-PIN) is the pinned-square criterion for one zero-field sheet. Row 1108 4.2 describes the lane's FST-P in those words, and FST-P is open (rows 1091, 1096, 1099; remaining input: PIN-U or PIN-2 with the torus form of T2, or UNS, together with EV). So this way contains the sheet line as its first step. It is not a way around it. (argued; I did not open row 1091's text of FST-P)
- **Where it could die.** (1) At the base case: six routes stopped there (row 1096), UNS is open, and the amplitude part of EV "has no lower-model form". (2) At model A: check 1114 notes that a finite-block criterion checked by a group-blind estimate would also prove exponential decay for U(1). Only the bracket reads the group, and it gives rotation responses. (3) At the block size: by 2.4 the blocks must exceed a length that is above the anchor's, plausibly the scale s(2b) of (O5). (4) At the supremum over pins: Proposition B', Theorem D2 and Lemma SHEET are warnings from four dimensions; I know no counterexample for P4.
- **What closure would change.** (P4-MIX) in a strong form at the window. EV and PIN-U of the strip by the same method. The full face still needs constants uniform in the number of sheets.

### 3.2 Way 2: a neutral estimate for the constrained end (K4), then continuation in 1/kappa (named by row 1110 5.4)

- **The model.** (K4) is a sigma model on SU(2)^3 with the energy b [E(A) + E(B) + E(C) + E(A B C^(-1))]. The rigid group SU(2)^4 acts transitively on its one-site space (Lemma P4-ORB at x = 1). There is no neutral one-site variable. The neutral content is in two-site singlets: bond energies, and the Q_u of (K7).
- **Charged decay ports.** Given B and C, the two terms that hold A are b Re(A_u [1 + V_uv] A_v^(-1)) with V_uv = (B C^(-1))_u (B C^(-1))_v^(-1). That is one right-twisted bond of strength at most 2b, the form (O4). So (O5) holds for (K4), given (3.61). (argued, one line)
- **First lemma (K4-N).** A box-uniform exponential bound for Cov(Q_u, Q_v) under (K4), b in the window. By (K9) this covariance is the first distant coefficient of the target.
- **Where it could die.** (1) At the common step: a neutral covariance of an interacting law outside the association class. Its U(1) form has a tail like distance^(-4) (check 1114, guide), so the step must read the bracket. (2) At the length: for U(1) the stiffness matrix of (K4) is I + w w^T with an eigenvalue 4 (check 1114). The model is stiffer than three free sheets. (3) At the continuation: the first correction has relative size 3/kappa, above 1 on the window (row 1110 3.4). Row 1077's Ising example (16) forbids "the end has a gap, so nearby points have one". Model B says the continuation must exclude a transition in kappa: (NO-1ST) in kappa.
- **What closure would change.** (K4-N) alone: the first neutral bound for interacting non-abelian sheets with no association. That is a mechanism for (SING). (P4-MIX) at kappa = b follows only with the continuation, and no tool on file reaches it. Two deaths; the second has no method.

### 3.3 Way 3: a monotone inequality from Proposition DIL and Corollary KIN-3 (check 1113, C5)

- **What the check said.** DIL and KIN-3 prove monotone inequalities with no rate at either end. That refutes one sentence of row 1109. The check does not offer them as a route.
- **Both tools are empty in GH2 as they stand.** DIL: the kernel of N on the invariant space holds every function of rho, so nu_1(N) = 0, the dilute range is empty, and the losses add over cuts (check 1113, C2 and C7). KIN-3 needs the frustration-free case, and Lemma KIN-4 closes that on the face for every beta_M > 0 (row 1076 6.3).
- **First lemma (FLUX-B).** A bound on the flux excess that does not grow with the box: the sum over cuts of <C_k>_1 - <C_k>_0 is at least -K, for b in the window and t in an interval. Its sign form, K = 0, is the sign form of (INT-CMP).
- **Where it could die.** At its first line, at the self term (row 1109, way 1). Guide: the sign fails for SU(2) on the two-site strip from b near 3.1 (row 1109 step 7), and row 1090's crossing came down with the box (3.416 at n = 6). If it reaches the window on strips up to the sheet's length, no box-uniform sign exists there.
- **What closure would change.** The bounded form gives m(t) >= m(0) - K t. That is positive only for t below m(0)/K. With m(0) at most about 0.25 (the frozen-end E8 candidates of row 1111, guide) this is a strip next to beta_L = infinity. It is not the window. The sign form would give (M), hence the first case of (MON-L). No tool for it is on file.

### 3.4 Way 4, from the target: the conversion in law, (CONV)

- **Why from the target.** In four dimensions every observable is a singlet (1.1). So any 4D engine needs a step from a response bound to mixing, with no association. Row 1018 has this step as clause (L3) of its pinned form (T-pin): "No statement 'Rbar small gives decay of all observables' is on record." Row 1052 has it as the missing finite-size criterion for T_JW-lat. Rows 1109 and 1110 met it in two dimensions: the charged engine ported ((O5), CB-CH), and the proof still stopped.
- **Statement (CONV).** Take a Markov field whose cells of side l are independent given the rings. Find a hypothesis H(l) on the pinned cells, stated in the law of the model, such that H(l) gives exponential clustering of all local observables at rate at least c/l.
- **First lemma: the right H.** Three forms.
  - (H-sup): the Dobrushin-Shlosman form with a supremum over pins. A classical theorem (recalled, not read). Its hypothesis is false or out of reach in the 4D pin class (Proposition B', Theorem D2, Lemma SHEET), and SSB of row 1110 refutes its single-sheet form in P4.
  - (H-ent): entrywise second-order responses small in law. This is the quantity Rbar of row 1018. Model B refutes it as a sufficient hypothesis for a state that may be a mixture: at coexistence one pin does not move the phase, so every entry is small in law, and the symmetric state does not mix. (argued; for extremal states it is not refuted)
  - (H-two): the two-sample form. Draw two pins independently from the ring law. Ask that the interior laws of one cell under the two pins are close, in mean. At coexistence the two pins sit in different phases half of the time, so (H-two) fails there, as it must.
- **Where it could die.** At "(H-two) gives mixing": the rare bad cells must be controlled in the model's own law, and that can be circular. At mixtures: the limit states of tori need not be extremal.
- **What closure would change.** (T-pin) gets its consumer. T_JW-lat gets a finite-size criterion. The two-dimensional rows get a target of the form "a response in law" in place of NR.
- It is blind as an implication. It is still the place where both first cases stopped.

### 3.5 Way 5, from the target: the supplier of that hypothesis in the one model with an engine, (RESP-TR)

- **The model.** One zero-field O(4) sheet. Its rigid group is transitive on the one-site space. So every change of one pin is a rotation of that pin, and there is no neutral one-site variable. Singlet mixing is a posted theorem there (through association). The engine is posted too (OpenAI's pinned-cell iteration).
- **Statement (RESP-TR).** For pinned cells of side l above the mixing length X(b), with pins drawn from the ring law: the cross-face response is small in the form H that (CONV) needs.
- **First lemma: from the collective response to the entries.** The posted iteration bounds the response to one common rotation of the pins. That is a sum of entries. H needs the entries, or a two-sample distance. Check 1097 records a limit of the same engine for the uniform form: "(3.61) bounds the difference, PIN-U needs the sum" (quoted from `parts/gap.md`; I did not open its context).
- **Where it could die.** There. Rows 1096 to 1100 stopped six routes for the form that is uniform in the pins. To my reading of `parts/gap.md` the in-law form is not on file; the reading row must confirm this before the row starts.
- **What closure would change.** With (CONV): a proof of singlet mixing for the sheet with no association. It ports to fixed twists, the class of (3.61). So it ports to GH2 given the gauge field and to the conditional sheets of P4, and (SING) reopens with a method. It also tests the design of (T-pin): whether a collective gain of Ward type can drive an entrywise response at all. If it cannot in two dimensions, with the engine in hand, then (DEC) of row 1018 needs an engine of another kind.

### 3.6 Two further ways, each in a few lines

- **The isotropic point alone, (GH2-ISO).** The target needs the point beta_L = b, not the path. By 2.4 the model is short there. In the coordinates (rho, v) of row 1109 it is the decorated ferromagnet at b plus b times a six-spin term. First lemma: a hand uniqueness bound in these coordinates. It could die at the number: already at beta_L = 0 the reduced bond has largest log-derivative b^2/4 = 1.44 (Lemma GH2-0's formula at s -> 0), and four neighbours with a one-site variance factor 1/4 give a constant near 1.4, not below 1 (guide arithmetic, not a criterion). It could also die at model A, which sits near its transition at the same couplings. Closure would reopen route RC ("a hand bound in the band") with a method. It is C_beta in miniature. Not first.
- **Stability from beta_L = 0.** Lemma DEC gives the end. Row 1109 notes that covariance decay does not give the tree decay of cumulants that an expansion in beta_L needs. Its yield would be a strip, as for the face.

### 3.7 The ways side by side (argued)

| Way | First lemma | First death | Yield if it closes |
|---|---|---|---|
| 1 joint blocks | (J4-PIN) | its kappa = 0 case is the open FST-P | (P4-MIX), strong form |
| 2 (K4), then 1/kappa | (K4-N) | the common step; then 3/kappa above 1 | a mechanism; (P4-MIX) only with a continuation that has no method |
| 3 DIL, KIN-3 | (FLUX-B) | both tools empty in GH2; the self term | a strip at beta_L = infinity, or (M) |
| 4 (CONV) | the right hypothesis H | bad cells; mixtures | a consumer for (T-pin) and for T_JW-lat |
| 5 (RESP-TR) | collective to entrywise | the engine bounds a sum of entries, not the entries | (SING) reopens with a method; a test of (DEC) |
| GH2-ISO | a hand bound | the number; model A | route RC reopens |

Ways 1 to 3 are the named ones. Each starts at a statement that is already open on file, or has no tool. Ways 4 and 5 put the common step in the one form that the four-dimensional route shares.

Status: step 3 done. Step 4 next.

## Step 4 result, task (3): the face endpoint records of row 1111

Everything in this step is a reading of stored, unchecked guide records. It is not a result. The endpoint errors are under-controlled, as row 1111 says.

### 4.1 The records

The lead's reading: at beta_T = beta the E64 covariances at distances 8, 16, 24 fall by a factor 1.9 to 2.2 per 8 sites, a naive rate 0.08 to 0.10. I read the same numbers in the analysis files, at all four transverse couplings. Pooled E64 covariance in units of 10^(-5), with the effective rates of the two steps, and the autocorrelation times in cycles:

| T | beta_T | C(8), C(16), C(24) | rates 8-16, 16-24 | tau |
|---|---|---|---|---|
| 4 | 0 | 18.0, 7.85, 3.80 | 0.104, 0.091 | 4 |
| 4 | 0.24 | 17.6, 8.20, 3.93 | 0.095, 0.092 | 4 to 5 |
| 4 | 1.2 | 18.2, 7.82, 2.97 | 0.106, 0.121 | 6 to 8 |
| 4 | 2.4 | 21.2, 10.4, 5.57 | 0.089, 0.078 | 28 to 31 |
| 6 | 0 | 7.81, 3.30, 1.40 | 0.108, 0.107 | 4 to 5 |
| 6 | 0.24 | 8.28, 3.78, 1.81 | 0.098, 0.092 | 5 to 7 |
| 6 | 1.2 | 8.39, 3.75, 1.56 | 0.101, 0.110 | 8 to 10 |
| 6 | 2.4 | 8.69, 3.93, 1.90 | 0.099, 0.091 | 25 to 28 |

Row 1111's own candidates agree: 0.105(4) at the anchor (T = 6), 0.103(5) at beta_T = 0.24 (T = 4, both axes pass), 0.102(4) at beta_T = 1.2 (T = 4, pooled; one axis fails the bin gate).

### 4.2 Four observations

**(a) An effective rate is an upper bound (argued).** The face transfer operator is S* S, so it is non-negative (Lemma KIN). For an observable O in one time slice, the connected correlation is a sum of c_n (lambda_n/lambda_0)^t with c_n >= 0, plus the images around the torus. A ratio C(t + s)/C(t) is then a weighted mean of the factors (lambda_n/lambda_0)^s. So every effective rate is at least the lowest rate in the sum. Read the other way: the lowest neutral rate of the box is at most every measured effective rate. Higher states cannot make a rate 0.5 look like 0.09. Only two things can: an error bar that is too small, or a chain that is not stationary. (Not bounded here: the image terms, of order e^(-m L).) So the next design does not need an isolated plateau. It needs a resolved signal.

**(b) The curve does not move with beta_T (guide).** The E64 covariances at beta_T = 0, 0.24 and 1.2, where the gates pass or nearly pass, agree with the endpoint values within about 30 percent. E32 shows the same. There is no trend toward a fast decay.

**(c) The mean values say the box is too small for the face (guide).** By 2.4, the two-point value c(64) of one link field is 0.023 at the anchor and 0.22, 0.34, 0.39 at beta_T = 0.24, 1.2, 2.4, the same for T = 4 and 6. Since E[Phi] = 0, a clustering state has c(r) near 0 far above its charged length. So at beta_T at least 0.24 the side 128 is not far above the charged length of the face. The registered size condition, "128 > 4 x 25.39", used the anchor's length. It does not hold for the face.
- A one-loop reading of the slope (guide; recalled formula c(r) = const - (3/(2 pi B)) log r for a sheet of stiffness B): face at beta_T = 2.4, from c(8) to c(32): B about 6.5, or 2.7 b. P4 at kappa = b, from c(4) to c(16): B about 3.9, or 1.6 b. A sheet of such stiffness has a length far beyond any box (the posted exponent pi gives e^(12) to e^(20) lattice units; a recalled asymptotic form, used far from where it is proved).
- Then the rate 0.08 to 0.10 at beta_T above 0 is a level of the box. Two massless quanta with opposite lowest momenta on a side 128 have energy 4 pi/128 = 0.098. The measured values sit there. (guide; a coincidence is not excluded) At the anchor a number of the same size is a true two-particle rate: 2/length is 0.06 to 0.08 for a length of 25 to 35.
- The jump of the autocorrelation time, from 5 to 30 cycles, fits a mode of the size of the box.

**(d) The symmetry predicts it (argued; physics reasoning).** At beta_L = infinity the corner groups are rigid at every beta_T. No gauge field confines their charges. Row 1109 step 1 says the rate at the frozen end is a two-particle rate. The same holds on the face: two far charged excitations of one sheet form a singlet. So the neutral rate of the face is at most twice its charged rate m*. A neutral rate 0.5 would need a charged length of at most 4 at beta_T = beta. The mean values exclude that at guide grade.

### 4.3 What follows

I give the consequences under the brief's reading (the face rate is anchor-like, about 0.1) and under mine (the face is stiffer than the anchor and its rate is below what a box of side 128 resolves). They point the same way.

**(MON-L).**
- At the isotropic end the sign has a slack of a factor 7 to 10 or more: 0.66 to 0.98 against at most 0.1. The sign is not where a proof dies there.
- As a theorem (MON-L) then says: the isotropic rate is at least a small positive number. That is C_beta with a number in it. The face supplies only the number, and a poor one. Row 1108 D6 argued this; the records support it.
- The transverse coupling does not raise the rate. The longitudinal coupling does, from at most 0.1 to about 0.95. So in this picture the four-dimensional gap is made on the descent, by gauging the rigid groups. (argued from the numbers; guide) The face leg adds cost and no rate.
- The small-box dips of rows 1085, 1090 and 1109 keep their force against proofs that are uniform over boxes.

**(FACE-SG).**
- At beta_T = beta the face is at least as deep as the anchor (brief's reading) or deeper (mine). A proof needs the charged estimate at the scale s(2b) or beyond ((O5) for P4; (FACE-TW) for the face, parked), and then the neutral step at that scale.
- No one-scale method and no block of a size near the anchor's length can reach it. A strip result for part (i-a) changes nothing at this point.
- (FACE-SCALE) of row 1108 fails at guide grade, as at the anchor or worse. So Way B of row 1108 to T_JW-lat is closed at guide grade.

**BR-2's value.**
- Fully proved it gives C_beta at one cutoff with a rate bound at least ten times below the true rate. It needs two legs, and neither is easier than C_beta (step 2). It has no advantage over C_beta attacked directly.
- Its value that stays: two exact two-dimensional models in which the common step can be tried.
- Row 1108 wrote the consequence of a stop beforehand (1.3). Both first cases stopped. I recommend that the lead apply it: BR-2 goes from "provisional (wounded)" to blocked-local at (SING) and blocked-stronger at (MON-L); the sheet line (PIN-U, EV) has no consumer on the gap path. Reopen condition: a bound, with no association, for a neutral response to boundary data in any member of the family of 2.1.

### 4.4 The longer endpoint run

- **What it would decide.** With bins of 256 to 512 cycles and about 8000 cycles per point (autocorrelation 25 to 42 cycles; effective sample at least 100), it gives controlled errors for the endpoint E64 covariances. By (a) a resolved signal is enough. It would settle, at guide grade, that the lowest neutral rate of the 128-box is below about 0.1.
- **What it would not decide.** The clustering rate of the face. By (c) the box is too small at beta_T at least 0.24. A longer chain does not change the box. A separate neutral extraction does not change it either.
- **Cost.** Compute is small: four chains at about four times the present length, one serial worker, about an hour (my estimate from row 1111's time stamps; not measured). The cost is the agent that registers, runs and reports.
- **Verdict: not worth its cost as designed.** It would put good error bars on a level of a finite box. No row in step 6 depends on it. Both readings give the same consequences (4.3). The 0.5 reading is already excluded at guide grade by (a) to (d) together.
- **What is worth doing instead, with no new sampling.** One mechanical re-analysis of the stored records: the mean values c(r) with their errors, and the second-moment length of the link field at each beta_T (from the spin sums chi0 and chi1 if they were saved at beta_T above 0, else from the saved configurations; the raw records are on the Mac mini SSD). It would register "the box is below the face's charged length at beta_T at least 0.24" at guide grade. Mechanical tier. I did not extract the errors of the mean values; the files hold hot against cold agreement for them (the P4 entries I saw are below one error).
- If a later row needs the face's true rate, it needs a finite-size scaling design at box sides far above 128. I do not recommend that now.

Status: step 4 done. Step 5 next.

## Step 5 result, task (4): moving the effort back to (W)

### 5.1 What (W) has on file for its selective half (reading)

- Row 998 9.4: "No mechanism for the selective step is on record". Rows 1101 to 1114 add none. I found none in this row.
- Row 1018 wrote the four-dimensional short step in three forms. (T-per) is (CAS); it has no slot for a mechanism. (T-vor) has a blind half (Mack and Petkova's inequality, rebuilt) and an open series half with no soft sign. (T-pin) has a slot: Lemma CHAIN, an exact identity. Its open clauses: (L1), a bound of the response at one scale by the response below; (FL) and (DEC), the selective pair; (L3), the consumer.
- Route (ii) of rows 1011 to 1048 (frames): first failing step (N1); only (N3) is selective. (N1) to (N3) read typical fields at small effective coupling. Row 1011 says the repair "does not cross the band by itself".
- The account of Sussman and Alpoge, on Balaban's method, controls the scales up to first passage. Nothing on file controls a scale inside the band.

### 5.2 What rows 1108 to 1114 teach about (W) (argued)

1. **The engine was not what stopped the two first cases.** In GH2 and in P4 the selective charged estimate was there as a port ((O5), CB-CH). Both rows stopped after it, at the passage to singlet mixing. In four dimensions every observable is a singlet. So a 4D engine, once found, meets the same stop, unless clause (L3) exists.
2. **Lemma CHAIN and (O6)-(O7) are one identity in two settings.** In both, the response at the larger scale is a covariance, over the law of the rings, of conditional means of the cells. Row 1110 calls it the covariance of the conditional means. Row 1018 calls it the cross-cell covariance of the Neumann data.
3. **The 4D form may be simpler in structure.** In two dimensions the pins split into an orientation, which the Ward identity sees, and a shape, which it does not. In four dimensions the pin of a cell modulo gauge is gauge-invariant data, and the tensor K_c is already a response of that data. There is no passage from charged to neutral inside (L3). (argued; no proof; I know no file that states it)
4. **Model B is a test for every criterion in law.** A hypothesis that reads single-pin responses in law holds at a first-order transition, where mixing fails (3.4). So (T-pin)'s quantity Rbar alone cannot be the hypothesis of (L3).
5. **The lengths.** At the window C_beta is short and BR-2's face is deep (2.4, 4.2). A bridge through the face imports a scale that the target does not have.

### 5.3 The two choices side by side (argued)

| | (SING) attacked directly at the window | Back to (W) |
|---|---|---|
| Distance to the target | after it: the face uniform in the transverse size, (MON-L), (P-GAP) with flux sectors, (D-SUB), the carry | it is the target's crux |
| Mechanism on file | none for the neutral step | none for the selective half |
| Stops so far | two first cases, both valid; before them the three ports of row 1084 and the six routes of row 1096 | 33 methods set aside (`parts/gap.md`) |
| Lengths at the window | above the anchor's 19 to 33 on the face leg | about one for C_beta; the band for (W) |
| Open clause that both share | the passage from a response to singlet mixing | clause (L3) of (T-pin); the missing criterion for T_JW-lat |

**Verdict.** Move the effort back to (W). Enter through the clause that (W) shares with (SING). Do not open a third proof row on P4 or GH2 at the window by the named ways.

### 5.4 The first (W) lemma I would attack now

**Clause (L3) of the pinned form (T-pin), in the typical-pin form (CONV) of 3.4.** Reasons:

1. It is where the proof stopped in practice. Rows 1109 and 1110 had an engine and still stopped at this passage.
2. Without it (T-pin) has "no consumer" (row 1018 2.3). Work on (DEC), (FL) or (N1) to (N3) then has no use, even if it closes.
3. It is also the finite-size criterion that T_JW-lat lacks. With it, the swap of row 1052 (the target through clustering, with no flux clause and no frozen-group tests) gets its one-box reduction back (check 1054).
4. A row can decide it: a proof of an implication, or three hypothesis forms refuted by models A, B and C.

It is blind as an implication. I say so. The selective pair (FL), (DEC) is where a proof through (T-pin) must find its gain, and I name no first lemma for it. Row 1018 fixed no definition of the non-abelian content NA_l for blocked links and found "no exact identity"; nothing in rows 1101 to 1114 changes that. A proof row on (DEC) today would be a search with no object.

The second item is the supplier test (RESP-TR) of 3.5. It asks, in the one model with an engine, the question that (DEC) asks in four dimensions: can a collective gain drive the entries.

Not first, with the reason:
- (BDD-Delta): blind and believed true. A proof does not die there.
- (N1): it works above the band, where the account already has control.
- A hand bound in the band (route RC): its smallest case is (GH2-ISO) of 3.6. It could die at the number. I rank it third, after the two rows of step 6.

Status: step 5 done. Step 6 next.

## Step 6 result, tasks (5) and (6): the next two rows, and the row not to run

### 6.1 How the choice was made (argued)

The rule: go where the proof could die first, not where it is easiest.

- The two first cases of BR-2 did not die at the selective estimate. They had it as a port. They died at the passage from a response to singlet mixing (5.2, point 1).
- The four-dimensional pinned form has the same passage open, as clause (L3). Its selective pair has no object that a row can attack today (5.4).
- So the first place where a proof through (T-pin), through T_JW-lat, or through BR-2 can die is this passage. It has two halves: the consumer (way 4) and the supplier in the one model with an engine (way 5). The two rows below are these halves.
- Neither row is the easiest input. The easiest input is still the strip of the face. Neither row is on P4 or GH2 at the window, where two valid stops stand and the lengths are long (2.4).

Order: row 1 first, or both at once on different providers. Row 2 proves its statement in two forms so that it does not wait for row 1.

### 6.2 Recommended row 1: `gap-conv-in-law`, the statement (CONV)

**Statement.** Setting: a Markov random field on Z^d, d = 2 or 4, with compact one-site spaces and interactions of the lane's kind (the O(4) sheet, P4, GH2, Wilson SU(2) with the cube cells and rings of row 1018 2.3). Cells of side l are independent given the rings. Prove:
- (CONV-two): there is eps_0(d) > 0 such that, if for some l the two-sample hypothesis (H-two) of 3.4 holds with eps below eps_0, with a stated tail bound for the bad cells, then every limit state of the stated class clusters exponentially on the gauge-invariant local observables, at rate at least c/l;
- or the same conclusion from another hypothesis H that is stated in the law of the model.
Decide also (H-ent): prove, or refute by hand through model B, the implication "Rbar small in law gives mixing".

**Why this is where the proof could die.** 6.1. Row 1018: "(L3): OPEN". Row 1052: no finite-size criterion for T_JW-lat.

**Order of work.** (1) Write model B as a test: a first-order point, the single-pin responses in law, the two-sample distance. (2) The two-sample form: a coupling of two ring samples scale by scale, with the bad cells counted in the model's own law. (3) A restricted supremum: (H-sup) over a set of pins that carries the measure and is connected under single-pin moves.

**Tests that any proof must pass.** Model B (no mixing may be proved at coexistence). Compact U(1) at weak coupling (the hypothesis must fail; show where). A product with a massless factor. Row 1077's Ising example (16). Proposition B', Theorem D2 and Lemma SHEET (H must hold no supremum that they refute). The ordered slabs of Proposition CA-FAIL.

**Stop rule.** A proof of one implication; or hand counterexamples to three written forms of H; or one named step that failed in three written ways. No computer-assisted step. Lean-formalizable in principle.

**Model tier.** The lane's hard-proof author tier, by the provider that wrote row 1091 (it holds FST-BD and its proof). One cross-provider check at the lane's check tier. The settings file decides the model names.

**What it changes.**
- Proved: (T-pin) has a consumer. T_JW-lat has a finite-size criterion, so the swap of row 1052 has a one-box form. The two-dimensional rows get a target "a response in law" in place of NR.
- Refuted or stopped: criteria in law are closed until a hypothesis is found that excludes coexistence. (T-pin) is parked with its registry line "no consumer" confirmed. The path through (W) stays with the periodic form, whose consumer is the seed engine (Theorem S, Theorem ZD-c).

**Literature reading row it needs** (reading tier; repository first). In the lane: row 1018 2.1 to 2.3 (clauses L0 to L3), row 1013 (rule R9), row 1091 (FST-BD), row 1052. Outside, recalled by name and not opened in this row, so each statement and its hypotheses must be confirmed: Dobrushin and Shlosman (the constructive criterion; completely analytical interactions); Martinelli and Olivieri, and Martinelli, Olivieri and Schonmann (weak mixing gives strong mixing in two dimensions); Olivieri and Picco; Bertini, Cirillo and Olivieri (renormalization in the strong-mixing regime, rare regions); Bassalygo and Dobrushin, von Dreifus, Klein and Perez, Gielis and Maes (uniqueness with rare bad regions); Dobrushin's criterion in a transport distance for continuous spins; Chatterjee, "A probabilistic mechanism for quark confinement" (a strong form of the mass gap and the area law; it bears on the flux clause); Adhikari and Cao (correlation decay for finite gauge groups).

### 6.3 Recommended row 2: `gap-resp-in-law-sheet`, the statement (RESP-TR)

**Statement.** One zero-field O(4) sheet at coupling b in [2.3, 2.6]. Free subgraphs and tori with sides at least L_0. Cells of side l at least C X(b), rings, and the ring law of the model. Prove, with no use of the association steps of OpenAI's Section 3.11, so that the proof keeps fixed twists:
- (i) the entrywise form: the mean over the ring law of the sum over y in one face and y' in the opposite face of abs(K_c(omega)(y, y'))^2, in the normalisation that is scale invariant for the free field, tends to 0 as l grows (the two-dimensional Rbar of row 1018);
- (ii) the two-sample form (H-two) for the same cells.
The row proves (i), (ii) or both, or stops, and says which.

**Why this is where the proof could die.** 3.5. The posted iteration bounds a collective response. H needs entries or a two-sample distance. If a collective gain cannot drive the entries here, where the engine is a posted theorem and singlet mixing is known, it cannot be expected to in P4, in GH2, or in (DEC).

**Order of work.** (1) Independent random rotations of the pins: their mean square response is the sum of squared entries. Test whether the posted profile bound (the second variation against the profile energy, OpenAI (3.11)-(3.12) as row 1084 reports it) reaches rough profiles; the profile energy of a rough profile grows with the boundary, so this is the first place to look for the death. (2) A chord through the cell and the Markov property, with (3.62) for the charged two-point function across the chord. (3) The two-sample form through a coupling in annuli, charged part by (3.61).

**Tests that any proof must pass.** The U(1) sheet at large coupling (the response is scale invariant there; the proof must stop). Lemma W, P1, A1, G1 and G2 of row 1096 (the uniform forms fail in small examples; the in-law form must not contradict them). Model B (entries can be small with no mixing, so (i) is used only with row 1). Fixed twists: every step must hold in the class of (3.61).

**Stop rule.** As in 6.2. The six routes of row 1096 and the three ports of row 1084 do not count among the three ways.

**Model tier.** The lane's hard-proof author tier, by the provider that wrote row 1099 (it holds Lemmas CR, FREE and LS, the sign clusters, and Pei's bonds). One cross-provider check at the lane's check tier.

**What it changes.**
- Proved, with row 1: singlet mixing for the sheet with no association. It ports to the twisted class. So (GH2-DESC) in its weak form given the gauge field, and the conditional sheets of P4, become proof targets again, and (SING) reopens with a method. For (W): a collective engine can drive entries, so (DEC) has a model to copy.
- Refuted or stopped: (SING) stays blocked-local. The lane records that an engine of Ward type does not give entrywise responses even where singlet mixing is a theorem. The design of (T-pin) is then in doubt at (DEC), and the frame line (N1) to (N3) loses its argument for a consumer.

**Literature reading row it needs** (reading tier; repository first). In the lane: rows 1091, 1096, 1099 and checks 1094, 1097, 1098, 1100, with one question: does any of them hold an in-law or typical-pin form of PIN-U. Outside: OpenAI's Sections 3.2 to 3.8 and 3.11 at the pages that rows 1009, 1010 and 1084 read; Pei's Theorem 6.1; Ding, Huang and Yang's Theorems 5.1 to 5.3 (their boundary classes); weak-to-strong mixing for continuous or unbounded spins (Yoshida; Martinelli's lecture notes; both recalled by name, not opened).

### 6.4 Two items for the lead that are not rows

- **The registry entry of BR-2.** Apply row 1108's pre-declared consequence (4.3): blocked-local at (SING), blocked-stronger at (MON-L); the sheet line has no consumer on the gap path; reopen on a neutral response bound with no association.
- **One mechanical re-analysis, no new sampling** (4.4): the mean values c(r) with errors and the charged second-moment length at each beta_T, from the stored records of row 1111.

### 6.5 Task (6): the row I would not run

**A second proof row on (P4-MIX) at kappa = b, by joint four-sheet blocks or by the constrained end (K4) with continuation.** This is the "next decision" that row 1110 names. Reasons (argued).
1. The first lemma of the block way, taken at kappa = 0, is the open pinned-square statement for one sheet (3.1). The row cannot start before row 2 above ends.
2. The continuation from (K4) has a first correction of relative size 3/kappa, above 1 on the window, and no method (3.2).
3. P4 at kappa = b is stiffer than the anchor (2.4). The blocks would have to exceed a length that no hand argument on file reaches.
4. Its yield, (P4-MIX), is far from the target: after it come the face uniform in the transverse size, (MON-L), the torus step, (D-SUB) and the carry. BR-2 fully proved stops at C_beta.
Reopen: when row 2 ends with a proof.

Also not now, one line each:
- The longer endpoint run as designed: it would refine a level of a box that is too small for the face (4.4).
- A monotone row from Proposition DIL and Corollary KIN-3: both tools are empty in GH2 as they stand (3.3).
- A third attempt on (GH2-DESC) over the whole interval of beta_L: the stop of row 1109 is valid, and the interval crosses from a short regime to a deep one (2.4).
- A proof row on (DEC): it has no object yet (5.4).

### 6.6 Limits and strong words, read against this file

- Nobody has checked this file. It is a direction row. It proves nothing. No run was made.
- Every reading of row 1111's records is at guide grade. Row 1111 is itself unchecked. I did not extract the errors of the mean values. The one-loop readings and the lengths e^(12) to e^(20) use recalled formulas outside the range where they are proved.
- "Stiffer than the anchor" and "the box is too small": from mean values at half the box, at one coupling b = 2.4, one box side 128, transverse sides 4 and 6. The infinite face is not measured.
- 4.2 (a): argued. It uses a non-negative transfer operator and leaves the image terms unbounded.
- Model B: the theorem is recalled through the lane's citation of van Enter and Shlosman. I did not open the paper. Its use against (H-ent) is argued and is not written out. For an on-site potential it is a belief.
- "No mechanism" means: none found in the files read. It does not say that none exists.
- 5.2 point 3, "(L3) may be simpler in four dimensions": a guess with a reason. No proof.
- The exact formula Cov(x_u, x_v) = c^4/4 at kappa = 0 is argued by hand in four lines. No second reader.
- The literature names in 6.2 and 6.3 are recalled. None was opened. No claim about their content is made beyond the words in brackets, and those words need the reading row.
- Not read: row 1091's text; the files of rows 1096 to 1100; rows 1053 and 1077; t0-tree; the OpenAI, Pei, and Ding, Huang and Yang papers; `library/gap-short-step-max.md` outside the lines named.
- Files changed: this file only. No commit, no push, no post.

Credits. T. Balaban, and E. Sussman and L. Alpoge (with Claude and Codex as authors of their text): the account on whose trajectory (W) is stated, and the Bessel formula GL3 that row 1110 uses. The authors of the OpenAI preprints on the two-dimensional O(n) and O(4) models. J. Ding, F. Huang and P. Yang. Y. R. Pei. A. van Enter and S. Shlosman. J. Frohlich and T. Spencer. R. Dobrushin and S. Shlosman. G. Mack and V. Petkova. D. Brydges, J. Frohlich and E. Seiler. M. Creutz, A. Kennedy and B. Pendleton, O. Borisenko and P. Skala, B. Lucini and M. Teper, S. Gongyo, G. Bighin and co-authors, W. Bardeen, R. Pearson and E. Rabinovici, for what the lane's rows cite from them. In this lane: rows 998, 1011, 1018, 1052, 1053, 1076, 1077, 1081, 1084, 1091, 1096, 1099, 1101, 1108, 1109, 1110, 1111, 1112 and their checks 1113, 1114.

RESULT: Row 1115 (Claude Fable 5.2 high, direction row, checked by no one, no run, no mass gap claimed): move the effort back to (W) through the clause that (W) and (SING) share, and do not open a third proof row on P4 or GH2 at the window. ARGUED: (SING) is not comparable with C_beta and not cheaper; it is the same kind of statement (false for compact U(1) at the same couplings at belief grade, false for a non-abelian sheet with a sharply peaked weight at its transition, not implied by charged decay), so a proof must read the group, a number in the weight and the whole state space. GUIDE (my reading of row 1111's stored records, not a result): on the face at beta_T at least 0.24 the link two-point value at half the 128-box is 0.22 to 0.39 against 0.023 at the anchor, so the box is below the face's charged length, the rate 0.08 to 0.10 is a level of the box (4 pi/128 = 0.098) and an upper bound, the face is stiffer than the anchor and 0.5 is not its common neutral rate; hence (MON-L) has slack but is C_beta with a number, (FACE-SG) at beta_T = beta is deeper than the anchor, and BR-2 has no advantage over C_beta; the longer endpoint run is not worth its cost as designed, one re-analysis of stored records is. Each named way starts at an open statement: joint four-sheet blocks at the open pinned-square criterion for one sheet, (K4) at the common step and then at 3/kappa above 1, DIL and KIN-3 at tools that are empty in GH2. First (W) lemma: clause (L3) of the pinned form (T-pin), a mixing criterion from pinned responses in the law of the model with no association. Next rows: (1) gap-conv-in-law, the statement (CONV); (2) gap-resp-in-law-sheet, the statement (RESP-TR), entrywise and two-sample responses in law for one O(4) sheet from the posted engine; each with a reading row. Row not to run: a second proof row on (P4-MIX) at kappa = b by joint blocks or by (K4) with continuation. Registry: BR-2 to blocked-local at (SING) by row 1108's pre-declared rule. OPEN: (SING), (CONV), (RESP-TR), (DEC), (MON-L), (FACE-SG), (W).
