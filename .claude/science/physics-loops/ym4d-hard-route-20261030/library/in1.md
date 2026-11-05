# IN1: constant order, mass induction and first passage

Provenance: Codex, Pass 2, 2026-11-04, distilling Claude's [pass-1 draft](in1-draft.md) at checkout e1464b5d12d63c11ce0d15dbaa99373c579a485e. Source attribution: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, revision 31a47c543775. Research text, not an audit; grants no status. Not yet refereed.

The main result is Theorem 12: a conditional IN1 reduction. The matrix estimate, budget arithmetic, genealogy calculation and scalar stopping argument below are hand proofs. The hypotheses concerning the actual four-dimensional construction remain imports; the missing implications are marked **Outstanding** where used. Source-line checks were recorded in a distiller's source record that is not in this checkout; the referee rechecked the YM3 and FG11 lines directly (`gates/in1-gate.md`, F1). Here SA means the pinned outline, CA-I the pinned complete account I, and YM3 the pinned three-dimensional manuscript.

## Definitions

Work with \(SU(2)\) in four dimensions, normalized Haar measure, odd block size \(L\ge27\), and Wilson action
\[
 A(U)=\sum_p a_p(U),\qquad a_p(U)=1-\tfrac12\operatorname{Re}\operatorname{Tr}\partial U(p).
\]
For real \(U\), put \(f_U(p)=\|\partial U(p)-1\|_{\rm op}\); then \(f_U(p)^2=2a_p(U)\). On complexified fields \(a_p=1-\tfrac12\operatorname{Tr}\partial U(p)\) denotes the holomorphic continuation. All lattice coordinates in estimates are in the units of the level being considered. The final microscopic spacing is \(a_K=L^{-K}\). Unspecified bound constants are positive and finite; reserve coefficients may be zero.

**Frames and thresholds.** Fix \(c_0>0,c_2\ge0\), and fix the weak constants before choosing a coupling ceiling:
\[
 \underline\lambda=c_0/4,\quad c_5=2c_2,\quad
 C_\beta=c_0+2c_2+2,\quad \overline B=C_\beta+1.
\]
A frame is a finite real sequence \(\theta\) with \(\theta_j\ge X_0=\gamma^{-2}>e\) and
\[
 \underline\lambda(j-i)-c_5\le\theta_i-\theta_j\le\overline B(j-i)
 \quad(i\le j).                                                    \tag{1}
\]
Write \(m_j=\min_{i\le j}\theta_i\), \(R_j=\lceil(\log m_j)^r\rceil_{L^{\mathbb N_0}}\), \(N_j=R_j\), and
\[
\begin{split}
 g_j&=\theta_j^{-1/2},& P_j&=A_0(\log\theta_j)^{p_0},&
 \epsilon_j&=g_jP_j,\\
 \delta_j&=A_1g_j(\log\theta_j)^{p_0},&
 \delta'_j&=A_1g_j(\log\theta_j)^{p_1},&
 \alpha_{\iota,j}&=C_\iota g_j(\log\theta_j)^q,\\
 s_j&=(A_1/C_0)(\log\theta_j)^{p_0-q}.&&&
\end{split}                                                        \tag{2}
\]
The letters \(A_0,A_1\) denote threshold amplitudes, not one-loop primitives. A tube is a prescribed positive function \(t(\theta)\) satisfying
\[
 |x_j-\theta_j|\le t(\theta_j)\le\theta_j/4,\quad
 t(\theta)/\theta\longrightarrow0,\quad
 t(\theta)\alpha_0(\theta)\delta(\theta)\longrightarrow0.              \tag{3}
\]
The actual source package must supply its stronger logarithmic tube bounds. Set \(\tau_j=x_j/\theta_j\).

**Domains, norms and coefficients.** Each connected union \(X\) of level-\(j\) \(M\)-cubes has a specified hereditary complex core \(\mathcal D_j(X)\), as in SA 5663–5755 (R4–R6). Its data include local gauges and potential/current bounds on every required subdomain, existence of the required averaging towers, and their uniform bounds. These requirements are part of the domain; small plaquette curvature alone is not its definition. Let \(d_j(X)\) be the minimum length of a tree in \(X\) meeting its cubes, divided by \(M\). The supplied boundary hull length is \(d_j^\natural(\mathcal S;X)\). For a pointed family,
\[
 \|E\|_{j,\kappa}
 =\sup_{\text{tori and companion}}\sup_{X,z\in X}
   e^{\kappa d_j(X)}\sup_{\mathbf p\in\mathcal D_j(X)}|E(X,\mathbf p,z)|. \tag{4}
\]
For an unpointed family omit \(z\). A companion is one family on \(\mathbb Z^4\) agreeing on common collared lifts across all admissible tori and cutoffs with the same frame prefix.

