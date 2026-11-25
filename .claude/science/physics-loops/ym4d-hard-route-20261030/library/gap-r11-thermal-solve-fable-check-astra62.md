## Repo search

Row 1523 · OpenAI Codex (assigned gpt-6.2-astra, max) · cross-provider hand check of Claude Fable 5.2's row 1522 at `729e35b53062`. Research text only. Unqualified line numbers refer to [row 1522](gap-r11-thermal-solve-fable.md).

Markdown and TeX refs searched were `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). ABS-band, gap-r11-thermal-solve, two-family rate, Proposition CB1, Corollary ABS and lukewarm cube returned no hits on those refs. The target search outside this lane also returned none. The row-specific prior file is absent. The November 8 digest's one-step Wilson-loop correlation concerns another observable. Registry line 1018 assigns R11 to 1517 and names proof row 1522. [November 8 digest, §11](prior/repo-search-2026-11-08.md#11-w1w2w5-witness-matching) · [Registry](open-registry.md)

- VIR_K, VIR-log, NOCRIT, BAND-sc and Remark N2 lead to identical main/lane sources under `research/mass-gap/library/`. Row 708 transports along one characteristic and defines NOCRIT by existence of a ratio-four seed at every coupling. Row 710 gives U′, the integer-time differentiated trace in SUF, and B1 with the gap in its denominator. Row 705 supplies the shape recursion. Row 697 supplies the integer gas used in (vii). [Transport](gap-mid-max.md) · [Level bounds](gap-vir-sc.md) · [Shapes](gap-seed-shape.md) · [Integer gas](gap-crux-restate.md)
- In this checkout, row 905 (R) gives the energy-weighted mean of level rates. Row 934 gives a conjectural avoided crossing. Row 910's two-phase example uses a time trace and free spatial walls. Rows 1517/1519 give the restart and its conditional U(1) endpoint. Row 1521, lines 94–103, supplies the real-power derivative used in (i). [Thermal ratio](gap-thermdi-astra.md) · [Avoided crossing](gap-vacsub-max.md) · [Free-wall example](gap-cutth-max.md) · [Restart check](gap-r11-tool-design-fable-check-astra62.md) · [Real powers](gap-twoperiod-solve-fable-check-astra62.md)
- Potts, latent heat, two-family and Borgs–Kotecký/Imbrie locate the periodic magnetization profile and conditional transfer crossover results. The abstracts in the digests give no estimate of both differentiated sums in (vi). The broad two-family search was capped. Targeted flat-wall, parallel-interface, striped-plaquette and slab-spin terms found no matching construction. The van Enter–Shlosman reading records a normalization issue for the nonlinear gauge weight. [Main literature hit, line 71](prior/gap-math-lit.md) · [Crossover results](prior/gap-lit-casimir.md) · [Gauge-weight reading](prior/gap-ves-read.md)
- In the Sussman–Alpoge snapshot `31a47c543775` (with Claude and Codex), outline 2197–2257 (GL3–4) proves the SU(2) Bessel coefficients and ratio bounds, and 2315–2335 (GL8) gives the gauge-projected torus trace. Outline 4638–4641 requires a separate spectral estimate. CA-I 2699–2709 gives a nonnegative Hamiltonian and excludes a gap from its conclusions. No Bałaban estimate enters. [Index and neighbouring rows](sa-index/chunk-02.md) · [Obligations](sa-index/obligations.md)

## (i) Proposition CB1 — HOLDS

No wrong line in the statement, lines 75–82. For $0<s<4$ let $V=|B|$, $\rho_i=\lambda_i/\lambda_0=e^{-E_i}$ and $d_i=\langle\psi_i,T'(s)\psi_i\rangle/\lambda_i$. Sum the positive excited eigenvalues with multiplicity. Then $S=\sum_{i>0}\rho_i^t>0$, $G=\log(1+S)$, $m=E_1$ and $\bar E_t=S^{-1}\sum_{i>0}E_i\rho_i^t$. At integer $t\ge4$ the differentiated trace in SUF gives

$$
G_s=\frac{t}{1+S}\sum_{i>0}(d_i-d_0)\rho_i^t,\qquad
-tG_t=\frac{t}{1+S}\sum_{i>0}E_i\rho_i^t .
$$

Line 86 checks the energy sum. For the signed sum use $|d_i|\rho_i^t\le(\|T'\|/\lambda_0)\rho_i^{t-1}$, while $E_i\rho_i^t\le e^{-1}\rho_i^{t-1}$. Both majorants are summable since $0<\rho_i\le1$ and $\sum_i\rho_i=\operatorname{Tr}T/\lambda_0<\infty$. These are trace diagonals, so any orthonormal basis of a multiple eigenspace works. Multiplying U′ by $\rho_i^t/s$ and summing adds exactly $c_s VtS/(1+S)$ to $(-tG_t)/(s\log(4/s))$, where $c_s=9+12/\log(4/s)$. Division by $-tG_t>0$ gives $c_s V/\bar E_t$ for the additive rate. Since $S\ge e^{-tm}$, $\bar E_t\ge m\ge t^{-1}\log(1/S)$. Thermal weighting retains the spatial volume.

For $G<1/1000$, the exponential series gives $S\le G/(1-G/2)<2/1999<0.0010006$. Also $\log(1999/2)=10\log 2-\log(1+49/1999)>6.9$, using $\log 2>2(1/3+1/81+1/1215)$ and $\log(1+x)\le x$. For $s\le2$, $c_s\le9+12/\log 2<26.4$, and $26.4/6.9<3.83$. For $t\le L/2$, $3.83tL^3\le1.915L^4<1.92L^4$.

The earlier bound on the same numerator at line 68 is false across the range of U′. If $\delta_t\le2S/(1+S)$ held on a fixed cube at all small $s>0$, the plaquette identity would give $S_s\le12tV S$ at integer $t\ge4$, first off the countable exceptional set and then by continuity of $S_s$. Hence $S(s)\le e^{12tV(s-\eta)}S(\eta)$. At zero the transfer is rank one, so continuity gives $S(\eta)\to0$. Yet at $s>0$ the positive Peter–Weyl coefficients and invertible spatial weight make the transfer form strictly positive on the two-dimensional span of the constant and a nonconstant invariant plaquette trace. Thus $S(s)>0$. The actual U′ bound includes the energy term used in CB1. The isolated factor $tV/\log L$ compares its extensive rate term on the band with the desired logarithm. [Transfer construction](gap-transfer.md) · [Plaquette identity](gap-mid-max.md)

**Real periods.** Row 1521 resolves the limitation reported at lines 98–99 and 356. On the full invariant space the shifted Wilson slab is a positive contraction, its bounded kernel is $C^1$ in Hilbert–Schmidt norm, and its simple isolated top is differentiable. Thus row 1521's trace argument applies to $T$ at every real $t>2$. Divide $(\operatorname{Tr}T^t)'=t\operatorname{Tr}(T^{t-1}T')$ by $\operatorname{Tr}T^t$ and subtract $t\lambda'_0/\lambda_0$. This gives the first sum, including at crossings. Differentiation in $t$ gives the second by the locally summable energy majorant. CB1 follows for all real $t\ge4$. [Row 710, lines 35–41, 89–98, 169](gap-vir-sc.md) · [Row 1521, §(viii)](gap-twoperiod-solve-fable-check-astra62.md)

## (ii) Remark BAND — HOLDS

No wrong line at 110–121. Keep a continuous $K_L\ge0$ on the interval and $\tau'=K_L\tau$ throughout. Only its differential inequality is restricted to band points. If $\phi(s)=G(\tau(s);L^3;s)$ exceeds $\epsilon_0=0.000505$, choose a value $c$ strictly between $\epsilon_0$ and the smaller of the higher value and $0.001$. Before the first hit of $c$, take the last point $u$ with $\phi(u)=\epsilon_0$ (the entrance may be below it). Up to the hit $v$, $\epsilon_0\le\phi\le c<0.001$. At each $s\in[u,v)$ the time difference quotient tends to $K_L\tau G_t$ by joint continuity of $G_t$, and the fixed-time upper right derivative is at most $-K_L\tau G_t$. Thus $D^+\phi\le0$ there. The continuous Dini comparison in row 708 gives $\phi(v)\le\phi(u)$, contradicting $c>\epsilon_0$. No derivative at $v$ is needed, even if $v$ is the right endpoint. [Row 708, lines 120–134](gap-mid-max.md)

## (iii) Corollary ABS — HOLDS

No wrong line at 128–134. For **real** $t\ge4$, $S/(1+S)=1-e^{-G}\ge G-G^2/2>0.000504$ on the band. Therefore

$$
-tG_t=\frac{S}{1+S}\,t\bar E_t
\ \ge\ \frac{S}{1+S}\log(1/S)
\ >\ 0.000504\cdot6.9=0.0034776>0.0034 .
$$

The coefficient in (ABS) works for $C\ge0$. The first wrong **converse estimate** is line 140. Inserting $t\bar E_t=O(\log L)$ into the relative bound gives $O((\log L)^2)$. For this black-box conversion one needs $-tG_t=O(1)$, equivalently $t\bar E_t=O(1)$ on the stated band. A separate cancellation in $G_s$ could prove ABS directly. The sufficient implication in lines 128–131 survives.

## (iv) Lemma SQ and Proposition HI — HOLDS

**SQ.** No wrong line at 154–159. Fix $t$ and an admissible $h$. Here $e=\log\lambda_0$ and $G=F-te$. The upper Taylor remainder for $F=\log Z$ on $[s-h,s]$ is at most $Mh^2/2$, since $F''$ is the variance of the total action. Convexity gives $-te(s-h)\le-te(s)+th e'(s)$. Addition gives $0\le G(s-h)\le G(s)-hG'(s)+Mh^2/2$. The choice $h=\sqrt{2G(s)/M}$ works for $M>0$ when $0<h<s$ and **the same $M$ bounds $F''$ on that chosen interval**. With $M=0$ the unoptimized inequality still applies. No susceptibility estimate enters SQ. [Row 708, Lemma 4.2](gap-mid-max.md)

**HI.** No wrong line at 170–182 for $S(t)>0$. Summing the assumed low-level bound and U′ on $E_i\ge\Lambda$ gives line 173, including equality levels in the upper range. The tail estimate follows from

$$
\sum_{E_i\ge\Lambda}e^{-tE_i}\le e^{-t\Lambda/2}S(t/2),
\qquad S(t)\ge e^{-tm}.
$$

With $S(t/2)\le1$ we have $0<S(t)\le e^{-tm/2}S(t/2)<1$. Write $z=\log(1/S(t))>0$. The additive term in HI is at most $(c_s Vt/z)e^{-(\Lambda-2m)t/2}$. The printed $\Lambda$ makes this **upper bound** one. The cutoff is positive even when its logarithmic correction is negative, since $t\Lambda/2\ge z-\log z+\log(c_s Vt)>0$. On the cold cubes of CB1 its increment is at most $\tfrac12\log(1.92L^4)<2\log L+0.33$ (the cubic Taylor lower bound gives $e^{0.66}>1.92$). In line 185's shortened cutoff one can omit $0.33$ for $L\ge16$ because $(2/t)\log(3.83tL^3)$ decreases for $t\ge4$ and at 4 is $\tfrac12\log(15.32L^3)\le2\log L$. The hypothesis at half-time is additional. The trace argument in (i) also permits a real $t\ge4$ whenever the stated half-time sum is bounded. [Row 710, SUF and BAND-sc](gap-vir-sc.md)

## (v) Compact U(1) — HOLDS AFTER CORRECTION

The Fourier calculation and the CB1 inequality through line 224 hold. For the cosine weight $c_{s,n}=e^{-s}I_{|n|}(s)$, where $I_k$ is the positive series called $J_k$ in row 710. Fourier expansion gives $\sum_{n\in\mathbb Z}c_{s,n}=1$. Thus product convolution is a positive trace-class contraction. On each character, $s(\log c_{s,n})'=|n|-s(1-r_{|n|})$ and $0<r_k\le s/(2(k+1))\le1$ for $s\le2$. The factorial series gives $c_{s,n}\le(s/2)^{|n|}/|n|!$, using $\sum_j((s/2)^j/j!)^2\le e^s$. Hence $\eta_n\ge|n|\log(2/s)$ for $0<s<2$, including $n=0$. Gauge averaging preserves the Fourier blocks.

The spatial half-weights are at least $e^{-3sV}$ and the product convolution has a positive integral kernel. Testing the constant unit vector gives $\lambda_0\ge e^{-6sV}c_{s,0}^{3V}\ge e^{-9sV}$. The gauge-averaged sandwich is positivity improving, with simple top. Sewing gives the same Haar-normalized trace in each direction. The kernel and its derivative are bounded at fixed box on compact coupling intervals. These facts justify the trace derivative above and the differentiation of the simple top. Rellich–Kato (RK), recalled in row 710, suffices for a statement about analytic excited branches. The thermal sum only uses trace diagonals. [Row 1519, §(iii)](gap-r11-tool-design-fable-check-astra62.md) · [Row 710, Lemmas J, C and (RK)](gap-vir-sc.md)

U(ii) has $R=\sum_\ell(1-r_{|n_\ell|})\in[0,3V]$ and $0\le V_1\le6V$. U(iii)'s entropy inequality gives $\langle N\rangle\log(2/s)\le-\log\lambda$. Subtract the vacuum as in U′, using $-d_0\le9V$ and $-\log\lambda_0\le9sV$. The result is line 224 with the **smaller** coefficient $9+9/\log(2/s)$ in front of $V/\bar E_t$. Its printed larger coefficient is valid.

The first overstatement is line 226. BAND and ABS only need the trace and its regularity. INT needs the derivative of an action with the specified plaquette normalization. HI needs a U′ estimate. For U(1) its numerical cutoff uses a bounded replacement for $c_s$. The $26.4$ bound works on $s\le1$ with $\log(2/s)$ and the printed larger coefficient. It is unavailable uniformly as $s\uparrow2$. Line 227's necessity claim also needs the endpoint premise of FLOOR. The finite-volume class and a small-coupling start are supplied. Absence of a seed at a **fixed periodic Wilson-cosine** weak-coupling endpoint is open in the cited work. Given that endpoint, TR2 excludes a logarithmic bound throughout the interval and band. It selects neither a failure at any prescribed coupling below 2 nor the family proposed in §5.3. [FLOOR, endpoint and boundary conditions](gap-r11-tool-design-fable-check-astra62.md) · [Periodic Wilson score, (24)](gap-tu-retry.md)

## (vi) The two-family rate at a first-order point — HOLDS AFTER CORRECTION

**Existence in row 705's class holds as an asymptotic theorem.** The first unsupported identification for a general model is at lines 232–234. Row 934 explicitly labels its avoided crossing a guide. At line 238 the last equality requires $S=g e^{-tV\Delta}$ exactly. Dominance in $S$ alone gives no error estimate for either differentiated sum. Also $12<c_s$ at line 240 fails for $\log(4/s)\ge4$. The numerator coefficient in a class example is the jump of its own conjugate density.

Fix $s_c$ in the interior of the coupling interval, $J=\log 2$ and $\alpha=(\log 2)/s_c$. On a four-dimensional rectangular torus put spins $\sigma_x=\pm1$. Each plaquette must be constant or consist of two parallel equal-spin pairs with opposite signs. A plus site has two internal states, a minus site one. An agreeing bond has two internal states, a disagreeing bond one. The fixed energy is $\alpha N_+$, where $N_+$ counts plus sites. Summing the internal states in the Gibbs weight $e^{-s\alpha N_+}$ leaves, up to the bulk factor $2^{4W}e^{hW}$ on $W$ sites,

$$
\exp\!\left(h\sum_x\sigma_x-J\sum_{\langle xy\rangle}\mathbf1_{\sigma_x\ne\sigma_y}\right),
\qquad h=\tfrac12(\log 2-\alpha s) .
$$

A disagreeing bond forces its opposite bond on every transverse plaquette to disagree with the same orientation. Translation along those plaquettes extends the disagreement across a whole coordinate hyperplane. Walls of two different normals would meet on a forbidden plaquette. Thus every nonconstant configuration is a stack of constant planes perpendicular to one axis. In an $N^4$ torus the count is at most $4\cdot2^N$. For the reduced spin sum the favored constant configuration contributes $e^{|h|N^4}$ and every spin weight is at most that value. Its limiting pressure is $|h|$. Restoring the bulk factor gives $4\log 2+h+|h|$, whose derivative jumps by $\alpha$ at $s_c$. Thus the model has latent heat in the coupling being differentiated. The bulk factor cancels from $G$.

For a fixed time direction and spatial cube of volume $V=L^3$, the two constant slices form the block

$$
M=\begin{pmatrix} e^x&d\\ d&e^{-x}\end{pmatrix},\qquad
x=hV,\quad d=e^{-JV},\qquad
\lambda_\pm=\cosh x\pm\sqrt{\sinh^2x+d^2}.
$$

A nonconstant admissible slice $\xi$ must repeat unchanged. Its transfer eigenvalue is $\exp(h\sum_y\xi_y-Jw(\xi))$, where $w$ counts its disagreeing spatial bonds. Sewing gives the periodic trace. The block is positive definite since $\det M=1-d^2>0$, and $\lambda_+>e^{|x|}$ strictly dominates every static eigenvalue. The same construction works with any three transverse sides and any time axis. The transfer is positive, finite dimensional and has a simple top. The rectangular partition functions are axis symmetric, with finite lower pressure by the constant configuration. These are the hypotheses of row 705, lines 56 and 207. [Class and Ising slice construction](gap-seed-shape.md)

Fix $u=\log 1500$, take even $L\to\infty$, $t=L/2$ and $s_L=s_c-u/(\alpha tV)$. All derivatives below are *partial derivatives*, evaluated at this pair. For the other block level $E=\log(\lambda_+/\lambda_-)$,

$$
tE\longrightarrow u,\qquad
-E_s=\alpha V\,\frac{\sinh x}{\sqrt{\sinh^2x+d^2}}=\alpha V(1+o(1)).
$$

Indeed $x=u/(2t)$, $0\le\lambda_+-e^x\le d$, and $E=2\log\lambda_+-\log(1-d^2)$. Differentiating the displayed eigenvalue gives $(\log\lambda_+)_x=\sinh x/\sqrt{\sinh^2x+d^2}$. There are at most $3\cdot2^L$ nonconstant slices. Each has $w(\xi)\ge2L^2$ by periodicity, hence normalized energy $E_\xi\ge2JL^2$. Also $E_\xi=O(V)$ and $|E_{\xi,s}|\le\alpha V$ from its diagonal entry and $|(\log\lambda_+)_x|\le1$. Their total contributions to the trace, its energy moment and its coupling-score moment are each $O(V2^L e^{-2JtL^2})=o(1/t)$. Consequently $S\to1/1500$ and $G\to\log(1+1/1500)$ strictly inside the band. Row 905's exact ratio now gives

$$
\frac{G_s}{-tG_t}
=\frac{\sum_{i>0}(-E_{i,s})e^{-tE_i}}{\sum_{i>0}E_i e^{-tE_i}}
\ \sim\ \frac{\alpha tV}{u}
\ \sim\ \frac{\alpha tV}{\log(1/S)} .
$$

This realizes §5.2 with $g=1$ and density jump $\alpha$, on an explicit sequence. First order **alone** cannot guarantee it. Tensor this family with an independent copy held at $h=0$. Its pressure is independent of $s$. The product has the same kink and still belongs to the class. The spectator has a level of energy $\log((1+d)/(1-d))$. Its weight tends to one uniformly for $4\le t\le L/2$, so the product has no band points on large cubes.

For the suggested ferromagnetic $q$-state Potts model, the periodic transfer is $D[(e^s-1)I+\mathbf1\mathbf1^\top]^{\otimes V}D$ with $D$ the positive spatial half-weight. At $s>0$ this is positive definite and entrywise positive, its top is simple, and axis symmetry gives the other traces. Bounded interaction gives finite pressure per site. Thus Potts lies in the class. Even granting its large-$q$ first-order transition, the cited periodic magnetization profile alone supplies neither the derivative of the cylinder vacuum nor the real-time energy moment with its error on the tuned band. The Potts rate remains unverified here. The spin example proves sharpness for the abstract trace class. It gives no exclusion specific to smooth SU(2) plaquette weights in lines 246–249. [Borgs–Kotecký and Borgs–Imbrie readings](prior/gap-lit-casimir.md)

## (vii) ABS-band versus NOCRIT — HOLDS AFTER CORRECTION

Lines 280–284 give the correct implication. For a fixed finite endpoint $\beta_1>\beta_0=1/25600$, suppose ABS-band holds with a single pair $C_1,L_0$ for **all** sufficiently large even sides, all real $4\le t\le L/2$ on the band, and $\beta_0\le s<\beta_1$. Set $K_L=\max(1,C_1/0.0034)\log L$. Parts (ii)–(iii) give exactly the comparison at each band point. TR2 starts from the strong-coupling seed and restarts on larger cubes. At every $s\in[\beta_0,\beta_1]$, including the endpoint by continuity, it produces $S(a;(2a)^3)<0.00051$. The ratio-four enlargement gives $S(a;(4a)^3)\le0.0396<1/25$. Together with the known start below $\beta_0$, this is interval NOCRIT. Global NOCRIT asks for every finite endpoint. [Row 1517, lines 151–191](gap-r11-tool-design-fable.md) · [Row 708, lines 188–207](gap-mid-max.md)

No line in 283–284 asserts the reverse implication. The first unsupported reading would be to take “restatement of the trigger” at 284–285 as equivalence. Line 140 supplies no reverse estimate even for the relative trigger. In the abstract trace class with TR2's coupling continuity, ABS-band is **strictly stronger**. Use the integer gas of row 697, Remark N2, with $f=0,c=1,q(s)=e^{-m(s)}$ and $m(s)=4+\sqrt{|\beta_1-s|}$. Its symmetric partition function is $\prod_\mu(1-q(s)^{n_\mu})^{-|n|/n_\mu}$. In direction $t$ the other three factors are a vacuum eigenvalue to power $t$, and $(1-e^{-mt})^{-V}$ expands with multiplicities $\binom{V+j-1}{j}$ at normalized energy $jm$. The resulting transfer operator has a simple top and finite trace. In particular

$$
G(t;L^3;s)=-L^3\log(1-e^{-m(s)t}).
$$

Since $m\ge4$, $G(a;(4a)^3;s)\to0$ as $a\to\infty$ uniformly in $s$. Seeds exist even at $\beta_1$. Fix $\gamma=\log(1+1/1500)$, $s_L=\beta_1-L^{-2}$ and choose $e^{-m(s_L)t_L}=1-e^{-\gamma/L^3}$. Then $G=\gamma$ and $m(s_L)t_L=3\log L-\log\gamma+o(1)$, so $4\le t_L\le L/2$ for all sufficiently large even $L$. At fixed $t=t_L$,

$$
\partial_sG
=\frac L2\,t_L L^3(e^{\gamma/L^3}-1)
\ \ge\ \frac{\gamma}2 L t_L .
$$

This family also tests line 140 pointwise. At $s=\beta_1-(\log L)^{-2}$ on the same level $G=\gamma$, the relative rate is $-m'/m=O(\log L)$ and $t\bar E_t=O(\log L)$, while $G_s$ grows as $(\log L)^2$.

On the sequence $s_L=\beta_1-L^{-2}$ the family violates every $C_1\log L$ on the interval. Its finite-box traces are analytic at every tested $s<\beta_1$ and continuous at the endpoint. The square-root parametrization there is allowed by the abstract consumer. It changes the coupling law and therefore does not decide a converse for the **fixed bare Wilson action**. For that action the established direction is ABS-band $\Rightarrow$ interval NOCRIT. A converse is open. In particular ABS-band cannot count as a strictly weaker Wilson target. [Integer gas, line 141](gap-crux-restate.md) · [TR2 hypotheses](gap-r11-tool-design-fable.md)

**Disposition for the R11 entry.** Adopt the band restriction and the absolute sufficient constant from §6.2. Cite CB1 with its $V/\bar E_t$ term for real $t\ge4$ using row 1521. The class example proves sharpness of the extensive order on a sequence. Wilson SU(2) still lacks the required logarithmic estimate. Only this check file was written. All arguments and constant comparisons are by hand. No numerical or Lean computation supplies a proof step.
