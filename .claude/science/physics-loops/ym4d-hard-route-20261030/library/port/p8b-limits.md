# P8, part 2: Limits and the curvature Hilbert space

Provenance: Codex (GPT-6 family; effort not exposed), 2026-11-05, checkout `e7a21cd9840a76989e21a00b1a733d1c2c2b1893`. Research text, not an audit; grants no status. Written by hand; not yet checked by another model.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account and outline at `31a47c543775`; Tadeusz Balaban for the lattice gauge theory and renormalisation results they use. This follows their route. Added steps are marked **(filled)**; repairs are marked **(correction)**.

This continues tranche 7 of `../chain-ca.md`, rows B10–B13. Part 1, `p8-positivity.md`, already ports B5, B7 and B8 and is not redone here. Every unproved input remains a named hypothesis.

## 1. Sources, standing, and the conditional interface

`I:L` and `II:L` mean lines of `theorem_0_complete_account_raw_I.tex` and `theorem_0_complete_account_raw_II.tex` at `31a47c543775`. `SA:L` means `YM4_sketch_500.tex` at that revision. The existing `/tmp/sa_ca_I.tex`, `/tmp/sa_ca_II.tex`, and `/tmp/sa_ym4.tex` supply the bounded excerpts. They were already fetched for the preceding ports; their SHA-256 values match the pinned identities recorded in P3. This is source bookkeeping only. This round does not read a whole CA file or redo part 1.

The source convention is I:27–46. Each requested numbered heading below is unqualified and followed by a proof. Its **source status is proved implication**. This describes the source's declaration, not a check of this port. The exact statements, including their labels and hypotheses, are transcribed in §14. The proofs here follow those statements in dependency order. A cross-reference in a source statement retains its hypotheses; it is not an assertion that they have been supplied.

GOAL.md, its method section, the requested FINISH sections, `chain-ca.md` A14 and §7.2, and `port-map.md` were read first. The outline index was searched before source excerpts. The neighbouring rows in `sa-index/chunk-22.md`, `chunk-23.md`, and `obligations.md` locate SA:24541–24718 and 25435–25647. Those passages give support-adapted extraction, moving tests, positivity, and the compact reconstruction. They are comparison passages; the proofs below port the complete account. The CA index locates II:65519–68080. In particular, II:67787–68079 completes clause (D) of B11 after the requested B13 range. We include that continuation so that B11 is not left with an unproved conclusion. I:2698–2711 fixes the scope.

The workflow and scoped-worker skill are absent from this sparse checkout. Their copies were read through git at local `origin/main`, `f5af11cd0102cfd0b51aef0911f600130bf5beb1`, together with the skill-freshness rule. These procedural sources supply no science. The pinned task and its narrower output rule govern this handoff. No worker, audit, numerical job, or independent check was launched.

### 1.1 Repository inputs

Use the owner's current standings, including where an older file header records an earlier round:

* [P1](p1-base.md), [P3](p3-free.md), [P4](p4-operator.md), [P5](p5-induction.md), and [P7](p7-torus.md): **checked ports**, each with its named hypotheses. P7 ports A14; its seven inputs are not discharged by its title.
* [P6](p6-correlation.md): **ported, not yet checked**. Its B3 is `5.1:thm-correlation-theorem`, II:2791–2966. Its source and weight hypotheses remain attached.
* [LSC](../lsc.md): **frozen**, including the round-2 freeze at its end. Its last-scale bounds use the common vacuum normalization. They retain the representation, flow, real-background, vacuum-energy, sourced/source-free matching, and eight sourced-upper-bound inputs stated there.
* [mu](../mu.md), [lrb](../lrb.md), [oc](../oc.md), [ui](../ui.md), and [pda](../pda.md): **refereed** inputs available to the lane. We do not infer a new interface from their titles. No extra conclusion from these files is used below.
* [P8 part 1](p8-positivity.md): **committed port, not yet checked by another model**, as its provenance and Result say. We use B5 and the conditional B7 bound. Its B8 proof is not repeated.

### 1.2 Named hypotheses retained

**H-CA.** Retain the standing SU(2) data and (H1)–(H7) of `7.1:not-torus-cumulants`, II:64632–64686, and the correlation theorem B3 at P6's standing. Retain its source/weight antecedents, including the outstanding window-data statement at II:2810–2812 and `5.6:prop-polydisc-holomorphy` at II:46167. Nothing in a limit argument proves them.

**H-FLOW.** Fix odd $L\ge L_0$, then $\mathfrak p,\gamma,\gamma_H$, with source radius $r>0$ fixed before its source threshold. Let
\[
0<g\le\min\{\gamma_H,\gamma_J(L,\mathfrak p,r)\},\quad
g_0^{(j)}\in(0,g_-(g)],\quad g_0^{(j)}\downarrow0,
\]
\[
K_j=K(g_0^{(j)},g)\longrightarrow\infty,\qquad
m_j\longrightarrow\infty,\quad m_j\ge m_{\mathbb T}(g_-(g)).
\tag{1}
\]
The first-passage conclusion is the clause-(0) input, not a new theorem about this trajectory. P1 supplies its conditional arithmetic; the actual running flow and torus independence retain P5/P7's antecedents.

**H-PB.** For every $n\ge2,d,R>0$, the real separated torus cumulants satisfy
\[
 |S^T_{n;K,m}(h_1,\ldots,h_n)|
 \le C_n^\infty(d;R)\prod_i\|h_i\|_\sharp
\tag{2}
\]
at admitted first-passage cutoffs and above the volume floor $m_*(n,R,g)$. Each support lies in its own ball of radius $R$, with arbitrary centre, and all support distances are at least $d$. The constant and floor are independent of the cutoff, bare coupling, volume, and support positions. This is the precise B7 interface consumed here.

For the literal CA statement, $m_* =\max\{m_{\mathbb T}(g_-(g)),\log_L\ell(n,R,g)\}$. For the repository application, use part 1 §5.4: the finite maximum over the LSC offsets, its Case-B local count, and, if using that sufficient floor, $L^{m}\ge L^{m_J}\ell(n,R)$. Relabel the resulting constant $C_n^\infty$. **(correction: inherited admission and normalization.)** The application retains $g\le\gamma_D$ wherever LSC requires it and the transported volume floor; it does not drop either because the source theorem prints a shorter list. These fixed extra floors are eventually met in (1). The common factor $e^{-E_{\rm vac}}$ cancels from normalized expectations and from every mixed derivative of the logarithm. No bare partition-function floor is asserted. H-PB retains part 1's H-LOC, H-DOM, H-STAB/LSC, and Balaban CMP 116 (1.26), its H-TREE. We do not re-prove them.

**H-RP.** The finite Wilson measure is invariant and reflection positive for the plane pair $x^0=0,L^m$, on bounded measurable functions of bonds in the open positive slab. This is B5 of part 1, in the centred half-integer lattice convention used below. No site-reflection or arbitrary-Gibbs-state extension is assumed.

**H-BLOCK.** Retain B11 hypothesis (d) exactly. There is a countable family $\mathcal T^\vee$ of block/smeared observables. Each expectation is eventually defined and bounded along (1). On every infinite subset where all these expectations converge, their cutoff-uniform density construction supplies a joint state $\omega_\infty$ on $\mathfrak A^\tau_{\rm loc}\otimes\mathfrak A^{\rm sm}_{\rm loc}$. This is a named input, not a consequence of curvature cumulant bounds. No mixed block/curvature bound is included.

The following analysis inputs are also named, as the account does at II:65780–65842. They are not rebuilt here:

* **H-AN:** completeness of the real and complex numbers; compactness of closed bounded sets in finite dimension; countable choice; elementary multivariable calculus, convergent power-series calculus, integration and dominated convergence for finite measures; normalized Haar measure with inversion and translation invariance; existence of smooth compact cutoffs and finite smooth partitions of unity; completion of an inner-product space. The concrete countability, diagonal, algebraic, and continuity arguments used below are written out.
* **H-KER:** the $n$-fold Schwartz kernel theorem for separately continuous multilinear forms on $\prod_i\mathcal D(V_i)$, with uniqueness; gluing compatible distributions on open covers; tensor products of distributions in disjoint variable sets and their continuity. The source states the kernel/gluing inputs at II:65808–65820. Our local estimates, tensor density, compatibility, and positive-time use are proved below.
* **H-FOURIER:** a smooth function compactly supported inside a period box equals its Fourier series, with convergence in every derivative. The coefficient and summability estimates needed here are filled below. This is the Fourier input of II:65822–65830.
* **H-SPEC:** the spectral theorem and measurable functional calculus for self-adjoint operators, uniqueness of positive square roots, SNAG for a strongly continuous unitary representation of $\mathbb R^3$, and its commutant and joint-spectral-measure conclusions (II:65834–65840). The semigroup construction, its injectivity, its domain, and its continuity are proved below, rather than assumed as a semigroup theorem.

All subsequent conclusions are implications from these inputs. The exact source theorem and the admitted repository version are distinguished above.

## 2. B10: finite conventions and algebra

**`7.4:not-finite-cutoff`, II:65519–65659; source status: definition with proof.** Put
\[
\mathbb T_m=\mathbb R^4/(2L^m\mathbb Z^4),\quad \varepsilon=L^{-K},\quad
\Lambda_{K,m}=q_m\bigl(\varepsilon(\mathbb Z+\tfrac12)^4\bigr).
\]
Here $m\ge1,K\ge0$, and $q_m$ is the quotient map. Bonds retain their periodic edge labels. Plaquettes have barycentres $x(p)$. A configuration assigns $U(b)\in SU(N)$, with $U(-b)=U(b)^{-1}$. In the final theorem $N=2$. Use normalized trace and product Haar measure:
\[
a_p=1-\operatorname{Re}\operatorname{tr}U(\partial p),\quad A=\sum_pa_p,
\quad d\mu_{K,m}=Z_{K,m}(0)^{-1}e^{-g_0^{-2}A}\,dU,
\quad\mathcal O(h)=\sum_ph(x(p))a_p.
\tag{3}
\]
The representatives in $(-L^m,L^m)^4$ are unique: in each coordinate the site indices are $-L^{m+K},\ldots,L^{m+K}-1$. Normalized traces of unitary matrices have real part in $[-1,1]$. Thus $0\le a_p\le2$; cyclic relabelling and reversal of a plaquette leave $a_p$ fixed. There are finitely many plaquettes, say $P$, so $|\mathcal O(h)|\le2P\|h\|_\infty$ and $Z_{K,m}(0)>0$.

The source integral is
\[
 Z_{K,m}(z;\vec h)=\int e^{-g_0^{-2}A+\sum_i z_i\mathcal O(h_i)}\,dU.
\]
Its exponential series converges uniformly on compact source sets by the preceding bound. Termwise integration makes it entire. Continuity and its positive value at zero give a zero-free neighbourhood there. Define
\[
 S^T_{n;K,m}(\vec h)=\partial_{z_1}\cdots\partial_{z_n}
       \log Z_{K,m}(0;\vec h)=\kappa_n(\mathcal O(h_1),\ldots,\mathcal O(h_n)).
\tag{4}
\]
The identity follows by writing $Z(z)=Z(0)\langle e^{\sum z_i\mathcal O(h_i)}\rangle$. Multiplication of $Z$ by a positive source-independent constant leaves (4) unchanged. The exponent is $-\sum_p(g_0^{-2}-\sum_i z_i h_i(x(p)))a_p$, which fixes the additive source convention.

For real $f\in C_c^1(\mathbb R^4)$, set
\[
 \|f\|_\sharp=\max\{\|f\|_\infty,40M\|\nabla f\|_\infty\},\qquad
 \mathfrak S_n=\{(f_i)_{i=1}^n:\operatorname{supp}f_i\text{ pairwise disjoint}\}.
\]
On the torus replace the gradient norm by the flat-metric Lipschitz constant. On $\mathbb R^4$, the fundamental theorem along a segment proves $\operatorname{Lip}f\le\|\nabla f\|_\infty$. Difference quotients in the unit gradient direction prove the reverse inequality. A finite collection of nonempty disjoint compact supports has a positive minimum distance. Empty supports have distance $+\infty$. Zero entries vanish in every multilinear expression.

**(filled: the moment/cumulant input, II:65792–65806.)** For bounded $X_1,\ldots,X_q$, work in the finite commutative algebra with $z_i^2=0$. Then
\[
 M(z)=\mathbb E e^{\sum_i z_iX_i}
 =\sum_{B\subset[q]}\mathbb E\!\prod_{i\in B}X_i\ z_B,
 \qquad \log M=\sum_{\varnothing\ne B\subset[q]}\kappa(X_B)z_B.
\]
Both exponential and logarithm terminate after degree $q$. Their coefficients agree with the mixed derivatives of the analytic functions, since every retained variable has degree at most one. In $\exp(\log M)$, the coefficient of $z_{[q]}$ is a sum over disjoint nonempty blocks covering $[q]$. Ordering $k$ blocks gives $k!$ copies, cancelled by $1/k!$. Hence
\[
 \mathbb E\prod_iX_i=\sum_{\pi\in\operatorname{Part}[q]}\prod_{B\in\pi}\kappa(X_B).
\tag{5}
\]
Conversely, the logarithm series gives
\[
 \kappa_q(X_1,\ldots,X_q)
 =\sum_{\pi\in\operatorname{Part}[q]}(-1)^{|\pi|-1}(|\pi|-1)!
                      \prod_{B\in\pi}\mathbb E\prod_{i\in B}X_i.
\tag{6}
\]
Each index occurs once in each summand, proving multilinearity, permutation symmetry, and reality on real inputs. Replacing $X_i$ by $X_i+c_i$ multiplies $M$ by $e^{\sum z_ic_i}$; its logarithm changes only in degree one. Thus all cumulants of order at least two are shift invariant. For centred variables, singleton blocks in (5) vanish.

## 3. B10: transport to a common torus chart

**`7.4:lem-torus-transport`, II:65661–65767. Source status: proved. Exact statement: §14.1.** For $L^m\ge2\rho+2$, transport a compactly supported Lipschitz $f$, with support inside the open $B_\rho$, by
\[
 f^{(m)}(q_mx)=f(x)\ (x\in B_\rho),\qquad f^{(m)}=0\text{ off }q_m(B_\rho).
\tag{7}
\]
This preserves its sup and Lipschitz norms, support distances, containing ball radii, and admitted translations and signed permutations.

