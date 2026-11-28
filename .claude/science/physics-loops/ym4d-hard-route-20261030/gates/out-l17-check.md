Codex (gpt-6-astra); checkout `8754e2c957b3fc3554fdf6b7de2041ba7f1df40e`; research-text check, not an audit; no status granted.

# Pre-send check of `out-l17.md`

Line references to OUT and WU mean `library/out-l17.md` and `library/wu-l17.md` at this checkout. SA and CA-I/II/III mean the source files at `31a47c543775`. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Tadeusz Balaban for the published constructions and estimates used by both texts.

The requested prior digest does not exist at this checkout. The registry's original curvature-only L17 is open and owned by `l17` (`library/open-registry.md:18`); this check does not attack it. The gap-order write-up belongs to `wu-l17` (registry:866), and the Stage-7 repair is already recorded (registry:874). FINISH:449 assigns this outward-package check, a distinct task. No proof lane, numerical verification, public post, or source edit was performed.

## 1. Faithfulness to the working note

**The transcribed mathematical core is faithful, conditional on its named inputs.** OUT:40–59 matches WU:50–79. OUT:67–111 matches WU:85–155, including the repaired matrix norms and all six proof steps. OUT:115–141 matches WU:159–201. The Taylor remainder coefficient 6, `C_3=2L^2`, `K^sharp=2 max(K,1)`, `D`, `c_*`, auxiliary radii, budget, and Stage-7 ceilings are preserved. No algebraic omission was found in those deductions. This does not certify a new proof of the external input bounds.

In particular, the three Taylor remainders each cost at most `2H t^2/r^2`, giving 6 (OUT:67–69); the three real-point bounds and that remainder give `K=3C_R+6H/r^2`, with `K^sharp` providing strict slack (OUT:99–109). If `mu<=1`, the two-power bound implies the one-power bound because `mu^2<=mu` (OUT:115–119). In the seed argument, `D c_*<=1/(16K^sharp)`, so the plaquette and true-current bounds fit strictly; the auxiliary pair consumes at most `alpha_0/2`, and (3.4) puts both auxiliary radii below their individual ceilings (OUT:123–133). Thus the numerical factors used in these deductions are consistent, including at equality in the non-strict target ceilings. These are analytic checks, not computational discharges.

The differences are these; renumbering and sentence compression are grouped rather than counted as defects.

| OUT | WU | Difference and consequence |
|---|---|---|
| 8, 178, 240 | 8, 266–281, 301 | Expanded model/check history; internal file and check locators are removed. OUT:178 says Codex wrote every derivation in its last column, though the last two rows are uses of Sussman–Alpoge proofs. OUT:240 compresses away the distinction between checked component texts and the repaired working note. Keep that distinction in the outward provenance. |
| 20, 187 | 30, 291, 301 | Replaces the internal target T0 by their Theorem 0. Appropriate for an outward note; those are not identical targets. |
| 30–34 | 34, 40–44, 272, 292 | Moves the outline comparison forward and adds a list headed “New here.” The budget, mechanism and conditional seed lemma are already theirs. WU:292 more carefully calls the remaining work implementation and compatibility/domain repairs. The final sentence “So the budget must carry the square” is inherited from WU:42; it is justified only for using this quadratic estimate, not as a necessity theorem about (1.17). |
| 40, 85–109 | 50, 119–153 | Removes internal names F0 and I1–I7. Renames the orbit constant `B_1` to `B_o`, and the three-point constant `C_1` to `C_R`, consistently. This usefully avoids collisions with the account's letters. |
| 54 | 73 | “Complete stencils” replaces the explicit “stencils/carriers, including the outward rows.” OUT:46 states the fuller convention only for (3.1). Repeat it for Lemma 3 so its statement keeps WU's read-set hypothesis. |
| 156, 205–217 | 205–234 | Moves and compresses the search inventory into Appendix B. The recorded ranges and substantive supplier exclusions remain. Descriptions of some symbol-only matches are shortened; these are not new mathematical suppliers. |
| 160–164 | 238–262 | Preserves the partial order and both repairs; renames `R_D2` to `R_D`. Drops WU:254's explicit exclusion of separately assumed uniform local-background operator bounds, and WU:262's optional running-radius alternative. The latter is not needed; the former is useful scope information. |
| 170–178, 189–201 | 273–281 | **Adds Appendix A**, which is absent from WU. WU cites exact internal derivations and checks; OUT replaces them by compressed sketches without usable links to those derivations. In particular the Euler-equation/flat-inverse step at OUT:201 is asserted rather than displayed. This is a change in the evidence offered, not a verbatim distillation. |
| 182–187 | 285–292 | Preserves the original-form, determining-set, minimality-identification and other-input limits. Adds an SU(2)-only checked-input limit (OUT:184), which WU did not state. Drops WU:288's explicit level-0 seam record. The SU(2) restriction must also qualify Proposition 1 and the issue's displayed claim. |
| 221–242 | no counterpart | Adds the issue body, including “needs the square,” “corrected bound,” “constants … explicit,” and “every proof step.” Those claims require their own check; they are not supplied merely by faithfulness to WU. The two `LINK` placeholders also remain unresolved (OUT:8,242). |

