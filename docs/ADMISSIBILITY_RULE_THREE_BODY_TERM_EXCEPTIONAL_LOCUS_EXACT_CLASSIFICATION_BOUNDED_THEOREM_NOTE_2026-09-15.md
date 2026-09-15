---
claim_id: admissibility_rule_three_body_term_exceptional_locus_exact_classification_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule of orbit weights (p, q, r): (X1) the two-body normalizer term never vanishes at a nonconstant triple — two mixed-difference ratios of K_2 are both 1 only when p = q = r (proved by factorization); (X2)–(X3) the three-body normalizer term vanishes — log K_3 is a sum of pair functions — exactly at six points of the positive octant up to scale: the constant rule, the point p = q = t* r with t* the positive root of t^3 - 3t^2 - 6t - 1 (in (4, 5)), the two points p = r, q = rho r and q = r, p = rho r with rho the positive root of x^3 - 3x^2 - 15x - 19 (in (6, 7)), and the two points (p, q) = (sigma_1, sigma_2) r and (sigma_2, sigma_1) r with sigma_1 in (1, 2), sigma_2 in (6, 7) the positive roots of x^6 - 6x^5 - 3x^4 + 4x^3 - 3x^2 - 6x + 31, linked by p = psi(q) for an explicit quintic psi; the three points on the lines p = q, p = r, q = r are explained by the collapse of the six-menu to a three-letter quotient on those lines, where pair-additivity is one equation; completeness is proved by exact elimination (a lex elimination basis of the two witness polynomials, exact root isolation, and the reduction of all 16 distinct third-difference numerators modulo each minimal polynomial); (X4) at the five nonconstant exceptional points the three-body normalizer of every formation law factorizes into nonzero pair terms on the co-recorded pairs, so the Markov-graph statements of blocks 09 and 10 hold there through their pair part, while every genuine three-body statement of blocks 08–10 holds exactly off the locus; (X5) the declared triples (3,1,2) and (5,2,4) are off the locus (all 16 numerators nonzero). Exact algebra over the rationals; isolating intervals in place of numbers; no order selected as physical."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
  - admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_bounded_theorem_note_2026-09-15
runner: scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py
---

# The three-body term of the six-menu rule vanishes at exactly five nonconstant weight ratios: the exact exceptional locus

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact algebra; conditional on the named supplied readings; unaudited)

## Result up front

The earlier notes found that forming records with the rule creates a genuine
three-way coupling among the three sites a site saw when it formed, and they
proved their three-way statements at two rule settings, leaving open whether
the coupling could ever vanish at some other nonconstant setting. It can, and
this note finds exactly where. Two settings where the rule stops
distinguishing two of its three pair types — same sign, opposite sign,
orthogonal — behave like rules on a three-letter alphabet, and on each such
line there is exactly one extra weight ratio (an algebraic number of degree
three) where the three-way coupling disappears; a third line of that kind is
the mirror image of the second. Surprisingly there is also one pair of
settings off all these lines, with weight ratios given by a degree-six
equation, where it disappears too. That is the whole list: six points in all,
counting the trivial constant rule. Everywhere else — in particular at the
two settings used throughout the campaign — the three-way coupling is
genuine; and even at the six points the two-way couplings across faces
survive, so the earlier conclusions about what a site listens to still hold
there. Nothing here selects a rule.

