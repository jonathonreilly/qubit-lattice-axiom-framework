---
claim_id: marked_tree_single_seed_dynamic_program_and_finite_rational_certificates_bounded_theorem_note_2026-09-17
claim_type: bounded_theorem
claim_scope: "Finite single-seed component reduction and exact level dynamic program; ZA/ZB/W1 minima, explicit W2/W3 tree ratios, four supplied-recursion rational point certificates and conditional scalar algebra. No global optimum, physical phase or completed negative certification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/marked_tree_single_seed_dynamic_program_finite_rational_certificates_check_2026_09_17.py
---

# Single-seed marked-tree dynamic programming and finite rational certificates

**Type:** bounded_theorem
**Status:** bounded-support; supplied finite objects, unaudited.
**Primary:** [exact finite checks](../scripts/marked_tree_single_seed_dynamic_program_finite_rational_certificates_check_2026_09_17.py).
**Cache:** [source-bound execution evidence](../logs/runner-cache/marked_tree_single_seed_dynamic_program_finite_rational_certificates_check_2026_09_17.txt).
**Recovery:** [complete original proofs, failures and deferred implications](work_history/review_loop/pr8176/README.md).

## Result up front

The finite component reduction and complete DP proof give the explicit minima
and tree constructions below. All five witness fixtures and four rational
certificates remain exact. ZA has20 marks; ZB has36. The finite ratio domain
is explicit, including the isolated-seed exception. The complete valid
uniform-budget implication is preserved readably with formal negative
certification deferred. No corrected-source execution occurred during author
preparation. Historical searches are recovery rather than live evidence.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite marked-tree optimization and supplied polynomial certificates"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "same-session affected source confirmation and bounded exact-source capture"
conditional_surface_status: "supplied finite objects only; broader negative certification deferred"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axioms memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework context:
one fixed covariant nearest-neighbor rule, probabilities varying with its
conditions, records forming and only records readable. It does not select
these finite objects. The primary reads and pins the context-only source
`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`.
No theorem from that context is required here. All automaton, graph, tree,
weights and polynomial definitions needed below are supplied explicitly;
historical campaign handoffs are not imported mathematical authority.

