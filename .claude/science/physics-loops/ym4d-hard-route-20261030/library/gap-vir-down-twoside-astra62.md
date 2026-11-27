# Repo search

Research text at `8ee4c9681660`. The requested prior inventory is absent. The task is to price a window ending at a certified HOT box, then test whether the negative contribution can be measured through the same observation as the positive contribution.

**ON FILE (VIR-DOWN, rows 1624–1627).** The registry assigns the thermal band question to no other row. LEV-FAIL concerns individual levels. Row 1624 (15) charges the full squared prediction distance on negative pairs and gives the thermal virial inequality at the trial speed. Row 1626 (2) expresses its margin as the signed observed contrast less a positive residual cost on negative pairs. Check 1627 §1.1 charges an exactly hidden, slow level its full deficit. Its §2 proves strict partial hiding of every Wilson excitation by a finite partition, without a uniform loss. The Wilson counterexamples in row 1626 use fixed size as \(\beta\downarrow0\) or the fixed interval \([1/512,1/128]\). Neither samples the calibrated window. [Tool](gap-vir-down-tool-astra62.md) · [Check 1625](gap-vir-down-tool-astra62-check-opus.md) · [Domination](gap-vir-down-dom-astra62.md) · [Check 1627](gap-vir-down-dom-astra62-check-opus.md) · [Registry](open-registry.md)