The coefficient \(b[\widehat E]\) is the SA R16 readout, not an arbitrary Hessian. In the fixed trivial chart, with the supplied linear background response
\(\mathfrak h_\infty B=(\mathsf H_\infty B,d^*d\mathsf H_\infty B)\), define
\[
\begin{split}
 \Pi^E(c,c';z)&=\tfrac13\sum_{a=1}^3\sum_{\widehat X\ni z}
  \operatorname{Hess}\widehat E(\widehat X,\cdot,z)
       [\mathfrak h_\infty\delta_c^a,\mathfrak h_\infty\delta_{c'}^a],\\
 \sum_z\Pi^E(c,c';z)&=\Pi^E_{\mu\nu}(c'_--c_-),\\
 b[\widehat E]&=\sum_{u\in\mathbb Z^4}\Pi^E_{\mu\nu}(u)u_\mu u_\nu
 \quad(\mu\ne\nu).
\end{split}                                                        \tag{5}
\]
Here \(c,c'\) are oriented unit bonds in directions \(\mu,\nu\), \(c_-\) is the initial site, and \(\delta_c^a\) is the bond form supported at \(c\) with value the \(a\)-th vector of a fixed orthonormal color basis. The Hessian uses SA's chart \((A,J)\mapsto(e^{i\eta_jA},J)\), where \(\eta_j\) is that chart's mesh in level-\(j\) units. Absolute convergence, displacement dependence, independence of \(\mu\ne\nu\), Ward identities and this normalization are hypotheses of OL1. Each pointed member subtracts its own coefficient times the tent Wilson action; the tents \(h_z(x)=\prod_{\mu=1}^4(1-|x_\mu-z_\mu|)_+\) sum to one.

**Histories and mass.** A history is the finite record of regions, failed and passed tests, created cells, marks, and integral operations. A node \(u=(n,C)\) is a component at level \(n\), with cell count \(|C|_n\). Its genealogy has lower-level predecessors and at most one successor per node. The outer genealogy stops at inner islands. A cut island is counted as an outer leaf, while its stored operation is kept as a separate inner factor; neither its interior history nor its old drop-outs are replayed.

For an outer record \(\omega^\circ\), define the charged volume
\[
 V^\circ(\omega^\circ)=\sum_{(n,C)\ {\rm outer}}
       (1+\log x_n)(MR_n)^4|C|_n,\qquad
 v^\natural(\omega)=V^\circ(\omega^\circ)+\sum_y v^\natural(\omega_y). \tag{6}
\]
Thus each uncut node occurs once and each cut boundary at most twice. This is a deliberately explicit enlargement of the own-level stored-site volume in SA. The geometry import must bound the source reserve volume \(v\) by \(C_vv^\natural\); a requested reserve \(c_rv\) is paid by choosing \(c=C_vc_r\) below.

All normalizers, densities and chart determinants remain in the integrand \(I_\omega\); the base measure \(\mu_\omega\) is a specified product of Haar and Lebesgue measures on the stored coordinates. Inner frame factors are kept explicitly. If \(w=|W_4|\) is the finite frame-group order, set
\[
 \mathfrak M_c(i,X)=\frac1w\sum_\omega e^{c v^\natural(\omega)}
   \int^*\sup_{\mathbf p\in\mathcal D_i(\widetilde X)}
                       |I_\omega(\xi;\mathbf p)|\,d\mu_\omega(\xi).  \tag{7}
\]
Here \(\widetilde X\) is the creation-domain hull of \(X\). The upper integral is the infimum over integrals of nonnegative Borel majorants. This avoids assuming measurability of an uncountable supremum.

For a drop-out, replace the supremum in (7) by the supremum over its compatible real evaluation fibre: the stored averages agree; the field is regular on each recorded layer; all recorded tests other than the new root failure hold; every inner operation is read in its creation domain; free Wilson weights have the prescribed positive lower bound and the kept forms and chart Jacobians obey the prescribed one-sided bounds. Include the carrying Wilson factor on its owned shares. The supremum of an empty fibre is zero. The root failure pays its next wait, not this mass.

**Oscillation.** For the supplied carrier decomposition \(\Phi_\omega=\Phi^\circ_\omega+\sum_f\Phi_{\omega,f}\), a carrier \(R_f\) supports both stored-variable and external-pair dependence. On the fixed creation domain put
\[
 \operatorname{osc}\Phi_{\omega,f}
 =\sup_{\xi,\mathbf p,\mathbf p'}|
       \Phi_{\omega,f}(\xi;\mathbf p)-\Phi_{\omega,f}(\xi;\mathbf p')|.
                                                                    \tag{8}
\]
No bound on the large negative scalar part is imposed.

## Named imports and their precise scope

The following are hypotheses, not conclusions about this checkout.

**H-M (actual matrices and UM, FP1/PR1/NL1).** For the actual localized Gaussian functional and its actual carriers, on every disc \(|s_\Delta|<e^{\bar\kappa}\), the covariance datum \(C\) is complex symmetric, \(\Gamma\) is rectangular, and there are real reference matrices \(C_*,\Gamma_*\), with \(C_*\) symmetric positive definite, such that
\[
 \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\qquad
 \|C-C_*\|+\|\Gamma-\Gamma_*\|
 \le H_0\{e^{b\bar\kappa-dM}+H_p(M)(a_0+a_1+j_0)\}
       +C_\tau|\tau-1|.                                             \tag{9}
\]
Here \(K_0\ge1\) and \(H_0,b,d,C_\tau>0\) precede \(\bar\kappa,M\); \(0\le H_p(M)<\infty\) is allowed to follow \(M\). The functional is normalized, hereditary in its declared carriers, wall-factorizing, holomorphic on these discs, and agrees at physical parameters with the actual fluctuation law. Its local dimension is at most \(c_m(LM)^4\) per cube. Import the finite-dimensional Gaussian comparison SA 13904–14089 (FG1–FG11): for reference bound \(K_0\), perturbation \(\varepsilon\le\varepsilon_0(K_0)\) and quadratic tilt \(\rho\le\rho_0(K_0)\), the absolute local Gaussian integral costs at most \(\exp[A_{K_0}(\varepsilon+\rho)m]\). Also import the UM carrier counts and logarithm implication SA 14276–14811.

**Outstanding — actual matrix envelope.** Lemma 2 below proves (9) for an auxiliary path-weighted construction under a *global* gap hypothesis. It does not identify that construction with H-M or prove heredity. SA 14141–14205 and the layered PR1 inputs do not supply this identification. The enlarged-disc estimate with constants fixed before \(\bar\kappa,M\) remains an actual-construction obligation. Note: [carrier-adopt.md](carrier-adopt.md) §6 and [inv-root.md](inv-root.md), passed by Codex in `carrier-check.md` as supplying um-envelope (6), may make this item smaller than stated; this is to be checked against H-M.

**H-OL (one-loop identity, OL1).** The actual companion normalizers have coefficients
\[
 b_j^0=\mathcal A_j-\mathcal A_{j-1},\quad
 \mathcal A_0=0,\quad |\mathcal A_j-jc_0|\le c_2,\quad
 c_0=\frac{11}{3\pi^2}\log L.                                       \tag{10}
\]
The readout (5), its own-coefficient subtraction and summable age decay apply to the actual regular members. This includes the localized-to-bulk identification and normal convergence needed to use the value in (10).

**Outstanding — coefficient identification.** The bulk calculation in [b-value.md](b-value.md), Theorem V, and the periodization argument in [prefactor-loc.md](prefactor-loc.md), Theorem S/Corollary T, do not by themselves identify every actual localized coefficient with that calculation. OL1 must supply the companion, normalization and localization sum; scalar stopping arithmetic cannot supply them.

**H-SF (small-field formation, NL1/ST1/OL1/SC1).** From any current presentation satisfying the class conditions below, the family \(\widehat E^{(k+1)}\) and its readout are formed at \((\theta_k,x_k)\), *before* choosing \(\theta_{k+1}\). They obey
\[
 b_{k+1}=b_{k+1}^0+e_{k+1},\quad
 |e_{k+1}|\le u(\theta_k):=
 C_f\theta_k^{-1/2}(\log\theta_k)^{p_0}
       +C_v^{\rm flow}\theta_k^{-(\kappa_0-4)/2}.                    \tag{11}
\]
The constants precede \(\gamma\), and formation uses only the current prefix and the weak constants (1). With a frame prolongation and the next tube condition, the exact step exists and preserves sourced integrals. Provided its list size, meaning \(\sum_jf_{n+1-j}\|E^{(j)}\|+\sum_jw_{n,j}\|R^{(j)}\|\) as in Lemma 5 (this matches SA R18, 5993-6010), is at most \(N_*\), it returns
\[
\begin{split}
 \|E^{(k+1)}\|&\le E_N+C_E(
 |1-\tau_k|+\delta_k+s_kN_*+e^{-c_{\rm tail}P_k^2}),\\
 \|R^{(k+1)}\|&\le\theta_{k+1}^{-\kappa_0/2},\qquad
 |B^{(k+1)}(X)|\le\mathsf B e^{-\kappa d_{k+1}^\natural(\mathcal S;X)}.
\end{split}                                                        \tag{12}
\]
\(c_{\rm tail}>0\) is fixed before \(\gamma\), and \(C_E\) depends on neither \(E_0\) nor \(N_*\). The boundary origin bounds defining \(\mathsf B\) do not depend on \(\mathsf B\); old boundary data enter only through a vanishing difference factor, a long-domain exponential, or a volume cost chosen after \(\mathsf B\). Analyticity, reality, gauge invariance, covariance, companion coherence and the pointed subtraction/age-decay structure are preserved. Actual remainder radius weights satisfy
\[
 w_{n,j}\le C_{\rm rad}(\alpha_{0,n}/\alpha_{0,j})^2,\qquad
 f_\nu\le C_{\rm age}\nu^aL^{-b_{\rm age}\nu},\quad b_{\rm age}>0.      \tag{13}
\]
The fixed factor \(C_{\rm rad}\) includes all radii, the enlargement factor and the evaluation-level convention of R18; it is not silently set to one.

**Outstanding — formation and domains.** This is the actual formation theorem, not its numerical output bound alone. [b4-induction.md](b4-induction.md) proves an ordered ordinary implication under its named inputs; it explicitly does not establish all typed/source bounds. [layered-a3.md](layered-a3.md) also leaves actual stage admission conditional. Neither is a proof of H-SF.

**H-LF (exact operations, LF1(1)).** Every partition, storage operation and change of variables is a specified Borel kernel, with each variable retained or integrated exactly once and with every physical real weight nonnegative. The equality of measures includes the source insertion and holds separately for each standing part. A test is a total indicator: it is one precisely when every object it reads exists and all its inequalities hold. This is the scope of [c1-repr.md](c1-repr.md).

**H-G (geometry and coding, LF1(2)).** For each outer genealogy let \(o_n,l_n,n_t^{\rm cr},n_t^{\rm mk}\) count occupied cells, light nodes, created cells and marked nodes (excluding the root mark). There are fixed \(C_g\ge1,s_0\ge1,C_T\ge1\) such that
\[
\begin{split}
 |C(u)|&\le C_g(1+o(u)),\\
 o_n&\le\tfrac12o_{n-s_0}+C_g l_{n-s_0}
                +C_g\sum_{n-s_0<t\le n}n_t^{\rm cr}.                \tag{14}
\end{split}
\]
Counts below the initial level vanish. A node is light if and only if \(o(u)\le C_g\), i.e. it has at most \(C_g\) occupied cells (SA 17744). A chain beginning at an event and continuing through nodes with exactly one predecessor, no new cell and no intervening mark has at most \(T_t=C_TR_t\) light nodes if it begins at \(t\). Every leaf has a created cell; predecessors have lower levels and successors are unique. Cut islands are leaves with at most \(N_{\rm cut}\) cells.

The outer record has a connected set of active addresses in a graph of fixed degree bound \(D\ge1\), with root fixed by \(X\); an address includes its level and spatial cell. Its volume (6) is determined by that set and is at least its cardinality. At each fixed address set the number of non-frame codes is at most \(e^{b_{\rm code}V^\circ}\). Every free frame choice is accompanied by its factor \(w^{-1}\). These are the coding hypotheses needed for Lemma 9; a bound at each *exact real value* of \(V^\circ\) is not a bound on a unit volume bin. The source-volume comparison following (6) is also part of H-G.

**Outstanding — actual genealogy.** The supplied local geometry and [geo5c-count.md](geo5c-count.md) do not verify (14), the waiting rule and this coding map for all actual histories. The relevant SA arguments are 17719–17762 and 18416–18715; these are imported geometric statements here.

**H-C (test certificates and owned gains, BG1/PR1/LF1).** The regular branch of the four-dimensional averaging map satisfies
\[
 f_{\mathcal MW}(p')\le\sum_p W(p',p)f_W(p)
           +C_{\rm SO}\max_{p\subset Y(p')}f_W(p)^2
 \quad\text{if }\max_{p\subset Y(p')}f_W(p)\le\varpi_L,               \tag{15}
\]
and agrees there with the globally defined real average. Here \(B(y)\) is the block of fine sites assigned to the coarse site \(y\), \(Y(p')\) is the union of the four corner blocks, and
\(W(p',p)=L^{-4}\#\{x\in B(y_1):p\in S_x(p')\}\), where, for \(p'\) in plane \(\mu\nu\),
\(S_x(p')=\{p_{\mu\nu}(x+ie_\mu+je_\nu):0\le i,j<L\}\).

Every failed total plaquette/background test has a plaquette witness \(f_{V_t}\ge c_{\rm lin}\epsilon_t\) in an owned neighbourhood containing its entire averaging cone. Failed approximate-fluctuation tests have the action-plus-gauge certificate of SA 18287–18301; failed kept-coordinate tests have the coercive-form certificate of SA 18303–18327. After bounded overlaps and exponent splitting, these give a gain \(c_GP_t^2\) per created cell. A renewed mark has gain \(P_t/2\) from a new window outside the old floor. The cut island's last ordinary plaquette failure is an unused witness, excluded from its own mass, giving \(c_wP_t^2\); it pays all at most \(N_{\rm cut}\) artificial leaf cells and a mark, by taking \(c_G\le c_w/(2N_{\rm cut})\) and then increasing \(X_0\). Distinct paid gains use disjoint or explicitly bounded-overlap shares, whose Wilson coefficients have a fixed positive ratio to \(\theta_t\). Stored averages are those read by the tests.

**Outstanding — certificates.** Totality alone does not prove the contrapositive certificate for failure of existence. The four-dimensional estimate (15), the cut-form comparison, renewed-window payment and cut-island ownership must be established for the actual maps. The proof of YM3 Lemma I-10-97 is three-dimensional; Lemma 6 below checks the four-dimensional counting and iteration, not the missing nonlinear estimate (15).

**H-E (common envelopes and later admission, LF1(4)/ST1).** The prepared operation has a real Borel scalar part and finitely many carrier exponents, Borel in stored variables, holomorphic on the external creation domain, real at real pairs and gauge invariant factor by factor. At every creation and on the union of all compatible drop-out fibres there is a nonnegative Borel envelope \(G_{\omega^\circ}(\xi^\circ;\xi_{\rm in})\), independent of the external evaluation, with
\[
\begin{split}
 \sup_{\rm allowed\ evaluations}|I_\omega|
 &\le \pi_{\rm int}(\omega^\circ)e^{C_{\rm env}V^\circ-\sum_e\Gamma_e}\,
      G_{\omega^\circ}(\xi^\circ;\xi_{\rm in})
          \prod_y\frac{m_{\omega_y}(\xi_y)}w,\\
 \sup_{\xi_{\rm in}}\int G_{\omega^\circ}\,d\mu^\circ
 &\le e^{C_{\rm int}V^\circ}.                                      \tag{16}
\end{split}
\]
Here \(m_{\omega_y}\) is the supremum in (7) on the inner island's fixed creation domain; \(\Gamma_e\) are the owned gains of H-C. If there are \(f(\omega^\circ)\) internal free outer-frame choices, \(\pi_{\rm int}=w^{-f(\omega^\circ)}\), and the outer weight including (7) is \(\pi_{\rm out}=w^{-1}\pi_{\rm int}\). H-G requires their normalized sum at a fixed non-frame code to be at most one. Every later inner read belongs to that full creation domain. The stored-variable measures factor as required by (16); all Jacobians and normalizers are included. The same hypotheses apply to an unoperated component, with fixed exterior variables and without an operation at the root.

**Outstanding — common domination.** The prepared modulus bound of [gates/sa-2.8-terms-gate.md](../gates/sa-2.8-terms-gate.md) does not prove (16) over evaluation fibres. Bounds of the form \(\sup_p\int G_p<\infty\) do not imply \(\int\sup_pG_p<\infty\): \(G_p(b)=e^{-(b-p)^2}\) has a constant integral but \(\sup_{p\in\mathbb R}G_p(b)=1\). Injective triangular coordinates and their uniformity must be supplied, not inferred from a determinant bound. Lemma 7 states exactly what fixed-evaluation integration does prove.

**Outstanding — full admission.** The numerical support estimate
\[
 \frac{C_{\rm sup}R_j^2\epsilon_j}{\alpha_{0,j}}
 \le C_{\rm sup}L^2(A_0/C_0)(\log\theta_j)^{2r+p_0-q}\longrightarrow0 \tag{17}
\]
controls curvature/current room when \(q>p_0+2r\). It does not construct the gauges, potential bounds or towers in R4–R6. Even at a real pair with zero fluctuation these other domain conditions remain. H-E requires their independent verification at every later read.

**H-O (oscillation, LF1/ST1).** Newly created operations preserve
\[
 \sum_{f:R_f=R}\operatorname{osc}\Phi_{\omega,f}
 \le B_\Phi(\log\theta_i)^{2p_0}
                 e^{-\kappa d_i^\natural(\mathcal S;R)}              \tag{18}
\]
on their fixed creation domains, with \(B_\Phi\) fixed before \(\gamma\).
**Outstanding:** this is SA R25 (6291–6310). Neither the mass estimate nor a bound on \(\operatorname{Re}\Psi\) implies (18); draft D.6 did not check it.

**H-SUM (healing, labels and the floor, LF1(5)–(6)).** The actual healed sum is exact and preserves the H-SF structure. For its specified nonnegative missing-vacuum/reserve charge \(W(\mathcal S)\), the loaded-label bound is
\(\sum_{\mathcal S}|e^{\mathcal E_{\mathcal S}}\tau_{\mathcal S}|(\mathcal V_k)e^{W(\mathcal S)}
\le e^{C_{\rm lab}N_k^{\rm site}}\);
here the absolute value is total variation on the retained configuration space, including the internal majorants. At zero source, after the prescribed vacuum normalization \(e^{-\mathcal E_k}\), the all-small-field term has density at least
\(\chi_k(V)e^{-x_kA(U_k(V))-C_{\rm sf}N_k^{\rm site}}\).
For some \(c_{\rm ball}>0\), the link ball of radius \(c_{\rm ball}x_k^{-1/2}\) passes every test and
\(A(U_k(V))\le C_{\rm act}c_{\rm ball}^2x_k^{-1}N_k^{\rm site}\) there.
All constants are uniform in level, torus and cutoff. Here \(N_k^{\rm site}\) is the number of sites, distinct from the waiting depth \(N_k\).

**Outstanding — sums and stability.** These are separate imports. The per-history mass argument does not alone establish the loaded-label sum or the link-ball hypothesis. SA 19766–19807 makes this distinction explicit.

**The class \(\mathfrak L_k(\theta)\).** Its elements are complete presentations: the weights \(x_j\), the pointed families and companions \((E^{(j)},\widehat E^{(j)},b_j)\), remainders, boundary slots, and stored operations through level \(k\), with their specified domains, kernels and normalization factors. Their represented measures are the exact history sums specified by H-LF; an array of numerical bounds without those kernels is not a presentation. Require (3), the bounds \(\|E^{(j)}\|\le E_0,\ \|R^{(j)}\|\le\theta_j^{-\kappa_0/2}\) and the boundary bound in (12), the own-coefficient/age structure (5), (13), and identification with the whole-lattice families formed from the earlier entries. Require analyticity, reality, gauge invariance, lattice covariance and companion coherence. Each island has a positive Borel stored measure, Borel dependence on stored variables, analytic external dependence, factorwise gauge invariance, (18), and
\(\mathfrak M_c(i,X)\le e^{-(2-\varepsilon_{\rm rar})P_i-\kappa_1|X|_i}\)
at its creation level \(i\). Every later read is admitted there. Physical real terms are nonnegative; positivity is not imposed at complex sources. The bare presentation has only \(x_0=\beta\) and Wilson density, with no regular terms or islands.

## Constant order

The following order is part of the hypotheses on the imported packages. A returned constant must precede every choice it bounds. The imported floors and ceilings must be uniform over the earlier admissible choices. This does not assert that all those imports have been proved.

| Order | Choice and dependence |
|---|---|
| 1 | Fix the desired reserve \(c_r\), rarity loss \(0<\varepsilon_{\rm rar}<1\), margins, Hölder exponent and finitely many source/age requirements. Fix the power-count constants before \(r\ge2,p_0,p_1,q,\kappa_0\): \(p_0>6r,\ p_0>3Cr,\ (p_0+Cr)/2<p_1<p_0-Cr,\ q>\max(p_0+2r,Cp_0),\ \kappa_0>\max(8,C)\). |
| 2 | Fix the scale-independent geometric and hull constants, \(\lambda_0,\sigma_0,\varepsilon_{\rm rate},g_*\); choose odd \(L\) with \(L>4C_h^{\rm WF}C_h^{\rm UM}c_\ell(1+4\beta_s)\). Then choose flat and averaging constants, \(c_0,c_2\), and the weak triple (1). |
| 3 | In the order of c4-order rows 4–7: local gauges/inverses and reference ceilings; propagator/profile/walk rates; local walk size \(M_1\), reset scale \(R_1\), gap \(\rho=R_1M_1\); then seam, A2/A3 and tower bounds and radii. The local walk size is distinct from \(M\). |
| 4 | H-M's early \(K_0,H_0,b,d,C_\tau\); Gaussian constants \(A=A_{K_0},\varepsilon_0,\rho_0\); geometric \(P,c_m\); fix \(W_0\) by (22). Choose \(\kappa\), then \(\Theta\), then \(\lambda\) in (24). |
| 5 | Choose \(\bar\kappa,\kappa_1\) above their entropy, bracket and response floors; \(R_s=e^{\bar\kappa}\). Next response-parameter length and small decoupled radii, \(M'_1,M_2\), preparation/profile constants, \(\Theta_1,\varpi_T\); then \(M\), a power of \(L\), meeting (23) and all collar/tower floors. |
| 6 | Choose post-\(M\) box, joint-chart, comparison and reference-cutoff constants; set \(\gamma_{\rm tilt}\) by (22). Choose \(A_1\), then \(A_0\); \(C_0\), then \(C_1\); absolute radii and current ceilings within (23). Fix all radius ratios and response-room/age constants. |
| 7 | Fix \(E_N,C_E,C_{\rm rad},f_\nu\); set \(E_0=E_N+1\), then \(N_*=E_0\sum_{\nu\ge1}f_\nu+1\). Choose the boundary-origin maximum \(\mathsf B\), then volume costs. Fix \(c_{\rm lin}\) and the H-C certificate constants, then \(C_g,s_0,C_T,N_{\rm cut},c_w\), then \(c_G\); \(C_{\rm env},C_{\rm int},b_{\rm code},D\), then \(c_{\rm ent}\); the source-volume factor \(C_v\), then \(c=C_vc_r\). Fix \(B_\Phi\) and finally \(c_1\ge c+C_{\rm env}+C_{\rm int}+c_{\rm ent}+c_{\mathsf B}\), where \(c_{\mathsf B}\) is the interior volume cost of the boundary maximum (Lemma 5). Also listed from c4-order: \(L^2\ge6\sqrt2\lambda_a\) (row 2), \(\kappa/4>\kappa_D\) and \(\kappa\)'s history-entropy floor (row 4). |
| 8 | All remaining prepared-form, source, label/floor and flow-error constants, including \(c_{\rm tail},C_{\rm lab},C_{\rm sf},C_{\rm act},c_{\rm ball},C_f,C_v^{\rm flow}\), and tube constants precede \(X_0\). The GEO5(c) exponent \(d_0\) follows \(L,r,\overline B\), not the other way round. |
| 9 | Increase \(X_0\) to meet all listed smallness, frame, tail, ledger, admission and list-size requirements; set \(\gamma=X_0^{-1/2}\). Compute \(\varsigma,\lambda_\sharp,B_\sharp\) from (25). Stronger requested source ceilings may decrease the allowed coupling, without redefining the early constants. |
| 10 | Choose \(0<g\le\gamma\), an admissible torus/grid, and \(\beta\ge g^{-2}+B_\sharp\). Form the next coefficient before choosing the next frame entry. |

Rows 3, 5–8 retain the internal dependency order of [c4-order.md](c4-order.md); they do not move later package constants into an earlier bound. A radius window is feasible, for example, by setting \(a_1=t,\ a_0=t/(2D_*)\) with \(D_*>CM\), and then taking \(t>0\) small: \(CMa_0<a_1,\ a_1^2\le Ca_0\). Inner radii are chosen afterwards. The running radii (2) fit these fixed absolute ceilings by increasing \(X_0\).

## Hand proofs

**Lemma 1 (weighted resolvent and inverse root).** Let finite coordinate sets, with integer-valued lattice distance \(d\) (allowing distinct coordinates at one site), satisfy
\(\#\{y:d(x,y)\le n\}\le n_c(2n+1)^4\). Define
\[
 V(\nu)=\sum_{n\ge0}n_c(2n+1)^4e^{-\nu n},\qquad
 \|B\|_\mu=\max\{\sup_x\sum_y,\sup_y\sum_x\}|B_{xy}|e^{\mu d(x,y)}.
\]
Suppose \(a,\mu'>0\), \(H'<\infty\), \(B\) is complex symmetric, \(\operatorname{Re}\langle v,Bv\rangle\ge a|v|^2\), and \(\|B\|_{\mu'}\le H'\). Put
\(\mu_1=\min\{\mu'/2,ea\mu'/(4H')\}\). Then
\[
 |(\zeta+B)^{-1}_{xy}|\le\frac{e^{-\mu_1d(x,y)}}{\zeta+a/2},
 \quad
 R(B)=\frac1\pi\int_0^\infty\zeta^{-1/2}(\zeta+B)^{-1}\,d\zeta,
 \quad |R(B)_{xy}|\le\sqrt{2/a}\,e^{-\mu_1d(x,y)}.                   \tag{19}
\]
The root is symmetric, holomorphic, and \(R(B)^2=B^{-1}\). For two matrices satisfying the same bounds,
\[
 |(R(B)-R(B'))_{xy}|
 \le \tfrac12(2/a)^{3/2}V(\mu_1/2)^2
          \|B-B'\|_{\mu'}\,e^{-(\mu_1/2)d(x,y)}.
\]

*Proof.* Conjugate by the diagonal multiplier \(e^{\mu d(x,z)}\).
The difference from \(B\) has row and column sums at most
\(\mu H'/[e(\mu'-\mu)]\), using
\(|e^t-1|\le |t|e^{|t|}\) and
\(\sup_{s\ge0}s e^{-(\mu'-\mu)s}=1/[e(\mu'-\mu)]\).
At \(\mu=\mu_1\) this is at most \(a/2\). Accretivity and a Neumann perturbation of the resolvent give norm at most \((\zeta+a/2)^{-1}\); take \(z=y\) to obtain the entry bound. The integral of
\(\pi^{-1}\zeta^{-1/2}(\zeta+a/2)^{-1}\) is \(\sqrt{2/a}\).
The scalar identity on the right half-plane and holomorphic functional calculus give the root identity; the integral gives transpose symmetry and holomorphy directly. For the difference, insert the resolvent identity. Split the three successive distances at rate \(\mu_1/2\), take out \(e^{-\mu_1d(x,y)/2}\), and sum the two intermediate coordinates using \(V(\mu_1/2)^2\).
Finally
\(\pi^{-1}\int_0^\infty\zeta^{-1/2}(\zeta+a/2)^{-2}d\zeta
=\tfrac12(2/a)^{3/2}\).
These arguments are uniform in dimension. \(\square\)

**Lemma 2 (what path decoupling proves).** Let a full matrix \(A(P)\) be holomorphic, symmetric and globally accretive with gap \(a\), real at a reference pair, and
\[
 |A(P)_{xy}|\le He^{-\mu_0d(x,y)},\quad
 |(A(P)-A_{\rm ref})_{xy}|\le\eta e^{-\mu_0d(x,y)}.
\]
Let \(Z_0^\sharp\) be a collar of \(Z_0\) with distance at least \(M\) to its complement. Fix a symmetric choice of lattice geodesic for each pair. On cubes of side \(\ell=LM\) outside the collar, put one parameter on each cube visited by that path, and define
\[
 B^s_{xy}=B_{xy}\prod_{\Delta\in D(x,y)}s_\Delta,\quad
 C=(\chi A(P)^s\chi)^{-1},\quad
 \Gamma=-\chi A(P)^s(1-\chi)R(A(P))^s,\qquad \chi=1_{Z_0}.            \tag{20}
\]
There are \(K_0,H_0,\mu_2>0\), depending only on \(a,H,\mu_0,n_c\), such that, if
\[
 M\ge128\bar\kappa/\mu_2,\quad
 2HV(\mu_0/2)e^{16\bar\kappa-\mu_0M/4}\le a/4,
\]
then on \(|s_\Delta|\le e^{\bar\kappa}\), the reference
\((C_*,\Gamma_*)=(C(0;{\rm ref}),\Gamma(0;{\rm ref}))\) is real,
\[
 C_*>0,\quad \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\quad
 \|C-C_*\|+\|\Gamma-\Gamma_*\|
       \le H_0(e^{32\bar\kappa-\mu_2M/4}+\eta).                     \tag{21}
\]
At \(s=1\), \(C+C\Gamma\Gamma^TC=\chi A(P)^{-1}\chi\). Zero walls separate this covariance into blocks.

*Proof.* Apply Lemma 1 with \(\mu'=\mu_0/2,\ H'=HV(\mu_0/2)\) and take \(\mu_2=\mu_1/2\). A geodesic segment of at most \(\ell\) sites meets at most \(16\) such cubes, hence
\(|D(x,y)|\le16(1+d(x,y)/\ell)\).
A varied path starting in \(Z_0\) has length at least \(M\); for the product of the two paths in \(\Gamma\), any variation forces their total length to be at least \(M\).
Thus a parameter product on one or two paths of total length \(t\) costs at most \(e^{32\bar\kappa}e^{\mu_2t/4}\). Its difference from the zero-parameter product vanishes unless \(t\ge M\).

For the compression, summing
\(2He^{16\bar\kappa-\mu_0M/4}e^{-\mu_0d/2}\)
gives a perturbation at most \(a/4\). It remains accretive with gap \(3a/4\), so \(\|C\|\le4/(3a)\).
At the reference, \(C_*^{-1}\) has norm at most \(HV(\mu_0)\), and
\(\|\Gamma_*\|\le HV(\mu_0)\sqrt{2/a}\,V(\mu_1)\);
their sum with \(4/(3a)\), enlarged to at least one, is an early \(K_0\).
The inverse identity bounds \(C-C_*\) by
\[
 (4/(3a))^2 V(\mu_0/2)
       \{\eta+2He^{16\bar\kappa-\mu_0M/4}\}.
\]
For \(\Gamma-\Gamma_*\), split the difference into variation of \(A,R\), and variation of the two parameter products. Lemma 1 bounds the first integrand by
\(H_1\eta e^{-\mu_2(d_1+d_2)}\) before parameter weights, where
\[
 H_1=\sqrt{2/a}+\tfrac12H(2/a)^{3/2}V(\mu_1/2)^2V(\mu_0/2).
\]
The second is at most
\(2H\sqrt{2/a}\,e^{32\bar\kappa-\mu_2M/4}
 e^{-\mu_2(d_1+d_2)/2}\).
The assumed floor absorbs the parameter weights in the first term. Summing the intermediate point and then using the Schur test costs at most \(V(\mu_2/4)^2\). The sum of these displayed constants gives \(H_0\), independent of \(M,\bar\kappa\).

At \(s=1\), block inversion and \(R(A)R(A)^T=A^{-1}\) give the stated identity. Across a zero wall, each entry of \(A^s\) vanishes. A nonzero cross term of \(\Gamma\Gamma^T\) would concatenate four uncut paths across that wall, which is impossible. This proves block factorization. \(\square\)

**Outstanding — heredity is stronger than block factorization.** The entries of \(R(A)\) in (20) still depend on the full exterior matrix after the path weights are set to zero. For example take \(A=I-T\) on a three-site chain, \(T_{12}=t,\ T_{23}=u\), \(0<t,u<1/4\), \(Z_0=\{1\}\), collar \(\{1,2\}\), and cut site \(3\). Then \(C=1\) and the local covariance is
\(1+t^2(R_{21}^2+R_{22}^2)\).
The convergent expansion
\(R=(I-T)^{-1/2}=\sum_{n\ge0}\binom{2n}{n}T^n/4^n\)
has nonnegative coefficients and
\(R_{22}=1+\tfrac38(t^2+u^2)+\cdots\); thus the purported local covariance depends on the exterior edge \(u\). Longer chains with all edge weights below \(1/4\) retain a uniform gap and nearest-neighbour bounds. A closed walk from site \(2\) to the exterior edge and back contributes positively to \(R_{22}\), placing this dependence beyond collars meeting arbitrarily large \(M\) floors. This does not refute (21); it refutes inferring carrier heredity from this construction. Moreover its inverse root explicitly uses a global gap. The source's locally gapped mutilated form cannot be substituted without an additional proof.

**Lemma 3 (conditional UM budget and simultaneous choice).** Under H-M, its scalar budget can be bounded by one before choosing \(\bar\kappa,M\). In particular the displayed IN1 conditions have the constant order above, provided the other imported constraints have the stated floor/ceiling order.

*Proof.* Enlarge the Gaussian/count bounds so \(A,P,c_m\ge1\). Put \(D_0=A c_mL^4\), and choose
\[
 W_0=\min\{[3PL^4(1+Ac_m)]^{-1},\,\rho_0/(2P)\},\quad
 \varepsilon_*=\min\{\varepsilon_0,(3D_0M^4)^{-1}\},\quad
 \gamma_{\rm tilt}=\min\{2/(3D_0M^4),\rho_0\}.                       \tag{22}
\]
Only the first choice precedes \(M\). Take \(M\) large and the later radii and tube small enough that
\[
 H_0e^{b\bar\kappa-dM}\le\varepsilon_*/2,\qquad
 H_0H_p(M)(a_0+a_1+j_0)+C_\tau|\tau-1|\le\varepsilon_*/2.            \tag{23}
\]
The first inequality is a floor on \(M\), since \(M^4e^{-dM}\to0\), as follows already from \(e^{dM}\ge(dM)^5/5!\). The second is a later radius/tube ceiling. UM14 holds because \(PW_0M^{-4}+\gamma_{\rm tilt}/2\le\rho_0\), and its UM15 cost satisfies
\[
 C_0^{\rm UM}=PL^4W_0(1+Ac_m)
            +D_0M^4(\varepsilon+\gamma_{\rm tilt}/2)\le1.
\]
Consequently set
\[
 \Theta=C_h^{\rm UM}\{3+c_\ell[(1+4\beta_s)\kappa+g_*]\},\qquad
 \lambda_0+\sigma_0+\Theta/L\le\lambda<
              \kappa/(2C_h^{\rm WF})-\varepsilon_{\rm rate}.         \tag{24}
\]
The floor on \(L\) makes the upper endpoint grow faster in \(\kappa\) than the lower endpoint, so the window is nonempty for large \(\kappa\). Next choose \(\bar\kappa\) above the response/bracket floors and with \(\log(e^{\bar\kappa}-1)\ge\Theta\), then \(M\).
The failed-bond condition is the explicit later floor
\[
 \mathfrak b^2\ge(2/\gamma_{\rm tilt})
       \{\Theta+\log(4c_b(LM)^4)\};
\]
the scaled box \(\mathfrak b\) grows proportionally to \((\log\theta)^{p_0}\).
The UM insertion allowance
\(a_*=\min\{W_0/2,(4e^\Theta A_a)^{-1}\}>0\)
has fixed \(A_a=2c_fL^4S_{\sigma_0}/W_0\). Imported formation must make the actual insertion size tend to zero; \(s_j\to0\) pays a first-difference contribution, but cannot by itself prove that formation statement.

All remaining displayed smallness requirements are finitely many ceilings after their constants. An ordered finite list of choices is satisfiable when each upward choice has finitely many floors, each downward choice has finitely many strictly positive ceilings, each window has nonempty intersection, and each determined choice satisfies its conditions identically: proceed in order, taking the maximum floor or minimum ceiling. This proves the claimed simultaneous *conditional* choice, not the missing H-M or formation theorem. \(\square\)

**Lemma 4 (flow, without next-step existence).** Suppose (10)–(11) hold along a formed segment with \(\theta=x\) and \(x_i\ge X_0\) at the inputs. Define
\[
 \varsigma=\sup_{x\ge X_0}u(x)\le\min(c_0/4,1),\quad
 \lambda_\sharp=c_0-\varsigma,\quad B_\sharp=c_0+2c_2+\varsigma.       \tag{25}
\]
Then
\[
 \lambda_\sharp(j-i)-c_5\le x_i-x_j\le B_\sharp(j-i),\qquad
 b_{i+1}\le B_\sharp.                                              \tag{26}
\]

*Proof.* Set \(a_j=\mathcal A_j-jc_0\). Summing the recursion gives
\(x_i-x_j=c_0(j-i)+a_j-a_i+\sum_{i<l\le j}e_l\).
Here \(|a_j-a_i|\le2c_2\). This gives the lower bound and
\((c_0+\varsigma)(j-i)+2c_2\) as an upper bound; for \(j>i\) the latter is at most \(B_\sharp(j-i)\). The case \(i=j\) is immediate. The error envelope tends to zero as \(X_0\to\infty\), so (25) is a legitimate last ceiling. Since \(\lambda_\sharp\ge3c_0/4\) and \(B_\sharp<\overline B\), (26) supplies the weak triple. No sign of an individual increment is asserted, and no next step is constructed by this calculation. \(\square\)

**Lemma 5 (uniform input and return of the regular bound).** Assume H-SF's list estimates (12)–(13) and the class bounds on its input. For any frame (1), sufficiently large \(X_0\) gives
\[
\begin{split}
 w_{n,j}&\le2C_{\rm rad}(n-j+2),\\
 \sum_{j\le n}w_{n,j}\theta_j^{-\kappa_0/2}
 &\le \rho_R(X_0):=
 2^{1+\kappa_0/2}C_{\rm rad}\sum_{m\ge0}(m+2)
                         (X_0+\underline\lambda m)^{-\kappa_0/2}
 \longrightarrow0.                                               \tag{27}
\end{split}
\]
Thus the list size is at most \(N_*\) and (12) returns \(E_0=E_N+1\), uniformly in its length.

*Proof.* With \(m=n-j\), \(\theta_j/\theta_n\le1+\overline Bm/X_0\) and \(\theta_n\le\theta_j+c_5\).
Therefore
\[
 (\log\theta_n/\log\theta_j)^{2q}
 \le\exp[2qc_5/(X_0\log X_0)]\le2.
\]
Use \(\overline B/X_0\le1\) in (13).
Also \(\theta_j\ge X_0+\underline\lambda m-c_5
\ge\tfrac12(X_0+\underline\lambda m)\) when \(X_0\ge2c_5\).
The series in (27) is dominated by a constant times
\((m+2)(1+\underline\lambda m)^{-\kappa_0/2}\), which is summable because \(\kappa_0>4\). Each term tends to zero, proving the limit by dominated convergence.
Consequently
\(\sum_{j\le n} f_{n+1-j}\|E^{(j)}\|+
\sum_{j\le n}w_{n,j}\|R^{(j)}\|
\le E_0\sum f_\nu+1=N_*\).
Choose \(X_0\) further so that the supremum of the correction in (12) is at most one. Its factors tend to zero with all \(E_0,N_*\) already fixed. The boundary maximum is chosen first; its vanishing difference and long-domain factors are handled by the same last ceiling, and its interior volume cost is included later in \(c_1\). There is no dependence of an earlier returned bound on \(X_0\). \(\square\)

**Lemma 6 (four-dimensional averaging and the plaquette certificate).** Assume (15). For a single level-\(t\) plaquette \(p'\), let \(\mathcal N_l(p')\) be the level-\(l\) plaquettes whose corners lie in its four ancestor corner blocks. Define \(\mathcal N_l(S)=\bigcup_{p'\in S}\mathcal N_l(p')\) and \(\mathcal N_t(S)=S\), using consistent lifts on an admissible torus. Enlarge \(C_{\rm SO}\) to at least one and set
\[
 e_L=\min\{\varpi_L^2/4,(108C_{\rm SO})^{-2}\},\qquad e_*=e_L/2.
\]
For any real configuration \(U\),
\[
 \sum_{\mathcal N_0(S)}a_p(U)\ge
       \min\left\{\tfrac18\sum_{p'\in S}
                  f_{\mathcal M^tU}(p')^2,e_*\right\}.              \tag{28}
\]
If the left side is below \(e_*\), all required averages are on their regular branch. With H-C's witness and owned-cone hypotheses, a failed plaquette/background test pays \(c_GP_t^2\) after the declared splitting and overlap losses.

*Proof.* Each row of \(W\) sums to \(L^2\): there are \(L^4\) offsets and \(L^2\) plaquettes per surface. For a fixed fine plaquette and each of its \(L^2\) possible surface offsets, its starting point belongs to exactly one block. Thus each column sums to \(L^{-2}\). Hence
\(\|W\|_{2\to2}\le1,\ \|W\|_{1\to1}\le L^{-2}\), and a product of \(h\) kernels has \(1\to2\) norm at most \(L^{-2h}\).
A fine plaquette belongs to at most \(24\) cones of any fixed higher level: the block of its base point must be a corner of the higher plaquette, and a site is a corner of four plaquettes in each of six planes.

The cones have the required recursion. For a single top plaquette their site box has \(2L^{t-l}\) sites in its two directions and \(L^{t-l}\) in each other direction. For \(l<t-1\), let \(s\) be a fine plaquette's base and \(R_\rho\) the corresponding box side after one blocking. Choose the intermediate base
\(q_\rho=\min\{\lfloor s_\rho/L\rfloor,R_\rho-2\}\)
in the two directions of that fine plaquette, and
\(q_\rho=\lfloor s_\rho/L\rfloor\) in the other directions, after translating the box origin to zero. All its corners are in the intermediate box, and its corner blocks contain the original fine plaquette. The reverse inclusion follows from nested blocks. The last step is the definition of the one-step cone. Taking unions proves the recursion for \(S\).

Put \(E_l=\sum_{\mathcal N_l(S)}f_{\mathcal M^lU}^2\).
The error in (15) has \(\ell^1\) norm at most \(24C_{\rm SO}E_l\) by the cone count. Iterating nonnegative kernels, while the local charts are valid, gives
\[
 \sqrt{E_m}\le\sqrt{E_0}+
       24C_{\rm SO}\sum_{l<m}L^{-2(m-1-l)}E_l .
\]
If \(E_0\le e_L\), induction gives \(E_l\le4E_0\):
the right side is at most
\(\sqrt{E_0}+108C_{\rm SO}E_0\le2\sqrt{E_0}\),
since \(\sum_{h\ge0}L^{-2h}\le9/8\).
At each step the maximum curvature is at most \(2\sqrt{E_0}\le\varpi_L\), so (15) and branch agreement remain available. Since \(E_0=2\sum a_p\), this proves (28) in the small-energy case; otherwise the \(e_*\) alternative proves it.

For a witness \(f_{V_t}\ge c_{\rm lin}\epsilon_t\), take \(S\) to be that plaquette. Bound the first entry of the minimum from below by \(c_{\rm lin}^2\epsilon_t^2/8\). This lower bound is below \(e_*\) when \(X_0\) is large, so the action is at least \(c_{\rm lin}^2\epsilon_t^2/8\).
By (1), (3), \(x_{t-1}\ge\tfrac34(\theta_t-c_5)\ge\theta_t/2\).
Multiplying its owned action by \(x_{t-1}\) gives at least
\((c_{\rm lin}^2/16)P_t^2\). For general carrying weights, H-C's fixed positive lower ratio to \(\theta_t\) replaces the factor \(1/2\). That ratio, splitting and bounded overlap are absorbed in the fixed \(c_G\).
For the other certificates H-C gives respectively a multiple of
\(x_{t-1}\delta_{t-1}^2\) or \((\delta_{t-1}/g_{t-1})^2\); these are fixed multiples of \(P_{t-1}^2\), and \(P_{t-1}\ge P_t/2\) for large \(X_0\). Renewed marks remain the separate H-C input. \(\square\)

**Lemma 7 (the local integration prices).** If \(0<\epsilon\le1\) and \(\theta\epsilon^2\ge1\), then
\[
 c_z\theta^{-3/2}\le
 z(\theta,\epsilon):=\int_{\|u-1\|<\epsilon}
          e^{-\theta(1-\frac12\operatorname{Tr}u)}\,du
 \le C_z\theta^{-3/2},                                              \tag{29}
\]
with universal positive constants. The full half-exponent integral is at most a universal multiple of \(z(\theta,\epsilon)\).
Separately, suppose stored coordinates \(b_1,\ldots,b_n\) have dimensions \(d_j\), and \(A_j=A_j(b_j;b_{j+1},\ldots,b_n)\) is, for each fixed later tuple, an injective \(C^1\) map on its integration domain with
\(|\det\partial_{b_j}A_j|^{-1}\le J_0^{d_j}\).
Then for \(\kappa_{\rm pos}>0\),
\[
 \int\exp[-\tfrac12\kappa_{\rm pos}\sum_j|A_j|^2]\prod_jdb_j
 \le J_0^{\sum d_j}(2\pi/\kappa_{\rm pos})^{\sum d_j/2}.              \tag{30}
\]

*Proof.* Write \(u=\cos\phi+i\sin\phi\,n\cdot\sigma\). The Haar density for class functions is \((2/\pi)\sin^2\phi\,d\phi\).
On \(0\le\phi\le\pi\),
\(\sin\phi\le\phi\) and \(1-\cos\phi\ge2\phi^2/\pi^2\), giving
\(C_z=(2/\pi)(\sqrt\pi/4)(\pi^2/2)^{3/2}\).
On \(0\le\phi<\theta^{-1/2}\le\epsilon\le1\), the cutoff holds,
\(\sin\phi\ge2\phi/\pi\), and \(\theta(1-\cos\phi)\le1/2\);
thus \(c_z=8e^{-1/2}/(3\pi^3)\) works. Apply the upper estimate with \(\theta/2\) for the half-exponent comparison.
For (30), integrate \(b_1\) first, change variables injectively to \(A_1\), enlarge its image to \(\mathbb R^{d_1}\), and obtain \(J_0^{d_1}(2\pi/\kappa_{\rm pos})^{d_1/2}\), independently of the later tuple. Repeat and use Tonelli. These are fixed-evaluation estimates. They imply the second line of (16) only when a *single* envelope, with these properties uniformly over the evaluations, has already been constructed. \(\square\)

**Lemma 8 (genealogy count and paid reserve).** Assume H-G, the frame and tube conditions (1)–(3), H-C's owned gains, and \(p_0>6r\). For any nonincreasing nonnegative sequence \(\widehat r_n\),
\[
 \sum_{u\in{\rm Gen}}\widehat r_{n(u)}|C(u)|
 \le C_{\rm cnt}\sum_t(n_t^{\rm cr}+n_t^{\rm mk})T_t\widehat r_t,
 \quad C_{\rm cnt}=2C_g(5C_g+1)+4C_g^2s_0.                          \tag{31}
\]
For every fixed \(c_1,\kappa_1\ge0\), increasing \(X_0\) then gives
\[
 \sum_e\Gamma_e
 \ge c_1V^\circ+\kappa_1\sum_{u\ {\rm outer}}|C(u)|
                     +(2-\varepsilon_{\rm rar})P_i                \tag{32}
\]
for an outer record rooted at level \(i\).

*Proof.* Write \(O=\sum_n\widehat r_no_n\) and \(Q=\sum_n\widehat r_nl_n\). Multiply (14) by \(\widehat r_n\), sum, and use its monotonicity; each created cell is counted at most \(s_0\) times. Then
\(O\le2C_gQ+2C_gs_0\sum_t\widehat r_tn_t^{\rm cr}\).
The first line of (14) bounds the left side of (31) by
\(2C_gO+C_g(C_g+1)Q\).

Partition the genealogy into stretches beginning at an own-level creation, a successor of a mark, or a merger. Every light node belongs to one such stretch, so its total cost is at most the sum of \(T_t\widehat r_t\) over these events. Own-level events use a distinct created cell; mark events use that mark's unique successor. At each merger choose a non-first predecessor, then follow first predecessors to a leaf and use its created cell. This assignment is injective among mergers: on the upward path from the assigned leaf, that merger is the first step entering a node through a non-first predecessor. Thus a created cell is used at most twice, a mark at most once. Its level is no later than the event, so it pays the event's larger-level cost. Therefore
\(Q\le2\sum_tn_t^{\rm cr}T_t\widehat r_t+
\sum_tn_t^{\rm mk}T_t\widehat r_t\).
Substitution proves (31), since \(T_t\ge1\).

For (32), (1) gives \(\theta_n\le m_n+c_5\), and (3) gives
\(x_n\le(5/4)(m_n+c_5)\).
For \(X_0\ge\max(e,2c_5)\),
\(1+\log x_n\le4\log m_n\le4R_n\).
Thus the cell cost
\(c_1(1+\log x_n)(MR_n)^4+\kappa_1\)
is bounded by the nonincreasing
\(\widehat r_n=4c_1M^4R_n^5+\kappa_1\).
This corrects the invalid comparison \(\log x_n\le R_n\) without frame slack.
Because \(R_n\le L(\log\theta_n)^r\), \(p_0>6r\) permits the last coupling ceiling to ensure
\[
 c_GP_n^2\ge2P_n+C_{\rm cnt}T_n\widehat r_n,\qquad
 P_n/2\ge C_{\rm cnt}T_n\widehat r_n .
\]
Use (31) to pay every cell cost. The remaining gain is at least
\(2\sum_tP_tn_t^{\rm cr}\). There is a leaf, and for its level \(t\le i\),
\(\theta_t\ge\theta_i-c_5\). Since
\(\log(\theta_i-c_5)\ge\log\theta_i-2c_5/\theta_i\),
one last uniform floor makes \(P_t\ge(1-\varepsilon_{\rm rar}/2)P_i\).
This proves (32). At cut leaves H-C supplies the same artificial creation gains: \(c_wP_t^2\) pays at most \(N_{\rm cut}c_GP_t^2+P_t/2\). No inner mass or old credit is used to pay them. \(\square\)

**Lemma 9 (normalized history entropy).** Under H-G there is \(c_{\rm ent}\), fixed before \(X_0\), for which
\[
 \sum_{\omega^\circ}\pi_{\rm out}(\omega^\circ)
                     e^{-c_{\rm ent}V^\circ(\omega^\circ)}\le1.     \tag{33}
\]

*Proof.* A rooted connected address set of size \(N\) has a canonical spanning-tree traversal of length \(2(N-1)\); its visited set recovers it. A graph of degree \(D\) therefore has at most \(D^{2(N-1)}\) such sets. At a fixed set, normalized frame summation is at most one for each non-frame code, and coding costs at most \(e^{b_{\rm code}V^\circ}\). Since \(V^\circ\ge N\), choose
\(c_{\rm ent}\ge b_{\rm code}+2\log\max(D,1)+\log2\).
The sum is bounded by \(\sum_{N\ge1}2^{-N}=1\).
This argument uses the code and its normalized frames, not an unsupported binning of real volumes. \(\square\)

**Theorem 10 (conditional component mass).** Assume H-LF, H-G, H-C and H-E on a frame and tube satisfying (1)–(3). Fix \(c,\kappa_1\ge0\) and \(0<\varepsilon_{\rm rar}<1\) before \(X_0\). With the stated exponent conditions and order,
\[
 \mathfrak M_c(i,X)\le
            e^{-(2-\varepsilon_{\rm rar})P_i-\kappa_1|X|_i}.         \tag{34}
\]
This holds for passed components, for drop-outs with their carrying factor and fibre supremum, and for the fixed-exterior unoperated components to which H-E applies. Later evaluations preserve it under H-E's full admission hypothesis.

*Proof.* Induct on the finite operation ancestry, which strictly decreases when entering a stored inner operation. Strict spatial inclusion is unnecessary. Choose
\(c_1\ge c+C_{\rm env}+C_{\rm int}+c_{\rm ent}+c_{\mathsf B}\).
For each inner supremum choose a Borel majorant, assigning summable positive error allowances so their total reserve-weighted integral excess is at most \(\eta\) per inner island. Such majorants exist by the upper-integral definition and the inductive finite mass bound. First work with a finite outer-record partial sum; each of its records has finitely many inner islands.

Apply (16) pointwise, then multiply by the additive reserve from (6). Tonelli allows the outer coordinates to be integrated first at fixed inner variables. The second line of (16) contributes \(e^{C_{\rm int}V^\circ}\). Summing each inner record with its own factor \(w^{-1}\) gives at most its mass plus \(\eta\), hence at most \(1+\eta\) by induction. Let \(\eta\) tend to zero in the finite outer sum, then exhaust the countable outer records by nonnegative partial sums. Thus
\[
 \mathfrak M_c(i,X)\le
  \sum_{\omega^\circ}\pi_{\rm out}(\omega^\circ)
    \exp\{(c+C_{\rm env}+C_{\rm int})V^\circ-\sum_e\Gamma_e\}.
\]
Use (32), keeping the root part \(\kappa_1|X|_i\) of its cell sum, then (33). This proves (34).
For a drop-out, (16) already majorizes the supremum over the entire evaluation fibre, with the carrying action and without the root failure's gain. The same calculation applies. For an unoperated component it applies to the stipulated fixed-exterior kernel. An island read later is bounded by its unchanged creation-domain supremum; H-E supplies that inclusion. A larger fixed source reserve is absorbed by increasing \(c_1\) before choosing \(X_0\).

Taking \(\kappa_1\) above rooted cell entropy gives the component decay required for C3 on these classes. The separate global loaded-label assertion remains H-SUM; (34) does not manufacture a missing label count, a missing existence certificate, or an admissible domain. \(\square\)

**Theorem 11 (conditional class step and floor).** Assume H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E and H-O, with their stated order. If
\(\mathfrak P_k\in\mathfrak L_k(\theta)\), the coefficient is formed as in H-SF, \(\theta_{k+1}\) prolongs the frame, and
\(x_{k+1}=x_k-b[\widehat E^{(k+1)}]\) satisfies its tube condition, then the exact step is defined and returns
\(\mathfrak P_{k+1}\in\mathfrak L_{k+1}(\theta)\), with unchanged constants. Include H-SUM when that step performs the healed sum. It preserves the sourced measure separately for every standing part. The bare presentation belongs to \(\mathfrak L_0(\theta)\) whenever its positive \(\beta\) is in the tube. Under H-SUM the physical zero-source partition function also obeys
\[
 e^{-\mathcal E_k}Z_k(0)\ge
       \exp[-(C_{\rm floor}+6\log x_k)N_k^{\rm site}].              \tag{35}
\]

*Proof.* Lemma 3 supplies the conditional UM budget; Lemma 5 supplies the uniform list size and returns the regular bound. H-SF supplies formation, the remainder and boundary bounds, domains, companion identification and the structural subtraction/age estimates. H-LF supplies the measure identity and real positivity. H-SUM supplies the healed resummation if used. Theorem 10 returns the mass bound, H-E supplies later admission, and H-O returns precisely the previously missing oscillation clause. The analytic, Borel, real and covariance requirements are the corresponding assertions of H-SF/H-LF/H-E, not consequences of scalar norm bounds. Earlier stored terms, domains and creation-level bounds are carried unchanged. The next tube condition is an assumption of this theorem, not an output.

At level zero the activity and island clauses are empty; Wilson density is positive, real, gauge invariant and lattice covariant. This proves the base case.
For (35), retain the positive all-small-field term from H-SUM and restrict its integral to the stipulated link ball of radius \(s=c_{\rm ball}x_k^{-1/2}\). The Haar mass of one \(SU(2)\) ball is at least \(c_Hs^3\), as follows by integrating \((2/\pi)\sin^2\phi\) over \(0\le\phi\le s\) for \(s\le1\); \(X_0\ge c_{\rm ball}^2\) ensures \(s\le1\). There are \(4N_k^{\rm site}\) links. The density bound, action bound and product Haar mass give
\[
 e^{-\mathcal E_k}Z_k(0)\ge
 e^{-(C_{\rm sf}+C_{\rm act}c_{\rm ball}^2)N_k^{\rm site}}
       (c_Hc_{\rm ball}^3x_k^{-3/2})^{4N_k^{\rm site}},
\]
which is (35) with the corresponding fixed \(C_{\rm floor}\).
The link-ball acceptance is essential and was imported explicitly. \(\square\)

**Theorem 12 (main theorem: conditional IN1).** Suppose all named imports hold for the actual construction on every admissible finite prefix, with constants and domains ordered as above, and with torus/cutoff-compatible companions. Choose \(X_0\) to meet Lemmas 3–9 and Theorems 10–11, set \(\gamma=X_0^{-1/2}\), and compute (25). For \(0<g\le\gamma\), put \(h=g^{-2}\). For every \(\beta\ge h+B_\sharp\), the actual run with frame \(\theta=x\) exists through
\[
 K(\beta,g)=\min\{k:x_k\le h+B_\sharp\}<\infty .
\]
Every prefix through \(K\) belongs to the same class of Theorem 11 and satisfies (26), the component masses (34) and the conditional floor (35). Its coefficients are independent of admissible torus and unused finer cutoff. Moreover
\[
\begin{gathered}
 h<x_K\le h+B_\sharp,\qquad
 \frac{\beta-h}{B_\sharp}-1\le K
       \le1+\frac{\beta-h-B_\sharp+c_5}{\lambda_\sharp},\\
 \mathcal W_k(g):=\{\beta\ge h+B_\sharp:K(\beta,g)=k\}
       \text{ is nonempty for infinitely many }k,\\
 \frac{\beta}{\log(1/a_K)}
       =\frac{\beta}{K\log L}\longrightarrow\frac{11}{3\pi^2}
 \quad(K\to\infty,\ \beta\in\mathcal W_K(g)),                        \tag{36}
\end{gathered}
\]
uniformly on those sets for fixed \(g\). The theorem asserts neither that every \(\mathcal W_k\) is nonempty nor that individual increments converge or are positive.

*Proof.* Start with the bare presentation and \(\theta_0=x_0=\beta\). Prefixes are constructed on tori large enough for them; their companions make these constructions compatible. The final bound below gives a single physical torus size adequate for every stopping depth.
If a constructed prefix has \(x_k>h+B_\sharp\), first use H-SF to form the next family and coefficient at the current pair. Lemma 4 applies to this newly formed increment because its input exceeds \(X_0\). In particular
\[
 x_{k+1}=x_k-b_{k+1}>h+B_\sharp-B_\sharp=h\ge X_0.
\]
Thus the extended sequence obeys (1), and choosing \(\theta_{k+1}=x_{k+1}\) gives zero tube deviation. Theorem 11 now constructs the next presentation. This finite-prefix induction proves existence without invoking first passage to justify its own final step.
If no stopping index existed, (26) would give
\(x_k\le\beta-\lambda_\sharp k+c_5\) for every \(k\), contradicting \(x_k>h+B_\sharp\). The final displayed inequality prevents overshoot when \(K>0\); when \(K=0\), \(\beta=h+B_\sharp\). The upper bound on \(K\) follows by applying lower drift at \(K-1\); the lower bound follows from \(\beta-x_K\le B_\sharp K\).
Consequently \(K\to\infty\) as \(\beta\to\infty\), and infinitely many stopping sets are nonempty. Companion identification, not the scalar inequalities, gives torus/cutoff independence.

For the last assertion let \(u_*(y)=\sup_{x\ge y}u(x)\), which tends to zero. Reverse drift from \(K\) gives
\[
 x_{l-1}\ge \max\{X_0,h+\lambda_\sharp(K-l+1)-c_5\}.
\]
The error sum divided by \(K\) is therefore bounded by the Cesàro mean of the fixed sequence
\(u_*(\max\{X_0,h+\lambda_\sharp m-c_5\})\), \(1\le m\le K\).
This sequence tends to zero: split any such mean into a fixed finite initial part and a uniformly small tail. Thus
\(\sum_{l\le K}|e_l|=o(K)\), uniformly over the stopping set.
Summing (10)–(11) yields
\(\beta=x_K+c_0K+a_K^{\rm loop}+\sum_{l\le K}e_l\),
where \(|a_K^{\rm loop}|\le c_2\).
The terminal window is bounded for fixed \(g\); division by \(K\log L\) proves (36).

Torus requirements can be chosen consistently with arbitrarily large cutoffs. If the geometric condition is that the level-\(j\) side contain \(2L^{11}MR_j\), choose a compatible physical side \(\ell=2L^m\) such that
\[
 \ell\ge 2L^{12}M\sup_{n\ge0}
       L^{-n}\{\log(h+B_\sharp+B_\sharp n)\}^{r}.
\]
The supremum is finite since an exponential dominates a logarithmic power. For \(n=K-j\), (26) gives
\(x_j\le h+B_\sharp+B_\sharp n\), so
\(\ell L^{K-j}\ge2L^{11}MR_j\).
Additional fixed grid floors from the imported geometry are imposed at the same last choice of \(\ell\). For frames different from \(x\), a next tube condition remains the separate SC1 input; it was not proved by this argument. \(\square\)

## Definitions supplied in distillation

The draft required the following explicit conventions or strengthened input definitions.

1. A uniform tube (3), distinct weak and returned flow constants, a tail error envelope, and distinctions between threshold amplitudes and one-loop primitives, waiting depths and site counts, and the positive analytic-tail rate and optional reserve coefficient.
2. The full hereditary core, companion compatibility, pointed norm, precise coefficient readout and own-tent subtraction, with their mathematical prerequisites retained as imports.
3. The holomorphic Wilson continuation, the weighted matrix norm and summation function \(V\), and the globally gapped auxiliary matrix family, its holomorphic inverse root, path carriers and reference choice; these do not define the actual UM carriers.
4. The outer genealogy cut at islands, artificial cut leaves, fresh-witness ownership, and the enlarged additive reserve volume (6).
5. Normalized frame weights, the active-address coding hypothesis and its volume convention, replacing an invalid inference from exact-volume counts to volume-bin counts.
6. The integrand/base-measure split, upper-integral convention, common Borel envelope, compatible drop-out fibre, and finite operation ancestry for induction.
7. Carrierwise oscillation on a fixed creation domain; later admission into the full core; the precise class of presentations, rather than arrays of bounds.
8. The uniform radius-weight comparison including \(C_{\rm rad}\), and explicit loaded-label and small-field-ball hypotheses for the stability assertion.
9. The four-dimensional surface kernel, the union convention for ancestor cones, and the injective triangular-coordinate hypothesis of the local integration estimate.

## Change log (pass 3 fixes, lead, 2026-11-04)

Applied the findings of `gates/in1-gate.md` (Claude fresh session, first failing step none):
- F1: the missing source record is noted; the referee rechecked the YM3 and FG11 lines.
- F2: X-tilde defined as the creation-domain hull of X.
- F3: list size defined as Lemma 5's sum (SA R18).
- F4: light node defined both ways (o(u) <= C_g, SA 17744).
- F5: Lemma 2's bound on C - C_* carries a factor at most 9/8 from the parameter weights, absorbed by H_0 (no statement changes).
- F6: c_lin and the H-C certificate constants placed before c_G in row 7.
- F7: the boundary volume cost c_B added to the c_1 floor (rows and Lemma 5).
- F8: the c4-order floors L^2 >= 6 sqrt2 lambda_a, kappa/4 > kappa_D and kappa's entropy floor listed.
- F9: carrier-adopt section 6 and inv-root cited at the matrix-envelope Outstanding note.
- F10: X_0 >= c_ball^2 made explicit.
- F11 (letters with several meanings) left for the hardening pass; clarity only.

**Status: frozen.** Reopens only on a `wrong` signal or when an import it reads changes.

## Result

The distilled IN1 proves the hand implications in Lemmas 1–9 and the conditional component, class and first-passage theorems 10–12. In particular the scalar leading logarithm follows from interval-telescoped one-loop information and a vanishing error envelope; it needs neither monotone increments nor their pointwise convergence.

Its imports are H-M (FP1/PR1 and actual UM), H-OL (OL1), H-SF (NL1/ST1/SC1), H-LF, H-G, H-C, H-E, H-O and H-SUM (the specified LF1, BG1, PR1 and domain statements), including their constant order. Their outstanding actual-construction links remain visible above. This is not an unconditional proof of C4, of C3 for unspecified labels, or of four-dimensional Yang–Mills existence.

Corrections to the pass-1 draft:

- Restricted the path-matrix result to its actual hypotheses, made holomorphy and the global gap explicit, and separated block factorization from the unproved heredity/identification needed for UM. Made the coefficient-ratio perturbation constant an explicit early input.
- Corrected the Gaussian proof citation to SA 13904–14089; FG11 continues beyond the draft's endpoint 14056. Corrected the YM3 exponent locator to 63108–63112, the tilt to 63448–63458, the later defect inequalities to 63239–63248, and other clipped endpoints in the source record. Kept every dimensional transfer from YM3 conditional on its four-dimensional hypothesis.
- Made localized-to-bulk coefficient identification an import, retained own-coefficient subtraction, restored the weak-envelope slack of c4-order, and included the fixed enlargement/all-radii factor in the list weights.
- Limited the simultaneous-choice claim to displayed conditions and ordered imports. An elementary choice lemma cannot verify the missing actual estimates or their uniformity.
- Proved the four-dimensional cone counting/recursion and additive energy bootstrap; retained the nonlinear averaging estimate, nonexistence certificates, overlap ownership and renewed gains as separate hypotheses.
- Replaced the running-minimum logarithm comparison by its frame-slack bound, fixed the genealogical volume convention, and supplied a normalized coding proof of entropy instead of the unsupported exact-volume binning.
- Required the unused cut-island witness and finite operation ancestry. Supplied the injectivity and triangularity needed for Gaussian changes of variables, and kept all normalizers and determinants in the integrand.
- Required a common envelope *before* the external or dropout supremum; a fixed-evaluation integration bound is insufficient. Required full creation-domain admission rather than inferring it from curvature/current room.
- Restored the unproved oscillation clause, separated the loaded-label sum and stability-floor inputs, and restricted positivity to physical real parameters. Removed the claim that nothing remains outstanding.
- Reordered the actual-run induction so the next weight is protected before the next class step; separated analytic next-step existence from stopping arithmetic and used a tail-envelope Cesàro proof of the leading logarithm.

All proofs here are mathematical text. Retrieval and file bookkeeping supply no proof step. The manuscript is **not yet refereed** and grants no scientific or audit status.
