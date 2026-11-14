# Check: library/leaf-hy.md

Claude (Opus 5.5), 2026-11-08. One line-by-line check of one proof note (544 lines, Codex gpt-6-astra).
Clone at `3d5dfc445` (branch claude/ym4d-hard-route).
Sources read: Y = YM4_1400.tex (2bc0658f) 63736-63825, 75842-75870, 75930-75960; CA-I (31a47c543775) 53770-53815, 63643-63649, 63906-63916, 64420-64442, 74309-74320; SA (31a47c543775) 7511-7518, 17328-17334.
Repo inputs read: hstep-tree §9, geoh.md §§1-2, geoh-gate.md 25, geoh-o1-check, geoh-live-ab §§2-6, fco-slot §2, geo-2 §6, geo-3 §2, ti-2 (N) and its reader table, st1-r4 Lemma 2, pda.md §3, geo-prop23 §3.
This is one reading by one other model. It is not an audit. Every step was redone by hand. No numerics.

## Verdict: ADVANCE

Outcome (a) holds for the two leaves as tree §9 states them.
Both kill tests are run correctly. HY-UNITS fails the proposed \(B+8L\) and closes with \(\widehat B=B+8LK_R\).
HY-READS is correct. Every geoh-live-ab premise that changes is supplied.
Three repairs are wording and handoff only (findings 14, 16, 17). One adds a missing one-line inclusion (finding 13). None changes a proof.

## Findings

