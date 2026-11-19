# Repo search

**GUIDE.** Row 1161, checkout `263ef6074`. The target-specific prior note is absent. The 8 November search covers thirteen earlier, chiefly ultraviolet questions. Its gap supplement points to the soft route and to the existence snapshot. At PR 10114 (`f76f6c649c`) the positive one-plaquette matrix element and the contraction for \(0<\beta\le1/32\) concern another scale. PR 10133 has the identical local-block source. The older hard-route tree on PR 10134 contains the goal and predates row 720. At PR 10141 (`a2f6a430e2`) the estimate in `research/ym4d/library/fp1.md`, lines 302–315, controls a constrained classical field in one step. Main at `8b11ae2bb9` gives a gapless observable sector for a finite cyclic Villain model in the specified coupling regime. Its link group and plaquette weight differ from the ones here. The W entry in the open registry points to the T0 reconstruction tree. I found no other owner of this continuation. [Lead search](prior/repo-search-2026-11-08.md) · [Gap supplement](prior/gap-crux-prior-ym.md) · [Scope of the wall](../parts/gap.md)

**GUIDE.** I use the positive projected transfer and periodic trace identity GL8 of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, outline lines 2313–2336. Their outline lines 31871–31882 distinguish a gap from polynomial decay. CA-I lines 2704–2712 explicitly leave the gap outside the theorem. Credit Tadeusz Bałaban for the upstream renormalization group and Sourav Chatterjee for the weak-coupling free-energy method in the preceding rows. The 4.12–4.19 index concerns stages of the ultraviolet induction. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2313-L2336) · [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

## Plan and outcome

**GUIDE.** Verify the hypotheses and quantifiers inherited from the preceding rows. Seek a proof or a counterexample, starting from the two outstanding estimates. Record each deduction, its status, and the obstruction to any unsuccessful route.

**GUIDE.** The one-cube theorem (9) and its explicit aspect bound give the periodic-wall criterion. Equations (19) and (24) give unconditional Wilson spectral estimates. Equation (26) characterizes the local finite-volume seed using only neutral traces at aspect two. Every PROVED label refers to a hand argument under its stated hypotheses. This research row has had no independent check and grants no scientific status.

**OPEN.** The Jaffe–Witten target here requires a nontrivial four-dimensional \(SU(2)\) theory with a strictly positive energy gap above the vacuum. The assigned wall is a sufficient finite-volume route to its gap clause. Fix the lane’s cutoff trajectory \(a_j,\beta_j\), a permitted physical side \(L\), \(n=L/a_j\) on its grid, and \(T=n/2\). With \(U=F/\|F\|\) on the full gauge-invariant periodic slice, the strict purity test is \(\liminf_j\operatorname{Tr}U^{2T}/(\operatorname{Tr}U^T)^2>1650/1651\) for some such \(L\). Row 720 also gives the equivalent wall with the domain \(L\ge4L_0\). The preceding chain through row 1155 has its recorded checks. I use the two newer rows as unchecked research inputs and give the arguments for the comparisons used below. The council’s neutral-spectator obstruction applies throughout. [Row 720](gap-phys-seed.md) · [Row 1155](gap-solve7-astra62.md) · [Row 1157](gap-solve8-astra62.md) · [Row 1158](gap-paths-fable.md) · [Council](gap-council-synthesis.md)

## A direct comparison between a twist trace and two-slice overlap

**PROVED.** Work at finite cutoff on the periodic cube. Write \(\psi>0\) for the normalized vacuum of the symmetric magnetic sandwich \(F\), \(\pi(dx)=\psi(x)^2dx\), and \(P=\psi^{-1}U\psi\) for its reversible Markov operator. Positivity of the finite-volume kernel gives a simple vacuum. The centre flips \(G=(\mathbb Z/2)^3\) fix \(\psi\) and commute with \(P\). Let \(p_t(x,y)\) be the density of \(P^t\) relative to \(\pi\), \(q_t=8^{-1}\sum_{g\in G}p_t(x,gy)\) the neutral kernel and \(R\) any nonidentity centre flip. Set
\[
 \tau_R(t)=\int\min\{p_t(x,y),p_t(x,Ry)\}\,d\pi(x)d\pi(y),\quad
 I_R(2t)=\operatorname{Tr}(R P^{2t}),\quad
 s_+(2t)=\operatorname{Tr}(P_+P^{2t})-1 ,
\]
where \(P_+\) is the group average. \(I_R(2t)\) is the Wilson partition function with temporal twist \(R\) in units of the vacuum eigenvalue to power \(2t\). For every integer \(t\ge1\) and every \(A>1\),
\[
 \boxed{\ I_R(2t)\ \le\ 8A\,\tau_R(t)+4\left(\frac A{A-1}\right)^2s_+(2t).\ } \tag{1}
\]
In particular if the ordinary twist ratio \(f_R(2t)=I_R(2t)/\operatorname{Tr}P^{2t}\) exceeds \(16s_+(2t)\), the overlap is at least \((f_R(2t)-16s_+(2t))/16\). The transfer trace is at least one.

**PROVED.** In the product measure \(\pi\otimes\pi\), symmetry and composition give \(I_R(2t)=\int p_t(x,y)p_t(x,Ry)\) and \(\int(q_t-1)^2=s_+(2t)\). On \(q_t\le A\), both factors are bounded by \(8A\). On the invariant set \(q_t>A\), average the product over the orbit of \(y\). Write \(a_g=p_t(x,gy)\). Pair \(g\) with \(Rg\). The average is \(\tfrac14\sum_{\rm pairs}a_ga_{Rg}\le\tfrac1{16}(\sum_g a_g)^2=4q_t^2\). Repeated orbit points cause no problem in this group sum. Finally \(q_t^2\le[A/(A-1)]^2(q_t-1)^2\) on the latter set. This proves (1) with no estimate on the vacuum density or on a bridge with prescribed endpoints.

**PROVED.** Let \(b\) be the leading eigenvalue of \(P\) in a character odd under \(R\), and \(\rho\) the first excited neutral eigenvalue. For every pair of positive integers \(t,u\),
\[
  \tau_R(t)\le 1-b^{2t}
              +b^{2t}\frac{1-b^u}{1-\rho^u}.                            \tag{2}
\]
In particular \(1-b^{2t}\ge (1-\rho^{2t})\tau_R(t)/(2-\rho^{2t})\). This is linear in the overlap, improving the quadratic dependence in row 1158 under the same hypotheses.

**PROVED.** Choose a real normalized eigenfunction \(h\) in the character. Contraction of absolute value in the Dirichlet form of \(P^u\) gives \(1-(\int |h|\,d\pi)^2\le(1-b^u)/(1-\rho^u)\), since \(|h|\) is neutral. Round \(h\) to its sign \(\sigma\), with any sign of the same character on the zero set. Such a sign exists almost everywhere, for instance a product of the requisite winding-loop trace signs. Their zero sets are Haar null and \(\pi\) is absolutely continuous. Since \(R\sigma=-\sigma\), the conditional mean \(P^t\sigma(x)\) is half the integral of \(\sigma\) against the difference of the two conditional laws. Its absolute value is at most their TV distance \(1-\tau_t(x)\). Hence \(\|P^t\sigma\|_2^2\le1-\tau_R(t)\). Projection onto \(h\) gives \(\|P^t\sigma\|_2^2\ge b^{2t}(\int|h|\,d\pi)^2\). Combining gives (2). Put \(u=2t\) and bound the coefficient \(b^{2t}\) above by one for the last assertion. This uses the sign rounding of row 1157 and the two-slice experiment of row 1158. [Row 1157, electric characters](gap-solve8-astra62.md) · [Row 1158, Lemmas F and T](gap-paths-fable.md)

**OPEN.** Neither inequality yet bounds \(I_R\) from below or \(s_+\) from above for the physical Wilson cube. A positive twisted ratio measured at a time sufficiently short compared with \(n\) could now be used without measuring a vacuum-conditioned overlap. The scale restriction matters.

## Fractional momentum removes six possible slow channels in each nonzero magnetic sector

**GUIDE.** The compensated spatial translations and their fractional momenta are prior work, including the credit to ’t Hooft. I use equation (6a) of the lane’s channel calculation. The application here combines this symmetry with the *untwisted* neutral trace bound. All energies in the comparison use the same periodic vacuum. [Channel calculation, §1.2](gap-channel-astra.md) · [Check of (6a)](gap-channel-check-opus.md) · [Twisted Wilson transfer](gap-transfer-twisted.md)

**PROVED.** Take any three-dimensional rectangular spatial torus with all sides even and at least four. Write \(m=(m_{23},m_{31},m_{12})\in\mathbb F_2^3\) for the magnetic vector and \(q\in\mathbb F_2^3\) for the electric character. Let \(M=(m_{ij})\) be the alternating spatial matrix. In sector \((m,q)\) every positive eigenvalue has even real multiplicity if \(Mq\ne0\). In particular this holds for six of the eight electric characters at every \(m\ne0\). Indeed \(\ker M=\{0,m\}\) for such \(m\). Pick an \(i\) with \((Mq)_i=1\). The real orthogonal compensated unit translation \(D_i\) preserves the sector and commutes with its transfer. On it \(D_i^{n_i}=-I\). In the explicit stacks \(x_i=n_i-1,x_j=n_j-1\), moving one step in \(i\) is compensated by flipping \(j\)-links at \(x_i=0,x_j=n_j-1\) for each \(m_{ij}=1\). This moves the stack back. After \(n_i\) steps it has swept precisely the full flip planes \(\prod_j C_j^{m_{ij}}\), yielding the formula. On a finite real eigenspace an odd dimension is impossible, since an even power of a real determinant cannot be \(-1\). Compactness makes each positive eigenspace finite-dimensional.

**PROVED.** Normalize every static magnetic transfer \(F_m\) by \(\lambda_0=\|F_0\|\) of the same spatial box. Write \(X_{m,q}(v)=\operatorname{Tr}_{q}(F_m/\lambda_0)^v\), \(s(v)=X_{0,0}(v)-1\), and \(b_{m,q}=\|F_m|_q\|/\lambda_0\), with zero for a missing sector. For each integer \(u\ge3\),
\[
 0\le X_{m,q}(u)\le X_{m,0}(u)\le X_{0,0}(u)=1+s(u),\qquad
 b_{m,q}\le1.                                                         \tag{3}
\]
The first upper bound follows from Fourier inversion of the eight positive twisted integrals. For the second, sum the original temporal twists, giving eight times the electric-neutral trace. Regard a spatial direction \(i\) as time and fix the temporal bits with neither index \(i\), as well as the static magnetic bits in this new frame. The sum over the old \(i\)-time bit inserts the projection even under its flip, times two. Removing the remaining seam involutions increases the trace against the commuting positive operator with this projection. This erases the old magnetic bits incident to \(i\) while retaining the old temporal sum. Repeat in the three spatial directions. This is row 1157 (19) in trace units. Taking arbitrarily large powers proves \(b_{m,q}\le1\).

**PROVED.** If \(s(u)\le s_0<1\), put \(d=(1+s_0)/2<1\). For \(v\ge u\) the two resulting bounds are
\[
\begin{split}
 X_{m,q}(v)&\le(1+s_0)d^{v/u-1} &&(Mq\ne0),\\
 0\le X_{m,q}(v)-b_{m,q}^{\,v}&\le(1+s_0)d^{v/u-1}
                          &&(\text{every }m,q).
\end{split}                                                            \tag{4}
\]
For the first line the largest eigenvalue occurs at least twice, so (3) bounds its \(u\)-th power by \(d\). For the second remove just the first eigenvalue. The same estimate bounds the \(u\)-th power of the second, counting multiplicities, in *every* sector. Spend the remaining \(v-u\) steps on this bound. In the periodic neutral sector the surviving term is exactly one. A short-period neutral trace strictly below two is the only thermal hypothesis. Neither a gap nor a trace estimate normalized by a twisted vacuum is required. This estimates 42 entire sectors of the actual twisted Wilson transfers.

## A neutral estimate makes torus twist weights nearly invariant under changes of basis

**PROVED.** On an even rectangular four-torus \(Q\), represent a twist by its alternating \(4\times4\) matrix \(B\) over \(\mathbb F_2\). Let \(f_Q(B)=Z_B(Q)/Z_0(Q)\). Suppose that in each coordinate time frame \(i\), with time length \(v_i\), its *periodic*, electric-neutral spatial transfer satisfies \(s_i(u_i)\le s_0<1\) at some integer \(3\le u_i\le v_i/K\), with \(K\ge1\). Put \(h=(1+s_0)((1+s_0)/2)^{K-1}\). Then
\[
 |f_Q(B)-f_Q(B')|\le160h\qquad
                  \text{whenever }\operatorname{rank} B=\operatorname{rank} B'.       \tag{5}
\]
No geometric symmetry between sides of unequal lengths is assumed.

**PROVED.** Replace the \(i\)-th basis vector of the four-dimensional bit space by its sum with the \(j\)-th, \(j\ne i\). In frame \(i\), this preserves the static matrix \(M\) and adds its \(j\)-row to the temporal star \(e\). In the electric Fourier expansion
\[
  f_Q(B)=\frac{\sum_q(-1)^{q\cdot e}X_{m,q}(v_i)}
                     {\operatorname{Tr}(F_0/\lambda_0)^{v_i}},
\]
every sign that changes has \((Mq)_j=1\). There are either zero or four such signs. Their coefficients are bounded by \(h\) by (4), with denominator at least one. The change in \(f_Q\) is at most \(8h\). A nonzero alternating form can be put in the same normal form as any other of its rank with at most ten such additions per form. Move an entry with value one to positions \(1,2\) by at most two coordinate swaps, each costing three additions over \(\mathbb F_2\). For \(k=3,4\) replace \(e_k\) by \(e_k+B_{2k}e_1+B_{1k}e_2\) to clear its pairings with \(e_1,e_2\). The remaining \(2\times2\) alternating block is zero or the standard nondegenerate block according to the rank. This proves (5), including the trivial rank-zero case. These are transformations of the **twist indices**, at fixed side lengths. The estimate comes from magnetic translations of the actual Wilson transfers.

**GUIDE.** Earlier Theorem R classifies light flux sets from small periodic neutral trace and small vacuum-energy additivity defect. Earlier (23) of row 1157 controls all twists when the transverse marginal is nearly uniform. Equation (5) uses neither the vacuum-energy defect nor a marginal frequency, and compares ranks on rectangular tori before a flux phase is selected. The two references supply different input conditions. [Earlier Theorem R, §4](gap-means-max.md) · [Earlier transverse criterion](gap-solve8-astra62.md)

## Two periods exclude intermediate twist weights

**PROVED.** Let \(4\mid n\), \(t=n/2\), and use the same coupling on \(Q_t=(n,n,n,t)\) and \(Q_{2t}=(n,n,n,2t)\). Assume the short-time neutral condition preceding (5) on both rectangles with the same \(s_0,K\). There are only two different periodic spatial boxes, \(n^3\) and \(n\times n\times t\). For either box use its own periodic vacuum. Define \(\eta=2561h\), and suppose \(\eta\le1/100\). At this cutoff one of the following alternatives holds on \(Q_t\).

- **PROVED, first alternative.** The ordinary periodic excited sum is at most \(78\eta\). All 64 twist ratios lie in \([1-108\eta,1]\). In each nonzero magnetic sector the sum of all thermal weights after removing its vacuum, normalized in units of the *periodic* vacuum at \(t\), is at most \(16\eta\).
- **PROVED, second alternative.** Every nontrivial twist ratio is at most \(11\eta\). Each of the seven nonzero electric characters in the periodic box has a state of weight at least \(1-20\eta\) at time \(t\). The sum of the neutral periodic excited weights and the full thermal weights of the seven nonzero magnetic boxes is at most \(78\eta\), in the same units.

**PROVED.** In the rest of this argument use the \(n^3\) vacuum \(\lambda_0\) and write \(I_v(B)=Z_B(Q_v)/\lambda_0^v\). By (3), \(1\le I_v(0)\le8(1+s_0)\le16\). Thus two rank-two twists differ in \(I_v\) by at most \(\eta\) at each period. Set \(c_v=\frac17\sum_{q\ne0} X_{0,q}(v)\). It decreases with \(v\) since all normalized eigenvalues are at most one. The average of \(I_v\) over the seven nonzero purely temporal twists is \(1+s(v)-c_v\), by Fourier inversion. Write \(y=1+s(t)-c_t\). Then \(0\le y\le1+h\). For any fixed nonzero, purely spatial twist \(m\), let \(Y_v=I_v(m,0)\), where the second index is the temporal seam. This has rank two at both periods. Hence
\[
   |Y_t-y|\le\eta,\qquad Y_{2t}\ge1-c_t-\eta\ge y-2\eta,\qquad
   Y_{2t}\le Y_t^2.                                                     \tag{6}
\]
The last bound is the trace-of-a-square inequality for the *same* positive magnetic transfer on \(n^3\). It follows that \(y(1-y)\le2\eta+2y\eta+\eta^2\le5\eta\).

**PROVED.** If \(y\le1/2\), then \(y\le10\eta\). Every rank-two \(I_t\) is at most \(11\eta\), directly by comparison with the temporal average. Each rank-four twist has a nonzero static component, and removing its temporal flip gives an upper bound of rank two. Consequently every \(X_{m,0}(t)\) and even the full sum \(Y_t\) for \(m\ne0\) are at most \(11\eta\). The claimed \(78\eta\) follows from \(s(t)\le h\). Also \(I_t(0)=8[1+s(t)]-7y\ge8-70\eta\). Fourier inversion in \(m=0\), using the seven bounds \(11\eta\), gives \(X_{0,q}(t)\ge1-19\eta\). Equation (4) removes the whole tail after the first level at cost \(h\le\eta\). This proves the second alternative.

**PROVED.** If \(y>1/2\), then \(1-y\le10\eta\) and \(c_t\le11\eta\). The periodic excited sum is \(s(t)+7c_t\le78\eta\). Every nonzero static \(m\) has \(Y_t\le1+2\eta\) and \(Y_{2t}\ge1-12\eta\). Put \(a_m=\|F_m\|/\lambda_0\). Since \(Y_{2t}\le a_m^tY_t\), we obtain \(a_m^t\ge1-14\eta\) and \(Y_t-a_m^t\le16\eta\). Its simple positive vacuum is fixed by all commuting flips, so \(I_t(m,e)\ge 2a_m^t-Y_t\ge1-30\eta\) for every temporal seam \(e\). For \(m=0,e\ne0\) the rank-two comparison gives \(I_t\ge y-\eta\ge1-11\eta\). Divide by \(I_t(0)\le1+78\eta\) for the lower ratio bound. The upper bound one follows by dropping temporal twists in successive frames. This proves the first alternative.

**PROVED (a flux-independent seed for the local sector).** Let \(S_\kappa(t)=s(t)+\sum_{m\ne0}X_{m,m}(t)\). In the first alternative each summand is bounded by the magnetic excited weight \(16\eta\), since its electric character is nontrivial. In the second it is bounded by the full weight \(Y_t\le11\eta\). Thus
\[
                  S_\kappa(t)\le113\eta                                   \tag{7}
\]
in either case, even when the alternative varies with the cutoff. \(S_\kappa\) is the earlier Pfaffian-weighted seed, which has a positive sector trace in every frame. If the hypotheses at one fixed physical side hold eventually and \(113\eta<1/5041\), the lane’s Theorem S-w propagates this seed and gives the gap on its centre-blind local observable space under the lane’s limit hypotheses. This does not yet give the assigned periodic wall in the second alternative. Earlier Theorem R requires a small vacuum additivity defect. The present implication replaces that input by a neutral thermal bound strictly below two at an earlier time on two specified periodic spatial shapes. [Pfaffian seed and its local consumer, §§3.1 and 8.4](gap-flux-exercise.md) · [Earlier even-seed theorem](gap-means-max.md)

**PROVED (a weaker transverse requirement for the periodic wall).** Suppose also that the all-twist mixture on \(Q_t\) has probability greater than \(616\eta\), with uniform strict margin in the cutoff, of a *nonzero* restriction to one transverse three-torus. In the second alternative at most 56 configurations have a nonzero restriction, each with probability at most \(11\eta\), since the unrestricted denominator contains \(Z_0\). Thus only the first alternative is possible eventually, and \(78\eta<1/1650\) gives (W). The observable is the complementary event to row 1157’s zero-class reading. Its vanishing decoding error on these tori preserves a strict margin. The new condition only asks that some magnetic flux occur with positive frequency at the accuracy set by \(K\). Row 1157 (25) tests accuracy around the uniform value.

**OPEN.** The neutral bound is required at a time at most a \(1/K\) fraction of the corresponding side. A neutral trace below two on an arbitrarily long cylinder would follow from compactness at fixed cutoff and cannot be substituted in this proof.

## One periodic cube suffices

**PROVED.** Let \(n_k\to\infty\), \(4\mid n_k\), and let the Wilson couplings vary arbitrarily. Suppose that on the **single periodic spatial cube** \(n_k^3\) there are integers \(u_k\ge3\) with \(n_k/u_k\to\infty\) and
\[
                     s_k(u_k)\le s_0<1.                                 \tag{8}
\]
Along every subsequence there is a further subsequence with exactly one of the following two limits. Write \(v_k/n_k\to r>0\), \(\lambda_k=\|F_{0,k}\|\). The same subsequence works for every \(r>0\) and every such sequence of integer periods.
\[
\begin{array}{c|cc}
 & Z_B(n_k^3,v_k)/\lambda_k^{v_k} & \text{sectors of limiting weight one}\\ \hline
 \mathrm{I}  & 1\quad\text{for all }B &(m,0)\quad\text{for all }m\\
 \mathrm{II} & 8\,{\bf1}_{B=0} &(0,q)\quad\text{for all }q .
\end{array}                                                             \tag{9}
\]
The sectors in the right column have magnetic index first. All other sectors have weight tending to zero. Each weight-one sector has exactly one level carrying its weight in the limit. In particular \(S_\kappa(\lfloor rn_k\rfloor)\to0\) on the **original sequence**, regardless of alternation between I and II. No neutral information on a second spatial shape is required.

**PROVED (compactness in the time variable).** Pass to a subsequence on which all 64 numbers \(b_{m,q}^{\,n_k}\) from (3) converge to \(a_{m,q}\in[0,1]\). For \(r>0\), (4) gives \(X_{m,q}(v_k)\to a_{m,q}^{\,r}\), with \(0^r=0\). This follows for any varying \(v_k/n_k\to r\) by bounding the exponent between two positive constants near \(r\). If \(Mq\ne0\) the limit is zero. The remaining possible indices are \((0,q)\), \((m,0)\), and \((m,m)\) for \(m\ne0\), with \(a_{0,0}=1\). In the chosen time frame let
\[
       I(r,B)=\sum_q(-1)^{q\cdot e}a_{m,q}^{\,r}.
\]
This is the limit of the normalized integral on the left of (9). It is real analytic for \(r>0\), being a finite sum of exponentials with zero entries omitted. This interpolation is derived from actual integer-period traces. No torus of noninteger length is needed.

**PROVED (a vanishing crossed coefficient has zero slope).** For any frame \(i\), static class \(c\) in that frame and character \(q\), define
\[
       H_{i,c,q}(r)=\tfrac18\sum_e(-1)^{q\cdot e}I(r,B_i(c,e)).
\]
It is nonnegative for *every* real \(r>0\). Indeed for \(v_k/n_k\to r\) its approximants are genuine positive sector traces in frame \(i\), divided by the positive \(\lambda_k^{v_k}\) of the original frame. At \(r=1\) take \(v_k=n_k\) exactly. All frames now have the same cubic periodic neutral bound (8), and \(\lambda_k^{v_k}\) is also the rotated vacuum normalization. For \(M_iq\ne0\), (4) gives \(H_{i,c,q}(1)=0\). Nonnegativity on both sides of the interior point and differentiability imply \(H_{i,c,q}'(1)=0\). Positivity away from the symmetric point is all that is required of the rectangular boxes.

**PROVED (rank and its first derivative).** Repeat the single basis addition of (5) in the Fourier expansion of \(I(r,B)\) in frame \(i\). All coefficients that change sign have \(M_iq\ne0\). Their values and derivatives vanish at \(r=1\). Thus both \(I(1,B)\) and \(\partial_r I(1,B)\) are constant on each rank. In the periodic magnetic sector, all seven nonzero purely temporal twists have the same value at \(1\). Fourier inversion therefore gives \(a_{0,q}=b\) independent of \(q\ne0\). For each of these temporal twists \(I(r,B)=1-b^r\). For any nonzero purely spatial twist \(m\), also of rank two, \(I(r,B)=A_m^r+C_m^r\), with \(A_m=a_{m,0}\ge C_m=a_{m,m}\ge0\) by (3) or by the positive magnetic vacuum. Equality of values and derivatives yields
\[
       A_m+C_m=1-b,\qquad
       A_m\log A_m+C_m\log C_m=-b\log b,\qquad 0\log0=0.              \tag{10}
\]
Every term on the left of the derivative identity is nonpositive and its right side is nonnegative. Consequently \(b,A_m,C_m\) all belong to \(\{0,1\}\). If \(b=0\) then \(A_m=1,C_m=0\) for every \(m\ne0\). If \(b=1\) then \(A_m=C_m=0\) for every \(m\ne0\). Fourier inversion gives precisely (9). This use of the *derivative* eliminates the extra geometry in (6), including from its hypotheses.

**PROVED (one finite aspect, with the order of choices).** For every \(s_0<1\), \(s_0\ge0\), tolerance \(\epsilon>0\), and fixed compact interval \(J\subset(0,\infty)\), there exists an integer \(K\) such that the following holds for **every** even cube with \(4\mid n\), every coupling, and \(3\le u\le n/K\) with \(s(u)\le s_0\). One of the alternatives (9) approximates all 64 normalized partition functions and all 64 sector weights within \(\epsilon\), simultaneously at every integer \(v\) with \(v/n\in J\). If this assertion failed, take counterexamples with \(K\to\infty\). They satisfy (8). A failure of the approximation for the alternative selected by (9) has a subsequence with a fixed offending index and \(v/n\) converging in \(J\), contradicting the convergence just proved. The same argument bounds the omitted higher-level weights by \(\epsilon\) using (4). This is an existence argument for \(K\) independent of \(n,\beta,L\).

**PROVED (consumer).** Choose \(s_0=1/2\), \(J=[1/2,1]\), and \(\epsilon<1/(8\cdot5041)\), then choose \(K\) as just proved. A cutoff-uniform neutral excited sum \(\le1/2\) at \(u=\lfloor n/K\rfloor\) on one admissible physical cube is sufficient for the Pfaffian seed because its seven nonzero \((m,m)\) sectors are absent in both alternatives and its periodic neutral excited sum is at most \(\epsilon\). A uniform lower bound on the probability of any nonzero transverse class greater than \(56\epsilon\) on \(Q_t\) selects I, since in II its 56 normalized weights are at most \(\epsilon\) each and the denominator is at least one. In I the periodic excited sum is at most \(8\epsilon\), giving (W). This turns the sharp class-frequency test of row 1157 into a choice between two alternatives after a **single untwisted neutral** test. In particular a probability bounded below by \(1/10\) suffices with these choices. The \(\epsilon\) can be chosen smaller before \(K\) if the proposed frequency floor is smaller.

**PROVED (necessity over physical sizes).** Under (W), for every fixed \(K\) the ordinary trace, hence also the periodic neutral trace, has arbitrarily small excited sum at \(\lfloor n/K\rfloor\) on sufficiently large fixed dyadic sides, with the cutoff limit taken first. To see this choose \(2^d\ge K\), set \(b=n/2^d\) on enlarged grid sizes and use the propagated shape-two seed at time \(b/2\) on \(b^3\). Its cutoff limsup tends to zero as the physical side \(ba_j\) increases dyadically. Proposition B3 with \(p=q=1\), time \(b/2\), enlarges the spatial cube to \(n^3\) at a finite multiplier \((2n/b)^3\) on the log trace. Monotonicity in time finishes since \(\lfloor n/K\rfloor\ge b/2\). With this neutral input, II would have periodic trace near eight at \(n/2\), contradicted by the same propagated periodic seed. The limiting transverse nonzero frequency is \(7/8\) as the physical side increases, by row 1157 (24), or by I in (9) with arbitrarily small tolerances. The neutral test at the fixed \(K\) above together with the fixed floor \(1/10\) is therefore equivalent to (W) **over the allowed sizes**. The neutral test alone, over such sizes, is equivalent to the corresponding uniform Pfaffian seed. For the converse use the same enlargement with the positive crossing-symmetric Pfaffian transfer of Theorem S-w and the inequality \(s\le S_\kappa\). The latter equivalence is for the finite-volume seed. The separate continuum assumptions of its local consumer still apply. [Shape comparison B3](gap-seed-shape.md) · [Theorem S-w](gap-flux-exercise.md)

## A one-period test with order-one margins

**PROVED.** Fix \(0<\delta<1/4\). There is a finite integer \(K=K(\delta)\) for which the following implication holds on the physical grid. On one periodic cube of fixed physical side use an even period \(u=2\lfloor n/(2K)\rfloor\). In the mixture of the eight temporal twists with zero static magnetic twist let \(\theta_0\) be the probability of the trivial temporal seam. Let \(A_+\) be the rectangle affinity of the two centre-orbit slices \(u/2\) apart in this mixture. If eventually
\[
                   A_+\ge\tfrac12+\delta,\qquad A_+-\theta_0\ge\delta,     \tag{11}
\]
then (W) holds. The same implication holds with strict limiting margins for the raw adjoint collar affinity and decoded zero frequency of row 1157. Conversely (W) supplies (11) on some sufficiently large fixed dyadic size for each such \(K,\delta\). The short period remains a fixed physical fraction of the spatial side. In particular the measurement no longer needs precision of order \(1/1651\) near a product law.

**PROVED.** Write \(D=X_{0,0}(u)\), \(Z=\operatorname{Tr}U^u\). Orbit averaging the two positive half-period kernels gives density \(q_{u/2}^2/D\) on the orbits relative to \(\pi\otimes\pi\). Its square-root kernel is the positive neutral half transfer divided by \(\sqrt D\). Integrating the four factors around a rectangle gives \(A_+=X_{0,0}(2u)/D^2\le1/D\). Fourier inversion gives \(Z=8\theta_0D\). Thus (11) gives
\[
             s(u)\le(\tfrac12+\delta)^{-1}-1<1,\qquad
             Z\le8\theta_0/A_+\le8(1-\delta).                           \tag{12}
\]
Choose the tolerance in the finite-aspect theorem after (10) below both \(\delta/2\) and \(1/(8\cdot5041)\), and choose \(K\) with its \(s_0\) equal to the upper bound in (12), using \(J=[1/2,1]\). Alternative II would give \(\operatorname{Tr}U^{n/2}\ge8-\epsilon\), while positivity of the spectrum and \(u\le n/2\) give \(\operatorname{Tr}U^{n/2}\le Z\). This contradiction selects I. The seven charged weights and the neutral excited weight then give an ordinary seed. Equivalently one may use any uniform bounds \(D\le2-\alpha,\ Z\le8-\alpha\) at that one short period with \(\alpha>0\), choosing \(K\) afterward.

**PROVED, using the collar recovery of rows 1155 and 1157.** At fixed \(K\) the temporal-twist collar measurement obeys \(A_{\rm obs}\le1/D+o(1)\) and \(\widehat\theta_0=\theta_0+o(1)\), just as in row 1157 (10). The proof requires space-time separation of order \(n\) with a constant allowed to depend on \(K\). At that separation the two small recovery collars fit inside the observed collars, and the strip decoder has a shortest noncontractible length of order \(n/K\). A logarithmic lower slope permits fixed lattice widths, and the growing-window version requires the windows to be \(o(n/K)\). Thus a strict margin in (11) transfers to (12) with a slightly smaller \(\delta\). Under (W) the shape enlargement used after (10) makes the full excited sums at \(u\) and \(u/2\) arbitrarily small in cutoff limsup. The lower affinity bound of row 1157 (10), using collars of width at most \(u/4\), then gives \(A_{\rm obs}\) arbitrarily close to one. Fourier inversion gives \(\theta_0=Z/(8D)\) arbitrarily close to \(1/8\). These statements also give the converse for the exact orbit slices. The temporal-twist mixture can be obtained from the all-twist ensemble by its decoded event \(m=0\), whose probability is at least \(1/8\) by (3). [Orbit recovery, (29)–(35)](gap-solve7-astra62.md) · [Raw collar bounds (5)–(11), (19)](gap-solve8-astra62.md)

## Selecting the periodic branch at fixed bare coupling

**PROVED.** Given the one-cube neutral input after (10), a flux estimate uniform in the cutoff is unnecessary if one can prove the following *pointwise in each bare coupling*. For every sufficiently large \(j\), let \(\zeta_{\beta_j}(b)\) denote the ratio for one elementary twist on \(b^4\). It suffices that
\[
           \liminf_{\substack{b\to\infty\\4\mid b}}
                        \frac{-\log\zeta_{\beta_j}(b)}{b}=0 .           \tag{13}
\]
The sizes in this limit need have no relation to \(a_j\). Condition (13) is also necessary under (W), for all sufficiently large \(j\).

**PROVED.** Choose the tolerance after (10) so that \(q_*:=5041\cdot8\epsilon<1\). In alternative II, \(S_{\rm full}(n/2)=s(n/2)+\sum_{m\ne0}X_{m,0}(n/2)\le8\epsilon\). Here “full” denotes the *all-magnetic neutral* seed of Theorem S-w. For \(2^k n\le b<2^{k+1}n\), its propagation gives \(S_{\rm full}(2^kn/2;b^3)\le q_*^{2^k}/71\). Rotate the elementary twist on \(b^4\) to a nonzero static \(m\). The denominator contains the periodic vacuum, and every electric sector in that magnetic transfer is bounded by its neutral one by (3). Time monotonicity now gives
\[
     \zeta_{\beta_j}(b)\le8X_{m,0}(b;b^3)
             \le \tfrac8{71}\exp[-b\log(1/q_*)/(2n)].                  \tag{14}
\]
This contradicts (13) already at the fixed \(j\). Consequently I holds and yields the uniform periodic seed. Conversely (W) gives, at every sufficiently fine cutoff, a periodic seed with uniform margin at some common physical size, passing to a larger size first if needed. Propagate it by the same theorem. In the temporal frame the untwisted vacuum is even under the elementary flip. Hence \(1-\zeta_\beta(b)\le2S_{\rm per}(b;b^3)\to0\) as \(b\to\infty\) at each such fixed \(\beta\). This proves (13). Together with the one-cube neutral criterion this is another equivalence for (W). It allows arbitrarily poor dependence of the magnetic screening length on bare coupling.

**PROVED (version with the variables of row 720).** Suppose (BDD-\(\Delta\)) holds with \(D_0,L_0\), and the *periodic neutral* dimensionless gap \(z_+^-(L)=\liminf_j n\,m_{+,j}(n^3)\) is unbounded on the dyadic sizes beyond every floor. Then the one-cube neutral criterion holds, so it gives the local Pfaffian seed and leaves only the branch choice (13) for (W). Indeed take a fixed power of two \(K\) at least as large as the required aspect and a dyadic \(L\ge2K L_0\). Enlarge the dyadic floor if needed to make \(n/(2K)\) integral. The count inequality behind row 720, Lemma Z, gives \(\log\operatorname{Tr}U^{n/(2K)}\le (2K)^3 D_j(n/(2K))\). Retaining only excited neutral states and then evolving a further \(n/(2K)\) steps gives
\[
                 s_j(n/K)\le
 \exp\big((2K)^3D_j(n/(2K))-n m_{+,j}(n^3)/(2K)\big).
\]
Choose one \(L\) with \(z_+^-(L)>2K[(2K)^3(D_0+1)+\log 2+1]\). The margin and the cutoff limits give \(s_j(n/K)\le1/2\) eventually. In particular under these two neutral/count assumptions the local consumer does not require row 1158’s (TUN). Condition (13) still concerns the *actual* Wilson weight. [Lemma Z and Theorem ZD-c](gap-phys-seed.md) · [All-magnetic seed propagation](gap-flux-exercise.md)

**OPEN.** Strict positivity of \(\zeta_\beta(b)\) on every fixed torus allows the exponential upper bound (14). The fixed-lattice asymptotic in row 1143 keeps \(b\) fixed while \(\beta\) grows. It gives no sublinear cost at fixed \(\beta\) as \(b\to\infty\). The cited vortex inequalities in the lane’s literature search require an input on the vortex free energy to obtain their large-scale consequence. [Fixed-lattice comparison, (6)](gap-solve-astra62.md) · [Vortex literature search](prior/gap-lit-fisher-odd.md)

## What an intermediate twist forces in the Wilson spectrum

**PROVED (a nonempty obstruction at each lattice size).** For every \(4\mid n\), \(n\ge4\), some finite coupling \(\beta_n\) has elementary twist ratio \(1/2\) on \(n^4\). At \(\beta=0\) the ratio is one. At fixed \(n\), row 1143 (6) makes it tend to zero as \(\beta\to\infty\). Both partition integrals are continuous and the denominator is positive, proving the assertion. More generally, along *any* sequence of couplings on growing even cubes with \(4\mid n\) on which this ratio stays in a closed subinterval of \((0,1)\), every \(3\le u=o(n)\) satisfies
\[
                 \liminf_{n\to\infty}X_{0,0}(u)\ge2.                    \tag{15}
\]
Otherwise a subsequence obeys (8), contradicting (9) at \(r=1\). Thus there are actual Wilson couplings where increasing \(K\) cannot verify the neutral criterion. This result locates a spectral effect of the crossover without locating those couplings on the physical trajectory.

**PROVED (more than two momentum harmonics).** Let \(F_m\) have a nonzero eigenvector in character \(q\) with periodic-vacuum-normalized eigenvalue \(b>0\). Let \(a=\|F_m\|/\lambda_0\). Diagonalize one compensated translation on that finite eigenspace, with phase \(\gamma\). If \((Mq)_i=1\), the order of \(\gamma^2\) is at least \(2^{\nu_2(n_i)}\), since \(\gamma^{n_i}=-1\). For \(1\le H\le\operatorname{ord}(\gamma^2)\) and \(u\ge3\),
\[
 X_{0,0}(u)\ \ge\
 a^u\sum_{\ell=0}^{H-1}\!\left[1-(2\ell)^2(1-(b/a)^u)\right]_+ .     \tag{16}
\]
For \(\ell=0\) the summand is one. In the magnetic vacuum Markov space normalize the complex eigenfunction \(z\) to norm one. For \(\ell\ge1\) take \(w_\ell=|z|\exp(2i\ell\arg z)\), set to zero on its zero set, and use the constant one for \(w_0\). These are neutral unit vectors with distinct translation phases \(\gamma^{2\ell}\), so they are orthogonal. The map \(z\mapsto |z|e^{id\arg z}\) is \(d\)-Lipschitz for integers \(d\ge1\), as follows by subtracting the polar coordinates and using \(|\sin(d\alpha)|\le d|\sin\alpha|\) in the angular term of the squared distance. Hence the \(u\)-step Dirichlet form of \(w_\ell\) is at most \((2\ell)^2[1-(b/a)^u]\). The Markov operator is positive, so its diagonal matrix element is also nonnegative. Sum these matrix elements, multiply by \(a^u\), and use the trace comparison (3). The ability to use distinct neutral harmonics is what the fractional-momentum phase provides.

**PROVED (bounded count and a separated neutral gap).** There is a second version of (9). Replace (8) by \(n/u\to\infty,\ X_{0,0}(u)\le C<\infty,\ 2^{\nu_2(n)}> C\) with the last integer uniformly at least \(\lfloor C\rfloor+1\), and \(n m_+(n^3)\to\infty\). Under these hypotheses (9) still holds. To prove it, take \(H=\lfloor C\rfloor+1\). If a misaligned eigenvalue has \(b^n\) bounded away from zero on a subsequence, then \(a^u,(b/a)^u\to1\), contradicting (16). Thus the top misaligned weight to power \(n\) tends to zero. The total at \(\lfloor rn\rfloor\) also tends to zero by spending \(u\) steps on the bound \(C\). In every sector only the first \(\lfloor C\rfloor\) levels can survive because (3) bounds the \(u\)-th power of the next level by \(C/(\lfloor C\rfloor+1)<1\). This gives the same finite exponential sums, with at most \(\lfloor C\rfloor\) entries in each sector.

**PROVED.** In the periodic neutral sector only the vacuum survives by the assumed gap and the same \(u\)-step count. In each periodic charged sector only its first level can survive. Indeed choose integer \(w=o(n)\) with \(w m_+\to\infty\), possible since \(n m_+\to\infty\) (one can use \(w=\lceil n/\sqrt{\min(n,nm_+)}\rceil\)). Row 1157 (1) gives \(b_{0,q,2}^{\,w}\le(3+e^{-wm_+})/4\). Its proof uses two real orthogonal eigenfunctions combined as \(z=f+ig\). For that choice the neutral functions \(|z|,z^2/|z|\) have total variance at least two and total Dirichlet form at most four times the sum for \(f,g\). Thus \(b_{0,q,2}^{\,n}\to0\). At the symmetric point the nonnegative crossed coefficients still have zero derivatives for \(Mq\ne0\). In (10) the magnetic side is now a sum over all the finitely many surviving aligned and neutral levels. Every term \(a\log a\) still has the same sign. Each positive limiting weight is one, their sum is \(1-b\), and the magnetic vacuum dominates every level. This proves (9) under the weaker count and the separate neutral gap. In particular at an intermediate elementary twist, a bounded earlier neutral count with this divisibility forces \(n m_+\) to stay bounded, since an unbounded subsequence would give the contradiction just proved. [Two-eigenfunction comparison, (1)](gap-solve8-astra62.md)

## An explicit aspect for the one-cube test

**PROVED.** One may take \(K=512\) in the \(s_0=1/2\) one-cube test with transverse nonzero-frequency floor \(1/10\). One sufficient lattice range is \(4\mid n,\ n\ge2^{70}\). Suppose \(s(u)\le1/2\) for an integer \(3\le u\le n/512\). On \(Q_{n/2}\) either \(S_{\rm per}<2^{-19}\), or \(S_{\rm full}<2^{-18}\) and the nonzero transverse probability is below \(1/1000\). In both cases \(S_\kappa<2^{-18}\). These conservative numbers come from the following difference estimate at the symmetric point.

**PROVED.** For each eigenvalue normalized by the periodic vacuum put \(x=(\lambda/\lambda_0)^n\), \(0\le x\le1\). In the original time frame extend the sector traces to \(s\in[1/2,3/2]\) as sums of \(x^s\), writing \(I(s,B)\) for their signed sum. This notation in the present section refers to the *finite-cutoff* interpolation. The absolute second derivative of each sector trace is at most \(96\), since the sum of \(x^{u/n}\) is at most \(3/2\), and \(\sup_{z\ge0}z^2e^{-z/4}\le64\), with \(z=-\log x\). This domination also justifies differentiation on a neighbourhood of the interval, or first on its interior and then by continuity at its endpoints using the actual margin \(1/2-u/n>1/4\). Thus \(|I''|\le768\) and the same bound holds for every crossed coefficient \(H=(1/8)\sum_e(-1)^{q\cdot e}I\). At \(s=1\), a misaligned coefficient has \(0\le H(1)\le h=(3/2)(3/4)^{511}<2^{-169}\), by (4) on the identical cube in that frame. Here \((3/4)^3<1/2\). Set \(r=\lceil n2^{-70}\rceil/n\). Both \(1\pm r\) correspond to integer periods, so \(H(1\pm r)\ge0\). Taylor’s inequality gives
\[
     |H'(1)|\le h/r+384r<2^{-59},\qquad 2^{-70}\le r\le2^{-69}.
\]
The nonnegativity here requires no evenness of the two neighbouring periods. The single basis additions in (5) now show that two rank-two raw values at \(1\) differ by at most \(160h\) and their derivatives by less than \(2^{-51}\).

**PROVED.** At \(s=1\) write \(U_N=\sum(-x\log x)\) for periodic neutral excited levels, \(U_C\) for the average of this sum over the seven periodic charged characters, and \(U_M\) for the sum over all levels of one fixed nonzero static magnetic transfer. Since \(-x\log x\le\sqrt x\), (4) yields \(U_N\le(3/2)(3/4)^{255}<2^{-84}\). The derivative of the mean of the seven nonzero temporal twist integrals is \(-U_N+U_C\), while the derivative of the purely magnetic integral is \(-U_M\). The derivative comparison gives \(U_C+U_M<2^{-50}\) for each \(m\ne0\). Thus each periodic charged or nonzero magnetic level has \(-x\log x<2^{-47}\). As \(x(1-x)\le-x\log x\), every such \(x\) is at most \(2^{-46}\) or at least \(1-2^{-46}\). Fourier inversion and the \(160h\) value comparison bound the difference between any two periodic charged traces at \(s=1\) by \(160h\). For two distinct nonzero characters their signs differ on four seams, two with each sign in the difference. Subtract the common reference value there and use the factor \(1/8\) in Fourier inversion. Removing their higher levels by (4) brings their top weights within \(162h\). So all seven top weights take the same side.

**PROVED.** If they are small, taking square roots and adding the \(n/2\) tails from (4) gives \(S_{\rm per}(n/2)<7\cdot2^{-23}+8\cdot2^{-84}<2^{-19}\). At \(s=1\) a purely magnetic trace differs by at most \(160h\) from \(1+s(n)-\frac17\sum_{q\ne0}X_{0,q}(n)\), so it lies between \(1-2^{-44}\) and \(1+2^{-44}\). The misaligned sectors and every tail are at most \(h\) each in (4). The two possible top weights in the neutral and aligned sectors cannot both be small or both large. The larger is the vacuum. The seven aligned nontrivial weights at \(n/2\) and the periodic neutral tail therefore also give \(S_\kappa(n/2)<2^{-19}\).

**PROVED.** If the seven periodic top weights are large, every nonzero purely magnetic trace at \(s=1\) is at most \(2^{-46}+161h<2^{-45}\) by the same comparison. The corresponding neutral magnetic trace at \(n/2\) is at most \(2^{-22}+2^{-84}\), by taking the square root of its top weight and bounding its tail. Thus \(S_\kappa\le S_{\rm full}<2^{-18}\). With nonzero \(m\), a twisted integral at \(n/2\) in periodic vacuum units is at most eight times this single neutral magnetic bound by (3), hence below \(2^{-18}\). With \(m=0\) and nonzero temporal seam the eight characters cancel on constants, and each of the eight sector weights differs from one by at most \(2^{-46}+2^{-84}\). Its integral too is below \(2^{-18}\). Dividing by the all-twist normalization, which contains at least the periodic vacuum, bounds the transverse nonzero probability by \(56\cdot2^{-18}<1/1000\). This proves the stated finite test entirely by hand.

## Local plaquette trial states in the actual periodic neutral sector

**PROVED.** There are absolute \(c,C>0\) such that on periodic spatial cubes with \(4\mid n\), \(n\) sufficiently large, and \(\beta\ge1\), at least \(c n^3\) *excited neutral* eigenvalues of \(U\), counting multiplicity, are at least \(1/[C(1+\beta)^2]\). In particular
\[
            s(u)\ \ge\ c n^3 [C(1+\beta)^2]^{-u}.                       \tag{17}
\]
This estimates low absolute lattice energies of an extensive family. The short-time gas law counts many more states, predominantly at much higher total energy. The soft-route note on PR 10114 proved one plaquette matrix element with an \(\exp(-68\beta)\) lower bound. The local inverse-convolution argument below uses its magnetic-sandwich setup. Row 1147, §11, counts products of plaquette trial states after removing single-boundary couplings. Equations (17)–(20) keep every Wilson coupling and control the trial span in the interacting vacuum. For the one-link multipliers I use GL3–GL4 of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Earlier plaquette-product construction](gap-solve3-astra62.md) · [Soft-route witness, §2](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L169) · [GL3–GL4](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2243)

**PROVED (the spatial Gram matrix).** Choose \(M\ge c n^3\) disjoint \(12\)-plaquettes separated by at least three lattice spacings, and choose one link on each. A grid of stride four suffices. On a finite space-time cylinder with periodic time, condition on all links except these chosen spatial links on one time slice. Their laws are independent, and each quaternion \(v\in S^3\) has density proportional to \(\exp(k\cdot v)\) with \(|k|\le6\beta\). The normalized plaquette trace \(W_p\) is \(a\cdot v\) for a fixed exterior unit vector \(a\). Uniformly over \(a,k\),
\[
                    \operatorname{Var}(a\cdot v)\ge c(1+|k|)^{-2}.
\]
Indeed \(t=v\cdot k/|k|\) has density proportional to \(e^{|k|t}\sqrt{1-t^2}\), and, conditional on \(t\), the orthogonal direction is uniform on \(S^2\). For \(|k|\ge8\), the variable \(x=|k|(1-t)\) has density proportional to \(e^{-x}\sqrt{x(2-x/|k|)}\) on \([0,2|k|]\). The normalizer is bounded above by \(\int_0^\infty e^{-x}\sqrt{2x}\,dx\), and each of \([1,2]\), \([3,4]\) has positive mass bounded below. Thus the longitudinal variance is at least \(c/|k|^2\) and the transverse variance in any unit direction is \(\mathbb E(1-t^2)/3\ge c/|k|\), with zero cross covariance. Compactness and strict positivity give the remaining range. Total variance and then the long-cylinder limit give
\[
      \operatorname{Var}_\pi\!\left(\sum_p t_p W_p\right)
                     \ge c(1+\beta)^{-2}\sum_p t_p^2 .
\]
For the limit the compact positive finite-volume transfer has simple top eigenvalue, so its powers after normalization converge in trace norm to the vacuum projector. This proves the bound for the true vacuum, including for signed coefficients.

**PROVED (a local inverse moment).** In the magnetic sandwich write \(F=D C D\) on the gauge-invariant space with normalized electric convolution \(C=\bigotimes_e C_e\), suppressing its common scalar, and \(h=D\psi\ge0\). With \(\lambda=\|F\|=\langle h,Ch\rangle\), the vacuum equation gives \(D^{-1}\psi=Ch/\lambda\). For \(f=W_p-\pi(W_p)\),
\[
        \langle f\psi,U^{-1} f\psi\rangle
                =\lambda^{-1}\|C^{-1/2}f C h\|^2\le C_1                \tag{18}
\]
with an absolute \(C_1\). These are inverse *quadratic forms*. Indeed the inverse form of \(DCD\) is \(\|C^{-1/2}D^{-1}v\|^2\) on its form domain, by the variational formula \(\sup_z(2\operatorname{Re}\langle v,z\rangle-\langle z,DCDz\rangle)\) and the substitution \(z\mapsto Dz\). The following bound establishes domain membership.

**PROVED.** On each of the four links of \(p\), a coordinate multiplier shifts the degree \(\ell=2j\) of a spherical harmonic on \(S^3\) to \(\ell\pm1\). Multiplying a homogeneous harmonic polynomial by a linear coordinate decomposes into a harmonic of degree \(\ell+1\) and the radius squared times one of degree \(\ell-1\), as is seen by taking its Laplacian and then restricting to the sphere. \(W_p\) is multilinear on the four links, with modulus at most one. The scalar subtracted in \(f\) also permits the unshifted degree. The multiplier of \(C_e\) on degree \(\ell\) is \(r_\ell=I_{\ell+1}(\beta)/I_1(\beta)\). For neighbouring allowed degrees \(\ell'\), \(r_\ell/r_{\ell'}\le C(1+\ell/\beta)\) at \(\beta\ge1\). In the downward direction use \(I_{k+1}/I_k<1\), in the upward direction use \(I_k/I_{k+1}=2(k+1)/\beta+I_{k+2}/I_{k+1}\). For the first inequality the positive Bessel series gives \(R=I_{k+1}/I_k\) starting below one at zero and \(R'=1-(2k+1)R/\beta-R^2<0\) at a first contact with one, an impossibility.

**PROVED.** Write \(v=C^{1/2}h\). In the four-link degree expansion of \(C^{-1/2} f C^{1/2}v\), every output block has at most \(3^4\) possible input blocks. The exterior degrees are preserved and their multipliers cancel. Cauchy–Schwarz on the finite input sum, orthogonality of the output projections for each fixed input, and \(\|f\|_\infty\le2\) bound its squared norm by
\[
  C_2\left\langle v,\prod_{e\in p}(1-\Delta_e/\beta^2)v\right\rangle .
\]
Here \(-\Delta_e\) has eigenvalue \(\ell(\ell+2)\), and \(1+\ell/\beta\le2[1+\ell(\ell+2)/\beta^2]\). This proof first applies to finite degree truncations. Factorial decay of the \(r_\ell\) makes the right hand form finite and gives convergence of the block sums. The Laplacians commute with \(C\). With \(z=x\cdot y\), the one-link kernel of \((1-\Delta/\beta^2)C_e\) divided by that of \(C_e\) is \(z^2+3z/\beta\), using \(\Delta z=-3z,\ |\nabla z|^2=1-z^2\). Its absolute value is at most four. Thus the four-link modified product kernel is bounded in absolute value by \(4^4\) times the original positive kernel. Integrating against \(h(x)h(y)\ge0\) bounds the form by \(4^4\lambda\). This proves (18). The calculation may use all spatial Haar functions before restriction because the insertions, the vacuum and the resulting forms for \(f\) are gauge invariant.

**PROVED.** Let \(V\) have the \(M\) columns \(f_p\psi\), all neutral and orthogonal to the vacuum. The Gram bound gives \(V^*V\ge c(1+\beta)^{-2}I\), and (18) gives \(\operatorname{Tr}(V^*U^{-1}V)\le C_1 M\). The trace of the inverse form compressed to their span is therefore at most \(C M(1+\beta)^2\), using the isometry \(V(V^*V)^{-1/2}\). On a subspace of dimension at least \(M/2\) this form is at most \(2C(1+\beta)^2\) times the norm squared, by diagonalizing the compression. The spectral min–max principle yields (17). In particular if \(\beta=O(\log n)\), \(s(u)\to\infty\) for \(u=o(\log n/\log\log n)\). This excludes these times for the new neutral test in the actual periodic Wilson theory, while \(u=n/512\) at a fixed physical size is beyond this range.

## A coupling-independent count from plaquette angle oscillations

**PROVED.** The \(\beta\) in (17) can be removed. There are absolute \(c,C>0\), independent of \(\beta\ge1\), such that for \(M\ge c n^3\) as above and every \(1\le k\le M\), at least \(\tfrac12\binom Mk\) excited neutral eigenvalues satisfy
\[
                            -\log(\lambda_i/\lambda_0)\le Ck .           \tag{19}
\]
Different values of \(k\) may count the same levels. In particular \(s(u)\ge c n^3 e^{-Cu}\) at every cutoff in this range. The proof chooses a plaquette observable that continues to fluctuate when the bare plaquette angles shrink.

**PROVED (a uniformly fluctuating bounded observable).** Let \(\theta_p=\arccos W_p\). For a sufficiently large fixed \(A\), set \(d=\lceil A\sqrt\beta\rceil\) and \(g_p=\cos(d\theta_p)\), with \(|g_p|\le1\). Its conditional variance given the exterior of the chosen link is bounded below by an absolute \(c_0>0\). To see this, let \(v\) have the tilted \(S^3\) law of the Gram proof, with tilt length \(s\le6\beta\), and write \(t=v\cdot\widehat k\) along its tilt. The density against normalized Haar is at most \(C(1+s)^{3/2}\), by the same \(x=s(1-t)\) integral used there. Integration of \(\operatorname{div}(e^{st}\nabla t)\), with \(\Delta t=-3t\), gives \(s\mathbb E|\nabla t|^2=3\mathbb E t\le3\) if \(s>0\).

**PROVED.** For \(\theta=\arccos(a\cdot v)\) in any direction \(a\), the radial Haar density is proportional to \(\sin^2\theta\). Its tilted one-dimensional density \(p(\theta)\) has
\[
       \int_0^\pi |p'(\theta)|\,d\theta
          \le 2\mathbb E|\cot\theta|+s\mathbb E|\nabla t|
          \le C\sqrt{1+s}.
\]
For the first inequality differentiate under the integral over \(S^2\) at fixed polar angle, using unit radial speed. For the second, off the two caps \(\sin\theta<(1+s)^{-1/2}\) the inverse sine is at most \(\sqrt{1+s}\). Inside the caps use the Haar density bound times the integral of \(\sin\theta\) there, which is \(O((1+s)^{-1})\). For bounded \(s\) the density bound alone suffices. Cauchy–Schwarz handles the gradient term. Integration by parts against \(\cos(\ell\theta)\) therefore gives \(|\mathbb E\cos(\ell\theta)|\le C\sqrt{1+s}/\ell\). The boundary term vanishes for integer \(\ell\). Choose \(A\) so that this is at most \(1/8\) for \(\ell=d,2d\) and all \(s\le6\beta\). The identity \(\cos^2(d\theta)=[1+\cos(2d\theta)]/2\) gives \(c_0=1/4\) as a permissible lower bound.

**PROVED (inverse moment for bounded multipliers at this degree).** Let \(f\) be bounded by two and have polynomial degree at most \(d\) in the quaternion coordinates on each of \(b\) links, independent of the other links. Take \(d=\lceil A\sqrt\beta\rceil\) with \(A\) now fixed. For a gauge-invariant \(f\) the inverse form in (18) satisfies
\[
                       \langle f\psi,U^{-1} f\psi\rangle\le C_A^{\,b}
                       \qquad(b\ge1).                                   \tag{20}
\]
Group each affected link’s harmonic degrees into bands \([jd,(j+1)d-1]\), \(j\ge0\). Multiplication changes single-link degree by at most \(d\), by iterating the coordinate decomposition in (18), so each output band meets at most three possible input bands per link. For an input band \(j\), put \(l=jd\). Between any input degree in that band and any degree in an allowed output band, the worst ratio of the electric multipliers \(r_{\rm in}/r_{\rm out}\) is at most
\[
             \exp[C_A+C_A l/\sqrt\beta].
\]
Indeed the indices differ by at most \(3d\), and each successive upward ratio is at most \(1+2(l+3d+2)/\beta\) by the Bessel recurrence. Downward ratios are at most one. Multiplying the bounds and using \(\log(1+x)\le x\), \(d\le(A+1)\sqrt\beta\), proves the displayed estimate also for the first band.

**PROVED.** For clarity, on an input band vector bound \(C^{1/2}\) by the largest square root multiplier in it, and on its allowed outputs bound \(C^{-1/2}\) by the reciprocal of the smallest square root multiplier there. Orthogonality of the output projections and \(\|f\|_\infty\le2\) bound the sum of the squared output norms for that input. Cauchy–Schwarz over the at most \(3^b\) input bands for each output then bounds \(\|C^{-1/2}fC^{1/2}v\|^2\), for \(v=C^{1/2}h\), by
\[
 C_A^b\left\langle h,C\prod_{e} \exp(C_A \ell_e/\sqrt\beta)\,h\right\rangle .
\]
The product is over the \(b\) affected links and \(\ell_e\) is the harmonic degree operator. The outside multipliers cancel in the conjugation.

**PROVED (positive-kernel estimate for that last form).** In a single Wilson link kernel \(c_\beta(g)\propto\exp(\beta\,\operatorname{tr}(g)/2)\), replace \(g\) by \(g V H_y V^{-1}\), average over Haar \(V\), and set \(H_y=\operatorname{diag}(e^y,e^{-y})\). The absolute value of the resulting kernel is at most \(c_\beta(g)\exp[\beta(\cosh y-1)]\). For \(g\in SU(2)\) the real part of the half trace after multiplication is \((\operatorname{tr}g/2)\cosh y\), as follows from the quaternion or Pauli representation. On degree \(\ell\) the resulting multiplier is \(r_\ell\,m_\ell(y)\), where
\[
                 m_\ell(y)=\frac{1}{\ell+1}\sum_{j=0}^{\ell}
                                         e^{(\ell-2j)y}
                              \ge\tfrac14 e^{\ell y/2}\quad (y\ge0).
\]
For imaginary \(y\) the multiplier formula is Schur averaging of the spin-\(\ell/2\) representation of an \(SU(2)\) matrix. Both sides of the matrix coefficient identity extend holomorphically to \(y\in\mathbb C\) by integration over compact real groups, so it holds at real \(y\). The lower bound keeps the terms \(j\le\ell/4\). Choose \(y=2C_A/\sqrt\beta\). The quantity \(\beta(\cosh y-1)\) is bounded in terms of \(A\) for \(\beta\ge1\), by the power series of \(\cosh\). The product of these \(b\) positive multipliers dominates the required spectral weight up to \(4^b\). The absolute kernel bound and \(h\ge0\) bound its quadratic form by a constant to power \(b\) times \(\langle h,Ch\rangle\). Finite truncations and the resulting summable degree weights justify the inverse form as in (18). This proves (20) uniformly in the volume.

**PROVED.** For every \(k\)-subset \(S\) of the chosen plaquettes let \(g_S=\prod_{p\in S}g_p\) and center it by subtracting its vacuum expectation. It is a polynomial of degree at most \(d\) on each of \(4k\) links because \(\cos(d\arccos x)\) is the Chebyshev polynomial. All these centered functions are neutral and bounded by two. Their Gram matrix in the vacuum is at least \(c_0^k I\). Indeed in the finite cylinder condition on the complement of the selected independent links, and write each factor as its conditional mean plus a centered variable. In \(\sum_{|S|=k} t_S g_S\) the terms containing \(k\) centered factors are orthogonal for distinct \(S\) and are orthogonal to every lower-degree term and to constants by conditional independence. Their variance is at least \(c_0^k\sum_S t_S^2\). Pass to the vacuum as before. Applying (20) to each centered product and the Gram/min–max argument of (18) proves (19), with constants enlarged to absorb the factor two for the median.

**PROVED (range of this obstruction).** If \(u=o(\log n)\), the bound \(s(u)\le1/2\) fails along *every* \(\beta\ge1\). More quantitatively, when \(M e^{-Cu}\) is sufficiently large, (19) gives \(\log(1+s(u))\ge c' M e^{-Cu}\) after increasing \(C\) if needed. Take \(k=\lfloor M e^{-Cu}/2\rfloor\) in (19) and use \(\binom Mk\ge(M/k)^k\), by comparing the factors \((M-i)/(k-i)\). The resulting contribution is at least \(2^{k-1}\). At a fixed physical \(u\) proportional to \(n\), this lower bound on the count gives no positive obstruction, and provides no upper bound. It extends the time range of a lower bound, independently of the short-period Gaussian error estimate.

## What the neutral slice law determines

**PROVED (obstruction with the actual Wilson vacuum).** Fix a finite periodic Wilson spatial cube at \(\beta>0\). Among strictly positive continuous reversible kernels on this **same connected gauge-configuration space**, with the Wilson vacuum \(\pi\), one can keep the entire Wilson neutral transfer fixed and make all seven charged transfers either vanish or approach a copy of the neutral transfer in spectrum. In particular the vacuum time correlations of *all* centre-invariant slice observables, at *all* integer time separations and orders, can coincide for these two cases. Their temporal twist ratios at any prescribed positive integer periods can approach opposite limits, one and zero. This concerns one time frame. The Wilson magnetic transfer and crossing across four frames impose the additional restrictions used in (9).

**PROVED.** Let \(Q=P_+P\) with strictly positive continuous kernel \(q(x,y)\) relative to \(\pi\), invariant under the group separately at each endpoint. For each spatial axis let \(H_i(x)\) be the sum of the real normalized traces of the straight winding loops parallel to that axis, one per transverse line. This is gauge invariant, changes sign under the \(i\)-th flip only, and is a nonzero real analytic function of the links (at the identity all terms are positive). Its zero set is Haar null because, with the other links fixed, one link on one line gives a nonconstant linear coordinate of its Haar quaternion plus a constant from the other lines. Hence the zero set is also \(\pi\)-null. Put \(h_i=\tanh(M H_i)\), \(h_S=\prod_{i\in S}h_i\), and for \(0\le c<1\) set
\[
 k_{c,M}(x,y)=q(x,y)\prod_{i=1}^3(1+c\,h_i(x)h_i(y)).
                                                                    \tag{21}
\]
This is strictly positive and symmetric. Its operator is \(\sum_S c^{|S|} M_{h_S} Q M_{h_S}\), where \(M_f\) denotes multiplication. Every term is positive trace class. Each term is supported on its own character \(S\), because \(Q\) averages to the neutral sector. Thus \(K_{c,M}1=1\), its vacuum is \(\pi\), and its neutral restriction is \(Q\) exactly. Products of invariant multiplication operators and powers of \(K_{c,M}\), starting and ending at the vacuum, use only this restriction. Formula (21) also preserves the spatial cubic symmetries by the choice of the three loop sums.

**PROVED.** The nonzero spectrum in character \(S\) equals that of \(c^{|S|}Q^{1/2}M_{h_S^2}Q^{1/2}\) on the neutral space, by the equality of the nonzero squared singular values on the two sides of an operator. As \(M\to\infty,\ c\uparrow1\), this converges to \(Q\) in trace norm. Its difference from \(Q\), taken in the order \(Q-c^{|S|}Q^{1/2}M_{h_S^2}Q^{1/2}\), is positive. Its trace tends to zero by integrating \(1-c^{|S|}h_S^2\) against each normalized neutral eigenfunction squared and summing with the summable eigenvalues of \(Q\). All cutoffs here are fixed during this limit. Thus even the traces of all powers in a prescribed finite set converge, and Fourier cancellation gives temporal twist ratios tending to zero for all nonidentity flips. At \(c=0\) all those ratios are exactly one. Parameters can be chosen afresh at each cutoff for any prescribed finite periods. Equation (2) likewise makes the two-slice overlap arbitrarily small for \(M\to\infty,\ c\uparrow1\) at fixed cutoff and time. This pinpoints what is missing from an inference of (13) solely from neutral vacuum dynamics. The comparison kernels have no claim to arise from a local isotropic four-dimensional Wilson action. [Earlier overlap formulation](gap-paths-fable.md) · [Earlier spectator obstruction](gap-council-synthesis.md)

## Continuation in the Wilson coupling

**PROVED (a fixed-coupling obstruction to changing branch).** Let \(\mathcal P,\mathcal M\subset[0,\infty)\) be the sets of finite bare couplings at which, at *some* shape-two lattice size, respectively \(S_{\rm per}<1/5041\) or \(S_{\rm full}<1/5041\). The side may depend arbitrarily on the coupling. Let \(\mathcal N\) consist of couplings for which, at some \(4\mid n,\ n\ge2^{70}\), the single periodic cube has \(s(\lfloor n/512\rfloor)<1/2\). Then
\[
               \mathcal N=\mathcal P\ \dot\cup\ \mathcal M,
       \qquad \mathcal P,\mathcal M\ \hbox{relatively open},
       \qquad 0\in\mathcal P .                                         \tag{22}
\]
The same set \(\mathcal N\) is obtained by admitting a Pfaffian seed at any shape-two size. Earlier method M5 and Corollary R6 identify the phase on intervals where the neutral trace and a vacuum-energy deficit are both controlled. Here the single-cube thermal test identifies the two disjoint open sets without a deficit assumption. [Earlier M5 and Corollary R6](gap-means-max.md)

**PROVED.** Finite-torus integrals are continuous in \(\beta\), as is the norm of the periodic transfer by uniform kernel convergence on the compact link space. These give continuity of each seed, including at \(\beta=0\), where the transfer is a rank-one constant kernel. The explicit one-cube result gives \(\mathcal N\subset\mathcal P\cup\mathcal M\) and also gives a Pfaffian seed on \(\mathcal N\). Conversely a strict seed in any of the three classes propagates under Theorem S-w. The argument after (10), now at *fixed* bare coupling with \(K=512\), makes the earlier periodic neutral trace arbitrarily close to one on enlarged cubes, since it is bounded above by each of the three positive sector sums. Concretely enlarge the spatial cube from \(b^3\) to \((512b)^3\) at time \(b/2\) by B3 applied to that seed's transfer sum, with a fixed multiplier on its log excess. Then increase time to \(b\). The propagated excess on \(b^3\) tends to zero, proving membership in \(\mathcal N\). The periodic seed gives an elementary twist ratio tending to one on symmetric tori as their side tends to infinity. The all-magnetic neutral seed gives decay (14) at the same coupling with its own positive exponent. Thus \(\mathcal P\cap\mathcal M\) is empty.

**PROVED.** If any finite \(\beta_1\) belongs to \(\mathcal M\), there is a *single fixed bare coupling* \(0<\beta_*<\beta_1\) with neither seed. Otherwise the connected interval between the two couplings would be the union of two disjoint, relatively open nonempty sets. At this \(\beta_*\) the conclusion (15) holds for every sequence \(4\mid n\to\infty,\ 3\le u=o(n)\). A subsequence with neutral trace bounded strictly below two would give (9), hence a periodic or all-magnetic seed at a finite size, a contradiction. In particular one cannot change the branch by sending the witnessing size to infinity while retaining such short-time neutral control at every intervening finite coupling. This is stronger than the drifting intermediate couplings obtained by the finite-torus intermediate value theorem.

**OPEN.** One alternative to estimating the vortex cost at individual target couplings is to establish \(\mathcal N\) throughout the interval from strong coupling to them. Equation (22) then selects \(\mathcal P\) throughout the interval, even if no size bound uniform in \(\beta\) is available there. Combined with the **uniform physical** neutral test at the target couplings it gives (W), by ruling out the second alternative of the explicit test. Openness alone supplies no such continuation. A fixed coupling satisfying the quantitative obstruction just proved would interrupt it.

## Testing the possible slow charge with all straight winding lines

**PROVED (conditional law of the complete family).** Row 1145, equations (1)–(4), treats separated coarse edges and windings through a base point. Its equations (16)–(17) treat all temporal lines in one direction by a representation-dependent coloring. Here one fixed set of links treats **all coordinate directions and every parallel line at once**, including neighboring lines, conditionally on the other links. Consider \(n^4\) or \(Q_{n/2}\), \(4\mid n\), and any of the 64 Wilson twists. Let \(Y\) consist of one full fundamental transport on each straight coordinate circuit, with fixed base points and positive orientation. There are \(N\le4n^3\) such circuits. Put \(p=n\) or \(p=n/2\), respectively, \(m=\lfloor p/8\rfloor\), \(B_\beta=1+6\beta\). For sufficiently large \(p\) there is a fixed link exterior \(\mathcal E\) for which
\[
 \left\|\frac{d{\cal L}(Y\mid\mathcal E)}{d{\rm Haar}^{N}}-1\right\|_\infty
 \ \le\ (1+\eta(m/B_\beta))^N-1,\qquad
 \eta(x)=\sum_{d\ge2}d^2e^{-(d-1)x}.                                  \tag{23}
\]
In particular the error tends to zero exponentially in \(n/(1+\beta)\) up to a polynomial factor at fixed \(\beta\) or when \(\beta=O(\log n)\). This estimate holds for every exterior configuration and every twist in a fixed stack representative. [Earlier one-link, coarse-board and temporal-line estimates](gap-solve2-astra62.md)

**PROVED.** On \(\mathbb Z/p\) partition the even residues into four disjoint sets \(A_\mu\) with sizes differing by at most one. Select the positive \(\mu\)-link at \(x\) if \(\sum_{\nu=1}^4 x_\nu\bmod p\in A_\mu\). The rule is periodic in all four coordinates. On a plaquette the two lower links start at residue \(s\) and the two upper links at \(s+1\). Only one residue is even, and at that residue only one direction can be selected. Thus no face uses two selected links. With all the unselected links fixed, the selected quaternions are independent, each with a translated central one-link law of tilt length at most \(6\beta\), including with signed plaquettes. Every straight circuit contains at least \(m\) selected links, and no selected link occurs in two circuits. In each representation of dimension \(d\), row 1145 (1) bounds the multiplier norm from the selected links by \(e^{-(d-1)m/B_\beta}\). Fourier inversion on each line gives the one-line density error \(\eta\), and conditional independence gives the product bound (23). If \(\eta\ge1\) the upper bound and nonnegativity suffice. For \(\eta<1\) use both \((1-\eta)^N\) and \((1+\eta)^N\). Since \(\eta(x)\le C e^{-x}\) for \(x\ge1\), the stated regimes follow.

**PROVED (two consequences for the wall).** The restrictions of any two twisted laws to this entire family of windings have TV distance at most the right side of (23). Thus even an arbitrary bounded nonlinear decoder on all of \(Y\) loses the twist information on the physical grid with \(\beta=O(\log n)\). For the Wilson vacuum transfer on \(n^3\) there is also a bound on the overlap with any charged eigenfunction \(h\) of eigenvalue \(b>0,\ \|h\|_{L^2(\pi)}=1\). Use the same construction on a single slice, partitioning its even residues among the three spatial directions, now with \(m'=\lfloor n/6\rfloor,\ N'=3n^2\). Let \(\delta=(1+\eta(m'/B_\beta))^{N'}-1<1\), and let \(Y_0\) be all its straight windings. Then
\[
                     b\,\|\mathbb E_\pi(h\mid Y_0)\|_2
                             \le \delta/\sqrt{1-\delta}.                \tag{24}
\]
For a character-matched function \(f(Y_0)\) the product-Haar mean is zero by multiplying all the windings in a direction with odd character by \(-1\). Hence its conditional mean given the exterior is bounded by \(\delta\|f\|_{L^2({\rm Haar})}\). The next slice, including \(h(X_1)\), is known to that exterior. On a finite periodic cylinder apply this bound and then pass to the vacuum cylinder at fixed spatial size. The one-slice density is bounded below by \(1-\delta\), and \(\mathbb E_\pi |h|\le1\). This gives \(b|\langle f,h\rangle_\pi|\le\delta\|f\|_{L^2(\pi)}/\sqrt{1-\delta}\). Approximation gives this for square-integrable \(f\). For the supremum defining the conditional-expectation norm one may first project to the character of \(h\), as the winding sigma field is flip invariant. This proves (24). In particular the straight-loop sign used in (21) cannot carry a slow charged eigenvector of the actual Wilson transfer in this regime. The full-field recovery of transverse classes in row 1157 uses local adjoint plaquette data that (23) does not retain.

## Cost of a randomized trial law for the elementary twist

**PROVED, using the specified-face estimate of row 1157.** Work on \(b^4\), put \(M=b^2\), and take sufficiently large bare \(\beta\). Let \(U\sim\mu_0\), and let \(A\) specify arbitrary endpoint rotations of every link, chosen after observing \(U\) with arbitrary extra randomness. The parameter may be continuous. Put \(Y=\Phi_A U,\ \nu={\cal L}(Y)\), and \(\widetilde\mu_B=\zeta_\beta(b)\mu_B\) for a fixed elementary twist \(B\). Write \(I_{\rm in}=I(A;U),\ I_{\rm out}=I(A;Y)\) for mutual information in nats. For absolute \(c_1,c_2,C>0,\ c_1M>C,\ c_2\beta M>C\),
\[
 D(\nu\|\widetilde\mu_B)
 \ \ge\ (c_2\beta M-C)
       \left[1-\frac{I_{\rm in}+\log 2}{c_1 M-C}\right]_+
                      -\log 2-I_{\rm out}.                             \tag{25}
\]
The entropy here is \(\int\log(d\nu/d\widetilde\mu_B)\,d\nu\) with value \(+\infty\) if absolute continuity fails. In particular, if \(I_{\rm in}=o(b^2)\) and \(I_{\rm out}=o(\beta b^2)\), every such trial has variational cost at least \(c\beta b^2\) for large \(b\). This includes adaptive countably many choices of Shannon entropy \(o(b^2)\). It also applies to continuous families with finite mutual informations, without a covering-number assumption. The actual optimum over all trial laws is \(-\log\zeta_\beta(b)\), attained at \(\mu_B\). [Specified-face estimates preceding (29)](gap-solve8-astra62.md)

**PROVED.** For each prescribed \(a\), take one offending face in each parallel plane as in row 1157 (28), breaking ties by a fixed ordering. Let \(E_a\) be the event of the required positive fraction of expensive faces in this list. The proof of (29) gives \(\mu_0\{\Phi_a U\notin E_a\}\le C'e^{-c_1M}\) and \(\widetilde\mu_B(E_a)\le C'e^{-c_2\beta M}\), uniformly in \(a\). The selection and event are measurable because the lattice is finite. For probability \(P\) and reference \(Q\) of mass at most one, restriction of entropy to the binary partition \(E,E^c\) gives \(D(P\|Q)\ge P(E)\log[1/Q(E)]-\log2\). Compare the actual joint law of \((A,U)\) with \({\cal L}(A)\otimes\mu_0\) on the failure event. Its actual probability is at most \((I_{\rm in}+\log2)/(c_1M-C)\). Next compare the actual joint law of \((A,Y)\) with \({\cal L}(A)\otimes\widetilde\mu_B\) on the success event. Its reference mass is at most \(C'e^{-c_2\beta M}\). The chain rule gives the entropy of this comparison as \(I_{\rm out}+D(\nu\|\widetilde\mu_B)\), proving (25) for finite informations (with the vacuous bound when \(I_{\rm out}=\infty\)). Thus allowing arbitrary random rotations only helps this variational route if enough information is taken from the input or retained about the chosen rotation in the output. The bound leaves open fully field-dependent transformations with that information.

## Range of the neutral counting argument

**PROVED (sharp limitation of the counting input).** The complete family of lower bounds (19), even with the binomial coefficient in place of half of it and every energy known on those states, is consistent with either outcome of the physical neutral test. On \(M\asymp n^3\) independent equiprobable signs take the tensor power of the strictly positive reversible two-state kernel with diagonal \((1+e^{-C})/2\) and off-diagonal \((1-e^{-C})/2\). The products of \(k\) distinct signs form \(\binom Mk\) orthogonal eigenvectors of energy \(Ck\). At \(u=\lfloor n/512\rfloor\) its neutral excited trace is \((1+e^{-Cu})^M-1\to0\), by \(1+x\le e^x\). Add one independent neutral sign with eigenvalue \(e^{-1/n^2}\). The original count still holds in every degree, but the excited trace at the same \(u\) now tends to one. The new level can have arbitrarily small energy although the local counted family has a uniform lower energy scale per excited sign. This comparison gives a precise obstruction to using the plaquette lower counts to bound the missing Wilson upper trace or to disprove that bound at physical time. Its abstract transfers serve only to test that inference. The centre-spectator principle itself is prior council work. [Council synthesis](gap-council-synthesis.md)

## The local seed from neutral traces at the ordinary shape

**PROVED.** The earlier time in the one-cube test can also be eliminated from the *input* if neutral information is available at two spatial sizes. Let \(K=512,\ n=Kb\), with \(b\) even, \(b/2\ge3\). Write \(m_+(n)\) for the first excited neutral energy on \(n^3\) and \(s(v;n)\) for its excited neutral sum. At every bare coupling,
\[
\begin{split}
 s(b;n)&\le
  [\,8(1+s(b/2;b))\,]^{(2K)^3}\exp[-n m_+(n)/(2K)]\\
 &\le [\,8(1+s(b/2;b))\,]^{(2K)^3}\,s(n/2;n)^{1/K}.                 \tag{26}
\end{split}
\]
Indeed (3) bounds the *entire* periodic trace on \(b^3\) at time \(b/2\) by eight times its neutral trace. Apply Proposition B3 with \(p=q=1\), initial spatial side \(b\) and time \(b/2\), to the ordinary log trace to enlarge \(b^3\) to \(n^3\). Its multiplier is \((2K)^3\). Evolving just the excited neutral part for the remaining \(b/2\) costs \(\exp[-(b/2)m_+(n)]\). Finally \(e^{-n m_+(n)/2}\le s(n/2;n)\). This proves both inequalities. They use neither an infinite-volume free-energy subtraction nor shape comparison for the neutral sector in isolation. [Proposition B3](gap-seed-shape.md)

**PROVED (equivalence over physical sizes).** Along a dyadic family of allowed physical sides beyond a floor, define
\[
 S^+_{\rm ev}(L)=\limsup_j s_j(n/2;n),\qquad
 z^-_+(L)=\liminf_j n\,m_{+,j}(n),\qquad n=L/a_j .
\]
Existence of a cutoff-uniform Pfaffian seed with strict margin at a fixed admissible side is equivalent, allowing dyadic enlargement from that side or a common grid floor, to each neutral condition below.

- **PROVED.** \(S^+_{\rm ev}(L)\) is bounded at all sufficiently large dyadic \(L\), and \(z^-_+(L)\) is unbounded beyond every floor.
- **PROVED.** \(S^+_{\rm ev}(L)\) is bounded at all sufficiently large dyadic \(L\), and its lower limit on these sizes is zero.
- **PROVED.** \(S^+_{\rm ev}(L)\to0\) on increasing dyadic sizes.

**PROVED.** For either of the first two conditions first bound \(S^+_{\rm ev}(L/K)\) by a common constant beyond its floor. Then choose one sufficiently large fixed \(L\) with, respectively, large \(z^-_+(L)\) or small \(S^+_{\rm ev}(L)\) to put the corresponding right side of (26) strictly below \(1/2\) in cutoff limsup. The integers required in (26) are available after \(K\)-fold dyadic enlargement on the lane grid. The explicit one-cube theorem gives the uniform Pfaffian seed, without any magnetic observable. For the converse Theorem S-w propagates a uniform Pfaffian seed to a vanishing excited sum on increasing dyadic physical sides, and to a uniform positive lower bound on the neutral mass in physical units there. Thus \(S^+_{\rm ev}(L)\to0\) and \(z^-_+(L)\) grows at least linearly in \(L\) past the seed. The third condition implies the second directly. These equivalences are for the local finite-volume seed. Adding (13) at the cutoff couplings gives the periodic wall. This replaces the full Casimir bound in the version after (14) by a bounded *neutral* heat trace measured only at aspect two. The bound and the growth or vanishing condition remain physical inputs.

## Finite sets of neutral moment tests

**PROVED (what can remain invisible on the same slice).** Fix the true Wilson vacuum measure at a finite spatial size. Given any finite family of continuous real neutral slice observables, any finite time \(T\), and any \(\epsilon>0\), there are two strictly positive continuous reversible Markov kernels on that slice with this vacuum and the following properties.

- **PROVED.** The stationary correlations of arbitrary strings of the specified observables at distinct integer times coincide, at every order and every separation. All periodic temporal twist ratios coincide and equal one.
- **PROVED.** One kernel has zero neutral excited trace. The other has a neutral eigenvalue whose \(T\)-th power exceeds \(1-\epsilon\).

**PROVED.** Let \(V\) be the span of the tests and the constant one. A neutral real scalar \(t(x)\) uniform on \([0,1]\) under \(\pi\) is obtained by applying the continuous distribution function of a plaquette trace to that trace. The distribution has no atoms, since a Haar quaternion on any one of its links gives a linear coordinate and the vacuum is absolutely continuous. For \(M\) large and fixed, \(w_d(x)=\tanh(M\sin(2\pi d\,t(x)))\) has mean zero and squared norm arbitrarily close to one, independent of integer \(d\ge1\). It converges weakly to zero as \(d\to\infty\). To see this condition on \(t\), approximate the conditional expectation of a test function in \(L^1[0,1]\) by interval step functions, and integrate complete periods on each interval. With \(\Pi_V\) the orthogonal projection, finite dimensionality and continuity of a basis give \(\|\Pi_Vw_d\|_\infty\to0\). Thus
\[
       k=(w_d-\Pi_Vw_d)/(1+\|\Pi_Vw_d\|_\infty)
\]
is continuous, neutral, perpendicular to all of \(V\), bounded by one, and can have squared norm arbitrarily close to one. Take kernels with densities \(1\) and \(1+c\,k(x)k(y)\) relative to \(\pi\), \(0<c<1\). They are strictly positive Markov kernels with nonnegative spectrum. Their positive-time powers send every \(f\in V\) to its constant mean. Integrating successively from the last time proves the correlation identity, including for repeated occurrences at different times. Both kernels annihilate every charged function. The sole excited eigenvalue of the second is \(c\|k\|_2^2\), whose \(T\)-th power can be as close to one as prescribed. The tests and the time can be chosen anew at each cutoff.

**GUIDE.** Row 1155 (16)–(18) treats finite scalar spectral comparisons, and the council identifies the neutral-spectator problem. Here the underlying Wilson slice measure and every moment string in the specified tests are fixed. A bound on the actual neutral heat trace must control the full space of states, either directly or through a completeness estimate for its probes. The counterexamples above concern inferences from the stated data. The Wilson action across time is the unexploited input in those counterexamples. [Earlier finite spectral comparisons](gap-solve7-astra62.md) · [Council synthesis](gap-council-synthesis.md)

## Remaining Wilson estimates

**OPEN.** On the cutoff trajectory, no estimate here gives \(s_j(\lfloor n/512\rfloor;n)\le1/2\) uniformly on one admissible physical cube. Equation (26) specifies exactly how a neutral bound and decay at the ordinary shape would suffice. The local plaquette states in (19) exclude times \(u=o(\log n)\) and sufficiently small constant multiples of \(\log n\). The sign-product comparison shows why their count is compatible with both outcomes at physical time, and the finite-moment construction shows where a probe-completeness argument would be needed. The ultraviolet partition-function estimates leave a volume-dependent remainder at one period, as detailed in row 720, §1.1. [Scope of the ultraviolet bounds](gap-phys-seed.md)

**OPEN.** Given the neutral input, it still takes a Wilson estimate to select the periodic branch. A nonzero transverse-class probability above \(1/10\) with strict limiting margin suffices. So does (13) separately at each sufficiently fine bare coupling, with no uniformity in its screening length. Equations (21), (23)–(25), and the fixed-coupling obstruction following (22) delimit the routes through one-frame neutral dynamics, straight winding observables, variational insertion, and continuation from strong coupling. None establishes sublinear elementary-twist cost at the required couplings. I have no further deduction of either physical estimate from the checked inputs. Both the periodic wall and the Jaffe–Witten gap remain open here.

RESULT: Row 1161. PROVED by hand under the displayed hypotheses, pending independent review. One vacuum-normalized periodic neutral trace at most \(3/2\) by time \(\lfloor n/512\rfloor\) gives a Pfaffian seed and forces one of two flux alternatives. A transverse nonzero-class probability above \(1/10\), or sublinear elementary-twist cost along an unbounded sequence of sizes at each sufficiently fine bare coupling as in (13), selects the periodic seed and gives (W). Equation (26) gives equivalent local criteria using only aspect-two neutral traces. Unconditionally for Wilson \(SU(2)\) at \(\beta\ge1\), (19) gives at least \(\tfrac12\binom Mk\) neutral excited levels of lattice energy at most \(Ck\), with \(M\ge c n^3\). OPEN. The physical neutral upper bound, the flux-branch choice, (W), and the mass gap remain unresolved.
