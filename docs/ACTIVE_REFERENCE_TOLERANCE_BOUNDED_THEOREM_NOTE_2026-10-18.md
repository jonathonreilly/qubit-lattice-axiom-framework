# Structured reference tolerances for the continuously active loader

Claim type: bounded_theorem.
Primary runner: `scripts/product_reference_attachment_controls_2026_10_18.py`.

Publication evidence boundary: The complete arguments below and their supporting derivations remain the mathematical basis, with exactly their stated suppliers and hypotheses. Original review dispositions, author-time statuses and old hashes record history; they are not fresh execution evidence or authority. Current live source identities are listed in `outputs/product_reference_attachment_review_2026_10_18/INPUT_CLOSURE.json`. The shared primary supplies finite matrix and budget controls, not a simulation of the enormous apparatus or a proof of physical supply.

Claim type: bounded_theorem, conditional on the explicit supplied Hamiltonian and input. Both the independently weighted reference-bond source and the centered-gap/simultaneous extension have supporting distinct checks and ROOT acceptance at their stated scopes. This manuscript is synthesis by their author, not another independent validation or retained audit. Exact source and review identities appear in section9.

The [active-energy cubic-loader parent](ACTIVE_ENERGY_CUBIC_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md) uses supplied positive one- and two-qubit blocks to implement a finite-window approximation to a fixed coherent loading operation while the literal \(\omega n_P\) remains installed. This extension relaxes two reference suppliers within explicit structured classes:

1. Every nearest-neighbor reference bond may have an independent positive weight in a declared interval; the weights need not be equal or individually known.
2. Reference occupation energies may have small static centered offsets. Their individual values need not be calibrated, but their mean remains exactly \(\omega\), equal to P's gap.

An explicit simultaneous proof is required because two separately controlled changes do not automatically compose. The family below provides that proof and retains the parent's complete-output vector allowance \(<7\epsilon/128\), fixed logical operation, counts, incident cap and eventual sufficient full-loader time order \(\Theta((\Lambda-\omega)^{-1}\epsilon^{-2})\) at fixed positive weight ratio. The centered offset ceiling is \(\lambda/N\), eventually of order \((\Lambda-\omega)\epsilon^4\).

With unequal reference gaps, the **actual unequal-gap free Hamiltonian is generally not conserved** by the interactions. The nominal uniform excitation-energy operator is conserved, as is the total static Hamiltonian. This change in the energy-conservation contract is explicit; it is not hidden by using a nominal free factor in the proof. The result is not a generic matrix-error, manufacturing, preparation, capture or permanent-halt theorem.

## 1. Actual device, input and one complete fixed-gate prescription

Use the parent's four-rail head and five-layer suffix, with shared ordinary qubits Q,P,R. Q and R are freely degenerate. Every extra reference \(\mathcal E\) is passive. The reference grid is \(V=\{0,\ldots,n-1\}^3\), with \(N=n^3\) qubits and corner e attached to P. Set \(M=\Lambda-\omega>0\) and fix \(0<\epsilon\le1\), \(0<\eta\le1\).

The physical local blocks are
\[
\begin{gathered}
 a(I+X_Q),\quad b(I+Z_Q),\quad b(I+Z_P),\quad c(I+Z_QZ_P),\\
 g(I+\sigma_P^+\sigma_e^-+\sigma_P^-\sigma_e^+),\\
 \kappa_{uv}(I-\operatorname{SWAP}_{uv})\quad(uv\text{ a grid edge}),\\
 \omega n_P,\qquad (\omega+\delta_v)n_{B_v}\quad(v\in V),
\end{gathered}                                                     \tag{1}
\]
where \(n_D=|1\rangle\langle1|_D\), \(\sigma_D^+=|1\rangle\langle0|_D\), and
\[
 a=\lambda/\sqrt2,\quad b=\sqrt5\lambda/4,\quad
 c=3\lambda/4,\quad g=\sqrt2\lambda,\quad s=a+2b+c+g.
\]
Each reference bond retains exactly its positive swap matrix; only its scalar weight varies. Each offset changes the coefficient of an existing positive occupation block. A negative \(\delta_v\) is not a separately installed negative block.

