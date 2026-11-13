lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-11T08:27Z

# Mass-gap skeleton (queue row 662, `gap-skeleton`)

`library/prior/gap-lit-2.md` is NOT at the pinned commit 0de407dd4. Every literature item below is marked 'not read', except the abstracts and the lines of Y that this session opened itself; those are marked with what was read.

Provenance: Claude Fable 5.2, high effort, Mac mini worker, checkout 0de407dd4, 2026-11-10. This is a direction document. It proves nothing and claims nothing. It is not checked by another model. No numerics were run. Short arguments below are marked "sketch"; a sketch is a proposal for a proof item, not a result.

Credit. The existence theorem, its hypotheses and every quoted line of Y are the text of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The renormalization group behind it is Tadeusz Bałaban's. The digests `library/prior/gap-prior.md` and `library/prior/gap-lit.md` are Codex readings (rows 655, 656). The tree of PR #10149 and the file `parts/physical-gap.md` are other lanes of this repository.

## 0. Repo search and sources read

Repo search. `library/open-core.md`, `library/open-registry.md`, `library/l17c.md` and the FINISH rows were searched for "mass gap", "spectral gap", "transfer operator", "small volume". Hits: FINISH rows 650, 655, 656, 661, 662 only. No open lemma of this lane covers a gap statement. This file attacks no open lemma.

Read in full for this file:

