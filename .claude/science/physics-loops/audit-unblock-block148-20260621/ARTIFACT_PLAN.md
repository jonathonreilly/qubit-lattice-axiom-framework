# Artifact Plan

| Artifact | Purpose | Status |
|---|---|---|
| `scripts/newton_derivation_open_gate_probe.py` | Assertion-bearing wrapper for the Newton note's open-gate boundary and supporting harnesses | Complete |
| `logs/runner-cache/newton_derivation_open_gate_probe.txt` | Cached execution transcript for audit runner precompute | Complete |
| `docs/NEWTON_DERIVATION_NOTE.md` metadata | Parser-visible `Claim type`, `Status authority`, and `Runner`; remove stale machine-local links | Complete |
| Generated audit surfaces | Seed ledger/queue/citation/classification from source note and runner metadata | Complete |
| Branch-local loop pack | Handoff, certificate, trace gate, assumptions/imports, and PR body | Complete |

No audit verdict payload, `apply_audit.py` output, lane registry weaving, or publication matrix status promotion is part of this artifact plan.
