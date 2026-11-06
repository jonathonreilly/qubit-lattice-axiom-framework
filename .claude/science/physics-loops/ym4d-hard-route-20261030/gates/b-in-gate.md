# Check of the sealing construction, FINISH row 397

Provenance: Codex (gpt-6-astra); checkout `e23605e01474e766258f008c0d477b349fbfc09c`; research text, not an audit and no status grant.

## 1. Scope and sources

This is one check of all 271 lines of `library/b-in.md` (Claude, row 389). `I`, `II`, `III` and `SA` denote the supplied account and outline at upstream `31a47c543775`, under `/Users/jonreilly/ym4d-lead/sa`. Credit belongs to Sussman and Alpoge, with Claude and Codex as authors of their text, and to Balaban for the cited constructions.

`library/prior/b-in-gate.md` is absent. The earlier digest `library/prior/b-in.md`, `gates/ca-gate.md` §§4–5, `library/ca-claude.md` and `library/ca-f.md` were read first. The registry assigns CA-BIN to `b-in`; this requested check does not open another proof lane. The pinned seed, conditional collar algebra and existing layer calculation are reused with their recorded premises.

Balaban's original pages are unavailable within the permitted source directories. This check uses the quotations and arguments in `library/lit-balaban.md`, `library/b102.md`, its cited notes and the account. It does not claim a new comparison against the printed pages. File searches are navigation, not mathematical evidence from a run.

## 2. First check: the one-block reset

**ADVANCE for the local reset on its admitted local problem; REVISE its scope in lines 49–56.** The localisation is supported by `b102.md:2944–3025` and `a1-balaban.md:1204–1326`. The proof freezes the actual outer averages. The resulting field is critical for the local constraint problem. Its reduced datum has two bounds: a bound from local regularity on the artificial part, and the datum-test bound on the two central layers (H21.1). Splitting the lift gives H21.3. The nonlinear error is bounded by the square of the local regularity radius; H21.4 absorbs it. No estimate of the field outside that local problem enters these steps. Thus substituting local radii for the two global radii in this calculation is legitimate.

The precise retained proviso is necessary: use a two-layer cube of CMP 102 (144), with its enlarged cube, averaging contours, current stencils and auxiliary gauge collars inside the admitted region. I:35155–35163 states the two-layer containment; `b102.md:1840–1877` retains the auxiliary collar. A block at an interface may require the finer of the two scales. “Every block, with the concentric box specified in line 49” is not an unconditional consequence of this local proof. The block covering must supply these local problems and their read sets. The floor (M) provides room in separated interior zones; it does not supply missing boundary data.

Write the corrected input as follows:

> For every chosen reset patch \(P_y\), include all its stencil, averaging and gauge reads in \(N(y)\). Measure each output test at its incidence level, as in (T1), and each input test as in CMP 102 (7). Suppose the local problem is of the admitted two-layer class and its field radius is at most \(a_5\). Then its central tests obey \(\rho(y)\le\max\{B_3e(y),\frac12\sup_{z\in N(y)}\rho(z)\}\). At a vertex without such a patch, supply a separate boundary inequality.

This checks localisation of the quoted and reconstructed argument, conditional on the patch geometry; the original printed pages were not independently inspected. The earlier H21 check, which used global radii, does not certify the new incidence and boundary assignments automatically.

**Lemma I, lines 58–69: ADVANCE.** The induction, interchange of supremum and finite maximum, directed reachability distance, and disappearance of the bounded remainder are correct. No symmetry of \(N\) is required. The equality with the distance formula uses nonnegative data. Empty and unreachable sets contribute zero.

**Theorem G, lines 71–79: ADVANCE as the stated abstract implication from (LR); REVISE the boundary convention.** Its first bound follows from Lemma I. Its factor two follows from \(e(z)\le\sup_{N(z)}t\) and one further directed edge. This requires a read-complete assignment of tests, not merely their base points when an averaging contour or a current stencil leaves that block.

