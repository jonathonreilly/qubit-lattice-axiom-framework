# CL1 — Continuum limits, Euclidean Hilbert space and cones

Provenance: Codex (GPT-6), 2026-11-05; Phase A, pass 2 (distil), from checkout `1724d326aee3af902e55c00bd248cf6ef6099e03`. Research text; not an audit; grants no status. Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, are credited for the constructions taken from their pinned account `31a47c543775`.

This part distils [s4-s6.md](s4-s6.md) and [cone-o6.md](cone-o6.md), checked line by line by Claude in [bridge-check.md](../gates/bridge-check.md), §§2–3, first failing step none. Theorem 9 is the CL1 statement of [ym4-assembly.md](ym4-assembly.md), §§4–5, with its centering and limit conventions made explicit. The assembled part has not been refereed.

## Definitions

Work on \(a\mathbb Z^4\) with \(SU(2)\), normalized Haar measure, and
\[
 A_p(U)=1-\tfrac12\operatorname{Re}\operatorname{Tr}U_p\in[0,2],\qquad
 \mathcal O_a(f)=\sum_p f(x_p)A_p(U).
 \tag{1}
\]
Here \(x_p\) is the plaquette barycenter. Count one plaquette per coordinate plane and site, hence six orientations. There is no spacing prefactor in \(\mathcal O_a\). The torus law \(\mu_{a,\ell,\beta}\) has density proportional to \(e^{-\beta\sum_pA_p}\).

Let \(\mathcal G_{a,\beta}\) be the Wilson DLR probability measures invariant under a full-rank sublattice of \(a\mathbb Z^4\). DLR means that, conditionally on bonds outside a finite set \(W\), the bonds in \(W\) have normalized Haar density proportional to \(e^{-\beta\sum_{p:p\cap W\ne\varnothing}A_p}\); denote this kernel by \(\gamma_W\). Compatible cubic tori have sides \(\ell=2L^m\), with \(m\) above the grid and size floors supplied by I1 and I3. At each fixed datum these form a cofinal family. Let \(\mathcal G^{\rm tor}_{a,\beta}\) be the weak limit points of their periodically lifted laws as \(\ell\to\infty\), at fixed \(a,\beta\).

Fix the odd block size \(L\) and a reference coupling \(g>0\) in the order below. A first-passage datum is \(\beta\in\mathcal W_K(g)\), where
\[
 K(\beta,g)=\min\{k:x_k(\beta)\le g^{-2}+B_\sharp\},\qquad
 \mathcal W_K(g)=\{\beta\ge g^{-2}+B_\sharp:K(\beta,g)=K\}.
\]
The run \(x_k\), \(B_\sharp\), and its compatibility are supplied by IN1. A **volume-first limit** is a limit of connected correlations through \(\rho_j\in\mathcal G^{\rm tor}_{a_j,\beta_j}\), with first-passage data and \(a_j=L^{-K_j}\downarrow0\). A limit **of SA 0(a)(iii) type** instead uses finite torus laws at the same data with \(\ell_j\to\infty\).

Put \(\mathbb E=\mathbb R^4\) and \(\mathbb E^n_{\ne}=\{\mathbf x:x_i\ne x_h\text{ for }i\ne h\}\). A separated tuple \(X=(f_1,\ldots,f_n)\) has \(f_i\in C_c^1(\mathbb E;\mathbb C)\) with pairwise disjoint supports. The empty tuple is \(1\); a zero entry has value zero. A tuple has type \((d,R)\) when its support distances are at least \(d>0\) and each support lies in its own radius-\(R\) ball. Centers are arbitrary; enclosing balls need not be disjoint. Set
\[
 \|f\|_\sharp=\max(\|f\|_\infty,c_M\|\nabla f\|_\infty),\qquad
 \|f\|_1=\max(\|f\|_\infty,\|\nabla f\|_\infty),\quad c_M>0.
\]
Multilinearity is required only when the unions of alternative supports retain separation from the other slots.

Write \(\mathfrak S(O)\) for these tuples supported compactly in an open set \(O\), including \(1\), and \(V(O)=\mathbb C\mathfrak S(O)\) for their finite formal span. Concatenation is used only when the combined tuple is separated. Set \(\tau_vf(x)=f(x-v)\). An isometry \(r\) acts by \(rf=f\circ r^{-1}\); conjugation acts on coefficients and entries. The group \(W_d\) consists of signed coordinate permutations. For a unit normal \(u\), let \(\theta_ux=x-2(u\cdot x)u\) and \(V_u=V(\{u\cdot x>0\})\). Coordinate and diagonal mirrors have normals \(e_\mu\) and \((e_\mu\pm e_\lambda)/\sqrt2\), including all affine translates. Reflection positivity means positivity on every finite combination in the appropriate \(V(O)\), including constants.

For \(\rho_j,\nu_j\in\mathcal G_{a_j,\beta_j}\), define
\[
 Z_j(f)=\mathcal O_{a_j}(f)-\nu_j(\mathcal O_{a_j}(f)),\qquad
 m_{j,n}(\mathbf f)=\rho_j\prod_iZ_j(f_i),\quad m_{j,0}=1.
 \tag{2}
\]
The symbol \(\sigma\) will denote their limiting moment functional. Its higher cumulants are \(S_n\), \(n\ge2\). The canonical centered functional is
\[
 \sigma_S(X)=\sum_{\pi\in\operatorname{Part}_{\ge2}[n]}
                      \prod_{B\in\pi}S_{|B|}(X_B),\quad
 \sigma_S(1)=1,\quad \sigma_S(f)=0.
 \tag{3}
\]
Here \(\operatorname{Part}[n]\) denotes set partitions; the subscript excludes singleton blocks. Write \(\kappa_n^\rho\) for the joint cumulant under \(\rho\), defined by the inverse partition formula (10) applied to its moments. In general \(\sigma\ne\sigma_S\).

Let \(\Delta_n=\mathbb E^{n}\setminus\mathbb E^n_{\ne}\). Write \(\mathcal S_{\Delta,n}=\mathcal S_{\ne}(\mathbb R^{4n})\) for Schwartz functions all of whose derivatives vanish on \(\Delta_n\), and put
\[
 p_s(\Phi)=\max_{|\alpha|\le s}\sup_x
                   (1+|x|^2)^{s/2}|\partial^\alpha\Phi(x)|.
\]
Let \(\mathcal E_{+,n}\) be those flat functions supported where all fourth coordinates are nonnegative. Smoothness forces flatness at every zero-time boundary. Set \(\mathcal E_{+,0}=\mathbb C\); only finite sequences of these spaces are used.

## Imports and order of constants

**I1 — IN1(4), first passage.** Import [in1.md](in1.md), Theorem 12, only for the compatible first-passage data and their common constants. For fixed admitted \(g\), the nonempty \(\mathcal W_K(g)\) have unbounded \(K\), and \(g^{-2}<x_K\le g^{-2}+B_\sharp\). Thus an admitted sequence with \(K_j\to\infty\) can be chosen. Its upstream imports remain H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E, H-O and H-SUM, with their Outstanding paragraphs. CL1 proves none of those actual-construction inputs.

