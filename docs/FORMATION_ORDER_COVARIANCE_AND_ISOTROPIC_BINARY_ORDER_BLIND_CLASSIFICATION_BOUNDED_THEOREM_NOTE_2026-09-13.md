---
claim_id: formation_order_covariance_and_isotropic_binary_order_blind_classification_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "On Z^3 with nearest-neighbor adjacency and the 24 proper cubic rotations about a site, no total order is invariant under a non-identity proper cubic rotation: if x < Rx then x < Rx < ... < x. For a sequential single-site formation process whose local kernel is a nearest-neighbor rule, the formation law of an order sigma is the product of the rule along recorded-neighbour sets; an adjacent transposition of sigma changes the joint if and only if the two consecutive sites are lattice neighbours and the adjacent-pair exchange identity fails on that background. On the isotropic binary alphabet, the only interior rules (every one-neighbour conditional in (0,1)) whose formation law is independent of order on every finite window are the independent (constant) rules, which do not vary with neighbour values; the identity forcing this is that the path3 matching residual equals (pminus-pplus)^2. A declared Ising-type kernel with e^J=2 is a positive pair-of-orders witness: path3 chain versus ends-first differs on all 8 configurations with total variation 9/50 and all-minus masses 8/25 versus 4/17; the 24 plaquette orders collapse to 4 laws and cyclic versus opposite-corners has total variation 9/50; the 720 orders on the 2x3 window give twenty-eight laws, and corners-first versus row-major differs on 44 of 64 configurations with total variation 135/578. Exact rationals throughout. The physical formation order is not selected; the physical rule is not selected; no axiom, primitive, order law, or clock is adopted."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
runner: scripts/formation_order_covariance_and_isotropic_binary_order_blind_classification_2026_09_13.py
---

# Sequential formation has no proper-cubic-invariant total order, and isotropic binary order-blind rules are independent

