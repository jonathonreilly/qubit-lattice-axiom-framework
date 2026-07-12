# Handoff

## Claim-state movement

The source note no longer claims that link factorization induces scalar
propagator scaling. It now proves an exact negative boundary for the explicitly
supplied map `G_prime = a G`. The paired runner enforces that scope in its
executable text contract. The downstream EW matching parametrization and its
runner now consume this only as a supplied scalar-propagator identity.

## Audit repair target

> missing_bridge_theorem: derive from the explicit lattice Dirac/EW-current
> construction how U -> u_0 V transforms G, or narrow the claim to the
> conditional algebraic statement assuming G_full = u_0 G_V.

This block executes the second action by making the scalar map an explicit
propagator-level premise and removing any link-level implication.

## Artifacts

- [source note](../../../../docs/YT_EW_M_RESIDUAL_NOTE_2026-05-02.md)
- [direct runner](../../../../scripts/yt_ew_m_residual_channel_check.py)
- [paired output](../../../../outputs/yt_ew_m_residual_channel_check_2026-05-02.txt)
- [downstream matching note](../../../../docs/EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md)
- [downstream runner](../../../../scripts/frontier_ew_current_matching_rule_no_go.py)
- [trace gate](TRACE_GATE.md)
- [claim-status certificate](CLAIM_STATUS_CERTIFICATE.md)
- [review history](REVIEW_HISTORY.md)

## Verification

```bash
python3 -m py_compile scripts/yt_ew_m_residual_channel_check.py \
  scripts/frontier_ew_current_matching_rule_no_go.py
python3 scripts/yt_ew_m_residual_channel_check.py
python3 scripts/frontier_ew_current_matching_rule_no_go.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Results: direct runner `6/6 PASS`; paired output byte-identical to a live run;
downstream runner `56` fatal checks passed and `0` failed; validation pipeline
queued the target at critical rank 40 and rendered its dispatcher target live
and ready; strict audit lint reported zero errors; generated audit authority
files were stripped after validation.

## Review disposition

Milestone review-loop disposition: `pass` after three iterations. The review
process does not assign an audit verdict.

## Imports retired

- Retired from the proof: `U -> u_0 V` implying `G_full = u_0 G_V`.

## Remaining physics gate

Derive the map on the propagator or correlator from the framework's explicit
lattice Dirac/EW-current construction. This is not needed to audit the narrowed
claim, but it is still needed for any broader CMT or physical matching claim.

## Exact next action

Submit `yt_ew_m_residual_note_2026-05-02` to the independent audit worker via
the verified live dispatcher target. The critical row requires
fresh-context-or-stronger review with cross-confirmation.

The branch-review N1-N8 preflight is recorded in
[`NO_GO_DISCIPLINE_CHECKLIST.md`](NO_GO_DISCIPLINE_CHECKLIST.md); it is not an
independent audit verdict.

## Proposed downstream weaving after audit

Do not weave these authority surfaces before independent audit. If the
narrowed claim is ratified, update:

- `docs/CANONICAL_HARNESS_INDEX.md:67` so the row names the common
  scalar-propagator negative boundary rather than a CMT link-factorization
  conclusion;
- `docs/publication/ci3_z3/DERIVATION_ATLAS.md:259` so it does not infer
  uniform propagator scaling from `U -> u_0 V`; and
- the generated effective-status atlas only through the audit pipeline, never
  by hand.
