# Handoff — poisson-self-bound-source (cycle 713)

## What landed on this branch

- `scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.py`
- `docs/POISSON_SELF_BOUND_SOURCE_EXISTS_AND_THE_FAMILY_SEPARATES_ON_BINDING_ENERGY_BOUNDED_THEOREM_NOTE_2026-07-27.md`
- `docs/CYCLE713_VALUE_NO_GO_AND_CLUSTER_CAP_GATES_2026-07-27.md`
- `logs/runner-cache/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.txt`
- this loop pack

Nothing under `docs/audit/data/`, `docs/audit/AUDIT_LEDGER.md`,
`AUDIT_QUEUE.md`, `MISSING_DERIVATION_PROMPTS.md`, or the publication
effective-status surfaces is touched. No repo-wide authority surface is woven.

## The result in one paragraph

The successor named at the close of PR #5693 is answered affirmatively. Replace
the propagator density with the density of the lowest eigenstate of the field
that density itself sources, and the self-consistent problem does have a
solution whose extent is fixed by the coupling rather than by the box. On that
construction the parent note's own four-member operator family separates, but
not on any decay exponent: unscreened and screened Poisson have both a
box-independent extent and a box-independent binding energy, biharmonic has the
extent but a binding energy that grows linearly with the box without limit, and
`local` has no single branch to compare. The mechanism is a property of the
kernels rather than of the nonlinear fixed point — with self-consistency removed
entirely and a prescribed source of fixed extent, the same split appears on
Dirichlet and on a boundary-free torus out to `N = 96`.

## What a reader should be sceptical of, in order

1. **The isolation condition is a choice.** Row R14 shows that biharmonic's
   potential *differences* across a fixed window are perfectly box-independent.
   Only the absolute binding energy diverges. Whether that disqualifies an
   operator depends on requiring that an isolated object's binding energy be a
   property of the object; that requirement is stated, not neutral. The no-go
   gate's N7 steelman forced this demotion and it is the block's weakest joint.
2. **The limits are fits.** Every box-independence statement compares an
   `a + c/M` fit against an `a + b*M` fit over six or seven lattice sizes. That
   is evidence of a limit, not a proof of one.
3. **Four operators is not all local operators.** The parent note says
   self-consistency *forces* Poisson. What is shown is a separation over the
   parent's own tested family.
4. **The composed selection sentence leans on an unmerged PR.** The second gate
   — that among the survivors only unscreened Poisson gives the Newtonian
   far-field exponent — is PR #5693's result, which is neither merged nor
   audited. Rows R0-R14 stand without it; the thesis row's final clause does not.

## Secondary finding, for the audit lane rather than for this block

Rows F1/F2 run `scripts/frontier_frozen_stars_rigorous.py` directly, at its own
parameters (`G = 0.5`, `n_particles = 8`), and add the `G = 0` control that
`docs/FROZEN_STARS_RIGOROUS_NOTE.md` never ran. Over `L = 6..16` the gravitating
width is 87-95% of the free box ground state and grows monotonically at every
step, fitting `a + b*L` with `b = 0.311` per unit `L`. The note's claim that
"Fermi stabilization is lattice-size independent" and "persists in full 3D" is
supported by its 1D probe but not by its 3D probe; the note's own "What is
needed next" section concedes the 3D width is unconverged, and its stability
test (`width < 1.5 -> COLLAPSED`) is passed by any delocalized state.

That row is `criticality: leaf`, `verdict: null`, `direct_in_degree: 0`, so
nothing downstream depends on it. This block does not re-audit it, does not
modify it, and does not touch its ledger row. Reported here so the audit lane
can decide.

## Proposed weaving, not done here

- The two-condition self-binding criterion is reusable wherever a self-gravity
  claim is made on a finite lattice. If it survives audit it belongs in the
  gravity lane's method surface rather than in this note alone.
- `docs/MATTER_SELF_FOCUSING_NOTE.md` and
  `docs/POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md` both
  build self-fields from a propagated amplitude density and both impose `1/r`
  by hand. Neither is touched here; both would be re-testable under this gate.

## Exact next action

Repeat both conditions for a multi-particle source. The landed frozen-stars
runner already implements the fermionic Hartree loop; replacing its hand-imposed
`-G sum(rho/r)` with a solve of `Op phi = rho` over the operator family, and
adding the binding-energy condition to its width-only test, is a direct
successor that reuses landed code and would settle whether Pauli pressure
changes the separation.

## Inference audit (step 11)

`scripts/inference_audit_lint.py` from the unmerged branch
`methodology/inference-audit-20260726` (PR #5652).

| Target | Result |
|---|---|
| the runner | clean |
| the deliverable note | one `DIRECTION` finding — a sentence describing the parent note's own conclusion read as an unbacked assertion of this note's. Fixed by quoting the parent note's claim verbatim instead of paraphrasing it with an assertion verb. Clean on re-run. |
| the gates document | one `LEDGER` finding — "no claim ledger found". **Justified, not fixed.** That document is a process record (V1-V5, N1-N8, cluster-cap), not a claim note; it asserts no physics and adding a claim ledger to it would manufacture claim rows where there are no claims. The physics claims all live in the deliverable note, which carries the ledger and passes. |

Review findings and their resolution are in `REVIEW_HISTORY.md`.
