# Proof lane OT — older-test margin at the CV reference

Provenance: Research text by Codex in checkout 4df934dd7b12e8ba71ada97b7ae8a406511d5c85. Source material by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is credited where used. This note is not an audit and grants no status.

## Contract and source checkpoint

This lane concerns FCON Lemma 7, not an independent audit of FCON. All mathematical arguments below are by hand. Source retrieval, searches and hashes are bookkeeping only. The frozen texts retain their stated hypotheses.

Fix a specified stored stage of level \(j\). Use FCON's real CV reference \(V=M_-(U_+(W))\), its localized reference \(V^\sharp\), and its fibre \(D(Z,W)\), \(Z\in D_b\). For an older level-\(j\) loop reading a moved row, set
\[
 t_\tau=6C_{\rm sm}L^4L_\flat^{2\mathcal E_{\rm old}(\tau)}
              \varepsilon_{m_{\rm old}(\tau)},\qquad
 q_\tau=\tfrac98 n_\tau C_{\rm ch}L^4\delta'_j.
\]
Here \(n_\tau\) counts moved occurrences, including repeated and reversed edges. The target is \(|\partial V(\tau)-I|\le t_\tau-q_\tau\), for every real datum in use. Merely constructing a smooth field is not a counterexample. A witness must occur in a nonzero-weight admitted history.

Constants follow IN1 rows 1–10 (L221–236), including Amendment 1 (L666–675). Choose the exponents and margins, then \(L\) above all floors, then the flat, chart, inverse, profile and geometric constants. Uniform constants precede \(\kappa\) and are independent of \(M,\bar\kappa\). Later amplitudes may enter the final coupling ceiling. An inequality for \(C_P(L)\) cannot be manufactured by selecting \(L\) after that constant.

**Source disposition.** The SA full-read index was used before the source excerpts. Its chunk 16 rows for SA 17369–17396 and 17612–17630 classify the old-test argument as sketched. Reading those source lines confirms the distinction: SA 17369 says “the new tests imply the old”; SA 17624 gives shell-dependent curvature tests with graded margins. Frozen ST-test (st1-r4 L152) tests free removed rows against \(V^\sharp\), retaining older factors. It does not contain those graded reference-curvature tests. No correction to SA is claimed.

The CA-I index, chunk 10, identifies the stage-theorem premise at CA-I 54989–54995. The source explicitly assumes that theorem before transferring boundary-term estimates. That transfer cannot prove OT for the revised ST-test. The local sources used here include all of fcon.md, fcon-draft §4.6, and the relevant definition, stage, geometry, domain and constant-order passages of frozen st1-r4, geoh, dom, cp12 and in1. The requested SCIENCE_WORKFLOW.md and repository skill files are absent from this pinned checkout; no historical automation was substituted.

## Two elementary reductions