A single sufficient policy for simultaneous weights and centered offsets is
\[
\begin{aligned}
 C_P&=(\sqrt5+3)/2+2\sqrt2,\\
 n&=\left\lceil(8192\pi^2/\epsilon^2)^{1/3}\right\rceil,
 &N&=n^3,\\
 \kappa_{\max}&=M/32,
 &\Delta_w&=\eta\kappa_{\max}/(3n^2),\\
 L&=\left\lceil\max\{16,(8192/\epsilon)^2\}\right\rceil,
 &J_{\rm budget}&=M/64,\\
 \lambda_{\max}&=\min\left\{
 \frac\omega2,\frac{M}{4C_P},\frac{\Delta_w}{16},
 \frac{\epsilon\eta\kappa_{\max}}{524288n},
 \frac{4J_{\rm budget}}{L+1}\right\},\\
 m&=\left\lceil\frac{\omega}{2\lambda_{\max}}\right\rceil,
 &\lambda&=\frac{\omega}{2m},\\
 \alpha&=\lambda/2,
 &\tau&=\pi/\lambda=2\pi m/\omega,\\
 J_c&=\lambda(L+1)/4,
 &C_{\rm head}&=4J_c,\\
 w&=\min\left\{
 \frac{\epsilon}{128(\omega+9\lambda/4)},
 \frac{\epsilon}{1024\lambda},\frac{\epsilon}{64\lambda L}
 \right\}.
\end{aligned}                                                       \tag{2}
\]
After these parameters are fixed, allow **every** deterministic assignment satisfying
\[
 \eta\kappa_{\max}\le\kappa_{uv}\le\kappa_{\max},\qquad
 |\delta_v|\le\lambda/N,\qquad \sum_v\delta_v=0.       \tag{3}
\]
The coefficients are static. There is no probabilistic independence or favorable averaging assumption; bond and offset assignments may be adversarially correlated. The policy does not use their individual values. It does require their declared bounds and the exact centered mean. The case \(\delta_v=0\) is included; an uncentered independent interval box is not.

The head is exactly the parent's supplied structured clock: links
\(k_r=\alpha\sqrt{r(L+1-r)}\), common diagonal \(C_{\rm head}\), and the chronological suffix
\[
 H_b,\quad \operatorname{CZ}_{b,P},\quad H_b,\quad X_b,
 \quad\text{all-rail }X_R.                            \tag{4}
\]
All physical head compensations, signed exchange bonds, identity-diamond occupations, rails and terminations are retained as specified in the parent. No operator inverse, projection or new many-body block is installed.

Supply one head at the input coordinate, with auxiliary rail \(a_{\rm path}=1\), arbitrary coherent joint input on \(b,Q,P,\mathcal E\), \(R=0\), and every other head vacant. Independently supply \(\beta=|+\rangle^{\otimes N}\). The fixed logical operation is
\[
 U_f=I_{a_{\rm path}}X_R C_P^{(b)}\operatorname{SWAP}_{QP},\qquad
 C_P^{(b)}=|0\rangle\langle0|_P X_b+|1\rangle\langle1|_P I_b.
\tag{5}
\]
It maps \((b,q,p,0_R)\) to \((b\oplus(1-q),p_Q,q_P,1_R)\). Old-P/passive-reference information is retained on Q. The normalized complete target, using the actual selected L and coefficients, is
\[
 \mathcal V_t\xi=
 e^{-i(C_{\rm head}+s)t}i^Le^{-i\pi/4}
 E_{\rm out}U_f\xi\otimes\beta(t),\qquad
 \beta(t)=\bigl(e^{-it\omega n}|+\rangle\bigr)^{\otimes N}.
\tag{6}
\]
Here \(E_{\rm out}\) places the head at the external endpoint, with every other head vacant. The nominal reference profile in (6) is intentional; it is not the free product evolved with the individual \(\omega+\delta_v\). All reference outputs are retained and any discrepancy is part of the full error.

Under the stated supplied conditions, the common theorem is
\[
 \sup_{t\in[\tau-w,\tau+w]}
 \|e^{-itH_{\rm actual}}E_{\rm in}-\mathcal V_t\|
 <7\epsilon/128.                                      \tag{7}
\]
The norm is induced on the entire input, stable under arbitrary passive references. It gives unhalved stabilized complete-channel error \(<7\epsilon/64\), and
\[
 \Pr(\text{external endpoint AND }R=1)>1-(7\epsilon/128)^2.
\tag{8}
\]
No actual output is discarded, projected away or normalized conditionally to state (7). The window is positive and contained in \((0,2\pi/\lambda)\). This note keeps free revival and the fixed \(U_f\) contract; it does not import a no-revival aged target or output-ray dwell construction.

## 2. Kernel, full-space gap and weighted inverse range

