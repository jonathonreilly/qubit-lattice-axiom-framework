# Handoff

This branch repairs `source_resolved_wavefield_mechanism_note` by preserving
the source-depth phase-ramp evidence while removing author-side closure
language.

What changed:

- status line is now bounded support;
- absolute local artifact links are replaced with repo-relative links;
- finite-speed rule and parameter envelope are explicit open imports;
- runner output says bounded depth-mechanism probe;
- source dependency bookkeeping no longer cites audit results.

Checks to run:

- `python3 scripts/cached_runner_output.py scripts/source_resolved_wavefield_mechanism.py --refresh --timeout-sec 1800`
- `python3 scripts/cached_runner_output.py scripts/source_resolved_wavefield_mechanism.py --check-only`
- `python3 -m py_compile scripts/source_resolved_wavefield_mechanism.py`
- `git diff --check`

Remaining blockers:

- derive or replace the finite-speed wavefield update rule;
- sensitivity-test the runner-selected parameter envelope;
- keep source-to-NV coupling, absolute units, and detector transfer in
  downstream Diamond lanes.
