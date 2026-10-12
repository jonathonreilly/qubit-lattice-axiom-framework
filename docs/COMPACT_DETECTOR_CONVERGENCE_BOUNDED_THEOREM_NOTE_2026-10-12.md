---
claim_id: compact_detector_convergence_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "For each fixed admissible arrangement of supplied direct compact creators with separated convex velocity regions, the scalar detector amplitude converges in norm on every finite-energy vector. With the exact vacuum remainder and unique vacuum, positive detector operators converge strongly with range in the constructed scattering space. No common-kernel triviality, exhaustion or physical realization follows."
upstream_dependencies:
  - compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
runner: scripts/compact_detector_convergence_2026_10_12.py
actual_current_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem


# Compact detector convergence from a reversed scalar Cook integral

**Claim type:** bounded_theorem

**Status:** conditional-support; complete separate C1–C28 reconstruction found no required correction. **Trace:** closure of the fixed-arrangement detector convergence obligation (PC) in `SCATTERING_EXHAUSTION_NEXT_OBLIGATION.md`. The proof below reconstructs every preliminary E-claim it uses; it does not assume the outcome of that note's separate review. No full-GNS exhaustion, no-common-kernel estimate (ND), all-channel coverage, or physical realization is inferred.

For each fixed family of the supplied direct compact creators, with disjoint convex detector velocity regions containing the creator velocities, the precise PC norm limit exists. The limit is computed in (C24). With the additional energy-only vacuum remainder, the positive detector operators converge strongly, and their range is in the constructed scattering space. Neither Fock isometry nor strong convergence of the unlocalized adjoints is a premise.

The mechanism is Dybalski's fixed-time compactness and reversed Cook integral. On the lattice the fixed-time spatial cutoff has finite rank. A direct two-time Fourier-kernel estimate supplies the needed propagation bound, avoiding the primary paper's monomial expansion and Weyl-calculus steps. This is a proof-level adaptation of that mechanism, not a claim of a new general scattering principle.

## 1. Source contract and precise hypotheses

S denotes the original research collection, preserved through the [complete detector milestone packet](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/3faf1cf7167d8f9ef78ed84f50e9f3ebb277a9fe/.claude/science/physics-loops/toe-compact-detector-convergence-20261012/). EVIDENCE_MAP.json binds the complete original proof, source ledgers, author evidence and separate review. The in-branch [compact-creator theorem](COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md) supplies the direct creator construction. This note rederives the preliminary reductions it needs; the sibling exhaustion-reduction note states the downstream conditional criterion. Full third-party papers and page extractions remain external at their recorded identities.

