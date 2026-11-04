# Nonconstant source arrays in B4
Provenance: Codex (GPT-6 family; exact serving variant and runtime effort unavailable; requested effort max); checkout `7ca5c00b4c97dbd45e1ab92af113a7f88863df79`; Sussman–Alpoge `31a47c543775`; research text, not an audit; no status granted.

## 1. Scope and cited input

This note addresses row 241 and D1–D2 of `gates/b4-ind-check.md`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the frozen-source construction.
SA denotes their [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).

SA L4908–4921 proposes a constant-source member at each base point.
It calls the array bounds “The remaining task”.
The lead's outline check stops there.
However, SA L22950–23150 gives the finite-source proof, conditional on its named formation and domain inputs.
It says: “Instead interpolate the data of a step”.
We take that detailed implication as a cited input under FINISH item 9.
This corrects the local classification of the freezing argument as merely assumed.

SA L16434–16492 proves (LB7)–(LB9) for the derivative at zero.
With \(\mathcal L_j[f]=\partial_tE_j^{tf}|_{t=0}\), its defect is
\[
 \mathcal D_j[f]=\mathcal L_j[f]-f(p_z)\mathcal L_j[1],\qquad
 \|\mathcal D_j[f]\|_\kappa
 \le CA_jL^{-(m-j)}\|f\|_{\sharp,m}.
\]
The bound retains the response amplitude \(A_j\).
The later data interpolation supplies the finite-source extension without repeated radius loss.
SA L13405–13420 also proves the separate cancellation for each frozen member.

SA L7581–7582 requires invariant remainder totals in its renormalised class.
`r-inv.md` addresses that requirement for constant sources.
The present task concerns the additional source defects.

## 2. Finite freezing on the ordinary box

Keep the inputs \(\mathscr P,BX^+,UR,YA,LOC\) of `b4-induction.md`.
Use `r-inv.md` for constant-source insertion totals.
Keep the three constant ceilings in `b4-ind-check.md`, D3.
All statements below retain those premises.
Keep the real run, tests, backgrounds, and reference measures fixed when sources vary.

Let \(h_j=L^jh_0\), fix a terminal level \(K\), and put
\[
 \|w\|_{\sharp,K}=\max\{\|w\|_\infty,C_Mh_K\operatorname{Lip}w\},
 \qquad \pi_j=L^{-(K-j)}.
 \tag{1}
\]
Use SA's fixed source radius \(r\) and its doubled constant-source disc.
The ordinary scalar envelope is \(\sum_j\mathsf d_{2r}[b_j]\le1/3\) (SA L22957–22974).
Here \(\mathsf d_R[b]=\sup_{0<|\zeta|<R}|b(\zeta)-b(0)|/|\zeta|\).
It remains an input from the constant-source run.
On \(|\zeta|<r\), Cauchy's estimate gives \(|b_j'(\zeta)|\le2\mathsf d_{2r}[b_j]\).
Thus the variable Wilson weight also has a uniform local slope.
Its tent coefficients must come from the same frozen members.

Here is the finite-freezing implication supplied by the later SA passage.
For a complete read region \(W\), define
\[
 \mu_j(W;w,\zeta)=
 \max\{\sup_{p\in W}|w(p)-\zeta|,
                 C_Mh_j\operatorname{Lip}(W;w)\}.
 \tag{2}
\]
Interpolate the input data toward the constant \(\zeta\), on \(|t|\mu_j<r\).
These data need not come from a physical source function.
Each regular member retains its own counterterm throughout the interpolation.
Older source defects gain \(h_i/h_j=L^{-(j-i)}\) on this line.
Complete reads are interpolated together.
Cut history operations use their recursively formed exponents, as in SA L23051–23150.
This clause retains the history formation premises.

The one-step gas gives a uniform bound with rate at least \(\kappa+1\).
The source-independent Gaussian normalizer cancels in the difference.
Schwarz on the data line gives
\[
 |E_j^w(X,P,z)-E_j^\zeta(X,P,z)|
 \le C\mu_j(X^\sim;w,\zeta)
                        e^{-(\kappa+1)d_j(X)}.                 \tag{3}
\]
When the line's radius is at most one, the two endpoint bounds give (3).
The constant \(C\) includes the fixed factor \(r^{-1}\).
It is independent of \(j,K\), volume, and the number of source labels.
For \(w=c+\sum_\ell z_\ell f_\ell\), use the same bound on
\(|c|+\sum_\ell|z_\ell|\|f_\ell\|_{\sharp,K}<r\).