**Proof.** If $x,y\in B_\rho$ and $k\in\mathbb Z^4\setminus\{0\}$,
\[
 |x-y+2L^mk|\ge2L^m-2\rho\ge2\rho+4>|x-y|.
\]
Thus $q_m$ is isometric on $B_\rho$, and globally is 1-Lipschitz. Formula (7) is unambiguous and preserves the supremum. Choose $\rho'<\rho$ with $\operatorname{supp}f\subset B_{\rho'}$. For two points of $q_m(B_\rho)$, their lifts give the Lipschitz bound. If one point has nonzero value and the other lies outside this chart, choose a shortest lift from the first to the second. Its straight segment exits $B_{\rho'}$ at $x^*$, where $f=0$. The length to $x^*$ is no longer than the full distance, so
\[
 |f(x)|=|f(x)-f(x^*)|\le\operatorname{Lip}f\,d_{\mathbb T}(q_mx,\eta).
\]
If both values vanish the bound is immediate. This proves the torus Lipschitz upper bound. The same exit-segment argument in Euclidean space shows that the global Lipschitz supremum of $f$ can be taken over pairs in $B_\rho$; isometry gives the reverse bound.

Continuity and compactness give $\operatorname{supp}f^{(m)}=q_m(\operatorname{supp}f)$. Taking infima of the isometric point distances proves exact support-distance preservation, including empty supports. If the support lies in $B(x,R)$, the global 1-Lipschitz property places its image in $B_{\mathbb T}(q_mx,R)$.

Let $\tau_af=f(\cdot-a)$, and suppose both original and translated supports lie in $B_\rho$. The nonzero locus of $\tau_{q_ma}f^{(m)}$ is the image of the translated nonzero locus. On that locus the unique lifts in $B_\rho$ give $(\tau_af)^{(m)}=\tau_{q_ma}f^{(m)}$; elsewhere both sides vanish. More explicitly, a purported nonzero value from a different periodic lift would give two distinct lifts of a point of the translated support inside $B_\rho$, contradicting injectivity. A signed permutation $w\in W_4$ preserves the period lattice and $B_\rho$. Evaluation at $q_mx$ gives $(w\cdot f)^{(m)}(q_mx)=f(w^{-1}x)=(w\cdot f^{(m)})(q_mx)$. Both vanish outside the chart. Taking $w=\theta$ proves the reflection identity. Transport is also linear by (7), and independent of an enlarged chart radius once both charts are admitted. ∎

## 4. B10: lattice symmetries and the positive slab

### 4.1 Exact lattice symmetries

**`7.4:lem-lattice-symmetries`, II:65844–65927. Source status: proved. Exact statement: §14.2.** For $b\in\varepsilon\mathbb Z^4$ modulo periods and $w\in W_4$, the three vectors of observables at $\tau_b\vec h,w\cdot\vec h,\vec h$ have the same joint law. In particular their means and cumulants agree.

**Proof.** Translation by $b$ preserves the site set and plaquette incidence. **(correction)** II:65871 says that translation sends the period lattice onto itself. This is generally false for a nonperiodic $b$. The needed assertion is that it preserves the equivalence relation: $(x+\lambda)+b=(x+b)+\lambda$. This proves that it descends to the quotient. Relabel $p=p'+b$; barycentres translate by $b$, and
\[
 \mathcal O(\tau_bh)(U)=\sum_{p'}h(x(p'))a_{p'+b}(U)
                       =\mathcal O(h)(U\circ\tau_b).
\tag{8}
\]
The configuration map permutes bond variables and plaquettes, preserving product Haar measure and $A$, hence $\mu_{K,m}$.

For a signed permutation, $-(k+\tfrac12)=(-k-1)+\tfrac12$ preserves the site convention. Put $(w\cdot U)(b)=U(wb)$, inverting a variable when its oriented bond is reversed. Haar inversion invariance and bond permutation preserve $dU$. The holonomy of an image plaquette differs only by cyclic relabelling or inversion, so $a_{wp'}(U)=a_{p'}(w\cdot U)$, and $A$ is invariant. Relabelling $p=wp'$ gives
\[
 \mathcal O(w\cdot h)(U)=\mathcal O(h)(w\cdot U).
\]
The same measure-preserving configuration map works for every entry of each vector. Integration against any bounded function of that vector proves equality of joint laws. Means and (6) then prove every asserted identity. ∎

### 4.2 Positive-time observables read only the open slab

**`7.4:lem-half-space`, II:65929–66046. Source status: proved. Exact statement: §14.3.** Let $\operatorname{supp}h\Subset B_\rho\cap\{x^0>0\}$, with $L^m\ge2\rho+2$, and $H_+=q_m\{0<x^0<L^m\}$. Every plaquette with $h^{(m)}(x(p))\ne0$ has all bonds in $H_+$, at time-distance at least $\rho+1$ from the antipodal plane. The raw and centred observables are bounded functions of these bonds. Reflection transports the observable and its mean exactly.

**Proof.** Lift such a plaquette to a bare square whose barycentre is $y\in B_\rho$ with $h(y)\ne0$. A period translation achieves this without changing the lattice. Thus $0<y^0<\rho$. A time-spatial square has corner times $(k+\tfrac12)\varepsilon,(k+\tfrac32)\varepsilon$ and barycentre time $(k+1)\varepsilon$. Its positivity forces $k\ge0$. Its bonds therefore have times at least $\varepsilon/2>0$, and less than $\rho+\varepsilon/2\le\rho+1$. A spatial square has constant time $y^0\in(0,\rho)$. Since $L^m\ge2\rho+2$, every such bond lies strictly inside the slab and has distance at least $\rho+1$ from its antipodal boundary. Periodic projection cannot introduce a crossing because this whole time interval lies inside the chosen slab.

The observable is a finite sum of bounded continuous functions of those bonds. Subtracting its finite expectation adds only a constant. Reflection preserves the lattice, maps barycentres to barycentres, and gives $a_p(\theta\cdot U)=a_{\theta p}(U)$. Hence, by relabelling and (7),
\[
 \mathcal O(h^{(m)})(\theta\cdot U)
 =\mathcal O(h^{(m)}\circ\theta)(U)
 =\mathcal O((h\circ\theta)^{(m)})(U).
\tag{9}
\]
The measure is reflection invariant by §4.1 (also H-RP). Integration proves equality of the two means. Subtraction therefore commutes with reflection. ∎

## 5. B10: the sharp translation modulus

**`7.4:lem-translation-modulus`, II:66048–66144. Source status: proved. Exact six-part statement: §14.4.** For $f\in C_c^1$, define
\[
 \omega_{\nabla f}(u)=\sup_{|x-y|\le u}|\nabla f(x)-\nabla f(y)|,
 \quad \varpi_f(u)=\max\{u\|\nabla f\|_\infty,40M\omega_{\nabla f}(u)\}.
\]
Then
\[
 \|\tau_af-\tau_bf\|_\infty\le|a-b|\|\nabla f\|_\infty,
\quad \operatorname{Lip}(\tau_af-\tau_bf)\le\omega_{\nabla f}(|a-b|),
\quad \|\tau_af-\tau_bf\|_\sharp\le\varpi_f(|a-b|)\longrightarrow0.
\tag{10}
\]
Translations preserve the sharp norm. For $f\in C_c^2$, $\omega_{\nabla f}(u)\le u\|\nabla^2f\|_\infty$. All these estimates survive transport into a common admitted chart. The vanishing modulus fails for general Lipschitz tests.

**Proof.** Integrate $\nabla f$ along the segment between $x-a$ and $x-b$ for the sup estimate. The gradient of their difference is $\nabla f(x-a)-\nabla f(x-b)$. The equality between gradient supremum and Lipschitz constant, proved in §2, gives the second estimate. A compactly supported continuous gradient is uniformly continuous: on a compact ball containing its support and a unit collar this follows from a finite subcover of continuity neighbourhoods; outside that ball both gradients vanish for distances at most one. Thus $\omega_{\nabla f}(u)\to0$, proving (10). For $C^2$ tests, integrating the Hessian along the same segment gives the stated rate. Translation is an onto isometry, preserving each norm. Linearity and norm preservation of (7), applied to the difference, prove all transported assertions.

For the counterexample take $f(x)=|x_1|\chi(x)$, where $\chi\in C_c^1$ equals one in $B_r$. It is Lipschitz: if $\operatorname{supp}\chi\subset B_R$, write $f=\chi\min\{|x_1|,R\}$, a product of bounded Lipschitz functions. For $0<|s|<r$, $g_s=\tau_{se_1}f-f$ satisfies $g_s(0)=|s|$ and $g_s(se_1)=-|s|$. Consequently $\operatorname{Lip}g_s\ge2$ and $\|g_s\|_\sharp\ge80M$. This is a hand counterexample, not a numerical probe. ∎

## 6. B10: centred moments and tensor-presentation independence

**`7.4:def-centred-moments`, II:66152–66207. Source status: definition with proof.** For separated torus sources, (5) and shift invariance give exactly
\[
 S_{q;K,m}(\vec h)=\left\langle\prod_{i=1}^q
        [\mathcal O(h_i)-\langle\mathcal O(h_i)\rangle]\right\rangle
 =\sum_{\pi\in\operatorname{Part}_{\ge2}[q]}\prod_{B\in\pi}S^T_{|B|;K,m}(\vec h_B).
\tag{11}
\]
Every subtuple remains separated. For $q=0$, the empty partition contributes one; for $q=1$, there are no permitted partitions, so the result is zero. Transport preserves the separations, proving the Euclidean-test version.

**`7.4:lem-linearity`, II:66209–66332. Source status: proved. Exact statement: §14.5.** Let $\mathsf F_q(\rho)$ be the span, as actual functions, of Lipschitz compact tensors supported slotwise in $B_\rho$. Write $\hat x(p)$ for the unique lift in $B_\rho$ of a barycentre in its image. For $F\in\mathsf F_q(\rho)$, define
\[
 \begin{aligned}
 \Phi_{K,m}(F)&=\sum_{p_1,\ldots,p_q}F(\hat x(p_1),\ldots,\hat x(p_q))
                       \prod_l(a_{p_l}-\langle a_{p_l}\rangle),\\
 \Psi_{K,m}(F)&=\sum_{p_1,\ldots,p_q}F(\hat x(p_1),\ldots,\hat x(p_q))
                       \kappa_q(a_{p_1},\ldots,a_{p_q}).
 \end{aligned}
\tag{12}
\]
Only plaquettes with barycentres in the chart are summed. These maps are linear, and
\[
 \Phi(\otimes_l f_l)=\prod_l{:}\mathcal O(f_l^{(m)}){:},\qquad
 \Psi(\otimes_l f_l)=\kappa_q(\mathcal O(f_1^{(m)}),\ldots,\mathcal O(f_q^{(m)})),
 \qquad \Phi(F)\Phi(G)=\Phi(F\otimes G).
\tag{13}
\]

**Proof.** In (12) the coefficients are independent of $F$; only values of the function enter. On a tensor these values factor by slot. Each factor vanishes outside the chart, so extending the indices to all plaquettes changes nothing. Multiplying the $q$ finite sums gives the first equality in (13). Cumulant multilinearity (6), applied successively in every slot, gives the second. Multiplication of the two finite sums for $F,G$ gives the sum for $F\otimes G$, proving the third for arbitrary finite tensor sums. These identities do not require separation at finite cutoff.

Restrict to the complex span $\mathcal T_q^{\rm sep}(\rho)$ of real separated $C^1$ tensors. There, $\langle\Phi(F)\rangle$ and $\Psi(F)$ extend (11) and (4). If two tensor presentations give the same function, their difference is zero at every tuple of lifted barycentres, so both maps annihilate it. This proves presentation independence before taking a limit. **(filled: degree conventions.)** Set $\Phi(c)=c$ for $q=0$. For $q=1$, the centred moment is zero but $\Psi(f)$ is the uncentred mean; no limit of that mean is claimed. ∎

## 7. B10: a support-adapted countable family

**`7.4:def-countable-family`, II:66343–66410. Source status: definition with proof.** Let $\mathcal Q$ be the finite unions of closed rational boxes. Put
\[
 C_Q^1=\{f\in C^1(\mathbb R^4;\mathbb R):f=0\text{ off }Q\},
 \quad \|f\|_{C^1}=\max\{\|f\|_\infty,\|\nabla f\|_\infty\}.
\]
Choose a countable dense $D_Q\subset C_Q^1$. Then
\[
 \mathfrak F=\bigcup_{n\ge2}\{(\varphi_1,\ldots,\varphi_n):
          Q_i\in\mathcal Q\text{ pairwise disjoint},\ \varphi_i\in D_{Q_i}\}
\tag{14}
\]
is countable and consists of separated tuples. It approximates any compact $C^1$ test inside any prescribed open neighbourhood of its support.

**Proof, including separability (filled).** On a fixed closed box $Q'\supset Q$, continuous functions are separable: piecewise multilinear interpolation on rational grids with rational vertex values gives a countable family, and uniform continuity makes its sup error tend to zero. A vector of five such functions has a separable metric topology. The map $f\mapsto(f,\partial_0f,\ldots,\partial_3f)|_{Q'}$ embeds $C_Q^1$; the componentwise sup norm and the Euclidean-gradient norm differ by at most the fixed factor two. A subspace of a separable metric space is separable: take a countable basis of balls, choose a subspace point from each nonempty intersection, and note that these points meet every relative open set. This proves the existence of $D_Q$ in the required norm without needing a closed-image assertion. Since $40M\ge1$,
\[
 \|f\|_\sharp\le40M\|f\|_{C^1},
\tag{15}
\]
so this density also holds in the sharp norm.

For compact $K=\operatorname{supp}f\subset W$, with $W$ open, choose around each point a rational open box whose closure lies in $W$. A finite subcover gives $Q\in\mathcal Q$ with $K\subset Q\subset W$. Then $f\in C_Q^1$, and all its $D_Q$-approximants stay in $W$. A zero function is already zero; include zero in every $D_Q$. There are countably many finite rational-box unions, finite lists of them, and finite products of their countable $D_Q$'s. Thus (14) is countable. Distances between its supports are bounded below by those between the disjoint compact $Q_i$, which are positive. For a separated target tuple, choose the neighbourhoods separately with small enough collars to retain separation. This last requirement is essential: arbitrary $C^1$-dense tests need not preserve supports. ∎

## 8. B11: one subsequence and equicontinuity

### 8.1 The source theorem and the single extraction

**`7.4:thm-infinite-volume`, II:66412–66675. Source status: proved implication from (a)–(d); exact statement: §14.6.** Its conclusions are: a common subsequence for H-BLOCK and every separated curvature tuple; real symmetric multilinear connected limits with (2); distributions off the diagonals of order at most $5n+1$; exact translations and $W_4$; centred OS positivity on the separated polynomial and compact smooth distribution domains; and the separable curvature Hilbert space with time semigroup, spatial momenta, and $W_3$ action. Sections 8–13 prove these on the source route. The generator-domain correction is in §13.3. The source's exclusions are preserved in §13.5 and in its exact statement.

Put $\mathfrak I=\mathcal T^\vee\sqcup\mathfrak F$. For $s=A\in\mathcal T^\vee$, let $v_j(s)=\langle A\rangle_j$ on its eventual domain. For $s=(g_1,\ldots,g_n)\in\mathfrak F$, let $v_j(s)=S^T_{n;K_j,m_j}(\vec g)$ after transport. Choose a finite $\rho$ containing its supports and any finite $d>0$ below their support distances. Once $L^{m_j}\ge2\rho+2$ and $m_j\ge m_*(n,\rho,g)$, transport and H-PB give
\[
 |v_j(s)|\le C_n^\infty(d;\rho)\prod_i\|g_i\|_\sharp.
\tag{16}
\]
This is uniform in $j$. H-BLOCK supplies the other coordinate bounds. Neither convergence nor a common threshold is required before extraction; each coordinate has its own finite initial segment.

**(filled: the diagonal argument.)** A bounded complex sequence has a convergent subsequence: put its values in a closed square, bisect into finitely many subsquares, retain one containing infinitely many indices, and repeat. The diameters tend to zero. Completeness gives the common limit and an increasing choice of indices converging to it. Boundary ties can be resolved by choosing the first available square. Enumerate $\mathfrak I$ as $s_1,s_2,\ldots$. Apply this construction recursively to nested infinite index sets $J_k$, starting after the domain threshold for $s_k$. Choose increasing $j_k\in J_k$. For fixed $l$, every $j_k$ with $k\ge l$ lies in $J_l$, so $v_{j_k}(s_l)$ converges. Let $\mathcal J=\{j_k:k\ge1\}$.

H-BLOCK now gives $\omega_\infty$ along this very $\mathcal J$. No mixed observable was inserted into the list; no mixed bound is claimed. Restricting later to an infinite subset preserves all these limits. This proves the extraction portion II:66606–66675 without using any of conclusions (A)–(D).

### 8.2 The equicontinuity lemma

**`7.4:prf-equicontinuity`, II:66677–66843. Source status: proved. Exact statement: §14.7.** Let compact $Q_i$ be pairwise at distance at least $d'>0$, each inside a radius-$R'$ ball, and all inside $B_\rho$. For real Lipschitz $f_i,\varphi_i$ supported in $Q_i$, at the volume and first-passage floors of H-PB,
\[
 |S^T_{n;K,m}(\vec f)-S^T_{n;K,m}(\vec\varphi)|
 \le C_n^\infty(d';R')\sum_{i=1}^n\|f_i-\varphi_i\|_\sharp
       \prod_{l<i}\|\varphi_l\|_\sharp\prod_{l>i}\|f_l\|_\sharp.
\tag{17}
\]
For every $\vec f\in\mathfrak S_n$, its values converge along the already selected $\mathcal J$.

