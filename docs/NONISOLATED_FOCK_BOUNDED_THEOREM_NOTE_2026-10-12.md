---
claim_id: "nonisolated_fock_bounded_theorem_note_2026-10-12"
claim_type: "bounded_theorem"
claim_scope: "Under the reviewed nonisolated scattering hypotheses, the full permanent Gram formula and incoming/outgoing Fock isometries hold over the closed span of actual regular targets. That span may be zero; no whole-sector density, onto, detector, massless-vacuum, S-matrix or physical realization conclusion is supplied."
upstream_dependencies:
  - nonisolated_mass_scattering_bounded_theorem_note_2026-10-12
  - compact_patch_fock_isometry_bounded_theorem_note_2026-10-12
runner: "scripts/nonisolated_fock_2026_10_12.py"
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "Construct nonzero regular seed targets in an actual model and separately address density, detectors and onto/exhaustion."
source_of_blocker_text: "handoff"
reachability_to_target: "partially_closes"
artifact_role: "theorem"
next_trace_action: "Construct nonzero regular seed targets in an actual model and separately address density, detectors and onto/exhaustion."
conditional_surface_status: "Fock isometries on the defined closed regular target space"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The dynamics, unique gap, reducing massive graphs and actual regular seed vectors remain supplied. Four bookkeeping mutations survive the finite author gates."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem


# Fock isometry for time-averaged regular massive graph targets

**Claim type:** bounded_theorem

**Actual current-surface status:** conditional-support; complete separate source review requires no mathematical correction. **Trace:** the Fock-inner-product and isometry obligation left open by the reviewed nonisolated-mass scattering construction. Root supplied an unverified small-width research lead and is a contributor. Neither this author proof nor its finite controls confer retained or audit status.

The time-averaged construction has a bosonic Fock isometry on the closed span of its actual regular seed targets, under the stated unique gapped vacuum, finite-range dynamics and compact massive graph hypotheses. The new estimate treats four independent averaging times. After choosing small fixed averaging powers by the preceding comparison theorem, localization and capped exponential clustering give a squared contraction remainder $O(T^{-d+3d\kappa})$, with $\max\nu_i<\kappa<1/3$. Uniform finite-energy bounds then give the full permanent Gram matrix, including orthogonality between different particle numbers.

The one-particle space is defined from regular targets that actually meet the spectral hypothesis. No density in an entire supplied physical mass sector is asserted. Its geometric momentum measures are absolutely continuous; smooth cutoff stability and the massive velocity maps give density of separated tensors in this defined space. Chart coordinates do not create additional species. The result gives closed scattering ranges, without onto, detector, ND, EX, boost, massless-vacuum or microscopic-model conclusions.

## 1. Source contract and exact theorem domain

