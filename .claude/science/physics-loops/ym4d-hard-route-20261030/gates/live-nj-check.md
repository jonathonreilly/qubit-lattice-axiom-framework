# Check of library/live-nj.md

Checked line by line by Claude (Opus 5.5), 2026-11-08. One reading. Not an audit.
Note at clone `3d5dfc445` (455 lines, Codex gpt-6-astra).
Sources, local copies: CA-I raw (I), YM4_sketch_500 (SA), YM4_1400 (N).

## Verdict: FIX

Every step I checked is correct. No bound fails. No constant depends on the history.
One gap must be closed before outward use. The note computes the core only in the form of I 63870.
It never computes the account's defining form, I 78969 (also I 93532).
The equality of the two forms is exactly what failed under joining in `live-fgi.md`.
Under the no-joining rule the two forms agree. The repair is one short paragraph (finding 6).
After that repair the note supports outcome (a) as stated.

## Findings

1. **The rule (note 53-84; SA 17575, 17440; N 63684, 73101-73110).** CONFIRMED.
   SA 17575 and N 63684 have the same text. It says "for k_flat ≤ i ≤ k the set X∩Z_i is a single component of Z_i and is small".
   It also says "it does not absorb a second component, X∩Z_i=Φ_i(X∩Z_{i-1})" and quarantine "in [k_flat,k), the lower end point included".
   N 73101-73110 repeats "quarantine ... including its lower endpoint" and "single-box traces". SA 17440 has "Marks wait" and s < t_flat.
   The note's cutoff 100 is N's own cutoff (N 63763-63764). It equals the account's (i) and the boxing smallness test (I 50074-50077, 100 W_t = 100 a_t).
   Restriction of I 45992-46000: rule 1 gives (i) and the window size bounds of (ii-a). Rule 2 gives no creation at T_{j→j+1}, h ≤ j ≤ k-1. Rule 3 contains (ii-b), whose window (h,k) lies inside [h,k).
   The note correctly says the two runs differ as histories (note 83). Declining an attempt is a valid transition of the prior induction (note 110).

2. **m < h and S ⊂ G_h (note 115-125, eqs. (1)-(2)).** CONFIRMED.
   An island is a marked component (SA 17433, "Islands and drop-outs are the marked components"). R_m acted on Y, so quarantine forces m ∉ [h,k). Since m < k, m < h.
   Prior clause (c) puts the strip's collar in the component of Z_i containing Y for every i > m. With i = h and rule 1 this is G_h.
   The note should cite SA 17433 for "an island carries a mark". Optional.

