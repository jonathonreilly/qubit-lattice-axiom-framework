# Historic intake: Top Yukawa from Z_3 Clebsch-Gordan Coefficients

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: open_gate
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Derives a Z_3 generation structure (cyclic permutation of the three spatial axes giving charges {0,1,2}, Higgs a Z_3 singlet via xi_5) and predicts y_t = 1.035 vs observed 0.994 and m_t = 180 GeV vs 173 GeV, both 4.2% off; script reports 12/12 tests PASS.

Original verdict: Numerical prediction 4.2% off, with self-listed limitations: the 2-loop correction factor 0.82 is approximate, the charm/up hierarchy is not captured, and the down-type/lepton base coupling g_0^d is a separate unfixed parameter.
Scope: What Z_3 Clebsch-Gordan coefficients determine: Yukawa texture (off-diagonal forbidden), tree-level universality, and the degenerate-Yukawa-plus-breaking-plus-IRFP mechanism — not the absolute scale g_0.
Escape conditions (negative claims): A full 2-loop RGE with threshold matching, plus higher-order Z_3 breaking for the light-generation hierarchy.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The Z3-Clebsch generation route: y_t = 1.035 vs observed (4.2% off) WITH the 12/12-PASS-framing flag — the independent April route in its honest form.

## Provenance (pinned)

- Original path: `docs/YT_Z3_CLEBSCH_NOTE.md`
- Source commit: `a43d30ac0bf3a1f5efe3e7b1b7ea062adeeb7bf0`
- git blob: `a3ce2e69a2375be96f343cae56617dbaffdd69e8`
- sha256: `778da74c1b9bc8f5b29df1df6eb0909356632413396542c196cbfd8caa25bc97`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch08/2501_YT_Z3_CLEBSCH_NOTE.md](../../archive_unlanded/historic_intake_originals/branch08/2501_YT_Z3_CLEBSCH_NOTE.md)
- Lines: 78; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_z3_clebsch​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Presents a 4.2%-off y_t/m_t prediction with 12/12 PASS framing; the 'cross-checks' (neutrino hierarchy, CKM smallness) are qualitative consistency statements, not independent verification.
- Supersession (as known at extraction): Independent April route to y_t distinct from the Ward and step-scaling lanes; not referenced by the May PR #230 chain.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_conjecture
intake_directive: owner_2026-08-05
```

Independent audit still required.
