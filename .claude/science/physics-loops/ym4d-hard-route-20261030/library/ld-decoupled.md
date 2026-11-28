# Layer decay at decoupled parameters (row 164)
Provenance: Codex (GPT-6 family; requested effort max; exact runtime identifiers are not exposed); checkout `6b9d348b8132e27a5a927a94c4af2452ac64abb7`; Sussman–Alpoge outline `31a47c543775`. Research text, not an audit; grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's geometry and response framework. Claude wrote `cond-c.md`. All arguments below are by hand.

## 1. Check of `cond-c.md`

Checked line by line by Codex, as implications from the stated inputs. The complementary-term arithmetic in Proposition L needs the clarification below.

**Lemmas G and T — ADVANCE.** In `geo-5.md` Section 3.3, ordinary steps give \(8s_i\), and the first pair gives \(s_1\). Prepared pairs and lower splices give \(m_i\). Upper splices shrink holes. Cross-component pairs give \(2s_t\ge m_i\). Thus every case preserves G's stronger gap. For T, healing and islands remove the internal hole. Partial drop-outs leave the top member unchanged. Full drop-outs are the stated exception. External pairs retain the two-cell padding. These are precisely the fates at SA 17417–17432.

**Theorem C1 — ADVANCE.** Its strict radius bound gives \(R_z\subset\Omega_{k-1}\subset\Omega_q\) for \(q\le j\). Definition A gives \(T_q(R_z)\subset R_z\). The common endpoints therefore satisfy (C), including the stipulated read collars. Lemma F follows from the frame floor and rounding to powers of \(L\).

**Example C3 and Lemma N — ADVANCE, with C3(b)'s stated qualification.** In C3(a), the cells at offsets \(4,6,8\) give the hole, live component and base point. Thus \(\delta_z=3.5s_j\). Continued creations prevent an operation. For \(2M\xi_k>\delta_z+\rho\xi_j\), the nearest hole point lies in \(T_j(R_z)\) by (A3). This violates (C). C3(b) has the same implication, conditional on an old base point in the kept nest. Its geometric series is \(\sum_{l\le k}m_l\le LM\xi_k/(L-1)\). For N, a nearest hole point either lies outside \(R\), or has depth at most \(e_j\le\rho\xi_j\). The triangle inequality proves N.

**Rule W and Theorem C2 — ADVANCE under Lemma M's base-point convention.** W1 uses C1. In W2,
\[
 r(R_z,z)\le(a+1)M\xi_{p-1}<m_p
       \le d(z,\Omega_{p-1}^c).
\]
In W3, \(r(R_z,z)<LM\xi_j\le s_j\le d(z,\Omega_j^c)\). This last inequality reads SA 20910–20911's one-cell margin. It does not follow from mere membership in the larger index set at SA 6322–6324. With that convention, nesting proves (C). The complementary distances are \(bM/\sigma_j-2\), \(bM/(L\sigma_{j,p})-2\), and \(bM-2\), respectively. The declared box-map hypotheses still supply WF8–WF10; geometry alone does not prove them.

**Proposition L — ADVANCE as an implication, with the frame factor accounted for explicitly.** Put \(a=p-j\), \(b=k-p\ge1\), and \(\epsilon_k=\delta_k/\alpha_k\). This avoids confusing the proof's ratio with the earlier cell length \(s_k\). The box meets only layers \(p-1,p,p+1\), by G. The room and Cauchy steps give
\[
 C\epsilon_k g_j(1+a)^{3/2}L^{-\alpha_Ha}
       e^{-(\theta_L-1)(b-1)}.
\]
For the complementary term, retain the original LD factor until the frame loss is absorbed:
\[
 \rho_j e^{-\theta_L(b-1)}
 \le C\sqrt{1+a}\sqrt{1+b}\,e^{-\theta_L(b-1)}
 \le C\sqrt{1+a}\,e^{-(\theta_L-1)(b-1)}.
\]
The last inequality follows from \(\sqrt{b+1}\le\sqrt2e^{b-1}\). WF12 at local age absorbs the remaining \(L^{3a}e^{-cML^a/L}\). The weakened exponent printed in step 3 alone would leave an unpaid \(\sqrt{1+b}\); the preceding display supplies the needed estimate directly from LD. Counting at most \(CL^{4(b+1)}\) windows gives the stated \(\omega_n^L\). Its two series converge since \(\alpha_H>0\) and \(\theta_L-1>4\log L\). The vacuum term uses the same summable \(b\)-series and \(\rho_{j,p}\le\rho_j\). No named conclusion fails under these premises.

## 2. Inputs and the retained rate

