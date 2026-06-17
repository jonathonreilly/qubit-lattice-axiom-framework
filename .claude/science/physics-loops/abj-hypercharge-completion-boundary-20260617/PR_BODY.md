## Summary

This PR adds a source-side ABJ hypercharge/completion decoupling boundary.

It proves the exact rational arithmetic for the ABJ row's P-HY/P-COMP half:
the bounded LH `{+1/3 x6, -1 x2}` surface plus declared P-HY and admitted
minimal RH completion forces `Y(u_R)=4/3`, `Y(d_R)=-2/3`, `Y(e_R)=-2`, and
the one-generation anomaly conditions cancel exactly.

## Honest Status

- Actual current surface status: bounded-support.
- Trace class: upstream_support.
- Reachability: partially closes the ABJ hypercharge/completion blocker.
- Not a retained/proposed-retained claim.
- Independent audit still decides any effective status.

## What Remains Open

- P-HY physical anomaly-relevant `U(1)_Y` identification.
- P-COMP-min minimal completion and vectorlike/mirror exclusion.
- P-REC spacetime Clifford `gamma_5` reconstruction.
- P-ABJ anomaly-to-inconsistency premise.

## Artifacts

- `docs/ABJ_HYPERCHARGE_COMPLETION_DECOUPLING_BOUNDARY_NOTE_2026-06-17.md`
- `scripts/frontier_abj_hypercharge_completion_decoupling_boundary_2026_06_17.py`
- `logs/runner-cache/frontier_abj_hypercharge_completion_decoupling_boundary_2026_06_17.txt`
- `.claude/science/physics-loops/abj-hypercharge-completion-boundary-20260617/HANDOFF.md`
- `.claude/science/physics-loops/abj-hypercharge-completion-boundary-20260617/TRACE_GATE.md`
- `.claude/science/physics-loops/abj-hypercharge-completion-boundary-20260617/CLAIM_STATUS_CERTIFICATE.md`

## Checks

```bash
PYTHONPATH=scripts python3 scripts/frontier_abj_hypercharge_completion_decoupling_boundary_2026_06_17.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_abj_hypercharge_completion_decoupling_boundary_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_abj_hypercharge_completion_decoupling_boundary_2026_06_17.py
python3 -m py_compile scripts/frontier_abj_hypercharge_completion_decoupling_boundary_2026_06_17.py
git diff --check
```

Review-loop disposition: reviewer-owned, not run in this branch.