**I2 — LG1, lattice structure.** Every state in \(\mathcal G_{a,\beta}\) is invariant under all lattice translations and \(W_4\), and is reflection positive at the coordinate site, coordinate bond, and diagonal lattice mirrors. This includes invariance of the centering state. Finite-torus link reflection positivity is an upstream input of SR1, not a diagonal-mirror assertion about one cubic torus.

**I3 — SR1, bounds and quantitative extension.** At all chosen data, for any two periodic states and every separated real tuple of type \((d,R)\), import the one-point comparison, higher cumulant bounds, and
\[
 \begin{split}
 |m_{j,1}(f)|&\le C_1(R)\|f\|_\sharp,\\
 |m_{j,n}(\mathbf f)|&\le B(R)^n(n!)^k
                 \max\{1,d^{-5n}\}\prod_i\|f_i\|_\sharp,\\
 |\kappa_n^{\rho_j}(\mathcal O(f_1),\ldots,\mathcal O(f_n))|
       &\le[2B(R)]^n(n!)^k\max\{1,d^{-5n}\}\prod_i\|f_i\|_\sharp
       \quad(n\ge2).
 \end{split} \tag{4}
\]
Here \(B(R)=C(R+1)^4\), \(k=\lceil p\rceil+5\) for SR1's cell-loss exponent \(p\), and all constants are independent of cutoff, states and positions. For \(n=1\), take \(d=1\). Complexification enlarges \(B\) by at most two. SR1's H1 implication gives the unique diagonal-flat extension with bound \(C_E^n(n!)^{k+32}p_{20n}\) and constrained smooth-tensor density. The per-order extension needed to identify the Hilbert spaces is proved again in Lemma 4; factorial accounting is imported from SR1. SR1 itself retains UV1's full D1 with rooted geometry and LG1.

**Analytic background.** As in the checked notes, use the Riesz representation theorem for positive functionals on a compact metric space, the spectral theorem and its measurable functional calculus, and the joint spectral theorem for strongly continuous abelian unitary groups. Integration uses Tonelli, Fubini, dominated convergence and Fatou. These are named mathematical imports, not estimates for the Yang–Mills construction. Fourier summability, the Gamma transform, and all limit and contraction steps used here are justified below.

**Constant order.** Freeze IN1's ten-row order, including Amendment 1, before choosing the sequence. The following abbreviates those rows; each row retains its internal floors and definitions in [in1.md](in1.md), “Constant order”.

| Order | Choices retained from IN1 |
|---|---|
| 1 | Reserve and rarity requirements, margins and Hölder exponent; power-count constants; then \(r,p_0,p_1,q,\kappa_0\). |
| 2 | Scale-independent geometry and hull constants; then odd \(L\), including \(L>L_0^\natural\) and the listed geometric floors; then flat/averaging constants, \(c_0,c_2\) and the weak frame bounds. |
| 3 | Local gauges, inverses and reference ceilings; propagator/profile/walk rates; \(M_1,R_1,\rho=R_1M_1\); then seam, A2/A3, tower bounds and radii. |
| 4 | H-M's early matrix constants, Gaussian constants, geometry and \(W_0\); then \(\kappa\ge\kappa_0^\natural(L)\), including its entropy/decay floors; then \(\Theta\), then \(\lambda\). |
| 5 | \(\bar\kappa,\kappa_1,R_s=e^{\bar\kappa}\); response lengths and decoupled radii; preparation/profile constants; then the localization size \(M\), a power of \(L\). |
| 6 | Post-\(M\) box/chart/comparison constants and tilt; \(A_1\) then \(A_0\), \(C_0\) then \(C_1\); absolute radii/current ceilings; radius ratios and response-room/age constants. |
| 7 | Regular/list constants; boundary maximum and volume costs; certificate and genealogy constants; envelope/interior/coding constants then entropy; \(C_v\) then \(c=C_vc_r\); oscillation bound then \(c_1\) above the total reserve cost. |
| 8 | Remaining prepared/source/label/floor/flow-error and tube constants; \(d_0\) after \(L,r,\overline B\). |
| 9 | Increase \(X_0\) for all requirements; set \(\gamma=X_0^{-1/2}\); then \(\varsigma,\lambda_\sharp,B_\sharp\). |
| 10 | Choose \(0<g\le\gamma\) within the source ceilings, admissible grids/tori and \(\beta\ge g^{-2}+B_\sharp\); form a coefficient before the next frame entry. |

The physical norm constant \(c_M\) is fixed with the source package after \(M\). SR1's \(C,C_1,B,k,C_E\) then remain fixed for the chosen \(g\). Choose first-passage data, then remove volume separately at each datum, then extract a cutoff subsequence. Proof constants \(M_n(d,R)\) depend only on (4), \(n,d,R\); per-order extension constants also depend on fixed smooth cutoffs. Test approximations, torus sizes, and spectral-probe parameters are chosen later and never change an upstream constant.

**Outstanding — supplied construction.** I1 and I3 are conditional on their stated upstream inputs. In particular, CL1 does not establish D1 or the actual run underlying IN1(4). The old notes' pointer to C1/OH1 as the first open item is not retained: bridge-check §4 explicitly calls that pointer stale. There is no additional Yang–Mills estimate assumed within the proofs below.

## Hand proofs

### Lemma 1. Fixed-cutoff volume-first states

For every admitted fixed \(a,\beta\), \(\mathcal G^{\rm tor}_{a,\beta}\) is nonempty and consists of translation-invariant Wilson DLR states.

*Origin:* s4-s6 §2; bridge-check §2. SA CC1–CC2, lines 24376–24467.

*Proof.* Enumerate the positively oriented bonds. The metric
\(\sum_{r\ge1}2^{-r}\min(1,\|U_{e_r}-V_{e_r}\|)\)
makes \(SU(2)^E\) compact: diagonal extraction in its compact factors gives convergence in this metric. Freezing all but finitely many coordinates changes the metric by an arbitrarily small amount, so continuous cylinder functions are uniformly dense.

The continuous-function space is separable. Take centers in a countable dense set, rational-radius finite covers, and weights \((r-d(x,x_i))_+\) divided by their positive sum. Rational linear combinations approximate every continuous function by uniform continuity. Extract convergence of torus integrals on this countable family. Uniform approximation yields a positive norm-one functional on all continuous functions; its Riesz measure is a weak limit.

For finite \(W\), the DLR denominator is at least \(e^{-2\beta|\mathcal P(W)|}\). Its kernel therefore sends continuous local functions to continuous local functions. For local \(F\), sufficiently large tori embed all bonds of \(W\), its interaction boundary, and \(F\) injectively. Integrating those torus variables gives \(\mu_\ell(\gamma_WF)=\mu_\ell(F)\). The weak limit satisfies the same identity. Cylinder approximation extends it to continuous \(F\); equality of the resulting Borel measures extends it to bounded Borel \(F\). For bounded outside-measurable \(b\), properness gives \(\gamma_W(bF)=b\gamma_WF\). This is the conditional DLR equation.

Lattice translations and \(W_4\) preserve Haar measure and the Wilson action, so their invariance passes weakly. I2 supplies all mirrors of the resulting state. This construction is performed at each fixed datum before the cutoff limit. \(\square\)

### Lemma 2. One subsequence for every separated tuple

