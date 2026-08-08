# Historic intake: Write-Up: Interference Regime of the Discrete Event-Network Toy Model

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: march_2026_event_network_era
Era: march_event_network — rectangular-grid causal DAG, source at (1,0), barrier at x=w/2 with slits at y=+/-s

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Six experiments over >25,000 path-sum evaluations establish that off-center visibility is governed by a topological threshold — exactly zero when the causal DAG admits paths through only one slit (6/6 zero-V cases single-slit, 4/4 nonzero both), jumping discontinuously to 0.004-0.875 at R_c(y) ~ 0.25|y| + 1.0 (1.25, 1.50, 1.75, 2.25 at y = 1, 2, 3, 5) — while record mode gives V=0.0000000000 everywhere and partial records give exactly V_0(1-p).

Original verdict: Status COMPLETE — promoted to canonical main; the interference regime shows three distinctly discrete-network features (topological threshold, discontinuous onset, y-dependent R_c) with no continuum analogue.
Scope: Standard path-sum over the causal DAG with phase_per_action=4.0, attenuation_power=1.0, no persistent nodes; six sweeps totaling ~1,152 + 20,160 + ~44,000 + 10 + ~5,040 + ~31,752 evaluations.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Era-consolidated interference claim (>25k evaluations; topological threshold, discontinuous onset, y-dependent R_c) carrying its own adverse validation rows — the era's canonical positive result, honest caveats included.

## Provenance (pinned)

- Original path: `.claude/science/write-ups/interference-regime-2026-03-30.md`
- Source commit: `c5c1745479599c85567e6500d57fd395702396c5`
- git blob: `1e8ae1b530626808ff4ebf52be3127532ae94232`
- sha256: `83e2615942d6bb15103bdfa128f2c61b440e4591f46d37cd749272be72da1055`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/march/3165_interference-regime-2026-03-30.md](../../archive_unlanded/historic_intake_originals/march/3165_interference-regime-2026-03-30.md)
- Lines: 96; runners named: historic runner (unpinned, not in this packet): `interference_geometry_sweep(.py)`; historic runner (unpinned, not in this packet): `interference_offcenter_fringe_sweep(.py)`; historic runner (unpinned, not in this packet): `interference_critical_ratio_sweep(.py)`; historic runner (unpinned, not in this packet): `interference_slit_reachability_audit(.py)`; historic runner (unpinned, not in this packet): `interference_asymmetric_sweep(.py)`; historic runner (unpinned, not in this packet): `interference_partial_record_sweep(.py)`

## Attached evidence (registered with, not as, this claim)

- `.claude/science/analyses/asymmetric-interference-2026-03-30.md` — Artifact-kill evidence consolidated into the interference-regime write-up; not a standalone claim.
- `.claude/science/analyses/interference-geometry-sensitivity-2026-03-30.md` — Own sanity audit ruled SUSPICIOUS: contrast=1 is setup symmetry, wrong observable; the honest record survives in the regime write-up's validation table.
- `.claude/science/analyses/interference-offcenter-fringe-2026-03-30.md` — Threshold evidence consolidated into the regime write-up.
- `.claude/science/analyses/irregular-network-2026-03-30.md` — Robustness evidence (topological features survive irregularity); consolidated.
- `.claude/science/analyses/partial-records-2026-03-30.md` — Own sanity audit: 'confirmed a tautology' — exact linear law follows from the amplitude-splitting rule; evidence attachment only.
- `.claude/science/sanity/asymmetric-interference-2026-03-30.md` — Audit evidence.
- `.claude/science/sanity/interference-geometry-sensitivity-2026-03-30.md` — The SUSPICIOUS ruling that redirected the lane to the right observable; audit evidence.
- `.claude/science/sanity/interference-offcenter-fringe-2026-03-30.md` — Audit evidence.
- `.claude/science/sanity/partial-records-2026-03-30.md` — Audit evidence (tautology concession).

## Flags carried

Its own validation table carries the geometry sweep as SUSPICIOUS (center V=1 a symmetry artifact), flags that the monotonic trends may be a rectangular-grid regularity artifact, that R_c was fit from 4 points, and that the linear decoherence law is mathematically trivial rather than model-specific.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
