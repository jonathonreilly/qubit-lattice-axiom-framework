Verdict: FIX

# Line-by-line check of library/uo2-geo.md (518 lines)

Checked line by line by Claude (Opus 5.5, fresh session), once. Branch `claude/ym4d-hard-route` at 4ddbc7cec.
I read the note in full, its task file, `gates/geoh-o2-check.md`, `prior/geoh.md` row GEOH-O2, `in1.md` 60-90 and 145, `sa-2.13.md` 220-268, `geoh-o2.md` 245-256 and 391, and `geoh-live-ab.md` 1-128 and 303-512.
Source lines read: Y 63680-63845, 64048-64078, 65175-65183, 73101-73160, 74216-74302, 74645-74670, 75842-75965, 78870-78940; SA 5612-5629, 17270-17278, 17315-17319, 17415-17460, 18080-18096, 18700-18717, 18874-18900.
No computation is used.

Summary. Every proved and ported step checks. The chain at every remade level is a correct port. The conditional bounds (15)-(18) check. The defect is again in the target. FCO is stronger than UO2-geo (b) needs, in two ways: it asks for full read stencils where the consumers use only stored and visible slots, and it measures the collar in M-layers where a fixed number of owner cells suffices. Both narrowings change the stop. The three routes are distinct methods but fail at one step. geoh-live-ab does not supply FCO; it supplies one stored-slot case, conditionally.

## Findings

**1. L77-104, the chain, (1). CONFIRMED.** Source: Y 63684 (class: single boxes, quiet, quarantine "the lower end point included"), Y 63714-63753 (tracing). The source says G_i is "a union of components of the original output of step i". The class makes it one component. For i > h the restricted input is G_{i-1}. Healing, island and standing-mark cases read as stated.

**2. L106-123, (2)-(3). CONFIRMED.** Y 63754-63771 gives a_i = MŘ_iL^i, G_{i-1} ⊂ H_i ⊂ G_{i-1}^{[a_i]}, O_i = H_i^{[8a_i]}, G_i = H_i^{[10a_i]}. Y 63773-63825 gives H_i ⊂ Z''_i ⊂ O_i ⊂ G_i in the early range, Z''_i ⊂ O_{k_0+1} ⊂ O_i in the late range, and G_h ⊂ Z''_{h+1} ⊂ ... ⊂ Z''_k.

**3. L125-135, remade range and genealogy. CONFIRMED.** Y 73112-73131 (stage entries, t♭ < j ≤ t♭+n(X)) and SA 17415-17440 (drop-out entries) match. Y 74218-74234 and 74250-74271 ("No third tree meets it") match. The chain has a node at every remade level, plus the bottom node.

**4. L141-169, owners and uniqueness. CONFIRMED.** Y 78906-78916 gives the four rules as stated. SA 17440-17449: "standing marks that share a part are nested, their windows ... are disjoint, and at any one place and level at most one drop-out mark is active." H-LF reads as stated at in1.md 145. Y 75915-75960 (coarea, sharp-failure branch) and 75961-75965 (admission is an input) read as stated.

**5. L171-207, (5) and (6). CONFIRMED.** Y 74655-74666 supplies the finite template. 2 (cut) × 3^4 (cells) × 2 (owner levels) × 5 (uses) × τ × L^4 = 20·3^4τL^4. geoh-o2.md 249-255 reads as cited.

**6. L390-473, (12)-(18). CONFIRMED as conditional ports.** SA 17274 (v counts log x_j per stored site) and SA 18087-18089 ("including the assigned collars and the operation's fixed coordinate multiplicities") match (12). (14) gives (1+2(c_0+1)/R_n)^4 ≤ 2. (15): 2(MR_n)^4 · μ_0L^4 · 2ℓ_n = 4μ_0L^4 w(a). (17) matches geoh-o2.md (13). (18) matches SA 18702-18710, with V° ≥ N.

