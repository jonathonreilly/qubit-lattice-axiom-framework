# RO1 — O(4) covariance

Provenance: OpenAI Codex, 2026-11-05; exact runtime variant and effort not exposed. Phase A, pass 2 (distil), checkout `a456311fd37ebcc1811c1180cff145d7d2b91570`. Research text, not an audit; grants no status. The source notes were checked individually; this part is not yet refereed as a whole.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the insertion, plate, angular-kernel, two-point and polygon methods. Sources are pinned to `31a47c543775`. The proofs below distil the five local ports, retaining their check reports' corrections. All deductions are by hand.

## Definitions and imports

**Definition 1. Fields and tests.** Work in four dimensions with Wilson SU(2), odd block factor \(L\ge3\), spacing \(a=L^{-K}\), localization length \(Ma_s\), \(a_s=L^{-s}\), \(M=L^{m_0}\), and compatible tori \(\ell=2L^m\), \(m\ge m_0\). Set
\[
 a_p=1-\tfrac12\operatorname{ReTr}U_p,\qquad
 \mathcal O_a(f)=\sum_p f(x(p))a_p,\qquad
 X_{a,\nu}(f)=\mathcal O_a(f)-\nu\mathcal O_a(f),\qquad
 \|f\|_\sharp=\max(\|f\|_\infty,c_M\|\nabla f\|_\infty).
\]
A separated tuple has compact \(C^1\) entries with pairwise disjoint supports. A field polynomial is a finite complex linear combination of such tuples, including the empty tuple \(1\). Products mean concatenation only where the resulting supports are separated. Conjugation conjugates coefficients and tests. A common translation acts by \(\tau_vf(x)=f(x-v)\), and \(Rf(x)=f(R^{-1}x)\).

A volume-first realization means periodic infinite-volume Wilson DLR states \(\rho_j,\nu_j\) at the same first-passage data, with \(a_j\to0\), for which every separated moment
\[
 \rho_j\prod_iX_{a_j,\nu_j}(f_i)\longrightarrow\sigma(f_1,\ldots,f_n).
 \tag{D.1}
\]
The volume limit is already taken at each spacing. This part assumes the realization; it does not construct first-passage data.

**Definition 2. Hilbert conventions.** Write \(t=x_4\), \(\theta x=(x_1,x_2,x_3,-t)\). On positive-time polynomials use the inner product, antilinear in its first entry,
\[
 \langle[F],[G]\rangle=\sigma(\theta\bar F\cdot G),\quad
 \Omega=[1],\quad \|F\|_b=\|[\tau_{-be_4}F]\|.
 \tag{D.2}
\]
The last expression requires every entry of \(F\) above \(b\). A coordinate-\(j\) picture uses \(x_j\) as time. The **cube cone** means joint spectral support \(E\ge0,\ |q_r|\le E\) in each such picture; the round cone is not assumed.

**Definition 3. Plates and configurations.** In the plane \((t,u)=(x_4,x_1)\), a plate is \(\alpha(t,u)\varphi(x_2,x_3)\). Initially both factors are compact \(C^1\), and \(\varphi\) is real. An \(L^1\) plate below means its explicitly constructed continuous extension. Write \(R_z\) for the usual planar rotation matrix at a complex angle. Define
\[
 v_\pm=v^0\pm iv^1,\quad \mathbb V=\{\Re v_\pm>0\},\quad
 r(v)=\min_\pm\Re v_\pm,\quad v^*=(\bar v^0,-\bar v^1),\quad e_0=(1,0).
 \tag{D.3}
\]
Write \(\partial(z_1,\ldots,z_n)=(z_2-z_1,\ldots,z_n-z_{n-1})\). A positive ordered configuration has \(x_1\in\mathbb V\) and consecutive differences in \(\mathbb V\). A pencil is real with every consecutive difference having argument in \((-\pi/8,\pi/8)\). Every real configuration used for harmonic coefficients has **distinct planar points**. Gram configurations have distinct points within each tuple, even when their times tie.

**Definition 4. Ultraviolet class.** Fix \(\vartheta_*=1/12000\). The class \(\mathfrak T(d;\vartheta_*)\) consists of nonzero nonnegative compact \(C^1\) tests \(f,h\), each supported in a radius-\(d\) ball, placed anywhere, with
\[
 d\le\operatorname{dist}(\operatorname{supp}f,\operatorname{supp}h)\le6d,
 \quad \int f\ge\vartheta_*\|f\|_\infty d^4,
 \quad \operatorname{Lip}f\le\|f\|_\infty/(\vartheta_*d),
 \tag{D.4}
\]
and the same two bounds for \(h\). A smaller shape parameter gives a broader admissible class.

**Definition 5. Distribution domain.** Put \(\mathcal C_n=\{(x_i):x_i\ne x_j\text{ for }i\ne j\}\), \(\Delta_n=\mathcal C_n^c\). The space \(\mathcal S_{\ne,n}\) consists of Schwartz functions whose every derivative vanishes on each coincidence diagonal. \(T_n\) denotes the moment distribution on \(\mathcal C_n\), and \(\Sigma_n\) its given continuous extension to \(\mathcal S_{\ne,n}\).

All subsequent statements use the following imports on the **same** realization.

- **H-U (UV1, full rooted D1).** For every ordinary finite real Lipschitz source family, the torus partition function has a complex upper bound and an unsourced floor. After division by the floor, on source norm below \(2r_{\rm src}\),
  \[
  |Z_\ell(W)|/Z_\ell(0)\le
  \exp\{\Re U_\ell(W)+\Re\sum_{s,X}e_{s,X}(W)+C_{\rm st}\ell^4\}.
  \tag{H.U}
  \]
  Here \(U_\ell=\sum_pu_p(W(x(p)))\). The point terms and domain terms are holomorphic and vanish at zero. Point terms have fixed-cutoff bounds uniform in position and torus. Domain terms have \(|e_{s,X}|\le A e^{-\kappa m(X)}\), normally convergent sums on smaller source balls, and depend only on the source in \(X^+\). They are independent of its list representation. Domains are nonempty unions of scale cubes; \(m(X)\) is the minimum length of a cubical edge tree meeting them. \(X^+\) lies in a fixed number of neighboring layers and has diameter at most \(C a_s(m(X)+1)\). Decay exceeds the rooted entropy rate, including any domain-type multiplicity. The source class includes mirror-periodized profiles, with independent even and odd coefficient lists before conjugate evaluation. All constants are uniform in the allowed cutoff data and tori.

  **Outstanding — imported UV1:** this manuscript does not prove this actual source representation, its bounds or its domain admission. A weaker unrooted count is insufficient.

- **H-L (LG1).** Every periodic state used is invariant under lattice translations and signed permutations, and reflection positive at coordinate site, coordinate bond and diagonal mirrors. Finite Wilson tori have coordinate reflection positivity. These statements apply to bounded local cell functions. Lemma 1 below supplies the precise chessboard consequence used here.

- **H-C (CL1(2)–(4), with its local SR1 bounds).** The limit is normalized, symmetric, real, translation- and hypercubic-invariant. It has position-uniform local \(C^1\) bounds on fixed separated geometries, the distributions \(T_n\), and coordinate and diagonal reflection positivity. Each coordinate Hilbert completion has a dense polynomial class map, strongly continuous self-adjoint contraction semigroup \(e^{-tH_j}\), strongly commuting tangential unitary translations, invariant unit vacuum, and the cube cone. The class maps realize real translations as in (D.2).

- **H-T (TP1(4), state-uniform TU10).** There are \(d_0>0\) and a finite nonnegative \(u(d)\to0\) such that the connected two-point function satisfies
  \[
  0\le S_2^T(f,h)\le u(d)\|f\|_\infty\|h\|_\infty
  \quad(0<d\le d_0,\ (f,h)\in\mathfrak T(d;\vartheta_*)).
  \tag{H.T}
  \]
  Here \(S_2^T(f,h)=\sigma(f,h)-\sigma(f)\sigma(h)\). The bound holds uniformly in positions and approximating periodic states, and passes to their realized limits. TP1's proposed \(u(d)=C'[\log(1/d)]^{-2}\) suffices; only its vanishing is used.

  **Outstanding — imported TU10:** the interacting ultraviolet estimate remains an input. A torus-only law, a bound for the mixture alone, or a narrower unchecked shape class does not replace it.

- **H-S (SR1(4)).** The continuous diagonal-flat extensions \(\Sigma_n\) exist, agree with separated moments, and have constrained tensor density. No extension through a coincidence diagonal is assumed.

- **H-P (PH1, only for components).** Each component has an all-state realization (D.1), the H-C and H-S interfaces, and convergent one-point differences. Its mean is \(c\int f\). The realization permits self-centering by those one-point limits. H-U and H-T are uniform over the states in this realization. Symmetry of the mixture is not used to infer symmetry of a component.

The mathematical background used is bounded-form representation on Hilbert space, joint spectral calculus for strongly commuting self-adjoint operators, the spectral theorem for strongly continuous unitary groups, Cauchy's formula and the holomorphic identity theorem, and elementary integration and distribution calculus. No Yang–Mills estimate is hidden in these background tools. The normal-family, transform-uniqueness and tensor-density steps needed below are written out.

## Order of constants

