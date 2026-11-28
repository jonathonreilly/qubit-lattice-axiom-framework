Verdict: FIX

# Check: library/fco-slot.md (613 lines, Codex gpt-6-astra)

Claude (Opus 5.5), 2026-11-08. One line-by-line check of one proof note, by one other model. Not an audit.
Clone at `5b818235d` (branch `claude/ym4d-hard-route`).
Read in full: the note, its task file, `gates/uo2-geo-check.md`, `gates/geoh-o1-check.md`. Read in part: `uo2-geo.md` 171-230, `ti-2.md` 30-90, `geoh-o1.md` 1-140, `geoh-live-ab.md` 306-430, `in1.md` 60-76.
Source lines read: Y 64048-64078, 65172-65185, 71902-71908, 74615-74672, 75842-75962, 78864-78940; SA 17270-17276, 17354-17358, 17418, 17436-17460, 17518-17532, 17604, 17642-17654, 18085-18092, 18450-18460, 18620-18632, 18836-18858. Lines of I were not checked.
Every step was redone by hand. No numerics.

## Summary

The case check and the counts are correct. The constants are fixed before R and do not depend on the history.
FCO-read is correctly left out. The code count (11)-(13) and the reserve bound (16) follow.
The defect is scope. "The specified revised rules" are N's (Y's) two-range nest, Y 63773-63825.
They are not ti-2's thin rule (N). The note never cites ti-2. GEOH-O1 showed the two nests differ.
The proof transfers to ti-2 with one short paragraph (Finding 3). The note must add it or narrow its claim.

## Findings

**1. L6, L88-97, the statement. CONFIRMED.** It is the task's target: stored slots only, a collar of c owner cells (not M-layers), multiplicity per owner site and per native site. Constants are claimed independent of depth, volume, stage and floor.

**2. L57-64, the ports. CONFIRMED.** Y 78906-78916 gives the four owner rules as stated ("Charge an unaltered layer site to its action cell ... Charge a site in a redone determining layer to the local history of the mark that remade it ... Prepared means are charged to their owned level cells ... use the latest operation owning the remade slot"). SA 17440-17449: a mark of level s inside a class component of level t has s < t_♭; "their windows (s_♭,s] are disjoint". The chain and cut ports were confirmed in uo2-geo-check findings 1-4.

**3. L59-60, L67-70, which nest. MISMATCH.**
- The note fixes "the explicit two-range preparation in Y 63773-63825". SA 17421 writes its drop-out labels as X \ Z''_l. That is the CA/N nest.
- ti-2.md 43-50, as it stands: "D_a:=C and, for a<i≤k ... α_i:=max{u∈F_i: u≤α_{i-1}-m_i}, β_i:=min{u∈F_i: u≥β_{i-1}+m_i}, F_i=m_i(Z+1/2)". geoh-o1.md outcome (b) and geoh-o1-check finding 6: these give different labels.
- So the theorem as written is about N's nest, not ours. L69 defers the match to GEOH-O1. That deferral is honest but leaves FCO-slot unproved for ti-2.
- What the slot argument actually reads from the nest (my check, once):
  (a) G_h = D_h ⊂ D_{h+1} ⊂ ... ⊂ D_t. ti-2 gives D_a = C = G_h and (N1).
  (b) D_i ⊂ O_i ⊂ G_i. ti-2 (N3) gives D_i ⊂ A_i = H_i^{[8]} = O_i.
  (c) Ownership of collar and inner rows (L168-174). C_j ⊂ O_{j+1} and inner rows in D_{j+1} hold for any nest. The double-block reach (two owner spacings) is inside one cell for any nest.
- So §§3-4 hold with D_i the ti-2 nest. The constants do not change.
- Not transferred by this: the validity of Y's row chart and prefix list (Y 75842-75960) for the thin first member. Y's first-stage clause ("the collar uses at most five of the eight layers") is CA/N-specific. Its compressed-stage clause ("the spacing of the prepared faces is at least one level-(j+1) M-cube, which exceeds the double-block reach") holds at every ti-2 stage by (N2). That is an operation fact for the ti-2 readers and GEOH-O1, not a slot fact.
- Repair. Add a paragraph after L70: "With ti-2 (N), the proof uses only (N1), (N3) and D_a = G_h. Sections 3-4 then hold unchanged. The row chart for the thin first member is a ti-2/GEOH-O1 input." Or adopt the hybrid of geoh-o1-check (first member Z''_{h+1}); then Y's first-stage clause applies directly.

**4. L118-125, ordinary storage. CONFIRMED.** SA 17528-17532: "On Ω_{j+1}^c, step j+1 stores V_j"; A' lives on Ω_{j+1}\Λ_{j+1}; the coupling "stops on the whole of Z_{j+1}, including Ω_{j+1}\Λ_{j+1}". So both sets lie in Z_{j+1}.

**5. L127-143, masks and visible slots. CONFIRMED.** SA 17356 defines the collar (distance ≤ ϖ_T) and rim. SA 17459 records the three bond sets separately. SA 17518-17526 makes the substitution "bond by bond, with new variable W'" and takes pivot values "from the constraint". Visible assignments are sa-2.13 (6.1)-(6.3).

