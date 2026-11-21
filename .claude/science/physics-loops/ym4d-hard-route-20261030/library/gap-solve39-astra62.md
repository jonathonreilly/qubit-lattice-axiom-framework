## Repo search

GUIDE. Row 1323, research at `f479e9b03`. The row-specific prior note is absent. First locate the strongest overlapping Wilson bounds and their hypotheses. Then choose an infrared estimate, test it on the actual measure and record exactly what follows in the physical limits.

GUIDE. The lead's November 8 search of main and PRs 10114, 10133, 10134 and 10141 found ultraviolet and finite-cutoff results. I checked the later gap-specific hits against the source objects. On main at `8b11ae2bb9`, Theorem ZD-c in `research/mass-gap/library/gap-phys-seed.md`, lines 311–329, relates the physical thermal seed to the finite-size spectral edge and a free-energy bound. PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149, has the finite-coupling one-step plaquette witness and contraction for \(0<\beta\le1/32\). Grok's PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–90, leaves the crossover and source transport open. PR 10134, `mass-gap-interface.md`, I1–I5, distinguishes a nonempty excited sector, the spectral threshold and identification. PR 10141, `fp1.md`, lines 299–315, controls a constrained classical minimizer. [Lead's search](prior/repo-search-2026-11-08.md)

GUIDE. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the physical transfer trace in the outline at lines 2315–2335. They explain the limits of clustering and scalar reconstruction at 581–599, 3712–3720 and 31858–31882. CA-I lines 2704–2712 and 3213–3222 explicitly leave the physical gap open. Both texts are at `31a47c543775`. The outline index, its neighbouring rows and its obligations locate these passages. Row 1218 locates the full thermal doubling criterion of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. Their hypothesis on a physical window of shapes is the relevant one here. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712) · [Row 1218](prior/gap-onebound-read-sol.md)

GUIDE. Row 1149, §7, already counts electric centre parities and shows that discarding their coherences can change the two-period ratio. Row 1236, (21), gives a limiting one-link electric distribution on its low-energy band in the electric half-step convention. Row 1321, (15)–(18), reads the relative closing condition of two replicas but leaves the probability of each closure open. The row 1322 check file is absent at this pin. The one-link character sine transform is also on file. I found no assignment in the open registry for restricting the *integer dimensions* of electric representations on selected links to multiples of \(q\ge3\) while preserving the thermal test. [Electric parities](gap-solve4-astra62.md) · [One-link law](gap-solve27-astra62.md) · [Character transform](gap-descent-sign-check-astra.md) · [Replica closure](gap-solve38-astra62.md)

## Choice of attack

GUIDE. Try to bound the thermal ratio by moving the physical transfer into an electric subspace in which every selected link has large Casimir. This would put the explicit electric convolution at our disposal. First determine whether sampling one congruence class of spins can preserve the one-period trace and its two-period sewing on the *same* Wilson measure. Then test the dynamical step with the intervening magnetic weights retained. The separation scale is a fixed physical time \(aT\) on a fixed physical box, with \(a\downarrow0\) and \(\beta\to\infty\).

OPEN. The target is a nontrivial four-dimensional SU(2) Yang–Mills vacuum theory on \(\mathbb R^4\), with all the required observables, \(\ker H=\mathbb C\Omega\), \(\Omega^\perp\ne0\), and a common \(m>0\) such that \(H|_{\Omega^\perp}\ge m\) in physical units. All new arguments below are author-side research.

## Sampling the spin of a link

GUIDE. Use probability Haar measure on each spatial link of a finite periodic three-dimensional box, all sides at least four. Write \(w(g)=\tfrac12\operatorname{tr}g\), \(\theta(g)=\arccos w(g)\), and give \(SU(2)=S^3\) its unit round metric. The physical space is the vertex-gauge-invariant subspace of this link \(L^2\) space. Let \(K=M C P_{\rm g}M\) be the positive transfer on a spatial slice. Here \(M=\exp[-\tfrac\beta2\sum_{p\ {\rm spatial}}(1-w(U_p))]\), \(P_{\rm g}\) averages vertex gauges and \(C\) is the product of electric convolutions with normalized kernel proportional to \(\exp(\beta w)\). Integrating the temporal links gives the torus trace, up to one scalar per time step which cancels from all ratios below. The placement of \(M\) gives the ordinary spatial Wilson marginal at each sampled end. This is the other ordering of the two half steps in Sussman and Alpoge's GL8.

PROVED. On one link let \(D\) have eigenvalue \(d=2j+1\) on the Peter–Weyl space of spin \(j\), including both matrix indices. For integer \(q\ge2\) put \(J_q=\mathbf1_{q\mid D}\). If a spherical cap has radius \(r<\pi/q\) and \(W\) is multiplication by its indicator, then
\[
                    W J_q W=q^{-1}W.                                      \tag{1}
\]
This also holds with \(W\) a subcap, or with the cap centre chosen from all the other links. In particular \(W=\mathbf1_{\theta(U_p)<r}\) works for any elementary plaquette using the link once. The projection \(J_q\) commutes with both end gauges.

PROVED. For \(0<t<\pi\) let \(S_t f(x)\) average \(f(xg)\) over the conjugacy sphere \(\theta(g)=t\), with mass one. By Schur's lemma the scalar on dimension \(d\) is \(\sin(dt)/(d\sin t)\). Indeed the representation of degree \(d-1\) in two variables has eigenvalues \(e^{i(d-1-2k)t}\), \(0\le k<d\), whose sum gives this character. Thus the derivative of \(\sin(t)S_t\) in matrix elements is \(\cos(tD)\). This holds for arbitrary \(L^2\) test vectors by the bound one on the scalar difference quotients and the orthogonal representation expansion. For two tests supported in the cap, \(\langle f,S_t h\rangle=0\) throughout \(2r<t<\pi\) by the triangle inequality. Hence \(W\cos(tD)W=0\) there. At \(t=\pi\), \(\cos(\pi D)\) is minus the antipodal translation, which also has zero compression. For \(\pi<t<2\pi\) use \(\cos(tD)=\cos((2\pi-t)D)\). Finally
\[
              qJ_q=I+\sum_{h=1}^{q-1}\cos(2\pi hD/q).
\]
Every angle in the sum has distance at least \(2\pi/q\) from \(2\pi\mathbb Z\). This proves (1). With other links fixed, the plaquette is a left and right translate of the selected link or its inverse, so its cap has the required radius. The argument by fibres proves the last case. The scalar on each Peter–Weyl space commutes with all left and right translations.

PROVED. Select \(m\) distinct pivots \(e_i\) and an elementary spatial plaquette \(p_i\) through each, with \(p_i\) containing no other pivot. The \(p_i\) are distinct. Write \(J=\prod_i J_{q,e_i}\), \(W_i=\mathbf1_{\theta(U_{p_i})<r}\), \(W=\prod_iW_i\). Since \(W_i\) commutes with every other pivot projection, successive applications of (1) give \(WJW=q^{-m}W\). Thus \(q^{m/2}JW\) is an exact isometry on the subspace \(W\mathcal H\), where \(\mathcal H\) can be the physical space. These operators also preserve the sector invariant under spatial centre flips, since each \(p_i\) is contractible. This statement includes all angular modes of the selected links.

## Repeated insertions in the Wilson transfer

