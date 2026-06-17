# No-Go Ledger

- This block cannot certify current Delta_R precision. The 2026-06-16 correction leaves the P1 Delta_R precision lane uncontrolled.
- The SM-RGE backward ratio cannot be used as a direct equality check against `Ward * (1 + Delta_R)`; the runner itself shows the quantities differ by an order-one factor and live in different matching pieces.
- Removing `FAILED: 0` from the cache is only runner hygiene. It is not scientific evidence for retained status.
