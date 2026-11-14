# Check: library/geoh-live-ab.md

Claude (Opus 5.5), 2026-11-08. One line-by-line check of one proof note (512 lines, Codex gpt-6-astra).
Sources: CA-I `theorem_0_complete_account_raw_I.tex` (31a47c543775), SA `YM4_sketch_500.tex`, N `YM4_1400.tex` (2bc0658f).
This check reads the note against the cited lines. It is not an audit.

## Verdict: ADVANCE

The proof of the finite-history strip invariant holds on CA's stated rules.
I found no step that fails. Two citation repairs below are optional (findings 5, 6). Neither changes a bound.

## Clause table (CA-I 85598-85644)

| Clause (CA-I line) | Exact text, short | Standing after this note |
|---|---|---|
| (a) 85602 | "s_i(Y) ≤ (101 Ř_m − 1) L^{−(i−m)} ≤ 101 Ř_i" | PROVED for i ≥ m, eq. (3). The second inequality needs i ≥ m. The note says so (line 322). |
| (b) 85606 | "A cell meeting Y♯ has level at most m and lies in Y♯. The strips of distinct live large-field regions are disjoint, and a cell lies in at most one of them." | PROVED. Section 5, eq. (13) and the cell-saturation paragraph. |
| (c) 85609 | "dist_m(Y♯, Ω_{m+1}) ≥ 5/2 Ř_m. Every cell at dist_m-distance less than 5/2 Ř_m ... has level at most m, and, for every i>m, this neighbourhood ... lies in the component of Λ_i^c containing Y." | PROVED, all three parts. Eq. (9), (12) and the collar induction. The h_1 = m remark is the case eq. (9) treats. |
| (d) 85617 | "At the site (T) ... dist_i(Y♯, Ω_{i+1}) ≥ 7 Ř_i." | PROVED. 8Ř_i for i > m; (15Ř_m+1)/2 for i = m. |
| (e) 85619 | "If C'' is not treated, then Y♯ ⊂ C'' and dist_k(Y♯, Z) ≥ Ř_k." | PROVED, at (L) and (P). Z is the running region (CA-I 64417-64420), so an exited sibling counts as untreated. |
| (f) 85622 | "Λ̃_C is a box whose sides are at most h♯ = 112 ... dist_k(Λ̃_C, Z^c) ≥ 9 Ř_k." | NOT TOUCHED. |
| (g) 85627 | "Then m ≤ h. The set C_C is a box ... Y♯ ⊂ C_C and dist_h(Y♯, C_C^c) ≥ ½(Ř_h+1). A cube ... touching Y♯ lies in Λ_C." | PARTLY. Only "m ≤ h" is derived (line 335, from class rule (ii-b), CA-I 45997-46000). The box, side, containment and touching parts are not claimed. Eq. (8) gives Y ⊂ Z_h, which a later lane can use for them. |
| (h) 85635 | "treated: dist_{h+1}(Y♯, R_ν) ≥ 5/2 Ř_{h+1} for every collar R_ν; not treated: dist_k(Y♯, R_ν) ≥ Ř_k. No integration bond of (P) lies on a strip." | PROVED, all three parts. Section 5 end and section 6. |
| (i1) 85640 | "A probe meeting Y♯ has level at most m." | NOT TOUCHED (the cell ceiling is proved; probes are not treated). |
| (i2) 85641 | "A probe meets the strips of at most 2^d live large-field regions." | NOT TOUCHED. |
| Contour hypothesis 85644 | "d^∧ obeys the triangle inequality. A contour pays at least c_∧ for each zone ..." | NOT TOUCHED. The note says so (line 490). |

## Findings

1. **Note 133-143, eq. (4). CONFIRMED.**
   Source: CA-I 50224-50226 gives "Ω_t^c = Q'^{∼2} ∪ P'^{∼4} ∪ Ŷ^{∼8} (2≤t≤K)". CA-I 50344 gives "Z[R] := (Ω_t^c)^{∼2} ∪ R^∼", boxed by M. SA 17320-17322 prints the same display.
   The layers are coarse cubes of side W_t = LMŘ_t in level-(t−1) bond units (CA-I 50153-50154). That is a_t = Ř_t u_t, as the note says.
   The input Y is "the large-field region Z_k = Λ_k^c" (CA-I 50163-50165). An island stays in Z_t (SA 17418; CA-I 64479-64497). So pockets enter T. The rule is as specified, not strengthened.

2. **Note 146-170, eq. (5). CONFIRMED.**
   Lower rule: CA-I 53783 "For h<i≤k_0, Z''_i=(Ω_i^{∼5})^c∩Z". Upper rule: CA-I 53778-53781, "Z''_i and Z''_{i-1} are 'separated by one layer' of level-i M-cubes", for i ∈ I_M. Taking i = k_0+1 covers the change of scale. h+1 ≤ k_0 is CA-I item (5), 63590-63592.
   The lower gap 3a_{i+1} ≥ u_{i+1} follows from (6) at the next index. The upper gap u_{i+1} is the specified one-layer rule.

3. **Note 172-210, eqs. (6)-(7). CONFIRMED.**
   The window is open: CA-I 45997-46000 excludes class components of R at "k' ∈ (k−N_k, k)". CA-I 46024-46027 says the geometric arguments "need only k' ≥ h+1".
   The tracing uses only steps h+1, ..., k−1. A heal at s removes level h on its own component (Ω_l ∪ X for l ≤ s). An island at s > h does too (SA 17418). An interruption at s ∈ (h,k) makes C ineligible. A heal of another component cannot meet the connected buffer N_8 H, which lies in the trace's own component of Z_s.
   The erosion is right. A cell in N_3 H is at index distance ≥ 6 from any cell outside N_8 H, so five layers added to Ω_{h+1} miss it.
   This is N 63718-63736 with "marks at levels h,...,k-1" (N 63727-63729) replaced by the open window. The replacement is valid because the operation at h comes before T at h+1.

