# ID: identification of the formed step
Provenance: Codex (GPT-6 family; exact serving variant and runtime effort not exposed; requested effort max); checkout `d63021134677981c3f77958e7e09c4d5e6fc9ace`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

## 1. Target and sources

The target is `ti-2.md` (ID), with its existing input list and complete physical pairs:
\[
 \operatorname{Tot}E^{(i)}(\mathbf p_{U_i(W')})
 =\mathcal E^{(i)}(W')+c_i,\qquad W'\in\mathcal K_i,\quad i\ge1.
 \tag{ID}
\]
Here \(c_i\) must not depend on \(W'\).
The argument must identify the actual sourced step, not only an abstract gas.

The step construction comes from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
SA below means their pinned `YM4_sketch_500.tex`, fetched once.
The local inputs are `ti-2.md` §§2–3, `um1.md`, `um1-fix.md`, `b4-step.md` §10, and `c1-repr.md`.
Queue rows 193, 202, 208, 212 and 213 fix their dependency order.
All arguments below are by hand. No run supplies a mathematical implication.

## 2. The source at a whole-torus physical pair

Put \(k=i-1\), \(U_+=U_{k+1}(W')\), and \(V=\mathcal M^kU_+\).
Use level-\(k\) units and the adopted mean contours throughout.
There are no outward seam rows in this problem.

Write the **plain one-step** constraint as
\[
 q_V(a)=i^{-1}\log[\mathcal M(e^{ia}V)W'^{-1}]
       =K_Va+R_V(a).
\]
The retained pivot-chart input [QC] gives \(K_Vh_V=1\), \(K_VC_V=0\), and
\[
 d=R_V(C_Vu-h_Vd),\qquad a(u)=C_Vu-h_Vd,\qquad V_k(u)=e^{ia(u)}V.
 \tag{1}
\]
Substitution gives \(q_V(a(u))=-d+R_V(a(u))=0\).
Thus \(\mathcal M(V_k(u))=W'\). The free coordinates remain exactly \(u\).

The source of R9 is instead a datum for the **fine straightened** constraint.
Its relative datum is
\[
 \boxed{B'(u)(c)=i^{-1}\log[V_k(u)(c)V(c)^{-1}]=a(u)(c).}
 \tag{2}
\]
To check the reduction, let \(v_k[h]\) be the accumulated straightening factor.
Successive block factorizations give
\(\mathcal M^k(e^{i\eta h}U_+)=(e^{iq_k^{\rm st}(h)}V)^{v_k[h]}\).
The gauge that makes this field tower axial has top value \(v_k[h]^{-1}\).
Gauge covariance therefore cancels both endpoint factors, giving \(e^{iq_k^{\rm st}(h)}V\).
Equating this with \(V_k(u)\) and using the same small logarithm proves (2).
This rebuilds the interior-row reduction of SA 7391–7403, 9924–9937 and 11182–11187.
Neither \(u\) nor \(C_Vu\) can replace \(a(u)\).

By [QC], (2) is holomorphic and finite range, with \(\|B'(u)\|\le C_L\|u\|_\infty\).
Take \(\delta<\min\{r_Q,cB^{-4}/C_L\}\), using the R9 constants of `um1.md` §3.
This places the entire tested box inside the R9 source disc.
This is a deduction from [QC], not a new proof of its uniform chart bounds.

## 3. Identification of the response, including its current

Retain (DOM), A1/A3's regular critical branch and Landau chart, and the adopted [R9], [RED] operators.
These are inputs, not conclusions of this note.
The fibre \(\{\mathcal M^kU=V\}\) lies inside \(\{\mathcal M^{k+1}U=W'\}\).
Thus \(U_+\) is critical on the first fibre too.
A1 and the common axial representative identify it with \(U_k(V)\).

Let \(h_*\) be the Landau representative of the actual branch at \(V_k(u)\).
Equation (2) gives \(Kh_*+\mathcal C(h_*)=B'(u)\).
At \(s=1\), put \(a_*=h_*+H\mathcal C(h_*)\); then \(Ka_*=B'(u)\), since \(KH=1\).
The physical reduction in `nl-r9.md` §4 gives its constrained slice equation:
\[
 a_*=H_1B'(u)-\mathfrak G W^{\rm red}_1(a_*),
 \qquad h_*=a_*-H\mathcal C(h_*).
 \tag{3}
\]
Indeed, on \(\ker K\) in the Landau slice the linear current pairs to zero.
The quadratic constrained inverse is \(\mathfrak G\), and its fixed-row solution is \(H_1B'\).
The derivative of the remaining scalar (4.6) is exactly (4.4), including both derivatives of \(-\langle Ka,Md\rangle\).
Applying that inverse gives the first equation in (3); the second is the coordinate substitution.
For \(u\) near zero, continuity puts this branch in the uniqueness neighbourhood of the R9 contractions.
Hence \(h_*=h:=\mathbf H(P;1,B'(u))\) there.
Both branches are holomorphic on the retained common datum neighbourhood.
The identity theorem extends the equality to its connected tested box.
Consequently \(U_y:=e^{i\eta h(gy)}U_+\) is gauge equivalent to \(U_k(V_k(gy))\).
For \(k=0\), this identification is simply \(U_0(V_k(u))=V_k(u)\).

The current must move too. Use the adopted readout `wf-room-2.md` (6.1).
Write \(K_h=Dq_k^{\rm st}(h)\), \(T=(K_h-K)H\), and \(R_h=(E_h^{\mathsf T})^{-1}\).
Criticality gives \(F'(h)=K_h^{\mathsf T}\lambda\), so
\[
 H^{\mathsf T}F'(h)=(1+T^{\mathsf T})\lambda,
 \qquad H^{\mathsf T}J(U_+)=\lambda_0,
 \qquad J(U_+)+\mathsf j=R_hF'(h)=J(U_y).
 \tag{4}
\]
The first equality identifies the readout multiplier by its invertible defining equation.
The second uses \(J(U_+)=K^{\mathsf T}\lambda_0\) and \(KH=1\).
The last is the chain rule from chart gradient to bond current.
Thus every gauge-invariant list term reads the complete physical pair at the fluctuated datum.
Equations (2)–(4) close the source identification, conditional on the retained chart and response inputs.

## 4. The exact scalar that the gas must represent

Fix the list action \(S\), including the adopted insertions. Put \(g=\theta^{-1/2}\), \(u=gy\).
Let \(\mathcal F\) be the free bonds, \(n=3|\mathcal F|\), and \(m\) the number of soft gauge factors.
The real pivot Jacobians are \(J_c\). Define
\[
 D(V)=\prod_c(\det J_c)^{-1},\qquad
 j_V(y)=\det D\Psi_V(C_Vgy)\prod_b\frac{\sigma(a_b(gy))}{\sigma_0},
 \qquad \kappa=(\sigma_0g^3)^{|\mathcal F|}z_{\mathfrak G}^{-m}.
\]
Here \(\sigma\) is the Haar density in exponential coordinates, with \(\sigma(0)=\sigma_0\).
To verify the measure, use \(t=C_Vu+h_Vv\), whose determinant is \(D(V)\).
The map \(a=\Psi_V(t)\) sends the constraint to \(v=0\).
Each group delta supplies \(\sigma_0^{-1}\); each bond Haar density supplies \(\sigma_0\).
Integrating \(v\) and scaling \(u=gy\) therefore gives exactly \(\kappa D(V)j_V(y)\,dy\).
This proves the needed substitution from [QC], as in SA QC25, without discarding a determinant.

On each gauge contour, finite products and the regular mean give \(|V_k(gy)(y_0,x)-1|\le C_L\delta\).
The background contour equals one. Choose the stipulated threshold ratio so \(C_L\delta<\varepsilon\).
All soft-gauge indicators then equal one; \(\chi(y)\) is the remaining nonpivot box indicator.
Set
\[
 f_x(y)=x[A(U_y)-A(U_+)]+\theta\,\mathrm{GF}(V_k(gy)),\quad
 Q_x=D^2f_x(0),\quad
 P_S(y)=-T_3f_x(y)+\log j_V(y)+S(\mathbf p_{U_y})-S(\mathbf p_{U_+}).
 \tag{5}
\]
Here \(f_x(0)=Df_x(0)=0\): the action is stationary on this fibre, and the gauge factor has its minimum there.
Retain the physical positive quadratic form from A2 and the adopted Gaussian identification.
For its normalized Gaussian \(\mu_{Q_x^{-1}}\), put
\[
 Z_x(V)=D(V)(2\pi)^{n/2}(\det Q_x)^{-1/2},\qquad
 I_S(V)=\int\chi(y)e^{P_S(y)}\,d\mu_{Q_x^{-1}}(y).
\]
Substitution into the definition of the step functional gives
\[
 \boxed{\exp\mathcal E^{(k+1)}(W')=\kappa Z_x(V)I_S(V).}
 \tag{6}
\]
The factors \(e^{-xA(U_+)+S(\mathbf p_{U_+})}\) cancel exactly.
This is the sourced rule of `c1-repr.md` §§3–4: the insertion stays inside the integral.
It supplies no identity replacing \(S(\mathbf p_{U_y})\) by its background value.

For completeness, the two-coupling Gaussian causes only a constant discrepancy.
Write \(\tau=x/\theta\), \(Q_x=\tau Q_A+Q_G\), and \(q=3m\).
The block gauge directions have dimension \(q\). Differentiated gauge invariance gives \(Q_AD\lambda=0\).
The contour differential sends \(D\lambda\) to \(-\lambda\); hence its kernel complements those directions.
On that complement \(Q_G=0\), so rescaling its \(n-q\) coordinates proves
\(Z_x=\tau^{-(n-q)/2}Z_\theta\).
The same calculation gives the total \(q\log\tau/2\) of SA's \(G_\tau\).
Indeed, tilting \(\mu_{\tau^{-1}Q_\theta^{-1}}\) by \(e^{-(1-\tau)\langle y,Q_Gy\rangle/2}\) gives precision \(Q_x\).
Its integral is \(\tau^{q/2}\). Dividing by that integral leaves \(\mu_{Q_x^{-1}}\), so extracting \(G_\tau\) leaves exactly \(I_S\).
The Gaussian localization of `prefactor.md` (10) retains \(D(V)\); its finite inclusion–exclusion sum equals \(\log Z_\theta\), up to chosen constants.
Thus \(\operatorname{Tot}(N+G_\tau)=\log Z_x+(n/2)\log\tau+c_N\).
All displayed logarithms use the real branch, continued from positive real couplings.

## 5. What the finite gas identity proves

The required potential total is precisely
\[
 \sum_YV(Y)=-T_3f_x+\log j_V+\Delta S=P_S.
 \tag{7}
\]
Theorem U' supplies the first term with its negative sign.
The local logarithms supply the second term, without deleting their linear or quadratic parts.
For each old member, `wf7-bf.md` (2) integrates its derivative between the two complete endpoint pairs.
On the whole torus its containment condition holds for every admitted box.
Summing these differences, with their counterterms and complementary terms retained, gives \(\Delta S\).
Each subsequent finite bracket preserves the total: expand
\(\prod_{\Delta\notin X_0}(\operatorname{ev}_0+\int_0^1\partial_{s_\Delta}ds_\Delta)f=f(\mathbf1)\).
Here the root parameters \(s_{X_0}=1\) stay fixed.
Every factor equals evaluation at one by the fundamental theorem of calculus.
This proves (7) **for the full collection**, under the adopted substitution domains and exact filing rules.
It does not give an estimate for that collection.

Expand \(e^{\sum_YV(Y)}=\prod_Y[1+(e^{V(Y)}-1)]\).
For each selected family keep its domain cutoffs, and expand the other cutoffs as \(1-(1-\chi_b)\).
The same finite bracket identity in the coarse parameters, followed by Gaussian block factorization, gives
\[
 I_S(V)=\sum_{\Gamma\ \mathrm{compatible}}\prod_{Z\in\Gamma}H(Z).
 \tag{8}
\]
This is exactly `b4-step.md` §10.1, applied to (7). No logarithm or convergence assertion enters this finite equality.

If the full connected expansion converges absolutely, grouping graphs by connected components gives
\(\exp(\operatorname{Tot}F)=I_S\).
Its branch starts at zero activities. Along the convergent real radial path it is the real logarithm.
Combining this equality with (6) and the Gaussian total proves
\[
 \operatorname{Tot}E^{(k+1)}(\mathbf p_{U_+})
 =\mathcal E^{(k+1)}(W')+c_{k+1},\qquad
 c_{k+1}=c_N+\tfrac n2\log\tau-\log\kappa.
 \tag{9}
\]
The dimensions, gauge normalizer, coupling and chosen subtraction constants are fixed before \(W'\).
Therefore \(c_{k+1}\) is independent of \(W'\).

## Result

**Proved by Codex, not yet checked by the other model:** the source identification (2)–(4), and the exact implication (7)–(9).
They retain the named background, chart, operator, substitution and Gaussian inputs.

**First new input not supplied:** a defined **full-list** logarithmic output at every \(W'\in\mathcal K_i\).
For B1's prescribed connected series, the missing justification is its absolute convergence there.
`b4-step.md` §10 supplies the intrinsic gas only; its §11 explicitly retains the older-potential bound (19).
The finite identity (8) does not establish this convergence.
Positivity of the physical integral does not establish convergence of its particular connected series either.
It gives a real total logarithm; identifying a specified continuation of the local activities with it would be another route.
Invoking B4's full identification here would assume the conclusion being sought.

Thus (ID) holds wherever that full formation input holds; it is **not closed on all of \(\mathcal K_i\)** by these notes.
The inherited [QC] and response premises also remain conditional.
No counterexample to (ID) is claimed, and Theorem TI gains no unconditional premise.
