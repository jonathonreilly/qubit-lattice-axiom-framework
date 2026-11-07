# GB1ISO. Isotropy of the cube-face gauge bridge

## 0. Status

**Pass 2; not refereed or frozen.** This item concerns the proposed empty-matter SU(2) test family and its two proposed Euclidean readings. It does not select a law, a reading, a physical vacuum, or an axiom.

**Proved here, conditional on the cited inputs.** The cube-face tick and both transfers factor over disjoint link cubes. Each transfer has a unique positive cube-product top state. Its equal-sided torus limit exists, with the bound in Theorem 3.2. Gauge-invariant observables on distinct cubes factor in that limit, while a cube magnetic observable has strictly positive autocovariance at every finite time separation. The exact R-SUM lift is not invariant under time-space exchange at any parameter: GB1E-ς is closed at the stated finite-torus scope. A rotation-invariant continuum two-point distribution obtained from uniformly bounded-range observables has no separated-point part (Theorem 5.2). The proposed FP layer gives the full plaquette sum on the infinite-register target; its local R-IA lift is not exchange invariant on the finite torus.

**GAP: asymptotic isotropy and T0 admission.** Strictly positive temporal correlations at each finite separation do not prove a nonvanishing anisotropy as separation tends to infinity: those correlations also decay to zero. Theorem 5.2 excludes a *nonzero separated two-point limit* under its explicit hypotheses, not every conceivable block transformation, action class, or T0-rate. The action class and the observable normalization and comparison needed for T0-rate remain unpinned. Finite-measure exchange failure decides membership only for a class requiring that symmetry. The draft's unconditional class-independent first-failure and rate claims are not established.

**GAP: maximum-weight configurations.** The draft does not prove its global classification on a periodic time circle or specify the allowed temporal holonomy. Section 5 gives the supported local statement and an example showing why holonomy must be retained.

**Open by name.** ISO-FP; T0-start^an[G]; GB1-CF; (H-class) for the actual unpinned class; the full reflection interface; Y1's local action and selected-state identification; Y2, Y3, E-2, VC1, T0-rate, and volume-uniform register convergence. GB1E-ς is closed only as above. The owner has adopted none of R-SUM, R-IA, R-ISO, or FP.

**Provenance.** Pass 1: `GB1ISO_DRAFT.md`, Claude Opus 5.5, max, as recorded there. Pass 2: Codex `gpt-6.1-terra`; effort and session id: see run log. Draft SHA-256 `cbde65e404a0dbcd8e081953ff7b17d668ee08dc13f811cb962b5ca32e6c9bba`; digest `prior/GB1ISO.md` SHA-256 `e35dee0a3c152e796f580a4144111593de075cea8740a45ddc58ebdd2b194c7d`. The source's scratch scripts and logs are unavailable here; their reported checks below are not reruns. This check is not an independent referee or audit.

## 1. Definitions inferred by the distiller

Fix even \(N\ge4\), \(N_t\ge3\), spatial torus \(\Lambda=(\mathbb Z/N\mathbb Z)^3\), its positively oriented links \(\mathcal L\), normalized Haar measure, and \(\mathcal H=\bigotimes_{\ell\in\mathcal L}L^2(SU(2))\). For a link \(xy\), \((h\cdot U)_{xy}=h_y^{-1}U_{xy}h_x\). Let \(P_0\) average the corresponding representation over \(SU(2)^\Lambda\).

Let \(\mathcal C\) be the unit cubes whose base coordinates have equal parity. Their spatial plaquettes form \(CF\). Write \(\ell(C)\) for the 12 links of \(C\), \(B_p=2\operatorname{Tr}X_p\) with the holonomy of `GB1QL.md` §1.3, \(B_C=\sum_{p\subset C}B_p\), \(H_B=\sum_{p\in CF}B_p\), \(A=\sum_\ell E_\ell^2\), and \(A_C=\sum_{\ell\in\ell(C)}E_\ell^2\). The unnormalized trace is in the defining representation. The electric eigenvalue on degree \(k\) is \(k(k+2)/4\); \(k_t\) is the corresponding SU(2) heat kernel.

