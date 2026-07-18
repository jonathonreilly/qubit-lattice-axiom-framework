# Review history — block05 (finite-range plaquette-class walk-expansion LR bound)

## Round 1 — combined adversarial lens (codex, read-only), 2026-07-18

Spec: `lens_b05_spec.md`. Output: `lens_b05_out.txt`. Verdict as
issued: no BLOCKER in the theorem; two MAJOR defects; do not ship
until repaired. The lens independently recomputed the entire geometry
table (all values confirmed, all orientations, radii 3-6), verified
the dilated reach lemma at the odd boundary, the sibling walk
convention, the coefficient/exponent bookkeeping, the μ-readout
arithmetic (−⌈d/2⌉ ≤ −d/2 route to 208eJ), the gauge regrouping
argument, and the honest scope boundaries. Dispositions:

### Major (2)

1. **Single-site subsumption sentence false as stated.** ACCEPTED —
   the lens's counterexamples are correct (a one-site region has no
   bond; relabeling onto an occupied bond duplicates a support in a
   set-indexed family or doubles the norm). Fixed by the lens's
   cheapest route: the sentence is deleted; the family is explicitly
   set-indexed with a same-support summation convention; genuinely
   single-site terms are declared outside the family; the gauge
   remark now describes electric link terms directly as bond terms on
   their own geometric bonds (no subsumption used anywhere); the
   refuted draft sentence is recorded in the N7 steelman.
2. **Runner gates weaker than their Verification descriptions.**
   ACCEPTED item by item: G2/G3 now enumerate EVERY bond and face
   orientation at both radii (cubic symmetry checked, not assumed);
   R1 adds the symbolic even/odd ceiling cases with the k = r
   boundary failure; T2 relabeled as the binomial-domination
   mechanism plus an exact partial-sum instance (the infinite-tail
   statement cited to the sibling); M4 added — a mixed-dimension
   FOUR-site face term with its own far-factor commutation and
   one-step opposite-corner arrival (the previous mixed-dim gates
   were two-site only); the count-only manifest replaced by an
   ordered label manifest (label drift fails the run); the
   Verification section now describes the N-group needles as presence
   checks, not correctness oracles.

### Minor (1)

"Two **distinct** terms are adjacent" wording fixed.

### Lens-confirmed survivals

All geometry values (independent recomputation, orientation- and
box-stable, with the note's inclusion-exclusion cross-check); the
dilated reach lemma including the odd-d boundary; the face-jump
sharpness exhibit; the chain carry-over for four-site terms (the
lens wrote out the reduction identity and confirmed no bond-only
algebra); every factor and exponent in the theorem display; the
μ-form and 208eJ readout; dimension-independence as established by
the general proof (with the honest caveat that instances support, not
replace, it — reflected in Verification); the gauge regrouping and
the Z_2 instance (up to a harmless basis convention); the d = 0
exclusion necessity (bond class is a subclass, the sibling
counterexample transfers); all non-claims.

### Post-repair state

Runner 22/0 under the ordered label manifest. Mutation battery: 14
probes, each flipping exactly the targeted gate; expected collateral
only (i06: M1/M2; i07: M2/M3).
