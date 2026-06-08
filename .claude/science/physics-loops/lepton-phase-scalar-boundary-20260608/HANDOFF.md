# Handoff

This PR repairs `lepton_phase_modulus_separation_no_go_2026-06-06`.

Science change:

- The exact `e1/e2/e3` phase/modulus separation is preserved.
- The old universal scalar-action no-go is demoted.
- The runner now verifies that `Im z^3` is a legal `C3` invariant and that a
  general real scalar can stationarize a supplied `delta=2/9` target.
- The runner also verifies that the even/spectral `W_X=0` branch can target the
  supplied phase.
- The surviving no-go is only the nondegenerate even/spectral branch
  `W_X != 0`, which forces `delta=n*pi/3` and excludes `delta=2/9`.

Verification:

```text
python3 scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py
python3 scripts/cached_runner_output.py --check-only scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py
python3 -m py_compile scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py
git diff --name-only -- docs/audit
```

No audit files are modified.
