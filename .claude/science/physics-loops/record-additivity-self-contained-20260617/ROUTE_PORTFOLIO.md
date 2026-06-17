# Route Portfolio

| Route | Score | Reason |
|---|---:|---|
| Self-contained finite word/count proof | 3 | Directly targets the audit blocker's missing dependency edge without adding axioms. |
| Keep monoid parent and wait for audit | 1 | No source movement; leaves the same conditional dependency. |
| Derive record production | 0 | Out of scope and not supplied by the Record axiom. |
| Narrow to fixed finite prefixes only | 1 | Safe but loses the unbounded finite schema. |

Selected route: self-contained finite word/count proof plus supplied-context
firewall.