The statements and their elementary deductions survive the distillation. The claimed completeness and novelty of the outward package require the source checks below.

## 2. Quotes and source locators

**The substantive use-site descriptions are accurate, with the quotation and locator corrections below.** The two raw status quotations at OUT:23,25 and their excerpts at OUT:224–225 match CA-III:111326–111327 and CA-I:166588–166589 after joining line breaks. They do not say the account proves the complex inclusion. OUT correctly preserves that distinction.

The short quotation at OUT:20 is an edited rendering: the source has a parenthetical cross-reference, TeX citation commands and line breaks (CA-I:34068–34072). Its ellipsis and square brackets disclose those edits. OUT:223 similarly replaces a citation command by `[p. 263]`. Neither should be described as a byte-exact source quotation. The phrases “once …” (OUT:30; SA:9753), “for sufficiently small …” (OUT:164; SA:6587), “a sufficiently large positive integer” (OUT:162; CA-I:32848), “chosen upward” (OUT:162; CA-I:1511,2064), and “the axial-gauge minimiser” (OUT:185; CA-I:32896) agree with the rendered source. The quoted color-coordinate sentence at OUT:184 agrees with `a1-balaban.md:1753–1754` after joining lines.

Two corrections are needed. OUT:22's list heading starts at **CA-III:111315–111316**, not 111316–111317. The phrase **“(i)–(iii) imply (iv)”** (OUT:20,139,237) is a paraphrase, not an exact quotation. CA-II:4383 says “the estimates (i)--(iii) imply condition (iv).” Use that wording or remove quotation marks. Identify the closing list by its title and source label `ch:13`; its TeX heading at CA-III:111167 uses a counter rather than a literal chapter numeral.

The following table checks every citation group in §§1, 2, 6, 7 and 8 and the issue body. Repeated ranges are grouped. Broad downstream ranges are resolved to the lines that actually support the claim; this is not a fresh check of every unrelated proof inside those ranges.