| Source | What | Where |
|---|---|---|
| Y | `YM4_1400.tex` at commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`, 136,637 lines, sha256 `222ef1bd…549f178`, fetched to this session's scratch folder | lines 154–291, 363–571, 1633–1909, 2355–2431, 2792–3021, 84296–84333, 86060–86105, 95984–95992, 97935–98053, 102540–102727, 119150–119237, 122700–122959, and the short passages 2021–2027, 6108–6113, 6614–6619, 117525–117541, 123133–123139, 125587–125593, 126116–126127 |
| `library/prior/gap-prior.md` | repository prior work, seven branches | all |
| `library/prior/gap-lit.md` | literature digest of row 656 | all |
| `library/assembly-status.md`, head of `library/t0-tree.md` | what this lane holds of T0 | all; first 40 lines |
| PR #10149 `PROOF_TREE.md` at `ec53007a8` | finite-depth response lane | all 254 lines |
| `parts/physical-gap.md` at `89faef229` (`ym/crossover-reduction`) | soft-kernel gap obligation | all 29 lines |
| arXiv abstracts (API records only, no paper text) | 0707.2179, 0711.4930, 1803.01950, 2006.16229, 2202.10375, 2204.12737, hep-ph/0008206 | abstract |

Not read: the proofs in Y behind the quoted statements; CA-I, CA-II, CA-III; every paper named below beyond its abstract.

Notation. "Y n" is line n of Y. Units, groups and symbols are Y's: $G=\mathrm{SU}(2)$, $a_K=L^{-K}$, $T_\ell=(\mathbb R/\ell\mathbb Z)^4$, $\mathcal O(f)=\sum_p f(x(p))a_p(U)$, first-passage datum $(K,\beta)$ at reference coupling $g$ (Y 1640–1670).

## 1. The object and the targets

### 1.1 (T0), what the existence theorem gives

**It is conditional.** Y 157–160: "Assume the uniform renormalization and short-distance estimates stated below. For sufficiently small reference coupling, the correlations of $\operatorname{tr}(F^2)$ in four-dimensional Wilson $\operatorname{SU}(2)$ theory have nontrivial volume-first subsequential continuum limits." Y 161–163: "In every canonical component, the Schwinger functions satisfy the Osterwalder--Schrader axioms and reconstruct a local Hermitian scalar Wightman theory with positive energy and a unique vacuum." Our lane: "**T0 remains open.** A frozen implication is not an established actual-construction input." (`library/t0-tree.md`, line 9).

**Observables.** Only the centred, smeared $\operatorname{tr}(F^2)$: $\mathcal O(f)=\sum_pf(x(p))a_p(U)$ with $a_p=1-\frac12\operatorname{Re}\operatorname{tr}U_p$ (Y 1647–1653). Tests are separated tuples, then Schwartz functions flat on the diagonals (Y 172–174). Y 174–175: "The reconstructed field generates the scalar sector associated with this observable." Y 117539–117541: "The assertion concerns this scalar cyclic sector. Gauge-theory existence, full observable identification and a positive mass gap require separate arguments."

**Schwinger functions.** $S^T_{n;K,\ell,\beta}(f_1,\dots,f_n)=\langle\mathcal O(f_1);\dots;\mathcal O(f_n)\rangle_{K,\ell,\beta}$, $n\ge2$, under Wilson's measure $\mu_{K,\ell,\beta}$ on $\Lambda_{K,\ell}=a_K\mathbb Z^4/\ell\mathbb Z^4$ (Y 1649–1653). The positive functional is the centred $\sigma_S=\sum_{\pi}\prod_{J\in\pi}S_{|J|}$ (Y 1709).

**Trajectory of the coupling and unit of length.** The run $x_0=\beta$, $x_k=x_{k-1}-b_k$ defines $K(\beta,g)=\min\{k: x_k(\beta)\le g^{-2}+B_\sharp\}$. Y 1663: "As the unit of length we take the scale at which the flow reaches, for the first time, the reference window $g^{-2}\le x\le g^{-2}+B_\sharp$ belonging to $g$". Y 1755: "$\beta/\log(1/a_K)\to\tfrac{11N^2}{12\pi^2}$ uniformly on $\mathcal{W}_K(g)$." So length 1 is the scale where the running coupling is the small number $g$. The renormalization steps of T0 run from spacing $a_K$ up to length 1 and stop there.

**Volume.** T0 lives in both places.

- Fixed torus $T_\ell$, cubic, with $\ell\in\mathfrak L(g)=\{2L^m\ge\ell_\star(g)\}$ (Y 1640–1646). The floor is $\ell_\star(g)=2L^{11}MR(g^{-2}+B_\sharp)$ (Y 84323–84326). Limits exist along subsequences (Y 1755 (a)(ii)), along the whole sequence at tuned couplings ((a)(i)), and "On each torus, the renormalised coupling by itself determines the limit theory" (Y 1836). The torus bound carries a volume factor: $|S^T_n|\le C_n(\mathsf d)e^{nc_V\ell^4}\prod_i\|f_i\|_\sharp$ (Y 1780).
- $\mathbb R^4$, volume first. Y 1690: "each $\nu_j\in\mathcal{G}^{\mathrm{tor}}_{K_j,\beta_j}$ is a limit point of the periodically extended torus measures as $\ell\to\infty$, with spacing and coupling held fixed. Thus the volume is removed first and the spacing only afterwards." Bounds uniform in the volume: (c)(2), Y 1781–1785, also "for $S^T_n[\nu]$, where $\nu$ is an arbitrary periodic Gibbs state".

**Axioms.** For every continuum limit: $W_4$ and translation invariance, reflection positivity at coordinate mirrors, symmetry, regularity (Y 1757–1761). On $\mathbb R^4$: growth, and a Hilbert space $\mathcal H(S)$ with $\mathcal T_t=e^{-tH}$, $H\ge0$, $H\Omega=0$ (Y 1762–1773). For a volume-first limit (Theorem "Canonical components", Y 1884–1909): $H\ge|P_j|$, $\mathrm O(4)$ invariance, a canonical decomposition $\sigma_S=\int_{\mathsf X}\sigma_\xi\,\lambda(d\xi)$ with $\ker H\cong L^2(\mathsf X,\lambda)$, and for each component $\sigma_\xi$ a unique vacuum, the forward cone, all Osterwalder–Schrader axioms and a Wightman theory. The Hamiltonian is stated on $\mathbb R^4$ only. On a torus Y states no Hamiltonian.

**Clustering.** Polynomial, per component. Y 1900–1907: $|\sigma_\xi(X\cdot\tau_vY)-\sigma_\xi(X)\,\sigma_\xi(Y)|\le C(X,Y)\,|v|^{-2}$ for $|v|\ge r(X,Y)$, "where $C(X,Y)$ and $r(X,Y)$ are the same for all $\xi$ and for all volume-first limits at $g$." Its source is the lattice plateau law, Y 2884–2893: for every translation-invariant Wilson Gibbs state $\nu$, $|\nu(\overline A\,\tau_yB)-\operatorname{Pl}_\nu(A,B)|\le C[(r/n)^2+(r/n)^3]\mathcal N_{\nu,r}(A)^{1/2}\mathcal N_{\nu,r}(B)^{1/2}$. Y 125589–125591: "The estimate in this section is a consequence of translation invariance and reflection positivity in coordinate and diagonal directions. No infrared bound, mass gap, or differentiability of a pressure is assumed." The bound depends on $r/n$ only. It contains no length, so it cannot give a rate.

**What Y says about a gap.** Y 556–563: "A polynomial cluster estimate likewise gives no positive mass gap. In a Hilbert space with a nonnegative self-adjoint $H$, a connected time correlation has the spectral form $\langle v,e^{-tH}v\rangle=\int_0^\infty e^{-tE}\,d\mu_v(E)$ for a vector orthogonal to the vacuum. If $d\mu_v(E)=E e^{-E}\,dE$, the integral is $(1+t)^{-2}$. It decays, yet its spectral measure meets every interval $(0,\varepsilon)$." (This is the example that the digest cites at outline lines 588–599.) Y 122956–122959: "A positive spectral gap requires an estimate that excludes spectral support in an entire interval above the vacuum. That question remains separate from the existence and reconstruction of the scalar sector described here." Y 126124–126127: "No spectral gap above the invariant subspace has been proved: the filter weight vanishes linearly near zero energy, and removing it is exactly what produces the inverse-square term." Y 122841–122843: the cluster limit "does not preserve a numerical decay rate on arbitrary vectors". The other occurrences of "gap" in Y (2025, 6111, 6618, 123137) are gaps of constrained fluctuation operators; each passage says that it is not a physical mass gap.

### 1.2 (G-inf), the gap in infinite volume

Let $\sigma=\sigma_\xi$ be a canonical component of a volume-first limit at $g$, with Hilbert space $\mathcal H(\sigma)$, vacuum $\Omega$ and Hamiltonian $H$ (Y 1899). Let $\mathfrak P_+$ be the complex span of products of separated tuples supported in $\{x_4>0\}$.

**(G-inf-D), decay.** There is $m>0$ such that for all $X,Y$ (finite products of separated tuples) there are $C(X,Y)$, $r(X,Y)$ with
$$|\sigma(X\cdot\tau_vY)-\sigma(X)\sigma(Y)|\le C(X,Y)\,e^{-m|v|}\qquad(|v|\ge r(X,Y)).$$

**(G-inf-S), spectrum.** $\ker H=\mathbb C\Omega$ and $\operatorname{spec}(H)\subset\{0\}\cup[m,\infty)$ on $\mathcal H(\sigma)$.

**(G-inf-T), time decay on reflected pairs.** For all $F\in\mathfrak P_+$ there is $C_F$ with $\langle[F],e^{-tH}[F]\rangle-|\langle\Omega,[F]\rangle|^2\le C_Fe^{-mt}$ for $t\ge0$.

The strong form asks this for every component of every volume-first limit at $g$. The weak form asks it for one reflection-positive continuum limit of T0's lattice measures on $\mathbb R^4$ that satisfies the axioms of 1.1.

**Which direction needs which axiom (sketch).**

- (T) $\Rightarrow$ (S). Needs: reflection positivity at the time mirror and the self-adjoint semigroup $e^{-tH}$ (Y 1759, 1770). Nothing else. Let $\psi=[F]-\langle\Omega,[F]\rangle\Omega$ and let $\mu_\psi$ be its spectral measure. Then $\mu_\psi([0,m'))\,e^{-tm'}\le\int e^{-tE}d\mu_\psi\le C_Fe^{-mt}$, so $\mu_\psi([0,m'))=0$ for every $m'<m$. The vectors $\psi$ are dense in $\Omega^\perp$. So the spectral projection of $[0,m)$ vanishes on $\Omega^\perp$. This direction also proves that the vacuum is unique. It uses no clustering hypothesis, no $\mathrm O(4)$ and no growth bound. The constant $C_F$ may be any finite number.
- (S) $\Rightarrow$ (T), with $C_F=\|[F]\|^2$: the spectral theorem.
- (S) $\Rightarrow$ (D) in the time direction: the same, since $\sigma(\theta\overline F\cdot\tau_{te_4}G)=\langle[F],e^{-tH}[G]\rangle$.
- (S) $\Rightarrow$ (D) in every direction, at the full rate $m$: needs $\mathrm O(4)$ invariance (Y 1894), to turn $v$ into the time direction, and the per-ball moment bound (c)(2) (Y 1781), to bound $\|[F]\|$ uniformly over the rotations. With $W_4$ and the commuting spatial translations only (Y 1758, 1771) the same argument gives $e^{-m|v|_\infty}$, so the rate $m/2$ in $|v|$.
- (D) $\Rightarrow$ (T): restrict to $v=te_4$ and reflected pairs, and use sesquilinearity.

So the three forms are equivalent for T0's components. The uniqueness of the vacuum is part of (S) and a consequence of (T). It is not needed as a hypothesis.

**What polynomial clustering gives.** Nothing towards (S): Y 556–563 above.

### 1.3 (G-ell), the gap at a fixed spatial side

T0 has no object with a finite spatial side and an infinite time. The object must be built.

**Lattice object.** Fix $\ell\in\mathfrak L(g)$ and a first-passage datum $(K,\beta)$. Let $\Lambda^{(3)}=(a_K\mathbb Z/\ell\mathbb Z)^3$, and let $\mathfrak H_{K,\ell}$ be the gauge-invariant functions in $L^2(G^{\text{bonds of }\Lambda^{(3)}},\text{Haar})$. The one-step transfer operator is $\mathsf T=W^{1/2}\,\mathsf C\,\mathsf P\,W^{1/2}$: $W$ multiplies by $\exp(-\beta\sum_{p\subset\Lambda^{(3)}}a_p)$, $\mathsf C$ convolves every bond with $c(u)=e^{-\beta(1-\operatorname{tr}(u)/2)}$, $\mathsf P$ is the gauge projection. Then $Z_{\ell^3\times na_K}=\operatorname{Tr}\mathsf T^n$. Y 102625–102634 states what is needed: "the Wilson transfer factor is the product of the gauge-invariant projection and the convolution with the product of the one-bond class functions … These operators commute. … Hence the crossing factor is positive … the convolution is trace class"; the character coefficients of $c$ are nonnegative (Y 102629–102631). So $\mathsf T\ge0$ is self-adjoint and trace class. Its kernel on gauge orbits is continuous and strictly positive, because $c>0$. By the theorem of Jentzsch (not read) the top eigenvalue $\lambda_0$ is simple. Put $E_i=-a_K^{-1}\log\lambda_i$.

**Sector.** Let $\Omega_K$ be the top eigenvector and let $\mathfrak H^{\rm cyc}_{K,\ell}$ be the closed span of the vectors $[F]$, $F$ a product of fields $\mathcal O(f_i)$ with separated supports in $\{x_4>0\}$, in the ground-state process of $\mathsf T$. A sector is needed, and it is not an assumption: multiplying by $-1$ every spatial bond that crosses a plane $\{x_i=c\}$ preserves all plaquettes and Haar measure, commutes with $\mathsf T$, fixes every $\mathcal O(f)$, and changes the sign of a spatial loop that winds once in direction $i$. So $\mathfrak H_{K,\ell}$ splits into eight sectors of this $\mathbb Z_2^3$, and $\mathfrak H^{\rm cyc}$ lies in the invariant one. The gap in the other sectors is a different number (the electric-flux energies; literature not read) and T0's observables do not see it.

**(G-ell), lattice form.** There are $m_\ell>0$ and $K_0$ such that for every first-passage datum with $K\ge K_0$: $\operatorname{spec}\big((H_{K,\ell}-E_0)|_{\mathfrak H^{\rm cyc}}\big)\subset\{0\}\cup[m_\ell,\infty)$. Equivalent decay form: $\mu(\theta\overline F\cdot\tau_tF)-|\mu(F)|^2\le\mu(\theta\overline F\cdot F)\,e^{-m_\ell t}$ for all such $F$, in the infinite-time measure $\mu=\mu^{\infty}_{K,\ell,\beta}$. The number $m_\ell$ is in Y's unit of length.

**(G-ell), continuum form.** The connected functions of $\mu^\infty_{K,\ell,\beta}$ have limits on separated tuples of $T_\ell^3\times\mathbb R$ as $K\to\infty$ (node A1 below). For every such limit, with Hamiltonian $H_\ell$: $\ker H_\ell=\mathbb C\Omega$ and $\operatorname{spec}(H_\ell)\subset\{0\}\cup[m_\ell,\infty)$.

The lattice form implies the continuum form: the inequality passes to the limit, because $\mu_K(\theta\overline F\cdot F)$ converges. The converse is open. A lattice eigenvector with $E_1(K)\to0$ that has no uniformly bounded polynomial representative leaves no trace in the limit.

**At fixed cutoff the gap is positive and that says nothing.** Positivity of $E_1-E_0$ at fixed $K$ follows from the strictly positive kernel. The content of (G-ell) is the uniformity in $K$.

### 1.4 What joins (G-ell) and (G-inf)

Two statements join them. Both are open.

**(U), uniformity in $\ell$.** There are $m_*>0$ and a sequence $\ell_j\to\infty$ in $\mathfrak L(g)$ with $m_{\ell_j}\ge m_*$.

**(J), the volume limit.** The moments of the systems $T_{\ell_j}^3\times\mathbb R$ are bounded uniformly in $j$ and $K$ on separated tuples (the analogue of (c)(2), Y 1781). Then a subsequence converges to a reflection-positive limit $S^\sharp$ on $\mathbb R^4$. The decay form of (G-ell) has the constant $\mu(\theta\overline F\cdot F)$, which is bounded by (c)(2). So $S^\sharp$ satisfies (G-inf-T) with $m=m_*$, and by 1.2 it has a unique vacuum and a gap $\ge m_*$.

**(J2), is $S^\sharp$ one of T0's theories?** At fixed spacing the limit points of the measures on $\ell_j^3\times\infty$ are translation-invariant Wilson Gibbs states. They are not by definition in $\mathcal G^{\rm tor}$, which is built from cubic tori (Y 1690). Y proves the lattice mirrors, the plateau law and the moment transfer for every periodic Gibbs state (G1, G3, G4: Y 2794–2800, 2907, 2922–2936), but states $\mathrm O(4)$ and the cone for volume-first limits (Y 1893–1894) and warns: "General growing-torus limits require their own mirror and cone argument" (Y 122927–122928). So (U) and (J) give the weak form of (G-inf). The strong form needs in addition that every component of every volume-first limit is such an $S^\sharp$. No uniqueness of the Gibbs state at fixed $(K,\beta)$ is known (Y 436–438: the proposition "gives no uniqueness or extremality of the limiting state").

**What the torus changes.** On $T_\ell^4$ the theory is, formally, the thermal state of $H_\ell$ at inverse temperature $\ell$; T0's torus statements (Y 1780, 1831–1836) are statements about that thermal state. They give no spectral statement by themselves. On $\mathbb R^4$ T0 gives $H$, a unique vacuum per component and $|v|^{-2}$. Neither gives a length scale at which correlations start to decay.

**The scale that (U) must cross.** By Y 1755 the bare coupling obeys $\beta\approx\frac{11N^2}{12\pi^2}\log(1/a_K)$. Read backwards from length 1 to larger lengths, the one-loop coupling reaches order one at the length $\xi_*\approx\exp\big(\tfrac{12\pi^2}{11N^2}g^{-2}\big)$ (heuristic; this file proves no flow beyond length 1). T0 admits every $\ell\in\mathfrak L(g)$, also $\ell\gg\xi_*$, but its renormalization steps stop at length 1 for every $\ell$. For $\ell\ll\xi_*$ the expected gap decreases with $\ell$ like a power of $g(\ell)$ over $\ell$ (literature, not read). So $m_\ell\ell$ is small in the whole range where the coupling at scale $\ell$ is small, and (U) is a statement about $\ell\gtrsim\xi_*$ only. (U) is the mass gap problem. (G-ell) for $\ell\ll\xi_*$ is not.

## 2. What is proved

"Abstract" means that this session read the arXiv abstract record and nothing else. "Row 656" means that `library/prior/gap-lit.md` read the abstract and this session did not. A statement from memory is marked so; it is not evidence.

| # | Statement | Regime | Source | Read |
|---|---|---|---|---|
| 1 | The Wilson transfer factor is positive and trace class; partition functions are submultiplicative in each side of a torus | SU(2), any $\beta>0$, finite lattice | Y 102623–102643 | read |
| 2 | The top eigenvalue of the finite-volume transfer operator is simple, so the gap is positive | fixed spacing, finite volume | theorem of Jentzsch | not read (from memory) |
| 3 | Plateau law: decay $(r/n)^2$ to the invariant plateau, for every translation-invariant Wilson Gibbs state | SU(2), every $\beta>0$, $\mathbb Z^4$, fixed spacing | Y 2862–2908 (statement), proof Y 125587 ff. | statement read, proof not read |
| 4 | Continuum limits of the $\operatorname{tr}(F^2)$ sector with the Osterwalder–Schrader axioms, unique vacuum per component, clustering $|v|^{-2}$ | SU(2), weak-coupling sequence, $T_\ell$ and $\mathbb R^4$ | Y 156–164, 1748–1909 | read; conditional on the inputs A–G of Y 1964–2944 |
| 5 | "Log-Sobolev and Poincaré inequalities hold" for the infinite-volume measure and "correlations of a large class of observables decay exponentially, namely the infinite volume measure has a strictly positive mass gap" | SU($N$), $d>1$, lattice, $|\beta|<\frac1{16(d-1)}$ ('t Hooft scaling $\beta N$) | Shen, Zhu, Zhu, arXiv:2204.12737 | abstract |
| 6 | Area law, clustering and gap in the convergent strong-coupling range | lattice, small $\beta$ | Osterwalder and Seiler 1978 | not read |
| 7 | "exponential decay of correlations for a wide class of gauge invariant functions" | finite gauge groups, possibly non-Abelian, weak coupling, lattice | Adhikari and Cao, arXiv:2202.10375 | abstract (no dimension, no rate in it) |
| 8 | Exponential decay for small and large $\beta$ | Ising lattice gauge theory | Forsström and Viklund, arXiv:2502.19942 | row 656 |
| 9 | No gap: Coulomb phase with a massless photon | U(1), $d=4$, weak coupling, lattice | Guth 1980; Fröhlich and Spencer 1982 | not read (named in `gap-prior.md` section 4) |
| 10 | Ultraviolet stability bounds on a torus | SU($N$), $d=4$, lattice, small-field and large-field steps | Bałaban, CMP 109, 119, 122 (local OCR) | not read by this session |
| 11 | Construction with an infrared cutoff | $d=4$ | Magnen, Rivasseau, Sénéor 1993 | not read |
| 12 | Low-lying spectrum on a small torus by perturbation theory in $g(\ell)$ and an effective Hamiltonian for the constant modes | SU(2), continuum, $\ell\ll\xi_*$ | Lüscher 1983; Lüscher and Münster 1984; Koller and van Baal 1988 | not read (from memory). van Baal, hep-ph/0008206: abstract, a review; it states no theorem |
| 13 | Inequality between the vortex free energy and the Wilson loop | SU(2) lattice | Tomboulis and Yaffe 1985; Borgs and Seiler 1983 | not read |
| 14 | Claim: "the SU(2) gauge theory is in a confining phase for all values of the coupling" by "approximate RG decimation transformations … which give both upper and lower bounds on the partition function" and "interpolation between these bounds" | SU(2), $d\le4$, lattice | Tomboulis, arXiv:0707.2179 | abstract |
| 15 | "We point out missing links in the recent paper by Tomboulis" | the same | Ito and Seiler, arXiv:0711.4930 | abstract; the failing step is not in it |
| 16 | "a theory is confining when center symmetry is unbroken"; "if the center of the gauge group is nontrivial, and correlations decay exponentially under arbitrary boundary conditions, then center symmetry does not break" | lattice gauge theories | Chatterjee, arXiv:2006.16229 | abstract |
| 17 | Comparison of SU(2) with $\mathbb Z_2$; a sufficient condition for confinement | SU(2) lattice | Mack and Petkova 1979, 1980 | not read |
| 18 | A statement of the open problems | — | Chatterjee, arXiv:1803.01950 | abstract; it lists no problem |
| 19 | Gap of an asymptotically free model in two dimensions | Gross–Neveu; O($N$) sigma model | Kopper, Magnen, Rivasseau; others | not read |
| 20 | Conditional lemmas: a loss budget below one gives a spectral bound; common decay on a dense algebra gives a gap and a unique vacuum | abstract | `ym/crossover-reduction`, as reported in `gap-prior.md` section 2 | digest read; branch files not read |
| 21 | Finite-depth response bounds $C u^{-1}e^{-\mu\tau_4}$, uniform in the volume | SU(2), two hidden layers, large $u=\beta$, soft kernels | PR #10149 `PROOF_TREE.md` 132–137 | tree read; "There is no proved physical mass gap" (its lines 14–15) |

No row gives a bound in physical units that is uniform in the lattice spacing. No row beyond the strong-coupling range gives exponential decay for SU(2) at fixed spacing.

## 3. The routes

### 3.0 Two tests that every mechanism must pass

**Test F (free field).** A generalized free field with a Källén–Lehmann weight that reaches zero is translation invariant and reflection positive, and it has no gap (Y 556–563 is the one-vector version). So a mechanism that uses only reflection positivity, translation invariance and regularity is false as a source of a rate. Y says the same of its plateau law (Y 125589–125591, 126124–126127).

**Test U (the group U(1)).** In four dimensions the U(1) lattice theory at weak coupling has no gap (table row 9, not read). Its transfer factor is positive and trace class by the argument of Y 102625–102634 (the character coefficients of $e^{\beta\cos\theta}$ are positive), so it obeys every inequality that follows from row 1. So a mechanism that does not use a property of SU(2) that U(1) lacks is suspect; it is false if row 9 holds. The candidates for that property are: positive Ricci curvature of the group, a finite centre, and the sign of the one-loop coefficient.

### 3.1 Route A, small physical volume

**The lead's candidate, tested.**

1. Row 662: "the renormalization steps of T0 reach the scale ell inside their domain of control". Changed. In Y the steps stop at length 1, and the torus has at least $\ell_\star(g)=2L^{11}MR(g^{-2}+B_\sharp)$ unit cells per side at that point (Y 84323–84326; Y 1646: "the floor … makes room for the localization cubes at every level"). A change of reference coupling moves the unit and keeps the floor: the implication $\ell\in\mathfrak L(g)\Rightarrow L^s\ell\in\mathfrak L(g_{[s]})$ "uses the stated torus floor and parameter choices" (Y 86076–86079). So the steps never reach a single block of side $\ell$.
2. Row 662: "what is left is a chain in the time direction with a compact fiber". Kept, with two changes. The fiber is a power of $G$ with of order $n_\ell^3$ bonds per time step, $n_\ell\ge\ell_\star(g)$ cells per side; it is compact and its dimension does not depend on $K$. The terminal law is not one Gibbs chain: Y 97942–97944: "A representation with a sum over large-field labels and label-dependent integral operations need not be a single coarse Wilson integral multiplied by one uniformly small polymer gas." It is $Z(w)=\sum_S\tau_S(w)(\mathcal V)$ with $\tau_S(0)\ge0$ (Y 97950–97955).
3. Row 662: "its gap is positive; the content of (G-ell) is the uniformity in the spacing". Kept (1.3).

**Which estimates of T0 hold along an infinite time direction.**

- By their statement, because they are local: the coupling sequence (Y 1755: "The values $x_k(\beta)$ are the same whatever torus the steps are carried out on"); the localized source energies, $|e_j(X;w)|\le Ce^{-\kappa_ed_j(X)}$ with dependence on $w$ only near $X$ (Y 95984–95987); the vacuum density, $|\ell^{-4}E_{\ell,K}-A_K|\le C_{\ell_0}e^{-c\ell/2}$ (Y 102563–102580); the terminal small-field density $\chi_n\exp\{E-x_nA(U_n(V))+F_n(U_n(V))\}dV$ (Y 98082–98089).
- By transfer, without a new renormalization construction: chessboard bounds on tori $\ell^3\times n\ell$. Y 102623–102643 varies "one side at a time" and ends: "The intermediate rectangular tori here use the same Wilson integrals and need no renormalisation construction."
- For every periodic Gibbs state on $\mathbb Z^4$: the bounds (c)(2) (Y 1785). They are infinite in four directions, not in one.
- Not: upper stability and the floor, $|\widetilde Z(w)|\le e^{C_g\ell^4}$, $\widetilde Z(0)\ge e^{-C_g\ell^4}$ (Y 95988–95989). On $\ell^3\times T$ they become $e^{\pm C_g\ell^3T}$ and say nothing about a correlation at time distance $T$. Y assumes no logarithm: "A zero-free logarithm on the whole global source ball is not assumed" (Y 2393–2394).

Y states the construction for cubic tori only (Y 1640). That the local statements hold on $\ell^3\times n\ell$ with the same constants is node A1; it is expected and not stated.

**What a proof of (G-ell) needs beyond them.** Three nodes.

*A1, the object.* The measures $\mu_{K,\ell^3\times n\ell,\beta}$ converge as $n\to\infty$ to the ground-state process $\mu^\infty_{K,\ell,\beta}$; its moments on separated tuples are bounded uniformly in $K$; so continuum limits on $T_\ell^3\times\mathbb R$ exist, are reflection positive in time, and carry $H_\ell\ge0$.

*A2, compactness uniform in the cutoff (sketch).* Let $\mathbb T=\mathsf T^{\ell/a_K}$. Then $\operatorname{Tr}\mathbb T=Z_{\ell^4}\le e^{E_{\ell,K}+C_g\ell^4}$ (upper stability at $w=0$). Submultiplicativity in the three spatial sides gives $Z_{(n\ell)^4}\le(\operatorname{Tr}\mathbb T^n)^{n^3}$, and $\operatorname{Tr}\mathbb T^n\le\lambda_0(\mathbb T)^{n-1}\operatorname{Tr}\mathbb T$. With the floor on $T_{n\ell}$, $n=L^q$, and the density comparison, $\lambda_0(\mathbb T)\ge e^{E_{\ell,K}-(C_g+\delta)\ell^4}$. Hence
$$\sum_i e^{-\ell(E_i-E_0)}=\operatorname{Tr}\mathbb T/\lambda_0(\mathbb T)\le e^{(2C_g+\delta)\ell^4}\quad\text{on all of }\mathfrak H_{K,\ell},\ \text{uniformly in }K.$$
So the number of eigenvalues with $E_i-E_0\le E$ is at most $e^{(2C_g+\delta)\ell^4+\ell E}$, and in the limit $e^{-\ell H_\ell}$ is trace class. The spectrum of $H_\ell$ is discrete. The bound has the form of the factor $e^{nc_V\ell^4}$ of Y 1780.

*A3, no vacuum degeneracy in the limit: (FV-U).* $\ker H_\ell=\mathbb C\Omega$ on $\mathcal H(\sigma_\ell)$ for every continuum limit $\sigma_\ell$ of A1.

A1, A2 and A3 give the continuum form of (G-ell): a discrete spectrum and a one-dimensional kernel give $m_\ell=E_1>0$. They give no number for $m_\ell$.

**The statement on the effective chain, named exactly: (TC$_\ell$).** A3 is where Route A can die. A degenerate limit vacuum needs a set of configurations that is metastable on a time scale that grows with $K$ and that the fields $\mathcal O(f)$ can see. T0 has upper bounds for rare events and one lower bound, on the product of small link balls (Y 98034–98049). A proof of A3 needs a lower bound that crosses a time slab. Let $\nu^\flat_K$ be the law of the final field $V$ on the unit lattice $n_\ell^3\times\mathbb Z$ under $\mu^\infty_{K,\ell,\beta}$.

- (TC1) Slab Peierls bound. There are a thickness $w$ and $\varepsilon<1$, independent of $K$, such that the $\nu^\flat_K$-weight of the labels $S$ that are not all-small-field in each of $k$ given disjoint slabs of thickness $w$ is at most $\varepsilon^k$.
- (TC2) Two-sided bound across a good slab. There is $\Delta(\ell,g)<\infty$, independent of $K$: for bounded Borel $A\ge0$ of the final field before a slab and $B\ge0$ after it, restricted to the labels that are all-small-field on the slab, $\nu^\flat_K(AB\mathbf 1_{\rm good})\ge e^{-\Delta}\,\nu^\flat_K(A\mathbf 1_{\rm good})\,\nu^\flat_K(B\mathbf 1_{\rm good})$.
- (TC3) Transfer to the fields. Conditional on the final field, the fields $\mathcal O(f)$ in two regions at time distance $t$ decouple up to $Ce^{-\kappa t}$, and the conditional law of the fields near a time depends on the final field at time distance $s$ up to $Ce^{-\kappa s}$, uniformly in $K$ and in mean over $\nu^\flat_K$.

(TC1) and (TC2) give that every limit point of $\nu^\flat_K$ is ergodic under time translations (sketch: an invariant event of weight $\delta>0$ meets a good slab within $k$ slabs once $\varepsilon^k<\delta/2$, and so does its complement; by stationarity both meet the same slab; approximate the event before the slab and its complement after it; (TC2) contradicts the disjointness). (TC3) carries ergodicity to $\sigma_\ell$. The expected size of $\Delta$ is $C(g)\,n_\ell^3$, the number of unit bonds that a time cut meets.

**A form that is false.** One may ask for the lower bound $\mu(FG)\ge c\,\mu(F)\mu(G)$ for all bounded $F,G\ge0$ of the fine fields, uniformly in $K$. The Ornstein–Uhlenbeck process is a counterexample to this scheme: it has a gap, and $P(x_{t_0}<0\mid x_0>\lambda)\to0$ as $\lambda\to\infty$. The fields $\mathcal O(f)$ have a range that grows with $K$. So the lower bound must be asked of the final field, whose fiber is compact, and (TC3) is needed. The same remark applies to a bound on the cross-ratio of the fine transfer kernel.

**What is known about the size of the gap.** Nothing rigorous was read. From memory, not read: for $\ell\ll\xi_*$ and periodic boundary conditions, perturbation theory with an effective Hamiltonian for the constant modes gives a gap of order $g(\ell)^{2/3}/\ell$ in the sector that the local fields see, and exponentially small splittings between the eight $\mathbb Z_2^3$ sectors of 1.3 (table row 12). A soft proof through (TC) would give at best $m_\ell\ge\exp(-C(g)n_\ell^3)$, and through A2 with A3 no number at all.

**What (G-ell) is worth.** It is not (G-inf) and not the Clay statement. It passes neither test of 3.0 as evidence for a gap: a compact U(1) theory on $T_\ell^3\times\mathbb R$ is expected to have a discrete spectrum and a unique vacuum too, and its infinite-volume limit has no gap. (G-ell) is a statement of ultraviolet control: the Hamiltonian of the continuum theory in a box exists, has compact resolvent and a non-degenerate ground state, uniformly in the cutoff. With T0's inputs as hypotheses it would be a new theorem. Its use for (G-inf) is to supply the object for (U), nothing more.

**A variant (not tested).** Twisted boundary conditions remove the constant abelian modes. From memory, not read: the small-volume gap is then of order $1/\ell$ without a power of $g$. T0 is not stated for twisted tori, so the variant costs a new object.

### 3.2 Route B, the crossover in infinite volume

**The lead's candidate, tested.** Row 662: "after the last step at which the coupling is small, the effective measure has a coupling of order one and no small parameter". Changed. T0 stops at reference coupling $g\le\gamma_J$ (Y 1724). The largest admitted $g$ is a threshold of the construction; it is small. Beyond length 1 there is no controlled step. What is left is a lattice gauge law on the unit lattice at the small coupling $g$, in infinite volume, and the distance to the expected correlation length is $\xi_*\approx\exp(\frac{12\pi^2}{11N^2}g^{-2})$ unit cells. This number does not depend on $K$, and no estimate of T0 is small against it. By the dilation identity (Y 1672–1678) the same statement can be said without any effective measure: Wilson's lattice theory at inverse coupling $\beta$ has a gap $m_W(\beta)\ge m\,L^{-K(\beta,g)}$ in lattice units. So Route B is the lattice gap at fixed weak coupling, with the asymptotic-scaling rate. T0 does not make it easier. T0 makes it equivalent to a statement on a precompact family of laws at one scale (Route C).

For each mechanism: the exact statement that it needs (N), what is known to fail (F), a first lemma for one lane (L), and the form of a counterexample to that lemma (X).

**B1. Poincaré or log-Sobolev inequality.**
(N) A Poincaré inequality $\operatorname{Var}_\nu(F)\le\kappa^{-1}\sum_b\nu(|\nabla_bF|^2)$ for the limit terminal law, or for Wilson's law at $\beta$, with $\kappa>0$ uniform in the volume and in the boundary condition; with locality of the interaction it gives exponential decay (the argument of table row 5; not read). The known sufficient condition is of Bakry–Émery type, $\operatorname{Ric}+\operatorname{Hess}S\ge\kappa$ (that the theorem of row 5 rests on it is reported by row 656 from the abstract of Nissim, arXiv:2510.22788; not read here). The range of row 5 is $|\beta|<\frac1{16(d-1)}$, which is $\frac1{48}$ in $d=4$.
(F) The gauge measure has the Ricci term (U(1) does not: Test U is passed). It lacks the Hessian term for two reasons. The function $a_p$ has a maximum at $U_p=-1$, so $\operatorname{Hess}(\beta a_p)$ has negative directions of size $\beta$. In a gauge-fixed small-field chart the Hessian is $\beta$ times a lattice Maxwell form, whose lowest eigenvalue on a box of side $R$ is of order $\beta R^{-2}$; so a constant $\kappa$ uniform in the volume cannot come from the quadratic part. It must come from the non-linear part, at a distance $\xi_*$. No theorem of this kind was found for weak coupling.
(L) The local version: on the product of link balls $\mathcal B_r$ of Y 98034–98049, in the axial chart, $-\log$ of the all-small-field terminal density is convex up to gauge directions, with Hessian $\ge c\,x\,(\text{Maxwell form})-C$.
(X) A direction of the chart with negative curvature of order $x$ at a point of $\mathcal B_r$. The lemma gives a Brascamp–Lieb bound with power-law decay only; it is a probe, not a step to a rate.

**B2. Reflection positivity with chessboard bounds.**
(N) None exists. FALSE as a source of a rate, by Test F and by Y 125589–125591, 126124–126127. Reflection positivity stays a tool: for the Peierls bound (TC1) and for A2.

**B3. Vortex free energy (Tomboulis and Yaffe; Borgs and Seiler).**
(N) The exact inequality is not read (row 661, item 6). In words: the Wilson loop is bounded by a power of a function of $Z^{\rm tw}/Z$, the ratio of the partition functions with and without a centre twist; an area law follows if $1-Z^{\rm tw}/Z$ decays exponentially in the area of the twisted plane on large tori. It uses the centre $\mathbb Z_2$ (Test U passed).
(F) Two things. First, the conclusion is an area law for Wilson loops. That is not (G-inf): the only implication read goes the other way (table row 16: exponential decay under arbitrary boundary conditions gives unbroken centre symmetry, which gives confinement), and Wilson loops are outside T0's sector. Second, the one attempt at the needed input (row 14) has "missing links" (row 15).
(L) The ultraviolet half: for fixed $\ell\in\mathfrak L(g)$, the ratio $Z^{\rm tw}_{K,\ell,\beta}/Z_{K,\ell,\beta}$ stays in a compact subset of $(0,1)$ along first-passage data. It needs T0's stability on a twisted torus.
(X) A sequence of data with the ratio tending to 0 or to 1 at fixed $\ell$.

**B4. Comparison with $\mathbb Z_2$ (Mack and Petkova).**
(N), (F) Not read; no statement is reconstructed here. From memory only: the comparison confines where the $\mathbb Z_2$ theory confines, and the $\mathbb Z_2$ theory in four dimensions does not confine at weak coupling. (L) A reading item for row 661, not a proof item.

**B5. Correlation inequalities for SU(2).**
(N) An inequality of Griffiths type that makes correlations of plaquette characters monotone in the couplings, and a domination of the terminal law by a Wilson law at strong coupling. (F) The first transports decay towards smaller $\beta$ only, which is the wrong direction; the second is not supplied by any weak-coupling renormalization. No Griffiths inequality for a non-Abelian plaquette action is known to this session (from memory, not read). Even the first one is not obvious: the fundamental representation of SU(2) is pseudo-real, $\int\operatorname{tr}(U^2)\,dU=-1$, so a Haar integral of a product of traces can be negative.
(L) $\langle\chi(U_p)\chi(U_q)\rangle\ge\langle\chi(U_p)\rangle\langle\chi(U_q)\rangle$ for two plaquettes of one cube, all $\beta\ge0$. (X) One value of $\beta$ where it fails; a run may look for it, a hand computation must confirm it.

**B6. Step scaling from $\ell$ to $2\ell$.**
(N) $m_{2\ell}\ge(1-\epsilon(\ell))\,m_\ell$ for $\ell\ge\ell_c$ with $\sum_k\epsilon(2^k\ell_c)<\infty$, and a bound at $\ell_c\approx\xi_*$.
(F) Positivity of the transfer factor gives $\operatorname{Tr}e^{-tH_{2\ell}}\le(\operatorname{Tr}e^{-tH_\ell})^8$ (Y 102623–102643 applied to three sides). With the vacuum energies removed this bounds the number of low states at $2\ell$ only when the defect $E_0(2\ell)-8E_0(\ell)$ is small against $m_\ell$, and it loses a constant factor at each doubling (sketch, not written out). Compact U(1) obeys the same inequalities, and its gap in a box is expected to go to zero with $1/\ell$ (Test U). So step scaling from positivity alone is false if table row 9 holds. A true step needs an input that is specific to SU(2); none is known.
(L) By hand: a family of positive trace-class semigroups that is submultiplicative in every side and has $m_\ell\ell$ bounded (candidate: the U(1) theory with Villain action in a box, where the constant modes and the plane waves are explicit). This closes the route without row 9. (X) A derivation of $\inf_\ell m_\ell>0$ from submultiplicativity and compactness alone.

**B7 (added). Zero-free source balls.** One could ask to strengthen D1 to a zero-free logarithm of $Z(w)$ on a complex source ball, with a bound proportional to the support of $w$ and uniform in the volume. FALSE as a source of a rate for the sources of T0: a lattice Gaussian field whose covariance is a superposition $C=\int d\rho(\mu^2)(-\Delta+\mu^2)^{-1}$ of massive propagators, with $\int d\rho(\mu^2)/\mu^2<\infty$ and weight reaching zero, is reflection positive, has $\log Z(w)=\frac12\langle w,Cw\rangle$, which is zero-free and bounded by $\frac12\|w\|_\infty^2|\operatorname{supp}w|\sum_x C(x)$, and has no gap. Analyticity in the linear sources of one field is not the complete analyticity of Dobrushin and Shlosman, which perturbs every local term (reported in `gap-prior.md` section 4; not read).

**B8. Rigorous numerics.** A finite-size criterion for the terminal law (a Dobrushin–Shlosman condition on a box of side several $\xi_*$) is a finite computation in principle. It is outside our rules (GOAL.md, "No computer-assisted steps") and, at T0's couplings, outside any machine. Ranked last.

**Verdict on Route B.** B2, B6 and B7 are false as mechanisms. B3 does not end at (G-inf). B4 and B5 have no statement to attack. B1 is the only mechanism with a theorem behind it, and its theorem is a strong-coupling theorem. No first lemma of Route B moves the crossover.

### 3.3 Route C, a conditional theorem

**H0, the hypothesis.** For every first-passage datum $(K,\beta)$ at $g$ with $K\ge K_0$ and every ergodic translation-invariant Wilson Gibbs state $\rho$ at $(K,\beta)$ that realizes a component (Y 119203–119211), with $\mathfrak P_+$ as in 1.2:
$$\rho(\theta\overline F\cdot\tau_{te_4}F)-|\rho(F)|^2\le\rho(\theta\overline F\cdot F)\,e^{-mt}\qquad(F\in\mathfrak P_+,\ t\in a_K\mathbb N).$$
In words: the transfer operator of Wilson's infinite-volume theory at $\beta$ has a gap $\ge m\,a_K=m\,L^{-K(\beta,g)}$ in lattice units on the sector that the plaquette fields generate. H0 is a statement on one one-parameter family of measures. It contains no continuum object.

**The implication T0 and H0 give (G-inf), node by node.**

| Node | Statement | Kind |
|---|---|---|
| C1 | T0: components $\sigma_\xi$ exist, with reflection positivity and $e^{-tH}$ | T0 itself; open |
| C2 | $\sigma_\xi$ is the limit of the moments of realizing states $\rho_j$, on every separated tuple | in T0 (Y 119203–119211); cited |
| C3 | $\rho_j(\theta\overline F\cdot F)$ and $\rho_j(\theta\overline F\cdot\tau_tF)$ converge; the inequality of H0 passes to $\sigma_\xi$ for $L$-adic $t$, then for real $t$ by strong continuity | routine |
| C4 | (G-inf-T) gives (G-inf-S), 1.2 | routine |
| C5 | (G-inf-S) gives (G-inf-D), 1.2, with $\mathrm O(4)$ from T0 | routine |

No node is non-routine. H0 is the weakest hypothesis in this file: (G-inf) is H0 for the limit, and H0 asks it of the approximants with the norm of T0 as the constant.

**H1, a hypothesis on one effective measure.** Replace H0 by the same inequality for the terminal law: $F$ a bounded function of the final field $V$, $\rho$ replaced by $\nu^\flat$, uniformly in $K$ (or for the limit points of $\nu^\flat_K$ only). Then two more nodes are needed, and both are non-routine.

| Node | Statement | Kind |
|---|---|---|
| C6 (TR) | Terminal sourced representation for the full measure: for $\nu^\flat$-almost every $V$, $E[e^{\mathcal O(w)}\mid V]=\exp\sum_X\epsilon(X;V,w)$ with $\epsilon$ local in $V$ and $w$ and $|\epsilon|\le Ce^{-\kappa d(X)}$, or the same up to label events with exponential tails | not routine. Y has it for the all-small-field label (Y 98082–98089) and warns that "A pointwise polymer logarithm cannot replace that history representation without an exact common integral formula" (Y 2404–2406) |
| C7 (FS) | The part of $\mathcal H(\sigma)$ orthogonal to the functions of the final field has spectrum in $[m_{\rm fl},\infty)$, $m_{\rm fl}>0$ of order $\kappa/M$ | not routine. At the lattice level the closed span of the functions of the final field is invariant under the unit time step $e^{-H}$, so it reduces $H$; the bound on its complement is (TC3) of Route A in spectral form |

H1 with C6 and C7 implies H0 for the limit. H1 is what Route B would have to prove. Its value is that it is a statement on a family of laws with a compact fiber, a fixed small coupling and bounds that do not depend on $K$.

**Comparison with the open nodes of PR #10149.** Its tree (lines 47–51) has: V "rough terminals and required new conditional classes", T "third transition and inherited-action closure", S "depth and cutoff control at physical scales", X "nontrivial continuum QFT reconstruction", M "positive physical spectral gap". Its arrows $T\to S\to X\to M$ and $S\to M$ are "unproved" (lines 83–86).

- X is T0. Once T0 is available, X is supplied, for Wilson's measure and Bałaban's averages; a second reconstruction for soft kernels would repeat it.
- S at weak coupling is the content of T0's inputs A–E (Y 1964–2544). S "at physical scales" beyond length 1 is not supplied by T0 and is not a step-by-step statement there; it is H.
- V and T are the closure of one more exact transition at weak coupling. In T0's language they are the large-field histories and the invariance of the inductive class (Y 2307–2355, inputs C1–C4); this matching is this session's reading of the two texts. They repeat, for another blocking, what T0 supplies. They are not a part of H0 or H1.
- M is (G-inf). The dotted arrow $S\to M$, "unproved physical decay", is H0.
- The finite-depth response bound itself ($Cu^{-1}e^{-\mu\tau_4}$ at depth two) is a decay in block units at a fixed depth. It is needed neither for T0 nor for H. The nearest node here is C6/C7: a connected response of the conditional law given the terminal field. If that lane continues, its estimate is useful only as a second derivation of C6 at small depth.

## 4. The tree

Status words: PROVED-READ (lines) = proved in a source that this session read; STATED-NOT-READ = stated in a source that was not read; OPEN; FALSE (counterexample). "OPEN, routine" means that this file gives a sketch and expects no obstacle; a sketch is not a proof. † marks the node where a route can die.

```text
(G-inf), strong form: every component of every volume-first limit at g
└─ (G-inf), weak form: one limit theory with the axioms of 1.1
   ├─ T0
   ├─ E: (T) => (S) => (D)
   ├─ Route C:  H0 ──C3──C4──C5──> (G-inf)
   │            H1 + C6(TR)† + C7(FS) ──> H0 for the limit
   ├─ Route A:  A1 + A2 + A3† ──> (G-ell) for each ell
   │            (G-ell) + U† + J ──> (G-inf), weak form
   └─ Route B:  a mechanism B1..B8 ──> H1 or H0     († at every mechanism)
   J2: the limit of Route A is a theory of T0 (strong form only)