Line 77's assertion \(\rho(y)=t(y)\) on pinned blocks is false for the full (T1): fixing the field fixes its current, but does not identify current with a single plaquette test. The repair is local: include the full current stencil in the datum neighbourhood. With \(\eta=1\), the divergence norm is at most \(6\max_{p\ni b}|\partial V(p)-1|\); the corresponding Lie-algebra current has bound \(12\max_{p\ni b}|\partial V(p)-1|\). Enlarge \(B_3\) to at least 12 before choosing the reset radius and buffer. Then the same inequality holds at a completely pinned stencil, without asserting equality of the two radii.

At the cut, \(e=a_1\) need not be bounded by the actual local tests \(t\). Consequently the second inequality of (G.1) cannot be applied there with the original \(t\). Use Lemma I with the artificial boundary datum retained. Expanding paths until their first exit from \(G\) gives exactly the sufficient replacement used later:

\[
\rho(y)\le 2B_3\max\left\{
 \sup_{z\in G}t(z)2^{-d_N^G(y,z)},\ a_1 2^{-i_S(y)}
\right\}.
\]

The factor two also covers a data read which first reaches the cut in the next reset neighbourhood. This proves the path split, subject to the corrected reset and boundary inequalities; it does not identify the actual splice datum.

## 3. Consumers, data and geometry

| Note passage | Verdict and checked scope |
|---|---|
| §§1–2, lines 12–36 | **ADVANCE** for the three consumers and the sufficient numerical margins. **REVISE** the claim that nothing reads the share decomposition: a total bound suffices for clauses (c), (d) at the original threshold, but does not itself verify the separately invoked floor or halved-factor statements. |
| Configuration and chain, lines 42–44 | **ADVANCE as construction inputs.** I:92401–92448, 92515–92535 and 138407–138411 identify the splice, its common blocks away from the cut, its reality and its raw datum. They do not prove (I-A)'s complete CMP 102 admission. |
| (I-A), line 85 | **ADVANCE as an explicitly open input.** The actual nest, every mixed-level datum test and the minimal-orbit identification remain to be supplied. |
| (I-G), line 86 | **ADVANCE on its stated class.** I:63571–63607, 91723–91728, 91991–92024, 92095–92097 and 137093–137097 support the retained geometry and separation. The interpretation as a compatible path metric remains part of the input. |
| (I-D), line 87 | **REVISE the attribution, retain as an input.** I:137012–137036 gives the pointwise same-stratum data bounds and cites the raised-block estimate. It does not spell out the new quantitative bound for every mixed-level test in a reset patch. Global admission at \(a_1\) in (I-A) is weaker than that local bound. Require the displayed (I-D) bound on the full test set, including the mixed-level transports. |
| (I-N0), line 88 | **ADVANCE conditional on the local indexing.** I:68327–68334 gives \(L_0^{6N_0}\le l_j^2\); hence \(L_0^{2\nu}\le l_j^{2/3}\le l_j\), since \(l_j\ge1\). The index \(j\) must be the datum's current level, as the note assumes. |
| (I-R), (I-T), (I-K), lines 89–91 | **ADVANCE as retained flow inputs.** Apply the comparisons to the finitely many exponents actually used: \(p_0,p_0+2r,q\). I:131413–131446 fixes the radius powers and finer-index comparison; I:77928–77954 fixes \(k=h+\check R_k\) and the lower scale bound. No arbitrary-exponent uniformity is needed. |
| Floor (M), line 93 | **ADVANCE.** The constants preceding (M) are fixed; increasing (M) supplies the stated finite geometric margins. Repaired reset read sets must still satisfy these margins, with a larger fixed floor if necessary. |

**REVISE the core definition, line 45.** The two definitions there do not make \(K=D_2\setminus B_S\): \(K\) excludes raw blocks, and is not explicitly intersected with \(D_2\). Also the source band \(\mathsf S\) of I:92468 is not the boundary \(S=\partial(\Omega''_{h+1})^\sim\) of I:138358–138362. Use separate names and define

