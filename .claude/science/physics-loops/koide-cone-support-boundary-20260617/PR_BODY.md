## Summary

This PR repairs the source boundary for the charged-lepton Koide cone
equivalence row.

The exact algebra stays intact: `Q = 2/3` is equivalent to
`a_0^2 = 2|z|^2` for a positive three-vector decomposed into `C_3`
characters. The repair removes source-side retained/proposed-retained carrier
framing and makes the row exact support with bounded downstream reuse, because
the paired runner still reports `KOIDE_FORCING_RESOLVED=FALSE`.

## Trace

- Target: `charged_lepton_koide_cone_algebraic_equivalence_note`
- Honest status: exact-support / bounded downstream reuse
- Trace class: upstream support
- Not claimed: Koide value derivation, physical cone forcing, observational
  pin derivation, retained status, or audit verdict

## Artifacts

- `docs/CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md`
- `scripts/frontier_charged_lepton_observable_curvature.py`
- `logs/runner-cache/frontier_charged_lepton_observable_curvature.txt`
- `.claude/science/physics-loops/koide-cone-support-boundary-20260617/HANDOFF.md`
- `.claude/science/physics-loops/koide-cone-support-boundary-20260617/TRACE_GATE.md`
- `.claude/science/physics-loops/koide-cone-support-boundary-20260617/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```bash
python3 scripts/frontier_charged_lepton_observable_curvature.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_charged_lepton_observable_curvature.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_charged_lepton_observable_curvature.py
python3 -m py_compile scripts/frontier_charged_lepton_observable_curvature.py
git diff --check
```

Review-loop disposition: `reviewer_owned_not_run`.

No audit ledger, audit queue, publication, or front-door files are edited.