Source comparison at the same Sussman–Alpoge pin: `YM3/YM3_I.tex`, Theorems I-87-35 and I-88-110 (lines 26821–26913, 33284–33367), uses weighted contraction and distance to the datum support. `QED3/QED3.tex` has the linear photon minimizer at 4335–4400 and a weighted inverse followed by a pointwise upgrade at 6960–7032. These are proof templates; no three-dimensional estimate is imported.

Use the common sequence through level \(k\), with metric \(d=d_{\mathbf B}\). Let \(E\subset\Omega_k\) contain the active step-data carriers. The tested datum satisfies \(\|B'\|_{Y,1}\le C_B\delta_k\) and vanishes off \(E\). This is the step's support convention, not an assumption that its response has compact support.

Retain Definition D, including (P) and the full read hulls. Read Theorems A–B with `o1-decoupled-gate.md` Sections 1–2. Read Theorem W with `h-walk-gate.md` Sections 5–7 and `h-walk-fix-gate.md` Sections 2–3. Only their fixed-sequence estimates are used.

The pointwise input is `pw-bridge.md` Sections 6–7, with its four named premises. The nonlinear input is **[RED], [Rows], [NL]** in `nl-r9.md` Sections 3–6. Both notes were checked by Claude in `pw-bridge-gate.md`, first failing step none. These dependencies are necessary: (O1) alone estimates a transpose and cannot construct the nonlinear step direction. Keep the repaired current estimates of `wf-room-2-gate.md` Section 6.3.

Put
\[
 \lambda=\tau_L/16,\qquad c_g=\min(M,\rho),\qquad
 \theta_L=\lambda c_g .
 \tag{1}
\]
The admitted floors give \(M>\rho\ge\rho'\) and \(\tau_L\rho'\ge256\log L\). Hence \(\theta_L\ge16\log L>5\log L\). All these constants precede the depth choice.

Here is the decoupling calculation. A walk or tree of metric length \(t\) has at most \(16+128t/\ell_{\mathsf P}\) parameter tags. Traverse a tree twice; divide the traversal into arcs of length at most \(\ell_{\mathsf P}/4\). Each thickened arc meets at most sixteen cubes by (P). Thus
\[
 |s^\omega|\le e^{16\bar\kappa}
                   e^{128\bar\kappa t/\ell_{\mathsf P}}.
\]
Take the already stipulated \(\ell_{\mathsf P}\ge2048\bar\kappa/\tau_L\) and the hull-radius floor. Tags spend at most \(\tau_L/16\). The pointwise walk and tree bounds retain endpoint rate \(\tau_L/8\). Their counts sum geometrically after the fixed \(M_1\) floor. A weight of rate \(\lambda\) leaves the summable rate \(\tau_L/16\), by MS. The composed force expansion is the one in `pw-bridge.md` (7.4), tagged once on its union. Consequently
\[
 \|H(s)\|_{Y_w\to X_w},\quad
 \|H_1(s)\|_{Y_w\to X_w},\quad
 \|\mathfrak G(s)\|_{F_w\to X_w}\le B,
 \qquad B=Ce^{16\bar\kappa}\ge1 .
 \tag{2}
\]
Theorem B gives (O1) for the same weights. The bounds hold throughout \(|s_\Delta|<e^{\bar\kappa}\), including complex independent currents. No identity between independently decoupled operators is used.

## 3. From the step datum to layer decay

First recall the geometric part of BC. For a layer-\(p\) point, any path to \(E\subset\Omega_k\) crosses layers \(p+1,\ldots,k-1\). In layer \(i\), take the last exit from \(\Omega_i^c\) before entry into \(\Omega_{i+1}\). This segment has physical length at least \(c_g\xi_i\), hence weighted length at least \(c_g\). These ordered segments are disjoint. Therefore
\[
 d(y,E)\ge c_g(k-p-1)_+ .
 \tag{3}
\]
The argument uses periodic paths and includes holes. Fixed pillar and read-collar offsets cost a constant in distance, not one loss per layer.

At \(s=1\) on the physical locus, integrate T4 along the datum segment from \(0\) to \(B'\). Split its exponent into two halves. One half bounds distance to \(E\); MS sums the other half. This gives
\[
 \xi_y|\mathbf H_k(y)|\le
 C\delta_k e^{-(\theta/2)d(y,E)} .
\]
With (3), its layer rate is \(\theta c_g/2\). The floor \(\theta c_g\ge64\log L\) suffices. The following argument supplies the corresponding estimate at decoupled \(s\).

Define \(w(y)=e^{\lambda d(y,E)}\). Distance to a set is 1-Lipschitz, so this is an admitted weight. On active datum rows \(w=1\); a fixed carrier convention changes this by a fixed factor only. Thus \(\|B'\|_{Y,w}\le C_B\delta_k\). If \(E\) is empty, the datum and response both vanish.

Write \(h=\mathbf H_k\). The adopted R9 equations are the two fixed-point equations
\[
 a=H_1(s)B'-\mathfrak G(s)W_s^{\rm red}(a),
 \qquad h=a-H(s)\mathcal C(h).
 \tag{4}
\]
Their weighted proof is short. Put \(b=\|B'\|_{Y,1}\), \(R=2Bb\), and retain the admitted \(b<cB^{-4}\). Choose
\[
 c\le\min\{r_0/4,\,(16C_W)^{-1},\,(16C_C)^{-1}\}.
\]
By [NL], the first map contracts the unweighted \(R\)-ball with
\[
 q=C_WB^3R\le1/8 .
\]
Its value at zero has norm at most \(Bb=R/2\). Thus it maps that ball into itself. The second map contracts the \(2R\)-ball with
\[
 q_C=2C_CBR\le1/4,\qquad 2R\le r_0/B .
\]
Its constant part has norm at most \(R\); its nonlinear part has norm at most \(q_C(2R)\). Iteration from zero therefore converges in both balls. The same inequalities force uniqueness there.

The [NL] Lipschitz estimates hold in every admitted weight on these same unweighted balls. Since both nonlinear maps vanish at zero, (2) and (4) give
\[
 \|a\|_{X,w}\le B\|B'\|_{Y,w}+q\|a\|_{X,w},
 \qquad
 \|h\|_{X,w}\le\|a\|_{X,w}+q_C\|h\|_{X,w}.
\]
Hence
\[
 \|h\|_{X,w}\le
 \frac{B}{(1-q)(1-q_C)}\|B'\|_{Y,w}
 \le2BC_B\delta_k .
 \tag{5}
\]
This is a finite-lattice norm calculation with constants uniform in the lattice. Iteration converges locally uniformly on the open complex domains, so its limit is holomorphic there. The construction, constants and weight work for every depth. Equation (5), followed by (3), proves
\[
 \xi_p|h|+\xi_p^2|\nabla_{\mathbf U}h|
 \le C\delta_k e^{-\theta_L(k-p-1)_+}
 \quad\hbox{in layer }p .
 \tag{6}
\]

## 4. The actual datum row

Fix a Rule W box and a datum row \(c\) of scale \(\xi_c\). Keep its full averaging carrier \(P(c)\), including its contours. On the admitted WF domains, the differentiated AV bound is
\[
 |D m_T(V)[q]_c|\le C_{\rm AV}\xi_c
                                  \sup_{P(c)}|q|.
 \tag{7}
\]
Here \(q\) is a potential tangent in physical units. This is the local row bound used in `wf7-extension.md`'s datum lemma. For a level-\(r\) row, the AV products use \(\sum_{l\le r}(\xi_l/\xi_r)^2\le(1-L^{-2})^{-1}\). This gives depth independence. The nonlinear average and its logarithm remain in their admitted charts.

For the actual path
\[
 V(\nu)=e^{i\eta_k(t+\nu\zeta)h}U_+,\qquad
 v(\nu)=m_T(V(\nu)),
\]
the tangent is \(q=\zeta h\). Indeed, \(h\) commutes with its scalar multiple at each bond. The grouped or complementary cutoff has a fixed supremum bound. It changes neither \(h\) nor its source set.

If \(P(c)\) lies in layer \(p\), insert (6) in (7):
\[
 \boxed{\displaystyle
 |v'_c|\le C_R\delta_k\frac{\xi_c}{\xi_p}
             e^{-\theta_L(k-p-1)_+},\qquad
 \theta_L=\frac{\tau_Lc_g}{16}\ge16\log L>5\log L .}
 \tag{LD}
\]
If the carrier convention adds an adjacent-scale collar, its scale changes by at most \(L\). The distance changes by a fixed amount; absorb both losses in \(C_R\). This is also how Proposition L handles the three layers met by a box. The bound is uniform in \(j,k,p\), mesh, volume and admitted geometry. It holds for every \(t,\nu\) on the stipulated substitution domains and every \(|s_\Delta|<e^{\bar\kappa}\). Its constant retains \(e^{16\bar\kappa}\) and the fixed chart losses.

## Result

**(LD) is proved as an implication for the adopted Definition D and [RED] response**, with \(\theta_L\ge16\log L\), uniformly in depth. Its inputs remain the four premises of `pw-bridge.md`, [Rows], [NL], AV, MS, BC and the admitted WF domains. The named results in `cond-c.md` survive with their stated geometric conventions and the explicit frame-factor calculation in Section 1. Proposition L then supplies its summable lower-layer weight.

This is a hand proof by Codex, not yet checked by the other model. It grants no status.
