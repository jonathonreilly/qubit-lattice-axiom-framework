# Lepton Block D12-Prime Matching - Physical-Operator Open Gate

**Date:** 2026-05-10
**Claim type:** open_gate
**Status:** source-note proposal; independent audit owns audit verdict and
pipeline-derived effective status.
**Scope:** current-surface YT-style matching attempt on the lepton `(2,1)`
block.
**Primary runner:** [`scripts/frontier_lepton_block_d12_prime_matching.py`](../scripts/frontier_lepton_block_d12_prime_matching.py)
**Cache:** [`logs/runner-cache/frontier_lepton_block_d12_prime_matching.txt`](../logs/runner-cache/frontier_lepton_block_d12_prime_matching.txt)

## Claim

The YT-style matching argument cannot be reused as a lepton-block Ward
identity on the current source surface unless an additional physical-operator
bridge is supplied.

The reason is narrow. In the quark YT chain, the two sides of the matching
refer to the same composite scalar operator. On current main, that operator
surface is supplied by the YT Ward source as the `H_unit` scalar-singlet
bilinear on the `Q_L` block, while the color-projection source is explicitly
only a representation channel-fraction boundary:

- [`YUKAWA_COLOR_PROJECTION_THEOREM.md`](YUKAWA_COLOR_PROJECTION_THEOREM.md)
- [`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)

The lepton-block analogy can formally write a hypercharge exchange equation
and, if a unit lepton scalar matrix element is supplied, it algebraically
solves `y_tau = g_1/sqrt(2)`. That formal algebra is not a framework
identity unless the supplied lepton scalar is shown to be the same physical
operator as the scalar used in the matching. The current cited sources do not
provide that bridge.

## Boundary

This note does not use empirical lepton masses, does not predict a lepton
Yukawa, and does not close or permanently rule out Lane 6. It only records a
current-surface gate:

> A YT-style lepton matching needs a theorem identifying a physical lepton
> composite/operator surface, not just a formal unit tensor on the lepton
> block.

Companion branch proposals about lepton tensors or tree-level exchange are
not load-bearing for this landing. If they are later retained by audit, this
gate should be rechecked against those retained inputs.

## Runner Checks

The paired runner verifies:

- the quark YT matching algebra gives `y_t = g_s/sqrt(6)`;
- the formal lepton hypercharge analogy would give `y_tau = g_1/sqrt(2)`
  if a unit lepton scalar operator were supplied;
- the current YT source defines `H_unit` as the scalar-singlet bilinear on
  the `Q_L` block;
- the current YUKAWA color-projection source is only a channel-fraction
  theorem, not a physical Yukawa or scalar wave-function normalization;
- the current cited source text does not define a lepton-composite scalar
  bridge;
- the result remains an open gate, not a retained-grade no-go or mass
  prediction.

## 2026-06-12 runner-cache refresh for re-audit

The audited-conditional re-audit note asked for the runner/cache to be
refreshed against the current cited authorities or for the quark-scalar
premise to be routed explicitly to
[`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md).
This source note now makes that routing load-bearing: the current YT
Ward source supplies `H_unit` as the scalar-singlet bilinear on the
`Q_L` block, while the current YUKAWA color-projection source remains a
non-physical channel-fraction boundary. The lepton side remains blocked
on a missing physical lepton-composite scalar bridge.

The paired runner now reports cited source paths relative to the repo
root instead of embedding a temporary worktree path in the cache. The
2026-06-12 cache refresh is therefore a runner-artifact repair only. It
does not change this row's status, close Lane 6, predict a lepton
Yukawa, or claim a retained-grade no-go.
