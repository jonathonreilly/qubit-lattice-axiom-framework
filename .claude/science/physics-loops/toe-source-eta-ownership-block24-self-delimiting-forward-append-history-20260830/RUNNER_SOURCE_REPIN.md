# Block24 compact-runner source repin

The independently static-accepted runtime repair and the preserved first
timeout were committed before repaired-source execution at
`63471f53403275d7ee39608fb46f52b23cd11340`.

```text
0a228689587f492fb3e922ee441e5bd23f7d827e6888f954c72c30c3a0b7cbb7  scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py
```

The ten declared execution inputs have frozen pre-run fingerprint:

```text
411f71c8b0a45f76a968aa6878abc4018757f286e25283469162188bc296ea2f
```

The only permitted repaired-source execution is one content-bound launch with
the exact result preserved without overwrite at:

```text
logs/runner-cache/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30_optimized.txt
```

The controller may use the absent canonical path as an atomic staging location
for `runner_cache` and then move those exact bytes once to the named optimized
path. It must capture merged stdout/stderr, reject source or declared-input
changes across execution, preserve a nonzero or timeout result, and refuse to
overwrite either path. The earlier source revision remains preserved at its
distinct `_initial_timeout.txt` path.

Any source or declared-input edit after this repin requires a new commit,
fingerprint, pin, and cache path before another execution. This repin is not a
runner result, audit verdict, obligation retirement, or TOE-score move.
