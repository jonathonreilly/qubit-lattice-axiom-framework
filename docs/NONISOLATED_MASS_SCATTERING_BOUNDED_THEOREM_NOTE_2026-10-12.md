---
claim_id: "nonisolated_mass_scattering_bounded_theorem_note_2026-10-12"
claim_type: "bounded_theorem"
claim_scope: "Under actual finite-range physical dynamics, a unique gapped vacuum, supplied stable graph sectors, positive full-operator transfer and geometric detuning regularity, fixed finite velocity-separated time-averaged products have incoming/outgoing limits independent of admissible creators and every fixed sublinear power width. No Fock, density, detector, exhaustion or microscopic-realization conclusion is supplied."
upstream_dependencies:
  - compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
  - compact_patch_fock_isometry_bounded_theorem_note_2026-10-12
runner: "scripts/nonisolated_mass_scattering_2026_10_12.py"
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A future independently checked nonexact-vacuum Fock and detector extension on actual regular creator classes."
source_of_blocker_text: "handoff"
reachability_to_target: "partially_closes"
artifact_role: "theorem"
next_trace_action: "Construct regular creators and establish their target density in an actual model; separately check Fock and detector extensions."
conditional_surface_status: "Finite-product scattering from an explicit geometric detuning bound on each residual packet"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual dynamics, stable graph sectors, positive transfer and regular seed vectors remain supplied; the analytic implication is conditional."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Nonisolated geometric mass-shell scattering on compact patches

**Claim type:** bounded theorem. **Actual current-surface status:** conditional-support. **Source review:** complete with the reviewed N36 definition repair below. The theorem below concerns finite, velocity-separated products on fixed compact dispersion charts. Its extra hypothesis is a per-packet spectral regularity bound for the actual geometric detuning. It does not assert that any microscopic model supplies the stable sector or regular creators. Root proposed the mechanisms and is a coauthor, not an independent checker.

Time averaging replaces the old exact vacuum-graph condition. A direct lattice proof gives strong incoming and outgoing product limits and creator independence. The proof first uses widths with an integrable vacuum derivative, then compares limits to cover every fixed power width strictly between zero and one. It retains the supplied unique gapped vacuum and actual finite-range physical dynamics. Fock inner products, isometries, detectors, all-channel density, ND, EX and physical realization are not conclusions.

## 1. Source contract, literature and status

S denotes the original research collection. The [frozen milestone handoff](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/HANDOFF.md) and [evidence map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/EVIDENCE_MAP.json) preserve the source files, full author/reviewer evidence and their identities. SW denotes the source-bound science checkout. The actual in-branch proof uses are [SC](COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md): Compact-patch signs, locality, packet and cutoff framework; the needed arguments are reconstructed, without importing isolated-shell scattering conclusions.; [Fock](COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md): F7-F9 mixed-lowering finite-energy proof mechanism, reproduced at the actual mass-note hypotheses; no Fock Gram, density or isometry conclusion is imported. Other historical references remain provenance only.

| Source | SHA-256 | Actual use |
|---|---|---|
| SC, original `COMPACT_PATCH_SCATTERING_COVARIANCE_PROBE.md` | d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a | Provenance of the compact-patch construction |
| SC, complete published source at SW f6f4348151734908dea3b32048ee1f36f694035b | 3adc57d0236fced52704aa76e4fa7d38abbe08204623162c8fd07404a2a44a05 | Complete argument read; actual microscopic dynamics, almost locality, packet signs/tails and cutoff comparison are reconstructed below |
| F, original `COMPACT_PATCH_FOCK_ISOMETRY_PROBE.md` | 9bc3a309e8fc35978bcac0c360b8557fb6a3c4484cfc2034a277a94072369404 | Provenance of the finite-energy lemma |
| F, complete published source at the same SW head | 494c283c163e88f959841462bbfbcfcc7c470072a0525d0dd6e2b44dd6f9b12b | Complete argument read; only F7–F9 are reused as a proof mechanism, reproduced in §4; no Fock conclusion is imported |
| `ISOLATED_CENTRE_FILTERING_PROBE.md` | 1dcb9580d128d8fc41b76517ce0fe18842291e8e32681fa9c6b22f0feb1e13de | Complete source read, including the recovered I22/density fragment; its on-mass centre isolation is distinguished from off-mass regularity in §9 |
| Dybalski, official hep-th/0412226v4 PDF | 3c616a4d6c8b52793bb669387a237de31ee66417450ddc5f29b7c93ece7b534d | Complete original TeX read; PDF pp. 2, 3, 6, 7, 8 checked visually |
| Dybalski v4 original TeX | c425cfecc20136576180271a1e8e9c12df48ded2ae941655ad4e842363ee64a6 | All sections and proofs, including the scope limits, read in full |
| BDN, official arXiv:1412.2970v2 PDF | 3edeb48a167b9ae6a26d6d885ccde03b068423d432176a256eb0a4ee42a14126 | §§2.1–2.4, 3.1–3.3, Proposition 4.3 and the relevant creator discussion, complete Appendix B/C arguments; precise reading coverage is recorded separately |

