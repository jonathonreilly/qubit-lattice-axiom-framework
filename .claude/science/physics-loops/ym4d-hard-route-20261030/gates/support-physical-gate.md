# Gate: support-physical, Sections 2–7 (queue row 97)
Provenance: OpenAI Codex (GPT-6; exact runtime model variant and effort not exposed; row requests xhigh), checkout `13e0982c193e76b0d45f9da722a89819695e0b05`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, no status granted.

This gate checks Claude's `library/support-physical.md` Sections 2–7 by hand for Package C rank 1, the physical-datum hypothesis (D-F) of floor screening. Credit for the outline's constructions and statements: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. `SA` line numbers refer to the requested `YM4_sketch_500.tex`, fetched once into `/tmp/sa_ym4.tex`. Balaban, CMP 119 (1988), is read in place from `~/ym4d-papers/cmp119.txt`; Proposition 2.4/CMP 122 remains a cited, conditional input. No numerical or computer-assisted inference is used.

| Source step | Verdict | Scope |
|---|---|---|
| §2 P(a), passed indicators | CORRECT-NO-ADVANCE | Extended history support |
| §2 P(b–c), births | ADVANCE | Retained physical rows, not later evaluations |
| §3 mixed loops | ADVANCE | Later seam births include A as well as T |
| §4 healed draws | ADVANCE | Bound \(2\varepsilon_s\) |
| §5 Proposition 2.4 restatement | CORRECT-NO-ADVANCE | Cited-pending input |
| §5 Proposition I | ADVANCE | Conditional on Proposition 2.4, R1 and H2 |
| §5 narrow-cut-off island at birth | ADVANCE | Local counterexample to an all-island envelope |
| §5 R1 necessary for later-floor (D-F) | WRONG | Later admitted history missing |
| §6 inherited raises and bare integrals | ADVANCE | Bound \(6L^6K R_i^2\varepsilon_i\), under H2 coverage/timing |
| §7 sufficient theorem | ADVANCE | H1–H4 and the stated stage readings remain premises |
| §7 ceiling and consumer substitution | CORRECT-NO-ADVANCE | No further input discharged |

**First failing step:** §5, source line 157's inference from a large island at birth to failure of (D-F). Lines 158–160 do not construct the required later history. The repair and the precise weaker result are in §5.2 below. **None fails in the conditional sufficient chain under R1.**

## 1. Scope and source boundary

The target is a bound on the physical label datum in the old core, not on every artificial localization lift at its geometric level. The row-94 gate separates these, and its lift counterexample does not refute this target. A birth certificate must survive on the full history support and must cover the actual mixed loops read by (D-F). The ordinary-step read sets are the specified CMP 119 convention. The source's references to raw I are not independently verified merely by repeating their line numbers; where the outline does not supply the needed statement, this gate identifies the additional premise.

Verdicts and hand derivations follow section by section.

## 2. Source Section 2: persistence and births

**P(a): CORRECT-NO-ADVANCE. P(b), P(c), and the birth inventory: ADVANCE for the history variables and determining sequence specified in the outline.**

Use the extended history space, retaining integration variables as well as the final datum. A passed factor is an indicator \(I_r(z_r)\). On the nonzero integrand locus, \(\prod_r I_r(z_r)\ne0\) forces every such factor to be one. This does not assert that the same indicator, re-evaluated on a later background, remains one. Integrating out \(z_r\) does not turn its old bound into a bound on a new variable. Thus the argument is legitimate precisely when the loop value itself is retained. “Support” here has the source's nonzero-integrand meaning; no strict indicator statement is claimed at every point of a topological support.

The actual variable operations give the needed persistence: an ordinary step sets \(V_t=\mathcal M(V_{t-1})\); a preparation retains that same delta constraint; a redraw changes only \(\mathfrak b_X\) (SA 17585, 17654, 22748–22749). Coordinate changes must be inverted when reading a physical bond. A common gauge transformation conjugates a loop product and preserves its norm. Hence a loop bound survives while all of its factors, including the finer bonds used by a substituted average, survive. One must not carry an eliminated constraint across a redraw.

