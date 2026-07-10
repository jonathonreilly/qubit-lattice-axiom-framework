# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|:---:|:---:|---|---|
| Target note text | Defines the finite source-local predicate | zero-input structural | `docs/UNIVERSAL_QG_OPTIONAL_TEXTBOOK_COMPARISON_NOTE.md` | yes | yes | Direct finite inspection | checked by runner |
| Current markdown corpus under `docs/` | Finite domain for inbound-reference enumeration | zero-input structural | current checkout | yes | yes | Exhaustive filesystem enumeration | checked by runner |
| Audit-history exclusion | Prevents archived audit prose from being treated as a current dependent | admitted normalization | runner scope | yes | yes | Keep exclusion explicit and narrow | accepted for metadata-only scope |
| Canonical textbook physics rows | Navigation names only | support-only | code-span filenames in target note | no | no | None required; they carry no edge here | excluded from proof inputs |
| External literature or observed values | No role | unsupported import | none | no | no | not applicable | absent |

No physics theorem, fitted value, observation, or literature statement is a
proof input to the finite metadata predicate.

## Counterfactual pass

| Implicit choice | What if it is wrong? | Direction opened | Effect on this block |
|---|---|---|---|
| `docs/` is the current dependent-note domain | A consumer outside `docs/` could exist | Widen a future repository-policy scanner | No current audit dependency edge is hidden; the audit graph is built from markdown notes under `docs/` |
| `docs/audit/` is history rather than a current dependent | Archived prompts necessarily repeat the filename without packaging guards | Treat audit history as evidence input | Rejected for this predicate because it would make history self-referential; the exclusion is explicit |
| Optional/non-authority context can be recognized syntactically | A future citation could use novel wording | Extend `context_guard` with the new native phrase before landing that citation | Runner fails closed on unrecognized current contexts |
| Code-span filenames are navigation, not dependency edges | The graph builder could later change its link semantics | Revisit `Z3` against the updated parser | Current graph policy treats markdown links as edges; the runner directly enforces the present syntax |
| The named comparison rows exist | One could be renamed or removed | Update the navigation inventory without granting authority | Runner fails until the informational list and files agree |

None of these counterfactuals opens a physics theorem route or requires a new
axiom/primitive. They only change the finite repository domain or parser
contract and therefore remain tooling-level maintenance paths.
