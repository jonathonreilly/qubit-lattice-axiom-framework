This PR repairs the local/global invariant contradiction in
`docs/FLAVOR_GENERATION_SPACE_BRIDGE_REDUCES_TO_OPEN_GATE_2026-05-31.md`.

The old wording said the global Lefschetz sum vanished while also displaying
`global = L*(2/9)`. The repaired wording distinguishes:

- unsigned same-orientation aggregate: `L*(2/9)`, useful only as a scale diagnostic;
- signed global invariant: zero after retained `Gamma_5` pairing;
- selected local density: `+2/9`, whose promotion to physical observable remains the open gate.

Scope boundary:

- This closes the formula-inventory contradiction.
- It does not derive the local-density-to-observable promotion.
- It does not repair the signed readout-class failure.
- It does not update `docs/audit/**` or any ledger status.
