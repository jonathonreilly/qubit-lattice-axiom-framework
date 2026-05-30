# Source-Measure Dependent Plaquette / Gauge-Vacuum Draft Note

Status: draft-dependent impact map.  This note does not promote plaquette,
gauge-vacuum, Haar-measure, or Wilson-loop rows.

Dependency: this draft may exit draft only if the source-measure
record-intervention line in PR #2373 receives a positive audit.  Even with that
audit, the expected direct movement here is low-confidence.

## Target Surface

The target surface is the small set of plaquette/gauge-vacuum rows that mention
P1/P-cal or source/measure language.  The current inventory marks roughly two
rows as possible candidates.

This lane is probably not directly retired by PR #2373 because gauge vacuum
rows typically depend on Haar integration, character coefficients, plaquette
measure, Wilson-loop scale setting, or gauge-field dynamics rather than
record-facing source interventions.

## Conditional Movement

If PR #2373 audits clean, it can help only where the gauge row contains a
record-facing source/readout subclaim.  The following remain separate:

1. SU(3) Haar measure and character expansion;
2. plaquette expectation and beta=6 bridge;
3. Wilson-loop scale setting;
4. gauge-vacuum dynamical measure.

## Review Checklist

- Identify whether the row's P1 wording is source/readout semantics or gauge
  Haar/plaquette measure.
- Apply PR #2373 only to the former.
- Keep any Haar, character, plaquette, Wilson-loop, or scale-setting blocker
  untouched.
- Do not infer gauge-vacuum closure from finite record-intervention closure.

## Non-Claims

This draft does not derive the plaquette, Wilson loops, gauge Haar measure,
character weights, beta=6 matching, alpha_s, or any gauge-vacuum expectation.
It records that PR #2373 is at most a source/readout support bridge for this
lane.
