# CN1RG. The tree-leaf RG

## 0. Status

**Pass 2; not refereed or frozen.** This is a mathematical analysis of the supplied model M″, not a derivation of a physical dynamics or of a common cone. Pass 1 is `CN1RG_DRAFT.md`. A fresh referee must check this file.

**Proved, within the stated hypotheses.** The fixed-background Grassmann step and composition; the small-field inverse and decay argument for the single-path averaging scheme, subject to the finite-volume qualifications below; the blocked Hermitian-part identity and its real-background consequences; the exact zero-mode correspondence; a corrected O(η) numerical-range estimate; the loop-holonomy bound; the near-null block-average estimate; and the conditional determinant consequence of LF. Proofs follow. These are author-side checks, not independent audit results.

**GAP.** The proposed symmetry-restored census is not established: averages of unit phases are generally not unit phases, and may vanish. Thus the projection identity and inherited inverse bounds used in its proof fail. The uncorrected fine-lattice test vector also misses the antiperiodic time boundary; a corrected estimate follows. The rescaled small-field corollaries need the divisibility of the rescaled torus, made explicit below. The large-field geometric-resolvent statement needs an explicit link-support convention; its abstract corrected form is given below. The claimed large-field threshold and the inference from exact to near-zero modes are not established. B1 for the full RG, the marginal census, B2 locality and (W) remain open.

**Open by name.** LF; (T3); S-small; M1; UB″; R1″-MOD[d]; R1″-MOD; R1-MOD; LIMIT; OBS; C1; the framework bridges in `CN1MOD.md` §5. (T1) below is narrower than B1: it concerns a specified fixed-background kernel, not a full invariant RG domain. (T2), the complete census, is open. These gaps do not establish failure of (W).

**Provenance.** Pass 2: Codex, model `gpt-6.1-terra`; effort and session id: see run log. Draft SHA-256 `8c1e08ebb0134c12a268f6fabc3cb63b8933f81c4d4f955e9db5fb4f11510cb8`. Context SHA-256: `prior/CN1RG.md` `44fec027367c000e300fc20906945213f45d25f623adffb0cf505fc001e3eb98`; `CN1_TREE.md` `623a64bcac6d9e3f7361705c14363facb4c21a9d380333c822bb829ad8a6176e`; `CN1MOD.md` `45cf11acd8714419f31f761d7b2e780e097f4ed2dc791e28d862826a0d80c51e`; `CN1.md` `d53b6ef39a9569435bb2c250790aa1cc6976e9308b6e8eeb72f46c739ee772ca`; `TOE_ASSEMBLY.md` `f443399e659c5411177e1735449c292e0465bee12f8d177193a44ead08fdd8b5`. Revisions stated in the draft are its historical report, not verified current branches. Scratch scripts reported by pass 1 were absent at the recorded `/tmp` paths in this session; their numbers below were not reproduced.

**Prior results.** `CN1.md` Theorems 1 and 3 and its integrable-forcing closure already prove conditional continuous-flow consensus; Proposition 4 gives a persistent-source counterexample. `CN1MOD.md` Theorems 1–3 already give conditional discrete contraction and UB″ ⇒ R1″-MOD[d], under their stated hypotheses. Neither constructs the RG. The prior digest also identifies the bounded high-mass one-step polymer result in `docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` and the conditional one-loop calculation in `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md`; neither supplies this massless invariant RG. The digest's quartet warning is in `docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md`. The related Combes–Thomas argument for a different gapped operator is in `docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`. These references do not import a proof of the present estimates.

## 1. Definitions inferred by the distiller

All definitions in this section are proposed mathematical specifications for the supplied model, not adopted readings or physical axioms. In particular, the chosen path, blocking strength and complex domain are not consequences of M″ alone.

**Targets.** (T1) is a scale- and volume-uniform inverse and exponential decay for the fixed-background fine operator on an explicit gauge-invariant complex small-field domain. (T2) is the full relevant/marginal coordinate census for a symmetry-preserving covariant scheme. (T3) is an exact full step and an invariant real domain giving the tree's gate
\[
x_{k+1}=x_k+(\log L)G_k\mathcal F(x_k)+r_{k,N},\quad b_-\le G_{k+1}^{-1}-G_k^{-1}\le b_+,\quad
\|r_{k,N}\|_\infty\le C(G_k^2+G_ke^{-\beta k}+G_ke^{-\beta(N-k)}).
\]
Constants must be uniform in volume and N; the action norm must control all other marginal data. The definitions are proposed specifications; pass 1's four checks (target specificity, closedness, downstream-premise test, unnecessary structure) returned P/P/P/P for these targets and the small-field domain, and P/P/C/P for the census scheme. The third census check is conditional on an observable bridge. These are pass-1 judgments, not adoption. The invalid averaging construction independently prevents acceptance of that census proof.

**Lattices, fields, paths, operators and small-field domain.** The formulas below specify them. The complex left inverse `tilde Q` is algebraic and need not be the Hilbert adjoint; it is the adjoint for the single unit-modulus path at real backgrounds. A link is outside a region only when both its endpoints and the whole averaging path used in its support avoid that region; stronger support assumptions are stated where needed. The antiperiodic time sign is a fixed flat link factor; gauge transformations are periodic. Matrix elements use the weighted fine-lattice inner product. Distances use torus ℓ∞ distance.

### 2.1 Lattices, fields, links

Fix \(d=4\), an integer \(L\ge2\), a scale \(k\ge1\), and \(\eta=L^{-k}\). Lengths are in units of \(L^k\) original lattice spacings ("rescaled units"). The fine lattice is \(\Lambda_\eta=(\eta\mathbb Z/T\mathbb Z)^4\) and the unit lattice is \(\Lambda_1=(\mathbb Z/T\mathbb Z)^4\), with an integer side \(T\) (the original torus has side \(TL^k\)). The unit cube of \(y\in\Lambda_1\) is \(B_y=y+\eta\{0,\dots,L^k-1\}^4\). Fermion fields are \(f:\Lambda_\eta\to\mathbb C^4\) with \(\langle f,g\rangle=\eta^4\sum_xf(x)^*g(x)\); unit-lattice fields \(\phi:\Lambda_1\to\mathbb C^4\) have \(\langle\phi,\chi\rangle=\sum_y\phi(y)^*\chi(y)\). The \(\gamma_\mu\) are Hermitian with \(\{\gamma_\mu,\gamma_\nu\}=2\delta_{\mu\nu}\); so \(\tfrac12(1\pm\gamma_\mu)\) are orthogonal projections.

A **background** is a family of link variables \(U_\mu(x)=e^{i\theta_\mu(x)}\), \(\theta_\mu(x)\in\mathbb C\), on the fine links \((x,x+\eta e_\mu)\). It is **real** when every \(\theta_\mu(x)\) is real. Antiperiodic time is built in: the links \((x,x+\eta e_0)\) with \(x_0=T-\eta\) carry an extra factor \(-1\) inside \(U_0(x)\). In M″, \(U_\mu(x)=e^{ieqA_\mu(x)}\) on the original lattice, so \(\theta=eqA\).

The **rescaled Wilson operator** with weights \(w=(1,v,v,v)\), \(v>0\), is
\[
(D_Uf)(x)=\frac1\eta\sum_\mu w_\mu\Bigl[f(x)-\tfrac12(1-\gamma_\mu)U_\mu(x)f(x+\eta e_\mu)-\tfrac12(1+\gamma_\mu)U_\mu(x-\eta e_\mu)^{-1}f(x-\eta e_\mu)\Bigr].
\]
With \(\psi_\eta(x)=\eta^{-3/2}\psi(x/\eta)\) and \(\bar m=\mu/\eta=L^k\mu\), the M″ action \(\sum_x\bar\psi(\mu+D)\psi\) of `CN1MOD.md` §1 equals \(\langle\bar\psi_\eta,(D_U+\bar m)\psi_\eta\rangle\) (Grassmann pairing with the measure \(\eta^4\)). For real \(U\), \(U^{-1}=\bar U\), and \(D_U\) is the operator of `CN1MOD.md` §1. Write \(w_{\min}=\min(1,v)\), \(w_{\max}=\max(1,v)\). Fix once and for all a compact speed interval \(v\in[v_-,v_+]\subset(0,\infty)\); all constants below depend on \(v_\pm\) only through \(w_{\min}\) and \(w_{\max}\).

