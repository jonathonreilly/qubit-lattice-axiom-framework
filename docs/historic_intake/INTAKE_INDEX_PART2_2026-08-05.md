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

## Review-loop regeneration (2026-08-08, iterations 1 and 2)

Every wrapper in this intake was regenerated through the corrected template
after review-loop iterations 1 and 2 (Sol, FIX_THEN_PROCEED then confirmation):
canonical `Claim type:` headers with the historic taxonomy preserved as
`historic_claim_class` (F1); byte-exact archived originals under
`archive_unlanded/historic_intake_originals/` linked from each wrapper and
sha256-verified fail-closed (F2); the Why-pulled section marked
provenance-not-authority with a non-evidentiary disclaimer (F3); every
rendered field display-neutralizes `.py` tokens with a zero-width split so
no current-tree runner can bind, with the byte-exact wording pinned in the
triage JSONLs and archived originals (F4); markdown links (deps edges) only
for attachment relations — contradiction/cross-flag relations are inert text
plus machine-readable `contradicts:`/`cross_reference:` yaml lists, with
named non-pulled evidence archived byte-exact (F5); extraction-time
commentary split into a clearly-attributed Triage-extraction-notes section
(F6); the Octopus registry typed meta with its evidence base archived (F7);
the hazards memo given a meta header plus a pinned archived evidence base
(F8); review flags on the three affected packsci01 wrappers (F9/F10/F11);
bare-code H1 titles rewritten with the explicit scientific name as the
heading — per vocab_lint's `legacy_alias_strip` rule no alias parenthetical
is kept, and the historic token survives in the Explicit-subject line, the
wrapper filename, and the pinned original (F13). Historical NEGATIVE
claims register as `bounded_theorem` (historic_claim_class keeps the
historic taxonomy; no live no-go is asserted by any wrapper — no-go
discipline applies at audit adjudication), and wrapper FILENAMES neutralize
no-go/obstruction/firewall tokens (NO_GO/NOGO->NEGATIVE,
OBSTRUCTION->OBSTRUCTED_ROUTE, FIREWALL->ROUTE_BARRIER) so no registration
wrapper is a no-go-named artifact; archived originals containing
era-absolute markdown links carry a `.frozen` filename suffix (bytes
unchanged). Manifests are identical to the shipped pins except the `file`
field, which records the neutralized filename; decision reasons are
byte-untouched in the triage JSONLs (sha256-verified). Generator:
`scripts/historic_intake_generate_2026_08_05` (a `.py` program; name
rendered without extension for graph hygiene on this meta surface).
