---
claim_id: order_blind_positive_formation_is_a_one_dependent_gibbs_field_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
claim_scope: "Formation reading of Admissibility, any finite alphabet, any translation-covariant strictly positive nearest-neighbour rule that is order-blind (equivalently, by the 2026-09-22 Theorem 2, of product form r0 prod phi_d with bond symmetry and normalisation on every neighbour condition). (T1) The finished law on any finite set of sites, for any formation order, is the induced-subgraph product form, and these laws are consistent under marginalisation; hence they extend uniquely to one translation-covariant record field on Z^3. (T2) In that field the conditional law of a site given every other record is the rule's distribution given its six neighbours: the formation and static readings coincide exactly. (T3) The field is 1-dependent: records on two sets with no lattice edge between them are independent. (T4) Consequently every truncated two-point function of local observables vanishes beyond adjacency and every structure factor is a trigonometric polynomial of degree one: no long-range order, no power-law correlations and no pinch points. Exhibit checks are exact on the soldered 48-point chiral-pair rule. No rule, reading, order or alphabet is adopted."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/order_blind_formation_one_dependent_record_field_2026_10_16.py
---

# Order-blind positive formation is a 1-dependent Gibbs field

**Date:** 2026-10-16
**Type:** bounded_theorem
**Status:** bounded-support; general proofs under stated hypotheses plus exact
exhibit checks; unaudited.

## Result up front

For a strictly positive order-blind nearest-neighbour rule (the class that
the 2026-09-22 note shows is nonconstant only under soldering, e.g. on the
24-point orbit, the 48-point chiral pair and the Haar sphere):

1. **One record field.** The finished laws of all finite windows and all
   formation orders are the induced-subgraph product
   `prod_x r0(a_x) prod_{edges xy} phi(a_x, a_y)`. They are consistent
   under deleting sites, so they define a single translation-covariant
   record law on all of Z^3.
2. **Static reading = formation reading.** In that law, a site's conditional
   distribution given *every other record* equals the rule's distribution
   given its six neighbours. The two readings of the Admissibility sentence
   compared in the 2026-09-06 note, which differ for the six-axis product
   class on every window with a plaquette, agree exactly here.
3. **1-dependence.** Records on two sets of sites with no edge between them
   are independent, however the sets are linked through other sites. This
   strengthens Theorem 1 of the 2026-09-22 note from pairwise non-adjacent
   single sites to arbitrary edge-separated sets.
4. **No critical or Coulomb correlations.** Every truncated correlation of
   local observables vanishes once their supports are edge-separated; every
   structure factor is `S(q) = C_0 + 2 sum_a C_a cos q_a`. Long-range order,
   power-law correlations and pinch points are impossible in this class.

## Premises and declared objects

The rule, alphabet, positivity and the sequential formation model are the
supplied objects of the 2026-09-22 note, used with the same definitions:
a rule assigns to each neighbour condition N (a partial map from the six
directions to formed neighbour values) a distribution r(.|N); a formation
order of a finite window draws sites sequentially; order-blind means every
order gives the same finished law. By that note's Theorem 2, strictly
positive translation-covariant order-blind rules are exactly the families

    r(a | N) = r0(a) prod_{(d,b) in N} phi_d(a, b),
    phi_d(a, b) = phi_{-d}(b, a),   E_{r0}[prod_{(d,b) in N} phi_d(., b)] = 1 for every N.

The framework axioms do not select this model; nothing here adopts it.

## Theorem 1 — product form and consistency

*Statement.* For every finite W and every order, the finished law is
`P_W(a) = prod_{x in W} r0(a_x) prod_{xy in E(W)} phi_{y-x}(a_x, a_y)`, with
E(W) the lattice edges inside W. For x in W, summing P_W over a_x gives
P_{W \ {x}}.

*Proof.* Along an order each site contributes r0(a_x) times one factor for
each already-formed neighbour, so each edge of E(W) contributes exactly once,
written (by bond symmetry) from either end. Summing over a_x isolates
`sum_a r0(a) prod_{y ~ x, y in W} phi_{y-x}(a, a_y) = 1` by normalisation on
the neighbour condition {(y - x, a_y)}; what remains is the product form on
W \ {x}. Iterating gives every marginal. The family {P_W} is consistent and
translation covariant, so Kolmogorov's extension theorem gives a unique
probability measure mu on A^{Z^3} with these finite marginals (A finite,
product topology). ∎

## Theorem 2 — the static reading holds exactly