Exactly: with `V_1, …, V_5` the five pattern values of `Z_3` (below), the
two witnesses `E_1 = V_1 V_5² − V_3³` and `E_2 = V_1 V_4² − V_2 V_3² = −(p − q)² G`
vanish together on the positive octant exactly at the six points of (X2)–(X3),
`log K_3` is pair-additive at each (all 16 distinct third-difference
numerators reduce to zero modulo the point's minimal polynomial), and at no
other point. Executed with exact rational and polynomial arithmetic:
20 checks, 11 mutations.

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
next_trace_action: "the open lemma is settled: false at exactly five nonconstant points, true elsewhere; blocks 08–10's three-body statements are now unconditional off a finite explicit set, and their Markov-graph conclusions hold everywhere nonconstant through the pair part. Next: the region's boundary in (p, q, r); strong coupling. Consumers: the campaign's queue; #8093's assembly; the parked statistical-bridge material (read-only)"
conditional_surface_status: "exact algebra over Q for every statement; the exceptional points are algebraic numbers given by their minimal polynomials and isolating intervals; conditional on the six-axis menu and the product form of the rule (the objects); no infinite-volume statement beyond citation"
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

## Prior art and what is new

Block 08 (stacked) exhibited the third difference `2160/2197 ≠ 1` at
`(3, 1, 2)`; block 09 conditioned its Markov-graph and separation theorems on a
nonzero third difference; block 10 named "nonzero at every nonconstant triple"
as its strongest missing lemma. Nothing on main or in the open PRs computes the
locus. The tools — elimination by resultants and Groebner bases, Sturm-sequence
root isolation, reduction modulo a minimal polynomial — are classical
computer-algebra methods, named here and under Imports and executed exactly.

New here: the complete exceptional locus (six points), its structural
explanation on the three collapse lines, the exact off-line pair, and the
consequences for blocks 08–10.

## Exact target and obligation graph

| obligation | status here |
|---|---|
| X1 the two-body term never vanishes at a nonconstant triple | proved (two factorizations) |
| X2 the line `p = q`: exactly `{1, t*}` | proved (three-letter collapse) and executed (factorization; sign-change) |
| X2′ the lines `p = r` and `q = r`: exactly `{1, ρ}` | proved (the same collapse with a different quotient) and executed |
| X3 completeness off the lines: exactly the pair `(σ_1, σ_2)`, `(σ_2, σ_1)` | executed exact elimination (resultant; elimination basis; reduction of all 16 numerators) |
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
unit multiple of `(q − 1)³ (q³ − 3q² − 15q − 19)` times a positive polynomial
(B5), so all vanish iff `q = 1` or `q = ρ`, the positive root of
`q³ − 3q² − 15q − 19` in `(6, 7)`. **(c) The line `q = r`** is the image of
(b) under the symmetry `p ↔ q` of every numerator (B6): the exceptional point
is `p = ρ r`. ∎

## Theorem X3 — completeness: the locus off the lines is one pair of points

**Statement.** A positive `(p, q)` (with `r = 1`) at which `log K_3` is
pair-additive satisfies `E_1 = E_2 = 0`; the positive solutions of this system
are exactly `(1, 1)`, `(t*, t*)`, `(1, ρ)`, `(ρ, 1)`, `(σ_1, σ_2)`, `(σ_2, σ_1)`,
where `σ_1 ∈ (1, 2)` and `σ_2 ∈ (6, 7)` are the two positive roots of
`s(x) = x⁶ − 6x⁵ − 3x⁴ + 4x³ − 3x² − 6x + 31`, and on that factor
`p ≡ ψ(q) := −(8/85) q⁵ + (116/255) q⁴ + (196/255) q³ + (82/85) q² + (121/255) q + 356/255 (mod s(q))`,
which exchanges `σ_1` and `σ_2`. At every one of the six points all `16`
numerators vanish; hence the pair-additive locus is exactly these six points.

*Proof (exact elimination, executed).* On the diagonal `p = q`, `E_2 ≡ 0` and
`E_1 = 0` gives `{1, t*}` (X2a). Off the diagonal, `E_2 = 0` iff `G = 0`. The
lex elimination basis of `(E_1, G)` in `p > q` consists of a univariate
`h(q) = (q − 1)⁶ (q³ − 3q² − 15q − 19) s(q) u(q)²` with `u` a sextic without
positive real roots (exact root isolation), an element `A(q) p − B(q)` with
`A = c (q − 1)`, and a quartic-in-`p` element (C1). For `q` a root of the
`ρ`-cubic, `p ≡ B/A ≡ 1 (mod the cubic)`; for `q` a root of `s`,
`p ≡ ψ(q) (mod s)` with `s(ψ(q)) ≡ 0`, `E_1(ψ(q), q) ≡ 0` and `G(ψ(q), q) ≡ 0
(mod s)` (C2), and the exact rational enclosures of `ψ` over the isolating
intervals of `σ_1`, `σ_2` (refined to width `10^{−30}`) show `ψ(σ_1) = σ_2`,
`ψ(σ_2) = σ_1` (C3); for `q = 1`, `A(1) = 0` and the system reduces to the line
`q = r` of X2c, giving `p ∈ {1, ρ}`. This lists every positive common zero.
Sufficiency: at each of the six points, every one of the `16` numerators,
reduced modulo the point's minimal polynomial after the substitution
`p = q`, `p = 1`, or `p = ψ(q)`, is zero (C4). ∎

The off-line pair is not explained by a collapse of the menu: at `(σ_1, σ_2)`
the three pair types carry three distinct weights and `Z_3` takes its five
generic values; a structural reason is not known (open).

## Theorem X4 — what survives at the exceptional points

**Statement.** At each of the five nonconstant exceptional points, for every
formation law of block 10's Theorem T1: the normalizer term `−log K_3(v_A)` on
every three-element recorded set `A` is a sum of three pair terms
`g(v_a, v_b) + g(v_b, v_c) + g(v_a, v_c)` on the co-recorded (face-diagonal)
pairs, and the vacuum-normalized pair term `Δ_2 g` is nonzero; consequently
block 09's dependence of the full conditional on the face-diagonal sites, its
Markov-graph theorem R1, its separation R2 and its eight-fold distinctness
R3, and block 10's T4 all hold at these points through the pair part, while
the genuine three-body statements (block 08's Q1f, block 09's "three-body"
wording, block 10's T3 for `k = 3`) hold exactly at every other nonconstant
triple.

*Proof.* Pair-additivity is the factorization; if `Δ_2 g ≡ 0` then `g` would be
a sum of one-point functions and `K_3(a, b, c) = f(a) f(b) f(c)`, which by the
internal covariance forces `f` constant and `K_3` constant, contradicting
`V_1 ≠ V_5` at a nonconstant triple (`V_1 − V_5 = p³ + q³ + 4r³ − 3r²(p + q)`,
which vanishes only at `p = q = r` by the arithmetic–geometric mean bound
applied to `p³ + r³ + r³ ≥ 3pr²` and `q³ + r³ + r³ ≥ 3qr²`). The face-diagonal
dependence of block 09's R1 then comes from `Δ_2 g` in place of the mixed
second difference of `log K_3`; the rest follows verbatim. ∎

## X5 — the declared triples are off the locus (executed)

At `(p, q, r) = (3, 1, 2)` and `(5, 2, 4)` all `16` numerators are nonzero (B7);
in particular `E_1 ≠ 0` there (block 08's ratios `2160/2197` and
`686196/704969`). Every three-body statement of blocks 08–10 is unconditional
at both.

## No-Go Discipline Gate

The negative sentence of this note is X3's completeness ("at no other point")
— a proved statement about the zero set of a polynomial system, executed by
exact elimination. Not a route no-go; the gate is answered for completeness.

### N1 — Routes by which another exceptional point could exist

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a common zero of `E_1`, `E_2` missed by the elimination | a positive solution outside the elimination basis's variety | the basis generates the same ideal; every positive `q` is a root of `h`; for each, `p` is forced (or the line `q = 1` is handled by symmetry) | RULED OUT (exact; C1–C3) |
| 2 a point where the two witnesses vanish but another numerator does not | a point in the variety off the locus | all 16 numerators tested at all six points | RULED OUT (C4) |
| 3 a point where some numerator vanishes but the witnesses do not | irrelevant: the locus needs all numerators, in particular the witnesses | — | RULED OUT BY DEFINITION |
| 4 boundary weights (`p, q` or `r = 0`) | zero weights | outside positivity; not considered | not attempted; obligation named |
| 5 other menus | a different alphabet | the pattern values change; not this note | not attempted; obligation named |

### N2 — Wall-independence audit
Walls: `W_pos` (positivity; the domain), `W_menu` (the six-axis menu; the pattern values), `W_prod` (the product form). No wall follows from another; all three define the object.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: none. The elimination steps are executed, not assumed.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 08 (stacked): Q1f | the third difference at (3,1,2), (5,2,4) | X5 | yes |
| block 09 (stacked): R1–R3 and their hypothesis | the Markov graph under a nonzero third difference | X4 (the hypothesis map) | yes |
| block 10 (stacked): T3, the open lemma | nonzero differences at every nonconstant triple | X2–X3 (false at five points), X4 | yes |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "at no other point" | executed: all 16 numerators at the six points; the factorizations of `E_1` on the three lines | — (no sites) | executed: the pattern values against the definition on all 216 triples; the three-letter collapses | executed: the elimination basis, the resultant's factors, the isolating intervals, the reductions modulo minimal polynomials | proved for the whole positive octant (a polynomial statement) |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no weight; none is a wall. No reframing changes a polynomial identity.

### N7 — Steelman
Hostile reviewer: "Isolating intervals are not proofs of which root is which; the pairing `ψ(σ_1) = σ_2` could be a numerical coincidence." Reply: `ψ` is computed exactly modulo `s`, `s(ψ) ≡ 0 (mod s)` exactly, so `ψ` permutes the roots of `s`; the enclosure of `ψ` over each isolating interval is an exact rational interval that contains exactly one root's interval — an exact statement, not a numeric one. Conceded: the structural reason for the off-line pair is open.

### N8 — Cross-cycle echo
The nearest prior wall is block 10's open lemma, now settled; block 04's "silent triples" are unrelated (a criterion's silence, not an algebraic locus).

## Falsifiers
- A positive `(p, q)` with all 16 numerators zero outside the six points (refutes X3).
- A nonzero numerator at any of the six points after exact reduction (refutes the sufficiency half).
- A factorization of `E_1` on the line `p = q` other than `−8(t − 1)³(t³ − 3t² − 6t − 1)`, or a fourth distinct `Z_3` value on the line `p = r`.
- Both `K_2` ratios of X1 equal to `1` at some nonconstant triple.

## Boundaries and non-claims
This note classifies the zero set of the three-body normalizer term of the six-axis product rule; it states nothing infinite-volume beyond the hypothesis map of X4, selects no rule or order as physical, and gives no structural reason for the off-line pair. No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision. Resultants, elimination bases, sign-change sequences and reduction modulo a minimal polynomial are classical computer-algebra methods executed here exactly; no value, constant or theorem is imported as authority.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Blocks 08, 09, 10 (stacked; proposed, unaudited): the objects and the hypothesis being classified.
- Executed exact methods (sympy over `Q`): polynomial factorization, resultants, the lex Groebner basis, Sturm root isolation with rational refinement, inverses and reductions modulo a minimal polynomial. No literature value enters; classical names appear only here and under Prior art.

## Review record
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
