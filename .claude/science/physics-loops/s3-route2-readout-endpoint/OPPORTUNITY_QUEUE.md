# Opportunity Queue

1. **Positive typed readout landing theorem**
   - Target: one of the three equivalent Route-2 readout landing edges named
     in the block22 note.
   - Expected output: exact support theorem or sharp obstruction.

2. **Two-edge scalarization/typecast split**
   - Target: separate `R_conn -> scalar_signed_minus_8_9` from
     `scalar_signed_minus_8_9 -> route2_center_TE_minus_8_9`.
   - Expected output: identify which half is already present and which half is
     truly new.

3. **Physical selector route**
   - Target: test whether a physical connected-trace selector can be typed
     into the Route-2 center ratio without importing endpoint data.
   - Expected output: conditional support or separate no-go.

4. **Direct E-channel source functional**
   - Target: bypass `R_conn` and compute a Route-2 E-center readout node from
     E-channel source structure.
   - Expected output: exact theorem or falsifier.

Recommended next `/goal`: **positive typed readout landing theorem**. Forbid
endpoint target values as proof inputs and require the output to land in one
of the three Route-2 readout nodes.
