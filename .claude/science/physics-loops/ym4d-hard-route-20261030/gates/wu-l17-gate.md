# Line-by-line check of `library/wu-l17.md`

Research-text check for FINISH row 380, before the owner's review. One reading by Codex (gpt-6-astra, xhigh); not an audit and no status is granted. The checked checkout is `f8287127f9168695f254504ca780e4d2adbe7c23`. All **WU** line numbers below refer to its 277-line `library/wu-l17.md`, SHA-256 `f98fa5b69d6a8f0b58c04dcc2588dcedf6f09f5ffafd178734a00d45460a49e5`. Its provenance records an earlier writing revision; that is not the revision used for this check.

**Disposition: REVISE.** The first defective displayed inference in the proof is the matrix-norm comparison at WU 103, repeated at 107. It has the local repair below. Lemma 1, the subsequent composition on I1–I7, the hereditary scaling, and the seed budget survive that repair. I found no BLOCK of the corrected conditional theorem. The prose is not ready unchanged: the consumer inventory has omissions and a false real-pair classification; the blanket cancellation of `c_T` is false; ER8 already has a conditional proof in the outline; and the constants and Result need the qualifications below. These are findings about this write-up, not a new proof of the original curvature-only (1.17).

**Scope and credit.** `library/prior/wu-l17-gate.md` did not exist. The registry separates original L17 (owner `l17`, open) from L17-CORR and ER7 (existing checked conditional results), and assigns the P20 F1 write-up to `wu-l17`. This check does not duplicate those proof lanes. I read `GOAL.md`, the requested FINISH instructions, the outline index and relevant neighbouring entries, `gates/l17c-gate.md` and `gates/p20-gate.md`; their already-checked constituent arguments remain named inputs. The a1 and flat-port gates were consulted for their stated repairs and scope, not re-proved. Tadeusz Balaban receives credit for the published machinery named in WU 12. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, receive credit for all material taken from the outline and complete account, especially the corrected budget, real-point argument, hereditary class and ER8 proof.

Sources are the four raw TeX files at Sussman–Alpoge commit `31a47c543775`. Each was fetched once. Source line references below use that revision, not rendered page numbers. Source reading was in bounded excerpts; the long consumer spans cited by WU were also opened in successive bounded ranges. Searches, line inventories and hashes were bookkeeping only. No computation discharges a mathematical step.

## 1. Quotations, references and source status

The two requested status checks are affirmative, with one line-range correction:

- **CA-III 111326–111327:** the inclusion sentence of CMP 109 (1.17), read at complex pairs, is in chapter 13's list of statements used without proof. Its status is exactly **“cited as printed at its use site”**. WU 32 cites only 111326, whereas the status words finish on 111327. The chapter title occurs at 111167.
- **CA-I 166588–166589:** the complex-pair inclusion sentence has status exactly **“printed without proof; cited as printed”**. Its placement among the published inputs of clause (0), under the heading identified at 166552–166563, is correct. Neither location records a proof of complex (1.17).

The following table records the remaining checks of the account and outline references. “Confirmed” means the source says what the write-up attributes to it, subject to the stated correction; it does not certify every theorem of the cited source.

