from pathlib import Path
import ast
w=Path('/private/tmp/review-drain-20260915/drain-author8146')
p=w/'docs/ADMISSIBILITY_RULE_THREE_BODY_TERM_EXCEPTIONAL_LOCUS_EXACT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md'
s=p.read_text()
def replace(a,b):
 global s
 assert a in s,a[:100]
 s=s.replace(a,b)
def section(start,end,body):
 global s
 a=s.index(start);b=s.index(end,a);s=s[:a]+body+'\n\n'+s[b:]
old=s.splitlines()[3]
replace(old,'claim_scope: "For the supplied positive six-axis product rule modulo scale: six explicit pair-additive three-neighbor log-normalizer constructions, exact pattern values, polynomial factorizations, isolating intervals and sufficiency reductions. Exhaustive classification and exclusion of other points are deferred, with their original proof preserved in history. The p=q family factors through three unsigned axes; p=r retains six letters. At the five displayed nonconstant points the pair component is nonzero. Opposite-corner single-site specifications coincide there; this does not establish equality or distinctness of infinite laws. Infinite-law discussion requires c < 1/3."')
replace('# The three-body term of the six-menu rule vanishes at exactly five nonconstant weight ratios: the exact exceptional locus','# Six pair-additive constructions for the three-neighbor normalizer of the supplied six-axis rule')
section('## Result up front','## Machine status and trace','''## Result up front

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
component. No physical rule or infinite-law distinction is selected.''')
replace('next_trace_action: "the open lemma is settled: false at exactly five nonconstant points, true elsewhere; blocks 08–10\'s three-body statements are now unconditional off a finite explicit set, and X4 retains the nonzero pair component, without an eight-law distinction or higher-body inference. Next: the region\'s boundary in (p, q, r); strong coupling. Consumers: the campaign\'s queue; #8093\'s assembly; the parked statistical-bridge material (read-only)"','next_trace_action: "Use the six explicit constructions and their exact sufficiency reductions. Exhaustive exceptional-locus classification and its necessity proof remain deferred in the original archive; no downstream assertion outside the displayed points follows here."')
replace('conditional_surface_status: "exact algebra over Q for every statement; the exceptional points are algebraic numbers given by their minimal polynomials and isolating intervals; conditional on the six-axis menu and the product form of the rule (the objects); no infinite-volume statement beyond citation"','conditional_surface_status: "Exact identities and six sufficiency constructions over algebraic numbers with isolating intervals, conditional on the supplied six-axis product rule; exhaustive locus certification deferred; infinite-law discussion only under the cited construction hypotheses."')
replace('New here: the complete exceptional locus (six points), its structural\nexplanation on the three collapse lines, the exact off-line pair, and the\nconsequences for blocks 08–10.','Live here: six explicit constructions, structural explanation on the named\nlines, the exact off-line pair, and their pair-potential consequences. The\noriginal complete-locus conclusion is historical and deferred.')
replace('| X2 the line `p = q`: exactly `{1, t*}` | proved (three-letter collapse) and executed (factorization; sign-change) |','| X2 the line `p = q`: constructions at `1, t*` | three-letter collapse, factorization and exact sufficiency |')
replace('| X2′ the lines `p = r` and `q = r`: exactly `{1, ρ}` | proved (three triple-pattern values on the six-letter menu) and executed |','| X2′ the lines `p = r` and `q = r`: constructions at `1, ρ` | three triple-pattern values and sufficiency reductions on the six-letter menu |')
replace('| X3 completeness off the lines: exactly the pair `(σ_1, σ_2)`, `(σ_2, σ_1)` | executed exact elimination (resultant; elimination basis; reduction of all 16 numerators) |','| X3 the pair `(σ_1, σ_2)`, `(σ_2, σ_1)` | exact polynomial identities and sufficiency reductions |\n| Exhaustive six-point classification and exclusion of all other points | deferred; original full necessity proof and failed/incomplete route packet preserved in history |')
replace('unit multiple of `(q − 1)³ (q³ − 3q² − 15q − 19)` times a positive polynomial\n(B5), so all vanish iff `q = 1` or `q = ρ`, the positive root of','multiple of `(q − 1)³ (q³ − 3q² − 15q − 19)`\n(B5), so all vanish at `q = 1` and at `q = ρ`, the positive root of')
section('## Theorem X3 — completeness:', '## Theorem X4', '''## Theorem X3 — six constructions and exact reduction identities

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
A structural explanation for the displayed off-line pair remains open.''')
replace('- A positive `(p, q)` with all 16 numerators zero outside the six points (refutes X3).','- An additional pair-additive point would concern the deferred classification; it would not refute the six constructions claimed here.')
replace('This note classifies the zero set of the three-body normalizer term of the six-axis product rule; it states nothing infinite-volume beyond the hypothesis map of X4, selects no rule or order as physical, and gives no structural reason for the off-line pair.','This note constructs six pair-additive points and verifies exact polynomial identities for the supplied six-axis product rule; exhaustive classification is deferred. It states nothing infinite-volume beyond the hypothesis map of X4, selects no rule or order as physical, and gives no structural reason for the off-line pair.')
replace('## Review record\nSupervisor-run block','## Historical author review record\nThe following records the original author process, not acceptance of its deferred exhaustive conclusion.\n\nSupervisor-run block')
p.write_text(s)
r=w/'scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py';q=r.read_text()
q=q.replace('This note classifies the zero set of the three-body normalizer term of the six-axis product rule; it states nothing infinite-volume beyond the hypothesis map of X4, selects no rule or order as physical, and gives no structural reason for the off-line pair.','This note constructs six pair-additive points and verifies exact polynomial identities for the supplied six-axis product rule; exhaustive classification is deferred. It states nothing infinite-volume beyond the hypothesis map of X4, selects no rule or order as physical, and gives no structural reason for the off-line pair.')
q=q.replace('lattice_wide: proved for the whole positive octant (a polynomial statement); the infinite-volume consequences are the hypothesis map of X4, by citation of blocks 08-10','lattice_wide: polynomial identities at their stated domains and six sufficiency constructions; exhaustive locus certification deferred; infinite-law remarks only under X4 hypotheses')
q=q.replace('scope: the exceptional locus of the three-body term —','scope: six pair-additive constructions; exhaustive classification deferred —')
q=q.replace('"X3: the lex Groebner basis','"X3 algebraic identity: the lex Groebner basis')
q=q.replace('"X3: on the sextic factor','"X3 construction: on the sextic factor')
ast.parse(q);r.write_text(q)
print('narrowed X3 note and runner prose; no scientific execution')
