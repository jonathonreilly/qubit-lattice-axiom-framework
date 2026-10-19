> Historical exposition/integration record. Mathematical arguments remain inspectable; historical status and execution assertions are not fresh evidence. Exact original recovery: `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`.

## 11. A product-clock return and a finite-window literal gate

**Status: conditional theorem supported by the distinct check, with no required correction, and accepted by ROOT at its stated supplier scope.** A specified real positive two-qubit clock block, added to the exactly calibrated mediator device of §10, gives the literal aged W operation with a common clock output on a positive-width observation interval. The device has five qubits and six positive blocks. Its clock starts in the real product state \(|00\rangle\); the mediator needs no selected input.

The new clock proof is an exact inverse rank-one spectral construction. The physical implementation uses §10's checked weak-background bound and retains its full scalar and effective mediator aging. At twice the ideal return time the clock implements \(W^2\), so the result is not permanent completion or a two-time same-W claim.

### 11.1. Literal old gate and a three-dimensional clock subspace

Put
\[
 X=X_1X_2,\qquad K=2I+Z_1Z_2,\qquad
 \theta=\arctan(4/3),\qquad
 W=e^{i\theta}e^{i\theta X}.
 \tag{CR1}
\]
Thus \(\cos\theta=3/5\), \(\sin\theta=4/5\), and the eigenvalues of W in the \(X=\pm1\) sectors are \(e^{2i\theta}\) and 1. Also \([K,X]=0\).

On the clock pair a,b, let \(T=Y_aY_b\). The real orthonormal vectors
\[
 e=\frac{|00\rangle-|11\rangle}{\sqrt2},\quad
 d=\frac{|01\rangle+|10\rangle}{\sqrt2},\quad
 f_0=\frac{|00\rangle+|11\rangle}{\sqrt2},\quad
 f_1=\frac{|01\rangle-|10\rangle}{\sqrt2}
 \tag{CR2}
\]
have T eigenvalues \(+1,+1,-1,-1\), respectively. Let
\[
 \mathcal S=d^\perp
       =\operatorname{span}_{\mathbb C}\{e,f_0,f_1\},\qquad
 T_3=T|_{\mathcal S}=2|e\rangle\langle e|-I_{\mathcal S}.
 \tag{CR3}
\]
The actual proposed clock input is the real product vector
\(|00\rangle=(e+f_0)/\sqrt2\in\mathcal S\).
The entangled vectors in (CR2) specify a basis for a real matrix; none is prepared as the input.

### 11.2. Interlacing spectra and positive weights

Define exact scalar parameters and three-point spectra
\[
 \begin{gathered}
 \tau=2\pi-3\theta,\qquad
 \omega=\frac{2\pi}{\tau},\qquad
 \delta=2+\frac{2\theta}{\tau}=\frac{4+2\omega}{3},\\
 \alpha=(0,\omega,2\omega),\qquad
 \beta=(\delta-\omega,\delta,\delta+2\omega).
 \end{gathered}
 \tag{CR4}
\]
Monotonicity of tangent and \(1<4/3<\sqrt3\) give
\[
 \frac\pi4<\theta<\frac\pi3,\qquad
 \pi<\tau<\frac{5\pi}{4},\qquad
 \frac85<\omega<2 .
 \tag{CR5}
\]
The formula for \(\delta\) implies \(\omega<\delta<2\omega\): these inequalities reduce to \(\omega<4\) and \(\omega>1\). Consequently
\[
 \alpha_1<\beta_1<\alpha_2<\beta_2<\alpha_3<\beta_3,
 \qquad \sum_k\beta_k-\sum_j\alpha_j=4.
 \tag{CR6}
\]
The nonuniform final spacing in \(\beta\) is part of this exact choice.

Let
\[
 q_j=-\frac{\prod_{k=1}^3(\alpha_j-\beta_k)}
             {4\prod_{l\ne j}(\alpha_j-\alpha_l)}
       \quad(j=1,2,3).
 \tag{CR7}
\]
All three \(q_j\) are positive. Before the leading minus sign, the numerator/denominator signs for \(j=1,2,3\) are respectively \((-,+),(+,-),(-,+)\), by (CR6).

To prove normalization, write \(p_\alpha(z)=\prod_j(z-\alpha_j)\) and \(p_\beta(z)=\prod_k(z-\beta_k)\). Matching the three residues and the value at infinity gives the rational identity
\[
 \frac{p_\beta(z)}{p_\alpha(z)}
        =1-4\sum_{j=1}^3\frac{q_j}{z-\alpha_j}.
 \tag{CR8}
\]
Indeed, the difference has no finite pole and tends to zero at infinity. Its \(1/z\) coefficient, using the trace difference in (CR6), proves
\[
 \sum_jq_j=1.
 \tag{CR9}
\]
Therefore \(f=(\sqrt{q_1},\sqrt{q_2},\sqrt{q_3})^{\mathsf T}\) is a real unit vector.

