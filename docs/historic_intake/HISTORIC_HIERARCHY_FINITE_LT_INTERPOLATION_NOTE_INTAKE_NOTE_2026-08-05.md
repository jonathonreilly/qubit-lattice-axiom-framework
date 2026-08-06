# Historic intake: Hierarchy Finite-L_t Interpolation Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The exact APBC temporal normalization on the minimal hierarchy block has a closed form for ALL finite L_t: A(L_t,u_0) = [1/(4 sqrt(3) u_0^2)] (1 - q^Lt)/(1 + q^Lt) with q = 2 - sqrt(3), recovering A_2 = 1/(8 u_0^2) and A_inf = 1/(4 sqrt(3) u_0^2); the observed prefactor C_obs = 246.22/253.4 = 0.971665351 lies on the same exact curve at L_t,eff = 3.177.

Original verdict: The temporal normalization family is exact and the observed prefactor is not ad hoc, but the hierarchy theorem is still not proved — the remaining gap is an exact finite-L_t order-parameter selection theorem.
Scope: Spatial-APBC minimal hierarchy block, small-m effective-potential coefficient Delta f = A(L_t,m) m^2 + O(m^4).


## Why pulled (supervisor decision, on the record)

Exact closed form for the APBC temporal normalization at ALL finite L_t — the prefactor family is not ad hoc; honest that it does not prove the theorem.

## Provenance (pinned)

- Original path: `docs/HIERARCHY_FINITE_LT_INTERPOLATION_NOTE.md`
- Source commit: `4680bce9bf11e4adc8794aaa67d73ea5accb7e9d`
- git blob: `c2ffa4659635128c827ea81ba6d3e5a15ce3800b`
- sha256: `91ae1ca8ba727256d18516ef30b211b7927d8bc4f3733bea8d308f2727648aca`
- Lines: 95; runners named: scripts/frontier_hierarchy_finite_lt_interpolation.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Note itself flags that it does not prove the hierarchy theorem and that the load-bearing L_t selection step remains open.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
