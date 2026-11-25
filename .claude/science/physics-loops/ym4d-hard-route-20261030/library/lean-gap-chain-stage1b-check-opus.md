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

