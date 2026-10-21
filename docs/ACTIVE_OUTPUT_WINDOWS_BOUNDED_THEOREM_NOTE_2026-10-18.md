# Finite freely aged output windows for an active-energy loader

Claim type: bounded_theorem.
Primary runner: `scripts/product_reference_attachment_controls_2026_10_18.py`.

Publication evidence boundary: The complete arguments below and their supporting derivations remain the mathematical basis, with exactly their stated suppliers and hypotheses. Original review dispositions, author-time statuses and old hashes record history; they are not fresh execution evidence or authority. Current live source identities are listed in `outputs/product_reference_attachment_review_2026_10_18/INPUT_CLOSURE.json`. The shared primary supplies finite matrix and budget controls, not a simulation of the enormous apparatus or a proof of physical supply.

This note gives two observation contracts for a constant Hamiltonian built from supplied real positive one- and two-qubit blocks. A local cubic product reference supports an approximate ordinary Q/P SWAP while the literal energy \(\omega n_P\) remains installed. A diagonal-P head suffix completes the path operation and flips a blank record. Every head, data, energetic-reference and passive-reference output is retained.

Both contracts compare the logical output with \(e^{-it\omega n_P}U_f\), not with fixed \(U_f\). The first retains a single endpoint head and uses a state-specific endpoint displacement estimate. The second places the suffix before the clock's middle and retains a normalized moving profile on a macroscopic ordinary output ray. Their complete-vector allowances are each \(<7\epsilon/128\). The endpoint policy has eventual sufficient size/time orders \(\epsilon^{-2}\) and relative half-width \(\Theta(\epsilon^2)\). The moving-profile policy has orders \(\epsilon^{-2}\log(1/\epsilon)\) and exact one-sided relative width \(\epsilon/(1024\pi)\).

Both construction sources have scoped supporting distinct checks, now fully read and accepted by ROOT. The drafting worker has also completely read the output-ray report at its frozen identity recorded in section 8. Claim type: bounded_theorem, conditional on the explicit supplied apparatus and input. ROOT has completed integration reading; this synthesis is not an independent check of its author's output-ray proposal. Neither contract is permanent halt, fixed-output storage, native preparation or arbitrary active-environment transfer.

The mathematical parent is the [active-energy cubic-loader note](ACTIVE_ENERGY_CUBIC_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md), canonical SHA256 `8023deeb062288b75065576d89f726d528e077e7b10fac90333b33c61fbff110`. It supplies the literal local blocks, all-sector reference elimination, positive diamond/mixer identities, exact clock gauge and incident-load accounting. Its source map retains the local-reference and engineered-transfer ancestry and attribution. Its old fixed-output revival/window is not silently transferred to either new contract. No tolerance, weighted-reference or detuning result is imported from a later branch base.

## 1. Complete input and the changed logical contract

Let \(n_D=|1\rangle\langle1|_D\), \(\sigma_D^+=|1\rangle\langle0|_D\), and \(\sigma_D^-=(\sigma_D^+)^*\). The ordinary qubits Q,P,R are shared physical qubits. P and each energetic reference qubit have equal gap \(\omega>0\); Q,R and every passive input reference \(\mathcal E\) are freely degenerate. The supplied input has one head at scalar coordinate0, rail label \(a_{\rm path}=1\), arbitrary coherent joint state of path label b, Q,P and \(\mathcal E\), blank R and every other head vacant. The four rails \((a_{\rm path},b)\) are positions of one head, not four head excitations or additional data qubits. Independently supply \(\beta=|+\rangle^{\otimes N}\) on the energetic reference.

Define
\[
 C_P^{(b)}=|0\rangle\langle0|_P X_b+|1\rangle\langle1|_P I_b,
 \qquad U_f=I_{a_{\rm path}}X_R C_P^{(b)}\operatorname{SWAP}_{QP}.
\tag{1}
\]
Products act right to left. On basis inputs this maps
\((b,q,p,0_R)\) to \((b\oplus(1-q),p_Q,q_P,1_R)\). It retains arbitrary old-P/passive-reference correlations on Q.

The logical target in this note is
\[
 e^{-it\omega n_P}U_f.
\tag{2}
\]
It includes the center-time operator \(e^{-i\omega\tau n_P}\). It is generally neither fixed \(U_f\) nor merely post-transfer aging \(e^{-i(t-\tau)\omega n_P}U_f\). It also differs from old-P-before-transfer aging:
\[
 U_f e^{-it\omega n_P}=e^{-it\omega n_Q}U_f
 \ne e^{-it\omega n_P}U_f
\tag{3}
\]
in general. Equation (2) ages the original Q state transferred to P. Keeping the old P state on Q does not establish (3)'s alternative ordered contract, much less arbitrary \(H_{P\mathcal E}\) dynamics. No inverse-aging correction is installed or authorized by this comparison.

## 2. Actual local apparatus and common reference policy

