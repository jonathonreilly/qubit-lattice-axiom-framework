# GB1E. The Euclidean lift of the lattice gauge bridge

## 0. Status

**Pass 3 done (GB1E_REFEREE.md); edits applied; ready to freeze**

All constructions below are on finite periodic boxes. They concern the proposed SU(2) test-law family of `GB1QL.md`, not a selected physical law. They do not establish the infinite-lattice Y1 target or a T0 hand-off.

**Proved, conditional on the displayed definitions.** For positive electric coefficient, the target Hamiltonian has a trace-class heat semigroup. The local heat-kernel lift is a gauge-invariant Haar-density probability measure with the stated transfer matrix. The exact semigroup has a finite-box lift, obtained as a total-variation limit of coarse local lifts. Both have coordinate link-reflection positivity. Their relation to the tick, the Wilson measure, the finite registers and their large-register limit is given below.

**GAP 1: principal generator.** Draft Proposition 3.2(a) mistakes absence of the eigenvalue −1 for absence of −1 from the spectrum. For irrational \(\tau_E/\pi\), the electric phases are dense on the circle. Thus −1 is in the spectrum and the owner's strict \(\|X_g\|<\pi\) generator does not exist for the infinite-register electric gate. The bounded Borel wrapped generator exists with norm \(\pi\), but is not the owner's strict R-GEN. The draft's inference about R-GEN widened to the target therefore fails at existence of its generator. Section 5 gives the corrected finite-register and wrapped statements.

**GAP 2: scope of the hand-off.** The constructed measures are finite-torus measures. T0-start[G] quantifies over every torus side (`GA2_Y2_DRAFT.md` line 211). On a hypercubic torus of even side \(N = N_t \ge 4\), both lifts are measures of the kind it takes. The infinite-volume clause concerns Y1 on \(\mathbb Z^3 \times \mathbb Z\) and the \(\mathbb Z^4\) wording of `GB1QL.md` line 335. A consistent infinite-volume measure, the full T0 reflection interface and membership in its unpinned class are not established. The draft's unconditional language that (H-4D), (H-RP), or Y1 is delivered on \(\mathbb Z^4\), and that (H-class) is the first failure, exceeds its proof. The fixed-register negativity result concerns the specified group-variable kernel and small Euclidean step; it does not exclude other representations.

**Open by name.** GB1E-ς; (H-class) as a decision; the reflection interface of the consumer; Y1 on `Z³ × Z`; T0-start for anisotropic, cube-face starts; Y3 and isotropy restoration; E-2; VC1; T0-rate; a volume-uniform form of Theorem 8.3; owner question: which generator reading GB1 uses.

**Provenance.** Editing session: Codex gpt-6.1-terra, effort high, codex-cli 0.165.0, session id `01a1b826-5073-7991-ae9f-c88c81eda6f8`. Pass 1: `GB1E_DRAFT.md`, Claude Opus 5.5, max, as recorded there. Pass 2: Codex, `gpt-6.1-terra`, effort and session id: see run log. Draft SHA-256 `aa1d0f932fdc3a6c568c4f2e8bd0ba3500a3223d1f20d3ed2d16be81420c4663`; digest `prior/GB1E.md` SHA-256 `f8bb1c9676f49e4252b9f43547ac80936f96839cb7cce6821383c092b754b745`. Source and proof checks here are not independent referee or audit results. Draft numerical checks are reported as such, not rerun.

## 1. Definitions inferred by the distiller

Fix \(N\ge4\) even, \(\Lambda=(\mathbb Z/N\mathbb Z)^3\), positively oriented spatial bonds \(\mathcal L\), and even \(N_t\ge2\). For reflections involving a two-slice direction, the usual two disjoint crossing planes must be interpreted with the torus's distinct oriented bonds. Put \(\Gamma=\Lambda\times\mathbb Z_{N_t}\), \(\mathcal K=L^2(SU(2),dU)\), \(\mathcal H=\mathcal K^{\otimes\mathcal L}\), with normalized Haar measure. Write \(H_k\) for the degree-\(k\) spherical harmonics on \(S^3\), \(\dim H_k=(k+1)^2\), and \(E^2=k(k+2)/4\) on \(H_k\). Set \(A=\sum_\ell E_\ell^2\) and
\[
 \Theta(u)=\sum_{k\ge0}(k+1)^2e^{-u k(k+2)/4}.
\]
These are the definitions and harmonic decomposition of `GB1QL.md` §1 and Lemma 4.1. Let \(R(h)f(U)=f(h\cdot U)\), \((h\cdot U)_{xy}=h_y^{-1}U_{xy}h_x\), and \(P_0=\int R(h)dh\).

The tiling cubes have bases with all three coordinates equal modulo two. Their faces form \(CF\): a spatial \((i,j)\)-plaquette belongs to \(CF\) exactly when its two in-plane base coordinates have equal parity. With \(X_p\) the ordered plaquette holonomy, put \(B_p=2\operatorname{Tr}X_p\), \(H_B=\sum_{p\in CF}B_p\), \(V_\theta=\theta H_B\), and \(H=\tau_E A+V_\theta\). The trace is the unnormalized two-dimensional trace. The cube-face convention and tick are from `GB1.md` and `GB1QL.md`; \(V_\theta\) is bounded and real.