Set \(\zeta=w(p_z)\).
The complete read geometry (LB2) gives
\(\mu_j\le C_Mh_j(1+d_j(X))\operatorname{Lip}w\).
Since \((1+d)e^{-d}\le1\), (3) yields
\[
 \|E_j^w-E_j^{w(p_z)}\|_{j,\kappa}
 \le C_fh_j\operatorname{Lip}w
 \le C_f'\pi_j\|w\|_{\sharp,K}.                              \tag{4}
\]
For sources measured at level \(m\ge j\), replace \(K\) by \(m\).
This gives exactly the gain \(L^{-(m-j)}\) of (LB9).
Unlike (LB7), (3) controls finite sources.
The enlarged domain is a step-data box, so no source radius shrinks with the number of steps.

## 3. The profile closes uniformly

Write \(\mathcal F_k^\circ[w]\) for the output with the earlier regular-source defects set to zero.
Keep the sourced aged remainders in their own sector.
Their formation estimate uses their norms, without (20).
Use plain insertion for these remainders, as allowed by `ti-2.md` §4 at the constant specialization.
There, `r-inv.md` makes plain insertion equal to (INS).
At nonconstant sources, retain every remainder term.
Averaging that fixed source array would not preserve its total.
Thus no unbounded succession of remainder-sized (INS) defects is introduced.

