# Shapiro Static Discriminator

**Date:** 2026-04-06 (interpretation narrowed 2026-07-12 per audit-lane verdict)  
**Status:** bounded finite-model card. Within the supplied runner the `static_cone`
and `causal` field builders are algebraically identical (same spatial cone law, no
delay), so their detector phase curves coincide **by construction**; the completed
finite sweep over fixed delays `0` through `3` gives a near-flat `static_schedule`
curve that does not track the c-dependent curve. This note asserts neither an
identification of the runner's in-file `causal` comparator with the retained causal
propagating-field lane nor an evaluated zero-strength control.

## Artifact Chain

- [`scripts/shapiro_static_discriminator.py`](../scripts/shapiro_static_discriminator.py)
- [`logs/2026-04-06-shapiro-static-discriminator.txt`](../logs/2026-04-06-shapiro-static-discriminator.txt)
- This note

## Question

Within this finite runner, how do a frozen spatial-cone field and a frozen
scheduling proxy compare, on the detector-line phase response, against the
runner's in-file cone comparator?

## Measured curves

The runner prints these per-mode mean detector phase curves (three grown
families, 16 seeds each):

| Mode | c=2.0 | c=1.0 | c=0.5 | c=0.25 |
| --- | ---: | ---: | ---: | ---: |
| in-file cone comparator (`causal`) | +0.0372 | +0.0446 | +0.0569 | +0.0662 |
| static cone shape (`static_cone`) | +0.0372 | +0.0446 | +0.0569 | +0.0662 |
| static scheduling (`static_schedule`) | +0.0446 | +0.0445 | +0.0446 | +0.0450 |

## What the runner actually establishes

1. **The static-cone row equals the comparator row by construction.**
   `_static_cone_field` and `_causal_field` have identical bodies — the same
   `cone_radius = c * det_radius * max(dx, 0) / x_span` support and `strength / r`
   fill, with no temporal delay in either — and the sweep evaluates them at the
   same `c`. The exact agreement of the two rows is therefore an internal identity
   of the runner (the comparator is compared against a verbatim copy of itself),
   not an empirical demonstration that a physically distinct static field shape
   mimics a causal propagating field.

2. **The scheduling proxy does not track the c-curve.**
   `_static_schedule_field` adds a genuine fixed layer delay
   (`layer < SOURCE_LAYER + delay_layers` gate). Sampled at delays `0` through `3`
   it produces only a near-flat phase response, so on this finite model a fixed
   activation schedule does not reproduce the c-dependence of the cone comparator.
   This mismatch is the retained finite-model content of the lane.

## What this note does NOT claim

- That the runner's `causal` mode represents the retained **causal
  propagating-field lane**. The `causal` mode is an in-file spatial-cone
  construct; a one-hop retained theorem constructing this comparator from that
  lane is not supplied, so no such identification is asserted here.
- That a physically distinct static field-shape family mimics a causal
  propagating field. The static-cone/comparator agreement is an identity by
  construction (§1), not a degeneracy between distinct hypotheses.
- An evaluated exact zero-strength control. The runner's null slot is a
  `zero_ok = max(zero_ok, 0.0)` placeholder that performs no zero-strength
  propagation; it is a no-op, not an evaluated null check.
- That the detector-line phase lag is a unique causal-propagation discriminator.
  On the current packet the only genuine separation shown is against the
  fixed-schedule proxy.

## Retained finite-model boundary

- `static_cone` equals the in-file `causal` comparator exactly, by construction.
- the fixed-schedule proxy (delays `0` through `3`) is near-flat and does not
  track the c-curve.

Reinstating a unique causal-propagation discriminator, or a physical
static-shape degeneracy claim, would each require additional retained structure:
(i) a one-hop bridge theorem tying the in-file comparator to the causal
propagating-field lane, (ii) a genuinely distinct static field-shape comparator,
and (iii) an evaluated zero-strength control.

## Audit boundary (2026-07-12)

Audit verdict (`audited_conditional`, 89 transitive descendants):

> Issue: `_causal_field` and `_static_cone_field` implement the same spatial
> field law, so their exact match is an algebraic consequence of the runner
> definitions rather than an independent causal-versus-static comparison. Why
> this blocks: no cited authority or construction establishes that the runner's
> so-called causal branch represents the retained propagating-field lane. Repair
> target: supply a retained bridge deriving this causal comparator from that lane
> and verify an actual zero-strength control rather than assigning `zero_ok` to
> zero. Claim boundary until fixed: the internal equality and the sampled
> delay-0-through-3 scheduling mismatch remain valid finite-model results.
