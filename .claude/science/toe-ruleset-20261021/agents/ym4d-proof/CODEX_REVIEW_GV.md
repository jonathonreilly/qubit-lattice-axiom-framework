## PRE-STATED

Independent hostile review of `GV55.md`. Requested reviewer configuration: Codex gpt-6-astra, max. This report records the checks actually performed; prior reviewer conclusions are dependency claims, not substitutes for checking interfaces.

Scope: the five claims in the user request, especially Proposition GV-E's change of source norm and the alleged failure of restriction between slices. No git; this is the only file authorized for writing. Large sources will be read through searches and bounded `sed` ranges. Arithmetic checks will use integers, rational numbers, or exact symbolic identities only.

Exposure before this registration: the user supplied the claims; the initial source search exposed GV55's statements, conclusions, and part of its proof. No independent derivation or numerical experiment had yet been performed. This is a pre-statement of the independent checks, not a claim of blindness to the author's conclusions.

1. Reconstruct the norm definitions and test the proposed constant level-1 source, including transpose normalization, composite co-closedness, and the actual top response. A norm mismatch establishes failure of a stated estimate to imply another estimate; it does not itself refute the desired estimate.
2. Trace every use of $N_\Sigma$ through CC-INV, TOP-cc, the unconverted RHT-cc estimate, EP-rec, and the inhomogeneous boundary response. Test $k=1$, fixed $\sigma>\alpha$, and $\sigma=1$. Accept GV-E only if constants are independent of $k,T$ and no level-weighted plain-current norm is silently restored.
3. Check the slice map and gauge signs, including descent for $T=3,4$, before using the gauge-fixed inverse in the nonlinear theorem. Match the actual conclusion and hypotheses of KOFF's banked implication, including (LA-1′), its analytic completion, the ball, and BFT-2's meaning.
4. Independently compute the dimensions and kernel implications for the depth-$j$ and depth-$k$ slice maps. Test whether a rank statement really implies non-preservation on the domain used by BA-9. Separate failure of that proof from failure of physical identification and from necessity/sufficiency of a proposed NSL repair.
5. Trace the weighted field estimate at $0\le m\le m_Y$, distinguishing finite-range reconstruction from global Coulomb estimates and checking source/data norms and small-torus descent.

Decision rule: **CONFIRMED** requires a matching proof or an explicitly scoped implication with all imported inputs identified; **REFUTED** requires an exact contradiction/counterexample to the stated claim; **NOT-VERIFIED** records a material missing step without asserting falsehood. Findings will cite a file and locating string. The final section will state exactly what may be banked.

## Disposition

**CONFIRMED as named-input implications:** Proposition GV-E, the corrected KOFF + GV-E contraction on the specified slice, and Proposition GV-E_m in its explicit source norms. The slice and small-torus gauge identity also check out.

**REFUTED:** the rank inequality and rank-based proof in GV55 §3.3. The inequality goes in the opposite direction. **CONFIRMED by a replacement proof below:** the elliptic slices nevertheless are not preserved under restriction. An exact quintic-tent example gives a nonzero defect of `−640/19683`. Thus the identification gap survives, but the author's reason for it must be replaced.

**NOT-VERIFIED:** NSL itself, identification with the prescribed per-level branch, analyticity of that branch action by this argument, and replacement of the explicit source-representation norm by an unrestricted abstract dual norm. The original BFT-0/2 and BFT-5(b) labels must not hide these qualifications.

All filenames below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. Locating strings accompany the findings so that line drift does not change their meaning. This is an independent review of the local packet, not a fresh audit of its entire inherited linear package.

## 1. The norm mismatch and the exact source witness

**CONFIRMED.** Target: `GV55.md`, §1.3, locating `N(S) is not bounded by C·N^{(σ)}(S) uniformly in k` and `Supporting computation for the §1.3 example`. Definitions: `COFUN_CC.md`, `Norms`; `KFACTOR_OFF55.md`, `The transport-weighted pair`.

Write

\[
A_0=\|G_0^c\|_\infty+[G_0^c]_\alpha,\qquad
J=\sum_{l=0}^{k-1}\pi_l(j_l),\qquad
\pi_l(j_l)=L^{3(k-l)}\|j_l\|_{\infty,\mathrm{own}}.
\]

The actual norms are

