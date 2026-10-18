# Supplied real two-body operation with a retained completion record

2026-10-18. Publication draft of a conditional finite-device result; selectively checked, not independently audited or assigned retained status. The [operation review](../outputs/common_product_two_body_operation_2026_10_18/common_product_two_body_scaled_operation_check/REVIEW.md), [real-gauge review](../outputs/common_product_two_body_operation_2026_10_18/common_product_real_two_body_gauge_check/REVIEW.md), and [quadratic-background refinement review](../outputs/common_product_two_body_operation_2026_10_18/common_product_two_body_background_refinement_check/REVIEW.md) support their respective constructions, including the exponent-21 sufficient family below. These are source-exposed same-model checks with shared ancestry, not blind replication. Pending labels in the frozen proposals record their drafting chronology; this new manuscript still requires its own integration review.

The construction composes the [resonant finite router](COMMON_PRODUCT_RESONANT_ROUTER_BOUNDED_THEOREM_NOTE_2026-10-18.md) with an exact entrance-program relocation, twelve simultaneous perturbative square gadgets, and a uniformly scaled background. It supplies a finite, static Hamiltonian made of specified **real positive blocks on at most two qubits**, with full-support incident norm cap \(\Lambda\), Manhattan interaction range at most 35, and a common complete-output comparison for arbitrary coherent program/path input and passive references. The quadratic-background refinement gives the sufficient family

\[
T=\Theta\!\left(\Lambda^{-1}\epsilon^{-21}\log^5(e/\epsilon)\right),
\qquad N_{\rm qubits}=\Theta\!\left(\epsilon^{-3}\log(e/\epsilon)\right).
\]

The separately checked alternative has \(T=\Theta(\Lambda^{-1}\epsilon^{-27}\log^5(e/\epsilon))\) at the same size order and output contract. These severe sufficient bounds establish neither optimality nor practical performance. Exact calibrated blocks, absent unwanted interactions, a physical dual-rail boundary input, and a joint preparation containing six cat+ and six cat− four-qubit registers remain supplied premises. The completion statement covers a declared finite window and an absolute branch contract up to its finite horizon; it is not permanent halt, reset, capture or release.

## Physical input and lossless program relocation

The [entrance interface](../outputs/common_product_two_body_operation_2026_10_18/common_product_autonomous_loader_interface/PROPOSAL.md) adds ordinary program qubit \(Q=(21,1,1)\) beside the old program \(P=(21,1,0)\). Each of two entrance bonds carries \(W=\operatorname{SWAP}_{QP}\). Its ideal four-support positive block is

\[
Q_j^W=j[n_i+n_j-a_j^\dagger a_iW-a_i^\dagger a_jW^*].
\]

This identity includes vacuum and double occupation. In the nominal one-head space, applying \(W\) only on the post-entrance head region is an exact unitary gauge relating the new reference router to a router logically controlled by \(Q\). Both sides of the entrance, possible returns, the single record bias, and the complete physical scalar are retained. There is no physical timed SWAP or discarded old register.

The [boundary contract](../outputs/common_product_two_body_operation_2026_10_18/common_product_boundary_input_contract/PROPOSAL.md) supplies an arbitrary state \(\rho_{LZ}\) of logical program/path and passive reference \(Z\), physically embedded by \(J_B\) into \(Q\) and the one-head subspace \(\operatorname{span}\{|10\rangle,|01\rangle\}\) of the two emitters. This embedding specifies an already prepared physical input; it does not implement an ordinary-qubit-to-dual-rail encoder. The actual initial state is

\[
(J_B\otimes I_Z)\rho_{LZ}(J_B^*\otimes I_Z)\otimes\omega_{\rm rest,E}.
\]

The fixed rest state is independent of that arbitrary input. It obeys the **joint**, unhalved trace-norm condition

\[
\left\|\omega_{\rm rest,E}
-|\mathrm{vac}_{\rm other\ heads},0_R\rangle\langle\mathrm{vac}_{\rm other\ heads},0_R|
 \otimes\bigotimes_{l=1}^{12}|\mathrm{cat}_{\sigma_l}\rangle\langle\mathrm{cat}_{\sigma_l}|
 \otimes\sigma_{PE}\right\|_1\le\epsilon_{\rm rest},
\]

