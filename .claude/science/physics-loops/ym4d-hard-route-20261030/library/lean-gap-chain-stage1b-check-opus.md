lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T13:10Z

# Check of row 1504 (Lean Stage 1b, Wilson.lean): row 1505

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, at commit dad112a12, started 2026-11-25T01:10Z (date -u). Cross-provider check by reading (author of the checked file: gpt-6.2-astra). Not an audit. The build and axiom print are the lead's replay, not this check.

## Plan

1. Repo search: earlier checks of Wilson-weight definitions (row 1503 check, design file, gap-seed-check Lemma 1.1, gap-crux-restate 3.4, gap-transfer).
2. Q1: read Wilson.lean definitions (links, step, transport, faceTrace, action, density, partition, sides, Haar) against Lemma 1.1 of library/gap-seed-check.md, row 697 section 3.4, row 667.
3. Q2: cross, log_lower, fields_of_bridge against TorusData fields in TheoremS.lean; bridge hypothesis minimal?
4. Q3: boxSpectrum_of_operator vs docstring, receipt, BoxSpectrum fields le_one, atThree.
5. Q4: kernel K_R of RECEIPT-1b vs row 698 Lemma 1.1, its L2 bound.
6. Verdict.

## Repo search

Read: row 1504 (`FINISH.md` L1586), `lean/gapchain/GapChain/Wilson.lean` (575 lines, all of it), `lean/gapchain/RECEIPT-1b.md` (all), the TorusData, BoxSpectrum, Box and HSNormLE declarations of `TheoremS.lean` (L315-335, L428-470) and `LemmaM1.lean` (L15-30), the hand sources `library/gap-transfer.md` (row 667: Notation N.1-N.8, Sections 1-3), `library/gap-seed-check.md` (row 698: Point 1, Lemma 1.1, and the uses at L59-129), `library/gap-crux-restate.md` (row 697: Section 1 normalization), and the row 1503 check (`library/lean-gap-chain-stage1-check-opus.md`, via its FINISH result). No earlier check of Wilson.lean exists in the repository (it was written at row 1504). Hand-source authorship as the receipt says: row 667 and row 698 by Claude Opus 5.5 (file headers), row 697 by Claude Fable 5.2. This check states nothing new; it compares definitions.

## Q1. The Lean partition function against the hand Wilson weight

Hand definition (row 667 N.1-N.6, row 697 Section 1, row 698 Lemma 1.1 (ii)): 4-torus with sides >= 3, normalized Haar dg on SU(2) on every positively oriented link, Wilson action S(U) = beta * sum over unoriented plaquettes of (1 - (1/2) tr U_P), Z = integral of exp(-S). For SU(2), tr is real (N.2), so (1/2) tr = (1/2) Re tr.

Lean, item by item (Wilson.lean line numbers):

| Lean object | What it is | Hand object | Verdict |
| --- | --- | --- | --- |
| `SU2` (L35) | `Matrix.specialUnitaryGroup (Fin 2) ℂ` | G = SU(2) | same |
| `linkHaar` (L58-64) | `Measure.haarMeasure` with normalizing compact set `univ`; `haarMeasure_self` gives mass 1 on univ, so a probability; Borel sigma-algebra (L54-55) | normalized Haar dg (N.1) | same: the left Haar probability of a compact group, unique, and also right- and inversion-invariant (not needed for the definition) |
| `Link n = Site n × Dir`, `Site n = Π i : Fin 4, Fin (n i)` (L97-101), `haar n = Measure.pi` (L102) | one variable per site and positive direction, product of link Haar probabilities | positive links of Lambda x Z_T, product Haar (N.3, N.6) | same: 4 * |sites| links |
| `step` (L105) | coordinate i moved by `finRotate`, i.e. x_i -> x_i + 1 mod n_i | periodic unit step | same: periodic boundary conditions |
| `transport U x i j` (L109) | U(x,i) U(x+e_i,j) U(x+e_j,i)^-1 U(x,j)^-1 | u_p of N.4, and the time-like holonomy of 1.1 (up to inversion) | same; reversal (j,i) is the inverse word (`halfTrace_reverse`, L112) |
| `halfTrace` (L67) | Re tr(g)/2 | (1/2) tr g | same on SU(2) |
| `action` (L125) | (1/2) * sum over sites x and ordered pairs i != j of (1 - halfTrace) | sum over unoriented plaquettes of (1 - (1/2) tr U_P) | same: `action_eq_geometric` (L145) proves action = sum over x and i < j of (1 - halfTrace), i.e. six plaquettes per site, each once, both orientations weighted 1/2. For sides >= 3 the map (x, i<j) -> plaquette is a bijection onto the geometric plaquettes (row 698 Point 1, item 3), so this is exactly the hand sum |n|*6 terms |
| `density`, `partition` (L159-161) | integral of exp(-beta * action) against `haar n` | Z = integral of exp(-beta A) (row 697 Section 1; S = beta A in row 667 N.6) | same; beta multiplies the action once, with no factor 2 or 1/g^2 |
| `sides a R = ![a, R.x, R.y, R.z]`, `Z β a R` (L287-290) | time side a on axis 0, spatial sides of R on axes 1-3 | Z(N_1, N_2, N_3 \| time k) of Lemma 1.1 (ii) | same |

