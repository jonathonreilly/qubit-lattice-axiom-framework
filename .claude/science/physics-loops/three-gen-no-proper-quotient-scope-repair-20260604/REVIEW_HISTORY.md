# Review History

Local checks run before PR:

- `PYTHONPATH=scripts python3 scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `python3 -m py_compile scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `git diff --check`

All passed locally.