| # | Note line | Source line | Claim checked | Result |
|---|---|---|---|---|
| 1 | 58-65 (K1) | hstep-tree 625-627 | \(a_{h+1}=R_{h+1}u_{h+1}=LR_k\cdot Lu_h\). So the two-sided \(3a_{h+1}\) erosion adds \(6L^2R_ku_h>8LR_ku_h\). | CONFIRMED |
| 2 | 70-92 (K2)-(K3) | SA 17334; SA 7514-7516; geoh.md 9-17 | SA rounds \((\log\min_{i\le k}x_i)^r\) up to a power of L. With \((\log T)^r=R\), \(x_3=T\) gives \(R_3=R\). \(x_0,x_1,x_2\in(T,e^{(LR)^{1/r}})\) give \(LR\). \(x_k>e^{(R/L)^{1/r}}\) keeps \(R_k=R\). One drop, at 2 to 3. \(x_i-x_j=b(j-i)\) meets the frame for an allowed slope. \(N_k=R\), \(k=R+1\), so \(h=1\). | CONFIRMED |
| 3 | 94-104 | geo-prop23.md 51-64; Y 63757-63771 | \(C=E_1^{[6a_1]}\) has side \(13a_1<a_2\). \(G_2\) has 21 cells. \(a_3=a_2\) gives \(H_3=G_2\), \(G_3\) 41 cells. \(41/27<2\), so \(H_4\) is at most 3 cells and \(G_4\) at most 23. Then 21. All below 100. For \(i\le R\), \(i-N_i\le0\), so no earlier operation. | CONFIRMED |
| 4 | 106-114 (K4) | Y 63799-63804 | \(H_2=E_2\), so \(D_2=E_2^{[3a_2]}\) has side \(7a_2=7L^2Ru_1\). \(B=13L\) is exact. \(7L^2>21L\) for \(L>3\). Precision: this refutes the implication with B the instance's starting constant. With a class-wide \(B=100K_R\) this record need not violate \(B+8L\). The note says it does not refute a larger fixed constant (line 114). Correct scope. | CONFIRMED |
| 5 | 118-137 (K5) | CA-I 63643-63649, 63908-63912; geoh-live-ab (9) | \(3R_{h+1}-(R_h-1)/(2L)\ge\tfrac52R_{h+1}+\tfrac1{2L}\) uses \(R_h\le LR_{h+1}\). Level-h form: \(3LR_{h+1}-(R_h-1)/2\ge\tfrac52R_h+\tfrac12\). Both lines redone. \(B_Y\subset D_{h+1}\), and the stage-1 stop writes \(\Omega_{h+1}\cap X=X\setminus D_{h+1}\). The first kill test passes. | CONFIRMED |
| 6 | 139-147; 437-476 (P2) | CA-I 64420-64442; Y 75953-75960 | CA: \(n^+=n+1\) only at (1.55); band at level \(h+n+1\), datum \(V_{h+n+1}\); chain terms \(1\le i\le n\); raised cells and bands kept. Y: determining list may stay the pre-stage one; collar nonpivots and translated density kept; no integrated normaliser. The table at 466-472 matches both. The second kill test passes, and the n-only record fails it. | CONFIRMED |
| 7 | 158-172 (U1)-(U2) | geoh.md 63-74 (Lemma 1, (4)); geoh-gate.md 25 | \(R_{t-N_t}\le K_RN_t\), \(N_t=R_t\), \(K_R=L2^{r-1}(1+r^r\overline B)\). Monotone radii give (U2). Precision: Lemma 1 needs its floor on \(X_0\), depending only on \(L,r,\overline B\). The note's "under its stated floors" covers this. | CONFIRMED |
| 8 | 174-186 (U3) | Y 63750-63765 | \(G_{i-1}\subset H_i\subset G_{i-1}^{[a_i]}\), \(O_i=H_i^{[8a_i]}\), \(G_i=H_i^{[10a_i]}\), \(G_k=X\). Exact. | CONFIRMED |
| 9 | 188-226 (U4)-(U7) | Y 63799-63804; ti-2 (N), (N2) | First face move \(\le a_{h+1}+3a_{h+1}\). Two faces: \(8a_{h+1}=8LR_{h+1}u_h\le8LK_RR_ku_h\). Later moves \(<2u_j\) each face. Geometric sum \(\le4Lu_i/(L-1)\). (U7): \(B_0R_h\le B_0K_RR_k\). Prior work not credited: geo-3 (2.4)-(2.6) already proves \(R_a\le L2^rR\) and applies geo-2 (6.1) with \(B=b_{\rm box}D_R\). That is the same \(R_h\to R_k\) conversion. | CONFIRMED; credit missing |
| 10 | 227-259 (U8)-(U10) | geo-2.md 158-182 | With \(K=2\): \(C_{\rm side}=\max\{\widehat B,4/(L-1)\}\), \(C_{\rm tops}=\max\{\widehat B,4L/(L-1)+1\}\). Shell length in sites \(M\{\widehat BR_kL^{h-j}+4L^2/(L-1)\}+1\). Main-box count \(M\{\cdot+4L/(L-1)+2\}+1\). Both are below \(C_{\rm tops}M(R_kL^{h-j}+L)\). | CONFIRMED |
| 11 | 261-271 (U11) | geo-2.md 22-24; geo-3 (2.6) | \(sL^{-s}\) decreases for \(s\ge1\). One threshold serves all later radii. \(\operatorname{side}\Lambda\le(1+4L/(L-1)+2)u_k<7.2u_k\). \(\widehat B\) depends only on \(B_0,L,r,\overline B\). Order of constants kept. | CONFIRMED |
| 12 | 281-318 (H1)-(H3) | Y 63806-63815; ti-2 (N1)-(N3) | \(R_{h+1}\) odd puts \(a_{h+1}(\mathbb Z+\tfrac12)\) in \(F_{h+1}\). Odd L gives \(F_i\subset F_{i-1}\). Induction: \(D_i\subset D_{i-1}^{[2u_i]}\subset H_i^{[2u_i]}\subset O_i\), since \(2u_i\le8a_i\). Base \(D_{h+1}\subset O_{h+1}\). Gaps \(3a_{h+1}\) and \(u_i\); both are at least LM in level-(i-1) sites. | CONFIRMED |
| 13 | 320-324 | CA-I 53786-53803; geoh.md (3) | \(\Lambda=D_k^{[u_k]}\subset X\) is shown. CA and GEOH (3) also state \(\Lambda\subset\Omega^{\circ c}_{k_0+1}\cap X\). The note does not show this. It holds: \(\Lambda\subset D_{h+1}^{[(2L/(L-1)+1)u_k]}\subset D_{h+1}^{[8u_k]}\subset H_{k_0+1}^{[8a_{k_0+1}]}=O_{k_0+1}\), using \(a_{k_0+1}=u_k\) (Y 63776-63778) and \(D_{h+1}\subset G_{k_0}\subset H_{k_0+1}\). Also, \(\Lambda\) is a new choice. Tree §9's root does not specify it. | UNCLEAR (gap in text; repair below) |
| 14 | 326-345 | ti-2 (N4) | Isometries fixing every \(F_i\) are signed permutations with translations in \(u_k\mathbb Z^4\). \(a_{h+1}/u_k=R_{h+1}L^{1-R_k}\le LK_R/\widehat B\le1/8\). It is a power of L, so \(a_{h+1}\mid u_k\). (N4) holds. | CONFIRMED |
| 15 | 347-401 (H4)-(H5), reader table | geoh-live-ab (5)-(9), (12)-(15), §5 assertions 1-7, §6; CA-I 74309-74320 | Each row matches what geoh-live-ab reads. (6)-(8) read only \(D_{h+1}\). (5) is read only for its gaps; (H3) supplies them. §6 masks match CA-I 74314-74320 inside X. Bond length \(u_j/M\le u_j<\) the gap. Main box contains \(D_k\). | CONFIRMED |
| 16 | 403-407; 542 | fco-slot.md 66-79 | The three nest facts hold: \(D_h=G_h\), (N1), and \(D_i\subset O_i\) for \(h<i\le k\). But fco-slot's class uses ancestral quarantine **with the lower endpoint included** (fco-slot 70-72). The hybrid keeps CA's **open** endpoint. The note says the remaining class assumptions are kept. That is true, but it hides the clash. fco-slot does not yet cover the hybrid's open-endpoint histories. Also, fco-slot 78-79 left Y's first-stage "five of the eight layers" clause open for the thin member. The hybrid's first member is Y's own, so Y 75863-75865 now supplies it. The note does not say so. | CONFIRMED for nest facts; MISMATCH in class scope |
| 17 | 409-435 (P1) | SA 17421-17426; CA-I 53806-53814 | Bottom splice \(O_h\subset G_h=D_h\subset D_{h+1}\). Top splice \(D_{h+s}\subset G_{h+s}\subset H_{h+s+1}\subset O_{h+s+1}\). | CONFIRMED |
| 18 | 478-512 | geoh-live-ab §§4-5; CA-I 132162-132176 (cited there) | Every exit, including \(n=0,p=1\) and \(n=1,p=2\), keeps \(B_Y\) inside \(D_{h+1}\). Raised bands lie outside \(D_{h+1}\). For \(m<h\), \(\Omega_{m+1}\) is unchanged. The induction transfers. | CONFIRMED |
| 19 | 514-526 | geoh-o1-check 63-69 | Handoff says no further hybrid leaf and the next boundary is FM-MATCH. That is too broad. See the consumer table. | MISMATCH (scope wording) |

