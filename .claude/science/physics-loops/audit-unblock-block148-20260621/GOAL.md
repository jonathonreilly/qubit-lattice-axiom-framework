# Goal

Package a source-side audit-unblock repair for `newton_derivation_note` without running the audit worker or proposing any retained Newtonian derivation.

The block adds a note-specific open-gate probe for `docs/NEWTON_DERIVATION_NOTE.md`, wires it into audit discovery, removes stale machine-local artifact links from the touched note, refreshes generated audit surfaces, and leaves the claim `open_gate` / `unaudited` / `effective_status: unaudited`.

This is a reviewer handoff PR. It is not a main push and it does not ask the repo to treat the Newton derivation as closed.