[Dybalski, *Haag–Ruelle scattering theory in presence of massless particles*](https://arxiv.org/abs/hep-th/0412226v4), equations (2)–(6), Lemmas 2.1–2.2, Theorem 2.3 and Lemma 2.4, supply the literature mechanism: sublinear time averages, an integrable vacuum derivative, restricted-energy spectator bounds, and comparison of averaging choices. That paper's setting is a relativistic local net. Its spacelike locality, Poincaré representation, relativistic harmonic-analysis bounds and massless-vacuum/Fock conclusions are not premises here. In particular its regularity variable is the relativistic mass Casimir; the geometric detuning in this note is a different required variable unless the off-mass relation in §9 is supplied.

[Bachmann–Dybalski–Naaijkens](https://arxiv.org/abs/1412.2970v2), Theorem 2.1, Proposition 3.6 with Appendix B, and Appendix C, give the finite-range lattice LR and transfer/smearing framework. Proposition 4.3 gives the packet estimates, which are also derived at the strength used here. BDN's isolated-shell scattering theorem is not invoked for a nonisolated shell. Neither external source alone proves this adaptation.

Instructions are frozen at science main `a13caa4885f547c8d206265b031ba7649e539fd9` and planning `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`; installed physics-loop/workhorse bytes and applicable references match the selected science revision. The supplied write contract confines this worker to this note and its evidence directory and forbids publication/Git mutations. The primitive registry was read: none of its approved units, kinetic-form or realized-state primitives supplies the stable spectral projection, the dynamics or the regularity condition used here. These remain explicit conditional inputs, not adopted axioms.

At author freeze this proof-level adaptation awaited fresh independent review; that source review is now complete and recorded below. No novelty claim beyond the stated source comparison is made. The scoped SW search for Herbst/nonisolated/embedded masses returned no matching existing theorem; unrelated flavor-text matches supply no scattering result.

## 2. Exact setting and conditional theorem

Let the observable algebra be the quasilocal tensor-product algebra of finite-dimensional sites on \(\mathbb Z^d\), \(d\ge1\), with geometric shifts \(\tau_x\). A translation-invariant finite-range interaction, with \(\sup_x\sum_{Z\ni x}\|\Phi(Z)\|<\infty\), supplies the actual norm-continuous physical automorphism group on each observable,
\[
\alpha_t=\operatorname{Ad}e^{itH},\quad H\ge0,\quad
T_x=e^{-ix\cdot Q},\quad \tau_x=\operatorname{Ad}T_x,
\qquad [e^{itH},T_x]=0.                                      \tag{N1}
\]
The vacuum GNS vector is invariant under both groups. Keep explicitly
\[
\ker H=\mathbb C\Omega,\qquad
\operatorname{spec}(H)|_{\Omega^\perp}\subset[\gamma,\infty),
\qquad\gamma>0.                                             \tag{N2}
\]
The existence proof below uses positivity and the LR bound, without a clustering step. We retain (N2) as part of this task's setting; no massless-vacuum extension is claimed. Continuous current flows, if separately supplied, need not be used in this proof.

For each packet label i choose the following fixed data.

1. An open single-lift geometric momentum chart \(O_i\) whose compact closure lies inside a larger smooth dispersion chart, a real smooth dispersion \(\Sigma_i\) positive on the relevant compact support, and a projection \(E_{1,i}\) commuting with H and the spectral measure of Q such that
   \[
   (H-\Sigma_i(Q))E_{1,i}\mathbf1_{O_i}(Q)=0.                 \tag{N3}
   \]
   This equality means spectral support on the graph, including the appropriate domain statement. Choose a smooth real extension of \(\Sigma_i\) to the torus agreeing on a neighborhood of \(\overline O_i\); compact patch refinement permits this extension. It is used only for functional calculus; none of the packet assertions depends on its values outside the packet support. For the selected geometric mass chart it is
   \[
   \Sigma_i(p)=\sqrt{M_i^2+\beta|p+\theta_i+2\pi n_i|^2},
   \quad M_i,\beta>0,\quad n_i\in\mathbb Z^d.                \tag{N4}
   \]
   No spectral gap about this graph or about its mass is assumed. Stability here means the supplied reducing graph sector, not a proof of its physical existence.
2. An almost-local observable \(B_i\), with almost-local norm time derivatives, whose **full operator** temporal transfer lies in a fixed interval
   \[
   \operatorname{Sp}_{\alpha}(B_i)\subset I_i=[\epsilon_i,L_i]
   \subset(0,\infty).                                      \tag{N5}
   \]
   The interval is independent of the averaging time. A vacuum energy support alone does not replace (N5). Section 3 constructs this class from a local regular seed using fixed smooth filters.
3. \(\widehat f_i\in C_c^\infty(O_i)\). With normalized torus measure define
   \[
   f_{i,t}(x)=\int e^{ip\cdot x-it\Sigma_i(p)}\widehat f_i(p)
                      \frac{dp}{(2\pi)^d},\qquad
   C_i(t)=\sum_x f_{i,t}(x)\alpha_t\tau_x(B_i).              \tag{N6}
   \]
   Put \(D_i=H-\Sigma_i(Q)\), \(v_i=\widehat f_i(Q)B_i\Omega\),
   \(\psi_i=E_{1,i}v_i\), \(r_i=(1-E_{1,i})v_i\). The extra regularity condition is: for some \(a_i>0,c_i<\infty,\eta_i>0\),
   \[
   \boxed{\quad
   \|\mathbf1_{\{|D_i|\le\eta\}}r_i\|\le c_i\eta^{a_i},
   \qquad 0<\eta\le\eta_i.\quad}                          \tag{N7}
   \]
   The projection includes zero detuning. Equivalently, one may impose the same bound for \(0<|D_i|\le\eta\) and separately impose
   \(\mathbf1_{\{0\}}(D_i)r_i=0\). Nonzero \(\psi_i\), when desired, is a further property of the chosen data; neither cyclicity nor a stable sector alone supplies a local regular seed.

For a fixed finite family the compact velocity sets
\[
\mathcal V_i=\nabla\Sigma_i(\operatorname{supp}\widehat f_i)
                                                               \tag{N8}
\]
are pairwise disjoint. Choose \(h_i\in\mathcal S(\mathbb R)\) with
\[
\widehat h_i(z)=\int h_i(u)e^{iuz}\,du\in C_c^\infty(\mathbb R),
\qquad\widehat h_i(0)=\int h_i=1.                            \tag{N9}
\]
Positivity of h is unnecessary; all operator bounds below use absolute integrals. For \(\sigma=+1\) or \(-1\), \(T\ge1\), and \(s_i(T)=T^{\nu_i}\), put
\[
g_{i,T}^{\sigma}(t)=s_i^{-1}h_i((t-\sigma T)/s_i),\qquad
A_i^{\sigma}(T)=\int g_{i,T}^{\sigma}(t)C_i(t)\,dt.             \tag{N10}
\]
All integrals and sums are norm convergent at fixed T.

**Conditional theorem.** Under (N1)–(N9), for every fixed finite internally velocity-separated family:

- If \(1/(1+a_i)<\nu_i<1\) for every i, the product \(A_1^{\sigma}(T)\cdots A_n^{\sigma}(T)\Omega\) has a strong limit as \(T\to\infty\). Its derivative has the integrable estimate (N30) below.
- The same limit exists for every choice \(0<\nu_i<1\) and kernels (N9), by comparison with an integrable reference width. Within the same fixed dispersion charts and selected graph sectors, any two internally separated creator/packet families with the same ordered vectors \(\psi_i\) give the same limit, without a cross-family separation assumption. Fixed smooth filter and seed choices are covered insofar as they give these same vectors and obey the stated direct conditions.
- Limits are permutation symmetric for these ordinary almost-local observable creators. If any \(\psi_i=0\), the product limit is zero. The empty product is \(\Omega\); the one-factor limit is \(\psi_1\).

Constants may depend on the finite family, temporal intervals, exponents, kernels and positive velocity separation. No uniformity in particle number, collapsing separation or an infinite chart/species collection is asserted. In particular no nonzero multiparticle norm, Fock Gram identity or bounded map on all Fock data is inferred.

## 3. Fixed filters supply the operator class but not regularity

Suppose a local seed A has (N7) for the chosen packet before filtering. Choose \(\chi\in C_c^\infty((0,\infty))\), equal to one near \(\Sigma(\operatorname{supp}\widehat f)\), and \(\zeta\in C_c^\infty(O)\), equal to one near that packet support. Let
\[
k(t)=\frac1{2\pi}\int e^{-iEt}\chi(E)\,dE,\qquad
b(x)=\int e^{ip\cdot x}\zeta(p)\frac{dp}{(2\pi)^d},
\]
\[
B=\sum_x b(x)\int k(t)\alpha_t\tau_x(A)\,dt.                 \tag{N11}
\]
Both kernels have arbitrarily many integrable polynomial moments. The signs in (N11) give
\[
B\Omega=\chi(H)\zeta(Q)A\Omega,\quad
E_1\widehat f(Q)B\Omega=E_1\widehat f(Q)A\Omega.              \tag{N12}
\]
All multipliers commute with \(D,E_1\); hence (N7) is preserved, with its constant multiplied by at most \(\|\chi\|_\infty\|\zeta\|_\infty\). The filter does not establish (N7) for an arbitrary seed.

Smearing a second time multiplies Fourier multipliers, so the full operator temporal transfer of B is contained in \(\operatorname{supp}\chi\), and its geometric transfer in \(\operatorname{supp}\zeta\). This uses the Arveson support of the whole observable; (N12) is not its proof. The transfer relation gives
\[
BP_R\mathcal H\subset P_{R+L}\mathcal H,\qquad
B^*P_R\mathcal H\subset P_{R-\epsilon}\mathcal H,\quad
B^*\Omega=0,                                                \tag{N13}
\]
where \(P_R=\mathbf1_{[0,R]}(H)\) and \(P_R=0\) for R<0. Geometric translations, time evolution, norm sums/integrals and norm derivatives preserve the fixed interval or its negative for adjoints.

For clarity the locality proof uses actual finite-range H dynamics. Its LR consequence for a local observable supported in X is
\[
\|(1-\mathbb E_{X^r})\alpha_t(A)\|
\le C|X|\|A\|e^{-\lambda(r-v_{\rm LR}|t|)}.                 \tag{N14}
\]
Fix a localization ball of radius R around the original seed. Truncate (N11) to \(|x|+|t|\le cR\) for a fixed sufficiently small \(c>0\), and apply its conditional expectation to that ball. For large R its padding after the geometric displacement and LR growth is at least R/2. The integrated local error is bounded by a constant times \(e^{-\lambda R/2}\|k\|_1\|b\|_1\); the omitted kernel tail is \(O(R^{-N})\) for every N, by absolute norms and Schwartz moments. Thus B is almost local. This does not integrate an exponential-in-time estimate over an unrestricted Schwartz tail.

Shifting k under \(\alpha_u\) in the norm integral gives
\(\delta_H^m B=\sum_x b(x)\int(-\partial_t)^m k(t)\alpha_t\tau_x(A)dt\).
The identical locality proof applies to every m. General direct-property creators can be used without a strictly local seed, provided their stated properties have separately been proved.

## 4. Exact finite-energy bounds and every spectator

This is the F7–F9 argument, with its proof hypotheses checked after dropping exact vacuum graph support. For a creator B with interval \([\epsilon,L]\), set
\[
S_B=\sum_{z\in\mathbb Z^d}\|[B^*,\tau_z(B)]\|<\infty.        \tag{N15}
\]
Almost locality makes the commutator rapidly decreasing. Write \(L_x=\tau_x(B^*)\), and let \(\mathcal P_r\) project onto the common kernel of **all ordered r-fold products** of the \(L_x\). Then \(L_x\operatorname{Ran}\mathcal P_r\subset\operatorname{Ran}\mathcal P_{r-1}\). For finite \(\Lambda\), put \(Q_\Lambda=\sum_{x\in\Lambda}L_x^*L_x\) and \(b_r=\|\mathcal P_rQ_\Lambda\mathcal P_r\|\), with \(b_1=0\).

For a unit \(\Phi\in\operatorname{Ran}\mathcal P_r\), the exact noncommutative expansion is
\[
\langle Q_\Lambda^2\rangle_\Phi
=\sum_{x,y}\langle L_x\Phi,[L_x,L_y^*]L_y\Phi\rangle
 +\sum_{x,y}\langle L_yL_x\Phi,L_xL_y\Phi\rangle.             \tag{N16}
\]
The first sum has absolute value at most \(S_B\langle Q_\Lambda\rangle_\Phi\), by the commutator row/column sums and \(2ab\le a^2+b^2\). Cauchy–Schwarz, reindexing x,y, and the common-kernel inclusion bound the second sum by
\(b_{r-1}\sum_x\|L_x\Phi\|^2\). Since \(\langle Q\rangle^2\le\langle Q^2\rangle\), one gets \(b_r\le b_{r-1}+S_B\le(r-1)S_B\). Equation (N13) puts \(P_R\mathcal H\) in this common kernel whenever \(r\epsilon>R\). Increasing finite \(\Lambda\) gives the bounded positive strong limit and
\[
\Gamma_B(R):=\left\|P_R\sum_x\tau_x(BB^*)P_R\right\|
\le\lfloor R/\epsilon\rfloor S_B.                          \tag{N17}
\]
It would be insufficient to know only \((B^*)^rP_R=0\); mixed products are essential.

Let \(F_2=\|\widehat f\|_{L^2(dp/(2\pi)^d)}\). Parseval and vector Cauchy–Schwarz give
\[
\|C(t)^*P_R\|\le F_2\sqrt{\Gamma_B(R)},\qquad
\boxed{\ \|C(t)P_R\|\le F_2\sqrt{\Gamma_B(R+L)}\ }.         \tag{N18}
\]
For the second bound insert \(P_{R+L}\) on the output and use the first by duality. The common physical time is removed because \(P_R\) commutes with H. These bounds hold for all real t. Integration of absolute kernels gives
\[
\|A^\sigma(T)^*P_R\|\le\|h\|_1F_2\sqrt{\Gamma_B(R)},\qquad
\|A^\sigma(T)P_R\|\le\|h\|_1F_2\sqrt{\Gamma_B(R+L)}.        \tag{N19}
\]
They require neither isolated masses nor an exactly constant vacuum vector.

Every fixed finite word of such averaged creators and adjoints has a uniform norm on \(P_R\mathcal H\): all intermediate vectors lie below \(R_* =R+\sum_j L_j\), since an adjoint only lowers energy. Insert \(P_{R_*}\) at every intermediate stage and multiply the bounds (N19), using the creator bound at R* also to dominate an adjoint. This accounts for each spectator. The same statement holds for mixed words from two families, or sums/differences with a common finite energy ceiling. This is the bound used on the residual vacuum derivatives and zero-target differences; multiplying their norms by the unrestricted polynomial norms would not suffice.

## 5. Vacuum limit and the two derivative formulas

For (N6), Fourier inversion with \(T_x=e^{-ixQ}\) gives exactly
\[
C(t)\Omega=e^{itD}v,\qquad
A^\sigma(T)\Omega=e^{i\sigma TD}\widehat h(sD)v.               \tag{N20}
\]
The vector \(E_1v=\psi\) lies in \(\ker D\). Taking \(\eta\downarrow0\) in (N7) proves \(\mathbf1_{\{0\}}(D)r=0\). Thus even without the rate, spectral dominated convergence gives \(A^\sigma(T)\Omega\to\psi\) whenever \(s\to\infty\). If \(\operatorname{supp}\widehat h\subset[-b,b]\), b>0, the quantitative form for sufficiently large T is
\[
\|A^\sigma(T)\Omega-\psi\|
\le c\|\widehat h\|_\infty(b/s)^a=O(T^{-\nu a}).             \tag{N21}
\]
The oscillatory phase is unitary and plays no role in this norm estimate.

There are two equal norm-derivative formulas; both are needed to expose the otherwise easily omitted terms. With \(u=(t-\sigma T)/s\),
\[
\partial_Tg_T^\sigma(t)
=-s^{-2}\{\sigma h'(u)+s'[h(u)+u h'(u)]\},\qquad
\partial_TA^\sigma(T)=\int(\partial_Tg_T^\sigma)(t)C(t)dt.     \tag{N22}
\]
In particular its absolute kernel integral is at most
\(s^{-1}\|h'\|_1+|s'|s^{-1}\|h+u h'\|_1\).
The alternative formula, obtained by t=\(\sigma T+su\), is
\[
\partial_T A^\sigma(T)
=\int h(u)(\sigma+s'u)\{C_{\sigma T+su}(\delta_HB,f)
                  +C_{\sigma T+su}(B,f^{(1)})\}\,du,
\quad\widehat f^{(1)}=-i\Sigma\widehat f.                    \tag{N23}
\]
Both the physical-generator term and the packet-clock term occur. Integration by parts in u proves equivalence of (N22) and (N23), with zero boundary terms because h is Schwartz while C and its derivative have polynomial norm growth. Local-in-T dominated norm differentiation justifies the formulas; no moving spatial cutoff is differentiated.

On the vacuum, they reduce to
\[
\partial_TA^\sigma(T)\Omega
=e^{i\sigma TD}\{i\sigma D\widehat h(sD)+s'D\widehat h'(sD)\}r.
                                                               \tag{N24}
\]
Let \(a_0=\sup_z|z\widehat h(z)|\) and \(a_1=\sup_z|z\widehat h'(z)|\). Equation (N7) gives
\[
\|\partial_TA^\sigma(T)\Omega\|
\le c b^a(a_0+|s'|a_1)s^{-1-a}
\le K T^{-\nu(1+a)},\quad s'=\nu T^{\nu-1}.                 \tag{N25}
\]
The last inequality uses \(0<\nu<1\). The width derivative has not been discarded. This bound is integrable when \(\nu(1+a)>1\). All these vectors have H-energy in \([0,L]\), since the full temporal transfer is fixed. Equations (N21) and (N25) are per-packet consequences of (N7), not a claim about a mass-operator regularity condition.

## 6. Unequal averaging times: the lattice commutator proof

Fix two distinct velocity-separated labels. The two time integrals in their commutator are independent. Put \(\bar\nu=\max(\nu_i,\nu_j)\) and choose
\[
\bar\nu<\mu<1.                                             \tag{N26}
\]
Choose smooth compact velocity collars \(W_i,W_j\) about the two velocity sets, separated by \(\delta>0\), and cutoffs \(\chi_i,\chi_j\) supported there and equal to one near the velocity sets. Direct nonstationary phase on the compact chart gives
\[
\|f_{i,t}\|_{\ell^1}\le C_i(1+|t|)^d,\quad
\|(1-\chi_i(x/t))f_{i,t}(x)\|_{\ell^1_x}\le C_{i,N}|t|^{-N}
                                                               \tag{N27}
\]
for \(|t|\ge1\), and the same for the amplitude \(-i\Sigma_i\widehat f_i\). To see the tail, the phase gradient \(x-t\nabla\Sigma_i(p)\) is bounded below by a fixed multiple of \(|x|+|t|\) outside the collar; repeated integration by parts gives arbitrary inverse powers. Summing more than d extra powers gives (N27). In the collar there are \(O(|t|^d)\) sites and each Fourier integral is bounded. Thus no Hessian nondegeneracy is needed here.

First restrict both averaging times to \(|t-\sigma T|,|u-\sigma T|\le T^\mu\). Then \(|t|,|u|\asymp T\), \(|u-t|\le2T^\mu\), and for \(x/t\in W_i,y/u\in W_j\),
\[
|x-y|\ge\delta T-C T^\mu\ge\delta T/2
\]
for large T, for either sign of \(\sigma\). Remove the common physical evolution **before** using LR:
\[
\|[\alpha_t\tau_x(B_i),\alpha_u\tau_y(B_j)]\|
=\|[\tau_x(B_i),\alpha_{u-t}\tau_y(B_j)]\|.                  \tag{N28}
\]
Approximate both fixed B's by norm-bounded local observables of radius \(r=\delta T/16\). The two approximation errors are \(O(T^{-N})\) for every N, uniformly under the remaining automorphisms. Their local supports have distance at least \(3\delta T/8\). LR bounds the local commutator by
\(C T^d\exp[-\lambda(3\delta T/8-2v_{\rm LR}T^\mu)]\), which is rapidly decreasing. Hence the commutator of the untruncated observables is uniformly \(O(T^{-N})\) in the central time windows and spatial collars. Multiplying by the two packet \(\ell^1\) norms costs at most \(T^{2d}\). Spatial-tail terms cost at most \(T^{d-N}\); arbitrary N absorbs both costs.

The time tails must also be checked with the polynomial packet growth. After \(t=\sigma T+T^{\nu_i}z\), for any Schwartz kernel k,
\[
\begin{split}
&\int_{|t-\sigma T|>T^\mu}T^{-\nu_i}|k((t-\sigma T)/T^{\nu_i})|
                      (1+|t|)^d\,dt\\
&\qquad\le C T^d\int_{|z|>T^{\mu-\nu_i}}|k(z)|(1+|z|)^d dz
\le C_{i,N}T^{d-(\mu-\nu_i)N}.                             \tag{N29}
\end{split}
\]
This is rapid since \(\mu>\nu_i\). Bound a two-time commutator tail by twice the product of the corresponding tail norm and the other full packet norm \(O(T^d)\), then choose N large enough. Formula (N22) writes a derivative as the same average with kernels h', h+zh' and coefficients \(-\sigma/s,-s'/s\); these coefficients are bounded for \(T\ge1\). The same proof therefore covers one or both averaged derivatives. Adjoints have the same absolute packet weights and locality estimates.

Consequently, for any P and internally separated labels,
\(\|[\partial_T^a A_i^\sigma(T),\partial_T^b A_j^\sigma(T)]\|
\le C_P T^{-P}\), \(a,b\in\{0,1\}\), also with either factor adjointed. The unrestricted norms of these factors grow at most as \(O(T^d)\). For a fixed n-factor product there are n−2 spectators beside each commutator: selecting P larger than \(d(n-2)+2\) makes the entire commutator contribution integrable. Independent integration times have never been identified, and no condition comparing physical packet speeds with the LR speed was needed; only the sublinear time **difference** enters (N28).

## 7. Finite-product Cook convergence

Suppress \(\sigma\) and write \(\Psi(T)=A_1(T)\cdots A_n(T)\Omega\). Norm differentiation, then commuting each differentiated factor to the vacuum, gives the exact identity
\[
\begin{split}
\Psi'(T)={}&\sum_{i<j}
A_1\cdots A_{i-1}A_{i+1}\cdots A_{j-1}
[A_i',A_j]A_{j+1}\cdots A_n\Omega\\
&+\sum_i A_1\cdots A_{i-1}A_{i+1}\cdots A_n A_i'\Omega.
\end{split}
\]
The order shown retains all other factors; the residual vacuum term is generally nonzero. Section 6 bounds the first line by \(K T^{-2}\), after accounting for all n−2 spectator norms. For the second line, \(A_i'\Omega\in P_{L_i}\mathcal H\). Insert the finite energy ceiling and apply §4 to **all** n−1 spectators. Then (N25) gives constants independent of T such that
\[
\boxed{\quad
\|\Psi'(T)\|\le K T^{-2}+\sum_{i=1}^n K_iT^{-\nu_i(1+a_i)}.
\quad}                                                      \tag{N30}
\]
For n=1 the first sum is empty; n=0 is constant. If every \(\nu_i(1+a_i)>1\), Cook's norm Cauchy estimate proves the strong limit, with tail bound
\[
\|\Psi(T)-\Psi^\sigma\|
\le K/T+\sum_i\frac{K_i}{\nu_i(1+a_i)-1}
                     T^{1-\nu_i(1+a_i)}.                    \tag{N31}
\]
Changing adjacent factors costs a rapid commutator times all remaining polynomial spectator norms. Thus every permutation has the same limit. No Fock contraction or Gram formula was used.

## 8. Creator independence, zero targets and all power widths

The comparison proof uses the uniform finite-energy estimates, rapid commutators, and vacuum convergence. It does not require integrability of each family's derivative. It therefore applies to all powers \(0<\nu_i<1\) and kernels (N9), and even to a comparison creator whose off-shell vector is only known to have no extra zero-detuning component and hence to converge by spectral dominated convergence.

**Zero target.** If \(\psi_i=0\), commute \(A_i(T)\) to the far right of its internally separated family. Each commutator error is rapid after all polynomial spectators. The final vector is a word of n−1 creators acting on \(A_i(T)\Omega\), whose norm tends to zero and whose energy is at most \(L_i\). Equation (N19) bounds that entire word uniformly. The product tends to zero. This is a convergence argument, not the false identity \(A_i(T)\Omega=0\) at finite T.

**Cross-compatible families.** If the velocity sets of different labels remain separated in every mixed pair, telescope two ordered products with equal targets. A difference \(Z_i(T)=A_i(T)-\widetilde A_i(T)\) is a sum of two admissible packet families. Its vacuum vector tends to zero and lies in \(P_{\max(L_i,\widetilde L_i)}\mathcal H\). Commute Z to the right, control commutator errors by §6, and bound the final spectator word by (N19). The product difference tends to zero, whether or not both limits were already known.

**Removal of the mixed-support condition on fixed graphs.** Let both original families be internally separated, with the same \(\Sigma_i,E_{1,i}\) and target \(\psi_i\) for each label. Zero targets were just handled, so assume they are nonzero. The compact Q-spectral support \(S_i\) of \(\psi_i\) lies inside both packet supports. Thus \(\nabla\Sigma_i(S_i)\) is separated from every other label's support in either family. Choose a smooth \(q_i\), equal to one near \(S_i\), supported in a sufficiently small neighborhood whose velocities avoid all those other supports, inside the common fixed chart.

Refine the first family's amplitude to \(q_i\widehat f_i\). The discarded factor is the **actual** packet with amplitude \((1-q_i)\widehat f_i\), the same B, kernel and width. Its target is zero, its velocity support remains a subset of the original \(\mathcal V_i\), and its vacuum vector merely tends to zero. The regularity condition is preserved because \(q_i(Q)\) commutes with \(D_i,E_{1,i}\); the no-extra-kernel condition alone is also preserved. Telescoping original versus refined products, all other factors remain within their own original supports. Commuting each discarded packet to the vacuum and using its finite-energy ceiling proves that refinement changes the product by a vector tending to zero. No small operator norm of the discarded packet is asserted.

The refined first family is cross-compatible with the entire alternative family, so the preceding comparison identifies their limits. This explicitly handles extra amplitude support carrying a zero target. Equal target vectors alone were not used to shrink the support of an unchanged operator.

Finally choose for each regular packet a reference exponent \(\nu_i^{\rm ref}\in(1/(1+a_i),1)\). Section 7 proves its limit. The comparison just proved transfers it to any prescribed \(0<\nu_i<1\), even when the new derivative bound is not integrable. It also proves independence of h and all admissible creator/filter realizations of the same targets on these fixed graphs. Different graph assignments or arbitrary raw nonseparated products would require an additional argument and are not included.

## 9. Decisive failure controls and the exact regularity variable

**Zero detuning cannot be excluded from the hypothesis without replacement.** On \(\mathbb C\Omega\oplus\mathbb Ce_1\oplus\mathbb Ce_2\), let H be zero on \(\Omega\), equal to E>0 on both other vectors, and take Q=p there with \(\Sigma(p)=E\). Let \(E_1=|e_1\rangle\langle e_1|\), \(v=e_1+e_2\). Then \(\mathbf1_{\{0<|D|\le\eta\}}(1-E_1)v=0\) for every \(\eta\), but the time average is always \(e_1+e_2\), not the declared target e1. A rank-one creator from \(\Omega\) realizes this positive-energy column. This is an abstract spectral control of the missing-kernel implication, not a local-lattice countermodel. Condition (N7), or its explicit kernel supplement, rejects it.

**Mass-Casimir regularity does not generally give geometric regularity.** Here is an infinite, explicit commuting spectral model that also exposes the limitation of centre isolation only on the exact mass sector. In one dimension set \(M=\beta=1\), \(J=[1/4,1/2]\), \(\Sigma(p)=\sqrt{1+p^2}\), and
\[
\mathcal H=\mathbb C\Omega\oplus L^2(J)\oplus
                         \bigoplus_{n\ge2}L^2(J).
\]
All generators vanish on \(\Omega\). On the target summand use \(Q=p,K=p,H=\Sigma(p)\); on summand n use
\[
Q=p,\qquad K_n=p+1/n,\qquad
H_n=\Sigma(p)+\delta_n,\qquad\delta_n=e^{-n^2}.               \tag{N32}
\]
The vacuum is unique and gapped, and the displayed generators strongly commute. With \(\mathcal C=H^2-K^2\), the target has \(\mathcal C=1\), while
\[
\mathcal C_n-1=2\Sigma(p)e^{-n^2}+e^{-2n^2}-2p/n-1/n^2,
\qquad
\frac{2}{5n}\le|\mathcal C_n-1|\le\frac{3}{2n}.              \tag{N33}
\]
For the bounds, \(n e^{-n^2}\le2e^{-4}<1/25\),
\(n e^{-2n^2}\le2e^{-8}<1/1000\), and \(\Sigma<9/8\). Hence the positive terms times n are below 1/10, whereas \(2p\ge1/2\). The expression is negative; the upper bound follows by dropping the positive terms and using \(1/n\le1/2\). In particular \(\mathcal C_n>0\), is never 1, and approaches 1. The exact mass projection is the target summand.

Choose a unit smooth \(a(p)\) compactly supported in the interior of J, and take residual components \(r_n=a/n\). Then
\[
\|\mathbf1_{\{|\mathcal C-1|\le\eta\}}r\|^2
\le\sum_{n\ge2/(5\eta)}n^{-2}=O(\eta).                     \tag{N34}
\]
Thus a mass-Casimir Herbst norm bound with exponent 1/2 holds. But the geometric detuning is exactly \(D_n=\delta_n\). At \(\eta_N=e^{-N^2}\),
\[
\|\mathbf1_{\{|D|\le\eta_N\}}r\|^2
=\sum_{n\ge N}n^{-2}\ge1/N.                                \tag{N35}
\]
Its norm is of logarithmic order \((\log(1/\eta))^{-1/4}\) and violates every bound \(C\eta^a\), a>0. Adding any target component to v does not change either residual estimate.

The centre representation \(V_j=e^{ijK}T_j\) has character zero on the entire exact mass sector and character \(1/n\) on summand n. The selected character is isolated on the exact mass sector, exactly as in a condition restricted to \(E_M\). Nevertheless any fixed smooth centre bump \(\phi\) with \(\phi(0)=1\) satisfies \(|\phi(1/n)|\ge1/2\) for all sufficiently large n and leaves the failure of (N7) intact. A positive temporal cutoff equal to one on the displayed energies also leaves it intact. This model supplies no UHF algebra, almost-local regular creator or finite-range interaction; it refutes the claimed implication from those **spectral** facts alone, not the conditional lattice theorem or possible extra consequences of a microscopic model.

There is a precise sufficient conversion route. For this general-beta statement, define \(\mathcal C_\beta:=H^2-\beta|K|^2\), using the same \(\beta\) as the dispersion. If a current momentum K strongly commuting with H and Q is supplied and, on the whole residual vector under consideration (including off-mass components), one has the selected lift relation \(K=Q+\theta+2\pi n\) and \(\Sigma(Q)^2=M^2+\beta|K|^2\), then
\[
\mathcal C_\beta-M^2=(H-\Sigma(Q))(H+\Sigma(Q)).                    \tag{N36}
\]
On the residual vector's bounded positive-energy support and compact patch, \(H+\Sigma(Q)\) is bounded above and away from zero. A regularity bound for \(\mathcal C_\beta-M^2\) and matching zero-kernel projection then convert to (N7) by the spectral theorem. A selector proved only on the exact mass space does not supply this off-mass identity. We do not rule out deriving it in a stronger model.

**The Cook exponent is a sufficient estimate, not a necessity theorem.** For a residual scalar spectral measure with density \(2a r^{2a-1}dr\) on (0,1), \(\|\mathbf1_{|D|\le\eta}r_0\|=\eta^a\). A real even nonzero \(\widehat h\) near zero gives a centre-derivative norm of order \(s^{-1-a}\). After removing the common unitary phase in (N24), the width multiplier is real and the centre multiplier imaginary in this representation, so they cannot cancel that lower order. Therefore the displayed Cook estimate need not be integrable at \(\nu(1+a)\le1\). Yet the one-factor limit still exists by (N20), and §8 transfers product existence from a regular reference width. Failure of that particular integral is not nonexistence of scattering.

The remaining controls are equally scoped: an equal-time commutator cannot replace the two-time integral; multiplying a residual derivative by unrestricted \(T^{d(n-1)}\) norms loses the proof; and omitting either term in (N23), or the width term in (N22)/(N24), gives the wrong derivative. These are identifiable proof errors, not broad no-go claims.

## 10. Scope, open work and recovery

This result replaces exact vacuum-shell support by an explicit geometric spectral hypothesis for prescribed regular packets. It proves the stated conditional finite-product limits and their independence on fixed graphs. It does not derive regularity, stable one-particle projections or a physical microscopic model; a regular class could fail to be dense or even to contain a nonzero target. No physical axiom or framework primitive has been added.

The previous Fock and detector proofs cannot simply be relabelled as this extension. Their equal-time exact-vacuum contraction, Gram/density and detector propagation arguments would need to be checked for the new averaged, nonexact-vacuum creators. No such extension, scattering isometry, multi-particle nontriviality, channel exhaustion, ND, EX, boost covariance or massless-vacuum theorem is claimed here.

The evidence directory preserves the interrupted predecessor checkpoint, its source/download records and malformed large layout extractions, the new source manifest and reading coverage, operations, finite author controls and full execution logs, one current checkpoint, and a final receipt. Nine finite author controls ran under a declared 60-second timeout, exited 0 in 0.04084 seconds and emitted ten complete JSON records with empty stderr. They checked both averaging derivative formulas (maximum finite-difference errors below \(1.8\times10^{-10}\)), omitted-term mutations, noncommutative Cook ordering with its nonzero vacuum residual, the energy-kernel expansion, creator energy padding, the zero-kernel control, exact rational margins in (N33), and all-spectator/time-tail exponent bookkeeping. The infinite-series counterexample and analytic locality/convergence proofs are written arguments, not finite-sampling conclusions. These are author controls and do not replace independent review.

Frozen author operational record: The fixed campaign deadline is 2026-10-12 16:00:52 UTC. This recovery author changed no repository, Git reference, PR, audit, axiom, primitive or prompt file, and performed no subdelegation or model/effort override. Editable prompt files changed: none.


## Publication evidence and review record

The frozen author source is `NONISOLATED_MASS_SCATTERING_PROBE.md`, SHA-256 `afd35b7b1ec2e564e7ea418b1233148009509359212db8312599cb535bb6b80d`.
The separate source review is `NONISOLATED_MASS_SCATTERING_REVIEW.md`, SHA-256 `09da880b4ebdf629cffcc72c490176e6706b0ae4b01790eb3a267b6d8b284143`,
with review receipt SHA-256 `9f2a7ef9c691f0edfbcc257340444b4923dcb48e771fa5e41a9d4f19f5573da4`. The complete source,
review, controls, output streams, failures, source revisions and root coverage
records are indexed by the [evidence map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/EVIDENCE_MAP.json).
The [exact transformation map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/PUBLICATION_EDITS.json) and
[reconstruction program](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/reconstruct.py) recover the entire note
and primary from their frozen bytes. Historical write-scope and pending-review
statements above describe the author freeze; the following record describes
the completed source review. Root contributed the mechanisms and is a coauthor,
not the independent reviewer. No new review was performed by the packaging worker.

The review supports N1-N31 and the beta=1 spectral example N32-N35. Its
one required mathematical repair is explicit: the general-beta conversion
now defines the weighted Casimir and consistently uses that variable in N36
and its regularity sentence. The frozen original remains unchanged. The
repair-only note, before any publication metadata, has SHA-256
`4fde0f00866d19decdbc3d9fc648bba510d14f78cacd31e5134c9e88f2854d7c`.
The exact before/after fragment, beta=2 counterexample and separate algebraic
and spectral checks are preserved in `nonisolated_mass_review/N36_PUBLICATION_REPAIR.json`.
No other proof edit is made.

The reviewer saw source text, receipt metadata and prior reviews. Its initial
reconstruction and distinct continuum control froze before opening the new
author helper/output. A first quadrature run failed; the refinement retained
its cases and gates, and both source versions and logs remain. The later N36
finding supersedes the reconstruction's preliminary assessment. The original
author helper reproduced byte for byte. Of fourteen actual-source mutations,
eleven defects were rejected, two defect gates were nondiscriminating and a
benign weakened padding inequality survived. Specifically, deleting both
compensating energy-word terms or setting the finite Casimir detuning to zero
could survive the relevant author gates. These limitations are preserved;
finite arithmetic does not establish the analytic inequalities or convergence.

The source's infinite-tail witness concerns only the declared commuting
spectral data. It is not a finite-range lattice countermodel. The Cook power
condition is sufficient; comparison covers all fixed positive sublinear
widths. The reviewed `SCOPE_STRESS_TEST.md` remains part of the evidence.
No regular-creator existence/density, multiparticle nontriviality, Fock or
detector extension, all-channel coverage or microscopic model is supplied.


The [canonical finite primary](../scripts/nonisolated_mass_scattering_2026_10_12.py) is separate from the
analytic proof. For the mass and regularity primaries, `TOTAL` counts one
completed assertion-guarded driver; for the joint primary it counts its recorded
finite predicates. Neither total is a proof grade. Canonical execution, whole-
source mutation replays, current cache creation, graph acknowledgment and final
focused checks were **not run by preparation**. Their actual results must be
recorded in [delivery checks](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/DELIVERY_CHECKS.md) before publication.
No helper-registry policy change or formal audit is performed here.

The complete frozen argument retains its supplied conditions, scoped negative
witnesses and open application obligations. No Lean certificate, applied audit
verdict, retained promotion, new physical axiom or microscopic model is asserted.
The global combined pipeline and strict audit lint remain independent landing
gates. This is a frozen milestone packet; the sole live campaign checkpoint
remains in the transport worktree. Editable prompt files changed: none.


Checker pairing: the authors and focused reviewers used separate worker
contexts of the same configured model family, preserving the user's selected
model and reasoning effort. Different model families and blind checking are
not claimed. The distinct reconstruction/control mechanisms and actual source
exposure are documented above and in each complete source review. This pairing
disclosure is not an independent-audit grade or a retained-status decision.
