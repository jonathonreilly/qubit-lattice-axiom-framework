# A continuously active energy loader with a cubic product reference

This manuscript describes a time-independent Hamiltonian of supplied real positive one- and two-qubit blocks that approximates a complete loading operation while the literal energy \(\omega n_P\) remains active. A cubic array of equal-gap qubits begins in a supplied coherent product state. A continuously acting local interaction approximately swaps the ordinary qubits \(Q,P\); an engineered head clock applies a diagonal-P path/record suffix near that swap's revival. Every head, reference, data and passive-reference output is retained.

The complete finite-window vector error is \(<7\epsilon/128\). The explicit family below has \(\Theta(\epsilon^{-2})\) qubits and blocks and eventual sufficient time \(\Theta((\Lambda-\omega)^{-1}\epsilon^{-2})\), at fixed \(\Lambda>\omega>0\). Its standalone nearest-neighbor SWAP specialization has sufficient time \(\Theta((\Lambda-\omega)^{-1}\epsilon^{-4/3})\). These orders follow from an inverse bound on the actual exchange-generated reference range, together with a separately proved bound on the overlap of the running swap and the late suffix.

The four construction source/check pairs have scoped supporting distinct checks. A separate energy-accounting pair supports the identities in section 9 with a controlling wording qualification. Historical “pending” statements in frozen author texts record author-time status; the current source disposition and exact identities appear in section 10. This note records a selectively checked conditional theorem; it is not a retained audit or an assertion that its physical suppliers have been realized.

The two mathematical parents are the [local-reference static SWAP note](LOCAL_REFERENCE_STATIC_SWAP_BOUNDED_THEOREM_NOTE_2026-10-18.md) and the [exact positive two-body engineered-loader note](EXACT_TWO_BODY_ENGINEERED_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md). The latter supplies its local diamond/mixer/structured-coefficient identities and scalar clock, with the established engineered-transfer attribution recorded there. Its old degenerate-data performance and all-time exact record identity are not transferred. Separate uniform-ray dwell results are also outside this active-energy device.

## 1. Complete operation, input and explicit full-loader policy

Write \(n_D=|1\rangle\langle1|_D\), \(\sigma_D^+=|1\rangle\langle0|_D\), and \(\sigma_D^-=(\sigma_D^+)^*\). The ordinary qubits \(Q,P,R\) are shared throughout the apparatus. Q and R are freely degenerate; P has the continuously installed energy \(\omega n_P\), \(\omega>0\). Every extra input reference \(\mathcal E\) is passive. An arbitrary active interaction \(H_{P\mathcal E}\) is outside the model.

The moving head has four physical rails labelled by \((a_{\rm path},b)\in\{0,1\}^2\). These labels are positions of one head, not additional data qubits. The supplied input has \(a_{\rm path}=1\), an arbitrary coherent joint state of \(b,Q,P,\mathcal E\), exactly one head at the input coordinate \(x=0\), \(R=0\), and every other physical head vacant. Independently supply
\[
 \beta=|+\rangle^{\otimes N}
\tag{1}
\]
on the reference array. Coherent endpoint preparation, the product coherence, equal gaps and isolation are premises.

Define
\[
 C_P^{(b)}=|0\rangle\langle0|_P\otimes X_b
          +|1\rangle\langle1|_P\otimes I_b,\qquad
 U_f=I_{a_{\rm path}}\otimes X_R C_P^{(b)}
                         \operatorname{SWAP}_{QP}.
\tag{2}
\]
Products act right to left. On basis inputs,
\[
 (b,q,p,0_R)\longmapsto
 (b\mathbin{\oplus}(1-q),p_Q,q_P,1_R).
\tag{3}
\]
Linearity retains arbitrary correlations: the old P state and its passive-reference correlations move to Q.

Fix an incident cap \(\Lambda>\omega>0\), accuracy \(0<\epsilon\leq1\), and \(M=\Lambda-\omega\). The grid side length is \(n\), the number of reference qubits is \(N=n^3\), and the head length is \(L\). Choose
\[
 \begin{aligned}
 C_P&=(\sqrt5+3)/2+2\sqrt2,\\
 n&=\left\lceil(8192\pi^2/\epsilon^2)^{1/3}\right\rceil,
 &N&=n^3,\\
 \kappa&=M/32,
 &\Delta&=\kappa/(3n^2),\\
 L&=\left\lceil\max\{16,(2^{20}/\epsilon)^2\}\right\rceil,
 &J_{\rm budget}&=M/64,\\
 \lambda_{\max}
 &=\min\left\{\frac{\omega}{2},\frac{M}{4C_P},
       \frac{\Delta}{8},\frac{\epsilon\kappa}{262144\sqrt n},
       \frac{4J_{\rm budget}}{L+1}\right\},\\
 m&=\left\lceil\frac{\omega}{2\lambda_{\max}}\right\rceil,
 &\lambda&=\frac{\omega}{2m},\\
 \alpha&=\lambda/2,
 &\tau&=\pi/\lambda=2\pi m/\omega,\\
 J_c&=\lambda(L+1)/4,
 &C_{\rm head}&=4J_c,\\
 w&=\min\left\{\frac{\epsilon}{128(\omega+9\lambda/4)},
               \frac{\epsilon}{1024\lambda},
               \frac{\epsilon}{64\lambda L}\right\}.
 \end{aligned}
\tag{4}
\]
All coefficients are fixed before evolution. In particular \(J_c\leq J_{\rm budget}\), \(\lambda\leq\Delta/8\), and \(0<w<\tau\). The large \(2^{20}\) clock constant is part of this finite prescription.

Let
\[
 a_d=\lambda/\sqrt2,\quad b_d=\sqrt5\lambda/4,\quad
 c_d=3\lambda/4,\quad g=\sqrt2\lambda,\quad
 s=a_d+2b_d+c_d+g,
\]
and retain the complete free reference profile
\[
 \beta(t)=e^{-it\omega\sum_v n_{B_v}}\beta.
\tag{5}
\]
For the physical input insertion \(E_{\rm in}\), let \(E_{\rm out}\) place one head at the external endpoint \(x=L\) on each appropriate output rail, with every other head vacant. The normalized comparator is
\[
 \mathcal V_t\psi
 =e^{-i(C_{\rm head}+s)t}i^L e^{-i\pi/4}
       E_{\rm out}U_f\psi\otimes\beta(t).
\tag{6}
\]
The initial blank R is understood in \(E_{\rm in}\); it is flipped by \(U_f\). The common scalar is prescribed, with no phase fit.

