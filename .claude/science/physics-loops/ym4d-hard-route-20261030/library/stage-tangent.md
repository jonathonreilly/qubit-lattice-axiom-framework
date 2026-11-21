# Stage tangent at the first prepared shell
Provenance: Codex (GPT-6 family; queue effort max; runtime variant and effort not exposed); commit `378dfb5f2a7c590643e8060822e306957a242197`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit; grants no status.

## 1. Sources and question

This note addresses row 251 and the first open input of `oa7.md`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's constructions.
Credit Tadeusz Bałaban for the stage method cited there.
SA denotes their [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
Source locations come first from `sa-index/`, including neighbouring entries in chunks 05, 15 and 16.

SA 5653–5661 includes representatives and chart transport in the background input.
SA 5696–5727 requires every old tower to exist in its assigned continuation domain.
SA 6155–6158 calls stage inclusions “analytic inclusion hypotheses”.
SA 16825–16851 assumes initial room and the all-domain response estimate (OA7).
SA 16866–16935 proves the larger-ball implication from those inputs.
It is a cited conditional result.
SA 17229–17233 says the primitive estimates “have not been proved for the Yang--Mills maps merely by this deduction”.
SA 17585–17660 defines the stage operation and sketches its real test comparisons.
These passages do not supply the requested complex transition estimate.

The question concerns the complete maps on the larger source, including every retained earlier parameter.
No numerical calculation is used below.

## 2. The endpoint problems and their return

Fix an eligible component that completes this stage and later drops out.
Keep its history and real stored variables fixed.
Set \(j=t-\mathsf N_t\ge0\) and \(l=j+1\).
There is no main-step tree gauge at this stage (SA 17585).
Only the following determining member changes:
\[
 \Omega_l^0\cap C=\Omega_l^\circ\cap C,\qquad
 \Omega_l^1\cap C=C\setminus Z_l''(C).                         \tag{1}
\]
The action sequence stays fixed.
For a bond \(c\), let \(E(c)\) be its two endpoints.
The two changed row sets are exactly
\[
\begin{aligned}
 \Gamma_j^n&=\{c\in\mathbb T^{(j)}:E(c)\subset\Omega_0,
 E(c)\cap\Omega_j\ne\varnothing,
 E(c)\cap\Omega_l^n=\varnothing\},\\
 \Gamma_l^n&=\{c\in\mathbb T^{(l)}:E(c)\subset\Omega_0,
 E(c)\cap\Omega_l^n\ne\varnothing,
 E(c)\cap\Omega_{l+1}=\varnothing\},\qquad n=0,1.              \tag{2}
\end{aligned}
\]
All other row sets agree.
Their actual rows are \(\mathcal M^m|_{\Gamma_m^n}\), including the endpoint transports in (R3).
The row spaces generally differ.
The node set, straightening and gauge slice also change (SA 5612–5651, 9630–9644).

Let \(D_n=(V_m^{(n)}|_{\Gamma_m^n})_m\) be the stage's physical determining datum.
It reads the surviving stored fields at their own levels, in that endpoint's recorded frames.
Retained row sets need not have equal data after earlier substitutions.
The first integration reads \(V_j\), with threshold \(\delta'_j\).
Its constraint uses \(\mathcal M(V_j)=V_l\) on the shell's integration constraint bonds.
For fixed real references \(D_{n,*}\), the endpoint background formula is
\[
 X_n=\Phi^{\mathbf B_n}_{D_{n,*}}(b_n),\qquad
 b_n=i^{-1}\Log(D_nD_{n,*}^{-1}),\qquad
 \mathbf B_n=\bigcup_m\Gamma_m^n.                              \tag{3}
\]
On a complex source, (3) is only a partial map until every displayed datum is admitted.
Each \(D_n(P,\zeta)\) must include the earlier compositions.
The real integration formula does not provide their bounds on \(D_1^+\times\{\zeta\}\).

The physical restriction identity gives a useful, but conditional, bridge.
When \(\Omega_m^0\subset\Omega_m^1\), SA 9776–9783 identifies
\(U_{\mathbf B_0}(M_{\mathbf B_0}(X_1))\) with \(X_1\), modulo the old residual gauge.
Thus one can compare \(D_0\) with \(M_{\mathbf B_0}(X_1)\) on the old sequence.
Using its complex continuation first requires both data in one old continuation ball.
Neither real criticality nor the identity itself supplies that ball.
Independent earlier parameters also need their own identification; they are not all physical background data.

For the complete carried pair, write \((\widehat U_n,\widehat J_n)\) before return to the old chart \(\tau\).
Use the old bare mesh \(\eta\), with (R7)'s current conversion.
The required returned maps are
\[
 W_n(b)=u_n(x)\widehat U_n(b)u_n(y)^{-1},\qquad
 K_n(b)=\operatorname{Ad}(u_n(x))\widehat J_n(b),\qquad
 w_n=(i\eta)^{-1}\Log(W_nU_\tau^{-1}).                          \tag{4}
\]
Here \(b=(x,y)\).
The return is constrained by the actual node prescription.
Each native Landau-to-canonical factor satisfies \(u^{\rm nat}v_m[h]=1\) at its active tops.
Junctions include the reduced-datum quotient (SA 9697–9716, 7747).
Axial extension satisfies
\(u(x)=T_{\rm target}(y,x)^{-1}u(y)T_{\rm source}(y,x)\).
This follows by solving the contour covariance identity for \(u(x)\).
Stored sites retain their recorded locations (SA 6397–6400, 17921–17925).
SA 7913 requires an additional smooth-bump correction at former tops carrying stored fields.
Consequently the top factor alone is not the assigned return in (4).

## 3. The full response and multiplier tangent

Fix a differentiable path in one admitted chart.
Dots below include all dependence on its base pair and earlier composition.
They do not differentiate a discrete row selector.
A path between (2)'s problems first needs the bridge described above.

Write the adopted (R9) equations as
\(a=H_1b-\mathfrak G\mathcal W(a)\), \(h=a-H\mathcal C(h)\).
Let \(\partial_r\) differentiate coefficients while holding the field argument fixed.
The product rule gives
\[
\begin{aligned}
 (I+\mathfrak G\mathcal W_a)\dot a
 &=H_1\dot b+\dot H_1b-\dot{\mathfrak G}\mathcal W
                      -\mathfrak G\partial_r\mathcal W,\\
 (I+H\mathcal C_h)\dot h
 &=\dot a-\dot H\mathcal C-H\partial_r\mathcal C.               \tag{5}
\end{aligned}
\]
Thus a datum derivative alone is not the full tangent.
The inverse bounds are \(8/7\) and \(4/3\) on the checked contraction balls.
In their fixed weighted norms, (5) gives the explicit estimate
\[
 \|\dot h\|_X\le\frac{32}{21}
 \bigl(\mathcal B\|\dot b\|_Y+\|\dot H_1b\|_X
 +\|\dot{\mathfrak G}\mathcal W\|_X
 +\|\mathfrak G\partial_r\mathcal W\|_X\bigr)
 +\frac43\bigl(\|\dot H\mathcal C\|_X
                    +\|H\partial_r\mathcal C\|_X\bigr).       \tag{6}
\]
Here \(\mathcal B\) bounds \(H_1\), and is distinct from `d4-chart.md`'s \(B\).
Freezing the base and operators recovers \(32\mathcal B\|\dot b\|_Y/21\).

Use the adopted multiplier of `wf-room-2.md` (6.1), with its check's repairs.
Let \(K_h\) be the straightened row derivative and \(F'_U(h)\) the Wilson force.
Put
\[
 M=I+H^{\mathsf T}(K_h-K_0)^{\mathsf T},\quad
 \lambda=M^{-1}H^{\mathsf T}F'_U(h),\quad
 \lambda_0=H^{\mathsf T}F'_U(0),\quad
 \mathsf j=R_hK_h^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0.   \tag{7}
\]
Here \(R_h\) is the inverse transpose of the exponential-chart derivative.
The current after the shift is \(\mathbf J+\mathsf j\), in common units.
At one change of units its baseline becomes \(L^{-3}\mathbf J_{\rm in}\).
The readout must use those same output units.
It is not replaced by the physical current at independent complex parameters.
Differentiating (7) gives
\[
\begin{aligned}
 \dot\lambda&=M^{-1}\bigl(\dot H^{\mathsf T}F'_U(h)
                 +H^{\mathsf T}\dot F'_U(h)-\dot M\lambda\bigr),\\
 \dot\lambda_0&=\dot H^{\mathsf T}F'_U(0)+H^{\mathsf T}\dot F'_U(0),\\
 \dot{\mathsf j}
 &=\dot R_hK_h^{\mathsf T}\lambda
   +R_h\dot K_h^{\mathsf T}\lambda
   +R_hK_h^{\mathsf T}\dot\lambda
   -\dot K_0^{\mathsf T}\lambda_0-K_0^{\mathsf T}\dot\lambda_0.   \tag{8}
\end{aligned}
\]
The force dots include the reference dependence.
These identities retain the anchor terms absent from a fixed-base derivative.
Their estimates require paired lift bounds; an unpaired second derivative of \(h\) is not licensed.

## 4. The returned tangent and the checked bounds

For one atomic field \(X=e^{i\eta h}U\), set
\(E_hv=\int_0^1\operatorname{Ad}(e^{is\eta h})v\,ds\).
Then
\(\dot X=i\eta E_h(\dot h)X+e^{i\eta h}\dot U\).
Apply this identity and (8) successively through every earlier substitution.
For the resulting pair and its return, the exact derivatives are
\[
\begin{aligned}
 \gamma&=\dot u u^{-1},\\
 \dot W(b)&=u(x)\dot{\widehat U}(b)u(y)^{-1}
                         +\gamma(x)W(b)-W(b)\gamma(y),\\
 \dot K(b)&=\operatorname{Ad}(u(x))\dot{\widehat J}(b)
                                      +[\gamma(x),K(b)].       \tag{9}
\end{aligned}
\]
For a product of assigned contour and node factors \(u=f_1\cdots f_q\),
\[
 \gamma=\sum_{a=1}^q\operatorname{Ad}(f_1\cdots f_{a-1})
                                 (\dot f_af_a^{-1}).           \tag{10}
\]
Differentiate each product factor and multiply on the right by \(u^{-1}\) to prove (10).
It includes the former-top corrections from Section 2.
It gives no uniform estimate by counting those factors.

The following are the usable recorded checks, not new checks by this note.

| Input | Check and scope |
|---|---|
| `dec-field.md`, Proposition 5.1 | Claude, `../gates/dec-field-gate.md` §4: first failing step none. Datum derivatives on fixed admitted response balls. |
| `pw-bridge.md` §§6–7; `nl-r9.md` §6 | Claude, `../gates/pw-bridge-gate.md` §§C–D: conditional pointwise and nonlinear bounds. Retain [Energy], [Coefficients], [Walk geometry], [Parameter geometry], [Rows] and the adopted [RED]. |
| `ld-decoupled.md` (5)–(6) | Claude, `wf-c.md` §1: first failing step none. Decay in the response's own sequence and metric. |
| `o1-decoupled.md`, Theorem B | Codex, `../gates/o1-decoupled-gate.md` §2.3: first failing step none. Weighted transpose bounds (O1) for the specified lift. |
| `wf-room-2.md` (6.1)–(6.4) | Codex, `../gates/wf-room-2-gate.md` §§6.2–6.3: multiplier construction and fixed-base bound, with the stated repairs and (O1). |
| `wf-room-2.md`, Theorem L | Codex, the same check §§4.1–4.8: conditional tower estimates, with doubled-radius room and memberwise containment. |
| `wf-c.md` §3 | Codex, `b4-step.md` §0: node comparison on common interior axial pillars or over one Landau reference. The all-collar extension is unproved. |

For a fixed-sequence datum tangent \(\dot b\), these inputs give
\[
 \|\dot h\|_{X,\omega}\le(32\mathcal B/21)\|\dot b\|_{Y,\omega},
 \qquad \omega(y)=e^{\lambda d(y,E)}.                           \tag{11}
\]
Layer decay uses the datum level \(j\), not the operation level \(t\).
The paired multiplier estimate controls the fixed-base derivative of (7).
It does not bound the changing anchor and reference terms in (8).
Theorem L acts after a potential and a fixed old tower have been admitted.
It does not construct the transition (3)–(4).

The gauge estimate needs more than a value bound for \(\gamma\).
For the old field \(W_0\), its required integrand is
\[
 \sup_b\frac{\lambda_e(b)}\eta
       |\gamma(x)W_0(b)-W_0(b)\gamma(y)|.                       \tag{12}
\]
A value bound alone gives only
\(2\sup|W_0|\sup|\gamma|\sup_b\lambda_e(b)/\eta\).
That estimate is not mesh uniform.
This does not prove that the actual tangent diverges.
The recorded node checks do not supply (12) across the remade shell with its former-top corrections.
Setting \(u=1\) would change the assigned return unless a common-reference identity is first proved.

## 5. Integration and the exact remaining margin

Suppose the actual maps admit a common chart segment for every \(P\in D_1^+\) and every retained \(\zeta\).
Freeze \(u_0\) along it.
Set \(\widetilde W_r=u_0\cdot\widehat U_r\) and \(v_r=u_ru_0^{-1}\).
Let \(T,a_e,g_e\) be exactly the three integrals in `oa7.md` (9), using (12) for \(g_e\).
Their suprema include \(P,\zeta\).
Then
\[
 A_e\le a_e,\qquad B\le e^T,\qquad G_e\le e^Tg_e,
 \qquad E_e\le e^{2T}(a_e+g_e).                                \tag{13}
\]
Here is the hand proof, including the gauge term.
Integrate \(\dot{\widetilde W}_r\) for the first bound.
The equations \(\dot v=\gamma v\) and \(\dot v^{-1}=-v^{-1}\gamma\) give the second bound.
For \(D_r=v_r(x)W_0-W_0v_r(y)\),
\[
 \dot D_r=\gamma_r(x)D_r+
    [\gamma_r(x)W_0-W_0\gamma_r(y)]v_r(y),\qquad D_0=0.
\]
Variation of constants costs \(e^T\).
The exponents use the disjoint intervals \([0,s]\) and \([s,r]\), so their sum is at most \(T\).
This proves the third bound.
The last bound follows from \(E_e=B^2A_e+BG_e\).

For each fixed old tower, retain `d4-chart.md`'s initial bounds and averaging constant.
Thus \(U_\tau\) is real, \(\lambda_e\ge\eta\), and \(\|w\|_{*,e}=\sup_b\lambda_e(b)|w(b)|\).
Assume \(\|b_{\tau,e}(w)\|\le C_{A,e}\|w\|_{*,e}\) throughout the radius-\(R_e\) potential ball.
Precisely, require
\[
\begin{gathered}
 \sup|W_0U_\tau^{-1}-I|\le q_0<q<1,\qquad
 \sup\|w_0\|_{*,e}<R_e/4,\qquad C_{A,e}R_e<r_{B,\tau,e},\\
 e^{2T}(a_e+g_e)
 <\min\{q-q_0,(1-q)R_e/4\}.                                   \tag{14}
\end{gathered}
\]
Every partial integral satisfies the same upper bound.
The logarithm series therefore gives
\(\sup\|w_r-w_0\|_{*,e}\le e^{2T}(a_e+g_e)/(1-q)<R_e/4\).
Indeed, \(\|X^m-Y^m\|\le m q^{m-1}\|X-Y\|\) for \(\|X\|,\|Y\|\le q\).
The logarithm's coefficient \(1/m\) leaves the sum \((1-q)^{-1}\).
Thus the whole path lies in the old half ball.
The fixed-reference averaging bound puts its datum inside \(r_{B,\tau,e}\).
This proves the old (R5) clause conditionally on (14).

Apply this argument separately to rule I and rule II.
Rule I uses the assigned \(\mathfrak M\)-cube erosions and outer-unit gap \(>\rho\).
Rule II uses the assigned \(M'_1\)-cube erosions and inner-unit gap \(\ge M'_1\).
Neither argument changes the old determining set or its continuation map.
Both retain Theorem L's containment and chart hypotheses.
No bound proved here verifies (14) for the actual stage.
SA (OA11) cannot supply it by itself, since its proof consumes (OA7) and initial room.

## Result

**Correction of the datum-only reduction of the outline's sketched stage step.**
Equations (2), (5), (8) and (9) retain the changed rows, coefficient derivatives, multiplier anchor and gauge tangent.
Equations (13)–(14) prove the integration implication for both erosion rules.
They do not prove uniform \(A_e,G_e,B\) for the actual stage.
No configuration with an unbounded actual assigned tangent has been established.
This is not a counterexample to the outline.

**First input still open:** admit the old-row re-expression of the prepared-shell background on all of \(D_1^+\times\{\zeta\}\).
It must identify the continued pair and the return that fixes the recorded stored sites.
Then (5), (8) and (12) need uniform bounds whose integrals satisfy (14).
The checked fixed-sequence responses do not provide that admission or those full derivative bounds.
(D4) remains open.
The full-tangent identities in this note have not been checked by another provider.