| WU location | Source opened | Finding |
|---|---|---|
| 16–21, 205 | CA-I 32599–32623; 32666–32670 | The smaller primed radii, average bound, two bounds of (1.17), and distinction from CMP 116's larger operator radii are confirmed. **Quotation repair:** WU 21 capitalizes and turns an embedded paraphrase at 32613–32614 into a freestanding quotation. Remove its quotation marks and call it the account's report of Balaban's conclusion. The explicitly quoted original sentence is instead at 15928–15929. |
| 23–28, 63–67, 159–165 | CA-I 34058–34218 | The complex estimate is an explicit hypothesis at 34067–34072; the original budget is at 34061–34062. The bracketed replacements in WU's quotation correctly resolve the paper citation. The proof uses the scaled radii in Step 2 and treats the real factor separately. The proposition has a proof, conditional on that hypothesis; the lack of a special status sentence is not itself the evidence of proof. |
| 30, 208 | CA-I 34241–34403; 56419–56439 | Class reproduction (e), and the clause-zero paths through (g) and (c), are confirmed as dependency paths. Their other hypotheses remain. |
| 30, 189–195, 206–207 | CA-I 29522–29605; 32412–32500 | True-pair admission and the coupling-increment polydisc invoke (1.17) through the stated route. The small-exponential replacement is relevant. These references do not establish cancellation of all `c_T` dependence. |
| 30, 193, 209 | CA-II 4333–4398, especially 4381–4384 | The proof does infer (iv) from (i)–(iii) at the target radii. Lemma C is a valid replacement for this seed step under R2. |
| 34, 246–248, 268 | SA 9746–9753; 9899–9911; 6571–6630 | See the precise distinctions immediately below. ER8 is **proved conditional on ER7**, not merely sketched. |
| 48, 155, 187, 228, 254, 262 | CA-I 32724–32730; 32834–33070, including 32871–32879, 32896 and 32921–32929 | Tower rules, block-letter convention, axial-gauge object, collar estimate and its proof are confirmed. The collar inequality carries the standing floors on `L` and `R_1`; it is not an unconditional geometry assertion. The cube grids are nested. |
| 98, 167–175, 255 | CA-I 10306, 10333–10378, and the proof ending at 10502 | The matrix norm is normalized Hilbert–Schmidt, distinct from operator norm. The curl convention and current-remainder identity are confirmed. The remainder lemma is proved there; the specialization `U_0=1`, `c=0`, `ell=1` is legitimate. |
| 159, 254 | CA-I 33276–33335 | The restriction theorem is followed by a proof. WU uses the elementary change-of-unit identity at 33314–33321, which does not assume the hereditary membership being proved. No circular appeal to the conclusion of that theorem is needed. |
| 193, 224–238 | CA-I 1490–1527, 1528–1554, 1614–1629, 1667–1669, 2063–2064, 34811–34830 | Running radii are bounded by the absolute radii; Stage 7 chooses `alpha_1` before `alpha_0`; the Stage 5 ordering tension is real. Section 4 below gives the precise compatible choice. |
| 195, 210 | CA-I 29828–29865, 30028–30107, 32258–32288, 32405–32409, 32452–32491; CA-II 4599–4727, 94811–97192; CA-III 90585–90624 | Fixed constants and Cauchy radii change with `c_T`. The running-radius ratio cancels `c_T`; several other quantities do not. Repair in §3 below. |
| 208 | CA-I 34700–34743 | **Wrong locator:** 34714 is the layerwise-maximum warning, not the small-pairs supplier. Use **34718**, with **34738–34741** for the orbit-form inputs and suppliers. |
| 214 | CA-I 10750–10754, 36806–36905, 42198–42340, 43590–44380, 128551–128930, 155275–155438; CA-II 99767–99813 | The real estimates in most of these passages are real. However **155275–155438 is a complex minimizer argument with a real base**, and the multilevel frozen-background conclusion in 128551–128930 retains a separate assumption. See §3. The reblocking proposition at 44127–44129 is expressly incomplete at its marked step; listing a correct real component does not complete it. |
| 216, 266 | CA-I 45162–45234 | The minimizer-uniqueness and own-constant results carry **“Proof outstanding”** there. The precise status lines include 45163 and 45204; WU's references point to the respective starts. Their stated source status is correct. |
| 218 | CA-I 4384–4554, 5822–5908; 13198–13255, 17523–17564, 18305–18346; 10028–10092, 120111–120334; 15918–15961, 20150–20185, 34886–35045, 117207–117328, 121282–121350; 154551–154588, 154825–154863, 155490–155511 | These do not reveal another fresh application of complex (1.17). Several descriptions in WU are inaccurate: the B'-ball ceilings at 117207–117328 are not a rejected (1.17) route; 154825–154863 excludes the general complex assertion; 155490–155511 rejects a linear-datum route. Only the first of the last three ranges is aptly called a units definition. |
| 249, 252 | CA-I 24239–24290; 32603–32606 | Locality is attributed to CMP 98, and the real average bound is used as printed within the sufficient-condition discussion. Neither passage separately proves the depth-uniform perturbation estimate I1. WU correctly obtains that input from its named repository work. |
| 250 | CA-II 85835–85914; CA-III 35572–35624 | Minimizer analyticity is cited from CMP 102. The second-variation formulas are explicitly printed without proof, and the account says it does not perform that computation. WU's source-status distinction is correct. |
| 251, 262 | CA-I 35140–35218; 32896 | The minimal-orbit theorem is cited from CMP 102. The critical-orbit construction alone does not rebuild the minimality identification. Keep §9(2). |
| 253 | CA-II 54460–54550 | The local-decay proposition records the printed bounds from CMP 99b and related inputs. Calling these cited inputs is correct; the repository flat port is a separate, scoped construction. |
| 263 | SA 9625 | The outline distinguishes the default convention, with inward determining bonds omitted and outward rows included, from the kept-inward variant. Its Theorem 5 is in the default convention. WU correctly limits its proof to that convention. This does not decide competing historical readings of CMP 96. |
| 266–267 | CA-I 38108–38144; 54986–54998 | The exclusions concerning stage backgrounds/re-minimization are real, and the later theorem assumes Balaban's CMP 122a stage theorem. WU does not supply that theorem or T0. |

