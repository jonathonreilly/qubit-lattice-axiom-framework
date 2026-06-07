# Handoff

This PR repairs the audit-readiness surface for `quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26`.

What changed:

- The quark note now names the Record-selector sidecar boundary and the exact remaining repair target.
- The quark runner checks the sidecar runner source, sidecar cache freshness, and the source-note no-transfer boundary.
- The Record-selector sidecar runner now handles historical selector rows whose current ledger status changed after the sidecar was created, while still requiring ledger metadata and source anchors.
- Both caches are refreshed and clean.

What this does not claim:

- It does not derive quark masses.
- It does not select quark-sector BAE or a quark dial.
- It does not transfer charged-lepton BAE to quarks.
- It does not modify audit verdict files.

Verification results:

```text
frontier_record_selector_audit_sidecar_2026_06_05.py: SCORECARD PASS=87 FAIL=0
frontier_quark_mass_spectrum_koide_scheme_open_gate.py: TOTAL: PASS=18 FAIL=0
```