For the actual constant Hamiltonian specified next,
\[
 \boxed{
 \sup_{t\in[\tau-w,\tau+w]}
 \left\|e^{-itH_{\rm tot}}E_{\rm in}-\mathcal V_t\right\|
 <\frac{7\epsilon}{128}.\ }
\tag{7}
\]
This is the induced complete-vector norm, stable under arbitrary passive input references. It implies unhalved stabilized complete-output channel error \(<7\epsilon/64\). Since the target lies entirely in the joint event “external endpoint and \(R=1\),” its actual probability is
\[
 \Pr(\text{external endpoint and }R=1)
 >1-(7\epsilon/128)^2.
\tag{8}
\]
No output is discarded or conditionally normalized in (7). Current \(R=1\), external arrival and permanent halt remain different statements.

## 2. The actual active-energy apparatus and head suffix

Let \(V=\{0,\ldots,n-1\}^3\), with a reference qubit \(B_v\) at every vertex and nearest-neighbor grid edges \(E\). Attach P to one corner \(e\). Install
\[
 \begin{gathered}
 a_d(I+X_Q),\quad b_d(I+Z_Q),\quad b_d(I+Z_P),
 \quad c_d(I+Z_QZ_P),\\
 g\bigl(I+\sigma_P^+\sigma_e^-+\sigma_P^-\sigma_e^+\bigr),\\
 \kappa(I-\operatorname{SWAP}_{uv}),\quad uv\in E,\\
 \omega n_P,\qquad \omega n_{B_v},\quad v\in V.
 \end{gathered}
\tag{9}
\]
Each block is real and positive on its full one- or two-qubit support. The exchange-plus-identity block has spectrum \(0,g,g,2g\); the ferromagnetic block has spectrum in \(\{0,2\kappa\}\).

In analytical notation their sum is
\[
 \begin{aligned}
 H_E&=\omega\left(n_P+\sum_vn_{B_v}\right),\\
 H_F&=\kappa\sum_{uv\in E}(I-\operatorname{SWAP}_{uv}),\\
 H_S&=a_dX_Q+b_d(Z_Q+Z_P)+c_dZ_QZ_P,\\
 V_{\rm loc}&=g(\sigma_P^+\sigma_e^-+\sigma_P^-\sigma_e^+),\\
 W&=H_S+V_{\rm loc},\qquad
 H_{\rm loc}=H_E+sI+H_F+W .
 \end{aligned}
\tag{10}
\]
Every term of \(H_F+W\) commutes with \(H_E\). Hloc stays installed throughout the operation. The effective transverse P term used later is a comparison, not an additional physical drive.

The head device uses the parent's full-support positive bond
\[
 Q_\eta(i,j;t)
 =t\left[n_i+n_j-\eta(\sigma_i^+\sigma_j^-
                       +\sigma_i^-\sigma_j^+)\right],
 \quad \eta=\pm1,\quad t>0,
\tag{11}
\]
whose spectrum is \(0,0,2t,2t\). A diamond on heads \(L_d,u,v,R_d\) uses the four signed outer bonds \(Q_+(L_d,u;a_L)\), \(Q_+(L_d,v;a_L)\), \(Q_+(u,R_d;a_R)\), \(Q_-(v,R_d;a_R)\), and the paired contacts
\[
 g_d n_u(I+D)+g_d n_v(I-D),
\tag{12}
\]
where \(D\) is \(Z_P\), \(X_R\), or the identity. Identity diamonds retain the nonzero \(2g_d n_u\) occupation and omit the zero v contact. The real arm rotation \(B=(u+v)/\sqrt2,\ C=(u-v)/\sqrt2\) and a data prefix turn this into a scalar segment with hoppings
\(-\sqrt2a_L,-g_d,-\sqrt2a_R\). Its forward data word is \(-D\), including the minus on an identity diamond. Physical arms retain the two prefix components through the inverse rotation; none is projected away.

The chronological suffix is
\[
 H_b,\quad \operatorname{CZ}_{b,P},\quad H_b,\quad X_b,
 \quad \text{all-rail }X_R .
\tag{13}
\]
The CZ layer has two P-gated and two identity diamonds. The record layer has four R-gated diamonds. Hadamard mixing uses signed bonds of weight \(k/\sqrt2\) in each two-rail mixer; the permutation uses ordinary bonds of weight \(k\). All four rails, including unused \(a_{\rm path}=0\) inputs, have identical scalar coefficients and terminations.

The first four layers give \(-C_P^{(b)}\), and the last gives \(-X_R\). Hence
\[
 G_{\rm out}=+X_R C_P^{(b)}.
\tag{14}
\]
It acts after the local SWAP in the comparator, giving (2) with a positive suffix sign. The earlier 26-layer SWAP network is absent from this device.

There are fourteen suffix slices, at virtual positions \(L-14,\ldots,L-1\):

| Module | Virtual positions |
|---|---|
| First Hadamard | \(L-14,L-13\) |
| CZ diamond \((L_d,B,C,R_d)\) | \(L-12,L-11,L-10,L-9\) |
| Second Hadamard | \(L-8,L-7\) |
| Permutation | \(L-6,L-5\) |
| Record diamond \((L_d,B,C,R_d)\) | \(L-4,L-3,L-2,L-1\) |

Positions \(0,\ldots,L-15\) are ordinary input heads, and \(L\) is one external output head per rail. For each scalar link choose
\[
 k_r=\alpha\sqrt{r(L+1-r)},\qquad 1\leq r\leq L,
 \qquad k_r\leq J_c.
\tag{15}
\]
The diamond outer weights are the corresponding \(k/\sqrt2\), its middle contact is the corresponding \(k\), and each mixer/cable/permutation uses its corresponding link weight. Repeat the assignment across rails.

Add one occupation potential on every physical head to make its transformed diagonal \(C_{\rm head}\):

| Physical head | Added occupation coefficient |
|---|---|
| Diamond terminal | \(C_{\rm head}-(2a_{\rm end}+k_{\rm cable})\) |
| Both arms of a diamond | \(C_{\rm head}-(a_L+a_R+g_d)\) |
| Hadamard port | \(C_{\rm head}-(\sqrt2k_H+k_{\rm cable})\) |
| Permutation port | \(C_{\rm head}-(k_{\rm link}+k_{\rm cable})\) |
| Ordinary head/endpoints | \(C_{\rm head}-(k_{\rm left}+k_{\rm right})\) |

Missing endpoint bonds are zero. Every subtraction is at most \((\sqrt2+1)J_c\), or \(2J_c\) for ordinary heads, so all compensations are strictly positive. Identity-diamond occupations remain separate. No uniform-matching \(\mu\) repair is added.

