# Gap lane: what is left of clause (L3) after rows 1115-1121, and where the next proof effort on (W) goes

Written by Claude Fable 5.2, reasoning effort high (FINISH row 1122, gap-l3-direction-fable).
Direction row. No mass gap is claimed in this file.
Marks used: **argued**, **guide**, **reading**, **open**.

## Plan (at most six steps; each step appends its result below)

1. Read the sources named in the row in full. State the Jaffe-Witten target, the crux (W) and (PHYS-SEED) in my own words.
2. Task (1): say in plain words what rows 1115-1121 established about (L3).
3. Task (2): decide whether (T-pin) can have a consumer with a supplier weaker than one-scale singlet mixing; compare with (T-per).
4. Task (3): Theorem W of row 691 at the window couplings, tested with the mechanism of Proposition J.
5. Task (4): compare with every other open entry for the selective half of (W), by the rule "where the proof could die first".
6. Tasks (5) and (6): recommend the next two rows, name the row not to run, list registry changes. End with the RESULT line.

Status: all six steps done 2026-11-17. RESULT line at the end. Step 5.1 reports prior work in the lane that was found late; it changes the reading of steps 3 and 4.

## Step 1 result: the target, the crux, and what was read

### 1.1 The target, in my words (argued; the standard statement, not a lane file)

**Jaffe-Witten target.** Take the gauge group SU(2). A quantum Yang-Mills theory exists on R^4. It satisfies the Osterwalder-Schrader (or Wightman) axioms. Its Hamiltonian has the spectrum 0 together with a part above a number Delta greater than 0.

In lattice words. The Wilson SU(2) theories at couplings beta_j tending to infinity have a limit. In the limit, the gauge-invariant local observables forget each other at an exponential rate. The rate is positive in physical units. It stays positive when the cutoff is removed.

Three properties bind every row below.
- (a) The rate is uniform in the cutoff.
- (b) Every observable is gauge invariant. So every observable is a singlet. No rigid group other than the centre is known on the link variables.
- (c) The statement is about one state at each cutoff, the limit state of periodic boxes. It is not a statement about all boundary values.

### 1.2 The crux (W) and its equivalent (PHYS-SEED), in my words (reading: `parts/gap.md` L13-50, L101-112, L277-288)

- **(W), the wall.** Take Wilson SU(2) on periodic cubes along the trajectory of the account of Sussman and Alpoge, which rests on Balaban's renormalization group. Fix one physical size L. Let z^-(L) be the lower limit over cutoffs of side times gap, all flux sectors included. Let (L_0, D_0) be a bound of the Casimir free energy from size L_0 on. (W) says: z^-(L) exceeds 256 D_0 + 30 for one L at least 4 L_0.
- **(PHYS-SEED).** One periodic box of one physical size holds the seed of the engine, at every cutoff. The seed is a number: the thermal sum of the excited states of the box, below a fixed threshold. Theorem ZD-c (row 720, cross-provider checked, conditional) makes (W) and (PHYS-SEED) equivalent. Both are equivalent to (BDD-Delta) together with (Z-UNB).
- **Sufficient forms.** (CAS) with theta below 1 on a bounded range, with an extensive base. The fixed-coupling seed (SEED) at each beta of the window 2.3 to 2.6, with a carry to finer cutoffs. The carry is open (set-aside method 23).
- **The consumer on this side is proved.** Theorem S (rows 697 to 699, checked by two models) and Theorem SH (row 705, checked by row 707) take a seed on one periodic box to a gap on every larger cube. They use reflection positivity. They use no supremum over boundary values and no association.
- **In plain words** (row 998 9.6): one selective inequality is missing at each scale between first passage and the seed size. Selective means: false for a model with a massless factor.

Two names need care in this file.
- "(W)" is the wall above.
- Row 691 calls the hypothesis of its Theorem W also "(W)". I write **(DS-W)** for that hypothesis. It is a finite-cube condition with a supremum over boundary values. It is a different statement.

### 1.3 Clause (L3) (reading: `library/gap-short-step-max.md` 2.1 to 2.3)

Row 1018 wrote a short step as four clauses: (L0) closure of the class, (L1) a blind half, (SS) a selective half, (L3) a consumer. The pinned form (T-pin) carries the response Rbar(l). Rbar is the mean square, in the law of the model, of the cross-cell covariance of the Neumann data of a pinned cube, in the normalisation that is scale invariant for the free photon. Lemma CHAIN is its mechanism slot. Its clause (L3) reads: "No statement 'Rbar small gives decay of all observables' is on record."

Row 1115 moved the effort to (L3). It gave (L3) the name (CONV): a hypothesis H(l) on pinned cells, stated in the law of the model, that gives exponential clustering of all local observables at rate c/l.

### 1.4 Read for this row

Read in full: `library/gap-sing-direction-fable.md` (409 lines); `library/gap-conv-in-law-astra.md` (354 lines); `library/gap-conv-in-law-check-opus.md` (222 lines); `library/gap-resp-in-law-sheet.md` (309 lines); `library/gap-resp-in-law-sheet-check-opus.md` L389-725 (steps 3.14 to 3.18, 4, 5 and 6); `library/gap-ds-gauge.md` (all 219 lines; the brief asked for L1-140); `library/gap-short-step-max.md` L70-137 (sections 2.1 to 2.4) and L271-361 (sections 4.5 and 5.1 to 5.6); `parts/gap.md` L1-112, the entries of rows 1115 to 1121 (L173-177), the requests, the route registry, the test table and the exact price (L178-288).

Read at the lines named, because steps 3 to 6 use them: `library/gap-mid-max.md` L252-274 (Lemma M, Proposition MIX) and L80-90 (candidate C-E), with the grep hits for Theorem DOB, Lemma INF and Proposition Delta; `library/gap-ac-lat.md` L93-126 (the three failures of (FS), Lemma C, Proposition D); `library/gap-pinned-cell-gauge-max.md` L476-502 ((N1) to (N3)); `library/gap-br2-direction-fable.md` L176-180 ((P-GAP), (D-SUB), the carry); FINISH rows 690 to 712 in their first 700 characters. `parts/gap.md` L113-172 was read with each line cut at 900 to 1300 characters.

Not read: `library/gap-resp-in-law-sheet-check-opus.md` L1-388; rows 978 to 988 (route RF); row 731; rows 1011, 1013, 1072 beyond their `parts/gap.md` entries; `library/gap-ds-gauge-check.md`; any paper. No run was made.

Status: step 1 done. Step 2 next.

## Step 2 result, task (1): what rows 1115 to 1121 established about (L3)

Everything in this step is a reading of the six files and of their `parts/gap.md` entries. Who proved and who checked is said in each line.

### 2.1 The hypothesis forms and what became of each