**ON FILE (five-ref search).** In Markdown and TeX on `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`), and `pr/10141` (`c73ad7b177d9`), the search for VIR-down, thermal virial, two-sided prediction, hidden slope budget, signed prediction cost, calibrated hot window and residual Gram contrast returned zero hits. The wider “calibrated band” search hit unrelated finite-channel matching notes, including `CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md`. A targeted check on PRs 10114 and 10133 found `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (5)–(8): for a simple spatial loop of length \(p\), the local convolution has multiplier \(\rho=(I_2/I_1)^p\) and dominates \((1+v_N/\rho)^{-1}|F\rangle\langle F|\) for its centered reading. The companion `REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md` (162–192) has small-\(\beta\) one-step oscillation factor \(\beta/(1-12\beta-\beta^2/(1-14\beta))\). Both concern a single propagation at one coupling. The November 8 digest identifies the same centered-loop result. The pinned checkout outside this lane gave no literal target hit. [November 8 digest, §11](prior/repo-search-2026-11-08.md)

**ON FILE (outline, index row 244).** The index entries GL8, GL10, RF53 and the common-prefix offset obligation lead to Sussman and Alpoge's outline (with Claude and Codex), supplied revision `31a47c543775`. Lines 2315–2335 give \(Z_s(0)=\operatorname{Tr}L^s\) for the positive gauge-averaged transfer, and 2371–2381 give the upper bound \(|\operatorname{Tr}(\Xi_1L\cdots\Xi_sL)|\le\operatorname{Tr}L^s\) for the admitted contractions. Lines 22014–22040 transport the same bare integral under dilation. Lines 32184–32198 keep additional premises for offsets comparing different runs. CA-I 2703–2711 expressly leaves a gap outside Theorem 0. None of these statements bounds a signed thermal derivative on the band. The local statement and method searches also located TR-down/Corollary B (1610, checked 1613), aspects 34 and 60 (1368, 1370, 1527) and the spectral positive-part upper bound for (15) (1626 (1), checked 1627). The last bound is used below in the opposite direction as a certificate for the consumer. [Index](sa-index/README.md) · [Obligations](sa-index/obligations.md)

## The rate paid by TR-down

**ON FILE (rows 1453, 1610 §§2.3, 3.4–3.5, check 1613).** Fix the witnesses \(b,g_0,\ell\), a late \(K\), \(n=\ell b^K,\ u=n/512\), and vary \(\beta\) on this one integer lattice. With positive excited neutral multipliers \(r_i=e^{-m_i}<1\), put \(G(t,\beta)=\sum_{i>0}r_i^t\), \(Z=1+G,\ X=\log Z\) and \(W_t=\sum_{i>0}m_i r_i^t=-G_t\). The required local inequality is \(G_\beta/t\ge\kappa W_t\), with the partial derivative taken at fixed time. For \(t'=t\kappa,\ t(\beta_K)=u\), the derivative along the curve is \(G_\beta-t\kappa W_t\). It suffices to prove the inequality at the points \(G\le 1/2\). A last crossing of \(1/2\) before an endpoint with \(G\le4/21\) contradicts integration on the remaining interval. One obtains \(G(u,\beta_K)\le4/21\). On infinitely many original roots check 1613's one fixed enlargement gives (PUR-io) at the same \(g_0,K\). [TR-down](gap-direction7-fable.md) · [Wilson regularity and enlargement](gap-direction7-fable-check-astra62.md)

**PROVED (exact budget with a specified hot endpoint).** Let \(w=\beta_h-\beta_K>0\). At that endpoint define \(T_*=\inf\{s\ge u:G(s,\beta_h)\le4/21\}\). This infimum is attained since \(G\) is continuous, decreases strictly and tends to zero, by domination by the summable weights at \(u\). If HOT has instead been established independently at a period \(T\ge u\), use \(T\) as the certified period. Let \(I\) be the order-one part of the bare interval, of length \(w_I>0\), and let \(J_o=\int_{[\beta_K,\beta_h]\setminus I}\kappa\) be the supplied stretch outside it. Then the sharp integrated requirement for reaching \(T\) is
\[
 \int_I\kappa\,d\beta\ \ge\ [\,\log(512T/n)-J_o\,]_+,\qquad
 \bar\kappa_{\min}=\frac{[\,\log(512T/n)-J_o\,]_+}{w_I}.                 \tag{1}
\]
Here \([z]_+=\max(z,0)\). Indeed \(t_h=u\exp(J_o+\int_I\kappa)\). With \(T=T_*\), (1) is necessary and sufficient for HOT *at this endpoint*. With only a certificate at \(T\), it is sufficient and is sharp from that single datum in the class of transfer spectra: the positive two-state kernel with one excited mass \(\log(21/4)/T\) attains equality in HOT exactly at \(T\). No pointwise smallest profile at positive budget exists on an interval: two continuous nonnegative profiles of the same integral can concentrate on disjoint subintervals. The virial inequality must hold on the characteristic of the actual chosen profile. The sharp endpoint formula with \(T_*\) is bookkeeping, and supplies no estimate of the hot spectrum. With the hot input \(n m_{1,h}\ge\gamma>0,\ G(t_0,\beta_h)\le N_0,\ N_0\ge4/21\), row 1610 Corollary B supplies \(T=\max(u,t_0+(n/\gamma)\log(21N_0/4))\). Check 1613 already established that this latter choice can exceed the true minimum.

**PROVED (margin and room below \(8/3\)).** Relative to the *reference value* \(c=3\pi^2/11\), the mean margin is \(c-\bar\kappa_{\min}\). With all the stretch paid on the window and the sole certificate \(G(n,\beta_h)\le4/21\), it is \(c-\log(512)/w\). It is positive exactly for \(w>(11/(3\pi^2))\log512\). A constant \(8/3-\delta\), \(0\le\delta<8/3\), pays for that certificate exactly when
\[
 \delta\ \le\ \frac83-\frac{\log512}{w}.                                  \tag{2}
\]
At row 1624's \(w_0=(3/8)\log512\) the maximum reduction is **zero**. The scaling margin there is \((9\pi^2-88)/33>0\), by \(223/71<\pi\). On a window \(w=4\log 2\) the required mean is \(9/4\), a reduction of \(5/12\), conditional on HOT at \(n\) at its own endpoint. On a window of exactly the one-loop nominal width \(\log(512)/c\), the scaling margin is **zero**. Check 1453 proves \(\beta_K/(K\log b)\to1/c\). Its finite dilation uses the same \(\beta_K\) on both sides. It gives neither \(w\) at a HOT box nor \(T_*\) there. In particular a leading slope cannot fix local widths: the numerical sequences \(K(\log b)/c + d(-1)^K\), for any fixed \(0<2d<(\log b)/c\), have the same slope and different consecutive increments. These are illustrations about the slope implication, not candidates for Wilson roots. No larger calibrated window or lower Wilson rate follows from (2) without its corresponding HOT and transport data. [Check 1453, BND-2 and the depth shift](sa-ym4-lean-trajectory-check-astra62.md)

**PROVED, using the ON FILE aspect-34 implication (rows 1368, 1370, 1527(ii)).** There is a concrete lower *conditional* rate on the very same bare window \(w_0\) if the desired output is the existential seed after the allowed change of aspect. Choose \(\ell\) divisible by \(17\cdot1024\) and start the characteristic at \(n/34\). Keep HOT at \(n\), at the same right endpoint. Repeating the last-crossing argument with this starting time gives \(G(n/34,\beta_K)\le4/21\) if the stretch is at least \(\log34\) and the rate holds on this new cold characteristic. The aspect-34 entry and the enlargement in check 1527 then apply with \(4\cdot34\mid n\). The exact mean, reduction and scaling margin are respectively
\[
 \frac{8\log34}{3\log512},\qquad
 \frac83\,\frac{\log(512/34)}{\log512},\qquad
 \frac{3\pi^2}{11}-\frac{8\log34}{3\log512}.                              \tag{3}
\]
This is the minimum to reach the same single hot certificate **for this aspect**. It does not bound \(G(n/512,\beta_K)\) on the initial box. The input interval in time and the spatial side in the conclusion are those of the aspect transfer. [Aspect thresholds](gap-agy-seed-neon.md) · [Checked handoff](gap-agy-seed-approaches-neon-check-astra62.md)


**ON FILE (actual root windows, row 1618 Theorem 3, check 1622 §3).** For the particular choice \(\beta_h=\beta_{K+d}\), set \(s=(\log b)/c\). With \(C_I,c_a,Q\) the common-root, coefficient-sum and harmonic-error constants of row 1461 (1)–(2), the proved interval is
\[
 sd-U_d\ \le\ w_K=\beta_{K+d}-\beta_K\ \le\ sd+U_d,\qquad
 U_d=2C_I+2c_a+(2Q/s)(1+\log d).
\]
The one-level necessary budget is \(\int\kappa\ge\log[512\log(21/4)/(n m_{1,h})]\). The full heat trace in (1) is needed for sufficiency. If \(sd>U_d\) and HOT is certified at \(n\), \(\log512/(sd+U_d)\le\bar\kappa_{\min,K}\le\log512/(sd-U_d)\) for the original aspect and an all-window mean based on that certificate. Thus a positive scaling margin is guaranteed geometrically if \(c(sd-U_d)>\log512\), conditional on the specified HOT endpoint. The width bound is credited to row 1618. [Root-window theorem](gap-vir-down-neon.md) · [Check 1622](gap-vir-down-neon-check-opus.md)

**PROVED (fixed depth shifts for the infinitely-often quantifier).** For each fixed \(d\ge1\) and every \(\epsilon>0\), infinitely many \(K\) have \(w_K>sd-\epsilon\). Otherwise, summing the reverse inequality on one tail arithmetic progression of step \(d\) would give \(\limsup_{j\to\infty}\beta_{K_0+jd}/(K_0+jd)\le s-\epsilon/d\), contradicting check 1453. In particular, given any constant \(k>0\), choose \(d\) with \(k s d>\log512\) and a permitted side \(\ell=b^d\ell_h\) with fixed \(1024\mid\ell_h\). The hot lattice at the deeper root has this same integer side \(n=\ell_h b^{K+d}\). **If** \(G(n,\beta_{K+d})\le4/21\) on the full late tail, the roots selected above have window mean \(\log512/w_K<k\). Use that constant mean across its actual window so the terminal time is exactly \(n\). A thermal bound of at least \(k\) on its cold points suffices. With HOT merely on an unrelated infinite set the selection need not intersect it. Alternatively take \(d\) large enough that \(k(sd-U_d)\ge\log512\) and the width guarantee holds on the full tail, including any infinite HOT set. The price of choosing smaller \(k\) here is a different physical side and a longer interval requiring the bound. This does not lower a required rate on a fixed interval of order-one effective coupling for which only \(J_o\) is supplied.


## Using the same prediction on both signs

**ON FILE (rows 1624 (1)–(3), (9)–(10), (15)–(16), and 1626 (1)–(2)).** Work at one finite box and coupling in real neutral \(L^2(\pi)\), with the vacuum Doob transfer \(P\), vacuum projection \(\Pi\), \(Q=I-\Pi\), and \(E\) the orthogonal projection onto the cells of row 1624. These are the binned traces of the three orientations of spatial squares of side \(n/32\) on the \(n/32\) grid after spatial flow for \((n/128)^2\). They include the constant direction. Write \(S^0=-Q U^{-1}(A_\beta^2)'UQ\) for the centered two-step action kernel of row 1624 (5), where \(A=T_+/\lambda_0\) and \(Uf=\Omega_\beta f\) is frozen during differentiation. The original mark is \(S=S^0+2\kappa(P-P^2)\). For buffer \(k\), the signed pair measure \(\mu\) has kernel \(P^k SP^k\) against \(\pi\otimes\pi\) and zero marginals. Its Jordan parts are \(\mu^\pm\). Let \(v=\lfloor t/2\rfloor,\ \theta=t/2-v,\ j=v-k-1\ge1\). For \(d_j(x,y)=p_j(x,\cdot)-p_j(y,\cdot)\), the negative weight in (15) is \(D_j=\|d_j\|^2\), and the visible prediction is \(L_{j+1}=\|EPd_j\|^2\). Its signed integral is \(V=\int L_{j+1}\,d\mu\). The old margin is \(\mathcal M_{15}=V-\int(D_j-L_{j+1})\,d\mu^-\).

**PROVED (sufficient test, including real periods).** Put
\[
 C=PEP,\quad R=P^{v-1}SP^{v-1},\quad
 H_0=I-C,\qquad H_\theta=P^{2\theta}-C,\qquad
 B(H)=H^{1/2} R H^{1/2}.
\]
The convention \(P^0=I\) includes \(\theta=0\). Since \(C\le P^2\le P^{2\theta}\le I\), both remainders are positive. For \(H\) equal to either remainder the proposed test is
\[
 \int L_{j+1}\,d\mu^+ \ \ge\
 \int L_{j+1}\,d\mu^- +2\operatorname{Tr} B(H)_+ .                         \tag{4}
\]
The pair weights on both signs are identical. The additional cost is the adverse spectral part *after integrating both signs* on the unresolved directions. The integer-slab choice \(H_0\) is precisely the right side of row 1626 (1) expressed as a passing test. That row used its failure to exclude (15). Here its **success** implies VIR-down, including at noninteger time. \(H_\theta\) gives the sharper version.

*Proof.* For every bounded nonnegative self-adjoint \(D\), the zero marginals give
\[
 \int\|D^{1/2}d_j\|^2\,d\mu=-2\operatorname{Tr}(D R).                    \tag{5}
\]
Indeed on one real vector \(f\) the mixed term of the squared increment of \(P^jf\) is \(-2\langle f,P^{j+k}SP^{j+k}f\rangle\). Sum this identity for \(D^{1/2}f\) over an orthonormal basis. The integrable majorant is \(\|D\|D_j\) against \(|\mu|\), since \(p_j\) is bounded on the compact Wilson box. In particular \(V=-2\operatorname{Tr}(CR)\). The true full secant contrast from row 1624 (10) is
\[
 -2\operatorname{Tr}(P^{2\theta}R)
  =4\left(G_\beta/t-\kappa\sum_{i>0}r_i^t(e^{m_i}-1)\right).               \tag{6}
\]
This also follows directly by taking the diagonal of \(S^0\) on \(f_i\), which is \(-2r_i\langle\psi_i,A'_\beta\psi_i\rangle\), and using the fixed-time trace derivative. All traces are absolutely convergent since \(j\ge1\) and \(P\) is trace class.

For \(0\le H\le I\) the exact variational identity is
\[
 \sup_{0\le Y\le H}\operatorname{Tr}(YR)=\operatorname{Tr}B(H)_+ .         \tag{7}
\]
To see this, the form \(\langle x,Yy\rangle\) on vectors \(H^{1/2}x,H^{1/2}y\) is well-defined and bounded by their norms, by Cauchy–Schwarz for \(Y\) and \(Y\le H\). It extends to a positive contraction \(J\) on the closed range closure of \(H^{1/2}\), extended by zero on its orthogonal complement. Thus \(Y=H^{1/2}JH^{1/2}\). In the spectral basis of the self-adjoint trace-class \(B(H)\), the supremum over \(0\le J\le I\) is attained at its positive spectral projection. This proves (7). Using \(H_\theta\) itself as a competitor in (7) proves
\[
 \mathcal M_{15}\ \le\ V-2\operatorname{Tr} B(H_0)_+
 \ \le\ V-2\operatorname{Tr} B(H_\theta)_+
 \ \le\ -2\operatorname{Tr}(P^{2\theta}R).                                \tag{8}
\]
For the first inequality, row 1626 (2) gives \(2B(H_0)=N_--N_+\) with \(N_\pm=\int |H_0^{1/2}d_j\rangle\langle H_0^{1/2}d_j|\,d\mu^\pm\), whence \(2\operatorname{Tr}B(H_0)_+\le\operatorname{Tr}N_-\). The middle inequality is nesting of the intervals in (7). Finally \(e^m-1\ge m\), so (4) implies \(G_\beta/t\ge\kappa W_t\) at the trial rate. The proof never commutes \(P\) with the loop projection \(E\).

**PROVED (exact saving and its scope).** If all one uses about the unresolved common quadratic weight is \(C\le C+Y\le C+H\), the middle test margin \(V-2\operatorname{Tr}B(H)_+\) is the largest lower bound valid for all such weights. This is (7) with its attained optimizer. For \(H_0\) the exact gain over (15) is
\[
 \tfrac12\{\operatorname{Tr}(N_-+N_+)-\|N_--N_+\|_1\}.                    \tag{9}
\]
This follows by taking the positive and negative spectral parts of \(N_--N_+\). It is **strictly positive on every finite Wilson box at every \(\kappa>0\)** for this observation, including any calibrated cold point. Indeed \(H_0\) is injective off constants since \(\|P Q\|=r_1<1\). For nonzero real \(f\perp1\), \(P^j H_0^{1/2} f\) is nonconstant by injectivity and analytic by the Wilson kernel argument of row 1624 (14). Its equal-value pairs have \(\pi\otimes\pi\)-measure zero. Both \(\mu^\pm\) are nonzero and absolutely continuous there by that same row and its buffered form. Thus both \(N_\pm\) have strictly positive quadratic form on every such \(f\). For the positive spectral projection \(J\) of \(N_--N_+\) on the excited subspace, the gain is \(\operatorname{Tr}((I-J)N_-)+\operatorname{Tr}(J N_+)>0\): whichever projection has nonzero range contributes a positive term. This pointwise improvement has no proved lower bound in units of \(W_t\). The minimax statement concerns the specified operator interval. The actual common weight \(P^{2\theta}\) is known and need not be its optimizer.


**PROVED (removing the one-step secant while keeping integer-slab options).** Write \(h_0(r)=r(1-r)\) and \(h_\infty(r)=-r^2\log r\), with \(h_\infty(0)=0\). For an integer \(p\ge0\) define
\[
 h_p(r)=r^2\sum_{a=1}^p\frac{(1-r)^a}{a}
             +\frac{r(1-r)^{p+1}}{p+1}.
\]
At \(0<r\le1\), expansion of \(-\log r\) by integration of the geometric series gives \(0\le h_p-h_\infty\le r(1-r)^{p+1}/(p+1)\). Also \(h_{p-1}-h_p=r(1-r)^{p+1}/[p(p+1)]\) for \(p\ge1\). Hence \(h_0\ge h_p\downarrow h_\infty\). Every finite \(h_p(P)\) is a sum of integer transfer powers. Put \(S_p=S^0+2\kappa h_p(P)\) and \(R_p=P^{v-1}S_pP^{v-1}\). Use \(p=\infty\) for the logarithm. Define
\[
 \Phi_p(H)=\inf_{0\le Y\le H}-2\operatorname{Tr}[(C+Y)R_p]
          =-2\operatorname{Tr}(CR_p)
                 -2\operatorname{Tr}(H^{1/2}R_pH^{1/2})_+.                  \tag{10}
\]
In the last term the trace is of the *operator* positive part. Formula (7) proves the equality. The infimum defines a common weight for both signs. It follows from the operator ordering of the \(h_p(P)\) that \(\Phi_p(H)\) increases as \(p\) increases. Each \(\Phi_p(H)\ge0\) is sufficient for VIR-down: take \(C+Y=P^{2\theta}\), then use \(h_p\ge h_\infty\) and
\[
 -2\operatorname{Tr}(P^{2\theta}R_\infty)
      =4\big(G_\beta/t-\kappa W_t\big).                                    \tag{11}
\]
Here \(P^{2v-2+2\theta}=P^{t-2}\), so the duration term now contributes precisely \(\sum r_i^t m_i\). The uniform-in-\(Y\) error from a finite \(p\) is at most \(4\kappa G(2v-1)/(p+1)\), since \(0\le C+Y\le I\) and \(h_p-h_\infty\le r/(p+1)\) off constants. At each finite box one can therefore certify any strict \(\Phi_\infty(H_0)>0\) with finite \(p\). The finite \(p,H_0\) test only needs integer propagation times, even when \(t\) is real. This is an analytic error estimate, not a numerical evaluation.

**PROVED (a two-sided field test with an unmarked allowance).** To avoid measuring a complementary *signed* response, set \(s_n=24n^3+\kappa/2\), the norm bound of row 1624 (21), also valid for \(S_p\) since \(0\le h_p\le h_0\le1/4\). A sufficient condition is
\[
\begin{split}
 \int L_{j+1}\,d\mu^+
 +4\kappa\operatorname{Tr}\!\left(C P^{2v-2}(h_0-h_p)(P)\right)
 \ \ge\ &\int L_{j+1}\,d\mu^-\\
 &+2s_n\big[G(t-2)-\operatorname{Tr}(E P^{2v}Q)\big].                    \tag{12}
\end{split}
\]
Only the same projected predictor is charged on negative and positive pairs. The supplement on the right is an **unmarked** heat-trace difference; it still contains information about missed modes. To prove (12) sufficient, the action part of \(-2\operatorname{Tr}(CR_p)\) is the original signed integral plus the displayed credit. For any \(0\le Y\le H_\theta\), \(S_p\le s_nQ\) gives \(2\operatorname{Tr}(Y R_p)\le 2s_n\operatorname{Tr}(H_\theta P^{2v-2}Q)\). The latter trace is exactly the bracket. Taking the supremum gives \(\Phi_p(H_\theta)\ge0\). Replacing \(G(t-2)\) by \(G(2v-2)\) gives a wholly integer-time version for finite \(p\), since \(G\) decreases in time. The cost \(s_n\) grows with the slice volume. The sharper test (10) avoids that worst-case bound. Neither requires pointwise domination of \(D_j\) by a coarse prediction on negative pairs.

**PROVED (what margin is still needed at an individual cold point).** Use the strongest test here, \(\Phi=\Phi_\infty(H_\theta)\), write \(B_\infty=H_\theta^{1/2}R_\infty H_\theta^{1/2}\), and put \(\mathcal R=G_\beta/(t W_t)\). Subtracting (10) from (11) gives the exact identity
\[
 \frac{\Phi}{4W_t}
    =\mathcal R-\kappa-\frac{\operatorname{Tr}(B_\infty)_-}{2W_t},          \tag{13}
\]
where again the trace is taken after the spectral negative part. This last cost measures the favorable unresolved response for which the robust test takes no credit. In particular the exact thermal identity (11) alone is a restatement. The separate bounds (4), (10) and (12) can be proved or falsified by different data.

There is a quantitative bound on how much changing the rate can help the test. Hold the point \(t,\beta\) and the loop observation fixed, let \(0\le k_1<k_2\) be two trial rates, and write \(W_E=\operatorname{Tr}(CP^{2v-2}h_\infty(P))\). Then
\[
 4(k_2-k_1)W_E\ \le\ \Phi(k_1)-\Phi(k_2)\
                  \le\ 4(k_2-k_1)W_t .                                    \tag{14}
\]
Indeed \(C\le C+Y\le P^{2\theta}\) makes the coefficient of \(-4\kappa\) on each affine expression in (10) lie in \([W_E,W_t]\). Taking the infima proves both bounds. \(W_E>0\) because \(E\) has a nonconstant neutral reading and \(h_\infty(r)>0\) for every excited multiplier. Thus for a fixed \(t,\beta\) a deficit greater than \(4(c-\kappa)W_t\) at \(c\) cannot be recovered by reducing the rate to \(\kappa<c\). A deficit smaller than \(4(c-\kappa)W_E\) can. Points of a different characteristic must themselves be tested. The calibration fixes neither \(\mathcal R\) nor the trace term in (13).


## A cold family separating the two tests

**PROVED (strict gain at cold energies, with the reference scaling rate).** The following positive transfer families use the same visible histories and even the same two *separately charged* coarse Jordan integrals. The stronger test (10) has opposite signs in the two families at their initial cold point. This example tests what can be inferred from the observation. The transfers below are finite Markov laws.

Take an even \(N\ge6\), with uniform measure on \(N\) states divided into two equal observed cells. Write \(O=E-\Pi\), the rank-one projection onto the observed sign \(f=\pm1\), and \(F=I-E\), of rank \(N-2\). Use \(k_*=8/3,\ c=3\pi^2/11,\ w=(\log512)/k_*\). For each \(n=\ell b^K\), measure \(x=\beta-\beta_K\) from the actual calibration label, put \(t=u e^{k_*x}\) for \(0\le x\le w\), and fix
\[
 a=e^{(c-k_*)w}\log(8(N-1)),\qquad
 z=1-a/u,\qquad s=1-(a/u)e^{-cx}.
\]
Use large enough \(u>2a\). Both transfers have the form
\[
 P=\Pi+sO+rF=rI+(s-r)E+(1-s)\Pi .
\]
In family A let \(r=1-(a/u)e^{-k_*x}\). In family B let \(r=z\). Since \(0<r\le s<1\), every matrix entry is strictly positive and the displayed eigenvalues give a positive self-adjoint transfer with fixed vacuum. The two labels form the same Markov chain in both families since \(P|_{\mathrm{ran}E}=\Pi+sO\). Moreover \(G(t)=s^t+(N-2)r^t\le(N-1)\exp[-a e^{-(c-k_*)w}]=1/8\) throughout, by \(1-d\le e^{-d}\). Both families satisfy HOT and the starting purity bound \(P_K\ge64/81>457/625\). At \(x=0\) **all** excited masses lie between \(a/u\) and \(2a/u\) by integrating \(1/(1-y)\) up to \(a/u<1/2\).

With fixed vacuum and fixed eigenspaces, the row 1624 mark is exactly
\[
 S=-2s\,[s'-k_*(1-s)]O-2r\,[r'-k_*(1-r)]F.                               \tag{15}
\]
In A the second bracket vanishes and the first is \((c-k_*)(1-s)>0\). Hence \(S\le0,\ B(H)_+=0\), and \(V>0\) on the whole window because \(C\) has a strictly positive coefficient on \(O\). Thus even the integer-slab test (4) passes strictly there, and so does (10). The old test fails for every admissible buffer at \(x=0\). In fact at this point, with \(r=s=z\), the signed density is \(-D f(x_1)f(x_2)\) relative to \(\pi\otimes\pi\), where \(D=2z^{2k+1}(c-k_*)(1-z)>0\). Each Jordan part has mass \(D/2\). On opposite labels \(L_{j+1}=4z^{2j+2}\). On equal labels, which carry the negative part, \(D_j\) is \(2Nz^{2j}\) if the microscopic states differ, and zero otherwise. This follows from \(p_j(x_1,\cdot)-p_j(x_2,\cdot)=Nz^j(\mathbf1_{x_1}-\mathbf1_{x_2})\). Conditional on equal labels the two states differ with probability \(1-2/N\). Therefore
\[
 \mathcal M_{15}=(D/2)z^{2j}\,[4z^2-2(N-2)]<0 .
\]
This loss persists in the cold scaling \(u m=O(1)\) with \(N\) fixed. Row 1624's passing example has a hidden mass \(\log2\); row 1626's Wilson failures exploit large lattice energies. Here the discarded modes have the requisite slope in A and cancel in the signed complementary response.

**PROVED (what a purely observed negative charge misses).** At every \(x\) and every buffer, \(P^kFP^k=r^{2k}F\). Its endpoint kernel is supported on equal observed labels because \(F=I-E\). On those pairs \(L_j=L_{j+1}=0\) in both families. On unequal labels (15) is identical in A and B. Hence even \(\int L_s\,d\mu^+\) and \(\int L_s\,d\mu^-\) separately agree for every integer \(s\ge1\), throughout the window. All label transition probabilities, and their coupling derivatives, also agree. At \(x=0\) in B the *full* thermal rate is
\[
 \mathcal R_B=\frac{c(1-z)}{(N-1)z(-\log z)}
   \ \longrightarrow\ \frac{c}{N-1}\quad (u\to\infty).
\]
Indeed just the single \(s\) multiplier has nonzero derivative there. Since \(1-z\le-\log z,\ z>1/2\), the rate is less than \(2c/(N-1)<8/3\), using \(c<3\) and \(N\ge6\). Thus (11) is strictly negative for B at the initial point and every sufficient test (10) fails there. For even \(N\) as large as desired the rate guaranteed by these shared coarse data is at most \(c/(N-1)\) in the limit, although every level slope in B is nonnegative. A bare substitution of \(L_j\) for \(D_j\) on the negative side of (15) would pass B at rate \(8/3\): the negative integral of \(L_j\) is zero and the positive observed integral is strictly positive. This is a quantitative counterexample to that substitution. It leaves room for Wilson-specific inputs such as the unmarked remainder in (12). It also separates the sufficient long-window test from a passing seed and HOT in positive transfer families with the prescribed scaling of the cutoff labels. For the unrestricted existential choice of profile, check 1613's two-state oscillating-mass example has a passing seed and a negative fixed-time derivative at every starting point, which excludes even zero speed there. None of these is a converse theorem on calibrated pure Wilson fields.


## Recovering partially hidden modes with the same loops at several times

**ON FILE (method search).** Row 1627 §2 proves \(\|Ef_i\|<1\) for every excited Wilson eigenfunction. The polynomial description of a cyclic subspace is already used in [the shape check, line 69](gap-shape-check-opus.md). [The free-wall comparison, lines 419–422](gap-next3-max.md) exhibits small overlap of a wall vector with a light state. A further five-ref search of the YM proof directories for observability Gramians, block Hankel matrices, cyclic subspaces and time-delayed loops found the reconstruction distinction in PRs 10114/10133, notably `REVIEW_REC_CONSUMER_ALIGNMENT_ASTRA.md:47`: identifying a scalar cyclic space with the full physical Hilbert space requires extra data. Here the space will be identified on the finite box and its orthogonal complement kept in the estimate.

**PROVED (optimal common quadratic weight from finitely many delays).** Keep the same loop cells. For integer \(a=0,\ldots,L\), measure their prediction differences at \(j+1+a\). Collect them in \(y=(E P^{1+a}d_j)_{a=0}^L\), with the cell \(L^2(\pi)\) inner product in each component. Set
\[
 T_L z=(E P^{1+a-\theta}z)_{a=0}^L,\qquad
 \Gamma_L=T_L T_L^*
     =\left(E P^{2+a+b-2\theta} E\big|_{\operatorname{ran}E}\right)_{a,b=0}^L .
\]
Then \(y=T_L P^\theta d_j\). Let \(\Gamma_L^\dagger\) invert the positive eigenvalues and vanish on its kernel. Use **the same weight**
\[
 L^{(L)}= \langle y,\Gamma_L^\dagger y\rangle
       =\langle d_j,C_Ld_j\rangle,\qquad
 C_L=P^\theta J_LP^\theta,\quad
 J_L=\operatorname{proj}\mathrm{span}\{P^{1+a-\theta}\operatorname{ran}E:0\le a\le L\}. \tag{16}
\]
Indeed \(T_L^*\Gamma_L^\dagger T_L\) is the identity on \(\operatorname{ran}T_L^*\) and zero on its orthogonal complement. For any \(z\), the smallest squared norm of a vector having readings \(T_Lz\) is \(\|J_Lz\|^2\): every such vector differs from \(J_Lz\) by an orthogonal kernel vector. Thus (16) is even the largest lower bound based only on these linear readings and valid for *every* input vector. The Gram entries are unmarked cell correlations at the indicated lags, interpreted by spectral powers for a noninteger lag. At even \(t\) all entries have integer lags. No inverse of an operator on the entire slice space is needed.

We have \(C\le C_L\le C_{L+1}\le P^{2\theta}\). For the first inequality, \(P^{1-\theta} E P^{1-\theta}\) is a positive contraction supported on \(\operatorname{ran}J_0\), hence bounded by \(J_L\). For the others use nesting of the ranges. Replace \(C,H_\theta\) in (10) by \(C_L,H_L=P^{2\theta}-C_L\), and use the logarithmic duration. The resulting lower bounds \(\Phi^{(L)}\) increase by nesting of the intervals \([C_L,P^{2\theta}]\). Every one is at least the single-delay bound (13). In (12) this same replacement uses \(L^{(L)}\) on both Jordan parts and the unmarked remainder \(\operatorname{Tr}(H_L P^{2v-2}Q)\). Thus the finite-delay version also has a certificate requiring no signed readings of unobserved predictors. For a fractional Gram lag an integer upper approximation is available: replace \(P^{2-2\theta}\) in every block by the linear interpolation of its two bounding integer powers *in the exponent*. Convexity of \(s\mapsto r^s\) gives a common positive operator majorant. Conjugating by the stacked powers \(P^a E\) gives a Gram majorant, with the same kernel by injectivity of \(P\). Its inverse on the range gives a smaller, safe weight. With the upper completion \(I\) and a finite \(h_p\), this uses only integer powers.

**PROVED (exactly which modes are left, with a finite-degree estimate).** For a positive multiplier \(r\) let \(F_r\) be its spectral projection. The increasing \(J_L\) converge strongly to
\[
 J=\bigoplus_{r>0}\operatorname{proj}(F_r\operatorname{ran}E).
 \qquad \operatorname{ran}(I-J)=\bigoplus_{r>0}
          \big(\operatorname{ran}F_r\cap\ker E\big).                        \tag{17}
\]
Here the vacuum occurs in \(J\). In fact every generator of \(J_L\) has its \(r\)-component in \(F_r\operatorname{ran}E\). Conversely, each \(r>0\) is isolated for the compact \(P\). Put \(\delta_r=\operatorname{dist}(r,\operatorname{spec}P\setminus\{r\})>0\). The polynomial \([1-(x-r)^2]^q\) is one at \(r\) and has absolute value at most \((1-\delta_r^2)^q\) elsewhere on the spectrum. Applied to \(P^{1-\theta}E g\), it converges in norm to \(r^{1-\theta}F_rEg\) and takes values in \(\operatorname{ran}J_{2q}\). The eigenspaces span the neutral space by injectivity and compact self-adjointness. Taking orthogonal complements within each eigenspace proves the second assertion. In particular, for simple \(r\) with unit eigenfunction \(f\) and \(\|Ef\|>0\),
\[
 \|(I-J_{2q})f\|\ \le\
 \frac{(1-\delta_r^2)^q}{r^{1-\theta}\|Ef\|}.                              \tag{18}
\]
Use \(g=Ef/\|Ef\|\) in the polynomial argument. An arbitrarily small nonzero overlap is sufficient at a fixed cutoff. Close eigenvalues and small overlaps can require many delays. In a multiple eigenspace it is the rank of \(F_r E\) that matters. A cutoff-independent delay bound is unproved for the prescribed Wilson loops.

**PROVED (limiting test and an exact price for unseen slopes).** Put \(A=P^{(t-2)/2}S_\infty P^{(t-2)/2}\), \(D=I-J\). The increasing finite-delay margins tend to
\[
 -2\operatorname{Tr}(JA)-2\operatorname{Tr}\big((D A D)_+\big).
\]
Indeed \(J\) commutes with \(P\) by (17). The strong limits of \(C_L,H_L\) are \(P^{2\theta}J,P^{2\theta}D\). Square roots also converge strongly, by uniform polynomial approximation on \([0,1]\). Multiplication on both sides of trace-class \(R_\infty\) then converges in trace norm: approximate it in trace norm by finite-rank sums, on which this follows vector by vector. Formula (7) makes the positive-part trace 1-Lipschitz in trace norm. These facts give the asserted limit. A strict positive limit can be witnessed by finitely many delays at that point.

There is a sharper test when the hidden response is bounded separately within each energy eigenspace. Write \(D_r=F_rD\), \(J_r=F_rJ\), \(m=-\log r\), and on \(F_r\) define the log-multiplier derivative matrix \(b_r=r^{-1}F_r U^{-1} A'_\beta U F_r\), with \(A_\beta\) the normalized Wilson transfer of row 1624. Let \(b_r^h=D_rb_rD_r\) restricted to \(D_r\). The certificate in energy units is
\[
 \mathcal B(\kappa)=
 \sum_{r<1}r^t\left\{
   \operatorname{Tr}\big(J_r(b_r-\kappa m I)\big)
    -\operatorname{Tr}_{D_r}\big((\kappa m I-b_r^h)_+\big)\right\}
 \ \ge\ 0 .                                                               \tag{19}
\]
In these sums \(0<r<1\). To verify it, compress \(A\) to \(F_r\). There it equals \(-2r^t(b_r-\kappa m I)\). In the supremum pricing \(D A D\), restrict the positive contractions to contractions acting separately on the \(D_r\). This decreases the supremum. The identity on all \(D_r\) is still allowed, so the resulting lower bound still lies below the actual thermal response. Optimizing on each finite-dimensional block gives exactly \(4\mathcal B\), at least the preceding limiting certificate. The sums converge absolutely: the sum of positive-part traces of the diagonal compressions is bounded by the trace norm of \(A\), by (7) on finite block unions and passage to the limit. The exact difference from the thermal rate is
\[
 \frac{\mathcal B(\kappa)}{W_t}
   =\mathcal R-\kappa-
      \frac{\sum_{0<r<1}r^t\operatorname{Tr}_{D_r}((b_r^h-\kappa m I)_+)}
           {W_t}.                                                         \tag{20}
\]
Thus the remaining penalty beyond the true virial inequality is precisely the favorable slope in **exactly invisible** directions. An unfavorable hidden slope still costs its actual deficit, as the thermal consumer requires. In particular, partial hiding of every eigenfunction, as proved in check 1627, cannot by itself determine the sign of this test. If \(D=0\), (19) reduces to VIR-down and that identity alone contributes no scientific progress. A proof via (19) must estimate the observed response and the hidden deficit independently. The finite-delay field tests supply one way to avoid diagonalizing a large box, with the weaker bounds (10), (12). In the two-cell examples above, all delay readings and their Gram matrices agree across A and B, \(J\) is the two-label space, and (19) has the same opposite signs as (10).


## A sharp rate bound from two independent hot-box numbers

**PROVED (explicit version of (1) for Corollary B's data).** There is also an exact worst-case budget using just \(n m_{1,h}\ge\gamma>0\) and \(G(t_0,\beta_h)\le N_0\), \(N_0\ge4/21\). This avoids defining the answer by the unknown hot crossing time. Put
\[
 d_h=e^{-\gamma t_0/n},\qquad D_h=\lfloor N_0/d_h\rfloor,\qquad
 e_h=N_0-D_h d_h,\qquad
 p=\frac{n}{512t_0}\exp\!\left(J_o+\int_I\kappa\right).
\]
The sharp uniform certificate from those two numbers alone is
\[
       p\ge1,\qquad D_h d_h^{\,p}+e_h^{\,p}\le\frac4{21}.                 \tag{21}
\]
For start \(n/34\) replace 512 by 34. Equivalently take \(T=t_0p_*\) in (1), with the lower cutoff \(T\ge u\) imposed if necessary, where \(p_*\ge1\) is the unique solution of \(D_hd_h^{p_*}+e_h^{p_*}=4/21\). All constants are stated in terms of the proposed independent hot estimates.

To prove sharpness, write \(x_i=e^{-t_0m_i}\in(0,d_h]\). Their sum is at most \(N_0\). For \(p\ge1\) and two entries strictly between zero and \(d_h\), transfer mass from the smaller to the larger until one is zero or the other reaches \(d_h\). The sum of their \(p\)-th powers increases weakly since the derivative \(p x^{p-1}\) is increasing. On a finite list this leaves only full entries and at most one remainder. The resulting upper envelope is increasing in the total mass and continuous at every multiple of \(d_h\). Apply it to finite partial sums and pass to the limit. This proves the bound in (21), and its left side decreases continuously and strictly from \(N_0\) at \(p=1\) to zero. Positive Markov transfers attain it. For \(e_h>0\) take \(D_h+2\) equiprobable states, with \(E_0\) the partition projection that joins one pair and leaves all other states single. With \(\alpha=d_h^{1/t_0},\ \eta=e_h^{1/t_0}\), the transition \(\eta I+(\alpha-\eta)E_0+(1-\alpha)\Pi\) has excited eigenvalues \(\alpha\) repeated \(D_h\) times and \(\eta\) once. For \(e_h=0\) use \(\alpha I+(1-\alpha)\Pi\) on \(D_h+1\) states. For \(0<p<1\), taking \(M\) equal \(t_0\)-weights \(N_0/M\le d_h\) yields \(N_0^p M^{1-p}\), unbounded with \(M\), by the same averaging-matrix construction. Thus an earlier period cannot be guaranteed from these two numbers. Corollary B's exponential bound is recovered by replacing \(e_h^p\) by \(e_h d_h^{p-1}\). This sharpness concerns the stated information about a spectrum, and supplies neither hot number for Wilson.

## Comparison laws and the band sign

**PROVED (where the best test fails).** In the free transverse photon and the compact Gaussian \(U(1)\) model of row 1618 Theorem 2, check 1622, use zero monopoles and zero spatial magnetic flux, with the three half-turn projections in the compact model. There the levels are \(m=E_{\rm ph}+e_Q\), \(e_Q=|Q|^2/(2\beta n)\), \(Q\in(2\mathbb Z)^3\). The oscillator transfer is independent of \(\beta\) after Gaussian rescaling and the rotor log-multiplier slope is \(e_Q/\beta\). These are ON FILE in rows 1618, 1624 (18). The flat-shift invariance of contractible flowed loops in row 1626 (12)–(13), checked at 1627, puts \(E\), every delayed reading and \(J\) in the zero-charge sector. The dynamics in that sector are the free photon. Thus in (19) an excited zero-charge photon of mass \(m\) contributes \(-\kappa m e^{-tm}\) per state, whether visible or hidden. All other sectors are hidden and their contribution to (19) is nonpositive. Consequently
\[
                 \mathcal B(\kappa)\le
         -\kappa\sum_{\mathrm{excited\ zero\!-\!charge\ photons}} m e^{-tm}<0
                 \quad(\kappa>0).                                          \tag{22}
\]
For the pure photon the zero-charge sector is the whole space, so this is equality for every observation. At \(\kappa=0\) the rescaled comparison gives zero in (19) for both models: the positive rotor slopes are invisible and all observed slopes vanish. The estimate is valid at every admissible time, including cold points. Finite-delay tests also fail at positive speed by their ordering below (19). In particular the compact model's failure below \(9/(10\beta)\) on the cold boxes of row 1618 is a failure of the observation, even where its full virial inequality passes. Block derivatives on one eigenspace are invariant under differentiable unitary changes of coordinates, since the compression of a commutator with the transfer vanishes there. The zero-charge dispersion and the duration of rotor diffusion are properties of the probability law. Flat-shift invariance alone gives neither slope. [Compact Gaussian theorem](gap-vir-down-neon.md) · [Sector comparison](gap-vir-down-dom-astra62.md)

**ON FILE / PROVED implication (rows 1553, 1573/1579, 1613 and 1617).** Lemma ALG allows no conclusion from the gauge algebra and dimension alone. For a strong test of this point, append a decoupled, coupling-independent neutral oscillator with \(um<\log2\) to the Wilson factor. Its initial \(G>1/2\); any HOT endpoint with \(G\le4/21\) then has a preceding last point with \(G=1/2\). By the mean value theorem there is an interior cold point with \(\mathcal B(\kappa)\le G_\beta/t-\kappa W_t\le-13/(42wt)\). This uses the change of \(G\) over a subinterval of length at most \(w\). The original Wilson factor and its loop law persist. The same implication at the original aspect applies to interacting weak compact Wilson \(U(1)\) given row 1573's periodic Villain comparison, which gives \(G_{\rm even}(u)>1\). For weak **five-dimensional Wilson \(SU(2)\)** a neutral level with \(um<\log2\) would give that failure too. I have no such bound for the interacting five-dimensional law. The algebraic projection and transport arguments hold in that dimension as well. [Lemma ALG](gap-mech-direction4-fable.md) · [Abelian comparison](gap-band-neutral-astra62.md) · [Check of the comparison](gap-direction7-fable-check-astra62.md)

**PROVED (strength test using an on-file separation).** In the mode interchange of row 1624 the original observation passes (15) throughout the long window. Equations (8), (10), (16) and (19) therefore pass too. Interchanging the two signs leaves the entire spectrum, HOT, the true thermal response and all purities fixed. Now the observed sign is the coupling-independent multiplier \(1/2\), and the fixed product eigenbasis leaves its one-dimensional excited space invariant under every delay. The observed term of (19) is \(-\kappa 2^{-t}\log2<0\), and the hidden term only subtracts. Thus (19) gives opposite answers on two isospectral laws. It is strictly stronger than the pointwise thermal inequality in this setting. Equivalence or strictness for the calibrated *pure Wilson* family remains unproved. [Interchange and check](gap-vir-down-tool-astra62-check-opus.md)

**ARGUED (Wilson verdict).** The actual amount to compare with the geometric headroom \(c-\kappa\) at a cold point is
\[
       c-\mathcal R+
       \frac{\sum_{0<r<1}r^t\operatorname{Tr}_{D_r}((b_r^h-\kappa m I)_+)}{W_t}.
\]
Equation (20) proves that a strictly smaller value is exactly a strictly positive margin for (19). The beta-function slope in check 1453 does not estimate the first difference. Check 1627's partial-hiding result does not estimate the second. The cold pair A and B above meet the same calibration labels, the same HOT threshold and all the same observed predictions and yet give opposite signs. Deciding the sign for the specified Wilson law needs information on its coupling derivative, for instance a lower bound for the observed slope together with an upper bound for the hidden adverse trace in (19). I do not have either estimate uniformly on the required cold points. In particular I have proved a positive improvement over (15) there, and I have neither proved a positive absolute Wilson margin nor proved that it is nonpositive.


**PROVED (size of the unresolved estimate on Wilson boxes).** Define the exactly invisible thermal-energy fraction and the observed rate at this point by
\[
 h=\frac{\sum_{0<r<1}m r^t\,\dim D_r}{W_t},\qquad
 c_o=\frac{\sum_{0<r<1}r^t\operatorname{Tr}(J_r b_r)}{(1-h)W_t}.
\]
The nontrivial loop reading and injectivity give \(h<1\) at each fixed box. If \(b_r^h\ge \rho m I\) on every hidden block, (19) gives the sufficient numerical inequality
\[
 \frac{\mathcal B(\kappa)}{W_t}
     \ \ge\ (1-h)(c_o-\kappa)-h(\kappa-\rho)_+.                            \tag{23}
\]
This follows by bounding each eigenvalue of the adverse hidden block. When \(c_o>\kappa>\rho\), a strictly positive margin is assured by \(h<(c_o-\kappa)/(c_o-\rho)\). For example, *if* \(c_o\ge c\) and all hidden slopes are nonnegative, the allowable \(h\) is \(1-88/(9\pi^2)\) at \(8/3\) and \(1-88\log34/(9\pi^2\log512)\) at the changed-aspect rate (3), with strict inequality at these endpoints. These fractions concern exactly invisible energy. Recoverable partial overlap has already been accounted for by (17).

A universal finite-box substitute for the unproved sign \(\rho=0\) follows from the Wilson action. Row 1617, using row 710 Theorem U(ii), writes the unnormalized log-eigenvalue derivative \(D_\psi=\langle\psi,T'\psi\rangle/\lambda\) as the electric average of \(\sum_e[k_e/\beta+I_{k_e+2}(\beta)/I_{k_e+1}(\beta)-1]\), less the spatial action mean in \(\psi\). Every summand is at least \(-1\) and the spatial action is at most \(6n^3\), whence \(D_\psi\ge-9n^3\) for each unit eigenvector. The shifted nonnegative slab action and positive vacuum give \(D_\Omega\le0\) by differentiating its matrix element. Thus \(D_\psi-D_\Omega\ge-9n^3\) as a quadratic-form bound on every eigenspace, including the hidden compression. At a cold point \(tm\ge\log2\) for every excited level since \(e^{-tm}\le G\le1/2\). Hence (23) applies on the actual band with \(\rho=-9n^3t/\log2\). Even if \(c_o=c\), this only certifies a strict margin for \(h<(c-\kappa)/(c+9n^3t/\log2)\); no estimate on file puts the hidden fraction below it. This bound shows precisely what the elementary Wilson score pays. Both \(c_o\) and the hidden low-energy response require a result on the field law at physical times. [Wilson eigenspace action formula, row 1617](gap-vir-down-astra62.md)

**RESULT (d), a two-sided tool and an exact conditional rate budget.** PROVED (1)–(3) and (21) give the required mean for a specified hot certificate. The original fixed window allows zero reduction from \(8/3\); the checked aspect-34 handoff allows \(8\log34/(3\log512)\) on a different characteristic.
PROVED (4), (8)–(12) use the same observed prediction on both signs. The gain over (15) is strict on each finite Wilson box at positive speed. PROVED (16)–(20) recover partially visible eigendirections by time delays and isolate the cost of exactly invisible slopes.
PROVED a cold transfer family where the new test passes and (15) fails, and a second with identical observed data and limiting thermal rate \(c/(N-1)\). PROVED (22) excludes every positive speed for the photon and for contractible loops in compact Gaussian \(U(1)\).
The absolute sign on the calibrated four-dimensional Wilson cold band is unresolved. Formula (23) gives a sufficient hidden-energy tolerance. HOT there, a weak interacting five-dimensional exclusion, (PUR-io), and the mass gap remain open. All new proofs are hand arguments. No Lean or numerical computation is used as evidence.