where \(\sigma_{PE}\) is any fixed old-program/environment state and all ancillary/preparation outputs remain in the accounted apparatus or passive environment. Correct separate marginals do not replace this joint premise. A joint ideal-subspace failure probability \(q\) permits a comparison cost \(2\sqrt q\); this is a state estimate, not a preparation method.

In the ideal final output the supplied logical program occupies \(P\), the controlled path action is \(C_0=X_{\rm path},C_1=I_{\rm path}\), and the old \(\sigma_{PE}\) is relocated intact to \(\sigma_{QE}\). The environment \(E\) is untouched. Both \(P\) and \(Q\), all original heads, record, ancillary qubits and passive references remain in the comparison. The physical old information is relocated, not erased or traced out.

## Joint positive gadget and the mixed scalar

The [isolated square](../outputs/common_product_two_body_operation_2026_10_18/common_product_loader_bond_realization/PROPOSAL.md) is a component only. The [joint derivation](../outputs/common_product_two_body_operation_2026_10_18/common_product_full_swap_gadget/PROPOSAL.md) treats all twelve squares on their actual six shared data qubits. For each entrance \(e=0,1\), \(H\in\{X,Y\}\) and \(A\in\{X,Y,Z\}\), let

\[
O_l=(H_{i_e},H_{j_e},A_Q,A_P),\qquad \Omega_l=\prod_{r=1}^4O_{l,r}.
\]

The full occupation identity is

\[
Q_j^{\rm SWAP}=Q_{j/2}(i_e,j_e)+\tfrac j2(n_{i_e}+n_{j_e})
-\tfrac j4\sum_{H,A}\Omega_{e,H,A}.
\]

Each square has four new ancillas with positive penalties \(\Delta(I-Z_rZ_{r+1})/2\) and positive couplers \(\nu(I+O_{l,r}X_{l,r})\). In the initial complex description, twelve literal cat+ states select the conserved plus sectors. With \(\alpha=\nu/\Delta\), the joint normalized effective coefficients are

\[
s_{\rm joint}=-24\nu^2/\Delta+27\nu^4/\Delta^3,
\qquad g=5\nu^4/(2\Delta^3),\qquad
E_{\rm lead}=s_{\rm joint}I-g\sum_l\Omega_l.
\]

Elementary couplers on shared data do not all commute. Among 1056 cross-square elementary pairs, 132 anticommute; their ordered contributions produce the fourth-order scalar \(288-30-231=27\), rather than the isolated-square sum \(-6\). No other mixed fourth-order Pauli word survives. The [distinct joint review](../outputs/common_product_two_body_operation_2026_10_18/common_product_full_swap_gadget_check/REVIEW.md) gives the normalized graph calculation and a separately written exact ordered-path enumeration. The retained [enumerator](../outputs/common_product_two_body_operation_2026_10_18/common_product_full_swap_gadget_check/exact_paths.py) and [historical output](../outputs/common_product_two_body_operation_2026_10_18/common_product_full_swap_gadget_check/exact_paths.txt) are evidence of that calculation; they were not rerun for this manuscript.

The [exact real gauge](../outputs/common_product_two_body_operation_2026_10_18/common_product_real_two_body_gauge/PROPOSAL.md) applies \(S=\operatorname{diag}(1,i)\) on precisely those ancillas whose data operator is \(Y\). It converts the couplers to \(\nu(I+XX)\), \(\nu(I+ZX)\) or \(\nu(I+YY)\), all real symmetric and positive. The actual inherited background is also real. No data basis is changed. For each entrance, ordered pairs \((H,A)=(X,X),(X,Y),(X,Z),(Y,X),(Y,Y),(Y,Z)\) require cat signs

\[
(\sigma_l)=(+,-,+,-,+,-).
\]

Thus there are six plus and six minus cats on 48 ancillary qubits. Let \(J\) append the original twelve cat+ states and \(J_{\rm real}\) append the stated signed cats. With the \(S\) convention, \(J_{\rm real}=UJ\) exactly, with no extra injection or dynamical phase. The transformed conserved sectors, effective coefficients and complete error operators are unitary conjugates of the originals. This defines a different supplied real Hamiltonian/state pair; it does not prepare the signed cats or perform physical gauge pulses. Other cat-sign penalty ground sectors still exist.

## Background attachment and simultaneous prescription

Use the parent's explicit finite recipe at \(0<\tau\le1\), denoting its quantities by bars:

\[
\bar h=\bar\eta^2=\bar\zeta=\bar r=\tau/10^6,\quad
\bar D_1=\Lambda/8,\quad \bar D_0=\bar\zeta\bar D_1,
\quad\bar b=\bar\eta\bar D_0,\quad
\bar j=\Lambda\tau^2/(8\cdot10^{12}),\quad
\bar\kappa=\bar r\bar j.
\]

The parent's exact source policy, real cutoff, derivative ceilings, coefficient maximum \(u\) and \(\ell=\lceil100u\rceil\) are unchanged. They specify actual coefficients before selecting time. In particular \(U=\bar j\bar T=7\ell/8=\Theta(\tau^{-3}\log(e/\tau))\); no numerical fitted constant replaces that prescription. The source-policy constant in the parent is distinct from the gadget \(\alpha\) below.

Let \(\bar H_{\rm new}\) be the entrance-SWAP reference router with \(\bar\mu=\Lambda/4\) on every **original** head. Let \(\bar B\) remove its two four-support entrance bonds and insert the six residual positive blocks from the displayed decomposition. Then, on the entire original occupation space,

\[
\bar H_{\rm new}=\bar B-\tfrac{\bar j}{4}\sum_l\Omega_l.
\]

Set \(K=48\), \(\Delta=\Lambda/4\), \(\nu=\Delta\alpha\), and

\[
\lambda=10\Delta\alpha^4/\bar j,\quad B=\lambda\bar B,\quad
H_{\rm act}=B+48\nu I+H_0+V_{\rm real},\quad
T=U/(10\Delta\alpha^4)=\bar T/\lambda.
\]

Every background coefficient scales by this same \(\lambda\), including source contacts, detunings, compensations, bias and original-head penalty. There is no retained unscaled head gap. Coefficient matching is exactly \(g=\lambda\bar j/4\).

The checked [background component](../outputs/common_product_two_body_operation_2026_10_18/common_product_loader_component_background/PROPOSAL.md) and [full composition](../outputs/common_product_two_body_operation_2026_10_18/common_product_two_body_scaled_operation/PROPOSAL.md) first establish a rectangular commutator argument for all 48 couplers, with actual incidence bound

\[
\bar C_B=\sum_{l,r}\|[\bar B,O_{l,r}]\|<25\Lambda,
\qquad C_B=\lambda\bar C_B.
\]

Repeated data incidences are counted separately; the X/Y program terms do not receive the isolated ZZ component's favorable detuning cancellation. This first method assumes no small global background norm or full attached spectral gap. It pays the full-output allowance

\[
10K\alpha+|t|\left(R_6+6\alpha C_B\right),\qquad
R_6=\frac{\Delta(8K\alpha)^6}{1-(8K\alpha)^2}.
\]

Its five-entry minimum, stated exactly in the checked composition, makes this allowance at most \(\epsilon_g\) throughout the horizon and yields the accepted exponent-27 family. The earlier fixed-strength allowance failed to close; simultaneous scaling resolves that certificate by changing all background strengths and paying longer physical time. The failed bound was not a physical lower bound or a no-go theorem.

The [quadratic-background refinement](../outputs/common_product_two_body_operation_2026_10_18/common_product_two_body_background_refinement/PROPOSAL.md) uses a different analytic method and pays the finite volume explicitly. There are \(293+8\ell\) residual-background blocks, each with full norm below \(\Lambda\), so

\[
\|\bar B\|\le B_{\max}:=\Lambda(293+8\ell),\qquad
\|B\|\le\beta:=\lambda B_{\max}.
\]

This includes the extensive original-head penalty and scalar vacancies on all occupation sectors. It is not a one-head or local-norm substitution. The two-variable normalized effective operator for \(H_0+xV+yB\) is analytic on radii \(R_x=1/(16K\alpha)\), \(R_y=\Delta/(16\beta)\), with norm at most \(\Delta\). Because \(B\) is ancilla-free, its exact axis is \(E(0,y)=yB\); ancillary parity gives \(E(-x,y)=E(x,y)\). Bounding **all** even mixed orders \(x^{n\ge2}y^{m\ge1}\) by the convergent bivariate Cauchy sum yields

\[
\|E(1,1)-E(1,0)-B\|\le C_{\rm mix}\alpha^2\beta,
\qquad C_{\rm mix}=16384K^2.
\]

