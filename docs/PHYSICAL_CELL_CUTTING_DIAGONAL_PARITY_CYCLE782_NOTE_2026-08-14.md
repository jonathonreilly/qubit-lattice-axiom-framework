# Physical cell cutting: the odd-diagonal count of every cutting is divisible by four

Date: 2026-08-14

Authority: none; self-contained finite construction proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [diagonal-label parity runner](../scripts/physical_cell_cutting_diagonal_parity_cycle782_2026_08_14.py)

Direct scientific dependencies: none.

Constitutional effect: none. This note changes zero axioms, primitives,
registries, policy rules, audit verdicts, effective statuses, or framework claims.

## Trace and status fields

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "the target domain is the declared finite unit-four-cube object and its exhaustively enumerated cutting family"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite geometry and combinatorics on the declared unit-four-cube object"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What this cycle asks

The unit four-cube cell object is rebuilt from scratch here. Of the 2672 five-corner sets
of normalized volume 1, the ones at the adjacency cost floor 6 number 400. A shifted
625-point rational grid enumerates 15800 candidate covers of 24 pieces. For every candidate,
the runner separately checks that its 24 normalized volumes sum to the cube volume and that
each of its simplex pairs has disjoint interior, witnessed by an integer separating
hyperplane. Thus all 15800 candidates are continuous exact cuttings of the unit four-cube,
not merely covers of the enumeration grid (gates K1 and K1G). The pieces that actually occur
number 192. Naming a piece by a start corner together with an order of the four axes gives
384 namings, 2 per piece. The two namings of a piece carry opposite start corners and
reversed axis orders, and the minimal naming is the one whose start corner is the smaller
of the two. Write (v0, sg) for that minimal naming.

Every piece then carries a **diagonal label** diag(P) = v0, a value below 8, the lower of
the two opposite corners the staircase path runs between. The quantity this cycle is about
is the **odd-diagonal count**

> N_odd_diag(T) = the number of pieces of the cutting T whose diagonal label has odd corner
> weight, that is, whose label is one of 1, 2, 4, 7.

`cycle 780` derived a divisibility by 4 for the handedness label sum, and `cycle 781`
sharpened it to a pointwise identity and a size bound. Neither says anything about the
diagonal label, which is a different per-piece attribute: it is a corner, not a sign, and
it is blind to the axis order that the handedness label reads. The census of the
odd-diagonal count over the 15800 cuttings nonetheless lands on multiples of 4 only. This
note derives that.

## Exact target

> **T.** N_odd_diag(T) is divisible by 4 for every one of the 15800 continuously certified
> cuttings T of the declared unit four-cube object.

This is a theorem only on that exact finite family. It makes no claim that the selection
rule is physically preferred and no claim about other cells or other cutting families.

## Inputs, imports, and provenance

| Item | Classification | Role in the claim |
|---|---|---|
| `{0,1}^4`, five-corner simplices, determinant, adjacency-cost floor, and exact-cover rule | zero-input structural | Declare the finite object and the family being exhaustively enumerated. |
| Exact integer/rational arithmetic, normalized simplex volume, and separating-hyperplane criterion | zero-input structural | Certify candidate admissibility and continuous coverage; no floating-point or fitted threshold enters. |
| The shifted 625-point rational grid | zero-input structural enumeration device | Enumerates candidate covers. It is not used as a surrogate for continuous coverage; K1G separately certifies every emitted candidate. |
| Minimal complement-and-reversal naming and the choice of coordinate 3 for the half set | explicit normalization/boundary condition | Declare the finite labels and selected half set. K13 checks naming invariance; the coordinate choice remains explicit and the theorem is scoped to it. |
| The two census distributions | support-only | Exhaustive descriptive outputs. Their multiplicities are not premises of the mod-four derivation. |
| Sibling-cycle names | support-only provenance | Terminology comparison only. No sibling result or file is a scientific dependency, and the runner rebuilds every load-bearing object. |
| Framework axioms/primitives, literature values, observations, fits, PDG/cosmological values, or continuum/physical identifications | none | No such input is used or claimed. |

## Proof-obligation graph

1. **O1 — object admissibility.** Enumerate all shifted-grid covers from the 400 floor
   simplices, then independently certify unit normalized volumes, pairwise interior
   separation, and total cube volume. This establishes the 15800 continuous cuttings.
2. **O2 — chamber partition.** Rebuild the 192 chambers and show that every cutting meets
   every chamber in exactly one piece.
3. **O3 — local-to-global count.** Prove the five-valued chamber law piece by piece and
   telescope it with O2 to obtain the congruence for each diagonal-label count.
4. **O4 — transported-label coupling.** Identify the six-valued class with the selected
   half set, prove parity transport, and sum over the four odd labels.
