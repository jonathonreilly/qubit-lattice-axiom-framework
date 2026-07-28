# Koide Q-delta linking-relation dependency classification (2026-05-17)

**Date:** 2026-05-17

**Claim type:** meta
**Status:** source-side metadata recording one dependency-classification measurement
for the parent note.
**Claim scope:** records whether the one historical co-cycle dependency named
for `koide_q_delta_linking_relation_theorem_note_2026-04-20` still appears in
that parent.

**Audit boundary:** this source note does not set or predict an audit outcome.
The independent audit lane owns any later classification or verdict.

## 1. Programmatic classification

Each of 1 named co-cycle deps was checked by case-insensitive substring search against the parent note (`docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md`). Classification heuristic:

- **NOT-CITED**: zero substring hits (programmatically certain)
- **CITED-INFORMATIONAL**: cited in Cross-references / See-also / Lane context / Background / Audit-dependency-repair-links sections (heuristic by section heading)
- **CITED-LOAD-BEARING**: cited in Proof / Theorem / Step / Premise / Argument sections (heuristic by section heading)
- **CITED-JUDGMENT-NEEDED**: cited in content sections where the heuristic cannot determine load-bearing vs informational; context provided for audit-lane judgment

## 2. Counts

| classification | count |
|---|---:|
| NOT-CITED | 1 |
| CITED-INFORMATIONAL | 0 |
| CITED-LOAD-BEARING | 0 |
| CITED-JUDGMENT-NEEDED | 0 |
| **total** | **1** |

## 3. CITED deps — context for audit-lane judgment

None. No named co-cycle dep is currently cited in the parent.

## 4. NOT-CITED deps (1)

This dep has ZERO substring hits in the parent. Zero hits here is not incidental absence: the dep *was* directly cited when this note was first written, and the citation was withdrawn deliberately, in the two steps recorded below.

<details>
<summary>full list</summary>

- `scalar_selector_remaining_open_imports_2026-04-20`

</details>

### Reclassification record (2026-07-26)

This dep was published above as CITED-INFORMATIONAL. It is re-measured here as NOT-CITED. The classification changed because the parent changed; the measurement below supersedes the original, which was accurate when taken.

| date | commit | change to the parent | hits |
|---|---|---|---:|
| 2026-05-16 | `62a903eb0e` | dep carried as a markdown link under "Audit dependency repair links" — a live citation-graph edge | 1 |
| 2026-05-17 | `2133821219` "audit: land cycle-break graph hygiene" | link converted to a backticked name: the graph edge is broken, the prose remains | 2 |
| 2026-05-26 | `79d70664e2` "review-loop: land Koide Q-delta formal ratio" | the whole "Audit dependency repair links" section retired, prose included | 0 |

The original measurement recorded the 2026-05-16 state — its section-3 snippet showed the markdown-link form — and was superseded roughly five hours later the same day by the cycle-break commit. Through the middle row the dep was still textually present, so CITED-INFORMATIONAL remained a correct text measurement; only the final row makes it wrong.

The withdrawn text stated its own purpose: the dep was a see-also cross-reference, "backticked to break cycle-0008 in the citation graph", and it recorded that the load-bearing citation direction runs `scalar_selector_remaining_open_imports_2026-04-20` → this theorem note, not the reverse. So zero hits is the state the firewall intends. Restoring the citation to make the paired runner's original expectation hold would reverse that firewall, which is why the runner's expectation is inverted instead: it now fails if the citation is ever reinstated. (Readers checking this against the current cycle inventory should note that the `cycle-0008` id has since been reused for an unrelated cycle; the cycle this text referenced is no longer in the inventory.)

Nothing in the parent is changed by this note, and no withdrawn citation is restored.

## 5. Independent-audit boundary

This metadata note records source-backed dependency classification only. It
does not choose, recommend, or prewrite an audit verdict. The independent audit
lane owns audit status, repair class, and effective status after reviewing the
evidence above.

## 6. What this note does NOT establish

- A retirement of any retained primitive
- An audit verdict (the audit lane decides)
- Permanent closure of any promotion path
- A claim that the parent is mathematically wrong

## 7. Verification

Paired runner: `scripts/frontier_koide_q_delta_linking_relation_theorem_note_2026-04-20_hostile_audit_findings.py`. Programmatically verifies the NOT-CITED set (expects zero hits) and the CITED set (expects ≥1 hit).

Every grep runs against the **parent**, never against this note. Grepping this note for the dep names it reports on would be self-referential and would gate nothing.

The runner additionally re-reads the exact dependency identities in sections 3
and 4 and the counts table in section 2. It fails if either the identities or
counts disagree with the classification the runner measures. Those checks
would have caught the drift recorded in section 4 at the time it happened,
rather than two months later: this note and its runner can no longer disagree
with the parent silently.

## 8. Cross-references (non-load-bearing)

- `docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md` (parent under audit)
- [PR #1277](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1277) (audit landscape diagnostic — Option 2 contribution)
