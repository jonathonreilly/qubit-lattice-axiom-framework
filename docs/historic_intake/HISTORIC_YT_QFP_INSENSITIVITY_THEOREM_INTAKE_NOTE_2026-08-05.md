# Historic intake: y_t Quasi-Fixed-Point Insensitivity Theorem

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pre_seeding_mainline_deleted
Era: april_pre_reset — dated 2026-04-14; g_bare = 1 as axiom, with an import table classifying each element

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Answers the objection that the SM EFT is the wrong theory above v by proving the backward Ward prediction y_t(v) = 0.973 is insensitive to which RG flow is used: Pendleton-Ross focusing gives a focusing ratio R = 1.09 over y_t(M_Pl) in [0.2, 0.8] and R = 1.98 over the upper half, with local sensitivity dy_t(v)/dy_t(M_Pl) = 0.90, so a 10% shift near the Ward value 0.436 produces only a 4.0% shift in y_t(v). Sensitivity budget: +/-3% beta coefficients gives <3%, +/-10% gives <8%, +/-20% b_3 alone <8%, 2-loop truncation ~2.4%; g_1, g_2 and lambda variation contribute <3.7%, <7.4% and <0.03%. Prediction m_t = 169.4 GeV with ~3% systematic from the RG-flow choice.

Original verdict: y_t(v; SM RGE) = y_t(v; lattice) + O(3%), so the Codex blocker is correct about the physics above v but not relevant to the backward Ward prediction.
Scope: Formal theorem over a family of smooth RG flows on [v, M_Pl] satisfying a gauge anchor alpha_s(v) = 0.1033, the Ward BC y_t(M_Pl) = 0.436, and a focusing structure with c_3 > c_self > 0; the note explicitly does NOT claim the SM RGE is the physical description above v, only that it is a valid interpolation.
Escape conditions (negative claims): The insensitivity holds for trajectories ABOVE the quasi-fixed point; below the QFP sensitivity is near 1:1, and the note relies on the Ward BC being a derived quantity whose uncertainty is bounded by Ward-identity precision rather than the full scan range. The focusing structure is claimed structural (depending only on signs and relative magnitudes of beta coefficients, not their values).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The quasi-fixed-point insensitivity theorem (y_t(v) RG-flow-insensitive above the QFP, honest asymmetry flag) — theorem-grade and load-bearing for the mass lane's boundary story.

## Provenance (pinned)

- Original path: `docs/YT_QFP_INSENSITIVITY_THEOREM.md`
- Source commit: `26fce6c2741b5ef4760ec26c9867b30ffa161c30`
- git blob: `bb55da54896839ed02ce670d8d0ca8b01e9fe640`
- sha256: `27e521ca0c5fc65ce2c100c61d714d6687abc5f4ba480fdad279c108ff57084f`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3619_YT_QFP_INSENSITIVITY_THEOREM.md](../../archive_unlanded/historic_intake_originals/recovery/3619_YT_QFP_INSENSITIVITY_THEOREM.md)
- Lines: 293; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_qfp_insensitivity​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: The claimed insensitivity is asymmetric — over the full range [0.2, 0.8] the focusing ratio is only R = 1.09 and y_t(v) spans 0.609 to 1.157 (m_t 106.0 to 201.5 GeV), so the bound depends on the Ward BC's own precision holding.
- Supersession (as known at extraction): Resolves a specific Codex blocker on the Boundary Selection Theorem's claim that the lattice theory (16 tastes) applies above v while the SM EFT applies below.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
