lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T08:53Z

# P82°: the weighted inverse of S° at a curved regular reference (queue row 98)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; checkout `4dd8762a8`; Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once into a private scratch folder (sha256 `d7f77d4d…4d6f`, matches `sa-map.md`); Balaban CMP 99b (389–434) read from `~/ym4d-papers/cmp99b.txt`, pp. 396–410. Research text, not an audit, not a gate, grants no status. Ungated.

Credit. T. Balaban for the whole architecture used here: background propagators by localization to cubes carrying a small gauge, perturbation from the flat propagators in that gauge, and random-walk summation (CMP 99b (3.35)–(3.47), Corollaries 3.5–3.6, Theorem 3.7, pp. 396–410; flat inputs CMP 95, 96). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the regular-pair class with gauges on cubes of side \(O(M_1\xi_j)\) (SA 10129–10137), the straightened rows, the pillar \(Q'\), \(R\), \(d_{\mathbf B}\) and the kernel algebra (BGR10)–(BGR13). OpenAI Codex for `flat-port.md` (the local saddle system (8.1), whose Schur complement is the Landau operator without \(R\) as a coefficient, and its parametrix) and for `a3-balaban.md` (summation §5, curved averaging comparisons §8.4–8.7, local estimates (7.19), §12), both used below as labelled inputs.

## 1. Statement, inputs, order of constants

**Moves:** the only quantitative input left in nonlinear A3 part 2, P82° of `a3-derivative.md` Lemma 8.1 as kept by `gates/a3-derivative-gate.md` item 2 (`sa-ledger.md` #3, `route-decisions.md` 1 and 4.2 item 1). If it holds, Theorem 4 (first paragraph), Theorem 3's Landau pair and Theorem 6(c) stand on P81, (G1) and the flat package alone. If it failed, both routes would stop at the linear core of A3.

**Setting.** As in SA (1c)(i), lines 10113–10137: \(L\) odd and large; a separated sequence \(\mathbf B\): \(\Omega_0\supset\dots\supset\Omega_k\), each \(\Omega_j\) a union of level-\(j\) \(M_1\)-cubes, \(\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho\,\xi_j\) with \(\rho=R_1M_1\); layers \(\mathcal L_j\), tops \(y\) with scale \(\xi_y=m_y\), rows \(c\) (interior and outward, no inward rows), the metric \(d_{\mathbf B}\). Fine pairing \(\eta^4\sum_b\operatorname{tr}\), counting row pairing \(\sum_c\operatorname{tr}\), physical top pairing with weight \(m_y^4\). Transposes \({}^{\mathsf T}\) are taken in these pairings.

At a real configuration \(U\) put: \(d=d_U\) the forward covariant curl; \(D=D_U\) the scalar covariant gradient (start-point transport); \(Q'=Q'_U\) the outline's pillar mean (SA 9634, contour-mean transports, not the comb \(R^{\mathsf c}\)); \(A_s=D^{\mathsf T}D+Q'^{\mathsf T}m^{-2}Q'\), \(S=A_s^{-1}\), \(N=(Q'S^2Q'^{\mathsf T})^{-1}\), \(R=1-SQ'^{\mathsf T}NQ'S\); \(K=K_U\) the derivative at \(A=0\) of the straightened rows \(\mathcal Q^{\rm st}(U;A)\) in the raw (dimensionless) normalization; and
\[
 S^\circ=\begin{pmatrix}d^{\mathsf T}d+DRD^{\mathsf T}&-K^{\mathsf T}\\ K&0\end{pmatrix},\qquad
 G=(d^{\mathsf T}d+DRD^{\mathsf T}+K^{\mathsf T}K)^{-1},
\]
with \(C_0,H,T\) as in `a3-derivative.md` (3), so that \(S^{\circ-1}(f,b)=(Tf+Hb,\,-H^{\mathsf T}f+(C_0^{-1}-1)b)\) whenever the inverses exist. The norms \(X_w,F_w,Y_w\) are those of `a3-derivative.md` (2), with \(\nabla\) the covariant start-point difference at \(U\); \(\mathcal W_\theta\) is the class of positive \(w\) with \(w(y)\le e^{\theta d_{\mathbf B}(y,z)}w(z)\).

**Hypothesis (Reg\(_\alpha\)).** For every \(j\) and every cube \(Z\) of side \(c_{\rm reg}M\xi_j\) with \(Z\subset\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})\) there is a real gauge \(g\) on \(Z\) with \(U^g=e^{i\eta A}\) on the bonds of \(Z\) and \(\xi_j|A|+\xi_j^2|\nabla A|\le\alpha\) there, \(\nabla\) the ordinary difference in that gauge. This is the outline's regular-pair condition (SA 10137) at a real pair, with its \(M_1\) equal to the walk size \(M\) chosen below and its \(O(1)\) equal to \(c_{\rm reg}\). Neither criticality nor a current bound is assumed: \(S^\circ\) contains no current.

