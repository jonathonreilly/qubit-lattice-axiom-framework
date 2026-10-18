# Review of the B26 + C8 consolidated note (fresh-context, same model family)

**Provenance.** I am a fresh-context reviewer of the same model family (Claude Opus 5.5) as the B26 and C8 workers, both checkers and the note writer. I am not independent of that family.
- **What I read:** the note, the runner, `B26_new_shift_letters/FINDINGS.md`, `B26_check/REPORT.md`, `C8_beyond_permutation_letters/FINDINGS.md`, `C8_check/REPORT.md`, the C11 sibling note and `NOTE_C11_review/REVIEW.md`.
- **What I checked by hand:** the proofs.
- **My script:** `rev_probes.py` execs the runner read-only, so it shares the runner's model build. It then tests four statements the runner does not test.

Nothing was staged, committed or pushed. The citation graph and manifest were not regenerated.

**Verdict: approve with changes applied.** I found no mathematical error in any load-bearing step.
- **Retitle.** The title overclaimed, so I renamed the file and updated its claim_id (edit E1).
- **One wrong side remark:** the claim that the class excludes every on-site letter except the identity. A0 is on-site and is in the class (E7).
- **Two places dropped A0 letters** when reducing D_Π words to "old words" (E2, E8).
- **One unclear gauge-invariance sentence:** it mentioned "μ-terms" in τ, and there are none (E6).
- **Label fixes:** the broken exact Π relation is exact only for the witness; for the other words it is a sample count. The reduced-word filter is now defined in the note, with both counts given (E3, E4, E9).
- **Smaller fixes:** a Hermitian-involution precision (E10), a screen coverage caveat in claim_scope (E3), title cross-references in Scope (E11), a provenance line (E5), and runner docstring and label fixes (R1–R4).

## Files
- **Note:** renamed. All edits are in place; the file is untracked, so I used `mv`, not `git mv`.
  - Old: `/home/user/wt-lanes/docs/CORNER_FERMION_COVARIANT_MONOMIAL_SHIFT_LETTERS_ARE_ONLY_THE_DIAGONAL_SHIFT_POWERS_AND_THEIR_ANTIPODAL_TWINS_AND_MOMENTUM_SHIFTING_OR_ANTIUNITARY_LETTERS_REDUCE_TO_OLD_WORDS_BOUNDED_THEOREM_NOTE_2026-10-18.md`
  - New: `/home/user/wt-lanes/docs/CORNER_FERMION_COVARIANT_MONOMIAL_SHIFT_LETTERS_ARE_ONLY_THE_DIAGONAL_SHIFT_POWERS_AND_THEIR_ANTIPODAL_TWINS_AND_THE_SETTLED_MOMENTUM_SHIFTING_AND_ANTIUNITARY_SUBCLASSES_REDUCE_TO_OLD_WORDS_BOUNDED_THEOREM_NOTE_2026-10-18.md`
  - The new basename has 224 characters. The longest existing basename in `docs/` has 238.
- **Runner:** `/home/user/wt-lanes/scripts/corner_fermion_symmetric_shift_letter_classification_2026_10_18.py`. Only docstring and label text changed (R1–R4).
- **References to the old name:** I searched `/home/user/wt-lanes` (md, py, json, yaml), the campaign directory and the supervisor scratchpad. The only reference was the runner's `Companion:` line, which is now updated.
- **Supervisor action:** stage the new path, and make sure the old path is not staged. Regenerate the graph and manifest with the owning tools.
- **Diffs in this directory:** `note.diff`, `runner.diff`.

## Runs
- **Before edits**
  - Default: `TOTAL: PASS=51 FAIL=0`, 16.7 s wall.
  - `--slow`: `TOTAL: PASS=52 FAIL=0`, 22.9 s.
- **After edits**
  - Default: `TOTAL: PASS=51 FAIL=0`, 16.5 s (`runner_default_after.log`).
  - `--slow`: `TOTAL: PASS=52 FAIL=0`, 18.5 s (`runner_slow_after.log`).
  - Output is line-for-line identical to the pre-edit runs, apart from the reworded 5.8 label.
