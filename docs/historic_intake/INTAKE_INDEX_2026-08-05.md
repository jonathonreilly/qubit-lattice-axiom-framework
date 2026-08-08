# Historic intake index — 2026-08-05

Claim type: meta

Assembly of the 2026-08-05 historic-science triage PULL decisions into intake
wrapper notes. Every wrapper is DATA: it carries the supervisor's decision reason
verbatim, the extraction's own claim compression, and a byte-exact provenance pin.
No keep/discard judgment was made or altered during assembly.

- Wrapper notes written: 621
- Era registries written: 1
- Machine manifest: `INTAKE_MANIFEST_2026-08-05.json`

## Counts per stratum

| Stratum | Wrappers |
|---|---|
| branch01 | 106 |
| branch02 | 129 |
| branch03 | 66 |
| branch04 | 77 |
| branch05 | 55 |
| branch06 | 47 |
| branch07 | 60 |
| branch08 | 39 |
| march | 8 |
| octopus | 1 |
| recovery | 34 |
| **total** | **622** |

## UNRESOLVED pins

none — original bytes were fetched and hashed for every wrapper.

## Slug collisions

none — every pull produced a distinct slug.

## Decision rows with no matching extraction row

none — every PULL decision matched an extraction row.

## Cross-stratum flags

- branch01 idx 40 (`docs/ADVERSARIAL_CHAIN_AUDIT_2026-04-13.md`, decision PULL) -> idx 3620 (`docs/YT_ZERO_IMPORT_CLOSURE_NOTE.md`, stratum recovery)
- branch01 idx 237 (`docs/CODEX_DM_RESPONSE.md`, decision LEAVE) -> idx 3594 (`docs/DM_CLEAN_DERIVATION_NOTE.md`, stratum recovery)

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

Independent audit still required for every note listed here.
