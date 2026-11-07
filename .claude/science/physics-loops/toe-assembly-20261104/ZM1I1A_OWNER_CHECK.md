# ZM1-I1[a] owner question: Astra max check

Checker: Codex gpt-6-astra, reasoning effort max, read-only, laptop, 2026-11-07 (run log ~/toe-lap/prior/astra_zmg1.log; spec ~/toe-lap/tmpl/astra_zmg1.txt). It checked the owner question on the zoom's block-map definition before the lead asked it (owner rule 2026-11-06). Its new spectral-endpoint argument against R-G1EQ is one model's argument, not refereed. The lead copied the final message below unchanged.

The framing is correct **under R-form**. The tentative recommendation needs changing. I find an additional obstruction to the printed R-G1EQ.

Definition Z alone permits general finite coarse algebras. R-form supplies the same five-mode construction. The referee explicitly leaves that interpretation to the owner. RC-1 resolves the coarse-link placement issue. It does not resolve R-form. [ZM1:53](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:53), [Referee:148](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:148), [Referee:229](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:229).

The original obstruction uses no vacuum, update, comparison class or exponent. Trace transfer preserves the nonzero covariance across a coarse edge. Exact Gauss identification therefore preserves adjacency. Locality and the density count then force \(L=1\). Changing class (a) or \(p\) cannot repair that contradiction. Every proposed class retains the obstructed map conditions. [ZM1I1A:25](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:25), [ZM1I1A:40](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:40), [Referee:154](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:154), [ZM1_OBS:50](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1_OBS.md:50).

The additional obstruction is as follows. **This is a new argument from this check. It is not an already refereed result.**

The printed G1-eq gives
\[
D_X^T=\Phi(\mathcal G_X^{(1),T})-\mathcal G_{x_X}^T
\in\Phi(\mathfrak A_1)'\cap\mathfrak A.
\]
That equivalence is already established in the report. [Referee:167](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:167).

Take the full matrix algebra of one coarse star. Its unital image splits off as a matrix tensor factor. Matrix units give this decomposition. Consequently,
\[
\Phi(\mathcal G_X^{(1),T})=H\otimes1,\qquad D_X^T=1\otimes D.
\]
If \(H\) has spectral endpoints \(a,b\), then the fine generator has endpoints
\[
a-\max\sigma(D),\qquad b-\min\sigma(D).
\]
If its endpoints are also \(a,b\), then \(D=0\).

On U, choose \(T=E_{jj}\). Its Gauss generator is one matter occupation plus six single-mode rishon occupations. Its spectrum is \(\{0,\ldots,7\}\). This holds for every \(m=1,\ldots,9\), including every allowed coarse \(m_1\). Thus G1-eq forces exact generator equality for each \(E_{jj}\). Summing gives (G1) at \(T=1\). Theorem 3 then forces \(L=1\). [LW1_5:96](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LW1_5.md:96), [ZM1I1A:44](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:44).

On O, each Cartan star generator has endpoints \(-7/2,7/2\) on both sides. The same argument forces (G1) on all five Cartan generators. Theorem 6 again forces \(L=1\). [ZM1I1A:66](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:66).

This is where I materially differ from the referee. The relative commutant defeats the original covariance comparison alone. The equal spectral endpoints remove that freedom for these particular registers. The report labels G1-EQ open. The argument above would close it negatively under the exact printed conditions, after an independent check. [Referee:158](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:158), [Referee:211](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:211).

Brothier–Stottmeister supplies no counterexample to this conclusion. The checked example is a one-dimensional pure-gauge analogue. It does not have these five-mode star generators. [Referee:175](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:175).

The three named options are neither exhaustive nor equally specified. The owner may also retain the definition and accept its empty \(L\ge2\) class. The following replacement clauses make the relevant alternatives explicit. Unchanged clauses of §3.8 remain in force where applicable. None of these clauses asserts existence.

1. **R-G1EQ.**

   Record:
   > Replace (G1) by
   > \[
   > \Phi\circ\operatorname{Ad}(e^{i\theta\mathcal G_X^{(1),T}})
   > =\operatorname{Ad}(e^{i\theta\mathcal G_{x_X}^T})\circ\Phi
   > \]
   > for every \(X,T,\theta\). Retain the unital injective graded *-homomorphism, (Z-a), (Z-b), (G2), disjoint singleton sets and R-form.

   Tests: **P P C P**. Test 1: it specifies a map condition. Test 2: its quantifiers are closed. Test 3: charge identification requires justification. Test 4: it adds no structure. This agrees with the referee’s specification score. It does **not** make the option viable. The additional obstruction above applies. [ZM1I1A:150](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:150).

