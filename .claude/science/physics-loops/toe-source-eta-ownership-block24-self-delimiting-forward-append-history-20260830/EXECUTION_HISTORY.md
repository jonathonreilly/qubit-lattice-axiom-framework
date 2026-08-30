# Block24 execution history

## First content-pinned execution

- source commit: `eb47d71ccc649c153982cb73018a868da2557af0`;
- source-pin commit: `82136db6d3ccc1b8fbd73a962c27e4f85fa68bc5`;
- source SHA-256:
  `7215b52c312dc14c3a2277f82c0f2145f5705c7bb8b6c2d685eb2a50bc4f34a5`;
- declared-input fingerprint:
  `c919e36dbddf74cb86f1c1e44aa2c56ed38815767319e02c9a20231b1e629df4`;
- preserved cache:
  `logs/runner-cache/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30_initial_timeout.txt`;
- cache SHA-256:
  `d8996094669d346a3ffd8d1eeee9d8f3820d548559e54d4015daa52827f72313`;
- process result: timeout after `900.01` seconds, exit `-9`; and
- merged stderr was empty.

The run passed every displayed check through `self_delimiting_tip`, including
the global append channel, classical Record QND, and full physical covariance.
It timed out inside the three-event stage before that check printed. Therefore
the cache is a preserved runtime failure and partial positive diagnostic, not a
completed runner result or negative physics terminal.

## Authorized runtime-only repair

The first source materialized a nineteen-component symbolic effect for each of
16,464 literal three-event branches and then repeatedly rescaled/summed those
objects. The repaired representation keeps the same literal roots, pointer
handoffs, append factor lists, and contractions, but records the mathematically
equivalent pair

```text
(exact initial effect E_b1, factor-derived scalar T(b2|b1) T(b3|b2)).
```

Branch equality, last-outcome marginals, full suffix normalization, symbolic
reference extension, and total POVM completion are then checked on that compact
representation. The repair must be committed, independently static-reviewed,
and repinned to a different cache path before reexecution.

Two independent static challengers accepted the exact repaired source SHA-256
`0a228689587f492fb3e922ee441e5bd23f7d827e6888f954c72c30c3a0b7cbb7`
for commit and repin. They did not execute the source; runtime and every
unreached predicate remain unverified. The accepted repair and this preserved
initial-timeout record were committed at
`63471f53403275d7ee39608fb46f52b23cd11340`.

## Compact three-event execution

- source commit: `63471f53403275d7ee39608fb46f52b23cd11340`;
- source-repin commit: `0f276b65dbea22efe44b813a5e5918459e2d5f9d`;
- source SHA-256:
  `0a228689587f492fb3e922ee441e5bd23f7d827e6888f954c72c30c3a0b7cbb7`;
- declared-input fingerprint:
  `411f71c8b0a45f76a968aa6878abc4018757f286e25283469162188bc296ea2f`;
- preserved cache:
  `logs/runner-cache/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30_optimized.txt`;
- cache SHA-256:
  `193a074c40305d6e4760f12861ea24621c227813105b18cc699706960f0dc5fa`;
- process result: timeout after `900.01` seconds, exit `-9`; and
- merged stderr was empty.

This run reproduced the first ten displayed passes and newly passed
`exact_three_event_composite`: every one of the 16,464 literal sequential
composites contracted to the factor-derived three-event cylinder, both prefix
marginals, total identity, and symbolic-reference identity. It then timed out
inside `finite_history_induction_certificate` before that predicate printed.
Thus the cache is a second harness-performance failure with a strictly
stronger partial positive diagnostic, not a completed runner result or a
negative physics terminal.

The remaining runtime hotspot repeatedly materializes and simplifies every
coefficient of an arbitrary symbolic prefix effect and its reference extension
for each next-outcome branch. A permitted repair may store the common arbitrary
effect plus each literal-contracted scalar and materialize only the summed
coefficientwise identity. It must retain symbolic depth and anchor, exact
returned-tip/QND typing, all target branches, factor-derived row normalization,
and symbolic `I_R`.