### 11.3. Explicit orthogonal map and clock matrix

Use the ordered real basis \((e,f_0,f_1)\) of \(\mathcal S\), so e has coordinates \((1,0,0)^{\mathsf T}\). Put
\[
 h_f=f-e,\qquad
 O=I-\frac{2h_fh_f^{\mathsf T}}{\|h_f\|^2},\qquad
 G=O\,\operatorname{diag}(\alpha)\,O^{\mathsf T}.
 \tag{CR10}
\]
Since \(q_2,q_3>0\), \(0<\sqrt{q_1}<1\), so
\(\|h_f\|^2=2(1-\sqrt{q_1})>0\).
The Householder matrix O is real symmetric and orthogonal. Also \(h_f^{\mathsf T}f=1-\sqrt{q_1}\), hence \(Of=e\), and \(O^{\mathsf T}e=f\). These formulas fix the matrix without an unspecified eigenvector or sign choice.

Conjugation by \(O^{\mathsf T}\) sends \(G+4|e\rangle\langle e|\) to \(\operatorname{diag}(\alpha)+4ff^{\mathsf T}\). The determinant lemma and (CR8) yield
\[
 \begin{aligned}
 \det[zI-\operatorname{diag}(\alpha)-4ff^{\mathsf T}]
 &=p_\alpha(z)
       \left(1-4\sum_j\frac{q_j}{z-\alpha_j}\right)\\
 &=p_\beta(z).
 \end{aligned}
 \tag{CR11}
\]
The calculation first holds away from the \(\alpha_j\); polynomial continuation establishes it everywhere. Thus the rank-one update has exactly the spectrum \(\beta\).

Define a full four-by-four real clock matrix C with no \(\mathcal S/d\) cross block by
\[
 C|_{\mathcal S}=G+T_3,\qquad Cd=0 .
 \tag{CR12}
\]
Both C and T preserve \(\mathcal S\). The physical positive clock matrix will be
\[
 D=C+I.
 \tag{CR13}
\]
This fixes every coefficient as a real function of the specified literal angle \(\theta\).

### 11.4. Exact sector phases and common clock return

On \(\mathcal S\), the two old-X generators are
\[
 C-T=G,\qquad
 C+T=G+4|e\rangle\langle e|-2I_{\mathcal S}.
 \tag{CR14}
\]
The first has spectrum \(\alpha\). Since \(\tau\omega=2\pi\), its exponential at \(\tau\) is \(I_{\mathcal S}\).
The second has spectrum \(\beta-2\), with offsets \(-\omega,0,2\omega\) from \(\delta-2\). Since \(\tau(\delta-2)=2\theta\), its exponential is \(e^{-2i\theta}I_{\mathcal S}\).

Resolving the old X sectors and using the two W eigenvalues in (CR1) proves the exact identity
\[
 \boxed{
 e^{-i\tau(C-XT)}\big|_{\mathrm{old}\otimes\mathcal S}
       =e^{-2i\theta}W\otimes I_{\mathcal S}.}
 \tag{CR15}
\]
The common phase \(e^{-2i\theta}\) is explicit; no logical-sector-dependent phase is hidden in a clock output. This identity holds on the whole old space and every passive extension, and for arbitrary old-clock correlations supported in \(\mathcal S\). The proposed independent \(|00\rangle\) seed therefore returns to that same common real product output in the ideal clock evolution.

This is the new clock step. A uniform approximation to the Q interaction alone would not establish (CR15); the matrix C, its spectra and their phases do.

### 11.5. Positive clock block and exact physical composition

G is positive with \(\|G\|=2\omega\). Thus
\[
 \|C\|\le2\omega+1<5,\qquad
 D|_{\mathcal S}=G+2|e\rangle\langle e|\ge0,\qquad
 Dd=d,\qquad
 \|D\|\le2\omega+2<6.
 \tag{CR16}
\]
Positivity holds on the full clock space, including the unused d direction. The supplied block is a general real positive two-qubit matrix on the adjacent a,b sites. Its detailed coefficients are an actuator premise; they are not derived from an exchange-only, compass or native microscopic inventory. Positivity of this complete block does not assert a decomposition into separately positive Pauli summands.

Take exactly §10's calibrated five-qubit Hamiltonian \(H_\lambda\) and add one block:
\[
 H_{\rm gate}=H_\lambda+b_{\rm eff}D,\qquad
 H_\lambda=K+\lambda(I+Y_1Y_a)+\lambda(I+Y_2Y_b)
                       +4n_m+g(I+X_1X_m).
 \tag{CR17}
\]
Here \(\ell=\lambda^2\), \(g^2=3\ell(2-\ell)/(1-\ell)\), and \(a_{\rm eff},b_{\rm eff},c_{\rm eff}\) are exactly (EM1), (EM20). In particular \(b_{\rm eff}=2\lambda^2/a_{\rm eff}>0\). No old-only counterterm is added.