2. **Non-singleton embedding sets.**

   Record:
   > Replace \(|S_X|=1\) by nonempty, finite, pairwise disjoint \(S_X\). Retain
   > \[
   > \Phi(\mathcal G_X^{(1),T})=\sum_{x\in S_X}\mathcal G_x^T
   > \]
   > and (G2).

   Tests: **P P C P**. Test 1: no outcome is assumed. Test 2: the sets are fully quantified. Test 3: diagonal invariance does not establish invariance under each fine-site gauge action. Test 4: these sets are already data allowed by Definition G. [ZM1:72](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:72).

   Proposition V is correct on U. Its equation is
   \[
   45(|S|-1)=6k_1-k|\partial S|.
   \]
   The bounds \(k\ge9\), \(k_1\le25\), and \(|\partial S|\ge6\) give \(|S|\le3\). Three sites give \(|\partial S|\ge14\), hence the contradiction \(90\le24\). Two sites give an even right side and the odd left side \(45\). Therefore \(|S|=1\). This option does not rescue U. The report proves no corresponding O proposition. [ZM1I1A:52](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:52), [Referee:216](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:216).

3. **Drop (G1), retaining only (G2).**

   Record:
   > Delete (G1). Impose no intertwining condition at representative sites. Retain (G2) and the remaining map conditions.

   Tests: **P P C P**. Test 1: no success is stipulated. Test 2: the deletion is exact. Test 3: the coarse-to-fine gauge correspondence is lost. Test 4: nothing is added.

   This cannot retain the claim \(\Phi(\mathfrak A_1^G)\subseteq\mathfrak A^G\) without another condition or proof. The existing proof uses (G1) at representatives and (G2) elsewhere. Calling the weakened map “gauge covariant” would therefore be misleading. [ZM1_OBS:66](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1_OBS.md:66).

4. **R-ISO.**

   The mathematical schema is:
   > Specify compatible finite-volume isometries \(V_\Lambda\), with
   > \[
   > V_\Lambda^*V_\Lambda=1,\quad
   > P_\Lambda=V_\Lambda V_\Lambda^*,\quad
   > \Phi_\Lambda(A)=V_\Lambda A V_\Lambda^*.
   > \]
   > Replace (G1) by
   > \[
   > \mathcal G_{x_X}^T V_\Lambda
   > =V_\Lambda\mathcal G_X^{(1),T}.
   > \]
   > Specify the subspace rule, locality, covariance, infinite-volume compatibility and comparison-state normalization.

   Tests **as currently offered**: **C F C C**. Test 1: the subspace rule could encode the desired sector. Test 2: that rule is missing. Test 3: dynamical closure or vacuum support could be assumed improperly. Test 4: the added subspace requires a reason.

   I change the referee’s second C to **F as written**. The referee itself says it fails until a rule is supplied. Also, \(\Phi(1)=P\). One must not silently assume \(\omega_0(P)=1\), or condition the vacuum onto \(P\). Attack 3 supplies no completed classification. [Referee:171](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:171), [ZM1:388](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:388).

5. **R-MEAS.**

   Record the route, rather than a completed definition:
   > Replace the operator embedding by a specified local gauge-covariant Euclidean blocking kernel \(K_L\). Define
   > \[
   > \mu_1(f)=\mu_{\rm fw}(K_Lf).
   > \]
   > Specify \(\mu_{\rm fw}\), \(K_L\), normalization, boundary conventions and the operator-to-Euclidean observable dictionary. Keep Y1, reflection positivity and the required RG-class membership as proof obligations.

   Tests **as currently offered**: **P F C C**. Test 1: no physical conclusion is asserted. Test 2: the kernel and dictionary are unspecified. Test 3: the bridges could otherwise be assumed by premise. Test 4: Euclidean structure needs independent justification.

   I change the referee’s closedness C to **F as written**. Positive weights do not themselves establish reflection positivity. This route also cannot inherit the real-time class-(a) comparison without its dictionary. [ZM1I1A:152](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:152), [Referee:173](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_REFEREE.md:173).

6. **\(L=1\), with separate time blocking.**

   A closed diagnostic is:
   > Set \(L_s=1\). For each specified integer \(K\ge2\), take
   > \[
   > \mathfrak A_1=\mathfrak A,\quad
   > \Phi=\mathrm{id},\quad
   > \alpha_1=\alpha^K,\quad
   > \omega_1=\omega_0.
   > \]
   > Replace \(Lt\) by \(Kt\). Enlarge the coarse-update class to include these iterates.

   Tests: **P P P C**, as a time-blocking diagnostic. Test 1: it claims no spatial zoom. Test 2: every datum is specified. Test 3: it assumes no common light cone. Test 4: independent temporal graining requires justification.

   The comparison is exact. Spatial coarse-graining is absent. If the original single-tick coarse-law form is retained, membership of \(\alpha^K\) in that form needs proof. The recorded spatial-and-temporal graining has \(c_t=c_s\). [ZM1:36](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:36), [Assembly:288](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:288).

7. **Change the coarse algebra.**

   “Another coarse algebra” scores **C F C C** until it is specified. Its target content is unknown. Its definition is incomplete. Its downstream assumptions are unknown. Its extra structure is unjustified.

   One exact alternative already exists:
   > Use Z0’s indexing and block algebras \(B_u\). Set \(\Phi=\mathrm{id}\), \(\alpha_1=\alpha^L\), and \(\omega_1=\omega_0\). Replace the same-type singleton gauge prescription by the product of fine-site gauge groups in each block.

   This scores **P P P P as an exact regrouping benchmark**. It asserts no bounded-content result. Its construction is explicit. It supplies no continuum physics. It retains the given degrees of freedom. Its cost is \(D=\exp(cL^3)\). [ZM1:93](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:93), [prior/ZM1I1A:25](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/prior/ZM1I1A.md:25).

   Adding neutral factors does not evade the original obstruction. Nor does an arbitrary finite-register replacement evade RC-3 when its stated trace-correlation hypotheses hold. [ZM1I1A:118](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:118).

