# Structurally Independent Checker Return

Verdict: **PASS**, with no scientific disagreement.

```text
checker sha256: 45b508529e0f6bb9ca36147bf2861feaada8c55aeed0145f79059359fd087441
baseline:       13/13
mutations:      19/19 rejected
primary import: none
```

The checker imports only the frozen Block-208 input.  It independently derives
all 24 proper-cubic rotations, the 36 fine-label orbits, the eight dot/cross
fibers and their covariance.  It diagonalizes every depth-one/depth-two coarse
effect and constructs exact positive square roots from Lagrange spectral
projectors rather than the primary runner's Cholesky factors.

Every coarse effect has rank four.  Both independently constructed Naimark
isometries have shape `32 x 4`, recover each effect, and meet the exact rank-sum
lower bound of 32.  The checker exhausts all 64 one-shell binary patterns,
reproduces the narrow raw-label orbit obstruction, and constructs both the
eight-label one-shell and raw 36-label two-shell escapes.

It reconstructs the raw H1 source polynomial and literal actual reverse
without calling the primary Block-211 decoder.  Calibrated and score-norm
self-normalizing routes both pass for depths one/two, radii one/one-half, both
realifications, forward and reverse.  It confirms four distinct conditional
probability vectors and explicitly fences the semantic blank from a Hilbert
state or CPTP formation channel.

This is independent mathematical checking, not `review-loop`, an audit
verdict, or retained status.
