# No-Go Ledger

## Determinant-only B4 transport

Status: exact route pruning.

Let `sig(C alpha_bare^a u_0^b) = (a, b)` with `C` independent of
`alpha_bare` and `u_0`. The determinant side has signature `(0, 16)`.
Every determinant-only finite product, power, or quotient has alpha exponent
`0`. The target `alpha_LM^16` has signature `(16, -16)`.

Therefore the determinant-only route cannot be B4 closure. The exact missing
multiplier relative to `u_0^16` is
`alpha_bare^16 u_0^(-32) = alpha_s^16`.

Scope: this does not rule out non-determinant attachment-observable routes.