3. **Quiet boxes and preparation (note 131-213, eqs. (3)-(6); N 63716-63834).** CONFIRMED.
   Tracing matches N 63716-63746. The restriction argument for a step with no creation is N 63697-63714.
   G_h is a box: it is a small component of a boxed step output (I 50074-50092), and no operation at a level ≥ h touched it.
   The hull of a box is a box; G_{i-1} ⊂ H_i ⊂ G_{i-1}^{[a_i]}. Eqs. (3), (5) match N's two displays.
   I checked the gaps by hand. Lower gap 3a_{i+1}. Change of scale gap u_k (I 63685: Z''_{k0+1} = (Z'_{k0})^~). Upper gaps u_{i+1}.
   First upper pair: w_{k0+2} < L u_k/(L-1) ≤ 3u_k/2, so the gap is at least u_k/2 > u_k/L ≥ u_{k0+2}. If k0+2 = k the gap is 2u_k.
   Endpoints (6): D_{k0+1} = H_*^{[u_k]}, D_k = H_*^{[3u_k]} = (Ω_{k0+1}^{~5})^c ∩ C (I 53783, 63788-63792).

4. **Clause (f) (note 215-257, eqs. (7)-(9); I 63788-63857; N 63827-63834).** CONFIRMED.
   Λ_C = H_*^{[4u_k]} and Λ̃_C = H_*^{[5u_k]}; both are boxes of level-k cubes.
   side(G_{k0+1}) = side(H_*) + 20u_k ≤ 100 u_k, so side(Λ̃_C) ≤ 90 u_k ≤ 112. Level-k unit is u_k (I 63815-63819).
   Λ_C ⊂ G_{k0+1} ⊂ G_{k-1} ⊂ H_k and C = H_k^{[10a_k]}. So dist_k(Λ̃_C, Z^c) ≥ 10R_k - 1 ≥ 9R_k.
   Z^c ⊂ C^c under either reading of Z (step-k region, I 63778, or running region), so the bound holds.
   The bounds hold at every treated step with the same constants.

5. **Clause (g): side, cell union, margin, touching cubes (note 259-303, eqs. (10)-(12)).** CONFIRMED.
   Side: 100R_h + 4LR_{h+1} ≤ 104LR_{h+1} in level-h units (I 63872-63877), using rule 1 at i = h.
   Cell union: the core lies in O_{h+1} before stage 1 and in D_{h+1} after it. So it lies in Ω_{h+1}^c at every P or L site.
   A cell of level n ≥ h+1 lies in Ω_n ⊂ Ω_{h+1} (I 62766-62770). Faces lie on the a_{h+1} grid, and a_{h+1}/u_h = LR_{h+1} is an integer. Nested grids then give a union of whole cells.
   This is a valid alternative to the account's moat argument (I 63879-63892).
   Margin: S ⊂ G_h ⊂ H_{h+1}, so dist_h(S, C_C^c) ≥ LR_{h+1} ≥ R_h ≥ (R_h+1)/2.
   Touching: S ⊂ D_{h+1} ⊂ D_k. A cube of side u_j ≤ u_k touching S lies in D_k^{[u_k]} = Λ_C.
   Small completeness point (note 267): Z'_h is the hull of all of Z_h, not only of G_h.
   Other components A of Z_h lie in other components of Z_k, since C ∩ Z_h = G_h. Then hull(A)^{[a_{h+1}]} ⊂ N_10 hull(A) ⊂ Z_{h+1} stays in that other component. So intersecting with C still clips nothing. Add one sentence.

6. **Clause (g): C_C a box under both forms (note 261-268).** MISMATCH (omission).
   The note uses only I 63870, C_C = (Z'_h)^~ ∩ C. The account's definition is I 78969, "C_C := (Ω''^{~2}_{h+1})^c ∩ C = Z'^~_h ∩ C". I 93532 gives only the first form.
   `live-fgi.md` showed these two forms can differ under joining. The task asked for both.
   The note never cites I 78969, I 93532 or I 63887.
   Repair, checked by hand. Ω''_{h+1} = (Z''_{h+1})^c (I 63887), and Z''_{h+1} ∩ C = D_{h+1} = H_{h+1}^{[3a_{h+1}]}.
   D_{h+1} is at distance 7a_{h+1} from C^c, since C ⊇ G_{h+1} = H_{h+1}^{[10a_{h+1}]}. So only C \ D_{h+1} matters near the core.
   Adding two layers of a_{h+1}-cubes to it removes two layers from the grid box D_{h+1}. The result is H_{h+1}^{[a_{h+1}]}.
   So (Ω''^{~2}_{h+1})^c ∩ C = H_{h+1}^{[a_{h+1}]} = (Z'_h)^~ ∩ C. Both forms give the same box, and the identity in I 78969 holds on this class.
   Insert this after eq. (10), with the three citations.

7. **Clause (i1): separation in the probe's own units (note 305-402, eqs. (13)-(17)).** CONFIRMED.
   This is the new step. The lemma dist_n(S, Ω_n) ≥ 3 for every existing n > m is proved by a complete case split.
   - T at n: S ⊂ Z_{n-1} if m < n-1, giving 8R_n. If m = n-1, the reach is q_m/L ≤ R_m/(2L) ≤ R_n/2, giving 15R_n/2. Uses R_m ≤ LR_{m+1}.
   - Foreign R: components of Λ_k^c are at distance ≥ R_k in level-k units (I 63549-63553). In level-n units this is R_k L^{k-n} ≥ 38.
   - Own R, h < n ≤ k_0: 3R_n. k_0 < n < k: D_n ⊇ H_*^{[u_k]} gives L^{k-n} ≥ 3. n = k: D_k = H_*^{[3u_k]} gives 3.
   - Levels n ≤ h are not changed. Prefixes, the n^+ = n+1 raise and every Ω^ν are built from these same sets.
   Every bound is at least 3 > 2. A probe lies within 2 of its cell Δ_n ⊂ Ω_n (I 62779-62788). So a probe of level n > m misses S.
   This also supplies I 63920's missing "clause (c′)" input (5/2), with room to spare.

8. **Clause (i2) (note 404-428; I 63926-63933).** CONFIRMED.
   By (i1), n ≤ m, so the probe side is at most 5L^{n-m} ≤ 5 birth units.
   Strip sides are at least R_m ≥ 38, by I 63549-63555 and 63657-63660, not by clause (a). The note says this correctly.
   The interval argument is right. An intersecting interval that is longer contains an endpoint of the shorter one.
   Prior clause (b) gives disjoint closed strips, so each vertex lies in at most one strip. That gives at most 2^d.

9. **Clauses (a)-(e), (h) under the rule (note 106-129).** CONFIRMED.
   The prior induction only needs h ≥ m and the endpoint case. Its timing inputs (gates/geoh-live-ab-check.md, findings 8, 12) become stronger under quarantine.
   The case h = m is empty by finding 2. The constants are the prior ones: 101, 5/2, 7, 1, 5/2.

10. **Constants (task item 6).** CONFIRMED.
    The constants are 112 (90 in fact), 9R_k, 104LR_{h+1}, (R_h+1)/2, 3 and 2^d. None depends on age, attempt count, test outcome or number of components.

## Clause table under the outlines' rule (after the repair of finding 6)

| Clause | Standing | Where |
|---|---|---|
| (a) | Proved, i ≥ m | geoh-live-ab eq. (3) |
| (b) | Proved | geoh-live-ab section 5 |
| (c) | Proved; case h = m is empty | geoh-live-ab sections 3-5; note eq. (1) |
| (d) | Proved | geoh-live-ab T-buffer |
| (e) | Proved | geoh-live-ab sections 5-6 |
| (f) | Proved: box, sides ≤ 90 ≤ 112, distance ≥ 9R_k | note section 4 |
| (g) m ≤ h | Proved, in fact m < h | note eq. (1) |
| (g) box | Proved for I 63870's form; I 78969's form needs the paragraph of finding 6 | note eq. (10) + repair |
| (g) cells, side, margin, touching | Proved | note eqs. (11)-(12), section 5 |
| (h) | Proved | geoh-live-ab sections 5-6 |
| (i1) | Proved: dist_n(S, Ω_n) ≥ 3 for all n > m | note section 6 |
| (i2) | Proved: at most 2^d | note section 7 |

## Who checked what

Codex wrote the note. Claude (Opus 5.5) checked it line by line against the cited I, SA and N lines. This is the only other-model reading.
The no-joining rule changes the class. It does not match the account's class or a different revised operation (GEOH-O1).
