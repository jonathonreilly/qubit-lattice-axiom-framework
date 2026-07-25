# N1–N8 No-Go Discipline — Cycle 697 (L2 and L3)

L1 is a positive classification and is out of scope for this gate. L2
(position blindness) and L3 (no dimensionless readout) are negative results and
are checked here. This checklist is author-side evidence; the N1–N8 verdict is
reviewer-owned and the note self-awards none.

## N1 — Alternative route enumeration (≥5 per claim)

### Against L2 (a Record readout cannot be a nonconstant field)

| # | Route | Outcome |
|---|---|---|
| 1 | Read "content" as including the record's site, so position is content. | ATTEMPTED, fails. Qubit makes a possibility an element of the one-site algebra; Lattice says no site is privileged. Absolute position as content privileges sites. |
| 2 | Let the Admissibility rule carry the position: a record's neighborhood is part of its situation. | ATTEMPTED, fails. Admissibility determines which possibilities are *available*; the readout clause independently says the value is determined by content alone. |
| 3 | Use a collection-level readout that is not a sum of singleton weights. | RULED OUT BY PRIOR. Cycle 693's factorization theorem forces the singleton-weight form from the same three clauses. |
| 4 | Use a vector of readouts, one per site, instead of one scalar. | ATTEMPTED, fails. Each component is separately position-blind, so each component is separately constant. |
| 5 | Define the field from the record set's shape (distances, adjacency, diameter). | ATTEMPTED, fails. Shape is not content, so no such rule is a readout in the axiom's sense. |
| 6 | Take limits of readouts, or allow infinite collections. | ATTEMPTED, **live escape**. Record's additivity is stated for finite collections; a limiting construction is not excluded, but it requires a supplied limit/measure structure. Recorded as an open route, not as a closed wall. |

### Against L3 (no nonzero Record readout is dimensionless)

| # | Route | Outcome |
|---|---|---|
| 1 | Deny the duplication is admissible — the copy might violate the admissibility rule. | ATTEMPTED, fails, and this is the load-bearing step. Checked exactly in C8 at the level of full neighbor **content** conditions, not occupancy. |
| 2 | Use a scalar group with torsion, so `I = 2I` need not force `I = 0`. | ATTEMPTED, fails. `I = 2I` gives `I = 0` in any abelian group by cancellation; no torsion-freeness is used. |
| 3 | Reject "duplication-invariant" as the meaning of dimensionless; use unit-rescaling invariance. | ATTEMPTED, fails. C10 checks the rescaling reading separately and reaches the same conclusion, with a vacuous-condition negative control. |
| 4 | Supply a canonical reference inside the axioms (record count with `f = 1`), making a canonical ratio. | ATTEMPTED, **live escape and named as such**. This needs a supplied unit in the scalar group; cycle 693 already established the codomain is supplied. C11 shows the quotient works and that different admissible references give different values (`6/35` vs `3/28`). |
| 5 | Use a non-additive readout. | Out of scope by definition — such a rule is not a Record readout. This is the ratio escape, named explicitly in the note. |
| 6 | Use infinite collections. | ATTEMPTED, **live escape**, same as L2 route 6. |

## N2 — Wall independence

Two walls are named: position blindness (L2) and extensivity (L3). C9 checks
both non-implications exactly: a position-blind readout still doubles under
duplication, and a duplication-invariant ratio is still built from
position-blind ingredients. Neither follows from the other. No third wall is
claimed.

## N3 — Hidden-wall scan

Grepped the note and runner for "we assume", "by construction", "naturally",
"standard", "registered", "canonical". Hits and dispositions:

- "canonical mathematical construction" — appears only in quoted cycle 693
  text, non-load-bearing context.
- range-1 locality — **promoted to an explicit named condition** in L1, in the
  scope section, and in the residual table. It is not an axiom.
- offset-insensitivity — **promoted to an explicit named condition** in L1b and
  explicitly disclaimed as underived in the scope section.
