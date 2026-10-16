# M11 canonical source correspondence and isolated cluster judgment

Reviewer: `/root/localized_history_check`. Final reviewed note: `docs/CASSINI_ERROR_DIRECTION_MODEL_BOUNDED_THEOREM_NOTE_2026-10-15.md`, SHA256 `6e321840bf78a2687fb516aca2e46da293c72c9499dd5175bf5434da017fcb10` (25,355 bytes). The complete initial 421-line note was frozen before reading, and both subsequent exact wording-only deltas were read in full. Copies and diffs remain immutable in this directory.

## Source correspondence findings

The final note's instrument assertions are consistent with the frozen `SOURCE_REVIEW_v1.md` (SHA256 `084e2ff22905e4466d0e001ad2dc41908234ed43c28655ffd8c06a1170a55b58`) and its pinned primary documents within this focused scope. No unresolved source-interpretation mismatch was found.

- **Expected setting versus measurement:** the observation/source-boundary section correctly treats FGAIN Px/No as an expected gain-setting input, not measured C/N0 or noise covariance. DSN0159 (2001), printed pp.3-13/14 (PDF 35/36), and label columns 33/34 support that distinction. The cited §3.5 is indeed the secondary-header section; the table of contents and §3.5 start were additionally checked. The 110 MHz field is the expected IF-bandwidth setting, not an empirical effective noise bandwidth of the retained 1 kSPS subchannel.
- **Quantization:** the note makes the ideal unsaturated analog cell an extra premise. DSN0159 §2.3 and printed p.3-20, together with the SIS and label, document truncation and `2*k+1` centering. They do not alone establish a physical analog preimage, absence of upstream clipping, or a complete physical-error budget. The note's caveat about nonextreme downstream codes and zero hardware-error counts is appropriate.
- **Statistical supplier:** the note explicitly declares the conditional sphere-direction law rather than claiming it follows from FIR filtering, equal bandwidth/sample rate, covariance isotropy or a large fitted tone fraction. Its explanatory FIR covariance and two-tap example agree with the exact reasoning in the frozen source report. A contiguous half-record split is not represented as documented receiver independence.
- **Positive supplier leads remain visible:** guide §2.5.2.4 identifies monitor streams that may contain receiver noise temperature and carrier SNR. Sections 3.2.1.1.1 and3.3.4.6 contain later averaging/overlap and I/Q SNR-estimation examples. The note preserves these as potential sources, explicitly reports no matching track-specific value/transfer response, and makes no archive-wide absence claim. The guide's operational independence wording for the 2009 FFT example is not converted into a certificate for this 2002 split.
- **Physical status:** the note correctly leaves the constant-tone, conditional-direction, actual measurement and calibration premises open. It distinguishes scale-free probability statements from deterministic error-energy bounds, and from derivation of scalar dynamics, initial state, scales or environment. The added review-record paragraph reinforces this separation without changing any mathematical proposition.

The source check does not independently establish that root acquired no other products, the actual header values, or the reported numerical fit/exclusion outcomes. For local review context I read the complete existing working `DIRECTION_SUMMARY_v1.json` and `CANONICAL_CONTROLS_PRELIM_v1.json`. The summary agrees with the note's reported FGAIN 38/44, IF setting 110, attenuation codes 40/49, zero data-error/extreme-record summaries, 600 records per band, median diagnostics and exclusions 489/592 and 168/578. That is a document-to-output consistency check, not raw decoding or empirical replication. The preliminary controls are synthetic/model evidence and are not a measured noise calibration. No final aggregate/cache execution was run or certified here.

## Actual issue and subsequent changes

Initial frozen note SHA256 `7e4072642e778ee1295e2219d247795641a409315ca159690cca5a9ce56ac9e8` called the uniform-phase basis-choice witness an atomic direction distribution. The basis/ray choice is atomic; the full complex-sphere distribution is supported on a finite union of phase circles and has no point atoms. I reported this narrow terminology issue promptly. The change to axis-supported/axis-choice wording in SHA256 `00310bf4a764ec80b3c00faa5eed53149fa2713184cf7a08b7ac23f156a67231` resolves it; the displayed 1/N rejection probability is unaffected. This incidental finding does not constitute a new full proof review.

The same v1→v2 diff changes a finite decimal described as exact into an approximate numerical value of an analytic probability. That is an appropriate precision qualification. The v2→v3 diff adds only the Review record heading and paragraph separating prior results, the new angular import and later landing/audit gates. I read both complete diffs. No equations, empirical data or executable source changed in those note deltas. I did not verify executable hashes or run code, which are outside this task.

## Isolated repeated-cluster judgment (295 words including verdict)

OPEN

