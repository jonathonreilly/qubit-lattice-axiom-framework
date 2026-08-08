# Historic intake: Handoff (Lane 4 neutrino cascade)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_verdict
Stratum: pack_science_family
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Cycle 1 verified: current-stack mu_current = 0, the diagonal seesaw atmospheric benchmark requires a nonzero invertible M_R, and direct one-Higgs Dirac use of y_nu^eff gives GeV-scale rather than meV-scale mass, so no hidden global retained closure follows from combining them. Verification: new runner PASS=10 FAIL=0, majorana zero-law PASS=13, mass-derived PASS=19, observable-bounds PASS=35, audit pipeline complete and audit_lint --strict OK with only the known graph-cycle warning.

Original verdict: This no-go is verified but is NOT a Lane 4 closure; Lane 4 remains open.
Scope: Lane 4 checkpoint; a narrow compatibility fix was applied to the majorana zero-law runner after an origin/main fast-forward introduced Pfaffian/Nambu atlas rows.
Escape conditions (negative claims): Derive a nonzero Majorana primitive or a tiny Dirac Y_nu activation law.

## Why pulled (supervisor decision, on the record)

Lane 4 neutrino cycle-1 verdict: current-stack mu_current=0 verified, the diagonal seesaw atmospheric benchmark requires a nonzero invertible M_R, and direct one-Higgs Dirac use is excluded; escape named (derive a nonzero Majorana primitive or a tiny Dirac coupling). VERIFICATION-INTEGRITY FLAG: the authority runner was repaired mid-cycle because it gated on the literal string 'Pfaffian' rather than a computation. Lane family attached.

## Provenance (pinned)

- Original path: `.claude/science/frontier-workstreams/lane4-neutrino-cascade-20260427/HANDOFF.md`
- Source commit: `e1e041d5740b00b1c4b255a1fc7518bf6650a8e5`
- git blob: `1cdb0950ea113258ff478d25c23cd3a3e506a366`
- sha256: `2538a995fd89e800be2b0576afaa4f38b672916523621e9b57f1c20a82d6bd14`
- Lines: 61; runners named: scripts/frontier_neutrino_lane4_dirac_seesaw_fork_no_go.py, scripts/frontier_neutrino_majorana_current_stack_zero_law.py, scripts/frontier_neutrino_mass_derived.py, scripts/frontier_neutrino_retained_observable_bounds.py, docs/audit/scripts/run_pipeline.sh, docs/audit/scripts/audit_lint.py

## Attached evidence (registered with, not as, this claim)

- `.claude/science/frontier-workstreams/lane4-neutrino-cascade-20260427/ASSUMPTIONS_AND_IMPORTS.md` — Ten-row retained bank incl. mu_current=0 (the Majorana zero law) kept as the fork anchor.
- `.claude/science/frontier-workstreams/lane4-neutrino-cascade-20260427/GOAL.md` — Working judgment: Lane 4 not ready for retained quantitative closure; endpoint forked.
- `.claude/science/frontier-workstreams/lane4-neutrino-cascade-20260427/NO_GO_LEDGER.md` — Six closed neutrino routes, every row with an explicit reopen condition.
- `.claude/science/frontier-workstreams/lane4-neutrino-cascade-20260427/REVIEW_HISTORY.md` — Cycle-1 seven-stance review record; review-loop was EMULATED locally, not the owner lane - provenance flag for audit.
- `.claude/science/frontier-workstreams/lane4-neutrino-cascade-20260427/ROUTE_PORTFOLIO.md` — Six routes scored; the Dirac/seesaw fork guardrail selected.

## Flags carried

An authority runner was found to be checking for a literal string rather than the semantic condition - a fragile-gate defect of the kind that can produce false PASSes elsewhere.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
