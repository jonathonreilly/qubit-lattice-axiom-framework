---
claim_id: rooted_marked_tree_extension_seed_induction_and_relaxed_lifted_tree_certificates_bounded_theorem_note_2026-09-17
claim_type: bounded_theorem
claim_scope: "Finite rooted extension/seed constructions and exhaustive conditional induction; exact finite predecessor profiles; relaxed lifted-tree upper-bound injection and eight point certificates;120 finite exact all-parent comparisons. No universal budget converse, local characterization, improved formation region or completed negative certificate."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - six_axis_two_level_domination_extended_explanation_tree_and_four_rational_certificates_bounded_theorem_note_2026-09-16
runner: scripts/rooted_marked_tree_extension_seed_induction_relaxed_lifted_certificates_check_2026_09_17.py
---

# Rooted marked-tree lemmas and relaxed lifted-tree certificates

**Type:** bounded_theorem
**Status:** proposed_retained; unaudited conditional finite mathematics.
**Primary:** [exact finite checks](../scripts/rooted_marked_tree_extension_seed_induction_relaxed_lifted_certificates_check_2026_09_17.py).
**Cache:** [exact-source evidence](../logs/runner-cache/rooted_marked_tree_extension_seed_induction_relaxed_lifted_certificates_check_2026_09_17.txt).
**Recovery:** [complete original history and deferred science](work_history/review_loop/pr8177/README.md).

## Result up front