### 2.2 Gauge-covariant averaging

A **single averaging step** from a lattice of spacing \(\lambda\) to spacing \(L\lambda\) averages over \(B^\lambda(u)=u+\lambda\{0,\dots,L-1\}^4\). The transport from \(x\in B^\lambda(u)\) to \(u\) runs along the **monotone path** that goes from \(u\) by fine links first in direction 1, then 2, 3, 4, and \(V(u,x)\) is the product of the \(U_\mu(z)\) along it, in path order from \(u\). (Each \(U_\mu(z)\) transports from \(z+\eta e_\mu\) to \(z\).) The **k-step averaging** \(Q_k\) is the composition of the steps from spacing \(\eta\) to spacing 1. Its transport \(V_k(y,x)\), \(x\in B_y\), is the product along the concatenated path, which is monotone in every coordinate, stays in \(B_y\), and has length \(|x-y|_1\le4\). Set
\[
(Q_kf)(y)=\eta^4\!\!\sum_{x\in B_y}\!V_k(y,x)f(x),\qquad (\tilde Q_k\phi)(x)=V_k(y,x)^{-1}\phi(y)\ (x\in B_y),\qquad P_k=\tilde Q_kQ_k .
\]
For a next step assume in addition that \(L\mid T\), so the unit lattice has a partition into \(L\)-blocks. On the unit lattice, \(Q\) is one averaging step from spacing 1 to spacing \(L\), with its transports also along fine links, and \(P=\tilde QQ\). Then \(Q_{k+1}:=QQ_k\) is the \((k+1)\)-step averaging viewed at scale \(k\).

**Lemma 2.1 (averaging).** (i) \(Q_k\tilde Q_k=1\), \(P_k^2=P_k\), and the same for \(Q,P\). (ii) If \(U\) is real, \(\tilde Q_k=Q_k^*\), \(\tilde Q=Q^*\), and \(P_k,P\) are orthogonal projections. (iii) For \(g:\Lambda_\eta\to U(1)\) put \(U^g_\mu(x)=g(x)U_\mu(x)g(x+\eta e_\mu)^{-1}\), let \(G\) multiply fine fields by \(g\) and \(G_1\) multiply unit-lattice fields by \(g|_{\Lambda_1}\). Then \(D_{U^g}=GD_UG^{-1}\), \(Q_k(U^g)=G_1Q_k(U)G^{-1}\), \(\tilde Q_k(U^g)=G\tilde Q_k(U)G_1^{-1}\), \(P_k(U^g)=GP_k(U)G^{-1}\).

*Proof.* (i) \((Q_k\tilde Q_k\phi)(y)=\eta^4\sum_{x\in B_y}V_kV_k^{-1}\phi(y)=\eta^4L^{4k}\phi(y)=\phi(y)\). Then \(P_k^2=\tilde Q_k(Q_k\tilde Q_k)Q_k=P_k\). (ii) For \(|V_k|=1\), \(\langle\phi,Q_kf\rangle=\eta^4\sum_y\sum_{x\in B_y}\phi(y)^*V_kf(x)=\langle\tilde Q_k\phi,f\rangle\). An idempotent equal to its adjoint is an orthogonal projection. (iii) Each hop picks up \(g(x)\cdot g(x+\eta e_\mu)^{-1}\) and a path product telescopes to \(g(y)V_kg(x)^{-1}\). □

### 2.3 The operators of one exact step