Write
\[
 H_F=\sum_{uv}\kappa_{uv}(I-S_{uv}),\quad
 H_E=\omega(n_P+\sum_v n_{B_v}),\quad
 H_S=aX_Q+b(Z_Q+Z_P)+cZ_QZ_P,\quad W=H_S+V_{\rm loc}.
\]
Let \(\Pi\) project onto the fully symmetric reference space, with identities on all spectators, and \(\Pi_\perp=I-\Pi\). Every weighted positive edge annihilates \(\Pi\). Conversely zero energy forces every adjacent swap to fix the vector; connected-edge swaps generate every permutation. Thus the kernel is exactly \(\Pi\), even though nonuniform \(H_F\) need not commute with arbitrary permutations outside it.

Termwise positivity and the parent's full-spin cubic comparison imply
\[
 H_F\ge\Delta_w\Pi_\perp,\qquad H_F\Pi=\Pi H_F=0.      \tag{9}
\]
The inherited comparison uses axis-ordered endpoint paths, congestion at most \(n^4/2\), and complete-graph spin identity
\(\sum_{u<v}(I-S_{uv})=N(N+2)/4-S_{\rm total}^2\ge N\Pi_\perp\).
It is a full-reference-space gap, not a one-magnon lifting assumption.

Let \(\mathcal L_0\) be the uniform graph Laplacian, \(\mathcal L_\kappa\) the one with the actual edge weights, and \(d_e=e_e-N^{-1}\mathbf1\). Restrict inverses to the common zero-sum space Z. The finite path cosine eigenvalues obey
\(2-2\cos(\pi r/n)\ge4r^2/n^2\); product eigenvector point weights are at most \(8/n^3\). Consequently
\[
 \|\mathcal L_\kappa^+\|\le\frac{n^2}{4\eta\kappa_{\max}},
 \qquad
 \langle d_e,\mathcal L_0^+d_e\rangle
 \le\frac2n\sum_{m=1}^{n-1}\frac{3m^2+3m+1}{m^2}<14.
\tag{10}
\]
The shell has \((m+1)^3-m^3\le7m^2\) nonnegative triples. There is no constant-mode inversion.

On Z, \(\mathcal L_\kappa\ge\eta\kappa_{\max}\mathcal L_0\) gives inverse order by conjugating with \(\mathcal L_0^{-1/2}\) and inverting that positive operator. Hence
\(\langle d_e,\mathcal L_\kappa^+d_e\rangle<14/(\eta\kappa_{\max})\).
For the single positive inverse B, \(B^2\le\|B\|B\), so
\[
 \|\mathcal L_\kappa^+d_e\|^2
 <\frac{7n^2}{2\eta^2\kappa_{\max}^2}.               \tag{11}
\]
This does **not** square a noncommuting Loewner inequality. The loss relative to the uniform squared Green bound \(7n/\kappa^2\) is retained.

Define \(B_\pm(f)=\sum_v f_v\sigma_v^\pm\Pi\) for zero-sum f. Direct edge expansion gives
\[
 H_FB_\pm(f)=B_\pm(\mathcal L_\kappa f),\qquad
 \Pi B_\pm(f)=0.                                    \tag{12}
\]
On a symmetric Dicke state with r excitations, the lowering Gram coefficient is \(r(r-1)/(N(N-1))\); raising replaces r by N-r. Both are at most one, and different r have orthogonal output sectors for each sign. Thus \(\|B_\pm(f)\|\le\|f\|\) on the entire symmetric subspace, including correlated spectators.

Set \(A=\Pi_\perp H_F\Pi_\perp\) on its complementary space and \(C_W=\Pi_\perp W\Pi\). Only the corner exchange contributes. With \(f=\mathcal L_\kappa^+d_e\),
\[
 A^{-1}C_W=g[\sigma_P^+B_-(f)+\sigma_P^-B_+(f)],\qquad
 \|A^{-1}C_W\|<\frac{\sqrt7\lambda n}{\eta\kappa_{\max}}.
\tag{13}
\]
The two exchange directions have opposite final P labels; their squared norms add without an extra \(\sqrt2\). Equations (10)–(13) are uniform over the unknown weights.

## 3. Centered gap offsets and their exact offdiagonal range

Put \(D_\delta=\sum_v\delta_v n_{B_v}\), so
\[
 H_{\rm actual}=H_{\rm head}+H_E+sI+H_F+W+D_\delta.
\tag{14}
\]
Its full norm is exactly
\[
 \|D_\delta\|=\tfrac12\sum_v|\delta_v|\le\lambda/2,   \tag{15}
\]
because its spectrum consists of subset sums and the total coefficient sum is zero. Permutation symmetry gives \(\Pi D_\delta\Pi=0\). Therefore the compressed comparison remains the exact nominal symmetric star, not a detuned effective data gate.

