# Repo search

**GUIDE.** FINISH row 1315, checkout `e60e519c3`. The row-specific prior is absent. The lead's November 8 digest searched main and PRs 10114, 10133, 10134 and 10141. I checked the following sources against the question of a lower spectral edge that survives removal of the cutoff.

**GUIDE.** On PR 10114 (`f76f6c649c`), `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149, gives a positive one-step plaquette witness at finite \(\beta\) and a transfer contraction for \(0<\beta\le1/32\). On Grok's PR 10133 (`89faef229f`), `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–86, leaves the crossover and source transport open. On PR 10134 (`1e70c7211a`), `mass-gap-interface.md` distinguishes existence of excitations, the lower spectral edge and identification with Yang–Mills. On PR 10141 (`a2f6a430e2`), `fp1.md`, lines 299–315, bounds a constrained classical field at one scale. On main `8b11ae2bb9`, Theorem ZD-c of `research/mass-gap/library/gap-phys-seed.md` relates a physical thermal seed to a volume growth estimate and a cube energy estimate. The open registry has no other owner for the specific cap/base spectral estimate tested below. [Lead's search](prior/repo-search-2026-11-08.md) · [Open registry](open-registry.md)

## Published work and choice of estimate

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the distinction between their scalar cyclic sector and the full algebra, and the example of polynomial clustering with spectrum down to zero. The index entries in chunks 01 and 29 and the obligations list point to the passages checked here. Their account explicitly excludes a mass-gap claim. [Outline 581–599](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L581-L599) · [Outline 31858–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [Account I 2704–2712](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** Row 1218 records the full thermal-window criterion of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. The four-author cube-dynamics paper of Bhattacharjee, Bhattacharya, Lockwood and Romanov controls very coarse straight paths at weak coupling. The ascent to the fine law requires additional estimates. Zeng Chunping's tunnelling route likewise has a microscopic input. I use row 1218 for this literature comparison. [Published-work reading](prior/gap-onebound-read-sol.md)

**GUIDE.** Row 1298 compares a resampling chain to the actual Wilson transfer. Row 1307 checked the comparison. Row 1300 tested its scaling on free modes. I use the stationary flux of a negative-trace plaquette to test the proposed order-\(a\) lower bound (37) in the interacting vacuum. [Row 1298](gap-solve34-astra62.md) · [Row 1307](gap-solve34-check-opus.md) · [Row 1300](gap-mini-solve-ax-opus.md)

**PROVED.** At fixed physical side \(L\), with \(a=L/n\) and \(\beta/\log n\to 11/(3\pi^2)\), choose a fixed \(\theta>\pi/2\) sufficiently close to \(\pi/2\). The number of spatial plaquettes with \(w_p<\cos\theta\) then has Rayleigh quotient \(o(a)\) for the specified resampling chain. This holds after restricting the chain to any gauge-invariant set of probability tending to one by rejection of proposals that leave it. The fluctuation estimate (20) and the flux bound (10) give (21). For the true Wilson transfer each individual centred, normalized indicator has vanishing weight at bounded physical energy by (8).

**OPEN.** The Jaffe–Witten problem requires a nontrivial continuum SU(2) Yang–Mills theory on \(\mathbb R^4\) satisfying the axioms of quantum field theory, with a positive lower spectral edge on its vacuum complement. The estimates below leave both the collective physical spectral bound and the continuum construction open.

## What a cap update can do to one plaquette

**GUIDE.** Work on an even periodic spatial cube of side \(n\) links with Wilson weight \(\exp[-\beta\sum_q(1-w_q)]\), where \(w_q=\tfrac12\operatorname{tr} U_q\) and \(U_q\) is the ordered plaquette product. Let \(P\) denote the one-step Wilson transfer divided by its top eigenvalue and transformed by its positive ground state to a Markov operator. Its stationary law \(\nu\) is the time-zero law in the infinite-time limit at fixed \(n,\beta\). Physical tests are gauge invariant. For a reversible kernel \(S\) the gap used below is the infimum of \(\langle f,(1-S)f\rangle/\operatorname{Var}(f)\) over such tests of positive variance, with the stationary inner product for \(S\).

**GUIDE.** Row 1298's kernel \(K\) exposes both neighbouring slices and all central links off one uniformly chosen colour. The six colours specify a link direction and the parity of the sum of the other two spatial coordinates. Hidden spins are drawn with flags as in that row. Flagged spins are redrawn from their indicated distributions, and unflagged spins are retained. For an active link \(e\), the four spatial staples give unit quaternions \(v_i\) oriented so the incident traces are \(v_i\cdot x_e\). Put \(h=\sum_{i=1}^4v_i\) and \(H=|h|\). A cap flag requires \(H\ge3\), and both spins are within angular radius \(\beta^{-1/2}\) of \(h/H\). The base flag has probability \(p_0=e^{-4\beta}/2\) before the hidden spin is drawn, with density \(\rho_h(ds)\propto e^{\beta h\cdot s}ds\). The rejection set \(G_d\) requires \(\beta\sum_q(1-w_q)\le Bd^3\) in every translated spatial cube of side \(d\), for each of the three face orientations separately. [Definitions and comparison (29)–(36) in row 1298](gap-solve34-astra62.md)

**PROVED.** Fix a spatial plaquette \(p\) and \(0<\eta<1\). Put \(A=\{w_p<-\eta\}\). For all sufficiently large \(\beta\), every cap update preserves \(\mathbf1_A\). Indeed, at either end of such an update,
\[
 v_i\cdot x_e=h\cdot x_e-\sum_{j\ne i}v_j\cdot x_e
 \ \ge\ 3\cos(\beta^{-1/2})-3>-\eta .
\]
An active colour contains at most one edge of \(p\). An update away from \(p\) leaves its trace fixed. This proves the assertion in both directions and for every exterior. In particular the cap-only chain restricted by rejection to \(G_d\) can have a nonconstant fixed gauge-invariant function. For example one spatial link equal to \(-1\) with all others \(1\) lies in the interior of \(G_d\) when \(Bd^3>8\beta\), and an adjacent plaquette belongs to \(A\). The flat field is in the interior of the complement in \(G_d\). Both neighbourhoods have positive vacuum probability. This is a local obstruction inside the energy tests of (36), whereas the configuration with every staple sum zero in row 1298 is spatially extensive.

**GUIDE.** To test the corrected chain on \(A\), divide its stationary base-flag flux by the variance of the indicator. The flag probability \(p_0\) is specified before sampling the spin. Conditioning on the old field changes that probability.

## The rate at which the base flag sees that plaquette

**GUIDE.** Set \(D_q(x)=1-w_q(x)\), and more generally \(A_\theta=\{w_p<\cos\theta\}\), \(\pi/2<\theta<\pi\). Write \(D_\theta=1-\cos\theta\). For \(e\in\partial p\) define \(D_e=\sum_{q\ni e,\ q\ {\rm spatial}}D_q\). For any finite set \(S\) of distinct faces containing a common coordinate direction, row 1149, (23) bounds the exponential moment of their total deficit by \(z_\beta^{-|S|}\) in the homogeneous periodic Wilson law. Applied to the four spatial faces at \(e\) this gives
\[
 \nu(e^{\beta D_e})\le z_\beta^{-4},\qquad
 z_\beta=\int_{SU(2)} e^{-\beta(1-w(u))}\,du
            \ge c(1+\beta)^{-3/2}.                              \tag{1}
\]
The last bound follows by integrating in an angular cap of radius \((1+\beta)^{-1/2}\). The same marked-face inequality holds on rectangular periodic four-tori prior to taking the vacuum limit. In a transfer direction common to the marks, deleting their electric factors replaces normalized single-link convolution by the projection on constants. It is below the original positive normalized convolution in operator order. Tensoring, applying the gauge projection and the magnetic sandwich preserve the order. If the common period is \(h\), trace Hölder with exponents \(h\), and eigenvalue monotonicity for the positive sandwiches, bound the resulting normalized trace by the homogeneous one. Each deletion has scalar cost \(z_\beta^{-1}\). This is the argument of row 1149, using the positive Wilson multipliers of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Row 1149, (23)](gap-solve4-astra62.md) · [Outline 2195–2213](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2213)

**PROVED.** Under the base density \(\rho_h(ds)\propto e^{\beta h\cdot s}\,ds\), with the other spatial links fixed, put \(D_e(s)=4-h\cdot s\). Its minimum is \(4-H\). The integral of \(e^{-\beta D_e(s)}\) is at least \(c(1+\beta)^{-3/2}e^{-\beta(4-H)}\), by integration near a maximizer of \(h\cdot s\) and \(H\le4\). On \(A_\theta\), \(D_e(s)\ge D_\theta\). Therefore
\[
 \mathbb E_\nu[\rho_h(A_\theta)]
 \le C(1+\beta)^{3/2} e^{-\beta D_\theta}\nu(e^{\beta(4-H)})
 \le C(1+\beta)^{15/2} e^{-\beta D_\theta}.                    \tag{2}
\]
Here \(A_\theta\) inside \(\rho_h\) uses the candidate spin at \(e\) and the unchanged other three edges. The last inequality follows from \(4-H\le D_e(X)\) and (1).

**PROVED.** Write \(Q_K(A,A^c)=\Pr_\nu(X\in A,X'\notin A)\) for the stationary outgoing flux. For large \(\beta\) the cap result above and the base probability \(p_0\) give
\[
 Q_K(A_\theta,A_\theta^c)
    \le C(1+\beta)^{15/2}\exp[-(4+D_\theta)\beta].             \tag{3}
\]
Indeed only an update of an edge of \(p\) can contribute. Conditional on the two temporal neighbours and the unselected colour complement, a base flag at the selected edge has the fixed probability \(p_0\). Given this flag, the *old* spin has law \(\rho_h\), and the three other edges of \(p\) are in the complement. Consequently its contribution is at most \(p_0\mathbb E_\nu[\rho_h(A_\theta)]\). Averaging over colours preserves the bound. Rejection on \(G_d\) can only remove exits between \(A_\theta\cap G_d\) and \(A_\theta^c\cap G_d\). The remaining task for this test is a lower bound for its variance under the restricted law.

## A lower bound for the Wilson probability

**PROVED.** Let \(p\) denote one oriented elementary square in the infinite unit lattice \(\mathbb Z^4\). For any \(\alpha>0\) and \(\epsilon>0\) there is a real, finitely supported edge cochain \(u\) with
\[
 (du)_p=\alpha,\qquad \sum_{q\ne p}(du)_q^2\le(1+\epsilon)\alpha^2 .
                                                                    \tag{4}
\]
Count each positive orientation once. To prove this, project \(\ell^2\) of plaquettes onto the closure of curls of finitely supported edge cochains, with orthogonal projection \(J\). The Fourier symbol of \(d\) is \(v\mapsto t\wedge v\) with \(t_i=e^{ik_i}-1\). At almost every \(k\) it has rank three in the six-dimensional plaquette fibre. The projection onto its range is the symbol of \(J\) because the orthogonal complement of the closed range is \(\ker d^*\), characterized by the pointwise adjoint equation after Fourier transform. Finite edge cochains are dense and \(d\) is bounded. Translation and coordinate permutation symmetry give equal diagonal entries in the six orientations. Their sum is the integral of the rank against normalized torus measure, hence \(J_{pp}=1/2\). Thus \(2\alpha J\delta_p\) has value \(\alpha\) at \(p\), squared norm \(2\alpha^2\), and is real since \(d\) is real. Approximate it in norm by real curls of finite support and rescale each approximant by the ratio of the desired to its achieved value at \(p\). This proves (4). The rank-three curvature symbol is from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Here it selects a deterministic group-valued deformation in the nonlinear Wilson integral. [Outline 1733–1778](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1733-L1778)

**PROVED.** In the ordinary isotropic periodic four-dimensional Wilson measure, if every period is sufficiently large and \(\beta\) is sufficiently large, then, for \(0<\theta<\pi\) and any \(\epsilon>0\),
\[
 \Pr(A_\theta)\ \ge\ c_{\theta,\epsilon}
        \exp[-\beta(D_\theta+\tfrac12\theta^2+\epsilon)] .         \tag{5}
\]
The constants and required minimum periods are independent of the box. Take \(\alpha\in(\theta,\pi)\) sufficiently close to \(\theta\), then choose the accuracy in (4) sufficiently small. Fix an imaginary quaternion unit \(i\). The deterministic link field \(V_e=\exp(iu_e)\) is trivial outside a finite set, and its plaquette trace is \(\cos((du)_q)\). Using \(1-\cos x\le x^2/2\) on all other faces shows its total action in units of \(\beta\) is at most \(D_\theta+\theta^2/2+\epsilon/2\). The selected plaquette has strict room inside \(A_\theta\).

**PROVED.** Here is the positive-probability starting event needed to insert \(V\). Take one fixed finite rectangular box containing every changed bond and every edge of every face meeting those bonds. In sufficiently large tori this box embeds without wrapping. For any fixed link neighbourhood of the identity in this box, the event that *all* these links lie in the neighbourhood has probability bounded below uniformly in the periods at large \(\beta\). Indeed (1) for one mark gives an exponentially small upper bound, up to a polynomial in \(\beta\), on any fixed plaquette deficit exceeding any prescribed positive threshold. A union bound applies to the fixed box. When all its plaquette holonomies are sufficiently close to \(1\), a gauge can put all the box links in an arbitrarily small neighbourhood of \(1\). To see the uniformity, first set any spanning tree to \(1\) by vertex gauges. On this finite tree gauge slice, exactly flat fields have all links \(1\) because any closed edge walk in a rectangular grid contracts by elementary square moves and backtracks. Compactness of the slice and continuity now give the assertion for fields sufficiently close to flat. Apply independent Haar vertex gauges in the box. For each admissible starting field, the probability that the random gauges lie in prescribed small balls about a flattening gauge is bounded below by the product of their Haar ball masses. Continuity of multiplication, uniformly on the compact group, puts all resulting box links in the chosen neighbourhood. The full Wilson law is gauge invariant, including under these gauges extended by \(1\) outside the box. The resulting lower bound depends only on the fixed box and the chosen neighbourhood.

**PROVED.** On this event map \(U_e\mapsto V_eU_e\) on the changed bonds, keeping all other links fixed. This bijection preserves product Haar. By continuity on the fixed finite set of affected faces, a sufficiently small initial neighbourhood ensures that the final field belongs to \(A_\theta\) and that the total increase of its dimensionless action is at most \(D_\theta+\theta^2/2+\epsilon\). All other face terms cancel exactly. Changing variables in the normalized Wilson integral proves (5). Taking the time period to infinity at each fixed spatial cube gives the same bound for \(\nu(A_\theta)\). For example one may insert a continuous test supported inside \(A_\theta\) equal to one on the transformed neighbourhood, using a smaller neighbourhood to retain the strict margin. Row 1215 gives a four-link bound uniform even in a prescribed exterior, with cost \(1+20(1-\cos(\pi/8))\) at the sign wall. Equation (5) uses the homogeneous law and allows the deformation to extend in all four directions. [Row 1215, (26)](gap-solve23-astra62.md)

## A counterexample to the proposed lower bound for the specified chain

**PROVED.** On even cubes of side \(n\to\infty\), take \(a=L/n\), \(0<L<\infty\) fixed, and assume the bare schedule \(\beta/\log n\to b>0\). Use exactly the cap and constant-probability base flags of row 1298, (29)–(32). Let \(G_d\) be its (36), with \(d=\lceil(K_0\log n)^{1/3}\rceil\). For fixed \(\theta\in(\pi/2,\pi)\), fixed \(\epsilon>0\), the \(B\) of (36) sufficiently large, and every fixed \(K_0\) sufficiently large in terms of these constants and \(b\), the gap \(\gamma_d\) of the chain restricted by rejection to \(G_d\), tested on gauge-invariant functions, obeys
\[
 \gamma_d \le C_{\theta,\epsilon}(1+\beta)^{15/2}
          \exp[-\beta(4-\tfrac12\theta^2-\epsilon)] .             \tag{6}
\]
The same inequality holds without the rejection. To prove it, use row 1298, (36) on the vacuum, which gives \(\nu(G_d^c)\le 3n^3e^{-cd^3}\). It also follows by applying the marked-plaquette moment of row 1155, (9) and Markov's inequality to each cube and orientation. Choose \(K_0\) to make this error smaller than half the lower bound in (5) for all large \(n\), using \(\beta/\log n\to b\). Hence \(s=\nu(A_\theta\cap G_d)\) is bounded below by half of (5). Also \(\nu(A_\theta)\le z_\beta^{-1}e^{-\beta D_\theta}\to0\) by one deletion. The outgoing flux of the restricted chain is at most (3) divided by \(\nu(G_d)\), while the variance of its indicator is \(s(1-s/\nu(G_d))/\nu(G_d)\). The ratio proves (6). Without rejection use \(s=\nu(A_\theta)\) directly. The indicator is a gauge-invariant, spatial-centre-neutral function of the original links.

**PROVED.** At the one-loop slope \(b_*=11/(3\pi^2)\) used in the previous rows, one can fix \(\theta>\pi/2\) and \(\epsilon>0\) so that \(4-\theta^2/2-\epsilon>1/b_*\). At the endpoint the strict inequality amounts to \(35\pi^2<352\), which follows from \(\pi^2<10\). First move \(\theta\) slightly right, then choose the slack. The logarithm of (6) divided by \(\log n\) has upper limit strictly less than \(-1\). In particular
\[
                         \gamma_d/a\longrightarrow0 .             \tag{7}
\]
This disproves the proposed uniform lower estimate for the concrete corrected kernel, on the stated schedule and with sufficiently large fixed \(K_0\). Inequality (37) of row 1298 remains a valid implication. Its premise can depend on the resampling kernel. Equation (7) gives no upper bound on the physical energy gap because the comparison (29) has the opposite direction. [Kernel, truncation and implication](gap-solve34-astra62.md) · [Previous free-mode test](gap-mini-solve-ax-opus.md)

**PROVED.** The same localized event has very little *physical* low-energy spectral weight. On the physical slice let \(P\) be the vacuum-normalized Wilson transfer in \(L^2(\nu)\). Put \(q=z_\beta^{-1}e^{-\beta D_\theta}\). Mark \(A_\theta\) on every other time slice of a \(2l\)-periodic cylinder. The marked faces share a spatial direction, so the \(l\)-fold probability is at most \(q^l\) by (1) with \(l\) marks. In transfer language this is
\[
 \operatorname{Tr}[(\mathbf1_{A_\theta}P^2\mathbf1_{A_\theta})^l]
                  \le q^l\operatorname{Tr}P^{2l}.
\]
The indicator inside the trace denotes multiplication. At fixed grid the positive transfer is compact, \(\operatorname{Tr}(P^2)<\infty\), and its simple top eigenvalue is one. Taking \(l\)-th roots gives the operator norm bound \(\|P\mathbf1_{A_\theta}\|_{\mathrm{op}}^2\le q\) on the physical space. For \(S=A_\theta\) or \(S=A_\theta\cap G_d\), put \(v_S=(\mathbf1_S-\nu(S))/\sqrt{\nu(S)(1-\nu(S))}\). Since \(P1=1\),
\[
 \|P v_S\|^2=
 \frac{\|P\mathbf1_S\|_{L^2(\nu)}^2-\nu(S)^2}{\nu(S)(1-\nu(S))}
 \le \frac{q}{1-\nu(S)} .
                                                                    \tag{8}
\]
Consequently the squared projection of \(v_S\) to any fixed physical energy band \([0,E]\) is at most \(e^{2aE}q/(1-\nu(S))\to0\), although its corresponding rejection-chain test gave (7). This uses the repeated-mark method of rows 1290 and 1298. [Marked transfer argument](gap-solve33-astra62.md) · [Band projection estimates](gap-solve34-astra62.md)

## How many plaquette readings give the same obstruction?

**PROVED.** The field used in (5) can cross the chosen threshold on \(p\) alone. For \(q\ne p\), \(|J_{qp}|<1/2\). Indeed equality in Cauchy–Schwarz between \(J\delta_p\) and \(J\delta_q\) would make the two projected vectors collinear. Pairing both against the curl of the unit cochain on an edge of \(p\) outside \(q\) gives \(\pm1\) and zero. The squared summability of \(J\delta_p\) then gives \(s_*=\sup_{q\ne p}2|J_{qp}|<1\). Choose \(\alpha>\theta\) so close to \(\theta\) that \(s_*\alpha<\theta\), as well as meeting the cost slack in (5). Norm approximation in (4) controls every individual coefficient. We may therefore arrange \(\sup_{q\ne p}|(du)_q|<\theta\). Shrink the starting neighbourhood in (5) so that on it none of the affected faces is marked, and in its image precisely \(p\) is marked. This includes every affected face of the original configuration because the chosen finite box contains all its edges. Unaffected readings agree before and after insertion.

**PROVED.** Let \(\mathcal P\) denote all \(M=3n^3\) positive spatial plaquettes of the middle slice. Write \(Y_p=\mathbf1_{\{w_p<\cos\theta\}}\), \(F_c=\sum_{p\in\mathcal P}c_pY_p\), \(I_\theta=D_\theta+\theta^2/2\). For every fixed \(\epsilon>0\),
\[
 \operatorname{Var}_\nu F_c\ \ge\
      c_{\theta,\epsilon}e^{-(I_\theta+\epsilon)\beta}
                        \sum_{p\in\mathcal P}|c_p|^2 .              \tag{9}
\]
Here and below the constants do not grow with \(n\) or the time period. To verify the variance bound before the vacuum limit, place a translated and coordinate-permuted copy of the construction at each \(p\). Partition these copies into \(J_0\) families so that within a family no four-dimensional face meets changed bonds from two copies. For example join two copies when the closures of their fixed boxes meet within distance two and greedily colour the resulting graph using one more than its bounded degree. Choose a family carrying at least \(1/J_0\) of \(\sum|c_p|^2\). Condition on all bonds outside its changed bond sets. The Wilson density factors across the sets since every action term sees at most one. Each summand in \(F_c\) also sees at most one. The conditional variance is the sum of the variances of its local contributions.

**PROVED.** For one such contribution \(F^{(p)}\) and any function \(m\) of the exterior, integrate \(|F^{(p)}-m|^2\) on the starting event \(E_p\) of (5) and its disjoint image. The change of variables preserves the exterior. On the image the contribution changes by \(c_p\), and the weight relative to the starting configuration is at least \(r=\exp[-(I_\theta+\epsilon)\beta]\). The two integrals together are at least
\[
 \int_{E_p}\!\left(|F^{(p)}-m|^2+r|F^{(p)}+c_p-m|^2\right)d\mu
 \ \ge\ \frac r{1+r}|c_p|^2\,\mu(E_p).
\]
Use the conditional mean for \(m\). The unconditional bound \(\mu(E_p)\ge c_{\theta,\epsilon}>0\) was obtained by gauge averaging on a fixed nearly flat box in the proof of (5). Sum and use the law of total variance. At fixed spatial grid, bounded gauge-invariant slice readings converge in the finite-time trace to the vacuum expectation by the simple top eigenvalue (equivalently apply trace convergence with bounded multiplication insertions). This proves (9).

**PROVED.** For the original six-colour \(K\) one simultaneously has
\[
 \langle F_c,(1-K)F_c\rangle_\nu
 \ \le\ C(1+\beta)^{15/2}e^{-(4+D_\theta)\beta}
                      \sum_{p\in\mathcal P}|c_p|^2 .                \tag{10}
\]
Given the flag kinds and the values retained in row 1298, the old and new flagged spins are independent product draws with the indicated densities. Each plaquette depends on at most one active spin. Thus the conditional variance of \(F_c\) groups into a sum over flagged edges. At a cap flag all its incident \(Y_p\) vanish on the cap. At a base flag the variance of the sum of its at most four terms is at most four times \(\sum_{p\ni e}|c_p|^2\rho_h(Y_p)\), by Cauchy–Schwarz on the centred terms. Average as in (2)–(3), then sum the incidences. This proves (10) without a factor \(M\).

**PROVED.** With \(K_0\) sufficiently large, (9) and (10) give the bound (6) on the Rayleigh quotient of *every* nonzero centred \(F_c\) in the restricted chain. Indeed, replacing \(\nu\) by \(\nu(\cdot\mid G_d)\) in (9) loses at most \(C M\nu(G_d^c)\sum|c_p|^2\) before division by \(\nu(G_d)\). To see this, first centre in \(\nu\), use \(\|F_c-\nu F_c\|_\infty\le\sqrt M\,\|c\|_2\), and subtract the squared conditional mean on \(G_d\) using Cauchy–Schwarz on \(G_d^c\). Choose \(K_0\) so this loss is \(o(e^{-(I_\theta+\epsilon)\beta})\), possible since \(M=3n^3\). Restriction only lowers the unnormalized jump form. These give an \(M\)-dimensional space of tests with auxiliary Dirichlet quotient \(o(a)\) on the schedule of (7). Taking all coefficients equal gives a translation-invariant, cubic-rotation-invariant, centre-neutral scalar test. Projecting onto these symmetries therefore preserves the obstruction.

## What the true transfer does on this space

**PROVED.** The single-face upper bound can be improved by charging neighbouring faces. On a four-dimensional rectangular torus with periods at least four, let \(p\) have directions \(i,j\). There are four elementary three-cubes containing \(p\), one on each side in each of the other two directions. Their remaining five-face sets are disjoint. In each cube the other five faces form a disk with boundary \(\partial p\). Peeling its squares writes the boundary product as a product of conjugated, possibly inverted face products. Equivalently, remove the face opposite \(p\) last after attaching the four side faces to it, cancelling each shared edge in the boundary word. Bi-invariance of quaternion chord distance gives \(|1-U_p|\le\sum_{q\ne p}|1-U_q|\). Squaring and using \(D_q=|1-U_q|^2/2\) gives \(D_p\le5\sum_{q\ne p}D_q\). This is the five-face estimate of row 1151. Take \(S_i,S_j\) to be the faces of this union containing \(i,j\), respectively. Each has 13 faces, including \(p\). Their half-weighted sum pays all of \(D_p\) and at least half of the remaining deficits, hence at least \(7D_p/5\). Cauchy–Schwarz and the common-direction deletion bound (1) now give
\[
             \nu(Y_p)\le z_\beta^{-13} e^{-7\beta D_\theta/5}.     \tag{11}
\]
This holds in the finite-time measures and their vacuum limit. [Five-face estimate](gap-solve5-astra62.md)

**PROVED.** In the unrestricted vacuum space let \(W\) be the span of the centred \(Y_p\), and \(\Pi_W\) its orthogonal projection. For \(\theta\) sufficiently close to \(\pi/2\) from above and sufficiently small fixed \(\epsilon>0\),
\[
 \frac1M\operatorname{Tr}(\Pi_W P^2\Pi_W)
 \le C_{\theta,\epsilon}(1+\beta)^{21}
       \exp[-\beta(7D_\theta/5-\theta^2/2-\epsilon)]
 =:\delta_\beta \ \longrightarrow 0.                              \tag{12}
\]
In fact write \(V c=F_c-\nu F_c\). By (9), \(G=V^*V\ge c_{\theta,\epsilon} e^{-(I_\theta+\epsilon)\beta}I\). The columns of \(VG^{-1/2}\) form an orthonormal basis of \(W\). The squared norm after applying \(P\) to each original column \(Ve_p\) is at most \(q\,\nu(Y_p)\) by the multiplication-operator estimate preceding (8). Taking the trace and using \(G^{-1}\le c_{\theta,\epsilon}^{-1}e^{(I_\theta+\epsilon)\beta}I\) proves (12) by (11). At \(\theta=\pi/2\) the exponent before slack is \(7/5-\pi^2/8>0\). The choice of \(\theta,\epsilon\) can meet this and (7) simultaneously.

**PROVED.** At most \(M\sqrt{\delta_\beta}\) eigenvalues of the positive compression \(\Pi_WP^2\Pi_W|_W\) exceed \(\sqrt{\delta_\beta}\). On their orthogonal complement in \(W\), every unit vector has squared projection onto physical energies \([0,E]\) at most \(e^{2aE}\sqrt{\delta_\beta}\). Thus a fraction tending to one of the dimensions in (9) has uniformly vanishing physical low-energy weight. All their auxiliary Dirichlet quotients are \(o(a)\). The zero-momentum scalar sum could lie in the exceptional subspace of this trace estimate.

## A local change tested against arbitrary physical states

**PROVED.** Let \(\mu\) be the ordinary stationary Wilson spacetime law in a finite spatial cube with unbounded time. For a fixed insertion used in (5), let \(t_*\) be a positive integer beyond its entire time support. Let \(X_t\) be the spatial slice and \(E_p\) its starting event. For every gauge-invariant \(f\in L^2(\nu)\),
\[
 \int_{E_p}|f((VU)_0)-f(X_0)|^2\,d\mu(U)
 \ \le\ 2t_*(1+r^{-1})\,\langle f,(1-P)f\rangle_\nu,\qquad
 r=e^{-(I_\theta+\epsilon)\beta}.                                \tag{13}
\]
Indeed integrate \(|f(X_0)-f(X_{t_*})|^2\) on \(E_p\) and its image, as in (9). The prediction at \(t_*\) is identical for the paired fields. The same two-square inequality gives the left side times \(r/(1+r)\). The unrestricted integral is \(2\langle f,(1-P^{t_*})f\rangle_\nu\le2t_*\langle f,(1-P)f\rangle_\nu\). The argument can first be made on a long periodic torus for bounded \(f\), then passed to the stationary slab. For raw link coordinates one obtains its law by undoing temporal gauge with independent Haar vertex frames inside the slab, by the Haar change of variables that fixes temporal links on this open time interval. Equivalently its local conditional density relative to product Haar, given the exterior bonds, has the original incident plaquette weights. Truncation extends the inequality by Fatou, since the finite change on \(E_p\) has bounded Radon–Nikodym ratio for each fixed \(\beta\).

**PROVED.** The right side of (13) tends to zero uniformly on unit vectors at physical energy at most any fixed \(E\), for the same choice of \(\theta\) with sufficiently small slack. Indeed \(I_{\pi/2}=1+\pi^2/8<3\pi^2/11=1/b_*\), since \(13\pi^2>88\). Thus \(a e^{(I_\theta+\epsilon)\beta}\to0\), while \(1-P\le1-e^{-aE}\) on this band. The original Wilson measure can therefore compare amplitudes on opposite sides of the plaquette threshold within these finite patches. The constant-probability base flag in (3) loses this comparison.

**ARGUED.** Scaling this insertion to a physical box requires control of its cost in the actual surrounding field. The probability lower bound for the near-identity starting neighbourhood in (5) was at fixed diameter. For a cube of side \(R\) one can choose \(cR^4\) separated four-edge blocks. Conditional on the other edges, row 1215, (26) gives each root face probability at least \(p_\beta=c_\epsilon e^{-(E_*+\epsilon)\beta}\) of negative trace, \(E_*=1+20(1-\cos(\pi/8))\). The blocks are then independent. Any box gauge in which every edge is within angle \(\pi/9\) of \(1\) has positive trace on every plaquette by the triangle inequality. The probability that such a gauge exists is at most \((1-p_\beta)^{cR^4}\). This vanishes at \(R\) proportional to \(n\) on the specified schedule, using \(b_*E_*<1\) from that row. Thus the fixed-patch argument supplies no physical-size starting event of comparable probability. The earlier exact gauge average for a deterministic left multiplication in a fixed frame likewise charges the squared link angles on a growing box. [Four-edge bound](gap-solve23-astra62.md) · [Fixed-frame formula (2.2)](gap-laptop-solve2-fable.md)

## Resampling directly from the Wilson bridge

**GUIDE.** To try to recover a gap estimate, remove the artificial base flag. Keep two successive neighbours \(U,Y\) of a central slice \(X\), together with \(Z=X_{J^c}\) for a prescribed set \(J\) of \(k\) spatial links. Resample the missing variables from their true conditional law. This gives a reversible operator \(R_J\) on \(L^2(\nu)\). Its Dirichlet form is the mean conditional variance given \(Z,U,Y\). I compare it with the true one-slice conditional variance given \(Z\). Row 1298, (9) uses a related comparison when predicting from one neighbour. [Three-slice law](gap-solve34-astra62.md)

**PROVED.** Suppose \(p,q\) are positive probability densities and the maximum-to-minimum ratio of \(p/q\) is at most \(D\ge1\), using essential bounds. Their two independent observations satisfy
\[
 \int \min(p\otimes p,q\otimes q)\ \ge\ \tfrac14D^{-2/3}.         \tag{14}
\]
For \(D=1\) the overlap equals one. Otherwise let \(l,u\) bound \(R=p/q\), with \(l\le1\le u\) and \(u/l\le D\). The case \(l=u\) gives identical laws. Under \(q\) one has \(\mathbb E R=1\). In \(\mathbb E\min(1,R_1R_2)\) the integrand is concave in each variable separately. Replacing each \(R_i\) independently by an endpoint variable on \(\{l,u\}\) of the same mean gives a lower bound, by the chord inequality twice. In this binary experiment put \(x=q(R=u)\), \(y=p(R=l)\). Then \(x+y\le1\) and \((1-x)(1-y)/(xy)=u/l\) in the nondegenerate case. On two draws the contributions of the two equal outcomes are \(x^2\) and \(y^2\). The two mixed outcomes add \(2\min(x(1-x),y(1-y))\). If \(\max(x,y)\ge1/2\), the sum is at least \(1/4\). Otherwise \(xy\ge1/(4D)\) and the mixed term is at least \(\min(x,y)\). The larger of \(\max(x,y)^2\) and \(\min(x,y)\) is at least \((xy)^{2/3}\). This proves (14). Endpoint variables of zero probability reduce to the identical-law case.

**PROVED.** The exponent \(2/3\) is sharp for this general overlap question. Set \(x=t^2,y=t\) with \(0<t<1/2\). The likelihood range ratio is \((1-t^2)(1-t)/t^3\), and the displayed sum for the overlap is of order \(t^2\) as \(t\downarrow0\). This example concerns arbitrary repeated observations.

**PROVED.** In the original finite Wilson vacuum, for arbitrary \(k\ge1\),
\[
 \tfrac14e^{-8k\beta/3}\mathbb E\operatorname{Var}(f(X)\mid Z)
 \ \le\ \langle f,(1-R_J)f\rangle_\nu
 \ \le\ 2\langle f,(1-P)f\rangle_\nu .                            \tag{15}
\]
At fixed \(z\), the law of one neighbour given \(X_J=s\) has density \(b_z(u)\exp(\beta\sum_{e\in J}s_e\cdot u_e)\) divided by its integral. This follows from the magnetic-sandwich Wilson kernel and its vacuum transform. Everything depending only on the starting point cancels in normalization. For \(s,s'\), the log likelihood ratio oscillates in \(u\) by at most \(2\beta\sum_e|s_e-s'_e|\le4k\beta\). Reversibility and the Markov property give two conditionally independent neighbours with that same law. Thus by (14) the overlap for the pair is at least \(\delta=e^{-8k\beta/3}/4\), uniformly in \(z,s,s'\). Drawing a new \(s''\) from the posterior given the pair is a further Markov kernel, so its two rows also have overlap at least \(\delta\). The resulting operator on the fibre contracts oscillations by \(1-\delta\). It is self-adjoint and positive by the conditional resampling identity. At fixed grid its continuous kernel on the compact fibre is bounded relative to its strictly positive stationary density. It is compact and takes every nonzero-eigenvalue eigenfunction to a continuous representative. Applying the oscillation bound to each nonconstant real eigenfunction proves the left inequality. Integration over \(z\) completes it. For the right inequality use \(f(U)\) as predictor given the exposed data.

**PROVED.** For \(k=1\) at \(b_*\) the factor \(e^{-8\beta/3}\) is asymptotically larger than \(a\), since \(88<9\pi^2\) (for example \(\pi>223/71\)). Hence the full two-neighbour update detects, on the physical scale, any test whose single-link conditional variance is a fixed fraction of its vacuum variance. In the specific test \(Y_p\), one can also update the four edges of \(p\) together in the exact bridge. Given its entire exterior and both ends, row 1215, (26) puts probability at least \(p_\beta=c_\epsilon e^{-(E_*+\epsilon)\beta}\) on positive trace, uniformly. Conditional variance of \(Y_p\) is therefore at least \(p_\beta\) times its conditional mean. Averaging gives a redraw form at least \(p_\beta\nu(Y_p)\). A bounded number of colours of separated four-edge squares covers all spatial plaquettes, by colouring their bounded-degree conflict graph. Simultaneously redrawing the squares of a uniform colour from their exact conditional law preserves \(\nu\). The colour containing a given \(p\) has the preceding lower bound for \(Y_p\), since its four-bond blocks are conditionally independent. Thus its indicator has Dirichlet quotient at least \(p_\beta\) divided by the number of colours. This exceeds order \(a\) on the specified schedule and repairs the individual test that exposed (7). [Four-link conditional probability](gap-solve23-astra62.md)

**OPEN.** For a collective test the conditioning in (15) can remove nearly all its variance. Taking \(J\) to be macroscopic in (15) pays an exponential in \(k\beta\). Resampling many disjoint squares together leaves their common exterior in both observations. An estimate on the *variance of the conditional means across those exteriors* is still needed. Even exact product laws within a fixed exterior do not bound that term in the law of total variance. Row 1298, (11)–(14) already exhibits the role of correlations in the exterior weights. Row 1211, (8)–(10) already recovers bounded-energy information from the walls of thin slabs. Neither argument supplies decay between the surviving collective readings at a fixed physical separation. [Exterior weights](gap-solve34-astra62.md) · [Thin-slab walls](gap-solve22-astra62.md)

## Excursions of the physical transfer

**PROVED.** There is a way to remove prescribed rare faces at relative accuracy at the lower spectral edge. Take \(k\) prescribed spatial plaquettes, put \(B=\{\text{at least one of these }Y_p=1\}\), and write \(G=B^c\). In this paragraph letters \(G,B\) as operator subscripts denote multiplication by their indicators. On the gauge-invariant space (8) implies
\[
 \|\mathbf1_B P\|^2\le kq,\qquad q=z_\beta^{-1}e^{-\beta D_\theta},
                                                                    \tag{16}
\]
by summing \(\|\mathbf1_{A_p}Pf\|^2\) for the prescribed faces. Put \(\eta=\sqrt{kq}<1\). At every finite grid define the first-return kernel on \(G\) by
\[
 T_G=P_{GG}+P_{GB}(1-P_{BB})^{-1}P_{BG}.
\]
The terms of the inverse sum paths spending successively more steps in \(B\) before their first return. They are nonnegative kernels. Since \(P1=1\), \((1-P_{BB})1_B=P_{BG}1_G\), hence \(T_G1_G=1_G\). It is reversible in \(\nu(\cdot\mid G)\). Every displayed norm bound below is on gauge-invariant functions.

**PROVED.** Let \(d_P,d_G\) denote the centred Dirichlet gaps of \(P,T_G\), respectively, per step of each kernel. Then
\[
 (1-\eta)^2\min(d_G,1-\eta)\ \le\ d_P\ \le\ d_G .                \tag{17}
\]
Use the original unnormalized restrictions of \(\nu\) on \(G,B\) for block inner products, and put \(A=1-P_{BB}\ge(1-\eta)I\), \(H=A^{-1}P_{BG}\). One has \(\|H\|\le\eta/(1-\eta)\) and \(H1_G=1_B\). Writing the full field reading as \(f=(g,Hg+h)\), direct expansion gives
\[
 \langle f,(1-P)f\rangle
  =\langle g,(1-T_G)g\rangle_G+\langle h,Ah\rangle_B .
\]
The norm of the map \((g,h)\mapsto(g,Hg+h)\) is at most \(1+\|H\|\le(1-\eta)^{-1}\). Taking the infimum over constant shifts bounds \(\operatorname{Var}_\nu f\) from above by \((1-\eta)^{-2}(\inf_c\|g-c\|_G^2+\|h\|_B^2)\). This proves the lower bound in (17). For the upper bound set \(h=0\) and use \(\operatorname{Var}_\nu f\ge\inf_c\|g-c\|_G^2\). This argument uses the true return through the discarded configurations. It accounts for arbitrarily small positive gaps without subtracting an absolute error of order \(kq\).

**PROVED.** For fixed \(0<\zeta<D_\theta\) one may take \(k\le e^{(D_\theta-\zeta)\beta}\). Now \(\eta\le C(1+\beta)^{3/4}e^{-\zeta\beta/2}\). Replacing the inverse in \(T_G\) by \(\sum_{j=0}^{l-1}P_{BB}^j\) costs at most \(\eta^{l+2}/(1-\eta)\) in operator norm. At \(\beta/\log n\to b>0\), any fixed integer \(l\ge1\) with \((l+2)b\zeta/2>1\) makes this \(o(a)\) on a fixed physical cube. Thus a finite number of excursion lengths suffices when testing a bound of order \(a\) on the centred form of this reduced transfer. Its physical-scale Dirichlet gap still has to be estimated.

**PROVED.** Removing the rough faces *wherever* they occur would make a very different return problem. For \(\theta\) sufficiently close to \(\pi/2\) from above, the probability of finding no \(Y_p=1\) on the entire spatial slice tends to zero on the stated schedule. Here is the extension from the sign threshold in row 1215 to the fixed threshold used in (6). At each four-edge conditional exterior, the construction in row 1215, (26) reaches a traceless plaquette with loss at most \(E_*=1+20(1-\cos(\pi/8))\) from the maximal local score. Change a single edge through angle \(\theta-\pi/2+\xi\) to give the plaquette angle \(\theta+\xi<\pi\). This costs at most \(6(\theta-\pi/2+\xi)\) in score, since each incident trace is 1-Lipschitz. A sufficiently small fixed product of Haar balls about these four edges preserves the strict threshold, with an arbitrarily small further score loss. Dividing its integral by the maximum-density bound for the conditional normalizer gives, uniformly over exteriors,
\[
 p_{\beta,\theta}=c_{\epsilon,\theta}
     e^{-\beta(E_*+6(\theta-\pi/2)+\epsilon)}
     \ \le\ \Pr(Y_p=1\mid\text{all bonds off its four edges}).    \tag{18}
\]
Choose \(\theta,\epsilon\) so the exponent coefficient times \(b_*\) is below one, possible by row 1215. On a spatial slice choose at least \(c n^3\) four-edge sets with no common incident action face between sets. Conditional on the rest their laws are independent, even in a four-torus with arbitrarily long time period. The no-mark probability is at most \((1-p_{\beta,\theta})^{c n^3}\to0\), uniformly in the time period, so the bound passes to the vacuum. For the union over the full slice, \(\|\mathbf1_B P\|\ge\|\mathbf1_B P1\|=\sqrt{\nu(B)}\to1\). Thus the small return correction in (16) cannot be extended to that union. This also shows why (8) for every individual face leaves a genuinely collective problem. [Uniform four-edge insertion](gap-solve23-astra62.md)

## What a single-link test misses

**PROVED.** In the actual vacuum the single-link estimates cannot be summed by taking the best link for each test. Set \(F=\sum_{p\in\mathcal P}Y_p\). Changing one link changes \(F\) by at most four, so \(\mathbb E\operatorname{Var}(F\mid X_{e^c})\le16\) for every \(e\). From (9) and \(b_*(I_\theta+\epsilon)<1\),
\[
 \max_e\frac{\mathbb E\operatorname{Var}(F\mid X_{e^c})}
                   {\operatorname{Var}_\nu(F)}
       \ \le\ C n^{-3}e^{(I_\theta+\epsilon)\beta}
       \ =\ o(n^{-2}).                                             \tag{19}
\]
Here \(X_{e^c}\) means all spatial links other than \(e\). This testing failure holds for a scalar invariant under translations and the cubic group. Its physical energy cannot be read from (19).

## Changing the rejection set

**PROVED.** The counterexample survives *every* gauge-invariant rejection set \(G_n\) with \(\nu(G_n)\to1\), including choices for which the elementary union estimate following (6) is too weak. Use the scalar \(F=\sum_{p\in\mathcal P}Y_p\). For the \(\theta,\epsilon\) used in (7) and (13), set \(r_\beta=\exp[-(I_\theta+\epsilon)\beta]\). There are fixed \(c_1,c_2>0\) such that, along the stated schedule, for all large even \(n\),
\[
 \inf_{m\in\mathbb R}\ \nu\bigl(|F-m|\ge c_1\sqrt{M r_\beta}\bigr)
                 \ \ge\ c_2,\qquad M=3n^3.                        \tag{20}
\]
This gives information beyond the variance in (9), whose lower bound might otherwise have come entirely from discarded fields.

**PROVED.** Work first on a periodic four-torus with sufficiently long time period. Place disjoint copies of the patch used in (9) about at least \(cM\) spatial faces at time zero. Choose the boxes far enough apart that no action plaquette meets two changed sets. Such a family exists by the bounded-degree colouring used in (9). Shrink the starting neighbourhood \(E_p\) once more so that the total initial deficit of all affected faces is less than \(D_\theta/2\). On \(VE_p\) the new target face alone has deficit at least \(D_\theta\). The ratio of new to old Wilson density is thus between \(r_\beta\) and one, and \(\mu(E_p)\) is still bounded below by a fixed positive constant.

**PROVED.** Condition on the exterior of these changed sets. In each patch record the pair \(\{x,Vx\}\) when \(x\in E_p\), treating the two configurations as the same record. Give every configuration outside \(E_p\cup VE_p\) its own singleton record. Conditional on the exterior and all records, the choices in the two-point records are independent. To verify this conditioning explicitly, use \(x\in E_p\) as the representative of a pair. Haar change of variables on \(VE_p\) gives the two conditional weights proportional to the densities at \(x,Vx\). The unconditioned patch factors multiply given the exterior, so the corresponding binary weights also multiply given the separate records. For each pair the probability of the new choice is between \(r_\beta/(1+r_\beta)\) and \(1/2\). Each such choice raises \(F\) by exactly one by the single-threshold crossing following (8).

**PROVED.** The expected number of two-point records is at least a fixed positive fraction of \(M\), using only the marginal lower bounds on \(\mu(E_p)\). This count is at most \(M\), so with probability bounded below by a positive constant it is at least \(cM\), for a smaller fixed \(c>0\). Given any such records, \(F\) is a constant plus a sum of independent Bernoulli variables with total variance \(v\ge c' M r_\beta\). This tends to infinity since \(b_*(I_\theta+\epsilon)<1\). With \(F'\) an independent draw given the same records and \(D=F-F'\), one has \(\mathbb E[D^2]=2v\) and \(\mathbb E[D^4]\le2v+3(2v)^2\), conditionally. Indeed the independent centred summands have absolute value at most one, so their fourth moments are at most their second moments, and the distinct pairs contribute at most three times the squared total variance. When \(v\ge1\), Cauchy–Schwarz applied to \(D^2\mathbf1_{\{D^2\ge v\}}\) gives \(\Pr(|D|\ge\sqrt v)\ge1/14\). For any \(m\), at least one of \(|F-m|,|F'-m|\) must then exceed or equal \(\sqrt v/2\). Each copy has the same law. Integration over the qualifying records proves (20) on the torus. Its constants hold at every sufficiently long time period, and its single-slice event passes to \(\nu\) at each fixed grid.

**PROVED.** Intersecting the event in (20) with \(G_n\) loses at most \(\nu(G_n^c)\). Taking \(m=\mathbb E_\nu[F\mid G_n]\) gives \(\nu(G_n)\operatorname{Var}_{\nu(\cdot\mid G_n)}F\ge c_3 M r_\beta\). The unnormalized jump form after rejection is at most (10) with all \(c_p=1\). Consequently the Rayleigh quotient of this same scalar in the rejected chain satisfies
\[
 \frac{\langle F,(1-K_{G_n})F\rangle_{\nu(\cdot\mid G_n)}}
      {\operatorname{Var}_{\nu(\cdot\mid G_n)}F}
 \le C_{\theta,\epsilon}(1+\beta)^{15/2}
                   e^{-\beta(4-\theta^2/2-\epsilon)}
 =o(a).                                                           \tag{21}
\]
Here \(K_{G_n}\) holds whenever the original cap/base proposal would leave \(G_n\). This includes every \(G_d\) for which (36) gives \(\nu(G_d)\to1\). The conclusion also holds on the unrestricted slice by taking \(G_n\) equal to the whole space. Equation (8) controls the physical projection of an individual reading, and (12) controls the average over their span.

## Comparing the two dynamics on the scalar sum

**PROVED.** The same separated patches give a direct comparison on the entire span of plaquette readings, including the zero-momentum scalar. Write \(\mathcal E_S(f)=\langle f,(1-S)f\rangle_\nu\) for either of the unrestricted kernels \(S=P,K\). At the same fixed \(\theta,\epsilon\) and sufficiently large grids,
\[
\begin{aligned}
 \mathcal E_P(F_c)&\ge c_{\theta,\epsilon}\,
              e^{-(I_\theta+\epsilon)\beta}\sum_p|c_p|^2,\\
 \mathcal E_K(F_c)&\le C_{\theta,\epsilon}(1+\beta)^{15/2}
              e^{-(4-\theta^2/2-\epsilon)\beta}\,\mathcal E_P(F_c).
\end{aligned}                                                       \tag{22}
\]
In the proof of (9) choose the same family of disjoint boxes carrying a fixed fraction of the coefficient mass. The sum of the expected conditional variances on the changed bond sets was already at least \(c_{\theta,\epsilon}e^{-(I_\theta+\epsilon)\beta}\sum|c_p|^2\). Consequently the same bound applies to the squared error in predicting \(F_c(X_0)\) by *any* function of all bonds outside those sets. Take the predictor \(F_c(X_{t_*})\), with \(t_*\) beyond all the boxes, fixed independently of the coefficients and the torus sides. On taking the infinite-time limit that error is \(2\langle F_c,(1-P^{t_*})F_c\rangle_\nu\le 2t_*\mathcal E_P(F_c)\). This proves the first inequality. Divide the bound (10) by the first inequality and use \(I_\theta=D_\theta+\theta^2/2\) to obtain the second.

**PROVED.** The multiplier of \(\mathcal E_P(F_c)\) in (22) is \(o(a)\) on the schedule of (7), also for the scalar sum itself.

**OPEN.** A physical spectral estimate for the sum would require control of its vacuum variance relative to \(\mathcal E_P(F_c)\), including covariances between distant plaquettes. Equations (9) and (20) give lower bounds on that variance.

## The remaining physical estimate

**OPEN.** One precise residual is to prove \(d_G\ge c a\), with one \(c>0\) uniform in the spatial volumes and sufficiently fine cutoffs required for a nontrivial continuum Wilson limit, for the *true* return kernel in (17). One may fix a single marked face independently of the volume, or at fixed physical side choose any prescribed collection satisfying \(kq\to0\) in (16). If the physical-scale estimate holds, (17) bounds \(d_P/a\) below. On centred states the operator for \(\lfloor t/a\rfloor\) steps then has norm at most \((1-d_P)^{\lfloor t/a\rfloor}\). In a matched vacuum representation with convergence on a dense generating family, this gives exponential decay and excludes spectrum below the resulting rate on the vacuum complement. The variance bound on one patch, the rare-event estimates on a collection of patches and the conditional laws inside them have not bounded the return operator on its full centred space. A nontrivial continuum construction with the full Yang–Mills observables is a separate outstanding premise. The conclusions above are author-side mathematical arguments at the stated lattice parameters. They have no independent check and grant no status.

RESULT — OPEN. The four-dimensional SU(2) Jaffe–Witten mass gap remains unproved. PROVED. On the stated bare schedule the cap/base chain of row 1298 has gap \(o(a)\) on every gauge-invariant restriction of vacuum probability tending to one, by (21). The true transfer suppresses each individual plaquette test at bounded physical energy by (8).
