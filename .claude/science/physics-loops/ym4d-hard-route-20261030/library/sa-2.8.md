# Obligation 2.8: the prepared/healed action comparison
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed to this session; the requested effort is max); repository commit `54d2a56e0a1a3224119188d9654e816f4ca1373c`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, granting no status.

## 1. Sources and scope

The source construction and proposed cancellation are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. The source is [YM4_sketch_500.tex, pinned revision](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), fetched once into `/tmp/sa_ym4.tex`; SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. Below, SA line numbers refer to that file. Balaban supplies the underlying programme and the cited box-minimization construction; attribution does not discharge their hypotheses or proofs.

This task concerns the action comparison in SA 17854–17889 and its reference measure, not the subsequent healed-history sum, aged comparison, mass theorem or continuum construction. The final index, SA 32891–32914, expressly lists 2.8 as still to be proved. A counterexample to a proposed intermediate estimate would not automatically refute the complete cancellation: cancellation between summands must also be considered.

The required local reading was `GOAL.md`, the three specified sections of `FINISH.md`, and `library/sa-histories.md`, particularly §§3.1, 7 and 8.1. The workflow is absent from the sparse working tree and is read from the same pinned commit using `git show`. The user's single-file research scope overrides broader workflow delivery instructions. Source retrieval, searches and hashes are bookkeeping only; no computation will discharge a mathematical statement. No other repository file is edited.

## 2. Variables and determining sets: two independent fields

Put \(k_f=k-\mathsf N_k\), \(\Lambda=\Lambda^{\rm pr}\), and \(C=C_{k_f}\). Work in level-\(k\) units, with \(\eta=L^{-k}\) and \(\xi_i=L^{i-k}\). A determining sequence \(\mathcal O=(O_i)\) has

\[
 \Gamma_i(\mathcal O)=\{c\in\mathbb T^{(i)}:
 c_\pm\in O_0,\ \{c_-,c_+\}\cap O_i\ne\varnothing,
 \ \{c_-,c_+\}\cap O_{i+1}=\varnothing\},\qquad
 \mathbf D(\mathcal O)=\bigcup_i\Gamma_i(\mathcal O).
\tag{1}
\]

Its datum is \((\mathcal M^iU(c))_{c\in\Gamma_i}\). Inward bonds are excluded. Adding them would change the problem (SA 5612–5660, 9607–9625).

Let \(\mathcal O^p\) be the **determining**, not action, sequence after all stages. Inside \(X\), for \(k_f<i\le k\), it has \(O_i^p\cap X=X\setminus Z_i''\); older entries and stored marks are those of the actual history. The healed determining sequence is \(O_i^h=O_i^p\cup X\), \(i\le k\). Outside \(X\) the sequences agree. The shell sets lie inside \(\Lambda\); the histories' older core need not be a single-scale lattice. These distinctions matter for both the action profiles and the averaging constraints (SA 17420–17446, 17585–17598).

Write \(\mathcal L_X\mathcal O\) for the **specified** localisation/joined sequence of Theorem 6(c), not for a new arbitrary erosion. Its old determining bonds keep their data. New collar bonds receive the lift of the exterior level-\(k\) field: identity within a block, and that coarse field on a crossing bond. These are extra constraints, not Dirichlet values equal to the unknown global background. This is the source of the localisation error (SA 9776–9789).

The fields needed below are:

