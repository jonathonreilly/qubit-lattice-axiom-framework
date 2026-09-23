# GPT-6 Sol max versus GPT-6 Astra low: matched PR8158 review

**Keep Astra low as the review default.** Sol max used an estimated **53% fewer credits**, but took **59% longer** and missed a consequential averaging restriction that Astra low found. Both rejected the defective source as stated. This single selected case does not establish general model accuracy or justify a default replacement.

## Matched experiment

Two fresh, blind agents received the same prompt and frozen 36-file scientific packet from original PR8158 head `dd78e677ba6cda496d6de20cfc215ef8bd09374f`, with methodology pinned to main `631d6b36cd1e9b860763ebcad36e40a2bbe7439c`. Neither saw previous findings, corrected source or the other report. Actual model/effort configurations were verified from session metadata. Each wrote and ran independent small controls; neither executed the submitted programs. All packet and report hashes were verified again for adjudication.

| Measure | Sol max | Astra low |
|---|---:|---:|
| Active task time | 10m36s | 6m40s |
| Modeled Standard credits | 36.82 | 77.81 |
| Input tokens, including cached input | 4,347,313 | 1,465,508 |
| Cached input tokens | 4,186,240 | 1,348,864 |
| Output tokens, including reasoning | 31,347 | 11,943 |
| Reasoning output, already included above | 16,923 | 1,365 |
| Known issue themes identified | 5 of 6 | 6 of 6 |
| Scientific recommendation | Needs manual science | Needs manual science |

Credit estimates use observed per-request tokens and published Standard rates: Sol 50/5/250 and Astra 250/25/1250 credits per million uncached-input/cached-input/output tokens. Fast rates multiply both totals by 2.5 (92.05 versus 194.53), leaving the percentage difference unchanged. The actual service tier was absent from observed metadata, so no Fast-mode claim is made. These are modeled credits, not billed charges or measured subscription allowance. Setup and coordinator/adjudication work are excluded. [Official Codex pricing](https://learn.chatgpt.com/docs/pricing), checked 2026-09-23 UTC.

## Findings adjudicated against the original source

| Issue theme | Sol max | Astra low |
|---|---|---|
| Triangle fixture cannot occur in nearest-neighbor cubic lattice | Found: F1 | Found: B-02 |
| Universal graph “if and only if” lacks its general proof and constant-rule exception | Found: F2 | Found: B-01 |
| Zero-attachment components also contribute constants | Found within F2 | Found within B-01/sound results |
| Finite static laws do not establish the claimed full axiom-model pair | Found: F3 | Found: B-03 |
| Averaging need not preserve nonlinear properties | **Missed** | **Found: B-04** |
| Submitted graph omits named scientific dependencies | Found: F4 | Found: B-05 |

The six rubric themes were frozen before either report. Some share a single finding, so raw finding counts (four versus five) are less useful than this mapping. No unsupported material finding was identified in either report. Both preserved the valid finite algebra and witnesses while holding the unsupported general claims.

### Why the missed issue matters

A property can hold for every fixed exterior condition and fail after those conditions are averaged. For example, the strictly positive two-bit laws `(9,3,3,1)/16` and `(1,3,3,9)/16` both describe independent bits. Their equal mixture `(5,3,3,5)/16` is dependent: its 2×2 determinant is `1/16` rather than zero. Astra supplied this counterexample, and the coordinator independently verified it with exact fractions.

Sol held the missing earlier-block attributions, but explicitly accepted the generic inference that uniformity in exterior records implies transfer by averaging. That is not the required nonlinear closure qualification. Linear expectation bounds and other properties proved stable under mixing can transfer; arbitrary nonlinear properties cannot. This finding does not refute a specific absent earlier theorem.

The same missed theme appeared in the earlier Sol-low pilot. Because that pilot used different context/prompt conditions, this is not a controlled comparison of Sol low versus Sol max.

## Limits and operational decision

- This is one deliberately selected, known-defective PR, not an unbiased sample or an estimate of recall/false-positive rates.
- The common packet omitted the referenced proof-search-governance document, exact earlier block sources and claimed mutation transcripts. Both disclosed those gaps.
- This tested scoped scientific review. Complete constituent disposition, live runner reproduction, current-main preservation and landing gates were outside scope. Neither report grants a landing PASS or audit verdict.
- Both reviewers worked on a shared host. Heavy backlog captures were held until both finished, but lightweight preparation continued; elapsed time is an observed run, not a laboratory benchmark.
- Sol's lower token price outweighed its larger input and output use. Its additional reasoning did not recover the missing issue on this case. Keep Astra low for ordinary review; make no local or remote skill default change from this experiment.

## Evidence

- [Frozen protocol](protocol.json), [common prompt](review-prompt.txt), [packet manifest](packet/manifest.json), [held rubric](held-rubric.json)
- [Sol report](reviewer-a/review.md), [Astra report](reviewer-b/review.md)
- [Sol usage](reviewer-a-usage.json), [Astra usage](reviewer-b-usage.json), [pricing snapshot](pricing.json)
- [Adjudication](adjudication.json), [exact averaging control](averaging-control.json), [verification script](adjudicate.py)

Full session rollouts and private reasoning text are not included; usage artifacts retain token metrics and model configuration only.