Fix \(\Lambda>\omega>0\), \(M=\Lambda-\omega\) and \(0<\epsilon\leq1\). Both constructions use
\[
 \begin{gathered}
 C_P=(\sqrt5+3)/2+2\sqrt2,\qquad
 n=\left\lceil(8192\pi^2/\epsilon^2)^{1/3}\right\rceil,
 \quad N=n^3,\\
 \kappa=M/32,\qquad \Delta=\kappa/(3n^2),\qquad
 J_{\rm budget}=M/64.
 \end{gathered}
\tag{4}
\]
The reference graph is the open n-by-n-by-n grid, with P attached to a corner e. For the positive \(\lambda\) chosen separately below, put
\[
 a_d=\lambda/\sqrt2,\quad b_d=\sqrt5\lambda/4,\quad
 c_d=3\lambda/4,\quad g=\sqrt2\lambda,\quad
 s=a_d+2b_d+c_d+g.
\]
The actual positive local blocks are
\[
 \begin{gathered}
 a_d(I+X_Q),\quad b_d(I+Z_Q),\quad b_d(I+Z_P),\quad
 c_d(I+Z_QZ_P),\\
 g(I+\sigma_P^+\sigma_e^-+\sigma_P^-\sigma_e^+),\quad
 \kappa(I-\operatorname{SWAP}_{uv})\ (uv\text{ a grid edge}),\\
 \omega n_P,\qquad \omega n_{B_v}\quad(v\text{ a reference site}).
 \end{gathered}
\tag{5}
\]
Their sum is
\[
 \begin{aligned}
 H_E&=\omega(n_P+\sum_v n_{B_v}),&
 H_F&=\kappa\sum_{uv}(I-\operatorname{SWAP}_{uv}),\\
 H_S&=a_dX_Q+b_d(Z_Q+Z_P)+c_dZ_QZ_P,&
 V_{\rm loc}&=g(\sigma_P^+\sigma_e^-+\sigma_P^-\sigma_e^+),\\
 H_{\rm loc}&=H_E+sI+H_F+H_S+V_{\rm loc}.&&
 \end{aligned}
\tag{6}
\]
All these terms commute with the actual \(H_E\). Hloc remains installed throughout. The parent proves on the complete reference space that its symmetric kernel \(\Pi\) has gap at least \(\Delta\), and that, for \(\lambda\leq\Delta/8\), the full local-to-projected-star error is
\[
 E_{\rm elim}(t)<2048\lambda\sqrt n/\kappa,
 \qquad 0\leq t\leq2\pi/\lambda.
\tag{7}
\]
This is an inverse bound on the actual exchange range and pays all complementary output. No one-excitation approximation is imported.

The exact star residual on \(\beta\) is \(g/(2\sqrt N)\). Its comparison data Hamiltonian satisfies
\[
 \begin{gathered}
 H_{\rm eff}=a_d(X_Q+X_P)+b_d(Z_Q+Z_P)+c_dZ_QZ_P,\\
 \|H_{\rm eff}\|=9\lambda/4,\qquad
 \tau=\pi/\lambda,\qquad
 e^{-i\tau H_{\rm eff}}=e^{-i\pi/4}\operatorname{SWAP}_{QP}.
 \end{gathered}
\tag{8}
\]
The physical free factor is restored in the order
\[
 e^{-ist}[e^{-it\omega n_P}e^{-itH_{\rm eff}}\psi]
       \otimes\beta(t),\qquad
 \beta(t)=e^{-it\omega\sum_v n_{B_v}}\beta.
\tag{9}
\]
The two data exponentials need not commute. Keeping the same free factor at time t in the target gives
\[
 E_{\rm loc,aged}(t)
 <2048\lambda\sqrt n/\kappa+gt/(2\sqrt N)
                  +(9\lambda/4)|t-\tau|.
\tag{10}
\]
Indeed left multiplication by \(e^{-it\omega n_P}\) preserves the norm of the difference between the effective gate at t and at \(\tau\). There is no \(\omega|t-\tau|\) term and no assumption \(\omega\tau\in2\pi\mathbb Z\). This is valid because the target has changed, not because the physical free evolution has been removed.

## 3. A common positive suffix at a selectable clock position

Let the finite scalar clock run from0 to L. Place the fourteen-slice chronological suffix
\[
 H_b,\quad D_b=\operatorname{CZ}_{b,P},\quad H_b,\quad X_b,
 \quad\text{all-rail }X_R
\tag{11}
\]
at coordinates \(q-14,\ldots,q-1\), where \(16\leq q\leq L\). The endpoint construction sets \(q=L\); the moving-profile construction specifies a central q. Coordinates0 through q-15 are ordinary input heads, and q through L are ordinary completed-output heads.

The parent's supplied signed positive head bond is
\[
 Q_\eta(i,j;t)=t[n_i+n_j-\eta(\sigma_i^+\sigma_j^-+
                             \sigma_i^-\sigma_j^+)],
 \quad\eta=\pm1,\ t>0,
\]
with full spectrum \(0,0,2t,2t\). Each diamond has four signed outer bonds with equal left-arm weights \(a_L\), equal right-arm weights \(a_R\), and contacts
\(g_d n_u(I+D)+g_d n_v(I-D)\), for \(D=Z_P,X_R\), or I. The fixed head-arm rotation \(B=(u+v)/\sqrt2,C=(u-v)/\sqrt2\), followed by the exact prefix gauge, gives scalar hoppings \(-\sqrt2a_L,-g_d,-\sqrt2a_R\) and forward word \(-D\). Identity diamonds retain \(2g_d n_u\) and omit the zero contact.

