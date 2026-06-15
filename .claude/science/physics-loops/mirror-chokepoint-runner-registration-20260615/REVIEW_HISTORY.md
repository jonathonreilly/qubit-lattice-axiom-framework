# Review History

- Before edit:
  - `extract_runner(...) -> None`.
  - primary and certificate caches were already fresh.
- After edit:
  - graph extraction resolves `scripts/mirror_chokepoint_joint.py`.
- Full pipeline:
  - `audit_lint` errors: 0.
  - hard invalidations: 8, all downstream of the intentionally edited
    `mirror_chokepoint_note` row.
