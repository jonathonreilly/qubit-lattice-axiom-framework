# CP1–2: P82M (M1 and (15) on the layered class) and PR-H ((H-ct), (H-prof)), pass 1

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05. Pass 1 (long draft) of the draft → distil → referee → freeze process. Written in the lead clone `F`, folder `ym4d-hard-route-20261030`, at its checked-out state; only this file was written. Not checked by another model. Research text, not an audit; it grants no status. No step rests on a computation; every argument is a finite hand proof meant to be Lean-formalizable.

**Credit.** The outline, the complete account and the three-dimensional text at upstream revision `31a47c543775` are by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. Their constrained backgrounds, Theorems 1–6 of the background chapter, the response system (BGR1–BGR27), the cell-weight conventions, the mesh-uniform Hölder estimate (BGH1–BGH30), the step anatomy (1a.2.8–1a.2.9), the profiles and the history sequences are used below with line numbers. **Tadeusz Balaban** supplies the programme: background fields, small-gauge localization, the regularity class, the local gauge theorem (CMP 99 (1985) 75–102, Prop. 6), the constrained propagators (CMP 99 (1985) 389–434), the derivative estimate (CMP 102 (1985) (190)) and the Hölder clause (CMP 109 (1987) (3.31)). **Jonathan Dimock** supplies the flat-propagator exposition used by the flat port. The library texts by Claude and Codex keep their own provenance: frozen `p82.md`, `pr-lay.md`, `hm.md`, `descent.md`, `in1.md`, `st1-r4.md`, `fp1.md`; gated `a3-derivative.md`; unrefereed `a2-full.md`, `bx-fix.md`, `b4-step.md`, `b4-induction.md`, `c1-repr.md`, `wf-c.md`.

**How to read line numbers.** "L n" is line n of the named library file in this clone. "SA n" is line n of `ym4.tex` in the scratchpad `sa/` folder (the pinned outline). "Y3 n" is line n of `YM3_I.tex` there. A quoted phrase is followed by its line. I say what a source proves only after quoting it.

## 0. Results and status

