# Supplied scalar-curvature diagnostics for the EWSB-selection question

**Date:** 2026-05-10; correction 2026-10-23
**Type:** open_gate
**Status:** conditional mathematical diagnostics; physical selection and matching unresolved
**Primary runner:** `scripts/cl3_higgs_mass_s4b_ewsb_selection_2026_05_10_s4bewsb.py`

## Current boundary

No physical S4a support follows from the finite trace identity in the
[corrected parent](HIGGS_MASS_S4_BORN_EXTENSION_BOUNDED_NOTE_2026-05-10_higgsS4.md).
For supplied finite rho and O, Tr(rho O) is an expectation; that identity does
not identify a physical Higgs observable, select a state or vacuum, or equate
an expectation with a particle mass. The former M1.5 causal interpretation is
withdrawn. A difference between two supplied mass-labelled numbers does not
identify a mean-field, state, operator or gap-correction error.

This note preserves a diagnostic calculation with supplied parameters. It does
not establish that the chosen numerical evaluation point is a physical vacuum
location. Neither S4a nor S4b-loc is discharged here. Splitting a question into
location and operator choices is bookkeeping, not a smaller established physical
residual. The historical claims that S4/S7 uniquely locate the obstruction,
that the Wilson chain is thereby vindicated, or that only S4b-op/S7 remain open
are withdrawn. Physical state/operator construction and matching remain tasks,
not impossibility theorems proved by these examples.

## Supplied inputs and arithmetic

The runner retains the original supplied values and formulas:

- P=0.5934, u=P^(1/4), alpha_bare=1/(4 pi), alpha_LM=alpha_bare/u;
- M=1.221e19, c=(7/8)^(1/4), v=M c alpha_LM^16, N=16, L=4u²;
- V(m)=-(N/2) log(m²+L), with the sampled evaluation point m=v/M;
- the signed diagnostic V''(m)v²/N and the absolute-value readout
  sqrt(|V''(m)|/N) v;
- historical comparison values 246.22, 125.25, 0.1179, 127.95 and 172.69,
  and supplied comparison outputs 0.1181, 127.67 and 172.57.

These are supplied model/scale conventions and comparison data. This runner
does not derive their physical provenance, UV scale, taste count, coupling
normalization, empirical calibration or continuum applicability. Using v as an
evaluation point does not prove it is a minimum. The comparison values are
used in discrepancy checks, so those checks are empirical-input-dependent
arithmetic, not independent physical predictions. No common-input uncertainty
analysis is supplied to attribute a discrepancy to a particular step.

## Exact supplied-function controls

For N,L>0 and real m, direct differentiation gives

```text
V'(m)  = -N m/(m²+L),
V''(m) = -N (L-m²)/(m²+L)²,
V''(0) = -N/L.
```

Thus V'(m)<0 for m>0. The origin is a local maximum, not a minimum or a
one-dimensional saddle; this supplied function has no finite local minimum.
This statement concerns this function only, not every physical effective
potential. The original note's second-derivative factor of two was a
transcription error; the original runner's derivative function was correct.

Put x=m²/L. Then

```text
V''(m)/V''(0) = (1-x)/(1+x)²,
1 - V''(m)/V''(0) = (3x+x²)/(1+x)² = 3x + O(x²).
3x - (3x+x²)/(1+x)² = x²(5+3x)/(1+x)² > 0  for x>0.
```

The linear term has coefficient 3, not the legacy 2x proxy. The symbolic runner
checks differentiation and these exact rational identities, including a strictly
positive change at x=10^-34. Positive denominators and numerators establish the
stated signs. For 0<x<1 the curvature remains negative; none of this identifies
a physical mass or vacuum.

The original binary64 calculation rounds the tiny difference at m=v/M to zero.
It cannot certify a 10^-34 or 10^-30 physical/numerical error bound. Old B1.3.d/e
are retained as explicitly **unscored historical diagnostics**, with their
original expressions and thresholds. Their zero result is not an analytical
precision certificate. The old 2x value is similarly retained unscored for
recovery, not asserted as the expansion.

## What the remaining checks cover

The other numerical expressions, tolerances, seven positive sample points and
comparison ratios are preserved. They check supplied arithmetic: signs,
reconstruction of 1/(2u), sampled derivative values, and the sizes of listed
discrepancies. They do not establish retained authority or a physical cause.
The sample sign checks are distinct from the elementary derivative argument
above. No universal rank or operator-domain conclusion follows from assigning
Q_dim=2; old B1.2.a is unscored. The current runner does not construct or compare
a physical charge operator and Higgs-mass operator.

All literal-True documentary assertions are unscored and identified by their
old check IDs. In particular B1.6.f is not a proof of a narrowed residual and
B1.7.d is not a causal control. Numerical B1.7.c still computes the same ratio,
but its label no longer locates an obstruction. Source-boundary checks read this
note and the corrected parent; their results are printed separately from the
mathematical checks and do not prove the prose scientifically.

## Recovery and unresolved scope

Complete former note, runner and cache are preserved under
`archive/notes/review_feedback/pr9848-higgs-s4b-2026-10-23/` as `.txt` snapshots,
and at Git `d8198c54e4233bb57e1434f7de49f6a804703d9e` under their original paths.
The original arguments, quotes, comparison tables, failed interpretations,
physical-chain assumptions and proposed residual accounting remain recoverable.
They are historical proposals, not current proof. The old helper's literal
assertions were not scientific evidence even when its cache printed PASS.

Historical provenance (not inherited authority for the present supplied model):

- [Original Higgs construction](HIGGS_MASS_FROM_AXIOM_NOTE.md)
- [Historical EWSB pattern](EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md)
- [Historical prediction chain](COMPLETE_PREDICTION_CHAIN_2026_04_15.md)
- [Original matching question](LATTICE_PHYSICAL_MATCHING_THEOREM_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_match.md)

Their other physical/retained-chain claims are unvalidated by this repair.
A physical post-EWSB state, selected observable, potential, scale matching and
uncertainty budget would require separate derivations and independent checks.
No new framework premise, retained status or global no-go is introduced here.

Run `python3 scripts/cl3_higgs_mass_s4b_ewsb_selection_2026_05_10_s4bewsb.py`.
The default run uses the declared 120-second cap for receipt capture. Any failed
mathematical or source-boundary check exits nonzero. An unscored historical
assertion is not counted as PASS or FAIL; the explicit exclusion is part of the
current scope, with full source recovery above.
