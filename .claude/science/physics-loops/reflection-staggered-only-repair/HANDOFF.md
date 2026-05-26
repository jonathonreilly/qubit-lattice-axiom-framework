# Handoff

This branch repairs the critical reflection-positivity row by narrowing its
source theorem to the staggered-only action surface.

Key outcome:

- `axiom_first_reflection_positivity_theorem_note_2026-04-29`
  - before: `audited_conditional`
  - after pipeline: `unaudited`
  - ready: true
  - descendants: 887
  - open dependency paths: none

What changed:

- removed the load-bearing Wilson-fermion Case B from the parent theorem;
- cited only the retained Case A determinant theorem and retained_bounded
  gauge-half theorem;
- changed the registered runner so E1-E5 are binding and E6 is diagnostic;
- regenerated audit/publication derived views mechanically.

Verification commands:

```bash
python3 scripts/axiom_first_reflection_positivity_check.py
python3 scripts/staggered_only_det_positivity_case_a_2026-05-17.py
bash docs/audit/scripts/run_pipeline.sh
```

Next exact action after PR creation:

```bash
git fetch origin
```

Then select the next critical audited-conditional row, starting with
`strong_cp_theta_zero_note` unless main has changed the queue.
