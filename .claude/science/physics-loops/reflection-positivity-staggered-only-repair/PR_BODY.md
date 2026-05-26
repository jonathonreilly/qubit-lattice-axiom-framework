## Summary

This PR repairs `axiom_first_reflection_positivity_theorem_note_2026-04-29`
by narrowing the load-bearing claim to the staggered-only fermion sector, as
requested by the latest audit feedback.

## Science Boundary

- Honest branch-local status: `proposed_retained` for independent audit.
- In scope: `M = M_KS + mI`, `m > 0`, plus the Wilson plaquette gauge half.
- Out of scope: fermion Wilson-term determinant positivity, including the
  symmetric-canonical `M_W = r*d*I` subsurface.
- E6 is no longer counted by the primary runner or used as theorem support.

## Verification

- `python3 scripts/axiom_first_reflection_positivity_check.py`
  -> `PASSED: 5/5`
- `bash docs/audit/scripts/run_pipeline.sh`
  -> row reset to `unaudited`; audit queue position 1; `ready: true`;
  `critical`; `transitive_descendants: 887`
- `python3 -m py_compile scripts/axiom_first_reflection_positivity_check.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
  -> passes with the existing unrelated Maradudin warning only
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md scripts/axiom_first_reflection_positivity_check.py .claude/science/physics-loops/reflection-positivity-staggered-only-repair`
- `git diff --check`

## Handoff

See
`.claude/science/physics-loops/reflection-positivity-staggered-only-repair/HANDOFF.md`.
