# PR Backlog

## Candidate title

Dynamics classifier for generation dial stable settings

## Candidate body

Adds bounded scaffold/proposal artifacts for the post-Record dynamics push:

- record-function finite-sector algebra from Record;
- local stability grammar on the positive generation dial;
- dynamics classification on the exact generation dial `r(s)=2^(s-1)`.

The classifier shows:

- two-sector entropy ascent stabilizes `s=0`;
- reverse branch `r -> sqrt(r/2)` stabilizes `s=0`;
- sharpening `r -> 2r^2` repels `s=0`;
- real-mode entropy ascent stabilizes `s=1`;
- heat-kernel path transits through `s=0`.

Runners:

- `python3 scripts/record_function_finite_sector_algebra_2026_06_05.py`
  with `PASS=18 FAIL=0`.
- `python3 scripts/generation_dial_local_stability_grammar_2026_06_05.py`
  with `PASS=13 FAIL=0`.
- `python3 scripts/generation_dial_dynamics_stability_classifier_2026_06_05.py`
  with `PASS=26 FAIL=0`.

This deliberately does not force Koide from Record. It frames `Q=2/3` as a
stable setting under named dynamics classes, with physical partition/arrow
selection left as the next gate.
