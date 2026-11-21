## Repo search

**GUIDE — Sources checked.** Row 1133 at `6b15c62cb` has no task-specific prior file or “Repo prior work” line. The lead's 8 November digest searched main and PRs 10114, 10133, 10134 and 10141 on thirteen mostly ultraviolet targets. Its closest hit is the soft-route Codex note `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (PR 10114, lines 1–11, 106–149). It gives a positive one-time plaquette witness and a contraction at fixed spacing for bare β at most 1/32. The seed needs an upper bound on excited-state propagation. The one-time witness bounds it from below. The finite-clock note on main (14 September, lines 79–94 and its statement) concerns an abelian Villain measure. The massive-Wilson-loop note (same date, lines 120–145) bounds a Dirichlet noncompact Maxwell covariance. PR 10141's `research/ym4d/README.md`, lines 25–38, identifies its hard-route snapshot lineage. I also searched the YM research and soft-route Markdown on main `8b11ae2bb` and PR heads 10114/33/34/41/44 for master loop equations, signed surface and Haar-pairing terms, and the pinned open registry for this target. These checks identified no other owner or supplier of the winding-surface estimate below. The digest's GEOH winding-carrier entry concerns localization of RG reads. [Lead’s search](prior/repo-search-2026-11-08.md) · [Council brief](gap-council-brief.md)

**GUIDE — Row 1133 research note.** Codex, combinatorics and random geometry, pinned at `6b15c62cb`. PROVED denotes a displayed hand argument or an explicitly conditional deduction. Independent checking and formalization are pending. Each label covers its accompanying displays and their continuation.

**GUIDE — Five-step plan**

1. Check the pinned sources and prior-work index, then identify the combinatorial obstacle and the limit of the nearest theorem.
2. Rank at most three attacks and give their first estimates, diagnostic cases and decisive tests.
3. Attempt the leading estimate by hand and record the first unresolved line or counterexample.
4. Compare the attacks with the route registry, test table and cited FINISH results.
5. Record the result and its scope.

## 1. Which surfaces would have to contract?

**PROVED — Finite-volume identity.** Write $\Lambda_n$ for the cubical four-torus with $n$ sites on a side and normalized link Haar measure, and $F(n)=\log Z(\Lambda_n)$. The regular cover $\Lambda_{2n}\to\Lambda_n$ has 16 sheets. The partition function of 16 disjoint copies is $Z(\Lambda_n)^{16}$ by independence. Thus $\Phi_2(n)=16F(n)-F(2n)$ compares the disjoint cover with the connected cover at the same bare coupling. Both sides are full periodic partition functions and include all transfer sectors. A contractible Wilson-loop area estimate measures a different observable.

**ARGUED — Existing interface.** The brief asks for a selective comparison after first passage with constants uniform in the fine cutoff. I use row 697's finite-volume seed for $\Phi_2$. Section 4 gives the precise connection to the Casimir formulation of row 708. The band refers to an effective action. Substituting a bare isotropic Wilson action at an effective $\beta$ would require a matching estimate. The ultraviolet method is Tadeusz Bałaban's, in the account of Ethan Sussman and Levent Alpoge with Claude and Codex as authors of their text. Outline index chunks 01, 18 and 29 and their obligations point to lines 588–599, 19813–19885 and 32485–32490. The scalar recursion reaches its terminal window under its next-step and drift hypotheses. CA-I lines 2691–2712 describe the curvature-sector reconstruction. The infrared spectral estimate is left open. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L19813-L19885) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2691-L2712)