```

| Node | Exact statement | Status |
|---|---|---|
| T0 | 1.1; Y 156–164, 1748–1909 | OPEN. Y states it under assumed estimates (Y 157). Our lane: "T0 remains open" (`t0-tree.md` line 9) |
| P | Wilson transfer factor positive and trace class; $Z$ submultiplicative in each side | PROVED-READ (Y 102623–102643) |
| PL | Plateau law $(r/n)^2$ for every periodic Wilson Gibbs state | PROVED-READ for the statement (Y 2884–2908); proof not read |
| NC | Polynomial clustering implies a gap | FALSE ($d\mu=Ee^{-E}dE$; Y 556–563, 122948–122957) |
| E | (G-inf-T) $\Rightarrow$ (G-inf-S) $\Rightarrow$ (G-inf-D), 1.2 | OPEN, routine. The same lemma is reported as L3 of `ym/crossover-reduction` (`gap-prior.md` section 2; not read) |
| FG | At fixed $K$ and $\ell$ the gap is positive | STATED-NOT-READ (Jentzsch), from P |
| A1 | The object $T_\ell^3\times\mathbb R$: $\mu^\infty_{K,\ell,\beta}$, moment bounds uniform in $K$, limits with $H_\ell\ge0$ (3.1) | OPEN, routine given D1 of Y 2359–2406 |
| A2 | $\operatorname{Tr}\mathbb T/\lambda_0(\mathbb T)\le e^{(2C_g+\delta)\ell^4}$ uniformly in $K$; discrete spectrum of $H_\ell$ (3.1) | OPEN, routine given Y 95984–95992, 102645–102672 and P |
| A3 † | (FV-U): $\ker H_\ell=\mathbb C\Omega$ for every limit of A1 | OPEN. Route A dies here |
| TC1 | Slab Peierls bound (3.1) | OPEN |
| TC2 | Two-sided bound across a good slab (3.1) | OPEN; T0 has the density on the all-small-field label (Y 98082–98089) and no statement across a slab |
| TC3 | Transfer from the final field to the fields $\mathcal O(f)$ (3.1) | OPEN; same content as C6 and C7 |
| DB | Lower mixing for all bounded functions of the fine fields, uniformly in $K$ | FALSE as a scheme (Ornstein–Uhlenbeck, 3.1); not decided for Yang–Mills |
| G-ell | 1.3, continuum form | OPEN; follows from A1, A2, A3 |
| U † | $\inf_jm_{\ell_j}>0$ along $\ell_j\to\infty$ | OPEN. This is the mass gap problem. The step from (G-ell) to (G-inf) dies here |
| J | Limits of the systems $T_{\ell_j}^3\times\mathbb R$ exist and keep the decay (1.4) | OPEN, routine given U and (c)(2)-type bounds |
| J2 | The limit of J has $\mathrm O(4)$ and the cone, or equals a component of a volume-first limit | OPEN (Y 122927–122928) |
| H0 † | 3.3 | OPEN. Route C's hypothesis; equivalent in content to U |
| C3–C5 | Passage of H0 to the limit and to (G-inf) | OPEN, routine |
| H1 | H0 for the terminal law | OPEN |
| C6 † | (TR), terminal sourced representation for the full measure | OPEN. The effective-measure form of Route C dies here; Y 2404–2406 warns |
| C7 | (FS), spectrum of the fluctuation sector | OPEN |
| B1 † | Poincaré inequality uniform in the volume at weak coupling | OPEN; PROVED only at $|\beta|<\frac1{16(d-1)}$ (STATED in an abstract that was read, table row 5) |
| B2 | A rate from reflection positivity and chessboard bounds | FALSE (generalized free field; Y 125589–125591, 126124–126127) |
| B3 † | Exponential decay of $1-Z^{\rm tw}/Z$ in the area | OPEN; inequality STATED-NOT-READ; does not end at (G-inf) |
| B4 | Comparison with $\mathbb Z_2$ | STATED-NOT-READ; no statement fixed here |
| B5 † | Griffiths-type inequality for SU(2) plaquette characters | OPEN; wrong direction for the crossover |
| B6 | Step scaling from positivity of the transfer factor alone | FALSE if table row 9 holds (compact U(1)); OPEN as a hand counterexample |
| B7 | A rate from a zero-free source ball | FALSE (Gaussian field with a superposed covariance, 3.2) |
| B8 | Finite-size criterion by rigorous numerics | outside our rules; last |

**Ranking.** Worth is on a scale where 10 is the strong form of (G-inf) for T0's theory. Chance is the chance that one proof lane closes the first node of the route.

| Rank | Route | Worth | Chance | Why |
|---|---|---|---|---|
| 1 | A, to (G-ell) only | 2 | 0.6 for A1 with A2; 0.2 for A3 | Worth: a theorem on the Hamiltonian in a box, uniform in the cutoff, conditional on T0's inputs; it is not evidence for a gap in infinite volume, because U(1) would have it too. Chance: A2 is ten lines from statements that Y prints; A3 needs a lower bound across a slab, and T0 has lower bounds only on the product of small link balls. |
| 2 | C | 1 with H0; 3 with H1, C6, C7 | 0.85 for C3–C5; 0.3 for C6 | Worth: with H0 it is a restatement; with H1 it reduces the gap of this sector to mixing of one family of laws with a compact fiber and a fixed small coupling. Chance: C3–C5 are limits of inequalities; C6 must turn Y's label sum into a conditional statement, against Y's own warning. |
| 3 | B | 10 | below 0.01 for a node that moves the crossover; 0.3 to 0.6 for the probes (L) | Worth: it is the problem. Chance: three mechanisms are false, one ends elsewhere, two have no statement, and the one with a theorem needs strong coupling. |
| 4 | B8, numerics | — | — | Outside the rules. |

No route in this file reaches (G-inf). Routes A and C can end in theorems that are conditional on T0. T0 itself is open in Y and in our lane.

## 5. The first three proof items

Hardest first. Each text is ready to queue. Each lane first applies rule 0a (grep `library/open-core.md`, `library/l17c.md` and the FINISH rows) and rule 9 (find the object in Y and quote it). All Y lines refer to commit `2bc0658f…`. In all three, T0's inputs are hypotheses, named by their Y labels; nothing is to be re-proved from T0.

### P1. `gap-fvu`: no vacuum degeneracy in a box (node A3; hard proof)

**Statement.** Fix $g\le\gamma_J$ and $\ell\in\mathfrak L(g)$. Assume the object of A1. Let $\nu^\flat_K$ be the law of the final field $V$ (the field on the unit lattice after the $K$ steps of the run) under the infinite-time measure $\mu^\infty_{K,\ell,\beta}$, for first-passage data $(K,\beta)$. Prove: every weak limit point of $\nu^\flat_K$ as $K\to\infty$ is ergodic under time translations of the unit lattice. Proposed proof: (TC1) and (TC2) of section 3.1, then the argument sketched there.

**Inputs, as hypotheses.** The label representation $Z=\sum_S\tau_S(\mathcal V)$, $\tau_S(0)\ge0$, with its term and label-sum bounds (Y 97946–97995); the floor on the product of link balls (Y 98034–98078); the terminal density of the all-small-field label, $\chi_n\exp\{E-x_nA(U_n(V))+F_n(U_n(V))\}dV$, and its bounds (Y 98080–98113); rarity of large-field histories, inputs C3 and D3 (Y 2335–2346, 2460–2473); locality and the torus floor (Y 84317–84333); positivity of the transfer factor (Y 102623–102643). The lane must first write these on $\ell^3\times n\ell$ and say which constants change (none is expected to).

**What a counterexample looks like.** A system of labels and measures on $n_\ell^3\times\mathbb Z$ that satisfies every hypothesis above as printed, and has a non-ergodic limit point: two sets of final fields, each of weight bounded below, with a transition weight that tends to zero as $K\to\infty$. If one exists, the lane names the property of the actual construction that the printed hypotheses omit.

**Model split.** Direction is fixed here. Hard proof: Fable at medium effort writes; Opus checks line by line.

**Stop rule.** A proof; or a counterexample of the form above; or one precise lemma (expected: (TC2) for labels that are large-field next to the slab) attacked in three distinct ways, with the reason each way failed. A missing lower bound in Y is not a stopping point: state it as the lemma.

### P2. `gap-tr`: from the final field to the fields $\mathcal O(f)$ (nodes TC3, C6, C7; hard proof)

**Statement.** For a first-passage datum and a periodic Gibbs state $\rho$ on $\mathbb Z^4$ (and for $\mu^\infty_{K,\ell,\beta}$), with final field $V$: there are $C,\kappa>0$, independent of $K$, of the state and of positions, such that for separated tuples $X,Y$ with supports at distance $d$,
$$\Big|\rho(X\cdot Y)-\rho\big(E[X\mid V]\,E[Y\mid V]\big)\Big|\le C_{X,Y}\,e^{-\kappa d},$$
and $E[X\mid V]$ is the limit of functions $\phi_s(V)$ of the final field within distance $s$ of the support of $X$, with $\rho(|E[X\mid V]-\phi_s|)\le C_Xe^{-\kappa s}$. The constants $C_X$, $C_{X,Y}$ are bounded by the moment bounds of (c)(2). Consequence to write: a rate $m_b$ for all bounded local functions of $V$ under $\rho$ gives the rate $\min(m_b,\kappa)/2$ for the fields $\mathcal O(f)$; this is "H1 gives H0" of section 3.3.

**Inputs, as hypotheses.** The localized source energies with locality and the bound $Ce^{-\kappa_ed_j(X)}$ (Y 95984–95992); the label representation (Y 97946–97966); the statement that a "pointwise polymer logarithm cannot replace that history representation without an exact common integral formula" (Y 2399–2406), which the lane must respect; the all-state transfer (Y 2918–2944).

**What a counterexample looks like.** A label system with all printed bounds in which two source regions far apart are coupled through one large-field label of weight that is small but does not decay with the distance, at fixed final field.

**Model split.** Hard proof: Fable at medium effort writes; Opus checks.

**Stop rule.** A proof; a counterexample; or one named lemma failed in three ways. If the statement holds only outside a set of final fields of small weight, prove that form and say what Route C loses.

### P3. `gap-box`: the Hamiltonian in a box and the conditional theorem (nodes A1, A2, E, C3–C5; routine)

**Statement.** (a) A1 of section 3.1: for $\ell\in\mathfrak L(g)$ and $n=L^q$, the bounds of Y 95984–95992 and the chessboard bounds hold on $\ell^3\times n\ell$ with constants per unit volume that do not depend on $n$; the limit $n\to\infty$ exists; continuum limits on $T_\ell^3\times\mathbb R$ exist along subsequences, are reflection positive at time mirrors and carry $H_\ell\ge0$. (b) A2: $\operatorname{Tr}\mathbb T/\lambda_0(\mathbb T)\le e^{(2C_g+\delta)\ell^4}$, the counting bound, and trace class of $e^{-\ell H_\ell}$ in the limit, by the sketch of 3.1. (c) The $\mathbb Z_2^3$ sectors of 1.3. (d) Lemma E of 1.2, both directions, with the axioms each direction uses. (e) T0 and H0 give (G-inf): nodes C3–C5 of 3.3. (f) Corollary: A1, A2 and the conclusion of P1 with P2 give the continuum form of (G-ell).

**Inputs.** Y 102623–102643 (positivity, submultiplicativity); Y 95984–95992 (stability, floor); Y 102543–102580 and 102645–102672 (vacuum density); Y 1757–1773 (the Hilbert space on $\mathbb R^4$, to copy for the box); Y 119203–119211 (realizing states); Y 1672–1678 (dilation identity). Check first whether L3 of `ym/crossover-reduction` and `docs/CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md` (on `origin/main` according to `gap-prior.md`; absent from this checkout; not read) already prove (d); if so, cite them.

**Model split.** Routine: Opus writes; the other model checks.

**Stop rule.** A proof of each part, or the first part that fails with its explicit failure. Part (b) can fail only if the stability bounds do not transfer to $\ell^3\times n\ell$; then state the missing bound.

**Not queued.** Route B. The reading of row 661 (items 5, 6, 7) is enough for B3 and B4. The probes (L) of B1, B5 and B6 are small and safe; none moves the crossover.

## Result

Kind: direction document. It proves nothing. Every short argument in it is a sketch and is unchecked.

1. T0, as Y states it, is conditional, concerns the $\operatorname{tr}(F^2)$ sector, lives on cubic tori and on $\mathbb R^4$ (volume first), and gives clustering $|v|^{-2}$ from reflection positivity alone. Y says in four places that it proves no gap.
2. (G-inf) is fixed in three equivalent forms; decay on reflected pairs in time gives the gap and the unique vacuum from reflection positivity and the semigroup alone; the converse in all directions needs $\mathrm O(4)$.
3. (G-ell) needs an object that T0 does not have. On it, a uniform trace bound follows from T0's stability bounds (sketch), so the continuum form of (G-ell) is equivalent to the absence of vacuum degeneracy in the limit. (G-ell) is not evidence for (G-inf).
4. Three candidates of the lead were changed: the steps of T0 do not reach the scale $\ell$; the terminal law is a sum over labels, not one chain; the coupling after the last step is small, not of order one, and the missing parameter is the ratio $\xi_*$.
5. Route B: B2, B7 false; B6 false if U(1) has no gap; B3 ends at an area law; B4, B5 without a statement; B1 a strong-coupling theorem.
6. Route C: T0 and H0 give (G-inf) with routine nodes only. A hypothesis on one effective measure needs C6 and C7. The finite-depth response of PR #10149 repeats what T0 supplies and is not a part of H.
7. Open: everything. First items: P1, P2, P3.
