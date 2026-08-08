# Historic intake: Write-Up: Decoherence Mechanisms in the Discrete Event-Network Model

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: march_2026_event_network_era
Era: march_event_network — cites Axiom 9 ('measurement is durable record formation that separates alternatives'); linear path-sum on a causal DAG

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Of four candidate decoherence mechanisms only two produce any visibility change: sector labels give exactly V_0(1-p), symmetric and asymmetric delay-field distortion give V unchanged, and topological DAG shortcuts give non-trivial V(p) that can INCREASE visibility (far-slit amplitude share rising from 16.5% to 50.2% at y=3 as pruning removes 81 edges and adds 39, net -42).

Original verdict: Interference = topology, gravity = field: for a record mechanism to decohere in this model it MUST change the causal DAG topology, so Axiom 9's 'separation' has to be topological rather than a path label.
Scope: Two-slit setup on a fixed causal DAG; the structural principle is argued from the phase sweep covering all relative phases and visibility being invariant to field-induced amplitude rescaling.
Escape conditions (negative claims): The 'field perturbations cannot decohere' negative rests on three stated conditions — the phase sweep already explores all relative phases, visibility (max-min)/(max+min) is invariant to path-independent amplitude rescaling, and the DAG is held fixed; the escape is any change to path EXISTENCE. The note also asks openly whether the principle is a consequence of the linear path-sum and would survive a nonlinear generalization.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The structural principle: in a linear path-sum on a fixed DAG, records must change topology to decohere (phase-sweep + rescaling-invariance argument); wrapper must carry the 3137 correction caveat on its shortcut row and the open linearity question.

## Provenance (pinned)

- Original path: `.claude/science/write-ups/decoherence-arc-2026-03-30.md`
- Source commit: `a9da85f9ec5a788d80011748f85edea5a3763f69`
- git blob: `3a1e901a0a5a586fbe6ac5cc690b8071c7471f41`
- sha256: `be5f569723b0392391b435fa149c02e8df9e89c4ce12d0b9f1e4fa85317aee07`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/march/3164_decoherence-arc-2026-03-30.md](../../archive_unlanded/historic_intake_originals/march/3164_decoherence-arc-2026-03-30.md)
- Lines: 45; runners named: none

## Attached evidence (registered with, not as, this claim)

- `.claude/science/analyses/topological-decoherence-2026-03-30.md` — Known-buggy implementation corrected by 3137; predecessor evidence.
- `.claude/science/analyses/topological-decoherence-corrected-2026-03-30.md` — Corrected non-trivial decoherence curve; quantitative evidence for the decoherence-arc principle, not a standalone row.
- `.claude/science/sanity/topological-decoherence-2026-03-30.md` — Audit evidence (edge-pruning explanation of the V increase).

## Flags carried

Lists as open whether the model can produce GENUINE decoherence (V monotonically decreasing) at all; its topological-shortcut result is the one whose implementation was later corrected (idx 3137).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
