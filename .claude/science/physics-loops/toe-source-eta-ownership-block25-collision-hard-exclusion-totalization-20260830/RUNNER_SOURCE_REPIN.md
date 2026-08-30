# Block25 final runner source repin

The content-reviewed result surface, N1--N8 packet, timeout repair, and final
frozen-input hashes were committed before this repin at
`f1c23952a4e1dbc78075ef3d72c919787b22345d`.

```text
5a1be28753ca13adc8fb22c1909fe3b2e86b79e9e8e65ab38aae02a625f6901f  scripts/admissibility_d4_block24_overlap_projector_hard_exclusion_gate_2026_08_30.py
```

The thirteen declared execution inputs, including the final checkpoint state,
have frozen pre-run fingerprint:

```text
17a88c863e3ba440c0d8b0436a97c899c40dde4505bf5a0099b5263fd5433b35
```

The only permitted final reproduction is one content-bound launch with the
exact result preserved without overwrite at:

```text
logs/runner-cache/admissibility_d4_block24_overlap_projector_hard_exclusion_gate_2026_08_30.txt
```

The earlier successful source revision remains preserved at the distinct
`_initial.txt` path. The final launch must capture merged stdout/stderr, reject
source or declared-input changes across execution, preserve a nonzero or
timeout result, and refuse to overwrite the canonical path.

Any source or declared-input edit after this repin requires a new commit,
fingerprint, repin, and distinct cache path before another execution. This
repin is not a runner result, audit verdict, obligation retirement, or TOE-score
move.