M11 warrants a separate reviewable milestone within the stated receiver family. M9 derived integer channel characters and ideal ADC-cell consequences, while preserving the need for a physical carrier estimator. M10 supplied carrier/reference reconstruction and exact feasible-set geometry conditional on an externally justified discrepancy radius. M11 changes the inferential target: under a newly declared conditional angular law, projection ratios eliminate the unknown error radius and radial distribution for specified tests. Its quantizer-safe cone enlargement and frequency-uniform model challenge are a meaningful additional derivation chain, rather than another application of M10's deterministic disk.

The formal claim category remains a conditional bounded theorem, so a different category label is not the reason to open. The substantive change is a statistical supplier hypothesis with a concrete falsifier. Existing paired output records numerical exclusions under two allocations, preserves uninformative arcs, and labels the data as previously exposed development. That offers marginal review value beyond the earlier pointwise cell obstruction or receiver-reference comparison. It also directly tests an attempted way around a named surviving measurement-scale input.

Independent reviewability is adequate at the note level: the required projection, cone, Dirichlet and Lipschitz arguments are presented, and source assertions do not convert gain settings into measured noise. This local check does not certify the implementation or final canonical execution. A combined PR would be possible, but the new probability premise and its failure modes form a coherent separate review boundary.

The result is mathematical reconstruction and a measurement-model challenge, not a new scalar-framework derivation. Angular symmetry is supplied and challenged; the physical calibration obligation survives. OPEN is therefore only a content/cluster decision for this third block. It is not permission to relabel exposed data as an independent experiment, an audit outcome, or approval of further variants lacking a new supplier or falsifier.

## Rule and comparison identities

The applied rule is the complete `docs/ai_methodology/skills/physics-loop/references/CAMPAIGN.md` at the locally resolved `origin/main` commit `92574ffe95192cc0724a27e1acad28e42d325115`, SHA256 `172be2f4301d6f32edbf4f0bf55fdfb9e045098253c6a5b475fc4446816c6666`. Its Cluster-Cap Evaluator gates only opening the third/subsequent family PR, evaluates new load-bearing content, claim type, independent reviewability and marginal review value, and defaults to BACKLOG when context is insufficient. I read the entire reference; no remote ref was fetched or changed. The parent supplied that M9 and M10 are the prior two receiver-family PRs; no GitHub-state verification is claimed.

The actual comparison sources were read completely:

- M9, `docs/SCALAR_INTEGER_CHANNEL_CALIBRATION_BOUNDED_THEOREM_NOTE_2026-10-15.md` at commit `e143a32663ad58483efa73050d9344a700d91508`: SHA256 `5bd3667c7e34646e616c82498401c8c9169604ce471aeefefd3f1b1da65f6616`.
- M10, `docs/CASSINI_CARRIER_REFERENCE_FEASIBILITY_BOUNDED_THEOREM_NOTE_2026-10-15.md`, current file: SHA256 `ee2c6e46a235de9a2c668d6013dc830eddb160c77d218309431669b8d9ab26f8`.
- M11 existing working summary: SHA256 `9df1ba0be48bb21249cc537a723d78bc33519929118d5f412356b3f7b094315e`.
- M11 preliminary control report: SHA256 `6dd2ac3534b28a59959b11e6eb9242c61748cdf50ca61bfba3be48a03c095829`.

The earlier integer-history note was incidentally consulted during source identification; it was not mistaken for M9 or used as the comparison basis. No claim is made to have reviewed its entire truncated initial display or revalidated it. The applicable current-main campaign rule, rather than the older installed skill's per-block delivery wording, governs this judgment.

## Exact scope and preserved evidence

Primary-source identities and original page/line scopes remain in `SOURCE_IDENTITIES_v1.json`; the complete original report and identity are unchanged. Added DSN0159 TOC/section-start reads are recorded separately. `CANONICAL_NOTE_FREEZE_v1/v2/v3.json`, `MAIN_CAMPAIGN_IDENTITY_v1.json`, `M9_NOTE_IDENTITY_v1.json` and `CLUSTER_CONTEXT_IDENTITY_v1.json` bind the copies used here. `CANONICAL_SOURCE_REVIEW_IDENTITY_v1.json` binds this report and its evidence.

This was a focused source comparison plus isolated content judgment. I did not review all mathematical proofs adversarially, inspect the implementation, reopen raw observations, execute an aggregate, inspect other reviewers' reports, modify a canonical source/backlog/state/lock/index/branch, or create/update a PR. I did not apply a formal audit verdict or combined landing judgment. Root retains scientific authorship. All writes were confined to the assigned `calibration_supplier/independent_source_v1` directory; previously frozen files were preserved.
