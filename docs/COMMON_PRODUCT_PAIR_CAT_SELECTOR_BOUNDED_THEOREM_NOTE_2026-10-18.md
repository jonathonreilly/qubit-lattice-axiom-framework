# Static pair selectors with an exact ancillary energy reference

2026-10-18. Conditional supplied-state and finite-operation result; selectively checked, not independently audited or assigned retained status. The [pair-selector source](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_pair_cat_selector/PROPOSAL.md) has a [distinct scoped check](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_pair_cat_selector_check/REVIEW.md) supporting its spectrum, joint energy certificate and runtime composition. The source's branch terminology was clarified in response, with the original reviewed version preserved and the change [separately confirmed](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_pair_cat_selector_check/CORRECTION_CHECK.md). These checks have shared-source, same-model exposure; no blind replication is claimed. The accompanying integration record and publication check distinguish manuscript review from the source checks.

The [real two-body operation](COMMON_PRODUCT_TWO_BODY_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md) requires a joint rest state close to twelve specified signed cats, blank original rest heads and blank record. Two static positive pair terms on each existing ancillary square provide an optional **local selector-energy quality condition** sufficient for that state comparison. Their exact reference energy and full gap are known. The 24 added terms remain installed throughout operation, with their actual dynamical disturbance paid uniformly. They do not provide cooling, state preparation or a ground-state theorem for the full running device.

The sufficient operating horizon and size orders remain

\[
T=\Theta(\Lambda^{-1}\epsilon^{-17}\log^5(e/\epsilon)),\qquad
\ell=\Theta(\epsilon^{-3}\log(e/\epsilon)).
\]

The sufficient absolute selector-energy allowance has order

\[
\Theta\!\left(\Lambda\epsilon^{38}/\log^{10}(e/\epsilon)\right).
\]

This relaxes the earlier onsite-selector's sufficient energy-quality scale, while leaving runtime and device-size exponents unchanged. It does not establish that a preparation or measurement process can attain the stated inequality.

## Exact signed square and full spectrum ordering

Label each existing square cyclically \(1,2,3,4\). Retain its four positive penalties once and define

\[
H_0=\Delta\sum_{\text{cycle }ij}\frac{I-Z_iZ_j}{2},\qquad
H_{\rm pair}=H_0+h[(I-X_1X_2)+(I-\sigma X_3X_4)],
\]

with \(0<h\le\Delta/64\), \(r=h/\Delta\) and \(\sigma\in\{+1,-1\}\). Each new block is real, positive and two-body, of full norm \(2h\), on an existing nearest-neighbor square edge. Its sign is a supplied coefficient. The true added identity scalar is \(2h\) per square. Here \(h\) is the selector coupling, distinct from the parent's packet bandwidth.

The commuting pair parities \(p=Z_1Z_2\), \(q=Z_3Z_4\), and \(F=X_1X_2X_3X_4\) resolve the entire square. In \(p=q=+1\), define

\[
\mathrm{cat}_t=(|0000\rangle+t|1111\rangle)/\sqrt2,\qquad
\chi_t=(|1100\rangle+t|0011\rangle)/\sqrt2.
\]

On \(\operatorname{span}(\mathrm{cat}_t,\chi_t)\), the centered matrix is exactly

\[
H_{\rm pair}-2hI=
\begin{pmatrix}0&-h(1+\sigma t)\\-h(1+\sigma t)&2\Delta\end{pmatrix}.
\]

Writing \(R=\sqrt{\Delta^2+4h^2}\), the \(t=\sigma\) eigenvalues are \(\Delta\pm R\), and the \(t=-\sigma\) eigenvalues are \(0,2\Delta\), before restoring \(2h\). These are all four states in the \(p=q=+1\) sector. In \(p=q=-1\), the two internal pair walls give \(H_0\ge2\Delta\). When \(p\ne q\), the two cross-edge signs oppose and \(H_0=2\Delta I\). The added terms are positive, so all twelve states outside \(p=q=+1\) have full energy at least \(2\Delta\).

Consequently the unique full ground has \(F=\sigma\), exact energy

