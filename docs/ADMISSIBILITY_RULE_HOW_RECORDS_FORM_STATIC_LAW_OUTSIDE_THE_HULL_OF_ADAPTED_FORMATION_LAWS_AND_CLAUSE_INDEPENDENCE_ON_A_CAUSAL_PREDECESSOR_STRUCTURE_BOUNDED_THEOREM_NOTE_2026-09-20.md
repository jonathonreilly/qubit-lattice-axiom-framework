---
claim_id: admissibility_rule_how_records_form_static_law_outside_the_hull_of_adapted_formation_laws_and_clause_independence_on_a_causal_predecessor_structure_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "For the six-axis rule of block 01 with positive weights (p, q, r) not all equal, on finite windows: (T1) an ADAPTED formation scheme forms one site at a time, the next site drawn from any law pi(. | F, v_F) that may depend on the formed set and its records (value-blind orders, clock laws with value-dependent rates and deterministic strategies included), each new record drawn from the rule given the recorded neighbours. With N_0 = 6, N_k = p^k + q^k + 4 r^k, D_sigma = prod_x N_{k_x(sigma)} and D_min its least value over orders: sum_s prod_{i<=k} phi(s, a_i) <= N_k for all recorded values, with equality exactly when the a_i are equal (or, only if p = q, antipodal); Z <= D_sigma for every order, strictly when some site reads two neighbours; every constant pattern has mu_S(v^b) <= p^|E|/D_min; and if the window's graph has a cycle then Z < D_min, so mu_S(v^b) <= (Z/D_min) mu_stat(v^b) < mu_stat(v^b) for every adapted scheme and the static law lies outside the closed convex hull of the adapted formation laws, separated by the indicator of the constant patterns with margin 6 p^|E| (1/Z - 1/D_min) (exact values on the plaquette, the 2x3 rectangle and the cube at (3,1,2), (5,2,4), (7,3,5); on windows without a cycle Z = D_min). (T2) On a finite predecessor structure (a directed acyclic graph; a site forms only after all its predecessors and reads exactly them) every readiness-gated adapted scheme, every clock law on the ready sites with any positive value-dependent rates, and every joint formation of an antichain gives the same law prod_x K(v_x | v_pa(x)); on level-ordered Z^3 two sites of one level are never nearest neighbours, so forming a level jointly is forming it site by site. CONTROL: on the undirected path of 3, where the read-set depends on the order, forming the middle site last changes the law (total variation 1/72 at (3,1,2)). The note does not say which predecessor structure the axioms intend."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_how_records_form_static_law_outside_adapted_hull_clause_independence_causal_structure_2026_09_20.py
---

# How records form: the static law is outside the hull of every adapted formation law on a window with a cycle, and on a causal predecessor structure every rate, order and unit clause gives one law

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact on finite windows; conditional on the named supplied readings; unaudited)

## Result up front

