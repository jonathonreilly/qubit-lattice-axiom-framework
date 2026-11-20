## Repo search

**GUIDE.** FINISH row 1272, based on commit `87d42ebf1`. The objective is a nontrivial four-dimensional continuum SU(2) Yang–Mills theory in the Jaffe–Witten sense and a strictly positive lower bound on the energy above its vacuum. Equation (25) gives a sufficient finite-volume estimate on one grid of cell boundaries. Equations (26)–(29) identify the local curvature observable that survives integration over long tree paths. The outstanding continuum inputs are stated in (33)–(34).

**GUIDE.** The lead's [November 8 search](prior/repo-search-2026-11-08.md), lines 13–36, 395 and 487, covers main and PRs 10114, 10133, 10134 and 10141. Its closest hit, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on PR 10114 at `f76f6c649c`, lines 4–14 and 106–149, gives a positive one-step Wilson loop correlation and a contraction for bare parameter at most \(1/32\). Grok's `MASS_GAP_CROSSOVER_REDUCTION.md` on PR 10133 at `89faef229f`, lines 77–86, lists source transport and the crossover estimate as open. PR 10134 at `1e70c7211a`, `mass-gap-interface.md`, I1–I5, distinguishes a nonzero excitation from a positive lower edge and from Yang–Mills identification. PR 10141 at `a2f6a430e2`, `research/ym4d/library/fp1.md`, lines 299–315, controls a classical constrained form. I checked these passages and main at `8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md`, Theorem ZD-c. That theorem relates the desired thermal seed to cube energies and a doubling defect while leaving their Wilson estimates as premises.