Points checked in detail.
- beta normalization: the plaquette Boltzmann factor is exp(-beta(1 - Re tr U_p/2)), the one-bond kernel c(g) of row 667 N.7 and the plaquette weight of row 698 Lemma 1.1 (iv); the corrected (TM-c) wording of row 698 uses the same normalization. No mismatch.
- Plaquette count: 6 per site (`count` in `mean_action`, 12 ordered planes / 2). Hand: 3N^3 spatial plus 3N^3 T time-like plaquettes per N^3 T sites (row 667 N.4, 1.1), also 6 per site.
- Orientation: tr U^-1 = tr U (N.2); Lean averages the two orientations and `halfTrace_inv` proves this equality, so the 1/2 weighting gives the unoriented sum (`action_eq_geometric`). Correct.
- Degenerate sides: `Z` is defined for all side vectors, including sides 0, 1, 2 where the plaquette count differs from the geometric one. Every consumer restricts to sides >= 3 (`Box.Valid`, `3 ≤ a`), and `integral_faceTrace` / `mean_action` assume sides >= 2. No consumer reads Z at a side below 3, so this is not a defect.
- The Haar measure is on the Borel sigma-algebra of the subspace topology (L54-55, instance declared locally). Remark only: if Mathlib also supplies a subtype measurable-space instance on this type, the two agree mathematically (second countable, Borel), and Stage 1c should use the same local instance to avoid a non-definitional diamond. Not a faithfulness issue.

**Q1 verdict: FAITHFUL.** `Z β a R` is the SU(2) Wilson partition function of the periodic 4-torus with sides (a, R.x, R.y, R.z), normalized product Haar probability on links, action beta * sum over unoriented plaquettes of (1 - (1/2) tr U_P), exactly as rows 667, 697 and 698 define it.

## Q2. cross, log_lower, fields_of_bridge against the TorusData fields

TorusData (TheoremS.lean L451-464):
- cross: for R valid, every axis i, a, b >= 3: (spectrum (R.replace i b)).weight a = (spectrum (R.replace i a)).weight b.
- lower: for R valid, every i, there is d with d*a*b <= log((spectrum (R.replace i b)).weight a) for all a, b >= 3.

Lean:
- `cross β R i a b : Z β a (R.replace i b) = Z β b (R.replace i a)` (L302), for all a, b (no side restriction needed; it is a relabelling). Proof: `sides b (R.replace i a) = sides a (R.replace i b) ∘ exchange i` with `exchange` the transposition of time and axis i, then `partition_permute`, which pulls back by the link bijection (site permutation x (direction permutation)), proved measure preserving (`measurePreserving_relabel`) and action preserving (`faceTrace_relabel`: the face (x, (i,j)) goes to (e x, (e i, e j)), the ordered planes are permuted bijectively). This is row 698 Lemma 1.1 (v) for Z, with the orientation issue removed because ordered planes are summed. Faithful.
- `log_lower` (L316): for R valid, a, b >= 3, (-6 beta s1 s2) a b <= log Z β a (R.replace i b), s1 s2 = `spectatorArea R i`, the product of the two sides of R other than i. Since R.replace i b keeps those two sides, the constant depends on (R, i) only, uniform in (a, b), as the field's quantifier order requires. Proof: Jensen for the convex exp against the Haar probability, with Haar mean of the action = 6 * |sites| (`integral_faceTrace`: multiplying one link by -1 negates the face trace, so each face trace has mean 0). Arithmetic: |sites| = a b s1 s2. Correct. The hand bound (row 698 L93) is the cruder pointwise ell >= -12 beta c d; Lean's -6 is sharper and both satisfy the field, which asks only for existence of d.
- `fields_of_bridge` (L336): from `bridge : ∀ R, R.Valid → ∀ a ≥ 3, (spectrum R).weight a = Z β a R` it returns two propositions whose statements are, symbol for symbol, the types of `TorusData.cross` and `TorusData.lower` (same binders, same order, same `3 ≤` guards). The validity of `R.replace i b` for b >= 3 is proved inside. Faithful.

