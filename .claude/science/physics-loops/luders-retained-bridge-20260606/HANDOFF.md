# Handoff

This PR is intended for reviewer extraction and independent audit, not direct
ledger mutation.

Core change:

- target note now derives finite trace/effect pairing from POVM additivity;
- target note uses retained canonical `K_P=P` and retained finite Kraus branch
  algebra to derive the Lüders branch state;
- runner now reports `82 PASS / 0 FAIL`.

Boundaries to preserve:

- no claim that Record supplies probability or measurement dynamics;
- no broad Born-rule promotion;
- no audit-result edits;
- no claim of uniqueness for all instruments implementing a projective POVM.
