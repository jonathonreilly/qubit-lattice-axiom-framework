---
claim_id: admissibility_rule_three_body_term_exceptional_locus_exact_classification_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the supplied positive six-axis product rule modulo scale: six explicit pair-additive three-neighbor log-normalizer constructions, exact pattern values, polynomial factorizations, isolating intervals and sufficiency reductions. Exhaustive classification and exclusion of other points are deferred, with their original proof preserved in history. The p=q family factors through three unsigned axes; p=r retains six letters. At the five displayed nonconstant points the pair component is nonzero. Opposite-corner single-site specifications coincide there; this does not establish equality or distinctness of infinite laws. Infinite-law discussion requires c < 1/3."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
  - admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_bounded_theorem_note_2026-09-15
runner: scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py
---

# Six pair-additive constructions for the three-neighbor normalizer of the supplied six-axis rule

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact algebra; conditional on the named supplied readings; unaudited)

## Result up front

The supplied six-axis product rule has five explicit nonconstant parameter
settings at which the three-neighbor log normalizer is pair-additive, in
addition to the constant rule. This note constructs those six points and
checks the pattern values and exact polynomial reductions. On `p=q` the
rule factors through three unsigned axes. On `p=r` the six-letter rule
retains the distinction of an antipodal partner, with three triple-pattern
values. Two further displayed points lie off those lines and are exchanged
by a polynomial map on a degree-six algebraic extension.

The live result is sufficiency at these six points, together with the
factorization and elimination identities written below. The original
exhaustive classification, its necessity argument and exclusion of every
other positive point are deferred: the original negative-claim packet did
not complete the required in-domain route coverage. Their full text remains
byte-exact in the history manifest under PR8142 and on its original branch.
No classification PASS is inferred from the identities or from a passing
runner. The five displayed nonconstant points retain a nonzero pair
component. No physical rule or infinite-law distinction is selected.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "blocks 08, 09 and 10 (stacked): 'the third difference of log K_3 nonzero at every nonconstant triple' named as the strongest missing lemma; the derivation campaign's assembly (#8093): the formation-law node's interaction structure"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use the six explicit constructions and their exact sufficiency reductions. Exhaustive exceptional-locus classification and its necessity proof remain deferred in the original archive; no downstream assertion outside the displayed points follows here."
conditional_surface_status: "Exact identities and six sufficiency constructions over algebraic numbers with isolating intervals, conditional on the supplied six-axis product rule; exhaustive locus certification deferred; infinite-law discussion only under the cited construction hypotheses."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "X1 is a factorization over Q; X2 is a structural collapse argument plus a factorization; X3 is exact elimination (resultant, lex elimination basis, exact root isolation, reductions modulo minimal polynomials) executed by the runner; X4 is a two-line consequence; every number is an exact rational or an isolating interval"
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form."