\[
e_{\rm pair}=2h+\Delta-R
=2h-\frac{4h^2}{R+\Delta},
\]

and exact first gap

\[
G_{\rm pair}=R-\Delta=\frac{4h^2}{R+\Delta}
\ge g_{\rm pair}:=h^2/\Delta.
\]

The competing low level has energy \(2h\), while all other levels exceed it. No sector or occupation state is omitted from this ordering. The ground is

\[
\psi_\sigma=\cos\theta\,\mathrm{cat}_\sigma+\sin\theta\,\chi_\sigma,
\qquad \tan\theta=\frac{2h}{R+\Delta}\le r,
\qquad \|\psi_\sigma-\mathrm{cat}_\sigma\|\le2r,
\]

with positive cat overlap. Uniqueness is not asserted at the excluded endpoint \(h=0\). These are exact finite-matrix statements; no perturbative remainder or onsite-selector spectrum is needed. The rationalized energy and gap avoid cancellation when evaluating the small corrections, but do not certify any prepared state's energy expectation.

## Joint energy-quality condition and the signed operating sectors

For each entrance, the parent's ordered data rows \((H,A)=(X,X),(X,Y),(X,Z),(Y,X),(Y,Y),(Y,Z)\) require signs

\[
(\sigma_l)=(+,-,+,-,+,-).
\]

Use these six plus/six minus signs on the twelve squares. With \(A_{\rm pair}=\sum_lH_{{\rm pair},l}\), the ancillary ground is the unique product \(\Psi=\bigotimes_l\psi_{\sigma_l}\), with exact reference \(12e_{\rm pair}\) and gap at least \(g_{\rm pair}\). Let \(\mathrm{Cats}=\bigotimes_l\mathrm{cat}_{\sigma_l}\). Telescoping the normalized factors bounds their vector distance by \(24r\) and unhalved density trace distance by \(48r\).

The fresh arbitrary logical program/path/reference state is supplied physically on ordinary \(Q\), the two input emitters in their one-excitation dual-rail code, and a passive reference. The normalized joint rest/environment state \(\omega\), including old \(P\) and a retained passive \(E\), is independent of that arbitrary input. Define

\[
\mathcal E_{\rm pair}=\operatorname{Tr}[(A_{\rm pair}-12e_{\rm pair}I)\omega],\qquad
q_{\rm blank}=\operatorname{Tr}[(I-P_{\rm blank})\omega].
\]

Here \(P_{\rm blank}\) requires all noninput original heads vacant and \(R=0\), excludes the two input emitters, and leaves \(P,E\) unrestricted. The selector excess uses the **exact** reference \(12e_{\rm pair}\); a truncated Taylor energy or the unperturbed cat expectation is not a substitute.

The ancillary gap bounds its joint ground-state failure by \(\mathcal E_{\rm pair}/g_{\rm pair}\). Its ground projector commutes with \(P_{\rm blank}\). When the summed bad-weight bound is below one, projection of a purification as a mathematical comparison gives some normalized retained state \(\sigma_{PE}\) and

\[
\begin{split}
&\left\|\omega-
 |\mathrm{blank},0_R\rangle\langle\mathrm{blank},0_R|
 \otimes|\mathrm{Cats}\rangle\langle\mathrm{Cats}|\otimes\sigma_{PE}\right\|_1\\
&\hspace{1cm}\le
2\sqrt{q_{\rm blank}+\mathcal E_{\rm pair}/g_{\rm pair}}+48r.
\end{split}
\]

This is one joint reference-safe state bound, not a sum of marginal fidelities. The square-root cost is retained even if an apparatus marginal is diagonal. Preparation-device outputs must be included in \(E\) or another declared retained factor. The proof does not physically project, reset, erase or discard them.

The exact selector ground's \(F=\sigma\) condition generally does **not** place it in the real operating gadget's transformed \(T_l=+1\) sector. The latter has Y factors on ancillas rotated by the parent's real gauge. The two conditions agree on the desired cat in the penalty-zero space, not on general excited components. The literal state-distance bound pays this initial discrepancy; the following full-space runtime comparison pays subsequent leakage. No hidden sector-invariance premise is used.

