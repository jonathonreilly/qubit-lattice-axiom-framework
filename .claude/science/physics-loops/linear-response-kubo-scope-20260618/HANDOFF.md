# Handoff

This PR repairs source-boundary language for
`linear_response_second_order_kubo_note`.

Changed source packet:

- Narrows the note's binding conclusion to the finite second-order replay.
- Removes citable all-orders Taylor/no-higher-order conclusion language from
  the body, bottom line, and repair-path sections.
- Leaves third-or-higher Taylor orders, alternate expansion basepoints, and
  non-perturbative treatments open.
- Leaves the existing runner/cache unchanged because the cache already supports
  the finite replay.

Verification:

```text
python3 scripts/cached_runner_output.py --check-only scripts/linear_response_second_order_kubo.py
fresh logs/runner-cache/linear_response_second_order_kubo.txt

git diff --check
```

Reviewer focus:

- Confirm the note no longer claims an all-orders Taylor no-go.
- Confirm the supported result remains the finite second-order replay.
- Confirm no generated ledgers, publication matrices, lane registry, active
  review queue, or front-door status surfaces are included.