**GUIDE.** Credit for the outline and complete account at `31a47c543775` belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Index chunk 01](sa-index/chunk-01.md), [chunk 29](sa-index/chunk-29.md) and [obligations](sa-index/obligations.md) lead to outline lines 581–599 and 31858–31882. Those passages separate the scalar cyclic space, full gauge-observable identification and exclusion of spectral support near zero. CA-I lines 2704–2712 and 3213–3222 explicitly delimit their assertion. The [4.12–4.19 index](sa-index/ca-4.12-4.19/README.md) concerns ultraviolet induction. [Original outline, spectral obligations](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [Complete account I, scope of the theorem](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** The [row 1218 reading](prior/gap-onebound-read-sol.md) credits Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy for a conditional ascent from thermal traces on a window of shapes. The first four authors also obtain a cube relaxation bound for a law of straight path products in a restricted weak-coupling regime. The fine-field comparison is open. Zeng Chunping formulates a common physical correlation rate and a conditional tunnelling route. I use this reading for the scope of those proposals. [Row 1186](gap-solve19-astra62.md), (27), quantizes two entire slices to bound the loss of mutual information. [Row 1192](gap-solve20-astra62.md), §§1–2, approximates Wilson integrals by positive finite sums. [Row 1222](gap-solve24-astra62.md), (1)–(2), integrates cell interiors given their walls. [Row 1254](gap-solve29-astra62.md), (33), (36), treats the overlap of slow modes with specified observations. [Row 1262](gap-solve30-astra62.md), (14)–(17), (35), leaves an interior conditional-variance inequality on a box of physical size open. These are research inputs. There is no target-specific prior file at this pin. I found no assignment of the conditional law inside individual quaternion bins in the [registry](open-registry.md).

## Choice of attack

**GUIDE.** I keep the exact Wilson measure and observe one finite-valued label on each fine link. The proposed angular resolution is \(c(1+\beta)^{-1/2}\), independent of the size of the torus. The first question is whether the fluctuations left after observing all labels can carry physical correlations. The second is whether the law of the labels admits a volume-uniform estimate on a fixed physical length. A solution also requires a nontrivial matched continuum theory on the full physical local algebra.

## Relaxation with the angular labels held fixed

**PROVED.** Let \(\Lambda=(\mathbb Z/N)^4\), \(N\ge4\), carry one \(SU(2)\) matrix per positive link, probability Haar reference and Wilson weight \(\exp(\beta\sum_p w(U_p))\), where \(w=\tfrac12\operatorname{tr}\) and \(\beta\ge0\). Join distinct links \(i,j\) in a graph if they occur on a common plaquette. Let \(m_{ij}\) count those plaquettes. Then \(m_{ij}=m_{ji}\) and \(\sum_jm_{ij}=18\). Use the Euclidean chord distance on unit quaternions. Partition \(SU(2)\) into Borel cells of diameter at most
\[
                 \delta=\frac1{5\sqrt{1+\beta}} .
\]
There is such a partition with at most \(C(1+\beta)^{3/2}\) cells, equivariant under inversion up to Haar null sets. Indeed divide each coordinate of \([-1,1]^4\) into \(\lceil4/\delta\rceil\) equal intervals of length \(h\). A cube crossing the unit sphere has diameter \(2h\le\delta\), and lies in the annulus with radii \(1-2h,1+2h\). The volume of the annulus is at most \(Ch\), so at most \(Ch^{-3}\) cubes occur. Reflection of the three imaginary coordinates permutes the cubes off their boundaries. Discard cells of zero surface measure. Changes on boundaries do not affect any Wilson integral. Denote by \(\eta_i\) the cell of link \(i\), by \(\eta\) the whole label field, and by \(\mu_\eta\) the exact conditional Wilson law. Every configuration of positive-measure labels has positive probability.

**PROVED.** For the law with these labels fixed, changing just the value at \(j\) within its cell changes the conditional distribution at \(i\) by total variation at most
\[
            c_{ij}=\tfrac14\beta\delta^2 m_{ij},\qquad
            \sum_j c_{ij}\le 9/50<\rho,\quad \rho=1/5 .                 \tag{1}
\]
For one plaquette the mixed difference, changing both the \(i\) and \(j\) entries, is the real part of an ordered product containing their two quaternion differences. Conjugation handles inverse links, and all the other factors have norm one. The absolute mixed difference is at most \(\delta^2\). For the one-site probability relative to Haar restricted to its cell, the change \(D\) of its log weight therefore has oscillation at most \(\beta m_{ij}\delta^2\). Interpolate by the weight \(\exp(tD)\) for \(0\le t\le1\). The derivative of an event probability is \(\operatorname{Cov}_t(1_A,D)\), of absolute value at most \(\operatorname{osc}(D)\Pr_t(A)(1-\Pr_t(A))\). Integration proves (1), also with further links fixed to exact values. This is the single-site comparison of Dobrushin applied to the Wilson plaquette.

**PROVED.** Here is the boundary estimate used below. In a finite set \(D\) of links with assigned cells, compare two conditionings on its exterior. At each exterior link next to \(D\), suppose its two prescribed values lie in the same assigned cell. Write \(J\) for the set of exterior disagreements. There is a coupling bound for the difference of expectations of any bounded \(f\) supported on \(S\subset D\),
\[
 |\mathbb E_1 f-\mathbb E_2 f|
 \le \sum_{i\in S} d_i(f)\sum_{j\in J} B^D_{ij},\qquad
 B^D=\sum_{k\ge0} (C_{DD})^k C_{D,D^c},\quad C=(c_{ij}),             \tag{2}
\]
where \(d_i\) is the oscillation upon changing coordinate \(i\) only. To prove it, start the two interiors in their respective stationary laws. Update one uniform site at a time by a maximal coupling of its two one-link laws. Such a coupling takes their common minimum density first and then the two residual densities. Telescoping through configurations differing at one coordinate bounds the new disagreement probability at \(i\) by \(\sum_{j\in D}c_{ij}p_j+\sum_{j\in J}c_{ij}\), where \(p_j\) are the previous disagreement probabilities. With \(M=|D|\), random scan gives the coordinatewise recursion with matrix \((1-1/M)I+C_{DD}/M\) and the boundary term divided by \(M\). Its row sums are at most \(1-(1-\rho)/M\). Iterate and take the upper limit. Both marginals remained stationary throughout, so telescoping \(f\) gives (2). The empty interior needs no update. Each row sum of \(B^D\) is at most \(\rho\). More precisely its sum over \(j\in J\) is at most \(\rho^{\operatorname{dist}(i,J)}\). Indeed \(C\) is a substochastic walk, killed with the missing row probability. The series sums probabilities of disjoint first exits into \(J\), which require surviving at least that many steps. Infinite distance gives zero.

**PROVED.** Let \(D_x\) contain all links based in the translated side-\(s\) cube at \(x\), \(1\le s<N\), and let \(\mathcal E_s(f)=s^{-4}\sum_x\mathbb E_\mu\operatorname{Var}(f\mid U_{D_x^c})\). For every square-integrable \(f\), including gauge-invariant functions, one has the volume- and coupling-independent comparison
\[
 (1-\rho)\, \mathbb E_\mu\operatorname{Var}(f\mid\eta)
                 \ \le\ \mathcal E_s(f).                                \tag{3}
\]
To see this, work in one fibre \(\mu_\eta\) and write \(P_x\) for conditional expectation off \(D_x\) there. If \(j\in D_x\), \(d_j(P_x f)=0\). For \(j\notin D_x\), (2), together with the direct change of the exterior argument of \(f\), gives
\[
       d_j(P_x f)\le d_j(f)+\sum_{i\in D_x}B^{D_x}_{ij}d_i(f).
\]
For \(K=N^{-4}\sum_xP_x\), summation in \(j\) gives
\(\sum_j d_j(K f)\le [1-(s/N)^4(1-\rho)]\sum_jd_j(f)\).
Here each \(i\) lies in exactly \(s^4\) cubes. Iteration bounds \(\|K^k(f-\mu_\eta f)\|_2\) by the \(k\)th power of the bracket times \(\sum_jd_j(f)\) for any bounded \(f\). Since \(K\) is an average of orthogonal projections, it is self-adjoint and positive. The spectral theorem excludes for this vector every spectral interval strictly above the bracket. Bounded functions are dense, so the exclusion holds on the centered fibre space. Multiplication of \(I-K\) by \((N/s)^4\) gives the asserted gap there. Integration gives the claim because conditioning on the extra inside labels can only decrease the integrated cube variance. This proves (3) for the original measure.

**PROVED.** In particular if \(H_s=s^{-4}\sum_x(I-\mathbb E_\mu[\,\cdot\mid U_{D_x^c}])\), \(M f=\mathbb E_\mu[f\mid\eta]\), and \(g\) has \(H_s\)-spectral support in \([0,\lambda]\), then
\[
           \|(I-M)g\|_2^2\le\lambda(1-\rho)^{-1}\|g\|_2^2 .              \tag{4}
\]
This covers arbitrary normalized rare-event readings. The estimate does not require \(M\) to commute with gauge transformations or with \(H_s\). The energy form for \(M g\) is a further issue because \(M\) need not commute with either operator.

## What the labels retain across a collar

**PROVED.** Write \(S^{[r]}\) for the graph-distance \(r\) neighbourhood of a link set \(S\). Let \(F\) be bounded on \(S\) and \(F_r=\mathbb E_\mu[F\mid\eta_{S^{[r]}}]\), with \(r\ge1\). For every integrable \(G\) measurable off \(S^{[r-1]}\),
\[
       |\mathbb E_\mu[(F-F_r)G]|
        \le 2|S|\,\|F\|_\infty\,\rho^r\,\mathbb E_\mu|G|.              \tag{5}
\]
Condition on the labels of \(S^{[r]}\) and on the actual links off \(S^{[r-1]}\). Only the exact outermost shell values affect the restricted interior law. Two choices of these values consistent with the shell labels differ within their cells. Apply (2) to the interior. The oscillation of the conditional mean is at most \(2|S|\|F\|_\infty\rho^r\), and integration at the given labels gives \(F_r\). Multiplication by the exterior reading and integration prove (5). If the neighbourhood fills the torus before reaching radius \(r\), the absent boundary gives zero error.

**PROVED.** Replacing each of two bounded separated insertions by its label prediction incurs at most \(2(|S_F|+|S_G|)\|F\|_\infty\|G\|_\infty\rho^r\) error in the pairing when their graph distance exceeds \(2r\). Their means are preserved. Apply (5) twice. The same argument telescopes over any fixed number of mutually separated supports. Thus if \(a\downarrow0\) with supports and supremum norms of at most polynomial size in \(1/a\), \(r=\lceil K\log(1/a)\rceil\) makes all these errors tend to zero for sufficiently large \(K\), while \(ar\to0\). Reflection-compatible versions of the predictions exist by uniqueness of conditional expectation, since the label partition is inversion-equivariant. For already matched local sources with positive time padding this preserves their reflected pairings and norms. It also applies to products treated as a single bounded insertion on each side. Matching and totality of the original sources are separate hypotheses. In particular this observation retains every such supplied vector, including nonzero ones.

**PROVED.** A pointwise estimate allows arbitrary normalized functions of the remote exterior. Let \(A=D_x\) be a side-\(s\) cube of bases, \(V\) its concentric enlargement by \(r\ge1\) layers on every face, \(Z=V^c\), and \(B=V\setminus A\). Assume \(2(s+2r)+4\le N\). Condition on all labels outside \(A\). The conditional joint law of the exact \(U_A,U_Z\), relative to the product of its two conditional marginals, has density in \([e^{-h_r},e^{h_r}]\), where
\[
     b_s=4[(s+2)^4-s^4],\qquad h_r=12\beta\delta\, b_s\rho^r .          \tag{6}
\]
These bounds hold uniformly in the prescribed labels.

**PROVED.** For fixed inner and outer values \(u,z\), integrate the pinned-cell Wilson weight over the collar \(B\), calling the result \(J(u,z)\). Factors involving only \(u\) or only \(z\) can be set aside. A plaquette cannot meet both \(A\) and \(Z\). To compare two inner values \(u,u'\), interpolate their inner boundary terms linearly in the exponent. At each interpolation point the mixed differences in two collar entries still satisfy (1), by convexity of that bound. The derivative of the log integral is the conditional mean of the difference \(D\) of the two boundary terms. Its varying collar links have bases in the one-layer enlargement of \(A\), and there are at most \(b_s\) of them. For each, \(d_i(D)\le12\beta\delta\), by the six incident plaquettes and the two inner configurations. Its distance to \(Z\) is at least \(r\), since one graph step moves a base by at most one in the maximum norm. Comparing two outer values \(z,z'\) in the same prescribed cells by (2) and integrating the derivative gives
\[
 \left|\log\frac{J(u,z)J(u',z')}{J(u,z')J(u',z)}\right|\le h_r .
\]
The conditional likelihood ratio for \(z\) at \(u\) and at \(u'\) therefore has log oscillation at most \(h_r\). Normalization bounds it between \(e^{-h_r}\) and \(e^{h_r}\). Average over \(u'\) to compare with the marginal of \(z\). This proves (6), including for events in \(A\) of arbitrarily small positive probability.

## Comparison with the cube dynamics of the exact finite label law

**PROVED.** Let \(\bar\mu\) be the pushforward law of \(\eta\). Use the same cube definition and normalization for its form \(\overline{\mathcal E}_s(h)=s^{-4}\sum_x\mathbb E\operatorname{Var}(h\mid\eta_{D_x^c})\). Write \(v_s,\bar v_s\) for the optimal constants in the Poincaré inequalities of the full and label laws on *all* functions. With \(t=s+2r\) as above and \(\epsilon=e^{h_r}-1\), one has
\[
 \bar v_s\ge v_s,\qquad
 v_t\ \ge\
 \frac{\bigl(\sqrt{\bar v_s}-\epsilon(N/s)^2\bigr)_+^2}
      {\bigl((t/s)^2+\sqrt{\bar v_s/(1-\rho)}\bigr)^2}.                \tag{7}
\]
For the first inequality apply the full law's inequality to \(h(\eta)\) and then condition on fewer exterior variables. For the second let \(A_x=M-\mathbb E[\,\cdot\mid\eta_{D_x^c}]\), an orthogonal projection, and let \(P_V\) condition on the exact exterior of \(V\). Given \(\eta_{D_x^c}\), (6) bounds the change in the expectation of any centered function of \(U_{V^c}\) upon observing \(\eta_{D_x}\) by \(\epsilon\) times its conditional \(L^2\) norm. This follows by subtracting one from the relative density and applying Cauchy–Schwarz. Center the exterior function at its conditional mean before applying the estimate. Integration gives \(\|A_xP_V f\|_2\le\epsilon\|f\|_2\). The complementary term is bounded by \(\|(I-P_V)f\|_2\). The triangle inequality in the direct sum over \(x\) now gives
\[
 \sqrt{\overline{\mathcal E}_s(Mf)}
       \le(t/s)^2\sqrt{\mathcal E_t(f)}+\epsilon(N/s)^2\|f\|_2 .
\]
For centered \(f\), bound \(\|Mf\|_2\) by the label Poincaré inequality and bound \(\|(I-M)f\|_2\) by (3) at side \(t\). Using \(\|f\|_2\le\|Mf\|_2+\|(I-M)f\|_2\) proves (7), with the zero-gap case following by positivity.

**PROVED, from [row 1254](gap-solve29-astra62.md), (8).** The use of all functions in (7) has the following uniform gauge-sector comparison. If \(v_s^{\rm inv}\) is the full law's constant restricted to vertex-gauge-invariant functions, then for \(s\ge2\)
\[
   \min\{v_s^{\rm inv},(1-1/s)^4\}\le v_s\le v_s^{\rm inv}.             \tag{8}
\]
The cited proof resolves the commuting vertex Haar projections. A component charged at a vertex is annihilated by an exterior projection for each cube containing the entire star of that vertex, giving the factor in (8).

**PROVED, conditional physical consequence.** Consider a matched diagonal as in [row 1254](gap-solve29-astra62.md), (1)–(4), (17). Work in fixed physical length units. For example take \(a\downarrow0,\ aN\to\infty,\ N\le a^{-P}\) for fixed \(P\), \(\beta\) comparable to \(\log(1/a)\), and \(s\) of order \((\log(1/a))^2\). An integer \(r\) of order \(\log(1/a)\) with sufficiently large coefficient makes \((e^{h_r}-1)(N/s)^2=o(as)\) in (7), since \(b_s=O((s+1)^3)\). This choice gives \(t/s\to1\). The sufficient input
\[
                         \bar v_s\ge c(as)^2,\qquad c>0                  \tag{9}
\]
then gives \(v_t\ge c'(at)^2\) with \(c'>0\). Indeed the positive ratio in (7) is increasing in \(\sqrt{\bar v_s}\), so its value at \(\sqrt c\,as\) suffices. Conversely a full gauge-invariant bound at side \(s\) and the same scale gives (9) by (7)–(8), reducing \(c\) if necessary. The earlier cube-size comparison and the finite-torus correlation estimate of Bhattacharjee, Bhattacharya, Lockwood and Romanov give a physical spectral exclusion under that row's support, growth, reflection-positive convergence and dense full-observable matching hypotheses. Equation (7) uses the actual label marginal at each cutoff, with no quadrature or change of Wilson action. Its present volume factor requires controlling the chosen diagonal.

## Removing the volume loss

**PROVED.** The following stronger comparison holds for the same exact measures on every torus with \(2t+4\le N\). Choose \(r\ge1\) so that \(h_r\le 2^{-12}\), put \(t=s+2r\) and \(e_0=e^{h_r}-1\). There is an absolute \(K\le 1+144e_0\) such that
\[
 \overline{\mathcal E}_s(Mf)\le K^2(t/s)^4\mathcal E_t(f),\qquad
 v_t\ge
 \frac{\bar v_s}{K^2(t/s)^4+\bar v_s/(1-\rho)}.                        \tag{10}
\]
The collar can be chosen with \(r\le C[1+\log(2+\beta)+\log(s+1)]\), independently of \(N\), by (6). Thus at \(s\) of order \(\beta^2\) the relative increase of side vanishes as \(\beta\to\infty\). The proof controls the contribution of each successive exterior shell by ordinary Wilson variances.

**PROVED.** First note two extensions of the preceding bounds. In a set \(L\) of free links with their cells prescribed and every other link fixed exactly, the proof of (3) gives, on that conditional law,
\[
 (1-\rho)\operatorname{Var} f\le t^{-4}\sum_y
         \mathbb E\operatorname{Var}(f\mid U_{L\setminus D_t(y)}).
                                                                         \tag{11}
\]
Using \(L\cap D_t(y)\) in (2) still counts each free link in \(t^4\) updates. Empty intersections cost zero. Also (6) continues to hold when any subset of the remote links \(Z\) has exact fixed values. Its cross-ratio proof compares only the remaining values, and the same oscillation controls normalization against a different remote marginal. One may enlarge the collar until it fills the torus. Before that point the periodic maximum-distance neighbourhood has the claimed separation from its complement, and the count \(b_s\) concerns the original, small core.

**PROVED.** Fix an origin \(x\). Denote its core by \(A\), put \(\mathscr C=\sigma(\eta_{A^c})\), and let \(V_k\) enlarge \(A\) by \(r+kt\) layers in each direction for integers \(k\ge0\). Stop at the first \(V_k\) that is the torus, and let \(\mathscr F_k=\mathscr C\vee\sigma(U_{V_k^c})\). For \(g=A_x f\), one has \(\mathbb E[g\mid\mathscr C]=0\) and, on fixing \(\mathscr C\), \(g\) depends only on the core labels. Set \(g_k=\mathbb E[g\mid\mathscr F_k]\). Applying (6) to this larger collar, now predicting the core function from the remote field, gives
\[
 \|g_k\|_2\le e_0\rho^{kt}\|g\|_2 .
\]
Indeed \(h_{r+kt}=h_r\rho^{kt}\) and \(e^{uz}-1\le u(e^z-1)\) for \(0\le u\le1\). The terminal \(g_k\) vanishes. Put \(D_{x,k}=\|f-\mathbb E[f\mid\mathscr F_k]\|_2^2\). In the telescoping decomposition of \(g\), the first difference \(g-g_0\) is orthogonal to \(\mathscr F_0\) and has norm at most \(\|g\|_2\). Each later \(g_{k-1}-g_k\) is orthogonal to \(\mathscr F_k\) and has norm at most \(\|g_{k-1}\|_2\). Pair with \(f\) and use \(\langle g,f\rangle=\|g\|_2^2\). This gives, also when \(g=0\),
\[
 \|A_x f\|_2\le \sqrt{D_{x,0}}+
      e_0\sum_{k\ge1}\rho^{(k-1)t}\sqrt{D_{x,k}},                      \tag{12}
\]
with the sum stopping at the terminal shell.

**PROVED.** Write \(d_V(f)=\mathbb E_\mu\operatorname{Var}(f\mid U_{V^c})\). One has \(D_{x,0}\le d_{V_0}(f)\). For each \(k\ge1\),
\[
 (1-e_0)D_{x,k}\le d_{V_0}(f)+
 \frac{t^{-4}}{1-\rho}\sum_{y:D_t(y)\cap V_k\ne\varnothing}
                         d_{D_t(y)}(f).                                 \tag{13}
\]
To prove it, fix \(\mathscr F_k\). The exact core \(X=U_A\) and the remote variables \(Y=U_{V_k\setminus V_0}\) have maximal centered \(L^2\) correlation at most \(e_0\), by the strengthened (6) for the first collar. On the centered space of this conditional law the map \((u(X),v(Y))\mapsto u(X)+v(Y)\) has squared norm at most \(1+e_0\) on the direct sum of the two centered spaces, since the cross term is at most \(2e_0\|u\|\|v\|\). Its adjoint has the same norm. Subtracting its squared norm inequality from twice the variance gives
\[
 (1-e_0)\operatorname{Var} f\le
       \mathbb E\operatorname{Var}(f\mid X)+\mathbb E\operatorname{Var}(f\mid Y)
\]
under the current conditioning. After additionally fixing \(Y\), all links outside \(V_0\) are exact, so the second variance integrates to at most \(d_{V_0}(f)\). After fixing \(X\), every free link of \(L=V_k\setminus A\) has its bin fixed, and all other links are exact. Apply (11). Upon integration each update variance is at most the corresponding ordinary \(d_{D_t(y)}(f)\) by nested conditioning. This proves (13).

**PROVED.** Sum (12) using the triangle inequality for the norm \((s^{-4}\sum_x|\cdot|^2)^{1/2}\). For fixed \(y\), the number of origins \(x\) with \(V_k(x)\cap D_t(y)\ne\varnothing\) is at most \(((2k+2)t)^4\) because the two sides before periodic truncation are \((2k+1)t\) and \(t\). This also bounds the count if \(V_k\) fills the torus. Equation (13) therefore gives the first inequality of (10) with
\[
 K=1+\frac{e_0}{\sqrt{1-e_0}}\sum_{k\ge1}
      \rho^{(k-1)t}\sqrt{1+(2k+2)^4/(1-\rho)} .
\]
For \(\rho=1/5\) the square root is at most \(9(k+1)^2\). Differentiating the geometric series twice gives \(\sum_{k\ge1}(k+1)^2(1/5)^{k-1}<8\), and \(1/\sqrt{1-e_0}<2\). This gives the stated constant. The orthogonal variance decomposition at \(M\), (3) and the label gap give the second inequality of (10). If \(\bar v_s=0\), it holds by positivity.

**PROVED, scope for the weak-coupling target.** In (9) one can now use an infinite set of permitted torus sizes at each cutoff, with the *same* enlargement \(t\), or a matched finite-torus diagonal without any bound on \(\log N\) from this comparison. If \(s\asymp\beta^2,\ \beta\asymp\log(1/a)\) and \(c(as)^2\le\bar v_s\), (10) gives \(v_t\ge c'(at)^2\), uniformly. The upward cube-size comparison of row 1254 can then be applied to the original measure. The exact finite label law still has to supply (9).

## Trying to prove the bound for the labels

**PROVED.** A single-link variation test on the label law behaves very differently from (1). Fix neighbouring links \(i,j\) and *any* labels outside this pair. Start at any current label for \(j\). By changing just this label the conditional probability law of \(\eta_i\) can be changed in total variation by at least
\[
                   1-C\,\frac{\log(2+\beta)}{1+\beta}                  \tag{13a}
\]
for all sufficiently large \(\beta\), uniformly in the volume and the chosen labels. The estimate permits every mesh of diameter at most the stated \(\delta\).

**PROVED.** The one-link weight given its exact neighbours is \(\exp(\beta u\cdot S)\) on \(S^3\), where \(S\) is the sum of six unit staples expressed in the frame of \(i\). On a torus of side at least four the eighteen other links of the six plaquettes are distinct. Choose representatives of their prescribed cells, apart from \(j\). Varying \(j\) makes its one staple run over the whole unit sphere while the other five sum to a fixed \(S_0\), \(|S_0|\le5\). Choose the new staple \(b\) on a two-sphere in \(S_0^\perp\), with any three-dimensional subspace permitted when \(S_0=0\). The directions \(n_b=(S_0+b)/\sqrt{1+|S_0|^2}\) run over a two-sphere of radius at least \(1/\sqrt{26}\). Select the label at \(j\) containing the prescribed value or having it in its closure. All actual neighbour values in these cells then give \(|S-(S_0+b)|\le18\delta\) by telescoping the three unit factors in each staple. In particular \(|S|\ge1/2\) and the direction \(S/|S|\) is within \(36\delta\) of \(n_b\) at large \(\beta\).

**PROVED.** Put \(l=L\sqrt{\log(2+\beta)/(1+\beta)}\) for a sufficiently large fixed \(L\). At fixed neighbours the link law has weight proportional to \(\exp[-\beta|S|\,|u-S/|S||^2/2]\). A cap of radius \(\beta^{-1/2}\) about its maximum supplies at least \(c\beta^{-3/2}\) to the integral, using the Haar radial element proportional to \(\sin^2\theta\,d\theta\) and the bound \(|S|\le6\). The probability outside radius \(l/2\) about \(n_b\) is consequently at most \(C\beta^{-2}\), upon increasing \(L\). This persists after averaging over the exact neighbours consistent with the altered labels. The set of cells meeting this cap lies inside radius \(l\) about \(n_b\). On the indicated two-sphere take a maximal \(3l\)-separated set. Each radius-\(3l\) cap covers at most \(C l^2\) of its area, so at least \(c l^{-2}\) such directions are available. Their label events are disjoint. The original law assigns mass at most \(C l^2\) to one of them, and its chosen altered law assigns it mass at least \(1-C\beta^{-2}\). This proves (13a). Thus replacing an exact link by its bin does not permit using the small disagreement coefficient of the *fixed-label* law for the label dynamics itself.

**GUIDE.** Test next whether this failure comes entirely from allowing highly atypical changes of a label. The absolute conditional correlation of *two ordinary, unaltered labels* is a different experiment. Row 1252's [fresh attempt](gap-solve-fresh-astra62.md), in its section on two conditional lines, exhibited a prescribed ladder exterior. The following test uses ordinary Wilson exteriors for two individual links. A related flat-staple \(1/6\) response was suggested for the Abelian Villain law in [the earlier mixed-derivative note](gap-mixed-opus.md), line 199.

**PROVED.** For the following test choose the mesh diameter \(\delta_\kappa=\kappa/\sqrt{1+\beta}\) with a sufficiently small fixed \(0<\kappa\le1/5\). All the preceding comparisons apply. Let \(c_{ij}^*(\eta)\) be the maximal absolute correlation of two real functions of \(\eta_i,\eta_j\), conditional on *all other labels*. For a fixed link \(i\), on ordinary periodic Wilson tori large enough to contain a fixed surrounding box without wrapping,
\[
       \Pr\!\left\{\sum_{j\sim i}c_{ij}^*(\eta)>2\right\}
                          \longrightarrow 1\quad(\beta\to\infty),       \tag{14}
\]
uniformly over those tori. This is a conditional correlation under the sampled law. It uses no adverse choice of a replacement label.

**PROVED.** In a fixed box containing all the plaquettes incident to \(i\) or any \(j\sim i\), the connection approaches the orbit of a flat connection in probability. The marked moment of [row 1155](gap-solve7-astra62.md), (9), is stronger than required. For clarity the weaker input here also follows on any periodic \(N^4\) directly. Normalize \(Z(\beta)\) using the action \(S=\sum_p(1-w_p)\). Restricting each link to a radius-\(\beta^{-1/2}\) cap about one costs at most \(C N^4\log(2+\beta)\) in minus log Haar volume and gives \(\beta S\le 48N^4\). Since \(\mathbb E_\beta S\) decreases in \(\beta\), one has \(\beta\mathbb E_\beta S\le-\log Z(\beta)\). Translation and axis symmetries give \(\mathbb E|U_p-1|^2\le C\log(2+\beta)/\beta\). A union bound and Markov's inequality put all the finitely many plaquettes within \((\log(2+\beta)/\beta)^{1/4}\) of one with probability tending to one. On a rectangular box a flat assignment is a pure gauge because the products from a root agree along paths. Indeed adjacent coordinate steps can be interchanged using a unit plaquette, and immediate backtracking cancels. On this fixed compact configuration space it follows that every assignment with all plaquettes tending to one has distance tending to zero from the pure gauges. Otherwise a convergent subsequence supplies a flat limit at positive distance. Thus on the event there are vertex frames in which all links of the box are \(o(1)\) from one, with the error uniform on the event.

**PROVED.** Freeze one such choice of frames and consider one pair \(i,j\). Exact exterior links consistent with their observed exterior labels, in these frames, differ from the reference links by at most \(\delta_\kappa\) each. In particular the relevant exterior parameters \(p\) all tend to the identity tuple. The log weight of the two free links divided by \(\beta\), denoted \(W_p(u,v)\), contains eleven plaquette traces, with five involving only \(u\), five involving only \(v\), and one common trace. At the identity exterior the maximum is unique at \((1,1)\), since the five terms for each single link are maximized there and the common term is bounded by one. In coordinates \((x,y)=(\operatorname{Im}u,\operatorname{Im}v)\) on the identity hemispheres, the negative Hessian there is
\[
       L=\begin{pmatrix}6I_3&\tau I_3\\ \tau I_3&6I_3\end{pmatrix},
 \qquad L^{-1}=\frac1{35}
         \begin{pmatrix}6I_3&-\tau I_3\\-\tau I_3&6I_3\end{pmatrix},
                                                                         \tag{15}
\]
where \(\tau=\pm1\) is the product of the two plaquette incidence signs. This follows from the quadratic contribution \(-|\pm x\pm y|^2/2\) of the common plaquette and \(-|x|^2/2\) or \(-|y|^2/2\) of each other term.

**PROVED.** Here are the uniformity details for using (15) under conditioning. The mixed Wilson terms are smooth in the finitely many variables and parameters. On a sufficiently small fixed coordinate ball about zero, the negative Hessian remains at least \(2I\) for all nearby \(p\). Outside a smaller ball the compact identity-exterior maximum is strictly separated, and that separation persists on parameter perturbation sufficiently small. The implicit function theorem gives a unique maximizer \(m(p)\) in the chart and a bounded derivative there, since its inverse Hessian is bounded and the mixed derivatives with the exterior parameters are bounded. For the exact two-link law, the first two moments of \(\sqrt\beta((x,y)-m(p))\) converge to those of a centered Gaussian with covariance \(L^{-1}\), uniformly as \(p\to1,\beta\to\infty\). Indeed on bounded rescaled sets Taylor's cubic remainder is \(O(|z|^3/\sqrt\beta)\), the Hessian converges to \(L\), and the Haar chart Jacobian converges to its positive value at zero. On the fixed ball the integrand times any polynomial of degree at most two is bounded, in rescaled coordinates after division by its maximum, by \(C(1+|z|^2)e^{-c|z|^2}\). Off this ball the strict separation gives an exponentially small contribution even after rescaling the normalization by \(\beta^3\) and multiplying by a quadratic moment. These estimates give the asserted moment limits by truncation.

**PROVED.** Integrate next over the exact exterior given its *labels*. Across its possible parameters the centers \(\sqrt\beta m(p)\) have diameter at most \(C\kappa\) by the derivative bound. Centering a Gaussian at an arbitrary mean does not change its covariance. The conditional law of total covariance consequently changes each entry of (15)'s inverse by at most \(C\kappa^2+o(1)\) since the exact conditional means, measured from their local centers, are uniformly \(o(1)\). Read one common imaginary coordinate of each link in the frozen frames, multiplied by \(\sqrt\beta\), using any representative of its label. Replacing an actual link by its representative changes this reading by at most \(\kappa\), including after the frame rotations. Since the centered variances before replacement are bounded, Cauchy–Schwarz changes their variances and covariance by \(O(\kappa)+o(1)\). Each conditional pair correlation in absolute value is therefore at least \(1/6-C\kappa-o(1)\). The constants are uniform over the eighteen pairs. The chosen coordinates may depend on the exterior in a maximal-correlation test. Fixing a good completion whenever one exists gives two functions of the individual labels. Taking \(\kappa\) small enough that the lower bound exceeds \(1/9\) proves (14). In particular an average of these unsigned row sums over ordinary exteriors cannot yield a contraction bound below one at weak coupling. This calculation leaves open an estimate using the signs and the larger update regions in (9).

## Integrating the unobserved bulk before testing the discrete law

**GUIDE.** The preceding test still recorded every link. I next allow whole four-dimensional cell interiors to move freely and retain finite observations only on their common three-dimensional boundaries. The cell factorization is from [row 1222](gap-solve24-astra62.md), (1). The private-variable projection argument in [row 1254](gap-solve29-astra62.md), (7), is the analogous earlier comparison for path interiors. Its criterion (2) uses several shifted walls. The [earlier skeleton analysis](gap-ps-disint-max.md), §5.3, treats a log-Sobolev inequality in the continuous boundary variables. Here the estimate concerns ordinary conditional resampling on one fixed wall grid, with constants uniform even when the cell size grows.

**PROVED.** Let \(b\mid N\), \(m=N/b\ge20\), and use the aligned cells of side \(b\). The retained set \(W\) consists of the links tangent to at least one cell wall, exactly as in row 1222. Group the links of \(W\) by the half-open cell containing their base and denote the resulting exact group variables by \(Y_z\), \(z\in(\mathbb Z/m)^4\). Write \(M_W f=\mathbb E[f\mid U_W]\), and \(\mathcal E^Y_k\) for the \(k^{-4}\)-normalized sum of the marginal heat-bath variances on side-\(k\) cubes of these variables. If \(1\le k\) and \((k+4)b<N\), then
\[
 \mathcal E_{(k+4)b}(f)\ \ge\
 \left(\frac{k}{k+4}\right)^4
 \left[\mathcal E^Y_k(M_W f)+\|(I-M_W)f\|_2^2\right].                 \tag{16}
\]
In particular, this comparison pays for the variance of all the omitted interiors at once, for any finite Wilson coupling.

**PROVED.** For a coarse origin \(z\) let \(A\) be the wall links based in its side-\(kb\) cube. Enlarge the proposed update to \(J_z\) consisting of \(A\) and the private links of every closed \(b\)-cell whose vertex set meets the cube of bases. Each cell whose weight reads \(A\) is included. Given \(W\), all private cell fields are independent, and the conditional law in every omitted cell depends only on \(W\setminus A\). Thus projecting a wall function onto the exact exterior of \(J_z\) gives exactly its marginal conditional expectation given \(W\setminus A\). This projection preserves the wall subspace and, by self-adjointness, its orthogonal complement. Its variance on \(f\) splits into the sum on these two components. On the complement it dominates the variance after additionally fixing all of \(W\) and resampling just the private fields in the selected cells. At fixed \(W\), obtain the product component for a subset of cells by applying \(I-P_C\) on that subset and \(P_C\) on its complement, with \(P_C\) integration over cell \(C\). These commuting products are orthogonal. Each nonconstant component has at least one cell, and its squared norm is counted at least \(k^4\) times as the coarse origin varies. Finally, \(J_z\) fits in every fine cube of side \((k+4)b\) with origin \(bz-b\mathbf1-h\), \(h\in\{0,\ldots,b-1\}^4\). These \(b^4\) origins per \(z\) partition the fine origins. Enlarging an update increases its integrated variance. Summation and normalization prove (16).

**PROVED.** The wall variables have an exact density against product Haar of the form \(\prod_C K_C(Y)\). Assign each plaquette to one closed cell containing it, choosing an incident cell for all-wall plaquettes, and integrate the private links of each cell independently at fixed \(W\). Its positive factor reads only the supervariables at corners \(z+\{0,1\}^4\). Each group \(Y_z\) has at most \(12b^3\) links because, in each of four directions, at least one of the three transverse coordinates must be on a wall. Changing each of the links in one \(Y_z\) by at most \(d\) changes \(\log K_C\) by at most \(72\beta b^3d\). Each changed link is used by at most six plaquettes, and changing one entry of a trace changes it by at most its chord displacement. The same pointwise likelihood bound survives the private integration, including at arbitrary boundary values.

**PROVED.** Observe the individual wall links in the same sphere partitions, now of diameter
\[
             d_b=\frac{2^{-32}}{(1+\beta)b^3},
\]
and let \(L_z\) be the resulting vector of labels on \(Y_z\). Let \(\widetilde v_2\) be the optimal full Poincaré constant for updating side-two cubes of these vectors under their *exact joint marginal*, with normalization \(2^{-4}\sum_z\). There is an absolute \(c_1>0\) independent of \(b,\beta,N\) such that
\[
                \frac{v_b}{16}\ \le\ \widetilde v_2,\qquad
                v_{8b}\ \ge\ c_1\widetilde v_2 .                        \tag{17}
\]
The number of recorded bits per side-\(b\) cell is at most \(C b^3[1+\log(2+\beta)+\log b]\). This counts a possible fixed-length encoding of the observations. No finite sum is evaluated.

**PROVED.** Apply the proof of (10) on the coarse lattice to the continuous variables \(Y_z\) with bins \(L_z\). For precision, the single-variable estimate and collar estimate needed in that proof follow as follows. With \(\kappa_0=2^{-32}\), each incident factor has log oscillation at most \(72\kappa_0\) as a pinned \(Y_z\) varies. At most sixteen factors meet a site and at most eighty other sites can share a factor with it. Changing another group, even arbitrarily, changes its conditional log-weight oscillation on this bin by at most \(2\cdot16\cdot72\kappa_0\). The interpolation proof of (1) gives a row sum at most \(80\cdot 2\cdot16\cdot72\kappa_0/4<1/5\). For a free side-two core the log interaction of its boundary with one pinned group has difference oscillation at most \(2\cdot16\cdot72\kappa_0\) between two inner configurations. There are at most \(4^4-2^4=240\) such groups. Linearly interpolating the log factors preserves the within-bin mixed oscillation bound. Thus the proof of (6) works, at every additional slab depth \(r\ge1\), with \(h_r=240\cdot 2\cdot16\cdot72\kappa_0\,\rho^r\). Already \(h_1<2^{-12}\). The factors have range one in coarse maximum distance, so the shell count and the variance proof of (10) apply at \(s=2,t=4\). We obtain \(v_4^Y\ge c_2\widetilde v_2\). Here \(\widetilde v_2\le1\) by testing a nonconstant function of one label group. Only the \(2^4\) updates meeting that group contribute, and each integrated variance is at most its variance. With \(K<2\) in (10) one may take \(c_2=1/66\). Combining with (16) at \(k=4\) gives \(c_1=1/1056\).

**PROVED.** For the other direction, apply the fine side-\(b\) form to a function of \(L\). A fine side-\(b\) cube with origin \(bz+h,\ 0\le h_\nu<b\), touches wall groups only in the aligned side-two coarse cube at \(z\). All other labels are known in the fine exterior. Its integrated conditional variance is at most the side-two label variance at \(z\). Summing over the \(b^4\) offsets gives \(\mathcal E_b(f(L))\le16\widetilde{\mathcal E}_2(f)\), proving (17). Equation (8) relates the fine constants to their gauge-invariant versions. In particular (17) applies with \(b\asymp\beta^2\), when a lower bound of order \((ab)^2\) suffices through the earlier cube ascent. It also applies with \(ab\) fixed and positive, when a strictly positive lower bound for \(\widetilde v_2\) already suffices on the matched tori. Thus only surface-order fine data per physical cell are needed in this version of the infrared estimate.

## Dependence of adjacent boundary blocks in the ordinary Wilson law

**PROVED.** At the remaining scale in (17) even the ordinary exterior gives strong dependence for certain adjacent, disjoint blocks of the wall labels. For \(b\ge8\), take two side-two coarse cubes side by side in direction one. In fine coordinates use \(\mathcal L=[0,2b)^4\) and \(\mathcal R=[2b,4b)\times[0,2b)^3\), restricting both to the recorded wall groups. Condition on the wall labels outside their union, with sigma-field \(\mathscr B\). For all sufficiently large \(\beta\), uniformly in \(b,N\),
\[
 \begin{split}
  \mathbb E\,\mathrm{corr}_{\max}(L_{\mathcal L},L_{\mathcal R}\mid\mathscr B)
      &\ge 1-C\log(2+\beta)/\beta-Cd_b,\\
  I(L_{\mathcal L};L_{\mathcal R}\mid\mathscr B)
      &\ge c b^2\left[\tfrac32\log\{\beta/\log(2+\beta)\}-C\right].
 \end{split}                                                            \tag{18}
\]
Here the first quantity averages the maximal absolute correlation in each conditional law and the second is conditional mutual information in nats. These tests concern touching update regions.

**PROVED.** Choose pairs \(v,w=v+\hat3\) in the plane \(v_1=2b,\ v_2=b\), with \(1\le v_3,v_4<b-1\), using alternating \(v_3\) so all endpoints are distinct. There are \(M_0\ge c b^2\) pairs. In \(\mathcal R\) read the direct link from \(v\) to \(w\), denoting its matrix by \(X_j\). In \(\mathcal L\) read the three-link path through \(v-\hat1,w-\hat1\), denoting its matrix by \(Y_j\). All its links are retained because they are tangent to the wall \(x_2=b\). The two paths differ by one elementary plaquette. No wall label in \(\mathscr B\) touches their starting vertices. Independent gauge rotations there preserve the conditional law and rotate the \(X_j\)'s independently on the left and act in the same way on the \(Y_j\)'s. In particular \(X\) alone and \(Y\) alone each have product Haar distribution at every exterior of positive probability. For one pair the two real parts have conditional means zero and variances \(1/4\). Their conditional covariance is \(\mathbb E[w(X_jY_j^{-1})\mid\mathscr B]/4\), by the rotation-average of two coordinates of a uniform unit quaternion. These are uses of the forest gauge integration also employed in [row 1192](gap-solve20-astra62.md).

**PROVED.** Replace links by representatives of their wall labels to form \(\widehat X,\widehat Y\) with chord errors at most \(d_b,3d_b\). This changes the bounded coordinate variances and covariance by at most \(C d_b\). Using the plaquette mean estimate preceding (15) proves the first line of (18). For the second, under the conditional joint law,
\[
 \mathbb E\sum_j|\widehat X_j-\widehat Y_j|^2
                \le C M_0\{\log(2+\beta)/\beta+d_b^2\}
\]
after averaging in \(\mathscr B\). Under the product of the two marginals at a fixed exterior, independently couple the first reading to its product-Haar \(X\). For every fixed second reading \(y\) and \(u\ge1\),
\[
 \mathbb E\exp\!\left[-u\sum_j|\widehat X_j-y_j|^2\right]
   \le e^{uM_0d_b^2}(C u^{-3/2})^{M_0}.
\]
Indeed \(|\widehat X_j-y_j|^2\ge |X_j-y_j|^2/2-d_b^2\). Haar integration with the \(\sin^2\theta\) radial element and \(1-\cos\theta\ge2\theta^2/\pi^2\) bounds each factor by \(C u^{-3/2}\). For laws \(P,Q\) the inequality \(D(P\|Q)\ge P h-\log Q(e^h)\) follows by applying Jensen's inequality to the likelihood ratio of \(Q e^h/Q(e^h)\) against \(P\), on the support of \(P\). Use \(h=-u\sum|\widehat X_j-\widehat Y_j|^2\) on the two label groups and \(u=\beta/\log(2+\beta)\). The bound on the product integral is uniform in the exterior. Integration gives the second line of (18). Thus the adjacent-group information diverges even if \(ab\) is held at a fixed positive length.

## Removing the shared gauge frames from the relaxation test

**PROVED.** There is a version of (17) on variables with the preceding frame information removed. In each half-open \(b\)-cell connect its wall vertices by a tree with root at the lower corner. Holding one coordinate on its lower wall lets a path decrease the other coordinates to the corner using only tangential links, so the graph is connected. The right edges \(X_j\) in (18) can all be included in the trees since they are vertex-disjoint edges within their respective groups and form a forest. For each wall vertex \(v\) let \(p_v\) be the transport from its root to \(v\), with \(p_v=1\) at a root. On every nontree wall edge \(e=(v,w)\) retain \(Q_e=p_vU_ep_w^{-1}\). Group these variables by the \(b\)-cell of the original edge base, and observe them in the \(d_b\)-bins. Write \(\widehat v_4\) for the normalized side-four coarse cube Poincaré constant of their exact marginal. For \(m=N/b\ge24\),
\[
       \widehat v_4\ge v_b/256,\qquad
       v_{10b}^{\rm inv}\ge \widehat v_4/200 .                          \tag{19}
\]
One root gauge group per cell is still present. Gauge-invariant conclusions use (8).

**PROVED.** Tree Haar coordinates change triangularly to independent Haar variables \(p_v\) for nonroot vertices by successive conditioning on the parent and Haar multiplication or inversion of the child edge. The remaining edges change by Haar translations at fixed frames. Each integrated cell factor \(K_C\) is invariant under vertex gauges on its closed cell, by changing its private integration variables and using invariance of the Wilson plaquette traces. Thus setting the tree links to one leaves the cell factors in the same local product form on \(Q\), and the \(p_v\)'s factor out as independent probability Haar variables. These cell factors on the reduced variables have the same \(72\beta b^3d_b\) oscillation estimate as before. With side-four core the one-layer boundary contains at most \(6^4-4^4=1040\) groups. The proof after (17) now gives \(h_1\le1040\cdot2304\cdot2^{-32}/5<2^{-12}\), and (10) gives \(v_6^Q\ge\widehat v_4/22\). All actions used in the comparison are exact integrals over the original Wilson measure.

**PROVED.** For a gauge-invariant fine \(f\), \(M_W f\) is invariant on the wall graph. In the new variables it is a function \(g(Q)\) because changing the nonroot frames at fixed \(Q\) is a vertex gauge transformation. For a group cube of size six, fixing all the frames and all \(Q\)'s outside the group cube fixes all the original wall links outside it. Therefore \(\mathcal E^Y_6(M_W f)\ge\mathcal E^Q_6(g)\) by conditioning, using the product disintegration for the latter variance. Substitute into (16) to get \(v_{10b}^{\rm inv}\ge(6/10)^4\min(1,v_6^Q)\), which gives (19) since \(\widehat v_4\le1\). Conversely, changing links in one fine side-\(b\) cube can change tree frames only in the side-two block of coarse groups that its bases meet. Reduced edges using one of those frames may have base in an adjacent group on the lower side. All affected reduced labels fit in \(z+\{-1,0,1,2\}^4\) for any fine origin \(bz+h,\ 0\le h_\nu<b\). The labels off this larger cube are functions of the exact fine exterior. Summing the resulting variance inequality over offsets gives \(\mathcal E_b(f(L^Q))\le256\,\widehat{\mathcal E}_4(f)\), proving the first inequality of (19).

**PROVED.** In these coordinates the right-hand reading on every chosen edge of (18) is exactly one. The left reading between the same two rooted vertices has chord distance to one equal to \(|Y_jX_j^{-1}-1|\), since the right edge was put in the tree. The independent Haar values producing (18) have been integrated out without changing (19)'s physical consumer. The reduced variables still include curvature loops and the relative transports between different cell roots.

## A gauge-invariant comparison remaining after any choice of the trees

**PROVED.** Suppose \(\beta\to\infty,\ b/(1+\beta)\to\infty\) in (19), with any allowed \(m\). For *every* choice of its within-cell trees, two adjacent side-two groups of reduced wall data have maximal correlation tending to one in probability, conditional on all the other reduced labels. The two scalar tests can be chosen as readings of gauge-invariant fundamental Wilson loops, to error at most \(3d_b\) in the labels. Their centered variances tend to \(1/4\) in probability. For the same exact loop traces, the covariance with any bounded distant insertion that misses the selected cell and its three-edge detour is at most
\[
             C\exp[-c b/(1+\beta)]\,\mathbb E|F|.                      \tag{20}
\]
Thus the correlation near the shared boundary and its consequence at separated support can both be tested on actual Wilson configurations.

**PROVED.** In the geometry of (18) take the right \(b\)-cell of coarse index \((2,1,1,1)\). On its ridge \(x_1=2b,\ x_2=b\), take a square \(D\) of side \(\ell\ge b/3\) in the middle of the \(x_3,x_4\) coordinate intervals \([b,2b)\), staying clear of their ends. Some nearest-neighbour edge \(e=(v,w)\) of \(D\) has tree distance at least \(c b\) between its ends. Here is an argument allowing the tree to leave the plane. Give its vertices in \(D\) weight one and all others weight zero. Choose a centroid vertex \(o\) for which every component on deletion has at most \(|D|/2\) weight. Find it by moving from any vertex towards its overweight component as long as one exists. This walk cannot traverse an edge backwards and must stop. With \(j=\lfloor\ell/8\rfloor\), keep all the rows and columns of \(D\) at coordinate distance greater than \(j\) from the corresponding coordinate of \(o\). Their union is connected, since at least one entire row and one entire column remain. At most \((2j+1)^2\) vertices were lost, so more than half remain for large \(b\). Every retained vertex has fine lattice distance greater than \(j\) from \(o\). If every adjacent pair in this union had tree distance at most \(j\), their tree paths would avoid \(o\), putting all these vertices in one component after deletion. This contradicts the centroid property. In particular the selected edge is nontree.

**PROVED.** Read \(A=w(Q_e)\) on the right and \(B\) as the half-trace of the product of the reduced matrices on the three-edge left detour of (18), using identity on tree edges. Both endpoints belong to the same right root cell, so both traces are gauge invariant. The tree frames cancel along the detour. In original variables both loops use the same tree return from \(w\) to \(v\). Consequently \(|A-B|\le|X-Y|\) for the two original open paths, and \(\mathbb E|A-B|^2\le C\log(2+\beta)/\beta\). Each true trace has a simple loop representative after deleting the conjugating stem. Its tree path contains at least \(c b\) distinct links. Every other reduced label outside the two large blocks is measurable off these tree links because a reduced edge can read a frame in this distinguished cell only if its base group is the cell or an immediate predecessor, all of which belong to the two blocks. This observation permits a conditional variance estimate even at rare exteriors.

**PROVED, using the one-link estimate of [row 1145](gap-solve2-astra62.md), (1)–(2).** Among the edges of the tree return choose at least its length divided by nineteen with no shared plaquette, by retaining one and removing its at most eighteen neighbours at each choice. Conditional on every other raw link, the holonomy of either simple loop has Haar density within \(\sum_{d\ge2}d^2 e^{-(d-1)c b/(1+6\beta)}\) of one in the supremum norm. The same independent-link Fourier estimate appears in [row 1149](gap-solve4-astra62.md), line 353, to obstruct a large tree chart. Its normalized one-link character formula is GL3 of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, in outline lines 2197–2231, located by [index chunk 02](sa-index/chunk-02.md). The error is \(O(e^{-c' b/(1+\beta)})\) here. Thus at every reduced-label exterior in question both exact scalar readings have means tending to zero and second moments tending to \(1/4\). The conditional squared difference tends to zero in probability by its ordinary expectation bound. The label readings differ from their exact traces by at most \(3d_b\), giving the conditional maximal-correlation assertion. If \(F\) is measurable off those selected raw links, the same conditional mean bound and centering give (20). In particular it applies to reduced-label groups at coarse distance at least two from the selected cell and outside the detour's support. The long return sits in *both* fine observables despite their disjoint groups of reduced coordinates.

## Joint boundary readings in fixed representations

**GUIDE.** A bound on one long chord leaves functions of many chords, including products in which tree routes cancel. I tested whether the Wilson one-link integral gives a bound on a whole family of joint readings with arbitrary coefficients. The relevant normalization is the variance in the Wilson law. The estimate below uses no count of spin-network terms.

**PROVED.** Write \(p_s(q)=e^{s w(q)}/Z(s)\) against probability Haar on \(SU(2)\), \(s\ge0\). For a fixed irreducible representation of dimension \(d\ge2\), let \(V_d\) be the span of all its matrix coefficients, and write \(\chi_d\) for its character. In the actual one-link norm the exact squared norm of averaging on this space satisfies
\[
   \sup_{f\in V_d,\ f\ne0}
       \frac{|\mathbb E_s f|^2}{\mathbb E_s|f|^2}
     =\frac{(\mathbb E_s\chi_d)^2}{\mathbb E_s\chi_d^2}
     \le\frac{(\mathbb E_s w)^2}{\mathbb E_s w^2}
     \le 1-\frac{c}{(1+s)^2}.                                         \tag{21}
\]
In particular the fundamental representation attains the middle bound. Translations of the density in the group leave the supremum unchanged. To see the equality, conjugation-average \(f\). This keeps its mean, reduces its norm and yields a multiple of \(\chi_d\), by irreducibility. For the next inequality put \(m_d(s)=\mathbb E_s\chi_d=d I_d(s)/I_1(s)\) by GL3. For \(s>0\), \(m_d>0\). Each \(I_{k+1}/I_k\) has positive derivative by the Riccati equation and comparison with its strictly increasing positive root in row 1145, (1). Thus \((\log m_d)'\ge(\log m_2)'\) by the product of the successive ratios starting with \(I_2/I_1\). But \(m_d'=\operatorname{Cov}_s(\chi_d,w)\) and \(m_2=2\mathbb E_s w\). Cauchy–Schwarz gives
\[
   \frac{\operatorname{Var}_s\chi_d}{m_d^2}
       \ge \frac{[(\log m_d)']^2}{\operatorname{Var}_s w}
       \ge \frac{\operatorname{Var}_s w}{(\mathbb E_s w)^2}.
\]
At \(s=0\) all the stated nontrivial means vanish. For the last inequality in (21), \(x=1-w\) has unnormalized density \(e^{-sx}\sqrt{x(2-x)}\) on \([0,2]\). Its integral is bounded above by \(C(1+s)^{-3/2}\) by comparison with a Gamma integral for \(s\ge1\) and boundedness for \(s\le1\). The disjoint intervals \([h/8,h/4]\) and \([h/2,3h/4]\), \(h=(1+s)^{-1}\), each have probability bounded below by an absolute constant. Taking two independent copies shows \(\operatorname{Var}_s w\ge c h^2\), and \(\mathbb E_s w^2\le1\).

**PROVED.** On the actual fine Wilson lattice take \(M_0\) distinct links \(I\) with no common plaquette between two of them. Let a square-integrable reading \(F\), at each fixed \(U_{I^c}\), belong to a tensor product of specified spaces \(V_{d_i}\) in the \(I\)-variables, with every \(d_i\ge2\). The dimensions can vary with the exterior. The coefficient array can be arbitrary, including entangled contractions. With \(P_{I^c}\) denoting expectation given the exact exterior,
\[
 \|P_{I^c}F\|_2\le e^{-c' M_0/(1+\beta)^2}\|F\|_2,\qquad
 \|\mathbf1_{[0,\lambda]}(H_s)F\|_2
       \le \bigl(e^{-c' M_0/(1+\beta)^2}+\sqrt\lambda\bigr)\|F\|_2 .    \tag{22}
\]
Conditional on the exterior the link laws are independent translates of \(p_{s_i}\), \(0\le s_i\le6\beta\). The norm of their product averaging functional on the Hilbert tensor product is the product of the one-factor norms. Apply (21) and integrate. For the second bound \(H_s\ge I-P_{I^c}\) as a quadratic form. Given the exterior, the product components for subsets of \(I\) are orthogonal, and each nonconstant component is counted by all \(s^4\) cube updates containing any one of its links. Giving the exterior as extra information only decreases each fine update variance. This is the product argument in row 1254, (36). Pair \(F\) with any unit vector in the indicated spectral band and split at \(P_{I^c}\). This proves (22). For a separated test measurable off \(I\) the first estimate alone applies, with its full norm factor. The adjoint and fundamental single-loop bounds previously used a product of matrices. Here the tensor norm applies to every coefficient array in the stated spaces.

**PROVED.** There is a finite-band version allowing coherent superpositions of different spins at each selected link. Write \(W_D=\bigoplus_{d=2}^{D+1}V_d\), \(D\ge1\). For any translate of \(p_s\), let \(\Pi_D\) be the orthogonal projection onto \(W_D\) in its weighted \(L^2\) space. There are explicit bounds of the form
\[
             1-\|\Pi_D 1\|^2 \ge
                   [C(D+1)(1+s)]^{-2D}/[C(D+1)],                      \tag{23}
\]
with an absolute \(C\). At fixed \(D\) the order \((1+s)^{-2D}\) is sharp up to a \(D\)-dependent factor. To prove the lower bound translate the maximum to one and conjugation-average as in (21). The residual \(P(w)=1-\Pi_D1\) is a degree-at-most-\(D\) polynomial with Haar mean one. Indeed the character \(\chi_d=\sin(d\theta)/\sin\theta\) is a polynomial of degree \(d-1\) in \(\cos\theta\) by the sine recursion. On the interval \(w\in[1-3h/4,1-h/4]\) the normalized \(p_s\) marginal density is at least \(c/h\), by the integral bound in (21). Select \(D+1\) disjoint subintervals there, each of length \(h/[4(D+1)]\) and with gaps of the same length. In each there is a point with \(|P|\le C\sqrt{D+1}\|P\|_{L^2(p_s)}\). Lagrange interpolation bounds the supremum on \([-1,1]\) by \((D+1)C\sqrt{D+1}[8(D+1)/h]^D\|P\|\), since every interpolation denominator factor has absolute value at least \(h/[4(D+1)]\). Absorb the outside \(D+1\le2^D\) into the absolute base constant. The supremum is at least one by the Haar mean. This gives (23). For the matching power choose \(P(w)=(1-w)^D/\mathbb E_{\rm Haar}(1-w)^D\). The zero Haar mean of \(1-P\) puts it in \(W_D\). The numerator of the \(p_s\) moment of \((1-w)^{2D}\) is at most \(C_D(1+s)^{-2D-3/2}\), while its normalizer is at least \(c(1+s)^{-3/2}\) by one of the intervals above.

**PROVED.** Let \(d_{D,\beta}\) be the right side of (23) at \(s=6\beta\). In (22), replacing each fixed representation by all of \(W_D\) gives the suppression \(e^{-M_0 d_{D,\beta}/2}\). More generally suppose that, on the same product fibre, \(F\) lies in the sum of tensor spaces whose factors lie in \(W_D\) on *at least* \(M_0-k\) of the \(M_0\) links, with all other factors unrestricted. If \(k\le M_0d_{D,\beta}/2\), its exterior prediction norm divided by \(\|F\|_2\) is at most \(e^{-c M_0d_{D,\beta}}\). Indeed the single-link weighted projections onto \(W_D\) commute. The function belongs to the subspace in which at most \(k\) of their complementary projections occur. The squared norm of the constant vector projected onto this subspace is the probability of at most \(k\) successes in an independent Bernoulli sum with probabilities \(1-\|\Pi_{D,i}1\|^2\ge d_{D,\beta}\). Applying Markov's inequality to \(e^{-\sum B_i}\) bounds that probability by \(\exp[-(1-e^{-1}-1/2)M_0 d_{D,\beta}]\). Cauchy–Schwarz and integration give the assertion with half the exponent. This works without specifying in advance *which* \(k\) links a summand omits. At any fixed \(D\) it gives decay for \(M_0\) growing faster than \((1+\beta)^{2D}\). This suppression absorbs polynomial source normalizations when the exponent also dominates their logarithms.

## Testing the extension to unrestricted joint functions

**PROVED.** At one link the best bound for *all* Haar-centered functions differs substantially from (21). In \(L^2(p_s)\) the orthogonal complement of the Haar-centered space is spanned by \(D_s=dH/dp_s=Z(s)e^{-s w}\), with \(H\) Haar probability. Its inner product with \(1\) is one and its squared norm is \(Z(s)Z(-s)=Z(s)^2\). The squared distance of \(1\) to the Haar-centered space is exactly \(Z(s)^{-2}\). Its projection onto that space is
\[
                    h_s(q)=1-e^{-s w(q)}/Z(s).
\]
Both \(\mathbb E_s h_s\) and \(\mathbb E_s h_s^2\) equal \(1-Z(s)^{-2}\). The cap integral in (21) gives \(Z(s)^{-2}\le C(1+s)^3e^{-2s}\). Centering at the actual staple direction gives a gauge-invariant conditional formula, since the scalar in its exponent is the Wilson staple pairing. In particular a single nontrivial representation and an unrestricted sum of nontrivial representations have different prediction norms.

**PROVED.** This failure persists in a growing ordinary Wilson box and for finite label functions. Let \(I\) be a prescribed set of \(M_0\) links with no two on a common plaquette, with \(\limsup_{\beta\to\infty}\beta^{-1}\log(M_0+1)<12\). The side of the surrounding torus may grow, provided it fits the set. For the fluctuation-scale bins in (1) there are functions \(G\) of the labels with \(\|G-1\|_{L^2(\mu)}\to0\) with the following property. At each fixed assignment of labels outside \(I\), \(G\) is zero or is a product with zero Haar mean in at least \((1-o(1))M_0\) of the individual \(I\)-coordinates. The fraction is deterministic. Haar mean here is with the Haar probabilities of the bins. Thus a count of nontrivial Haar components on many links cannot replace the angular restriction in (22)–(23).

**PROVED.** Choose \(0<\epsilon<1\) such that \(\limsup\log(M_0+1)/\beta<12-2\epsilon\). At each \(i\in I\) compute \(\widehat S_i\) from representatives of its eighteen other links. All these labels belong to the exterior of \(I\). Keep the sites with \(|\widehat S_i|\ge6-\epsilon/2\). At large \(\beta\), \(|S_i-\widehat S_i|\le18\delta\) ensures \(|S_i|\ge6-\epsilon\) at every kept site and every exact exterior compatible with its labels. A discarded site has \(|S_i|\le6-\epsilon/4\) eventually, which forces \(\sum_{p\ni i}(1-w_p)\ge\epsilon/4\) because its six traces sum to \(U_i\cdot S_i\le |S_i|\). Thus the expected discarded fraction is \(O_\epsilon(\log(2+\beta)/\beta)\) by the ordinary plaquette estimate. If this fraction exceeds \([\log(2+\beta)/\beta]^{1/2}\), set \(G=0\). The event has probability tending to zero by Markov's inequality.

**PROVED.** Otherwise, at each retained site take \(E_i\) to be the union of bins meeting a cap of chord radius \(\beta^{-1/2}\) at \(-\widehat S_i/|\widehat S_i|\). Its Haar mass \(q_i\) is between \(c\beta^{-3/2}\) and \(C\beta^{-3/2}\). On \(E_i\) the chord distance to the true antipodal staple is \(O_\epsilon(\beta^{-1/2})\), so the density given the exact exterior is at most \(C_\epsilon(1+\beta)^{3/2}\exp[-2(6-\epsilon)\beta]\) there. Indeed its exponent is at most \(-\beta|S_i|+C_\epsilon\) and its normalizer is at least \(c(1+\beta)^{-3/2}e^{\beta|S_i|}\). Use \(h_i=1-\mathbf1_{E_i}/q_i\) and take \(G\) to be the product over the kept sites. Each \(h_i\) has Haar mean zero. Conditional on the exact exterior these factors are independent. Their means are between \(1-d\) and one, and their second moments are at most \(1+d\), where \(d=C_\epsilon(1+\beta)^3 e^{-2(6-\epsilon)\beta}\). The conditional squared error of the product from one is at most \(2M_0d+e^{M_0d}-1\). This tends to zero, proving the assertion after integrating and including the discarded exterior event.

**PROVED.** Centering does not rescue a prediction estimate based only on this count. If \(B\) is any centered exterior label reading bounded by one, let \(c_\beta=\mu(BG)/\mu(G)\). Then \((B-c_\beta)G\) stays centered, has the same conditional Haar cancellations and converges to \(B\) in Wilson \(L^2\) in the sense that their difference tends to zero. This follows from \(\mu G\to1\), \(|\mu(BG)|\le\|G-1\|_2\), and the triangle inequality. For instance one can take a nonconstant bounded label reading on a disjoint link with variance bounded away from zero, since that link's ordinary marginal is Haar and the mesh tends to zero. The exterior prediction of the resulting centered function has asymptotically its full norm. The multipliers can have large supremum norms. This construction rules out the proposed unrestricted Fourier-support estimate under the actual lattice measure. The auxiliary eigenfunction and continuum-state questions remain open.

## Angular bandwidth on contours growing exponentially in the coupling

**PROVED.** The loss in (23) can be reduced enough to let the permitted degree grow linearly in the Wilson parameter \(\beta\). Uniformly in \(D\ge1\), \(s\ge0\),
\[
       1-\|\Pi_D1\|^2\ \ge\
           {1\over C(D+1)}\left({cD\over D+s}\right)^{2D}.               \tag{24}
\]
Use the residual polynomial of (23) but now put \(h=D/(D+s)\). On \(1-3h/4\le w\le1-h/4\) the normalized \(p_s\) density is at least \(c(1+s)^{3/2}\sqrt h\,e^{-sh}\ge c e^{-D}/h\), since \((1+s)h\ge1\) and \(sh\le D\). In the same \(D+1\) subintervals choose points \(w_j\) with \(|P(w_j)|\le C e^{D/2}\sqrt{D+1}\|P\|_{L^2(p_s)}\). In increasing order their distances satisfy \(|w_j-w_k|\ge |j-k|h/[4(D+1)]\). The sum of the absolute interpolation weights on \([-1,1]\) is bounded by
\[
      [8(D+1)/h]^D\sum_{k=0}^{D}{1\over k!(D-k)!}
         =[16(D+1)/h]^D/D!\le(C/h)^D .
\]
Use \(D!\ge(D/e)^D\), absorb \(e^{D/2}\) into the base, and use \(\sup|P|\ge1\). Squaring gives (24).

**PROVED.** Suppose \(M_0\ge e^{\gamma\beta}\) for some \(\gamma>0\) and the counted links satisfy the disjoint-plaquette hypothesis of (22). There is \(\alpha(\gamma)>0\) such that for any integer \(1\le D\le\alpha(\gamma)\beta\) the product suppression for the full space \(W_D\) on those links is at most \(\exp[-c e^{\gamma\beta/2}]\) for all large \(\beta\). The same estimate with a changed absolute \(c\) holds when at most \(M_0d/2\) links per summand are exceptions, where \(d\) is the right side of (24) at \(s=6\beta\). Indeed \(D\log[C(1+6\beta/D)]\) increases with \(D\) for \(C\ge1\), and \(2\alpha\log[C(1+6/\alpha)]\to0\) as \(\alpha\downarrow0\). Choose it strictly below \(\gamma/2\), so \(M_0d\ge e^{\gamma\beta/2}\) eventually, including the polynomial prefactor. Apply the projection proof following (23). This establishes prediction decay on specified contours for growing bandwidth and arbitrary coefficient contractions. It leaves unrestricted the functions in which the contour spins cancel to the trivial representation.

## Fixing all straight coarse transports in the finite-label test

**PROVED.** For \(b>4,\ m=N/b\ge24\) let \(C_{z,\nu}\) be the straight product of the \(b\) fine links from coarse root \(z\) to coarse root \(z+\hat\nu\). Choose the tree in each wall group to contain the first \(b-1\) links of each of the four outgoing arms. These arms form a tree and extend to a spanning tree of the group. The reduced nontree matrix on the last edge of each arm is exactly \(C_{z,\nu}\). In the canonical Wilson fibre \(C_{z,\nu}=1\) for every \(z,\nu\), discard those fixed matrices, and bin all remaining reduced wall matrices at \(d_b\) as in (19). Denote the true marginal's normalized side-four cube constant by \(\widehat v_4(\mathbf1)\). Put
\[
 \eta_b=48(1+6\beta)^{3/2}
              \left({4\beta\over1+4\beta}\right)^{b-4},
 \qquad \theta_b=\left({1-\eta_b\over1+\eta_b}\right)^{4m^4}.
\]
For \(\eta_b<1\), the *ordinary* fine Wilson law satisfies
\[
       v_{10b+2}^{\rm inv}\ \ge\
          \theta_b\left({10b\over10b+2}\right)^4\,
                        {\widehat v_4(\mathbf1)\over200}.                \tag{25}
\]
All the retained matrices on this fibre have a based loop representation. If a reduced edge connects different roots, close it by the reversed straight coarse arm between them. Its product is one on the fibre. A common conjugation at the roots still acts on these matrix coordinates.

**PROVED.** In the Haar change of variables before (19) the arm products are individual Haar coordinates before multiplication by the positive cell factors. Evaluation of the factors at prescribed arm products, followed by normalization, gives the canonical disintegration, including at \(\mathbf1\). The same fibre can be obtained by solving for one fine link on each arm. Since this conditioning reads only wall links, the private cells are still independent given the exact walls and their conditional distributions are unchanged. In (16) every exterior private cell touching a resampled wall factor is included just as before. Relations among the raw wall links caused by conditioning do not affect that conditional-independence proof. Nonroot gauge transformations preserve the constraints. The \(p_v\) again have product Haar law independent of \(Q\), and \(M_W f\) depends only on \(Q\) when \(f\) is restricted from a full-gauge-invariant test. Fixing some factor arguments to one only decreases the preceding counts of variable sites and possible oscillations. Thus (16) and the lower-bound proof of (19) on this fibre give the side-\(10b\) fine inequality with constant \(\widehat v_4(\mathbf1)/200\) for these restricted tests. In particular it holds on such tests of the complement of the private straight-path interiors. Apply (9) of [row 1254](gap-solve29-astra62.md), based on the straight-path density estimate of Bhattacharjee, Bhattacharya, Lockwood and Romanov. Its \(\theta\) is exactly \(\theta_b\), and the outer minimum with one is redundant since \(\widehat v_4(\mathbf1)\le1\) by a one-group test. This proves (25) without approximating the constrained cell factors.

**PROVED.** The near-perfect adjacent *invariant* correlation from (20) persists in this pinned law if \(b/(1+\beta)\to\infty,\ \beta\to\infty,\ m^4\eta_b\to0\). Choose the ridge square away from the ends of the \(x_3,x_4\) intervals by at least \(b/5\), still of side at least \(b/3\). Every vertex in it is at fine lattice distance at least \(b/5-O(1)\) from the union of the straight coarse paths, since membership in a path requires three coordinates on the coarse grid. Of the first \(c'b\) links along the long tree return, starting at its endpoint in the square, a positive fraction have disjoint plaquettes and avoid every pinned path by choosing \(c'\) sufficiently small. The prescribed products and the exterior reduced labels read none of these selected links. Conditional on the other raw links under the canonical fibre, their law is again the independent product of the ordinary Wilson staple densities. This follows either by the product constraint being a function of the complementary links, or by solving the path constraints using only complementary links in the Haar disintegration. The estimate (20) therefore holds on this fibre as well. The elementary plaquette comparing the two paths is measurable off all private path interiors. Its mean deficit on the fibre is at most \(\theta_b^{-1}\) times its ordinary mean by (6) of row 1254. Since \(\theta_b\to1\), the two scalar tests again have conditional variance tending to \(1/4\) and conditional correlation tending to one in probability. Pinning all interroot transports still leaves this shared-path effect.

## Recovering the local curvature signal from the two adjacent readings

**PROVED.** The part of the joint law of \((A,B)\) from (20) visible off its long tree return can be identified explicitly. Work in the ordinary Wilson law or the identity fibre of (25). Use the raw direct and detour transports \(X,Y\) and a common tree return \(T\), so that \(A=w(XT)\), \(B=w(YT)\). Put \(c_p=w(XY^{-1})\), the elementary plaquette half-trace. Choose the disjoint-plaquette set \(I\) in the return as above. With \(\epsilon_b=C\exp[-c_0 b/(1+\beta)]<1\), the conditional law given the exact \(I^c\) is bounded above and below, as measures on the pair of real readings, by \(1+\epsilon_b\) and \(1-\epsilon_b\) times the law of
\[
              (u,\ c_p u+\sqrt{1-c_p^2}\,v),                            \tag{26}
\]
where \((u,v)\) is uniform in the unit disk. Indeed the conditional law of \(T\) is within \(\epsilon_b\) of density one relative to Haar by the same independent-link convolution as in (20). Under Haar, \(w(XT)\) and \(w(YT)\) are scalar products of a uniform unit four-vector with unit directions of inner product \(c_p\). A rotation gives (26). For the disk law write the four-vector as \((\cos\varphi\cos t,\cos\varphi\sin t,\sin\varphi\cos s,\sin\varphi\sin s)\), with \(0\le\varphi\le\pi/2\). Its volume element is proportional to \(\sin\varphi\cos\varphi\,d\varphi\,dt\,ds\). The projected radial law is \(2r\,dr\). This includes the degenerate pairs at \(c_p=\pm1\) by the same map. The measure comparison holds for all bounded Borel readings at once, including readings with arbitrary angular frequency.

**PROVED.** Write \(D_p=1-c_p\) and \(Z_p=2(A-B)^2\). Conditional on \(I^c\), for every integer \(k\ge1\),
\[
 (1-\epsilon_b)\,\frac{(2k)!}{k!(k+1)!}\,D_p^k
 \ \le\ \mathbb E[Z_p^k\mid I^c]\ \le\
 (1+\epsilon_b)\,\frac{(2k)!}{k!(k+1)!}\,D_p^k .                     \tag{27}
\]
Under Haar, the difference of the two scalar products is distributed as \(\sqrt{2D_p}\,u\). The squared reading is consequently \(4D_p u^2\). Integrating \(u^{2k}\) against \((2/\pi)\sqrt{1-u^2}\,du\), or integrating by parts recursively, gives \(\mathbb E(4u^2)^k=(2k)!/[k!(k+1)!]\). Positivity and (26) give (27) with relative error independent of \(k\). In particular the conditional mean of \(Z_p\) recovers \(D_p\) to this relative error and its Haar conditional second moment is \(2D_p^2\). For any integrable \(F\) measurable off \(I\),
\[
 |\operatorname{Cov}(Z_p,F)-\operatorname{Cov}(D_p,F)|
 \le\epsilon_b\{\mathbb E(D_p|F|)+\mathbb E D_p\,\mathbb E|F|\}.        \tag{28}
\]
This follows by conditioning \(Z_p-D_p\) and centering \(F\). The separate correlations of \(A\) and \(B\) obey (20). Thus their joint bounded quadratic reading transmits a genuine local energy observable through the same conditional averaging.

**PROVED.** The assertion also holds with both members of a separated correlation measured this way. Take two copies of the construction in cells whose tree paths and plaquette detours are disjoint and have no common incident plaquette between the chosen sets of private links. One may translate the construction in the ordinary torus, or use disjoint cells with the same prescribed tree in the identity fibre. Given the complement of the two private sets, the selected links have independent Wilson one-link laws and the two pushforwards are conditionally independent. Each \(D_p,D_q\) is measurable in this complement. Hence
\[
 |\operatorname{Cov}(Z_p,Z_q)-\operatorname{Cov}(D_p,D_q)|
 \le (2\epsilon_b+\epsilon_b^2)
               [\mathbb E(D_pD_q)+\mathbb E D_p\,\mathbb E D_q].         \tag{29}
\]
Apply (27) with \(k=1\) separately to the product and the product of means. Reading the loops using the finite bins changes \(Z_p\) by at most \(C d_b\) pointwise, by boundedness and the trace Lipschitz estimate. The mesh in (19) or (25) can be decreased to any \(d\le d_b\) while preserving the comparison constants, since all within-bin oscillations only decrease. At \(ab\to L>0,\ \beta=O(\log(1/a))\), (29)'s exponential error is smaller than any fixed power of \(a\), and \(d\) can be chosen to have the same property at any prescribed finite power. Thus polynomial normalizations in a separated plaquette two-point function do not suppress this screened joint reading relative to the corresponding local curvature signal.

**OPEN.** Equations (26)–(29) identify what must be controlled even for two fundamental loops and a quadratic reading. At fixed exterior their joint prediction is a function of one ordinary plaquette trace. At separated points the covariance of the resulting deficits remains a Wilson energy-density covariance. The conditional Haar integrations above supply no physical-distance decay rate for it. The same problem remains for higher local gauge-invariant tensors, which are needed for the full physical Hilbert space.

**PROVED, reflected forms.** There is an exact joint matrix identity \(w(Q(X)Q(Y)^{-1})=c_p\), by cancellation of the common endpoint frames. Equation (27) gives a stronger statement about readings that use only one scalar trace from each side. Put \(\Delta_p=Z_p-D_p\). Place its full support in the positive-time half of the ordinary reflection-positive torus, clear of the reflection plane and its periodic translate. Whenever a reflected reading \(F\) is supported in the disjoint negative half,
\[
       |\mathbb E(\overline F\,\Delta_p)|
                \le\epsilon_b\,\mathbb E(|F|D_p).
\]
In particular let \(O_j=\sum_p t_{p,j}D_p\), \(O'_j=\sum_p t_{p,j}Z_p\), with \(\sum_p|t_{p,j}|\le a_j^{-K}\) for fixed \(K\). Each \(p\) may use a translated and rotated square and its own tree, provided every support of the enlarged readings lies strictly in the positive half. These comparisons are all in the same ordinary Wilson measure with auxiliary choices made separately for each reading. With \(ab\to L>0,\ \beta=O(\log(1/a))\), the centered lattice reflection seminorm of \(O'_j-O_j\) tends to zero. Indeed \(0\le D_p\le2,\ 0\le Z_p\le8\), and the absolute value of the centered reflected form is at most \(C\epsilon_b(\sum_p|t_{p,j}|)^2\) by (28). The same conclusion holds after binning with \(d=o(a^{2K})\). In contrast, each of the two *individual* long trace readings has centered reflected squared seminorm \(O(\epsilon_b)\) by (20). Thus if a normalization of this local energy produces a nonzero continuum vector, the quadratic readings produce the same vector. Vanishing of the two separate vectors would not eliminate this obstruction to a gap proof. No existence or nonvanishing of the proposed energy vector is assumed in the seminorm estimate.

## Testing a uniform pinned-wall estimate in the quadratic gauge theory

**GUIDE.** [Row 1222](gap-solve24-astra62.md), after (14), finds a long-wavelength Abelian curvature reading predictable from each of three walls in a box. I test the particular ordinary cube-resampling constant left by (25) on a *periodic* gauge field, with one wall grid and exactly the straight-transport constraints used in (25). This comparison asks whether those constraints and the curl action suffice by themselves.

**PROVED, noncompact Abelian comparison.** On the \(N^4\) torus take real edge potentials with density proportional to \(\exp(-\|dA\|_2^2/2)\) modulo gauge, where \(d\) is the oriented plaquette curl. Prescribe zero sum on each straight coarse arm. In each half-open cell choose the wall tree of (25) and extend it to a spanning tree of all vertices in that cell. Fix its tree edges to zero. The last edge of each arm is then fixed to zero as well. The Gaussian precision is positive on the remaining coordinates. Indeed if \(dA=0\), a potential on the universal cover is a gradient by interchange of consecutive coordinate steps and cancellation of inverse steps. Its periods vanish since the straight coarse paths have zero sums and concatenate to give each period. The potential descends to the torus, where it is constant per tree, with constants equal on adjacent roots. Thus \(A=0\) in these coordinates. Let \(W_{\rm lin}\) consist of the free wall edges in this gauge and let \(v_4^{W_{\rm lin}}\) be their exact marginal's side-four cube Poincaré constant. Along \(b\to\infty,\ N/b\to\infty\),
\[
                   v_4^{W_{\rm lin}}\ \le\
                        C\big[(b/N)^2+b^{-1}\big].                     \tag{30}
\]

**PROVED.** Use the transverse reading \(f(A)=\sum_x\cos(2\pi x_2/N)A_1(x)\). It is unchanged by adding any periodic gradient, by summation along the 1-direction. Use as variational test field \(A_1^0(x)=\cos(2\pi x_2/N)\) except on the straight coarse 1-arms, where it is zero, and \(A_\nu^0=0\) for \(\nu\ne1\). This field obeys the path constraints and can be put in the chosen tree gauge by a gradient with zero values at the roots. Both \(f(A^0)\) and \(dA^0\) are preserved. The smooth wave gives \(N^4/2\) to \(f\) and has squared curl at most \(C N^4/N^2\). Erasing its values on the straight lines changes at most \(N^4/b^3\) edges by at most one and each enters six plaquettes. It follows that \(f(A^0)\ge cN^4\) and \(\|dA^0\|^2\le C N^4(N^{-2}+b^{-3})\). The inverse of the positive quadratic precision gives
\[
             \operatorname{Var}f
          =\sup_{h\ne0}|f(h)|^2/\|dh\|^2
          \ge cN^4/(N^{-2}+b^{-3}).
\]

**PROVED.** For a variation \(h\) supported in a side-\(q\) cube the same quotient is at most \(Cq^6\). Choose a periodic discrete antiderivative \(J(x_2)\) for the cosine, with the sign chosen so that \(J(n-1)-J(n)=\cos(2\pi n/N)\). Summation by parts gives \(f(h)=\sum_x J(x_2)(dh)_{21}(x)\), as the other term telescopes in \(x_1\). Subtract a constant from \(J\) so \(|J|\le q+2\) on the support of \(dh\), using its one-step increments bounded by one. There are at most \(Cq^4\) contributing plaquettes. Cauchy–Schwarz gives the quotient bound. For the Gaussian conditional law on a cube the variational supremum over its allowed variations is precisely the conditional variance of the linear reading, by completing the square. Hence \(\mathcal E_q(f)\le C N^4 q^2\). Conditional on \(W_{\rm lin}\), private cell variables are independent because each plaquette lies in a closed cell and tree constraints are individual fixed edge values. The part of \(f\) from each private cell has conditional variance at most \(Cb^6\) by the same calculation. Consequently \(g=\mathbb E[f\mid W_{\rm lin}]\) satisfies \(\operatorname{Var}g\ge\operatorname{Var}f-C N^4 b^2\), at least half the full variance eventually. The proof of (16) uses just this local cell disintegration and applies also in the fixed coordinates, giving \(\mathcal E_4^{W_{\rm lin}}(g)\le16\mathcal E_{8b}(f)\). Division by the variance bound proves (30).

**PROVED.** For each finite torus this upper test can be approximated by functions of finite bin labels with the same limiting quotient as the bins refine. Use increasing finite partitions of the real line generating its Borel field, in every free wall coordinate. Project \(g\) onto all labels at level \(n\). Its projection next onto the exterior labels of any cube is exactly the exterior label projection of \(g\). The two projections converge in \(L^2\) to \(g\) and to its exact exterior projection, respectively, by density of simple functions from the generating partitions. Only finitely many cubes enter at this torus. The quotient therefore converges. In this comparison pinning all path products, retaining only wall loops, and observing at arbitrarily fine finite resolution can coexist with a vanishing cube constant. For compact \(SU(2)\), the precision and the linear variational formula used in (30) are unavailable. The interacting curvature estimate in (25) remains open.

## Arbitrary trees carrying smeared colour curvature in the Wilson law

**GUIDE.** [Row 1231](gap-solve26-astra62.md), (7)–(9), transports plaquette colour to one root and compares its singlet readings to a Gaussian on short spatial scales. The calculation below tests this class directly at fixed physical wavelengths, for arbitrary tree paths. I use the one-link Fourier estimate of row 1145. Rows 1161 and 1222 already select independent links simultaneously on a straight tiling by an eight-periodic rule. The selection below applies to arbitrary paths even if they run side by side for their whole length.

**PROVED.** Suppose a finite list of oriented simple path segments is given and each has at least \(r\) fine links private to that segment. A private link is used once there and by none of the other segments or local insertions under consideration. Two private links in different segments may share a plaquette. There is a simultaneous deterministic choice of at least \(\lfloor r/256\rfloor\) private links on every segment such that *no* plaquette meets two chosen links. To see this, partition \(r\) eligible links per segment into disjoint groups of 256, discarding remainders. For the existence argument draw an independent uniformly chosen member of each group. For each plaquette-neighbour pair in distinct groups, the bad event that both are selected has probability \(p=256^{-2}\) and shares random inputs with at most \(D=2\cdot256\cdot18\) other events. Bad pairs in one group are impossible. Put \(x=2p\), so \(p\le x(1-x)^D\) by \((1-x)^D\ge1-Dx\ge1/2\). The elementary local lemma of Erdős and Lovász gives positive probability of avoiding every event. For completeness, by induction on the size of a conditioning avoidance list, the conditional probability of any new bad event is at most \(x\). Split the list into non-neighbours and at most \(D\) neighbours. The new event is independent of the joint non-neighbour list, and the conditional probability of avoiding the neighbours one at a time is at least \((1-x)^D\) by the shorter-list bounds. If there are no neighbours use independence directly. This proves the induction and positivity of the full avoidance probability. It is an existence argument on finite sets.

**PROVED.** For \(J\) such segments under the ordinary Wilson law, condition on the exact complement of the simultaneous selection. The segment products are independent, and for \(r\ge C(1+\beta)\) each has density \(1+O(e^{-c r/(1+\beta)})\) relative to Haar, uniformly in the exterior and orientations. This is the convolution bound used in (20) with at least \(\lfloor r/256\rfloor\) independent factors per segment. The full product density lies between \(\exp[-CJ e^{-c r/(1+\beta)}]\) and \(\exp[CJ e^{-c r/(1+\beta)}]\) after enlarging \(C\) in the lower cutoff on \(r\). In any joint bounded reading replace those products by independent Haar averages, holding its other raw arguments fixed, and call the resulting function \(\mathcal A f\). For an insertion \(F\) measurable off the selected links this gives
\[
 |\mathbb E[(f-\mathcal A f)F]|
      \le \big(\exp[CJ e^{-c r/(1+\beta)}]-1\big)
                         \|f\|_\infty\,\mathbb E|F|.                    \tag{31}
\]
The same inequalities hold on the identity fibre of (25) when all its prescribed paths avoid the selected links, by the canonical Wilson disintegration there. The reading may reuse a segment product many times as one matrix argument. No bound on its representation degree is necessary for (31).

**PROVED.** For a rooted spatial tree, attach \(k\) based local colour readings to marked vertices. Each transforms by a group action at its own vertex, for example simultaneous adjoint action on the imaginary parts of finitely many based plaquettes. Transport each reading to the root along the tree and apply a bounded jointly rotation-invariant function. Retain only the subtree from the root to the marks, suppressing unmarked degree-two vertices. Split also at both endpoints of any tree edge used in a local reading. For fixed \(k\) and a bounded number of local links per mark, the resulting tree has a bounded number \(J_0\) of segments. This follows by counting the branch vertices by the leaves of the original minimal tree and adding at most two vertices per used edge. Replace the transports on its segments of length greater than \(r\) by Haar integrals as in (31). Their interior links are private by construction. The resulting function depends on gauge-invariant data in separate connected components of the tree left by the cuts. Each component containing a mark has diameter at most \(J_0 r\), plus the radii of its local insertions. To see this, choose an anchor in each component and transport its local readings to that anchor using the uncut paths. Conditional on these data, a cut edge attaches the child component by a Haar rotation, unaffected by its fixed endpoint transports. Recursively the accumulated child rotations are independent Haar relative to a fixed root rotation, since conditional on each parent left translation preserves the new Haar variable. Joint rotation invariance also permits averaging the root rotation. Thus the output is a function of the orbit of the data within each component, with the components rotated independently. For a multilinear contraction, a component whose tensor product has zero invariant subspace gives identically zero, by the Haar projection. For a singleton in the adjoint representation this always occurs. Components with singlets can contribute, even if widely separated from one another.

**PROVED.** In particular take one tree on a spatial slice, \(v_x=\operatorname{Im}U_{p_x}\) at a chosen elementary plaquette based at \(x\), and \(T_x\) the path from the common root to \(x\). For the bilinear obtained by squaring a smeared vector, set
\[
 B_{\alpha}=\left|\sum_x\alpha_x\operatorname{Ad}(T_x)v_x\right|^2
   =\sum_{x,y}\alpha_x\overline{\alpha_y}\,
                   v_x\mathbin{\cdot}\operatorname{Ad}(T_x^{-1}T_y)v_y .
\]
Take real coefficients or the complexified norm in this identity. The common prefix cancels, leaving the simple tree path between \(x,y\). Let \(B_{\alpha,\le r}\) be the same sum with tree distance at most \(r\). Every summand retained is an individually gauge-invariant observable of diameter at most \(r+4\) in fine units. For any \(F\) supported off the slice, or on links disjoint from the selected path links of all omitted pairs,
\[
 |\mathbb E[(B_\alpha-B_{\alpha,\le r})F]|
 \le C e^{-c r/(1+\beta)}\Big(\sum_x|\alpha_x|\Big)^2\mathbb E|F|
 \quad\text{for } r\ge C(1+\beta).                                     \tag{32}
\]
For each omitted pair exclude the at most eight links used by its plaquettes, then choose at least \((r-8)/19\) remaining path links with no shared plaquette. At fixed complement the two endpoint vectors have magnitude at most one and the Haar integral of the adjoint matrix on the connecting path is zero. Use the same one-path density bound as in (20) and sum. Pairs may use different selected links. At logarithmic bare coupling and polynomial coefficient sum in \(1/a\), one can choose \(r=C_K(1+\beta)\log(1/a)\) so \(ar\to0\) and the error vanishes even against polynomially growing separated tests. In particular the omitted sum has vanishing centered reflected seminorm on a slice clear of the reflection plane. This follows by taking the reflected omitted sum as a bounded test with norm at most \((\sum_x|\alpha_x|)^2\) and increasing \(C_K\).

**ARGUED.** Equations (31)–(32) remove the relative colour carried on long bare unbranched paths as a candidate for the transverse wave in (30). They leave sums of local singlet observables and correlations between separate singlet components. The local plaquette recovery in (27) exhibits one such component directly in the interacting theory. The size of a connected correlation between two such components is not controlled by the Haar average over the transport between them.

## The remaining physical estimate

**PROVED, conditional on the following two inputs.** Take even periodic Wilson tori with \(a_j\downarrow0,\ a_jN_j\to\infty,\ b_j\mid N_j,\ a_jb_j\to L\in(0,\infty)\) and \(m_j^4\eta_{b_j}\to0\), \(m_j=N_j/b_j\). For instance the last condition follows with \(N_j\) at most polynomial in \(1/a_j\) and \(\beta_j=O(\log(1/a_j))\). Suppose the exact pinned finite-label laws of (25) have
\[
                       \liminf_j\widehat v_4(\mathbf1)=v_*>0.            \tag{33}
\]
Suppose also that a nontrivial continuum Yang–Mills theory with the required local gauge-observable space has been constructed on this sequence. More precisely, for a family of vacuum-subtracted vectors spanning densely in \(\Omega^\perp\), require matched bounded gauge-invariant positive-time insertions \(F_j\) in fixed physical boxes, convergence of their centered reflected forms at every positive physical time padding to \(\langle u,e^{-tH}u\rangle\), \(H\ge0\), and
\[
        \log(2+\|F_j\|_\infty)+\log(2+|\operatorname{supp}F_j|)
                          =o(N_j/b_j).
\]
Then the physical Hamiltonian on this space satisfies
\[
                 H|_{\Omega^\perp}\ \ge\ {v_*\over78125\,e^2 L}.         \tag{34}
\]
Indeed \(\theta_{b_j}\to1\), so any \(v<v_*/200\) works eventually in the fine cube inequality at side \(10b_j+2\), of physical size eventually below every \(\ell>10L\). The finite-torus estimate of Bhattacharjee, Bhattacharya, Lockwood and Romanov and the matched-diagonal reflection argument of [row 1254](gap-solve29-astra62.md), (1)–(4), give \(H|_{\Omega^\perp}\ge16v/(625e^2\ell)\). Take \(v\uparrow v_*/200\), \(\ell\downarrow10L\). This is a conditional lower bound in inverse physical length. The auxiliary heat-bath operator appearing in (3) is a different operator.

**OPEN.** I have no lower bound uniform in \(j\) for (33). The local averaging estimate controls a fixed-label fibre, and the long-path estimates control the part of a colour reading that changes under averaging that path. Even on an ordinary weak-coupling exterior, a pair of such readings can recover a local action-density insertion with its long-distance correlations intact. The quadratic gauge comparison gives a vanishing coarse constant with the same straight-path constraints. A proof for \(SU(2)\) would have to bound the interacting gauge-invariant sector left by these calculations, or obtain the spectral exclusion by a different argument. Construction and full Jaffe–Witten identification of the matched continuum theory are also open in this work. All estimates here are analytic. No independent check of this row has been made.

RESULT — OPEN. Row 1272. Equation (25) gives a sufficient finite-volume estimate using finite labels on gauge-reduced cell boundaries after fixing every straight coarse transport. Equations (26)–(29) recover elementary curvature correlations from paired long loops. The uniform interacting bound (33) and the matched nontrivial continuum construction remain open. This work does not prove the four-dimensional SU(2) Jaffe–Witten mass gap and grants no scientific status.