- **Every number the note quotes matches the logs:**
  - 1.7 counts: 324/1,500/4,116/8,748 seeds, giving 6/10/14/18 letters;
  - residuals: ≤ 2e−16 for the identities; 0.71 and 1.41 for the 2.3 alternatives;
  - 2.7 maximum deviation: 6.6e−16 (default) and 9.8e−16 (`--slow`); the note's "7e−16" is the default figure;
  - orbit, piece and G0 counts, 4 admissible pairs and 16 words;
  - 5.8: 79/79 (default) and 112/112 (`--slow`);
  - 5.9: 80/80 and 0/80 (default); 160/160 and 0/160 (`--slow`).
- **New in the note:** the non-reduced 5.8 counts, 90/112 broken by default and 81/126 with `--slow`. The note now reports these as 22 of 112 and 45 of 126 surviving.
- **Reviewer probes** (`rev_probes.py`, log `rev_probes.log`): all PASS.
  - **P1, gauge law.** 5 random gauges × 48 lifts: λ′ = λ + μ + R_hᵀμ and τ′(c) = τ(c) + ε(c) + ε(R_h c) + const. τ has no μ-terms. This supports E6.
  - **P2, filter is local.** `hygienic(E₊ S⁻¹ Rt S E₊ S)` is True, yet the word equals −i·S, which is E-free. This supports E9.
  - **P3, A0·R_L is not an involution.** (A0 R_L)² = −Rt R_L, which is not a scalar. So z·A0R_L and z·R_LA0 are not involutions, and the "P R_L P⁻¹ is ±R_L or ±Rt" corollary of the a·R_L·b lemma follows exactly.
  - **P4, Hermiticity needs commutation.** For a non-commuting symmetric projector, R_L P + (1 − P) is not Hermitian. This supports E10.
- **`scripts/vocab_lint.py --report-only`** on the note: 0 violations.
- **`repo_invariants_check.py`:** not run. It measures git-tracked state only, and the note is untracked. I checked the links by hand instead (Hygiene).

## Mathematics (checked by hand)
- **Global-sign composition.** Correct.
  - Δ = G_g G_h G_gh⁻¹ has the affine form (−1)^{μ·v+ε(c)} and covers the identity.
  - The PSG equations make every lift preserve every signed hopping term, so Δ commutes with H. A diagonal ±1 that commutes with H is constant on each connected component. The graph is connected: on-site edges join the 12 corners, and links run along all three axes.
  - So Ad(G) is a true representation. Since O^ab = Z₂, χ ∈ {A1, A2}. Runner 1.1a tests the composition directly on all 24² pairs.
- **One column fixes X.** The displayed formula X|0,Rc⟩ = χ⁻¹z(−1)^{τ_g(c)+λ_g·a+τ_g(i)}|Ra, Ri⟩ follows from X G_g = χ(g)⁻¹G_g X. The 12 corners form one O-orbit (24/|Stab| = 12).
- **Stabiliser.** Correct.
  - For c = {d, e}, h_c swaps d and e and negates the third axis, so its fixed corners are exactly c and −c.
  - Its +1 eigenspace is R·f_c, and f_c is primitive, so the fixed lattice vectors are Z·f_c.