For **R-SUM, proposed**, fix \(\theta\in\mathbb R\), \(\tau_E,a_0>0\), set \(H=\tau_E A+\theta H_B\), and use \(T=e^{-a_0H}\). For **R-IA, proposed**, fix \(\lambda,\tau_E>0\), \(\theta\in\mathbb R\), put \(t=\lambda\tau_E\), \(\beta=-2\lambda\theta\), and use \(T=e^{\beta H_B/4}e^{-tA}e^{\beta H_B/4}\). More generally the local transfer below allows any \(\beta\in\mathbb R,t>0\). The transfer-kernel lift is the normalized product of \(\kappa(U_r,V_r\cdot U_{r+1})\) against Haar measure, as in `GB1E.md` §1. The readings' recorded checks are R-SUM P P C C, R-IA P C C C. R-ISO is a recorded, not proposed, tree-level calibration; its checks are F P F C (`GB1E.md` §4).

The **cube-wise gauge group** is \(\mathcal G_\square=\prod_CSU(2)^{\mathrm{corners}(C)}\), acting separately on each cube's link factors. The ordinary site group is its diagonal subgroup at shared sites. A bounded local gauge-invariant four-dimensional observable \(F\) lies in a finite time window \([r_1,r_2]\), \(w=r_2-r_1<N_t\). Let \(\widetilde F\) be its expression after setting the temporal links inside the window to the identity. Its **cube support** is the set of cubes containing spatial links on which \(\widetilde F\) depends. Pure temporal local observables may be included after gauge averaging; their temporal-gauge representatives must have finite spatial support. All limits called equal-sided below take \(N=N_t\to\infty\) through even integers, with a fixed local observable and fixed transfer parameters.

## 2. Cubes, kernels and transfer lemmas

**Theorem 2.1 (tiling and factorization).** Each link belongs to one cube in \(\mathcal C\), each site to two, and \(|\mathcal C|=N^3/4\). A plaquette in the \((i,j)\)-plane belongs to \(CF\) exactly when its in-plane base coordinates have equal parity. Thus, on empty matter,
\[
 U_{KS}=\bigotimes_C(e^{-i\theta B_C}e^{-i\tau_EA_C}),\quad
 T_{\rm ex}=\bigotimes_C e^{-a_0(\tau_EA_C+\theta B_C)},\quad
 T_{\rm loc}=\bigotimes_C e^{\beta B_C/4}e^{-tA_C}e^{\beta B_C/4}.
\]
Each factor commutes with its independent cube-corner gauge group.

*Proof.* A direction-1 link at \(y\) belongs to a cube with base \(b_1=y_1\), \(b_2\in\{y_2,y_2-1\}\), \(b_3\in\{y_3,y_3-1\}\). Equal base parities choose a unique cube. Relabel axes; counting links gives the cube count. A site is a corner of exactly one cube of each base parity. A face in plane \((i,j)\) has base coordinates fixed in those directions; equal parity is necessary and sufficient. Regroup the independent electric and magnetic factors. The exact semigroup factorizes by the product formula or the functional calculus for commuting tensor-factor Hamiltonians. Casimirs and traced face holonomies are invariant under the corner group. □

The link partition is already proved in `GA1_5.md` Theorem 2.1; the SU(2) tick and empty-matter reduction are in `GB1QL.md` §1.3 and `GB1.md` Theorem 2.2. The abelian one-layer precursor of the extra symmetry is `GA1_5.md` Theorem 2.2. These results do not by themselves supply the correlation conclusions below.

**Theorem 2.2 (strict heat-kernel positivity).** \(k_t(g)>0\) for every \(t>0\) and \(g\in SU(2)\); its minimum \(m_t\) is positive.