GUIDE. I use the Wilson bound for prescribed bad plaquettes from row 1155, (9), checked in row 1156. For any finite set \(S\) of distinct spacetime plaquettes on the periodic rectangles in use, its statement is
\[
 \mathbb E\exp\!\left(c_0\beta\sum_{p\in S}(1-w(U_p))\right)
                  \le C_0^{|S|},\qquad c_0=1/8 .                         \tag{2}
\]
The source chooses one direction shared by the marked plaquettes as transfer time, halves their electric couplings, and uses the ordering of the normalized one-bond multipliers and trace Hölder. Ordinary Hölder combines four direction classes. The Haar normalization ratio at \(\beta/2,\beta\) is bounded by an absolute constant. This argument works on rectangular periodic lattices, including repeated copies of a mark at distinct times. GL3 gives the one-bond spectrum. [Row 1155, (9)](gap-solve7-astra62.md) · [Check, item 17](gap-solve7-check-opus.md) · [Multiplier ordering](gap-solve4-astra62.md) · [Sussman–Alpoge, GL3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2218)

PROVED, using (2). Put \(T=bk\), with positive integer slab thickness \(k\), sample count \(b\) and \(T\ge4\). Let \(K_* = K\) on the full physical space. The centre-neutral choice is specified below. For the same \(m\) pivots at every sample put \(B_k=q^m J K_*^k J\) on \(J\mathcal H_*\). Define \(u=4c_0\beta/(9q^2)\) and
\[
 \delta_q=2\sqrt{C_0}\sum_{h=1}^{q-1}
             e^{-u\min(h,q-h)^2}
       \le {4\sqrt{C_0}\,e^{-u}\over 1-e^{-u}} .
\]
Then
\[
 \left|{\operatorname{Tr}B_k^b\over \operatorname{Tr}K_*^{bk}}-1\right|
                         \le (1+\delta_q)^{mb}-1.                        \tag{3}
\]
All traces include multiplicities. No factor equal to the number of states or to the spatial volume occurs in the error.

PROVED. Expand \(qJ_{q,e}=I+\sum_{h=1}^{q-1}C_{e,h}\) with \(C_{e,h}=\cos(2\pi hD_e/q)\). For a marked factor choose \(t_h=2\pi\min(h,q-h)/q\), \(r_h=t_h/3\) and its cap \(W_e=\mathbf1_{\theta(U_{p_e})<r_h}\). Write \(L_e=I-W_e\). The spherical-mean argument for (1) gives \(W_e C_{e,h}W_e=0\). Hence \(C_{e,h}=L_e C_{e,h}+W_e C_{e,h} L_e\). In a product of \(s\) chosen factors on one slice this gives \(2^s\) terms \(L_X O L_Y\). Here \(X,Y\) partition the marks, \(L_X=\prod_{e\in X}L_e\), and \(\|O\|\le1\). The pivot condition permits moving the bad indicators through every factor at a different pivot. All factors preserve physical gauge invariance.

PROVED. Write \(\|\cdot\|_p\) for the Schatten norm. At one sample,
\[
 \|L_X K^{k/2}\|_{2b}^{\,2b}=
       \operatorname{Tr}(K^{k/2}L_XK^{k/2})^b .
\]
Dividing by \(\operatorname{Tr}K^{bk}\) gives the periodic Wilson probability that the specified plaquettes are bad at *all* \(b\) sample times. For \(X=\varnothing\) it gives one. Otherwise apply (2) and the exponential Markov bound at thresholds \(1-\cos r_{h_e}\). Thus
\[
 {\|L_X K^{k/2}\|_{2b}\over(\operatorname{Tr}K^{bk})^{1/(2b)}}
    \le \prod_{e\in X}\sqrt{C_0}\,
         e^{-c_0\beta(1-\cos r_{h_e})/2}.                                \tag{4}
\]
The same bound holds on the right of the sandwich by taking the adjoint. Hölder bounds the \(b\)-norm of \(K^{k/2}L_X O L_YK^{k/2}\) by the product of the two norms. Since \(1-\cos r\ge2r^2/\pi^2\) for \(0\le r\le\pi\), summing the two choices of side and the angles costs at most \(\delta_q\) per mark. For a term with possibly different marks on the \(b\) slices, trace Hölder bounds its absolute trace by the product of these \(b\)-norms. The denominators in (4) multiply to \(\operatorname{Tr}K^{bk}\). Summing over subsets of the \(mb\) positions other than the empty subset proves (3). This argument uses positive Wilson probabilities only in (4). The cosine operators themselves have operator norm at most one and can have signed matrix elements.

PROVED. The same bound holds on the spatial centre-neutral sector with \(C_0\) replaced by \(8C_0\). Let \(P_+\) average the eight spatial centre flips. It commutes with \(K,J,W_e\). For \(H_X=K^{k/2}L_XK^{k/2}\ge0\), one has \(\operatorname{Tr}(P_+H_X^b)\le\operatorname{Tr}H_X^b\). The homogeneous denominator satisfies \(\operatorname{Tr}(P_+K^{bk})\ge\operatorname{Tr}K^{bk}/8\), since each twisted trace is a positive Wilson integral and the identity flip occurs. For nonempty \(X\) the extra factor eight in the probability is at most \(8^{b|X|}\), and for the empty set the quotient equals one. This proves (4) and then (3) on this sector, including the signs in the subsequent Hölder bounds.

## Physical time and the low-lying eigenvalues

PROVED. Define the full thermal doubling defect by
\[
       \Psi(K,T)=2\log\operatorname{Tr}K^T-\log\operatorname{Tr}K^{2T}.
\]
It is invariant under multiplying \(K\) by a positive constant. Suppose \(aT\to\tau>0\), \(T=bk\) on the chosen grids and \(mb\,\delta_q\to0\). Apply (3) with \(b\) and \(2b\), using the same \(B_k\) in both. The two relative trace errors tend to zero, so
\[
                       \Psi(B_k,b)=\Psi(K_*,T)+o(1).                      \tag{5}
\]
For example, on a dyadic time grid with \(\beta\to\infty\), \(\beta=O(\log T)\), take \(q=\max(3,\lfloor\beta^{1/4}\rfloor)\), \(m=\lceil\beta\rceil\), and take \(b\) the largest power of two at most \(\beta^2\). These obey the hypothesis since \(u\) grows at least as a positive constant times \(\sqrt\beta\). Disjoint plaquettes of one orientation on a physical cube supply more than \(m\) pivots eventually. Here \(ak\to0\). Equation (5) also holds uniformly over a window of rectangles when the same bound on \(mb\,\delta_q\) holds throughout. To infer the published thermal condition from a compressed one on such a window requires margin in the logarithmic bound, uniformly on that window.

PROVED. There is an operator estimate on the genuine transfer underneath the comparison of traces. Set \(\lambda=\|K\|>0\) and \(U=K/\lambda\). For any selected set of plaquettes and thresholds \(r_i\),
\[
    \|L_X U^{1/2}\|^2
       \le C_0^{|X|}e^{-c_0\beta\sum_{i\in X}(1-\cos r_i)}.              \tag{6}
\]
Indeed \(\|L_X U^{1/2}\|^2=\|U^{1/2}L_XU^{1/2}\|\). Take \(k=1\) in the trace identity preceding (4), take the \(b\)-th root and send \(b\) through even integers to infinity at fixed box and coupling. For a positive trace-class operator \(A\), \(\|A\|\le(\operatorname{Tr} A^b)^{1/b}\le \|A\|^{1-1/b}(\operatorname{Tr}A)^{1/b}\). This gives (6), including the numerator with the bad indicators. The empty case has norm one. The same proof on the neutral sector uses (4) there.

