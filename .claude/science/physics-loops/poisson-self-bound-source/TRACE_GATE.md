# Trace Gate — poisson-self-bound-source (cycle 713)

```yaml
trace_class: direct_blocker_closure
target_claim_id: self_consistency_forces_poisson_note
target_blocker_text: "the attraction comparison uses the same negative source with operators of different sign definiteness, making the Poisson-versus-biharmonic/local/random sign discriminator convention-dependent; moreover, the measured susceptibility decays as r^(-2.805), despite the claimed Poisson-kernel interpretation. The note correctly names finite-family and linear-response limitations, but a response-kernel bridge is still missing."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Report whether the two-gate selection (box-independent binding, then far-field exponent) survives a multi-particle source, which the landed frozen-stars note already occupies for the fermionic case."
```

## What this artifact moves

The parent row's `notes_for_re_audit_if_any` sets three tasks. Cycle 710
(PR #5656) did the first two — the matched point-to-point kernel comparison
and the consistent source-sign normalization. Cycle 712 (PR #5693) did the
third for a **prescribed** source and found the parent's own diagnostic
inverted. What none of the three settled is whether the parent note's actual
subject — a *self-consistent* field — admits a source to which any far-field
test applies at all. Cycle 712's row U9 answered "not with the propagator
density" and named the escape.

This cycle takes the escape and finds the answer is yes, with a criterion the
lane did not previously have: the operator family splits on whether the
self-consistent **binding energy** has a box-independent limit, not on any
fitted decay exponent.

## What it does not move

- It does not retire the parent row. The row's headline claim is that
  self-consistency *forces* Poisson; what is shown here is a two-gate
  separation over the parent's own four-member tested family, which is not an
  exhaustiveness result over local operators.
- It does not restore the parent note's `beta` evidence, which PR #5693 showed
  is inverted under the parent's own window.
- It does not touch the continuum limit.
- The secondary finding against `FROZEN_STARS_RIGOROUS_NOTE.md` is a
  measurement on that note's own runner at its own parameters. It is reported
  as an observation for the audit lane, not as a re-audit; that row is `leaf`
  with in-degree 0, so nothing downstream depends on it.