8. **Restrict the map to invariant observables.**

   This is a further precise proposal:
   > Replace the full-algebra map by a unital injective *-homomorphism
   > \[
   > \Phi:\mathfrak A_1^G\longrightarrow\mathfrak A^G.
   > \]
   > Retain cell covariance. Require exponential locality for every local invariant input, with support-radius-dependent constants. Use this \(\Phi\) in class (a). Impose no map on charged fields or Gauss generators.

   Tests: **P P C P**. Test 1: existence remains unproved. Test 2: the domain and conditions are closed. Test 3: charged-sector consumers require another bridge. Test 4: the domain contains exactly the selected comparison observables.

   Neither full-algebra obstruction applies directly. Existence remains a separate question. This preserves class (a)’s stated physical-sector scope. [ZM1_OBS:169](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1_OBS.md:169).

9. **Allow a nonmultiplicative operator map.**

   Another precise proposal is:
   > Replace the *-homomorphism by a unital injective graded completely positive map. Retain G1-eq, (G2) and cell covariance. Require exponential locality for every local input. Keep the displayed products of images in \(F_0\). Do not identify \(\Phi(AB)\) with \(\Phi(A)\Phi(B)\).

   Tests: **P P C P**. Test 1: no matching result is assumed. Test 2: the map class is specified. Test 3: algebraic consumers need new bridges. Test 4: positivity has its own operational reason.

   The full-matrix tensor-factor argument no longer follows. This is an unproved alternative, not a construction.

10. **Drop locality.**

    Record:
    > Delete (Z-a). Retain the other conditions.

    Tests: **P P C P**. Test 1: no physical result is stipulated. Test 2: the deletion is exact. Test 3: spatial consumers lose their locality premise. Test 4: nothing is added.

    This removes the stated density contradiction. Adjacency still gives a graph bijection. It does not establish a spatial block map with controlled errors. [ZM1I1A:154](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:154).

These scores assess specifications. They do not establish nonemptiness. A criterion becomes a test-1 failure if its successful realization is inserted as a physical premise.

None of the closed kinematic alternatives above establishes T0-start, LZ1-i or GA2. R-ISO and R-MEAS need particular care when their missing rules are filled. Assuming the desired low-energy sector would import physics. Assuming a common speed would settle LZ1-i by premise. Assuming the required Euclidean representation or RG-domain membership would import unresolved GA2 bridges. T0-start itself remains a separate uniform theorem request. [GA2_Y2:176](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA2_Y2.md:176).

Class (a) supplies neither unconditional spectral transfer nor a common speed. RC-4 yields an approximate travelling correlation under an image hypothesis. RC-5 establishes the particular \(1/4\) tail. Neither supplies the required map images. The two-band application remains conditional. [ZM1I1A:100](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:100), [ZM1I1A:126](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:126).

The owner must be told that §3.8 already retained the obstructed conditions explicitly. It retained \(L\ge2\), the Definition-Z map, (G1), (G2) and singletons. It also explicitly said, “It asserts no existence result.” The choice specified a comparison problem. It did not establish its realizability. [Assembly:243](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:243).

The sentence “It is not shown impossible or trivial” is now stale under R-form. A suitable dated amendment would say:

> Under R-form, the frozen trace obstruction proves that the map conditions retained in §3.8 have no \(L\ge2\) instance. This supersedes the sentence “It is not shown impossible or trivial.” Class (a) and \(p=2\) did not cause the obstruction. No replacement definition is adopted here.

ZM1 already records the negative result in Amendment 3. The older prior digest predates it. Those historical “open” statements must not override the amendment. [ZM1:14](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:14), [prior/ZM1I1A:79](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/prior/ZM1I1A.md:79).

Q1 should therefore begin by clarifying R-form. It should not presume that the owner must adopt a replacement. Q2 should describe retention of an existing choice. The obstruction supplies no reason to change that choice.

For Q2, record:

> Retain class (a) and \(p=2\) as the comparison required of any replacement whose observable and state interfaces make that comparison well-defined. Whether the bound is achieved remains unproved.

Its recorded score is **P P P C**. The envelope imposes stronger matching than the printed absolute-error target. It forces matching asymptotic tail amplitudes and decay parameters when those forms exist. That accepted cost remains. Thus **P P C P is not the score of the whole proposed package**. Combining it with the retained envelope carries the additional test-4 qualification. [Assembly:244](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:244), [ZM1_OBS:284](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1_OBS.md:284).

I recommend retaining class (a), \(p=2\) as an unproved benchmark and offering the invariant-algebra map for owner consideration, because it preserves the selected observables without the full-algebra obstruction or an assumed continuum result.

No files changed. No git commands ran. The cited source hashes remained unchanged.