*Proof.* By `GB1E.md` Theorem 7.1, for eigenvalues \(e^{\pm i\psi}\), \(0<\psi<\pi\), put \(q=e^{-t/4}\) and \(\vartheta(\psi)=\sum_{m\in\mathbb Z}q^{m^2}e^{im\psi}\). Then \(k_t=e^{t/4}(-\vartheta')/(2\sin\psi)\). Let \(P(z)=\prod_{n\ge1}(1+q^{2n-1}z)(1+q^{2n-1}z^{-1})\). Locally uniform convergence on \(\mathbb C^*\) and \(P(q^2z)=P(z)/(qz)\) imply its Laurent coefficients are \(c_m=c_0q^{m^2}\). Evaluation at \(z=1\) gives \(c_0>0\). Hence \(\vartheta(\psi)=P(e^{i\psi})/c_0>0\), and logarithmic differentiation yields
\[
 k_t(\psi)=e^{t/4}\vartheta(\psi)\sum_{n\ge1}\frac{q^{2n-1}}{1+2q^{2n-1}\cos\psi+q^{4n-2}}>0.
\]
The right side extends continuously and positively to both endpoints. Compactness gives the minimum. This is the needed part of Jacobi's triple product. □

**Theorem 2.3 (positive cube transfers).** Both cube transfers are positive, injective, trace class, and have real symmetric kernels bounded above and below by positive constants. Their top eigenvalue \(\lambda_0\) is simple, with a strictly positive normalized eigenvector \(\Omega_C\), invariant under every cube-corner gauge transformation. All other eigenvalues are positive and at most \(q\lambda_0\), for some \(q<1\).

*Proof.* Since \(|B_C|\le24\), the local kernel is bounded between \(e^{-12|\beta|}m_t^{12}\) and \(e^{12|\beta|}k_t(e)^{12}\). For the exact kernel, the symmetric product formula and heat-kernel convolution give bounds \(e^{\mp24a_0|\theta|}\prod_{\ell\in C}k_{a_0\tau_E}(U_\ell U_\ell'^{-1})\); trace-norm convergence passes them to the limiting kernel almost everywhere. Trace class and injectivity follow from the heat semigroup, bounded multipliers and spectral calculus. For a compact positive self-adjoint operator with a kernel bounded below by \(c>0\), the Rayleigh quotient of \(|f|\) is at least that of a real top eigenvector \(f\), with equality only if \(f\) has a constant sign. The eigenvalue equation then makes it strictly positive. Two orthogonal top eigenvectors cannot both have a constant strict sign, so the eigenvalue is simple. A gauge transformation commutes with the transfer and preserves positivity and norm; uniqueness makes it fix \(\Omega_C\). Compactness and injectivity give the remaining spectral assertions. □

**Theorem 2.4 (temporal gauge and cycle).** For a transfer with nonnegative gauge-covariant kernel, let \(\mathfrak F\) be the window chain kernel obtained by inserting \(\widetilde F\) between its endpoint slices. Then
\[
 \mathbb E F=\frac{\operatorname{Tr}(\mathfrak F T^{N_t-w}P_0)}{\operatorname{Tr}(T^{N_t}P_0)}.
\]
If a slice isometry \(s\) preserves the full lift, and the kernel of \(TP_0\) is symmetric and bounded above and below by positive constants, then its induced unitary commutes with \(TP_0\).

*Proof.* Use successive gauge transformations inside the window to set its temporal links to one; Haar invariance leaves the exterior chain and its gauge average \(P_0\). For the second assertion, integrate all temporal links. The spatial marginal is the cyclic product of the kernel \(\bar\kappa\) of \(TP_0\). Set \(f(x,y)=\log\bar\kappa(sx,sy)-\log\bar\kappa(x,y)\). It is bounded and symmetric, and the sum of \(f\) around almost every \(N_t\)-cycle is zero. For \(n\ge3\), integrating such a cycle over all but \(x,y\) gives \(f(x,y)=-a(x)-a(y)-(n-3)c\), where \(a(x)=\int f(x,u)du\) and \(c=\int a\). Further integration gives \(c=a=0\), hence \(f=0\) almost everywhere. Equality of kernels is the desired commutation. □

## 3. Product state and correlations

**Theorem 3.1 (draft D1–D2).** The finite-volume top eigenspace of either transfer is spanned by \(\Omega=\bigotimes_C\Omega_C\). It is invariant under \(\mathcal G_\square\), hence lies in \(P_0\mathcal H\). For R-SUM it is the unique ground state of \(H\), also in the gauge-invariant sector. Any operator supported on cube factors \(S\) remains on those factors under any integer number of empty-matter ticks. The same support statement holds for the finite-register cube-face ticks of `GB1QL.md` and the other cube-face rungs.

*Proof.* Tensor products of the simple cube top eigenvectors give the unique top eigenvector. Theorem 2.3 gives its gauge invariance. For R-SUM, spectral calculus relates the top eigenvalue of \(e^{-a_0H}\) to the bottom eigenvalue of \(H\). Tick factors have the same cube support at every power; the argument uses only gate supports for finite registers. □

**Theorem 3.2 (draft D3–D5).** Fix the parameters of either reading. Let \(F\) have window length \(w\) and cube support \(S\). Put \(\varepsilon_m=\operatorname{Tr}(T_C^m)/\lambda_0^m-1\), \(\delta_N=(1+\varepsilon_{N-w})^{N^3/4}-1\), and
\[
 \omega_\infty(F)=\lambda_0^{-w|S|}\langle\Omega_S,\mathfrak F_S\Omega_S\rangle.
\]
Then, for even \(N=N_t>w\),
\[
 |\mathbb EF-\omega_\infty(F)|\le2\|F\|_\infty\delta_N,\qquad
 \varepsilon_m\le q^{m-1}\operatorname{Tr}(T_C)/\lambda_0,
\]
so the limit exists. If \(S(F)\cap S(G)=\varnothing\), then \(\omega_\infty(FG)=\omega_\infty(F)\omega_\infty(G)\), at any finite time separation. In particular this holds when their spatial link endpoints are at sup-distance at least two. For every \(\tau\ge0\),
\[
 \operatorname{Cov}_{\omega_\infty}(B_C(0),B_C(\tau))
 =\sum_{n\ge1}|\langle\varphi_n,B_C\Omega_C\rangle|^2(\lambda_n/\lambda_0)^\tau>0.
\]

*Proof.* The cube spectra are identical under tiling-preserving translations. Let \(\Lambda=\lambda_0^{N^3/4}\) and \(\Pi=|\Omega\rangle\langle\Omega|\). The tensor product gives \(T^m/\Lambda^m=\Pi+R_m\), with \(R_m\ge0\), \(\operatorname{Tr}R_m=\delta_N\), and \(P_0R_mP_0\le R_m\) in trace. Theorem 2.4 and the kernel bound \(|\mathfrak F|\le\|F\|_\infty T^w\) yield the displayed error; the factorization of \(\mathfrak F\) yields the formula for \(\omega_\infty\). The eigenvalue ratio bound makes \(N^3\varepsilon_{N-w}\to0\). Separate cube supports factor the window kernel and the product state. No cube contains link endpoints at sup-distance two. Finally insert the cube spectral resolution. The nonconstant function \(B_C\) takes values 24 at identity and 8 when one link is \(-1\) and all others are identity. Since \(\Omega_C>0\), its variance is positive; injectivity makes every term's temporal factor positive. □

**Theorem 3.3 (draft D8).** The equal-sided torus lifts converge on bounded local observables to a gauge-invariant probability measure on \(SU(2)\) link configurations on \(\mathbb Z^3\times\mathbb Z\).

*Proof.* Average any local observable over gauge transformations at its finitely many incident sites. Finite-volume gauge invariance leaves its expectation unchanged, and Theorem 3.2 gives the limit. Positivity, normalization and consistency pass to limits. Compactness of the countable product and the Riesz representation theorem give the measure. Gauge invariance passes to the limit. This proves existence along this sequence, not a local action or Y1's physical state identification. □

## 4. Finite-torus exchange symmetry

**Theorem 4.1 (draft A; GB1E-ς).** On the even cubic four-torus \(N=N_t\ge4\), the R-SUM exact lift is not invariant under any lattice isometry mapping time to a spatial direction, for any \(\theta\in\mathbb R\), \(\tau_E,a_0>0\). For \(\theta\ne0\) it is also not invariant under a unit spatial translation or a spatial coordinate site reflection.

*Proof.* At \(\theta=0\), the exact lift equals the local lift at \(\beta=0\), already excluded by `GB1E.md` Theorem 7.2. Suppose \(\theta\ne0\). The measure is invariant under unit time translation. A time-space exchange would conjugate that translation to a unit spatial translation. The exact kernel and its gauge average are bounded above and below by positive constants by Theorem 2.3, so Theorem 2.4 makes that translation commute with \(TP_0\). On the gauge-invariant sector, logarithmic functional calculus makes it commute with \(H\). It also commutes with \(A\); applying the resulting identity to the constant function gives equality of \(H_B\) and its translate. This is false: a unit translation changes cube-face plaquettes to omitted plaquettes in planes containing that direction. Distinct plaquette traces are nonzero and orthogonal in Haar \(L^2\), since their distinct link supports contain a link carrying a nonconstant matrix coefficient in just one trace. A site reflection likewise exchanges the selected and omitted faces in those planes (`GB1E.md` Theorem 6.1). The same argument excludes those slice symmetries. □

The prior exceptional discrete set in `GB1E.md` Theorem 7.2 is therefore empty for this exact lift. The proof uses the cyclic transfer marginal, rather than the three failed attacks in `GB1E_REFEREE.md` §3.2: extra characters could not exclude common zeros, convexity did not separate face means, and the spatial Markov-property violation was not shown.

**Theorem 4.2 (draft D6, fixed lattice).** For either reading and every fixed parameter, the limit measure is not invariant under a lattice isometry exchanging time and space. This remains true at the R-ISO tree-level step, when that step exists.

*Proof.* A cube-face observable and its time translate by \(\tau\ge3\) have positive covariance by Theorem 3.2. After a time-space exchange the corresponding finite Wilson-loop observables occupy spatially separated regions, with all spatial link endpoints at sup-distance at least \(\tau-1\ge2\). Temporal gauge makes their cube supports disjoint. Theorem 3.2 gives zero covariance. An invariant measure would give equal values. □

**GAP: “no restoration at any scale.”** The preceding proof establishes failure of exact exchange invariance at each fixed finite lattice separation. It does not establish a nonzero lower bound at large separation: the temporal covariance is bounded by \(q^\tau\operatorname{Var}(B_C)\) and tends to zero. A time rescaling does not change the fixed-parameter zero-versus-positive distinction, but a scaling limit can still be the zero distribution, or can require changing parameters and observable normalizations. Theorem 5.2 states the supported continuum conclusion. Neither a finite-distance mismatch nor a vanishing limit alone establishes the draft's claimed rate failure.

## 5. Classical dynamics and continuum consequences

**Theorem 5.1 (draft F, corrected).** The classical cube-face Hamiltonian \(\tau_E\sum_\ell|E_\ell|^2+\theta\sum_CB_C\) has a product flow over cubes. Its linearization at \(U=1\) has cube-local normal modes and flat bands, hence zero group velocity. Per Lie-algebra direction, the kernel of the linearized cube-face flux map has dimension \(7N^3/4\), while that of the full plaquette flux map has dimension \(N^3+2\); the difference is \(3N^3/4-2\).

*Proof.* Disjoint cubes carry disjoint canonical variables, so their Hamiltonian flows factor. The same finite matrix is repeated over a tiling cell; its Bloch eigenvalues are independent of momentum. The cube graph has 12 edges and 8 vertices. Its six face boundaries span its five-dimensional cycle space, so zero face fluxes are gradients, a seven-dimensional space. Sum over \(N^3/4\) cubes. On the full 3-torus, closed 1-cochains consist of \(N^3-1\) exact ones and three independent periods. □

**GAP: draft F(b), global maxima.** The draft asserts a global classification modulo four-dimensional gauge but gives no proof that temporal flatness has the claimed static representative on a periodic time circle, or how temporal holonomy enters it. The local statement is that maximal positive-\(\beta\) spatial face weights impose identity face holonomies, hence a pure gauge on each individual spatial cube. Temporal maximality imposes identity temporal plaquettes but leaves global holonomy data. For example, set all spatial links to identity and all temporal links to identity except one time slice, where every temporal link equals \(-I\). All plaquette weights are maximal, but each temporal Polyakov loop is \(-I\), which no periodic gauge transformation can turn into \(I\). This does not by itself refute the draft's static-representative claim: a static representative may retain that holonomy. It does refute any interpretation that silently sets all temporal links to identity. The draft's negative-\(\beta\) global classification likewise needs a proof retaining this data.

The tree-level smooth-field stiffness matching in `GB1E.md` Theorem 7.3 is already proved there. It does not assert a propagation speed. The flat cube modes explain why it does not rule out the factorization above.

**Theorem 5.2 (draft D7, scoped).** Let \(a_k\to0\), and take any sequence of the equal-sided limit states of these lifts, allowing parameters to vary. Let \(\rho_k(x)\) be gauge-invariant observables with spatial support within a fixed number of fine lattice units of \(x\), and let \(O_k(f)=a_k^4\sum_x f(x)\rho_k(x)\), with any deterministic normalization absorbed into \(\rho_k\). Assume their connected two-point functions converge on separated tests to a distribution \(S\). If \(S\) is invariant under \(D_cSO(4)D_c^{-1}\), \(D_c=\operatorname{diag}(c,1,1,1)\), for a fixed \(0<c<\infty\), then \(S\) vanishes on all separated tests. The conclusion also applies to block images whose relevant observable pullbacks have uniformly bounded fine-lattice spatial support and are gauge invariant.

*Proof.* If the spatial projections of the test supports have positive separation, their summands have disjoint cube supports for all sufficiently small \(a_k\), so their covariance is exactly zero. A partition of unity and density of tensor products show that \(S(x,y)\) vanishes where the spatial parts of \(x,y\) differ. Any nonzero four-vector can be rotated after applying \(D_c^{-1}\) to have a nonzero spatial component. Rotated copies of that open set cover the off-diagonal, and invariance carries the vanishing to each copy. A block observable with the stated pullback property obeys the same support argument. □

**GAP: block and T0 conclusions.** The draft calls every bounded-range block map covered without specifying whether its range is bounded in fine or coarse units, or whether repeated RG steps have uniformly bounded fine support. The theorem covers only the stated pullback condition. It also assumes convergence and a fixed finite rescaling. If T0's particular normalized action-density correlator is known to have a nonzero separated limit, the theorem excludes such a limit for this family under those hypotheses. The supplied material does not prove the full T0-start conclusion, its required normalization, every block image, or an independent rate contradiction. Membership in an unpinned class cannot be decided in general by this argument. A zero separated correlator is compatible with rotation invariance by itself.

## 6. Proposed full-plaquette layer and open interfaces

**FP, proposed, not adopted.** Replace the magnetic layer by
\[
 W_B^{FP}=\prod_{v\in\{0,e_1,e_2,e_3\}}\ \prod_{C\in\mathcal C+v} e^{-i(\theta/2)B_C}.
\]

**Theorem 6.1 (FP counting and finite-torus local lift).** Each of the four layers uses disjoint-link cubes. Every spatial plaquette occurs twice in their combined face sum. On the infinite-register target all \(B_C\) commute and \(W_B^{FP}=\exp(-i\theta\sum_pB_p)\). The resulting local R-IA lift is not invariant under a time-space exchange on an even cubic four-torus for any \(\beta\in\mathbb R,t>0\).

*Proof.* A face in plane \((i,j)\) with base \(y\) belongs to the translated tiling \(\mathcal C+v\) iff \(y_i-v_i\equiv y_j-v_j\pmod2\). Exactly two of the four specified \(v\)'s satisfy this. Cube operators are multiplication operators on the infinite-register target, so their exponents add. For the last assertion, compare the two densities after exchange with all links identity except one spatial link \(g\). It meets four spatial Wilson plaquettes and two temporal heat-kernel plaquettes; its exchanged temporal link meets six heat-kernel plaquettes. Equality of the continuous densities would imply \(e^{4\beta\operatorname{Tr}g}k_t(g)^2\) is proportional to \(k_t(g)^6\), hence \(k_t(g)\) is a Wilson weight. `GB1E.md` Theorem 7.1 excludes that equality even locally. □

The four tilings are permuted by translations and cube symmetries, so their commuting target product has those symmetries. At finite register, shared-link plaquette operators need not commute (`GB1.md` §4 and `LW1.md` GA1-P); the ordered product's covariance and exact full-sum form do not follow. **GB1-CF remains open** for an admissible finite-register update. The pass-1 four tests for FP are **C P P P**: alignment with the magnetic target is conditional; the text is finite; isotropy is not assumed; the stated ingredients have a reason. These are proposed author-side judgments, not an adoption or a proof of uniqueness among all possible constructions. In particular, “cell covariance forces all three shifts” is only an argument within this chosen four-tiling ansatz.

**ISO-FP (OPEN).** Find parameter families under FP and either reading whose volume-first action-density correlations have a nontrivial continuum limit invariant under \(D_cSO(4)D_c^{-1}\), \(c>0\), with a stated power rate. Finite-torus exchange invariance for R-SUM under FP is also open; Theorem 4.1 relied on the non-translation-invariant cube-face set and does not apply. The draft tried: (1) RO1, but its diagonal-mirror hypotheses are not supplied by axis reflection positivity; (2) tree-level matching and perturbative anisotropy renormalization, which give no nonperturbative convergence bound; (3) the Sussman–Alpoge Ward route, for which the required anisotropy decay and its applicability to these starts are unproved. These failures do not prove impossibility. The claim that every FP start has order-one anisotropy is not established: anisotropy depends on the parameters and definition used.

For \(\theta<0\), the draft's smooth-field FP matching gives \(\xi_{cl}^2=c_t/(2\lambda|\theta|)\) and \(g_{cl}^4=2/(c_t\lambda|\theta|)\), where \(t=\lambda\tau_E\), \(c_t\) is `GB1E.md`'s heat-kernel quadratic coefficient. If \(tc_t\to1\), then as \(\lambda\to0\), \(\xi_{cl}\sim(2\lambda^2|\theta|\tau_E)^{-1/2}\) and \(g_{cl}^2\to(2\tau_E/|\theta|)^{1/2}\). This is a classical dictionary, not a quantum restoration proof.

**T0-start^an[G] (OPEN request, not a theorem).** For \(G=SU(2)\), specify an anisotropic RG class \(\mathcal A_k^{an}(g,\xi)\) with \(\xi\) in a fixed compact positive interval. Ask for CT1–CT4 uniformly in lattice spacing, volume, start and \(\xi\); convergence of the \(\operatorname{tr}F^2\) sector, after a start-dependent finite positive time rescaling, to T0's theory up to scale; and T0-rate for those rescaled correlations. Proposed start symmetries are spatial translations and cubic symmetry, time translation and reflection, gauge invariance and coordinate link reflection positivity. Tests **P C P P**: the class and topology are unpinned; all requested conclusions remain proof obligations. The draft suggests four tasks:

- **Y-a:** prove anisotropic small-field, propagator, block and localization estimates uniformly in the chosen compact range.
- **Y-b:** control the anisotropy flow and justify any limiting speed and summable increments. The draft cites perturbative finite renormalization, not a nonperturbative proof.
- **Y-c:** prove rescaled O(4) restoration without assuming missing diagonal mirrors, or justify an applicable Ward route and its decay. The digest records `library/ro1.md` Theorem 9 as conditional on H-U, H-L, H-C and H-T, and `library/o4-two-point.md` as a narrower conditional two-point result; neither discharges the FP obligations.
- **Y-d:** admit the temporal heat-kernel weights or the exact semigroup with all needed uniform estimates. `GB1E.md` Theorem 3.2 supplies fixed-box time-blocked convergence of R-IA to R-SUM, not uniform RG admission or interchange of limits.

The D4 event set remains Y3's alternative, outside this proof. The draft proposes regrading the cube-face class's test 3 as F when pure-gauge inter-cube propagation is required, while retaining C for a bridge test law. That is a proposal only; it does not alter `GB1.md`.

## 7. Handoff and evidence limits

Under the torus interface with P8.1 coordinate link reflections, `GB1E.md` Theorems 3.1, 3.2 and 6.1 already establish finite-box lifts, gauge invariance and coordinate link reflection positivity. `GB1E.md` Theorem 7.2 already excludes local-lift exchange symmetry; Theorem 4.1 extends the exact-lift exclusion to all angles. Thus an action class that requires exchange invariance excludes both lifts on these tori. With a mirror interface requiring time-space diagonal invariance, that interface fails for these finite measures. For other action classes and possible RG extensions, the first failing step is not determined. Both readings share the cube factorization; no comparison here selects one.

The digest identifies earlier repository results, not new closures here: finite SU(3) Wilson-to-Hamiltonian convergence with cutoff estimate in `docs/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md`; spatial cubic symmetry allowing unequal time and space coefficients in `docs/SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`; and the conditional B4 kinetic-form result in `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`. The digest records these main-branch ledger results as unaudited. Their hypotheses do not identify either lift with T0's class. The YM digest records all-mirror Wilson RP in `library/lg1.md` Theorem 13 and conditional restoration in `library/ro1.md` Theorem 9; those branch files were not available as independently checked premises in this pass.

Pass 1 reports numerical checks of the heat-kernel product, \(N=4\) cube/flux counts (16 cubes, kernels 112 and 66), and FP multiplicities (192 plaquettes, each twice). The scratch files and outputs are absent in this session, so none was reproduced. The source's literature record credits Jacobi, Perron, Frobenius, Jentzsch, Creutz, Klassen, Karsch, Menotti and Onofri, and others; its bibliographic-only and snippet-only entries are explicitly unverified. The proofs above use no unverified literature claim. No independent referee has checked this distillation.
