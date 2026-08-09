# Historic intake: Direct Top Mass from Lattice Propagator Pole

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

Registered as a bounded registration of a historical negative claim; no live no-go is asserted by this wrapper — no-go discipline applies at audit adjudication.

## The claim (as stated by the original, supervisor-compressed)

The free staggered Hamiltonian at the hw=1 corner k = (pi,0,0) has all eight eigenvalues degenerate at E = 2r, so with r = 1 the bare mass is 2 M_Planck ~ 2.4e19 GeV and m_t/m_bare ~ 7e-18 — the bare mass IS the cutoff. Attempts to skip the RGE fail: the 1-loop CW potential has lambda_eff < 0 (unbounded below, no stable vacuum at v = 246), the naive ratio at M_Z gives m_t ~ 73 GeV (off by 2.4x), and CW dimensional transmutation gives v ~ 1e7 GeV.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The Planck-degeneracy fact: all eight corner eigenvalues at 2 M_Pl — you cannot skip the RGE; kills the direct-readout dream exactly.

## Provenance (pinned)

- Original path: `docs/YT_DIRECT_POLE_NOTE.md`
- Source commit: `fb4d882b586b3983f9cc6a2db7fe4f97eed84ab0`
- git blob: `e5b5cd454f8d23b9757aad7471953140a65e0588`
- sha256: `c7a3d6b76129218aab9e4dfb5d8908aa9f58703dcfdc8bb435a3fdf8ec8e413a`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2175_YT_DIRECT_POLE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2175_YT_DIRECT_POLE_NOTE.md)
- Lines: 78; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_direct_pole​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): You cannot skip the RGE — the lattice pole lives at the Planck scale and bridging to 173 GeV requires either the existing RGE chain or a non-perturbative hierarchy mechanism; the CW mechanism alone needs tuned bare parameters.
- Extraction scope (triage compression; may reflect later context): Free staggered propagator pole plus 1-loop CW with SM couplings at Lambda = M_Planck.
- Extraction escape conditions (negative claims; triage compression): A non-perturbative mechanism generating the full hierarchy is the named alternative to the RGE route.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Negative result confirming the lattice -> Cl(3) ratio -> alpha_V -> RGE chain as the minimal path; consistent with the V-lane finding at idx 2105 that CW crossover lands far above the EW scale.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
