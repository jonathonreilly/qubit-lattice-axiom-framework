# Handoff

This branch repairs `poisson_self_gravity_mechanism_note` by turning the old
hard-coded mechanism summary into a finite hard-bar certificate.

## What It Fully Supports

- Exact `epsilon = 0` identity checks pass in the cached main loop and V3
  outputs.
- Frozen-field / step-local Born values are machine-clean.
- Nonzero-coupling rows keep the weak-field TOWARD sign.
- Source-strength scaling remains near-linear on the cached rows.
- V3 matched-null observables move in the signed direction.

## Why It Is A No-Go For The Mechanism Claim

- Nonzero-coupling loop rows fail strict convergence.
- End-to-end Born is not machine-clean and is diagnostic-only.
- The matched-null effect remains tiny on the tested family.
- No stable converged nonzero-coupling regime with a non-tiny effect is shown.

## Reviewer Notes

The branch does not add axioms and does not apply an audit verdict. The audit
pipeline queues the row for independent review as `no_go`, `unaudited`,
`ready=true`, with no open dependency paths.