**What the outline actually supplies.** SA Theorem 5(a) states holomorphic existence and the two bounds with `K^sharp(alpha_0' + alpha_1'^2)`, the current factor `L^{2(n-p)}` in level-n units, and inclusion under that budget and `alpha_1' <= alpha_1`. It says `K^sharp` depends on `L` and `rho`; it also gives the one-power hereditary weight and the trivial triple. WU 34 represents this correctly, but a claim of independence from the separation constants must come from its own named uniform inputs, not from this citation alone.

Mechanism 8 explicitly gives the real-point Taylor inequality with unnamed constants, explains complex linearity of the first derivative, displays the covariant plaquette expansion, obtains the small covariant curl, and applies the real linear datum estimate to the three real points. It explains both the square and its scale factors. Thus neither the mechanism nor the corrected quadratic budget is new here. WU's explicit constant 6 and detailed composition implement that argument.

ER7 is expressly an **assumption** of a uniform holomorphic tower estimate, including both rules, all restricted domains, depths and changes of units. ER8 is a proposition under ER7 and sufficiently small target radii. Its proof starts at SA 6598 and ends at 6630. It includes the exponential-plaquette estimate, exactly the auxiliary-radius choice used in WU (5.3), the zero real factor, the budget, and hereditary inclusion. Replace “SA (ER8) ... sketched” at WU 248 by **“SA (ER8) is proved conditional on ER7; here it is implemented with explicit constants, the true-current specialization, and the account's consumer identifications.”**

## 2. Argument check: §§4–5

Here ADVANCE confirms the indicated inference on its stated inputs; it does not independently re-prove I1–I7. The earlier p20 and l17c gates cover the constituent results. The following is the check of their composition in this write-up.

