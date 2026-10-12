---
claim_id: compact_patch_fock_isometry_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Under the compact-patch construction's supplied conditions and a unique gapped vacuum, selected mass/centre components have permanent scattering Gram matrices and covariant isometric Fock embeddings. Full-GNS exhaustion and boost covariance remain open."
upstream_dependencies:
  - compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
runner: scripts/compact_patch_fock_isometry_2026_10_12.py
actual_current_surface_status: conditional-support
---

# Compact-patch Fock inner products and isometric wave operators

**Claim type:** bounded theorem. **Status:** conditional-support; complete source review found no required correction. **Trace:** upstream support for the constructive scattering part of N1. The compact-patch construction remains a **provisional dependency**; its separate core review completed during this task and is recorded below without importing a Fock conclusion. Root proposed the regular-shell route and is a contributor, not an independent reviewer.

The construction admits a bosonic Fock inner-product and isometry extension if its provisional creator/existence statements hold and the vacuum has a unique ground-state vector with a positive spectral gap. N1's full H-gap clause already supplies that additional vacuum condition. Compact positive temporal transfer is furnished by the existing filter; the exact mass dispersions furnish nondegenerate Hessians. Momentum absolute continuity and density of velocity-separated tensor data are proved below rather than assumed.

The result is an isometric embedding of the Fock space over finitely many **selected isolated mass components** into the GNS Hilbert space. It does not prove that the range is the entire GNS space, that all particles lie in those components, or that boosts intertwine the scattering construction. No physical premise is adopted.

## 1. Exact sources and dependency boundary

The frozen predecessor is [compact-patch construction](COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md), whose complete frozen author source is preserved in its publication packet, SHA-256
d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a.
Its author receipt has SHA-256
23a9f9aa165a1b88183b07ab7f5234c5b3294bbfdbd526a3fd475f5752bf3059.
Neither file is changed. The dependencies used here are its supplied S1–S4 setting, almost-local filtered creators with exact vacuum graph support, positive compact temporal transfer, and existence/permutation of finite velocity-separated packet limits. The Fock Gram formula below gives its own well-definedness argument, so the predecessor's fixed-chart cutoff comparison is not a substitute for the present Fock-density proof.

During this derivation, the predecessor's independent review completed at SHA-256 924b2fa9d6175bcbc213d164da6322d3fde0d769f06a5608d4aadc1644f974be. Its sole finding concerned the separate downstream EX discussion's unstated gap/unique-vacuum setting. The proposed exact repair, SHA-256 d4aac1e14a20e82be994bd4b8de966f0063affcbaa22a40a173b126f77fa3516, was confirmed by the addendum at SHA-256 8135fdaf9481c492738eee35d7b360c0e4f864b9213fd9751218bd3ee64f3029. All three documents were read in full here. The core S1–S4 construction was supported; that review did not assess this Fock extension. Condition (F1) below explicitly supplies the additional vacuum hypotheses, and exhaustion remains unproved.

N1 is C4_N1_report.md, SHA-256
c284a41bfee8a1238643330ddd46f3a7c4f6f1a865509a9aaec5ab6f4238ad13.
The exact report was previously read fully; the complete setting and reduction in lines 1–190 were reread here. It is unchanged at PR source commits dec0b37467be8cd7b47449833a734e1c799dc1c0 and 407f99203a553b336f98e832213045ed49f7fc13. Its bytes were also verified unchanged at PR9476 revision `0cc560e3935fa1ad7623592bf9974680c922d52d`. Its own claim labels are not proof inputs. No Y1/RZ, RV4 or other changed science is certified.

Primary sources:

- **BDN:** Bachmann–Dybalski–Naaijkens, [arXiv:1412.2970v2](https://arxiv.org/abs/1412.2970v2), PDF SHA-256 3edeb48a167b9ae6a26d6d885ccde03b068423d432176a256eb0a4ee42a14126. Exact items: Theorem 2.4; Proposition 3.6 and its Appendix B proof; Theorem 3.11; Proposition 4.3; Lemmas 4.5(c), 4.6(b), 4.7(b); the regular-shell proof of Theorem 4.9; the wave-operator construction in Theorem 4.13 and Lemmas 4.15–4.19.
- **NS:** Nachtergaele–Sims, [Locality Estimates for Quantum Spin Systems, arXiv:0712.3318v1](https://arxiv.org/abs/0712.3318v1), PDF SHA-256 74829f87cc51d399613043a3abdc48ba3146c81292a09e4df1035b50eb464b5c. Theorem 4.1 and its full proof, PDF pages 9–12, give the clustering bound used by BDN. Interaction definitions on pages 3–4 were checked.

This is proof-level reuse of that regular-shell machinery. BDN's complete standing geometric-shell isolation premise is not asserted for folded towers. Each replacement creator property and each use of it are stated below. The pseudo-relativistic alternative is not used. No novelty claim is made for the scattering or Fock arguments.

## 2. Hypotheses and theorem

Retain the predecessor's conventions
\[
\alpha_t=\operatorname{Ad}e^{itH},\quad
K=P/\beta,\quad \rho_y=\operatorname{Ad}e^{-iy\cdot K},
\quad T_x=e^{-ix\cdot Q},\quad
V_j=e^{ij\cdot K}T_j.
\]
Here \(K=P/\beta\) is continuous momentum in the predecessor's notation; it is not the boost generator also called \(K\) in N1. A centre phase \(V_j=e^{i\theta\cdot j}\) gives \(Q=k-\theta\) modulo \(2\pi\).

Add the explicit vacuum condition
\[
\ker H=\mathbb C\Omega,\qquad
\operatorname{spec}(H)|_{\Omega^\perp}\subset[\gamma,\infty),
\qquad \gamma>0.                                      \tag{F1}
\]
Together with the finite-range microscopic \(H\)-interaction, this is exactly the hypothesis needed for exponential clustering. N1 H-gap's spectral clause on all of \(\Omega^\perp\) implies (F1). Mere uniqueness among translation-invariant states, without that spectral clause, would not suffice.

Choose a finite set \(\mathfrak M\) of positive masses satisfying the predecessor's isolated-Casimir hypothesis. On these components retain the supplied common \(q\) with \(V_{qe_a}=1\). For any chosen subset of their finitely many centre projections, define the actual Hilbert subspace
\[
\mathcal H_1=\bigoplus_{(M,\theta)\in I}\Pi_\theta^M E_M\mathcal H,
\qquad |I|<\infty.                                    \tag{F2}
\]
Distinct mass/centre summands are orthogonal. Momentum charts are coordinate covers of these summands, not extra species copies. All continuous momenta in each selected summand are allowed through a countable cover of relatively compact charts; no uniform estimate over that cover is required.

A creator \(B_i\) and packet use one such chart:
\[
\Sigma_i(p)=\sqrt{M_i^2+\beta|p+\theta_i+2\pi n_i|^2},
\quad
f_{i,t}(x)=\int e^{ipx-it\Sigma_i(p)}
                  \widehat f_i(p)\frac{dp}{(2\pi)^d},
\]
\[
C_i(t)=\sum_x f_{i,t}(x)\alpha_t\tau_x(B_i),\qquad
C_i(t)\Omega=\psi_i.                                  \tag{F3}
\]
The amplitude is smooth and compactly supported strictly inside the chart. The predecessor supplies almost locality, almost locality of time derivatives, exact graph support, and positive compact temporal transfer. Thus, for suitable \(0<\epsilon_i\le L_i<\infty\),
\[
\operatorname{Sp}_{\alpha}(B_i)\subset[\epsilon_i,L_i],
\qquad C_i(t)^*\Omega=0.                              \tag{F4}
\]
Finite sums within a fixed graph, and symmetry transforms preserving it, are admitted through these direct properties; a transformed seed need not be strictly local.

**Conditional theorem.** For two finite families separately having disjoint compact velocity supports, the provisional incoming or outgoing limits obey
\[
\left\langle\Psi^\pm(\widetilde\psi_1,\ldots,\widetilde\psi_m),
                    \Psi^\pm(\psi_1,\ldots,\psi_n)\right\rangle
=
\delta_{mn}\sum_{\sigma\in S_n}
       \prod_{j=1}^n\langle\widetilde\psi_j,\psi_{\sigma(j)}\rangle.
                                                               \tag{F5}
\]
The permanent on the right is evaluated for \(m=n\); the right side is zero for \(m\ne n\). There is no cross-family disjointness requirement. The dense span of these bosonic tensor products therefore defines unique isometries
\[
W^\pm:\Gamma_s(\mathcal H_1)\longrightarrow\mathcal H,\qquad
W^\pm\Omega_{\mathrm F}=\Omega,\quad
W^\pm a^*(\psi_1)\cdots a^*(\psi_n)\Omega_{\mathrm F}
       =\Psi^\pm(\psi_1,\ldots,\psi_n).                \tag{F6}
\]
The packet-limit identity in (F6) initially applies to admissible separated data. Other Fock vectors are defined by continuous extension; convergence of raw unseparated packet products is not asserted. The isometries intertwine the geometric space-time translations, the supplied continuous current translations, and the \(V_j\) action with their second quantizations restricted to \(\mathcal H_1\). Their ranges are closed scattering subspaces, with no assertion that either range equals \(\mathcal H\).

The extra vacuum condition (F1) is already supplied by N1. No additional absolute-continuity, Hessian-regularity, Fock, or asymptotic-completeness premise is imposed here. The microscopic implementation, isolated masses and finite-order centres remain the predecessor's explicit supplied assumptions.

## 3. Compact temporal transfer gives uniform finite-energy bounds

The predecessor's joint multiplier is
\[
G(E,k)=\chi(E)h(k)\eta(E^2-\beta|k|^2),
\qquad \chi\in C_c^\infty((0,\infty)).
\]
Smearing again in physical time by a Fourier multiplier equal to one on the energy projection of \(\operatorname{supp}G\) leaves the creator unchanged. Thus its temporal Arveson spectrum is in a compact interval \([\epsilon,L]\). The finite centre average commutes with \(\alpha\) and preserves this property. Geometric translations, physical time evolution and packet smearing preserve the interval too. Equivalently the joint geometric energy–momentum transfer lies in
\([\epsilon,L]\times\mathbb T^d\), a compact set, even though it need not isolate a shell in the global geometric spectrum.

Write \(P_R=1_{[0,R]}(H)\) and
\[
S_B=\sum_{z\in\mathbb Z^d}\|[B^*,\tau_z(B)]\|<\infty. \tag{F7}
\]
Almost locality makes the summand rapidly decreasing. The energy-transfer relation gives \(B^*P_R\subset P_{R-\epsilon}\mathcal H\), with zero output when \(R<\epsilon\). It gives this for every translate and hence for arbitrary mixed products of translates.

For completeness, the lattice form of the Buchholz estimate behind BDN Theorem 3.11 has the following direct proof. Put \(A_x=\tau_x(B^*)\), let \(\mathcal P_r\) be the orthogonal projection onto the intersection of the kernels of **all** \(r\)-fold products of the \(A_x\), and for a finite \(\Lambda\) let \(Q_\Lambda=\sum_{x\in\Lambda}A_x^*A_x\). Then \(A_x\operatorname{Ran}\mathcal P_r\subset\operatorname{Ran}\mathcal P_{r-1}\). Set
\[
b_r=\|\mathcal P_r Q_\Lambda\mathcal P_r\|,\qquad b_1=0.
\]
For a unit vector \(\Phi\in\operatorname{Ran}\mathcal P_r\), expand
\[
\langle Q_\Lambda^2\rangle_\Phi
=\sum_{x,y}\langle A_x\Phi,[A_x,A_y^*]A_y\Phi\rangle
 +\sum_{x,y}\langle A_yA_x\Phi,A_xA_y\Phi\rangle .
\]
The first sum in absolute value is bounded by
\(S_B\langle Q_\Lambda\rangle_\Phi\), using \(2ab\le a^2+b^2\) and the commutator row/column sums. Cauchy–Schwarz and the same inequality bound the second sum by
\[
\sum_{x,y}\|A_yA_x\Phi\|^2
\le b_{r-1}\langle Q_\Lambda\rangle_\Phi.
\]
Since \(\langle Q_\Lambda\rangle_\Phi^2
\le\langle Q_\Lambda^2\rangle_\Phi\), this proves
\(b_r\le b_{r-1}+S_B\), hence \(b_r\le(r-1)S_B\).
Energy transfer puts \(P_R\mathcal H\) inside \(\operatorname{Ran}\mathcal P_r\) whenever \(r\epsilon>R\). Increasing \(\Lambda\) then gives a bounded positive strong limit and
\[
\Gamma_B(R):=
\left\|P_R\sum_x\tau_x(BB^*)P_R\right\|
\le \left\lfloor R/\epsilon\right\rfloor S_B.          \tag{F8}
\]
This proof needs positive energy and the compact lowering interval, not an isolated geometric shell. Knowing only \(A^r=0\) would not justify the mixed-product kernel step.

Parseval gives \(\|f_t\|_{\ell^2}=\|\widehat f\|_{L^2(dp/(2\pi)^d)}=:F_2\). Vector-valued Cauchy–Schwarz and (F8) imply
\[
\|C(t)^*P_R\|\le F_2\sqrt{\Gamma_B(R)}.
\]
For the creator, its output from \(P_R\) lies in \(P_{R+L}\), so the dual Cauchy–Schwarz argument gives
\[
\boxed{
\|C(t)P_R\|\le F_2\sqrt{\Gamma_B(R+L)},\qquad
\|C(t)^*P_R\|\le F_2\sqrt{\Gamma_B(R)}\ }.             \tag{F9}
\]
Physical time evolution is removed from \(\Gamma_B\) because \(P_R\) commutes with it. These bounds are uniform in \(t\).

Consequently every fixed finite word of creators and annihilators, applied to \(\Omega\), is uniformly bounded: take \(R_*\) to be the sum of the upper transfer bounds of all factors, insert \(P_{R_*}\) at intermediate stages, and use (F9) at each stage. Negative transfers never increase this energy ceiling. This also bounds the norm of any corresponding vacuum row functional, by taking its adjoint. Constants can depend on the finite word and its filters.

## 4. Regularity and the mixed-creator clustering estimate

For \(k=p+\theta+2\pi n\) and \(E=\sqrt{M^2+\beta|k|^2}\),
\[
D^2\Sigma(p)=\frac{\beta}{E}I-\frac{\beta^2}{E^3}kk^{\mathsf T},
\qquad
\det D^2\Sigma(p)=\frac{\beta^d M^2}{E^{d+2}}>0.        \tag{F10}
\]
The transverse eigenvalues are \(\beta/E\), and the longitudinal one is \(\beta M^2/E^3\); at \(k=0\) all equal \(\beta/M\). On \(|k|\le R\) the smallest eigenvalue is at least
\(\beta M^2/(M^2+\beta R^2)^{3/2}\).
Thus the regular stationary-phase bounds in BDN Proposition 4.3 apply separately to every mass/centre chart:
\[
\|f_{i,t}\|_\infty\le u_i(1+|t|)^{-d/2},\qquad
\|f_{i,t}\|_1\le v_i(1+|t|)^{d/2}.                  \tag{F11}
\]
Smooth compact amplitudes, finite chart partitions and the already checked rapid off-velocity tails make these uniform in lattice \(x\). The constants need not be uniform as charts run to infinite energy.

Condition (F1) and the microscopic interaction imply exponential clustering. To make its constants explicit, use the NS interaction norm \(N_H=\|\Phi_H\|_\lambda\), summable \(F\), and convolution constant \(C_\lambda\). One may take
\[
\mu=\frac{\lambda\gamma}{4N_HC_\lambda+\gamma},\quad
C_{\rm cl}=2\left(1+\mu^{-1/2}
                     +\frac{2\|F\|}{\pi C_\lambda}\right).
\]
For nonempty finite supports \(X,Y\) at distance at least one,
\[
|\omega(AB)-\omega(A)\omega(B)|
\le C_{\rm cl}\|A\|\|B\|\min(|X|,|Y|)
                    e^{-\mu\,\operatorname{dist}(X,Y)}.         \tag{F12}
\]
This follows from NS Theorem 4.1 with imaginary time zero and
\(B-\omega(B)1\); its norm is at most \(2\|B\|\).
Uniqueness gives both ground-projection annihilation conditions of that theorem.
Finite range and bounded interactions give finite \(N_H\).
No gap or uniqueness for the current generators is required.

Let \(A_1,\ldots,A_4\) be any fixed almost-local observables, and set
\(P_\perp=1-|\Omega\rangle\langle\Omega|\). The BDN Lemma 4.7(b) proof yields, for every \(N\),
\[
|\langle\Omega,[\tau_{x_1}A_1,\tau_{x_2}A_2]
 P_\perp[\tau_{x_3}A_3,\tau_{x_4}A_4]\Omega\rangle|
\le D_N
 \prod_{(a,b)=(1,2),(2,3),(3,4)}
          (1+|x_a-x_b|)^{-N}.                       \tag{F13}
\]
Here are the relevant details. The first and third relative decays follow from almost-local commutators. For the middle decay put \(R=|x_2-x_3|\), approximate each \(A_i\) by its norm-bounded conditional expectation on a radius \(r\) ball, and take \(r=(1+R)/16\) for large \(R\). Either a local commutator vanishes or its two centres are at most \(2r\) apart. In the latter case the two pair supports have distance at least \(R-6r\), so (F12) bounds their connected correlation by a constant times
\((1+r)^d e^{-\mu(R-6r)}\). The almost-local approximation error is \(O(r^{-L})\) for arbitrary \(L\). This proves arbitrary middle-variable decay. Applying the three separate bounds at order \(3N\) and taking their geometric mean gives the product in (F13). Small distances are absorbed in \(D_N\).

Take two arbitrary admissible packets \(C_i(t)\), \(C_k(t)\), including ones on different mass/centre charts; their velocity supports may overlap. Since \(C_i(t)^*\Omega=0\),
\[
P_\perp C_i(t)^*C_k(t)\Omega
=P_\perp[C_i(t)^*,C_k(t)]\Omega.
\]
Its squared norm is a four-packet sum with the kernel (F13), after pulling out the common physical time evolution. The four scalar factors consist of two copies each of \(|f_{i,t}|\) and \(|f_{k,t}|\). For fixed three relative variables, bound one factor in \(\ell^1\) and the other three in \(\ell^\infty\). Equation (F11) contributes
\((1+|t|)^{d/2-3d/2}=(1+|t|)^{-d}\).
Taking \(N>d\) makes all three relative sums finite. Therefore
\[
\boxed{\ C_i(t)^*C_k(t)\Omega
 =\langle\psi_i,\psi_k\rangle\Omega+r_{ik}(t),
\qquad
\|r_{ik}(t)\|\le d_{ik}(1+|t|)^{-d/2}\ }.            \tag{F14}
\]
This is the regular-shell contraction estimate with its actual hypotheses exposed. The proof uses neither a common dispersion for the two packets nor geometric spectral isolation. Different mass/centre sectors give a zero scalar contraction by orthogonality in \(\mathcal H_1\).

## 5. Mixed velocity partitions and the Gram recursion

The predecessor's almost-local equal-time commutator estimate applies to creators or adjoints with disjoint packet velocity supports. For packets \(X(t),Y(t)\) with disjoint velocity supports and an arbitrary third admissible packet \(A(t)\), it also gives
\[
[[A(t),X(t)],Y(t)]=O((1+|t|)^{-\infty}),              \tag{F15}
\]
and the same with any adjoints.

For clarity, choose a smooth velocity-space function \(\chi\) equal to one near \(\mathcal V_X\) and zero near \(\mathcal V_Y\). Split the third amplitude by
\(\chi(\nabla\Sigma_A(p))\) and \(1-\chi(\nabla\Sigma_A(p))\), choosing collars so the first piece is separated from \(\mathcal V_Y\) and the second from \(\mathcal V_X\). The second piece has a rapidly small inner commutator. For the first, Jacobi expresses the double commutator in terms of its commutator with \(Y\) and the commutator of \(X\) with \(Y\). Both are rapid. Polynomial packet norms absorb the remaining factors. This partition works for any smooth third dispersion, so different masses, centres and lifts create no exception. Adjoints have the same spatial packet supports.

Write
\[
I_{m,n}(t)=
\langle\widetilde C_1(t)\cdots\widetilde C_m(t)\Omega,
                       C_1(t)\cdots C_n(t)\Omega\rangle .
\]
Commute \(\widetilde C_1(t)^*\) through the right-hand product. Its terminal action on \(\Omega\) is zero. Move each resulting
\([\widetilde C_1^*,C_k]\) to the right. All double-commutator terms vanish rapidly by (F15), since the right family is internally velocity-separated. Their remaining finite number of polynomial packet norms can be absorbed in the arbitrary decay order.

In the remaining terms insert (F14):
\[
\widetilde C_1(t)^*C_k(t)\Omega
=\langle\widetilde\psi_1,\psi_k\rangle\Omega+r_{1k}(t).
\]
Each error is multiplied by a vacuum row functional consisting of finitely many other packet factors. Its norm is \(O(1)\) by (F9), not merely polynomially bounded. Thus, for every fixed pair of families,
\[
I_{m,n}(t)
=\sum_{k=1}^n\langle\widetilde\psi_1,\psi_k\rangle
       I_{m-1,n-1}^{(k)}(t)+O((1+|t|)^{-d/2}),        \tag{F16}
\]
where the tilde label 1 and right label \(k\) are deleted. The rapid double-commutator contribution has been absorbed into this displayed rate.

For \(m=0<n\) or \(n=0<m\), the expression is zero because a terminal annihilator kills the vacuum; equivalently the adjoint of the first creator annihilates the vacuum row. For \(m=n=0\) it equals one. Iteration of (F16) proves (F5), including unequal particle numbers. This proof requires separation only within each family and works independently for \(t\to+\infty\) and \(t\to-\infty\).

Using only the predecessor's full operator-norm bound in the error term would fail: \(O(t^{-d/2})\) times an arbitrary product of polynomial packet norms need not tend to zero. Equations (F8)–(F9) provide the needed replacement. This is a repaired estimate, not a no-go statement.

## 6. Spectral absolute continuity and density

First, the constructed one-particle creator vectors are locally dense. For an open bounded continuous-momentum patch \(O\), the predecessor's exact formula is
\[
B\Omega=\Pi_\theta^M h(K)E_M A\Omega,
\qquad A\in\mathcal A_{\rm loc},\quad h\in C_c^\infty(O).
                                                               \tag{F17}
\]
Smooth bounded multipliers exhausting \(O\), together with cyclicity of \(\Omega\), show that these vectors span a dense subspace of
\(\Pi_\theta^M E_M1_O(K)\mathcal H\). Choosing the packet amplitude equal to one on the compact support of \(h\) realizes the same vector as \(C_i(t)\Omega\). A countable cover of continuous momentum gives density in \(\mathcal H_1\). This argument uses the supplied exact joint filter and centre selection; it does not use BDN's unverified geometric transfer-isolation condition.

For any such \(B\), \(B^*\Omega=0\), and
\[
\langle B\Omega,T_xB\Omega\rangle
=\langle\Omega,[B^*,\tau_x(B)]\Omega\rangle.            \tag{F18}
\]
Almost locality makes this sequence rapidly decreasing in \(x\). Fourier uniqueness then says that the \(Q\)-spectral measure of \(B\Omega\) has a smooth density with respect to normalized Haar measure on the torus. In particular every Haar-null set \(Z\) satisfies \(1_Z(Q)B\Omega=0\). By the just-proved density this holds throughout \(\mathcal H_1\).

On any fixed centre/lift chart, \(Q=k-\theta\) is a smooth measure-preserving change of coordinates modulo \(2\pi\). The chart projection commutes with \(Q\), so the same argument gives absolute continuity of the continuous \(K\)-spectral measures in that chart. Countably many charts give it on each selected summand. No global isolated Bloch band or Wigner-representation decomposition is used for this conclusion.

The physical velocity on a mass component is
\[
v_M(k)=\frac{\beta k}{\sqrt{M^2+\beta|k|^2}}.
\]
It is a smooth bijection from \(\mathbb R^d\) onto \(\{|v|<\sqrt\beta\}\), with inverse
\[
k_M(v)=\frac{Mv}{\sqrt{\beta}\sqrt{\beta-|v|^2}}.      \tag{F19}
\]
The Jacobian determinant of \(k\mapsto v_M(k)\) is the positive number in (F10). Thus for any two masses, and for each fixed momentum of the second particle, the first particle has at most one momentum with the same velocity. Fubini makes each pairwise equal-velocity subset Lebesgue-null in the product of two charts. Finite unions over pairs and countable unions over charts remain null.

The product spectral measure on \(\mathcal H_1^{\otimes n}\) assigns zero projection to these diagonals: scalar product measures of elementary tensors are absolutely continuous by (F18), and elementary tensors are dense. Hence the complement of coincident velocities has full spectral projection.

Finally cover that complement by products of relatively compact momentum neighbourhoods whose velocity images have disjoint closures. Such boxes exist by continuity and strict velocity inequality. Their spectral subspaces span a dense tensor subspace: a vector orthogonal to all box ranges is annihilated by the spectral projection of their union. In each factor, (F17) supplies a dense set of creator vectors inside the corresponding neighbourhood. Algebraic tensor products of these dense sets are dense in each box range. Symmetrizing proves that the span of admissible velocity-separated bosonic products is dense in every \(\Gamma_s^{(n)}(\mathcal H_1)\).

This is a density statement in the **asymptotic Fock space**, not density of the scattering range in the interacting GNS space.

## 7. Extension, covariance and remaining obligations

The standard bosonic vectors
\(a^*(\psi_1)\cdots a^*(\psi_n)\Omega_{\mathrm F}\)
have the Gram matrix on the right of (F5), with no extra factorial when this creation-operator normalization is used. Map each admissible such vector to its scattering limit. For any finite linear combination, (F5) preserves its squared norm. A zero Fock vector therefore has zero image, so the map is well defined even when a vector has different admissible creator/chart realizations. It extends uniquely by continuity to each particle sector. Different particle sectors have orthogonal images by (F5), so their Hilbert direct sum gives the isometries (F6).

For fixed geometric space-time translation \(e^{isH}T_x\), continuous current translation \(R_y=e^{-iyK}\), or \(V_j\), conjugation preserves the direct creator properties, its compact temporal interval and its selected mass/centre/patch. It also commutes with the packet's common \(\alpha_t\tau_z\). Its finite-time conjugated product is therefore the product constructed from the transformed one-particle vectors. Applying the fixed unitary through the provisional strong limit gives covariance on the dense admissible domain; (F5) and continuity extend it to (F6). In particular,
\[
V_jW^\pm=W^\pm\Gamma_s(V_j|_{\mathcal H_1}),\qquad
V_j^q=1\ \hbox{on }\operatorname{Ran}W^\pm.            \tag{F20}
\]
These finite transformations preserve almost locality; no transformed strictly local seed is required.

What remains is explicit:

- The predecessor remains a conditional source with supplied physical premises. Its core review and exact EX scope repair are separately bound above; neither assesses the present Fock extension or grants audit status.
- The complete Fock proof received a separate reconstruction of the energy restriction, mixed-chart contraction, full recursion and density steps. The review found no required correction; this is a source check, not an applied audit verdict or retained status.
- The microscopic implementations, isolated mass components and finite-order selected centres are supplied conditions, not derived physics.
- No boost/Poincaré intertwining theorem is established here.
- Full-GNS exhaustion would require \(\operatorname{Ran}W^\pm=\mathcal H\), including coverage of all relevant particle components. It remains a separate obligation. Isometries alone do not imply it.
- No claim about an isometric or unitary scattering matrix is inferred solely from two isometric wave operators.

The [Fock milestone packet](../.claude/science/physics-loops/toe-compact-patch-fock-20261012/) preserves the complete original note, source ledger, author checks, full outputs, separate review and pre-author-control reconstruction. PUBLICATION_EDITS.json and reconstruct.py recover this publication from those frozen sources. Complete third-party papers and page extractions remain in the external research directory, with exact hashes and official URLs in EVIDENCE_MAP.json. The finite controls concern algebra; they do not supply a physical premise or replace the analytic proof.

## 8. Author checks and evidence limits

The original author execution of the [finite Fock control](../scripts/compact_patch_fock_isometry_2026_10_12.py) used a declared 60-second timeout and exited 0 in about 0.69 seconds. The complete nine-record stdout, empty stderr, exact command, runtime and hashes are preserved in the evidence directory.

| Check | Exact target and limit |
|---|---|
| Free noncommutative expansion, 1–9 right factors | Checks the unreduced annihilator recursion and every double commutator before any vacuum/asymptotic replacements. Omitting double commutators is rejected. |
| \(Q_\Lambda^2\) expansion, 1–7 translates | Checks the identity used in the kernel induction without assuming the lowering operators commute. The inequalities themselves are proved in §3. |
| Symbolic Hessian in \(d=1,2,3\); inverse velocity in \(d=1,\ldots,5\) | Checks differentiated formulas. The dimension-independent matrix/eigenvalue argument is (F10). An explicit different-mass equal-velocity example rejects automatic separation by species. |
| Finite cyclic hard-core models, 1–3 sites and nine energy cutoffs | Exact principal-minor tests check the creator and adjoint bounds; \(\Gamma_B(R)=R\) saturates the count factor. Omitting the creator's energy padding fails already on the vacuum. These are algebraic controls, not infinite-lattice scattering models. |
| Mixed-kernel negative control | A square-zero operator can have a nonzero product with a translated copy. This preserves the distinction between all mixed-product kernels and mere powers of one operator. |
| Fock normalization and exponent bookkeeping | Checks factorial counts and 66 regular-contraction power counts. The normalization enumeration is not a separate proof of the analytic Gram recursion. |

No earlier compact-patch control was treated as a proof of these new claims. These author controls are distinct from the independent reconstruction. The separate review is `bc88af1dda77065d8806da9d689546547f40847a340177086793dab5f3a277cf`; its pre-author-control reconstruction is `85f4d93458c6f00ede645e6d2ac272084dc0cd053b66801b25db8574586df484`, frozen before the reviewer opened the author source, logs or receipt. The reviewer reconstructed the complete analytic argument and checked the original BDN and NS hypotheses/proofs. Separately written finite matrix and occupation-polynomial controls checked the algebra. The later exact author rerun reproduced its output; that rerun is reproduction, not an independent implementation. Root proposed the regular-shell route and is a contributor. Stationary phase, clustering, spectral density and the Hilbert-space extension rest on the written proofs and checked primary hypotheses. No Lean verification, full-GNS completeness, physical realization or retained status is claimed. Publication execution and its exact limits are in DELIVERY_CHECKS.md in the milestone packet.