One subsequence \(j_r\) makes (2) converge at every order and separated \(C^1\) tuple. It also gives moving-test convergence when entries converge in \(C^1\) within fixed separated compact containers. The limit preserves (4).

*Origin:* s4-s6 §§1, 3; bridge-check §2. SA CC3–CC9; YM3_I IV-10-25/28.

*Proof.* The finite moment–cumulant identity is
\[
 m_{j,n}(\mathbf f)=\sum_{\pi\in\operatorname{Part}[n]}
                 \prod_{B\in\pi}\kappa^{\rho_j}_{|B|}(Z_j(f_i):i\in B).
 \tag{5}
\]
In commuting variables with \(z_i^2=0\), the exponential of the cumulant polynomial gives this formula: its factorial cancels the orders of the blocks. Subtraction changes only singleton cumulants. Thus SR1's one-point and higher cumulant bounds supply a position-independent bound \(M_n(d,R)\prod_i\|f_i\|_\sharp\); the stronger bound is (4).

For each finite union \(Q\) of rational closed boxes, supported \(C^1\) functions embed through their values and four derivatives into the separable space \(C(Q)^5\). A subspace of a second-countable metric space is second-countable, hence separable by selecting one point from each nonempty basic open set. Choose a countable dense family in each supported space. Enumerate all tuples from these families with separated containers, at every order. Successive extraction and a diagonal subsequence make all their bounded values converge. Any prescribed countable collection of bounded scalar sequences may be included in this extraction.

For entries \(f_i,h_i\) in fixed separated containers, multilinearity gives
\[
 |m_{j,n}(\mathbf f)-m_{j,n}(\mathbf h)|
 \le M_n(d,R)\sum_i\|f_i-h_i\|_\sharp
                \prod_{l\ne i}\max(\|f_l\|_\sharp,\|h_l\|_\sharp).
 \tag{6}
\]
Every mixed tuple is separated. Enclose any given compact separated supports in rational box unions with positive mutual distance. Approximation there makes (6) uniformly small in \(j\). Comparing two subsequence values through a fixed approximant proves the Cauchy property. This defines \(\sigma_n\) on every tuple along the same subsequence. Admissible multilinearity, symmetry, conjugation and all bounds pass through finite identities and closed inequalities.