A **transfer-kernel lift** of a bounded operator \(T\) with nonnegative measurable kernel \(\kappa\) is the normalized product of \(\kappa(U_t,V_t\cdot U_{t+1})\) against Haar measure on all spatial links \(U_t\) and temporal links \(V_{x,t}\), provided its integral is finite and positive. This is a specified representation, not an assertion that every transfer admits one. A kernel is nonnegative only if it is real almost everywhere.

Write \(\Pi_k\) for projection onto \(H_k\), \(Z_k(x,y)\) for its kernel, \(z_k(g)=Z_k(g,e)\), and \(k_t=\sum_k e^{-tk(k+2)/4}z_k\). Define \(\mathcal P\) as the continuous class functions \(\sum_q a_q\chi_{R_q}\), with \(a_q\ge0\), finite-dimensional unitary \(R_q\), and \(\sum_q a_q(\dim R_q)^m<\infty\) for every positive integer \(m\).

The **local lift** \(\mu_{\rm loc}[\beta,t]\), \(t>0\), has unnormalized density
\[
 \prod_{r,p\in CF}e^{\beta\operatorname{Tr}X_p(U_r)}\prod_{r,\ell}k_t(W_{\ell,r}),\qquad
 W_{xy,r}=V_{x,r}^{-1}U_{xy,r+1}^{-1}V_{y,r}U_{xy,r}.
\]
Call its local weight class \(\mathcal A_{HK}\). The **exact lift** \(\mu_{\rm ex}\) is the transfer-kernel lift of \(e^{-a_0H}\), when constructed below. The class \(\mathcal A_{FK}\) consists of these exact lifts, equivalently their specified coarse-grained local limits. Neither class is identified with T0's \(\mathcal A_{k_0}(g)\).

A coordinate **link reflection** is reflection in a plane halfway between sites, together with the second such plane on the even torus. Its positive algebra consists of bounded functions of bonds wholly in one open half. A reflection acts on bond variables by \((\vartheta\cdot U)_b = U_{\vartheta b}\), inverted when \(\vartheta\) reverses the orientation of \(b\), as in (P8.1). Reflection positivity means \(\langle\overline{F\circ\vartheta}F\rangle\ge0\), with reflection invariance separately required.

## 2. Hamiltonian and heat kernel

**Theorem 2.1.** If \(\tau_E>0\), \(H\) is self-adjoint on \(D(A)\), gauge invariant, bounded below, and has compact resolvent. Its ordered eigenvalues satisfy \(\mu_i\ge\tau_E\alpha_i-\|V_\theta\|\), where \(\alpha_i\) are those of \(A\). Hence
\[
 \operatorname{Tr}e^{-uH}\le e^{u\|V_\theta\|}\Theta(u\tau_E)^{|\mathcal L|}<\infty\quad(u>0).
\]
For \(\tau_E<0\), \(e^{-uH}\) is unbounded. For \(\tau_E=0\), \(\operatorname{Tr}(P_0e^{-uH})=\infty\).

*Proof.* Bounded perturbation gives self-adjointness and gauge invariance; a resolvent factorization gives compactness. Min–max gives the eigenvalue bound and the trace estimate. For negative \(\tau_E\), one-link high-flux vectors make the energy tend to minus infinity. For zero \(\tau_E\), the semigroup is bounded below by a positive multiple of the identity, and \(P_0\) has infinite rank: powers of one plaquette trace are independent gauge-invariant functions. □

**Theorem 2.2.** For \(t>0\), \(k_t\) is a continuous nonnegative real class function, integrates to one, is positive near the identity, and is the convolution kernel of \(e^{-tE^2}\). Moreover \(1,k_t\in\mathcal P\), and \(e^{\beta\operatorname{Tr}g}\in\mathcal P\) for \(\beta\ge0\).

*Proof.* Invariance of \(H_k\) under left and right translations makes \(Z_k(x,y)=z_k(xy^{-1})\), with \(z_k(e)=(k+1)^2\), \(|z_k|\le(k+1)^2\), and \(z_k\) the character of left translation on \(H_k\). The series converges uniformly and gives the spectral kernel and unit integral. On polynomial data, the heat equation \(\partial_tu=\frac14\sum_{\mu<\nu}D_{\mu\nu}^2u\) preserves nonnegativity by the first-minimum argument applied to \(u+\epsilon(1+t)\). Approximate a nonnegative continuous function by squares of polynomials; continuity of the kernel then forces \(k_t\ge0\). Its value at the identity is positive. The heat-kernel character coefficients are positive and rapidly summable. For the Wilson weight, expand the exponential in tensor powers of the defining character; the factorial controls every dimension moment. □

The same positive-character mechanism for finite Wilson slabs is already proved in `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`, as identified by `prior/GB1E.md`; that source is recorded there as unaudited. The heat-kernel extension above is the draft's argument.

## 3. Local and exact lifts

**Theorem 3.1.** For every real \(\beta\) and \(t>0\), \(\mu_{\rm loc}\) exists, has bounded continuous Haar density, is gauge invariant, and has positive injective transfer
\[
 T_{\rm loc}=M e^{-tA}M,\qquad M=e^{(\beta/4)H_B}.
\]
For bounded slice functions \(F_j\),
\[
 Z=\operatorname{Tr}(P_0T_{\rm loc}^{N_t}),\qquad
 \mathbb E\prod_jF_j=Z^{-1}\operatorname{Tr}\prod_j(F_jT_{\rm loc}P_0).
\]

