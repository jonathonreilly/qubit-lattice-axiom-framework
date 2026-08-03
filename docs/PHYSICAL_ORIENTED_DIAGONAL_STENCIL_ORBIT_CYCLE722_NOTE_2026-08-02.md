# The assembly stencil names an *oriented* body diagonal; projection is what makes the frame label four-valued — Cycle 722

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02.py`
(51 PASS / 0 FAIL, exit 0).

## Why this exists

Cycles 717–721 read an order-12 frame group, a proper sextet, and a four-valued
frame label off the landed **static** second-variation form, and cycle 721
(`PHYSICAL_STENCIL_DERIVED_CENTRALITY_CYCLE721_NOTE_2026-08-02`, in flight)
derived that whole reading from the assembly stencil's body diagonal without
evaluating an assembled form at all. It left two questions standing in its own
closing text: **which** admissible stencils share the body-diagonal line and
whether the framework selects one — which moves the question onto the axioms —
and what happens at **tick length beyond 2**, where the tick complement is no
longer the identity.

Both are answered here. The first answer is clean and it is an axiom-level
answer. The second answer is not the one cycle 721 anticipated, and this note
records the correction explicitly.

## Setup

The [tick extension of the cubic Regge second
variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
(landed, unaudited) fixes a 3+1 complex whose tick direction is one of the
fifteen 0/1 classes. The landed compiler
`scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`
assembles the static form on a spatially open box at tick length 2. This runner
imports that compiler's **local** pieces verbatim — its direction classes, its
edge-length class map, its simplex and area gradients, and its finite-difference
Hessian step — and rebuilds the assembly on the **tick-resolved** complex at tick
lengths 2, 3, 4 and 5, with the tick direction periodic and the three spatial
directions open.

The assembly stencil is the Kuhn path triangulation of the unit 4-cube: the 24
simplices whose vertex chain runs from one corner to the opposite corner by
flipping the four coordinates in some order. Each such stencil is named by its
main diagonal. Writing the diagonal as *(a, 0) → (1−a, 1)* with *a ∈ {0,1}³* the
spatial corner at tick 0, there are exactly **eight** stencils, one per
**oriented** main diagonal of the 4-cube, and four unoriented diagonal **lines**.
Write *S_a* for the stencil and *Q[S_a]* for the form it assembles.

Edge slots are classified by a **sign-absorbing** rule: the class is the
componentwise absolute step and the anchor is the componentwise minimum of the
two endpoints, so a step and its reverse land on the same slot. Gate B fixes this
rule against the landed cell template (0 slot mismatches over 240) and against an
anchor law — *anchor + class direction* must be the far endpoint of the slot —
which the sign-absorbing rule satisfies on all 1920 slots of all eight stencils
and which a sign-blind rule violates on 1116 of them.

## Result

**T1 — the static form is blind to tick length.** The tick-resolved assembly
contracts onto the landed static form exactly, with the **entire** tick-length
dependence carried by the overall factor *LT/2*: deviation below 1.0e-09 at
(L, LT) = (3, 2), (3, 3), (4, 2), (4, 3), against form scale 2.945214e+01. A
rejector using a shifted tick-length factor fires at 2.945214e-02. The static
form therefore cannot see anything tick length does, and cycles 717–721 could not
have seen it either.

**T2 — the axioms select no stencil.** Assembly is covariant for the LATTICE
axiom's proper cubic rotations: relabelling by *g* carries *Q[S_a]* onto
*Q[S_{g·a}]* below 1.0e-09 over 192 (frame, stencil) pairs at (3, 3) and at
(4, 2), while holding the stencil fixed under the same relabelling is refused at
2.789850e+00. The 24 proper rotations act **transitively** on the eight oriented
diagonals (stabilizer of order 3) and on the four diagonal lines (stabilizer of
order 6, the sextet). Every stencil is carried onto every other by an axiom
symmetry, so no axiom-admissible frame prefers one: **the label counts an orbit,
not a preference.** The line stabilizer of order 6 agrees with the [proper-cubic
covariance
ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md)
reading that the Kuhn complex attains 6.

**T3 — the frame label is eight-valued on the tick-resolved complex.** At tick
lengths 2, 3 and 5 the eight stencils give eight distinct forms (dimensions 446,
669, 1115) and the 24 proper frames sort them into eight classes of three. The
four-valued label of cycles 717–721 is **not** present before a projection.

**T4 — the identification law.** Over three tick lengths and four projections —
tick-resolved or tick-folded, all classes kept or temporal classes dropped —
twelve rows out of twelve obey a single exceptionless rule:

> the projected form admits an order-12 frame group **exactly when** the
> projection identifies the two stencils sharing one diagonal line, and an
> order-6 group exactly when it separates them.

Identifications sit below 1.0e-09; separations sit at 2.789850e+00 or at
1.000000e+00. Order 12 is therefore not a property of the geometry; it is a
property of what the projection **cannot distinguish**.

**T5 — two projections identify, and tick length tells them apart.** The tick
fold identifies at every tick length checked. Dropping the temporal classes
identifies only at tick length 2: at tick lengths 3, 4 and 5 the stencils stay
apart at floor exactly 1.000000, while at those same tick lengths the fold still
identifies below 1.0e-09. The landed static form applies **both** projections at
once, which is precisely why cycles 717–721 saw only the folded answer.

**T6 — the improper half needs a tick reversal; it does not vanish.** Spatial
signed permutations combined with tick **translations** admit order 6 at every
tick length in {2, 3, 4, 5}. Admitting a simultaneous tick **reversal** raises
this to order 12 at every one of those tick lengths. Inside the 48 signed axis
permutations the stabilizer of the **unoriented** diagonal line has order 12 —
exactly the group cycles 717–721 measured — while the stabilizer of the
**oriented** diagonal has order 6. The improper half is precisely the
orientation-reversing coset of the oriented stabilizer inside the line
stabilizer.

**T7 — the box-centre point reflection is an intertwiner.** The reflection sends
source corner 000 to 111 and carries *Q[S_000]* onto *Q[S_111]* below 1.0e-09. It
enters through the compiler's **computational identities** and is not a new
symmetry postulate. Its apparent failure when applied to *Q[S_000]* alone is
2.789850e+00 — exactly the minimum separation between *Q[S_000]* and the other
seven forms, and independent of box size. What looked in earlier cycles like a
symmetry a single stencil breaks is the stencil separation itself, seen through a
map that changes stencil.

**T8 — restoring the axiom's full symmetry has a priced cost.** Averaging the
eight forms at equal weight restores all 48 signed axis permutations and
collapses the frame label to a single class. The cost, measured as the distance
from the averaged form to any member of the orbit, is 1.394925e+00 — exactly half
the stencil separation 2.789850e+00. Full frame symmetry is available; it is
bought by giving up the distinction between the eight stencils.

**T9 — the stencil is derived structure, not the axiom's adjacency.** The stencil
carries 240 edge slots, 120 of them spatial. Of those 120, 72 lie along the six
nearest-neighbour axis directions of the LATTICE axiom and 48 do not. The
assembly stencil is therefore a construction **on top of** the axiom's 6-NN
adjacency, and this is the exact seam where the supplied input still lives.

**T10 — the earlier reading is reproduced.** Restricting to the static rows
returns four frame labels at tick length 2 and at tick length 3, matching cycles
717–721 on their own ground.

## What this corrects

Cycle 721 recorded the expectation that at tick length beyond 2 *"the improper
half should vanish while the proper sextet survives"*, reasoning that on a
length-2 tick the complement is the identity so a chain reversal is absorbable.
The measurement says otherwise. **The improper half survives at every tick length
checked** — 2, 3, 4 and 5 — and what tick length actually controls is narrower
and different: whether a tick **translation** can stand in for a tick
**reversal** under temporal-class dropping. It can at tick length 2 and it cannot
beyond, which is why the sextet-plus-coset structure is stable while the *route*
to the coset is not. The order-12 group was never contingent on the length-2
tick; the projection that hides the orientation was.

## Derivation sketch

Each Kuhn path simplex of the 4-cube contains the full main diagonal as the chain
from first to last vertex, so every simplex of *S_a* — and therefore *S_a* itself
— carries the oriented diagonal *(a,0) → (1−a,1)*. A frame symmetry of the
assembly must carry the stencil to a stencil, hence the diagonal to a diagonal.
Inside the 48 signed axis permutations the stabilizer of an **oriented** body
diagonal has order 6 and the stabilizer of the corresponding unoriented **line**
has order 12, the extra coset being exactly the elements that reverse the
diagonal. On the tick-resolved complex the two ends of the diagonal sit at
different ticks, so reversing it demands a tick reversal, which the spatial
signed permutations alone do not supply — hence order 6. Any projection that
forgets the tick order supplies the missing reversal and lifts the group to 12.
The tick fold does this at every tick length because folding makes the two tick
endpoints of the diagonal a single slot; dropping temporal classes does it only
when the surviving tick translation happens to realise the reversal, which for a
periodic tick of length *LT* happens at *LT = 2*. Everything above is then
checked against real assembled forms rather than asserted.

## Honest boundary

- The **eight** stencils here are the Kuhn path family. That family is not the
  set of all admissible triangulations of the 4-cube; the transitivity in T2 is
  transitivity **on this family**. Whether a wider admissible family is still a
  single orbit is open and is the natural next measurement.
- The separation magnitude 2.789850e+00, the averaging cost 1.394925e+00 and the
  form scale 2.945214e+01 are **measured, not derived**. Only their exact
  relation — cost is half the separation — is structural in this note.
- The identification law T4 is verified over twelve rows at three tick lengths
  and four projections. It is exceptionless there, and it is a finite check, not
  a proof over all projections.
- The imported local pieces come from the landed compiler, which was built at
  tick length 2. T1 is the gate that makes the extension legitimate, and it is
  the gate a reader should attack first.
- The second-variation form assembled here is indefinite. Nothing in this note
  reads a spectrum or claims a definiteness property.
- The stencil itself remains supplied input, as T9 makes quantitative: 48 of its
  120 spatial edge slots are not axiom-adjacency steps.

## The next paths opened

1. **Widen the stencil family.** Enumerate admissible triangulations of the
   4-cube beyond the Kuhn path family and test whether the proper rotations still
   act with a single orbit. If they do, the frame label is an orbit count for a
   much larger input class; if they do not, the orbit decomposition itself is new
   structure to name.
2. **Attack the 48 non-adjacency slots of T9.** These are the exact slots where
   the stencil exceeds the LATTICE axiom's 6-NN adjacency. A construction that
   assembles using axiom-adjacency slots only would make the whole frame-label
   question axiom-internal.
3. **Price the orientation directly.** T8 prices full frame symmetry at half the
   stencil separation. The same quantity computed against a record-side quantity
   rather than a form distance would connect the orbit average to what the record
   registers.
4. **Follow the tick reversal.** T6 makes the improper half a tick-reversal
   coset. Emergent time enters this framework as the direction of monotone record
   accumulation, so a tick reversal is not a free relabelling — which of the two
   halves survives once the arrow is imposed is a well-posed next question.

## Runner

`scripts/physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02.py`
assembles the tick-resolved form from the landed compiler's local pieces at
(L, LT) up to (4, 3) and (3, 5), and prints twelve gate blocks A–L ending in
`TOTAL: PASS=51 FAIL=0`. Cold output and receipt are landed alongside it.

## Citations

- [Tick extension of the cubic Regge second
  variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
  — landed, unaudited. Supplies the 3+1 complex this runner resolves in tick.
- [Proper-cubic covariance
  ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md)
  — landed, unaudited. Its Kuhn-complex reading of 6 agrees with the line
  stabilizer measured in T2.
- [Direction-set covariance versus triangulation
  covariance](PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md)
  — landed, unaudited. Establishes that stabilizers of a triangulation and of its
  direction set are different invariants, which is why T2 is stated for the
  stencil orbit specifically.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the LATTICE axiom's 6-NN
  adjacency and proper cubic rotations are the symmetry class used throughout T2
  and T9.

Context without dependency: `PHYSICAL_STENCIL_DERIVED_CENTRALITY_CYCLE721_NOTE_2026-08-02`
(in flight) is the cycle whose two closing questions this note answers, and whose
tick-length expectation this note corrects;
`scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py` is the
landed compiler whose local pieces are imported.
