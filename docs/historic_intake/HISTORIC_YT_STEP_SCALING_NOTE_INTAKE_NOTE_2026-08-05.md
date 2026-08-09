# Historic intake: y_t Step-Scaling: Non-Perturbative Gauge Crossover

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

Lattice step-scaling at g_bare = 1 (beta = 6) on L = 4, 6, 8, 12 gives <P> = 0.542/0.538/0.537/0.539 and alpha_V = 0.147/0.148/0.148/0.148 — nearly flat over a factor 3 in scale, a lattice beta function about 30x weaker than perturbative QCD, with the framework coupling crossing the SM trajectory near 10^3.5 GeV and a resulting m_t = 208 GeV (20.5% off).

Original verdict: BOUNDED, not closed — the route and mechanism (suppressed running, no Landau pole) are demonstrated but the number is not paper-grade.
Scope: Non-perturbative gauge-side handoff from the framework strong boundary (alpha_s(M_Pl)=0.073, ~3.9x the SM 0.019) to the perturbative SM trajectory.
Escape conditions (negative claims): Larger lattices (L = 16, 24, 32) for controlled continuum extrapolation and 100+ configurations per ensemble; a non-perturbative V-to-MSbar scheme conversion.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

April step-scaling: alpha_V flat over a factor 3 in scale (suppressed running mechanism real) WITH the honest 20.5%-off m_t = 208 GeV flag.

## Provenance (pinned)

- Original path: `docs/YT_STEP_SCALING_NOTE.md`
- Source commit: `206c63374a99bb68f591245d74a587b7523f42bb`
- git blob: `e535e2977e6b66516f8083cb2f9488ed6ef55da8`
- sha256: `c6d4fd84a7b1efd7a80f5a189973ad8b11a89f08ef930df6236d1cae5080b35e`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch08/2455_YT_STEP_SCALING_NOTE.md](../../archive_unlanded/historic_intake_originals/branch08/2455_YT_STEP_SCALING_NOTE.md)
- Lines: 140; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_step_scaling​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Quantitative prediction m_t = 208 GeV is 20.5% off PDG and rests on 8 configs at L<=12; the note itself labels this BOUNDED, so no overclaim in text, but the number should not be cited as a framework prediction.
- Supersession (as known at extraction): April-era gauge-side lane, distinct from the May PR #230 scalar/LSZ lane; its self-listed bounds (finite volume, statistics, integration model dependence, scheme matching) are unresolved.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