*Proof.* The kernel is \(M(U)\prod_\ell k_t(U_\ell U_\ell'^{-1})M(U')\), bounded, continuous and nonnegative. It is injective and positive as an operator. The two \(M\) factors per slice give exactly the spatial weight; conjugacy of each temporal holonomy gives the heat factors. Gauge averaging each temporal link yields the kernel of \(TP_0\). The cyclic integral is the displayed trace because bounded kernels are Hilbert–Schmidt and \(N_t\ge2\). Positivity and injectivity on the nonzero invariant subspace give \(Z>0\). Haar invariance and conjugation invariance of plaquette weights give gauge invariance. □

**Theorem 3.2.** Let \(\tau_E>0\), \(s=a_0/n\), \(S_s=e^{-sV_\theta/2}e^{-s\tau_EA}e^{-sV_\theta/2}\). For fixed box and \(a_0>0\),
\[
 \|S_{a_0/n}^n-e^{-a_0H}\|_1\le C(1+\log n)/n
\]
for sufficiently large \(n\). The exact lift exists and has a bounded nonnegative Haar density, is gauge invariant, and has partition function \(\operatorname{Tr}(P_0e^{-N_ta_0H})>0\). For odd \(n\), retain every \(n\)-th spatial slice of the local lift with \((\beta,t)=(-2a_0\theta/n,a_0\tau_E/n)\), and multiply its intervening temporal links in order. The resulting measures converge to \(\mu_{\rm ex}\) in total variation.

*Proof.* Put \(W=V_\theta\), \(Q_s=e^{-s\tau_EA}e^{-sW}\), \(E_s=e^{-sH}\). The product rule for \(A=-\frac14\sum D_i^2\) gives \(\|[A,f]z\|\le C_f(\|z\|+\|Az\|)\) for smooth \(f\). Duhamel and this bound give \(\|(Q_s-E_s)z\|+\|(Q_s^*-E_s)z\|\le Cs^2(\|z\|+\|Az\|)\). Each product of \(m\) factors \(Q_s,Q_s^*\), or \(S_s\), has kernel between zero and \(e^{ms\|W\|}\) times the heat kernel at time \(ms\tau_E\); splitting the product in two gives a uniform trace-norm bound when each half has duration bounded below. The telescoping sum \(Q_s^n-E_s^n=\sum_j E_s^j(Q_s-E_s)Q_s^{n-1-j}\), the smoothing estimate \(\|Ae^{-uH}\|\le C(1+u^{-1})\), and a separate \(j=0\) estimate give \(C(ns^2+s\sum_{j<n/2}j^{-1}+s)\). The end multipliers give \(\|S_s^n-Q_s^n\|_1\le Cs\). This proves the rate.

The kernel bound passes to the \(L^2\) limit of the kernels and gives a bounded nonnegative kernel for \(e^{-a_0H}\). Gauge covariance passes from \(H\); the trace argument of Theorem 3.1 gives the probability measure and its partition function. In each coarse interval, Haar-preserving changes of intermediate spatial variables gauge away the individual temporal links. Integrating the intermediate slices gives the kernel of \(S_s^n\), while their ordered temporal product is Haar distributed. Uniform kernel bounds and \(L^2\) kernel convergence give \(L^1\) convergence of the cyclic products and their normalizations. □

The compact interacting Hamiltonian limit for a supplied anisotropic SU(3) cube is already proved, with strong convergence and its stated cutoff estimate, in `docs/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md` (digest: unaudited). It does not by itself prove this SU(2), full-box trace-norm or measure statement. Full-boundary gluing is already treated in `docs/GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md`; compressed powers need the extra contract identified in `docs/GAUGE_WILSON_CUBE_SLAB_SIMULTANEOUS_ANISOTROPIC_SOURCE_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-09-07.md`.

## 4. Tick and proposed readings

**Theorem 4.1.** Define \(\Phi(z_B,z_E)=e^{-z_BH_B/2}e^{-z_EA}e^{-z_BH_B/2}\), for \(\Re z_E\ge0\). The tick \(U_{KS}=e^{-i\theta H_B}e^{-i\tau_EA}\) is unitarily equivalent to \(\Phi(i\theta,i\tau_E)\). For \(\lambda>0\), \(\tau_E>0\), \(\Phi(\lambda\theta,\lambda\tau_E)\) is \(T_{\rm loc}\) at \((\beta,t)=(-2\lambda\theta,\lambda\tau_E)\). Its \(n\)-th power at \(\lambda=a_0/n\) tends in trace norm to \(e^{-a_0H}\).

*Proof.* Move the half magnetic factor across the symmetric product. Substitute the parameters into Theorem 3.1, and apply Theorem 3.2. □

The tick alone fixes neither its logarithm nor this continuation: `GB1.md` Theorem 2.1 already proves the logarithm ambiguity, and its Theorem 2.3 proves the finite \(\mathbb Z_2\) transfer identity. The positive local transfer defines \(-\lambda^{-1}\log T_{\rm loc}\); equality to \(H\) at finite \(\lambda\) is not claimed. The constants and angles are supplied data, not derived from the unitary alone. \(W_E\) fixes \(\tau_E\) only modulo \(8\pi\), since \(4E^2\) has spectrum \(\{k(k+2)\}\). Each representative \(\tau_E + 8\pi n > 0\) gives its own ray; the step \(\lambda\) is the one free constant on each ray.

The following four tests are the draft's: (1) fixes a target, (2) is open-ended, (3) settles downstream physics by premise, (4) adds unneeded structure. P passes, C is conditional, F fails. These are author-side checks, not owner decisions.