Let \(d_j=\|D_j^w\|_{j,\kappa}\).
Split the new difference exactly into
\[
 D_k^w=
 [\mathcal F_k(w,D_{<k})-\mathcal F_k^\circ[w]]
 +[\mathcal F_k^\circ[w]-E_k^{w(p_z)}].                        \tag{5}
\]
The first bracket is the defect dependence in `b4-induction.md`, Step 4.
The data-line proof of (3)–(4) applies to the second bracket with those slots identically zero.
They vanish at constant sources.
Hence
\[
 d_k\le Cs_{k-1}\sum_{j<k}\rho_{j,k}^2d_j+a\pi_k,
 \qquad a=C_f'\|w\|_{\sharp,K}.                              \tag{6}
\]
Use the admissible radius bound \(\rho_{j,k}^2\le C_\rho(1+k-j)\).
For \(q=L^{-1}\), the geometric series and its derivative give
\[
 S_L:=\sum_{n\ge1}(1+n)L^{-n}
 =\frac{q}{1-q}+\frac{q}{(1-q)^2}
 =\frac{2L-1}{(L-1)^2}.                                     \tag{7}
\]
Indeed \(\pi_j/\pi_k=L^{-(k-j)}\).
Consequently
\[
 Cs_{k-1}\sum_{j<k}\rho_{j,k}^2\pi_j
 \le CC_\rho s_*S_L\pi_k\le\tfrac12\pi_k.                    \tag{8}
\]
Fix \(\varepsilon\le\min\{r/2,(2C_f')^{-1}\}\) and require \(\|w\|_{\sharp,K}\le\varepsilon\).
Include \(2C_f'\varepsilon C_\rho S_L\) in the input budget \(N_*\).
Choose the coupling floor last so that \(CC_\rho s_*S_L\le1/2\) and \(s_*(1+N_*)\) is small.
This choice depends on \(L\), not on \(K\).
With the empty initial list, (6) now proves by induction
\[
 d_j\le2a\pi_j,
 \qquad N_{k-1}(D)\le2aC_\rho S_L\pi_k\le2aC_\rho S_L.       \tag{9}
\]
The induction step substitutes \(d_j\le2a\pi_j\) into (6) and uses (8).
The first level has no old bracket.
The fixed source radius gives \(2a\le1\).
Then every defect satisfies the ordinary box bound, including at \(k=K\).
For \(K=k\) or \(K=k+1\), this is SA's ordinary step profile.
The profile has no failing source array within this fixed Lipschitz ball.
An unrestricted spatial array has only its stipulated one-step defect bound.

## 4. The sourced induction statement

Use one localization rule for the actual output and its constant specializations.
This can be arranged by carrying the source in Lemma R's average:
\[
 \widetilde F_k^w(X,P,z)=\frac1{|\mathfrak G_k|}
 \sum_{g\in\mathfrak G_k}
 F_k^{g^{-1}w}(g^{-1}X,g^{-1}P,g^{-1}z).                     \tag{10}
\]
Here \(gw\) transports the source array and its anchors.
Earlier sourced identities and (NAT) give \(S_k^{gw}(gU)=S_k^w(U)\).
Substitute \(V=gV'\) in Theorem TI's kernel.
This proves (12) before the current gas identity.
After gas summation, \((ID)_k\) gives the same covariance for the formed total.
Thus (10) preserves that total at complete physical reads and their datum continuations.
On the full cores it preserves holomorphy, norms, and complete read locality.
At constant sources it is exactly Lemma R's average.
Transport preserves distances, so (3)–(9) hold for this rule too.

At each actual base \(z\), supply the entire Euclidean member
\[
 G_{k,z}^w:=\bar E_k^\zeta\big|_{\zeta=w(p_z)},\qquad
 b_{k,z}^w:=b[\bar E_k^\zeta]\big|_{\zeta=w(p_z)}.             \tag{11}
\]
Only its term pointed at \(z\) enters the array.
The hypothetical other bases of this member all use the same \(\zeta\).
The actual output is that frozen array plus \(D_k^w\).

**\(TI_k\) for sources.** Each frozen member has the invariant total of Theorem TI on its admitted physical pairs.
The actual sourced functional satisfies
\[
 \mathcal E_k^{gw}(gW)=\mathcal E_k^w(W).                     \tag{12}
\]
Its formed total satisfies the same identity, by \((ID)_k\).
The identities extend to the stated common complex domains.
Invariance at fixed nonconstant \(w\) is not asserted.

**\((20)_k\) for sources.** Put
\(F_{k,z}^\zeta(B)=\sum_{X\ni z}\bar E_k^\zeta(X,P_k(B),z)\).
Theorem P gives, before any restriction of the pointed sum,
\[
 D^2\!\left[F_{k,z}^{w(p_z)}
       -b_{k,z}^w(A_z\circ P_k)\right](0)[\ell_F,\ell_F]=0.   \tag{13}
\]
There is one coefficient for each selected member.
No coefficient is assigned to \(D_k^w\).

**\(H_{\le k}\) for sources.** Carry the original analytic domains, normal gas convergence, locality, bounds, and \((ID)_i\).
For every \(i\le k\), add (11)–(13) and the defect bound (9).
Carry the complete-read data-line bounds (2)–(3) for the sourced remainder and history inputs.
SA's formed-line argument propagates those bounds on the same radius, given its formation premises.
Steps 1–5 of `b4-induction.md` use only earlier members and budgets.
Step 6 applies TI and Lemma R to each constant specialization.
Theorem P then supplies (13) for the next step.
Equation (8) supplies the previously missing budget edge.
Hence \(H_{<k}\) extends to \(H_{\le k}\), uniformly in run length and torus.

## Result

**Proof of the source-profile induction, conditional on the inherited ordinary formation inputs.**
The finite-source freezing implication is already proved in SA L22950–23150 under those inputs.
Thus this also corrects the lead's incomplete outline classification; it is not a correction of SA.
Equations (8)–(13) close D1–D2 for the admitted Lipschitz source trajectory.
They give ordinary B4 with frozen-member TI and cancellation, and covariance of the full sourced output.
The typed potential and zone tests remain separate.
This proof is by hand and has not been independently checked.

**First input still open for this argument:** (D4) of `loc-4.md` §5.
It must admit the carried compositions on their full common complex domains, including stored arguments and healing gauges.
`d4-stage.md` (5) isolates its unresolved continuation budget for the actual transported (R5) datum.
The source interpolation uses those domains; the profile estimate does not supply them.
The constant-source envelope and all other inherited formation premises also remain required.
