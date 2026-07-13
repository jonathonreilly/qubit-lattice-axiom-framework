## Science block

This block makes the strongest honest move on the missing derivation without
retyping the existing `single_axiom_information_note` meta identity.

- adds an exact scoped no-go under a separate polarity-safe claim identity;
- proves that neither `CF-add` nor `CF-norm` entails a single
  state-independent linear unitary dynamics on the stated finite state space;
- proves that even supplied linear Hilbert unitarity does not entail sparse or
  local generator support;
- proves the conditional positive boundary: finite complex Hilbert geometry +
  a linear differentiable norm-preserving one-parameter group gives a unique
  self-adjoint generator;
- preserves the original meta note and records that its positive derivation
  remains unclosed.

This is negative closure for two explicit formal semantics, not a positive
single-axiom graph-unitary derivation and not an exhaustive theorem about every
meaning of the English sentence. Independent audit is required before any
effective negative status is assigned.

## Trace

The block directly attacks the prior blocker:

> The missing step is a derivation that the verbal axiom uniquely or
> necessarily entails sparsity, Hermiticity, locality, and the specific
> Hamiltonian structure rather than defining them into H.

Trace classification: `direct_blocker_closure`, reachability
`partially_closes`, artifact role `no_go`. The scoped formal routes close
negatively; the undefined verbal semantics remain the sharply isolated
blocker.

## Artifacts

- [source no-go](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/single-axiom-information-no-go-block01-20260712/docs/SINGLE_AXIOM_INFORMATION_TWO_FORMALIZATIONS_NONFORCING_NO_GO_NOTE_2026-07-12.md)
- [paired runner](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/single-axiom-information-no-go-block01-20260712/scripts/frontier_single_axiom_information_two_formalizations_nonforcing_2026_07_12.py)
- [SHA-pinned runner output](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/single-axiom-information-no-go-block01-20260712/logs/runner-cache/frontier_single_axiom_information_two_formalizations_nonforcing_2026_07_12.txt)
- [trace gate](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/single-axiom-information-no-go-block01-20260712/.claude/science/physics-loops/single-axiom-information-closure-20260712/TRACE_GATE.md)
- [claim-status certificate](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/single-axiom-information-no-go-block01-20260712/.claude/science/physics-loops/single-axiom-information-closure-20260712/CLAIM_STATUS_CERTIFICATE.md)
- [review history](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/single-axiom-information-no-go-block01-20260712/.claude/science/physics-loops/single-axiom-information-closure-20260712/REVIEW_HISTORY.md)
- [handoff](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/single-axiom-information-no-go-block01-20260712/.claude/science/physics-loops/single-axiom-information-closure-20260712/HANDOFF.md)

## Verification

- `python3 scripts/frontier_single_axiom_information_two_formalizations_nonforcing_2026_07_12.py` — `PASS=20 FAIL=0`;
- independent manual/SymPy checks — Markov spectrum, norm-dependent rotation
  group law, complete-support spectrum/edge count, basis diagonalization, and
  generator signs agree;
- `python3 -m py_compile ...` — pass;
- SHA-pinned cache freshness — pass;
- `scripts/vocab_lint.py --fix` — zero violations;
- review-loop iteration 2 — pass across code/runner, physics boundary,
  imports, Nature-bar negative scope, labeling, N1-N8, and governance;
- disposable-worktree 16-stage audit pipeline + `audit_lint.py --strict` — no
  errors; new row seeded `no_go` / `unaudited`, queue-visible, paired runner
  attached, dependency `minimal_axioms`; original row remained `meta` /
  `unaudited`;
- `git diff --check`, portable-link gate, and pipeline-output-stripped gate —
  pass.

No generated audit ledger, queue, effective-status surface, audit verdict, or
repo-wide authority surface is included.

## Review and import disposition

Review ran two iterations. Seven consolidated findings were fixed: broad
English-semantics overreach, non-transfer phase witness, same-identity polarity
hazard, incorrect author audit-class wording, mutable runner-note cache input,
incomplete N1-N8 schema, and final evidence-locator drift.

No observation, fitted value, target value, unit convention, or literature
input is load-bearing. The positive route still needs Hilbert geometry, linear
time-group dynamics, a carrier basis, support semantics, and a locality rule.
The first two give the conditional reconstruction theorem; the remaining
three are not retired.

Loop: `single-axiom-information-closure-20260712`; major cycles: 2. Do not
merge this PR as part of the physics-loop run.