**GUIDE — Nearest exact theorem.** Sky Cao, Minjae Park and Scott Sheffield, Theorem 6.29, express finite-lattice symplectic Wilson expectations as sums over maps. Their graph permits a plaquette list closed under reversal, as on the torus. Take their matrix size $N=2$, so $Sp(N/2)=Sp(1)=SU(2)$. In (1.2) the coefficient of the ordinary real trace per unoriented plaquette is $2N\beta$, giving $\beta=\beta_W/8$ here. The theorem takes the absolute value *after* the signed sum at fixed plaquette multiplicities. It gives a finite-volume representation. A bound on the connected winding part of a logarithm uniform in box and cutoff would be a further inequality. Their open problem 7 explicitly asks about cancellation between surface resolutions. Earlier SU(2) surface representations are due to David Brydges, Charles Giffen, Bergfinnur Durhuus and Jürg Fröhlich. Sourav Chatterjee's Theorem 3.1 gives an absolutely convergent string-trajectory sum for SO(N) at sufficiently small coupling parameter in the large-N limit. Jafar Jafarov's Theorem 4.1 bounds the SU(N) expansion order by order, with a small-coupling interval that may depend on the order. At $N=2$ the loop identities are exact, but a uniform estimate of the signed winding sum across the order-one band is still needed. [Cao–Park–Sheffield, §§1, 6.1.2 and 7](https://arxiv.org/abs/2307.06790) · [Chatterjee, Theorem 3.1](https://arxiv.org/abs/1502.07719) · [Jafarov, §4](https://arxiv.org/abs/1610.03821)

## 2. Two attacks, ranked by the availability of a decisive hand test

**GUIDE — Common notation.** For a set $S$ of unoriented plaquettes, $Z_n(S)$ uses normalized link Haar measure and the weight $w(g)=\exp(\beta_W\operatorname{Re}\operatorname{Tr}(g)/2)$ on $S$. The extensive Wilson constant cancels in every covering difference. With $\pi:\Lambda_{2n}\to\Lambda_n$, put

$$
D_n(S)=16\log Z_n(S)-\log Z_{2n}(\pi^{-1}S),\qquad
d_n(S)=\sum_{A\subseteq S}(-1)^{|S|-|A|}D_n(A).
$$

**PROVED — Meaning of the grouping.** Finite inclusion–exclusion gives $\Phi_2(n)=\sum_{S\subseteq P(\Lambda_n)}d_n(S)$. To see what has already been summed, expand each log on its own plaquette-subset lattice. The upstairs coefficient of $B$ occurs in $\log Z_{2n}(\pi^{-1}A)$ precisely when $\pi B\subseteq A$. Its coefficient in the finite difference for $S$ is therefore zero unless $\pi B=S$. Each partition integral retains every multiplicity and spin on its support. Disconnected plaquette–link components factorize, so their logarithms add. If the incidence graph of $S$ lifts to 16 disjoint copies, every subset does too and $d_n(S)=0$. All identities hold at finite real coupling.

### 1. Sum all lift choices at fixed plaquette support

**GUIDE — Mechanism.** Take the difference between covers before taking any absolute value. This removes every support that lifts trivially. For the remaining supports, a plausible geometric estimate would pay for their windings by the loss of Haar colour degrees of freedom on a surface. The hoped-for gain is in the sum of all maps on the same support, even when a face is visited many times. This changes the order of the majorization in the strong-coupling trajectory method. The coefficients are extracted exactly from the homogeneous Wilson partition function.

**GUIDE — Proposed first statement (A), refuted in §3.** Fix the trajectory of the brief, with $\beta_j\to\infty$. At one fixed physical base size in the band take admissible sides $n_j\to\infty$ with $a_jn_j$ tending to that size. Ask whether there exist $C>0$, $k\ge0$ and $j_0$, all finite, such that $\sum_S|d_{n_j}(S)|\le Cn_j^k$ for every $j\ge j_0$. Even this polynomial allowance is weaker than the cutoff-uniform bound an absolute estimate would need at the base. A successful seed argument would also need a gain on subsequent doublings.

**ARGUED — Comparisons and precedent.** The nearest item in brief §5 is contraction by class-wide tools (RA/RB). Absolute surface sums in §3 suggest the counting step. Here one tests an all-orders, signed, projected-support coefficient of the actual torus defect. In compact U(1) a winding torus already carries the one-dimensional electric character. Its Fourier multiplier approaches one at weak coupling. In a product the full defect adds, and a pure spectator excitation survives any operation on the SU(2) factor. For frozen Q₈ and the binary tetrahedral group the defining representation still propagates around the torus. At deep freeze its normalized multiplier also approaches one. The failing line is polynomial control after taking absolute values across winding supports. Section 3 computes the contributions. The cheapest test is to extrude a winding polygon with independently optional detours around the boundary of one transverse square.

### 2. Sum over different supports before estimating a marked plaquette

**GUIDE — Mechanism.** Choose an independent Bernoulli(t) subset A of base plaquettes, omitting a distinguished p. Use its complete inverse image as the mask upstairs. During an interpolation from the empty set to the full lattice, insert p simultaneously on all sheets. Take the signed average over A before estimating the insertion. This places intersecting and detoured winding sheets in the same expectation. The normalized integrals retain the full matrix group and arbitrary spin. Small t admits a purely geometric estimate. A selective estimate would have to enter once the occupied component of p winds with appreciable probability.

**PROVED — Marked plaquette identity.** Set

$$
b_{j,n}(t)=\sum_{p}\mathbb E_t\!\left[
16\log\langle w_p\rangle_{n,A}
-\log\left\langle\prod_{q:\pi q=p}w_q\right\rangle_{2n,\pi^{-1} A}\right],
$$

where the brackets denote expectation under the indicated normalized masked Wilson law at the same $\beta_j$. The marked difference is $D_n(A\cup\{p\})-D_n(A)$. For a Bernoulli subset $A_t$ on *all* base plaquettes, $\mathbb E_t D_n(A_t)=\sum_S t^{|S|}d_n(S)$. Differentiating with respect to one occupation probability at a time gives

$$
b_{j,n}(t)=\sum_{S\ne\varnothing}|S|t^{|S|-1}d_n(S),\qquad
\int_0^1 b_{j,n}(t)\,dt=\Phi_2(n).
$$

**PROVED — Source of cancellation.** The identity averages over different projected supports *before* the estimate. All 16 lifts of a base plaquette carry the same occupation bit.

**OPEN — First statement (B).** Fix a first-passage base on the physical dyadic grid, with $n_j=L_b/a_j$ integral at all sufficiently fine cutoffs. Take as input a cutoff-uniform bound $\Phi_2(n_j)\le M$ there. Find $\theta\in(0,1)$, $j_0$ and a finite integer $K\ge1$ with $\theta^K M<1.9\,10^{-4}$ such that for every $j\ge j_0$, $0\le k<K$, $n=2^k n_j$ and $0<t<1$,

$$
 b_{j,2n}(t)\leq\theta\,b_{j,n}(t).
$$

**PROVED — Conditional implication.** Integrating and iterating the displayed inequality gives $\Phi_2(2^K n_j)\le\theta^K M$ at physical side $2^K L_b$ for every large $j$. Row 697's Theorems D and S take this as a strict seed. The calculation requires no sign assumption on an individual derivative. Compared with SHEET (row 996), the estimate reads one signed mean over a specified mask law. In the RA/RB families it singles out a finite-volume Haar integral supported on winding components.

**PROVED — Geometric part of (B)'s test.** When the component of p in A ∪ {p} lifts trivially, all factors from components disjoint from it cancel from the insertion. The two remaining integrals agree under the lift, so the marked difference is zero. A component with nontrivial monodromy contains a walk whose lift displaces a coordinate by at least n. Modulo n this walk meets a plaquette centre at circular coordinate distance at least n/2 − 1 from the centre of p in that coordinate. Adjacent centres across an edge differ by at most one per coordinate. For n ≥ 8 there is consequently a simple occupied path from p of at least m = ⌊n/4⌋ − 1 steps. At most 20 plaquettes are adjacent to one plaquette across its four edges in four dimensions. The union bound and |log w| ≤ βⱼ give |bⱼ,ₙ(t)| ≤ 32βⱼ · 6n⁴ (20t)ᵐ. This tests the support and normalization only. For t near one the bound gives no attenuation.

**ARGUED — Where selectivity is required.** For compact U(1) in the Coulomb regime a commutator of winding holonomies is identically one. The missing line is the signed bound (B) once the mask percolates. In any periodic photon model with the specified bounded base and a full-sector thermal floor above the seed threshold, integration and row 697 force (B) to fail for some doubling and density. For the Wilson cosine the particular periodic-seed inference has the scope qualification of rows 786, 794 and 999. For a decoupled product the marked difference adds over factors. In transfer language $\Omega_{\rm SU(2)}\otimes v_{\rm spectator}$ keeps the spectator's excitation energy. Estimating the SU(2) summand alone loses exactly that channel. With the same bounded base, (B) through the stated range would imply a full-sector seed in the product, contradicting any admitted spectator with a thermal floor above it. The free photon supplies the floor in its own normalization. Positive-character coexistence tests any extension to a fixed coupling that dispenses with first-passage data. Its membership in the Wilson trajectory would be a separate premise.

**PROVED — Cheapest frozen-group test for (B).** Set w to the flatness indicator on a finite group H. A spanning tree leaves one root frame, and the flat holonomies are homomorphisms from the torus fundamental group. Fix the $V-1$ tree transports and assign the four commuting holonomies in the rooted frame. Thus $Z=|H|^{V-1-E}\#\operatorname{Hom}(\mathbb Z^4,H)$ for $V$ vertices and $E$ links. The powers proportional to volume cancel, giving $\Phi_2(n)=15\log(\#\operatorname{Hom}(\mathbb Z^4,H)/|H|)$ at every $n$. For each of $Q_8$ and the binary tetrahedral group $2T$, the four generators of $\mathbb Z^4$ can independently map into one chosen cyclic subgroup of order four. This gives at least $4^4$ homomorphisms, exceeding both $|Q_8|=8$ and $|2T|=24$. The defect is strictly positive and constant. Every masked integral remains positive because the all-identity field is available. The finite interpolation therefore gives ∫₀¹(b₂ₙ − θbₙ)dt > 0 for each θ < 1. At least one interior dilution violates (B). On a fixed pair of boxes this persists for sufficiently large finite Wilson β by continuity after restoring the plaquette constant. This tests the exactly frozen law and its finite-box neighbourhood. Section 4 gives the single-deletion test for the Wilson law.

## 3. Hand test of (A) on the actual four-dimensional Wilson tori

**PROVED — Counterexample.** For any βⱼ → ∞ and any integers nⱼ → ∞, the exact projected-support coefficients obey

$$
 \liminf_{j\to\infty}\frac{1}{n_j}\log
 \sum_{S\subseteq P(\Lambda_{n_j})}|d_{n_j}(S)|
 \ \ge\ \frac{\log 2}{3}.
$$

This includes $a_jn_j$ tending to a prescribed finite physical size. A cutoff-uniform upper estimate at that size must allow cancellations between different projected plaquette supports. The proof uses the character gluing of two-dimensional lattice gauge theory (Migdal's character expansion) on an embedded subcomplex of the four-torus.

**PROVED — A family with known monodromy.** For n ≥ 6 take the straight loop along coordinate 1 in the first two-torus at height zero. Select any subset J of the horizontal edges starting at 0, 3, …, 3(⌊n/3⌋−1). Replace each selected edge by the three other sides of the unit square immediately above it. The separation of the chosen sites, including across the periodic seam, keeps the resulting polygon $\gamma_J$ simple. Its length is $n+2|J|$ and its winding is $(1,0)$. In coordinates 3 and 4 take $C$ to be the boundary of a single square. The distinct supports $S_J=\gamma_J\times C$ are embedded square tori of area $A=4(n+2|J|)$. The subgroup of deck translations traced by their loops has order two, generated by translation by n in coordinate 1. The inverse image of $S_J$ therefore consists of eight disjoint square tori of area 2A. The same count follows by choosing a transverse lift of C (four choices) and a lift of the height of the polygon (two choices). Its longitudinal lift takes two turns to close.

**PROVED — Proper subsets have zero defect.** Let c₀ = ∫w(g)dg, with probability Haar measure. The dual graph of each of these tori is connected. Every proper nonempty subset of faces therefore has an edge from an occupied face to an unoccupied one. Integrating that link removes exactly the incident occupied face at cost c₀, by Haar invariance. Repetition gives c₀ to the power of the number of occupied faces. On each of the eight covering tori, the inverse image of a proper subset also omits a face. Its partition function has the same single-face factors, so $D_n$ vanishes on every proper subset of $S_J$. In particular $d_n(S_J)=D_n(S_J)$ in the inclusion–exclusion expansion of the full four-dimensional free energy.

**PROVED — The whole support.** Write $w/c_0=\sum_\rho d_\rho r_\rho\chi_\rho$, with $d_\rho$ the degree and $r_{\mathbf 1}=1$ for the trivial representation. For SU(2), expanding exp(β_W χfund/2) into tensor powers gives nonnegative character coefficients. The sum with each character replaced by its degree is finite by evaluation at the identity, so termwise integration is justified. Also rᵨ ≤ 1 by |χᵨ| ≤ dᵨ. Orient an embedded torus consistently. At an edge the two incident faces traverse it in opposite directions. Schur orthogonality identifies their irreducible labels and the two matching pairs of indices, with factor 1/dᵨ. Connectedness makes the label common to the whole surface. The index identifications around each vertex leave one free index because its link is one circle. Thus each label contributes $d_\rho^{V-E+A}r_\rho^A$. Since $V-E+A=0$, the partition function divided by $c_0^A$ is $Q(A)=\sum_\rho r_\rho^A$. This computes the entire signed surface sum on that support.

**PROVED — The uncancelled contribution.** Let r be the fundamental multiplier. Since Q(2A) ≤ Q(A), the eight lifts give

$$
 d_n(S_J)=16\log Q(A)-8\log Q(2A)
       \ \ge\ 8\log(1+r^A)\ \ge\ 4r^A.
$$

The last inequality integrates 1/(1+x) ≥ 1/2 on [0,1]. Summing only the displayed family of supports gives the explicit lower bound

$$
 4r^{4n}(1+r^8)^{\lfloor n/3\rfloor}.                 \tag{1}
$$

For $x(g)=\operatorname{Re}\operatorname{Tr}(g)/2$, $r$ is the mean of $x$ under the normalized weight $e^{\beta_W x}$. For $0<\varepsilon<1$ the tilted probability of $x\le1-\varepsilon$ is at most $e^{-\beta_W\varepsilon/2}$ divided by the positive Haar mass of $x\ge1-\varepsilon/2$. Hence r → 1 as β_W → ∞. Taking the logarithm of (1) and dividing by n proves the claim, without a rate relation between n and β_W. Already at a fixed β_W for which r¹²(1+r⁸) > 1, (1) grows exponentially. This last condition is a sufficient test. No value at the effective crossover is assumed.

**PROVED — Cancellation between different supports.** At fixed $\beta_W$ and $0<t\le1$, the contribution of these tubes to $b_n(t)$ is at least $4n/t$ times the right side of (1) evaluated at $t\,r$. This follows from $|S_J|\ge4n$ in the marked-generator identity. The direct bound is $|b_n(t)|\le192\beta_W n^4$. Consequently whenever $(t\,r)^{12}(1+(t\,r)^8)>1$, other projected supports must cancel an exponentially large positive contribution. What remains to prove in (B) is a signed comparison of the two *net* marks after this cancellation.

**PROVED — Group checks of the counterexample.** For compact U(1) with w = exp(β cos α), the two conjugate unit charges have multiplier tending to one by the same cap estimate. Their Fourier coefficients are nonnegative by expansion of the exponential. Both frozen groups have an irreducible defining doublet (the two quaternion generators have no common eigenline), and x = 1 only at the identity. The tensor-power expansion and the finite sum give r → 1 there as well. On a decoupled SU(2) × U(1) product the two factors' projected-support coefficients for each tube are nonnegative and add. These are explicit failures of the same absolute bound in the comparison regimes. They use arbitrarily weak coupling or deep freeze, independently of the numerical crossover locations.

**GUIDE — Which representations matter.** Row 838, Lemma F1, identifies the first distinguishing moments for Q₈ and the binary tetrahedral group at degrees four and six, respectively, reaching spins 2 and 3. The signed mark in (B) retains those channels. Turning their different Haar moments into a quantitative difference across a percolating component remains open. [Row 838, §3.1](gap-assume-opus.md)

## 4. Comparison with the recorded routes

**GUIDE — Two distinct defects in the source.** The brief writes $\Phi_4$ for $16F(n)-F(2n)$. Row 720, lines 247 and 276, defines $\Phi_\rho(n)=\rho^4F(n)-F(\rho n)$, so doubling is $\Phi_2$ and quadrupling is $\Phi_4$. This report uses row 720's convention. Also, row 708's literal (CAS) contracts the excess $\Delta(n)=F(n)-f n^4$. From the uniform base $\Delta(n_j)\le M_\Delta$ one gets $\Phi_2(n_j)\le16M_\Delta$, since $\Phi_2(n)=16\Delta(n)-\Delta(2n)$ and $\Delta\ge0$. This base is a premise. Row 978's stability input has its own conditions. Equation (B) contracts $\Phi_2$ and reaches row 697's Theorem D(b) through its bound $1+S(n;(2n)^3)\le e^{\Phi_2(n)}$. This avoids inferring literal (CAS) over a bounded range from a comparison of finite defects. I credit the gap authors of rows 697, 708 and 720 for these consumers and Ursachi for the doubling-defect idea as credited in row 697. [Row 697, §§1, 3.1, 3.4](gap-crux-restate.md) · [Row 708, C-B](gap-mid-max.md) · [Row 720, §3](gap-phys-seed.md) · [Row 978, §5.2](gap-ladder-max.md)

**ARGUED — Attack 1 revisits absolute surface estimates. The counterexample for these coefficients is new in the reviewed rows.** Rows 811/816 already sum spin labels and vacuum decorations before bounding an odd-flux surface. Their single flat plane rules out the particular $400q<1$ budget at $\beta_W=1/2$. Their rooted estimate (J12) concerns a dressed odd-sector ratio. Row 833 and check 847 pay surface entropy at strong coupling. Row 838, §3.8, explicitly proposed testing independently decorated sheets and called its roughening ceiling a guide. I reuse both the entropy test and the torus Schur sum. Here the full periodic log defect is grouped by projected *bare plaquette support*. Each tube bounds the three-chain $\gamma_J\times[0,1]^2$ in the ambient lattice. Its mod-two two-dimensional homology class is zero even though a longitudinal circuit changes cover sheet. This family contributes to the vacuum defect in a channel missed by an odd-flux selector. I found no previous evaluation of this grouped norm or of (1) in the named rows. The counterexample decides (A). Row 811's (J12) remains open in the window. [Rows 811/816, §§3–4](gap-joint-astra.md) · [Row 833](gap-rtailsos-opus.md) · [Row 838, §3.8](gap-assume-opus.md)

**PROVED — Exact limitation at fixed bare coupling.** For the same tubes the sum of the *actual* $d_n(S_J)$ decays exponentially throughout $0<\beta_W\le13/5$. To check this without numerical Bessel values, let $d=2j+1$ be the degree of a spin and let $I_m$ be the $m$th Fourier coefficient of $\exp(\beta_W\cos u)$. The SU(2) character is $\sin(du)/\sin u$, with class Haar density $2\sin^2u/\pi$. Integrating $\sin(du)\sin u\,e^{\beta_W\cos u}$ by parts gives the character coefficient $2d I_d/\beta_W$, hence $r_j=I_d/I_1$. The Fourier series of $\exp[\beta_W(z+z^{-1})/2]$ gives

$$
 I_m=\sum_{h\ge0}\frac{(\beta_W/2)^{2h+m}}{h!(h+m)!},\qquad
 \frac{I_{m+1}}{I_m}\le\frac{\beta_W}{2(m+1)}\le q:=\frac{13}{20}
 \quad(m\ge1).
$$

Consequently $r_j\le q^{d-1}$ and $Q(A)-1\le q^A/(1-q)$. Summing $0\le d_n(S_J)\le16\log Q(A)\le16q^A/(1-q)$ gives

$$
 \sum_J d_n(S_J)\le \frac{16}{1-q}\,
 q^{4n}(1+q^8)^{\lfloor n/3\rfloor}.
$$

Here $q^{12}(1+q^8)<2(2/3)^2<1$. Thus these tubes alone are exponentially small at fixed Wilson coupling in the specified band. The effective action at first passage requires its own estimate.

**ARGUED — Attack 2 gives a new interpolation within the existing contraction route.** Row 697, Theorem D(f), already integrates the difference of mean plaquette actions over a common *coupling*. Rows 708 and 998 already ask for a selective contraction. Methods 7–8 (rows 754, 756, 760 and 767) test association, separate-volume finite-radius loop equations and coupled certificates. Methods 19–21 (rows 970, 977, 996 and 997) test suprema over tilts and deterministic coupling fields. Method 34 (rows 845, 852, 895, 896 and 1118–1123) tests stationary block paths, pinned-cell means or replica differences. Here there is one sample of independent occupation bits on the base, lifted to the cover, with a nonlinear difference of *normalized log insertions* from two exact integrals. No coupling of independently sampled Gibbs fields or supremum over their boundary pins is taken. Row 794 mentions diluted Villain comparison for an abelian observable. Row 986 reports Möbius localization for a three-dimensional Gaussian determinant. Neither has the signed derivative of this four-dimensional Wilson cover defect. In the crux, registry, test table, methods 1–34 and their relevant RESULT entries, I found no prior test of this specific $b_{j,n}$. Its percolating-mask inequality is stronger than the integrated comparison and still lacks a Wilson supplier. [Route registry and test table](../parts/gap.md) · [Methods 1–18](gap-crux-exercise2-max.md) · [Methods 19–33](gap-crux-exercise3-max.md) · [Method 34, scope corrections](gap-l3-closure-check-astra.md) · [Queue results](../FINISH.md)

**PROVED — Cheapest necessary Wilson test for (B).** Continuity of the finite mask polynomial extends (B) to $t=1$. For positive Wilson weights this endpoint needs just one deleted base plaquette and its 16 translates. Write full-volume expectations without the mask subscript. Division of the full and deleted partition functions gives

$$
 b_{j,n}(1)=
 \sum_{p\in P(\Lambda_n)}
 \log\frac{\left\langle\prod_{q:\pi q=p}w_q^{-1}\right\rangle_{2n}}
               {\left\langle w_p^{-1}\right\rangle_n^{\,16}}.
$$

For example, a sequence of admissible doublings at arbitrarily fine cutoffs with $b_{j,n}(1)\le0<b_{j,2n}(1)$ would refute every positive $\theta$ for that range. For the strictly frozen finite groups use the original deletion formula, because $w$ can vanish. The five other faces of a cube fill the boundary of the omitted plaquette. If those faces are flat, the omitted plaquette is flat. Distinct lifts of the omitted plaquette lie in distinct such cubes for $n\ge3$. Hence both insertions in the original formula equal one at $t=1$. The frozen test in §2 forces failure at an *interior* density even though this endpoint agrees exactly.

**OPEN — Decision after the tests.** The unresolved comparison is the signed marked insertion on two successive covers, uniform in the cutoff through the needed doublings. In the Coulomb diagnostic, the periodic Villain result and the Wilson-cosine transfer have different premises (rows 786, 794 and the corrections to row 998). A spectator that violates the full-sector seed identifies the missing summand in a factor-only argument. Deep freeze disproves a group-blind form of (B) by direct finite-group algebra. None of these comparisons settles (B) on the SU(2) trajectory. [U(1) transfer check](gap-tu-check-opus.md) · [Frozen even-sector check, §7](gap-crux-exercise2-check-astra.md) · [Council test table](../parts/gap.md)

## 5. Result

**PROVED — Check of the factor of eight without character integration.** For a finite group $H$ at exact flatness, a rooted flat connection on a square torus is specified by tree transports and a commuting pair. The number of pairs is $\sum_{g\in H}|C_H(g)|=|H|k(H)$, where $k(H)$ is the number of conjugacy classes. Since $V-E=-A$ on the tube and $c_0=1/|H|$, division by $c_0^A$ gives $k(H)$ on each connected torus, irrespective of area. The disjoint cover gives 16 such factors and the connected cover restricted to the tube gives eight. Its log coefficient is therefore $8\log k(H)$, confirming both the sign and the lift multiplicity in the frozen control.

RESULT: PROVED by hand that the absolute sum over projected bare plaquette supports grows at exponential rate at least $(\log 2)/3$ per unit side along $\beta_j,n_j\to\infty$. The same tube family is exponentially small at fixed Wilson $\beta_W\le13/5$ with $\beta_W>0$. OPEN is the signed comparison between different supports on percolating masks in the first-passage band. The physical seed remains open.
