# Handoff

## Block13 Summary

Branch:

```text
physics-loop/s3-route2-readout-endpoint-block13-20260621
```

PR:

```text
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4542
```

Block13 proves the exact source-side Gram collapse:

```text
K_R^T M K_R = (a^T M a) b b^T.
```

Unit `E` and `T1` bright probes therefore see the same response scalar for
all source-side `K_R` Gram/tensor-power contractions in the current
channel-blind grammar. The route gives `lambda=1`, not `9/4`.

## Artifacts

- `docs/QUARK_ROUTE2_KR_GRAM_NONSEPARABLE_DEGREE2_NO_GO_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_kr_gram_nonseparable_degree2_no_go_2026_06_21.py`
- `logs/runner-cache/frontier_quark_route2_kr_gram_nonseparable_degree2_no_go_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/`

## Current Verification

Completed:

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_kr_gram_nonseparable_degree2_no_go_2026_06_21.py
PASS=14 FAIL=0

python3 -m py_compile scripts/frontier_quark_route2_kr_gram_nonseparable_degree2_no_go_2026_06_21.py
pass

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py
PASS=12 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PASS=11 FAIL=0

git diff --check
pass

branch-local status/overclaim rg scan
no matches
```

PR identity verification:

```json
{"baseRefName":"main","headRefName":"physics-loop/s3-route2-readout-endpoint-block13-20260621","number":4542,"state":"OPEN","title":"[physics-loop] s3-route2-readout-endpoint block13 no-go","url":"https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4542"}
```

## Remaining Nature-Grade Blocker

Derive a channel metric/normalization primitive with the needed reciprocal
square ratio, or construct a new nonseparable total-degree-2 primitive outside
current `K_R` source-side Gram contractions.

## Exact Next Action

Continue the campaign with the channel metric/normalization primitive target,
or a new nonseparable total-degree-2 primitive outside current `K_R`
source-side Gram contractions.