5. **O5 — parity certificate.** Exhibit the 20-member certificate chamber set, check its
   per-piece parity law, and telescope with O2 to make the selected odd count even.
6. **O6 — target.** Combine O4 and O5 to conclude T.

The runner closes O1-O6 by exact finite arithmetic. None of the obligations assumes T or
an equivalent mod-four statement, and no observational or framework bridge is needed.

The derivation is local everywhere except at one place. A chamber is named (b, s) as in
`cycle 780`, with b the order of the four magnitudes of u = x - centre taken decreasingly
and s the signs of u at the first three slots of b; the sign at the fourth slot is not
chamber data. There are 192 chambers, each piece holds 8 of them, each chamber lies in 8
pieces, and every chamber meets every cutting in exactly one piece. That last statement,
the partition property of `cycle 780`, is re-verified on the rebuilt object with 0 failures
over the 15800 cuttings (gate K1), and it is the only global input used below: every other
step is a statement about one piece and its 8 chambers, or about one chamber.

Two derived sets of pieces are used throughout. The **half set** H is the set of pieces
whose minimal naming steps axis 3 within its first 2 steps; H has 96 members. The
**odd-diagonal half-set indicator** hodd(P) is 1 when P lies in H and its diagonal label
has odd corner weight, and 0 otherwise; exactly 48 of the 192 pieces have hodd = 1
(gate K8). The choice of axis 3 is a choice of one coordinate, made once and kept.

## The sign classes and the local law

Each label w below 8 gives a sign pattern on the four axes, plus one where the bit of the
label is clear and minus one where it is set. Because the labels run below 8 the fourth
axis always carries plus one, so the pattern is genuinely a pattern on three axes with a
fixed fourth. Let Y_w be the class of chambers whose signs agree with that pattern at the
three axes their own order puts first. Each of the 8 classes holds exactly 24 of the 192
chambers (gate K2).

Fix a piece i with minimal naming (v0, sg) and a label w. Compare the sign pattern of the
label diag(i) with the sign pattern of w, not axis by axis but **step by step**: the
mismatch pattern of the pair is the set of step positions k at which the two patterns
disagree at the axis sg[k] that the piece takes at step k. The count of chambers of the
piece lying in Y_w depends on nothing else.

> **T1 (the local law).** For every one of the 1536 pairs of a piece and a label, the
> number of chambers of the piece lying in Y_w is 1 when w is the label of the piece;
> 4 when the mismatch pattern is the last step alone, or the last three steps together;
> 6 when it is the last two steps; and 0 in every other case.

Verified with 0 failures over the 1536 pairs, and the pair classes themselves are counted
rather than assumed: 192 self pairs, 144 pairs whose mismatch is the last step alone, 48
whose mismatch is the last three, 96 whose mismatch is the last two, and 1056 pairs that
contribute nothing. The weighted total is 192 plus 4 times 144 plus 4 times 48 plus 6
times 96, which is 1536, and 1536 is also 8 times 192, one entry for each chamber of each
piece (gate K3). The law is therefore not merely consistent, it is complete: it accounts
for every chamber of every piece exactly once.

## The telescoping identity

Sum the local law over the 24 pieces of a cutting T. By the partition property the left
side counts each of the 24 chambers of Y_w exactly once. On the right, write n_w for the
number of pieces of T whose label is w, a_w for the number whose mismatch pattern at w is
the last step alone, c_w for the number whose mismatch is the last three steps, and q_w
for the number whose mismatch is the last two. Then

> n_w = 24 - 4 a_w - 4 c_w - 6 q_w,

on every cutting at every label, with 0 failures over the 126400 instances (gate K4).
Reduce modulo 4. The two four-weighted terms drop, and 6 q_w becomes 2 q_w, so

> n_w is congruent to 2 q_w modulo 4.

The whole of the mod-four behaviour of the label counts is carried by the class with the
six-valued entry. That the 6 is doing the work and not the 4 is checked directly: replacing
the six-valued entry of the local law by 4 breaks the rule at exactly 96 pairs, which are
exactly the pairs of that class (gate K12).

## The transported label

The class carrying the 6 has a closed form, and the closed form is what turns a statement
about labels into a statement about pieces. For a piece i, let x(i) be the diagonal label
with the bits of the last two axes of its order flipped, and let phi(i) be the smaller of
x(i) and the corner opposite to x(i), so that phi(i) is again a label below 8.

> **T2 (the q class).** For every one of the 1536 pairs, the mismatch pattern of the pair
> is the last two steps if and only if the piece lies in the half set H and phi of the
> piece equals the label w.

Verified with 0 failures, and the 8 fibres of phi on H are counted and all have size 12,
so phi spreads the 96 pieces of H evenly over the 8 labels (gate K5). In particular q_w is
the number of pieces of T lying in H with phi equal to w.

