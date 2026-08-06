# Historic intake: Alpha0 Transport Current-Surface No-Go

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Narrowed claim: current surfaces do not supply ALPHA0_TRANSPORT_RETAINED, ALPHA0_RETAINED, or RETAINED_ALPHA0_LOW_ENERGY_COULOMB. One-loop target surface alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) T_EM + Delta_match with T_EM = sum_f N_c(f) Q_f^2 log(M_Z/m_f^eff); the retained charge/count surface fixes only sum_f N_c(f) Q_f^2 = 8 and b_QED = (4/3)*8 = 32/3. Comparators (not proof inputs): alpha_EM(M_Z)^-1 = 127.67, alpha(0)^-1 = 137.035999084.

Original verdict: Support-only non-supply boundary; five of eleven contract inputs are explicitly missing (QED loop kernel, R-Lep, R-Q-heavy, R-Had-NP, scheme/decoupling matching).
Scope: The Lane 2 low-energy coupling input consumed by the static-source Rydberg lane.
Escape conditions (negative claims): Supply the five missing inputs plus owner ratification and audit acceptance; note that admitted literature R(s) is retained-with-import and does not satisfy the zero-import branch.

## Why pulled (supervisor decision, on the record)

Lane 2 terminal: alpha(0) transport not supplied — five of eleven inputs missing, the whole QED apparatus priced.

## Provenance (pinned)

- Original path: `docs/ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
- Source commit: `a750e4fdb1b4e8a0296a90db1cb51b74cf51b903`
- git blob: `c64c4c53e7172a7a21c182f5000532021e3f1429`
- sha256: `efcc8487b4e56e8bc4ddfdc60a14118f54d4b6130b6f06cac1ac6746b3efd863`
- Lines: 320; runners named: scripts/frontier_zero_import_hydrogen_alpha0_transport_current_surface_no_go.py

## Attached evidence (registered with, not as, this claim)

- `docs/ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` — Lane 2 member.
- `docs/ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md` — Lane 2 member.
- `docs/ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` — Lane 2 member.
- `docs/ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md` — Lane 2 member.
- `docs/ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md` — Lane 2 member.

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