Use the order of [in1.md](in1.md), “Constant order,” including Amendment 1, as an imported condition. In its ten rows: (1) reserves, margins and power-count exponents; (2) scale-independent geometry, then odd \(L\), then flat constants; (3) gauges, propagator/profile rates, \(M_1,R_1\), seam/tower bounds; (4) early H-M constants, Gaussian constants, \(W_0\), then \(\kappa,\Theta,\lambda\); (5) \(\bar\kappa,\kappa_1\), response lengths/radii, \(M'_1,M_2,\Theta_1,\varpi_T\), then \(M\); (6) post-\(M\) charts, \(A_1,A_0,C_0,C_1\), radii and response room; (7) activity, history, volume and entropy costs in that row's internal order; (8) remaining source, floor, flow and tube constants; (9) \(X_0\), then \(\gamma=X_0^{-1/2}\), then first-passage window constants; (10) \(g\), admissible geometry and cutoff data. This reference retains the row's floors and windows; it does not assert that its conditional imports are established.

For RO1, fix the rooted geometry and its entropy rate before the source decay floor. Fix the source radius and H-U constants in IN1's source-constant rows, before its final small-coupling choice. Fix \(\vartheta_*\) and the explicit shapes of Lemma 5 before requesting TP1's ceiling; impose that ceiling together with IN1's ceiling before choosing \(g\). TP1 supplies \(d_0,u\). RO1 adds no ceiling on the coupling.

After these fixed choices, set \(c_I=1/(40L)\), choose \(r_{\rm src}>0\) inside H-U's radius, and derive the positive entropy gaps and \(C_1,C_2\) in Lemma 2. Then choose \(B_0,Q_0\) there and set \(C_I=2Q_0/r_{\rm src}\), \(p_I=0\). Choose a compact parametrix cutoff, then \(\epsilon=\min(c_I/8,1/1024)\) and the density constant \(C_{\rm PD}\); set \(\wp=p_I+5=5\). These constants precede \(n\), labels, positions, outside polynomials and \(\eta\). Only afterwards choose the local scale \(l\), parametrix radius \(\epsilon\eta\), and product padding. Constants depending on a fixed label or configuration are marked as such. No later constant is fed back into IN1.

## The insertion and plate bounds

**Lemma 1 (cell domination).** For an even-cell compatible torus and an aligned board of side \(l\), let
\[
 p_{l,\ell}(D)=\left\langle\prod_C D^{[C]}\right\rangle_\ell^{1/N},
 \qquad N=(\ell/l)^4,
 \tag{1.1}
\]
where copies are reflected into each cell and conjugated for odd parity. Unoccupied cells carry the factor one. Then \(p\) is a seminorm, \(p(1)=1\), \(p(D)\le\|D\|_\infty\), and
\[
 |\langle\prod_C D_C\rangle_\ell|\le\prod_Cp_{l,\ell}(D_C),\qquad
 |\rho(\prod_C D_C)|\le\liminf_{\ell\to\infty}\prod_Cp_{l,\ell}(D_C).
 \tag{1.2}
\]
The second bound holds for every periodic state and finite collection of cells. Coarse-cell seminorms of products are bounded by the products of their fine-cell seminorms.

*Origin:* [ui-port.md](ui-port.md) §2; [o4-check-1.md](../gates/o4-check-1.md) §2.

*Proof.* Reflection positivity gives reflection Cauchy–Schwarz. In one coordinate with an even number \(q\) of slabs, normalize each of finitely many profiles by \((Z_j+\varepsilon)^{1/q}\), where \(Z_j\) is its fully reflected integral. Maximize the absolute integral among all fillings. If the maximum is positive, reflecting either half of a maximizing filling preserves the maximum. Choose a maximizer with the longest constant run. A run of length at most \(q/2\) can be doubled by reflecting at its end. A longer run contains a whole half; reflecting that half gives a constant filling. Thus a constant filling maximizes, and its value is at most one. The zero-maximum case is immediate. Let \(\varepsilon\downarrow0\) and apply this in each coordinate. The commuting coordinate reflections prove the first inequality. Expansion of the dissemination of \(D+E\) then proves the triangle inequality; conjugation and homogeneity follow directly. The fully reflected integral is nonnegative by the same reflection positivity.

For a real bounded cell function \(H\), conditional Jensen and the DLR equation compare its copies in a side-\(\ell\) cube with the torus. Put \(n=\ell/a\). For each plaquette orientation the common interior has \(n^2(n-1)^2\) terms, while the DLR and torus actions have \(n^4+2n^3\) and \(n^4\). Since \(0\le a_p\le2\), the total oscillation cost over six orientations is at most \(72\beta n^3\). Dividing by the number of cells gives
\[
 \rho(H)\le\log p_{l,\ell}(e^H)+72\beta l^4a^{-3}\ell^{-1}.
 \tag{1.3}
\]
Invariance under board reflections makes every copy have the same mean. Apply (1.3) to \(H=\log(1+tV)\), real bounded \(V\), \(0<t\|V\|_\infty\le1/2\). Use \(\log(1+tV)\ge tV-t^2V^2\) and \(p(1+tV)\le1+tp(V)\). First take the volume limit along a subsequence attaining the lower limit, then \(t\downarrow0\). Thus \(\rho(V)\le\liminf p(V)\). Apply this to \(\Re(e^{-i\phi}D)\), where \(\phi=\arg\rho(D)\); the seminorm of that real part is at most \(p(D)\).

An odd coarsening \(d=L^r\) preserves fine walls and reflection parity. Disseminate the coarse product, apply the finite inequality on the fine board, and take the coarse-cell root. This proves refinement. Enclose a finite collection in one aligned coarse cell and use the one-cell bound just proved. This gives the second inequality of (1.2). All volume limits are at fixed cutoff. ∎

**Lemma 2 (UI, uniform small-ball insertion).** Under H-U, H-L and H-C, if \(0<\eta\le1\), \(k\) is real compact \(C^1\),
\[
 \operatorname{supp}k\subset B(y,c_I\eta),\quad |y_4|\le\eta/8,
 \qquad F,G\text{ have all entries strictly above }\eta/4,
\]
then
\[
 |\sigma(\theta\bar F\cdot(k)\cdot G)|
 \le C_I\|k\|_\sharp\|F\|_{\eta/4}\|G\|_{\eta/4}.
 \tag{2.1}
\]
The constant is independent of the numbers and coefficients of outside fields, the states, the cutoff sequence and the position. Thus \(p_I=0\). Complex \(k\) costs at most a factor two.

*Origin:* [ui-port.md](ui-port.md) §§3–6; [o4-check-1.md](../gates/o4-check-1.md) §2. SA L28229–28521; Y3 IV-55-9, IV-55-19, IV-56-17.

*Proof.* At fixed cutoff, let a cell have time faces \(c,c+l\). On raw functions above \(c\), put
\[
 \langle B,A\rangle_c=\rho(\overline{\theta_cB}A),\quad
 T_DA=D\tau_{le_4}A,\quad D^\sharp=\overline{\theta_{c+l/2}D},\quad
 K_D=T_{D^\sharp}T_D,\quad s_n=\langle A,K_D^nA\rangle_c.
\]
Reflection and translation give \(\langle B,T_DA\rangle_c=\langle T_{D^\sharp}B,A\rangle_c\). Moving these formal adjoints yields
\[
 s_{2r}=\|K_D^rA\|_c^2,\quad s_{2r+1}=\|T_DK_D^rA\|_c^2,
 \quad s_n^2\le s_{n-1}s_{n+1},\quad s_1^n\le s_0^{n-1}s_n.
 \tag{2.2}
\]
For odd indices use Cauchy–Schwarz on \(K_D^rA,K_D^{r+1}A\); for even indices use \(T_DK_D^{r-1}A,T_DK_D^rA\). If \(s_0=0\), the first pair already gives \(s_1=0\). Otherwise the last inequality follows from increasing positive ratios, with the zero case immediate.

The expanded \(s_n\) has two endpoint functions and \(2n\) alternating reflected copies of \(D\). Choose an aligned odd coarsening \(d=L^r\) enclosing \(A\) above \(c\), and let \(n\) run through multiples of \(d\). Endpoints lie in the coarse cells below \(c\) and above \(c+2nl\); the column occupies only intervening cells. Lemma 1 bounds the endpoints in their entirety by \(\|A\|_\infty\), and refines the column. With \(q_D=\liminf_\ell p_{l,\ell}(D)\),
\[
 0\le s_n\le\|A\|_\infty^2q_D^{2n}.
\]
Take volume limits first, then the \(n\)-th roots in (2.2), then \(n\to\infty\). The case \(q_D=0\) follows at any allowed \(n\ge2\). Cauchy–Schwarz gives
\[
 |\rho(\overline{\theta_cB}D\tau_{le_4}A)|\le q_D\|B\|_c\|A\|_c.
 \tag{2.3}
\]
Only now does the map descend to a bounded Hilbert operator. Outside degrees disappear with the endpoint root limit.

Next let \(h\) lie in the middle cube of sup-radius \(l/4\), \(l\le1\), initially \(a\le l/64\). The rooted count for a fixed cube \(Q\) is
\[
 \#\{X\supset Q:m(X)=m\}\le16\,8^{2m}2^{16(m+1)}.
 \tag{2.4}
\]
Indeed choose a corner of \(Q\), traverse each of the \(m\) tree edges twice with eight choices per step, and select the cubes incident to the at most \(m+1\) vertices. There are at most sixteen such cubes per vertex. Thus \(\kappa_D=22\log2\) works for this indexing; H-U includes any additional type entropy. Its strict decay gap gives, with \(\gamma_1>0\),
\[
 \sum_{X:X^+\cap B(u)\ne\varnothing,\ m(X)\ge t}e^{-\kappa m(X)}
 \le C(1+u/a_s)^4e^{-\gamma_1t},\qquad
 \sum_Xe^{-\kappa m(X)}\le C\ell^4a_s^{-4}.
 \tag{2.5}
\]
The first inequality counts possible root cubes in a fixed-layer enlargement of the ball; the second counts all roots. Tree traversal works on the torus quotient too.

Mirror-periodize \(zh\). Its norm is at most \(2|z|\|h\|_\sharp\), so \(|z|\|h\|_\sharp<r_{\rm src}\) is allowed. Retain every point term and each domain term whose whole dependence region lies inside a cell. Average these terms over cells, conjugating odd-cell values, to obtain a holomorphic \(E_{h,\ell}(z)\), zero at zero. On an odd cell this uses \(\overline{g(\bar z)}\), which is holomorphic. Locality and representation independence are needed here.

A discarded nonzero domain reaches a face from the middle support, hence \(m(X)\ge cl/a_s-C\). For \(a_s\ge l\), use the global bound (2.5) divided by \(N\); for \(a_s<l\), use its local bound once per source copy. The respective per-cell costs are
\[
 C_1(l/a_s)^4,\qquad C_2(1+l/a_s)^4e^{-\gamma' l/a_s},\quad\gamma'>0.
\]
Their sums, with the stability/floor cost, are at most
\[
 B_0=C_{\rm st}+\frac{C_1}{1-L^{-4}}
       +\frac{16C_2\,6!}{(\gamma')^6(1-L^{-2})}.
 \tag{2.6}
\]
For the fine scales use \((1+L^j)^4\le16L^{4j}\) and \(e^{\gamma'L^j}\ge(\gamma'L^j)^6/6!\). No scale is omitted. Thus
\[
 p_{l,\ell}(e^{z\mathcal O_a(h)-E_{h,\ell}(z)})\le e^{B_0}.
\]
At fixed cutoff the normalizers are uniformly locally bounded in \(\ell\), by the point bounds and the finite scale sum in (2.5). Cauchy bounds their Taylor coefficients. Diagonal selection of coefficients and the geometric Taylor-tail bound give a locally uniform holomorphic limit \(E_h\) along one torus subsequence, independent of every infinite-volume state. On that subsequence \(q_{e^{z\mathcal O_a(h)-E_h(z)}}\le e^{B_0}\).

For \(3\le l/a<64\), direct plaquette counting gives \(\|\mathcal O_a(h)\|_\infty\le12\cdot64^4\|h\|_\infty\); take \(E_h=0\). For \(l/a=1\), the middle cube contains no plaquette barycentre. Hence every allowed mesh ratio is covered by
\[
 Q_0=\max(e^{B_0},e^{12r_{\rm src}64^4}).
\]
Use (2.3) with \(D_z=e^{z\mathcal O_a(h)-E_h(z)}\) and apply Cauchy's formula at zero. Fixed-cutoff observables are bounded, so the expectation is holomorphic. This bounds insertion of \(\mathcal O_a(h)-E_h'(0)\) by \(Q_0\|h\|_\sharp/r_{\rm src}\) times the outside norms. Applying the same normalizer in state \(\nu\), with \(A=B=1\), bounds \(|\nu\mathcal O_a(h)-E_h'(0)|\) by the same scalar. The \(D=1\) case of (2.3) therefore gives
\[
 |\rho(\overline{\theta_cB}X_{a,\nu}(h)\tau_{le_4}A)|
 \le(2Q_0/r_{\rm src})\|h\|_\sharp\|B\|_c\|A\|_c.
 \tag{2.7}
\]
The possibly divergent normalizer derivative cancels.

For (2.1), choose \(l=L^{-i}\), \(y_*\in L^{-i-2}\mathbb Z^4\) with
\[
 \eta/(5L)<l\le\eta/5,\quad |y-y_*|_\infty\le l/(2L^2),\quad c=y_{*,4}-l/2.
\]
The support radius is below \(13l/72<l/4\), and \(|y_{*,4}|+l/2\le17\eta/72<\eta/4\). Put \(B=\tau_{2ce_4}F\), \(A=\tau_{-le_4}G\). When \(K_j\ge i+2\), the cell center is a lattice site, \(c\) a bond mirror, and both shifts are exact lattice translations. All plaquettes have the required positive margins for sufficiently large \(j\). Every norm and insertion tuple is fixed and separated. Thus (D.1) passes (2.7) to the limit. The two limiting norms are
\[
 \|e^{-(c+\eta/4)H}[\tau_{-(\eta/4)e_4}F]\|,
 \qquad
 \|e^{-(\eta/4-c-l)H}[\tau_{-(\eta/4)e_4}G]\|.
\]
Both times are positive. Contractivity proves (2.1), including null vectors. ∎

**Lemma 3 (PD, analytic density and compatible plates).** There is an operator-norm holomorphic density \(V_\eta\) on
\[
 |\Re z_4|+\sum_{j=1}^3|\Im z_j|<\eta/32,
 \qquad \|V_\eta(z)\|\le C_{\rm PD}\eta^{-5},
 \tag{3.1}
\]
such that, for compact \(C^1\) \(k\) supported in \(|t|<\eta/64\),
\[
 \sigma(\theta\bar F\cdot(k)\cdot G)
 =\int k(x)\langle\Phi,V_\eta(x)\Psi\rangle\,dx,
 \quad \Phi=[\tau_{-(\eta/4)e_4}F],\quad\Psi=[\tau_{-(\eta/4)e_4}G].
 \tag{3.2}
\]
Consequently this insertion extends to \(L^1\) strip tests, with bound \(C_{\rm PD}\eta^{-5}\|k\|_1\|\Phi\|\|\Psi\|\). Define
\[
 V_{\varphi,\eta}(t,u)=\int\varphi(z)V_\eta(t,u,z)\,dz,\qquad
 B_{\varphi;a}=V_{\varphi,4a}(0,0),\quad0<a\le1/4.
\]
For \(\varphi\in L^1(\mathbb R^2)\),
\[
 \|B_{\varphi;a}\|\le Ca^{-5}\|\varphi\|_1,\qquad
 B_{\varphi;b}=e^{-(b-a)H}B_{\varphi;a}e^{-(b-a)H}\quad(a<b\le1/4).
 \tag{3.3}
\]
Real labels give self-adjoint plates. In particular the plate insertion bound has exponent \(\wp=p_I+5=5\), independent of outside degrees.

*Origin:* [pd-port.md](pd-port.md) §§2–4; [o4-check-1.md](../gates/o4-check-1.md) §3. SA L28527–28882. The three-dimensional point-density analogue is Y3 L76400–76490; the parametrix below is four-dimensional.

*Proof.* Lemma 2 applied to outside polynomials shifted forward by \(\eta/4\) gives a bounded form. It kills null vectors and represents an operator \(B_{h,\eta}\) with
\[
 \|B_{h,\eta}\|\le C\|h\|_\sharp,\qquad
 B_{h,\eta}[A]=[(\tau_{(\eta/4)e_4}h)\cdot\tau_{(\eta/2)e_4}A].
 \tag{3.4}
\]
Pairing with every polynomial class and translating once proves the identity; the displayed supports are separated. For the joint spectral measure set
\[
 T(z)=\int e^{-z_4E+i\mathbf z\cdot\mathbf q}\,d\Pi(E,\mathbf q).
\]
The cube cone gives contraction when \(\Re z_4\ge\sum|\Im z_j|\). On a strict margin \(\delta>0\), derivatives of order \(m\) have norm at most \(\sup E^me^{-\delta E}\le m!\delta^{-m}\). The spectral Taylor series thus converges in operator norm on smaller neighborhoods.

For \(h\) supported in \(B(0,c_I\eta/2)\), put
\[
 M_{h,\eta}(z)=T(\eta e_4/8+z)B_{h,\eta/2}T(\eta e_4/8-z).
 \tag{3.5}
\]
It is holomorphic and bounded by \(C\|h\|_\sharp\) on the tube with margin \(\eta/8\). Substitution of (3.4), spatial covariance, and one common time translation give
\(\sigma(\theta\bar F\cdot(\tau_xh)\cdot G)=\langle\Phi,M_{h,\eta}(x)\Psi\rangle\) for real \(|x_4|<\eta/8\). Only positive time semigroups occur.

In \(\mathbb R^4\) set \(G_0(x)=-|x|^2\log|x|/(64\pi^2)\), \(G_0(0)=0\). This is \(C^1\). Radial differentiation gives \(\Delta(|x|^2\log|x|)=8\log|x|+6\) and \(\Delta\log|x|=2|x|^{-2}\). Integration outside a shrinking ball gives boundary errors \(O(\varepsilon^4|\log\varepsilon|)\) and \(O(\varepsilon^2)\). For \(|x|^{-2}\) the remaining flux is \(-2|S^3|f(0)=-4\pi^2f(0)\); its other boundary term tends to zero. Therefore \(\Delta^3G_0=\delta_0\).

Choose real \(\chi\in C_c^\infty(B_1)\), equal to one near zero. Let \(n=\chi G_0\), \(s=\delta_0-\Delta^3n\). All uncancelled terms differentiate \(\chi\) away from zero, so \(s\) is smooth and compact. For \(0<r\le1\),
\[
 n_r(x)=r^2n(x/r),\quad s_r(x)=r^{-4}s(x/r),\quad
 \Delta^3n_r=\delta_0-s_r,\quad
 \|n_r\|_\sharp\le Cr,\quad\|s_r\|_\sharp\le Cr^{-5}.
 \tag{3.6}
\]
The scaled logarithm is \(\log(|x|/r)\); there is no extra \(|\log r|\) loss. Convolution gives \(k=(\Delta^3k)*n_r+k*s_r\), first distributionally and then pointwise.

Set \(r=\epsilon\eta\) in (3.6) and \(V_\eta=\Delta_z^3M_{n_r,\eta}+M_{s_r,\eta}\). A polydisc of radius \(\eta/128\) around any point of the smaller tube in (3.1) lies in the tube of (3.5). Six Cauchy derivatives cost \(6!(128/\eta)^6\), and the sum of coefficients of \(\Delta^3\) is \(4^3\). Hence
\[
 \|V_\eta\|\le C(\eta^{-6}r+r^{-5})\le C_{\rm PD}\eta^{-5}.
\]
For smooth compact \(k\) in the stated strip, convolution Riemann sums converge in \(C^1\) with common compact support between the outside fields. Local continuity passes the insertion through the integrals. Integrating six derivatives off \(k\) gives (3.2), with positive sign and no boundary terms. Mollification proves it for compact \(C^1\) tests; \(L^1\) density gives its unique continuous extension. Any two parametrices have continuous matrix-element differences integrating to zero against every smooth test. Their densities agree pointwise, then holomorphically on overlaps.

Transverse integration gives \(V_{\varphi,\eta}\); uniform local Taylor estimates justify holomorphy and integration term by term. The bound is \(C\eta^{-5}\|\varphi\|_1\), with unrestricted real \(u\). A plane approximate identity converges to \(B_{\varphi;a}\) in operator norm by this continuity. For smooth insertions, a common time translation gives the padding identity (3.3). Pass to the plane-point limit and then approximate any \(L^1\) label by smooth compact labels. The same argument gives
\[
 V_{\varphi,4a}(t,u)
 =T((a-a'+t)e_4+ue_1)B_{\varphi;a'}T((a-a'-t)e_4-ue_1)
 \tag{3.7}
\]
for \(0<a'<a\), \(|t|<a/16\), \(a-a'>|t|\). Reflect a real time-even plane approximate identity, conjugate the matrix element and translate; this proves self-adjointness for real labels. No unsandwiched point operator has been postulated. ∎

## Angular kernels

**Lemma 4 (AK, kernels, band and cut).** For each \(n\), the compatible plates give holomorphic product kernels, norm removal of plane smoothing and one glued kernel \(\mathcal K_n\) on a connected domain \(U_n\). On distinct real planar configurations there are real-analytic harmonic coefficients \(c_m\) with
\[
 c_m(R_tY)=e^{4imt}c_m(Y),\quad c_{-m}=\overline{c_m},\quad
 4|m|\le5n.
 \tag{4.1}
\]
They sum to the moment density on ordinary ordering charts. Let \(M(n)\) be the largest occurring \(|m|\) over all real labels, or zero if none occurs, and \(M(0)=M(1)=0\). The coefficients give positive boosted Gram matrices, top-coefficient positivity across any oriented line up to its fixed phase, and
\[
 2M(k+l)\le M(2k)+M(2l)\qquad(k,l\ge0).
 \tag{4.2}
\]

*Origin:* [ak-port.md](ak-port.md) §§1–9; [o4-check-2.md](../gates/o4-check-2.md) §1. SA L28888–29916. The distinct-point restriction and compact \(C^1\) profile condition are explicit here.

*Proof.* In the plane, the spectral multiplier of \(T(v)\) is \(e^{-v_+E_--v_-E_+}\), with \(E_\pm=(E\pm q)/2\ge0\). Thus
\[
 \|T(v)\|\le1,\quad T(v)^*=T(v^*),\quad T(v)T(w)=T(v+w),\quad T(v)\Omega=\Omega.
\]
It is strongly continuous on the closed tube by dominated convergence. On \(\Re v_\pm\ge r>0\), its Taylor coefficient of degree \((j,k)\) has norm at most \(r^{-j-k}\), since \(x^je^{-x}/j!\le1\). This proves norm holomorphy.

Choose \(0<a\le1/4\), \(2a<\min r(v_i)\), and define
\[
 K_n(v;\vec\varphi)=\langle\Omega,B_{\varphi_1;a}T(v_1-2ae_0)B_{\varphi_2;a}
 \cdots T(v_{n-1}-2ae_0)B_{\varphi_n;a}\Omega\rangle.
 \tag{4.3}
\]
For a positive ordered configuration, also take \(a<r(x_1)\) and set
\[
 \Psi(\mathbf x;\vec\varphi)=T(x_1-ae_0)B_{\varphi_1;a}
 \prod_{i=1}^{n-1}[T(x_{i+1}-x_i-2ae_0)B_{\varphi_{i+1};a}]\Omega.
 \tag{4.4}
\]
Products are written in increasing index from left to right. Replacing padding \(b\) by \(a<b\) in (3.3) turns each internal translation into
\((b-a)e_0+(v-2be_0)+(b-a)e_0=v-2ae_0\). The leftmost factor in (4.4) becomes \(T(x_1-ae_0)\), and final semigroups fix \(\Omega\). Thus the definitions are independent of padding. Fixed local padding proves holomorphy. With \(\delta=\min(1,\min_i r(v_i))\), choose \(a=\delta/4\):
\[
 |K_n(v;\vec\varphi)|\le\prod_i(4^5C\|\varphi_i\|_1)\,\delta^{-5n}.
 \tag{4.5}
\]
The vector bound includes \(r(x_1)\) in the minimum. Set \(K_0=1\), \(\Psi(\varnothing)=\Omega\); \(K_1\) is the position-independent vacuum expectation, zero for a self-centered field.

For a unit-mass plane bump \(\beta_\varepsilon\) of support radius \(\varepsilon<a/16\),
\[
 B_a[\beta_\varepsilon,\varphi]=\int\beta_\varepsilon(y)V_{\varphi,4a}(y)\,dy
 \longrightarrow B_{\varphi;a}
\]
in operator norm. Its action on \([G]\) is \([(\tau_{ae_0}(\beta_\varepsilon\otimes\varphi))\cdot\tau_{2ae_0}G]\), by pairing and translation. Substitution in (4.4) from right to left places the centers at \(x_i\). Telescoping finite products proves convergence uniformly on compact tube subsets, even with different shrinkage rates in different entries. For compact \(C^1\) plane profiles with strictly ordered time supports, integrate these identities and pass by \(C^1\) continuity of convolution and norm convergence. This proves
\[
 \sigma((\alpha_i\otimes\varphi_i)_i)
 =\int\prod_i\alpha_i(y_i)\,K_n(y_2-y_1,\ldots,y_n-y_{n-1};\vec\varphi)\,d\mathbf y.
 \tag{4.6}
\]
A common time translation removes any lower-time restriction.

For \(\nu\in\{0,\pi/2,\pi,3\pi/2\}\) and permutation \(\rho\), set
\[
 U_{\nu,\rho}=\{\mathbf z:R_{-\nu}(z_{\rho(i+1)}-z_{\rho(i)})\in\mathbb V\},
 \quad K^{\nu,\rho}=K_n(R_{-\nu}\partial(\rho\mathbf z);\rho\vec\varphi).
\]
Each overlap is convex and contains the real part of each of its points. On a real overlap, small bumps preserve both orders. Equation (4.6), symmetry and hypercubic invariance identify both densities. Shrinking the bumps gives equality there. A holomorphic function vanishing on a real open ball has zero Taylor series; continuation through overlapping balls gives equality throughout the overlap. The kernels therefore glue on \(U_n=\bigcup U_{\nu,\rho}\). Every time-order chart meets every spatial-order chart, because both orders can be prescribed independently at real points. The other frames reverse these orders. Thus \(U_n\) is connected, with real locus
\(\operatorname{Ord}_n=\{\text{all times distinct or all abscissae distinct}\}\).
The glued kernel inherits translations, labelled permutations, reality and quarter turns by the same uniqueness argument.

For positive ordered configurations \(\mathbf x,\mathbf y\) of lengths \(k,l\), let
\[
 J(\mathbf x,\mathbf y)=((x_k-x_{k-1})^*,\ldots,(x_2-x_1)^*,x_1^*+y_1,
 y_2-y_1,\ldots,y_l-y_{l-1}).
\]
Reverse the left labels, and conjugate them if complex. Taking the adjoint of (4.4) with a common padding gives
\[
 K_{k+l}(J(\mathbf x,\mathbf y))=\langle\Psi(\mathbf x),\Psi(\mathbf y)\rangle.
 \tag{4.7}
\]
For an empty side omit its list and the central entry; both empty gives one. Since \((R_zv)_\pm=e^{\pm iz}v_\pm\), imaginary rotations preserve the tube and commute with star. Applying (4.7) to \(R_{is}\mathbf x,R_{is}\mathbf y\) proves positivity of the boosted kernel for all real \(s\), all finite families and mixed lengths. This is a vector Gram identity, not continuation of a scalar inequality.

For a pencil, choose a nearest quarter turn to \(\Re z\). Every rotated difference has light margins at least \(r_0\cos(3\pi/8)e^{-|\Im z|}\), with \(r_0\) the smallest consecutive length. Thus \(a_Y(z)=\mathcal K_n(R_zY)\) is entire, \(\pi/2\)-periodic, and bounded by \(A_{Y,\vec\varphi}e^{5n|\Im z|}\). Moving its Fourier integral to height \(s\) gives
\[
 |c_m(Y)|\le A_{Y,\vec\varphi}e^{4ms+5n|s|}.
\]
Choose \(s\to-\infty\) for \(4m>5n\), or \(s\to+\infty\) for \(4m<-5n\). These coefficients vanish. The entire periodic function descends under \(w=e^{4iz}\) to a holomorphic function on \(\mathbb C\setminus\{0\}\); its Laurent series is therefore the remaining finite sum.

To extend coefficients beyond pencils, put \(N=\lfloor5n/4\rfloor\),
\[
 \mathcal L=\sum_i(-z_i^1\partial_{z_i^0}+z_i^0\partial_{z_i^1}),\quad
 P(X)=\prod_{j=-N}^N(X-4ij),\quad
 p_m(X)=\prod_{\substack{-N\le j\le N\\j\ne m}}\frac{X-4ij}{4im-4ij}.
\]
The finite band gives \(P(\mathcal L)\mathcal K_n=0\) on pencils, hence on connected \(U_n\). Define \(c_m=p_m(\mathcal L)\mathcal K_n\). Interpolation gives
\[
 \sum_m c_m=\mathcal K_n,\quad \mathcal Lc_m=4imc_m,\quad
 \mathcal K_n(R_{is}\mathbf z)=\sum_m e^{-4ms}c_m(\mathbf z).
 \tag{4.8}
\]
The last equality solves the angular differential equation; imaginary rotations preserve every chart. Real rotation gives the phase in (4.1) while the path stays ordinary. Total derivatives annihilate translation-invariant kernels, so the projectors preserve translation invariance. Conjugating their coefficients gives \(c_{-m}=\bar c_m\) on real points.

Distinct planar configurations with no perpendicular pair of nonzero differences form a dense open set: the excluded equations are finitely many nonzero polynomial equations, nonzero at distinct collinear points. On a line segment to such a point the product polynomial has only finitely many zeros, proving density. Every rotation of these configurations is ordinary. For any other distinct configuration choose an angle \(t\) giving distinct rotated times; only finitely many angles are forbidden. Define locally \(\widetilde c_m(Y)=e^{-4imt}c_m(R_tY)\). Different choices agree on the dense set, hence on overlaps by continuity. These real-analytic coefficients obey (4.1) globally and agree with the original ones on ordinary configurations. We henceforth omit the tilde.

For real positive-half-plane configurations with distinct points in each tuple define
\[
 G_s(\mathsf x,\mathsf y)=\sum_m e^{-4ms}c_m^{(k+l)}(\theta\mathbf x,\mathbf y;\vec\varphi,\vec\psi).
 \tag{4.9}
\]
The combined reflected configuration is distinct because its groups lie on opposite sides. Sorting distinct times identifies (4.9) with (4.7). Perturb time ties within the half-plane and pass to the limit in each finite matrix; positivity is preserved. The empty tuple remains included. For fixed length \(k\), multiply by \(e^{-4M(2k)s}\) and send \(s\to+\infty\). This gives positivity of the top kernel \(H=c_{-M(2k)}^{(2k)}\). Across a line with normal \(R_\nu e_0\), its positive kernel is \(e^{4iM(2k)\nu}H(\theta_\ell X,Y)\). In particular,
\[
 |H(\theta_\ell X,Y)|^2\le|H(\theta_\ell X,X)|\,|H(\theta_\ell Y,Y)|.
 \tag{4.10}
\]

If \(M(k+l)>0\), a negative-top coefficient is nonzero on some pencil, by reality and holomorphic uniqueness. Split after its first \(k\) points, translate the cut to time zero, and reflect and reverse the left group. Cauchy–Schwarz for (4.9) compares a nonzero leading rate \(e^{8M(k+l)s}\) with a right-hand rate at most \(e^{4(M(2k)+M(2l))s}\). This proves (4.2). For an empty side translate the whole pencil into positive time and use \(\Omega\), whose diagonal entry is one. If the left degree is zero the inequality is immediate.

Finally (3.3) gives norm convergence under \(L^1\) label approximation. Cauchy estimates give convergence of the finite projector derivatives. Every identity and positive matrix therefore extends to \(L^1\) labels; a nonzero coefficient remains nonzero at some smooth approximation. The definition of \(M(n)\) is unchanged. ∎

## Two-point elimination

**Lemma 5 (TU10 gives strict endpoint decay).** For each real compact \(C^1\) transverse label \(\varphi\), the connected equal-label kernel has a positive axis measure \(\mu\) supported on \(\mathcal C=\{E\ge|q|\}\), with
\[
 G(t,x)=\int e^{-tE+ixq}\,d\mu,\quad
 \Gamma(t)=G(t,0)<\infty\ (t>0),\quad
 |G(y)|\le\Gamma(|y|/\sqrt2),\quad
 t^8\Gamma(t)\longrightarrow0.
 \tag{5.1}
\]

*Origin:* [tu-port.md](tu-port.md) §§2–3; [o4-check-2.md](../gates/o4-check-2.md) §2. SA L29939–30266 supplies the interface and an alternative dilation proof. The low-energy mass proof below is the checked local replacement.

*Proof.* In the coordinate Hilbert space put \(\zeta_{\varphi,a}=(1-P_\Omega)B_{\varphi;a}\Omega\). The vacuum projection commutes with translations. The padding identity gives \(\zeta_{\varphi,b}=e^{-(b-a)H}\zeta_{\varphi,a}\). Hence
\[
 d\mu=e^{2aE}\,d\langle\zeta_{\varphi,a},\Pi(E,q)\zeta_{\varphi,a}\rangle
\]
is independent of \(a\), positive and cone-supported. For any \(t>0\), choose \(0<a<\min(t/2,1/4)\) in (4.3). This proves the spectral representation and finiteness. Vacuum subtraction removes precisely \(\sigma(f)\sigma(h)\); it needs no unique vacuum.

The two-point density formula holds for arbitrary disjoint planar supports. Partition each into pieces of diameter below one quarter of their mutual distance \(d\). Each pair has coordinate separation at least \(d/\sqrt2\) at selected points, and at most \(d/2\) is lost across the two pieces. Thus one signed coordinate orders each pair, and (4.6) applies in that frame. Summing proves the formula. Shrinking bumps passes the inherited symmetries to the continuous kernel. A quarter turn makes the positive time coordinate at least \(|y|/\sqrt2\); the spectral bound and monotonicity of \(\Gamma\) give the third assertion of (5.1).

For a plane profile \(\alpha\) supported at time at least \(\delta>0\), connected reflection positivity and Fubini give
\[
 \|[\alpha\otimes\varphi]\|_T^2
 =\int\left|\int\alpha(t,x)e^{-tE+ixq}\,dt\,dx\right|^2d\mu.
 \tag{5.2}
\]
The absolute integral before interchange is at most \(\|\alpha\|_1^2\Gamma(2\delta)\). Here \(\|\cdot\|_T\) is the connected reflection seminorm: subtract the vacuum vector in the relevant reflection space. It has the triangle inequality.

We verify every shape used in H-T. Let \(a_0\) be one on \([9/4,11/4]\), zero outside \([17/8,23/8]\), with cubic ramps \(3s^2-2s^3\) on the two intervening intervals. Let
\[
 b_0(s)=(1-3s^2+2|s|^3)1_{|s|\le1}.
\]
Both are \(C^1\); direct integration gives \(\int a_0=5/8\), \(\|a_0'\|_\infty\le12\), \(\int b_0=1\), \(\|b_0'\|_\infty\le3/2\). Also \(b_0(s)+b_0(1-s)=1\) on \([0,1]\), so its integer translates sum to one. Let \(\rho_0\) be one on \([-1,1]\), zero outside \([-3/2,3/2]\), with cubic ramps. Then \(\int\rho_0=5/2\), \(\|\rho_0'\|_\infty\le3\). Set
\[
 \psi(z)=b_0(z_1)b_0(z_2),\qquad
 \widetilde\psi(z)=\rho_0(z_1)\rho_0(z_2).
\]
They have gradient bounds \(3,6\), \(\psi\le\widetilde\psi\), and \(\int\widetilde\psi=25/4\).

For \(\varphi\ne0\), choose \(R\ge1\) with \(\operatorname{supp}\varphi\subset B(0,R)\), and \(0<h\le\min(1,2d_0/5)\). Define
\[
 \alpha_h(t,x)=a_0(t/h)b_0(4x/h),\quad
 A=\|\varphi\|_\infty+h\|\nabla\varphi\|_\infty,
\]
\[
 \psi_i(z)=\psi(z/h-i),\quad \widetilde\psi_i(z)=\widetilde\psi(z/h-i),\quad
 f_i^-=\alpha_h\otimes2A\widetilde\psi_i,\quad
 f_i^+=\alpha_h\otimes(2A\widetilde\psi_i+\psi_i\varphi).
\]
Keep the \(N\le(2R/h+3)^2\le25R^2h^{-2}\) indices with \(\psi_i\varphi\ne0\). Then \(\alpha_h\otimes\varphi=\sum_i(f_i^+-f_i^-)\), and the transverse factors lie between \(A\widetilde\psi_i\) and \(3A\widetilde\psi_i\). Thus \(A\le\|f_i^\pm\|_\infty\le3A\).

Put \(d=5h/2\). The four support half-widths are \(3h/8,h/4,3h/2,3h/2\); their squared sum is \(301h^2/64<5h^2<d^2\). Each support fits in a radius-\(d\) ball centered at \((5h/2,0,hi)\). Its distance from its time reflection lies between \(4h\) and \(6h\), hence in \([d,6d]\). Direct product integration and differentiation give
\[
 \int f_i^\pm\ge\frac{125}{128}Ah^4
 \ge\frac1{120}\|f_i^\pm\|_\infty d^4,
 \quad \operatorname{Lip}f_i^\pm\le70A/h
 \le\frac{\|f_i^\pm\|_\infty}{\vartheta_*d}.
 \tag{5.3}
\]
The derivative coefficient is \(3(12+6)+12+3+1=70\). The reflected tests have the same norms and integrals. Thus H-T applies to \((\theta f_i^\pm,f_i^\pm)\), and the triangle inequality gives
\[
 \|[\alpha_h\otimes\varphi]\|_T^2\le(6NA)^2u(5h/2).
 \tag{5.4}
\]

Restrict (5.2) to \(E\le1/h\). The cone gives \(|q|\le1/h\), so evenness of \(b_0\) and \(\cos(xq)\ge1/2\) on \(|x|\le h/4\) bound the spatial transform below by \(h/8\). The time transform is at least \((h/2)e^{-3}\). If \(m_\mu(Q)=\mu\{E\le Q\}\), then
\[
 \frac{e^{-6}}{256}h^4m_\mu(h^{-1})\le\|[\alpha_h\otimes\varphi]\|_T^2,
 \quad m_\mu(Q)\le C_\varphi Q^8u(5/(2Q))=o(Q^8),
 \tag{5.5}
\]
where one may take \(C_\varphi=256e^6[150R^2(\|\varphi\|_\infty+\|\nabla\varphi\|_\infty)]^2\). Local finiteness follows independently from \(m_\mu(Q)\le e^Q\Gamma(1)\).

Tonelli gives \(\Gamma(t)=t\int_0^\infty e^{-tQ}m_\mu(Q)\,dQ\). For any \(\varepsilon>0\), choose \(Q_\varepsilon\) above which \(m_\mu(Q)\le\varepsilon Q^8\). Thus
\[
 t^8\Gamma(t)\le t^9Q_\varepsilon m_\mu(Q_\varepsilon)+8!\varepsilon.
\]
The factorial follows by eight integrations by parts. First let \(t\downarrow0\), then \(\varepsilon\downarrow0\). This proves (5.1); the zero label is immediate. ∎

**Theorem 6 (TU, all nonconstant two-point harmonics vanish).** Under the imports, \(M(2)=0\), including the critical angular frequencies \(\pm8\).

*Origin:* [tu-port.md](tu-port.md) §§4–6; [o4-check-2.md](../gates/o4-check-2.md) §2. SA L30268–30502. The use of the finite band on the imaginary axis is the checked local shortening.

*Proof.* For a real equal label and \(r>0\), Lemma 4 gives
\[
 g_r(z)=G(R_z(r,0))=\sum_{m=-2}^2a_m(r)e^{4imz}.
\]
At complex arguments this denotes the analytic continuation. On the imaginary axis the spectral formula and cone give
\[
 0\le g_r(is)=\int e^{-r(E\cosh s+q\sinh s)}d\mu
 \le\Gamma(re^{-|s|})=o(e^{8|s|}).
\]
Divide by \(e^{8s}\) as \(s\to+\infty\), and by \(e^{-8s}\) as \(s\to-\infty\), to kill \(a_{-2}\) and \(a_2\). Reality and spatial reflection then give
\[
 g_r(z)=c_0(r)+2c_1(r)\cos4z,\qquad c_0,c_1\in\mathbb R.
 \tag{6.1}
\]
A mere bounded \(u\) would not have removed the critical modes.

Put \(D(t,x)=G(R_{\pi/4}(t,x))\). Diagonal reflection positivity, applied to mollified points with transverse label \(\varphi\), and connected vacuum subtraction imply positivity of
\[
 \langle e_{t,x},e_{u,v}\rangle_D=D(t+u,v-x),\qquad t,u>0.
 \tag{6.2}
\]
The reflected planar pairs stay separated, so the density formula and continuity justify the point limit. On finite sums define \(T_s e_{t,x}=e_{t+s,x}\), \(U_b e_{t,x}=e_{t,x+b}\). The latter preserve the form; the former are symmetric and commute with them. Lemma 5 bounds every time orbit of \(v=\sum c_ie_{t_i,x_i}\) by
\(B_v=\Gamma(\sqrt2\min_i t_i)^{1/2}\sum|c_i|\). Moreover
\[
 \|T_sv\|^2=\langle v,T_{2s}v\rangle_D\le\|v\|\,\|T_{2s}v\|.
\]
Null vectors remain null. Iterating gives \(\|T_sv\|\le\|v\|^{1-2^{-k}}B_v^{2^{-k}}\), hence contraction. The completed operators are self-adjoint and positive, since \(T_s=T_{s/2}^2\). Continuity of \(D\) gives strong continuity on point vectors, then on the completion. If \(T_1v=0\), positivity successively gives \(T_{1/2^k}v=0\); strong continuity forces \(v=0\). Spectral calculus defines \(H_D=-\log T_1\ge0\); uniqueness of positive roots gives \(T_s=e^{-sH_D}\) first at rational times and then at every time. The unitary group gives \(P_D\), strongly commuting with \(H_D\).

With its joint spectral measure define \(d\nu=e^{2aE}d\langle e_{a,0},\Pi_D(E,q)e_{a,0}\rangle\). The shift of \(e_{a,0}\) makes this independent of \(a\), and for \(t>0\),
\[
 D(t,x)=\int e^{-tE+ixq}d\nu,\quad\nu\ge0,\quad
 \int e^{-tE}d\nu=D(t,0)<\infty.
 \tag{6.3}
\]
At this stage only \(E\ge0\) is known for \(\nu\), not a diagonal cone.

We use Fourier–Laplace uniqueness. Equality of such transforms for real \(t>0,x\) extends, by exponential domination and the identity theorem, to \(t=a+i\tau\). These are the Fourier transforms of finite measures weighted by \(e^{-aE}\). Their difference is zero: convolve with a Gaussian, use its Fourier integral and Fubini, then let its width decrease to zero against compact continuous tests. Removing the positive weight proves uniqueness, also for positive linear combinations.

Let
\[
 L_s(E,q)=(E\cosh s+q\sinh s,E\sinh s+q\cosh s),\quad
 \mu_s=(L_s)_*\mu,\quad C=\cosh4>1.
\]
These maps preserve the axis cone, satisfy \(L_sL_t=L_{s+t}\), and give \(E_s\ge e^{-|s|}E\), so all Laplace weights remain finite. Direct multiplication of the rotation matrix shows
\[
 \int e^{-tE+ixq}d\mu_s=G(R_{is}(t,x))=g_r(\theta+is),
 \qquad (t,x)=R_\theta(r,0),\quad t>0.
\]
Indeed \(R_{is}(t,x)=(t\cosh s-ix\sinh s,x\cosh s+it\sinh s)\), whose multiplier is \(e^{-tE_s+ixq_s}\). The constant and two exponential terms in (6.1) each obey
\[
 (C-1)g_r(\theta+\pi/4)+g_r(\theta+i)+g_r(\theta-i)=(C+1)g_r(\theta).
\]
Transform uniqueness therefore gives
\[
 (C-1)\nu+\mu_1+\mu_{-1}=(C+1)\mu,\qquad
 0\le\nu\le\frac{C+1}{C-1}\mu.
 \tag{6.4}
\]
This derives the diagonal cone. Integrate (6.4) against \(w_s=e^{-r(E\cosh s+q\sinh s)}\). Its integrability follows from the domination and the group law. The sum of the shifted coshes is \(2C\cosh4s\), so
\[
 \int w_s\,d\mu=c_0+2c_1\cosh4s\ge0,\qquad
 \int w_s\,d\nu=c_0-2c_1\cosh4s\ge0.
\]
Dividing by \(\cosh4s\) and taking \(s\to\infty\) forces both \(c_1\ge0\) and \(c_1\le0\). Thus equal-label kernels are radial. Symmetry and a half turn imply \(G_{\varphi,\psi}=G_{\psi,\varphi}\), whence
\[
 G_{\varphi,\psi}=\tfrac14(G_{\varphi+\psi,\varphi+\psi}-G_{\varphi-\psi,\varphi-\psi}).
\]
Mixed real labels are radial; complex labels follow by bilinearity, and \(L^1\) labels by Lemma 4's continuity. The full two-point kernel differs from the connected one only by the position-independent product of means, which adds no nonconstant harmonic. Hence \(M(2)=0\). ∎

## All-order closure

**Lemma 7 (polygon divisibility and discrete convexity).** The degrees of Lemma 4 satisfy
\[
 k\mid2M(2k),\qquad M(2k)=kM(2),\qquad 2M(n)\le nM(2).
 \tag{7.1}
\]
In particular Theorem 6 makes every degree zero.

*Origin:* [ac-port.md](ac-port.md) §§2–3; [o4-check-2.md](../gates/o4-check-2.md) §3. SA L30582–30685; Y3 IV-37-27, L76854–76913.

*Proof.* If \(M(2k)=0\), divisibility is immediate; it is also immediate for \(k=1\). Otherwise suppose it fails and put \(H=c_{-M(2k)}^{(2k)}\). Give every vertex of a regular \(2k\)-gon the same real label \(\varphi\). Rotation through \(\pi/k\) permutes the labelled vertices, while (4.1) multiplies \(H\) by \(e^{-4\pi iM(2k)/k}\ne1\). Its value is therefore zero.

Call a labelled set zero if every distinct \(2k\)-point completion has zero \(H\), with arbitrary real remaining labels. Suppose such a set \(S\) lies in \(\theta_\ell Q\cup Q\), with reflected labels matched, \(|Q|=j\le k\), and all points of \(Q\) strictly on one side of the line. Add any \(k-j\) points \(A\) on that side, with arbitrary labels. The diagonal for \(Q\cup A\) contains \(S\), so (4.10) makes its whole row zero:
\[
 H(\theta_\ell(Q\cup A),B)=0
 \tag{7.2}
\]
for every \(k\)-point \(B\) on the same side. Fix the free labels. The free positions in (7.2) vary in a nonempty open subset of their collision-free configuration space, avoiding the fixed \(\theta_\ell Q\). This space is connected: move points individually through auxiliary positions, avoiding the finite occupied set; choose each bend outside the finitely many forbidden lines. Real analyticity extends (7.2) throughout this space. Thus \(\theta_\ell Q\) is itself zero, with unrestricted other labels and positions. This releases labels as well as positions.

An edge-bisector reflection first reduces the full polygon to a consecutive arc of \(k\) vertices. For an arc \(0,\ldots,j-1\), \(2\le j\le k\), use the index reflection \(i\mapsto j-1-i\) if \(j\) is even, and \(i\mapsto j-i\) if \(j\) is odd, modulo \(2k\). In the odd case include vertex \(j\) in the reflected union. Both index sums are odd, so no polygon vertex is fixed. A half arc of \(\lceil j/2\rceil\) consecutive vertices lies strictly on one side. The reduction applies and eventually leaves one point with label \(\varphi\). Translation moves it anywhere. Since \(\varphi\) was arbitrary and all completion labels were released, \(H\) vanishes identically. This contradicts its definition as a nonzero top coefficient and proves divisibility.

Set \(a_k=M(2k)\), \(a_0=0\). The cut with lengths \(k-1,k+1\) gives
\[
 2a_k\le a_{k-1}+a_{k+1},\qquad 0\le a_k\le5k/2.
\]
The increments \(d_k=a_k-a_{k-1}\) are nondecreasing nonnegative integers. An increment at least three would persist and violate the linear bound for sufficiently large \(k\). Thus \(d_k\in\{0,1,2\}\), eventually a fixed integer \(d\). Put \(D=\sum_{j\ge1}(d-d_j)\ge0\); the sum is finite, and eventually \(a_k=dk-D\). Divisibility says every sufficiently large \(k\) divides \(2D\). Choose such a \(k>2D\); then \(D=0\). Every summand is nonnegative, so all increments equal \(d=a_1=M(2)\). The empty-tuple cut gives \(2M(n)\le M(2n)=nM(2)\). This proves (7.1). ∎

**Lemma 8 (local translations remove exceptional support).** If all degrees vanish, the moment distributions are invariant under rotations in the chosen plane, including configurations with equal planar projections but distinct transverse positions. This invariance passes to separated compact \(C^1\) tuples and to \(\Sigma_n\).

*Origin:* [ac-port.md](ac-port.md) §§4–6; [o4-check-2.md](../gates/o4-check-2.md) §3. SA L30687–30860. H-S is needed only in the last paragraph.

*Proof.* First split a compact separated tuple at a strict coordinate cut \(x_j=0\), writing its two products as \(F_-,F_+\). Take \(a,b>0\) below their distances from the cut and define
\[
 \Phi=[\tau_{-ae_j}\theta_j\overline{F_-}],\quad
 \Psi=[\tau_{-be_j}F_+],\quad d=a+b.
\]
The Hilbert translation dictionary gives, for small real \(z\),
\[
 \sigma(F_-\cdot\tau_zF_+)
 =\langle\Phi,e^{-(d+z_j)H_j}U_{z_\parallel}\Psi\rangle.
 \tag{8.1}
\]
Indeed reflection of the first vector translates \(F_-\) by \(ae_j\), and the second becomes \(\tau_{ae_j+z}F_+\); common translation cancels. For a real vector \(v\), (8.1) with \(z=sv\) is holomorphic whenever
\[
 \eta_s=d+v_j\Re s-\sum_{r\ne j}|v_r||\Im s|>0.
 \tag{8.2}
\]
The cube cone bounds the multiplier by \(e^{-\eta_sE}\). On a smaller neighborhood with \(\eta_s\ge\varepsilon>0\), the derivative of order \(q\) is bounded by \((\sum|v_r|)^q q!\varepsilon^{-q}\). The spectral Taylor series converges in operator norm. No complex translation of a test function is assumed.

For a planar angle \(u\), let \(D_u=T_n-R_u^*T_n\), meaning
\[
 D_u(f_1\otimes\cdots\otimes f_n)=\sigma(f_1,\ldots,f_n)-\sigma(R_uf_1,\ldots,R_uf_n).
 \tag{8.3}
\]
At a configuration with all original and rotated times distinct, choose product boxes preserving both orders. Smooth slot tests there admit finite plate approximations in \(C^1\). To see this, extend a compact smooth test periodically inside a larger product box, expand in Fourier series and multiply by fixed product cutoffs equal to one near its support. Repeated integration by parts gives coefficient bounds \(C_N(1+|q|)^{-N}\). In \(D\) variables, derivative order \(r\) has a convergent shell sum \(\sum_{j\ge1}j^{D+r-1-N}\) when \(N>D+r\). Each term factors between plane and transverse variables. This proves the required approximation, and with \(D=4n\) also proves local density of slot tensors in the smooth test topology. Since the only harmonic is \(c_0\), (4.6) and local \(C^1\) continuity give \(D_u=0\) on this ordinary open set.

Fix any \(y\in\mathcal C_n\). In each coordinate take threshold cuts halfway between successive distinct coordinate levels of the points. These finitely many cuts together separate every pair, and no point lies on a cut. Choose a product neighborhood \(W\) and \(0<u_0<\pi/3\) such that each cut has the same index partition for \(x\) and \(R_ux\), throughout \(W\), whenever \(|u|<u_0\). Bounding displacement and box widths below one quarter of the smallest distance to a cut ensures this, with uniform positive gaps.

Fix such a \(u\) and put
\[
 q(x)=\#\{i<l:x_{i,4}=x_{l,4}\}+\#\{i<l:(R_ux_i)_4=(R_ux_l)_4\}.
 \tag{8.4}
\]
The sets \(\{q\le q_0\}\) are open: all inequalities already present persist locally. Induct on \(q_0\). The case zero is proved. At a point with \(q=q_0>0\), choose a tied pair and a common cut separating it. Let \(A\) be the positive group for that cut, and translate precisely its slots by \(se_4\). Cross-group time differences have slopes \(\pm1\) in the original frame and \(\pm\cos u\) in the rotated frame. Internal differences do not change. For sufficiently small nonzero \(s\), old inequalities persist and all cross-group ties disappear, including the chosen one.

Choose one such \(s_*\), an interval \(I\) about it, and a smaller product neighborhood \(V\) of the point. All translated boxes remain in \(W\). Preserve all old inequalities and remove all cross-group ties uniformly on \(V\times I\). Remaining ties are among internal pairs originally counted, so their count is at most \(q_0-1\). The induction hypothesis makes (8.3) zero there for every slot tensor supported in \(V\).

For each such tensor its translated difference is holomorphic near the segment from zero to \(I\). Use (8.1)–(8.2) with \(v=e_4\) for the first term, and \(v=R_ue_4\) for the second. The same common cut separates the same index groups in both frames. Shrinking the segment keeps both strict gaps positive and gives a connected complex neighborhood satisfying (8.2). The identity theorem carries zero from \(I\) to zero. Tensor density proves \(D_u=0\) on \(V\). Since \(q\le n(n-1)\), induction terminates. This excludes a distribution supported on time ties; mere density of ordinary configurations would not do so.

For an arbitrary compact off-diagonal test and finite angle, the union of its rotated supports along the angle interval is compact in \(\mathcal C_n\). Cover it by finitely many neighborhoods \(W\), take the minimum positive angle bound, and divide the angle into smaller steps. A smooth partition of unity gives equality on each current support; compose the steps. Smooth approximation in fixed separated neighborhoods then gives compact \(C^1\) tuples.

Finally take a diagonal-flat Schwartz test. A large-radius cutoff removes its tails in every fixed Schwartz seminorm. On the remaining compact support, multiply by pair cutoffs vanishing within distance \(\varepsilon\) of each coincidence diagonal. Derivatives of order \(r\) cost at most \(C_r\varepsilon^{-r}\). Flatness and Taylor's formula give an arbitrary power \(\varepsilon^N\) for each derivative of the original test near the corresponding diagonal; take \(N\) above the finitely many derivative losses. Thus the cutoff error tends to zero in each seminorm. The remaining compact off-diagonal function has a finite partition into product boxes with separated slot supports. The Fourier construction above gives finite sums of separated smooth tensors converging in every derivative. A diagonal choice over seminorms gives Schwartz convergence. Rotations preserve diagonals and flatness and act continuously on Schwartz space by the chain rule. Apply the proved invariance to these approximants and pass through H-S's continuity. This proves invariance of the existing \(\Sigma_n\). ∎

**Theorem 9 (RO1, main theorem).** Let \(S\) be a volume-first limit through periodic Gibbs states, or a canonical component of PH1 with its all-state realization. Assume UV1 (rooted D1), LG1, CL1(2)–(4), and TP1(4) in its state-uniform form, precisely H-U, H-L, H-C and H-T above. Use SR1(4), H-S, for the diagonal-flat conclusion, and H-P for components. With constants in the stated IN1 order:

1. **UI:** the small-ball one-field Hilbert insertion bound (2.1) holds with \(c_I=1/(40L)\), \(p_I=0\), independently of the surrounding field numbers and coefficients.
2. **PD:** the scaled parametrix, analytic \(L^1\) density, plate bound and compatible point plates of Lemma 3 hold with \(\wp=p_I+5=5\).
3. **AK:** Lemma 4 gives holomorphic tube products, norm removal of plane smoothing, frame gluing on connected \(U_n\), a Gram representation, the band \(4|m|\le5n\), boost positivity and the cut inequality including the empty tuple.
4. **TU:** every nonconstant two-point harmonic vanishes, including the critical frequencies \(\pm8\).
5. **AC:** polygon divisibility and discrete convexity give \(M(2k)=kM(2)\). Local analytic translations remove exceptional distributional support. Every \(M(n)=0\), and the hierarchy is O(4)-invariant on separated compact \(C^1\) tuples and on its diagonal-flat extension:
   \[
   S_n(Rf_1,\ldots,Rf_n)=S_n(f_1,\ldots,f_n),\qquad
   \Sigma_n(R\phi)=\Sigma_n(\phi),\qquad R\in\mathrm O(4).
   \tag{9.1}
   \]

*Origin:* [ym4-assembly.md](ym4-assembly.md) §§4–5, RO1; the five port notes and the two check reports identified in Lemmas 1–8. This is their combined implication, not a new unconditional existence theorem.

*Proof.* Lemmas 1–4 prove the first three clauses. Lemma 5 and Theorem 6 prove the fourth. Lemmas 7–8 give all-order invariance in the chosen plane. Hypercubic conjugation transports it to all six coordinate planes. Their rotations generate SO(4): use successive rotations of row pairs to clear entries below the diagonal with positive pivots. Orthogonality leaves a diagonal matrix with the first three entries one; determinant one fixes the last. Reversing the row operations expresses the given matrix as a product of coordinate-plane rotations. An inherited coordinate reflection supplies the other component of O(4). The zeroth moment is one. The one-point function \(c\int f\) is invariant.

For a component with common-centering realization (D.1), H-P supplies
\(\rho_j\mathcal O_{a_j}(f)-\nu_j\mathcal O_{a_j}(f)\to c\int f\).
Expanding the finite product after subtracting these differences shows that \((\rho_j,\rho_j)\) realizes its self-centered hierarchy. H-U, H-L and H-T apply to those same periodic states. Substitution of the field minus its mean is an invertible triangular map on finite polynomials. It commutes with translations and reflection and identifies the self-centered reflection form with the original form on the substituted polynomials. Thus it induces a unitary identification of completions, preserving H-C and its spectral cone. At distribution level its finite subset expansion uses lower moments and integration in omitted variables; those integrations are continuous on Schwartz space and preserve flatness in the remaining variables. H-S therefore supplies the self-centered extension as well. Run Lemmas 1–8 for this self-centered component. Restoring its mean expands each moment into finitely many lower centered moments and factors \(c\int f_i\), all invariant. H-S and Lemma 8 pass this equality to the component's given extension. This argument is performed for each realized component; covariance is never inferred from covariance of the mixture. ∎

## Definitions supplied in distillation

The previously dispersed conventions are now explicit: the common-centering realization (D.1); admissible field-polynomial concatenation and the pulled-down Hilbert norm; the distinction between cube and round cones; compact profiles versus extended \(L^1\) plates; light coordinates, star, tube, pencils, ordering domains and distinct-point Gram configurations; the full TU10 shape class and connected reflection seminorm; the rooted source interface including representation independence and mirror coefficient lists; the cell seminorm and raw reflection operators; the scaled parametrix and its density; the padded product vectors, harmonic projectors and global degree \(M(n)\); the axis and diagonal spectral measures and Lorentz pushforwards; labelled zero sets, the convexity defect, common cuts and time-tie count; and the off-diagonal and diagonal-flat test domains. Each is defined where first used. No new physical identification is supplied.

## Source and gate record

The following ranges were read in the pinned raw files after locating the objects in `sa-index/README.md`, chunk rows and `obligations.md`. SA means `YM4_sketch_500.tex`; Y3 means `YM3/YM3_I.tex`, both at `31a47c543775`.

| Proof in this part | Checked local note and check | Raw source read for the argument |
|---|---|---|
| Lemmas 1–2, cell source interface | `ui-port.md` §§2–6; `o4-check-1.md` §2 | SA L23767–23831, L24041–24169, L28229–28526; Y3 L79104–79201, L79374–79443 |
| Lemma 3, density and plates | `pd-port.md` §§2–4; `o4-check-1.md` §3 | SA L28527–28887; Y3 L76400–76497 |
| Lemma 4, kernels and band | `ak-port.md` §§1–9; `o4-check-2.md` §1 | SA L28888–29921 |
| Lemma 5 and Theorem 6 | `tu-port.md` §§2–6; `o4-check-2.md` §2 | SA L29922–30507; the low-energy mass and imaginary-axis arguments are the checked local alternatives |
| Lemmas 7–8 | `ac-port.md` §§2–6; `o4-check-2.md` §3 | SA L30508–30865; Y3 L76854–76913 |
| Theorem 9, component scope | Both reports; especially `o4-check-2.md` §4, defect 1 | SA L31799–31856 |

The outline contains conditional proofs of these angular steps. D1 and TU10 remain hypotheses of that implication. The local improvement \(p_I=0\) is the fixed-cell argument of `ui-port.md`, consistent with Y3 IV-56-17; the outline's displayed UI10 instead uses the weaker \(\eta^{-4}\). It must not be substituted into the exponent-five argument without that improvement.

The five port notes, `t0-skeleton.md`, and both cited gates were read whole. Gate 1's lattice-only remarks concern LG1: the missing enclosing-cube size, simultaneous gauge covariance of the transfer square root, and the scope of the no-common-torus lemma do not add RO1 premises. LG1 stays an import; volume-first is the chosen realization, not a consequence excluding every possible alternative construction. The shortcut and generalized-free-field counterexample in `pd-port.md` §5 are not needed in RO1's proof and are not recopied.

The outline and CA-I were fetched once to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`; Y3 was fetched once to `/tmp/sa_ym3_I.tex`. CA-I was not used as a proof input. No CA-II/III claim or quotation is made. SHA-256 identities of the raw files and local inputs are recorded in `/tmp/ro1-distil-a456311fd/source-sha256.txt`. The raw source identities are:

- SA: `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`.
- CA-I: `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.
- Y3: `248959db554e4678aa88e92c9fe98372cd54b45719bb70bf43c47547d0c9f443`.

## Result

RO1 proves the conditional implication in Theorem 9: rooted D1, the lattice mirror interface, the continuum Hilbert and cube-cone interface, and state-uniform TU10 give full scalar O(4) covariance. SR1 supplies the existing diagonal-flat extension. PH1 supplies each component's realization and one-point convergence. The component argument uses that component's own connected two-point function. Neither D1 nor TU10 nor existence of the realizations is discharged here.

Corrections and clarifications made in this distillation:

1. Made the insertion support and \(p_I=0\) explicit; kept it distinct from the plate exponent \(\wp=5\). The small-ball bound is not asserted for arbitrary supports.
2. Retained the gate's distinct-point condition within every Gram configuration, and required compact \(C^1\) plane profiles before using the original moment functional. \(L^1\) cases refer to the constructed extension.
3. Named the local continuity, all-coordinate cube cones, off-diagonal distributions and diagonal-flat extension/density imports. Neither analytically extended coefficients nor equality on a dense ordinary set replaces Lemma 8.
4. Preserved the essential line phase for the top positive kernel, the empty-tuple cut, the full TU10 shape checks, connected vacuum subtraction, and the derivation of the diagonal cone from the positive-measure identity.
5. Made self-centering and state-uniform TU10 explicit for every realized component. Mixture symmetry supplies no component covariance.
6. Removed the obsolete “D1 starts at C1/OH1” diagnosis. The outstanding import is actual rooted UV1, together with state-uniform TP1(4); this text does not reclassify upstream results.
7. Used IN1's current ordered choices, including its amendment, rather than repeating the assembly's older constant-order diagnosis. Renamed colliding local symbols and supplied unique equation numbers.
8. Corrected the skeleton's compressed Y3 locator for UI: the insertion propositions are at L79104–79201 and L79374–79443, outside its L75578–77017 rotation range. The source record distinguishes the local endpoint proof from the outline's dilation proof.

No additional unresolved step was found in the deductions from these named imports. **Outstanding** marks above concern the actual imported D1 and TU10 estimates; realization and extension remain explicit hypotheses. This is a hand-written distillation of checked notes, **not yet refereed as a whole part**, not an audit, and it grants no scientific status. No computer-assisted step is used.