**Date:** 2026-09-13
**Type:** bounded_theorem
**Scope:** total orders on `Z^3`, sequential single-site formation products of a nearest-neighbor kernel, and the isotropic binary alphabet on the three-site path, the four-site plaquette, and the `2x3` window.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/formation_order_covariance_and_isotropic_binary_order_blind_classification_2026_09_13.py`](../scripts/formation_order_covariance_and_isotropic_binary_order_blind_classification_2026_09_13.py)
**Pinned cache:**
[`logs/runner-cache/formation_order_covariance_and_isotropic_binary_order_blind_classification_2026_09_13.txt`](../logs/runner-cache/formation_order_covariance_and_isotropic_binary_order_blind_classification_2026_09_13.txt)

## Result up front

The Lattice axiom gives `Z^3` with nearest-neighbor adjacency and proper cubic
rotations about each site. No total order on those sites can be invariant
under a non-identity proper cubic rotation: if `x < Rx` then iterating gives
`x < Rx < … < x`. So a sequential single-site formation process, whose
physical content includes an order, is never itself lattice-covariant.

Admissibility still supplies one covariant nearest-neighbor rule, and Record
says records form. The rule may be applied along any order. The joint law on
a finished finite window is then the product of the rule's conditionals along
the recorded-neighbour sets of that order. That product is independent of
order for every window if and only if adjacent lattice neighbours satisfy the
exchange identity

```text
r(a | S_x) r(b | S_y ∪ {x:a}) = r(b | S_y) r(a | S_x ∪ {y:b})
```

on every recorded background. On the isotropic binary alphabet the interior order-blind kernels are the
only independent rules: `r(+ | anything) = c` whenever every one-neighbour
conditional lies strictly between `0` and `1`. Those rules do not vary with
nearest-neighbour conditions. The identity that forces this is
elementary: matching the two formation orders on a three-site path makes the
residual between the plus-side and minus-side normalizations equal to
`(pminus - pplus)^2`.

A declared Ising-type kernel with `e^J = 2` varies with neighbour values
(`P(+ | empty) = 1/2`, `P(+ | one plus) = 4/5`, `P(+ | one minus) = 1/5`)
and is a positive pair-of-orders witness. On the path, the chain order and
the ends-first order differ on all eight configurations, total variation
`9/50`, all-minus masses `8/25` versus `4/17`. On the plaquette the
twenty-four orders collapse to four laws; cyclic versus opposite-corners
again has total variation `9/50`. On the `2x3` window the 720 orders give
twenty-eight distinct laws, and corners-first versus row-major differs on
44 of 64 configurations with total variation `135/578`. Opposite-corner
monotone classes coincide, which is the already-landed rectangle fact used
here only as a control, not as a premise.

The physical formation order is not selected. The note selects neither order
and selects neither rule. Order-dependent record statistics are registered
data under
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
until a clause supplies an order, a covariant law on orders, joint formation
on covariant sets, or a restriction to order-blind rules. Those clauses are
owner decisions and are not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Lemma C, the exchange characterization, the isotropic-binary interior classification, and the Ising pair-of-orders witness are proved exactly on the declared graphs. No physical order, rule, clock, rate, or axiom clause is selected."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the axioms do not force a unique sequential formation law; order-dependent record statistics remain registered data until a clause supplies an order, a covariant order-law, joint covariant formation, or order-blindness"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "possibility-covariance / Cl(3,0) soldering fork; use this block's order-blind class as the declared formation-side restriction when a later block needs one"
conditional_surface_status: "exact on Z^3 for Lemma C; exact for sequential products of a nearest-neighbor kernel; interior classification exact on the isotropic binary alphabet; witness exact on path3, the plaquette, and 2x3. No infinite-volume statement, no physical-law selection, no order-law, no clock."
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The scientific dependencies are the current four-axiom authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the registered realized-state primitive
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md).
The axiom sentences used, verbatim:

- Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
  nearest-neighbor adjacency, standard translations, and proper cubic
  rotations about each site."
- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and "For
  each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form." — "Only records are readable." — "A site with no
  record cannot be read."

Admissibility is not a dynamics axiom. The axiom document states that it
does not provide a record-production process. The realized-state primitive
supplies pointwise evaluation at a law-admissible realized state and "no
averaging over alternatives"; a value that would change under a different
law-admissible realized state is registered data, not derivation output. A
quantity that changes with the realized formation order is of that kind
unless the rule is order-blind.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the 24-element group of proper signed-permutation rotations of the three
  coordinate axes;
- finite windows of `Z^3` with nearest-neighbor edges and the records-only
  reading (an unrecorded neighbour contributes no factor);
- the isotropic binary alphabet `{0,1}` with a kernel that depends on a
  recorded-neighbour assignment only through the pair `(m, k)` = (number
  recorded, number equal to `1`);
- one declared varying kernel, the Ising-type rule with `e^J = 2`,

```text
P(+ | m, k) = 2^{2k} / (2^{2k} + 2^{2(m-k)}),
```

used as a witness choice, not as the physical Admissibility rule.

No Hamiltonian, action, carrier, clock, formation unit, rate, Born weight,
Gauss kernel, or readout instrument is imported. No order is supplied.

## Exact target and objects

**Target.** (i) Prove there is no proper-cubic-invariant total order on
`Z^3`. (ii) Characterize sequential formation products that are independent
of order. (iii) Classify the interior isotropic binary kernels that satisfy
that characterization. (iv) Exhibit an exact pair of orders whose formation
laws differ for a covariant varying kernel.

Let `Λ` be a finite set of sites with nearest-neighbor edges. A formation
order is a bijection `σ = (x_1, …, x_n)` onto `Λ`. For a nearest-neighbor
rule `r` and an assignment `v : Λ → {0,1}`, the formation law is

```text
μ_σ(v) = Π_k r(v_{x_k} | v restricted to A_k^σ),
A_k^σ = N(x_k) ∩ {x_1, …, x_{k-1}}.
```

The rule is isotropic binary when `r(+ | η) = f(m, k)` with `m = |η|` and
`k` the number of `+` values in `η`. It is interior when `0 < f(1, 0) < 1`
and `0 < f(1, 1) < 1`. It is independent when `f(m, k)` is constant in
`(m, k)`.

## Prior art and what is new

The landed notes
[`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)
and
[`ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md`](ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md)
already separate the formation law of a product rule from its static law,
and prove that every monotone order on a rectangle gives one law. Those
notes work inside a declared six-projector menu and a declared product-rule
family. They are related context. They are not premises of the proofs
below, and they do not contain Lemma C, the exchange characterization, or
the interior isotropic-binary classification.

The Q8 pair
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md)
is the model-pair precedent: two covariant local laws, neither selected.
The present witness is a pair of orders for one covariant local law.

## Proof-obligation graph

