# Inherited markers: affected confirmation

UTC: 2026-10-30T18:26:43.857326+00:00. Corrected source SHA-256: `2b0b511ea539a76ee410dad2f26adf88d9cab294123cad9256ca840b896d08e9` (1039 lines). The initial HOLD and its receipt are preserved unchanged in [the source-first report](../gates/inherited-markers-fbe0652b18.md) and [initial receipt](gate_inherited_markers_fbe0652b18_initial_receipt.json).

**The scoped correction is confirmed.** I read the exact 24-line insertion and lines 920–994 in context, and mechanically verified that removing corrected lines 933–956 reproduces the complete frozen source at fbe0652b18. No other mathematical change is included in this confirmation.

For a fixed pulled-back bad set with k disjoint components, possible completion outcomes are subsets of those components. Their weighted envelope is `r_cut^(|B_A|/2) product_i(1+r_cut^(|Y_i|/2)) <= 2^k r_cut^|B_A| <= 2^|A| r_cut^|B_A|`. The correction now places a common positive normalized-density/source-score envelope before coefficientwise output/buffer suprema and retains the fixed bad-set indicators inside the integral. It pays the r_cut power once and retains the additional combinatorial factor. `D + marked <= 1+2^|A| <= 3^|A|` fits exactly the existing GH23 log 3 allowance through the direct count already used in GH36–GH37; no extra independent lambda-radius factor is available. This resolves the new counting issue identified in the initial report.

Landing scope is **section 13 as checked finite identities, reader/source bookkeeping, and an explicitly unproved quantitative continuation proposal**. GH47, the GH48 changed-marker identity, the pointwise/shared-reserve count, GH50 and GH51 retain the conclusions and scope stated in the initial report. The proposed GH49 bound remains unverified: the previous positive density/reader forest chain and its uniform envelopes have not been independently certified here. This verdict does not approve earlier GH11–GH46 as theorems or authorize consuming GH49 as established. Non-free continuum existence and a positive physical continuum mass gap remain open.

No author routing context, external primary paper, new worker or scientific job was used. Source editing was performed by the coordinator; this reviewer wrote only review evidence. Backend attestation remains unavailable. Direct pinned vocabulary lint is recorded in the final receipt and supplies no mathematical evidence.

VERDICT: LAND
