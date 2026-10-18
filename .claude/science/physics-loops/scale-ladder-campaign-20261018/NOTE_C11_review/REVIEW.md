# Review of the C11 consolidated note (fresh-context, same model family)

**Provenance.** I am a fresh-context reviewer of the same model family as the worker, the checker and the note writer (Claude Opus 5.5). I am not independent of that family. I read the note, the runner, `C11_generalised_L1/FINDINGS.md`, `C11_check/REPORT.md` and B20's L1–L4, and checked the mathematics by hand. My script `rev_q2_and_kappa.py` reuses the runner's model build: it execs runner Sections 0–3 read-only. It then tests two statements the runner does not test.

**Verdict: approve with changes applied.** I found no mathematical error. The lemma, its proof (Schur, Wigner–Eckart, the ε-relation sign step, path additivity with the A2 labels), the corollaries and the 4-fold claims all hold. I made seven scoped precision edits (nine string replacements):
- one sharpening, which makes "one global κ" exact rather than measured;
- two label fixes, so that the Daleckii–Krein zeros are marked as reducing to a numerical zero;
- one missing premise in the conditional obstruction;
- one undefined symbol (T);
- two small accuracy fixes;
- one provenance line.

## Files
- Note: `/home/user/wt-lanes/docs/CORNER_FERMION_STEP_SPEED_AT_THE_FULL_OCTAHEDRAL_NODE_IS_A_SUM_OF_PER_LETTER_COEFFICIENTS_AND_GENERIC_LETTERS_SPLIT_THE_FOUR_FOLD_DIRAC_LEVEL_BOUNDED_THEOREM_NOTE_2026-10-18.md` (edited, re-staged)
- Runner: `/home/user/wt-lanes/scripts/corner_fermion_generalised_speed_law_per_letter_additivity_2026_10_18.py` (not edited)

## Runs
- **Default, 2 threads:** `TOTAL: PASS=42 FAIL=0`, 47 s (`runner_default.log`).
- **`--slow`:** `TOTAL: PASS=42 FAIL=0`, 109 s (`runner_slow.log`). Every number the note quotes for `--slow` matches:
  - 1,493 isolated levels;
  - 40 + 40 generic and 25 old-palette 4-fold levels;
  - 60 two-fold Berry levels;
  - same chirality in 26/77;
  - the example on-site · exp(iθR_L) · exp(iH) · Z, with |W₃| = 5.0e−3, 2.7e−5, 2.8e−8, 1.8e−10.
- **Default numbers quoted in the note,** all matching:
  - 606 levels;
  - same chirality in 11/33, with upper-pair Chern ±2 on 11/11 and 0 on 22/22;
  - example A0·exp(iH)·R_L·A0·Z with v₊ = 1.1875, v₋ = 1.2227;
  - W₃ = −0.417, −4.1e−3, +4.9e−5;
  - control −0.998;
  - partner distance 1.99, near miss 5.8e−4;
  - generic example v = −0.775 / +0.266.
- **`repo_invariants_check.py --check --enforce-links`:** PASS before and after the edits (`link_violations=0`, `graph_delta=acknowledged`).
- **Reviewer script** `rev_q2_and_kappa.py` (log `rev_q2_and_kappa.log`): both checks PASS.
  - **R1 (proof step 4, the O(q²) scalar):** on 42 isolated 2-fold levels, (s(δ)/δ − |Σv|) at δ = 4e−3 vs 2e−3 has ratio 3.988–4.003. That is O(δ²), so there is no O(q²) splitting. The runner's Richardson step removes exactly this term and so never tests it.
  - **R2:** τ^(±) satisfy τ_xτ_yτ_z = i and are unitarily equivalent to the Pauli triple (error 6e−16).

## Mathematics (checked by hand)
- **Step 1 (Schur).** Correct. At the fixed point, U(R^T k₀ + πλ) = U(k₀) by 2π-periodicity, and U_R^T = U_R^{−1}. A2 ⊗ D_b ≅ D_{−b}, and A2 ⊗ G3/2 ≅ G3/2, so A2 letters map D_b onto D_{−b}.
- **Step 2 (Wigner–Eckart).** Correct. Differentiating gives U_R Σ_j R_ij ∂_jU U_R^T = χ ∂_iU. This matches the runner's `t1_triples`, whose row-major vec convention gives ρ_out Y ρ_in⁻¹. The relation P U†∂U P = u* P∂U P holds because P U† Q = (Q U P)† = 0.
- **Step 3 (additivity and ε sign).** Correct.
  - The telescoped sum W†∂W = Σ V_j† U_j†∂U_j V_j is exact.
  - The label b_j = a ∏_{l>j} χ_l is the doublet entering letter j from the right.
  - X_j†τX_j is a Hermitian T1 triple. Because X_j is unitary D_a → D_{b_j}, c² = 1, and the product relation gives c² = c, so c = 1.
  - It is right that F4's one-dimensionality alone would allow −τ.