PROVED. The expansion used in (3), now with operator norms and (6), gives
\[
 \|U^{k/2}(q^mJ-I)U^{k/2}\|
       \le \epsilon_m,\qquad \epsilon_m=(1+\delta_q)^m-1,\quad k\ge1.    \tag{7}
\]
Use the constant for the chosen sector and its own vacuum normalization. For \(k=1\) the bound on each marked subset is the product of the two square roots in (6), giving the same angular sums. For larger \(k\) sandwich by the contraction \(U^{(k-1)/2}\). The nonzero eigenvalues of \(q^m J U^k J\) equal those of \(U^{k/2}q^m JU^{k/2}\), since these are \(AA^*\) and \(A^*A\) for \(A=q^{m/2}J U^{k/2}\). The variational characterization of eigenvalues of compact positive operators therefore gives
\[
   |\lambda_i(q^m J U^k J)-\lambda_i(U)^k|\le\epsilon_m                  \tag{8}
\]
in decreasing order with multiplicity, completed by zeros if necessary. In particular its top eigenvalue is within \(\epsilon_m\) of one, even though every selected dimension is at least \(q\). If \(b\epsilon_m\to0\) and \(aT\to\tau>0\), the normalized compressed levels of bounded physical energy and the original ones differ by \(o(1)\) in physical energy. For such a level either \(k\)-slab ratio stays bounded below, since \(ak\le aT\). Equation (8) then bounds the difference of the two log ratios by \(O(\epsilon_m)\). Divide by \(ak=aT/b\). Conversely, a positive lower bound for the first compressed excitation separated from zero by a fixed physical margin transfers back, by applying (8) to any subsequence of original excitations below that margin. These comparisons alone supply no value for that excitation.

PROVED. The centred *electric measurement* at one pivot, \(A_q=qJ_q-I\), mostly creates high lattice energies, even if other excitations approach the vacuum arbitrarily closely. Write \(\Omega\) for the normalized finite-volume vacuum and \(Q_E=\mathbf1_{[e^{-E},1]}(U)\) for \(E\ge0\) in lattice units. Equation (7) at \(m=k=1\) gives \(\|Q_E A_q\Omega\|\le e^{E/2}\delta_q\). Also \(A_q^2=(q-2)A_q+(q-1)I\) and \(|\langle\Omega,A_q\Omega\rangle|\le\delta_q\), so \(\|A_q\Omega\|^2\ge q-1-(q-2)\delta_q\). For \(\beta/q^2\to\infty\), even \(E=u\) gives a vanishing fraction of squared norm in \(Q_E\). This controls the spectral weight of this particular vector. A gap requires a common bound for all excitations.

## What a measurement on the opposite slice can predict

PROVED. Let \(v(X,Y)=K^t(X,Y)/\sqrt{\operatorname{Tr}K^{2t}}\), \(2t\ge4\), viewed as a unit vector in the tensor product of a slice space and its conjugate. Measure the dimensions at the \(m\) indicated pivots on its first end. On the other end make *any* discrete quantum measurement, with result \(y\). Let \(p_{\mathbf d,y}\) be the joint probability. There is a box-, time- and \(m\)-independent \(C\) such that
\[
          \sum_y\sup_{\mathbf d}p_{\mathbf d,y}
                          \le (C/\sqrt\beta)^m \qquad(\beta\ge1).           \tag{9}
\]
The same bound holds with a different absolute \(C\) in the neutral ensemble. Thus even a list of \(H\) candidate dimension tuples, chosen after seeing \(y\), succeeds with probability at most \(H(C/\sqrt\beta)^m\).

PROVED. Write the measurement effects as \(E_y\ge0\), \(\sum_yE_y=I\), and apply their square roots on the second end to obtain unnormalized vectors \(v_y\). For any product \(O\) on the first end, \(\sum_y\|O v_y\|^2=\|O v\|^2\). For angles \(0<t_i\le\pi\), expand \(\prod_i\cos(t_iD_{e_i})\) using the bad indicators at radii \(t_i/3\) as in (4). For each term the sum over \(y\) of the absolute matrix elements is at most \(\|L_Xv\|\,\|L_Yv\|\) by Cauchy–Schwarz. Each squared norm is an ordinary one-slice event on the \(2t\)-periodic torus, by sewing the two kernels. Apply (2) to obtain
\[
 \sum_y\left|\left\langle v_y,\prod_i\cos(t_iD_{e_i})v_y\right\rangle\right|
        \le (2\sqrt{C_0})^m
             \exp\!\left[-c_0\beta\sum_i t_i^2/(9\pi^2)\right].           \tag{10}
\]
For the neutral choice the one-slice probability is bounded by eight times the full one, by positivity and the projection argument above. Cosine inversion on the positive integers expresses \(p_{\mathbf d,y}\) as the integral of the matrix element times \((2/\pi)^m\prod_i\cos(d_i t_i)\) over \([0,\pi]^m\). The series of joint probabilities is absolutely summable. Taking absolute values and integrating (10) proves (9).

