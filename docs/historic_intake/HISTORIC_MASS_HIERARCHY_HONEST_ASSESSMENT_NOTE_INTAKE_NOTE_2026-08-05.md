# Historic intake: Mass Hierarchy: Honest Assessment of the Strongest Paper-Safe Claim

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

The zero-parameter prediction m_t/m_u ~ 3 x exp(0.173 x 39) x 39 ~ 12,000 against observed ~75,000: log_10 predicted 4.1 vs observed 4.87, a 0.8-decade (factor ~6, ~16% on the log) discrepancy with the U(1) proxy. The SU(3) Casimir raises Delta(gamma)_13 to 0.286 (log 5.5) and with non-perturbative confinement to 0.333 (log 6.2), so the observed 4.87 lies inside the [4.1, 5.5] band.

Original verdict: The strongest honest phrasing is that the zero-parameter prediction reproduces the exponent to within 16% (the ratio to within a factor of 6); the recommended paper claim is the ~2-decade band log_10(m_t/m_u) in [3.5, 5.5] bracketing 4.87, explicitly not a precision test.
Scope: BOUNDED — the mechanism is structural and zero-parameter but the numerical output depends on a U(1) proxy for SU(3) and a strong-coupling model that is not first-principles.
Escape conditions (negative claims): Upgrading to closed requires a first-principles SU(3) calculation replacing the strong-coupling model and U(1) proxy.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The mass-hierarchy honest synthesis: exponent reproduced to 16% (0.8 decades short), mechanism real, band ~2 decades — with instructions against overclaiming.

## Provenance (pinned)

- Original path: `docs/MASS_HIERARCHY_HONEST_ASSESSMENT_NOTE.md`
- Source commit: `123915eb68febdd5783f0d751876a0b40a8dc7eb`
- git blob: `297c58898604c9a1f0e679d418990826e5f2f0c5`
- sha256: `a229b1dde03329f9148de80d75caa096f4aaa5d5a3ec5c7ce5d5d14c446fabcd`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1132_MASS_HIERARCHY_HONEST_ASSESSMENT_NOTE.md](../../archive_unlanded/historic_intake_originals/branch04/1132_MASS_HIERARCHY_HONEST_ASSESSMENT_NOTE.md)
- Lines: 288; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_mass_hierarchy_synthesis​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_mass_hierarchy_su3​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_mass_hierarchy_rg​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/MASS_HIERARCHY_RG_NOTE.md` — Two-loop narrowing; blocking measurement uncertainty flagged.
- `docs/MASS_HIERARCHY_SU3_LATTICE_NOTE.md` — Lattice Casimir-enhancement test.
- `docs/MASS_HIERARCHY_SU3_NOTE.md` — SU(3) proxy correction (65%).
- `docs/MASS_SPECTRUM_NOTE.md` — Three-of-four mechanisms fail.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Warns the band is ~2 decades wide and explicitly instructs not to claim precision; the band width reflects model dependence.
- Supersession (as known at extraction): Synthesis/assessment over MASS_HIERARCHY_RG, MASS_HIERARCHY_SU3, MASS_SPECTRUM, EWSB_GENERATION_CASCADE and GENERATION_GAP_CLOSURE; no new scripts run.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