The full extension, seed and induction proofs below establish a sufficient
route from the open tight-sibling statement to the unit budget on explicitly
finite realizations. The original polynomial is retained as a RELAXED upper
sum with a complete injection proof, not an exact occupancy count. Its eight
rational certificates remain unchanged. Exact profiles distinguish ZA from
ZB; the fixed sample is140 realizations for the rooted lemmas and120 equal
minima from60 realizations/two costs for the all-parent restriction.
No corrected-source primary, mutation or historical solver was run during
author preparation. Earlier evidence remains historical, not fresh capture.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite rooted induction and restricted admissible-tree existence"
source_of_blocker_text: review_loop
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "original same-session affected confirmation and bounded exact-source capture"
conditional_surface_status: "finite outside-zero window; open tight-sibling residual and restricted admissibility"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework vocabulary.
The [product-rule parent](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies the six-axis
product conditional used to interpret the displayed weights. The
[two-level domination and explanation-tree theorem](SIX_AXIS_TWO_LEVEL_DOMINATION_EXTENDED_EXPLANATION_TREE_AND_FOUR_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md)
supplies the full-slot comparison and conditional application framework.
Its hypotheses are p>=q>0,r>0, the six signed-axis menu, records-only level
order, independent site draws conditional on the previous level and an
initial all-a plane. Its finite-cone localization and infinite-plane formation
conclusion do not automatically apply to a new restricted family. That family
needs the separate admissible-tree existence premise stated below. No source
from an unlanded sibling is imported as a theorem; all finite data are explicit.
The landed finite construction lower bound5/3 does not establish global
sharpness2; the parent upper2 theorem retains its own supplied scope.

- **Finite domain.** Fix a finite box B in Z3, with sites outside B fixed to0.
Process its sites in increasing `tau(z)=z1+z2+z3`: a site is1 if at least two
of its predecessors z-ej are1, or if it is marked. This is the supplied
finite model; no full forward all-Z3 interpretation is asserted. A live
site is a seed/amplified/processed according to0/1/at least2 live predecessors.
- **Graph and family.** Arrows join live predecessors; forks join live siblings
z and z±(ei-ej). A family tree contains the queried live root; every non-seed
has exactly one downward arrow to a live predecessor, a seed none. Remaining
edges are forks. E counts processed arrows,A amplified nodes,S seeds,F forks.
Descending arrow chains end at seeds; their components are arborescences.
Contracting them in a tree gives F=|S|-1. Cost is E-3(|S|-1)-A.
- **Rooted value.** v(z) is the minimum cost over trees whose nodes have level
at most tau(z). A downward path always supplies a finite tree, so this
minimum is attained. For a seed, its singleton gives v<=0. A processed site
is tight if v=0. H means v<=0 for processed sites and v<=-1 for amplified
sites. H implies a unit-budget tree by forgetting the cap; no converse used.
- **Restriction.** A child of u is a site whose arrow points to u. At most
one processed child is allowed at EVERY node. The lifted relaxation below
forgets incoming occupancy, not the original meaning of this restriction.
- **Fixtures.** ZA(box4x4x7,root3,3,3,20marks), ZB(box5x5x8,root4,4,4,36marks)
and the retained W1/W2/W3 coordinates are exactly listed in the primary.
They are supplied finite data; historical sources/searches are archived.

## Theorem T1 — finite extension, seed construction and sufficient induction



**T1.1 (extension).** For a non-seed site `z` and any 1-predecessor `u`: `v(z) ≤ 1 + v(u)`, and `v(z) ≤ −1 + v(u)` if `z` is amplified. *Proof.* Take a rooted tree `T` of `u` with `cost(T) = v(u)`; all its nodes lie at levels `≤ τ(u) < τ(z)`, so `z ∉ T`, and `T ∪ {z}` with the arrow `z → u` is a tree of the family rooted at `z` (for an amplified `z`, `u` is its single 1-predecessor); its cost is `cost(T) + 1` or `cost(T) − 1`. ∎

**T1.2 (seed lemma).** Let `z` be processed with a seed 1-predecessor `s` and another 1-predecessor `w`. If `w` is processed, then for any 1-predecessor `p` of `w`: `v(z) ≤ v(p) − 1 ≤ −1` given (H) at `p`; if `w` is amplified with predecessor `q`: `v(z) ≤ v(q) − 3`. If `z` has two seed 1-predecessors `s, s'`: `v(z) ≤ −2`. *Proof.* Take a rooted tree `T_p` of `p` of cost `v(p)`; its nodes lie at levels `≤ τ(p) = τ(z) − 2`, so `s, w, z ∉ T_p`. Then `T := T_p ∪ {w, s, z}` with arrows `z → w`, `w → p` and the fork `s—w` (siblings, both predecessors of `z`) is a tree of the family: `s` is its own arborescence, `w` joins `p`'s, the fork joins the two, and `F = |S| − 1` is preserved. Its cost is `v(p) + 1 + 1 − 3`. For amplified `w` the same with `w → q` gives `v(q) − 1 + 1 − 3`. For two seeds, `{z, s, s'}` with `z → s` and the fork `s—s'` costs `1 − 3`. ∎

**T1.3 (the inductive step and the reduction).** Assume (H) at all sites below level `ℓ`, and let `z` be a non-seed site at level `ℓ`. If `z` is amplified, `v(z) ≤ −1` by T1.1. If `z` is processed: with an amplified 1-predecessor `u`, `v(z) ≤ 1 + v(u) ≤ 0`; with a seed 1-predecessor, `v(z) ≤ −1` by T1.2; with a processed 1-predecessor `w` of `v(w) ≤ −1`, `v(z) ≤ 0` by T1.1. The only case left is a processed `z` whose 1-predecessors are all processed with `v = 0` — the **tight-sibling case**. For each fixed finite realization, the following statement implies H by induction from the lowest level (all live sites there are seeds). At an amplified site the predecessor is either a seed of value at most0 or satisfies H; the cases above cover every processed site except the stated residual. Conversely H directly implies the residual statement. Thus H is equivalent to that residual statement on this finite domain and is SUFFICIENT for the unrooted unit budget. No converse from the unrooted budget, no truncation equivalence and no all-Z3 extension is asserted.

> **Tight-sibling lemma (open).** A processed site all of whose 1-predecessors are tight processed sites has a rooted tree of cost at most zero.

