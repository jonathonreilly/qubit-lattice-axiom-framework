---
claim_id: detector_scattering_projection_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "For the stated selected outgoing scattering sector and narrow bounded Borel energy windows, a countable family of admissible positive detectors has support exactly the selected scattering projection. Ordered detector-time, family and resolvent limits recover it; a conditional finite-time response gives a one-sided lower witness. No full-GNS exhaustion, physical realization, effective enumeration or numerical witness constants are proved."
upstream_dependencies:
  - compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
  - compact_patch_fock_isometry_bounded_theorem_note_2026-10-12
  - compact_detector_convergence_bounded_theorem_note_2026-10-12
runner: scripts/detector_scattering_projection_2026_10_12.py
actual_current_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A countable detector resolution of the constructed scattering projection

**Claim type:** bounded theorem. **Status:** conditional-support. A separate complete P1–P33 reconstruction found no required mathematical correction. The compact detector convergence dependency PC also has a separate source-bound review. Root proposed the route and is a contributor, not an independent reviewer. No physical realization, retained audit status, no-common-kernel condition ND, or full-GNS exhaustion EX is asserted.

For the already constructed selected outgoing scattering space, one can choose a countable admissible detector family whose positive weighted sum has support exactly its energy-window projection. The choice exists by separability; an effective enumeration, a lower frame bound and a resolvent convergence rate are not proved. The projection is reconstructed by ordered strong limits of positive finite-time detector sums. The remaining kernel is exactly the complement of the selected scattering space in that energy window, and is not shown to vanish.

## 1. Source contract and scope

S denotes the original external research collection. The [complete projection milestone packet](../.claude/science/physics-loops/toe-detector-scattering-projection-20261012/) preserves the frozen argument, author evidence, separate review and exact reconstruction maps. Its EVIDENCE_MAP.json records external primary-source recovery without redistributing complete papers. The actual in-branch premises are the [compact-creator construction](COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md), [selected Fock isometry](COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md) and [detector convergence](COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md). Original source identities below remain unchanged. The author acquired sourcec3f84746b1991e0a15c6da79d049b89d9469f727; the reviewed E/PC publication advanced the branch to296155eda2ca6a5ab6ae6307190362b9a84ea690. Planning remains3a4b2c66a1ead7a1c48b4359627e968f681e3c39.

| Frozen source | SHA-256 | Exact role here |
|---|---|---|
| `COMPACT_PATCH_SCATTERING_COVARIANCE_PROBE.md` | `d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a` | Supplied microscopic setting S1–S4, direct almost-local creator class, compact separated packet limits |
| `COMPACT_PATCH_SCATTERING_EX_PUBLICATION_REPAIR.md` | `d4aac1e14a20e82be994bd4b8de966f0063affcbaa22a40a173b126f77fa3516` | Separate unique-vacuum/gap hypothesis; no exhaustion conclusion |
| `COMPACT_PATCH_FOCK_ISOMETRY_PROBE.md` | `9bc3a309e8fc35978bcac0c360b8557fb6a3c4484cfc2034a277a94072369404` | F5–F6: products depend only on one-particle vectors; selected Fock range and separated-product density; F17–F19: density justification |
| `COMPACT_PATCH_FOCK_ISOMETRY_REVIEW.md` | `bc88af1dda77065d8806da9d689546547f40847a340177086793dab5f3a277cf` | Separate source-bound review of that Fock result; does not assess this note |
| `COMPACT_DETECTOR_CONVERGENCE_PROBE.md` | `bed0584922876c64de1658f3135390420b703dd661edf5076e02a0a36af34d64` | Conditional C6–C10, C24a–C24, C28; only the direct filtered class and fixed-arrangement scope are used |
| `COMPACT_DETECTOR_CONVERGENCE_REVIEW.md` | `2f9ebfed745c217d97750ddc5f7a5edeaffaede72895ad0da1af0974ef2c51f0` | Separate review completed for unchanged C1–C28; full report read here, including its review of C24a and its limits |
| `SCATTERING_EXHAUSTION_NEXT_OBLIGATION.md` | `c4af4f5e9823e2cd1cfb79a0f17498fb2ffe117cb24c90bc572b888e31ae08c2` | Motivation for weighted sums/ND; every weighted-sum and resolvent assertion used here is proved anew |
| `ROOT_DETECTOR_SUPPORT_PROJECTION_LEAD.md` | `8ae35c637fd77aee6a68e7a120c36d7d5c4aba4c9fef6df8b594316369c5138f` | Conjectural research lead only, not evidence |

