# RESULTS — block 11: the exceptional locus of the three-body term (2026-09-15)

**Deliverables (branch `physics-loop/admissibility-induced-law-block11-three-body-exceptional-locus-20260915`, stacked on block 10):** the note `docs/ADMISSIBILITY_RULE_THREE_BODY_TERM_EXCEPTIONAL_LOCUS_EXACT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md`; the runner `scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py` (20 checks, 11 mutations, exact algebra, ~3 s); the pinned cache; controls A and C–F with outputs; `GOAL_block11.md`; `CHECKER_block11_findings.md`; this record.

## Result, in one paragraph
The three-body normalizer term of the six-axis product rule — the term blocks 08–10 found in every formation law with a three-element recorded set — vanishes at exactly six points of the positive octant up to scale: the constant rule; `p = q = t* r` with `t*` the positive root of `t³ − 3t² − 6t − 1` (in `(4, 5)`); `(p, q) = (1, ρ) r` and `(ρ, 1) r` with `ρ` the positive root of `x³ − 3x² − 15x − 19` (in `(6, 7)`); and the mirror pair `(σ_1, σ_2) r`, `(σ_2, σ_1) r` with `σ_1 ∈ (1, 2)`, `σ_2 ∈ (6, 7)` the positive roots of `x⁶ − 6x⁵ − 3x⁴ + 4x³ − 3x² − 6x + 31`, linked by an explicit quintic `p = ψ(q)`. The three points on the lines come from the collapse of the six-menu to a three-letter quotient where pair-additivity is one cubic; the off-line pair has no known structural reason. Completeness is exact elimination (two witness polynomials, a lex elimination basis, root isolation, and the reduction of all 16 distinct third-difference numerators modulo each minimal polynomial). The two-body term never vanishes at a nonconstant triple (X1). At the five nonconstant exceptional points the three-body normalizer factorizes into nonzero pair terms, so blocks 09–10's Markov-graph conclusions hold there through the pair part; the declared triples `(3,1,2)`, `(5,2,4)` are off the locus, so every three-body statement of blocks 08–10 is unconditional there.

## Certificate
- Runner: `TOTAL: PASS=20 FAIL=0`; 11 mutations each in its family; no floating-point literal, conversion or numeric-root call; classical names only under Prior art and Imports.
- Refuting pass (`CHECKER_block11_findings.md`): the candidate pairs excluded by exact interval enclosures (control C) and the collapse-line factorizations by direct enumeration (control D) agree with the elimination route.
- Claim type `bounded_theorem`; status `bounded-support`; trace `upstream_support`; audit required.

## Not claimed
A structural reason for the off-line pair; the loci for `k ≥ 4`; zero weights; other menus.