\[
 K_0=\{y\subset D_2\cap G:d_{\rm sc}(y,\mathsf S)\ge\check R_k/2\},
 \quad K_+=\{y\in K_0:o(y)\ge1\},\quad B_S^{\rm new}=D_2\setminus K_0.
\]

The positive-level assertions concern \(K_+\). Raw collar assertions are B1 and the existing pinned-seed calculation. This repair does not identify \(B_S^{\rm new}\) with the account's set; that matching and the coverage of the discarded band remain obligations. In particular the claimed containment of the entire \(Z_h^{(2)}\) in positive-level \(K\) is false when that enlargement contains raw cells. Nor does a fixed physical enlargement have a uniformly bounded length in a metric which counts finer local cells.

**Lemma C, lines 99–110: ADVANCE on the declared reset neighbourhoods and path metric.** C0 uses the separation of consecutive zones. In C1 the crossing intervals have disjoint interiors; the extra step reserved in each interval makes the summation valid. The reverse crossing uses the larger starting block and is covered by the factor \(6L R_1M_1\). C2 correctly combines a level-crossing bound with a spatial-distance bound by taking half their sum. Its hypotheses must include the last edge reaching the cut and the fact that the cut region reached is the source band. These are geometric inputs, not consequences of criticality. Enlarging a reset neighbourhood requires rechecking its step bound, not silently keeping the old constants.

## 4. B1: the part the collar consumer needs

**ADVANCE as an implication from the read-complete reset, (I-A), full (I-D), the stated geometry and flow inputs.** This is not an unconditional discharge of these inputs.

| Step, note lines | Verdict |
|---|---|
| Placement near the collar, 120 | **ADVANCE** under the retained separation: the \(20M\eta\) neighbourhood avoids \(\Lambda_1\), after a fixed lower bound on \(\check R_1\), and its level-at-most-one blocks are in \(Z_1\subset Z_h\). |
| Splitting paths, 122 | **ADVANCE** with the artificial cut datum retained as in §2 above. |
| Paths in \(G\), 124 | **ADVANCE.** The level-0 and level-1 cases are covered by \(c_R\). For larger levels the factor \(L_0^{2\lambda}\) is dominated by \(2^{-s_0(\lambda-2)}\). The remaining inequality \(4^{-m}\sqrt{m+1}\le1\) is correct. |
| Paths to the cut, 126–134 | **ADVANCE.** The factor \(\sqrt{k-1}\) is bounded by \(\sqrt{(1+h)\check R_k}\). The bound \(2^{-(h-3)^+s_0/2}\sqrt{1+h}\le2\) holds. Since \(r\ge2\), \(2^{-R/64}e^{t/2}\sqrt R\to0\) uniformly for \(R\ge(\log(e^t-c_5))^r\). |
| Conversion to the level-one radius, 136–140 | **ADVANCE.** \((\Gamma_1)\) supplies exactly the required \(1/64\). Retain the incidence convention at seam plaquettes; a base point in level zero does not change the plaquette's level-one threshold. |
| Application to Lemma B and its cubes, 142 | **ADVANCE conditional on the preceding inputs.** The genuine index-zero cubes have at most \(10M\) sites per side and only pinned or level-one plaquettes (I:142771–142783). Thus B1 supplies all their non-pinned plaquettes. Lemma A supplies the pinned part. The previous current and axial-gauge calculation then applies without a separate (S-B) assertion. |

**REVISE the ceiling terminology.** \((\Gamma_1)\) has degree \(p_0-q<0\); \((\Gamma_3)\), \((\Gamma_4)\) have degree \(p_0+2r-q<0\), not degree \(-\infty\). The exponential cut ceiling has degree \(-\infty\). All can be imposed by choosing \(\gamma\) last. These are ceilings on \(\gamma\), not “caps” as defined at I:1246–1253. This correction does not break absorption.

## 5. B2: own-level entries and cubes

**Condition (Q), lines 146–148: ADVANCE.** The expression for \(l\), the exponent \(p_0+2r-q\), and its domination by the account's floor \(q\ge p_0+7r+1\) are correct (I:1364, 70839–70841). A polynomial loss from raised data can therefore be absorbed. This does not prove the mixed-test bound (I-D).

