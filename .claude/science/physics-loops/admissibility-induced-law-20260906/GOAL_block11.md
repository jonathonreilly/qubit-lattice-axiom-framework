# GOAL — block 11: the exceptional locus of the three-body term — exact elimination (launched 2026-09-15)

Branch `physics-loop/admissibility-induced-law-block11-three-body-exceptional-locus-20260915`, cut from block 10's tip; stacked PR (base = block 10's branch). Supervisor-run seats. Control first: `specs/supervisor_control_block11_locus.py` and `_b.py` (sympy over `Q`; exact root isolation; no floats as evidence).

## Why
Blocks 08, 09 and 10 state their three-body conclusions "at triples where the third difference of `log K_3` is nonzero", executed at `(3,1,2)` and `(5,2,4)`, and name "nonzero at every nonconstant triple" as the open lemma. The control finds that the lemma is **false**: on the line `p = q = t r` all third differences vanish exactly at the positive root `t*` of `t^3 − 3t^2 − 6t − 1` (`t* ∈ (4, 5)`), because with `p = q` the six-menu collapses to three axes on which pair-additivity is one equation `W_2^3 = W_1 W_3^2 = 8(t−1)^3(t^3−3t^2−6t−1)`. For `k = 2` the lemma is true (two witness ratios vanish together only at `p = q = r`).

## Exact target contract

| field | content |
|---|---|
| Target statement | For the six-axis product rule: (X1) `Δ_2 log K_2 ≢ 0` at every nonconstant triple (proved: the ratios `[(p²+q²+4r²)/(2(pq+2r²))]²` and `[(p²+q²+4r²)/(2r(p+q+r))]²` are both `1` iff `p = q = r`); (X2) the set where every third difference vanishes (the pair-additive locus of `log K_3`) contains, on the line `p = q`, exactly the constant rule and the point `t*`; (X3) off the line, the pair-additive locus is contained in the common zeros of two explicit witness polynomials `E_1`, `G`, whose resultant in `q` has finitely many positive real roots in `p` (listed exactly); each candidate is decided by an exact gcd over the algebraic field («OFFLINE»); (X4) consequences: at `(t*, t*, 1)` the monotone formation law's interaction has no three-body term — its normalizer factorizes into pair terms on the face-diagonal pairs — while the pair terms stay nonzero, so blocks 09–10's Markov-graph conclusions hold there through the pair part; the three-body statements of blocks 08–10 hold exactly off the locus; (X5) the values at the declared triples `(3,1,2)`, `(5,2,4)` are off the locus (exact). |
| Quantifiers / domain | all positive triples for X1–X3; the executed identities are polynomial identities over `Q`; root isolation exact (Sturm intervals) |
| Allowed premises | `minimal_axioms`; the supplied readings of blocks 01–10; block 10's T3 (the term on a maximal recorded set is `−m_A Δ_k log K_k`) and block 08's Q1f |
| Forbidden weakenings | no floating-point value as evidence (numeric labels only); no physical claim about `t*` |
| Required edge cases | the constant rule (all terms vanish); the line `p = q` (the three-axis collapse); `p ≠ q` (the two-witness system) |
| Completion witness | polynomial identities checked by sympy over `Q`; the factorization of `E_1` on the line; the resultant's factors and their isolating intervals; the exact gcd decisions |
| Outcomes that do not count | a numeric root without its isolating interval; a witness whose vanishing is only necessary, presented as the locus |

## Supervisor lens (one seat)
- *Refuter:* "A single witness's vanishing is not pair-additivity." — Correct: pair-additivity needs all cross-ratios `c`-independent; on the line `p = q` the collapse reduces all of them to one equation (proved via the pattern values `W_1, W_2, W_3`); off the line, two witnesses give a necessary condition, decided exactly. "Is `t*` really a zero of every third difference?" — On the line the third difference of any argument choice is a rational function of `(W_1, W_2, W_3)` whose vanishing reduces to `W_2^3 = W_1 W_3^2` (the pattern argument); executed on every pattern class.
- *Prior art:* blocks 08–10 (the hypothesis named as open); nothing on main computes the locus.
- *Scope:* exact algebra; no physics selected; `t*` is an algebraic curiosity of the six-menu, recorded as such.
