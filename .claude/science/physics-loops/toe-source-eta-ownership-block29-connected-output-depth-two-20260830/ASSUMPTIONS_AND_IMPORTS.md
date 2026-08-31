# Block29 assumptions and imports

## Conditional imports

1. Block23 supplies exact current-Record preparation/write factors, physical
   Locked words, transition coefficients, and Record-QND controls.
2. Block24 supplies the exact self-delimiting one-Blank append instrument,
   full STOP completion, covariance, and finite-prefix marginal identity.
3. Block26 supplies the precedent that two commuting current-presence
   projectors form four exact empty/singleton/pair direct-sum sectors.
4. Block28 supplies two conditional first-layer pair instruments on the same
   ten-block carrier with

   ```text
   q_lambda(g,h) = (1-lambda)/16 + lambda/4 * delta(g,h)
   lambda in {0, 1/2}.
   ```

   Both have uniform one-arm marginals and a common complement STOP.

## New supplied construction data

- one external first-layer invocation followed by one external future append
  on every newly written arm;
- the empty/left/right/pair routing rule;
- eight exact future Blank candidates, one for every possible first exit on
  each arm; and
- arbitrary states on the additional identity-only spectator blocks.

For a fixed first Record outcome, the two selected future-resource Blank
projectors define four commuting sectors `D_00`, `D_10`, `D_01`, and `D_11`.
They route identity, the literal left append, the literal right append, and
the tensor product of both appends.  The eight possible future rails are
present on the initial declared carrier and acted on by identity in layer one;
inserting them only after observing the first outcome would be an external
intervention rather than a cylinder.

## Exact cylinder reading

The future marginal is equality after restriction to the algebra of Records
already present after the first layer, equivalently after tracing/summing the
new future output blocks.  It is not equality of the full output state:
future Blank blocks have become Records.

For one arm the history coefficient is

```text
T(first | source) T(second | first).
```

Summing `second` gives the first coefficient in a singleton future-resource
sector.  In `D_11`, the joint coefficient is this product on both arms times
`q_lambda(g,h)`, so `q_lambda` factors unchanged through the future marginal.

The first exit-choice singleton is a new uniform one-arm turn instrument.  It
uses the Block23/24 factor grammar but is not literally the Block24 straight
append: its extra uniform four-way lateral-exit selector is supplied
downstream law data.  The connected second layer is the literal Block24
straight append.

## Representation boundary

No common-cause factorization is assumed.  A visible classical Locked cause,
an unrecorded cause, a quantum environment, and a direct joint channel are
different realizations and may not be identified by a Kraus decomposition.
In particular, requiring singleton uniformity conditional on a visible cause
would be an additional screening premise; it is not smuggled into this block.
