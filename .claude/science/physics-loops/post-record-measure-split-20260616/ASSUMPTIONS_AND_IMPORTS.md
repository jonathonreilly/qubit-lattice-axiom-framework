# Assumptions And Imports

## Allowed Inputs

- Finite carrier `X` is supplied.
- Rational nonnegative weights `w_x` are supplied on `X`.
- The total weight is positive.
- Exact rational arithmetic is allowed for the runner certificate.

## Explicitly Not Supplied By The Lemma

- A Record-native derivation of the carrier.
- A Record-native derivation of the weights.
- A physical prior, Born rule, selector rule, production mechanism, clock, rate,
  or stable-setting selection.
- Audit verdicts or audit data.

## Import Movement

The PR retires the row-shape import that made one row carry both a meta
subdivision and theorem content. It does not retire the deeper carrier/weight
bridge import.
