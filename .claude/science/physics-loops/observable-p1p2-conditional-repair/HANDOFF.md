# Handoff

This branch repairs `observable_principle_from_axiom_note` by narrowing the
source theorem to explicit P1+P2 conditional scope.

Key outcome:

- before: `audited_conditional`
- after pipeline: `unaudited`
- ready: true
- descendants: 723
- open dependency paths: none

What changed:

- P2 phase-blind scalar-generator selection is admitted, not claimed as
  runner-derived.
- The runner still verifies candidate phase-blindness and derives/checks P3/P4
  locally.
- The `v` comparator remains out of scope.

Verification:

```bash
python3 scripts/frontier_hierarchy_observable_principle_from_axiom.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md
git diff --check
```

Next exact action after PR:

```bash
git fetch origin
```

Then inspect `strong_cp_theta_zero_note`.