Historical original-source finite outcomes (B1–B3; fresh corrected evidence is separate): on `140` tiny realizations with every rooted tree enumerated exactly, the extension inequalities hold at `357` predecessor pairs and `121` amplified sites, the seed lemma's instances at `15` single-seed and `78` double-seed cases, (H) at all `788` sites, and the tight-sibling case does not arise.

**Conjectural local characterization.** In a single-seed component the no-fork reduction permits optimization over predecessor-closed node sets. If an optimal set at a fixed cap omits an amplified site whose predecessor is included and whose level does not exceed that cap, adding the site and its arrow lowers cost by1. Thus saturation holds only for such admissible sites BELOW OR AT THE CAP. This observation does not prove the original formula reducing the residual to marks near z; sites at z's level, connectedness and competing optimal sets require control. The proposed local saturated-support characterization remains conjectural, and the tight-sibling residual remains a full-strength open obligation. The complete original proposal is readable in recovery.

## Theorem T2 — exact finite rooted profiles

For ZA the root(3,3,3) has value0 and its three processed predecessors have
values[-1,-1,-1]. For ZB the root(4,4,4) has value0 and predecessor values
[-1,-1,0]. Its second tight site(4,4,3) has three predecessors[-1,-1,-1].
These are exact capped single-seed calculations on the two declared fixtures.

**Proof by finite level transfer.** Restrict candidate nodes to levels at
most the queried root level; predecessor kinds are unchanged because every
predecessor is one level lower. In a one-seed component any family tree has
one descending arborescence and no forks: each downward chain terminates at
the unique seed, so adding a fork would create a cycle. Conversely a node
set containing the root and one live predecessor for each non-seed permits
one arrow per non-seed and yields that tree. The cost is the sum of+1 at
processed nodes,-1 at amplified nodes,0 at the seed. Transfer over subsets
of successive levels, requiring a predecessor for each chosen non-seed,
forcing the queried root and terminating at the singleton seed, therefore
enumerates exactly the finite rooted family. Exact rational minimization
gives the displayed values (C1,C2). They establish the profiles at these
sites only, not absence of tight-sibling sites in every realization. ∎

## Theorem T3 — relaxed lifted-tree upper sum and eight certificates

**Successor-slot identity.** For n labelled successor positions, each empty,
processed(weight xP*U), or amplified(weight xA*U), assignments with at most
one processed occupant have sum
`U_n=(1+xA*U)^n+n*xP*U*(1+xA*U)^(n-1)`.
Proof: separate zero processed occupants from the choice of its unique slot;
all other slots are independently empty or amplified. This identity is exact
for THESE remaining slots, not a complete occupancy rule at a visited vertex.

**Relaxed family and injection.** Root a finite restricted lattice tree at
the queried site, label every edge by its displacement (three down, three up,
six sibling/fork labels), and label each arrow P or A by its originating
node kind. The unique root path to each vertex gives a word of these labels.
Reading the displacements recovers every original vertex and edge, so the
map from rooted labelled lattice trees to lifted word trees is injective and
weight preserving. The original tree has no cycle and distinct vertices;
forgetting geometric collisions and consistency between repeated projected
locations only ADDS possible lifted trees.

At the root, three successor slots remain, at most one of three predecessor
slots can be chosen, and six fork slots remain. On entering by a down edge
(D), the reverse successor slot is occupied, leaving two successors, at most
one of three predecessors, and six forks. Entering by an up edge(U) consumes
the vertex's sole downward arrow, leaving no predecessor slot, three
successors and six forks. Entering by a fork(F) leaves three successors,
at most one of three predecessors and five forks. A down choice has three
possible displacement labels and either arrow label, hence weight3*(xP+xA)*D;
optional forks have weight y*F. Impose at most one P on the REMAINING
successor slots by U_n, but deliberately do not debit an incoming P child
at a D entry. Any restricted lattice tree has at most one processed child
TOTAL, so its remaining successors satisfy this weaker rule. Every lifted
image therefore belongs to this relaxed family, proving the upper bound.
The relaxed family is strictly larger: if a D entry arrived from a processed
successor, the two remaining successor slots must have zero additional P
in a truly restricted tree (4 assignments at unit weights), while U_2 permits
8. This is overcount, not a defect in an upper bound. Node-kind consistency
is also relaxed; the historical kind-typed code shares the occupancy omission.