| obligation | exact disposition |
|---|---|
| the proper cubic group has 24 elements | signed permutations of determinant `+1` |
| every non-identity rotation moves a lattice point | checked on the 23 non-identity elements against the seeds `(1,0,0)`, `(0,1,0)`, `(0,0,1)`, `(1,1,0)`, `(1,1,1)` |
| an invariant total order is then impossible | if `x < Rx` then `x < Rx < … < R^{m-1}x < x` |
| adjacent transposition of a formation order changes the product only for a lattice-adjacent pair | non-neighbours do not enter each other's recorded sets; later sites see the same recorded set |
| exchange identity characterizes order-blindness | the symmetric group is generated by adjacent transpositions |
| interior isotropic binary order-blind kernels are independent | path3 matching residual equals `(pminus-pplus)^2` |
| constant kernels are order-blind | the sequential product is `c^{#plus}(1-c)^{#minus}` |
| a varying covariant kernel can fail order-blindness | declared Ising kernel, exact joints on path3, plaquette, `2x3` |
| identify the physical order or rule | open and not claimed |

Every leaf needed for the stated finite target is discharged. The last row
is a downstream physics question, not a terminal lemma of this target.

## Theorem 1 — no proper-cubic-invariant total order

The proper cubic rotations about the origin are the 24 signed permutation
matrices of determinant `+1`. The identity is one of them. For every other
element `R` there is a lattice point `x` with `Rx ≠ x`: each of the 23
non-identity rotations moves at least one of `(1,0,0)`, `(0,1,0)`,
`(0,0,1)`, `(1,1,0)`, `(1,1,1)`, and the orbit of that point under `R` has
length at least 2.

Suppose a total order `<` on `Z^3` satisfied `x < y` if and only if
`Rx < Ry`. Take `x` with `Rx ≠ x`. Then either `x < Rx` or `Rx < x`. In
the first case, applying `R` repeatedly yields `x < Rx < R^2 x < … <
R^{m-1}x < R^m x = x`. A strict total order cannot satisfy `x < x`. The
second case is the same with `R^{-1}`. Hence there is no proper-cubic-invariant
total order on `Z^3`.

Translations do not help: a translation-invariant total order is already
impossible because translations act freely. The Lattice axiom's "no site is
privileged" sentence is the same obstruction in the translation direction.

This is a statement about orders. It does not forbid applying a covariant
local rule along a non-invariant order. It says that if the induced record
law is to inherit lattice covariance from the rule, something else must
make the order physically idle or replace it by a covariant construction.

## Theorem 2 — exchange characterization of order-blind sequential products

Fix a finite window and a nearest-neighbor rule. Let `σ` be a formation
order and let `τ` be the adjacent transposition of positions `k` and
`k+1`. Write `x = σ(k)` and `y = σ(k+1)`, and write `S` for the set of
sites formed before both.

If `x` and `y` are not lattice neighbours, then neither recorded-neighbour
set includes the other, and the two factors of the product merely swap.
Every later site sees the same recorded set. So `μ_σ = μ_τ`.

If `x` and `y` are lattice neighbours, the two factors become
`r(v_x | S ∩ N(x)) r(v_y | (S ∩ N(y)) ∪ {x})` before the swap and
`r(v_y | S ∩ N(y)) r(v_x | (S ∩ N(x)) ∪ {y})` after it. Equality for all
values is the exchange identity on that background.

Adjacent transpositions generate the symmetric group, so `μ_σ` is
independent of `σ` if and only if the exchange identity holds for every
lattice-adjacent pair and every background that a prefix can realize. On
`Z^3` every assignment of the other neighbour slots of an adjacent pair is
realizable on a large enough window. The identity is therefore the
characterization of order-blindness for sequential single-site formation.

The runner executes the two sides of the dichotomy on the three-site path:
swapping a consecutive non-neighbour pair leaves the Ising joint unchanged;
the chain order and the ends-first order, which differ by bringing a
neighbour pair together against a nonempty background, do not.

## Theorem 3 — interior isotropic binary order-blind rules are independent

On a three-site path `L—M—R`, two orders are the chain `L, M, R` and
ends-first `L, R, M`. Write `pplus = f(1,1)`, `pminus = f(1,0)`, and
`p0 = f(0,0)`, all in `(0,1)`. Matching the two joints on the four
configurations with `L = R = +` and `L = R = -` forces

```text
p0 = pplus^2 + (1 - pplus) pminus
```

from the plus-plus side and a parallel identity from the minus-minus side.
The difference of those two normalizations is the polynomial identity

```text
(1 - pminus)^2 + pminus (1 - pplus) - (1 - p0) = (pminus - pplus)^2,
```

checked exactly on the five sample pairs `(1/2, 1/2)`, `(4/5, 1/5)`,
`(2/3, 1/4)`, `(1/7, 5/8)`, `(3/10, 3/10)` and on the declared Ising
kernel. The residual vanishes if and only if `pplus = pminus`. Then
`p0 = pplus`, and the two-neighbour kernel required by matching is the
same constant. The perpendicular L-window is the same path graph and
carries the same identity, so a cubic-covariant binary rule that
distinguishes opposite pairs from perpendicular pairs is still forced to
be constant on each one-neighbour slot and each two-neighbour orbit.