| Reading | Text and check results |
|---|---|
| **R-SUM, proposed** | Sum the written layer exponents, giving \(H=\tau_EA+\theta H_B\) and its finite-register analogue. Tests P P C C. It selects Euclidean correlations and uses angle representatives and the sign \(\tau_E>0\), neither fixed by the tick. It does not select the state or isotropy. It is not generally a logarithm of the product tick. |
| **R-IA, proposed** | At a supplied \(\lambda>0\), continue the symmetric layers by multiplying their angles by \(-i\lambda\). Tests P C C C. It supplies the Euclidean continuation and an extra step; \(\tau_E>0\) is required here. |
| **Bounded R-GEN, recorded for SMG1 only** | Sum strict principal gate generators in the certified decomposition. Its recorded SMG1 tests are C P C C. Applying it to GB1 is not an owner decision and encounters GAP 1. Its SMG1 grades were made for finite-dimensional gates; on GB1 it fails the definedness check at irrational \(\tau_E/\pi\). |
| **R-ISO, recorded, not proposed** | Choose the tree-level isotropic step of Theorem 7.3. Tests F P F C. This selects a target-based calibration; it does not make the measure hypercubic invariant. |

## 5. Bounded generators

**Theorem 5.1.** If \(H'\) is bounded, self-adjoint and gauge invariant on \(\mathcal H\), then \(e^{-a_0H'}\) has no transfer-kernel lift of the stated form for even \(N_t\): any nonnegative kernel representation has infinite partition integral.

*Proof.* Gauge averaging gives the nonnegative kernel of \(X=e^{-a_0H'}P_0\). If the cyclic integral were finite, Tonelli and self-adjointness would make \(X^{N_t/2}\) Hilbert–Schmidt, so \(\operatorname{Tr}X^{N_t}<\infty\). But \(X^{N_t}\ge e^{-N_ta_0\|H'\|}P_0\), and \(P_0\) has infinite rank. □

**Theorem 5.2 (corrected draft Proposition 3.2).** Assume \(\tau_E>0\), \(24|\theta|<\pi\), and \(\tau_E/\pi\) irrational. Every finite-register gate has a strict principal generator. Its sum equals the R-SUM \(H_s\) exactly when \(\tau_Es(s+2)/4<\pi\). On the infinite target the electric gate has no strict principal generator. The Borel wrapped sum \(H_{wr}=V_\theta+\sum_\ell w(\tau_EE_\ell^2)\), \(w(x)=x-2\pi\lfloor(x+\pi)/(2\pi)\rfloor\), is bounded and gauge invariant, and Theorem 5.1 applies to it.

*Proof.* No finite electric eigenphase equals −1 under irrationality; the finite spectrum therefore has positive distance from −1. The magnetic norm is below \(\pi\). The wrapped and unwrapped electric eigenvalues agree exactly below \(\pi\), giving the finite-register criterion. On the infinite register, the quadratic phase lemma below, with \(\alpha=\tau_E/(8\pi)\), \(c=\alpha+1/2\), and \(m=k+1\), applied to \(\tau_E k(k+2)/4=2\pi\alpha((k+1)^2-1)\), puts electric eigenphases arbitrarily close to \(\pi\); hence −1 belongs to the closed spectrum. A self-adjoint \(X\) with \(\|X\|<\pi\) would have \(e^{-iX}\) spectrally separated from −1, a contradiction. Borel functional calculus gives the bounded wrapped operator, whose norm can equal \(\pi\); its exponential is the electric gate. □

**Quadratic phase lemma (referee closure, GB1E_REFEREE.md).** If \(\alpha\notin\mathbb Q\) and \(c\in\mathbb R\), then for every \(\epsilon>0\) there is \(m\ge1\) with \(\operatorname{dist}(\alpha m^2-c,\mathbb Z)<\epsilon\).

