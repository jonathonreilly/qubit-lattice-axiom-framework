# Review History

- Self-review: identified that the old runner's sampled `delta=-0.3` check was
  insufficient.
- Repair: added exact formula and branch tests.
- Verification: `PYTHONPATH=scripts python3 scripts/delta_sign_from_retained_mediator_runner.py`
  produced `TOTAL: PASS=20 FAIL=0`.

No review-loop was run in this block; the user has reviewer extraction running
separately.
