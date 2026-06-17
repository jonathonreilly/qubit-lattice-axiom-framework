## Summary

Adds an exact negative boundary for the quark Route-2 endpoint numerical-match
rows:

- proves E-center-blind endpoint constraints leave `rho_E = beta_E/alpha_E`
  free;
- shows `rho_E = 21/4`, `q_E = 15/8`, and center `T/E = -8/9` are exactly
  equivalent under the granted T-side endpoint data;
- updates the endpoint quotient/chain notes and existing naturality no-go with
  narrow companion pointers.

## Honest Boundary

This is a no-go/source-unblock PR. It does not derive `rho_E`, quark masses,
CKM/J, or any retained quark closure. It does not edit audit results or status
surfaces.

## Trace

- Handoff:
  `.claude/science/physics-loops/quark-route2-ecenter-blindness-20260617/HANDOFF.md`
- Trace gate:
  `.claude/science/physics-loops/quark-route2-ecenter-blindness-20260617/TRACE_GATE.md`
- Certificate:
  `.claude/science/physics-loops/quark-route2-ecenter-blindness-20260617/CLAIM_STATUS_CERTIFICATE.md`

## Checks

```bash
python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
python3 scripts/cached_runner_output.py scripts/frontier_quark_route2_e_center_blindness_no_go.py --refresh
python3 scripts/cached_runner_output.py scripts/frontier_quark_route2_e_center_blindness_no_go.py --check-only
python3 -m py_compile scripts/frontier_quark_route2_e_center_blindness_no_go.py
git diff --check
```

Results:

- direct runner: `PASS=14, FAIL=0`
- new runner cache: refreshed and fresh
- adjacent Route-2 naturality no-go cache: fresh
- `py_compile`: pass
- `git diff --check`: pass
- generated audit/status surface scan: empty