PROVED. In particular, measure the same pivots at the other end. The joint weights are \(\|\Pi_{\mathbf d}K^t\Pi_{\mathbf d'}\|_{\rm HS}^2/\operatorname{Tr}K^{2t}\). In an attempted calculation of the numerator of the thermal purity, keeping only \(|d_i-d_i'|\le w\) for every \(i\) retains a fraction at most \([C(2w+1)/\sqrt\beta]^m\). For \(w=o(\sqrt\beta)\) it already loses a fraction tending to one at a single pivot. This is a bound relative to the actual two-period trace, even if the purity itself tends to zero. It applies to ordinary integer dimensions and to predictions from the whole other slice. The earlier centre-parity count concerns the one-period marginal in an electric half-step placement.

PROVED. At a single magnetic-placement cut let \(p_d=\operatorname{Tr}(\Pi_d K^{2t})/\operatorname{Tr}K^{2t}\). There are absolute constants giving
\[
          p_d\le {C\over\sqrt\beta}
                     \exp[-c\min(d^2/\beta,d)]\qquad(d\ge1,\ \beta\ge1).
                                                                            \tag{11}
\]
Indeed the one-angle bound in (10) and
\(|\cos((d+1)s)-\cos(ds)|\le s\) give \(|p_{d+1}-p_d|\le C_1/\beta\) by inversion. To get the upper tail, continue a left \(U(1)\) rotation of the first pivot in \(v\) from \(e^{ix\sigma_3}\) to \(e^{i(x-iy)\sigma_3}\), \(y\ge0\), where \(\sigma_3=\operatorname{diag}(1,-1)\). In the positive integral for \(K^t\) this endpoint link occurs in four spatial half plaquettes and one temporal plaquette. Each trace is linear in this link or its inverse. For a real unit quaternion \(g\), the real part of the continued normalized trace is \(\cosh(y)w(g)\), after cycling factors to put the rotation first. Hence the modulus of the continued kernel is bounded by the real rotated kernel times \(\exp[3\beta(\cosh y-1)]\). The same bound survives the gauge and centre averages. Fourier series in \(x\), or shifting the Fourier coefficient contour on one period followed by Parseval, now gives
\[
           \mathbb E e^{2y k_z}\le e^{6\beta(\cosh y-1)},
\]
where \(k_z\) is the integer generator of that left circle on the measured link. The reduced link state commutes with left translations because the compensating transformations on the other links at its initial vertex disappear under their partial trace. Conditional on \(d\), the \(d\) weights \(d-1,d-3,\ldots,1-d\) are therefore uniform. At least one quarter are at least \((d-1)/2\). Taking \(y=\min(1,(l-1)/(12\beta))\), using \(\cosh y-1\le y^2\), gives \(\Pr(d\ge l)\le C_2e^{-c_2\min(l^2/\beta,l)}\). Finally \(\sum_{j\ge0}p_{d+j}\ge\sum_{j\ge0}(p_d-C_1j/\beta)_+\ge\beta p_d^2/(2C_1)\), by integration of this decreasing linear profile. This proves (11).

PROVED. This locates a limit of the normalization in (3). At a single magnetic cut with even time period, if \(q/\sqrt\beta\to\infty\), then
\[
              q\,\operatorname{Tr}(J_q K^{2t})/\operatorname{Tr}K^{2t}
                  =q\sum_{j\ge1}p_{jq}\ \longrightarrow\ 0 .             \tag{12}
\]
Use (11) and \(\min((jq)^2/\beta,jq)\ge j\min(q^2/\beta,q)\) to sum a geometric series. At \(q/\sqrt\beta\to0\), equation (3) with one pivot and one sample instead gives limit one. The two estimates constrain different attempts to profit from a large minimum spin. Neither determines the thermal defect at the original coupling.

## Fixing an exact spin at the electric cut

GUIDE. To use the bare electric eigenvalue itself, put the cut between two electric half steps. With \(Y=C^{1/2}M/\sqrt\lambda\) on the gauge-invariant space, write \(\widetilde U=YY^*\), \(U=Y^*Y\). The new input for this step is the temporal plaquette law in row 1236, (21), on the indicated neutral spectral band, and the beyond-deletion bound in row 1151, (23). Row 860, Lemma OS, already identifies a spin insertion with a character replacing a temporal plaquette kernel. Row 1236, (12)–(16), already gives the weak joint spin law and returns for smooth electric weights. The question here is the relative probability of a *single prescribed* integer dimension, which tends to zero. The underlying open-box method is due to Sourav Chatterjee. The free exact-curl projection comes from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Row 860](gap-hs-max.md) · [Row 1151](gap-solve5-astra62.md) · [Row 1231, (1)–(2)](gap-solve26-astra62.md) · [Row 1236](gap-solve27-astra62.md) · [Check of (21)](gap-solve27-check-opus.md) · [Outline, free symbol](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1735-L1762)

PROVED, using these inputs. On even spatial cubes \(n^3\), \(\beta\to\infty,\ \beta\le B\log n\), take \(h\to1\), \(0<h\le1\), in the centre-neutral sector of row 1236. Write \(Q=\mathbf1_{[h,1]}(\widetilde U)\), \(\Pi_d=\mathbf1_{D_e=d}\), \(z_\beta=\int e^{-\beta(1-w)}dg\). Uniformly in the edge and in integer \(1\le d\le R\sqrt\beta\) for each fixed \(R\),
\[
  \left\|Q\left({\Pi_d\over p^0_\beta(d)}-I\right)Q\right\|=o(1),
 \qquad p^0_\beta(d)=2^{3/2}z_\beta d^2 e^{-d^2/\beta}.                 \tag{13}
\]
In particular this is a relative estimate even for \(d=1\), whose probability is \((4/\sqrt\pi+o(1))\beta^{-3/2}\).

PROVED. Let \(T_g\) denote \(U\) with \(g\) inserted on the temporal plaquette over this link. Write \(a_d=I_d(\beta)/I_1(\beta)\), \(X=\beta(1-w)\), \(r=\sqrt{2X}\). Joining the electric halves gives
\[
       Y^*\Pi_dY=z_\beta d^2 a_d\, T_{e^X\chi_d/d}.
\]
The character is evaluated at the plaquette holonomy. For bounded Lipschitz \(g(r)\), row 1236, (21), gives the scalar limit of \(T_g\) on the magnetic band \(U\ge h\) as the expectation under \(r=|Z|/\sqrt2\), \(Z\) a standard three-dimensional normal. There are constants \(\eta>0\) and \(C<\infty\) for which \(\|T_{\exp((1+\eta)X)}\|\le C\), providing the tail control for this unbounded insertion. Indeed the even power trace of this self-adjoint insertion divided by the homogeneous trace repeats the plaquette in the same perpendicular spatial parity class at every time. Row 1151, (23), bounds this ratio by \(C^M\) in even period \(M\ge n\). The rectangle extension used after (8) of row 1236 is uniform as \(M\to\infty\). Taking even roots gives the norm bound. The kernel for this majorant is pointwise positive, so deleting a tail \(X>K_0\) in \(T_{e^X\chi_d/d}\) costs at most \(Ce^{-\eta K_0}\) in operator norm. This domination can be taken on the full gauge-invariant space before neutral restriction. A continuous cutoff with the same tail bound suffices.

PROVED. Along \(d/\sqrt\beta\to x\in[0,R]\), the character divided by \(d\) converges on compact \(r\)-sets to \(\operatorname{sinc}(xr)\), with \(\operatorname{sinc}(0)=1\). This follows from \(\sin(d\theta)/(d\sin\theta)\) and \(r=2\sqrt\beta\sin(\theta/2)\). Compact uniform convergence and the preceding tail bound allow the use of (21). The limiting expectation of \(e^{r^2/2}\operatorname{sinc}(xr)\) is \(2^{3/2}e^{-x^2/2}\). Multiplying the density \(\pi^{-3/2}e^{-|z|^2}\) by \(e^{|z|^2/2}\) gives \(2^{3/2}\) times a standard normal density, and averaging \(e^{ix u\cdot z}\) over unit \(u\) gives the sinc. Likewise \(a_d\to e^{-x^2/2}\) by the normalized one-bond Haar integral, and \(z_\beta\sim\sqrt{2/\pi}\,\beta^{-3/2}\) by rescaling its angle using \(1-\cos\theta\ge2\theta^2/\pi^2\). On \(U\ge h\) the map \(YU^{-1/2}\) is unitary onto the range of \(Q\). This follows from \(U=Y^*Y\) and \(\widetilde U=YY^*\) on bands away from zero. The factors \(U^{-1/2}\) cost \(1+o(1)\) there. The limiting scalar divided by \(2^{3/2}e^{-x^2}\) is one, including \(x=0\). A failing uniform estimate would give a subsequence with \(d/\sqrt\beta\) convergent in \([0,R]\) and a unit Rayleigh vector contradicting this calculation. This proves (13).

