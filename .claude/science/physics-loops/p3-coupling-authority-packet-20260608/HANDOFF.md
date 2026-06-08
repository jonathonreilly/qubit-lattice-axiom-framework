# Handoff

Branch: `physics-loop/p3-coupling-authority-packet-20260608`

Target claim: `p3_coupling_is_retention_eligible_composition_2026-06-06`

What changed:

- Added the one-hop authority packet requested by the audit blocker.
- Changed the runner to verify authority rows against the live ledger.
- Replaced the hard-coded `alpha_LM/u0` numerical solve with canonical-surface
  imports and formula checks.
- Narrowed the source note to an open-gate composition packet, not retained P3
  closure.

Verification:

```text
TOTAL: PASS=44 FAIL=0
```

Remaining boundary:

The physical-vs-bare register-not-read selector, conditional `4pi`/I1 bridge,
and bounded canonical `u0` surface remain open or bounded.