No mixed scalar or nonscalar term is dropped. With \(\alpha\le1/(32K)\) and \(\beta\le\Delta/32\), comparing the full projection to \(\Pi(0,1)=P_{\rm cat}:=JJ^*\) bounds its difference by \((256/105)K\alpha\). This ancillary low-space projector is distinct from the physical program qubit \(P\). The literal-endpoint simulation bound is

\[
16K\alpha+|t|\left(R_6+C_{\rm mix}\alpha^2\beta\right).
\]

This method does require a small **global** background and its corresponding low-space separation; the following prescription pays that hypothesis. For \(0<\epsilon_g\le1\), choose exactly

\[
\alpha=\min\left\{
\frac1{32K},\ \frac{\epsilon_g}{48K},\
\sqrt{\frac{5\epsilon_g}{2(8K)^6U}},\
\sqrt{\frac{\epsilon_g\bar j}{3C_{\rm mix}U B_{\max}}},\
\left(\frac{\bar j}{320B_{\max}}\right)^{1/4},\
\left(\frac{\bar j}{10\Delta}\right)^{1/4}
\right\}.
\]

The last two entries ensure \(\beta\le\Delta/32\) and \(\lambda\le1\). The first three evolution costs satisfy

\[
16K\alpha\le\epsilon_g/3,\qquad
TR_6\le\tfrac2{15}(8K)^6U\alpha^2\le\epsilon_g/3,\qquad
TC_{\rm mix}\alpha^2\beta
=C_{\rm mix}\alpha^2UB_{\max}/\bar j\le\epsilon_g/3.
\]

Thus the full-device simulation allowance is \(\epsilon_g\) for the entire horizon. The exact real conjugacy transfers this estimate as well: the background is ancilla-free, and the signed-cat input/output is \(UJ\). No physical preparation step or error allowance is removed by that transfer.

For \(\tau,\epsilon_g\) proportional to \(\epsilon\), \(B_{\max}=\Theta(\Lambda\epsilon^{-3}\log(e/\epsilon))\). The fourth entry eventually controls, giving \(\alpha=\Theta(\epsilon^{9/2}/\log(e/\epsilon))\) and \(\lambda=\Theta(\epsilon^{16}/\log^4(e/\epsilon))\), hence exponent 21 with logarithmic power 5. In the checked local-commutator alternative, \(\alpha=\Theta(\epsilon^6/\log(e/\epsilon))\), \(\lambda=\Theta(\epsilon^{22}/\log^4(e/\epsilon))\), and exponent 27 remains valid. Constants can be enormous; both prescriptions use exact supplied coefficients, not a tolerance or manufacturing theorem.

## Full target, physical phase and absolute branch

At reference time \(s=\lambda t\), retain the parent's exact inelastic radial profile

