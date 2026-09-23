---
claim_id: the_soldering_menu_four_actions_of_the_proper_cubic_rotations_on_qubit_possibilities_and_what_each_lets_formation_build_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Admissibility names covariance under proper cubic rotations but not how they move possibilities. For the supplied complex-linear *-automorphism reading, an action on possibilities is a homomorphism from the proper cubic group O (= S4) into the qubit's automorphisms (SO(3) on the Bloch ball). Up to conjugacy there are exactly four: trivial (the unsoldered reading), a sign twist (A1+2A2), axis soldering (A2+E, through the axis permutation) and full soldering (T1), proved by the S4 character table with the determinant character sign^(#A2 + #E + #T2) and exhibited by explicit integer matrices. Their kernels have orders 24, 12, 4, 1 and orbit counts 1, 1, 3, 6 on the six bond directions; in a supplied conditionally independent broadcast model with invariant output labels, kernel-orbit equality gives relaxed bounds: ice count 5/16, 5/16, 1/2, 1; odd Gauss parity 1/2, 1/2, 1/2, 1; parity-role link profile at most 16/243, at most 16/243, relaxed feasibility, relaxed feasibility. These are necessary kernel constraints, not a construction of a covariant physical formation rule. No action is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/soldering_menu_four_cubic_actions_on_qubit_possibilities_and_formation_bounds_2026_09_22.py
---

# Four proper-cubic actions on qubit possibilities and conditional broadcast bounds

**Date:** 2026-09-22
**Type:** bounded_theorem
The question is which actions of the proper cubic group on a qubit's Bloch
ball are available, and what their kernels imply for a supplied independent
broadcast model. The formation interpretation remains conditional.

## Result up front

