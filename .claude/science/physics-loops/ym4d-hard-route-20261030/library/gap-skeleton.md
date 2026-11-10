lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-11T08:27Z

# Mass-gap skeleton (queue row 662, `gap-skeleton`)

`library/prior/gap-lit-2.md` is NOT at the pinned commit 0de407dd4. Every literature item below is marked 'not read', except the abstracts and the lines of Y that this session opened itself; those are marked with what was read.

Provenance: Claude Fable 5.2, high effort, Mac mini worker, checkout 0de407dd4, 2026-11-10. This is a direction document. It proves nothing and claims nothing. It is not checked by another model. No numerics were run. Short arguments below are marked "sketch"; a sketch is a proposal for a proof item, not a result.

Credit. The existence theorem, its hypotheses and every quoted line of Y are the text of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The renormalization group behind it is Tadeusz Bałaban's. The digests `library/prior/gap-prior.md` and `library/prior/gap-lit.md` are Codex readings (rows 655, 656). The tree of PR #10149 and the file `parts/physical-gap.md` are other lanes of this repository.

## 0. Repo search and sources read

Repo search. `library/open-core.md`, `library/open-registry.md` and the FINISH rows were searched for "mass gap", "spectral gap", "transfer operator", "small volume". Hits: FINISH rows 650, 655, 656, 661, 662 only. No open lemma of this lane covers a gap statement. This file attacks no open lemma.

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
- $\mathbb R^4$, volume first. Y 1690: "each $\nu_j\in\mathcal G^{\mathrm{tor}}_{K_j,\beta_j}$ is a limit point of the periodically extended torus measures as $\ell\to\infty$, with spacing and coupling held fixed. Thus the volume is removed first and the spacing only afterwards." Bounds uniform in the volume: (c)(2), Y 1781–1785, also "for $S^T_n[\nu]$, where $\nu$ is an arbitrary periodic Gibbs state".

**Axioms.** For every continuum limit: $W_4$ and translation invariance, reflection positivity at coordinate mirrors, symmetry, regularity (Y 1757–1761). On $\mathbb R^4$: growth, and a Hilbert space $\mathcal H(S)$ with $\mathcal T_t=e^{-tH}$, $H\ge0$, $H\Omega=0$ (Y 1762–1773). For a volume-first limit (Theorem "Canonical components", Y 1884–1909): $H\ge|P_j|$, $\mathrm O(4)$ invariance, a canonical decomposition $\sigma_S=\int_{\mathsf X}\sigma_\xi\,\lambda(d\xi)$ with $\ker H\cong L^2(\mathsf X,\lambda)$, and for each component $\sigma_\xi$ a unique vacuum, the forward cone, all Osterwalder–Schrader axioms and a Wightman theory. The Hamiltonian is stated on $\mathbb R^4$ only. On a torus Y states no Hamiltonian.

**Clustering.** Polynomial, per component. Y 1900–1907: "$|\sigma_\xi(X\cdot\tau_vY)-\sigma_\xi(X)\,\sigma_\xi(Y)|\le C(X,Y)\,|v|^{-2}$ $(|v|\ge r(X,Y))$, where $C(X,Y)$ and $r(X,Y)$ are the same for all $\xi$ and for all volume-first limits at $g$." Its source is the lattice plateau law, Y 2884–2893: for every translation-invariant Wilson Gibbs state $\nu$, $|\nu(\overline A\,\tau_yB)-\operatorname{Pl}_\nu(A,B)|\le C[(r/n)^2+(r/n)^3]\mathcal N_{\nu,r}(A)^{1/2}\mathcal N_{\nu,r}(B)^{1/2}$. Y 125589–125591: "The estimate in this section is a consequence of translation invariance and reflection positivity in coordinate and diagonal directions. No infrared bound, mass gap, or differentiability of a pressure is assumed." The bound depends on $r/n$ only. It contains no length, so it cannot give a rate.

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

**Lattice object.** Fix $\ell\in\mathfrak L(g)$ and a first-passage datum $(K,\beta)$. Let $\Lambda^{(3)}=(a_K\mathbb Z/\ell\mathbb Z)^3$, and let $\mathfrak H_{K,\ell}$ be the gauge-invariant functions in $L^2(G^{\text{bonds of }\Lambda^{(3)}},\text{Haar})$. The one-step transfer operator is $\mathsf T=W^{1/2}\,\mathsf C\,\mathsf P\,W^{1/2}$: $W$ multiplies by $\exp(-\beta\sum_{p\subset\Lambda^{(3)}}a_p)$, $\mathsf C$ convolves every bond with $c(u)=e^{-\beta(1-\operatorname{tr}(u)/2)}$, $\mathsf P$ is the gauge projection. Then $Z_{\ell^3\times na_K}=\operatorname{Tr}\mathsf T^n$. Y 102625–102634 states what is needed: "the Wilson transfer factor is the product of the gauge-invariant projection and the convolution with the product of the one-bond class functions … These operators commute. The character coefficients of $c$ are nonnegative … Hence the crossing factor is positive … the convolution is trace class". So $\mathsf T\ge0$ is self-adjoint and trace class. Its kernel on gauge orbits is continuous and strictly positive, because $c>0$. By the theorem of Jentzsch (not read) the top eigenvalue $\lambda_0$ is simple. Put $E_i=-a_K^{-1}\log\lambda_i$.

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

(Sections 2 to 5 follow.)