The axioms say that records form and leave open how: in which order, at which rate, one site at a time or several. Blocks 14, 15 and 16 (PRs #8148, #8149, #8150) recorded witnesses that these choices change the law, and block 16 left one case open: formation orders that depend on the values already recorded. Two statements settle what is left.

1. **The static law is never a formation law, however adaptively the order is chosen (T1).** Let the next site be chosen by any rule that looks at everything recorded so far. On any window whose graph has a cycle, every such scheme gives each constant pattern strictly less weight than the static law does, by the explicit factor `Z/D_min < 1`. So the static law is outside the closed convex hull of all adapted formation laws, and one functional separates it for every weight: the indicator that all records agree. On a window without a cycle `Z = D_min` and the separation disappears, as block 14 found for trees.
2. **Under a fixed predecessor structure the clauses do not matter (T2).** Suppose each site has a fixed set of predecessors, forms only after them, and reads exactly them. Then the order among ready sites, any clock rates (value-dependent included), and forming an antichain jointly all give the same law: the product of the rule's kernels. On level-ordered `Z³` two sites of one level are never neighbours, so a level formed at once is a level formed site by site.
3. **What is left of "how".** The clause witnesses of blocks 14 and 15 are all cases in which the clause changes which neighbours a forming record reads. Once that is fixed nothing else changes the law. The open question about how records form is therefore one question: which neighbours are already written when a site is written.

For the supplied six-axis positive pair weights (not all equal), the static law lies outside the closed convex hull of adapted single-site formation laws on a finite window with a cycle. On a fixed causal predecessor structure, readiness-gated adapted schedules give the product law; joint ready-antichain draws must use the explicitly factorized kernel. Arbitrary correlated joint draws are excluded. No predecessor structure is selected by this result.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 16 (PR #8150): 'value-dependent order laws open beyond the plaquette'; blocks 14, 15 (PRs #8148, #8149): the formation-rate and formation-unit clause candidates recorded, not adopted; the owner's standing question: HOW records form (order, unit, rate)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "block 16's open case closed (adapted schemes on every window with a cycle); the rate, order and unit clauses shown immaterial under a fixed predecessor structure. Next: the one remaining choice, the predecessor structure (which bonds point which way), is the owner's; the infinite-volume separation of the static law from the monotone formation laws (relative-entropy density) is a refereed probe input not yet written"
conditional_surface_status: "T1 and T2 proved for every finite window and every positive not-all-equal six-axis triple; exact values executed on five windows at three triples; conditional on the records-only reading and block 01's rule as supplied; no statement about which predecessor structure the axioms intend"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." and "Records form.". Block 01 (on `main`, proposed and unaudited) supplies the rule as a product of pair weights, the formation conditional and the static law of a product rule.

- **Window, rule.** A finite graph `(Λ, E)` of sites with nearest-neighbour edges; menu `M` = the six axes; `φ(a, b) = p, q, r` for equal, opposite, orthogonal axes, positive and not all equal; `Z₁ = p + q + 4r`. The static law `μ_stat(v) = Π_{⟨xy⟩} φ(v_x, v_y)/Z`.
- **Formation conditional.** A site forming with recorded neighbours `A` draws `a` with probability `Π_{y∈A} φ(a, v_y) / Σ_s Π_{y∈A} φ(s, v_y)` (uniform if `A` is empty).
- **Adapted scheme `S`.** For every formed set `F ≠ Λ` and records `v_F`, a probability law `π(· | F, v_F)` on the unformed sites; the scheme draws the next site from it, draws its record from the formation conditional given `N(x) ∩ F`, and repeats. Value-blind orders (block 16), clock laws `π(x | F, v_F) = λ_x/Σ_y λ_y` with any positive rates (block 14) and deterministic strategies are special cases. `μ_S` is the law of the finished pattern.
- **Order quantities.** `k_x(σ)` = the number of neighbours of `x` formed before it in the order `σ`; `N_0 = 6`, `N_k = p^k + q^k + 4r^k`; `D_σ = Π_x N_{k_x(σ)}`; `D_min = min_σ D_σ`. `v^b` = the pattern with every record equal to `b`.
- **Predecessor structure.** A finite set with a parent set `pa(x)` for each site, acyclic. A site is **ready** when its parents are formed; it then draws its record from the formation conditional given exactly `pa(x)`. A readiness-gated adapted scheme has `π` supported on ready sites. An **antichain unit** is a set of ready sites formed jointly from the law proportional to `Π_{x∈U} Π_{y∈pa(x)} φ(v_x, v_y)`.

The inequality of step 3 below is a case of the inequality of Hölder, proved here from the inequality of the arithmetic and geometric means; laws of the static kind are those of Gibbs; the product law of T2 is the factorization of a directed Markov structure. None is used as authority.

## Prior art and what is new

Block 14 proved that on the plaquette no covariant rate law is the static law and that on trees seeded growth is the static law; block 15 compared sequential and joint formation; block 16 proved that the static law is not a mixture of value-blind order laws on any window with a cycle and left value-dependent orders open beyond the plaquette. What is new: (i) the adapted case in full generality with one separating functional and an explicit margin, by a representation of `μ_S` as a pattern-dependent mixture of order laws evaluated only at constant patterns, where every order law has the closed form `p^{|E|}/D_σ`; (ii) the clause-independence theorem, which turns the clause questions of blocks 14 and 15 into a single question about read-sets. Both statements came back from the probes' derivation rounds on `ai/probes` (`static-law-in-the-hull`, `causal-clauses`, `formation-order-independence`: attempts by Claude Opus and Grok workers, refereed across model families); both are re-proved here and re-computed with the supervisor's own code.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | `μ_S(v^b) ≤ p^{|E|}/D_min`; `Z < D_min` with a cycle; the hull | representation; constant patterns; the product inequality; elimination of sites | B |
| T2 | one law under a predecessor structure; antichains; level-ordered `Z³` | the same representation with order-free factors | C |

## Theorem T1 — the static law is outside the hull of the adapted formation laws

**Step 1 (representation).** For every adapted scheme and pattern `v`, `μ_S(v) = Σ_σ ρ_S(σ | v) μ_σ(v)`, where `μ_σ` is the formation law of the order `σ`, `ρ_S(σ | v) = Π_j π(σ_j | {σ_1…σ_{j−1}}, v_{σ_1…σ_{j−1}})`, and `Σ_σ ρ_S(σ | v) = 1` for each `v`. The event that the finished pattern is `v` is the disjoint union over `σ` of "the sites form in the order `σ` with the records `v`", whose probability is the product of the choice probabilities and of the formation conditionals; for fixed `v` the choice probabilities are those of a sequential choice and sum to one.

**Step 2 (constant patterns).** `μ_σ(v^b) = p^{|E|}/D_σ` and `μ_stat(v^b) = p^{|E|}/Z`. A site reading `k ≥ 1` neighbours, all equal to `b`, draws `b` with probability `p^k/N_k`, since `φ(s, b)` takes the value `p` once, `q` once and `r` four times; a site reading none draws `b` with probability `1/6`; every edge is read once, at its later endpoint.

**Step 3 (the product inequality).** For `a_1, …, a_k ∈ M`: `Σ_s Π_i φ(s, a_i) ≤ N_k`, with equality exactly when the functions `φ(·, a_i)` coincide. For non-negative numbers `Π x_i ≤ (1/k) Σ x_i^k`, with equality only when all are equal; apply it to `x_i = φ(s, a_i)` and sum over `s`, using `Σ_s φ(s, a)^k = N_k` for every `a`. Two orthogonal `a_i` give different functions unless `p = q = r`; two opposite ones unless `p = q`.

**Step 4 (`Z ≤ D_σ`).** Sum the static weight over the sites in the reverse of the order `σ`: the last site's sum is `Σ_s Π_{y∈A} φ(s, v_y) ≤ N_k` by step 3 (equal to `6` or `Z₁` when `k = 0, 1`), and the remaining weight is the static weight of the window without that site. By induction `Z ≤ D_σ`, strictly if some site has `k ≥ 2`, because its two read neighbours carry orthogonal records in some patterns of positive weight.

**Step 5 (a cycle forces `k ≥ 2`).** In any order, the site of a cycle that forms last reads its two neighbours on the cycle. So with a cycle `Z < D_σ` for every order, and `Z < D_min`.

**Conclusion.** By steps 1 and 2, `μ_S(v^b) ≤ p^{|E|}/D_min = (Z/D_min) μ_stat(v^b)`. For `f(v) = 1[v` is constant`]`, every law in the closed convex hull of the adapted formation laws has `E f ≤ 6p^{|E|}/D_min`, and the static law has `E f = 6p^{|E|}/Z`, larger by `6p^{|E|}(1/Z − 1/D_min) > 0`. ∎

At `(3,1,2)`: plaquette `Z = 20784`, `D_min = 22464`; `2×3` rectangle `6000000`, `7008768`; cube `6982520832`, `10933678080`; path of 3 and star of 4: `Z = D_min = 864` and `10368`. On the plaquette the constant pattern has static weight `27/6928` and at most `3/832` under any adapted scheme; 60 random adapted schemes computed exactly stay at or below it, No attainment by the random sample is claimed.

## Theorem T2 — under a predecessor structure every clause gives one law

For a readiness-gated adapted scheme the representation of step 1 holds with `μ_σ(v)` replaced by `Π_x K(v_x | v_{pa(x)})`, because whenever a site forms its parents are formed and it reads exactly them, whatever the order. This factor does not depend on `σ`, so `μ_S(v) = Π_x K(v_x | v_{pa(x)}) · Σ_σ ρ_S(σ | v) = Π_x K(v_x | v_{pa(x)})`. Clock laws on the ready sites are such schemes (the jump chain of the clocks). For an antichain unit of ready sites the joint law is proportional to `Π_{x∈U} Π_{y∈pa(x)} φ(v_x, v_y)`, which has no factor joining two sites of `U`, so it is the product of the one-site formation conditionals, and inserting joint steps changes nothing. On `Z³` with parents `x − e_j`, the displacement between two sites of one level has coordinate sum zero, whereas a nearest-neighbour displacement has coordinate sum +1 or -1: they are not neighbours, and a level is an antichain. ∎

**Control.** On the undirected path of three sites, where a forming site reads whichever neighbours are recorded, the order that forms the middle site last makes it read two neighbours, and the law differs from the order that forms it first: total variation `1/72` at `(3,1,2)`. What changed is the read-set, not the rate or the unit.

## Historical refuting control (not fresh evidence)

`specs/supervisor_control_block38_refuter.py`: `Z` of the `2×3` rectangle by enumerating all `6⁶` patterns (`6000000`) against the least `D_σ` over all 720 orders (`7008768`); a linear program finds no mixture of the 24 value-blind order laws of the plaquette equal to the static law; an adversarial adapted scheme that always forms next the site whose recorded neighbours agree gives the constant patterns probability `0.0201 ± 0.0003` over `2·10⁵` runs, against the bound `0.02163` and the static value `0.02338`; a value-dependent readiness-gated scheme on the diamond reproduces the product law within sampling error.

## No-Go Discipline Gate

T1 is a negative sentence (the static law is not a mixture of adapted formation laws); the gate applies.

### N1 — Routes by which the sentences could fail
1. *A wider class of schemes* — schemes that form several neighbouring sites jointly from a law other than the rule's conditionals are outside T1; block 15 treats joint formation of connected units, and the whole window as one unit is the static law by definition.
2. *Equal weights* — for `p = q = r` the rule is constant and every law is uniform; excluded by hypothesis.
3. *Windows without a cycle* — `Z = D_min` there and orders that read one neighbour at a time give the static law (block 14); T1 claims nothing for them.
4. *The read-set* — T2 assumes the read-set is the fixed parent set; on an undirected window the read-set depends on the order and the control shows the law changes.
5. *Infinite volume* — not treated; both statements are finite.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None: the inputs are block 01's rule, formation conditional and static law.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the rule's sentences; "Records form." | yes (premise) |
| block 01 (`main`) | the rule, the formation conditional, the static law | yes (premise, proposed) |
| blocks 14, 15, 16 (open PRs #8148–#8150) | the clause candidates; the value-blind case; the open case closed here | placement |
| blocks 05, 08–12 (PRs) | the level-ordered law to which T2 applies | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "static law outside the adapted hull on windows with a cycle; one law under a predecessor structure" | executed: the product inequality and its equality cases for every tuple, `k ≤ 4`, four triples | executed: every order of the plaquette and the rectangle | not applicable | executed: `Z`, `D_min` on five windows at three triples; exact laws of 60 adapted and 24 gated schemes | proved for every finite window and every positive not-all-equal triple; the predecessor structure is not decided |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no order, rate, unit or predecessor structure; none is a wall.

### N7 — Steelman
Hostile reviewer: "T2 is the chain rule for a directed graphical model and T1 is one application of a classical inequality; neither needs a note." Reply: the campaign carried three clause questions as separate open items with separate witnesses, and block 16 left the adapted case open. These two short arguments close the adapted case everywhere and collapse the three questions into one, the read-set, which is the form in which the owner can decide it.

### N8 — Cross-cycle echo
Block 14's tree equality is the case `Z = D_min`; block 16's flip lemma is the value-blind shadow of step 4; block 05's single law for the monotone class and block 09's eight corner laws are T2 for eight predecessor structures.

## Falsifiers
- A tuple of recorded values violating the product inequality, or an equality case outside the stated ones (B1).
- A window with a cycle where `Z ≥ D_min`, or a window without one where `Z ≠ D_min` (B2).
- An order whose constant-pattern weight differs from `p^{|E|}/D_σ`, or an adapted scheme giving a constant pattern more than `p^{|E|}/D_min` (B3–B4).
- A readiness-gated scheme on a predecessor structure whose law differs from the product of kernels; an antichain whose joint law is not the product; two same-level sites of `Z³` that are neighbours (C1–C2).
- The undirected control giving equal laws (C3).

## Boundaries and non-claims
For the supplied six-axis positive pair weights (not all equal), the static law lies outside the closed convex hull of adapted single-site formation laws on a finite window with a cycle. On a fixed causal predecessor structure, readiness-gated adapted schedules give the product law; joint ready-antichain draws must use the explicitly factorized kernel. Arbitrary correlated joint draws are excluded. No predecessor structure is selected by this result. It makes no infinite-volume statement, does not treat joint formation of connected units, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises. Block 01 (on `main`): the rule, the formation conditional, the static law; proposed, unaudited. Blocks 05, 08–12, 14–16 as evidence addresses.
- Named standard imports at definition level: the inequality of the arithmetic and geometric means (from which the case of Hölder's inequality used here is proved); the law of total probability over formation orders; variable elimination for an exact partition function.
- Reference only: Hölder (1889); the factorization of directed Markov structures.

## Review record — original author provenance
Supervisor-run block (owner 2026-09-20: "harvest again, and then write any blocks that are meaningful / valuable"). Lens: the owner's standing question is how records form; two refereed probe results bear on it directly and are short enough to check completely. The supervisor re-derived both arguments before computing, then computed `Z` and `D_min` with its own elimination code; the numbers agree with the workers' (`27/6928`, `6982520832`, total variation `1/72`). Refuting pass: brute enumeration of `Z`, a linear program for the value-blind case, and Monte Carlo of an adversarial adapted scheme and of a gated scheme, all disjoint from the runner's exact recursions. Fold: the statement that T2's schemes are a subclass of T1's (every bond oriented, children never before parents) was added so that T1 applies to every causal law on a window with a cycle. Mutation census: seven mutations, each failing in its own family.

The original support scripts and experimental outputs remain recoverable on the PR branch. Historical reports are not the fresh landing certificate.

## Verification

```bash
python3 scripts/admissibility_rule_how_records_form_static_law_outside_adapted_hull_clause_independence_causal_structure_2026_09_20.py
python3 scripts/admissibility_rule_how_records_form_static_law_outside_adapted_hull_clause_independence_causal_structure_2026_09_20.py --list-mutations
python3 scripts/admissibility_rule_how_records_form_static_law_outside_adapted_hull_clause_independence_causal_structure_2026_09_20.py --mutation causal_gate_removed
```
