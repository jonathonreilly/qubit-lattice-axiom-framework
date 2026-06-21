# Summary

Adds block52 exact support for the S3/Route-2 readout endpoint triple.

Main result:

```text
If a typed magnitude bridge supplies |gamma_T(center)/gamma_E(center)| = R_conn = 8/9,
then the existing positivity bound q_E > 0 forces the negative branch
gamma_T(center)/gamma_E(center) = -8/9.
The endpoint algebra then gives q_E = 15/8 and rho_E = 21/4.
```

This is not an endpoint derivation.  The remaining open import is the typed
magnitude bridge itself.

# Artifacts

- `docs/QUARK_ROUTE2_RCONN_MAGNITUDE_SIGN_SPLIT_EXACT_SUPPORT_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py`
- `outputs/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-rconn-magnitude-sign-split/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-rconn-magnitude-sign-split/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-rconn-magnitude-sign-split/CLAIM_STATUS_CERTIFICATE.md`

# Claim Status

Actual current surface status: `exact-support`.

Trace class: `upstream_support`.

Reachability: `supports` the endpoint target by reducing the open color/readout
bridge to a typed magnitude bridge.  It does not close the target.

# Verification

```text
python3 scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py
TOTAL: PASS=52 FAIL=0
```

Parent checks:

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
TOTAL: PASS=103, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
TOTAL: PASS=8 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py
TOTAL: PASS=46, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py
TOTAL: PASS=28, FAIL=0
```

Additional checks:

```text
python3 -m py_compile scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py
git diff --check
overclaim scan: clean
```

# Open Import

```text
typed magnitude bridge |gamma_T(center)/gamma_E(center)| = R_conn
```

No audit verdict is applied in this PR.