**Proof of the estimate.** Multilinearity of (4), and linearity of transport, give
\[
 S^T(\vec f)-S^T(\vec\varphi)
 =\sum_i S^T(\varphi_1,\ldots,\varphi_{i-1},f_i-\varphi_i,f_{i+1},\ldots,f_n).
\]
The $l$th entry in each term stays inside $Q_l$. Consequently every hybrid tuple has the same lower separation and ball-radius bounds. Apply (2) separately to each term, and use the preserved norms in §3. Summation proves (17), for Lipschitz tests as stated.

**Proof of convergence.** First suppose every $f_i$ is nonzero, and put $d=\mathsf d(\vec f)<\infty$. Choose $\rho$ containing their supports and $R'=\rho+d/3$. Inside the open $d/3$ neighbourhood of each support choose a rational-box union $Q_i$ by §7. Every $Q_i$ is inside $B_{R'}$, and for points in distinct $Q_i,Q_k$ the triangle inequality gives distance at least $d-2d/3=d/3$. Select $\varphi_i\in D_{Q_i}$ with $\|f_i-\varphi_i\|_{C^1}\le\eta$. Equation (15) gives $\|f_i-\varphi_i\|_\sharp\le40M\eta$, and $\|\varphi_i\|_\sharp\le\|f_i\|_\sharp+40M\eta$. Thus (17) gives, on a tail independent of the cutoff value,
\[
 |S^T_{n;j}(\vec f)-S^T_{n;j}(\vec\varphi)|\le\Delta_{\vec f}(\eta),
 \quad
 \Delta_{\vec f}(\eta)=C_n^\infty(d/3;R')
       \sum_i40M\eta\prod_{l\ne i}(\|f_l\|_\sharp+40M\eta).
\tag{18}
\]
It tends to zero. The fixed approximant belongs to $\mathfrak F$, so its values converge along $\mathcal J$. Given $u>0$, choose $\eta$ so that $2\Delta_{\vec f}(\eta)<u/2$. Beyond the domain and convergence thresholds, the difference of two approximant values is below $u/2$. The triangle inequality shows that the two target values differ by less than $u$. Completeness proves convergence. The limit is that of the original sequence at $\vec f$; changing approximants or neighbourhoods cannot change it.

**(correction: zero-entry endpoint.)** The source permits zero tests, for which $\mathsf d$ may be $+\infty$; its formula $R'=\rho+\mathsf d/3$ then fails to give a finite radius. If a tuple has a zero entry, multilinearity makes every cumulant zero. Set that approximating entry to zero, enclose the remaining compact supports in disjoint neighbourhoods, and use any finite lower separation. Convergence and the approximation assertion are then immediate with error zero. The numerical formula (18) is used only when its parameters are finite. This covers the full stated domain without evaluating $C_n^\infty$ at infinity.

### 8.3 Limit structure and moving tests

The proof at II:66845–66887 gives the remaining elementary portion of (A). Reality and permutation symmetry follow from (6) at each cutoff. An admissible linear relation in one slot holds at every cutoff, and all its finitely many tuples converge, so the relation persists. Their alternative slot supports have a common compact union still separated from the other slots. For a finite sum $F$ of separated tensors, (12) gives
\[
 S_n^T(F)=\lim_{j\in\mathcal J}\Psi_{K_j,m_j}(F).
\tag{19}
\]
Every summand converges. If $F=0$ as a function, the right side is zero at every cutoff. Thus this linear extension is independent of the tensor presentation.

If the original tuple has radius-$R$ supports and separation at least $d$, apply H-PB to that tuple after its own chart/volume threshold, then take the limit. This proves (2) with $S_n^T$ and its original $d,R$, without the enlarged approximation radii. Passing to the limit in (17) gives the same local continuity estimate.

**(filled: moving tests.)** Suppose $f_i^{[j]}\to f_i$ in the sharp norm, all supported slotwise in fixed separated compact $Q_i$. Their norms are bounded. Equation (17) bounds $|S^T_{n;j}(\vec f^{[j]})-S^T_{n;j}(\vec f)|$ by a finite constant times a sum tending to zero. Add fixed-tuple convergence to get the moving-test limit. This requires no new subsequence.

### 8.4 The remaining subsection-7.4 deductions

**Cluster-point remark, II:66889–66923; source status: proved remark.** Every pointwise cluster point $\Xi$ on the separated tuples is determined by its values on $\mathfrak F$ and is a subsequential limit. Here “cluster point” means that every finite coordinate neighbourhood is met at arbitrarily large indices. The finite-coordinate inequality (17) passes to such a point: otherwise a neighbourhood of its finitely many involved coordinates would contradict the eventual inequality. Hence $|\Xi(\vec f)-\Xi(\vec\varphi)|\le\Delta_{\vec f}(\eta)$. Enumerate $\mathfrak F$; choose increasing $j_k$ beyond all first-$k$ domain thresholds with first-$k$ errors at most $1/k$. The cluster property supplies these indices. The same two-approximation estimate used in §8.2 gives convergence to $\Xi$ on every tuple. If a simultaneous block state is wanted, further extract the countable H-BLOCK coordinates; curvature limits persist.

**`7.4:rem-iterated-limits`, II:66925–67010; source status: proved conditional remark.** Keep the source's extra hypothesis: for every admitted fixed $m$, some infinite $I'_m$ gives $K_i\to\infty$ and limits $S_n^{(m)}$ on all transportable separated tuples; the source also assumes their fixed-torus bounds and full torus symmetries, although those two properties are not needed for this deduction. Suppose $m_j\to\infty$ and $S_n^{(m_j)}$ converges on the length-$n$ portion of $\mathfrak F$. Enumerate that portion as $\vec g_l$ and choose chart radii $\rho_l$. Inductively choose $i_j\in I'_{m_j}$, with $i_j>i_{j-1}$ and $K_{i_j}\ge j$, such that
\[
 |S^T_{n;K_{i_j},m_j}(\vec g_l)-S_n^{(m_j)}(\vec g_l)|\le2^{-j}
\tag{20}
\]
for the finitely many $l\le j$ whose charts are admitted at $m_j$. Fixed-$m_j$ convergence and $K_i\to\infty$ provide this choice. Every fixed $l$ is eventually included. Thus the diagonal and iterated values agree on the countable family. For an arbitrary target tuple and its approximant from (18), apply (17) both before the fixed-volume limit and after taking it. The difference between diagonal and iterated values is at most $2\Delta_{\vec f}(\eta)+2^{-j}$ on a tail. The diagonal values are Cauchy by comparison with their convergent approximant values. Let $j\to\infty$, then $\eta\downarrow0$. The iterated values converge to the same limit. This proves only the asserted conditional direction; it creates no fixed-volume limits and gives no uniqueness.

## 9. B12: distributions off the diagonals

**`7.5:prf-limit-distributions`, II:67014–67129. Source status: proved, with its stated classical analysis inputs. Exact statement: §14.8.** Write $\Omega_n=(\mathbb R^4)^n_{\ne}$. If the open $G_i$ have diameter at most $2R$ and pairwise distance at least $d>0$, there is a unique $T_G\in\mathcal D'(\prod_iG_i)$ agreeing with $S_n^T$ on tensors. These pieces glue uniquely on $\Omega_n$. Tensor sums are dense in each product test space. For prescribed cutoffs $\chi_i\in\mathcal D(G_i;\mathbb R)$ equal to one near the coordinate projections of $\operatorname{supp}\Phi$,
\[
 |T_G(\Phi)|\le C(n,d,R,G,\chi)\|\Phi\|_{C^{5n+1}}.
\tag{21}
\]

**Local existence. (filled: open-ball endpoint.)** A nonempty $G_i$ of diameter at most $2R$ lies in a radius-$2R$ open ball about any of its points. Indeed, equality in the distance from that point cannot be attained at another interior point without a small outward displacement exceeding the diameter. The empty-set case is vacuous. By (2) and (15), the real multilinear form on $\prod_i\mathcal D(G_i;\mathbb R)$ obeys
\[
 |S_n^T(\vec\varphi)|\le(40M)^n C_n^\infty(d;2R)\prod_i\|\varphi_i\|_{C^1}.
\]
Complexify by writing each entry as its real plus imaginary part. This gives
\[
 |\mathsf B(\vec\varphi)|\le A_G\prod_i\|\varphi_i\|_{C^1},
 \qquad A_G=2^n(40M)^n C_n^\infty(d;2R).
\tag{22}
\]
For fixed other entries, the right side is a continuous seminorm on every fixed-compact test space in the remaining slot. The defining test-function topology therefore makes the form separately continuous. H-KER supplies a unique $T_G$ with these tensor values. This is an explicit retained kernel-theorem input, not a claim that a scalar diagonal argument alone constructs distributions.

**Compatibility and gluing.** At a configuration of distinct points let $\delta=\min_{i\ne k}|x_i-x_k|>0$. Balls of radius $\eta<\delta/3$ give an admissible product neighbourhood. Thus these products cover $\Omega_n$. Two products intersect in $\prod_i(G_i\cap G_i')$. If nonempty, this is again admissible, with the first family's diameter and separation bounds. Both restrictions have the same values on its real tensors, hence on complex tensors. H-KER uniqueness gives equality on the overlap, and its gluing clause supplies a unique global distribution. For unbounded separated $V_i$ in B11(A), cover their product by bounded products of this type. Each fixed compact tensor is covered by finitely many such neighbourhoods, and partitioning its factors proves agreement. **(filled)** This proves the unbounded-$V_i$ extension of the bounded-$G_i$ statement.

**Fourier construction, density, and order.** Choose an open box $Y\subset\mathbb R^4$ containing every $\operatorname{supp}\chi_i$ with a collar. Extend $\Phi$ by zero and regard it as periodic on $Y^n$. Let $\xi=(\xi_1,\ldots,\xi_n)$ range over its dual lattice. Then
\[
 \Phi_\Xi=\sum_{|\xi|\le\Xi}\widehat\Phi(\xi)
          \bigotimes_{i=1}^n(\chi_i e^{i\xi_i\cdot})
\tag{23}
\]
has support in one fixed compact subset of $\prod_iG_i$.

**(filled: coefficient and lattice-tail estimates.)** Put $D=4n$. At a nonzero frequency choose a coordinate with $|\xi_a|\ge|\xi|/\sqrt D$. Integration by parts $\nu$ times in that coordinate has no boundary terms, since $\Phi$ vanishes near the period faces. It gives, including the zero frequency by direct integration,
\[
 |\widehat\Phi(\xi)|\le C_{\nu,Y^n}(1+|\xi|)^{-\nu}\|\Phi\|_{C^\nu}.
\tag{24}
\]
The dual lattice is a fixed diagonal rescaling of $\mathbb Z^D$. Its shell $2^k\le1+|\xi|<2^{k+1}$ contains at most $C_Y2^{(k+1)D}$ points: each integer coordinate lies in an interval of length at most a fixed multiple of $2^{k+1}$. Thus the shell contribution to exponent $D+1$ is at most a fixed multiple of $2^{-k}$. The sum converges and its tails tend to zero. This is a written bound, not enumeration.

For any derivative order $r$, Leibniz bounds a tensor in (23) by $C_{r,\chi}(1+|\xi|)^{nr}$. Take $\nu=nr+4n+1$ in (24). The tail tends to zero in that derivative norm. H-FOURIER identifies the limit before multiplication with the periodized $\Phi$; multiplication by $\prod_i\chi_i$ leaves $\Phi$ unchanged. Hence (23) converges to $\Phi$ in $\mathcal D(\prod_iG_i)$, proving the required density.

Continuity of $T_G$ and (22) now give
\[
 T_G(\Phi)=\sum_\xi\widehat\Phi(\xi)
                 \mathsf B((\chi_i e^{i\xi_i\cdot})_i),\qquad
 |\mathsf B((\chi_i e^{i\xi_i\cdot})_i)|
 \le A_G\prod_i(1+|\xi_i|)\|\chi_i\|_{C^1}.
\tag{25}
\]
For the complex gradient norm the last estimate follows from
$|\nabla\chi_i+i\xi_i\chi_i|\le|\nabla\chi_i|+|\xi_i||\chi_i|$. Since $\prod_i(1+|\xi_i|)\le(1+|\xi|)^n$, equations (24)–(25) with $\nu=5n+1$ give (21). The constant is explicitly bounded by
\[
 A_G\prod_i\|\chi_i\|_{C^1}\ C_{5n+1,Y^n}
                  \sum_\xi(1+|\xi|)^{-4n-1}<\infty.
\]
For each fixed compact support choose the cutoffs once. That is the definition of order at most $5n+1$ on the product. Finite partitions of unity give locally finite order on $\Omega_n$. No extension across a diagonal or to a Schwartz space is used. ∎

## 10. B12: exact invariance in the limit

**`7.5:prf-exact-invariance`, II:67131–67310. Source status: proved. Exact statement: §14.9.** Every $S_n^T$, $n\ge2$, is invariant under simultaneous real translations and $W_4$, and under permutation of entries. The centred moment functionals $S_q$ have the same invariance for every $q$, including $S_0=1,S_1=0$.

**Proof.** For $w\in W_4$, choose a centred ball containing the supports; it also contains their images. Transport intertwines $w$ and the torus action. Section 4.1 gives exact equality at every sufficiently large cutoff. Both fixed tuples converge by §8, so their limits agree. Permutation symmetry was proved in §8.3.

Fix $a\in\mathbb R^4$ and a nonzero separated tuple with separation $d>0$. Round each coordinate of $a$ to a multiple of $\varepsilon_j=L^{-K_j}$, obtaining $a_j$. Four coordinate errors of at most $\varepsilon_j/2$ give $|a-a_j|\le\varepsilon_j$. For a ball $B_\rho$ containing the original supports, take the tail with
\[
 \varepsilon_j\le\min\{1,d/4\},\quad
 L^{m_j}\ge2(\rho+|a|+1)+2,\quad
 m_j\ge m_*(n,\rho+|a|+1,g).
\]
The sets $Q_{i,j}=\operatorname{supp}f_i+a+\bar B_{\varepsilon_j}$ contain both translated supports, lie in $B_{\rho+|a|+1}$, and have pairwise distances at least $d/2$. Though the sets vary, these common radius and separation parameters do not. Equations (10) and (17) give
\[
 |S^T_{n;j}(\tau_a\vec f)-S^T_{n;j}(\tau_{a_j}\vec f)|
 \le C_n^\infty(d/2;\rho+|a|+1)
       \sum_i\varpi_{f_i}(\varepsilon_j)\prod_{l\ne i}\|f_l\|_\sharp
 \longrightarrow0.
\tag{26}
\]
By §4.1 and §3, $S^T_{n;j}(\tau_{a_j}\vec f)=S^T_{n;j}(\vec f)$ exactly. Both fixed tuples $\tau_a\vec f$ and $\vec f$ converge along $\mathcal J$, so their limits coincide. A zero entry again makes both sides zero. This uses no invariance assertion for a nonlattice translation at finite cutoff.

Every block in the finite partition sum (11) has at least two entries. Each limiting block cumulant has the proved invariances, so their products and sums do too. Linearity (19) and its moment version prove invariance on actual tensor-sum functions. On each product chart the transformed connected distribution has the same tensor values as the original. Density in §9 gives equality on the chart, and gluing gives equality globally. The moment distributions below inherit the same invariances through their disjoint-variable tensor products. This proves B11(B) as well. ∎

## 11. B12: positivity of the centred limit

**`7.6:prf-centred-positivity`, II:67312–67515. Source status: proved. Exact statement: §14.10.** Let $\mathcal T^{\rm sep}_{q,+}$ be the complex span of actual tensors of real $C_c^1$ functions with pairwise disjoint compact supports in $x^0>0$. Put $\mathcal T^{\rm sep}_{0,+}=\mathbb C$, $\mathcal P_+=\bigoplus_{q\ge0}\mathcal T^{\rm sep}_{q,+}$, and
\[
 (\Theta\bar F)_q(x_1,\ldots,x_q)=\overline{F_q(\theta x_1,\ldots,\theta x_q)}.
\]
Put $\Omega_{q,+}=\{(x_1,\ldots,x_q)\in\Omega_q:x_i^0>0\text{ for every }i\}$ for $q\ge1$, with degree zero a scalar. The limits
\[
 S_q(F)=\lim_{j\in\mathcal J}\langle\Phi_{K_j,m_j}(F)\rangle_j,
 \quad S_0=1,\quad S_1=0,
\]
are well-defined linear functionals on separated tensor sums. On a tensor they equal (11) with limiting cumulants. The form
\[
 Q(F,G)=\sum_{q,q'}S_{q+q'}((\Theta\bar F)_q\otimes G_{q'})
\tag{27}
\]
is Hermitian, sesquilinear, and positive semidefinite. It equals the limit of the finite reflection forms, and its positivity extends to every finite sequence of smooth compact tests in $\Omega_{q,+}$.

**Moment existence and presentation independence.** For each tensor, all block cumulants in (11) converge by §8. There are finitely many blocks and partitions, so its moment converges. A finite linear combination also converges. Equation (12) makes a zero function vanish at each cutoff, so its limit vanishes. This proves independence of its presentation and linearity. At degrees zero and one the assertions follow from the exact finite values one and zero. In particular this argument never asks the possibly divergent uncentred one-point expectations to converge.

**(filled: the moment distribution used in the source.)** For a partition $\pi$ without singletons, the product domain $\prod_{B\in\pi}\Omega_{|B|}$ contains $\Omega_q$ after the coordinate ordering by blocks. H-KER supplies the tensor product of the connected distributions in these disjoint variable sets. Restrict to $\Omega_q$, undo that ordering, and sum over the finite set of partitions. This defines a distribution $S_q$ agreeing with (11) on separated smooth tensors. Set $S_1=0$ as a distribution and $S_0=1$. There is no product of two distributions in the same variables here, and no claim at a collision diagonal.

**Finite reflection forms.** For $F,G\in\mathcal P_+$ choose one ball containing every factor in fixed finite presentations of both. For large $j$ their transport is defined. Section 4.2 puts
\[
 \mathbb F_j=\sum_q\Phi_{K_j,m_j}(F_q),\qquad
 \mathbb G_j=\sum_q\Phi_{K_j,m_j}(G_q)
\]
in the bounded half-algebra of bonds in $0<x^0<L^{m_j}$. Equation (9), including the equality of means, and reality of $a_p$ imply
\[
 \overline{\mathbb F_j(\theta\cdot U)}
          =\sum_q\Phi_{K_j,m_j}((\Theta\bar F)_q)(U).
\]
By multiplicativity (13),
\[
 \left\langle\overline{\mathbb F_j(\theta\cdot U)}\mathbb G_j(U)\right\rangle_j
 =\sum_{q,q'}S_{q+q';j}((\Theta\bar F)_q\otimes G_{q'})\longrightarrow Q(F,G).
\tag{28}
\]
For each summand, reflected factors have negative times and unreflected factors have positive times. Their compactness gives a positive cross gap; each group is internally separated. Different tensor terms may overlap, which does not invalidate any pairwise reflected concatenation. **(filled: tensor terminology.)** For general $F_q,G_{q'}$ their product is a finite sum of separated tensors, not necessarily a single tensor; linearity is what makes (27) meaningful.

The two reflecting planes have times $0,L^{m_j}$ in $\varepsilon_j\mathbb Z$ and contain no half-integer lattice sites. H-RP applies to $\mathbb F_j$. With $G=F$, every left side of (28) is nonnegative, so $Q(F,F)\ge0$. Complex conjugation of that left side followed by the change of variables $U\mapsto\theta\cdot U$ interchanges $F,G$; the measure is invariant and $\theta^2=1$. Passing to the limit proves $\overline{Q(F,G)}=Q(G,F)$. Formula (27) is conjugate linear in its first entry and linear in its second. This proves part (b).

**Distributional positive-time density and positivity.** Let $F_q\in\mathcal D(\Omega_{q,+})$ for finitely many $q$. For each point of its compact support, choose disjoint small balls about its coordinates, all strictly above time zero. Their product is a neighbourhood within $\Omega_{q,+}$. A finite subcover and H-AN's partition of unity split $F_q$ into finitely many smooth pieces in such products. For $q=1$ only the positive-time condition is needed; degree zero remains a scalar.

For each piece choose compact one-variable cutoffs inside its balls, equal to one near the projected support. The Fourier sums (23) converge to the piece in the test topology and stay in the same separated positive-time compact sets. Their complex factors are linear combinations of real cutoff sines and cosines with the same supports, so they belong to $\mathcal T^{\rm sep}_{q,+}$. Adding the finitely many pieces produces $F_q^{(k)}\to F_q$ and a sequence $F^{(k)}\in\mathcal P_+$. Every $Q(F^{(k)},F^{(k)})\ge0$.

For a pair of pieces, the product of the reflected compact set and the positive compact set stays strictly inside $\Omega_{q+q'}$. Reflection/conjugation preserves smooth convergence. Leibniz's rule on separate variables shows that $\Theta\overline{F_q^{(k)}}\otimes F_{q'}^{(k)}$ converges with every derivative and fixed compact support. Distribution continuity therefore gives
\[
 \sum_{q,q'}S_{q+q'}((\Theta\bar F)_q\otimes F_{q'})
       =\lim_k Q(F^{(k)},F^{(k)})\ge0.
\tag{29}
\]
All limits are over finite degree and piece sums. This is precisely the source's compact off-diagonal version of (E2), and completes B11(C). ∎

## 12. B13: the curvature Hilbert space and its orbit bound

**`7.7:prf-reconstructed-space`, II:67528–67753. Source status: proved. Exact statement: §14.11.** With $Q=(\cdot,\cdot)_{\rm OS}$ from (27), let
\[
 \mathcal N=\{F\in\mathcal P_+:Q(F,F)=0\},\quad
 \mathcal H^{\rm curv}=\overline{\mathcal P_+/\mathcal N},\quad
 \mathbb1=(1,0,\ldots),\quad \Omega=[\mathbb1].
\tag{30}
\]
The lemma asserts a separable Hilbert space with unit $\Omega$, and a time-uniform bound on $Q(F,\mathsf T_tF)$, with the source's individual-ball radius and support gaps. Here
\[
 (\mathsf T_tF)_q(x_1,\ldots,x_q)=F_q(x_1-te_0,\ldots,x_q-te_0),\quad t\ge0.
\]

### 12.1 Null vectors and completion

**(filled: Cauchy–Schwarz and the quotient.)** Positivity gives $Q(F+zG,F+zG)\ge0$ for every complex $z$. If $Q(G,G)>0$, choosing $z=-\overline{Q(F,G)}/Q(G,G)$ gives
\[
 |Q(F,G)|^2\le Q(F,F)Q(G,G).
\tag{31}
\]
If $Q(G,G)=0$ and $Q(F,G)\ne0$, choose the phase of $z$ to make the cross term negative and then increase its modulus. This contradicts positivity. Thus (31) holds in that case too. A vector is null exactly when it is orthogonal to every vector. This characterisation proves that $\mathcal N$ is a linear subspace and that $Q$ descends to a positive definite inner product on the quotient. Its completion by H-AN is a Hilbert space. Since $S_0=1$, $\|\Omega\|^2=Q(\mathbb1,\mathbb1)=1$.

It is useful to name the finite moment constants obtained directly from (11):
\[
 D_0(d;R)=1,\quad D_1(d;R)=0,\quad
 D_q(d;R)=\sum_{\pi\in\operatorname{Part}_{\ge2}[q]}
                       \prod_{B\in\pi}C_{|B|}^\infty(d;R)\quad(q\ge2).
\tag{32}
\]
For a real separated tuple in individual radius-$R$ balls with distances at least $d$,
\[
 |S_q(\vec f)|\le D_q(d;R)\prod_i\|f_i\|_\sharp.
\tag{33}
\]
Each block uses (2); each entry appears in exactly one block. This proves (33) without any assumption on growth in $q$.

### 12.2 Separability

Write $F\in\mathcal P_+$ as a finite list of real tensors with complex coefficients $c_\alpha$, allowing the empty tensor. Discard zero tensor terms. If only the empty tensor remains, rational complex constants approximate it. Otherwise let $R_F>0$ be a common upper bound for the radii of individual support balls, let $d_F$ be the least within-tensor support distance, and let $\delta_F>0$ be the least time coordinate of any support. A minimum over no pairs is $+\infty$. Each nonempty support is compact in positive time, and each tensor is internally separated, so $d_F>0$ and $\delta_F>0$.

Choose $0<h\le\min\{1,d_F/4,\delta_F/2\}$. Use §7 to place each occurring support inside a rational-box union $Q(f)$ contained in its open $h$-neighbourhood. In one tensor these sets have distances at least $d_F/2$ and positive times at least $\delta_F/2$; each lies in a ball of radius $R_F+h$. Choose $g\in D_{Q(f)}$ with $\|f-g\|_{C^1}\le\eta$, $0<\eta\le1$, and rational complex coefficients $c_\alpha'$ with $|c_\alpha-c_\alpha'|\le\eta$. Let $G$ be the resulting finite tensor sum.

The possible $G$'s form a countable set: there are countably many allowed boxes, finite lists, degrees, dense-set elements, and rational coefficients. To prove density, use the exact tensor telescoping identity
\[
 \bigotimes_{a=1}^q f_a-\bigotimes_{a=1}^q g_a
 =\sum_{a=1}^q g_1\otimes\cdots\otimes g_{a-1}\otimes(f_a-g_a)
                       \otimes f_{a+1}\otimes\cdots\otimes f_q.
\tag{34}
\]
It follows by subtracting consecutive hybrids, so it holds as an identity of functions. Expanding $F-G$ gives finitely many terms $\xi_j\otimes_a\varphi_{j,a}$, each carrying either an $O(\eta)$ coefficient or one sharp norm at most $40M\eta$. With
\[
 \Gamma_F=1+\max_\alpha|c_\alpha|,\quad
 \Lambda_F=1+40M+\max_f\|f\|_\sharp,\quad
 \bar q=\max\{q:F_q\ne0\},
\]
every term satisfies
\[
 |\xi_j|\prod_a\|\varphi_{j,a}\|_\sharp
       \le\Gamma_F\Lambda_F^{\bar q}\eta.
\tag{35}
\]
All norms of unchanged factors and their approximants are bounded by $\Lambda_F$. The reflected concatenation of any two such terms has within-group distance at least $d_F/2$ and cross distance at least $\delta_F$. Apply (33), at $d_* =\min\{d_F/2,\delta_F\}$ and $R_F+h$, to every pair. Equations (27) and (35) give
\[
 \|[F]-[G]\|^2\le C_F\eta^2,
\tag{36}
\]
where $C_F$ is a finite sum of the corresponding $D_{q_j+q_{j'}}(d_*;R_F+h)$ times $(\Gamma_F\Lambda_F^{\bar q})^2$. The empty-pair term uses $D_0=1$; terms of total degree one vanish. The number of terms and $C_F$ are independent of $\eta$. This proves density of the countable quotient classes, hence separability of the completion.

### 12.3 Uniform time bounds

**(filled: constants and empty minima.)** If $F=F_0$, then $Q(F,\mathsf T_tF)=|F_0|^2$ for all $t$, so the assertion is immediate. For a constant vector in later mixed formulas set $R_F=1$ and $d_F=\delta_F=+\infty$; use any finite positive lower bound when a separation condition has no pairs. Otherwise use the nonempty supports retained in §12.2.

For $t\ge0$, expand $Q(F,\mathsf T_tF)$ using the finite tensor presentation. A pair of terms reads
$S_{q+q'}(\theta\vec f_\alpha,\tau_{te_0}\vec f_\beta)$. Each individual support still has radius at most $R_F$. Two reflected supports retain distance at least $d_F$. Two translated supports do too. A reflected support has time at most $-\delta_F$, whereas a translated one has time at least $\delta_F+t$. Their distance is at least $2\delta_F+t$. Thus every block cumulant has separation at least
\[
 d_0=\min\{d_F,2\delta_F\}>0,
\]
independently of $t$. Formula (33) gives the explicit finite bound
\[
 |Q(F,\mathsf T_tF)|\le B_F:=
  \sum_{\alpha,\beta}|c_\alpha|\,|c_\beta|
       D_{q_\alpha+q_\beta}(d_0;R_F)
       \prod_a\|f_{\alpha,a}\|_\sharp\prod_b\|f_{\beta,b}\|_\sharp<\infty.
\tag{37}
\]
Empty products equal one, so this includes $|F_0|^2$ and the vanishing degree-one terms. No constant depending on one enclosing radius is substituted for this individual-ball bound.

The raw symmetry identity proved in §13.1 below uses only §10 and the definition (27), not a quotient operator or a bound. It gives
$Q(F,\mathsf T_tF)=Q(\mathsf T_{t/2}F,\mathsf T_{t/2}F)\ge0$. **(filled)** This also proves that the supremum in the source statement is a supremum of real numbers before any Hamiltonian is constructed. Thus $M_F:=\sup_{t\ge0}Q(F,\mathsf T_tF)\le B_F<\infty$. This proves both parts of B13. ∎

## 13. Completing B11(D) on the account's continuation

**`7.7:prf-semigroup-hamiltonian`, II:67786–68079. Source status: written proof completing (D), with the classical spectral inputs in `7.4:rem-standard-facts`.** This is immediately after the requested B13 range. Omitting it would leave the time and momentum clauses of the requested infinite-volume theorem unported.

### 13.1 Raw identities, null preservation, and contraction

Time shifts $\mathsf T_t$ for $t\ge0$ preserve $\mathcal P_+$, satisfy its exact semigroup law, and fix $\mathbb1$. The reflected first factor satisfies
$\Theta\overline{\mathsf T_tF}=\mathsf T_{-t}(\Theta\bar F)$. Its supports have negative times at most $-\delta_F-t$. In each reflected concatenation with $G$, translating all slots by $te_0$ preserves separation. Translation invariance from §10 therefore gives
\[
 Q(\mathsf T_tF,G)=Q(F,\mathsf T_tG).
\tag{38}
\]
This is the raw identity used in §12.3. In particular,
\[
 Q(\mathsf T_tF,\mathsf T_tF)=Q(F,\mathsf T_{2t}F)
 \le Q(F,F)^{1/2}Q(\mathsf T_{2t}F,\mathsf T_{2t}F)^{1/2}.
\tag{39}
\]
If $F$ is null, the finite right-hand side is zero. Thus $\mathsf T_t$ preserves $\mathcal N$ even before proving boundedness.

For $q_F=Q(F,F)>0$, set $\eta_k=Q(\mathsf T_{2^kt}F,\mathsf T_{2^kt}F)^{1/2}$. Equations (38)–(39) and (37) give
\[
 \eta_k^2\le q_F^{1/2}\eta_{k+1},\quad
 \eta_k^2=Q(F,\mathsf T_{2^{k+1}t}F)\le M_F.
\]
Since $M_F\ge Q(F,F)=q_F$, division and repeated square roots yield
\[
 \frac{\eta_0}{q_F^{1/2}}
 \le\left(\frac{\eta_k}{q_F^{1/2}}\right)^{2^{-k}}
 \le(M_F/q_F)^{2^{-k-1}}\longrightarrow1.
\tag{40}
\]
Thus $Q(\mathsf T_tF,\mathsf T_tF)\le Q(F,F)$. The null case was already handled. The induced quotient map extends uniquely, by taking limits of quotient approximants, to a contraction $T_t$ on the completion. Equation (38) makes this everywhere-defined bounded operator symmetric, hence self-adjoint: the defining identity of its adjoint holds for every pair of Hilbert vectors. The semigroup law and vacuum invariance extend from the dense quotient. Also
\[
 \langle v,T_tv\rangle=\langle T_{t/2}v,T_{t/2}v\rangle\ge0.
\]
So the operators are positive self-adjoint contractions. Only the single-plane positivity of §11 entered.

### 13.2 Strong continuity

Fix $F,G$ in finite real-tensor presentations, and $s,t\ge0$ with $|t-s|\le\min\{1,d_G/4\}$. Subtract the expressions for $Q(F,\mathsf T_tG)$ and $Q(F,\mathsf T_sG)$, then apply the tensor telescoping identity (34) to the translated factors of each term. Every resulting tuple has exactly one factor $\tau_{te_0}g-\tau_{se_0}g$.

The two translates of each $g$ lie in its support plus the segment $[\min\{s,t\},\max\{s,t\}]e_0$, a compact set in a ball of radius $R_G+1$. For two such sets their shifts differ by at most $|s-t|$, so their distance is at least $d_G-|t-s|\ge d_G/2$. Reflected factors keep distance $d_F$, and their distances from the shifted group are at least $\delta_F+\delta_G$. Thus fixed parameters
\[
 R_{F,G}=\max\{R_F,R_G+1\},\quad
 d_{F,G}=\min\{1,d_F,d_G/2,\delta_F+\delta_G\}>0
\]
serve every term, independently of $s,t$. **(filled)** The additional minimum with one makes this a finite lower bound even when some sets of pairs are empty; it weakens no needed separation claim. Expand its moment by (11). Each entry occurs in exactly one block, so the unique difference entry contributes the small factor from (10). The other factors retain their sharp norms. Summing the finite terms gives
\[
 |Q(F,\mathsf T_tG)-Q(F,\mathsf T_sG)|
 \le C_{F,G}\max_{g\text{ occurring in }G}\varpi_g(|t-s|)\longrightarrow0.
\tag{41}
\]
If no factor occurs in $G$, the difference is zero. All degree-zero and degree-one cases are covered by (32).

On quotient vectors, contraction and (41) give
\[
 \|T_t[F]-[F]\|^2
 \le2Q(F,F)-2\operatorname{Re}Q(F,\mathsf T_tF)\longrightarrow0
 \quad(t\downarrow0).
\]
For arbitrary $v$ and a quotient approximant $[F]$,
\[
 \|T_tv-v\|\le2\|v-[F]\|+\|T_t[F]-[F]\|.
\]
First fix $[F]$ close to $v$, then let $t\downarrow0$. This proves continuity at zero on the whole Hilbert space. The inequalities
$\|T_{t+h}v-T_tv\|\le\|T_hv-v\|$ and, when $t\ge h$, $\|T_tv-T_{t-h}v\|\le\|T_hv-v\|$ prove strong continuity at all nonnegative times.

### 13.3 Injectivity and the generator, with its domain

If $T_tv=0$, then $\|T_{t/2}v\|^2=\langle v,T_tv\rangle=0$. Iteration gives $T_{t2^{-k}}v=0$ for every $k$, and strong continuity gives $v=0$. Thus every $T_t$ is injective.

Let $E_1$ be the spectral measure of the positive contraction $T_1$, supplied by H-SPEC. It is supported on $[0,1]$ and $E_1(\{0\})=0$. Define
\[
 H=\int_{(0,1]}-\log\lambda\,dE_1(\lambda),\qquad
 D(H)=\left\{v:\int_{(0,1]}|\log\lambda|^2\,d\langle v,E_1(\lambda)v\rangle<\infty\right\}.
\tag{42}
\]
**(correction: domain.)** The source theorem says “acting in the whole of” $\mathcal H^{\rm curv}$ at II:66562, and its proof says “on all of” that space at II:67995. The warranted statement is a nonnegative self-adjoint operator **on that ambient Hilbert space with dense domain (42)**. It is not generally defined on every vector. This interpretation agrees with the explicit “densely defined” wording in SA:25611–25613.

**(filled: density and the functional-calculus passage.)** The spectral subspaces $E_1([e^{-k},1])\mathcal H^{\rm curv}$ lie in $D(H)$, since $|\log\lambda|\le k$ there. Their projections increase strongly to the identity because $E_1(\{0\})=0$. Hence $D(H)$ is dense. H-SPEC makes (42) self-adjoint and nonnegative. The need for a domain is substantive: on $\ell^2(\mathbb N)$, $T_te_k=e^{-tk}e_k$ is an injective strongly continuous positive contraction semigroup, but its logarithm has $He_k=ke_k$. The diagonal entries prove positivity, contraction, injectivity, and the semigroup law. For every $v\in\ell^2$, $\sum_k|e^{-tk}-1|^2|v_k|^2\to0$ by domination by $4\sum_k|v_k|^2$, proving strong continuity. The vector with coordinates $1/k$ is square summable because $\sum_{k=2^j}^{2^{j+1}-1}k^{-2}\le2^{-j}$; its image under the logarithm would have every coordinate one, which is not square summable. This example concerns the general implication, not the spectrum of the Yang–Mills construction.

Uniqueness of positive square roots gives $T_{2^{-k}}=T_1^{2^{-k}}$ by induction. The semigroup law gives $T_u=T_1^u=e^{-uH}$ at every nonnegative dyadic rational $u$. For any $v$, bounded convergence against its finite spectral measure shows that $u\mapsto e^{-uH}v$ is continuous: the squared norm difference is the integral of $|\lambda^u-\lambda^{u'}|^2$, bounded by four and converging pointwise on $(0,1]$. Dyadic approximation and §13.2 therefore yield $T_t=e^{-tH}$ for every real $t\ge0$. If another self-adjoint nonnegative $H'$ has these exponentials, the inverse function $-\log$ in the spectral calculus applied to $e^{-H'}=T_1$ gives $H'=H$, including equality of domains. Finally $T_1\Omega=\Omega$, so $\Omega$ lies in the spectral subspace at one; it belongs to $D(H)$ and $H\Omega=0$.

### 13.4 Spatial translations, momenta, and $W_3$

Define $(\mathsf S_aF)_q(x_1,\ldots,x_q)=F_q(x_1-(0,a),\ldots,x_q-(0,a))$. It preserves $\mathcal P_+$ and has inverse $\mathsf S_{-a}$. It commutes with reflection and with $\mathsf T_t$. Exact simultaneous translation invariance in (27) gives
\[
 Q(\mathsf S_aF,\mathsf S_aG)=Q(F,G).
\tag{43}
\]
Thus it preserves null vectors and induces an invertible quotient isometry. Its extension $\mathcal U(a)$ is unitary, fixes $\Omega$, obeys the group law, and commutes with every $T_t$.

**(filled: spatial continuity.)** For small $a$, the support of $g$ and that of $\tau_{(0,a)}g$ lie in the compact swept set $\operatorname{supp}g+[0,1]\cdot(0,a)$. Its time coordinates are unchanged, and its radius increases by at most $|a|$. Within one tensor, two such sets have distance at least $d_G-|a|$, hence at least $d_G/2$ for small $a$. The gap to a reflected factor remains at least $\delta_F+\delta_G$. The same finite telescoping and (33) as in (41) bound the change of each scalar product by constants times $\varpi_g(|a|)$. Thus
\[
 \|\mathcal U(a)[F]-[F]\|^2
   =2Q(F,F)-2\operatorname{Re}Q(F,\mathsf S_aF)\longrightarrow0.
\]
Density and the uniform unitary norm extend this to all vectors, using the same two-approximation inequality as for $T_t$. The group law moves continuity at zero to every point.

Apply H-SPEC's SNAG theorem to this strongly continuous representation:
\[
 \mathcal U(a)=\int_{\mathbb R^3}e^{ia\cdot p}\,dE_P(p),\qquad
 P_l=\int p_l\,dE_P(p),\quad
 D(P_l)=\{v:\int p_l^2\,d\langle v,E_P(p)v\rangle<\infty\}.
\tag{44}
\]
The $P_l$ are self-adjoint and their spectral projections commute. Each $\mathcal U(a)$ commutes with $T_1$, hence, by H-SPEC's commutant clause, with $E_1$ and the spectral measure $E_H$ of (42). Each bounded projection $E_H(B)$ then commutes with every $\mathcal U(a)$, and hence with $E_P$. This proves strong commutation of $H$ with each $P_l$, not just an identity on a test core. Their joint spectral measure is supported in $[0,\infty)\times\mathbb R^3$. **(filled: the vacuum domain.)** Vacuum invariance gives $\int|e^{ia\cdot p}-1|^2\,d\langle\Omega,E_P(p)\Omega\rangle=0$ for every $a$. Take the countable set of rational $a$. Their common zero locus is $\{0\}$: for $p_l\ne0$ choose a sufficiently small nonzero rational $a_l$ with $0<|a_lp_l|<2\pi$ and the other coordinates zero. Thus the vacuum spectral measure is supported at zero. Formula (44) places $\Omega$ in every $D(P_l)$ and gives $P_l\Omega=0$.

For $w\in W_3$, acting only on spatial coordinates, the map $F\mapsto w\cdot F$ preserves positive time, commutes with $\Theta$ and $\mathsf T_t$, and conjugates $\mathsf S_a$ to $\mathsf S_{wa}$. By §10 it preserves (27). The same quotient construction gives a unitary $\mathcal U(w)$ with
\[
 \mathcal U(w)\Omega=\Omega,\quad
 \mathcal U(w)T_t=T_t\mathcal U(w),\quad
 \mathcal U(w)\mathcal U(a)\mathcal U(w)^*=\mathcal U(wa).
\tag{45}
\]
Commutation with $E_1$ means that it preserves $D(H)$ and commutes with $H$ there. For the spectral covariance, the Fourier integral of the measure $\Delta\mapsto E_P(w\Delta)$ is $\int e^{ia\cdot w^{-1}p}\,dE_P(p)=\mathcal U(wa)$ because $w$ is orthogonal. Uniqueness in SNAG therefore gives
$\mathcal U(w)E_P(\Delta)\mathcal U(w)^*=E_P(w\Delta)$. Along with its commutation with $E_H$, this proves $W_3$ symmetry of the joint spectrum. Clauses (D1)–(D3) are proved, with H-SPEC explicitly retained. ∎

### 13.5 Exact scope of the ported conclusion

This completes B11(A)–(D) as a conditional implication, with B10, B12, and B13 proved on the account's route and with the domain correction in (42). Clause (E) remains part of the theorem. We obtain no uncentred one-point limit, coincident-point value, tempered extension, factorial growth bound, field operator, Wightman function, vacuum uniqueness, clustering, mass gap, full $O(4)$ invariance, forward-cone bound $H\ge|P|$, nontriviality of the Hilbert space, uniqueness of the subsequence, regularisation independence, convergence for merely Lipschitz tests, identification with a block/smeared Hilbert space, or mixed block/curvature correlation. The centred conventions $S_0=1,S_1=0$ are exact and do not supply the missing raw one-point limit. H-BLOCK gives a state on the same subsequence; it gives no identification of that state with this curvature reconstruction.

## 14. Exact source statements

The following are literal statement transcriptions from CA-II at `31a47c543775`. The labels, quantifiers, source cross-references, and source exclusions are retained. Each numbered heading has no incomplete/outstanding/model/citation qualifier; its declared standing is **proved implication**, with the source proof following it. The proofs and named inputs are above. The source wording is preserved even where the port explicitly marks a correction: admission/normalization in §1.2, zero entries in §8.2, and the generator domain in §13.3. The lattice-translation correction concerns its proof rather than its statement. These transcriptions are source text credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

### 14.1. 7.4:lem-torus-transport

Source: theorem_0_complete_account_raw_II.tex:65661–65690. Status at the source heading: proved implication.

```latex
\begin{lemma}[Transport of compactly supported test functions to the torus]
\label{7.4:lem-torus-transport}
Let $\rho>0$ and let $m$ satisfy $L^m\ge 2\rho+2$. Write $B_{\rho}$ for the open ball of radius
$\rho$ about $0$ in $\mathbb{R}^4$. For $f$ Lipschitz on $\mathbb{R}^4$ with $\operatorname{supp}f$
compact and contained in $B_{\rho}$, define $f^{(m)}$ on $\mathbb{T}_m$ by
\begin{equation}\label{7.4:eq-torus-transport-1}
f^{(m)}(q_m(x)):=f(x)\quad(x\in B_{\rho}),\qquad
f^{(m)}(\xi):=0\quad(\xi\in\mathbb{T}_m\setminus q_m(B_{\rho})).
\end{equation}
Then the following hold.
\begin{enumerate}
\item[(i)] $f^{(m)}$ is well defined and Lipschitz on $\mathbb{T}_m$, with
$\|f^{(m)}\|_\infty=\|f\|_\infty$ and $\operatorname{Lip}_{\mathbb{T}}f^{(m)}=\operatorname{Lip}f$;
hence $\|f^{(m)}\|_{\sharp}=\|f\|_{\sharp}$.
\item[(ii)] For $f$ and $g$ both supported as above,
\begin{equation*}
\operatorname{dist}_{\mathbb{T}}\bigl(\operatorname{supp}f^{(m)},\operatorname{supp}g^{(m)}\bigr)
=\operatorname{dist}(\operatorname{supp}f,\operatorname{supp}g),
\end{equation*}
and if $\operatorname{supp}f\subset B(x,R)$, then
$\operatorname{supp}f^{(m)}\subset B_{\mathbb{T}}(q_m(x),R)$.
\item[(iii)] If moreover $\operatorname{supp}\tau_af\subset B_{\rho}$, then
$(\tau_af)^{(m)}=\tau_{q_m(a)}(f^{(m)})$. For $w\in W_4$ one has $(w\cdot f)^{(m)}=w\cdot(f^{(m)})$;
here $W_4$ acts on $\mathbb{T}_m$ fixing $q_m(0)$, since each of its elements preserves
$2L^m\mathbb{Z}^4$. In particular $(f\circ\theta)^{(m)}=f^{(m)}\circ\theta$.
\end{enumerate}
Here $\operatorname{dist}_{\mathbb{T}}$ is the distance between subsets of $\mathbb{T}_m$ for
$d_{\mathbb{T}}$, $B_{\mathbb{T}}(\xi,R)$ is the ball of radius $R$ about $\xi$ for $d_{\mathbb{T}}$,
$\tau_{\xi}h:=h(\cdot-\xi)$ for $\xi\in\mathbb{T}_m$, and $(w\cdot h)(\xi):=h(w^{-1}\xi)$.
\end{lemma}
```

### 14.2. 7.4:lem-lattice-symmetries

Source: theorem_0_complete_account_raw_II.tex:65844–65867. Status at the source heading: proved implication.

```latex
\begin{lemma}[Lattice symmetries of the curvature cumulants]\label{7.4:lem-lattice-symmetries}
Fix $K$ and $m$, and let $\varepsilon=L^{-K}$, with the torus $\mathbb{T}_m$, the bare lattice, the
measure $\mu_{K,m}$ and the observables $\mathcal{O}(h)$ as in
Notation~\ref{7.4:not-finite-cutoff}. Let
$b\in\varepsilon\mathbb{Z}^4$ \textup{(}taken modulo $2L^m$\textup{)}, let $w\in W_4$, and let
$h_1,\dots,h_n$ be Lipschitz functions on $\mathbb{T}_m$. Write
$\tau_b\vec h=(\tau_bh_1,\dots,\tau_bh_n)$ and $w\cdot\vec h=(w\cdot h_1,\dots,w\cdot h_n)$. For a bond
configuration $U$ write $w\cdot U$ for the configuration given on every positively oriented bond
$\ell$ by $(w\cdot U)(\ell):=U(\overline{w\ell})^{\pm1}$, where $\overline{w\ell}$ is the positively
oriented bond underlying $w\ell$ and the exponent is $+1$ or $-1$ according as $w$ preserves or
reverses the orientation of $\ell$; equivalently, with $U(\ell^{-1}):=U(\ell)^{-1}$ on
reversed bonds, $(w\cdot U)(\ell)=U(w\ell)$ for every oriented bond $\ell$. Then the
joint laws under $\mu_{K,m}$ of $(\mathcal{O}(\tau_bh_i))_{i}$, of $(\mathcal{O}(w\cdot h_i))_{i}$ and of
$(\mathcal{O}(h_i))_{i}$ coincide. Hence, when $n\ge 2$,
\begin{equation*}
S^T_{n;K,m}(\tau_b\vec h)=S^T_{n;K,m}(w\cdot\vec h)=S^T_{n;K,m}(\vec h),
\end{equation*}
and, for every Lipschitz $h$ on $\mathbb{T}_m$, with $\langle\cdot\rangle_{K,m}$ the expectation
under $\mu_{K,m}$,
\begin{equation*}
\langle\mathcal{O}(\tau_bh)\rangle_{K,m}=\langle\mathcal{O}(w\cdot h)\rangle_{K,m}
=\langle\mathcal{O}(h)\rangle_{K,m}.
\end{equation*}
\end{lemma}
```

### 14.3. 7.4:lem-half-space

Source: theorem_0_complete_account_raw_II.tex:65929–65952. Status at the source heading: proved implication.

```latex
\begin{lemma}[Half-space observables depend only on an open slab]\label{7.4:lem-half-space}
Let $\rho>0$ and $L^m\ge 2\rho+2$, let $B_{\rho}$ be the open ball of radius $\rho$ about $0$ in
$\mathbb{R}^4$, and let $h$ be Lipschitz on $\mathbb{R}^4$ with $\operatorname{supp}h$ compact and
contained in $B_{\rho}\cap\{x^0>0\}$. Let $\theta$ denote the time reflection $x^0\mapsto -x^0$, on
$\mathbb{R}^4$ and on $\mathbb{T}_m$, and put
\begin{equation*}
H_{+}:=q_m\bigl(\{x\in\mathbb{R}^4:\ 0<x^0<L^m\}\bigr)\subset\mathbb{T}_m .
\end{equation*}
Then every bare plaquette $p$ of $\mathbb{T}_m$ with $h^{(m)}(x(p))\neq 0$ has all four of its bonds in
the open slab $H_{+}$. In particular no such bond lies in or crosses the plane $x^0=0$, and every
such bond keeps time-distance at least $\rho+1$ from the antipodal plane $x^0=L^m$, which is
identified with $x^0=-L^m$.
Consequently $\mathcal{O}(h^{(m)})$ and the centred observable
\begin{equation*}
{:}\mathcal{O}(h^{(m)}){:}\ :=\ \mathcal{O}(h^{(m)})-\langle\mathcal{O}(h^{(m)})\rangle
\end{equation*}
are bounded measurable functions of the bond variables in $H_{+}$; here $\langle\cdot\rangle$ is the
expectation under $\mu_{K,m}$. Moreover
\begin{equation*}
\mathcal{O}(h^{(m)})(\theta\cdot U)=\mathcal{O}\bigl((h\circ\theta)^{(m)}\bigr)(U),
\qquad
\langle\mathcal{O}(h^{(m)})\rangle=\langle\mathcal{O}\bigl((h\circ\theta)^{(m)}\bigr)\rangle .
\end{equation*}
\end{lemma}
```

### 14.4. 7.4:lem-translation-modulus

Source: theorem_0_complete_account_raw_II.tex:66048–66088. Status at the source heading: proved implication.

```latex
\begin{lemma}[The translation modulus in the sharp norm]\label{7.4:lem-translation-modulus}
For $a\in\mathbb{R}^4$ let $\tau_a f:=f(\cdot-a)$. For $f\in C^1_c(\mathbb{R}^4)$ write
$\|\nabla f\|_\infty:=\sup_{x}|\nabla f(x)|$, with the Euclidean norm on $\mathbb{R}^4$, and for
$\delta\ge 0$ let
\begin{equation*}
\omega_{\nabla f}(\delta):=\sup\bigl\{|\nabla f(x)-\nabla f(y)| : x,y\in\mathbb{R}^4,\ |x-y|\le\delta\bigr\}
\end{equation*}
be the modulus of uniform continuity of $\nabla f$. Let $f\in C^1_c(\mathbb{R}^4)$ and $a,b\in\mathbb{R}^4$.
\begin{enumerate}
\item We have $\|\tau_af-\tau_bf\|_\infty\le\|\nabla f\|_\infty|a-b|$ and
\begin{equation*}
\operatorname{Lip}(\tau_af-\tau_bf)=\|\nabla f(\cdot-a)-\nabla f(\cdot-b)\|_\infty
\le\omega_{\nabla f}(|a-b|).
\end{equation*}
\item Consequently
\begin{equation}\label{7.4:eq-translation-modulus-a}
\|\tau_af-\tau_bf\|_{\sharp}\le\varpi_f(|a-b|),
\qquad
\varpi_f(\delta):=\max\{\|\nabla f\|_\infty\delta,\ 40M\,\omega_{\nabla f}(\delta)\},
\end{equation}
and $\varpi_f(\delta)\to 0$ as $\delta\to 0$.
\item If $f\in C^2_c(\mathbb{R}^4)$, then $\omega_{\nabla f}(\delta)\le\|\nabla^2f\|_\infty\,\delta$, where
$\|\nabla^2 f\|_\infty$ is the supremum over $x$ of the operator norm of the Hessian
$\nabla^2f(x)$; this is an explicit rate.
\item $\|\tau_af\|_{\sharp}=\|f\|_{\sharp}$.
\item Let $\rho>0$ and $L^m\ge 2\rho+2$, and suppose that $\tau_af$ and $\tau_bf$ are supported in
$B_{\rho}$. Then the transported functions on $\mathbb{T}_m$ satisfy the same bounds:
$\|(\tau_af)^{(m)}-(\tau_bf)^{(m)}\|_\infty\le\|\nabla f\|_\infty|a-b|$,
\begin{equation*}
\operatorname{Lip}_{\mathbb{T}}\bigl((\tau_af)^{(m)}-(\tau_bf)^{(m)}\bigr)\le\omega_{\nabla f}(|a-b|),
\end{equation*}
hence $\|(\tau_af)^{(m)}-(\tau_bf)^{(m)}\|_{\sharp}\le\varpi_f(|a-b|)$, and
$\|(\tau_af)^{(m)}\|_{\sharp}=\|f\|_{\sharp}$. If moreover $\operatorname{supp}f\subset B_\rho$, then
$(\tau_af)^{(m)}=\tau_{q_m(a)}(f^{(m)})$ and $(\tau_bf)^{(m)}=\tau_{q_m(b)}(f^{(m)})$.
\item For merely Lipschitz $f$ the conclusion of \textup{(2)} fails in general. Let $e_1$ be a
coordinate unit vector, $x_1:=x\cdot e_1$, and $f(x)=|x_1|\chi(x)$ with $\chi\in C^1_c(\mathbb{R}^4)$,
$\chi\equiv 1$ near $0$. Then $\operatorname{Lip}(\tau_{se_1}f-f)\ge 2$ for all small $s\ne 0$: the
gradient jump $2e_1$ across $x_1=0$ is displaced, not removed. Hence
$\|\tau_{se_1}f-f\|_{\sharp}\ge 80M$, which does not tend to $0$.
\end{enumerate}
\end{lemma}
```

### 14.5. 7.4:lem-linearity

Source: theorem_0_complete_account_raw_II.tex:66209–66253. Status at the source heading: proved implication.

```latex
\begin{lemma}[Linearity in the test function]\label{7.4:lem-linearity}
Let $\rho>0$, let $m$ satisfy $L^m\ge 2\rho+2$, let $K$ be a cutoff and let $q\ge 1$. Tori, bare lattices
and barycentres are as in Notation~\ref{7.4:not-finite-cutoff}, and $\langle\cdot\rangle_{K,m}$ is
the expectation with respect to $\mu_{K,m}$.

Let $\mathsf{F}_q(\rho)$ be the complex vector space of functions on $(\mathbb{R}^4)^q$ spanned by the
tensors $f_1\otimes\cdots\otimes f_q$ of Lipschitz functions $f_l$ on $\mathbb{R}^4$ with compact
supports in $B_{\rho}$. For a bare plaquette $p$ with $x(p)\in q_m(B_{\rho})$ let $\hat x(p)\in B_{\rho}$
be the lift of $x(p)$, that is, the point with $q_m(\hat x(p))=x(p)$. For $F\in\mathsf{F}_q(\rho)$
let $\Phi_{K,m}(F)$ and $\Psi_{K,m}(F)$ be defined by the first two lines of
\begin{equation}\label{7.4:eq-linearity-a}
\begin{aligned}
\Phi_{K,m}(F)&:=\sum_{p_1,\dots,p_q}F\bigl(\hat x(p_1),\dots,\hat x(p_q)\bigr)
\prod_{l\le q}\bigl(a_{p_l}(U)-\langle a_{p_l}\rangle_{K,m}\bigr),\\
\Psi_{K,m}(F)&:=\sum_{p_1,\dots,p_q}F\bigl(\hat x(p_1),\dots,\hat x(p_q)\bigr)\,
\kappa_q\bigl(a_{p_1},\dots,a_{p_q}\bigr),\\
\Phi_{K,m}(F)\,\Phi_{K,m}(G)&=\Phi_{K,m}(F\otimes G),
\end{aligned}
\end{equation}
the sums running over $q$-tuples of bare plaquettes whose barycentres lie in $q_m(B_{\rho})$. The same
formulas with $q$ replaced by $q'$ define $\Phi_{K,m}$ and $\Psi_{K,m}$ on $\mathsf{F}_{q'}(\rho)$ for
every $q'\ge 1$, the number of arguments being read off the function. Then:
\begin{enumerate}
\item $\Phi_{K,m}$ and $\Psi_{K,m}$ are linear in $F$;
\item on tensors,
\begin{gather*}
\Phi_{K,m}(f_1\otimes\cdots\otimes f_q)=\prod_{l\le q}{:}\mathcal{O}(f_l^{(m)}){:},\\
\Psi_{K,m}(f_1\otimes\cdots\otimes f_q)
=\kappa_q\bigl(\mathcal{O}(f_1^{(m)}),\dots,\mathcal{O}(f_q^{(m)})\bigr);
\end{gather*}
\item the third line of \eqref{7.4:eq-linearity-a} holds for $F\in\mathsf{F}_q(\rho)$ and
$G\in\mathsf{F}_{q'}(\rho)$.
\end{enumerate}
Let $\mathcal{T}^{\mathrm{sep}}_q(\rho)$ be the complex span of the separated real $C^1$ tensors
$f_1\otimes\cdots\otimes f_q$, that is, those with $f_l$ real, of class $C^1$, with compact supports in
$B_{\rho}$ and with pairwise disjoint supports. Consequently, for $F\in\mathcal{T}^{\mathrm{sep}}_q(\rho)$ the
expressions
\begin{equation*}
S_{q;K,m}(F):=\bigl\langle\Phi_{K,m}(F)\bigr\rangle_{K,m},\qquad
S^T_{q;K,m}(F):=\Psi_{K,m}(F)
\end{equation*}
are well-defined linear functionals of the function $F$. They extend, respectively, the centred
moments of Definition~\ref{7.4:def-centred-moments} and the cumulant, and they are independent of the
representation of $F$ as a sum of tensors.
\end{lemma}
```

### 14.6. 7.4:thm-infinite-volume

Source: theorem_0_complete_account_raw_II.tex:66412–66593. Status at the source heading: proved implication.

```latex
\begin{theorem}[The infinite-volume theorem]\label{7.4:thm-infinite-volume}
Let $L\ge L_0$ be odd, let $\mathfrak{p}$, $\gamma$ and $\gamma_H$ be fixed after $L$, let $r>0$ be
fixed first, and let
\begin{equation*}
0<g\le\min\{\gamma_H,\gamma_J(L,\mathfrak{p},r)\}.
\end{equation*}
Let $(g_0^{(j)})_{j\in\mathbb{N}}$ be a sequence in $(0,g_{-}(g)]$ decreasing to $0$, for instance the
subsequence of clause~(ii-b) of Theorem~\ref{3.1:thm-main}. Let $K_j:=K(g_0^{(j)},g)$ be the
first-passage cutoffs, so that $K_j\to\infty$ by clause~(0) of Theorem~\ref{3.1:thm-main}. Let
$(m_j)_{j\in\mathbb{N}}$ be integers with
$m_j\to\infty$ and $m_j\ge m_{\mathbb{T}}(g_{-}(g))$ for every $j$. Write
$\langle\cdot\rangle_j:=\langle\cdot\rangle_{K_j,m_j}$, $S^T_{n;j}:=S^T_{n;K_j,m_j}$ and
$S_{q;j}:=S_{q;K_j,m_j}$.

For $n\ge1$ let $\mathfrak{S}_n$ be the set of $n$-tuples $\vec f=(f_1,\dots,f_n)$ of real-valued
$C^1$ functions on $\mathbb{R}^4$ with compact, pairwise disjoint supports; for $n\ge2$ let
$\mathsf{d}(\vec f)>0$ be the least distance between two of these supports. On such tuples,
$S^T_{n;j}(\vec f)$ ($n\ge2$) and $S_{n;j}(\vec f)$ ($n\ge1$) are understood through the transport
to the torus, \eqref{7.4:eq-torus-transport-a}, and Definition~\ref{7.4:def-centred-moments}; they
are defined for every $j\ge j(\vec f)$, for some index $j(\vec f)$. For $a\in\mathbb{R}^4$ put
$\tau_af:=f(\cdot-a)$; for $w\in W_4$
put $(w\cdot f)(x):=f(w^{-1}x)$. Let $\theta$ be the time reflection $(x^0,\vec x)\mapsto(-x^0,\vec x)$
and $e_0$ the unit vector in the time direction.

Assume:
\begin{enumerate}
\item[(a)] the correlation theorem, in the standing setting of
Definition~\ref{7.1:not-torus-cumulants}, in which the gauge group is $\mathrm{SU}(2)$, that is
$N=2$, and the hypotheses \textup{(H1)}--\textup{(H7)} hold;
\item[(b)] reflection positivity of the lattice measure;
\item[(c)] the per-ball volume-free bound;
\item[(d)] the extraction of the limit state of block and smeared observables, in the following form.
Let $\mathcal{T}^{\vee}$ be the countable family of block and smeared observables on which that state
is constructed; for $A\in\mathcal{T}^{\vee}$ the expectation $\langle A\rangle_j$ is defined for every
$j\ge j(A)$, for some index $j(A)$. For every $A\in\mathcal{T}^{\vee}$ the sequence
$(\langle A\rangle_j)_{j\ge j(A)}$ is bounded uniformly in the cutoff. Along every infinite subset of
$\mathbb{N}$ along which $\langle A\rangle_j$ converges for every $A\in\mathcal{T}^{\vee}$, the joint
limit state $\omega_{\infty}$ exists on the quasilocal algebra
$\mathfrak{A}^{\tau}_{\mathrm{loc}}\otimes\mathfrak{A}^{\mathrm{sm}}_{\mathrm{loc}}$ of block and
smeared observables; its construction uses only this convergence together with the density of
$\mathcal{T}^{\vee}$ in that algebra, uniform in the cutoff.
\end{enumerate}
Then there is an infinite set $\mathcal{J}\subset\mathbb{N}$ with the following properties. It is
obtained by a single diagonal extraction over the countable set
$\mathcal{T}^{\vee}\sqcup\mathfrak{F}$, where $\mathfrak{F}$ is the family of
Definition~\ref{7.4:def-countable-family}. Along this same $\mathcal{J}$ the joint limit state
$\omega_{\infty}$ exists. Moreover, the following hold.
\begin{enumerate}
\item[(A)] \emph{Existence, bounds, structure.} For every $n\ge2$ and every $\vec f\in\mathfrak{S}_n$
the limit
\begin{equation*}
S^T_n(\vec f):=\lim_{j\in\mathcal{J}}S^T_{n;j}(\vec f)
\end{equation*}
exists, the terms being defined for $j\ge j(\vec f)$. The functional $S^T_n$ has the following
properties.
\begin{itemize}
\item It is multilinear on separated tuples, in each argument among the functions that keep the tuple
in $\mathfrak{S}_n$.
\item It is symmetric under permutations of its arguments.
\item It is real-valued.
\item Suppose each $f_i$ is supported in a ball of radius $R$ and the supports are pairwise at
distance at least $\mathsf{d}$. Then
\begin{equation}\label{7.4:eq-infinite-volume-a}
|S^T_n(\vec f)|\le C^{\infty}_n(\mathsf{d};R)\prod_{i=1}^n\|f_i\|_{\sharp},
\end{equation}
where $C^{\infty}_n(\mathsf{d};R)$ is the constant of the per-ball volume-free bound.
\end{itemize}
Let $V_1,\dots,V_n\subset\mathbb{R}^4$ be open sets pairwise at positive distance. There is a unique
$T_V\in\mathcal{D}'(V_1\times\cdots\times V_n)$ with
$T_V(\varphi_1\otimes\cdots\otimes\varphi_n)=S^T_n(\vec\varphi)$ for real-valued
$\varphi_i\in\mathcal{D}(V_i)$; the right side is extended complex-multilinearly to complex-valued
$\varphi_i$. These distributions glue to a unique $S^T_n\in\mathcal{D}'((\mathbb{R}^4)^n_{\neq})$, where
\begin{equation*}
(\mathbb{R}^4)^n_{\neq}:=\{(x_1,\dots,x_n)\in(\mathbb{R}^4)^n:\ x_i\neq x_k\ \text{for all}\ i\neq k\}.
\end{equation*}
This $S^T_n$ has order at most $5n+1$ on every product of pairwise separated balls, so its order is
locally finite. Convergence of $S^T_{n;j}(\vec f)$ for tuples of merely Lipschitz functions is not
asserted.
\item[(B)] \emph{Invariance.} For every $n$, every $\vec f\in\mathfrak{S}_n$, $a\in\mathbb{R}^4$,
$w\in W_4$ and every permutation $\sigma$ of $\{1,\dots,n\}$,
\begin{equation*}
\begin{aligned}
S^T_n(\tau_af_1,\dots,\tau_af_n)&=S^T_n(\vec f)=S^T_n(w\cdot f_1,\dots,w\cdot f_n)\\
&=S^T_n(f_{\sigma(1)},\dots,f_{\sigma(n)}).
\end{aligned}
\end{equation*}
The distributions $S^T_n$ are invariant under the diagonal action of $\mathbb{R}^4\rtimes W_4$ on
$(\mathbb{R}^4)^n_{\neq}$. Invariance under $O(4)$ is not asserted.
\item[(C)] \emph{Osterwalder--Schrader positivity for the centred field.} Put $S_0:=1$ and $S_1:=0$.
Put $\mathcal{T}^{\mathrm{sep}}_{0,+}:=\mathbb{C}$. For $q\ge1$ let
$\mathcal{T}^{\mathrm{sep}}_{q,+}$ be the complex span of the tensors $f_1\otimes\cdots\otimes f_q$ with
$f_a\in C^1_c(\mathbb{R}^4;\mathbb{R})$ whose supports are compact, pairwise disjoint and contained in
$\{x^0>0\}$. Let $\mathcal{P}_+:=\bigoplus_{q\ge0}\mathcal{T}^{\mathrm{sep}}_{q,+}$, whose elements
$F=(F_q)_q$ have finitely many non-zero components. Put
\begin{equation*}
(\Theta\bar F)_q(x_1,\dots,x_q):=\overline{F_q(\theta x_1,\dots,\theta x_q)}.
\end{equation*}
For $q\ge2$ and $\vec h\in\mathfrak{S}_q$, and for $F,G\in\mathcal{P}_+$, put
\begin{equation}\label{7.4:eq-infinite-volume-b}
\begin{gathered}
S_q(\vec h):=\sum_{\pi\in\operatorname{Part}_{\ge2}[q]}\ \prod_{B\in\pi}
S^T_{|B|}\bigl((h_l)_{l\in B}\bigr),\\
(F,G)_{\mathrm{OS}}:=\sum_{q,q'}S_{q+q'}\bigl((\Theta\bar F)_q\otimes G_{q'}\bigr).
\end{gathered}
\end{equation}
Let $\mathcal{T}^{\mathrm{sep}}_q$ be the complex span of the tensors $h_1\otimes\cdots\otimes h_q$
with $\vec h\in\mathfrak{S}_q$, regarded as functions on $(\mathbb{R}^4)^q$. By the linearity in the test
function (Lemma~\ref{7.4:lem-linearity}), $S_q$ extends linearly and unambiguously to
$\mathcal{T}^{\mathrm{sep}}_q$, and $S_{q;j}\to S_q$ there as $j\to\infty$ in $\mathcal{J}$.
Since the reflected factors are supported in $\{x^0<0\}$, $(\Theta\bar F)_q\otimes G_{q'}$ is a
separated tensor, that is, an element of $\mathcal{T}^{\mathrm{sep}}_{q+q'}$, so the second line of
\eqref{7.4:eq-infinite-volume-b} is defined.

Then $(\cdot,\cdot)_{\mathrm{OS}}$ is sesquilinear, Hermitian and positive semidefinite on
$\mathcal{P}_+$, and
\begin{equation*}
(F,G)_{\mathrm{OS}}=\lim_{j\in\mathcal{J}}
\bigl\langle\overline{\mathbb{F}_j(\theta\cdot U)}\,\mathbb{G}_j(U)\bigr\rangle_j .
\end{equation*}
Here $\mathbb{F}_j:=\sum_q\Phi_{K_j,m_j}(F_q)$ and $\mathbb{G}_j:=\sum_q\Phi_{K_j,m_j}(G_q)$ are the
centred lattice polynomials of Lemma~\ref{7.4:lem-linearity}, and $\theta\cdot U$ is the bond
configuration transformed by the time reflection of $\mathbb{T}_{m_j}$ in the plane pair
$\{x^0=0\}\cup\{x^0=L^{m_j}\}$, acting on bond variables as in Lemma~\ref{1.1:lem-invariance}.
Moreover, the positivity condition $(\mathrm{E}2)$ of \cite{OS73} holds on distributions. Put
\begin{equation*}
(\mathbb{R}^4)^q_{\neq,+}:=\{x\in(\mathbb{R}^4)^q_{\neq}:\ x_a^0>0\ \text{for all}\ a\}.
\end{equation*}
Then for every finite sequence $(F_q)_q$ with $F_q\in\mathcal{D}((\mathbb{R}^4)^q_{\neq,+})$,
\begin{equation*}
\sum_{q,q'}S_{q+q'}\bigl((\Theta\bar F)_q\otimes F_{q'}\bigr)\ge0,
\end{equation*}
where $S_{q+q'}\in\mathcal{D}'((\mathbb{R}^4)^{q+q'}_{\neq})$ now denotes the distribution given by
the first line of \eqref{7.4:eq-infinite-volume-b} with the distributions $S^T_{|B|}$ of (A),
tensored over the blocks and restricted to $(\mathbb{R}^4)^{q+q'}_{\neq}$.
\item[(D)] \emph{Osterwalder--Schrader reconstruction.} Put
\begin{equation}\label{7.4:eq-infinite-volume-c}
\begin{gathered}
\mathcal{N}:=\{F\in\mathcal{P}_+:\ (F,F)_{\mathrm{OS}}=0\},\qquad
\mathcal{H}^{\mathrm{curv}}:=\text{the completion of}\ \mathcal{P}_+/\mathcal{N},\\
\Omega:=[(1,0,0,\dots)],\\
(\mathsf{T}_tF)_q(x_1,\dots,x_q):=F_q(x_1-te_0,\dots,x_q-te_0)\qquad(t\ge0),\\
(\mathsf{S}_{\vec a}F)_q(x_1,\dots,x_q):=F_q\bigl(x_1-(0,\vec a),\dots,x_q-(0,\vec a)\bigr)
\qquad(\vec a\in\mathbb{R}^3).
\end{gathered}
\end{equation}
Then $\mathcal{H}^{\mathrm{curv}}$ is a separable Hilbert space and $\|\Omega\|=1$.
\begin{enumerate}
\item[(D1)] For real $t\ge0$, $\mathsf{T}_t$ induces a well-defined operator $T_t$ on
$\mathcal{H}^{\mathrm{curv}}$. The family $(T_t)_{t\ge0}$ is a strongly continuous semigroup of
positive self-adjoint contractions with $T_t\Omega=\Omega$ and $\ker T_t=\{0\}$. There is a unique
self-adjoint operator $H\ge0$, acting in the whole of $\mathcal{H}^{\mathrm{curv}}$, with
$T_t=e^{-tH}$ for $t\ge0$. Moreover $H=-\log T_1$ and $H\Omega=0$.
\item[(D2)] $\mathsf{S}_{\vec a}$ induces a strongly continuous unitary representation
$\vec a\mapsto\mathcal{U}(\vec a)$ of $\mathbb{R}^3$ with $\mathcal{U}(\vec a)\Omega=\Omega$ and
$\mathcal{U}(\vec a)T_t=T_t\mathcal{U}(\vec a)$. Its generators $\vec P=(P_1,P_2,P_3)$, obtained from
the projection-valued measure of the representation, are self-adjoint and strongly commute pairwise
and with $H$. The joint spectrum of $(H,\vec P)$ lies in $[0,\infty)\times\mathbb{R}^3$.
\item[(D3)] $W_3$, the group of signed permutations of $x^1,x^2,x^3$, acts by unitaries
$\mathcal{U}(w)$. These fix $\Omega$, commute with $T_t$ and $H$, and satisfy
$\mathcal{U}(w)\mathcal{U}(\vec a)\mathcal{U}(w)^*=\mathcal{U}(w\vec a)$. The joint
spectrum of $(H,\vec P)$ is $W_3$-symmetric.
\end{enumerate}
\item[(E)] \emph{Not asserted.} The theorem asserts nothing about the following:
\begin{itemize}
\item the case $n=1$, or anything at coinciding points;
\item temperedness (the extension of $S^T_n$ to test spaces of Schwartz type), or the linear growth
condition $(\mathrm{E}0')$ of \cite{OS75};
\item field operators or Wightman functions;
\item uniqueness of $\Omega$, clustering, or a mass gap;
\item invariance under $O(4)$, or the relativistic spectrum condition $H\ge|\vec P|$;
\item that $\dim\mathcal{H}^{\mathrm{curv}}>1$, or that $S^T_2\not\equiv0$ (both are consequences
stated in clause (iv) of Theorem~\ref{3.1:thm-main} and drawn in Chapter~\ref{ch:8});
\item uniqueness of $\mathcal{J}$, independence of $S^T_n$ from the choice of $(K_j,m_j)$, or
independence from the regularisation;
\item convergence on merely Lipschitz tuples;
\item any identification of $\mathcal{H}^{\mathrm{curv}}$ with the space
$\mathcal{H}^{\mathrm{sm}}$ reconstructed from $\omega_{\infty}$, or with any other Hilbert space
reconstructed in this book;
\item any mixed correlation of block and curvature observables.
\end{itemize}
\end{enumerate}
\end{theorem}
```

### 14.7. 7.4:prf-equicontinuity

Source: theorem_0_complete_account_raw_II.tex:66677–66721. Status at the source heading: proved implication.

```latex
\begin{lemma}[Equicontinuity and existence of the limits]\label{7.4:prf-equicontinuity}
Let $L$, $\mathfrak{p}$, $\gamma$, $\gamma_H$, $r$ and $g$ be as in the standing data of
Theorem~\ref{7.4:thm-infinite-volume}, and let $\mathcal{J}$ be the diagonal subsequence of
\eqref{7.4:eq-infinite-volume-d}.
\begin{itemize}
\item[(i)] Let $n\ge 2$, $R'>0$, $\mathsf{d}'>0$ and $\rho>0$, and let
$Q_1,\dots,Q_n\subset\mathbb{R}^4$ be compact sets such that:
\begin{itemize}
\item each $Q_i$ is contained in a ball of radius $R'$;
\item the $Q_i$ are pairwise at distance at least $\mathsf{d}'$;
\item $Q_1\cup\dots\cup Q_n\subset B_{\rho}$.
\end{itemize}
Let $f_i$, $\varphi_i$ ($i\le n$) be real Lipschitz functions on $\mathbb{R}^4$ supported in $Q_i$.
Let $(K,m)$ satisfy
\begin{equation*}
m\ge\max\{m_{\mathbb{T}}(g_{-}(g)),\ \log_L\ell(n,R',g)\},\qquad L^m\ge 2\rho+2,
\end{equation*}
and let $K=K(g_0,g)$ be the first-passage cutoff of a bare coupling $g_0\in\,]0,g_{-}(g)]$.
Then
\begin{equation}\label{7.4:eq-equicontinuity-a}
\bigl|S^T_{n;K,m}(\vec f)-S^T_{n;K,m}(\vec\varphi)\bigr|
\le C^{\infty}_n(\mathsf{d}';R')\sum_{i\le n}\|f_i-\varphi_i\|_{\sharp}
\prod_{l<i}\|\varphi_l\|_{\sharp}\prod_{l>i}\|f_l\|_{\sharp}.
\end{equation}
\item[(ii)] Let $n\ge 2$ and $\vec f\in\mathfrak{S}_n$, put $\mathsf{d}:=\mathsf{d}(\vec f)$, choose
$\rho>0$ with $\operatorname{supp}f_1\cup\dots\cup\operatorname{supp}f_n\subset B_{\rho}$, and put
$R':=\rho+\mathsf{d}/3$. For $\eta>0$ put
\begin{equation}\label{7.4:eq-equicontinuity-1}
\Delta_{\vec f}(\eta):=C^{\infty}_n(\mathsf{d}/3;R')\sum_{i\le n}40M\eta
\prod_{l\neq i}\bigl(\|f_l\|_{\sharp}+40M\eta\bigr).
\end{equation}
Then $\Delta_{\vec f}(\eta)\to 0$ as $\eta\downarrow 0$. For every $\eta>0$ there are
$\vec\varphi\in\mathfrak{F}$ with $\|f_i-\varphi_i\|_{\sharp}\le 40M\eta$ for $i\le n$, and an index
$j_0(\vec f,\eta)$, such that
\begin{equation*}
\bigl|S^T_{n;j}(\vec f)-S^T_{n;j}(\vec\varphi)\bigr|\le\Delta_{\vec f}(\eta)
\qquad\text{for all }j\in\mathcal{J}\text{ with }j\ge j_0(\vec f,\eta).
\end{equation*}
The limit
\begin{equation}\label{7.4:eq-equicontinuity-b}
S^T_n(\vec f):=\lim_{j\in\mathcal{J}}S^T_{n;j}(\vec f),\qquad\vec f\in\mathfrak{S}_n,\ n\ge 2,
\end{equation}
exists.
\end{itemize}
\end{lemma}
```

### 14.8. 7.5:prf-limit-distributions

Source: theorem_0_complete_account_raw_II.tex:67014–67042. Status at the source heading: proved implication.

```latex
\begin{lemma}[The limits as distributions off the diagonals]\label{7.5:prf-limit-distributions}
Assume the standing data of the infinite-volume theorem, Theorem~\ref{7.4:thm-infinite-volume}.
Let $n\ge 2$, and let $S^T_n$ be the limit functional on $\mathfrak{S}_n$ defined by
\eqref{7.4:eq-equicontinuity-b}. Put
\begin{equation*}
(\mathbb{R}^4)^n_{\neq}:=\{(x_1,\dots,x_n)\in(\mathbb{R}^4)^n:\ x_i\neq x_k\ \text{for all } i\neq k\}.
\end{equation*}
\begin{itemize}
\item[(a)] Let $R>0$ and $\mathsf{d}>0$, and let $G_1,\dots,G_n\subset\mathbb{R}^4$ be open sets, each
of diameter at most $2R$, pairwise at distance at least $\mathsf{d}$. There is a unique
distribution $T_G\in\mathcal{D}'(G_1\times\dots\times G_n)$ such that
$T_G(\varphi_1\otimes\dots\otimes\varphi_n)=S^T_n(\vec\varphi)$ for all real-valued
$\varphi_i\in\mathcal{D}(G_i)$, a space we denote $\mathcal{D}(G_i;\mathbb{R})$.
\item[(b)] There is a unique distribution on $(\mathbb{R}^4)^n_{\neq}$, again written $S^T_n$, whose
restriction to $G_1\times\dots\times G_n$ is $T_G$ for every family $(G_i)$ as in \textup{(a)}
(with any $R>0$ and $\mathsf{d}>0$).
\item[(c)] For $(G_i)$ as in \textup{(a)}, finite sums of tensors $\varphi_1\otimes\dots\otimes\varphi_n$
with $\varphi_i\in\mathcal{D}(G_i)$ are dense in $\mathcal{D}(\prod_iG_i)$. Moreover, if
$\chi_i\in\mathcal{D}(G_i;\mathbb{R})$ are given, there is a constant
$C=C(n,\mathsf{d},R,G,\chi)$ such that
\begin{equation}\label{7.5:eq-limit-distributions-a}
|T_G(\Phi)|\le C\,\|\Phi\|_{C^{5n+1}}
\end{equation}
for every $\Phi\in\mathcal{D}(\prod_iG_i)$ such that each $\chi_i$ is identically $1$ on a
neighbourhood of the projection of $\operatorname{supp}\Phi$ to the $i$-th factor. Thus $T_G$ has
order at most $5n+1$ on $\prod_iG_i$, and the distribution $S^T_n$ of \textup{(b)} has locally finite
order on $(\mathbb{R}^4)^n_{\neq}$.
\end{itemize}
\end{lemma}
```

### 14.9. 7.5:prf-exact-invariance

Source: theorem_0_complete_account_raw_II.tex:67131–67168. Status at the source heading: proved implication.

```latex
\begin{lemma}[Exact invariance under translations and signed permutations]\label{7.5:prf-exact-invariance}
Assume the standing data of the infinite-volume theorem, Theorem~\ref{7.4:thm-infinite-volume}.
Let $\mathcal{J}$ be the diagonal subsequence of \eqref{7.4:eq-infinite-volume-d}. For $n\ge 2$ let
$S^T_n$ be the limits along $\mathcal{J}$ given by \eqref{7.4:eq-equicontinuity-b}. Let
$\mathfrak{S}_n$ be the class of separated real $C^1$ tuples of Lemma~\ref{7.4:prf-equicontinuity},
on which these limits are defined; we recall that its elements are the $n$-tuples of real $C^1$
functions of compact support on $\mathbb{R}^4$ with pairwise disjoint supports. For
$a\in\mathbb{R}^4$ put $\tau_a f:=f(\cdot-a)$. For
a signed permutation of the coordinates $\eta\in W_4$ put $(\eta\cdot f)(x):=f(\eta^{-1}x)$. Both actions
are applied componentwise to tuples.
\begin{itemize}
\item[(a)] For every $n\ge 2$, every $\vec f=(f_1,\dots,f_n)\in\mathfrak{S}_n$, every
$a\in\mathbb{R}^4$, every $\eta\in W_4$ and every permutation $\sigma$ of $\{1,\dots,n\}$,
\begin{equation}\label{7.5:eq-exact-invariance-1}
S^T_n(\tau_a f_1,\dots,\tau_a f_n)=S^T_n(f_1,\dots,f_n)=S^T_n(\eta\cdot f_1,\dots,\eta\cdot f_n)
\end{equation}
and
\begin{equation*}
S^T_n(f_{\sigma(1)},\dots,f_{\sigma(n)})=S^T_n(f_1,\dots,f_n).
\end{equation*}
\item[(b)] Let $q\ge1$ and let $\mathcal{T}^{\mathrm{sep}}_q$ be the linear span of the tensors
$f_1\otimes\dots\otimes f_q$ with $(f_1,\dots,f_q)\in\mathfrak{S}_q$. Let
$\mathbb{R}^4\rtimes W_4$ act on such tensors factorwise through $f\mapsto\tau_a(\eta\cdot f)$. For
$F\in\mathcal{T}^{\mathrm{sep}}_q$ let $S_q(F)$ be the limit Schwinger function of $q$ arguments
of the infinite-volume theorem, Theorem~\ref{7.4:thm-infinite-volume}, that is, the limit along
$\mathcal{J}$ of the centred moments of Definition~\ref{7.4:def-centred-moments}, taken on the
transported factors; on
$f_1\otimes\dots\otimes f_q$ it equals the sum over partitions $\pi\in\operatorname{Part}_{\ge2}[q]$
of the products, over the blocks $B$ of $\pi$, of the cumulants $S^T_{|B|}$ of the subtuples
$(f_i)_{i\in B}$, which exist by \eqref{7.4:eq-equicontinuity-b}, and it is linear in $F$. Then
\begin{equation}\label{7.5:eq-exact-invariance-a}
S_q\bigl((a,\eta)\cdot F\bigr)=S_q(F)\qquad
\text{for all } F\in\mathcal{T}^{\mathrm{sep}}_q,\ (a,\eta)\in\mathbb{R}^4\rtimes W_4 .
\end{equation}
In particular $S_q$ is invariant under the reflection $\theta$ of the time coordinate and
under all time and space translations.
\end{itemize}
\end{lemma}
```

### 14.10. 7.6:prf-centred-positivity

Source: theorem_0_complete_account_raw_II.tex:67312–67352. Status at the source heading: proved implication.

```latex
\begin{lemma}[Reflection positivity of the centred limit]
\label{7.6:prf-centred-positivity}
Let the standing data of the infinite-volume theorem (Theorem~\ref{7.4:thm-infinite-volume}) be in
force, let $\mathcal{J}$ be the diagonal subsequence of \eqref{7.4:eq-infinite-volume-d}, and write
$\langle\cdot\rangle_j:=\langle\cdot\rangle_{K_j,m_j}$ and $S_{q;j}:=S_{q;K_j,m_j}$. Put $S_0:=1$,
$S_1:=0$,
$\mathcal{T}^{\mathrm{sep}}_0:=\mathbb{C}$ and $\Phi_{K,m}(c):=c$ for $c\in\mathbb{C}$. Recall that
$\mathcal{P}_+=\bigoplus_{q\ge 0}\mathcal{T}^{\mathrm{sep}}_{q,+}$, where
$\mathcal{T}^{\mathrm{sep}}_{0,+}=\mathbb{C}$ and, for $q\ge 1$, $\mathcal{T}^{\mathrm{sep}}_{q,+}$ is
the complex span of the tensors $f_1\otimes\cdots\otimes f_q$ of real $f_a\in C^1_c(\mathbb{R}^4)$
with compact, pairwise disjoint supports contained in $\{x^0>0\}$. Then the following hold.
\begin{enumerate}
\item[(a)] Let $q\ge 2$ and $F\in\mathcal{T}^{\mathrm{sep}}_q$, all supports in some $B_{\rho}$. For
$j\in\mathcal{J}$ with $L^{m_j}\ge 2\rho+2$ the number
$S_{q;j}(F):=\langle\Phi_{K_j,m_j}(F)\rangle_j$ is well defined, the limit
\begin{equation*}
S_q(F):=\lim_{j\in\mathcal{J}}S_{q;j}(F)
\end{equation*}
exists, it is linear in the function $F$, and on a separated tensor $h_1\otimes\cdots\otimes h_q$ it
equals
\begin{equation}\label{7.6:eq-centred-positivity-1}
S_q(h_1\otimes\cdots\otimes h_q)
=\sum_{\pi\in\operatorname{Part}_{\ge 2}[q]}\ \prod_{B\in\pi}S^T_{|B|}\bigl((h_l)_{l\in B}\bigr).
\end{equation}
\item[(b)] The form $(\cdot,\cdot)_{\mathrm{OS}}$ of \eqref{7.4:eq-infinite-volume-b} is
sesquilinear, Hermitian and positive semidefinite on $\mathcal{P}_+$, and for
$F=(F_q)_q$, $G=(G_q)_q\in\mathcal{P}_+$
\begin{equation}\label{7.6:eq-centred-positivity-2}
(F,G)_{\mathrm{OS}}=\lim_{j\in\mathcal{J}}
\bigl\langle\overline{\mathbb{F}_j(\theta\cdot U)}\,\mathbb{G}_j(U)\bigr\rangle_j,
\qquad
\mathbb{F}_j:=\sum_q\Phi_{K_j,m_j}(F_q),\quad \mathbb{G}_j:=\sum_q\Phi_{K_j,m_j}(G_q).
\end{equation}
\item[(c)] Let $(\mathbb{R}^4)^q_{\neq,+}:=\{x\in(\mathbb{R}^4)^q_{\neq}:x_a^0>0\ \text{for all } a\}$.
For every $q_0$ and every finite sequence $F_q\in\mathcal{D}((\mathbb{R}^4)^q_{\neq,+})$, $q\le q_0$,
\begin{equation}\label{7.6:eq-centred-positivity-3}
\sum_{q,q'\le q_0}S_{q+q'}\bigl((\Theta\bar F)_q\otimes F_{q'}\bigr)\ \ge\ 0,
\end{equation}
where $S_{q+q'}$ is the distribution on $(\mathbb{R}^4)^{q+q'}_{\neq}$.
\end{enumerate}
\end{lemma}
```

### 14.11. 7.7:prf-reconstructed-space

Source: theorem_0_complete_account_raw_II.tex:67528–67559. Status at the source heading: proved implication.

```latex
\begin{lemma}[The reconstructed space and bounds uniform in time]\label{7.7:prf-reconstructed-space}
Assume the standing data of the infinite-volume theorem, Theorem~\ref{7.4:thm-infinite-volume}.
Let $\mathcal{P}_+$ and the Osterwalder--Schrader form $(\cdot,\cdot)_{\mathrm{OS}}$ be as in
\eqref{7.4:eq-infinite-volume-b}, let $\mathsf{T}_t$ be as in \eqref{7.4:eq-infinite-volume-c},
and write $\mathbb{1}:=(1,0,0,\dots)\in\mathcal{P}_+$.
\begin{enumerate}
\item[(a)] The set $\mathcal{N}:=\{F\in\mathcal{P}_+ : (F,F)_{\mathrm{OS}}=0\}$ is a linear subspace
of $\mathcal{P}_+$, and $(\cdot,\cdot)_{\mathrm{OS}}$ descends to an inner product on
$\mathcal{P}_+/\mathcal{N}$. Its completion $\mathcal{H}^{\mathrm{curv}}$ is a separable Hilbert
space. Writing $[F]$ for the class of $F$, the vector $\Omega:=[\mathbb{1}]$ satisfies
$\|\Omega\|=1$.
\item[(b)] Let $F\in\mathcal{P}_+$ be written with real tensors. Define three quantities:
\begin{itemize}
\item for each test function occurring in $F$ choose a closed ball containing its support, and let
$R_F$ be the largest of the radii of these balls; every occurring function is then supported in a
ball of radius $R_F$;
\item $\mathsf{d}_F$ is the least distance between two supports within one tensor term;
\item $\delta_F$ is the least distance of an occurring support from the plane $\{x^0=0\}$.
\end{itemize}
Here a minimum over the empty set is $+\infty$; if $F=F_0$ all claims below are trivial.
Then $\mathsf{d}_F>0$ and $\delta_F>0$. Moreover, for every $t\ge 0$, each connected function
arising when $(F,\mathsf{T}_tF)_{\mathrm{OS}}$ is expanded by \eqref{7.4:eq-infinite-volume-b}
into connected functions is evaluated at a separated real
$C^1$ tuple with supports in balls of radius $R_F$, at mutual distances at least $\mathsf{d}_0$,
where
\begin{equation}\label{7.7:eq-reconstructed-space-a}
\mathsf{d}_0:=\min\{\mathsf{d}_F,2\delta_F\}>0,\qquad
M_F:=\sup_{t\ge 0}\,(F,\mathsf{T}_tF)_{\mathrm{OS}}<\infty .
\end{equation}
The separation $\mathsf{d}_0$ does not depend on $t$.
\end{enumerate}
\end{lemma}
```

## Result

**Port completed: B10–B13, as conditional implications.** B10 includes the five requested finite lemmas, finite conventions, centred-moment algebra, tensor-presentation independence, and the support-adapted countable family. B11 includes the single joint extraction, equicontinuity, every separated $C^1$ tuple, the limit structure and bounds, and the cluster-point and iterated-limit deductions. B12 includes the off-diagonal distributions, their exact translation/$W_4$ invariance, and centred positivity on both stated test domains. B13 supplies the separable curvature Hilbert space and the time-uniform individual-ball bound. The continuation `7.7:prf-semigroup-hamiltonian`, through **CA-II:68079**, completes B11(D1)–(D3). All eleven requested numbered statements appear literally in §14, with their source lines and declared standing. Part 1 was not redone.

**Filled steps.** These include the finite moment/cumulant algebra; support-space separability and the diagonal selection; moving-test continuity; degree-zero and zero-factor cases; the Fourier coefficient/tail estimate giving order $5n+1$; unbounded product charts; the moment distribution in disjoint variables; positive-time tensor density; Cauchy–Schwarz and the quotient; constant-vector separation conventions; positivity of the time-orbit scalar before quotient operators; spatial strong continuity; and the Hamiltonian and vacuum-momentum domains. Every argument is written by hand. No program, numerical estimate, search, or enumeration discharges a proof step.

**Corrections.** The lattice-translation proof needs preservation of the quotient equivalence relation, not preservation of the period lattice as a set (§4.1, II:65871–65872). A zero source is handled before using the finite-radius approximation formula (§8.2). The Hamiltonian has the explicit dense domain (42); the source's “whole”/“all” wording is not used to assert an everywhere-defined unbounded operator (§13.3, II:66562,67995). The vacuum normalization and LSC coupling/volume admission conditions are inherited from frozen LSC and part 1 (§1.2); no new bare-floor assertion is made.

**Named hypotheses.** H-CA and H-FLOW retain the actual RG, source, first-passage, and torus-independence antecedents. H-PB retains part 1's H-LOC, H-DOM, H-STAB/LSC and Balaban's H-TREE, including the outstanding source/window suppliers. H-RP is supplied by the unreviewed part-1 port in its precise lattice geometry. H-BLOCK remains the separate countable-skeleton-to-state implication. H-AN, H-KER, H-FOURIER, and H-SPEC are the explicitly retained classical analysis inputs. The iterated-limit remark has its own stated fixed-volume convergence hypotheses. Their standing is not changed by this port.

This is a port and completion of Ethan Sussman and Levent Alpoge's proof route, with Claude and Codex credited as authors of their text and Tadeusz Balaban credited for the underlying construction. It is research text, not an audit, and grants no status. It does not establish full T0 or the clauses excluded in §13.5. **This text is not yet checked by another model.** Only this output file was written. Source-transcription, formatting, and path checks are editorial bookkeeping, not mathematical verification.