| OUT location | Source checked | Finding |
|---|---|---|
| §1:16–18; §6:149; §8:173,178 | CA-I:32498–32623,32666–32670 | Correct transcription/paraphrase of the spaces, sufficient condition, and distinct CMP 116 primes. The source attributes the complex application to the printed sentence; OUT must not turn the attribution into a proof. |
| §1:20; §6:147; issue:223,235 | CA-I:34058–34218 | Correct. The linear budget is at 34062; complex (1.17) is an explicit hypothesis at 34068–34072; the one-power conversion and the geometry are at 34107–34189. The consequence keeps the other hypotheses. |
| §1:20; §6:150–152; issue:236 | CA-I:29522–29605,32412–32500,34241–34403,34718,34738–34741,56419–56439 | Correct dependency descriptions. Membership (e) uses small pairs at 34372–34375; other memberships have other suppliers. CA-I:32473–32491 uses true-pair configuration conditions, then replaces the independent current. Lemma 3 supplies this configuration route, not the other increment inputs. |
| §1:22–26; issue:224–225 | CA-I:32703–32706,166552–166589; CA-III:111164–111170,111315–111327 | Status accurately reported. Heading locator correction as above. |
| §2:30–32; issue:229 | SA:6571–6630,9746–9753,9899–9911 | Correct distinction between assumed ER7, conditional ER8 proof, and the sketched tower proof. The exact auxiliary radii already occur at 6618–6619. Additional tower passages are addressed in §3 below. |
| §6:148; §7:164; issue:235 | CA-I:34811–34830 | Correct: 34819 is the linear-budget entry, and 34827 chooses ceilings after `(L,B^(109),M)`. Replace the complete hypothesis/budget package, including the individual ceilings, not just its one displayed inequality. |
| §6:153; issue:237 | CA-II:4333–4398 | Correct target. The proof takes `(alpha_0',alpha_1')` equal to the target radii at 4378 and 4384. The sufficient condition requires smaller auxiliary radii; it does not justify this application at equal radii. Lemma 3 supplies an alternative argument. This identifies a failed inference, not a counterexample to the lemma. |
| §6:154; §5:139–141; issue:236 | CA-II:4599–4727; within 94811–97192:94811–94865,96280–96304,96404–96468,97064–97075; CA-III:90585–90624 | Correct. `c_T` cancels from `mathfrak t_j`, not from `C_beta`, `mathfrak e_Q`, `C_mathfrak e`, or `C_Pi`. These formulas retain inverse powers of `c_T`. The box extension and nesting remain additional hypotheses (96280–96291). Narrow the 2,382-line citation to these actual use sites. |
| §7:160–162; issue:238 | CA-I:1498–1514,1614–1629,1667–1669,2063–2070,4434–4437,13411–13420,32834–32936 | Correct partial order and Stage-5 compatibility arithmetic. The rule-1 gap is **strictly greater than** `R_1 mathfrak M L^q` (32877); OUT's “has gap” means a lower bound, not equality. Rule 2 has the stated lower bound at 32882. The displayed collar bound also assumes `L,R_1 >= 4d` (32925); preserve these earlier floors. |
| §7:164 | SA:6586–6594; CA-I:1614–1629,1667–1669,34827–34828 | Correct: sufficiently small target radii and downward choices already occur. The explicit Stage-7 inequalities implement that condition. No absolute relation `alpha_1^2 <= c alpha_0` is needed. |
| §8:170 | CA-I:24239–24269,32603–32606,166568 | Correct as a comparison of the cited statements: locality and the printed curvature-of-averages assertion do not themselves state the uniform raw increment bound of OUT:85. The outline has much more of its mechanism at SA:11510–11597. |
| §8:171 | CA-II:85845–85886; CA-III:35577–35624; CA-I:166573 | Correct about these named statements. The analyticity theorem displays first derivatives of the potential, not the uniform continued-current bound used here. The second-variation/response proposition is explicitly printed without proof. This is not evidence that every possible current statement in the account is absent. |
| §8:172 | CA-I:35144–35200,166573 | Correct published-input locator. The minimal orbit and regularity are cited; OUT:185 correctly retains the minimality identification as a cited clause. |
| §8:174 | CA-I:166571–166572; CA-II:54464–54517 | Correct citations for the propagator input. The account's statement is for regular backgrounds; its flat specialization is an input to the repository derivation. The outward note does not itself rebuild that package. |
| §8:175–176 | CA-I:32834–32936,33276–33322,10306–10405 | Correct. The unit formulas actually used are at 33314–33321, inside the theorem beginning at 33276. The current remainder gives `c_F=c_F(d,N)` and the required quadratic bound at `U_0=1`, `ell=1`, `mathsf c=0`. |
| issue:240 | SA:9607–9625 | Correct default convention. The outline expressly omits inward bonds in Theorem 5. The SU(2)-only checked-input restriction is repository provenance, not a claim that Balaban's printed results only concern SU(2). |

The unbounded quotient argument at OUT:34,227 is a failure of a particular estimate, not proof that a square term is necessary. Their outline already explains the scale loss (SA:9911), and their account records the potential-sized limitation at CA-I:15942–15951 and 155492–155507. Calling this a new defect would be unfair.

Appendix A also needs a locator split: OUT:191's range SA:11507–11640 locates PX141–PX154, not QC1–QC7. The latter occur in the earlier block-chart construction (see §3). This is outside the requested minimum sections but matters to the added proof sketch.

## 3. What their texts already contain

The classifications below concern the mathematical statements, not whether their location or notation matches OUT. “Proved there” retains the source's hypotheses. “Not there” means that the specific assembly was not found in the indexed passages and their cited suppliers; it is not a claim of mathematical originality. The already covered pieces should not be developed again as new research.

