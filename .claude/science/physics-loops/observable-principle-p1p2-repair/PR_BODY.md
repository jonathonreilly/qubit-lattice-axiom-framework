## Summary

This PR repairs `observable_principle_from_axiom_note` for re-audit by
narrowing the source to the explicit P1+P2 conditional surface requested by
the latest audit feedback.

It does not introduce new axioms and does not apply an audit verdict.

## Science Boundary

- Honest branch-local status: `conditional-support`.
- Keeps P1 scalar additivity as an admitted selection premise.
- Keeps P2 continuous phase-blind scalar-generator selection as an admitted
  selection premise.
- Recasts the old "runner-local derivation of P2/P3/P4" language as candidate
  consistency checks only.
- Preserves the finite `log|det(D+J)|` source-response algebra and the
  comparator-only `v` readout boundary.

## Verification

- `python3 scripts/frontier_hierarchy_observable_principle_from_axiom.py`
  -> `27 pass, 0 fail`
- `bash docs/audit/scripts/run_pipeline.sh`
  -> row reset to `unaudited`; audit queue position 1; `ready: true`;
  `critical`; `transitive_descendants: 723`
- `python3 -m py_compile scripts/frontier_hierarchy_observable_principle_from_axiom.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
  -> passes with the existing unrelated Maradudin warning only
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md scripts/frontier_hierarchy_observable_principle_from_axiom.py .claude/science/physics-loops/observable-principle-p1p2-repair`
- `git diff --check`

## Handoff

See
`.claude/science/physics-loops/observable-principle-p1p2-repair/HANDOFF.md`.