Declared objects.
- **Level time and the one-sided automaton.** Sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`. A **realization** is the output `η` of the one-sided two-level majority rule from a finite set of noise marks `ζ` in a box: `η_x = 1` if at least two predecessors are `1`, otherwise `η_x = 1` iff `x ∈ ζ`; sites outside the box are `0` (the same as the infinite lattice with marks only inside the box). A **seed** is a 1-site with no 1-predecessor, an **amplified site** one with exactly one, a **processed-type site** one with at least two.
- **The graph `G` and the counted family.** Arrows `{x, x − e_j}`, forks `{x, x ± (e_i − e_j)}`. A **marked tree of the family** at a realization is a subtree `T` of `G` through 1-sites containing `x` such that every non-seed node of `T` has exactly one downward arrow in `T`, to one of its 1-predecessors (an amplified node: to its single one), seeds have none, and the remaining edges are forks; `E(T)` counts the arrows at processed-type nodes, `A(T)` the amplified nodes, `S(T)` the seeds, `F(T)` the forks. The arrows of `T` form one arborescence per seed (levels decrease along arrows), and the forks join these arborescences into a tree, so `F = |S| − 1`. The **cost** for any real c is `E-3(|S|-1)-c|A|`, including trees with `|A|=0`. Write `m(c)` for its minimum over the finite nonempty family. The raw ratio statistic `rho(eta,x)` is the minimum of `(E-3(|S|-1))/|A|` over trees with `|A|>=1` ONLY when that restricted family is nonempty; otherwise it is undefined. We assert no universal coverage equivalence from this restricted statistic. An isolated seed has just its singleton tree, cost0 for every c and undefined rho. Ratios such as W3's `-12/17` remain negative raw statistics.
- **The component.** `C(η, x)` is the connected component of `x` in `G` restricted to the 1-sites of `η`.
- **The realizations.** `Z_A`: box `[0,4)²×[0,7)`, root `(3, 3, 3)`, marks `(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,2), (1,0,5), (1,2,0), (1,2,5), (1,3,1), (2,0,0), (2,1,3), (2,2,3), (2,3,3), (3,0,1), (3,0,2), (3,1,0), (3,1,3), (3,3,5), (3,3,6)` (46 ones). `Z_B`: box `[0,5)²×[0,8)`, root `(4, 4, 4)`, the 36 marks listed in the runner (69 ones). `W1`, `W2`, `W3`: the three supplied finite witnesses, restated in the runner.
- **The supplied recursion.** `D=(1+xU)^2(1+3xD)(1+yF)^6`, `U=(1+xU)^3(1+yF)^6`, `F=(1+xU)^3(1+3xD)(1+yF)^5`, `R=(1+xU)^3(1+3xD)(1+yF)^6`. These are declared finite polynomial products, not a supplied probability theorem. The scalar comparison condition is explicitly `x<4/27`. The deviations are defined in T4 below.

## Theorem T1 — finite component reduction and dynamic program



**T1.1 (the component lemma).** Every marked tree of the family at `(η, x)` lies in `C(η, x)`. *Proof.* A tree is a connected subgraph of `G` through 1-sites containing `x`. ∎

**T1.2 (one seed).** If `C(η, x)` holds exactly one seed `s`, then every tree of the family at `x` has `S(T) = {s}` and `F(T) = 0`, and a set `N` of 1-sites contained in `C(eta,x)` is the node set of a tree iff `x ∈ N` and every non-seed node of `N` has a 1-predecessor in `N` (an amplified node: its single one). *Proof.* The seeds of `T` are 1-sites of `C(η, x)` without a 1-predecessor, so `S(T) ⊆ {s}`; every arrow chain from a non-seed node descends and ends at a seed, so `s ∈ T` and the arrows form one arborescence, which is already connected: no fork can be added without a cycle, and `F = |S| − 1 = 0`. Conversely, given such `N`, choosing one arrow per non-seed node into `N` gives an acyclic graph (levels decrease) in which every node's chain ends at `s`; it is a tree containing `x`, and it is a subtree of `G` through 1-sites. ∎

**T1.3 (the dynamic program).** Under T1.2, `min_T [E − 3(|S| − 1) − c|A|]` equals the minimum over such node sets `N` of `Σ_{z ∈ N} cost(z)` with `cost = +1` (processed-type), `−c` (amplified), `0` (the seed). Ordering the levels of the component from the top down, the minimum is computed exactly by a dynamic program whose state at level `ℓ` is `N ∩ {level ℓ}`, with the transition requiring every non-seed node of the state to have a 1-predecessor in the next state, the root forced at its level, and the terminal state `{s}` at the seed's level (no 1-site of the component lies below `s`, since its chain could not reach `s`). *Proof.* The constraints on `N` are local between consecutive levels, and the cost is a sum over levels. ∎ Historical original-source execution (not a fresh corrected-source run): on `90` tiny realizations whose component holds one seed, the program equals a brute-force enumeration of the full family (node sets, arrow choices, fork forests between arborescences) in every case; on `51` tiny realizations with several seeds, forks lower the minimum or are needed for any tree in all `51` — the multi-seed part of the family is real, and the reduction is used only where T1.2 applies (B1–B2).

## Theorem T2 — exact finite minimum values

 In the realization `Z_A` the component of the root `(3, 3, 3)` has `42` of the `46` ones and exactly one seed, `(0, 0, 0)` (the other three seeds sit in components not joined to the root's by any arrow or fork). The exact minimum of `E − 3(|S| − 1) − c|A|` over every tree of the family is `6` at `c = 0`, `3/2` at `c = 3/4`, `3/50` at `c = 99/100`, `0` at `c = 1` and `−1/10` at `c = 101/100`; it is non-increasing and concave in `c` (a minimum of affine functions). An optimal tree at `c = 1` has `E = |A| = 6` and is exhibited and verified (C1, C3).

**T2.2 (`Z_B`).** In `Z_B` the component of `(4, 4, 4)` has `60` of the `69` ones and one seed; the minimum is `0` at `c = 1` and `2/25` at `c = 99/100`; an optimal tree has `E = |A| = 9` (C2).

**Proof and domain.** T1 enumerates precisely the node sets in each unique-seed component; its exact rational level transfer gives the displayed minima. Choosing one live predecessor per non-seed in the recovered node set gives the exhibited tree and its independently recounted E,A,S. A minimum of finitely many affine functions with slopes `-A<=0` is non-increasing and concave: for0<=lambda<=1, every tree's affine value at the interpolated c is at least the interpolation of the two minima, so the minimum is too. This is a finite optimization identity. The uniform-budget implication is preserved completely in the readable deferred argument, with formal negative certification withheld.

The root of ZA sits nine levels above the seed, whose three live successors are amplified. An optimal tree uses the chain `(2,2,3)->(2,1,3)->(2,1,2)->(1,1,2)->(1,0,2)->(1,0,1)->(0,0,1)->(0,0,0)`. Every root-to-seed chain includes an amplified node; the ratio domain is nonempty here. No assertion about a typical or infinite realization follows.

## Theorem T3 — explicit finite tree ratios

W1 has a single-seed component, minimum0 at c=3/4 and positive minimum at74/100, with an exhibited tree E=6,A=8,S=1. Its restricted ratio minimum is3/4. Indeed the zero minimum implies each E-(3/4)A>=0, while the exhibited tree attains equality and has A>0. The positive minimum at74/100 is a separate finite check.

W2 carries the explicitly listed tree E=7,A=11,S=2,F=1, ratio4/11. W3 carries the explicitly listed tree E=9,A=17,S=8,F=7, numerator `E-3(S-1)=-12`, raw ratio `-12/17`. These two displayed ratios are witness values, not asserted minima. They are not silently clamped. Their full arrow/fork fixtures are retained in the primary.

**Proof.** Rebuild the finite automaton in increasing level order. For each listed arrow check that its lower endpoint is a live predecessor; count exactly one such arrow from every non-seed and none from seeds. Each fork joins live siblings. The endpoint graph contains the specified root, is connected and has one fewer edges than nodes, hence is a tree. Recounting processed, amplified and seed nodes gives the integers above, and division gives the ratios. T1 supplies the W1 minimum. No global construction or sharpness theorem is invoked. ∎

## Theorem T4 — four supplied-recursion certificates and scalar identities

For p,q,r>0 define
`d1=1-p^3/(p^3+q^3+4r^3)`,
`d2=1-p^2*q/(p*q*(p+q)+4r^3)`,
`d3=1-p^2*r/(r*(p^2+q^2)+r^2*(p+q)+2r^3)`.
Set epsilon1=d1,epsilon2=max(d2,d3), x=t+epsilon2/t, y=epsilon1/t^3.
These are supplied rational definitions. Equivalently enumerate six signed
coordinate axes with pair weights p for equal, q for opposite and r for
perpendicular axes: predecessor triples (a,a,a),(a,a,-a),(a,a,b) with b
perpendicular to a give the three denominators by summing their six product
weights. This is finite algebra, not a physical rule selection.

Each key below is ONE parameter point; each value is `(t,Dbar,Ubar,Fbar)`:

```python
{
        (453, 1, 2): (Fraction(77, 1000), Fraction(530590310409, 62500000000), Fraction(2581678475343, 1000000000000), Fraction(11343276538931, 1000000000000)),
        (232, 1, 1): (Fraction(19, 250), Fraction(3177134369, 390625000), Fraction(2565214474763, 1000000000000), Fraction(10810979357851, 1000000000000)),
        (905, 2, 4): (Fraction(39, 500), Fraction(8819680764063, 1000000000000), Fraction(2607018650019, 1000000000000), Fraction(2955282963089, 250000000000)),
        (677, 1, 3): (Fraction(77, 1000), Fraction(8860200884553, 1000000000000), Fraction(1306536163573, 500000000000), Fraction(5937627036121, 500000000000)),
    }
