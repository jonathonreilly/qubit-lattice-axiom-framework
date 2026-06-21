# Claim Status Certificate

| Field | Value |
|---|---|
| Target claim | `newton_derivation_note` |
| Target note | `docs/NEWTON_DERIVATION_NOTE.md` |
| Actual current surface status | `open` |
| Ledger claim type | `open_gate` |
| Ledger audit status | `unaudited` |
| Ledger effective status | `unaudited` |
| Conditional surface status | null |
| Hypothetical axiom status | null |
| Admitted observation status | null |
| Runner | `scripts/newton_derivation_open_gate_probe.py` |
| Runner result | `SUMMARY: PASS=14 FAIL=0` |
| Runner classification | dominant class `B`, assert count `1`, decoration candidate `true` |
| Trace class | `upstream_support` |
| Reachability | `supports` |
| Review-loop disposition | `pass` for local audit-compatibility review only |
| Proposal allowed | `false` |
| Audit required before effective retained | `true` |
| Bare retained allowed | `false` |

`proposed_retained` and `proposed_promoted` wording is not allowed for this block. The runner checks discoverability, execution of bounded supporting harnesses, and preservation of the open residual gate. It does not retire the persistent compact-object external-field inertial-mass step.