**Lemma J, lines 150–152: ADVANCE on a full six-plaquette stencil.** The expansion of \(W-W^*\), cancellation of constants and remainder \(6(0.56)\theta^2<3.4\theta^2\) are correct. For a real field the inverse actually has norm one, so the stated inverse bound is conservative. Boundary bonds without that full stencil need their boundary convention.

**B2(a), lines 156, 166: ADVANCE as a conditional estimate.** The graded-data supremum and the first-exit term are controlled as stated. Here \(0\le n\le h\) is essential: \(U_2\) has order \(h\), and \(k-n=\check R_k+h-n\). Then

\[
2^{-(h-n-2)^+s_0/2}\sqrt{1+h-n}\le2,
\]

so the same \((\Gamma_2)\) applies. No factor depending on the age remains.

**B2(b), lines 160, 168–172: REVISE the current step; the conclusion follows from the same inputs and ceiling.** The use of \(\theta\le\rho' L^{-2n}\) does not follow from a neighbouring plaquette at level \(n-1\): its (T1) bound would carry \(L^{-2(n-1)}\). The following repair avoids that loss. For a real \(U\), unitary parallel transport commutes with \(\pi\operatorname{Im}\). The current formula I:142632–142641 therefore gives, on the same complete stencil as (T1),

\[
\eta^3J(U)=\pi\operatorname{Im}\bigl(\eta D_U^{\eta *}\partial U\bigr),
\qquad
\eta^3|J(U)(b)|\le c_\pi\rho(y)L^{-3n}
\le4B_3c_R\varepsilon_n^D L^{-3n}.
\]

Here \(c_\pi\le2\): taking the imaginary part is contractive, and subtracting the scalar trace part costs at most a factor two. Read (T1) at the bond's incidence level, or at the weaker level \(n\). The existing \((\Gamma_3)\) is stronger than the required \(256B_3c_R\delta_D\le\varphi_\flat\), since \(c_R\ge1\). The plaquette estimate and \(A'=0\) give entries 1, 5, 6 and 7 as written.

**B2(c), lines 161, 174–178: BLOCK at the enlarged-cube inference.** “Meets \(K\)” does not establish the regularity and geometry on the whole collar that H14.1 reads. The proof assumes that this collar stays at distance \(\check R_k/4\) from the source band, and that its regularity can be read at scale \(\lambda\) with only the displayed \(L^3c_R\) loss. Neither follows just from physical size and one intersection point. A physical enlargement measured at level \(\lambda\) can traverse finer cells, which cost more in \(d_{\rm sc}\). No relation between \(\lambda\) and the level at the intersection point is imposed in the displayed statement.

The alternative citation does not remove this issue. I:36550–36565 requires regularity on an entire specified collar. H14.1 retains its admitted enlarged region and smallness condition. The exact useful restricted statement is:

> For each required cube \(Q\) of family index \(\lambda\), supply an enclosing admitted cube and auxiliary collar \(Q^+\) inside the domain of \(U_2\). Prove on all of its reads the scale-\(\lambda\) regularity bound \(2L^3B_3c_R^2\varepsilon^D_\lambda\), and the required gauge-chart smallness. Then H14.1 gives the claimed gauge estimate by \((\Gamma_4)\).

The last implication is **ADVANCE**; the collar hypotheses are the blocking step for the unrestricted claim and the actual frozen families. Calling the cube a “level-\(\lambda\) cube” does not verify them. **REVISE** B2's hypothesis list to include \((\Gamma_4)\), which line 154 omits, and the finite gauge smallness ceilings.

**B2(d), lines 162, 180: ADVANCE conditional on (Ref) for every actual triple.** Criticality under stronger constraints and uniqueness give the gauge identification. The two scaling identities transfer entries 1 and 3 to entries 2 and 4. I:137049–137070 gives this conditional argument. The refined boundary conditions, admissible class and uniqueness remain part of (Ref).

