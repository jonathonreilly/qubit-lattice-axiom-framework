# Historic intake: Gauge-Vacuum Plaquette Scalar-Bridge Theorem

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pre_seeding_mainline_deleted
Era: april_pre_reset — dated 2026-04-16

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Closes the insertion gap by four exact ingredients: the plaquette is exactly the source derivative of the unique additive local scalar generator W_loc(j) = log Z_1plaq(beta+j) - log Z_1plaq(beta); the scalar 3+1 bridge ratio is A_inf/A_2 = 2/sqrt(3); the plaquette density scales as P(u_0 V) = u_0^4 P(V) so only the fourth root Gamma_sc = (2/sqrt(3))^(1/4) preserves the four-link coupling map; and the incidence factor is 6/4 = 3/2. Hence P(beta) = P_1plaq(beta * (3/2) * (2/sqrt(3))^(1/4)), giving beta_eff = 9.329531846652698, P(6) = 0.593530679977098 and u_0 = 0.877729698485538.

Original verdict: The bridge theorem is closed; what remains is the repo-wide numeric migration from the historical same-surface value 0.5934 to the analytic value, a downstream implementation sweep rather than a theorem gap.
Scope: The 3+1 scalar route on the minimal APBC block; the uniqueness argument is that a one-link object carries a first root and a two-link object a square root, so only the plaquette's four link powers admit the fourth root.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The scalar-bridge theorem closing the plaquette insertion gap by four exact ingredients — with the pending numeric-migration caveat carried.

## Provenance (pinned)

- Original path: `docs/GAUGE_VACUUM_PLAQUETTE_BRIDGE_THEOREM_NOTE.md`
- Source commit: `37b57b4edbd3764ec7cc0da5b66625c783671589`
- git blob: `64b4a85734fa026fc27fe4ee9f51429c9a78d33a`
- sha256: `043159c86c6a869c490add886a6a67b065eefaddd8ef0061216b472c67baa535`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3610_GAUGE_VACUUM_PLAQUETTE_BRIDGE_THEOREM_NOTE.md](../../archive_unlanded/historic_intake_originals/recovery/3610_GAUGE_VACUUM_PLAQUETTE_BRIDGE_THEOREM_NOTE.md)
- Lines: 171; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_gauge_vacuum_plaquette_bridge_theorem(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_scalar_3plus1_temporal_ratio(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/GAUGE_VACUUM_PLAQUETTE_ANALYTIC_SUPPORT_NOTE.md` — The analytic support subtools + the named missing theorem the bridge then closes.

## Flags carried

Numeric migration on main still pending a dedicated rerun, so downstream lanes still carry the old 0.5934.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
