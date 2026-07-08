# Handoff — matter-mass-wep

Campaign 2026-07-08. Owner: Jon. Supervisor: Claude (Fable), workhorse split
with codex workers. All four science blocks delivered; campaign paused at
the owner-conversation checkpoint per the owner's standing instruction
("stop and have the axiom conversation as soon as it's apparent").

## PRs in review order (each verifiable by its stated runner command)

1. #5061 block01 — mass observable. `python3 scripts/mass_observable_two_step_surface_2026_07_08.py` -> PASS=7 FAIL=0.
2. #5062 block02 (stacked on #5061) — inertial closure, retires the 123%
   mechanism. `python3 scripts/inertial_closure_two_step_surface_2026_07_08.py` -> PASS=8 FAIL=0.
3. #5063 block03 (stacked) — composite additivity + binding defect.
   `python3 scripts/composite_mass_additivity_binding_defect_2026_07_08.py` -> PASS=6 FAIL=0.
4. block04 (stacked) — WEP source reduction, finite-spacing boundary,
   scaling-window universality. `python3 scripts/wep_source_reduction_scaling_window_2026_07_08.py` -> PASS=6 FAIL=0.

Nothing is landed; the review lane owns landing. Every claim is bounded off
declared imports; expected first audit verdicts are audited_conditional via
the staggered-realization dependency cascade — normal bookkeeping.

## What the framework now yields on mass (plain language)

- One number per species governs everything measured: the rest gap and the
  inertial response are two readouts of one free datum through the exact
  species-independent function F(x) = (1/2) sinh(2x). The value of the
  datum is free (that freedom was already proven unremovable).
- Packets accelerate at the rate that number dictates, independent of their
  width (the 2026-04-07 failure is now formally the massless limit of the
  same formula, reproduced by a control leg).
- Free composites: rest energies and inertial responses both add exactly.
- Bound composites: inertial mass is bandwidth-dominated (binding makes a
  lattice pair HEAVIER to push while lowering its rest energy), so no
  species-blind source built from rest energy alone can give exact
  equal-fall at finite lattice spacing (exact convexity proof + a
  constructive witness pair: equal rest energies, inertial masses apart by
  47%).
- In the scaling window everything reconciles: universal free fall holds
  with derived correction exponents (all quadratic in the mass datum, plus
  a binding term), exhibited numerically at 4.1% observed vs 12.7% bound.

## The one question that decides the fork

Does "full WEP closure" mean:
(A) scaling-window universality with derived exponents — then block04's T4
    is the closure shape, the finite-spacing boundary is a lattice fact
    (true of any lattice theory with bound states), and the campaign's
    verdict is: THE FRAMEWORK YIELDS MASS, with the source-coefficient
    identification remaining a named bounded gate (as it is for G in any
    physical theory); or
(B) exact finite-spacing WEP — then the diagnosis is already written
    (block04 note + NO_GO_DISCIPLINE_CHECKLIST.md): the source would have
    to read dynamical band content, which the current axiom surface does
    not supply and the Record axiom's readout clause does not cover; the
    write-up-then-stop protocol has effectively completed its write-up and
    the axiom conversation is open.

Supervisor recommendation: reading (A). Reading (B) demands something no
lattice theory satisfies, so it would send the axioms back to the drawing
board for a failure that new axioms could not fix either — only a
continuum-exact reformulation would, which is a different program.

## Proposed repo-wide weaving (deferred to review; NOT done in-loop)

- The conditional shared-coupling template's "ratio is one" language should
  eventually point at the universal-function correction (block01 T5).
- EP-S3b's residual text could be updated to the sharpened form (source
  must target the inertial-response functional).
- Both are review-lane decisions.

## Resume

Read STATE.yaml. If owner answers (A): draft the verdict memo into the
block04 PR body / owner surface, then either close the campaign or spend
remaining budget on the named residual stretch rounds (R3 Noether
identification; unequal-mass composite gates; d=3 lift of the composite
comparator). If (B): campaign halts; the conversation artifacts are the
block04 note, the checklist, and this brief.
