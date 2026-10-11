---
claim_id: compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "Supplied microscopic commuting flows, isolated mass components, finite centre spectrum and separated compact packets imply almost-local creators, finite-product scattering limits and commutant covariance. No Fock isometry or full-GNS completeness is asserted."
upstream_dependencies: []
runner: scripts/compact_patch_scattering_covariance_2026_10_11.py
actual_current_surface_status: conditional-support
---

# Compact-patch scattering and commutant covariance

**Claim type:** bounded theorem. **Status:** conditional-support; the complete argument received a separate source review. **Trace:** upstream support for N1's constructive scattering/HR-covariance premise. **Full-GNS completeness:** unproved and not assumed in the theorem below. No physical axiom, retained status, audit verdict, or N1 certification is supplied.

Under the explicitly supplied microscopic implementations, an isolated exact mass shell and a finite set of momentum-centre phases, joint \(H/P\) filtering produces almost-local creators on one continuous-momentum patch. Packets formed with geometric lattice shifts then have strong incoming and outgoing finite-product limits and the required \(V_j\) covariance. The proof gives an integrable \((1+|t|)^{-2}\) Cook bound with all derivative terms included. It works even when the chosen shell overlaps other spectrum at fixed geometric lattice momentum, because the filter separates the additional commuting continuous momentum before packets are formed.

The scattering mechanism is the Haag–Ruelle Cook argument of Bachmann–Dybalski–Naaijkens (BDN), with its almost-locality proof adapted to several microscopic flows. This is a source-matched application and extension of the creator construction, not a new scattering mechanism. The result concerns finite families of admissible packets and their scattering span. It does not supply a Fock-space isometry, asymptotic completeness, or the full-algebra identity \(\alpha_t=\tau_q\).

## 1. Sources, exact scope, and literature match

