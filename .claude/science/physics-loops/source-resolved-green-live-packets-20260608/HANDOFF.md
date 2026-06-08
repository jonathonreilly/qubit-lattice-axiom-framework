# Handoff

Branch: `physics-loop/source-resolved-green-live-packets-20260608`

Target claims:

- `source_resolved_retarded_green_pocket_note`
- `source_resolved_transverse_propagating_green_note`

What changed:

- Corrected retarded runner to print `ret/inst` and true `ret/same` separately.
- Corrected transverse runner to print `trans/inst` and true `trans/same` separately.
- Added assertion gates to both runners.
- Added restored live source notes under `docs/`.
- Refreshed both caches.
- Did not edit audit outputs.

Verification:

```text
python3 scripts/cached_runner_output.py --refresh scripts/source_resolved_retarded_green_pocket.py --tail-chars 2500
python3 scripts/cached_runner_output.py --refresh scripts/source_resolved_transverse_propagating_green.py --tail-chars 2500
python3 scripts/cached_runner_output.py --check-only scripts/source_resolved_retarded_green_pocket.py
python3 scripts/cached_runner_output.py --check-only scripts/source_resolved_transverse_propagating_green.py
python3 -m py_compile scripts/source_resolved_retarded_green_pocket.py scripts/source_resolved_transverse_propagating_green.py
```

Result: both caches fresh, both end with `ASSERTIONS: PASS`.

Remaining boundary:

No full retarded field equation, no full propagating transverse field theory,
and no continuum theorem is claimed.
