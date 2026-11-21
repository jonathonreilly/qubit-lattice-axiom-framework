# SF + OL: the one-step formation theorem (IN1 H-SF), NL1(1) B1, and H-OL — pass 1 draft

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05. Pass 1 (long draft) of critical-path item 9 of `library/assembly-status.md` (L190). Not checked by another model. Research text, not an audit; it grants no status. Every argument is by hand; no computation is a proof step.

**Credit.** The outline being rebuilt is Ethan Sussman and Levent Alpoge's (SA = `sa/ym4.tex`; Claude and Codex are authors of its text). The block-averaging, background and pointed-extraction mechanisms are Balaban's (CMP 109, 116, 119) and, for the lattice gauge RG, Dimock's (I–III). Library inputs by Claude and Codex keep their stated premises: `prefactor-loc.md` (Claude), `b-value.md` (Codex), `b2-extract.md` (Claude), `b4-step.md`, `b4-induction.md` (Codex), and the frozen texts named below.

**Words.** *Proved* means proved here by hand as an implication from the inputs named at that place. *Outstanding* means not proved here. "Lx" is line x of the named file in this clone; "SA n" is line n of `sa/ym4.tex`.

## 0. Result and status

| Clause | Where | Status |
|---|---|---|
| H-OL: actual background is the multi-level CV branch read by prefactor-loc / b2-extract (Id) | Lemma 3.1 | **proved** (definition match, SA 5631–5661, st1-r4 L41) |
| H-OL: relative (Y3) and absolute gauge forms agree at real block-axial references; the orbit normalizer is a constant | Lemma 3.2 | **proved** (exact, nonperturbative) |
| H-OL: companion normalizer coefficient is intrinsic, \(b[\mathbf N_l]=b[\Phi_l]\) | Prop. 3.4 | **proved** given G-ID(cov) (hma Thm 8, conditional on PH1–PH4) and the assignment rule NA (a definition) |
| H-OL: localized-to-bulk identification | Lemma 3.5 | **proved** |
| H-OL: companion normalization \(b^0_j=\mathcal A_j-\mathcal A_{j-1}\), \(\mathcal A_0=0\), \(\mathcal A_j=b[\Psi_j]\) | Prop. 3.6 | **proved** from prefactor-loc Corollary T (checked by Codex, b-value L6–14) |
| H-OL: \(|\mathcal A_j-jc_0|\le c_2(L)\) (Theorem V) | §3.7 | **checked here** (assembly and arithmetic; first failing step none); estimates (4)–(9) read, not re-derived |
| H-OL / OL1(1) B2: own-coefficient pointed cancellation (20) for the actual members, at the flat point | Thm 4.3 | **proved** conditional on (TI) for the actual member (supplied conditionally by b4-induction, Steps 5–6) |
| cp12 L412 Outstanding (window response vs companion) | Lemma 4.1, Remark 4.2 | **dissolved** in the ordinary unlayered region; in layered regions it is D7 bullet 2 (item 4) |
| cp12 D7 bullets 3–4 for actual members | Lemma 4.4 | **proved** except the pair-ball inclusion (ER8u) |
| cp12 D7 bullets 1–2 for actual members at curved/layered data | §4.4 | **Outstanding** (items 1, 4, 5) |
| H-OL summable age decay; IN1 (13) second clause | Cor. 4.6 | **proved** conditional on D7 (cp12 Lemma 9) |
| NL1(1) B1 for the actual gas | §5 | reduced (no new proof): intrinsic part checked chain; old-origin type = OSF-loc |
| H-SF: decomposition \(b_{k+1}=b^0_{k+1}+e_{k+1}\) | Prop. 6.1 | **proved** (linearity + NA) |
| H-SF (11), marked term \(C_v^{\rm flow}\theta_k^{-(\kappa_0-4)/2}\) | Lemma 6.2 | **proved** conditional on ER8u and flat response decay |
| H-SF (11), fresh unmarked term \(C_f\theta_k^{-1/2}(\log\theta_k)^{p_0}\) | Thm 6.3 | **proved** conditional on [BG-u], [R], [B1♭] |
| H-SF (11), carried-member term | §6.4 | **Outstanding: Lemma NFE** (three attacks) |
| H-SF formation, (12), (13) first clause, structure | §6.5 | imports (item 8 CI, item 6 HM); not proved here |
| Constant order | §8 | **proved** (no cycle); \(c_0,c_2\) depend on \(L\) only |

**First remaining Outstanding statement, in item 9's order:** Lemma NFE (§6.4): the near-flat extension of the carried regular companions, with the coefficient-scale bound \(C_{\mathfrak n}g_{j-1}(\log\theta_{j-1})^{p_0}\). Attack 1 (Cauchy on the class domain) fails by the factor \(\alpha_j^{-2}=\theta_j(\log\theta_j)^{-2q}/C_0^2\). Attack 2 (dial Schwarz) works for the fresh part but needs NFE for the carried part. Attack 3 (induction of NFE through the near-flat B1 with the pointed age gain) stops at [BG-u]: a uniform-in-depth analyticity radius of the k-fold critical branch around the flat datum. The library's checked A1 (9.2) radius shrinks with depth (b2-extract L185).

**Supplied to OSF-loc** (ci-draft §14): of SA's four parts of "the renormalisation assertion" (SA 19666–19669), this text supplies the correct counterterm (coefficient identification: Prop. 3.4, Lemma 3.5, Thm 4.3) and covariance of the pointed Hessian conditional on (TI) (Thm 4.3 via b2-extract Lemma R). It does not supply regularity of the background within the window or uniform membership after substitution (D7 bullets 1–2, items 1, 4, 5). Given those, OSF-loc's pointed-member part follows from cp12 Lemma 9 with \(f_\nu=C(1+\nu)^{3/2}L^{-\alpha_{\rm H}(\nu-1)}\) (Cor. 4.6). Details in §7.

## 1. The clauses exactly as the frozen consumers read them

### 1.1 IN1 (frozen `in1.md`, with Amendment 1)

**H-OL** (in1 L110–116): "The actual companion normalizers have coefficients
\(b_j^0=\mathcal A_j-\mathcal A_{j-1},\ \mathcal A_0=0,\ |\mathcal A_j-jc_0|\le c_2,\ c_0=\frac{11}{3\pi^2}\log L\) (10). The readout (5), its own-coefficient subtraction and summable age decay apply to the actual regular members. This includes the localized-to-bulk identification and normal convergence needed to use the value in (10)." Its Outstanding note (L118): "OL1 must supply the companion, normalization and localization sum; scalar stopping arithmetic cannot supply them."

The parts of H-OL, as I separate them for proof:

- **OL-a** the actual background read by (5) (the response \(\mathfrak h_\infty\), L59–60);
- **OL-b** the companion normalizer and its coefficient \(b^0_j\);
- **OL-c** companion normalization \(b^0_j=\mathcal A_j-\mathcal A_{j-1}\), \(\mathcal A_0=0\);
- **OL-d** the value \(|\mathcal A_j-jc_0|\le c_2\) (Theorem V);
- **OL-e** localized-to-bulk identification and normal convergence;
- **OL-f** own-coefficient subtraction for the actual regular members (SA R14, B2);
- **OL-g** summable age decay (feeds (13) and OSF-loc).

