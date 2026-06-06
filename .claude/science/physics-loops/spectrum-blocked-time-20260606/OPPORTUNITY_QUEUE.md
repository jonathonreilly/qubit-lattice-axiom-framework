# Opportunity Queue

After this PR, the best follow-up opportunities are downstream consumers of
the spectrum-condition formula. They should be handled in independent PRs only
when their transfer object is confirmed to be the same two-step `T_hat^2`.

1. Inspect `OSTERWALDER_SCHRADER_FROM_FRAMEWORK_NARROW_THEOREM_NOTE_2026-05-27.md`
   and `scripts/osterwalder_schrader_from_framework_runner_2026_05_27.py` for
   whether their generic `H = -(1/a_tau) log(T)` notation refers to a one-step
   transfer or to the repaired two-step spectrum-condition object.

2. Inspect `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
   and its runner for the same spacing convention.

3. Recheck KMS/Stefan-Boltzmann consumers only after the reviewer decides how
   the repaired spectrum-condition row should be woven.