The independent kernel `f(m, k) = c` satisfies exchange on every
background: the sequential product is `c^{n_+} (1-c)^{n_-}` and does not
see the order. The runner checks this through five recorded neighbours, on
every path3 order, every plaquette order, and every `2x3` order.

An independent kernel does not vary with nearest-neighbour conditions. In
the interior isotropic binary class, Admissibility's variation sentence and
order-blind sequential formation therefore do not hold together.

## Theorem 4 — a covariant varying kernel is a pair-of-orders witness

The declared Ising kernel with `e^J = 2` is a function of `(m, k)` only, so
it is covariant under translations and proper cubic rotations. It varies:
`f(0,0) = 1/2`, `f(1,1) = 4/5`, `f(1,0) = 1/5`. It fails twenty-four
exchange identities already at recorded-neighbour cardinalities `0` and
`1`. Executed joints:

- Path3: six orders, two laws. Chain versus ends-first differs on all 8
  configurations, total variation `9/50`, all-minus masses `8/25` versus
  `4/17`. Forest orders (`|A_k| ≤ 1` for every site) coincide with one
  another; the two orders that form the middle last coincide with one
  another.
- Plaquette: twenty-four orders, four laws of sizes `4, 4, 8, 8`. Cyclic
  order `(0,1,2,3)` versus opposite-corners `(0,2,1,3)` differs on all 16
  configurations, total variation `9/50`. Rotating the cyclic order by one
  site produces a different law, and that law is exactly the pushforward of
  the original law under the corresponding vertex rotation of the square.
  The induced record statistics of a fixed sequential order are therefore
  not rotation-invariant, even though the local rule is.
- `2x3` rectangle: 720 orders, twenty-eight distinct laws. Row-major and
  its reverse coincide (opposite-corner monotone classes). Corners-first
  versus row-major differs on 44 of 64 configurations, total variation
  `135/578`.

This is a positive pair-of-orders witness. It selects neither order as the
framework's physical formation process, and it selects neither rule as the
framework's physical Admissibility law.

## Boundary and falsifiers

The result is falsified if any of the following finite statements fails:

- a non-identity proper cubic rotation fixes every tested lattice seed;
- the path3 residual is not `(pminus - pplus)^2` on the sampled pairs;
- the constant kernel fails exchange or gives two distinct path3 laws;
- the declared Ising kernel's chain and ends-first joints agree;
- the quoted masses `8/25`, `4/17`, total variations `9/50` and
  `135/578`, or the `2x3` census of twenty-eight laws fail to reproduce.

The theorem does not say sequential formation is forbidden. It does not
say the Admissibility rule must be independent. It does not supply an
order, a measure over orders, a clock, a rate, a formation unit, or a
joint-formation construction. It does not treat the uniform mixture over
orders as a law: the realized-state primitive supplies no such mixture.
It does not classify kernels that take the values `0` or `1` at a
one-neighbour slot (deterministic copying, majority, and related boundary
rules), and it does not classify alphabets larger than binary.

## Separating clauses, not adopted

The axioms as written do not force the record statistics of a varying
isotropic binary rule to be independent of formation order. The smallest
sentences that would separate the two path3 worlds, phrased in the axiom
document's register and recorded as owner decisions, are:

1. the nearest-neighbour rule is order-blind (in this class, that forces
   the independent kernel, which then fails the variation sentence);
2. records on a covariant set form jointly, not along a total order;
3. the formation order is itself drawn from a covariant law on orders;
4. the induced record law is not required to be lattice-covariant, and
   order-dependent statistics are registered data.

None of these is adopted here.

## Honest-auditor read

Lemma C is a one-line group fact about `Z^3`. The exchange characterization
is the standard adjacent-transposition generation of `S_n` applied to
recorded-neighbour products. The classification is a two-parameter
polynomial identity on a three-site path; it is not a scan of all binary
rules, and it does not touch deterministic kernels. The witness is one
declared covariant kernel on three small graphs. The downstream physical
question — which of the four clauses, if any, is the theory — is not
answered. What the block does settle is that "apply the covariant rule
along some sequential order and read the finished window" is not a
derivation of a unique record law from the axiom text.

## Verification

```bash
python3 scripts/formation_order_covariance_and_isotropic_binary_order_blind_classification_2026_09_13.py
```
