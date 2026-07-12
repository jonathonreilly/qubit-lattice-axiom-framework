# Handoff

## Current State

The old runner does not contain a causal propagation history. Both the old
"causal" and static-cone branches construct the same position-only node field.
The selected repair is an exact input-interface/history-label no-go, not a prose
promotion of that mislabeled branch.

## Current Block

- Branch: `physics-loop/shapiro-static-discriminator-block01-20260711`
- Base: `origin/main@def6c1127`
- Claim target: `shapiro_static_discriminator_note`
- Trace: direct closure of the quoted Class-A blocker
- Audit authority surfaces: untouched

## Next Exact Action

Push the reviewed branch and open the single unmerged review PR. After merge,
the independent audit worker should audit `shapiro_static_discriminator_note`
first; the two direct companion rows remain dependency-blocked until that
target is ratified.

## Final Verification

- all three changed runners compile;
- all three SHA-pinned caches are fresh, exit `0`, and end in
  `ASSERTIONS: PASS`;
- primary full replay: `93.99 s`, six assertive checks;
- QA and unique-discriminator consumers pass live;
- manual independent reduction verifies equal inputs to a fixed deterministic
  map have equal outputs;
- review-loop iteration 2: Code/Runner PASS, No-Go Discipline N1-N8 PASS,
  imports disclosed, repo governance clean;
- audit pipeline: target `no_go/unaudited/ready`, `deps=[]`; QA companion
  `bounded_theorem/unaudited`; unique companion `no_go/unaudited`;
- strict audit lint: zero errors;
- generated audit, publication-effective-status, registry, and front-door
  surfaces restored to `origin/main` and absent from the branch diff;
- `git diff --check`: pass.
