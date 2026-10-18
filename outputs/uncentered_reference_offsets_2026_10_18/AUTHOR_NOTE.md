# Uncentered reference-gap offsets with a fixed logical loading operation

Claim status: **bounded_theorem**, conditional on the supplied device and input below. The new source has a supporting distinct check and ROOT acceptance at its stated scope, as does the direct [structured-reference tolerance parent](ACTIVE_REFERENCE_TOLERANCE_BOUNDED_THEOREM_NOTE_2026-10-18.md). This author synthesis is not another independent validation or retained audit. Section7 identifies the exact evidence and disposition.

The parent permits independently weighted positive reference bonds and small reference-gap offsets whose mean is exactly zero. This extension permits **every** static assignment in the independent interval
\[
 |\delta_v|\le\frac{\lambda}{2N},
 \qquad \mu=\frac1N\sum_v\delta_v,                  \tag{1}
\]
without requiring knowledge or calibration of \(\mu\). The logical operation stays the same fixed \(U_f\); the complete target reference is explicitly
\(\beta_{\omega+\mu}(t)=(e^{-it(\omega+\mu)n}|+\rangle)^{\otimes N}\).
Thus an unknown mean is allowed by a supplier-dependent common apparatus output, not by discarding that output or silently changing the logical gate.

A conserved-charge factorization pays two P-qubit errors totaling at most \(2|\mu|t\), while retaining the extensive reference rotation exactly. On the parent's policy this addition is below \(\epsilon/128\). The resulting complete-vector and unhalved stabilized complete-channel ceilings are \(\epsilon/16\) and \(\epsilon/8\). Counts, cap and the sufficient full-loader size/time orders remain unchanged. P's declared gap \(\omega\), the original free revival and all coherent-input/positive-block suppliers remain premises. Actual unequal free energy is generally not conserved.

## 1. Physical device and one explicit prescription

Fix \(\Lambda>\omega>0\), \(M=\Lambda-\omega\), \(0<\epsilon\le1\), and \(0<\eta\le1\). Use the parent's finite four-rail head, five-layer delayed suffix and cubic reference grid. There are \(N=n^3\) reference qubits \(B_v\), with corner e coupled to P; Q and R are freely degenerate. Every additional reference \(\mathcal E\) is passive. Define \(n_D=|1\rangle\langle1|_D\) and \(\sigma_D^+=|1\rangle\langle0|_D\).

The installed local positive blocks are
\[
\begin{gathered}
 a(I+X_Q),\quad b(I+Z_Q),\quad b(I+Z_P),\quad c(I+Z_QZ_P),\\
 g(I+\sigma_P^+\sigma_e^-+\sigma_P^-\sigma_e^+),\\
 \kappa_{uv}(I-\operatorname{SWAP}_{uv})\quad(uv\text{ a grid edge}),\\
 \omega n_P,\qquad (\omega+\delta_v)n_{B_v},
\end{gathered}                                                     \tag{2}
\]
with
\[
 a=\lambda/\sqrt2,\quad b=\sqrt5\lambda/4,\quad
 c=3\lambda/4,\quad g=\sqrt2\lambda,\quad s=a+2b+c+g.
\]
The actual offset replaces the coefficient of an existing occupation block; a negative offset is not installed as a separate negative block. Each reference bond retains its exact positive swap matrix, with independently chosen static scalar weight
\(\kappa_{uv}\in[\eta\kappa_{\max},\kappa_{\max}]\).

Use the following complete policy, unchanged from the simultaneous centered parent:
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
 &\lambda&=\frac\omega{2m},\\
 \alpha&=\lambda/2,&\tau&=\pi/\lambda=2\pi m/\omega,\\
 J_c&=\lambda(L+1)/4,&C_{\rm head}&=4J_c,\\
 w&=\min\left\{\frac{\epsilon}{128(\omega+9\lambda/4)},
 \frac{\epsilon}{1024\lambda},\frac{\epsilon}{64\lambda L}\right\}.
\end{aligned}                                                     \tag{3}
\]
After fixing (3), allow every offset assignment (1) and every weight assignment in its declared interval. Weights and offsets may be adversarially cochosen; no probabilistic independence or favorable averaging is assumed. Neither individual values nor their mean enter the selected parameters. The case of equal weights is \(\eta=1\).

