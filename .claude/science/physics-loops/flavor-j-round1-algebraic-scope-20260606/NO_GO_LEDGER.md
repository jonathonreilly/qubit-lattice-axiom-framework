# No-Go Ledger

## Static J_cs Selects det_C

Result: no-go within this finite packet.

Reason:

- `exp(theta J_cs)` is an `SO(2)` rotation on the real doublet plane.
- The rotation preserves the Hilbert-Schmidt metric block `6I`.
- The determinant is one, so the static structure is measure-neutral.
- `J_cs` also commutes with the tested Hermitian circulant family, so it is
  operator-silent for this packet.

## Gamma_chi Equals J_cs

Result: no-go within this finite packet.

Reason: `Gamma_chi` is a real involution built from the all-ones matrix; `J_cs`
is anti-Hermitian and squares to `-P_doublet`.