**7. L211-229, FCO versus UO2-geo (b): read stencils. MISMATCH: stronger than the consumers need.**
- (15) uses only stored slots. L397 and L420 say so.
- (16) uses only discrete slots per owner-level site (L441). Y 74655-74659 attaches tests to sites. A test needs an anchor address, not a whole stencil.
- N's load is already paid by visible slots: sa-2.13.md (6.2)-(6.4). That text says full read regions of past activities "are an analytic-envelope issue".
- Y 78923: "No factor counts the number of later reads of a mark." Note L69 and L399 agree.
- The full read region of SA 18878-18887 serves the restriction and history-product argument (SA 18888ff: "If two clusters never touch, their cell margin exceeds the fixed reach of every test, pivot and collar"). It is not a consumer of v or the code.
- Repair. Split FCO. **FCO-slot**: every stored slot (with SA's assigned collar), every visible determining and action slot, and every discrete-record anchor lies in its owner's collar at native level n or n-1. **FCO-read**: the full elementary stencils of L213-224. Restate (15)-(18) as conditional on FCO-slot only. Name the consumer of FCO-read (SA 18878-18900, and Y 78917's C_d if it is read that way) and leave it to that row.

**8. L215-216, collar width. MISMATCH: c_0 M-layers is stronger than needed.** A collar of c_1 whole owner cells, c_1 fixed, serves every consumer. Its site budget is (2c_1+1)^4(MR_n)^4 instead of 2(MR_n)^4. Its covering count is (2c_1+1)^4 per level instead of 3^4. Only C_v, C_d and b_code change, by fixed factors. The note's own route-one example is then inside the collar: Y 65175-65183 says the read reach is "less than one cell by the choice of M". Y 64048-64078 keeps test-cube reads at widths M_2Ř_m in level-m units, again O(1) level-m cells. Repair: state FCO with c_1 cells, and redo route one at that width. The 1D illustration at L275-279 then no longer bears on actual reads.

**9. L235-282, route one. CONFIRMED as stated; failure point weakened by Finding 8.** (7) is sa-2.13.md (6.1). SA 5612-5629 gives the determining-bond rule. The visible-site assignment is right. (8) is unproved for full stencils, as stated. With a cell collar, the cited reaches (Y 65175, Y 64048-64078, SA 17317's □^{~2}) fit. Whether every actual stencil has O(1)-cell reach is the open part.

**10. L284-334, route two. CONFIRMED source reads; failure point CONFIRMED but likely filed wrongly.** Y 75842-75862 (row sets and double blocks), 75890-75904 (old strip centre, "evaluate each surviving old indicator on its complete original carrier"), 75934-75949 (every prefix), 75951-75960 (sharp failure) read as stated. (9) is a correct set inclusion. Remark: the note files (9) at F's native level. File instead each elementary read of Ψ_b at the stage that performs it. The collar coordinates lie in double blocks inside G_{j+1}; the remaining arguments are old, already-filed reads or shell data in some D_i. The note does not try this. UNCLEAR whether it closes; it is the obvious fourth route.

**11. L336-380, route three. CONFIRMED arithmetic; MISMATCH in what it tests.** (10)-(11) follow from G_i = H_i^{[10a_i]} and H_i ⊃ G_{i-1}. 10a_t/(ML^j) = 10R_tL^{t-j}. L372-374 (L^{4(t-j)}) is right. But the route files a whole-box read at the reader's level j. L222-224 says FCO does not require that. Filed by datum, level-i data in X lie in Ω_{i+1}^c ∩ X = O_{i+1} ⊂ G_{i+1}, by (2). The route's own repair (L366-369) defers to route two.

**12. L476-494 and L518, distinctness of the three routes. UNCLEAR as stated.** The methods are distinct: mask inclusion, chart induction, box locality. The failure points are not: all three stop at the native footprint of retained test and centre reads, (9). That is acceptable for stop (c) (one supplier). But route three adds no independent failure. Say so at L480-484.

**13. Gap in the note's own reasoning on FCO-slot. UNCLEAR, likely closable.** L168 leaves the stored-slot inclusion to §5. Inside a standing mark much of it is already in §3. Prepared data lie in D_i ⊂ O_i ⊂ G_i, by (3). The core is C_{k♭} = X ∩ Z_{k♭} = G_h. Level-i determining data in X lie in O_{i+1} ⊂ G_{i+1}, by (2). Visible slots are route one. Not checked here: island kept variables (SA 17423), collar, rim and cut-off-zone bonds (SA 17452ff), seam data, ordinary unaltered layers. Repair: a short lane FCO-slot over these cases (size S/M).

**14. Cross-link: geoh-live-ab.md §5 Theorem. Does not supply FCO. Supplies one FCO-slot case, conditionally.**
- Its assertion 2 is ownership of native cells by live strips. FCO needs ownership of reads by genealogy cells. These are different maps.
- Its assertions 5-7 separate integration sites from strips. That is disjointness, not a covering of reads. Nothing in it touches (9) or route three's boxes.
- Useful clauses: assertions 3-4 give B_Y ⊂ Ω_{m+1}^c, inside the component of Λ_i^c that contains Y, for every existing i > m. With S_Y ⊂ B_Y, a live strip's stored sites lie in the level-(m+1) node containing Y. That is FCO-slot for second-class storage, with owner level m+1 and zero collar.
- The level-m owner does not work: S_Y = Y^{(q_m)} reaches q_m ≈ R_m/2 native cubes beyond Y. That is not c_0 M-layers. It is within one boxing cell, so Finding 8's cell collar would also serve at level m.
- Needed to use it: (i) the GEOH-O1 dictionary from CA's open-endpoint class to N's revised operation (geoh-live-ab §7 claims the closed class keeps the bounds; not checked here); (ii) identify the strip with N's kept island record and its latest-owner rule; (iii) cells of level below m inside S_Y (assertion 2 allows them) need their own-level owner. geoh-live-ab is under its own check. Any use is conditional on that check.

**15. Scope and honesty. CONFIRMED.** No status is claimed. No analytic estimate is used. The 1D example and (10)-(11) are correctly called non-counterexamples. Minor: L54 cites `geoh.md:26-35`; the row is `prior/geoh.md:26`.

## Repairs, in order

1. Split FCO into FCO-slot and FCO-read. Make (15)-(18) conditional on FCO-slot (Finding 7).
2. Measure the collar in c_1 owner cells, not c_0 M-layers. Adjust C_v, (6) and b_code by fixed factors (Finding 8).
3. Run FCO-slot as a short lane from §3 (2)-(3), route one and the case list in Finding 13. Add geoh-live-ab assertions 3-4 as the second-class case, conditional on its check and GEOH-O1 (Finding 14).
4. If FCO-read is still wanted, try route two with stage filing of Ψ_b's reads (Finding 10). Hand FCO-read to the row that consumes SA 18878-18900.
5. Restate L480-484: three methods, one failure point (Finding 12).