**Readings carried, named, nothing new adopted.** The six-axis menu with orbit
weights `φ = p` (same axis and sign), `q` (same axis, opposite sign), `r`
(orthogonal), `p, q, r > 0`; `Z_k(a_1, …, a_k) = Σ_s Π_i φ(s, a_i)` and
`K_k = Z_k/Z_1^k` (block 08's notation); the mixed differences and the
vacuum-normalized potential of block 10 (its T3: the term of a formation law
on a maximal recorded set of size `k` is `−m_A Δ_k log K_k`). Scaling: `φ` and
`λφ` give the same kernels, so every statement is about `(p/r, q/r)`; the
note writes `r = 1`.

**The five pattern values of `Z_3`.** By the internal symmetry, `Z_3(a, b, c)`
depends only on the pattern of the triple: `V_1 = p³ + q³ + 4r³` (all three
equal), `V_2 = pq(p + q) + 4r³` (two equal, one opposite), `V_3 = r(p² + q²) + r²(p + q) + 2r³`
(two equal, one orthogonal), `V_4 = 2pqr + r²(p + q) + 2r³` (an opposite pair
and an orthogonal third), `V_5 = 3r²(p + q)` (three distinct axes). Executed
against the definition (B1).

**Cross-ratios and pair-additivity.** `log K_3` is pair-additive (a sum of
functions of pairs) iff every cross-ratio
`CR_c(a, a'; b, b') = K_3(a, b, c) K_3(a', b', c) / (K_3(a, b', c) K_3(a', b, c))`
is independent of `c`; each third difference `Δ_3 log K_3` is the logarithm of
a ratio `CR_c/CR_{c'}`. Over the `6^6` argument tuples there are exactly `16`
distinct nonzero numerators `N_i(p, q) = num − den` of these ratios (`r = 1`;
B2). The two witnesses used for elimination are
`E_1 = V_1 V_5² − V_3³` (from `(a, a'; b, b') = (x, y; x, y)`, `c ∈ {x, z}`) and
`E_2 = V_1 V_4² − V_2 V_3²` (from `(x, −x; x, −x)`, `c ∈ {x, y}`);
`E_2 = −(p − q)² G(p, q)` with `G` a polynomial of degree five, and `E_1`, `G`
are symmetric in `(p, q)`.


### Linked source authority

- [Admissibility Rule Three Dimensional Monotone Formation Law Plane Chain Coupling Region Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md): only its explicit hypotheses and conclusions are used.
- [Admissibility Rule Three Dimensional Formation Law Markov Graph Eight Corner Laws Sweep Imprint Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_MARKOV_GRAPH_EIGHT_CORNER_LAWS_SWEEP_IMPRINT_BOUNDED_THEOREM_NOTE_2026-09-15.md): only its explicit hypotheses and conclusions are used.
- [Admissibility Rule Recorded Set Gibbs Theorem Formation Laws Markov Graph Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_RECORDED_SET_GIBBS_THEOREM_FORMATION_LAWS_MARKOV_GRAPH_BOUNDED_THEOREM_NOTE_2026-09-15.md): only its explicit hypotheses and conclusions are used.

## Prior art and what is new

Block 08 (stacked) exhibited the third difference `2160/2197 ≠ 1` at
`(3, 1, 2)`; block 09 conditioned its Markov-graph and separation theorems on a
nonzero third difference; block 10 named "nonzero at every nonconstant triple"
as its strongest missing lemma. Nothing on main or in the open PRs computes the
locus. The tools — elimination by resultants and Groebner bases, Sturm-sequence
root isolation, reduction modulo a minimal polynomial — are classical
computer-algebra methods, named here and under Imports and executed exactly.

Live here: six explicit constructions, structural explanation on the named
lines, the exact off-line pair, and their pair-potential consequences. The
original complete-locus conclusion is historical and deferred.

## Exact target and obligation graph

| obligation | status here |
|---|---|
| X1 the two-body term never vanishes at a nonconstant triple | proved (two factorizations) |
| X2 the line `p = q`: constructions at `1, t*` | three-letter collapse, factorization and exact sufficiency |
| X2′ the lines `p = r` and `q = r`: constructions at `1, ρ` | three triple-pattern values and sufficiency reductions on the six-letter menu |
| X3 the pair `(σ_1, σ_2)`, `(σ_2, σ_1)` | exact polynomial identities and sufficiency reductions |
| Exhaustive six-point classification and exclusion of all other points | deferred; original full necessity proof and failed/incomplete route packet preserved in history |
| X4 the pair part survives at the exceptional points | proved |
| X5 the declared triples are off the locus | executed |
| a structural reason for the off-line pair; the analogous loci for `k ≥ 4` | open; not this note |

## Theorem X1 — the two-body term never vanishes at a nonconstant triple

**Statement.** `Δ_2 log K_2 ≢ 0` for every positive `(p, q, r)` not all
equal.

*Proof.* At `(a, b) = (−x, −x)` with vacuum `+x`,
`K_2(−x,−x) K_2(x,x)/(K_2(−x,x) K_2(x,−x)) = [(p² + q² + 4r²)/(2(pq + 2r²))]²`,
equal to `1` iff `p = q`. At `(a, b) = (y, y)`,
`K_2(y,y) K_2(x,x)/(K_2(y,x) K_2(x,y)) = [(p² + q² + 4r²)/(2r(p + q + r))]²`,
equal to `1` iff `(p − r)² + (q − r)² = 0` iff `p = q = r`. ∎ Executed: both
factorizations over `Q` (B3). (Equivalently, `K^2` has rank one iff both
nontrivial eigenvalues `(p − q)/Z_1` and `(p + q − 2r)/Z_1` of `K` vanish.)

## Theorem X2 — the three collapse lines

**(a) The line `p = q`.** With `p = q = t r`, `φ` does not distinguish the two
signs of an axis, so `Z_3` depends only on the axes of its arguments:
`W_1 = 2t³ + 4` (one axis), `W_2 = 2(t² + t + 1)` (two axes), `W_3 = 6t`
(three axes), in units of `r³`. A function of three letters from a
three-letter alphabet that depends only on the partition pattern is
pair-additive iff `3g_s = log W_1`, `g_s + 2g_d = log W_2`, `3g_d = log W_3`
are solvable, i.e. iff `W_2³ = W_1 W_3²`; and
`W_2³ − W_1 W_3² = 8(t − 1)³(t³ − 3t² − 6t − 1)`. The cubic has one positive
root `t* ∈ (4, 5)` (exact root isolation; the other two lie in `(−2, −1)` and `(−1, 0)`).
Pair-additivity on the six-menu follows from pair-additivity on the quotient,
since `log K_3` is the pull-back. Executed: `E_1` restricted to the line equals
`−8(t − 1)³(t³ − 3t² − 6t − 1)` and `E_2` vanishes identically there (B4).

**(b) The line `p = r`.** With `p = r = 1`, `φ` distinguishes only "opposite"
from "not opposite", and `Z_3` takes three values: `q³ + 5`, `q² + q + 4`,
`3q + 3` (executed, B5: three distinct polynomials over the `216` triples).
Every one of the `16` third-difference numerators restricted to the line is a
multiple of `(q − 1)³ (q³ − 3q² − 15q − 19)`
(B5), so all vanish at `q = 1` and at `q = ρ`, the positive root of
`q³ − 3q² − 15q − 19` in `(6, 7)`. **(c) The line `q = r`** is the image of
(b) under the symmetry `p ↔ q` of every numerator (B6): the exceptional point
is `p = ρ r`. ∎

## Theorem X3 — six constructions and exact reduction identities

**Statement.** Set `r=1`. The points
`(1,1)`, `(t*,t*)`, `(1,ρ)`, `(ρ,1)`, `(σ_1,σ_2)` and `(σ_2,σ_1)`
have pair-additive `log K_3`. Here `t*` and `ρ` are the roots specified
in X2; `σ_1` in `(1,2)` and `σ_2` in `(6,7)` are positive roots of
`s(x)=x⁶−6x⁵−3x⁴+4x³−3x²−6x+31`. Define
`ψ(q)=−(8/85)q⁵+(116/255)q⁴+(196/255)q³+(82/85)q²+(121/255)q+356/255`.
The map `ψ` exchanges these two isolated roots.

*Construction and sufficiency.* Exact reduction gives
`s(ψ(q)) ≡ E_1(ψ(q),q) ≡ G(ψ(q),q) ≡ 0 (mod s(q))`.
Rational interval evaluation of `ψ` on the two isolating intervals,
refined to width `10^{-30}`, lies inside the opposite root's coarse
isolating interval. At each displayed point every one of the 16
third-difference numerators is zero: substitute `p=q`, `p=1`, or
`p=ψ(q)` and reduce modulo the associated minimal polynomial.
Parameter-exchange symmetry supplies the mirrored points. Thus the
mixed third differences vanish and `log K_3` is pair-additive. ∎

**Additional exact identities.** The executed elimination basis for
`(E_1,G)` in the variable order `p > q` has a univariate member proportional to
`(q−1)^6 (q³−3q²−15q−19) s(q) u(q)^2`, where
`u(q)=q⁶+3q⁵+6q⁴+13q³+15q²+12q+22`, and a member `A(q)p−B(q)`.
Reduction of `B/A` gives `1` modulo the `ρ` cubic and `ψ(q)` modulo `s`.
These are algebraic identities and construction checks. The runner's
polynomial root counts describe those named univariate polynomials.
They are not a passing exhaustive classification certificate for the
original physical/model exclusion target.

**Deferred conclusion.** The original necessity argument assembling these
identities into “these and no other positive points” is not asserted here.
It and the attempted N1 routes remain in the exact PR8142 history archive.
A structural explanation for the displayed off-line pair remains open.

## Theorem X4 — what survives at the exceptional points

**Statement.** At each of the five nonconstant exceptional points, for every
formation law of block 10's Theorem T1: the normalizer term `−log K_3(v_A)` on
every three-element recorded set `A` is a sum of three pair terms
`g(v_a, v_b) + g(v_b, v_c) + g(v_a, v_c)` on the co-recorded (face-diagonal)
pairs, and the vacuum-normalized pair term `Δ_2 g` is nonzero. This is a
pair-potential conclusion. In the constructed infinite-law region `c < 1/3`,
the opposite corners `κ` and `−κ` have the same six diagonal sites, and their
pair-additive denominators give the same single-site specification. A common
specification alone proves neither equality nor distinctness of infinite laws.
No eight-law distinction follows at these exceptional points, and no statement
about higher maximal-set differences follows from this three-body calculation.

*Proof.* Pair-additivity is the factorization; if `Δ_2 g ≡ 0` then `g` would be
a sum of one-point functions and `K_3(a, b, c) = f(a) f(b) f(c)`, which by the
internal covariance forces `f` constant and `K_3` constant, contradicting
`V_1 ≠ V_5` at a nonconstant triple (`V_1 − V_5 = p³ + q³ + 4r³ − 3r²(p + q)`,
which vanishes only at `p = q = r` by the arithmetic–geometric mean bound
applied to `p³ + r³ + r³ ≥ 3pr²` and `q³ + r³ + r³ ≥ 3qr²`). The face-diagonal
pair dependence comes from `Δ_2 g`. For opposite corners, each diagonal
pair contribution appears with the same multiplicity because their diagonal
sets agree; regrouping a pair-additive triple sum does not change the
single-site denominator. The stronger law-distinctness inference is not made. ∎

## X5 — the declared triples are off the locus (executed)

At `(p, q, r) = (3, 1, 2)` and `(5, 2, 4)` all `16` numerators are nonzero (B7);
in particular `E_1 ≠ 0` there (block 08's ratios `2160/2197` and
`686196/704969`). Every three-body statement of blocks 08–10 is unconditional
at both.

## No-Go Discipline Gate — deferred broader certification

This revision retains the constructive identities, quantitative bounds and named
finite witnesses above. It does not certify the broader exclusion claims in the
original packet. The original N1–N8 text and every recovery route are preserved
byte-exact in [the PR8146 history manifest](work_history/review_loop/pr8146/original-manifest.json)
under PR8142; the original branch remains a recovery handle for unlanded work.

### N1 — Route coverage
The original list includes unattempted and out-of-domain routes. It is not a
completed route search; broader negative certification is deferred.

### N2 — Walls
The positive weights, six-axis menu, product rule and specified formation class
remain supplied conditions, not deductions or selected physical inputs.

### N3 — Hidden walls
The statements above carry their finite-window, parameter, nonvanishing and
invariance hypotheses explicitly. No unrestricted exclusion follows.

### N4 — Citation scope
Linked source arguments support only their stated mathematical hypotheses.
Historical branch review and cache records are provenance, not authority.

### N5 — Resolution
Exact finite witnesses and the proved formula domains remain as stated above.
They do not establish exhaustive route, phase or infinite-law classification.

### N6 — Partial closure
The positive results are preserved. Unproved exclusions remain open with their
original attempted routes recoverable; no new premise closes them.

### N7 — Steelman
A quantitative bound or finite discrepancy does not settle every alternative
law or order. This revision concedes that gap rather than asserting closure.

### N8 — Recovery
The history manifest binds original heads, paths, decompressed SHA256 hashes and
archive hashes. This deferred certificate is not a passing negative-claim gate;
any future broader exclusion must complete the applicable discipline.

## Falsifiers
- An additional pair-additive point would concern the deferred classification; it would not refute the six constructions claimed here.
- A nonzero numerator at any of the six points after exact reduction (refutes the sufficiency half).
- A factorization of `E_1` on the line `p = q` other than `−8(t − 1)³(t³ − 3t² − 6t − 1)`, or a fourth distinct `Z_3` value on the line `p = r`.
- Both `K_2` ratios of X1 equal to `1` at some nonconstant triple.

## Boundaries and non-claims
This note constructs six pair-additive points and verifies exact polynomial identities for the supplied six-axis product rule; exhaustive classification is deferred. It states nothing infinite-volume beyond the hypothesis map of X4, selects no rule or order as physical, and gives no structural reason for the off-line pair. No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision. Resultants, elimination bases, sign-change sequences and reduction modulo a minimal polynomial are classical computer-algebra methods executed here exactly; no value, constant or theorem is imported as authority.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Blocks 08, 09, 10 (stacked; proposed, unaudited): the objects and the hypothesis being classified.
- Executed exact methods (sympy over `Q`): polynomial factorization, resultants, the lex Groebner basis, Sturm root isolation with rational refinement, inverses and reductions modulo a minimal polynomial. No literature value enters; classical names appear only here and under Prior art.

## Historical author review record
The following records the original author process, not acceptance of its deferred exhaustive conclusion.

Supervisor-run block (owner directive 2026-09-15: no subagents). Controls A–F (`specs/supervisor_control_block11_*.py`) found the locus stepwise: the pattern values and the witness `E_1` on the line `p = q` (A); the interval exclusion of candidate pairs (C); the `p = r` collapse and the elimination basis (D); the exact decision of the sextic pair (E); the full pair-additivity test of all 16 numerators at every candidate (F). The lens pass is in `GOAL_block11.md`; the primary seat wrote X1–X5 and the runner; the refuting pass (`CHECKER_block11_findings.md`) recomputed the locus by the other elimination order and by direct interval evaluation. Facts settled while executing: the first control's algebraic-field gcd route was
abandoned (too slow) for the elimination basis plus exact reductions; the root
exchange `ψ(σ_1) = σ_2` is established by containment of an exact enclosure in the
coarse isolating interval, not in the refined one (a refined interval is narrower
than any enclosure of a nonconstant polynomial over it); the method names were
moved out of the theorem sections.

## Verification

```bash
python3 scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py
python3 scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py --exact
python3 scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py --mutation offline_pair_denied
```

Families: A authority and inputs; B the pattern values, the numerators, X1's factorizations, the three lines; C the elimination (the elimination basis, the sextic pair, the reductions); F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 11 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