For general \(\alpha>0\), set
\[
 k_r=\alpha\sqrt{r(L+1-r)},\quad
 J_c=\alpha(L+1)/2,\quad C_{\rm head}=4J_c.
\tag{12}
\]
Every \(k_r\leq J_c\). Each diamond outer weight is its corresponding \(k_r/\sqrt2\), the middle contact its corresponding \(k_r\); Hadamard signed bonds have weight \(k_r/\sqrt2\), and ordinary/permutation/cable bonds weight \(k_r\). Different links may have different values, but both arms and all four rails share the required indexed coefficient. Add one head occupation with coefficient

| Head type | Positive added coefficient |
|---|---|
| Diamond terminal | \(C_{\rm head}-(2a_{\rm end}+k_{\rm cable})\) |
| Diamond arm | \(C_{\rm head}-(a_L+a_R+g_d)\) |
| Hadamard port | \(C_{\rm head}-(\sqrt2 k_H+k_{\rm cable})\) |
| Permutation port | \(C_{\rm head}-(k_{\rm link}+k_{\rm cable})\) |
| Ordinary site/endpoints | \(C_{\rm head}-(k_{\rm left}+k_{\rm right})\) |

Missing endpoint bonds are zero. Module subtractions are at most \((\sqrt2+1)J_c\) and ordinary ones at most \(2J_c\), strictly below \(C_{\rm head}\). No extra uniform-matching \(\mu\) shift is added.

The module coordinates are first H at q-14,q-13; first diamond at q-12,q-11,q-10,q-9; second H at q-8,q-7; permutation at q-6,q-5; final diamond at q-4,q-3,q-2,q-1. The ordered prefixes are

| Coordinate | Prefix \(G_x\) |
|---|---|
| \(x\leq q-14\) | \(I\) |
| \(q-13,q-12,q-11\) | \(H_b\) |
| \(q-10,q-9,q-8\) | \(-D_bH_b\) |
| \(q-7,q-6\) | \(-H_bD_bH_b\) |
| \(q-5,q-4,q-3\) | \(-X_bH_bD_bH_b\) |
| \(x\geq q-2\) | \(X_RX_bH_bD_bH_b=G_{\rm out}\) |

The two diamond signs cancel and \(G_{\rm out}=X_RC_P^{(b)}\). Every prefix commutes with \(H_E,H_F,H_S\): it is reference independent, acts trivially on Q and has only diagonal P dependence. In particular this includes both virtual arm coordinates. The physical arm rotation \(\mathcal A\) is head-only. Consequently the exact one-head gauge gives
\[
 \begin{gathered}
 (\mathcal AG)^*H_{\rm head}(\mathcal AG)=h_L\otimes I,
 \qquad h_L=C_{\rm head}I-\sum_r k_r(|r\rangle\langle r-1|+\mathrm{h.c.}),\\
 \widetilde H=h_L+H_{\rm loc}+\mathcal D,\qquad
 \mathcal D_x=G_x^*V_{\rm loc}G_x-V_{\rm loc},\\
 \mathcal D_x=0\ (x<q-10),\qquad \|\mathcal D_x\|\leq2g.
 \end{gathered}
\tag{13}
\]
This is an exact mathematical difference after a unitary change of representation, not an installed higher-body interaction. All physical blocks remain positive and at most two-body.

The benchmark \(h_L+H_{\rm loc}\) contains the actual running local apparatus. Its scalar head profile from the product endpoint seed is exactly
\[
 f_x(t)=e^{-iC_{\rm head}t}b_x(t),\qquad
 b_x(t)=\sqrt{\binom Lx}[i\sin(\alpha t)]^x
                              [\cos(\alpha t)]^{L-x}.
\tag{14}
\]
The mathematical spin representation gives this finite-chain identity; those spins are not resources. It includes all finite endpoints without an infinite-packet or finite-cut approximation. Duhamel, on this benchmark trajectory, yields
\[
 E_{\rm join}(t)\leq2g\int_0^t
       \sqrt{\Pr[X_v\geq q-10]}\,dv,\qquad
 X_v\sim\operatorname{Bin}(L,\sin^2(\alpha v)).
\tag{15}
\]
Actual joint evolution need not factorize. The local benchmark has norm one for arbitrary correlated logical inputs. The seed at0 has identity gauge, so there is no initial-state matching error.

## 4. Endpoint freely aged window