For \(B_n(f)=\sum_vf_vn_{B_v}\Pi\), zero-sum f, the Dicke correlations \(\langle n_i\rangle=r/N\), \(\langle n_in_j\rangle=r(r-1)/(N(N-1))\) give
\[
 \|B_n(f)D_r\|^2=\frac{r(N-r)}{N(N-1)}\|f\|^2,
 \qquad \|B_n(f)\|\le\sqrt{\frac{N}{4(N-1)}}\|f\|.
\tag{16}
\]
Different r outputs are orthogonal. Thus, with \(C_\delta=\Pi_\perp D_\delta\Pi\),
\[
 \|C_\delta\|\le\frac{\lambda}{\sqrt{2N}}\le\lambda/2.
\tag{17}
\]
The full norm in (15) and the offdiagonal norm in (17) play different roles.

The exact occupation intertwiner is
\(H_FB_n(f)=B_n(\mathcal L_\kappa f)\). It identifies
\(A^{-1}C_\delta=B_n(\mathcal L_\kappa^+\delta)\).
For the simultaneous bound it suffices to use the conservative full gap:
\[
 \|A^{-1}C_\delta\|\le\frac{\|C_\delta\|}{\Delta_w}
 \le\frac{3\lambda\sqrt n}{\sqrt2\eta\kappa_{\max}}.
\tag{18}
\]
No orthogonality between the exchange-generated and occupation-generated ranges is assumed. The triangle inequality is used below. In the uniform case the exact graph inverse also gives the sharper estimate
\(\|A^{-1}C_\delta\|\le n^2\|C_\delta\|/(4\kappa)\), but the stated policy does not need it.

## 4. A complete simultaneous elimination estimate

Write \(C=C_W+C_\delta\) and
\(D_\perp=A+\Pi_\perp(W+D_\delta)\Pi_\perp\).
From \(\|W\|<4\lambda\), (15), and \(\lambda\le\Delta_w/16\), the complementary perturbation is below \(\Delta_w/2\). Its ordered Neumann inverse gives
\[
 \zeta:=\|D_\perp^{-1}C\|
 \le2(\|A^{-1}C_W\|+\|A^{-1}C_\delta\|)
 <\frac{12\lambda n}{\eta\kappa_{\max}}.             \tag{19}
\]
In particular no inverse on \(\Pi\) is taken and no commutation of the two inverse factors is required.

