# [physics-loop] s3-route2-readout-endpoint block23 exact-support

## Summary

Adds a narrow sign-support theorem for the Route-2 source-domain split.

Main result:

```text
rho_E > -6  =>  q_E > 0
q_T = 5/6 > 0
s_TE = -2 < 0
c_TE = s_TE q_T / q_E < 0
```

So the sign of `-F_adj` is compatible with the positive-lift Route-2 family.
The missing blocker is now sharper: `|c_TE| = F_adj`, the scalar-to-Route-2
typecast, or a direct typed readout landing edge.

## Files

- `docs/QUARK_ROUTE2_SOURCE_DOMAIN_SIGN_SUPPORT_TYPECAST_REMAINDER_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.py`
- `outputs/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.py
TOTAL: PASS=45, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
TOTAL: PASS=8 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py
TOTAL: PASS=28, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
TOTAL: PASS=103, FAIL=0

python3 -m py_compile scripts/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.py
pass

git diff --check
pass

branch-local wording scan
pass
```

## Boundary

This PR proves sign support only. It does not supply `|c_TE| = F_adj`, does
not typecast color-domain magnitude into Route-2 readout, and does not change
parent row authority status.
