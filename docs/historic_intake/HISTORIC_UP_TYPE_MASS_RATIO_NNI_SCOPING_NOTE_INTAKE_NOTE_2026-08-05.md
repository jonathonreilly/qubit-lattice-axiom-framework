# Historic intake: Up-Type Mass Ratio — Phase 2 NNI Scoping Investigation (No-Go)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The combination of the promoted atlas CKM package, the bounded Phase-1 down-type ratios (m_d/m_s = alpha_s(v)/2, m_s/m_b = [alpha_s(v)/sqrt(6)]^(6/5)) and an NNI texture on M_u does not close the up-type extraction: the least-squares residual on the (x_u, x_c, phi_a) scan never falls below O(1e-3) over phi_a in [0, 2pi), and every package-native closed form for m_c/m_t misses the PDG comparator 0.00782 by >= 10% (closest is |V_cb|^(3/2) at +10.8%, an exponent with no promoted Casimir or anomalous-dimension origin).

Original verdict: Phase 2 does not close on the stated ingredients — the NNI system is generically over-determined once implicit U_d unitarity is counted, and the observed up-type exponent ~3/2 differs from the down-type 5/6 = C_F - T_F.
Scope: Current live package surface with the Fritzsch-seed M_d; no observed quark masses used as derivation inputs (provenance audit PASS).
Escape conditions (negative claims): Route A: relax the Fritzsch (1,1)=0 constraint on M_d to gain a second residual (a larger but still over-determined surface, unexplored). Route B: promote y_t so the up-sector exponent becomes (C_F - T_F + y_t^2/g_s^2 gamma_y)-like, which is the physically motivated route.

## Why pulled (supervisor decision, on the record)

NNI Phase-2 no-go: generically non-closing on the stated ingredients; two named routes.

## Provenance (pinned)

- Original path: `docs/UP_TYPE_MASS_RATIO_NNI_SCOPING_NOTE.md`
- Source commit: `9c0b9402073a7446f93d7239c6dc0b257b98c613`
- git blob: `dabce346fcdd732f26d573fb954f0fe27512fa0e`
- sha256: `32c5f5de679f5375719f204f4a32cdc85d33774a76fc9c50fe72c5b89d9da552`
- Lines: 143; runners named: scripts/frontier_mass_ratio_up_sector_nni_scoping.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
