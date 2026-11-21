## Repo search

**GUIDE.** Check the lead’s search and the target-specific inventory against the cited sources. Then identify the live Wilson estimate, test analytic proof routes, and record the hypotheses and limits of each result here.

**GUIDE.** Row 1177, checkout `d0f24a0d7`. There is no row-specific prior file. The lead’s [8 November search](prior/repo-search-2026-11-08.md) covers thirteen earlier obligations. The [mass-gap supplement](prior/gap-crux-prior-ym.md) locates the nearer results. I fetched the heads and checked PR 10114 (`f76f6c649cff`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, 4–14, 106–117), a one-plaquette witness at finite coupling and a contraction only through bare coupling 1/32. Grok’s PR 10133 (`89faef229ff6`, `APPROACH_REGISTRY.md`, 226–229) explicitly leaves the physical crossover open. The interface I1–I3 on PR 10134 (`1e70c7211a2c`) distinguishes a nonzero excitation from a positive spectral threshold. PR 10141 (`a2f6a430e251`, `fp1.md`, 299–315) estimates a constrained single-scale fluctuation. The additional PR 10149 (`7fc6b1a3e644`, `PROOF_TREE.md`, 47–51) leaves the third transition and the physical gap open. On main `8b11ae2bb9`, Theorem ZD-c supplies the seed equivalence. The local registry gives no competing assignment for the one-cube Wilson estimate. Row 1176 owns the check of row 1175. [Seed theorem](gap-phys-seed.md) · [Domain correction](gap-zd-astra.md) · [Previous construction](gap-solve16-astra62.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, give the gauge-projected transfer trace at outline 2315–2335 and an example of polynomial clustering whose spectral measure reaches zero at 588–599. CA-I 2703–2712 excludes the mass gap from its assertions. Its estimate at 47244–47251 fixes the block size. Tadeusz Bałaban’s renormalization estimates address the ultraviolet part of this route. Sourav Chatterjee’s weak-coupling free-energy comparison enters the earlier lane work. This note is research text and grants no status. The branch criterion is (7), the unconditional tension bound is (26), and (33) treats changes of both normal link fields. [Outline source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [Complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2703-L2712)

**OPEN.** On the assigned trajectory write \(n_j=L/a_j\) at a fixed permitted dyadic physical side and normalize the ordinary positive transfer \(U\) by its vacuum eigenvalue. The target is a strict margin \(\limsup_j(\operatorname{Tr} U^{n_j/2}-1)<1/1650\) at one such side, equivalently the repaired (W) after permitted enlargement. Row 1161 gives two branches if the periodic centre-neutral excited trace \(s_+(\lfloor n_j/512\rfloor;n_j^3)\) is at most \(1/2\) on one fixed physical cube for all sufficiently fine cutoffs. Row 1175 gives, pending its check, a sufficient bound on the cost of an elementary twist on symmetric four-tori. I start by asking what a twist on a rectangular torus can force when only its two normal periods grow. [One-cube alternative and physical grid](gap-solve9-astra62.md)

## Two infinite directions at fixed transverse width

**PROVED.** Fix a bare coupling \(\beta>0\). Give the elementary twist \(12\) normal periods \(a,b\) and give directions 3 and 4 the same period \(w\). All periods are integers at least three. Put
\[
 Z=Z_0,\qquad z=Z_{12}/Z,\qquad Q=(Z-Z_{12})/2,\qquad
 V=2^{-3}\sum_{B\in H^2(\mathbb T^4;\mathbb F_2)} Z_B .
\]
The even/odd centre projection giving \(Q\) is due to ’t Hooft’s electric-flux construction. Both \(Q\) and \(V\) have positive trace representations with \(a\) as time and with \(b\) as time. For \(Q\) the other long direction carries the odd electric character, with the two spectator characters unrestricted. For \(V\) the temporal sum projects each static magnetic sector onto its neutral character. In either time frame the top eigenvalue of \(V\) is the ordinary periodic vacuum eigenvalue. Indeed for every twist \(0<Z_B\le Z\) by removing its temporal unitary in successive frames. Thus \(Z/8\le V\le 8Z\), and taking long-time roots identifies the vacuum norms. The odd sector is nonempty and has positive norm at every \(\beta>0\). The fundamental trace winding around the other active direction is a nonzero odd test. Every electric convolution multiplier is positive, as follows by expanding the Wilson exponential in nonnegative tensor powers of the fundamental character, one of which contains each irreducible representation. The positive, invertible spatial sandwich preserves injectivity on the physical space. [Flux transfer constructions](gap-flux-exercise.md) · [Theorem F](gap-crux-restate.md)

**PROVED.** For \(A=Q,V,Z\) define, with \(w\) fixed,
\[
 e_A(b)=\lim_{a\to\infty}a^{-1}\log A(a,b),\qquad
 f_A(w)=\lim_{\min(a,b)\to\infty}\frac{\log A(a,b)}{ab}.
\]
The second limit is the infimum over the two integer arguments, and \(f_Z=f_V\). In fact the scaled logarithm is separately nonincreasing by monotonicity of the \(\ell^p\) norm of a positive spectrum. The first limit is the log of its top eigenvalue. The sequence \(e_A(b)\) is convex by log-convexity of the trace in the other frame and pointwise passage to the limit. Its first finite difference gives an affine lower bound, so \(f_A=\inf_b e_A(b)/b>-\infty\). This includes \(Q\). The bound \(Z/8\le V\le8Z\) gives the stated pressure equality. In particular the planar electric flux cost per normal plaquette is given by
\[
 \sigma_\beta(w)= -\lim_{\min(a,b)\to\infty}
             \frac{\log[(1-z(a,b;w))/2]}{ab}
            = f_V(w)-f_Q(w).
 \tag{1}
\]
Consequently the crude stack bound of row 1175 already gives the strictly positive lower bound \(\sigma_\beta(w)\ge-\log\tanh(\beta w^2)\). Indeed \((1-z)/2\le(1-z)/(1+z)\le\tanh(\beta w^2)^{ab}\) by summing even and odd translated twist stacks. This bound holds in either branch. The new issue is the \(w\)-dependence of the pressure difference in (1). [Mack–Petkova stack parity and row 1175, (14)](gap-solve16-astra62.md)

**PROVED.** Write \(g_A(a;b)=\log A(a,b)-a e_A(b)\) and \(\kappa_A(b)=e_A(b)-b f_A\). Then \(g_A,\kappa_A\ge0\), and \(\kappa_A\) is nonincreasing. A positive increment of this convex sequence would force a strictly positive asymptotic slope, contrary to \(\kappa_A(b)/b\to0\). Frame exchange therefore gives, for \(3\le t<b\),
\[
 0\le (b-t)\kappa_A(b)
 \le g_A(t;b)-g_A(b;t).                                      \tag{2}
\]
This is row 697’s ground-state deficit argument applied also to the odd partition function with its *own* vacuum and planar pressure. In particular, a common multiplicity in the two \(g_Q\)'s cancels before the bound. [Lemma K](gap-crux-restate.md)

**GUIDE.** I will estimate both terms in (2) on a rectangle with long sides of order \(w^2/n_0\), where \(n_0\) is the seed size in lattice units. A bound on a square with all four periods equal does not by itself control the limit in (1).

## How small the planar electric tension must be in the competing branch

**PROVED (conditional on either seed).** Fix a seed size \(n_0\) divisible by four and a margin \(0<q<1\) such that the selected partition function \(A_0\), either \(Z\) or \(V\), satisfies
\[
 \operatorname{Tr}(T_{A_0}/\lambda)^{n_0/2}-1\le q/5041
 \quad\text{on the cube }n_0^3.
\]
Here \(\lambda\) is the periodic vacuum eigenvalue for this box. Write \(x=w/n_0\). For all sufficiently large \(x\), constants \(c,C>0\) depending only on the margin give
\[
 \begin{array}{ll}
 A_0=Z: & \displaystyle \sigma_\beta(w)\ge
                  {c\over n_0^2\log(2+x)},\\[4pt]
 A_0=V: & \displaystyle \sigma_\beta(w)\le
       {C\over n_0^2 x^4}
       \exp[-c x^2/\log(2+x)] .
 \end{array}                                                     \tag{3}
\]
In the second line both normal lengths in (1) tend to infinity at fixed \(w\). An estimate at a single finite normal length cannot be passed to that limit by continuity.

**PROVED (the tile estimate used below).** For the periodic seed use \(P=Q,\ U=Z\). For the competing seed use \(U=V\) and \(P=2^{-3}\sum_{B:B_{ij}=1}Z_B\). In the latter case regard \(i,j\) as spectators, and in the former take 3 and 4 as spectators. In either active time frame \(P\) is a positive sector sum contained in the excited part of \(U\). If the spectator sides \(d_1,d_2\) both lie in \([h,D]\), take \(h/n_0\) the first dyadic power at least \(K\log(2+D/n_0)\), with \(K\) a sufficiently large constant depending only on \(q\). For large \(D/n_0\), wherever the indicated sides permit this tile,
\[
 {P(r,s;d_1,d_2)\over U(r,s;d_1,d_2)}
       \le \exp[-c\,rs/(h n_0)],\qquad r,s\ge h.                \tag{4}
\]
Indeed Theorem S gives \(S_U(h/2;h^3)\le q^{h/n_0}/5041\), where \(S=e^g-1\). Lemma E′ increases each spectator side from \(h\) at a cost at most \(2D/h\) in \(g\). Thus \(S_U(h/2;h,d_1,d_2)\le e^{-c h/n_0}\) after increasing \(K\). In the active plane use its own bulk \(f_U\), with these spectators fixed. By (2) the vacuum correction \(h\kappa_U(h)\) is at most \(2g_U(h/2;h)\). At \(h,h\), \(P\) divided by the vacuum to power \(h\) is at most \(S_U(h/2;h)^2\) by positivity and the sector inclusion. The two active trace powers imply \(P(r,s)\le P(h,h)^{rs/h^2}\). The lower bound \(U(r,s)\ge e^{rs f_U}\) proves (4). In the magnetic case \(Z_B/Z\le64P/U\) whenever \(B_{ij}=1\), by positivity and \(V\le8Z\). This recovers the finite rectangle input of row 1175 without using its conclusion as a checked premise. In the periodic case take spectators \(w,w\) and pass to (1) to get the first line of (3). [Seed and enlargement](gap-crux-restate.md) · [Magnetic sector inclusion, C5–C6](gap-flux-exercise.md)

**PROVED (calibration in the other frame).** In the competing branch put \(b=2\lceil n_0 x^2/2\rceil\), \(t=b/2\). For \(s\in\{t,b\}\) and \(r\in\{t,b,2b\}\) consider the actual rectangle \((r,s,w,w)\). Every nonzero \(B\) has a nonzero entry. For that entry as spectators, all four sides are at least \(w\) and at most \(2b\), once \(x\) is large. Formula (4) with \(D=2b\) gives, simultaneously,
\[
 Z_B/Z\le C e^{-c x^2/\log(2+x)}=:\eta .                         \tag{5}
\]
The notation on the right allows increasing \(C\) or decreasing \(c\) in what follows. Hence \(Q/V=4(1+O(\eta))\), with factor four equal to \((1/2)/(1/8)\), since the periodic integral is the only one contributing to first order in both sums.

**PROVED.** In the same rectangles \(g_V(r;s)\le C e^{-c r/n_0}\). Choose a dyadic seed side \(d=2^k n_0\in(w/2,w]\). Apply the propagated seed at time \(d/2\), then Lemma E′ in the three spatial directions to \(s,w,w\). Its total factor on \(g\) is at most \(8s w^2/d^3=O(x)\). Thus \(S_V(d/2;s,w,w)\le e^{-c d/n_0}\) for large \(x\). Taking higher powers of its positive excited spectrum gives \(S_V(r;s,w,w)\le e^{-c' r/n_0}\) for \(r\ge d/2\), as asserted. In particular on each calibration rectangle,
\[
  \log Q(r,s)=r e_V(s)+\log4+O(\eta).                              \tag{6}
\]

**PROVED.** For \((r,s)=(t,b),(b,t)\), positivity bounds \(Q(2r,s)/Q(r,s)\le e^{r e_Q(s)}\), and \(e_Q(s)\le e_V(s)\) since \(Q\le Z\). Subtract (6) at the two times to obtain
\[
 0\le r(e_V(s)-e_Q(s))\le C\eta,\qquad
 |g_Q(r;s)-\log4|\le C\eta .
\]
Using both orientations in (2) now gives \(\kappa_Q(b)\le C\eta/b\). Finally
\[
 f_V-f_Q
 = b^{-1}\{e_V(b)-e_Q(b)+\kappa_Q(b)-\kappa_V(b)\}
 \le C\eta/b^2.
\]
This proves the second line of (3). Bounding either \(g_Q\) in isolation by a constant would give just \(O(b^{-2})\) at this step.

**PROVED (branch test).** With the physical one-cube neutral bound of row 1161, (W) is equivalent to the following statement at each sufficiently fine fixed cutoff. There are unbounded integer widths \(w\) along which
\[
 \frac{\log(2+w)}{w^2}\,[-\log \sigma_{\beta_j}(w)]_+
 \longrightarrow 0 .                                                 \tag{7}
\]
The ordinary branch gives (7) by the first line of (3). At each fixed cutoff \(n_0\) is a fixed number, so the second line excludes (7) in the competing branch. Row 1161’s explicit alternative supplies the uniform ordinary seed if the competing branch is excluded for each sufficiently fine cutoff. Conversely (W) supplies the ordinary seed after enlargement. All infinite-plane limits in (7) are taken **before** increasing \(w\) and at fixed \(\beta_j\). The universal lower bound following (1) is too small to verify (7).

## The elementary twist through the crossover on a finite rectangle

**PROVED (conditional on the competing seed).** There are \(c,C,X>0\), depending only on \(q\), such that if \(w/n_0\ge X,\ b\ge4w,\ b/2\le a\le2b\), then
\[
 \left|\frac{1-z(a,b;w)}{1+z(a,b;w)}
                   -e^{-\sigma_\beta(w)\,ab}\right|
 \le C e^{-c b/n_0}.                                                 \tag{8}
\]
Equivalently \(z=\tanh(\sigma_\beta(w)ab/2)+O(e^{-c b/n_0})\). This estimates the full change from a small twist ratio to a ratio near one. No monotonicity of the twist in a side length is assumed.

**PROVED (cooling on arbitrarily elongated sections).** In the \(V\) transfer with spatial sides \((s,w,w)\), for \(s\ge w/2\) and integer \(r\ge s/16\),
\[
 S_V(r;s,w,w)\le C e^{-c r/n_0}.                                    \tag{9}
\]
Choose the largest dyadic \(d=2^k n_0\le w/32\), so \(32\le w/d<64\). At time \(d/2\) the propagated seed at \(d^3\) is at most \(q^{d/n_0}/5041\). Enlarge the three sides to \(s_0=16d,w,w\) by E′. All three costs on \(g\) are bounded by absolute constants. Set \(u_0=d/2\). At each subsequent doubling \((s_i,u_i)=(2^is_0,2^iu_0)\), enlarging \(s_i\) to \(2s_i\) costs at most four on \(g\) since \(u_i=s_i/32\). Squaring in time gives \(S_{i+1}\le[(1+S_i)^4-1]^2\le225S_i^2\) for \(S_i\le1\). For \(w/n_0\) sufficiently large the first bound gives \(225S_0\le e^{-c d/n_0}\). Induction gives the corresponding bound raised to \(2^i\). Take \(s_i\le s<2s_i\) and use E′ once more at time \(u_i\). The positive excited spectrum at that time has sum at most \(e^{-c' u_i/n_0}\). Raising its powers to \(r/u_i\ge1\) proves (9), including the case \(s=s_0\). This avoids paying a factor proportional to an arbitrarily large \(s/w\) at a fixed initial time.

**PROVED.** For \(b\ge w,\ a/b\in[1/2,2]\), (2) for \(V\) and (9) give
\[
 0\le\log V(a,b)-ab f_V
      =g_V(a;b)+a\kappa_V(b)\le C e^{-c b/n_0}.                       \tag{10}
\]
Indeed one may drop \(g_V(\lfloor b/2\rfloor;b)\)'s crossed counterpart in (2). An arbitrary \(B\) with an entry other than \(12\) has a nonzero static entry in at least one of the two long time frames. In that frame positivity of the twist integrals gives \(\operatorname{Tr}_h F_m^\ell\le\operatorname{Tr}_0 F_m^\ell\) by Fourier inversion for each electric character \(h\). Deleting the temporal unitary therefore bounds \(Z_B\) by eight times the static neutral trace at that nonzero \(m\). It is part of \(V\)'s excited trace. From (9), \(Z_B/V\le C e^{-cb/n_0}\). In particular, for \(H=(Z+Z_{12})/2\),
\[
                  H=4V\{1+O(e^{-cb/n_0})\}.                           \tag{11}
\]
The exceptional twist \(12\) is temporal in both long frames.

**PROVED (four electric characters).** In the \(a\)-time frame let \(Q_h\) be the periodic trace odd on direction 2 and with prescribed character \(h\in\mathbb F_2^2\) on directions 3,4. Then
\[
  \left|Q_h-Q/4\right|\le C e^{-cb/n_0}V,\qquad
  \left|\frac{Q(a,b)}{e^{a e_V(b)}}-4 e^{-a E_b}\right|
                         \le C e^{-c b/n_0},\qquad E_b=e_V(b)-e_Q(b).
 \tag{12}
\]
For the first inequality expand the three commuting projections in temporal seams. The two terms with no seam in directions 3,4 sum to \(Q/4\). Each of the other six has a static entry in the \(b\)-time frame and satisfies the estimate before (11). For the second choose \(h\) containing a top eigenvalue of \(Q\). The periodic neutral excitation ratio \(\rho\) in the spatial box \((b,w,w)\) obeys \(\rho\le e^{-c/n_0}\) by (9) and long-time roots. Row 1157’s two-real-eigenfunction inequality gives \(1-\lambda_{h,2}/\lambda\ge(1-\rho)/4\), where \(\lambda=e^{e_V(b)}\), and \(\lambda_{h,2}\) counts the second level in this full electric character including multiplicity. Thus \(\lambda_{h,2}/\lambda\le e^{-c'/n_0}\) after reducing \(c'\), uniformly for \(n_0\ge6\). At time \(\lfloor a/2\rfloor\) the entire character trace in vacuum units is bounded by the periodic neutral trace by Fourier positivity, hence by \(1+S_V\le2\). Spending the remaining time on its second eigenvalue makes the tail in \(Q_h/\lambda^a\) at most \(C e^{-c b/n_0}\). The top contributes \(e^{-aE_b}\). Combine this with (9) and the first inequality to obtain (12). [Two-eigenfunction comparison, (1)](gap-solve8-astra62.md)

**PROVED (recovering the pressure with an error uniform in area).** Use (12) for the two ordered pairs \((r,s)=(\lfloor b/2\rfloor,b),(b,\lfloor b/2\rfloor)\). For odd \(b\) the ratio in the second pair exceeds 2 by \(O(1/b)\). All estimates (9)–(12) used here hold on the slightly larger ratio interval \([1/3,3]\) by the same bounds, since the half times and crossed periods are still at least one sixteenth of the relevant spatial side for large \(w\). The lower pressure bound \(Q(r,s)\ge e^{rs f_Q}\) and (10) imply
\[
 Q(r,s)e^{-r e_V(s)}
    \ge \exp[-rs\,\sigma_\beta(w)-C e^{-c b/n_0}].
\]
Choose an absolute fraction \(\epsilon>0\) of the decay constant in (12), small enough that the additive error in (12) divided by this lower bound is at most \(C e^{-c' b/n_0}\) whenever \(b\sigma_\beta(w)\le\epsilon/n_0\). In that range (12) gives \(g_Q(r;s)=\log4+O(e^{-c' b/n_0})\) in both frames. By (2), \(0\le\kappa_Q(b)\le C e^{-c' b/n_0}/b\). Together with (10) this gives
\[
 |E_b-b\sigma_\beta(w)|\le C b^{-1}e^{-c' b/n_0}.
\]
Equations (9), (11) and (12) now give (8) because \(Q/H=(1-z)/(1+z)\).

**PROVED.** In the remaining range put \(b_*=\lfloor\epsilon/(2n_0\sigma_\beta(w))\rfloor\). Positivity in (1) makes it finite, and (3) gives \(b_*\ge4w\) as soon as \(w/n_0\) is sufficiently large uniformly in \(n_0\). At this earlier side the last bound on \(\kappa_Q\) gives \(\kappa_Q(b_*)\le b_*\sigma_\beta(w)/2\), since \(b_*\sigma_\beta(w)\ge\epsilon/(4n_0)\) and \(b_*/n_0\) grows. Monotonicity of \(\kappa_Q\) then gives \(E_b=b\sigma_\beta(w)+\kappa_V(b)-\kappa_Q(b)\ge b\sigma_\beta(w)/2\) when \(b\sigma_\beta(w)>\epsilon/n_0\). Both \(e^{-aE_b}\) and \(e^{-ab\sigma_\beta(w)}\) are bounded by \(e^{-c b/n_0}\) here. Equations (11)–(12) finish (8). Finally \(u\mapsto(1-u)/(1+u)\) is 2-Lipschitz on \([0,1]\), giving the stated formula for \(z\).

## A thinner finite Wilson test

**PROVED.** At each fixed cutoff in the competing branch, let \(N\) be the common normal period and let \(w_*(N)\) be the first transverse width \(w\in[3,N]\) with \(z(N,N;w)\le1/2\). For large \(N\) it exists and
\[
 c_\beta \sqrt{\log N}\ \le w_*(N)\le
         C_j\sqrt{\log N\,\log\log N}.                                \tag{13}
\]
The lower bound is the earlier stack inequality. In fact if \(\beta w^2\le(1-\epsilon)\log N\), it gives \(1-z\le2\exp(-N^{2\epsilon})\). For the upper bound choose \(w=\lceil A_j\sqrt{\log N\log\log N}\rceil\). At fixed cutoff \(n_0\) is constant. By taking \(A_j\) large enough in (3), one gets \(N^2\sigma_\beta(w)\le N^{-D}\) for any *prescribed* \(D>0\) and all sufficiently large \(N\). For example \(\log(2+w/n_0)\le\log\log N\) eventually, so \(cA_j^2/n_0^2>D+3\) suffices after increasing the floor in \(N\). Equation (8) gives \(z\le C N^{-D}\) at that width. This proves (13) without any ordering in \(w\). The earlier upper bound on the first width was \(C_j\log N\). [Row 1175, (14)–(16)](gap-solve16-astra62.md)

**PROVED.** The width can also be prescribed without knowing a seed constant. Take, for example, \(w_N=\lceil\sqrt{\log N}\,\log\log N\rceil\). In the competing branch \(z(N,N;w_N)\) is smaller than any inverse power of \(N\), by the same argument, while in the ordinary branch it tends to one by (4). Thus with row 1161's physical neutral premise, an inverse-polynomial lower bound for the actual elementary twist along arbitrarily large \(N\) at this prescribed width, with the exponent allowed to depend on the fixed cutoff, is equivalent to (W). The width is \(o(\log N)\).

**PROVED.** At fixed transverse \(w\) the crossover location can instead be read in the normal period. For \(u>0\), take \(N(w)\) nearest to \(\sqrt{u/\sigma_\beta(w)}\). In the competing branch (3) ensures \(N(w)/w\to\infty\), and (8) gives \(z(N(w),N(w);w)\to\tanh(u/2)\). Conversely any normal periods at least \(4w\) with a limiting twist \(z_*\in(0,1)\) obey \(\sigma_\beta(w)N(w)^2\to\log[(1+z_*)/(1-z_*)]\). These limits are at a single bare coupling. They give neither the value of the tension of the Wilson measure nor the physical neutral input.

## A lower bound from separate Wilson vortex insertions

**PROVED (no seed assumption).** There are absolute \(C,c>0\) such that for all sufficiently large \(\beta\) and integers \(w\ge C\beta^{1/3}\),
\[
     \sigma_\beta(w)\ \ge\
      c\,\beta^{-1/6}\exp[-C\beta^{5/6}w^2].                          \tag{14}
\]
This improves the coefficient of \(w^2\) in the elementary thin-section lower bound as \(\beta\to\infty\). It is an estimate on the infinite-plane tension of the original Wilson model. Row 1169 inserts one spread twist in a finite partition function. Here disjoint insertions must control an exponential *rate* in the number of normal plaquettes. The parity decomposition is Mack and Petkova’s. The use of axes transported by tangential links follows row 1169. [Single insertion](gap-solve13-astra62.md) · [Container parity](gap-cr-tomboulis-max.md)

**PROVED (local change and its cost).** Fix integers \(2\le R\le l,\ w\ge4l\). At a given first-coordinate cut and second-coordinate row \(q\), give a stack of \(12\)-faces a label \(\tau=\pm1\) multiplying their plaquette traces. Toggle this label. On forward 1-links at the cut and at successive rows \(q+i\), left-multiply by \(\exp(\tau\alpha_i v_x)\). Here \(\alpha_i=\pi(1-(i-1)/R)\) for \(1\le i\le R+1\), and zero elsewhere. The \(v_x\) are unit imaginary quaternions depending only on unchanged tangential links. The jump from zero to \(\pi\) cancels the toggled stack exactly in either direction. All other angular differences have magnitude at most \(\pi/R\). The inverse map at the new label undoes the left multiplications and preserves product Haar.

**PROVED.** Partition the transverse torus into rectangles with side lengths in \([l,2l]\) and use their products with the interval of rows of the ramp as boxes. In each box choose a root and transport a fixed unit axis by coordinate-ordered tree paths from it. Choices below use only faces in directions \(2,3,4\), whose weights have no sign. There is a choice for which the total squared tangential mismatch on the internal edges satisfies
\[
 \sum_{\mathrm{internal}\ e=xy}|v_x-\operatorname{Ad}_{U_e}v_y|^2
 \le C l^2 \sum_{p\ \mathrm{tangential\ in\ boxes}}(1-w_p),
 \qquad w_p=\operatorname{tr}(U_p)/2.                                \tag{15}
\]
To verify it, average the root uniformly in each box. For adjacent endpoints differing in coordinate \(i\), move their extra unit \(i\)-edge through the ordered path. Each later coordinate \(j\) contributes one width-one strip of length at most \(2l+2\). Telescope the face holonomies along these strips and apply Cauchy–Schwarz. The squared mismatch costs at most \(Cl\) times their total plaquette deficit, since \(\|\operatorname{Ad}_g-I\|\le 2|1-g|\) in quaternion chord. For a fixed \(ij\)-face, its \(i\)-coordinate fixes the endpoint's \(i\)-coordinate up to orientation. There are at most \(2l+2\) endpoint \(j\)-coordinates. For each other coordinate either the endpoint is prescribed by the face, or the root is prescribed there and the sum over the free endpoint cancels that root probability. Thus after summing edges the mean incidence of the face is at most \(Cl\). This proves (15) in mean over roots, hence for a minimizing root, with deterministic tie breaking. Changing the normal links leaves these choices fixed. Boxes crossing the periodic seam use their interval coordinates. On edges between transverse rectangles the squared mismatch is at most four and the number of such edges is at most \(CRw^2/l\).

**PROVED.** Let \(D_i\) consist of the tangential plaquettes just used and all normal plaquettes touched by insertion \(i\), with at most \(C Rw^2\) faces. For signed deficits \(s_p=1-\tau_p w_p\) of the **original** labelled path (\(\tau_p=1\) off the labelled stacks), the absolute difference of its log weight and the toggled weight is bounded by
\[
 L_i\le C\beta w^2(R^{-1}+R/l)
          + C\beta(1+l^2)\sum_{D_i}s_p .                              \tag{16}
\]
Indeed for a \(1k\)-face the trace after rotation is the scalar part of \(B(\tau_p U_p)\), by cyclically moving the two rotation factors together. The chord of \(B\) from one is at most the angular difference, corrected by the central jump, plus the mismatch of the two axes across the unchanged \(k\)-edge. The squared angular differences sum to \(Cw^2/R\). At the central jump the two rotations are central and produce zero residual regardless of axes. For unit quaternions \(P,B\),
\(\left|\operatorname{Re}(BP)-\operatorname{Re}P\right|\le C(|1-B|^2+1-\operatorname{Re}P)\) by \(|\operatorname{Im}P|^2\le2(1-\operatorname{Re}P)\). Sum this estimate, (15) and the interbox count. It holds for either starting label, without assuming a flat exterior.

**PROVED (exponential control over many insertions).** Place \(m\ge c ab/R\) such stacks, for all sufficiently large \(a,b\) at fixed \(R\), by spacing cuts by at least three first-coordinate steps and rows by \(R+4\) or more. For example take every third cut and every \((R+4)\)-th row within the torus minus one such interval at each seam. The read and changed sets of different insertions are disjoint, including the faces incident to a changed link. Give the \(m\) labels counting measure normalized to one and use the signed Wilson weight jointly with Haar on the links. Its total mass is \((Z+Z_{12})/2\) by the cohomology of the stacks. Under the normalized joint law, for every deterministic set \(D\) of distinct plaquettes,
\[
        \mathbb E\exp\!\left[c_0\beta\sum_{p\in D}s_p\right]
                         \le 2C_0^{|D|}.                              \tag{17}
\]
For a common direction of the marks, make it time and halve the marked electric couplings. Move each fixed sign assignment to a standard twist by central link changes, which also move the signs on the marked terms correctly. In each time layer the normalized halved one-link convolution is below the full one in positive-operator order. The ratio of scalar normalizers \(z_{\beta/2}/z_\beta\) is bounded absolutely as in row 1155, (9). Gauge projection and the spatial magnetic sandwich preserve this order, also with fixed static twist. Schatten Hölder bounds the trace of the product, with its possible temporal unitary, by the product of the layer Schatten norms at the full period. By eigenvalue monotonicity each norm is bounded by the homogeneous static norm times the scalar cost of its marks. The homogeneous static trace is at most \(Z\). Thus the *unnormalized* tilted integral at each label is at most \(C_0^{|D|}Z\). Divide the label average by its mass at least \(Z/2\). Classify general marks by one of their directions and use Hölder under the joint probability with exponent four, taking \(c_0=1/8\). This argument needs no lower bound on any twisted partition function. [Marked-face multiplier bound](gap-solve7-astra62.md) · [Original multiplier comparison](gap-solve4-astra62.md)

**PROVED.** Call an insertion usable on its orbit if its absolute log weight difference is at most
\[
                  K=Cw^2\{\beta/R+\beta R/l+R l^2\}.
\]
For an individual path, (16) implies usability whenever \(\beta\sum_{D_i}s_p\le A Rw^2\), for a fixed large \(A\) and corresponding absolute \(C\) in \(K\). For any \(k\) prescribed unusable insertions, apply (17) to the disjoint union of their \(D_i\)'s. Their probability is at most \(2\exp[-(c_0 A-C')k Rw^2]\). A union bound over subsets of size \(\lceil m/2\rceil\) shows that having fewer than \(m/2\) usable insertions has probability at most \(2e^{-c m Rw^2}\), after choosing \(A\). Usability is constant on each orbit because toggling that label negates the log weight difference, while the other insertions affect none of its read or changed faces.

**PROVED.** On an orbit of the commuting involutions, the two choices for each label are independent with odds given by its own weight ratio. Indeed the reference measure is invariant under all toggles and each affected action term belongs to just one toggle. Equivalently one may average the integrand over the \(2^m\) transforms before integrating. The expectation of total label parity is \((Z-Z_{12})/(Z+Z_{12})\). Its absolute value on an orbit after averaging is the product of \(\tanh(L_i/2)\), where \(L_i\) here denotes the actual absolute log difference. Thus
\[
 0\le (1-z)/(1+z)
    \le \exp[-m e^{-K}/2]+2e^{-c m Rw^2},                             \tag{18}
\]
using \(\tanh(K/2)\le1-e^{-K}\). Passing to (1) gives \(\sigma_\beta(w)\ge(c/R)e^{-K}\), since \(Q/Z\le(1-z)/(1+z)\). Take \(R=\lfloor\beta^{1/6}\rfloor,\ l=\lfloor\beta^{1/3}\rfloor\) with an absolute increase in the lower bound on \(\beta,w\). All three terms in \(K/w^2\) are then \(O(\beta^{5/6})\), proving (14).

**PROVED (where this absolute estimate stops).** At fixed bare coupling the two-plaquette result of row 1141, (4), (6)–(7), in the transverse \(34\)-plane implies that except on a set of probability \(e^{-c w^2}\),
\[
 \sum_{xy\ \mathrm{transverse}}
       |v_x-\operatorname{Ad}_{U_{xy}}v_y|^2
             \ge c w^2/(1+6\beta)
\]
for *every* unit-axis assignment on that sheet, chosen after seeing all links. Its proof uses disjoint \(3\times3\) cells and the one-link bound conditional on their exterior. It applies also at a prescribed label since signs only change the six staple vectors without increasing their lengths. At a noncentral ramp row of fixed angle \(\alpha\), the sum of squared chords of the inserted factors on the mixed faces is exactly \(\sin^2\alpha\) times this mismatch because the two quaternion multipliers have equal scalar part. For \(R\ge2\) a ramp row has \(\sin^2\alpha\ge1/2\). Therefore the nonnegative squared-displacement estimate used in (16), even optimized over all the axes, pays order \(w^2\) at fixed coupling on a typical sheet. The bound (14) cannot meet (7) by optimizing these ramp parameters. This lower bound concerns the displacement proxy. The true signed action change also pairs an imaginary part with the original plaquette, a term lost in taking absolute bounds. [Typical-field bound, row 1141](gap-crux2-astra62.md)

## What the ordinary partition function and the neutral trace see

**PROVED (ordinary free energy at fixed transverse width).** Write \(f_\beta(w)=f_Z(w)\) and \(F=\log Z\). For comparable \(a,b\ge4w\) in the range of (8),
\[
 F(a,b,w,w)-ab f_\beta(w)=
 \begin{cases}
 O(e^{-cb/n_0}), &\text{ordinary seed},\\
 \log4+\log(1+e^{-\sigma_\beta(w)ab})+O(e^{-cb/n_0}),
                                      &\text{competing seed}.
 \end{cases}                                                         \tag{19}
\]
The ordinary case follows by applying the proof of (9)–(10) directly to \(Z\). In the competing case insert (8), (10) and (11) into \(Z=H+Q\). Thus on sending \(N\to\infty\) first at any sufficiently large **fixed** \(w\), the unmodified square-plane difference \(4F(N,N,w,w)-F(2N,2N,w,w)\) tends to zero or \(3\log4\), respectively. Positivity of \(\sigma_\beta(w)\) is essential to this order of limits. In the competing branch the excess in (19) is instead close to \(\log8\) below the crossover. Row 1163 obtained the \(\log8\) excess on large four-dimensional cubes. Equation (19) resolves its change when only two directions keep growing. [Previous ordinary excess](gap-solve10-astra62.md)

**PROVED (a neutral test with the ordinary planar bulk).** Let
\[
 Z_+(a;b,w,w)=\tfrac18\sum_e Z_{m=0,e}(a,b,w,w)
\]
denote the temporal-seam average in the \(a\)-frame, where the summands here are *twisted integrals*, not the electric character traces. Define
\[
 H_+(a;b,w)=\log Z_+(a;b,w,w)-ab f_\beta(w).
\]
With \(g_+=\log\{\operatorname{Tr}_+(F_{\rm tr}/\lambda)^a\}\) for the ordinary Wilson transfer \(F_{\rm tr}\), one has at **every** cutoff
\[
 g_+\le H_+=g_++a\kappa_Z(b)
 \le {b\over b-a}g_+ + {a\over b-a}\log 8,\qquad 3\le a<b.          \tag{20}
\]
All vacuum eigenvalues in (20) refer to the same spatial box \((b,w,w)\). The identity is the definition of \(\kappa_Z\). For the upper bound apply (2) to \(Z\), drop the nonnegative crossed thermal sum and use \(Z\le8 Z_+\), since every temporal twist integral is positive. In either seed, the stronger estimate \(0\le H_+\le C e^{-c b/n_0}\) holds for \(w/n_0\) large, \(b\ge w\) and \(a/b\) in a fixed compact subinterval of \((0,\infty)\). The upper bound follows from \(Z_+\le A_0\), the common planar pressure and (9)–(10) for the seed \(A_0\). For a smaller fixed lower endpoint of the aspect interval, start the proof of (9) with \(d\) a correspondingly smaller fixed fraction of \(w\) and keep \(u_0/s_0\) below that endpoint. The constants may depend on the interval. The lower bound is the identity in (20).

**PROVED.** The physical neutral premise, allowing dyadic enlargement, is equivalent to making \(H_+(\lfloor n/512\rfloor;n,n)\) arbitrarily small in cutoff limsup at a sufficiently large *fixed physical* side. Small \(H_+\) implies the required upper bound on \(s_+=e^{g_+}-1\) by (20). In the other direction row 1161 gives a seed in \(Z\) or \(V\) at each fine cutoff, with the same physical seed size and the same margin. The preceding exponential upper bound then applies at a common enlarged physical side even if the branches alternate with cutoff. This form compares a finite neutral integral to the planar pressure of the ordinary Wilson measure. It still requires an order-one finite-size estimate.

**PROVED (replicating the compact period).** For unequal transverse sides write \(f_\beta(c,d)=\lim_{\min(a,b)\to\infty} F(a,b,c,d)/(ab)\) as in (1). The quantity
\[
   \tau_\beta(w)=2 f_\beta(w,w)-f_\beta(2w,w)
\]
measures a contribution from the whole Wilson spectrum. At all \(\beta\ge1,\ w\) sufficiently large, absolute constants give the following lower bound. The upper bound holds under either seed for \(w/n_0\) sufficiently large.
\[
       c w e^{-Cw}\ \le\ \tau_\beta(w)\
                \le\ C_q w^{-2}e^{-c_q w/n_0}.                         \tag{21}
\]
For fixed \(w\) take the other spatial sides \(N,N\) and time \(w\), writing \(g_Z(t)\) for the full thermal logarithm in that box. The undivided doubling difference equals \(2g_Z(w)-g_Z(2w)\) and lies between \(g_Z(w)\) and \(2g_Z(w)\). For the lower bound, row 1161 (19) places at least \(\tfrac12\binom Mk\) excited neutral levels below lattice energy \(Ck\) for \(1\le k\le M\). Its proof uses separated spatial plaquettes with disjoint selected links, giving \(M\ge c N^2 w\) on the rectangle \((N,N,w)\) by the same stride-four construction. The conditional Gram lower bound and local inverse-convolution estimate involve only the links of the multiplied plaquettes and do not change on this rectangle. Choose \(k=\lfloor M e^{-Cw}/2\rfloor\). Since \(\binom Mk\ge(M/k)^k\), the neutral trace is at least \(2^{k-1}\) when \(N\) is large. Dividing its logarithm by \(N^2\) and then taking \(N\to\infty\) gives the first inequality. For the upper bound, take a dyadic seed side \(d\in(w/2,w]\), time \(d/2\), and enlarge the spatial sides to \(N,N,w\). Lemma E′ gives \(g_{A_0}(w)\le C(N/w)^2 e^{-c w/n_0}\) by time monotonicity. Also \(g_Z(w)\le g_{A_0}(w)+\log8\). Divide by \(N^2\) and pass to the same limit. [Neutral product trial states and their inverse forms](gap-solve9-astra62.md)

**PROVED (obstruction to extracting the neutral margin from planar thermodynamics).** The pressures in (1) and (21), their differences at *all* finite transverse sizes, and even the limiting order-one terms of (19) at each fixed cutoff cannot by themselves prove the estimate in (20). Use the local three-cell sign factor of row 1175 with \(\rho_j=e^{-a_j^5}\). Its multiplicative partition correction on every torus is \(1+\rho_j^{ab c d}\), including each twist and its positive temporal average. Expanding its local four-cell factors leaves only the empty and full four-chain, since neighboring occupancies must agree across every face. Its two nonzero transfer eigenvalues in a spatial box of volume \(v\) are \(1,\rho_j^v\), both neutral. At fixed \(j,c,d\) its whole logarithmic correction tends to zero exponentially in \(ab\). Thus it preserves the planar pressures, the coefficient \(\sigma_\beta\), every normalized twist curve including (8), the fixed-cutoff limiting excess, and the exact value of \(\tau_\beta\), even when the latter includes the strictly positive Wilson contribution in (21). But at \(a=\lfloor n_j/512\rfloor,\ b=c=d=n_j=L/a_j\), its addition to \(H_+\) tends to \(\log2\). The product's excited neutral trace has liminf at least one. This is a counterexample to the inference from those data on local reflection-positive extensions. The pure Wilson estimate (20) remains open. It pinpoints the missing information at finite normal area and in the order of the cutoff limit. [Local factor and its transfer kernel, row 1175 (29)](gap-solve16-astra62.md)

## Trying to use a signed bound uniform in the fields outside one sheet

**PROVED (a Wilson conditional counterexample).** Fix all links tangent to a pair of adjacent first-coordinate slices. The 1-links between them are spins \(p_x\in SU(2)\) on the three-dimensional sheet with directions \(2,3,4\). With equal tangential fields \(A\) on both sides their interaction on \(xy\) is \(\beta\,\operatorname{Re}(\bar p_x A_{xy}p_y A_{xy}^{-1})\). An elementary \(12\)-twist on this cut is an antiperiodic spin boundary in direction 2. There are explicit such tangential fields, an absolute \(\beta_*\), and \(c,C>0\) for which
\[
 {Z^{\mathrm{anti}}_{\mathrm{sheet}}(b,w,w)\over
   Z^{\mathrm{per}}_{\mathrm{sheet}}(b,w,w)}
      \le C b w^2e^{-c\beta w^2},                                    \tag{22}
\]
for \(\beta\ge\beta_*\), dyadic integers \(b,w\) with \(b\ge w\ge8\), whenever \(C b w^2e^{-c\beta w^2}\le1\) (the proof uses half this upper bound for the probability of the nonzero classes). In particular, increasing the ramp depth polynomially in \(w\) does not secure a subarea signed insertion cost uniformly in these pins. This is a statement about an integrated conditional Wilson partition function, including the spin entropy. The equal curved background and its two-dimensional order proof are due to row 1139, building on row 876's pinning proposal and the Durhuus–Fröhlich conditional slab. The use here is a bound on the probability of a surface winding in a three-dimensional sheet. [Curved pin and reflection proof](gap-frameless-2d-astra.md) · [Check of that proof](gap-frameless-2d-check-opus.md)

**PROVED.** In directions 3 and 4 take row 1139's reflected tile \(\{0,1,2\}^2\), with the two consecutive top horizontal bonds carrying conjugation by \((1+i)/\sqrt2\) and \((1+j)/\sqrt2\), all other bonds the identity. Repeat in direction 2 with identity bonds in that direction. Within one tile, vanishing bond deficits require the spins on its connected identity edges to be one common quaternion. The two upper bond conditions make it commute with both \(i\) and \(j\), hence equal \(+1\) or \(-1\). The same conclusion holds on a cube of side two by joining the three transverse tiles by the identity 2-bonds.

**PROVED (reflection estimate with twisted sectors included).** Put uniform counting measure on all flat link signs \(\xi\) on the three-torus, and multiply the spin trace on each bond by \(\xi_{xy}\). Each of the eight cohomology classes has the same reference mass. Vertex sign changes of spins remove every exact sign field, also locally on each coarse cube. Call a cube good if, after such local trivialization, its spins all belong to a single chord cap of radius \(1/4\) about \(+1\) or \(-1\). This condition is independent of the remaining common sign. Share each bond deficit between its incident coarse cubes, assigning it positive weight in each. By compactness and the zero-energy calculation, a bad cube costs at least a fixed \(\delta>0\) of this assigned energy. Write \(m=(b/2)(w/2)^2\) for the cube count. The event that every cube is bad has probability at most \(e^{-\kappa\beta m}\) for \(\beta\ge\beta_*\). In the zero class, of reference mass \(1/8\), restrict all gauge-transformed spins to a smaller cap about \(+1\). Since every conjugation fixes \(+1\), a fixed cap radius can be chosen so the total action without \(\beta\) is at most \(\delta m/2\). Its Haar cost is \(c_*^{8m}\) for fixed \(c_*>0\). Compare this contribution to the all-bad upper weight \(e^{-\beta\delta m}\) and increase \(\beta_*\).

**PROVED.** Under this joint law any specified set \(S\) of bad tiles has probability at most \(e^{-\kappa\beta |S|}\). For clarity, at two opposite coarse site planes condition on their spins and their in-plane sign bonds. Every plaquette flatness constraint belongs to a half or to the boundary. All flat classes are included, so the two reflected interiors factor with identical weights. This gives \(P(S)^2\le P(S_1)P(S_2)\) by Cauchy–Schwarz, where \(S_i\) mirrors one half into the other. Site reflection of the periodic background was built into the tile. The two new sizes sum to \(2|S|\). Putting all spins in a small cap about the same purely imaginary quaternion makes every cube bad with positive probability. Maximize \(\log P(S)-(|S|/m)\log P(\text{all})\) over positive-probability events. A positive maximizer contains a tile and can be replaced by either mirrored copy at the same maximum. Choose the end of a marked run as reflection plane, keeping the half with the run. Repeated doubling first fills a line, then a sheet of such lines and then all tiles, since each side in coarse units is dyadic. This contradicts the positive maximum. This is the chessboard argument of row 1139 with the flat-sign constraints retained.

**PROVED (area of the required defect).** At coarse vertices write \(s_x=\operatorname{sgn}\operatorname{Re}p_x\), ignoring Haar-null ties. On a coarse edge \(xy\) take \(s_x\xi_{xy}^{(2)}s_y\), where the middle factor is the product on its two fine bonds. These signs form a closed cochain in the class of \(\xi\). The dual faces of its negative edges form a closed mod-two surface. Each component connected by shared edges is closed, since all faces at any one edge lie in the same component whenever they occur. A nonzero class requires a component with odd intersection with a coordinate winding. Its intersection parity is the same for every parallel translate of that winding, since the difference bounds a strip and the component is closed. These disjoint windings require at least \((w/2)^2\) distinct dual faces. Every negative coarse edge is incident only to bad cubes, because its two endpoints cannot be in the same locally trivialized cap. For any specified \(k\) faces choose one incident bad cube for each primal edge by a fixed rule. This gives at least \(k/12\) distinct cubes. The number of connected sets of \(k\) dual faces is at most \(3m\,12^{2k}\), by a traversal of a spanning tree from a chosen starting face in the adjacency graph of degree at most twelve. Sum \(3m\,12^{2k}e^{-\kappa\beta k/12}\) for \(k\ge(w/2)^2\), increasing \(\beta_*\) once. This bounds the probability of all nonzero sign classes by \(C b w^2 e^{-c\beta w^2}\). Comparing the desired class to the trivial class now proves (22).

**PROVED (odd sheet energy).** For these pins let \(K\) be the sheet transfer in direction 2, \(\lambda=\|K\|\), and \(\lambda_o\) its largest eigenvalue odd under simultaneous spin negation. At each sufficiently large fixed \(\beta\), along these widths,
\[
         -\log(\lambda_o/\lambda)\le C_\beta w^2 e^{-c\beta w^2}.       \tag{23}
\]
Choose a dyadic \(b\) within a factor two of \(e^{c_1\beta w^2}\), with \(c_1\) small in (22). Positivity of the periodic transfer, its even vacuum, and (22) give \(\operatorname{Tr}_{o}(K/\lambda)^b\ge1/3\) for large \(w\), by the odd/even trace ratio. The elementary bound \(\operatorname{Tr}(K/\lambda)\le e^{C_\beta w^2}\) follows by bounding the one-layer diagonal kernel above and testing the constant for a vacuum lower bound, each action containing at most \(Cw^2\) bounded terms. The temporal convolution \(e^{\beta p\cdot p'}\) is positive by its tensor-power series. Spending \(b-1\) steps on the largest odd eigenvalue proves (23), with a decreased absolute \(c\). For each finite sheet the partition ratio is continuous in its pins, so neighborhoods of the example still violate a proposed pin-uniform subarea lower bound, and have positive Wilson measure. No estimate in (22) gives their probability on the unconditioned torus. This prevents using the signed conditional bound as a substitute for the average in (7).

## Actual sign cancellation and the width information it gives

**PROVED (without either seed).** Let \(d_\beta=\log\int_{SU(2)}e^{\beta\operatorname{tr}g/2}\,dg\) and fix sufficiently large \(\beta\). There is an absolute \(C_1\) such that for
\[
        C_1\beta^{5/6}<s<d_\beta,\qquad
        N=\lfloor e^{s w^2/2}\rfloor ,
\]
the translated-stack measure \(\nu\) of row 1175 satisfies, as \(w\to\infty\),
\[
 \mathbb E_\nu\prod_x|\tanh J_x|\longrightarrow1,\qquad
 0\le\mathbb E_\nu\prod_x\tanh J_x
             \le C_\beta\exp[-c_\beta e^{(s-C_1\beta^{5/6})w^2}],
 \qquad \Pr_\nu\!\left(\prod_x\operatorname{sgn}J_x=-1\right)
             \longrightarrow\tfrac12 .                               \tag{24}
\]
Here \(J_x=\beta\sum_{p\in x} w_p\) for each of the \(N^2\) disjoint stacks of \(w^2\) faces, and \(P_J=\prod_x\operatorname{sgn}J_x\), with an arbitrary fixed sign at zero. The interval for \(s\) is nonempty since Haar integration on a cap of radius \(\beta^{-1/2}\) gives \(d_\beta\ge\beta-C\log(2+\beta)\). To see the first assertion directly, keep the other Wilson factors and weight these stacks by \(\prod\cosh J_x\). Removing one cosh gives an expectation of its reciprocal at most \(2e^{-d_\beta w^2}\) by expanding the remaining signs, moving their total twist to the deleted stack and applying the directional deletion comparison of row 1167. Each removed normalized temporal convolution is replaced by the constant projection below it in positive-operator order. Trace Hölder over the time layers pays the ratio of one-link integrals per deletion, and the label-averaged denominator is at least \(Z/2\). Thus \(1-\mathbb E_\nu\prod|\tanh J_x|\le2N^2e^{-d_\beta w^2}\). The signed expectation is exactly \((1-z)/(1+z)\) by summing parity. Apply (18) to this same ratio using the separate spread insertions, with \(m\ge cN^2/R\), \(K\le C_1\beta^{5/6}w^2\). The difference between the parity sign and the signed product has expectation in absolute value bounded by the first error. This proves (24) and \(z\to1\) for the original Wilson integral. No numerical value of a sign average enters. [Stack identity and deletion, row 1175 (14), (17)–(18)](gap-solve16-astra62.md) · [Temporal deletion proof](gap-solve12-astra62.md)

**PROVED (additional lower bound assuming a seed).** Let \(L_\beta=\log(2+\beta),\ J_\beta=1+\log(2+L_\beta),\ D_\beta=C_2 L_\beta^3 J_\beta^2\), with the absolute constant from the actual elementary twist insertion of row 1171. At fixed cutoff with competing seed and \(w\) sufficiently large, take \(a=b=\lceil K_q n_0(1+D_\beta w^2)\rceil+4w\). Then
\[
 \sigma_\beta(w)\ \ge\ b^{-2}e^{-D_\beta w^2},\qquad
 \limsup_{w\to\infty}{[-\log\sigma_\beta(w)]_+\over w^2}
                 \le D_\beta .                                       \tag{25}
\]
Indeed all periods exceed the required constant times \(\sqrt{1+\beta}\), and row 1171 gives \(z\ge e^{-D_\beta w^2}\). Choose \(K_q\) large enough for the error in the tanh version of (8) to be at most half this lower bound. Then use \(\tanh u\le u\). The limsup conclusion holds under the ordinary seed as well by (3). Here a bound on one twist at a polynomial normal period yields a bound on the infinite-plane pressure difference. The coefficient in (25) improves with respect to (14) as \(\beta\to\infty\), under its additional premise. At fixed coupling (25) still allows a strictly positive area coefficient. [Actual rectangular twist insertion, row 1171 (9), (32)–(33)](gap-solve14-astra62.md)

## Spreading the insertions in both normal directions

**PROVED (a stronger unconditional Wilson bound).** There are absolute \(c,C>0\) such that for every sufficiently large fixed \(\beta\) and all \(w\ge w_0(\beta)\),
\[
 \sigma_\beta(w)\ \ge\
 c\,\beta^{-1/2}\exp[-C\sqrt{\beta}\log(2+\beta)\,w^2].                \tag{26}
\]
Equation (24) holds throughout \(C\sqrt\beta\log(2+\beta)<s<d_\beta\), with this new coefficient in its exponential. The width threshold in (26) is allowed to depend on the coupling. The argument uses conditional *partition* odds in many disjoint boxes. Opposite rotations of a single link configuration need not be inverse maps on a common orbit.

**PROVED (a local axis with a deterministic weighted error).** Let \(l\ge2\), with every period \(>100l\). Choose direction 1 as time. For a vertex \(x\), take nonnegative translated tent weights \(\phi_x(z)\) supported on a cube of side \(2l+1\) centered at \(x-4l\hat 1\), with \(\sum_z\phi_x(z)^2=1\). Products of the functions \((1-|k|/l)_+\), normalized in \(\ell^2\), give \(\sum_z|\phi_x(z)-\phi_y(z)|^2\le C/l^2\) for neighbors. The one-dimensional squared derivative sum before normalization is \(O(l^{-1})\), while the squared norm is at least \(c l\). Set the \(z\)-block of the three-row operator \(F(x)\) equal to \(\phi_x(z)T(x,z)\), where \(T\) is adjoint transport along the coordinate-ordered path from \(x\) to \(z\), moving backwards in time first. Then \(F(x)F(x)^{\mathsf T}=I\). For common independent standard three-vectors \(\eta_z\) put \(v(x)=F(x)\eta/|F(x)\eta|\). On the probability-zero event of a zero vector use a fixed default axis. Only links with positive base time strictly earlier than \(x\) are read.

**PROVED.** For an edge \(e=xy\), there are deterministic nonnegative weights \(b_{e p}\), supported within \(Cl\) of \(e\), with \(\sum_p b_{e p}\le Cl^2\), for which, for every configuration and any plaquette signs \(\tau_p\),
\[
 \mathbb E_\eta|v(x)-T_{xy}v(y)|^2
          \le C/l^2+\sum_p b_{e p}(1-\tau_p w_p).                     \tag{27}
\]
Indeed the conditional Gaussian normalization estimate in row 1171 bounds the left side by \(C\|F(x)-T_{xy}F(y)\|_{\rm F}^2\). To see it, split the Gaussian vector into the row space of \(F(x)\) and its independent complement, use \(E|F(x)\eta|^{-2}<\infty\) in three dimensions and the chord bound for vector normalization. The scalar tent differences contribute \(C/l^2\). For each common endpoint \(z\), comparison of the two ordered paths moves the extra unit edge through at most four coordinate runs of length \(O(l)\), filling at most \(Cl\) unit plaquettes in width-one strips. The same bound applies wherever one of the two weights is zero by allocating the weight difference first and defining both short ordered paths to that endpoint. Triangle and Cauchy–Schwarz bound the squared adjoint transport difference by \(Cl\) times the sum of signed deficits on those strips because adjoint transport ignores the centre and \(\|\operatorname{Ad}_g-I\|_{\rm F}^2\le C(1-\tau\,\operatorname{tr}g/2)\) for either sign. Average with the squared tent coefficients. Their sum is one and a strip contains at most \(Cl\) plaquettes, giving (27). The sharp ordinary-law rectangle estimate of row 1171 is unnecessary for this pathwise bound. [Covariant axes and Gaussian normalization](gap-solve14-astra62.md)

**PROVED (conditional odds).** Take \(R\ge2\) and disjoint normal-plane squares of side \(C_3(R+l)\) with separating corridors of width at least three, extended across the full transverse torus. Place one labelled stack in each centre, with signs \(\tau_i=\pm1\). One can place \(m\ge c ab/(R+l)^2\) for sufficiently large \(a,b\) at fixed \(R,l\). Condition on the links \(Y\) outside the interiors. The link variables and labels of different interiors are then conditionally independent, since no plaquette meets two interiors. Let \(\delta_i(Y)\) be the absolute log ratio of the two conditional partition functions in interior \(i\).

**PROVED.** Use the compact normal-plane profile of row 1169 in each square. Its real angles \(u_e\) have curl \(\pi({\bf1}_o-\rho)\), with \(\sum\rho=1,\ 0\le\rho\le R^{-2}\), and \(\sum_{\text{normal plane}}u_e^2\le C\log(2R)\). For clarity, send unit flow outwards by equally partitioning it along the \(s+1\) vertices of each diagonal shell in one quadrant. From \((k,s-k)\) the fraction \((k+1)/(s+2)\) goes to \((k+1,s-k)\) and the rest to \((k,s+1-k)\). This takes uniform mass on shell \(s\) to uniform mass on shell \(s+1\). Stop equal shares on the shells \(R,\ldots,2R-1\). Rotating this dual flow through a quarter turn and multiplying by \(\pi\) gives the profile, with \(O(s+1)\) edges of size \(O(1/(s+1))\) on each shell. Translate the square to leave room for the past in (27). From either label, toggle it and rotate the affected forward links by left multiplication by \(\exp(\epsilon u_e v(x))\) with \(\epsilon=\pm1\). For fixed \(\eta,\epsilon\) the map preserves conditional product Haar. The multipliers at each time depend only on earlier original layers, which are recovered in order starting at the untouched buffer. It fixes \(Y\). [Single-profile construction](gap-solve13-astra62.md)

**PROVED.** For the starting label and configuration, average the action increase over \(\epsilon,\eta\). By (27) it is at most
\[
 B_i=C\beta w^2\{R^{-2}+l^{-2}\log(2R)\}
                   +\beta\sum_p h_{i p}(1-\tau_p w_p),\qquad
 \sum_p h_{i p}\le C w^2(1+l^2)\log(2R).                              \tag{28}
\]
Here \(h_{i p}\ge0\) are deterministic, supported in square \(i\) including its buffer, with \(\max_p h_{i p}\le H(l,R)<\infty\) independently of all periods and \(w\). To check the sign in the estimate, transport the four inserted axes to the face base using the original edges. Their differences from the base axis are bounded by \(d=\sum_{e\in\partial p}|v(x)-T_e v(y)|\). With identical axes the central toggle leaves a residual angle at most \(\pi\rho_p\), zero away from normal squares. Thus the scalar deficit of either signed rotation is at most \(C(\rho_p^2+d^2\sum_{e\in p}u_e^2)\). In its imaginary part averaged over opposite rotations only terms with two or four sine factors survive. With equal axes these terms are real. The residual norm is at most \(C d\sum_{e\in p}u_e^2\). Pair it with the imaginary part of the original signed plaquette, whose squared norm is at most twice its deficit. This bounds the extra increase by \(C(d^2+1-\tau_p w_p)\sum_{e\in p}u_e^2\). Sum the squared profile, \(\sum\rho^2\le R^{-2}\), and (27), including the \(w^2\) copies. The local support and weight sum per edge in (27), the bounded angles and the bounded number of lattice edges in a ball of radius \(Cl\) also give the required finite \(H(l,R)\). This is the opposite-rotation cancellation of row 1171 used in both sign sectors.

**PROVED.** For the more probable of the two labels at given \(Y\), the log ratio to the other one is at most the conditional mean of \(B_i\) at that label. Indeed the change of variables expresses the ratio of other to starting mass as the mean of the exponential of minus the action increase. Apply Jensen for each map and then average. The more probable label has probability at least one half, so \(\delta_i(Y)\le2E[B_i\mid Y]\) under the joint labelled measure. For any union \(I\) of \(k\) prescribed squares write \(h_p=\sum_{i\in I}h_{i p}\). The supports are disjoint, hence \(h_p\le H\). Independently mark each plaquette with probability \(h_p/H\). Jensen in the marks followed by (17) gives
\[
 E\exp\{(c_0/H)\beta\sum_p h_p(1-\tau_p w_p)\}
      \le 2\exp\{(C_0-1) H^{-1}\sum_p h_p\}.                         \tag{29}
\]
Conditional Jensen gives the same upper bound with the weighted sum replaced by its conditional expectation given \(Y\). Consequently the probability that all \(k\) odds exceed
\[
 K=C_4 w^2\{\beta/R^2+(\beta/l^2+1+l^2)\log(2R)\}
\]
is at most \(2\exp[-c k w^2(1+l^2)\log(2R)/H]\) for large absolute \(C_4\). A union bound over subsets of size \(\lceil m/2\rceil\) now costs at most \(2e^{-c_{l,R} m w^2}\) for \(w\) sufficiently large at fixed \(l,R\). On the complementary exteriors the absolute conditional expectation of total parity is the product of \(\tanh(\delta_i/2)\), and is at most \(\exp[-m e^{-K}/2]\). Passing to (1) as in (18), then taking \(l=R=\lceil\beta^{1/4}\rceil\), proves (26) and the extension of (24). This proof controls rare unfavorable exteriors for a positive density of insertions. An estimate of the mean cost of a single unconditional insertion alone would not give (29).

**PROVED (limit of the quadratic cost).** The typical transverse mismatch bound following (18) also applies to every axis field of (27), for each auxiliary realization. For the explicit profile, some normal edge next to the source has \(|u_e|\ge\pi/4\) by its circulation, and \(|u_e|\le\pi/2\) for the equally split first shell. The two mixed orientations through a parallel copy of this edge see the transverse mismatch at its initial normal site, multiplied in squared chord by \(\sin^2 u_e\). This follows by factoring the two rotations on the parallel normal links across the unchanged transverse link. Thus the quadratic displacement proxy on these mixed faces alone is at least \(c_\beta w^2\) with probability \(1-e^{-c_\beta w^2}\), even though (28) controls conditional signed odds. Reducing its coefficient as a function of the *bare coupling* in (26) does not yield the subarea exponent in *width at fixed coupling* in (7). Controlling the signed Wilson integral beyond this proxy would require another estimate.

**PROVED (a barrier even where the actual signs are balanced).** Fix \(s\) strictly inside the enlarged interval in (26) and \(0<\epsilon<d_\beta-s\). In the thin-stack measure at \(N=\lfloor e^{s w^2/2}\rfloor\),
\[
 \nu\{\min_x|J_x|\le\epsilon w^2\}
             \le 2e^{-(d_\beta-s-\epsilon)w^2}.                       \tag{30}
\]
Indeed \(\operatorname{sech}J_x\ge e^{-|J_x|}\), and the one-stack bound in (24) applies before a union bound. Consider any stationary update that changes each \(J_x\) by at most \(\epsilon w^2\) per step (single-link updates obey this for large \(w\) at fixed \(\beta\)). A parity change must start in the event in (30). The stationary probability of a parity change during \(k\) steps is at most \(2k e^{-(d_\beta-s-\epsilon)w^2}\). Starting instead in stationarity conditioned on positive parity costs a factor \(1/\nu(P_J=+1)=2+o(1)\). At \(k\le e^{(d_\beta-s-\epsilon)w^2/2}\), the negative-parity probability is \(o(1)\), whereas its stationary value tends to one half by (24), (26). This proves an exponentially long obstruction to local mixing of the actual auxiliary measure in a range where the *unconditional* Wilson sign answer is known. Row 1175 had a local barrier and branch-conditional conclusions at larger widths. No Markov chain has been run. [Local parity change, row 1175 (30)](gap-solve16-astra62.md)

## What fixes the first width

**PROVED (resolution allowed by the scalar estimates).** Even exact knowledge that the ratio is of the tanh form in (8), together with the competing upper bound in (3) and the lower bounds (25)–(26), permits both orders of first width in (13). For a concrete positive transfer system at each fixed \(w\), give a two-dimensional \(\mathbb Z_2\) lattice gauge model coupling \(J(w)=\operatorname{arctanh}(\exp[-s(w)])\). On an \(a\times b\) torus its ordinary plaquette signs are exactly the even-parity patterns, all of equal Haar multiplicity. An elementary twist selects the odd ones. Every even pattern is obtainable by joining negative plaquettes in pairs by dual paths and flipping the crossed links. Factoring the even and odd sums of \(\prod_p e^{J(w)\xi_p}\) gives exactly \(z=\tanh(s(w)ab/2)\). Fix the cutoff. A profile \(s(w)=e^{-k w^2}\) with sufficiently small \(k>0\) obeys all the cited large-width bounds and crosses at \(w_*(N)\sim \sqrt{2\log N/k}\). A profile \(s(w)=e^{-k w^2/\log w}\) with \(k>c/n_0^2\) in (3), strictly beyond its exponential coefficient, also obeys them and has \(w_*(N)\sim\sqrt{\log N\log\log N/k}\). Both follow by solving \(N^2s(w)\le\log3\), with integer rounding negligible. A constant positive profile obeys the ordinary branch lower bound and every unconditional lower bound here. These examples model the scalar plane data at each width. They do not identify the transverse dynamics of the four-dimensional Wilson model. In particular, neither the crossover shape nor the improved weak-coupling coefficient supplies (7).

**PROVED (a coefficient at the lower edge under the competing seed).** Using the actual \(D_\beta\) in (25) and the earlier unconditional lower edge in (13),
\[
 \liminf_{N\to\infty}\frac{w_*(N)^2}{\log N}\ge \frac{2}{D_\beta}.     \tag{31}
\]
Indeed these first widths diverge at fixed cutoff and are \(o(N)\). At the first width, (8) gives \(\sigma_\beta(w)N^2\le\log3+o(1)\). In (25) its auxiliary period \(b\) is \(O_j(w^2)\). It follows that \(D_\beta w^2\ge2\log N-4\log w-O_j(1)\). The upper edge in (13) makes the correction \(o(\log N)\). This bound still leaves the two width orders above.

## Allowing arbitrary changes of both normal link fields

**PROVED (uniform area obstruction for the quadratic comparison).** Let \(U\) have the ordinary Wilson law on \((a,b,w,w)\), with all periods at least five. Hold its links in directions 3 and 4 fixed. The replacement \(\widetilde U\) on directions 1 and 2 can depend on the *entire* configuration and vary from site to site. On the target use the elementary stack representative \(\omega_p=-1\) on the \(12\)-plaquettes at one fixed normal position and \(+1\) elsewhere. For a forward normal link put \(R_i(x)=\widetilde U_i(x)U_i(x)^{-1}\). Sum each unoriented face once to define the nonnegative squared displacement
\[
 \begin{split}
 D(U,\widetilde U)={}&
 \sum_{p\parallel12}|1-\omega_p\widetilde U_p U_p^{-1}|^2\\
 &+\sum_{i=1,2;\ k=3,4;\ x}
 |R_i(x)-U_k(x)R_i(x+\hat k)U_k(x)^{-1}|^2 .
 \end{split}                                                        \tag{32}
\]
All normal plaquettes use the same positive orientation at their base. On a mixed face \(p=(i,k)\), the displacement in the second sum is the chord of the multiplier \(B_p\) in its Wilson trace. Indeed with \(S=U_k(x)R_i(x+\hat k)U_k(x)^{-1}\), cyclicity gives \(\operatorname{Re}\widetilde U_p=\operatorname{Re}(S^{-1}R_i(x)U_p)\). Thus (32) includes precisely the mixed-face quadratic comparison used on the profiles above. For every \(A>0\) there are \(c_A,C_A>0\), independent of coupling and all periods, such that
\[
 \Pr_\beta\left\{
    \inf_{\widetilde U_{3,4}=U_{3,4}} D(U,\widetilde U)
         <{c_A w^2\over 1+6\beta}\right\}
           \le C_A abw^2 e^{-A w^2},\qquad
 \inf_{\widetilde U_{3,4}=U_{3,4}}D(U,\widetilde U)\le4w^2.           \tag{33}
\]
The upper bound is deterministic, by choosing the identity replacement and the usual elementary stack representative. The infimum is measurable by continuity on the compact finite product. The lower bound holds even for rotations whose angles, axes, support and location vary across the transverse torus. Row 1141 supplies the two-plaquette pinning estimate. Here the rounded relative field of an arbitrary replacement determines a surface to which that estimate applies. [Two-loop pinning and conditional bound, (3)–(6)](gap-crux2-astra62.md) · [Connected curvature counts](gap-solve12-astra62.md)

**PROVED (local alternatives on each face).** At every normal link set \(\eta_i(x)=\operatorname{sgn}\operatorname{Re}R_i(x)\), with a fixed sign for ties, and take \(\eta_3=\eta_4=1\). The face signs \(c_p=\omega_p(d\eta)_p\) represent the same nontrivial class as the twist. Where \(c_p=-1\), either the term for \(p\) in (32) is at least one, or some normal multiplier based at a vertex of \(p\) has \(|\operatorname{Im}R_i(x)|\ge c_*>0\). In fact if all its multipliers are within chord \(1/8\) of their rounded signs, telescoping their insertion into the normal plaquette, or into the displayed mixed multiplier, changes the product from the central value \(-1\) by at most \(4/8\). Its chord from \(+1\) is then at least \(3/2\). A unit quaternion at distance at least \(1/8\) from the nearer centre has imaginary norm bounded below by an absolute constant. There are no negative \(34\)-faces.

**PROVED (localized cost of a noncentral multiplier).** At a vertex \(x\), base the northeast and southwest \(34\)-plaquette loops \(\gamma_1,\gamma_2\) there. Write
\[
 m_x=\min_{|v|=1,\ v\ {\rm imaginary}}
              \sum_{j=1,2}|v-\operatorname{Ad}_{U_{\gamma_j}}v|^2.
\]
For any \(0<t\le1\), the proof of row 1141 (3)–(4) gives \(\Pr(m_x<t\mid\text{all links outside the two loops})\le4(1+6\beta)t\). Namely the smaller Gram eigenvalue of the two imaginary holonomy vectors is \(m_x/4\). If the first vector is longer it bounds from below half the squared perpendicular projection of the second to the first axis, and vice versa. Leaving a private link of the tested loop unconditioned bounds this small-cap probability by the one-link pushforward estimate. Take the union of the two choices. This applies to any prescribed set of disjoint loop pairs by iterated conditioning. If \(m_x\ge t\) and \(|\operatorname{Im}R_i(x)|\ge c_*\), the sum of the mixed-face terms in (32) along those two loops is at least \(c t\) by telescoping the four covariant differences along each loop for \(R_i\) and applying Cauchy–Schwarz. The real component is fixed by conjugation. Thus a negative face either pays at least \(c t\) among a bounded number of nearby terms in (32), or one of its finitely many vertices has \(m_x<t\). Each term can be in only a bounded number of these neighborhoods, uniformly in all periods.

**PROVED (counting the required surface).** The dual faces of the negative cochain form a closed two-cycle modulo two. Break it into components sharing dual edges. Each is closed separately, since all faces incident to any one edge belong to the same component. Some component has odd pairing with a normal \(12\)-torus, since the sum represents \(\omega\). This pairing is the same on all \(w^2\) disjoint parallel normal tori by the coboundary identity on the strip between them. Thus that component contains \(k\ge w^2\) faces. If \(D<c' t w^2\) for a sufficiently small absolute \(c'>0\), at least half the faces of this component must have a vertex with \(m_x<t\), by bounded overlap of the local costs.

**PROVED.** There are at most \(6abw^2 C_5^k\) rooted candidates for such a component, by a doubled spanning-tree walk in the bounded-degree graph on dual faces. On any prescribed candidate, choose a subset of at least half of its faces and one candidate vertex per chosen face, in at most \(C_6^k\) ways. Bounded face incidence gives at least \(c k\) distinct vertices. Greedy deletion of overlapping loop pairs gives at least \(c' k\) vertices with disjoint pairs, by the fixed diameter of these neighborhoods. Their joint small-pin probability is at most \([4(1+6\beta)t]^{c'k}\). Choose \(t=\epsilon_A/(1+6\beta)\), with \(\epsilon_A>0\) small enough that \(C_5 C_6(4\epsilon_A)^{c'}\le e^{-A-1}\). Sum over \(k\ge w^2\) to obtain (33). All events counted here are in the original Wilson field. The choices made in a replacement incur no probabilistic independence assumption.

**PROVED (consequence at the discriminating geometry).** On any sequence with \(\log(ab)=o(w^2)\), including \(a=b=N,\ w=\lceil\sqrt{\log N}\log\log N\rceil\), (33) forces every such change to pay at least \(c w^2\) in \(\beta D\) with probability tending to one for \(\beta\ge1\). This includes the infimum over all changes before Wilson averaging. In particular an upper bound obtained by paying a fixed positive multiple of this displacement cannot provide the subarea Wilson input, even with adaptive supports. The true signed action retains a pairing with the original plaquette on every face. Equations (24), (26) show that signed parity can already cancel at some exponential normal areas. Equation (33) explains which positive comparison loses that information.

**PROVED (the signed remainder that would have to be kept).** Choose the normal multiplier \(B_p=\omega_p\widetilde U_p U_p^{-1}\) and the mixed multiplier \(B_p=S^{-1}R_i(x)\) just specified. Write \(S_0(U)=\beta\sum_p(1-\operatorname{Re}U_p)\), with \(S_\omega\) its twisted version. The identity \(|1-B|^2=2(1-\operatorname{Re}B)\) and quaternion multiplication give
\[
 \frac{S_\omega(\widetilde U)-S_0(U)}{\beta}
 =\tfrac12D-
 \sum_p\left[(1-\operatorname{Re}B_p)(1-\operatorname{Re}U_p)
              -\operatorname{Im}B_p\cdot\operatorname{Im}U_p\right].   \tag{34}
\]
Take \(B_p=1\) on the unchanged transverse faces. Along the geometries following (33), any randomized replacement fixing the transverse links and having mean signed action increase \(o(w^2)\) must have the expectation of the bracket sum, times \(\beta\), at least \(c w^2\) for large \(w\) and \(\beta\ge1\). This follows by averaging (33), since its event is simultaneous for all replacements. Thus even a method that retained some signed terms but bounded this whole correction by \(o(w^2)\) could not give the needed small mean action cost. Nothing in (34) gives the size of the correction for a comparison which actually attains the Wilson twist ratio.

**PROVED (separation on the same pure Wilson tori).** Fix \(\beta\) and \(s\) in the open interval of (26), and take \(a=b=N=\lfloor e^{s w^2/2}\rfloor\). Given \(A>s\), equations (24), (26) and (33) give simultaneously
\[
 -\log z(N,N;w)\longrightarrow0,\qquad
 \Pr_\beta\left\{\beta\inf_{\widetilde U_{3,4}=U_{3,4}}
           D(U,\widetilde U)\ge c_A' w^2\right\}\longrightarrow1.     \tag{35}
\]
For the first limit, write \(-\log z=2\operatorname{arctanh}((1-z)/(1+z))\) and use the double-exponential upper bound in (24) with the coefficient from (26). For the second, \(N^2 w^2e^{-Aw^2}\to0\) and \(\beta/(1+6\beta)\ge1/7\) for \(\beta\ge1\). Thus the minimum of the entire quadratic comparison in (32) costs order area at precisely these torus sizes where the true signed twist free energy vanishes. This separation uses the original four-dimensional Wilson integrals for both conclusions.

## Remaining Wilson inputs

**OPEN.** At every sufficiently fine fixed cutoff, (7) calls for widths along which \([-\log\sigma_{\beta_j}(w)]_+=o(w^2/\log w)\). The signed Wilson bounds (25)–(26) allow the competing rate. Equation (33) gives an area obstruction for every quadratic comparison that preserves transverse links, (22) gives a signed counterexample with prescribed exterior fields, and (30) bounds the rate of any local attempt to change the auxiliary parity. The two explicit plane models after (30) show the width ambiguity even with the crossover shape specified exactly. On the physical neutral side, (20) requires an order-one finite-area estimate at a fixed physical size. The local factor following (21) preserves the limiting pressures and twist ratios while adding \(\log2\) to that excess. I have no remaining argument from these routes for selecting the pure Wilson branch or bounding its physical neutral trace. The selective inequality, (W), and the Jaffe–Witten mass gap remain open. [Council comparison](gap-council-synthesis.md) · [Wall and prior results](../parts/gap.md)

RESULT — Row 1177. PROVED by hand, pending independent review. Given the one-cube physical neutral bound, (W) is equivalent to the planar tension test (7). In the competing branch the elementary twist follows (8) and first reaches one half or less at a width between \(c_\beta\sqrt{\log N}\) and \(C_j\sqrt{\log N\log\log N}\). For pure Wilson fields at sufficiently large fixed \(\beta\), (26) bounds the tension below by \(c\beta^{-1/2}e^{-C\sqrt\beta\log(2+\beta)w^2}\). On the same tori (35) gives a vanishing twist free energy and an area cost for every quadratic comparison (32) fixing the transverse links. OPEN. Wilson branch selection, the physical neutral upper bound, (W), and the Jaffe–Witten mass gap remain unresolved.