The head keeps the parent's links \(k_r=\alpha\sqrt{r(L+1-r)}\), common diagonal \(C_{\rm head}\), signed exchanges, positive compensations and chronological suffix
\[
 H_b,\quad\operatorname{CZ}_{b,P},\quad H_b,\quad X_b,
 \quad\text{all-rail }X_R.                           \tag{4}
\]
No physical mean-removal interaction, projection, higher-body term or corrective gate is installed.

Supply the input endpoint head with auxiliary rail \(a_{\rm path}=1\), arbitrary coherent joint b/Q/P/\(\mathcal E\) input, R=0 and every other head vacant. Independently supply \(\beta=|+\rangle^{\otimes N}\). The fixed operation is
\[
 U_f=I_{a_{\rm path}}X_R C_P^{(b)}\operatorname{SWAP}_{QP},\qquad
 C_P^{(b)}=|0\rangle\langle0|_P X_b+|1\rangle\langle1|_P I_b.
\tag{5}
\]
On computational inputs it maps \((b,q,p,0_R)\) to
\((b\oplus(1-q),p_Q,q_P,1_R)\). Old P/passive correlations are retained on Q/passive outputs, not discarded.

## 2. Complete fixed-logical target and result

Let \(E_{\rm in}\) be that supplied input isometry and \(E_{\rm out}\) the physical endpoint embedding, with all other heads vacant. For the actual assignment define
\[
\begin{aligned}
 \Phi(t)&=e^{-i(C_{\rm head}+s)t}i^Le^{-i\pi/4},\\
 \beta_{\omega+\mu}(t)&=
       \bigl(e^{-it(\omega+\mu)n}|+\rangle\bigr)^{\otimes N},\\
 \mathcal V_{\delta,t}\xi&=
      \Phi(t)E_{\rm out}U_f\xi\otimes\beta_{\omega+\mu}(t).
\end{aligned}                                                     \tag{6}
\]
This target is normalized and keeps every reference output and its collective phase. It is a specified formula, not an arbitrarily fitted apparatus state. It generally differs both from \(\beta_\omega(t)\) and from the product freely aged at every individual \(\omega+\delta_v\).

Under the stated supplied conditions, the theorem is
\[
 \sup_{t\in[\tau-w,\tau+w]}
 \|e^{-itH_\delta}E_{\rm in}-\mathcal V_{\delta,t}\|
 <\epsilon/16.                                       \tag{7}
\]
The norm is induced on the entire supplied input and stable under arbitrary passive-reference extensions. It implies unhalved stabilized complete-channel error \(<\epsilon/8\), with no apparatus discarded to obtain that bound, and
\[
 \Pr(\text{external endpoint AND }R=1)
       >1-(\epsilon/16)^2.                            \tag{8}
\]
The closed window has positive width and lies in \((0,2\pi/\lambda)\). Neither (7) nor (8) states normalized correctness on an arbitrarily rare event, exact earlier R1 correctness or permanent halt.

The logical operation in (6) is the same fixed \(U_f\) for all times in the window and every allowed assignment. It is not \(e^{-it\omega n_P}U_f\), and it does not assume revival at \(\omega+\mu\). Only the original calibrated \(\omega\tau=2\pi m\) is used. The extra mean-dependent P effect is paid in the proof below.

## 3. Exact conserved-charge comparison

Set
\[
 N_B=\sum_vn_{B_v},\quad G=n_P+N_B,\quad
 d_v=\delta_v-\mu,\quad D_c=\sum_vd_vn_{B_v}.
\tag{9}
\]
Let \(H_c\) be the full centered device at the **original** P gap \(\omega\), with the same actual bond weights, head and data coefficients, and reference offsets \(d_v\). Then
\[
 \sum_vd_v=0,\qquad |\mu|\le\lambda/(2N),\qquad
 |d_v|\le\lambda/N.                                  \tag{10}
\]
The parent theorem therefore applies to this actual centered assignment. It gives, on the entire window,
\[
 \|e^{-itH_c}E_{\rm in}-\mathcal V_{c,t}\|<7\epsilon/128,
 \qquad
 \mathcal V_{c,t}\xi=
       \Phi(t)E_{\rm out}U_f\xi\otimes\beta_\omega(t).
\tag{11}
\]
The parent obtains (11) from the weighted full-space gap, occupation and exchange inverse ranges, exact symmetric star, delayed suffix and complete endpoint clock comparison. Their five allowances are, respectively, local elimination \(<\epsilon/128\), star residual \(<\epsilon/64\), fixed-gate timing \(\le\epsilon/128\), suffix overlap \(<\epsilon/64\), and endpoint replacement \(\le\epsilon/128\). No uncentered compression is substituted into those arguments.