SA 17415–17440 supplies the changes of determining sequence: healed and island decisions remove the lower layers throughout the component; a drop-out keeps the completed raises and their bare integrals. Tests, changes of coordinates and frame choices assign no additional physical values. These facts yield T/H/I/A as the exhaustive birth types; a final decision supersedes its own preparation. Quarantine and marks-wait (SA 17575, 17440) put a surviving older operation below the current bottom. The core itself is not unfolded by the current preparation. Nothing in this inventory proves regularity; it identifies where a certificate has to come from.

Dropping factors causes no extra support inference here: retain the original indicator in the extended history representation. Identifying a reorganized analytic expression with that representation still requires the outline's exactness identities; positivity alone would not prove that identification. This gate concerns the stated history kernels, not arbitrary analytic evaluation points.

## 3. Source Section 3: mixed loops

**ADVANCE, with the following harmless wording correction.** A later seam can be made by a preparation as well as by an ordinary step; replace “a later step, as case T” by “a later T or A birth.”

At a T birth, use the delta constraint separately on each fine-side row of the loop. Its substituted value is the same \(V_t(c)\) used on the coarse side, so the loop is exactly the ordinary level-\(t\) plaquette, up to common conjugation. At an H or I decision, all of the component is added to \(\Omega_t\); its outside collar was already in \(\Omega_t\). There is consequently no level-\(t\) fine/coarse interface through the newly completed component. At an A birth the same row identity holds if the full averaging rows are determining rows of the certified background; Section 6 below checks the needed coverage separately. Subsequent coarsening either preserves the old test value, removes the test, or creates a new T/A/H/I test. There is no factor accumulated with the age of an unchanged loop.

## 4. Source Section 4: healed draws

**Proposition H: ADVANCE. The bound is \(2\varepsilon_s\), without Proposition 2.4.**

