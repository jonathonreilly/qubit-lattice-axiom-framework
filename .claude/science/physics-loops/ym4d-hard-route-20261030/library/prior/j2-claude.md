# Prior work: J2 (rooted ordinary sources)

Reading digest at `a123fc509`; research text, not an audit or independent mathematical check. No status is granted.
Paths are relative to `ym4d-hard-route-20261030/`. I/II/III denote the complete account at `31a47c543775`; SA denotes the outline. Copies: `/tmp/sa_ca_I.tex`, `/tmp/ym-prior-digests/sa_ca_II.tex`, `/tmp/ym-prior-digests/sa_ca_III.tex`, `/tmp/sa_ym4.tex`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Tadeusz Balaban for their RG construction. Reported proof standing always retains named inputs.

Search scope: whole-folder tracked `git grep` for target symbols, note names, account labels, paper names and equation numbers; both complete-account TSVs, outline chunks/neighbours and obligations were searched. Full hit logs: `/tmp/ym-prior-digests/j2-complete-search.txt`, `j2-outline-index.txt`, `j2-upstream-labels.txt`. These are navigation records, not proof evidence.

## 1. Exact target and statement sites

Read first: `library/t0-joins.md:250`–306 and `library/ro1-vs-ca.md:24`–73,122–152. They already give the supplier/domain comparison; do not redo it as a proof attack.
Exact J2 is SR1's **entire** UV1 import, `library/sr1.md:38`–65, equations (4)–(6), together with RO1 H-U, `library/ro1.md:54`–62. It is restated in `library/t0-joins.md:250`–292 as (J2.1)–(J2.3), in B04/B13/J2 of `library/t0-tree.md:132`, `:141`, `:250`, and FINISH row 359 (`FINISH.md:423`). All label it **open/imported**, not proved by SR1/RO1.
For every common admitted first-passage datum and compatible cofinal torus ℓ=2L^m, every ordinary finite real Lipschitz list (overlap/repetition allowed), W=Σz_i f_i with Σ|z_i|t_fi<2r_src and t_f=max(sup norm,c_M Lip f), require fixed cutoff/torus/list-independent r_src,A_src,C± and real V such that

`|Z(W)| ≤ exp{V + Re[U(W)+Σ_{s=0}^K Σ_X e_{s,X}(W)] + C+ ℓ^4}`, `Z(0) ≥ exp{V−C− ℓ^4}`,

with the exact source identity Z(W)/Z(0)=<exp O_K(W)>. U=Σ_p u_p(W(x_p)); u_p is holomorphic, zero at zero, with fixed-cutoff position/torus-uniform bounds (allowed to grow with K). Every e is holomorphic, zero at zero, reads only W|X+, is list-independent and zero when that restriction is zero. Sums converge normally on smaller balls. Bounds: |e_sX|≤A_src exp(−κ m(X)), diam X+≤C_dep a_s(m(X)+1).
All scales 0≤s≤K remain. Domains are nonempty unions of cubes of side Ma_s; m(X) is the minimum cubical edge-tree length meeting every cube; X+ has a fixed number of neighbouring layers. κ exceeds the **actual rooted entropy**, including type multiplicities. Require ST6: Σ_{X:X+ meets B(R),m(X)≥t} exp(−κm(X))≤C(R+1)^4 a_s^-4 exp(−ct), position-uniform. Sources include global mirror profiles and independent even/odd complex lists **before** conjugate evaluation. Division by the floor gives H-U with C_st=C++C−. No global zero-free assertion is part of J2.
Parameter/data matching is retained: J1 supplies common construction/order, not J2; H-T/TU10 is separate J3 (`library/t0-joins.md:71`; `library/t0-tree.md:144`).
Their exact outline counterpart is D1, SA:4088–4135, **named obligation**, expanded as ST5–ST6 at SA:23769–23831 and actual rooted geometry GS1–GS3 at SA:24051–24112. Repeated presentations: Theorem 4.1 SA:22514–22522 (**sketched**), Theorem 4.2 SA:22524–22550 (**conditional source hypotheses**), source convention SA:22556–22611, explicit assumptions for insertion SA:28229–28248. SA:28527–28568 then assumes the insertion consequence, not a J2 proof.
Index first: `library/sa-index/chunk-04.md:34`–43; `library/sa-index/chunk-21.md:22`–40; `library/sa-index/chunk-22.md:22`–30,53–59 all-state/rooted entries; `library/sa-index/chunk-23.md:59` records the limit consequence; `library/sa-index/chunk-26.md:6`–10,56–60 insertion entries; `library/sa-index/obligations.md:1201`–1211,1487,1589–1592. CA full index `library/sa-index/ca-full/index.tsv:602` labels `5.1:thm-correlation-theorem` PROVED, but source II:2791–2812 explicitly assumes outstanding preparatory window data. This is a conditional theorem, not an exact J2 theorem. Its (iii) at II:2919–2936 gives sourced local format; (iv) II:2937–2966 is a separated n≥2 torus bound. Neither alone states full repeated-list rooted J2. Leaves searches also locate geometric re-filed/hatted sources (`library/sa-index/ca-full/leaves.tsv:149`, `:152`), which are different, stronger-comparison constructions, not proofs of ordinary J2.

