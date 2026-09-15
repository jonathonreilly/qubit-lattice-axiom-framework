---
claim_id: admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_the_static_law_on_a_plaquette_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On finite windows of Z^3 with the six-axis menu and the covariant positive product rule (p, q, r), executed at (3, 1, 2), under the records-only reading, with records forming one at a time under independent memoryless clocks whose rates depend covariantly on the recorded set and its values: (R1) the next site is x with probability lambda_x / sum lambda, the finished law is the jump chain's, and for value-blind rate laws it is the mixture over orders of the sequential laws, depending on the rate law only through the induced distribution on recorded-set multisets (proved); (R2) the uniform, seeded and attracting laws give pairwise different finished laws on the 2x3 rectangle (exact total variations; the uniform one equals the census note's Theorem 3 rational) and different all-+x probabilities on the 2x2x2 cube; a value-dependent parallel-growth law differs from all three on the plaquette (executed); (R3) on every tree window the seeded law gives the static law exactly, since every record after the first has exactly one recorded neighbour (proved; executed on the path and the star); (R4) for every covariant rate law, with arbitrary causal dependence on the recorded values, the finished law of the 2x2 plaquette is not the static law at every non-constant rule (proved by the plaquette's symmetry types and a strictly increasing weight; executed symbolically for the general law and exactly for four laws); (R5) the static plaquette law is not a convex combination of the sequential laws (proved); (R6) the parallel-growth law's plaquette law lies outside the affine span of the sequential laws (executed). The separating clause candidates are recorded and not adopted; no order, rate, rule or coupling is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py
---

# The formation-rate clause witness: every covariant clock law gives a mixture over orders that is the static law on trees and never the static law on a plaquette

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

The axioms say records form and say how a forming record's value depends
on its recorded neighbours; they say nothing about *when* a site forms. The
derivation campaign asks for a witness that the missing rate law matters,
and names three clause candidates: a rate that ignores the neighbourhood, a
rate set by it, or no clause at all. Give every empty site a clock whose
rate may depend, in any covariant way, on where the records are and what
they say. Then the order in which records form is random, the finished
pattern law is an average over orders, and different clock laws give
different averages: on a two-by-three window the uniform clock, a clock
that only fires next to existing records, and a clock that fires faster
the more recorded neighbours a site has give three different laws, and we
print their exact distances from the static law. That is the witness the
campaign asked for.

The sharper question is whether some clock law could make the
record-by-record reading reproduce the static law that the rest of the
repository uses — the law a gravity Green function would need (block 13).
On any tree-shaped window the answer is yes, exactly: the clock that fires
only next to existing records gives every site exactly one recorded
neighbour, and then the two readings agree. On a single square the answer
is no, for every covariant clock law whatsoever, value-dependent or not:
the square's symmetries pin the only decisions a clock can make down to a
few numbers, and the resulting weight is strictly increasing in a quantity
that takes different values on two patterns the static law weighs equally.
So a rate clause cannot deliver the static reading on any window with a
square in it, while it delivers it exactly on windows without cycles.

Exactly: `P(next = x) = λ_x/Σλ` (R1); on `2×3` at `(3,1,2)` the distances to
the static law are `372254646387017/12790481418000000` (uniform, the census
note's number), `5951761987229/292725576000000` (seeded) and
`32318135184155791/1253467178964000000` (attracting) (R2); on the plaquette
`μ/Π_edges K = (1/4) Σ_s G(p_{type(s)}, d)` with `G(p,d) = (1−p)d/6 + p d²/36`
and `d_same = 72/13`, `d_anti = 72/11`, `d_orth = 6` at `(3,1,2)` (R4).
Executed with exact arithmetic: 22 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's clock-and-rate block (#8093, verdict table row 'Formation rate': to compute) — whether any finished-window statistic depends on the formation-rate law, with the separating clause candidates (a) rate independent of the nearest-neighbour conditions, (b) rate determined by them, (c) no clause; and the reconciliation question behind it: whether a rate clause can make the formation reading reproduce the static law"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the witness is exhibited exactly and the reconciliation question is answered: a rate clause reproduces the static law on trees and on no window containing a plaquette; the clause decision is the owner's. Consumers: #8093's verdict table and assembly; the gravity node (block 13: its Green function needs the static reading, which no rate clause supplies); the formation-unit block (next)"
conditional_surface_status: "R1, R3, R4, R5 proved for every positive triple (R4 at every non-constant rule); R2, R6 executed at (3,1,2); conditional on the records-only reading, the six-axis menu, the product rule and the clock model as supplied conditions"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "competing memoryless clocks (R1); exact enumeration of orders and patterns with the multiset key (R2); a counting argument on trees with block 01's Theorem B (R3); a symmetry-type argument with a strictly increasing weight (R4, R5); an exact rank test (R6); every number an exact rational"
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable." — and from its
reading note (2): the distribution "does not supply the formation site,
probability, or rate."

**Readings carried, named, nothing new adopted.** The records-only reading
and the formation law of block 01
([`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)):
along an order `σ` the site `x_k` draws from the rule with its recorded
neighbours `A_k` only, `μ_σ(v) = Π_k r(v_{x_k} | v_{A_k})`, with
`r(a | ∅) = 1/M` and `r(a | A) = Π_{y∈A} K(v_y, a)/K_{|A|}(v_A)`,
`K(b, a) = φ(a, b)/Z_1`, `K_k(v_A) = Σ_s Π_{y∈A} K(v_y, s)` (`K_1 ≡ 1`). The
static law `Π_edges φ(v_e)/Z`. The six-axis menu, positivity, the product rule
with weights `(p, q, r)`, `Z_1 = p + q + 4r`. The multiset key of the census
note ([`ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`](ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md),
Lemma L): `μ_σ` depends on `σ` only through the multiset of recorded sets of
size at least two.

**The clock model (the supplied object of this block).** Every unrecorded
site `x` carries an exponential clock of rate `λ(x, S, v_S) ≥ 0`, a function
of the site, the recorded set `S` and the recorded values, invariant under the
simultaneous action of lattice translations and proper cubic rotations on
`(x, S, v_S)` (the menu carries the rotation action on axes). Clocks are
independent given the state and memoryless. When `x`'s clock rings first, `x`
records a value from the rule given `v_{N(x)∩S}`; then all clocks restart. The
window `Λ` is the set of sites that can form; the process stops when `Λ` is
recorded. *Value-blind* laws depend on `(x, S)` only. Executed laws: uniform
`λ ≡ 1`; seeded `λ = 1` if `N(x) ∩ S ≠ ∅` or `S = ∅`, else `0`; attracting
`λ = 1 + |N(x) ∩ S|`; parallel growth
`λ = 1 + [∃ y ∈ N(x) ∩ S : v_y = the axis from y to x]`.

**Windows.** The `2×3` rectangle; the open `2×2×2` cube; the plaquette
(sites `1 = (0,0)`, `2 = (1,0)`, `3 = (1,1)`, `4 = (0,1)` in the plane `z = 0`);
the path of three sites; the star (a site and four of its neighbours).

**Plaquette types.** For a corner `s` let `δ_s` point from `s` to the opposite
corner (`δ_1 = (1,1,0)`, `δ_2 = (−1,1,0)`, `δ_3 = (−1,−1,0)`, `δ_4 = (1,−1,0)`).
A value `v_s` is of type *toward* if `v_s · δ_s > 0`, *away* if `< 0`,
*perpendicular* if `v_s = ±z`. Write `d_same = 1/K_2(a,a)`,
`d_anti = 1/K_2(a,−a)`, `d_orth = 1/K_2(a,b)` for `b ⊥ a`; at `(3,1,2)`:
`72/13`, `72/11`, `6`.

## Prior art and what is new

The census note (on `main`) proved the multiset key and computed the uniform
mixture over all orders on `2×3` and on the cube, calling it a
witness-generating device; block 01 proved Theorem B (the two readings agree
when every record forms with at most one recorded neighbour) and the
disagreement on every window with a cycle; PR #8137 (open) shows a varying
possibility-symmetric rule has order-dependent statistics. Competing
exponential clocks and their jump chain are the textbook construction of a
continuous-time Markov chain (Gillespie's algorithm is the same fact);
growth restricted to the boundary of the recorded cluster is the Eden model's
support rule. None of it is used as authority. Nothing on `main`
(`f1755b6e10`; search recorded in `ROUTE_PORTFOLIO.md`) exhibits the rate-law
witness or asks whether a rate law can reproduce the static law.

New here: the witness (R2) and the positive/negative reachability pair —
exact equality on trees (R3), impossibility on the plaquette for every
covariant rate law, value-dependent ones included (R4), with its two
corollaries (R5, R6).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| R1 clocks to orders; value-blind laws give mixtures through the multiset distribution | proved; the jump probability executed symbolically; mixtures by classes against full enumeration (B1–B2) |
| R2 the witness on `2×3`, the cube and the plaquette | executed (C1–C4) |
| R3 trees: seeded growth = static | proved; executed on the path and the star (D1–D2) |
| R4 the plaquette no-go for every covariant rate law | proved; executed symbolically in the type probabilities and exactly for four laws (E1–E3) |
| R5 not a convex combination of the sequential laws | proved; executed by the class ratios (E4) |
| R6 parallel growth outside the affine span | executed (E5) |
| larger windows containing a plaquette; other menus; the formation-unit question | open; not this note |

## Theorem R1 — clocks give orders, orders give mixtures

**Statement.** In the state `(S, v_S)` with unrecorded rates `λ_y`,
`Λ = Σ_y λ_y > 0`, the next site to form is `x` with probability `λ_x/Λ`,
independent of the waiting time, and the finished law is that of the
discrete chain with these jump probabilities. For a value-blind law the jump
probabilities do not depend on the values, the order `σ` has a law `P_R(σ)`
independent of the values, and the finished law is `μ_R = Σ_σ P_R(σ) μ_σ`,
which depends on `R` only through the induced law of the recorded-set
multiset. For a value-dependent law the finished law is
`μ_R(v) = Σ_σ P_R(σ | v) μ_σ(v)`, where `P_R(σ | v)` uses at each step only
the values recorded before it.

*Proof.* With independent exponential times `T_y` of rates `λ_y`,
`P(T_x < T_y ∀ y ≠ x) = ∫_0^∞ λ_x e^{−λ_x t} Π_{y≠x} e^{−λ_y t} dt = λ_x/Λ`,
and the minimum's law is exponential with rate `Λ` independent of which clock
rang; memorylessness makes the state sequence Markov with these jump
probabilities, and the finished pattern depends only on the state sequence.
Value-blind: the jump probabilities are functions of `(S)` only, so the order
law factorizes out of the value draws; the last claim is Lemma L. ∎ Executed:
the jump probabilities for rates `(1, 2, 3)` by the exact integral (B1); the
mixtures on `2×3` computed by multiset classes against the full enumeration of
`720` orders (B2).

## Theorem R2 — the witness

**Statement.** At `(3,1,2)` on `2×3` (28 classes, as in the census note) the
uniform, seeded and attracting laws give pairwise different finished laws;
their distances to the static law are `372254646387017/12790481418000000` (`0.0291…`) (uniform; equal to the
census note's Theorem 3 value), `5951761987229/292725576000000` (`0.0203…`) (seeded; it charges 6 of the 28
classes) and `32318135184155791/1253467178964000000` (`0.0258…`) (attracting); the pairwise distances are
`1415480709077/147346345935360` (uniform–seeded, `0.0096…`), `842029569149/229205427010560` (uniform–attracting, `0.0037…`), `12238463804737/2062848843095040` (seeded–attracting, `0.0059…`). On the open cube (542 classes) the all-`+x` pattern has
probability `338229/7997080000` (uniform), `84807/1799782400` (seeded), `3244436397/73116160000000` (attracting) under the three laws, against `59049/775835648` for the
static law. On the plaquette the four laws give distances `262271/15806232` (uniform, `0.0166…`), `30457/2431728` (seeded, `0.0125…`), `591377/39515580` (attracting, `0.0150…`), `2239744469/137703893184` (parallel growth, `0.0163…`) to the
static law and are pairwise different.

*Proof.* Enumeration; the class structure is Lemma L. ∎ (C1–C4.)

## Theorem R3 — on trees the seeded law is the static law

**Statement.** Let `Λ` be a tree (a connected window without cycles). Under
the seeded law the recorded set is connected at every step, so every record
after the first has exactly one recorded neighbour, and `μ_seeded` equals the
static law of `Λ` exactly, whatever the first site. The uniform law differs
from it on the path and on the star.

*Proof.* If the recorded cluster is connected and `x` has two recorded
neighbours, the two paths from `x` through them into the cluster close a
cycle; so on a tree every new site has exactly one recorded neighbour, the
seeded law keeps the cluster connected by construction, and block 01's Theorem
B applies to every order it charges. Under the uniform law an order in which
two non-adjacent sites form before their common neighbour has positive
probability and gives a site with two recorded neighbours. ∎ Executed: the
path and the four-leaf star, seeded equal to static, uniform at distance
`1/216` on the path and `56059/3369600` on the star (D1–D2).

## Theorem R4 — no covariant rate law reaches the static law on a plaquette

**Statement.** For every covariant rate law — value-dependent or not — and
every non-constant rule (not `p = q = r`), the finished law of the plaquette
is not the static law.

*Proof.* Write `Π K = Π_edges K(v_e)`. Every order of the plaquette is of one of
two kinds: a *path* order (start `s`, then an adjacent corner, then the next
along the cycle, then the last corner, which records both its neighbours, the
ends of one diagonal) with `μ_σ = (1/6) Π K · d`, `d = 1/K_2` of that diagonal;
or a *diagonal-first* order (start `s`, then the opposite corner with no
recorded neighbour, then the remaining two, each recording both) with
`μ_σ = (1/36) Π K · d_s²`, `d_s` for the diagonal through `s`. (Each edge factor
`K` appears once, when its later endpoint forms; `K_1 ≡ 1`.) The static law is
`Π K · Z_1⁴/Z`, a constant multiple of `Π K`.

Now the clock. At `S = ∅` the four rates are equal (the 90° rotation about
the plaquette's axis is a proper rotation carrying each corner to the next
and fixing the configuration), so the first site is uniform and its value is
uniform. At `S = {s}` the probability `p_s` that the opposite corner forms
next is `λ_diag/(λ_diag + λ_a + λ_b)`, a function of `(s, v_s)` alone; the
180° rotation about the axis `δ_s` (a proper rotation; it swaps the two
adjacent candidates and fixes the diagonal one, and acts on values by
swapping the two in-plane axes along `δ_s` and reversing `z`) shows that `p_s`
depends only on the type of `v_s`: `p_in`, `p_out`, `p_perp`. Whatever happens
later, a diagonal-first history from `s` ends with weight `(1/36) Π K d_s²`,
and a path history from `s` ends with weight `(1/6) Π K d` for the diagonal it
closes. Hence for any pattern whose two diagonals have the same pair type,
`d_1 = d_2 = d`, the finished law is
`μ(v) = Π K · (1/4) Σ_s [(1 − p_{type(s)}) d/6 + p_{type(s)} d²/36] = Π K · (1/4) Σ_s G(p_{type(s)}, d)`,
where `G(p, d) = (1 − p) d/6 + p d²/36` is strictly increasing in `d > 0` for
every `p ∈ [0, 1]`, and the path-class decisions (which may depend on values)
drop out because both diagonals carry the same `d`.

Take `P_1 = (+x, −x, +x, −x)`: diagonals `(+x,+x)` and `(−x,−x)`, `d = d_same`;
types toward, toward, away, away. Take `P_3 = (+x, +x, −x, −x)`: diagonals
`(+x,−x)` twice, `d = d_anti`; types toward, away, toward, away — the same
multiset. So `μ(P_3)/ΠK(P_3) − μ(P_1)/ΠK(P_1) = (1/2) Σ_{τ ∈ {in, out}} [G(p_τ, d_anti) − G(p_τ, d_same)]`,
which is strictly positive when `d_anti > d_same`, i.e. `K_2(a,−a) < K_2(a,a)`,
i.e. `(p − q)² > 0`. If `p = q`, take `P_4 = (+x, −x, +y, +y)`: diagonals
`(+x,+y)` and `(−x,+y)`, `d = d_orth`; types toward, toward, away, away — the
multiset of `P_1`; and `d_orth ≠ d_same` iff `(p − r)² + (q − r)² > 0`. In
either case the two ratios differ while the static law's ratio is constant. ∎

Executed: the general identity with `p_in`, `p_out` as symbols and the three
`d`'s as rational functions of `(p, q, r)` (E1); the four explicit laws'
ratios at `P_1, P_3, P_4` (uniform: `152/169, 136/121, 1`) and their distances
to the static law (E2); the type assignment of `P_1, P_3, P_4` and the three
values of `d` (E3).

*Reading.* The clock can only decide, at the first fork, how often to jump
across the square, and that decision cannot depend on more than the type of
one recorded value; everything else is fixed by the square's shape. Two
patterns the static law weighs equally then receive weights that differ by a
strictly monotone function of the diagonal normalizer.

## Corollaries R5 and R6

**R5.** The static plaquette law is not a convex combination of the sequential
laws `μ_σ`. *Proof.* A combination `Σ c_σ μ_σ` with `c_σ ≥ 0` has, on patterns
with `d_1 = d_2 = d`, the ratio `(c_path/6) d + (c_diag/36) d²` to `Π K`, strictly
increasing in `d` unless `c_path = c_diag = 0`. ∎ Executed by the four class
laws' ratios at `P_1, P_3, P_4` (E4).

**R6 (executed).** The parallel-growth law's plaquette law lies outside the
affine span of the four class laws: the rank of the five laws as vectors on
the `1296` patterns is five (E5). So value-dependent rates leave not only the
convex hull but the linear span of the order laws.

## The clause candidates (recorded, not adopted)

| candidate | what this note says about it |
|---|---|
| (a) "records form at a rate that does not depend on the nearest-neighbour conditions" | the uniform law; its finished law is the census note's mixture, at distance `0.0291…` from the static law on `2×3` (R2); on the plaquette never the static law (R4) |
| (b) "records form at a rate determined by the nearest-neighbour conditions" | a family; on trees one member (seeded) gives the static law exactly (R3); on the plaquette no member does, however the rates depend on the recorded values (R4) |
| (c) no clause | every rate-dependent statistic is registered data under the realized-state primitive; the witness shows which statistics those are |

The decision among them is the owner's. This note selects none.

## No-Go Discipline Gate

The negative sentences are R4 and R5 (the static plaquette law is unreachable
by any covariant rate law and by any convex combination of order laws). Both
are proved for every positive triple except the constant rule.

### N1 — Routes by which a rate clause could still reach the static law

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 value-dependent rates | bias the order by the recorded values | the only value-dependent decision that survives the type argument is `p_{type}`; the weight stays strictly increasing in `d` (R4) | RULED OUT AT SCOPE |
| 2 a larger window | different class structure | not claimed either way; the plaquette suffices for the clause table | narrowed |
| 3 the constant rule | `p = q = r` | `d_same = d_anti = d_orth`; the static law is uniform and so is every formation law | trivial |
| 4 non-memoryless clocks | a clock law with memory | outside the model (the campaign's clause is about rates) | not attempted; obligation named |
| 5 joint formation | several sites at once | the formation-unit block (next) | not this note |

### N2 — Wall-independence audit
Walls: the records-only reading, the product rule, positivity, the clock model. Independent; each defines the object.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: "registered data" in the clause table quotes the campaign's wording for candidate (c); none in the theorems.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| census note (main): Lemma L, Theorem 3 | the multiset key; the uniform mixture | R1's last clause; R2's uniform value | yes |
| block 01 (main): Theorem B; the cycle disagreement | equality with at most one recorded neighbour | R3 | yes |
| #8093's clock-and-rate block | the witness and the clause candidates | R2; the clause table | yes |
| block 13 (PR #8147, open; not an input) | the Green function needs the static reading | the motivation only | context only |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "never the static law on the plaquette" | executed: the ratios at `P_1, P_3, P_4` for four laws and symbolically for the general law | executed: every pattern of the plaquette (`1296`) and of `2×3` (`46656`) | executed: the 28 classes of `2×3`, the 542 of the cube, the 4 of the plaquette | executed: the three windows and two trees | proved for every positive triple except the constant rule (R4, R5); larger windows not claimed |

### N6 — Partial-closure paths and primitive scan
The realized-state primitive supplies no measure over orders (the campaign's reading); the clock law is the supplied object here and is not adopted. No primitive is a wall.

### N7 — Steelman
Hostile reviewer: "The witness is trivial given order dependence, and the no-go is one window." Reply: the witness is what the campaign asked for and is exhibited exactly; the no-go quantifies over every covariant rate law including value-dependent ones and is paired with the exact positive result on trees, so the clause table now has the precise boundary of what a rate sentence can buy. Conceded: larger windows are not classified.

### N8 — Cross-cycle echo
Block 01's cycle disagreement and block 13's parabolic kernel are the same fact seen twice: the record-by-record reading is causal, and causality is what a static Green function lacks. No structurally similar wall was retired.

## Falsifiers
- A rate vector for which the exact integral does not give `λ_x/Λ` (B1); a `2×3` mixture by classes that differs from the full enumeration (B2).
- Two of the three value-blind laws with the same `2×3` law, or a uniform distance differing from the census note's rational (C1–C2).
- A tree window on which the seeded law differs from the static law (D1).
- A pattern pair among `P_1, P_3, P_4` with equal type multisets and equal `d` at a non-constant rule, or a general-law identity whose difference is not strictly positive (E1–E3); a nonnegative combination of the class ratios that is constant (E4); a rank below five (E5).

## Boundaries and non-claims
This note exhibits the formation-rate witness and settles where a covariant rate law can reproduce the static law (trees) and where none can (a plaquette); it does not classify larger windows, does not treat clocks with memory or joint formation, does not select an order, rate, rule or coupling as physical, and adopts no clause. No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- The census note and block 01 (both on `main`): proposed, unaudited; the parts used (Lemma L; Theorem B) are restated and re-used as stated.
- Re-proved at scope: R1 (competing memoryless clocks), R3, R4, R5.
- Reference only (named, not used): Gillespie's construction of a continuous-time Markov chain by competing exponentials; the Eden model as the classical seeded growth.

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane and take it; no subagents). The control (`specs/supervisor_control_block14_rate_laws.py`) computed the plaquette laws, the `2×3` classes and mixtures, and the trees before the contract; the lens pass is in `GOAL_block14.md`; the primary seat wrote R1–R6 and the runner; the refuting pass (`CHECKER_block14_findings.md`) recomputed the plaquette mixture from the per-order weights by hand-derived formulas, the `2×3` seeded law by direct history enumeration without classes, and the type assignment of the three patterns by an independent geometric routine. Facts settled while executing: the first symbolic positivity test in the runner expanded the cofactor of `(d_anti − d_same)` in `1 − p` and saw negative coefficients; the proof's own form — the cofactor is a convex combination of `1/6` and `(d_anti + d_same)/36` — was executed instead (E2); the general identity was checked against all four explicit laws' exact ratios before the symbolic step (E1).

## Verification

```bash
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py --exact
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py --mutation static_reached_on_plaquette_claimed
```

Families: A authority and inputs; B the jump probabilities and the class mixtures; C the witness on `2×3`, the cube and the plaquette; D the trees; E the plaquette no-go (general identity, explicit laws, types, the class ratios, the rank); F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=22 FAIL=0`.
