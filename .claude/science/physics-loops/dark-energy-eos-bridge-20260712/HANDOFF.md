# Handoff

## Current result

The source note now carries a `proposed_retained` no-go rather than a positive
EOS derivation.  `T_F` plus an explicitly granted intrinsic round-
`S^3` spectrum does not entail a physical cosmological constant, a map to a
fixed physical radius, or an EOS.  Closed-FRW geometry sharpens the residual
to extrinsic curvature and source data; pure de Sitter supplies equality only
at its time-symmetric throat.  A supplied constant vacuum density still
implies `w=-1` conditionally.

## Proposed later weaving (not performed in this science PR)

After independent audit, the integration process should inspect
`COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`,
`DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`, the cosmology rows in
`docs/publication/ci3_z3/PUBLICATION_MATRIX.md`, and the graviton/vector/scalar
spectral-tower rows that consume the asserted identity.  These are proposed
post-audit invalidation/weaving candidates only.  This branch does not modify
the lane registry, status board, publication matrix, audit ledger/queue,
canonical harness index, or other repo-wide authority surface.

## Remaining Nature-grade blocker

Derive a covariant graph-spectrum-to-vacuum-action term with exact
normalization, graph-radius-to-physical-curvature-radius identification,
source-split control, conservation, and a frozen-modulus or superselection
theorem.

## Exact next action

Push the reviewed branch, open one review PR, verify its base and body, and
record the PR URL in this pack.  Independent audit remains required before
effective retention.

## Verification completed

- primary Class-A runner: `PASS=12 FAIL=0`;
- legacy source-pin helper: `2 PASS / 0 FAIL`;
- Python compilation and `git diff --check`: pass;
- vocabulary lint: zero violations;
- independent SymPy reductions: FRW residual, de Sitter throat, source split,
  and shell series all pass;
- review-loop: pass after three iterations;
- N1--N8 no-go discipline: pass;
- validation-only audit pipeline and strict lint: pass with no errors;
- generated audit/status outputs: stripped from the science branch.
