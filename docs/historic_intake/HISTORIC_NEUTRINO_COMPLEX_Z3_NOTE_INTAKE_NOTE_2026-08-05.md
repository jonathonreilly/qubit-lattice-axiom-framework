# Historic intake: Complex Z_3 Breaking: Fixing delta_CP and Sum m_i Tensions

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

Allowing the Z_3-breaking parameter eps in M_R = [[A,0,0],[0,eps,B],[0,B,eps]] to be COMPLEX — as the Cl(3) algebra structure in the Z_3 eigenbasis requires — resolves both standing tensions: a phase phi ~ 50 degrees gives delta_CP ~ -103 degrees (vs the experimental hint -90) and Sum m_i ~ 122 meV (vs the previous 131 meV against a 120 meV DESI+CMB bound). The CP phase is traced to the imaginary Pauli matrix sigma_2 in Cl(3).

Original verdict: Numerically verified; the Jarlskog |J| ~ 6.5e-3 is about 5x below the maximum allowed ~0.033, which the note flags as either a prediction or a limitation of the minimal model.
Scope: Both tensions resolved, but the mass-sum fix is marginal — 122 meV is 1.3% above the bound, argued to be within its ~10% systematic uncertainty.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Complex-eps resolution of both standing tensions with |J| ~ 6.5e-3 predicted — the Z_3 neutrino repair, marginality flagged.

## Provenance (pinned)

- Original path: `docs/NEUTRINO_COMPLEX_Z3_NOTE.md`
- Source commit: `bf17ed280b6e8c05bcdb4f4b32c86b068b5d93ab`
- git blob: `821d75c4b9796d819a61ff8c50a2076ff779acce`
- sha256: `19d7b5bb060a5055dede55263e75f9795a5578844c65813a640cca215b71f0a1`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1183_NEUTRINO_COMPLEX_Z3_NOTE.md](../../archive_unlanded/historic_intake_originals/branch04/1183_NEUTRINO_COMPLEX_Z3_NOTE.md)
- Lines: 229; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_neutrino_complex_z3(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/NEUTRINO_HIERARCHY_DERIVED_NOTE.md` — Normal-hierarchy structural constraint with forbidden phrasings listed.
- `docs/NEUTRINO_MASSES_NOTE.md` — Two-parameter texture with named tensions and fitted inputs.

## Flags carried

The mass-sum resolution is marginal (still above the cosmological bound, rescued by claimed systematics) and the note leaves ~2 meV excess to be absorbed by RG running, higher-order seesaw corrections or thresholds.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement_numerically_verified_proposal
intake_directive: owner_2026-08-05
```

Independent audit still required.
