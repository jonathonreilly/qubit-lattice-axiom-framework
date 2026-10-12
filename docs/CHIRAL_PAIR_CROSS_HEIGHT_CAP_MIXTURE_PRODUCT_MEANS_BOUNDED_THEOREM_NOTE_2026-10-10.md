---
claim_id: chiral_pair_cross_height_cap_mixture_product_means_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), the sum of the height-1 and height-2 chirality caps at coefficient 1/2 is strictly positive, with values 1/2, 1, and 3/2, and every one-neighbour mean is 1. The two-neighbour mean on -e_x and -e_y at far ends (1, -3, -2) and (-3, 2, -1) is 97/96. Of the unordered two-direction partner pairs, 1536 have mean different from 1. The sum of the height-1 chirality cap and the height-2 sign-product cap, again at coefficient 1/2, is strictly positive with the same three values, and every one-neighbour mean and every two-direction mean is 1. Each record meets at most two live directions, so every neighbour product of the second mixture has mean 1. These are two named mixtures. The rational span of two opposite-height bases is not classified. The 300-dimensional affine space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_opposite_height_basis_mixtures_product_means_bounded_theorem_note_2026-10-10
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_cross_height_cap_mixture_product_means_2026_10_10.py
---

# Two cross-height cap mixtures have different product means

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_cross_height_cap_mixture_product_means_2026_10_10.py`](../scripts/chiral_pair_cross_height_cap_mixture_product_means_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
[the opposite-height mixture note](CHIRAL_PAIR_OPPOSITE_HEIGHT_BASIS_MIXTURES_PRODUCT_MEANS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "One cross-height cap mixture has two-neighbour moment 97/96, and another has every two-direction mean equal to 1."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide which rational coefficient pairs on two opposite-height bases have every cross moment equal to 0. Do not claim that 20-dimensional span is classified by these two mixtures. Do not claim the 300-dimensional affine space is classified."
conditional_surface_status: "48 signed permutations of (1, 2, 3); height-1 and height-2 caps; coefficient 1/2; witness far ends (1, -3, -2) and (-3, 2, -1)"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Quoted premises

Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site."

Admissibility: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations."

Reading note (2), interpretive: "Read with Record, the distribution
concerns which possibility a forming record locks, conditional on
formation at that site; it does not supply the formation site,
probability, or rate."

Theorem 2 of the parent: "with phi_d(a, b) = phi_-d(b, a) and
E_r0[prod_{(d, b) in N} phi_d(., b)] = 1 for every N. Conversely every
family with these properties is order-blind on every window." The parent
leaves the sentence "Other generic orbits and higher-rank bond spaces
are not classified."

## Theorem

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

**Target.** On the 48 signed permutations of `(1, 2, 3)`, compare two
rational mixtures that each use caps at two absolute heights.

**Ansatz.** The chirality cap at height `h` is the product of the orbit
signs on `a·d = h` and `b·d = -h`. The sign-product cap is that product
multiplied by the two transverse signs. The failing mixture is
`phi = 1 + (1/2) K_chi,1 + (1/2) K_chi,2`. The passing mixture replaces
the second kernel by the height-2 sign-product cap. A general
coefficient pair on the two ten-kernel bases is not in this ansatz. The
300-dimensional affine space is not classified.

**Conclusion.** Both mixtures are bond-symmetric and soldered. Each
takes values `1/2`, `1`, and `3/2`, so each is strictly positive. Every
far-end sum equals 48. Every one-neighbour mean equals 1.

For the failing mixture, the mean on `-e_x` and `-e_y` at far ends
`(1, -3, -2)` and `(-3, 2, -1)` is `97/96`. Among the unordered
two-direction partner pairs, `1536` have mean different from 1. Theorem
2's converse is not applied to this mixture.

For the passing mixture, every two-direction mean equals 1. Each record
meets at most two live directions, and those directions are not
opposites. A neighbour condition names at most one far end in each
direction, so every neighbour product has mean 1. Theorem 2's converse
makes this one family order-blind on every window.

**Proof.** The runner enumerates the proper rotations and the alphabet.
Both mixtures agree on every rotated bond and on every reversed bond.
The value set of each mixture is `{1/2, 1, 3/2}`. Summing the factor
over either endpoint gives 48. Summing one factor over the centre gives
48 for every far end.

On the witness, `b = (1, -3, -2)` lies on the height-1 cap of `-e_x`
and not on the height-2 cap, because `b·(-e_x) = -1`. The far end
`c = (-3, 2, -1)` lies on the height-2 cap of `-e_y` and not on the
height-1 cap, because `c·(-e_y) = -2`. Both orbit signs are `-1`. The
only contributing centres are `(-1, -2, 3)` and `(-1, -2, -3)`. Each
orbit sign squares to 1, so each centre contributes
`(1/2)(-1)(1/2)(-1) = 1/4`. The excess sum is `1/2`, and the uniform
mean is `1 + (1/2)/48 = 97/96`. The runner finds this value and finds
`1536` unordered pairs whose mean is not 1.

The same enumeration gives mean 1 for every one-neighbour condition and
every unordered two-direction pair of the passing mixture. A third
direction cannot carry a third factor of either mixture, because each
height meets a record in only one direction. The product over any
larger condition therefore reduces to one of the checked pairs.

Both heights are used. Some record is live in a height-1 direction and
a different height-2 direction.

**Obligations.** Proved here: soldered covariance, bond symmetry, the
value sets, the far-end sums, the one-neighbour means, the witness
moment `97/96`, the count `1536`, the passing two-direction means, and
the live-direction bound. Cited from Theorem 2, and not re-proved: bond
symmetry together with every product mean equal to 1 makes a strictly
positive family order-blind on every window. The converse is applied
only to the passing mixture. Cited from the opposite-height mixture
note, and not re-proved: inside one height every rational mixture
already has product mean 1. Cited from the chiral-pair bond note, and
not re-proved: far-end sum 1 is the normalisation of that bond space.
The strongest missing lemma is which rational coefficient pairs on two
opposite-height bases have every cross moment equal to 0.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not classify the rational span of two opposite-height bases.
- It does not claim that the 300-dimensional affine space is classified.
- It does not apply Theorem 2's converse to the failing mixture.
- It does not repeat the one-height classification.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_cross_height_cap_mixture_product_means_2026_10_10.py`
repeats the covariance comparison, the witness moment, and the
two-direction counts. `TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the two cap mixtures, and the moment sums are
enumerated here. Theorem 2's converse is applied to the passing mixture
only. The opposite-height mixture note supplies the one-height identity.
The chiral-pair bond note supplies the meaning of far-end sum 1.


## No-Go Discipline Gate

**Packet status: incomplete; no PASS claimed.** This is a partial narrowing
proposal under the displayed finite ansatz, not a framework-wide exclusion.

- **N1:** The actual routes here are the finite orbit/slice reduction and
  the explicit algebraic argument in the Proof. Related coefficient choices
  are not five independent approach families. The five-family packet is
  absent; no route count or retained prior authority is invented.
- **N2:** The alphabet, covariance, support and coefficient restrictions
  define one ansatz. No count of independent physical walls is asserted.
- **N3:** The uniform finite-record model and any order-blind converse are
  explicit mathematical inputs. They supply no physical selection, formation
  rate, empirical scale or additional framework primitive.
- **N4:** The Imports and Obligations identify which parent result is used.
  A finite kernel rank, a two-centre cross sum and a normalized neighbour
  product are different statements; none is substituted for another.
- **N5:** The primary runner reports the finite resolution it executes.
  Mode spectra, evolving site ensembles and lattice-wide dynamics are not
  computed. Any all-window consequence uses the cited analytical converse
  with strict positivity, not a lattice simulation.
- **N6:** No new axiom is requested or declared necessary. Expanding the
  ansatz is legitimate further work and is not ruled out by these results.
- **N7:** The strongest broader escape is to allow additional support
  signatures or coupled height sectors: cancellation can change when the
  partner domain changes. A full-space classification must derive the joint
  slice and product equations and prove their solution set; the present
  restricted result supplies no such closure. Inside the stated ansatz the
  displayed exact proof, rather than failure to find an escape, is the claim.
- **N8:** The cited parent and companion notes exhibit successive escapes
  from smaller cap and cross spans. Those examples explicitly prohibit
  treating any restricted span classification as closure of the full bond
  space. Historical next-step statements are local frontiers, not evidence
  that later companion results remain unproved.
