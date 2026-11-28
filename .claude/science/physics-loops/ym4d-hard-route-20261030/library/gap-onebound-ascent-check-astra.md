# Repo search

Row 1311, cross-provider research check by Codex (gpt-6.2-astra, max), at `a80482fd5`. The text checked is Claude Opus 5.5's row 1295. This note grants no scientific status.

The lead's November 8 digest covers earlier ultraviolet and transfer work. Row 1218 gives the closer, paper-specific locators. I checked the following passages at the fetched revisions.

| Source | Relation to the question |
|---|---|
| Main `8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md` 305–329 | Theorem ZD-c already connects a full periodic seed, a doubling defect and thermal counting on a physical size ladder. Its hypotheses differ from the rectangular window in Theorem 7.56. |
| PR 10114 `f76f6c649c`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 4–14, 106–149 | One-step nontriviality and a fixed-spacing strong-coupling result. |
| Grok's PR 10133 `89faef229f`, `MASS_GAP_CROSSOVER_REDUCTION.md` 77–86, and PR 10134 `1e70c7211a`, `mass-gap-interface.md` I1–I5 | The former leaves the crossover and source-transport bounds open. The latter distinguishes an excited sector, a gap and field identification. Neither gives the thermal window. |
| PR 10141 `a2f6a430e2`, `research/ym4d/library/fp1.md` 299–315 | A constrained classical one-scale energy estimate for a different operator. |

Row 697 supplies the earlier crossing and one-cube argument. Row 1218 compared the published criterion with the neutral trace. Row 1224, line 295, left the ascent for a later check. The references in *gap-mini-solve-p-fable.md* (197) and *gap-mini-solve-ab-opus.md* (28) compare or cite it. Row 1295 performed the first line-by-line reading. The target-specific prior file is absent. The registry and the five fetched refs yielded no other owner or cross-provider check of AU1–AU3 under the paper title, record number or target labels. [Row 1295](gap-mini-solve-au-opus.md) · [Row 1218](prior/gap-onebound-read-sol.md)

The Sussman–Alpoge index (chunks 01, 09, 29 and the obligations list) locates the scope of their results. Their outline, lines 581–599, 9568–9573 and 31860–31882, separates polynomial clustering and a classical quadratic gap from a positive physical threshold. CA-I, lines 2704–2712 and 3213–3222, explicitly leaves the mass gap unasserted. The CA-I 4.12–4.19 index concerns ultraviolet induction. Credit for these distinctions belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at `31a47c543775`.

# The conditional thermal ascent

## Plan

1. Establish the repository baseline, prior work, ownership, and source locators.
2. Read the published ascent and the lane statements side by side and fix notation.
3. Check Lemmas 7.27, 7.31, 7.33, and 7.44 by hand.
4. Check Proposition 7.45(ii), Lemma 7.51, and Proposition 7.52 by hand.
5. Check Theorem 7.56, Proposition 7.57, and Theorem F(i)–(ii) by hand.
6. Check Corollary AU1, including the parameters and quantifiers in (RR).
7. Check Corollary AU2 and Remark AU3 against the two observables and their hypotheses.
8. Reconcile the verdicts with row 1295 and record the result and any open obligations.

