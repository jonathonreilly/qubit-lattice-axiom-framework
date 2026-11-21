# Check: library/geoh-o1.md

Claude (Opus 5.5), 2026-11-08. One line-by-line check of one proof note (310 lines, Codex gpt-6-astra).
Clone at `e12686c94`; the note pins `f977f18f`. ti-2.md is unchanged between them.
Sources: CA-I `theorem_0_complete_account_raw_I.tex` (31a47c543775), SA `YM4_sketch_500.tex` (31a47c543775), N `YM4_1400.tex` (2bc0658f).
This is one reading by one other model. It is not an audit. Every step was redone by hand. No numerics.

## Verdict: ADVANCE

Outcome (b) holds. The mismatch is real. (3)-(5) and (7)-(11) are correct.
Two precisions below (findings 9, 10) sharpen section 5. Neither changes a stated result.
Recommendation: neither pure option. Use the CA/N first prepared member and keep ti-2's thin rule above it (section R).

## Findings

| # | Note line | Source line | Claim | Result |
|---|---|---|---|---|
| 1 | 137-142 | ti-2.md 43-50 (pinned and current) | ti-2 (N): "\(D_a:=C\) and, for \(a<i\le k\) ... \(\alpha_i:=\max\{u\in F_i:u\le\alpha_{i-1}-m_i\}\), \(\beta_i:=\min\{u\in F_i:u\ge\beta_{i-1}+m_i\}\), \(F_i=m_i(\mathbb Z+\tfrac12)\)". Here \(m_i=ML^{i-k}\) is the level-i M-cube side (geo-3.md 10), \(a=k-N_k\), \(C=X\cap Z_a\) (geo-3.md 18, geo-2.md 13). The note's restatement with \(u_i\) is exact. Its cite "39-52" contains the rule (43-50). | CONFIRMED |
| 2 | 144-154 | N 63773-63812; I 53776-53785; I 63706-63712 | CA-I: \(Z''_i=(\Omega_i^{\sim5})^c\cap Z\) for \(h<i\le k_0\), with \(\Omega^{\sim n}\) made of \(a_i\)-cubes. N's erosion gives \(Z''_i=H_i^{[3a_i]}\). N states \(h<k_0\), so \(i=h+1\) is in the lower range. | CONFIRMED |
| 3 | 159 (3) | ti-2 (N2) | \(\beta_{h+1}\) is the least point of a grid of spacing \(u\) at or above \(c^++u\). So it is below \(c^++2u\). Strict. | CONFIRMED |
| 4 | 162-172 (4) | N 63757-63771 | \(H_{h+1}\supset G_h=C\), so the CA face is at least \(c^++3R_{h+1}u\). The test point \(c^++2u\) is outside the thin box and inside the CA box. The CA box lies in \(O_{h+1}\subset X\). The difference is interior. | CONFIRMED |
| 5 | 174-184 (5) | SA 17421-17426; I 53806-53814 | SA's drop-out rule is \(\Omega_l\cap X=X\setminus Z''_l(X)\), \(t_\flat<l\le t_\flat+n\). The completed first stage therefore writes different \(\Omega_{h+1}\) labels. An interruption keeps them. | CONFIRMED |
| 6 | 193-201 | geoh-live-ab.md 172, 217, 242, 421, 445 | (6) feeds (8), (9), assertion 7 and (15). The thin rule gives one native layer \(u_{h+1}\), not \(3a_{h+1}\). So (6) fails for the thin rule. | CONFIRMED |
| 7 | 208-231 (7)-(8) | N 63684, 63757-63771; I 63524-63535 | The island \(Y=E_m^{[10a_m]}\) has side \(21a_m<100a_m\). \(21<L\) puts each next hull in the centred cell. N's closed window \([k'-R,k')\) bars attempts for \(k'\le m+R\). At \(k=m+R+1\), \(h=m+1>m\). The class conditions hold, so compulsory admission selects \(X\). The pocket is live. | CONFIRMED |
| 8 | 233-265 (9)-(11) | I 63528-63531; I 53806-53814; CA-I 85635 (clause (h)) | \(21R/L\) is odd, so the faces of \(C\) lie on \(F_{h+1}\) and the thin rule adds exactly \(u_{h+1}\). The strip half-side is \((21R+R-1)u_m/2=(11R-\tfrac12)u_m\). \(u_{h+1}=L^2u_m\). The distance is the half-side difference. \(21R/(2L)+1\le 7R/18+1\le 8R/9\) for \(L\ge27\), \(R\ge2\). CA clause (h) asks \(\ge\tfrac52\check R_{h+1}\). | CONFIRMED |
| 9 | 285 | geoh-live-ab.md 223-262 | "Closing the lower endpoint does not remove the obstruction." True for the constant \(5R/2\). Precision: the closed endpoint is necessary for the thin rule. With CA's open endpoint and \(m=h\), \(C\) may equal the island. The strip reaches \(q_hu_h\approx(R_h/2)u_h\) beyond \(C\). The thin margin is \(Lu_h\). So the strip enters the first collar once \(R_h>2L+1\), and geoh-live-ab §4 (the \(h=m\) cycle) fails outright. | CONFIRMED, sharpened |
| 10 | 287-290 | — | Section 5 names two options only. A third, smaller one exists (section R). | UNCLEAR (omission, not an error) |
| 11 | 282-284 | geoh-live-ab.md 147-160, 305-306 | geoh-live-ab says "We use that existing preparation; we do not replace its grid or selector" and its theorem reads "the printed T rule ... and prepared sequence specified above". It is a theorem on CA's stated rules. The note does not touch it. | CONFIRMED |