The readout (5) (in1 L57–66) reads the companion \(\widehat E\) through \(\operatorname{Hess}\widehat E(\widehat X,\cdot,z)[\mathfrak h_\infty\delta^a_c,\mathfrak h_\infty\delta^a_{c'}]\), colour-averaged, and \(b[\widehat E]=\sum_u\Pi^E_{\mu\nu}(u)u_\mu u_\nu\). L64: "Absolute convergence, displacement dependence, independence of \(\mu\ne\nu\), Ward identities and this normalization are hypotheses of OL1. Each pointed member subtracts its own coefficient times the tent Wilson action".

**H-SF** (in1 L120–139). "From any current presentation satisfying the class conditions below, the family \(\widehat E^{(k+1)}\) and its readout are formed at \((\theta_k,x_k)\), *before* choosing \(\theta_{k+1}\). They obey
\(b_{k+1}=b_{k+1}^0+e_{k+1},\ |e_{k+1}|\le u(\theta_k):=C_f\theta_k^{-1/2}(\log\theta_k)^{p_0}+C_v^{\rm flow}\theta_k^{-(\kappa_0-4)/2}\) (11). The constants precede \(\gamma\), and formation uses only the current prefix and the weak constants (1). With a frame prolongation and the next tube condition, the exact step exists and preserves sourced integrals." It then returns (12) (\(\|E^{(k+1)}\|\le E_N+C_E(\ldots)\), \(\|R^{(k+1)}\|\le\theta_{k+1}^{-\kappa_0/2}\), the boundary bound) and (13) (\(w_{n,j}\le C_{\rm rad}(\alpha_{0,n}/\alpha_{0,j})^2\), \(f_\nu\le C_{\rm age}\nu^aL^{-b_{\rm age}\nu}\)), and "Analyticity, reality, gauge invariance, covariance, companion coherence and the pointed subtraction/age-decay structure are preserved." Outstanding (L143): "This is the actual formation theorem, not its numerical output bound alone."

**Consumers.** Lemma 4 (L373–386) uses (10)–(11) only through \(\varsigma=\sup_{x\ge X_0}u(x)\le\min(c_0/4,1)\) and the telescoped sum \(x_i-x_j=c_0(j-i)+a_j-a_i+\sum e_l\). Theorem 11 (L562–566) uses H-SF for "formation, the remainder and boundary bounds, domains, companion identification and the structural subtraction/age estimates". Theorem 12 (L604–607): "use H-SF to form the next family and coefficient at the current pair. Lemma 4 applies to this newly formed increment". The class \(\mathfrak L_k\) (L217) carries \(\|E^{(j)}\|\le E_0\), \(\|R^{(j)}\|\le\theta_j^{-\kappa_0/2}\), "the own-coefficient/age structure (5), (13)", "lattice covariance and companion coherence". It carries no separate bound on coefficients or on Hessian moments (see §6.4, §9 item 1).

### 1.2 The skeleton's NL1(1) and OL1(1),(3)

ym4-assembly L274 (NL1(1), B1): "Σ_{Y≁X} |z(Y)| e^{a(Y)} ≤ a(X) with strict room for complex sources and decoupling parameters, for the actual complex interacting matrices and all allowed cores; the connected-cluster logarithm converges absolutely with termwise differentiation and a majorant for each derivative; the finite-volume identity is exact (SA B1, L3910–3936)". L288: "(1) for the actual gas [SS] (SA B1 says the primitive hypotheses must still be verified for the actual complex interacting matrices)".

L258 (OL1(1), B2): "For an actual regular member with no stored colour spectators, with pointed totals converging normally, locally gauge invariant and covariant under unit translations and W₄, the coefficient is defined by (ph:extractor) and cancelled by the member's own midpoint tent action; |b(E)| + ‖T[E]‖ ≤ C a^{−2}‖E‖ on physical radius a; … the near-domain sum at one base point after vacuum and own-counterterm subtraction is ≤ C‖E‖[ρ²σ^{4+α_H} + ρ³σ⁶ + (1 + ρ²σ⁴)e^{−c/σ}]". L260 (OL1(3)): "|b[Ψ_k] − k c₀| ≤ c₂(L) (`b-value.md` Theorem V)". L262 (OL1(5), OL-nl): "b_j = b_j⁰ + f_j + q_j with |f_j| ≤ C x_{j−1}^{−1/2}(log x_{j−1})^p and |q_j| ≤ C x_{j−1}^{−(κ₀−4)/2}" — this is (11).

### 1.3 cp12 (frozen) and b4-step

cp12 D6 (L348–373) assumes, for \(F_z(B)=\sum_{X\ni z}G(X,\mathcal P(B),z)\): normal convergence through two derivatives, flat reference, gauge covariance of the background, gauge invariance of each member, unit-translation and full hypercubic covariance, the absolute moment (20), and "that the **same actual** \(H\) reproduce affine constant-curl fields modulo gradients, with zero current". Lemma 8 (L375–410) proves (21) under D6. L412: "**Outstanding — application to b4-step (20).** … A coefficient extracted using a companion \(h_\infty\) is not automatically the Hessian coefficient for an actual finite-window response. Exact identification or a quantified boundary comparison is required. IN1 H-OL retains these actual-family inputs." D7 (L414–429): four bulleted imports (holomorphic window map with (15) and whole-core room; the datum (22) with the boundary comparison; member bound, \(DG_X(0)=0\), D6, \(|b[G]|\le C\mathsf g/a_j^2\); domain counts and \(\rho_j^2\le C(1+n)\)). Lemma 9 (L431–455) gives the age gain (23) under D7.

b4-step L596–601 states (20): \(D^2(F_{j,z}-b_j(G)(A_{j,z}\circ\mathcal P_j))(0)[\ell_F,\ell_F]=0\), with "\(F_{j,z}(B)=\sum_{X\ni z}G_j(X,\mathcal P_j(B),z)\) uses the actual critical background pair" and "\(b_j(G)\) must be that member's prescribed bulk extractor". L628: "**First new stop:** (19), at the actual pointed cancellation and normalization (20)".

### 1.4 What OSF-loc reads (ci-draft, unrefereed)

ci-draft L550–555 states OSF-loc; L563 (Attack 3 (i)) says the needed age gain requires the cancellation of SA 19562–19568. I read SA 19561–19568: "The cancellation invoked here uses the full hypotheses of Section ch:pointed-hessian-cancellation, including gauge invariance, the actual normalized response, absolute Hessian moments and covariance of its *pointed* total under unit translations and the full hypercubic group. Under those hypotheses, subtracting its own coefficient times its own tent action cancels its marginal affine quadratic term at that base point." SA 19666–19669: "That estimate contains the renormalisation assertion: covariance of the pointed Hessian, the correct counterterm, regularity of the background within the window and uniform membership after substitution must be proved for the actual formation rule."

## 2. The actual construction and the imports

**Construction** (as in ci-draft §2.1). Gauge form: descent Theorem B's relative Y3 form, \(\mathsf A^{\rm Y}(P)=X(\mathbf p(P))+\mathsf C_V^{\mathsf T}\mathsf G^{\rm Y}_V\mathsf C_V\) (descent (4), L52–57), with soft-gauge exponent \(-x\Phi^{\rm Y}_V\) (hma (4), L60). Domains: ST1 (frozen `st1-r4.md`) with Tq0 (L82–89: \(r_\iota(m)=C_\iota g_m\ell_m^q\), \(\lambda_\tau\equiv1\), \(\Lambda_Q=1\)) and Amendment CV (L41: "the canonical background representative uses the averaged contour variable: \((\mathcal M^nU)(z,x)=I\) at each nonnode with parent \(z\)"). The averaging is SA's R3 (SA 5631–5650; st1-r4 (5)).

**Imports** (each a hypothesis here; owner item in brackets).

| Name | Statement used | Source, status |
|---|---|---|
| [BG] | uniqueness of the real critical branch near each regular datum, its holomorphic continuation, and its CV representative (SA 5651–5661 calls these "separate background theorems") | BG1; for fixed depth near flat: prefactor-loc Lemmas B, D (checked by Codex) |
| [FP1] | uniform-in-depth exponential decay and Hölder regularity of the flat responses \(R_{0,j}\) | FP1 (skeleton [C]); b2-extract L120 names "response decay uniform in j (SA 13323-13345)" |
| [BG-u] | a radius \(r_A>0\), fixed after \(L\) and independent of the depth, on which the k-fold critical branch and the step's pivot parametrization are holomorphic around the flat datum, with uniform bounds | Outstanding; A1 (9.2) as checked shrinks with depth (b2-extract L185); this is (ER7) at the flat point |
| [ER8u] | the pair ball of radius \(c\,\alpha_{0,j}\) around the flat pair lies in every member's core | Outstanding; b2-extract L120 "(ER8) and reduces to (ER7)" |
| [R] | real gap \(\mathsf A^{\rm abs}(P_0)\ge c_LI\) at real block-axial references of real bound \(<a_R\) | descent L62 (import R); [item 6] |
| [G-ID] | G-ID(cov): at admitted complete physical pairs the step's quadratic term is \(\mathsf A\) | hma Theorem 8 (L367), conditional on PH1–PH4 [item 6] |
| [TI] | invariance of the total of each actual regular member under the lattice symmetries about a level-j site and unit translations | b4-induction Steps 2, 5–6, \(\mathrm{TI}^E_k\) from \((ID)_k\), conditional on BX⁺, UR, YA, LOC |
| [D7] | cp12 D7, bullets 1–2, for actual members and data | Outstanding [items 1, 4, 5] |
| [CI], [HM] | formation (nl1-L Theorem 7) and H-M | items 8, 6 |

## 3. H-OL

### 3.1 OL-a: the background read by the coefficient

b2-extract §4 (L105) reads "the actual critical background pair" as "the j-fold augmented critical branch \(u_{0,j}\) of `prefactor-loc.md` Section 2: the R3 average … with the contour gauge insertion", and calls this reading **(Id)**. prefactor-loc L50–52 defines \(u_{0,k}\) as the critical branch of \(\widetilde S_k=S+\sum_{j<k}G_{j,j+1}\circ M_{0,j}\) on \(\{M_{0,k}U=z\}\). prefactor.md L59–62 defines \(G_{01}(U)=\sum_{x\notin N_1}w(T_{yx}(U))\), \(w(V)=1-\frac12\operatorname{tr}V\), with \(T_{yx}\) the contour mean from the block node, and L106 states that the augmented branch has \(G_{01}=G_{12}=0\).

**Lemma 3.1 (Id holds for the actual construction).** Let \(V\) be a real regular level-\(k\) datum near the flat datum, and let \(U^{\rm CV}(V)\) be the actual canonical background: the real critical orbit of \(\sum_pa_p\) on \(\{\mathcal M^kU=V\}\) (SA 5651–5657) in the CV representative of st1-r4 L41. Then \(U^{\rm CV}(V)=u_{0,k}(V)\). The same holds for the holomorphic continuations on any connected domain where both are defined and agree on a real open set.

*Proof.* (i) *Same average.* SA 5631–5641 defines \(\mathcal M\) as the symmetric contour average (R3): contour transports are means over shortest coordinate-ordered paths in the centred block. st1-r4 (5) (L38–39) is the same formula, and prefactor-loc L42 uses "the linearisation at 1 of the one-step R3 map". SA 7943–7960 (QC1, "the exact finite map") uses the same block \(B(y)=\{|x-y|_\infty\le(L-1)/2\}\) and the paths \(\mathcal G(y,x)\) "which complete one coordinate displacement before starting the next". So the three texts use one average.

(ii) *Same representative.* \(w(V)\ge0\) on \(SU(2)\), with equality only at \(V=I\) (since \(\frac12\operatorname{tr}V=\cos\phi\le1\)). Hence \(G_{j,j+1}(M_{0,j}U)=0\) for all \(j<k\) if and only if every contour mean \(T_{yx}(M_{0,j}U)\) from a level-\((j+1)\) node to a nonnode equals \(I\). This is CV's condition \((\mathcal M^nU)(z,x)=I\) at each nonnode with parent \(z\), for \(n=j<k\). On the residual orbit (gauge maps equal to one at the nodes; SA 5627 "A residual gauge function equals 1 at all nodes"), prefactor.md L66 gives \(T_{yx}(U^h)=T_{yx}(U)h(x)^{-1}\) when \(h(y)=1\). So each regular orbit has exactly one point with all \(T_{yx}=I\), namely \(U^h\) with \(h(x)=T_{yx}(U)\), fixed level by level from the top down as in prefactor-loc Lemma A(c).

(iii) *Same critical point.* \(S\) is gauge invariant and \(G_{j,j+1}\circ M_{0,j}\ge0\) vanishes at the CV representative. At \(U^{\rm CV}\) the gradient of \(\sum_jG_{j,j+1}\circ M_{0,j}\) vanishes (a nonnegative function at a zero). \(U^{\rm CV}\) is critical for \(S\) on the constraint set. So it is critical for \(\widetilde S_k\) on the constraint set. Uniqueness of the augmented branch near 1 (prefactor-loc L52, from prefactor.md L101–104) identifies it with \(u_{0,k}(V)\). Holomorphic identity on a connected domain from a real open set is the identity theorem. \(\square\)

*Scope.* This is near the flat datum, where prefactor's branch is constructed (at fixed depth). For curved real data the identification is the uniqueness part of [BG]. The coefficient (5) reads only the second jet at the flat datum, so the near-flat statement is what OL-a needs.

### 3.2 OL-b: the companion normalizer and the gauge form

**Lemma 3.2 (gauge forms at real axial references).** Let \(V\) be a real block-axial reference (all level-one contour means \(c_b(V;x)=I\)), and use descent's notation (descent (3), L43–50; hma (4)–(5), L59–68).

(a) \(\mathsf G^{\rm abs}_V=\mathsf G^{\rm Y}_V\) as bilinear forms.

(b) For a residual gauge map \(h=e^{i\lambda}\) (\(\lambda=0\) at every node), let \(D_V\lambda\) be the tangent at \(t=0\) of the fluctuation \(D(t)\) with \(e^{iD(t)}V=V^{e^{it\lambda}}\). Then \(\mathsf b_V(D_V\lambda)_{b,x}=-\lambda(x)\) at every nonnode \(x\) (with the convention of prefactor.md L66). This is independent of \(V\).

(c) The orbit normalizer is exact and constant: for every \(U\) on the regular branch, \(\int\prod_xdh(x)\,\chi\,e^{-x\,\mathrm{GF}(U^h)}=z^{r}\), with \(z=\int_{SU(2)}\chi(h)e^{-xw(h)}dh\), \(r\) the number of nonnodes and \(\chi\) the fixed conjugation-invariant cutoff. The same holds for \(\Phi^{\rm Y}_V\) in place of GF, at every real reference \(V\).

(d) At \(V\), the Gaussian of the soft-gauge exponent with weight \(x_{\rm gf}>0\) satisfies, on \(\ker B_V\) (\(B_V\) the linearized constraint),
\[
 \int_{\ker B_V}e^{-\frac12\langle D,(X+x_{\rm gf}\mathsf C_V^{\mathsf T}\mathsf G_V\mathsf C_V)D\rangle}dD
 =c(x_{\rm gf},r)\,J(V)\int_{\ker B_V\cap\ker\mathsf C_V}e^{-\frac12\langle D,XD\rangle}dD,       \tag{3.1}
\]
with \(c\) independent of \(V\), and \(J(V)\) the Jacobian of \((\lambda,D_c)\mapsto D_V\lambda+D_c\), provided \(X\) annihilates every \(D_V\lambda\). The right side is the linear delta-gauge Gaussian with its Faddeev–Popov Jacobian.

*Proof.* (a) By hma Lemma 1's proof (L72–74), \(\widehat W^V_{b,x}(D)=c_b(e^{iD}V;x)c_b(V;x)^{-1}\), and at an axial \(V\) this is \(W^V_{b,x}(D)\), with \(W^V_{b,x}(0)=I\). Write \(W^V_{b,x}(D)=\exp(i\Omega(D))\) with \(\Omega\) holomorphic near \(0\), \(\Omega(0)=0\), so \(D\Omega(0)=\mathsf b_V\) by (5). With \(\langle A,C\rangle=\frac12\operatorname{tr}(AC)\) and an orthonormal Pauli basis, \(\frac12\operatorname{tr}e^{i\Omega}=\cos\sqrt{\langle\Omega,\Omega\rangle}\), an entire function of \(\langle\Omega,\Omega\rangle\). Hence \(1-\frac12\operatorname{tr}W^V_{b,x}(D)=\frac12\langle\Omega(D),\Omega(D)\rangle+O(|D|^4)=\frac12\langle\mathsf b_V(D),\mathsf b_V(D)\rangle+O(|D|^3)\). Its Hessian at \(0\) is \(\langle\mathsf b_V(D),\mathsf b_V(E)\rangle\). Summing over \(b,x\) gives (a). (Off the axial set \(W^V(0)\ne I\), and descent L273 shows the two forms then differ by \(\cos\varphi\).)

(b) By the equivariance used in hma L72–74 and prefactor.md L66, \(c_b(V^h;x)=h(y_b)c_b(V;x)h(x)^{-1}=h(x)^{-1}\) at axial \(V\) with \(h(y_b)=1\). So \(W^V(D(t))=e^{-it\lambda(x)}\), and differentiating \(\operatorname{Log}\) at \(t=0\) gives \(-\lambda(x)\).

(c) For GF this is prefactor.md L66–68, re-proved: \(\mathrm{GF}(U^h)=\sum_xw(T_{yx}(U)h(x)^{-1})\); for each independent nonnode variable \(h(x)\), Haar translation by \(T_{yx}(U)\) removes it; the cutoff is conjugation invariant; the integrals factor over nonnodes. For \(\Phi^{\rm Y}_V(D)=\mathrm{GF}((e^{iD}V)^v)\) with \(v=c_b(V;\cdot)\) fixed (hma (4)), the composition with the fixed gauge map \(v\) is absorbed by the same Haar translation.

(d) Decompose \(\ker B_V=\{D_V\lambda\}\oplus(\ker B_V\cap\ker\mathsf C_V)\). The first summand lies in \(\ker B_V\) because the average is residual-gauge invariant. The sum is direct and spanning: by (b), \(D\mapsto(\lambda,D_c)=(-\mathsf C_VD,\,D+D_V\mathsf C_VD)\) is the inverse map, since \(\mathsf C_V(D+D_V\mathsf C_VD)=\mathsf C_VD-\mathsf C_VD=0\). In these coordinates \(\mathsf G_V\) vanishes on \(\ker\mathsf C_V\), is the cross-term-free \(\sum_x\langle\lambda(x),\lambda(x)\rangle\) on gauge directions (by (b)), and has no cross term. \(X\) has no gauge rows by hypothesis. So the quadratic form is block diagonal, and Fubini gives (3.1) with \(c=(2\pi/x_{\rm gf})^{3r/2}\). \(\square\)

The hypothesis "\(X\) annihilates every \(D_V\lambda\)" is the statement "The action Hessian kills \(D\), since the background is stationary" (b-value L75): \(S\) and the constraint are residual-gauge invariant and \(V\) is constrained-critical, so differentiating \(DS(e^{iD}V)[E]=\lambda\cdot DM\) along the orbit at \(D=0\) gives \(X(D_V\lambda,\cdot)=0\). For the actual \(X\) (pr-lay (7) without \(K_{\rm GF}\), descent L57) this is the physical-pair statement of [G-ID]: at a complete physical pair the quadratic term is the constrained Wilson Hessian plus the gauge term.

**Definition 3.3 (assignment rule NA).** The *companion normalizer* \(\mathbf N_l\) of step \(l\) is the logarithm of the step's full Gaussian factor as a function of the level-\(l\) datum, normalized at the flat datum: the compressed determinant and all elimination factors \(z^{(j)}\) (hma L277, SA 17528–17545), all chart and pivot Jacobians at zero fluctuation, and the orbit normalizer. Every other term of the step is a non-Gaussian member. This is a definition of the actual construction's filing, not a theorem. It removes hma L277's item "companion and coefficient readout" as an assignment problem; its bounds remain hma's.

**Proposition 3.4 (the companion coefficient is intrinsic).** Assume [G-ID] at the real block-axial physical pairs of the flat neighbourhood, Lemma 3.1, and NA. Then \(b[\mathbf N_l]=b[\Phi_l]\), with \(\Phi_l\) the step-\(l\) Gaussian logarithm of prefactor-loc L54. In particular \(b^0_l:=b[\mathbf N_l]\) does not depend on the gauge form (Y3, absolute, or prefactor's insertion) or on the gauge weight.

*Proof.* \(b\) is a linear functional of the Hessian at the flat datum along real directions (in1 (5)); the Hessian of a holomorphic function at a real point along real directions is the real Hessian. So \(b[\mathbf N_l]\) depends only on \(\mathbf N_l\) restricted to real data near flat. By Lemma 3.1 those data have real block-axial CV backgrounds. On them: (i) by Lemma 3.2(a) the Y3 and absolute precisions coincide; (ii) by Lemma 3.2(c) the orbit normalizer is a constant; (iii) by Lemma 3.2(d), the Gaussian factor is a \(V\)-independent constant times the delta-gauge Gaussian with its Jacobian \(J(V)\); (iv) NA puts the elimination factors and chart Jacobians into \(\mathbf N_l\), and b-value L46–50 ("If pivot elimination gives \(a=Cb\) and Jacobian \(\prod_cz(c)\), … \(\log Z=\sum_c\log z(c)-\frac12\log\det(C^TTC)+\)constant") shows that their sum is the Gaussian integral in the original Haar-normalized coordinates, independent of the pivot choice. The fluctuation chart \(D\mapsto e^{iD}V\) is a left translate of the exponential chart, so its Haar density at \(D=0\) is \(1\) for every \(V\). prefactor's \(\Phi_l\) is the same constrained Gaussian, with prefactor's insertion, whose normalizer is the constant \(z_g^r\) (prefactor.md L66–68), and to which (i)–(iii) apply (b-value L75–88 proves the same linear Faddeev–Popov identity for it). Two functions that differ by a constant on a real neighbourhood of flat have the same Hessian there. \(\square\)

*What remains.* [G-ID] is supplied by hma Theorem 8 only under PH1–PH4 (hma L553, L600), and hma L557 keeps "the full vacuum interface, including elimination factors, class/boundary and companion/coefficient identifications" Outstanding. Proposition 3.4 removes the coefficient identification at the flat point from that list (given G-ID and NA); it does not supply the \(z^{(j)}\) bounds or class/boundary filing across changing records.

### 3.3 OL-e: localized-to-bulk

**Lemma 3.5 (localized-to-bulk).** Let \(G=\{G(X,\cdot,z)\}\) be a pointed family on every admissible torus \(T_N\) with a companion \(\widehat G\) on \(\mathbb Z^4\) (agreement on non-wrapping collared lifts), and suppose: (i) \(\sum_z G_z=\operatorname{Tot}_N\) on \(T_N\); (ii) DG vanishes at the flat pair (colour invariance); (iii) domain-weighted uniform moments: \(\sup_z\sum_{X\ni z}\sum_{b,b'}e^{\kappa'd_j(X)+m(|b-z|+|b'-z|)}|D^2G(X,0,z)[h\delta_b,h\delta_{b'}]|\le C_m\) for some \(\kappa',m>0\), for the companion and on each torus with \(N\)-independent \(C_m\) (this is what the class weight \(e^{\kappa d_j}\), Cauchy on a pair ball and response decay give); (iv) (Tr) for the companion. Then \(b[\widehat G]=b[\operatorname{Tot}]\), where \(b[\operatorname{Tot}]\) is the second moment of the bulk kernel \(H=\lim_N D^2\operatorname{Tot}_N(0)\).

*Proof.* On \(T_N\), \(D^2\operatorname{Tot}_N(0)(b,b')=\sum_zK^N_z(b,b')\) (a finite sum; (ii) removes the first-derivative chain term). Fix \(b,b'\). For each \(z\), \(K^N_z(b,b')-\widehat K_z(b,b')\) receives contributions only from domains \(X\ni z\) that wrap or leave the common collar; such domains have \(d_j(X)\ge cN/M-C\). By (iii) their contribution is at most \(2C_me^{-\kappa'(cN/M-C)}e^{-m(|b-z|+|b'-z|)}\). Summing over \(z\) gives at most \(C'e^{-\kappa'cN/M}\to0\). The torus response is the periodization of the bulk response (prefactor-loc Lemma B(vi)), and its image terms are bounded the same way. Hence \(H(b,b')=\sum_z\widehat K_z(b,b')\), absolutely convergent by (iii). By (Tr), \(\widehat K_z(x,y)=\widehat K_0(x-z,y-z)\). So \(\pi^H_{\mu\nu}(u)=\sum_z\widehat K^{\mu\nu}_z(x,x+u)=\sum_y\widehat K^{\mu\nu}_0(y,y+u)=\pi^{\widehat G}_{\mu\nu}(u)\), reindexing \(y=x-z\). Equal kernels have equal second moments. \(\square\)

This is the statement in prefactor-loc L214 (remark 1 to Corollary T), with its torus limit written out. Its hypothesis (iii) at fixed depth is b2-extract §4's (D), (Mo) row (L110). Uniformity in \(N\) is all that is used; uniformity in depth is not.

### 3.4 OL-c: companion normalization

**Proposition 3.6.** Under Proposition 3.4 and Lemma 3.5, \(b^0_l=\mathcal A_l-\mathcal A_{l-1}\) with \(\mathcal A_l:=b[\Psi_l]\), \(\mathcal A_0=0\), for every \(l\ge1\), exactly, uniformly in volume.

*Proof.* prefactor-loc Corollary T (L204–212): \(\sum_{l\le k}b[\Phi_l]=b[\Psi_k]\), from \(H_l=H_{\Phi_l}+R_l^{\mathsf T}H_{l-1}R_l\) and Theorem S (\(b[R^{\mathsf T}\Pi R]=b[\Pi]\) under Lemma A's (R-i), (R-ii)). Codex checked Lemmas A, B, D, Theorem S and Corollary T line by line, first failing step none (b-value L6–14). Subtract consecutive \(k\). \(\Psi_0=0\) by definition (prefactor-loc L54). Proposition 3.4 replaces \(b[\Phi_l]\) by \(b[\mathbf N_l]\). \(\square\)

I re-read Theorem S's mechanism for this use: \(R\) maps level-\(k\) to level-\((k-1)\) fields; (R-ii) says \(R\ell\) is affine with curl \(L^{-2}\operatorname{curl}\ell\) plus a gradient (prefactor-loc L93), and (R-i) fixes the field unit \(c/L\) (L94). Under the Ward identity the second moment reads only curls, so \(b[R^{\mathsf T}\Pi R]\cdot|\operatorname{curl}\ell|^2=b[\Pi]\cdot L^{4}\cdot|L^{-2}\operatorname{curl}\ell|^2\) per coarse cell (the factor \(L^4\) is the fine cells per coarse cell). My reading agrees with this identity; I found no failing step. (prefactor-loc's remark after Lemma A explains why (R-i) is still needed: it fixes the field unit in the bulk kernel's normalization.)

### 3.5 OL-d: check of Theorem V

**What I checked.** b-value §7 (L278–302) and the inputs it reads.

1. *Assembly.* (15) follows from (10) and (14) with \(z=\eta^2=L^{-2k}\): \(\frac{11}{6\pi^2}\log(1/z)=\frac{11}{6\pi^2}\cdot2k\log L=kc_0\). The other terms of (10): \(-z\widetilde\beta'(z)\) and \(\frac12z^2\widetilde\beta''(z)\) are bounded by \(C_M\) (14); \(|e_k|\le C_E(L)\). So \(c_2(L)=C_E+C_R+C_M\). Correct.
2. *Leading coefficient.* (13) \(\widetilde\beta=8(4-\frac13)I_2+r\). With \(u=\frac16I_2+O(1)\) (12) and \(v=4u-4I_2+O(1)\), two real charged colours give \(2u-v=4I_2-2u=(4-\frac13)I_2\). With \(\varphi=2f\), a coefficient \(c\varphi^2\) has second \(f\)-derivative \(8c\). So \(\widetilde\beta=\frac{88}{3}I_2+r\). The radial integral (L264–266): \(\int_{|q|<\delta}\frac{d^4q}{(2\pi)^4}\frac1{(q^2+z)^2}=\frac{2\pi^2}{(2\pi)^4}\int_0^\delta\frac{r^3dr}{(r^2+z)^2}=\frac1{8\pi^2}\big(\frac12\log\frac1z+O(1)\big)\). So \(I_2=\frac1{16\pi^2}\log\frac1z+O(1)\) and \(\widetilde\beta=\frac{88}{48\pi^2}\log\frac1z+O(1)=\frac{11}{6\pi^2}\log\frac1z+O(1)\). Correct.
3. *Normalization against IN1.* IN1 L111–114 and the skeleton L256 give \(c_0=\frac{11}{3\pi^2}\log L=\frac{11N^2}{12\pi^2}\log L\) at \(N=2\); the colour pairing \(\frac12\operatorname{tr}\) and \(A(e^{iB})=\frac12|dB|^2+O(B^3)\) are those of IN1 (5), cp12 D6 and b2-extract L44. The sign: \(\mathbf N\) is a log-density member, so \(x_{k+1}=x_k-b_{k+1}\) (in1 L564) decreases the Wilson coefficient by \(\approx c_0\) per step, which is asymptotic freedom; (26) of IN1 uses exactly this sign.
4. *Finite-rank terms* (L182–184). Per Bloch fibre, \(Q^{\mathsf T}Q\) has rank at most \(4\cdot3\) and \(DR^{\mathsf T}RD^{\mathsf T}\) at most \(3\); the weighted bounds are (4), (7). Correct as stated.
5. *Schatten bound* (9). \(\sum_{n\in\mathbb Z^4}(1+c|p+2\pi n|^2)^{-3}\) converges since \(6>4\). Correct.
6. *Gauge form.* Theorem V is for "the contour gauge of Section 1" (L280). Proposition 3.4 shows the actual Y3 companion normalizer has the same coefficient, given G-ID and NA. This was the identification IN1 L118 asked for.

**Read, not re-derived.** The uniform jets (4) (L113–127), the coercivity (5)–(6), the mixed bounds (7), the three-inverse truncation (8) and the numerator calculation (11)–(12). I found no failing step in reading them. The \(k\)-uniformity of every constant rests on (4), whose key step is "\(\prod_i(1+C_L|f|s_i^2)\le\exp(C_L|f|\sum_is_i^2)\). Both bounds are independent of \(k\)" (L120–121); this holds because \(s_i=L^{i-k}\) gives \(\sum_is_i^2\le(1-L^{-2})^{-1}\).

**Verdict.** Theorem V: first failing step none found in this check (assembly, arithmetic, normalization, finite-rank and Schatten steps checked; (4)–(8), (11)–(12) read). One other-model check: this one, by Claude. Codex wrote it.

### 3.6 OL-f, OL-g: deferred to §4

**Theorem 3.7 (H-OL, conditional).** Assume [G-ID] (item 6), [TI], [D7] and the inputs of Lemma 4.4. Then H-OL holds for the actual construction: (10) with \(c_0=\frac{11}{3\pi^2}\log L\) and \(c_2=c_2(L)\) of Theorem V; the readout (5) is the pointed coefficient of every actual member at every base (Theorem 4.3); its own-coefficient subtraction cancels the affine jet exactly (Theorem 4.3); the age decay is summable (Corollary 4.6); the localized-to-bulk identification is Lemma 3.5.

*Proof.* OL-a Lemma 3.1; OL-b Proposition 3.4; OL-c Proposition 3.6; OL-d Theorem V (§3.5); OL-e Lemma 3.5; OL-f Theorem 4.3; OL-g Corollary 4.6. \(\square\)

Without [D7], everything in Theorem 3.7 except the age decay (OL-g) holds, conditional on [G-ID] and [TI].

## 4. The pointed cancellation for the actual members (cp12 D6–D7, b4-step (20))

### 4.1 Which response the actual members read

**Lemma 4.1 (composition: no separate level-\(j\) window response).** Let \(n>j\), let \(V_n\) be a real level-\(n\) datum near the flat datum, \(U^*=u_{0,n}(V_n)\) the actual background (Lemma 3.1) and \(B_j=M_{0,j}(U^*)\) its level-\(j\) averages. Then \(U^*=u_{0,j}(B_j)\). Hence every level-\(j\) member in an ordinary (unlayered) region reads exactly the pair \(\mathcal P_j(B_j)\), with \(\mathcal P_j\) the \(j\)-fold branch, at the actual level-\(j\) datum \(B_j\). The identity continues holomorphically.

*Proof.* \(\{M_{0,j}U=B_j\}\subset\{M_{0,n}U=V_n\}\) because \(M_{0,n}=M_{j,n}\circ M_{0,j}\). On the smaller set the terms \(G_{i,i+1}\circ M_{0,i}\) with \(i\ge j\) are constant, since \(M_{0,i}=M_{j,i}\circ M_{0,j}\) is constant there. So \(\widetilde S_n=\widetilde S_j+{\rm const}\) on the smaller set. \(U^*\) is critical for \(\widetilde S_n\) on the larger set, hence on the smaller submanifold through \(U^*\), hence critical for \(\widetilde S_j\) there. Uniqueness of the \(j\)-fold branch near 1 gives \(U^*=u_{0,j}(B_j)\). This is the argument of prefactor-loc (2.1) (L60) iterated. Continuation: the identity theorem. \(\square\)

**Remark 4.2 (what cp12 L412 asks, and what is left).** cp12 L412 worries that the coefficient read with the companion response \(h_\infty\) need not be "the Hessian coefficient for an actual finite-window response". By Lemma 4.1, in an ordinary region there is no second response at level \(j\): the window enters only through the datum \(B_j\). The coefficient identity (20) is a statement about the composite \(F_z=G_z\circ\mathcal P_j\) at the flat datum and is proved below for the actual member. What remains is a statement about the **datum**: how close the actual \(B_j\) (induced from later levels, possibly through ST1's layered background) is to an affine field near \(z\). That is cp12 D7 bullet 2, (22) and its boundary comparison. In layered regions the actual pair is ST1's layered background, not \(\mathcal P_j(B_j)\), and its comparison with \(\mathcal P_j(B_j)\) near an ordinary base is also bullet 2 (DR, item 4; P82M, item 1).

One reading point for D7. cp12 Lemma 9 (L449–451) expands \(G_X\) at \(\mathcal P^W(D)=L_F+E_X\) and invokes Lemma 8 for "the complete affine tensor sum". Lemma 8 is for the composite with a response reproducing affine fields *modulo gradients* (D6, L360–361). The actual members are known to be invariant only under level-\(j\) block-constant bare gauge maps (b2-extract L108, from carrier-adopt Lemma L(c) and h-walk-fix Theorem IC). So \(L_F\) in D7 must be read as \(\mathfrak h_\infty\ell_F=(\ell_f+d\psi,0)\), the bulk response to the affine datum including its bare gradient (prefactor-loc Lemma A(c)–(d)), not the bare affine field \((\ell_f,0)\). With that reading the pair-form tensor sum equals the composite jet and Lemma 8 applies. With the bare reading it would need invariance under the non-block-constant bare map \(e^{i\psi}\), which is not supplied. cp12 D7 bullet 2 compares \(D\mathcal P^W(0)\ell_F\) with "\(L_F\)" via "the affine problem", whose solution is \(\mathfrak h_\infty\ell_F\); so the frozen text is consistent with this reading, and I record it as a precision note, not an error.

### 4.2 The cancellation

**Theorem 4.3 (own-coefficient cancellation for actual members).** Let \(E^{(j)}\) be an actual regular member of level \(j\) with its companion, gauge invariant under level-\(j\) block-constant maps, colour invariant, holomorphic on its core with the class bound, and assume [TI] for it. Replace it by its re-pointed family \(\bar E^{(j)}\) (b2-extract Lemma R, L136–147). Then for every base \(z\) and all affine \(\ell,\ell'\) of constant curl,
\[
 D^2\big(F_z-b[\widehat{\bar E}^{(j)}]\,A_z\circ\mathcal P_j\big)(0)[\ell,\ell']=0,
 \qquad F_z=\textstyle\sum_{X\ni z}\bar E^{(j)}(X,\mathcal P_j(\cdot),z),             \tag{4.1}
\]
as absolutely convergent extended Hessians, and \(b[\widehat{\bar E}^{(j)}]\) is IN1's readout (5) and equals \(b[\operatorname{Tot}E^{(j)}]\). This is b4-step (20) and cp12 D6's cancellation (21) for the actual member, at the flat datum.

*Proof.* Apply b2-extract Theorem P (L65–101) to \(\bar E^{(j)}\). Its inputs:

- (C) holds: b2-extract L108 (constant maps are block-constant; prefactor-loc Lemma D(c)).
- (G) holds given (Id): b2-extract L109; (Id) is Lemma 3.1.
- (D), (Mo) hold at fixed \(j\): b2-extract L110 gives \(C_m(z)\le Cg_jr_j^{-2}\) from the near-zero core of radius \(r_j>0\) (A1 (9.2), checked), the member bound and fixed-depth response decay. Lemma R(ii)–(iv) keeps them for \(\bar E\), with \(\sup_zC_m(z)\) and at most the factor \(M^4\) in rooted counts.
- (AR) holds given (Id): b2-extract L111, from prefactor-loc Lemma A with \(\eta=L^{-j}\) and Lemma B's decay.
- (H_z) at every \(z\) and (Tr): b2-extract Lemma R(i) for \(\bar E\); Lemma R(v) shows the total is unchanged exactly when [TI] holds, so the re-pointed family is a legitimate filing of the same effective action (SA 6229–6231, quoted at b2-extract L149, "supplied once, for every torus and list").

Theorem P(c)–(d) gives (4.1) at \(\ell=\ell'\) with \(b=b_z=b[\bar E]\); polarization gives \(\ell\ne\ell'\). Theorem P(d) identifies \(b_z\) with the bulk extractor \(\sum_u\pi_{\mu\nu}(u)u_\mu u_\nu\) of the companion composite kernel; the colour average of IN1 (5) is Theorem P Step 2's \(\delta_{ab}K_z\). That is IN1's (5). Lemma 3.5 identifies it with \(b[\operatorname{Tot}]\). \(\square\)

I re-read b2-extract Theorem P's Steps 1–10 for this use and found no failing step. This re-reading is by Claude, the author of b2-extract, and is not an other-model check.

*Scope.* (4.1) is at the flat datum, at each fixed \(j\); no constant is uniform in \(j\) here (b2-extract Remark (iii), L101). It needs no window. Its domain restriction to a window (WF13a) changes the kernel only by long domains, weighted \(Cge^{-c/\sigma}\) (b2-extract Remark (i), L101; SA 15868–15876).

### 4.3 cp12 D7 for the actual members

**Lemma 4.4 (D7 bullets 3–4).** Let \(G\) be an actual re-pointed member of level \(j\) with class bound \(|G_X|\le\mathsf ge^{-\kappa d_j(X)}\) on its whole core, and assume [ER8u]: the pair ball of radius \(2a_j\), \(a_j=c_a\alpha_{0,j}\), around the flat pair lies in that core, in the chart norm \(\|P\|_X=\max_{X^+}(|A|,|\nabla A|,|J|)\). Assume [FP1] decay \(\|\mathfrak h\delta_c\|_X\le C_he^{-m_h\operatorname{dist}(c,X)}\) uniformly in \(j\). Then:

1. \(DG_X(0)=0\) for every \(X\).
2. The pointed tent action obeys \(|A_z(P)|\le Ca_j^2\) on that ball.
3. \(|b[G]|\le C\mathsf g/a_j^2\), with \(C\) depending on \(m_h,\kappa-\kappa_D\) and the rooted-count constant (which may carry \(M^4\), Lemma R(iv)).
4. Rooted counts \(\le C_De^{\kappa_Dq}\) and \(\operatorname{diam}X\le C_M(d_j(X)+1)\); domains leaving a window of radius \(R\) about \(z\) have \(d_j(X)\ge R/C_M-1\).
5. If the member radius and output radius are the Tq0 radii, \(a_j=c_a\alpha_{0,j}\), \(a_{\rm out}=c_a\alpha_{0,j+n}\), and \(\theta\) is a frame (in1 (1)), then \(\rho_j^2=\max(1,a_{\rm out}/a_j)^2\le4^q(1+\overline Bn/X_0)\le C(1+n)\).

*Proof.* 1. b2-extract Step 1: the adjoint representation of \(SU(2)\) has no nonzero invariant vector. 2. On the ball \(|\nabla A|\le2a_j\); \(|a_p(e^{i\eta A})|\le C\eta^4|\nabla A|^2\) for small complex \(\eta\nabla A\) (holomorphic, vanishing to second order at \(0\)); \(\eta^4\sum_ph_z(p)=1\) per orientation (b2-extract quadrature, L93). 3. Cauchy on the ball: \(|D^2G_X(0)[P,P']|\le\mathsf ge^{-\kappa d_j(X)}\|P\|_X\|P'\|_X/a_j^2\). With \(P=\mathfrak h\delta_x\), \(P'=\mathfrak h\delta_y\) and decay, \(\sum_{x,y}e^{m(|x-z|+|y-z|)}\|\mathfrak h\delta_x\|_X\|\mathfrak h\delta_y\|_X\le C(\operatorname{diam}X+1)^{8}\) for \(m<m_h\). The polynomial in \(\operatorname{diam}X\le C_M(d+1)\) is summed against \(e^{-(\kappa-\kappa_D)d}\). The second moment defining \(b\) is bounded by these absolute moments. 4. A connected union of \(M\)-cubes with tree length \(q\) is coded by a rooted tree walk with \(\le C(q+1)\) steps of bounded degree; the diameter of a union of cubes joined by a tree of length \(qM\) is \(\le M(q+1)\sqrt4\cdot\)const. 5. Frame (1) with \(i=j\), and \(j+n\) later: \(\theta_{j+n}\le\theta_j+c_5-\underline\lambda n\) and \(\theta_j\le\theta_{j+n}+\overline Bn\). So \(\alpha_{0,j+n}/\alpha_{0,j}=(\theta_j/\theta_{j+n})^{1/2}(\ell_{j+n}/\ell_j)^q\). The first factor is \(\le(1+\overline Bn/\theta_{j+n})^{1/2}\le(1+\overline Bn/X_0)^{1/2}\). The second is \(\le(\log(\theta_j+c_5)/\log\theta_j)^q\le2^q\) for \(X_0\ge1+c_5\). Squaring gives the claim. \(\square\)

### 4.4 D7 bullets 1–2: what is Outstanding

**Outstanding — D7 bullets 1–2 for actual members at actual data.** Bullet 1 (holomorphy of the actual window map on a product ball with the localized first response (15), and whole-core membership with room, including at young ages) is P82M's (15) on the admitted layered class (item 1) and DOM's admission (item 5), with [ER8u]. Bullet 2 (the actual datum is \(\ell_F+r\) with (22), and the boundary comparison \(\|D\mathcal P^W(0)\ell_F-\mathfrak h_\infty\ell_F\|_X\le C|F|(R+1)^se^{-cR}\)) is P82M's derivative bound for the induced data (item 1) and, in layered regions, DR's response (item 4). cp12 L457–462's three failures of the draft Lemmas 10.5–10.6 remain the precise failures of the earlier attempt; nothing here repairs them.

**At the flat datum** (the case the readout (5) and Proposition 3.6 use) both bullets hold in the bulk companion: the datum induced by an affine later-level field is exactly affine plus a gradient (prefactor-loc Lemma A(b), composed by Lemma 4.1), so \(r=0\), and no window is needed because the extended Hessian converges absolutely. Bullet 1 at the flat datum is [ER8u] plus [FP1]. This is what Theorem 4.3 and Lemma 4.4 use.

**Corollary 4.6 (age decay, conditional on D7).** Under D7 for the actual members (bullets 1–2 as imports; bullets 3–4 by Lemma 4.4 with [ER8u]), cp12 Lemma 9 applies with the cancellation of Theorem 4.3. So each old-scale base contributes \(C\mathsf g[\rho_j^2\sigma^{4+\alpha}+\rho_j^3\sigma^6]\), and a later unit window \(C\mathsf g\,\omega_n\), \(\omega_n=(1+n)^{3/2}L^{-\alpha(n-1)}\). For \(n\ge1\), \(\omega_n\le2^{3/2}L^{\alpha}n^{3/2}L^{-\alpha n}\). This is IN1 (13)'s second clause with \(a=3/2\), \(b_{\rm age}=\alpha_{\rm H}\), \(C_{\rm age}=2^{3/2}L^{\alpha_{\rm H}}C\). \(\square\)

## 5. NL1(1) B1 for the actual gas

**What is supplied (no new proof here).** b4-step §10 (L449–542) proves the B1 majorant, the connected-graph identity and nonvanishing for the *intrinsic* gas, conditional on the matrix envelope (6), the intrinsic UM1 bound (14), full-hull locality and heredity with [RT], and the order of um-envelope §5. Claude checked it line by line, first failing step none (b2-extract §1, L21). b4-induction Step 4 (L134–160) applies the same argument to **all** types with the common budget \(a_k\le C\{\delta(t)+t^{-1/2}+|x/t-1|+s_{k-1}N_{k-1}\}\) (its (2)). That budget reads the old-origin potential bound \(\|V^{\rm old}_{k-1}\|_\lambda\le Cs_{k-1}N_{k-1}\) (its (1) = b4-step (19)). ci-draft Theorem 9.1 gives normal (Mayer) domination for the main-step gas on the global fibre, and ci-draft Theorem 12.1 gives UM1 for the non-gauge types, both conditional on OSF-loc and AGE.

**Reduction.** For the actual gas, B1 holds as soon as every type has its UM1 budget on the actual domains. The intrinsic, gauge (hma Theorem 4), pivot/Haar and Wilson-cubic/Jacobian (ci-draft §5) types have theirs conditionally. The one remaining type is the old-origin potential, whose bound (19) is b2-extract's Proposition W (L160–184): it reads (20) (now Theorem 4.3, given [TI]), (ER8u), (BX), (UR), (YA). In OSF-loc's form it is ci-draft (6.2). So:

\[
 \text{NL1(1) B1 for the actual gas}\ \Longleftarrow\ \text{b4-step §10}+\text{UM1 for all types},\qquad
 \text{UM1(old origin)}\ \Longleftarrow\ \text{Thm 4.3}+[{\rm TI}]+[{\rm ER8u}]+({\rm BX})+({\rm UR})+({\rm YA})+[{\rm D7}].
\]

**Status.** Proved here: nothing new for B1 at actual (curved, layered) data; the old-origin input now reads only [TI], [ER8u], (BX), (UR), (YA) and [D7] besides the checked chain. *Outstanding:* [D7] bullets 1–2 at actual data (items 1, 4, 5), (BX) (`bx-fix.md` ends without proving it, b4-induction L68–71), [ER8u].

**At near-flat data** (the case needed in §6), B1 for the fresh gas is [B1♭] below.

## 6. H-SF

### 6.1 The decomposition

**Proposition 6.1.** Write the formed level-\((k+1)\) companion as
\(\widehat E^{(k+1)}=\mathbf N_{k+1}+G^{\rm fr}+G^{\rm car}+G^{\rm m}\):
the companion normalizer (NA); the *fresh* non-Gaussian part (the current fluctuation integral's Wilson, gauge, Jacobian and cutoff terms beyond the Gaussian); the *carried* part (the fluctuation-induced change of earlier regular members, filed into the new family; the earlier members stay listed); and the *marked* part (formed remainder-type terms and the induced change of earlier remainders). Then \(b_{k+1}=b^0_{k+1}+e_{k+1}\) with \(b^0_{k+1}=b[\mathbf N_{k+1}]\) and \(e_{k+1}=b[G^{\rm fr}]+b[G^{\rm car}]+b[G^{\rm m}]\). If the step is run with the ratio \(\tau=x/\theta\ne1\), the Gaussian \(G_{k+1,\tau}\) of SA 6252 has coefficient \(b^0_{k+1}\) exactly.

*Proof.* \(b\) is linear (in1 (5)). For the last sentence: rescaling the Gaussian precision by \(\tau\) changes its logarithm by \(-\frac{n}{2}\log\tau\), a constant in the datum. \(\square\)

This is SA's split (SA 6249–6256): "\(\|E^{(j),\mathrm u}-\mathbf N_j^\circ-\mathbf G_{j,\tau_{j-1}}\|_{j,\kappa}\le C_{\rm u}\bar g_{j-1}(\log\theta_{j-1})^{\mathfrak p_0}\), … \(|b_j^{\mathrm m}|\le C_b\bar g_{j-1}^{\kappa_0-4}\), \(|b_j^{\mathrm u}-b_j^0|\le C_b\bar g_{j-1}(\log\theta_{j-1})^{\mathfrak p_0}\)", which SA introduces with "Require, for fixed constants". SA lists the coefficient bound **separately** from the norm bound. §6.4 shows why it is a separate statement.

### 6.2 The marked term

**Lemma 6.2.** Assume [ER8u] at every level \(j\le k+1\) (pair ball of radius \(a_j=c_a\alpha_{0,j}\) in the core), [FP1], and the class bounds \(\|R^{(j)}\|\le\theta_j^{-\kappa_0/2}\) (in1 L217) together with the new one \(\|G^{\rm m}\|\le C_{\rm m}\theta_{k+1}^{-\kappa_0/2}\) on that ball. Then
\[
 |b[G^{\rm m}]|\le C_v^{\rm flow}\theta_k^{-(\kappa_0-4)/2},
 \qquad C_v^{\rm flow}=C(\kappa_0,\underline\lambda)\,C_{\rm D}\,(C_{\rm m}+2)\,(c_aC_0)^{-2}.
\]

*Proof.* Lemma 4.4(3) on the ball gives \(|b[H]|\le C_{\rm D}\|H\|/a_j^2\) for a family \(H\) bounded by \(\|H\|\) there. The coefficient is scale invariant (four dimensions; Theorem S, prefactor-loc L13), so a level-\(j\) family read at level \(k+1\) through the response has the same bound. With \(a_j^{-2}=(c_aC_0)^{-2}\theta_j(\log\theta_j)^{-2q}\le(c_aC_0)^{-2}\theta_j\): the formed part contributes \(\le C_{\rm D}C_{\rm m}(c_aC_0)^{-2}\theta_{k+1}^{-(\kappa_0-2)/2}\). The induced change of \(R^{(j)}\) is bounded on the ball by \(2\|R^{(j)}\|\) (the shifted pair stays in the core: [ER8u] with room, the box \(\mathfrak b\), and \(g_k\mathfrak b\ll a_j\)), so it contributes \(\le2C_{\rm D}(c_aC_0)^{-2}\theta_j^{-(\kappa_0-2)/2}\). By the frame (1), \(\theta_j\ge\theta_k+\underline\lambda(k-j)-c_5\ge\frac12(\theta_k+\underline\lambda(k-j))\) for \(X_0\ge2c_5\), and \(\theta_{k+1}\ge\theta_k-\overline B\ge\theta_k/2\). Hence the sum over \(j\le k\) is at most
\(2^{(\kappa_0-2)/2}\sum_{m\ge0}(\theta_k+\underline\lambda m)^{-(\kappa_0-2)/2}\le2^{(\kappa_0-2)/2}\big(\theta_k^{-(\kappa_0-2)/2}+\frac{2}{\underline\lambda(\kappa_0-4)}\theta_k^{-(\kappa_0-4)/2}\big)\) (compare with the integral; \(\kappa_0>8\), in1 row 1). \(\square\)

This explains the exponent \((\kappa_0-4)/2\) of (11) and of SA 3996: one power of \(\theta\) is lost to \(a^{-2}\), one to the sum over levels. *Outstanding:* [ER8u].

### 6.3 The fresh unmarked term: a coupling-dial argument

**Imports for this subsection.**

- **[BG-u]** There are \(r_A,r_P,r_\Pi>0\), fixed after \(L\) and before \(\kappa\), independent of the depth \(k\), \(M\), \(\bar\kappa\), such that: the step's fluctuation map \(\Pi(v,\xi)\) (background at level-\((k+1)\) datum \(v\), fluctuation \(\xi\) in the actual pivot-eliminated coordinates, satisfying the constraint exactly) and the k-fold critical action \(S_k\) are holomorphic for \(|v|<r_A\), \(|\xi|<r_\Pi\) (sup norms, level units), and each polymer integrand is holomorphic in the background pair on \(X^+\) for pair norm \(<r_P\), with bounds independent of \(k\).
- **[R]** descent's import R (L62): real gap \(c_L\) at real block-axial references of bound \(<a_R\); take \(r_A\le a_R/2\) small enough that complex perturbations of size \(r_A\) cost at most \(c_L/4\).
- **[B1♭]** the cluster expansion of b4-step §10 for the fresh gas defined below, on the polydisc \(|w|<w_0\), \(|v|<r_A\): polymer activities \(F_X(w,v)\) with \(|F_X|\le M_Fe^{-\mu\ell(X)}\), normal convergence, and the finite-volume identity. Its type budget is the Gaussian third-moment bound \(a\le C(LM)^4|w|\) proved in step (c) below, plus the fresh types' UM1 (ci-draft Theorem 5.1 and Proposition 5.2, unrefereed; hma Theorem 4 for the gauge type).

**The fresh family with a dial.** For complex \(w\) and datum \(v\) put
\[
 \Sigma(w,v;\zeta)=w^{-2}\big[S_k(\Pi(v,w\zeta))-S_k(\Pi(v,0))\big]
   +w^{-2}\Phi^{\rm Y}_{\Pi(v,0)}(w\zeta)-\log j_v(w\zeta),
\]
with \(j_v\) the Haar density times the pivot Jacobian, normalized by \(j_v(0)=1\) (its value at zero is in \(\mathbf N\) by NA). Let \(Z(w,v)=\int_{\rm box}e^{-\Sigma(w,v;\zeta)}d\zeta\), with the step's fixed real box \(|\zeta_b|\le\mathfrak b\), \(\mathfrak b=C_{\rm win}A_1(\log\theta_k)^{p_0}\) (nl1-L (1)–(5) via ci-draft L91). The physical step is \(w=x_k^{-1/2}\) (a change of variables \(\zeta\to(x_k/\theta_k)^{1/2}\zeta\) has a constant Jacobian). Put \(F(w,v)=\log Z(w,v)-\log Z(w,0)\) and \(b^{\rm fr}(w)=b[F(w,\cdot)]-b^0_{k+1}\), so that \(b[G^{\rm fr}]=b^{\rm fr}(x_k^{-1/2})\).

**Theorem 6.3 (fresh term of (11)).** Under [BG-u], [R], [B1♭], NA and [FP1],
\[
 |b[G^{\rm fr}]|\le C_f\,\theta_k^{-1/2}(\log\theta_k)^{p_0}
 \quad\text{for }\theta_k\ge X_0,\qquad
 C_f=\frac{32\,C_{\rm D}M_F}{r_P^2}\max\Big(\frac{2}{r_\Pi},\frac{8C_3}{c_L}\Big)C_{\rm win}A_1+1 .
\]

*Proof.* (a) *Removable singularity at \(w=0\).* Fix \(v,\zeta\). The function \(f(w)=S_k(\Pi(v,w\zeta))-S_k(\Pi(v,0))\) is holomorphic for \(|w||\zeta|<r_\Pi\), with \(f(0)=0\). Its derivative at \(0\) is \(DS_k(\Pi(v,0))[\partial_w\Pi(v,0)\zeta]\). The curve \(w\mapsto\Pi(v,w\zeta)\) lies in the constraint set, so its tangent is a constrained direction, and \(\Pi(v,0)=p_{k+1}(v)\) is constrained-critical (Lemma 4.1 and [BG]); so \(f'(0)=0\). Hence \(w^{-2}f(w)\) is holomorphic, with value \(\frac12f''(0)\) at \(0\): the constrained Hessian including constraint curvature (b-value L44–46). Likewise \(w^{-2}\Phi^{\rm Y}(w\zeta)\) has value \(\frac12\mathsf G^{\rm Y}(\zeta,\zeta)\) because \(\nabla\Phi^{\rm Y}_V(0)=0\) (hma (5), L63–66), and \(\log j_v(w\zeta)=O(w^2)\). So \(\Sigma(0,v;\zeta)=\frac12\mathcal Q_v(\zeta,\zeta)\), the companion normalizer's quadratic form (Proposition 3.4).

(b) *Domination.* Cauchy's estimate for \(w\mapsto w^{-2}f(w)\) on the disc \(|w|<r_\Pi/|\zeta|\) gives \(|\Sigma(w,v;\zeta)-\frac12\mathcal Q_v(\zeta,\zeta)|\le C_3|w|\sum_s|\zeta_s|^3\) for \(|w|\mathfrak b\le r_\Pi/2\), summing over local sites by the locality of \(S_k\) and \(\Pi\) (exponential decay; [FP1]). By [R], \(\operatorname{Re}\frac12\mathcal Q_v(\zeta,\zeta)\ge\frac{c_L}4|\zeta|^2\) for \(|v|<r_A\). On the box, \(C_3|w|\sum|\zeta_s|^3\le C_3|w|\mathfrak b|\zeta|^2\le\frac{c_L}8|\zeta|^2\) if \(|w|\le w_0:=\min(r_\Pi/(2\mathfrak b),\,c_L/(8C_3\mathfrak b))\). So \(\operatorname{Re}\Sigma\ge\frac{c_L}8|\zeta|^2\) on the box.

(c) *Small interaction in Gaussian \(L^1\).* Per site, \(|e^{-(\Sigma-\frac12\mathcal Q)}-1|\le C_3|w||\zeta_s|^3e^{c_L|\zeta|^2/8}\), and the Gaussian third moments are bounded. So the interaction's Gaussian \(L^1\) size per coarse cube is at most \(C(LM)^4|w|\le C(LM)^4w_0\), which tends to zero as \(\mathfrak b\to\infty\). This is the type budget of [B1♭]; with it, [B1♭] gives \(F(w,v)=\sum_XF_X(w,v)\), \(|F_X|\le M_Fe^{-\mu\ell(X)}\), holomorphic on the polydisc, normally convergent.

(d) *Coefficient bound on the dial disc.* Each \(F_X\) is a function of the background pair on \(X^+\), holomorphic for pair norm \(<r_P\) ([BG-u]). By Lemma 4.4(1),(3) with \(\mathsf g=M_F\), \(a=r_P/2\), \(\kappa\to\mu\): \(|b[F(w,\cdot)]|\le4C_{\rm D}M_F/r_P^2\) for \(|w|<w_0\). Also \(|b^0_{k+1}|\le4C_{\rm D}M_F/r_P^2\) after enlarging \(M_F\) to bound \(\mathbf N\) too. So \(|b^{\rm fr}(w)|\le8C_{\rm D}M_F/r_P^2\) on the disc.

(e) *Value at \(w=0\).* \(F(0,v)\) is the logarithm of the box-restricted Gaussian. It differs from the full Gaussian logarithm \(\mathbf N_{k+1}\) by \(\log(1-\Pr_v(\text{outside box}))\), which is holomorphic on \(|v|<r_A\) and bounded per cube by \(C(LM)^4e^{-c_L\mathfrak b^2/16}\). By Lemma 4.4(3), \(|b^{\rm fr}(0)|\le C(LM)^4e^{-c_L\mathfrak b^2/16}/r_P^2\le\theta_k^{-1/2}\) for \(X_0\) large.

(f) *Schwarz in the dial.* \(b^{\rm fr}\) is holomorphic in \(w\) on \(|w|<w_0\) (normal convergence permits differentiating under the sums). The function \(b^{\rm fr}(w)-b^{\rm fr}(0)\) vanishes at \(0\) and is bounded by \(16C_{\rm D}M_F/r_P^2\) there, so \(|b^{\rm fr}(w)-b^{\rm fr}(0)|\le16C_{\rm D}M_Fr_P^{-2}|w|/w_0\). At \(w=x_k^{-1/2}\le2\theta_k^{-1/2}\) (tube (3): \(x_k\ge\frac34\theta_k\)) and \(1/w_0=\max(2/r_\Pi,8C_3/c_L)\,\mathfrak b\), this is the claim. The condition \(x_k^{-1/2}<w_0\) is \(\theta_k^{1/2}\gtrsim(\log\theta_k)^{p_0}\), a floor on \(X_0\). \(\square\)

*Remarks.* (i) The argument uses the dial disc of radius \(w_0\asymp1/\mathfrak b\), much larger than the physical \(g\); the gain \(g/w_0=g\mathfrak b\) is exactly \(\theta^{-1/2}(\log\theta)^{p_0}\), the form of (11). (ii) It never uses a class norm of the members on the small domain \(\mathcal D_j\); it uses analyticity in the background on a ball of fixed radius \(r_P\) around flat. That is what makes the coefficient bound possible (compare Attack 1 in §6.4). (iii) Parity would improve the gain to \(g^2\) for the Wilson part, but (11) does not need it, and the box cutoffs and gauge terms need not be even.

### 6.4 The carried term: the first remaining Outstanding statement

**Statement (SF-car).** For the formed family at level \(k+1\),
\[
 |b[G^{\rm car}]|\le C_{\rm car}\,\theta_k^{-1/2}(\log\theta_k)^{p_0},
\]
with \(C_{\rm car}\) fixed in in1 row 8. Here \(G^{\rm car}=\sum_{j\le k}\Delta_j\), and \(\Delta_j\) is the fluctuation-induced change of the re-pointed earlier regular member \(\bar E^{(j)}-b_jA\) (including the earlier normalizers \(\mathbf N_j-b^0_jA\)), as filed into the new family.

The natural scale. Theorem S (prefactor-loc L13) says the linear-response pullback of \(\bar E^{(j)}-b_jA\) to level \(k+1\) has coefficient \(b[\bar E^{(j)}]-b_j=0\) exactly. So \(b[G^{\rm car}]\) comes only from the genuinely fluctuation-induced part \(\Delta_j\), which is at least first order in the induced shift. The question is the size of the constant.

**Attack 1 (Cauchy on the class domain).** Bound \(b[\Delta_j]\) by Lemma 4.4(3) on the core ball of radius \(a_j=c_a\alpha_{0,j}\), with \(\sup|\Delta_j|\le2\|E^{(j)}\|\le2E_0\) from the class (in1 L217). This gives \(|b[\Delta_j]|\le C_{\rm D}E_0\,a_j^{-2}=C_{\rm D}E_0(c_aC_0)^{-2}\theta_j(\log\theta_j)^{-2q}\). Adding the Schwarz gain in the induced shift (size \(g_k\mathfrak bL^{-\nu}\) in level-\(j\) units against radius \(a_j\)) gives at best \(C E_0\theta_j(\log\theta_j)^{-2q}\cdot g_k\mathfrak bL^{-\nu}/a_j\le CE_0\,\theta_j(\log\theta_j)^{p_0-3q}L^{-\nu}\).
*Why it fails:* the class bounds members only in sup norm on domains of radius \(\alpha_{0,j}\asymp\theta_j^{-1/2}(\log\theta_j)^q\). A function of size \(E_0\) on such a ball can have Hessian \(E_0/\alpha^2\), which is unbounded in \(\theta\). So the class \(\mathfrak L_k\) does not control coefficients of carried members. This is why SA states \(|b^{\rm u}_j-b^0_j|\le C_b\bar g_{j-1}(\log\theta_{j-1})^{\mathfrak p_0}\) as a separate requirement (SA 6255–6256), and it is a gap in the class, not only in the proof (§9 item 1).

**Attack 2 (dial Schwarz, as in Theorem 6.3).** Suppose the carried members were holomorphic on a near-flat ball of fixed radius. Precisely:

> **NFE\(_j\) (near-flat extension).** There are \(r_\flat\in(0,r_P]\) (in1 row 3) and \(C_{\mathfrak n}\) (row 8) such that \(\widehat{\bar E}^{(j)}-\mathbf N_j\) extends holomorphically from its class domain to the pair ball \(\mathfrak B_j(r_\flat)\) (pair norm \(<r_\flat\) on \(X^+\), level-\(j\) units, about the flat pair), with
> \(\sup_z\sum_{X\ni z}e^{\kappa d_j(X)}\sup_{\mathfrak B_j(r_\flat)}|\widehat{\bar E}^{(j)}(X,\cdot,z)-\mathbf N_j(X,\cdot,z)|\le C_{\mathfrak n}\theta_{j-1}^{-1/2}(\log\theta_{j-1})^{p_0}\);
> and \(\mathbf N_j-b^0_jA\) is holomorphic on \(\mathfrak B_j(r_\flat)\) with pointed bound \(C_{\mathbf N}r_\flat^2\) (it vanishes to second order at flat: value normalized, gradient zero by colour invariance).

Given NFE\(_j\) for all \(j\le k\), run Theorem 6.3's dial on \(\Delta_j(w,v)\): \(\Delta_j(0,v)=0\). In the composite (coarse-gauge-reduced) form the induced level-\(j\) datum from \(v\) and \(w\zeta\) is \(\ell_F+r\) with (22) at \(a_{\rm out}=C(|v|+|w|\mathfrak b)\), \(\sigma=L^{-\nu}\) (D7♭ below). Over a window of radius \(R\asymp\sigma^{-1}\) its size is at most \(Ca_{\rm out}\sigma\), so it stays in \(\mathfrak B_j(r_\flat)\), with \(\rho_j=\max(1,a_{\rm out}/r_\flat)\le2\), when \(|v|\le c\,r_\flat\) and \(|w|<w_\flat:=c\,r_\flat/\mathfrak b\). (On a larger dial disc \(\rho_j\) grows like \(|w|\mathfrak b/r_\flat\) and Lemma 9's factor \(\rho_j^3\) destroys the age sum; so the disc must not depend on \(\nu\).) Per later unit cell the sum over the \(L^{4\nu}\) old bases is then controlled by cp12 Lemma 9 with Theorem 4.3's cancellation: \(C\mathsf g_j\omega_\nu\), \(\mathsf g_j\) the NFE bound. Schwarz in \(w\) gives a factor \(g_k/w_\flat=g_k\mathfrak b/(c\,r_\flat)\), and Cauchy in \(v\) a factor \((c\,r_\flat)^{-2}\). Summing over \(j\) (\(\nu=k+1-j\)) and using \(\mathsf g_j\le C_{\mathfrak n}+C_{\mathbf N}r_\flat^2\),
\[
 |b[G^{\rm car}]|\le C\,(C_{\mathfrak n}+C_{\mathbf N}r_\flat^2)\,r_\flat^{-3}\Big(\sum_{\nu\ge1}\omega_\nu\Big)\,C_{\rm win}A_1\cdot2\theta_k^{-1/2}(\log\theta_k)^{p_0}.
\]
That is SF-car, given NFE\(_{\le k}\), Theorem 4.3 ([TI]) and D7♭ (below).
*Why it does not finish:* NFE is not in IN1's class and is not an output of any frozen text. It must be carried inductively, which is Attack 3.

**Attack 3 (induct NFE through the near-flat step).** Assume NFE\(_{\le k}\). The level-\((k+1)\) family on \(\mathfrak B_{k+1}(r_\flat)\) is \(\mathbf N_{k+1}+G^{\rm fr}+G^{\rm car}+G^{\rm m}\).

- Fresh: steps (a)–(f) of Theorem 6.3 bound \(F(w,v)\) itself, not only its coefficient: \(|F_X(x_k^{-1/2},v)-F_X(0,v)|\le2M_Fe^{-\mu\ell(X)}x_k^{-1/2}/w_0\le C\theta_k^{-1/2}(\log\theta_k)^{p_0}e^{-\mu\ell(X)}\) for \(|v|<r_A\). So the fresh part satisfies NFE\(_{k+1}\)'s bound with a constant \(C_{\rm fr}\) independent of \(C_{\mathfrak n}\).
- Carried: by Attack 2's estimate before taking coefficients, the pointed bound of \(G^{\rm car}\) on the near-flat ball is at most \(C(C_{\mathfrak n}+C_{\mathbf N}r_\flat^2)(\sum_\nu\omega_\nu)\,g_k\mathfrak b/r_\flat\). The part proportional to \(C_{\mathfrak n}\) carries the factor \(g_k\mathfrak b\to0\), so it is at most \(\frac12C_{\mathfrak n}\theta_k^{-1/2}(\log\theta_k)^{p_0}\) after a floor on \(X_0\); the rest has a constant independent of \(C_{\mathfrak n}\).
- Marked: Lemma 6.2's bound is \(o(\theta_k^{-1/2})\).
- Choose \(C_{\mathfrak n}\ge2(C_{\rm fr}+C_{\mathbf N}\text{-term}+1)\). Then NFE\(_{k+1}\) holds with the same \(C_{\mathfrak n}\). The base \(k+1=1\) has no carried part.

The inputs of this induction are: [BG-u], [R], [B1♭] for the full near-flat gas (the carried potentials' UM1 budget is the bound just stated, small with \(g_k\mathfrak b\)), Theorem 4.3 ([TI]), and

> **D7♭ (D7 at near-flat data).** For near-flat complex data \(|v|<r_A\) and fluctuations in the dial disc, the level-\(j\) datum induced near an old base \(z\) is, in an admissible coarse gauge, \(\ell_F+r\) with (22) at \(a_{\rm out}=C(|v|+|w|\mathfrak b)\), and the induced map is holomorphic on the product ball with cp12's first-response bound (15).

For real near-flat data the linear part of D7♭ is [FP1] (Hölder regularity and decay of the flat responses, composed by Lemma 4.1 and prefactor-loc Lemma A(b)); the nonlinear part is second order in \(|v|+|w|\mathfrak b\) and is bounded by Cauchy from [BG-u]. I did not write out that Cauchy step; it is routine given [BG-u], but D7♭ is not proved here.
*Why it fails:* every step reads [BG-u], a radius \(r_A\) independent of the depth on which the k-fold critical branch is holomorphic around the flat datum. The library's checked A1 (9.2) gives a radius that "shrinks with depth like \(L^{-(p-n)}\)" (b2-extract L185), and b2-extract L120 names the uniform version "(ER8) and reduces to (ER7)". b-value (4) (L113–127) proves the analogous uniformity only for the constant-flux jets at zero flux; it says "No bounded complex-flux operator on the whole infinite lattice is asserted" (L127). So Attack 3 proves NFE and SF-car **conditional on [BG-u] and D7♭**, and stops there.

**Conclusion of §6.4.** The precise remaining statement is
\[
 \textbf{[BG-u]}:\ \exists\,r_A>0\ \text{(after }L\text{, before }\kappa\text{, independent of }k,M,\bar\kappa)\ \text{with the k-fold branch holomorphic and uniformly bounded on }|v|<r_A,
\]
together with D7♭, which follows from [BG-u] and [FP1] by a Cauchy step not written here. Granted these, Lemma NFE and (11)'s carried term hold, and with Theorem 6.3 and Lemma 6.2, all of (11):

**Theorem 6.4 ((11), conditional).** Assume [BG-u], D7♭, [R], [B1♭] (fresh and carried near-flat gas), [FP1], [ER8u], [TI], NA. Then for the actual step \(|e_{k+1}|\le u(\theta_k)\) with \(C_f+C_{\rm car}\) in place of \(C_f\), and NFE\(_{k+1}\) holds; both are formed at \((\theta_k,x_k)\) from the current prefix only. \(\square\) (Proposition 6.1, Lemma 6.2, Theorem 6.3, Attacks 2–3.)

### 6.5 The rest of H-SF

The remaining H-SF clauses are not proved here. Their owners and best texts:

- *Formation, existence, sourced-integral preservation, domains*: nl1-L Theorem 7 (CI-base, CI-maps, CI-Gauss = IN1 H-M, CI-form) — item 8 (ci-draft) and item 6 (hm, descent, hma).
- *(12)*: the member bound \(E_N+C_E(\cdots)\) is b4-induction (3) (L162–165) for the ordinary step, conditional on its inputs; the remainder and boundary bounds are CI/LF outputs.
- *(13), first clause* (\(w_{n,j}\le C_{\rm rad}(\alpha_{0,n}/\alpha_{0,j})^2\)): a radius bookkeeping statement of R18 (SA 5993–6010); not treated here.
- *(13), second clause*: Corollary 4.6, conditional on D7.
- *Structure preservation*: analyticity, reality, gauge invariance and companion coherence are CI/HM outputs; covariance of pointed totals is Lemma R re-pointing given [TI]; the pointed subtraction is Theorem 4.3.

**Proposed class amendment (for the lead; not applied).** Add NFE\(_j\) to the class \(\mathfrak L_k\) of in1 L217, with \(r_\flat\) in row 3 and \(C_{\mathfrak n}\) in row 8. Without it, H-SF's (11) is asked of every class member, and Attack 1 shows the class bounds alone cannot give it. With it, Theorem 6.4 returns it.

## 7. What this supplies to OSF-loc

OSF-loc (ci-draft L550–555) bounds, for each age \(\nu\) and each family carried from level \(j=i-1-\nu\), the oscillation of its nl1-L Theorem 4 presentations by \(C_{\rm OSF}f_\nu\|G\|\). ci-draft's Attack 3 (L563) reduces its pointed-member part to (i) the own-coefficient cancellation, (ii) P82M's level-uniform derivative bound, (iii) a \(\nu\)-uniform expansion. SA 19666–19669 lists the four parts of "the renormalisation assertion".

| SA 19666–19669 part | Supplied here? | Where |
|---|---|---|
| "the correct counterterm" | **yes**, at each fixed \(j\): the subtracted coefficient is the member's own pointed coefficient at every base, equal to IN1's readout and to \(b[\operatorname{Tot}]\) | Thm 4.3, Lemma 3.5, Prop. 3.4 |
| "covariance of the pointed Hessian" | **yes, conditional on [TI]**, by re-pointing | Thm 4.3 (b2-extract Lemma R) |
| "regularity of the background within the window" | **no** at actual curved/layered data (D7 bullet 2; items 1, 4); at the flat datum it is exact (§4.4) | §4.4 |
| "uniform membership after substitution" | **no** (D7 bullet 1; item 5 and [ER8u]) | §4.4 |

Also supplied: D7 bullets 3–4 for actual members (Lemma 4.4, given [ER8u]); the reading \(L_F=\mathfrak h_\infty\ell_F\) that makes cp12 Lemma 9's appeal to Lemma 8 valid for members invariant only under block-constant maps (Remark 4.2); and the age function \(f_\nu=C_{\rm age}\nu^{3/2}L^{-\alpha_{\rm H}\nu}\) in IN1 (13)'s form (Corollary 4.6).

**Consequence.** Given D7 bullets 1–2 at the actual data, cp12 Lemma 9 with Theorem 4.3 gives the per-window bound \(C\mathsf g\,\omega_\nu\) for each pointed regular family after its own subtraction. That is SA's (OSF3) times the base count (SA 19597–19599, quoted at ci-draft L362), which is the pointed-member part of OSF-loc in the per-window form. Two steps remain on item 8's side and are not done here: translating the per-window bound into OSF-loc's oscillation form over switches and fluctuation polydiscs (ci-draft (6.2)), and the remainder/defect part (SA OSF5–OSF6). ci-draft's input (iii) is not needed on this route: Lemma 9 uses the order-three Taylor bound on the member's pair ball, not a lattice Poincaré expansion.

**On item order.** ci-draft L35 says item 8 needs parts of items 1 and 9. After this text, item 9's part is Theorem 4.3 (conditional on [TI]); the rest of OSF-loc's needs are items 1, 4, 5. So OSF-loc should be placed after items 1, 4, 5 and after Theorem 4.3; it need not wait for H-SF.

## 8. Constant order (in1 rows 1–10 with Amendment 1)

IN1's rule (in1 L223): "A returned constant must precede every choice it bounds." Row 2 fixes \(L\) (with Amendment 1's floor \(L>L_0^\natural\)) and then "flat and averaging constants, \(c_0,c_2\), and the weak triple (1)". Row 4 fixes \(\kappa\ge\kappa_0^\natural(L)\). Row 5 fixes \(\bar\kappa\) and then \(M\). Row 8: "flow-error constants, including … \(C_f,C_v^{\rm flow}\) … precede \(X_0\)". Row 9 raises \(X_0\).

| Constant | Depends on | Fixed in row | Before \(\kappa\)? Independent of \(M,\bar\kappa\)? |
|---|---|---|---|
| \(c_0=\frac{11}{3\pi^2}\log L\) | \(L\) | 2 | yes; yes |
| \(c_2(L)=C_E(L)+C_R+C_M\) (Theorem V) | \(L\) only: the one-step analytic disc "depends only on \(L\)" (b-value L287) | 2 | yes; yes |
| \(b^0_l\), \(\mathcal A_l\) | the Gaussian; "contains no bare coupling" (b-value L302) | (values, not choices) | — |
| \(r_A,r_P,r_\Pi\) ([BG-u]), \(c_L,a_R\) ([R]), \(C_3\) | \(L\), local geometry | 3 | yes; yes (if [BG-u] holds as stated) |
| \(r_\flat\le r_P\) (NFE) | row 3 constants | 3 | yes; yes |
| \(m_h\) ([FP1] decay), \(\alpha_{\rm H}\) | \(L\) | 1–3 | yes; yes |
| \(c_a\) (member radius ratio, Lemma 4.4) | Tq0 radius table | 6 | after \(M\) |
| \(C_{\rm D}\) (rooted counts and moment sums, Lemma 4.4(3)) | \(\kappa-\kappa_D\), \(m_h\), and the factor \(M^4\) of Lemma R(iv) | 7 | after \(M\) |
| \(C_{\rm win},A_1\) (box) | rows 5–6 | 6 | after \(M\) |
| \(M_F\) ([B1♭] gas bound) | local dimension \((LM)^4\), \(c_L\) | 7 | after \(M\) |
| \(C_f\) (Thm 6.3), \(C_{\rm car}\), \(C_{\mathfrak n}\) (§6.4), \(C_v^{\rm flow}\) (Lemma 6.2) | the above | 8 | after \(M\), before \(X_0\) — as in1 row 8 allows |
| \(C_{\rm age},a=\frac32,b_{\rm age}=\alpha_{\rm H}\) (Cor. 4.6) | Lemma 9's \(C\), which keeps its \(M\)-dependence (cp12 L427) | 7 ("Fix \(E_N,C_E,C_{\rm rad},f_\nu\)") | after \(M\) |
| \(X_0\) floors: \(X_0\ge2c_5\), \(X_0\ge1+c_5\), \(x_k^{-1/2}<w_0/2\) (i.e. \(\theta^{1/2}\gtrsim(\log\theta)^{p_0}\)), \(C(LM)^4e^{-c_L\mathfrak b^2/16}\le\theta^{-1/2}\), \(g_k\mathfrak b\) small for NFE's induction, and \(\varsigma=\sup u\le\min(c_0/4,1)\) (Lemma 4) | all earlier | 9 | — |

**No cycle.** \(c_0,c_2\) read only \(L\). The row-3 radii read only \(L\) and geometry. Every row-7/8 constant reads rows \(\le6\). Every \(X_0\) floor reads rows \(\le8\), and each is a "sufficiently large \(X_0\)" condition because the left sides tend to zero. Lemma 4's \(\varsigma\le\min(c_0/4,1)\) is satisfiable because \(c_0\) is fixed in row 2 and \(u(X_0)\to0\).

**On the stated rule "fixed before \(\kappa\), independent of \(M\) and \(\bar\kappa\)".** IN1 requires this for \(c_0,c_2\) (row 2) and for H-M's early constants (row 4); both hold here for \(c_0,c_2\). IN1 does **not** require it for \(C_f,C_v^{\rm flow}\) (row 8, after \(M\)). The constants of Theorem 6.3 and Lemma 6.2 do depend on \(M\) (through \(M_F\), \(C_{\rm D}\), \(A_1\)); this is allowed and creates no cycle, since (11) is consumed only through \(\varsigma\) at row 9. If a consumer needs \(C_f\) before \(M\), Theorem 6.3 does not supply that.

## 9. Statements that frozen or distilled texts use wrongly or more strongly than supplied

1. **IN1's H-SF asks (11) of every class member, but the class does not carry a coefficient bound** (in1 L120–126 with the class at L217). Attack 1 of §6.4 shows that the class bounds (\(\|E^{(j)}\|\le E_0\) in sup norm on radius-\(\alpha_{0,j}\) domains) do not control the coefficients of carried members: the Cauchy bound is \(E_0\alpha_{0,j}^{-2}\asymp\theta_j(\log\theta_j)^{-2q}\). SA states the coefficient bound as a separate requirement (SA 6255–6256). I have not built a class member for which (11) fails, so this is not a counterexample. It means H-SF as stated may be unprovable from \(\mathfrak L_k\) alone. Proposed repair: add NFE to \(\mathfrak L_k\) (§6.5). in1 Theorem 11's "with unchanged constants" (L564) then needs NFE returned, which Theorem 6.4 does conditionally.
2. **cp12 L412** ("A coefficient extracted using a companion \(h_\infty\) is not automatically the Hessian coefficient for an actual finite-window response"). By Lemma 4.1, in an ordinary region the actual level-\(j\) response *is* \(\mathcal P_j\); there is no second response at level \(j\). The obstacle is the datum's regularity (D7 bullet 2), not the coefficient. Not an error in cp12; its Outstanding item is mislocated. Its other sentence, that (21) "does not close b4-step's actual-family stop", is superseded at the flat datum by Theorem 4.3 (conditional on [TI]).
3. **cp12 Lemma 9's "\(L_F\)"** (L449–455) must be read as \(\mathfrak h_\infty\ell_F\), including its bare gradient (Remark 4.2). With the bare affine pair, the appeal to Lemma 8 would need invariance under non-block-constant bare maps, which the actual members are not known to have (b2-extract L108–109). cp12's D7 bullet 2 phrase "the affine problem" supports the correct reading. Precision note, not an error.
4. **assembly-status §2.3** (L170): "Whether the NL1 step needs (ER7) elsewhere: **cannot tell**." On this route it does: Lemma 6.2 needs [ER8u] and Theorem 6.3/§6.4 need [BG-u], which is (ER7) at the flat datum.
5. **IN1 H-OL's Outstanding note** (L118) is correct as stated. Proposition 3.4 and Lemma 3.5 now supply the identification it asks for, modulo [G-ID] and NA. hma L557 still lists "companion/coefficient identifications" among the Outstanding vacuum-interface items; for the coefficient at the flat datum this is now supplied conditionally (Proposition 3.4), while the elimination-factor bounds and class/boundary filing remain.
6. **b2-extract Theorem P's (Id)** (L105) was a reading, not a proved identification. Lemma 3.1 proves it for the actual construction (CV, R3), near the flat datum.

I found no statement in a frozen text that is false.

## 10. Source checks

| Lines | What I read |
|---|---|
| SA 3986–4001 | B3: \(b_j=b_j^0+f_j+q_j\), \(|f_j|\le Cx_{j-1}^{-1/2}(\log x_{j-1})^p\), \(|q_j|\le Cx_{j-1}^{-(\kappa_0-4)/2}\); "A continuum perturbative coefficient quoted without this comparison does not discharge this obligation." |
| SA 5625–5650 | residual gauge "equals 1 at all nodes"; \(\mathcal M\) is "the symmetric contour average"; (R3). |
| SA 5651–5661 | the background input is "a regular critical orbit … The representatives, gauge, analytic domain and transport under local charts are included in this input. Uniqueness, existence and uniform estimates for these maps are separate background theorems." |
| SA 6245–6256 | R16-type requirements, with "Require, for fixed constants"; the separate coefficient bounds \(|b^{\rm m}_j|\le C_b\bar g^{\kappa_0-4}\), \(|b^{\rm u}_j-b^0_j|\le C_b\bar g(\log\theta)^{\mathfrak p_0}\). |
| SA 7943–7960 | "The exact finite map": blocks \(B(y)\), paths \(\mathcal G(y,x)\) "which complete one coordinate displacement before starting the next". |
| SA 19561–19568 | the pointed cancellation's hypotheses (quoted in §1.4). |
| SA 19664–19670 | "These summations do not prove (OSF3). That estimate contains the renormalisation assertion …". |
| SA 5883–5898 | companions; (R14) "for every lattice isometry \(r\), including unit translations". |
| SA 21565–21579 | (RF37); "Threshold and large-field changes contribute at most \(C\theta_k^{-(\kappa_0-4)/2}\) per step". |
| SA 22881 | "the increment \(b_{k+1}\) is holomorphic in the shifts … On these discs its non-constant part, less the remainder, is bounded by \(Cg_k(\log x_k)^{\mathfrak p_0}\)" — SA's own dial-type argument, for the coupling shifts of earlier levels; Theorem 6.3 uses a dial on the current fluctuation instead. |
| library | in1 L1–143, 216–238, 373–400, 555–699; ym4-assembly L254–290; cp12 L346–462, 652–690; b4-step L449–630; b4-induction L58–265; b2-extract L35–150, 185–211; prefactor-loc L36–112, 202–232; prefactor.md L54–70, 100–107; b-value L1–324; descent L40–66, 285–316; hma L55–75, 255–280, 551–600; hm L43–46; st1-r4 L38–46, 80–92; ci-draft L1–125, 350–372, 548–606; assembly-status (whole). |

## Result

**Proved here** (as implications from the named inputs; by hand; not checked by another model):

- Lemma 3.1: the actual CV background is the multi-level augmented branch \(u_{0,k}\) read by prefactor-loc and b2-extract, near the flat datum (so b2-extract's (Id) holds).
- Lemma 3.2: at real block-axial references the Y3 and absolute gauge Hessians coincide; the gauge-direction coordinates are background-independent; the orbit normalizer is an exact constant; the soft-gauge Gaussian equals a constant times the delta-gauge Gaussian with its Faddeev–Popov Jacobian.
- Proposition 3.4: the actual companion normalizer's coefficient equals \(b[\Phi_l]\), independent of gauge form and weight (given [G-ID] and the assignment rule NA).
- Lemma 3.5 (localized-to-bulk) and Proposition 3.6 (\(b^0_l=\mathcal A_l-\mathcal A_{l-1}\), \(\mathcal A_0=0\), exactly).
- §3.5: a check of b-value Theorem V (assembly, leading coefficient \(\frac{88}{3}I_2\to\frac{11}{6\pi^2}\log\frac1z\to kc_0\), normalization and sign against IN1, finite-rank and Schatten steps); first failing step none found; estimates (4)–(9), (11)–(12) read, not re-derived.
- Lemma 4.1: in an ordinary region the actual level-\(j\) pair is \(\mathcal P_j(B_j)\) exactly.
- Theorem 4.3: the own-coefficient pointed cancellation (b4-step (20), cp12 (21)) for the actual re-pointed members, at the flat datum, conditional on [TI].
- Lemma 4.4: cp12 D7 bullets 3–4 for actual members, given [ER8u] and [FP1].
- Corollary 4.6: IN1 (13)'s age clause with \(a=\frac32\), \(b_{\rm age}=\alpha_{\rm H}\), conditional on D7.
- Proposition 6.1, Lemma 6.2 (the \(\theta^{-(\kappa_0-4)/2}\) term, given [ER8u]), Theorem 6.3 (the \(\theta^{-1/2}(\log\theta)^{p_0}\) term for the fresh part, by a coupling-dial Schwarz argument, given [BG-u], [R], [B1♭]).
- §6.4 Attacks 2–3: (11)'s carried term and the near-flat extension NFE, by induction, conditional on [BG-u] and D7♭ (Theorem 6.4).
- §8: the constant order, with no cycle; \(c_0,c_2\) depend on \(L\) only.

**First remaining Outstanding statement** (item 9's order: OL-a…g, then (20), then (11)): the carried term of (11), SF-car, reduced by Attack 3 to **[BG-u]** — a radius \(r_A>0\), fixed after \(L\) and before \(\kappa\), independent of depth, \(M\), \(\bar\kappa\), on which the k-fold critical branch (and the step's pivot parametrization) is holomorphic and uniformly bounded around the flat datum — plus D7♭, which follows from [BG-u] and [FP1] by a Cauchy step not written here. The three attacks and their exact failures are in §6.4: (1) Cauchy on the class domain loses \(\alpha_{0,j}^{-2}\asymp\theta_j(\log\theta_j)^{-2q}\); (2) the dial argument needs NFE, which no class or frozen text carries; (3) the induction of NFE needs [BG-u], while the checked A1 (9.2) radius shrinks with depth (b2-extract L185) and b-value (4) is uniform only for constant-flux jets.

**Other Outstanding items, named:** [TI] for the actual members (b4-induction's ordered implication, under BX⁺, UR, YA, LOC); [G-ID] (hma Theorem 8, under PH1–PH4); [ER8u]; D7 bullets 1–2 at actual curved/layered data (items 1, 4, 5); [B1♭]'s fresh-type UM1 inputs (ci-draft §5, unrefereed); formation, (12), (13) first clause and structure (items 6, 8); NL1(1) B1 for the actual gas, whose old-origin type is OSF-loc.

**Supplied to OSF-loc:** the correct counterterm and (given [TI]) covariance of the pointed Hessian; D7 bullets 3–4; the \(L_F\) reading; the age function. Not supplied: background regularity in the window and uniform membership (items 1, 4, 5).

**Statements used wrongly or more strongly than supplied:** §9 items 1–6; none is a false statement in a frozen text. The substantive one is item 1: IN1's class \(\mathfrak L_k\) carries no coefficient bound, so H-SF's (11) cannot follow from the class by Cauchy; NFE is proposed as a class amendment (not applied).

This is research text. It grants no status. Not yet checked by another model.
