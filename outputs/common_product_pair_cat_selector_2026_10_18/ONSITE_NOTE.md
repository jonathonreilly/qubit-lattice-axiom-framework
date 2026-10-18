# Static ancillary selectors with an exact energy reference

2026-10-18. Conditional supplied-state and finite-operation result; selectively checked, not independently audited or assigned retained status. The [selector review](../outputs/common_product_static_cat_selector_2026_10_18/common_product_static_cat_selector_check/REVIEW.md) and [exact-energy review](../outputs/common_product_static_cat_selector_2026_10_18/common_product_selector_exact_energy_check/REVIEW.md) support the respective arguments. These are source-exposed same-model checks with shared ancestry, not blind replication. This new manuscript remains an integration-review proposal; pending labels in the frozen sources reflect their earlier drafting chronology.

The [real two-body operation](COMMON_PRODUCT_TWO_BODY_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md) requires a joint initial state close to twelve specified signed cats, blank original rest heads and blank record. The present construction adds 48 static positive onsite fields. A sufficiently small **assumed local selector-energy excess**, together with a separate blank-state assumption, implies the needed joint state quality, including retained environments. The fields remain installed during operation, and their full dynamical disturbance is paid. This is an optional energy-quality certificate, not a cooling process, preparation mechanism or claim about the ground state of the full running device.

The sufficient operating horizon remains \(\Theta(\Lambda^{-1}\epsilon^{-17}\log^5(e/\epsilon))\). The new sufficient absolute selector-energy allowance has the severe order

\[
\Theta\!\left(\Lambda\epsilon^{74}/\log^{20}(e/\epsilon)\right).
\]

An exact algebraic reference makes the required subtraction unambiguous; it does not establish that an experiment or preparation procedure attains that allowance.

## One square: static signs, unique ground and exact energy

On each existing ancillary square retain its four positive penalties once and define

\[
H_0=\Delta\sum_{r=1}^{4}\frac{I-Z_rZ_{r+1}}2,\qquad
H_{\rm sel}=H_0+h\sum_{r=1}^{4}(I-s_rX_r),\qquad
r_h=h/\Delta,
\]

with cyclic indices, \(s_r\in\{+1,-1\}\), and \(\prod_rs_r=\sigma\). One explicit choice is \((s_1,s_2,s_3,s_4)=(\sigma,1,1,1)\). Each new field is a real positive one-qubit block of full norm \(2h\). Here \(h\) is the new selector field strength, distinct from the parent's packet bandwidth. For each entrance, the parent's ordered rows \((H,A)=(X,X),(X,Y),(X,Z),(Y,X),(Y,Y),(Y,Z)\) require

\[
(\sigma_l)=(+,-,+,-,+,-).
\]

Thus six squares select cat+ and six select cat−, where \(\mathrm{cat}_{\sigma}=(|0000\rangle+\sigma|1111\rangle)/\sqrt2\). A local Z conjugation removes negative field signs and maps the chosen cat to cat+; this is an exact spectral comparison, not a physical pulse.

The [selector argument](../outputs/common_product_static_cat_selector_2026_10_18/common_product_static_cat_selector/PROPOSAL.md) treats both sectors of \(F=X_1X_2X_3X_4\). For

\[
0<r_h\le r_*:=\frac1{4\cdot32^3},
\]

the ground \(\psi_\sigma\) is unique, belongs to \(F=\sigma\), and satisfies

\[
\|\psi_\sigma-\mathrm{cat}_\sigma\|<20r_h,
\qquad \operatorname{gap}(H_{\rm sel})\ge
g_{\rm sel}:=4h^4/\Delta^3.
\]

The centered low energies in the two F sectors are

\[
E_t=-2h^2/\Delta-h^4/(2\Delta^3)
-\tfrac52(h^4/\Delta^3)t\sigma+R_t,\qquad
|R_t|\le\frac{\Delta(32r_h)^6}{1-(32r_h)^2}.
\]

