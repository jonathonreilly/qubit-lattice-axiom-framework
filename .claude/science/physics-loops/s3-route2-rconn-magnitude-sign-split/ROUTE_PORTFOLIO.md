# Route Portfolio

## Selected Route: Magnitude/Sign Split

Pattern: selector/chamber plus exact runner.

Score: 3/3 for claim-state movement.  It does not derive the magnitude bridge,
but it retires a separate sign ambiguity once the existing positivity bound is
allowed.

Premise set:

- exact Route-2 endpoint algebra;
- `q_T=5/6`, `s_TE=-2`;
- positivity `q_E>0`;
- scalar `R_conn=8/9`.

Output:

- `docs/QUARK_ROUTE2_RCONN_MAGNITUDE_SIGN_SPLIT_EXACT_SUPPORT_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py`
- `outputs/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.txt`

## Fan-Out Considered

| Route | Expected movement | Result |
|---|---|---|
| Derive signed bridge directly from `R_conn` | Would close the color route | Prior source-domain no-go says sign/orientation are not supplied by the color projection itself |
| Use positivity alone | Could select sign or endpoint | Positivity only gives `q_E>0`; continuum remains |
| Split magnitude from sign | Narrows the missing import | Selected and checked |
| Wrong-structure controls | Falsify accidental arithmetic | Added for `N_c=2`, denominator `5`, denominator `12` |
| Typed magnitude bridge derivation | Highest next-value target | Next campaign target after this PR |

## Synthesis

The selected route is the smallest exact movement available: it does not solve
the typed color/support bridge, but it turns the remaining bridge into a
magnitude theorem and removes a separate sign-choice premise.