S denotes the original research collection. The [frozen milestone handoff](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/HANDOFF.md) and [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserve the original source bundles and complete own evidence. The direct in-branch proof dependencies are [Mass](NONISOLATED_MASS_SCATTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md): N1-N31 existence, all fixed sublinear-width comparison, unequal-time locality and mixed-word energy bounds. Geometric regularity is imposed directly; N36 is not used.; [Fock](COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md): Checked contraction/Gram and finite-energy proof mechanism, reconstructed for the actual averaged nonexact-vacuum hypotheses; its old shell-density conclusion is not imported. Other named sources are historical context or transitive dependencies unless their use is stated explicitly. The complete source snapshots and identities are in `nonisolated_fock/source_manifest_initial.json`. The load-bearing predecessor is N = `NONISOLATED_MASS_SCATTERING_PROBE.md`, SHA-256 `afd35b7b1ec2e564e7ea418b1233148009509359212db8312599cb535bb6b80d`. Its independent review is SHA-256 `09da880b4ebdf629cffcc72c490176e6706b0ae4b01790eb3a267b6d8b284143`. That review supports N1–N31 and the beta=1 spectral control. It requires an explicit weighted-Casimir definition in N36. The exact `N36_PUBLICATION_REPAIR.json`, SHA-256 `22d272711226acccb48f0c2e167bd47bc5296d4142c7e60ac537c0ae6f74a453`, is preserved. N36 is not used here: geometric detuning regularity is imposed directly.

The original SC and Fock arguments were read completely, at SHA-256 respectively `d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a` and `9bc3a309e8fc35978bcac0c360b8557fb6a3c4484cfc2034a277a94072369404`, together with their complete matching reviews. Their publication diffs were read completely after those original reads. The published Fock source, SHA-256 `494c283c163e88f959841462bbfbcfcc7c470072a0525d0dd6e2b44dd6f9b12b`, supplies a checked predecessor mechanism, not an already proved averaged contraction. The nonisolated theorem remains a conditional, unaudited dependency.

Primary-source use is precise:

- [Dybalski, hep-th/0412226v4](https://arxiv.org/abs/hep-th/0412226v4): complete original 673-line TeX, SHA-256 `c425cfecc20136576180271a1e8e9c12df48ded2ae941655ad4e842363ee64a6`, read in full. Its small-width comparison and contraction/Gram strategy motivate this extension. Its continuum massless four-point estimate is not imported.
- [Bachmann–Dybalski–Naaijkens, arXiv:1412.2970v2](https://arxiv.org/abs/1412.2970v2): PDF SHA-256 `3edeb48a167b9ae6a26d6d885ccde03b068423d432176a256eb0a4ee42a14126`; complete pages 7–24 and 39–43 read from fresh extracts. Theorem 2.4, Proposition 4.3, Lemmas 4.6–4.7, the regular part of Theorem 4.9, and the transfer/localization proofs are used at proof level. Neither geometric shell isolation nor its whole-shell density theorem is assumed.
- [Nachtergaele–Sims, arXiv:0712.3318v1](https://arxiv.org/abs/0712.3318v1): PDF SHA-256 `74829f87cc51d399613043a3abdc48ba3146c81292a09e4df1035b50eb464b5c`; complete pages 3–4 and 9–12 read. Theorem 4.1 at imaginary time zero gives the clustering bound below with its support-volume dependence.

The provided science/main revision is `a13caa4885f547c8d206265b031ba7649e539fd9`, planning revision `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`, and worktree source head `dc7f415f73df3754653f4985382ca0fb96f07cda`. This worker did not run Git commands. Source bytes, rather than a moving ref, bind this derivation. The current worktree entry instructions, science workflow, primitive registry, and installed physics-loop/workhorse instructions were read; the relevant installed skill bytes match that worktree. No listed approved primitive supplies the dynamics, graph sectors or regularity used below. They remain explicit supplied conditions.

### Supplied setting and actual regular targets

Use N1–N9 with the massive dispersions N4. Explicitly, the quasilocal finite-site algebra on $\mathbb Z^d$, $d\ge1$, has geometric shifts $\tau_x$, an actual translation-invariant bounded finite-range interaction generating $\alpha_t$, and commuting implementers
\[
\alpha_t=\operatorname{Ad}e^{itH},\qquad T_x=e^{-ix\cdot Q},
\qquad H\ge0,\quad \ker H=\mathbb C\Omega,
\quad H|_{\Omega^\perp}\ge\gamma>0.                    \tag{NF1}
\]
The unit vector $\Omega$ is invariant. No relativistic locality is assumed.

Choose a specified countable family of **actual pairwise orthogonal projections** $E_s$, each reducing H and Q. For each s choose a countable collection of single-lift open momentum charts $O_{s\alpha}$, with compact closure inside a larger smooth chart, on which
\[
H E_s\mathbf1_{O_{s\alpha}}(Q)
=\Sigma_{s\alpha}(Q)E_s\mathbf1_{O_{s\alpha}}(Q),\qquad
\Sigma_{s\alpha}(p)=\sqrt{M_s^2+\beta|p+c_{s\alpha}|^2},
\quad M_s,\beta>0.                                    \tag{NF2}
\]
Here $p$ is the chosen lift and $c_{s\alpha}$ is fixed. Equation (NF2) includes its domain assertion; it is a bounded equality after restriction to any compact packet support. A sector may be one orthogonal graph piece of a larger physical mass component. The charts need not cover all of $E_s\mathcal H$. There is no mass-gap or shell-isolation assumption around these positive-energy graphs. The common positive $\beta$ is the N4 parameter, not an empirical inference.

An admissible regular packet consists of a chart as above, $\widehat f\in C_c^\infty(O_{s\alpha})$, and an almost-local B, with almost-local norm time derivatives, satisfying the **full operator** temporal-transfer condition
\[
\operatorname{Sp}_{\alpha}(B)\subset[\epsilon,L]\subset(0,\infty).
                                                               \tag{NF3}
\]
Set $D=H-\Sigma_{s\alpha}(Q)$, $v=\widehat f(Q)B\Omega$, $\psi=E_s v$, and $r=(1-E_s)v$. A smooth extension of $\Sigma$ outside the chart is used only in functional calculus. Require the actual geometric regularity
\[
\|\mathbf1_{\{|D|\le\eta\}}r\|\le c\eta^a
\quad(0<\eta\le\eta_0),\qquad a>0.                    \tag{NF4}
\]
The zero-detuning projection is included. For the local-seed construction, B is exactly a fixed smooth positive-energy/geometric filter of a local seed as in N11. The proof also covers any separately verified direct-property B of N §3. One may restrict throughout to the local-seed class: every amplitude cutoff used below keeps that same B and seed. No existence or nonzero-target statement is inserted into the definition.

Let $\mathscr R_s$ be the collection of these actual target vectors, over the chosen charts and admitted seed class, with every admissible amplitude. Define
\[
\mathcal H_{{\rm reg},s}=\overline{\operatorname{span}\mathscr R_s},
\qquad
\mathcal H_{\rm reg}=\overline{\operatorname{span}\bigcup_s\mathscr R_s}
=\bigoplus_s\mathcal H_{{\rm reg},s}\ \subset\mathcal H.       \tag{NF5}
\]
If starting from a smaller chosen packet collection, include its smooth amplitude cutoffs; §6 proves their regularity without adding seeds. This gives the same theorem for that possibly smaller space. A zero regular space is permitted and gives only the vacuum Fock sector.

The packet and average use exactly N6/N9/N10:
\[
C(t)=\sum_x f_t(x)\alpha_t\tau_x(B),\quad
f_t(x)=\int e^{ip\cdot x-it\Sigma(p)}\widehat f(p)\frac{dp}{(2\pi)^d},
\]
\[
A^{\sigma}(T)=\int g_T^{\sigma}(t)C(t)dt,\quad
g_T^{\sigma}(t)=T^{-\nu}h((t-\sigma T)/T^{\nu}),\quad
0<\nu<1,\quad\sigma\in\{+1,-1\},                    \tag{NF6}
\]
where $h\in\mathcal S(\mathbb R)$, $\widehat h\in C_c^\infty$, and $\int h=1$. Complex kernels are allowed; all norm estimates use absolute integrals. Each finite scattering family has pairwise disjoint compact sets $\nabla\Sigma_i(\operatorname{supp}\widehat f_i)$. Constants may depend on that fixed family, its positive separation, graph charts, kernels and widths.

**Theorem.** For two finite families individually satisfying this velocity separation, the N strong limits obey, for the same time sign,
\[
\left\langle\Psi^{\sigma}(\widetilde\psi_1,\ldots,\widetilde\psi_m),
                    \Psi^{\sigma}(\psi_1,\ldots,\psi_n)\right\rangle
=\delta_{mn}\sum_{\pi\in S_n}\prod_{j=1}^n
           \langle\widetilde\psi_j,\psi_{\pi(j)}\rangle.       \tag{NF7}
\]
The permanent is evaluated only for m=n; no separation between the two families is required. This holds for every fixed choice of widths $0<\nu_i<1$. There are unique isometries
\[
W^{\sigma}:\Gamma_s(\mathcal H_{\rm reg})\longrightarrow\mathcal H,
\quad W^{\sigma}\Omega_{\rm F}=\Omega,
\quad W^{\sigma}a^*(\psi_1)\cdots a^*(\psi_n)\Omega_{\rm F}
      =\Psi^{\sigma}(\psi_1,\ldots,\psi_n)                  \tag{NF8}
\]
on the admissible separated domain. Their ranges are closed. The extension defines images of general Fock vectors by continuity; it does not assert convergence of their raw nonseparated packet products.

## 2. Exactly what is reused from the nonisolated construction

N1–N31 and N §8, at the frozen identity above, establish the following under (NF1)–(NF6):

1. The strong finite-product limits exist for integrable reference widths $\nu>1/(1+a)$, and comparison transfers the **same limits** to every fixed $0<\nu<1$. Changing widths does not assert integrability of the new vacuum derivatives. For a finite family, choose any new exponents before taking $T\to\infty$; no T-dependent exponent is used.
2. $A^{\sigma}(T)^*\Omega=0$ exactly, from the positive full transfer interval, while
\[
A^{\sigma}(T)\Omega=e^{i\sigma TD}\widehat h(T^{\nu}D)v
=\psi+O(T^{-\nu a}).                                  \tag{NF9}
\]
The vector on the left does **not** in general have exact graph support at finite T.
3. Any two internally velocity-separated averaged factors have a commutator $O(T^{-P})$ for every P, also with adjoints. Independent averaging times, the LR estimate after removal of common time, and both time tails are part of that statement.
4. For $P_R=\mathbf1_{[0,R]}(H)$, $F_2=\|\widehat f\|_2$, and
\[
S_B=\sum_x\|[B^*,\tau_x(B)]\|<\infty,\quad
\Gamma_B(R)=\left\|P_R\sum_x\tau_x(BB^*)P_R\right\|
\le\lfloor R/\epsilon\rfloor S_B,
\]
one has, uniformly in T,
\[
\|A(T)^*P_R\|\le\|h\|_1F_2\sqrt{\Gamma_B(R)},\qquad
\|A(T)P_R\|\le\|h\|_1F_2\sqrt{\Gamma_B(R+L)}.             \tag{NF10}
\]
The creator uses the output ceiling R+L. N's proof uses the common kernel of all mixed lowering words, not merely powers of one lowering operator. Thus loss of exact vacuum graph support does not invalidate it. A fixed finite word of creators and adjoints, from either family, is uniformly bounded on each $P_R\mathcal H$: insert the ceiling $R+\sum L_j$ at every intermediate stage and multiply (NF10). An adjoint lowers energy. In particular every finite vacuum word and its adjoint row functional has norm $O(1)$.

Only width comparison on each original fixed graph is needed to choose small widths below. It does not presuppose a comparison between distinct charts or a Fock isometry.

## 3. Four independent times and the clustering convolution

All spatial radii and distances in this section use the maximum norm on $\mathbb Z^d$; the finite-range LR estimate in graph distance implies the needed bound in this weaker distance. Finite balls obey $V(R)\le(2\lceil R\rceil+1)^d$.

### Packet bounds and localization after removing the common time

For $k=p+c$, $E=\sqrt{M^2+\beta|k|^2}$, direct differentiation gives
\[
D^2\Sigma=\frac{\beta}{E}I-\frac{\beta^2}{E^3}kk^{\mathsf T},
\qquad\det D^2\Sigma=\frac{\beta^d M^2}{E^{d+2}}>0.          \tag{NF11}
\]
The longitudinal eigenvalue is $\beta M^2/E^3$, and the transverse ones are $\beta/E$. On a fixed compact packet support they are uniformly positive. The compact stationary-phase argument in BDN Proposition 4.3 therefore gives
\[
\|f_t\|_{\infty}\le C(1+|t|)^{-d/2},\qquad
\|f_t\|_1\le C(1+|t|)^{d/2}.                            \tag{NF12}
\]
The second bound follows by multiplying the first by the $O(|t|^d)$ sites in a fixed velocity collar and adding the arbitrary-order nonstationary-phase tail. Small t are absorbed into C. This is a lattice Fourier-series estimate on each compact chart; the continuum massless estimate plays no role.

For any finite list of packets, use §2 to choose fixed exponents satisfying
\[
0<\max_i\nu_i<\kappa<1/3.                              \tag{NF13}
\]
Set $U=T^{\kappa}$, $r_0=\lceil U\rceil$, and $R=\lceil(v_{\rm LR}+4)U\rceil$. Restrict each of four independent physical times to $|t_j-\sigma T|\le U$; write $u_j=t_j-\sigma T$. Vacuum invariance and $P_\perp=1-|\Omega\rangle\langle\Omega|$ allow the **same** outer $\alpha_{\sigma T}$ to be removed from their four-point expression. The remaining observables are $\alpha_{u_j}(B_j)$, with $|u_j|\le U$, not the fixed $B_j$ themselves.

Let $B_{r_0}=\mathbb E_{B(0,r_0)}B$ and
$B^{[R]}_u=\mathbb E_{B(0,R)}\alpha_u(B)$. Conditional expectations are contractive, so $\|B^{[R]}_u\|\le\|B\|$. The LR local-approximation consequence N14, or BDN (C.7), gives
\[
\begin{split}
\|\alpha_u(B)-B^{[R]}_u\|
&\le2\|B-B_{r_0}\|+
C\,V(r_0)\|B\|e^{-\lambda(R-r_0-v_{\rm LR}|u|)}\\
&\le C_N U^{-N}+C'(1+U)^d e^{-2\lambda U}
\le C_N' U^{-N},\qquad |u|\le U.                       \tag{NF14}
\end{split}
\]
For $U\ge1$, the padding is at least $2U$. This displays the LR input-support factor $V(r_0)$; it is absorbed by the exponential only after the sublinear time window is imposed. Almost-locality errors have arbitrary order N. The operators $B^{[R]}_u$ have support radius R and a uniform norm, despite their T-dependent definition.

### The local four-point kernel and all three relative sums

From (NF1), finite range and NS Theorem 4.1, there are fixed $C_{\rm cl},\mu>0$ such that local X,Y satisfy
\[
|\omega(XY)-\omega(X)\omega(Y)|
\le C_{\rm cl}\|X\|\|Y\|\min(|\operatorname{supp}X|,|\operatorname{supp}Y|)
e^{-\mu\operatorname{dist}(\operatorname{supp}X,\operatorname{supp}Y)}
                                                               \tag{NF15}
\]
at support distance at least one. To apply the theorem, subtract $\omega(Y)1$: the unique-vacuum projection annihilates both centered Y and its adjoint on $\Omega$, its norm is at most $2\|Y\|$, and its support stays in the same local algebra. Finite range makes the NS interaction norm finite. For example the predecessor's sufficient constants are $\mu=\lambda\gamma/(4\|\Phi\|_\lambda C_\lambda+\gamma)$ and $C_{\rm cl}=2(1+\mu^{-1/2}+2\|F\|/(\pi C_\lambda))$. No spatial support factor is suppressed in (NF15).

Let $X_j$ be any of the four localized observables $B^{[R]}_{u_j}$, including adjoints, and put
\[
K_R(x_1,x_2,x_3,x_4)=
\langle\Omega,[\tau_{x_1}X_1,\tau_{x_2}X_2]P_\perp
                       [\tau_{x_3}X_3,\tau_{x_4}X_4]\Omega\rangle.
                                                               \tag{NF16}
\]
Write $a=x_1-x_2$, $b=x_3-x_2$, $c=x_4-x_3$. A local commutator vanishes unless $|a|\le2R$, respectively $|c|\le2R$. In the remaining case the first pair support lies in $B(x_2,3R)$, the second in $B(x_3,3R)$, and their distance is at least $|b|-6R$. Each pair support has cardinality at most $2V(R)$. Moreover, directly from $\|P_\perp\|=1$, $|K_R|\le4\prod_j\|X_j\|$. Combining this norm cap with (NF15) yields a bound by a fixed constant times
\[
\mathbf1_{|a|\le2R}\mathbf1_{|c|\le2R}\,k_R(b),\qquad
k_R(b)=
\begin{cases}
1,& |b|\le7R,\\
(1+R)^d e^{-\mu(|b|-6R)},& |b|>7R.
\end{cases}                                                   \tag{NF17}
\]
The constant absorbs the four fixed operator norms, the cardinality constant and $C_{\rm cl}$, and is uniform in the four $u_j$. The near region uses the norm cap, not $R^d$ times that cap. The far region has support distance at least R, so (NF15) applies.

The middle relative sum, including its tail, obeys
\[
\begin{split}
\sum_b k_R(b)
&\le C_d(1+R)^d+
C_{d,\mu}(1+R)^d\sum_{\ell\ge0}(1+7R+\ell)^{d-1}e^{-\mu(R+\ell)}\\
&\le C_{d,\mu}'(1+R)^d.                                  \tag{NF18}
\end{split}
\]
Indeed the second line before absorption is bounded by a constant times
$(1+R)^{2d-1}e^{-\mu R}$, and $R\ge1$. There are $O((1+R)^d)$ possibilities for each of a and c. Hence
\[
\sum_{a,b,c}\sup_{x_2}|K_R(x_2+a,x_2,x_2+b,x_2+b+c)|
\le C(1+R)^{3d}.                                          \tag{NF19}
\]
There is no omitted logarithmic factor: using the crossover of the norm cap and exponential bound would give a radius $6R+O(\log(1+R))$, already bounded by a constant times R. The split at 7R proves (NF18) directly, with its exponential tail. Uncapped use of the support-volume prefactor near the origin would lose an unnecessary extra $R^d$.

Fix the three relative variables and sum the four absolute packet weights over the remaining translation $x_2$. One factor is bounded in $\ell^1$, the other three in $\ell^\infty$, regardless of the relative shifts. In the central windows $|t_j|\asymp T$, for either sign, (NF12) gives
\[
\sum_{x_1,\ldots,x_4}|f_{1,t_1}(x_1)\cdots f_{4,t_4}(x_4)|\,|K_R|
\le C T^{d/2-3d/2}(1+R)^{3d}
\le C T^{-d+3d\kappa}.                                  \tag{NF20}
\]
The observable approximation (NF14) changes the four-point kernel by at most $C_N U^{-N}$, uniformly in all centers. Summing that error uses four $\ell^1$ bounds, costing $T^{2d}$, so its contribution is
\[
C_N T^{2d-\kappa N}.                                    \tag{NF21}
\]
Thus replacing the growing-time observables by fixed ones, or claiming fixed almost-local constants without (NF14), is unnecessary and unjustified.

### Every time tail and the averaged contraction

For each packet j and every N, the global bound (NF12) gives
\[
\begin{split}
G_j(T)&:=\int |g_{j,T}^{\sigma}(t)|\|f_{j,t}\|_1dt\le C_jT^{d/2},\\
G_j^{\rm tail}(T)&:=\int_{|t-\sigma T|>T^\kappa}|g_{j,T}^{\sigma}(t)|\|f_{j,t}\|_1dt
\le C_{j,N}T^{d/2-(\kappa-\nu_j)N}.                      \tag{NF22}
\end{split}
\]
For the second estimate substitute $t=\sigma T+T^{\nu_j}z$, use $1+|t|\le2T(1+|z|)$, and use Schwartz decay on $|z|>T^{\kappa-\nu_j}$. This is an absolute polynomial moment estimate; no exponential moment of h is required.

The complement of the four central windows is a union of four tail events. Bound the original kernel there by $4\prod\|B_j\|$. Its full absolute integral is at most
\[
C\sum_{j=1}^4G_j^{\rm tail}(T)\prod_{\ell\ne j}G_\ell(T)
\le C_N T^{2d-\delta N},\qquad
\delta=\min_j(\kappa-\nu_j)>0.                           \tag{NF23}
\]
This includes configurations with any number of tail times; the union bound may overcount them harmlessly. Every central averaging integral has total variation at most $\|h_j\|_1$, so (NF20)–(NF21) incur no extra width-volume factor there.

For arbitrary packets i,j, with no mutual velocity separation, put $A=A_i^{\sigma}(T)$, $B=A_j^{\sigma}(T)$. Positive transfer gives $A^*\Omega=0$, and therefore
\[
\|P_\perp A^*B\Omega\|^2
=\langle\Omega,[B^*,A]P_\perp[A^*,B]\Omega\rangle.          \tag{NF24}
\]
Expand this as the four independent Bochner integrals belonging, in order, to $B^*,A,A^*,B$. Conjugate kernels and conjugate packet coefficients accompany the adjoints. Absolute integrability follows from the $G_j(T)$ bound before any exchange of sums or integrals. Remove common physical time, then apply (NF20)–(NF23). For every P, choose the arbitrary locality/Schwartz orders N large enough to obtain
\[
\|P_\perp A_i(T)^*A_j(T)\Omega\|^2
\le C_{ij}T^{-d+3d\kappa}+C_{ij,P}T^{-P}.                 \tag{NF25}
\]
In particular, with $\rho=d(1-3\kappa)/2>0$, (NF9) and (NF25) imply
\[
A_i(T)^*A_j(T)\Omega
=\langle\psi_i,\psi_j\rangle\Omega+e_{ij}(T),\qquad
\|e_{ij}(T)\|\le C_{ij}
\big(T^{-\rho}+T^{-\nu_i a_i}+T^{-\nu_j a_j}\big).          \tag{NF26}
\]
The scalar is initially $\langle A_i(T)\Omega,A_j(T)\Omega\rangle$; its limit follows from (NF9). No exact finite-T vacuum graph identity was inserted. The threshold $\kappa<1/3$ is a sufficient bound for this proof, not a necessity theorem or a claimed optimal exponent.

## 4. Averaged double commutators with all clocks retained

Let X(T),Y(T) be internally velocity-separated averaged packets, and let A(T) be a third admissible packet, possibly adjointed and on a different graph. Choose a smooth velocity function $\chi$ equal to one on a neighborhood of $\mathcal V_X$, with support disjoint from a neighborhood of $\mathcal V_Y$. Split the third amplitude into
\[
\widehat f_{A,0}(p)=\chi(\nabla\Sigma_A(p))\widehat f_A(p),\qquad
\widehat f_{A,1}=(1-\chi\circ\nabla\Sigma_A)\widehat f_A.     \tag{NF27}
\]
Then $A=A_0+A_1$, the 0-piece is separated from Y, and the 1-piece is separated from X. Compactness and the chosen collars ensure positive separation for both. The same split of conjugate amplitudes applies to adjoints.

Each of the three clocks remains independent. Before estimating, the expression is the norm-convergent triple integral
\[
[[A(T),X(T)],Y(T)]
=\iiint g_A(t)g_X(u)g_Y(v)
          [[C_A(t),C_X(u)],C_Y(v)]\,dt\,du\,dv,            \tag{NF28}
\]
with conjugation of g where required. The N two-time commutator proof applies to $[A_1,X]$, $[A_0,Y]$, and $[X,Y]$ separately. For completeness, restrict their independent times to a window $T^\mu$ with $\max\nu<\mu<1$; linear spatial velocity separation dominates the LR growth from a relative time at most $2T^\mu$. Spatial tails are arbitrarily small by nonstationary phase. Each time tail, weighted by the global packet norm, is $O(T^{d/2-(\mu-\nu)N})$ by the calculation in (NF22); a triple tail costs at most $O(T^{3d/2-\delta_\mu N})$. Hence integrating the third polynomially bounded factor preserves arbitrary decay.

Equivalently, after the absolute integrations one can use the exact identity
\[
[[A_0,X],Y]=[A_0,[X,Y]]-[X,[A_0,Y]].                      \tag{NF29}
\]
Both terms contain one of those fully averaged rapid commutators. The other factor has norm $O(T^{d/2})$, by (NF12)/(NF22). The A1 term has a rapid inner commutator. Consequently
\[
\|[[A(T),X(T)],Y(T)]\|=O(T^{-P})\quad\hbox{for every P},    \tag{NF30}
\]
also with any adjoints. No equality between t,u,v was used. This proof works for all fixed powers below one; only the vacuum contraction of §3 requires the auxiliary small widths.

## 5. Gram recursion, finite-energy rows, and particle number

Work first with small widths (NF13), using the same $\sigma$ in both families. Suppress T in products. Write $a=\widetilde A_1^*$. Commuting a through the right product, and then moving each bracket to the far right, gives the **exact** identity on $\Omega$
\[
\begin{split}
a A_1\cdots A_n\Omega
={}&\sum_{k=1}^n\Big(\prod_{j\ne k}^{\longrightarrow}A_j\Big)[a,A_k]\Omega\\
&+\sum_{k<\ell}
 \Big(\prod_{j<\ell,\,j\ne k}^{\longrightarrow}A_j\Big)
 [[a,A_k],A_\ell]
 \Big(\prod_{j>\ell}^{\longrightarrow}A_j\Big)\Omega .       \tag{NF31}
\end{split}
\]
The arrow preserves original order. The omitted terminal term is $A_1\cdots A_na\Omega=0$, exactly. Each double bracket has n−2 right-family spectators. Multiplication on the left by the remaining m−1 tilde annihilators gives m+n−3 spectators in the corresponding scalar product. Whenever a double-bracket term occurs, their unrestricted norms grow at most as $T^{d(m+n-3)/2}$. Choosing P in (NF30) larger than this exponent plus any desired margin makes every such term vanish. There are only finitely many terms.

In the first line $[a,A_k]\Omega=aA_k\Omega$. Use (NF26) for every k. The accompanying row functional is
\[
\ell_{k,T}(\xi)=
\left\langle\widetilde A_2\cdots\widetilde A_m\Omega,
           \Big(\prod_{j\ne k}^{\longrightarrow}A_j\Big)\xi\right\rangle.
                                                               \tag{NF32}
\]
Its representing vector is
\[
\Big(\prod_{j\ne k}^{\longrightarrow}A_j\Big)^*
 \widetilde A_2\cdots\widetilde A_m\Omega.
\]
This is a word of **all m+n−2 remaining factors**, consisting of creators and adjoints. By (NF10), insert $P_{R_*}$ at every intermediate stage, with $R_*=\sum_jL_j+\sum_i\widetilde L_i$. Its norm is bounded uniformly in T. Thus $\|\ell_{k,T}\|\le C_k$ as a functional on the entire Hilbert space; no unproved spectral restriction on $e_{1k}(T)$ is needed. In particular
$|\ell_{k,T}(e_{1k}(T))|\le C_k\|e_{1k}(T)\|\to0$.

Writing $I_{m,n}(T)$ for the original inner product gives
\[
I_{m,n}(T)=\sum_{k=1}^n
\langle\widetilde\psi_1,\psi_k\rangle I_{m-1,n-1}^{(k)}(T)+o(1),
                                                               \tag{NF33}
\]
where the indicated labels are deleted. For $m=0<n$, the inner product is exactly zero because $A_1^*\Omega=0$; for $n=0<m$ use the same argument and conjugation. The empty–empty value is one. Iteration of (NF33) proves the permanent if m=n and zero if m≠n, for both signs of time. There is no extra factorial with the creation-operator normalization in (NF8).

Finally restore any original fixed widths $0<\nu_i<1$ and kernels. The N §8 comparison says each **strong product limit** equals its small-width representative on the same original charts and targets. Their inner products therefore equal the values just computed. This transfers (NF7), not a uniform-in-width version of the estimate (NF25). It neither assumes raw unaveraged convergence nor extends the contraction estimate to widths near one.

## 6. Cutoff stability, absolute continuity, and chart compatibility

### Cutoffs and the actual closed regular space

If $\psi=E_s\widehat f(Q)B\Omega$ is regular and q is a smooth torus function, the actual packet with amplitude $q\widehat f$ uses the same B, graph and seed. Its residual is $q(Q)r$, so
\[
\|\mathbf1_{|D|\le\eta}q(Q)r\|
\le\|q\|_\infty c\eta^a.                                \tag{NF34}
\]
Its support stays inside the original packet support, and its target is $q(Q)\psi$. Thus all smooth cutoffs preserve the regular target class. By taking closed spans, $\mathcal H_{{\rm reg},s}$ is invariant under q(Q) and its adjoint. Smooth functions are uniformly dense in continuous torus functions; bounded pointwise approximation, or the spectral theorem, then shows this subspace reduces all Q-spectral projections. Since the $E_s$ are orthogonal, the decomposition in (NF5) is in the actual Hilbert space and is not a direct sum of duplicated chart labels.

For an open set U, choose $q_n\in C_c^\infty(U)$, $0\le q_n\le1$, tending pointwise to $\mathbf1_U$. Applied after approximating a vector by finite regular-target sums, these cutoffs prove local density in $\mathbf1_U(Q)\mathcal H_{{\rm reg},s}$. This is density **by definition and cutoff stability in the regular space**, not an appeal to cyclicity for arbitrary seeds.

### Geometric spectral absolute continuity

Positive transfer gives $B^*\Omega=0$. For its unprojected vacuum vector,
\[
\langle B\Omega,T_xB\Omega\rangle
=\langle\Omega,[B^*,\tau_x(B)]\Omega\rangle.               \tag{NF35}
\]
Almost locality makes these coefficients decay to every power. Fourier uniqueness therefore identifies the Q-spectral measure of $B\Omega$ with a smooth density relative to normalized Haar measure. For any Haar-null Z, using the commuting projection $E_s$,
\[
\|\mathbf1_Z(Q)E_s\widehat f(Q)B\Omega\|
\le\|\widehat f\|_\infty\|\mathbf1_Z(Q)B\Omega\|=0.        \tag{NF36}
\]
Finite spans and norm closure yield $\mathbf1_Z(Q)|_{\mathcal H_{\rm reg}}=0$. This proves absolute continuity on the full defined regular space, including arbitrary multiplicity. The selected density need not remain smooth, and $E_s B$ need not be an almost-local observable. Neither assertion is used.

### Charts and species

On overlaps use a common torus lift. Coordinate transitions have the form $p'=p+2\pi\ell$; replacing $c$ by $c-2\pi\ell$ preserves k=p+c. It also preserves the packet itself, since $e^{2\pi i\ell\cdot x}=1$ for lattice x.

Even if two listed charts for the same sector initially use different massive graph expressions, (NF2) implies that the Q measure of their common-sector overlap is supported on $\Sigma_a=\Sigma_b$. In common coordinates,
\[
\Sigma_a(p)^2-\Sigma_b(p)^2
=M_a^2-M_b^2+\beta\big(2p\cdot(c_a-c_b)+|c_a|^2-|c_b|^2\big).
                                                               \tag{NF37}
\]
Here $M_a=M_b=M_s$ within the specified sector; the displayed general form also checks comparison of massive expressions. This polynomial is either identically zero, in which case the positive square roots and their gradients agree, or its zero set is empty or a hyperplane and hence Haar-null locally. By (NF36), the latter overlaps carry no regular vectors. Applying this on the countably many coordinate-overlap components gives a well-defined velocity spectral operator on $\mathcal H_{{\rm reg},s}$, equal to $\nabla\Sigma_{s\alpha}(Q)$ on each chart, up to zero projections. There is no extra multiplicity from overlaps.

Distinct s label actual orthogonal subspaces, so their one-particle inner products vanish. Distinct species may nevertheless have equal velocities; species orthogonality is not used as velocity separation. Different admissible creator or chart realizations of the same target will have the same image under (NF8), by the Gram argument in §8. No physical identification of s with an exhaustive list of particles is asserted.

## 7. Density of separated tensors in the defined Fock space

For each massive chart the velocity map is
\[
v_M(k)=\frac{\beta k}{\sqrt{M^2+\beta|k|^2}},\qquad
k_M(v)=\frac{Mv}{\sqrt\beta\sqrt{\beta-|v|^2}},
\quad |v|<\sqrt\beta.                                    \tag{NF38}
\]
It is injective and has the nonzero Jacobian (NF11). In any pair of charts, including different sectors or masses, the set $v_i(p)=v_j(q)$ has at most one p for each fixed q, after the fixed shift by c. Fubini makes that equal-velocity subset Lebesgue-null in the chart product. Finite unions over particle pairs and countable unions over sector/chart choices remain null. The scalar product spectral measures of elementary tensors are absolutely continuous by (NF36), and elementary tensors are dense. Thus every coincident-velocity diagonal has zero product spectral projection on $\mathcal H_{\rm reg}^{\otimes n}$.

The complement of those diagonals is covered by countably many products of relatively compact momentum neighborhoods, each contained in one of the actual charts, whose velocity images have pairwise disjoint closures. Such boxes exist at every distinct-velocity tuple by continuity. Their product spectral ranges span a dense subspace: a vector orthogonal to all those ranges is annihilated by the projection of their full-measure union.

In each factor box, actual regular targets with packet support inside the assigned neighborhood and its velocity collar are dense. Here is the chart detail needed for that assertion. Approximate a vector by regular targets from arbitrary original charts, then apply the smooth cutoffs of §6 supported in the box neighborhood. Each resulting amplitude has compact support in the intersection of its original chart with the box chart. Use a finite smooth partition on that compact support subordinate to overlap components and common coordinate lifts. On a component where the two massive graphs agree, their velocities agree pointwise and the packet now has the required velocity support. On a component where they disagree, (NF37)/(NF36) makes that target exactly zero; discard it. Every surviving cutoff is still an actual regular packet by (NF34). This proves the local density required for the box without assuming that all original creators were built in its chart.

Algebraic tensor products of these local dense classes are dense in each box range. Their factors have genuinely disjoint **packet** velocity supports, not merely different target spectral labels. Symmetrization is continuous, so the span of admissible separated bosonic products is dense in every $\Gamma_s^{(n)}(\mathcal H_{\rm reg})$. Finite particle sectors are dense in the full Fock space. No density of the interacting scattering range has been inferred.

## 8. Isometry and exact stopping point

The creation-operator vectors in bosonic Fock space have Gram matrix (NF7). Assign each admissible separated vector its strong scattering limit. For any finite linear combination, (NF7), including cross terms with different charts and different particle numbers, preserves the squared norm. A zero Fock vector therefore has zero image. This proves well-definedness for all seed, cutoff, chart, partition and species presentations of the same actual Fock vector. It is stronger than a fixed-chart creator comparison and does not assume one.

The dense domain in §7 consequently extends uniquely to an isometry in each particle sector. Different sectors have orthogonal images by §5, so their Hilbert direct sum gives (NF8). An isometry from a complete Hilbert space has closed range. If admissible separated targets are all nonzero, their within-family orthogonality follows from their disjoint velocity spectral supports, and their scattering norm squared is $\prod_i\|\psi_i\|^2>0$. This nontriviality is conditional on having those actual nonzero regular targets.

The result does not enlarge $\mathcal H_{\rm reg}$ to an entire physical mass space, construct regular seeds, derive graph stability, compare incoming with outgoing ranges, or prove an isometric/unitary S-matrix. No detector convergence, ND, EX, onto, boost covariance, massless vacuum or microscopic realization is asserted. In particular the gapped-vacuum clustering step cannot be transplanted to a massless vacuum without a new estimate. The geometric regularity variable and the predecessor's beta=1 counterexample remain intact.

## 9. Author evidence and recovery

The complete proof above is the mathematical evidence. `nonisolated_fock/check_fock_extension.py` completed under a declared 60-second timeout, exiting 0 in 0.28 seconds (rounded), with seven complete JSON output records and empty stderr. Its full source, stdout, execution metadata and hashes are preserved. All output was read; no truncated record was accepted as verification.

| Author control | Result and actual limit |
|---|---|
| Exact free noncommutative words, n=1–9 | The full identity underlying (NF31), including its terminal annihilator and every ordered spectator, holds. Omitting all double brackets or an individual double bracket is rejected when such terms exist. This checks algebra, not asymptotic decay. |
| Support geometry and lattice majorant | 14,155 one-dimensional support configurations verify the 6R support-distance subtraction and reject an incorrect 2R subtraction. A separate exact rational shell-sum calculation includes the infinite exponential tail in d=1–4, R=1,2,4,8,16,32. An independently organized finite sum plus exact residual reproduces all 24 totals. The all-dimension/all-R power estimate is still the analytic argument (NF18)–(NF19). |
| Four independent clocks | A two-site positive-transfer matrix model with discrete complex clock weights gives projected norm squared 0.0006108867017679198; its 144-term four-time covariance sum agrees within 2e-18. Pairwise clock tying and a common-clock replacement each change this test by about 0.121889; omitting the connected projection changes it by about 0.050825. The triple integral and Jacobi identity agree within 2e-16, while the wrong Jacobi sign fails by about 0.741376. This is a finite algebraic control, not a nonisolated infinite-lattice model or an approximation of the Schwartz time integrals. |
| Finite-energy bounds | The same nonexact-vacuum creators satisfy the padded creator and annihilator bounds at four energy ceilings. Omitting R+L predicts zero on the vacuum, whereas the tested creator norm there is about 0.674978. This controls the distinction used in (NF10), whose general proof is the reviewed mixed-word argument. |
| Width and tail accounting | Exact rational calculations in d=1–6 with five regularity exponents verify the reference Cook widths, small fixed widths and every displayed four-time/localization error order. Most small-width derivative estimates in the table are nonintegrable, as expected; the proof uses strong-limit comparison. The arithmetic does not prove that the exponent threshold is necessary. |

The controls were written without inspecting predecessor control sources or outputs. The previous proofs, their review descriptions, and the root lead were visible; this is author checking, not an independent review. `PRECONTROL_PROOF.md` and `precontrol_freeze.json` preserve the pre-execution derivation. A subsequent complete cold read corrected inline-math escaping and one section reference, and added this execution account; the earlier bytes remain preserved. No failed computational run is hidden. The operational executable/output-display failures are recorded in `OPERATIONS.md`.

`READING_COVERAGE.json` binds the complete argument and primary-source reads. `receipt.json` binds the final note, all evidence files and a fresh source-identity check. At the author freeze, `CHECKPOINT.md` was its recovery checkpoint; current campaign recovery and its science-checkout pointer remain root-owned. At the author freeze, the exact next scientific action was a fresh independent review of (NF14)–(NF38) and their stated N dependencies before extensive downstream reuse; the completed review is recorded below. No Lean formalization or independent review of this extension was performed by this author.

Frozen author operational record: only this probe and `nonisolated_fock/` are author outputs. No existing frozen source, repository science file, Git reference/index, PR, audit, main branch, axiom, primitive, other chat, or editable prompt has been changed. Editable prompt files changed: none. The inherited user-selected model and reasoning effort were preserved, with no subdelegation. Fixed campaign deadline: 2026-10-12 16:00:52 UTC.


## Publication evidence and review record

The complete frozen author source is `NONISOLATED_FOCK_PROBE.md`, SHA-256
`90471bd9b63f6a39356152a725e633a1d465272188ff1574bd198f71e97b85f5`. Its separate review is `NONISOLATED_FOCK_REVIEW.md`, SHA-256
`be5ad6f72a82e08f3cd1d841aea1bf3478ea3c92dfd309de0d2ba070818ed919`, with receipt SHA-256 `4db257dacc70363b8db4fee15613e868dc03ada4a7702becd85ce931c7034068`.
The [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserves the complete own
author/reviewer sources, earlier versions, failures, stdout/stderr, execution
receipts, root source-coverage records and their byte identities. The
[exact transformation map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/PUBLICATION_EDITS.json) and
[reconstruction program](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/reconstruct.py) recover every byte of
this complete note and its entire primary. No mathematical correction is made.
Historical review-pending and worker-scope statements above describe the author
freeze; this separate appendix records the completed source review.

**Author/checker pairing:** Same selected model family in separate author/reviewer contexts; the selected model and reasoning effort were preserved. Candidate formulas and reported outcomes were visible before distinct controls, so this was neither blinded nor cross-family checking. Root proposed mechanisms and is a coauthor, not the independent reviewer. The mechanical preparer performed no new scientific review.

The complete NF1-NF38 source review requires no mathematical correction.
It checks the four independent averaging clocks, the capped clustering kernel
with three relative lattice sums, the squared contraction bound, every
finite-energy spectator, the full Gram recursion and the defined regular
one-particle space. The small-width sufficient bound is not asserted necessary.
Width comparison then transfers the result to every fixed sublinear power.
Compatible overlapping charts do not add species. The regular target space
may be zero; its separated-tensor density does not assert density in an entire
physical mass sector or density of the interacting scattering range.

The original author driver emits seven complete JSON records. Publication's
TOTAL counts one completed assertion-guarded driver, not seven predicates.
Thirteen full-source mutations preserve the original gates: nine are rejected,
while removal of the volume-growth factor, one relative count, the contraction
exponent and the tail margin survive. All changed numeric output and passing
rows remain. No calculation or gate is silently repaired to hide this limit.
The proof carries the general exponents; the finite arithmetic does not prove
them. The original independent matrix control timed out after two partial
records at 60 seconds. A rational-pair optimization retained its matrices,
cases and gates and completed six records. Both implementations, timeout,
partial output and completed run are preserved with their actual receipts.

The Nonisolated mass note supplies N1-N31 existence/comparison and energy
bounds. The prior compact-patch Fock mechanism is a second direct dependency,
reconstructed at the actual averaged, nonexact-vacuum hypotheses. Original SC
is context and transitive through N. N36's weighted-Casimir repair is preserved
as predecessor provenance; this proof imposes geometric regularity directly
and does not use N36. The exact Dybalski, BDN and NS paper versions and read
page scopes are recorded externally. No regular-seed existence, whole-sector
density, onto/exhaustion, detector, ND/EX, S-matrix, boost or microscopic model
is inferred. The positive-gap clustering premise is not a massless-vacuum result.

The [canonical finite primary](../scripts/nonisolated_fock_2026_10_12.py) retains every
original calculation and failure gate. Publication adds only mapped input and
timeout declarations, an assertion guard and finite-scope output. Original
adjacent-result writes are suppressed where present; the complete original
JSON outputs remain in the evidence map. Required output destinations in the
Boost and Integrated CLIs become optional for ordinary canonical execution.
Where present, self-hash calculations remain and refer to the source actually run.

Preparation ran no primary, mutant, independent control, runner-cache API,
vocabulary fixer, graph builder or audit compatibility check. Actual canonical
execution and complete original mutation replay are root's subsequent work,
recorded in [delivery checks](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/DELIVERY_CHECKS.md). Historical
source-bound results are not fresh canonical results. No retained promotion,
applied audit verdict, Lean certificate, helper-registry change or completed
publication is asserted here. Combined candidate validation and strict audit
lint remain separate landing gates.

This is a frozen milestone record. Root owns the sole live campaign checkpoint
and its current science-checkout pointer. Editable prompt files changed: none.
