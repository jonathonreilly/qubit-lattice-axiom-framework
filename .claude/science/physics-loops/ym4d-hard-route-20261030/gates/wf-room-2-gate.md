# Gate of `wf-room-2.md` — queue row 125
Provenance: OpenAI Codex (GPT-6), effort xhigh (row-125 assignment); checkout `4d90efd101038e8af38b939549f763010ef4670f`; Sussman–Alpoge outline `31a47c543775`; research text, not an audit, granting no status.

Scope: every section of `library/wf-room-2.md`, with rows 113, 116 and 125 and `wf-room.md` §§5–7, 9 read first. Source line numbers below refer to this pinned checkout; SA line numbers refer to the outline fetched once into `/tmp/sa_ym4.tex`. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's maps, statements and analytic mechanisms used below; credit Tadeusz Balaban for the background/domain constructions. All mathematical checks below are hand arguments. File searches and source retrieval supply no mathematical discharge. The entry-point workflow file is absent in this checkout; no replacement checkout or planning state is used.

## 0. Result — WRONG as a completion claim

First failing claim: line 24 says (O1) holds at s=1 for the specified lift; the cited theorem does not identify or bound that lift (Defect 1 below). The universal claim about non-unitary raw representatives (lines 25, 377, 381) is also false; the endpoint and removed-map arguments require checks beyond their displayed algebra. Thus the remaining items have not been reduced to the listed inputs. The detailed section verdicts and repairs below replace this summary. No conclusion here changes a ledger or scientific status.

## 1. Inputs and their standing — CORRECT-NO-ADVANCE

Read the displayed statements as hypotheses, preserving their dependencies. None fails merely as a declared hypothesis. In particular (T4) is an estimate on the full complex datum ball, (6.2) is a real profile estimate, and neither is an independent-current theorem for decoupled parameters. The local-scale inequalities require separated sequences, the stated torus floors, and omission of inward bonds throughout. References to a previous gate are not proofs supplied by this report.

## 2. Counterexamples first — CORRECT-NO-ADVANCE, with corrections

**C1.** The scale obstruction is real. On an abelian constant-flux patch, a level-p plaquette has angle \(\Theta=c\alpha_{0,r}L^{2(p-r)}\), whereas the proposed weaker clause allows at most \(C\alpha_{0,r}L^{p-r}\). Choose an integer \(d=p-r\) with \(cL^d>2CC_1\), then choose \(\alpha_{0,r}>0\) so small that \(c\alpha_{0,r}L^{2d}<\pi/100\). These choices explicitly avoid the discrete-scale issue in line 48. A background satisfying the claimed fine curvature clause would, by the local curvature-of-averages bound, have coarse angle at most \(CC_1\alpha_{0,r}L^d\); the exact averaging constraint contradicts this. This refutes universal simple-to-tower admission for unrestricted \(Z\), not an already imposed core clause.

The first literal error is line 46, “others trivial”: a cutoff depending on \(x_3,x_4\) also produces \(32\)- and \(42\)-curvature. Repair: define abelian links by line integrals of the displayed compactly supported potential; bound **all** components of \(dA\) by \(C\phi_0\), using a cutoff with \(|\nabla^m\chi|\le C_m\xi_p^{-m}\), \(m=1,2\). The central patch still has exactly constant \(12\)-flux. Enlarge the patch by the fixed averaging-carrier diameter if necessary. On each local contractible cube, the axial primitive has size at most its diameter times \(C\phi_0\), giving the stated simple conditions after reducing \(c\). Cutoff plaquettes therefore do not defeat the counterexample. The example requires a sufficiently large layer patch and torus, which an unrestricted uniform assertion must allow.

**C2.** Correctly labelled a failed estimate, not a counterexample. The displayed crude derivative really leaves one factor \(\lambda(x)^{-1}\). A special pure-gauge direction cannot establish a bound for general directions; §§4.5–4.7 must do that work.

**C3.** Correct specification gap: R9 and SA 10360–10428 do not give the first-system multiplier formula. Algebraically the difference of the two proposed readouts is \(T^{\mathsf T}\lambda\). Replace “whenever” both factors are nonzero by “when \(T^{\mathsf T}\lambda\ne0\)”; two nonzero factors need not have a nonzero product. Nonuniqueness of an off-shell extension also follows directly: adding a holomorphic term vanishing on the physical current graph leaves physical exactness unchanged.