> **T3 (parity transport).** On each of the 96 pieces of H, the corner weight of phi has
> the same parity as the corner weight of the diagonal label.

Verified with 0 failures (gate K6). The reason is short enough to state: x differs from
the diagonal label by flipping the bits of two distinct axes, which changes the corner
weight by an even amount, and passing to the opposite corner flips all 4 bits, which is
even again. So the parity survives both operations.

Now sum over the four labels of odd corner weight. On the left the telescoping identity
gives N_odd_diag(T), the odd-diagonal count, as the sum of n_w over those four labels. On
the right the sum of q_w over those four labels counts the pieces of T lying in
H whose phi is odd, which by T3 is the count of pieces of T lying in H whose diagonal label
is odd, that is, the hodd-count of T. That coupling is checked on its own, with 0 failures
over the 15800 cuttings (gate K14). Hence

> N_odd_diag(T) is congruent to 2 times the hodd-count of T, modulo 4.

Divisibility by 4 is now exactly the statement that the hodd-count is even.

## The parity certificate

The evenness comes from a function of the chamber alone, gathered into the **certificate
chamber set** by five conditions. Two of them sit over the chambers whose order carries
axis 3 in its
second slot with second sign plus one: one takes the orders whose last two slots ascend,
together with disagreeing first and third signs, and the other the orders whose last two
slots descend, together with third sign plus one. Each of those two cells holds 6 chambers.
The remaining three sit over the chambers whose order opens with axis 3 and whose first
sign is plus one: the orders whose last three slots ascend contribute 2 chambers when the
second and third signs agree, the orders whose third slot carries the largest of the last
three axes contribute 4 chambers when the second sign is minus one, and the orders whose
last three slots descend contribute 2 chambers when the third sign is plus one.

> **T4 (the certificate).** The five cells are pairwise disjoint, of sizes 6, 6, 2, 4 and 2,
> so the certificate chamber set holds 20 chambers, an even number; and for every one of the
> 192 pieces, the number of its chambers lying in that set has the same parity as hodd of the
> piece.

The disjointness and the five sizes are measured on the rebuilt object, not read off the
conditions, and the per-piece parity law holds with 0 mismatches over the 192 pieces, its
support being the 48 pieces with hodd = 1 (gates K7 and K8).

Sum the parity law over the 24 pieces of a cutting. By the partition property the left side
counts each certificate chamber exactly once, giving 20, which is even. The right side is the
hodd-count of T. Therefore

> **every cutting holds an even number of odd-diagonal half-set pieces**,

with 0 failures over the 15800 cuttings (gate K9). Combined with the previous section,
N_odd_diag(T) is congruent to 2 times an even number modulo 4, hence to 0, which is theorem
T, and it too is confirmed cutting by cutting with 0 failures over the 15800 (gate K10).

That the certificate is load-bearing rather than decorative is checked by dropping a single
chamber from it: the per-piece parity law then fails at exactly 8 pieces, and those 8 are
exactly the pieces holding the dropped chamber (gate K11). The number 8 is measured on the
perturbed object and compared with the count the incidence structure predicts, not imposed.

A last check guards the one arbitrary-looking ingredient, the minimal naming. All of diag,
membership in H, and hodd are recomputed from the second naming of each piece, using the
complement-and-reversal algebra directly on its raw start corner and axis order rather than
by looking the minimal naming up first, and the resulting 192 values agree everywhere
(gate K13). The theorem does not depend on which of the 2 namings of a piece is held.

## The two censuses

Both distributions are **measured, not derived**. Over the 15800 cuttings the hodd-count
takes the value 0 on 472 cuttings, 2 on 1848, 4 on 3384, 6 on 4392, 8 on 3384, 10 on 1848
and 12 on 472; the values are exactly the even numbers up to 12, and the shape is symmetric
about 6 (gate K9). The odd-diagonal count takes the value 0 on 112 cuttings, 4 on 1176, 8 on 3936,
12 on 5352, 16 on 3936, 20 on 1176 and 24 on 112; the values are exactly the multiples of 4
up to 24, and the shape is again symmetric, about 12 (gate K10).

The derivation above forces the support of both censuses and nothing more. It says the
hodd-count is even and that the odd-diagonal count is a multiple of 4; it does not say why the middle values
are so much heavier, why the two are so nearly proportional, or why the ends carry 472 and
112 respectively. The censuses are measured, not derived; the divisibility is derived.

## What this does not establish

**The census shapes are not derived.** Only the support is. The symmetry of both
distributions, the peak at the middle value, and every individual multiplicity above are
measurements on the rebuilt object, and nothing in the chain predicts them. In particular
the derivation constrains the odd-diagonal count to the multiples of 4 between 0 and 24 and does not exclude
any of them.

