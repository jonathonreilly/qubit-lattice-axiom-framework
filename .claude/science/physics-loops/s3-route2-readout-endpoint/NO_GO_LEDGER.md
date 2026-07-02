# No-Go Ledger

| Route | Boundary | Evidence |
|---|---|---|
| Scalar `+8/9` only | Wrong Route-2 sign and no typed landing edge | block22 runner |
| Scalar `-8/9` only | Sign is present but still untyped | block22 runner |
| Physical selector only | Does not identify a Route-2 center endpoint ratio | block22 runner |
| T-side sign only | Does not supply E-center magnitude | block22 runner |
| Center slot only | Slot existence is not a value | block22 runner |
| Wrong signed typed bridge | Computes a different E-center entry | block22 runner |

This ledger is narrow: it prunes weaker repairs, while leaving a future typed
readout landing theorem open.