Apply the checked bound (EM31) to \(B=b_{\rm eff}D\). On the complete physical space, for every real t, it bounds the operator difference by
\[
 164\lambda\,[1+|t|b_{\rm eff}\|D\|],
 \tag{CR18}
\]
capped at two, against
\[
 V(t)=e^{-it(c_{\rm eff}+b_{\rm eff})}
       e^{-itK}e^{-itb_{\rm eff}(C-XT)}
                    \otimes e^{-it\,2a_{\rm eff}n_m}.
 \tag{CR19}
\]
The scalar \(b_{\rm eff}\) is the installed +I shift in D, retained once. The factorization is valid because K commutes with \(C-XT\). Its own \(2I\) is still inside \(e^{-itK}\). The exact-mediator bound is on all clock states, so (CR18) also pays for any actual leakage out of \(\mathcal S\); invariance of that subspace is required only of the ideal clock generator.

At the physical return time \(T_{\rm gate}=\tau/b_{\rm eff}\), (CR15) makes the comparison on \(\mathrm{old}\otimes\mathcal S\otimes m\)
\[
 e^{-iT_{\rm gate}(c_{\rm eff}+b_{\rm eff})-2i\theta}
   \big[e^{-iT_{\rm gate}K}W\big]\otimes I_{\mathcal S}
                \otimes e^{-iT_{\rm gate}\,2a_{\rm eff}n_m}.
 \tag{CR20}
\]
The mediator need not be selected or independent. The product comparison unitary acts on arbitrary existing old/mediator/passive correlations. Obtaining the common product clock output \(|00\rangle\) uses the actual independent clock input \(|00\rangle\); it does not replace a correlated mediator by a fresh environment.

### 11.6. A complete positive-width observation window

Choose \(0<\epsilon\le1\), \(\Lambda>4\), scaled half-width \(h=\epsilon/24\), and
\[
 0<\lambda\le\min\left\{
      10^{-3},\quad
      \frac{\epsilon}{656[1+6(\tau+1)]},\quad
      \frac{\Lambda-4}{8+2\sqrt7}\right\}.
 \tag{CR21}
\]
Observe at any
\[
 t\in\mathcal I_\epsilon
   :=\left[\frac{\tau-h}{b_{\rm eff}},
           \frac{\tau+h}{b_{\rm eff}}\right].
 \tag{CR22}
\]
The interval has strictly positive width and lies at positive times because \(\tau>\pi>h\). Write \(s=b_{\rm eff}t\). Then \(|s-\tau|\le h\) and \(|s|\le\tau+1\).

The first error is the physical comparison (CR18):
\[
 164\lambda[1+|s|\|D\|]
       \le164\lambda[1+6(\tau+1)]
       \le\epsilon/4.
 \tag{CR23}
\]
For the second error, selfadjoint-generator continuity and (CR16) give
\[
 \begin{aligned}
 \|e^{-is(C-XT)}-e^{-i\tau(C-XT)}\|
 &\le\|C-XT\|\,|s-\tau|\\
 &<6h=\epsilon/4 .
 \end{aligned}
 \tag{CR24}
\]
No old or mediator evolution is frozen when this clock factor is compared.

Let \(J_{00}\) append the independent clock state \(|00\rangle_{ab}\), with a fixed tensor ordering, to an arbitrary old/mediator/passive input. Combining (CR15), (CR19), (CR23) and (CR24) yields the complete isometry theorem
\[
 \boxed{
 \begin{aligned}
 \big\|e^{-itH_{\rm gate}}J_{00}
 &-e^{-it(c_{\rm eff}+b_{\rm eff})-2i\theta}
    J_{00}\big[(e^{-itK}W)\otimes
                         e^{-it\,2a_{\rm eff}n_m}\big]\big\|\\
 &\le\epsilon/2
       \qquad(t\in\mathcal I_\epsilon).
 \end{aligned}}
 \tag{CR25}
\]
Passive identities are implicit in the two displayed maps. The scalar, entire old aging and mediator aging use the actual observation time t; only the gate phase \(-2\theta\) is fixed by the return identity. Every actual clock and mediator output is included before any reduction. For mixed inputs and passive extensions, the unhalved complete channel distance is at most \(\epsilon\), by twice the isometry bound. There is no postselection, rare-event normalization or fitted output phase.

The mediator comparison frequency remains \(2a_{\rm eff}\), not the bare installed gap 4. Its existing correlations with the old system are retained. A separate product mediator output can be asserted only when that mediator was initially independent; the theorem does not require that additional premise.

### 11.7. Counts, incident loads and sufficient resource orders

