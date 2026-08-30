# Block24 primary runner source pin

The independently static-accepted primary source was committed, without prior
import, compilation, or execution, at
`eb47d71ccc649c153982cb73018a868da2557af0`.

```text
7215b52c312dc14c3a2277f82c0f2145f5705c7bb8b6c2d685eb2a50bc4f34a5  scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py
```

The ten declared execution inputs have pre-run fingerprint:

```text
c919e36dbddf74cb86f1c1e44aa2c56ed38815767319e02c9a20231b1e629df4
```

The only permitted first execution is the content-bound runner-cache launch
after this pin is committed. Its new, non-overwriting canonical cache path is:

```text
logs/runner-cache/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.txt
```

The launch must capture merged stdout/stderr, refuse a cache write if the source
or any declared input changes during execution, preserve any nonzero or timeout
result, and never overwrite an earlier cache. Any source or declared-input edit
after this pin requires a new commit, explicit repin, and a different cache
path before reexecution.

Runtime and every displayed science predicate remain unverified until the first
execution completes. This pin is not a result, audit verdict, obligation
retirement, or TOE-score move.