| Piece in OUT | Outline | Complete account | Assessment of the contribution |
|---|---|---|---|
| Proposition 1, including uniformity in depth and the quadratic potential term | **Sketched there:** Theorem 5(a), SA:9746–9753, states this tower estimate. Mechanism 8, SA:9899–9911, gives the three-real-point/Taylor argument, curl reduction and scale arithmetic. SA:15882–15919 repeats the argument for hereditary substitution room. **Assumed there:** ER7, SA:6571–6584, explicitly takes the same uniform holomorphic estimate as input. | **Assumed there** for the needed general complex application: CA-I:34068–34072. Real regularity is cited at CA-I:35144–35200. Some complex memberships are **proved conditionally as special cases**, using separate nesting/representative hypotheses: CA-I:155388–155426 and 156008–156033. These do not prove Proposition 1 on its stated whole domain. | An elaboration of their existing mechanism, conditional on the uniform averaging and continued-current inputs. The coefficient 6 and the displayed `K^sharp` make constants traceable; the estimate and its proof idea are theirs. |
| Corollary 2's budget | **Sketched there in exactly this form:** SA:9753 has `K^sharp(alpha_0'+(alpha_1')^2) <= alpha_0`, `alpha_1' <= alpha_1`, and the one-power unit change. SA:15917–15919 again imposes the quadratic tower budget. | The printed small-pairs proposition instead has the linear budget, CA-I:34062, with complex (1.17) assumed. Its one-power conversion is supplied at CA-I:34107–34189. The quadratic replacement is **not there** in that proposition or its ceiling corollary, CA-I:34811–34830. | Useful synchronization of the account with the outline, not a new budget. The proof of this implication is elementary once Proposition 1 is available. |
| Lemma 3 and its auxiliary radii | **Proved there, conditional on ER7:** ER8 and its proof, SA:6586–6630. It uses a physical `C^1` ball, an independent current, the trivial real configuration, and all hereditary clauses. The exact choices `epsilon_0=a_0/(4K_T)` and `epsilon_1=min(a_1/2,sqrt(a_0/(4K_T)))` are at SA:6615–6627. | The true-pair argument at CA-I:29522–29605 and the polydisc argument at CA-II:4333–4398 assert the corresponding conclusions using the inclusion supplier. Neither passage supplies the reduced-radius argument replacing that invocation. Thus the conclusions are already there; the needed justification at these uses is **assumed there**. | The conditional seed lemma and radii are redundant as new results. The explicit `D,c_*`, true-current remainder, complete-carrier check and dictionary to the account are useful implementation details. |
| The choice of `c_T` in OUT:139 | The general near-zero radius choice is **proved there conditionally**, SA:6615–6629; this particular account-wide minimum is **not there**. | Three of its four entries and use of a common `c_T` are already in CA-I:29522–29605; the polydisc uses that same constant at CA-II:4333–4398. The extra ceiling `c_T <= c_*`, and its assembly with both arguments, are **not there**. | A useful additional ceiling and dependency record. It is not a new extraction radius mechanism. The inverse-power costs retained at CA-II:4619–4727,96404–96468 and CA-III:90585–90624 must travel with it. |
| Replacement of CA-II:4381–4384 | The sufficient replacement argument is **proved there conditionally** in ER8, SA:6586–6630. | The proposed replacement is **not there** at this use site. CA-II:4378,4384 takes the simple-condition radii equal to the target radii. The small-pairs budget does not permit that invocation. | The strongest concrete contribution: replace this inference by the already available reduced-radius proof, with checked account notation and constants. It repairs an argument, not a false conclusion or a counterexample. |
| Gap order: choose `M_1` large enough that the required `R_1` still satisfies `R_1 <= M_1/mathfrak M` | **Sketched there:** SA:9916 chooses decay/localization first and the gap much larger than the localization length, with a quantitative lower rate, before later size and field-strength choices. | Stage 5 allows an upward `M_1` choice (CA-I:1498–1514,2063–2070); the rule requires the upper bound on `R_1` (32846–32850). The explicit interval construction using `R_req` is **not there**. | A useful compatibility witness for the account's two requirements. It does not introduce a new scale-order principle. Its supplier lengths still need an exact definition or link. |
| Stage-7 target-radius ceilings | Smallness of target radii is explicit in ER8, SA:6587. The auxiliary-radius arithmetic is **proved there conditionally**, SA:6615–6627. The exact inequalities in OUT:53 are **not there** in its notation. | Downward radius choices after the earlier constants are prescribed at CA-I:1614–1629,1667–1669,34827–34828. The two extra inequalities coupling targets to Proposition 1's individual ceilings are **not there** in these passages. | Explicit bookkeeping for an already required smallness choice. They ensure `alpha_0' <= bar alpha_0'` and `alpha_1' <= bar alpha_1'`; they are not a new restriction such as `alpha_1^2 <= c alpha_0` on the target pair. |

The outline search was not limited to Theorem 5's statement. The relevant chain includes the input disclaimer (SA:6456–6468); ER7–ER11 and their proof/continuation qualifications (6571–6660); the two rules, tower domain and torus floors (9646–9658); all parts of Theorem 5 (9746–9774); its proof plan (9795); mechanism 8 (9899–9911); the constants order (9916); and the second tower argument (15882–15931). The class assertion at SA:10256–10262 uses that tower input, and the substitution discussion at 12337–12366 invokes the same calculation with separate domain checks. None is a second, fully supplied proof of the uniform continued-current input on OUT's whole domain.

The finite-map material is substantial prior work, not just an outline promise. QC1–QC7 and their contraction proof are at **SA:7963–8053**; the relative average, linear derivative, Cauchy bounds, first-exit recurrence, node factors and depth-independent averaging bounds are at **SA:11510–11597**. These already cover much of OUT's Appendix A1. Its reference-field smallness is a hypothesis at SA:11552; the repository's curvature-to-local-gauge verification and matching of actual read sets are relevant additional checks. Appendix A2's continuation/current estimate remains a separate input. Neither the existence of a holomorphic map on an unspecified open neighborhood (CA-I:39087–39206) nor the one-step averaging calculation supplies a uniform datum radius and current bound by itself.

The account is also explicit about the limitation being discussed: CA-I:15942–15951 and 155492–155507 record a potential-sized complex estimate whose ratio to the requested curvature budget can be unbounded. CA-I:154825–154863 does not assert general complex (1.17). Its separately conditional complex membership results cannot be silently promoted to that general statement. Conversely, the note must not advertise this limitation as newly discovered: SA:9911 already explains the homogeneity issue and also mentions a gradient-assisted linear route. No necessity theorem for the quadratic budget has been established here.

## 4. Value to Sussman and Alpoge

Their README's Collaboration section (README.md:32–35 at `31a47c543775`) prioritizes checking, cleaning, restructuring and exposition, with mathematical understanding at a human pace and appropriate credit. My judgment as a prospective recipient is that the local account patch is worth adopting after the edits below. The present issue asks the reader to sort out too much provenance and apparent novelty before reaching that patch.

The useful pieces are the exact use-site map (OUT:145–154), the replacement of CA-II:4381–4384, the explicit current-remainder specialization and `c_*`, the shared `c_T` with its surviving inverse-power costs (OUT:123–141), and the compatibility interval for the two gap requirements (OUT:160–164). The explicit Taylor coefficient and norm repairs also make an existing argument easier to check. Their value is highest when every input has a direct locator and the conclusion is visibly conditional on those inputs.

The budget and auxiliary-radius trick are redundant as discoveries: they are already at SA:9753 and 6615–6627. Much of Appendix A1 repeats SA:7963–8053,11510–11597. These repetitions can serve exposition if credited as such. The account's statement of the complex-(1.17) limitation is already quite candid (CA-I:154825–154863,166588–166589; CA-III:111326–111327). Leading with multiple status quotations adds little to an actionable patch. The model genealogy and the full search inventory are useful provenance in a linked note, but mostly noise in the issue itself. The internal gate also says that some parametrix estimates were followed as sketches rather than rederived constant by constant (`gates/a1-balaban-gate.md:158`); a claim that the package displays every proof step should not conceal that boundary.

The issue body is about 500 words. That is a reasonable upper length for a technical issue, but its repetition and six-part contribution list make it longer than necessary for this request. It is substantially fair in acknowledging their outline and the remaining original-form problem. It is **not yet free of overclaiming**: the title's “needs,” the “corrected bound” language (OUT:221,229), “New here” in the linked note (OUT:32), and the input-completeness language (OUT:178,240) need qualification. No counterexample establishes necessity; several advertised pieces are already proved conditionally in their outline.

**The single highest-value change:** lead with one patch to CA-II:4381–4384, explicitly credited to their ER8 argument, and link the conditional tower/input elaboration as supporting material. This lets them assess a concrete replacement without deciding a broad novelty claim. A suitable issue text is written out in edit 8 below.

## 5. Verdict and required edits

**SEND AFTER EDITS.** The algebraic core can support a useful, narrowly framed contribution. The present text is not ready to send because its novelty framing, input completeness, front-loaded scope and unresolved links do not yet match that contribution. No post has been made, and `library/out-l17.md` has not been changed. The following eight grouped edits are the complete requested edit list; they do not ask for a fresh attack on the original L17.

1. **Replace the novelty and necessity wording (OUT:32, final sentence of 34).** Use:

   > This note implements the outline's Theorem 5(a) and mechanism 8 in the complete account's notation. The quadratic budget is already stated at SA 9753, and the unit-base inclusion with these exact auxiliary radii is proved conditional on ER7 at SA 6586–6630. The additions here are explicit constants, the current-remainder specialization, the consumer dictionary, and compatibility checks for the choices of gap and target radii. Proposition 1 remains conditional on the input estimates listed in §8; Appendix A summarizes their derivations.

   Replace the necessity sentence by:

   > The quadratic budget is sufficient for this argument. Failure of the direct linear estimate does not refute the printed curvature-only claim or prove that a quadratic term is necessary in every proof.

   Describe the bound at OUT:229 as “the outline's quadratic tower bound,” rather than “the corrected bound.” Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, in the surrounding provenance.

2. **Put scope and inputs before Proposition 1; restore Lemma 3's full read sets (OUT:38–40,54).** Insert:

   > The supplied derivations are checked here for SU(2), with the default convention that omits inward bonds. The notation retains N to display matrix-norm dependence; no checked extension of the input package to general SU(N) is claimed. All statements inherit the account's tower, collar and admissible-torus hypotheses, including the earlier L and R_1 floors. Proposition 1 is an implication from the uniform averaging, continued-current, real critical-orbit, real-average-curvature and flat estimates specified in §8. The identification with the published minimal configuration remains the cited identification described in §9.

   At OUT:54 replace “read on the complete stencils” by:

   > read on the complete stencils and carriers of every difference, current and average, including outward rows.

   This preserves OUT:184–185, WU:73 and the inherited floors at CA-I:32925 and SA:9658, rather than hiding them after the statement.

3. **Restore a reviewable input trail and label Appendix A honestly (OUT:170–178,189–201).** Change its heading to “Appendix A. Summaries of the two uniform input estimates.” Add this paragraph before A.1:

   > This appendix summarizes the input derivations; it is not a standalone derivation of the flat inverse or every contraction estimate. For the averaging input see `b109.md`, P15, (72), (74)–(77), and `a1-balaban.md`, §§3.5, 7.6, (7.14). For the continued-current input see `a1-balaban.md`, §9.1, (9.1)–(9.2), conditional on the flat package. The real-orbit and real-average inputs are at its §8, (8.2), and §7.1, (3.6), respectively. The flat package is `flat-port.md`, §§2, 4–9. The geometry, unit-change and current-remainder inputs are the cited complete-account results. The proof in §§4–5 uses these estimates with their stated domains and uniformity; it does not discharge them anew.

   Turn each file/section reference into a usable link in the outward copy. These are the suppliers already listed at WU:273–279; restoring them introduces no new supplier. Replace OUT:178's blanket authorship sentence by:

   > The repository derivations and their checks are identified separately from the complete-account results used as cited inputs. Model checks retain every named hypothesis and are not independent certification of those inputs.

   Immediately before “Subtract the Euler equation” at OUT:201 insert the omitted D3 step:

   > The holomorphically extended constrained Euler residual is holomorphic in the datum B and vanishes for real B, where the representative is critical. The identity theorem on the connected datum ball therefore gives the same equation for complex B.

   This is the repair already specified at `gates/a1-balaban-gate.md:136`; it explains the complex equation's use, while the subsequent uniform second-order estimate remains part of the linked input derivation.

4. **Make the gap requirement an exact supplier condition (OUT:162).** Replace the informal identification of `R_D` by:

   > Let R_D be a fixed L-power satisfying all four separation requirements of the linked gap-order calculation: the summability gap, the auxiliary-parametrix collar plus its stencil, the localization/reset collar, and twice the descent collar. These are fixed after L and the flat-package constants, before M_1 and the field radii; the parametrix side used in this calculation is not the later lattice parameter M. Let R_req be the least L-power at least R_D and every earlier floor for R_1. Choose M_1 at least mathfrak M R_req, then choose an L-power R_1 with R_req <= R_1 <= M_1/mathfrak M. This meets both the supplier's lower bound and the account's upper bound. It implements the order already described at SA 9916.

   Link the four-length calculation (`gates/a1-balaban-gate.md:128–134`, with its references into `a1-balaban.md`), or reproduce that short list with its suppliers. Keep the existing Stage-7 inequalities (OUT:53,164). Add:

   > These choices do not supply the separately assumed uniform local-background operator bounds used in other applications.

   That last sentence restores WU:254's scope limit. The interval argument is sufficient bookkeeping; it does not supply a new localization theorem.

5. **Correct the quotations and locators.** At OUT:22 use CA-III **111315–111316** for the list heading. At OUT:20,139,237 remove quotation marks around the shortened “(i)–(iii) imply (iv),” or replace it by the exact rendered phrase **“the estimates (i)–(iii) imply condition (iv)”** (CA-II:4383). At OUT:191 write:

   > the outline's contour mean (QC1)–(QC7), SA 7963–8053, and averaging recursion (PX141)–(PX154), SA 11507–11640.

   Keep ellipses and square brackets on the edited printed-sentence quotations. Identify the concluding source list by title and `ch:13`, avoiding an unsupported literal chapter numeral. Narrow the long CA-II:94811–97192 locator to **94857–94865, 96280–96304, 96404–96468, 97064–97075**, according to whether the sentence concerns order, box hypotheses, cancellation or the remaining constant.

6. **Update check provenance without inflating it (OUT:8,191,240).** Use a compact account such as:

   > Claude distilled this note from Codex's working derivation. The component checks and their repairs are listed with the suppliers; the repaired working note was not subsequently checked as a whole by Claude. Codex (gpt-6-astra) then checked this outward version line by line, with findings and required edits in `gates/out-l17-check.md`. This records a model review of a conditional argument, not a proof of Theorem 0 or a new check of all supplier derivations.

   Do not say that Codex authored every derivation in the table, or that every supplier proof step is displayed in this note. The explicit constants in §§4–5 are algebraic in the named supplier constants; they are not numerical evaluations of the flat or critical-orbit constants.

7. **Resolve the two `LINK` placeholders and expose the dependencies.** OUT:8 needs an actual link to the working derivation/check record; the issue needs an actual stable link to the corrected outward note, with the suppliers in edit 3 accessible from it. Use the final corrected version's permalink, not a permalink to the present unedited draft. No such corrected public artifact exists within this check, which is authorized to write only this report. This is an outstanding send condition, not a claim that any link has been published or tested.

8. **Replace the issue title and body (OUT:221–242) with the following shorter, focused version.** The bracketed final artifact reference is to be replaced by the real permalink required in edit 7.

   **Title:** Apply the outline's ER8 radius choice in the account's polydisc-containment proof

   **Body:**

   > I have a proposed local clarification of `5.2:lem-polydisc-containment`, based on your outline's ER8 argument. Credit for that argument and the quadratic tower mechanism belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of your text.
   >
   > At [CA-II 4378–4384](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L4378-L4384), the proof invokes the inclusion at auxiliary radii equal to the target radii. The budget in [small pairs](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L34058-L34072) does not justify that invocation. This concerns the inference, not a counterexample to the lemma.
   >
   > Your [ER8 proof](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L6586-L6630) already gives the replacement, conditional on ER7: use
   > `alpha_0' = alpha_0/(4K)`,
   > `alpha_1' = min(alpha_1/2, sqrt(alpha_0/(4K)))`.
   > These consume at most half the target curvature budget in [Theorem 5(a)](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L9746-L9753), provided the individual auxiliary-radius ceilings hold.
   >
   > [Corrected note and explicit input links] spells out the account notation, an explicit seed constant, the true-current specialization, and a common smaller `c_T` for the true-pair and polydisc uses. It tracks the inverse powers of `c_T` that remain in extraction constants and the choices needed before the final coupling ceiling. It also expands your tower mechanism with explicit constants, conditional on the listed uniform input estimates.
   >
   > The checked input derivations cover SU(2), default omitted-inward bonds and the stated admissible domains. The note does not establish the original curvature-only complex (1.17), the separate continuation/nesting hypotheses, or Theorem 0. Its authorship and model-review history are recorded in the linked note. The proposed change is the reduced-radius replacement at this use site.

This send recommendation is for the corrected, explicitly conditional package described above. No scientific status is assigned to the original L17, any input, or the construction.

Checked line by line by Codex (gpt-6-astra).
