# Handoff

This PR repairs the parent Lueders row boundary. The PEP bridge remains useful
finite matrix algebra, but the parent no longer says it supplies trace/effect
probability interpretation, measurement instruments, or a full Lueders/Born
derivation.

Verification:

```bash
python3 scripts/cached_runner_output.py --refresh scripts/luders_parent_boundary_guard_2026_06_07.py
PYTHONPATH=scripts python3 scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py
git diff --check
git diff -- docs/audit
```

Remaining blocker: derive or explicitly retain the measurement-side
trace/effect probability and record-conditioning instrument semantics.
