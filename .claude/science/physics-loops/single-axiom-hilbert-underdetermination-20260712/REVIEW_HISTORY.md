# Review history

## Review iteration 1

- Code/math: FAIL with five findings: missing `t>=0`, hard-coded readout
  fractions, label-only Cartesian product, incomplete CPTP/semigroup coverage,
  and non-verbatim output capture.
- Physics/import/Nature: two blockers: physical-selector nonuniqueness was
  worded as absence of any definable rule, and the high-in-degree existing ID
  could not safely be retyped to `no_go`.
- No-go/governance: N1/N4/N6/N7/N8 locators and path/status/mechanism records
  were incomplete.
- Fixes: split the existing bounded positive hub from a new leaf no-go; define
  one expansion signature; narrow the falsifier; add exact locators and
  cross-cycle tables; compute readout weights; certify Kraus completeness,
  Choi positivity, full-superoperator semigroup composition, and eight concrete
  expansions.
- Re-review disposition: pending.
- Independent audit: not run; audit authority remains outside this branch.

## Review iterations 2-3

- Code/math iteration 2 found one same-signature notation error (`U_t` versus
  the induced channel `mathcal U_t`); fixed and re-reviewed PASS.
- Physics/import iteration 2 found a citation-graph cycle, context links that
  would become dependencies, and a missing finite-dimension domain. All were
  fixed: both claim rows now depend only on `minimal_axioms`, the cross-row
  references are context-only code paths, and the domain is explicit.
- No-go discipline: N1-N8 PASS.
- Repo governance: PASS.
- Code/runner/math: PASS; independent SymPy/manual checks and byte-for-byte
  output comparisons passed.
- Physics boundary: same-path BOUNDED; leaf NO-GO.
- Imports: CLEAN.
- Nature retention review: meets the repo bar for independent audit.
- Final local review-loop disposition: PASS.

## Audit compatibility validation

- Disposable worktree commit: `fe1483f43`.
- Full 16-stage audit pipeline: PASS.
- `audit_lint.py --strict`: PASS with no errors; repo-wide legacy warnings and
  notices only.
- `single_axiom_hilbert_note`: `bounded_theorem`, `unaudited`, ready, high
  criticality, nine inbound edges, dependency `minimal_axioms` only.
- New selector no-go: `no_go`, `unaudited`, ready, leaf, zero inbound edges,
  dependency `minimal_axioms` only.
- No generated audit/effective-status output was copied to the science branch.
