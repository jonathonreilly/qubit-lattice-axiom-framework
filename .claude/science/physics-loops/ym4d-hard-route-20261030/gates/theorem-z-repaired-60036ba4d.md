lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T04:52Z

# Gate: repaired Theorem Z, `library/quiet-boundary-rarity.md`, at 60036ba4d

**Provenance.** Reviewer: Claude Opus 5.5, effort high, fresh session, mapped side of the firewall. Commit 60036ba4d. Text under review was written by Claude Opus 5.5 at max effort, so this is a SAME-MODEL check: not independent in model, and not an audit. Verdicts steer research and grant no status.

## Verdicts

| Statement | Verdict | What it establishes if true |
|---|---|---|
| Theorem Z | **CORRECT-NO-ADVANCE.** No counterexample to the inequality, but its proof rests on Lemma OC, which fails as written (D1, D2, D3), and its induction does not close on the stated mark term (D4). Its "So" clause is false for a general V^fl (D7). | Own-level lower bound for F at any field against a class reference, with no rough field held fixed. |
| Lemma OC | **WRONG as written.** (O1) is false or (O2) is, by the definition of Y_i (D2). At a long flux sheet 𝒜_i is empty, so Lambda_i, V^# and the descent do not exist at the stated radius (D1). Abel summation in (O3) is right. | Every rough cell and marked brick pays at its own level. |
| Lemma ST | **ADVANCE** for one quiet layer at one level. Local repairs in D8. Layers at several levels are not covered by its proof, as the note says itself. | Flux bound next to quiet data, with no sup-norm constant. |
| Exploration, stop | **ADVANCE.** (i) to (iii) hold, and the old D1, D2 are gone. Sigma(E) must be redefined (D6). | A stopping set from outside, with failure read at the top level only. |
| Recursion for a leaf | **CORRECT-NO-ADVANCE.** The count closes only after D4's repair, and it reads Theorem Z with marks. | p_j <= 2 z'_j with no per-level factor. |
| Step 5 | **ADVANCE at class minimisers only.** As written, a_B(d) has rough chains and marks in the collar and a tropical form is not a difference of two infima (D5). Read for the top bracket it holds, and that is all it is needed for. | The data on Sigma cost only a tail. |
| (M), Steps 1 to 3 | **ADVANCE**, given the exploration. | The outside cancels exactly. |
| (A1') | **CORRECT-NO-ADVANCE.** The structure repairs the old D11, and it adds nothing until Theorem Z stands. | Activity per cell, far family cancelled. |

## Defects, ranked by what each breaks

**D1. A long flux sheet has no narrow class fill, so Lemma OC's reference does not exist. Breaks (O2), V^#, W_B^#, and the dense step of Prop 10. Repair direction only, unproved.**
`library/quiet-boundary-rarity.md:149`, `:153`, `:167`, hostile (4) at `:169`; `library/relative-density-bound.md:245`, consequence (CI''') at `:273`.

Concrete failure. Take a level-j field of centre links: V_j = -1 on the links crossing a 3-volume, +1 elsewhere. Its plaquettes are +1 except on a closed 2-sheet Gamma, where they are -1, and rectangles around Gamma have holonomy -1 at every radius (N1). So X is exactly the thin sheet, and V_j is trivial off it. By non-abelian Stokes, a field equal to V_j off a set whose section is a disc of n plaquettes has total plaquette angle at least pi on that disc. So a field of flux at most T needs n >= pi/T, a radius of about (pi/T)^{1/2}/2 = (L/2)(pi/a_*)^{1/2} cells, which is (1/2)(pi/a_*)^{1/2} blocks.

- Y_i has absolute radius r_{I_*}, or J boxes at a dense cluster. The order of constants at `library/relative-density-bound.md:245` is J, K, I_*, then L, then T small, and a_* <= a_th(L). So for a_* < pi/(4 J^2), 𝒜_i is empty and Lambda_i = +infinity. Under the kernel a sheet box is dense, its parents are Haar, but the off-dropped parents still see the holonomy, so widening within dropped boxes does not help.
- The dense step says "Fill D^{+j}" with Lemma F. Lemma F fills a cube: its shell is simply connected. The shell of a sheet's neighbourhood has a non-contractible loop with holonomy -1, and no flat fill exists. So (CI''') as derived has no proof on a long dense cluster. The note already knows this obstruction for (F2): `library/quiet-boundary-rarity.md:45` and `parts/hard-core--mapped.md:61`. It was not carried into the descent, nor into Lemma OC, whose whole point is that Y_i may be narrower than a block.
- The same holds at intermediate strength, with no centre flux: a sheet of width w and flux 2 T per cell, with 2 T w^2 <= pi so nothing unwinds, needs Y to reach about 0.2 w on each side, by area alone. So Y is wider than a block once w >> L, which that bound allows, as T^-1/2 = L a_*^-1/2, and all its boxes are dense.

*Why it is not simply harmless.* Long sheets are exactly the large polymers (A1') must weigh. *Repair direction, unproved:* at a sheet, take Y_i wide, of width about (theta_h/T)^{1/2}, nested with Y_{i+1} so no parent has to be restored across it. These lie inside tube(X), so Theorem Z's region does not change. The gain must come from the sheet's own excess energy, as the fill spreads the same flux over more cells. That needs a near-optimal fill, or a class threshold the fill can meet: (F2) gives flux C_a T, which pays only where the cells are above C_a T, and cells in (T, C_a T) on a thick sheet remain to be treated. A named lemma is owed, and I did not prove it.

**D2. Y_i contradicts itself between (O1) and (O2). Breaks (O1) as written; repair in hand, unproved.**
`:149`, `:151`, `:153`. Y_i contains "the blocks of affected parents". (O2) needs that: the bump moves level-j data over the whole block, or U^(i+1) is not in 𝒜_i. But (O1) reads "a fraction f <= C (r_{I_*}/L)^3 of the lines of a parent". With whole blocks in Y_i the fraction is 1, the minimiser of 𝒜_{i-1} is not tied to the parent there, and it releases the parent's energy. This is the false step the Lemma was written to remove (`:145`), one level down. N2 finds, for one parent at flux T in d = 4, a released fraction 0.71, 0.57 of the lift's energy at L = 3, 5, with the parent moved by 0.81, 0.65 T, against 0.18, 0.008 with the hull alone. The lift's energy there is 19.1, 23.0 T^2, so about 13 T^2 is released at L = 5. In d = 3: 0.67, 0.54, 0.48 at L = 3, 5, 7. So delta is not small in this model. (O3) needs delta <= c/4.

*Repair, unproved:* take Y_i := the hull and dropped parents only, and in 𝒜_i let level-i data differ from V_i off Y_i by bumps on the blocks of affected parents, of size at most the bound of (a) on `library/relative-density-bound.md:267`. Then the parent mismatch in (O1) is at most C f^{1/2} K^{1/2} T, as the proof reads, and U^(i+1) is in 𝒜_i. I tried holding all higher levels fixed in 𝒜_i instead, which gives G_i >= 0 at once. It fails: a dropped parent then forces a column of changed cells at every higher level, with a loss per level.

**D3. Lemma OC with frozen data is not proved, and Theorem Z needs exactly that. Breaks Step 4's use of Trop.**
`:149` says "and quiet boundary", and no step reads the boundary. In Step 4 the chains run over all W_B inside Sigma, so a rough cell can sit next to a frozen brick (level by level, next to each Sigma_j). Descent fills a cube, flat inside, and that cube meets frozen bonds, which it may not change. Lemma ST does not help: it bounds a minimiser, not a general field. *Repair, unproved:* a boundary form of Lemma F with target the lift on the frozen part, reading that quiet data have energy at most C K T^2 per box. I see no obstruction.

**D4. The mark loss recurs at every level. Breaks the induction of Theorem Z's mark term as stated; repair in hand.**
`:69`, `:109`, `:113`, `:123`. Step 4 carries -𝔈_{l-1} d_x^4 |S'| from level l - 1, and `:111` absorbs only the term in |tube X(W_B)|. Step 1 puts a column with collar above each lower mark in A_0, so level l adds C n log x_l >= C_1 d_x^4 |S| log x_l for the same marks. The stated 𝔈_l d_x^4 |S| has no room for both, so at depth D below the top the written proof gives a loss of about D C_1 log x per mark. That exceeds the own-level gain c eps_q^2 T^2 x once D >= D_1, of order eps_q^2 T^2 x/log x. Witness trees go down to level 0, so the recursion p_j <= z'_j + N p_{j-1}^q does not follow as written. The slope of the flow does not pay for it, since c c_0 eps_q^2 T^2 is far below C_1 log x.

*Repair, by hand, level of each term, not independent of the rest:* count distinct columns. Replace d_x^4 |S| by the sum over levels i <= l of d_x^4 C(t_0) |pi_i(S)|, with pi_i(S) the level-i balls over S. For the leaves of a witness tree, a level-i ball is one tree node, every node has q >= 2 children, so nodes <= 2 leaves, and the total is at most 2 C(t_0) 𝔈 d_x^4 |S|. Equivalently, carry each mark's value upward as a number: m_j >= min(Z_j, q m_{j-1}) - C 𝔈, which closes as q >= 2. An isolated deep mark still loses per level, so the statement must be restricted to leaf sets of trees, or to depth one, which is what the consumers read.

**D5. Step 5 as written compares the wrong objects; the repair is a narrower reading.**
`:115`, `:117`. (a) a_B(d) is an inf over all W_B, with rough chains and marks. "Both are class there: marks and cells above T lie in A_0" is false: the cells above T of V lie in A_0, those of W_B and its chain do not, and the marks of certificates lie in B outside A_0. Then P is not a competitor for b(d), or P' loses a mark. (b) "x-trop(a_B(d) - b(d))" is not defined: Trop is a functional of a chain, not of two infima, and the claim that the exchange closes the old gap at Step 5(ii) does not follow for all levels.

*Repair, checked by hand:* Step 5 is needed only at the top bracket. Let V^# be the reference, W_a the minimiser for Lambda_l with data d, W_* the one with no data. Both are class, parents agree in the collar, and the fibre chart there is connected. The exchange gives 𝔸^d(V^#) <= Lambda_l^d + tr, so G_l^d >= -tr. That is what Lemma OC with data needs, and the chain part is D3. The tail then reads a collar of width about d_x, as written. If certificates are present the cut must stay outside their marks, so the room is the 6 bricks of margin, with tail a large power of T per certificate brick, from t_0 >= C L log(1/T). This is small against the marks' own gain, but not of the stated form x e^{-delta d_x} |boundary tube|.

**D6. Sigma(E) := bricks that touch E has thickness about t_0/8 in d = 4, not t_0. Breaks the layer claims; repair in hand.**
`:37`, `:41`. On Lemma BG's tiling a corner leaves a brick near E that does not touch it. N3: minimum thickness 4, 2, 1 at t_0 = 8 in d = 2, 3, 4. So "Thickness at least t_0", "in Sigma_{l+1}" and the clearance fail once (B) lets E_l stand about (2/3) t_0 parents past shadow E_{l+1} at such a corner, and t_0 >= 3 R_loc no longer gives R_loc of room. The mirroring changed Lemma 22.1's definition. *Repair:* Sigma(E) := bricks within t_0 of E, not in E, as the upper chain has it. N3 control: thickness at least t_0. The note's numbers then hold: parent within (2/3 + 2/L) t_0 + 2 <= t_0 - 1 of E_{l+1}, and clearance at least t_0 L/3 - 2 t_0 - L >= r_S L, for L large against the note's constants. Reading parents on a patch stays on or outside Sigma_{l+1} if r_lift <= t_0/4, as `:35` gives.

**D7. Marks and the general reference.**
(a) `:71`: "So its value ... is at least" is false for "any class field" V^fl: take V^fl of larger energy than V, and 𝔹 - 𝔸 < 0. It holds only at V^fl = V^#, where G_{m+1} = 0. Consumers such as (FF_j)(U) at `:135` must take V^#. (b) (O2') replaces the field on a patch, so the patch must lie in Y_j, or U^(j+1) is not in 𝒜_j. Then Theorem Z's "equal to V off tube(X)" must read "off tube(X) and the patches of S", and (O1) must pin the parents on the patches, or a minimiser of 𝒜_{i-1} moves them. Both are one-line changes.

**D8. Lemma ST: the quantity and the citation.**
`:21`, `:29`. theta_c(V_l) - theta_c(Lift_b) depends on the frame, and the fibre contains the gauge moves that vanish at block centres. Read at bare sites the difference is not small for a typical field, as the two plaquettes are rotated relative to one another. It must be read in the tree gauge of Text 5.1, rooted at block centres. Then the typical size claimed at `:23` stands, up to a correction of about t_0^5 T^2/x by a count, also below eps_q^2 T^2 for x >= x_*. Lemma U is stated for one field at trivial background, and the proof cites it for a relative field: a perturbative relative form is owed, with C(L) T << 1/L, which a_* <= a_th(L) gives. Routine, and neither is written. C_s stays a U(1) number: `checks/hard-core--mapped_face_stability.py` was read, not re-run, and nothing non-abelian was run.

**D9. Constants that do not change the outcome.**
(a) `:61`: every third cell of a chain at range 4 t_0 is not 12 t_0 apart. Project on a diameter: q = ceil(L/48) works. (b) `:61`: N := (C L^4)^q should have the ball's volume, (C t_0 L)^{4 q}. (c) `:111`: sigma_j := 𝔈_j/x_j must carry the factor C (d_x + t_0)^4. (d) `:123`: a chain's bricks are not separated, so the weight per brick is z'^{1/C}, C about 24^4, not p_{l-1}; x_* still pays. (e) A failed crossing of 5 bricks at range 4 t_0 gives one separated cell.

## The old defects, one by one

| Old | Status now |
|---|---|
| D1 annuli, per-level factor | **Repaired.** No annuli below the top; failure reads level t only. New geometry defect D6. |
| D2 duality, outermost family | **Repaired** by the algorithm. I rechecked the stopping set and the witness claim; hostile (14) holds. |
| D3 quiet at T, forced rough face | **Repaired** by Lemma ST and quiet in l^2, subject to D8 and to several levels. |
| D4 sectors | **Rerouted, not closed here.** Step 4 reads (VAL^𝔡) correctly and no path is read. The clause is a sketch in `library/sector-values.md`, Section 6, with its inputs in queue items 1 and 5. |
| D5 pockets | **Repaired**: |tube| <= C (d_x + t_0)^4 |X| holds by construction. It moves the weight to (F2), still a gap. |
| D6 labelled cells | **Repaired in form**: (BE_2) and descent read no labels. It rests on Lemma OC, so see D1, D2. |
| D7 Lemma TE | Not consumed now. |
| D8 own-level attribution | **Replaced** by Lemma OC, itself WRONG as written. Its Abel step is right, and only x_j >= x_i - C(L) is read, which the flow's bound gives. |
| D9 range | **Repaired**, given D6's room. |
| D10 forced marks, S | **Repaired**: A_0 holds S, and the leaf rule stops at the highest non-quiet cell. Hostile (15), (16) hold. |
| D11 units, (A1') | **Repaired** in structure: N(F) exact, and the absence of further polymers is in I^class. |

## Steps

- Base, Step 1: hold. Step 2: holds; each thin complement of B counts within the margin.
- Step 3, (M): holds. I rechecked that O_B is common, including reading parents on patches, given d_x/L > r_lift, which t_0 >= C L log(1/T) allows.
- Step 4: I^D's lower bound holds, given (I_{l-1}^{𝔡'}) and Lemma ST. The numerator fails at D1, D3, D4.
- Step 5: D5. Step 6: holds up to D4, D9.
- (O3): holds given (O1), (O2). (O2') holds given D7(b), with the flux at a mark as written. (O2) outside sheets, away from layers: holds at the level read, given (BE_2) and Prop 10 at non-dense or cube-like clusters.

## Numerics

Criteria are in the headers of `checks/gate_tz/tz_geometry.py` and `tz_o1_blocks.py`, written before running. Output: `tz_geometry.out`, `tz_o1_blocks.out`. Run under the lock from 17:17 UTC, at 50 percent memory free at the start.

- **N1, PASS.** 4-torus of side 12: 288 of 288 expected -1 plaquettes, all on two sheets; holonomy -1 on rectangles of half-side 1, 2; Stokes control 0 violations in 1000 trials. It shows the field and the bound. It says nothing on energy.
- **N3, control PASS.** The first run read -2 at d = 2: a bug of mine, as a random E could be empty. I skipped empty E, with the criterion unchanged. Thickness of the touching layer 4, 2, 1 at d = 2, 3, 4, t_0 = 8. Within t_0: 8. Finite window, few cases for the control at d = 3, 4.
- **N2.** Controls: residual at most 4e-9; block-Q prints 0.00000, so it is confirmed to 1e-5 in rho, not to the 1e-6 of C0, as my print had five digits. d = 3 meets C1 at L = 3, 5, 7. C2 not met, as rho(7) is above half of rho(3). rho falls with L, and I claim no limit. d = 4, L = 3 was stopped by the RSS guard during factorisation, so I wrote `tz_o1_d4.py` (N2b), with criteria first and no factorisation, output `tz_o1_d4.out`, run under the lock at 17:27 UTC at 50 percent free. Its controls hold: stationarity at most 5.6e-9, residual at most 1.2e-9. **d = 4 meets C1:** rho(block) 0.70741, 0.57487 and s 0.8070, 0.6534 at L = 3, 5; rho(hull) 0.17613, 0.00817. rho falls with L in both dimensions, and two sizes in d = 4 give no limit, so I claim none. Abelian, one level, one parent, chosen as a worst case: a mechanism, not a size in SU(2). D2 does not rest on it: the fraction-of-lines step fails by definition.

## What was and was not read

Read: `FINISH.md`, `GOAL.md`, `gates/theorem-z-3b7fd4e57.md`, all of `library/quiet-boundary-rarity.md`; `library/relative-density-bound.md` Props 10, 10' and their hostile pass; `library/sector-values.md` Sections 4, 6; `library/lattice-uhlenbeck.md` statements of Lemmas U, F; Lemma BG; Texts 5.1, 5.2 of the mapped file; the upper chain's Lemmas 20.3, 22.1, 22.2. That part of the upper chain mentions an equation of the sibling attempt by number. No proof text of the sibling was read or used. `parts/hard-core--independent.md` and gates on it were not opened. The Sussman-Alpoge repository was not read.

Not checked: (F2) (queue item 8); (VAL^𝔡), Lemma EX; Nest coercivity; Theorem F-D; Claim A; (o); Text 5.9's bulk step; Prop MD*; the flow beyond the one bound read; (A2) and the Dobrushin step; Lemma ST with layers at several levels.

Status: finished.