The same estimate proves moving-test convergence and uniform convergence on compact subsets of a fixed product of supported \(C^1\) spaces, using finite nets. The determining evaluations \(X^m\) metrize the closed bounded class by \(\sum_m2^{-m}\min(1,|\sigma(X^m)-\sigma'(X^m)|)\). Equation (6) separates points and makes each evaluation continuous; a finite-head/tail argument proves the reverse continuity. Diagonal extraction proves compactness in this metric. \(\square\)

### Lemma 3. Symmetries, mirrors, centering and connected limits

Both \(\sigma\) and \(\sigma_S\) are translation- and \(W_4\)-invariant, symmetric, real, and reflection positive at every coordinate and diagonal affine mirror. For some uniformly bounded real \(c\), \(\sigma_1(f)=c\int f\). Their higher cumulants agree and are the limits of the integrating states' cumulants, with the bounds (4).

*Origin:* s4-s6 §4; bridge-check §2, including its centering and mirror corrections. SA CC9–CC16. The explicit distinction between \(\sigma\) and \(\sigma_S\) follows SA CC16 and YM3_I IV-24-15.

*Proof.* Uniform continuity of a compact \(C^1\) gradient gives
\[
 \|\tau_vf-\tau_wf\|_\sharp
 \le\max\{\|\nabla f\|_\infty|v-w|,
                   c_M\omega_{\nabla f}(|v-w|)\}\longrightarrow0.
 \tag{7}
\]
Round a real translation to \(a_j\mathbb Z^4\), use invariance of both states, and apply Lemma 2 with moving tests. Signed coordinate permutations act exactly at every spacing and pass directly. Symmetry and reality are finite moment identities.

For \(x_\mu=b\), choose link mirrors \(b_j\in a_j(\mathbb Z+\tfrac12)\) tending to \(b\). For \(x_\mu\pm x_\lambda=b\), choose \(b_j\in a_j\mathbb Z\). The reflected tests differ by translations \(2(b_j-b)e_\mu\) and \((b_j-b)(e_\mu\pm e_\lambda)\), respectively. The unit-normal diagonal offset grid is \(a_j\mathbb Z/\sqrt2\).

Fix a finite combination \(F\) of separated tuples strictly in one open half-space. Its compact supports have a positive mirror gap. Since a plaquette has diameter at most \(\sqrt2a_j\), all sampled plaquettes eventually lie on the correct side of the rounded mirror. Centering commutes with reflection by I2. Lattice positivity gives
\[
 0\le\rho_j(\overline{\theta_jF_j}F_j)
       \longrightarrow \sigma(\theta\bar F\cdot F).
 \tag{8}
\]
Every concatenated tuple retains internal separation and a gap between its two halves. Lemma 2 therefore justifies each term of this finite limit. Reflection invariance passes by the same argument; either side may be used.

I2 makes \(\delta_j=\rho_j(A_p)-\nu_j(A_p)\) independent of \(p\). Exactly,
\[
 m_{j,1}(f)=c_jR_j(f),\qquad
 c_j=6a_j^{-4}\delta_j,\qquad R_j(f)=\frac{a_j^4}{6}\sum_pf(x_p).
 \tag{9}
\]
Each orientation is a shifted cubic grid. Comparing a sample to its side-\(a_j\) cube costs at most \(2a_j\|\nabla f\|_\infty\). At most \(C(R+1)^4a_j^{-4}\) cubes meet the support or its adjacent cubes, uniformly in its position. Thus
\[
 |R_j(f)-\int f|\le C(R+1)^4a_j\|\nabla f\|_\infty.
\]
Choose a fixed nonnegative smooth \(f_*\) with integral one. Along the existing subsequence,
\[
 c_j=\frac{m_{j,1}(f_*)}{R_j(f_*)}\to c=\sigma_1(f_*),\qquad
 \sigma_1(f)=c\int f,\qquad |c|\le C_1(R_*)\|f_*\|_\sharp .
\]
Reality gives real \(c\); if \(\rho_j=\nu_j\), then \(c=0\).

The finite logarithm in squarefree variables gives
\[
 S_n(\mathbf f)=
 \sum_{\pi\in\operatorname{Part}[n]}(-1)^{|\pi|-1}(|\pi|-1)!
                       \prod_{B\in\pi}\sigma_{|B|}(\mathbf f_B).
 \tag{10}
\]
Indeed its term with \(r\) blocks counts \(r!\) orders and divides by \(r\). Every subtuple converges, so (10) is the limit of the lattice cumulants. A scalar shift changes the logarithm only in degree one. Hence \(n\ge2\) gives the raw \(\rho_j\) cumulants, independently of \(\nu_j\), and (4) passes.

Centering the lattice moments at \(\rho_j\) instead gives, on the same subsequence,
\[
 \sigma_S(\mathbf f)=\sum_{A\subset[n]}
         \sigma_{|A|}(\mathbf f_A)\prod_{i\notin A}(-c\int f_i).
 \tag{11}
\]
The exponential identity (5) identifies this with (3). Applying (4) and (8) to the pair \((\rho_j,\rho_j)\) proves its bounds and reflection positivity without a new recentering constant. The other identities pass likewise. \(\square\)

### Lemma 4. Off-diagonal distributions and the flat extension

Each \(\sigma_n\) and \((\sigma_S)_n\) for \(n\ge1\), and \(S_n\) for \(n\ge2\), has a unique distribution of locally finite order on \(\mathbb E^n_{\ne}\) with its prescribed smooth separated-tensor values. It has a unique continuous extension to \(\mathcal S_{\Delta,n}\). For the corresponding lattice and limit forms there is a common per-order bound
\[
 |\Sigma_{j,n}(\Phi)|,\ |\Sigma_n(\Phi)|\le A'_n p_{20n}(\Phi).
 \tag{12}
\]
Along the original subsequence their values converge, also for \(\Phi_{j_r}\to\Phi\) in Schwartz topology. For the limit forms of the moments \(\sigma_n\) and \((\sigma_S)_n\), I3 improves \(A'_n\) to \(C_E^n(n!)^{k+32}\). No factorial bound is claimed here for the cumulant limits \(S_n\) or for the lattice forms \(\Sigma_{j,n}\).

*Origin:* s4-s6 §6; bridge-check §2, with its explicit box sizes and overlap repair. SA QF8–QF22 and CC17–CC18. Factorial growth remains the SR1 import.

*Proof.* For each of these forms, (4) on independently placed unit-radius supports gives
\[
 |T_n(\mathbf f)|\le A_n\max(1,d^{-5n})\prod_i\|f_i\|_1,
 \tag{13}
\]
uniformly in \(j\) for the lattice forms. For cumulants use their bound in (4); for canonical moments use the self-centered lattice pair.

Fix \(0<h\le1/16\), \(\ell=h/64\). The inner slot cubes are \(c_i+[-\ell,\ell]^4\), expanded cubes are \(c_i+[-2\ell,2\ell]^4\), and Fourier periods are \(8\ell\). Require expanded cubes to be separated by at least \(h/2\); they fit in unit-radius balls. Expand a smooth \(u\) supported in the product of inner cubes in its period-\(8\ell\) Fourier series. Multiply each slot mode by a smooth cutoff supported in its expanded cube and equal to one on its inner cube. No other periodic copy of the inner cube meets that cutoff.

In rescaled variables, four applications of \(1-\pi^{-2}\Delta_i\) in each four-dimensional slot give
\[
 |\widehat u(\mathbf v)|\le C_nJ_{8n,\ell}(u)
                   \prod_i(1+|v_i|^2)^{-4},\qquad
 J_{q,\ell}(u)=\max_{|\alpha|\le q}\ell^{|\alpha|}
                                     \|\partial^\alpha u\|_\infty .
\]
A cut-off mode has \(C^1\) norm at most \(C\ell^{-1}(1+|v_i|)\). In \(\mathbb Z^4\), the shell \(|v|_\infty=r\) contains \(O((r+1)^3)\) points, whereas \((1+|v|)(1+|v|^2)^{-4}=O(r^{-7})\). The mode-value sum is therefore absolutely convergent. Equation (13) defines a local functional with
\[
 |T(u)|\le C_n h^{-6n}J_{8n,\ell}(u).                 \tag{14}
\]
Extra integrations by parts give convergence in every fixed derivative. To identify the Fourier series with \(u\), the period-two Fejér kernel
\(N^{-1}|\sum_{k=0}^{N-1}e^{i\pi ks}|^2\)
has normalized integral one by orthogonality, and is at most
\([N\sin^2(\pi\epsilon/2)]^{-1}\) for \(\epsilon\le|s|\le1\).
Its product kernels concentrate at zero, so uniform continuity proves convergence of their convolutions. The absolutely convergent Fourier series has the same limit. On separated tensors, slotwise \(C^1\) convergence and (13) recover the given value.

Tensor relations are respected. For finite-dimensional slot spans, finitely many point evaluations distinguish all vectors; tensoring these injective maps proves injectivity of their algebraic tensor product into functions. On an overlap of two product boxes, partition the compact support into smaller product boxes whose expanded cubes lie inside the overlap. Their cut-off Fourier tensors are evaluated identically by both local functionals; (14) passes equality to the limit. Products of two partitions of unity then prove independence of the cover. Finite partitions glue a distribution on \(\mathbb E^n_{\ne}\). Partitioning each entry of a larger separated tensor recovers its prescribed value. On a compact subset, a finite box cover makes (14) a finite-order distribution bound. Fourier approximation also proves uniqueness there.

For the global extension choose a fixed smooth \(\zeta\) equal to zero on \(|x|_\infty\le1\) and one on \(|x|_\infty\ge2\). Put
\[
 h_r=2^{-r}/16,\quad P_h=\prod_{i<l}\zeta((x_i-x_l)/h),\quad
 D_0=P_{h_0},\quad D_r=P_{h_r}-P_{h_{r-1}}\ (r\ge1).
\]
Their sum is one off the diagonals. On a fine layer the closest pair has sup-distance between \(h_r\) and \(4h_r\). For \(n=1\), \(P_h=1\) and fine layers vanish.

Use a smooth grid partition with slot supports \(c_i+[-\ell_r,\ell_r]^4\), centers in \(\ell_r\mathbb Z^4\), and \(\ell_r=h_r/64\). Construct it by dividing compact bump translates by their positive periodic sum. If a product box meets a nonzero layer, some point there has all pair distances at least \(h_r\). The expanded cubes are thus at least \(h_r-6\ell_r>h_r/2\) apart. Let \(\chi_{r,z}\) be this product partition.

For \(\Phi\) flat on the diagonals, Taylor expansion to a nearest pair diagonal gives
\[
 J_{8n,\ell_r}(\chi_{r,z}D_r\Phi)
 \le C_nh_r^{10n+2}p_{20n}(\Phi)
       \sup_{x\in\operatorname{supp}\chi_{r,z}}(1+|x|^2)^{-10n}.
 \tag{15}
\]
The Taylor segment has length at most \(8h_r\), and its weights have bounded ratio. Taylor uses \(10n+2\) derivatives after at most \(8n\): \(18n+2\le20n\). Each cutoff derivative costs \(h_r^{-1}\), canceled by its scaled factor in \(J\). Leibniz introduces only a finite constant depending on \(n\). The coarse layer has the same estimate without the small power of \(h_r\).

The position sum of the displayed weight is at most \(C_nh_r^{-4n}\). Indeed
\[
 (1+\sum_i|x_i|^2)^{-10n}\le\prod_i(1+|x_i|^2)^{-10},
\]
and each slot grid sum is \(O(\ell_r^{-4})\) by comparison with its integral. Its radial tail is bounded by \(\int_1^\infty r^{-17}dr<\infty\). Equations (14)–(15) bound a fine layer by
\[
 C_nh_r^{10n+2-6n-4n}p_{20n}(\Phi)
          =C_nh_r^2p_{20n}(\Phi).
\]
Summing layers and positions defines \(\Sigma_n\) and proves (12), including the lattice version with the same constant.

For density, first cut off infinity; an extra Schwartz weight bounds the error in each \(p_s\) by a negative power of the cutoff radius. Next multiply by \(P_h\). Taylor to a diagonal to arbitrary order \(m>s\) bounds the error by \(C_{n,s,m}h^{m-s}p_{s+m}(\Phi)\). The remaining compact off-diagonal test has a finite product-box partition. Its Fourier partial sums converge with every derivative and fixed compact support, hence in Schwartz topology. A diagonal choice of approximants proves density of smooth separated tensors and uniqueness of the extension.

For positive-time tests, also multiply by \(\prod_i b(x_{i,4}/h)\), where \(b=0\) below 1 and \(b=1\) above 2. Taylor to a zero-time hyperplane gives the same error estimate. Choose all expanded Fourier boxes inside the resulting positive-time gap. Thus strictly positive-time separated tensors are dense in \(\mathcal E_{+,n}\).

Finally approximate a fixed \(\Phi\) by one finite tensor sum. The common bound (12) controls both approximation errors; Lemma 2 gives convergence on that sum. This proves convergence on the whole flat space and, by the same bound, for Schwartz-convergent moving tests. For \(\sigma_n\) and \((\sigma_S)_n\), I3's quantitative extension agrees by uniqueness, so its factorial bound applies to these two limit forms. \(\square\)

### Lemma 5. The reflection Hilbert spaces and their translations

Let \(\varphi\) be either \(\sigma\) or \(\sigma_S\), and let \(u\) be a coordinate or diagonal unit normal. The completed quotient of \(V_u\) by
\[
 q_u(F,G)=\varphi(\theta_u\bar F\cdot G),\qquad
 \mathcal N_u=\{F:q_u(F,F)=0\},\qquad
 \mathcal H_u=\overline{V_u/\mathcal N_u}
 \tag{16}
\]
is separable. The vacuum \(\Omega=[1]\) has norm one. Normal translations give strongly continuous positive self-adjoint contractions \(T_t^u=e^{-tH_u}\), \(t\ge0\), with \(H_u\ge0\), \(H_u\Omega=0\), and \(\ker T_t^u=0\) for \(t>0\). Tangential translations give commuting strongly continuous unitaries. For \(u=e_4\), fix the convention
\[
 U_x=e^{ix\cdot P},\qquad
 \varphi(\theta\bar F\cdot\tau_{(x,t)}G)
       =\langle[F],e^{-tH}U_x[G]\rangle,\quad \theta=\theta_{e_4}.
 \tag{17}
\]
The \(P_i\) commute strongly with \(H\), meaning that their spectral projections commute. Spatial \(W_3\) acts unitarily, fixes \(\Omega\), commutes with \(H\), and sends \(U_x\) to \(U_{wx}\).

*Origin:* s4-s6 §5 and cone-o6 §2; bridge-check §§2–3, with its momentum-sign correction. SA HB1–HB7a; YM3_I IV-27-22.

*Proof.* Lemma 3 gives positivity. Polarization and positivity of \(q_u(F+zG,F+zG)\) give Hermiticity and Cauchy–Schwarz. Null vectors are orthogonal to every vector, so the quotient is defined. Its empty class has squared norm one.

Translation invariance and \(\theta_u\tau_{tu}=\tau_{-tu}\theta_u\) give symmetry of normal translation. Tangential translations preserve the form and have inverse translations. For a fixed finite \(F\), individual support radii and norms remain fixed under \(\tau_{tu}\). Internal separations remain fixed, and opposite-side distances cannot decrease:
\[
 |y+ru-x|^2=|y-x|^2+2r\,u\cdot(y-x)+r^2\ge|y-x|^2
 \quad(u\cdot x<0<u\cdot y,\ r\ge0).
\]
The position-independent bound (4) therefore gives \(a_F(t)=\|\tau_{tu}F\|_{q_u}\le C_F\) for all \(t\ge0\). Empty tuples use normalization; for singletons there is no internal separation requirement. Symmetry and Cauchy–Schwarz give
\[
 a_F(t)^2=q_u(F,\tau_{2tu}F)\le a_F(0)a_F(2t).
\]
If \(a_F(0)=0\), this preserves null vectors. Otherwise iteration gives
\[
 a_F(t)\le a_F(0)^{1-2^{-r}}C_F^{2^{-r}}\longrightarrow a_F(0).
 \tag{18}
\]
Thus the normal maps extend as contractions. Their bounded symmetric extensions are self-adjoint, and \(T_t^u=(T_{t/2}^u)^2\ge0\). Tangential maps extend as unitaries. Their laws and commutation pass by density.

Equations (6)–(7) apply to all terms in
\[
 \|(T_t^u-I)[F]\|^2
 =q_u(F,\tau_{2tu}F)-2\operatorname{Re}q_u(F,\tau_{tu}F)+q_u(F,F),
\]
and in the analogous unitary formula \(2q_u(F,F)-2\operatorname{Re}q_u(F,\tau_yF)\). For small \(t,y\) the supports lie in fixed separated neighborhoods. Hence these norms tend to zero. Approximation by \([F]\) costs at most twice its norm error, uniformly in \(t,y\), extending continuity to every vector.

If \(T_1^ua=0\), then \(\|T_{1/2}^ua\|^2=\langle a,T_1^ua\rangle=0\). Repeated halving and continuity give \(a=0\). The spectral measure of \(T_1^u\) has no atom at zero. Define \(H_u=-\log T_1^u\); the spectral subspaces \(T_1^u\in[1/N,1]\) show its domain is dense. Unique positive square roots give \(T_t^u=e^{-tH_u}\) for dyadic \(t\), then for every \(t\ge0\) by continuity. Its kernel is zero for \(t>0\), since \(e^{-tE}>0\).

The joint spectral theorem for the tangential unitary group and \(e^{isH_u}\) supplies their strongly commuting self-adjoint generators. Commutation with \(T_1^u\) passes to its spectral projections. Empty tuples are fixed, so every generator annihilates \(\Omega\). Equation (17) follows on representatives from (16) and then by density. Spatial signed permutations preserve \(q_{e_4}\), commute with \(\theta\), and preserve positive time; they therefore give the stated unitaries and covariance.

Finally choose rational box unions strictly inside the half-space and countable dense supported \(C^1\) families as in Lemma 2. Expanding the squared norm of an approximation error and applying (6) gives a countable total set after rational complex linear combinations. This proves separability. \(\square\)

### Lemma 6. The extended domain and the centering convention

For \(\varphi=\sigma\) or \(\sigma_S\), the finite positive-time flat sequence space has the positive form
\[
 Q(\Phi,\Psi)=\sum_{p,q}
           \Sigma^\varphi_{p+q}(\Theta\bar\Phi_p\otimes\Psi_q),
 \tag{19}
\]
where \(\Theta\) reflects every time argument and \(\Sigma^\varphi_0(1)=1\). Its completed quotient is canonically the compact-tuple Hilbert space of Lemma 5, with the same translations and \(W_3\). The spaces for \(\sigma\) and \(\sigma_S\) are unitarily equivalent, with vacuum and translations intertwined.

*Origin:* s4-s6 §7; bridge-check §2. SA lines 25905–25960. The explicit recentering is supplied here from (11), as in YM3_I IV-28-12/13/15.

*Proof.* Each tensor in (19) is flat on every pair diagonal. Internal diagonals are killed by the corresponding factor. At a cross diagonal of positive time the negative-time factor vanishes with all derivatives; at negative time the positive-time factor does; at zero time both are flat. For disjoint variable groups,
\[
 p_s(f\otimes h)\le p_s(f)p_s(h),
 \tag{20}
\]
because \(1+|x|^2+|y|^2\le(1+|x|^2)(1+|y|^2)\). Lemma 4 approximates every component by smooth separated tensors strictly above time zero. Equations (12) and (20) make their finite forms converge to (19). Positivity follows from Lemma 3.

These smooth tensors are total for the sequence form. They are also total for the compact form: mollify each entry at a common sufficiently small scale, preserving separation and the time gap; \(C^1\) convergence and (6) give convergence of the classes. Both forms agree on this common dense space, so its identity extends to a unitary between completions.

No zero tensor relation creates an extra vector. For smooth entries this follows from the distribution constructed in Lemma 4. For \(C^1\) entries, common slotwise mollification preserves a zero tensor identity and its smooth relations are null; their class limits are null too. This also justifies using actual tensor functions in place of the formal span.

For each fixed translation, the corresponding Schwartz map is continuous and preserves the positive-time domain when its time component is nonnegative. Apply it to the common approximating tensors. The unitary identification intertwines the actions; their boundedness and strong continuity were already proved on the compact domain. Spatial \(W_3\) intertwines in the same way. All affine coordinate and diagonal mirror positivities extend by the same constrained density, using coordinates normal to that mirror solely to construct approximations.

For the last assertion define, for real \(b\),
\[
 \mathsf{sh}_bX=\sum_{A\subset[n]}
                    \prod_{i\notin A}(b\int f_i)\,X_A .
\]
This preserves support domains, commutes with isometries and conjugation, and respects every defined concatenation. Expanding subsets gives \(\mathsf{sh}_b\mathsf{sh}_{b'}=\mathsf{sh}_{b+b'}\). By (11), \(\sigma_S=\sigma\circ\mathsf{sh}_{-c}\), whence
\[
 q^{\sigma_S}_u(F,G)=q^\sigma_u(\mathsf{sh}_{-c}F,\mathsf{sh}_{-c}G).
\]
The inverse shift proves surjectivity on the dense quotients. The resulting unitary fixes the vacuum and intertwines translations, hence their spectral measures. It also identifies the completed extended spaces through the preceding bridge. \(\square\)

### Lemma 7. A two-reflection measure estimate

Let \(\mu\) be a finite positive measure on \([0,\infty)\times\mathbb R\), and put \(w=(E-iq)/\sqrt2\). Suppose vectors \(a,b\) and self-adjoint \(A\ge0,B\) satisfy
\[
 \int e^{-sw-s'\bar w}\,d\mu
       =\langle a,e^{-sA}e^{-is'B}b\rangle\qquad(s,s'\ge0).
 \tag{21}
\]
Then \(\mu\{|q|>E\}=0\). Commutation of \(A,B\) is not required.

*Origin:* cone-o6 §3; bridge-check §3. YM3_I IV-28-17, lines 75480–75530.

*Proof.* For \(c\in L^1(0,\infty)\), set \(p(z)=\int_0^\infty c(s)e^{-sz}\,ds\). Multiply (21) by \(c(s)\overline{c(s')}\) and integrate. The kernels on the left and the operators on the right have norm at most one, so Fubini applies. With \(C=\|a\|\|b\|\) and \(p^\sharp(y)=\overline{p(-iy)}\), spectral calculus in the displayed order gives
\[
 \int|p(w)|^2\,d\mu
 =\langle a,p(A)p^\sharp(B)b\rangle
 \le C\sup_{x\ge0}|p(x)|\sup_{y\in\mathbb R}|p(iy)|.
 \tag{22}
\]
The left side is real nonnegative; the last step bounds the absolute value of the matrix element.

Take \(\alpha=\varepsilon+i\kappa\), \(\varepsilon,\eta>0\), \(\kappa\in\mathbb R\), and
\[
 c(s)=\frac{s^{\alpha-1}e^{-\eta s}}{\Gamma(\alpha)},\qquad
 p(z)=(z+\eta)^{-\alpha}.
 \tag{23}
\]
Here is the normalization by hand. Define \(\Gamma(\alpha)=\int_0^\infty t^{\alpha-1}e^{-t}\,dt\). Integrating the beta integral by parts \(N\) times and setting \(t=s/N\) gives
\[
 \Gamma(\alpha)=\lim_{N\to\infty}
       \frac{N!\,N^\alpha}{\alpha(\alpha+1)\cdots(\alpha+N)}.
 \tag{24}
\]
Dominated convergence uses \((1-s/N)^N\le e^{-s}\) for \(0\le s\le N\). This limit is nonzero: the product is
\(\alpha^{-1}N^\alpha\prod_{k=1}^N(1+\alpha/k)^{-1}\).
Its logarithm converges to a finite number. Indeed \(\sum_{k=1}^Nk^{-1}-\log N\) is nonnegative and decreasing, by integral comparison, and
\[
 \log(1+z)-z=-z^2\int_0^1\frac{t}{1+tz}\,dt,\qquad
 |\log(1+z)-z|\le |z|^2\quad(|z|\le\tfrac12)
\]
makes the logarithmic tail absolutely summable. All finitely many remaining factors are nonzero since \(\operatorname{Re}\alpha>0\). The limit is a nonzero exponential.

Substitution proves (23) for positive real \(z+\eta\); differentiation under exponential majorants gives holomorphy, so the identity theorem proves it throughout \(\operatorname{Re}(z+\eta)>0\). Also \(c\in L^1\). With the principal logarithm, the suprema in (22) are bounded by \(\eta^{-\varepsilon}\) and \(\eta^{-\varepsilon}e^{|\kappa|\pi/2}\). Therefore
\[
 \int|w+\eta|^{-2\varepsilon}e^{2\kappa\arg(w+\eta)}\,d\mu
       \le C\eta^{-2\varepsilon}e^{|\kappa|\pi/2}.
\]
Fatou first as \(\varepsilon\downarrow0\), then as \(\eta\downarrow0\), gives
\[
 \int_{w\ne0}e^{2\kappa\arg w}\,d\mu\le Ce^{|\kappa|\pi/2}.
 \tag{25}
\]
For every \(\delta>0\), the set \(\arg w\ge\pi/4+\delta\) has measure at most \(Ce^{-2\kappa\delta}\) for all \(\kappa>0\). Let \(\kappa\to\infty\). Negative \(\kappa\) treats the lower sector. Their countable union over \(\delta=1/m\) is exactly \(\{|q|>E\}\), since \(\operatorname{Re}w\ge0\). \(\square\)

### Lemma 8. The spectral cube cone

In the coordinate-time Hilbert space of Lemma 5, for either centering, the joint spectral measure \(\mathsf E\) obeys
\[
 \mathsf E\{(E,p):E<\max_{1\le i\le3}|p_i|\}=0.
 \tag{26}
\]
Thus \(H\ge|P_i|\) in the joint spectral and quadratic-form senses.

*Origin:* cone-o6 §4; bridge-check §3. YM3_I IV-28-21, lines 75532–75576. This is the two-continuum-reflection proof, with no lattice plateau or phase input.

*Proof.* Fix \(i\). Put \(u=(e_4+e_i)/\sqrt2\), \(v=(e_4-e_i)/\sqrt2\), \(r=\theta_u\theta\), and \(W_i=\{x:x_4>|x_i|\}\). If \(F\in V(W_i)\), then \(F,rF\in V_u\): as point maps, \(r(x_i,x_4)=(x_4,-x_i)\), so
\[
 u\cdot x=(x_4+x_i)/\sqrt2>0,\qquad
 u\cdot rx=(x_4-x_i)/\sqrt2>0.
\]
Push the finite positive measure \(\langle[F],\mathsf E(\cdot)[F]\rangle\) forward by \((E,p)\mapsto(E,p_i)\), calling it \(\mu_F\). With \(w=(E-ip_i)/\sqrt2\), one correlation has two representations:
\[
 \begin{split}
 \int e^{-sw-s'\bar w}\,d\mu_F
 &=\varphi(\theta\bar F\cdot\tau_{su+s'v}F)\\
 &=\langle[rF]_u,e^{-sH_u}e^{-is'Q}[F]_u\rangle_u,
 \end{split}\qquad s,s'\ge0.                         \tag{27}
\]
The first uses (17) and \(su+s'v=((s+s')e_4+(s-s')e_i)/\sqrt2\), with the fixed convention \(U_x=e^{ix\cdot P}\). The second uses \(\theta_ur=\theta\), Lemma 5, and \(U^u(s'v)=e^{-is'Q}\), where \(Q\) is the negative tangential momentum generator. Every concatenation is separated: its coordinate halves retain their time gap, and its diagonal halves stay on opposite sides of \(u\cdot x=0\). No invariance under \(r\) is used.

Lemma 7 shows that \(\Pi_i=\mathsf E\{E<|p_i|\}\) annihilates \([F]\). For arbitrary \(F\in V_{e_4}\), a sufficiently large positive time shift \(\tau_{Re_4}\) puts all its finitely many compact supports in \(W_i\). Thus \(\Pi_iT_R[F]=0\). Strong commutation gives \(T_R\Pi_i[F]=0\), and injectivity of \(T_R\) gives \(\Pi_i[F]=0\). These classes are dense, so \(\Pi_i=0\). The three indices give (26).

For \(\mu_\psi(B)=\langle\psi,\mathsf E(B)\psi\rangle\), integration of \(|p_i|\le E\) proves
\[
 \operatorname{Dom}H^{1/2}\subset\operatorname{Dom}|P_i|^{1/2},\qquad
 \||P_i|^{1/2}\psi\|^2\le\|H^{1/2}\psi\|^2.
 \tag{28}
\]
Integration of \(p_i^2\le E^2\) also gives
\(\operatorname{Dom}H\subset\operatorname{Dom}P_i\) and
\(\|P_i\psi\|\le\|H\psi\|\).
Lemma 6 transfers the same spectral statement to the extended domain. The spatial section of (26) is a cube; no round-cone inequality is asserted. \(\square\)

### Theorem 9. CL1

Assume **SR1, LG1 and IN1(4)** in the precise forms I1–I3, with the constant order above. Let \((K_j,\beta_j)\) be first-passage data at the fixed admitted \(g\), with \(K_j\to\infty\), \(a_j=L^{-K_j}\), and centering states \(\nu_j\in\mathcal G_{a_j,\beta_j}\). Let \(\rho_j\in\mathcal G_{a_j,\beta_j}\) be the integrating states; the self-centered case is \(\rho_j=\nu_j\).

1. **Compactness.** One subsequence makes the \(\nu_j\)-centered moments converge on every separated \(C^1\) tuple, with the countable extension, moving tests, mirrors, one-point and cumulant limits above. Volume-first subsequential limits exist. Every volume-first limit of the connected functions is a limit of SA 0(a)(iii) type.
2. **Inheritance.** The connected limit \(S\) is invariant under translations and \(W_4\), symmetric, real, and regular on \(\mathbb E^n_{\ne}\): each \(S_n\) has a unique distribution of locally finite order with the prescribed smooth tensor values. Its centered functional \(\sigma_S\) is reflection positive at every coordinate and diagonal affine mirror. The same inheritance holds for the original two-state moments \(\sigma\).
3. **Hilbert space (H2).** On \(\mathbb C\mathfrak S(\{x_4>0\})\), the form
   \(\langle F,G\rangle=\sigma_S(\theta\bar F\cdot G)\)
   defines a separable completed quotient \(\mathcal H(S)\). It carries strongly continuous self-adjoint contractions \(e^{-tH}\), \(H\ge0\), \(H\Omega=0\); a strongly continuous unitary representation \(e^{ix\cdot P}\) of \(\mathbb R^3\) commuting strongly with \(H\); and a unitary representation of \(W_3\). The spatial actions fix \(\Omega\), and \(W_3\) commutes with \(H\). The same structures act on the canonically identified diagonal-flat extended completion.
4. **Cones.** On that space \(H\ge|P_i|\), \(i=1,2,3\), in the senses (26)–(28). The joint spectrum lies in the cube cone \(E\ge\|p\|_\infty\).

*Origin:* s4-s6 and cone-o6, with bridge-check §§2–3. The explicit volume-first recognition argument below supplies a step absent from those two notes, by the forward implication of YM3_I IV-21-28/33, lines 74449–74485, adapted to (1).

*Proof.* I1 supplies data of unbounded cutoff depth. Lemma 1 supplies torus-limit states at each datum; Lemma 2 extracts the common cutoff subsequence. Lemmas 3–4 prove the inheritance and regularity, including canonical centering. Lemmas 5–6 prove H2, and Lemma 8 proves its cone.

It remains to justify the finite-torus realization of every volume-first limit. Fix a defining sequence \(\rho_j\in\mathcal G^{\rm tor}_{a_j,\beta_j}\). At one fixed \(j\), there are finitely many plaquettes whose barycenters lie in \(B(0,j)\); call their number \(N_j\). Along a sequence of torus laws converging weakly to \(\rho_j\), every cumulant of these plaquette variables converges, including repeated indices. This follows from weak convergence of their bounded continuous product functions and the finite polynomial formula (10).

Choose a compatible torus on that sequence with side \(\ell_j\ge j\), large enough to embed this ball and its incident bonds. Choose it so that every such plaquette cumulant of orders \(2\le n\le j\) differs from its \(\rho_j\) value by at most
\[
 \frac{1}{j\,\max(1,N_j)^j}.
\]
There are finitely many requirements at this fixed \(j\), so convergence permits this choice. For bounded \(f_i\) supported in the ball, multilinearity of the finite sum (1) then gives
\[
 \left|\kappa_n^{\mu_{a_j,\ell_j,\beta_j}}
          (\mathcal O(f_1),\ldots,\mathcal O(f_n))
       -\kappa_n^{\rho_j}
          (\mathcal O(f_1),\ldots,\mathcal O(f_n))\right|
 \le\frac1j\prod_i\|f_i\|_\infty\qquad(2\le n\le j).
 \tag{29}
\]
Every fixed compact tuple eventually meets these conditions. The same first-passage pairs therefore give its connected limit along finite tori with \(\ell_j\to\infty\). Canonically centered moments follow by (3). This is exactly SA 0(a)(iii) type. It neither identifies an arbitrary periodic DLR state as a torus limit point nor claims the converse for arbitrary growing-torus sequences. \(\square\)

## Source checks and definitions supplied

All external references below are at **31a47c543775**, credited to **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**. Outline objects were located through [sa-index/README.md](sa-index/README.md), chunks 01, 06, 22–23 and the corresponding rows of [obligations.md](sa-index/obligations.md), with neighboring rows read. The cited source passages were then read in bounded excerpts.

| Source passage checked | Use here |
|---|---|
| [SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), 6836–6940 | Observable, first passage, volume-first definition, 0(a)(iii), 0(b), and canonical centering. These clauses state the target; they do not discharge I1–I3. |
| SA, 24376–24905, CC1–CC18 | Lemmas 1–3, flat convergence, and the two-state/canonical distinction; detailed conditional proofs from the stated uniform bounds. |
| SA, 24927–24984 and 25073–25373, QF1–QF3 and QF8–QF22 | Lemma 4 and constrained density. The four-dimensional Fourier, grid and Taylor orders are used explicitly. The graded factorial implication is imported as SR1. |
| SA, 25424–25682 and 25905–25960, HB1–HB7a and HB16 | Lemmas 5–6; detailed conditional compact reconstruction and its separate flat-domain input. |
| SA, 25736–25903, HB8–HB15 | Compared with Lemma 8. This outline route reads the lattice plateau carrier; CL1 instead carries the checked YM3 continuum-reflection proof. |
| [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), 72903–73054 and 74343–74671 | Support-adapted extraction, centering, mirrors, and the forward volume-first recognition proof. Equation (29) uses four-dimensional (1), without YM3's spacing prefactor. |
| YM3_I, 75249–75577 | General reflection Hilbert space, recentering unitary, measure estimate, and two-reflection cone, all written here in four dimensions. |
| [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex), 64630–64700 and 68108–68235 | Compared its moment conventions and limits of the compact reconstruction. These passages do not supply the factorial bound or identify a curvature Hilbert space with a block-observable space. They supply no additional premise here. |

The requested outline and CA-I were each fetched once to the named scratch files. YM3_I and CA-II were each fetched once for the passages above. No CA-I or CA-III theorem is an additional import of this part. No raw manuscript was read whole.

Definitions made explicit in this distillation, including conventions previously left implicit:

1. The Wilson plaquette count, barycentric observable with no spacing prefactor, DLR class, compatible torus-limit class, first-passage data, and the two distinct orders of limits.
2. Separated support types and supported multilinearity; the formal tuple span with restricted concatenation; translation, isometry, conjugation, and affine mirror conventions.
3. The distinction between \(m_j,\sigma,S_n,\sigma_S\); the partition formulas and scalar shift \(\mathsf{sh}_b\).
4. Off-diagonal configuration space, diagonal-flat Schwartz space, seminorms, positive-time boundary flatness, and finite sequence domain.
5. The inner/expanded Fourier cubes, period, scaled derivative norm, dyadic layers and grid partition in Lemma 4.
6. Reflection-null quotients, vacuum, \(U_x=e^{ix\cdot P}\), strong commutation, the joint spectral measure, and the spectral/form-domain meaning of the cube cone.
7. The cone proof's diagonal frame \(u,v\), wedge \(W_i\), point map \(r\), negative tangential generator \(Q\), spectral pushforward \(\mu_F\), and principal-branch Laplace probe in Lemma 7.

## Result

**CL1 is proved as an implication from SR1, LG1 and IN1(4).** It gives volume-first subsequential limits, all coordinate and diagonal affine mirrors, off-diagonal distributions, the compact/flat Hilbert-space identification, and \(H\ge|P_i|\) with the cube cone. Its imports are exactly I1–I3, their stated constant order, and the named analytic background. Their actual-construction obligations remain Outstanding.

Corrections and completions made in distillation:

- Made the integrating states explicit and separated two-state moments from \(\sigma_S\). Included canonical recentering and its unitary identification.
- Added the finite-plaquette approximation (29) proving the stated volume-first-to-growing-torus implication. No converse or all-state torus recognition is assumed.
- Kept the gate's explicit Fourier geometry: inner side \(2\ell\), expanded side \(4\ell\), period \(8\ell\), and separation after enlargement. Wrote the smaller-box overlap and partition-independence argument.
- Kept the four-dimensional repair: eight Fourier derivatives per slot, \(h^{-4n}\) position counting, Taylor order \(10n+2\), and the summable \(h^2\) remainder. Used the polynomial separation bound, not arbitrary per-order constants, for the flat extension.
- Fixed the momentum convention to \(U_x=e^{ix\cdot P}\) and \(Q\) to the negative diagonal tangential generator. Stated both spectral and form domains for the cone.
- Retained the cutoff-sequence and lattice-symmetry inputs, reflection-invariant centering, and a nonnegative unit-integral bump. Replaced the notes' stale C1/OH1 pointer by the live named imports; preserved IN1's order and Amendment 1.
- Kept factorial growth as the SR1 import and the cone proof independent of the lattice plateau/phase argument. The compact and flat spaces are identified only for this same scalar moment functional.

The two source notes have the line-by-line check recorded above. **This distilled text, its added completions, and CL1 as a whole part are not yet refereed.** Every proof step here is a written hand argument. Text retrieval and editing supplied no mathematical discharge. This research text grants no status and does not establish the upstream Yang–Mills construction.

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/cl1-gate.md` (Claude fresh session, first failing step none):
1. Lines 208 and 273: "I3 improves A'_n to C_E^n (n!)^{k+32}" overstates SR1's H1, which covers the moment limits sigma, sigma_S, not the cumulant limits S_n or the lattice extensions Sigma_{j,n}. No clause of Theorem 9 uses that bound. SR1's Lemmas 7-9 need only the bound (28); the cumulants meet it by the third line of (4) and the lattice forms meet it at each j (SA (QF1), L24929-24946).
2. Symbol clashes, read as follows: the growth constant C_E is C_{H1} (distinct from IN1's row-7 C_E); the one-point constant c of Lemma 3 is c_sigma (distinct from IN1's reserve product c = C_v c_r).

## Change log (2026-11-13)

Item 1 of the pass 3 change log is now applied in the text. Before this edit, line 208 (statement of Lemma 4) and line 273 (end of its proof) still gave the factorial bound \(C_E^n(n!)^{k+32}\) to all the forms of (12). The scope review of PR #10141 held the snapshot on 2026-11-11 for that reason. Both sentences now give the bound to the limit forms of the moments \(\sigma_n\) and \((\sigma_S)_n\) only. Lemma 4 states no such bound on the flat extensions of the cumulant limits \(S_n\) or of the lattice forms \(\Sigma_{j,n}\); their separated-tuple bounds (4) are unchanged. No other line of this part is changed.

Edit: Claude (Fable 5.2), 2026-11-13. The read of the edited lemma by another model is recorded in [cl1-l4-read.md](../gates/cl1-l4-read.md).

**Status: frozen**, as a conditional implication from SR1, LG1 and IN1(4). Reopens only on a `wrong` signal or when an import it reads changes.