**1. The reference is inside the new passing chart.** On real data, FCON (2) gives \(D(m,W)=V\). F6/FC1 of ST1 give \(|m_e|\le b/8\). Thus the reference has at least \(7b/8\) free-coordinate room inside \(D_b\). Every removed row of \(V\) is also within \(\delta'_j/8\) of \(V^\sharp\). The pivot clause holds after the stated chart ceiling. This uses the real estimate; no Gaussian mean identification is needed.

Consequently ST-test alone does not keep the reference away from an old threshold. It accepts the reference whenever its datum and localization are admitted. A smaller fluctuation radius does not change this observation.

**2. A shell reference would give an open-set witness, subject to history realization.** Suppose an actual admitted stage and stored parameters have
\[
 t_\tau-q_\tau<|\partial V(\tau)-I|<t_\tau.                 \tag{1}
\]
Assume every other carried indicator is constant and passing on a real neighbourhood of \(D=V\). Assume the remaining real density is continuous and positive there, with finite positive normalizers. These are hypotheses about the complete stored integrand, not only its Wilson factor. Then this stage has positive-weight configurations violating OT.

*Proof.* The two inequalities in (1) are strict. Continuity preserves the old passing inequality on a small neighbourhood of \(Z=m\). Reduction 1 places that neighbourhood inside the new passing chart. Intersect it with the finitely many other passing neighbourhoods. ST1 FM5's real coarea density is positive on its chart. A positive continuous density has positive integral on a sufficiently small open ball. The reference is unchanged at fixed \(W\), so its violation of OT remains. If the stored parameters are integrated, the same hypotheses must hold on a positive-measure set of those parameters. ∎

This criterion removes the need to find a special nonzero fluctuation. It does **not** supply the admitted history or its other passing factors. A reference violating OT also need not make the old indicator nonredundant: \(q_\tau\) is an upper estimate for the possible change, not a proven outward displacement.

For any actual old datum passing this test in \(D_b\), F2 gives
\(\|a_V(u)\|<\tfrac98C_{\rm ch}L^4\delta'_j\). Telescope the loop product over moved occurrences. Each change costs at most that bond angle, since the other real factors are unitary. Hence
\[
 |\partial D(\tau)-\partial V(\tau)|<q_\tau,\qquad
 |\partial V(\tau)-I|<t_\tau+q_\tau.
\]
Thus a failure of OT in use lies in the precise strip
\(t_\tau-q_\tau<|\partial V(\tau)-I|<t_\tau+q_\tau\).
Reduction 2 treats the part of this strip below \(t_\tau\).

For an own-level loop, \(m_{\rm old}=j\), direct division gives
\[
 \frac{q_\tau}{t_\tau}
 =\frac{3n_\tau C_{\rm ch}}{16C_{\rm sm}}
 L_\flat^{-2\mathcal E_{\rm old}(\tau)}
 \frac{A_1}{A_0}\ell_j^{-(p_0-p_1)}.                    \tag{2}
\]
For bounded loop length and nonnegative exponents this tends uniformly to zero. This follows from \(p_0>p_1\), after fixing all constants. Exceptional radius indices require their recorded comparison; they are not silently replaced by \(j\). Equation (2) makes a pre-existing fractional margin sufficient. It creates no such margin.

## Round 1: can constrained energy imply an inward maximum principle?

This attack uses stationarity and the quadratic form directly, without estimating \(C_P(L)\).

At a flat real reference, fix a gauge slice and the remaining zero modes. Let \(X\) be the Wilson quadratic form on that space, and let \(Q\) be the actual linearized determining map. Retain the inverse hypotheses; a formal inverse is insufficient. If
\[
 G=(X+Q^{\mathsf T}Q)^{-1},\qquad
 B=GQ^{\mathsf T}(QGQ^{\mathsf T})^{-1},                 \tag{3}
\]
exist, CP12 Lemma 1 gives the constrained stationary extension \(a_*=Bw\). Indeed \(Qa_*=w\), and \(Xa_*\) lies in \(\operatorname{ran}Q^{\mathsf T}\). For any other \(a\) with \(Qa=w\), put \(v=a-a_*\). Then
\[
 \tfrac12 a^{\mathsf T}Xa-\tfrac12a_*^{\mathsf T}Xa_*
 =\tfrac12v^{\mathsf T}Xv\ge0,                          \tag{4}
\]
when \(X\) is nonnegative. The cross term vanishes because \(Qv=0\).

The desired estimate concerns individual readouts \(C_\tau a_*\), where \(C_\tau\) is the derivative at the flat field of the loop of \(M_-\). The weights are the *old* thresholds. Equation (4) controls the Wilson quadratic energy. Even a bound on the sum of squared readouts would not give an order-preserving projection or a contraction in their weighted maximum norm.

Here is a hand diagnostic of that missing implication. Minimize \((a_1^2+a_2^2)/2\) subject to \(2a_1+a_2=w\). Direct differentiation gives
\[
 a_*=(2w/5,w/5),\qquad
 P=BQ=\tfrac15\begin{pmatrix}4&2\\2&1\end{pmatrix}.
\]
This is an orthogonal projection, but \(P(1,1)=(6/5,3/5)\). Even its nonnegative entries do not make it a maximum-norm contraction. Positivity and energy minimization alone therefore cannot prove the needed implication.

The diagnostic also survives an arbitrarily small passing neighbourhood. Fix \(0<q<t\), put \(a_*=(t-q/2,(t-q/2)/2)\), and take
\(a=a_*+s(-1,2)\). The constraint is unchanged. For sufficiently small \(s>0\), both coordinates of \(a\) have absolute value below \(t\), and \(|a-a_*|\) is arbitrarily small. Yet \(a_{*,1}>t-q\). This is **not** a Wilson history. It disproves only the proposed deduction from convexity plus small fluctuation.

Could the actual operator supply the extra sign? CP12 Theorem 3 supplies absolute, exponentially decaying derivative bounds. Its proof, L80–113, retains the constraint multiplier and differentiates a saddle system. It supplies no entrywise sign for \(C_\tau B\), or old-threshold contraction. At curved backgrounds the multiplier-paired constraint Hessian remains. Dropping that term would change the problem. Even unconditional energy minimization is unavailable as a general shortcut: SA 9791 uses regular criticality at nonidentity data.

The scalar heat-kernel positivity in CP12 Lemma 5 does not repair this step. Formula (3) also contains \((QGQ^{\mathsf T})^{-1}\) and the curl readout. Their positivity-preserving properties do not follow from a positive scalar resolvent. The slowly weighted maximum argument actually available in a3-profile L616–666 gives \(r\le4C_0P\); it does not give coefficient one or an inward fraction in the old thresholds. SA 9658 and 9860–9867 allow the relevant constants to depend on \(L\).

**Exact failure of Round 1.** No sign or sharp weighted maximum bound has been established for the actual constrained curvature extension, including seam rows. The energy identity is proved, but the step from (4) to OT fails as an inference. The finite diagnostic does not refute OT.

## Round 2: an exact commuting-field witness

This attack tries to realize the shell by an explicit critical field. It does not tune an unspecified profile constant.

Work first on an embedded rectangular patch in one level's lattice units. Put \(T=\operatorname{diag}(1,-1)\) and
\[
 U_2(n)=e^{i\phi n_1T},\qquad U_1(n)=U_3(n)=U_4(n)=I.       \tag{5}
\]
Every positive \(12\)-plaquette is \(e^{i\phi T}\); all other plaquettes are identity. Use the exact average of SA QC1–QC3, L7957–7987, not an average of link matrices. On its small branch, the mean of commuting exponentials is the exponential of their mean angle: substitution in QC1 proves this identity, and the prescribed local uniqueness selects it.

For a block centre \(y\) and site \(x\), half the coordinate orders perform direction 1 before direction 2. Thus
\[
 U(y,x)=\exp\{i\phi(y_1+x_1)(x_2-y_2)T/2\}.              \tag{6}
\]
If either displacement vanishes, the same formula follows directly. Directions 3 and 4 contribute identity. Reversing a displacement gives the same expression by reversing the corresponding bonds.

For a coarse bond in direction 2, substitution in QC3 gives
\(Z_x=\exp[i\phi L(x_1-y_1)T]\). For direction 1 it gives
\(Z_x=\exp[-i\phi L(x_2-y_2)T]\). In directions 3 and 4, \(Z_x=I\). The centered block has zero mean displacement. Hence
\[
 \mathcal M(U)_2(y)=e^{i\phi Ly_1T},\qquad
 \mathcal M(U)_1=\mathcal M(U)_3=\mathcal M(U)_4=I.
\]
The coarse \(12\)-plaquette is therefore exactly \(e^{iL^2\phi T}\). Iteration has the same property whenever all the required branches and patches exist. CV changes the field by a real gauge, so it does not change these plaquette defects.

There is also an exact periodic realization of (5). Take integer periods \(N_\mu>4L+4\), with \(\phi N_1N_2\in2\pi\mathbb Z\). Keep \(U_2(n)=e^{i\phi n_1T}\), and set
\[
 U_1(n)=
 \begin{cases}e^{-i\phi N_1n_2T},&n_1=N_1-1,\\I,&n_1<N_1-1.
 \end{cases}                                             \tag{7}
\]
Keep directions 3 and 4 trivial and periodic. At the first-coordinate seam, the four factors give \(e^{i\phi T}\). At the corner seam they give \(e^{i\phi T}e^{-i\phi N_1N_2T}=e^{i\phi T}\). This checks every seam type. At each direction-1 or direction-2 bond, the two nontrivial contributions to the Wilson current are \(\sin\phi\,T\) and \(-\sin\phi\,T\). All contributions at the other bonds vanish. Thus the current is zero, including all colour directions. The field is an unconstrained critical point on this action torus, hence a constrained critical point for its own datum.

This statement is limited to that action domain. To identify its orbit with \(U_+(W)\), the imported regularity and uniqueness hypotheses must hold on the selected determining system. To use it in OT, one must also realize that system and datum in the actual history. Neither follows from zero current.

**The coarse test defeats the simplest candidate.** Let
\(f(\phi)=|e^{i\phi T}-I|=2|\sin(\phi/2)|\). Suppose an old plaquette and a coarse plaquette have recorded radius indices \(j,j+1\), and thresholds \(t,t_+\) with
\[
 \mathcal E_+\le\mathcal E_{\rm old}+1,\qquad
 \varepsilon_{j+1}\le2\varepsilon_j,
 \quad\text{so}\quad t_+\le2L_\flat^2t.                  \tag{8}
\]
Assume the coarse plaquette has its whole averaging carrier in the constant-field patch. For \(L^2|\phi|\le1\),
\[
 f(L^2\phi)\ge\tfrac34L^2 f(\phi).                      \tag{9}
\]
For completeness, \(1-\cos x\le x^2/2\) follows by two integrations of \(|\cos x|\le1\). Integrating \(\cos x\ge1-x^2/2\) gives \(\sin x\ge x-x^3/6\). Apply this at \(x=L^2|\phi|/2\le1/2\), and use \(f(\phi)\le|\phi|\), to obtain (9).

Write \(q=q_\tau\) for the old plaquette. By (2), a final ceiling can impose \(q\le t/4\) here. A shell candidate has \(f(\phi)>t-q\ge3t/4\). Equations (8)–(9) would then require
\[
 t_+>\tfrac9{16}L^2t,
 \qquad t_+\le2L_\flat^2t<\tfrac12L^2t,
\]
which is impossible. The last inequality uses the prescribed \(L_\flat<L/2\). This is a hand exclusion of this homogeneous candidate under the stated threshold comparison. It is not a universal proof of OT.

At inherited seams, (8) has not been proved for all the relevant carriers. ST1 L660–673 prescribes new exponents and retains inherited ones; (56) is only their upper envelope. Its proof explicitly keeps actual test support as input. Assigning a large coarse exponent by hand would not construct a permitted history. Conversely, imposing (8) at every seam without proving it would repeat the old FCON gap.

A second obstruction remains even when a local shell configuration is available. GEOH L19–56 requires a creation, a quiet interval, quarantine and a prepared nest for the actual operation. The periodic critical field supplies none of those recorded outcomes. Adding a local failure can change the determining data and their critical reference; their preservation would need proof. CP12's response estimate would control a change only along an already admitted construction; it does not provide the required history. DOM L275–315 likewise retains the curved localization rule and its quantitative chart as inputs.

**Exact failure of Round 2.** The exact field, current and average calculations are established. The homogeneous candidate is excluded when (8) applies. No seam candidate satisfying all actual threshold records, localization, creation and stage-selection conditions has been constructed. Thus there is no admitted-history counterexample.

## Round 3: fix the old cutoff boundaries during deformation

This attack retains the old indicators geometrically instead of replacing them by one. Temporarily suppose all the other factors have their required analytic extension and integrable majorant. This isolates the older-loop obstruction; it does not assume that obstruction away.

Let \(P_\tau(Z,W)=\partial D(Z,W)(\tau)\). On real data, \(P_\tau\in SU(2)\). Its eigenvalues are \(e^{\pm i\alpha}\), so
\[
 |P_\tau-I|^2=2-\operatorname{tr}P_\tau,\qquad
 \rho_\tau(Z,W)=t_\tau^2-2+\operatorname{tr}P_\tau(Z,W).
                                                               \tag{10}
\]
The function \(\rho_\tau\) has a holomorphic extension. The indicator is its real inequality, not its analytic continuation. At fixed real \(W\), the remaining real domain is
\[
 \Omega(W)=D_b\cap\bigcap_\tau\{\rho_\tau(Z,W)>0\}.         \tag{11}
\]

A compactly supported deformation inside this domain works. Write the holomorphic density as \(F\), choose a real vector \(\nu\), and choose smooth \(\psi\) compactly supported in \(\Omega(W)\). Keep
\(H_s(Z)=Z+is\psi(Z)\nu\), \(0\le s\le1\), inside the analytic tube. Its Jacobian is \(1+is\partial_\nu\psi\). The chain rule gives the exact identity
\[
 \frac{d}{ds}\{F(H_s(Z))(1+is\partial_\nu\psi)\}
   =\partial_\nu\{i\psi(Z)F(H_s(Z))\}.                  \tag{12}
\]
The right side integrates to zero, because its primitive has compact support in \(\Omega(W)\). Differentiation under the integral is justified by the tube bound on that compact support. Thus the integral is unchanged. No regularity of the remote boundary is needed. This proves a fixed-real-datum contour identity while keeping every old indicator.

Two required steps remain. First, FC9's translation equals the prescribed centre shift on its central region. If an old boundary passes through that region, a deformation vanishing there cannot also be that translation. A displacement tangent to each boundary could be an alternative, but the required common tangency is not supplied. Second, (12) is at fixed real \(W\). The domain (11) and a cutoff adapted to it need not depend analytically on \(W\). FCON's real tie requires the actual value at every real datum in use, not only at regular chambers.

Here is a three-dimensional contact calculation. It has the dimension of one free colour row. For \(b>0\), set
\[
 J(x)=\int_{|z|<b}\mathbf1_{\{z_1<b-x\}}\,d^3z.
\]
For \(x\le0\), \(J(x)=4\pi b^3/3\). For \(0<x<2b\), integrate the transverse discs to obtain
\[
 J(x)=\tfrac43\pi b^3-
 \int_{b-x}^{b}\pi(b^2-s^2)\,ds
 =\tfrac43\pi b^3-\pi b x^2+\tfrac\pi3x^3.              \tag{13}
\]
The second derivative jumps from zero to \(-2\pi b\) at zero. Hence even an entire density and analytic cutoff surface can give a nonanalytic parameter integral when the old surface touches the new boundary. This is a local integration example, not a Yang–Mills history. It shows precisely what a proposed analytic domain trivialization must exclude or otherwise handle.

**Exact failure of Round 3.** Equation (12) proves a deformation only at fixed real data. No uniform analytic trivialization or contact cancellation for the actual old-cutoff domains has been established. It therefore supplies neither frozen FC-test nor a substitute with the required joint continuation. This differs from indicator splitting: the old factors were never discarded, and the fixed-datum deformation actually holds.

## Source record and recovery checkpoint

SA and CA-I were each fetched once at 31a47c543775, to the two requested /tmp paths. Their line counts are 32,992 and 166,711. SHA-256 identities are:

    SA    d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f
    CA-I  4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93

The source excerpts supporting the note were read after their index rows and neighbouring rows:

| Object | Checked source range | Use and limitation |
|---|---|---|
| Actual two means and averaging map | SA 7931–8000; index chunk 07 L193–201 | Definitions used in (5)–(9); no many-level analytic theorem inferred. |
| Critical orbit, CV, profile | SA 9658–9684, 9791, 9860–9867; chunk 09 L50–64, L128–137 | Regularity/criticality and sketched profile; no coefficient-one maximum principle imported. |
| New-test implication | SA 17317–17325, 17369–17396, 17612–17630; chunk 16 L24–50, L83–108; obligations L908–938 | The graded curvature argument belongs to SA's tests. |
| Transfer of stage bounds | CA-I 54985–55003; CA index chunk 10 L108–126 | The stage theorem is an explicit premise. |

The existing [lit-balaban.md](lit-balaban.md) search record was reused. A targeted local reading of the owner's OCR copies covered CMP 119, text L1160–1225, and CMP 102, text L895–917. They concern the old-test comparison and constrained minimization respectively. The OCR has damaged formulas; no proof step or quotation here relies on reconstructing those formulas. Tadeusz Bałaban is credited for the underlying background and stage methods. The SA/CA constructions are credited above to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

The frozen local passages used are ST1's definitions and imports, (56)/(58), F2–F6, CV, FC1–FC2 and Theorem 14; GEOH's history/preparation definitions and relative row contract; DOM's background imports and localization/stage section; CP12's multiplier, derivative and scalar-regularity statements; IN1's constant table and Amendment 1. FCON was read whole, and fcon-draft §4.6 was read with its stronger assertions corrected by the distillation. These imports retain their own qualifications.

**Recovery state.** The three new attacks are complete at the limits stated above. None proves OT or supplies an admitted-history counterexample. A next attempt must control the actual constrained reference at inherited seams, or construct a fully supported history realizing (1). A successful variational argument must bound the actual curvature readout, not just its energy. A contour alternative must prove continuation through every admitted parameter value. Repeating the previous three FCON attacks without their missing inputs does not change this state.

Only library/ot.md was written. No frozen text, stage test, audit, ledger or editable prompt file was changed. The arguments are by Codex and have not been checked by another provider. No numerical or computer-assisted proof step was used.

## Result at the end of Round 3

**Open lemma**

For the unchanged ST-test, prove the following uniform separation statement. With FCON's import package H and actual stored-stage conventions, choose the constants in IN1 order, including Amendment 1. After the permitted choices of late parameters, there is a single coupling ceiling such that every admitted finite history, every passing level-\(j\) stage, every real datum \(W\) in use, and every older type-(58) level-\(j\) loop \(\tau\) reading a moved row satisfy
\[
 \boxed{
 |\partial M_-(U_+(W))(\tau)-I|
 \le
 6C_{\rm sm}L^4L_\flat^{2\mathcal E_{\rm old}(\tau)}
      \varepsilon_{m_{\rm old}(\tau)}
 -\tfrac98 n_\tau C_{\rm ch}L^4\delta'_j .}
\]
The structural constants precede \(\kappa\) and are independent of \(M,\bar\kappa\), volume and history. The final ceiling may depend on the permitted late parameters. Each loop retains its own old exponent and radius index, including inherited and seam cases.

The three new failures are exact: constrained energy gives no old-threshold maximum contraction; the explicit commuting field fails the comparable coarse test and has no realized seam history; cutoff-preserving deformation gives no joint analytic continuation through parameter contacts. This leaves **Lemma OT itself open**, with no additional lemma represented as a closure. FCON's separate complete-factor and majorant obligations also remain. This is an attempted proof of a missing step for our revised tests, not a correction of the Sussman–Alpoge text and not an audit result.

## Continuation at 4df934dd7: Rounds 4–6

Provenance: further research text by Codex. The exact runtime model identifier and effort setting are not exposed here. This continuation preserves Rounds 1–3 and their qualifications. It grants no status and is not an audit. Credit remains with Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the source constructions. The arguments added below are by hand.

**Source checkpoint.** The checkout is still `4df934dd7b12e8ba71ada97b7ae8a406511d5c85`. The incoming, untracked `ot.md` had SHA-256 `0ca7c16bccb5e74c59e6511f61069ca4d2f2681e2996f7c515b1a36000dd0f4b`; a copy is at `/tmp/ot-continuation-4df934dd7/ot.before.md`. SA and CA-I were each fetched once for this continuation. Their hashes and line counts agree with the preceding source record. The requested workflow file remains absent from this checkout. No replacement workflow, audit, or backlog process was run.

The index rows and neighbouring rows were read before the new source excerpts. SA 17369–17396 and 17612–17630 still give a **sketch for SA's own tests**. In particular, SA 17624 explicitly requires a graded bound on the background curvature. CA-I 54985–55008 assumes the stage theorem. Neither source passage establishes the implication for the revised free-row ST-test. This is a continuation on our missing implication, not a correction of their text.

## Round 4: recover a margin from the birth record

This attack follows an old test backwards through its actual record. It tries to use quarantine, the overlap assignments, and the analytic radius reserve instead of a new profile constant.

**A pointwise assignment comparison does hold.** Keep the original layer \(l(x)\) and the operation's \(k_\sharp\) fixed. On points to which ST1 L654–660 applies, its formula is
\[
 e_j(x)=(j-\max\{l(x),k_\sharp\}-1)_+.
\]
For \(j\le k_\sharp\) this is zero. For \(j>k_\sharp\) it is precisely the relevant second or third case. Therefore
\[
 0\le e_{j+1}(x)-e_j(x)\le1.                         \tag{C1}
\]
Indeed the map \(v\mapsto v_+\) is increasing and changes by at most one when its argument increases by one. If two assignments at this same point are both fresh, \(\mathcal E_j=e_j+1\), and both radius indices are their respective stage levels, their threshold weights obey
\[
 \frac{L_\flat^{2\mathcal E_{j+1}(x)}\varepsilon_{j+1}}
      {L_\flat^{2\mathcal E_j(x)}\varepsilon_j}
 \le 2L_\flat^2.                                    \tag{C2}
\]
Here the factor two is ST1's adjacent radius comparison, after its final ceiling. This is a comparison of two fresh assignments at the same point. It is not a comparison between every pair of old and new loop stencils.

There are two obstacles to extending (C2). ST1 L660 inherits all other exponents. Also L669 takes the minimum over a loop's **complete test stencil**. A new coarse loop and an old loop do not have the same stencil. Equation (20), ST1 L237–254, compares layers within one supplied separated sequence. It does not identify the birth sequence of a frozen record with the present determining sequence. SA 17440 explicitly distinguishes the action sequence governing carried tests from the determining sequence governing the current background. SA 17449 also permits later coverage of a healed location. GEOH L28–34, L76–80 and L89–95 retain these distinctions. Quarantine alone therefore gives no missing identification of the two threshold records.

**Transport of a birth margin has an exact budget.** Suppose one frozen test is evaluated successively at real references \(V_0,\ldots,V_s\). Keep its threshold \(t\), its complete read, and its stored transports fixed. Let
\[
 f_a=|\partial V_a(\tau)-I|,\qquad
 |f_{a+1}-f_a|\le d_a.
\]
Unitary comparison may be made in any consistent real gauge. Telescoping gives
\[
 t-f_s\ge (t-f_0)-\sum_{a<s}d_a.                    \tag{C3}
\]
Thus a birth estimate \(t-f_0\ge q_\tau+\sum d_a\) would suffice. Positive birth slack alone does not suffice. For \(0<q_\tau<t\), the scalar values \(f_a=t-q_\tau/2\) have zero transport cost and positive passing slack, but fail the desired margin. This is a diagnostic of (C3), not a history counterexample.

The analytic coefficient debt in ST1 (17)–(18) does not supply this birth estimate. It shrinks radii of analytic records. The threshold in (58) has no such coefficient. More quantitatively, at an ordinary radius index \(m\), the largest threshold allowed by (56) is at most
\[
 C_{\rm te}C_R^2\ell_m^{2r_R}\varepsilon_m,
 \qquad
 \frac{r_0(m)}{C_{\rm te}C_R^2\ell_m^{2r_R}\varepsilon_m}
 =\frac{C_0}{C_{\rm te}C_R^2A_0}
       \ell_m^{q-p_0-2r_R}\longrightarrow\infty.      \tag{C4}
\]
The exponent is positive by Tq0. Fixed fractional room in this larger analytic radius is consistent with arbitrarily small slack in the real test. No exceptional radius index is identified with \(m\) in (C4).

**Exact failure of Round 4.** Equations (C1)–(C3) are proved. The history and radius arguments give neither a loopwise birth buffer nor the cross-record threshold identification needed to use it. This failure is prior to summing response tails. Making those tails smaller cannot create the absent birth buffer. It does not prove that the actual histories lack such a buffer; proving it from their actual tests remains necessary.

## Round 5: an oscillating critical field with the actual average

The constant-field candidate in Round 2 could not cancel its coarse curvature. This attack uses alternating coarse data and solves the nonlinear critical equation. It works on a uniform one-step system, not on a prepared seam.

Use unit fine spacing and \(L=2h+1\). Take a periodic cubic lattice whose period is an even multiple of \(L\) greater than \(4L+4\). Put \(T=\operatorname{diag}(1,-1)\). For a real function \(f\) of the first coordinate set
\[
 U_2(n)=e^{if(n_1)T},\qquad U_1=U_3=U_4=I.             \tag{C5}
\]
All statements use sufficiently small angles on the prescribed branches.

**Exact block calculation.** The actual QC1–QC3 means give
\[
 U(y,x)=\exp\!\left\{\tfrac i2(x_2-y_2)
                   [f(y_1)+f(x_1)]T\right\},
 \qquad
 (\mathcal M U)_2(y)=e^{iL\bar f(y_1)T},              \tag{C6}
\]
where \(\bar f(mL)=L^{-1}\sum_{r=-h}^h f(mL+r)\). The other coarse bonds are identity.

To verify the first formula, half of the coordinate orders place direction 1 before direction 2, and half place it after. Their two angles are \((x_2-y_2)f(x_1)\) and \((x_2-y_2)f(y_1)\). The commuting contour mean is their arithmetic angle mean. If a displacement vanishes the formula gives the same value directly. For a direction-2 coarse bond, QC3's closed angle is \(L[f(x_1)-f(y_1)]\). For a direction-1 coarse bond it is
\[
 \tfrac12(x_2-y_2)
 [f(y_1)+f(x_1)-f(y_1+L)-f(x_1+L)].
\]
The latter averages to zero over the centred transverse coordinate. Directions 3 and 4 cancel directly. This proves (C6), using both of SA's different means. Their definitions were checked at SA 7957–7987.

**An exact critical solution.** For \(0<\lambda L/2<1\), define, for \(0\le r\le h\),
\[
 f_\lambda(r)=\tfrac12\arcsin(\lambda L/2)
       +\sum_{s=r}^{h-1}\arcsin\!\bigl(\lambda(s+\tfrac12)\bigr).
                                                               \tag{C7}
\]
Set \(f_\lambda(-r)=f_\lambda(r)\), then extend by
\(f_\lambda(n+L)=-f_\lambda(n)\). These prescriptions agree at each block interface. Write
\(p_n=f_\lambda(n+1)-f_\lambda(n)\). On the block centred at zero, including its right outgoing edge,
\[
 \sin p_n=-\lambda(n+\tfrac12),\qquad -h\le n\le h.   \tag{C8}
\]
At the right interface, \(p_h=-2f_\lambda(h)=-\arcsin(\lambda L/2)\), which checks the endpoint. Reflection checks the negative indices. On block \(m\), every sign is multiplied by \((-1)^m\). Hence at each site of that block
\[
 \sin p_{n-1}-\sin p_n=\lambda(-1)^m.                \tag{C9}
\]

The field (C5), (C7) is critical for the Wilson action under **all** its prescribed coarse-bond constraints. Here is the first-variation check, including directions outside the ansatz. For a diagonal variation \(a\), the only nonzero action current is the direction-2 current (C9). The direction-1 current cancels by translation in direction 2; the other plaquettes are identity. For such variations, the differential of the actual average is the plain Abelian map
\(P_L=S_L-d_L\sigma\), with \(S_L\) as in SA 8467–8493. This also follows directly by differentiating the additive angles in QC1–QC3. Summing over all transverse coarse sites at a fixed block index \(m\) gives
\[
 \sum_{y_\perp}(P_La)_2(mL,y_\perp)
       =L^{-3}\sum_{n_1=mL-h}^{mL+h}\sum_{n_\perp}a_2(n).
                                                               \tag{C10}
\]
The coarse gradient telescopes in direction 2. The centred transverse blocks tile their three periodic coordinates. The length-\(L\) segment sum counts each direction-2 bond \(L\) times, leaving \(L/L^4=L^{-3}\). Thus the action derivative is the constraint derivative paired with multipliers \(L^3\lambda(-1)^mT\) on coarse direction-2 rows, and zero on the other rows.

An off-diagonal colour variation gives zero on both sides of this identity. Conjugation by \(\operatorname{diag}(i,-i)\) fixes the background and negates every off-diagonal variation. The action is invariant. QC1's locally unique mean, QC3 and their logarithms are conjugation covariant, so their derivatives send this variation to an off-diagonal matrix. Its pairing with \(T\) is zero. Therefore the multiplier identity holds for every real bond variation. In particular the derivative vanishes on the kernel of the full determining derivative. This proves constrained criticality, not merely criticality within (C5).

For each fixed \(L\), the field tends uniformly to identity as \(\lambda\to0\). Subject to A1/F0/REG on this uniform torus system, regular uniqueness identifies its orbit with the canonical critical orbit for its own datum. CV changes no loop defect. This identification is conditional on that imported theorem; it does not construct a prepared operation history.

**Its curvature ratio leaves a margin.** Let
\[
 A(\lambda)=L^{-1}\sum_{r=-h}^h f_\lambda(r),\quad
 F(\lambda)=2\sin\!\left[\tfrac12\arcsin(\lambda L/2)\right],\quad
 G(\lambda)=2\sin(LA(\lambda)).                       \tag{C11}
\]
Here \(F\) is the largest fine plaquette defect. Every coarse \(12\)-plaquette has defect \(G\), for small positive \(\lambda\). Differentiating the finite sum (C7) at zero gives
\[
 \left.\frac{d f_\lambda(r)}{d\lambda}\right|_0
       =\frac{L^2+1}{8}-\frac{r^2}{2},\qquad
 A'(0)=\frac{L^2+2}{12}.
\]
For the last equality use
\(L^{-1}\sum_{r=-h}^h r^2=h(h+1)/3=(L^2-1)/12\).
The square-sum identity follows by induction from the increment \(h^2\); no enumeration is used. Independently, the displayed quadratic has discrete second difference \(\lambda\), its outgoing slope is \(-\lambda L/2\), and its block mean is \(\lambda(L^2+2)/12\). This checks the linear coefficient against (C8)–(C9). Consequently
\[
 \lim_{\lambda\downarrow0}\frac{F(\lambda)}{G(\lambda)}
                      =\frac{3}{L^2+2}.              \tag{C12}
\]
All limits here follow from differentiable finite expressions, with nonzero denominator derivative.

Suppose the old and coarse thresholds in a proposed use of this field have own-level indices and \(\mathcal E_+\le\mathcal E_{\rm old}+1\). Bounded adjacent frame increments give \(\varepsilon_{j+1}/\varepsilon_j\to1\) uniformly above the coupling floor: both \(\theta_{j+1}/\theta_j\) and \(\log\theta_{j+1}/\log\theta_j\) tend to one. Thus a final ceiling gives
\[
 t_+\le\tfrac{17}{16}L_\flat^2t,\qquad
 F/G\le\tfrac{17}{16}\frac{3}{L^2+2}.
\]
If the coarse test passes, then
\[
 F<\left(\tfrac{17}{16}\right)^2
          \frac{3L_\flat^2}{L^2+2}\,t
   <\frac{867}{1024}t<\frac78t.                     \tag{C13}
\]
Only \(L_\flat<L/2\) was used in the second inequality. The old margin ratio (2) permits \(q_\tau\le t/8\). Equation (C13) then gives OT for those tested loops of this field. The ceilings follow the fixed structural choices; no new choice of \(L\) follows a profile constant.

**Exact failure of Round 5.** This alternating solution is also excluded as a shell witness under the stated threshold comparison. Its nonlinear criticality and ratio are established. The proof uses complete periodic transverse sums in (C10) and a uniform determining map. Restricting those sums to a prepared region can leave interface terms, and its determining rows include retained finer data. The same multiplier calculation therefore does not establish that the restriction is the critical field of that mixed system. Neither (C12) nor (C13) bounds arbitrary modes or supplies the missing inherited threshold comparison. This is a new exact test case, not a proof of OT on general histories.

## Round 6: lift linear saturation and supply its history

This attack separates two issues: whether nonlinear corrections can destroy a prospective shell witness, and whether its datum can occur in a complete history. It then tries a fibre-preserving insertion to supply the latter.

**Quadratic errors are smaller than the requested shell.** For an own-level loop with at least one moved occurrence, (56) and the definitions give
\[
 \frac{t_\tau^2}{q_\tau}
 \le C\frac{A_0^2}{A_1}
       e^{-\ell_j/2}\ell_j^{\,2p_0+4r_R-p_1}
       \longrightarrow0.                              \tag{C14}
\]
Here \(C=C_{\rm te}^2C_R^4/[(9/8)C_{\rm ch}L^4]\) is an early constant; the amplitudes remain visible. To see this, square the bound
\(t_\tau\le C_{\rm te}C_R^2A_0g_j\ell_j^{p_0+2r_R}\),
divide by \(q_\tau\ge(9/8)C_{\rm ch}L^4A_1g_j\ell_j^{p_1}\), and use \(g_j=e^{-\ell_j/2}\). For any fixed real power \(b\), choose an integer \(N>\max\{b,0\}\). The series inequality \(e^{x/4}\ge(x/4)^N/N!\) bounds \(e^{-x/2}x^b\) by \(4^NN!e^{-x/4}x^{b-N}\), which tends to zero. This proves the limit by hand. The same conclusion allows any additional fixed polynomial factor in \(\ell_j\). Exceptional indices need their own comparisons; (C14) does not cover them automatically.

**Conditional shell-lifting criterion.** Consider a family of specified determining systems with flat real data \(W_\nu(0)\) and real analytic datum paths \(W_\nu(a)\). Include their actual CV critical maps. Suppose, on \(|a|<r\), the old loop has a holomorphic logarithm
\[
 R_\nu(a)=i^{-1}\Log\partial M_{-,\nu}
                     (U_{+,\nu}(W_\nu(a)))(\tau_\nu),
 \quad R_\nu(0)=0,
\]
with
\[
 R_\nu(a)=aH_\nu+E_\nu(a),\qquad
 |E_\nu(a)|\le C_2|a|^2,qquad
 0<A_*\le |H_\nu|\le A^*.                            \tag{C15}
\]
The disc, bounds and nonzero lower bound must be uniform in this family. If they are used as structural estimates, they must have IN1's early uniformity. Analyticity for one finite system supplies only a system-dependent version. For example, a uniform bound \(|R_\nu|\le B\) on the disc gives \(C_2=2B/r^2\) on its half-disc: Cauchy's coefficient bound and the geometric series bound the sum of terms of degree at least two. This implication does not itself supply the uniform disc or a suitable direction \(H_\nu\).

Suppose the actual thresholds satisfy \(t_\nu\to0\), \(q_\nu/t_\nu\to0\), and \(t_\nu^2/q_\nu\to0\). Set
\[
 a_\nu=\frac{t_\nu-q_\nu/2}{|H_\nu|}.                 \tag{C16}
\]
For all sufficiently large \(\nu\),
\[
 t_\nu-\tfrac34q_\nu
 <|\partial M_{-,\nu}(U_{+,\nu}(W_\nu(a_\nu)))(\tau_\nu)-I|
 <t_\nu-\tfrac14q_\nu.                              \tag{C17}
\]

*Proof.* On real paths the logarithm is traceless Hermitian. Its norm changes from \(a_\nu|H_\nu|\) by at most \(C_2a_\nu^2\). For a small nonnegative \(x\), integration of \(1-\cos(x/2)\le x^2/8\) gives
\(0\le x-2\sin(x/2)\le x^3/24\).
The \(SU(2)\) defect is \(2\sin(|R_\nu|/2)\). Thus its difference from \(t_\nu-q_\nu/2\) is bounded by \(C_3t_\nu^2\), with \(C_3\) depending only on (C15). The three threshold limits make \(a_\nu<r/2\) and \(C_3t_\nu^2<q_\nu/4\). This proves (C17). ∎

This is a quantitative lift, not a counterexample. It shows that a uniformly controlled, linearly saturated reference could be placed in the **passing** half of the old shell. It also shows how strict slack in other loop tests survives: if their normalized linear readouts have a fixed fractional slack, their \(O(t_\nu^2)\) errors and the \(O(q_\nu/t_\nu)\) radial adjustment cannot remove it, provided those thresholds are uniformly comparable to \(t_\nu\). Actual failed tests, stored variables, gauge factors and stage selection still require their own support checks. A direction satisfying only the new coarse plaquette tests is insufficient.

**The local fibre can change a stage outcome while keeping its datum.** There is a concrete insertion to try. Fix an admitted real datum and a free removed row \(e\). Strengthen the final chart ceiling to
\[
 2\delta'_j<r_u,\qquad
 2C_{\rm ch}L^4\delta'_j+\delta'_j/8<r_{\rm sol}/4.
                                                               \tag{C18}
\]
At \(u=0\), the field is \(D=V\) and passes the new free-row test. At \(u_e=2\delta'_jT\), with other free coordinates zero, F2 gives an exact field on the **same** fibre: \(F(D)=W\). On this free row \(D_e=e^{2i\delta'_jT}V_e\). By LOC and the real group triangle inequality,
\[
 d_G(D_e,V_e^\sharp)
 \ge2\delta'_j-d_G(V_e,V_e^\sharp)
 \ge\tfrac{15}{8}\delta'_j>\delta'_j.                 \tag{C19}
\]
Thus it fails the new test. Equation (C18) keeps every removed row inside the full-coordinate neighbourhood. Both conclusions are strict and persist on small open free-coordinate sets. F2 and the positive real coarea density prove these local statements. They do not prove that the complete carried integrand is nonzero on either set.

Why this insertion does not finish the history is specific. It supplies a failure of a **preparatory stage** only after a component has already entered the operation class. GEOH starts with an empty live region (L19–26). Its first creation, the ensuing quiet window, its quarantine and its prepared nest still have to be realized. Using (C19) as the first creation would assume the class operation that the construction was meant to produce. Using it later also requires every carried old factor to remain nonzero; the fibre equation does not establish that. No such complete sequence of test outcomes has been supplied by this insertion.

There is also a quantifier that a fixed finite example cannot evade. For the frozen class,
\(N_t=R_t\ge(\log X_0)^r\), and an operation requires \(t-N_t\ge1\) (GEOH L9–30). Therefore histories with any fixed upper bound on their length contain no such operations when \(X_0\) is sufficiently large. A counterexample to the existence of a common weak-coupling ceiling must occur at arbitrarily small admissible couplings, with growing class windows. Scaling a field in one fixed geometric history towards identity does not supply that family. The threshold calculation (C14) is uniform; the needed history realization is not obtained from it.

**Exact failure of Round 6.** Nonlinear error is not the obstacle for a candidate satisfying (C15) and the threshold limits: (C16)–(C17) place it in the shell. The unresolved step is a direction and a family of complete admitted histories satisfying all the other tests at those parameters. The fibre-preserving failure construction does not seed the class from the empty history and does not preserve arbitrary carried factors. The alternating family in Round 5 has a strict inward margin instead of the required saturation. No admissible shell direction, with its full history support, has been constructed.

## Continuation source record and current checkpoint

The new source reads were bounded excerpts, after their index rows and neighbours:

| Source | Checked lines | Use |
|---|---|---|
| SA; index chunk 07 L193–201 | 7931–7992 | Actual two means and the embedded double-block convention in (C5)–(C6). |
| SA; index chunk 08 L18–25 | 8465–8530 | Plain derivative, straight sums and gradient cancellation used in the independent first-variation check. |
| SA; index chunk 16 L43–48, L98–100 | 17369–17398; 17612–17630 | Sketched old-test implication and the additional graded background tests. |
| SA; index chunk 16 L51–58 | 17433–17449 | Distinct action/determining sequences, record birth and later coverage of healed places. |
| CA-I; its index chunk 10 L108–126 | 54985–55008 | The assumed stage theorem; no converse admission implication. |

The corresponding obligations entries at L908–938 were read. The existing `lit-balaban.md` search record was reused, and the scoped paper-folder README was checked. No damaged OCR formula was used. Conditional orbit identification retains A1/F0/REG; the other new calculations are explicit hand arguments. The old source credit includes Tadeusz Bałaban's background and stage methods. The new exact Abelian calculation uses SA's actual map.

Local checked passages include FCON in full and fcon-draft §4.6; ST1 definitions/imports, (17)–(22), (56)/(58), Lemma 12, F2, the exact real coarea formula, FC1–FC2 and Theorem 14; GEOH's class, preparation, record and relative-row definitions; DOM's imports and LOC/stage section; CP12 §§1–2; and IN1 rows 1–10 with Amendment 1. Source statements remain qualified by their imports. In particular, DOM's localization rule and GEOH's actual realization are not inferred from the algebraic examples.

**Current recovery state.** Three further attacks are complete. Keep (C1)–(C4), the exact oscillating constrained critical field (C5)–(C13), the quadratic-error estimate and conditional shell lift (C14)–(C17), and the same-fibre stage-outcome calculation (C18)–(C19). None settles OT. The next decisive work must provide an actual inherited/seam threshold barrier, or a complete family of histories realizing a saturated reference. A periodic mode calculation alone cannot supply either. The frozen integrand-accounting and analytic-majorant obligations remain separate.

Only `library/ot.md` was edited. The incoming proof text was preserved; its Result heading was dated to Round 3. No frozen file, stage test, audit, ledger or editable prompt file was changed. No platform instruction was modified. Source retrieval and file comparisons were bookkeeping. No numerical run, machine enumeration or computer-assisted proof step was used. The continuation has not been checked by another provider.

## Result

**Open lemma**

For FCON's import package H and the unchanged ST-test, prove the uniform older-test separation below. Choose structural constants in IN1 rows 1–10, with Amendment 1, before \(\kappa\), independently of \(M,\bar\kappa\). After the permitted late choices there must be one coupling ceiling such that, for every admitted finite history, passing level-\(j\) stage, real datum \(W\) in use, and older type-(58) level-\(j\) loop \(\tau\) reading a moved row,
\[
 \boxed{
 |\partial M_-(U_+(W))(\tau)-I|
 \le 6C_{\rm sm}L^4L_\flat^{2\mathcal E_{\rm old}(\tau)}
              \varepsilon_{m_{\rm old}(\tau)}
       -\tfrac98 n_\tau C_{\rm ch}L^4\delta'_j .}
\]
Every loop keeps its recorded exponent, radius index and complete read, including inherited and seam cases. The final ceiling may depend on permitted late parameters; the structural constants may not depend on history or volume.

The three new attacks fail at different steps. Birth-record transport lacks the actual birth buffer and cross-record threshold match. The oscillating critical field has a strict margin in its uniform system, while its periodic multiplier proof does not cover a mixed seam. The quantitative shell lift lacks a direction and complete admitted histories on which all other tests retain support; a same-fibre stage failure does not create the required initial class history. **OT remains open, with no admitted-history counterexample.** This is research on a missing implication for our revised tests, not a correction of the Sussman–Alpoge text and not a grant of scientific status.