**All \(w\ge1\) and finer birth indices, lines 164 and 31: ADVANCE for the established entries.** A bound at \(w=c=1,F=\varphi_\flat\) implies the larger thresholds. I:131441–131446 gives the finer-index comparison. Neither observation repairs the cube gap.

## 6. Lemma P: placement

**ADVANCE for the positive-level point statements; BLOCK for the general cube statement (lines 184–188).** Timing (I:132086–132175), \(W_c\subset X_c\subset Z_h\), the law-site separation and the corrected definition of \(K_+\) put every positive-level block of \(W_c\) in \(K_+\). The same argument puts the positive-level blocks near the collar there. The genuine index-zero cube assertion follows from B1 with its retained premises.

The proof's assertion that a cube meeting \(W_c\) meets a block of \(K\) drops the positive-level restriction. The account permits raw points in \(W_c\) (I:133037–133051). A small cube contained in a raw part of \(W_c\) meets \(W_c\) and no positive-level \(K\), while satisfying the stated upper bound on its side. This refutes P(i)'s unrestricted cube assertion, not the placement of positive-level blocks.

The corrected point statement is \(W_c\subset K_0\) and \(W_c\cap\{o\ge1\}\subset K_+\), with all sets restricted to the completion domain. For actual frozen cubes, supply their family constraints and enlarged-cube containment from §5. Saying they “meet \(K\)” does not establish “whole in \(D_2\setminus B_S\)” at I:136752–136756. Line 188 and Result item 3 must retain this obligation.

## 7. Shares: the algebra passes; the actual norm comparison is missing

**Lemma BCH, lines 194–196: ADVANCE.** The differential equation, commutator cancellation and Gronwall argument are correct. For \(x=1.022|X|\le1.022/40\), the elementary series bound \(e^x-1\le x/(1-x)\) already gives the stated coefficient below 1.05, hence below 1.1. This needs no numerical run.

**Lemma \(A_n\), lines 198–203: ADVANCE.** Each of its three conclusions follows with the displayed constants, provided its input derivative is genuinely \(\nabla_{\mathbb U}\). In (i), the linear and quadratic contributions carry \(L^{-2n}\), while the curvature-transport term carries \(\theta L^{-n}\). In (ii), the rescaled bond logarithm gives 1.06. In (iii), the quadratic BCH remainder is small enough to use the elementary difference bound: its \(L^{-n}\) cancels the derivative's \(L^n\). The two contributions are \(2.2Na\) and \(2.1Na\). Thus \((1+4.3a)N\le1.06N\). No estimate of a derivative of \(A'\) is being assumed.

**Lemma E', lines 205–207: ADVANCE** for the corrected positive-level core and the stronger zone thickness used there. The crossings of levels \(n+1,\ldots,h-1\) are disjoint. Combining their length with the core-distance bound by half the sum is valid.

**Proposition Sh, lines 209–224: BLOCK as an implication from only its displayed premises.** The first unsupported step is the passage at lines 211–216 from the tuple norm at each layer's kernel to \(N_{\mathbb U_{\rm partial}}(H_s)\), which Lemma \(A_n\) needs. Changing length units costs \(L^2\); changing the connection in a covariant derivative is a different operation. Small curvature of both connections does not bound their difference in the fixed presentation gauge.

For example, on a level-\(n\) patch let \(W_\mu=1\), let a constant flat connection \(V_\mu=g\) act nontrivially on a matrix \(H\), and take \(h_\nu=\epsilon H/(L^n\eta)\), all other components zero. Its \(W\)-gradient vanishes and \(L^n\eta|h|=O(\epsilon)\), but

\[
(L^n\eta)^2|\nabla_{V,\mu}h_\nu|
=\epsilon L^n|\operatorname{Ad}_gH-H|.
\]

Both kernels can be flat. Their individual regularity and the layer size therefore cannot supply the claimed comparison. This example refutes the inferred norm implication, not the actual completion construction.

I:142476–142480 explicitly uses the derivative at the preceding partial product. It does not identify that norm with the norm at the kernel of the cancellation-based construction used here. The collar proof in ca-f avoids the issue by a unit-spacing estimate; at positive levels that shortcut would cost the unbounded \(L^n\) above.