| Step | Verdict | Check or required repair |
|---|---|---|
| Lemma 1, WU 85–94 | **ADVANCE** | Cauchy's homogeneous-term estimate sums to `2H (norm(x)/r)^2`; the displayed complex-linear identity is exact; three remainders give 6. No real maximum principle is being assumed. |
| Setting, WU 96 | **ADVANCE** | `eta_n=eta/s`, `w=sa`, gradient factor `s^2`, and `eta_n^2 s^2=eta^2` match the units of both conclusions. |
| Step 1, WU 98–115 | **REVISE** | The ordered four-exponential identity and the two transport discrepancies are correct. The stated norm comparison is false in the inherited convention. Apply repair N below. The curl bound and both real-projection curvature bounds then follow with a larger fixed `C_s`. |
| Step 2, WU 117–125 | **ADVANCE** | The recursion is on straightened angles, not plain angles. Dividing by `t_q` leaves summable `t_q^2` and `t_q` errors. The first-exit bound is uniform in depth after the two fixed smallness choices. Endpoint factors are explicitly supplied by I1's checked source; holomorphy is on the same fixed small chart. |
| Step 3, WU 129–135 | **ADVANCE** | `r <= r_B/(2C_4)` keeps the datum perturbation inside the I2 ball. Its crude `H` is independent of the small curvature radius. The admissibility of `V_0`, used here, is verified by I4 in Step 4, without using the desired complex estimate. Keep I2's axial-representative bound, including its fixed conjugation constants. |
| Step 4, WU 139–147 | **ADVANCE** | I4 retains `s^2`; the two real fields have curvature controlled by the repaired Step 1. Real uniqueness identifies the real values of the same holomorphic branch. I3 yields (4.4) with `C_1=B_1 C_3 max(1,C_s)`. This is regular critical-orbit uniqueness, with the minimality limitation retained. |
| Step 5, WU 149–153 | **ADVANCE** | Both projections contract the chosen field norm. `t <= s alpha_1'` makes the Taylor error quadratic with the same `s^2`. Multiplication by `eta_n^2` restores the plaquette units. Doubling `max(K,1)` gives the strict inequalities since `alpha_0'>0`. Independence of the listed late parameters is conditional on the corresponding uniformity in I1–I4. |
| Step 6, WU 155 | **ADVANCE** | The cited collar estimate and `M >= 2LR_1M_1` give room for the local stencils, under the standing `L >= 4d` and `R_1 >= L` floors. Setting `A'=0` gives the real-factor bound. Preserve the default determining sets and complete read sets. |
| Corollary B, WU 159–165 | **ADVANCE** | The two unit changes give radii `(mu alpha_0',mu alpha_1')`. Since `mu^2 <= mu`, (5.1) fits precisely the one-power hereditary clause. The same real factor and all the other supplier hypotheses are retained. |
| Lemma C: C1, WU 167–173 | **ADVANCE** | Here the factor `b=sqrt(N)` is already included. The exponential remainder is quadratic in `xi r`, the linear term is the discrete curl, and division costs no inverse spacing. The chosen `D` is conservative. Call the norm normalized Hilbert–Schmidt rather than “trace norm” to avoid the usual nuclear-norm meaning. |
| Lemma C: C2, WU 175 | **ADVANCE** | I7 at the unit background gives the stated quadratic current remainder and `J(1)=0`. The second-order input is exactly `D_1^*D_1 A`. |
| Lemma C: (5.3), WU 177–185 | **ADVANCE** | The choice fits (B1) with factor-two room and the domain ceilings by (C0). The `r^2` inequality, strict field bound, plaquette bound and independent/true-current bounds all have the claimed room. The trivial cube gauge is valid. |
| Lemma C(c), WU 187 | **ADVANCE** | Nested cube grids put `X` in the required lower grid. The rule-1 tower gives coefficient at most `alpha_0/2`. The containment `tilde X^{-2} subset X^{wr j}` has the required cube margin for the standing odd `L>1`. |
| (5.4) and seed applications, WU 189–193 | **ADVANCE** | Shrinking the single fixed `c_T` to `c_*` supplies the true-pair and independent-current seed steps at all running radii; R2 descends by `alpha_{i,j} <= alpha_i`. The source norm is read after `A=ell_j Z` and with the corresponding current-unit conversion. |
| Last sentence of WU 193 and WU 195 | **REVISE** | The *formula* for the radius survives, but its numerical value can shrink. Only the displayed ratio cancels `c_T`. The list of affected fixed constants is not exhaustive; see §3. |

**Repair N (WU 103–107, written out).** Use `|X|=(tr X*X)^{1/2}` with normalized trace, and reserve `||X||_op` for operator norm. CA-I 10306 gives

\[
 |X|\le\|X\|_{\rm op}\le b|X|,\qquad b=\sqrt N.
\]

Unitary transport preserves each norm, but does not remove `b` when passing between them. For example, the traceless complex matrix `E_{12}` has operator norm 1 and normalized Hilbert–Schmidt norm `N^{-1/2}`. Thus the implication written at WU 103 is literally false if its double bars mean the source's operator norm; interpreting both bars as the normalized norm would instead lose the submultiplicative estimate used next.

The four exponents obey `||X_nu||_op <= b eta |A'|`. Their product's terms of total degree at least two are bounded by

