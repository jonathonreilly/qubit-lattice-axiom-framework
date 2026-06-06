# Handoff

## What Changed

- Updated the stack-map runner to expect `SUMMARY: PASS=60 FAIL=0` in the directed-certificate examples cache.
- Updated the stack-map note to name the stacked upstream cache repair.
- Refreshed the stack-map cache.

## Claim Movement

This directly repairs the stack-map cache mismatch identified by the audit row, but it is stacked on PR #2957.

It does not edit `docs/audit/**`, apply an audit verdict, promote a row, or change the Record axiom.

## Exact Next Action

Open the stacked review PR against `physics-loop/post-record-directed-cert-count-drift-20260606`.