- **Step 4 (cone).** Correct. Sym²T1 = A1 + E + T2 and End(E1/2) = A1 + T1 share only A1. R1 confirms this numerically.
  - The original text attributed the global κ to a runner convention ("up to the orientation convention of τ … the runner fixes that convention once"). In fact it is exact: the ε relation fixes τ up to unitary equivalence, including orientation. Edited (E3).
- **Corollaries.** Correct.
  - Composition and inverse follow from the same telescoping.
  - The corollary does not need an even word or an isolated level, since it is an identity of compressed U†∂U.
  - v_{A0} = 0 holds because A0 is constant.
  - n_eff: "#A0 to the left, counting the letter's own A0" equals (−1)^{#A0 strictly to the right} because the total A0 count is even. This matches b_j, and the runner's counter (`nA += 1` before use) implements it.
- **4-fold claims.** Correct.
  - The no-mixing claim follows from F5 (E1/2* ⊗ E5/2 = A2 + T2).
  - The "two opposite labels at every letter" claim follows from b_j.
  - Under-claim, not changed: the total upper-pair charge ±2 for same-sign levels follows exactly from the first-order block structure. The upper pair is the two upper cone bands, separated from the lower pair by 2|v_slow||q| ≫ O(q²). FHS confirms it, but it is not only numerical.
- **W₃.** Correct.
  - Additivity and homotopy invariance hold for maps T³ → U(12).
  - exp(iH(k)) is homotopic to 1, and H is Bloch-periodic.
  - The A_i of diagonal letters commute.
  - R_L and Rt are Hermitian with square 1, so they are reflections.
  - Every named letter, A0·exp(iH) and Z are in the class.
- **F2.** The order statistics {1:1, 2:13, 3:8, 4:6, 6:8, 8:12} are GL(2,3)'s.
  - Among the four central Z₂-extensions of S₄: S₄×Z₂ and the extension with a split A₄ part have no elements of order 8, and 2O has one involution.
  - So the identification is sound.
- **Claim labels.**
  - F1–F5 are numerical.
  - The lemma is exact given F1–F5.
  - The obstruction is conditional on Bessho–Sato and on the T-fixed set.
  - Two overclaims were in the letter-value labels. "Exact for functions of R_L by Daleckii–Krein" in fact reduces exactly to P∂R_L P = 0, which is itself numerical (2e−16). Edited (E1, E4).

## Runner review
- **Self-contained.** It imports only `os`, `itertools`, `sys`, `time`, `numpy` and `scipy.linalg.schur`, and has no `.claude/` or repository imports. Campaign scripts appear only in the docstring, as provenance.
- **Load-bearing checks are not tautological:**
  - 4.3 compares the analytic per-letter path sum (`predicted`, using letter derivatives and the τ frames) entrywise against a whole-word central finite difference, which uses no product rule.
  - 4.5 uses direct diagonalisation.
  - 4.2 compares overlap-tracked labels with the b_j formula.
  - 2.1 tests step 3 directly on random intertwiners.
  - 6.2 and 6.3 use whole-word finite differences at tuned levels.
  - 4.6, 6.6 and 6.7 use FHS Berry flux, which needs no frame.
- **Expected values.**
  - √2/3 per S (3.5, 5.1, 5.2) is an external constant from B20, not runner output.
  - n_eff is counted from the letter names, independently of `predicted`.
  - KAPPA is measured in 4.6 and reused in 6.6. That is legitimate: one global constant, measured once.
- **Minor redundancy, not changed:**
  - F4's "−τ violates it" is implied by "τ satisfies it".
  - 4.4 reuses 4.3's matrix M.
  - 6.7 overlaps 6.6.
  - None of these inflates a claim.
- **Check 7.3, post-hoc example change.** It is disclosed accurately in the code comment and in the note. The first run failed on the shortest same-sign word (partner distance 5.8e−4 < 1e−3). The threshold was kept, and the selection rule was changed to "length ≤ 5, largest partner distance".
  - Consequence: 7.3 is now an existence check over the sample, "some sampled same-sign level has no partner level within 1e−3", not a test of a pre-fixed example.
  - That matches what the note uses it for, a witness. The near miss is reported as a caveat.
  - The selected distances (1.99 default, 1.25 slow) are far from the threshold. Acceptable as disclosed.
- **Example selection.** Only levels with gap[4] > 2e−2 at k₀ enter, so k₀ has no other level at the node quasi-energy. This supports the premise added in E5.

## Repo hygiene
- **Front matter.** The fields (claim_id, claim_type, claim_scope, upstream_dependencies, runner) and the Date / Type / Status / Provenance header lines match the 2026-10-18 siblings, for example the eight-node and C6 notes.
- **Upstream dependencies.** Both exist:
  - the long-wavelength 10-17 note;
  - the eight-node 10-18 note, on this branch, from commit f83881ca5f.
  
  Their cited content is present: ±k* are the two O-fixed momenta, and the eight-node note has the S, R_L, √2/3 and E1/2 + E5/2 + 2 G3/2 statements.
- **Links.** The note links only to those two notes and to `MINIMAL_AXIOMS_2026-06-29.md`. There are no links to the scale-ladder note (PR #9702) or to `.claude/`; `.claude/` paths appear only in code spans.
- **Citation graph.** No links or dependencies changed. The manifest stores only `deps_hash` and `out_degree`, so it was not regenerated. I re-staged the edited note with `git add`. Nothing was committed or pushed.

## Edits applied to the note (old → new)
1. **E1, claim_scope, letter values.**
   - Old: "R_L, Rt, exp(+-i pi/4 R_L), exp(i theta R_L) and symmetric on-site letters: 0 (exact for functions of R_L by Daleckii-Krein)"
   - New: "… : 0 (numerical for R_L and Rt; functions of R_L or Rt reduce exactly to that zero by Daleckii-Krein; on-site letters exactly 0)"
2. **E2, claim_scope, obstruction.**
   - Old: "a same-chirality 4-fold node at k* with no level at -k* at its quasi-energy forces"
   - New: "… with no other level at +-k* at its quasi-energy forces"
3. **E3, proof step 4.**
   - Old: "The Berry charge of a cone i(Σv)(q·τ) is sign(Σv) up to the orientation convention of τ. The runner fixes that convention once, by Berry flux, as one global κ for both doublets (Section 4.6). ∎"
   - New: "A Hermitian triple with τ_iτ_j = δ_ij + iε_ijk τ_k is unitarily equivalent to the Pauli triple: the ε relation fixes the orientation, τ_xτ_yτ_z = i. So the Berry charge of the cone i(Σv)(q·τ) is κ·sign(Σv), with κ = ±1 set only by the Berry-flux orientation and eigenphase conventions, and the same for both doublets at both ±k*. The runner measures κ = +1 (Section 4.6). ∎"
4. **E4, letter table, E± / exp(iθR_L) row status.**
   - Old: "exact for functions f(R_L) by Daleckii–Krein: R_L(k₀) is a scalar r on D±, so P∂f(R_L)P = f′(r)·P∂R_L P = 0"
   - New: "exact reduction to the numerical R_L zero, by Daleckii–Krein: R_L(k₀) is a scalar r on D±, so P∂f(R_L)P = f′(r)·P∂R_L P = 0; likewise f(Rt) = A0·f(R_L)·A0⁻¹". The row includes exp(0.9i·Rt), which is not a function of R_L.
5. **E5, Implication, compensating charge.**
   - Old: "(conditional also on the T-fixed set of the basic translation lattice being {±k*}, from B20's L4). Suppose a same-chirality 4-fold node at k* carries ±2, and −k* has no level at the same quasi-energy."
   - New: "(… from B20's L4; T ⊂ O is the tetrahedral rotation group). Suppose a same-chirality 4-fold node at k* carries ±2, k* has no other level at that quasi-energy, and −k* has none either."
   - Why: a coincident G3/2 or other level at k* would change the T-fixed net charge. T was not defined anywhere in the note.
6. **E6, N5 wording.**
   - Old: "points whose little group does not contain T (B20's L4)"
   - New: "points whose little group's rotation parts do not contain the tetrahedral rotation group T (B20's L4)", B20's exact wording.
7. **E7, small accuracy fixes:**
   - the generic row "in 8/8 sampled letters" → "in 8/8 sampled letters (6 exp(iH), 2 A0·exp(iH))", since the row is labelled A1 but the runner's 8 include 2 A2 letters;
   - "Its W₃ on midpoint grids N = 8, 12, 16 is 0.42, 4.1e−3 and 4.9e−5" → "Its |W₃| …", since the signed values are −0.417, −4.1e−3, +4.9e−5.
8. **Provenance.** Added the bullet "Reviewed by a fresh-context same-family agent (`NOTE_C11_review`), whose scoped edits are applied here."

## Not changed, and why
- **The R_L zero is plausibly exact by I·K.** The long-wavelength note says the model is "nonrelativistic with I·K". R_L is real and inversion-symmetric, so an I·K-type antiunitary symmetry at ±k* would forbid a q·τ term in R_L. This is not verified, so the label stays numerical. It is a possible upgrade for later.
- **The total charge ±2 is exact at first order** (see Mathematics). Leaving it labelled as confirmed by Berry flux is conservative.
- **The "Independent check" heading.** It is the sibling style, and the section states that the check is same-family.
- **Runner.** No change needed. Redundant checks were left as they are; removing them would alter the PASS count and gives no correctness gain.
