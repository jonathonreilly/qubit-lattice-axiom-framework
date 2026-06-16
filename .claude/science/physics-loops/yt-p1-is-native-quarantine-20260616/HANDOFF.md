# Handoff

This PR is a source-side audit-unblock repair for the YT P1 citation packet.
It does not audit, retag, or land any ledger result.

What changed:

- The note now says the old `I_S_native = 3.902` route is quarantined by the
  2026-06-16 correction and cannot provide `P1_native`.
- The restricted-packet verifier now checks current corrected BZ evidence:
  `I_v_scalar ~ 32.435`, positive uncontrolled Delta_R diagnostic, correction
  cache, and fermion-regulator cache.
- The verifier confirms the old `3.754%` native P1 central value and old
  systematic band are absent.

Verification:

- `python3 scripts/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.py`

Remaining blocker:

The positive YT P1 native lane remains open. A future PR needs a corrected
taste-normalized/full-doubler matching derivation; this PR only prevents the
known-bad native replacement from being consumed downstream.