At the stated radius the remainder is less than one eighth of \(h^4/\Delta^3\). The two-low-level splitting therefore exceeds \(g_{\rm sel}\). The other fourteen centered levels stay above \(2\Delta-4h\), while the chosen low energy is nonpositive and the low-level splitting is below \(8h<\Delta\). This establishes the full first-gap and uniqueness statements, not merely a comparison of two selected eigenvalues. It is the isolated four-spin selector calculation, not a sum of interacting gadget energies.

The [exact-energy supplement](../outputs/common_product_static_cat_selector_2026_10_18/common_product_selector_exact_energy/PROPOSAL.md) gives the subtraction explicitly. Set

\[
u=r_h^2,\qquad C=\sqrt{1+16u^2},\qquad
D=\sqrt{1+4u},\qquad L=\sqrt{2+8u+2C}.
\]

The exact one-square ground energy and exact first gap are

\[
e_{\rm sel}=4h+\Delta(2-L)
=4h-\Delta\frac{8u+32u^2/(C+1)}{L+2},
\]

\[
G_{\rm exact}=\Delta(L-1-D)
=4\Delta u^2\,
\frac{8+16u/(C+1)+4/(D+1)}{(C+D)(L+1+D)}.
\]

The positive rationalized gap selects the \(F=\sigma\) ground. These exact formulas hold on the supplement's larger domain \(0<r_h\le1/64\); the operating prescription here still uses the stricter \(r_*\). As \(r_h\to0\), \(G_{\rm exact}/(\Delta u^2)\to5\). The rationalized expressions avoid subtracting nearly equal roots when evaluating the small corrections. They do not remove the need to bound the error in an actual energy-excess subtraction. An unchecked fourth-order Taylor value must not replace \(e_{\rm sel}\).

## Joint energy-quality certificate with retained references

Let \(A_{\rm sel}=\sum_{l=1}^{12}H_{{\rm sel},l}\). The squares are disjoint and sign-conjugate, so this ancillary operator has unique ground

\[
\Psi_{\rm sel}=\bigotimes_l\psi_{\sigma_l},\qquad
E_{\min}(A_{\rm sel})=12e_{\rm sel},
\qquad \operatorname{gap}(A_{\rm sel})\ge g_{\rm sel}.
\]

Write \(\mathrm{Cats}=\bigotimes_l\mathrm{cat}_{\sigma_l}\). With compatible positive-overlap phases, telescoping gives vector distance below \(240r_h\) and unhalved density trace distance below \(480r_h\) between \(\Psi_{\rm sel}\) and Cats.

The arbitrary logical program/path/reference input is supplied physically on ordinary \(Q\), the two emitter qubits in their one-excitation dual-rail code, and a passive reference. Let \(\omega\) be a normalized joint state of the remaining apparatus and retained environment \(E\), independent of that arbitrary input. Define the assumed selector excess using the **exact** subtraction

\[
\mathcal E_{\rm sel}:=\operatorname{Tr}[(A_{\rm sel}-12e_{\rm sel}I)\omega]\ge0.
\]

The spectral inequality implies a joint ancillary bad weight at most \(\mathcal E_{\rm sel}/g_{\rm sel}\). Separately, let \(\Pi_{\rm blank}\) require vacancy of all original rest heads and \(R=0\), excluding the two supplied input emitters and leaving old \(P\) and \(E\) unrestricted. Put \(q_{\rm blank}=\operatorname{Tr}[(I-\Pi_{\rm blank})\omega]\). The two projectors commute. If their summed failure bound is below one, projecting a purification only as a mathematical comparison yields some normalized \(\sigma_{PE}\) and

\[
\begin{split}
&\left\|\omega-
 |\mathrm{vac}_{\rm rest},0_R\rangle\langle\mathrm{vac}_{\rm rest},0_R|
 \otimes|\mathrm{Cats}\rangle\langle\mathrm{Cats}|\otimes\sigma_{PE}\right\|_1\\
&\hspace{1cm}\le
2\sqrt{q_{\rm blank}+\mathcal E_{\rm sel}/g_{\rm sel}}+480r_h.
\end{split}
\]

