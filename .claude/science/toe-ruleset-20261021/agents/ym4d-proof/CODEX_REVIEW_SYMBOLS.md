# Independent hostile review of SYMBOLS.md

## PRE-STATED

UTC: 2026-10-28 22:14:53 UTC

Review scope: `SYMBOLS.md`, `checks/sy1_*`, and narrowly matched source excerpts in the lane. The two additional procedural reads are `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `/Users/jonBridger/.codex/skills/review-loop/SKILL.md`. The owner's narrower read/write/no-git restrictions override broader workflow operations. Only this deliverable will be written. No source repairs or audit-status changes are authorized by this review.

Prior exposure: the prompt supplied alleged depth corrections 66/90/122, an alleged HW coefficient correction about 5.01e-22, family counts, and alleged omissions. These are hypotheses, not independently established results.

Targets and falsifiers, recorded before derivation:

1. Rebuild the PLD depth inequalities from the actual definitions, domains, and selected constants. Refute either the source's depth 3 or the audit's replacement if the exact defining inequality and minimality disagree. Separate sufficient rounded bounds from evaluated mathematical constants.
2. Rebuild the HW bad-event coefficient symbolically, maintaining the identities of every eta, epsilon, and prefactor. Refute the audit or source coefficient on an algebraic, exponent, domain, or quantifier mismatch.
3. Sample at least 30 individually identified classified use sites against matching source text. A mismatch of object, formula, domain, or locator counts as an error; report object errors and locator errors separately and disclose the sampling rule. Lower-bound collision counts require distinct witnessed objects, not token frequencies.
4. Challenge the audit's zero/coverage claims using the omitted families in the prompt. A finite family whitelist cannot establish lane-wide completeness. Inspect every executable check and ask whether an independently false target can make it fail, whether hard-coded examples miss changed inputs, and whether its outputs justify its prose.
5. Test the rename tables as an executable specification: overlapping scopes, same-scope multiple meanings, missing occurrences, ambiguous identifiers, stale locations, or incorrect replacements refute an unqualified mechanical-landing claim.

Review verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED is restricted to the precisely reproduced assertion; it never grants the scientific proof a status.

## Findings (appended during review)

### F1 — CONFIRMED: the PLD arithmetic correction, with conditional scope

Targets: `SYMBOLS.md:245–289, 838–850`; source strings `PLD.md:1097` “(L²/(2C_I))^{m}c_1 ≥ 2C_IL^{-2}”, `PLD.md:1098,1206,1244,1260` “m_τ = 3”; `RLARGE.md:64,976` defining η_1; `../ym4d-existence/EXISTENCE.md:1771` defining the KN ratio.

At d=4, L=3, N=2, A_d=9, write ε=e=67/10^41. The RS quadratic entry is active because e<512. Hence η_RS=e²/9216, η_KN=e/117. Dividing the descent inequality by η gives b^m ≥ z, where b=9/(2C_I), z=2048 C_I/e for RS and z=26 C_I for KN. Independently evaluated exact rational powers certify b^(m−1)<z≤b^m in each of the nine cases:

| C_I | KN, every e>0 | RS at e=67/10^41 | RS at e=2 |
|---|---:|---:|---:|
| 1 | 3 | 66 | 5 |
| 3/2 | 4 | 90 | 7 |
| 2 | 5 | 122 | 10 |

Thus the replacements 66/90/122 are PROVEN arithmetic for the displayed recurrence and selected e; 3/4/5 are not RS depths at that e. This does not prove the physical product estimate or the existence of (BG)_k: `PLD.md:1098–1099` explicitly leaves C_I<L²/2 OPEN and the aggregate transfer ARGUED. The fixed depth is not uniform over all smaller admissible ε: z∝1/ε and m diverges as ε→0. `RLARGE.md:71–73` gives a ceiling with unevaluated additional entries, not an established equality ε=6.7e−40. Landing “66” as an unconditional architectural constant would repeat the stale-input error.

### F2 — REFUTED: SY1-2's NO-DEFECT branch is not the negation of its target

Targets: `checks/sy1_criteria.md`, strings “FAIL (no defect; PLD's 3/4/5 is right ... ) iff any entry is ≤ 10”; `checks/sy1_symbols.py`, strings `elif any(m <= 10 for m in t_rs)` and `v2 = "NO-DEFECT"`; `SYMBOLS.md:285–289` claims the control validates the verdict.

The exact allowed control e=2 gives (5,7,10), not (3,4,5), while the registered criterion calls it NO-DEFECT. The test is sensitive to ε, but it distinguishes large depths from small depths, not wrong depths from correct depths. Its “every entry≥40” branch supports a difference in this particular run; its other branch is a false negative. Correct decision: compare each computed minimal depth with its corresponding claimed value; report equality only if the triples agree. The present live triple remains independently verified by F1.

### F3 — REFUTED: HW's corrected cap was promoted to a value of a_bad

Targets: `SYMBOLS.md:525–536,857–865`, strings “a_bad = (1/640)·...” and “under-states the suppression”; `HW.md:603–605`; `SQ.md:294–298`.

Let B=(1/640)(θ_SUP/53)². From the rounded θ_SUP=3·10^−8/C_D²,

B = [9/17977600000000000000000]/C_D⁴,

with 5.006229e−22 < B C_D⁴ < 5.006230e−22, established by exact rational comparison. The old θ coefficient 10^−8 gives 5.562477…e−23/C_D⁴. Thus **CONFIRMED**: the coefficient of the displayed upper bound in `HW.md:604` changes from roughly 5e−23 to roughly 5.01e−22; the exact rounded-input ratio is 9, and the ratio to HW's displayed 5e−23 is 28125/2809 ≈ 10.01246. `HW.md:826` repeats the stale 5e−23 coefficient and is absent from the proposed fix.

But HW writes a_bad=c_♭τ_♭² **≤** B, and only on ε_1≥53τ_♭. The audit replaces this by equality and claims that suppression increases. SQ's τ_♭ is a minimum containing other entries (`SQ.md:294`); the SUP entry need not bind. Consequently the corrected statement is a bound, a_bad≤B on that branch, not a_bad≈B. Increasing an upper bound alone does not establish a conservative change to a lower suppression estimate or preserve every downstream conclusion. That direction argument is REFUTED; blanket downstream safety is NOT-VERIFIED.

### F4 — REFUTED as unconditional: SY1-4 deletes the entry that can reverse its first half

Targets: `SYMBOLS.md:294–307, 966–970`; `checks/sy1_symbols.py`, `eta_q` and `r_rs`; source `RLARGE.md:64–65` explicitly says “unless δ_0/A_d binds”.

For e=67/10^41, put q0=e/4608, r=e²/9216. The full q is min(q0,δ_0/9). Deleting δ_0/9 gives r/q0=e/2=3.35e−40 and (e/117)/q0=512/13. These are lower bounds on the full ratios, not in general their values. A positive exact counterexample to the unconditional RS ordering is δ_0=9r/2: then q=r/2 and r/q=2>1. The missing condition for RS≤q is δ_0≥9r. KN>q survives deletion because decreasing q only increases its already >1 ratio. Thus the two-half verdict and quoted equality of ratios are CONDITIONAL on the omitted entry not binding. No assertion is made that this counterexample is the lane's selected δ_0; the script supplies no value or proved lower bound for it.

### F5 — REFUTED: the c_1 spread is 29,914.53, not 41,000

Target: `SYMBOLS.md:694,981` (“×4.1·10⁴”). For the two formulas the audit itself gives, (1/117)/(1/3500000)=3500000/117, strictly between 29914 and 29915, approximately 2.99145299145e4. The claimed 41000 overstates the ratio by 4797/3500≈1.37057. The collision remains serious; its advertised size is wrong. Source-site confirmation and corrected rename completeness are recorded below.

### Sampling contract (before the remaining source-site pass)

Use the 28 line-sites explicitly listed for θ_0 in §§4.2/4.5 (24 SQ, two HW, one PLD, one PROOF), the 11 ε_1 minority sites comprising the first five BFT_B entries in §5.2, all five FLOW entries, and the EXISTENCE loop-word entry, plus the first PG c_1 definition in §6.2: **40 line-sites total**. This is a deterministic, stratified convenience sample, not a random population estimate. Previously exposed defining sites are included and disclosed. Repeated glyphs on one listed line are one sampling unit. Score object identity separately from the published original locator, and account for §13's errata separately. This does not certify all claimed 239 sites or approximately 1600 file-level classifications.

### F6 — CONFIRMED object assignments in the sample; REFUTED locator freshness

Targets: `SYMBOLS.md` §§4.2, 4.5, 5.2, 6.2 and errata §§13.1–13.4. Forty independently inspected line-sites follow. “CONFIRMED” here means the quoted occurrence has the assigned mathematical role, not that its theorem is proven. All source line numbers are as observed during this review; accompanying strings and section descriptions control if concurrent edits move them.

| # | File | Audit locator → observed locator | Object assignment | Verdict |
|---|---|---|---|---|
| 1 | `SQ.md` | 183 → 183 | θ_SUP | CONFIRMED |
| 2 | `SQ.md` | 188 → 188 | θ_SUP | CONFIRMED |
| 3 | `SQ.md` | 210 → 210 | θ_SUP | CONFIRMED |
| 4 | `SQ.md` | 212 → 212 | θ_SUP | CONFIRMED |
| 5 | `SQ.md` | 216 → 216 | θ_SUP | CONFIRMED |
| 6 | `SQ.md` | 217 → 217 | θ_SUP | CONFIRMED |
| 7 | `SQ.md` | 218 → 218 | θ_SUP | CONFIRMED |
| 8 | `SQ.md` | 219 → 219 | θ_SUP | CONFIRMED |
| 9 | `SQ.md` | 225 → 225 | θ_SUP | CONFIRMED |
| 10 | `SQ.md` | 231 → 231 | θ_SUP | CONFIRMED |
| 11 | `SQ.md` | 294 → 294 | θ_SUP | CONFIRMED |
| 12 | `SQ.md` | 306 → 306 | θ_SUP | CONFIRMED |
| 13 | `SQ.md` | 318 → 318 | θ_SUP | CONFIRMED |
| 14 | `SQ.md` | 342 → 342 | θ_SUP | CONFIRMED |
| 15 | `SQ.md` | 557 → 557 | θ_SUP | CONFIRMED |
| 16 | `SQ.md` | 930 → 930 | θ_SUP | CONFIRMED |
| 17 | `SQ.md` | 1167 → 1167 | θ_SQ4 | CONFIRMED |
| 18 | `SQ.md` | 1168 → 1168 | θ_SQ4 | CONFIRMED |
| 19 | `SQ.md` | 1357 → 1357 | θ_SQ4 | CONFIRMED |
| 20 | `SQ.md` | 1622 → 1622 | θ_SQ4 | CONFIRMED |
| 21 | `SQ.md` | 1623 → 1623 | θ_SQ4 | CONFIRMED |
| 22 | `SQ.md` | 1628 → 1628 | θ_SQ4 | CONFIRMED |
| 23 | `SQ.md` | 1633 → 1633 | θ_SQ4 | CONFIRMED |
| 24 | `SQ.md` | 1634 → 1634 | θ_SQ4 | CONFIRMED |
| 25 | `HW.md` | 183 → 183 | θ_SUP | CONFIRMED |
| 26 | `HW.md` | 604 → 604 | θ_SUP | CONFIRMED |
| 27 | `PLD.md` | 1437 → 1437 | level-0 tilt | CONFIRMED |
| 28 | `PROOF.md` | 6502 → 6554 | level-0 localisation error | CONFIRMED |
| 29 | `BFT_B.md` | 2773 → 2773 | N2 flatness threshold | CONFIRMED |
| 30 | `BFT_B.md` | 2870 → 2870 | N2 flatness threshold | CONFIRMED |
| 31 | `BFT_B.md` | 2871 → 2871 | N2 flatness threshold | CONFIRMED |
| 32 | `BFT_B.md` | 2909 → 2909 | N2 flatness threshold | CONFIRMED |
| 33 | `BFT_B.md` | 2927 → 2927 | N2 flatness threshold | CONFIRMED |
| 34 | `FLOW.md` | 1927 → 1927 | disc radius | CONFIRMED |
| 35 | `FLOW.md` | 1931 → 1931 | disc radius | CONFIRMED |
| 36 | `FLOW.md` | 2834 → 2834 | disc radius | CONFIRMED |
| 37 | `FLOW.md` | 3000 → 3000 | disc radius | CONFIRMED |
| 38 | `FLOW.md` | 771 → 771 | mode amplitude | CONFIRMED |
| 39 | `../ym4d-existence/EXISTENCE.md` | 2205 → 2205 | loop orientation exponent | CONFIRMED |
| 40 | `PROOF.md` | 3629 → 3681 | PG constant at κ=1 | CONFIRMED |

Object-assignment error rate: **0/40 = 0%** on this sample. Original-locator error rate: **2/40 = 5%**. The two are PROOF's `CURV1_0 at θ_0` and the first `c_1 := 1/(3.5·10⁶)` definition. Even §13's corrected locators (6527 and 3654) are stale at this read (6554 and 3681). This is not evidence that the author originally read the wrong text; it is evidence that the tables are not executable by present line number. Strings remain necessary. These sample rates do not estimate omitted-use errors; F7 supplies explicit omitted uses.

### F7 — REFUTED: even the corrected c_1 mechanical rename is incomplete and creates a new collision

Targets: `SYMBOLS.md:697–701`, §9 item 3, §11.5 item 3, and §13.2's corrected “FIVE sites in PROOF.md ... plus LINEAR_PACKAGE.md l.354”.

The full matched PG-role list observed in PROOF contains **at least 14 lines / 16 tokens**:

`3681, 3688, 3692, 3694, 3696, 5376, 5382, 5386, 5619, 5620, 5726, 5732, 6114, 6181`.

The definition line 3681 and N5-coer line 5376 each contain two tokens. `LINEAR_PACKAGE.md:353–354` adds **two lines / two tokens**; the plan lists only 354. Thus this inspected PG chain needs at least **16 line-sites / 18 token substitutions**, not the original four sites or corrected six sites. The ten omitted line-sites after §13.2's correction include the load-bearing NA smallness bound, N5-coer proof and sharpened γ_i, and γ_0. A rename confined to the plan's lines leaves the defining constant and its consumers differently named.

Worse, the destination `c_PG` is already defined in the same file: `PROOF.md:2921`, “c_PG := min(1, κ)/(3.5·10⁶)”, also quoted at 2392 and 4906. The fixed `c_1` at 3681 is explicitly “Proposition PG at κ=1”. At the admitted κ=1/4 (`PROOF.md:3123`), the existing c_PG=1/14000000, whereas this c_1=1/3500000, exactly four times larger. Renaming the latter to an unqualified `c_PG` manufactures the same parameter/fixed-value collision the audit was meant to remove. The claim in §9 that this name did not exist is REFUTED. A possible precise destination is `c_PG(1)` after explicitly declaring the parameterized convention; choosing and propagating that convention requires a new checked patch.

**Disposition:** do not land the c_1 table mechanically. This is a semantic defect, independent of line drift.

### F8 — REFUTED: the audit treats a frozen supplier as current architecture

Targets: `SYMBOLS.md:271–277,346–368,728–734,917–926`, especially “This line supplies a_η to RLARGE”, and the assertion that the corrected depth changes the lane's live architecture.

The audit's downstream a_RS definition is `RLARGE.md:1020`, inside the explicitly frozen Appendix A beginning at **824**. The source's reading instructions at **830–832** replace the old PLD assumption by the forward joint moments, and supersede a_♯, c_RS and the old fixed n_♯. The current route explicitly lists `(PLD)_k (i)-(ii), (PLD-q)_k; RS-joint and the greedy joint pricing` under **“Not hypotheses of RLF-step v3”** at **513–515**. Its live exponent is `a := min{θa_bad,a_A}` (`RLARGE.md:88`), with `a_bad := c_pr·min{ε_1²,t_pr²}`.

This directly contradicts treating the appendix's a_RS supplier as a current RLF-step-v3 obligation. F1 remains a correct refutation of PLD's written RS-depth assertion. It does **not** establish that the active proof must acquire 66 levels of look-ahead. The audit must distinguish an erroneous surviving PLD statement from a consumed current architectural dependency. No external worker's verdict was used to make this finding; the source's route and replacement instructions supply the evidence.

### F9 — CONFIRMED lower-bound collision counts; NOT-VERIFIED completeness

Targets: `SYMBOLS.md` §§4.1, 5.1, 6.1, 6.2, 6.5 and §7. These are identity/type witnesses, not confirmations of every numerical bound in the source theorems.

| Family | Independently witnessed distinct roles and source anchors | Verdict |
|---|---|---|
| θ_0 | SUP ceiling (`SQ.md:188`); EPS-0 ceiling (`SQ.md:1622`); Chernoff tilt (`PLD.md:1437`); first-order localisation error (`PROOF.md:6554`, `CURV1_0 at θ_0`) | CONFIRMED: four witnessed objects; “two” omits two |
| ε_1 | Plaquette cut (`RLARGE.md:58`); N2 flatness ceiling (`BFT_B.md:3058`); flux-disc radius (`FLOW.md:1927`); mode amplitude (`FLOW.md:771`); loop orientation (`../ym4d-existence/EXISTENCE.md:2205`); already distinguished gas activity (`HW.md:1444`) | CONFIRMED: six witnessed roles, five bare-glyph roles plus one superscripted role |
| C_1 | Fourteen witnessed roles listed immediately below, of which SF's is already distinguished | CONFIRMED: ≥13, even excluding SF's corrected superscript |
| c_1 | Eleven witnessed roles listed immediately below | CONFIRMED: ≥11; advertised pair ratio REFUTED by F5 |
| κ | Constraint/coupling parameter (`PROOF.md:3123`, examples 1 and 1/4); polymer decay (`PROOF.md:2114,2122`); imported large-field parameter (`PROOF.md:1350`); group-valued gauge ratio (`BFT_B.md:2678`); constant Lie-algebra-valued gauge function (`BFT_B.md:4468–4469`) | CONFIRMED: ≥5 roles |

C_1 witnesses (matching the audit's numbering):

1. CE prefactor `2κ_0B`, `PROOF.md:2118,2485`.
2. `L^2+4cA_L`, `PROOF.md:4034`.
3. Localisation constant `C(R_0)`, `PROOF.md:2001`.
4. Covariance operator `Õ_1(V,W)^{-1}−(1−Π_V)`, `PROOF.md:6489`.
5. SUP-price constant, `SQ.md:190`.
6. `(9/8)·5⁴·49√6·L⁴`, `SQ.md:1587`.
7. Energy-inequality (★) prefactor, `SQ.md:1487` (the audit's cited 1485 is not the displayed inequality).
8. Green-function first-difference constant, `GREENT.md:288`.
9. Critical-map derivative prefactor, `BFT_B.md:228`.
10. Residual estimate `5κ̂/(L^{1−α}−1)`, `BFT_B.md:2632`.
11. LR-pot constant 775, `BFT_A.md:1123`.
12. `C_SPD`, `BFT_A.md:1554`.
13. Quartic-band coefficient renamed `C_1^Q`, `SF.md:1122–1124`.
14. Three-element set `C_1={ζ_1−1,ζ_1,ζ_1+1}`, `HW.md:1918`.

c_1 witnesses: KN ratio (`PLD.md:42`, `EXISTENCE.md:1771`); fixed PG coefficient (`PROOF.md:3681`); BL-3 shift (`BFT_A.md:500`); history exponent `c_LI+c_f` (`HW.md:1194`); coarse-link label (`RLARGE.md:967`); BB-W coefficient 1 (`BFT_B.md:986`); angular function (`FLOW.md:4133`); transverse coefficient (`FLOW.md:4770`); rectangle weight −1/12 (`PROOF.md:1425`); root-tree child multiplicity (`PROOF.md:2155`); CEM/Gaussian normalisation (`PLD.md:2586,2764`). The value of the last Gaussian approximation is not independently certified here.

The κ comparison is real but must retain its scopes: the file **uses** coupling values 1 and 1/4; it does not define a universal coupling bound κ≤1. The exact distinct decay condition is κ>3+48 log(12800), conventionally rounded to “about 457”, not an exact integer threshold. Also `SYMBOLS.md:741` calls μ(c_X) a “scalar”; `BFT_B.md:4328,4468–4469` defines μ as a Lie-algebra-valued gauge function, so that type description is REFUTED. It is still a distinct fifth object.

No upper/exhaustive count is established by this review. In particular `PROOF.md:1350` also quantifies an imported ε_1 alongside Balaban's constants; its identification with any of the six listed roles is NOT-VERIFIED from the restricted excerpt. The file-level “#1 only” classification for PROOF should not silently absorb that binder. This candidate is outside the preselected 40-site sample and was not added to its denominator.

### F10 — REFUTED: candidate-family scanning supports lane-wide completeness or its “honest zeros” as a coverage certificate

Targets: `SYMBOLS.md:17–22,43–44,632–636,761–783,795–796,807–813`. The method starts with a finite candidate-glyph list, greps defining forms, and manually checks uses. The sole supplied script performs six arithmetic checks; it enumerates no symbols, inventories no definitions, parses no binder scopes, and checks no rename coverage. There is no supplied inventory proving that the candidate list covers the lane.

The method can find additional collisions **if the glyph is nominated**. It did more than the original four families (C_3 is an additional manually selected family), so “it only searched the four it was told about” would itself overstate the evidence. But neither its pre-stated list nor the script forces discovery of unlisted families. C_♭ and q below are explicit defining-form counterexamples to any claim that this search achieved general coverage.

| Prompt's omitted family | Source-level spot check | Review verdict and scope |
|---|---|---|
| c_RS | Greedy separation `5⁴=625`, `RLARGE.md:1021`; joint-route factor `81`, `HIST.md:510–511` | CONFIRMED: different route-specific constants; active/superseded status must be recorded, not inferred from equal names |
| n_♯ | Fixed `floor(4/(a_♯β_-))`, `RLARGE.md:1024`; existential cutoff `n_♯≥max{n_*^J,n_H}`, `RLARGE.md:187`, and `n_H=floor((4+c_B)/(aβ_-))`, `RLARGE.md:588` | CONFIRMED: different quantified roles; replacing the free current cutoff by the historical equality is unjustified |
| q | Contraction factor `L^−3+C_qτ`, `SQ.md:1097`; integrability exponent `q:=8`, `SQ.md:1621` | CONFIRMED: two explicit, same-file definitions, absent from the family inventory |
| θ | Plaquette norm in `SQ.md:1623`; Chernoff tilt in `PLD.md:1437`; localisation error in `PROOF.md:6555` | CONFIRMED: multiple roles. The prompt's literal “none are in the audit” needs qualification: bare θ **is explicitly OPEN-NOT-SWEPT** at `SYMBOLS.md:780–783,811–812` |
| α | Hölder exponent, `BFT_B.md:2019`; root `α=e_i−e_j`, `FLOW.md:2112` | CONFIRMED: scalar exponent versus root label |
| M | CE cube side, `SF.md:630`; operator `(Ad_{e^z}−1)/ρ_j`, `BFT_B.md:1796` | CONFIRMED: scale versus operator |
| Q_str | Straight linear average, `LINEAR_PACKAGE.md:71`; nonlinear straight-root residual in `BFT_B.md:4330`; explicitly background-transported maps `Q_{str,l}^Z`, `BFT_B.md:4331` | CONFIRMED: distinct maps/versions requiring domain and background tags. NOT-VERIFIED: an unsafe bare-glyph substitution between them; the Z version is already distinguished |
| C_♭ | `L²+1+(12+3L)A_d` in `HIST.md:301` (199 at d=4,L=3); `4S_♭n_1/r_♭`, an analytic Hessian Lipschitz bound, `PROOF.md:5887` | CONFIRMED: explicit distinct formulas, with an actual cross-file quoting hazard (`SF.md:2195` consumes the analytic one) |

The omission of these families does not logically refute the singleton status of a_RS or τ_♭. Their displayed defining formulas were found at `RLARGE.md:1020` and `SQ.md:318–319`; exhaustive singleton claims remain **NOT-VERIFIED**. The “one defining form” for t_pr (`SYMBOLS.md:768`) is overly narrow: `HW.md:178–186` gives the same formal CLS-min cutoff role two suppliers, `53τ_♭` and `2`, depending on the route. This is not automatically two unrelated objects, but the route parameter is essential. The method must distinguish parameterized roles, alternate bounds, superseded inputs, and actual collisions.

Finally, absence of a second defining form is not proof of uniform use: a cross-file imported object may appear without a local definition, two different domains may share the same formula, and a changed numerical parameter may preserve syntax. The audit acknowledges some of those limits but nevertheless calls roughly 1600 file-level assignments “provable”. That promotion is REFUTED as a method of certification.

### F3 addendum — CONFIRMED from the full constants: the unrounded cap is about 5.08764e−22/C_D⁴

To avoid using SQ's own correction as evidence, I rebuilt θ_SUP directly from `SQ.md:143–145,168,182–189`. At d=4,L=3,N=2,κ_-=1, the formulas give

- A_d=9, A_ax=12, p_L=11; B_1=3.011·9+10.
- K/C_D = 39121/500; K_top/C_D = 121855493/1500000.
- C_p=34√2; C_e=17072/5+(1331/5)√2.
- Put u=39121/500, v=121855493/1500000. Then E:=C_err/C_D² = 34√2(u²+v²)+4(17072/5+(1331/5)√2)(u²/6+3033u/8000).
- θ_SUP C_D²=1/(2E), and the full SUP cap coefficient is B_exact C_D⁴ = 1/[640·53²·(2E)²].

No floating arithmetic was used. The rational endpoints 14142135623730950488/10^19 and 14142135623730950489/10^19 bracket √2 because their squares bracket 2. All coefficients in E are positive; substitution and reciprocal monotonicity give the exact certified enclosures

`3.0242947278e−8 < θ_SUP C_D² < 3.0242947279e−8`,

`5.0876416211e−22 < B_exact C_D⁴ < 5.0876416212e−22`.

Thus **5.00623e−22 is correctly reproduced only from SQ's rounded 3e−8 input**; it is not the exact coefficient of the defining SUP formula. At five displayed significant figures the full-formula cap is **5.0876e−22/C_D⁴**. Neither cap is the actual value of a_bad unless the appropriate minimum branch binds. This addendum refines F3 without claiming a proof of SUP-price's analytic hypotheses.

### F11 — Check-by-check falsifiability and evidence limits

Targets: all of `checks/sy1_criteria.md`, all of the small `checks/sy1_symbols.py`, and its recorded `sy1_out.txt`. I inspected them but did not execute the original script, because its `math.sqrt(float(...))` at lines 118 and 121 violates this review's exact-arithmetic restriction. All numerical checks reported here were independently implemented with integers/Fraction only, without importing or executing that script.

| Gate | Can it reject, and what did this review establish? | Verdict |
|---|---|---|
| SY1-1, script 58–65 | Compares independently specified 3/4/5 with computed depths. Different c_1 or C_I can reject; varying ε alone cannot because η_KN/ε is constant. Exact neighboring-power certificates establish the advertised triple. | CONFIRMED for the named recurrence and inputs |
| SY1-2, 68–79 | ≥40 can distinguish this live numerical example from the claimed triple. “Any ≤10 ⇒ NO-DEFECT” also accepts the wrong 5/7/10 triple. | REFUTED as a two-sided defect decision; actual 66/90/122 arithmetic CONFIRMED |
| SY1-3, 82–91 | The e=2 control genuinely changes depths to 5/7/10 and fails ≥40. That proves sensitivity to ε, not validity of SY1-2's no-defect interpretation. | CONFIRMED control result; adequacy as validation of the verdict REFUTED |
| SY1-4, 94–105 | Both comparisons can vary in a full model, but the script excludes δ_0/A_d before testing; no possible value of the omitted δ_0 can make this script detect its effect. Full ratios at N=2 are max(e/2,e²/(1024δ_0)) and max(512/13,e/(13δ_0)). | REFUTED as an unconditional ordering certificate; CONDITIONAL when the deleted entry does not bind |
| SY1-5, 108–128 | For the explicit rounded k=33100000, C′=53, τ_R=2.75e−15, C_D²=40000000000/192973. Exact squaring brackets C_D between 455.283300 and 455.283302; at ten times τ_R, C_D≤150 and outside the registered tolerance. Both comparisons can reject. | CONFIRMED conditional arithmetic; NOT-VERIFIED as the actual minimum's binding transition with all other entries |
| SY1-6, 131–147 | Corrected/stale rounded coefficients have ratio 9; the corrected/displayed ratio exceeds 5; using the stale input instead falls inside the registered [1/2,2] interval. Thus it is not an unsatisfiable or tautological gate. It tests one rounded coefficient, not a_bad's active branch or the full SUP constants. | CONFIRMED rounded arithmetic; broader suppression conclusion REFUTED by F3 |

The check header's “Exact rational arithmetic only” is **REFUTED** by the floating square roots that enter the SY1-5 verdict, not merely its printing. This does not refute its present result: the independent squared-rational enclosure above verifies that result.

The final summary at script **150–153** also drops two conditions: the separate `t_rs_ill == (5,7,10)` check (line 91) is not included in its SY1-3 summary, and `ctrl5_fails` (line 122) is not included in its SY1-5 summary. A changed control can therefore print DISAGREES or CONTROL DID NOT FAIL while the final line still reports its favorable shorthand. There are no assertion/exit gates for these verdicts (the only explicit exception is the recurrence's 100000-iteration safeguard). Treat the output as a diagnostic report, not a fail-closed validation gate.

All script inputs are hard-coded. None of these six checks reads the mathematical source definitions; changing a lane formula would leave the recorded arithmetic unchanged. Manual source synchronization, semantic coverage and consumer-route verification are therefore necessary independent obligations. No supplied gate tests the purported lane-wide inventory or the rename tables.

### F12 — REFUTED: “landable as written”; scoped rename dispositions

Target: `SYMBOLS.md:1053`, “θ_0, ε_1, ε_*, c_PG rename tables ... MECHANICAL — landable as written”, interpreted together with §13's corrections.

| Rename family | Disposition |
|---|---|
| θ_0 | ARGUED mechanically implementable on the inspected primary sites after matching context and refreshing locators. No misclassification in the sampled 28 sites. HW's associated numerical repair must preserve the upper-bound sign and full-minimum caveat; it also has an omitted repeated value at HW.md:826. |
| ε_1 | ARGUED for the inspected minority roles; the BFT_B matching lines agree with the table. NOT-VERIFIED as exhaustive lane-wide classification, including the imported PROOF binder. |
| ε_* | NOT-VERIFIED as a complete patch. The six BFT_B continuation uses match the identified object, but the full multi-file proposed rename was not exhaustively certified in this restricted review. A generic old string `ε_*` is not a unique source anchor when three versions occupy one file. |
| c_1 → c_PG | REFUTED: creates a fixed-vs-variable collision in both PROOF and LINEAR_PACKAGE (`LINEAR_PACKAGE.md:342` already defines c_PG=min(1,κ)/3500000), and misses ten observed line-sites even after its own correction. |
| η_1 | NOT-VERIFIED for a full patch. The audit correctly records ambiguity, but “one word from owner” is insufficient: current-vs-frozen route status and the ε-dependent depth must also be preserved. |
| C_1, κ, θ_w | NOT-VERIFIED as complete renames; the audit itself declines mechanical tables for these. |

A safe mechanical patch would need source-string-plus-scope anchors, a complete classified occurrence list, parameter/domain-qualified target names, and a residual-use check. These are missing in the submitted artifact. No source patch was made by this reviewer.

## Summary table

| Finding | Review verdict | Claim status / consequence |
|---|---|---|
| F1 RS depth correction | CONFIRMED | PROVEN arithmetic: 66/90/122 at the selected ε; physical multi-level transfer remains OPEN |
| F2 SY1-2 decision logic | REFUTED | GAP: its own control is a false negative for “defect” |
| F3 HW correction | CONFIRMED for the rounded cap; REFUTED as an a_bad value or guaranteed conservative change | CONDITIONAL on the active branch; full-formula cap about 5.08764e−22/C_D⁴ |
| F4 omitted δ_0 entry | REFUTED as unconditional | CONDITIONAL ratios/order; an exact positive counterexample gives RS/q=2 |
| F5 c_1 spread | REFUTED | PROVEN correction: 3500000/117≈29914.53, not 41000 |
| F6 40-site sample | CONFIRMED identities; REFUTED locator freshness | 0/40 identity errors; 2/40 locator errors; no population estimate |
| F7 c_PG rename | REFUTED | GAP: new parameter collision; at least 16 line-sites/18 tokens versus six proposed corrected sites |
| F8 live architectural consequence | REFUTED for current RLF-step v3 | The named a_RS/PLD supplier is on an explicitly replaced appendix route |
| F9 family counts | CONFIRMED lower bounds; NOT-VERIFIED exhaustive counts | θ_0≥4; ε_1≥6 including gas; C_1≥13; c_1≥11; κ≥5 |
| F10 coverage and honest-zero certificate | REFUTED as completeness; individual exhaustive zeros NOT-VERIFIED | Explicit omitted families and untracked route parameters |
| F11 complete gate coverage | CONFIRMED arithmetic only where scoped above | GAP: hard-coded sources, dropped control flags, float-based “exact” gate |
| F12 mechanical landing | REFUTED as written | Requires a new complete, parameter-aware patch |

**Single most dangerous unverified issue:** the positive suppression rate a_bad actually available on the current route, after all threshold minima and its conditional hypotheses are imposed. Neither the SY1 script nor this bounded review establishes it; substituting the much larger SUP upper cap for that rate would invalidate every lower-suppression comparison built on the substitution.

Final string-based locator check (2026-10-28 22:31:09 UTC): concurrent edits moved `PROOF.md` again. The strings `c_PG := min(1, κ)/(3.5·10⁶)`, `c_1 := 1/(3.5·10⁶)`, and `CURV1_0 at θ_0` were freshly found at **2923, 3683, and 6556**, respectively. Earlier source numbers and the sample table retain their as-inspected meaning; no uniform offset was inferred or applied. This additional drift does not change the sample score or the semantic findings.

## Stdout summary

CONFIRMED: RS depths 66/90/122 at ε=6.7e−40; requested collision-count lower bounds; 40/40 sampled object identities. REFUTED: two-sided SY1-2 verdict, unconditional SY1-4 ordering, cap-as-rate inference, c_1 ratio, active-route inference, completeness, and mechanical landing.

Numerical corrections: 3/4/5 → 66/90/122 for RS at the named ε; HW's 5e−23/C_D⁴ → rounded-input cap 5.00623e−22/C_D⁴, or full-formula cap in (5.0876416211,5.0876416212)e−22/C_D⁴; 41000 → 3500000/117≈29914.53; four original/six corrected PG rename line-sites → at least 16 line-sites/18 tokens. The quoted RS/q=3.35e−40 and KN/q=512/13 require the omitted minimum entry not to bind; full ratios are the maxima in F11, and RS/q can equal 2. The two stale sampled PROOF locators are 6502 (erratum 6527) → 6554, and 3629 (erratum 3654) → 3681, with strings controlling over line numbers (final recheck: 6556 and 3683).

NOT-VERIFIED: exhaustive lane coverage and the actual positive a_bad after every minimum and hypothesis. The latter is the most dangerous unresolved item.
