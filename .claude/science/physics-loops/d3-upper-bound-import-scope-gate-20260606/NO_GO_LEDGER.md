# No-Go Ledger

## Atomic Weak Upper Bound Alone

Route: use atomic stability alone to select `d = 3` from the current
lower-bound packet.

Result: pruned. The weaker atomic-stability import gives `d <= 4`, so
`{3,4,5} intersect {d : d <= 4} = {3,4}`. It is compatible with `d = 3` but
does not select it by itself.

## Framework-Internal Upper Bound Claimed From Wrapper

Route: treat the named-import wrapper as if it were a framework-internal
derivation.

Result: pruned. The wrapper explicitly says it is a named non-derivation import
and does not re-derive Bertrand's theorem, atomic stability, or a framework
dimension theorem.