## 2. Existing pieces: keep their inputs attached

The detailed match table is already `library/t0-joins.md:291`–306.

| Supplier and standing | Coverage / missing match |
|---|---|
| P6 B3, `library/port/p6-correlation.md:2645`–2671, **ported, unrefereed conditional**; II:2791–2966 | Actual sourced RG format, shifts, local terms and torus-bound machinery. Must still identify its produced energies/domains with all-scale ordinary repeated-list J2. |
| P8 H-LOC, `library/port/p8-positivity.md:152`–166; II:60692–60821, **input** | Weight-local, list-independent, holomorphic zero-subtracted terms with Ce exp[−(1−δ)κ d_j(X)]. Need actual cubical metric/support conversion, all type counts, rate losses and any point term. |
| P8 H-DOM, `library/port/p8-positivity.md:200`–208 and §3.5, **input** | Full weight-class or every-finite-list reading; ordinary transported radius and factor-two mirror radius. Must use full reading, not just separated n≥2 tuples; admit even/odd lists before conjugation. |
| P8 H-TREE, `library/port/p8-positivity.md:191`–198; II:62045–62061, **cited CMP 116 (1.26)** | Anchored sum with a strict rate margin. Actual SR1 rooted indexing and multiplicities remain to be matched; convergence in a different metric is insufficient. |
| Frozen LSC, `library/lsc.md:27`–76, §3, `:720`–724, **checked conditional implication** | Common vacuum-normalized upper bound and floor, uniform last-scale constants and bounded offset. Retains representation, real-background, zero-source energy identification and eight sourced upper inputs. Not an all-scale local-energy identification. |
| LSC rescaling already settled, `library/t0-joins.md:303`–304 | Auxiliary N=2L^(m1+b), bounded b, gives N^4=L^(4b)ℓ^4. Absorb finite max in C± and take V=E_vac. Do not reopen normalization arithmetic; still include small-cutoff branch and all scales. |
| P10 A19/A20, `library/port/p10-stability.md` §§5–6 (A19 register at `:1037` onward), **ported conditional** | Integrated stability and exact sourced mass identity, in corrected convention. Retains positivity, representation, complex-move and history-majorant hypotheses. Source-free mass equality alone is not a complex-list upper bound. |
| LG1; SR1 Lemmas 2–6, `library/sr1.md:131`–331, **frozen conditional** | Once J2 holds: all-periodic-state domination, common holomorphic normalizer, one-point transfer, rooted counting and graded moments. These are consequences, not suppliers of J2. |
| SR1 Lemmas 7–10, `library/sr1.md:333`–512; freeze `:562`–568 | Factorial diagonal-flat extension, tensor density and RP transfer for supplied limits. No proof of source representation or first-passage realization. |
| RO1 Lemmas 1–3, `library/ro1.md:99`–289, freeze `:695`–702; SA:28229–28768 | From full H-U and LG1/CL1: insertion norm uniform in outside degrees, then analytic density/plates. No typed-source construction is needed, but ordinary source admission is not thereby proved. |
| CA per-ball theorem `6.4:thm-per-ball-bound`, II:63964–64285; P8 B7 `:560`–707 | Position-uniform fixed-order separated bounds at its inputs. Does not supply all-state n=1/repeated lists, graded factorial constants or the full rooted insertion package. |
| O4-2, `library/o4-two-point.md:173`–203, **checked restricted implication** | Two-point O(4) on volume-first torus-limit states can bypass H-U for that narrow task. Does not give all-order/component RO1, SR1 or J2. |