\[
\begin{aligned}
N(S)&=A_0+\pi_0(j_0)+\max_{1\le l<k}L^{\theta(k-l)}\pi_l(j_l)
       +\|G\|_Y+\|s\|_R,\\
N_\Sigma(S)&=A_0+J+\|G\|_Y+\|s\|_R,\\
N^{(\sigma)}(S)&=A_0+J+\|s\|_{R(\sigma)}.
\end{aligned}
\]

These are norms of the specified source representations. No minimization over alternative representations, and no identification with a full Banach dual, is implicit here.

For $k\ge2$, put $j_1=(Q^{(1\to k)})^T(c e_\mu)$, $c\ne0$, and set every other source slot and $B_k$ to zero. One step of the transpose on a constant current is exactly multiplication by $L^{-3}$: `BFT_B.md`, `29.3 Theorem RHT-cc`, displays

\[
(Q_{\rm str}^Tj)(b)=L^{-4}\sum_{i=0}^{L-1}j(X(b-ie_\mu),\mu).
\]

Moreover $Q^T=Q_{\rm str}^T-h^Td^*$, and $d^*$ kills a constant current. Therefore

\[
j_1=L^{-3(k-1)}c e_\mu,\quad d^*j_1=0,\quad
D(S)=0,\quad J=|c|,
\]

and exactly

\[
N(S)/N^{(\sigma)}(S)=L^{\theta(k-1)},\qquad
N_\Sigma(S)=N^{(\sigma)}(S)=|c|.
\]

The top response can be checked against every link Euler equation, without assuming fine-translation invariance of the rooted operator. For constant fields $x_i=a_i e_\mu$, set $a_k=0$, $r_i=La_i-a_{i+1}$, and write $J_i$ for the own-unit constant current amplitude. The curvature term vanishes and the full Euler equation is

\[
L^{-3}\kappa_i r_i-\kappa_{i-1}r_{i-1}=J_i,
\]

where the preceding term is zero at $i=0$. Consequently $r_0=0$, and for $1\le i<k$,

\[
\kappa_i r_i=L^{3i}J_1=L^{-3(k-1-i)}c.
\]

Backward substitution $a_i=(r_i+a_{i+1})/L$ gives a genuine full critical point, and

\[
r_{k-1}=r^c_{k-1}=c/\kappa_{k-1}.
\]

Composite root-pinned gauge changes leave this residual invariant, so it is also the residual of the $S_E$ response. This confirms both normalizations in the proposed witness.

The logical conclusion is precise: the displayed GF-E bound with $N(S)$ cannot be converted into GV by a uniform comparison of the stated right-hand sides. This is **not** a counterexample to GV; the response is compatible with the stronger bound. The witness also does not establish growth of the actual nonlinear Wilson correction in the $P_c$ norm. GV55 correctly labels that latter attainment unverified.

## 2. Proposition GV-E: the J-based proof survives

**CONFIRMED as an implication.** Target: `GV55.md`, `The repair — Proposition GV-E`, proof steps 1–6. Inputs: `CODEX_REVIEW_TOPCC.md`, banking item 3, `The bound also holds with N_Σ`; `COFUN_CC.md`, `The same with N_Σ` and `Theorem CC-INV`; `BFT_B.md`, `Theorem RHT-cc` and `29.3 Theorem RHT-cc`; `CODEX_REVIEW_GSHARP.md`, banking items 1 and 3.

The stronger estimate in the weaker source norm is available in the invariant inputs. In particular, TOP-cc's regrouped plain-current estimate uses

