# B98-P5 round 2: line-by-line check

Codex (gpt-6-astra), xhigh; checkout `125fb568be535c9e1ba3e185c7582723cff3c1cd`; 2026-11-07. Research check, not an audit. This grants no status.

## 0. Scope and source identities

Target: FINISH row 431, `library/b98p5-r2.md`, Claude Opus 5.5 max, Mini worker 2. Only this report is edited. The requested prior gate does not exist. `library/prior/b98p5.md` identifies the real-reference work as already done and the carrier bridge as open. Registry B98-P5 assigns this round to `b98p5`; PRINT-AVERAGE is its unowned alias. No separate proof lane is started.

Read GOAL, the specified FINISH instructions, round 1, its prior-work digest and `pi-gate.md` §3.2 before round 2. `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent. The four supplied SA files have the exact SHA-256 identities recorded in round 1 and its prior digest, including CA-I `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`. The supplied source revision is `31a47c543775`.

Page images and text retrieval are reading aids only. No computation discharges a mathematical step. CMP 109 is not on this laptop; statements attributed to it are checked against the account's quotation, not against its original printed pages.

Dispositions below concern the exact hypotheses stated with each result. The valid real-reference work is reused, not re-proved.

## 1. Opening summary and objects (§1)

**REVISE — distinguish the cube test from the full cited setting.** CA-I 12949–12967 and 13058–13066 explicitly use side-12 class cubes. CA-I 24824–24843 gives their two-layer containment and nonempty lower-layer intersection. These support the fixed-side interpretation used in Proposition 1. Write `S_12` for precisely this cube-test class, with (S2)–(S3). It is the account's explicit side-12 specialization of (S1). The sentence at 12955–12957 asserting coverage by these cubes is a further claimed consequence; the construction below refutes that consequence too. If coverage is instead imposed as an additional hypothesis, the construction is excluded.

**ADVANCE — the geometric restriction concerns only the outer region.** CMP 99b p.394 permits a surrounding layer, and p.396 specifies the big-block neighbourhood of Omega_1 for Omega_0. CMP 96 p.224, (2.1)–(2.4), permits sums of big blocks, the nest gap and whole-lattice lower regions. Its later discussion at pp.228–229 does not make every nest maximal: the smallest-domain choice there is an application. CMP 99b p.393 imports these nest conditions unchanged. Thus no additional *stated nest-thickness condition* in these passages excludes a higher-level island. Taking the big-block parameters sufficiently large, as required at CMP 99b p.408, does not remove the example.

**REVISE — the unqualified identification of Balaban's class.** P.396 says that the size number is at least 10, and bounds the potential by the cube's size times alpha_0. P.409 says the number may be taken equal to 12 in its localization argument. The example refutes the fixed-side-12 cube test even when Omega_0 obeys p.396. It does not refute the alternative class testing all larger cubes with their size-dependent bounds. An index-(k-1) cube of side about `(wL+2) M ell_(k-1)` reaches the island in that class. Keep this qualification in the summary and result, not only in the remark at the end of §2. Do not describe the restricted setting as differing from the account solely by Omega_0 without specifying the cube-size and radius conventions.

The printed images also correct a source detail: CMP 99b p.408 defines its enlargement with side `(2+2n) M ell_j`; its fifth enlargement has side **12**, not 11. CA-I 12955–12957 itself says 11. This does not change the thin-island argument. It does prevent using that account sentence as an exact transcription of the paper.

The carrier and Frobenius-norm definition of (D) agree with round 1. The outline separately *requires* real and complex curvature bounds (SA 10129–10137); it does not prove them from this cube test. Its local-gauge hypothesis at SA 11552–11554 is likewise explicit. The index rows and neighbouring obligations were read before these source lines. No outline result is being re-proved here.

## 2. The finger and Proposition 1 (§2)

### 2.1 Literal finger

**ADVANCE — the changed bond is outside every positive-height carrier.** For height 1 the prescribed finger distance exceeds L eta. For height at least 2, the preceding nest gap keeps the carrier inside Omega_1. The geometric reason is especially simple: translate the second endpoint block by one row length to the first; this bounds its distance to Omega_j in the l1 metric as well. Thus the literal print-inverse example gives zero curvature on these carriers. It does not refute (D).

### 2.2 Proposition 1(a): admission

**REVISE — make the parameter choices literal.** Use the account's admitted nested grids and torus periods; for example, take M a permitted power of L and P=2L^m with m sufficiently large. For the simplest counterexample take k>=2. Then Omega_0=Omega_1=T, so the p.396 outer-neighbourhood rule holds exactly. For k=1, select the stated neighbourhood alternative unless that neighbourhood already fills the torus; the default choice Omega_0=T need not obey that rule. The empty-complement gap argument and the block alignment are otherwise correct. Arbitrarily increasing the allowed period satisfies all stated room requirements.

### 2.3 Proposition 1(b): all radii

**ADVANCE on S_12.** The three index cases exhaust the cube test: the lower layers are empty; no side-12 cube fits in F; and an index-(k-1) test must reach the complement of F. The centre is too far from that complement. The gauge on every tested cube is the identity, and both the twist and the independent current vanish. Thus every positive radius works.

One boundary convention needs an explicit repair. The account associates bonds to a region by **at least one endpoint** (CA-I 12721–12722); §1 silently substitutes two endpoints. Both endpoints of b_0 must therefore be excluded. The centre choice gives distance to the complement in each possible exit coordinate at least `w M/2-1+eta`, which is at least `12 M/L+eta`. Moving to the other endpoint loses at most eta. Both endpoints consequently remain farther than the test cube's coordinate extent `12 M/L-eta` from every outside site. This repairs the argument for incident bonds as well. Alternatively choose w=11 throughout; it leaves ample room even for the neighbouring difference stencils. No new field estimate is needed.

### 2.4 Proposition 1(c)–(d): the curvature obstruction

**ADVANCE — the carrier placement and matrix calculation.** The nested centred blocks contain p_0. Its holonomy is V, with Frobenius deviation `2 sqrt(2)` and operator-norm deviation 2. The right side of (D) is `8 sqrt(N) a_0 L^(2-2k)`. The quoted sufficient threshold therefore gives a strict failure, at any k>=1. The twist and current cannot repair it. This also refutes the displayed curvature consequence at level k for sufficiently small radii.

**REVISE — retain the norm qualification in the latter threshold.** The assertion `a_0+a_1<1/2` is sufficient in operator norm. In normalized trace norm the left side is `2 sqrt(2/N)`; a sufficient threshold independent of k is instead `a_0+a_1<sqrt(2/N)/2`. The account uses both conventions in different places (compare I 820 and 161778–161795). Either choice gives the counterexample at round 1's small radii. The Frobenius statement (D) has no such ambiguity.

### 2.5 Proposition 1(e): logarithms and the account's extended map

**ADVANCE — failure of the literal CMP 98 identity-chart formula.** The first averaging bond on the ancestral straight path has reference transport V. For x=x_0+eta e_2 the two one-step transverse connectors and translated segment avoid b_0, so the relative loop is V^{-1}. CMP 98 p.23 (42), pp.35–36 (119)–(124), and p.37 (127) confirm the loop and its role in the composition. Its eigenvalue -1 is outside the stipulated logarithm chart. Hence round 1's literal q is not defined at this background. Cancellation at increment zero does not define the individual formula on a complex neighbourhood. Statement T, with that literal prescription and the S_12 domain, is false.

**BLOCK — extending “the map is not defined” to the account's globally defined block map.** CA-I 788–858 explicitly includes an extension off the small-field set: a double-contour average, followed by straight transport on the exceptional logarithm set. It says that this defines M on *all* real configurations. The same bad loop in a small-field formula does not erase this fallback. Repair: “The literal small-field formula and the formula (124) for its linearisation cannot be used at this pair. The globally extended real map remains defined; this argument supplies no analytic derivative for that extension.” No claim about its actual differentiability is proved here.

### 2.6 Locality and interpretation

**ADVANCE — the isolated-island rescaling**, with the stated isolation from the remaining regions and the same admitted grids. The argument reads a fixed neighbourhood at the island's own scale. “A finger works the same way” needs the changed bond in a similarly insulated middle portion; that extra variant is unnecessary for the counterexample already proved.

**REVISE — what is refuted.** The result is a counterexample to deriving (D), the display at I 12973 and the literal-map version of T from S_12, including its p.396 outer-region specialization. CMP 98 Proposition 5 is untouched: its real reference satisfies (52), visibly printed on p.26. The small-field extension on pp.42–43 retains that reference hypothesis. The alleged “tacit thickness” at CMP 99b p.409 is not a separately stated hypothesis. Its coverage assertion fails for the fixed-side interpretation on this island. Record that source tension; do not resolve it by both claiming failure on the paper's full class and adding an unstated thickness restriction to exempt the paper.

## 3. Positive statements (§3)

### 3.1 Definition (PL) and Lemma 3.1

**ADVANCE — (PL) implies (D).** The minimum corner level is the right convention for a face-crossing plaquette. Every carrier lies in Omega_(j-1), and hence its plaquettes have lambda(p)>=j-1. The resulting loss is exactly L^2. No cube test enters this implication.

The proof's sufficient floor `R M>=dL` should either be stated or replaced by the sharper block-translation argument of §2.1: each point of the outer endpoint block is at l1-distance at most ell_j from Omega_j. Thus `R M>=L` already suffices, and follows from M>=L and R>=1. This also covers j=1 and proper Omega_0. There is no additional thickness assumption here.

**REVISE — coefficient of the account's display.** On the class defined with alpha<=8a_0, (PL) gives coefficient alpha for the real-reference Frobenius bound. It does not automatically give the display's coefficient 4a_0 in the account's norm. Replace the sentence after the reduction to round 1 by: “(PL) supplies the required level-graded real curvature estimate; the literal coefficient 4 requires the corresponding stronger norm bound.” In operator norm one may impose `|partial U_r-1|<=4a_0(eta/ell_lambda)^2` directly. The proposed S1' later imposes coefficient a_0, which is stronger still. It is not merely the unchanged display moved into the hypotheses.

### 3.2 Corollary 3.2(i)–(iii)

**ADVANCE — (i), as an implication from the quoted CMP 109 hypotheses.** CA-I 13037–13050 explicitly quotes (1.11): the real factor has curvature less than alpha_0 eta^2 on X. Since ell_lambda<=1, this gives (PL). The norm conversion to Frobenius and `alpha_0<=a_0` under the first ceiling are correct. Thus these admitted pairs satisfy (D) on every admitted tower of X. This does not rely on enlarging a small cube inside an arbitrary X. CMP 109 itself is unavailable locally; the original (1.11) was not independently read.

**ADVANCE — (ii), retaining all hypotheses of the glued-window proposition.** CA-I 17059–17090 requires (i)–(iii) on the whole lattice and identifies the representative's real factor as the unchanged U. CA-I 17140–17150 explicitly keeps its (1.11)–(1.12) conditions across both seams. The ceiling on alpha_0''' therefore gives (PL). In level-k units the source's level-(k+1) estimate has the extra factor ell_(k+1)^(-2)<=1, so the proposed weaker top-unit estimate is valid. Gluing changes the twist, not this real reference. This checks the quoted-hypothesis implication, not the separately assumed rim theorem or the unavailable CMP 109 original.

**ADVANCE — (iii), representative-wise only.** A complex gauge transform need not have a unitary real factor equal to the transformed U_r. The corollary correctly applies (D) to the chosen representative and then invokes covariance. The numerical `4^4` derivative loss remains part of round 1's local-port input; this check does not upgrade that input.

### 3.3 Reduction to round 1

**ADVANCE as the stated implication.** On a rectangular double block the coordinate-tree slide count gives (18); every twist bond has level at least j-1, giving the asserted L loss in (19). The latter observation suffices without assuming precisely three possible levels. These two estimates supply the local small-potential hypothesis required by the port, on its stipulated identity chart and radii. They do not check §§2.1–2.5 of round 1, which remain a separate input. Consequently say “T follows on S^pl from the local port”; do not say that B98-P5 has been proved without that qualification.

### 3.4 Definition (TH), Lemma 3.3 and its two cases

**ADVANCE.** The definition supplies a genuine aligned cell partition at every positive level. Use admitted torus grids, or their local lifts, throughout.

The aligned-rounding inequality is correct, including its half-open right endpoint. In Case A the outside block provides the required lower-layer intersection. The two nest gaps put the rounded cube inside Omega_(j-1) and outside Omega_(j+1). In Case B the product of the cell intervals meeting the rectangular carrier really is a box of included cells; no convexity of the whole region is assumed. Its rounded cube meets layer j and misses Omega_(j+2). Both cases give one containing class cube, with index j-1 or j, including the interface plaquettes. The stated floor R>12d suffices in the l1 metric. No level-zero thickness is used.

### 3.5 Lemma 3.4, Theorem 3.5 and remarks

**ADVANCE — Lemma 3.4.** The two differences are exactly between the parallel bonds of the plaquette. Duhamel's identity has unitary outer factors. The commutator estimate therefore gives the displayed two linear contributions and the quadratic contribution, with the stated Frobenius conversion. Under sqrt(N)a_0<=1 their sum is at most `4 sqrt(N) a_0 (eta/ell_q)^2`.

**ADVANCE — Theorem 3.5.** Combining this with the verified containing-cube lemma gives (D), with the claimed better constant `4 sqrt(N) L^2 a_0`. This is a proof on (TH), independent of CMP 109 and the census. The direct supplied-gauge alternative in remark (2) also follows from the same containing cube. The level-zero observation in remark (1) is correct for the literal straightened map. Revise remark (3) to say that the island shows the implication cannot be extended to all merely gapped towers; (TH) is a sufficient condition, not a proved necessary condition for an individual tower.

## 4. Use-by-use census (§4)

### 4.1 Citation inventory

**REVISE — the census omitted explicit uses in CA-II.** The seven references to `4.5:rem-averaging-analyticity` in CA-I are exactly those listed. There are none to that label in II or III. But searching the plural citations as well finds:

| Additional source | What it actually uses | Disposition |
|---|---|---|
| II 54824, `5.8:lem-averaging-correction` | Propositions 4, 5 and 7 for local analyticity and the quadratic value bound | **REVISE:** add this real-background use. |
| II 54849 | The functional-derivative kernel estimate, from CMP 102b (72) and Propositions 4, 5 and 7 | **REVISE:** add the fine density bound. |
| II 54857 | A kernel majorant on the larger complex increment ball before Cauchy | **REVISE:** add the common-ball requirement. |
| II 60311 | Propositions 4, 5, 6 and 7 in the clause-(v) input inventory | **REVISE:** add this inventory entry. |

The lemma and proof at II 54788–54878 were read, not just the citation hits. Its background is real; its increment and data are complex. It therefore uses real-reference Proposition 5, rather than by itself establishing the moving-reference extension. The real-reference proof is prior work and is not re-done. Carrier admission remains attached. II 53792–53805 records local gauges for C_beta, while II 54237 explicitly appeals to the (3.35) class for rippled backgrounds. Neither citation count alone proves that every application has the exact S^pl contract.

Also distinguish the other inventory entries: I 166597 cites the printed-without-proof sentence, not explicitly Proposition 5; I 166568 includes Proposition 5 through “Propositions 1–7”. The remark itself cites Proposition 5 at I 13179 and the nonlinear lemma at I 13990 cites (157). These are not additional independent consumers, but belong in a literal citation inventory.

### 4.2 Each row of the supplied table

| Round-2 row | Check and disposition |
|---|---|
| I 13316–13326, near-bound frame | **ADVANCE** for the supplied-frame use: the text supplies a small potential for the window background. **REVISE** the added reference to Corollary 3.2(ii): that corollary bounds the unchanged real factor of the glued representative, not automatically the complex window minimizer itself. Keep those two sufficient routes distinct. |
| I 13680–13686 and 13742–13795, free-current lemma | **ADVANCE** that it states conclusions on all S and assumes the two printed leaves. **REVISE** “applications: true” to the explicitly checked CMP 109 entry points; I 4138 names this lemma as an input and is not an exhaustive admission proof. |
| I 13922–13931, (J5) | **ADVANCE**: this is (149) at complex U, with H^{J,T}J of weight -4. A density/Hessian contraction is required, not just a value bound. Its domain remains the lemma's domain. |
| I 13980–13994, nonlinear correction | **ADVANCE**: the section setting at I 13547 is S, and the lemma expressly assumes analytic, uniform Proposition 5. Its chart increment A' must remain distinct from the background twist. |
| I 14049–14054, step (c) | **ADVANCE**: the derivative estimate is composed with the separate kernel algebra and H^J inputs. Replacing S by a verified smaller domain is a proposed restriction of the theorem, not an already printed restriction. |
| I 14075–14080, step (d) | **ADVANCE**: (157) controls the functional-derivative leg, and Cauchy controls the other. The common larger complex ball remains required. |
| I 14500–14540, chart theorem | **ADVANCE** that its asserted domain is all S. **REVISE** the application claim: the one-power hereditary class at I 10600–10640 carries (1.11)–(1.16) by hypothesis, and the glued window supplies the checked representative. This verifies those entries, not every downstream chart use. |
| I 19578–19626, operator theorem (O) | **ADVANCE**: (i)–(iii) under the inclusion ceilings explicitly supply (PL) through Corollary 3.2(i). Other operator and localization hypotheses remain. |
| Same theorem, (F) | **ADVANCE** with the common representative specified at I 19629–19646 and rho4 at I 13116–13126. Both members of the intersection must hold at that representative; an arbitrary complex orbit member is not substituted. |
| I 29855–29926 | **ADVANCE**: the frame and composite small potential are expressly supplied. The two differences of B are spatial differences, not second functional derivatives. The unavailable CMP 109 estimates are being checked as quotations of the account. |
| I 161032–161061 and 161774–161806 | **ADVANCE** for the stated use: the derivative constant enters absorbed data-norm constants. These passages do not prove the frame or its uniform admission themselves. |
| III 36700–36736 | **BLOCK** as a completed admission check. The source uses the plain iterated mean of a minimizer on a complex data tube, together with the separate CMP 102b (190) response bound. III 35626–35640 states the minimizer comparison; it does not itself provide round 1's complete-carrier small-potential bound on that entire complex tube. Keep this as the expressly unresolved supplier. The Cauchy and diameter/2 deduction is correct once the uniform tube derivative estimate is supplied. |
| III 75787–75799; I 166589–166604 | **ADVANCE** as inventories only; include the additional inventory sites identified above. |

### 4.3 Proposed S1', curvature remainder and lowest levels

**ADVANCE — S1' is sufficient for the carrier bridge**, with the coefficient and representative specified in §3.1. The two quoted CMP 109 inclusions deliver that stronger real-reference clause under their ceilings.

**BLOCK — “every application found is covered” and “the account needs it only on S^pl.”** Even the original table leaves the minimizer tube unverified. The omitted CA-II uses require an admission check. Moreover I 52248–52300 carries cube regularity at levels 0 and 1 near Z as an input to operator-domain admission; it does not in that passage supply (1.11) on every relevant carrier. Calling the eventual domain an (i)–(iii) domain does not prove membership. These are explicit open dependencies, not disproved applications. Repair the conclusion to: “The checked CMP 109 entry points and supplied frames are covered; sufficiency for all downstream uses is not established.” No other owner's admission problem is attacked here.

**ADVANCE — the identified curvature-remainder dependency.** I 14084–14126 actually uses the claimed level-graded curvature consequence. The island defeats that consequence under the cube-only reading. Adding a real-reference plaquette hypothesis addresses that factor. The twist estimate and the rest of the curvature-remainder theorem are outside this check; retain the note's label “sketch” rather than claiming that S1' alone has completed its repair.

## 5. Result, summary repairs and recovery point (§5)

**REVISE — round 2 as a whole.** Its two positive carrier lemmas survive. Its cube-only counterexample survives with the explicit conventions above. Its unqualified source claims and claim of complete consumer coverage do not.

| Requested question | Answer established by this check |
|---|---|
| Is (D) false on the account's class? | **Yes for its explicit fixed-side-12 cube test (S1)–(S3).** The isolated bond at positive height refutes it. If the asserted covering sentence is instead made an additional premise, that is a stronger class and excludes this pair. |
| Is (D) false on Balaban's restricted class? | **Yes for the fixed-side-12 specialization with his outer-region rule.** Higher-level thin islands obey the printed nest conditions. **The unqualified claim about every reading of the inherited O(1)-cube class is not established.** Testing all larger cubes, or imposing the localization coverage as a hypothesis, excludes the example. |
| Is (D) proved on S^pl? | **Yes**, with alpha<=8a_0 and the elementary carrier-to-previous-region inclusion. CMP 109's two quoted entry points supply it. The original CMP 109 paper was unavailable. |
| Is (D) proved on thick towers? | **Yes**, under (TH), the stated floors and sqrt(N)a_0<=1, with constant `4 sqrt(N)L^2a_0`. |
| Does the account need B98-P5 only on S^pl? | **Not established.** The checked entry points and frame uses are covered, but the census omitted CA-II and leaves the complex minimizer tube and lowest-level admission unresolved. Frame uses are also a separate sufficient domain, not automatically membership in S^pl. |

Replace the proposed lead disposition by: “Carrier bridge proved on S^pl and on (TH); false for the fixed-side-12 cube-only class, including its prescribed outer neighbourhood. T on S^pl remains conditional on round 1's local analytic port. The all-application repair by S1' is incomplete.” No registry or status file is changed by this report.

The first decisive source correction is Proposition 1(e)'s extension from the literal logarithm formula to the account's globally defined map. The first decisive census correction is the omitted CA-II lemma. The independent positive results can be kept without settling either consumer admission problem.

Recovery point: retain the pinned sources above and this report. Reuse the checked cube-test example, Lemmas 3.1, 3.3, 3.4 and Theorem 3.5. Outstanding work is round 1's local-port check and the named consumer admissions, not another proof of real-reference Proposition 5 or another thin-island construction. Do not infer a counterexample to those downstream applications from this report.

Source coverage: round 2 was read whole. Every account range cited in its argument and table was read, together with the additional CA-II passages identified in §4. CMP 99b images read: pp.392–394, 396–398, 408–409; CMP 98 images read: pp.23, 26, 35–37, 42–43. CMP 96's geometry and relevant later qualifications were read in the supplied OCR, especially pp.224, 228–229, 231 and 234. The account/outline distinction was checked at SA 10111–10139 and 11510–11554, with the neighbouring index rows and obligations; SA 8108–8163 supplies the already written local analytic argument. Reading aids and citation inventories supplied no mathematical evidence beyond locating these texts.

Only `gates/b98p5-r2-gate.md` was written. No scientific status is granted.

Checked line by line by Codex (gpt-6-astra).