The resulting nonnegative polynomials are
`D=U_2*(1+3*(xP+xA)*D)*(1+y*F)^6`,
`U=U_3*(1+y*F)^6`,
`F=U_3*(1+3*(xP+xA)*D)*(1+y*F)^5`,
`R=U_3*(1+3*(xP+xA)*D)*(1+y*F)^6`.
Starting with(1,1,1), height truncations enumerate relaxed word trees of
bounded height. Coefficients and weights are nonnegative; monotonicity and
induction show that any triple at least1 dominating its right sides bounds
every truncation, hence the sum of all finite lifted trees. This bounds the
restricted lattice-tree weight sum by the injection. Replacing U_n by
`(1+(xP+xA)*U)^n` drops even the remaining-slot constraint and gives the
full relaxed slot count of the linked two-level theorem. It is termwise
larger, as the elementary slot expansion shows.

**Weights and exact certificates.** For supplied p,q,r>0 set
`d1=1-p^3/(p^3+q^3+4*r^3)`,
`d2=1-p^2*q/(p*q*(p+q)+4*r^3)`,
`d3=1-p^2*r/(r*(p^2+q^2)+r^2*(p+q)+2*r^3)`;
`epsilon1=d1`, `epsilon2=max(d2,d3)`, `xP=t`, `xA=epsilon2/t^c`,
`y=epsilon1/t^3`. The six signed-axis product weights in the linked
product-law parent give these rational formulas by summing six products;
for the present polynomial theorem they are explicit supplied definitions.
Each key below is(c,p,q,r), each value(t,Dbar,Ubar,Fbar):

```python
{
        (2, 2921, 1, 2): (Fraction(121, 1000), Fraction(38819515651721, 125000000000), Fraction(2614495936247, 1000000000000), Fraction(411275330287659, 1000000000000)),
        (2, 1464, 1, 1): (Fraction(121, 1000), Fraction(116365070741407, 500000000000), Fraction(652123939263, 250000000000), Fraction(3080327991177, 10000000000)),
        (2, 5841, 2, 4): (Fraction(61, 500), Fraction(151842195690607, 500000000000), Fraction(1303405077461, 500000000000), Fraction(12551068393373, 31250000000)),
        (2, 4380, 1, 3): (Fraction(121, 1000), Fraction(321841798858453, 1000000000000), Fraction(653785718103, 250000000000), Fraction(21312272709127, 50000000000)),
        (1, 405, 1, 2): (Fraction(91, 1000), Fraction(11697402025031, 1000000000000), Fraction(155146937439, 62500000000), Fraction(46962997959, 3125000000)),
        (1, 208, 1, 1): (Fraction(89, 1000), Fraction(10283263176051, 1000000000000), Fraction(152629090359, 62500000000), Fraction(2627739909739, 200000000000)),
        (1, 810, 2, 4): (Fraction(91, 1000), Fraction(11697402025031, 1000000000000), Fraction(155146937439, 62500000000), Fraction(46962997959, 3125000000)),
        (1, 605, 1, 3): (Fraction(93, 1000), Fraction(3032442310293, 250000000000), Fraction(2482877419491, 1000000000000), Fraction(7794092314937, 500000000000)),
    }
```

Fraction(n,d) means n/d. Substitute each row into the displayed polynomials
and clear positive denominators. All entries are at least1, each dominates
its right side, and epsilon1*Rbar<1/100000. This proves eight POINT
certificates for the relaxed upper sum. D2 retains exact arithmetic.
The additional full-factor tuple at(4165,1,2), c=2 is
t=99/1000, Dbar=56694252249173/500000000000,
Ubar=3279872914431/1000000000000,
Fbar=168429466648591/1000000000000; direct substitution dominates both
polynomial systems (D3). No interval or improved formation law is inferred.

