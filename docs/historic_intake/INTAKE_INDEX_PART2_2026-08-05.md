# Historic intake index, part 2 — branch09 + pack-family strata

Claim type: meta

Part 2 of the 2026-08-05 historic-science triage intake (part 1:
`INTAKE_INDEX_2026-08-05.md`, 622 wrappers). Same mechanism, same template,
same audit fields. Every wrapper is DATA: the supervisor's decision reason
verbatim, the extraction's claim compression, and a byte-exact provenance pin.

- Wrapper notes written: 159
- Machine manifest: `INTAKE_MANIFEST_PART2_2026-08-05.json`
- Audit-lane hazards from these strata (not wrappers):
  `triage decisions/packsci_hazards_for_audit_lane.md` (in the census worktree),
  shipped alongside as `HISTORIC_INTAKE_PART2_HAZARDS_2026-08-05.md`.

## Counts per stratum

| Stratum | Wrappers |
|---|---|
| branch09 | 26 |
| packsci01 | 42 |
| packsci02 | 33 |
| packsci03 | 30 |
| packsci04 | 9 |
| packsci05 | 19 |
| **total** | **159** |

## UNRESOLVED pins

none — original bytes were fetched and hashed for every wrapper.

## Review-loop regeneration (2026-08-08)

Every wrapper in this intake was regenerated through the corrected template
after review-loop iteration 1 (Sol, FIX_THEN_PROCEED): canonical `Claim type:`
headers with the historic taxonomy preserved as `historic_claim_class` (F1);
byte-exact archived originals under `archive_unlanded/historic_intake_originals/`
linked from each wrapper and sha256-verified fail-closed (F2); the Why-pulled
section marked provenance-not-authority with a non-evidentiary disclaimer
(F3/F6); historic runner names rendered inert and unlinked (F4); attach/cross
references to pulled wrappers rendered as relative links (F5); the Octopus
registry typed meta with its evidence base archived (F7); the hazards memo
given a meta header (F8); review flags added to the three affected packsci01
wrappers (F9/F10/F11); explicit subject lines under bare-code titles (F13).
Both manifests are byte-identical to the originally shipped pins; decision
reasons are untouched (sha256-verified). Generator:
`scripts/historic_intake_generate_2026_08_05(.py)` (extension split per the
F4 inert-name convention; this index is a meta surface and names no runner).
