# Poisson Self-Gravity Born Audit Note

**Date:** 2026-04-05  
**Status:** bounded - bounded or caveated result note
Poisson-like backreaction loop

**Status authority and audit hygiene (2026-05-10):**
The audit lane has classified this note `audited_conditional` (verdict
2026-05-10). The zero-coupling exact reduction (`epsilon = 0`) and the
frozen-snapshot Born check are sound and survive to machine precision.
The audit-conditional perimeter is on the nonzero-coupling row, where
the runner reports `stepConv = False` and `endConv = False` at
`max_iters = 6`. The supplied runner therefore provides a
finite-six-iteration capped diagnostic, not a converged-loop theorem,
and the unconverged-return code path uses amplitudes propagated before
the last relaxation. Read all "end-to-end Born drift" content in this
note as a capped-iteration diagnostic only; the nonzero-coupling row
is not a converged full nonlinear-loop result. This rigorization edit
makes the conditional perimeter explicit; nothing here promotes
audit_status.

## Artifact chain

- [`scripts/poisson_self_gravity_born_audit.py`](../scripts/poisson_self_gravity_born_audit.py)
- [`logs/runner-cache/poisson_self_gravity_born_audit.txt`](../logs/runner-cache/poisson_self_gravity_born_audit.txt)

## Question

Does the iterated Poisson-like self-gravity loop preserve Born only at the
level of each frozen propagation step, or also end-to-end through the full
loop?

This audit is intentionally narrow:

- one exact 3D lattice family at `h = 0.25`
- one three-slit source set on the input layer
- one screened Poisson-like backreaction loop
- one exact `epsilon = 0` reduction check
- one step-local Born check on a frozen loop snapshot
- one end-to-end Born check through the full iterated loop

## What Born means here

The audit separates two distinct questions:

1. **Step-local Born** (bounded retained claim of this note)
   - freeze the converged field snapshot
   - test the usual three-slit Sorkin `I3/P` on that fixed field

2. **End-to-end Born** (diagnostic-only, see split section below)
   - run the iterated nonlinear loop separately for `a`, `b`, `c`, `ab`,
     `ac`, `bc`, and `abc`
   - read the detector `I3/P` from the loop outputs

That distinction matters because the outer map is nonlinear even if each fixed
field propagation step is linear. As of the 2026-05-18 audit-conditional
repair, only the step-local row is retained as a bounded result; the
end-to-end row is explicitly demoted to a finite-six-iteration diagnostic.

## Frozen result (bounded retained: step-local Born only)

Representative retained row:

- `epsilon = 0.05`
- source strength `s = 0.004`

Reduction check:

- exact `epsilon = 0` reduction survives exactly

Bounded retained Born audit row (step-local column only):

| `epsilon` | source strength | step-local Born | step converged |
| --- | ---: | ---: | ---: |
| `0.05` | `0.0040` | `8.834e-16` | `False` |

The step-local column is the bounded retained reading: the frozen
converged field snapshot is Born-clean to machine precision. `stepConv =
False` here means the outer relaxation has not converged at
`max_iters = 6`, but the step-local Born value `8.834e-16` is a
direct numerical evaluation on the returned snapshot and does not
require the outer loop to be converged to be machine-clean.

## Diagnostic-only finite-six-iteration result (end-to-end Born)

The end-to-end row below is **not** a retained bounded theorem. Per the
2026-05-17 audit verdict, the nonzero-coupling end-to-end Born row does
not converge at `max_iters = 6`, and the unconverged-return code path
reads final detector amplitudes from the pre-last-relaxation propagated
amplitudes rather than recomputing them from the returned field. The
row is preserved here strictly as a diagnostic for the audit-conditional
repair record.

Finite-six-iteration diagnostic row (DIAGNOSTIC ONLY, not retained):

| `epsilon` | source strength | end-to-end Born (diagnostic, `max_iters = 6`) | end converged |
| --- | ---: | ---: | ---: |
| `0.05` | `0.0040` | `6.830e-05` | `False` |

The `6.830e-05` value is what the iterated loop returns after six
iterations, with detector amplitudes read from the pre-last-relaxation
code path. It is **not** a converged-loop observable and does not load-
bear any Born-drift theorem.

## Safe read (bounded retained scope)

The strict bounded retained conclusion is:

- the frozen field snapshot remains Born-clean to machine precision
  (step-local Born = `8.834e-16` on the representative row)
- the `epsilon = 0` reduction survives exactly

The finite-six-iteration end-to-end diagnostic above is **not** part of
the retained reading. It does not support a "full iterated loop is
not Born-clean end-to-end" claim at the bounded theorem tier; that
would require a converged seven-subset loop with recomputed-from-field
amplitudes, which is queued as out-of-scope follow-up.