**The certificate is exhibited, not derived.** The certificate chamber set is given by five conditions on
the chamber and its correctness is a finite check over the 192 pieces; nothing here derives
those conditions from the geometry, and no claim is made that they are the only such set.
The same applies to the closed form phi and to the local law: each is stated and checked,
and each could have other presentations.

**The half set carries a choice.** H is defined by axis 3 appearing within the first 2
steps of the minimal naming. The derivation never uses which coordinate was taken, but
neither does it show that the choice is immaterial, and nothing is claimed about the
half sets the other three coordinates would give.

**The chamber partition property is verified by exhaustive incidence, not assumed from a
predecessor.** It is checked over all 15800 cuttings on the rebuilt object. Separately, K1G
uses normalized volumes and pairwise separating hyperplanes to certify that those objects
are continuous geometric cuttings of the cube.

**Nothing here leaves the declared cutting family.** The claim type is bounded_theorem
because the statements concern only the unit four-cube object as rebuilt, with its 192
pieces, 192 chambers, and 15800 continuously certified cuttings. The continuous geometry
certifies those finite objects; it is not an extension to another cell or a larger family,
and no physical interpretation is claimed or implied.

## Relation to sibling cycles

The terminology parallels `cycle 779`, `cycle 780`, and `cycle 781`, but no predecessor
construction or conclusion is imported: this note's runner rebuilds the object, continuous
geometry, chamber picture, partition property, minimal naming, and half set. The note
extends that line rather than correcting it, and nothing in any sibling cycle is withdrawn.
The attribute studied here is new: `cycle 780` and `cycle 781` both concern the handedness
label, a sign, whereas the odd-diagonal count concerns a property of the diagonal label, a
corner. The local law, transported label phi, parity transport, and parity certificate are
new here.
The half set reappears in a different role, as the support of the class carrying the
six-valued entry of the local law rather than as the carrier of a label sum, and the fact
that the same 96 pieces serve both is a measurement, not something derived. All references
above are decorative names only, with no citation edges and no scientific dependency.

## Gate list with the measured numbers

All 15 gates are computational identities about the explicitly rebuilt finite object, exact
over the integers and the rationals; no floating point enters any gate. The runner is
`scripts/physical_cell_cutting_diagonal_parity_cycle782_2026_08_14.py` and it uses the
standard library only.

* **K1** object rebuild: 2672 unit pieces, cost floor 6, 400 at the floor, 15800 cuttings
  of 24, 192 used pieces, 192 chambers, 8 chambers per piece, 8 holders per chamber, and
  the partition property with 0 failures over the 15800 cuttings.
* **K1G** continuous geometry: two independent determinant formulas agree; every selected
  simplex has normalized volume 1; and all 15168 co-occurring simplex pairs are separated
  by at least one of the 80 nonzero integer normals in {-1,0,1}^4. Therefore every
  24-piece candidate is a continuous exact cutting of the cube.
* **K2** the sign classes: each of the 8 label classes holds 24 of the 192 chambers, 0 size
  failures over the 8.
* **K3** the local law 1, 4, 4, 6, 0 by mismatch pattern, 0 failures over the 1536 pairs,
  with pair classes 192 self, 144 and 48 at the value 4, 96 at the value 6, 1056 at 0, and
  weighted sum 1536.
* **K4** the telescoping identity for n_w on every cutting at every label, 0 failures over
  the 126400 instances.
* **K5** the q class: the six-valued mismatch pattern holds exactly at the half-set pieces
  with phi equal to the label, 0 failures over the 1536 pairs, and 8 fibres of phi of
  size 12.
* **K6** parity transport on the half set, 0 failures over its 96 pieces.
* **K7** the certificate shape: five pairwise disjoint clause cells of sizes 6, 6, 2, 4, 2,
  total 20 chambers, even.
* **K8** the certificate law: per-piece parity of the certificate count equals hodd, 0
  failures over the 192 pieces, support 48.
* **K9** evenness: every cutting holds an even number of odd-diagonal half-set pieces, 0
  failures over the 15800, with the census 472, 1848, 3384, 4392, 3384, 1848, 472.
* **K10** the theorem: the odd-diagonal count is the sum of n_w over the odd labels 1, 2,
  4, 7, congruent to 2 times the hodd-count and to 0 modulo 4, 0 failures over the 15800,
  with the census 112, 1176, 3936, 5352, 3936, 1176, 112.
* **K11** the first control: dropping 1 chamber from the certificate breaks the per-piece
  parity at exactly 8 pieces, its holders.
* **K12** the second control: replacing the 6 of the local law by 4 breaks the rule at
  exactly 96 pairs of the 1536, exactly the q class.
* **K13** naming invariance: the second of the 384 namings, 2 per piece, taken by
  complement and reversal, gives the same 192 hodd values, 0 failures.
* **K14** the coupling: the sum of q_w over the four odd labels equals the hodd-count of
  the cutting, 0 failures over the 15800.