For evolution from any normalized \(\xi\in\Pi\), decompose the state under \(H_F+W+D_\delta\) into \(p(t)+q(t)\). The equations are
\[
 ip'=\Pi W\Pi p+C^*q,\qquad iq'=Cp+D_\perp q,
 \qquad q(0)=0.
\]
Because \(\Pi D_\delta\Pi=0\),
\[
 \|p'\|\le4\lambda+\|C_\delta\|\le4.5\lambda,
 \qquad \|C\|\le g+\|C_\delta\|<2\lambda.            \tag{20}
\]
The extensive diagonal norm is needed for inverse existence, but is not inserted into \(\|p'\|\). Integrating the q equation once by parts keeps the operator \(D_\perp^{-1}C\) in its endpoints and integral. Duhamel on p then yields the complete bound
\[
 E_{\rm elim}\le\zeta[2+vt+c_*(2t+vt^2/2)],
 \quad v=4.5\lambda,\ c_*=2\lambda.
\]
For \(0\le t\le2\pi/\lambda\) the bracket is at most
\(2+17\pi+18\pi^2<259\). Since \(12\cdot259<4096\),
\[
 E_{\rm elim}<4096\frac{\lambda n}{\eta\kappa_{\max}}.
\tag{21}
\]
This is the explicit simultaneous proof. It retains every complementary output and is stable under passive references. It uses the actual weighted, detuned apparatus, not two separate perturbation estimates that are presumed to compose.

For comparison, the sharper separate variants are:

| Reference class | Inverse-existence condition | Complete elimination ceiling on \([0,2\pi/\lambda]\) |
|---|---|---|
| Arbitrary allowed weights, zero offsets | \(\lambda\le\Delta_w/8\) | \(2048\lambda n/(\eta\kappa_{\max})\) |
| Uniform bonds, centered offsets as (3) | \(\lambda\le\Delta/16\), \(\Delta=\kappa/(3n^2)\) | \(4096\lambda\sqrt n/\kappa\) |
| Both variations | \(\lambda\le\Delta_w/16\) | (21) |

The uniform centered bound uses the parent's exchange numerator \(\sqrt{14}\lambda\sqrt n/\kappa\), plus the detuning numerator \(3\lambda\sqrt n/(\sqrt2\kappa)\). After the Neumann factor the sum is below \(14\lambda\sqrt n/\kappa\), and \(14\cdot259<4096\). The weighted-only bound uses the original \(4\lambda\) derivative and \(g\) offdiagonal norm. These separate estimates remain distinct from the common conservative policy (2).

## 5. Closing the actual full-output comparison

The compressed star is unchanged because the kernel and \(\Pi D_\delta\Pi=0\) are exact. On the supplied \(\beta\), its residual relative to
\[
 H_{\rm eff}=a(X_Q+X_P)+b(Z_Q+Z_P)+cZ_QZ_P
\]
is \(g/(2\sqrt N)\). The parent's exact spectrum gives
\(\|H_{\rm eff}\|=9\lambda/4\) and
\(e^{-i\tau H_{\rm eff}}=e^{-i\pi/4}\operatorname{SWAP}_{QP}\).
The nominal free/scalar factors restore in the order
\[
 e^{-ist}[e^{-it\omega n_P}e^{-itH_{\rm eff}}\xi]
 \otimes\beta(t).
\tag{22}
\]
At \(\tau=2\pi m/\omega\) the nominal free factor revives; timing costs at most \((\omega+9\lambda/4)|t-\tau|\). There is no separate phase \(t\sum\kappa_{uv}\) or \(t\sum\delta_v\): the ferromagnet remains intact and its symmetric energy is zero, while the centered occupation compression is exactly zero.

Every suffix prefix acts trivially on the reference, and hence commutes with both the actual \(H_F\) and \(D_\delta\). It also commutes with nominal \(H_E\) and \(H_S\). Its only gauge defect remains the actual corner exchange conjugation, supported at virtual \(x\ge L-10\), of norm at most \(2g\). The parent proves the complete time-zero-to-window integral on the benchmark containing the actual local apparatus:
\[
 E_{\rm join}(t)<64/\sqrt L+2\sqrt2\lambda w<\epsilon/64,
 \qquad0\le t\le\tau+w.                             \tag{23}
\]
Actual joint evolution need not factorize. No term proportional to \(\|D_\delta\|t\) is inserted into that already exact benchmark comparison.

The original head endpoint estimate, without using the optional aged-window refinement, is
\(E_{\rm head}\le(\lambda L/2)|t-\tau|\le\epsilon/128\).
All budgets in the fixed-gate policy are simultaneous:

| Complete-vector contribution | Allowance |
|---|---:|
| Simultaneous local elimination (21) | \(<\epsilon/128\) |
| Star residual \(gt/(2\sqrt N)\) | \(<\epsilon/64\) |
| Nominal free/effective-gate timing | \(\le\epsilon/128\) |
| Actual suffix overlap (23) | \(<\epsilon/64\) |
| Whole head endpoint replacement | \(\le\epsilon/128\) |

Their sum is \(<7\epsilon/128\). At the physical endpoint the arm rotation is identity and the forward prefix is \(+X_RC_P^{(b)}\), proving exactly (6)–(8). Both possible input b states share the same scalar clock, so arbitrary coherent path input introduces no extra square-root rail factor. Every initial and output reference is retained.

If desired, the parent's original larger floor \(L=\lceil\max\{16,(2^{20}/\epsilon)^2\}\rceil\) also works with all dependent quantities recomputed; its original join bound gives the same allowance. Neither choice adds an output ray or a permanent completion mechanism.

## 6. Positive blocks, cap and counts

Condition (2) gives \(\lambda\le\omega/2\), so
\(\omega+\delta_v\ge\omega-\lambda/N>0\).
Also \(|\delta_v|\le\lambda/N<M/8\). Thus (1) stays within positive one-/two-body blocks for every allowed assignment. An independently varying bond has full norm \(2\kappa_{uv}\le2\kappa_{\max}\); the upper cap bound, not a compressed low-energy value, is used.

The head's compensating occupations remain positive because their subtracted local diagonal is at most \((\sqrt2+1)J_c<C_{\rm head}\). Its block inventory and the local inventory are unchanged. There are
\[
 \begin{aligned}
 \text{head qubits}&=4(L+1),&\text{head blocks}&=8L+34,\\
 \text{all qubits}&=4L+N+7,&
 \text{all blocks}&=8L+N+40+3n^2(n-1).
 \end{aligned}                                      \tag{24}
\]
The local count is \(N+1\) occupation blocks, five data/exchange blocks and \(3n^2(n-1)\) grid bonds. Modifying a coefficient does not add another physical block.

Full-support incident sums obey
\[
\begin{aligned}
 \operatorname{load}(P)&\le\omega+C_P\lambda+8J_c
                      \le\omega+M/4+M/8,\\
 \operatorname{load}(Q)&<M/4,&\operatorname{load}(R)&\le M/4,\\
 \operatorname{load}(\text{head})&\le(5+\sqrt2)M/64,\\
 \operatorname{load}(B_v),\ v\ne e&\le\omega+M/8+12\kappa_{\max}
                                  =\omega+M/2,\\
 \operatorname{load}(B_e)&<\omega+M/8+6\kappa_{\max}+M/4
                         =\omega+9M/16.
\end{aligned}                                                       \tag{25}
\]
Every ceiling is below \(\Lambda\). Negative offsets do not cause a sign problem, and positive offsets are charged explicitly.

The unchanged placement is P=(0,0,0), R=(1,0,0), Q=(0,0,-1), and \(B_{i,j,k}=(-1-i,-j,-k)\). The suffix occupies its parent cube \(\{0,1,2,3\}^3\), with eight distinct upward rays. The reference grid and Q are disjoint from all heads. Reference, corner-P and QP edges are nearest-neighbor; suffix range is at most nine and maximum total graph degree is eight at R. The complete loader is not asserted to be a nearest-neighbor cubic device. Unlisted geometric adjacencies do not install interactions.

## 7. Sufficient resources and what the tolerance comparison establishes

At fixed \(\eta,\omega,M>0\), \(n=\Theta(\epsilon^{-2/3})\), \(N,L=\Theta(\epsilon^{-2})\). In (2), the simultaneous accuracy constraint is of order \(\eta M\epsilon^{5/3}\), the gap constraint of order \(\eta M\epsilon^{4/3}\), and the clock cap of order \(M\epsilon^2\). The clock eventually dominates. Since \(\lambda_{\max}/2<\lambda\le\lambda_{\max}\),
\[
 \text{qubits, blocks}=\Theta(\epsilon^{-2}),\quad
 \tau=\Theta(M^{-1}\epsilon^{-2}),\quad
 \lambda/N=\Theta(M\epsilon^4).                     \tag{26}
\]
The eventual statement is not uniform as \(\eta\to0\); the crossover can be very unfavorable. The finite minimum (2), enormous head floor and all coefficient conditions are the actual prescription. The fixed-gate window retains \(w=\Theta(\epsilon)\) and \(w/\tau=\Theta(\epsilon^3)\) at fixed parameters. No wider aged-target or ray-dwell statement is included.

For comparison, ordinary finite-time Duhamel gives
\[
 \|[e^{-itH_{\rm actual}}-e^{-itH_{\delta=0}}]E_{\rm in}\|
 \le t\|D_\delta\|\le tNd/2
\]
when \(|\delta_v|\le d\). To assign an additional vector allowance b over horizon T, \(d\le2b/(NT)\) is sufficient. At \(b=\Theta(\epsilon)\), \(T=\Theta(1/\lambda)\), this certificate allows order \(\epsilon\lambda/N\), eventually order \(M\epsilon^5\). The centered ferromagnetic argument certifies the larger interval of order \(M\epsilon^4\). This is a comparison of sufficient estimates; it does not show that offsets above either ceiling cause failure or that the new tolerance is optimal. With \(d=\lambda/N\), the crude bound over \(2\pi/\lambda\) is only \(\pi\); the new small error follows from the structured projection and inverse argument.

The standalone specialization omits the head and R. Use
\(n_{\rm st}=\lceil(512\pi^2/\epsilon^2)^{1/3}\rceil\), \(N_{\rm st}=n_{\rm st}^3\), \(\kappa_{\max}=M/32\), \(\Delta_w=\eta\kappa_{\max}/(3n_{\rm st}^2)\), and
\[
 \lambda_{\max}^{\rm st}=
 \min\{\omega/2,M/(2C_P),\Delta_w/16,
              \epsilon\eta\kappa_{\max}/(131072n_{\rm st})\}.
\tag{27}
\]
Keep revival rounding and \(w_{\rm st}=\epsilon/[32(\omega+9\lambda/4)]\), with offsets bounded by \(\lambda/N_{\rm st}\). It yields complete vector/channel bounds \(<\epsilon/8,<\epsilon/4\), and center vector ceiling \(\epsilon/16\), with target \(e^{-i(st+\pi/4)}\operatorname{SWAP}_{QP}\xi\otimes\beta(t)\). Its qubit/block counts are \(N_{\rm st}+2\) and \(N_{\rm st}+6+3n_{\rm st}^2(n_{\rm st}-1)\); all edges are nearest-neighbor. The larger standalone data allowance gives corner load below \(\omega+13M/16\), still below cap.

The sharper separate standalone policies use the elimination table in section4: weighted-only uses \(\Delta_w/8\) and \(\epsilon\eta\kappa_{\max}/(65536n)\); uniform centered offsets use \(\Delta/16\) and \(\epsilon\kappa/(131072\sqrt n)\). All other standalone entries and reference-size conditions remain as just stated.

| Standalone reference class | Sufficient time order at fixed positive parameters |
|---|---|
| Parent uniform, no offsets | \(\Theta(M^{-1}\epsilon^{-4/3})\) |
| Nonuniform positive bonds, no offsets | \(\Theta((\eta M)^{-1}\epsilon^{-5/3})\) |
| Uniform bonds, centered offsets | \(\Theta(M^{-1}\epsilon^{-4/3})\) |
| Simultaneous weights and offsets | \(\Theta((\eta M)^{-1}\epsilon^{-5/3})\) |

These are different sufficient prescriptions. No optimality, practical hardware comparison or generic precision claim follows from the exponents.

## 8. Energy meaning and remaining suppliers

The installed local Hamiltonian factors using the nominal operator
\(H_E=\omega(n_P+\sum_v n_{B_v})\), since every physical term, including \(D_\delta\), commutes with it. Thus the full nominal charge distribution is conserved. The target reference in (6) is the common nominal profile because the centered D compression is zero; actual reference deviations and correlations are paid by the full norm bound.

The actual free occupation Hamiltonian is
\[
 H_{E,\rm actual}=\omega n_P+\sum_v(\omega+\delta_v)n_{B_v}
                =H_E+D_\delta.
\tag{28}
\]
A reference swap with \(\delta_u\ne\delta_v\), or the corner-P exchange when \(\delta_e\ne0\), generally fails to commute with (28). Therefore the parent's exact conservation of the actual equal-gap free energy is **not** transferred to arbitrary detuned spectra. The total static Hamiltonian remains conserved. Positivity is maintained by the actual occupation coefficients in (1). Nominal charge conservation is not a substitute claim of free-energy conservation for (28).

Even in the equal-gap case, the parent's complete-vector proximity does not certify exact reference-energy return or uniform control of extensive energy moments as N grows. Those limitations remain; no detuned reference reuse is supplied here. The initial coherent product state is still prepared externally to this theorem and is not obtained by cooling the ferromagnet.

The relaxed suppliers are precisely equal reference bond strengths and equal individual reference occupations within the centered interval (3). The declared lower bond bound, connected exact swap matrices, calibrated mean \(\sum\delta=0\), P gap \(\omega\), remaining local/clock coefficients, free revival, selective interactions, coherent head/reference inputs and blank apparatus remain. Arbitrary matrix perturbations, missing bonds, \(\eta=0\), time-dependent offsets, unknown mean or active \(H_{P\mathcal E}\) require new analysis. A nonzero mean gives \(\Pi D_\delta\Pi\ne0\), altering the effective dynamics and target; it is not silently covered.

Unknown individual values inside (3) do not enter the parameter selection or target, but the theorem does not derive certification of that interval from native physics. It neither implements a correcting gate nor permits a post hoc redefinition of the target. The record event, external arrival, stable capture and permanent halt remain distinct; the Hamiltonian keeps acting after the window. No preparation, cooling, reset, indefinite reuse or historical literal-processor realization is claimed.

## 9. Evidence map and synthesis exposure

Canonical destination: `docs/ACTIVE_REFERENCE_TOLERANCE_BOUNDED_THEOREM_NOTE_2026-10-18.md`. New evidence root: `outputs/active_reference_tolerance_2026_10_18/source_checks/`. The unchanged mathematical parent is the linked active-energy cubic note, 44932 bytes, SHA256 `8023deeb062288b75065576d89f726d528e077e7b10fac90333b33c61fbff110`. ROOT subsequently supplied publication context: regular PR9746 OPEN, head `8e119e9d45c30498a111e4e36d22f0676fdec4c6`, with unchanged canonical identity and source-manifest SHA256 `3e761b4431c60f80b4c4f05069ba37fcd88434844edf61a0a6beff3f9cff33fd`. These publication facts are parent-supplied context, not a fresh Git/remote check by this drafting worker; no merge is asserted.

| New frozen evidence | SHA256 | Disposition |
|---|---|---|
| Weighted reference source (`outputs/active_reference_tolerance_2026_10_18/source_checks/weighted_cubic_reference/PROPOSAL.md`) | `b2f4aaa21de3508c3d51ebf51fc6132a6ad16b8a9a836b3bc1ef9b75973294cb` | Scoped supporting check and ROOT acceptance |
| Weighted reference check (`outputs/active_reference_tolerance_2026_10_18/source_checks/weighted_cubic_reference_check/REVIEW.md`) | `8ce18b7cdea55345c292d391154713dff1940ff037e767aff96d47a523ccbb36` | SUPPORT for its exact structured class |
| Centered offsets and explicit simultaneous source (`outputs/active_reference_tolerance_2026_10_18/source_checks/reference_gap_detuning/PROPOSAL.md`) | `d2a4ffae8b2f7d2e2fc0aae7c654f78665c400e16d9d8e0dfb7eb4689c380c23` | Scoped supporting check and ROOT acceptance |
| Centered-offset and simultaneous check (`outputs/active_reference_tolerance_2026_10_18/source_checks/reference_gap_detuning_check/REVIEW.md`) | `11787f41138baea458ff7451424fabedde8b4a5f5fe185f1c30220311f38cf9e` | SUPPORT at the stated conditional scope; no required correction |

The source bodies remain unchanged, including historical pending labels. The later detuning review supports the explicit simultaneous proof, actual unequal-free-energy nonconservation and calibrated zero mean; ROOT fully read and accepted that disposition. This manuscript excludes the sources' optional aged-target extensions. The new packet carries the two new source/check pairs; inherited proof bodies remain linked in the parent's packet rather than recursively recopied.

The direct inherited closure is cubic gap (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_gap_swap/PROPOSAL.md`) `72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee` / check (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_gap_swap_check/REVIEW.md`) `507e83cce4949b58c8dbc0ba84339ba9af05e55fa02a11ab2da1a223c62997d7`; local exchange inverse (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_resolvent/PROPOSAL.md`) `7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895` / check (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_resolvent_check/REVIEW.md`) `25f290e96014dd8622575c207fd66f125ae2160727ca7d0b7a7bf35b7c3de3b5`; physical suffix (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_loader_interface/PROPOSAL.md`) `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570` / check (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_loader_interface_check/REVIEW.md`) `ebf747aa6327d0c240054d21eacf14c6b28aeae2fa9967d55101b9c25ce599a6`; and smaller head policy (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_suffix_prefactor/PROPOSAL.md`) `793e9706b867f415647f2f6b7370f8e0daba0bf5efb993be3373c5337e52d0d0` / check (`outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_suffix_prefactor_check/REVIEW.md`) `aa56fd71a965ef3a81e1f05a73d6a58706d4439d797952e31fba92c98eddc347`.

The parent's source map supplies the unchanged local/star proof and exact positive head primitives. No aged-output, output-ray, old degenerate-data performance or all-time record theorem is imported through genealogy.

ROOT proposed the inverse-energy, centered-offset and simultaneous-extension routes. This drafting worker authored both new sources and several inherited resolvent/suffix interfaces; it also read the complete weighted and centered-offset reviews at the exact identities above. The worker read the current parent completely, repairing a truncated aggregate display with bounded rereads. Synthesis of one's own source is not another independent check. The source/check workers share campaign ancestry and model/effort; their selective exposed checks are not blind replication, a physical realization or retained audit. The detuning disposition was inserted only after the actual complete review was read and its identity verified; this resolves the draft-time pending flag without rewriting the frozen author sources or implying an additional review of this synthesis.

The author changed only its research-directory manuscript. ROOT integrated this canonical note and frozen evidence packet after complete source/check and manuscript reads, followed by the changed disposition passages. Source reading and analytical reconstruction supplied the scientific checks; deterministic identities, links and citation topology supplied mechanical validation. No scientific executable, new simulation, blanket Lean run, physical validation or retained audit was performed. No physical axiom or editable prompt changed.

## Finite execution boundary

The primary retains all sectors of its declared small matrices, the scalar phases and complete outputs, and checks explicit sufficient coefficient/count budgets. It does not dynamically execute the proof texts. Uniform-in-volume estimates follow from the displayed arguments under their hypotheses; finite controls alone do not establish them. Infinite-lead scattering is not a finite product-seed launcher, and none of these controls supplies capture, reset or permanent halt.
