# Historic intake: Koide Loop Iteration 18 — I5: PMNS Sum Rules from Iter 4 Conjecture

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

The three iteration-4 formulas collapse into two sum rules — SR1 theta_13 = 2(theta_23 - pi/4) exactly, and SR2 Q sin^2 theta_12 + sin^2 theta_13 = delta at leading order (Q/3 = 2/9 = delta with O((delta Q)^4) ~ 5e-4 correction) — and SR2 holds within 1 sigma across all six NuFit releases (0.29-0.75 sigma), unlike TM1 (0.684 vs 0.667) and TM2 (0.294 vs 0.333).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The two PMNS sum rules: SR1 theta_13 = 2(theta_23 - pi/4) EXACT and SR2 at leading order — three coincidences become one relation; the structure behind the repo's live theta_23 falsifier.

## Provenance (pinned)

- Original path: `docs/KOIDE_PMNS_SUM_RULES_NOTE_2026-04-21.md`
- Source commit: `c29599d4d9f1b5b3aa281c088f71e3f2b32feadd`
- git blob: `e36f132e69f7b9ea4e31bc21461774be818a7cac`
- sha256: `a2c147d54d0248856e42c63eae7cfe8dac68eec02ec7bb43ec77c2ff2a20f086`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/888_KOIDE_PMNS_SUM_RULES_NOTE_2026-04-21.md](../../archive_unlanded/historic_intake_originals/branch03/888_KOIDE_PMNS_SUM_RULES_NOTE_2026-04-21.md)
- Lines: 124; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_koide_pmns_sum_rules​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/KOIDE_PMNS_DELTA_Q_DEFORMATION_NOTE_2026-04-21.md` — The original I5 conjecture (theta_13 = delta*Q etc.) — lineage of the live PMNS falsifier.
- `docs/KOIDE_PMNS_E_ROW_UNIQUENESS_NOTE_2026-04-21.md` — Why-the-e-row answered.
- `docs/KOIDE_PMNS_MASS_BASIS_FACTORIZATION_NOTE_2026-04-21.md` — Rotation factorization with residual coincidences flagged.
- `docs/KOIDE_PMNS_NEAR_TM1_STRUCTURE_NOTE_2026-04-21.md` — Soft-TM1 reading, retracted next iteration.
- `docs/KOIDE_PMNS_NUFIT_CROSS_VALIDATION_NOTE_2026-04-21.md` — NuFit robustness 4/6 releases; caveat stated.
- `docs/KOIDE_PMNS_ROTATION_AXIS_SYMBOLIC_NOTE_2026-04-21.md` — Complex-multiplication identity; sqrt5/2 'pure numerics' admitted.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Three apparent coincidences are one underlying relation plus an angle complementarity, making the derivation target a single equation instead of three coefficients.
- Extraction scope (triage compression; may reflect later context): Sum rules derived FROM the iteration-4 conjecture, not from first principles; SR2 is a leading-order relation.
- Extraction red flags: The sum rules inherit the conjectural status of iteration 4 — the iteration-24 critique notes their conservation reading is conditional on that conjecture being exact.
- Supersession (as known at extraction): Unifies the iteration-4 formulas; the resulting SR2 becomes the iteration-19+ derivation target and the iteration-21 'conservation law'.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
