# Third coherence review: scale-ladder note

Provenance: a fresh-context agent of the same model family as the note's author (Claude Opus 5.5). This is not an independent model lineage. Reviewed file: `docs/SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md`, in worktree /home/user/wt-9702, branch claude/scale-ladder-20261018, base commit ddd20e99c7. Edits are uncommitted, as instructed.

Sources read: AGENTS.md; SCIENCE_WORKFLOW.md; the whole note; FINDINGS.md for C7, C8, C9, C10, C11, B26 and B20; REPORT.md for C7, C8, C9, C11, B26 and B20 (C10_check is empty); and the review-2 edits.py.

## Checks

- `python3 docs/audit/scripts/repo_invariants_check.py --check --enforce-links`: PASS (rows=5722, link_violations=0, class_f_violations=0).
- `python3 scripts/scale_ladder_corner_fermion_cross_rung_invariants_2026_10_18.py`: TOTAL PASS=20 FAIL=0, 1 min 26 s. The runner was not touched.
- No markdown links were added. Every new reference to C9, C10, C11, B26 or C8 is plain text.

## Edits (old → new)

1. Item 7 header: "(C1–C4b, C6–C9, C11, B24–B26; each checked …)" → "(C1–C4b, C6–C11, B24–B26; each checked …, except C10, which is unchecked)". The C10 bullet sat under a header that said every item was checked.
2. C9 ruler sub-bullet: added "(an affine field-space model, not a relabelling of a periodic field)". This is the C9 check's scope correction (b).
3. C9 enlarged-generator sub-bullet: added "The examples are abstract graded algebras; realisation by lattice relabellings is open." Source: the C9 check's sharpening 1 and C9's "Not covered" list.
4. C10 label: "(C10; unchecked)" → "(C10; campaign evidence, unchecked)". This matches the labels of the neighbouring bullets.
5. C10 uniform background: "At a uniform background" → "At a uniform background (a winding sector)". The C10 Theorem A1 caveat requires a winding sector.
6. C10 cheap closure: "the constraints factorise." → "…factorise, and this is C9's moved-background mechanism carried over to constraints". Source: the C10 "Relation to C9" line.
7. C10 jets: "A broader window has flat first-order jets; higher order is open." → "A broader shift-invariant window has flat first-order jets; higher order, and so whether an exact finite-range solution exists, is open". This matches the C10 table, window (1,2).
8. C8 bullet: "(its tastes stay on B24 lattices)" → "… (120-word census)". The census size bounds the claim.
9. C8 bullet: "A numerical observation (sketched argument, not a proof) is that every O-symmetric letter tested …" → "Every O-symmetric letter tested … ; C8 observed this numerically, and C11 below proves it for isolated doublets." C11 made this statement stale; C11 is exact given F1–F5.
10. C11 4-fold sub-bullet: "a 4-fold level at ±k*" → "a 4-fold level at ±k* made of both doublets (D₊⊕D₋)". Added: "This replaces, for generic letters, the equal-speed, opposite-chirality Dirac point of the B20 word class." This separates these levels from G3/2 4-fold levels and states the link to B20.
11. C11 winding sub-bullet: "The zero-winding lemma extends to these letters. So such a node … The doubling obstruction therefore reaches these levels too." → "(B20's L3) extends exactly to words in these letters. So a same-chirality node forces a compensating ∓2 charge … on the basic translation lattice … B20's conditional obstruction therefore reaches these levels too. The opposite-chirality ones generically have two speeds…; only v₊ = −v₋ escapes both, and it needs tuning."
    - "Doubling obstruction" could be confused with the gap-based doubling corollary. The obstruction meant is B20's chirality obstruction.
    - The old text did not cover the opposite-chirality case. The new text follows the C11 check's (e) implication.
12. Net reading: "(C3) it has no exact lattice form with the continuum spectrum" → "(C3) with field-independent structure constants and one generator per momentum it has no exact lattice form…".
    - Added: "The structure-function examples that evade this do so where closure is automatic (C9's frames at backgrounds the relabellings move) or cheap (C10's 1D model with no local degrees of freedom; unchecked); for lattice parametrised field theory … exact closure is open (C10)."
    - Reason: C9 and C10 made the unscoped sentence stale. The C9 check explicitly asks for the "field-independent structure constants" and "one generator per momentum" qualifiers.
    - "Only" was avoided because the C9 check calls "help only at moved backgrounds" overstated: the common-zero loopholes and mixed backgrounds remain.
