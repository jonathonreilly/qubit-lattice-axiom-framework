# Historic intake: Claim Status Certificate - Cycle 7: Physical-Lattice Necessity Dep-Declaration Audit

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_correction
Stratum: pack_science_family
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

A DEMOTION packet: PHYSICAL_LATTICE_NECESSITY_NOTE.md was carrying proposed_retained with deps declared as EMPTY while its runner actually reads 11 upstream notes plus a sibling runner. Recommends explicit dep declaration and demotion to bounded support theorem. Runner PASS=34 FAIL=0; 301 transitive descendants inherit the corrected dep chain.

Original verdict: Demotion recommended; the deeper question of which upstream notes are load-bearing versus context is left open.
Scope: Dep-declaration correctness only.


## Why pulled (supervisor decision, on the record)

Demotion packet: docs/PHYSICAL_LATTICE_NECESSITY_NOTE.md carried proposed_retained with deps declared EMPTY while its runner actually reads 11 upstream notes; 301 descendants inherit. CROSS-LINK: this note is the load-bearing locality authority of the A_min-to-Q chain (idx 10256) - the demotion and the chain must be audited together.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/audit-backlog-campaign-20260502/cycle07-physical-lattice-necessity-audit/CLAIM_STATUS_CERTIFICATE.md`
- Source commit: `9ec0e48d22beb8f7bd1fc302af6e4c9b74ecc8f2`
- git blob: `7dac46fd370efe0f6de245f84ed6731f1fb584d5`
- sha256: `c07d18694ec7b76ecd1bcf311f91312b214727b4366c598b06aa71c746d5ebfb`
- Lines: 51; runners named: scripts/frontier_physical_lattice_necessity_dep_declaration_audit.py

## Attached evidence (registered with, not as, this claim)

- none

## Cross-stratum flags

- Attaches across strata to idx 10256 (`.claude/science/physics-loops/axiom-to-main-lane-cascade-20260429/PR_BODY_BLOCK01.md`, stratum packsci01) — Demotion packet: docs/PHYSICAL_LATTICE_NECESSITY_NOTE.md carried proposed_retained with deps declared EMPTY while its runner actually reads 11 upstream notes; 301 descendants inherit. CROSS-LINK: this note is the load-bearing locality authority of the A_min-to-Q chain (idx 10256) - the demotion and the chain must be audited together.

## Flags carried

A proposed_retained note with 301 descendants had declared ZERO dependencies while reading eleven upstream notes - a systemic dep-declaration failure mode.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