| Field | Determining set and datum |
|---|---|
| \(P=U''\) | \(\mathbf D_p=\mathbf D(\mathcal O^p)\), with actual stored core datum \(\zeta\), exterior data, and shell datum \(e^{ig_kB}V_0\). |
| \(P_X\) | \(\mathbf D_{pX}=\mathbf D(\mathcal L_X\mathcal O^p)\), with the same old data and the prescribed lifted collar data. |
| \(H=\bar U\) | \(\mathbf D_h=\mathbf D(\mathcal O^h)\), with the newly drawn level-\(k\) field in \(\Lambda\), unchanged exterior data and unchanged data outside \(X\). |
| \(R(b)\) | \(\mathbf D_{hX}=\mathbf D(\mathcal L_X\mathcal O^h)\), datum \(e^{ig_kb}V_\Lambda\) on the level-\(k\) box bonds and the same exterior/lifted collar data. This is \(U_{k,X}(V'_kV_\Lambda)\). |
| \(S=U_0\) | The preceding local reference problem at \(b=0\). |

Here \(B\) is the **old shell integration variable**, on \(\mathbb B_0=\mathbf D_p\cap\text{shells}\), in the multiscale tree gauge \(T_0\). Its centre is \(V_0(c)=\mathcal M^iS(c)\) for a level-\(i\) shell bond, and \(\|B\|_\infty<\delta'_k/g_k\). In contrast, \(b\) parametrises the **new reference variable** \(V'_k\), on free level-\(k\) bonds, in the separate tree gauge \(\delta_{\rm ax}\); its cutoff is \(\|g_kb\|_\infty<M_0\varepsilon_k\). The reference draw follows the integration of the old box. There is no definition identifying \(b\) with the multiscale \(B\). SA 17861 uses \(B\) in the reference argument, whereas SA 17598 identifies \(B\) as multiscale. Below the two variables are separated as required by the actual measure at SA 17604–17608. This notation repair does not refute the intended comparison.

## 3. An explicit accounting of the residual

The source does not specify its ten summands. The following is a ten-entry **algebraic decomposition of its displayed residual**, proposed here to expose the estimates needed. It is not a claim to have recovered a uniquely specified, unprinted list, or to have verified these ten entries.

Write \(x=x_k\), \(w(p)=x_k''(p)\), and \(v(p)=x_k^{\rm healed}(p)\); thus \(v\) is the spatial weight multiplying \(A(\cdot,H)\), not the scalar \(x\). Let \(\chi=\phi_X\), \(\psi=\phi_{\rm c}\), \(0\le\chi,\psi\le1\), and choose the core cutoff supported where \(\chi=1\). Then \(\chi\psi=\psi\) and \(\phi=\chi-\psi\). Without this support choice an additional overlap term must be retained. Put

\[
 Q(B)=\tfrac12\|\phi^{1/2}D\mathsf H B\|^2,
 \quad
 \mathcal R=A(v,H)-A(w(1-\psi),P)
       -xA(\chi,R(b))+xA(\chi,S)+Q(B).
\tag{2}
\]

For one auxiliary comparison keep \(\mathbf D_{pX}\), replace **every nonshell datum** by the corresponding average of \(S\), and put \(e^{ig_kB(c)}\mathcal M^iS(c)\) on its level-\(i\) shell bonds. Denote the resulting background, if admitted, by \(T(B)\), and let \(F(B)=A(\phi,T(B))\). Showing that this replacement changes only core data, that it has an admitted analytic path, and that \(T(0)=S\) are obligations, not definitions. This formulation keeps any unverified exterior or seam match visible.

Whenever these functions are defined and \(F\) is twice differentiable, the following identity is exact:

\[
\begin{aligned}
 R_1={}&A(v(1-\chi),H)-A(v(1-\chi),P),\\
 R_2={}&A((v-w)(1-\chi),P),\\
 R_3={}&x\{A(\chi,H)-A(\chi,R(b))\},\\
 R_4={}&A((v-x)\chi,H),\\
 R_5={}&-A((w-x)\phi,P),\\
 R_6={}&x\{A(\phi,P_X)-A(\phi,P)\},\\
 R_7={}&x\{A(\phi,T(B))-A(\phi,P_X)\},\\
 R_8={}&-x\{F(B)-F(0)-DF(0)[B]-\tfrac12D^2F(0)[B,B]\},\\
 R_9={}&x\{A(\phi,S)-F(0)-DF(0)[B]-\tfrac12D^2F(0)[B,B]\}+Q(B),\\
 R_{10}={}&xA(\psi,S),\qquad \mathcal R=\sum_{a=1}^{10}R_a.
\end{aligned}
\tag{3}
\]

Proof: \(R_1+R_2=A(v(1-\chi),H)-A(w(1-\chi),P)\). Adding \(R_3+R_4\) replaces the healed part by \(A(v,H)-xA(\chi,R(b))\). Also \(R_6+R_7=xF(B)-xA(\phi,P)\), whereas \(R_8+R_9=-xF(B)+xA(\phi,S)+Q(B)\). Finally \(R_5-xA(\phi,P)=-A(w\phi,P)\), \((1-\chi)+\phi=1-\psi\), and \(\phi+\psi=\chi\). These substitutions give (2). No locality, stationarity or smallness is used.

Thus the large weight \(x\) is not lost in bookkeeping. In particular, \(R_9\) retains the linear term, the exact Hessian discrepancy and any defect of \(T(0)=S\); none may be silently replaced by zero.

## 4. Hardest-first attempts to break the comparison

**Thin shells are not by themselves a counterexample.** Prepared gaps can be only \(LM\) in level-\(j\) units (SA 17398–17410), so a comparison across one prepared seam has only an \(O(M)\) distance guarantee. It cannot acquire \(\check R_k\) from that gap. But the distance relevant to \(R_1\) is from the region of changed constraints/data in the box to the outer support of \(1-\chi\). For \(R_3,R_6\) it is from the support of the cutoff to the artificial localisation collar. Those distances can be of order \(M\check R_k\) even though the inner gaps are thin. The old observation about the thin gaps does not refute these terms.

For an actual application of Theorem 6(c), one still has to specify the comparison region \(W\), its parts, their boundary layers, the common determining bonds **and data**, and the inner edge of each lifted collar. The theorem has constant \(C_\mu\sim e^{O(\mu)\delta_0}\), and its mismatch lies as much as \(O(\mu)\) inside the boundary. Taking \(\mu\) proportional to \(M\check R_k\) and ignoring this prefactor is invalid. A useful application keeps \(\mu\), for example \(M_1'\), fixed before the coupling and gains its large distance from a larger region. The supplied inequalities for the prepared nests do not specify all these comparison regions.

**Core replacement is different from outer localisation.** For \(R_7\), the two data need not agree in the core. Agreement on an outer collar does not give an error small on plaquettes immediately adjacent to that core. A valid proof needs a specified cutoff \(\psi\), both distance to the actual mismatched core rows and a bound on the reset data on their local scales. Shrinking physical diameter alone does not suppress arbitrary fine-scale action in four dimensions: if a fixed small plaquette angle \(t\) occupies a fixed number of fine plaquettes, its action is independent of that mesh spacing. This example is a warning about the inference, not an admissible-history counterexample. The retained core action can pay for precisely such configurations. One possible repair is to choose a buffer at an intermediate shell and compare outside it; the necessary collar and test verification has not been done here.

**The weight attack does not produce a factor \(x\).** Exactly,

\[
 w(p)-x=\sum_{i\le k}b_i\{1-\varphi[\Lambda_i^{(\mathsf N_k)}](p)\}.
\tag{4}
\]

If the profile lies in \([0,1]\), its deficits vanish for \(i<j-d_0\), and \(|b_i|\le B_*\), then the triangle inequality gives
\( |w(p)-x|\le B_*(k-j+d_0+1)\).
There is no multiplicative \(x\). The source's earlier estimate is \(O(1+k-j)\) (SA 17640); the later \(O(k-j)\) (SA 17888) must be read with the endpoint allowance, not as an asserted exact zero at \(j=k\). Actual profile support and the bounded number \(d_0\) of transition levels still need checking. The general frame tube alone does not prove \(|b_i|\le B_*\). On the real run, the separate flow hypothesis of Theorem 2.1 does: set \(j=i+1\) in that hypothesis to obtain \(\lambda_\sharp-c_5\le b_{i+1}\le B_\sharp\), and take \(B_*=\max\{B_\sharp,|\lambda_\sharp-c_5|\}\). This uses the stated flow hypothesis, not its production by the unclosed induction. A constant profile deficit near the top shell is therefore not a refutation of the intended estimate.

No explicit configuration satisfying the outline's full history support and violating its quantitative action comparison has been obtained. In particular, failures of the proposed shortcuts above are not promoted to a counterexample to 2.8.

## 5. What stationarity would actually remove

Proposition 2.4 concerns the unweighted reduced action \(f(V)=A(U_{k,X}(V))\) while varying the level-\(k\) bonds having an endpoint in \(\Lambda\). It does not concern \(A(\phi,U)\) for an arbitrary cutoff. Here is the precise conditional passage from reduced criticality to bare criticality. Write \(q_{\rm ext}\) for the fixed exterior averages and collar constraints, and \(q_{\rm box}\) for the free box averages, in local datum coordinates. Put \(q_0=q(S)\). Suppose the admitted background chart \(\Phi\) satisfies \(q\Phi(q)=q\). For a bare tangent \(h\) preserving \(q_{\rm ext}\), put \(d=Dq_{\rm box}(S)h\). Then

\[
 h=h_0+D\Phi(q_0)[0,d],\qquad Dq(S)h_0=0.
\tag{5}
\]

The first term is annihilated by constrained background stationarity; the second is annihilated by stationarity of \(f\) at \(V_\Lambda\). Thus \(DA(S)h=0\). This argument requires an actual differentiable right inverse and a common variational domain. For the shell path it also requires \(q_{\rm ext}(T(tB))\) to remain fixed. The determining-set restriction theorem is the proposed means of checking this, including boundary-crossing rows; an arbitrary tangent in a tree gauge is not sufficient.

Even if those requirements and \(T(0)=S\) are granted, linearity in the action weight gives

\[
 DF(0)[B]
 =DA(\phi,S)[DT(0)B]
 =-DA(1-\phi,S)[DT(0)B].
\tag{6}
\]

The last expression includes the outer cutoff region and the removed core. The background response is not compactly supported in the box. Consequently, \(J(S)=0\) inside \(\Lambda\), or even (5), does not establish that (6) is zero. One must either show cancellation with the other action differences, or estimate this tail. The source's sentence about vanishing of the linear term does not perform that check for the cutoff action. This is an unverified step, not an explicit counterexample to stationarity of its unweighted minimum.

Likewise the exact quadratic coefficient of \(F\) is not defined to be \(g_k^2\|\phi^{1/2}D\mathsf H B\|^2\). It includes the curvature part of the Wilson Hessian and, for the cutoff functional, the current paired with the second derivative of the background path. Those contributions must be estimated in \(R_9\). Positivity of the displayed curl square is elementary; identification of the remainder after extracting it is not.

## 6. Cubic and shrinking-core factors: conditional calculations

These calculations isolate genuine small factors but do not verify the uniform background bounds needed to use them.

For the cubic term, write \(T(B)=\widetilde T(g_kB)\). Suppose, on the whole segment \(tg_kB\), \(0\le t\le1\), that the actual third derivative of \(A(\phi,\widetilde T(\cdot))\) in the product bond norm is at most \(C(\log x_k)^s\), uniformly in the fine mesh, history and torus. One-dimensional Taylor's theorem along this segment then gives

\[
 |R_8|\le\frac C6 x_kg_k^3(\log x_k)^s\|B\|_\infty^3
 \le C g_k(\log x_k)^{s+3\mathfrak p_1}.
\tag{7}
\]

We used \(x_kg_k^2=1\), i.e. the real run \(\theta=x\), and \(\delta'_k/g_k=A_1(\log x_k)^{\mathfrak p_1}\). For any fixed \(a\ge0\), \(y^ae^{-y/4}\) is bounded on \([0,\infty)\); its derivative gives its maximum at \(y=4a\) when \(a>0\). Taking \(y=\log g_k^{-2}\) proves that (7) is bounded by \(C_a g_k^{1/2}\). The positive power is therefore a valid consequence **if** the stated mesh-uniform derivative bound is proved. Finite-dimensional analyticity alone supplies no such uniform bound and cannot discharge (7) on the actual prepared geometry.

For the reference contribution \(R_{10}\), suppose that \(\operatorname{supp}\psi\) lies in a box of level-\(k\) side \(\rho_c\), that this box contains at least one bare spacing, and that \(|\partial S-1|\le C_0\varepsilon_k\eta^2\) there. For \(G\in\mathrm{SU}(2)\),
\(a(G)=1-\tfrac12\operatorname{tr}G=\tfrac12\|1-G\|_{\rm op}^2\).
There are at most \(C(\rho_c/\eta)^4\) contributing plaquettes, so

\[
 0\le R_{10}\le Cx_k\varepsilon_k^2\rho_c^4.
\tag{8}
\]

If the cutoff really has \(\rho_c\le C M\check R_{k_f}L^{-\mathsf N_k}\), as does the geometric core before enlargement, this is at most
\(C p_0(g_k)^2(M\check R_{k_f})^4L^{-4\mathsf N_k}\).
A fixed polynomial in the waiting depth and logarithms can be absorbed into a smaller exponential rate. A cutoff enlarged to a suitable intermediate shell could also give \(L^{-c\mathsf N_k}\), with a different positive \(c\), **provided its actual support has that bound**. SA gives the diameter of \(C\) at 17585, but not a construction of \(\psi\) checking simultaneously this volume bound and the core-separation estimate for \(R_7\). Bound (8) concerns the smooth reference \(S\); it gives no bound on the real retained core action of \(P\).

## 7. The displayed denominator: an explicit conditional positive set

There is a useful elementary support statement, conditional on Proposition 2.4 and admission of its background. Fix one hypercubic frame and exterior data. Suppose its critical representative \(V_\Lambda\) exists, has the required fixed exterior values, and has curvature at most \(a_\Lambda/2\) on every coarse plaquette affected by a box-bond variation. Suppose the background exists on the full mild class with curvature strictly less than \(a_\Lambda\), as Proposition 2.4 asserts. Choose the coupling ceiling so that

\[
 t=M_0\varepsilon_k<\min\{a_\Lambda/16,1/2\},\qquad r=t/2.
\tag{9}
\]

Let \(n\) be the number of free level-\(k\) bonds after fixing the tree, including its specified external anchoring bond among the fixed bonds. On each free bond set \(V'(c)=e^{ia_c}\), \(a_c\in\mathfrak{su}(2)\), \(\|a_c\|<r\), and set \(V'=1\) on the tree. This is an explicit open product set **in the gauge-fixed integration space**; the delta-supported set is not open in the unfixed Haar product space.

All literal tests in the denominator pass on this set. The principal logarithms exist and obey the strict box cutoff. For a varied plaquette, telescoping its four unitary factors gives
\(\|\partial(V'V_\Lambda)-\partial V_\Lambda\|\le4r\),
since \(\|e^{ia}-1\|\le\|a\|\); reversed bonds obey the same estimate. Its curvature is therefore less than \(a_\Lambda/2+4r<a_\Lambda\). This also verifies admission for the *whole* cutoff support \(\|a_c\|<t\), using \(4t<a_\Lambda/4\). Unaffected plaquettes are unchanged. The background is real, its Wilson action is finite and nonnegative, and the exponential is strictly positive.

For completeness, in Pauli coordinates \(a=\boldsymbol a\cdot\boldsymbol\sigma\), normalized Haar measure of the ball of radius \(r<1/4\) is

\[
 h_r=\frac2\pi\int_0^r\sin^2u\,du
       \ge\frac{r^3}{6\pi}>0,
\tag{10}
\]

using \(\sin u\ge u/2\) on that interval. To obtain the measure formula, identify SU(2) with the unit three-sphere by \((\cos u,\sin u\,\boldsymbol n)\), \(\boldsymbol n\in S^2\). The radial tangent has length one and the two angular tangent lengths acquire \(\sin u\); the area element is therefore \(\sin^2u\,du\,d\boldsymbol n\). Dividing its angular integral \(4\pi\sin^2u\,du\) by the total area \(2\pi^2\) gives (10). Tree integration removes one normalized Haar variable per fixed tree bond, with unit Jacobian. If \(N_\chi\) is the finite number of bare plaquettes meeting \(\operatorname{supp}\chi\), then \(0\le A(\chi,U)\le2N_\chi\). Hence the denominator in this frame obeys

\[
 0<h_r^n e^{-2x_kN_\chi}\le\mathsf D_X\le1.
\tag{11}
\]

This is a written finite-cutoff argument, not a numerical estimate. It proves positivity of the **displayed reference denominator from the stated box-background inputs**; it is deliberately not a uniform quantitative lower bound. Choosing \(\gamma\) small after \(M,M_0,a_\Lambda\) makes (9) and the assumed curvature bound follow from the *asserted* Proposition 2.4 estimate \(C(M)\varepsilon_k\). The proposition's actual minimizer/admission theorem has not been rebuilt here.

The denominator contains \(\delta_{\rm ax}\), the logarithmic box cutoff and the background action. Earlier stage and last-shell tests are tests of the old stored variables, not extra factors of this denominator. Their passing for the original history is not proved by (11). Nor does (11) show that every draw is healed: the final \(\chi_k\) can instead produce an island. The full requested support statement, including every carried test and hereditary substitution, therefore remains open here. The missing “Reality and positivity” paragraph is not supplied by the induction assertion in (2e).

## 8. Inputs and their actual standing in the outline

| Input used or needed here | Source and standing |
|---|---|
| Wilson action, its linear dependence on the weight, and determining-bond convention | SA 5552–5660: definitions. The telescoping identity (3), the weight arithmetic (4), and the elementary SU(2)/Haar estimates above are proved here from them. |
| Prepared/action sequences, localisation rule, geometry of the nest and class | SA 17398–17446, 17576–17598, 9776–9789: construction and asserted geometric properties. Catalogue C2, SA 4052–4061, still requires the constructive margins/determination proof. No explicit collar verification for every term has been supplied here. |
| Regular background orbit, analytic chart, restriction identity | Theorems 1, 3 and 6(b), SA 9659–9732, 9776–9783; outline mechanisms at 9795–9913. Catalogue A1, SA 3809–3831, explicitly keeps the uniform many-level orbit and substitution problem open. These are conditional inputs here. |
| Nonlinear response and two-background exponential comparison | Theorems 4 and 6(c), SA 9734–9744, 9783–9789. Catalogue A3, SA 3864–3896, explicitly says the non-Abelian background and multiscale response estimates remain to be proved. The proved flat reference kernels do not close this input. The later use at SA 13437–13498 likewise identifies A1–A3 and boundary-row compatibility as inputs. |
| Critical box continuation and mild-class admission | Proposition 2.4, SA 17656–17662: stated with a contraction/Hessian/Poincaré outline and attribution to Balaban. A full verification on the actual constrained domains is not given in that passage or rebuilt here. Its use in §§5, 7 is explicitly conditional. |
| Profiles and recovered shell weights | SA 6331–6358 specifies profiles as supplied formation data; SA 17628–17640 gives stage recovery and asserts the shell bound. The weight identity is exact. Profile plateau/transition incidence for every prepared shell is unverified here. |
| Flow, radii and scale hierarchy | The flow bounds are hypotheses of Theorem 2.1 (SA 17259); (2e), SA 19408–19524, supplies the class and order of constants. Individual increment bounds follow from the real flow hypothesis as above. The actual induction and its uniform analytic/mass inputs remain C4 (SA 4074–4084), not a consequence of listing an order. |
| Reference law and test support | SA 17604–17610 gives the formula. SA 17508 declares failed normalization a drop-out and claims it does not occur on support, with a dangling positivity pointer. Equation (11) supplies a conditional finite-cutoff positivity argument only; it does not settle the full support assertion. |

The premise list is not a claim that every asserted theorem in those ranges is false. The outline itself separates the open nonlinear obligations from its proved flat and conditional results. In particular, accepting Theorem 6(c) as an assumption would make an appropriate locality application a conditional deduction, not a discharge of that open estimate.

## 9. One strictly smaller stopping inequality

The remaining target of this note is **one real plaquette of \(R_6\)**, with already admitted backgrounds. It does not ask for a new background existence theorem as part of the inequality.

Fix the source constants in their prescribed order and restrict to the real run \(\theta=x\). Let an actual component have passed the tests preceding the reference draw. Let \(P\) and \(P_X\) be the admitted real prepared backgrounds in the table in §2, using the same specified localisation rule. Its collar width parameter \(\mu\), for instance \(M_1'\), is fixed before the coupling. Let \(\mathcal C_X\) be the union of the double-block supports of the **changed or added collar determining rows**, including their innermost edge. It is the actual mismatch set, not just \(\partial X\). Choose a bare plaquette \(p\) whose fixed local stencil is in the common level-\(k\) layer of the two sequences, inside \(\operatorname{supp}\phi\), away from the core. Define

\[
 D_p=d_{\mathbf D_p}(p,\mathcal C_X),\qquad
 a_k=g_k(\log x_k)^q.
\]

Restrict further to \(D_p\ge c_0M\check R_k\), for a fixed \(c_0>0\), and to real data for which both plaquette curvatures on this stencil are at most \(C_0a_k\eta_k^2\). These admission, collar and curvature hypotheses are part of the smaller task; they are not asserted to have been checked for all main-step terms. The desired inequality is

\[
 \boxed{\quad
 |a_p(P_X)-a_p(P)|
 \ \le\ C\,g_k^2(\log x_k)^{2q}\eta_k^4\,e^{-mD_p}.
 \quad}
\tag{L}
\]

There must be \(C,m>0\), with \(m\) a fixed fraction of the background decay rate, and a coupling ceiling, independent of the cutoff, level, torus and admitted history. Dependence on the fixed construction constants and \(C_0,c_0\) is allowed. The estimate must hold on the whole specified real class, not just near the identity or for one fixed fine lattice.

**Why this is strictly smaller.** It is the restriction of the outline's proposed termwise locality input to a single specified comparison, one scalar plaquette, a real field, and a common top layer; existence and admissibility are supplied hypotheses. It neither sums plaquettes nor proves any estimate on \(R_1,R_2,R_3,R_4,R_5,R_7,R_8,R_9,R_{10}\). It has no complex continuation, core reset, stationary jet, reference normalization or all-history domain assertion. Its bound, multiplied by \(x_k\), is precisely a local contribution of the size needed in \(R_6\). This is a smaller **proof obligation**, not a claim that an estimate on the total residual alone logically forces estimates on its separate terms; cancellation could prevent that converse.

**Why the proof stops here.** Matching determining data in the interior is a fact about constraints, not a bound on the solutions' plaquette holonomies. The source proposes obtaining that bound from a gauge-aligned collar response. Its required uniform non-Abelian, multiscale response is explicitly open in A3. No hand proof for this particular actual comparison has been supplied here. Repeating the asserted Theorem 6(c) with the word “therefore” would assume the missing step. The assumed curvature bounds and the SU(2) identity already give \(C a_k^2\eta_k^4\); they supply no factor decaying with \(D_p\).

The attempted variational route identifies the operator that must be controlled. In a common coordinate chart write the stationarity equations as \(\nabla\mathcal A(u)=Dq(u)^T\omega\), \(q(u)=v\), where \(\mathcal A\) is the Wilson action in that chart. Along an admitted branch their derivative is

\[
 \left(D^2\mathcal A(u)-\sum_a\omega_aD^2q_a(u)\right)\dot u
      -Dq(u)^T\dot\omega=0,\qquad Dq(u)\dot u=\dot v.
\tag{12}
\]

This follows by differentiating the two equations; the actual gauge equations must be adjoined. Turning a collar mismatch into forcing for this system also requires the common chart and boundary-row identification. The Hessian in (12) contains the constraint-curvature term with its actual multiplier. A flat Wilson inverse, without that term and the gauge/constraint rows, is not the inverse needed for (L). I have not constructed the uniform, exponentially weighted inverse for this comparison or shown that its whole interpolation stays admitted. This is the concrete uncompleted analytic step, rather than a claim that the mere presence of an open catalogue entry prevents further work.

**Expectation: (L) is true.** Prescribed block averages remove the low-frequency fluctuation directions in the common collar, and the mismatch is confined to its actual boundary rows. The flat constrained kernels and the proposed weighted perturbation mechanism are consistent with the required decay. This is a reason to attempt the nonlinear estimate, not a proof. Its conversion to a scalar action bound has no additional mystery: if a common base-point gauge gives holonomies \(G,H\) with \(\|1-G\|,\|1-H\|\le r\), then
\( |a(G)-a(H)|\le r\|G-H\|\),
by \(a(G)=\tfrac12\|1-G\|^2\) and the reverse triangle inequality. Thus a curvature-sized decaying relative holonomy would yield exactly the two powers of \(a_k\eta_k^2\) in (L). What is missing is that relative estimate with the actual constraint and gauge rows, uniformly in the fine mesh.

## 10. Coverage and recovery

Bounded source excerpts used: SA 3790–3922 and 4034–4087 (dependency catalogue); 5550–5705 (action, averages and determining sets); 6320–6365 (profiles); 9570–9745, 9776–9799 and 9900–9930 (background statements and the relevant proof mechanisms); 13437–13498 (explicit response input); 17251–17317, 17398–17520 and 17521–17675 (history, preparation, local reference and box minimizer); 17840–17940 (cancellation); 19408–19525 ((2e)); 20694–20773 (conditional flow discussion); 32869–32922 (final obligation list). Navigation searches elsewhere are not proof coverage. Substantive passages initially hidden by oversized outputs were retrieved in smaller excerpts before use; the entire background/propagator dependency closure was not read or verified.

Local comparison coverage: `sa-histories.md` §§1–3, 7, 8.1 and 9, and `sa-map.md`'s 2.8 entry. The required GOAL/FINISH sections and the pinned workflow were read. No unrelated local rarity lemma is used as a premise. The [publisher record for Balaban's second large-field paper](https://link.springer.com/article/10.1007/BF01238433) and the [Rutgers record](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Large-field-renormalization-II-Localization-exponentiation/991031665237504646) were consulted while seeking the original comparison. The publisher exposed subscription content only; no full paper was obtained or treated as read. No assertion in this note is discharged by that bibliographic search.

Recovery point: (3) is an exact conditional algebraic accounting; (5)–(11) identify conditional deductions and the premises they do not supply. No counterexample to 2.8 is established. The next mathematical decision is whether (L) can be proved for the actual collar rows using a handwritten nonlinear comparison, or refuted by an admissible real prepared configuration. Even a proof of (L) leaves the core replacement, cutoff jet, full Taylor bounds and all-test support checks outstanding. Only this report is written; no prompt, platform instruction, audit file or other repository file is changed. No computational certificate, subagent, audit, commit, push, PR or post is used.

STOPPED