13. Open list, first item: appended "; for lattice parametrised field theory, a finite-range flat Kuchař density beyond first order (C10, unchecked)". This is C10's Open item 1.
14. Open list, new item: "4-fold levels at ±k*: levels with G3/2 content (unscreened, B23), and generic-letter D₊⊕D₋ levels with v₊ = −v₋ (C11; this needs tuning)". Source: the C11 Open list and the C11 check (e).
15. Open list, shift-letter item: appended "(by C11 such letters can only rescale an isolated k* doublet's speed, so they matter through the other nodes and the tastes)". This keeps the item consistent with C11.
16. B20 4-fold lemma (Detail): reordered and rescoped.
    - Old text: "…is an exact isotropic Dirac point… (This is for this word class; with generic symmetric letters the two speeds differ, see summary item 7, C11.) Four-fold G3/2 levels are not covered…, and the conditional obstruction applies to 2-fold doublets only. Screening all 10,174 such levels…".
    - New text: "in this word class, a 4-fold level … is an exact isotropic Dirac point…, and here the conditional obstruction applies to 2-fold doublets only. Screening all 10,174 such Dirac levels… With generic symmetric letters (C11, summary item 7) the two speeds generically differ, and the levels whose two cones share a chirality fall under the obstruction. Four-fold G3/2 levels are not covered…, and levels with spin-3/2 content … are not screened (B23)."
    - Reason: after C11, the unqualified "applies to 2-fold doublets only" was false for generic letters. "Such levels" referred ambiguously to the G3/2 levels of the preceding sentence.
17. B18 taste paragraph: "Enlarged and spectral taste groups (B24, B25, checked) do not change this" → "Enlarged and spectral taste groups (B24, B25) and new letters (B26, C8), all checked, do not change this".
18. Constraint-closure "Consequence" bullet: appended "Both evade the lemma (C9, checked): the structure-function examples sit at backgrounds the relabellings move, where closure is automatic, and the enlarged sets are so far abstract algebras (summary item 7)." The old sentence named both routes as open and did not report C9's result.
19. Information-minimal target status:
    - Old text: "(B17, B18, B20, B23–B25), because each has anisotropic species at its node quasi-energy."
    - New text: "(B17, B18, B20, B23–B26, C8). Each tested step reaches its node quasi-energy somewhere other than at isotropic cones of one speed: a band crossing, or an anisotropic, tilted, flat or other-speed node. By C11 an isolated doublet at ±k* is always an untilted isotropic cone, so the obstruction lies at the other momenta and in the tastes."
    - Reason: the B26 and C8 screens were missing. "Anisotropic species" misdescribed the failures: in B20, 99.1% are band crossings, and B26 and C8 also report tilted and flat nodes.
20. What stays open, "Exact redundancies": "…excluded within field-independent structure constants (C3)." → "…structure constants and one generator per momentum (C3). C9's structure-function evasions sit at backgrounds the relabellings move, where closure is automatic, and for lattice parametrised field theory the naive constraints are anomalous (C10, unchecked)."

## Spot checks of the new bullets against the evidence (no change needed beyond the above)

- **C7.** Matches FINDINGS and the check: π on every 4-cycle, ±π/2 triangles, no O-fixed momentum, the "searched static sectors" wording, the O(t2⁴) margin, and no gauge-equivalent corner-family member. The label (checked) is right.
- **C8.** The counts (69,660 levels, 0 pass) and the scope "among the π/4 exponentials examined" match the check's correction.
- **B26.** The classification (exact; range ≤ 4 in the check), the ~73k words, 0 pass, and the S^{±3} coverage caveat match the check's correction 7. The label (checked) is right.
- **C9.** The 2cos(2π/L) result, the SLAC result, the gap form at a common zero, and L8 (≥ 2 generators at 0, ±1) match the evidence.
- **C10.** The bullets match FINDINGS. The "unchecked" label is correct, and C10_check is empty.
- **C11.** Speed |Σv|, the per-letter values and the ~30% same-chirality share (29–30% with Berry flux) match the evidence.

## Considered and not changed

- **Frontmatter `claim_scope` and Status line.** These cover the note's own theorems (items 1–8 of the scope). Phase-2 lane results are already marked there as "interpretation only". They are listed by topic, which does not include letter classification or the speed law, but the list is a description, not a claim. I left the machine-readable scope unchanged to avoid churn.
- **Premises and the No-Go gate.** These concern the note's own theorems; none of C7–C11 or B26 enters them. N6/N7 already say that the common-speed closure results are conditional and leading-order. No contradiction was found.
- **Summary item 5** ("No tested word passes … 69,894 … 10,174"). This is still accurate for B20 and B23. The B26 and C8 screens are reported in item 7 and now also in the target status, so I did not duplicate them here.
- **Answer item 4** ("Beyond leading order the lattice relabellings do not close"). It concerns linear relabellings about the vacuum, which C9's L4 says stand. It is still correct.
- **C9 common-zero sub-bullet.** It is already scoped to "continuous structure functions" and "linear relabellings about the vacuum". The remaining loopholes, (S) degenerating at linear order and 2 ∉ S, are not spelled out. I left them out to keep item 7 short; the Open list covers mixed backgrounds.
- **Length of item 7.** It is long, but each bullet carries a distinct result and label. Tightening it further would have meant dropping content, so I made only the scoped edits above.
- **The C11 statement "exact, given numerically certified model facts".** This label is right: F1–F5 are certified numerically to machine precision.