P6's carried open register must remain named (`library/port/p6-correlation.md:2647`–2670): C-admitted; C-boundary; C-preparation/window-data; C-B1/5.6 actual reached-link polydisc holomorphy; C-slots; C-frozen whole-disc bounds; C-sites' eight hypotheses; C-reference; cited C-one-loop; incomplete C-Mfree; unwritten C-sixth; C-last's nine hypotheses; C-compact; C-positive; C-rank only for N≥3; C-uniform-last for its literal uniform claim. Frozen LSC addresses its own uniform normalization issue, not all this register. P6 Result `:4630`–4662 keeps its published/printed and F01–F35 suppliers, not a closed RG construction.

Additional existing steps located by the whole-account rooted/source searches:

- SA:22947–23248 (index `library/sa-index/chunk-21.md:92`–112) assembles ordinary sources **conditionally**: actual data-line admission and sum-norm formation are hypotheses; SA:23147–23152 explicitly leaves those inputs unproved. Given them, SA:23154–23173 gives upper stability, :23175–23196 the positive-label floor, :23198–23205 representation/mirror matching, and :23207–23220 the rooted geometry/base-point polynomial absorption. This is substantial prior work toward J2, not an unconditional source package.
- `4.6:lem-rooted-tree-majorant`, I:22172–22348 (`library/sa-index/ca-full/index.tsv:68`, PROVED), proves a cluster-series majorant from its summability hypothesis; it does not verify actual RG activities. Its ported convergence machinery lies in P5/P6. Do not redo generic tree summation as a J2 solution.
- `5.2:thm-rooted-sum`, II:22529–22696, proves source-rooted summation over **cut cells/hubs** on its geometry and rate floors; `5.6:lem-rooted-sets`, II:45645–45698, proves the graph count (4D)^(m−1). They are existing ingredients, not an identification of that cut-cell metric with every actual SR1 cubical edge-tree energy. See P6's W6/W5 register and `library/sa-index/ca-full/index.tsv:677`, `:746` (both PROVED).

## 3. Earlier work, failures and repairs

No completed proof round of the exact J2 join exists in this checkout: row 359 is queued, and `library/t0-joins.md:306` expressly leaves the aggregate match open. Do not mistake the following older conditional routes for completed J2.

| Earlier route | Exact stopping point / repair already present |
|---|---|
| Outline ordinary source construction | SA:4088–4135 still requires actual domain geometry, stability and source classes; SA:22609 calls conjugated-copy input 4.11 “to be proved”. Analytic deductions do not verify formation/admission. |
| SA 2.8 signed action, `library/sa-2.8-terms.md:12`–27,384–406 | Ten-term bound is conditional on actual comparison backgrounds, P81/profile/geometry inputs. Criticality does not cancel the cut Wilson linear term; corrected (9a)–(9b) bounds it. Core cutoff needs inner-shell margin. Not a whole-history source estimate. |
| SA 2.10 erasure/replay, `library/s210.md:300`–310, `library/s210-fix.md:217`–227, `library/s210-3.md:177`–182 | Support/reference identities repaired via conditional replay/pivot lemmas. Full density equality fails when strip backgrounds differ; density interaction must be paid by gas. Formed-term label locality LOC, stopping nests/common-gauge tests, mass bound and rate order remain inputs. |
| SA 2.13, `library/sa-2.13.md:4`–8; continuation `library/sa-2.13-2.md:297`–311 | Forest summation and one-sided denominator prices proved conditionally. Actual joint reference critical chart, complex-pair remainder, absolute curved carrier moment, rigidity/owned-neighbourhood and healed regular-slot matching not supplied. |
| Preparation reduction, `library/pre-213.md:268`–277 | Inn's inner read uses ξ alone while the real reference varies with β; no uniform real bound to transfer. Act and actual denominator/Hessian inputs remain. |
| D1 floor/OH4, `library/d1-floor.md:14`–18,140–190 | Floor and upper variation are implications. Retain C1/history positivity, regular-action bound (ER7) and actual loaded-history hypotheses; a Haar-ball calculation is not full stability. |
| LSC round 1, `library/lsc.md:9`, `:708`–724 | Bare floor dropped E_vac; withdrawn and corrected in round 2. The normalized version is now frozen. Do not repeat the rejected bare floor or the overbroad claim that no normalization works. |
| Per-ball or separated correlations substituted for H-U | `library/ro1-vs-ca.md:42`–73,132–152; `library/t0-tree.md:132`–146: missing ordinary/repeated/mirror classes, n=1, actual rooted geometry and uniform outside-degree insertion. Fixed-order bounds do not furnish these. |