| Item | Result here | Status in this text |
|---|---|---|
| **M1** (multiplier normalization and the match of P82's output with what (15) consumes) | Stated exactly as Theorem 3.10 (seven clauses). Proved. | **proved** (finite linear algebra; no import beyond the definitions) |
| **(15) at one real critical reference** | Theorem 4.1: frozen P82 Theorem P + M1 + P81 ⟹ (15), via the gated implication of `a3-derivative.md` §§4, 6, 7, whose key steps are re-derived in §4. | **proved as an implication** from P82 Theorem P (frozen; I1–I5, I8), P81 (= A1, ST1's A1/F0/REG) and the local nonlinear bounds of `a3-derivative.md` §4 |
| **(15) uniformly on the admitted layered class** | Theorem 5.7: constants \(C_4,\theta_4\) depend on \(L,\alpha_{\rm H}\) only; fixed at IN1 row 3, before \(\kappa\), independent of \(M,\bar\kappa\), depth, volume and region shape; at interior elements. | **proved as an implication** from the same imports plus frozen pr-lay's G, B, Q (Lemmas 5–7) |
| **(H-prof)** | The literal statement fails at standing drop-out marks (Proposition 8.6, conditional on the existence of such a history). A corrected statement (H-prof♯) with an extra \(C'_x(\log\theta_k)^r\) is proved (Theorem 8.5), and it still closes the consumer (Corollary 8.7). | **literal form: refuted conditionally; corrected form: proved** from SA 6331, SA 17415–17440, IN1 (1), (10)–(11) |
| **Fine-mesh Hölder estimate** (the one FP1 does not supply) | Theorem 9.9: in a real gauge on any cube, the real regular background has \(|A|,\xi|\nabla A|,\xi^{1+\alpha}[\nabla A]_\alpha\le C_\alpha a\,\xi^{-1}\), uniformly in the mesh. Supplies the real part of PR1's clause (H) (Corollary 9.10). | **proved** from RCG4 (pr-lay's Q, conditional on F0) and the rebuilt BGH estimates; new gauge construction (massive Coulomb gauge, Lemma 9.6) |
| **(H-ct)** | Theorem 10.8: an implication from five named inputs (I1)–(I5). Its central identity, `b4-step.md` (20), is proved (Lemma 10.3, Corollary 10.4) from the hypotheses IN1 assigns to OL1. | **proved as an implication**; first remaining Outstanding: **(DOM-in)**, §11, after three attacks |

The first remaining Outstanding statement is (DOM-in) in §11: the step's complex evaluation pairs lie in the level-\(k+1\) core with SA 9767's \(\square_0\)-tower clause and factor room. It belongs to node DOM (critical path item 5 of `assembly-status.md`). (H-ct) also reads H-OL (item 9), the localized comparison (G1) and the decoupled response. These are named in Theorem 10.8.

---

# Part I. P82M

## 1. What the consumers read

### 1.1 ST1

`st1-r4.md` L129 (frozen) states the input: "At a real curved regular critical reference, the weighted inverse for the outline's pillar-\(R\) slice and straightened \(K_0\), with the multiplier normalization, implies the four-dimensional derivative estimates of `a3-derivative.md` §§6–7." On the whole fixed raw-datum ball, for a row direction \(e_c\) (L130–133):
\[
 \xi_y|\dot H|,\ \xi_y^2|\nabla\dot H|,\ \xi_y^3|D^{\mathsf T}D\dot H|,\ \xi_y^3|\dot J|,\ |\dot u(y)|\le C_4e^{-\theta_4d(y,y_c)}|e_c|.\tag{15}
\]
L135: "P82° is now proved conditionally on its imports I1–I8 (including A1/F0) and frozen …; the remaining matching item on this route is M1. The current member of (15) is proved in a3-derivative §7.3 only at bonds whose plaquettes lie in \(\Omega_0\), so (15) is asserted only at interior elements, which is the only place ST1 uses it."

ST1 Lemma 6 (L366–420) writes the response at \(s=1\) with masses. L389: "\(a,\widehat a\) are the fixed positive diagonal masses in the declared scalar and raw-row pairings. Their normalization is part of M1/OPS." L1179–1180 transfers (15) to the mean-axial base: "P82 is proved at its own axial A1 representative, and the mean-axial base differs from it by a real residual gauge (SA 9676), under which P82 is covariant ([p82.md](p82.md) line 243)." Theorem 14, hypothesis 1 (L1541): "P82°–M1 with (15) … hold on every system used. The required IN1 precision and derivative constants are fixed before \(\kappa\), independently of \(M,\bar\kappa\)." Result L1665: "The principal analytic import remains **P82°/M1 and (15)** uniformly on the admitted layered class."

Note: (15) has **no multiplier member**. Its members are \(\dot H,\nabla\dot H,D^{\mathsf T}D\dot H\), the current and the top factor.

### 1.2 a3-derivative (gated, not frozen)

`a3-derivative.md` L41: "Use the fine pairing \(\eta^4\sum_b\operatorname{tr}_{\rm col}\) and the **counting** row pairing \(\sum_c\operatorname{tr}_{\rm col}\). … If the row pairing is instead \(\sum_c\xi_c^4\operatorname{tr}_{\rm col}\), its multiplier is \(\xi_c^{-4}\lambda(c)\). … All multiplier value bounds below refer to \(\lambda\)." Lemma 8.1 (L474): if \(S^\circ=\begin{pmatrix}D^{\mathsf T}D+DRD^{\mathsf T}&-K_0^{\mathsf T}\\K_0&0\end{pmatrix}\) has the bounds (4) with constant \(C^\circ\), the Hölder member and \(D(1-R)D^{\mathsf T}:X_w\to F_w\), then Sections 6–7 hold with \(S^\circ\) in place of \(S_0\), once \(\kappa,r\) are small with respect to \(C^\circ\). §7.5 (L461): "The bound \(|\dot\omega(c')|\le\dots\) is (34), in the counting normalization of Section 3. If the outline's datum pairing carries cell weights \(\mu_c\), its multiplier is \(\mu_c^{-1}\omega\), and the bound has to be converted; this is matching item M1 of Section 12." L556: "**M1**, the multiplier normalization. The outline pairs \(\omega\) with \(\mathcal Q^{\rm st}\) through "datum cell weights" \(\mu_c\) (SA 11761–11770) and never fixes them in Theorems 3–4. The bound holds for the counting multiplier and converts by \(\mu_c^{-1}\), so this is a convention for the outline to fix, not a proof gap." The verdict table (L548) lists Theorem 4's first paragraph as "**proved, conditional** … P81, P82° (Lemma 8.1), M1".

### 1.3 P82 (frozen)

`p82.md` L28: "Fine pairings have weight \(\eta^4\), top pairings weight \(m_y^4\), and row pairings are counting pairings. Transpose means transpose in these pairings, extended complex linearly." L104: "The row multiplier \(\ell\) is in counting normalization." Import I1 (L148): "The row mass Q^*aQ of flat-port equals K^T K here because a^dim = I". Theorem P (L192–218): for real \(U\) satisfying Reg\(_\alpha\), \(0\le\alpha\le\alpha_*\), with \(M_P\mid M_1\), \(\rho\ge\rho_P\) and torus room, \(S_q^\circ\) is invertible, \(K\) is onto, \(\Delta_U:\ker Q'\to\operatorname{ran}R\) is an isomorphism, and for \(0\le\theta\le\theta_0\), \(w\in\mathcal W_\theta\),
\[
 \|a\|_{X,w}+\|\ell\|_{Y,w}+\sup_yw(y)m_y^{2+\beta}[\nabla_Ua]_{\beta,y}\le C^\circ(\|f\|_{F,w}+\|b\|_{Y,w}),\qquad
 \|D(I-R)D^{\mathsf T}a\|_{F,w}\le C^\circ\|a\|_{X,w}.\tag{P15–P16}
\]
"The constant is uniform in depth, mesh, volume and admissible shapes, and serves both curls" (L218). Theorem P82 (L220) supplies "the real-reference linear premise of [a3-derivative.md](a3-derivative.md), Lemma 8.1, including its all-weight reading, Hölder member, \(D(I-R)D^{\mathsf T}\) member and counting multiplier." Lemma 1 ends (L243): "All operators and norms are covariant under real gauge changes." Lemma 2 (L294): "\(R\) is the orthogonal projection onto \(\Delta_U\ker Q'\), independent of the choice of positive top mass in \(A_s\)." §2 step 5 (L180–L188): "All bounds and ceilings in (11)–(12) are functions of \(L,\alpha_{\rm H}\) only, **conditional on the uniformity specified in I1–I8**. The actual \(M_1,R_1\) may increase above their floors without changing them. The later construction size \(M\) and decoupling radius \(\bar\kappa\) do not occur."

### 1.4 The outline

SA 9734–9740 (Theorem 4) lists the members \(\xi_y|\mathsf h|,\xi_y^2|\nabla\mathsf h|,\xi_y^3|D^{\mathsf T}D\mathsf h|,\xi_y^3|\Delta_{U_0}\mathsf h|,\xi_y^3|\delta J|\le Ce^{-c\delta_0d_{\mathbf B}(y,y_c)}|e|\), "together with a Hölder member", and "the value estimates \(|\dot\omega(c')|\le Ce^{-c\delta_0d_{\mathbf B}(y_{c'},y_c)}|e|\) and \(|\dot u(y)|\le\dots\) … both are measured in the unweighted colour or matrix value norm." SA 9729–9731: the pair "satisfies the two equations \(F'=K^{\mathsf T}\omega\), \(\mathcal Q^{\rm st}=\mathsf b(B)\) as well". SA 11760–11770: "Its fine pairing and the datum pairing are the actual cell-weighted pairings. … The weights \(\mu_a\) in this coordinate expression are the datum cell weights. Equivalently the second term is the Hessian of the scalar pairing \(\langle\omega,\mathcal Q^{\rm st}(A)\rangle\)." SA 10010–10015: "Here we use the per-length constraint \(q(A)=\ell^{-1}\mathcal Q^{\rm st}(A)\) … the corresponding multiplier is \(\omega_{\rm len}=\ell\omega_{\rm raw}\)". SA 9602 defines \(d_{\mathbf B}\) by exactly the formula of `p82.md` (1). SA 9658: "The constants \(C\) and the rates depend on \(L\) alone, and in Hölder members also on \(\alpha_{\rm H}\)." SA 9660 (Theorem 1, last sentence): "if \(U\) is any configuration whose plaquettes are regular at a small radius \(\varepsilon\le cL^{-2}\), then the tests of \(M_{\mathbf B}(U)\) are within \(2\varepsilon\) of \(\mathbf 1\) in the interior of a layer and within \(CL^2\varepsilon\) across a seam."

So the outline uses three multiplier normalizations (raw counting, per-length, cell-weighted) and never fixes the cell weights in Theorems 3–4. That is the content of M1.

## 2. Conventions

Work on a finite compatible torus at depth \(k\), \(\eta=L^{-k}\), with a separated sequence \(\Omega_0\supset\dots\supset\Omega_k\) of `p82.md` §1. Colour space: traceless Hermitian \(2\times2\) matrices with \(\langle X,Y\rangle=\frac12\operatorname{Tr}(XY)\), extended bilinearly. Rows \(c\) are the default determining set (interior and outward rows, inward rows omitted). Tops \(y\) carry scale \(m_y=\xi_y\).

**Definition 2.1 (pairings, coordinates, masses).**
1. Fine pairing \(\langle a,b\rangle_{\rm f}=\eta^4\sum_b\langle a(b),b(b)\rangle\). Fine site pairing likewise.
2. Row pairing with weights \(\mu=(\mu_c)>0\): \(\langle\lambda,\beta\rangle_\mu=\sum_c\mu_c\langle\lambda(c),\beta(c)\rangle\). Counting: \(\mu\equiv1\).
3. Top pairing with weights \(w=(w_y)>0\): \(\langle\phi,\psi\rangle_w=\sum_yw_y\langle\phi(y),\psi(y)\rangle\). P82 uses \(w_y=m_y^4\).
4. Row coordinate with lengths \(\ell=(\ell_c)>0\): \(q_\ell(A)=\ell^{-1}\mathcal Q^{\rm st}(A)\) (componentwise). Raw: \(\ell\equiv1\). Per-length: \(\ell_c=s_c\).
5. For a linear map \(T\) between two of these spaces, \(T^{\sharp}\) is its transpose for the declared pairings. \(T^{\mathsf T}\) means \(\sharp\) for the fine pairing and the counting pairing.
6. A **scalar top mass** is a positive diagonal map \(\mathsf a\) on tops. A **row mass** is a positive diagonal map \(\widehat{\mathsf a}\) on rows.
7. \(K_A=(\mathcal Q^{\rm st})'(A)\) (SA 9627), \(Q'\) the pillar average (`p82.md` (4)), \(D=D_U\) the covariant gradient on sites, \(d_U\) the start-point covariant curl on 1-forms (`p82.md` (2)).

**The multiplier of a normalization.** For \(A\) in the chart with \(K_A\) onto and \(F'(A)\) annihilating \(\ker K_A\), the multiplier in normalization \((\mu,\ell)\) is the unique \(\omega^{\mu,\ell}\) with
\[
 F'(A)=\big(q_\ell'(A)\big)^{\sharp_\mu}\omega^{\mu,\ell}.\tag{2.1}
\]
Write \(\omega^{\rm cnt}=\omega^{1,1}\). This is the \(\omega\) of `a3-derivative.md` (37) and the \(\ell\) of `p82.md` L104.

## 3. M1: statement and proof

### 3.1 The seven clauses

**Theorem 3.10 (M1).** At a real regular critical reference \(U_0\) satisfying the hypotheses of `p82.md` Theorem P, on the datum polydisc of `a3-derivative.md` Proposition 6.4:

- **(M1.1) Metric and weights.** P82's distance (1) is the outline's \(d_{\mathbf B}\) (SA 9602). P82's norms (6) and class \(\mathcal W_\theta\) are those of `a3-derivative.md` (2) and Lemma 8.2. Hence P82's estimate (P15) is the bound (4) of `a3-derivative.md` "for every \(w\in\mathcal W_\theta\)", as Lemma 8.2 requires.
- **(M1.2) Slice.** For every positive scalar top mass \(\mathsf a\) and every top pairing \(w\), the operator \(R_{\mathsf a,w}=I-G'Q'^{\sharp}(Q'G'^2Q'^{\sharp})^{-1}Q'G'\), \(G'=(\Delta_U+Q'^{\sharp}\mathsf aQ')^{-1}\), is the fine-orthogonal projection onto \(\Delta_U\ker Q'\). In particular ST1's \(R\) (L389), pr-lay's \(R\) ((6)), a3-derivative's \(R\) and P82's \(R\) ((5)) are the same operator.
- **(M1.3) Row mass.** For every row mass \(\widehat{\mathsf a}\) with \(X+K^{\mathsf T}\widehat{\mathsf a}K\) invertible (\(X\) the field block), the constrained inverse \(S^{\circ-1}\) is the same matrix. Its field-output blocks \(T,H\) do not depend on \(\widehat{\mathsf a}\); its multiplier block equals \(\Sigma_{\widehat{\mathsf a}}-\widehat{\mathsf a}\), also independent of \(\widehat{\mathsf a}\).
- **(M1.4) Multiplier conversion.** \(\omega^{\mu,\ell}(c)=(\ell_c/\mu_c)\,\omega^{\rm cnt}(c)\), and the same holds for every datum derivative \(\dot\omega\). The outline's value member for \(\dot\omega\) in normalization \((\mu,\ell)\) holds with constant \(C\sup_c(\ell_c/\mu_c)\) whenever it holds for \(\omega^{\rm cnt}\) with constant \(C\).
- **(M1.5) Normalization-free members.** The Landau pair \((\mathcal H(B),u_B)\), the physical current \(J(e^{i\eta\mathcal H(B)}U_0)\) and all their datum derivatives are independent of \((\mu,\ell,\mathsf a,\widehat{\mathsf a},w)\). So every member of (15) is independent of every choice in Definition 2.1.
- **(M1.6) Straightened rows.** If an operator \(\widetilde K=\mathcal T K_0\) is used in place of \(K_0\), with \(\mathcal T=I+\mathcal N\), \(\mathcal N\) a row-to-row map of finite range \(D_L\) in \(d_{\mathbf B}\), entries bounded by \(C_L\), and \(\mathcal N^2=0\), then the bounds (P15)–(P16) for one of the two systems imply them for the other with constant \(C_L'e^{2\theta D_L}C^\circ\). Thus either reading of "the actual straightened derivative" at outward rows meets Lemma 8.1.
- **(M1.7) Reference multiplier.** \(\lambda_0:=\omega^{\rm cnt}(0)=H^{\mathsf T}J\), \(J=F'(0)\), and \(\|\lambda_0\|_{Y}\le C^\circ\|J\|_F\).

In addition: (i) P82's curl \(q=d_U\) is the \(D\) of \(D^{\mathsf T}D\) in `a3-derivative.md` (L452), and \(\Delta'=F''(0)-d_U^{\mathsf T}d_U\); (ii) Theorem P assumes only Reg\(_\alpha\) on a real \(U\), which is a gauge-invariant condition, and its conclusions are real-gauge covariant (L243).

**Consequence.** The only normalization that the proof of (15) reads is the counting multiplier \(\omega^{\rm cnt}\), through `a3-derivative.md` (34), 7.3 and 7.5. P82 supplies exactly that (L104, L220). No member of (15) depends on the outline's cell weights, which it never fixes. The outline's Theorem 4 multiplier value bound is true for \(\omega^{\rm cnt}\). It transfers to another normalization only through \(\sup_c\ell_c/\mu_c\). For example, with physical cell weights \(\mu_c=s_c^4\) and per-length rows \(\ell_c=s_c\), in level-\(k\) units, \(\ell_c/\mu_c=s_c^{-3}\) is not bounded uniformly in depth. So the outline's bound "in the unweighted colour norm" (SA 9740) must be read for \(\omega^{\rm cnt}\) or for a normalization with \(\ell_c\le C\mu_c\). This is the convention that M1 fixes. It is a reading, not a correction of a proved statement.

### 3.2 Proofs

**Lemma 3.1 (M1.1).** *Proof.* `p82.md` (1) and SA 9602 are the same infimum over connected torus paths of \(\sum_{j\ge1}\xi_j^{-1}\operatorname{length}(\Gamma\cap\mathcal L_j)+\eta^{-1}\operatorname{length}(\Gamma\setminus\Omega_1)\), letter for letter. `a3-derivative.md` (2) defines \(\|a\|_{X,w}=\sup_yw(y)\max\{\xi_y|a|_y,\xi_y^2|\nabla a|_y\}\), \(\|f\|_{F,w}=\sup_yw(y)\xi_y^3|f|_y\), \(\|b\|_{Y,w}=\sup_cw(y_c)|b(c)|\); `p82.md` (6) is the same with \(m_y=\xi_y\), and includes stencils in the local norms in both. The weight condition \(w(y)\le e^{\theta d(y,z)}w(z)\) is the same. Lemma 8.2 asks for "every \(w\in\mathcal W_\theta\)"; Theorem P is stated for every \(w\in\mathcal W_\theta\). ∎

**Lemma 3.2 (M1.2).** *Proof.* Fix \(\mathsf a,w\). *Existence.* For a site field \(\chi\), \(\langle\chi,(\Delta_U+Q'^{\sharp}\mathsf aQ')\chi\rangle_{\rm f}=\|D\chi\|_{\rm f}^2+\langle Q'\chi,\mathsf aQ'\chi\rangle_w\ge0\), with equality only if \(D\chi=0\) and \(Q'\chi=0\). Theorem P says \(\Delta_U\) is injective on \(\ker Q'\); \(D\chi=0\) gives \(\Delta_U\chi=0\); so \(\chi=0\). The real symmetric form is positive definite, so \(G'\) exists and is positive definite. \(Q'\) is onto the tops (`a3-derivative.md` L413: "Indeed \(Q'\) is onto"; directly, for a top \(y\) and a colour vector \(v\), the field \(\lambda(x)=\operatorname{Ad}(\mathsf T(y,x))^{-1}v\) on \(P_y\), zero elsewhere, has \((Q'\lambda)(y)=v\) and \(Q'\lambda=0\) at the other tops, because pillars partition the sites). Hence \(Q'^{\sharp}\) is injective, \(G'Q'^{\sharp}\) is injective, and \(N:=Q'G'^2Q'^{\sharp}=(G'Q'^{\sharp})^{\sharp}(G'Q'^{\sharp})\) is positive definite on tops (transposes now for the fine pairing and \(w\)). *Projection.* Put \(P=G'Q'^{\sharp}N^{-1}Q'G'\). Then \(P^2=G'Q'^{\sharp}N^{-1}(Q'G'^2Q'^{\sharp})N^{-1}Q'G'=P\), and \(P^{\sharp}=P\) because \(G'\) is fine-symmetric. So \(P\) is the fine-orthogonal projection onto \(\operatorname{ran}P=\operatorname{ran}G'Q'^{\sharp}\) (the inclusion \(\supset\) holds because \(N^{-1}Q'G'\) maps onto the tops). Hence \(R=I-P\) is the orthogonal projection onto \((\operatorname{ran}G'Q'^{\sharp})^\perp=\{\chi:Q'G'\chi=0\}=G'^{-1}\ker Q'\). For \(\psi\in\ker Q'\), \(G'^{-1}\psi=\Delta_U\psi+Q'^{\sharp}\mathsf aQ'\psi=\Delta_U\psi\). So \(\operatorname{ran}R=\Delta_U\ker Q'\). This set involves neither \(\mathsf a\) nor \(w\). An orthogonal projection is determined by its range. ∎

The identity for a change of top pairing is the special case \(Q'^{\sharp_w}=Q'^{\sharp_{w'}}(w/w')\), which only replaces \(\mathsf a\) by \((w/w')\mathsf a\).

**Lemma 3.3 (M1.3).** Let \(X\) be any field operator, \(K\) onto, and \(S=\begin{pmatrix}X&-K^{\mathsf T}\\K&0\end{pmatrix}\) invertible. Let \(\widehat{\mathsf a}\) be a symmetric row map with \(G_{\widehat{\mathsf a}}=(X+K^{\mathsf T}\widehat{\mathsf a}K)^{-1}\) existing and \(KG_{\widehat{\mathsf a}}K^{\mathsf T}\) invertible. Put \(\Sigma=(KG_{\widehat{\mathsf a}}K^{\mathsf T})^{-1}\), \(H=G_{\widehat{\mathsf a}}K^{\mathsf T}\Sigma\), \(T=G_{\widehat{\mathsf a}}-HKG_{\widehat{\mathsf a}}\). Then
\[
 S^{-1}(f,b)=\big(Tf+Hb,\;-H'f+(\Sigma-\widehat{\mathsf a})b\big),\qquad H'=\Sigma KG_{\widehat{\mathsf a}}.\tag{3.1}
\]
*Proof.* Let \((a,\ell)\) be the right side. Then \(Ka=KG f-KHKGf+KHb=KGf-KGf+b=b\), because \(KH=I\). Next \((X+K^{\mathsf T}\widehat{\mathsf a}K)a=G^{-1}(Tf+Hb)=f-K^{\mathsf T}\Sigma KGf+K^{\mathsf T}\Sigma b\). So \(Xa=f-K^{\mathsf T}\Sigma KGf+K^{\mathsf T}\Sigma b-K^{\mathsf T}\widehat{\mathsf a}b\), using \(Ka=b\). And \(K^{\mathsf T}\ell=-K^{\mathsf T}\Sigma KGf+K^{\mathsf T}(\Sigma-\widehat{\mathsf a})b\). Hence \(Xa-K^{\mathsf T}\ell=f\). So \(S(a,\ell)=(f,b)\). Since \(S\) is invertible, (3.1) is \(S^{-1}\) for every admissible \(\widehat{\mathsf a}\). Two matrices equal to \(S^{-1}\) are equal blockwise. ∎ (With \(\widehat{\mathsf a}=I\) this is `a3-derivative.md` (27) and `p82.md` (14); with \(\widehat{\mathsf a}\) equal to ST1's row mass it is the first line of ST1's (38).)

**Lemma 3.4 (M1.4).** *Proof.* For a field \(v\) and a row family \(\beta\): \(\langle q_\ell'v,\beta\rangle_\mu=\sum_c\mu_c\ell_c^{-1}\langle(K_Av)(c),\beta(c)\rangle=\langle K_Av,\mu\ell^{-1}\beta\rangle_{1}=\langle v,K_A^{\mathsf T}(\mu\ell^{-1}\beta)\rangle_{\rm f}\). So \((q_\ell')^{\sharp_\mu}=K_A^{\mathsf T}\circ(\mu\ell^{-1})\). Then (2.1) reads \(F'(A)=K_A^{\mathsf T}(\mu\ell^{-1}\omega^{\mu,\ell})\). Uniqueness of the counting multiplier (\(K_A^{\mathsf T}\) injective since \(K_A\) onto) gives \(\mu\ell^{-1}\omega^{\mu,\ell}=\omega^{\rm cnt}\). Differentiating in the datum at fixed \((\mu,\ell)\) gives the same for \(\dot\omega\). The value bound transfers by \(|\dot\omega^{\mu,\ell}(c')|\le(\ell_{c'}/\mu_{c'})|\dot\omega^{\rm cnt}(c')|\). ∎

**Lemma 3.5 (M1.5).** *Proof.* By `a3-derivative.md` Proposition 6.4 (37), on the whole polydisc the Landau pair is the unique holomorphic pair with value \((0,\mathbf1)\) at \(0\) satisfying \(\Phi(B)=(e^{i\eta\mathcal H}U_0)^{u_B}\), \(RD^{\mathsf T}\mathcal H=0\), \(u_Bv[\mathcal H]=\mathbf 1\) at the tops (uniqueness: Lemma 6.3 and the identity theorem, L409–L423). These conditions involve \(\Phi\) (fixed by P81), \(R\) (independent of every choice by Lemma 3.2), the node factors \(v\) (built from the averages only) and nothing else. So \((\mathcal H,u)\) is independent of every choice. The current \(J(U)\) is the left-variation gradient of the inner-plaquette action in the fine pairing (SA 7375; `a3-derivative.md` 7.3); it involves no row or top pairing. Datum derivatives of choice-independent functions are choice-independent. ∎

**Lemma 3.6 (M1.6).** Let \(S_K=\begin{pmatrix}X&-K^{\mathsf T}\\K&0\end{pmatrix}\) and \(\widetilde K=\mathcal TK\) with \(\mathcal T\) as in (M1.6). Then \(S_{\widetilde K}(a,\widetilde\ell)=(f,b)\) iff \(S_K(a,\mathcal T^{\mathsf T}\widetilde\ell)=(f,\mathcal T^{-1}b)\), and \(\mathcal T^{-1}=I-\mathcal N\).

*Proof.* \(\widetilde K^{\mathsf T}\widetilde\ell=K^{\mathsf T}(\mathcal T^{\mathsf T}\widetilde\ell)\) and \(\widetilde Ka=b\iff Ka=\mathcal T^{-1}b\). Also \((I+\mathcal N)(I-\mathcal N)=I-\mathcal N^2=I\). Hence \(a=\big(S_K^{-1}(f,(I-\mathcal N)b)\big)_1\) and \(\widetilde\ell=(I-\mathcal N^{\mathsf T})\big(S_K^{-1}(f,(I-\mathcal N)b)\big)_2\). For \(w\in\mathcal W_\theta\), a row map of range \(D_L\) with entries \(\le C_L\) and at most \(C_L\) entries per row and column has \(\|\mathcal N\beta\|_{Y,w}\le C_L^2e^{\theta D_L}\|\beta\|_{Y,w}\), and the same for \(\mathcal N^{\mathsf T}\). Insert these in (P15). The field members, the Hölder member and (P16) are read from \(a\) only. ∎

Remark. `a3-derivative.md` L392 records \(D\tilde q_A=\mathcal T_AK_A\) "with \(\mathcal T_A\) the identity plus a part that is nilpotent of order two (outward rows read interior rows only)". That is exactly (M1.6)'s structure. `p82.md` Theorem P82 says "with \(K=K_0\) the actual straightened derivative" (L220). I do not need to decide which of the two operators P82's recursion (3) produces at outward rows: Lemma 3.6 covers both.

**Lemma 3.7 (M1.7).** *Proof.* At \(A=0\), `a3-derivative.md` Lemma 6.2 gives \(J=F'(0)=K_0^{\mathsf T}\lambda_0\). By (3.1) with \((f,b)=(J,0)\): \(S^{\circ-1}(J,0)=(TJ,-H'J)\), and by Theorem P \(\|H'J\|_Y\le C^\circ\|J\|_F\). Since \(KH=I\), \(H^{\mathsf T}K_0^{\mathsf T}=I\) on rows, so \(\lambda_0=H^{\mathsf T}K_0^{\mathsf T}\lambda_0=H^{\mathsf T}J\). In Theorem P's pairings \(H'=H^{\mathsf T}\) (fine and counting transposes; `p82.md` L28). ∎

**Clause (i).** `a3-derivative.md` 7.2 (L446–452) defines \((Dh)_{\nu\mu}=\nabla_\nu h_\mu-\nabla_\mu h_\nu\) with start-point transport; this is `p82.md` (2) \(d_U\). SA 9627 writes \(F''(0)=\Delta^{\rm W}_{U_0}=D^*D+\Delta'\); so \(\Delta'\) is defined as the difference. Lemma 8.1's proof only needs \(\|(\Delta'-W_0)v\|_{F,w}\le C_2\kappa\|v\|_{X,w}\) (L476), proved in 7.1 from the plaquette Hessian remainder. **Clause (ii).** Reg\(_\alpha\) (`p82.md` (10)) asks for the existence of a real gauge on each cube; if \(U^g=e^{i\eta A_0}\) then \((U^h)^{h^{-1}g}=e^{i\eta A_0}\). So Reg\(_\alpha\) holds for \(U\) iff it holds for every real gauge transform. ∎

*Proof of Theorem 3.10.* Lemmas 3.1–3.7 and clauses (i)–(ii). ∎

## 4. (15) at one real critical reference

**Theorem 4.1.** Let \(U_0\) be a real regular critical configuration on a geometry satisfying `p82.md` §2 step 5 (\(M_P\mid M_1\), \(\rho\ge\rho_P\), torus room), with Reg\(_\alpha\), \(\alpha\le\alpha_*\). Assume P81 at \(U_0\): a holomorphic \(\Phi\) on the datum polydisc of radius \(r_{\rm P81}\), \(\Phi(0)=U_0\), \(M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0\), critical for real \(B\) (`a3-derivative.md` Lemma 6.3). Let \(\kappa\) bound the local potential, gradient and curvature of \(U_0\) on row carriers in the normalization of `a3-derivative.md` §3 (L56), and the current by \(\kappa\xi^{-3}\). There are \(\kappa_*>0\), \(r_*>0\) and \(C_4\), depending only on \(L,\alpha_{\rm H}\) (through \(C^\circ\) and the constants of `a3-derivative.md` §4), such that if \(\kappa\le\kappa_*\) then on the datum polydisc of radius \(r_{\rm B}=\min(r_*,r_{\rm P81})\), at every row direction \(e_c\), (15) holds with \(\theta_4=\min(\delta_0,\delta_w)/8\): the potential, gradient and \(D^{\mathsf T}D\) members at every bond, the current member at every bond whose plaquettes lie in \(\Omega_0\), and the top factor at every top.

*Proof.* By Theorem 3.10, Theorem P at \(U_0\) supplies the premise of `a3-derivative.md` Lemma 8.1 with \(C^\circ\): (4) for every \(w\in\mathcal W_\theta\), \(\theta\le\theta_0=\delta_w/2\) (M1.1), the Hölder member and \(D(1-R)D^{\mathsf T}\) member ((P15)–(P16)), in the counting multiplier (L104), with the outline's \(R\) (M1.2) and \(K_0\) (M1.6); also \(\|\lambda_0\|_Y\le C^\circ\kappa\) (M1.7). I re-derive the chain of `a3-derivative.md` §6–7 that converts this to (15), to fix the constants.

*Step 1 (fixed point).* With \(N_1,N_2\) of (25) and \(N_1^\circ=N_1+(\Delta'-W_0)a\) (Lemma 8.1's proof), (26) gives \(\|N^\circ\|\le C_Nr^2+C_2\kappa r\) and Lipschitz constant \(C_Nr+C_2\kappa\) on \(\|a\|_X+\|\nu\|_Y\le r\le r_*/4\), with \(C_N,C_2\) from (9)–(12) (constants of \(L\) only: §4.1–4.3 count finite one-step stencils, L88–L190). Choose \(\kappa_*\) and \(r\) with \(C^\circ C_2\kappa_*\le1/8\), \(C^\circ C_Nr\le1/8\). Choose \(r_{\rm B}\le r/(4C^\circ C_b)\), \(C_b\) from (30). Then \((a,\nu)\mapsto S^{\circ-1}(-N_1^\circ,\mathsf b(B)-N_2)\) maps the closed radius-\(r\) ball into the radius-\(r/2\) ball with Lipschitz constant \(\le1/4\) (L353). Its fixed point is holomorphic in \(B\) (uniform limit of holomorphic iterates; Cauchy formula on complex lines).

*Step 2 (derivative).* Differentiate at fixed reference: \((1+S^{\circ-1}DN^\circ)(h,\dot\omega)=S^{\circ-1}(0,D\mathsf b(B)e_c)\) ((33)). In every weight \(w\in\mathcal W_\theta\) the perturbation has norm \(\le1/4\) by (26), and (30) gives \(\|D\mathsf b(B)e_c\|_{Y,w_{y_c}}\le C_be^{\theta D_L}|e|\) with \(w_{y_c}=e^{\theta d(\cdot,y_c)}\in\mathcal W_\theta\). So, with \(\theta=\theta_4\),
\[
 \|h\|_{X,w_{y_c}}+\|\dot\omega\|_{Y,w_{y_c}}\le\tfrac43C^\circ C_be^{\theta D_L}|e|=:C_1|e|.\tag{4.1}
\]
This is (34), in the counting normalization.

*Step 3 (Landau identification).* Proposition 6.4 (P81 and Theorem P's isomorphism \(\Delta_U:\ker Q'\to\operatorname{ran}R\)) identifies the fixed point with \((\mathcal H,u)\) and \(\omega^{\rm cnt}=\lambda_0+\nu\). By Lemma 3.5 this pair is choice-independent.

*Step 4 (members).* 7.1 (L435–444): \(D^{\mathsf T}Dh=(DK_a[h])^{\mathsf T}\omega+K_a^{\mathsf T}\dot\omega-\Delta'h-N_0'(a)h\), each term bounded via (9), (11), (12) and \(|\omega|_Y\le C^\circ\kappa+r\): \(\xi_y^3|D^{\mathsf T}Dh|\le C(C_1+1)e^{-\theta d(y,y_c)}|e|\). 7.3 (L455): with \(U_a=e^{i\eta a}U_0\), \(F'(a)=\Xi_a^{\mathsf T}J(U_a)\) at bonds whose plaquettes lie in \(\Omega_0\), \(|\Xi_a-1|\le C\eta|a|\); differentiating \(J(U_a)=(\Xi_a^{\mathsf T})^{-1}K_a^{\mathsf T}\omega\) gives \(\delta J=(\Xi_a^{\mathsf T})^{-1}[(DK_a[h])^{\mathsf T}\omega+K_a^{\mathsf T}\dot\omega]+D((\Xi_a^{\mathsf T})^{-1})[h]\,K_a^{\mathsf T}\omega\); the first bracket is bounded by the same two terms as in 7.1, the last by \(C\eta|h|\cdot C(C^\circ\kappa+r)\xi^{-3}\). Hence \(\xi_y^3|\delta J|\le C(C_1+1)e^{-\theta d}|e|\) at those bonds. 7.5 (L461): \(u_B=v[a]^{-1}\) at tops; the node factor of a level-\(j\) top is a product of \(j\) block means whose derivatives have row norm \(\le C_LL^n\eta\) ((5), (8)); summing, \(|\dot u(y)|\le C_L\sum_{n<j}L^n\eta\sup_{B^j(y)}|h|\le C\sup_{B^j(y)}\xi|h|\le CC_1e^{-\theta d(y,y_c)}|e|\), since the pillar has \(d_{\mathbf B}\)-diameter \(O(1)\).

*Constants.* \(C_4=C(C_1+1)\) with \(C\) a function of \(L\) through §4 and of \(C^\circ(L,\alpha_{\rm H})\). The rate is \(\theta_4=\min(\delta_0,\delta_w)/8\) (P82 §2 step 5, L188: the common rate is decreased to \(\min\{\delta_0,\delta_w\}\), "not reset upwards"). No depth, volume, region, \(M\) or \(\bar\kappa\) enters. ∎

**What I re-derived.** Steps 1–4 above re-check (26)–(34), 7.1, 7.3, 7.5 at the level of the displayed identities. The local bounds (9)–(12) of `a3-derivative.md` §4 are used as written (gated in its rows 85, 89, 98, 100, 101; not re-derived here). The Hölder member 7.4 and the Laplacian member 7.2 are not part of (15).

## 5. The layered class

### 5.1 Definition

**Definition 5.1 (admitted layered class \(\mathfrak C\)).** An element is a pair \((\mathbf S,U)\):
1. \(\mathbf S\) is a separated sequence of `pr-lay.md` (1): members are unions of aligned level-\(j\) \(M_1\)-cubes, \(\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho\xi_j\), \(\rho=R_1M_1\); with \(M_P\mid M_1\), \(\rho\ge\rho_P\) (`p82.md` (11)), the A1 geometric floors, and torus room. The default determining set is used. If \(\mathbf S\) is a stage sequence of pr-lay's "longer class", it is cut at its own depth (pr-lay L22, L326).
2. \(U\) is a real regular critical background for its datum, in any real representative, with **real bound** \(r_0\) in the sense of pr-lay (L38–L46) with cube constant \(c_g\ge c_{\rm reg}\), and current \(l_b^3|J(U)(b)|\le r_0\) at complete bonds.
3. P81 holds at \(U\) (ST1's A1/F0/REG, an import).

\(\mathfrak C(r)\) is the subclass with \(r_0\le r\).

The *admitted* class of ST1 Theorem 14 is the set of systems used by ST1. pr-lay's admission inputs G, B, Q (L217–L240) state when the actual stage, prepared and retained sequences and their backgrounds belong to \(\mathfrak C(r)\); Lemmas 5.2–5.4 make this precise.

### 5.2 Lemmas

**Lemma 5.2 (geometry).** pr-lay's G, with \(M_1\mid M\), \(LM\ge2\rho\) and \(cM\ge2\rho\) (pr-lay §2 step 3), implies item 1 of Definition 5.1 except the P82 floors, which are floors on \(M_1,R_1\) fixed earlier.

*Proof.* pr-lay Lemma 5 (L258): "G and the floors on \(M\) imply (1)." An \(M\)-cube is a union of \(M_1\)-cubes, hence of aligned \(M_P\)-cubes when \(M_P\mid M_1\). The floors \(\rho\ge\rho_P\), (13) and A1's are imposed when \(M_1,R_1\) are chosen (IN1 row 3; pr-lay §2 step 2 asks \(\rho\) "above all imported floors"). ∎

**Lemma 5.3 (real bound gives Reg).** If \(U\) has real bound \(r_0\) with \(c_g\ge c_{\rm reg}\) and \(M_P\mid M_1\), then \(U\) satisfies Reg\(_{2r_0}\) of `p82.md` (10).

*Proof.* Reg\(_\alpha\) concerns embedded cubes \(Z\) of side \(c_{\rm reg}M_P\xi_j\) in \(\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})\). Since \(M_P\le M_1\) and \(c_{\rm reg}\le c_g\), \(Z\) has side \(\le c_gM_1\xi_j\), so pr-lay's real bound gives a real gauge with \(\xi_j|A|,\xi_j^2|\nabla A|\le r_0\) "throughout the cube on contained stencils" (pr-lay L45). The sum is \(\le2r_0\). ∎

The choice \(c_g\ge c_{\rm reg}(L)\) is legal: both are fixed at the first step with \(L\) (pr-lay §2 step 1: "\(c_g\ge1\), large enough for the imported local models"; P82 §2 step 1).

**Lemma 5.4 (admission makes the bound small).** Under pr-lay's G, B, Q, the real bound of the actual background is \(\le C_Gv\) and its current bound is \(\le C_{\rm RA}C_\lambda A_0\sup_m\theta_m^{-1/2}(\log\theta_m)^{p_0+2r_R}\), with \(C_G=8L^4B_*(c_gM_1+2L)\); both tend to zero with the coupling ceiling \(\gamma\).

*Proof.* pr-lay Lemma 6 (L263–L303) gives the real bound \(C_Gv\) under (21); B (17) gives the current bound; Lemma 7 (L305–L315) gives \(\sup_{t\ge\gamma^{-2}}t^{-1/2}(\log t)^Q\le F_Q(\gamma)\to0\). ∎

**Lemma 5.5 (the A3 curvature parameter).** If \(U\in\mathfrak C(r)\), the parameter \(\kappa\) of Theorem 4.1 satisfies \(\kappa\le C_{\rm car}r\), with \(C_{\rm car}=C(L)\).

*Proof.* A row carrier of a level-\(j\) row is its double block, of side \(\le2L\xi_j\) at adjacent scales (`a3-derivative.md` §3, L39). It lies in a cube of side \(c_{\rm reg}M_P\xi_j\) inside \(\mathcal L_j\cup\mathcal L_{j+1}\) or, at a seam, inside the concentric cube of side \(c_{\rm reg}M_P\xi_j/L\) (`p82.md` L245, the proof of Lemma 1). Lemma 5.3's gauge gives \(\xi|A|,\xi^2|\nabla A|\le2r\) there, with at most an \(L\)-factor for the scale change. The curvature of a plaquette is gauge invariant and \(\le\eta^2l_p^{-2}r\) by the real bound. The current bound is item 2. ∎

**Lemma 5.6 (datum regularity for P81).** If \(U\in\mathfrak C(r)\) with \(r\le cL^{-2}\), its datum \(M_{\mathbf B}(U)\) is \(CL^2r\)-regular.

*Proof.* SA 9660, the last sentence of Theorem 1 (quoted in §1.4); also ST1's AV/CURV (L128): "The resulting test bound is \(2\epsilon\) inside a layer and \(C_{\rm sm}L^2\epsilon\) across a seam." ∎

So P82 Theorem P82's own hypothesis \(\varepsilon_1\le\varepsilon_P\) also holds once \(CL^2r\le\varepsilon_P\). This is not needed for Theorem 5.7, which uses Theorem P directly at the given representative.

### 5.3 The theorem

**Theorem 5.7 ((15) uniformly on the admitted layered class).** Fix \(L\), \(\alpha_{\rm H}\) and the constants of `p82.md` §2 steps 1–4 and of `a3-derivative.md` §4. Put
\[
 r_{\mathfrak C}=\min\{\alpha_*/2,\ \kappa_*/C_{\rm car},\ cL^{-2}\}.\tag{5.1}
\]
Then for every \((\mathbf S,U)\in\mathfrak C(r_{\mathfrak C})\), on the datum polydisc of radius \(r_{\rm B}\) of Theorem 4.1 (intersected with P81's), (15) holds at interior elements with constants \(C_4(L,\alpha_{\rm H})\) and \(\theta_4=\min(\delta_0,\delta_w)/8\). The constants and \(r_{\mathfrak C}\) do not depend on depth, volume, torus, region shape, number of layers, \(M_1,R_1\) above their floors, \(M\) or \(\bar\kappa\). They are fixed at IN1 row 3 (c4-order rows 4–7), before \(\kappa\). Under pr-lay's G, B, Q, every actual stage system belongs to \(\mathfrak C(r_{\mathfrak C})\) once \(\gamma\le\gamma_{15}\), where \(\gamma_{15}\) is defined by \(C_GC_{\rm RA}C_\lambda A_0F_{p_0+2r_R}(\gamma_{15})<r_{\mathfrak C}\) and may depend on \(M_1\) and on the post-\(M\) amplitude \(A_0\) (IN1 rows 6, 9).

*Proof.* Lemma 5.3 gives Reg\(_{\alpha}\) with \(\alpha\le\alpha_*\); Lemma 5.2's geometry and the floors make Theorem P applicable (clause (ii) of Theorem 3.10: any real representative). Lemma 5.5 gives \(\kappa\le\kappa_*\). P81 is item 3. Theorem 4.1 gives (15) with constants depending on \(L,\alpha_{\rm H}\) only. For the admission statement, Lemma 5.4 and Lemma 7 of pr-lay. ∎

**Remarks.**
1. *Interior elements.* The current member is proved at bonds whose plaquettes lie in \(\Omega_0\), as ST1 L135 records.
2. *Mean-axial base (Amendment CV).* ST1 uses the averaged-contour representative (`st1-r4.md` L41). Theorem P applies at it directly (clause (ii)); P81 transfers by the residual gauge (SA 9676: both representatives lie in one \(\mathcal G^{\rm res}\) orbit, and the constraint is unchanged by gauges equal to \(\mathbf 1\) at the nodes). This agrees with ST1 L1180.
3. *Uniformity in \(M_1\).* \(C_G\) of Lemma 5.4 grows with \(M_1\). It enters only \(\gamma_{15}\), not \(C_4,\theta_4\).
4. *Imports.* Theorem 5.7 is an implication from: P82 Theorem P (frozen; I1–I5, I8); P81 (A1/F0/REG); `a3-derivative.md` §4 bounds and §6.1 identification (gated); pr-lay's G, B, Q for the admission statement (frozen pr-lay imports them as hypotheses). It proves none of these.

## 6. Status of Part I

- **M1: proved** (Theorem 3.10). It is a statement about definitions; it uses Theorem P only for injectivity and onto-ness.
- **(15) at a real critical reference: proved as an implication** (Theorem 4.1).
- **(15) uniformly on the admitted layered class: proved as an implication** (Theorem 5.7), with the constant order required by ST1 Theorem 14 hypothesis 1.
- **Not proved here:** P81, the complex-reference extension of P82 (needed by `a3-derivative.md` 9.1 for non-critical pairs, not by (15)), periodisation, (G1), M2.

---

# Part II. PR-H

## 7. What the texts say

`ym4-assembly.md` L188: "6. *Counterterm accounting and profile inputs of A2* ⟦open: PR-H⟧: (H-ct) (SA L7864) and (H-prof)." `assembly-status.md` L52: "No later text mentions it." The statements are in `a2-full.md` (Claude, unrefereed; its gate `gates/a2-full-gate.md` by Codex):

- **(H-prof)**, `a2-full.md` L166: "Input (H-prof): |x_k(p) - x_k| <= C_x (1 + n(p)), also for complex x." Here (L139) "Let n(p) := k - j(p) be the depth of the layer of p", for the step's background, which (L137) "is real and critical for the depth-k sequence with datum V_k^bg". L250: "(H-prof): reduced in Corollary IV.1 to the reading "small-field region of step i" = Omega_i and "interior region" = Lambda_i (SA 6331), and to the premise that the step's background lives on the label's regions." The gate (L120): "The region-name interpretation remains part of H-prof … it has not been discharged by this gate."
- **(H-ct)**, `a2-full.md` L180: "On the step's complex fluctuation domain {B : |g_k B(c)| < r_k for every active row c}, the subtracted brackets sum_{j<=k}{E^(j) - b_j A(phi_j, .)}, together with the aged remainders, admit a representation sum_Y F_Y(B). Here Y runs over connected unions of level-k cubes of side M, each F_Y is holomorphic and depends only on B on Y, and |F_Y| <= eps_ct e^{-kappa |Y|}, with eps_ct <= C sum_{n>=1} omega_n and omega_n <= C(n+1)^{3/2} L^{-alpha_H(n-1)} at age n = k+1-j." The gate (L132–L134): "This uses H-ct's **local dependence on fluctuation coordinates in Y**, not merely polymer locality before composing with the background. That strong premise is left untouched. At a centre with ||g_k B_0||_infty<=v r_k, v<1, the same proof costs (1-v)^(-2) … A claim on a complex reference family must retain that uniform version of H-ct."
- **Consumers.** Theorem IV (L154), Corollary IV.1 (L166) and Theorem V (L182); Theorem A2-full (L212). a2-full's own remark (L190): "Where the consumer keeps these brackets in the integrand instead of the precision, as (FG5) allows, no comparison with A is needed. … Theorem V is needed only for a consumer that absorbs their quadratic part into the Gaussian."

**The fine-mesh Hölder estimate.** `fp1.md` L50 (D4): "These are discrete, current-scale estimates. They are not mesh-uniform pointwise bounds for a physical fine-mesh Green-function density." `fp1.md` L495 (change log): "at current scale the Holder clause follows from the kernel bound; it is not a fine-mesh Holder estimate, and PR1's clause (H) cannot cite FP1(2) for that." PR1's clause (H) is `bx-fix.md` §2.2 (L50): every cube \(D\subset X\) of side \(\le C_{\rm box}LM\) "has a unitary gauge g on D with U = (e^{iη_ℓ A_r})^g, such that in level-ℓ units \(|A_r|,|\nabla A_r|,[\nabla A_r]_{\alpha_H,D}<C_{\rm pot}Ma_0\), \([\nabla A'']_{\alpha_H,D}<a_1\)". SA's mesh-uniform estimate is SA 12385–12900 (BGH1–BGH30). SA 12774–12775 says what it does not do: "This proves the H\"older implication once (BGH24) is known; it does not construct the gauge or prove the nonlinear Laplacian estimate in (BGH24)." §9 below constructs that gauge and proves that Laplacian estimate for the real regular background. (The response's fine-mesh Hölder member is already in frozen P82 Theorem P, from import I3 = flat-port (4.1)–(4.2), not from FP1(2); `p82.md` L150, L415.)

## 8. (H-prof)

### 8.1 The objects

SA 6331–6334: "Profiles \(\varphi_j\) are supplied real functions on plaquette midpoints, equal to zero outside their prescribed small-field regions and to one on their prescribed interior regions. The interpolation rule in the intervening layers is part of the data. With \(x_k(p)=\beta-\sum_{j\le k}b_j\varphi_j(p)\), the exponent is …". SA 17440: "The choice \(\boldsymbol\nu=n\) gives the *determining sequence* … It governs the determining sets, \(U_k(\mathbf V)\) and the propagators … The choice \(\boldsymbol\nu=0\) gives the *action sequence* … It governs the index sets of \(\mathbf E_k,\mathbf R_k,\mathbf B_k\), the profiles \(\varphi_j\) and hence \(x_k(\cdot)\) … No single sequence can play both roles." So the profiles live on the **action** sequence, while \(n(p)\) in (H-prof) is read in the step's background sequence, the **determining** sequence. (H-prof) as stated compares two different sequences. a2-full's reduction (L250) reads both with one set of regions. That is where it fails (Proposition 8.6).

Write \(\Omega^{\rm a}_l,\Lambda^{\rm a}_l\) for the action sequence and \(\Omega^{\rm d}_l\) for the determining sequence of the label at the step, \(l\le k\). For a plaquette \(p\) meeting \(\Omega_0\) (membership by midpoint), put
\[
 j_{\rm a}(p)=\max\{l\le k:p\in\Omega^{\rm a}_l\},\quad j_{\rm d}(p)=\max\{l\le k:p\in\Omega^{\rm d}_l\},\quad n_{\rm a}=k-j_{\rm a},\quad n_{\rm d}=k-j_{\rm d}.
\]
\(n_{\rm d}(p)\) is a2-full's \(n(p)\). The scalar coupling is \(x_k=\beta-\sum_{1\le l\le k}b_l\) (IN1 L605: "\(x_{k+1}=x_k-b_{k+1}\)", with \(\theta_0=x_0=\beta\), L602). Put \(b_0=0\).

**Hypotheses (PD), on the supplied data.**
- (PD1) \(0\le\varphi_l\le1\). SA 6331 leaves the interpolation to the data. SA 22410 states "Choose also profiles \(0\le\varphi_j(p)\le1\)" in the source chapter; a2-full L28 reads \(\varphi_j\in[0,1]\). I take (PD1) as a hypothesis. If only \(|\varphi_l|\le\Phi_0\), replace \(1\) by \(1+\Phi_0\) below.
- (PD2) \(\varphi_l(p)=1\) if \(p\in\Lambda^{\rm a,\sim-1}_l\) (the interior region less one layer of level-\(l\) \(M\)-cubes) and \(\varphi_l(p)=0\) if \(p\notin\Omega^{\rm a}_l\). This allows one cube of margin, as a2-full L166 does.
- (PD3) The action sequence is nested as in SA Proposition 2.3 (SA 17398–17407): \(\Omega^{\rm a}_{l+1}\subset\Lambda_l^{\rm a,\sim-1}\subset\Lambda^{\rm a}_l\subset\Omega^{\rm a}_l\). SA 17440 says each \(\Omega^{\boldsymbol\nu}\) "is the label of an actual history … and so Proposition 2.3 applies to it".
- (PD4) The drop-out windows (SA 17415–17440). Let \((t,X)\) be a standing drop-out mark, \(t_\flat=t-\mathsf N_t\), with \(n(X)\le\mathsf N_t\) stages (SA 17419). Then for \(t_\flat<l\le t_\flat+n(X)\): \(\Omega^{\rm d}_l\cap X=X\setminus Z''_l(X)\) and \(\Omega^{\rm a}_l\cap X=\Omega^\circ_l\cap X\), where \(\Omega^\circ\) are the regions before the operation (SA 17432–17436 with \(\boldsymbol\nu=n\), resp. \(0\)); outside this window the two sequences agree on \(X\). Also \(Z''_l(X)\subset X\setminus\Omega^\circ_l\) (SA 17415: "The nest consists of increasing boxes in \(\Omega_l^c\cap X\)"). And "Marks wait" (SA 17440): "a mark of level \(s\) lying inside a class component of level \(t\) satisfies \(s<t_\flat\). Hence standing marks that share a part are nested, their windows \((s_\flat,s]\) are disjoint".
- (PD5) **Coupling increments.** \(|b_l|\le B_b:=c_0+2c_2+1\) for \(1\le l\le k\). This follows from IN1 (10)–(11) (L112, L122): \(b_l=b^0_l+e_l\), \(b^0_l=\mathcal A_l-\mathcal A_{l-1}\), \(|\mathcal A_l-lc_0|\le c_2\), \(|e_l|\le u(\theta_{l-1})\le1\) once \(X_0\) is large (IN1 row 9). These are IN1's H-OL and H-SF imports. Complex \(b_l\) with the same bound are allowed.
- (PD6) **Frame.** \(\theta_i-\theta_j\le\overline B(j-i)\) for \(i\le j\) (IN1 (1), L19), \(\theta_j\ge X_0>e\), and \(\mathsf N_t=R_t=\lceil(\log m_t)^r\rceil_{L^{\mathbb N_0}}\), \(m_t=\min_{i\le t}\theta_i\) (IN1 L22; SA 17334 gives the same definition with \(x\)). On the run \(\theta_j=x_j\) (IN1 L605).

### 8.2 Lemmas

**Lemma 8.2 (one sequence).** Under (PD1)–(PD3) and (PD5), \(|x_k(p)-x_k|\le B_b(1+n_{\rm a}(p))\).

*Proof.* \(x_k(p)-x_k=\sum_{l\le k}b_l(1-\varphi_l(p))\). If \(l\le j_{\rm a}(p)-1\), then \(p\in\Omega^{\rm a}_{j_{\rm a}}\subset\Omega^{\rm a}_{l+1}\subset\Lambda^{\rm a,\sim-1}_l\) by (PD3), so \(\varphi_l(p)=1\) by (PD2) and the term vanishes. The remaining indices are \(j_{\rm a}\le l\le k\): there are \(n_{\rm a}+1\) of them, each with \(|b_l(1-\varphi_l)|\le B_b\) by (PD1), (PD5). ∎

**Lemma 8.3 (action against determining).** Under (PD4): \(j_{\rm a}(p)\le j_{\rm d}(p)\) for every \(p\). If \(j_{\rm d}(p)\) lies in the window \((t_\flat,t_\flat+n(X)]\) of a standing drop-out mark \((t,X)\) with \(p\in X\), then \(j_{\rm a}(p)\ge t_\flat\) and \(k-t\le n_{\rm d}(p)\); otherwise \(j_{\rm a}(p)=j_{\rm d}(p)\). Hence
\[
 n_{\rm a}(p)\le n_{\rm d}(p)+\mathsf N_{t(p)}\mathbb 1_{\rm win}(p),\qquad k-t(p)\le n_{\rm d}(p).\tag{8.1}
\]

*Proof.* *Inclusion.* At a level \(l\) in the window of a mark \((t,X)\), on \(X\): \(\Omega^{\rm a}_l\cap X=\Omega^\circ_l\cap X\subset X\setminus Z''_l(X)=\Omega^{\rm d}_l\cap X\), since \(Z''_l(X)\cap\Omega^\circ_l=\varnothing\). Elsewhere the sequences agree. So \(\Omega^{\rm a}_l\subset\Omega^{\rm d}_l\) for all \(l\), and \(j_{\rm a}\le j_{\rm d}\). *No window.* If \(j_{\rm d}(p)\) is in no window at \(p\), the two sequences agree at level \(j_{\rm d}\) at \(p\), so \(p\in\Omega^{\rm a}_{j_{\rm d}}\) and \(j_{\rm a}\ge j_{\rm d}\). *Window.* By Marks wait, windows at \(p\) are disjoint, so \(j_{\rm d}(p)\) lies in exactly one, that of \((t,X)\). The level \(t_\flat\) is in no window at \(p\): it is not in \((t_\flat,t]\); a mark \((s,X')\ni p\) inside \(X\)'s class component has \(s<t_\flat\) (Marks wait), so \((s_\flat,s]\not\ni t_\flat\); a mark \((s,X')\) with \(X\) inside its component has \(t<s_\flat\) by Marks wait applied to it, so \(t_\flat<s_\flat\). Since standing marks sharing a part are nested, there is no other case. So the sequences agree at level \(t_\flat\) at \(p\). Now \(p\in\Omega^{\rm d}_{j_{\rm d}}\subset\Omega^{\rm d}_{t_\flat}\) because \(j_{\rm d}>t_\flat\) and the sequence is nested. Thus \(p\in\Omega^{\rm a}_{t_\flat}\) and \(j_{\rm a}\ge t_\flat\). Since \(j_{\rm d}\le t_\flat+n(X)\le t_\flat+\mathsf N_t=t\), we get \(k-t\le k-j_{\rm d}=n_{\rm d}\), and \(n_{\rm a}=k-j_{\rm a}\le k-t_\flat=k-t+\mathsf N_t\le n_{\rm d}+\mathsf N_t\). ∎

**Lemma 8.4 (stage count).** Under (PD6), for \(t\le k\),
\[
 \mathsf N_t\le L\,2^{r-1}\big[(\log\theta_k)^r+r^r(1+\overline B(k-t))\big].\tag{8.2}
\]

*Proof.* The smallest power of \(L\) not less than \(y\ge1\) is at most \(Ly\); \((\log m_t)^r\ge1\) since \(m_t\ge X_0>e\). So \(\mathsf N_t\le L(\log m_t)^r\le L(\log\theta_t)^r\). By (PD6), \(\theta_t\le\theta_k+\overline B(k-t)\le\theta_k(1+\overline B(k-t))\) (as \(\theta_k\ge1\)). So \(\log\theta_t\le\log\theta_k+\log(1+\overline B(k-t))\). Use \((u+v)^r\le2^{r-1}(u^r+v^r)\) for \(u,v\ge0\), \(r\ge1\) (convexity), and \(\log(1+y)\le r((1+y)^{1/r}-1)\le r(1+y)^{1/r}\), which gives \((\log(1+y))^r\le r^r(1+y)\). ∎

### 8.3 The corrected statement and the failure of the literal one

**Theorem 8.5 ((H-prof♯)).** Under (PD1)–(PD6), for every plaquette \(p\) meeting \(\Omega_0\),
\[
 |x_k(p)-x_k|\le C_x(1+n_{\rm d}(p))+C'_x(\log\theta_k)^r,\qquad
 C_x=B_b\big(1+L2^{r-1}r^r(1+\overline B)\big),\quad C'_x=B_bL2^{r-1}.\tag{8.3}
\]
The constants depend only on \(c_0,c_2,\overline B,L,r\), all fixed at IN1 rows 1–2. The same holds for complex \(b_l\) with \(|b_l|\le B_b\).

*Proof.* Lemma 8.2 and (8.1): \(|x_k(p)-x_k|\le B_b(1+n_{\rm d}+\mathsf N_{t(p)}\mathbb 1_{\rm win})\). By (8.2) and \(k-t(p)\le n_{\rm d}\), \(\mathsf N_{t(p)}\le L2^{r-1}[(\log\theta_k)^r+r^r(1+\overline B n_{\rm d})]\). Collect terms, using \(1+\overline Bn\le(1+\overline B)(1+n)\). ∎

**Proposition 8.6 (the literal (H-prof) fails at drop-out windows).** Assume (PD1)–(PD6) and the lower half of IN1 (10): \(\sum_{l=a}^{k}b_l\ge(c_0/2)(k-a+1)-2c_2\) (this holds when \(u\le c_0/2\)). Suppose an admitted history has, at step \(k\), a standing drop-out mark \((t,X)\) with \(k-t=m\), \(n(X)=\mathsf N_t\), and a plaquette \(p\) in \(X\) with \(p\in\Omega^\circ_{t_\flat}\setminus\Omega^\circ_{t_\flat+1}\) and \(p\in X\setminus Z''_t(X)\). Then \(n_{\rm d}(p)=m\) and
\[
 x_k(p)-x_k\ \ge\ \tfrac{c_0}2(m+\mathsf N_t)-2c_2-B_b.\tag{8.4}
\]
Consequently no constant \(C_x\) can satisfy \(|x_k(p)-x_k|\le C_x(1+n(p))\) for all such histories if \(\mathsf N_t\) is unbounded over them (for instance as \(\beta\to\infty\) with \(m\) fixed, since \(\mathsf N_t\ge(\log m_t)^r\)).

*Proof.* \(p\in X\setminus Z''_t\) gives \(p\in\Omega^{\rm d}_t\) (window level \(l=t=t_\flat+n(X)\)), and \(p\notin\Omega^{\rm d}_{t+1}\) because \(t\) is the top of the window and \(X\cap\Omega_{t+1}=\varnothing\) (SA Prop. 2.3, \(\operatorname{dist}(Z_t,\Omega_{t+1})\ge LM\), with \(X\subset Z_t\)). So \(j_{\rm d}=t\), \(n_{\rm d}=m\). In the action sequence \(j_{\rm a}(p)=t_\flat\). By (PD2), \(\varphi_l(p)=0\) for \(l\ge t_\flat+1\), and \(\varphi_l(p)=1\) for \(l\le t_\flat-1\) (Lemma 8.2). So \(x_k(p)-x_k=b_{t_\flat}(1-\varphi_{t_\flat}(p))+\sum_{l=t_\flat+1}^kb_l\ge-B_b+(c_0/2)(k-t_\flat)-2c_2\), and \(k-t_\flat=m+\mathsf N_t\). ∎

I did not prove that such histories exist; that is a statement about the history construction (H-G). SA 17419 admits drop-outs after "\(n\le\mathsf N_t\)" stages. I also did not check whether the actual step exponent puts a profile weight on plaquettes inside drop-out components: SA 7559 says that for a drop-out "the Wilson weight of the carrying term over \(X\) appears inside the integral". a2-full's Theorem IV, as written, sums over every plaquette meeting \(\Omega_0\). If a consumer excludes the drop-out regions, the literal statement may survive on what remains. Theorem 8.5 does not need this distinction.

### 8.4 The consumer still closes

**Corollary 8.7 (Corollary IV.1 with (H-prof♯)).** Take a2-full's Theorem IV in the repaired form of `gates/a2-full-gate.md` (D1–D3: ambient/free convention, the correct complex chart with constant \(C_{\rm IV}(L,\theta,r_{\rm B})\), and the fixed boundary completion). With \(w(p)=(x(p)-x_k)/t\), \(|t/x_k-1|\le1/2\), the signed-profile perturbation satisfies
\[
 \|P_{\rm prof}\|\le\tfrac83C_{\rm IV}\big(C_x+C'_x(\log\theta_k)^r\big)\theta_k^{-1}.\tag{8.5}
\]
So A2-full's first ceiling \(RC_{\rm IV}(C_x+C_\zeta)g_k^2\le c_L/20\) becomes \(\tfrac83RC_{\rm IV}(C_x+C'_x(\log\theta_k)^r+C_\zeta)\theta_k^{-1}\le c_L/20\). It holds for all \(\theta_k\ge X_0\) once \(X_0\) is large, because \(\theta^{-1}(\log\theta)^r\) is decreasing for \(\theta\ge e^r\) and tends to zero. This is a further increase of \(X_0\) at IN1 row 9, after \(R\), \(C_{\rm IV}\) and \(C_x,C'_x\).

*Proof.* \(P_w\) is linear in \(w\). Split \(w=w_0+w_1\) with \(|w_0(p)|\le(C_x/|t|)(1+n_{\rm d}(p))\) and \(|w_1(p)|\le C'_x(\log\theta_k)^r/|t|\) (choose \(w_0=w\cdot\min\{1,\ C_x(1+n_{\rm d})/|x(p)-x_k|\}\), \(w_1=w-w_0\)). Theorem IV applies to each with \(\omega_0=C_x/|t|\), resp. \(\omega_0=C'_x(\log\theta_k)^r/|t|\) (a constant weight satisfies \(|w_1|\le\omega_0(1+n)\)). Sum the bounds. Finally \(|t|\ge x_k/2\) and \(x_k\ge\tfrac34\theta_k\) by the tube (IN1 (3)). ∎

**Status of (H-prof).** The literal statement is **refuted** for any history with the configuration of Proposition 8.6 and unbounded \(\mathsf N_t\). The corrected statement (8.3) is **proved** from (PD1)–(PD6). (PD1) and (PD2) are readings of SA 6331 and SA 22410 for the supplied profile data; (PD3)–(PD4) are SA Proposition 2.3 and SA 17415–17440; (PD5)–(PD6) are frozen IN1's hypotheses. The consumer closes with one more increase of \(X_0\) (Corollary 8.7).

## 9. The fine-mesh Hölder estimate for the real background

### 9.1 Statement

Work on \(\eta\mathbb Z^4\) (a cube that embeds in the torus without wrapping, with its margins, is the same). Forward and backward differences \(D_i^\pm\), \(\nabla_i=D_i^+\), \(\nabla_i^-=D_i^-\), \(\Delta_\eta=\sum_iD_i^-D_i^+\) (SA (BGH1), SA 12397–12402). \(Q_r(x)=\{y:|y-x|_\infty\le r\}\). Colour components are taken in a fixed orthonormal basis; norms of colour vectors are Euclidean, of \(2\times2\) matrices the operator norm. A 1-form \(A\) has components \(A_\mu(x)=A(x,x+\eta e_\mu)\). \([f]_{\alpha,Q}=\sup\{|f_\bullet(x)-f_\bullet(x')|/|x-x'|^\alpha\}\) over \(x\ne x'\in Q\) and like components, with Euclidean \(|x-x'|\) (as in `bx-fix.md` L48 and SA 12404).

**Wilson current.** With IN1's action \(a_p=1-\tfrac12\operatorname{Re}\operatorname{Tr}\partial U(p)\) (IN1 L10–L11), the left-variation gradient in the fine pairing is
\[
 J(U)(b)=\eta^{-3}\sum_{p\ni b}\pi(P_{p,b}),\qquad\pi(P)=\frac{P-P^*}{2i},\tag{9.1}
\]
where \(P_{p,b}\) is the holonomy of \(p\) started at \(b_-\) and traversed first along \(b\). *Proof.* For \(v\) Hermitian traceless, \(\frac{d}{dt}a_p(e^{it\eta v}U)=-\frac12\operatorname{Re}\operatorname{Tr}(i\eta vP_{p,b})=\frac\eta2\operatorname{Im}\operatorname{Tr}(vP_{p,b})=\frac\eta2\operatorname{Tr}(v\pi(P_{p,b}))=\eta\langle v,\pi(P_{p,b})\rangle\), using \(\operatorname{Tr}(vP^*)=\overline{\operatorname{Tr}(vP)}\). \(a_p\) does not depend on orientation. Sum over \(p\ni b\) and compare with \(\eta^4\langle v,J(b)\rangle\). For \(P\in SU(2)\), \(\operatorname{Tr}P\) is real, so \(\pi(P)\) is traceless Hermitian. Under \(U\mapsto U^g\), \(J(b)\mapsto\operatorname{Ad}(g(b_-))J(b)\). ∎ Another fixed normalization of the action changes only constants below.

**Hypotheses (F).** Let \(\xi\ge\eta\) (the local scale), \(s\ge0\), \(Q=Q_s(x_0)\), \(Q^+=Q_{s+8\xi}(x_0)\). \(U\) is a real field on the bonds of \(Q^+\) such that
- (F1) \(|\partial U(p)-\mathbf 1|\le\varepsilon\eta^2\xi^{-2}\) for every plaquette of \(Q^+\);
- (F2) \(|J(U)(b)|\le\varepsilon\xi^{-3}\) for every bond whose six plaquettes lie in \(Q^+\);
- (F3) there is a real gauge \(g_1\) on \(Q^+\) with \(U^{g_1}=e^{i\eta A_1}\), \(|A_1|\le a\xi^{-1}\), \(|\nabla A_1|\le a\xi^{-2}\) on all stencils in \(Q^+\);
- (F4) \(\varepsilon\le a\le a_{\rm FH}\), where \(a_{\rm FH}\) is the absolute constant of Lemma 9.6 and (9.20).

**Theorem 9.9 (fine-mesh Hölder estimate).** Under (F), for each \(0<\alpha<1\) there is a real gauge \(g\) on \(Q\) with \(U^g=e^{i\eta A}\) and, on \(Q\),
\[
 |A|\le C_{\rm F}a\xi^{-1},\qquad|\nabla A|\le C_{\rm F}a\xi^{-2},\qquad[\nabla A]_{\alpha,Q}\le C_{{\rm F},\alpha}a\xi^{-2-\alpha}.\tag{9.2}
\]
\(C_{\rm F}\) is absolute (dimension four, \(SU(2)\)); \(C_{{\rm F},\alpha}\) depends only on \(\alpha\). Nothing depends on \(\eta/\xi\), on \(s\) or on the volume.

The proof is in §9.2–9.4. §9.2 rebuilds SA's mesh-uniform estimate (SA 12385–12740), with its proof written out; credit Sussman and Alpoge, with Claude and Codex as authors of their text. §9.3 is new: a gauge in which the background has a bounded componentwise Laplacian. That is the step SA 12774–12775 leaves open.

### 9.2 Mesh-uniform interior estimates (rebuilt from SA)

**Lemma 9.1 (heat-kernel tails; SA (BGH2)–(BGH5)).** Let \(q_T(n)=(2\pi)^{-4}\int_{[-\pi,\pi]^4}e^{-T\omega(\theta)}e^{in\cdot\theta}d\theta\), \(\omega(\theta)=4\sum_i\sin^2(\theta_i/2)\), and \(p_t^\eta(\eta n)=\eta^{-4}q_{t/\eta^2}(n)\). Then \(q_T\ge0\), \(\sum_nq_T(n)=1\), and for integers \(r,N\ge0\) there is \(C_{r,N}\), independent of \(\eta,t,a\), with
\[
 \sum_{|x|\ge a}\eta^4|D^rp_t^\eta(x)|\le\begin{cases}C_{r,N}t^{-r/2}(1+a/\sqrt t)^{-N},&t\ge\eta^2,\\ C_{r,N}\eta^{-r}(1+a/\eta)^{-N},&0\le t\le\eta^2.\end{cases}\tag{9.3}
\]
Here \(D^r\) is any product of \(r\) differences from (BGH1).

*Proof.* (SA 12419–12530.) With \(\mathsf A\) the sum of the eight nearest-neighbour translations, \(\Delta_1=\mathsf A-8I\) and \(e^{T\Delta_1}=e^{-8T}\sum_kT^k\mathsf A^k/k!\); every coefficient is \(\ge0\) and \(e^{T\Delta_1}1=1\); Fourier transformation gives \(q_T\). A product of \(r\) unit differences has multiplier \(m_r(\theta)\), a product of factors \(e^{\pm i\theta_i}-1\); assigning derivatives to factors gives \(|\partial^bm_r|\le C|\theta|^{(r-|b|)_+}\). On \([-\pi,\pi]^4\), \(\omega\ge c|\theta|^2\) (as \(\sin^2(u/2)\ge u^2/\pi^2\) for \(|u|\le\pi\)), \(|\nabla\omega|=O(|\theta|)\), higher derivatives bounded. For \(T\ge1\) the product rule gives \(|\partial^be^{-T\omega}|\le C_bT^{|b|/2}(1+|\sqrt T\theta|)^{M_b}e^{-c_bT|\theta|^2}\). With Leibniz and the substitution \(\theta=T^{-1/2}v\), \(\int|\partial^b(m_re^{-T\omega})|^2\le C_{r,b}T^{|b|-r-2}\). Parseval, expanding \((1+|n|^2/T)^M\) into monomials, gives \(\sum_n(1+|n|^2/T)^M|\delta^rq_T(n)|^2\le C_{r,M}T^{-r-2}\); no boundary terms arise since the multipliers are smooth and periodic. For \(M>N+2\), comparison with the radial integral on unit cubes gives \(\sum_{|n|\ge A}(1+|n|^2/T)^{-M}\le C_{M,N}T^2(1+A/\sqrt T)^{-2N}\). Cauchy–Schwarz then gives \(\sum_{|n|\ge A}|\delta^rq_T(n)|\le CT^{-r/2}(1+A/\sqrt T)^{-N}\). For \(0\le T\le1\) all derivatives of \(m_re^{-T\omega}\) are bounded, and the same argument gives \(C(1+A)^{-N}\). Finally \(\sum_x\eta^4|D^rp^\eta_t(x)|=\eta^{-r}\sum_n|\delta^rq_{t/\eta^2}(n)|\); substitute \(T=t/\eta^2\), \(A=a/\eta\). ∎

**Lemma 9.2 (massive resolvent; SA (BGH11)–(BGH19)).** For \(\mu>0\) put \(G_\mu^\eta=\int_0^\infty e^{-\mu^2t}p^\eta_tdt\) and \(R_\mu f=G^\eta_\mu*f\) (convolution with measure \(\eta^4\times\)counting). Assume \(\mu\eta\le1\). Then:
- (a) \((-\Delta_\eta+\mu^2)R_\mu f=f\), \(\|R_\mu f\|_\infty\le\mu^{-2}\|f\|_\infty\), and every bounded solution of \((-\Delta_\eta+\mu^2)v=f\) equals \(R_\mu f\);
- (b) \(\sum_x\eta^4|DG^\eta_\mu(x)|\le C_{\rm G}\mu^{-1}\), hence \(\|DR_\mu f\|_\infty\le C_{\rm G}\mu^{-1}\|f\|_\infty\);
- (c) \([DR_\mu f]_\alpha\le C_\alpha\mu^{\alpha-1}\|f\|_\infty\);
- (d) for \(R\ge\eta\), \(c>0\), \(r=0,1,2,3\): \(\sum_{|x|\ge cR}\eta^4|D^rG^\eta_{1/R}(x)|\le C_{r,c}R^{2-r}\).

*Proof.* (a) \(\Delta_\eta\) is bounded on \(\ell^\infty\) (norm \(\le16\eta^{-2}\)), so \(\frac{d}{dt}(e^{-\mu^2t}e^{t\Delta_\eta})=e^{-\mu^2t}e^{t\Delta_\eta}(\Delta_\eta-\mu^2)\) in operator norm. Integrate over \([0,\infty)\): \((\mu^2-\Delta_\eta)R_\mu=I\). Heat contraction (\(q_T\ge0\), mass one) gives the sup bound. For a bounded solution \(v\), integrate the same derivative applied to \(v\); the terminal term vanishes by \(e^{-\mu^2t}\) and contraction; so \(v=R_\mu f\). (b) Integrate (9.3) with \(r=1\), \(a=0\): \(\int_0^{\eta^2}C\eta^{-1}dt=C\eta\le C\mu^{-1}\), and \(\int_{\eta^2}^\infty e^{-\mu^2t}Ct^{-1/2}dt\le C'\mu^{-1}\). (c) For a lattice displacement \(h\) and \(t\ge\eta^2\), \(\|\tau_hDp_t-Dp_t\|_1\le C\min(t^{-1/2},|h|t^{-1})\): the first by (9.3) with \(r=1\); the second by telescoping along a coordinate path of physical length \(\le2|h|\) and (9.3) with \(r=2\). For \(t\le\eta^2\) use \(C\eta^{-1}\). If \(\eta\le|h|\le\mu^{-1}\), split \(\int_0^\infty\) at \(\eta^2,|h|^2,\mu^{-2}\): the pieces are \(\le C\eta\), \(\le2C|h|\), \(\le C|h|\log(1/(\mu|h|))\) and \(\le C|h|\int_1^\infty e^{-u}u^{-1}du\). So \(\|\tau_hDG_\mu-DG_\mu\|_1\le C|h|(1+\log(1/(\mu|h|)))\). For \(0<x\le1\), \(x^{1-\alpha}(1+\log(1/x))\le1+1/(e(1-\alpha))\); with \(x=\mu|h|\) this gives \(\le C_\alpha\mu^{\alpha-1}|h|^\alpha\). If \(|h|>\mu^{-1}\), use twice (b). (d) Choose \(N>\max(0,r-2)\). On \([\eta^2,R^2]\), (9.3) gives \(Ct^{-r/2}(\sqrt t/(cR))^N\), whose integral is \(O(R^{2-r})\). On \([R^2,\infty)\), \(e^{-t/R^2}Ct^{-r/2}\) integrates to \(O(R^{2-r})\). On \([0,\eta^2]\): \(C\eta^{2-r}(\eta/(cR))^N\le CR^{2-r}\). ∎

**Theorem 9.3 (interior first-difference Hölder bound; SA (BGH20), SA 12644–12722).** Let \(R\ge64\eta\), \(u\) defined on \(Q_{2R}\) (centred at a lattice point) with \(\Delta_\eta u=f\) at every point the equation needs there. Put \(M=\|u\|_{\infty,Q_{2R}}\), \(F=\|f\|_{\infty,Q_{2R}}\). On \(Q_{R/2}\), with differences and comparisons in its one-mesh enlargement,
\[
 \|Du\|_\infty\le C(R^{-1}M+RF),\qquad[Du]_\alpha\le C_\alpha(R^{-1-\alpha}M+R^{1-\alpha}F).\tag{9.4}
\]

*Proof.* Let \(\chi=\chi_0(\cdot/R)\) with \(\chi_0\) smooth, \(=1\) on \(Q_1\), supported in \(Q_{3/2}\); \(|D\chi|\le C/R\), \(|\Delta_\eta\chi|\le C/R^2\), and the difference supports of \(\chi\) lie in a collar at distance \(\ge cR\) from \(Q_{R/2}\) and its one-mesh enlargement (\(R\ge64\eta\) keeps this after every difference used). Extend \(u\) arbitrarily; \(v=\chi u\) does not depend on the extension. With \(\mu=1/R\), \((-\Delta_\eta+\mu^2)v=a-[\Delta_\eta,\chi]u\), \(a=\chi(-f+\mu^2u)\). By Lemma 9.2(a), \(v=R_\mu a-R_\mu[\Delta_\eta,\chi]u\). \(\|a\|_\infty\le F+R^{-2}M\), so Lemma 9.2(b),(c) give the \(R_\mu a\) contributions. For the commutator, move it onto the kernel: for scalar multiplication by \(\chi\), \([\Delta_\eta,\chi]^{\mathsf T}=-[\Delta_\eta,\chi]\) in the constant cell-weighted pairing. For \(K_j(y)=D^j_xG_\mu(x-y)\), the discrete product rule writes \(\Delta(\chi K)-\chi\Delta K-K\Delta\chi=\sum_i[(D_i^+\chi)(D_i^+K)+(D_i^-\chi)(D_i^-K)]\); all factors with a difference of \(\chi\) live in the collar. So \(|D^j(R_\mu[\Delta_\eta,\chi]u)(x)|\le CM(R^{-2}\|1_{|\cdot|\ge cR}D^jG_\mu\|_1+R^{-1}\|1_{|\cdot|\ge cR}D^{j+1}G_\mu\|_1)\), and Lemma 9.2(d) bounds this by \(CM/R\) (\(j=1\)) and \(CM/R^2\) (\(j=2\)). Telescoping \(Dw\) for \(w=R_\mu[\Delta,\chi]u\) along coordinate paths in \(Q_{R/2}\) gives \(|Dw(x)-Dw(x')|\le CMR^{-2}|x-x'|\le C_\alpha MR^{-1-\alpha}|x-x'|^\alpha\) (as \(|x-x'|\le CR\)). On \(Q_{R/2}\), \(v=u\) with all differences used. ∎

The theorem applies componentwise to vector-valued \(u\), with a dimensional constant (SA 12724–12726).

### 9.3 Algebra on the lattice

**Lemma 9.4 (iteration lemma).** Let \(\Phi:[\rho_0,\rho_1]\to[0,\infty)\) be bounded. Suppose \(\Phi(t)\le\vartheta\Phi(t')+K(t'-t)^{-1}+K'\) for all \(\rho_0\le t<t'\le\rho_1\), with \(0\le\vartheta\le1/2\). Then \(\Phi(\rho_0)\le12K(\rho_1-\rho_0)^{-1}+2K'\).

*Proof.* Let \(\tau=(1+\vartheta)/2\in[1/2,3/4]\), \(t_0=\rho_0\), \(t_{i+1}=t_i+(1-\tau)\tau^i(\rho_1-\rho_0)\); then \(t_i<\rho_1\). Iterating \(m\) times,
\(\Phi(\rho_0)\le\vartheta^m\Phi(t_m)+\sum_{i<m}\vartheta^i[K(1-\tau)^{-1}\tau^{-i}(\rho_1-\rho_0)^{-1}+K']\). Since \(\Phi\) is bounded, \(\vartheta^m\Phi(t_m)\to0\). Also \(\sum_i(\vartheta/\tau)^i\le(1-\vartheta/\tau)^{-1}=(1+\vartheta)/(1-\vartheta)\le3\), \((1-\tau)^{-1}=2/(1-\vartheta)\le4\), \(\sum\vartheta^i\le2\). ∎

**Lemma 9.5 (flat Hodge identity).** For a 1-form \(A\) on the flat lattice, with \((dA)_{\nu\mu}=\nabla_\nu A_\mu-\nabla_\mu A_\nu\), \((\delta F)_\mu=\sum_\nu\nabla^-_\nu F_{\nu\mu}\), \(\operatorname{div}A=\sum_\nu\nabla^-_\nu A_\nu\):
\[
 \Delta_\eta A_\mu=(\delta dA)_\mu+\nabla_\mu\operatorname{div}A\tag{9.5}
\]
at every site where the stencils are defined. *Proof.* \((\delta dA)_\mu=\sum_\nu\nabla^-_\nu\nabla_\nu A_\mu-\sum_\nu\nabla^-_\nu\nabla_\mu A_\nu\), and flat differences commute: \(\nabla^-_\nu\nabla_\mu=\nabla_\mu\nabla^-_\nu\). ∎

**Lemma 9.6 (massive Coulomb gauge).** Let \(A_1\) be as in (F3). Put \(\mu=\xi^{-1}\) and \(Q'=Q_{s+6\xi}(x_0)\). There are absolute \(a_{\rm FH},C_\lambda,C_2,C_\nabla\) such that, if \(a\le a_{\rm FH}\), there is a Hermitian traceless \(\lambda\) on \(\eta\mathbb Z^4\) with
\[
 |\lambda|\le C_\lambda a,\qquad\xi|\nabla\lambda|\le C_\lambda a,\tag{9.6}
\]
and the gauge transform \(A_2\) of \(A_1\) by \(g_2=e^{i\lambda}\) satisfies, on \(Q'\),
\[
 \operatorname{div}A_2=-\xi^{-2}\Psi_1(\lambda)\lambda,\qquad|A_2|\le C_2a\xi^{-1},\qquad|\nabla\operatorname{div}A_2|\le C_\nabla a\xi^{-3}.\tag{9.7}
\]
Here \(\Psi_1\) is the holomorphic linear-map-valued function defined in the proof, with \(\Psi_1(0)=I\).

*Proof.* *The gauge action.* With \(U^g(b)=g(b_-)U(b)g(b_+)^{-1}\) (`p82.md` L292), \(e^{i\eta A_2(b)}=e^{i\lambda(x)}e^{i\eta A_1(b)}e^{-i\lambda(x+\eta e_\nu)}\) for \(b=(x,x+\eta e_\nu)\). Let \(\Phi(u,u',w)=\frac1i\operatorname{Log}(e^{iu}e^{iw}e^{-iu'})\), holomorphic on the polydisc \(|u|,|u'|,|w|\le r_\Phi\) (principal log of a matrix within \(1/2\) of \(I\)), real (Hermitian-valued) on Hermitian arguments. \(\Phi(u,u,0)=0\). Put \(\Psi_1(u)=-\partial_{u'}\Phi(u,u,0)\), \(\Psi_2(u)=\partial_w\Phi(u,u,0)=\operatorname{Ad}(e^{iu})\). Differentiating \(\Phi(u,u,0)\equiv0\) gives \(\partial_u\Phi(u,u,0)=\Psi_1(u)\). \(\Psi_1(0)=\Psi_2(0)=I\). Define \(\mathcal R(u;v,w)=\Phi(u,u+v,w)+\Psi_1(u)v-\Psi_2(u)w\). It is holomorphic for \(|u|\le r_\Phi/3\), \(|v|,|w|\le r_\Phi/3\), and vanishes to second order in \((v,w)\). Schwarz's lemma on the disc \(z\mapsto\mathcal R(u;zv,zw)\), and Cauchy estimates in \(u\) and in \((v,w)\), give absolute \(C_{\mathcal R}\) with
\[
 |\mathcal R|\le C_{\mathcal R}(|v|+|w|)^2,\quad|\partial_u\mathcal R|\le C_{\mathcal R}(|v|+|w|)^2,\quad|\partial_{(v,w)}\mathcal R|\le C_{\mathcal R}(|v|+|w|)\tag{9.8}
\]
for \(|u|\le r_\Phi/6\), \(|v|+|w|\le r_\Phi/6\). Also \(|\Psi_i(u)-I|\le C|u|\) and \(|\Psi_1(u)^{-1}|\le2\), \(|\Psi_2(u)|\le2\) for \(|u|\le n_0\) (absolute \(n_0\)).

*The divergence.* Write \(A_{2,\nu}(x)=\eta^{-1}\Phi(\lambda(x),\lambda(x+e_\nu),\eta A_{1,\nu}(x))\) (\(x+e_\nu\) means \(x+\eta e_\nu\)). Expand the term at \(x\) about \(u=\lambda(x)\) and the term at \(x-e_\nu\) about \(u=\lambda(x-e_\nu)\):
\[
\begin{split}
 \eta\,\nabla^-_\nu A_{2,\nu}(x)={}&-\Psi_1(\lambda(x))\nabla_\nu\lambda(x)+\Psi_1(\lambda(x-e_\nu))\nabla_\nu\lambda(x-e_\nu)\\
 &+\Psi_2(\lambda(x))A_{1,\nu}(x)-\Psi_2(\lambda(x-e_\nu))A_{1,\nu}(x-e_\nu)+\eta^{-1}(\mathcal R_+-\mathcal R_-).
\end{split}
\]
Rewrite the first line as \(-\Psi_1(\lambda(x))\,\eta\nabla^-_\nu\nabla_\nu\lambda(x)-[\Psi_1(\lambda(x))-\Psi_1(\lambda(x-e_\nu))]\nabla_\nu\lambda(x-e_\nu)\), and similarly the second. Summing over \(\nu\),
\[
 \operatorname{div}A_2=-\Psi_1(\lambda)\Delta_\eta\lambda+\Psi_2(\lambda)\operatorname{div}A_1+S(\lambda),\tag{9.9}
\]
\[
 |S(\lambda)(x)|\le C_S\max_{\rm st}(|\nabla\lambda|+|A_1|)^2,\tag{9.10}
\]
with the maximum over the stencil \(\{x,x\pm\eta e_\nu\}\). Indeed \(|\eta^{-1}(\Psi_i(\lambda(x))-\Psi_i(\lambda(x-e_\nu)))|\le C|\nabla^-_\nu\lambda(x)|\), and by (9.8) \(|\mathcal R_\pm|\le C_{\mathcal R}\eta^2(|\nabla\lambda|+|A_1|)^2\), which after the prefactor \(\eta^{-2}\) is bounded as stated. Every factor of \(\eta^{-1}\) has been absorbed into a difference or a second-order remainder. By (9.8), \(S\) is also Lipschitz:
\[
 |S(\lambda)-S(\lambda')|(x)\le C_S\max_{\rm st}\big[(|\nabla\lambda|+|\nabla\lambda'|+|A_1|)^2|\lambda-\lambda'|+(|\nabla\lambda|+|\nabla\lambda'|+|A_1|)|\nabla(\lambda-\lambda')|\big].\tag{9.11}
\]

*The equation.* We want \(\operatorname{div}A_2=-\mu^2\Psi_1(\lambda)\lambda\) on \(Q'\). By (9.9) this is equivalent to \((-\Delta_\eta+\mu^2)\lambda=\mathcal G(\lambda)\) on \(Q'\), where
\[
 \mathcal G(\lambda)=-\Psi_1(\lambda)^{-1}\big[\Psi_2(\lambda)\operatorname{div}A_1+S(\lambda)\big].
\]
Solve the fixed-point problem \(\lambda=R_\mu(\mathbb 1_{Q'}\mathcal G(\lambda))\) on \(\ell^\infty(\eta\mathbb Z^4)\) (Hermitian traceless values), with \(\mathcal N(\lambda)=\max(\sup|\lambda|,\xi\sup|\nabla\lambda|)\). By Lemma 9.2(a),(b) (\(\mu\eta=\eta/\xi\le1\)), \(\mathcal N(R_\mu f)\le C_0'\xi^2\|f\|_\infty\), \(C_0'=\max(1,C_{\rm G})\). For \(\mathcal N(\lambda)\le N\le n_0\), \(|\operatorname{div}A_1|\le4a\xi^{-2}\) and (9.10) give \(\|\mathbb 1_{Q'}\mathcal G(\lambda)\|_\infty\le\xi^{-2}[16a+2C_S(N+a)^2]\). With \(N_*=32C_0'a\): if \(2C_S(33C_0')^2a\le16\) and \(N_*\le n_0\), the ball \(\{\mathcal N\le N_*\}\) is mapped into itself. By (9.11) and the Lipschitz bounds of \(\Psi_i^{\pm1}\), \(\|\mathbb 1_{Q'}(\mathcal G(\lambda)-\mathcal G(\lambda'))\|_\infty\le C_L'\xi^{-2}(a+N_*)\mathcal N(\lambda-\lambda')\), so the map has Lipschitz constant \(\le C_0'C_L'\cdot33C_0'a\le1/2\) for \(a\le a_{\rm FH}\). The ball is closed in the complete space \(\ell^\infty\); Banach's fixed-point theorem gives \(\lambda\) with \(\mathcal N(\lambda)\le N_*\), i.e. (9.6) with \(C_\lambda=32C_0'\). The map preserves the real (Hermitian) subspace, so \(\lambda\) is Hermitian and \(g_2\) is real. On \(Q'\), \((-\Delta+\mu^2)\lambda=\mathcal G(\lambda)\), which is the stated divergence identity. *Bounds.* \(|A_2|\le|\Psi_1||\nabla\lambda|+|\Psi_2||A_1|+\eta^{-1}|\mathcal R|\le(2C_\lambda+2+C_{\mathcal R}(C_\lambda+1)^2)a\xi^{-1}\) (using \(\eta\le\xi\), \(a\le1\)). \(|\nabla_\mu(\Psi_1(\lambda)\lambda)|\le(2+Cn_0)|\nabla\lambda|\), so \(|\nabla\operatorname{div}A_2|\le C\xi^{-2}C_\lambda a\xi^{-1}\). ∎

**Lemma 9.7 (current and curvature).** Let \(U=e^{i\eta A}\) on a region, \(\eta|A|\le1/16\), and let \(F_A(x;\nu,\mu)=(i\eta^2)^{-1}\operatorname{Log}P(x;\nu,\mu)\), where \(P(x;\nu,\mu)\) is the holonomy from \(x\) along \(\nu\) then \(\mu\). Then \(F_A(x;\mu,\nu)=-F_A(x;\nu,\mu)\) and, at bonds whose plaquettes lie in the region,
\[
 |(\delta F_A)_\nu(x)+J(U)(x,x+\eta e_\nu)|\le C_J\max_{\rm st}\big(|A||F_A|+\eta^3|F_A|^3\big).\tag{9.12}
\]
*Proof.* Antisymmetry: \(P(x;\mu,\nu)=P(x;\nu,\mu)^{-1}\) and \(\operatorname{Log}(P^{-1})=-\operatorname{Log}P\). In (9.1), the bond \(b=(x,x+e_\nu)\) lies in the plaquettes \(P_{+\mu}=P(x;\nu,\mu)\) and \(P_{-\mu}\), the plaquette with corners \(x,x+e_\nu,x+e_\nu-e_\mu,x-e_\mu\) traversed from \(x\) along \(\nu\). Direct multiplication gives \(P_{-\mu}=h^{-1}P(x-e_\mu;\nu,\mu)^{-1}h\) with \(h=e^{i\eta A_\mu(x-e_\mu)}\). For Hermitian traceless \(2\times2\) \(X\), \(\pi(e^{iX})=\sin(|X|)X/|X|\), so \(|\pi(e^{iX})-X|\le|X|^3/6\); also \(\pi(P^{-1})=-\pi(P)\) and \(|\operatorname{Ad}(h^{-1})-I|\le4\eta|A|\). Hence
\(J(b)=\eta^{-3}\sum_{\mu\ne\nu}\big[\eta^2F_A(x;\nu,\mu)-\eta^2F_A(x-e_\mu;\nu,\mu)\big]+E\), \(|E|\le C(|A||F_A|+\eta^3|F_A|^3)\). The bracket is \(\eta^3\nabla^-_\mu F_A(\cdot;\nu,\mu)(x)\). By antisymmetry \(\sum_\mu\nabla^-_\mu F_A(\cdot;\nu,\mu)=-(\delta F_A)_\nu\). ∎

**Lemma 9.8 (curl and curvature).** With the hypotheses of Lemma 9.7, \(|dA-F_A|\le C_d|A|^2\) and \(|\delta(dA-F_A)|\le C_d\max_{\rm st}|A||\nabla A|\).

*Proof.* \(\operatorname{Log}(e^{X_1}e^{X_2}e^{X_3}e^{X_4})=\sum X_r+\beta(X)\) with \(\beta\) holomorphic for \(\sum|X_r|\le1/4\) and vanishing to second order. With \(X_r=\pm i\eta A(b_r)\) along the plaquette, \(\sum X_r=i\eta^2(dA)_{\nu\mu}(x)\). So \(dA-F_A=-(i\eta^2)^{-1}\beta(X)\), \(|\beta|\le C(4\eta|A|)^2\). For the divergence, compare \(\beta\) at the plaquettes based at \(x\) and \(x-e_\nu\): \(|\beta(z)-\beta(z')|\le C(|z|+|z'|)|z-z'|\), \(|z|\le4\eta|A|\), \(|z-z'|\le4\eta^2|\nabla A|\). Dividing by \(\eta^3\) gives the claim. ∎

### 9.4 Proof of Theorem 9.9

*Step 1 (gauge).* Lemma 9.6 gives \(A_2\) on \(Q'=Q_{s+6\xi}\) with (9.6)–(9.7). Since \(\eta|A_2|\le C_2a\le1/16\) for small \(a\), Lemmas 9.7–9.8 apply.

*Step 2 (Laplacian identity).* By (9.5), (9.7), Lemma 9.8 and Lemma 9.7, at every bond of \(Q'\) whose stencils lie in \(Q'\),
\[
 |\Delta_\eta A_2|\le|\delta F_{A_2}|+|\delta(dA_2-F_{A_2})|+|\nabla\operatorname{div}A_2|\le|J|+C_J(|A_2||F_{A_2}|+\eta^3|F_{A_2}|^3)+C_d|A_2||\nabla A_2|+C_\nabla a\xi^{-3}.
\]
Gauge invariance gives \(|J(U^{g})|=|J(U)|\le\varepsilon\xi^{-3}\) and \(|F_{A_2}|\le2\varepsilon\xi^{-2}\) (from (F1) and \(|\operatorname{Log}P|\le2|P-I|\) for \(|P-I|\le1/2\)). With \(\varepsilon\le a\le1\), \(\eta\le\xi\):
\[
 |\Delta_\eta A_2|\le C_\Delta\big(a\xi^{-3}+a\xi^{-1}\max_{\rm st}|\nabla A_2|\big).\tag{9.13}
\]

*Step 3 (gradient by iteration).* Fix \(x_0'\in Q_{s+2\xi}\). For \(t\in[\xi,2\xi]\) let \(\Phi(t)\) be the maximum of \(|\nabla A_2|\) over bonds whose stencils lie in \(Q_t(x_0')\subset Q_{s+4\xi}\subset Q'\). \(\Phi\) is finite (finitely many bonds; \(|\nabla A_2|\le2\eta^{-1}\sup|A_2|\)). Let \(\xi\le t<t'\le2\xi\), \(x\in Q_t(x_0')\), and \(R=\min\{(t'-t)/4,\ \xi\}\).
- If \(R\ge64\eta\): \(Q_{2R}(x)\) and its stencils lie in \(Q_{t'}(x_0')\). Theorem 9.3 with \(M\le C_2a\xi^{-1}\) and \(F\le C_\Delta(a\xi^{-3}+a\xi^{-1}\Phi(t'))\) (by (9.13)) gives \(|\nabla A_2(x)|\le C(R^{-1}C_2a\xi^{-1}+RC_\Delta a\xi^{-3}+RC_\Delta a\xi^{-1}\Phi(t'))\).
- If \(R<64\eta\): \(|\nabla A_2(x)|\le2\eta^{-1}\sup|A_2|\le128R^{-1}C_2a\xi^{-1}\).

With \(R\le\xi\) and \(R^{-1}\le4(t'-t)^{-1}+\xi^{-1}\):
\[
 \Phi(t)\le CC_\Delta a\,\Phi(t')+K(t'-t)^{-1}+K',\quad K=4\max(C,128)C_2a\xi^{-1},\quad K'=C(C_2+C_\Delta)a\xi^{-2}.
\]
Require \(CC_\Delta a\le1/2\) (part of \(a\le a_{\rm FH}\)). Lemma 9.4 on \([\xi,2\xi]\) gives \(\Phi(\xi)\le12K\xi^{-1}+2K'=:C_3a\xi^{-2}\). Hence \(|\nabla A_2|\le C_3a\xi^{-2}\) on \(Q_{s+2\xi}\) (with stencils).

*Step 4 (Laplacian bound).* By (9.13), \(|\Delta_\eta A_2|\le C_\Delta(1+C_3)a\xi^{-3}\) on \(Q_{s+\xi}\) with stencils.

*Step 5 (Hölder).* For \(x\in Q_s\) take \(R=\xi/2\); then \(Q_{2R}(x)\subset Q_{s+\xi}\). If \(\xi\ge128\eta\), Theorem 9.3 gives on \(Q_{\xi/4}(x)\): \([\nabla A_2]_\alpha\le C_\alpha((\xi/2)^{-1-\alpha}C_2a\xi^{-1}+(\xi/2)^{1-\alpha}C_\Delta(1+C_3)a\xi^{-3})=C'_\alpha a\xi^{-2-\alpha}\). For \(x,x'\in Q_s\) with \(|x-x'|_\infty\le\xi/4\), both lie in \(Q_{\xi/4}(x)\). If \(|x-x'|_\infty>\xi/4\), then \(|\nabla A_2(x)-\nabla A_2(x')|\le2C_3a\xi^{-2}\le2C_3\,4^\alpha a\xi^{-2-\alpha}|x-x'|^\alpha\). If \(\xi<128\eta\), then for all \(x\ne x'\), \(|x-x'|\ge\eta>\xi/128\) and \(|\nabla A_2(x)-\nabla A_2(x')|\le2C_3a\xi^{-2}\le2C_3\,128^\alpha a\xi^{-2-\alpha}|x-x'|^\alpha\).

*Conclusion.* \(g=g_2g_1\) and \(A=A_2\) satisfy (9.2) on \(Q\) with \(C_{\rm F}=\max(C_2,C_3)\), \(C_{{\rm F},\alpha}=\max(C'_\alpha,2C_3\cdot128^\alpha)\). Collecting the smallness conditions on \(a\) defines
\[
 a_{\rm FH}=\min\{\text{Lemma 9.6's ceiling},\ (16C_2)^{-1},\ (2CC_\Delta)^{-1},\ 1\}.\tag{9.20}
\]
∎

### 9.5 PR1's clause (H): the real part

**Corollary 9.10.** Work in level-\(\ell\) units (\(\xi=1\)). Let \(D=Q_{s}(x_0)\) be a cube of side \(2s\le C_{\rm box}LM\), and let \(D^{++}\) be the concentric cube of side \(2s+22\), inside one layer. Suppose that on \(D^{++}\) the real background \(U\) has curvature \(<wL^2\eta^2\), matrix divergence \(|D_U^{\mathsf T}\partial U|<2L^3w\eta^2\) and current \(|J|\le wL^2\), with \((C_{\rm box}LM+18)L^3w<c_{\rm rg}\) and \(a:=4L^3B_*(C_{\rm box}LM+18)\,w\le a_{\rm FH}\). Then there is a real gauge on \(D\) with
\[
 |A_r|,\ |\nabla A_r|,\ [\nabla A_r]_{\alpha_{\rm H},D}\le C_{{\rm F},\alpha_{\rm H}}\,a.\tag{9.21}
\]
So the real clause of `bx-fix.md` (H) holds with \(C_{\rm pot}Ma_0\), \(C_{\rm pot}=4L^3B_*(C_{\rm box}L+18)\,C_{{\rm F},\alpha_{\rm H}}\), whenever \(w<a_0\).

*Proof.* RCG4 (pr-lay's Q, L230–L240; ST1's PROF/RCG4, `st1-r4.md` L136; conditional on F0) on the cube \(Q^+=Q_{s+8}(x_0)\), of side \(2s+16\le C_{\rm box}LM+16\), whose side-\((2s+22)\) enlargement is \(D^{++}\), gives (F3) with \(\xi=1\) and \(|A_1|,|\nabla A_1|<4L^3B_*(2s+18)w\le a\). (F1) and (F2) hold with \(\varepsilon=wL^2\le a\). Theorem 9.9 with \(Q=D\) and \(\alpha=\alpha_{\rm H}\) gives (9.21). Since \(M\ge1\), \(a\le4L^3B_*(C_{\rm box}L+18)Mw\). ∎

At a seam (two adjacent layers) use the finer scale as \(\xi\); the curvature hypotheses in the coarser layer's local units imply those in the finer one with a factor \(L^2\), and the conclusion in "ambient local units" costs \(L^{2+\alpha_{\rm H}}\), as `bx-fix.md` §10 (L314–L318) records for its Lemma 2.

**Status of §9.** Theorem 9.9 is **proved**: Lemmas 9.1–9.3 rebuild SA's proofs (SA 12412–12740); Lemmas 9.4–9.8 and the proof are new and elementary. Corollary 9.10 is **proved as an implication** from RCG4 (an import, conditional on F0) and the actual curvature/current bounds of the background (B of pr-lay, an import). The complex clause \([\nabla A'']_{\alpha_{\rm H}}<a_1\) of (H) is not treated here; `bx-fix.md` Proposition I (unrefereed) is its supplier. FP1(2) is not used. The three-dimensional text treats the analogous scalar problem in the same way (Y3 10428–10429: "We next obtain pointwise and H\"older bounds from a local \(L^2\) bound and the lattice Poisson equation"); it is not used here.

## 10. (H-ct)

### 10.1 What the outline says, and the exact statement

SA Proposition 1a.2.8 (SA 7569–7578) takes an action correction "local, analytic and *renormalised* in the same way as \(\mathbf E_k+\mathbf R_k\)", \(S=\sum_{j\le k}[\sum_z\sum_{X\ni z}(G^{(j)}(X,\cdot,z)-G^{(j)}(X,\mathbf 1,z))-e_jA]+\sum_{j\in\mathcal J}\sum_X(H^{(j)}(X,\cdot)-H^{(j)}(X,\mathbf 1))\), with \(N(S)=\sum_{j\le k}\omega_{k+1-j}\|G^{(j)}\|_{j,\kappa}+\sum_{j\in\mathcal J}\mathsf q_j^2\|H^{(j)}\|_{j,\kappa}\) and \(\omega_n\le Cn^CL^{-\alpha_{\rm H}n}\); "The covariance of the pointed totals is what makes the bracket left after the subtraction of \(e_jA\) irrelevant (1e)." "Along the run, \(G^{(j)}=E^{(j)}\) and \(e_j=b_j\), while the \(H^{(j)}\) are the aged \(R^{(j)}\)" (SA 7593). SA 7864 gives the mechanism: "The bracket of level \(j\) in \(\{S\}\) is \(O(\mathsf q_j^3\eta_{k-j}^{4+\alpha_{\rm H}})\), because every Cauchy estimate taken at a later background loses a power of \(\mathsf q_j\), up to the third … and a cube of level \(k\) contains \(\eta_{k-j}^{-4}\) cubes of \(\pi_j\). What is left at the age \(n=k+1-j\) is \(\mathsf q_j^3\eta_{k-j}^{\alpha_{\rm H}}\le C(n+1)^{3/2}L^{-\alpha_{\rm H}(n-1)}\), and these are the weights \(\omega_n\)." The library's version is `b4-step.md` (19) (L580; L582: "This is SA WF15"), whose first stop (L597–L607) is the pointed cancellation
\[
 D^2\!\big(F_{j,z}-b_j(G)(A_{j,z}\circ\mathcal P_j)\big)(0)[\ell_F,\ell_F]=0,\tag{20}
\]
and L609: "The checked box/core room does not establish (20)."

**Notation.** Step \(k\); its fluctuation \(B\) on the active level-\(k\) rows; \(\mathfrak B_k(r)=\{B:|g_kB(c)|<r\ \forall c\}\). For \(j\le k\), age \(n=k+1-j\), \(\sigma_j=L^{-(k-j)}\). The level-\(j\) pointed members \(E^{(j)}(X,\mathbf p,z)\), \(z\in X\) a level-\(j\) site, with IN1's norm (4); tents \(h_z(x)=\prod_\mu(1-|x_\mu-z_\mu|)_+\) (IN1 L64), \(\sum_zh_z=1\); tent action \(A_{j,z}(U)=\sum_ph_z(p)a_p(U)\). For a pair \(\mathbf p\) put
\[
 \Psi_{j,z}(\mathbf p)=\sum_{X\ni z}\big[E^{(j)}(X,\mathbf p,z)-E^{(j)}(X,\mathbf 1,z)\big]-b_jA_{j,z}(\mathbf p).\tag{10.1}
\]
The subtracted bracket of level \(j\) is \(\mathrm{Br}_j=\sum_z\Psi_{j,z}+b_j\big(\sum_{z}A_{j,z}-A(\varphi_j,\cdot)\big)\), the sum over the index set of the label (SA 6338–6342). The last term is supported where \(\varphi_j\ne\sum_{z\in\text{index}}h_z\), i.e. in a layer of width \(O(1)\) level-\(j\) cells at the boundaries of the action regions.

**(H-ct)\(^*\) (the statement proved below).** Fix \(r^{\rm ct}_k=c_{\rm ct}\alpha_{0,k}\). There are functions \(F_Y\) on \(\mathfrak B_k(2r^{\rm ct}_k)\), indexed by connected unions \(Y\) of level-\(k\) \(M\)-cubes, such that up to a \(B\)-independent constant
\[
 \sum_{j\le k}\mathrm{Br}_j(\mathbf p(B))+\sum_{j\ \rm aged}\big(R^{(j)}-R^{(j)}(\mathbf 1)\big)=\sum_YF_Y(B),
\]
each \(F_Y\) is holomorphic on \(\mathfrak B_k(2r^{\rm ct}_k)\), depends only on \(B|_Y\), and
\[
 |F_Y|\le\varepsilon_{\rm ct}e^{-\kappa|Y|},\qquad
 \varepsilon_{\rm ct}=C_{\rm ct}\,e^{\bar\kappa}M^4\Big(E_0\sum_{n\ge1}\omega_n+E_0e^{-\theta_4LM}\big(1+(\log\theta_k)^r\big)^2+\sum_{j\ \rm aged}w_{k,j}\|R^{(j)}\|\Big),\quad\omega_n=(n+1)^{3/2}L^{-\alpha_{\rm H}(n-1)}.\tag{10.2}
\]

Two differences from a2-full's wording, both forced. (a) The domain has radius \(2r^{\rm ct}_k\), twice the radius at which Theorem V is applied; this gives the gate's uniform version at every centre in \(\mathfrak B_k(r^{\rm ct}_k)\) (gate L132–L134). (b) The radius is \(\alpha_0\)-sized, not a2-full's \(r_k\sim\alpha_{1,k}\) (a2-full L190). At fluctuations of size \(\alpha_{1,k}\gg\alpha_{0,k}\) the step's pairs leave the old members' domains: the current clause of the core is \(|\mathbf J|<\alpha_0\) (SA 9646, the simple conditions), and the physical current moves linearly in \(B\) ((15), current member). With (b), Theorem V gives \(\|P_{\rm ct}\|\le C_V\varepsilon_{\rm ct}(g_k/r^{\rm ct}_k)^2=C_V\varepsilon_{\rm ct}(c_{\rm ct}C_0)^{-2}(\log\theta_k)^{-2q}\), still small (IN1 (2): \(\alpha_{0,j}=C_0g_j(\log\theta_j)^q\)).

The factor \(e^{\bar\kappa}M^4\) in \(\varepsilon_{\rm ct}\) comes from the decoupling (Lemma 10.7) and from the \(M^4\) level-\(k\) unit cubes in an \(M\)-cube. Theorem V's constant is already \(C_V(L,M)\); its consumer is the coupling ceiling at IN1 row 9. So this dependence creates no cycle.

### 10.2 Does the T0 path need it?

a2-full L190 says Theorem V "is needed only for a consumer that absorbs their quadratic part into the Gaussian". SA's step (SA 7617) interpolates only the boundary/profile/strip terms (\(t_1\)) and the young remainders \(\mathbf R''_k\) (\(t_2\)): "\(\log\mathsf I=\int_0^1dt_1\langle\{\mathbf B_k-A(x_k(\cdot)-x_k,\cdot)\}+\mathsf W^{(k)}\rangle_{t_1,1}+\int_0^1dt_2\langle\{\mathbf R''_k\}\rangle_{0,t_2}+\log\mathsf I|_{t_1=t_2=0}\)", and SA 7873: "The third term contains only regular terms." On that reading the old brackets stay in the integrand of the cluster expansion, and (H-ct) is not an A2 input; its content is then the old-origin bound (19) of the NL1 step (node CI/SF). I record this as a route observation, not a proof of non-use. The rest of §10 proves (H-ct)\(^*\) either way.

### 10.3 Inputs

- **(I1) Members (the induction hypothesis).** For \(j\le k\), the IN1 class \(\mathfrak L_k(\theta)\) (IN1 L217–L219): \(\|E^{(j)}\|_{j,\kappa}\le E_0\); analyticity, reality, gauge invariance, lattice covariance (translations and the hypercubic group of \(\mathbb T^{(j)}\), via companions on \(\mathbb Z^4\)); each pointed member subtracts its own coefficient \(b_j=b[\widehat E^{(j)}]\) of IN1 (5) times the tent action (IN1 L64); aged remainders with IN1 (12)–(13).
- **(I2) OL1's readout hypotheses.** IN1 L64: "Absolute convergence, displacement dependence, independence of \(\mu\ne\nu\), Ward identities and this normalization are hypotheses of OL1." Precisely, for the kernel \(\Pi(c,c';z)\) of IN1 (5) of each member, and of the tent action:
  (S1) \(\sum_{c,c'}|\Pi(c,c';z)|(1+|m_c-z|)^2(1+|m_{c'}-z|)^2<\infty\), uniformly in \(z\) (\(m_c\) is the midpoint of \(c\));
  (S2) \(\Pi(c+v,c'+v;z+v)=\Pi(c,c';z)\) for lattice vectors \(v\);
  (S3) covariance under the hypercubic group fixing \(z\), with the 1-form orientation signs;
  (S4) \(\sum_{c'}\Pi(c,c';z)(\nabla\chi)(c')=0\) for every polynomial \(\chi\) of degree \(\le2\);
  (S5) colour: \(\Pi^{ab}=\delta^{ab}\Pi\); and the normalization \(b[A]=1\) for the Wilson action (as the pointed family \(A_{j,z}\)). (If IN1's (5) gave \(b[A]=c_A\ne1\), the subtraction would have to use \(b[\widehat E]/c_A\); I read IN1's "this normalization" together with "Each pointed member subtracts its own coefficient times the tent Wilson action" as \(c_A=1\).)
- **(I3) (DOM-in) with room.** Stated in §11, where it is the first remaining Outstanding item.
- **(I4) Localization.** SA Theorem 6(c), as proved conditionally in `a3-derivative.md` Lemma 10.1 (on P81, P82°, and the geometric premise (G1), L527): two backgrounds whose sequences and data agree on a window \(W\) differ there by \(C\varepsilon e^{-\delta_Wd_{\mathbf B}(y,W^c)}\) in the norms of (15).
- **(I5) Decoupled response.** A family \(\mathbf p(B;s)\), \(s=(s_\Delta)\) over level-\(k\) \(M\)-cubes, holomorphic in \((B,s)\) on \(\mathfrak B_k(2r^{\rm ct}_k)\times\{|s_\Delta|<e^{\bar\kappa}\}\), equal to the step's pair at \(s\equiv1\), such that for \(s\) vanishing off a connected \(Y\ni\square\) the restriction of \(\mathbf p(B;s)\) to the reads of bases in \(\square\) depends only on \(B|_{\widehat Y}\) and on \(s|_Y\) (\(\widehat Y\): \(Y\) plus one layer), and (I3) holds for \(\mathbf p(B;s)\) uniformly in \(s\). This is SA 1c.10 and PR1(2)'s "holomorphic derivatives in decoupling parameters obey Cauchy bounds on a fixed enlarged disc" (`ym4-assembly.md` L184); a2-full's (H-walk) is the corresponding walk statement (a2-full L196).

### 10.4 The pointed cancellation (20)

**Lemma 10.3 (affine Hessian of a pointed family).** Let \(\Pi(c,c';z)\) be a symmetric kernel on oriented level-\(j\) bonds with (S1)–(S5). For a constant antisymmetric \(F\in\Lambda^2(\mathbb R^4)\otimes\mathfrak{su}(2)\) let \(\ell^{(z)}_F(c)=\tfrac12\sum_\rho F_{\rho\mu}(m_c-z)_\rho\) for \(c\) in direction \(\mu\) (an affine datum with lattice curl \(F\)). Then
\[
 q_z(F):=\sum_{c,c'}\Pi(c,c';z)\langle\ell^{(z)}_F(c),\ell^{(z)}_F(c')\rangle=b\sum_a\sum_{\rho<\mu}(F^a_{\rho\mu})^2,\qquad b=\sum_u\Pi_{\mu\nu}(u)u_\mu u_\nu,\tag{10.3}
\]
for every \(z\) and every \(\mu\ne\nu\), where \(\Pi_{\mu\nu}(u)=\sum_z\Pi(c,c';z)\), \(c\) in direction \(\mu\), \(c'\) in direction \(\nu\), \(c'_--c_-=u\) (IN1 (5)). The same identity holds with \(\ell^{(z)}_F\) replaced by \(\ell^{(z')}_F\) for any \(z'\).

*Proof.* *Colour.* By (S5) it suffices to treat one colour component. *Moments.* For \(c\) in direction \(\mu\), \(c'\) in direction \(\nu\), put \(M_{\rho\mu;\sigma\nu}=\sum\Pi(c,c';0)(m_c)_\rho(m_{c'})_\sigma\), absolutely convergent by (S1). *Antisymmetry.* For symmetric \(S\), the datum \(c\mapsto(Sm_c)_{\operatorname{dir}c}\) is \(\nabla\chi\) with \(\chi(x)=\tfrac12x\cdot Sx\): indeed \(\chi(x+e_\mu)-\chi(x)=(Sx)_\mu+\tfrac12S_{\mu\mu}=(Sm_c)_\mu\). By (S4), \(\sum_{\sigma,\nu}S_{\sigma\nu}M_{\rho\mu;\sigma\nu}=0\) for all symmetric \(S\), so \(M\) is antisymmetric in \((\sigma,\nu)\); by symmetry of \(\Pi\), also in \((\rho,\mu)\). So \(M\) is a symmetric bilinear form on \(\Lambda^2\). *Invariance.* For \(g\) in the hypercubic group, \(m_{gc}=gm_c\) and directions transform with the orientation sign, so (S3) makes \(M\) an invariant tensor. A sign flip of axis \(\alpha\) multiplies \(M(P,P')\) (\(P=\{\rho<\mu\}\), \(P'=\{\sigma<\nu\}\)) by \((-1)^{\#}\), \(\#\) the number of occurrences of \(\alpha\) in \(P\cup P'\) counted with multiplicity; if \(P\ne P'\) some \(\alpha\) lies in exactly one of them, so \(M(P,P')=-M(P,P')=0\). Permutations act transitively on 2-subsets, and a transposition inside a pair costs two signs. Hence \(M_{\rho\mu;\sigma\nu}=m_0(\delta_{\rho\sigma}\delta_{\mu\nu}-\delta_{\rho\nu}\delta_{\mu\sigma})\). *The pointed value.* At \(z=0\), \(q_0(F)=\tfrac14\sum F_{\rho\mu}F_{\sigma\nu}M_{\rho\mu;\sigma\nu}=\tfrac14m_0\sum(F_{\rho\mu}^2-F_{\rho\mu}F_{\mu\rho})=m_0\sum_{\rho<\mu}F_{\rho\mu}^2\). *The bulk value.* By (S2), \(\sum_z\Pi(c,c';z)=\sum_w\Pi(w,w+(c'-c);0)\), so \(b=\sum_{w,w'}\Pi(w,w';0)(w'_--w_-)_\mu(w'_--w_-)_\nu\), absolutely convergent. Write \(w'_--w_-=\Delta m+\tfrac12(e_\mu-e_\nu)\), \(\Delta m=m_{w'}-m_w\), and expand \([(\Delta m)_\mu+\tfrac12][(\Delta m)_\nu-\tfrac12]\). Every term except \(-(m_{w'})_\mu(m_w)_\nu\) is, for fixed \(w\), a constant or \((m_{w'})_\nu\) (a gradient of \(\tfrac12x_\nu^2\) on direction-\(\nu\) bonds) in \(w'\), or for fixed \(w'\) a constant or \((m_w)_\mu\) in \(w\); each vanishes by (S4) (and symmetry of \(\Pi\)). So \(b=-M_{\nu\mu;\mu\nu}=m_0\). *Base point.* By (S2), \(q_z=q_0\). Finally \(\ell^{(z')}_F-\ell^{(z)}_F\) is a constant datum in each direction, i.e. \(\nabla\chi\) with \(\chi\) linear; (S4) and (S1) show it does not change \(q_z\). ∎

**Corollary 10.4 ((20) holds).** Under (I1) and (I2), for every member and base point, \(D^2(\Psi_{j,z}\circ\mathfrak h_\infty)(0)[\ell_F,\ell_F]=0\) for every affine datum \(\ell_F\), and by polarization \(D^2(\Psi_{j,z}\circ\mathfrak h_\infty)(0)[\ell_F,\ell_{F'}]=0\).

*Proof.* \(D(E^{(j)}(X,\cdot,z)\circ\mathfrak h_\infty)(0)=0\) for each \(X\): it is a linear functional invariant under constant gauge transformations, and \(\mathfrak{su}(2)\) has no nonzero \(\operatorname{Ad}\)-invariant vector. So the second derivative of the composite at \(0\) is the kernel \(\Pi\) of IN1 (5). By Lemma 10.3, the members give \(b[\widehat E^{(j)}]|F|^2\) and the tent action gives \(b[A]|F|^2=|F|^2\) (S5). With \(b_j=b[\widehat E^{(j)}]\) (I1), the difference is zero. ∎

This proves `b4-step.md`'s identity (20) from the hypotheses IN1 already assigns to OL1. It does not prove those hypotheses for the actual members; they are IN1's H-OL (Outstanding there, IN1 L118). In particular the Ward identities (S4) for quadratic \(\chi\) are a statement about \(\mathfrak h_\infty\) on unbounded gradient data, made sense of by (S1).

### 10.5 The per-base bound

**Lemma 10.5 (interior bases).** Assume (I1)–(I4). Let \(z\) be a level-\(j\) base whose window \(W=W_{j,z}\) (side \(w_j=W_0M(1+n)\) level-\(j\) units, \(W_0\) fixed below) lies inside the action region where the pointed sum is complete, and let the step's datum on \(W\) (in the window gauge of (I3)) be \(D=\ell_F+r\) with
\[
 |\ell_F(c)|\le S_1|m_c-z|,\quad|r(c)|\le S_H|m_c-z|^{1+\alpha_{\rm H}}\ (c\in W),\quad\sup_W|D|\le R_j/4.\tag{10.4}
\]
Then
\[
 |\Psi_{j,z}(\mathbf p)|\le C_\Psi E_0\Big[\frac{S_1S_H}{R_j^2}+\frac{S_H^2}{R_j^2}+\frac{S_1^3}{R_j^3}\Big]+C_\Psi E_0e^{-\delta_Ww_j/2}.\tag{10.5}
\]
\(C_\Psi\) depends on \(L,\kappa,\theta_R\), the stencil constants, and polynomially on \(M\) (through \(\operatorname{diam}X\le CMm\) for \(X\) made of \(m\) cubes); not on \(j,k,n\).

*Proof.* *Localization.* By (I4) and (ROOM)'s derivative bound (§11, (11.2)), replacing the actual pair on \(X\subset W'\) (the concentric half window) by \(P^W_j(D)\) changes \(E^{(j)}(X,\cdot,z)\) by at most \(CE_0e^{-\kappa d(X)}e^{-\delta_Ww_j/2}\); polymers \(X\ni z\) not inside \(W'\) have \(d(X)\ge w_j/4\) and are bounded by \(2E_0e^{-\kappa d(X)}\), whose sum is \(\le CE_0e^{-\kappa w_j/8}\). Take \(\delta_W\le\kappa/4\) in (10.5). *Taylor.* For \(X\subset W'\) let \(f_X(D)=E^{(j)}(X,P^W_j(D),z)-E^{(j)}(X,\mathbf 1,z)\), holomorphic for \(\sup_W|D|<R_j\) by (ROOM) (11.1). Then \(f_X(0)=0\), \(Df_X(0)=0\) (colour, as in Corollary 10.4), and
\[
 f_X(D)=\tfrac12D^2f_X(0)[D,D]+T_X(D),\qquad|T_X(D)|\le\sup_{t\in[0,1]}\tfrac16|D^3f_X(tD)[D,D,D]|.
\]
*Decay of derivative kernels.* (11.2) says \(|\partial_cf_X(D')|\le CE_0e^{-\kappa d(X)}e^{-\theta_Rd(c,X)}R_j^{-1}\) for \(\sup|D'|\le R_j/2\). For three rows \(c_1,c_2,c_3\) let \(g(z_1,z_2,z_3)=f_X(D'+\sum z_ie_{c_i})\) on \(|z_i|\le R_j/8\), and \(\tilde g\) its alternating sum over the eight faces \(z_i=0\). Along a segment in one variable, \(|\tilde g|\le2\min_i(|z_i|\sup|\partial_{c_i}f_X|)\le CE_0e^{-\kappa d(X)}e^{-(\theta_R/3)\sum_id(c_i,X)}\) (minimum \(\le\) geometric mean). The subtracted terms miss a variable, so they integrate to zero against \((z_1z_2z_3)^{-2}\); Cauchy's formula on the torus \(|z_i|=R_j/8\) gives
\(|\partial_{c_1}\partial_{c_2}\partial_{c_3}f_X(D')|\le CE_0e^{-\kappa d(X)}R_j^{-3}e^{-(\theta_R/3)\sum d(c_i,X)}\), and likewise \(|\partial_{c_1}\partial_{c_2}f_X(0)|\le CE_0e^{-\kappa d(X)}R_j^{-2}e^{-(\theta_R/2)\sum d(c_i,X)}\) (repeated rows: use \(g(z)-g(0)\) and the higher Cauchy formula). This is the argument of a2-full Lemma 6.1, with (11.2) in place of (6.1). *Local sizes.* For \(X\ni z\), \(\sum_ce^{-(\theta_R/3)d(c,X)}|m_c-z|^p\le C_p(1+\operatorname{diam}X)^{4+p}\) (at most \(C(\operatorname{diam}X+t+1)^3\) rows at distance \(t\) from \(X\)). So with \(\Lambda_X(v)=\sum_ce^{-(\theta_R/3)d(c,X)}|v(c)|\): \(\Lambda_X(\ell_F)\le CS_1(1+\operatorname{diam}X)^5\), \(\Lambda_X(r)\le CS_H(1+\operatorname{diam}X)^{6}\). *Cubic term.* \(|T_X(D)|\le CE_0e^{-\kappa d(X)}R_j^{-3}\Lambda_X(D)^3\le CE_0e^{-\kappa d(X)}(1+\operatorname{diam}X)^{18}(S_1+S_H)^3R_j^{-3}\). *Quadratic term.* Summing over \(X\ni z\) and subtracting the tent action (holomorphic and bounded by \(C\) on the same polydisc, supported at distance \(\le1\) from \(z\)), the quadratic part is \(\tfrac12Q_z[D,D]\) with \(Q_z=D^2(\Psi_{j,z}\circ P^W_j)(0)\). Up to the window error \(CE_0e^{-\delta_Ww_j/2}\) (localization of \(DP^W_j(0)\) to \(\mathfrak h_\infty\), (I4) at the flat reference, SA 9744), \(Q_z\) is the kernel of IN1 (5). By Corollary 10.4, \(Q_z[\ell_F,\ell_F]=0\). So \(\tfrac12Q_z[D,D]=Q_z[\ell_F,r]+\tfrac12Q_z[r,r]\), bounded by \(CE_0R_j^{-2}\sum_{X\ni z}e^{-\kappa d(X)}\Lambda_X(\ell_F)\Lambda_X(r)+\dots\). *Sum over \(X\).* \(\sum_{X\ni z}e^{-\kappa d(X)}(1+\operatorname{diam}X)^{18}\le C\) for \(\kappa\) above the polymer-count floor (IN1 row 4; \(\kappa\ge\kappa_0^\natural\)), since there are at most \(C_0^m\) connected unions of \(m\) cubes containing a given cube and \(\operatorname{diam}X\le CMm\). Collect terms; \(S_H\le S_1\) is not assumed, hence the separate \(S_H^2\) term. ∎

**Lemma 10.6 (the datum at a base).** Assume Theorem 9.9 for the real background at level-\(k\) scale, (15) with its Hölder member (`a3-derivative.md` 7.4; P82 Theorem P's Hölder member) for the fluctuation response, and AV (`a1-balaban.md` §3.5 (3.7), with 7.1; quoted in `bx-fix.md` L75: "the j-fold actual mean on a double block in one layer is 𝓠_j(w) + 𝓒_j(w), with 𝓠_j the flat linear map, 𝓒_j holomorphic … sup|𝓒_j| ≤ C_Qr_0², 𝓒_j(0) = 0, D𝓒_j(0) = 0"). Let \(a=C(\varepsilon_k+r)\) be the level-\(k\) size of the step's pair on a level-\(k\) cube around \(z\) of side \(2w_j\sigma_j+16\), for \(B\in\mathfrak B_k(r)\). Then in a gauge on that cube with vanishing potential at \(z\), the level-\(j\) datum satisfies (10.4) with
\[
 S_1\le C_D\sigma_j^2a,\qquad S_H\le C_D\sigma_j^{2+\alpha_{\rm H}}a,\qquad\sup_W|D|\le C_D\sigma_j^2a\,w_j,\tag{10.6}
\]
provided \(C_D\sigma_j^{2-\alpha_{\rm H}}a\,w_j^{1-\alpha_{\rm H}}\le1\).

*Proof (sketch at the level of the displayed bounds; the AV import is used as stated).* Theorem 9.9 gives a real gauge with \(|A_r|,\xi_k|\nabla A_r|,\xi_k^{1+\alpha}[\nabla A_r]_\alpha\le C\varepsilon_k\xi_k^{-1}\). The complex part of the step's pair is the Landau potential \(\mathcal H(g_kB)=\int_0^1\sum_cg_kB(c)h_c(\tau g_kB)d\tau\) at the real reference; (15) and 7.4 give \(|\mathcal H|,\xi_k|\nabla\mathcal H|,\xi_k^{1+\alpha}[\nabla\mathcal H]_\alpha\le Cr\xi_k^{-1}\) after summing \(e^{-\theta_4d}\) over rows (the argument of `bx-fix.md` Lemma 5, L242–L251, with the reference \(U_{k+1}\) in place of \(\mathbf 1\)). Combine the two by BCH; first differences and Hölder seminorms of products are bounded by products of the bounds. A gauge \(e^{i\chi}\) with \(\chi\) linear removes the value at \(z\); its non-abelian corrections are \(O(|A(z)|\,|x-z|\,|A|)\), affine to leading order, with a quadratic remainder bounded as in (10.6). In level-\(j\) units the potential near \(z\) has gradient \(\le C\sigma_j^2a\) and Hölder seminorm \(\le C\sigma_j^{2+\alpha}a\). The level-\(j\) datum is the \(j\)-fold actual mean: by AV its linear part \(\mathcal Q_j\) maps an affine potential to the affine datum with the same curl (the straight segment average of a linear 1-form over a block centred on \(c\) is its integral over \(c\)), and maps the Hölder remainder to a datum bounded by \(CS_H|m_c-z|^{1+\alpha}\); its quadratic part is \(\le C(\sigma_j^2a|m_c-z|)^2\le C\sigma_j^{2+\alpha}a|m_c-z|^{1+\alpha}\) under the displayed proviso. ∎

The step "affine potential ↦ affine datum with the same curl" is exact for the flat linear map \(\mathcal Q_j\) only up to a gauge direction; `bx-fix.md` Lemma 4 (unrefereed) states "the box tower reproduces affine data exactly, up to a gauge direction". A gauge direction does not change \(\Psi_{j,z}\) at second order (Corollary 10.4's colour argument and gauge invariance). I mark Lemma 10.6 as **proved conditionally, with this one cited step**.

**Summation over bases and ages.** In Lemma 10.5 the weights \(e^{-(\theta_R/3)d(c,X)}\) localize every sum near \(X\), so no power of the window size \(w_j\) appears in the first three terms of (10.5); \(w_j\) enters only through the error term and the proviso \(\sup_W|D|\le R_j/4\). Consider first a base \(z\) in the top determining layer (\(j_{\rm d}(z)=k\)), so that the local scale is \(\xi_k\). A level-\(k\) unit cube contains \(\sigma_j^{-4}\) level-\(j\) bases. Put \(\varrho_n=a/R_j\). By (10.5) and (10.6),
\[
 \sum_{z\in\text{unit cube}}|\Psi_{j,z}|\le C E_0\big[\sigma_j^{\alpha_{\rm H}}\varrho_n^2+\sigma_j^2\varrho_n^3+\sigma_j^{-4}e^{-\delta_Ww_j/2}\big].\tag{10.7}
\]
Choose \(W_0\) with \(\delta_WW_0/2\ge4\log L+1\); then \(\sigma_j^{-4}e^{-\delta_Ww_j/2}\le L^{4(n-1)}L^{-4(n+1)}e^{-(n+1)}\le e^{-n}\). The radius comparability of admissible systems (SA 7569: "the quotient of the radii of level \(k+1\) by those of any level \(j\le k\) lies between \((1+\beta_{\rm s})^{-1}\) and \((1+\beta_{\rm s})(k+2-j)^{1/2}\)") and \(a\le C(\varepsilon_k+2r^{\rm ct}_k)\le C'\alpha_{0,k}\) give \(\varrho_n\le C(n+1)^{1/2}\). So (10.7) is \(\le CE_0[(n+1)^{3/2}L^{-\alpha_{\rm H}(n-1)}+e^{-n}]\le C'E_0\,\omega_n\), with \(\omega_n=(n+1)^{3/2}L^{-\alpha_{\rm H}(n-1)}\) as in a2-full L180 and SA 7864. The proviso of Lemma 10.6 and \(\sup_W|D|\le R_j/4\) follow from \(C_D\sigma_j^2a\,W_0M(1+n)\le R_j/4\), i.e. \(\sigma_j^2(1+n)\varrho_n\le(4C_DW_0M)^{-1}\); since \(\sigma_j^2(1+n)^{3/2}\le1\) this holds once \(c_{\rm ct}\le c/M\) (\(n=1\) is the binding case). This is a choice after \(M\) (IN1 row 6).

*Bases in deeper layers.* If \(j_{\rm d}(z)=l<k\), the local scale is \(\xi_l\); replace \(k\) by \(l\) in \(\sigma_j\) and in the age (\(n_{\rm loc}=l+1-j\)), and note that only the \(B\)-dependent part of \(\Psi_{j,z}\) enters (H-ct)\(^*\). Its derivative in \(B(c)\) carries the response decay \(e^{-\theta_4d_{\mathbf B}(z,y_c)}\) ((15) and (11.2)), and a level-\(l\) layer is at \(d_{\mathbf B}\)-distance \(\ge(\rho/2)(k-l)-C\) from the active rows (a2-full Theorem IV's layer separation, L160). So these bases add at most \(CE_0\sum_{m\ge1}e^{-\theta_4\rho m/2}\sum_n\omega_n\) per level-\(k\) unit cube.

**Non-interior bases.** These are bases whose window meets a boundary of the action region of level \(j\), where the pointed sum or the profile is incomplete, together with the boundary term \(b_j(\sum A_{j,z}-A(\varphi_j))\). They get no cancellation: per base \(|\Psi_{j,z}|\le CE_0(\sigma_j^2a/R_j)^2\), i.e. \(\le CE_0\varrho_n^2\) per level-\(k\) unit cube. Their \(B\)-dependent parts carry the decay \(e^{-\theta_4d_{\mathbf B}(z,{\rm active})}\). There are two cases.
1. *Where the action and determining sequences agree near \(z\).* Then the level-\(j\) action boundary is a determining boundary of level \(j\), in layers \(\le j\), at \(d_{\mathbf B}\)-distance \(\ge(\rho/2)(n-1)-C\) from the active rows. The contribution is \(\le CE_0\sum_n(n+1)e^{-\theta_4\rho(n-1)/2}\) per unit cube.
2. *Inside a standing drop-out component \(X\) of level \(t\le k\), with \(j\) in its window \((t_\flat,t]\).* Then \(X\cap\Omega^{\rm d}_{t+1}=\varnothing\) and \(\operatorname{dist}(X,\Omega_{t+1})\ge LM\xi_t\) (SA Prop. 2.3), so \(d_{\mathbf B}(X,{\rm active})\ge LM+(\rho/2)(k-t)-C\). The window contains at most \(\mathsf N_t\) ages, each \(n\le k-t+\mathsf N_t+1\). With (8.2) the contribution is \(\le CE_0e^{-\theta_4LM}\sum_{m\ge0}e^{-\theta_4\rho m/2}\mathsf N_t(m+\mathsf N_t+2)\le C_\flat E_0e^{-\theta_4LM}\big(1+(\log\theta_k)^r\big)^2\).

So the drop-out windows add a factor \(e^{-\theta_4LM}(1+(\log\theta_k)^r)^2\), the same phenomenon as in Theorem 8.5. It is harmless for the consumer: Theorem V multiplies \(\varepsilon_{\rm ct}\) by \((g_k/r^{\rm ct}_k)^2=(c_{\rm ct}C_0)^{-2}(\log\theta_k)^{-2q}\), and \(q>p_0+2r>2r\) (IN1 row 1). The aged remainders are polymers at level \(k\) after re-blocking (SA 7873: "an aged \(R^{(j)}\) has each of its cubes inside a single block … it is counted together with \(\mathbf E_k\)"), with the weights \(w_{k,j}\) of IN1 (13); they need no cancellation and enter (10.2) through their norms.

### 10.6 Locality in \(B\)

**Lemma 10.7 (polymer form in \(B\)).** Assume (I5), and let \(\Psi_z(B;s)\) denote any of the per-base functions above evaluated at \(\mathbf p(B;s)\), with \(\sup|\Psi_z(\cdot;s)|\le\epsilon_z\) on \(\mathfrak B_k(2r^{\rm ct}_k)\times\{|s|<e^{\bar\kappa}\}\). Let \(\square_z\) be the level-\(k\) \(M\)-cube containing \(z\). For connected \(Y\ni\square_z\) put
\[
 F_{Y,z}(B)=\int_{[0,1]^{Y\setminus\square_z}}\partial^{Y\setminus\square_z}_s\Psi_z(B;s_Y,0_{Y^c})\,ds_{Y\setminus\square_z}\Big|_{s_{\square_z}=1}+\big(\text{the analogous term with }\partial_{s_{\square_z}}\big).
\]
Then \(\Psi_z(B;1)=\sum_{Y\ni\square_z\ \rm connected}F_{Y,z}(B)\), each \(F_{Y,z}\) depends only on \(B|_{\widehat Y}\), and \(|F_{Y,z}|\le2\epsilon_z(e^{\bar\kappa}-1)^{-(|Y|-1)}\). Hence \(F_Y:=\sum_{z:\square_z\subset Y}F_{Y,z}\) satisfies \(|F_Y|\le2|Y|\max_{\square\subset Y}\big(\sum_{z\in\square}\epsilon_z\big)e^{-(\bar\kappa-1)(|Y|-1)}\le\varepsilon_{\rm ct}e^{-\kappa|Y|}\) if \(\bar\kappa\ge\kappa+3\).

*Proof.* For a function \(f\) of finitely many variables \(s_\Delta\), iterating \(f(1)=f(0)+\int_0^1\partial f\) in each variable gives \(f(1)=\sum_{Y'}\int_{[0,1]^{Y'}}\partial^{Y'}f(s_{Y'},0_{Y'^c})ds_{Y'}\) over all subsets \(Y'\). By (I5), at \(s\) vanishing off \(Y'\cup\square_z\), \(\Psi_z\) does not depend on \(s_\Delta\) for \(\Delta\) outside the connected component of \(Y'\cup\square_z\) containing \(\square_z\); so \(\partial^{Y'}\) vanishes unless \(Y=Y'\cup\square_z\) is connected. Group the subsets with the same \(Y\) (two: with or without \(\square_z\)). Locality is (I5). For \(s\in[0,1]^{Y'}\), the polydisc of radius \(e^{\bar\kappa}-1\) about \(s\) lies in \(|s|<e^{\bar\kappa}\); Cauchy's estimate in each variable gives the bound. Finally \(e^{\bar\kappa}-1\ge e^{\bar\kappa-1}\), \(\sum_{z\in\square}\epsilon_z\le M^4\times\)(the unit-cube sums of §10.5), and \(|Y|e^{-|Y|}\le1\). ∎

### 10.7 Assembly

**Theorem 10.8 ((H-ct)\(^*\) as an implication).** Assume (I1)–(I5). Fix \(L,\alpha_{\rm H}\), the constants of IN1 rows 1–3 and Part I, then \(\kappa\) (row 4), \(\bar\kappa\ge\kappa+3\) (row 5), \(M\), and \(c_{\rm ct}\) small (row 6). Then (H-ct)\(^*\) holds with (10.2), where \(C_{\rm ct}\) depends only on \(L,\alpha_{\rm H},\kappa\), polynomially on \(M\), and on the fixed stencil and polymer-count constants. It is a consumer constant: Theorem V's ceiling on \(g_k\) (IN1 row 9) follows it.

*Proof.* For \(B\in\mathfrak B_k(2r^{\rm ct}_k)\) and \(|s|<e^{\bar\kappa}\), (I5) gives (I3) for \(\mathbf p(B;s)\), hence Lemma 10.6's datum structure and Lemma 10.5's bound at interior bases, and the crude bound at non-interior bases; summing over bases in a level-\(k\) \(M\)-cube and over ages gives \(\sum_{z\in\square}\epsilon_z\le CM^4(E_0\sum_n\omega_n+\sum w_{k,j}\|R^{(j)}\|)\). Lemma 10.7 gives the polymer form. \(B\)-independent terms are the constant. ∎

**Status of §10.** Lemma 10.3 and Corollary 10.4: **proved** from (I1)–(I2); this settles `b4-step.md`'s first stop (20) at the level of IN1's OL1 hypotheses. Lemma 10.5, the summation and Lemma 10.7: **proved as implications** from (I1)–(I5). Lemma 10.6: **proved conditionally**, with the cited affine-reproduction step. Theorem 10.8: **proved as an implication**. Not proved here: (I2) for the actual members (IN1 H-OL), (I3) (§11), (I4)'s premise (G1), (I5).

## 11. The first remaining Outstanding statement: (DOM-in)

In the proof order of Theorem 10.8 the first input used is (I3), at the first line of Lemma 10.5.

**(DOM-in) with room.** There are \(c_R>0\) and \(\theta_R>0\), fixed at IN1 row 3, such that the following hold with \(R_j=c_R\alpha_{0,j}\).
1. *(Inner Landau form at the evaluation points.)* For every \(j\le k\), every base \(z\) and every \(B\in\mathfrak B_k(2r^{\rm ct}_k)\) (and every \(s\) of (I5)), the pair at which the step evaluates \(E^{(j)}(X,\cdot,z)\), \(X\subset W'_{j,z}\), is, in a gauge on the window \(W_{j,z}\), the inner Landau triple \(P^W_j(D)=(\mathbf 1,\mathcal H^W_j(D),J(e^{i\eta_j\mathcal H^W_j(D)}))\) of a level-\(j\) datum \(D\) on the window's tower, up to the localization error of (I4). This is the conclusion of SA 9767–9772: "the inner substitution in Landau form takes values in the cores of every level \(1\le j\le k\), with the running radii". Its hypothesis (SA 9767) is: "\((U,A')\) satisfies, on some region containing \(\square_0\) and at radii larger than \(\alpha_{i,k}\) by a fixed factor, both the simple conditions of level \(k+1\) and, at that same level, the tower clause of \(\square_0\)".
2. *(Room.)* For \(X\subset W'\), \(f_X(D)=E^{(j)}(X,P^W_j(D),z)\) is holomorphic and
\[
 |f_X(D)|\le E_0e^{-\kappa d_j(X)}\quad\text{on }\{\sup_W|D|<R_j\},\tag{11.1}
\]
and for \(\sup_W|D|\le R_j/2\),
\[
 |\partial_cf_X(D)|\le C_RE_0e^{-\kappa d_j(X)}e^{-\theta_Rd(c,X)}R_j^{-1};\tag{11.2}
\]
the same for the tent action with \(E_0\) replaced by an absolute constant.

Item 2 would follow from \(P^W_j(\{\sup|D|<R_j\})\subset\mathcal D_j(X)\) with a field-norm margin, together with the response decay of Theorem 4.1 at the flat reference (where P82 reduces to the flat package). Item 1 is the place where the evaluation points must be shown to be admitted. Both concern the hereditary core \(\mathcal D_j(X)\) of IN1 (L41: "Its data include local gauges and potential/current bounds on every required subdomain, existence of the required averaging towers, and their uniform bounds. These requirements are part of the domain; small plaquette curvature alone is not its definition.").

**Attack 1: from the frozen texts.** ST1 Theorem 14 hypothesis 2 keeps "complex input membership" as a hypothesis (`assembly-status.md` L127, quoting `st1-r4.md`). pr-lay Theorem 8 needs its D (L242–L252), and "**Outstanding — D for the actual domains**" (L254). IN1 L190: "It does not construct the gauges, potential bounds or towers in R4–R6." hm L37: "R4, and the additional R5–R6 conditions defining SA's hereditary core, do not imply Rep." descent L285: "Nor does this note put every ST1 chain domain inside this R4 domain." *Failure:* every frozen text that meets this statement takes it as a hypothesis. pr-lay's Lemma 2 (an admitted complex line) concerns the regular class \(\mathcal R_h\) (pr-lay L58), which has no tower clause.

**Attack 2: build item 1 directly, from Part I and §9.** The simple conditions of level \(k+1\) at the step's pair \((U_{k+1},A'(B))\) with \(B\in\mathfrak B_k(2r^{\rm ct}_k)\) can be checked:
- curvature: \(|\partial U-\mathbf 1|<\alpha_0\eta^2\) for the real factor by B (17) and Lemma 5.4; for \(e^{i\eta A'}U\) by pr-lay (14) (\(\le4\alpha\) with \(\alpha=s(P)\));
- real gauges on \(O(LM)\) cubes with \(|A|,|\nabla A|<CM\alpha_0\): Corollary 9.10 (with Hölder clause);
- \(|A'|,|\nabla_UA'|<\alpha_1\): `a3-derivative.md` (31), \(\le2C_{\rm lin}C_b\sup|g_kB|\);
- \(|\mathbf J|<\alpha_0\) for the physical current: Theorem 4.1's current member, summed over rows, gives \(|J(B)-J(0)|\le C\sup|g_kB|\le2Cr^{\rm ct}_k=2Cc_{\rm ct}\alpha_{0,k}\), which is \(<\alpha_0/2\) for \(c_{\rm ct}\) small. (This is why (H-ct)\(^*\) uses an \(\alpha_0\)-sized radius, §10.1 (b).)

What remains is the **tower clause of \(\square_0\)**: every tower configuration of every \(Z\subset\square_0\) of level \(p\le k+1\) exists, with \(|\partial U_n(Z;\mathbf U)-\mathbf 1|<\alpha_0L^{-(j-p)}\eta_p^2\) and \(|J(U_n(Z;\mathbf U))|<\alpha_0L^{-(j-p)}L^{2(n-p)}\) (SA 9646, the tower clauses of the core). For the real factor, the curvature recursion \(v_{q+1}\le L^2v_q+C(L^2v_q)^2\) (ST1's AV/CURV, L128, imported from `a1-balaban.md` §3.5) gives a tower datum of radius \(Ca\lambda^2\), \(\lambda=L^{n-p}\), and Theorem 3's regularity radius (SA 9693–9700: "\(\Phi(B)\) is regular at the radius \(C(\varepsilon_1+\sup|B|)\)") then bounds the tower curvature. For the complex fluctuation, the only library argument is `c1-repr.md` §8 (Codex, "not yet checked by the other model", L220), whose "three real values" identity \(f(a+ib)=f(a)+if(b)-if(0)+Q(a+ib)-Q(a)-iQ(b)\) I checked (it follows from \(f(w)=f(0)+Df(0)w+Q(w)\) and complex linearity of \(Df(0)\)). Its bound on \(Q\) rests on its (7): "A1 (9.2) gives the crude bound \(|f(w)|\le S:=C_0\lambda^{-2}\)" on the enlarged ball \(\|w\|_\infty<c_T/\lambda\) (L180–L186). *Failure:* that enlarged-ball continuation of A1 (9.2), with \(C_0\) fixed before \(n,p\) and volume, is not in a frozen text, and I could not derive it from Theorem 3's polydisc, whose radius \(r_{\rm B}\) is fixed and does not grow like \(\lambda^{-1}\). The attack therefore establishes the simple conditions and reduces the complex tower clause to this one statement.

**Attack 3: avoid towers.** If the members' domains omitted the hereditary clauses, item 2 would follow from Theorem 4.1 at the flat reference and the simple conditions alone. *Failure:* IN1's norm (4) takes the supremum over \(\mathcal D_j(X)\), which includes the tower clauses by definition (IN1 L41), and the members' bounds are only known there. Shrinking the domain changes the class \(\mathfrak L_k(\theta)\), which is frozen IN1's induction hypothesis; its heredity would have to be re-proved (IN1 H-SF, L120–L143).

**The precise residual statement.** After Attack 2, (DOM-in) reduces to:

> **(DOM-in\(_\flat\)).** For a real \(U\) with curvature \(\le\varepsilon_0\eta_p^2\) on an admitted tower, \(\lambda=L^{n-p}\le1\), and \(\Phi(w)=U_n(Z;e^{i\eta_pw}U)\): \(\Phi\) is holomorphic on \(\|w\|_\infty<c_T/\lambda\) and \(|\eta_p^{-2}(\partial\Phi(w)-\mathbf 1)|+\lambda^{-2}|J_n(\Phi(w))|\le C_0\lambda^{-2}\) there, with \(c_T,C_0\) fixed before \(n,p\), depth and volume.

This is `c1-repr.md` §8 (7). Given it, `c1-repr.md` (8) gives the complex tower clause with the stronger factor \(L^{-2(j-p)}\), and (DOM-in) item 1 follows by SA 9767's inner substitution, which itself must then be rebuilt (it is SA's statement, not yet a library text). Item 2 then follows as indicated above. Owner: node DOM (critical path item 5), with BG1(2).

## 12. Result

**Proved in this text.**
1. **M1** (Theorem 3.10): the seven matching clauses between frozen P82's output and what (15) consumes. The only normalization read by the proof of (15) is the counting multiplier, which P82 supplies; (15) has no multiplier member; the outline's Theorem 4 multiplier value bound is the counting one and transfers to other normalizations only through \(\sup\ell_c/\mu_c\).
2. **(15) at a real critical reference** (Theorem 4.1) and **uniformly on the admitted layered class** (Theorem 5.7), as implications from frozen P82 Theorem P, P81 and `a3-derivative.md` §4, at interior elements, with \(C_4(L,\alpha_{\rm H})\), \(\theta_4=\min(\delta_0,\delta_w)/8\), fixed at IN1 row 3, before \(\kappa\), independent of \(M,\bar\kappa\).
3. **(H-prof)**: the literal statement is refuted at drop-out windows (Proposition 8.6, conditional on such a history); the corrected (H-prof♯) (Theorem 8.5) is proved and the consumer closes with a larger \(X_0\) (Corollary 8.7).
4. **The fine-mesh Hölder estimate** (Theorem 9.9) for the real regular background, uniform in the mesh, and the real part of PR1's clause (H) (Corollary 9.10), without FP1(2).
5. **(20)** of `b4-step.md` (Corollary 10.4), from the hypotheses IN1 assigns to OL1.
6. **(H-ct)\(^*\)** (Theorem 10.8) as an implication from (I1)–(I5), with an \(\alpha_0\)-sized radius and the doubled domain the gate asks for.

**First remaining Outstanding statement:** (DOM-in) of §11; after Attack 2 its residual is (DOM-in\(_\flat\)), the enlarged-ball continuation of A1 (9.2) (`c1-repr.md` §8 (7)).

**Other open inputs named here:** P81 (A1/F0/REG); (G1); OL1's hypotheses (S1)–(S5) for the actual members (IN1 H-OL); the decoupled response (I5) (PR1(2), a2-full (H-walk)); RCG4 and B (pr-lay imports); the complex part of clause (H) (`bx-fix.md` Proposition I).

**What changes elsewhere (evidence for the lead; no other file was edited).**
- `st1-r4.md` L135 and Theorem 14 hypothesis 1: "the remaining matching item on this route is M1" can cite Theorem 3.10; (15) on the layered class can cite Theorem 5.7 (with its imports).
- `a3-derivative.md` L537, L556: M1 is a convention, now fixed: counting multiplier; conversion \(\omega^{\mu,\ell}=(\ell/\mu)\omega^{\rm cnt}\).
- `a2-full.md` Corollary IV.1: replace (H-prof) by (8.3) and add the \((\log\theta_k)^r\) term to its ceiling; Theorem V: use radius \(c_{\rm ct}\alpha_{0,k}\), not \(r_k\sim\alpha_{1,k}\).
- `ym4-assembly.md` PR1(6): PR-H's (H-prof) part is closed in corrected form; its (H-ct) part reduces to DOM (item 5), H-OL (item 9), (G1) and the decoupled response; `assembly-status.md` §3 item 2 waits on item 5.
- `b4-step.md` §11's first stop (20) is closed at the level of OL1's hypotheses.
- `bx-fix.md` (H): its real clause is supplied by Corollary 9.10.

Not yet refereed. Research text; it grants no status.
