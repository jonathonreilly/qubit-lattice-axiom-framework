# Historic intake: y_t Gate: Zero-Import Closure via Hierarchy + Vertex Matching

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded
Stratum: pre_seeding_mainline_deleted
Era: april_pre_reset — dated 2026-04-14; single axiom Cl(3) on Z^3 with g_bare = 1 canonical normalization

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Three observables from the single axiom Cl(3) on Z^3 with zero SM inputs: v = 246.3 GeV vs 246.22 observed (+0.03%), alpha_s(M_Z) = 0.1182 vs 0.1179 (+0.3%), and m_t = 165.4 GeV vs 172.69 (-4.2%). The structural insight is that hierarchy and gauge coupling are the same physics from one number <P> = 0.5934: v/M_Pl = alpha_LM^16 uses one u_0 per link (det route) while alpha_s(v) = 4*pi*alpha_LM^2 = 0.1033 uses two u_0 per vertex (Lepage-Mackenzie), so the 17 decades between M_Pl and v are bridged by the hierarchy theorem, not by running.

Original verdict: The y_t gate is BOUNDED with three honest readings: zero-import m_t = 165 GeV (-4.2%), one-import m_t = 173 GeV (+0.1%) using observed alpha_s(M_Z), and structural m_t ~ v/sqrt(2) = 173.3 GeV (+0.4%).
Scope: BOUNDED, 12/12 PASS, zero external inputs; bounded uncertainties itemized as <P> lattice artifacts ~0.1%, 2-loop QCD running ~1%, 1-loop y_t RGE over 17 decades ~5% (the m_t bottleneck), threshold matching ~1%, scheme matching ~3%.
Escape conditions (negative claims): The -4.2% m_t residual is attributed to the 1-loop y_t RGE systematic over 17 decades (~5%), with the named fix being a 2-loop y_t RGE; the zero-import chain explicitly trades 4.2% accuracy for zero imports where the 1-import chain trades one observed input for 0.1% accuracy.

## Why pulled (supervisor decision, on the record)

The zero-import closure claim (v +0.03%, alpha_s +0.3%, m_t -4.2%) WITH the red flag that three m_t readings are presented as all honest — the mass-lane era flagship, pulled for audit with its own contradictions attached.

## Provenance (pinned)

- Original path: `docs/YT_ZERO_IMPORT_CLOSURE_NOTE.md`
- Source commit: `8912465c3f919075b667d5490b74f23f228f6a46`
- git blob: `91a586b6e624775262143c5635fb1a3f5f38a75e`
- sha256: `e08670791b88921a901b4f5da192ff625da7d481ca32eb74d817c0326e235fca`
- Lines: 107; runners named: scripts/frontier_zero_import_chain.py

## Attached evidence (registered with, not as, this claim)

- `docs/YT_FLAGSHIP_CLOSURE_NOTE.md` — Gate decomposition naming the single upgrade computation (2-loop V-scheme matching); rides the closure claim.

## Cross-stratum flags

- Cross-stratum reference from branch01 idx 40 (`docs/ADVERSARIAL_CHAIN_AUDIT_2026-04-13.md`, decision PULL) — Hostile chain audit: the y_t chain imports the observed v = 246 GeV (HIGH severity) + g_* inconsistency (106.75 vs 110.75) — direct adverse evidence against the pulled zero-import closure claim; audit lane needs both sides.

## Flags carried

Presents three different m_t readings (165.4, 173, 173.3 GeV) as all honest and well-supported without selecting one; the zero-import value is the worst match to observation.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
