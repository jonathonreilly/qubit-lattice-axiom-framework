---
claim_id: compact_detector_exhaustion_reduction_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Under the supplied direct compact-creator conditions and a unique gapped vacuum, full operator filtering gives the scalar detector source reduction; propagation convergence and a no-common-kernel condition imply full-GNS exhaustion. This theorem does not prove the no-common-kernel condition or physical realization."
upstream_dependencies:
  - compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
runner: scripts/compact_detector_exhaustion_reduction_2026_10_12.py
actual_current_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Full-GNS scattering exhaustion: the next conditional obligation

Status: conditional-support, bounded theorem and primary-source route assessment, 2026-10-12. A separate complete E1–E18 reconstruction found no required correction. The results are the detector/source reduction in §4 and the conditional exhaustion criterion in §5. This proof treats PC and ND as explicit additional conditions. The sibling theorem `COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md` now supplies PC for its stated admissible arrangements; ND remains open. No asymptotic-completeness premise or audit verdict is added, and no local-UHF no-go theorem is asserted.

The most useful route is to construct particle detectors from the existing compact creators, then prove that these detectors leave no nonzero finite-energy state undetected. The final coverage estimate is stronger than scattering existence, Fock isometry, or convergence of individual detector arrangements. A narrow energy window removes one apparent obstacle: the vacuum remainder needed by detector arguments can be obtained from the gap without requiring a globally isolated geometric Bloch band.

## 1. Exact inputs and target

S denotes the original external research collection. The [complete detector milestone packet](../.claude/science/physics-loops/toe-compact-detector-convergence-20261012/) preserves the complete frozen note, repository sources, author and separate review evidence. EVIDENCE_MAP.json records recovery paths and external primary URLs/hashes; full third-party papers and page extractions remain external. The in-branch [compact-creator theorem](COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md) contains the complete upstream proof and its reviewed unique-vacuum/gap clarification.

| Source | SHA-256 | Scope reused |
|---|---|---|
| `C4_N1_report.md` | `c284a41bfee8a1238643330ddd46f3a7c4f6f1a865509a9aaec5ab6f4238ad13` | H-loc/H-int/H-cov/H-gap and the conditional index reduction; H-AC is excluded as an input |
| `C4_B1_report.md` | `95044a142cf94ad397c5f7b2bdf806905d2f40bb166fb8d5920fb5daf54a7a0e` | Previously read bounded-sector scope only |
| `C4_M1_report.md` | `fb2d6b5f54fcff8680219dce5f903d6620e5f987d4f093462502dc3e600b1b2b` | Previously read scattering/shift bridge, with its supplied completeness premise |
| `COMPACT_PATCH_SCATTERING_COVARIANCE_PROBE.md` | `d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a` | Conditional direct creator properties and compact-packet Cook limits |
| Its independent review | `924b2fa9d6175bcbc213d164da6322d3fde0d769f06a5608d4aadc1644f974be` | Supported core S1–S4; no Fock or exhaustion conclusion |
| `COMPACT_PATCH_SCATTERING_EX_PUBLICATION_REPAIR.md` | `d4aac1e14a20e82be994bd4b8de966f0063affcbaa22a40a173b126f77fa3516` | Explicit unique vacuum and positive gap in EX |
| `COMPACT_PATCH_FOCK_ISOMETRY_PROBE.md` | `9bc3a309e8fc35978bcac0c360b8557fb6a3c4484cfc2034a277a94072369404` | Separate Fock review completed; the historical author freeze predates it. Its isometry conclusion is not an input here |

The exact candidate commit `0cc560e3935fa1ad7623592bf9974680c922d52d` was inspected for N1/B1/M1 identity only: all three reports match these frozen hashes. Shared checkout HEAD was observed at `773321aa8fdfccc05248682dfc96bf94215034a2`; no working-tree or Git changes were made. RV4/Y1/RZ science is outside this assessment.