**Missing application premise.** To turn this count into a probability
bound one still needs a restricted admissible tree within the chosen budget
at every dissent realization, the supplied stochastic domination and
independent seed/amplification events. If these are supplied, F=|S|-1 and
E<=3F+cA imply, for0<t<=1,
`epsilon1^|S|*epsilon2^A <= epsilon1*t^E*(epsilon2/t^c)^A*(epsilon1/t^3)^F`.
The injection bounds the right-hand tree sum. Restricted admissibility is
not proved by eight numerical points or a finite tiny-fixture sample.
Thus no improved ordered region is claimed here. ∎

## Theorem T4 — exact finite restriction comparisons

The fixed primary sample has60 tiny realizations and costs c=1,2. All120
computed restricted and unrestricted minima agree, with zero differences;
a tree satisfying the budget exists in all120 cases. The restriction is
at most one processed child at EVERY parent, including seeds/amplified
parents. This is a finite sample, not a universal admissibility theorem.

**Finite verification.** Enumerate node subsets containing the root, one
live predecessor choice for each non-seed, and the resulting arrow forest.
For the restricted family count processed children at every parent and
reject a choice with two. Forks can join the arrow components into a tree
exactly when the component adjacency graph is connected; choose any spanning
tree of that graph. Each choice has F=S-1 and cost E-3(S-1)-cA. Minimize
these exact rational costs. The queried root is a maximal-level live site,
so the rooted level cap removes no candidate in this comparison. This is
precisely the finite enumeration in E1, with original fixtures unchanged.
The historical125-case floating MILP and W3 observation use a weaker
restriction and are not promoted as exact certificates; their full scope,
errors and original sources remain readable in recovery. ∎

## No-Go Discipline Gate — deferred applicability

N1: finite extension/seed constructions, induction case coverage and explicit
slot enumeration are actual controls of positive statements; the original
six concerns are not five normalized attacks on one negative target. No
quota PASS is asserted. N2: no repository wall is imported. N3: finite cap,
model assumptions, incoming occupancy and all-parent distinction are explicit.
N4: current mathematical source roles are above; historical floating MILP and
unresolved imports are recovery, not theorem authority. N5: finite rooted
instances, rational points and exact small enumeration are executed only by
future bounded capture; no spectral modes or infinite lattice are executed.
N6: preserve the branch and all deferred original science. N7: a cost-increasing
exchange retaining the budget, or direct construction, remains possible;
solver optimum differences do not exclude these. N8: finite absence and
historical search maxima are not a universal characterization or threshold.

## Boundaries and non-claims

This note proves finite rooted extension and seed lemmas, a sufficient induction conditional on an open tight-sibling statement, and a relaxed lifted-tree upper sum with eight rational point certificates.

The unrooted unit-budget converse and the local saturated-support characterization are not established; restricted admissibility and improved formation regions remain open.

Finite samples and historical floating solver observations do not complete formal negative certification; all original arguments and failures remain recoverable.

## Imports

Finite graph trees, level induction, finite rational minimization and
nonnegative monotone polynomial iteration are the mathematical tools.
Complete proofs appear above. The linked conditional process theorem is
used only for its explicit comparison/application framework. Its hypotheses
are not consequences of registered primitives, and this note supplies no
new probability or physical identification premise. Historical negative
arguments remain readable with formal certification deferred.

## Verification

The stdout-only primary retains18 completed checks: A4+B3+C2+D3+E1+F4+G1.
C1 now binds both exact sorted predecessor profiles and E1 binds120 equal
minima/zero differences; the unchanged140-realization B sample remains.
The new `predecessor_profile_wrong` target tests the corrected ZB profile.
No mathematical outcome is asserted from the packaging checks alone.

```bash
python3 scripts/rooted_marked_tree_extension_seed_induction_relaxed_lifted_certificates_check_2026_09_17.py
python3 scripts/rooted_marked_tree_extension_seed_induction_relaxed_lifted_certificates_check_2026_09_17.py --list-mutations
```