This is a joint bound on all 48 ancillas and the other retained factors, not a sum of marginal fidelities. The square-root cost is retained even if an apparatus marginal happens to be diagonal. All preparation-device outputs must be included in \(E\) or another declared retained factor; no environment is erased or discarded by the proof.

The exact selector ground generally does **not** lie in the operating gadget's transformed \(T_l=+1\) sectors. Those operators contain Y factors on the ancillas rotated by the parent's real gauge, whereas the selector uses real X fields. The ground's \(F_l=\sigma_l\) condition agrees with the desired cat only in the penalty-zero space; it does not imply the transformed-sector condition outside that space. The literal state-distance bound pays this initial leakage. No sector-invariance assumption is added.

## Actual runtime and phase with the fields left on

Let \(H_{\rm run}\) be the parent's real, unpenalized exponent-17 Hamiltonian. It already contains every square's \(H_0\). Add only the 48 fields:

\[
H_{{\rm run},{\rm sel}}
=H_{\rm run}+48hI-h\sum_{l,r}s_{l,r}X_{l,r}.
\]

There is no second copy of \(H_0\), timed switch, or original-head chemical potential. The nonconstant field sum has full norm \(48h\), giving the complete reference-extended unitary bound

\[
\|e^{-itH_{{\rm run},{\rm sel}}}
-e^{-i48ht}e^{-itH_{\rm run}}\|\le48h|t|.
\]

This estimate does not assume that the selectors commute with the running gadget or preserve its low sectors. It pays their runtime leakage and correlations on the entire physical space. The exact scalar introduced by the installed field blocks is \(48h\). The isolated reference energy \(12e_{\rm sel}\) is neither the ground energy of the interacting runtime nor an additional phase.

Retaining the parent's notation, the complete target phase is precisely

\[
\exp\{-it[48\nu+s_{\rm joint}+\lambda\bar c+48h]\},
\quad s_{\rm joint}=-24\nu^2/\Delta+27\nu^4/\Delta^3,
\quad\bar c=8\bar b+8(\sqrt2-1)\bar j.
\]

