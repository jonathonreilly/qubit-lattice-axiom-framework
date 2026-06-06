This PR repairs the CHSH comparison wording in
`docs/CHSH_TSIRELSON_LATTICE_QUBITS_BOUND_NOTE_2026-05-20.md`.

The corrected ordering is:

```text
classical <= 2 < Tsirelson <= 2 sqrt(2) < algebraic/no-signaling <= 4
```

Scope boundary:

- This closes only the comparison-wording repair item.
- It does not resolve the broader composition-premise audit blocker.
- It does not update `docs/audit/**` or any ledger status.
