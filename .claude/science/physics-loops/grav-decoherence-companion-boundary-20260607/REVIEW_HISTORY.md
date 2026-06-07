# Review History

No automated review loop was run in this block. The user has delegated extraction and landing review to the reviewer.

Local checks run before PR:

```text
python3 scripts/frontier_grav_decoherence_derived.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_grav_decoherence_derived.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_grav_decoherence_derived.py
git diff --check
git diff --name-only docs/audit
```