## Question 3: is the mismatch real?

Yes. ti-2 contains no step equal to the CA/N lower nest.
ti-2 (N) applies one-M-cube increments at every level. That is CA's upper-range rule (I 53778-53780), used also in the lower range.
geo-3.md §2 and geo-2.md §6 read (N) as the P nest. So our geometry uses the thin nest.
But st1-r4.md Lemma 2 (line 229) and pda.md (L) assume the CA lower nest \(Z\cap(\Omega_i^{\sim5})^c\).
So the construction is already split between the two nests. One side must change in any case.

## Question 4: which change is smaller

**Full switch to the CA/N nest.** It meets geoh-live-ab unchanged. But it breaks the K-readers of ti-2.
For \(h<l\le k_0\), \(\operatorname{side}(Z''_l)\ge6a_l=6R_lu_l\).
GEO3 (geo-2.md (2.1), SA 17598) asks \(\le C_n(RL^{a-l}+L)u_l\) with \(C_n\) fixed before R.
At \(l=a+j\), \(j\ge2\), this needs \(C_n\gtrsim6\min(L^{j},R/L)\). No constant fixed before R works.
So geo-2 §6 (6.1)-(6.2), geo-3 §2 (K = 2), geo-4, inn-213 §7, inn-fix and sa-2.8-terms Lemma W would all need new proofs.

**Keep the thin nest and prove its collar bound.** My one-line bound, closed endpoint (\(m<h\)):
\(Y\subset Z_{h-1}\cap C\), and tracing at \(i=h\) gives \(\operatorname{dist}_h(Y,C^c)\ge10R_h\).
The thin rule adds \(u_{h+1}\). The strip reach is at most \(R_h/(2L)\) in level-(h+1) units (I 63563-63569).
So \(\operatorname{dist}_{h+1}(S_Y,R_\nu)\ge\tfrac{19}{2L}R_h+1\). Example (11) shows this is sharp up to \(O(R/L^2)\).
This is below R for \(L\ge27\). It is not R, and not \(\tfrac52R_{h+1}\).
In level-m units it is \(\ge9.5R_m+L^2\). That meets the level-m birth collar of CA (c) and N 127519.
It does not meet CA (h), stated in level-(h+1) units. Every consumer of (h) would need rechecking. I did not find which consumers need the level-(h+1) form.
It also needs the closed endpoint (finding 9).

**Recommended: a hybrid nest.** Take the first member from CA/N: \(D_{h+1}=Z''_{h+1}=X\cap(\Omega_{h+1}^{\sim5})^c\) (\(=H_{h+1}^{[3a_{h+1}]}\) on quiet boxes). For \(i\ge h+2\) keep ti-2 (N) unchanged.
Reasons, each checked once by me only:
1. geoh-live-ab reads only \(D_{h+1}\) through (6), (8), (9), (15). It reads later members only through nesting and the one-cube gap (5). Thin increments give (5) by (N2).
2. The first member faces lie on \(a_{h+1}(\mathbb Z+\tfrac12)\subset F_{h+1}\) (\(R_{h+1}\) odd). So (N) starts correctly at \(i=h+2\), and (N1)-(N3) hold. \(Z''_{h+1}\subset O_{h+1}=H_{h+1}^{[8a]}\).
3. The first face move is below \(4a_{h+1}\le4LR_hu_h\). It enters geo-2 (6.1) as part of the initial side: \(B'=B+8L\), still fixed before R.
4. The first member is defined by hull and metric erosion on centred grids. It is isometry covariant, so (N4) and ti-2's purpose survive.
5. It keeps CA (h) at \(\tfrac52R_{h+1}\) and works with CA's open endpoint, so geoh-live-ab §4 stands.

Readers and branches to match under the hybrid:
- geo-2.md §6 and geo-3.md §2: start the K-bound at \(D_{h+1}\), with \(B'\); confirm geo-2's R versus \(R_a\) convention.
- inn-213.md §7 and inn-fix.md: nest box \(N_c\) through geo-2 §6, constant change only.
- sa-2.8-terms.md GEO3 and Lemma W: \(C_n\) changes by \(O(L)\).
- ti-2.md (N): state the new first member; recheck (N4) for it.
- st1-r4.md Lemma 2 and pda.md (L): their lower formula holds only at \(i=h+1\). Replace their lower gaps for \(i\ge h+2\) by the one-cube gap. st1-r4's conclusion uses only gaps \(\ge LM\).
- Interrupted branches: retained labels \(X\setminus D_l\), \(l\le h+n\), use the hybrid members. CA's (1.55) exit with \(n^+=n+1\) (I 64420-64442) stays a separate interface, as the note says.

The hybrid is a proposal. It is not proved here. Its first open step is the B' bookkeeping in geo-2 §6.

## Question 5

Confirmed (finding 11). geoh-live-ab proves its invariant on CA's printed rules. The note blocks only its use for an operation carrying ti-2's thin first member.