**C4.** ADVANCE as a refutation of the **raw logarithm** endpoint bound. Choose two adjacent node values with a fixed small nonzero unitary relative angle, avoiding the logarithm cut. The input is flat and satisfies arbitrarily small simple radii in its real gauge, but its raw datum logarithm has that fixed angle. Thus no bound \(C_BMa\tau\) is possible uniformly as \(a\downarrow0\). This says nothing against a gauge-adjusted datum or the pair's membership in the real-gauge-invariant core.

## 3. Layered quantifier — CORRECT-NO-ADVANCE

No failure in the proposed **definition** (LQ) or its unit conversion: multiplying the R6 curvature inequality by \(\xi_j^2/\eta^2\), and its level-n current inequality by \(\xi_j^2/\xi_n^2\), gives \(a_0L^{j-p}\) in both cases. A radius \(a_0\) in (3.1) is stronger. Also \(T'_q\subset Z\subset\Omega_p\subset\Omega_q\) for \(q\le n\le p\), so \(\xi'\le l\).

C1 proves that an unrestricted universal quantifier cannot work. It does not prove that (LQ) is the unique necessary repair, nor does SA 5(b)'s memberwise containment hypothesis literally require \(Z\subset\Omega_p\) in every possible assignment. Replace “necessary” by “a sufficient geometric restriction which excludes C1.” Sufficiency **for analytic admission** still depends on Theorem L; compatibility with healed labels and every preceding structure is expressly open at line 78. The definition alone grants no closure.

## 4. Localised complex layered estimate — ADVANCE as an implication

### 4.1 Statement — ADVANCE, conditional

