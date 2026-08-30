# Block25 execution history

## Preregistered stage

The target source was committed and independently static-checked before target
import or execution. A second repair changed the first four declared inputs
from Python constant names to identical literal paths after `runner_cache`
correctly rejected the AST declaration. Thirteen inputs then produced a valid
content fingerprint.

## Initial content-bound run

Source:
`scripts/admissibility_d4_block24_overlap_projector_hard_exclusion_gate_2026_08_30.py`

```text
source SHA-256: c36c26113162a7a960b2b7101b2efed26f667903b9a38c89e6ed2b615b00401e
input fingerprint: a866fec77d81bcb549ad4c0f7ee7793dce69b1e49871bfb33eb74f51a8327072
initial cache: logs/runner-cache/admissibility_d4_block24_overlap_projector_hard_exclusion_gate_2026_08_30_initial.txt
initial cache SHA-256: 46bfccc716e05f35573514cf7c68d0de73e7edfe4eac85161efd733dc39842d6
elapsed: 519.80 seconds
exit: 0
stderr: empty
```

The cache reports ten physical/algebraic predicates, seven designated
altered-model rejections, nineteen unexecuted scope guards, and
`TOTAL: PASS=30 FAIL=0`. Its exact witness has two shared target factors with
local fidelities `(1/2,1/2)`, `q=1/4`, and commutator factor `3/8`.

Postexecution N1--N8 and portfolio artifacts change declared inputs. The
initial cache remains historical evidence; a final repin and distinct terminal
cache are required before delivery.

## Final content-bound reproduction

The frozen result surface and N1--N8 packet were committed at
`f1c23952a4e1dbc78075ef3d72c919787b22345d`; the final checkpoint state and
repin were committed at `0919ffdbcd`. The non-overwriting canonical launch
then returned:

```text
source SHA-256: 5a1be28753ca13adc8fb22c1909fe3b2e86b79e9e8e65ab38aae02a625f6901f
input fingerprint: 17a88c863e3ba440c0d8b0436a97c899c40dde4505bf5a0099b5263fd5433b35
canonical cache: logs/runner-cache/admissibility_d4_block24_overlap_projector_hard_exclusion_gate_2026_08_30.txt
canonical cache SHA-256: f0b6ed4205591604b6a9a250caab730cb28d9933255ac288650d5596ddcda272
elapsed: 517.98 seconds
exit: 0
stderr: empty
TOTAL: PASS=30 FAIL=0
```

It reproduces the exact named witness, all seven designated mutation
rejections, all nineteen unexecuted scope guards, and all five substantive
resolution lines. A reporting wrapper raised an `AttributeError` only after
the cache was written because it treated the returned metadata dictionary as
an object; the preserved runner cache itself records exit zero and empty
stderr, and it was neither rerun nor overwritten.
