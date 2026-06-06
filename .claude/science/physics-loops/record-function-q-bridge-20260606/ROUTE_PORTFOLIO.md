# Route Portfolio

## Tried

1. Cite `KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05`.
   - Rejected as the primary repair because that row is currently unaudited on
     main, so it should not be treated as a retained definition edge.

2. Remove `Q` endpoint entries.
   - Not chosen because it would narrow away useful science even though the
     required finite derivation is short and exact.

3. Same-row derivation of `Q`.
   - Chosen route. The record-function runner now derives the finite power-sum
     formula first and then checks endpoints.