- **Character restriction and the sign facts.** Correct.
  - With i = c, the τ terms cancel and (F-a) gives χ(h_c) = +1. Since A2(h_c) = −1 (h_c's axis permutation is a transposition), χ = A1.
  - With i = −c, (F-b) gives χ = A2.
  - Gauge invariance holds. E6 states the exact transformation law, which P1 confirms. Combined with runner 0.1 (loop rank 22 = 36 − rank COB), it is a property of the model.
- **Existence and uniqueness.** Correct. S^t and A0·S^t have the required supports and characters, and a covariant X is fixed by one column.
- **"Any displacement range".** Justified: no step uses a bound on the displacement or on the entries.
- **Twisted-average enumeration.** It is a valid exhaustive search inside the box. A covariant monomial X with c_xy-column z|a,i⟩ is proportional to P_χ(|a,i⟩⟨0,c_xy|), because only Stab(c_xy) contributes to that column. So the check is not tautological.
- **Frobenius remark.** Correct. The support space is induced from the sign character of {1, h_c}, so ⟨χ|_Stab, sign⟩ is 1 for exactly one of A1 and A2.
- **Identities.** All correct. (I1) follows from Theorem 1 plus a scalar; (I4) holds because A0² is a scalar; (I5) restates (I3).
- **Even-A reduction.** Correct.
  - A_a X A_b = A0 S^a X A0 S^b = −(A0S^aA0⁻¹)(A0XA0⁻¹)S^b = −S^{−a}X̃S^b, using A0 = −A0⁻¹.
  - The prefactor is z = ±1 for general on-site fills and z ∈ {±1, ±i} for PC fills (from 2.6).
  - In n_eff, counting the A0 inside A_a "to the left of its own S^a" matches the formula and `neff()`.
- **D± swap.** Correct: Schur's lemma with D₋ ≅ A2 ⊗ D₊, both of multiplicity one at ±k*.
- **Q ∈ {0, Π}.** Correct.
  - G_g T_w G_g⁻¹ = (−1)^{λ_g·w}T_{R_gw}; the sign cancels in conjugation.
  - The C4 rotations about z and x give Q = (q, q, q) with 2q ≡ 0.
  - Q = Π monomial letters follow from Theorem 1 applied to D_Π X.
- **D_Π relations.** Correct. f_c has even coordinate sum, and R_L hops by unit vectors.
  - **Defect fixed:** moving the D_Π letters out of a word of D_Π·S^a and D_Π·A0·S^a letters leaves A0 letters. The statement "± an old word" was therefore incomplete. It is now "± a word in the old letters and A0, hence z times an old word when A1, by the even-A reduction" (E2, E8).
- **Doubled-cell orbits.** Consistent: 4·12 + 2·24 = 96 modes per doubled cell. The stabiliser orders are 2 and 1 in the group of 192 elements.
- **G0 and pure-permutation words.** G0 = 2·8²·4⁶ = 524,288 letters, with 8 translation-invariant (2 perm parts × 4 phases). The pure-permutation argument is exact: a product of monomials is a nonzero monomial, with the product character.
- **a·R_L·b lemma.** Correct.
  - With Smith invariants all 1, {x : Ax ∈ Zᵐ} = Z¹² + ker_R(A), since V is unimodular.
  - The common-phase property of the kernel directions makes the U(1) case one word per pair up to a scalar.
  - The ℤ₄ enumeration gives 4 names × 4 phases.
  - A0 R_L A0 = −Rt is correct.
  - The P R_L P⁻¹ corollary follows exactly (P3).
- **Antiunitary reduction.** Correct with its proviso.
  - U(e^{iθ}ψ) = e^{−2iθ}λ(e^{iθ}ψ), and (VK)² = VV*.
  - The reality of S, R_L, Rt, A0 and the lifts makes V* the slot-conjugated word.
  - The symmetric on-site algebra is conjugation-closed because the U_R are real.
  - The A letters in V·V* pair up, so the even-A reduction applies.
  - The pairing follows from K(VV*)K = V⁻¹(VV*)V.
- **exp(π/4·A0).** Correct, and only T-covariant. (1 − A) is not a multiple of (1 + A).
- **E± identities.** Correct: they all follow from R_L² = 1, R_L(k+Π) = −R_L(k), and R_L real and Hermitian, which gives E(k)ᵀ = E(−k).
- **exp(iπ/6·R_L) ≠ z·E₊ⁿ.** Correct for every z, since tan(π/6) ≠ tan(nπ/4).
- **Precision fixed.** "(1 + iX)/√2 unitary ⇔ X² = 1" is stated for unitary X. The context is therefore Hermitian involutions, and R_L P + (1 − P) is Hermitian iff [R_L, P] = 0. The original "no involution" was too broad; it now reads "no nontrivial … Hermitian involution" (E10, P4).
- **Side remark fixed.** "The class excludes … every on-site letter except the identity" was false: A0 = z·A0·S⁰ is on-site and is in the class. It now reads "except multiples of 1 and A0" (E7). The B26 check's sentence was about the A1 part only.

## Labels
- **Title, retitled (E1).** "Momentum-shifting or antiunitary letters reduce to old words" read as a universal claim, but it is not settled for:
  - displaced doubled-cell letters;
  - mixed words with two or more link letters (sampled only);
  - multiplets with Q outside π{0,1}³ mixed with link letters;
  - non-monomial doubled-cell letters;
  - antiunitary V outside a conjugation-closed palette.

  The new title is "… and the settled momentum-shifting and antiunitary subclasses reduce to old words". The Scope bullets for Theorem 4 and Proposition 5 now say that they are the subclasses the title means (E11). The claim_id, H1 and the runner's `Companion:` line are updated.
- **Spectral Π-taste.** It was already labelled numerical. The population is now defined: "reduced" means the runner's local `hygienic()` filter. The note says the filter is local and was fixed post hoc, with the P2 example (E9).
- **Broken exact Π relation.** It was headed "(exact)", but "fails for every sampled reduced E-word" is a sample count.
  - Now: exact for W(k+Π) = (−1)^{n_R}W′(k) and for the witness E₊·S; the sample count is labelled as such (E4, E9).
  - The non-reduced counts are now reported in the note. The disclosure said "both counts are now reported", but only the runner's detail line had them.
- **Not-rechecked C8 items.** Already labelled correctly: the Q-multiplet paragraph and the 20,000-word sample are "by hand or worker-only, not rechecked", and the P R_L P⁻¹ statement is "not re-run".
- **Screens.** Already labelled as cited, numerical negative searches, not no-go theorems, with the S^{±3} caveat in the Screens section. claim_scope lacked the caveat, so I added it (E3).
- **No physical identification** is made anywhere.

## Runner review
- **Self-contained.** It imports only `os`, `collections`, `itertools`, `sys`, `time`, `numpy`, `scipy` and `sympy`. Campaign packs and the C11 runner appear only in the docstring, as provenance. The C11 runner path exists and is tracked.
- **Not tautological.**
  - 1.1a and 1.4 compute from the GF(2) lifts.
  - 1.7 identifies the averaged letters against independently built `Spow` (orbit propagation).
  - 2.7 compares numerical Bloch products with the symbolic `reduce_word` output.
  - 3.4 and 5.8 compare Bloch matrices at shifted k.
  - 3.8b–d enumerate.
  - 4.4 tests AB versus BA isospectrality, a genuine fact, not code-derived.
  - Mild: 2.7's n_eff check compares two of the runner's own formulas. The deviation check in the same line is the load-bearing part.
- **Disclosed post-hoc fixes.** Honest and adequate.
  1. The restriction to reduced words after 52/63 is a scope restriction, disclosed with both counts.
  2. The filter extension after E₊·Rt·Rt·E₋·o·S = o·S excludes a word that really is E-free, so it is legitimate. It is still post hoc, and the filter stays local (P2). The note now says so and states that the counts are for the filter as written.
  3. The sample enlargement from 200 to 300 meets a pre-declared size floor, not an outcome criterion.

  I could not verify the numbers of the failed first runs (no logs are kept), but they are consistent with the current non-reduced counts.
- **Runtime.** The docstring said "default ~1 min". Measured: about 16 s default and 18–23 s `--slow`. Fixed (R2).

## Hygiene
- **Front matter.** The fields match the C11 sibling: claim_id, claim_type, claim_scope, upstream_dependencies, runner.
- **Upstream dependencies.** All three claim_ids resolve to tracked notes on this branch.
- **Markdown links.** All four targets exist and are tracked: the long-wavelength note, the eight-node step note, the C11 speed-law note and MINIMAL_AXIOMS. There are no links to `.claude/` files or to the scale-ladder note of PR #9702. `.claude/` paths appear only in backticks, as in the sibling.

## Edits (old → new)

### Note
- **E1, retitle.**
  - claim_id `…_and_momentum_shifting_or_antiunitary_letters_reduce_to_old_words_…` → `…_and_the_settled_momentum_shifting_and_antiunitary_subclasses_reduce_to_old_words_…`
  - H1 "…, and momentum-shifting or antiunitary letters reduce to old words" → "…, and the settled momentum-shifting and antiunitary subclasses reduce to old words"
  - Filename renamed to match.
- **E2, claim_scope (Theorem 4).** "so translation-invariant words are +- old words and the D_Pi relation" → "so translation-invariant words are +- words in the old letters and A0 (z times old words when A1, by the even-A reduction) and the D_Pi relation"
- **E3, claim_scope (screens and E-words).**
  - "… negative searches pass 0." → "… negative searches pass 0; B26's family does not contain every even-A word of length <= 5 (some reduce to S^{+-3} skeletons or adjacent slots)."
  - "(exact, witness E+ S);" → "(exact for the witness E+ S; for every sampled locally reduced E-word, a sample count);"
- **E4, Status.** "the exclusion of exp(π/4·A0), the E± identities and the broken exact Π relation." + "**Numerical:** the spectral Π-taste of E-words, which is a sample statement." → "the exclusion of exp(π/4·A0), the E± identities, the relation W(k+Π) = (−1)^{n_R}W′(k) and its breaking by the witness E₊·S." + "**Numerical (sample statements):** the spectral Π-taste of E-words, and the breaking of the exact Π relation in every sampled reduced E-word."
- **E5, Provenance.** "None of these is an independent human reviewer, and no reviewer of this note has run yet." → a bullet "Reviewed by a fresh-context same-family agent (`NOTE_B26C8_review`), whose scoped edits are applied here." + "None of these is an independent human reviewer."
- **E6, gauge invariance.** "λ_h·f_c changes by an even amount, because h fixes f_c. τ_h(c) + τ_h(−c) changes by 2ε(c) + 2ε(−c) plus μ-terms of the same parity. The runner also confirms this on three random gauges." → "the lift of h becomes (λ_h + μ + R_hᵀμ, τ_h(c) + ε(c) + ε(R_h c)), up to the global sign. So λ_h·f_c changes by 2μ·f_c, because h fixes f_c, and τ_h(c) + τ_h(−c) changes by 2ε(c) + 2ε(−c) (plus 2 for a global sign flip), because h fixes c and −c. The runner confirms the parities on three random gauges."
- **E7, Remarks.** "every on-site letter except the identity" → "every on-site letter except multiples of 1 and A0"
- **E8, Theorem 4(b).** "So it is ± an old word." → "So it is ± a word in the old letters and A0, and, when its character is A1, z times an old word by the even-A reduction."
- **E9, Proposition 6.**
  - The heading "Broken exact Π relation (exact)" → "(exact for the witness; sampled otherwise)"; "(exact)" added after the W′ relation; "a sample count" added after 79/79 and 112/112.
  - "In the sample it survives only in words whose E letters merge" → "only in non-reduced words (22 of 112 by default, 45 of 126 with `--slow`), e.g. words whose E letters merge".
  - New bullet defining "Reduced" as the `hygienic()` filter (its pairs listed), saying that it was fixed after the first runs and is local, giving the E-free example E₊·S⁻¹·Rt·S·E₊·S = −i·S, and stating that the counts are for the filter as written.
- **E10, Proposition 6.** "No symmetric on-site projector P gives an involution R_L·P + (1 − P)" → "No nontrivial symmetric on-site projector P gives a Hermitian involution R_L·P + (1 − P), since Hermiticity needs [R_L, P] = 0"
- **E11, Scope.**
  - "**Theorem 4** settles:" → "**Theorem 4** settles (these are the "settled momentum-shifting subclasses" of the title):"
  - "**Proposition 5** needs V in a conjugation-closed palette." → "… (the "settled antiunitary subclass" of the title)."

### Runner (text only; no logic changed)
- **R1, docstring line 1.** "antiunitary letters reduce to old words" → "antiunitary letters (conjugation-closed palette) reduce to old words"
- **R2, Usage.** "default ~1 min on 2 threads; --slow enumerates…" → "default ~15 s on 2 threads; --slow (~20 s) enumerates…"
- **R3, `Companion:` path.** Changed to the new filename.
- **R4, 5.8 label.** "only in non-hygienic words, whose E letters merge, e.g. E+ E+ = i R_L" → "only in non-hygienic words, e.g. those whose E letters merge, E+ E+ = i R_L". The non-hygienic set also contains R_L·R_L, Rt·Rt and S·S⁻¹ cancellations.

## Not changed, and why
- **Numbering.** Theorem 1, Theorem 4 and Propositions 5 and 6 leave no Theorem 2 or 3. This is cosmetic, with 14 occurrences, so I left it.
- **The `hygienic()` filter itself.** Changing it would be another post-hoc criterion change and would alter the samples. Instead, the note now states the filter's local scope.
- **"Old-palette word up to a phase" in Proposition 5.** The even-A step is implicit but correct, since V·V* has an even number of A letters. Left as is.
- **"The k* speed of an even-A word is |n_eff|·√2/3".** It rests on the C11 lemma, which is an upstream dependency on this branch.
- **Under-labelled, conservative:** the "every translation-invariant conjugate P R_L P⁻¹" statement is still marked "not re-run". It follows exactly from (e) (P3).
- **The S power check in 2.7.** It checks internal consistency only, as noted above. It is harmless, and the deviation check carries the claim.
- **Not done:** the citation graph and manifest were not regenerated, and nothing was staged. These are for the supervisor.
