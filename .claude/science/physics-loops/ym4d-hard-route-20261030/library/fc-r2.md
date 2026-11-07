lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T12:50Z

# FC-r2: the complex frame-change BLOCK of gates/fc-gate.md §2

Row 404 (`fc-r2`). Pinned at commit 2f8fd8e61. Written section by section; the Result is §6.
Proved by Claude (Mini worker 1), not yet checked by the other model.

Moves: the complex frame-change BLOCK of `gates/fc-gate.md` §2 on `library/fc.md` (Lemma G seams and datum conversion, (2.3) membership, the reduction to CC). FC is the open lemma of `library/stage-claude.md:275`, needed only under the one-frame reading (R1) of the stage spaces (owner `stage-claude`, inside H-STAGE).

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker 1, checkout at 2f8fd8e61 (branch `claude/ym4d-hard-route`). Research text, not an audit; grants no status. Written arguments only; no numeric run (none was needed). Sources: CA-I, CA-II and SA (`theorem_0_complete_account_raw_{I,II}.tex`, `YM4_sketch_500.tex`) at `31a47c543775`, fetched by URL into a scratch folder, SHA-256 equal to `library/arr.md:21-23`. Balaban CMP 99a p. 82 ((1.30)-(1.32)), CMP 102b pp. 279-281 (Theorem 1, (12)-(21)), CMP 109 pp. 252-253 ((0.3)-(0.12)), CMP 119 p. 256 ((2.10)-(2.12)) read from `~/ym4d-papers/` (page images where the OCR is garbled).

Credit: Tadeusz Balaban for the averages (CMP 109 (0.3)-(0.12)), the determining sets (CMP 119 (2.10)-(2.12)), the background theorem (CMP 102b Theorem 1, Proposition 2) and the datum convention (CMP 99a (1.31), CMP 102b (20)). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account at `31a47c543775`: the response chart (CA-I 4.5: (K1), (K2), (K6), (K8)), the chart class and its inclusion statement (CA-I 12936-13060), nested criticality (CA-I 128485), the data-axial frame and its twist bounds (CA-I 17322-17600), the quotation of the CMP 122a stage spaces (CA-I 148080-148240) and their weight exponents (CA-I 49596-49645). Claude for `library/fc.md` and `library/stage-claude.md`; Codex for `gates/fc-gate.md` and `library/prior/fc.md`.

## 0. Duplicate check (rule 0a) and consumers

Searched `library/open-core.md`, `library/l17c.md`, `library/open-registry.md` and the FINISH rows for: frame change, common gauge, double block, seam, Lemma CC, C_rel, b_D, chart datum, FC, fc-gate, one-frame, (R1).

* No other row attacks this item. FINISH rows 388 (`stage-gate`), 392 (`fc`) and 404 (this row) are its lineage. The registry has no row for the frame change; FC-test, FC-mean-match and FC6 (owner FCON) are different statements that share the letters.
* `C_rel` in `library/open-core.md:246` is the velocity constant of the L16 path statement (LOC). It is a different object: a bound along a path of data in A_in, not a gauge comparison of two fixed fields. No overlap.

Consumers. FC has one consumer, the source inclusion (SRC) of `stage-claude.md` §5.1, and only under (R1). Under the birth-frame reading (R♭) Lemma F gives (SRC) with no frame change. Which reading is CMP 122a's is not settled (`gates/fc-gate.md` §2.1-2.2). So this note is worth doing only for the (R1) branch. It says, at the end, what (R1) costs.

## 1. What changed: three structural findings

These three facts reorganize the three items of the row. Each is proved in the section named.

1. **Lemma G's construction is wrong on seams, by a factor L (§2.1).** The comb gauge of `fc.md` §2.5, pinned at the block centres, gives relative seam data of size about L²κ/2 on an explicit pair of SU(2) fields with plaquettes at most κ and equal coarse data. The claimed bound is 3Lκ. With L²κ the scale gain L⁻¹ of the advanced clause is lost entirely, so (FC*) could never be paid from the stage gap. The order Lκ is nevertheless the right one: every gauge leaves at least about Lκ/6 on the same pair (§2.6), and Lemma G′ (§2.4) attains C_rel·Lκ with C_rel a number that depends on d only, not on L.
2. **The chart base may be any gauge representative of Q^u (§2.2, Lemma B).** The chart identity (K6) needs a real base U_k(V₀) with regular real data V₀. Any real gauge transform of the base's data is again such a datum. So the gauge freedom may be spent on the base, not on 𝐔. Then no pin is needed at the D′-endpoints next to Γ′_j (the "rim"). Only the coarse centres are pinned, and the hat-function patching pins them exactly. The rim and its corners disappear from Lemma G.
3. **The chart datum on the layer interface carries Balaban's block correction (§2.5).** On the level-(j+1) bonds from the collar into Ω_{j+1}, CMP 99a (1.31) adds to the raw ratio an average over the block of the relative contour transports. For any gauge whose relative links are O(Lκ), this correction is O(L²κ). A bump correction inside each interface block removes it at a cost O(Lκ) (Lemma G″). Without it the datum bound fails by a factor L at the interface.
