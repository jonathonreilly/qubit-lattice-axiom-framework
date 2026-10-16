# Narrow terminology correction confirmation

PASS for the v2 correction. The complete code diff changes only two strings: the isotropic-ensemble assertion and reported family label now say coherence instead of visibility. All executable formulas, tolerances, paths and test values remain unchanged. Note v1 and all original v1 source/output hashes remain unchanged, and the original independent report preserves the terminology finding.

The full v2 runner reproduced CONTEXT_ECHO_CONTROLS_v2.json exactly: five passing families, including 24 finite-loop cases. Apart from the updated runner hash and corrected family label, its JSON equals the v1 output. No failure or timeout occurred. Execution used the recorded 120-second limit; stdout, stderr and receipt are preserved separately. Exact source hashes are in frozen_sources_v2.json and the exact code diff is v2_code.diff.

Signed sinc is correctly identified as coherence; visibility magnitude would be its absolute value. The prior mathematical proof and physical-scope qualifications continue to apply to the unchanged note and formulas. This addendum grants no empirical validation or audit status and makes no canonical-publication change.

- NETWORK_EVOLUTION_BLOCK12_v1.md: e5fe9458c1794b28562bd5215b090083362cda6daf472e441ba2f3e651c90f1e
- probe_context_echo_v2.py: 1495843bdc467731645d18ebfc6a7468d682766c27a060a78eb8fb00c5f8fbd8
- CONTEXT_ECHO_CONTROLS_v2.json: 2667d74ae009fd096568d8b359489ad6fdc2566d41bb1d770565775427340680
