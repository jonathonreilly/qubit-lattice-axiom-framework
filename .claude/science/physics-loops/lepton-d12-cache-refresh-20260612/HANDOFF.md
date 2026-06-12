# Handoff

## What Changed

The lepton D12-prime matching runner was stale against current main. It
expected the old Yukawa source to define the scalar with a
color-indexed quark bilinear and the cache embedded an old temporary
worktree path.

This branch updates the source note and runner to the current authority
split:

- `YT_WARD_IDENTITY_DERIVATION_THEOREM.md` supplies `H_unit` as the
  scalar-singlet bilinear on the `Q_L` block.
- `YUKAWA_COLOR_PROJECTION_THEOREM.md` is only a channel-fraction
  boundary, not a physical Yukawa or scalar normalization.

The refreshed cache reports repo-relative source paths and
`TOTAL: PASS=13, FAIL=0`.

## What This Does Not Do

- It does not supply a lepton-composite scalar bridge.
- It does not predict a lepton Yukawa.
- It does not claim retained-grade no-go status.
- It does not edit audit data.

## Verification

- `python3 scripts/frontier_lepton_block_d12_prime_matching.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_lepton_block_d12_prime_matching.py --force --concurrency 1 --push-mode none --allow-non-main`

## Next Exact Action

Reviewer/auditor can re-run the refreshed runner. The remaining science
work is a separate lepton-composite scalar bridge.