The existing creator and Fock sources and their relevant reviews were read fully in this continuing worker's earlier task. The present task reread the exact creator filtering, Fock well-definedness/density, and PC creation-map and detector-limit passages it uses. PC was provisional when this task began. Its separate review later completed for the unchanged source, with receipt SHA-256 `e9fb01e5d88618f1905a7426d07991e0a96e88cdd32a8d996b4caa92bd39db5d`. The full report was read and its identities checked here. This author has not performed an independent reconstruction of its own PC proof or rechecked the reviewer's full reconstruction/control packet. The new theorem has now received its own complete independent reconstruction; the exact report and limits are appended below. Neither the separate E1–E18 review verdict nor an unreviewed root suggestion substitutes for a premise.

The closest primary comparison is Dybalski–Gérard, [*A criterion for asymptotic completeness in local relativistic QFT*, arXiv:1308.5187v1](https://arxiv.org/abs/1308.5187v1), Theorem 2.9 and its full §7 proof. Complete PDF page texts 6–9 and 20–22 were read in this task. They identify a detector-range span with a selected scattering sector under their relativistic/global-shell assumptions. Their Lemma 7.5 refers its proof elsewhere; that lemma and those assumptions are **not** imported here. The argument below instead uses the supplied direct creators, the explicit PC limit, and a new finite refinement argument with total-energy compression. No novelty claim is made for the general detector-span or positive-operator support mechanism. The primary PDF and exact page-text hashes, read limits, and official metadata lookup are recorded in the evidence ledger.

Assume the same supplied microscopic Hamiltonian/current implementations, isolated positive mass components and selected finite-order centres as the compact sources. In particular,
\[
H\ge0,\qquad \ker H=\mathbb C\Omega,\qquad
\operatorname{spec}H\subset\{0\}\cup[\gamma,\infty),\quad\gamma>0,
\quad \alpha_t=\operatorname{Ad}e^{itH},\quad T_x=e^{-ix\cdot Q}. \tag{P1}
\]
Fix the finite set of selected mass/centre components in F2, and let
\(\mathcal H_{\rm sc}=\operatorname{Ran}W^+\), with orthogonal projection \(P_{\rm sc}\).
This is exactly the existing Fock scattering space over those components, including the vacuum. It is a closed reducing subspace for H. No extra component is added. Equivalently it is the closed span of the vacuum and the existing finite, internally velocity-separated compact packet products. We use this latter generating description below.

The same proof applies to a specifically declared closed span of such constructed products from a larger chosen collection if the finite-family creator-independence and covariance premises hold for that collection. It does not establish those premises for unspecified channels. The main theorem concerns the fixed F2 selection.

For a bounded nonempty Borel set \(J\subset[\gamma,\infty)\), write
\[
P_J=\mathbf1_J(H),\qquad d_J=\operatorname{diam}J<\gamma/4,
\qquad J_{\rm h}=[\inf J,\sup J]. \tag{P2}
\]
Here \(J_{\rm h}\) is the closed interval hull. We will only use its diameter and the inclusion \(J\subset J_{\rm h}\). The empty-window assertion is zero and needs no detectors. The proof includes singleton windows and either choice of interval endpoints; it assumes no energy boundary has measure zero.

The conditional PC input has this precise content. For every fixed tuple of direct creators \(B_i\), their positive compact temporal operator intervals \(I_i\), compact full geometric operator transfer supports \(\Lambda_i\) inside single species/centre/lift charts, and nonnegative smooth compact velocity cutoffs with disjoint convex support hulls containing \(v_i(\Lambda_i)\), put
\[
\begin{split}
\mathscr K_\alpha&=\ell^2(\mathbb Z^{dn}),\qquad
\omega_\alpha(D)=\sum_i\Sigma_i(D_i),\qquad
\mathsf h_{\alpha,t}(\mathbf x)=\prod_i h_i(x_i/t),\\
J_{\alpha,t}f&=\sum_{\mathbf x}f(\mathbf x)
B_n(t,x_n)\cdots B_1(t,x_1)\Omega,\qquad
S_\alpha=\operatorname{s-lim}_{t\to\infty}J_{\alpha,t}e^{-it\omega_\alpha(D)}.
\end{split} \tag{P3}
\]
Each dispersion has its own smooth torus extension, agreeing with its physical chart near its carrier. PC gives bounded \(J_{\alpha,t}\) and \(S_\alpha\), with
\[
S_\alpha=S_\alpha P_{\Lambda_\alpha},\quad
e^{iaH}S_\alpha=S_\alpha e^{ia\omega_\alpha(D)},\quad
\operatorname{Ran}S_\alpha\subset\mathcal H_{\rm sc},\qquad
\Lambda_\alpha=\prod_i\Lambda_i. \tag{P4}
\]
The range assertion follows from the dense smooth tensor domain and the closed scattering space. If
\((J_{\rm h}-\sum_iI_i)\cap\operatorname{spec}H\subset\{0\}\), the positive compressed detectors obey
\[
Q_\alpha(t):=P_JJ_{\alpha,t}\mathsf h_{\alpha,t}J_{\alpha,t}^*P_J
\xrightarrow[t\to\infty]{\rm strong}
Q_\alpha=P_JS_\alpha\mathsf h_\alpha(v(D))S_\alpha^*P_J. \tag{P5}
\]
For Borel J, this follows from the interval version at \(J_{\rm h}\) by compression with \(P_J\); no boundary approximation is necessary. A degenerate hull can instead be enlarged slightly in the strict gap margin obtained below, if the interval convention excludes a singleton. With \(0\le h_i\le1\), PC supplies a finite constant \(B_\alpha\) such that \(0\le Q_\alpha(t)\le B_\alpha P_J\) for all \(t\ge1\), and the same bound holds for \(Q_\alpha\). This is a fixed-arrangement bound, with no uniformity in the number or widths of the arrangements.

## 2. Exact finite refinement of a separated packet product

Take one of the existing generating products
\[
\Psi=\Psi^+(\psi_1,\ldots,\psi_n),\qquad
\psi_i=\widehat f_i(Q)B_i^0\Omega,\quad
\widehat f_i\in C_c^\infty(O_i). \tag{P6}
\]
The compact sets \(K_i=\operatorname{supp}\widehat f_i\) lie strictly inside their geometric-momentum charts, each with its fixed species/centre/continuous-momentum lift. Zero amplitudes or zero resulting products can be omitted. Their velocity images \(V_i=v_i(K_i)\) are pairwise disjoint. For \(n\ge2\), let \(\delta=\min_{i\ne j}\operatorname{dist}(V_i,V_j)>0\) and put \(r=\delta/10\). For \(n=1\), choose any \(r>0\); there is no separation condition to check.

Choose positive temporal halfwidths \(r_i\) with
\[
\sum_i r_i\le\gamma/8,\qquad
r_i<\tfrac14\min_{p\in K_i}\Sigma_i(p). \tag{P7}
\]
Such choices exist for every fixed finite product because the compact mass dispersions are strictly positive. For each \(p\in K_i\), continuity supplies an open neighborhood \(U_{i,p}\Subset O_i\) with
\[
v_i(U_{i,p})\subset B(v_i(p),r),\qquad
|\Sigma_i(p')-\Sigma_i(p)|<r_i/3\quad(p'\in U_{i,p}). \tag{P8}
\]
Choose a finite subcover and a smooth partition \(\chi_{i,a}\) subordinate to it, compactly supported in the corresponding neighborhoods, whose sum equals one on a neighborhood of \(K_i\). Put
\(\widehat f_{i,a}=\chi_{i,a}\widehat f_i\),
\(K_{i,a}=\operatorname{supp}\widehat f_{i,a}\), and discard zero amplitudes. Each \(K_{i,a}\) is compactly contained in its chosen \(U_{i,a}\); the sum of these amplitudes equals \(\widehat f_i\) exactly. The partition functions may overlap. Distinct factors i, rather than pieces of the same factor, need separated velocities.

Let \(p_{i,a}\in K_i\) be the center used to choose \(U_{i,a}\), let \(e_{i,a}=\Sigma_i(p_{i,a})\), and set
\[
I_{i,a}=[e_{i,a}-r_i,e_{i,a}+r_i]\Subset(0,\infty).
\]
Choose real smooth multipliers \(0\le\zeta_{i,a},\phi_{i,a}\le1\) such that
\[
\begin{split}
&\zeta_{i,a}=1\text{ near }\Sigma_i(K_{i,a}),\quad
\operatorname{supp}\zeta_{i,a}\subset(e_{i,a}-r_i,e_{i,a}+r_i),\\
&\phi_{i,a}=1\text{ near }K_{i,a},\quad
\Lambda_{i,a}:=\operatorname{supp}\phi_{i,a}\Subset U_{i,a}.
\end{split} \tag{P9}
\]
The margins in (P8) guarantee these choices. Define the **operator** refiltering
\[
\begin{split}
k_\zeta(s)&=(2\pi)^{-1}\int e^{-iEs}\zeta(E)\,dE,
\qquad c_\phi(z)=\int_{\mathbb T^d}e^{ip\cdot z}\phi(p)\,\frac{dp}{(2\pi)^d},\\
B_{i,a}&=\sum_{z\in\mathbb Z^d}c_{\phi_{i,a}}(z)
\tau_z\left(\int_{\mathbb R}k_{\zeta_{i,a}}(s)\alpha_s(B_i^0)\,ds\right).
\end{split} \tag{P10}
\]
Both kernels are Schwartz; the sums and integrals converge in norm. The commuting translation flows permit either order of the two filters. The Fourier signs in (P10) and \(T_z=e^{-izQ}\) give
\[
B_{i,a}\Omega=\phi_{i,a}(Q)\zeta_{i,a}(H)B_i^0\Omega,
\qquad
\widehat f_{i,a}(Q)B_{i,a}\Omega
=\widehat f_{i,a}(Q)B_i^0\Omega=:\psi_{i,a}. \tag{P11}
\]
The last equality uses the exact vacuum graph on the original chart and both multipliers being one near the packet support. This is equality of one-particle vectors, not of the underlying operators.

All the PC creator properties survive this operation. Fourier multiplication bounds the **full operator** temporal transfer by \(I_{i,a}\) and geometric transfer by \(\Lambda_{i,a}\), also if the original operator transfer was much larger. The vacuum graph, species, centre and lift are preserved. No separation of the selected graph from the full geometric spectrum is asserted.

Here is the almost-locality point for the temporal filter on an already almost-local seed. At a large target radius R, approximate \(B_i^0\) by a norm-bounded local operator on radius R/4 with error \(O(R^{-N})\) for every N. For \(|s|\le cR\), with fixed c smaller than the inverse Lieb–Robinson velocity scale, evolve that approximant and take a conditional expectation onto radius R. The LR error is a polynomial in R times \(e^{-c'R}\); evolution of the initial approximation error has its unchanged norm. Integrating over this region costs only the fixed \(L^1\) norm of \(k_\zeta\). The remaining times have norm contribution at most \(2\|B_i^0\|\int_{|s|>cR}|k_\zeta(s)|ds=O(R^{-N})\). Thus the filter is almost local. Every norm time derivative is obtained by replacing the kernel with \((-\partial_s)^a k_\zeta\), again Schwartz, so the same argument applies. This uses the supplied finite-range H dynamics. It does not integrate an exponential LR prefactor over the entire Schwartz tail. Splitting the spatial sum at \(|z|\le R/2\) and using its Schwartz tail proves almost locality of the spatial filter and its time derivatives as well.

Finite multilinearity and (P11), followed by the Fock creator-independence identity, give the exact finite decomposition
\[
\Psi=\sum_{\mathbf a}\Psi^+(\psi_{1,a_1},\ldots,\psi_{n,a_n}). \tag{P12}
\]
For clarity: multilinearity first decomposes the original packet amplitudes; for each term the new creators have the same one-particle vectors as the old ones. The F5 Gram identity makes the difference of the two scattering realizations have norm zero. The new direct creators satisfy all hypotheses used for that identity. No approximation, change in normalization, or factorization of a total-energy projection occurs in (P12).

For each tuple \(\mathbf a\), let \(c_i=v_i(p_{i,a_i})\). These centers from different i are at least \(\delta\) apart. Choose \(h_i\in C_c^\infty(\mathbb R^d)\), \(0\le h_i\le1\), equal to one on a neighborhood of \(v_i(\Lambda_{i,a_i})\subset B(c_i,r)\), and supported in \(B(c_i,2r)\). Their convex support hulls are disjoint, since \(4r<\delta\). They and a small velocity enlargement of each carrier lie in the disjoint closed balls of radius \(3r\), since \(6r<\delta\). Smooth carrier cutoffs equal to one near \(\Lambda_{i,a_i}\), as required in the PC proof, exist inside the same chart neighborhoods. Thus the convex condition, its positive separation margin, and the full operator carrier condition all hold. For \(n=1\), a single such ball suffices. The argument never requires the convex hulls of the original, possibly disconnected velocity supports to be disjoint.

Let \(f_{\mathbf a}\in\mathscr K_\alpha\) have Fourier transform \(\prod_i\widehat f_{i,a_i}(p_i)\), where \(\alpha\) denotes this complete refiltered arrangement. By (P3), packet permutation invariance and the direct Cook construction,
\[
\Psi^+(\psi_{1,a_1},\ldots,\psi_{n,a_n})=S_\alpha f_{\mathbf a}.
\tag{P13}
\]
In particular every term is an actual range vector of a bounded creation map, and every carrier velocity has detector weight exactly one.

## 3. Total-energy support and the vacuum remainder

Put \(E_{i,a_i}=\Sigma_i(K_{i,a_i})\), a compact subset of the interior of \(I_{i,a_i}\). The covariance in (P4) implies, by the spectral theorem,
\[
P_JS_\alpha f_{\mathbf a}
=S_\alpha\mathbf1_J(\omega_\alpha(D))f_{\mathbf a}. \tag{P14}
\]
One can derive this bounded intertwiner identity first for Fourier transforms of integrable time functions, then for spectral projections by bounded Borel functional calculus. It acts on the **sum** \(\omega_\alpha=\sum_i\Sigma_i\), with the same common time on the whole product. The auxiliary product vector has spectral support in \(E_{1,a_1}+\cdots+E_{n,a_n}\). Hence a term with
\(J\cap(E_{1,a_1}+\cdots+E_{n,a_n})=\varnothing\)
has zero total-energy projection and can be discarded exactly.

For every remaining tuple choose
\(e_*\in J\cap(E_{1,a_1}+\cdots+E_{n,a_n})\).
There are \(e_i'\in E_{i,a_i}\subset I_{i,a_i}\) with \(e_*\!=\sum_i e_i'\). For any \(x\in J_{\rm h}\) and \(y_i\in I_{i,a_i}\),
\[
\left|x-\sum_i y_i\right|
\le |x-e_*|+\sum_i|e_i'-y_i|
\le d_J+2\sum_i r_i<\gamma/2. \tag{P15}
\]
Consequently
\[
J_{\rm h}-\sum_iI_{i,a_i}\subset(-\gamma/2,\gamma/2),
\qquad
(J_{\rm h}-\sum_iI_{i,a_i})\cap\operatorname{spec}H\subset\{0\}. \tag{P16}
\]
This strict margin also covers closed transfer supports, the closed hull of an open or half-open window, and any sufficiently small enlargement of a singleton hull. The selection criterion may retain a tuple whose projected vector happens to be zero; that is harmless. It discards none with nonzero projection. It does not require \(\sum_iI_i\subset J\), which would generally fail at a boundary.

We have proved the essential coverage statement:
\[
P_J\mathcal H_{\rm sc}
=\overline{\operatorname{span}}
\{P_JS_\alpha f:\alpha\text{ as constructed above},\ f\in\mathscr K_\alpha\}.
\tag{P17}
\]
The inclusion from right to left follows from (P4) and reduction of \(\mathcal H_{\rm sc}\) by H. For the converse, apply the contraction \(P_J\) to the dense span of the existing separated scattering products, use the exact decomposition (P12), (P13), and discard precisely the terms justified by (P14). The vacuum has zero projection since \(J\subset[\gamma,\infty)\). The target \(P_J\mathcal H_{\rm sc}\) is closed because the two orthogonal projections commute. This uses density only inside the already constructed scattering space.

For every arrangement in (P17), \(\mathsf h_\alpha(v(D))=1\) on \(\Lambda_\alpha\). Hence (P4), (P5) give
\[
Q_\alpha=P_JS_\alpha S_\alpha^*P_J=A_\alpha A_\alpha^*,
\qquad A_\alpha:=P_JS_\alpha. \tag{P18}
\]
The identity follows by multiplication with \(P_{\Lambda_\alpha}\), not by commuting a momentum filter through a finite-time spatial cutoff. In particular
\(\ker Q_\alpha=\ker A_\alpha^*\) and
\(\overline{\operatorname{Ran}Q_\alpha}=\overline{\operatorname{Ran}A_\alpha}\), since both closed ranges are the orthogonal complement of \(\ker A_\alpha^*\). No individual detector is asserted to be a projection or a lower-bounded frame operator.

The finite-time operators in (P5) have an explicit positive form without using \(P_{\rm sc}\). With \(A_i(t,x)=B_i(t,x)^*\), let \(D_{\alpha,\mathbf x}(t)=A_1(t,x_1)\cdots A_n(t,x_n)\). Temporal transfer and (P16) give
\(D_{\alpha,\mathbf x}(t)P_J=P_0D_{\alpha,\mathbf x}(t)P_J\), where \(P_0=|\Omega\rangle\langle\Omega|\). Therefore, exactly,
\[
Q_\alpha(t)=P_J\sum_{\mathbf x}\mathsf h_{\alpha,t}(\mathbf x)
D_{\alpha,\mathbf x}(t)^*D_{\alpha,\mathbf x}(t)P_J\ge0. \tag{P19}
\]
The sum is finite at each t. It is a total-energy compression of finite sums of almost-local operator products. It contains no scattering projection. The ordered product of separate one-particle detectors need not be positive at finite time; (P19) is the positive coincidence expression used for the resolvents. PC's commutator reordering shows that the compressed separate-detector product differs from it by \(O(t^{-N})\) in norm for each N and each fixed arrangement. We do not need that asymptotic replacement to prove positivity.

One available bound is the PC bound \(B_\alpha=M_{L_\alpha}^2\), where
\[
L_\alpha=\sum_i\sup I_i,\quad
M_R=\prod_i\left(\left\lfloor R/\inf I_i\right\rfloor
\sum_z\|[B_i^*,\tau_z(B_i)]\|\right)^{1/2}. \tag{P20}
\]
Almost locality and the strictly positive lower transfer edges make it finite. PC C3–C6 prove the common-word lowering estimate giving this bound; this note does not assume an unbounded product estimate. A larger finite bound is equally suitable.

## 4. Countable selection and the exact support of a positive sum

The local finite-dimensional site algebras on the countable lattice have a countable norm-dense union of rational finite matrix combinations. Their quasilocal completion is separable. Cyclicity of \(\Omega\) implies that \(\mathcal H\), hence its closed subspace \(T_J:=P_J\mathcal H_{\rm sc}\), is separable.

Choose a countable dense set \(u_k\) in \(T_J\). For every pair \((k,l)\), (P17) supplies a finite linear combination of vectors \(A_\alpha f\) within \(2^{-l}\) of \(u_k\). Collect all arrangements occurring in those combinations. This is a countable family, and its range vectors still have dense linear span in \(T_J\). If the target is zero the family may be empty; finite families are allowed. Relabel its members by a subset of the positive integers, and take missing terms to be zero when writing sums. This selection is an existence proof. It is not an algorithm for finding the family, a claim about an arbitrary family, or an enumeration of all physical channels.

For this **chosen** family and its actual individual bounds, set
\[
w_\alpha=\frac{2^{-\alpha}}{1+B_\alpha}>0,\qquad
K_{J,m}(t)=\sum_{\alpha\le m}w_\alpha Q_\alpha(t),\quad
K_{J,m}=\sum_{\alpha\le m}w_\alpha Q_\alpha,\quad
K_J=\sum_\alpha w_\alpha Q_\alpha. \tag{P21}
\]
The last series converges in operator norm. Positivity gives
\[
0\le K_J\le P_J,\qquad
\|K_J-K_{J,m}\|\le\sum_{\alpha>m}2^{-\alpha}=2^{-m}. \tag{P22}
\]
The same bound holds for tails of the finite-time series if one chooses to form it. Only the finite sums are needed below. At fixed m, \(K_{J,m}(t)\to K_{J,m}\) strongly by (P5); they are uniformly positive contractions supported in \(P_J\mathcal H\).

For any \(\psi\in\mathcal H\), norm convergence and positivity permit the identity
\[
\langle\psi,K_J\psi\rangle
=\sum_\alpha w_\alpha\|S_\alpha^*P_J\psi\|^2.
\tag{P23}
\]
It vanishes exactly when every \(A_\alpha^*\psi=0\). By the chosen range density this is exactly \(\psi\perp T_J\). Since a positive operator has zero quadratic form exactly on its kernel,
\[
\boxed{\quad
\ker K_J=T_J^\perp,\qquad
\overline{\operatorname{Ran}K_J}=T_J,\qquad
\mathbf1_{(0,\infty)}(K_J)=P_JP_{\rm sc}.
\quad} \tag{P24}
\]
In particular,
\[
\ker(K_J|_{P_J\mathcal H})=P_J\mathcal H\cap\mathcal H_{\rm sc}^{\perp}.
\tag{P25}
\]
All three parts of (P24) are exact. The first uses positivity of every summand, not cancellation in a signed sum. The second uses self-adjointness: the closure of the range is the orthogonal complement of the kernel. Each \(S_\alpha S_\alpha^*\), and hence \(K_J\), commutes with H by (P4). No positive lower spectral bound on \(T_J\) follows.

## 5. Ordered finite-time, truncation and resolvent limits

For a bounded positive operator A and \(\eta>0\), define
\(F_\eta(A)=A(A+\eta1)^{-1}=1-\eta(A+\eta1)^{-1}\).
For positive A and B the resolvent identity, retaining its order, gives
\[
F_\eta(A)-F_\eta(B)
=\eta(A+\eta1)^{-1}(A-B)(B+\eta1)^{-1},\qquad
\|F_\eta(A)-F_\eta(B)\|\le\eta^{-1}\|A-B\|. \tag{P26}
\]
It also proves strong continuity on a strongly convergent family of bounded positive operators: apply \((A_t-A)\) to the fixed vector \((A+\eta1)^{-1}\psi\), and bound the other resolvent by \(\eta^{-1}\). Thus, for each fixed m and \(\eta>0\),
\[
F_\eta(K_{J,m}(t))P_J\xrightarrow[t\to\infty]{\rm strong}
F_\eta(K_{J,m})P_J,
\quad
\|[F_\eta(K_J)-F_\eta(K_{J,m})]P_J\|
\le 2^{-m}/\eta. \tag{P27}
\]
Finally \(\lambda/(\lambda+\eta)\) tends to \(\mathbf1_{(0,\infty)}(\lambda)\), is bounded by one on the nonnegative axis, and is zero at \(\lambda=0\). The spectral theorem and dominated convergence give
\[
\boxed{\quad
P_JP_{\rm sc}
=\operatorname{s-lim}_{\eta\downarrow0}\,
\operatorname{s-lim}_{m\to\infty}\,
\operatorname{s-lim}_{t\to\infty}
K_{J,m}(t)(K_{J,m}(t)+\eta1)^{-1}P_J.
\quad} \tag{P28}
\]
The m-limit at fixed \(\eta\) is actually an operator-norm limit after the t-limit. No convergence rate as \(t\to\infty\) uniform in m, uniform rate as \(\eta\downarrow0\), or uncontrolled joint finite-time limit is inferred. Choosing a diagonal sequence would require choices adapted to a specified dense set and tolerances; (P28) makes no such effective construction claim.

To recover the full selected scattering projection, choose for example the disjoint half-open windows
\(J_j=[\gamma+j\gamma/8,\gamma+(j+1)\gamma/8)\), \(j=0,1,\ldots\).
Their diameter is \(\gamma/8\), they cover \([\gamma,\infty)\), and (P1) gives
\[
P_{\rm sc}=P_0+\operatorname{s-lim}_{N\to\infty}
\sum_{j=0}^{N}P_{J_j}P_{\rm sc}. \tag{P29}
\]
Replace each summand by its ordered expression (P28), with those inner limits taken for each fixed finite collection of windows before the final N-limit. Orthogonality of the energy windows proves the last strong convergence. The vacuum term is known from (P1). No all-channel completeness is inserted into this formula.

The complement has the equally exact formula
\[
\operatorname{s-lim}_{\eta\downarrow0}
\eta(K_J+\eta1)^{-1}P_J=P_J(1-P_{\rm sc}). \tag{P30}
\]
For a countable local cyclic set \(A_r\Omega\), vanishing of the left side on every \(P_JA_r\Omega\) is therefore equivalent to \(P_J\le P_{\rm sc}\). Boundedness of the projections and density justify the converse from that cyclic set to all vectors. This is the precise ND/energy-capture test for the chosen family. This note proves the identity, not its vanishing. Other necessary particle components, physical realization and full-GNS EX remain separate obligations.

There is also a conditional finite-time lower witness, using the stronger remainder bound PC C24a. Fix one arrangement, set \(E=P_J(1-P_{\rm sc})\), and choose a finite R with \(P_J\le\mathbf1_{[0,R]}(H)\). This E is an orthogonal projection and commutes with H. Since \(S_\alpha^*E=0\), C24a and \(\sup_t\|S_{\alpha,t}\|\le M_{L_\alpha}\) give, for every N, a finite constant \(C_{\alpha,N,J}\) with
\[
\|Q_\alpha(t)E\|\le C_{\alpha,N,J}t^{-N}\qquad(t\ge1).
\tag{P31}
\]
Indeed PC gives \(\|u_t(E\psi)\|\le c_{\alpha,N,R}t^{-N}\|E\psi\|\), and the exact identity \(Q_\alpha(t)E\psi=P_JS_{\alpha,t}u_t(E\psi)\) permits \(C_{\alpha,N,J}=M_{L_\alpha}c_{\alpha,N,R}\). Positivity, followed by compression with E, now gives the operator-norm estimate
\[
\|Q_\alpha(t)^{1/2}E\|^2
=\|E Q_\alpha(t)E\|\le\|Q_\alpha(t)E\|
\le C_{\alpha,N,J}t^{-N}. \tag{P32}
\]
For \(\psi\in P_J\mathcal H\), split \(\psi=P_{\rm sc}\psi+E\psi\) and apply the triangle inequality after \(Q_\alpha(t)^{1/2}\). If \(B_\alpha>0\), this proves
\[
\boxed{\quad
\|P_{\rm sc}\psi\|
\ge\frac{\max\{0,\sqrt{\langle\psi,Q_\alpha(t)\psi\rangle}
-\sqrt{C_{\alpha,N,J}}\,t^{-N/2}\|\psi\|\}}{\sqrt{B_\alpha}}.
\quad} \tag{P33}
\]
The sharper intermediate error contains \(\|E\psi\|\); replacing it by \(\|\psi\|\) makes the displayed witness usable without the unknown projection. If \(B_\alpha=0\), that detector is zero and supplies no witness. Formula (P33) becomes a quantitative lower bound only after the arrangement's source seminorms and constants have been controlled. Their existence does not supply numerical or effective values. A zero finite-time response proves no vanishing of the scattering component and cannot certify an undetected sector. This consequence uses exactly the same conditional PC remainder estimate.

## 6. Failed shortcuts and discriminating checks

The refinements above resolve specific proof obstacles; the following shortcuts remain invalid.

1. **Factoring a total-energy projection.** Two factors with energies 1 and 2 have pair energies 2, 3 and 4. The sum-energy projection on \(J=\{3\}\) selects the two crossed basis vectors. Its coefficient mask \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) has rank two and cannot be a product of one-factor indicator masks. All uses of \(P_J\) above are on the whole product.
2. **Narrow packet support without operator refiltering.** A vacuum vector near energy 1 need not force its creator's temporal operator transfer near 1. With \(\gamma=1\), \(J=[2,21/10]\), and two still-broad intervals \([1/10,3]\), the difference contains energy 1, so the vacuum remainder does not follow. The filters (P10), not a statement about vacuum support alone, reduce both full operator transfers.
3. **Separated sets with overlapping convex hulls.** In one velocity dimension, \(\{-2,2\}\) and \(\{0\}\) are disjoint, but the first convex hull contains the second. The finite small-ball partition is necessary for this PC route. It preserves the entire product by finite multilinearity.
4. **An arbitrary detector family covers the scattering range.** A single rank-one detector on one axis of a two-dimensional selected scattering space misses its other axis. The countable selection explicitly uses (P17); positivity alone does not supply it.
5. **Support equality implies a lower frame bound or norm convergence rate.** On \(\ell^2(\mathbb N)\), let \(Q_\alpha=|e_\alpha\rangle\langle e_\alpha|\), \(B_\alpha=1\). Then \(K=\operatorname{diag}(2^{-\alpha-1})\) has support 1, but \(\|F_\eta(K)-1\|=1\) for every \(\eta>0\). Strong convergence has no uniform unit-ball rate. Finite controls cannot establish or refute the infinite-dimensional analytic limit.
6. **An uncontrolled joint finite-time/resolvent limit.** Even \(K(t)=\operatorname{diag}(1,e^{-t})\to\operatorname{diag}(1,0)=K\) has a rapidly vanishing response on the complement of \(\operatorname{supp}K\), while \(\eta(t)=e^{-2t}\) gives \(F_{\eta(t)}(K(t))\to1\), the wrong projection. The bound \(2^{-m}/\eta\) alone also deteriorates as \(\eta\downarrow0\), and a fixed finite m in the preceding infinite diagonal example sees only its first m coordinates. The theorem asserts its displayed controlled order; it does not claim that every other iterated order fails. In fact, after the detector time limits have been taken, positivity gives increasing supports for the finite sums. Finite-time positivity itself requires (P19), not a potentially nonselfadjoint product of separate detectors.

The first, second, third and fourth examples are elementary algebraic counterexamples to the named steps. The fifth is an abstract Hilbert-space operator example. None is a countermodel to the supplied local-UHF microscopic setting or a no-go theorem for physical completeness.

Six author controls ran once under a declared 60-second timeout, exited 0 in about 0.035 seconds, and retained all seven stdout records and empty stderr in `detector_scattering_projection/`. Their finite targets are the nonfactorizing energy mask (all 16 independent binary factorizations rejected), strict interval-margin arithmetic (216 exact endpoint/singleton cases), operator refiltering and exact finite partitions, positive-sum common kernels with nonorthogonal generators, the noncommuting resolvent identity, and the square-root lower witness (588 toy-matrix cases). Intentional wrong algebraic steps are rejected at their stated finite scope. These checks cannot certify the analytic PC premise, all-scale almost locality, Hilbert-space density, physical hypotheses or independence. The proof, its exact sources and a fresh independent reconstruction carry those obligations.

Frozen author operational record: only this note and `detector_scattering_projection/` were written for the author task. The earlier PC note and packet remain frozen. The initial stream disconnect and an unsuccessful source-directory lookup are preserved in the operational record; unavailable platform failure details are not invented. The single recovery checkpoint, source ledger, complete controls, source identities and freeze receipt are in that directory. Editable prompt files changed: none. No repository, Git, PR, audit, axiom, model, other-chat or subagent action was taken. The fixed campaign deadline remains 2026-10-12 16:00:52 UTC.


## Publication evidence and remaining scope

The complete separate report has SHA256
`d9ab71d88615c78cb49eda7cc85ff263d65c12be6cc6e019314cd96eb42a20a2`,
with receipt`1fed9654096e0c67535640f60c1f1c318ac313c1436d84a21c4544b744f6ce3b`.
The full reconstruction and distinct exact-rational control were frozen before
new author evidence, at01:55:53UTC, record
`76c3d7adfc4cfa8d5c77f427aa35f8aaf1615b08e537103b9f6677eb985f895a`.
No required proof correction was found. Root read the complete source,
reconstruction and control evidence and is a coauthor, not a second independent
reviewer. Neither same-family context separation nor source hashes establish
independence of shared physical premises.

The [finite projection control](../scripts/detector_scattering_projection_2026_10_12.py) preserves the entire
original helper. Its rank-one witness sweep does not distinguish every invalid
universal error formula: a linear-error substitution passes that toy family.
This limitation and its complete passing output are preserved. The separately
checked scalar case Q=(1/16)E gives zero true selected component and a false
lower witness3/4 under the linear-error formula. The primary includes that
explicit exact scalar discriminator. P32 supplies the actual universal
square-root proof; neither toy family establishes analytic propagation.

PUBLICATION_EDITS.json and reconstruct.py recover the complete note and primary
from frozen bytes and explicit metadata/evidence additions. DELIVERY_CHECKS.md
records canonical execution, actual whole-primary defects and the outstanding
independent audit gates. No Lean certificate, physical realization, effective
enumeration, numerical witness constants, ND, EX or retained status is claimed.
The live campaign checkpoint remains toe-dynamics-bridge-20261009 in the
transport worktree; this packet is a frozen milestone snapshot.