```

`Fraction(n,d)` means n/d. Substitute into the four declared polynomials
and clear their positive denominators. Each triple dominates its three
right sides, all three entries are at least1, x<4/27 and epsilon1*Rbar<1/100000.
The primary retains those exact rational checks. These four points do not
establish an interval, optimality, a stochastic bound or an ordered phase.

The completed-square identity
`t*(4/27-t)=4/729-(t-2/27)^2`
gives maximum4/729 on[0,4/27], attained at2/27. For c>=1 and0<t<1,
`t^c<=t`. Thus, CONDITIONAL on epsilon2>0 and `t+epsilon2/t^c<4/27`,
`epsilon2<t^c*(4/27-t)<=t*(4/27-t)<=4/729`.
On(p,1,2), `d3=(2*p+11)/(p*p+2*p+11)`. For real p>0,
`d3<4/729` is equivalent to `4*p*p-1450*p-7975>0`, by positive-denominator
cross multiplication, or `p>(725+sqrt(557525))/4`. Direct substitution gives
`d3(367)>4/729>d3(368)`. The rounded necessary condition p>=368 is only
for positive INTEGER p; `p=36799/100` passes the scalar inequality but is
not a full recursion certificate. The broader negative route inference is
readable and deferred; no physical conclusion is imported. ∎

## No-Go Discipline Gate — DEFERRED applicability record

N1: component containment/extra seeds and DP coverage are actual arguments;
the independent original review used a separate bottom-up integer DP, direct
sequential automaton and pairwise geometry, full finite tree validation, and
six-menu/port enumeration. These are not five normalized attacked families
against one negative target. Different families are outside scope; uniform
attainment at c=1 remains open; c>1 possibilities strengthen the lower bound;
point certificates address another question. No quota PASS is invented.
N2: no repository wall is imported. N3: finite outside-zero domain, graph,
marks, cost and restricted ratio domain are explicit. N4: axiom source is
framework context; product-law source is context only; open handoffs are
historical. N5: finite sites, subsets and rational points are tested when the
primary is captured; no spectral modes or infinite lattice is executed.
N6: preserve the original branch and complete readable negative argument.
N7: worst-case finite implications do not identify typical configurations or
supply a probability count. N8: historical unseeded/seeded searches and the
failed general DP stay exact recovery; sampled maxima are not global values.

## Boundaries and non-claims

This note retains exact finite marked-tree minima, explicit witness ratios and four supplied polynomial certificates; no physical rule, order or coupling is selected.

The ratio statistic is defined only on its nonempty positive-amplification domain; zero-amplification costs remain defined and negative witness ratios are not clamped.

Formal negative certification and global construction conclusions remain deferred; finite checks and point certificates do not supply five closed attack families.

## Imports

Finite graph connectivity, finite dynamic programming, exact rational
arithmetic and concavity of a finite minimum of affine functions are proved
or used at the stated definition level. No stochastic domination, count
coverage, global upper budget or physical application is supplied here.
The original full proofs and historical attempts are preserved in recovery.

## Verification

Expected stdout is `TOTAL: PASS=22 FAIL=0`: the original19checks plus an
isolated-seed domain check, exact36-mark check and real-parameter scalar
boundary check. The original seeded tiny-realization batch is unchanged;
its accepted sample counts are reported at runtime. The program writes no
JSON. Only the three changed-claim targets need new mutation consideration;
unchanged historical mutations are retained, not routinely rerun.

```bash
python3 scripts/marked_tree_single_seed_dynamic_program_finite_rational_certificates_check_2026_09_17.py
python3 scripts/marked_tree_single_seed_dynamic_program_finite_rational_certificates_check_2026_09_17.py --list-mutations
```