1. **There are four homomorphisms into SO(3), up to conjugacy.**
   Admissibility requires covariance "under lattice translations and
   proper cubic rotations", and the Qubit axiom distinguishes
   possibilities "by the supplied algebraic structure alone". Here we restrict to complex-linear unital *-automorphisms,
   which act as proper rotations of the Bloch ball. This additional reading
   is explicit; general algebra automorphisms are not being classified. How a
   lattice rotation moves a possibility is a homomorphism from the
   proper cubic group O (isomorphic to S4) into SO(3). Up to conjugacy
   there are exactly four:
   - trivial, the unsoldered reading;
   - a sign twist, diag(1, s, s), with s the sign of the axis permutation
     (A1 + 2A2);
   - axis soldering, s(g) |g|, which permutes the three axes (A2 + E);
   - full soldering, g itself (T1).

   Proof: a real three-dimensional representation of S4 splits into
   irreducibles, and its determinant is sign^(#A2 + #E + #T2). Of the
   eight splittings, exactly these four have determinant 1. T2, and
   A1 + E, fail on a quarter-turn.

2. **Each action leaves some bond directions indistinguishable.** A
   kernel element fixes every possibility but moves bond directions.
   The kernels have orders 24, 12, 4 and 1. Their orbits on the six
   directions number 1, 1, 3 and 6; under axis soldering the orbits are
   {+x, -x}, {+y, -y} and {+z, -z}. With invariant output labels, neighbours in one kernel orbit have
   equal one-site marginals conditional on the centre. Conditional independence
   is a separate supplied hypothesis, not a consequence of covariance.

3. **Bounds in the relaxed independent broadcast model per action** (trivial / sign twist / axis /
   full):
   - ice count (3 of 6 occupied): 5/16 / 5/16 / 1/2 / 1;
   - odd Gauss parity: 1/2 / 1/2 / 1/2 / 1;
   - parity-role link profile: at most 16/243 / at most 16/243 / relaxed feasibility
     / relaxed feasibility.

   Axis soldering ties the probabilities at +x and -x, not their realized
   occupations. Its odd-count probability is at most 1/2. With six independent
   parameters the relaxed model admits deterministic assignments. Full
   covariance, the centre stabilizer and a physical encoding can restrict this
   model further; kernel information alone proves no physical sufficiency.

4. **What the menu decides, in the broadcast order.**
   - Registering the parity-role skeleton by broadcast needs at least axis
     soldering.
   - Achieving the ice count with certainty in this product-law model needs
     full soldering.
   - Achieving odd parity with certainty in this product-law model also needs
     full soldering.
   - The sign twist behaves like the unsoldered reading for all three.

   These are necessary conditions in the supplied independent model, not
   sufficient conditions for a physical construction. They hold for the broadcast order, where the centre forms
   first and each neighbour sees only it. Other orders, in which a
   neighbour also sees other formed sites and relative geometry, are not
   classified here. In such orders an unsoldered rule might register a
   frame of its own.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "classify SO(3) actions and their necessary constraints on independent broadcast; a downstream physical consumer is not yet established"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "construct and check complete covariant formation rules, including output encodings and centre stabilizers, before claiming physical attainability"
conditional_surface_status: "complex-linear unital *-automorphism action; conditionally independent draws; invariant output labels; fixed broadcast order; no action adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the classification is exact character theory of a finite group with explicit matrices; the continuous upper bounds are proved below; grids supply finite controls only"
```

## Premises and declared objects

The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) motivate the question;
they do not supply the following broadcast law. Let O be the 24 signed
permutation matrices of determinant 1. Supply a homomorphism rho: O -> SO(3).
For a fixed centre record, the six surrounding binary occupation variables
are independent Bernoulli variables, with equal probabilities within each
kernel orbit. The output labels used below are invariant under the kernel.
These are explicit mathematical conditions, not derived formation dynamics.

Ice count means exactly three occupied neighbours; odd parity means an odd
number. For the role profile, a distinguished label V must occur exactly on
one opposite pair; additional prescribed letters distinguish the transverse
pairs. This note bounds the union over the three choices of the V pair.
Requiring specified transverse letters can only decrease that probability.
For relaxed deterministic feasibility each direction may be assigned a label
provided that label is constant on its kernel orbit.

Earlier possibility-covariance and formation notes motivated this calculation.
Their conclusions are not premises: the objects, classification and bounds
used here are stated and proved here. In particular, no unlanded PR supplies
an assumed theorem.

## Theorem 1 — Four actions

For completeness, the real irreducibles are the trivial and sign characters
(A1 and A2), the standard two-dimensional representation of the quotient
S4/V4 = S3 (E), the standard sum-zero subspace of the four-letter permutation
representation (T2), and its sign twist (T1). Their squared dimensions sum
to 24, and their character inner products give orthonormality. Thus the list
is complete. Their determinant characters are respectively 1, sign, sign,
sign and 1: for the standard permutation representation remove its invariant
line; for the sign twist in dimension three multiply the determinant by sign.
Every representation of a finite group admits an invariant positive inner
product. Orthogonal equivalence in odd dimension also gives SO(3) conjugacy,
since replacing a determinant-minus-one intertwiner Q by -Q changes its
orientation without changing conjugation. These facts justify completeness
up to the claimed conjugacy, not just the displayed examples.

The four listed maps are homomorphisms into SO(3), checked on all 576
pairs, and their characters on the five classes (sizes 1, 6, 3, 8, 6) are
(3,3,3,3,3), (3,-1,3,3,-1), (3,-1,3,0,-1), (3,1,-1,0,-1). The five
irreducible characters of S4 are orthonormal. Among the eight splittings
of dimension three, the determinant rule leaves exactly 3A1, A1+2A2,
A2+E and T1. The constructed characters decompose into exactly those, so
the four actions are pairwise inequivalent and form the complete menu. T2 has
determinant -1 on a quarter-turn.

## Theorem 2 — Kernel orbits and broadcast bounds

If g lies in the kernel of rho, covariance fixes the centre record and
invariant output labels while moving d to gd. The marginals at d and gd
therefore agree. Only the separately supplied independence hypothesis lets
us multiply probabilities. Kernels constrain a conditional law necessarily;
the full centre stabilizer may impose more constraints.

For one orbit of six with occupation probability p, the ice probability is
20 p^3(1-p)^3 <= 20/64 = 5/16, attained at p=1/2. For three pairs with
probabilities p_1,p_2,p_3, the probability generating function evaluated at
-1 is product_i (1-2p_i)^2 >= 0. Thus P(odd) <= 1/2 and P(total=3) <= 1/2.
The assignment (p_1,p_2,p_3)=(1,1/2,0) attains the latter bound. For one
six-site orbit, P(odd)=[1-(1-2p)^6]/2 <= 1/2. Six singleton orbits permit a
relaxed deterministic assignment with exactly three occupations or exactly
one occupation, respectively. These inequalities hold for every real
probability in [0,1], not only the runner's rational grid.

For one orbit, write q=P(V). The disjoint events with V exactly on an opposite
pair have total probability 3q^2(1-q)^4. Its derivative is
6q(1-q)^3(1-3q), so its maximum is 16/243 at q=1/3 (both endpoints give zero).
The full role-profile event is a subset. A fixed choice of V pair has the
smaller upper bound 16/729. The kernel partition permits deterministic role
labels exactly when every orbit needs one label; this is true for the axis
and full actions and false for the other two. This is relaxed label feasibility,
not a construction of a physical qubit encoding or a covariant formation law.

## No-Go Discipline Gate

The negative conclusion is restricted to the supplied independent broadcast
model. It is not an impossibility result for record formation in general.

- **N1 alternative routes (ATTEMPTED).** Five distinct challenges were checked:
  (1) continuous probability optimization between grid points, closed by the
  inequalities and derivative in Theorem 2; (2) mixing over centre records,
  closed by averaging the pointwise bound; (3) directional discrimination
  inside a kernel orbit, excluded by the covariance equality in Theorem 2;
  (4) richer transverse output alphabets, bounded by the containing V-pair
  event; (5) correlations between neighbours, a real escape outside the
  independence hypothesis: choose a uniformly random three-element subset
  of the six sites, giving equal marginals and ice probability one.
  The fifth challenge narrows the theorem; it rules out a general covariance
  no-go. These arguments, not prior audit labels, are the local evidence.
- **N2 wall independence.** No count of independent physical walls is claimed.
  The action, invariant labels, product law and order jointly define the
  supplied domain. Pairwise independence of these conditions is not used.
- **N3 hidden walls.** Independence and label invariance are now explicit.
  A kernel is smaller than a possible centre stabilizer; relaxed feasibility
  is not promoted to full covariant attainability. No implicit physical bridge
  is used. Character theory is mathematical machinery.
- **N4 residual matching.** No external negative witness is used. The relevant
  residual is attainment in the specified product-law class; the source is
  Theorem 2 immediately above, with the same domain and quantifiers.
- **N5 rhetoric audit.** Group elements and six-direction stars are checked.
  Spatial fields, modes, multiple-star compatibility and infinite lattices
  are not computed or excluded. The runner states these execution limits.
- **N6 partial-closure paths.** Joint draws, checker-last orders, additional
  recorded neighbours and different label actions remain possible escapes.
  No new axiom is asserted necessary. Registered scale, kinetic-form and
  realized-state primitives are not ingredients of this finite probability
  calculation and are not classified as walls.
- **N7 steelman.** Equal marginals do not imply independent draws: a correlated
  uniform three-subset has the desired ice count with certainty and all the
  permutation symmetry. It defeats the original inference from covariance
  alone. The corrected theorem expressly assumes a product law, and does not
  decide whether record formation supplies that hypothesis or a correlated law.
- **N8 cross-cycle echo.** The earlier two-reading possibility-covariance
  question supplies motivation, not a no-go witness. Open formation packets
  consider joint units and alternate orders; these routes remain outside the
  present domain, not foreclosed by this classification. No retired physical
  wall is being reinstated here.

## Falsifiers

- A homomorphism O -> SO(3) not conjugate to one of the four, a failed
  homomorphism or orthogonality check, or a character decomposition other
  than stated falsifies Theorem 1.
- A broadcast rule beating a stated bound under the stated action, or a
  kernel of different order, falsifies Theorem 2.

## Boundaries and non-claims

No action is adopted. The classification concerns actions of the proper
cubic rotations on possibilities through the qubit's automorphisms;
antiunitary maps are not complex-linear *-automorphisms and are excluded. The bounds
concern the broadcast order only. No physical identification is made.
Nothing here grades, unlocks or audits any other claim.

## Imports

The mathematical input is real representation theory of the finite group S4.
The *-automorphism reading, invariant labels, independent conditional draws
and broadcast order define a supplied mathematical model. None is derived
from the framework axioms here. No empirical comparator or fitted input is used.

## Review record

The original proposal's physical sufficiency statements were narrowed to
necessary kernel constraints and relaxed label feasibility. Conditional
independence and invariant labels are explicit. Global bounds now have
continuous proofs rather than finite-grid assertions. The runner retains the
finite group and grid controls, adds a correlated escape control, and records
its actual resolution limits. Standard character theory is the mathematical
input; no observations, fitted constants, physical dynamics or action choice
are imported. Source review and fixes were performed serially in one Codex
session under the owner's no-subagent direction; no separate fix reviewer or
independent audit is claimed.

## Verification

```bash
python3 scripts/soldering_menu_four_cubic_actions_on_qubit_possibilities_and_formation_bounds_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=11 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/soldering_menu_four_cubic_actions_on_qubit_possibilities_and_formation_bounds_2026_09_22.txt`.