Keep the microscopic implementation premises explicit. Besides geometric translations, the compact construction assumes actual strongly commuting microscopic flows of H and the current generators, selected isolated positive mass-Casimir components, and finite-order centre selection on those components. Formal Lie-algebra relations alone do not establish these hypotheses. Add
\[
\ker H=\mathbb C\Omega,\qquad
\operatorname{spec}H\subset\{0\}\cup[\gamma,\infty),\quad\gamma>0. \tag{E1}
\]
This full Hilbert-space gap is supplied by N1 H-gap; uniqueness only among translation-invariant states would not suffice. The Fock extension adds the same requirement. This probe uses its direct analytic prerequisites, not its isometry conclusion.

Fix outgoing scattering; the incoming version uses the opposite time direction. Let \(\mathcal H_{\rm sc}\) be the closed span of \(\Omega\) and all constructed finite products for the chosen collection of mass/centre components and compact charts. The collection must eventually include every channel needed for the intended conclusion; choosing a finite subset does not settle that obligation. Write \(P_{\rm sc}\) for its projection. Compact-construction time covariance makes this space reducing for H. The repaired criterion is
\[
\|(1-P_{\rm sc})\,\mathbf1_{[\gamma,E]}(H)\pi(A)\Omega\|=0
\quad\text{for every finite }E\text{ and local }A. \tag{EX}
\]
It is equivalent to \(P_{\rm sc}=1\): use local cyclicity, strong convergence of the energy cutoffs, and \(\Omega\in\mathcal H_{\rm sc}\). It is enough to prove \(\mathbf1_J(H)\mathcal H\subset\mathcal H_{\rm sc}\) for a countable disjoint partition of \([\gamma,\infty)\) into bounded Borel intervals of width less than \(\gamma/4\). No common rational centre on unconstructed channels is inferred from EX's formulation.

The premise graph is: direct compact creators + (E1) + the BDN finite-energy bound imply the reduction (E3)–(E14); adding the explicit (PC) condition gives positive detector limits with scattering range; adding the unproved (ND) on every J gives EX. The separately checked Fock theorem identifies the range with a Fock image but is unnecessary for these implications. A later full-algebra shift conclusion would still require the common finite centre order on every covered channel.

## 2. Primary literature and the compatibility boundary