4. **Note 212-222, eq. (8); note 238-260, eqs. (9)-(10). CONFIRMED.**
   3LŘ_{m+1} − q_m ≥ 3Ř_m − (Ř_m−1)/2 = 5Ř_m/2 + 1/2. This uses Ř_m ≤ LŘ_{m+1} (CA-I 63566-63569, proved at 63645-63648).
   After the first replacement, Ω_{m+1} ∩ C = C \ D_{m+1} (SA 17422-17426). So the bound is exactly clause (c)'s width, and the h_1 = m remark at CA-I 85613-85616 is this case.

5. **Note 148-150. MISMATCH (citation only).**
   The note says the five-layer rule "is the convention stated in I 63703–63716". Those lines are item (5)'s proof. They give the cube side L^{-(k-j)}MŘ_j and h+1 ≤ k_0, but not the five layers. The five-layer rule is at CA-I 53783.
   Repair: cite CA-I 53783 for the five layers and keep 63703-63716 for the layer side.

6. **Note 161-163 and status row 501. MISMATCH (attribution only).**
   N 63773-63825 builds boxes H_i^{[3a_i]} from the quiet class. That class bars joining and marks at h (SA 17575; N 63727-63729). The note's class allows both, so N's box formulas do not apply as written.
   The proof does not need them. The lower gap is proved from (6), with "no box equality" (line 208). The upper gap is the CA-I 53778-53781 rule.
   Repair: say N's quiet boxes are the special case without joining, and that the upper gap is taken from CA-I 53778-53781. Remove "quiet-box construction ported" from row 501.

7. **Note 262-276, the n^+ = n+1 branch. CONFIRMED.**
   CA-I 64429-64433: "on that branch n^+(C')=n(C')+1, since there the change of variables of the next stage is made ... while its fluctuation integral is not". Exit (e4) at CA-I 132013-132016 has n ≤ N−1 and n^+ = n+1. For n = 0, level h+1 = m+1 is relabelled to C \ D_{m+1}, so (9) holds. For larger n^+, only higher levels change. This is the worst case, and it leaves 5Ř_m/2 + 1/2.

8. **Note 278-300, the next cycle. CONFIRMED.**
   (11): S_Y ⊂ Z_k, and eight layers of side LŘ_{k+1} give ≥ 8Ř_k > 7Ř_k.
   R_{k+1} cannot treat the component: the mark at k lies in (k+1−N_{k+1}, k+1) because N_{k+1} > N_0 ≥ 2 (CA-I 53773).
   Later attempts have h_b ≥ k: CA-I 132165-132172 proves "k_a ≤ h_b" ((T2)). So Ω_{m+1} is never relabelled again while the pocket lives.

9. **Note 324-430, the induction. CONFIRMED.**
   Each move is covered.
   - T: it leaves earlier entries alone, and failures and boxing only add sets.
   - Joining: it keeps B_Y in one component.
   - Healing or island of another component: it cannot meet B_Y, which lies in Y's own component.
   - Completed operation on Y's component: Y dies (CA-I 63540-63543).
   - Interruption or exclusion: h ≥ m, by (ii-b) and the birth factor (CA-I 63864-63867). For h > m it leaves Ω_{m+1} alone; for h = m, (9) applies.
   - Births: the old pocket in C dies. Other old strips lie in other components. Eq. (13) gives Ř_k − q_k ≥ (Ř_k+1)/2.
   Simultaneous births are ≥ Ř_m − 2q_m ≥ 1 apart, as in CA-I 20455-20457.
   Raises occur only in Z \ Z''_i (CA-I 64862). D_{h+1} contains B_Y, so the collar is never raised. The constants are 5/2, 7, 1 and 1/2. None depends on age, attempt count or outcome.

10. **Note 402-411, assertion 6 and siblings. CONFIRMED.**
    CA-I 64417-64420: Ba{\l}aban "continues to denote by Z" the running region. So in (e), an exited sibling is not treated. Its strip lies in its own component, which is ≥ Ř_k from every running component. The treated bound in (h) also holds for every collar outside the own component, because D_{h+1} ⊂ C.

11. **Note 432-474, integration sites. CONFIRMED.**
    The coordinate sets at CA-I 74313-74318 lie outside Z''_{j+1}. The incident-bond count at CA-I 159071 is the larger convention. Bond length is u_j/M.
    - Stage 1: (15) gives 5/2 Ř_{h+1}u_{h+1} > u_h.
    - Later stages: gap (5) gives u_{j+1} > u_j.
    - Main integration: it meets the strip. It is site (L), not (P). It ends the pocket's life. The note reports this honestly (line 465).

12. **Note 484-487, open vs closed endpoint. CONFIRMED.**
    SA 17435 says marks satisfy "s < t_♭". SA 17575 quarantines "[k_♭,k), the lower end point included". Under SA, a mark or pocket at h is excluded, so h = m never occurs and the wider T-collar survives. The same induction then holds with the critical case empty.
    The note does not claim that SA's class and CA's class give the same histories, or that any revised operation implements either one (GEOH-O1).

13. **Note 476-492, scope. CONFIRMED.**
    The claim is a finite-history geometric invariant from stated rules. It makes no claim about contour, norm, probe or measure. It does not assume (b)-(e) or (h). It does not use CA-I 64468-64472, which would be circular.

## Who checked what

Checked line by line by Claude (Opus 5.5) against the cited CA-I, SA and N lines. Codex wrote the note. This is the only other-model reading.