- the supplied scalar codomain `G` and realized content set — carried from
  cycle 693 as supplied, stated in the L1 preamble.
- "proper" cubic rotations — load-bearing and cited to the Lattice axiom text;
  the runner shows dropping rotations changes the dimension 2 → 7.

## N4 — Residual matching

Cycle 693 is cited as the witness for the singleton-weight factorization. Its
residual matches exactly: 693 establishes the form of scalar readouts and
disclaims the alphabet, codomain, and product — none of which L2 or L3 relies
on. Cycle 692 is cited only for what it disclaimed (it did not classify every
dimensionless construction), which is the exact gap L3 fills. No other prior
no-go is used as a witness, so no citation needed dropping.

## N5 — Rhetoric audit

The phrase at risk is "a Record readout cannot be a field". Resolutions tested:
per-singleton (C6 kernel constancy), per-site (row equality of the induced
operator), per-configuration (constant output for every source), and
whole-lattice (the proof, which is not box-limited). The note states the
narrowed form — "a nonconstant record-sourced field is never a family of Record
readouts" — rather than the unqualified "the framework has no fields". The
phrase "no nonzero Record readout is dimensionless" is tested at both readings
of dimensionless (C7, C10) and is stated with the ratio escape attached.

## N6 — Partial-closure path scan

Two partial-closure paths were found and **both are named in the note as live
routes, not as new-axiom requirements**:

1. Supplying a unit and using the record-count readout as reference discharges
   L3's residual by convention rather than by axiom. The note says so and C11
   quantifies what remains (the reference choice changes the value).
2. A site-anchored readout is a definitional relativization, not a new axiom;
   the note names it as the single object L2 requires.

Neither is described as requiring an axiom extension. This matters because the
r=1/2 lane already reduced its bridge to "one shared convention plus a measured
constant" and preserved count-once under doubling — a structurally identical
convention-shaped discharge.

## N7 — Steelman against the author's own negatives

> The Record clause says a readout value is determined by record content alone,
> but a physical readout is always taken *somewhere*. Reading "content alone" as
> forbidding position over-reads a clause whose job was to forbid the readout
> depending on *history* or on *unrecorded* structure, not to forbid a detector
> at a site. Under the intended reading, `Phi_x` is a family of readouts indexed
> by the detector site, each of which is content-determined given the anchor, and
> L2 dissolves into a notational remark. Likewise, calling a ratio "not a
> readout" is bookkeeping: physics measures ratios, and the framework plainly
> permits forming one from two readouts it does supply, so L3 forbids nothing a
> physicist wanted.

Disposition: this steelman is strong and the note is written to survive it
rather than to defeat it. L2 is not claimed to forbid site-anchored readouts —
it is claimed to show that a site anchor is *exactly* the extra structure
required, and that it is not supplied by the current clause. L3 is not claimed
to forbid ratios — it is claimed that the reference is a second supplied datum
and that different admissible references give different numbers. Both claims
survive the steelman in the form written. Because the steelman is convincing
against the *stronger* readings, the note carries the weaker ones, and the
titles and status lines were narrowed accordingly.

## N8 — Cross-cycle echo

Structurally similar prior walls searched: cycle 692's free-scale `alpha`
(not retired; L3 explains it structurally rather than retiring it), the r=1/2
lane's count-once convention under doubling (retired by an owner-adopted shared
convention — the same mechanism named in N6 route 1), and cycle 693's supplied
codomain (not retired). One prior wall of this shape was therefore retired by a
convention-adoption mechanism, and that mechanism is explicitly carried into
this note's residual table rather than ignored.

## Outcome

No failure condition is hit at the strengths actually claimed. Two live escapes
(infinite collections; supplied reference) and two named conditions (range-1
locality; offset-insensitivity) are recorded in the note. Claim strength is
`bounded_theorem` with reviewer-owned N1–N8, not `no_go`.
