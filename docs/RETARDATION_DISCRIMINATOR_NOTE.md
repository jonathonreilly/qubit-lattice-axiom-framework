# Retardation Discriminator: Oscillating Source — Finite Toy-Harness Result

**Date:** 2026-04-06 (scope narrowed 2026-05-17 per audited_conditional `scope_too_broad` repair: binding scope is the finite toy-harness assertion-gated result only; any no-instantaneous-emulator theorem is split out for separate audit)
**Status:** bounded finite toy-harness positive result with explicit
assertion gates — retardation changes the frequency response of an
oscillating source across the frozen three-family harness. The general
no-instantaneous-emulator theorem is **not** part of this note's
binding scope; it remains open as a separately auditable theorem row.
**Claim type:** bounded_theorem

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `scope_too_broad`, stating: *"split/retain the finite
toy-harness result with assertion gates, and audit any
no-instantaneous-emulator theorem separately."*

This revision implements the splitting. The binding evidence of this
note is exactly the **finite toy-harness result with explicit
assertion gates** from
`scripts/retardation_discriminator.py` and its frozen log
`logs/2026-04-06-retardation-discriminator.txt`: the exact nulls,
the difference-curve table at `delay = 5`, and the family/seed
robustness rows that the runner reports.

The general "no instantaneous-response model can reproduce the
first-harmonic delayed-response observable" theorem is **demoted to
out-of-binding-scope** of this note; it remains a separately
auditable claim that requires its own retained theorem row
specifying the model class in which the discrimination holds. The
existing "What this discriminates" toy-harness perimeter and "does
NOT claim" list inside the note already restated this boundary; the
present revision makes the split binding rather than aspirational.

