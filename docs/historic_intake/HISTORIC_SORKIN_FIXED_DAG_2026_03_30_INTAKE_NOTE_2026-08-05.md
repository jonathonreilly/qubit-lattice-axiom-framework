# Historic intake: Analysis: Fixed-DAG Sorkin Test

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: march_2026_event_network_era
Era: march_event_network — path-sum with linear amplitude propagation on a fixed causal DAG

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

With the causal DAG held fixed (all barrier nodes present, amplitude zeroed at closed slits instead of removing nodes), the Sorkin parameter is zero to machine precision: max |I3|/|P_ABC| = 4.73e-16 (symmetric), 6.44e-16 (close), 2.56e-16 (wide), 4.22e-16 (asymmetric) — drops of 1e17 to 1e25 versus the original topology-changing test.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Machine-precision pairwise-only result PLUS the mechanism discovery: apparent Sorkin violations up to 1e9 x P in causal-DAG models are entirely topology reconfiguration; fixed-DAG protocol restores I3=0 exactly. Citable caution for discrete/causal-set interference tests. Sanity objection (linearity guarantees I3=0) goes in the wrapper caveat.

## Provenance (pinned)

- Original path: `.claude/science/analyses/sorkin-fixed-dag-2026-03-30.md`
- Source commit: `ae6269eca37448cc6f7a6a01b3cb58c3ad78f612`
- git blob: `a5dbb508c21322da7b5a611b5f6a17672e0e25f9`
- sha256: `dec62233266ac68963c1f64e2ee75f88224d8400fb2e8de4a399a1018a8d3db6`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/march/3132_sorkin-fixed-dag-2026-03-30.md](../../archive_unlanded/historic_intake_originals/march/3132_sorkin-fixed-dag-2026-03-30.md)
- Lines: 45; runners named: none
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/analyses/dag-reconfiguration-2026-03-30.md` — Quantifies the topology-reconfiguration mechanism behind the Sorkin resolution; evidence attachment.
- `.claude/science/analyses/sorkin-test-2026-03-30.md` — The ambiguous original the fixed-DAG note resolves; evidence attachment.
- `.claude/science/sanity/sorkin-fixed-dag-2026-03-30.md` — Audit evidence; linearity-guarantees-I3=0 objection goes in the wrapper caveat.
- `.claude/science/sanity/sorkin-test-2026-03-30.md` — Audit evidence (precision flags on the original).

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): BORN RULE CONFIRMED — the model has standard pairwise interference only, and the original I3 != 0 was entirely DAG reconfiguration with zero genuine higher-order interference.
- Extraction scope (triage compression; may reflect later context): Four slit configurations (-4,0,+4), (-2,0,+2), (-6,0,+6), (-4,+1,+6) with the DAG held fixed.
- Extraction escape conditions (negative claims; triage compression): The 'no higher-order interference' negative is stated to depend on holding the DAG fixed via amplitude-zeroing rather than node removal; the escape it identifies is topology change, where DAG reconfiguration reintroduces nonlinear coupling between slit configurations (the original I3 up to 4.6e9).
- Extraction red flags: none recorded
- Supersession (as known at extraction): Explicitly resolves the earlier AMBIGUOUS Sorkin test (idx 3133) by refining it to a fixed-DAG protocol.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