| Form | In short | What became of it | Source |
|---|---|---|---|
| (H-sup), full supremum over pins | every pin, one cell | Classical in shape. Out of reach in the 4D pin class (Proposition B', Theorem D2, Lemma SHEET bind forms near it). A supremum over a set of pins of full measure is the full supremum: no escape. | row 1115 3.4; row 1118 5.2; check 1121 step 7: HOLDS |
| (H-ent-local), one pin replaced, fixed core, mean square in law | a response at one sampled ring | **Refuted as a criterion.** It holds in every bounded regular Gibbs law, mixtures included (reverse-martingale lemma (3.6), with its derivative form (3.7)). The coexistence mixture of van Enter and Shlosman satisfies it and does not cluster. | row 1118 3.2, proved by gpt-6-astra; check 1121 step 4: HOLDS |
| (H-ent) as Rbar, the scale-normalised growing-face form of row 1018 | a response at one sampled ring, summed over two faces | **Open after row 1118.** Row 1115 said that the first-order model refutes it. That claim is unsupported: it needs decay inside each phase at a rate that beats the count of pairs. | row 1118 L132; check 1121 step 4 |
| (H-two), two independent rings, total variation of the core laws | a comparison of two samples | **One-scale mixing in disguise.** It equals the core-ring mixing coefficient within a factor 2 (Lemma TS). It bounds every core-outside covariance (Lemma TS2). The converse holds (Lemma TS3). It is not circular as a hypothesis for (CONV): it gives no decay. No proof of (CONV-two) from it exists. | row 1119 4.1, proved by Claude Fable 5.2; check 1120 3.15, 5.2: HOLDS; TS3 proved by the check, no second reader |
| Weaker two-sample forms | a smaller test class, or no small constant | **Each is one-scale mixing of the class it tests** (TS3), or it fails a test. Charged observables only: no hypothesis for the sheet. Local neutral observables only: holds for compact U(1) at large coupling. An overlap form with no small constant: holds for the massless Gaussian sheet. | check 1120 5.3, argued |
| (H-two-N1), one bounded neutral core observable at a time | the weakest two-sample form that passes the tests | Still one-scale singlet mixing. Whether (CONV) follows from it is open. | check 1120 5.3, argued |
| (H-swap), a joint tail of the swap defect of two independent rings | a free-energy difference under recombined rings | **Sufficient, and false at the window.** Theorem CONV-swap is a proved conditional implication. Proposition J: one cell violates the hypothesis at beta or b in [2.3, 2.6] for every l. E p_c is at least 0.010 in 4D and 0.050 for the sheet, against the thresholds 1/1250 and 1/50. Lemma JI: no other localized ownership helps. A smoothed exchange is not an exact symmetry. The hypothesis holds at strong coupling only (argued). | row 1118 4.2 to 4.4, proved by gpt-6-astra; check 1121 steps 6 and 8: HOLDS; Proposition J and Lemma JI proved by the check, no second reader |
| (H-two-col), two rings drawn given the same outside of a collar, for every outside | a property of the specification | **Open.** It is one-scale weak mixing with a supremum over the far boundary only. No consumer is written for it. Its bad events are not local. Nobody has tested it against Proposition B', Theorem D2 or Lemma SHEET. | check 1120 5.3, argued |
| (DS-W), the hypothesis of row 691's Theorem W | one changed boundary link of a cube changes few links, all boundary values, sum normalised by the volume | **Open at the window.** The implication is proved (row 691, checked by row 693). Proposition J's mechanism does not exclude the hypothesis. Nothing on file bears on it above the one-link Dobrushin range. | row 691; check 1121 8.5 |

### 2.2 The supplier side (row 1119, checked by row 1120)

- Row 1119 asked the supplier question in the one model with a posted engine, the zero-field O(4) sheet. It stopped by the third rule. Check 1120: stop VALID.
- The engine drives two things. In the ring law it drives the response of a whole face to a smooth rotation of the opposite face (Lemma LOW; the bound does not decay with l). For all pins it closes the charged channel (Lemma DEEP).
- The engine does not drive the entries of K_c, and it does not drive the two-sample distance. Both sit in the neutral channel, once the ring has fixed the frame.
- Lemma GB: no group-blind repair of the rough-profile way exists. The Gaussian sheet has Rbar bounded below at every l.
- (N-CH), the "next statement" of row 1119, is form (i) itself (Lemma CH; check 1120 3.17). The row isolated no smaller statement.

### 2.3 In plain words

1. A hypothesis that looks at one sampled ring and asks how the cell responds there cannot give mixing in its local form. Every Gibbs law passes that test, a mixture of two phases included.
2. A hypothesis that compares two sampled rings can give mixing. But with a small constant it is already mixing at one scale, for the class of observables that it tests.
3. A hypothesis that swaps pieces of two sampled rings is sufficient. At the window it is false. Two independent samples carry independent gauge frames. So the plaquettes at the junction are Haar-random, and each junction costs a fixed amount.
4. The engine of Ward type, where it exists, gives collective and charged gains. It does not give the neutral statement that every form in 1 to 3 needs.

So after rows 1115 to 1121 clause (L3) has no hypothesis that is both weaker than mixing and sufficient. Three forms stay open by name: the Rbar form, (H-two-col), and (DS-W). Step 3 treats the first two. Step 4 treats the third.

Status: step 2 done. Step 3 next.

## Step 3 result, task (2): can (T-pin) have a consumer whose supplier is weaker than one-scale singlet mixing?

**Answer: no. This is an argued obstruction with the scope of 3.7. It is not a closure.** A consumer can buy scales: from one scale to all scales. It cannot buy the passage from a response to mixing. Every statement in this step is argued by hand in this file. Nobody has checked it.

### 3.1 The question made exact

A consumer is an implication "Hyp(l) gives Concl". Two conclusions are on file.
- (C-seed): the seed of Theorem S, or (W). This is clause (L3) as row 1018 wrote it.
- (C-clus): exponential clustering of all local observables at rate c/l. Its uniform form is the bound (4.6) of row 1118, or (C) of row 691's Theorem W: the constant is a number times the size of the smaller support times the two sup norms. Its weak form is T_JW-lat: a total set, one constant per pair of observables.

A hypothesis in the sense of rows 1115 to 1121 is of one of three kinds.
- (K-aff) A one-sample mean in the state: E_mu[Phi_c] at most r, with Phi_c a fixed bounded function of the ring of the cell c. Rbar(l)^2 = E_mu[R_c^2] is of this kind. So is (H-ent-local).
- (K-quad) A two-sample mean: E over two independent rings of a distance between the two cell laws, or of a swap defect. (H-two), (H-two-N1) and (H-swap) are of this kind.
- (K-spec) A property of the specification with a supremum over boundary values: all of them ((H-sup), (DS-W), FST-BD of row 1091) or the far ones only ((H-two-col)).

### 3.2 Lemma AFF: a one-sample mean cannot be sufficient unless it forces uniqueness (argued)

**Statement.** Let gamma be a specification and G(gamma) the set of its Gibbs states. Let Phi_c be bounded measurable functions, one for each cell. Put Hyp_r = {mu in G(gamma) : E_mu[Phi_c] at most r for every c}. Then Hyp_r is convex. If Hyp_r holds two different states, their midpoint lies in Hyp_r and does not satisfy the uniform form of (C-clus). So "Hyp_r gives (C-clus)" is true on G(gamma) only if Hyp_r has at most one point.

**Proof.** E_mu[Phi_c] is affine in mu, so each constraint cuts out a convex set. A state with the uniform bound is tail-trivial, hence extremal in G(gamma) (check 1121, step 7). The midpoint of two different Gibbs states is a Gibbs state and is not extremal. QED

**Reading.** A hypothesis of kind (K-aff) is blind to the difference between a pure state and a mixture, by its form. Lemma (3.6) of row 1118 showed this for (H-ent-local) by analysis. Lemma AFF shows it for every one-sample mean by convexity, with no estimate. The price: Lemma AFF needs two states that both satisfy the hypothesis.

Where two such states are on file.
- **A discrete factor at a first-order point** (argued; the literature input is recalled, not opened). Take the gauge group SU(2) x H with H finite and a product weight. Let the SU(2) factor be Wilson at beta_1 below 1/18. Let the H factor have two Gibbs states that differ on a local observable. The Neumann data are derivatives along su(2). So K_c of the product is K_c of the SU(2) factor, and Rbar does not see H. At beta_1 below 1/18 the pinned cells of the SU(2) factor have covariances that decay like alpha^distance for every pin, alpha = 18 beta_1 (Dobrushin's estimate; Lemmas DC and INF of row 708 hold its comparison form; the covariance form is recalled). So Rbar(l) tends to 0 in both states. By Lemma AFF the Rbar consumer for (C-clus) is false in this class.
- **The weight w_p at its transition coupling** (Proposition V; the lane's theorem given van Enter and Shlosman). Two Gibbs states, one connected group. Whether both have small Rbar is a belief. If they do, Lemma AFF applies inside the class of positive-character weights on SU(2).

### 3.3 Example PROD: the Rbar consumer for (C-seed) is false on the engine's class (argued, given two lane theorems)

- **The model.** Gauge group SU(2) x Z_2, product weight: Wilson SU(2) at beta_1 below 1/18, frozen Z_2 at beta_2 above 2.191. The engine's class holds products (the device of row 708, Lemma PT).
- **Rbar is small.** As in 3.2: Rbar reads the SU(2) factor only, and tends to 0.
- **No seed at any size.** On a periodic box the partition function is a product. So 1 + S = (1 + S_1)(1 + S_2), and S is at least S_2. Frozen Z_2 above 2.191 has no periodic seed (the lane's theorem by a Peierls bound; test table, row "Frozen Z_2").
- **So** "Rbar(l) at most r_0 for one l gives the seed" fails here, for every r_0 above 0.

This is the pattern of lead rule W2: a tool that reads one factor of the state space is bound by a product with a no-seed factor. Row 1018 tested (T-pin) against a massless factor, which keeps Rbar up. A frozen factor does not. Its own table says of Q_8 and 2T: "not defined: K_c is a second derivative". That is the opening that PROD uses.

What PROD forces. A consumer for (C-seed) must read the whole fibre, the discrete part included. For SU(2) alone the discrete part is the centre. So an Rbar consumer for (W) must carry a flux clause that no second derivative supplies. This is the distance between T_JW-lat and (W) that check 1055 records.

### 3.4 Lemma BACK: the uniform conclusion gives one-scale singlet mixing back (argued)

**Statement.** Let mu satisfy the uniform form of (C-clus) at rate c/l with constant C. Let c' be a cell of side l', with core at depth l'/3 and ring of at most 32 l'^3 links (4D, l' at least 7). Then for every bounded function F of the core,
  alpha_F = E_mu abs(m_Omega(F) - mbar(F)) is at most 32 C l'^3 exp(-c l'/(3 l)) norm(F).
So (H-two-N1)(l', eta) holds with eta = 64 C l'^3 exp(-c l'/(3 l)). It is small for l' at least C' l log l.

**Proof.** By Lemma TS3 (a), alpha_F is the supremum of abs(Cov_mu(F, G)) over functions G of the ring with norm at most 1. The ring is a finite support. Apply the uniform bound with the ring as the smaller support and the distance l'/3. Lemma TS3 (b) gives the two-sample form. QED

**Reading.** Every hypothesis that is sufficient for the uniform conclusion implies (H-two-N1) at a scale larger by a logarithm. So no sufficient hypothesis is weaker than one-scale singlet mixing. For (C-seed) the same holds in a shorter form: the seed is itself a one-scale number, and Theorem S returns it at every larger size.

### 3.5 The decision

Put 3.2 to 3.4 beside Lemma TS3 and Proposition J. ("Lemma BACK" is a new name; the lane already holds a "Lemma NEC" in other files, which is a different statement.)

1. **(K-aff) alone is not a consumer hypothesis.** It needs a companion that excludes coexistence and reads the whole state space (AFF, PROD). The companion is not a one-sample mean. So the Rbar form of (H-ent) leaves the open list as a criterion on a class. For Wilson SU(2) alone it stays open only in this form: Rbar small together with a uniqueness clause that fails for w_p at its transition coupling. That clause is the kind of input that the test table asks of (K-one): a number in the weight.
2. **(K-quad) with a small constant is one-scale mixing of the class it tests** (TS3). To pass the U(1) test and the coexistence test the class must hold the bounded neutral observables (check 1120 5.3). So the hypothesis is at least (H-two-N1). The swap form is stronger and is false at the window (Proposition J).
3. **(K-spec) is stronger than mixing in one state.** It bounds all boundary values. (DS-W) gives (H-two-col) at a scale C R log R, through part (A) of Theorem W (argued, one line: (A) bounds the total variation distance of the core laws for every pair of rings). Row 691 section 6: no converse from a gap in one state is known.
4. **So every consumer for (T-pin) needs a supplier that contains one-scale singlet mixing**, in law or uniformly in the boundary, at a scale above the correlation length. The supplier is not weaker than the one-scale content of C_beta.

**Is that supplier equivalent to (CAS) or (W) at one scale?** In kind yes, in strength it depends on the conclusion.
- For the conclusion (W): the supplier must carry the flux clause (PROD). With it, the one-scale statement on a periodic box is the seed, and the seed is (W) at one cutoff. Theorem S is its proved consumer.
- For the conclusion T_JW-lat: the supplier is at least (H-two-N1). No implication from one-scale mixing in law to the seed is on file: the flux clause is missing, and (CONV-two) is open.
- (CAS) is a way to reach the seed in steps. No consumer needs it.

### 3.6 What this means for the pinned form against the periodic form (T-per)

- **(T-pin) carries the wrong kind of variable.** Its merit was the mechanism slot, Lemma CHAIN. Its end product, "Rbar small", is a one-sample mean. By 3.5 it cannot hand over to any conclusion without a mixing input of full strength.
- **(T-per) carries the right kind of variable and has no slot.** D(a) and Phi(a) are free-energy differences. They are not affine in the state. D(a) small is the seed (Proposition Delta of row 708). The consumer is proved.
- **Why the periodic difference survives where the pinned one does not** (argued). The non-affine variables on file are free-energy cross-differences: Phi(a) = 16 F(a^4) - F((2a)^4) on periodic boxes, and D_c of (H-swap) on pinned cells. Proposition J removes D_c at the window, because recombined pins have Haar-random junction plaquettes. A torus is glued to itself. Its frames are integrated, not pinned. So the periodic difference has no junction cost.
- **Remark RHO: the in-law quantity that composes** (argued; standard Hilbert-space facts). Let rho(A, w) be the maximal correlation coefficient, in mu, between the links of a closed cube A and the links outside the interior of its w-neighbourhood A^(+w). Suppose rho(A, w) is at most theta below 1 for every cube A of a nested family A^(+jw). Then for f measurable in A and g measurable outside the interior of A^(+kw): abs(Cov(f, g)) is at most theta^k times the two L2 norms. Proof: let Y_j be the ring of A^(+jw); by the Markov property E[f given the outside of A^(+jw)] = E[f given Y_j] =: f_j, and f_(j+1) = E[f_j given Y_(j+1)]; f_j is measurable in the closed cube A^(+jw); so the L2 norm of f_(j+1) is at most theta times that of f_j. QED
  - This form has all four clauses with no pins and no supremum: the blind half is the product rule, the consumer is the display above. Its whole content is one number theta below 1, uniform in the side of the cube. For a massless Gaussian field rho tends to 1 as the side grows at fixed w (argued). A coexistence mixture has supremum 1.
  - For half-spaces of a reflection-positive state, rho at distance w is exp(-w times the gap). So the pinned form, once its variable both composes and consumes, is the spectral form of the target. It is the Poincare member of the family of route RF. **It is not new to the lane** (found after this step was written; see 5.1): Lemma MC of row 895 is the slab case, and row 1004 judged the radial frame (its idea I2: FAILS, no reflection through a sphere on the lattice). I did not read rows 978 to 988.
- **Verdict.** The pinned form does not replace the periodic form as the consumer of the gap path. (T-pin) keeps a place only as an engine whose output is a mixing coefficient. With Rbar as output, a proof of (FL) and (DEC) would change nothing downstream.

### 3.7 Scope and limits of the obstruction

- Lemma AFF binds a consumer that is claimed for all Gibbs states of a specification, or for a class that holds a specification with two states in the hypothesis. It does not bind a consumer whose proof first establishes uniqueness by other means.
- PROD uses product groups. Its inputs: the lane's theorem for frozen Z_2 above 2.191; Dobrushin's covariance estimate at beta_1 below 1/18 (recalled in covariance form; Theorem DOB of row 708 holds the comparison form).
- Lemma BACK needs the uniform form of the conclusion. For T_JW-lat it gives only a bound for each fixed pair of local observables.
- "Both phases of w_p have small Rbar" is a belief. So inside the class of one connected group the refutation of the Rbar consumer is at belief grade. In the class with product groups it is argued from theorems.
- The obstruction says nothing against mixing. It says nothing against an engine. It says where the engine's output must live.
- (H-two-col) and (DS-W) are not touched as hypotheses. (DS-W) has a proved consumer. (H-two-col) has none on file.

Status: step 3 done. Step 4 next.

## Step 4 result, task (3): Theorem W of row 691 at the window couplings

Everything in 4.2 to 4.6 is argued by hand in this file, with no second reader, except where a source is named.

### 4.1 The hypothesis and the theorem, restated (reading: `library/gap-ds-gauge.md` sections 3, 4 and 6)

- **The cube.** V_R holds the links with both ends in {0, ..., R}^4. It has N_R = R (R+1)^3 links in each direction. Its boundary holds the links outside V_R that share a plaquette with a link of V_R. The kernel gamma_V( . given tau) holds the plaquettes that meet V only.
- **(DS-W) at (R, delta).** There are numbers k_z at least 0, one for each boundary link z, with: for each direction the sum of the k_z is at most delta N_R; and for every pair of boundary values that differ at z only, the two laws of the cube have a coupling with at most k_z different links in mean.
- **In words.** Change one boundary link by any amount, for any values of the other boundary links. Then the cube changes, in mean, in at most k_z links. The k_z need not be small. Their sum must be below the volume. So a boundary link may move about delta R/7 links of the cube (4.2).
- **Theorem W** (proved by Claude Fable 5.2 medium; checked line by line by Claude Opus 5.5 high, row 693). (DS-W) with delta below 1 gives: (A) weak mixing for every finite set of links, uniform in the boundary values, at rate eps = ln(1/delta)/(2(R+2)); (B) one Gibbs state on Z^4; (C) a covariance bound for all bounded local functions on Z^4 and on every torus with sides at least R + 4, with constants that do not depend on the torus; (D') the same for every action that a flip makes equal to Wilson's in each cube, the twisted actions included. The proof does not use the group.
- **Proposition B of row 691.** (DS-W) at (R, delta) forces R + 2 at least (1/2) ln(1/delta) times the correlation length. **Proposition S.** Exponential decay of the influence of one boundary link, uniform in the boundary values, for cubes, gives (DS-W) at large R.
- **Status on file.** "Whether (W) holds for Wilson's SU(2) at any beta beyond the single-link Dobrushin regime. Nothing here bears on it." Row 691's named next statement, (D-to-W), was not run: row 697 moved the crux to a new statement the same day (my reading of FINISH rows 692 to 712 at their first 700 characters).

### 4.2 A reduction: the hypothesis is one number (argued)

The boundary links are of two kinds. A **normal link** joins a site of the box to a site outside. A **layer link** joins two sites outside and is parallel to a face.

**Lemma GM (a normal link at the inside of a face is a gauge move).** Let x be a site of the box with exactly one coordinate at an end value. Its eight links are seven links of V and one normal link z. A gauge transformation h at x leaves every plaquette term unchanged. It changes tau at z only. So gamma_V( . given tau^h) is the image of gamma_V( . given tau) under the action of h on the seven links. Every tau' that equals tau off z is some tau^h. The pair (sigma, h sigma) is a coupling with at most 7 different links. **So k_z at most 7, at every coupling and every R.**

**Lemma TILT (every other boundary link is a bounded tilt of few links).** A layer link lies in exactly one plaquette that meets V. That plaquette holds exactly one link of V. So the two laws differ by a density that depends on one link of the cube, with logarithm between -2 beta and 2 beta. A normal link at an edge or corner of the box changes the staples of at most 6 links of the cube. Couple those m links first, at most 6 of them. Where they agree, the rest of the cube has the same conditional law in both copies. So k_z is at most t (m + I). Here t below 1 is the total variation distance of the two laws of the m links. I is the mean number of links of the cube that must change when m links next to the wall are pinned to other values.

**The count.** In each direction there are 2 (R+1)^3 normal links, of which 2 (R-1)^3 are of the kind of Lemma GM, and 6 R (R+1)^2 layer links. Let K be the supremum of k_z over the other boundary links and over all boundary values. Then the sum in one direction is at most (R+1)^3 (14 + 6 K (1 + 1/R)). So

  **(DS-W) holds at (R, delta) for every R at least max(6, (14 + 7 K)/delta).**

K may also grow with R, as long as K(R) stays below delta R/7 less a constant.

**First lemma for a proof row, (INF-L).** For Wilson SU(2) at beta in [2.3, 2.6]: K is finite, uniformly in R and in the boundary values. In words: pin one link next to the wall of a cube to another value; then the cube changes in a bounded number of links, whatever the wall holds. Its first case is the cold wall, tau equal to the identity.

### 4.3 Proposition J's mechanism as a test

Proposition J's mechanism: two independent samples carry independent Haar frames; a plaquette with links from both has a Haar-random holonomy; so a recombination of two rings costs about beta per junction plaquette, and the cost has no core term to cancel it.

- **(J1) Against the hypothesis: no refutation.** A change of frame at one boundary site costs at most 7 links (Lemma GM). It does not grow with R. The kernel of a cube holds no plaquette that lies in the boundary alone, so (DS-W) has no ring-only cost. The budget allows about delta R/7 links per boundary link. This agrees with check 1121, 8.5, and gives its reason in one line.
- **(J2) Inside the supremum: a test family.** Fix the normal links to the identity by gauge moves at the outside sites. Then a boundary value is a field W on the links of the faces, and each face link U feels the term (beta/2) tr(U W^(-1)). The supremum runs over every W. It holds the cold wall (W the identity), the hot wall (W Haar-random at each link), and the hybrids of two independent samples, whose seam carries Haar-random plaquettes of W. (INF-L) must hold at each of them. A proof that treats only walls with plaquettes near the typical value is not a proof of (DS-W).
- **(J3) Against a weakening in law: an obstruction.** Lemma 1 of row 691 changes the boundary of a cube one link at a time, from one coupled copy to the other. The intermediate boundary values are hybrids of the two copies. A hybrid is a recombination in the sense of Proposition J. Its plaquettes across the set of disagreement are not typical, and its law has no bounded density against the law of the model that is uniform in the size of that set. So the supremum in (DS-W) is what pays for the hybrids. A form of (DS-W) that asks the bound for typical boundary values only does not run through the proof of row 691. This matches row 1116: every published criterion with averaging "still takes a local worst case over boundary values before averaging". Scope: the proof scheme of row 691; not a theorem that no in-law cube criterion exists.

So the test separates the three forms cleanly. (H-swap) recombines and pays per junction: false at the window. (DS-W) takes the supremum and pays nothing for frames: not excluded. Any form between them meets the hybrids.

### 4.4 The nearest models where (DS-W) is false

| Model | Why (DS-W) fails | Grade | What a proof must use |
|---|---|---|---|
| Frozen Z_2 above 2.191 | Part (C) gives a gap at least eps on every periodic cube with sides at least R + 4, flux sectors included (argued from (C)). There the flux sectors stay degenerate. So (DS-W) fails at every (R, delta). In boundary words (row 691 section 6, heuristic): a boundary value with frustrated plaquettes forces a vortex sheet through the cube. I add (argued): a boundary curve with two spanning sheets of nearly equal area makes one link flip a region of order R^3 links. | the degeneracy is the lane's theorem as row 1018 5.3 and the test table record it; I did not open its proof | the centre: forced centre flux must dissolve within a fixed length, for every boundary pattern |
| Compact U(1), Coulomb phase; a product with a massless factor | Proposition B of row 691: with no gap, (DS-W) fails at every R. | theorem at very large coupling; belief at order one | the non-abelian structure; the whole state space |
| The weight w_p at its transition coupling | Two Gibbs states, against part (B). | the lane's Proposition V, given van Enter and Shlosman | a number in the weight |
| A positive specification with a surface transition | A unique, massive bulk state. For one family of boundary fields, two states of the face layer have free energies that cross. At the crossing one link shifts their weights by a factor of order one. Then k_z is of order R^3 for the links of that face, and the sum is of order R^6 against delta R^4. | recalled (Shlosman's examples; "weak mixing does not give strong mixing for cubes above two dimensions"); not opened; the mechanism is argued | all boundary fields |

The first three rows are the test profile of the periodic seed at one coupling. The fourth row is new to this file. It is a way to fail that the periodic form does not have: (DS-W) can be false in a model where C_beta and the seed are true. For Wilson SU(2) at the window I know no boundary field W that orders a face. I know no argument that excludes one.

### 4.5 Where a proof could die

1. **At the supremum** (4.4, row four). A surface transition under one family of boundary fields refutes (DS-W) at every R. Nothing in the bulk excludes it.
2. **At the centre** (4.4, row one). The flux half of the problem enters in supremum form.
3. **At the number.** (INF-L) at the cold wall is one-scale mixing next to a wall at a coupling of order one. The tools on file are Dobrushin's condition (alpha at most 18 beta, range 1/18, or about 1/10 with the sharper one-link bound that row 708 names), disagreement percolation, and curvature criteria. Each reads only the size of the plaquette term, or works at strong coupling. Compact U(1) with a plaquette term of the same size is in its Coulomb phase (belief; the transition near 1.01 is from numerics, recalled). So a group-blind verification at 2.3 is excluded at belief grade. Theorem W's proof does not use the group. A proof of its hypothesis must.
4. **At the size.** R is at least (14 + 7 K)/delta, and K is at least the number of links that one link moves. So the cube has a side of some hundreds of lattice units at the window (guide; an order of magnitude from a length near 1). The condition is a finite one in name only: no hand computation reaches it, and the owner's rule excludes a computer check as a proof step.
5. **At the cutoff.** (DS-W) counts links. It is a statement at one cutoff. The proved sufficient size (Proposition S) grows like the fourth power of the correlation length. So it is not a form of (W) at one physical size along the trajectory (argued).

### 4.6 What closing it would change

- **At one beta of the window.** One Gibbs state. C_beta with the explicit rate ln(1/delta)/(2(R+2)), for all bounded local functions. The same on every torus with sides at least R + 4 and for the twisted actions. That is (P-GAP) with flux sectors, the first step that row 1108 found missing between C_beta and (SEED).
- **On the interval (0, beta] with one pair (R, delta).** The fixed-coupling seed (SEED) at beta (argued). The chain: the two laws of Proposition MIX of row 708 are mixtures of the kernels of one set of links, so part (A) bounds eps(a) by a constant times R times the size of the box times exp(-eps (a/2 - R - 3)); Proposition MIX gives Phi; Theorem SH gives the gap of every larger cube, from a side of order R log R. A proof row must write this chain; I did not check its constants.
- **For (W).** (SEED) at the window, on record as sufficient together with the carry. The carry stays open.
- **Against BR-2.** BR-2 fully proved stops at C_beta. (DS-W) on the interval reaches (SEED).
- **Not changed.** The carry. T_JW-lat along the trajectory. (BDD-Delta).

### 4.7 Verdict on Theorem W at the window

- It is not excluded. Proposition J's mechanism does not touch it (J1).
- It is stronger than the fixed-coupling seed: it adds a supremum over boundary fields, and with it a way to be false that the target does not have (4.5, point 1).
- It is route RC, "a hand bound in the band", in supremum form. Its first lemma (INF-L) has no tool that reads the group.
- Lemmas GM and TILT make the hypothesis one number K. That is a gain in statement, not in proof.

Status: step 4 done. Step 5 next.

## Step 5 result, task (4): the other open entries for the selective half of (W)

### 5.1 Prior work found late, and what it changes in steps 3 and 4 (reading)

I checked the lane for my own label names before this step. The search found that the question of rows 1115 to 1121 is older than those rows.

**What is on file** (read now: the FINISH entries of rows 845, 852, 853, 895, 896; `library/gap-glue-max.md` L218-246; `library/gap-glue-check-astra.md` L268-280; `library/gap-brainstorm-max.md` L246-262; `library/gap-squeeze-opus.md` L90-106; one table line of `library/gap-outside-box-max.md`).
- **Row 845, Theorem AG** (Claude Opus 5.5 max; checked line by line by gpt-6-astra xhigh, row 852, cross-provider). A conversion theorem for 4D Wilson SU(2): an annealed condition (AN) on block response fields along the stationary block heat-bath chain gives a block gap and exponential clustering, uniform in the torus and the flux sectors, "with no independence and no uniformity over exteriors". Check 852: the implication HOLDS, "but literal (AN1) is equivalent to an essential worst-case exterior bound"; a pure-exterior space-time Peierls bound (SP-ext) FAILS under repeated block updates; "Open repair: conditions only on surviving path sums, which still lack a model-specific supplier."
- **Row 895** (Claude Fable 5.2 max; check 896 by gpt-6-astra xhigh). Proposition FIB: an L2-averaged condition on a finite block is the worst case over exteriors. Lemma MC: the maximal correlation of two slabs at distance w is exactly r_1^w, so an averaged slab condition is the claim itself. Check 896: both hold (FIB after correction), and the sentence "every averaged condition is either the worst case or the claim itself" is **not proved**. Three forms stay outside: "An averaged scalar estimate, a weighted estimate with a bad-set term, or an estimate only for exterior-independent tests".
- **Row 859, the walls** (Claude Fable 5.2 max; check 882). WALL A, the worst-case ladder: single-link Dobrushin to 2/9, star blocks to 0.3609, every vertex block below 0.775, every background-uniform layer bound below 1.0109, because "the worst background is the flat one, where the conditional model is a ferromagnet at its critical coupling". WALL B: "typical is not better link by link" (guide: single-link influence row sums 2 to 4 at order one; gauge-invariant 2^4 block responses 0.7 at beta 1 and 2.5 at beta 2).
- **Row 1004**, idea I2: the exterior of a block in a radial frame FAILS.
- **Row 731**: the limit half of the engine reads the even sector only (Theorem EV-L); the doubling step needs the flux sectors (Remark 2.A); (EV-STEP) is open.

**None of this is cited in rows 1115 to 1121.** Grep for "row 845", "gap-annealed", "(AN1)", "Proposition FIB", "row 895", "row 836", "row 821" gives 0 hits in the five files of rows 1115 and 1118 to 1121, in the reading file of row 1116, and in `parts/gap.md`. I am the writer of row 1115. I did not find these rows then.

**What it changes.**
1. **The (L3) excursion repeated the annealed excursion of rows 821 to 853 in a pinned setting.** Its outcome agrees with the older one. Rows 1118 to 1121 walked two of the three forms that check 896 left outside: an averaged scalar estimate ((H-ent-local), Rbar, (H-two)) and a weighted estimate with a bad-set term ((H-swap) with its joint tail).
2. **Step 3 of this file adds a third branch to the lane's sentence** (argued). An averaged one-scale condition is the worst case in disguise (FIB; (AN1); a supremum over a set of full measure), or the claim at one scale (Lemma MC; Lemma TS3), **or not sufficient** (a one-sample mean: Lemma AFF, Example PROD). The weighted form with a bad-set term fails where it was tried: (SP-ext) under repeated updates, and (H-swap) at the window by Proposition J. This is still not a theorem that no other form exists.
3. **Remark RHO is withdrawn as a remark of this row.** It is Lemma MC in another geometry, and row 1004 judged that geometry. The edit is in 3.6.
4. **For step 4.** WALL A binds every verification of (DS-W) by small blocks or by layers. It does not bind the cube form at large R: a layer model has two frozen slices, a cube has one frozen shell. So (INF-L) is the one worst-case form on file that WALL A does not reach. It has no tool. WALL B's guide numbers say why the cube must be large.
5. **For route RE.** A criterion in law for local observables is blind to the centre (Lemma LOC of row 895). So such criteria are candidates for the even step. The ones on file are Theorem AG (worst case in disguise), CONV-swap (false at the window) and Theorem W (a supremum). None is weaker than its conclusion at one scale.

### 5.2 Base cases and steps (reading: row 1108; `library/gap-br2-direction-fable.md` L176-180)

- A supplier at one cutoff, at a coupling of the window, moves C_beta and (SEED). To reach (W) it needs the carry. Row 1108 on the carry: it "gives the gap of all cubes at every coupling", so it is "the wall again".
- So every entry of the (K-one) kind at the window is a base case of an induction whose step is the open selective inequality. This holds for BR-2, for route RC and for (DS-W).
- An entry moves (W) only if it is uniform in the cutoff at one physical size. That is the (K-flow) kind, or (K-one) for the family of first-passage actions (the statement (SEED-FP) of row 859).

### 5.3 The entries side by side (argued, from the sources named)

| Entry | Kind | First lemma | Where a proof dies first | What closure would change | Binding tests |
|---|---|---|---|---|---|
| (FL), (DEC), the selective pair of (T-pin) (row 1018 5.5) | (K-flow) | none: the non-abelian content NA_l has no definition at the cell scale; "no exact identity" for (DEC) | before it starts. And by 3.5 its output, Rbar small, has no consumer. Row 1119 adds: where the engine is posted, a gain of Ward type does not drive the entries. | nothing downstream, until the output is a mixing coefficient | adjoint Higgs (FL false at the cell scale); frozen slices and five dimensions (DEC false as written); PROD (this file) |
| (N1) to (N3), a frame on typical rings (row 1011 7.4) | (K-flow), above the band | (N1) | at (N1): a Jacobian inequality that nobody has; the mean sign fails for the transported frame (Corollary RM-TREE, row 1051) | a prerequisite; by its own reading it "does not cross the band by itself" | Remark HOPF (no frame on all pins) |
| Route RC, a hand bound in the band; in periodic form the seed, or eps(a) of Proposition MIX, or (BOOT_eps) of row 708 | (K-one) | the thermal sum of one cube at a coupling of order one; in the words of row 708, "the plaquette at mid-height does not feel the rules at the cut" | at its first line: no object on file reads the group at order one. WALL A caps the worst-case tools. Check 852 and WALL B cap the averaged ones. | (SEED) at one coupling; a base case (5.2) | Proposition V with p named; compact U(1) at the same size of the plaquette term; Q_8 and 2T |
| (DS-W), the hypothesis of Theorem W (row 691) | (K-one), supremum | (INF-L) of 4.2 | at the supremum (a surface transition; forced centre flux), then at the same number as route RC | (SEED) with one Gibbs state and the flux sectors; a base case (5.2) | the profile of the periodic seed, and all boundary fields (4.4) |
| (CAS), the form (T-per) (rows 708, 1018) | (K-flow) | none: "as a mechanism it is empty" | it has a proved consumer and no slot | (W), with the extensive base | compact U(1); a product with a massless factor; Proposition NP |
| (BDD-Delta) | blind half | bounded Casimir free energy on physical sizes | not at a selective step: it is true for compact U(1); its open inputs are start values of the account ((SV3), (UV-Cas), row 1058) | the price: (W) becomes (Z-UNB) alone | frozen Z_2 in the form (BL-c) (row 1051) |
| (SER), (SPR), the form (T-vor) (row 1018) | flux half | the series direction of a vortex container | at a number: "an energy-entropy balance with a threshold" | the flux half at one coupling, not the seed (row 1025) | frozen Z_2 has the same identities |
| (EV-STEP) (row 731) | even half | an even step | blocked-local; the in-law candidates are in 5.1, point 5 | the flux half leaves the path to T_JW-lat | - |
| (H-two-col) (check 1120) | one-scale weak mixing, far boundary uniform | a local bad event | no consumer is written; implied by (DS-W) | nothing until a consumer exists | not tested |

### 5.4 The comparison by the rule

The rule: go to the place where the proof could die first, not to the easiest input.

1. **Every entry for the selective half dies first at the same place.** It is an inequality at a coupling of order one that reads the group. No entry has a mechanism for it. Rows 1101 to 1121 added none, and this row adds none. Row 859 said it in one line: the weak side stops at first passage, and "every proved tool stops below Wilson beta 1.01".
2. **What rows 1118 to 1121 did change.** They closed the consumer side as a place to look. The proved consumers are the periodic one (Theorems S and SH, with ZD-c), the supremum one (Theorem W), and the worst-case one (Theorem AG). An in-law consumer whose hypothesis is weaker than one-scale mixing is not on file, and step 3 argues that it cannot be.
3. **Ranking of the entries above.**
   - First: the selective step in a cutoff-uniform form, (CAS) or its engine. It is where a proof of (W) dies. It has a consumer and no first lemma.
   - Second: its base case at one coupling, route RC. A proof dies at the first line.
   - Third: (DS-W). It is route RC with a supremum. It can also die at the supremum, in a way that the target cannot. It is the form with the most ways to fail and the same lack of a tool.
   - Not first: (FL) and (DEC) (no object, and no consumer for the output); (N1) to (N3) (above the band); (BDD-Delta) (blind).
4. **Where the next proof effort on (W) goes.** Not to clause (L3): that question is answered at argued grade, twice now. Not to (DS-W) at the window. It goes to the selective step itself, with two conditions that this row can state: the carried variable is not a one-sample mean, and no step recombines two independent samples. I name no first lemma. Step 6 says what I would run with that.

Status: step 5 done. Step 6 next.

## Step 6 result, tasks (5) and (6): the next two rows, the row not to run, the registry

### 6.1 How the choice was made (argued)

- The excursion to clause (L3) is over. Its outcome is the lane's older lesson with one branch added (5.1). The lane paid for that lesson twice, because the second excursion did not find the first. So the first need is small: make the lesson one checked statement and one lead rule.
- Three statements carry the verdict "value: none at the window" and have no second reader: Proposition J and Lemma JI (proved by check 1121) and Lemma TS3 (proved by check 1120, same provider as the row it checked). The first row below gives them one.
- For the selective step no entry has a first lemma with a mechanism (5.4). By the rule, the effort goes to the half for which the lane names no tool at all. Row 895: "nothing at order one, no tool named for the glue half". The flux half has at least a proved blind half (Lemma PAR and Corollary MP of row 1018).
- Example PROD and Lemma LOC of row 895 say the same thing from two sides: responses of pinned cells, and every criterion in law for local observables, see the glue half only. So the engines of rows 1009 to 1121 were glue-half engines. Their output must then be the glue half's own variable, which is periodic and not a one-sample mean: the even thermal sum, or the even slab correlation r_1 of Lemma MC.

### 6.2 Recommended row 1: `gap-averaged-closure`

**Statements to prove by hand** (in the class of row 1118 4.2 unless said; each Lean-formalizable in principle; no computer-assisted step).
- (A1) Lemma AFF of 3.2.
- (A2) Example PROD of 3.3, with the covariance form of Dobrushin's estimate written for pinned cells at beta below 1/18, so that Rbar tends to 0 for all pins, and with the product formula for the thermal sum.
- (A3) Lemma BACK of 3.4, with constants.
- (A4) The class form for clustering: one model with two Gibbs states that both satisfy the Rbar hypothesis. Either a finite-group factor at a first-order point with a cited theorem, or both phases of w_p at its transition coupling. The row says which one it proves.
- (A5) For (DS-W): Lemmas GM and TILT and the count of 4.2; remark (J3) as a lemma with a number (the relative entropy of a hybrid against the ring law, per plaquette across the set of disagreement); the chain of 4.6 from (DS-W) on (0, beta] to (SEED), with constants; the frozen Z_2 row of 4.4 from the lane's theorem, opened.
- (A6) The sentence of 5.1, point 2, as one statement with its scope, set against Proposition FIB, Lemma MC, check 852 and the three forms of check 896. The row says which of the three forms it covers and which it does not.

**Stop rule.** Each of (A1) to (A6) proved; or a counterexample to one of them, with what then reopens for (T-pin); the third rule (one named step, three written ways) applies to (A4) only.

**Model tier.** The lane's hard-proof author tier, on the provider that did not write Proposition J, Lemma JI and Lemma TS3, so that the row is also their second reader. One check at the lane's check tier on the other provider. The settings file decides the model names.

**What it changes.**
- Proved: the registry lines of 6.5 rest on checked statements. (T-pin) is parked with a stated reopen condition. (DS-W) is one number K with a written chain to (SEED). A lead rule stops a third excursion.
- A counterexample to (A1), (A2) or (A4): the Rbar consumer is open again, and (FL), (DEC) regain a possible use.

**Literature reading row it needs** (reading tier; the lane first).
- In the lane, one question for each: is (A6) already proved in a stronger form? Rows 821, 836, 845 with check 852, 853, 859 with check 882, 895 with check 896, 1004 (idea I2), 731, 978 to 988.
- Outside, recalled by name, none opened in this row, each statement to be confirmed: Kotecky and Shlosman (first-order transitions in models with large entropy; for the finite-group factor of (A4)); Dobrushin's uniqueness theorem in covariance form, with Kunsch and Follmer (for (A2)); Dobrushin and Shlosman 1985, the constructive criterion (to set (DS-W) against the published hypothesis; row 1073 read their 1987 paper, as row 1076 records); Shlosman's examples of surface transitions and Martinelli and Olivieri on cubes (for row four of 4.4).

### 6.3 Recommended row 2: `gap-glue-engine-tree`

**Statement.** (GLUE-STEP): for the periodic boxes of the first-passage family of the account of Sussman and Alpoge, after Balaban, at one physical size: one doubling inequality for the glue half, in a periodic variable (the even thermal sum, or the even slab correlation r_1), with a gain that reads the group. Its target is row 895's (GLUE-FP). The deliverable is a proof tree from the Jaffe-Witten target down to named leaves. Each leaf is marked: proved in the lane (with its row), supplied by the account, or open. Then the row attacks the first open leaf.

**Conditions that the tree must pass before any leaf is attacked** (from this file and from the walls of row 859).
- The carried variable is not a one-sample mean of a cell response (Lemma AFF, Example PROD).
- No step recombines two independent samples of a ring (Proposition J, Lemma JI).
- No two-sample hypothesis is used as if it were weaker than mixing (Lemma TS3).
- No worst-case small-block or layer bound above 1.0109 (WALL A). No annealed condition that is a worst case in disguise (check 852).
- The step fails at a named line for compact U(1), for a product with a massless factor, and for w_p at its transition coupling with p named. Q_8 and 2T bind it, or the tree says why not.

**How to run it.** From the target, with the lane files closed until the comparison step. On the other provider's top tier: row 998 9.5 excludes another fresh-framing exercise by the model family that wrote it, and that family wrote this file.

**Stop rule.** The first open leaf proved (then the next leaf); or a counterexample to it; or the third rule. One clause is declared beforehand: if every leaf of the tree is on file as blocked, the row stops at once and reports the tree in one page as a found-again map.

**What it changes.**
- A leaf with a mechanism: route RA's reopen condition, "a mechanism that gives theta below 1 from the group", is met for the glue half, and the next proof rows have a first lemma.
- A fast stop: a cross-provider record that no tool for the glue half is known, at the cost of one row.

**My own doubt, stated.** Rows 859, 895, 975, 1013, 1031, 1032 and 1076 are earlier rows of this kind, and none named a tool. The new parts are the provider, the target-first order, the periodic variable and the five conditions. If the lead judges that this does not justify the cost, then my recommendation is to run no second proof row now. It is not to run (DS-W) or (DEC) in its place.

**Literature reading row it needs** (reading tier). In the lane: rows 731, 895, 896, 1052 to 1055, and the digests under `library/prior/`; the row reports only what is not there. Outside, recalled by name, none opened: Chatterjee (a probabilistic mechanism for confinement; scaling limits of Yang-Mills-Higgs models); Adhikari and Cao; Cao, Park and Sheffield (surface sums for lattice Yang-Mills); Shen, Zhu and Zhu (Langevin dynamics and curvature criteria for lattice Yang-Mills); Bauerschmidt, Bodineau and Dagallier (the Polchinski flow and multiscale curvature criteria); Chevyrev and Shen. The question for each: does it hold a step at a coupling of order one that reads a non-abelian group and bounds a thermal sum or a slab correlation?

### 6.4 Task (6): the row I would not run

**A proof row on the hypothesis of Theorem W at the window couplings, that is on (INF-L).** Reasons (argued; 4.4 to 4.7, 5.1 to 5.3).
1. It is stronger than the fixed-coupling seed. It adds a supremum over boundary fields, and with it a way to be false that the target does not have.
2. Its first lemma is one-scale mixing next to a wall at a coupling of order one. No tool on file reads the group there. WALL A caps every small-block and layer verification below 1.0109.
3. A cube of some hundreds of lattice units is needed (guide). No hand computation reaches it.
4. Closed, it gives (SEED) at one coupling. That is a base case. The carry is the wall again.
5. What is quick to gain from it is in row 1 already: the reduction to K and the chain to (SEED).
Reopen: a tool that reads the group for one-scale mixing next to a wall; or a published theorem that gives strong mixing for cubes from a bulk property, in four dimensions, for a continuous fibre.

Also not now, one line each.
- (N-CH), which is form (i) of (RESP-TR), and any row whose deliverable is "Rbar small in law", (DEC) included: by 3.5 the output has no consumer.
- (CONV-two) from mean total variation, or from (H-two-N1): the hypothesis is one-scale mixing, it has no supplier, and the periodic form has a proved consumer.
- An estimate of (H-swap) at the window: false there for every l (Proposition J).
- A form of (DS-W) in law through the proof of row 691: it meets the hybrids (J3).
- A second proof row on (P4-MIX) at kappa = b: row 1115's reason stands, and row 1119 ended in the branch that reopens nothing.

### 6.5 Registry changes that rows 1118 to 1121 require (for the lead; I edited no file but this one)

1. **`parts/gap.md`, entry of row 1115.** Its sentence "a single-pin hypothesis in law fails at a first-order point; a two-sample form does not" needs two notes: only (H-ent-local) is refuted (row 1118, check 1121); the two-sample form is one-scale mixing of its class (Lemma TS3).
2. **Route registry, a line for (T-pin).** Strength: unknown. Status: blocked-local at (L3). Evidence: rows 1118 to 1121; this file, step 3 (argued, unchecked). Reopen: a carried variable that is not a one-sample mean, with an exact composition identity; or a supplier of one-scale singlet mixing.
3. **Route registry, a line for (DS-W), the hypothesis of row 691's Theorem W.** It has none today (grep of `parts/gap.md` for "691": one hit, inside the entry of row 1118). Strength: stronger than (SEED) at one coupling. Status: open at the window; blocked-stronger. Evidence: row 691, check 693, check 1121 8.5, this file, step 4 (argued). Reopen: as in 6.4.
4. **Route registry, the BR-2 line.** Status unchanged. Add rows 1119 and 1120 as evidence: (RESP-TR) stopped; Lemma LOW bounds a collective response, not the neutral response that the reopen condition asks for.
5. **Route registry, the RE line.** Add 5.1, point 5: the even steps in law on file are Theorem AG, CONV-swap and Theorem W; none is weaker than its conclusion at one scale.
6. **Test table, lines that are not models.** Proposition J with Lemma JI: a recombination of two independent ring samples costs a fixed amount per junction at the window; it binds every swap form (proved by check 1121, no second reader). Lemma TS3: a two-sample form with a small constant is one-scale mixing of its class (proved by check 1120, same provider). After row 1: Lemma AFF and Example PROD.
7. **"Routes tried", a method 34.** Criteria in the law of the model for pinned cells (rows 1115 to 1121), with a pointer to rows 821 to 853 and 895 to 896. Row 998's digest does not cover rows 879 to 956, and it covers the rows before 879 only through exercise 2.
8. **A lead rule, proposed text.** "A row on a criterion in the law of the model first cites rows 845, 852, 895, 896 and 1118 to 1122. It states the kind of its hypothesis: a one-sample mean, a two-sample mean, or a supremum. A one-sample mean needs a uniqueness clause (Lemma AFF; argued until checked). A two-sample mean with a small constant is one-scale mixing of its class (Lemma TS3). A step that recombines two independent samples pays the cost of Proposition J."
9. **"Hardest open obligation".** Unchanged: (W).

### 6.6 Limits and strong words, read against this file

- Nobody has checked this file. It is a direction row. It proves nothing. No run was made. No paper was opened.
- The same model family wrote rows 1115 and 1119 and this file. I recommended the excursion that this file closes. This file is not an independent view of it.
- Lemma AFF, Example PROD, Lemma BACK, Lemmas GM and TILT, the count, remark (J3) and the chain to (SEED) are argued by hand here, with no second reader. PROD's covariance step is recalled. The frozen Z_2 row of 4.4 uses the lane's theorem as two files record it; I did not open its proof.
- The surface-transition row of 4.4 rests on recalled literature. Its mechanism is argued. For Wilson SU(2) I have neither an example nor an exclusion.
- "The supplier is not weaker than the one-scale content of C_beta" is an argued obstruction for three kinds of hypothesis. It is not a theorem about every possible criterion. Check 896 said the same of the older sentence.
- "No mechanism" and "no tool" mean: none in the files read. They do not say that none exists.
- The prior-work search of 5.1 was made by label names and was bounded. I read FINISH entries of rows 845, 852, 853, 895 and 896 and parts of four files. I did not open `library/gap-annealed-opus.md`, its check, or the files of rows 821, 836 and 853. Other rows may hold more.
- "Some hundreds of lattice units" in 4.5 is a guide from one order of magnitude.
- The word "closed" in 6.1 and 5.4 means: answered at argued grade in the three kinds tried. Clause (L3) is not proved impossible.
- Files changed: this file only. No commit, no push, no post.

Credits. T. Balaban, and E. Sussman and L. Alpoge (with Claude and Codex as authors of their text): the account on whose trajectory and first-passage data (W) and (GLUE-STEP) are stated. R. Dobrushin and S. Shlosman: the shape of the cube criterion that row 691 rebuilt, and the uniqueness condition behind Theorem DOB. J. van den Berg and C. Maes: disagreement percolation. A. Adhikari and S. Cao: the exchange of two samples. O. Redner, J. Machta and L. Chayes, through row 1099. A. van Enter and S. Shlosman: the first-order model. G. Mack and V. Petkova: the vortex inequality behind Lemma PAR. H. Gebelein: maximal correlation. The authors of the OpenAI preprints on the two-dimensional O(n) and O(4) models. J. Frohlich, B. Simon and T. Spencer, for what WALL A cites from them. R. Kotecky; H. Kunsch; H. Follmer; F. Martinelli and E. Olivieri (recalled by name only). In this lane: rows 691 and 693; 708 and 709; 731; 845 and 852; 859; 895 and 896; 998; 1004; 1018; 1108; 1115; 1116 and 1117 (gpt-6-luna); 1118 (gpt-6-astra) and its check 1121 (Claude Opus 5.5); 1119 (Claude Fable 5.2) and its check 1120 (Claude Opus 5.5).

RESULT: Row 1122 (Claude Fable 5.2 high, direction row, checked by no one, no run, no mass gap claimed): clause (L3) has no hypothesis on file that is both sufficient and weaker than one-scale singlet mixing, and an argued obstruction says that none exists in the three kinds tried: a one-sample mean such as Rbar is affine in the state, so it cannot give clustering unless it forces uniqueness (Lemma AFF), and it does not give the seed in a product with a frozen Z_2 factor (Example PROD); a two-sample mean with a small constant is one-scale mixing of its class (Lemma TS3 of check 1120); a supremum form is stronger than mixing in one state; the swap form is false at the window (Proposition J of check 1121); scope: argued by hand, unchecked, uniform form of the conclusion, classes with two states or product groups, belief grade inside one connected group. READING: the same question was run in rows 821 to 853 and 895 to 896 (Theorem AG, Proposition FIB, Lemma MC: an averaged condition is the worst case in disguise or the claim itself), rows 1115 to 1121 do not cite them, and this row adds the branch "or not sufficient". Pinned against periodic: (T-pin) carries the wrong kind of variable, (T-per) has the proved consumer and no slot, and the pinned form keeps a place only as an engine whose output is a mixing coefficient. Theorem W of row 691 at the window: its hypothesis reduces to one number K (a frame change at a boundary link costs at most 7 links, every other boundary link is a bounded tilt of at most 6 links, and the hypothesis holds for R at least (14 + 7 K)/delta); Proposition J does not exclude it, but a weakening in law meets Proposition J at the hybrids of row 691's Lemma 1; it is false for frozen Z_2 above 2.191, for compact U(1) in its Coulomb phase and for w_p at its transition; it could die at the supremum by a surface transition, at the centre, and at the same number as route RC; closed on (0, beta] it would give (SEED) at a window coupling with the flux sectors, which is a base case and not (W). Comparison: every open entry for the selective half dies first at one inequality at a coupling of order one that reads the group, and none has a mechanism. Next rows: (1) gap-averaged-closure, the obstruction and the reduction of Theorem W's hypothesis as checked statements, with a second reader for Proposition J, Lemma JI and Lemma TS3, and a lead rule; (2) gap-glue-engine-tree, a proof tree and first leaf for a periodic engine of the glue half, on the other provider, with a fast stop declared beforehand, and if the lead judges it not worth its cost, no second proof row now. Row not to run: a proof row on the hypothesis of Theorem W at the window; also no row whose deliverable is Rbar small in law. Registry: (T-pin) to blocked-local at (L3); a line for Theorem W's hypothesis as blocked-stronger at one coupling; Proposition J and Lemma TS3 into the test table; a lead rule for criteria in law. OPEN: (W), the selective step, (INF-L), (H-two-col), (EV-STEP), (DEC), the Rbar consumer for one connected group.
