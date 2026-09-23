---
claim_id: admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For strictly positive binary full-conditionals on a finite nonempty set of sites, a positive joint law exists exactly when the conditional-odds one-form has zero multiplicative curl on every two-site configuration square; the joint law is then unique and recovered by path integration. For a translation- and proper-cubic-covariant rule whose probability depends only on the occupied-neighbor count, compatibility in every finite cubic edge environment is equivalent to geometric odds, hence an affine logit and a finite-volume nearest-neighbor Ising-type action."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py
---

# Finite Binary Full-Conditional Compatibility And Cubic Count-Action Classification

**Date:** 2026-08-10
**Type:** bounded_theorem
**Status:** proposed_retained
**Scope:** finite nonempty-site strictly positive binary full-conditionals, with
a count-only cubic specialization.
**Audit-status authority:** independent audit lane.
**Primary runner:**
[admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py](../scripts/admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py)

## Result Up Front

Let `V` be a finite nonempty set of binary sites. For each site `i`, suppose a
strictly positive one-site full conditional is supplied for every configuration
of the other sites. Write `r_i(x)` for the conditional odds of changing site
`i` from zero to one while the other bits equal `x`. These conditionals arise
from one positive joint probability law exactly when every two-site
configuration square satisfies

    r_i(x) r_j(x^i) = r_j(x) r_i(x^j).

When the square equations hold, multiplying odds along a path from the
all-zero configuration gives a path-independent positive weight. Normalizing
the weights gives the unique joint law with the supplied full conditionals.

For a count-only rule on the cubic lattice, write `q(k)` for the probability of
one given `k` occupied nearest neighbors and

    o_k = q(k)/(1-q(k)),       k = 0,...,6.

Compatibility in every finite cubic edge environment is equivalent to

    o_k = A B^k

for positive `A` and `B`. The corresponding finite-region probability law has
weight

    A^(sum_i x_i)
    B^(sum_(<ij> subset Lambda) x_i x_j + sum_i b_i x_i),

where `b_i` is the occupied exterior-neighbor count at site `i`. Thus the
finite action is the nearest-neighbor Ising-type action associated with the
affine conditional logit.

## Admissibility Context And Imports

