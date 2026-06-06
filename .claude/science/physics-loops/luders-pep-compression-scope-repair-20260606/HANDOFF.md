# Handoff

This PR repairs the Lueders/PEP row by narrowing it to a finite
projection-compression theorem.

Changed source surface:

- No longer treats measurement update or trace/effect probability semantics as
  theorem inputs.
- States only `PEP` compression positivity, trace cyclicity, boundaries, and
  nested compression.
- Measurement/Born interpretation is downstream context only.

Changed runner:

- Replaced conditional measurement runner with finite compression runner.
- Checks exact rational `d=2`, numeric `d=2,3,4`, nested compression, and
  Jordan guard.

Verification:

```text
python3 scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py
python3 scripts/cached_runner_output.py scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py --refresh
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py --check-only
git diff --check
```

No audit data, ledger verdict, queue status, or repo-wide status surface was
edited.