\[
 e^{4b\eta|A'|}-1-4b\eta|A'|
 \le 8b^2e^{4b}\eta^2|A'|^2
 \quad(\eta|A'|\le1).
\]

Write `P=partial U_r`. For either discrepant transport, operator norm gives

\[
 \|\operatorname{Ad}(P)Y-Y\|_{\rm op}
 \le2\|P-1\|_{\rm op}\|Y\|_{\rm op}
 \le2b^2|P-1|\,|Y|.
\]

There are two such terms; their factors `eta`, `|P-1|<alpha_0' eta^2`, and `|Y|<alpha_1'` give the same `C eta^3 alpha_0' alpha_1'` error as (4.1), with fixed `N` dependence. Also replace WU 107's operator-norm upper bound by `2b alpha_0' eta^2`, or write that line entirely in normalized Hilbert–Schmidt norm. Passing back by `|E| <= ||E||_op` gives (4.2)–(4.3) with a larger `C_s(d,N)`. Nothing acquires depth, mesh, volume or radius-ratio dependence. This repairs the first defective proof step without changing (A2).

For clarity, carry the inherited complete-read convention explicitly into (A1) and Lemma C: local differences, currents and averages are read on their required stencils/carriers, including the outward rows. A norm bound only on a smaller set that omits those reads would not be the named source hypothesis.

## 3. Exhaustive-search check and repairs to §6

The list is **not complete as written**. The literal `1.17` count itself is correct: 34 matching lines in CA-I, of which 31 concern CMP 109; 27 in CA-II, none concerning CMP 109; 10 in CA-III, of which only 111326 concerns CMP 109. The other matches concern CMP 116/122a/122b or decimal numbers. I also searched `2B_3` with braced subscripts, spacing and line-break variants, `B_3^2`, `c_T`/`c_{T}`, the implication wording and variants, and the supplier/display labels. Symbol matches are not automatically uses of (1.17).

For reproducibility, the 31 CA-I lines concerning CMP 109 are:

`15918, 15926, 15933, 15938, 15940, 15946, 15961, 20172, 29558, 29563, 29570, 32423, 32485, 32499, 32501, 32601, 32705, 34069, 34083, 34148, 34168, 34202, 34212, 34925, 34933, 35005, 38114, 40196, 42677, 154851, 166588`.

**Add or correct the following records.** The distinction between a fresh admission, a downstream use of a radius, and a separate assumed input is load-bearing.

| Source range or occurrences | Missing/corrected classification | Effect on this repair |
|---|---|---|
| CA-I 32703–32706 | Additional explicit status record for the complex sufficient condition. | Record it with §1's status references. |
| CA-I 40189–40212, especially 40194–40197 | Smaller (i)–(iii) implying (iv) is named as a **separate input**; that openness argument does not derive or use it. | Omitted exclusion, not an additional fresh consumer. |
| CA-I 42545–42640; 42670–42688 | The former explains why the proposed weakenings do not give the own-radius clause; the latter expressly declines an assertion about (1.17). | Add to excluded assertions. Do not claim A supplies those own-radius conclusions. |
| CA-I 144962–145024, 145167–145182 | Kernel membership includes another CMP 109 regularity statement and bounds containing `2B_3`; it is a separate regularity input. | Not an application of (1.17), and not supplied here. |
| CA-I 148810–148832, 148885–148903; 149809–149888, 150005–150055, 150745–150755, 151807–151919 | Window minimizers and their scale/rim thresholds use regularity, restriction, minimizer and response hypotheses, with factors involving `2B_3`. | Add to the separate-input/threshold records. These do not derive general complex (1.17), and A does not supply the window machinery. |
| CA-I 155275–155438 | **Not a real pair.** At 155310–155316, `W=exp(i eta H)U_0` is complex. The real `U_0` supplies its real-factor conditions; 155388–155426 obtains the complex tower bounds through the separate nesting input. The `2B_3` comparison at 155421 is arithmetic after those bounds. | Remove from WU 214's all-real list. Retain as complex nesting with a real base. Lemma C is not its supplier. |
| CA-I 155940–156060; 156177–156189 | Complex minimizer family with unit base. Its (iv) is obtained using N1 nesting at 156008–156033; the subsequent cutoff-free constant calculation uses the same auxiliary radius. | Omitted complex membership, but not a fresh use of complex (1.17). Keep nesting as a separate premise. |
| CA-I 153616–153622, 154875–154918, 154959–154970, 155139–155150, 156425–156447; 163946–163970, 164015–164026, 164136–164183 | Complex-background and cutoff-free radius constants, followed by auxiliary coupling thresholds; `2B_3` enters definitions, substitutions and comparisons. | Additional symbol uses, not an additional application of the sufficient-condition sentence. Preserve the complex-background and threshold hypotheses. |
| CA-I 128551–128930 | Real frozen-background argument. Hypothesis (b) at 128807–128817 asks for current bounds uniform in the number of strata; 128923–128930 keeps that uniformity as an assumption. | Real does not mean wholly supplied by A. Preserve the multilevel stage input. |
| CA-I 154825–154863; 155490–155511 | Respectively an excluded general complex assertion, and a rejected linear-datum route. | Replace WU 218's “definitions that fix units” classification for these two ranges. |
| CA-I 117207–117328; 121282–121350 | Respectively B'-ball/entry-conversion ceilings, and a near-pair chain mentioning an alternative starting route. | Separate them from a list purportedly consisting entirely of rejected literal (1.17) applications. Their own source inputs remain. |
| CA-I 29458–29466, 29640–29642, 29982–30012, 30562–30573, 31304–31457, 31605–31664, 31709, 31740–31756, 31833–31874, 32242–32409 | Additional uses of `c_T`: shift/simple-case radii, total-field ratios, fundamental shares, counterterm leftovers, smallness ceilings and extraction constants. | Add as downstream consumers. Shrinking `c_T` may enlarge fixed constants or require a smaller final coupling ceiling. It does not cancel from all these expressions. |
| CA-I 35963–35971 | Gauge-transported complex pair over an existing real factor, with a `c_T`-sized perturbation. | Not a seed with real factor 1. The tower condition is preserved because the relevant configuration is unchanged; this is not fresh admission by (1.17). |
| CA-III 81024–81032, 81041–81052, 81118, 81155–81159 | Cauchy second-derivative/kernel estimates with `4B_3^2 mathfrak r_j^{-2}`. | Omitted downstream radius consumer, additional to the CA-III 90585–90624 extraction record. |

Other `2B_3`/`B_3^2` occurrences do not add a fresh complex (1.17) premise: the near-case gauge bounds and their ceilings (e.g. CA-I 33704–33723), real cube-gauge estimates and floors (36519–36546, 36678–36705, 37914–37943), real reblocking bounds, datum-radius and running-constant comparisons, and estimates from CMP 102 or CMP 109 (3.38). In CA-II these include 43094–43139 (remainder constants), 44456 and 44514 (a decimal `1.2B_3`, not `2B_3`), 86147–86161 (base regularity), 95984–96138 (real regularity with an explicit nesting assumption), 109508–109517 (local real minimizer), and 119774–119847 (a separately assumed support/comparison energy argument). CA-III 34805–34814, 35023–35038, 35364–35370, 36974–36999 and 37123–37140 are regularity/averaging/refinement estimates from the real CMP 102 machinery, not the complex sufficient-condition sentence. Constants involving `B_3^2` alone also occur in unrelated large-field bounds.

The `c_T` spelling has unrelated homonyms: CA-I 70548 and 75590–75665 concern term constants, 119041/119386/119406/124591 concern a size constant, and CA-II 81373 concerns a moment-recursion constant. They must not be reset by (5.4). “At every occurrence” at WU 193 must mean **every occurrence of the true-pair/polydisc constant**, not every identical character string in the account.

**Repair to WU 44, 212 and 268.** Replace the universal real/seed classification by:

> The fresh admissions in the true-pair and polydisc arguments have unit real factor and are supplied by Lemma C. The generic small-pairs supplier is replaced by Corollary B under (B1), and real curvature-only estimates may be retained under their original hypotheses. Other complex memberships, including minimizer families over nontrivial real bases, retain their separate nesting, inheritance, gauge-transport or increment suppliers. The search found no further fresh application of the original complex (1.17) requiring an unbudgeted non-seed pair; it did find additional complex memberships, excluded assertions and downstream constant uses.

This also avoids confusing the generic hypothesis at CA-I 34067–34072, which permits a nontrivial real factor, with its concrete seed applications. The corrected result supplies a replacement implication with a changed budget. It does not prove the original generic hypothesis as printed.

**Repair to the `c_T` claims, WU 193, 195, 210 and 275.** The cancellation in `mathfrak t_j^{-2}` is correct, because both numerator and denominator carry the same `c_T`. But:

\[
 C_\beta=4B_3^2 C S(\delta_1)\mathfrak r_\circ^{-2}
 \quad\text{(CA-II 4721)},
\]

\[
 \mathfrak e_Q=\frac{C_{\mathfrak a}B_3M_Q}{c''c_T}\varepsilon',
 \qquad
 C_{\mathfrak e}=C_wB_3\max\{2,C_{\mathfrak a}M_Q/(c''c_T)\}
 \quad\text{(CA-II 96412, 97071)}.
\]

Thus the field-amplitude cancellation in CA-II 96444–96468 removes running amplitudes, not `c_T`. Similarly, CA-III 90592's

\[
 C_\Pi=C_\beta\mathfrak r_\circ^2/(c_TC_*)^2
\]

retains `c_T` dependence after inserting `C_beta`. Replace the last table entry at WU 210 by **“the same form of polydisc radius; the ratio `mathfrak t_j` is unchanged; fixed extraction and response constants may increase.”** Add `C_beta`, `C_mathfrak e` and their descendants to WU 195, using “including” rather than an exhaustive list. Replace “unchanged radius” by **“the same radius formula with one possibly smaller fixed `c_T`.”** Once this positive constant is fixed before the final coupling choice, the powers of the coupling and logarithms are unchanged. The cited `q>p_0` limit still gives a one-sided small-coupling ceiling. This is not cancellation of all constants.

The broad CA-II 94811–97192 citation also contains separate box-minimizer extension and nesting hypotheses (notably 96010–96026 and the core-estimate hypothesis at 96276 onward). The corrected seed inclusion does not construct those maps or remove those hypotheses.

## 4. Argument check: §7 and the Stage 5 remark

| Item | Verdict | Finding |
|---|---|---|
| WU 222–226, displayed order | **REVISE** | It is a partial dependency order for this argument, not a replacement for every stage in the account. Preserve all earlier floors and distinguish the early block/parametrix sizes from late `M`. Also place `B^{(109)}` before `M` when spelling out a total order: CA-I 4434–4437 explicitly requires that order. The phrase “every letter chosen after” cannot accompany a listing that puts these in the opposite order. |
| Smallness ceilings, WU 226 | **ADVANCE** | Choose `bar alpha_1'` small for the fixed analytic ball and the quadratic ceiling, then `bar alpha_0'` small. The first-exit smallness can be included. No constraint on the ratio of the two running auxiliary radii is introduced. |
| R1, WU 228 | **ADVANCE** | The four D2 lengths are early constants; the two tower gaps dominate the chosen required gap. The account's gap number and a1's localization factor must remain distinct. Theorem A's parameter independence is read from the named inputs with their uniform floors. |
| Stage 5 remark, WU 230 | **ADVANCE**, with the explicit choice below | The cap `R_1 <= M_1/mathfrak M` is real. Adding an early floor to `M_1` resolves existence of a compatible choice. It does **not** preserve arbitrary later upward freedom of `R_1` with `M_1` frozen. |
| R2, WU 232–236 | **ADVANCE** for the ceilings; **REVISE** for the claimed failure without them | The ceilings are sufficient and downward, and running radii inherit them. The example where `alpha_0/(4K^sharp)>bar alpha_0'` shows that this chosen proof exits Theorem A's domain. It is not a counterexample to the seed-inclusion lemma. |
| No square ceiling, WU 238 | **ADVANCE** | The auxiliary-radius choice avoids a floor on the later absolute `alpha_0`. The displayed running-radius ratio tends to zero at weak coupling; it is a possible later ceiling, not a premise used here. |

**Explicit Stage 5 choice.** After the fixed early estimates, define `R_req` to be the least power of `L` satisfying all the account's earlier floors for `R_1`, including `R_1>=L`, the kernel/summation floors and the D2 floor. Strict floors are satisfied strictly in this choice. The relevant kernel floors are CA-I 13415–13417; their coefficients are fixed decay and blocking constants, not late amplitudes. Choose the Stage 5 power `M_1` to obey its old floors and

\[
 M_1\ge\mathfrak M R_{\rm req}.
\]

Then choose `R_1=R_req` at its recorded later position, or choose a power satisfying

\[
 R_{\rm req}\le R_1\le M_1/\mathfrak M.
\]

This meets CA-I 32847–32851 and both tower-rule gaps. Fix the remaining early constants, then `B^{(109)}` and the late `M` in their required order, impose R2 at Stage 7, and choose `c_T` and the final coupling ceiling after their inputs. Increasing a late `M` does not force an increase of the already chosen `R_1`. There is no cycle in this choice for the present argument. It does not establish the account's separately assumed uniform local-background operator bounds or its entire global order theorem.

**Replacement for the overstatement at WU 236:** “Without R2, the auxiliary value `alpha_0/(4K^sharp)` need not lie below the available Theorem A ceiling, so this proof of the lemma over the advertised target-radius range is not justified. R2 supplies the missing domain restriction; no counterexample to seed inclusion is asserted.”

## 5. §§8–9, novelty and Result

**Section 8: REVISE only the identified attribution/status wording.** The source statuses for I1–I7 are supported by the cited passages and the repository gate records. The scope of the a1 gate is conditional on F0 and its repairs; the flat-port gate is a scoped flat/default-convention check with W1–W3. WU correctly does not turn those records into an audit or an unconditional proof. “Checked” describes the recorded other-model reading, not mathematical independence merely from a model count.

The Taylor estimate is already stated and explained in mechanism 8; the new presentation gives explicit remainder constants. Theorem A implements the already stated corrected theorem from the named rebuilt inputs. ER8 has an actual proof under ER7, including the same auxiliary radii, so WU 248 must be changed as specified above. The real-field numerical `2B_3` bound can be kept as a separate published input; A itself establishes its own `K^sharp`, not equality of those constants.

**Section 9: ADVANCE for items 1–7 at their expressly limited scope; REVISE item 8.** Original L17 remains open, not refuted by the scale-loss argument or the flat commuting example. The critical/minimal distinction, default determining sets, pointed-core exclusion, unused cube-gauge/current hypotheses, separate nesting/own-gauge/near-case inputs and absence of any conclusion about T0 must all remain. The claim that the “complex use is a seed or real” is false as an inventory description and should be replaced by the narrower statement in §3.

The novelty statement should read:

> The corrected quadratic budget, the real-point mechanism, and the conditional small-exponential inclusion are already in the Sussman–Alpoge outline. This note writes out their mechanism using the repository's named CMP 102/averaging inputs, makes the constants and domain ceilings explicit, and reconciles the fresh seed admissions and constant choices with the complete account. The true-current and `U^c_j` specializations and the correction of the target-radius polydisc step are explicit consumer work. R1 and R2 are compatibility/domain repairs, not new estimates. This is a comparison with the cited texts and repository results, not a claim of global mathematical priority.

**Result: REVISE the scope and radius wording; preserve the conditional conclusion.** A suitable replacement is:

> On I1–I7, in the default determining-set convention and on their complete read sets, with the corrected norm constants, R1 and R2, the argument proves Theorem A with an early fixed `K^sharp` independent of the auxiliary-radius ratio, depth, mesh and volume as specified by those inputs. Corollary B replaces the small-pairs implication under (B1). Lemma C supplies the fresh unit-base true-pair and independent-current polydisc admissions at a radius of the same form `c_T min(alpha_0,alpha_1)`, with one possibly smaller fixed `c_T`. Its dependent constants and the final coupling ceiling must be read at that choice. Other complex memberships retain their separate suppliers. This supplies the corrected inclusion component along the stated clause-(0)(g) and true-pair-(c) paths; it proves neither the original curvature-only (1.17), the remaining clause-(0) inputs, nor T0. Minimality identification and the other scope restrictions of §9 remain attached.

WU 8 and 277 accurately described the draft's unread status before this check. After incorporating these findings, replace that description by a dated reference to this gate and its **REVISE** outcome; do not say the revised draft was checked unless the changed text is subsequently read. This gate itself edits neither the write-up nor any status register.

## 6. Evidence and verification boundary

The pinned source files and SHA-256 identities are:

| Source | Local fetched copy | SHA-256 |
|---|---|---|
| SA | `/tmp/sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | `/tmp/sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | `/tmp/wu-l17-check/sa_ca_II.tex` | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| CA-III | `/tmp/wu-l17-check/sa_ca_III.tex` | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

Excerpt records and full search results are under `/tmp/wu-l17-check/`: `read.log`, `hits-*.txt`, `expanded-*.txt`, `index-hits.txt` and `r1-hits.txt`. These are recovery aids, not computer-certified proofs. The findings above identify the source lines needed to reproduce the substantive comparisons without rereading whole volumes. The prior constituent gates were used at their recorded scope; this check does not re-establish all published or repository inputs, review every theorem in the account, or certify any physical conclusion. Only this gate file was written in the checkout.

Checked line by line by Codex (gpt-6-astra).