Fix \(a>0\) and \(a_k=a(1-L^{-1})/(1-L^{-k})\in[a(1-L^{-1}),a]\). (This is the parameter that the composition of single Gaussian steps of strength \(a\) produces, as Lemma 2.3 shows; it is Dimock's \(b_k\) of [D17] eq. (18).) Put
\[
X_k=D_U+\bar m+a_kP_k,\qquad S_k=X_k^{-1},\qquad H_k=a_kS_k\tilde Q_k,\qquad D_k=a_k-a_k^2Q_kS_k\tilde Q_k,\qquad \Gamma_k=\Bigl(D_k+\frac aLP\Bigr)^{-1},
\]
whenever the inverses exist. \(D_k\) and \(\Gamma_k\) act on unit-lattice fields; \(H_k\) maps them to fine fields. By Lemma 2.1(iii), \(X_k(U^g)=GX_k(U)G^{-1}\) and \(D_k(U^g)=G_1D_k(U)G_1^{-1}\).

**Lemma 2.2 (exact fermion step at a fixed background).** Let \(X_k\) be invertible. For Grassmann fields \(\psi,\bar\psi\) on \(\Lambda_\eta\) and \(\Psi,\bar\Psi\) on \(\Lambda_1\),
\[
\int\exp\Bigl(-\langle\bar\psi,(D_U+\bar m)\psi\rangle-a_k\bigl\langle\bar\Psi-\bar\psi\tilde Q_k,\ \Psi-Q_k\psi\bigr\rangle\Bigr)D\bar\psi D\psi=\det X_k\cdot\exp\bigl(-\langle\bar\Psi,D_k\Psi\rangle\bigr),
\]
where \(\bar\psi\tilde Q_k\) denotes the unit-lattice row field \(y\mapsto\eta^4\sum_{x\in B_y}\bar\psi(x)V_k(y,x)^{-1}\).

*Proof.* The exponent is \(-\langle\bar\psi,X_k\psi\rangle+a_k\langle\bar\Psi,Q_k\psi\rangle+a_k\langle\bar\psi,\tilde Q_k\Psi\rangle-a_k\langle\bar\Psi,\Psi\rangle\). Translate \(\psi=W+H_k\Psi\), \(\bar\psi=\bar W+a_k\bar\Psi Q_kS_k\); Berezin integration is translation invariant. Since \(X_kH_k=a_k\tilde Q_k\) and \(a_kQ_kS_kX_k=a_kQ_k\), the cross terms cancel and the exponent becomes \(-\langle\bar W,X_kW\rangle-\langle\bar\Psi,(a_k-a_k^2Q_kS_k\tilde Q_k)\Psi\rangle\). Finally \(\int e^{-\langle\bar W,X_kW\rangle}=\det X_k\) in the normalization of the Berezin measure that absorbs \(\eta^4\). □

**Lemma 2.3 (composition).** Let \(R=(a_k+\tfrac aLP)^{-1}=a_k^{-1}(1-P)+(a_k+\tfrac aL)^{-1}P\), \(a'=a_k\frac aL/(a_k+\frac aL)\), and \(X'=D_U+\bar m+a'\tilde Q_kPQ_k\) (the \((k+1)\)-step operator at scale \(k\)). If \(X_k\) and \(X'\) are invertible, then \(D_k+\frac aLP\) is invertible and
\[
\Gamma_k=R+R\,a_kQ_k\,X'^{-1}\tilde Q_k\,a_k R,\tag{2.1}
\]
\[
\det X_k\cdot\det\Bigl(D_k+\frac aLP\Bigr)=\det\Bigl(a_k+\frac aLP\Bigr)\det X',\tag{2.2}
\]
\[
\frac aL-\Bigl(\frac aL\Bigr)^2Q\,\Gamma_k\,\tilde Q=a'-a'^2\,Q_{k+1}X'^{-1}\tilde Q_{k+1},\qquad \tilde Q_{k+1}:=\tilde Q_k\tilde Q.\tag{2.3}
\]
After rescaling by \(L\), \(X'\) is \(L^{-1}\) times the operator \(X_{k+1}\) at spacing \(\eta/L\) with parameter \(La'=a_{k+1}\), and (2.3) is \(D_{k+1}\). So one exact step maps \((\det X_k,D_k)\) to \((\det X_{k+1},D_{k+1})\) up to the explicit constant \(\det(a_k+\frac aLP)\) and the rescaling.

*Proof.* Consider the block operator on (fine field, unit-lattice field)
\[
M=\begin{pmatrix}X_k&-a_k\tilde Q_k\\-a_kQ_k&a_k+\frac aLP\end{pmatrix}.
\]
Its Schur complement with respect to the first block is \(a_k+\frac aLP-a_k^2Q_kS_k\tilde Q_k=D_k+\frac aLP\). With respect to the second block it is \(X_k-a_k^2\tilde Q_kRQ_k=D_U+\bar m+\tilde Q_k(a_k-a_k^2R)Q_k\). Since \(P^2=P\), \(a_k-a_k^2R=a'P\), so this complement is \(X'\). Both complements are invertible, so \(M\) is, and the lower-right block of \(M^{-1}\) equals both \((D_k+\frac aLP)^{-1}\) and the right side of (2.1). The two Schur factorizations of \(\det M\) give (2.2). For (2.3), the Gaussian integral over (fine, unit-lattice) fields with the next step's term \(\frac aL\langle\bar\Psi'-\bar\Psi\tilde Q,\Psi'-Q\Psi\rangle\) gives the kernel \(\frac aL-(\frac aL)^2Q(M^{-1})_{22}\tilde Q\) for \(\Psi'\). Insert (2.1): \(QP=Q\) and \(Q(1-P)=0\) give \(QR=(a_k+\frac aL)^{-1}Q\), and the scalars combine to \(a'\) and \(a'^2\). The rescaling statement is the substitution \(x\mapsto x/L\), under which \(D_U\) gains a factor \(L\) and \(1/a_{k+1}=1/(La_k)+1/a\) holds for \(a_{k+1}=La'\). □

Lemmas 2.2 and 2.3 are the fermionic half of one exact blocking step: at every fixed background, the step is a Gaussian Grassmann integral with explicit kernel and determinant. They hold for any background for which the inverses exist. The bounds are §§3-5.

### 3.1 Domain and statement

For a background \(U=e^{i\theta}\) write \(\theta=\theta_R+i\theta_I\) and \(U_R=e^{i\theta_R}\). For a plaquette \(p\), \(\varphi_p\in(-\pi,\pi]\) is the oriented sum of \(\theta_R\) around \(p\), reduced mod \(2\pi\). (The antiperiodic signs enter a plaquette twice with opposite orientation, so they cancel.) The **small-field domain** is
\[
\mathcal U_k(\varepsilon,\delta)=\bigl\{U:\ |\varphi_p|\le\varepsilon\eta^2\ \text{for every plaquette},\ \ |\theta_I|\le\delta\eta\ \text{on every link}\bigr\}.
\]
In M″ terms (\(\theta=eqA\), rescaled field strength \(F=dA/\eta^2\), rescaled \(A/\eta\)): \(|eqF|\le\varepsilon\) and \(|eq\operatorname{Im}A|\le\delta\) in rescaled units. **The domain is invariant under real gauge transformations** \(\theta_\mu(x)\mapsto\theta_\mu(x)+\chi(x)-\chi(x+\eta e_\mu)\): plaquette sums and \(\theta_I\) do not change. This is the form of "compatible gauge transitions" used here: the domain is defined gauge-invariantly, and the proof below only evaluates gauge-invariant quadratic forms in local gauges. No transition function between local gauges ever enters.

**Theorem 1 (uniform inverse and decay).** Fix \(a>0\), \([v_-,v_+]\subset(0,\infty)\), and set \(\kappa=w_{\min}/4\), \(a_-=a/2\), \(a_+=a\), \(s_1=\min(a_-/4,\ \kappa^2/(16a_+),\ 0.3\kappa)\), \(s_0=s_1/2\). There are an explicit integer \(M\ge2\) and explicit \(\varepsilon_0,\delta_0,\mu_0,\alpha_0>0\), depending only on \(a,w_{\min},w_{\max}\), such that for every \(L\ge2\), every \(k\ge1\), every torus side \(T\ge6M\) that is a multiple of \(M\), every \(U\in\mathcal U_k(\varepsilon_0,\delta_0)\) and every \(\bar m\ge-\mu_0\):

1. \(X_k(U)\) is invertible and \(\|X_k(U)f\|\ge\tfrac{s_0}2\|f\|\), \(\|X_k(U)^*f\|\ge\tfrac{s_0}2\|f\|\); for real \(U\) the constant is \(s_0\).
2. For all sets \(\Delta,\Delta'\subset\Lambda_\eta\), \(\|1_\Delta X_k(U)^{-1}1_{\Delta'}\|\le\frac4{s_0}e^{-\alpha_0\operatorname{dist}_\infty(\Delta,\Delta')}\).
3. \(\theta\mapsto X_k(e^{i\theta})^{-1}\) is holomorphic on the interior of the domain, and \(X_k(U^g)^{-1}=GX_k(U)^{-1}G^{-1}\) for real gauge transformations.

For uniformity in \(v\), use \(w_{\min}=\min(1,v_-)\) and \(w_{\max}=\max(1,v_+)\) in these constants. All constants are independent of \(k\), \(L\), \(T\), \(v\in[v_-,v_+]\) and \(U\). The proof is Lemmas 3.1-3.8.

### 3.2 The lemmas

**Lemma 3.1 (the Wilson term).** For real \(U\), with \((\delta^U_\mu f)(x)=\eta^{-1}(f(x)-U_\mu(x)f(x+\eta e_\mu))\) and \(\|\nabla_Uf\|^2=\sum_\mu\|\delta^U_\mu f\|^2\),
\[
\operatorname{Re}D_U:=\tfrac12(D_U+D_U^*)=\tfrac\eta2\sum_\mu w_\mu(\delta^U_\mu)^*\delta^U_\mu\ \ge0 .
\]
*Proof.* Let \((T_\mu f)(x)=U_\mu(x)f(x+\eta e_\mu)\); it is unitary and \(T_\mu^*f(x)=U_\mu(x-\eta e_\mu)^{-1}f(x-\eta e_\mu)\). So \(D_U=\eta^{-1}\sum_\mu w_\mu[1-\tfrac12(T_\mu+T_\mu^*)+\tfrac12\gamma_\mu(T_\mu-T_\mu^*)]\). \(\gamma_\mu\) commutes with \(T_\mu\), so the last term is anti-Hermitian. Finally \(\eta^2(\delta^U_\mu)^*\delta^U_\mu=(1-T_\mu)^*(1-T_\mu)=2-T_\mu-T_\mu^*\). □

**Lemma 3.2 (free lower bound).** On \(\ell^2(\eta\mathbb Z^4;\mathbb C^4)\) with \(U\equiv1\), \(\|D_1h\|^2\ge\frac{w_{\min}^2}2\|\nabla_1h\|^2\).

*Proof.* The symbol of \(D_1\) is \(\eta^{-1}(m(p)+i\sum_\mu w_\mu\gamma_\mu\sin\eta p_\mu)\) with \(m(p)=\sum_\mu w_\mu s_\mu\), \(s_\mu=1-\cos\eta p_\mu\in[0,2]\). By the anticommutation relations its modulus squared is \(\eta^{-2}(m^2+\sum_\mu w_\mu^2\sin^2\eta p_\mu)\). The symbol of \((\delta_\mu)^*\delta_\mu\) is \(2\eta^{-2}s_\mu\). If every \(s_\mu\le1\), \(\sum w_\mu^2s_\mu(2-s_\mu)\ge w_{\min}^2\sum s_\mu\). If some \(s_\nu>1\), then \(\sum s_\mu>1\) and \(m^2\ge w_{\min}^2(\sum s_\mu)^2\ge w_{\min}^2\sum s_\mu\). In both cases the symbol of \(D_1^*D_1\) is at least \(\frac{w_{\min}^2}2\cdot2\eta^{-2}\sum s_\mu\). Plancherel. □

**Lemma 3.3 (Poincaré on a unit cube).** For \(g:B_y\to\mathbb C^4\) with mean \(\bar g=\eta^4\sum_{B_y}g\), \(\ \eta^4\sum_{B_y}|g-\bar g|^2\le4\,\eta^4\sum_{\ell\subset B_y}\eta^{-2}|g(x_\ell)-g(x_\ell+\eta e_{\mu_\ell})|^2\).

*Proof.* Let \(n=L^k=1/\eta\). By Jensen, \(|g(x)-\bar g|^2\le n^{-4}\sum_{x'}|g(x)-g(x')|^2\). Join \(x\) to \(x'\) by the rectilinear path that changes coordinate 1 first, then 2, 3, 4; it has at most \(4n\) links, so Cauchy-Schwarz gives \(|g(x)-g(x')|^2\le4n\sum_{\ell\in\text{path}}|\delta_\ell g|^2\). A link in direction \(\mu\) lies on the paths of at most \(n^{\mu-1}\cdot n^{4-\mu}\cdot n^2=n^5\) ordered pairs (free: \(x_1..x_{\mu-1}\), \(x'_{\mu+1}..x'_4\), and the pair \(x_\mu,x'_\mu\)). So \(\sum_x|g-\bar g|^2\le4n^2\sum_\ell|\delta_\ell g|^2\). Multiply by \(\eta^4=n^{-4}\). □

**Lemma 3.4 (axial gauge on a cube).** Let \(C\) be a lattice cube of side \(s\le T/2\) and \(U\) real with \(|\varphi_p|\le\varepsilon\eta^2\) on the plaquettes of \(C\), and \(3s\varepsilon\eta<\pi\). There is \(g:C\to U(1)\) with \(U^g_\mu(x)=e^{i\theta'_\mu(x)}\), \(|\theta'_\mu(x)|\le3s\varepsilon\eta\), on every link of \(C\). So the transport of \(U^g\) along any path of \(n\) links in \(C\) has angle at most \(3s\varepsilon\eta\,n\).

*Proof.* Root \(c\) at a corner. The axial tree is the set of \(\mu\)-links \((x,x+\eta e_\mu)\) with \(x_\nu=c_\nu\) for all \(\nu>\mu\); its path from \(c\) to \(x\) moves in direction 1, then 2, 3, 4. Choose \(g\) so that \(U^g=1\) on tree links. For a non-tree \(\mu\)-link at \(x\), \(U^g\) equals the holonomy of the loop: tree path to \(x\), the link, tree path back from \(x+\eta e_\mu\). The two tree paths share their legs in directions below \(\mu\), and their legs in directions above \(\mu\) are translates by \(\eta e_\mu\). So the loop bounds a ribbon of at most \(3s/\eta\) plaquettes. Lattice Stokes for an abelian field: the holonomy is the product of the plaquette variables of the ribbon. Take \(\theta'\) to be the sum of the \(\varphi_p\). □

**Lemma 3.5 (IMS localization with local gauges).** Let \(U\) be real with \(|\varphi_p|\le\varepsilon\eta^2\) everywhere, \(M\ge2\) dividing \(T\), \(T\ge6M\), and \(9M\varepsilon\le1\). Then for every \(f\)
\[
\|D_Uf\|^2\ge\frac{w_{\min}^2}4\|\nabla_Uf\|^2-E\|f\|^2,\qquad E=\frac{K_{I}}{M^2}+7225\,w_{\max}^2M^2\varepsilon^2,\quad K_I=3301\pi^2w_{\max}^2 .
\]
*Proof.* *Partition.* In one dimension let \(\phi_j(t)=\sin(\pi(t-(j-1)M)/2M)\) on \([(j-1)M,jM]\), \(\cos(\pi(t-jM)/2M)\) on \([jM,(j+1)M]\), zero elsewhere; then \(\sum_j\phi_j^2=1\) and \(|\phi_j(t)-\phi_j(t')|\le\frac\pi{2M}|t-t'|\). Put \(\chi_J(x)=\prod_\mu\phi_{J_\mu}(x_\mu)\). So \(\sum_J\chi_J^2=1\), \(\operatorname{supp}\chi_J\subset C_J\) (a cube of side \(2M\)), \(|\chi_J(x)-\chi_J(x')|\le\frac\pi{2M}|x-x'|_1\), and every point lies in at most \(3^4=81\) of the cubes enlarged by \(3\eta\).

*IMS identity.* For any operator \(Z\), \(\sum_J[\chi_J,[\chi_J,Z^*Z]]=2Z^*Z-2\sum_J\chi_JZ^*Z\chi_J\), so \(\sum_J\|Z\chi_Jf\|^2=\langle f,Z^*Zf\rangle-\frac12\sum_J\langle f,[\chi_J,[\chi_J,Z^*Z]]f\rangle\). Also \([\chi,Z^*]=-[\chi,Z]^*\) gives \(\langle f,[\chi,[\chi,Z^*Z]]f\rangle=2\operatorname{Re}\langle[\chi,[\chi,Z]]f,Zf\rangle-2\|[\chi,Z]f\|^2\).

*Commutator sizes.* \(\|D_U\|\le12w_{\max}/\eta\). A hop \(T\) has \(\|[\chi_J,T]\|\le\frac{\pi\eta}{2M}\) and \(\|[\chi_J,[\chi_J,T]]\|\le(\frac{\pi\eta}{2M})^2\). Hence \(\|[\chi_J,D_U]\|\le\frac{4\pi w_{\max}}M\) and \(\|[\chi_J,[\chi_J,D_U]]\|\le\frac{2\pi^2w_{\max}\eta}{M^2}\). These commutators act only within the \(\eta\)-neighbourhood of \(C_J\). With the overlap count 81,
\(\frac12\sum_J|\langle f,[\chi_J,[\chi_J,D_U^*D_U]]f\rangle|\le81(24\pi^2+16\pi^2)\frac{w_{\max}^2}{M^2}\|f\|^2\). The same computation for \(\delta^U_\mu\) (\(\|\delta_\mu\|\le2/\eta\)) gives \(\frac12\sum_J|\langle f,[\chi_J,[\chi_J,\nabla_U^*\nabla_U]]f\rangle|\le\frac{243\pi^2}{M^2}\|f\|^2\).

*Local step.* Let \(g_J\) be the axial gauge of Lemma 3.4 on the cube \(C_J^+\) (the \(\eta\)-neighbourhood of \(C_J\), side \(s\le3M\)), extended by 1. Put \(h=g_J\chi_Jf\), supported in \(C_J\). \(D_U\chi_Jf\) uses only links of \(C_J^+\), on which \(|U^{g_J}-1|\le9M\varepsilon\eta\). So, with Lemma 2.1(iii), \(\|D_U\chi_Jf\|=\|D_{U^{g_J}}h\|\ge\|D_1h\|-72w_{\max}M\varepsilon\|h\|\), and \(\|\nabla_1h\|\ge\|\nabla_{U^{g_J}}h\|-18M\varepsilon\|h\|=\|\nabla_U\chi_Jf\|-18M\varepsilon\|h\|\). Lemma 3.2 (with \(h\) extended by zero to \(\eta\mathbb Z^4\)) then gives \(\|D_U\chi_Jf\|\ge\frac{w_{\min}}{\sqrt2}\|\nabla_U\chi_Jf\|-85w_{\max}M\varepsilon\|\chi_Jf\|\). Use \((\alpha-\beta)_+^2\ge\alpha^2/2-\beta^2\): \(\|D_U\chi_Jf\|^2\ge\frac{w_{\min}^2}4\|\nabla_U\chi_Jf\|^2-7225w_{\max}^2M^2\varepsilon^2\|\chi_Jf\|^2\).

*Sum.* Sum over \(J\), use \(\sum_J\|\chi_Jf\|^2=\|f\|^2\), and the IMS identity for \(Z=D_U\) and for \(Z=\delta^U_\mu\). The two error terms give \(K_I\le(3240+61)\pi^2w_{\max}^2\). □

The local gauges \(g_J\) of different cubes are never compared. Each enters one gauge-invariant number, \(\|D_U\chi_Jf\|\) or \(\|\nabla_U\chi_Jf\|\).

**Lemma 3.6 (two-case coercivity, real backgrounds).** Under the hypotheses of Lemma 3.5 and \(144\varepsilon\le1\), for real \(U\), \(\bar m\ge-\mu_0\), and \(\|f\|=1\),
\[
\|X_kf\|\ge s_1-\mu_0-E_0,\qquad E_0=37\kappa\varepsilon+\sqrt E .
\]
*Proof.* Let \(p=\|P_kf\|\), \(q=\|(1-P_k)f\|\), \(p^2+q^2=1\) (Lemma 2.1(ii)).

*Step 1 (Hermitian part).* By Lemma 3.1, \(\|X_kf\|\ge\operatorname{Re}\langle f,X_kf\rangle\ge\bar m+a_kp^2\).

*Step 2 (Poincaré through the averaging).* On each unit cube \(B_y\) take the axial gauge of Lemma 3.4 rooted at \(y\) (side 1): links have \(|\theta'|\le3\varepsilon\eta\), and the averaging transports (monotone paths, at most \(4/\eta\) links) have \(|V_k'-1|\le12\varepsilon\). With \(f'=g_yf\) on \(B_y\) and \(\bar f'\) its mean: \(\|g_yP_kf-\bar f'\|_{B_y}\le12\varepsilon(2+12\varepsilon)\|f\|_{B_y}\le25\varepsilon\|f\|_{B_y}\) (pointwise bound, using \(|V_k'|=1\) and Cauchy-Schwarz); and by Lemma 3.3 and Lemma 3.4, \(\|f'-\bar f'\|_{B_y}\le2\|\nabla_Uf\|_{B_y}+12\varepsilon\|f\|_{B_y}\), where \(\|\nabla_Uf\|_{B_y}\) keeps the links inside \(B_y\). Minkowski in \(\ell^2\) over the cubes: \(q\le2\|\nabla_Uf\|+37\varepsilon\).

*Step 3.* Lemma 3.5 and Step 2: \(\|D_Uf\|\ge\frac{w_{\min}}2\|\nabla_Uf\|-\sqrt E\ge\kappa q-37\kappa\varepsilon-\sqrt E\). So \(\|X_kf\|\ge\kappa q-a_kp-|\bar m|-E_0\).

*Cases.* Let \(p_0=\min(\frac12,\frac\kappa{4a_k})\). If \(p\ge p_0\), Step 1 gives \(\|X_kf\|\ge a_kp_0^2-\mu_0\). If \(p<p_0\) and \(\bar m\ge0.3\kappa\), Step 1 gives \(\|X_kf\|\ge0.3\kappa\). If \(p<p_0\) and \(\bar m<0.3\kappa\), then \(q\ge\sqrt3/2\), \(a_kp\le\kappa/4\), \(|\bar m|\le\max(0.3\kappa,\mu_0)\), and Step 3 gives \(\|X_kf\|\ge(0.866-0.25-0.3)\kappa-\mu_0-E_0\). Finally \(a_kp_0^2=\min(a_k/4,\kappa^2/(16a_k))\ge s_1\) because \(a_k\in[a/2,a]\). □

**Lemma 3.7 (complex backgrounds).** If \(U\in\mathcal U_k(\varepsilon,\delta)\) and \(\delta\le1/8\), then \(\|X_k(U)-X_k(U_R)\|\le K_5\delta\) with \(K_5=16w_{\max}+24a_+\).

*Proof.* \(|e^{i\theta}-e^{i\theta_R}|=|e^{-\theta_I}-1|\le2\delta\eta\), and the same for the inverses; the hopping coefficients are at most \(w_\mu/\eta\) in norm, four directions, two hops: \(\|D_U-D_{U_R}\|\le16w_{\max}\delta\). A transport is a product over at most \(4/\eta\) links, so \(|V_k(U)/V_k(U_R)-1|\le e^{4\delta}-1\le8\delta\) and \(|V_k(U)^{\pm1}|\le2\). Cauchy-Schwarz on each cube (\(\eta^4|B_y|=1\)) gives \(\|Q_k(U)-Q_k(U_R)\|,\|\tilde Q_k(U)-\tilde Q_k(U_R)\|\le8\delta\) and \(\|Q_k(U)\|\le2\). So \(\|P_k(U)-P_k(U_R)\|\le24\delta\). □

**Lemma 3.8 (Combes-Thomas conjugation).** Let \(\rho:\Lambda_\eta\to\mathbb R\) satisfy \(|\rho(x)-\rho(x')|\le|x-x'|_\infty\) (torus distance), \(0\le\alpha\le1\), and \(X_\alpha=e^{\alpha\rho}X_ke^{-\alpha\rho}\). For \(U\in\mathcal U_k(\varepsilon,\delta)\) with \(\delta\le1/8\): \(\|X_\alpha-X_k\|\le K_6\alpha\), \(K_6=32w_{\max}+8a_+\).

*Proof.* \((X_\alpha-X_k)(x,x')=X_k(x,x')(e^{\alpha(\rho(x)-\rho(x'))}-1)\). Hops join points at distance \(\eta\), so the hopping part changes by at most \(\eta^{-1}\cdot4w_{\max}\cdot2\cdot2\cdot2\alpha\eta\). \(P_k(x,x')=\eta^4V_k(y,x)^{-1}V_k(y,x')\) joins points of one unit cube (\(\ell^\infty\)-diameter below 1); the Schur test bounds its change by \(4(e^\alpha-1)\le8\alpha\). □

### 3.3 Proof of Theorem 1

Choose an integer \(M\ge2\) with \(M^2\ge128K_I/s_1^2\) (the torus side is then required to be a multiple of \(M\); for the tower of scales take the original side \(ML^{N'}\)); then \(\varepsilon_0\le\min\bigl(s_1/(85\sqrt{128}\,w_{\max}M),\ s_1/(296\kappa),\ 1/(12M)\bigr)\), so that \(\sqrt E\le s_1/8\) and \(37\kappa\varepsilon_0\le s_1/8\); and \(\mu_0=s_1/4\). Lemma 3.6 gives \(\|X_k(U_R)f\|\ge s_1/2=s_0\) for real backgrounds. \(X_k^*\) is the same kind of operator with \(\gamma_\mu\mapsto-\gamma_\mu\) and the same \(P_k\), so the same bound holds for it. Take \(\delta_0=\min(1/8,s_0/(2K_5))\); Lemma 3.7 gives item 1 for complex \(U\). In finite dimension an injective operator is invertible, so \(\|X_k^{-1}\|\le2/s_0\). Take \(\alpha_0=\min(1,s_0/(4K_6))\); Lemma 3.8 gives \(\|X_\alpha f\|\ge\frac{s_0}4\|f\|\), so \(\|X_\alpha^{-1}\|\le4/s_0\). With \(\rho=\operatorname{dist}_\infty(\cdot,\Delta')\), \(1_\Delta X_k^{-1}1_{\Delta'}=1_\Delta e^{-\alpha_0\rho}X_{\alpha_0}^{-1}1_{\Delta'}\), which is item 2. Item 3: the entries of \(X_k\) are polynomials in \(e^{\pm i\theta}\), and on the open set where item 1 holds the inverse is holomorphic by Cramer's rule; covariance is Lemma 2.1(iii). □

**Remarks.** (i) Nothing in the proof uses \(d=4\) except the constants 4, 81, \(3^d\); the same proof works in every dimension. (ii) The tree (`CN1_TREE.md` L3) asked to "Port from three Euclidean dimensions to four" the construction of [D17] Lemmas 5-6. Theorem 1 is not that port; it reaches the same global bound by a route without local inverses on the fine lattice. Proposition 5.2 shows why this global fine-lattice accretivity estimate is not uniform, and Corollary 4.3 supplies them on the unit lattice.

## 4. Theorem 2: an exact identity for the blocked operator, and its consequences

**Theorem 2 (blocked Hermitian part).** Let \(U\) be real, \(\bar m\in\mathbb R\), and \(X_k(U)\) invertible. Then
\[
\operatorname{Re}D_k=\frac1{a_k}D_k^*D_k+H_k^*\bigl(\operatorname{Re}D_U+\bar m\bigr)H_k .\tag{4.1}
\]
*Proof.* For real \(U\), \(\tilde Q_k=Q_k^*\) (Lemma 2.1(ii)), so \(H_k=a_kS_kQ_k^*\) and \(D_k=a_k-a_k^2Q_kS_kQ_k^*\). Hence \(\operatorname{Re}D_k=a_k-a_k^2Q_k(\operatorname{Re}S_k)Q_k^*\). From \(X_kS_k=1\), \(\operatorname{Re}S_k=S_k^*(\operatorname{Re}X_k)S_k\), and \(\operatorname{Re}X_k=\operatorname{Re}D_U+\bar m+a_kP_k\). So
\[
a_k^2Q_k(\operatorname{Re}S_k)Q_k^*=H_k^*(\operatorname{Re}D_U+\bar m)H_k+a_k(Q_kH_k)^*(Q_kH_k),
\]
using \(a_kS_kQ_k^*=H_k\) and \(P_k=Q_k^*Q_k\). Since \(Q_kH_k=1-D_k/a_k\), the last term is \(a_k-D_k-D_k^*+a_k^{-1}D_k^*D_k\). Therefore \(\operatorname{Re}D_k=D_k+D_k^*-a_k^{-1}D_k^*D_k-H_k^*(\operatorname{Re}D_U+\bar m)H_k\). Subtract \(\operatorname{Re}D_k\) from both sides. □

[check] `check_gw.py`: a 2D analogue (two-component spinors, \(L^k\in\{2,4,8\}\), a \(4\times4\) unit lattice, random real links with angle spread from 0 to 1.5, \(\bar m=0\), \(a=1\)). The residual of (4.1) was at most \(1.4\times10^{-15}\), and \(\|D_k\|\le0.94\le a\) in every case. Guidance only.

Block-spin transformations of fermions are the setting in which Ginsparg and Wilson derived their relation ([GW82]); (4.1) is a relation of the same origin for the Hermitian part, with the Wilson term as the inhomogeneous piece. It is proved here and not attributed to [GW82].

**Corollary 4.1 (every real background).** Let \(U\) be real and \(\bar m\ge0\). Then:

1. \(X_k(U)\) is invertible, and so are \(X'\) and \(D_k+\frac aLP\) (notation of Lemma 2.3).
2. \(\|D_k(U)\|\le a_k\), and \(\operatorname{Re}D_k(U)\ge a_k^{-1}D_k(U)^*D_k(U)\ge0\).
3. \(\|Q_kH_k(U)\|\le1\) and \(\frac\eta2\sum_\mu w_\mu\|\delta^U_\mu H_k(U)\phi\|^2\le a_k\|\phi\|^2\).
4. \(\|D_k+\frac aLP\|\le a_k+\frac aL\), so \(|\det(D_k+\frac aLP)|\le(a_k+\frac aL)^{4|\Lambda_1|}\), and \(D_{k+1}\) of (2.3) again obeys item 2.

No small-field condition and no bound on the field strength enters. Items 2 and 4 are the bounded half of B2 of `CN1MOD.md` §5: in every real background, the blocked kernel and the single-step fermion determinant are bounded uniformly in \(k\), \(L\), the volume and the speeds.

*Proof.* 1. By Lemma 3.1 \(\operatorname{Re}X_k\ge a_kP_k\ge0\). If \(\langle f,\operatorname{Re}X_kf\rangle=0\), then \(\delta^U_\mu f=0\) on every link and \(P_kf=0\). The first condition makes \(f\) covariantly constant: \(f(z)=U_\mu(z)f(z+\eta e_\mu)\) on every link. Telescoping along the averaging path gives \(V_k(y,x)f(x)=f(y)\), so \((Q_kf)(y)=f(y)\). Then \(P_kf=0\) forces \(f=0\). So \(\operatorname{Re}X_k\) is positive definite and \(X_k\) is injective, hence invertible. The same argument applies to \(X'\) (it has the same form). Lemma 2.3 then gives \(D_k+\frac aLP\) invertible.
2. By (4.1) and \(\operatorname{Re}D_U+\bar m\ge0\), \(\|D_kF\|^2\le a_k\operatorname{Re}\langle F,D_kF\rangle\le a_k\|F\|\|D_kF\|\).
3. With \(N=D_k/a_k\): \(\|N\|\le1\) and \(\operatorname{Re}N\ge N^*N\), so \((1-N)^*(1-N)=1-2\operatorname{Re}N+N^*N\le1-N^*N\le1\). And (4.1) gives \(H_k^*(\operatorname{Re}D_U)H_k\le\operatorname{Re}D_k\le a_k\); use Lemma 3.1.
4. \(\|P\|=1\) for real \(U\) (orthogonal projection). Hadamard's inequality \(|\det A|\le\prod_i\|Ae_i\|\le\|A\|^{n}\) on the \(4|\Lambda_1|\)-dimensional space. The last claim is (2.3) and item 2 at the next scale (after rescaling). □

**Corollary 4.2 (small fields: unit-lattice kernels).** Let \(\mathcal U_k^\sharp=\mathcal U_k(\varepsilon_0/L^2,\delta_0/L)\), \(\bar m\ge-\mu_0/L\), \(T\ge6ML\), \(ML\mid T\), with the constants of Theorem 1. (Field strength has dimension two, so this is the domain on which Theorem 1 also applies to \(X'\) after rescaling by \(L\).) Then for \(U\in\mathcal U_k^\sharp\):

1. \(|D_k(y,y')|\le a_k\delta_{yy'}+\frac{16a_k^2}{s_0}e^{-\alpha_0(|y-y'|_\infty-1)_+}\) (matrix norm on \(\mathbb C^4\)).
2. \(\|\Gamma_k\|\le\frac1{a_k}+\frac{8L}{s_0}\) for real \(U\) (for complex \(U\), \(\|R\|\le5/a_k\) and \(\|P\|\le4\) give \(\|\Gamma_k\|\le\frac5{a_k}+\frac{200L}{s_0}\)), and \(|\Gamma_k(y,y')|\le C(L)\,e^{-\frac{\alpha_0}L(|y-y'|_\infty-2L)_+}\).
3. \(D_k\), \(\Gamma_k\) and \(\det X_k\) are holomorphic in \(\theta\) on the interior of the domain, and covariant under real gauge transformations.

*Proof.* 1. \((Q_kS_k\tilde Q_k)(y,y')=Q_k1_{B_y}S_k1_{B_{y'}}\tilde Q_k\); the factors have norms at most 2, \(\frac4{s_0}e^{-\alpha_0\operatorname{dist}_\infty(B_y,B_{y'})}\), 2 (Theorem 1 item 2 and Lemma 3.7), and \(\operatorname{dist}_\infty(B_y,B_{y'})\ge|y-y'|_\infty-1\). 2. Use (2.1). \(R\) acts inside single \(L\)-blocks of \(\Lambda_1\). \(X'=L^{-1}\times\)(the operator of Theorem 1 at spacing \(\eta/L\)), so \(\|X'^{-1}\|\le2L/s_0\) and its block kernel decays at rate \(\alpha_0\) per scale-\((k+1)\) unit, that is \(\alpha_0/L\) per unit at scale \(k\). 3. Theorem 1 item 3 and Cramer's rule. □

**Corollary 4.3 (unit-lattice accretivity; local inverses on every subset).** Let \(U\in\mathcal U_k^\sharp\) be real, \(\bar m\ge0\), \(M_k=D_k+\frac aLP\), and \(\sigma=(\frac1{a_k}+\frac{8L}{s_0})^{-1}\). Then
\[
\operatorname{Re}M_k\ge c_N:=\frac{\sigma^2}{2a}.
\]
Consequently, for **every** subset \(Y\subset\Lambda_1\), the compression \(M_{k,Y}=1_YM_k1_Y\) on \(\ell^2(Y)\) is invertible with \(\|M_{k,Y}^{-1}\|\le1/c_N\), and \(|M_{k,Y}^{-1}(y,y')|\le\frac2{c_N}e^{-\alpha_1|y-y'|_\infty}\) for an explicit \(\alpha_1>0\) depending on \(a,w_{\min},w_{\max},L\). For complex \(U\in\mathcal U_k(\varepsilon_0/L^2,\delta_1/L)\) with \(\delta_1\) small enough, the same holds with \(c_N/2\).

*Proof.* By (4.1), \(\operatorname{Re}M_k\ge a_k^{-1}D_k^*D_k+\frac aLP\). Corollary 4.2 gives \(\|M_kF\|\ge\sigma\|F\|\). And \(\|M_kF\|^2\le2\|D_kF\|^2+2(\frac aL)^2\|PF\|^2\le2a\bigl(a_k^{-1}\|D_kF\|^2+\frac aL\|PF\|^2\bigr)\) since \(a_k\le a\). So \(\operatorname{Re}\langle F,M_kF\rangle\ge\frac{\sigma^2}{2a}\|F\|^2\). A lower bound on the Hermitian part passes to every compression: \(\operatorname{Re}\langle F,M_{k,Y}F\rangle=\operatorname{Re}\langle F,M_kF\rangle\) for \(F\) supported in \(Y\); then \(\|M_{k,Y}F\|\ge c_N\|F\|\). Decay: Combes-Thomas as in Lemma 3.8, using the kernel bound of Corollary 4.2 item 1; the change of \(M_{k,Y}\) under conjugation by \(e^{\alpha\rho}\) is at most \(\sum_{z}\sup|M_k(y,y+z)|(e^{\alpha|z|_\infty}-1)\), which is \(O(\alpha)\) for \(\alpha\le\alpha_0/2\). Complex \(U\): the resolvent identity and Theorem 1 give \(\|D_k(U)-D_k(U_R)\|=O(\delta)\). □

Corollary 4.3 supplies local inverses on small fields; it does not construct the full covariant random-walk expansion. In d = 3 at zero field, [D17] eq. (115) obtains them "by some Fourier analysis and taking advantage of the Wilson form of the free fermion action"; here the Wilson form enters through (4.1) and no Fourier analysis at the unit-lattice level is used.

**Corollary 4.4 (accretivity survives decoupling).** Partition \(\Lambda_1\) into cubes \(\{Y\}\). Let \(S=(s_{YY'})\) be a real positive semidefinite matrix with \(s_{YY}=1\), and let \(M_k\circ S\) have blocks \(s_{YY'}(M_k)_{YY'}\). Under the hypotheses of Corollary 4.3, \(\operatorname{Re}(M_k\circ S)\ge c_N\), so \(M_k\circ S\) is invertible with \(\|(M_k\circ S)^{-1}\|\le1/c_N\), uniformly in \(S\).

*Proof.* Write \(S=\sum_ru_ru_r^{\top}\) and \(D_r=\bigoplus_Yu_{r,Y}1_Y\). Then \(A\circ S=\sum_rD_rAD_r\) for every block operator \(A\), so \(A\ge0\) implies \(A\circ S\ge0\). Apply this to \(A=\operatorname{Re}M_k-c_N\): \(\operatorname{Re}(M_k\circ S)-c_N(1\circ S)\ge0\), and \(1\circ S=1\) because \(s_{YY}=1\). □

Interpolation matrices of the Brydges-Kennedy type, \(s_{YY'}=\min\) of the forest parameters on the path from \(Y\) to \(Y'\), are positive semidefinite with unit diagonal; so cluster expansions of \(\log\det M_k\) and of \(\Gamma_k\) with such parameters keep the bound of Corollary 4.3 at every interpolation point. (Positive semidefiniteness of these matrices is a standard fact; it is not used elsewhere in this file, and the corollary is stated for any such \(S\).)

## 5. Large fields

**Proposition 5.1 (zero modes pass to the blocked operator exactly).** Let \(U\) be real, \(\bar m\ge0\) (so \(X_k\) is invertible, Corollary 4.1). Then \(Q_k\) is injective on \(\ker(D_U+\bar m)\) and
\[
\ker D_k(U)=Q_k\,\ker(D_U+\bar m).
\]
*Proof.* If \((D_U+\bar m)\psi_0=0\), then \(X_k\psi_0=a_k\tilde Q_kQ_k\psi_0\), so \(\psi_0=H_k\Phi\) with \(\Phi=Q_k\psi_0\). Then \(Q_kH_k\Phi=\Phi\) and \(D_k\Phi=a_k(1-Q_kH_k)\Phi=0\). If moreover \(\Phi=0\), then \(X_k\psi_0=0\), so \(\psi_0=0\): injectivity. Conversely, if \(D_k\Phi=0\), put \(\psi=H_k\Phi\); then \(Q_k\psi=\Phi\) and \((D_U+\bar m)\psi=X_k\psi-a_kP_k\psi=a_k\tilde Q_k(\Phi-Q_k\psi)=0\). □

So the blocked operator inherits every exact zero mode of the fine operator, with the same multiplicity. For U(1) backgrounds on \(T^4\) with constant \(F_{12},F_{34}\) and flux quanta \(n_{12},n_{34}\), the continuum Dirac operator has index \(n_{12}n_{34}\) (standard; not used as a proof step). The Wilson term can lift these modes. The exact kernel statement alone does not give a quantitative statement for near-zero modes.

**GAP 5.2 (antiperiodic time).** Pass 1 takes `f(x)=c cos(2πx₁)e` with a constant time factor. With antiperiodic time links, the boundary hop contributes to its energy. The equality in its proof omits that contribution. Thus the stated constant `2π²w_max` is not established by that proof.

**Proposition 5.2 (corrected numerical-range estimate).** For free links with the antiperiodic time sign and `m̄=0`, there is a unit vector `f` such that
\[
 \operatorname{Re}\langle f,X_k f\rangle\le w_{\max}\eta\left(2\pi^2+\frac{\pi^2}{2T^2}\right).
\]
*Proof.* Take `f(x)=c exp(iπx₀/T) cos(2πx₁)e`, normalized. Each unit cube has zero spatial mean, hence `Q_k f=0`; paths inside a cube do not cross the time seam. The antiperiodic plane wave has time momentum `π/T`, and the cosine has spatial momentum `2π`. By the Wilson identity the real part is
\[
\frac2\eta\left[w_1\sin^2(\pi\eta)+w_0\sin^2\left(\frac{\pi\eta}{2T}\right)\right],
\]
which gives the bound by `sin t≤t`. The formula includes `L^k=2`. □

The numerical range approaches zero as `η→0` for fixed `T`; this alone says nothing about the smallest singular value.

**Proposition 5.3 (no small-link gauge on a large-field cube).** Let a cube contain a square loop \(\gamma\) of rescaled side \(\ell\) in a coordinate plane, with holonomy angle \(\Theta\in(-\pi,\pi]\). Then for every real gauge transformation \(g\) some link of \(\gamma\) has \(|\theta^g_\mu(x)|\ge|\Theta|\eta/(4\ell)\) (representatives in \((-\pi,\pi]\)), and so \(\eta^{-1}|U^g_\mu(x)-1|\ge|\Theta|/(2\pi\ell)\).

*Proof.* \(\gamma\) has \(4\ell/\eta\) links, and the signed sum of the representatives is \(\equiv\Theta\) mod \(2\pi\). If every representative had modulus below \(|\Theta|\eta/(4\ell)\), the sum would have modulus below \(|\Theta|\le\pi\), hence would equal \(\Theta\), a contradiction. Finally \(|e^{i\theta}-1|\ge\frac2\pi|\theta|\) for \(|\theta|\le\pi\). □

**GAP 5.3 (claimed threshold).** Pass 1 substitutes `ℓ=min(1,sqrt(π/F))` into Proposition 5.3 without requiring `ℓ` to be an integer multiple of η or proving the loop exists on the lattice. It also identifies a link coefficient with an operator-norm bound without tracking the Wilson hopping matrices. Proposition 5.3 itself proves the holonomy bound only. It does not prove that every local free Neumann expansion fails at `F≥2πs₀`.

**GAP 5.1 (near-zero interpretation).** The kernel identity proves exact zero-mode correspondence, not that every near-zero fine mode remains near zero after blocking. A quantitative lower bound on its block average would be needed. The continuum flux-index remark in pass 1 is not used.

[check] `check_flux.py`: the 2D analogue with uniform flux \(N_\Phi\) quanta on a \(4\times4\) unit lattice, \(a=1\), \(\bar m=0\), \(L=2\) for the unit-lattice step. At rescaled field strength \(F\approx6.3\): \(\sigma_{\min}(X_k)=0.675\) at \(\eta=1/4\) and \(0.365\) at \(\eta=1/8\) (zero field: \(1.28\), \(1.26\)). The ratio \(\sigma_{\min}/(\eta F)\) is 0.43 and 0.46, as expected if would-be zero modes are lifted by the Wilson term at a rate of order \(\eta F\). On the same toy, \(\sigma_{\min}(D_k+\frac aLP)\) stayed between 0.22 and 0.83 and \(\lambda_{\min}(\operatorname{Re}(D_k+\frac aLP))\) stayed positive (at least 0.22). The toy is too coarse to settle the possible behavior of near-zero modes of the blocked step. Guidance only: this suggests that Theorem 1's constant cannot be made uniform in \(k\) on large fields, and it neither proves nor refutes a uniform bound for \(D_k+\frac aLP\).

## 6. Census: the failed symmetry restoration

**GAP 6.1 (averaged transports).** Pass 1 changes to centered odd-`L` blocks and replaces each path phase by the mean of the `4!` path phases. It asserts that these means are unimodular, that `tilde Q=Q*`, and that all previous projection-based proofs hold verbatim. This fails even for real backgrounds. Two paths enclosing a plaquette can have phases `1` and `−1`; their mean is zero. Even when the mean is nonzero, e.g. `(1+i)/2`, it has modulus `1/sqrt(2)`. Consequently the algebraic inverse of the averaged transport may not exist and, when it exists, is not generally its conjugate. Averaging the reversed transports instead also gives `Q Q*≠1` in general. This is the exact point where Lemma 6.1's symmetry proof stops. Small field makes the average close to one but not exactly unimodular. A normalized phase or another construction would need a new symmetry, analyticity and inverse proof.

Pass 1's **proposed census**, not an established exhaustive list, has for each species the relevant mass and the marginal time and spatial kinetic coefficients `z_{a,0},z_{a,s}`, and photon coefficients `z_E,z_B`; it normalizes `z_{a,0}=1` and identifies `v_a=z_{a,s}/z_{a,0}`, `c²=z_B/z_E`, `G=e²/z_E`. It claims that the only odd marginal coordinate is `v₁−v₂` and the odd relevant coordinate is `m̄₁−m̄₂`. Its proposed noncovariant list includes `A₀²`, `ΣA_j²`, additional two-derivative quadratic terms, and the four quartics `A₀⁴`, `A₀²ΣA_j²`, `(ΣA_j²)²`, `ΣA_j⁴`. The full symmetry transformations, photon blocking and treatment of the nonlocal transverse mass need explicit verification before this can be an exhaustive census. Gauge covariance alone does not supply it. C1 cannot be discharged on this basis. Tuning the two critical masses is an additional open input, not an established fact.

**Theorem 6.2 (free Wilson node).** With positive weights and zero mass, the free symbol has its only zero in the Brillouin zone at `p=0` modulo reciprocal lattice vectors. At a doubler corner with any `ηp_μ=π`, its scalar Wilson term is at least `2w_min/η`.

*Proof.* The square of the symbol is the sum of `η⁻²(Σw_μ(1−cos ηp_μ))²` and `η⁻²Σw_μ² sin²(ηp_μ)`. A zero forces every sine to vanish and the nonnegative scalar sum to vanish. Hence every cosine is 1. At any other corner one scalar summand is at least `2w_min`. □

## 7. Large fields and remaining steps

Fix L and let `U′` be in the rescaled small-field domain of Corollary 4.2, with its corrected volume condition. Let `R` be a union of unit cubes, and suppose `U` and `U′` differ only on specified links in `R`. Write `Φ_R=η⁻² max_{p⊂R}|φ_p(U)|`, when that set is nonempty.

**LF (open).** For constants independent of scale and volume, establish
\[
|D_k(U)(y,y')-D_k(U')(y,y')|\le C(1+\Phi_R)^{p_*}e^{-\gamma(\operatorname{dist}(y,R)+|y-y'|_\infty)}.
\]
The constants may depend on fixed L. Boundary plaquettes and the notion of links belonging to `R` must be fixed before applying the statement. The factor cannot by itself encode arbitrary changed boundary links unless the convention makes it appropriate.

**Theorem 7.1 (conditional determinant consequence).** Assume LF and that the changed coarse projection is supported in the `L`-blocks meeting `R`. Then, with `M_k(U)=D_k(U)+(a/L)P(U)`,
\[
\log|\det M_k(U)|-\log|\det M_k(U')|\le C_L(1+\Phi_R)^{p_*}|R|.
\]
*Proof.* Put `Δ=D_k(U)−D_k(U′)` and `A=(Δ+(a/L)(P(U)−P(U′)))M_k(U′)⁻¹`. The real-background invertibility result gives nonzero determinants. The finite-dimensional inequality `|det(1+A)|≤exp ||A||₁` applies. LF gives `||Δ||₁≤4Σ_{y,y′}||Δ(y,y′)||≤C(1+Φ_R)^{p_*}|R|`. The projection difference has norm at most 2 and rank at most `4L⁴|R|`, hence trace norm at most `8L⁴|R|`. Corollary 4.2 bounds the reference inverse. □

**Theorem 7.2 (near-null block averages).** For real `U`, `m̄≥0`, and every `ψ`,
\[
\|Q_k\psi\|^2=\|P_k\psi\|^2\le a_k^{-1}\|\psi\|\,\|X_k\psi\|.
\]
*Proof.* `a_k||P_kψ||²≤Re⟨ψ,X_kψ⟩≤||ψ||||X_kψ||`. □

The same inequality holds for `X_k*` because it has the same Hermitian part. Thus each left and right unit singular vector at singular value `σ` has block average at most `sqrt(σ/a_k)`. This proves boundedness of its individual sandwiched singular contribution; it does not bound the sum or establish locality.

**Theorem 7.3 (geometric resolvent, conditional support form).** Let `X=X_k(U)`, `X′=X_k(U′)` be invertible, let `χ` be a real multiplier, and put `C=[X′,χ]`, `S=X⁻¹`, `S′=X′⁻¹`. Suppose `(X−X′)χ=χ(X−X′)=0`, `C=1_Λ C 1_Λ`, and unit cubes `B_y,B_y′` lie where `χ=1` and have the same averaging maps for `U,U′`. Then
\[
\Delta(y,y')=a_k^2Q_k1_{B_y}\bigl[S'\chi C S'+S'C(1_\Lambda S1_\Lambda)CS'\bigr]1_{B_{y'}}\widetilde Q_k.
\]
*Proof.* The support assumptions and the commutator identity imply on inputs supported where `χ=1`, `S=χS′−SC S′`; on outputs there, `S=S′χ+S′CS`. Substitution yields `S−S′=−S′χCS′−S′CSC S′` between the two cubes. Insert `1_Λ` around `S` and use `Δ=−a_k²Q_k(S−S′)tilde Q_k` there. □

**GAP 7.3.** Pass 1 states this for a geometric cutoff without fully specifying whether a changed link crosses the boundary of `R` or how coarse paths cross it. The abstract support hypotheses above are sufficient; their verification for a chosen region convention remains open. A bound on `1_ΛS1_Λ` must also control decay along the boundary, not merely its norm.

**Three attempted routes.** (1) Local axial-gauge resolvent expansion: loop holonomy prevents making every link arbitrarily small, but the numerical threshold claimed by pass 1 is not proved; no convergent expansion on the large-field cubes was supplied. (2) Covariant random-walk expansion: the missing input is a scale-uniform local large-field resolvent bound or a way to keep the cancellation in Theorem 7.2. The pass-1 two-dimensional flux experiment reports `σ_min(X)=0.675` at `η=1/4` and `0.365` at `η=1/8`, with `F≈6.3`; its scripts were unavailable here, and two points prove no scaling law. (3) Finite-range polymer localization: the available background-uniform norm and energy bounds do not themselves give exponential decay; the energy bound permits an `η⁻¹/²` loss. None of these failures excludes other methods. A near-null spectral split is a proposed route; it requires quantitative control of the remaining spectrum and boundary couplings.

Pass 1's comparison of a global large-field factor with the number of cubes fails to give a uniform bound along a sequence such as `k≈N/2`, since an exponential volume can dominate `exp[−c(log k)^{2p}]`. Its stronger assertion for every `k≤N/2` is false as stated for very small `k`. This only rules out that particular global estimate, not every nonlocal approach.

**S-small (open).** Construct and bound the small-field photon cumulant or cluster expansion, including the claimed higher-cumulant `O(G_k²)` estimate. **M1 (open).** Match the per-step one-loop speed increment to `hG_k F(x_k)` with the stated ultraviolet and infrared boundary errors. Neither was attempted in pass 1. **(T3)** also needs a specified full step, invariant domain, and all marginal controls. **UB″** remains the stronger open alternative. No counterexample to (W) is supplied; symmetry by itself is not a remainder estimate.

## 8. Readings and reported checks

No reading, law text or axiom change is proposed for adoption. The three specifications and their pass-1 four-test results are recorded in §1; the census construction has GAP 6.1 despite that earlier check. `CN1MOD.md` describes M″ as a supplied model, not a realized live law. Scheme coefficients are not yet invariant threshold speeds; OBS and LIMIT remain separate.

Pass 1 reports a two-dimensional identity check with residual at most `1.4×10⁻¹⁵` and `||D_k||≤0.94` for the cases it tried. It also reports that the blocked step in its flux toy had smallest singular values between `0.22` and `0.83` and Hermitian-part minimum at least `0.22`. These are finite toy checks, not proofs; the scripts were not present for reproduction. Pass 1 reports reading Dimock arXiv:1712.10029, Lemmas 5–6 and equations (94)–(95), and arXiv:2204.07201, equation (19). It reports the tree's BBS15 theorem locator unverified; BOS89, BOS91, CN83, M07, BDH98 and the claimed FGM22 paper were not verified. No literature citation supplies the missing RG.
