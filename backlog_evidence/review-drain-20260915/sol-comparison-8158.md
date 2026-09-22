# GPT-6 Sol versus Astra: blind PR8158 pilot

**Result:** GPT-6 Sol at low reasoning independently caught the same two central blockers as GPT-6 Astra at low: an impossible cubic-lattice witness and an unsupported universal graph criterion. Sol is promising for lower-cost initial reviews. This single case does not establish that it can replace the full Astra landing review.

Both reviewed original PR8158 head `dd78e677ba6cda496d6de20cfc215ef8bd09374f`, delta `df5316ee81d59d573b3837afb80d371d12d890d6`. Sol received no prior conversation, Astra findings, corrected draft or reviewer control outputs. Its first report was frozen before comparison. A second blind phase completed the initially omitted history/parent/disposition scope, without revealing missed findings. No primary scientific runner was run by either comparison phase. Existing Astra review and landing requirements remain in force.

| Issue | Astra | Sol |
|---|---|---|
| Triangle-containing fixture cannot be nearest-neighbor cubic lattice | Found | Found independently in phase 1 |
| Global iff: constant-rule counterexample and missing arbitrary-component/noncancellation proof | Found | Found independently in phase 1 |
| Zero-attachment components also give constants | Found | Found in phase 1 |
| Finite static measures do not establish complete all-axiom models | Found | Found independently in phase 2 |
| Averaging transfers uniform linear bounds, not arbitrary nonlinear law properties | Found | Not explicitly flagged |
| Submitted graph manifest has zero dependency edges despite named parents | Packaging corrected during authoring | Explicit additional finding in phase 2; root verified original node has empty dependency hash and out_degree 0 |

The Sol report’s three main analytical checks are valid: cubic-lattice parity, the constant-rule three-site counterexample, and the six-axis spectral decomposition. Astra additionally recomputed the named rational witnesses through 20 independent exact controls and read a broader historical packet. Sol intentionally excluded old reviewer findings and control outputs to preserve blindness. A brief Sol completion message miscounted changed/absent current paths; the report’s actual 22-row table contains 11 collisions, matching the verified inventory. This has no effect on its scientific findings but illustrates the need for mechanical identity checks.

## Measured usage and cost

Local task telemetry verifies the actual configurations `gpt-6-astra/low` and `gpt-6-sol/low`. These are request-token sums, including repeated cached context, not unique source-token counts.

| Metric | Astra original review | Sol phases 1 + 2 |
|---|---:|---:|
| Active task time | 405.638 s | 226.841 s |
| Input tokens | 3,315,296 | 1,708,353 |
| Cached input tokens, included above | 3,195,904 | 1,616,256 |
| Output tokens | 6,766 | 9,375 |
| Modeled Standard credits | 118.2031 | 15.02988 |

Published Codex Standard rates per million tokens are Astra 250 input / 25 cached / 1,250 output credits and Sol 50 / 5 / 250: **Sol costs 80% less for the same token mix**. Fast mode multiplies both by 2.5. Source: [OpenAI pricing](https://learn.chatgpt.com/docs/pricing), checked 2026-09-22. Reasoning tokens are included in output and were not double-counted. These estimates are not billing receipts.

This run’s modeled total was about 87% lower, but it is **not an equal-work cost benchmark**: the reused Astra session had different prior context, broader history coverage and additional executed exact controls. Scope and context differences must not be presented as a pure model saving.

## Recommendation

Keep the current landing default for now. Sol is a strong candidate for a controlled lower-cost first review, with Astra reserved for unresolved mathematics, premise/quantifier issues and sampled misses. Before changing local or remote review-loop defaults, test several additional unseen PRs with matched source packets and required coverage, including a clean PR, an imported-theorem applicability case and a subtle false-positive case. One known-defective PR cannot estimate missed-bug or false-positive rates.

Evidence: `sol-comparison-protocol-8158.json`, `drain8158-original-review.json`, `sol-compare-8158/independent-review.md`, `sol-compare-8158/phase2-completion.md`, and the two immutable usage receipts. The model default has not been changed.