\[
\pi_0(C(j')), \max_l\pi_l(\widehat j'_l)
\ \le\ \left(1+\frac{2d}{1-L^{-3}}\right)|j'|_\Sigma,
\]

and the flux/decomposition correction is bounded in the same level-sum norm. There is no need to return to $P_c$. I accept the named analytic inputs to these banked estimates; I do not promote their conditional status to an unconditional proof of the entire package.

Here is the independent summation check. Set $a=1-\alpha>0$, $\alpha<\theta_0<1$, and

\[
K_f=\frac{2d}{1-L^{-(2+\alpha)}}.
\]

The unconverted RHT-cc display gives

\[
\begin{aligned}
N_{\rm res}(x)\le\frac5{\kappa_-}\bigg[&
\frac{\kappa_+\|r^c_{k-1}\|_\infty+L^{-\theta_0}\|s\|_R}{L^a-1}
+\frac{L^{-\theta_0}\|s\|_R}{L^{\theta_0-\alpha}-1}\\
&+\frac1{1-L^{-a}}\left(
 (1+K_f)L^{-a}J+
 \frac{6\|G\|_Y}{L^{\theta_0-\alpha}-1}\right)\bigg].
\end{aligned}
\]

The plain sums are bounded by $L^{-a}J$ because $k-l\ge1$. For the funnel contribution, interchanging the nonnegative sums gives the convergent convolution

\[
2d\sum_{u\ge0}L^{-(3-a)u}
=\frac{2d}{1-L^{-(2+\alpha)}};
\]

there is no factor $k$. For positive-level divergence sources,

\[
\sum_{l\ge1}L^{-a(k-l)}L^{k-l}\|G_l^c\|_\infty
\le \|G\|_Y\sum_{u\ge1}L^{-(\theta_0-\alpha)u}
=\frac{\|G\|_Y}{L^{\theta_0-\alpha}-1}.
\]

TOP-cc supplies the top residual in $N_\Sigma$; CC-INV supplies the invariant norm in $N_\Sigma$. EP-rec therefore gives

\[
\|x_E(S,0)\|_{\mathfrak M^\nabla}
\le C_{\rm rec}(\|x\|_{\rm inv}+N_{\rm res}(x))
\le C_S N_\Sigma(S).
\]

For $k=1$, $N_{\rm res}$ is an empty sum; no denominator or absent level-1 slot is needed. The data-only case follows from GF-E′ with all sources zero, in the same slice. Linear superposition yields

\[
\boxed{\ \|x_E(S,B_k)\|_{\mathfrak M^\nabla}
\le C_{\rm GV}\bigl(N_\Sigma(S)+\|B_k\|_D\bigr).\ }
\]

For the representations consumed by KOFF, $G_l=0$ for $l>0$, so $\|G\|_Y=A_0$. With $q=k-1-l\ge0$,

\[
\|s\|_{R(\theta_0)}
=\max_q L^{\theta_0(q+1)+q}\|s^c_{k-1-q}\|_\infty
\le L^{\theta_0}\|s\|_{R(\sigma)}
\quad(\theta_0\le\sigma).
\]

Thus the exact advertised comparison is valid:

\[
N_\Sigma(S)=2A_0+J+\|s\|_{R(\theta_0)}
\le\max(2,L^{\theta_0})N^{(\sigma)}(S)
\le L N^{(\sigma)}(S).
\]

For every fixed $\sigma\in(\alpha,1]$, one may choose, for example, $\theta_0=(\alpha+\sigma)/2$. This is strictly below 1, including at $\sigma=1$. Constants may depend on these fixed exponents; no uniformity as $\sigma\downarrow\alpha$ is asserted. All level sums above are bounded independently of $k$, and the imported estimates are uniform in $T$. The descended small-torus construction is checked in §3 below.

GV's left side has only the three field terms; it has no residual-weight slot. The stronger residual weight $2+\sigma$ is supplied separately by $\mathrm{LIN}^{(\sigma)}$. Consequently the repaired proof supplies exactly the missing GV hypothesis, rather than proving an unnecessary new residual-Hölder theorem.

## 3. Slice matching and the sign, including T = 3,4

**CONFIRMED.** Target: `GV55.md`, `1.1 The slice — SAME object`; definitions: `BFT_B.md`, `Setting EΠ (elliptic slice)` and `16.1 Lemma EP-alg`; `BFT_A.md`, `Γ_E(x) := Λ(x)` and `33.13 Proposition SM`.

The functional is the same one:

\[
\Gamma_E(x)=\Lambda(x)=\sum_X\chi_X^5\lambda_X^E(x),\qquad S_E=\ker\Lambda.
\]

For any scalar gauge function $\mu$, the pinned Neumann minimizer obeys

\[
\lambda_X^E(x+d\mu)=\lambda_X^E(x)-\mu+\mu(c_X).
\]

If $\mu$ vanishes at the terminal roots, the last term is zero and the partition of unity gives

\[
\Gamma_E\Xi\mu=-\mu.
\]

Also $\Lambda(x)$ vanishes at every terminal root. Thus the codomain is the pinned gauge-function space and the stated map on that space is onto, with the indicated sign. The different meanings of `Λ_0` in the older files must be replaced by the explicit pinned-space description; the identity is not $-\mu$ for an arbitrary nonzero constant root value.

For a cc source, apply the pinned adjoint $\Xi^T$ to

\[
(H+\Gamma^T\Gamma)x=S.
\]

Since $H\Xi=0$, $\Xi^TS=0$ on pinned directions, and $\Gamma\Xi=-I$, this gives $-\Gamma x=0$, hence $Hx=S$. The analogous data right-hand side also annihilates pinned gauges. The kernel of $H$ is precisely the composite pinned gauge space, so this is the unique slice representative identified by EP-opt. There is no additional projected-source estimate concealed in this identification.

For $T=3,4$, let $\widetilde x$ be its periodic lift to an admissible larger torus. Coarse translation covariance makes $\Lambda_{T'}(\widetilde x)$ periodic with the original period, and its restriction defines $\Gamma^{(T)}$. A pinned $\mu$ lifts to a pinned $\widetilde\mu$. Therefore

\[
\Gamma^{(T)}\Xi\mu
=\left.\Lambda_{T'}(\Xi\widetilde\mu)\right|_T
=-\mu.
\]

Its image is still pinned. This verifies the exact algebra required by KOFF at $T=3,4$, not merely boundedness of a descended projection. The same reasoning covers the other small tori in the linear estimates.

## 4. Theorem BFT-E: confirmed implication, with the value identified correctly

**CONFIRMED for the explicit slice theorem.** Target: `GV55.md`, `Theorem BFT-E (assembly)`; input: `CODEX_REVIEW_KOFF.md`, `5.3 What the contraction statement actually earns` and banking item 5. The input is the corrected theorem with (LA-1′) and §4.3's finite local analytic completion. It is not the literal theorem based on the false printed (LA-1).

The composed response bound is $G=G_{\rm inv}(\sigma)+G_{\rm gv}$. The banked corrected-source bounds have the form

\[
N^{(\sigma)}(\widetilde S(x))\le K(\eta+s)^2,\qquad
N^{(\sigma)}(\widetilde S(x)-\widetilde S(x'))
\le K(\eta+\eta'+s)\|x-x'\|_{(\sigma)},
\]

with $s=\|B_k\|_D$. Every inverse source is cc, by CCP and root-pinned CD. The newly supplied Γ and GV therefore match the actual hypotheses, including all off-critical iterates.

For example, take $C_0=\max(2,4G)$ and reduce the data radius so that

\[
GK(2C_0+1)\varepsilon_0\le\tfrac12,\quad
GK(C_0+1)^2\varepsilon_0\le C_0/4,
\]

as well as the local analytic and CCP injectivity conditions in the cited review. This gives the invariant ball and contraction. At fixed $B_k$, the expression involving $Qx_{k-1}-B_k$ defines an **affine** ball; differences use zero terminal datum. There is no claim that it is a norm of $x$ independent of the datum. CCP then identifies the fixed point with a full critical point and excludes other full critical points in that slice ball.

The bankable quantitative conclusions are exactly the displayed ones in GV55:

\[
|\log U_{j,p}|\le L^{-2(k-j)}(2\eta+9\eta^2),\qquad
|\rho_j|\le L^{-(2+\sigma)(k-1-j)}\eta+C L^{-3(k-j)}\eta^2,
\]

and $|x_j|\le L^{-(k-j)}\eta$, with the stated coarse field/curvature regularity. The weight triple $(2,2+\sigma,1)$ refers to these explicit estimates. In particular, the source/transport pair uses a residual **sup** term; a stronger residual Hölder norm with that entire extra exponent is not silently added to its definition.

The fixed local analytic extension and the complexified fixed inverse give a uniform analytic contraction on a smaller complex ball. Thus $x^*(B_k)$ and

\[
E_k^{\rm comp}(B_k):=\mathfrak F_k(x^*(B_k);B_k)
\]

are holomorphic on a fixed small terminal-data polydisc, independently of $k,T$. No per-level covariance is used as an inverse.

**NOT-VERIFIED if “BFT-2” means the original prescribed branch action.** `REVIEW_S22.md`, locating `BFT-2 (analyticity)`, names $E_k^{br}$. GV55 explicitly proves analyticity of the composite value above, while §3.3 retains $E_k^{cb}=E_k^{br}$ as an unresolved identification. Therefore `GV55.md`, locating `This is REVIEW_S22's` and the proposed tally updates in §7.4, must retain this qualification. Analyticity of the composite value does not itself identify it with the previously prescribed branch action. The slice existence/uniqueness and the displayed regularity estimates are unaffected.

## 5. Restriction: the rank proof is wrong, but an exact witness repairs the conclusion

### 5.1 The displayed inequality is refuted

**REFUTED.** Target: `GV55.md`, §3.3, locating `Proof (rank count)` and `rank Λ^{(j)} = N_0 − N_j`; repeated in finding V16 and summary N4. Count convention: `BFT_A.md`, `1.1 The composite problem`, level-$i$ side $TL^{k-i}$.

On the common fine torus, $N_i=(TL^{k-i})^4$. For $j<k$,

\[
N_j>N_k,\qquad N_0-N_j<N_0-N_k.
\]

The individual ranks, per Lie-algebra component, are indeed $N_0-N_j$ and $N_0-N_k$: the image vanishes on the corresponding roots, and $\Lambda^{(i)}\Xi=-I$ on functions pinned there proves surjectivity. But their ordering is the opposite of the author's. Kernel inclusion would imply precisely the true rank inequality, so it produces no contradiction. For the exact example $L=3,k=2,j=1,T=5$,

\[
(N_0,N_j,N_k)=(4100625,50625,625),\qquad
(\operatorname{rank}\Lambda^{(j)},\operatorname{rank}\Lambda^{(k)})=(4050000,4100000).
\]

The asserted dimension obstruction cannot be banked.

### 5.2 Independent exact non-preservation witness

**CONFIRMED.** Target conclusion: `GV55.md`, `a depth-k slice point restricted to depth j is in general not in the depth-j slice`. Construction uses only `BFT_B.md`, `Setting EΠ` and `16.1 Lemma EP-alg`, not any rank inference.

Let $I_i u=\sum_X\chi_X^{5,(i)}u(c_X^{(i)})$ be the depth-$i$ quintic-tent interpolant of root values. For an arbitrary periodic scalar $\mu$, the local minimization for $x_0=d\mu$ has the explicit zero-energy solution

\[
\lambda_X^{E,(i)}=-\mu+\mu(c_X^{(i)}).
\]

It is the unique pinned solution. Hence the exact identity

\[
\Lambda^{(i)}(d\mu)=-\mu+I_i\operatorname{ev}_i\mu.\tag{*}
\]

Choose $d=4,L=3,k=2,j=1$, with depth-2 torus side $T=5$. Translate a common root to the origin. The nested depth-2 roots are spaced 9 fine steps and the depth-1 roots 3 fine steps. The depth-1 torus after restriction has side 15; both slices use embedded boxes.

Give the depth-2 roots value 1 when their first coordinate is 0 modulo 45 and 0 at the other first-coordinate roots, independently of the other three coordinates. Let $\mu=I_2u$. Tensor partition of unity reduces this exactly to a one-coordinate function. On $0\le t\le9$,

\[
\mu(t)=s(t/9),\qquad s(t)=1-10t^3+15t^4-6t^5.
\]

Since interpolation reproduces its root data, (*) gives $\Lambda^{(2)}(d\mu)=0$ everywhere. But at the fine site $t=1$,

\[
\begin{aligned}
\mu(0)&=1,&\mu(3)&=s(1/3)=64/81,&\mu(1)&=s(1/9)=19456/19683,\\
(I_1\operatorname{ev}_1\mu)(1)
&=s(1/3)\mu(0)+s(2/3)\mu(3)
=6272/6561.
\end{aligned}
\]

Consequently

\[
\boxed{\ \Lambda^{(1)}(d\mu)(1)
=6272/6561-19456/19683=-640/19683\ne0.\ }
\]

This is a four-dimensional example, not a lower-dimensional model extrapolated to four dimensions: the tensor-product tents and the exact zero-energy Neumann solution establish the reduction directly. Multiplication by a fixed nonzero Lie-algebra element gives the stated field convention.

Complete the chain by $x_l=d\operatorname{ev}_l\mu$, including $B_2=d\operatorname{ev}_2\mu$. Root covariance gives $r_l=0$, and $dx_0=0$; thus it is even a source-free critical point of the linear energy. Scaling $\mu$ by any positive rational factor makes all fields and data arbitrarily small while preserving the nonzero slice defect. The failure is not an artifact of large fields or an inadmissible fine-lattice domain.

It follows that BA-9's assertion `the per-level covariant slice is a product of per-level conditions, so restriction preserves it` (`BFT_A.md`, §3.8) cannot be imported for $S_E$. The corrected reason is failure of quintic interpolation to be compatible with subdivision, not an excess of lower-depth constraints.

### 5.3 What the identification gap does and does not establish

**CONFIRMED:** the present proof does not deliver BFT-0's per-level identification. **NOT-VERIFIED:** NSL, or a theorem saying that NSL is the only possible repair. Locations: `GV55.md`, `(NSL)_j` and `Status of (NSL): OPEN`; `BFT_A.md`, `What BA-9 does not give`.

The witness is not a counterexample to identification modulo gauges. For a pure gradient, the discrepancy in (*) is itself corrected by the root-pinned gauge $I_j\operatorname{ev}_j\mu-\mu$. It proves only that direct restriction into the chosen slice fails. A uniform nonlinear gauge-attainment theorem such as NSL is one sufficient route to a comparison modulo depth-$j$ gauges. A direct gauge-invariant uniqueness argument would be another possible route; none is ruled out here.

To use NSL in BA-9, the transformed restricted critical point must lie in a region of **critical-point uniqueness**, not merely have small absolute norm. One cannot infer membership in the radius $C_0\|\log U_j\|_D$ ball from a bound in terms of the original depth-$k$ datum: that lower datum may be much smaller. The corrected KOFF Lipschitz estimate does allow uniqueness of any two fixed points in a sufficiently small fixed-radius slice neighborhood, independently of the datum's exact size. Shrinking the original data radius after a uniform $C_N$ is supplied would handle this point. NSL would then support the modulo-gauge/value comparison, subject to the other BA-9 branch conventions. It still would not establish equality to a separately prescribed $E_j^{br}$ without the branch-ball identification already retained in BA-9.

The sketch's derivative $\Lambda(-\Xi\xi)=\xi$ at zero is correct. Uniform nonlinear estimates and ball membership are not proved by that derivative alone. This review does not bank NSL from the phrase `ARGUED-standard`.

## 6. Proposition GV-E_m: the weighted field estimate is a valid assembly

**CONFIRMED as an implication in the stated representation norms.** Target: `GV55.md`, `Proposition GV-E_m`; inputs: `CODEX_REVIEW_GSHARP.md`, banking item 6 and `Positive mass: finite reach is enough`; `CODEX_REVIEW_COFM.md`, banking preamble and items 2–4; `BFT_B.md`, `29.5 Theorem RHT_m-cc` and `Theorem RH_m`; review checks: `REVIEW_BFT_B_S9_S10.md`, `S9-8`, and `REVIEW_BFT_B_S6.md`, `B.6 Theorem RH_m`.

Here the norm must be COFM55's actual $N_{\Sigma,m}$, not an unspecified weighting of the earlier display. Its level-zero divergence slot is

\[
\|G_0\|_m^L=\|wG_0^c\|_\infty+[wG_0^c]^\infty_\alpha,
\]

its positive-level divergence slot is a weighted **sup** maximum, and its plain slot is $J_m=\sum_l\pi_{l,m}(j_l)$. See `COFM55.md`, `New shorthands` and `N_m(S) :=`. Campanato and pointwise equivalences at zero weight do not license dropping this weighted source convention.

For centre roots and fixed package constants, choose $c$ with

\[
L^c\ge\max(260,6952C_j),\qquad
m_Y=\frac{\log2}{16L^c}\le m_*'/6.
\]

If the second condition is not imposed, keep the minimum with $m_*'/6$. GV55 does impose it.

The finite-reach reconstruction gives, with an unspecified absolute $C_*$,

\[
\|\Pi_E x\|_{\mathfrak M^\nabla,m}
\le C_{\rm rec}e^{C_*m}
\bigl(\|x\|_{{\rm inv},m}+\|x_k\|_{D,m}+N_{{\rm res},m}(x)\bigr).
\]

No derivative of the weight is needed. RHT_m-cc is the preceding geometric summation with weighted sup norms and a fixed factor at most $e^{14m}$; the centre-root funnel costs $e^{2m}$. TOP-cc_m removes its top-response term, and CC-INV_m supplies its invariant input. Thus, for $B_k=0$,

\[
\boxed{\ \|x_E(S)\|_{\mathfrak M^\nabla,m}
\le C(m)N_{\Sigma,m}(S),\qquad 0\le m\le m_Y.\ }
\]

The bound with $N_m$ follows from the geometric comparison of the level-sum plain norm with its $P_c$ form. For the source-free data response, Proposition W and the data clause of RH_m instead give

\[
\boxed{\ \|y_E(B_k)\|_{\mathfrak M^\nabla,m}
\le C_D(m)\|B_k\|_{D,m},\qquad 0\le m<m_*'.\ }
\]

Constants are independent of $k,T,X_0$; on the larger data range they may depend on a strictly positive strip margin. Neither conclusion uses DX_m, DB_m, or an exponentially localized global Coulomb potential. The reconstruction uses pinned local Neumann gauges; the inherited invariant estimates are used only at their banked scope.

**Small-torus citation correction.** Target: `GV55.md`, proof of GV-E_m, locating `≤ 16 cells, factor ≤ e^{4m}`. `CODEX_REVIEW_COFM.md`, locating `For T ≤ 2`, supplies that statement only for $T\le2$, not all $T\le4$. In dimension four, the coarse ℓ¹ diameter for $T\le4$ is at most $2T\le8$. The safe repair is immediate on the original torus:

\[
1\le w\le e^{8m},\qquad
\|\Pi^{(T)}x\|_{\mathfrak M^\nabla,m}
\le e^{8m}C_{\rm rec}
\bigl(\|x\|_{{\rm inv},m}+\|x_k\|_{D,m}+N_{{\rm res},m}(x)\bigr).
\]

Use unweighted SM/EP-rec and compare these norms directly; do not assert that a single-centre weight is unchanged by lifting. The citation's extension is **REFUTED**, while the all-$T$ theorem with an unspecified uniform $C(m)$ is **CONFIRMED** after this correction.

**NOT-VERIFIED numerical reach:** neither $C_*=21$ nor GV55's explicitly `ARGUED` count 36 is needed or banked. The finite absolute reach is enough. No decimal exponential comparison enters this review.

**NOT-VERIFIED broad clause promotion.** `GV55.md`, locating `What remains of clause (b) is (R2)`, is justified only if clause (b) is explicitly restricted to these source representations and their norms. `BFT_B.md`, `32.1 (BFT-5_E)`, instead prints a bound in $\|S\|_{\mathfrak M^*}$ for every cc source and originally claimed gauge-fixing-independent field bounds. The latter are already refuted by `CODEX_REVIEW_GSHARP.md`; the former requires a uniform source-norm/representation comparison. GV-E_m proves the displayed $N_{\Sigma,m}$ estimate, not that additional comparison. No such comparison is supplied by cc membership. This does not affect KOFF, whose corrected sources have explicitly controlled representations.

## 7. Evidence and review boundary

The new independent checks were the unconverted residual/funnel summation, the source-norm comparison with its endpoint window, the linkwise constant-sector Euler equations, the pinned-gauge inverse identity, the small-torus descent identity, and the explicit cross-depth interpolation witness. The analytic reconstruction, invariant linear estimates, and corrected KOFF nonlinear estimates remain named imported implications at their reviewed scope.

One in-memory `python3 -I -B` invocation used only integers and `fractions.Fraction`. It reproduced the three interpolation fractions and the nonzero defect, the rank counts above, and all constant-sector Euler equations and source/top normalizations for $L=3,5$, $k=2,\ldots,7$, $c=7/11$, and $\kappa_i=(i+2)/(i+1)$. The all-depth conclusions come from the symbolic recurrences and geometric series, not these finite cases. No floating-point computation, numerical analytic radius, new script, or check artifact was used.

This review applies the repository review-loop evidence and premise rules within the user's narrower one-file scope. No git command, branch operation, source repair, status-ledger update, or external communication was performed. Exact non-preservation is a counterexample to a particular slice-compatibility assertion, not a no-go theorem for Yang–Mills, nonlinear gauge attainment, or branch identification by another route.

Local SHA-256 content identities of the principal inspected packet, rechecked unchanged after drafting:

| File | SHA-256 |
|---|---|
| `GV55.md` | `23bbd4ff8976ccd89a822b5e1b2b79eec0e3a859973cb2f3d0e460f2ba05f843` |
| `COFUN_CC.md` | `2a399a7dce1de8f0a4e9b4dfb81d9f0595e8eb4d8b294e2764b1b518d98ce035` |
| `BFT_A.md` | `8074d6c5efe3648bfb28e3463a6076cf6df74c9c358a8613390044148ac6fbe0` |
| `BFT_B.md` | `b6ddf451a4dfe2028a9f23fe7fe696ce11f1c17e497709ac3761da3e7a1172c6` |
| `KFACTOR_OFF55.md` | `6a47b6543bfefa31f8eb103ff057c4d64b38a97a48f35a195caa70367a9c3159` |
| `CODEX_REVIEW_GSHARP.md` | `0089399ed8af98529176046fe0b7ad10b60c3211718051a736c41b10ff8e50b5` |
| `CODEX_REVIEW_TOPCC.md` | `68bc5d15520d1cc12e25ff0aef313f75c8bcf00965fce34821c1ed0afbb313d6` |
| `CODEX_REVIEW_KOFF.md` | `e284b99415a1abb6f3a7ceaafb81542a6df12483cf838b4d99dd38522607247f` |
| `CODEX_REVIEW_COFM.md` | `56283909870c4620736c78fc35fe94e2152263742459a6fe086a5630f46e526f` |

## Exactly what may be banked

1. **CONFIRMED — norm mismatch and exact witness.** `GV55.md`, §1.3: on the stated single level-1 cc current, $N/N^{(\sigma)}=L^{\theta(k-1)}$ and $r_{k-1}=c/\kappa_{k-1}$. GF-E's printed norm bound alone does not supply the required uniform comparison.
2. **CONFIRMED — Proposition GV-E as a named-input implication.** `GV55.md`, `Proposition GV-E`: at $Z=1,m=0$, for fixed $d=4$, odd $L\ge3$, admissible fixed $\kappa_\pm$, and $0<\alpha<\theta_0<1$, the $S_E$/descended response obeys $\|x_E\|_{\mathfrak M^\nabla}\le C(\|B_k\|_D+N_\Sigma)$, uniformly in $k,T$. For every fixed $\alpha<\sigma\le1$, choose $\theta_0\le\sigma$; the exact norm comparison above supplies GV.
3. **CONFIRMED — slice identity and small-torus sign.** `GV55.md`, `1.1 The slice`: $\Gamma_E=\Lambda$, $\ker\Gamma_E=S_E$, and $\Gamma\Xi=-I$ on root-pinned gauges, also for the descended slices at $T=3,4$.
4. **CONFIRMED — corrected KOFF + GV-E contraction.** `GV55.md`, `Theorem BFT-E`, with `CODEX_REVIEW_KOFF.md`, banking item 5 and its (LA-1′)/analytic completion: on $\mathcal C_{\rm glob}$, trivial centring, $m=0,T\ge3$, bank the unique full critical point in the stated slice ball, the displayed $(2,2+\sigma,1)$ regularity estimates, and holomorphy of that point and its **composite critical value**. Constants are independent of $k,T$. Identification with $E_k^{br}$, and hence that literal branch-action version of BFT-2, remains **NOT-VERIFIED**.
5. **CONFIRMED — failure of slice preservation, with this report's replacement proof.** `GV55.md`, §3.3: bank the exact quintic witness $\Lambda^{(2)}(d\mu)=0$, $\Lambda^{(1)}(d\mu)(1)=-640/19683$. The author's rank inequality and rank proof are **REFUTED**. BA-9's direct restriction argument does not apply to $S_E$. NSL and the per-level branch identification remain **NOT-VERIFIED**; no impossibility of repairing them is claimed.
6. **CONFIRMED — Proposition GV-E_m in the explicit COFM source norms.** `GV55.md`, `Proposition GV-E_m`: conditional on the stated weighted inputs and rate condition, bank the source field bound in $N_{\Sigma,m}$ (also $N_m$) for $0\le m\le m_Y$, and the data field bound for $0\le m<m_*'$, uniformly in $k,T,X_0$. Use the bounded small-torus correction above. No DX_m/DB_m or exponentially localized global Coulomb representative is required. An unrestricted dual-norm BFT-5(b), background transfer, BFT-3/4, numerical reconstruction reach, and constructive four-dimensional Yang–Mills closure are **NOT-VERIFIED**.
