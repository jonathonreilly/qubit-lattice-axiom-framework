# NGYM — the Yang–Mills estimates needed by the combined witness

Author sprint, 2026-10-30. This file carries the argument to its conditional
endpoint; it does **not** establish the missing interacting estimates.
The stipulated uniform INDUCT bounds are accepted as named inputs, without
asserting that their unspecified source-dependent consequences hold.

Only this file is created or edited. No commits, numerical experiments,
per-lane review, audit, ledger, axiom or prompt edits are made. The numbered
steps below are the counting units. Each has exactly one sprint status.
All newly assembled implications remain author drafts, including those whose
algebra is elementary. Local source notes' older use of “PROVEN” is not the
brief's stricter “already landed, at its reviewed scope” classification.
None of the required science-note paths occurs in the identified `origin/main`
snapshot. Accordingly no step here is promoted to that classification.

## S01 — DRAFTED(high): fix the common observable, tests and target

**Consumes:** COMBO §1, WITNESS §§1,5 and the original flat Wilson law.
**Produces:** one field and one set of moment coordinates for both witnesses.
**Most likely failure point:** using a different source image or normalization
when an interacting producer is eventually supplied.

Fix \(N\ge2\), \(d=N^2-1\), odd \(L\ge3\), \(a=L^{-K}\),
\(\lambda_m=L^{-m}\), \(k=K-m\), and
\(u_i=g_{\mathrm{FLOW},i}^{-2}=2N/g_{\mathrm{std},i}^{2}\). Use

\[
 e_a(x)=\frac1{4a^4}\sum_{\mu\ne\nu}
       \sum_{p\in\operatorname{clover}_{\mu\nu}(x)}
           [1-\Re\operatorname{tr}(U_p)/N],\qquad
 \widehat e_a=e_a-\langle e_a\rangle_{K,R},\quad Z(a)=1.
\tag{1}
\]

Here \(N,L,K,m\) are integers, \(0\le m\le K\), and \(R\) ranges over
admissible physical torus sizes of the stipulated original-law family.

The scalar hierarchy is \(\mathcal A_e=\bigoplus_{n\ge0}\mathcal E_n\),
\(\mathcal E_n={}^0\mathcal S(\mathbb R^{4n})\): tests and every jet vanish
on pair-coincidence planes. No coincident product is added. Let
\(b(t)=e^{-1/(1-t^2)}\) for \(|t|<1\), zero otherwise,
\(\rho(x)=\prod_{\mu=0}^3b(x_\mu)/(\int b)^4\),
\(\epsilon=10^{-4}\), \(c_i=((2i-5)/2,0,0,0)\), and

\[
 f_i(x)=\epsilon^{-4}\rho((x-c_i)/\epsilon),\qquad
 f_{i,\lambda}(x)=\lambda^{-4}f_i(x/\lambda),\qquad
 O_i=a^4\sum_x f_{i,\lambda}(x)\widehat e_a(x).
\]

These are fixed nonnegative unit-integral bumps. Reflection exchanges
\((1,4)\) and \((2,3)\). Clover thickening preserves separation once
\(k\ge k_{\rm geom}\), for a fixed sufficiently large integer
\(k_{\rm geom}\). All source derivatives below are at zero sources.
Define, on the actual normalized Wilson law,

\[
 Q_{ij}^{K,R}(m)=\lambda_m^8\kappa_2(O_i,O_j),\quad
 V^{K,R}_m=Q_{14}^{K,R}(m),\quad Q=Q_{23}^{K,R}(m),
 \quad P^{K,R}(m)=\lambda_m^{16}\kappa_4(O_1,O_2,O_3,O_4).
\tag{2}
\]

For centered variables the unscaled fourth cumulant is
\(S_4-C_{12}C_{34}-C_{13}C_{24}-C_{14}C_{23}\). It is a polynomial in
seven separated moments, with all six pairs retained. Without centering it
is the partition polynomial in all fifteen nonempty-subset moments.
Centering changes only source-linear coefficients, hence does not change
(2). The desired endpoint, on one limiting hierarchy, is

\[
 V_m\longrightarrow0,\qquad L^{\eta m}V_m\longrightarrow+\infty
 \ (\eta>0),\qquad
 \kappa_{4,\star}>0\quad\hbox{at one fixed }m_\star.
\tag{3}
\]

The limit in cutoff/volume always precedes the limit \(m\to\infty\).
In particular the fourth witness does not move with the cutoff.

## S02 — GAP: identify the content of the assumed INDUCT package

**Consumes:** the owner's instruction to assume its uniform bounds.
**Produces:** the exact interface ledger below, not a new induction theorem.

There is no `INDUCT.md` in this folder. `INDUCT55.md` contains 33 lines of
prestated targets and failure criteria, ending without an induction hypothesis,
proved estimate or constant window. I therefore denote the owner's stipulated
package by **I-IND** and continue conditionally on it. Its assumption is not
being rejected or reopened. What cannot be verified from the source is which
of the following estimates it actually supplies:

| Interface | Required output at the consumer |
|---|---|
| I-FLOW | The actual-chain brackets (6), including finite-coupling errors, tuning, and uniform terminal lower bound. |
| I-FREE | The exact free slice decomposition, K-dec and the order-two LGF comparison used in S06–S07. |
| I-REG | The all-order, original-law test-space bound (4) and the symmetry/reflection defects needed in S03–S04. |
| I-SRC | Normalized connected source jets for the original clover, with the relative **difference** bound (12), not just a source-free or absolute upper bound. |
| I-IR, optional | The translated two-/four-point block estimate (26) for the same sequence. |

These rows are requirements for a handoff, not quotations of nonexistent
INDUCT outputs. Once I-IND supplies a row at exactly this strength its use
below is unconditional **relative to that stipulated input**. Source-free
activity contraction, bounded jets at the identity, or a fixed bare-source
radius alone cannot be substituted for I-SRC. If I-IND already contains
(12), the principal lower-matching gap is supplied by assumption rather
than proved in this file. The corresponding distinction applies to I-REG
and I-IR. No additional physical axiom is proposed.

The newer `UNIFORM_ONE_LOOP_COUPLING_ASTRA.md` supersedes FLOW's older
unclosed Gaussian coefficient frontier: its UL4 gives
\(|B_n-B_j-\beta_0(n-j)\log L|\le2C_{\rm FP}\),
\(\beta_0=11N^2/(12\pi^2)\), in its supplied model, with volume taken
first at fixed depth and momentum. Its scoped review is recorded separately.
That result expressly does not estimate the finite-\(u\) remainder, finite
torus coupling, or connected clover sources. It therefore cannot silently
fill the I-FLOW/I-SRC rows. No claim that the Gaussian coefficient remains
unresolved is inherited from the older FLOW summary.

## S03 — DRAFTED(high): E-SEQ from an explicit all-order bound

**Consumes:** I-REG in the following exact form, along a preliminary
\((K_j,R_j)\to(\infty,\infty)\) trajectory.
**Produces:** one subsequence and a continuous hierarchy containing every
test in (2), and, if needed, every finite-cube cluster test in S16.
**Most likely failure point:** I-REG being available only on selected
histories, fixed orders, or a smaller test space.

For one fixed \(s\in\mathbb N\), \(s\ge1\), \(\alpha>0\), and
\(0\le\beta<\infty\), require

\[
 |S_{n,j}(F)|\le\alpha(n!)^\beta\|F\|_{sn,1}\quad
 (n\ge1,\ F\in\mathcal E_n),\qquad
 \|F\|_{q,1}=\max_{|\gamma|\le q}\sup_X
 (1+|X|^2)^{q/2}|\partial^\gamma F(X)|.
\tag{4}
\]

For each \(n\), choose a countable dense subset of the flat Schwartz space
and include all fixed-\(m\) pairs and the fixed four-point tests. Values
on the union of these sets are bounded complex numbers. Successive
subsequence extraction and a diagonal give convergence on their countable
union. If \(F_\ell\to F\) in the Schwartz topology, (4) bounds
\(|S_{n,j}(F-F_\ell)|\) uniformly in \(j\); the triangle inequality makes
\(S_{n,j}(F)\) Cauchy and defines its unique continuous extension.
The bound (4) persists in the limit. Thus the same subsequence works for
all \(F\), not merely for each chosen coordinate on a different subsequence.

This is a distributional argument. It does not replace moment convergence
by weak convergence of random variables. An alternative probability-law
proof must supply uniform integrability at the needed orders. Fixed finite
linear combinations, reflection forms and cumulant polynomials then pass
to the limit. Integrated cluster tests at each fixed spatial cube are
also covered by the extension, when they belong to the admitted flat space.

## S04 — GAP: E-ALG and actual reconstruction

**Consumes:** I-REG and source maps from the lattice to \(\mathcal E_n\).
**Required output:** \(S_0=1\), component reality, permutations, reflection
positivity on the specified positive-time cone, full scalar E(4) covariance,
and (4), with the matching hypotheses of REC_CONT §1 and REC_LIB §18.