The remaining steps have these verdicts:

| Step | Verdict |
|---|---|
| Weight and decay, 211–214 | **ADVANCE conditional on the extended (G-sep), complete local read sets and ca-f's full tuple inputs.** Taking \(\delta_R\le w\delta/2\) is valid. The split of \(\sqrt{\check R_k+h-n}\) and the finite \(S_2\) remove the age. |
| Entries 6 and 7, 216 | **BLOCK at the norm comparison just identified.** The subsequent \(A_n\) algebra is correct. |
| Entries 1 and 5, 217 | **REVISE for the second layer.** Entry 5 is unchanged. At that layer use \(\theta\le L^{-2n}[(\varphi_\flat/64)\alpha_{0,n}+3F]\), not B2's bound on the original base alone. |
| Current, 218 | **ADVANCE** at the kernel of each layer. ca-f's constant-cut current calculation is valid in the local unit \(l_y\), given (N6), (N7), the smallness bound and the actual segment-current identification. |
| Derived entries, 219 | **REVISE.** Input 1(e), I:131580–131586, gives an upper increase, not an absolute difference. It also requires \(C^b(a_\flat+\kappa_{\max})\le1\), admissible triples and a majorant for the layer in its required norm. The majorant must include the unit and connection comparison constants. |
| Ceiling, 220–224 | **ADVANCE as an absorption argument once the preceding bounds hold.** A fixed enlargement of its constant is harmless. Keeping the \(G\)-part fixed preserves existing cube gauges; it does not construct the missing gauges of B2(c). |

A concrete conditional repair is available. Supply, on every required read set and in one gauge, the kernel identities \(W_3=U_2\) and \(W_4=e^{i\eta H_3}U_2\) (or \(W_4=U_2\)), together with their compatibility with the cancellation datum. If the converted tuple bound is \(F_0\), these identities imply

\[
l^2|(\nabla_{\mathbb U_{\rm partial}}-\nabla_{W_4})H_4|
\le 2.2F_0^2,\qquad
N_{\mathbb U_{\rm partial}}(t_4H_4)\le2F_0
\quad(F_0\le1/100).
\]

Indeed the relating left factor is \(e^{i\eta uH_3}\), \(|u|\le1\); the adjoint difference is bounded by \(e^{2\eta|H_3|}-1\), and the factor \(l/\eta\) cancels against \(\eta|H_3|\). This also handles partial \(t_3\).

Set \(F=2F_0\), enlarge \(C_S\) accordingly, and require \(F\le\min\{1/100,\alpha_{*,n}/100\}\) and \(\alpha_{0,n}\le1/10\). The corrected second-layer curvature bound then still gives \(5.6\theta L^n<0.1\). Use a fixed multiple of the global weight majorant that includes this comparison and the neighbour-unit factors in 1(e). Inductively each derived entry remains below its full radius, so each upper increase is at most \(2\pi r_e\). The enlarged \((\Gamma_{\rm Sh})\) yields

\[
Q_e(\text{chain})(y)\le Q_e(\mathfrak b_2)(y)
       +\frac{3\varphi_\flat}{64}r_e(n).
\]

This one-sided statement suffices for spend. It does not assert the absolute-difference conclusion for entries 2 and 4. The repair is proved conditional on the specified kernel/read-set matching and full rescaling hypotheses. Their verification for the actual \(H_4\) is still open here; neither (N7) nor a change of units supplies it.

**Line 226: REVISE.** A bound for the sum of two layers is sufficient for the original spend calculation. It does not identify the account's three named shares, their separate floors, or the additional halved-factor application in II:1208–1212. No such identification is proved by partitioning a numerical total after the fact.

## 8. Source coverage and the absence claim

**REVISE “stated or proved nowhere” to “no independent, noncircular supplier located in the four supplied sources.”** The former is literally too strong: I:138382–138390 states the base and increment conclusions, and I:138438–138464 describes the purported own-level theorem and shares in considerable detail. These are the consumer's assertions and invocations, not a separate construction proving its inputs.