The resulting head Hamiltonian \(H_{\rm head}\) consists of actual positive one-/two-body blocks, conserves head number and annihilates the head vacuum. The local apparatus need not annihilate that vacuum. The actual device is
\[
 H_{\rm tot}=H_{\rm head}+H_{\rm loc}.
\tag{16}
\]
Every installed term also commutes with \(H_E\), since head contacts act on P only through \(Z_P\) and R is freely degenerate.

## 3. Full many-body cubic gap and the local inverse range

Let \(\Pi\) be the fully symmetric reference projector, with identities on data and passive references, and \(\Pi_\perp=I-\Pi\). Positivity and connected edge transpositions imply
\[
 \ker H_F=\operatorname{ran}\Pi,\qquad H_F\Pi=\Pi H_F=0.
\]
The graph Hamiltonian need not be invariant under all permutations away from this kernel.

For completeness, the new full-space gap follows by elementary comparison. An endpoint transposition along a simple path of d edges is an adjacent-swap palindrome of length \(2d-1\), using each edge at most twice. Prefix telescoping,
\[
 U_1\cdots U_l-I
 =\sum_{r=1}^lU_1\cdots U_{r-1}(U_r-I),
\]
and \(\|(I-S)\psi\|^2=2\langle\psi,(I-S)\psi\rangle\) give
\[
 \langle I-S_{uv}\rangle_\psi
 \leq(4d-2)\sum_{\text{path}}\langle I-S_e\rangle_\psi.
\tag{17}
\]
Choose axis-ordered x/y/z paths for every ordered pair. Their lengths are at most \(3(n-1)\), so \(4d-2<12n\). An edge across \(k|k+1\) occurs in exactly
\[
 2n^2(k+1)(n-k-1)\leq n^4/2
\]
ordered paths: the straddling coordinate supplies the first factor and the other two free endpoint coordinates supply \(n^2\). This is valid for each axis with the appropriate fixed source/target coordinates. Taking half the ordered endpoint-energy sum yields
\[
 \sum_{u<v}(I-S_{uv})
 \leq3n^5\sum_{uv\in E}(I-S_{uv}).
\tag{18}
\]
On the complete N-qubit space,
\[
 \sum_{u<v}(I-S_{uv})
 =\frac{N(N+2)}4I-\mathbf S_{\rm total}^2
 \geq N\Pi_\perp.
\]
The last inequality follows because the spin-\(N/2\) symmetric sector has zero energy and the next spin label lowers \(S(S+1)\) by N. Thus
\[
 H_F\geq\Delta\Pi_\perp,\qquad
 \Delta=\frac{\kappa}{3n^2}.
\tag{19}
\]
This includes every reference excitation sector; no one-magnon lifting theorem is assumed.

The sharper estimate concerns the inverse acting on the actual local exchange. Let \(\mathcal L\) be the open-grid combinatorial Laplacian, \(d_e=\mathbf e_e-N^{-1}\mathbf1\), and
\[
 \varphi=\mathcal L^+d_e,\qquad \sum_v\varphi_v=0.
\]
The open path eigenpairs are
\[
 \ell_r=2-2\cos(\pi r/n),\quad
 u_0(j)=n^{-1/2},\quad
 u_r(j)=\sqrt{2/n}\cos[\pi r(j+1/2)/n]\ (r\geq1).
\]
They obey the degree-one endpoint equations and cosine orthogonality; tensor products give the cubic-grid eigenbasis. Since
\(\ell_r\geq4r^2/n^2\) and \(|u_r(j)|^2\leq2/n\),
\[
 \begin{aligned}
 \|\varphi\|_2^2
 &\leq\frac n2
    \sum_{\boldsymbol r\ne0}
      \frac1{(r_1^2+r_2^2+r_3^2)^2}\\
 &\leq\frac n2\sum_{m=1}^{n-1}
       \frac{3m^2+3m+1}{m^4}
 \leq\frac{7n}{2}\sum_{m=1}^{n-1}m^{-2}
 \leq7n.
 \end{aligned}
\tag{20}
\]
The shell \(\max r_i=m\) has exactly \(3m^2+3m+1\) nonnegative triples. The last sum is at most two. The constant mode is removed before inversion; this is a finite-grid estimate.

For any zero-sum vector f, define
\[
 B_\pm(f)=\sum_v f_v\sigma_v^\pm\Pi.
\]
Permutation invariance of \(\Pi\) gives \(\Pi B_\pm(f)=0\). Direct edge expansion gives the exact intertwining
\[
 (I-S_{ij})B_\pm(f)
 =(f_i-f_j)(\sigma_i^\pm-\sigma_j^\pm)\Pi,\qquad
 H_FB_\pm(f)=\kappa B_\pm(\mathcal Lf).
\tag{21}
\]
For the normalized symmetric Dicke vector \(D_r\) with r excitations, the lowering Gram entries are \(r/N\) on the diagonal and \(r(N-r)/(N(N-1))\) off the diagonal. The zero-sum condition therefore gives
\[
 \|B_-(f)D_r\|^2
 =\frac{r(r-1)}{N(N-1)}\|f\|_2^2.
\tag{22}
\]
Raising replaces r by \(N-r\). Both coefficients are at most one. Distinct r map to distinct final excitation sectors for each fixed sign, so
\[
 \|B_\pm(f)\|\leq\|f\|_2
\tag{23}
\]
on the entire symmetric subspace, including coherent Dicke-sector superpositions entangled with data or passive references.

Restrict \(A=\Pi_\perp H_F\Pi_\perp\) to its invertible complementary space and set \(C=\Pi_\perp W\Pi\). H_S contributes nothing to C. Equations (21)–(23) imply
\[
 \begin{aligned}
 C&=g[\sigma_P^+B_-(d_e)+\sigma_P^-B_+(d_e)],\\
 A^{-1}C
 &=\frac g\kappa
       [\sigma_P^+B_-(\varphi)+\sigma_P^-B_+(\varphi)],\\
 \|A^{-1}C\|&\leq\frac{g\sqrt{7n}}{\kappa}.
 \end{aligned}
\tag{24}
\]
The two exchange directions have orthogonal final P labels, so their squared output norms add; no extra \(\sqrt2\) factor is needed. This identity identifies a particular inverse range. It does not claim that the whole reference complement is a one-particle space.

## 4. Complete local evolution and the comparison SWAP

Let \(W_\perp=\Pi_\perp W\Pi_\perp\) and \(D=A+W_\perp\) on the complementary space. From \(\|W\|<4\lambda\) and \(\lambda\leq\Delta/8\),
\[
 D^{-1}C=(I+A^{-1}W_\perp)^{-1}A^{-1}C,\qquad
 \eta:=\|D^{-1}C\|\leq\frac{2g\sqrt{7n}}{\kappa}.
\tag{25}
\]
The Neumann factor has norm at most two. Its order matters: A and \(W_\perp\) need not commute. The global gap is used to establish this inverse; the improved numerator in (24) is retained.

