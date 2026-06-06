# Handoff

## What Changed

- Replaced stale exact row-bucket equality checks with at-least-prior-map checks.
- Added a sum check for the stability subbucket partition.
- Made `ARROW_OR_DYNAMICS_BRIDGE_ROWS` print the computed current count.
- Updated the source note wording and refreshed the runner cache.

## Claim Movement

This directly repairs the completed runner/source drift for `post_record_directed_certificate_examples_2026-06-06`.

It does not edit `docs/audit/**`, apply an audit verdict, promote a row, or change the Record axiom.

## Exact Next Action

Open the review PR from `physics-loop/post-record-directed-cert-count-drift-20260606`.