*Proof.* Write \(e(x)=e^{2\pi ix}\). For \(|u_m|\le1\) on \(1\le m\le M\), zero otherwise, and \(1\le H\le M\), each \(u_m\) occurs \(H\) times in \(\sum_n\sum_{r<H}u_{n+r}\), with \(M+H-1\) values of \(n\). Cauchy–Schwarz and grouping pairs by \(h=r-r'\) give the van der Corput inequality
\[
 |\textstyle\sum_m u_m|^2\le\frac{M+H}{H}\sum_{|h|<H}(1-|h|/H)|S_h|,\qquad S_h=\sum_n u_{n+h}\overline{u_n}.
\]
For an integer \(j\ne0\), take \(u_m=e(j\alpha m^2)\). For \(h\ne0\), the geometric sum gives \(|S_h|\le1/|\sin(2\pi jh\alpha)|\), while \(|S_0|\le M\). Divide by \(M^2\), let \(M\to\infty\), then \(H\to\infty\): \(M^{-1}\sum_{m\le M}e(j\alpha m^2)\to0\).

For \(0<\epsilon<1/2\), the tent function \(f(x)=\max(0,1-\operatorname{dist}(x-c,\mathbb Z)/\epsilon)\) has integral \(\epsilon\), is positive only within \(\epsilon\) of \(c+\mathbb Z\), and has absolutely summable Fourier coefficients \(\widehat f(j)=\epsilon e(-jc)(\sin(\pi j\epsilon)/(\pi j\epsilon))^2\), with the quotient interpreted as 1 at \(j=0\). Dominated convergence of its Fourier series and the preceding limit give \(M^{-1}\sum_{m\le M}f(\alpha m^2)\to\epsilon>0\), so some term is positive. □

**Strict R-GEN on GB1 (referee closure, GB1E_REFEREE.md).** Widening the strict reading to GB1's finite-box cube and link gates defines its Hamiltonian exactly when every gate \(g\) has \(-1\notin\operatorname{spec}g\). For any unitary \(g\), a Hermitian \(X\) with \(e^{-iX}=g\) and \(\|X\|<\pi\) exists exactly under that condition and is unique: the forward direction follows from spectral mapping; conversely the continuous inverse of \(x\mapsto e^{-ix}\) on the spectral arc gives \(X\) by functional calculus, and the same inverse recovers any other such \(X\). This extends `SMG1.md` Lemma G0 to any dimension. Each principal generator commutes with gauge transformations, so their finite sum is bounded, self-adjoint and gauge invariant; Theorem 5.1 excludes its lift. If any gate has −1 in its spectrum, the reading defines no Hamiltonian, including for every irrational \(\tau_E/\pi\) by the quadratic phase lemma. A rational example of failure is \(\tau_E=\pi/2\), \(k=2\).

Both cases occur: for \(\tau_E=\pi/3\), \(24|\theta|<\pi\), the cube generators have norm below \(\pi\), and a link phase is \(\pi\) modulo \(2\pi\) only if \((k+1)^2\equiv13\pmod{24}\), hence \((k+1)^2\equiv5\pmod8\), impossible for a square. The link phases take finitely many values, so −1 is outside their spectrum and the partition obstruction applies.

**R3, recorded only.** If −1 is not an eigenvalue of a unitary \(g\), exactly one Hermitian \(X\) with \(\|X\|\le\pi\) has \(e^{-iX}=g\) (referee closure, GB1E_REFEREE.md). The report records a non-strict variant requiring uniqueness, with author-side tests P P C P; it is not proposed. At irrational \(\tau_E/\pi\) it gives the wrapped link generator, and Theorem 5.1 excludes a lift.

Thus the draft's partition-function obstruction is valid for this explicitly defined wrapped reading and for any supplied bounded gauge-invariant generator. Strict R-GEN gives the same obstruction wherever it is defined, and is undefined at every irrational \(\tau_E/\pi\). For \(\tau_E=0\), Theorem 5.1 applies to \(H=V_\theta\); for \(\tau_E<0\), the proposed transfer is unbounded by Theorem 2.1.

## 6. Reflection positivity

**Theorem 6.1.** The cube-face set is invariant under every spatial coordinate link reflection. A spatial coordinate site reflection exchanges the \(CF\) and non-\(CF\) plaquettes in each plane containing its normal direction. The local and exact lifts are invariant and reflection positive for coordinate link reflections in all four directions. For \(\beta\ne0\), the local lift is not invariant under a spatial coordinate site reflection. For \(\theta\ne0\), the exact lift's transfer does not commute with that reflection.

*Proof.* A direction-1 bond at \(y\) belongs to the unique tiling cube based at \((y_1,y_2-a,y_3-b)\), where \(a\equiv y_2-y_1\), \(b\equiv y_3-y_1\pmod2\). A \((1,2)\)-plaquette is a cube face exactly when \(y_1\equiv y_2\pmod2\); the other planes are analogous. Reflection in \(x_i=m+1/2\) sends the in-plane base coordinate to \(2m-x_i\), preserving parity; reflection in \(x_i=m\) sends it to \(2m-x_i-1\), changing parity.

For a reflection-invariant product of nonnegative plaquette weights, suppose every crossing weight lies in \(\mathcal P\). Expand each crossing character in representation matrices. Replace each crossing-bond Haar variable by the product of two independent Haar variables. Matrix coefficients then separate into reflected half-lattice factors. Integrating gives a sum of nonnegative coefficients times absolute squares of half-lattice integrals. The dimension-moment condition justifies the sums and integrations. This is the crossing-kernel argument of `library/port/p8-positivity.md` on the YM branch, cited through `prior/GB1E.md`; that digest reports it not independently checked. The finite Wilson-slab version is also already in the repository note cited after Theorem 2.2.

For temporal mirrors, only heat-kernel plaquettes cross. For spatial mirrors with \(\beta\ge0\), crossing weights are heat kernels, positive Wilson weights, or 1; Theorem 2.2 applies. For \(\beta<0\), multiply spatial links by a time-independent central sign field with plaquette product −1, for example \(\sigma_{x,1}=(-1)^{x_2+x_3}\), \(\sigma_{x,2}=(-1)^{x_3}\), \(\sigma_{x,3}=1\) for the direction-1 mirror. It is well defined on the even torus, commutes with that reflection, flips every spatial plaquette sign and leaves temporal plaquettes unchanged. Permute coordinates for the other directions. This maps the negative coefficient measure to the positive coefficient case.

For the exact lift, odd subdivision makes each coarse link mirror a fine link mirror. The coarse map intertwines reflections and maps half-algebra functions to fine half-algebra functions. Total-variation convergence in Theorem 3.2 preserves reflection invariance and positivity. For site reflections, distinct plaquette traces occupy orthogonal flux subspaces. The parity change thus changes \(H_B\) by a nonzero function. It changes the local density for \(\beta\ne0\); if the exact transfer commuted with the reflection, injective functional calculus would make its logarithm, hence \(H_B\) for \(\theta\ne0\), commute as well. □

This coordinate link-reflection result does not include spatial site or diagonal mirrors. The digest reports a stronger, isotropic Wilson all-mirror theorem in the YM branch, `library/lg1.md` Theorem 13; it is not imported as a theorem for these lifts.

## 7. Comparison with Wilson SU(2)

**Theorem 7.1.** For \(g\) with eigenvalues \(e^{\pm i\psi}\), normalized Haar integration of a class function is \((2/\pi)\int_0^\pi f(\psi)\sin^2\psi\,d\psi\), and
\[
 z_k(\psi)=(k+1)\frac{\sin((k+1)\psi)}{\sin\psi},\qquad
 c_k(e^{b\operatorname{Tr}})=\frac{I_{k+1}(2b)}b\quad(b\ne0),
\]
where convolution by a class function \(f\) acts on \(H_k\) by \(c_k(f)=(k+1)^{-2}\int fz_k\,dU\), and \(I_j(x)=\sum_{r\ge0}(x/2)^{j+2r}/(r!(j+r)!)\). For \(b=0\), \(c_k=\delta_{k0}\). No \(t>0\) and real \(a,b\) satisfy \(k_t(g)=e^{a+b\operatorname{Tr}g}\) on a neighborhood of the identity.

*Proof.* Spherical coordinates give Haar integration. The zonal harmonic is the unique degree-\(k\) polynomial solution of \((1-u^2)P''-3uP'+k(k+2)P=0\), normalized at \(u=1\); this gives the sine quotient. The sine basis and orthogonality of \(\Pi_k\) give the convolution multiplier. Expand \(e^{2b\cos\psi}\) and integrate cosines; \(I_k(x)-I_{k+2}(x)=2(k+1)I_{k+1}(x)/x\) gives the formula. Both candidate weights are analytic in \(\psi\), so equality near zero gives equality of all multipliers. For \(b\ne0\), \(|c_k|\ge |b|^k/(k+1)!\), while the heat multiplier is \(e^{-tk(k+2)/4}\); their equality fails for large \(k\). For \(b=0\), all nonconstant multipliers vanish. □

**Theorem 7.2.** On a cubic four-torus \(N_t=N\), \(\mu_{\rm loc}\) is never invariant under exchanging time with a spatial axis, and hence is never the isotropic Wilson measure. If \(\beta\ne0\), it is also not invariant under a unit spatial translation. For fixed \(\tau_E,a_0>0\), possible time–space exchange invariance of \(\mu_{\rm ex}\) is confined to a discrete subset of \(\mathbb R\setminus\{0\}\).

*Proof.* Vary a single link near the identity. A spatial link meets two \(CF\), two other spatial, and two temporal plaquettes; a temporal link meets six temporal plaquettes. Invariance under exchange would give \(2g_W+2g_K=6g_K\), where \(g_W=2\beta(\cos\psi-1)\) and \(g_K=\log k_t(\psi)-\log k_t(0)\). This makes \(k_t\) a Wilson weight near the identity, contrary to Theorem 7.1. A unit spatial translation exchanges \(CF\) and non-\(CF\) plaquettes in planes containing that direction; orthogonality of distinct plaquette traces proves the second statement.

For the exact lift, at \(\theta=0\) it is the local lift with \(\beta=0\), so it is not exchange invariant. Choose neighboring spatial plaquettes \(p\in CF\), \(p'\notin CF\), and define \(\Delta(\theta)=\langle\operatorname{Tr}X_p-\operatorname{Tr}X_{p'}\rangle\). Exchange invariance and time-translation invariance force \(\Delta=0\). The Duhamel series for the finite-box Gibbs trace is entire in \(\theta\): in the \(m\)-th term one heat segment has length at least \(N_ta_0/(m+1)\), and \(\Theta(u)=O(1+u^{-3/2})\), which leaves a summable factorial bound. At zero, distinct plaquette flux sectors are orthogonal. Differentiation gives
\[
 \Delta'(0)=-\frac2{Z_0}\int_0^{N_ta_0}\!\|e^{-u\tau_EA/2}(\operatorname{Tr}X_p)P_0e^{-(N_ta_0-u)\tau_EA/2}\|_2^2\,du<0.
\]
Thus \(\Delta\) is nonzero real analytic, and its zeros are discrete. Since the measure at zero is already noninvariant, the possible set excludes zero. □

The sign field \(\Psi\) of Theorem 6.1 commutes with \(A\) and \(P_0\), and conjugates \(H_B\) to \(-H_B\). It changes the sign of each spatial plaquette trace, so \(\Delta(-\theta)=-\Delta(\theta)\); the possible exceptional set is symmetric (referee closure, GB1E_REFEREE.md).

**Theorem 7.3 (tree-level dictionary).** Write
\[
 c_t=\frac23\frac{\sum_k(k+1)^2\frac{k(k+2)}4e^{-tk(k+2)/4}}{\sum_k(k+1)^2e^{-tk(k+2)/4}}.
\]
Then \(\log k_t(\psi)=\log k_t(0)-c_t\psi^2+O(\psi^4)\), \(c_t\) decreases strictly from infinity to zero, and \(tc_t\to1\) as \(t\downarrow0\). For \(\theta<0<\tau_E\), \(\beta=2\lambda|\theta|\), \(t=\lambda\tau_E\), the draft's smooth-field, \(CF\)-averaged classical normalization gives
\[
 \xi_{cl}^2=2c_t/\beta,\quad g_{cl}^4=8/(c_t\beta),\quad
 \xi_{cl}\sim(\lambda^2|\theta|\tau_E)^{-1/2},\quad
 g_{cl}^2\to2(\tau_E/|\theta|)^{1/2}.
\]
There is one tree-level isotropic step, determined by \(c_{\lambda\tau_E}=\lambda|\theta|\).

*Proof.* Expand the sine quotient through \(\psi^2\). Differentiating the weighted mean gives \(dc_t/dt=-(2/3)\operatorname{Var}_t(E^2)<0\). Gaussian Riemann sums give \(\langle E^2\rangle_t\sim3/(2t)\); at infinity the zero mode dominates. Spatial plaquettes contribute stiffness \(\beta\) on half the plaquettes and zero on the rest, while temporal plaquettes have stiffness \(c_t\). Match the resulting quadratic form for a smooth connection with spacings \(a,a_0\) to the isotropic Wilson calibration \(g^2=4/x_0\); this yields the displayed expressions. Strict monotonicity gives the unique crossing. □

This is a smooth-field tree-level comparison, not a quantum anisotropy or universality theorem. Both lifts and T0 use SU(2) and product Haar reference. T0 uses Wilson weight \(e^{(x_0/2)\operatorname{Tr}W}\) on every plaquette. The local lift uses heat weights in time and cube-face weights in space; the exact lift need not have a finite plaquette-product action. The normalized Wilson temporal multipliers are \(I_{k+1}(x_0)/I_1(x_0)\), versus \(e^{-tk(k+2)/4}\) for the heat kernel. A fixed law's angles do not specify a T0 coupling trajectory; the asymptotic dictionary suggests a family with \(\tau_E/|\theta|\to0\), subject to its approximation regime. `GB1.md` row H5 already names the need for a law family or a suitable T0-start and T0-rate. A trajectory or renormalized coupling is not proved here.

## 8. Finite registers and regulator limit

Let \(R_s=\bigoplus_{k\le s}H_k\), \(d_s=\sum_{k\le s}(k+1)^2\), \(\iota\) be its inclusion in \(\mathcal K\), and \(D_s(x,y)=\sum_{k\le s}Z_k(x,y)\). Set \(m_s=-\min D_s\).

**Theorem 8.1.** For \(s\ge1\), \(m_s>0\). If \(X=X^*\) on \(R_s^{\otimes\mathcal L}\) and \(\|X-1\|<m_s/d_s\), the real part of the continuous kernel of \(\iota_{\mathcal L}X\iota_{\mathcal L}^*\) is negative on a nonempty open set. Thus, for any finite-register Hermitian \(H_s\), its embedded \(e^{-a_0H_s}\) has no nonnegative kernel when \(0<a_0<\log(1+m_s/d_s)/\|H_s\|\); if \(H_s=0\), the conclusion holds for every \(a_0>0\). For R-SUM with \(\theta=0\), it holds whenever \(0<a_0\tau_E<4\log(1+m_s/d_s)/(s(s+2))\), independently of box size.

*Proof.* \(D_s(e,\cdot)\) integrates to one and reproduces \(y_4\), whose value at \(e\) is one. If it were nonnegative, its integral against \(1-y_4\) would vanish although \(1-y_4>0\) except at a Haar-null point, a contradiction. At the configuration pair with one link at a negative minimum and all others at the identity, the projection kernel is \(-m_sd_s^{|\mathcal L|-1}\). Cauchy–Schwarz bounds the kernel change by \(\|X-1\|d_s^{|\mathcal L|}\). A self-adjoint kernel can be complex off the diagonal. The bound therefore shows that its **real part** is negative there, which excludes a nonnegative kernel. Continuity gives an open set. The exponential norm bound proves the threshold. At \(\theta=0\), factor over links and use the one-link bound; all other diagonal factors are positive. □

The draft's statement that an arbitrary operator's kernel is "negative" is ill-defined for a complex kernel. The real-part formulation above is the correction. The conclusion excludes this particular embedded group-variable transfer, not every possible measure or every Euclidean step.

**Theorem 8.2.** A finite-dimensional continuous unitary representation of a connected group which preserves the nonnegative cone of some orthonormal basis is trivial.

*Proof.* Each unitary matrix has nonnegative orthonormal columns, hence is a permutation matrix. A continuous map from a connected group to the finite set of permutations is constant and equals the identity at the group identity. □

This excludes a basis in which the nontrivial register gauge action itself acts by positive transformations. It does not prove that every gauge-invariant measure requires an infinite register, nor exclude other representations.

**Theorem 8.3.** On a fixed box, for \(\tau_E>0\), the R-SUM finite-register Hamiltonians \(H_s\) obey
\[
 \|\iota_{\mathcal L}e^{-a_0H_s}\iota_{\mathcal L}^*-e^{-a_0H}\|_1\longrightarrow0.
\]
For bounded slice functions, their gauge-projected finite-temperature correlators converge to the corresponding correlators of \(\mu_{\rm ex}\).

*Proof.* Extend the finite-register potential by zero outside \(\Pi_s\). It is uniformly bounded and converges strongly to \(V_\theta\) by the plaquette approximation of `GB1QL.md` Lemma 4.7 and density of finite-flux vectors. Duhamel gives strong convergence of the heat operators. Min–max on projected low-energy eigenvectors gives the eigenvalue limsup; compactness of the electric form domain, strong convergence of the bounded potentials, and lower semicontinuity give the liminf. Each ordered eigenvalue is bounded below by \(\tau_E\alpha_i-C\). Dominated convergence therefore gives convergence of traces. Strong convergence plus convergence of traces for positive trace-class operators gives trace-norm convergence: split with a finite-rank projection and bound the tails by Cauchy–Schwarz for Hilbert–Schmidt operators. The compressed bounded slice multipliers converge strongly, as do their adjoints; trace-norm convergence and the nonzero limiting partition function yield the correlator statement. □

The limit is fixed-box, fixed \(a_0,N_t\), then \(s\to\infty\). It does not prove that the fixed-register kernels are probability measures, nor a volume-uniform estimate. The volume-uniform, finite-time SU(2) real-time regulator comparison was already proved in `GB1QL.md` Theorem 4.8 and Corollaries 4.9-4.10; the digest also identifies a different supplied SU(3) local-observable cutoff result in `docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`, with its own hypotheses and unaudited status.

## 9. Hand-off and checks

| Input | Finite-box result | Remaining step |
|---|---|---|
| (H-G) | SU(2) gauge covariance is supplied by the proposed test law (`GB1QL.md` Proposition 4.11(a)). | Physical law and framework identification remain open. |
| (H-4D), (H-GI), (H-Haar) | Both target lifts are gauge-invariant finite-torus link probabilities with bounded Haar densities, under their stated readings. | Construct the required infinite-lattice object and its consistency. The finite-register embedded kernel fails positivity for the small steps of Theorem 8.1. |
| (H-RP) | Coordinate link reflections on the finite tori, Theorem 6.1. | Establish the precise reflection geometry and half-algebra required by the consumer, including any limiting step. Axis RP alone does not imply O(4). |
| (H-class) | The local lift is not isotropic Wilson; both lifts fail time–space exchange generically. If the specified class consists only of hypercubic-invariant densities, this excludes the local lift and the exact lift outside the exceptional set. | Pin \(\mathcal A_{k_0}(g)\) and topology; decide the exceptional exact-lift cases and the small-coupling condition. |
| T0-rate, Y3, E-2, VC1 | Not supplied. | See the named open items in §0. |

The first missing input in the original infinite-lattice hand-off remains (H-4D) unless the finite-box construction is extended with the required consistency. `GB1QL.md` Lemma H already establishes that measure properties cannot be inferred merely from slice covariance. Under (i) T0-start[G] in its torus form with \(N_t=N\) even, (ii) (H-RP) read as (P8.1), and (iii) a class \(\mathcal A_{k_0}(g)\) of densities invariant under exchanging time with a space axis, (H-class) fails first: for the local lift at every parameter and for the exact lift outside the discrete exceptional set. With LG1 Theorem 13's mirror set, (H-RP) fails first. Without condition (iii), the class decision remains open; on \(\mathbb Z^4\), (H-4D) is not delivered. Under the wrapped bounded reading, Theorem 5.1 gives a finite-box partition obstruction. Under strict R-GEN widened to GB1, no \(\tau_E\) gives a Hamiltonian with a transfer-kernel lift; the first failing step is the existence of the generator at every irrational \(\tau_E/\pi\), and the partition function wherever the generator exists. No proposed reading is adopted here.

The local transfer is the imaginary-angle continuation of the target tick, not the original unitary update as a positive transfer. The exact lift is the Trotter limit of those continued layers. Neither statement selects the framework state or proves its ground-state relation. The finite-temperature Gibbs trace converges to the target measure's correlators as \(s\to\infty\); this is not finite-\(s\) positivity or a proof of Y1 on \(\mathbb Z^3\times\mathbb Z\).

**Draft scratch checks, not independently rerun.** The pass-1 script `/tmp/toe-GB1E/check_hk.py` sampled 2001 angles and truncated at \(k=400\). It reported minima of the heat kernel of approximately \(-6.4\cdot10^{-12},-8.7\cdot10^{-13},8.8\cdot10^{-3},0.80\) at \(t=0.05,0.2,1,4\), respectively, and numerical integrals 1.000000. The draft attributes the small negative values to roundoff; this is not an independent certificate. It reported character-orthogonality error \(7\cdot10^{-10}\) for \(j,k<6\), and Wilson multiplier agreement to \(10^{-11}\) for \(b=0.5,2\), \(k\le5\). For \(s=1,\ldots,5\), it reported minima of \(D_s\) of \(-3,-2.333,-10,-6.034,-21\). It also reported one-link band-limited heat-kernel minima \(-2.97,-2.71,-1.75\) for \(s=1\), and \(-21.2,-1.35,-5.5\cdot10^{-5}\) for \(s=8\), at \(t=0.01,0.1,0.5\); sampled kernels were positive at \(t=2\) for \(s\le8\). These computations motivate no general positivity claim.

**Literature scope.** Pass 1 reports reading abstracts or selected sections of arXiv:2107.01166, 2103.02602, 2208.10417, hep-lat/0311014, hep-th/9511179, hep-lat/9609042 and 1802.07880. It reports only bibliographic records or incomplete texts for Creutz, Lüscher, Osterwalder–Seiler, Seiler, Kogut–Susskind, Karsch, Menotti–Onofri and Fradkin–Susskind. These were not rechecked in pass 2 and are not proof inputs. In particular numerical or perturbative universality evidence does not prove the needed anisotropic-to-isotropic extension.
