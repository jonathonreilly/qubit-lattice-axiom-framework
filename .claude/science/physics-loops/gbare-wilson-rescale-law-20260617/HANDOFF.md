# Handoff

Branch: `physics-loop/gbare-wilson-rescale-law-20260617`

This block adds a Wilson-action generator-rescaling boundary theorem. It
separates three exact laws:

- fixed component field under `T_a -> cT_a`: `beta_new/beta_old = 1/c^2`;
- pure basis relabeling: beta unchanged;
- coupling-coordinate WM route `g -> g/c`: `beta_new/beta_old = c^2`.

The original `g_bare` rescaling row remains Gram-only. The beta arithmetic row
now consumes only the coupling-coordinate WM route and explicitly does not
claim `c^2` as fixed-component Wilson compensation.

Checks to rerun:

```bash
PYTHONPATH=scripts python3 scripts/frontier_wilson_action_generator_rescaling_beta_transformation_2026_06_17.py
PYTHONPATH=scripts python3 scripts/frontier_beta_gbare_squared_rescaling_invariance.py
PYTHONPATH=scripts python3 scripts/frontier_g_bare_rescaling_conditional_algebra_check.py
```

No audit files were intentionally edited.