The current [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies a
nearest-neighbor-dependent one-site distribution. The theorem below studies a
declared binary specialization of such local distributions. Its mathematical
premises are the finite nonempty binary domain, strict positivity, and the stated
full-conditional interpretation. The cubic classification adds the cubic
nearest-neighbor graph and count-only dependence. All arithmetic and all
finite constructions are derived in this note and its runner.

External scientific inputs: empty set. The derivation's observational-
comparator, fitted-value, literature-identity, and boundary-normalization input
inventories are empty. The parameters `A` and `B` remain symbolic; the rational
values used by the runner are exact test fixtures.

## Machine Status And Trace

~~~yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
claim_type_reason: "The finite nonempty-site positive binary square-curl equivalence, path reconstruction, uniqueness theorem, cubic count classification, proper-rotation certificate, and finite action formula are proved under explicit hypotheses."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Audit the finite theorem and then test any proposed physical binary law against the square equations."
conditional_surface_status: "exact finite nonempty-site binary theorem under strict positivity, with a count-only cubic specialization"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## 1. Typed Setup

Let `V` be a finite nonempty set of sites and let

    Omega = {0,1}^V.

The two symbols can be embedded in the one-site matrix domain as
`B_0=-I_2` and `B_1=+I_2`. This embedding fixes the binary alphabet used by the
theorem.

For each site `i` and each configuration `x` with `x_i=0`, define

    q_i(x) = P(X_i=1 | X_(V\{i})=x_(V\{i})),
    0 < q_i(x) < 1,
    r_i(x) = q_i(x)/(1-q_i(x)).

A compatible positive joint law is a function
`pi: Omega -> (0,1)` summing to one whose full one-site conditionals equal the
declared `q_i`.

## 2. Finite Binary Square-Curl Theorem

### Theorem 1

The strictly positive full-conditionals `(q_i)` admit a compatible positive
joint law if and only if, for every pair `i != j` and every configuration `x`
with `x_i=x_j=0`,

    r_i(x) r_j(x^i) = r_j(x) r_i(x^j).          (SC)

Here `x^i` is `x` with bit `i` changed from zero to one. When (SC) holds, the
joint law is unique.

### Necessity

If `pi` exists, then

    r_i(x) = pi(x^i)/pi(x).

Following the square first through `i` and then `j` gives

    pi(x^(ij))/pi(x) = r_i(x) r_j(x^i).

Following it first through `j` and then `i` gives

    pi(x^(ij))/pi(x) = r_j(x) r_i(x^j).

Equality of these expressions proves (SC).

### Sufficiency

Fix the all-zero configuration `0`. For any target `x`, choose an order of the
sites where `x_i=1` and multiply the appropriate odds along that monotone path.
Call the product `w(x)`.

Any two orders of the same finite set differ by adjacent transpositions.
Swapping two adjacent flips changes one path segment from

    r_i(y) r_j(y^i)

to

    r_j(y) r_i(y^j).

Equation (SC) equates those products, so `w(x)` is path-independent. Set

    pi(x) = w(x) / sum_(z in Omega) w(z).

Every weight is positive. For any `x_i=0`, compare a path to `x` followed by
the flip at `i` with a path to `x^i`. Path independence gives

    pi(x^i)/pi(x) = w(x^i)/w(x) = r_i(x).

Converting odds back to probabilities recovers `q_i(x)` and proves existence.

### Uniqueness

Every compatible positive law has the same ratio
`pi(x^i)/pi(x)=r_i(x)` on every hypercube edge. The connected configuration
hypercube determines every weight relative to `pi(0)`, and normalization fixes
`pi(0)`.

## 3. Nearest-Neighbor Reduction

Suppose `q_i` depends only on the graph neighbors of site `i`. For nonadjacent
sites `i` and `j`, changing `j` leaves `r_i` fixed and changing `i` leaves
`r_j` fixed. Their square equation therefore holds identically. It is enough
to check adjacent pairs.

## 4. Cubic Count Classification

On the cubic lattice, let the local law depend only on

    k = sum_(y~x) 1{B_1 at y}

and write `q(k)` and `o_k=q(k)/(1-q(k))`.

Take adjacent sites `i,j`. Excluding their shared edge, the five remaining
neighbors of `i` and the five remaining neighbors of `j` are disjoint in
`Z^3`. Their occupied counts `a,b` can be assigned independently from zero
through five. The square condition is

    o_a o_(b+1) = o_b o_(a+1).

Division by the positive product `o_a o_b` gives

    o_(a+1)/o_a = o_(b+1)/o_b.

Because `a,b` range independently, all six successive ratios equal one
positive constant `B`. With `A=o_0`,

    o_k = A B^k,
    q(k) = A B^k/(1+A B^k).

Conversely, geometric odds make both square products
`A^2 B^(a+b+1)`, so every square closes.

### Theorem 2

A strictly positive count-only cubic binary rule is compatible in every finite
edge environment exactly when its conditional logit is affine in the occupied
neighbor count. The exact linear system on the seven formal log-odds values
has rank five and nullity two; the constant vector and the neighbor-count
vector span its solution space.

## 5. Derived Finite-Volume Action

Let `Lambda` be finite, fix an exterior binary configuration, and let `b_i`
count occupied exterior neighbors at site `i`. Define

    pi_Lambda(x|b) = Z_Lambda(b)^(-1)
      A^(sum_i x_i)
      B^(sum_(<ij> subset Lambda) x_i x_j + sum_i b_i x_i).

Changing site `i` from zero to one multiplies the weight by

    A B^(b_i + sum_(j~i, j in Lambda) x_j) = A B^k.

The full conditional is exactly `q(k)`. In logarithmic notation, the action,
up to its normalization constant, is

    S_Lambda(x|b)
      = -(log A) sum_i x_i
        -(log B)[sum_(<ij>) x_i x_j + sum_i b_i x_i].

### Optional Code-Swap Symmetry

If a supplied symmetry exchanges `B_0` and `B_1`, then

    q(6-k) = 1-q(k),
    o_(6-k) = 1/o_k.

Substitution of `o_k=A B^k` gives the single relation

    A B^3 = 1.

The runner uses the exact compatible fixture

    A = 1/8,
    B = 2,
    q = (1/9, 1/5, 1/3, 1/2, 2/3, 4/5, 8/9).

## 6. Scope Boundary

The certified object is the finite nonempty-site probability theorem in
Sections 1-5. Its declared domain consists of a configuration space on a finite
nonempty set of binary sites and strictly positive full conditionals. The cubic
specialization additionally uses the standard cubic nearest-neighbor graph and
count-only dependence. Infinite
volume, stochastic update dynamics, physical code selection, Record formation,
realized-history selection, and gravitational interpretation are separate
source candidates.

## 7. Verification

Run:

    python3 scripts/admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py

The runner checks:

- current source binding and the relevant Admissibility sentence;
- exact square closure and path reconstruction from an independent rational
  four-site joint weight;
- normalized uniqueness and recovery of every full conditional;
- a one-entry odds mutation and the resulting nonzero square residual;
- rank five and nullity two for the cubic count constraints;
- the geometric-odds fixture and optional code-swap relation;
- determinant, identity, closure, and neighbor action for all 24 proper cubic
  rotations, including a determinant-sign mutation control; and
- exact finite-action conditional recovery for all 36 pairs of exterior
  endpoint counts.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Review Record

This salvage retains the independently verified static theorem, cubic
classification, proper-rotation certificate, and finite action. The earlier
cross-region projectivity proposal, stochastic update interpretation, hostile
route-closure claim, and campaign-local process fields are excluded from this
source candidate. Independent audit remains the ratification step.

## Theorem Verdict

For strictly positive binary full-conditionals on a finite nonempty site set,

    compatible positive joint law
      iff zero square curl
      iff path-independent positive weights.

For the count-only cubic specialization,

    compatibility in every finite edge environment
      iff geometric conditional odds
      iff affine conditional logit
      iff the displayed nearest-neighbor Ising-type finite action.