| Source | Frozen SHA-256 | Role |
|---|---|---|
| `SCATTERING_EXHAUSTION_NEXT_OBLIGATION.md` | `c4af4f5e9823e2cd1cfb79a0f17498fb2ffe117cb24c90bc572b888e31ae08c2` | Exact PC target and downstream distinction from ND; used reductions rebuilt below |
| `COMPACT_PATCH_SCATTERING_COVARIANCE_PROBE.md` | `d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a` | Direct creator class, microscopic supplied conditions, packet Cook limits |
| `COMPACT_PATCH_SCATTERING_EX_PUBLICATION_REPAIR.md` | `d4aac1e14a20e82be994bd4b8de966f0063affcbaa22a40a173b126f77fa3516` | Separate unique-vacuum/gap setting for EX |
| `COMPACT_PATCH_FOCK_ISOMETRY_PROBE.md` | `9bc3a309e8fc35978bcac0c360b8557fb6a3c4484cfc2034a277a94072369404` | Complete finite-energy proof also inspected; its Fock conclusion is not needed here |
| `COMPACT_PATCH_FOCK_ISOMETRY_REVIEW.md` | `bc88af1dda77065d8806da9d689546547f40847a340177086793dab5f3a277cf` | Source-bound scope confirmation; does not review this new proof |
| Dybalski, [arXiv:1608.08750v1](https://arxiv.org/abs/1608.08750v1) | PDF `9d574c50f960920daa39a13fb2a07de09b57d717d715f4507731a43f03e6f1c4` | Theorem 4.2, all of its proof, Appendices A–B; all 13 pages read |
| Bachmann–Dybalski–Naaijkens (BDN), [arXiv:1412.2970v2](https://arxiv.org/abs/1412.2970v2) | PDF `3edeb48a167b9ae6a26d6d885ccde03b068423d432176a256eb0a4ee42a14126` | Complete pages 9–13 and 39–40: transfer, almost locality, finite-energy bound and transfer-lemma proof |

The read-only source tree was `c3f84746b1991e0a15c6da79d049b89d9469f727`; planning instructions were `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. The core creator review and its EX repair confirmation were read in full. This pass is an author derivation, not another independent review of those sources. The source ledger binds exact files and reading limits.

Let \(\mathcal H\) carry a vacuum \(\Omega\), a positive Hamiltonian H, and geometric lattice translations
\[
\alpha_t=\operatorname{Ad}e^{itH},\qquad
T_x=e^{-ix\cdot Q},\quad \tau_x=\operatorname{Ad}T_x,
\quad H\Omega=0,\ T_x\Omega=\Omega. \tag{C1}
\]
The flows commute. Fix a finite number \(n\ge1\) of creators \(B_i\). Their required direct properties are:

1. Each \(B_i\), its norm time derivative \(\delta B_i\), and the spatial Schwartz smears used below are almost local. Equal-time commutators of any two of these operators or their adjoints decay faster than every inverse power of their spatial separation.
2. The temporal operator transfer of \(B_i\) lies in a fixed compact interval \(I_i=[\epsilon_i,L_i]\subset(0,\infty)\). There is a compact full **operator** geometric momentum transfer set \(\Lambda_i\Subset O_i\), obtained by the geometric Schwartz filter (C2). Vacuum-vector momentum support alone is insufficient for the argument.
3. The exact vector \(B_i\Omega\) lies on the graph \(H=\Sigma_i(Q)\) in its chart. Each \(\Sigma_i\) is extended to a real smooth function on the torus, agreeing with the chart dispersion near \(\Lambda_i\). For the supplied construction, \(\Sigma_i(p)=\sqrt{M_i^2+\beta|p+\theta_i+2\pi n_i|^2}\) on its selected lift. Different masses, centres and lifts use separate extensions.
4. Fix \(h_i\in C_c^\infty(\mathbb R^d)\), \(h_i\ge0\). Their compact convex hulls are pairwise disjoint and contain \(v_i(\Lambda_i)\), where \(v_i=\nabla\Sigma_i\). Zero detectors are trivial and may be removed. Choose a small neighborhood of each \(\Lambda_i\) inside its chart so that its velocity image and \(\operatorname{supp}h_i\) still have disjoint compact convex hulls after a small enlargement. This choice follows from compactness, positive separation and continuity; it is not an extra shell-isolation condition.

The microscopic flow implementations, isolated positive mass-Casimir components and finite centre selectors needed to construct this class remain supplied conditions from the compact-creator source. They are not consequences of the four framework axioms in this note. There is no requirement that the geometric momentum supports of different species be disjoint: the separation is in their respective velocity images. No global isolated geometric energy–momentum shell is assumed.

The finite-energy estimate used below needs only positive energy, compact strictly lowering temporal transfer and almost locality. A self-contained derivation is given in §2. The direct creator Cook argument is also recalled there with all derivative terms. Thus the proof does not import Dybalski's global-shell hypotheses or his printed p.4 empty-set clause.

## 2. Full filtering, energy bounds, and the strong creation limit

For a smooth geometric filter \(\phi_i\) supported compactly in \(O_i\), the filtered creator is
\[
B_i=\sum_{z\in\mathbb Z^d}c_i(z)\tau_z(B_i^{\rm old}),\qquad
c_i(z)=\int_{\mathbb T^d}e^{ipz}\phi_i(p)\frac{dp}{(2\pi)^d}. \tag{C2}
\]
The coefficients are rapidly decreasing. Its vacuum vector is \(\phi_i(Q)B_i^{\rm old}\Omega\), while its full operator geometric transfer is contained in \(\Lambda_i=\operatorname{supp}\phi_i\). The latter follows directly by applying another spatial filter: convolution of the translation coefficients multiplies their transfer multipliers. Time evolution commutes with the spatial sum. Splitting \(|z|\le r/2\) from its Schwartz tail proves almost locality at radius r, also for its norm time derivatives. Temporal transfer, the selected graph and the centre sector are preserved.

Put \(A_i=B_i^*\) and \(P_R=\mathbf1_{[0,R]}(H)\), for \(R\ge0\). For completeness the finite-energy annihilation bound can be recovered without a geometric shell. For one creator B with lower transfer edge \(\epsilon>0\), set
\[
A_x=\tau_x(B^*),\quad
S_B=\sum_z\|[B^*,\tau_z(B)]\|<\infty.
\]
For finite \(\Lambda\subset\mathbb Z^d\), put \(Q_\Lambda=\sum_{x\in\Lambda}A_x^*A_x\). Let \(\mathcal P_r\) project onto the common kernel of all r-fold words in the \(A_x\), and \(b_r=\|\mathcal P_rQ_\Lambda\mathcal P_r\|\). Then \(b_1=0\), and \(A_x\operatorname{Ran}\mathcal P_r\subset\operatorname{Ran}\mathcal P_{r-1}\). For a unit vector \(\Phi\) in \(\operatorname{Ran}\mathcal P_r\), the exact expansion is
\[
\langle\Phi,Q_\Lambda^2\Phi\rangle
=\sum_{x,y}\langle A_x\Phi,[A_x,A_y^*]A_y\Phi\rangle
 +\sum_{x,y}\langle A_yA_x\Phi,A_xA_y\Phi\rangle. \tag{C3}
\]
The first sum in absolute value is at most \(S_B\langle Q_\Lambda\rangle_\Phi\) by its commutator row and column sums and \(2ab\le a^2+b^2\). Cauchy–Schwarz for the second sum, followed by swapping x and y in one factor, bounds it by \(\sum_{x,y}\|A_yA_x\Phi\|^2\le b_{r-1}\langle Q_\Lambda\rangle_\Phi\). Since \(\langle Q_\Lambda\rangle_\Phi^2\le\langle Q_\Lambda^2\rangle_\Phi\), this gives \(b_r\le S_B+b_{r-1}\le(r-1)S_B\). Every r-fold lowering word kills \(P_R\) when \(r\epsilon>R\). Monotone convergence of the bounded positive compressed sums therefore gives
\[
\sum_x\|A_xP_R\Psi\|^2\le b_B(R)\|\Psi\|^2,
\qquad b_B(R)=\lfloor R/\epsilon\rfloor S_B. \tag{C4}
\]
The common-word kernel, rather than a kernel of a single power, is essential. This is the Buchholz/BDN finite-energy mechanism; the displayed argument is also the one reconstructed in the frozen Fock source, §3.

Write \(M_R=\prod_i b_{B_i}(R)^{1/2}\). Repeated use of (C4) is legitimate because every annihilator lowers energy. It proves
\[
\|a_tP_R\|\le M_R,\qquad
(a_t\Psi)(\mathbf x)=A_1(t,x_1)\cdots A_n(t,x_n)\Psi,
\quad A_i(t,x)=\alpha_t\tau_x(A_i). \tag{C5}
\]
The common time evolution is unitary and commutes with \(P_R\), so the bound is uniform in t. All constants concern this fixed finite arrangement.

Let \(\mathscr K=\ell^2(\mathbb Z^{dn})\), \(L=\sum_iL_i\), and define initially on finitely supported f
\[
J_tf=\sum_{\mathbf x}f(\mathbf x)
B_n(t,x_n)\cdots B_1(t,x_1)\Omega.
\]
Every such vector has energy in \(I_1+\cdots+I_n\subset[0,L]\). Duality against \(P_L\mathcal H\), using (C5), gives
\[
\|J_t\|\le M_L,\quad J_t=e^{itH}J_0,\qquad
F_t(\Psi)=J_t^*\Psi,\quad
F_t(\Psi)(\mathbf x)=\langle\Omega,A_1(t,x_1)\cdots A_n(t,x_n)\Psi\rangle. \tag{C6}
\]
The inner product is antilinear in its first argument. Thus the creator order in \(J_t\) is the reverse of the annihilator order in \(F_t\).

Use \(\widehat f(p)=\sum_xe^{-ipx}f(x)\), with normalized Haar measure in the inverse transform. In each variable, taking the adjoint of (C2) yields a factor \(\overline{\phi_i(p_i)}\) in the Fourier transform of \(F_t\): indeed translation of the coordinate by z multiplies that transform by \(e^{ip_i z}\), and \(\sum_z\overline{c_i(z)}e^{ip_i z}=\overline{\phi_i(p_i)}\). The unfiltered amplitudes are in \(\mathscr K\) by the same finite-energy bound. Hence, as an \(\mathscr K\)-identity,
\[
\operatorname{supp}\widehat F_t\subset\Lambda:=\prod_i\Lambda_i,
\quad F_t=P_\Lambda F_t,
\quad J_t=J_tP_\Lambda. \tag{C7}
\]
Here \(P_\Lambda\) is the orthogonal Fourier multiplier by \(\mathbf1_\Lambda\). This is full-operator filtering, not a vacuum-support inference.

Choose real \(q_i\in C_c^\infty(O_i)\), equal to one on a neighborhood of \(\Lambda_i\), with their supports inside the velocity neighborhoods of hypothesis 4. Put
\[
q(D)=\prod_iq_i(D_{x_i}),\quad
\omega(D)=\sum_i\Sigma_i(D_{x_i}),\quad v=\nabla\omega,
\qquad S_t=J_te^{-it\omega(D)}. \tag{C8}
\]
Then \(S_t=S_tq(D)\), \(\sup_t\|S_t\|\le M_L\), and
\[
S=\operatorname{s-lim}_{t\to\infty}S_t\quad\hbox{exists on all of }\mathscr K. \tag{C9}
\]
Here is the precise density argument. The linear span of smooth product functions on the torus is dense. Apply q to each such product; its factors now have pairwise separated velocity supports. \(S_t\) on that product is the direct compact-packet scattering approximant with reversed creator order. Its one-particle vectors are constant in t because their \(-it\Sigma_i\) packet clock cancels the \(+itH\) vacuum-vector clock. The derivative of each packet contains **both** the packet with \(\delta B_i\) and the packet with amplitude \(-i\Sigma_i\widehat f_i\). Commuting that derivative to the vacuum gives every pairwise commutator, with all n−2 remaining factors. Each full packet norm is \(O((1+t)^d)\); almost locality and the rapid off-velocity packet tails bound each derivative commutator by \(c_N(1+t)^{2d-N}\). All n−2 remaining factors therefore give a total bound \(c_N'(1+t)^{nd-N}\). Take N=nd+2. For n=1 the derivative is zero. This is the compact-source §6 Cook argument, equations (24)–(27), and it applies to the filtered direct class. Uniform boundedness in (C6) extends convergence from that dense linear span to all of \(\mathscr K\). No adjoint strong-convergence conclusion is taken from (C9).

Let \(\mathcal H_{\rm sc}\) be the closed span of the vacuum and the constructed scattering states from the selected collection of charts/species. Then \(\operatorname{Ran}S\subset\mathcal H_{\rm sc}\). Also
\[
e^{iaH}S=Se^{ia\omega(D)}\quad(a\in\mathbb R), \tag{C10}
\]
because \(e^{iaH}S_t=S_{t+a}e^{ia\omega(D)}\) and both strong limits exist. Repeating this for the collection shows that \(\mathcal H_{\rm sc}\) is reducing for H. In particular its energy spectral projections remain in that space.

## 3. The complete scalar source and its exact support

Fix \(\Psi\in P_R\mathcal H\), R finite. From (C5)–(C6),
\[
F_t=J_0^*e^{-itH}\Psi,\quad
\sup_t\|F_t\|_2\le M_R\|\Psi\|,
\quad \sup_t\|\partial_tF_t\|_2\le R M_R\|\Psi\|. \tag{C11}
\]
Differentiation is strong in \(\mathscr K\). Let \(\kappa_i(z)\) be the inverse Fourier coefficients of the smooth periodic \(\Sigma_i\), and define
\[
A_i^{\Sigma}=\sum_z\kappa_i(z)\tau_{-z}(A_i),\qquad
D_i=\delta A_i+iA_i^{\Sigma}. \tag{C12}
\]
These are almost local, norm time-smooth where needed, and have temporal transfer contained in the same fixed negative interval as \(A_i\). The kernel is Schwartz; this spatial convolution does not enlarge the full geometric momentum support. With our transform convention, \(\Sigma_i(D_x)f(x)=\sum_z\kappa_i(z)f(x-z)\), explaining the minus sign in \(\tau_{-z}\).

The exact vacuum graph gives \(\langle\Omega,D_i(t,x)\Phi\rangle=0\) for every \(\Phi\). In detail, the row derivative of \(A_i(t,x)\) is \(-i\) times its row composed with H, while that row is the adjoint of \(B_i(t,x)\Omega\). H on this vector is \(\Sigma_i(Q)\); Fourier transformation in x converts it to \(\Sigma_i(D_x)\). All these vacuum vectors have compact energy, so this row identity has no unspecified unbounded-generator domain.

Differentiating the full ordered product and commuting each \(D_i\) to the far left gives the exact scalar equation
\[
\partial_tF_t=-i\omega(D)F_t+\mathcal R_t, \tag{C13}
\]
\[
\mathcal R_t(\mathbf x)=
\sum_{i=2}^n\sum_{j<i}
\langle\Omega,A_1\cdots A_{j-1}[A_j,D_i]
A_{j+1}\cdots A_{i-1}A_{i+1}\cdots A_n\Psi\rangle. \tag{C14}
\]
The factor \(A_k\) carries \((t,x_k)\), and \(D_i\) carries \((t,x_i)\). This keeps both derivatives from (C12), every commutator, and all n−2 other factors in their original order. It is zero for n=1. Equal common times factor out of the commutator by \(\alpha_t\), leaving no growing LR-time constant. Almost locality and the bounded norms of all remaining factors imply, for every integer N,
\[
|\mathcal R_t(\mathbf x)|\le c_N\|\Psi\|
\sum_{i>j}\langle x_i-x_j\rangle^{-N},\qquad
\sup_t\|\mathcal R_t\|_2\le(R+\|\omega\|_\infty)M_R\|\Psi\|. \tag{C15}
\]
The second bound follows from (C11)–(C13); it is not obtained by summing a pointwise bound with uncontrolled spectator coordinates.

Most importantly, the **entire** source has the required full momentum filter:
\[
\mathcal R_t=P_\Lambda\mathcal R_t=q(D)\mathcal R_t. \tag{C16}
\]
Indeed (C7) holds for every t, the subspace \(P_\Lambda\mathscr K\) is closed, the derivative in (C11) stays in it, and \(\omega(D)\) preserves it. Thus (C13) proves (C16) for the sum, independently of how its individual commutator terms are written. Vacuum graph support alone would not prove this step.

Write \(m=nd\), and let \(\mathcal D=\{\mathbf y:y_i=y_j\text{ for some }i\ne j\}\). For any fixed smooth compact \(\chi\) whose support avoids \(\mathcal D\), lattice-point counting in (C15) gives
\[
\|\chi(X/s)\mathcal R_s\|_2
\le c_{\chi,N}s^{m/2-N}\|\Psi\|,\qquad s\ge1. \tag{C17}
\]
This estimates only an off-collision source. It does not claim global source decay or absence of cluster channels.

## 4. A two-time kernel estimate with both Schur sums

Choose compact convex sets \(K_i\) containing both \(\operatorname{supp}h_i\) and \(v_i(\operatorname{supp}q_i)\), with a positive mutual separation. They exist by hypothesis 4 and the choice of q. Put
\[
K=\prod_iK_i\subset\mathbb R^m,\qquad
\mathsf h(\mathbf x)=\prod_i h_i(x_i),\quad \mathsf h_t=\mathsf h(X/t).
\]
For n≥2, K has positive distance from \(\mathcal D\). Choose a small \(\delta>0\) and \(0\le\chi\le1\), smooth and compact, equal to one on the closed \(\delta\)-neighborhood of K, and supported away from \(\mathcal D\). For n=1 there is no collision set and the source is identically zero; any such compact cutoff may be used.

**Two-time lemma.** For every integer \(A\ge0\) there is a finite constant \(c_A\), independent of \(s\ge t\ge1\), such that
\[
\|\mathsf h_t e^{i(s-t)\omega(D)}q(D)(1-\chi(X/s))\|
\le c_A s^{-A}. \tag{C18}
\]
No division by \(s-t\) occurs; in particular the estimate includes \(s=t\).

To prove it, write \(\mu=s-t\ge0\). The lattice kernel, with \(\mathbf x,\mathbf y\in\mathbb Z^m\), is
\[
\mathsf h(\mathbf x/t)(1-\chi(\mathbf y/s))
\int_{\mathbb T^m}e^{i\Phi(p)}q(p)\frac{dp}{(2\pi)^m},
\quad
\Phi(p)=(\mathbf x-\mathbf y)\cdot p+\mu\omega(p). \tag{C19}
\]
Whenever the two spatial factors are nonzero and \(p\in\operatorname{supp}q\), \(\mathbf x/t\in K\), \(v(p)\in K\), and \(\operatorname{dist}(\mathbf y/s,K)\ge\delta\). Convexity gives
\[
\frac{\mathbf x+\mu v(p)}s
=\frac ts\frac{\mathbf x}t+\left(1-\frac ts\right)v(p)\in K,
\qquad
|\nabla_p\Phi(p)|=|\mathbf x-\mathbf y+\mu v(p)|\ge\delta s. \tag{C20}
\]
This verifies the stationary sign directly: the stationary source position is \(\mathbf y=\mathbf x+(s-t)v(p)\). The opposite sign is incompatible with (C19).

Since \(v\) is bounded, combine (C20) with \(|\nabla\Phi|\ge|\mathbf x-\mathbf y|-s\|v\|_\infty\). There is a fixed c>0 with
\[
|\nabla\Phi|\ge c\bigl(s+|\mathbf x-\mathbf y|\bigr)
\quad\hbox{on }\operatorname{supp}q. \tag{C21}
\]
For \(|\mathbf x-\mathbf y|\) larger than \(2s\max(1,\|v\|_\infty)\), use the second bound; otherwise use (C20). All positive-order p-derivatives of \(\nabla\Phi\) are bounded by constants times s, hence by constants times \(r=s+|\mathbf x-\mathbf y|\). Consequently every fixed derivative of \(b=\nabla\Phi/(i|\nabla\Phi|^2)\) on a neighborhood of \(\operatorname{supp}q\) is \(O(r^{-1})\). One may insert a smooth cutoff in \(|\nabla\Phi|/r\), equal to one on that neighborhood, to define b periodically everywhere without a zero denominator.

The vector field \(b\cdot\nabla_p\) sends \(e^{i\Phi}\) to itself there. Integrating by parts N times on the torus bounds the kernel by
\[
|L_{t,s}(\mathbf x,\mathbf y)|
\le c_N\bigl(s+|\mathbf x-\mathbf y|\bigr)^{-N}. \tag{C22}
\]
Derivatives of q are fixed, and the above derivative estimates keep constants uniform even when \(\mu\) is zero or very small. There is no momentum-boundary term: q and the smooth dispersions are periodic, and \(\mathbf x-\mathbf y\) is an integer vector. Equivalently, each q factor has compact chart support and integration may be done there.

For N>m, the two Schur sums satisfy
\[
\sup_{\mathbf x}\sum_{\mathbf y}|L_{t,s}(\mathbf x,\mathbf y)|
\le c_N' s^{m-N},\qquad
\sup_{\mathbf y}\sum_{\mathbf x}|L_{t,s}(\mathbf x,\mathbf y)|
\le c_N' s^{m-N}.
\]
Both follow from the same translation-invariant lattice sum \(\sum_z(s+|z|)^{-N}\le c s^{m-N}\); the latter follows by counting shells of thickness s. Schur's test therefore gives an operator norm \(O(s^{m-N})\). Choosing N>m+A proves (C18). No finite-dimensional truncation or numerical propagation test is used in this proof.

## 5. Reversing the scalar integral at fixed t

Let g be the real smooth product multiplier in PC, equal to one on \(\Lambda\), with support in the specified charts. It need not commute with \(\mathsf h_t\), and no such commutation is used. Define
\[
w_t=e^{it\omega(D)}F_t=S_t^*\Psi,
\quad K_t=e^{it\omega(D)}g(D)\mathsf h_t e^{-it\omega(D)},
\quad u_t=K_tw_t=e^{it\omega(D)}g(D)\mathsf h_tF_t. \tag{C23}
\]
By (C9), \(w_T\rightharpoonup S^*\Psi\) as \(T\to\infty\). At a **fixed** t, \(\mathsf h_t\) has finite support on the lattice, so K_t has finite rank. Hence \(K_tw_T\to K_tS^*\Psi\) in norm for that fixed t. There is no exchange of a moving-t compactness limit with T.

Equation (C13) gives \(\partial_s w_s=e^{is\omega(D)}\mathcal R_s\) strongly. For finite T≥t its exact integral is
\[
u_t=K_tw_T-\int_t^T K_te^{is\omega(D)}\mathcal R_s\,ds,
\qquad
K_te^{is\omega(D)}\mathcal R_s
=e^{it\omega(D)}g(D)\mathsf h_t e^{i(s-t)\omega(D)}q(D)\mathcal R_s.
\]
The rightmost q is inserted using (C16), and its location is retained. Insert \(1=\chi(X/s)+(1-\chi(X/s))\) **after q**. The localized term is bounded by
\(\|g\|\|\mathsf h\|_\infty\|q\|\,\|\chi(X/s)\mathcal R_s\|_2\), rapidly small by (C17). The other term is bounded using (C18) and the global \(\ell^2\) source bound in (C15). Therefore, for every A,
\[
\|K_te^{is\omega(D)}\mathcal R_s\|_2
\le c_{A,R}s^{-A}\|\Psi\|\qquad(s\ge t\ge1).
\]
The constants depend on the fixed arrangement and R. This proves absolute Bochner integrability to infinity and permits the fixed-t norm limit T→∞. It yields
\[
u_t=K_tS^*\Psi-\int_t^\infty K_te^{is\omega(D)}\mathcal R_s\,ds,
\qquad
\|u_t-K_tS^*\Psi\|_2\le c_{N,R}t^{-N}\|\Psi\|
\quad\text{for every N}. \tag{C24a}
\]
Only after taking that fixed-t limit do we let t increase.

The remaining free limit is elementary and strong:
\[
e^{it\omega(D)}\mathsf h(X/t)e^{-it\omega(D)}
\longrightarrow\mathsf h(v(D)).
\]
For completeness, Fourier-invert the Schwartz function \(\mathsf h\) in its Euclidean argument. For each fixed \(\eta\in\mathbb R^m\), the transformed operator \(e^{it\omega(D)}e^{i\eta\cdot X/t}e^{-it\omega(D)}\) acts in momentum space by
\[
\widehat f(p)\longmapsto
e^{it[\omega(p)-\omega(p-\eta/t)]}\widehat f(p-\eta/t).
\]
The phase tends uniformly to \(e^{i\eta\cdot v(p)}\), and torus translations converge strongly in \(L^2\). The operator norms are one. Dominated convergence against the integrable Fourier transform of \(\mathsf h\) gives the displayed strong limit for every f. Thus \(K_t\to g(D)\mathsf h(v(D))\) strongly. Combining this with (C24a), and noting \(S^*=P_\Lambda S^*\), proves the exact PC statement and its limit:
\[
\boxed{\quad
\operatorname{s-lim}_{t\to\infty}
e^{it\omega(D)}g(D)\mathsf h(X/t)F_t(\Psi)
=\mathsf h(v(D))S^*\Psi,
\qquad\Psi\in P_R\mathcal H,
\quad 0\le R<\infty.\quad} \tag{C24}
\]
The g on the limit is the identity on \(\Lambda\); it was not deleted at finite time. Vector norm convergence implies the requested norm-Cauchy condition. The free limit is strong, not claimed to be an operator-norm limit. On \(P_R\mathcal H\cap\mathcal H_{\rm sc}^{\perp}\), \(S^*\Psi=0\), so (C24a) additionally gives rapid convergence to zero uniformly on its unit ball.

This closes PC at the specified fixed-arrangement scope if the written proof is confirmed. It does not assert that \(S_t^*\) itself converges strongly on arbitrary vectors. It also avoids a separate, omitted “standard scattering-sector” calculation: the fixed-t compactness argument applies to every finite-energy vector and retains its weak limit \(S^*\Psi\).

## 6. Positive detector convergence and scattering range

Now add exactly the separate vacuum hypotheses
\[
\ker H=\mathbb C\Omega,\quad
\operatorname{spec}H\subset\{0\}\cup[\gamma,\infty),\quad\gamma>0,
\]
and choose a bounded energy interval J with
\[
(J-I_1-\cdots-I_n)\cap\operatorname{spec}H\subset\{0\}.
\tag{C25}
\]
For example, an interval difference contained in \((-\gamma,\gamma)\) suffices. Temporal transfer addition gives the exact vacuum remainder
\[
A_1(t,x_1)\cdots A_n(t,x_n)P_J
=|\Omega\rangle\langle\Omega|A_1(t,x_1)\cdots A_n(t,x_n)P_J.
\]
This uses no joint geometric shell isolation. It does not establish that available tuples cover every vector in J.

Define the finite-time individual detectors and the positive compressed product by
\[
C_i(t)=\sum_xh_i(x/t)A_i(t,x)^*A_i(t,x),\qquad
Q_J(t)=P_JJ_t\mathsf h_tJ_t^*P_J. \tag{C26}
\]
The spatial sums are finite for fixed t. Reorder the factors in \(C_1(t)\cdots C_n(t)\) to \(a_t^*(1\otimes\mathsf h_t)a_t\). Each swap is between different labels whose positions are separated by a fixed multiple of t. Its equal-time commutator is \(O(t^{-N})\), and all 2n−2 remaining operator factors have fixed norms. There are \(O(t^{nd})\) position tuples and finitely many swaps. Taking N arbitrarily large gives
\[
C_1(t)\cdots C_n(t)P_J
=J_t\mathsf h_tJ_t^*P_J+O(t^{-\infty})
\tag{C27}
\]
in operator norm; the vacuum remainder was used only at this step. Compression gives \(P_JC_1(t)\cdots C_n(t)P_J=Q_J(t)+O(t^{-\infty})\).

At every t,
\[
0\le Q_J(t)\le M_L^2\|\mathsf h\|_\infty P_J.
\]
For \(\Psi\in P_J\mathcal H\), \(Q_J(t)\Psi=P_JS_tu_t(\Psi)\): indeed \(J_tg(D)=J_t\), without commuting g through \(\mathsf h_t\). Equations (C9) and (C24) therefore prove
\[
\boxed{\quad Q_J(t)\longrightarrow
Q_J=P_JS\mathsf h(v(D))S^*P_J
\quad\text{strongly},\qquad
0\le Q_J\le M_L^2\|\mathsf h\|_\infty P_J,
\quad\operatorname{Ran}Q_J\subset P_J\mathcal H_{\rm sc}.\quad} \tag{C28}
\]
Positivity and the range are transparent from the formula and (C10). In fact \(S\mathsf h(v(D))S^*\) commutes with H because \(\mathsf h(v(D))\) commutes with \(\omega(D)\). Thus (C27) also gives the uncompressed product limit on \(P_J\mathcal H\), with the same value as (C28). No uniformity over growing particle number, infinitely many charts, vanishing separation, or unbounded energies is claimed.

For a countable family of admissible arrangements, each limit is now a positive bounded operator with scattering range. One may form the norm-convergent weighted positive sum used in the frozen exhaustion criterion. Its common kernel is still an independent issue: neither (C24) nor (C28) proves that every nonzero vector in \(P_J\mathcal H\) has a nonzero detector response. ND, energy capture, coverage of all needed channels, EX, and the later full-algebra shift conclusion remain separate unproved obligations. A Fock isometry identifies selected scattering ranges but cannot supply their surjectivity.

## 7. Preserved failed shortcuts and source precision

1. **Strong creation limits do not give strong adjoint limits.** On \(\ell^2\), \(T_n=|e_0\rangle\langle e_n|\) tends strongly to zero, but \(\|T_n^*e_0\|=1\). The proof uses only weak adjoint convergence, followed by a compact operator at fixed t.
2. **Fixed-time compactness is not uniform moving-time compactness.** A sequence of rank-one projections onto \(e_n\) preserves \(e_n\) although \(e_n\rightharpoonup0\). Taking T→∞ at fixed t before letting t increase is essential in (C24a).
3. **The forward Cook estimate is insufficient.** Differentiating u directly produces a generally nonintegrable \(t^{-1}(\nabla\mathsf h)(X/t)\cdot(v(D)-X/t)\) term. The reversed integral estimates the collision source at times s≥t instead. No conclusion is drawn from an unintegrated 1/t bound.
4. **Dropping the full momentum filter breaks this estimate.** The velocity in (C20) is controlled on \(\operatorname{supp}q\). A vacuum-only support assertion, or an unfiltered propagator after multiplication by \(\chi_s\), does not preserve that control. The exact order \(\mathsf h_t e^{i(s-t)\omega}q(D)(1-\chi_s)\) is used throughout.
5. **Dropping convex containment breaks this geometric proof.** The stationary source coordinate is the convex combination in (C20). Mere pairwise separation of the detector supports does not force that segment to avoid collisions when carrier velocities lie outside their corresponding convex regions. This is a limit of the demonstrated route, not an impossibility claim for other detector cutoffs.
6. **Dybalski v1 typography is not a premise.** The p.4 condition \((h-h)\cap\operatorname{Sp}U=\varnothing\) cannot hold for a nonempty shell with a vacuum; BDN's corresponding pseudo-relativistic condition has \(\{0\}\). Also direct differentiation of \(f(\lambda)=\Sigma(\xi+\lambda z/2)-\Sigma(\xi-\lambda z/2)\) gives a **sum** of third derivatives at the two arguments in \(f'''\); the printed difference in (B.17) fails already for the periodic function \(\Sigma(p)=\sin p\), \(\xi=0\). The p.12 image was freshly rendered from the hash-bound PDF and visually checked: the difference is printed in the source, not introduced by extraction. The usual cubic remainder bound survives the corrected differentiation, but neither that identity nor the primary Weyl/Taylor expansion is used in (C18)–(C24).

These are explicit failed proof shortcuts and scope boundaries. No local-UHF countermodel to the full supplied microscopic setting or universal no-go theorem has been constructed.

## 8. Evidence, verification limits, and recovery

The proof's load-bearing new step is the uniform two-time kernel bound (C18) together with the fixed-t reversed integral (C24a). The written proof checks its stationary sign, both Schur sums, the case s=t, periodic momentum boundaries, the full source filter, the complete source derivative and the order of all noncommuting cutoffs. The inherited compact Cook construction is used at its directly proved scope; Fock isometry and the E1–E18 review outcome are not substituted for these checks.

Six finite author controls ran once with a declared 60-second timeout, exit 0, in approximately 0.029 seconds; all seven output records and empty stderr are preserved in `compact_detector_convergence/`. The 11-mode Fourier identities had errors below 4.5e-15 and rejected opposite phases, wrong Duhamel signs, moving g through the spatial cutoff, and deleting q after a spatial cutoff. Seventy-two exact rational convex-combination cases include s=t and s/t close to one; a wrong-sign case reaches the collision plane. Exact cubic arithmetic and a periodic sine case reject the printed Taylor difference. These controls discriminate finite algebra and signs; they cannot certify the all-scale kernel estimate, analytic convergence, the supplied microscopic conditions, independence, ND or EX. The separate source rendering also ran under a declared 60-second timeout and exited 0. Complete commands, stdout/stderr and execution metadata are stored in the evidence directory. The complete proof has now received that separate reconstruction. The report `2f9ebfed745c217d97750ddc5f7a5edeaffaede72895ad0da1af0974ef2c51f0` and its pre-author-evidence reconstruction/control freeze `4d75d0893cc6fdddb207dd31ddd137359874183b2f8b8b8878382c21adaa8702` are preserved in the milestone packet. The reviewer checked the full analytic argument, used a distinct two-time Fourier-kernel control, then reproduced the author output and rejected six actual copied-code defects. Finite Schur sums have no uncomputed-tail certificate; the written all-scale estimate establishes convergence. Root supplied the mechanism and is a contributor, not an independent reviewer.

The [finite detector control](../scripts/compact_detector_convergence_2026_10_12.py) retains the entire original helper. The milestone packet preserves its complete source, frozen recovery record, separate proof reconstruction, all controls and failures. PUBLICATION_EDITS.json and reconstruct.py recover every note and primary byte; DELIVERY_CHECKS.md states the publication checks and remaining audit gates. No Lean certificate, physical realization, retained status, applied audit verdict, editable-prompt change or physical-axiom change is claimed. The live campaign checkpoint remains in `toe-dynamics-bridge-20261009`, with fixed deadline 2026-10-12 16:00:52 UTC.