The parent radial profile is evaluated at \(\lambda t\), with its fixed \(-i\), incoming translation \((\ell+57)k\), outgoing \(nq(k)\), Jacobian \(\sqrt{q'(k)}\), and positive final normalization. There is no separate record-bias, selector-ground or \(\lambda\bar\mu\) phase. The same unnormalized finite profile is used for the record1 branch at every horizon time.

## Simultaneous error, energy and resource budgets

For \(0<\epsilon\le1\), instantiate the parent's exact unpenalized prescription at \(\tau=\epsilon/8\) and gadget allowance \(\epsilon_g=\epsilon/16\), including its selected finite \(T,\ell\) and all coefficients. Set \(\Delta=\Lambda/4\) and choose exactly

\[
h=\min\left\{
\frac{\Delta}{4\cdot32^3},\quad
\frac{\Delta\epsilon}{3840},\quad
\frac{\epsilon}{768T}\right\}.
\]

Then \(480r_h\le\epsilon/8\) and \(48hT\le\epsilon/16\). The optional sufficient initial quality assumptions are

\[
q_{\rm blank}\le\epsilon^2/512,\qquad
\mathcal E_{\rm sel}\le g_{\rm sel}\epsilon^2/512,
\]

which imply the parent's complete rest-state allowance \(\epsilon_{\rm rest}\le\epsilon/4\). This inference supplies no channel that attains either premise. A directly supplied joint state satisfying that rest-state allowance also suffices for the displayed runtime bounds; the energy criterion is optional.

On the parent's final window \([3\ell/(4\lambda\bar j),T]\), the ideal-rest vector error is below \(11\epsilon/64\). Including the actual supplied rest state gives unhalved complete-channel error at most

\[
19\epsilon/32.
\]

For every \(0\le t\le T\), the same absolute record1 branch has unhalved subnormalized complete-channel error at most \(5\epsilon/8\). Both branch maps are contractions; there is no division by a rare flag probability. The final joint event of retained F output, record1, other original heads vacant and the signed-cat comparator has probability at least

\[
1-121\epsilon^2/4096-\epsilon/8.
\]

All outputs and references remain in these comparisons. The logical program appears on \(P\), the controlled path operation is retained, and old \(P/E\) information is relocated intact to \(Q/E\) in the comparator. Actual residual correlations and imperfect ancillary states remain charged to the full error. The parent finite window and whole-horizon branch contract are preserved; neither becomes a permanent halt or release theorem.

The fields add no sites or two-body couplers. Counts become **\(175+4\ell\) qubits and \(313+4\ell\) listed positive blocks**, comprising the parent's \(265+4\ell\) blocks plus 48 onsite fields. Each ancillary incident norm becomes \(2\Delta+2\nu+2h<\Lambda\); all other loads are unchanged. Every new block is real, positive and onsite, so the supplied at-most-two-body class and Manhattan range at most 35 remain unchanged. The magnitude \(h\) is an additional exact supplied coefficient.

As \(\epsilon\to0\), the third field-strength entry eventually controls. Thus

\[
\begin{aligned}
T&=\Theta(\Lambda^{-1}\epsilon^{-17}\log^5(e/\epsilon)),&
\ell&=\Theta(\epsilon^{-3}\log(e/\epsilon)),\\
h&=\Theta(\Lambda\epsilon^{18}/\log^5(e/\epsilon)),&
g_{\rm sel}&=\Theta(\Lambda\epsilon^{72}/\log^{20}(e/\epsilon)),\\
g_{\rm sel}\epsilon^2/512
&=\Theta(\Lambda\epsilon^{74}/\log^{20}(e/\epsilon)).&&
\end{aligned}
\]

The actual isolated-selector gap has the same order by the exact formula. These are sufficient-family and energy-quality scales, not necessary temperatures, cooling times or achievable measurement-precision claims. Certified intervals for \(12e_{\rm sel}\) may be used, but they must bound the exact reference tightly enough to support the actual excess allowance. The algebraic formulas alone do not verify that inequality for a prepared state.

## Scope and source exposure

The separately analyzed \(A_{\rm sel}\) is an ancillary observable whose ground selects and approximates the required cat signs. The full running Hamiltonian also contains the router and data couplers. Its ground need not be \(\Psi_{\rm sel}\), and small total operating energy is not the stated selector excess. No ground-state preparation, bath, thermalization, autonomous cooling, measurement, entropy disposal or initialization procedure is supplied. Blank original heads and record retain their separate quality requirement; no old head-gap, energy-to-blank or Gibbs certificate is revived.

Physical dual-rail input, input/rest independence, arbitrary specified positive real blocks, range-35 couplings, absent unwanted terms, exact coefficient correlations and observation/readout remain premises. No native realization, nearest-neighbor compilation, practical-cost result, reset or permanent halt is inferred. The earlier perturbative-gadget prior-art attribution remains unchanged.

The accompanying source-exposure list pins both complete new arguments and checks, the canonical operation parent, and the necessary existing isolated-square, signed-gauge and unpenalized-runtime interfaces. This pass read all four new texts completely and refreshed the historical exact-square polynomial output without executing its script. Earlier complete component reads are reused at their unchanged scopes; source and canonical copies were compared byte-for-byte. The exact-energy supplement was ROOT-authored, and its checker shared the original square-calculation ancestry. Neither that lineage nor this manuscript authoring is represented as blind independent replication.

Only this note and its source-exposure list are authored here. No scientific replay, packaging, canonical installation, publication or audit verdict is claimed. The manuscript itself still requires ROOT's integration review.