## Honest limitation

This is a narrow audit, not a universal theorem.

- it uses one exact lattice family
- it uses one representative nonzero coupling row
- bounded retention is now scoped to the step-local Born and exact-
  reduction rows; the end-to-end row is diagnostic-only

## Branch verdict (post-2026-05-18 repair)

Treat this as:

- **per-step / frozen-snapshot Born survives** (bounded retained)
- **exact `epsilon = 0` reduction** (bounded retained)
- **end-to-end Born finite-six-iteration value** (diagnostic only;
  not a converged-loop observable, no bounded theorem claim)

So the retained control on step-local Born stays useful. Whether the
iterated backreaction map preserves Born as a full nonlinear evolution
is an open question on this audit, not a closed bounded reading.

The end-to-end finite-six-iteration value is bounded by the runner's
`max_iters = 6` cap. Both `stepConv` and `endConv` are `False` on the
cached run, and the runner's unconverged-return path reads amplitudes
from the pre-last-relaxation code path. A converged seven-subset loop
with recomputed-from-returned-fields amplitudes is queued as out-of-
scope follow-up before any end-to-end Born statement can promote
beyond diagnostic.

## Cited Lane sibling status (audit-explicit)

This audit note has no audit-graph dependencies (`deps = []`); it is a
narrow numerical audit on its own runner. The cited Lane siblings and
their current ledger statuses are:

| Sibling row | `audit_status` | `effective_status` | `claim_type` |
|---|---|---|---|
| [`POISSON_SELF_GRAVITY_LOOP_NOTE`](POISSON_SELF_GRAVITY_LOOP_NOTE.md) | audited_conditional | audited_conditional | bounded_theorem |
| `poisson_self_gravity_loop_v3_note` | audited_conditional | audited_conditional | bounded_theorem |
| `poisson_self_gravity_mechanism_note` | unaudited | unaudited | bounded_theorem |
| `gate_b_poisson_self_gravity_note` | audited_clean | retained_no_go | no_go |

The retained-no-go sibling (`gate_b_poisson_self_gravity_note`) is the
load-bearing closure on the broader Poisson-like self-gravity branch.
This audit's bounded reading is consistent with that no-go: the
zero-coupling reduction is exact (consistent with linearity in the
limit), the frozen-snapshot step-local Born is machine-clean (consistent
with each propagation step being linear), and the end-to-end Born
deviates at finite coupling (consistent with the iterated nonlinear
map not preserving Born as a full evolution). No audit-graph cycle is
introduced by these cite-only references.

## Audit-aware repair path

Per `audit_ledger.json`, `notes_for_re_audit_if_any` for
`poisson_self_gravity_born_audit_note`:

> runner_artifact_issue: cheapest repair is to make the runner enforce
> convergence for all seven slit subsets and recompute final amplitudes
> from the returned field, or split out a separate finite-six-iteration
> diagnostic claim.

Two routes match this audit-stated repair path:

1. **Enforced-convergence runner.** Lift `max_iters` and add a runtime
   assertion that every slit subset (`a`, `b`, `c`, `ab`, `ac`, `bc`,
   `abc`) reaches `stepConv = True` and `endConv = True` before the
   detector probabilities are read. Then recompute final detector
   amplitudes from the returned field rather than from the pre-last-
   relaxation propagated amplitudes. This would let the "end-to-end
   Born drift at nonzero coupling" reading promote from a
   capped-iteration diagnostic to a converged-loop theorem.
2. **Scope split.** Keep this note as a finite-six-iteration diagnostic
   and move any converged-loop Born statement to a separate note that
   ships a runner with hard-bar PASS assertions on convergence (compare
   the `--quick` mode and five hard-bar pattern in the sibling
   `poisson_self_gravity_loop` runner).

Neither route is attempted in this rigorization edit; both are open.

## 2026-05-18 audit-conditional repair: split end-to-end Born claim to finite-six-iteration diagnostic

Per the 2026-05-17 audit verdict, the nonzero-coupling end-to-end row does
not converge and reads amplitudes from the pre-last-relaxation code path.
Per the audit's offered repair option, this revision splits the bounded
end-to-end Born claim into an explicit finite-six-iteration diagnostic-only
result. A converged seven-subset loop with recomputed-from-returned-fields
amplitudes is queued as out-of-scope follow-up.

The bounded retained reading is now scoped to the step-local Born and the
exact `epsilon = 0` reduction. The end-to-end Born row at nonzero coupling
is preserved in the "Diagnostic-only finite-six-iteration result" section
above as a diagnostic and explicitly does not load-bear any bounded
theorem.