*Statement.* mu(a_x | a_{Z^3 \ {x}}) = r(a_x | N(x)), where N(x) holds the six
neighbour records.

*Proof.* For any finite W containing x and its six neighbours, Theorem 1 gives
P_W(a_x | a_{W \ {x}}) = r0(a_x) prod phi(a_x, a_y) / sum_a r0(a) prod phi(a, a_y);
the denominator is 1, so the conditional is r(a_x | N(x)) and does not depend
on W. Letting W increase to Z^3, the martingale convergence theorem carries
this to the conditional given all other records. ∎

So mu is a Gibbs measure for the specification "each site is drawn from the
rule given its neighbours", with local partition function identically one.
Uniqueness of the Gibbs measure for that specification is not claimed.

## Theorem 3 — 1-dependence

*Statement.* If A and B are sets of sites with no lattice edge between them,
the records on A and on B are independent under mu.

*Proof.* For finite A, B, Theorem 1 gives the law of A ∪ B as the product
form on the induced subgraph of A ∪ B, which has no edge between A and B and
therefore factorises as P_A P_B. Infinite sets follow from the finite case
by the definition of independence of sigma-algebras. ∎

The marginal on two opposite corners of a plaquette is r0 ⊗ r0 although the
corners are joined by two paths; the runner checks this exactly.

## Theorem 4 — correlation consequences

*Statement.* For local observables F, G with edge-separated supports,
Cov(F, G) = 0. For a single-site observable h with C(r) = Cov(h(a_0), h(a_r)),
C(r) = 0 unless r is 0 or a lattice neighbour, so
S(q) = C(0) + 2 sum_a C(e_a) cos q_a, an entire function of q. In particular
mu has no long-range order, no power-law decay, no pinch-point singularity,
and the variance of a block sum is exactly |Λ| C(0) + 2 sum over edges in Λ
of the corresponding bond covariance.

*Proof.* Immediate from Theorem 3. ∎

**Bearing on the Coulomb lane.** A Coulomb (emergent U(1)) phase in static
records requires dipolar ~ r^-3 correlations and pinch points in S(q). By
Theorem 4, strictly positive order-blind formation cannot produce them on any
alphabet; such correlations need zeros/holes (hard constraints, cf. the
2026-09-22 holes note and the hard-ice measures of the Coulomb-selection
note) or an order-sensitive formation law.

## Exhibit (runner, exact)

The soldered 48-point chiral-pair rule (κ = 1/2) of the 2026-09-22 note,
compressed exactly to twelve classes of four points:

- normalisation on all 3^6 neighbour patterns, positivity, bond symmetry;
- plaquette: all 24 orders give the product form, total mass 1, the edge
  marginal is the two-site product form, the diagonal marginal is r0 ⊗ r0,
  and each full conditional equals the rule;
- 5-site path: the law of {0,1} ∪ {3,4} factorises, while the adjacent pair
  is correlated;
- <X_z X_{-z}> = κ/36 = 1/72 on a bond, 0 at distances 2 and 3, variance
  1/6, so S(q) = 1/6 + (1/36) cos q along z.

## What this does not do

- It does not classify order-blind rules or select a reading, alphabet or
  order; order-sensitive rules and rules with zeros are outside its scope.
- It does not claim uniqueness of Gibbs measures for the rule's
  specification, or anything about dynamics.
- It does not say Coulomb correlations are impossible in the framework, only
  in this class.

## No-Go Discipline Gate

### N1 — Routes that could evade Theorem 4
1. *Rules with zeros (holes)*: RULED OUT BY SCOPE; the 2026-09-22 holes note
   shows pair-form rules with failure produce 3^-d tails; not covered here.
2. *Order-sensitive rules*: RULED OUT BY SCOPE; finished laws then depend on
   the order and are not covered.
3. *Infinite alphabets*: the Kolmogorov step needs a standard Borel
   alphabet; the Haar-sphere exhibit qualifies, but the proofs here are
   written for finite alphabets.
4. *Non-translation-covariant rules*: outside the Admissibility covariance.
5. *Observables of infinite support*: Theorem 4 is for local observables.

### N2–N8
One structural statement with explicit hypotheses; no walls counted; the
prior results cited (2026-09-22 Theorems 1–2, 2026-09-06 Theorem B) are used
with their exact scopes; "cannot produce" is stated only for strictly
positive order-blind rules on finite alphabets and local observables.

## Verification

```bash
python3 scripts/order_blind_formation_one_dependent_record_field_2026_10_16.py
```

Expected: `TOTAL: PASS=17 FAIL=0` (about a minute).