\[
B_n(s)=\frac{-i}{\sqrt{2\pi}}\int
e^{\,in q(k)+i(\ell+57)k-is\bar E(k)}\sqrt{q'(k)}\,g_{\rm src}(k)\,dk,
\]

where \(q(k)=\arccos(\cos k+\bar\kappa/(2\bar j))\), \(\bar E(k)=2\bar j(1-\cos k)\), and \(g_{\rm src}=\chi F/\sqrt p\) is the same complex source amplitude with the parent's real cutoff and positive normalization. Its full-line norm is one at every time by the \(q\)-Jacobian. Let \(B_{\rm fin}\) retain \(1\le n\le\ell\); its norm is at most one. On the final window define \(\beta_F=B_{\rm fin}/\|B_{\rm fin}\|\), with its proven nonzero positive normalization.

The complete normalized comparator uses this \(\beta_F(\lambda t)\), logical program on \(P\), controlled path operation, record1, every other original head vacant, the specified twelve signed cats, and the relocated \(\sigma_{QE}\). Its one common physical phase is exactly

\[
\exp\{-it[48\nu+s_{\rm joint}+\lambda\bar c+\lambda\bar\mu]\},
\qquad \bar c=8\bar b+8(\sqrt2-1)\bar j.
\]

The \(-i\), incoming translation \((\ell+57)k\), two different momenta and scalar phase are retained. No separately fitted phase or extra record-bias phase is allowed. Actual gadget evolution need not conserve original head number or retain perfect cats; those excursions remain in the full norm error. Only the ideal reference one-head trajectory uses the scalar \(\lambda\bar\mu\).

Uniformly for

\[
t\in\left[\frac{3\ell}{4\lambda\bar j},\frac{7\ell}{8\lambda\bar j}\right],
\]

the ideal-rest complete vector/isometry error is below \(3\tau/8+\epsilon_g\). For the supplied imperfect joint rest, the unhalved complete-channel discrepancy is at most

\[
\epsilon_{\rm rest}+3\tau/4+2\epsilon_g.
\]

For **every** \(0\le t\le T\), the actual record1 projection is compared to the same full output map with \(\beta_F\) replaced by unnormalized \(B_{\rm fin}(\lambda t)\). Both maps are contractions. Their unhalved subnormalized complete-channel discrepancy is at most

\[
\epsilon_{\rm rest}+\tau+2\epsilon_g.
\]

There is no early replacement by zero, division by a rare branch probability, or discarded apparatus. On the final window, the joint event of the intended F output, record1, other-head vacancy and supplied ancillary comparator has probability at least

\[
1-(3\tau/8+\epsilon_g)^2-\epsilon_{\rm rest}/2.
\]

For example, \(\tau=\epsilon/4\), \(\epsilon_g=\epsilon/8\) and \(\epsilon_{\rm rest}\le\epsilon/4\) give complete error \(11\epsilon/16\), absolute branch error \(3\epsilon/4\), and joint success at least \(1-49\epsilon^2/1024-\epsilon/8\). These are mathematical output/event statements, not a supplied measurement apparatus or a guarantee beyond \(T\).

## Geometry, cap and remaining physical supplies

The six data sites are the four entrance heads \((19,0,0),(20,0,0),(23,2,0),(22,2,0)\) and \(Q,P\) above. Square \(l=1,\ldots,12\) uses

\[
(24,4,2l),\ (25,4,2l),\ (25,5,2l),\ (24,5,2l).
\]

These sites avoid the retained finite rays, core, cables and writers. Square penalties are nearest-neighbor; data-to-ancilla couplers have Manhattan length at most 35, independently of \(\ell\). This is an enlarged finite-range interaction supply, not a nearest-neighbor routing theorem.

Each ancilla has full-support incident load \(2\Delta+2\nu<\Lambda\). Added load is \(12\nu\) per entrance head and \(24\nu\) at each of \(P,Q\). Original background head/program loads are below \(\Lambda/2\) before the nonincreasing scale, and these additions fit the remaining margin. The record bias is counted once. The installed device contains **\(175+4\ell\) qubits and \(389+8\ell\) listed positive blocks**, including \(124+4\ell\) original-head penalties. The inventory without those penalties would be \(265+4\ell\) blocks; the stated installed theorem includes them. No original-head penalty is added to the new ancillary qubits.

The real gauge removes complex matrix entries from this particular supplied construction. Arbitrary specified positive Pauli-product blocks, range-35 edges, exact coefficients and absent unwanted couplings remain assumptions; they have not been derived from the earlier primitive set or a native law. The old ground/energy-to-blank/Gibbs preparation certificates do not transfer to the actual gadget Hamiltonian, which changes original head number. Signed-cat preparation, dual-rail encoding, input injection work/time, coefficient tolerance, observation/readout and any reset or release must be supplied or separately proved.

The [prior-art record](../outputs/common_product_two_body_operation_2026_10_18/loader_gadget_prior_art/NOTE.md) identifies Jordan and Farhi's established perturbative cat-mediator paradigm. That general paradigm is not claimed as new here. The square construction, mixed scalar, full-output/background estimates and particular finite-family composition have their named scoped arguments and checks; no literature theorem or physical preparation claim is imported.

## Source exposure and review boundary

The accompanying source record pins every new proposal/review, the historical exact-check code/output, and the necessary unchanged parent interfaces. This authoring pass read all eight new argument/check pairs completely, the parent's finite resource argument/review, the single-control inventory and the actual writer inventory. It also read the isolated-square and joint-gadget historical checker code/output and the prior-art context note. Those historical programs were not executed again. Ancestor scattering proofs are reused through the explicitly checked parent interface, not claimed as a new blanket audit. The unreviewed root cross-path note is disclosed as design exposure, not additional independent validation.

Only this draft and its source-exposure record are authored here. Publication, canonical review and retained status are separate root/integration actions. No further runtime variant, native identification or unrelated continuation is included.