PROVED. At fixed physical time, replacing the entire magnetic residue class by this one exact electric dimension still retains the finite-volume spectral test. If \(aT\to\tau>0\), \(an=L>0\), take \(h=1-T^{-1/3}\) in (13). Splitting at \(Q\) gives
\[
 \left\|\widetilde U^{T/2}
        \big(\Pi_d/p^0_\beta(d)-I\big)\widetilde U^{T/2}\right\|=o(1).
                                                                            \tag{14}
\]
The term on \(Q\) uses (13). The two cross terms and the complementary term cost at most \(3(1+1/p^0_\beta(d))h^{T/2}=o(1)\). Here \(p^0_\beta(d)\ge c_R\beta^{-3/2}\). The \(AA^*,A^*A\) comparison in (8) gives the same individual eigenvalues up to \(o(1)\) for the scaled exact-spin compression and \(\widetilde U^T\). This operator-norm comparison gives no trace error without state counting.

PROVED. At a microscopic separation the local dynamical correction can be computed. In the vacuum \(\widetilde\Omega\) let \(p=\langle\widetilde\Omega,\Pi_d\widetilde\Omega\rangle\), and keep \(s\ge1\) fixed in lattice units. With \(d/\sqrt\beta\to x<\infty\) and \(\rho_s=2b(s)\), where \(b(s)\) is the complementary free-curvature entry of row 1236, (16), one has
\[
 {\langle\widetilde\Omega,\Pi_d\widetilde U^s\Pi_d\widetilde\Omega\rangle
       \over p^2}
 \longrightarrow
 {e^{-2\rho_s^2 x^2/(1-\rho_s^2)}\over(1-\rho_s^2)^{3/2}}\,
 {\sinh(2\rho_s x^2/(1-\rho_s^2))\over 2\rho_s x^2/(1-\rho_s^2)}.        \tag{15}
\]
The last quotient takes value one at zero. A Gaussian calculation enters only as the limit of the specified two marked Wilson integrals.

PROVED. Insert the two characters as above in a long even time period. Row 1231, (2), gives the joint limit of these two Wilson plaquette radii, uniformly over periods at least \(n\), so one may first take the vacuum limit at fixed \(n,\beta\). Both marks belong to one perpendicular parity class. Row 1151, (23), bounds the exponential moment at \(1+\eta\) of their *sum*, controlling the two-character tail. For each of three independent colours the limiting curvature pair has covariance \(\Gamma\), with \(A=I-\Gamma=\tfrac12\left(\begin{smallmatrix}1&\rho_s\\\rho_s&1\end{smallmatrix}\right)\). To see that \(0<b(s)<1/2\), observe that the Fourier expression in row 1236, (15)–(16), integrates the nonnegative function \((|t_2|^2+|t_3|^2)/(2\sinh\omega)\) times \(e^{-s\omega}\) for an edge in direction one, with \(t_i=e^{ik_i}-1\), \(2\cosh\omega=2+\sum_i|t_i|^2\). Its value at \(s=0\) is \(1/2\), and it decreases strictly. Completing the square in the Gaussian integral for \(e^{(|G_1|^2+|G_2|^2)/2}\) gives the factor \((\det A)^{-3/2}\) and covariance \(\Gamma A^{-1}\) for the tilted pair. Write the two sinc functions as angular averages of plane waves at vectors \(x u_1,x u_2\). The two bare multipliers contribute \(e^{-x^2}\), changing the matrix in their combined quadratic exponent from \(\Gamma A^{-1}\) to \(A^{-1}\). On division by the two single-cut values this gives the first factor on the right of (15) and the angular average of \(\exp[2\rho_s x^2 u_1\cdot u_2/(1-\rho_s^2)]\). The dot product is uniform on \([-1,1]\), giving the stated quotient.

PROVED. The normalized trial vector \(\Pi_d\widetilde\Omega/\sqrt p\) bounds \(\|\Pi_d\widetilde U^s\Pi_d\|/p\) below by the left side of (15). At \(x=0\) the limiting bound is strictly greater than one. For fixed \(s\) it grows without bound as \(x\to\infty\) *after* the displayed cutoff limit, because the net exponential is \(\exp[2\rho_s x^2/(1+\rho_s)]\) divided by a factor of order \(x^2\). Thus even choosing a spin with arbitrarily small limiting bare multiplier \(e^{-x^2/2}\) need not make the vacuum-normalized one-step compression small after accounting for the cost of selecting that spin. In fact in \(\Pi_d\widetilde U^s\Pi_d\) the outer \(C^{1/2}\)'s contribute the same scalar \(a_d\) to every eigenvalue. The remaining operator retains \(M U^{s-1}M\) between the other electric factors, with the appropriate vacuum scalar. The bare factor cancels from the ratio of the first two eigenvalues.

## Retaining winding loops at an electric seam

GUIDE. A single conditioned spin leaves many spatial degrees of freedom. For a collective test, erase the temporal plaquettes over \(S=E\setminus H\) on one cut, where \(H\) is a spatial graph. Erasing means selecting \(d=1\) on those bonds in the electric placement. Row 1290, (9), already obtains the full thermal defect by leaving a spanning tree. Its (15) gives the large higher moments at a fully erased cut even after integration of the temporal gauge. I use both results below. The test here keeps the three winding loops dynamical on the cut. [Row 1290](gap-solve33-astra62.md) · [Row 1297, check of the fully erased cut](gap-solve33-check-opus.md)

PROVED. Work on an \(n^3\) cube. Start with the three straight coordinate rings through the origin, their only intersection. Attach a forest to include every other vertex without creating more cycles. One choice is a tree of the unwrapped box containing the three straight coordinate paths from the origin to the three far axial endpoints, then add just their three wrapping bonds. Denote this retained graph by \(H\). Normalize each retained electric kernel to mass one. Its gauge-integrated cut kernel \(k_H(X,Y)\) satisfies
\[
  \sup_{X,Y}|k_H(X,Y)-1|
       \le (1+\zeta_n)^3-1,\qquad
  \zeta_n\le C(1+\beta)^{3/2}\exp[-c(n-1)/(1+\beta)].                  \tag{16}
\]
To see this, integrate the temporal vertex gauges on attached trees, from the leaves, giving one per bond. Conditional on the root gauge, the internal gauges on each ring convolve its \(n\) central kernels. Explicitly, separate endpoint gauge transformations put all edges of each ring except the closing one at identity on each of \(X,Y\). Integrate along the resulting path by the convolution identity. Each resulting ring factor is the \(n\)-fold convolution evaluated on the two closing holonomies and the common root conjugation. Its departure from one is bounded by \(\sum_{d\ge2}d^2 a_d^n\). The adjacent Bessel ratios in row 1149, (16), are positive and below one, so \(a_d\le a_2\) for \(d\ge2\). Also \(\sum d^2a_d=1/z_\beta\) by the character expansion at identity. Finally \(1-a_2=\int(1-\cos\theta)c_\beta(\theta)\,dg\ge c/(1+\beta)\) for \(\beta\ge1\), by restricting to angles between \(\tfrac12\beta^{-1/2}\) and \(\beta^{-1/2}\) and using \(z_\beta\le C\beta^{-3/2}\). This proves (16) before integrating the root. Row 1149 gives the straight-path damping. Retaining the three windings enables the two-cut test below.