No failing mathematical step found, with the small-radius bookkeeping in §4.7 below. The output current is normalized by \(l^2\xi'\), not \(l^3\). Existence on a ball means the continuation of the fixed real regular datum; bounds by \(K_L(a_0+a_1^2)\) are asserted only under (H). The theorem retains the real-profile, averaging, full-polydisc response, representative and separated-geometry inputs of §1.

### 4.2 Lemma A′ — ADVANCE, conditional

No failure found. Here is the local bootstrap with its scales explicit. On the carrier of a level-q row set \(s=\xi_q\) and \(A=\sup_{P(c)}|w|\). All intermediate scales satisfy \(t_m\le s\), with \(\sum_m t_m\le C_Ls\) and \(\sum_m(t_m/l)^2\le C_L\). Divide the increment recursion by \(A\). Up to a first crossing of \(a_m=2A\), its linear products are bounded by \(\exp(C_La_0)\) and its quadratic contribution relative to \(A\) by \(C_LsA\). Choosing these two errors small closes \(a_m\le2A\). Thus \(|B_c|\le2sA\le2L\sup_{P(c)}\xi'|w|\). This uses the actual adjacent-level carrier property, not a product of depth-dependent constants.

For the Cauchy derivative, set the direction to zero outside the carrier first; locality makes this harmless, and its global starred norm is then its carrier norm. On a circle of radius approaching \(r_*/2\), the first bound gives \(2Lr_*\), hence the derivative bound \(4L\). Without this harmless restriction, a direction normalized only on the carrier need not stay in the global ball. Holomorphy and reality are inherited from the fixed near-identity branches of the means and logarithms.

### 4.3 Lemma D — ADVANCE, conditional

No failure found **conditional on (AX)**. The all-site extension is an actual additional argument. In the gauge convention used in line 139, the contour equation solves to
\[
u(z)=T_{U'_0}(y,z)^{-1}u(y)T_W(y,z).
\]
Along a pillar of height s, every contour perturbation is bounded by \(C(t_m/s)\|a\|_X\); its differentiated term is bounded by \(C(t_m/s)\sup_P\xi'|h|\). Products cost at most \(\exp(C\|a\|_X\sum_m t_m/s)\), and the differentiated sum has the same finite geometric factor. This gives both all-site bounds in line 148 from the top values. Moving from a pillar to its top changes a decay exponential by only a fixed factor.

Differentiating a plaquette gives a curl term \(\eta^2D h\), terms bounded by \(C\eta^2|a||h|\), and a term \(C\eta|h||\partial W-1|\). Multiplication by \(\eta^{-2}\xi'^2\) bounds all of them by \(C(\xi'^2|\nabla h|+\xi'|h|)\), since \(\eta\le\xi'\). Differentiating the conjugation adds \([\dot uu^{-1},\partial\Phi-1]\), with the required normalized bound. The current has the same commutator plus the (T4) current derivative. No second difference of h is inferred from a first-difference estimate.

### 4.4 Real values — CORRECT-NO-ADVANCE

No failure found. The plaquette logarithm gives
\(l^2|D_Uw|\le C(a_0+a_1^2+(η/l)a_0a_1)\le C'(a_0+a_1^2)\).
Unitary transport commutes with the real involution, so this bound applies separately to the real and imaginary parts. Their exponentials are real fields; the profile theorem can therefore be applied to each.

For clarity, the profile calculation is
\[
|\psi_x(0)|\le C\sup_\tau e^{-\delta d'(x,\tau)}
 \lambda(y_\tau)^2\varepsilon(\tau),\qquad
\lambda(y)^2/\lambda(x)^2\le C_Le^{2\kappa d'(x,y)}.
\]
After dividing by \(\lambda(x)^2\), \(2\kappa\le\delta/2\) proves (4.5). The carrier's bounded diameter only changes C. The real-value bound (4.6) follows for the same canonical map by agreement at real data. This rechecks `wf-room.md` (6.2); it does not independently prove its profile-theorem input.

### 4.5 Lemma Q — ADVANCE, conditional

No failure found. Assign boundary bonds consistently to cells and enlarge carriers by a fixed adjacent-cell collar. Aligned nested cube unions tile each layer by its block cells. A cell meets only a fixed number of row carriers at its own and adjacent levels (omitted inward bonds are important here); the number is independent of the fine mesh. The scale-crossing bound yields the displayed cell count. Summing integer shells gives a polynomial times \(\exp[-(\gamma-8\log L/\rho)m]\); the stated stronger threshold \(\gamma>9\log L/\rho\) suffices.

Write \(G_x=\psi_x\circ B\). For directions supported in Q and Q′, Lemmas A′ and D first give
\(|DG_x(v)k_Q|\le C e^{-\theta d'(x,Q)}\|k_Q\|_*\).
Cauchy on the \(r_Q/2\) circle and symmetry of the Hessian give
\[
|D^2G_x(v)[k_Q,k_{Q'}]|
\le {2C\over r_Q}e^{-\theta\max(d'(x,Q),d'(x,Q'))}
 \|k_Q\|_*\|k_{Q'}\|_*.
\]
The maximum is at least half the sum. The integral remainder has factor \(\int_0^1(1-t)dt=1/2\); expanding the two finite cell sums proves (4.8). There is no dimension factor from applying Cauchy: the directions, rather than all coordinates simultaneously, are normalized. This is the fixed-second-order mechanism of SA BGR25, credited above.

### 4.6 Theorem L(a) — ADVANCE, conditional

No failure found. The constant and linear terms cancel exactly in (4.9). For each of its three remainders,
\[
\lambda(x)^{-2}\!left(\sum_Qe^{-\theta d'(x,Q)/2}
 \|w\|_{*,Q}\right)^2
\le C_La_1^2\!left(\sum_Qe^{-(\theta/2-\kappa)d'(x,Q)}\right)^2.
\]
There are **two** cell factors \(\lambda(Q)\), one for each Hessian leg, and each is bounded by \(C_L\lambda(x)e^{\kappa d'(x,Q)}\). These cancel both inverse powers at x before summation. The summation condition is exactly \(\rho>22\log L/\theta\). Together with the three real values this proves the claimed bound uniformly in depth and volume. A single global Cauchy estimate would not prove it.

### 4.7 Theorem L(b), (c) — ADVANCE with the radius repair

The near/far argument works; no substantive failure found. There is a radius-bookkeeping repair: establish (a) at enlarged radii \((2a_0,2a_1)\), with ratio constant \(2C_0\), and choose the final input ceiling at most half that ceiling (for example reserve \(a_*\le r_Q/8\)). Constants in the response bound may depend on the fixed \(C_0\). Otherwise the invocation of (a) at line 239 need not satisfy its literal smallness assumptions.

The cutoff has \(l|\nabla\chi|\le C_L\); fixed stencil/adjacent-scale constants replace the printed 2 or 3 where necessary. If its first-order increment b is comparable to \(a_0\), the endpoint bounds suffice. Otherwise the circle of radius \(d_*a_0/(C_Lb)>1\) stays in the enlarged simple domain; Schwarz bounds the near difference by \(Cb\).

For the far difference there initially remains \(\lambda(x)^{-1}\). For a far point y put \(R=d'(x,y)\). Along a shortest inner-metric path,
\[
1<d(x,y)\le C_L\lambda(x)R e^{\kappa R}.
\]
Using \(R\le e^{\kappa R}/\kappa\), either \(\lambda(x)^{-1}\) is already bounded by \(C_L/\kappa\), or an exponential \(e^{-(\theta-\kappa)R/2}\) absorbs it when \(\theta\ge5\kappa\). Moving from y to its cell costs a fixed factor. Of the remaining two quarter-exponentials, one is summable if \((\theta-\kappa)/4>9\log L/\rho\), equivalently \(\rho>38\log L/\theta\); the other retains at least \(e^{-(\theta/8)d(x,y)}\). Thus cancellation does **not** consume all source decay. For a cell meeting the far set, use a far point for absorption and then its bounded diameter to move to the maximizer of \(l|h|\).

Finally \(d(x,S_0)\le d(x,y)+d(y,S_0)\) proves (c), and the near ball costs \(e^{2\gamma}\). This is a proof at unsettled elements as well as settled ones under the stated interior condition.

### 4.8 Constants and scope — CORRECT-NO-ADVANCE

No additional failure. Fix the response/profile rates first, increase separation afterwards, and reserve the doubled-radius slack just described. The printed \(40\log L/\theta\) exceeds both 22 and 38. All sums used above are bounded by convergent geometric tails with polynomial factors; no numerical evaluation is needed. Definition A and meets supply the aligned cells and separation, not the analytic inputs. This result does not itself prove decoupled WF response bounds.

## 5. Corollary R — ADVANCE for the conditional tower-margin estimate

No failing decay calculation found. First establish the shifted **simple field** bounds on the chosen disc, using the local product estimate; then apply L(c) to the two fields. This avoids assuming the tower conclusion to admit the second endpoint. On a smaller fixed disc this is the same smallness choice used in `wf-room.md` §3.

The conclusion, written with its needed radius comparison explicit, is
\[
{\text{tower change}\over\alpha_{0,m}}
\le C|z|(1+|\nu|){\delta_k\over\alpha_{0,m}}
 e^{-\gamma cML(n-1)}.
\]
Use \(\alpha_m\le C\alpha_{0,m}\) for the chosen usable analytic radius and the running-radius comparison indexed by these intervening layers, \(\delta_k/\alpha_{0,m}\le Cs_k\sqrt{1+n}\). WF1–WF2 alone, with an otherwise unspecified analytic radius, do not define this identification. With the radius convention of `wf-room.md` §4 and that layer/age identification, it is the intended comparison. Since \(n+1\le2^n\),
\[
2^n\sqrt{n+1}e^{-D(n-1)}\le4\,2^{-n/2}\le2\sqrt2
\quad(n\ge1,\ D\ge\log4).
\]
This is precisely the margin mechanism at SA 15933. It retains an initial clause margin, the actual weighted response, the nested gap geometry and the radius comparison as premises. It is not admission of all three WF substitutions: current admission still reads §6, and removed-map/inner-map identification is separate. In particular the last paragraph's attribution of the entire layered room to premises (i)–(ii) alone is too broad.

## 6. Current readouts — WRONG as the claimed completed match

### 6.1 What the outline fixes — CORRECT-NO-ADVANCE

No failure in identifying the specification gap. R9 defines the field system, and SA 10423–10428 prescribes a multiplier-based current without its formula. A separately specified extension is legitimate. It must still have the declared parameter dependence, transport and locality.

### 6.2 Specification — ADVANCE as a conditional construction

No failure in the algebraic definition (6.1). For a given small field A and holomorphic lift H, put \(M_A=I+[(K_A-K_0)H]^{\mathsf T}\). If \(M_A\) is invertible, the formula uniquely defines a multiplier and gives exactly `wf-room.md` (5.4). The pair keeps its independent baseline current. The formula uses the complex pair, so it introduces no dependence on a choice of real/complex splitting, provided the supplied first-system maps themselves have that property. It does not prove those maps exist on the independent fine-parameter discs.

### 6.3 S1–S4 — CORRECT-NO-ADVANCE, conditional; S5–S6 as claimed — WRONG

**S1 (holomorphy).** The Neumann argument is valid under the declared operator bound and response bound. First literal error: line 299 says the maps do not depend on the independent current. SA 10139–10200 defines \(\mathsf G^{-1}=\mathsf G_0^{-1}-\Delta'_\pi[\mathbf J]\), then H from \(\mathsf G\), and H₁ from a further current-dependent operator. R9 uses these operators. Thus (6.1) generally depends on \(\mathbf J\) through H and the first-system field. **Repair:** retain that dependence; joint holomorphy follows by composition and the Neumann series if it holds for those inputs. Independence is unnecessary.

**S2 (anchor).** No failure. At \(B'=0\), A=0, \(M_A=I\), \(R_A=I\), and both reconstructed currents are \(K_0^{\mathsf T}H^{\mathsf T}F'(0)\), so their difference vanishes for every independent current.

**S3 (splitting and covariance).** No algebraic failure under the asserted wall decomposition of H and the first-system field. Every local row/action stencil must be contained in the appropriate wall component. The inverse of a block diagonal \(M_A\) is block diagonal; on a datum-free component the anchor cancellation applies. Bilinear transposes intertwine the adjoint actions because the trace pairing is invariant, and the inverse and chart conversion do likewise. These prove real-gauge covariance, and its complex continuation wherever defined. Mere locality without the stated stencil separation would not suffice.

**S4 (physical exactness).** No failure. For the **actual** undecoupled lift, \(K_0H=I\) follows directly from its definition \(H=\mathsf G K_0^{\mathsf T}(K_0\mathsf G K_0^{\mathsf T})^{-1}\); the row-length factors cancel. Consequently
\[
H^{\mathsf T}K_A^{\mathsf T}\lambda=M_A\lambda,
\quad H^{\mathsf T}J(U)=\lambda_0,
\quad J(U)+\mathsf j=R_AK_A^{\mathsf T}\lambda=J(e^{i\eta A}U).
\]
This requires the stated identification of R9's physical field with the constrained critical solution. It does not require identifying its lift with the P82 lift, and does not justify imposing \(K_0H(s)=I\) at decoupled s.

**S5, conditional estimate.** Integration by parts in (6.2) and use of (O1) do give the desired first-order bound. The exact Wilson first variation can be paired plaquette by plaquette with the covariant curl: after cyclically moving factors in the trace, the full plaquette transport on the last two edges cancels. Thus \(F'(0)=D_{\mathbf U}^{\mathsf T}\mathcal F\), with the appropriate fixed action-normalization factor and \(|\mathcal F|\le C\alpha_0\xi^{-2}\). This remains a holomorphic identity at complex links. The force increment uses the same action and boundary convention. No estimate of the full current in the \(\xi^3\)-norm is assumed.

There is a small but necessary correction to line 335. Keep the factor \(C_H\), and use the two localized product estimates
\[
\|T^{\mathsf T}\mu\|_{Y,w}
\le CC_H\|A\|_X\|\mu\|_{Y,w},\qquad
\|T^{\mathsf T}\mu\|_{Y,w}
\le CC_H\|A\|_{X,w}\|\mu\|_Y.
\]
They follow by first applying the local row bound to \((K_A-K_0)^{\mathsf T}\mu\), then (O1) to \(H^{\mathsf T}\). Choose \(CC_H\|A\|_X<1/2\) for the weighted inverse. The curl term, lower-order term and anchor then give
\[
\|\lambda-\lambda_0\|_{Y,w}
\le CC_H(1+C_H\alpha_0)\|A\|_{X,w},\qquad
\|\lambda_0\|_Y\le CC_H\alpha_0.
\]
The three-term expansion of `wf-room.md` (5.5) gives (6.4), up to fixed constants. This implication is valid.

**Defect 1 (operator input; breaks the claimed stopping point).** The first unsupported identification is line 331, “(O1) ... read from ... Theorem P(e) ... applied to the H block and its gradient.” `p82-curved.md` lines 32, 220 explicitly assert the **first-line row sums only**, not the column half. More decisively, its lift is built from
\(d^{\mathsf T}d+DRD^{\mathsf T}\); the H in (6.1), specified at line 288 by R9, is built from the Wilson Hessian **minus** \(\Delta'_\pi[\mathbf J]\). These are different operators, even at s=1. `a3-clauses.md` §4.3 expressly leaves that current-correction operator and its needed transpose estimates unchecked. Merely changing a block's name does not identify them.

**Visible partial repair.** For the P82 lift \(H^\circ\), its pointwise response bound at rate \(\theta_0\) implies
\[
\xi_b|H^\circ(b,c)|+\xi_b^2|D H^\circ(b,c)|
 \le Ce^{-\theta_0d(b,c)}.
\]
For a weight of smaller rate \(\vartheta<\theta_0\), multiply by the factors of (O1). Each scale cell contributes at most a fixed multiple of \(e^{-(\theta_0-\vartheta)d(Q,c)}\), because \(\eta^4\sum_{b\in Q}\xi_b^{-4}\le C_L\). The cell count in §4.5 sums these contributions if \(\theta_0-\vartheta>9\log L/\rho\). This proves (O1) for **that lift at a reduced rate**. It does not prove it for R9's H. A repair for R9 requires a uniform bound on the current-corrected Hessian perturbation, including the transpose in \(\Delta'_\pi\), and a resolvent argument identifying the resulting constrained lift. That repair remains unproved here. Accordingly (O1) for the actual H is open already at s=1 on the general pair domain, as well as for decoupled s.

**Defect 2 (removed comparison).** Line 337 invokes (5.6) “along the segment,” but that estimate holds with the background, rows and anchor fixed. A removed box problem can change the reference, node transport, rows, and inner-plaquette action. No common admitted segment is supplied. In particular
\[
\Delta\lambda_0=(H-H^\square)^{\mathsf T}F'_U(0)
 +(H^\square)^{\mathsf T}\bigl(F'_U(0)-F'_{U^\square}(0)\bigr)
\]
after common-coordinate identification; the second term is absent from the displayed bound. Even with an identical restricted field, changing the plaquette set changes the action near the boundary. (O1) alone is no comparison of these terms. The source correctly calls a boundary comparison pending, but it has not specified all quantities that comparison must control.

**Repair, unproved for the actual removed maps.** Put both maps in common coordinates and explicitly include differences of the base field, row maps, chart conversions, action/plaquette sets and node lifts, or prove that each is identical on the relevant enlarged carrier. Avoid an unsupported segment by subtracting the two formulas and using
\(M^{-1}-(M^\square)^{-1}=M^{-1}(M^\square-M)(M^\square)^{-1}\).
Transfer derivatives in every anchor/action difference to the corresponding lift before estimating it. If these additional localized differences and the field/lift differences carry the stated boundary exponential, the telescoping products preserve it. The published S6 inequality is justified only in the narrower case of a fixed reference, identical rows/action, a common small analytic ball and the stated operator comparison. This does not yet identify both actual OA7 removed currents.

## 7. Inner endpoint — WRONG as a completed core-admission argument; repaired endpoint advances

### 7.1 Objects — CORRECT-NO-ADVANCE

No failure in distinguishing the raw average from a datum over 1. SA 5(c) explicitly specifies a Landau triple and only places the other pair in its complex gauge orbit. SA 15959–15971 makes the same distinction. Thus WF3–WF4 by themselves do not mandate the extra interpretation that their output is the unmodified canonical representative in the unsaturated core. This distinction matters to the claimed refutation in §7.4.

### 7.2 Lemma N — WRONG as written; explicit repair below gives ADVANCE

**Defect 3 (gauge composition and holomorphy).** The first failing equality is in line 359. With the convention explicitly used in §4.3, \(W^g(x,y)=g(x)W(x,y)g(y)^{-1}\), one has \((\widehat W^h)^g=\widehat W^{gh}\), not \(\widehat W^{hg}\). Furthermore a real local gauge g selected by an existence clause is not a holomorphic function of the complex input. The sentence “everything is a composition ... on \(\mathbf U\)” has not established this for the displayed construction.

**Hand repair.** Fix a root o and fixed coordinate axial paths in the box. Normalize the auxiliary real gauge by \(g(o)=1\), which a constant unitary change permits without changing any bound. For the purpose of estimates write \(\mathbf U=W^g\), set
\[
h(z)=T_W(o,z)^{-1},\qquad
v(z)=T_{\mathbf U}(o,z)^{-1}=g(z)h(z),\qquad
\widehat W=\mathbf U^{v^{-1}}=W^{h^{-1}}.
\]
Now **define** v by the middle direct-path formula, not by a choice of g. It is a finite product of links and inverses, hence holomorphic, unitary for real input, and uses only the box. The gauge g is used solely to estimate its condition number.

Every path has at most \(CM\xi_{k+1}/\eta\) links. Only the imaginary part of the small complex potential contributes to the singular-value growth; hence \(\operatorname{cond}v\le e^{CM\alpha_1}\). In coordinate axial gauge each remaining link is a product of at most \(CM\xi_{k+1}/\eta\) transported plaquette holonomies. The transport condition numbers have the same exponential bound. The telescoping product inequality and the small-log series give
\[
|\widehat W(b)-1|\le CM\alpha_0\eta\xi_{k+1}^{-1}e^{CM\alpha_1},
\qquad \xi_{k+1}|\widehat A|\le CM\alpha_0e^{CM\alpha_1}.
\]
Choose \(M\alpha_1\) small so the exponential is a fixed constant. Lemma A′ at the identity, with \(\xi'\le\xi_j\), yields
\(\sup|\log M_{\mathbf B'}(\widehat W)/i|\le C_BM\alpha_0\xi_j/\xi_{k+1}\).
Covariance gives \(M_{\mathbf B'}(\mathbf U)=M_{\mathbf B'}(\widehat W)^{v|_{\rm nodes}}\). This proves the corrected N, including its stronger \(\tau\) factor. The bounds are independent of how the auxiliary real gauge was chosen. No polar decomposition is used to define a holomorphic map.

### 7.3 Lemma E — ADVANCE for the endpoint after the N repair; final core conclusion WRONG

For the numbered conclusions 1–3, no remaining failure found under their stated background/tower inputs, the corrected N, and the comparison \(\alpha_0\le Ca\) needed to write the first endpoint bound using a. At reference 1, (T4) integrated along \(tB\) gives holomorphy, \(f(0)=0\), and \(|f(B)|\le C\|B\|\). The identity of representatives can be justified without applying a real-reference theorem at an uncharted complex reference:

Fix the real splitting U. On a sufficiently small complex first-order potential ball, both the R5 continuation and
\(\Phi_1(B_{\rm end}(w))^{\widetilde v(w)}\)
are holomorphic. The first is admitted by A′ and the datum radius. For the second, the repaired axial construction bounds \(B_{\rm end}(w)\) on that ball by \(CM(\alpha_0+\|w\|_1)\tau\); choose the ball inside the fixed datum radius. It contains the input after the fixed field ceilings are imposed. On its real slice the two maps agree by uniqueness of the real canonical background and real node covariance. The finite-dimensional identity theorem gives equality throughout the ball. This supplies the domain justification missing from the terse identity-theorem sentence at line 370.

Applying \(u^{-1}\widetilde v^{-1}\) transports both curvature and current at their base sites. Their norms grow by at most
\((1+C\|B_{\rm end}\|)^2e^{CM\alpha_1}\), by D(i) and corrected N. In top-level-j units the assumed level-\((k+1)\) tower bounds are exactly \(a\tau^2\) for both quantities. Choosing the displayed ceiling below \(1+\beta\) proves the second endpoint bound. Thus the **scalar/vector endpoint estimate (7.2)** is recovered in the Landau representative.

**Defect 4 (endpoint is not hereditary admission).** The first new unsupported conclusion is line 372: (7.3) “then puts ... in the level-j core.” That estimate bounds curvature and current at the chosen elements. It does not check every subdomain and truncation, the restriction identity with its prescribed gauge, or all simple potential/gradient bounds on the independent B′ disc. This is the distinction retained at `wf-room.md` line 323. Balaban CMP 109, pp. 277–280, explicitly uses (3.38) to transfer the hereditary condition, in addition to the endpoint and radial bounds (3.39)–(3.52). Those pages confirm the required step, rather than eliminating it by citation.

**Visible repair, not completed for the actual WF maps here:** for each lower tower, prove the restriction/background identity with its node lift, bound that lift and the Landau gauge on the whole independent datum disc, and transfer the generated background's curvature/current bounds to that tower. Also impose the potential/gradient ceiling from \(\|\mathcal H(B)\|_X\le C\|B\|\), and choose B′ below both adjacent curvature radii, as in Balaban (3.51). Alternatively a small-simple-radii admission lemma can be used only with its full \(K^\sharp\) loss explicitly budgeted. Neither the one endpoint estimate nor “\(L\ge4\)” absorbs an unspecified constant C in line 372: write the actual inequality \(C\sqrt{1+m}L^{-2m}\le1/4\) and verify the constant/order of choice. The repaired endpoint is useful; the full inner substitution has not thereby been gated.

### 7.4 Raw representative — WRONG universally; a narrower refutation is provable

**Defect 5 (upper bound turned into lower bound).** The first failure in line 377 is “if \(\widetilde v_{\rm p}\ne1\), adjacent pillars carry different ... values”; non-unitarity does not imply that assertion. Even when they differ, an \(O(\alpha_1\tau)\) upper bound gives no \(c\alpha_1\tau\) lower bound. Thus “lies in the core only when v is unitary” is false. At a fixed finite lattice the identity is strictly inside the core; sufficiently small nonzero holomorphic flat-gauge deformations remain inside it and have non-unitary node factors.

**Explicit repaired counterexample to uniform raw admission.** In a contractible box let \(T=\operatorname{diag}(1,-1)\),
\[
\mathbf U_1(x)=e^{-\epsilon\eta T},\qquad
\mathbf U_\mu(x)=1\ (\mu\ne1),\qquad
U=1,\quad A'_1=i\epsilon T,\quad \mathbf J=0.
\]
This is flat, has zero current, and \(\nabla A'=0\). Take \(0<\epsilon<\alpha_1/(2\xi_{k+1})\). Its pure gauge is \(v(x)=e^{\epsilon(x_1-o_1)T}\), and its level-j datum is \(1^{v|_{\rm nodes}}\). Corrected N gives V=1 and \(B_{\rm end}=0\). Real node covariance, continued in \(\epsilon\), gives the raw canonical representative \(1^{\widetilde v}\). Across a boundary between level-j pillars its link has singular values \(e^{\pm\epsilon\xi_j}\).

For any splitting \(e^{i\eta A''}U''\) with U″ unitary,
\(\|e^{i\eta A''}\|\le e^{\eta\|\operatorname{Im}A''\|}\), by the differential norm inequality for its exponential. Thus the seam forces
\[
\eta\|\operatorname{Im}A''\|\ge\epsilon\xi_j,
\qquad \xi_j\|A''\|\ge\epsilon\xi_j^2/\eta.
\]
For fixed positive \(\epsilon\xi_{k+1}\) and fixed \(\tau\), this violates the level-j potential radius as \(\eta/\xi_j\downarrow0\). All flux and tower-curvature tests remain zero. This is a hand-checkable failure of **uniform use of that raw representative**. Conversely, at fixed mesh take \(\epsilon\) small enough that both its seam potential and seam first difference fit the strict radii; it then supplies the counterexample to the author's universal “only when unitary.”

Replacing that representative by the Landau triple is consistent with SA 5(c), not a refutation of SA's stated Landau/orbit distinction. On real parameters the activity values agree by real gauge invariance. A holomorphic replacement on complex discs additionally needs the common analytic domains, prescribed node/datum transport and the hereditary admission left in Defect 4. Real physical equality alone cannot specify an extension in arbitrary independent variables. Accordingly C4 and the repaired flat example diagnose the raw reading; they do not close the whole WF4 map-identification obligation.

## 8. Verdicts and stopping point — WRONG as written

First failing entry is the claimed completed operator match in item 2 (line 391), followed by the completed core-admission reading of item 3. The five numbered defects above are ranked by the obligations they obstruct; the local corrections in the earlier sections do not add separate open research items.

What survives is precise: Theorem L, including cell-by-cell cancellation and retained source decay, advances as an implication from its explicit background/geometry inputs; Corollary R advances the tower-margin comparison with its stated response, geometry and radius premises. Formula (6.1) is a workable conditional anchored current specification, with valid physical-locus algebra. Corrected Lemma N and the endpoint part of Lemma E give the Landau endpoint estimate. C1 refutes the unrestricted simple-to-tower assertion, and C4 refutes the raw logarithm bound. The corrected flat example refutes uniform raw canonical admission, not every non-unitary representative.

The actual remaining obligations are: identify and bound **R9's** current-corrected lift (already at s=1 on the general complex/independent-current pair domain), then its independent decoupling discs; prove the full removed-map comparison including changed anchors/action/rows/transports; and supply the hereditary restriction and datum-transport argument for the chosen inner Landau map. The source's expressly pending first-system response bounds, nested geometry and label-formation checks also remain pending. No audit, status action, source edit, commit, push, PR or subagent work was performed.