For evolution from a unit vector \(\xi\in\Pi\), decompose
\(\psi(t)=e^{-it(H_F+W)}\xi=p(t)+q(t)\) into \(\Pi,\Pi_\perp\). The exact block equations give
\[
 ip'=\Pi W\Pi p+C^*q,\quad iq'=Cp+Dq,\quad
 q(0)=0,\qquad\|p'\|\leq v:=4\lambda.
\]
One integration by parts in
\(q(t)=-i\int_0^t e^{-iD(t-u)}Cp(u)\,du\)
uses the endpoint operators \(D^{-1}C\), rather than a scalar replacement for them. Hence
\[
 \begin{aligned}
 \|q(t)\|&\leq\eta(2+vt),\\
 \|p(t)-e^{-it\Pi W\Pi}\xi\|
 &\leq g\eta(2t+vt^2/2).
 \end{aligned}
\]
Write \(E_{\rm elim}(t)=\|e^{-it(H_F+W)}\Pi-e^{-it\Pi W\Pi}\Pi\|\), interpreting the second exponential on \(\operatorname{ran}\Pi\). Adding the two output errors proves the complete induced bound
\[
 E_{\rm elim}(t)\leq
 \eta[(2+vt)+g(2t+vt^2/2)]
 <2048\,\frac{\lambda\sqrt n}{\kappa},
 \qquad0\leq t\leq2\pi/\lambda.
\tag{26}
\]
Indeed the bracket is at most
\(2+8\pi+\sqrt2(4\pi+8\pi^2)<250\), and
\(\eta<8\lambda\sqrt n/\kappa\). No extensive \(\|H_F\|\) enters \(\|p'\|\), and the actual complementary output is paid in full.

Permutation symmetry gives
\[
 \Pi W\Pi=\Pi(H_S+V_{\rm star})\Pi,\qquad
 V_{\rm star}=\frac gN\sum_v
       (\sigma_P^+\sigma_v^-+\sigma_P^-\sigma_v^+).
\tag{27}
\]
The star preserves \(\Pi\). On the supplied product reference,
\[
 (V_{\rm star}-(g/2)X_P)(\psi\otimes\beta)
 =\frac g{2N}Y_P\psi\otimes\sum_vY_v\beta,\qquad
 \|(V_{\rm star}-(g/2)X_P)E_\beta\|
 =\frac g{2\sqrt N}.
\tag{28}
\]
The single-site deviations \(Y_v\beta\) are orthonormal. This residual holds along the whole comparison trajectory, including arbitrary data correlations, and gives full star error \(gt/(2\sqrt N)\).

Since \(g/2=a_d\), the comparison data operator is
\[
 H_{\rm eff}=a_d(X_Q+X_P)+b_d(Z_Q+Z_P)+c_dZ_QZ_P.
\]
Its singlet energy is \(-3\lambda/4\). On the triplet,
\((H_{\rm eff}+c_dI)/\lambda\) has diagonal
\((3+\sqrt5)/2,0,(3-\sqrt5)/2\), adjacent entries one, and characteristic polynomial
\((x-3)(x-1)(x+1)\). Consequently
\[
 \|H_{\rm eff}\|=9\lambda/4,\qquad
 e^{-i\tau H_{\rm eff}}
 =e^{-i\pi/4}\operatorname{SWAP}_{QP}.
\tag{29}
\]
The singlet's relative sign is included.

Restoring the actual commuting free/scalar factors gives the ordered comparator
\[
 e^{-ist}[e^{-it\omega n_P}e^{-itH_{\rm eff}}\psi]
       \otimes\beta(t).
\tag{30}
\]
The free P factor and \(H_{\rm eff}\) need not commute. At \(\tau=2\pi m/\omega\), the entire integer-gap free evolution revives. For nearby t, replacing (30) by
\(e^{-i(st+\pi/4)}\operatorname{SWAP}\psi\otimes\beta(t)\)
costs at most \((\omega+9\lambda/4)|t-\tau|\). Thus
\[
 E_{\rm loc}(t)
 <2048\frac{\lambda\sqrt n}{\kappa}
  +\frac{gt}{2\sqrt N}
  +(\omega+9\lambda/4)|t-\tau|.
\tag{31}
\]
The reference comparator retains \(\beta(t)\) across the window. No separate \(\kappa|E|t\) phase is added: the positive ferromagnetic operator stays intact and has zero energy on \(\Pi\).

## 5. Paying the overlap with a continuously acting local SWAP

Let \(\mathcal A\) be the physical head-arm rotation and \(G=\bigoplus_xG_x\) the ordered data/rail prefixes. The structured head construction gives, exactly on its preserved one-head sector,
\[
 (\mathcal A G)^*H_{\rm head}(\mathcal A G)=h_L\otimes I,\qquad
 h_L=C_{\rm head}I-\sum_{r=1}^L
 k_r(|r\rangle\langle r-1|+\mathrm{h.c.}).
\tag{32}
\]
The prefixes, including the diamond arm coordinates, are as follows. Here \(H=H_b\), \(D_b=\operatorname{CZ}_{b,P}\), and \(X=X_b\).

| Coordinate | \(G_x\) |
|---|---|
| \(x\leq L-14\) | \(I\) |
| \(L-13,L-12,L-11\) | \(H\) |
| \(L-10,L-9,L-8\) | \(-D_bH\) |
| \(L-7,L-6\) | \(-HD_bH\) |
| \(L-5,L-4,L-3\) | \(-XHD_bH\) |
| \(L-2,L-1,L\) | \(X_RXHD_bH\) |

The first potentially noncommuting prefix is at the first CZ diamond's C coordinate \(L-10\). Every prefix acts trivially on reference qubits and diagonally on P. Thus it commutes with \(H_E,H_F,sI\), while \(\mathcal A\) commutes with the entire local apparatus. Conjugating the *actual* installed sum gives
\[
 \widetilde H
 =h_L+H_{\rm loc}+\mathcal D,\qquad
 \mathcal D=\sum_x|x\rangle\langle x|\otimes
             (G_x^*WG_x-W).
\tag{33}
\]
The defect vanishes for \(x<L-10\), and its fiber norm is \(<8\lambda\). These are analytical differences after a unitary change of representation, not extra installed many-body blocks. The grid introduces no term proportional to \(\|H_F\|\) into (33).

The benchmark \(h_L+H_{\rm loc}\) contains the actual running local apparatus. It factorizes only in the scalar clock coordinate and has the exact profile
\[
 f_x(t)=e^{-iC_{\rm head}t}\sqrt{\binom Lx}\,
        [i\sin(\alpha t)]^x[\cos(\alpha t)]^{L-x}.
\tag{34}
\]
One derivation identifies \(|x\rangle\) with the normalized symmetric weight-x vector of L mathematical spins, where \(h_L-C_{\rm head}I=-\alpha\sum_jX_j\). These mathematical spins add no physical resources. This is the known engineered-chain transfer mechanism attributed in the gate parent, used with its actual negative-hopping convention. The amplitude retains the sign of the cosine after the revival.

Because \(L\geq16\), the input at zero has identity arm/prefix gauge. Duhamel on the benchmark trajectory gives the complete induced estimate
\[
 E_{\rm join}(t)
 \leq8\lambda\int_0^t\sqrt{p_{\rm tail}(v)}\,dv,\qquad
 p_{\rm tail}(v)=\sum_{x=L-10}^L|f_x(v)|^2.
\tag{35}
\]
Actual joint dynamics need not factorize, and the logical input may be correlated. The local benchmark evolution has norm one on the entire data/reference fiber.

For \(0\leq v\leq\tau\), put \(\theta=\alpha v\) and
\(Y=L-X\), where \(X\) has binomial law
\(\operatorname{Bin}(L,\sin^2\theta)\). Applying Markov's inequality to \(e^{-Y}\),
\[
 p_{\rm tail}=\Pr(Y\leq10)
 \leq e^{10}[1-(1-e^{-1})\cos^2\theta]^L
 \leq e^{10-L\cos^2\theta/2}.
\]
Taking the square root, using
\(\cos\theta\geq2(\pi/2-\theta)/\pi\), and extending the positive Gaussian integral gives
\[
 \int_0^\tau\sqrt{p_{\rm tail}(v)}\,dv
 \leq\frac{\pi\sqrt\pi\,e^5}{\lambda\sqrt L}.
\tag{36}
\]
Thus the prearrival contribution to (35) is \(<8192/\sqrt L\). For any \(t\leq\tau+w\), the additional interval after \(\tau\) costs at most \(8\lambda w\), since \(p_{\rm tail}\leq1\). This yields, on the full required horizon,
\[
 E_{\rm join}(t)\leq8192/\sqrt L+8\lambda w
 \leq\epsilon/64.
\tag{37}
\]
All time from preparation is included. No head amplitude is declared exactly absent before the suffix, and no interaction is switched off at \(\tau\).

At \(\tau\), (34) equals \(e^{-iC_{\rm head}\tau}i^L|L\rangle\). Since
\(\|h_L-C_{\rm head}I\|=\alpha L=\lambda L/2\), the complete scalar-head replacement obeys
\[
 \left\|f(t)-e^{-iC_{\rm head}t}i^L|L\rangle\right\|
 \leq(\lambda L/2)|t-\tau|\leq\epsilon/128.
\tag{38}
\]
This charges all nonendpoint benchmark heads.

The policy (4) closes the separate allowances:

| Contribution on \([\tau-w,\tau+w]\) | Bound |
|---|---|
| Complete local elimination | \(<2048\lambda\sqrt n/\kappa\leq\epsilon/128\) |
| Product-reference star residual | \(gt/(2\sqrt N)<\epsilon/64\) |
| Local free/gate timing | \(\leq\epsilon/128\) |
| Actual suffix overlap (37) | \(\leq\epsilon/64\) |
| Complete head endpoint replacement (38) | \(\leq\epsilon/128\) |

The first three sum to \(<\epsilon/32\). Restoring \(\mathcal A\) and \(G\) preserves the errors; at the external endpoint \(\mathcal A\) is identity and \(G_L=+X_RC_P^{(b)}\). The sum of the five allowances is \(<7\epsilon/128\), proving (7) with exactly the phase in (6). The local, clock and free revivals are synchronized by the single static relation \(\alpha=\lambda/2,\ \lambda=\omega/(2m)\).

## 6. Physical counts, incident cap and bounded-range placement

The fourteen suffix slices contain 56 heads. Before head compensations, the CZ diamonds contribute 22 blocks, the record diamonds 24, the two Hadamard layers 16, the permutation four, and the interlayer cables 16: a total of 82. Adding 56 head occupations gives 138 suffix blocks. Outside it are \(4L-52\) ordinary heads, the same number of ordinary bonds and the same number of positive head occupations. Therefore
\[
 \begin{aligned}
 {\rm head\ qubits}&=4(L+1),&
 {\rm head\ blocks}&=8L+34,\\
 {\rm total\ qubits}&=4L+N+7,&
 {\rm total\ blocks}&=8L+N+40+3n^2(n-1).
 \end{aligned}
\tag{39}
\]
The local inventory is \(N+1\) free occupations, five data/exchange blocks and \(3n^2(n-1)\) grid bonds. Q/P/R are shared actual qubits. The two possible input b endpoints encode one head, not two simultaneous excitations.

All load accounting uses full-support positive-block norms. The compensated head load is at most \((5+\sqrt2)J_c\); there are four P contacts of norm at most \(2J_c\) and eight R contacts of that ceiling. With (4),
\[
 \begin{aligned}
 {\rm load}(P)&\leq\omega+C_P\lambda+8J_c
                 \leq\omega+M/4+M/8,\\
 {\rm load}(Q)&<M/4,&
 {\rm load}(R)&\leq16J_c\leq M/4,\\
 {\rm load}(\text{head})&\leq(5+\sqrt2)M/64,\\
 {\rm load}(B_v),\ v\ne e
 &\leq\omega+12\kappa=\omega+3M/8,\\
 {\rm load}(B_e)&\leq\omega+6\kappa+2g
       <\omega+3M/16+M/4.
 \end{aligned}
\tag{40}
\]
Every bound is below \(\Lambda\). The corner has three grid neighbors; its exchange bound follows from
\(2g\leq\sqrt2 M/(2C_P)<M/4\).
Projection to the symmetric or one-head space does not reduce any physical load.

One explicit cubic-lattice placement is
\[
 P=(0,0,0),\quad R=(1,0,0),\quad Q=(0,0,-1),\quad
 B_{i,j,k}=(-1-i,-j,-k).
\tag{41}
\]
Place the suffix in \(\{0,1,2,3\}^3\), with four left ports \((i,3,3)\) and four right ports \((i,2,3)\), \(i=0,\ldots,3\). After removing P, R and those eight ports, 54 cube sites remain for the other 48 suffix heads. Attach \(L-14\) ordinary input heads above each left port and one output head at \(z=4\) above each right port. The eight vertical rays have distinct horizontal coordinates and do not intersect the negative-x reference cube or Q.

Reference bonds, the corner-P bond and QP are nearest-neighbor. Suffix bonds have Manhattan range at most nine. Maximum installed graph degree is eight at R; P has four head contacts, Q and the reference corner; grid degree is at most six and the attached corner degree four. The complete loader is bounded-range, while its reference subsystem is nearest-neighbor. Selective absence of unlisted couplings is supplied.

## 7. Optional checked policy with a smaller head constant

The original policy (4) remains a valid separate choice. A further checked estimate permits replacing only its head-length definition by
\[
 L_{\rm sharp}=\left\lceil\max\{16,(8192/\epsilon)^2\}\right\rceil.
\tag{42}
\]
Every dependent quantity in (4)–(6), including \(\lambda_{\max},m,\lambda,\tau,J_c,C_{\rm head},w\) and \(i^L\), must then be recomputed using this new actual integer L. The local resolvent, reference-size and cap restrictions remain imposed.

Here is the changed proof. The full prefix table in section 5 acts trivially on Q and is diagonal on P. Each prefix therefore commutes separately with \(X_Q,Z_Q,Z_P,Z_QZ_P\), and hence with \(H_S\). This includes both virtual arm coordinates of both diamonds. The defect in (33) is consequently exactly
\[
 \mathcal D_x=G_x^*V_{\rm loc}G_x-V_{\rm loc},\qquad
 \mathcal D_x=0\ (x<L-10),\qquad \|\mathcal D_x\|\leq2g.
\tag{43}
\]
This is a full-fiber bound: it assumes no actual symmetric-sector restriction or product-state factorization. It replaces the coefficient \(8\lambda\) in (35) by \(2g=2\sqrt2\lambda\).

For the same binomial variable Y, choose exponential Markov parameter \(z=1/11\). Since \(1-e^{-1/11}\geq1/12\),
\[
 \sqrt{\Pr(Y\leq10)}
 \leq e^{5/11}\exp[-L\cos^2(\alpha v)/24].
\]
The cosine chord bound and \(y=\pi/2-\alpha v\) give
\[
 \int_0^\tau\sqrt{p_{\rm tail}(v)}\,dv
 \leq\frac{e^{5/11}\pi\sqrt{6\pi}}{\lambda\sqrt L}.
\tag{44}
\]
Multiplication by \(2g\) gives the coefficient
\[
 2\sqrt2\,e^{5/11}\pi\sqrt{6\pi}<440/7<64.
\tag{45}
\]
An elementary certificate uses \(\sqrt2<10/7\), \(\pi<22/7\),
\(\sqrt{6\pi}<35/8\), and \(e^{5/11}<8/5\). The last inequality follows from
\(\log(8/5)\geq2[(8/5)-1]/[(8/5)+1]=6/13>5/11\);
\(\log x-2(x-1)/(x+1)\) has nonnegative derivative for \(x\geq1\).

As before, only the trivial tail bound is used after \(\tau\). Thus
\[
 E_{\rm join}(t)
 <64/\sqrt L+2\sqrt2\lambda w
 \leq\epsilon/128+\sqrt2\epsilon/512
 <\epsilon/64
\tag{46}
\]
for all \(0\leq t\leq\tau+w\), with L from (42). Equations (26), (31), (38) and all cap constraints are unchanged, so (7)–(8) hold for the new complete target and new apparatus.

The real-valued head-length floor changes from \(2^{40}\epsilon^{-2}\) to \(2^{26}\epsilon^{-2}\), a factor 16384. Ceilings, additive core/reference resources and the other entries of \(\lambda_{\max}\) prevent assigning that exact reduction to every physical count or runtime. Both policies still have large constants, supplied exact coefficient correlations, and the same eventual exponents. This refinement introduces no stopping mechanism or exact rare-event record theorem.

## 8. Standalone specialization and sufficient resource orders

For the standalone local SWAP, omit the head device and R, and choose the smaller reference size and its own policy:
\[
 \begin{aligned}
 n_{\rm st}&=\left\lceil(512\pi^2/\epsilon^2)^{1/3}\right\rceil,
 &N_{\rm st}&=n_{\rm st}^3,\\
 \kappa&=M/32,&
 \Delta_{\rm st}&=\kappa/(3n_{\rm st}^2),\\
 \lambda_{\max}^{\rm st}
 &=\min\left\{\omega/2,M/(2C_P),\Delta_{\rm st}/8,
       \epsilon\kappa/(65536\sqrt{n_{\rm st}})\right\},\\
 m&=\left\lceil\omega/(2\lambda_{\max}^{\rm st})\right\rceil,
 &\lambda&=\omega/(2m),\qquad\tau=\pi/\lambda,\\
 w_{\rm st}&=\epsilon/[32(\omega+9\lambda/4)].
 \end{aligned}
\tag{47}
\]
These are a separate apparatus and parameter choice. On its closed window, the normalized complete comparator
\[
 \mathcal B_t\psi=e^{-i(st+\pi/4)}
       \operatorname{SWAP}_{QP}\psi\otimes\beta(t)
\]
has vector error \(<\epsilon/8\), channel error \(<\epsilon/4\), and center vector error \(<\epsilon/16\). Equation (26) pays \(\epsilon/32\), the star residual pays \(<\epsilon/16\), and local timing pays \(\epsilon/32\).

This standalone apparatus has \(N_{\rm st}+2\) qubits and
\(N_{\rm st}+6+3n_{\rm st}^2(n_{\rm st}-1)\) blocks. The geometry (41) without the suffix/R is wholly nearest-neighbor, with maximum degree at most six. Its P and Q loads are bounded by \(\omega+M/2\) and \(M/2\), its unattached reference loads by \(\omega+3M/8\), and its corner by \(<\omega+11M/16\). No local-load argument imports the stronger full-loader allocation by assumption.

For fixed positive \(\omega,M\), both reference prescriptions have
\[
 n=\Theta(\epsilon^{-2/3}),\qquad
 N=\Theta(\epsilon^{-2}),\qquad
 \Delta=\Theta(M\epsilon^{4/3}).
\tag{48}
\]
In (47), both nonconstant restrictions \(\Delta/8\) and
\(\epsilon\kappa/(65536\sqrt n)\) have order \(M\epsilon^{4/3}\). In the full-loader policy, the analogous two restrictions have that same order, while the clock cap
\[
 4J_{\rm budget}/(L+1)=\Theta(M\epsilon^2)
\]
eventually becomes smaller. Revival rounding preserves these orders because
\(\lambda_{\max}/2<\lambda\leq\lambda_{\max}\).

| Explicit family | Qubit/block order | Sufficient time order |
|---|---|---|
| Standalone cubic SWAP, (47) | \(\Theta(\epsilon^{-2})\) | \(\Theta(M^{-1}\epsilon^{-4/3})\) |
| Full loader, original (4) | \(\Theta(\epsilon^{-2})\) | \(\Theta(M^{-1}\epsilon^{-2})\) |
| Full loader, optional (42) | \(\Theta(\epsilon^{-2})\) | \(\Theta(M^{-1}\epsilon^{-2})\) |

The standalone half-width is \(\Theta(\epsilon/\omega)\), with relative half-width \(\Theta((M/\omega)\epsilon^{7/3})\). For either full-loader family, the three width entries have respective orders \(\epsilon/\omega\), \(M^{-1}\epsilon^{-1}\), and \(M^{-1}\epsilon\). Thus \(w=\Theta(\epsilon)\) and \(w/\tau=\Theta(\epsilon^3)\) at fixed \(\omega,M\). The exact minima govern finite accuracy; asymptotic dominance is not a claim of a favorable finite crossover or dwell fraction.

The earlier checked gap-only cubic calculation remains valid. It uses
\(E_{\rm elim}<512\lambda/\Delta\), with accuracy restrictions
\(\lambda\leq\epsilon\Delta/16384\) standalone or
\(\lambda\leq\epsilon\Delta/65536\) for the suffix, giving sufficient time order \(\epsilon^{-7/3}\). The improvement here retains the same global gap and uses (24) on the actual exchange range. The frozen earlier policy is preserved in its source; it is not silently relabelled as the new one.

## 9. Exact energy accounting and remaining physical supplies

Every listed physical block commutes with
\(H_E=\omega(n_P+K_B)\), where \(K_B=\sum_vn_{B_v}\).
This holds on the full physical Hilbert space, beyond the one-head or symmetric-reference sectors. Therefore the entire actual \(H_E\) distribution and all its moments are conserved. This statement concerns the installed equal-gap free energy \(H_E\); it does not identify it with \(H_{\rm tot}\) or an arbitrary active-environment Hamiltonian.

Let
\[
 p=\langle n_P\rangle_{\rm in},\qquad
 q=\langle n_Q\rangle_{\rm in}.
\]
The initial \(K_B\) is binomial \(\operatorname{Bin}(N,1/2)\), independent of the whole data/passive-reference input. Since \(n_P^2=n_P\), the actual values at every time are
\[
 \begin{aligned}
 \langle H_E\rangle_{\rm act}
 &=\omega(N/2+p),\\
 \operatorname{Var}_{\rm act}(H_E)
 &=\omega^2[N/4+p(1-p)],\\
 \langle H_E^2\rangle_{\rm act}
 &=\omega^2[N^2/4+N/4+(N+1)p].
 \end{aligned}
\tag{49}
\]
Initial Q/P/path coherences and correlations do not alter these formulas. Subsequent actual reference/data correlations need not vanish.

The target (6) has
\(U_f^*n_PU_f=n_Q\), because the suffix is diagonal on P and the SWAP exchanges Q and P. Its independent reference factor \(\beta(t)\) has the same binomial charge distribution as \(\beta\). Therefore its three moments are exactly (49) with p replaced by q:
\[
 \begin{aligned}
 \langle H_E\rangle_{\rm act}-\langle H_E\rangle_{\rm tar}
 &=\omega(p-q),\\
 \langle H_E^2\rangle_{\rm act}-\langle H_E^2\rangle_{\rm tar}
 &=\omega^2(N+1)(p-q),\\
 \operatorname{Var}_{\rm act}(H_E)
 -\operatorname{Var}_{\rm tar}(H_E)
 &=\omega^2[p(1-p)-q(1-q)].
 \end{aligned}
\tag{50}
\]
For example, input \(Q=1,P=0\) makes the target mean larger than the conserved actual mean by \(\omega\), at every N. A vanishing complete-vector error in the growing family does not imply vanishing energy-moment error: \(\|H_E\|=\omega(N+1)\) grows with the apparatus. Retaining every energetic output in the norm comparison is not an exact reference-energy-return statement.

More explicitly, if actual and normalized comparison vectors differ by at most \(\delta\), the bounded observable \(n_P\) obeys
\(|\langle n_P\rangle_{\rm act}-q|\leq2\delta\).
Conservation of the mean then gives
\[
 \omega\langle K_B\rangle_{\rm act}
 =\omega(N/2+p-q)+e,\qquad |e|\leq2\omega\delta.
\tag{51}
\]
This estimate uses a norm-one data observable, not continuity of an extensive energy operator. Exact reference return to \(\beta(t)\) is **not guaranteed**. If \(p\ne q\) and \(\delta<|p-q|/2\), (51) excludes equality with that reference by its mean. Equality is not universally excluded: at time zero the actual supplied reference is exactly \(\beta\), and no such exclusion is asserted for every input or time. This is the controlling qualification to the frozen energy-accounting source's overly universal sentence.

The maintained suppliers are the coherent reference product, physical coherent head input, blank R and other heads, equal gaps, freely degenerate Q/R/passive references, exact structured coefficients and compensations, selective installed real positive blocks, and isolation from undeclared interactions. \(H_F\beta=0\) does not prepare \(\beta\); its ground subspace is highly degenerate. No cooling, thermal-state certificate, native material Hamiltonian or fabrication-tolerance theorem follows. The inverse and prefix transformations are proof tools, not additional physical interactions.

The nonzero defect \(\mathcal D\) prevents importing the old exact all-time current-record factorization. Equation (7) is a finite-window statement with a high-probability joint external/record event; it is not exact normalized correctness for arbitrary early or rare \(R=1\) events. The Hamiltonian continues to act after the window and may undo the operation. The construction proves no physical switch-off, stable capture, reset, repeated reference reuse or permanent halt. It also makes no optimality or literature-novelty claim. A different aged-target or no-revival operation is not included.

## 10. Source map, review status and exposure

The canonical destination is
`docs/ACTIVE_ENERGY_CUBIC_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md`.
The evidence root is
`outputs/active_energy_cubic_loader_2026_10_18/source_checks/`.
Links below point to the packaged frozen evidence; each maps to the unchanged original file under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.
ROOT integration preserves the frozen author manuscript and source texts separately; mechanical packaging evidence is recorded in the packet.

| Frozen original and proposed packet link | Bytes | SHA256 |
|---|---:|---|
| [Active suffix proposal](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_loader_interface/PROPOSAL.md) | 21721 | `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570` |
| [Active suffix review](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_loader_interface_check/REVIEW.md) | 15996 | `ebf747aa6327d0c240054d21eacf14c6b28aeae2fa9967d55101b9c25ce599a6` |
| [Cubic gap and original policies](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_gap_swap/PROPOSAL.md) | 9999 | `72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee` |
| [Cubic gap review](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_gap_swap_check/REVIEW.md) | 17902 | `507e83cce4949b58c8dbc0ba84339ba9af05e55fa02a11ab2da1a223c62997d7` |
| [Exchange-range resolvent proposal](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_resolvent/PROPOSAL.md) | 20825 | `7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895` |
| [Resolvent review](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/cubic_reference_resolvent_check/REVIEW.md) | 15646 | `25f290e96014dd8622575c207fd66f125ae2160727ca7d0b7a7bf35b7c3de3b5` |
| [Optional smaller-head policy](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_suffix_prefactor/PROPOSAL.md) | 16060 | `793e9706b867f415647f2f6b7370f8e0daba0bf5efb993be3373c5337e52d0d0` |
| [Smaller-head review](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_suffix_prefactor_check/REVIEW.md) | 13925 | `aa56fd71a965ef3a81e1f05a73d6a58706d4439d797952e31fba92c98eddc347` |
| [Energy-accounting original](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_moment_accounting/PROPOSAL.md) | 3191 | `4bd84f3b86e74792724649bf355152d9eeb58f45d595a5f25b513c9b7fb86627` |
| [Controlling energy-accounting review](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_moment_accounting_check/REVIEW.md) | 7914 | `d3e54559249cf619a9252e748f4f3c4cbcc0f7c5081e13870c4e2ba5674b8d5a` |

The first four pairs have SUPPORT at their stated conditional mathematical scopes. The energy review supports all displayed identities and requires the reference-return wording qualification implemented in section 9; the original source is preserved as written. Historical pending flags in the grid, resolvent and smaller-head texts are superseded only by these actual later reviews and ROOT's source acceptance. They are not evidence of an unresolved mathematical dependency in this assembled draft, and the frozen files are not rewritten to conceal their chronology.

The direct mathematical parents remain in their existing packets:

| Canonical parent | Exact canonical bytes/SHA256 | Imported scope |
|---|---|---|
| [Local-reference static SWAP](LOCAL_REFERENCE_STATIC_SWAP_BOUNDED_THEOREM_NOTE_2026-10-18.md), PR9739 | 20939; `f072a5d6a885cb987fce5bc11f7cb0c9fb24097e610802c20984d965dfaa180f` | Actual positive local blocks, full-reference projection/elimination framework, star residual, exact effective SWAP and ordered free/scalar phase. |
| [Exact engineered loader](EXACT_TWO_BODY_ENGINEERED_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md), PR9737 | 31454; `43558ea59ebee23bf539d27ba1818a06b914fff52bb87d251b959b4889f3b868` | Local diamond/mixer identities, structured positive compensation and exact engineered scalar propagator; primary transfer attribution. |

The local parent's unchanged operative source pair is
[9e68 local proposal](../outputs/local_reference_static_swap_2026_10_18/source_checks/local_reference_static_swap/PROPOSAL.md) /
[bc0e review](../outputs/local_reference_static_swap_2026_10_18/source_checks/local_reference_static_swap_check/REVIEW.md);
its [star proposal](../outputs/local_reference_static_swap_2026_10_18/source_checks/product_reference_static_swap/PROPOSAL.md) /
[star review](../outputs/local_reference_static_swap_2026_10_18/source_checks/product_reference_static_swap_check/REVIEW.md)
carry identities `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825` /
`69c07739988970d1671e2b5acd985ec48d935d74066afc456761301e086be195`.
The gate parent's [structured source](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_loader_structured_coefficients/PROPOSAL.md) /
[structured review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_loader_structured_coefficients_check/REVIEW.md)
are `515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2` /
`273da0a0d28269e6e40aff0695f5465456acd35abe4c0b4eddc1acf0578334c8`;
its source map retains the diamond, corrected matching and engineered-transfer premises. Those unchanged histories need not be duplicated into the new packet.

The load-bearing chain is: actual positive local/head interfaces; full cubic gap; exchange-range inverse and complete local comparison; exact late-supported suffix defect; its time-zero-to-window integral; synchronized complete target and cap. The optional head refinement changes the defect coefficient and tail inequality while preserving the remaining chain. Energy accounting clarifies the comparison's meaning and is not an additional operation premise.

ROOT supplied branch base PR9742, head
`45f3a59e13ae73edf18d238a0328fc66bc1f5191`, for later integration. That is genealogical metadata supplied to this drafting task, not a Git observation or a mathematical dependency. No conserved-reference lower bound, old degenerate-data runtime, uniform-ray dwell, aged-target variant, unproved coefficient tolerance or arbitrary \(H_{P\mathcal E}\) result is imported from branch ancestry.

The drafting worker completely read all ten new files above, the complete local-reference canonical note, and the required active/reference arguments. Its earlier complete read of the unchanged exact-loader note and original gate sources was reused after verifying the canonical identity; the relevant physical-block, compensation and scalar-clock passages were refreshed. The worker authored the cubic-gap review and has prior loader/rotation exposure. ROOT proposed several of the routes; the source authors and checkers share campaign ancestry, and some reviewers previously authored or checked inherited machinery. The reviews reconstruct changed arguments under that exposure. They are neither blind replication nor independent physical validation of the suppliers, and this manuscript's synthesis is not another independent check of its author's own grid review.

This authoring task used analytical reading/reconstruction and deterministic file/hash/link bookkeeping. It ran no scientific executable, spectral fit, simulation, sweep or new literature search. Only this research-directory NOTE.md was written; no canonical file, Git state, checkpoint, axiom, editable prompt, model/effort or publication/audit status was changed. Final integration review and actual packaging/publication actions belong to ROOT.

## Integration record

ROOT completely read the 742-line manuscript snapshot and the full final clarification diff, as well as every changed source and distinct review at the identities above. The canonical changes concern publication provenance only. The [energy-accounting disposition](../outputs/active_energy_cubic_loader_2026_10_18/source_checks/active_energy_moment_accounting/ROOT_DISPOSITION.md) preserves the controlling reference-return qualification. Source identities, inherited pins and packaging limits are recorded in the [source manifest](../outputs/active_energy_cubic_loader_2026_10_18/SOURCES.json) and [publication scope](../outputs/active_energy_cubic_loader_2026_10_18/PUBLICATION_CHECK.md). No retained status, science merge, physical axiom or editable-prompt change is claimed.
