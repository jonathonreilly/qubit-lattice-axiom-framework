# Handoff

## Claim-state movement

The branch moves the claim from a runner-artifact-blocked state to an
audit-ready `proposed_retained` source package.  It does not assign an audit
verdict and does not change the physical Wilson-environment boundary.

## Verification

```bash
python3 scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py
python3 scripts/precompute_audit_runners.py \
  --runners scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py \
  --force --allow-non-main --push-mode none
python3 -m py_compile scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py
python3 scripts/vocab_lint.py --fix \
  docs/SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md \
  scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py \
  logs/runner-cache/frontier_su3_character_diagonal_convolution_equivalence_narrow.txt
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

The pipeline was validation-only; its generated audit and publication outputs
were removed from the branch after confirming queue visibility.

## Exact next action

Land the source note, runner, cache, and this loop checkpoint, then send
`su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10`
to the independent re-audit lane.