## Consumers of ti-2 (N) under the hybrid

| Consumer | What it reads | Covered by the note? |
|---|---|---|
| geo-2 §6 (6.1)-(6.2) | initial side and per-step bound K | Yes, (U5)-(U10). |
| geo-3 §2 (2.2)-(2.6) | containment \(D_i\subset A_i\), junction clearance, final box | Yes in substance: (H1)-(H2), (P1), (U11). geo-3 is not named. Its K bound (2.2) does not hold at the first move; nothing downstream reads it beyond (6.1). |
| geo-4, geo-5 (3.1), cond-c, geo5c-count | nesting, \(D_i\subset O_i\), gap \(\ge m_i\) or LM, face grid | Yes, (H2)-(H3) and the grid paragraph. Not named. |
| inn-213 §7, inn-fix | nest box \(N_c\) via geo-2 §6 | Yes, constant change only, via (U9)-(U10). Not named. |
| sa-2.8-terms Lemma W (GEO3) | \(C_n\) via geo-2 §6 | Yes, \(C_n=C_{\rm side}\). Not named. |
| st1-r4 Lemma 2 (line 229) | **states** \(Z''_i=Z\cap(\Omega_i^{\sim5})^c\) for \(h<i\le k_0\), one M-layer above \(k_0\), and (19) | **No.** The hybrid breaks this hypothesis for \(i\ge h+2\). Its conclusion (gaps \(\ge LM\)) is supplied by (H3). The lemma must be restated. |
| pda.md (L), (L1)-(L2), (U3) | the CA lower nest for \(h<i<s\) and its junction gaps | **No.** (L) holds only at \(i=h+1\). Its gap proofs must be redone with (H3). |
| fco-slot §§3-4 | three nest facts, closed-endpoint class | Nest facts yes. Class no (finding 16). |
| geoh-live-ab | first member, gaps, collar | Yes (finding 15). |

## Repairs

1. Line 17 or 227: credit geo-3 (2.4)-(2.6) as the earlier \(R_a\to R\) conversion fed into geo-2 (6.1).
2. After line 322: add the inclusion \(\Lambda\subset O_{k_0+1}\) (finding 13). State that \(\Lambda=D_k^{[u_k]}\) is part of the hybrid specification.
3. Lines 403-407 and row 542: say that fco-slot assumes the closed endpoint. Its transfer to the open-endpoint hybrid is not supplied here. Note that Y 75863-75865 now holds for the first member.
4. Lines 523-526: list the open consumer restatements: st1-r4 Lemma 2, pda.md (L), ti-2 (N)/(N2) text for the new first member, and fco-slot's class endpoint. Then FM-MATCH.