Choose
\[
 \begin{aligned}
 L&=\left\lceil\max\{16,(8192/\epsilon)^2\}\right\rceil,\quad q=L,\\
 \lambda&=\min\left\{\omega/2,M/(4C_P),\Delta/8,
       \epsilon\kappa/(262144\sqrt n),4J_{\rm budget}/(L+1)\right\},\\
 \alpha&=\lambda/2,\quad J_c=\lambda(L+1)/4,\quad
 \tau=\pi/\lambda,\\
 w&=\min\{\epsilon/(288\lambda),\epsilon/(1024\lambda),
                            \epsilon/(64\lambda\sqrt L)\}.
 \end{aligned}
\tag{16}
\]
There is no integer rounding to a free revival. The chosen \(\lambda\) is the full minimum, not an arbitrary smaller value for the resource claim. On \([\tau-w,\tau+w]\), \(0<t<2\tau\), and (10) is \(<\epsilon/32\): elimination pays \(\epsilon/128\), star error is \(<\epsilon/64\), and effective-gate timing pays \(\epsilon/128\). The first w entry is redundant with the second but displays its allocation.

The parent's sharper time-zero overlap estimate applies without a free revival. For \(0\leq v\leq\tau\), \(Y=L-X_v\) is binomial with parameter \(\cos^2(\alpha v)\). Exponential Markov with parameter1/11 and \(1-e^{-1/11}\geq1/12\) gives
\[
 \sqrt{\Pr(Y\leq10)}\leq e^{5/11}e^{-L\cos^2(\alpha v)/24}.
\]
Using \(\cos\theta\geq2(\pi/2-\theta)/\pi\) and extending the Gaussian integral,
\[
 \int_0^\tau\sqrt{p_{\rm tail}(v)}\,dv
 \leq e^{5/11}\pi\sqrt{6\pi}/(\lambda\sqrt L).
\]
Multiplying by \(2g\) gives a coefficient \(2\sqrt2e^{5/11}\pi\sqrt{6\pi}<64\). For example \(\sqrt2<10/7,\pi<22/7,\sqrt{6\pi}<35/8,e^{5/11}<8/5\) give \(<440/7\); the last inequality follows from \(\log(8/5)\geq6/13>5/11\). The post-\(\tau\) integral costs at most \(2gw\). Thus
\[
 E_{\rm join}(t)<64/\sqrt L+2\sqrt2\lambda w<\epsilon/64,
 \quad 0\leq t\leq\tau+w.
\tag{17}
\]

The new endpoint estimate pays the entire head state without its global operator norm. Put \(\bar h=h_L-C_{\rm head}I\), \(d=t-\tau\). Since \(f(\tau)=e^{-iC_{\rm head}\tau}i^L|L\rangle\), stationarity gives
\[
 f(\tau+d)=e^{-iC_{\rm head}(\tau+d)}i^L e^{-id\bar h}|L\rangle,
 \quad \langle L|e^{-id\bar h}|L\rangle=\cos(\lambda d/2)^L.
\]
For both signs of d, the window ensures \(|\lambda d/2|<\pi/2\). Therefore
\[
 \begin{aligned}
 \|f(t)-e^{-iC_{\rm head}t}i^L|L\rangle\|^2
 &=2[1-\cos(\lambda d/2)^L]\\
 &\leq2L[1-\cos(\lambda d/2)]
 \leq L\lambda^2d^2/4.
 \end{aligned}
\tag{18}
\]
The last w entry makes this norm at most \(\epsilon/128\). This is a particular endpoint displacement, not a reduction of \(\|\bar h\|=\lambda L/2\), and no target phase has been fitted.

Let \(E_L\) be the physical endpoint insertion retaining the rail. The normalized complete target is
\[
 V_t^{\rm end}\psi=e^{-i(C_{\rm head}+s)t}i^Le^{-i\pi/4}
 E_L e^{-it\omega n_P}U_f\psi\otimes\beta(t).
\tag{19}
\]
The first three local allowances, (17) and (18) sum to
\[
 \sup_{[\tau-w,\tau+w]}
 \|e^{-itH_{\rm tot}}E_{\rm in}-V_t^{\rm end}\|<7\epsilon/128.
\tag{20}
\]
All nonendpoint heads are vacant in the comparator. It implies unhalved stabilized complete-output channel error \(<7\epsilon/64\) and joint endpoint/\(R=1\) probability \(>1-(7\epsilon/128)^2\).

Because \(\sqrt L>16\), the third entry of w is strictly smallest, so
\[
 w=\epsilon/(64\lambda\sqrt L),\qquad
 w/\tau=\epsilon/(64\pi\sqrt L).
\tag{21}
\]
At fixed positive \(\omega,M\), the clock cap eventually controls (16), giving \(\lambda=M/[16(L+1)]\), time and size orders \(\epsilon^{-2}\), and relative half-width \(\Theta(\epsilon^2)\). The absolute half-width is \(\Theta(M^{-1})\), tending to \(2048/M\) for this explicit enormous length floor. This is not a constant logical-output dwell, since (19) freely ages. The line-reference and old larger-clock alternatives in the frozen aged source are not operative policies of this cubic-focused note.

## 5. A central suffix and macroscopic completed-output region

