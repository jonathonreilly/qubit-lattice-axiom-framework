# Historic intake: Koide Cone — Anomaly-Forced 3+1 Cross-Species Attack Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The retained anomaly-forced 3+1 temporal surface is flavor-trivial on the hw=1 triplet: gamma_5 acts on spinor indices only, the RH singlet completion carries the same hypercharge in all three generations, all five anomaly traces vanish on the SM branch, and on every tested APBC block L_t in {6,8,12,16} the perturbed resolvent still commutes with all lattice translations, forcing K_ij = 0 for i != j.

Original verdict: ANOMALY_FORCED_MIXING_GENERATES_B=FALSE — the necessary step fails, so the Koide cone a_0^2 = 2|z|^2 remains unreachable on this attack surface and Agent 4's pure-APBC b = 0 no-go extends unchanged.
Scope: Rules out only the stand-alone anomaly-forced 3+1 cross-species propagator on a non-minimal temporal block (candidate 6 of the G5 successor list); symbolic in m_i, u_0, L_t, r, m_chi.
Escape conditions (negative claims): The obstruction is translation-character orthogonality on pure APBC: species pairs disagree on at least one translation axis, so any species-blind insertion leaves the kernel diagonal; the anomaly does carry a sector-SCALE signal (Q_L : L_L = -1/27 : 1 for Tr[Y^3]) but within a sector all three generations share Y, so escaping requires a mechanism that is not species-blind — e.g. Higgs VEV / Yukawa input, explicitly out of scope as G1 territory.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Flavor-triviality no-go: the anomaly-forced 3+1 surface cannot generate b != 0 (translation-character orthogonality) — escape named.

## Provenance (pinned)

- Original path: `docs/KOIDE_ANOMALY_FORCED_CROSS_SPECIES_NOTE.md`
- Source commit: `4c3906a20b8570e70a14c5b8d96fe6110647d003`
- git blob: `8ac7398232c8e76ae68a76e6f18482123c52dce1`
- sha256: `2f3cdf5f680aad8685c28c38290e5709eedbcede075ae017d90437272add6c24`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/755_KOIDE_ANOMALY_FORCED_CROSS_SPECIES_NOTE.md](../../archive_unlanded/historic_intake_originals/branch03/755_KOIDE_ANOMALY_FORCED_CROSS_SPECIES_NOTE.md)
- Lines: 298; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_koide_anomaly_forced_cross_species(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Internal date (2026-04-17) disagrees with the manifest creation date (2026-04-19).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