For example the needed continuous Euclidean recovery is, for every fixed
allowed test \(F\) and Euclidean motion \(g\),

\[
 S_{n,j}(gF)-S_{n,j}(F)\longrightarrow0,
\tag{5}
\]

together with a common continuous action and support-compatible reflection
maps. Cubic lattice covariance and boundedness alone do not imply (5).
S03 passes already established finite forms and vanishing defects; it does
not produce them. The same is true of the all-order growth constants and
the actual ordered analytic matching required for reconstruction. This is
the E-ALG gap if those items are not included in the assumed I-IND package.
The rest of the argument uses this reconstruction interface conditionally,
once, for the same \(e\) hierarchy.

## S05 — DRAFTED(high): the actual trajectory and its constant window

**Consumes:** I-FLOW, fixed nonzero admissible \(g_{\rm ref}\), and \(L\).
**Produces:** E-TR and the small-coupling parameter used by both witnesses.
**Most likely failure point:** replacing the actual finite-coupling flow by
its volume-first Gaussian coefficient.

Require the following on the very same original-law trajectory:

\[
\begin{split}
 0<U_-(m)&\le u_{K-m}\le U_+(m)<\infty,\\
 U_\pm(m)&=g_{\rm ref}^{-2}+\beta_\pm m\log L\ \pm R_F,
 \qquad0<\beta_-\le\beta_+,\quad R_F\ge0,\\
 b_-(n-j)-R_F&\le u_j-u_n\le b_+(n-j)+R_F
 \quad(0\le j\le n\le K),\qquad b_\pm=\beta_\pm\log L,\\
 u_i&\ge u_{\min}>0.
\end{split}\tag{6}
\]

Keep the terminal TR-7 lower bound required by the producer; in TSE55's
notation it includes \(u_K-R_F\ge\gamma^{-2}\). The positive lower
bracket is required only on the selected \(m\ge m_0\) domain. The two
endpoint brackets are compatible since \(U_+-U_-\ge0\), and \(U_-\)
eventually exceeds any fixed finite threshold. They give \(u_k\asymp m\)
there without requiring convergence of \(u_k\) along the cutoff sequence.

FLOW §§7–8's finite-\(u\) production still needs SF-g, RLF-delta,
continuity and tuning on the chain's own past. Its corrected remainder
has the form \(\rho_i=-\beta[\sum E_i^{\ge2}]+\delta\beta_i\), with
\(|\rho_i|\le(C_\Pi E_2+1)/u_i\) under its uniform hypotheses.
The constants and the continuation/finite-volume transfer must be in
I-FLOW to use (6). An exact numerical beta slope is unnecessary below.

## S06 — DRAFTED(high): a positive, correctly normalized free reference

**Consumes:** the Wilson/clover normalization, the free LGF kernel and the
fixed smooth tests. **Produces:** positive \(A_{ij}\), \(A_4\), and the
free pair and four-cycle coefficients.
**Most likely failure point:** an incorrect color, orientation or clover
weight in the eventual interacting source identification.

With \(\operatorname{tr}(t^at^b)=\delta_{ab}/2\) and
\(U=\exp(i\sqrt{2N}B^at^a)\), a plaquette has quadratic term
\(\tfrac12\sum_a(dB)^2\). Counting the four clover corners and both
orientations in (1) gives
\(w_i(p)=\tfrac14\sum_{x\in\operatorname{corners}(p)}f_{i,\lambda}(x)\).
The quadratic continuum reference is
\(q_u=u^{-1}\sum_{a,I=\mu<\nu}:F_I^a{}^2:\).
Differentiating \(D(z)=1/(4\pi^2|z|^2)\) twice gives the six-dimensional
curvature covariance

\[
 G(z)=\frac{J(z)}{\pi^2|z|^4},\qquad
 J(z)=\Lambda^2(I-2zz^T/|z|^2),\qquad J(z)^TJ(z)=I.
\]

Consequently \(\kappa_2^q(x,y)=12d/(\pi^4u^2|x-y|^8)\).
A connected Wick pairing of four quadratic insertions is a cycle. Each
of its four vertices assigns two legs to its two neighbors in two ways;
there are three undirected cycles, each with factor \(16\) and one color
loop \(d\). Thus set

\[
\begin{split}
 A_{ij}&=\frac{12d}{\pi^4}\int f_i(x)f_j(y)|x-y|^{-8}\,dx\,dy>0,\\
 A_4&=\frac{d}{\pi^8}A,\qquad
 A=16\int\prod_{r=1}^4[f_r(x_r)\,dx_r]
       \sum_{c=1234,1243,1324}\operatorname{tr}
                \prod_{ij\in c}\frac{J(x_i-x_j)}{|x_i-x_j|^4},\\
 A_2&=A_{23},\qquad R_0=A_4/A_2^2.
\end{split}\tag{7}
\]

Here the integrals are finite by support separation. At the centers
\(J_0=\operatorname{diag}(-1,-1,-1,1,1,1)\), and
\(96(1/81+1/256+1/20736)=169/108\). This is **not** the smeared value.
For every edge with center length \(\ell\in\{1,2,3\}\), the support
displacement is at most \(1/2500\). The scalar radial factor differs
from one by less than \(1/500\), while
\(\|J(z)-J_0\|\le8/4999<1/600\). Hence
\(\|\ell^4\pi^2G(z)-J_0\|<1/250\). Four-factor telescoping gives a
trace error less than \(6/60\) per normalized cycle. Integrating the
positive center weights yields

\[
 \frac{9971}{6480}<A<\frac{10309}{6480},\qquad
 \frac32<A<\frac53,\quad
 11<B_0:=\pi^4A_2/d<13,\quad R_0>\frac3{338d}.
\tag{8}
\]

The \(B_0\) bounds follow directly from
\(12(2500/2501)^8<12|x-y|^{-8}<12(2500/2499)^8\) on its supports.
Thus the smooth free coefficients really are positive. The two-point
coefficient for AF is \(A_{14}\), not \(A_2\).

LGF (37)–(41) supplies, for the counting mean-zero torus inverse,
\(G^F=d_{\rm lat}\Delta_1^{-1}d_{\rm lat}^*\) and curvature error
\(O(r^{-5})+O(T^{-4})\), \(1\le r\le T/4\), \(T=R/a\).
Rescaled on our supports this is
\(O(L^{-k})+O((\lambda/R)^4)\). Orders zero and one instead have
torus errors \(T^{-2}\) and \(T^{-3}\). No interacting estimate is
obtained by relabeling this free kernel.

## S07 — DRAFTED(high): PL-1L implies E-TS, with the terminal term

