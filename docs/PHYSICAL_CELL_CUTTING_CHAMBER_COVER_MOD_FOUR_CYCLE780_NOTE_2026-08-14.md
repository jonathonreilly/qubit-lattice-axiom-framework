# Physical cell cutting: the covers are the chambers of a hyperplane arrangement, and the label sum of a cutting is divisible by four

Date: 2026-08-14
Authority: none
Audit: unset.
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.
Audit-status authority: independent audit lane only; this note authors no verdict.

## Trace gate

- `trace_class: frontier_discovery`
- `target_claim_id: null`
- `target_blocker_text: null`
- `source_of_blocker_text: frontier_question`
- `reachability_to_target: unknown_frontier`
- `artifact_role: theorem`
- `next_trace_action: test whether the finite chamber-cover and label-sum mechanism has a canonical downstream consumer; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact finite chamber-incidence and parity identities for the declared unit four-cube object; no broader physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Exact target, inputs, and proof obligations

The exact target is to prove, for the finite unit four-cube object rebuilt here, that its
192 eight-piece non-co-occurrence covers are exactly the 192 chambers of the displayed
hyperplane arrangement and that the handedness-label sum of each of its 15800 cuttings is
divisible by four.

The primary executable evidence is
[`scripts/physical_cell_cutting_chamber_cover_mod_four_cycle780_2026_08_14.py`](../scripts/physical_cell_cutting_chamber_cover_mod_four_cycle780_2026_08_14.py).

The import and support inventory is:

* **zero-input structural:** the runner starts from the 16 explicitly constructed corners
  of the unit four-cube and uses exact finite enumeration and integer/rational arithmetic;
* **declared finite conventions:** adjacency cost, the staircase-path naming, and the
  handedness label are definitions of this test object, not framework axioms or physical
  identifications;
* **repository scientific inputs:** none; the runner reads no external or ancestral
  scientific file, and earlier censuses are motivation only rather than premises;
* **literature, empirical, fitted, scale, normalization, and observational inputs:** none;
  and
* **implementation support:** Python's standard library only, which supplies no scientific
  value.

The unit-determinant five-corner candidates number 2672. The 400 candidates at adjacency
cost floor 6 have 15800 exact sample covers of 24 pieces; 192 pieces occur, each in 1975
cuttings, for 379200 incidence slots. Each occurring piece is a staircase path and has two
equivalent start-corner/axis-order namings.

The proof-obligation graph is:

| obligation | disposition in this note |
|---|---|
| rebuild the candidate and cutting census without an ancestral result | proved by K1 |
| prove every sample-selected set is a genuine geometric cell cutting | proved by K15: exact pair separators plus the unit volume sum |
| identify the occurring pieces with well-defined staircase paths and labels | proved by K2 |
| classify the arrangement chambers and their true piece incidence | proved by K3 and K5 |
| identify the chamber piece-sets with the covers and prove meets-once | proved by K6 and K7 |
| prove the local label formula | proved by K4 |
| prove both chamber parity certificates and their even global totals | proved by K8--K10 |
| telescope those certificates through each cutting and obtain divisibility by four | proved by K11 and K12 |

The theorem concerns this enumerated four-dimensional object only. Arrangement-wall points
are excluded from the open chambers; simplex boundary points may have more than one closed
simplex description and are not used for the unique chamber-incidence count. No claim is
made about another cell, dimension, lattice-wide dynamics, or a physical observable. No
lemma inside the stated target remains open. The strongest missing lemma outside the target
is a structural, non-enumerative proof of the measured bound `|S(T)| <= 8` (and, separately,
of the stronger observed corner-parity count modulo four).

## The chamber identification

**Chamber-cover theorem.** Put u = x - 1/2 in each of the four coordinates, so that u = 0 is the centre of the
cell. Cut the open cell by the 12 hyperplanes

> x_i = x_j and x_i + x_j = 1, one of each for every one of the 6 coordinate pairs,

that is, by u_i - u_j = 0 and u_i + u_j = 0. Name a chamber of that cut by the pair
(b, s), where b is the order of the four magnitudes |u_1|, ..., |u_4| taken decreasingly —
a permutation of the four axes — and s = (s1, s2, s3) collects the signs of u at the first
three slots of b. The sign at the fourth slot is **not** chamber data: u at that slot
vanishing is not one of the 12 walls, so both of its signs lie in one and the same chamber.
There are 24 orders times 8 sign triples = 192 chambers. The naming is faithful: the 192
exact rational sample points below realise 192 distinct sign patterns on the 12 walls, and
none of them sits on a wall (gate K3).

The following facts are all verified on the rebuilt object.

**(a) Each used piece holds exactly 8 chambers**, dealt by a sign recursion. For the piece
named (v0, sigma) and each rho in {+1, -1} of length 3, run down the axis list sigma
popping from the front when rho_k = +1 and from the back otherwise; the popped axes in
order are b, and s_k = rho_k times eta at b_k, where eta_j = 1 - 2 v0_j at the start
corner. The 8 values of rho give 8 distinct chambers, and the piece's other naming deals
exactly the same 8 (gate K3).

**(b) Each chamber lies in exactly 8 used pieces** (gate K3). The two counts agree on the
total: 192 times 8 = 1536 incidence slots, seen from either side.

**(c) The identification is geometric, not combinatorial bookkeeping.** For each chamber
take the exact rational point whose offsets from the centre are 8/20, 6/20, 4/20 and 2/20
down the b-order, with signs (s1, s2, s3, +1). Testing that point against the five integer
affine forms of each of the 192 pieces, with exact rational arithmetic, it lies strictly
inside exactly the 8 pieces that (a) assigns to it, with 0 mismatches over all 192 chambers
(gate K5). So the incidence dealt by the recursion is the true containment incidence.

**(d) The 192 chamber piece-sets are exactly the 192 covers.** They are pairwise distinct,
and the sorted list of them equals the sorted list of the covers returned by the clique
enumeration rebuilt in the primary runner (gate K7).

**(e) Each chamber meets each cutting in exactly one piece.** Checked directly on all 192
times 15800 = 3033600 chamber and cutting pairs, with 0 exceptions (gate K6).

Fact (e) is the conceptual content, and it has a short reason once the chambers are in
view: a cutting partitions the cell, so any point of the cell lies in exactly one of its 24 pieces,
and a whole chamber travels together because no piece boundary crosses a chamber. The
counting is tight — the 24 pieces of a cutting carry 24 times 8 = 192 chamber slots, which
is exactly the number of chambers, so the assignment is a bijection. This is what a cover
is: **a cover is the point-evaluation class of a chamber**, the set of pieces that can hold
that chamber. The covers stop being the output of a search over the 192 pieces; they are
read off the arrangement, which does not know about the cuttings at all.

## The local label formula

**Local-label theorem.** For every incident piece and chamber pair,

> L(P) = sign(b) times s1 times s3 times eta at b2 times eta at b4,

where sign(b) is the sign of the order b as a permutation, s1 and s3 are the first and
third chamber signs, and eta is taken at the start corner of P. Verified on all 192 times
8 = 1536 incident pairs with 0 failures (gate K4).

Two readings. First, the handedness of a piece is a *local* quantity: one chamber it holds,
plus the corner parity of the piece at two slots of that chamber's order, already determine
it. Second, the formula is what makes the next section work, because it expresses L in
chamber data on which one can build functions of the chamber alone.

## The mod-four law, derived

Write, for a piece P with naming (v0, sigma),

> q_order(P) = 1 when sign(sigma) = -1 and 0 otherwise, and q_corner(P) = the weight of v0 modulo 2.

Both are well defined on the path, not merely on the naming: the two namings of a piece
agree on L and on the pair (q_order, q_corner) for all 192 pieces, and each statistic equals
1 on 96 of them (gate K2).

**(i) Product form.** L(P) = (1 - 2 q_order(P)) times (1 - 2 q_corner(P)) on all 192 pieces
(gate K2).

**(ii) The per-cutting identity.** Let N_order be the sum of q_order, N_corner the sum of
q_corner, and N_joint the sum of q_order q_corner, all over the 24 pieces of a cutting T.

> S(T) = 24 - 2 N_order(T) - 2 N_corner(T) + 4 N_joint(T),

an identity holding on all 15800 cuttings with 0 failures (gate K11). It is (i) expanded:
each piece contributes 1 - 2 q_order - 2 q_corner + 4 q_order q_corner.

**(iii) Certificates on chambers.** Define two functions of a chamber c = (b, s) alone:

> g_corner(c) = 1 when sign(b) times s1 s2 s3 = +1, and 0 otherwise;
> g_order,j(c) = 1 when sign(b) = -1 and the last slot b4 is a fixed axis j, and 0 otherwise.

Then, for every one of the 192 pieces P:

* **Corner-parity certificate.** The sum of g_corner over the 8 chambers of P is congruent
  to q_corner(P) modulo 2 — 0 failures (gate K8).
* **Order-parity certificate.** The sum of g_order,j over the 8 chambers of P is congruent
  to q_order(P) modulo 2, and this holds for each of the 4 choices of the fixed axis j: 768
  checks, 0 failures (gate K9).

So each of the two piece statistics that build the label is recovered, modulo 2, from a
function of the chambers the piece holds.

**(iv) The totals are even.** Summed over all 192 chambers, g_corner has weight 96, and
g_order,j has weight 24 for each of the four axes (gate K10). Both are even, and that is
the whole input the next step needs.

**(v) Telescoping.** Fix a cutting T and sum the corner-parity certificate over its 24
pieces. The left side is a double sum over pairs (P, c) with P in T and c a chamber of P.
By the meets-once part of the chamber-cover theorem, each chamber belongs to exactly one
piece of T, and every chamber belongs to some piece of T, so the pairs are in bijection
with the 192 chambers and the double sum collapses to the total
weight of g_corner over all chambers, which is 96 by (iv). The right side is N_corner(T)
modulo 2.
Hence

> N_corner(T) is congruent to 96, that is to 0, modulo 2, for every cutting.

The same argument with g_order,j at a fixed axis gives N_order(T) congruent to 24, that is
to 0, modulo 2. Both are confirmed directly: 0 cuttings of the 15800 have odd N_order, and
0 have odd N_corner (gate K11). Now feed the two parities into (ii). Modulo 4 the term
4 N_joint drops, and 2 N_order and 2 N_corner both drop because the two counts are even,
leaving

> S(T) congruent to 24, that is to 0, modulo 4, for every cutting.

Directly: S is divisible by 4 on all 15800 cuttings, 0 exceptions, with census -8 on 120
cuttings, -4 on 2832, 0 on 9896, 4 on 2832 and 8 on 120 (gate K12). The divisibility by 4,
previously available only as a census fact, is therefore derived here from the meets-once
property plus the two piecewise certificates and the two even totals.

The chain has a control. Gate K13 perturbs it in two ways: flipping g_corner at a single
chamber breaks the corner-parity certificate at exactly 8 pieces, precisely the pieces
that hold that chamber; and
negating the label of a single piece breaks the identity (ii) at exactly 1975 cuttings,
precisely the cuttings through that piece. Both perturbations are detected, and each count
is the one the structure predicts, so the gates can fail and do fail when the object is
disturbed.

## What this does not establish

**The bound on the size of S is measured, not derived.** The census says S lies in the five
values -8, -4, 0, 4, 8, so |S| is at most 8 over the 15800 cuttings; nothing above forces
that bound. Divisibility by 4 restricts S to a lattice, not to an interval, and the
derivation in the mod-four law section is silent about size.

A live path towards the bound, opened by the same chamber picture and reported here as a
measurement only: group the 24 pieces of a cutting by their main diagonal, taking the
smaller of the start corner and its opposite, which gives 8 diagonals, and let D_w be the
label sum of the pieces on diagonal w. Measured over the 15800 cuttings, |D_w| never
exceeds 4, and the maximum is attained; the sum over the 8 diagonals of |D_w| takes the
value 0 on 9320 cuttings, 4 on 6096 and 8 on 384, so its largest value is 8 (gate K14).
Since |S| is at most the sum of |D_w| by the triangle inequality, and that sum has largest
value 8, a per-diagonal bound proved rather than measured would deliver the bound on |S|
pointwise. That derivation is not attempted here.

**The corner-parity count modulo 4 is observed, not derived.** N_corner is divisible by 4
on all 15800 cuttings (gate K14), which is stronger than the parity the telescoping argument
gives. A certificate in the style of (iii) taking values modulo 4 rather than modulo 2
would sharpen the whole law; none is offered here, and finding one is the natural next path.

Two further limits, stated plainly. The mod-four derivation uses the meets-once property,
which is checked on all 3033600 chamber/cutting pairs and also follows from the exact
simplex-separation and volume certificate in K15. The claim type is `bounded_theorem`, not a
stronger one, because the object is the finite cell rebuilt here; nothing extends the result
to another cell or a physical lattice.

## Self-containment and dependency boundary

The runner rebuilds the finite object, the staircase-path label, the clique covers, the
chambers, and the cutting census. It uses no scientific result from an earlier branch or
unlanded note, so this note intentionally has no citation-graph dependency edge. Prior
censuses supplied the question only; every load-bearing premise is reconstructed here.

## Gate list with the measured numbers

All 15 gates are computational identities about the explicitly rebuilt finite object, exact
over the integers and the rationals; no floating point enters any gate. The runner is
linked above and uses the standard library only.

* **K1** object rebuild: 2672 unit pieces, cost floor 6, 400 at the floor, 15800 cuttings
  of 24, 192 used pieces each in 1975, 379200 slots, 384 namings, 2 per piece.
* **K2** the label: product form on 192 of 192 pieces; both namings agree on L and on
  (q_order, q_corner) for 192; each statistic equals 1 on 96.
* **K3** the chambers: 12 walls, 24 orders times 8 signs = 192 chambers, 8 per piece from
  either naming, 8 pieces per chamber, 192 distinct wall sign patterns, 0 on a wall.
* **K4** the local formula on all 192 times 8 = 1536 incident piece and chamber pairs,
  0 failures.
* **K5** geometry: 192 exact sample points, offsets 8/20, 6/20, 4/20, 2/20 from the centre,
  each strictly inside exactly 8 of the 192 pieces, 0 mismatches.
* **K6** the partition read at a point: on all 192 times 15800 = 3033600 chamber and
  cutting pairs the meeting is exactly 1 piece, 0 exceptions.
* **K7** the clique enumeration returns 192 covers of 8, and the sorted cover sets equal
  the 192 distinct chamber piece-sets.
* **K8** the corner-parity certificate on all 192 pieces, 0 failures.
* **K9** the order-parity certificate on all 192 pieces for each of the 4 axes, 768 checks,
  0 failures.
* **K10** totals over the 192 chambers: g_corner weight 96, g_order,j weight 24 on each axis,
  all even.
* **K11** per cutting on all 15800: the identity holds with 0 failures; cuttings of odd
  N_order 0, of odd N_corner 0.
* **K12** S divisible by 4 on 15800 of 15800 cuttings, 0 exceptions; census -8:120,
  -4:2832, 0:9896, 4:2832, 8:120, sum 15800.
* **K13** the control: flipping g_corner at one chamber breaks the corner-parity certificate
  at exactly 8 pieces; negating one piece label breaks the identity at 1975 cuttings.
* **K14** the boundary: 8 diagonals, largest |D_w| 4, census of the sum of |D_w| 0 on 9320,
  4 on 6096, 8 on 384, largest 8, N_corner divisible by 4 on 15800.
* **K15** exact cutting geometry: all 15168 co-occurring simplex pairs have a weak separator
  among the 80 nonzero ternary normals, and 24 unit-determinant simplex volumes sum to the
  unit four-cube volume.