PROVED. Let \(X_S(t)=\beta\sum_{e\in S}(1-w(U_{p(t,e)}))\) for the temporal plaquettes on cut \(t\). Write \(M_1=\mathbb E_T e^{X_S(0)}\) and \(M_2=\mathbb E_{2T} e^{X_S(0)+X_S(T)}\) in the respective ordinary Wilson tori. Uniformly in \(T\ge2\), as \(n\to\infty,\ \beta=O(\log n)\),
\[
                   \log M_2-2\log M_1=\Psi(K,T)+O(\zeta_n).              \tag{17}
\]
On an erased bond multiplication by \(e^{\beta(1-w)}\) leaves the constant \(1/z_\beta\) from the normalized Wilson kernel. Thus \(z_\beta^{|S|}M_1\) and \(z_\beta^{2|S|}M_2\) insert mass-one Haar on the erased bonds. The deterministic factors cancel in (17). The modified numerators contain respectively one and two copies of \(k_H\) in positive integrals. Replacing them by one costs \(O(\zeta_n)\) in their logs by (16). The resulting cut, with the spatial half weights reinstated, is \(M|1\rangle\langle1|M\). Its two-cut numerator is exactly the square of the one-cut numerator. The original torus denominators give (17). Thus this graph may replace a full reset in the physical test while keeping winding cycles in all three spatial directions.

