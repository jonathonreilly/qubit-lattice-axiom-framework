Handoff

This branch repairs the `kernel_vs_gravity_note` failed source boundary without
touching audit artifacts.

Changed source files:

- `archive_unlanded/kernel-gravity-conflation-2026-04-30/KERNEL_VS_GRAVITY_NOTE.md`
- `scripts/complex_action_kernel_vs_gravity.py`
- `logs/runner-cache/complex_action_kernel_vs_gravity.txt`

What changed:

- the runner no longer says local damping implies detector escape below one for
  every `gamma > 0`;
- the runner now records PASS/FAIL checks for the finite thresholded detector
  statement and the gravity centroid-crossover statement;
- the archived note now has a 2026-06-17 executable boundary repair section.

Verification:

- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/complex_action_kernel_vs_gravity.py --refresh --timeout-sec 600`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/complex_action_kernel_vs_gravity.py --check-only`
- `python3 -m py_compile scripts/complex_action_kernel_vs_gravity.py`
- `git diff --check`