**Theorem P (P82° on the regular class).** Fix \(L\ge L_0\) and \(\alpha_{\rm H}\in(0,1)\). There are \(M\) (a power of \(L\)), \(c_{\rm reg},\rho_0,\alpha_*,\theta_0>0\) and \(C^\circ\), depending only on \(L\) and \(\alpha_{\rm H}\), such that the following holds for every separated sequence with \(\rho\ge\rho_0\), of any depth, mesh, volume and region shape above the torus floors of SA (1b)(ii), and every real \(U\) satisfying (Reg\(_\alpha\)) with \(\alpha\le\alpha_*\).

- (a) \(S^\circ\) is invertible, \(K\) is onto, and \(\Delta_U:\ker Q'\to\operatorname{ran}R\) is an isomorphism.
- (b) For every \(w\in\mathcal W_\theta\), \(0\le\theta\le\theta_0\):
  \(\|Tf+Hb\|_{X,w}+\|-H^{\mathsf T}f+(C_0^{-1}-1)b\|_{Y,w}\le C^\circ(\|f\|_{F,w}+\|b\|_{Y,w})\).
- (c) Hölder member: for \(a=Tf+Hb\), \(\sup_y w(y)\,\xi_y^{2+\alpha_{\rm H}}[\nabla a]_{\alpha_{\rm H},y}\le C^\circ(\|f\|_{F,w}+\|b\|_{Y,w})\), the difference taken with the covariant comparison along a straight path, at separations at most \(\xi_y\).
- (d) \(\|D(1-R)D^{\mathsf T}a\|_{F,w}\le C^\circ\|a\|_{X,w}\).
- (e) Every block of \(S^{\circ-1}\), including the gradient output components, has the BGR11 row sums (first line) at rate \(\theta\).
- (f) (b)–(e) hold, with \(2C^\circ\), when \(d^{\mathsf T}d\) is replaced by the plaquette-curl form \(\mathfrak d^{\mathsf T}\mathfrak d\) of PX114, after a further fixed decrease of \(\alpha_*\).

So P82° holds at every real reference of the class, curved or not, critical or not, with constants free of depth.

**Inputs, with their labels.** Nothing below counts as more than its label.

- [F] `flat-port.md` (Codex, PROVED, ungated; gate is queue row 99): (F1) the flat local models of the enlarged local system, (8.1) with the row multiplier of §9.2, on the one- and two-scale periodic boxes of §8.2 and the bare boundary models, with the inverse bound (8.5) uniform over those geometries; (F2) the cutoffs (8.6), their bounded overlap and the commutator bound (8.8); (F3) the free local estimate (4.1).
- [A] `a3-balaban.md` (Codex, STOPPED, ungated): (A1) the summation lemma (5.1)–(5.6); (A2) the curved averaging bounds (8.7) and comparisons (8.11)–(8.12), re-derived in Lemma 4.2 below; (A3) the covariant local estimate (7.19) and the covariant Hölder paragraph of §12 ((12.2)).
- [G] `gates/a3-derivative-gate.md` item 8: Lemma 8.1 and Lemma 8.2 ADVANCE (Lemma 8.2 with its finite-colour repair, row sums only).
- [Reg at \(U_0\)] For the consumer: the critical reference \(U_0=U^\circ(\mathbf V_0)\) satisfies (Reg\(_\alpha\)) with \(\alpha=C\rho\varepsilon_1\). Source: SA (1b) Theorem 2, second half (SA 9684–9697): on a cube of side \(m\xi_j\), \(m\) a multiple of \(\rho\), whose \(O(\rho)\)-enlargement lies in \(\Omega_j\), a gauge with \(\xi_j|A|,\xi_j^2|\nabla A|\le Cm\varepsilon\); a cell of side \(c_{\rm reg}M\xi_j\le\rho\xi_j\) lies in such a cube of side \(m\le2\rho\) (use index \(j-1\) near the outer face of \(\Omega_j\)), and the gauge restricts. `route-decisions.md` identifies this statement with Balaban CMP 99a Proposition 6. **Cited-pending**, part of P81's package. Its proof uses the current bound, not curvature alone (`a3-balaban.md` §8.3).

**Order of constants.** Fix \(L\), \(\alpha_{\rm H}\). Then the flat and averaging constants: the local inverse bound \(B_L\), commutator constant \(C_L\), overlap number \(N_L\), cell diameter \(D_L\) (in units of \(M\)), read-set width \(a_L\). Then \(M\), so that \(B_LN_LC_L/M\le1/8\). Then \(c_{\rm reg}=C_LL\) and \(\alpha_*\), so that \(B_LN_LC_L\alpha_*\le1/8\); this uses the outline's form "\(\alpha\) on the whole cube", and with Balaban's form \(O(M)\alpha\) one takes \(\alpha_*\) smaller by \(1/M\). Then the walk rate \(\delta_w=\log2/(D_LM)\) and \(\theta_0=\delta_w/2\). Then \(\rho_0\), above flat-port's own gap requirements, above \(C_LML\) (so that cells meet two layers only) and above the summation threshold \(32\log L/\delta_w\) of (A1). Last, \(C^\circ\). Depth, mesh, volume and region shape enter nowhere. For the consumer, \(\varepsilon_1\le\alpha_*/(C\rho)\), chosen after \(\rho\); this is of the form of Theorem 3's ceiling \(\bar\varepsilon\le c(L)/\mathfrak M\), a radius chosen after the lengths.

Status: Sections 2–8 below are written in order; read the verdict in Section 8.