**Bachmann–Dybalski–Naaijkens, [arXiv:1412.2970v2](https://arxiv.org/abs/1412.2970v2), Proposition 3.6, Lemma 3.9 and Theorems 3.10–3.11 (BDN).** These supply spectral transfer, almost locality and the finite-energy annihilation bound used below. Theorem 3.11 needs positive energy and compact energy-decreasing transfer with almost locality; it does not need the isolated geometric shell used later in their scattering construction. Its exact hypotheses were checked from the primary source, without using the Fock extension.

**Dybalski, [arXiv:1608.08750v1](https://arxiv.org/abs/1608.08750v1), Theorem 4.2 and Appendices A–B.** This is the closest lattice mechanism: compactness and almost locality control coincidence detectors on arbitrary bounded-energy vectors. Its stated framework uses an isolated geometric energy–momentum shell; its detector tuple has small transfer sets, a vacuum-only spectral remainder, and velocity cutoffs with disjoint convex hulls containing the relevant velocities. The limit has scattering range, and the ranges span the corresponding scattering subspace. That does not establish full-GNS exhaustion. Here the vacuum graph is isolated through (H,current momentum), while packets use geometric translations; the stated global-shell hypotheses are not supplied. Sections 4–5 below rebuild the needed preliminary reduction from direct properties. All 13 pages were read. A source precision issue is preserved: p.4 prints \((h-h)\cap\operatorname{Sp}U=\varnothing\), impossible with a nonempty h and vacuum; BDN Definition 4.1(3) gives \(\{0\}\). The p.4 image confirms this is in the source. No literal theorem with that impossible clause is imported.

**Dybalski–Gérard, [arXiv:1308.5187v1](https://arxiv.org/abs/1308.5187v1), Theorems 2.8–2.9, 4.1; Lemma 4.2; Proposition 5.3.** Their continuum Haag–Kastler setting has geometric spacetime covariance, microcausality and an isolated mass hyperboloid with a higher continuum threshold. The detector problem is reduced to an inhomogeneous many-particle equation and a phase-space propagation estimate. The resulting detected subspace equals the scattering subspace, with equality to the full Hilbert space left as a separate criterion. Microscopic current flow is not a continuum geometric translation net, so their full theorem cannot be applied by replacing one momentum symbol. The scalar evolution mechanism can be reconstructed on the lattice, as below. The indicated statements, hypotheses and the relevant proofs in §§4–5 and 7 were read.

**Kruse, [CMP 405:236 (2024)](https://doi.org/10.1007/s00220-024-05091-7), Theorem 1.1, Theorem 3.4, Corollary 1.2 and §§5.1,5.3–5.4.** The stated AQFT framework has one spinless isolated mass m and continuum above the 2m threshold. A single detector converges on the jointly absolutely continuous energy–momentum subspace when its annihilator leaves a one-particle remainder; Theorem 3.4 uses \((\Delta-\operatorname{Sp}B^*)\cap\operatorname{Sp}U\subset H_m\) uniformly. The spin-system extension invokes an isolated regular, pseudo-relativistic geometric shell. Joint absolute continuity, that remainder condition, and geometric-shell isolation do not follow from our compact vacuum graph. Section 5.1 proposes comparing energy density with canonical creation/annihilation detectors, but explicitly leaves that bridge unproved. N1 supplies bounded local energy density, not this detector approximation. The stated conditions and discussion were read; no Mourre theorem is imported. The cited 1986 ideal-detector construction was not obtained/read and supplies no premise here.

**Graf–Schenker, [Ann. IHP 67 (1997), 91–107](https://www.numdam.org/item/AIHPA_1997__67_1_91_0.pdf), Theorems 1.1 and 2.1.** This provides genuine lattice completeness for a fixed two-magnon problem, with bound-pair channels retained. Its reduction has a lattice Laplacian and a bounded self-adjoint interaction invariant along the diagonal and supported in finitely many transverse equivalence classes. Magnon number is conserved. N1 supplies neither such a fixed-number coordinate realization nor an all-channel decomposition. The scanned theorem statements and hypotheses were inspected as rendered pages; this is a useful comparison, not a theorem about the present interacting GNS representation.

These are mathematical imports or route comparators, not novel constructions attributed to this probe. The bounded search also checked newer primary leads; it does not establish an exhaustive literature survey or a general impossibility result.

## 3. Ranked routes and their actual missing estimates

| Rank | Route | Precise additional work | What it would still leave |
|---|---|---|---|
| 1 | Lattice coincidence detectors, adapting Dybalski's compactness argument | Prove the norm-Cauchy condition (PC) below for the direct compact-chart creator class, including mixed dispersions and operator momentum cutoffs. The reduction in §4 supplies the vacuum remainder and source estimate without global Bloch isolation. | Prove (ND): the limiting detectors have no common kernel on every finite-energy window. Convergence/range identification alone does not do this. |
| 2 | Low-energy single detectors and energy capture, motivated by Kruse | First establish the required joint spectral absolute continuity and one-particle remainder on a specified window, and adapt the geometric-shell argument. Then derive a nonzero response or a controlled comparison of the microscopic energy form with canonical detectors. | Other spectral components, higher-energy windows and composite/charged channels; a two-particle result cannot exhaust the GNS space. |
| 3 | Propagation estimates for the scalar equation (E11) | Prove a lattice version of the localized estimate \(\int_1^\infty\|(X/t-v(D))\mathsf h_t^wF_t\|^2dt/t<\infty\), with the companion free estimate, collision avoidance and the symbol correction used in DG §5. These are conditions to prove, not asserted consequences of a gap. | This is another way to establish (PC); it still needs (ND). |
| 4 | Fixed-particle/composite-channel Mourre or Enss analysis | Construct the microscopic coordinate-channel representation and prove positive-commutator/escape estimates away from every threshold, with bound clusters included. A fixed-two-particle theorem cannot supply that representation. | Uniform control across all relevant channels and energies, then identification with the original local GNS space. |

The single consequential coverage target is (ND). The most accessible preceding derivation is (PC), because the available compact creators already give all the elementary reductions below. N1 H-AC is never substituted for either estimate.

## 4. A reusable reduction proved from the direct creator properties

### 4.1 Conventions and further harmless filtering

Use the compact note's signs. Write \(\mathsf K=P/\beta\) for current momentum (not N1's boost operator denoted K),
\[
\alpha_t=\operatorname{Ad}e^{itH},\quad
R_y=e^{-iy\cdot\mathsf K},\quad T_x=e^{-ix\cdot Q},\quad
V_j=e^{ij\cdot\mathsf K}T_j.
\]
For centre phase \(e^{i\theta\cdot j}\), geometric momentum on a fixed lift obeys \(k=p+\theta+2\pi n\), and
\[
\Sigma_i(p)=\sqrt{M_i^2+\beta|p+\theta_i+2\pi n_i|^2},\qquad
v_i(p)=\nabla\Sigma_i(p). \tag{E2}
\]
All detectors and packets below use the geometric shifts \(\tau_x=\operatorname{Ad}T_x\). No continuous-current parameter is treated as a lattice position.

Let \(B_i\) be direct compact creators: almost local, norm smooth for time evolution with almost-local derivatives, temporal transfer in \(I_i=[\epsilon_i,L_i]\subset(0,\infty)\), and exact vacuum vector on the chosen graph. Shrink the compact patch and the original temporal cutoff if a narrower interval is required. For \(\phi_i\in C_c^\infty(O_i)\), define
\[
c_i(z)=(2\pi)^{-d}\int_{\mathbb T^d}e^{ipz}\phi_i(p)\,dp,
\qquad B_i^{\phi_i}=\sum_{z\in\mathbb Z^d}c_i(z)\tau_z(B_i). \tag{E3}
\]
Then \(B_i^{\phi_i}\Omega=\phi_i(Q)B_i\Omega\) and the **full operator** geometric momentum transfer is contained in \(\operatorname{supp}\phi_i\). The coefficients are rapidly decreasing. Splitting the sum into \(|z|\le r/2\) and its tail proves almost locality; time derivatives commute with this sum. Temporal transfer and the selected vacuum mass/centre are preserved. This is BDN Proposition 3.6 and Theorem 3.10 applied to geometric translations, and does not assert \(\operatorname{Sp}_{B_i}^{(H,Q)}\cap\operatorname{Sp}(H,Q)\) is an isolated shell. From now on rename the filtered creators \(B_i\).

Choose slightly larger compact chart neighbourhoods on which the velocity images have disjoint closures, and smoothly extend each \(\Sigma_i\) to a real function on the torus. Only its values near the creator's momentum transfer matter. This does not require different species to have different geometric momentum supports. For this lemma all n, charts and operator seminorms are fixed; no uniformity as patches shrink is claimed.

Set \(A_i=B_i^*\), \(A_i(t,x)=\alpha_t\tau_x(A_i)\). The annihilators have compact negative temporal transfer. For each R, BDN Theorem 3.11 supplies a finite constant
\[
\sum_x\|A_i(x)\mathbf1_{[0,R]}(H)\Psi\|^2
 \le b_i(R)\|\Psi\|^2. \tag{E4}
\]
The checked hypotheses are positive energy, compact negative transfer and almost locality; geometric shell isolation and Fock isometry do not enter this theorem. Put \(M_R=\prod_i b_i(R)^{1/2}\). Repeatedly applying (E4) is legitimate because each annihilator lowers energy. It gives
\[
\|a\mathbf1_{[0,R]}(H)\|\le M_R,\qquad
(a\Psi)(x_1,\ldots,x_n)=A_1(x_1)\cdots A_n(x_n)\Psi. \tag{E5}
\]
These constants may depend on the fixed creators and energy cutoff. This use of a primary theorem avoids relying on the Fock note's quantitative kernel induction.

### 4.2 Vacuum remainder and detector factorization

Let J be a bounded energy interval and require
\[
\bigl(J-I_1-\cdots-I_n\bigr)\cap\operatorname{spec}H\subset\{0\}.
\quad\text{A sufficient condition is }J-\sum_i I_i\subset(-\gamma,\gamma). \tag{E6}
\]
For example, if \(I_i\subset[e_i-\delta_i,e_i+\delta_i]\) and \(J\subset[\sum e_i-\delta_0,\sum e_i+\delta_0]\), it suffices that \(\delta_0+\sum_i\delta_i<\gamma\). Transfer addition, unaffected by geometric shifts, gives exactly
\[
A_1(t,x_1)\cdots A_n(t,x_n)P_J
=|\Omega\rangle\langle\Omega|A_1(t,x_1)\cdots A_n(t,x_n)P_J,
\quad P_J=\mathbf1_J(H). \tag{E7}
\]
This is the useful replacement for a stronger joint geometric spectral-remainder hypothesis. It does not prove that such tuples cover every state in J.

For \(h_i\in C_c^\infty(\mathbb R^d)\), \(h_i\ge0\), with pairwise separated supports, let
\[
C_i(t)=\sum_x h_i(x/t)A_i(t,x)^*A_i(t,x),\qquad
\mathsf h_t(\mathbf x)=\prod_i h_i(x_i/t).
\]
For the preferred Dybalski compactness route, also choose their convex support hulls disjoint and containing the corresponding creator velocity supports. The preliminary factorization itself only needs separation.
Let \(a_t\) be (E5) with time-translated operators. Almost-local equal-time commutators are independent of the common evolution time, since \(\alpha_t\) pulls out of each commutator. Reordering the finite sums uses at most a fixed number of swaps and yields, for every N and \(t\ge1\),
\[
\left\|\left(C_1(t)\cdots C_n(t)-a_t^*(1\otimes\mathsf h_t)a_t\right)P_J\right\|
 \le C_Nt^{nd-N}. \tag{E8}
\]
Indeed there are \(O(t^{nd})\) position tuples; every swapped pair is separated by \(\delta t\), while all remaining factors have fixed operator norm. Taking N arbitrarily large gives rapid decay. No norm estimate on an exponentially growing time-dependent localization radius is used.

Define the scalar amplitude and the creation map
\[
F_t(\Psi)(\mathbf x)=\langle\Omega,A_1(t,x_1)\cdots A_n(t,x_n)\Psi\rangle,
\quad J_t f=a_t^*(\Omega\otimes f).
\]
The second map is first defined on finitely supported f. Its vectors have energy at most \(L=\sum_i L_i\); (E5) at L therefore extends it to a bounded map on \(\ell^2(\mathbb Z^{dn})\), with \(\|J_t\|\le M_L\). Equations (E7)–(E8) give
\[
C_1(t)\cdots C_n(t)\Psi=J_t\mathsf h_tF_t(\Psi)+O(t^{-N})\|\Psi\|,
\quad\Psi\in P_J\mathcal H. \tag{E9}
\]
Thus the exactly positive compressed approximants
\[
Q(t)=P_JJ_t\mathsf h_tJ_t^*P_J \tag{E10}
\]
approximate \(P_JC_1(t)\cdots C_n(t)P_J\) rapidly in norm. They obey \(0\le Q(t)\le B_JP_J\), with the fixed explicit-in-(E4) bound \(B_J=M_L^2\prod_i\|h_i\|_\infty\).

### 4.3 Scalar evolution and its collision source

Use the unitary Fourier transform with kernel \(e^{-ipx}\), and let \(\widetilde\Sigma(D)=\sum_i\Sigma_i(D_{x_i})\). On \(P_J\mathcal H\subset\mathbf1_{[0,R]}(H)\mathcal H\),
\[
F_t=(\langle\Omega|\otimes1)a e^{-itH}\Psi,
\quad \sup_t\|F_t\|_2\le M_R\|\Psi\|,
\quad\|\partial_tF_t\|_2\le R M_R\|\Psi\|.
\]
In particular differentiation is in \(\ell^2\), not just pointwise. The full operator filter in (E3) also restricts each partial Fourier support to its compact chart.

Let \(\delta A_i=\left.\partial_t\alpha_t(A_i)\right|_{t=0}\). If \(\kappa_i\) is the rapidly decreasing convolution kernel of \(\Sigma_i(D)\), put
\[
A_i^\Sigma=\sum_z\kappa_i(z)\tau_{-z}(A_i),\qquad
D_i=\delta A_i+iA_i^\Sigma.
\]
These are almost local and energy decreasing. The exact vacuum graph gives, for every \(\Phi\),
\(\langle\Omega,\delta A_i(t,x)\Phi\rangle=-i\Sigma_i(D_x)\langle\Omega,A_i(t,x)\Phi\rangle\), so \(\langle\Omega,D_i(t,x)\Phi\rangle=0\). The momentum-centre shift in (E2) is included in \(\Sigma_i\).

Differentiating the ordered product and commuting each \(D_i\) to its far left gives
\[
\partial_tF_t=-i\widetilde\Sigma(D)F_t+\mathcal R_t, \tag{E11}
\]
\[
\mathcal R_t(\mathbf x)=\sum_{i=2}^n\sum_{j<i}
\langle\Omega,A_1\cdots A_{j-1}[A_j,D_i]
A_{j+1}\cdots A_{i-1}A_{i+1}\cdots A_n\Psi\rangle. \tag{E12}
\]
Each operator carries its own \((t,x_k)\); \(D_i\) carries \((t,x_i)\). This formula includes both the time derivative and the packet-dispersion derivative. Equal-time almost locality proves
\[
|\mathcal R_t(\mathbf x)|\le C_N\|\Psi\|\sum_{i>j}\langle x_i-x_j\rangle^{-N},
\quad
\sup_t\|\mathcal R_t\|_2\le(R+\|\widetilde\Sigma\|_\infty)M_R\|\Psi\|. \tag{E13}
\]
For a smooth compact \(\chi(\mathbf x)\) supported a positive distance from every collision plane \(x_i=x_j\), counting lattice points gives
\[
\|\chi(X/t)\mathcal R_t\|_2\le C_{\chi,N}\,t^{nd/2-N}\|\Psi\|. \tag{E14}
\]
This is the promised nontrivial reusable lemma. It uses mixed masses and centres through their separate smooth dispersions, and uses no claim that different species automatically have different velocities. It proves rapid decay off collisions, not decay in all relative directions when some particles remain together.

### 4.4 The remaining norm-Cauchy estimate

Choose real \(g_i\in C_c^\infty(O_i)\), equal to one on the full creator momentum support, within the mutually separated velocity charts. Let \(g(D)=\prod_i g_i(D_{x_i})\). The concrete target is
\[
u_t(\Psi)=e^{it\widetilde\Sigma(D)}g(D)\mathsf h_tF_t(\Psi),
\qquad
\lim_{T\to\infty}\sup_{t,s\ge T}\|u_t(\Psi)-u_s(\Psi)\|_2=0
\quad(\Psi\in P_J\mathcal H). \tag{PC}
\]
It is enough to prove this on a dense core, using the uniform bounds above. If (PC) holds, then (E10) converges strongly and its limit has range in \(P_J\mathcal H_{\rm sc}\). Here is the full implication: \(S_t=J_te^{-it\widetilde\Sigma(D)}\) is uniformly bounded and \(S_t=S_tg(D)\). On products of smooth functions inside the respective charts it is a compact-creator scattering approximant (with reversed creator order). The linear span of such products is dense in the tensor product of the \(L^2(O_i)\) momentum spaces, and their velocities are separated. On its orthogonal complement \(S_t\) vanishes, by the full operator momentum cutoffs. The independently checked compact Cook construction therefore gives a strong limit \(S\) on all of \(\ell^2\), with range in \(\mathcal H_{\rm sc}\). Equations (E9)–(E10) give \(Q(t)\Psi=P_JS_tu_t(\Psi)\), hence \(Q(t)\Psi\to P_JSu_+(\Psi)\). Positivity and the bound in (E10) pass to the limit. Fock isometry or asymptotic completeness is not needed for this implication.

There is a precise failed shortcut. From (E11),
\[
\partial_tu_t=e^{it\widetilde\Sigma}g
\{\partial_t\mathsf h_t+i[\widetilde\Sigma,\mathsf h_t]\}F_t
+e^{it\widetilde\Sigma}g\mathsf h_t\mathcal R_t. \tag{E15}
\]
The last term is rapidly decreasing by (E14). A first-order Taylor expansion of the rapidly decreasing convolution kernel of each \(\Sigma_i(D)\) gives
\[
\partial_t\mathsf h_t+i[\widetilde\Sigma(D),\mathsf h_t]
=t^{-1}(\nabla\mathsf h)(X/t)\cdot\{v(D)-X/t\}+O(t^{-2}), \tag{E16}
\]
with the multiplication operator on the left of \(v(D)\), and \(v=(v_1,\ldots,v_n)\). The kernel remainder is bounded by a constant times \(t^{-2}\sum_z|z|^2|\kappa(z)|\). Uniform \(\ell^2\) boundedness of \(F_t\) only yields \(O(1/t)\), which is not integrable. Thus the compact-packet Cook estimate does **not** by itself prove (PC). The compactness or propagation mechanisms in §3 address exactly this term.

## 5. An exact conditional exhaustion criterion

For a fixed J, choose a countable family of arrangements \(\alpha\) satisfying §4, and suppose (PC) has been proved for each. Denote their positive limits by \(Q_\alpha\) and bounds by \(B_\alpha\). This step is a named obligation, not a conclusion of the present note. Define on \(P_J\mathcal H\)
\[
K_J=\sum_{\alpha=1}^\infty\frac{2^{-\alpha}}{1+B_\alpha}Q_\alpha,
\qquad 0\le K_J\le1. \tag{E17}
\]
The sum converges in norm. Positivity gives \(\ker K_J=\bigcap_\alpha\ker Q_\alpha\). Since each \(Q_\alpha\) is self-adjoint and has scattering range, it vanishes on \(\mathcal H_{\rm sc}^{\perp}\). Consequently the following additional condition is sufficient for exhaustion on J:
\[
\ker K_J=\{0\}\quad\text{within }P_J\mathcal H. \tag{ND}
\]
Indeed \(\overline{\operatorname{Ran}K_J}=(\ker K_J)^\perp=P_J\mathcal H\), whereas that range is contained in the closed space \(P_J\mathcal H_{\rm sc}\). This proves \(P_J\mathcal H\subset\mathcal H_{\rm sc}\). It does not presume a detector range is already dense.

There is a version involving only the finite-time positive operators and an explicitly ordered limit. Put
\[
K_{J,m}(t)=\sum_{\alpha=1}^m\frac{2^{-\alpha}}{1+B_\alpha}Q_\alpha(t).
\]
Under (PC), (ND) is equivalent to
\[
\lim_{\eta\downarrow0}\lim_{m\to\infty}\lim_{t\to\infty}
\|\eta(K_{J,m}(t)+\eta)^{-1}P_J\pi(A)\Omega\|=0
\quad\text{for every local }A. \tag{E18}
\]
Proof: bounded strong convergence of the positive operators gives strong convergence of their resolvents for fixed \(m,\eta>0\). The norm tail obeys \(\|K_J-K_{J,m}\|\le2^{-m}\), so the resolvent identity bounds the next error by \(2^{-m}\|\Psi\|/\eta\). Finally \(\eta(K_J+\eta)^{-1}\) converges strongly to \(\mathbf1_{\{0\}}(K_J)\). The local vectors \(P_J\pi(A)\Omega\) are dense in \(P_J\mathcal H\). This proves the equivalence and fixes the order of limits. It supplies a mathematically checkable target; it is not a proof that the target vanishes.

Combining (PC), (E18) on every partition interval J, local cyclicity and (E1) proves EX. This implication is independent of the Fock-isometry identification. Conditional on that identification, its meaning is surjectivity of the corresponding wave operator, rather than merely an isometry into the GNS space.

## 6. The strongest unresolved estimate and a discriminating next derivation

The hardest missing statement is that the microscopic energy cannot remain in states invisible to all admissible creator detectors. Neither local cyclicity nor \(H\ge\gamma\) on \(\Omega^\perp\) proves (ND): the detector class uses selected vacuum one-particle graphs, whereas cyclicity uses all local operators. The compact/Fock arguments establish particle-state control and do not estimate the complement.

A useful concrete test is to derive an energy-capture comparison on a fixed small J directly from the supplied bounded local density. A sufficient, deliberately stronger target is a positive form \(D_J\), assembled from the \(Q_\alpha\) so that every common undetected vector has zero \(D_J\) form, for which
\[
\langle\Psi,H\Psi\rangle\le C_J\langle\Psi,D_J\Psi\rangle
\quad(\Psi\in P_J\mathcal H), \tag{EC}
\]
with all sums, energy restrictions and time limits controlled. Then any common undetected vector has zero energy and hence vanishes. A uniform inequality such as (EC) can be stronger than necessary, especially with infinitely many channels; the exact target remains the vectorwise condition (E18). No finite list of particle species or uniform detector-frame constant is supplied by N1.

For the next bounded attack, fix one specified energy interval and a finite set of selected charts. First attempt (PC) using Dybalski's proof with the direct graph/filter properties verified here; track both parts of (E15), mixed dispersions, convex velocity neighbourhoods, and the momentum cutoff after multiplication by \(\mathsf h_t\). Then ask whether the microscopic energy form on that interval is approximable by the resulting detector forms with an error smaller than its positive gap. Local terms need not be positive or annihilate the interacting vacuum; replacing them by square roots or summing vacuum-subtracted terms is not justified without a form/domain argument. Failure of that approximation should be preserved as a specific failed inequality or residual channel, not converted into a general no-go.

The known short routes do not close this step: N1's current locality does not supply continuum microcausality; a positive-energy Poincaré representation does not eliminate singular-continuous mass spectrum; the gap does not select all isolated particle masses; and proving detector response on scattering states says nothing about an undetected orthogonal complement. This note constructs no local-UHF countermodel satisfying all N1 premises. The abstract addition of a spectator Hilbert space would not provide one.

## 7. Checks, preserved failures and evidence limits

One new deterministic author check ran once with a declared 60-second timeout, exit 0, in about 0.62 seconds. Its script, complete five-record stdout, empty stderr and execution metadata are in `scattering_exhaustion_next/`. It did not rerun or mirror a compact/Fock author runner.

- Free-word expansion verifies (E12)'s ordered commutator identity for n=1,…,8.
- An exact four-site periodic XY calculation verifies 84 scalar source equations for n=1,2,3. Forty have a nonzero collision source; reversing the free-evolution sign fails in 80 cases. This is a finite local-algebra control of the formula, not a scattering or N1 model computation.
- In the actual on-site qubit UHF model \(H=\sum_x n_x\), lowering two occupied sites in a three-spin excitation leaves a one-spin excitation. Thus removing (E6) invalidates the vacuum remainder. The model has a product vacuum and gap but does not satisfy N1's Poincaré closure; this is only a counterexample to the weakened remainder claim.
- A two-dimensional positive-matrix control shows the time and \(\eta\) limits in (E18) cannot be merged arbitrarily; scalar exact controls check the \(2^{-m}/\eta\) truncation scaling.

The source-derivative, spectral-transfer, Hilbert-space and resolvent arguments require the written proofs. Finite checks cannot establish (PC), (ND), (EC), an infinite-volume scattering theorem, or independent review. Source extraction failures (`pdftotext` unavailable; Swift blocked by the existing Xcode license state) were bypassed using installed PDF libraries without accepting a license or changing the machine configuration. Raw texts, rendered source pages and full relevant logs are retained. Editable prompt files changed: none.

The result is therefore a source-bound conditional route with one completed preliminary lemma and an exact terminal estimate. Full-GNS exhaustion remains a separate unproved obligation here.

The separate review report has SHA256 `8c9f7bb60724982ce7580a8b5688d8b61572ea008d92305f057d3f9b7a4e735d`; its complete 337-line reconstruction was frozen before new author controls. Full evidence roles, original reading limits, operational failures and exact source bindings are preserved in the milestone packet. The [finite reduction control](../scripts/compact_detector_exhaustion_reduction_2026_10_12.py) retains the complete original helper. Its five records and distinct independent finite controls are not continuum proofs. Root is a contributor, not the separate reviewer. PUBLICATION_EDITS.json and reconstruct.py recover the whole source and control. DELIVERY_CHECKS.md states the scoped publication verification; no Lean certificate or retained status is claimed.
