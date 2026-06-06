This PR repairs the chirality/anticommutator convention wording in
`docs/FLAVOR_DETR_DEFAULT_FULL_EXERCISE_NOTE_2026-05-30.md`.

The repaired statement is:

- `G_U1` is on-block and commutes with `Gamma_chi` and `C`;
- `||{G_U1,Gamma_chi}||=2.828` is nonzero, so `G_U1` is not a chiral splitter;
- a true chiral splitter would be a separate off-block anticommuting object.

Scope boundary:

- This closes only the convention-wording repair item.
- It does not derive the physical beta=0 tracial-vacuum premise.
- It does not force the det_C measure choice.
- It does not update `docs/audit/**` or any ledger status.