Every physical term of \(H_c\) commutes with G. Grid swaps conserve \(N_B\), corner exchange conserves \(n_P+N_B\), data fields are diagonal on P, and the suffix blocks involving P are diagonal on P. Q is freely degenerate; its X field does not change G. Head-only terms and all occupations also commute. These facts hold on the complete finite Hilbert space, not merely within a one-head or symmetric sector. Thus
\[
 H_\delta=H_c+\mu N_B=(H_c-\mu n_P)+\mu G,
 \quad[G,H_c]=[G,n_P]=0,
\]
\[
 e^{-itH_\delta}=e^{-it\mu G}e^{-it(H_c-\mu n_P)}.
\tag{12}
\]
The auxiliary \(H_c-\mu n_P\) is only a bounded self-adjoint comparison generator. It is not installed as a negative positive-block coefficient and needs no independent physical cap. The actual positive device remains (2). Ordinary full-space Duhamel gives
\[
 \|e^{-it(H_c-\mu n_P)}-e^{-itH_c}\|
 \le|\mu|t,\qquad t\ge0,                             \tag{13}
\]
using \(\|n_P\|=1\).

Retaining the first factor of (12) exactly transforms the centered target into
\[
 e^{-it\mu G}\mathcal V_{c,t}\xi
 =\Phi(t)E_{\rm out}[e^{-it\mu n_P}U_f\xi]
                  \otimes\beta_{\omega+\mu}(t).       \tag{14}
\]
The P rotation is after the whole \(U_f\); no commutation of \(n_P\) with the SWAP is assumed. Since
\(\|e^{-it\mu n_P}-I\|\le|\mu|t\), (11)–(14) prove
\[
 \|e^{-itH_\delta}E_{\rm in}-\mathcal V_{\delta,t}\|
 <7\epsilon/128+2|\mu|t.                             \tag{15}
\]
Both P contributions are paid: the changed dynamics in (13), and removal of the residual logical phase in (14). The extensive collective reference rotation is kept in (6), not bounded by \(N|\mu|t\) or silently called a scalar.

Finally, throughout the window,
\[
 2|\mu|t\le\lambda t/N<2\pi/N
 \le\frac{\epsilon^2}{4096\pi}<\epsilon/128.           \tag{16}
\]
Combining (15) and (16) gives (7). The channel bound follows from the isometry inequality \(\|V\rho V^*-W\rho W^*\|_1\le2\|V-W\|\), including passive references and mixed inputs by purification. The target lies in the event in (8); its actual complementary norm is bounded by (7), proving (8).

## 4. Unknown suppliers, observation time and energy meaning

For a fixed unknown assignment the theorem provides the explicit common output (6); it does not provide knowledge of its mean. If supplier assignments are classically randomized independently of the logical input, the same complete-channel bound holds against the corresponding mixture of the reference states in (6), with fixed logical \(U_f\). This is a uniform family of apparatus-output contracts, not closeness to one supplier-independent pure reference.

For a classical observation-time distribution supported in the window and independent of the logical input, convexity gives the same bound against fixed endpoint/\(U_f\) tensored with
\[
 \sigma_\mu=\int|\beta_{\omega+\mu}(t)\rangle
                  \langle\beta_{\omega+\mu}(t)|\,d\nu(t).
\tag{17}
\]
The scalar \(\Phi(t)\) cancels only in this density-matrix assertion; the vector theorem retains it. Random supplier/time choices may likewise be averaged with their actual joint distribution when it is independent of the logical input. If a classical choice register is physically retained, the ideal mixture retains the same register and its correlations with the reference output. Input-correlated choices and coherent superpositions/control of time or supplier settings are not covered by this classical averaging statement.

Nominal \(H_E=\omega G\) is still conserved. The actual free occupation operator is
\[
 H_{E,\mathrm{actual}}=\omega n_P+
                    \sum_v(\omega+\delta_v)n_{B_v}.
\tag{18}
\]
It is generally not conserved by the interactions: unequal adjacent offsets fail to commute with the corresponding grid swap, and even a uniform nonzero mean fails to commute with the P-corner exchange. The total static Hamiltonian remains conserved. Factoring the nominal charge in (12) does not restore conservation of (18). This limitation is already present for the parent's centered nonuniform gaps and remains explicit here.

