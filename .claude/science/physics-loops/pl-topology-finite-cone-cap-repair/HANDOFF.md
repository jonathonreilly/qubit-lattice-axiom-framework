# Handoff

## Target

`pl_topology_infrastructure_textbook_import_note_2026-05-17`

## Repair

The row is narrowed from a broad named-import wrapper to a finite cone-cap
construction certificate. The runner verifies, for `R = 2, 3, 4`, that the
triangulated cubical boundary is connected, closed, has `chi = 2`, and that
the cone cap has exactly that boundary, paired side faces, apex link equal to
the boundary triangulation, and `chi = 1`.

## Verification

- `bash docs/audit/scripts/run_pipeline.sh` -> pass; pre-existing Maradudin
  warning/notices only.
- `PYTHONPATH=scripts python3 scripts/frontier_pl_topology_finite_cone_cap_certificate.py | tee outputs/pl_topology_finite_cone_cap_certificate_2026-05-26.txt` -> PASS=42 FAIL=0.
- `python3 -m py_compile scripts/frontier_pl_topology_finite_cone_cap_certificate.py` -> pass.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors;
  pre-existing warning/notices only.
- `python3 scripts/render_controlled_vocabulary.py --check` -> clean.
- `python3 scripts/vocab_lint.py --report-only docs/PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` -> 0 violations.
- `git diff --check` -> pass.

## Audit Queue State

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `deps`: `[]`
- `open_dependency_paths`: `[]`
- `transitive_descendants`: `703`
- `load_bearing_score`: `10.459`
- queue position: `1`
- queue ready: `true`
- criticality: `critical`

## Remaining Blockers

Global PL cap-map uniqueness, `S^3` compactification, Perelman/Moise,
Schoenflies/Alexander, mapping-class gluing uniqueness, van Kampen, and
Kawamoto-Smit physical closure remain outside this row.