Searches of all three account files and the outline, together with the full-read index's neighbouring rows and cited source ranges, give the following:

| Object | What is actually present |
|---|---|
| Sealing construction and placement | I:138361–138366 names its objects; I:138402–138405 invokes placement. I:136724–136756 uses core membership in ambient inclusion. Neither passage supplies the missing construction and its hypotheses. |
| Own-level bound, all weights, cube gauges | I:138438–138450 invokes exactly the age-independent \(1/64\) bound. II:39436–39482 is an admission statement about terms/families with its own hypotheses, not a proof of this bound for the actual \(U_2\). |
| Age-independent ratio, shares and floors | I:138454–138464 invokes the ratio corollary, three shares, bend and ownership floors and floors at a set \(\Gamma_\flat\). No separate supplier of this package was located. I:131806 does define a numerical \(\Gamma_\flat=(\varphi_\flat/\varphi_{\min})\Gamma\); it is not the asserted set with those floor conditions. |
| Later uses | II:1128–1212 invokes the sealing theorem's proviso, weight condition and halved-factor application. II:44284–44316 invokes sealing relations again. These are additional uses, not suppliers. |
| Outline predecessors | SA:9678–9691 already states a local regularity profile in Theorem 2, with a sketched argument. SA:12309–12381 (BGR32–33) and 17433–17459 give the birth/transport framework conditionally. They do not construct this sealing package for the actual \(U_2\). III:22159–22170 likewise assumes a local-zone halving input. |
| Closing list | III:111170–111509 does not separately name the sealing construction, its own-level theorem, share statement, placement statement, ratio corollary or its floors. It does name “dissolution of the arrested region” (111379–111380), ambient inclusion (111391–111392), and the arrest theorem (111393). The omission is of the named supplier, not of every related incomplete claim. |

Thus the requested substantive absence finding is supported at this source revision, with that precise wording and scope. A search cannot certify absence of every conceivable differently formulated theorem. The inspected nearby candidates do not discharge these inputs. There is no basis here for claiming a new general local-profile idea: the outline already contains that idea. The check target—the proposed quantitative instantiation for \(U_2\)—is not thereby covered elsewhere.

## 9. Dependence and the note's final claims

**No direct analytic self-discharge; no unconditional acyclicity certificate for the actual construction.** The note's reset, path iteration, absorption and left-factor calculations do not use clause (b), clause (c), or the arrest theorem's conclusion as estimates. It uses the room lemma as a consumer and uses rescaling input 1(e) as an input; using that separately stated hypothesis is not invoking the arrest theorem.

However, the identification of the actual completion objects must remain a primitive obligation. I:142292–142317 explicitly attributes some completion-site facts, including part of the core identification, to the arrest theorem. Importing that whole package to fill the placement/kernel gaps would not establish an independent supplier for the arrest theorem. Timing, the raw splice and the layer definitions must supply the required facts independently, with their exact premises. The note does not currently complete that task.