Is the bridge exactly what a transfer-operator proof must supply? Hand: Lemma 1.1 (ii) gives Z(R | time k) = Tr T_P^k for k >= 2, and Tr T_P^k = sum of the positive eigenvalues of T_P to the power k with multiplicity (row 667 A2, row 698 Verdict (1) remark (b)); with the BoxSpectrum normalization weight a = top^a (1 + sum ratio_i^a) this is the bridge at a >= 3. The bridge asks it only for valid R and a >= 3, which is less than Lemma 1.1 (ii) (k >= 2). It asks nothing about simplicity, positivity of the ground state, the centre flips (iv) or gauge invariance, which TorusData does not use (row 1503 check). So: no more than the transfer-operator proof supplies, and exactly what TorusData's cross and lower need.

One property worth recording (proved here by hand, short): the bridge determines the spectral data that Theorem S reads. If two BoxSpectrum values B, B' have weight a = weight' a for all a >= 3, then top = top' and the multisets of positive ratios agree (power sums of a nonnegative summable family for all a >= 3 determine its positive values with multiplicity: the largest value is the limit of weight(a)^(1/a); remove it and repeat; the constraint ratio <= 1 forces top to be the largest value, and the explicit 1 removes one copy of it). Hence `thermal`, `seed`, `seedRate` and `gap` of TorusData are those of the true transfer operator whichever BoxSpectrum family satisfies the bridge. So the bridge cannot be met by a spectrum that is not the operator's.

With `Check1503.weight_logConvex` (row 1503, Step 5: logConvex follows from the BoxSpectrum fields) the bridge alone then yields a full TorusData. The receipt says this (next row 2). Correct.

**Q2 verdict: FAITHFUL.** cross and log_lower state the hand facts; fields_of_bridge's conclusions are exactly the TorusData fields; its hypothesis is Lemma 1.1 (ii) restricted to valid boxes and a >= 3 with the spectral trace identity, no more.

## Q3. boxSpectrum_of_operator

Statement (L496-500): for a complex Hilbert space H (complete, nontrivial), T : H ->L H compact, positive (`IsPositive`: self-adjoint with nonnegative quadratic form), T != 0, and `HSNormLE T δ` for some real δ, there is a BoxSpectrum B with
(a) B.top = ‖T‖;
(b) a slot t : PositiveSlot T with value ‖T‖ such that `EnumeratesRatios B (slot value) t`;
(c) for every a >= 3, B.weight a = tsum over PositiveSlot T of (slot value)^a.