The failed shortcut is to discard \(\Pi D\Pi=\mu\Pi N_B\Pi\) as a scalar on the symmetric reference space. It is not scalar, and the coherent product spans many number sectors. The proof instead retains its reference action and pays the nonextensive data consequences. Consequently removal of exact mean-zero calibration does not mean removal of P-frequency, revival, bounded-error or coherent-reference suppliers.

## 5. Positive cap, inventory and sufficient resources

Actual occupations remain strictly positive because
\[
 \omega+\delta_v\ge\omega-\lambda/(2N)
 \ge\omega(1-1/(4N))>0.                             \tag{19}
\]
The comparison centered occupations also satisfy the parent's positive interval. No comparison decomposition is physically implemented. Since the actual offsets are within the parent's larger absolute cap allowance, its full-support incident ceilings remain valid:
\[
\begin{aligned}
 \operatorname{load}(P)&\le\omega+M/4+M/8,
 &\operatorname{load}(Q)&<M/4,\\
 \operatorname{load}(R)&\le M/4,
 &\operatorname{load}(\text{head})&\le(5+\sqrt2)M/64,\\
 \operatorname{load}(B_v),\ v\ne e&\le\omega+M/2,
 &\operatorname{load}(B_e)&<\omega+9M/16.
\end{aligned}                                                     \tag{20}
\]
All are below \(\Lambda\). Each positive bond is charged by its full norm \(2\kappa_{uv}\le2\kappa_{\max}\), not by a projected value. The local occupation change adds no qubit, block, edge or scalar repair:
\[
 \text{qubits}=4L+N+7,\qquad
 \text{positive blocks}=8L+N+40+3n^2(n-1).            \tag{21}
\]
The parent's negative-coordinate reference cube, suffix and eight upward head rays stay disjoint. Reference-grid and P-corner couplings are nearest-neighbor; the full device keeps range at most nine and degree at most eight. It is not a nearest-neighbor claim for the entire loader.

At fixed positive \(\eta,\omega,M\), the actual minimum (3) has local accuracy entry of order \(\eta M\epsilon^{5/3}\), gap entry of order \(\eta M\epsilon^{4/3}\), and eventual controlling clock entry of order \(M\epsilon^2\). Revival rounding changes \(\lambda\) by less than a factor two. Hence
\[
 \text{size}=\Theta(\epsilon^{-2}),\qquad
 \tau=\Theta(M^{-1}\epsilon^{-2}),\qquad
 \frac{\lambda}{2N}=\Theta(M\epsilon^4).             \tag{22}
\]
The fixed-gate window is unchanged: \(w=\Theta(\epsilon)\), \(w/\tau=\Theta(\epsilon^3)\) at fixed parameters. These are sufficient asymptotics with enormous constants, not practical performance or optimality; eventual dominance is not uniform as \(\eta\to0\).

Generic norm-Duhamel for an arbitrary uncentered box \(|\delta_v|\le d\) gives \(t\|\sum_v\delta_v n_v\|\le tNd\). On this horizon it certifies an order-\(\epsilon\) addition only with sufficient \(d=O(\epsilon\lambda/N)=O(M\epsilon^5)\). The new interval has order \(M\epsilon^4\), but the comparison also permits the explicit supplier-dependent reference output. No same-target optimality or necessary-precision conclusion follows.

## 6. Remaining assumptions and limits

The result retains supplied exact positive block matrices, selective interactions, the declared bond lower bound and offset interval, original P gap and clock revival, freely degenerate Q/R, endpoint logical/head supply, coherent product reference and blank apparatus. It does not prepare or cool that reference, implement native coefficients, tolerate arbitrary matrix errors, include undeclared active \(H_{P\mathcal E}\), or preserve the actual unequal free-energy charge.

All-output norm proximity does not certify extensive energy moments, exact reference return or indefinite reuse. External endpoint arrival and R1 success in the stated window do not provide capture, reset or permanent halt. No output-ray, aged-logical-target, autonomous supplier, old literal-processor or normalized rare-branch theorem is inherited through publication genealogy.

## 7. Evidence closure and author exposure

