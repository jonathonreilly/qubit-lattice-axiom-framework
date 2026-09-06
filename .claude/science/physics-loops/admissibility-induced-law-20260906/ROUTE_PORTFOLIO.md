# Route portfolio — admissibility-induced-law-20260906

## Prior-art sweep (workflow step 2), searched commit origin/main 341511a74e381be959777b1cb68ceb2dd217c890 (2026-09-06)

Commands run (worktree at the same tip):

```bash
git fetch origin main:refs/remotes/origin/main
git grep -n -iE "formation order|order of formation|sequential(ly)? form" origin/main -- 'docs/*.md'
git grep -n -iE "static law|Gibbs (measure|law|specification|potential)|Markov random field|Hammersley" origin/main -- 'docs/*.md'
git grep -n -iE "Brook|full conditional|local characteristic|compatib.*conditional|conditional.*compatib" origin/main -- 'docs/*.md'
git grep -n -iE "product over (the )?neighbo|neighbo.*product form" origin/main -- 'docs/*.md'
git grep -n -iE "normali[sz]er.*neighbo|neighbo.*normali[sz]er" origin/main -- 'docs/*.md'
git grep -n -iE "order[- ]independen|order[- ]dependen" origin/main -- 'docs/*.md'
git grep -l -iE "hammersley|markov random field|formation order|Brook" origin/main -- 'docs/audit/data/ledger/*.json' docs/audit/data/derivation_obligations.json
git ls-tree -r --name-only origin/main -- docs/ | grep -iE "FORMATION_(ORDER|LAW)|GIBBS|MARKOV|SEQUENTIAL|STATIC_LAW|NEIGHBOR_RULE|ADMISSIBILITY_RULE"
grep -rli -e "hammersley" -e "markov random field" docs archive .claude/science
```

Hits and classification (each read at its own text):

| Hit | Classification | What it establishes / why it is not this block |
|---|---|---|
| `docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md` (unaudited; candidate-retained-grade in its own status field) | MATCHING PRIOR ART for the static half, binary menu | Brook square-curl compatibility of strictly positive binary full conditionals, uniqueness by path integration, the cubic count-only classification to geometric odds and an Ising-type finite action. Its scope boundary excludes "stochastic update dynamics" and "Record formation". This block LINKS it as upstream, re-proves the static half for the six-state menu (general finite-menu Brook lemma + pair form on triangle-free graphs + positivity necessity), and adds the formation law, which that note does not define. |
| `docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md` | context-only | An append-only cellular relation witness (majority menu; one record per step; permanence) and a rule-space census; states that the rule supplies conditional odds for the forming record and not the formation site/rate. No static law, no formation law as a probability law, no comparison. |
| `docs/R_HALF_OPEN_BACKLOG_FORMATION_LAW_PROBE_BATCH_EXACT_SUPPORT_NOTE_2026-07-13.md` | context-only | Formation-weight probes across epochs (`w=1/3`, `w=1/2`); marginals differ between complete record environments. Different object (formation weights across epochs), no static-vs-formation theorem. |
| `docs/RECORD_MARKOV_GENERATOR_PREMISE_CLASSIFIER_2026-06-06.md`, `docs/RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md` | context-only | Continuous-time generator embeddability premises for two-state record dynamics. Not a nearest-neighbor rule's joint law. |
| `docs/ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md` (order-independent partial-map union) | context-only | Set-theoretic order independence of compatible partial-map unions; explicitly "not physical commutation of formation". |
| `docs/work_history/repo/review_feedback/LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md:505` | context-only | Counts transcripts if formation order is certified; no law. |
| `archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md` RESULT 136 (+ `opus_t210-213.py`), archived, never refereed, floating point | REFERENCE (archive tier, no authority) | The static reading of the rule as a full conditional; Hammersley–Clifford as a quoted step; the sum rule's compatibility failure in floats; the normalizer-constancy argument. This block re-proves the finite statements exactly, names the reading, and adds the formation law. |
| `archive/notes/docs/work_history/repo/review_feedback/EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md` | context-only (archived) | Law-type vs law-value taxonomy; no theorem on the two laws. |
| ledger shards / `derivation_obligations.json` | no hits for hammersley / markov random field / formation order / Brook | — |

Target state after the matched-hit review: **open**. The static half is a generalization of a landed binary theorem (cited as upstream); the formation law and its exact relation to the static law are not on `origin/main` or in the archive.

## Artifact routes for this block

| Route | Artifact type | Status |
|---|---|---|
| Exact finite theorems T1/T2 on declared windows and menu, native proofs, exact runner, one note | theorem note + runner certificate | active (block 01) |
| The five attempted coincidence routes as exact computations (family G) | runner certificate + N-gate section | active (block 01) |
| Infinite-volume (DLR) existence/uniqueness of the static specification | open; not this block | queued (OPPORTUNITY_QUEUE.md) |
| The Gaussian (gravity-lane) instance of the static/formation distinction on the lane's own fixture | open; not this block | queued |