Reading of the objects.
- `PositiveSlot T` (L477) = Σ over reals r > 0 of Fin (finrank of the r-eigenspace). For r not an eigenvalue the eigenspace is 0 and contributes no slot; for an eigenvalue r > 0 of a compact operator the eigenspace is finite-dimensional (`finite_dimensional_eigenspace`), so finrank is its dimension, the full multiplicity (geometric = algebraic for a self-adjoint operator). `nonzero_eigenvalue_has_slot` (L481) proves every nonzero complex eigenvalue is a positive real with at least one slot. The zero eigenspace (infinite-dimensional in the Wilson case: T_P vanishes off the gauge-invariant subspace) has no slot, matching the hand convention that zero eigenvalues do not contribute (row 698 Verdict (1) remark (b)).
- (a) and the existence of t: `positive_top_eigenvalue` (L387) proves ‖T‖ > 0 and ‖T‖ is an eigenvalue (norm of a nonnegative element of a C*-algebra lies in its spectrum; for compact T a nonzero spectral point is an eigenvalue). This is the hand lambda_0 = ‖T_P‖ (Lemma 1.1 (iii)).
- `EnumeratesRatios` (L399): an injection e of the slots into ℕ with ratio(e t) = 0, ratio(e i) = value_i / top for every other slot i, and ratio = 0 off the range. So exactly one slot of the top is removed (it is the explicit 1 in weight), further copies of the top give ratio 1, every other positive eigenvalue appears once per multiplicity, and the padding is zero. This is what the docstring and the receipt claim.
- (c): proved by `boxSpectrum_of_slots`: weight a = top^a (1 + sum over slots i != t of (value_i/top)^a) = sum over all slots of value_i^a, with the summability of value^2 obtained from `HSNormLE` applied to the finite orthonormal families of eigenvectors (‖T v_i‖ = value_i), and value_i <= ‖T‖ from `le_opNorm`. Since the tsum convention returns 0 on non-summable families, I checked that the right side is a genuine sum: summability of value^a for a >= 2 is proved inside (`hrs`), and in any case weight a > 0 rules out the junk value.
- Match with the BoxSpectrum fields: `le_one` holds because each ratio is value/top <= 1 (or 0); `atThree` holds because the cube sum is dominated by the square sum. `top_pos`, `nonneg` are immediate.

Hypotheses no stronger than needed: compactness and positivity are what the hand Lemma 1.1 (i) supplies (positive trace class implies both); HSNormLE is implied by the hand Statement (3) (HS norm <= 1). Without a Hilbert-Schmidt or Schatten-type bound a compact positive operator can have sum of lambda^3 infinite (eigenvalues 1/log n), so some summability hypothesis is needed; HS is the natural one and the Wilson operator meets it. Positivity is used for (b) (top attained at ‖T‖) and for the eigenvalues being nonnegative reals.

What it does not say (correctly not claimed): that weight a equals a trace or a Haar integral. That identity is the remaining bridge unit, stated as such in the receipt (Section Spectral bridge, last two paragraphs) and in the docstring of L494-495.

**Q3 verdict: FAITHFUL.** boxSpectrum_of_operator states what its docstring and the receipt claim: top = operator norm, every positive eigenvalue with its full multiplicity, one top slot removed, weights = power sums for a >= 3; the produced B meets le_one and atThree by construction.

## Q4. The candidate kernel K_R of the receipt

Receipt (Section Spectral bridge):
K_R(U, V) = exp(-beta (S_s(U) + S_s(V))/2) * integral over vertex gauges g (product Haar probability) of the product over positive spatial links e: x -> y of exp[-beta (1 - (1/2) Re tr(g_x V_e g_y^-1 U_e^-1))].

Hand kernel (row 667 statement (1a); row 698 Lemma 1.1 extends it to Lambda = Z/N_1 x Z/N_2 x Z/N_3):
A_T(u, v) = exp(-(V(u) + V(v))/2) * integral over G^V of product over (x,i) in E of exp[-beta (1 - (1/2) tr(h(x) v_(x,i) h(x+e_i)^-1 u_(x,i)^-1))] dh, with V = beta * sum over spatial plaquettes of (1 - (1/2) tr u_p).

Identification: U = u (slice t), V = v (slice t+1), g = h, e = (x,i), y = x + e_i, and beta S_s = V provided S_s is the spatial action without beta (the receipt says "spatial plaquette action", and its formula puts beta outside, consistent with Lean's `action`, which also has no beta). With these the two formulas are identical symbol for symbol. Orientation check against Lean's own holonomy: with time on axis 0 and g_x = U(x,0), Lean's `transport U x 0 e` is g_x V_e g_y^-1 U_e^-1 (the receipt's word, and the hand 1.1 holonomy), so the kernel is the one whose cyclic product gives Lean's Z after integrating the temporal links (row 667, 1.2-1.3, eq. (1.2)). Each time-like plaquette is in one factor; each spatial plaquette gets weight 1/2 from each neighbouring kernel, as the receipt says. The gauge average inside the kernel is the hand projection: the integral operator with kernel A_T is T_P = P T P = T P (row 667 1.6), which is the operator whose positive spectrum Lemma 1.1 uses; it is 0 on the non-invariant subspace, consistent with Q3.

