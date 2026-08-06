# Historic intake: Derivation: Visibility Threshold R_c(y)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_theorem
Stratum: march_2026_event_network_era
Era: march_event_network — events as grid nodes; causal DAG edge A->B only if arrival_time(B) > arrival_time(A); barrier nodes blocked except at slits

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The off-center visibility threshold is derived exactly as R_c(y) = 1 + |y|/s (equivalently w >= 2(s + y_d)) from the grid causal DAG's maximum deflection of one vertical unit per horizontal step, matching the observed R_c = 1.25, 1.50, 1.75, 2.25 at y_d = 1, 2, 3, 5 for slit_half=4 at all four data points exactly.

Original verdict: Status CONFIRMED — the law R_c(y) = 1 + |y|/s is derived from the grid's causal DAG connectivity constraint, not fit from data.
Scope: Rectangular grid with nearest-neighbour plus diagonal links, source at (1,0), barrier at x=w/2 with slits at y=+/-s, detector at x=w; the derivation assumes max deflection per step is exactly 1.


## Why pulled (supervisor decision, on the record)

The era's one exact theorem: R_c(y) = 1 + |y|/s derived from DAG connectivity, 4/4 exact match, weakest link self-named (max-deflection-1 assumption). Attach 3114 (data), 3131 (mechanism), sanity audits.

## Provenance (pinned)

- Original path: `.claude/science/derivations/visibility-threshold-2026-03-30.md`
- Source commit: `c5c1745479599c85567e6500d57fd395702396c5`
- git blob: `fa79eae1242ecb6892e8010e8c901df4d0876bd2`
- sha256: `33245739623d554ff53090364dd79db402a7a6fbbef012d8720f3cb5ce77a4c0`
- Lines: 100; runners named: none

## Attached evidence (registered with, not as, this claim)

- `.claude/science/analyses/critical-ratio-2026-03-30.md` — The data the R_c(y) theorem derives exactly; evidence attachment.
- `.claude/science/analyses/slit-reachability-2026-03-30.md` — The topological mechanism (6/6, 4/4, exact zeros) behind the derived threshold; evidence attachment to the theorem.
- `.claude/science/sanity/critical-ratio-2026-03-30.md` — Audit evidence (4-point fit concession the theorem then discharges).
- `.claude/science/sanity/slit-reachability-2026-03-30.md` — Audit evidence incl. the cannot-cancel-at-all-phases argument.

## Flags carried

Names its own weakest link: Step 1's assumption of max deflection 1 per step depends on how build_causal_dag constructs the DAG — longer-range links (e.g. knight's-move) would lower the threshold.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
