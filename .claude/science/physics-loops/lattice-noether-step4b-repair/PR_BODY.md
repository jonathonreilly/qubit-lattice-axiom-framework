## Summary

This PR repairs the lattice Noether Step 4b boundary without adding any
framework axiom or applying an audit verdict.

- narrows the `(2Z)^3` translation branch from the old density (3) claim to
  the exact localized central two-step Ward identity (3a)
- keeps the canonical density (3) as support-only unless a later audit-clean
  proof derives it from the two-shift Ward identity
- adds runner exhibit `E7` on a nondegenerate `L=6` block for the field-level
  localized-envelope identity
- regenerates the audit queue/ledger so the edited row is ready for
  independent audit

## Audit Queue Result

`axiom_first_lattice_noether_theorem_note_2026-04-29` is now:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `claim_type`: `bounded_theorem`
- ready audit queue rank: 1
- criticality: critical
- descendants: 895
- runner: `scripts/axiom_first_lattice_noether_check.py`

## Verification

- `python3 -m py_compile scripts/axiom_first_lattice_noether_check.py`
- `python3 scripts/axiom_first_lattice_noether_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `git diff --check`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md scripts/axiom_first_lattice_noether_check.py .claude/science/physics-loops/lattice-noether-step4b-repair`

Known existing warning: strict audit lint still reports the unrelated
`lattice_greens_function_maradudin_textbook_import_note_2026-05-18`
conditional-repair-prefix warning already present on main.

## Handoff

See `.claude/science/physics-loops/lattice-noether-step4b-repair/HANDOFF.md`.