Primary source: S. Bachmann, W. Dybalski, P. Naaijkens, [*Lieb–Robinson bounds, Arveson spectrum and Haag–Ruelle scattering theory for gapped quantum spin systems*, arXiv:1412.2970v2](https://arxiv.org/abs/1412.2970v2), published in *Annales Henri Poincaré* 17 (2016), 1737–1791. The versioned [PDF](https://arxiv.org/pdf/1412.2970v2) was downloaded on 2026-10-11 and is preserved in the external research directory at `resume_20261011/compact_patch_scattering/sources/BDN_1412.2970v2.pdf`, SHA-256 `3edeb48a167b9ae6a26d6d885ccde03b068423d432176a256eb0a4ee42a14126`. Complete page texts 7–23 and 40–43 were read by the author and independent reviewer; all page texts remain in external recovery, without claiming all were read. The [milestone evidence map](../.claude/science/physics-loops/toe-compact-patch-scattering-20261011/EVIDENCE_MAP.json) records reference hashes and the official URL; complete third-party papers are not redistributed.

| Exact BDN item | Role here | Hypothesis match and limit |
|---|---|---|
| Theorem 2.1, Corollary 2.2, Appendix C Proposition C.2, especially (C.7) | LR dynamics and finite-region approximants | Each supplied current and \(H\) has a translation-invariant bounded finite-range interaction, hence finite BDN interaction norm. |
| Definition 3.8, Lemma 3.9, Theorem 3.10 and Appendix C | Almost locality, rapid spatial commutators, Schwartz smearing | The parameter truncation in §3 extends the same proof to \(d+1\) commuting microscopic flows. |
| Definition 4.1 and Definition 4.4 | Distinguish shell isolation from creator properties | BDN's geometric energy–momentum isolation/transfer condition is **not** silently assumed for the folded shell. It may fail. |
| Proposition 4.3 | Polynomial packet \(\ell^1\) bounds and rapid off-velocity tails | Smooth dispersion on a chart and compact smooth packet support suffice for the bounds used here; no global isolated Bloch band is needed. |
| Lemmas 4.5(a,b,d), 4.6(a), Theorem 4.8 and its proof | Constant vacuum vectors, both derivative terms, commutator decay, finite-product Cook limits | These are reconstructed below from directly verified creator properties. This is a proof-level reuse, not an invocation of Theorem 4.8 with its unverified Definition 4.4 hypothesis. |
| Theorems 4.9 and 4.13 | Delimit stronger assertions | Their Fock inner-product/isometry claims need further arguments; they are not consequences of the Cook estimate and are not imported as conclusions here. |

Repository source reports are the previously fully read `C4_N1_report.md`, `C4_B1_report.md`, and `C4_M1_report.md`, with SHA-256 respectively:

```text
c284a41bfee8a1238643330ddd46f3a7c4f6f1a865509a9aaec5ab6f4238ad13
95044a142cf94ad397c5f7b2bdf806905d2f40bb166fb8d5920fb5daf54a7a0e
fb2d6b5f54fcff8680219dce5f903d6620e5f987d4f093462502dc3e600b1b2b
```

Their Git prefix is `.claude/science/exercises/gravity-current-state-20261009/agents/`. They agree at PR heads `dec0b37467be8cd7b47449833a734e1c799dc1c0` and `407f99203a553b336f98e832213045ed49f7fc13`. All three report identities were also rechecked unchanged at `0cc560e3935fa1ad7623592bf9974680c922d52d`. Main `a13caa4885f547c8d206265b031ba7649e539fd9` was checked against the remote main ref on 2026-10-11 at 23:44 UTC. The motivating assessment `INDEX_TO_PHYSICS_NEXT_OBLIGATION.md` has SHA-256 `cb512af29397a3a6e8c58161bbe1dd6c15e61944b5f8bdd9ae0c1a0cc53c2536` and remains unchanged. N1 lines 39–45 supply the setting; lines 156–168 and 271 name the scattering/HR-covariance dependence. M1 line 234 explicitly leaves scattering convergence unproved. B1-U does not address this unbounded mass-shell setting.

The accepted partial-factor index review and its sources remain unchanged and are not proof inputs to the scattering argument. No Y1/RZ science is assessed. Main searches for Haag–Ruelle and scattering/almost-locality matches, with full outputs in the evidence directory, found no matching main theorem; one spectral-response filtering hit was context-only. No broad novelty claim follows from that search.

## 2. Supplied hypotheses and fixed conventions

Let \(\mathcal A\) be the quasilocal tensor-product algebra of finite-dimensional sites on \(\mathbb Z^d\), \(d\ge1\), with geometric translations \(\tau_x\). Let \((\pi,\mathcal H,\Omega)\) be a nonzero vacuum GNS representation. We suppress \(\pi\) on operators after their algebraic construction.

**S1 — Microscopic implementation.** A translation-invariant, uniformly bounded finite-range interaction generates \(\alpha_t\) on \(\mathcal A\), implemented by \(e^{itH}\), with \(H\ge0\) and \(H\Omega=0\). For \(\beta>0\), set \(K_a=P_a/\beta\). Each \(K_a\) is the actual generator of a supplied bounded finite-range current interaction, and

\[
\rho_y=\operatorname{Ad}e^{-iy\cdot K}
\tag{1}
\]

is the corresponding microscopic automorphism, with \(K_a\Omega=0\). The operators \(H,K_1,\ldots,K_d\) strongly commute. Their implementers commute with the geometric translation implementers \(T_x\), all fixing \(\Omega\). These are implementations of the stated microscopic derivations, not merely formal infinite sums. A formal Lie-algebra identity alone does not supply S1.

**S2 — Isolated exact mass component.** For each particle family used below, the joint spectral function

\[
\mathcal C=H^2-\beta |K|^2
\]

has a nonzero eigenspace \(\mathcal H_M=E_{\mathcal C}(\{M^2\})\mathcal H\), \(M>0\), with an open spectral gap around \(M^2\). Write \(E_M\) for this projection. Thus the positive-energy joint spectrum on \(\mathcal H_M\) lies on the graph

\[
E_M(k)=\sqrt{M^2+\beta|k|^2}.
\tag{2}
\]

The same symbol \(E_M(k)\) denotes the scalar dispersion only when an argument is displayed. The mass component is supplied; a gap above the vacuum alone does not guarantee it.

**S3 — Commutant symmetry and centre condition.** Define

\[
R_y=e^{-iy\cdot K},\qquad V_j=R_j^*T_j,
\qquad \nu_j=\operatorname{Ad}V_j=\rho_{-j}\tau_j.
\tag{3}
\]

The \(V_j\) form a representation of \(\mathbb Z^d\), commute with \(H,K,T_x\), and fix \(\Omega\). N1 obtains the stronger Poincaré-commutant statement under its integrated covariance hypotheses; only the displayed properties are used here. For the mass components to be selected, assume one common positive integer \(q\) with

\[
V_{q e_a}|_{\mathcal H_M}=1\quad(a=1,\ldots,d).
\tag{4}
\]

This is the operator form of the supplied rational-centre condition, including multiplicity spaces. Equation (4) is **not** imposed on the rest of \(\mathcal H\).

**S4 — Patch and packet data.** Choose a nonzero centre component of \(\mathcal H_M\), and an open continuous-momentum chart \(O\) on which the projection to the torus is one-to-one. Shrink to a single lift so that the integer \(n\) in (6) is fixed on the chart. Every packet has smooth compact Fourier support strictly inside its chart. For each fixed finite product, the compact group-velocity supports of its packets are pairwise disjoint. Nothing is asserted for nonseparated packet products without an additional extension argument.

The exact centre and clock conventions are:

\[
T_x=e^{-ix\cdot Q},\qquad
V_j|_{\theta}=e^{i\theta\cdot j},\qquad
Q\equiv k-\theta\pmod{2\pi}.
\tag{5}
\]

On a chosen lift, \(k=p+\theta+2\pi n\), and the geometric-momentum dispersion is

\[
\Sigma(p)=\sqrt{M^2+\beta|p+\theta+2\pi n|^2}.
\tag{6}
\]

If a centre is instead named by the convention \(Q=k+\theta\), its phase in (5) is \(e^{-i\theta\cdot j}\). These are equivalent centre labels; their signs cannot be mixed within one calculation. Rationality and finite order are unaffected. The scattering time is the \(+itH\) convention in S1. The N1 current-flow identity, if later supplied, uses \(\operatorname{Ad}e^{-isP_b}\) at \(s=q/\beta\), equivalently generator \(P_b/\beta\) at time \(q\).

## 3. Joint filtering is almost local, including time derivatives

Fix \(\lambda>0\) and a common summable LR function \(F\) with finite convolution constant \(C_\lambda\), as in BDN §2.2. Every finite-range interaction here has finite norm \(N_\ell=\|\Phi_\ell\|_\lambda\). For example, if its range is \(r_\ell\) and \(J_\ell=\sup_x\sum_{Z\ni x}\|\Phi_\ell(Z)\|<\infty\), then

\[
N_\ell\le J_\ell/F_\lambda(r_\ell),\qquad
v=\max_\ell\frac{2N_\ell C_\lambda}{\lambda},
\qquad C_0=\frac{4\|F\|}{C_\lambda}.
\tag{7}
\]

Signs of the current flows do not change these norm bounds. Let \(\mathbb E_Y\) be the product-trace conditional expectation onto \(\mathcal A(Y)\). BDN (C.7), using the LR bound outside a region containing the \(r\)-neighbourhood of the initial support, gives

\[
\|(1-\mathbb E_{X^r})\sigma_u^{(\ell)}(A)\|
\le C_0|X|\|A\|e^{-\lambda(r-v|u|)}
\quad(A\in\mathcal A(X)).
\tag{8}
\]

For \(g\in\mathcal S(\mathbb R^{d+1})\), define the norm-convergent Bochner integral

\[
B_g(A)=\int g(s,y)\alpha_s\rho_y(A)\,ds\,dy.
\tag{9}
\]

Let \(m=d+1\), \(a=[2m(1+v)]^{-1}\), and \(A\in\mathcal A(X)\). For \(|(s,y)|_1\le ar\), approximate the \(m\) individual flows successively, applying a conditional expectation after each flow onto \(X^{\ell r/m}\) at step \(\ell\). Call the final local operator \(A_r(s,y)\). All conditional expectations are contractive. A telescoping use of (8), with each intermediate support bounded by \(|X|(2r+3)^d\) for \(r\ge1\), gives

\[
\|\alpha_s\rho_y(A)-A_r(s,y)\|
\le m C_0|X|(2r+3)^d\|A\|e^{-\lambda r/(2m)},
\quad A_r(s,y)\in\mathcal A(X^r).
\tag{10}
\]

Here \(v|s|\) and each \(v|y_a|\) are at most \(r/(2m)\). Integrate \(A_r\) only over this parameter region. The resulting \(B_{g,r}\in\mathcal A(X^r)\) satisfies

\[
\begin{split}
\|B_g(A)-B_{g,r}\|
\le {}&m C_0|X|(2r+3)^d\|A\|\|g\|_1 e^{-\lambda r/(2m)}\\
&+\|A\|\int_{|z|_1>ar}|g(z)|\,dz.
\end{split}
\tag{11}
\]

The second term is \(O(r^{-N})\) for every \(N\), by Schwartz decay. Thus (9) is almost local. The constants depend on the microscopic interaction norms, \(d\), the fixed seed support and the Schwartz seminorms of \(g\); they are finite for the fixed data. They need not be uniform over infinitely many shell patches or increasing particle number.

All time derivatives are controlled by the same argument. Translation of the integrable kernel gives

\[
\delta_H^a B_g(A)=B_{(-\partial_s)^a g}(A),
\qquad \delta_H B=\left.\frac{d}{dt}\alpha_t(B)\right|_{t=0}.
\tag{12}
\]

This is a norm derivative, proved by convergence of translated kernels in \(L^1\); it does not require taking an unbounded-generator commutator on an unspecified domain. Every kernel on the right is Schwartz, so every displayed derivative is almost local. Fixed finite microscopic flows and fixed geometric translations preserve almost locality, by first approximating the input locally and then applying (8). Hence each fixed \(\nu_j\) also preserves this class and commutes with its time derivatives.

**Failed estimate retained.** It is invalid to bound (9) by integrating an exponential-in-parameter LR prefactor against an arbitrary Schwartz kernel. For example, \(g_0(u)=\exp[-(1+u^2)^{1/4}]\) is Schwartz but \(e^{c|u|}g_0(u)\) is not integrable for any \(c>0\). Equation (11) uses contractivity on the parameter tail and never asks for an exponential moment. This is a defect of that estimate, not a failure of the filtering construction.

## 4. Exact mass and centre selection

Choose \(h\in C_c^\infty(O)\). Let \(\eta\in C_c^\infty(\mathbb R)\) equal one at \(M^2\), with support in a spectral-isolation interval for \(\mathcal C\). Choose \(\chi\in C_c^\infty((0,\infty))\) equal one on the energies \(E_M(\operatorname{supp}h)\). Set

\[
G(E,k)=\chi(E)h(k)\eta(E^2-\beta|k|^2),
\qquad
g(s,y)=\frac1{(2\pi)^{d+1}}\int e^{-iEs+ik\cdot y}G(E,k)\,dE\,dk.
\tag{13}
\]

Then \(G\) is smooth and compactly supported, \(g\) is Schwartz, and the joint spectral theorem with the signs in (1) gives

\[
B_g(A)\Omega=G(H,K)A\Omega=h(K)E_M A\Omega.
\tag{14}
\]

This is exact selection in \((H,K)\), not a separation claim in \((H,Q)\). The same Fourier calculation for the adjoint gives \(B_g(A)^*\Omega=0\), since its transfer function is \(\overline{G(-E,-k)}\), supported at negative energy, while \(H\ge0\). Its temporal energy transfer is confined to the compact positive-energy projection of \(\operatorname{supp}G\).

Joint \(H/K\) filtering alone does not select a momentum centre. For \(\theta\in(2\pi/q)\mathbb Z^d\) modulo \(2\pi\), define

\[
\mathcal P_\theta(B)=q^{-d}\sum_{z\in\{0,\ldots,q-1\}^d}
e^{-i\theta\cdot z}\nu_z(B).
\tag{15}
\]

On \(\mathcal H_M\), the corresponding unitary average is precisely the joint character projection \(\Pi_\theta^M\), by (4). For

\[
B=\mathcal P_\theta(B_g(A)),
\qquad B\Omega=\Pi_\theta^M h(K)E_M A\Omega,
\tag{16}
\]

almost locality, all the derivatives in (12), and \(B^*\Omega=0\) are preserved. The finite average is not asserted to be a projection on arbitrary operators or on the full Hilbert space. It uses no global identity \(V_j^q=1\).

Assume the selected centre/patch spectral projection is nonzero. Cyclicity of \(\Omega\) then ensures nonzero creators can be chosen. More generally, as local \(A\) and smooth cutoffs \(h\) vary, (16) spans a dense subspace of the selected open patch: approximate its spectral projection by such bounded smooth spectral multipliers and use density of \(\mathcal A_{\rm loc}\Omega\). This is one-particle density only.

On the support of (16), (5) gives a single geometric-momentum graph (6). Other states at the same \((E,Q)\) do not contaminate (14). Nevertheless, the geometric Arveson spectrum of \(B\) can intersect other parts of the global spectrum. BDN Definition 4.4 is therefore not automatically met. The following argument uses the exact graph support of \(B\Omega\), smoothness/almost locality, and geometric packet separation directly.

## 5. Geometric packets and both derivative terms

Use normalized Haar measure \(dp/(2\pi)^d\) on the torus. For a creator (16), choose \(\widehat f\in C_c^\infty\) inside the chosen chart and define

\[
f_t(x)=\int_{\mathbb T^d}e^{ip\cdot x-it\Sigma(p)}\widehat f(p)\,
\frac{dp}{(2\pi)^d},\qquad
C_t(B,f)=\sum_{x\in\mathbb Z^d}f_t(x)\alpha_t\tau_x(B).
\tag{17}
\]

One may extend \(\Sigma\) smoothly outside the support to define the formula on the torus. That extension asserts nothing about the physical spectrum outside the chart. The sums and their first derivatives converge in norm on bounded time intervals. Fourier inversion and graph support give the exact identities

\[
C_t(B,f)\Omega=\widehat f(Q)B\Omega=:\psi,
\qquad
D_t(B,f)\Omega=0,
\tag{18}
\]

where

\[
D_t(B,f):=\frac{d}{dt}C_t(B,f)
=C_t(\delta_H B,f)+C_t(B,\dot f),
\quad
\dot f_t(x)=\int e^{ip\cdot x-it\Sigma(p)}[-i\Sigma(p)\widehat f(p)]\frac{dp}{(2\pi)^d}.
\tag{19}
\]

In (18), the factor \(e^{itH}\) cancels \(e^{-it\Sigma(Q)}\). Both terms in (19) are necessary. The second packet has the same velocity support bound as the first. The proof differentiates the **uncut** packet (17). Spatial velocity cutoffs enter only as estimates afterward; no derivative of a moving cutoff has been omitted.

## 6. Quantified commutators and the finite-product Cook bound

Write \(T=1+|t|\), \(|t|\ge1\). For each packet \(i\), let

\[
\mathcal V_i=\{\nabla\Sigma_i(p):p\in\operatorname{supp}\widehat f_i\}.
\]

Choose \(0\le\chi_i\le1\), smooth and compactly supported in velocity space, equal to one near \(\mathcal V_i\), with pairwise disjoint supports separated by \(\delta>0\). Set \(f_i^{(0)}=f_i\), \(f_i^{(1)}=\dot f_i\), and choose finite constants

\[
\sum_x|f_{i,t}^{(a)}(x)|\le L_i^a T^d,
\qquad
\sum_x|(1-\chi_i(x/t))f_{i,t}^{(a)}(x)|\le R_{i,N}^aT^{-N},
\quad a=0,1.
\tag{20}
\]

These are BDN Proposition 4.3 applied also to the amplitude \(-i\Sigma_i\widehat f_i\). For completeness, outside the velocity collar the phase gradient \(x-t\nabla\Sigma_i(p)\) is bounded below by a positive multiple of \(|x|+|t|\). Repeated integration by parts in \(p\), on compact smooth support, gives \(O((1+|x|+|t|)^{-M})\) for arbitrary \(M\). Summing with \(M>N+d\) gives the tail in (20). Inside the collar there are \(O(T^d)\) lattice sites and the Fourier integral is uniformly bounded, giving the first estimate. These estimates hold also as \(t\to-\infty\). Their constants depend on finitely many dispersion/amplitude derivatives and the chosen collar, not on \(t\).

Let \(B_i^a=\delta_H^a B_i\), \(b_i^a=\|B_i^a\|\), \(a=0,1\). Almost locality gives, for any integer \(N\ge0\), finite constants

\[
\|[B_i^a,\tau_z(B_k^b)]\|\le K_{ik,N}^{ab}(1+|z|)^{-N}.
\tag{21}
\]

Indeed, replace both operators by conditional-expectation approximants at radius \(|z|/3\); these commute, and the two approximation errors decay to arbitrary order. For example, with \(\epsilon_N(A)=\sup_{r\ge1}(1+r)^N\|A-\mathbb E_{B_r}(A)\|\), the safe bound

\[
K_N(A,B)\le2\,7^N\big(\|A\|\|B\|+\epsilon_N(A)\|B\|+\|A\|\epsilon_N(B)\big)
\tag{22}
\]

covers small as well as large \(z\). All these seminorms are finite by §3.

There is **no** exponentially growing physical-time factor in the equal-time commutator:

\[
\|[\alpha_t\tau_x(A),\alpha_t\tau_y(B)]\|
=\|[A,\tau_{y-x}(B)]\|.
\tag{23}
\]

For near-cone positions, \(|x-y|\ge\delta|t|\ge\delta T/2\). Let \(\kappa_N=\max(1,2/\delta)^N\). Splitting each packet into its \(\chi_i(x/t)\) part and its remainder, and using (20)–(23), gives

\[
\|[D_i(t),C_k(t)]\|\le A_{ik,N}T^{2d-N},\qquad i\ne k,
\tag{24}
\]

where one explicit sufficient constant is

\[
\begin{split}
A_{ik,N}=\sum_{a=0}^1\Big[&\kappa_NK_{ik,N}^{1-a,0}L_i^aL_k^0\\
&+2b_i^{1-a}b_k^0\big(R_{i,N}^aL_k^0+L_i^aR_{k,N}^0\big)\Big].
\end{split}
\tag{25}
\]

The first term bounds two near-cone pieces. A tail piece has operator norm at most \(b_i^{1-a}R_{i,N}^aT^{-N}\), and the other full packet at most \(b_k^0L_k^0T^d\); its commutator is bounded by twice the product. The two tail terms initially scale as \(T^{d-N}\), which is at most \(T^{2d-N}\). Equation (25) includes both terms of (19).

Now fix any finite \(n\) and put

\[
\Psi_t=C_1(t)\cdots C_n(t)\Omega,
\qquad c_i=b_i^0L_i^0,
\quad\|C_i(t)\|\le c_iT^d.
\]

For \(n\ge2\), differentiate, then commute each \(D_i(t)\) to the right. Its final action on \(\Omega\) vanishes by (18). The exact expression is a sum over \(i<k\), with one \([D_i,C_k]\) and all the other \(n-2\) factors in their original relative order. Consequently

\[
\|\dot\Psi_t\|
\le\sum_{i<k}A_{ik,N}\prod_{\ell\ne i,k}c_\ell\,T^{dn-N}.
\tag{26}
\]

Choose \(N=dn+2\), and define

\[
C_n=\sum_{i<k}A_{ik,dn+2}\prod_{\ell\ne i,k}c_\ell.
\]

Then

\[
\boxed{\ \|\dot\Psi_t\|\le C_n(1+|t|)^{-2}\ },
\qquad
\|\Psi_{t_2}-\Psi_{t_1}\|\le\frac{C_n}{1+t_1}
\quad(t_2\ge t_1\ge1).
\tag{27}
\]

The analogous estimate holds toward negative infinity. Hence both limits \(\Psi^\pm=\lim_{t\to\pm\infty}\Psi_t\) exist strongly. For \(n=1\), (18) is already constant; \(n=0\) is the vacuum. No restriction on the finite \(n\) was introduced. No uniform bound in \(n\) or in vanishing velocity separation is claimed.

The same argument without the derivative, using (21) for \(B_i,B_k\), shows that exchanging adjacent packet factors changes \(\Psi_t\) by a quantity tending rapidly to zero. Thus finite-product limits are permutation symmetric for these ordinary almost-local observable creators. Charged cone-local or graded field constructions are not included.

## 7. Dependence on the one-particle data

First consider two families producing the same one-particle vectors \(\psi_i\), with every mixed pair carrying different particle labels having disjoint velocity supports. Telescoping the difference of their products gives terms with one difference \(E_i(t)=C_i(t)-\widetilde C_i(t)\). Equation (18) gives \(E_i(t)\Omega=0\). Commute it to the right. All resulting commutators have the bound used in (24), now without the derivative. Polynomial norms of the remaining factors are absorbed by choosing the almost-locality order as in (26). The difference of the limits is zero. This is the comparison step in BDN Theorem 4.8.

Within fixed dispersion charts, the mixed-support requirement can be removed by a cutoff refinement. Suppose both original families are separately velocity-separated and create the same \(\psi_i\) on the same chosen dispersion graph for each label. Let \(S_i\) be the compact geometric-momentum spectral support of \(\psi_i\). It is contained in both packet supports. Thus \(\nabla\Sigma_i(S_i)\) is separated from every other label's original and alternative velocity support. Choose a smooth \(h_i\), equal to one near \(S_i\), supported in a sufficiently small neighbourhood whose velocities remain separated from all those other supports.

Replace the first family's amplitude by \(h_i\widehat f_i\), retaining the same creator \(B_i\), and call the packet \(C_i^h(t)\). The discarded operator is an actual packet,

\[
F_i(t):=C_i(t)-C_i^h(t)
=C_t(B_i,f_i-f_i^h),\qquad
\widehat{f_i-f_i^h}=(1-h_i)\widehat f_i,
\qquad F_i(t)\Omega=(1-h_i(Q))\psi_i=0.
\tag{27a}
\]

No small operator norm of \(F_i(t)\) is asserted. Its packet velocity support is a subset of the **original** \(\mathcal V_i\), because the amplitude is \((1-h_i)\widehat f_i\). Every other original or refined first-family packet has support contained in its own original \(\mathcal V_k\). Thus \([F_i(t),C_k(t)]\) and \([F_i(t),C_k^h(t)]\) decay to arbitrary order for \(k\ne i\), by the same equal-time commutator proof. Telescope the difference of the original and refined products, then commute each \(F_i(t)\) to the right. Its terminal action is zero, and all remaining terms tend to zero by the finite-product power count (26). The refined limit therefore equals the original limit.

The refined operator packet's velocity support is restricted by its new Fourier amplitude to \(\nabla\Sigma_i(\operatorname{supp}(h_i\widehat f_i))\). By the choice of \(h_i\), it is separated from every alternative packet with a different label. The refined and alternative families are cross-compatible, so the comparison in the first paragraph identifies their limits. Equality of the one-particle vectors alone was used for the annihilation in (27a), not to shrink an unchanged operator packet's support. If any \(\psi_i=0\), commuting that entire factor to the right directly shows the product limit is zero, without a cutoff construction.

Therefore, for admissible finite products on the **fixed dispersion charts**, the limit depends only on the one-particle vectors and is independent of the local seed, filter, and packet realization. This proof does not compare inequivalent dispersion/centre assignments or assert that arbitrary nonseparated tensor data already define a bounded wave operator on Fock space; such an extension requires an inner-product/continuity theorem.

## 8. \(V_j\) covariance and its exact stopping point

For each fixed \(j\), \(\nu_j\) preserves almost locality and norm time-smoothness, commutes with \(\alpha_t,\tau_x\) and the joint spectral filters, and preserves the mass/centre/patch spectral subspaces.

The admissible class used in §§5–7 consists of creators with these direct properties: almost locality of the creator and its time derivatives, and exact vacuum-vector support on the chosen graph. The local-seed construction in §§3–4 supplies such creators. The transformed creator \(\nu_j(B_i)\) remains in this direct-property class; its seed \(\nu_j(A_i)\) need not be strictly local. This is the class to which the covariance argument applies. For these creators,

\[
V_j C_t(B_i,f_i)V_j^*=C_t(\nu_j(B_i),f_i)
\tag{28}
\]

exactly at every finite \(t\). The transformed family meets the same hypotheses and has one-particle vectors \(V_j\psi_i\), with unchanged packet velocity supports. Passing the fixed bounded unitary through the strong limit and using §7 gives

\[
\boxed{\ V_j\Psi^\pm(\psi_1,\ldots,\psi_n)
=\Psi^\pm(V_j\psi_1,\ldots,V_j\psi_n)\ }.
\tag{29}
\]

For centre eigenvectors, multilinearity and (5) yield

\[
V_j\Psi^\pm=e^{i(\theta_1+\cdots+\theta_n)\cdot j}\Psi^\pm,
\qquad V_j^q\Psi^\pm=\Psi^\pm.
\tag{30}
\]

Hence \(V_j^q\) is the identity on the closed span of the vacuum and all such constructed states. No global identity was used to build the centre filters. Conversely, (30) cannot imply a global identity without a density/completeness premise. It cannot imply equality of automorphisms on \(\mathcal A\) merely from faithfulness of \(\pi\).

In the assessment's separate vacuum setting, assume additionally
\(E_H(\{0\})=|\Omega\rangle\langle\Omega|\) and
\(\operatorname{spec}(H)\subset\{0\}\cup[m,\infty)\), with \(m>0\).
Let \(P_{\rm sc}\) project onto the closed span of all relevant constructed
scattering states over all needed patches, including \(\Omega\). The
downstream exhaustion condition in that setting is

\[
\|(1-P_{\rm sc})\mathbf1_{[m,E]}(H)A\Omega\|=0
\quad\text{for every local }A\text{ and finite }E,
\tag{EX}
\]

With those additional spectral assumptions, (EX) expresses full-GNS
completeness: the spectral cutoffs \(\mathbf1_{[m,E]}(H)\) tend strongly
to \(1-|\Omega\rangle\langle\Omega|\) as \(E\to\infty\), and the local
vectors \(A\Omega\) are dense. This equivalence is not asserted from
S1–S4 alone. Neither (27), one-particle density, nor (29) proves (EX).
The present theorem also does not prove that all finite-energy excitations
belong to isolated mass components, that the common rational denominator
exists, or that the supplied continuous generators are microscopic
implementations.

## 9. Checks, limits, and recovery

The [finite convention and product control](../scripts/compact_patch_scattering_covariance_2026_10_11.py) preserves the exact author control and checks finite character projections, the Fourier/centre and time signs, the noncommutative finite-product derivative identity modulo only \(D_i\Omega=0\), and the final power count. Its negative controls rejected a wrong centre weight, treating the centre average as a global projection without the finite-order spectrum, an omitted commutator pair, a reversed commutator, either omitted packet-derivative term, and double division by \(\beta\). The execution used the declared 60-second timeout, exited 0 in about 0.72 seconds, and preserved full stdout/stderr plus an execution receipt. The algebraic checks do not prove the analytic estimates, independence, or completeness; they are author controls, not independent review.

The statement/proof checks are the load-bearing evidence: (11) controls the joint filter without an exponential moment; (14) isolates the exact mass spectrum; (15) selects centres only on the supplied finite-order mass space; (18) cancels the one-particle clock; (25) includes both derivatives; (26) accounts for every factor; and (29) passes a bounded symmetry through an already established strong limit. A separate reviewer reconstructed the complete argument before inspecting the author-control evidence. The report is `924b2fa9d6175bcbc213d164da6322d3fde0d769f06a5608d4aadc1644f974be`; its sole downstream EX wording finding was resolved by the exact replacement confirmed in addendum `8135fdaf9481c492738eee35d7b360c0e4f864b9213fd9751218bd3ee64f3029`. This selective source review does not apply an audit verdict or retained status.

If a supplied mass value is not isolated, (13) cannot be claimed to produce the exact projection in (14). If centres have no suitable exact selector, joint \(H/K\) filtering alone does not produce the single graph (6). If the continuous generators are only formal or their flows fail the microscopic LR hypotheses, (11) is unavailable. These are explicit conditions of this construction, not claims that alternative scattering theories are impossible. No counterexample satisfying S1–S4 was found or asserted.

The useful next obligation is still full scattering exhaustion, with Fock inner-product/isometry and extension to all needed channels treated explicitly on the way. For the specified isolated mass components and finite packets under S1–S4, this result supplies a construction and symmetry action of the kind M1 assumed. It does not retire M1's complete scattering assumption or establish a complete N1 obstruction on the physical framework.

The [milestone packet](../.claude/science/physics-loops/toe-compact-patch-scattering-20261011/) preserves the complete original note, author evidence, independent reconstruction, exact EX repair and both review receipts. PUBLICATION_EDITS.json and reconstruct.py reproduce this note and its runner from those frozen sources. Earlier assessments and candidate-law reports are unchanged; no editable prompt, physical axiom, main branch, audit verdict or retained status is changed. The live campaign checkpoint remains in the transport worktree at `toe-dynamics-bridge-20261009/STATE.yaml` and `HANDOFF.md`. Fixed campaign deadline: 2026-10-12 16:00:52 UTC.