PROVED, using row 1290, (15). There is a quantitative trade-off for *arbitrary* retained spatial graphs \(H\), even after integrating all temporal gauges at the cut. Take the even \(n^4\) ordinary torus of that result and write \(V=n^3\). For \(A\subset E\) let \(I_A(X,Y)\) be the temporal gauge integral of the product of the **unnormalized** Wilson deficit weights on \(A\), with \(I_\varnothing=1\). The positive deletion reading is \(B_H=I_H/I_E\). Let \(r(H)=|E(H)|-V+\#\{\text{components of }H\}\), including isolated vertices. For fixed \(p>1\), define
\[
 \mathcal L_p(H)=\log{\mathbb E B_H^p\over(\mathbb E B_H)^p}.
\]
Then
\[
       |\mathcal L_p(H)-\mathcal L_p(\varnothing)|\le 2p\beta\, r(H).
                                                                            \tag{18}
\]
Indeed a spanning forest \(F\) of \(H\) has \(I_F=z_\beta^{|F|}\) by leaf integration. Every extra bond takes values in \([e^{-2\beta},1]\), so \(e^{-2\beta r(H)}I_F\le I_H\le I_F\) pointwise. Bounding numerator and denominator in both directions proves (18). Row 1290 supplies \(c_p\beta V\le \mathcal L_p(\varnothing)\le C_p\beta V\) for large \(n,\beta\). The same one-cut comparison on its centre-neutral circle uses the seam convention of that source. In particular the winding repair (16), with \(r=3\), has a higher-moment cost of order \(\beta V\).

PROVED. More generally, for all sufficiently large \(n,\beta\), either \(\mathcal L_p(H)\ge c_p\beta V/2\), or the isolated normalized electric kernel on \(H\), with vertex gauge projection and Haar on every erased edge, has at least \(\kappa_p V\) disjoint neutral loop tests of lengths at most \(l_p\). Here \(\kappa_p>0\) and \(l_p<\infty\) depend only on \(p\). In the latter case (18) gives \(r(H)\ge c_pV/(4p)=:\gamma V\). Partition the spatial torus into boxes of sides between \(l\) and \(2l\), for a fixed \(l\) sufficiently large that fewer than \(\gamma V/2\) edges cross the box boundaries (at most \(3V/l\)). Removing those retained edges decreases the cycle rank by at most their number. A box contributes at most \(3(2l)^3\) cycles to the rank, so at least \(\gamma V/[6(2l)^3]\) boxes contain a simple cycle, each of length at most \((2l)^3\). Use one in each such box. They are contractible for sufficiently large \(n\). This extends the short-cycle count in row 1149, §8 after (21), to a hypothesis on cycle rank. Inequality (18) forces that rank when the moment cost is small. [Earlier short-cycle count](gap-solve4-astra62.md)

PROVED. Products of the fundamental characters around any subset of these cycles are orthonormal in link Haar measure. Integrating an edge in an unpaired loop gives zero and the Haar squared character norm is one. The electric convolution multiplies each product by \(a_2\) to the power of its total length. Gauge and centre projection preserve the products. Thus the neutral thermal trace of this *isolated electric kernel* at power \(k\ge1\) is at least \((1+a_2^{\,l_pk})^{\lfloor\kappa_p V\rfloor}\). In particular a stand-alone contraction bounded strictly below one for all these graphs at one step is incompatible with subextensive cost \(\mathcal L_p(H)=o(\beta V)\). The calculation concerns the isolated seam and a fixed \(p>1\). It gives no lower bound on the first excitation of the full magnetic transfer.

## Comparing the two Wilson moments with the free curvature law

GUIDE. A remaining possibility is to estimate the *difference* in (17) after the large first moments have cancelled. The local limit used in (13)–(15) suggests replacing the interacting radii on both cuts by those of the exact-curl Gaussian. I evaluate that proposal on the same cut geometries. This is a hand calculation in the comparison law.

PROVED. On the finite \(n^3\times T\) torus let \(P_{\rm ex}\) be the orthogonal projection onto real exact two-forms, and use three independent colour copies with this covariance. For any marked plaquette set \(L\), let \(\Gamma_L\) be the compression of \(P_{\rm ex}\) to its coordinates. The Gaussian substitute for the raw deletion moment is
\[
 G(L)=\mathbb E\exp\!\left(\tfrac12\sum_{p\in L}|G_p|^2\right)
           =\det(I-\Gamma_L)^{-3/2} .                                    \tag{19}
\]
It is infinite precisely if the marked set supports a nonzero exact two-form. Indeed all eigenvalues of \(\Gamma_L\) are in \([0,1]\). Gaussian integration in an orthogonal basis gives the formula and divergence at eigenvalue one. A unit vector extended by zero achieves Rayleigh quotient one exactly when it belongs to the range of the projection. The cochain convention and covariance are those of Sussman and Alpoge, outline 1674–1698 and 1735–1762. Row 1145, §2, previously used the gradient and harmonic decomposition for a different fixed-torus determinant. [Row 1145](gap-solve2-astra62.md)

PROVED. Take \(L\) above the complement of a spatial spanning tree, on each of \(b\) temporal cuts in a single time circle. Per colour the space of such exact forms has dimension \(3(b-1)\). On each cut a supported exact form has a closed spatial one-form as its temporal components. This follows from commuting finite differences and the vanishing of all spatial two-form components. Its three periods sum to zero across the cuts, since for an exact form each is the time difference of periods of the spatial potential. A closed spatial one-form vanishing on the tree is determined by its three periods. Zero periods permit a single-valued primitive by path integration, and this primitive is constant along the tree. Existence at arbitrary periods follows by starting with a constant one-form and subtracting a gradient obtained by integrating it on the tree. Conversely write the closed form on each cut as \(h_t+\nabla f_t\), harmonic constant plus gradient, and put zero on unmarked times. When \(\sum_t h_t=0\), a periodic spatial potential with time difference \(h_t\), together with temporal potential \(-f_t\), realizes those components. This gives the stated dimension. In particular the two-cut Gaussian moment at the exact tree reset is infinite at *finite* \(n,T\). Once the three independent windings are kept, a supported closed form must also have zero periods on those rings, so (19) is finite for both moments in (17).

PROVED. Write \(\mathcal G_H=\log G_2-2\log G_1\) for the Gaussian counterpart of (17), with the same spatial graph at both cuts. To compute it, use spatial Fourier momentum \(k\) in lattice units, \(v_i=e^{ik_i}-1\), \(s=\sum_i|v_i|^2\), \(2\cosh\omega=2+s\). On temporal plaquettes the symbol of \(I-P_{\rm ex}\) at nonzero spacetime momentum is
\[
                 {sI-vv^*\over s+2-2\cos k_0}.
\]
At the origin it is identity. On a single cut in period \(T\), denote its compressed-in-time covariance by \(A_{\rm P}\). Also form \(A_{\rm A}\) with antiperiodic temporal frequencies \((2j+1)\pi/T\). These are operators on spatial edge arrays. The two-cut compression in period \(2T\) splits into \(A_{\rm P}\) and \(A_{\rm A}\) on the symmetric and antisymmetric combinations of the cuts because the factor \(e^{ik_0 T}=(-1)^j\) selects the even or odd frequency indices. Restriction to spatial coordinates \(S\) commutes with this splitting. Consequently
\[
              \mathcal G_H=\tfrac32\log
                      {\det (A_{\rm P})_S\over\det (A_{\rm A})_S}.        \tag{20}
\]
Both matrices are strictly positive on these coordinates for the connected graphs containing three independent windings under consideration.

PROVED. Split the real spatial cycle space (orthogonal complement of gradients) as \(Z\oplus H_0\), where \(H_0\) is the three-dimensional space of constant edge fields, and \(Z\) is transverse at nonzero spatial momenta. Both operators vanish on gradients. On \(H_0\) they are \(I/T\) and zero respectively. On \(Z\) their eigenvalues, each on two polarizations, are
\[
       a_{\rm P}(k)=\tanh(\omega/2)\coth(T\omega/2),\qquad
       a_{\rm A}(k)=\tanh(\omega/2)\tanh(T\omega/2).                     \tag{21}
\]
Indeed averaging the symbol over temporal frequencies uses the Fourier coefficients \(e^{-|j|\omega}/(2\sinh\omega)\) of \((2\cosh\omega-2\cos k_0)^{-1}\), verified by summing two geometric series. The multiples of \(T\) have signs \(+1\) in the periodic average and alternating signs in the antiperiodic average. Also \(s/(2\sinh\omega)=\tanh(\omega/2)\). In particular \(A_{\rm A}\le A_{\rm P}\le I\).

PROVED. The coordinate restriction from the cycle space to \(\mathbb R^S\) is onto. To lift a vector, correct the divergence of any prescribed entries on \(S\) by routing its opposite on a spanning tree of \(H\), successively from the leaves. Its kernel \(D_H\) consists of cycle flows supported in \(H\). Their harmonic projections span \(H_0\) because the retained cycles span the three windings. Put \(D_0=D_H\cap Z\), \(Z'=Z\ominus D_0\). For a harmonic vector \(h\), the unique lift in \(D_H\ominus D_0\) has the form \(h+Rh\), \(Rh\in Z'\). Thus \(D_H^\perp\) *within the cycle space* consists of \(z-R^*z\), \(z\in Z'\). The adjoint of the coordinate restriction maps onto this subspace isomorphically. Its determinant factors, and those of the parameterization by \(z\), cancel in (20). If \(P',A'\) denote the form compressions of \(A_{\rm P},A_{\rm A}\) to \(Z'\), respectively, this gives
\[
 \mathcal G_H=\tfrac32\log{\det P'\over\det A'}
          +\tfrac32\log\det_{H_0}(I+T^{-1}R^*(P')^{-1}R).                \tag{22}
\]
Indeed the two forms pulled back to \(z\) are \(P'+RR^*/T\) and \(A'\). The last equality uses the identical nonzero eigenvalues of \(LL^*\) and \(L^*L\). This argument also verifies invertibility in (20).

PROVED. For the three individual rings of (16), \(D_0=0\), \(Z'=Z\). For a unit constant field \(h_i\) of orientation \(i\) (value \(n^{-3/2}\) on its edges), the retained lift \(h_i+Rh_i\) is \(\sqrt n\) times the oriented unit flow on that ring. It has squared norm \(n^2\), and different orientations are orthogonal. Hence \(R^*R=(n^2-1)I\). Using \(P'\le I\) gives the lower bound
\[
      \mathcal G_{\rm three}\ \ge\
        6\sum_{k\ne0}\log\coth(T\omega(k)/2)
              +\tfrac92\log\!\left(1+{n^2-1\over T}\right).               \tag{23}
\]
The transverse coefficient includes the two polarizations and three colours. In particular finiteness of both Gaussian integrals after the winding repair still leaves a divergent signed answer at fixed aspect.

## A signed discrepancy on two choices of cut

PROVED. There is a second retained graph with the same Wilson test and bounded Gaussian defect. For even \(n\), keep all direction-one rings with \(y,z\) even, all direction-two rings with \(z\) odd and \(x\) even, and all direction-three rings with \(x,y\) odd. These \(3n^2/4\) rings are pairwise vertex-disjoint. Contract each to a vertex, include the unused vertices, and add the edges of a spanning tree of the resulting connected graph. These bridge edges give no additional cycles. Call this graph \(H_{\rm many}\). In the temporal gauge integral, start with the leaf pieces of that tree. Each leaf ring contributes, conditional on its attachment gauge, a factor between \(1-\zeta_n\) and \(1+\zeta_n\), by the convolution in (16). After this bound the attachment bridge integrates to one. An isolated vertex piece contributes just its bridge integral. Repeating to the root bounds \(k_{H_{\rm many}}\) between \((1-\zeta_n)^{3n^2/4}\) and \((1+\zeta_n)^{3n^2/4}\) when \(\zeta_n<1\). The comparison with a rank-one cut used in (17) therefore applies with error \(O(n^2\zeta_n)\). In particular the two actual Wilson differences \(\mathcal W_H=\log M_2-2\log M_1\) obey
\[
               \mathcal W_{\rm three}-\mathcal W_{\rm many}=o(1)           \tag{24}
\]
along \(\beta=O(\log n)\). This estimate holds even if the common thermal defect diverges.

PROVED. Uniformly for \(0<\alpha\le T/n\le A<\infty\),
\[
       \mathcal G_{\rm three}=\tfrac92\log n+O_{\alpha,A}(1),
       \qquad 0\le\mathcal G_{\rm many}\le C_\alpha .                       \tag{25}
\]
For the three rings, \(R h_i\) has unit-modulus spatial Fourier coefficient in polarization \(i\) at every nonzero \(k\) with \(k_i=0\), and zero at other frequencies. This follows by summing the oriented ring over its \(n\) edges with Fourier normalization \(n^{-3/2}\) and multiplying by \(\sqrt n\). Different polarizations give zero cross terms. Thus \(R^*(P')^{-1}R\) is a scalar matrix with entry \(\sum_{k\ne0,\,k_i=0}a_{\rm P}(k)^{-1}\), between \(n^2-1\) and \(C n^2\). For the upper bound, with centered frequency indices \(k=2\pi l/n\), \(a_{\rm P}(k)\ge\tanh(\omega/2)\ge c|l|/n\). This uses \(\sin(|k_i|/2)\ge |k_i|/\pi\) and boundedness of \(s\). Each nonzero two-dimensional square shell \(\|l\|_\infty=j\) has at most \(8j\) indices. The transverse sum in (23) is uniformly bounded since \(T\omega\ge c\alpha\|l\|_\infty\), three-dimensional shells have at most \(Cj^2\) indices, and \(\log\coth(u/2)=\log[(1+e^{-u})/(1-e^{-u})]\le C_\alpha e^{-u}\) for \(u\ge c\alpha\). Using equality in the transverse term of (22) proves the first estimate.

PROVED. For \(H_{\rm many}\), the flow equal to \(4n^{-3/2}\) on the union of rings of orientation \(i\), zero elsewhere, projects harmonically to \(h_i\) and has squared norm four. The three choices are orthogonal. Taking the minimum-norm lift thus gives \(\|R\|\le\sqrt3\). On \(Z'\), \((P')^{-1}\le C n I\) by the preceding lower bound on \(a_{\rm P}\). The harmonic factor in (22) has log at most \(3\log(1+3Cn/T)\). For the transverse determinant, the generalized Rayleigh ratios of \(A_{\rm P}\) to \(A_{\rm A}\) on \(Z\) are all at least one. By the variational principle the ordered ratios after restriction to \(Z'\) are bounded above by the corresponding unrestricted ones. Multiplying gives a bound by the full transverse determinant already estimated. Both factors in (22) are at least one. This proves the second estimate.

PROVED. Put \(\mathcal N_H=\mathcal W_H-\mathcal G_H\), with no assumption that the local Gaussian comparison extends to these collective moments. Equations (24)–(25) establish an unconditional difference of *signed* errors,
\[
             \mathcal N_{\rm many}-\mathcal N_{\rm three}
                     =\tfrac92\log n+O_{\alpha,A}(1).                     \tag{26}
\]
Independent per-cut scalar normalizations cancel in \(\mathcal W_H\). Even after keeping windings so that both Gaussian integrals exist, the same signed error cannot approximate both full Wilson deletions to order one.

PROVED. Removing the harmonic term from **both** Gaussian predictions still leaves a discrepancy at order one. Write \(\mathcal G_H^\perp=\tfrac32\log(\det P'/\det A')\). Fix \(T/n\to\alpha>0\). Consider the real unit vector \(v\) proportional to the direction-one flow \(\mathbf1_{\{y,z\ {\rm even}\}}\cos(2\pi y/n)\), constant in \(x\), on the retained rings of \(H_{\rm many}\). This is a cycle with zero mean, hence \(v\in D_0\) for \(n>4\). The ratio of the determinant quotients on \(Z\) and on \(Z\cap v^\perp\) is \(\langle v,A_{\rm A}^{-1}v\rangle/\langle v,A_{\rm P}^{-1}v\rangle\), using inverses on \(Z\). Indeed the cofactor in the \(v\)-direction of either matrix is its determinant times that entry of its inverse. The further restriction to \(Z'\subset v^\perp\) can only decrease the quotient by the preceding variational argument. The two parity masks in \(v\) each split a Fourier component into its original frequency and its translate by \(\pi\) with equal amplitudes. One quarter of its squared norm is at \(k=(0,\pm2\pi/n,0)\). The other frequencies stay a fixed distance from zero and contribute only \(O(1)\) to the inverse forms. The low-frequency terms grow linearly in \(n\) by (21), and their inverse ratio tends to \(\coth^2(\pi\alpha)\). Consequently
\[
       \liminf(\mathcal G_{\rm three}^\perp-\mathcal G_{\rm many}^\perp)
                          \ge 3\log\coth(\pi\alpha)>0 .                    \tag{27}
\]
Equation (24) still compares the actual Wilson answers. Thus discarding the explicit winding determinant does not give a universally accurate transverse substitution on these two cuts.

PROVED. On the denser graph the remaining free transverse modes themselves prevent the small thermal bound at an aspect used by the seed. The polarization space at \(k=(2\pi/n)(1,1,1)\) is orthogonal to every retained cycle flow, since each ring sums a nontrivial longitudinal Fourier character. It therefore survives in \(Z'\), including its conjugate on real fields, with the two scalar eigenvalues from (21). All other generalized ratios are at least one. For one polarization, the conjugate pair gives two real modes, each with periodic-to-antiperiodic ratio \(\coth^2(T\omega/2)\). Their contribution to (22) gives
\[
      \mathcal G_{\rm many}^{\perp}\ge
                6\log\coth(T\omega(k)/2)\ge 6\log\coth 4
                     >\log(1651/1650),\qquad T\le n/2.                  \tag{28}
\]
Here \(T\omega(k)/2=T\,\operatorname{arsinh}(\sqrt3\sin(\pi/n))<4\). The strict comparison uses \(\coth4=1+2/(e^8-1)>1+2/6560\) and the binomial inequality. All of (19)–(23), (25), (27) and (28) are Gaussian integral statements. Equation (24) uses the Wilson kernel, and (26) compares the two measures. A bound for the interacting thermal defect still requires the Wilson contribution.

## The physical estimate still needed

PROVED. On an admissible physical trajectory take a fixed cube of side \(L\) in the dyadic family of Theorem ZD-c, with \(n_j=L/a_j\) divisible by four, \(\beta_j\to\infty\), \(\beta_j=O(\log n_j)\), and \(T_j=n_j/2\). Use the full physical transfer \(U_j=K_j/\|K_j\|\), including all centre sectors. Put \(S_j=\operatorname{Tr}U_j^{T_j}-1\), which is the excited thermal sum of that theorem. The spectrum lies in \([0,1]\) and includes one. Consequently \(1\le\operatorname{Tr}U_j^{2T_j}\le1+S_j\), giving
\[
 \log(1+S_j)\ \le\ \Psi(K_j,T_j)\ \le\ 2\log(1+S_j).
                                                                         \tag{29}
\]
The comparison (17), (24) gives \(\mathcal W_{\rm many}=\Psi(K_j,T_j)+o(1)\) on this sequence. Thus \(\limsup_j\mathcal W_{\rm many}<\log(1651/1650)\) at one such \(L\) would suffice for the two-stage seed \(\limsup_j S_j<1/1650\). The transfer and shape hypotheses for propagating that seed are those of Theorem ZD-c. [Physical seed and thresholds](gap-phys-seed.md)

PROVED. Conversely, if this two-stage seed holds at the chosen \(L\), its *necessary* consequence on this graph is
\[
 \limsup_j \mathcal N_{\rm many}
 < 2\log(1651/1650)-6\log\coth 4 <0 .                                    \tag{30}
\]
Indeed (29) bounds the Wilson term from above and (22), (28) bound the Gaussian term from below. For the strict sign, \(\coth4>1+2/6560\) implies \(\coth^3 4>1+6/6560>1651/1650\). Thus a negative contribution of definite size from the interacting law is necessary even for the graph with bounded Gaussian defect.

OPEN. Equation (26) determines the difference of the two Wilson-minus-Gaussian errors. Their common Wilson thermal defect at one fixed physical size remains uncontrolled. I have no upper bound that establishes the seed, or a construction of the required continuum theory with a unique vacuum and a common positive energy threshold. The derivations above are analytical research arguments. They carry no audit verdict.

RESULT — OPEN. The two winding cuts agree on the Wilson thermal defect up to \(o(1)\), while their Gaussian deletion predictions differ by \(\tfrac92\log n+O(1)\) at fixed aspect ratio. The interacting estimate needed for a physical seed and the Jaffe–Witten mass gap remain open.