The second construction uses a different actual clock and suffix placement. Write
\[
 \begin{gathered}
 h=\log(1024/\epsilon),\qquad
 L=\left\lceil(8192/\epsilon)^2h\right\rceil,\qquad
 s_h=\lceil\sqrt{Lh}\rceil,\\
 q=\lfloor L/2\rfloor-s_h,\qquad a_{\rm cut}=q-10,
 \qquad m_g=L/2-a_{\rm cut}.
 \end{gathered}
\tag{22}
\]
Here \(s_h\) is not the local scalar s. Since \(h>1\), \(\sqrt{h/L}\leq\epsilon/8192\), and \(s_h\leq L/8192+1\), we have q at least16, \(a_{\rm cut}>0\), q below L, and
\[
 0<m_g\leq\sqrt{Lh}+12<L/2.
\tag{23}
\]
There are q-14 ordinary input sites and L-q+1 ordinary output sites per rail. Output comprises approximately half of the entire chain.

Use the same local reference (4), but choose
\[
 \begin{aligned}
 \lambda&=\min\left\{\omega/2,M/(4C_P),\Delta/8,
       \epsilon\kappa/(262144\sqrt n),8J_{\rm budget}/(L+1)\right\},\\
 \alpha&=\lambda/4,\qquad J_c=\lambda(L+1)/8,\qquad
 C_{\rm head}=\lambda(L+1)/2,\\
 \tau&=\pi/\lambda,\qquad w=\epsilon/(1024\lambda).
 \end{aligned}
\tag{24}
\]
The factor \(\alpha=\lambda/4\) is intentional: at the local gate time \(\alpha\tau=\pi/4\) and the scalar head mean is L/2. Its clock cap is correspondingly \(8J_{\rm budget}/(L+1)\), not the endpoint family's factor4. Every coefficient and compensation is recomputed for this actual geometry.

### 5.1 Finite-binomial tail bound