**Consumes:** I-FREE, (6), and the following additional PL-1L estimate.
**Produces:** E-TS for the AF pair with \(\kappa=\kappa'=2\).
**Most likely failure point:** absence of a normalized, original-law
producer for PL-1L, which is part of S09's matching gap.

Put \(G_i=\mathbb E[O_4\mid U_i]\), \(H_i=\mathbb E[O_1\mid U_i]\)
on the actual normalized chain. Conditional covariance gives exactly

\[
 V_m^{K,R}=\sum_{i=0}^KD_i,\quad
 D_i=\lambda^8\mathbb E\operatorname{Cov}(G_i,H_i\mid U_{i+1})\ (i<K),
 \quad D_K=\lambda^8\operatorname{Cov}(G_K,H_K).
\]

For coupling-one free curvature slices \(\mathcal K_i\), require
\(\sum_i\mathcal K_i=G^F\), K-dec
\(|\mathcal K_i(p,q)|\le M L^{-4i}e^{-\mu|x_p-x_q|_1/L^i}\)
for \(i<K\), and \(|\mathcal K_K|\le ML^{-4K}\). Set
\(a_i=\mathcal K_i/u_i\), \(G_{\rm run}=\sum_i a_i\), and

\[
 \Lambda_i=\lambda^8d\sum_{p,q}w_4(p)w_1(q)
             [4a_i(p,q)\sum_{j>i}a_j(p,q)+2a_i(p,q)^2].
\]

Expansion of the square shows
\(\sum_i\Lambda_i=2\lambda^8d\sum w_4w_1G_{\rm run}^2\).
The terminal cross sum is empty. Individual slices have no required sign.
The stronger producer and its sufficient summed consequence are

\[
\begin{split}
 |D_i-\Lambda_i|&\le E_2u_{\max(i,k)}^{-2-\theta_2}p_{i,2}(k),
                  \qquad \theta_2>0,\\
 p_{i,2}(k)&=
 \begin{cases}L^{4(k-i)}e^{-\mu_2D_-L^{k-i}},&i<k,\\
 L^{-8(i-k)},&i\ge k,\end{cases}\\
 \left|\sum_i(D_i-\Lambda_i)\right|&\le C_{{\rm err},2}u_k^{-2-\theta_2}.
\end{split}\tag{9}
\]

Here \(D_-=\min_{r\ne s}\operatorname{dist}_1
(\operatorname{supp}f_r,\operatorname{supp}f_s)>0\),
\(0<M<\infty\), \(\mu>0\), \(0<\mu_2\le\mu/2\), and the error
constants are finite and nonnegative. Reducing the common decay constant
and enlarging the error constant permits a finite union of test pairs.

The fine weights are summable. For coarse \(i=k+n\), (6) gives
\(u_i\ge u_k/2\) until \(b_+n+R_F\le u_k/2\). Past that point use
\(u_{\min}\); \(L^{-8n}\) beats every fixed inverse power of \(u_k\).
This proves the summation implication, with constants independent of
\(K,R,m\). Similarly
\(|u_i^{-1}-u_k^{-1}|\le(b_+|i-k|+R_F)/(u_i u_k)\)
and K-dec give a cross-kernel error
\(C_1L^{-4k}u_k^{-2}\); two-factor telescoping gives bubble error
\(C_{{\rm AF},14}u_k^{-3}\).

Choose geometry/depth/volume thresholds so the coupling-one bubble lies
in \([A_{14}/2,3A_{14}/2]\). Then require, uniformly using \(U_-(m)\),
\(C_{{\rm AF},14}/u_k\le A_{14}/8\) and
\(C_{{\rm err},2}/u_k^{\theta_2}\le A_{14}/8\). Triangle inequality gives

\[
 \frac{A_{14}}{4u_k^2}\le V_m^{K,R}\le\frac{7A_{14}}{4u_k^2}.
\tag{10}
\]

This is the requested sufficient PL-1L-to-E-TS implication. Reflection
positivity alone gives no magnitude lower bound. PL-1L for pair \((1,4)\)
alone supplies neither pair \((2,3)\) nor the other four pairs.

## S08 — DRAFTED(high): one source system and one matching estimate

**Consumes:** the exact normalized Wilson source tilt and free reference.
**Produces:** a single two-/four-source difference estimate whose consequences
are evaluated in S10. **Most likely failure point:** dropping mixed
conditional terms, source normalizers, or triples during RG propagation.

Use the finite ring \(\mathbb C[t_1,t_2,t_3,t_4]/(t_1^2,\ldots,t_4^2)\).
With \(Y_i=u_k\lambda^4O_i\), define the finite source jet

\[
 \mathscr L=\log\mathbb E\prod_i(1+t_iY_i),\qquad
 [t_B]\mathscr L=u_k^{|B|}\lambda^{4|B|}\kappa(O_i:i\in B).
\tag{11}
\]

The logarithm is a finite polynomial because its argument has constant
term one and its remaining part is nilpotent.
The scaling of \(Y_i\) is bookkeeping; the physical field is still (1).
No coincident continuum moment or uniform full moment-generating function
is assumed. Let \(\mathscr L_{\rm run}\) use the same clover quadratic
weights and covariance \(G_{\rm run}\). Equivalently its finite-lattice
coefficients come from \(-\tfrac d2\operatorname{Tr}\log
(I-2u_k\lambda^4G_{\rm run}\sum_i t_iW_i)\), with source-linear
centering. This is a finite coefficient identity, not a continuum determinant.

Set \(\mathcal B=\{\{i,j\}:i<j\}\cup\{\{1,2,3,4\}\}\), with
\(A_B=A_{ij}\) for a pair and \(A_B=A_4\) for the quadruple. Define the
coefficient **seminorm**
\(\|F\|_{2,4}=\max_{B\in\mathcal B}|[t_B]F|/A_B\).
The single sufficient interacting estimate is

\[
 \boxed{\quad
 \|\mathscr L_{K,R}(m)-\mathscr L_{{\rm run},K,R}(m)\|_{2,4}
       \le C_{\rm src}\,u_k^{-\theta},\qquad \theta>0.
 \quad}\tag{12}
\]

It is uniform on one domain \(m\ge m_0\), \(k\ge k_0\),
\(R/\lambda_m\ge t_0\), with constants independent of all three
indices. S09 records its unproved producer. It is a joint lower-matching
requirement after comparison, not a deduction from upper bounds.

The actual uncentered source tilt is
\(u_0(p)\mapsto u_0-h_t(p)\), where
\(h_t(p)=\tfrac12u_k\lambda^4\sum_{x\in\operatorname{corners}(p)}
\sum_i t_if_{i,\lambda}(x)\). All chain kernels and their field-dependent
normalizers are kept fixed when differentiating; the coupling is not retuned
as a function of sources. Subtract the deterministic linear term for
centering. If \(\Phi_i=\log\mathbb E[e^{\sum t_rY_r}\mid U_i]\), its
distinct-subset jets satisfy exactly

\[
 J_{i+1,B}=\sum_{\pi\in\mathcal P(B)}
       \kappa_{|\pi|}(J_{i,C}:C\in\pi\mid U_{i+1}).
\tag{13}
\]

This follows by expanding \(\log\mathbb E\exp\Phi_i\) in the finite
ring: the \(|\pi|!\) orders cancel the factorial in the outer cumulant
expansion. All fifteen nonempty subsets, including triples, are propagated.

For clarity the fourth increment of the cumulant of first conditional
images \(X_r=\mathbb E[O_r\mid U_i]\), conditional on \(U_{i+1}\), is

\[
 D_{i,4}/\lambda^{16}
 =\mathbb Ec_{1234}
 +\sum_{4}\operatorname{Cov}(c_{abc},\mu_d)
 +\sum_{3}\operatorname{Cov}(c_{ab},c_{cd})
 +\sum_{6}\kappa_3(c_{ab},\mu_c,\mu_d),
\tag{14}
\]

where \(c_B=\kappa(X_r:r\in B\mid U_{i+1})\) and
\(\mu_r=\mathbb E[X_r\mid U_{i+1}]\). These are fourteen terms;
the fifteenth partition is the subtracted outer fourth cumulant of the
means. Add \(D_{K,4}=\lambda^{16}\kappa_4(G_K^1,\ldots,G_K^4)\).
Neither (14) nor its terminal term can be replaced by one conditional
fourth cumulant. The jets in (13) and the conditional \(c_B\) in (14)
are different objects.

An optional sufficient analytic implementation of (12) is, for every
\(B\in\mathcal B\), a zero-free holomorphic log branch on fixed relative
source radii \(\rho_i>0\). Write
\(\mathcal W(t)=\log\mathbb E\exp(\sum_i t_iY_i)\), and use
\(\mathcal W_{\rm run}\) for the reference. The sufficient bound is

\[
 \max_{B\in\mathcal B}\frac{
    \sup_{|t_i|<\rho_i,\,i\in B}|\Pi_B(\mathcal W-\mathcal W_{\rm run})(t)|}
    {A_B\prod_{i\in B}\rho_i}
 \le C_{\rm src}u_k^{-\theta},\qquad
 \Pi_BH=\sum_{J\subseteq B}(-1)^{|B|-|J|}H(t_J).
\tag{15}
\]

Only variables in \(J\) are active in \(t_J\). Cauchy's formula, once
in each variable, proves (12) with no \(|B|!\). Proper-subset terms are
removed, but the interaction meeting all indicated supports remains.
A controlled finite jet also suffices; (15) is not necessary. A fixed
absolute bare-source radius may become a radius of order \(1/u_k\) in
these variables and lose the required gain. The full log trace need not
have a uniform bound even when its projected difference does.

## S09 — GAP: the original-law producer of (12), including PL-1L

**Consumes:** I-IND's actual source/large-field estimates, once specified.
**Required output:** (12), or summed PL-1L for the needed pairs and PL-4C
for the quadruple, with common domains, normalization and coupling.

The four-point summed form is
\(|P-P_{\rm run}|\le C_4u_k^{-4-\theta_4}\).
A stronger sufficient per-step form from K4MATCH is
\(|D_{i,4}-\Lambda_{i,4}|\le E_4u_{\max(i,k)}^{-4-\theta_4}p_{i,4}(k)\),
where the fine weight has the form in (9), with a possibly reduced common
positive decay constant, and the coarse weight is
\(L^{-16(i-k)}\). Here
\(\Lambda_{i,4}=F_4(H_i)-F_4(H_{i+1})\),
\(H_i=\sum_{j\ge i}\mathcal K_j/u_j\), \(H_{K+1}=0\), and
\(F_4(H)=16d\lambda^{16}\sum_c\operatorname{Tr}
(W_{c_1}HW_{c_2}HW_{c_3}HW_{c_4}H)\).
Telescoping retains all mixed-slice cycles and the terminal contribution.
The same near/far summation as S07 proves the summed implication, but
does not establish the interacting per-step estimate.

The missing source work must control: the leading image coefficient tending
to **one**, background and coarse covariance, coupling identification with
the same \(u_i\), normalized source recursion, and all source insertions
on returned/failed/large-field histories. At the jet level the latter
requires a summed bound on their contribution to each coefficient in (12),
after all denominator derivatives and connected subtractions. Small
probabilities without inserted moment estimates do not give it.

The obstruction to the obvious upper-bound shortcut is explicit. The laws
\(p_t(x)=2^{-4}(1+t x_1x_2x_3x_4)\) on \(\{\pm1\}^4\),
\(|t|\le1\), have identical proper-subset moments and uniformly bounded
all-order moments, but their distinct fourth cumulant is \(t\).
Conditional centered Gaussians of random variance similarly have zero
conditional fourth cumulant but a nonzero outer one, from the \(2+2\)
terms in (14). These are information counterexamples, not YM models.
They explain why a two-source theorem or an absolute four-source upper
bound leaves the leading fourth coefficient undetermined.

F17 estimates a first moment of a spatially flowed bare **magnetic**
observable on its own marked algebra. Its nonnegative history partition
does not transfer to the signed connected \(e\) source jets, does not give
their second/fourth insertion bounds, and supplies no CL2 estimate.
No such transfer is used here. This remains a live derivation problem,
not a theorem that lower matching is impossible.

## S10 — DRAFTED(high): the single resulting YM estimate and compatible windows

**Consumes:** (12), I-FREE, (6) and the fixed tests.
**Produces:** E-TS and C-4MATCH/C-2MATCH simultaneously, with one window.
**Most likely failure point:** constants or source radii depending on the
cutoff in the missing producer of (12).

K-dec and (6) give on each cross-support edge
\(|G_{\rm run}-G^F/u_k|\le C_1L^{-4k}u_k^{-2}\),
\(|G^F|\le C_0L^{-4k}\). Two-factor telescoping costs \(u_k^{-3}\)
for a pair. Four-factor telescoping costs \(u_k^{-5}\); for example
K4MATCH's normalization permits
\(C_{{\rm AF},4}=192d\,12^4C_1(C_0+C_1)^3\), once
\(\sum_pw_i(p)\le12a^{-4}\). The identity
\(\lambda^{16}a^{-16}L^{-16k}=1\) cancels the scaling factors.
LGF and the separated Riemann sums add
\(u_k^{-|B|}O(L^{-k}+(\lambda/R)^4)\).
Take finite maxima over the six pairs and quadruple after division by
their positive coefficients (7). Thus

\[
\boxed{\begin{split}
 \max\left\{\max_{i<j}\left|\frac{u_k^2Q_{ij}^{K,R}(m)}{A_{ij}}-1\right|,
               \left|\frac{u_k^4P^{K,R}(m)}{A_4}-1\right|\right\}
 &\le\varepsilon_{K,R}(m),\\
 \varepsilon_{K,R}(m)
 &= C_{\rm src}u_k^{-\theta}+C_{\rm run}u_k^{-1}
       +C_{\rm lat}L^{-k}+C_{\rm vol}(\lambda_m/R)^4.
\end{split}}\tag{16}
\]

All four constants are named nonnegative finite bounds, not assigned
numerical values. The free constants depend on the fixed bumps, \(N,L\)
and I-FREE/I-FLOW constants; \(C_{\rm src}\) is the unproved interacting
constant. Formula (16) is conditional on (12), not an achieved YM estimate.

There is no incompatible constant window **if** those constants are
uniform. Choose in this order:

| Choice | Required inequalities |
|---|---|
| \(m_0\) | \(U_-(m_0)\) meets every coupling threshold, and \(C_{\rm src}U_-(m_0)^{-\theta}+C_{\rm run}U_-(m_0)^{-1}\le1/8\). |
| \(k_0\) | All clover/LGF/source depth thresholds and \(C_{\rm lat}L^{-k_0}\le1/16\). |
| \(t_0\) | All torus geometry thresholds and \(C_{\rm vol}t_0^{-4}\le1/16\). |
| \(R_{\min}\) | All producer volume thresholds and \(R_{\min}\ge t_0\lambda_{m_0}\). |

Since \(U_-\) increases without bound, \(L^{-k}\to0\), and \(t^{-4}\to0\),
these choices exist without changing \(g_{\rm ref}\). For \(m\ge m_0\),
\(K\ge m+k_0\), \(R\ge R_{\min}\), one has
\(R/\lambda_m\ge t_0\) and \(\varepsilon\le1/4\). In particular

\[
 \frac{3A_{ij}}{4u_k^2}\le Q_{ij}^{K,R}(m)\le\frac{5A_{ij}}{4u_k^2},
 \qquad \frac{3A_4}{4u_k^4}\le P^{K,R}(m)\le\frac{5A_4}{4u_k^4}.
\tag{17}
\]

This supplies the required \(E\)-TS exponents \(2,2\). Also
\(12/25\le(P/Q^2)/R_0\le20/9\). More precisely, with
\(|\delta_n|\le\varepsilon_n<1\),
\[
 \left|\frac{(P/Q^2)}{R_0}-1\right|
 \le\frac{\varepsilon_4+2\varepsilon_2+\varepsilon_2^2}
           {(1-\varepsilon_2)^2}.
\tag{18}
\]
First taking the fixed-\(m\) cutoff/volume limit, then \(m\to\infty\),
makes this relative error vanish. No separate retuning or reconstruction
is needed for the two conjuncts.

## S11 — DRAFTED(high): shared renormalization and the complete first correction

**Consumes:** K4CORR's explicitly conditional one-coupling Ward/insertion
identities, with a fully specified regulator and local operator matching.
**Produces:** cancellation identities and the actual coefficient that must
be enclosed; no enclosure is inferred. **Most likely failure point:**
identifying the renormalized coupling insertion with the unchanged clover.

Write \(h=u^{-1/2}\), \(\beta_h=-b_0h^3-b_1h^5+\cdots\), and assume
\(e_R=2\partial\mathcal L_R/\partial u\), the scale Ward identity, and
vanishing of EOM/BRST-exact terms on these separated physical insertions.
For \(D=\mu\partial_\mu+\beta_u\partial_u\),
\([D,\partial_u]=-\beta_u'\partial_u\). In the convention
\(De_R=-\gamma_e e_R\), this gives

\[
 \gamma_e=\beta_u'(u)=\beta_h'(h)-3\beta_h(h)/h
       =-2b_1h^4+O_{\rm formal}(h^6),\qquad
 H(h)=-\frac{\beta_h(h)}{b_0h^3}=1+\frac{b_1}{b_0}h^2+\cdots,
 \quad D(H e_R)=0.
\tag{19}
\]

Thus the absence of a local order-\(h^2\) anomalous term does not remove
the integrated order-\(h^2\) operator factor. A common multiplicative
source-image factor \(F\) gives \(P\mapsto F^4P\), \(Q\mapsto F^2Q\).
It cancels in \(P/Q^2\) exactly. It does not fix the absolute size of
either moment, remove nonmultiplicative mixing, or authorize changing
\(Z(a)=1\). A factor tending to zero could preserve the ratio while
destroying a fixed-scale cumulant margin. A uniform two-sided bound on
the actual image factor would suffice for the qualitative witness with
adjusted constants; (12)/(16) demand the stronger unit leading matching.

With \(\ell=\log(\mu\lambda)\), the formal separated RG equation yields

\[
\begin{split}
 P_R&=A_4h^8[1+h^2(a_4+8b_0\ell)+O_{\rm formal}(h^4)],\\
 Q_R&=A_2h^4[1+h^2(a_2+4b_0\ell)+O_{\rm formal}(h^4)],\\
 (P_R/Q_R^2)/R_0&=1+c h^2+O_{\rm formal}(h^4),\qquad c=a_4-2a_2.
\end{split}\tag{20}
\]

Indeed \(D h^{2n}=-2nb_0h^{2n+2}+\cdots\), forcing the displayed
log coefficients; their ratio combination is zero. For
\(F=1+zh^2+\cdots\), \(a_4\) changes by \(4z\), \(a_2\) by \(2z\),
so \(c\) is unchanged. Finite shape/cross-ratio/bump-width contributions
remain in \(c\). Even-power formal remainders require the full
field/coupling-reversal symmetry of the regulator and counterterms;
without it the displayed first coefficient still makes sense, but the
formal next order need not be \(h^4\). No formal remainder is used as a
quantitative estimate.

For completeness the complete order-\(h^2\) coefficient has five families.
At \(\lambda=1\), put \(s=\sqrt{2N}\),
\(F_{0,\mu\nu}^a=\partial_\mu A_\nu^a-\partial_\nu A_\mu^a\),
\(C_{\mu\nu}^a=f^{abc}A_\mu^bA_\nu^c\), with ordered tensor sums, and

\[
\begin{aligned}
 X_{r,0}&=\tfrac12\int f_r F_0^2,&
 X_{r,1}&=s\int f_r F_0 C,&
 X_{r,2}&=\tfrac{s^2}{2}\int f_r C^2+X_{{\rm ct},r,2},\\
 V_1&=\tfrac s2\int F_0C
       +s\int f^{abc}(\partial_\mu\bar c^a)A_\mu^b c^c,&
 V_2&=\tfrac{s^2}{4}\int C^2+S_{{\rm ct},2}.
\end{aligned}
\]

For \(I=\{2,3\}\) or \(I=\{1,2,3,4\}\), \(n=|I|\), define

\[
\begin{split}
 \mathcal D_n={}&\sum_{r\in I}\kappa_0(X_{r,2},X_{s,0}:s\ne r)\\
 &+\sum_{r<s}\kappa_0(X_{r,1},X_{s,1},X_{t,0}:t\ne r,s)\\
 &-\sum_r\kappa_0(X_{r,1},X_{s,0}:s\ne r,V_1)\\
 &-\kappa_0(X_{r,0}:r\in I,V_2)
    +\tfrac12\kappa_0(X_{r,0}:r\in I,V_1,V_1),\\
 c={}&\mathcal D_4/A_4-2\mathcal D_2/A_2.
\end{split}\tag{21}
\]

To verify the signs/factors, tilt the Gaussian by \(\sum t_rX_{r,0}\).
The coefficient of \(h^2\) in the normalized logarithm is
\(\langle\sum t_rX_{r,2}-V_2\rangle_t+
\tfrac12\kappa_t(\sum t_rX_{r,1}-V_1,\sum t_rX_{r,1}-V_1)\),
minus its value at zero sources. Distinct differentiation gives (21).
Ghosts use Grassmann signs. Original Wilson matching must also account
for Haar/discretization terms and finite source counterterms; renaming
continuum \(V_2\) does not supply them. The algebra fixes what must be
computed, not its sign, size or regulator-independent existence.

## S12 — GAP: the renormalized coefficient and full-law correction route

**Consumes:** the five families (21), a regulator/subtraction/matching
scheme, and the original Wilson normalization. **Required output:** a
finite uniform \(\bar C\ge|c|\), and the original-law remainder in S13.
This is an **alternative producer** of the fourth lower bound, not an
extra necessary conjunct when (12) is already available.

K4CORR2 supplies finite bounds on specified external-only and four-support
star subfamilies. Its honest remainder split is
\(c=c_{\rm fin}+c_{\rm rem}\),
\(|c_{\rm fin}|\le C_{\rm safe}\), with \(C_{\rm rem}\) still absent.
It also bounds every **bare regulated** family using a heat UV cutoff
\(\delta\) and interaction box volume \(V=(2R)^4\). For order \(n\),
the three types of majorants grow as
\(\delta^{-4n}\), \(V\delta^{-4n-4}\), and
\(V^2\delta^{-4n-8}\). In particular its positive polynomial
\(M_4(\delta,R)\) obeys
\(M_4(\delta/2,R)\ge2^{16}M_4(\delta,R)\).
Its resulting formal non-cancellation window shrinks to zero. This is a
failure of that majorant to uniformize, not evidence that renormalized
\(c\) diverges.

External separation leaves bulk-bulk, bulk-insertion and nested collision
regions. For instance \(D_\delta(0)=1/(16\pi^2\delta^2)\) and a quartic
insertion contraction leaves a quadratic tadpole; centering only removes
the scalar part. Also \(|\nabla D(z)|^2=1/(4\pi^4|z|^6)\) has a
nonintegrable absolute bulk-collision integral. A local Taylor subtraction
of degree \(q\le2\) gives the legitimate estimate

\[
 \int_{|z|<r}\frac{|\phi(z)-T_q\phi(z)|}{|z|^{4+q}}\,dz
 \le \frac{32\,2^{q+1}}{(q+1)!}\,r
       \max_{|\alpha|=q+1}\|\partial^\alpha\phi\|_{\infty,B_r},
\tag{22}
\]

but the remaining derivative bound is not uniform on overlapping
collision regions. A compatible forest/sector construction, gauge/ghost
identities, finite matching terms and an IR limit are still needed for
the complete (21). Neither a single subtraction nor a finite first
coefficient bounds the original-law higher-order remainder.
This file does not fabricate \(\bar C\), a positive actual-YM coupling
window, or an instanton suppression constant.

## S13 — DRAFTED(high): the corrected lower bound if that alternative closes

**Consumes:** \(|c|\le\bar C<\infty\), (6), Q-LOW and K4RATIO-REM in
the exact following form. **Produces:** a nonzero unnormalized fourth
cumulant at fixed scale. **Most likely failure point:** either uniform
remainder control or absolute denominator matching being missing.

Write \(x=1/u_k\), \(\mathcal R=P/Q^2\). On the same law require,
for \(0<x\le\min(x_0,1)\),

\[
 \left|\frac{\mathcal R}{R_0}-1-cx\right|
 \le Hx^2[1+\log(1/x)]+Je^{-S/x}+\eta_{K,R}(m),\qquad
 \left|\frac{Q}{A_2x^2}-1\right|\le\tfrac12,
\tag{23}
\]

where \(H,J\ge0\), \(S,x_0>0\) are uniform and
\(\eta_{K_j,R_j}(m)\to0\) for every fixed \(m\). The exponential form
is merely one sufficient proposed bound; no nonperturbative action is
asserted known. The second estimate is independent information about
absolute normalization that a ratio cannot provide.

For \(x\le1/2\), \(\log(1/x)\le1/x\) and
\(e^{S/x}\ge S^2/(2x^2)\) imply that the two explicit remainder terms
are at most \(Tx\), \(T=3H/2+J/S^2\). Therefore the common window

\[
 x<\min\{x_0,\tfrac12,[2\max(1,\bar C)]^{-1},
                         [8\max(1,T)]^{-1}\},\qquad \eta\le\tfrac18
\]

gives \(|cx|<1/2\), remainder at most \(1/4\), and

\[
 \mathcal R/R_0>1/4,\qquad P>A_4x^4/16,\qquad
 \kappa_{4}^{K,R}(m_\star)>
 \frac{A_4}{16\lambda_\star^{16}U_+(m_\star)^4}.
\tag{24}
\]

Choose \(m_\star\) using \(U_-\to\infty\), keep it fixed, and only
then take a tail making \(\eta\le1/8\). The limiting strict inequality
may become non-strict, but its right side is a fixed positive number.
This proves the required witness margin conditionally. The ratio need
not be defined or continuous at the zero field; the limiting witness is
the cumulant polynomial. S07 supplies AF independently if using this route
instead of (12).

For the optional isolated-correction rate, require FLOW's additional
F-ll/F-tune inputs with fixed terminal \(U=u_K>R_F\),
\(B=2b_0>0\), and \(b_*=B\log L\). Their required envelope is
\(|u-b_*m|\le E_m\), where

\[
 E_m=U+R_F+\frac{C_\rho}{U-R_F}
      +\frac{C_\rho}{b_-}\log\left(1+\frac{b_-m}{U-R_F}\right),
 \qquad U>R_F.
\]

If \(E_m\le b_*m/2\), then
\(|c/u-c/(b_*m)|\le2\bar C E_m/(b_*m)^2\). This yields the isolated
\(c/[B\log(1/\lambda)]\) term with a
\(\log\log(1/\lambda)/\log^2(1/\lambda)\) error under those inputs.
It is not a full-ratio asymptotic without (23), and is not needed for (3).

## S14 — DRAFTED(high): pass both witnesses to the same limiting state

**Consumes:** E-ALG, S03, (6), and either (16) or the S07+S13 alternative.
**Produces:** (3) and its field-preserving reconstructed meaning.
**Most likely failure point:** an exchange of the fixed-scale continuum
limit with the short-distance limit, or absent reconstruction matching.

On the (16) route, for every fixed \(m\ge m_0\) all sufficiently late
members of the **same** sequence satisfy (17). Pass the moment coordinates
to their limits using S03. Thus

\[
 \frac{3A_{14}}{4U_+(m)^2}\le V_m\le
 \frac{5A_{14}}{4U_-(m)^2},\qquad
 \kappa_{4,\star}\ge
 \frac{3A_4}{4\lambda_\star^{16}U_+(m_\star)^4}>0.
\tag{25}
\]

The upper bound tends to zero. The lower bound multiplied by
\(L^{\eta m}\) tends to infinity for every \(\eta>0\), since an
exponential dominates a fixed polynomial in \(m\). These are all
countably many \(m\)'s in one state, not a new subsequence per \(m\).
Take any fixed \(m_\star\ge m_0\) for the fourth witness.
On the alternative route use (10) and the positive margin (24) instead;
the same argument applies with their stated constants.

For the reconstruction step, require the actual E-ALG matching in S04.
Continue each partition term of the fourth cumulant to its ordered
forward tube. Subtuple gaps are sums of future-cone gaps; different blocks
use disjoint variable slots. Their boundary products are tensor products,
not coincident distribution products. If the reconstructed named field
were Gaussian, its Wick cumulant boundary would vanish. Boundary
uniqueness and the ordered Euclidean matching then force the Euclidean
cumulant to vanish, contradicting (25). A vacuum-, field- and
spacetime-preserving equivalence preserves the same separated data.
No statement about an unmarked ambient net follows by forgetting these
identifications. No new reconstruction is performed for the ratio.

## S15 — DRAFTED(high): exactly which Gaussian and Wick classes are excluded

**Consumes:** (3), E-ALG and the specified comparator definitions.
**Produces:** exclusion of the literal COMBO union, with a limited mixture
extension. **Most likely failure point:** widening “finite canonical” to
arbitrary spectral measures or interpreting a composite as Gaussian on \(e\).

Let F1 consist of scalar Hermitian finite Wick polynomials, with finitely
many derivatives, in finitely many canonical free fields of fixed finite
masses/spins, whose propagators are finite matrix differential polynomials
in mass-shell scalar propagators. Arbitrary coefficients and finite tensor
products are allowed. Let F2 be elementary generalized-free hierarchies
on the named generators, and F3 all Gaussian/quasi-free hierarchies on
those generators, allowing means and degenerate covariance. Here F2 is
contained in F3. These are assignments of the named field and vacuum.

For F1 the scalar propagator heat representation is
\(G_s(r)=(16\pi^2)^{-1}\int_0^\infty t^{-2}e^{-r^2/(4t)-st}\,dt\).
For positive mass write \(G_{m^2}=Y(mr)/(4\pi^2r^2)\); its equation is
\(z^2Y''-zY'-z^2Y=0\). The series
\(Y=a_0+\sum_{n\ge1}(a_n+b_n\log z)z^{2n}\) has
\(b_1=a_0/2\), \(4n(n-1)b_n=b_{n-1}\), and
\(4n(n-1)a_n+(4n-2)b_n=a_{n-1}\) for \(n\ge2\).
Factorial denominators give convergence with finite derivatives away
from zero; its two free constants span the solutions. Finite derivatives
and Wick products consequently have a convergent integer-power series
with bounded nonnegative log degree. After cancellations a nonnull
centered scalar F1 covariance has leading term
\(c r^{-\gamma}|\log r|^j\), integer \(\gamma\), integer \(j\ge0\).
Scalar covariance gives radiality and reflected-point positivity fixes
\(c>0\). If every series coefficient vanishes the separated covariance
is null and already fails (3).

Smearing on the fixed disjoint positive tests preserves that leading
power and sign. If \(\gamma\ge8\), \(V_m\) cannot tend to zero; if
\(\gamma\le7\), \(L^{m/2}V_m\to0\), contradicting (3). Thus AF-e
excludes F1. It is this ultraviolet property, **not** the fourth cumulant,
that excludes canonical free composites.

For a Gaussian assignment use the square-free ring again. Its subset
moment polynomial is
\(\exp(\sum_i\mu_it_i+\sum_{i<j}C_{ij}t_it_j)\). Its logarithm
has degree at most two, so every distinct fourth cumulant vanishes.
This proves that the second part of (3) excludes all F2/F3, irrespective
of spectral density, means or degeneracy. Hence the conditional state
lies outside **F1 union F2 union F3**.

AF alone also excludes finite canonical mixtures, or the common-envelope
canonical mixtures specified in COMBO: assume finite component-mean
variance and \(0\le C_t(r)\le D r^{-\gamma_t}|\log r|^J\) with common
\(D,J,r_0\). The mixed covariance is
\(\int C_t\,d\nu+\operatorname{Var}_\nu\mu_t\). Fatou and positivity
exclude components with \(\gamma_t\ge8\) if \(V_m\to0\). The envelope
then bounds the remaining covariance by
\(O(\lambda_m^{-7}|\log\lambda_m|^J)+O(1)\), contradicting the lower
AF clause. Without that envelope this argument does not interchange
ultraviolet asymptotics and an arbitrary mixture. S17 supplies a different
extension when clustering is assumed.

## S16 — GAP: the actual infrared estimate for mixture clustering

**Consumes:** the same hierarchy and common sequence, with no new field.
**Required output:** CL2, or the following original-law sufficient producer.

Let \(P_0\) range over a countable dense determining family of complex
compact positive-time words of degree one or degree two, the latter with
strictly ordered disjoint time supports. Include rational complex linear
combinations within each degree. With reflected conjugation \(\Theta\),
spatial translation \(\tau_b\) and \(B_A=[-A,A]^3\), require convergence
of the fixed-\(A\) integrated moments and

\[
 \limsup_{j\to\infty}\left|
 \frac1{|B_A|}\int_{B_A}
   [S_j(\Theta P_0\,\tau_bP_0)-|S_j(P_0)|^2]\,db\right|
 \le\delta_{P_0}(A),\qquad \delta_{P_0}(A)\longrightarrow0.
\tag{26}
\]

The envelopes \(\delta_{P_0}(A)\) are nonnegative and finite.

Here \(A\) is a spatial averaging radius, distinct from the torus radius
\(R_j\) and from coefficient \(A\) in (7). First \(j\to\infty\) at
fixed \(A\), then \(A\to\infty\). Reflection keeps the two blocks in
opposite half-spaces for every spatial translation, so these are separated
two-/four-point tests on the existing hierarchy. This is precisely CL2
after passage to the limit.

For factorizable centered degree-two words the block covariance is the separated
\(\kappa_4\) plus the two **cross-block** pair products; the within-block
pair product cancels; integrate and polarize for general degree-two tests.
Thus elementary two-point clustering alone cannot
control (26). A sufficient stronger bound would dominate this whole block
covariance by a bounded function of \(b\) whose Cesaro average vanishes,
uniformly after the fixed-\(A\) continuum limit. Neither (16), which
uses a fixed ultraviolet geometry, nor F17's magnetic first-moment bound
provides it. An I-IND estimate valid only locally or at fixed scale has
no such implication. If I-IR is supplied by the stipulated package, (26)
can instead be read as that named input. No mass-gap or quantitative
exponential decay is needed; none is inferred.

## S17 — DRAFTED(high): CL2 removes admissible invariant Gaussian/canonical mixtures

**Consumes:** E-ALG, (3), (26), and an admissible invariant barycenter.
**Produces:** exclusion of arbitrary admissible probability mixtures of
F1 and invariant affine Gaussian hierarchies, without an ENV assumption.
**Most likely failure point:** applying this to non-invariant components
or to mixtures without the needed moment integrability.

Suppose \(S=\int S_t\,d\nu(t)\). Each component is an individually
Euclidean-invariant normalized hierarchy on the same algebra, with its own
OS construction. Moment evaluations are measurable and integrable, and
\(\int S_t(\Theta P_0P_0)d\nu<\infty\). The barycenter has E-ALG.
Let \(v_t=[P_0]_t\), \(U_t(b)\) the strongly continuous spatial unitary
group, and \(E_t\) its invariant projection. The cube average of \(U_t\)
converges strongly to \(E_t\): it is a contraction, fixes invariant
vectors, and on \((I-U_t(b_0))w\) its norm is bounded by
\(|B_A\triangle(B_A+b_0)|\,\|w\|/|B_A|\to0\). The orthogonal
complement of the span of these differences is exactly the invariant
subspace, proving strong convergence by density.

Since the vacuum is invariant, dominated integration, using
\(|\langle v_t,U_t(b)v_t\rangle|\le\|v_t\|^2\), gives

\[
 \lim_{A\to\infty}\operatorname{avg}_{B_A}
      S(\Theta P_0\tau_bP_0)-|S(P_0)|^2
 =\int\|E_tv_t-S_t(P_0)\Omega_t\|^2\,d\nu
     +\int|S_t(P_0)-S(P_0)|^2\,d\nu.
\tag{27}
\]

Both terms are nonnegative. CL2 makes every component's first and second
moment equal to the barycenter's, almost surely, on the determining
family. Intersect its countably many full-measure sets and use individual
test-space continuity. Euclidean covariance extends equality from strictly
ordered positive-time pairs to all separated pairs: locally rotate any
nonzero separation to strict time order, translate to positive time, and
use a partition of unity. Consequently component means and connected
covariances agree with those of \(S\).

AF then precludes every F1 component on that full-measure set by S15.
All remaining Gaussian components have the same means and covariance,
hence the same entire Wick hierarchy. Their barycenter is Gaussian and
has zero fourth cumulant, contradicting (3). This proves the stated
mixture exclusion. Component clustering was never required, and invariant
zero modes were not discarded by definition. CL2 is sufficient at these
two degrees; it is not an extremality theorem for arbitrary non-Gaussian
states or for decompositions into non-invariant states.

## S18 — DRAFTED(medium): preserve the mixture and generalized-free composite escapes

**Consumes:** positive spectral free fields and Wick contraction.
**Produces:** concrete limits on the comparator conclusion.
**Most likely failure point:** the flat-test extension and joint Gaussian
point-splitting identification; these use the full stated OS domain, not
just convergence of the displayed two-/four-point kernels.

Without CL2 a mixture can satisfy (3). Let \(q\) be a centered elementary
GFF with separated covariance
\(Q_q(r)=\int_0^\infty s^2G_s(r)\,ds/\log^2(e+s)\), and independently
choose a spacetime-constant \(T\in\{1,2\}\) with equal probabilities.
For \(e=Tq\),
\(C_{ij}=\tfrac52Q_{q,ij}\) and
\(\kappa_4=\tfrac94(Q_{q,12}Q_{q,34}+Q_{q,13}Q_{q,24}
+Q_{q,14}Q_{q,23})>0\). The heat representation, splitting mass at
\(r^{-1}\) for an upper bound and restricting it to
\([r^{-2},2r^{-2}]\) for a lower bound, gives
\(Q_q(r)\asymp r^{-8}/\log^2(1/r)\). Thus AF holds. This is a finite
mixture of Gaussian states, not a Gaussian state on \(e\). Its component
two-point functions differ, so degree-two CL2 fails by (27), even when
the degree-one cluster test has no invariant mean variance to detect.

More strongly, even CL2 does not exclude all generalized-free Wick
composites. Put

\[
 H(r)=\int_1^\infty\frac{G_s(r)}{\log(e+s)}\,ds,\qquad
 e_*=2\sum_{a=1}^{p}:\psi_a\chi_a:,
\tag{28}
\]

with integer \(p\ge1\), all \(2p\) fields independent and of covariance
\(H\). The heat
formula gives \(0<H(r)\le1/(\pi^2r^4)\). On setting
\(\ell_\lambda=\log(\lambda^{-2})\) and \(s=\sigma/\lambda^2\),
the interval \([\lambda^2,\lambda]\) contributes
\(O(\lambda\ell_\lambda)\); on the remaining interval the logarithm
ratio is at most two and converges to one. Dominated integration by
\(2G_\sigma(r_{\min})\) proves uniformly on compact separated distances

\[
 \ell_\lambda\lambda^4H(\lambda r)\longrightarrow(\pi^2r^4)^{-1},
 \qquad H(r)\le4e^{-r/2}/(\pi^2r^4).
\tag{29}
\]

The second inequality follows from
\(r^2/(8t)+t/2\ge r/2\) in the heat integral. Wick contraction gives
\(C_*=4pH^2\) and
\(\kappa_{4,*}=32p\sum_c\prod_{ij\in c}H_{ij}>0\).
Consequently this composite has AF and a positive fourth cumulant on the
specified nonnegative bumps. In any finite Wick expansion of two separated
blocks, the terms without cross edges equal the product of expectations;
every other term has a decaying \(H\) edge. Equation (29) therefore proves
ordinary clustering, hence CL2, at every fixed block order.

These are admissible separated hierarchies, not coincident Euclidean products.
Approximate each spectral measure by finite positive atomic sums using
right endpoints. Monotonicity of \(G_s\) gives pointwise convergence and
domination by the limiting kernel. For (28), each \(n\)-point Wick term
has at most \(n\) edges and admits
\(|S_{n,\ell}(X)|\le C^n n!\min(1,\delta)^{-4n}\),
\(\delta=\min_{i<j}|x_i-x_j|\). Flatness and Taylor's formula of order
\(4n\) contribute the factor \(\delta^{4n}/(4n)!\); a weight
\((1+|X|^2)^{-5n/2}\) is integrable in \(4n\) dimensions. Thus
\(|S_{n,\ell}(F)|\le D^n n!\|F\|_{9n,1}
\le e^D(n!)^2\|F\|_{9n,1}\), uniformly. This proves convergence on
every flat test. Each atomic free hierarchy has RP; finite OS forms,
covariance and reality pass to the limit. The common reconstruction
interface applies. Cross-species point splitting has no self-contraction
and converges in the same OS norms on ordered supports, giving the
composite realization in the joint Gaussian theory. For \(q\), its
Gaussian pairings with kernel bounded by \(192/(\pi^2r^8)\) give the
same maximal \(4n\) power and the same argument.

Choosing \(p=3d\) in (28) also matches the free Maxwell trace spectrum:
each quadratic block has matrix \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\),
so even trace powers are \(2p=6d\) and odd ones vanish. At collinear
points Maxwell's fixed \(J_0\) has precisely this spectrum. In the units
\(u=\ell_\lambda\), all collinear leading connected kernels therefore
agree. This is **not** a claim that (28) satisfies (16) for the exact
finite-width bumps, all geometries, or an identified YM coupling. It
shows that (3), even with clustering and more collinear leading data,
has no universal exclusion theorem for arbitrary GFF composites.

Finally the atomic approximants to (28) are F1 states and converge on every
finite set of separated moments. Any continuous finite-moment function
vanishing on all F1 states must vanish at their limit, which satisfies
(3). Thus one cannot universally convert just the COMBO conjunction into
the unchanged N5 finite-moment separator. This does not rule out a different
YM-specific witness with additional information.

## S19 — GAP: remaining endpoint, scope checks and recovery checkpoint

**Consumes:** the completed conditional chain S01–S18.
**Required output for an actual YM conclusion:** supply the missing
original-law interfaces at their exact strengths, then check the whole
assembled proof. The present note establishes no actual YM lower match.

The desired limiting state would have a covariance of dimension-eight
short-distance order with a sub-power vanishing amplitude, and a fixed
nonzero separated fourth connected moment. A Gaussian \(e\) cannot have
the latter; a finite canonical Wick-composite \(e\) cannot have the former.
With (26), no admissible invariant mixture of those classes can have the
same data. Arbitrary Wick composites of GFFs remain a broader target.
If that target is intended, a new class-wide discriminator and matched YM
data are still required. MIXGFF's two-geometry GEO route is live for its
restricted common-scalar-kernel quadratic class Q; it neither classifies
all GFF composites nor follows from matching this one four-bump tuple.

The combined criterion is a countable asymptotic condition plus a
finite-moment polynomial. It does not satisfy an unchanged requirement
for one continuous finite-moment witness null on the entire union.
No contract, axiom or algebra is silently changed to remove that mismatch.
Existence of the complete YM observable theory, scattering and the physical
Hamiltonian mass gap are separate from this scalar conditional witness.

### No-Go Discipline Gate: scoped tests, not a universal no-go

**N1 — alternatives.** The real mathematical routes examined are listed
below. No route is called ruled out by landed authority; no packet PASS is
claimed, and a count of routes supplies no proof of exhaustiveness.

| Route | Actual result in this note |
|---|---|
| Canonical mass-shell power/log expansion | ATTEMPTED: S15 gives the F1 contradiction at its finite-propagator scope. |
| Arbitrary elementary Gaussian spectral covariance | ATTEMPTED: AF can hold, but the exact Gaussian cumulant identity fails the other conjunct. |
| Invariant mixture/ergodic decomposition | ATTEMPTED: S17 works only with CL2; S18 preserves the nonclustered escape. |
| Logarithmic spectral Wick composite | ATTEMPTED: S18 is an explicit surviving clustering example for the conjunction. |
| Normalized source-jet comparison versus renormalized graph matching | ATTEMPTED reductions, not closed routes: (12) and (21)–(23) name two different mechanisms for the remaining dynamical estimate. Neither is declared impossible. |
| Multiple geometries/OPE data | Unexecuted live extension: GEO targets a narrower quadratic class; a general WGF theorem and actual YM data are missing. |

These entries deliberately include successful routes, counterexamples and
open routes; they are not five failed attacks supporting a global negative
claim. The audit packet's five-closed-route submission condition is not met
and is not asserted met. The owner's single-file/no-audit instruction
precludes separate packet/ledger/runner artifacts; this is only an internal
scope check for an author draft.

**N2 — dependence.** Do not count the named residuals as independent walls.
Let A denote actual E-ALG/SEQ, T denote I-FLOW, J denote (12), and C denote
(26), with common definitions held fixed. The actual-YM implication audit is:

| Pair | First implies second? | Second implies first? | Independent? |
|---|---|---|---|
| A, T | Unresolved | Unresolved | Not established |
| A, J | Unresolved | Unresolved | Not established |
| A, C | Unresolved on actual YM | Unresolved | Not established |
| T, J | Unresolved | Unresolved | Not established |
| T, C | Unresolved | Unresolved | Not established |
| J, C | Unresolved | Unresolved | Not established |

At the abstract hierarchy level, ALG and separated convergence alone do
not imply CL2: S18's invariant scale mixture supplies a counterexample.
That is not a counterexample on the actual Wilson trajectory. The cluster
family concerns only degrees one/two and cannot be silently identified
with the all-order A contract. Conditional on A,T,I-FREE, J supplies both AF and
the fourth lower match, so those consequences are not extra walls.
The coefficient/remainder route S12–S13 is an alternative to J's fourth
part; it is not stacked as an independent mandatory condition.

**N3 — hidden conditions.** All uses of reconstruction, invariant components,
moment integrability, full Euclidean recovery, relative source radii,
finite-coupling tuning, Ward identities, operator matching, counterterms
and terminal/large-field terms have explicit consumers above. No use of
“standard QFT,” centering, or a beta function supplies them. The primitive
registry was inspected; the approved units, kinetic-form and realized-state
primitives are not being treated as missing axioms or as estimates of these
connected Wilson observables.

**N4 — residual matching.** LGF is used only for a free order-two kernel;
TSE55/WITNESS only for conditional PL-1L summation; CUMUL for separated
free coefficients; K4MATCH for the complete fourth-source recursion;
K4CORR/K4CORR2 for formal cancellation and the explicitly unclosed
renormalized complement; MIXGFF for invariant-mixture and spectral-composite
arguments. F17 has a different observable and is not used to close an
\(e\)-source residual. The newer Gaussian coupling theorem supplies a
Gaussian coefficient bracket, not finite-\(u\) source matching.

**N5 — resolutions.** The comparator arguments concern complete hierarchies
on flat separated tests and their reconstructed named field. The lower
cumulant is at four separated supports at a fixed physical scale; AF uses
a countable family after continuum limits. No per-link, per-slice or
time-zero magnetic statement is promoted to that conclusion. No numerical
per-site/per-mode/per-block experiment was executed. No unmarked-net or
all-GFF-composite exclusion is asserted.

**N6 — partial closure.** Nothing here says new axioms are required.
Actual proofs of normalized source matching, a compatible renormalized
forest estimate plus a full-law remainder, or IR block clustering would
close their respective interfaces without new physical primitives.
Changing the target to COMBO's stated union resolves only the target
contract, not a dynamical estimate. A common multiplicative normalization
cancels in the ratio but cannot retire absolute matching for the fixed field.

**N7 — steelman.** A stronger sourced INDUCT norm might already propagate
all fifteen normalized jets with a uniform relative radius, retain all
returned histories, and make the nonlinear source remainder summably
smaller than its Gaussian reference. In that case derive (12) directly
with its constants; do not force the detour through a separately evaluated
finite \(c\). A global block-tree estimate could also yield (26). These
are concrete unclosed mechanisms, so failure to obtain them from the
currently written INDUCT source is not an impossibility result.

**N8 — prior echoes.** COMBO's mixture escape survives without CL2; MIXGFF
already supplies the conditional infrared mechanism removing it, which S17
uses. Its clustering logarithmic composite still survives the broader WGF
claim. K4CORR2 improves the earlier diagnostic regulator/subtraction work,
but expressly leaves its full complement open. The newer uniform Gaussian
coupling theorem improves FLOW's old coefficient frontier and was checked
for that change of scope; it does not retire the finite-coupling or source
residual. No stale OPEN label is used as evidence of a physical obstruction.

### Current checkpoint and next decision

Target: (3) for the original \(Z(a)=1\) flat Wilson clover, on the same
all-order hierarchy, optionally with (26). The only new artifact is this
conditional synthesis and joint estimate (12)/(16); it is not a claim
of a new free-side theorem or of a completed four-dimensional YM construction.

The next decisive handoff is the precise I-IND source norm and its output
constants. Check whether it controls the actual normalized fifteen-jet
recursion and yields (12), or only absolute/source-free bounds. If it does,
instantiate S10's windows and S03–S04's full hierarchy hypotheses. If it
does not, the missing work is (12) or the alternative full-law (21)–(23),
not another rephrasing of the free coefficient. Request (26) only for the
mixture enlargement. Reopen the bare-majorant route only with compatible
subtractions and finite matching; shrinking the UV cutoff in its present
absolute bound cannot help. This checkpoint supersedes any partial progress
summary for this single-file task.

### Source identities and author verification

Working HEAD: `fe7b56d4c938a301e1fefb6b082a844862776a94` on `claude/q-S1`.
The initial local `origin/main` was
`01589af3faf806b736c42dc2f3bd625e9edead9f`; a root fetch attempt was
denied access to `FETCH_HEAD`. During source extraction the shared ref
advanced to `bcab5d2ee4a908fbb4e6025635fb878e6c157ebe`, which was rechecked.
The workflow and selected skill sources matched that snapshot. Planning
ref `origin/ai/execution` was
`56c5c0ab64f532c5784e895b2f9aa6894fa334e0`. Planning supplies no science
status. Searches of the identified main snapshot for AF-e, PL-1L,
K4RATIO-REM/N5-COMBO and the flow/induction identifiers did not supply a
landed matching result; this is not an exhaustive equivalence search.

| Local source | SHA256 |
|---|---|
| AUTHOR.md, briefs_q/NGYM | `6127cfa71e791865d7d25e533c2a7dc490775e72d3bac202e9509fa22ed2e6e7` |
| COMBO.md | `194a32f0547189aa195e2047090026603d5119208b3cac2a0f0c9fb123fdf276` |
| WITNESS.md | `f545b2b544234e9e2a133fb0957bee18cf2c290912897d5a5028ccadc484ecb8` |
| CUMUL.md | `50f337bffacc0e49b7e3bc737609190bd106d8b9210c2ab8f1059745cc1bcfd8` |
| K4MATCH.md | `2f795c75609075e6d48096abf5ba8572a80f6271a554889f7212c4be75827604` |
| K4CORR.md | `e7d63ea8071f8f9c7eeadfb4f7c02ce0efc2435809096f8c30099c2dc094d689` |
| K4CORR2.md | `f7af21719921a45f7ada8f82ab8a8f2bd1db5d37f86ba282d6b725a452323b25` |
| MIXGFF.md | `6978578119322af1c1161f3282c81055815e5f3cce098d5be78261cfe8e328d3` |
| LGF.md | `40ea604c79f17027129628bc8b31f5fd6209da21dded864bf45a422dad24505e` |
| TSE55.md | `a894d1b2439a7b83311175c9e6e30f6fb52cc015a74c6be7e839be8192a7869a` |
| F17.md | `b2a4f0f8650ff2db736acfaa1b0f30be1d30d449ceb827e32f55186b81e82440` |
| FLOW.md | `085cd225228a23847b053650fe8bff4c14529d7e630a74565b301d39855e442f` |
| INDUCT55.md | `2fbb4575b95d5c8f2d4ba25f93f1665274ba36b0e266c4ecb2bab9ad3f515000` |
| FLOW55.md | `56d2707f4b571585db26cf2a077dbaee57bc936c76821cdbc50710e4b36e9d25` |
| UIR55.md | `4c6d80473a80714e2a5aa1e241e8835648bbe3c65a7bca38a5758faf3c5accb4` |
| UNIFORM_ONE_LOOP_COUPLING_ASTRA.md | `b7baa6a711969c8fc96538009bb8f9f9acdde3f14f6d2f570a6ca5b9391516ce` |
| REVIEW_UNIFORM_ONE_LOOP_COUPLING_ASTRA.md | `ca80f189e924ac7d15462258d4a1e95734cfa55e45d382e7791dabdf0de2cc27` |

COMBO/WITNESS were read completely by the author; bounded read-only source
readers read CUMUL/K4MATCH/K4CORR/K4CORR2 and MIXGFF/LGF/TSE55/F17
completely, with the load-bearing passages reread for this argument. They
performed extraction, not review. FLOW's heading inventory and relevant
complete interface arguments were examined at lines 1–237, 366–505,
865–935, 1579–1649, 4403–4490, 4541–4784 and 4824–4851 (coverage within
those ranges was targeted); its entire historical research log was not
independently reverified. The newer uniform Gaussian theorem and its review
were read completely by a source reader; its statement and boundary were
also checked by the author. INDUCT55 was read completely.

Primary literature abstracts were checked for orientation only:
[Dütsch–Rehren, generalized free fields](https://arxiv.org/abs/math-ph/0209035)
and [Pottel, configuration-space BPHZ](https://arxiv.org/abs/1706.06762).
No theorem from either abstract is imported to discharge a step. Wick,
Osterwalder–Schrader and the Balaban/Dimock constructive program are the
methodological antecedents, not substitutes for the hypotheses printed here.

Author checks cover the complete final text, status counting, dependency
directions, source identities, constant margins, and the three orders of
limits (cutoff/volume, ultraviolet scale, spatial cluster radius). They are
not independent review. No checker from a previous note was rerun or its
historical PASS counts adopted as proof of an interacting estimate.

Mechanical receipt: all nineteen step IDs occur once, with one status each;
the thirteen drafts comprise twelve high-confidence and one medium-confidence
conditional arguments. All seventeen recorded input hashes matched after
writing. The final source has 377 balanced inline math delimiter pairs and
36 balanced display pairs, with no control characters. Author checking
repaired missing opening delimiters, the source-log/block-factor and
volume-threshold/free-ratio notation collisions, and differential spacing.
An initial punctuation assertion also falsely flagged a valid escaped thin
space; the corrected assertion distinguishes it from the malformed text.
These are document checks, not numerical verification of YM. The tracked
diff is empty, HEAD is unchanged, and the sole newly created work product
is `NGYM.md`; the untracked author-brief directory predated this task.

**Step counts:** PROVEN 0; DRAFTED 13; GAP 6.
**Three weakest links:** (i) I-IND to the original-law normalized joint
source estimate (12), especially mixed/terminal/large-field terms;
(ii) compatible renormalization and absolute clover matching, or the full
uniform coefficient-plus-remainder alternative (21)–(23);
(iii) actual all-order common-hierarchy reconstruction and, for mixtures,
the additional infrared block-cluster estimate (26). These are grouped
handoff priorities, not three asserted independent mathematical walls.