Write the cell side as \(a=MR_s\xi_s\). Quiet evolution gives \(X'=H^{[10]}\) and \(\Omega_s^c\cap X'=H^{[8]}\) (SA 17575–17583). Since the prepared box meets the nonempty core in \(H\) and has side at most \(CM\xi_s<a/2\), it is contained in \(H^{[1]}\). For the second inclusion, take the hull of the old component in the current cell grid. The old component is boxed, so this hull is \(H\). If another old hull had its four-layer enlargement intersecting \(H^{[10]}\), the two ten-layer enlargements would touch. They would therefore belong to the same new component, contrary to the single-component, no-joining condition. Thus \(\widehat Y^{\sim4}\cap X'=H^{[4]}\). This argument uses the component condition, not just a diameter bound on an arbitrary subset.

For a cell \(C\subset H^{[4]}\), an incident test cube \(D\subset C\) lies in the healing decision region, since \(X'^{\sim-6}\supset H^{[4]}\). Its test passed on the **new** field. For a cell outside \(H^{[4]}\), the ordinary test was performed outside the omitted four-layer region and passed by quietness. CMP 119, pp. 264–265, (3.1)–(3.5), explicitly supplies that omitted region and the later eight-layer margin. Its cube read extends at most five test sides, with \(5M_2R_s\xi_s\le5a/L^2<a\). The cell is at least a full cell from \(H^{[3]}\), whereas the redraw bonds, including their exterior endpoints, lie inside \(H^{[3]}\) once \(R_s\) is large. Hence this particular read is unchanged by the redraw. This is stronger than merely saying its central plaquette is unchanged.

In either case a **single** passed cube background \(W\) bounds every bare plaquette in the four complete averaging rows by \(\varepsilon_sL^{-2s}\). Iterating centered blocks gives half-side \((L^s-1)/2\) in bare spacings; the union of the four endpoint blocks is within \(3\xi_s\) of the chosen corner. Thus the rows lie inside \(D^{\sim}\). CMP 119 (2.13) puts the tower's top member over its domain minus two \(M_1\)-cube layers; applied to \(D^{\sim4}\), this includes \(D^{\sim}\). Equations (1.2)–(1.4), (2.16)–(2.17) then give \(\mathcal M^sW=V_s\) on all four coarse bonds and the stated curvature test. Closure conventions at faces do not shrink this margin.

For completeness, the averaging estimate used here has a hand proof. In coordinate-tree gauge on the finite row rectangle, each bond closes a coordinate contour tiled by at most a fixed \(N_L\) elementary plaquettes. Telescoping their transported products bounds the bond's distance from one by \(N_La\), and its logarithm by \(2N_La\) for small \(a\). The one-step averaged plaquette has linear term \(L^{-4}\sum_z\sum_{r,u=0}^{L-1}(dA)_{\mu\nu}(z+r e_\mu+u e_\nu)\), where \(z\) ranges over the \(L^4\) block sites: internal endpoint terms cancel. All weights are nonnegative and their total is \(L^2\). The elementary plaquette logarithm differs from \(dA\) by \(O_L(a^2)\). Taylor's integral remainder on this fixed finite-dimensional ball therefore gives \(a_{n+1}\le L^2a_n+K_La_n^2\). Starting from \(a_0\le E L^{-2s}\), induction gives

\[
a_n\le E L^{2(n-s)}\exp\!\left({K_L\over L^2}\sum_{r<n}a_r\right)
\le2E L^{2(n-s)},
\]

because \(\sum_{r<n}2E L^{2(r-s)}\le2E/(L^2-1)\), and the two smallness conditions in (5.3) apply. Setting \(n=s,E=\varepsilon_s\) proves H. No fixed loss is iterated \(s\) times. The attempted counterexample of a large redraw in the inner box is rejected by the healing test itself; outside that box the quiet tests remain valid.

## 5. Source Section 5: islands and the cut-off reading

### 5.1 Proposition 2.4 and the island bound

**Proposition 2.4 restatement: CORRECT-NO-ADVANCE, cited-pending. Proposition I: ADVANCE as an implication under R1, Proposition 2.4, and the stated stage-domain reading H2.**

SA 17656 states a fixed-radius class, a unique critical gauge orbit and a bound \(C(M)\varepsilon\) on its curvature, provided the exterior curvature is below \(\varepsilon\) and \(C(M)\varepsilon\le a_\Lambda\). The sentence that its application has \(\varepsilon\le C\varepsilon_s\) is not an extra hypothesis of the proposition. Using \(\varepsilon=7L^2R_s^2\varepsilon_s\) is therefore a legitimate conditional application. The class's distance-one neighborhood, read in the stated lattice sup norm, contains every plaquette incident to a changed bond. Neither the contraction proof nor the constants of CMP 122 are discharged here.

Redo the three cases. Outside \(H^{[4]}\), the quiet cube read used in Section 4 still passes and is untouched, giving \(2\varepsilon_s\). For a plaquette in the inner region with no bond in \(\mathfrak b_Y\), all four coarse sites are outside the box. The box is a union of complete level-\(s\) blocks; the four averaging rows lie in the union of their endpoint blocks and thus miss the box. They remain at least five cells inside the outer boundary of \(Y\). Consequently the final prepared background has these exact averages and its passed, nonshell stage test bounds their full footprint. This is the substantive domain clause of H2; it is not supplied merely by the existence of a background.

Put \(j_0=s_\sharp+1\). The overlap factor obeys

\[
L_\flat^{2e}\le L^{2(s-j_0)}=R_{j_0}^2\le L^2R_s^2.
\]

The bare bound is at most \(3L^2R_s^2\varepsilon_sL^{-2s}\). The averaging induction above therefore gives \(6L^2R_s^2\varepsilon_s<\varepsilon\). Beyond \(Y\), the ordinary passed reads provide \(2\varepsilon_s\); the exterior collar lifts preserve these plaquette values or are flat. These are exactly the unchanged exterior data for Proposition 2.4, not the untested new bonds.

For a plaquette meeting \(\mathfrak b_Y\), write its four oriented factors for the centre and for the draw in the same gauge. Unitary multiplication and inversion preserve operator norm, so telescoping the four-factor product yields

\[
\|\partial V_s-1\|\le\|\partial V_\Lambda-1\|
 +\sum_{b\in\partial p'}\|V_s(b)-V_\Lambda(b)\|
 \le C(M)\varepsilon+4M_0\varepsilon_s.
\]

The last inequality follows from R1 and \(\|e^{iA}-1\|\le\|A\|\). Conjugation by a frame or a gauge leaves it unchanged. Thus the proposed
\(C_I=7L^2(C(M)+1)+4M_0\) covers all three cases. Strengthen the harmless ceiling to \(C(M)\varepsilon+4M_0\varepsilon_s<a_\Lambda\) when asserting that the entire supported draw lies in the existence class; the limit in Section 7 permits this. No long-time persistence or later-floor construction is needed for this sufficient bound.

### 5.2 Narrow cut-off: what the counterexample proves

**Draw, failed decision, and large island datum: ADVANCE, conditional on Proposition 2.4's existence class. Necessity of R1 for the later-floor statement (D-F): WRONG as a claimed proof.**

The local construction can be made exact. Start with the flat exterior and flat prepared-shell history described in `support-envelope.md` Section 16. Its creation is a pure gauge with one nonpivot bond deviation \(3\delta_b>2\delta_b\); all curvatures vanish, its average at the next level is one, and its later quiet, flat tests pass. The perturbation is in the core, so the preparatory shell fields and their fluctuation tests can be flat. The finite-dimensional strict inequalities give a positive incoming mass near this history, as in the row-94 gate. Zero Wilson action identifies the tree-gauged box centre as one.

Choose a boundary-crossing bond other than the single external tree bond. Set its draw to \(g=\exp(i\theta\sigma_3)\), all other draw bonds to one, and choose \(h=\|g-1\|\) strictly between \(a_\Lambda/2\) and \(a_\Lambda\) (the fixed small existence radius may be reduced below one). Each plaquette through that bond has curvature exactly \(h\); every other plaquette is flat. The narrow cut-off sees only internal bonds and passes. The tree constraint passes. This is inside the existence class and has positive finite Wilson weight. With a small exterior perturbation, the norm differs from \(h\) by at most the centre's plaquette norm, so the strict inequalities persist. Thus this is a relatively open set of draws, not a zero-measure gauge point. This conclusion uses the reference law on its defined class; it does not supply a total definition on any configurations outside that class.

Choose \(\varepsilon_s\) so small that \(2\varepsilon_s<h\). The incident ordinary cube test cannot pass: its full-row bound would give \(h\le2\varepsilon_s\). Its cube lies in the final decision domain. Earlier tests precede the redraw, so this is an island. Since
\(R_s^2\varepsilon_s\le L^2A_0\theta_s^{-1/2}(\log\theta_s)^{2r+\mathfrak p_0}\to0\), these island births violate any fixed \(CR_s^2\varepsilon_s\) envelope on **all island plaquettes**.

**D1 — the first failing step is source line 157, “so (D-F) fails,” with the missing step exposed at lines 158–160.** (D-F) is quantified only over tests whose bare supports meet the floor of a later operation. Immediately after the island decision, \(Y\subset\Omega_s\); the offending plaquette is not thereby a test in such a floor. Marks-wait is a restriction on a later containing class component **if one occurs**. It is not an existence theorem for that component on the support of this nonflat draw.

The geometric part of line 158 is valid conditionally. If the island survives to a quiet bottom \(m_b>s\), its hull is inside the eight-cell excluded region and hence in the floor. On a radius plateau one can set \(m=s+R+1\), \(m_b=s+1\), so quarantine and marks-wait allow that geometry. But every intervening test and exact averaging relation must also be satisfied. The earlier flat template has zero offending curvature; replacing its draw by this one changes later fields and their background-dependent tests. Continuity at each finite history gives an unspecified radius, not a radius exceeding the required violation scale. This is precisely the limitation already stated in `support-envelope.md` Section 18. Source line 160 explicitly leaves the full later history unconstructed.

**Repair, proved at the weaker scope:** replace the necessity claim by “R1 suffices; the narrow reading does not enforce a uniform \(CR_s^2\varepsilon_s\) bound on island data at birth.” Keep the later-floor necessity claim open. **Repair at the original scope, visible but unproved:** exhibit the above plateau continuation with the large plaquette still determining, all intervening ordinary and collar/rim outcomes specified, and positive mass through the later class admission. A quantitative response estimate could establish quietness outside the retained island, but invoking that estimate without verifying its hypotheses would merely add a new conditional input. No admitted later-floor counterexample has been proved here. This defect does not enter Propositions H, I or A, or the sufficient theorem under R1.

## 6. Source Section 6: inherited raises and bare integrals

**Proposition A: ADVANCE under the declared H2 stage-domain and pre-integration-test reading. The constant \(6L^6K\) is correct.** This is a conditional certificate for the actual rows, not a verification of the missing CMP 122a formation data.

**Recorded pass and exact identity.** Fix a surviving level-\(i\) row born at the \(q\)-th integration, \(i=t_b+q\). SA 17585 says the stage tests precede that integration; SA 17654 keeps the completed bare integrals on a drop-out. Read H2 as requiring the stated curvature test among those passed tests. If its background is denoted \(U^{(q)}\), its coarse determining constraints give \(\mathcal M^iU^{(q)}=V_i\). On the finer-side rows, the retained delta gives the identical value \(\mathcal M(V_{i-1})\). If the pre-integration background is instead denoted \(U^{(q-1)}\), the newly raised rows satisfy

\[
V_i=\mathcal M(V_{i-1})
   =\mathcal M(\mathcal M^{i-1}U^{(q-1)})
   =\mathcal M^iU^{(q-1)}.
\]

A row already stored at level \(i\) is handled by its existing constraint, not by the inaccurate literal assertion that every row is in level-\(i-1\) territory. Telescoping these exact row identities around the loop gives \(\partial V(\tau)=\partial(\mathcal M^iU')(p')\). No equality is inferred across a removed delta.

The scheduling qualification matters: a test which failed after the last integration is never a certificate. The previous-background alternative requires an actually recorded passed test on that previous background. At \(q=1\), merely naming \(U^{(0)}\) would not establish such a pass. Under the stipulated pre-integration reading it is the first passed test itself (with either index convention), so this edge case is covered. A convention that first raises a region and then tests its first background, with no passed predecessor, is **not** covered by this proof. Thus “both readings” is valid as the two stated pre-integration certificates, not as an assertion about arbitrary stage schedules.

**Whole footprint.** For a genuinely new row the inner boundary is \(Z''_i\), with a gap of at least \(M\xi_i\) to \(Z''_{i-1}\) in the compressed nest. In the earlier uncompressed part, the five-layer erosion of the quiet eight-layer box leaves \(H_i^{[3]}\); keeping two layers of clearance already suffices. At the first raise the corresponding inner set is the old core. The row footprint has radius at most \(3\xi_i\), so for \(M>4\) it misses the preceding inner set. It lies inside the component because every changed row was in the original excluded region, which has two outer cells of clearance. An actual level-\(i\) test has no endpoint in the higher member of the determining sequence; the aligned endpoint blocks cannot cross into a higher layer. Its footprint consequently uses the level-\(i\) region and at most the level-\(i-1\) shell. Existing level-\(i\) rows at an outer junction are included as just explained.

These geometric facts exclude the old core and the artificial outer lift. They do not by themselves say that an indicator reads the footprint. That final inclusion is exactly the H2 domain reading of SA 17624 used in the source: the shell test plus the nonshell test cover this entire footprint for the chosen \(U'\). The outline's summary and `support-envelope.md` Section 17 do not constitute an independent reconstruction of all CMP 122a test domains. Narrower domains would leave this proposition unproved.

**Arithmetic, redone.** In the attempt's window, frame values differ by at most \(O(R_t)\), whereas \(R_t=O((\log\theta_t)^r)=o(\theta_t)\). Increasing the ceiling makes their ratios lie between \(1/2\) and \(3/2\), and their logarithms comparable within two. Applying this directly to the one-step window ending at \(i\) gives
\(\varepsilon_{i-1}\le K\varepsilon_i\), \(K=2^{\mathfrak p_0+1}\); no \(K^2\) is needed. Upward power-of-\(L\) rounding gives \(R_{i-1}\le LR_i\). The unrounded ratio is eventually less than \(L\), so adjacent rounded radii differ by at most that factor.

The overlap bound \(L_\flat^{2(i'-j_0)_+}\le L^2R_{i'}^2\) gives bare curvature at most \(3L^2R_{i'}^2\varepsilon_{i'}L^{-2i'}\) on a tested level \(i'\). A nonshell test at stage scale \(j\) obeys the same bound with \(j\). For \(i'=i\) this is smaller than the proposed common bound. For \(i'=i-1\), or a predecessor test at \(j=i-1\),

\[
3L^2R_{i-1}^2\varepsilon_{i-1}L^{-2(i-1)}
\le3L^2\,(L^2R_i^2)\,(K\varepsilon_i)\,(L^2L^{-2i})
=3L^6K R_i^2\varepsilon_iL^{-2i}.
\]

Apply the averaging induction once with \(E=3L^6K R_i^2\varepsilon_i\). It yields exactly \(2E=6L^6K R_i^2\varepsilon_i\). This factor is paid once at the last birth, not once per earlier stage or mark.

**Persistence and cases.** On the surviving stratum \(Z''_{i+1}\setminus Z''_i\), further stages integrate outside \(Z''_{i+1}\), so these values are untouched. Bare integrals retain the equality on their extended support. Later operations either preserve the rows or give them a new birth certificate. An exclusion before the first stage adds no raised rows; an exclusion after all stages is covered by the same argument through \(q=N\). Stored collar functions are not determining datum. Nothing here uses a near-group-total hypothesis for inherited analytic arguments.

## 7. Source Section 7: assembly and ceiling

**The sufficient theorem under H1–H4 and the specified stage readings: ADVANCE. The ceiling and the consumer substitution: CORRECT-NO-ADVANCE.** There is no failing implication in this sufficient chain; its analytic and formation-data premises remain conditional.

Assign each actual loop its last T/H/I/A certificate, using the coarse-side identity at seams. T supplies the initial-strip constant \(C'_L\) or \(2\varepsilon_l\); H supplies \(2\varepsilon_l\); I and A supply the constants checked above. Since \(R_l\ge1\), the maximum

\[
C_F=\max\{C'_L,6L^6K,7L^2(C(M)+1)+4M_0\}
\]

covers all four. Persistence transfers a certified value, never a product of constants along the history. This proves the asserted physical-datum envelope for the specified history construction, conditional on H1–H4 including H2's exact coverage and timing. The failed necessity argument is not used.

All constants are chosen before \(\gamma\). Set \(d=2r+\mathfrak p_0\). For \(\theta\ge e^{2d}\), differentiation gives

\[
{d\over d\theta}[\theta^{-1/2}(\log\theta)^d]
=\theta^{-3/2}(\log\theta)^{d-1}(d-\tfrac12\log\theta)\le0.
\]

The function tends to zero: writing \(u=\log\theta\), the exponential series with any integer degree greater than \(d\) bounds \(u^d e^{-u/2}\to0\). Thus the supremum for \(\theta\ge\gamma^{-2}\) tends to zero, while the minimum radius tends to infinity. The pivot, footprint, averaging, and strengthened box-class ceilings can all be imposed at once. The largest averaging parameter is the A-case parameter, which also dominates those used for H and I.

For floor tests the row-94 geometric exclusion removes the current artificial collar; these are the physical tests just bounded. Lemma T then gives the consumer amplitude \(A_F=4L^2C_FR_m^2\varepsilon_m\), with \(C_F\) fixed before \(\gamma\). This is a conditional replacement of (D-F), not a discharge of Proposition 2.4, the unrebuilt stage domains, or the other floor-screening inputs.