For a Bernoulli Z of mean p, define \(F(t)=\log\mathbb E e^{t(Z-p)}\). It has \(F(0)=F'(0)=0\) and \(F''(t)=p_t(1-p_t)\leq1/4\) for its tilted Bernoulli mean. Integrating twice for either sign of t gives \(F(t)\leq t^2/8\). For a sum X of L independent such variables,
\(\mathbb E e^{t(X-\mathbb EX)}\leq e^{Lt^2/8}\).
Exponential Markov with \(t=4a/L\), and its negative counterpart, therefore yields for \(a\geq0\)
\[
 \Pr[X-\mathbb EX\geq a]\leq e^{-2a^2/L},\qquad
 \Pr[X-\mathbb EX\leq-a]\leq e^{-2a^2/L}.
\tag{25}
\]
Degenerate Bernoulli parameters obey the same bounds by direct evaluation. This supplies the precise finite-tail inequality needed below.

### 5.2 Entire time-zero contact integral

For \(0\leq v\leq\tau\), set \(\theta=\alpha v\), \(y=\pi/4-\theta\). The head mean \(\mu=L\sin^2\theta\) obeys
\[
 L/2-\mu=(L/2)\sin(2y)\geq2Ly/\pi,\qquad
 a_{\rm cut}-\mu\geq2Ly/\pi-m_g.
\tag{26}
\]
Here the sine chord applies on \(0\leq2y\leq\pi/2\). Where the latter difference is positive, the square root of the upper tail in (25) is at most \(\exp[-(2Ly/\pi-m_g)^2/L]\); elsewhere use one. Put \(y_0=\pi m_g/(2L)<\pi/4\). Since \(dv=4d\theta/\lambda\),
\[
 \begin{aligned}
 \int_0^\tau\sqrt{\Pr[X_v\geq a_{\rm cut}]}\,dv
 &\leq\frac4\lambda\left[y_0+
 \int_{y_0}^{\infty}e^{-(2Ly/\pi-m_g)^2/L}\,dy\right]\\
 &=\frac{2\pi}{\lambda}\left[\frac{m_g}{L}
                  +\frac{\sqrt\pi}{2\sqrt L}\right].
 \end{aligned}
\tag{27}
\]
This is an integral of norms over the full journey from the product seed, not an oscillatory cancellation argument or an assumption of zero early contact.

Multiplying by \(2g\) and using (23),
\[
 E_{\rm join}(\tau)
 \leq4\sqrt2\pi\left[\frac{m_g}{L}+\frac{\sqrt\pi}{2\sqrt L}\right]
 <18\frac{\sqrt h}{\sqrt L}+\frac{216}{L}+\frac{16}{\sqrt L}
 <\frac{35\epsilon}{8192}<\frac{\epsilon}{128}.
\tag{28}
\]
For explicit arithmetic, \(\sqrt2<10/7,\pi<22/7,\sqrt\pi<16/9\) give \(4\sqrt2\pi<18\) and \(2\sqrt2\pi\sqrt\pi<16\). The first and third terms are bounded by \(18\epsilon/8192\) and \(16\epsilon/8192\); the remaining term is less than \(\epsilon/8192\) using the length floor and \(h>1\).

After \(\tau\), the defect remains installed on output. The extra contact over w is bounded by \(2gw\), not omitted. Thus uniformly from zero through \(\tau+w\),
\[
 E_{\rm join}(t)<\epsilon/128+2\sqrt2\epsilon/1024<\epsilon/64.
\tag{29}
\]
The actual joint state need not have a small or factorized suffix occupation; (15) evaluates the exact factorized benchmark and pays the full actual difference.

### 5.3 Normalized common moving output, including its phase

For \(t\in[\tau,\tau+w]\), \(\alpha t\in[\pi/4,\pi/4+\epsilon/4096]\subset[0,\pi/2]\); the scalar mean is at least L/2. Since \(q\leq L/2-s_h\), (25) gives
\[
 p_{\rm bad}(t)=\sum_{x<q}|b_x(t)|^2
 \leq e^{-2s_h^2/L}\leq e^{-2h}=(\epsilon/1024)^2.
\tag{30}
\]
The event x less than q is contained in x at most q, so the integer threshold causes no loss. Let \(P_{\rm out}=\sum_{x=q}^L|x\rangle\langle x|\) and define
\[
 \gamma_t=\frac{P_{\rm out}b(t)}{\sqrt{1-p_{\rm bad}(t)}}.
\tag{31}
\]
This unit vector is the same for all logical inputs and rails. It is proportional to
\[
 \sum_{x=q}^L\sqrt{\binom Lx}\,i^x
       \sin(\alpha t)^x\cos(\alpha t)^{L-x}|x\rangle.
\tag{32}
\]
The \(i^x\) phase at every position is retained. The common \(e^{-iC_{\rm head}t}\) is excluded from \(\gamma_t\) and appears once in the complete target. An endpoint \(i^L\) substitution would be wrong here.

Because \(\langle b(t),\gamma_t\rangle=\sqrt{1-p_{\rm bad}(t)}>0\),
\[
 \|b(t)-\gamma_t\|^2
 =2[1-\sqrt{1-p_{\rm bad}(t)}]\leq2p_{\rm bad}(t),
 \qquad \|b(t)-\gamma_t\|<\epsilon/128.
\tag{33}
\]
This pays every omitted input/suffix head and the normalization. It is a target defined solely by the known scalar clock and time; no actual successful branch is normalized. The finite endpoint L is included in the exact output profile and needs no infinite-ray or boundary-return approximation.

Let \(B_t\) embed \(\gamma_t\) into the ordinary physical output heads, preserving the logical rail. On all this support \(\mathcal A=I\) and \(G_x=G_{\rm out}\). The complete normalized isometry is
\[
 V_t^{\rm ray}\psi=e^{-i(C_{\rm head}+s)t}e^{-i\pi/4}
       B_t e^{-it\omega n_P}U_f\psi\otimes\beta(t).
\tag{34}
\]
Every physical head outside that output profile is vacant in the target. All data/reference outputs are retained. There is no extra \(i^L\), suffix minus, uniform \(\mu\) phase or fitted scalar.

On this one-sided interval, (7) pays \(\epsilon/128\), the star term is \(<\epsilon/64\) since \(t<2\tau\), and local timing is \(9\epsilon/4096<\epsilon/128\). Hence local error is \(<\epsilon/32\). Combining it with (29) and (33), then undoing the exact physical gauge, proves the moving-profile conclusion
\[
 \sup_{[\tau,\tau+w]}
 \|e^{-itH_{\rm tot}}E_{\rm in}-V_t^{\rm ray}\|<7\epsilon/128.
\tag{35}
\]
It implies unhalved stabilized complete-channel error \(<7\epsilon/64\) and probability \(>1-(7\epsilon/128)^2\) for the joint event “head in q,...,L and R=1.” Both statements are consequences of the complete normalized comparator, not premises about postselection.

## 6. Literal counts, incident cap and geometry for both choices

Moving the suffix changes neither its modules nor their support inventory. Fourteen slices have56 heads and82 non-compensation blocks:22 in controlled-Z diamonds,24 in record diamonds,16 in the two Hadamard layers,4 permutation bonds and16 interlayer cable bonds. Adding56 compensations gives138 suffix blocks.

Each rail has q-14 input sites and L-q+1 output sites, totaling L-13 ordinary sites. It also has L-13 ordinary links outside the suffix, including both external connections. Thus there are \(4L-52\) ordinary heads, the same number of ordinary bonds and the same number of ordinary compensations. In both constructions,
\[
 \begin{aligned}
 \text{head qubits}&=4(L+1),&\text{head blocks}&=8L+34,\\
 \text{total qubits}&=4L+N+7,&
 \text{total blocks}&=8L+N+40+3n^2(n-1).
 \end{aligned}
\tag{36}
\]
The local apparatus has N+1 free occupations, five data/exchange blocks and \(3n^2(n-1)\) reference bonds. No mathematical spins or analytical gauge operators count as hardware.

Both actual policies ensure \(J_c\leq M/64\) and \(C_P\lambda\leq M/4\). Full-support positive-block incident loads obey
\[
 \begin{aligned}
 \operatorname{load}(P)&\leq\omega+C_P\lambda+8J_c
                 \leq\omega+M/4+M/8,\\
 \operatorname{load}(Q)&<M/4,&
 \operatorname{load}(R)&\leq16J_c\leq M/4,\\
 \operatorname{load}(\text{head})&\leq(5+\sqrt2)J_c<\Lambda,\\
 \operatorname{load}(B_e)&\leq\omega+6\kappa+2g
                         <\omega+3M/16+M/4,\\
 \operatorname{load}(B_v),\ v\ne e&\leq\omega+12\kappa
                                      =\omega+3M/8.
 \end{aligned}
\tag{37}
\]
These include the positive identities and occupations, not reduced-sector energies. Every bound is below \(\Lambda\). All installed terms preserve the actual \(H_E\) and the head number.

For an explicit lattice placement, put P=(0,0,0), R=(1,0,0) in \(\{0,1,2,3\}^3\). Reserve left ports(i,3,3) and right ports(i,2,3), i=0,...,3. After P,R and these eight ports are removed,54 sites remain for the other48 suffix heads. Inject them in a fixed order. All suffix/contact pairs then have Manhattan range at most9.

Attach q-14 ordinary input sites above each left port, with q-15 adjacent to it and seed0 at the far end. Attach L-q+1 ordinary output sites above each right port, with q adjacent and L at the far end. Their eight horizontal coordinates are distinct, so the rays do not intersect one another or the cube away from their ports. Each ray bond is nearest-neighbor regardless of ray length.

Put Q=(0,0,-1) and \(B_{i,j,k}=(-1-i,-j,-k)\). These are disjoint from all heads and R. QP, the corner-P link and grid links are nearest-neighbor. The full device has range at most9 and maximum graph degree8 at R; it is not an all-nearest-neighbor loader. Unlisted geometric adjacency creates no coupling under the supplied selective-interaction premise.

## 7. Resource comparison and what the wider interval means

All following orders fix positive \(\omega,M\) and use the displayed full minima, not arbitrarily smaller \(\lambda\). The reference has \(n=\Theta(\epsilon^{-2/3})\), \(N=\Theta(\epsilon^{-2})\). Both local nonconstant restrictions have order \(M\epsilon^{4/3}\).

| Contract and actual policy | Head length and total size | Eventual sufficient duration | Relative width |
|---|---|---|---|
| Endpoint freely aged, (16) | \(\Theta(\epsilon^{-2})\) | \(\Theta(M^{-1}\epsilon^{-2})\) | half-width \(\Theta(\epsilon^2)\) |
| Moving-profile freely aged, (22),(24) | \(\Theta(\epsilon^{-2}\log(1/\epsilon))\) | \(\Theta(M^{-1}\epsilon^{-2}\log(1/\epsilon))\) | one-sided \(w/\tau=\epsilon/(1024\pi)\) |

For the ray policy, \(h=\log(1024/\epsilon)\) and the clock entry \(M/[8(L+1)]\) eventually dominates the local entries. Thus
\[
 \lambda=\Theta(M\epsilon^2/h),\quad
 w=\Theta(M^{-1}\epsilon^{-1}h),\quad
 \tau=8\pi(L+1)/M,\quad w=\epsilon(L+1)/(128M)
\tag{38}
\]
in that eventual clock-limited regime. At finite accuracy the exact minimum is mandatory. Both constructions have enormous supplied constants and no practical-performance or optimality assertion.

The ray's logarithmic size cost pays two distinct requirements: the completed-output probability tail and the prearrival contact caused by placing the suffix before the mean. Keeping its full moving profile avoids any endpoint displacement cost. It does not eliminate the post-arrival \(2gw\) cost or local gate timing of order \(\lambda w\). No lower bound on an optimal window is inferred from these sufficient estimates.

These are static devices with finite observation intervals, not interaction schedules. The freely aged logical factor and, in the ray case, spatial profile vary with t. Averaging unknown times can dephase logical coherences; neither pointwise complete-channel statement supplies a common fixed-U_f channel for such a mixture. A fixed-output target would need separate timing/revival control of \(\omega\), and old-P-before-transfer aging is a different ordered operation as (3) shows.

The exact common reference comparator is not an exact reference-return certificate. As in the parent energy-accounting result, actual total \(H_E\) is conserved while its mean differs from the comparator by \(\omega(\langle n_P\rangle_{\rm in}-\langle n_Q\rangle_{\rm in})\). Growing reference energy-operator norm permits this despite vanishing vector error. Exact reference equality is not guaranteed, and is not universally excluded at every input/time. Reference preparation, reset and repeated reuse are not supplied by the proof.

## 8. Source map, current disposition and remaining supplies

Canonical path:
`docs/ACTIVE_OUTPUT_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-18.md`.
Evidence root:
`outputs/active_output_windows_2026_10_18/source_checks/`.
The links below identify the frozen packaged evidence. ROOT installed this packet on the publication branch.

| New frozen evidence | SHA256 | Current scope/status |
|---|---|---|
| Aged endpoint proposal (`outputs/active_output_windows_2026_10_18/source_checks/active_energy_aged_window/PROPOSAL.md`) | `c27d1d965d4981b8831754b947fddb6d21ac2153957696cf2f5654f33f5ad3e3` | Complete changed ordered-target and endpoint-width argument. |
| Aged endpoint review (`outputs/active_output_windows_2026_10_18/source_checks/active_energy_aged_window_check/REVIEW.md`) | `3bceccec2ae60b983a8aceda4af9b5555ab05bc9d092eba1c112705b4a7b6e1b` | SUPPORT at explicitly freely aged scope; ROOT acceptance supplied. |
| Moving output-ray proposal (`outputs/active_output_windows_2026_10_18/source_checks/active_energy_output_ray/PROPOSAL.md`) | `b3adb12439a3333aa9d7a5c23a44029cb8266af13800d21e914e9abd727e0abf` | Frozen author source; scoped distinct support and ROOT acceptance now recorded. |
| Moving output-ray review (`outputs/active_output_windows_2026_10_18/source_checks/active_energy_output_ray_check/REVIEW.md`) | `7b6a72abad53395b2fd938e48cfe3ccc76cb6aac3eb1e67046caf0ad644b2bf4` | SUPPORT for the complete freely aged moving-profile theorem; fully read by this drafter and ROOT, with ROOT acceptance. |

The original research root is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. The output-ray review there at `active_energy_output_ray_check/REVIEW.md` is 23,437 bytes and 307 lines. It was absent when drafting began, then was frozen, completely read, and incorporated at the exact identity above. It found no required correction and specifically checked time-zero contact, all phase/normalization and physical inventory obligations. Historical pending statements in the frozen proposals remain author-time records; they are not rewritten. No inherited or editorial review is counted as a second independent proof of this author's output-ray source.

The direct canonical parent at SHA256 `8023deeb062288b75065576d89f726d528e077e7b10fac90333b33c61fbff110` is supplied as PR9746/head `8e119e9` ancestry; the short head identifier is ROOT-supplied integration context, not a Git observation by this task. The parent retains exact links/pins for physical suffix source `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570` and review `ebf747aa6327d0c240054d21eacf14c6b28aeae2fa9967d55101b9c25ce599a6`; resolvent source `7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895` and review `25f290e96014dd8622575c207fd66f125ae2160727ca7d0b7a7bf35b7c3de3b5`; and prefactor source `793e9706b867f415647f2f6b7370f8e0daba0bf5efb993be3373c5337e52d0d0` and review `aa56fd71a965ef3a81e1f05a73d6a58706d4439d797952e31fba92c98eddc347`. These unchanged proof interfaces are reused at their exact scopes rather than copied as new independent evidence. Their older pending flags remain historical author-time records.

The supplied ingredients remain product reference coherence, a coherent localized head input, blank R/other heads, equal gaps and degenerate Q/R/passive references, exact local ratios and local/head coupling relation, engineered indexed head links and compensations, and selective real positive finite-range interactions. Removing integer free revival for a different target does not remove coefficient calibration. This note imports no weighted-bond, detuning, generic matrix-error or manufacturing-tolerance theorem, regardless of the eventual publication branch base. The exact binomial and physical gauge calculations are not native fabrication or initialization mechanisms.

There is no exact all-time current-record factorization, no normalized rare-R1 correctness, no arbitrary H_PE operation, native preparation, thermal certificate, external correction, physical release, stable capture, reset, permanent halt or reference reuse result. After either window the constant Hamiltonian continues evolving and can undo the operation.

ROOT exposed both new routes and read their sources; the endpoint reviewer and the output-ray author are this drafting worker. The worker also checked several inherited interfaces and has authorship exposure to the campaign's exact clock/gauge ancestry. The output-ray report was written by its assigned distinct checker, who disclosed shared campaign ancestry and prior cubic-gap/loader work; that actual report, rather than this authoring synthesis, supplies the new distinct check. This manuscript is author editorial integration, not another independent proof or evidence of the physical suppliers. The parent canonical text was read, with the truncated first read's affected central sections explicitly refreshed; the full changed source arguments are retained above.

The author created only its research-directory manuscript. ROOT fully read the changed source/check pairs and this manuscript, repairing a truncated aggregate display with a complete reread of lines1–235, then integrated the canonical note and frozen packet. No scientific executable, numerical fit, symbolic solver, sweep, blanket Lean run, physical validation or retained audit was performed. Deterministic source identities, links and citation topology supply mechanical checks only. No physical axiom or editable prompt changed.

## Finite execution boundary

The primary retains all sectors of its declared small matrices, the scalar phases and complete outputs, and checks explicit sufficient coefficient/count budgets. It does not dynamically execute the proof texts. Uniform-in-volume estimates follow from the displayed arguments under their hypotheses; finite controls alone do not establish them. Infinite-lead scattering is not a finite product-seed launcher, and none of these controls supplies capture, reset or permanent halt.
