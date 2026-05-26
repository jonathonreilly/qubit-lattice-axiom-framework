# Review History

- Replaced the old hard-coded `MechanismVerdict` runner with a
  recomputation harness.
- Ran the mechanism certificate:
  `python3 -u scripts/poisson_self_gravity_mechanism.py` -> `PASS=26 FAIL=0`.
- Ran `bash docs/audit/scripts/run_pipeline.sh`; result: no errors, only the
  pre-existing Maradudin `conditional_repair_prefix` warning.
- Static runner hint now classifies this runner as class A rather than no
  class.
