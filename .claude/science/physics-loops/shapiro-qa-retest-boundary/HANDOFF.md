# Handoff

This PR repairs `shapiro_qa_retest_note` as bounded cache-backed QA:

- removes archived failed bridge dependencies from the live source note;
- replaces retained-confirmation language with bounded QA consistency;
- adds `scripts/shapiro_qa_retest_boundary.py` to check the phase-lag and
  static-discriminator caches together;
- records that phase-lag cache freshness is owned by the base phase-lag repair,
  while the static-discriminator cache is SHA-fresh and directly verified here.

Checks run:

- `python3 scripts/shapiro_qa_retest_boundary.py`
- `python3 scripts/cached_runner_output.py scripts/shapiro_qa_retest_boundary.py --refresh`
- `python3 -m py_compile scripts/shapiro_qa_retest_boundary.py`
- `git diff --check`

No audit loop was run, no audit data was edited, and no main landing was done.