These are upstream partial routes. CM/CR/CA/CW/CH/CV endpoints remain separately named in `library/t0-tree.md:170`–177; merely conjoining their names does not prove the J2 match or J1's common-order identification.

## 4. Consumers and weakest statements

| Consumer and locus | Weakest identified input |
|---|---|
| SR1 one-point/state transfer and common normalizers, `library/sr1.md:109`–114,164–216 | Raw ordinary torus upper bound/floor with local list-independent terms and mirrored profiles, including n=1/repetitions. No global log needed. |
| SR1 graded moments/factorial growth, `library/sr1.md:115`–127,218–512 | Actual rooted all-scale geometry/strict entropy plus same ordinary-source bounds. Abstract ST6 alone is insufficient. |
| CL1 I3 / continuum compactness, `library/t0-tree.md:136`; `library/cl1.md:63`–74 | SR1's finite-cutoff all-state moments and one-point comparison; extension/density for supplied limits. J1 supplies sequence. |
| PH1 S3/growth/component realization, `library/t0-tree.md:138`–140; `library/ph1.md:44`–52 | Same common-centering, all-periodic-state comparison and factorial bounds; torus-selected limits alone do not cover components. |
| RO1 H-U / Lemmas 2–3 / higher-point rotations, `library/ro1.md:54`–62,121–289,630–649 | Normalized ratio H.U, actual rooted/list-independent energies and independent even/odd lists. Absolute V cancels. H-T is additional J3, not J2. |
| WR1 growth and insertion H1/H4, `library/t0-tree.md:150`–156; `library/wr1.md:19`–24,42–49 | SR1 factorial extension plus RO1 full insertion density uniform over outside degrees/coefficient sums. Two-point O4-2 does not replace it. |
| Full T0/component hierarchy, `library/t0-joins.md:240`–248; `library/t0-tree.md:123`–162 | Same data, centering and realized components across SR1/CL1/PH1/RO1/WR1; no switch between hierarchies. |

A weaker **normalized** formulation H.U with the same local/rooted/domain clauses suffices downstream: V cancels, and only C++C− is consumed. This normalization weakening is already used in the proofs; no current result proves its actual all-source realization. Fixed-order torus bounds suffice only for the restricted O4-2 route, not all J2 consumers.

## 5. Overlaps and disposition

FINISH row 279 (frozen Phase A, `FINISH.md:283`), 300 (RO1/CA comparison, `:364`), 316 (P6, `:380`), 323/327 (P8/P8b, `:387`, `:391`), 313 (LSC, `:377`), 358 (T0 joins, `:422`), 359 (this join, `:423`) and 376 (digest, `:440`) overlap through the sources/interfaces; none is a proved full J2. `library/t0-tree.md:250` owns J2 as one source-package leaf; J1 is data/order and J3 is component-uniform TU10. Neither `prior-1.md` nor `open-registry.md` exists here. No proof/port lane was started.

partly covered: sourced-format/locality inputs, normalized stability and downstream conditional deductions exist; the common-data all-scale repeated/mirror-source representation with actual rooted geometry and retained open suppliers is still unproved.