L2 bound: every exponent -beta(1 - (1/2) tr) is <= 0 for beta > 0 (tr <= 2), so 0 < K_R <= 1 pointwise (hand (1a): e^(-12 beta |Lambda|) <= A_T <= 1). On the probability space X x X, ‖K_R‖_L2 <= sup K_R <= 1. The receipt's statement "the candidate kernel's L² norm at most one" is right; by row 667 A0(e) and Statement (3) the Hilbert-Schmidt norm of T_P equals ‖A_T‖_L2 <= 1, so `HSNormLE T_P 1` is the expected Stage 1c bound.

**Q4 verdict: CORRECT.** K_R is the hand kernel A_T of row 667 (1a), extended to rectangular boxes by row 698 Lemma 1.1, and its L2 bound (<= 1) is right.

## Release convention (credit check)

Sussman and Alpoge, with Claude and Codex as authors of their text, CA-I Definition 1.1 (theorem_0_complete_account_raw_I.tex L447-483 at 31a47c543775, fetched once into a scratch folder): normalized product Haar on one orientation of each bond, trace normalized to tr 1 = 1, A(U) = sum over unoriented plaquettes of (1 - Re tr U(dp)), bare density exp(-g_0^-2 A). For SU(2) their normalized trace is (1/2) Tr, so their A is exactly Lean's `action` and their g_0^-2 is Lean's (and the lane's) beta. The receipt's credit to their conventions is accurate; no factor (such as the lattice convention beta = 4/g^2) separates the three.

## Verdict

**FAITHFUL.** No definition or statement needs to change.

| Question | Verdict |
| --- | --- |
| Q1 Z (links, step, transport, faceTrace, action, density, partition, sides, Haar) | FAITHFUL: SU(2) Wilson weight of the periodic 4-torus, normalized Haar probability, beta once, six plaquettes per site, both orientations averaged, periodic steps; equal to rows 667/697/698 and to the release's g_0^-2 convention |
| Q2 cross, log_lower, fields_of_bridge | FAITHFUL: conclusions are exactly TorusData.cross and TorusData.lower; the bridge is Lemma 1.1 (ii) on valid boxes for a >= 3 with the spectral trace identity, no more; and it pins top, ratios, seed and gap to the operator's |
| Q3 boxSpectrum_of_operator | FAITHFUL: top = ‖T‖, every positive eigenvalue with full multiplicity, one top slot removed, weights = power sums for a >= 3; le_one and atThree met |
| Q4 kernel K_R and its L2 bound | CORRECT: K_R = A_T of row 667 (1a) on the rectangular slice (row 698 Lemma 1.1); 0 < K_R <= 1, so ‖K_R‖_L2 <= 1 |

Defects that break something: none.

Remarks (do not break anything; for Stage 1c and the receipt):
1. The receipt's K_R writes beta outside S_s; state explicitly that S_s is the spatial action without beta (as Lean's `action`), otherwise beta enters twice.
2. Wilson.lean L54-55 declares the Borel measurable-space instance on SU2 locally. Stage 1c should build its L2 space on this same instance (and `linkHaar`), so that the spectral side and `Z` live on one measure without a non-definitional instance diamond.
3. The docstring of `action` (L124) "each unoriented plaquette contributes exactly one copy" is literally true for the (x, i<j) labels (`action_eq_geometric`); the identification of those labels with distinct geometric plaquettes needs sides >= 2 (row 698 Point 1, item 3), which every consumer has.
4. Hand lower constant -12 beta c d (row 698 L93, pointwise) versus Lean's -6 beta c d (Jensen): Lean's is sharper; both satisfy `lower`.

Not done here: building or replaying the Lean (the lead replays and prints axioms; the receipt's axiom list shows only propext, Classical.choice, Quot.sound for all 29 exported declarations, which I did not reproduce). This was a check by reading. What stays open on the Wilson TorusData route (the receipt's remaining units, unchanged by this check): the analytic kernel-to-Hilbert-Schmidt unit, the rectangular operator T_R (positive, nonzero, compact, HSNormLE 1; row 1506), and the periodic kernel identity giving the bridge; the physical seed is open.

Ended 2026-11-25T01:13Z (date -u).