## Permanently installed pair terms and the physical phase

Let \(H_{\rm run}\) be the parent's real, unpenalized exponent-17 device. It already contains every square's \(H_0\). Add only the 24 pair-selector terms:

\[
H_{{\rm run},{\rm pair}}=H_{\rm run}+24hI
-h\sum_{\text{24 pairs}}s_{ij}X_iX_j.
\]

The nonconstant perturbation has full norm at most \(24h\). Full-unitary Duhamel, including every apparatus and passive reference, gives

\[
\|e^{-itH_{{\rm run},{\rm pair}}}
-e^{-i24ht}e^{-itH_{\rm run}}\|\le24h|t|.
\]

There is no duplicated \(H_0\), switched selector or assumption of F/T/head-number conservation by the running device. The exact new runtime identity scalar is \(24h\). The isolated selector reference \(12e_{\rm pair}\) is neither a runtime phase nor the ground energy of the interacting operating Hamiltonian.

In the parent's notation the complete comparison phase is exactly

\[
\exp\{-it[48\nu+s_{\rm joint}+\lambda\bar c+24h]\},
\quad s_{\rm joint}=-24\nu^2/\Delta+27\nu^4/\Delta^3,
\quad \bar c=8\bar b+8(\sqrt2-1)\bar j.
\]

