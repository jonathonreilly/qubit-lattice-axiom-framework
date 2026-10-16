# M11 affected canonical wording confirmation, v1

This supplements the complete canonical source review `CANONICAL_REVIEW_v1.md` (SHA256 ba2534d17187b67e6e84d15c4338b4170296ca28cbd92351bcef804af63638f5). It does not replace that review or its original finding. I inspected the complete exact diff from the previously reviewed note and verified the current note/snapshot identity and unchanged geometry hash. No author control or aggregate was executed.

The final copied note is SHA256 **00310bf4a764ec80b3c00faa5eed53149fa2713184cf7a08b7ac23f156a67231**, 24860 bytes. The geometry helper remains SHA256 **c9b1e47cbaeaa8faf31543541e983c19f23a4e4d1fdfebae88e1e0590843e7aa**, 9491 bytes, exactly as completely reviewed. `CANONICAL_WORDING_SOURCE_FREEZE_v1.json` records full paths and hashes; `CANONICAL_WORDING_DIFF_v1.patch` preserves the entire delta.

The delta has only two substantive wording corrections and their repeated references:

1. The selection witness now states “analytic false-rejection probability approximately 0.3518716581.” This resolves the independently retained finite-decimal exactness finding. The analytic expression and its diagnostic computation did not change.
2. The covariance counterexample now says axis-supported/axis choices rather than atomic directions/atoms, including the no-go table and witness references. With a continuous uniform phase, each selected axis contributes a circle-supported distribution with no point atom; the discrete axis selection is what has probability1/N. The replacement wording is accurate. Its mean, covariance I/N and cone rejection probability1/N remain unchanged because those calculations depend on axis choice and phase symmetry, not point atomicity.

This second change is distinct from the independent pre-exposure finite128-point counterexample: that independent construction uses four discrete phases and is genuinely atomic, so it needs no alteration. Any atomic terminology in the older working-source correspondence is historical wording for the author's example; the corrected canonical interpretation is the axis-supported continuous-phase law above. The old reports remain immutable.

There are no formula, source-code, domain or empirical-result changes in this exact delta. The original review's mathematical conclusion and limits therefore carry forward to these final bytes. No additional claim about mutation execution, source-cache status, raw data, formal audit or integrated-main validation is made here.
