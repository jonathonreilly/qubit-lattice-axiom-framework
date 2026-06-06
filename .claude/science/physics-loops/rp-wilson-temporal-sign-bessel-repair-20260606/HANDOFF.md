# Handoff

Branch-local science block:

- Target: Wilson temporal-gauge reflection-positivity bridge.
- Repair: sign convention and `U(1)` Bessel certificate.
- Main files:
  - `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
  - `scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py`
  - `logs/runner-cache/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.txt`

Verification:

```bash
python3 scripts/cached_runner_output.py scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py --refresh --timeout-sec 240
python3 scripts/cached_runner_output.py scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py --check-only
git diff -- docs/audit --exit-code
git diff --check
```

Expected runner result: `16 PASS / 0 FAIL`.

Independent review should check whether this source repair fully answers the
named blocker; this branch does not edit audit outputs.