## Sources and normalizations

Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy are the authors of *The Yang-Mills Mass Gap from One Bound at One Scale* (A below). I checked the specified §7 passages in the 157-page `papers/4Y-MPaper.pdf` from the public v5.0.0 archive dated 12 November 2026. The archive matched the record's checksum. Page numbers below are the paper's printed pages. [Zenodo record 24147967](https://zenodo.org/records/24147967)

At one coupling let $Z(s,M)$ be the unnormalized four-torus integral, $V(s)=s_1s_2s_3$, $T_s$ the transfer on the spatial torus, $E(s)=-\log\lambda_0(s)$, and $r_k=\lambda_k/\lambda_0$ with multiplicity. Put
$$
h_s(M)=\log\mathcal Z_s(M)=\log Z(s,M)+ME(s),\qquad
D_s(M)=e^{h_s(M)}-1=\sum_{k\ge1}r_k^M .
$$
A, pp. 20–21, 39 (Lemma 7.3 and its rectangular application), supplies the transfer in each frame. Haar relabelling permutes axes. The symmetric Hilbert–Schmidt kernel is strictly positive, its maximal eigenspace is simple, and operator positivity at nonnegative coupling gives $0\le r_k<1$ off the vacuum. The latter is essential for odd powers. Thus $0\le h_s(M)\le h_s(2)<\infty$ for $M\ge2$, so $M^{-1}\log Z(s,M)\to-E(s)$ on each fixed spatial torus. These are the finite-volume inputs for the check.

For comparing the two sources I use $\beta_W$ for row 1258's coefficient of $\tfrac12\operatorname{Tr}U_p$ and $\beta_A$ for A's coefficient before the representation-dimension factor. Their actions agree at $\beta_W=4\beta_A$ for fundamental $SU(2)$ (A, p. 1, footnote 1 and (7.2) on p. 20, and row 1258, lines 63–79). Times and volumes here are in lattice units up to the explicit introduction of $a_j$ or $1/N$. The six authors' continuum hypothesis (W) and row 1161's periodic-wall condition use the same letter for different statements.

## Spectral and tube lemmas

**Lemma 7.27 — HOLDS** (A, p. 39, and row 1295, lines 89–93, 109–111, 120). In the frame perpendicular to a cut, expand $(\sum_k\lambda_k^a)(\sum_m\lambda_m^b)$. Its diagonal is $Z(a+b,\ldots)$ and every off-diagonal term is nonnegative. Axis symmetry gives the same result for a cut in any of the four directions, with both new lengths and the other sides at least three. The identical diagonal argument on the excited spectrum of the *same* normalized transfer gives $D_s(M'+M'')\le D_s(M')D_s(M'')$ for $M',M''\ge2$. Hilbert–Schmidt summability makes all these sums finite.

**Lemma 7.31 — HOLDS** (A, p. 41, and row 1295, line 121). Fix $b,c\ge3$ and write $E_\ell=E(\ell,b,c)$. Apply the cut inequality at time $M\ge3$, take $-M^{-1}\log$, then $M\to\infty$. This gives $E_{a+d}\ge E_a+E_d$. In A's Wilson normalization $Z\ge1$ by Jensen's inequality. Under product Haar each plaquette is Haar, and its mean real trace is the dimension of the representation's invariant subspace. Thus $E_\ell\le0$. For fixed $m\ge3$, write every large $\ell=qm+r$ with $3\le r\le m+2$. The finite remainder gives $\liminf E_\ell/\ell\ge E_m/m$. The supremum over $m$ also bounds the limsup, so $e=\lim E_\ell/\ell=\sup_{m\ge3}E_m/m\in[E_3/3,0]$ and $\zeta(\ell)=\ell e-E_\ell\ge0$.

1. On the identical torus, $M^{-1}h_{(b,c,M)}(\ell)=M^{-1}\log Z(\ell,b,c,M)+\ell E_M/M\to-E_\ell+\ell e$. Here the limit at fixed $\ell$ uses the transfer in the $M$ direction. This proves (i).
2. Substitution in $E_{a+d}-E_a-E_d$ gives $\zeta(a)+\zeta(d)-\zeta(a+d)$, between zero and $\zeta(a)+\zeta(d)$. Applying (i) to the two terms gives the printed upper limit in (ii).
3. Successive binary cuts in the three directions produce $1+2+4$ defects. Interior energies cancel once with each sign. Each defect costs at most two of the stated half-length deficits by (ii), giving the factor $14$ in (iii). Row 1295 uses (i)–(ii) only.

**Lemma 7.33 — HOLDS** (A, p. 42, and row 1295, line 127). The vacuum terms cancel in $\psi_s(M)=2\log Z(s,M)-\log Z(s,2M)=2h_s(M)-h_s(2M)$. Since $0\le h_s(2M)\le h_s(M)$, this puts $\psi$ between $h_s(M)$ and $2h_s(M)$. Summing the normalized identity with weights $2^{-k-1}$ at $2^kM$, $0\le k<K$, leaves $h_s(M)-2^{-K}h_s(2^KM)$. The subtracted term tends to zero. For sharpness it already suffices to take the two eigenvalues $1,r$ and put $x=r^M$. The ratio $\psi/h$ is $2-\log(1+x^2)/\log(1+x)$. As $x\uparrow1$ it tends to one. As $x\downarrow0$ the quotient of logarithms is at most $x(1+x)$ by $x/(1+x)\le\log(1+x)\le x$, so the ratio tends to two. Both limits respect a simple vacuum at every test point.

**Lemma 7.44 — HOLDS** (A, p. 51, and row 1295, line 122). For $A_m=\sum_k w_k^m$ with $w_k\ge0$, Cauchy–Schwarz gives $A_m^2\le A_{m-1}A_{m+1}$ wherever all three traces exist. Taking $w_k=\lambda_k$ gives discrete convexity of $\log Z$ in a side. Subadditivity was proved in 7.27. Taking the pointwise limit of $-M^{-1}\log Z(\ell,b,c,M)$ gives concavity of $E_\ell$ on the integer domain $\ell\ge3$. Its superadditivity follows from the cut argument in 7.31(ii). Subtracting $E_\ell$ from $\ell e$ proves convexity of $\zeta$. In 7.31(i) each rotated relative trace decreases weakly with $\ell$ since $0\le r_k\le1$, so $\zeta$ does too. Finally $w_k=r_k$ gives convexity and monotonicity of $h_s$ on $M\ge2$. This checks (i)–(iii), including the monotonicity needed for a cut.

## Exchange of directions and the cost of cuts

**Proposition 7.45(ii) — HOLDS** (A, pp. 51–52, and row 1295, line 123). An exact two-frame identity gives a shorter hand check of the long-tube argument. Write $h_\ell(\tau)=h_{(b,c,\ell)}(\tau)$. Expanding the same $\log Z(b,c,\ell,\tau)$ first in direction $\tau$, then in direction $\ell$, cancels the bulk term $-\ell\tau e$ and gives
$$
\tau\zeta(\ell)+h_\ell(\tau)=\ell\zeta(\tau)+h_\tau(\ell).
$$
For $\ell>\tau\ge3$, $h_\tau(\ell)\ge0$ and $\zeta(\ell)\le\zeta(\tau)$. Thus $h_\ell(\tau)\ge(\ell-\tau)\zeta(\tau)$, with the shorter length in the deficit. In A's proof, cutting $k\ell$ into $k$ copies bounds $(k\ell)^{-1}\log Z(b,c,k\ell,\tau)$ by $\ell^{-1}\log Z(b,c,\ell,\tau)$. Adding $\tau E_{k\ell}/(k\ell)$ and taking the limit reproduces $\ell\zeta(\tau)\le h_\ell(\tau)+\tau\zeta(\ell)$. The direct identity is also row 697's Lemma X, lines 182–184 of *gap-crux-restate.md*, with $\kappa=\zeta$. Its displayed bound has $\zeta(\ell)$ on the left. Its identity and Lemma K(d) give the stronger bound just derived.

**Lemma 7.51 — HOLDS** (A, pp. 55–56, and row 1295, lines 109–112, 124). Fix integers $T\ge3$, $P\ge2T$, $S\ge2P$, and $2T\le t_j\le S$. If a side $n=qP+r\ge2P$ with $0\le r<P$, use $q-1$ pieces of length $P$ and one of length $P+r$. A shorter side stays whole. Count pieces with multiplicity, so equal shapes in different positions count separately. Their volumes sum to $V(t)$ and all their sides are in $[2T,2P)$. Successive cuts give $Z(t,M)\le\prod_s Z(s,M)$ for $M\ge3$. The proof on p. 55 writes “for every $\tau\ge2$”. The spatial-cut clause of 7.27 as stated applies directly for $M\ge3$, which includes both $M=T$ and the entire tail used in the limit. Taking $-M^{-1}\log$ and letting $M\to\infty$ gives $\kappa=E(t)-\sum_sE(s)\ge0$. Using the product inequality at $M=T$ gives $h_t(T)\le T\kappa+\sum_s h_s(T)$.

Let $f_S=\max_{2T\le t'_j\le S}h_{t'}(T)/V(t')$. On a cut of $A$ into $a,d$ across $B\times C$, both cut lengths are at least $P$. Its defect is at most $\zeta(a)+\zeta(d)\le2\zeta(T)$ at this cross-section. By 7.45(ii) with $\ell=2T$, its cost is at most $2h_{(B,C,2T)}(T)/T\le4f_SBC$. This application of the maximum is legitimate because $B,C$ are original sides or piece lengths, all in $[2T,S]$. Write $c_j$ for the number of cuts along an original side $t_j$, and $a_i,b_k$ for the piece lengths in the first two directions. The total cut areas in the three directions are respectively $c_1t_2t_3$, $c_2(\sum_i a_i)t_3$, $c_3(\sum_i a_i)(\sum_k b_k)$. Each is at most $V(t)/P$ because $c_j\le t_j/P$. Interior energies telescope, so $\kappa\le12 f_S V(t)/P$, including the case of zero cuts.

**Proposition 7.52 — HOLDS** (A, p. 56, and row 1295, lines 89, 95–96, 125). Let $g=\max_{2T\le s_j<2P}h_s(T)/V(s)$ and choose finite $S\ge\max(2P,t_1,t_2,t_3)$. Apply 7.51 to *every* $t'$ defining $f_S$ and use $\sum_s h_s(T)\le gV(t')$. Taking the finite maximum after division by $V(t')$ gives $(1-12T/P)f_S\le g$. For $P>12T$ this bounds the chosen $h_t(T)/V(t)$, uniformly in $S$. At $P=24T$ the factor is exactly two. Taking the finite maximum avoids subtracting two infinite quantities.

## Ascent and the finite-volume conclusions

**Theorem 7.56(a)–(c) — HOLDS for $0<y_0\le1/20$. At $y_0=0$ the logarithmic gap HOLDS AFTER CORRECTION with $\delta_*=+\infty$.** A, pp. 58–59, and row 1295, lines 80–108, 126, 131–137. The six authors describe the mechanism as “positivity in the four directions propagates a datum at one scale” (p. 59).

**(a)** Write $T_i=2^iT_0$, $v_i=(96T_i)^3$, $F_i=y_i/v_i$. The hypothesis $h_s(T_0)\le\gamma V(s)$ for $2T_0\le s_j<48T_0$ bounds exactly $g(T_0,24T_0)$. Proposition 7.52 gives $h_t(T_0)\le2\gamma V(t)=F_0V(t)$ for all $t_j\ge2T_0$. Suppose the same density bound holds at $T_i$. On the next base window $4T_i\le s_j<96T_i$ one has $V(s)<v_i$. Convexity gives $e^{F_iV}-1\le(V/v_i)(e^{y_i}-1)$ for $0\le V\le v_i$ by the chord through zero. Hence
$$
 \frac{h_s(2T_i)}{V(s)}
 \le \frac{D_s(T_i)^2}{V(s)}
 \le \frac{V(s)}{v_i^2}(e^{y_i}-1)^2
 \le\frac{(e^{y_i}-1)^2}{v_i}.
$$
The first inequality is $\log(1+x)\le x$ and 7.27. At the new time 7.52 multiplies the density by two, while $v_{i+1}=8v_i$. Thus $y_{i+1}=16(e^{y_i}-1)^2$ suffices at every size in the new range.

For $0<y\le1/20$, the exponential series from its quadratic term has subsequent term ratios at most $y/3$. Consequently
$$
 (e^y-1)/y\le1+\frac{y}{2(1-y/3)}\le 1+\frac3{118}<1.0255 .
$$
Multiplication gives $16(1.0255)^2=16.826404<16.83$. This supplies exact bounds for the rounded equalities at row 1295, line 98. Therefore $y_{i+1}\le0.8415\,y_i$ and $16.83y_{i+1}\le(16.83y_i)^2$. Induction gives $16.83y_i\le u_0^{2^i}$, $u_0=16.83y_0$.

**(b)** If $2T_i\le t_j<96T_i$, then $r_1^{T_i}\le D_t(T_i)\le e^{y_i}-1\le1.0255y_i\le u_0^{2^i}$. Taking the $T_i$-th root gives $r_1\le u_0^{1/T_0}$. Choose the largest $i$ with $2T_i\le a=\min_j t_j$. Then $a<4T_i$, so $\max_j t_j<24a$ puts all sides in that window, including every cube with $a\ge2T_0$. For $x=1-0.8415=0.1585$, $-\log(1-x)\ge x+x^2/2+x^3/3>0.1585+0.0125+0.0013>0.172$.

**(c)** For $2T_i\le n<4T_i$, $F_i n^3\le y_i/24^3=y_i/13824$. The geometric-series bound $e^z-1\le z/(1-z)$ and $y_i\le1$ give $D_{n^3}(T_i)\le y_i/13823$. By time monotonicity and 7.27,
$$
 D_{n^3}(n)\le D_{n^3}(2T_i)\le
 \frac{u_0^{2^{i+1}}}{(16.83\cdot13823)^2}
 \le 1.9\cdot10^{-11}u_0^{n/(2T_0)} .
$$
Indeed $16.83\cdot13823>16.8\cdot13800>230000$, whose inverse square is below $1.9\cdot10^{-11}$, and $n/(2T_0)<2^{i+1}$. The exponent comparison uses $u_0<1$.

The printed cap also admits $y_0=0$, realized by the Wilson product-Haar law at $\beta_A=0$. Part (a) then forces $h_t(T_0)=0$ for every $t_j\ge2T_0$. Every excited eigenvalue is zero, so (b)'s eigenvalue bound and (c) still hold. Write $\delta_*=+\infty$ in that case, or state that every finite gap lower bound holds. The printed real expression $\log(1/u_0)$ requires $u_0>0$.

**Proposition 7.57 — HOLDS** (A, pp. 60–61, and row 1295, lines 52, 127, 132). Take logs of (B**) on each shape. Lemma 7.33 gives $(\mathrm B^{**})_\gamma\Rightarrow(\mathrm B^*)_\gamma$ and $(\mathrm B^*)_\gamma\Rightarrow(\mathrm B^{**})_{2\gamma}$. A bulk factor $e^{cV(s)T}$ cancels from $\psi_s(T)$. There are $46T_0$ integer choices for each ordered spatial side and two time lengths, giving the paper's $2(46T_0)^3$ evaluations before symmetry. The factor two matters in row 1295's word “equivalently”. For a transfer with any $0<r_k<1$, $h(T)>h(2T)$, hence $\psi(T)>h(T)$. The reverse implication gives the published factor, and doubling $\gamma$ at the endpoint would double $y_0$ to $1/10$.

**Theorem F(i) — HOLDS. Theorem F(ii) — HOLDS.** Both use $y_0>0$ for a real logarithm, with the same correction at zero. A, pp. 59–60, and row 1295, lines 128–129. The paper assumes (W), fixed $t_0>0$ and common $y_0\le1/20$, and, for each $p\ge p_0$, $N\ge N_0(p)$ in the family, some integer $3\le T_0(N,p)\le Nt_0$ satisfying (B*) at $\beta_{N,p}$. The conclusions are for $L_p\ge2t_0$, as holds eventually. At $n=NL_p$ we have $n\ge2T_0$. With $\Delta=t_0^{-1}\log(1/u_0)$, (c) gives
$$
 0\le\mathcal Z_{N,p}-1\le1.9\cdot10^{-11}u_0^{NL_p/(2T_0)}
 \le1.9\cdot10^{-11}e^{-\Delta L_p/2}.
$$
This bounds the inner $\limsup_N$ uniformly, then $L_p\to\infty$ gives (Z), exactly in the order on p. 28. Part (b) gives $0\le\lambda/\lambda_0\le u_0^{1/T_0}\le e^{-\Delta/N}$ for every nonvacuum eigenvalue on the spatial cube. For $y_0=0$ the excited trace and these eigenvalues vanish identically on the stated cubes. These two deductions use the finite-volume hypotheses alone. The phase and Wightman conclusion F(iii) is outside this check.

## Corollary AU1

**HOLDS for the all-shapes (RR) hypothesis at lines 148–157. The (SL) formula HOLDS AFTER CORRECTION at zero coupling.** Use integer $T_0\ge3$ and the same Wilson measure in both texts, at $\beta_A=\beta_W/4$. Fix a shape $s$ in A's window and let $K=K_{T_0}$ be its positive slab kernel with the spatial boundary half-weights. Row 1258, lines 71–79 and 344–356, defines $\eta_*$ as the supremum of the absolute logarithmic four-point difference. Hence, pointwise on the two slices,
$$
 K(x,x)K(y,y)\le e^{\eta_*}K(x,y)K(y,x).
$$
Integrating both sides in the two independent slice Haar variables gives $Z(s,T_0)^2\le e^{\eta_*}Z(s,2T_0)$. This directly verifies the part of Proposition RR(i) used here. Assuming $\eta_*\le V(s)/[40(96T_0)^3]$ for **every** $s$ in the window gives (B**) with $\gamma=1/[40(96T_0)^3]$. Lemma 7.33 gives (B*) at that same $\gamma$, hence $2\gamma(96T_0)^3=1/20$. Theorem 7.56(b) gives $r_1\le0.8415^{1/T_0}$ and gap at least $0.172/T_0$ on the stated cubes and bounded-aspect tori.

The optional TV premise invokes row 1258's WS′, lines 230–240, also checked in row 1265, *gap-ws-check-astra.md*, “Lemma WS′ and Proposition RR”. On these rectangular slabs there are $3V(s)$ top links. A unit-quaternion geodesic changing one has length at most $\pi$. Conditional on the middle slice at $\lfloor T_0/2\rfloor$, the upper slab law is independent of the bottom boundary. The change between two bottoms of the expected top-plaquette derivative is thus at most $2\pi\tau_*$, also for $T_0=3$. Summing the top-link changes after cancellation of their boundary-only terms gives $\eta_*\le6\pi\beta_W V(s)\tau_*$. The sufficient condition valid on the closed coupling domain is
$$
 240\pi\beta_W(96T_0)^3\,\tau_*(T_0,s;\beta_W)\le1 .
$$
Dividing by $\beta_W$ in line 154 is legitimate only for $\beta_W>0$. At zero coupling $K=1$, $\eta_*=\tau_*=D_s=0$, and the conclusion holds directly. Using the same numerical bare parameter in the two different actions would also require correcting the coupling conversion.

Row 1258 defines (RR) for a specified shape, thickness and tolerance. Its separate one-cutoff sufficient datum (6.1), lines 363–369, sums bounds on **four** shapes. For $N=T_0$ even the cube $(2T_0)^3$ is absent from that list when the blow-up factor is 25. The all-window premise in AU1 is additional. Lines 179–182, 219 and 227 of row 1295 should retain this qualification when referring to “the chain's datum”. The implication supplies a criterion at one coupling. Producing that bound at weak coupling remains open.

## Corollary AU2

**HOLDS on the stated compatible cutoffs. The claim of (N-phys) at the exact side $L=16384t_0$ HOLDS AFTER CORRECTION unless that side is eventually admissible.** Row 1295, lines 159–173, 219–220. Row 1161, lines 146–150 and 215, and row 1179, lines 304–309, require one fixed side with $4\mid n_j=L/a_j$ at *every* sufficiently late cutoff. The explicit $K=512$ consumer uses $n_j\ge2^{70}$, automatic eventually at a fixed admissible $L>0$ when $a_j\to0$.

Fix $K\ge2$ and a common upper bound $0<y_0\le1/20$ for the base constants. Choose $i_*$ once so that
$$
 (16.83y_0)^{2^{i_*}}\le16.83\log(3/2)(48/K)^3.
$$
Take **any** fixed admissible $L\ge K2^{i_*}t_0$. At cutoff $j$ apply (B*) at the actual coupling on that trajectory and at its own $T_0(j)$ with $a_jT_0(j)\le t_0$. Set $n=L/a_j$ and choose $i$ maximal with $K2^iT_0(j)\le n$. Then $i\ge i_*$ and $K T_i\le n<2KT_i$. The cube belongs to the all-sizes conclusion 7.56(a), because $n\ge2T_i$. Thus
$$
 h_{n^3}(T_i)\le y_i\left(\frac{n}{96T_i}\right)^3
 \le \frac{(16.83y_0)^{2^{i_*}}}{16.83}(K/48)^3
 \le\log(3/2).
$$
Set $u_j=T_i$. This proves $3\le u_j\le n/K$ and $D_{n^3}(u_j)\le1/2$. Spatial centre flips preserve the two-slice Wilson kernel and take the normalized strictly positive vacuum to another such vacuum. Simplicity fixes it under every flip. Restricting the trace to the centre-invariant subspace thus keeps the same vacuum and a subset of the excited eigenvalues with their multiplicities. It gives $s_{+,j}(u_j;n^3)\le D_{n^3}(u_j)$. All those eigenvalue ratios are in $[0,1]$, so the estimate persists at $\lfloor n/K\rfloor$. The larger cube and the choice of time are needed before this last projection.

For $K=512$, the worst-case $u_0=0.8415$ has successive squares bounded above by $0.71,0.505,0.256,0.066,0.004356$. In particular $u_0^{32}<1/200$. The series $\log(3/2)=2\sum_{k\ge0}(1/5)^{2k+1}/(2k+1)$ gives $0.4<\log(3/2)<0.406$ by summing the tail with denominators at least three. The right side of (AU2) exceeds $16(0.4)(3/32)^3=27/5120>1/200$. Thus $i_*=5$ works and $512\cdot32=16384$. For the rounded “30.0” at line 166, $0.7081<u_0^2<0.709$, and squaring the lower bound successively gives $u_0^4>0.5014$, $u_0^8>0.2514$, $u_0^{16}>0.0632$. Hence $u_0^{30}>0.0632^2/0.709>0.005633$, whereas $16.83(0.406)(3/32)^3<0.005631$. This leaves the dyadic choice intact.

The quantifier failure is at the transition from “with $n_j=L/a_j$ an integer” in lines 163–164 to “(N-phys) holds at $L$” in line 165. For example, take $a_j=1/j$, $\beta_W=0$, $T_0(j)=3$ and $t_0=\sqrt2$. The (B*) hypothesis holds for every large $j$, yet $16384\sqrt2\,j$ is never an integer. This counterexample concerns the claimed side, even for a theory with vanishing excited trace. More generally, increasing the time upper bound preserves the thermal premise on any trajectory, whereas the eventually admissible sides form a countable union over starting cutoffs of subsets of a single cutoff grid. On the lane's unbounded dyadic ladder of admissible sides choose one at or above $16384t_0$. Equivalently, enlarge the initial time **upper bound** to $t'_0=L/16384$ before stating the equality. If $16384t_0$ is already admissible, row 1295's numerical conclusion holds there exactly. No passage to a compatible subsequence proves the every-cutoff assertion.

## Remark AU3

**HOLDS AFTER CORRECTION. The factor 7.5 at lines 195–196 FAILS.** Row 1295, lines 185–206, 221 and 228. At the common time $n=T_0$ and common cube $s=(2n)^3$, Theorem S (row 697, lines 192–203) requires $D_s(n)<1/5041$, exactly $h_s(n)<\log(5042/5041)$. It propagates to dyadic cubes of side $2^{k+1}n$, with gap at least $n^{-1}\log(1/(5041D_s(n)))$ for a positive seed. A's maximum (B*) threshold on this cube is $\gamma V=1/4423680$ at $y_0=1/20$, and it asks for bounds on every ordered shape of the window. Dividing both thresholds by $8n^3$ leaves the same ratio,
$$
 R=5\cdot96^3\log(5042/5041)=4423680\log(1+1/5041).
$$
Using $x-x^2/2<\log(1+x)<x-x^2/2+x^3/3$ at $x=1/5041$ gives $877.45<R<877.46$. Even the bounds $1/5042<\log(5042/5041)<1/5041$ put $R$ between 877 and 878. The two rounded densities in row 1295 explain “about 876”. The exact thresholds give about **877-fold**. If one uses the doubling observable, $\psi_s(n)<\log(5042/5041)$ is *sufficient* for S by 7.33. Comparing that threshold with (B**) on this cube again gives $R$. The two observables $h$ and $\psi$ need not be equal. Row 1290, lines 386 and 425, identifies $J(1)=\psi_s(T_0)$ for ordinary full-trace sewing. Its centre-projected variant uses a different trace.

At the positive fixed point $y_c$ of $y\mapsto16(e^y-1)^2$, the limiting ratio of thresholds is $R_c=R/(20y_c)$. To bound it by hand, $16y[(e^y-1)/y]^2$ increases strictly from zero to infinity. At $y=0.05890$, the series bound from 7.56(a) gives $(e^y-1)/y<1.03005$ and $16y(1.03005)^2<1$. At $y=0.05892$, $1+y/2+y^2/6>1.03$ and $16y(1.03)^2>1$. Thus $0.05890<y_c<0.05892$, which gives $744.5<R_c<745$. The corrected factor is about **745**, as $y_0\uparrow y_c$. At $y_c$ the recursion stays fixed. A's remark on p. 59 allows other ascent constants strictly below $y_c$. It does not extend the $16.83$ estimate to the fixed point.

The proposed $6.8/m$ change of time is a gas heuristic. An exactly exponential *dimensionless* quantity would give $\log(R)/m$ for a threshold ratio $R$. The numerical rounding is consistent. In $\log R=10\log2-\log(1024/R)$, the series $2(z+z^3/3+z^5/5+\cdots)$ at $z=1/3$ gives $0.693<\log2<0.694$ (bound the remainder after $z^5/5$ by $2z^7/[7(1-z^2)]$). At $z=(1024-R)/(1024+R)\in(0.076,0.078)$ the same series puts $\log(1024/R)$ between $0.15$ and $0.16$. Thus $6.77<\log R<6.79$. Even if the density itself were $Ce^{-mT}$, the two density thresholds are $c_S/T^3$ and $c_A/T^3$. At equality the time shift would obey $m(T_A-T_S)=\log R+3\log(T_A/T_S)$. The estimates supply no Wilson equation of state from which to infer a time saving or the relative difficulty of the two inputs.

Line 200's comparison with (N-phys) also needs its size quantifier. Projection works at the same time. The S seed on a cube of side $2n$ is measured at $n$, while the neutral test at $K=512$ is at most $n/256$. For a counterexample to a *projection-only* inference, fix a large multiple $n$ of 256 and let $Z(t,M)=1+\exp[-cV(t)M]$, $c=14\log2/[n(2n)^3]$. This symmetric positive-transfer example has slice eigenvalues $1,e^{-cV(t)}$, both neutral. On the cube $(2n)^3$, $D(n)=2^{-14}<1/5041$ while $s_+(n/256)=2^{-14/256}>1/2$. It tests precisely the time comparison in the transfer setting of Theorem S.

Over admissible larger sides the claimed direction does hold for a family of seeds at a common physical base. Row 697, line 194, gives after one doubling $s'\le((1+s)^{64}-1)^2\le(65s)^2$ for $s\le1/5041$, since $64/(1-64s)\le65$. Thus $5041s'\le4225/5041<1$ uniformly. Theorem S now makes $h_{b^3}(b/2)$ uniformly small on a dyadic descendant. Its physical side is fixed first and $b$ denotes its lattice length at each cutoff. At that same time, row 697's Lemma E, lines 188–190, multiplies the log trace by at most four per spatial side doubling since the doubled side starts at least twice the time. Enlarging the cube from $b$ to $256b$ costs at most $4^{24}$, a fixed factor. Choose the descendant so this factor times its log trace is at most $\log(3/2)$. On the enlarged cube the time $b/2$ equals $(256b)/512$, and projection gives the neutral bound. Row 1161, line 150, uses the same enlargement principle with its shape-comparison bound. A single-coupling seed supplies no cutoff-uniform hypothesis on its own.

## Disposition

Row 1295 identifies a valid finite-volume route from a bound on the full trace to a bound on the neutral trace at a fixed physical aspect. The unsupplied input is the uniform small thermal density on the base window at weak coupling. The cited four-shape slab datum supplies no estimate on the missing window shapes. The derivations above are hand arguments. Retrieval, extraction and page images served only to identify and read the sources.

RESULT — Row 1311. The published conditional lattice ascent HOLDS, with all excited transfer eigenvalues zero at the zero endpoint. AU1 HOLDS from the all-window (RR) bound with $y_0=1/20$ at matched Wilson coupling. AU2 HOLDS for $K=512$ at any fixed admissible $L\ge16384t_0$, including equality when admissible. AU3 HOLDS AFTER CORRECTION to about 877-fold at $1/20$ and 745-fold approaching the fixed point. The weak-coupling seed and the four-dimensional $SU(2)$ mass gap remain open.
