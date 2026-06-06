# Route Portfolio

## Selected Route

Use the existing native bridge:

- `P E P` is a valid effect with `0 <= PEP <= P <= I`.
- `Tr(rho PEP)/Tr(rho P) = Tr(rho|_P E)`.
- Trace/effect pairing is real-linear and maps states/effects to `[0,1]`.
- The Jordan-product guard shows boundaries alone do not suffice.

Then patch the parent to consume that bridge and exclude zero-probability
conditioning events.

## Rejected Routes

- Add a new standard-math import node: unnecessary because a native bridge
  already exists.
- Retag the ledger: outside this workstream.
- Reprove full general sequential-product uniqueness: not needed for the finite
  operator-algebra blocker.