The device uses five qubits and six positive blocks: K, two YY bonds, the onsite mediator gap, the old1/mediator XX bond and \(b_{\rm eff}D\). There are five nearest-neighbor edges plus the onsite block, and maximum geometric degree three. The clock edge joins the already adjacent a,b sites. No higher-body block or extra entangled input is installed.

The exact incident sums are
\[
 \begin{array}{c|c}
 \text{site}&\text{incident load}\\ \hline
 1&3+2\lambda+2g\\
 2&3+2\lambda\\
 a,b&2\lambda+b_{\rm eff}\|D\|\\
 m&4+2g .
 \end{array}
 \tag{CR26}
\]
Using \(g\le\sqrt7\,\lambda\), \(b_{\rm eff}\le\lambda^2\), \(\|D\|<6\), and \(\lambda\le1\), the clock loads are less than \(8\lambda\), and every row is bounded above by \(4+(8+2\sqrt7)\lambda\). Thus (CR21) is a conservative sufficient cap prescription.

For fixed \(\Lambda>4\), choose \(\lambda\) equal to the minimum in (CR21). For sufficiently small \(\epsilon\), \(\lambda=\Theta(\epsilon)\), while \(b_{\rm eff}/\lambda^2\to1\). Therefore this supplied family has
\[
 T_{\rm gate}=\Theta(\epsilon^{-2}),\qquad
 \frac{h}{b_{\rm eff}}=\Theta(\epsilon^{-1}),\qquad
 \frac{h/b_{\rm eff}}{T_{\rm gate}}
      =\frac{\epsilon}{24\tau}.
 \tag{CR27}
\]
The absolute half-width grows while its relative size shrinks with tolerance. These are sufficient orders in the fixed old-gap time unit, not optimality, practical precision, a native calibration claim or a comparison using the same actuator inventory as the original two-port device.

### 11.8. Return is not halt, and suppliers remain explicit

The exact clock identity at twice the scaled return time is
\[
 e^{-2i\tau(C-XT)}
       \big|_{\mathrm{old}\otimes\mathcal S}
       =e^{-4i\theta}W^2\otimes I_{\mathcal S}.
 \tag{CR28}
\]
This is not the same W operation. It is a statement about the ideal clock factor; any physical error at that later time is charged by (CR18) at that time, rather than by silently extending the window budget. The uniform base simulation in §10 does not make the logical output stationary.

The theorem supplies an approximate aged literal W and common clock return during the specified finite interval. It does not satisfy a two-time same-W contract, provide capture, release, reset, reuse or permanent halt, or implement the original two-port source/contact apparatus. The old K, fixed mediator gap, exact mediator calibration, detailed general real positive clock block, independent clock product seed and selected observation window all remain explicit premises. The mediator need not be initialized, but its effective aging must be retained.

### 11.9. Frozen source identities and exposure

The complete new source is [counterterm_free_gap_mediation/CLOCK_RETURN.md](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/CLOCK_RETURN.md), **9589 bytes, 144 lines**, SHA256 `4aff7c09f875daebe5d5f22e8682ab6225c9882e1cec5a61afd5c1f75d8dc027`.
Its distinct [CLOCK_RETURN_REVIEW.md](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation_check/CLOCK_RETURN_REVIEW.md), **11561 bytes, 113 lines**, SHA256 `a5cefc254ee147172d7e6006862e66133433df21642ec23f6ee6522de0627acc`, supports the exact clock construction and physical composition without a required correction. ROOT fully read and accepted both at their stated scope.

The sole new physical-composition dependency is the exact-mediator pair: [EXACT_ALL_TIME.md](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/EXACT_ALL_TIME.md), SHA256 `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`, and its [distinct check](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation_check/EXACT_ALL_TIME_REVIEW.md), SHA256 `80c09db471dea4542ccfe9b236b91ccd2cd285502ce4b091d59cbcfbfa7e1e70`. These are the unchanged sources of §10. No earlier second-order bound or negative-contract result is a theorem premise.

Historical pending-status text in the frozen clock source, including the author's not-yet-received exact-interface acceptance, is preserved. The actual check above supplies the present scoped disposition. ROOT proposed the inverse rank-one construction. The source author and distinct checker disclosed shared campaign/design and same-model exposure; neither this manuscript nor their shared ancestry is a blind or model-diverse validation claim.

The manuscript writer fully read all four displayed source/check bodies and reconstructed the new spectral, phase, positivity and window argument for this exposition. This is synthesis rather than another independent check or retained audit. Only `APPENDIX_CLOCK_RETURN.md` was written for this step. The frozen main note, selected-input historical appendix and exact-mediator appendix remain unchanged. No scientific executable, numerical optimizer, external search, Git/canonical/checkpoint/prompt/axiom edit, delegation, model/effort override or publication was performed. ROOT owns final packet provenance and integration.