The common radial profile is evaluated at \(\lambda t\), preserving \(-i\), the incoming translation \((\ell+57)k\), outgoing \(nq(k)\), Jacobian \(\sqrt{q'(k)}\), and positive final normalization. There is no extra record-bias, selector-ground or original-head-penalty phase. The same unnormalized finite profile is used for the record1 branch throughout the horizon.

## Simultaneous budgets and all outputs

For \(0<\epsilon\le1\), evaluate the parent's complete unpenalized prescription at \(\tau=\epsilon/8\) and gadget allowance \(\epsilon_g=\epsilon/16\), retaining its exact source policy, finite \(T,\ell\), scale \(\lambda\) and all coefficients. Set \(\Delta=\Lambda/4\) and choose exactly

\[
h=\min\left\{\frac{\Delta}{64},\quad
\frac{\Delta\epsilon}{384},\quad\frac{\epsilon}{384T}\right\}.
\]

Then \(48r\le\epsilon/8\) and \(24hT\le\epsilon/16\). The optional initial-state quality assumptions

\[
q_{\rm blank}\le\epsilon^2/512,\qquad
\mathcal E_{\rm pair}\le g_{\rm pair}\epsilon^2/512
\]

give a square-root projection cost at most \(\epsilon/8\) and total joint rest trace allowance \(\epsilon_{\rm rest}\le\epsilon/4\). The energy criterion certifies only the ancillary contribution; blank heads/record and the physical boundary input remain separate supplies. A directly supplied rest state satisfying the same trace allowance also suffices. Neither form is a preparation procedure.

On the final window \([3\ell/(4\lambda\bar j),T]\), the ideal-rest vector error is at most

\[
3\epsilon/64+\epsilon/16+\epsilon/16=11\epsilon/64.
\]

Adding the supplied rest-state error gives unhalved complete-channel distance at most \(19\epsilon/32\). For every \(0\le t\le T\), the ideal-rest **absolute unnormalized branch-comparison error** is

\[
\|P_{R=1}e^{-itH_{{\rm run},{\rm pair}}}E_{\rm in}-V_{\rm fin}(t)\|
\le3\epsilon/16,
\]

where \(E_{\rm in}\) appends the nominal blank/signed-cat rest and \(V_{\rm fin}(t)\) is the same unnormalized parent output map with the new common phase. This is an error between maps, not a bound on the record1 amplitude itself, which is near one on the final window. Both branch maps are contractions. Including the supplied rest state gives unhalved subnormalized complete-channel error at most \(5\epsilon/8\), with no division by a possibly rare flag probability. The final joint event of retained F output, record1, every other original head vacant and the signed-cat comparator has probability at least

\[
1-121\epsilon^2/4096-\epsilon/8.
\]

Every output remains in these comparisons: logical program on \(P\), controlled output path, all original heads and ancillary qubits, and old \(P/E\) information relocated intact to \(Q/E\) in the comparator. Passive input and preparation references are acted on by identity. Actual residual correlations and imperfect ancillary states stay in the full error. The window retains relative width \(1/6\); the theorem provides neither infinite retention nor capture, reset or permanent halt.

## Counts, energy scale and historical comparison

Each ancillary qubit belongs to exactly one new pair, adding incident norm \(2h\). Its full load is \(2\Delta+2\nu+2h<\Lambda\) under the parent's \(\alpha=\nu/\Delta\le1/(32\cdot48)\) and the displayed h bound. Other loads are unchanged. There are no new qubits and 24 added positive blocks, giving **\(175+4\ell\) qubits and \(289+4\ell\) listed blocks**. The selector edges have range one; the full device retains its supplied Manhattan range at most 35. Negative pair signs on the minus-cat squares preserve positivity. All coefficients and absent unwanted interactions remain supplied.

With the parent instantiated at the stated budgets, its T and length are not extended by adding the selectors. As \(\epsilon\to0\), the third h entry eventually controls, so

\[
\begin{aligned}
h&=\Theta(\Lambda\epsilon^{18}/\log^5(e/\epsilon)),\\
G_{\rm pair},\ g_{\rm pair}
&=\Theta(\Lambda\epsilon^{36}/\log^{10}(e/\epsilon)),\\
g_{\rm pair}\epsilon^2/512
&=\Theta(\Lambda\epsilon^{38}/\log^{10}(e/\epsilon)).
\end{aligned}
\]

These are sufficient-family and local energy-quality scales, not necessary temperatures, cooling times, optimal costs or achievable measurement-precision claims. Accurate subtraction of the exact \(12e_{\rm pair}\) from an expectation remains an unproved physical capability; rationalized algebra does not supply that experiment.

The earlier [onsite-selector construction](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_static_cat_selector/PROPOSAL.md) and its [review](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_static_cat_selector_check/REVIEW.md) remain historical comparison: four one-qubit fields per square, 48 added blocks, runtime scalar \(48h\), and sufficient excess allowance \(\Theta(\Lambda\epsilon^{74}/\log^{20}(e/\epsilon))\). Its [exact-energy supplement](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_selector_exact_energy/PROPOSAL.md) and [review](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_selector_exact_energy_check/REVIEW.md) give that different selector's exact subtraction. Their spectra, gaps and root formulas are not imported into the pair theorem. The joint-projector and runtime-budgeting pattern is reused explicitly and re-established in the pair source and its check, together with the new spectrum and constants.

## Limits and evidence

\(A_{\rm pair}\) is a separately analyzed ancillary observable. Its unique ground is not asserted to be the ground of the full running Hamiltonian, and small total operating energy is not the assumed local selector excess. The result supplies no product-to-cat evolution, cooling, thermalization, bath, measurement, entropy disposal, native coefficient source or state-preparation mechanism. Old head-gap, energy-to-blank and Gibbs certificates remain unavailable. Boundary encoding/loading, blankness, reference independence, exact real positive blocks, full-device range-35 couplings, observation/readout and absence of unwanted terms remain premises.

The source-exposure list pins the corrected pair argument, the [initial reviewed version](../outputs/common_product_pair_cat_selector_2026_10_18/common_product_pair_cat_selector/AUTHOR_PROPOSAL_V1.md), the actual review, the immediate canonical operation parent and exact necessary inherited interfaces. The correction makes the whole-horizon branch-comparison meaning explicit without changing formulas, premises or budgets. Historical onsite arguments/checks are marked separately from operative proof dependencies. The new pair construction is ROOT-authored; author and checker exposures must not be counted as independent lineage. This drafter authored the preceding operation manuscript and read its component arguments and bounded integration changes. No scientific executable or historical checker was rerun for this note.

The complete onsite draft is preserved separately as ONSITE_NOTE.md. The accompanying source-exposure record preserves the drafter's actual work and limits. ROOT's integration record and publication check document the separate manuscript review; no retained-status verdict is claimed.