| Final passage of the note | Verdict and corrected statement |
|---|---|
| Opening summary, lines 1–10 | **REVISE** to the conditional conclusions and blocking steps recorded here. The complete sealing construction has not been supplied. |
| §8, local reset and admission limitations | **ADVANCE** for the acknowledged conditionality; **REVISE** to retain the full local read sets and boundary convention of §2 above. Global \(a_1\)-admission alone is not the local graded estimate needed away from the cut. |
| §8, data, exponent floor, refinement | **ADVANCE** for the exponent floor and the declared use of refinement; **REVISE** the assertion that the pointwise data clause supplies every local mixed-level test. |
| §8, two failed approaches | **ADVANCE** as failures of the proposed deductions. Uncontrolled shell weights cannot be inserted into the reset, and the global maximum estimate alone loses the age factor. Neither observation is a no-go theorem for other approaches. |
| Result 1, B1 removes (B-in), (S-B) | **ADVANCE conditionally**, with the corrections in §§2–4. The old names can be replaced by the explicit reset, admission, local-data and geometry inputs. They have not all been discharged for the actual splice. |
| Result 2, full own-level theorem | **REVISE** to the established cell entries and conditional refinement statement. **BLOCK** the unrestricted cube assertion at the missing enlarged-collar argument in §5. |
| Result 3, placement | **REVISE** to \(W_c\subset K_0\), positive-level points in \(K_+\), and the genuine index-zero collar result. **BLOCK** the stated unrestricted frozen-cube and account-\(B_S\) identification. |
| Result 4, shares | **BLOCK** as stated. The repaired conditional one-sided spend estimate is §7; it still needs the actual kernel comparison and full rescaling premises. |
| “Clauses (b), (c) … get their inputs” | **BLOCK** for the full package. Cell bounds are substantial conditional progress; the cube, placement and share gaps prevent this conclusion. |
| “New mathematics”, “Kind” | **REVISE** to checked conditional estimates and proposed instantiation. Theorem G's local-profile principle has the outline predecessor just identified; no priority or full sealing theorem is established here. |
| Named inputs, consumer changes and next steps | **REVISE** by adding the obligations below and correcting the ceiling terminology. There is no basis for an unconditional node/status update. The suggested registry/tree changes and posting are not performed. |
| Provenance | **ADVANCE** as the author's provenance record, not an independent certification of its original-paper reads. This check uses the on-disk text; the four source hashes match those recorded in library/arr.md:19–24. |

## 10. What remains open

1. **Actual Balaban instance and local reset geometry.** Identify \(U_2,V_2,\mathbb B_2\), the admissible nest, minimal orbit, every mixed-level datum test, and the reset patches with all their averaging/current/gauge reads. CMP 122b (1.52)–(1.53) and CMP 119 (2.12)–(2.15) remain imported admission inputs. The local reset argument passes on its admitted class; its use on every required splice block needs this matching.
2. **Local graded data and derived entries.** Establish full (I-D), not just pointwise same-stratum bounds or global \(a_1\)-admission. Retain (Ref) for the actual refined triples. For shares retain all of input 1(e), including its smallness, weight, norm and radius-comparison conditions.
3. **Cube geometry and placement.** Prove the enlarged-collar regularity and scale relation for the actual frozen cube families. Identify the corrected \(K_0,K_+\) and \(B_S^{\rm new}\) with the sets the consumer uses. The assertion that a cube merely meeting the core suffices is not proved.
4. **Layer antecedents and positive-level shares.** ca-f's (N1)–(N3) remain open antecedents, with (N1) owned by stage-claude and (N3)'s operator issue recorded under B99b-T314. No attempt to solve those other rows is made here. In particular the datum norm, admissible weights, operator identification and any covariant-Laplacian entry must match. Also retain cancellation, the extended (G-sep), the actual local budget and kernel irregularity, and establish the missing comparison with the preceding partial product. ca-f already identifies \(W_3=U_2\); the unresolved matching concerns \(H_4\), its read sets and its cancellation-based datum.
5. **Gauge group.** The rebuilt reset checked here is for \(SU(2)\). The \(SU(N)\), \(N\ge3\), extension is not checked by this note.
6. **Ambient inclusion's discarded band.** Coverage of the actual \(B_S\) by the keystone region is still an obligation of consumer A, as the note acknowledges. Enlarging or redefining that band does not establish coverage.
7. **The exact account package.** The three separately named shares, bend and ownership floors, floors at the asserted set \(\Gamma_\flat\), and the halved-factor application in II:1208–1212 have not been reconstructed. A corrected total spend bound would suffice for the original numerical \(1/16\) addition, but does not by itself supply this entire package.

**Overall: REVISE, with BLOCK on the full sealing conclusion.** Lemma I, the admitted local reset, the conditional graded decay and age absorption, Lemmas C, J, BCH, \(A_n\), E', and the restricted B1/B2 cell estimates survive as specified above. The full B2 cube statement, P's unrestricted cube placement and Sh from its stated premises do not. No run discharged a mathematical obligation; no status is granted.

Checked line by line by Codex (gpt-6-astra).