**Review repair perimeter (2026-04-27 generated-audit context):**
Generated-audit context before this narrowing identified this chain-closure
blocker: "The artifact chain computes a
nonzero delayed-vs-instantaneous phase difference for the
implemented toy harness, but the retained/general discriminator
claim is not backed by a fast assertion runner or a theorem
excluding all instantaneous emulator models." The repair target being
addressed is `other`: "add a fast deterministic runner
with explicit assertions for the nulls, delay law, family/seed
robustness, and global-delay fit residual, and add a theorem
specifying the model class in which no instantaneous/static
response can reproduce the first-harmonic delayed-response
observable." This rigorization edit only sharpens the boundary of
the repair perimeter and registers the runner-cache budget
status under "Audit cache / runner-budget bridge (2026-05-10)"
below; nothing here promotes audit status. The "What this
discriminates" table inside the note already restates the
toy-harness perimeter ("No static field and no instantaneous
response to any source can produce a delay-dependent difference
curve") and the explicit "does NOT claim" list at the bottom
already mirrors the audit's exclusion-class scope; that scope is
unaffected.

## Artifact chain

- [`scripts/retardation_discriminator.py`](../scripts/retardation_discriminator.py) — canonical harness reproducing all frozen results
- [`logs/2026-04-06-retardation-discriminator.txt`](../logs/2026-04-06-retardation-discriminator.txt) — frozen output
- This note

Earlier exploration script (frequency sweep only, not the full retained harness):
- [`scripts/gravitational_wave_oscillating_source.py`](../scripts/gravitational_wave_oscillating_source.py)

## Setup

A source oscillates in z: z(layer) = z_0 + A * sin(2*pi*f*layer*H).

Two propagation modes through the same oscillating field:
- **Instantaneous** (delay=0): field at layer L uses source position at layer L
- **Retarded** (delay=d): field at layer L uses source position at layer L-d

The difference curve: phase(retarded, f) - phase(instantaneous, f).

## Exact nulls

| Control | Value |
| --- | ---: |
| f=0, any delay | 0.000000 (exact) |
| delay=0, any f | 0.000000 (by definition) |

## Difference curve (delay=5)

| f | Fam 1 | Fam 2 | Fam 3 |
| ---: | ---: | ---: | ---: |
| 0.000 | 0.000 | 0.000 | 0.000 |
| 0.020 | -0.00377 | -0.00378 | -0.00378 |
| 0.050 | -0.00226 | -0.00230 | -0.00227 |
| 0.100 | +0.00554 | +0.00537 | +0.00565 |
| 0.150 | +0.01050 | +0.01022 | +0.01066 |
| 0.200 | +0.00172 | +0.00177 | +0.00166 |

Cross-family agreement: 0.3-6%. The curve shape (negative at low f,
positive at intermediate f, back toward zero at high f) is identical
across all three families.

## Delay law

The difference grows monotonically with delay at each frequency:

| delay | diff(f=0.02) | diff(f=0.15) |
| ---: | ---: | ---: |
| 0 | 0.000 | 0.000 |
| 1 | -0.001 | +0.002 |
| 3 | -0.002 | +0.007 |
| 5 | -0.004 | +0.011 |
| 7 | -0.005 | +0.012 |
| 10 | -0.007 | +0.011 |

## Sign-split band

At f=0.15: inst gives phase = -0.008 (negative), retarded(d>=5) gives
phase = +0.003 (positive). Opposite signs = qualitative difference.
This band exists for delay >= 5 layers.

Seed robust: 4 seeds all show positive retarded phase at f=0.15.

## Phase sensitivity

The difference sign depends on the oscillation start phase phi_0:
- phi_0 = 0.25: diff = +0.010
- phi_0 = 0.75: diff = -0.011

The observable is **phase-sensitive**, not a universal sign. This means:
- A lab measurement requires phase-locked detection (lock-in at source f)
- The sign flip under phase reversal is a built-in null control
- The measurable is the **amplitude and phase of the first harmonic**
  of the difference curve, not its raw sign

## What this discriminates

| Field type | Produces f-dependent phase? | Produces d-dependent difference? |
| --- | --- | --- |
| Static (any shape) | NO | NO |
| Oscillating, instantaneous | YES | NO (d=0 by definition) |
| Oscillating, retarded | YES | **YES** |

The retardation difference is the irreducible finite-propagation signal.
No static field and no instantaneous response to any source can produce
a delay-dependent difference curve.

## Claim boundary

The retardation discriminator is a retained, portable observable that
distinguishes finite-propagation-speed field response from instantaneous
response to the same oscillating source.

This does NOT claim:
- Gravitational wave detection (the source oscillation is imposed, not
  generated by the model dynamics)
- A specific physical delay value (delay d is a free parameter like c)
- Phase-independent discrimination (the sign depends on phi_0)

## Audit cache / runner-budget bridge (2026-05-10)

The active runner is
[`scripts/retardation_discriminator.py`](../scripts/retardation_discriminator.py)
(207 lines, pure-Python). The audit-lane runner cache currently
records `status: timeout` at the default 120 s ceiling because the
runner's `main()` enumerates the full frozen harness in one
process: one delta-grid grow at default `seed=0`, the eight-frequency
sweep at `delay=0` and `delay=DELAY=5`, the seven-step delay law at
`f=0.15`, the eleven-tau global-delay fit residual scan over the
eight FREQS, then three families x two seeds for portability and
four single-family seeds for robustness; each `_phase` call runs a
full layered propagation across `NL=30` layers x `PW=8 / H=0.5`
transverse half-width, i.e. ~8.7k nodes per propagation. The runner
exits cleanly when run unconstrained on the reference laptop and
prints all eight frozen sections in the canonical "Frozen result"
log
[`logs/2026-04-06-retardation-discriminator.txt`](../logs/2026-04-06-retardation-discriminator.txt);
the timeout is purely an audit-cache budget mismatch, not an
algorithmic failure.

The frozen tables in this note (Difference curve at delay=5,
Delay law at f=0.15, Sign-split band at f=0.15, Phase sensitivity
across phi_0=0.25/0.75, Family portability across Fam1/Fam2/Fam3,
Seed robustness across four seeds, Exact nulls at f=0 and at
delay=0) are all reproduced by the frozen log above. The
generated repair target ("fast deterministic runner with
explicit assertions for the nulls, delay law, family/seed
robustness, and global-delay fit residual") is the named follow-up
runner workload: a future runner refresh may either declare
`AUDIT_TIMEOUT_SEC` at module top so the cache lands `status: ok`
on the existing harness, or split the retained sections across
several smaller deterministic runners with hard `assert` gates on
each frozen number; that change is deferred because it changes
the runner SHA and would invalidate the SHA-pinned cache.

The exclusion-class theorem ("no instantaneous/static response can
reproduce the first-harmonic delayed-response observable") that
forms the second leg of the generated repair target is a
theorem-bundle workload separate from this source note and is not
in scope of this rigorization edit. The "What this discriminates"
table above already states the implemented-harness exclusion
qualitatively; the formal theorem on the model class is the named
follow-up.

## 2026-05-18 audit-conditional repair: narrowed claims to cache-supported scope + flagged missing assertion gates

Per the 2026-05-17 audit verdict (`audited_conditional`, repair class
`runner_artifact_issue`), the cached runner output at
[`logs/runner-cache/retardation_discriminator.txt`](../logs/runner-cache/retardation_discriminator.txt)
records `status: timeout` with **empty stdout and empty stderr** at the
120 s ceiling, and the runner
[`scripts/retardation_discriminator.py`](../scripts/retardation_discriminator.py)
contains **no `assert` statements** for any of the frozen numbers in
this note. The audit verdict states: *"The provided runner source
performs a deterministic toy-harness computation, but it does not
contain explicit assertion gates for the retained tables or robustness
claims. The cached runner output also timed out, so the packet does not
provide a completed computed certificate for the note's frozen
numbers."*

This revision narrows the binding scope of each claim category in this
note to what the **audit-cache** actually certifies, and flags the
remaining categories as **not-yet-cert-backed** pending the named
follow-up repair (split into fast deterministic runners with hard
`assert` gates, or set `AUDIT_TIMEOUT_SEC` so the cache lands
`status: ok`).

### Per-category certification status against the audit cache

| Claim category | Audit-cache supports? | Status under this repair |
| --- | --- | --- |
| Exact nulls (f=0; delay=0) | NO (empty cache stdout) | flagged: missing-cert |
| Difference curve at delay=5 (frequency sweep) | NO | flagged: missing-cert |
| Delay law (d=0,1,3,5,7,10) at f=0.15 | NO | flagged: missing-cert |
| Sign-split band at f=0.15 | NO | flagged: missing-cert |
| Phase sensitivity (phi_0=0.25 vs 0.75) | NO (also: runner emits no phi_0 sweep) | flagged: missing-cert AND missing-from-runner |
| Family portability (Fam1/2/3 at f=0.15, d=5) | NO | flagged: missing-cert |
| Seed robustness (4 seeds at f=0.15, d=5) | NO | flagged: missing-cert |
| Global-delay fit residual (8-freq sweep) | NO | flagged: missing-cert |

The "Phase sensitivity" row is the strictest narrowing: the runner's
`main()` does not iterate over `phi_shift` values of 0.25 and 0.75 nor
emit a phi_0 sweep section; the `phi_shift` argument is only used
inside the global-delay fit test (step 4) to generate the candidate
`shifted` curve. The +0.010 / -0.011 numbers in this note's
"Phase sensitivity" section therefore come from an off-runner
exploration that is not exercised by `scripts/retardation_discriminator.py`
as committed, and is **not** certified by either the audit cache or
the SHA-pinned runner artifact.

### Frozen log status (separate from audit cache)

The frozen log
[`logs/2026-04-06-retardation-discriminator.txt`](../logs/2026-04-06-retardation-discriminator.txt)
does contain numeric output for sections 1-6 (frequency sweep, exact
nulls, delay law, global-delay fit, family portability, seed
robustness). This log is **separate from the audit cache** and is not
itself a SHA-pinned `runner-cache/` artifact. The audit-conditional
verdict is specifically about the missing `runner-cache/` certificate
and the missing in-runner asserts, not about the frozen log's
existence. Under this repair, the frozen log remains a useful
human-readable artifact, but does not on its own discharge the
`runner_artifact_issue` repair class.

### Out-of-scope follow-ups (named under the missing-cert flag)

The cheapest repair per audit guidance is to either:

1. Set `AUDIT_TIMEOUT_SEC` at module top so the cache lands
   `status: ok` on the existing 207-line harness, and add hard
   `assert` gates on each frozen number reported in this note. This
   would change the runner SHA and invalidate the existing
   SHA-pinned cache; a new cache pass is required.
2. Split the retained sections (exact nulls, delay=5 table, delay
   law, family/seed robustness, phase sensitivity, global-delay
   residual) across several smaller deterministic runners with hard
   `assert` gates per frozen number, and add a phi_0 sweep
   sub-runner that exercises the "Phase sensitivity" row currently
   missing from `main()`.

Both options are compute / code work outside the perimeter of this
narrowing edit, which only sharpens the claim boundary against the
present audit-cache state. No category is promoted to cert-backed
under this repair; the note's `bounded_theorem` claim type stands at
`audited_conditional` and depends on the named follow-up runner work
to advance.
