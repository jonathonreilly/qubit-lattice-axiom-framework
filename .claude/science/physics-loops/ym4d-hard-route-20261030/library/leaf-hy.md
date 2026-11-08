## Repo search

The lead's [search record](prior/repo-search-2026-11-08.md), §§5–7, searched main and PRs #10114, #10133, #10134 and #10141.
It found no outside-lane supplier for this hybrid.
That is a search result, not an absence theorem.
I fetched main and PR #10141 without changing this checkout.
Main was `43a1fcc374711ca50626eca667441d3ca575c7d1`.
PR #10141 was `c73ad7b177d94f89ff37b77386936e3d52b48b05`.

| Hit checked | Closeness and use |
|---|---|
| PR #10141, `research/ym4d/library/st1-r4.md:1697–1710` | Its Amendment GS records the separate outer GEO-slot mismatch. It requires SLOT-ST and, for CA identification, SLOT-CA/FM-match. It supplies no hybrid selector. |
| [geoh-o1](geoh-o1.md), with [Claude's check](../gates/geoh-o1-check.md) | The all-thin mismatch is already proved. The check proposes this hybrid but leaves its radius conversion open. Neither counterexample is repeated here. |
| [geoh-live-ab](geoh-live-ab.md), §§3–6 | Supplies the checked finite-history invariant. This note matches its geometric premises, including its open endpoint. |
| [fco-slot](fco-slot.md), §2 | Its nest transfer reads only \(D_h=G_h\), nesting (N1), and containment (N3). We use that reduction, without repeating its owner or code proofs. |
| [geo-2](geo-2.md), §6; [ti-2](ti-2.md), §2 | Supply the shell-count argument and the thin face rule. Only the first-member constant changes. |
| [geoh](geoh.md), Definition 1 and Lemma 1, lines 9–17 and 61–74 | **The window ratio is already proved.** Its bound is \(R_{k-N_k}\le K_RR_k\). [Claude's check](../gates/geoh-gate.md), line 25, verifies it. This supplies HY-UNITS' scale input; we do not prove it again. |

`prior/leaf-hy.md` is absent at the task pin.
The registry keeps FM-MATCH, GEOH-O3 and FCO-read separate.
FINISH row 545 assigns this finite hybrid match; it does not transfer those other targets.
The targeted `open-core`, `l17c`, registry and FINISH search found no separate HY-UNITS/HY-READS assignment.

# HY-UNITS and HY-READS

Codex, 2026-11-08. Source pin `b0be684f1131d66016b38103591ea5dc5de80cc9`.
The shared checkout advanced externally to `2faf203b2a37bc739eaac1a0ebdb7182a79ae220` during writing.
The cited local proof inputs were compared with the pin and remain unchanged.
Research text, not an audit. This text grants no status.
All mathematical checks below are written arguments. No run supplies a proof step.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the large-field method and preparation geometry.
The source keys are:

- **SA:** [YM4_sketch_500.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), revision `31a47c543775`.
- **I:** [complete account, Part I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), the same revision.
- **Y:** [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), revision `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.

The outline index was searched before reading bounded source excerpts.
The relevant entries are chunk 16, its obligations, and CA 4.12–4.19 chunks 03 and 09.
Their source status remains attached: the class and updates are definitions; quiet-box geometry is a conditional proof.
The complete CA lower nest is not the hybrid defined here.

This note concerns the proposed operation in [hstep-tree](hstep-tree.md), §9.
Its quiet, single-box window is retained, with CA's open quarantine endpoint.
Its stage coordinate masks and whole-component outcomes are retained as specified rules.
Analytic admission and equality of measures are outside this finite geometric implication.

## 1. Kill tests, before the proof

Write \(u_{i+1}=Lu_i\) for native \(M\)-cube sides and \(a_i=R_i u_i\) for boxing-cell sides.
All distances below use the sup norm in an admissible lift.
Distance with subscript \(i\) means physical distance divided by \(u_i\).

### HY-UNITS: the proposed constant fails

Allow \(R_{h+1}=LR_k\), as the test requests.
Even when the core equals its first hull, the two-sided addition is
\[
 6a_{h+1}=6L^2R_ku_h>8LR_ku_h.
 \tag{K1}
\]
Thus \(B+8L\) is not justified in the consumer's radius convention.
SA 17334 excludes consecutive drops, not this single drop.

The full quiet-window geometry does not exclude it either.
Here is a geometric record, using the existing single-creation construction of [geo-prop23](geo-prop23.md), §3.
Only its scale sequence changes.
Fix the allowed odd \(L\ge27\), exponent \(r\ge2\), and an allowed positive frame slope \(b\).
Choose a sufficiently large power \(R=L^p\), put \(k=R+1\), and set
\[
 T=\exp(R^{1/r}),\qquad x_i=T+b(3-i),\qquad 0\le i\le k.
 \tag{K2}
\]
Choose \(p\) so that
\[
 T-b(R-2)>\exp((R/L)^{1/r}),\qquad
 T+3b<\exp((LR)^{1/r}).
\]
Also impose the existing coupling and preparation floors.
Such a choice exists: exponential growth dominates the displayed polynomial losses.
For example, \(e^t\ge t^q/q!\) for any integer \(q>r\) proves the required domination.
The sequence decreases, and \(x_i-x_j=b(j-i)\), so it meets the frame inequalities when \(b\) is an allowed slope.
The literal rounded radii are
\[
 R_0=R_1=R_2=LR,\qquad R_3=\cdots=R_k=R,
 \qquad N_k=R,
 \qquad h=1.
 \tag{K3}
\]
These are radii of the same sequence, not radii inferred from a tube around it.

At level 1 use the cited single-cell failure: \(C=E_1^{[6a_1]}\), of side \(13a_1\).
Here \(E_i\) denotes the centred boxing cell.
Give later steps no failures, joining, or other component.
The source's eight- and ten-layer rules give \(G_2=E_2^{[10a_2]}\), of side \(21a_2\).
At the drop, \(a_3=a_2\), so \(H_3=G_2\) and \(G_3\) has side \(41a_3\).
The next hull has at most three cells per side, since \(41/L<3\).
Thus \(G_4\) has at most 23 cells per side; subsequent boxes have 21.
All traces are single boxes below the cutoff 100.
There is no earlier attempt: for \(i<k\), \(i\le R\le N_i\).
A sufficiently large torus contains all these boxes and their margins.
Hence this record meets depth, size, quietness and either quarantine convention.

Its first hybrid member is \(D_2=E_2^{[3a_2]}\), of side \(7L^2Ru_1\).
The initial bound is exact with \(B=13L\), but
\[
 7L^2Ru_1>(13L+8L)Ru_1.
 \tag{K4}
\]
This realizes the failed constant conversion on the geometric class.
It asserts no positive Wilson weight or analytic realization of the record.
It does not refute the hybrid with a larger fixed constant.

### HY-READS: both specified tests pass with both counts retained

Put a live pocket \((Y,m)\) at the open endpoint \(m=h\), against a face of \(C\).
Its fixed strip extends by \(q_hu_h\), where \(q_h=(R_h-1)/2\).
The first hybrid member has at least \(3a_{h+1}\) beyond \(C\).
The already proved adjacent comparison gives \(R_h\le LR_{h+1}\).
Therefore
\[
 \begin{aligned}
 \operatorname{dist}_{h+1}(Y^\sharp,D_{h+1}^c)
 &\ge3R_{h+1}-q_h/L
 \ge\tfrac52R_{h+1}+\tfrac1{2L},\\
 \operatorname{dist}_{h}(Y^\sharp,D_{h+1}^c)
 &\ge3LR_{h+1}-q_h
 \ge\tfrac52R_h+\tfrac12.
 \end{aligned}
 \tag{K5}
\]
This is the endpoint calculation in geoh-live-ab (9), applied to the same first member.
Its sources are I 63524–63535, 63643–63649 and 63908–63915, due to Sussman and Alpoge.
An ordinary stop after stage 1 retains \(\Omega_{h+1}\cap X=X\setminus D_{h+1}\).
The strip and its birth collar remain protected.

For the second test take \(n=1\), \(n^+=2\).
The second stage changes coordinates but performs no second fluctuation integral.
Its frozen geometry includes \(D_{h+2}\), its band and its level-\((h+2)\) datum.
The completed integral list still has length one.
These are the separate records in I 64420–64442 and 64796–64850.
The thin rule places \(D_{h+1}\) at least \(u_{h+2}\) inside \(D_{h+2}\).
It therefore preserves (K5) and the second-stage bond separation.
A record containing only \(n=1\) would omit the second raised member and **fail** this test.
Section 4 retains both counts in all geometric and integral reads.

## 2. HY-UNITS: use the existing window lemma

Fix one operation at level \(k\), and put \(h=k-N_k\).
Use the literal scale sequence of that operation.
For SA this is \(x_i\), with the upper flow bound in SA 7511–7518.
For GEOH's frame-defined geometry it is \(\theta_i\), with Definition 1's bound.
Let \(B_{\rm flow}\) be the corresponding fixed upper decrement constant.
An arbitrary point of IN1's tube cannot replace either sequence.

GEOH Lemma 1 already proves, under its stated floors,
\[
 N_k=R_k,\qquad
 R_h\le K_RR_k,\qquad
 K_R=L2^{r-1}(1+r^rB_{\rm flow}).
 \tag{U1}
\]
Its proof uses the running minimum and the upper decrement bound.
Its conclusion does not use closed-endpoint quarantine.
Monotonicity therefore gives the required history-uniform conversion immediately:
\[
 1\le R_{h+1}/R_k\le R_h/R_k\le K_R.
 \tag{U2}
\]
This is an application of the checked repo lemma, not a new scale theorem.

Let \(C=G_h=X\cap Z_h\).
Sussman and Alpoge's quiet-box calculation gives
\[
 G_{i-1}\subset H_i\subset G_{i-1}^{[a_i]},\qquad
 O_i=H_i^{[8a_i]},\qquad G_i=H_i^{[10a_i]},
 \quad h<i\le k.
 \tag{U3}
\]
Here \(O_i=X\cap\Omega_i^{\circ c}\), and the circle denotes the pre-operation label.
These are Y 63757–63771, obtained from the restriction argument at Y 63694–63756.
For the open endpoint, geoh-live-ab §3 already supplies the surviving-buffer argument.
Only levels strictly above \(h\) are traced.
An operation at \(h\) is included in their input and is permitted.

The hybrid is
\[
 D_h=C,\qquad D_{h+1}=H_{h+1}^{[3a_{h+1}]},
 \qquad
 D_i=\operatorname{box}_{F_i}\bigl(D_{i-1}^{[u_i]}\bigr)
 \quad(h+2\le i\le k),
 \tag{U4}
\]
where \(F_i=u_i(\mathbb Z+\tfrac12)\) is the face grid.
The first formula ports Y 63785–63812 and I 53776–53785.
The later formula is ti-2 (N).
Each first face moves less than \(4a_{h+1}\).
Each later face moves in \([u_i,2u_i)\).

Suppose first that \(\operatorname{side}C\le BR_ku_h\), coordinate by coordinate.
The resulting sufficient constant is
\[
 \widehat B=B+8LK_R.
 \tag{U5}
\]
Indeed, adding the opposite face increments gives, for \(i\ge h+1\),
\[
 \begin{aligned}
 \operatorname{side}D_i
 &\le BR_ku_h+8LR_{h+1}u_h
                  +4\sum_{j=h+2}^i u_j\\
 &\le\widehat B R_ku_h+\frac{4L}{L-1}u_i.
 \end{aligned}
 \tag{U6}
\]
An empty sum is zero.
If the literal starting bound is \(B_0R_hu_h\), use instead
\[
 B=B_0K_R,\qquad \widehat B=K_R(B_0+8L).
 \tag{U7}
\]
The source's small-box convention permits \(B_0=100\).
This states explicitly which radius pays for the initial core.

Apply the counting argument already proved in geo-2 §6, with later increment constant \(K=2\).
Equations (U5)–(U7) replace its initial-side constant.
In its exact \(R=R_k\) convention, sufficient constants are
\[
 C_{\rm side}=\max\{\widehat B,4/(L-1)\},\qquad
 C_{\rm tops}=\max\{\widehat B,4L/(L-1)+1\}.
 \tag{U8}
\]
Thus every used nest box satisfies
\[
 \operatorname{side}D_i
 \le C_{\rm side}(R_kL^{h-i}+L)u_i.
 \tag{U9}
\]
For completeness, the shell substitution uses \(D_{j+1}\) for a level-\(j\) shell.
Its lattice spacing is \(\xi_j=u_j/M\).
Equation (U6) bounds its coordinate length in sites by
\[
 M\{\widehat B R_kL^{h-j}+4L^2/(L-1)\}.
\]
The endpoint allowance is one site per coordinate.
Consequently the existing shell-top count becomes
\[
 \#\{\text{level-}j\text{ shell tops}\}
 \le\bigl[C_{\rm tops}M(R_kL^{h-j}+L)\bigr]^4,
 \qquad h\le j<k.
 \tag{U10}
\]
The same bound holds for \(j=k\) in the hybrid main box \(\Lambda=D_k^{[u_k]}\).
Its coordinate bound before rounding is
\(M\{\widehat B R_kL^{h-k}+4L/(L-1)+2\}+1\).
It is below the right-hand coordinate bound in (U10), since \(M\ge1\) and \(L\ge27\).
This is precisely geo-2's count, with the first jump accounted for.

All these constants precede the running radius and coupling ceiling.
Choose the latter so that the existing scale floors hold and
\[
 \widehat B R_kL^{-R_k}\le1.
 \tag{U11}
\]
This is a permissible uniform floor.
For positive integers \(s\), the ratio of consecutive \(sL^{-s}\) is at most \(2/L<1\).
Hence a fixed threshold suffices for every later allowed radius.
Then \(\operatorname{side}\Lambda<8u_k\); in particular the main box has fixed native size.
The source's order of constants is preserved.

**HY-UNITS closes.** Its scale bound was already in GEOH.
Its new content is the hybrid substitution (U5)–(U10).
The next leaf is HY-READS, treated below.

## 3. HY-READS: geometry of this sequence

### Grids, containment and gaps

The first member's faces lie on \(a_{h+1}(\mathbb Z+\tfrac12)\).
Since \(R_{h+1}\) is odd, this grid is contained in \(F_{h+1}\).
Thus the later thin recursion starts on its required grid.
This ports the grid argument in Y 63806–63812.
Odd \(L\) also gives \(F_i\subset F_{i-1}\).
Every later increment is a multiple of \(u_{i-1}\), as required by ti-2 (N2).

The first member lies inside \(O_{h+1}\) by (U3).
For each subsequent level, assume \(D_{i-1}\subset G_{i-1}\).
The thin face rule gives
\[
 D_i\subset D_{i-1}^{[2u_i]}
 \subset H_i^{[2u_i]}
 \subset H_i^{[8a_i]}=O_i\subset G_i.
 \tag{H1}
\]
Induction proves the whole chain
\[
 D_i\subset O_i\subset G_i\subset H_{i+1}
 \quad(h<i<k),\qquad D_k\subset O_k\subset G_k=X.
 \tag{H2}
\]
The level-\(h\) premise is \(D_h=G_h=C\).
The (N3) assertion starts at \(h+1\), exactly as in ti-2.
In particular, an endpoint-born island need not satisfy \(C\subset O_h\).

The gap estimates are
\[
 \operatorname{dist}(D_h,D_{h+1}^c)\ge3a_{h+1},\qquad
 \operatorname{dist}(D_{i-1},D_i^c)\ge u_i
 \quad(h+2\le i\le k).
 \tag{H3}
\]
They include the first splice and every later splice.
After division by the preceding lattice spacing \(u_{i-1}/M\), each gap is at least \(LM\).
This is the gap read by ti-2's consumer table and geoh-live-ab (5).
There is no uniform \(K=2\) upper face bound at the first move.
Its replacement is (U6), already sufficient for the shell readers.

For the main box, \(\Lambda=D_k^{[u_k]}\) has the native grid and stays inside \(X\).
Indeed, \(k\ge h+2\), and (H1) gives \(\Lambda\subset H_k^{[3u_k]}\subset G_k\).
It contains \(D_k\), as required by geoh-live-ab §6.
This is the hybrid's main box, defined by one added native layer.
No identity with CA's later thick boxes or its erosion formula for the main box is used.

### Covariance, including the first hull

Hull, metric enlargement and the unique smallest face-grid box commute with lattice isometries when their grids are carried.
Induction in (U4) therefore gives \(D_i(gC)=gD_i(C)\), with the pre-operation data carried too.
This uses Sussman–Alpoge's hull construction and the uniqueness argument checked in ti-2 §1.

For fixed grids, also check the first boxing grid.
An isometry preserving every \(F_i\), through \(F_k\), has translation in \(u_k\mathbb Z^4\).
Equations (U2) and (U11) give
\[
 \frac{a_{h+1}}{u_k}
 =R_{h+1}L^{1-N_k}
 \le K_RR_kL^{1-R_k}
 \le\frac{LK_R}{\widehat B}\le\frac18.
\]
Both sides' grid lengths are powers of \(L\) times the same base length.
Hence \(a_{h+1}\) divides \(u_k\).
These translations, and signed coordinate permutations, preserve the first centred boxing grid.
Thus the hybrid has ti-2's actual fixed-grid (N4), as well as covariance with carried grids.
This does not assert covariance under arbitrary continuous rotations.

### What the live-A/B proof reads

Use the notation of geoh-live-ab: \(S_Y=Y^\sharp\), born at level \(m\).
The open quarantine rule gives \(m\le h\) for a treated old pocket.
Its retained set satisfies \(Y\subset C\), by the existing retention argument in that note, §5.
Its strip reaches only \(q_mu_m\) beyond \(Y\).
The ported radius comparison I 63643–63649 gives
\[
 q_mu_m\le\tfrac12R_{h+1}u_{h+1}.
\]
Consequently
\[
 \operatorname{dist}_{h+1}(S_Y,D_{h+1}^c)
 \ge\tfrac52R_{h+1}.
 \tag{H4}
\]
This is Sussman and Alpoge's treated-collar argument, I 63908–63915.
Every later member contains \(D_{h+1}\).
Thus (H4) applies to every preparatory collar \(G_i\setminus D_i\), including an unintegrated raised band.

The exact geometric uses in the existing invariant proof are these:

| Induction step in geoh-live-ab | Members and premises read | Hybrid supply |
|---|---|---|
| §3, (6)–(8): first protected member | \(C=G_h\), its hull, and \(N_3H_{h+1}\subset D_{h+1}\) | Equality in (U4). No later thick member is read. |
| §4, endpoint cycle; §5, birth-collar induction | \(D_{h+1}\) when \(m=h\); unchanged \(\Omega_{m+1}\) when \(m<h\); retained later members | (K5), nesting, and the prefix records in §4 below. |
| §5, retention of \(Y\) | Levels at most \(h\) stay fixed during preparation; whole-component outcomes; \(m\le h\) | The hybrid keeps these rules. |
| §5, cell saturation, level ceiling and disjointness | The birth collar, nested native grids, fixed birth strip, and whole-component deletion | The preceding rows supply the only changed premise, the birth collar. |
| §5, T-site and untreated-component bounds | Original T buffers and separation of distinct top components | Original regions are unchanged; (H2) keeps every new site inside its own component. |
| §5, treated P bound | \(D_{h+1}\) and inclusion in every later \(D_i\) | (H3)–(H4). |
| §6, first-stage bonds | Distance from \(S_Y\) to \(D_{h+1}^c\) exceeds \(u_h\) | (H4), since \(R_{h+1}\ge1\) and \(L\ge27\). |
| §6, later-stage bonds | \(S_Y\subset D_j\) and gap to \(D_{j+1}^c\) at least \(u_{j+1}\) | Nesting and (H3). |
| §6, main integration and late exits | \(D_k\subset\Lambda\subset X\); retained prepared label; original lifetime rule | The main-box construction and §4 below. |

This list isolates the lower members actually read.
The repeated lower thick formula is used in geoh-live-ab §3 only to establish later gaps.
Equation (H3) supplies those gaps directly for the hybrid.
The invariant's other steps use the first thick member, nesting, or unchanged operation rules.

For clarity, the bond argument uses the actual two coordinate masks.
At stage \(j-h+1\), these are
\[
 (O_{j+1}\setminus D_{j+1})^{(j)*},
 \qquad G_{j+1}\setminus O_{j+1}.
 \tag{H5}
\]
These are I 74309–74320, restricted to \(X\).
Both masks are outside \(D_{j+1}\).
Under the larger incident-bond convention, a bond can extend one level-\(j\) spacing beyond its mask.
That spacing is \(u_j/M\le u_j\), by I 159058–159075.
At the first stage (H4) exceeds this length.
At each later stage (H3) gives \(u_{j+1}=Lu_j>u_j\).
Hence no preparatory integration bond reaches a live strip.
An exceptional coordinate change uses the same separated masks.
Main integration remains a distinct site, as in the existing invariant.

Finally, (H2) and (H3) give exactly the three nest inputs isolated in fco-slot §2:
\(D_h=G_h\), (N1), and (N3).
Its nest substitution therefore applies with the same slot constants.
This does not change that theorem's remaining class, chart or coordinate assumptions.
In particular, its full-read supplier FCO-read remains separate.

## 4. Every stopped prefix and the extra raised level

Write \(\Omega_i^\circ\) for the pre-operation domains.
For an ordinary completed prefix of length \(s\), the surviving entries inside \(X\) are
\[
 \Omega_i^{[s]}\cap X=
 \begin{cases}
  \Omega_i^\circ\cap X,&i\le h,\\
  X\setminus D_i,&h<i\le h+s,\\
  \Omega_i^\circ\cap X,&h+s<i\le k.
 \end{cases}
 \tag{P1}
\]
This ports the update in SA 17415–17440 and I 53806–53814.
The corresponding \(\Lambda_i\) replacements have the same range, except that \(\Lambda_k\cap X\) stays empty on a drop-out.
Thus the stopped component remains in the top large-field region.
The original entries also remain recorded as the action presentation.

For \(s=0\), (P1) is the original nested label.
For \(1\le s\le N_k\), check its two splices and its interior.
At its bottom, \(G_h=D_h\subset D_{h+1}\).
Within the prefix, use (H3).
At its top, \(D_{h+s}\subset O_{h+s}\subset G_{h+s}\subset O_{h+s+1}\), when the next level exists.
The last inclusion follows from (U3), since the next hull contains \(G_{h+s}\).
Outside \(X\) all entries stay fixed.
These are exactly the splices needed for the alternating \(\Omega,\Lambda\) nesting.
This also checks a stop immediately after the first stage.

Now retain two integers, as the source requires:
\[
 n=\text{number of completed fluctuation integrals},\qquad
 p=n^+=\text{number of raised levels}.
 \tag{P2}
\]
For ordinary exits, \(p=n\).
For the exceptional sharp-collar exit, \(p=n+1\le N_k\).
The frozen record includes every raised member \(D_{h+1},\ldots,D_{h+p}\), its bands, and its native data.
The list of completed chain terms has indices only \(1,\ldots,n\).
These are the distinctions in I 64420–64442 and 64796–64850.

There is a useful presentation distinction at this exit.
Y 75934–75959 allows the determining list to remain the one before the incomplete stage.
It retains the collar nonpivots and the exact translated density, including eliminated-pivot factors.
It has no integrated normalizer for that stage.
Use that presentation here: the surviving completed-stage \(\Omega\)-list is (P1) with \(s=n\).
Keep the raised geometry through \(p\) as a separate, mandatory part of the same record.
A read of raised cells, bands or their top datum uses \(p\), not the length of the integral list.
No equality between these two records is inferred.

The geometric prefix with \(s=p\) also satisfies (P1)'s nesting calculation.
Thus a presentation reading that raised prefix has the same collar protection.
This verifies the invariant's local premises for either permitted presentation.
It does not identify their analytic functions by changing notation.
The actual stored-density and coordinate identification stays with FM-MATCH.

Here is the requested exceptional test with its complete indices:

| Read at the \(n=1,p=2\) exit | Retained object |
|---|---|
| Completed-stage \(\Omega\)-list | \(\Omega^{[1]}\); in particular \(\Omega_{h+1}\cap X=X\setminus D_{h+1}\). Higher entries keep their original values in this presentation. |
| Raised geometry | Both \(D_{h+1}\) and \(D_{h+2}\), with the second band in \(G_{h+2}\setminus D_{h+2}\). |
| Extra stage coordinates | The level-\((h+2)\) datum and the retained level-\((h+1)\) collar nonpivots and translated density. |
| Completed integral or chain-term list | Stage 1 only. Stage 2 has no performed fluctuation integral or integrated normalizer. |
| Later raised-level read | Top level \(h+2\). Its datum and band persist until the attempt is consumed. |

The second member is strictly larger: (H3) gives a positive gap around \(D_{h+1}\).
The extra datum therefore cannot be dropped by declaring the completed depth to be the full record.
This explains precisely the failure of the \(n\)-only version of the kill test.

### The invariant survives every exit

If \(m=h\), (K5) puts the entire birth collar
\[
 B_Y=\{x:\operatorname{dist}_m(x,S_Y)<5R_m/2\}
\]
inside \(D_{h+1}\).
For \(s=0\), it lies inside the wider original \(O_{h+1}\).
For every \(s\ge1\), (P1) keeps it outside \(\Omega_{h+1}^{[s]}\).
All additional raised bands lie outside \(D_{h+1}\), so none raises a cell of that birth collar.
This includes \(n=0,p=1\), as well as the requested \(n=1,p=2\).
If \(m<h\), the operation leaves \(\Omega_{m+1}\) unchanged.
Nesting keeps the previously protected collar inside the first core and hence outside every new raised band.

Every ordinary pre-localisation interruption keeps these same prefixes and the standing mark.
The next T step leaves earlier entries fixed and supplies its original eight-layer buffer.
The new standing mark prevents an immediate attempt on this lineage.
At any later permitted attempt, the open endpoint gives a bottom index at least the marked level.
The existing induction in geoh-live-ab §§4–5 therefore applies without a second collar loss.
Its proof of that timing already covers the open endpoint.

Late exits retain the full prepared prefix and their actual main-step variables.
The main box stays inside \(X\), so foreign-component estimates stay unchanged.
A completed localisation removes the old pockets before inserting any new second-class pocket.
These are the existing lifetime and outcome rules, I 63524–63545 and SA 17415–17430.
They need no additional lower member.

Start with no live pockets and order the finite history by moves and stages.
The reader table in §3 supplies every changed premise of geoh-live-ab's induction.
Equations (P1)–(P2) cover all stopped stages, including the unintegrated extra raise.
Every other move has the same geometric rule as that induction.
Induction therefore transfers its assertions 1–7 to this hybrid, with their original constants.
In particular, live strips remain disjoint and retain their birth collar and native-cell level ceiling.
The treated P bound stays \(5R_{h+1}/2\), and no P integration bond meets a live strip.
This proves **HY-READS** for every finite history of the specified hybrid rules. \(\square\)

## 5. Result and handoff

**Stopping condition (a): both finite geometric leaves are proved from the stated rules and existing scale inputs.**
The supplied pieces are (U5)–(U10), (H1)–(H5), and the two-count prefix record (P1)–(P2).
They fill the geometric part of hstep-tree §9's hybrid preparation supplier.
The proposed constant \(B+8L\) fails; the hybrid itself passes with \(\widehat B\).
The window-ratio proof belongs to the earlier GEOH note and its Claude check.
The live invariant belongs to geoh-live-ab; this note supplies its consumer match.

HY-READS is the leaf after HY-UNITS, and is completed here.
Section 9 names no further hybrid leaf.
The next supplier boundary is the already owned analytic realization/FM-MATCH, not another scale or collar proof.
GEOH-O3 and FCO-read retain their existing owners and scope.

Written and author-checked by Codex. Not yet checked by another model.
Only this file was written. No audit, registry or scientific status was changed.

| Item | Status in this text | Exact supply or limit |
|---|---|---|
| Original \(B+8L\) conversion | Refuted on the geometric class | (K1)–(K4); no analytic-weight claim. |
| Full-window radius comparison | Existing checked repo result, reused | GEOH Lemma 1; (U1)–(U2). |
| Initial \(R_h\) versus consumer \(R_k\) | Matched | (U5) or (U7), according to the initial convention. |
| Shell side and site counts | Proved for this hybrid | (U6)–(U10), using geo-2 §6. |
| Grid, nesting, gap and containment | Proved for this hybrid | (H1)–(H3); (N3) ranges over \(h<i\le k\). |
| Covariance | Proved for the required lattice isometries | §3, including the first boxing grid. |
| Open-endpoint pocket and first stop | Kill test passed; invariant premise supplied | (K5), (P1). |
| Treated P collar and integration bonds | Original bounds preserved | (H4)–(H5), with the geoh-live-ab proof reused. |
| Exceptional \(n=1,n^+=2\) exit | Kill test passed with both records | §4; the \(n\)-only record fails. |
| FCO-slot's nest inputs | Matched | \(D_h=G_h\), (N1), (N3); other hypotheses retained. |
| Whole CA selector, analytic admission and FM-MATCH | Not claimed | The hybrid is a specified new selector. |
| First open input within these two leaves | None | Outside them: the existing analytic operation/FM-MATCH identification. |