Intended canonical destination: `docs/UNCENTERED_REFERENCE_OFFSETS_BOUNDED_THEOREM_NOTE_2026-10-18.md`. Intended new packet root: `outputs/uncentered_reference_offsets_2026_10_18/source_checks/`. The mathematical parent linked above is 30910 bytes, SHA256 `3ab7256b888e291c05689536700726724775efc57830bae869a937b2f1fdab87`, completely read and hash-verified for this synthesis. ROOT supplied PR9748/head `31ff71b7cf9d96757210f427d55849751144074d`; those publication facts are parent context, not a new remote/Git check. ROOT subsequently supplied the current publication base as regular PR9749 OPEN, head `080bca905af368f3088afce20ac798efe6043950`. That base is genealogy only and imports no output-window or other mathematical result; the direct mathematical parent remains PR9748.

The sole new source is [uncentered-offset proposal](../outputs/uncentered_reference_offsets_2026_10_18/source_checks/reference_uncentered_offsets/PROPOSAL.md), 17273 bytes, SHA256 `3d6f94736ca81dd7253fcd1778ecbb532fa3389a7eb2809e0cedc8e8b9faaf20`. Its [distinct review](../outputs/uncentered_reference_offsets_2026_10_18/source_checks/reference_uncentered_offsets_check/REVIEW.md), 18695 bytes, SHA256 `133fc11a87352d144cb7f99c2b7f191cd4248b1d1e4aea8ba08d3749cb6d0834`, supports the stated conditional full-loader scope with no required correction. ROOT fully read and accepted that disposition. The full report was read and its identity verified before this update. Its scope includes the two mean-dependent P errors, supplier-dependent complete reference versus fixed logical operation, classical mixtures and actual-free-energy limitation. Historical pending language in the frozen source is preserved; the new evidence packet contains only this source/check pair.

The exact inherited changed theorem is [centered/simultaneous source](../outputs/active_reference_tolerance_2026_10_18/source_checks/reference_gap_detuning/PROPOSAL.md) `d2a4ffae8b2f7d2e2fc0aae7c654f78665c400e16d9d8e0dfb7eb4689c380c23` with [check](../outputs/active_reference_tolerance_2026_10_18/source_checks/reference_gap_detuning_check/REVIEW.md) `11787f41138baea458ff7451424fabedde8b4a5f5fe185f1c30220311f38cf9e`. Its weighted dependency is [source](../outputs/active_reference_tolerance_2026_10_18/source_checks/weighted_cubic_reference/PROPOSAL.md) `b2f4aaa21de3508c3d51ebf51fc6132a6ad16b8a9a836b3bc1ef9b75973294cb` / [check](../outputs/active_reference_tolerance_2026_10_18/source_checks/weighted_cubic_reference_check/REVIEW.md) `8ce18b7cdea55345c292d391154713dff1940ff037e767aff96d47a523ccbb36`. These bodies remain in their existing packet. The parent's source map closes the unchanged cubic gap/resolvent, star, suffix and clock dependencies; no recursive source archives are needed.

ROOT proposed the mean-removal opportunity and the conserved-charge route, and also suggested a shifted-P auxiliary comparison. This author derived the route (12) using the original centered device, avoiding any new auxiliary positive-cap or revival assertion. The author also wrote the centered and weighted sources and several inherited interfaces. This manuscript is synthesis of source-exposed author work, not another distinct check. The reviewer also authored the centered review and shares inherited campaign exposure; the new review checks this extension, not its own inherited work anew. The workers share campaign ancestry and model/effort; their selective checks are not blind replication, physical verification or retained audit.

Only this research-directory manuscript and its explicitly requested preservation/diff files were written for the synthesis. The initial pending-disposition manuscript is preserved byte-for-byte as `NOTE_initial_3e56a8.md`, SHA256 `3e56a8c18a450d911e7af586314e3e6cc13bc9eb672f3b292ecc67588a8f75bb`; `DISPOSITION_UPDATE.diff` records the complete update. No scientific formula, proof, parameter, target, cap, count or error budget changed during the disposition update. Work used complete relevant source reading, analytical organization and deterministic identity/link bookkeeping. No scientific executable, simulation, external search, delegation, Git/canonical/checkpoint/axiom/editable-prompt/model change or publication was performed. ROOT owns final integration, packaging and publication. No editable prompt changed.
