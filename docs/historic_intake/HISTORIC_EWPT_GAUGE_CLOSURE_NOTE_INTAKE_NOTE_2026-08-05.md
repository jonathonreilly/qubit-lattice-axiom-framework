# Historic intake: EWPT Gauge Closure: v/T Unconditional Without Imported R Factor

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Three attacks replace the imported R = 1.5: a gauge-effective scalar MC on L = 12-32 gives v/T = 0.56 +/- 0.05 (above the 0.52 threshold), a monotonicity theorem floors v/T at the scalar-only 0.49, and a first-principles R_NP = 1.035 gives 0.507.

Original verdict: CLOSED - v/T >= 0.52 is established by Attack 1 with two independent analytic supports, leaving no conditional steps in the chain.
Scope: The remaining external input is the magnetic mass coefficient c = 0.3 from generic pure-SU(2) lattice studies (Hart et al. 2000), not 2HDM-specific.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The EWPT gauge-closure claim (v/T = 0.56 +/- 0.05 above threshold) WITH its own two-of-three-attacks-short flags — belongs beside the nucleation negative at audit.

## Provenance (pinned)

- Original path: `docs/EWPT_GAUGE_CLOSURE_NOTE.md`
- Source commit: `8bc730019cff4daf26bd7ac57ee9c12fe4e038fc`
- git blob: `9fd3650ba627ff6ee81e997dc45a43b15dca741c`
- sha256: `bdc90425d3dabd70062fc1228a2b5d81834419f825cce3bbb33cc9dfc8c7a152`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/443_EWPT_GAUGE_CLOSURE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/443_EWPT_GAUGE_CLOSURE_NOTE.md)
- Lines: 96; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_ewpt_gauge_closure(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_ewpt_lattice_mc(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_ewpt_strength(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_baryogenesis(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/EWPT_LATTICE_MC_NOTE.md` — MC measurement; headline depends on imported R = 1.5.
- `docs/EWPT_STRENGTH_NOTE.md` — 2HDM strength argument; two methods below threshold.

## Flags carried

Two of the three attacks (0.49 floor and 0.507) fall short of the 0.52 threshold; only the MC clears it, and c = 0.3 is still literature-supplied.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_closed
intake_directive: owner_2026-08-05
```

Independent audit still required.