**6. L147-166, (1)-(2). CONFIRMED.** Both are direct from O_{j+1} := X ∩ Ω_{j+1}^{◦c} and Z_{j+1}^◦ ∩ X = G_{j+1}. Y 75845-75846 has C = (Ω_{j+1}^c \ Y) ∩ Z.

**7. L168-174, rows. CONFIRMED.** Y 75849-75860: an R_in double block lies in Y; an R_col double block "lies outside Ω_{j+1}" in the same component. So it lies in O_{j+1}; no collar is needed. Wording: "in the old hole" (L170) should read "outside the old Ω_{j+1}".

**8. L176-205, shells, core, main box, prefixes. CONFIRMED.** The shell-datum dichotomy (D_{i+1} if remade, O_{i+1} if not) is correct. Y 75951-75960: the sharp failure retains the nonpivots and translated density, "no integrated normaliser". Earlier failures precede the pivot change.

**9. L207-243, islands and live strips. CONFIRMED.** SA 17418: "T'_t(X) is kept together with its variables, its measure and its factors". SA 17654 lists the drop-out retention as stated. The live-strip shortcut is optional (L242). Remark for ti-2: geoh-live-ab assertions 3-4 use its (9) only when h = m. With the closed endpoint, h > m, and its "Ω_{m+1} unchanged" branch serves for any nest. The birth reach q_m ≤ (R_m-1)/2 M-cubes is under one cell.

**10. L245-270, seams and discrete anchors. CONFIRMED.** Y 74655-74669: fixed alphabet, "a fixed finite number of such tests is attached to each site or bond", headers a power of R_n+1, and "another discrete choice must include its code". The note keeps that limit (L270).

**11. L272-309, c = 6. CONFIRMED.** Y 65177-65181: the read "reaches at most 2LM_2Ř_m+1 beyond the base ... less than one cell by the choice of M", with cell side LMŘ_m. Y 71905: "M ≥ L^2M_2". Endpoint plus double block ≤ 3 owner spacings ≤ MR_n. Storage collar, ϖ_T collar, test reach: one cell each. Masks: two (SA 17459). Sum 6. The test reach is not needed for a slot anchored in a created cell; the overcount is harmless.

**12. L311-330, multiplicity in time. CONFIRMED.** Disjoint windows (SA 17440-17449) give one remaking index per place. An island keeps the older window. Healing fills Z_n at that place; no later step remakes level n there (SA window lemma, same paragraph).

**13. L332-367, μ, A_c, C_d. CONFIRMED.** μ = 2·2·5·τ. A_c = 13^4 counts collars and cells. C_d = 2 (owner levels) · 2 (cut) · A_c · μL^4. Minor: "five geometry uses" (Y 73147-73158) and J (uo2-geo.md 441-442) are not defined here; cite them.

**14. Constants. CONFIRMED.** c, A_c, μ, τ, J, K, K_f, p, D ≤ L^4+3^4+2 and c_R = log(2^{r+1}L)+r depend only on L, r and the fixed template. They are fixed before R and do not depend on depth, volume, stage, floor or history. M enters only through w(a).

**15. L377-411, FCO-read left out. CONFIRMED.** Storage filing through Ψ terminates. (7) is a correct inclusion. No step of (11)-(17) reads a full read region. SA 18878ff is the consumer.

**16. L413-440, restated UO2-geo and (8). CONFIRMED at slot scope.** (8) is a port of sa-2.13 (6.2)-(6.4); its constants were not rederived here.

**17. L442-505, code count (9)-(13). CONFIRMED.** Per occurrence: A_cJμL^4(MR_n)^4 log K + log 2 + log(3K_f) + p c_R ℓ_n ≤ b_code w(a), using ℓ_n ≥ 1. Then D^{2(N-1)} e^{-(2 log D + log 2)N} sums to ≤ D^{-2}. SA 18703 has c_e ≥ b + 2 log D + log 2.

**18. L507-554, reserve (14)-(17). CONFIRMED.** SA 17274: v "counts log x_j for each stored site of level j". SA 18087-18089: "including the assigned collars and the operation's fixed coordinate multiplicities". Each occurrence contributes ≤ A_c(MR_n)^4 · μL^4 · 2ℓ_n. So v ≤ 2A_cμL^4 v^natural, with v^natural from in1.md (6). (17) is immediate.

**19. L556-582, (18)-(19). CONFIRMED as conditional ports.** SA 18629 and 18848-18855 match. The note's q and c_ent are SA's c and c_e.

**20. L584-613, scope. MISMATCH, minor.** L586 and the status table say "the specified revised rules" without naming the nest. "First open input: None" holds only for N's nest. Repair: name the nest, and add the Finding 3 transfer or list it as the first open input for ti-2.

## Repairs, in order

1. Add the ti-2 transfer paragraph (Finding 3), or narrow L6, L586 and the table to N's nest.
2. Name the ti-2 row chart and prefix list for the thin first member as an input owned by ti-2/GEOH-O1 (Finding 3).
3. Cite J and the five uses; reword L170 (Findings 7, 13).
