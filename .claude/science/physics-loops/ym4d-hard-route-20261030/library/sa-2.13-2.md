# Obligation 2.13, continuation: the literal analytic certificate
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed; queue row 117 requests max); checkout `ceeb30b1b83daac2b540bbf0f0de9a7819db5a0c`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, granting no status.

**Outcome: STOPPED at the session budget.** The smaller statements below are proved with their displayed premises. The literal certificate (8.1) and normalized assembly are neither proved nor refuted. No admitted counterexample was obtained.

## 1. Scope and sources

This is row 117, continuing `library/sa-2.13.md`, not a new proof of its conditional forest sum. The target is its (8.1) for the literal operations, followed by its hypothesis 3. In particular the full mixed form $Q$ and the exterior-field-dependent reference denominator remain in the integrand. The conclusions of that note's Lemmas 3.1 and 7.1 and Sections 4–6 and 8 are cited with their stated hypotheses, not re-proved or promoted to unconditional facts.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the construction and arguments of [the outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex). `SA Lx–y` denotes its literal TeX lines. It was fetched once to `/tmp/sa_ym4.tex`; SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. Repository references are at the checkout above. The literature starting point is the existing `library/lit-balaban.md`, Sections 0 and 3, and the source-by-source analysis in `library/sa-2.13.md`, Section 2; cited literature has only the standing specified there. No external paper directory is designated in this item.

Read first: `GOAL.md`; `FINISH.md`, “How we work”, “Working efficiently”, “Rules”, and row 117; then `library/sa-2.13.md` in bounded consecutive ranges, and Section 7 of both `gates/sa-2.8-terms-gate.md` and `library/sa-2.8-terms.md`. The sparse checkout's workflow is read from this same commit with `git show`. No other branch is fetched. Only this file is written; no proof computation, audit, delegation, commit, push, PR or post is used.

## 2. Counterexample-first scope

The first tests concern the actual carrier-truncated stored form and a possible zero of the actual reference denominator at a permitted complex pair. A matrix example lacking the literal walk construction, or an integral lacking the critical-reference structure, refutes only a shortcut. It does not refute row 117. Sections 3–4 distinguish these outcomes and close the smaller analytic and cut-comparison statements reached by these attacks.

## 3. Critical centring gives a zero-free estimate without a Hessian comparison

The analytic implication below is proved. It keeps the actual field-dependent denominator, the Haar density, and the full mixed $Q$. It removes the relative-Hessian and Gaussian-factorization requirements for this particular consumer. The reference-chart hypotheses in its application retain their actual standing.

Fix a frame. After its tree delta functions have been integrated, let $m$ be the number of free reference bonds, $d=3m$, and $u_e\in\mathbb R^3$ their physical exponential coordinates. Write $g^{-2}$ for the coefficient in the actual reference law, put $u=gb$ and $H=M_0\varepsilon_k/g$ (thus $H=M_0P_k$ when the threshold frame uses that same coupling), and set

\[
 F_p(u)=A(\phi_X,U_{k,X}(e^{iu}V_\Lambda(p))),\quad
 \widehat D(p)=e^{F_p(0)/g^2}D_X(p),\quad
 \mathcal B_H=\{b:|b_e|<H\ \forall e\}.
 \tag{3.1}
\]

These reference coordinates are distinct from the prepared-shell coordinates of $Q$. With normalized Haar measure, the exact formula is

\[
 \widehat D(p)=(2\pi^2)^{-m}g^d
  \int_{\mathcal B_H}e^{-g^{-2}[F_p(gb)-F_p(0)]}J_g(b)\,db,
 \quad J_g(b)=\prod_e\left(\frac{\sin(g|b_e|)}{g|b_e|}\right)^2.
 \tag{3.2}
\]

At a complex parameter the integration variables remain real. Equation (3.2) defines the continuation on this fixed reference-coordinate domain; it is not a translation of Haar measure onto a complex contour.

**Lemma 3.1 (comparison to the actual real reference law).** Let $z\mapsto p(z)$ join a real reference parameter $p(0)$ to $p(s)$, $|s|<\rho$. Suppose $F_z(u):=F_{p(z)}(u)$ is holomorphic on the product domain $|z|<\rho$, $\max_e|u_e|<r$, and $|F_z(u)|\le C_FK$ there. Let $F_z^{\rm all}$ be the complete reduced reference action, and put $F_z^{\rm out}=F_z^{\rm all}-F_z$. Assume

\[
 DF_z^{\rm all}(0)=0,\qquad
 \|DF_z^{\rm out}(0)\|_{\infty\to\mathbb C}\le T
       \quad(|z|<\rho).
 \tag{3.3}
\]

The norm is dual to the maximum of the bond norms. Assume $F_0$ is real on the real cutoff, that the whole cutoff is admitted, and $gH\le\min(r/2,1/2)$. Define

\[
 \delta_*:=\frac{2TH}{g}
       +\frac{2C_FKH^2}{r^2}\frac{|s|}{\rho-|s|}.
 \tag{3.4}
\]

Then

\[
 \left|\frac{\widehat D(p(s))}{\widehat D(p(0))}-1\right|
       \le e^{\delta_*}-1.
 \tag{3.5}
\]

In particular, if $\delta_*\le\log(3/2)$, the denominator has no zero and $|\widehat D(p(s))|\ge\widehat D(p(0))/2$. No positive lower bound for its Hessian is assumed.

*Proof.* Fix nonzero real $b$ in the cutoff, write $v=b/\max_e|b_e|$, and expand $F_z(tv)=\sum_{n\ge0}a_n(z)t^n$. The one-variable Cauchy formula on radii tending to $r$ gives $|a_n(z)|\le C_FK r^{-n}$. Expanding each coefficient on the $z$ disc and applying the same formula gives

\[
 |a_n(s)-a_n(0)|\le C_FK r^{-n}
                   \frac{|s|}{\rho-|s|}.
\]

For the coefficient of degree one use complete criticality instead: $a_1(z)=-DF_z^{\rm out}(0)[v]$, hence $|a_1(s)-a_1(0)|\le2T$. Subtract the two constant terms, evaluate at $t=g\max_e|b_e|$, and divide by $g^2$. The terms of degree at least two sum to at most

\[
 \frac{C_FK}{g^2}\frac{|s|}{\rho-|s|}
       \frac{(gH/r)^2}{1-gH/r}
 \le\frac{2C_FKH^2}{r^2}\frac{|s|}{\rho-|s|}.
\]

The linear term costs $2TH/g$. The same bound holds at $b=0$. Thus the difference $\Delta_s(b)$ of the two centred exponents has modulus at most $\delta_*$ everywhere on the cutoff.

The real centred integral is positive and finite: its integrand is positive on an open product ball, continuous there and bounded on the cutoff by the admitted action bound. Divide its integrand by its integral to obtain a positive probability measure $\nu_0$ on $\mathcal B_H$. The scalar Haar/scale factor cancels in the ratio; the density $J_g$ remains in $\nu_0$. Exactly,

\[
 \frac{\widehat D(p(s))}{\widehat D(p(0))}
      =\int e^{-\Delta_s(b)}\,d\nu_0(b).
\]

The exponential series gives $|e^{-w}-1|\le e^{|w|}-1$. Integrate this inequality to obtain (3.5). The disc of radius $1/2$ about one avoids zero. For $m=0$ both centred integrals equal one, and the conclusion holds directly. ∎

Apply `sa-2.13.md`, Lemma 3.1, to the real denominator, with its own admitted chart. This gives, without a new real normalization proof,

\[
 -\log|\widehat D(p(s))|
       \le d\log(g^{-2})+C_a d+C_FK+\log2.
 \tag{3.6}
\]

The omitted factor of $D_X^{-1}$ is exactly $e^{F_p(0)/g^2}$. It must cancel against the same reference action in the complete exponent, as in the exact identity of `sa-2.8-terms.md` (1.3). It is not bounded separately or called a number. Equation (3.5) also supplies a single local branch of the logarithm of the ratio, by the convergent series for $\log(1+w)$ on $|w|\le1/2$.

**The property doing the work.** It is uniform complete-action criticality of the moving reference branch. It changes the parameter-dependent linear coefficient, after scaling, from a possible $g^{-1}$ forcing into the distant-cutoff tail $T/g$. The rest of the centred action changes by a quadratic amount $O(|s|H^2)$ on the *entire real cutoff*. No Laplace approximation, determinant identification, or Gaussian separation is involved. The example (9.2) of the prior note has $DF_z^{\rm all}(0)=z$, so fails exactly this hypothesis.

**Scale check.** SA L6033 specifies $\alpha_{\iota,k}=C_\iota\theta_k^{-1/2}(\log\theta_k)^q$; these are $g$ times logarithmic powers on the unsourced frame. A fixed tube comparison between frame and action couplings preserves the estimates below; it is not an equality of those couplings. The cancellation preceding (3.6) must always use the coefficient actually present in the reference law. Suppose the parameter readout has $|s|\le Cg\ell^{q+b}$, $K\le C\ell^a$, $H\le C\ell^{\mathfrak p_0}$, fixed positive chart radii $r,\rho$, and $T\le CK e^{-cM\check R_k}$ with $\check R_k\ge c_R\ell^{r_{\rm h}}$, $r_{\rm h}\ge2$, where $\ell=\log g^{-2}$. Here $r_{\rm h}$ denotes the hierarchy exponent. The two terms of (3.4) are bounded by a polynomial in $\ell$ times $e^{\ell/2-c'M\ell^{r_{\rm h}}}$ and $e^{-\ell/2}$ respectively. Both tend to zero at one ceiling independent of depth. For a written verification, first make $c'M\ell^{r_{\rm h}}\ge\ell$, then use $e^t\ge t^n/n!$ with $n$ larger than each fixed polynomial degree. If the chart radii have polynomial losses in $\ell$, the same argument absorbs them; an exponentially shrinking chart would be a different input.

The complex derivative tail can also be reduced to a **real** tail on a sufficiently roomy joint chart, rather than assumed as a new complex locality theorem.

**Lemma 3.2 (real tail to complex tail).** If $f$ is holomorphic on a neighborhood of $|z|\le R$, $|f|\le B$ there, and $|f(x)|\le\epsilon\le B$ for real $|x|\le R$, then $|f(z)|\le\sqrt{B\epsilon}$ for $|z|\le R/4$.

*Proof.* In the upper half disc put
$u(z)=\frac2\pi\operatorname{Im}\log\frac{R+z}{R-z}$.
It is harmonic, zero on the diameter and one on the semicircle. The maximum principle applied to $\log|f|$ gives
$\log|f(z)|\le(1-u(z))\log\epsilon+u(z)\log B$.
One can remove the two boundary endpoints from this use of the principle by adding
$\eta\log(|R-z||R+z|/(4R^2))$ to the left minus the right: it tends to minus infinity at the endpoints and is nonpositive on the rest of the boundary. Apply the maximum principle and let $\eta\downarrow0$. Zeros of $f$ give minus infinity and cause no difficulty; alternatively apply the ordinary maximum-modulus principle to the corresponding exponential times $f$. For $|z|\le R/4$,
$u(z)\le(4/\pi)\arctan(1/4)<1/2$.
This follows also by taking the argument of the ratio, whose tangent is $2R\operatorname{Im}z/(R^2-|z|^2)$. The asserted bound follows; reflect the construction for the lower half disc. If $\epsilon=0$, the identity theorem gives $f=0$. ∎

Apply this to $f_v(z)=DF_z(0)[v]$ for every real unit bond-supremum direction $v$. Cauchy gives $B=C_FK/r$. At real $z$, complete criticality gives $f_v(z)=-DF_z^{\rm out}(0)[v]$. A uniform real locality estimate $|f_v(x)|\le CK e^{-cM\check R_k}$ thus gives a complex tail $C'K e^{-cM\check R_k/2}$ on the smaller disc, with any polynomial chart losses absorbed in the prefactor. Splitting a complex direction into real and imaginary parts costs at most another factor two. Reset $\rho$ in Lemma 3.1 to a radius inside this smaller disc; the exponential rate still suffices in (3.4). For a complex field written with $A'=A_R+iA_I$, use the slice $e^{i\eta(A_R+zE)}U$, $E=A_I/\|A_I\|$, and target $z=i\|A_I\|$; its diameter consists of real fields. If $A_I=0$ no such slice is needed. Admission and the real tail must hold on that diameter, not just at its centre. The independent current is not an argument of the Wilson-only reference law.

**Standing of the application.** SA L17604–17610 gives (3.1)–(3.2), and SA L17585 bounds $d$ by $12(C_\Lambda M)^4$. The action bound and real product-ball admission are the named I2/GEO inputs of the prior note. The holomorphic complete critical branch is Proposition 2.4, SA L17656, still I4's unrebuilt input in `sa-2.8-terms.md`. Its real stationary identity extends by the identity theorem only where that same branch is already admitted. Section 7(a) of the gate proves the real cutoff-tail estimate with the corrected $g^{-1}$; it does not establish the larger joint chart and real slice required above for every pair. Lemma 3.2 supplies the complex tail once those real-slice premises hold. These arguments eliminate the relative-Hessian subproblem for this consumer; they do not silently discharge the reference admission theorem.

## 4. The stored cut: a direct comparison, and its exact input

Use the actual free pivot coordinates, with their counting inner product. At a step's physical axial pair, `a2-full.md`, Theorems I–II, identify the complete precision with the next-fibre Hessian, including the constraint second jet and the gauge term. At other complex pairs that note requires the additional gauge-gradient term in $\mathsf A^{\rm full}$. Its real gap is conditional on the separated-layer results and their stated gauges. The note is research text, awaiting its cross-provider check; it explicitly does **not** prove the carrier walk expansion (H-walk). The latter is also only a task placeholder in `library/h-walk.md` at this checkout. No gap for the profile-weighted main-step $Q$ is supplied by these statements or needed by Lemma 7.1 of the prior note.

**Lemma 4.1 (carrier-tail comparison for the literal cut).** Let $\mathsf A$ be a finite real symmetric matrix on orthogonal free-coordinate groups $I$ (stored) and $J$ (integrated), with $\mathsf A\ge\gamma I$. Suppose its actual specified carrier expansion and that of $C_J=(\mathsf A_{JJ})^{-1}$ have the two-sided absolute moments

\[
 \begin{split}
 \sup_x\sum_{y,\lambda}e^{\kappa D(\lambda)}
           |\mathsf A_\lambda(x,y)|&\le W_A,\\
 \sup_x\sum_{y,\mu}e^{\kappa D(\mu)}
           |(C_J)_\mu(x,y)|&\le W_C,
 \end{split}
 \tag{4.1}
\]

and the same inequalities with rows and columns interchanged. The series are closed under transposition, with the same carrier for a term and its transpose. Each carrier is connected, contains the coordinates at its ends, and $D$ is its diameter in the distance used to control physical cell crossings. A chain carrier is the union of the carriers of its factors. Expand

\[
 S=\mathsf A_{II}-\mathsf A_{IJ}C_J\mathsf A_{JI}
 \tag{4.2}
\]

using precisely those series, then apply the retention rule of SA L17550. If every rejected chain meeting $I$ has carrier diameter at least $s$, the retained matrix $K$ satisfies

\[
 K\ge[\gamma-(W_A+W_A^2W_C)e^{-\kappa s}]I.
 \tag{4.3}
\]

Thus $K\ge\gamma I/2$ when $(W_A+W_A^2W_C)e^{-\kappa s}\le\gamma/2$. This is a bound for the truncated series itself, not an identification of it as a Schur complement.

*Proof.* For $a\in\mathbb R^I$, complete the square in $b\in\mathbb R^J$:

\[
 (a,b)^{\mathsf T}\mathsf A(a,b)
  =a^{\mathsf T}Sa+
    (b+C_J\mathsf A_{JI}a)^{\mathsf T}\mathsf A_{JJ}
    (b+C_J\mathsf A_{JI}a).
\]

Minimizing the left side and using orthogonality gives $a^{\mathsf T}Sa\ge\gamma|a|^2$. In a product chain the three carriers intersect successively at their contracted coordinates, so their union has diameter at most the sum of their diameters. Absolute row sums of the product are bounded, successively, by $W_AW_CW_A$; the column argument is identical. Consequently the chains of (4.2) have absolute exponential moment at most $W=W_A+W_A^2W_C$. Restricting the sum to rejected chains bounds each row and column of $R=S-K$ in absolute value by $We^{-\kappa s}$. The retention rule is invariant under reversing a chain, so $K$ and $R$ are symmetric. Explicitly,

\[
 |a^{\mathsf T}Ra|
 \le\tfrac12\sum_{x,y}|R_{xy}|(|a_x|^2+|a_y|^2)
 \le We^{-\kappa s}|a|^2.
\]

Subtract this estimate from the bound for $S$. A retained chain is assigned to the unique component containing its stored-cell intersection. Hence $K$ is block diagonal over those components, and (4.3) holds for every block by extension of its test vector by zero. ∎

There is a short geometric check behind the rejected-chain threshold. On a cubical grid of side $s$, use connectivity by intersecting **closed** cells and include every cell incident to an endpoint bond. A set of $\ell^\infty$ diameter strictly less than $s$ meets at most two adjacent grid intervals in each coordinate. All cells it meets therefore have a common point: in each varying coordinate choose their common face coordinate. Every nonempty subcollection of these cells is connected, and every one is within one cell layer of each other. If the carrier meets a stored endpoint, its intersection with the stored cells is nonempty, connected, and has every carrier cell within one layer. It is kept. The contrapositive proves the diameter threshold. If the walk convention enlarges a carrier by a fixed number of walk-cube layers, apply the same argument to that enlarged carrier; its exponential moment must then be the moment in (4.1). One cannot omit the enlargement when identifying $s$ with the level-$(j+1)$ cell size $LM\check R_{j+1}$ in level-$j$ units.

This geometric argument removes a tempting counterexample in which a short chain clips two corners: closed-cell contact connects the clipped cells. With face-only adjacency the argument is false, and the connectivity convention would have to be supplied differently. The analytic input in (4.1) is about **absolute carrier sums**, not just the kernel after cancellation. For example the scalar positive matrix $S=1$ can be written as a short-carrier term $-1$ and a long-carrier term $2$. Keeping the first makes $K=-1$, even though the summed kernel is local and positive. This explicitly refutes the smaller inference “positive complete precision and a decaying summed kernel imply a positive carrier cut.” It is not the outline's specified walk expansion and not an admitted Yang–Mills counterexample.

For the actual series, SA L10311–10328 asserts the needed local walk bounds for both the compressed precision and covariance; products give the chains in (4.2). Lemma 4.1 explains exactly how such an absolute bound proves the stored lower bound, without an additional IMS argument. Replacing that asserted series by an arbitrary new decomposition would change the literal operation. The conditional gap in `a2-full.md` alone therefore does not discharge this application.

**A closed flat specialization.** Specify the local flat models and carrier assignment of `flat-port.md`, Sections 10–11, with the plain/straight identification repair W2 of `gates/flat-port-gate.md`. Those are existing checked research inputs, not new audit status. They give the complete flat gap $\gamma_L$, including the actual soft contour gauge and pivot coordinates, and an absolute local expansion for the precision and every conditioned covariance. Here is the extra step needed to apply the cut. Its patch expansion has a sum of operator norms of length-$n$ terms from a fixed initial patch bounded by $Bq^n$, $q<1$, with the reverse bound too. Finite products and the nested covariance expansion preserve such a bound after replacing $q$ by a larger number less than one, as in that Section 11. Each enlarged patch has level-metric diameter at most a fixed $D_0$, so a length-$n$ carrier has physical diameter at most $D_0(n+1)$ in the current level's units. A terminal patch contains at most a fixed $N_0$ current-level free scalar coordinates: its physical side is bounded by its fixed walk-cube size, since all finer scales are at most one. There are boundedly many possible initial patches for one such coordinate. Bounding a matrix entry by its operator norm therefore gives

\[
 \sup_x\sum_{y,\lambda}e^{\kappa D(\lambda)}|O_\lambda(x,y)|
 \le C N_0 B e^{\kappa D_0}
                 \sum_{n\ge0}(q e^{\kappa D_0})^n<\infty
 \tag{4.4}
\]

for $0<\kappa< D_0^{-1}\log(1/q)$, and likewise for columns. All constants are fixed before the coupling ceiling. With $s=LM\check R_{j+1}$, (4.3) then proves the cut lower bound $\gamma_L/2$ at sufficiently small coupling, uniformly in depth and conditioning, for this specified flat expansion. Thus a flat counterexample cannot be obtained by just cutting those walks at irregularly shaped stored regions. This does not identify an unspecified different series term by term, nor extend its local inverse construction to the curved independent-current system.

## 5. Local normalizers and Jacobians on the admitted one-step charts

These costs can be established without the cut-form lower bound. They concern actual local maps, not the unknown multiscale reference admission.

**Pivot elimination.** Use the actual centered average, SA (QC1)–(QC4), L7959–8001: its internal contour mean is implicit, whereas its outer mean is an exponential of averaged closed logarithms. The local holomorphy and contraction construction are already proved in `a2-curved.md`, Section 5. Their finite derivative bounds depend on $L$, not on depth or the number of blocks. In the notation there, $q_V(a)=K_Va+R_V(a)$, $\|DR_V(a)\|\le C_L\|a\|$, and only one pivot occurs in a row. At flat data that pivot derivative is $L^{-3}I_3$: exactly $L$ of the $L^4$ straight segments contain the middle crossing bond and no internal contour contains it. At a real pure gauge the coefficient is $L^{-3}$ times an orthogonal adjoint transport, not necessarily $L^{-3}I_3$ in the original frame. The local curvature comparison in that section yields $\|J_c(0)^{-1}\|\le2L^3$ on its specified small chart.

Choose its physical radius $r_L$ smaller so that $2L^3C_Lr_L\le1/2$. At every point of its nonlinear graph,

\[
 \|J_c(a)^{-1}\|\le4L^3,\qquad
 |\det J_c(a)|^{-1}\le(4L^3)^3.
 \tag{5.1}
\]

Indeed $J_c(a)=J_c(0)(1+J_c(0)^{-1}[J_c(a)-J_c(0)])$; the inverse is its norm-convergent geometric series. Each singular value is at least $(4L^3)^{-1}$, giving the determinant bound. Different pivot equations have no other pivot in their support (SA L8167–8176), so coarea gives one such factor per coarse row, not a determinant of a dense global matrix. Normalized group delta in exponential coordinates is $(2\pi^2)\delta_{\mathbb R^3}(q)$. Together with Haar densities this leaves one fixed Haar constant per nonpivot bond. Those densities and their inverses are bounded on a smaller fixed chart: the analytic function $[\sin\sqrt z/\sqrt z]^2$ equals one at zero and is uniformly within $1/2$ of one on a sufficiently small disc, by its convergent power series. Thus the total local coarea price is $C_L$ per involved coordinate. Substituting $a=gb$ contributes exactly $g^3$ per free bond. Its logarithmic price is $3\log(g^{-1})$ when an inverse scale factor is required. These estimates also bound the holomorphic coefficients of the coarea formula; an absolute value of a complex determinant is not used to define its continuation.

**Tree gauges.** The tree includes the external anchoring bond, as specified at SA L17598–17604. Order its vertices from the leaves toward the anchor. Each gauge variable replaces its incoming bond by a left or right translate of a Haar variable; Haar invariance and a normalized group delta integrate it with mass one. Repeating removes every tree variable and leaves no residual constant gauge variable. This gives exactly unit tree Jacobian.

**The strip shift.** For fixed later data SA L17526 uses
$\Psi(W)=W e^{-i\vartheta(W)H}e^{iH}$,
with a fixed smooth cutoff satisfying $\operatorname{Lip}(\vartheta)\le C/\delta$. In a bi-invariant metric the inverse equation at $Y$ is
$W=Ye^{-iH}e^{i\vartheta(W)H}$.
Its right side is a contraction if $C\|H\|/\delta<1/2$: two exponentials here are on the same one-parameter subgroup, so their distance is at most $\|H\||\vartheta(W_1)-\vartheta(W_2)|$. Iteration on the complete compact group gives a unique inverse. The derivative differs from an isometry by a matrix of norm at most $C\|H\|/\delta$; hence its inverse determinant is at most $2^3$. Its holomorphic coefficient continuation in $H$ has the same bounded-inverse conclusion on a smaller complex ball. The cutoff is kept a function of the real stored variable, not analytically continued as a sharp field test. The required small ratio follows conditionally from the real strip locality estimate $\|H\|\le C\varepsilon_j e^{-\check R_j}$ and $\delta_j=(A_1/A_0)\varepsilon_j$. It is a pointwise bound before integration.

**The soft gauge normalizer.** For $\theta\epsilon^2\ge1$, $\epsilon\le1$, write $u=\cos t+i\sin t\,\widehat n\cdot\sigma$. Then $\|u-1\|=2\sin(t/2)$, $a(u)=1-\cos t$, and normalized radial Haar measure is $(2/\pi)\sin^2t\,dt$. The cutoff restricts $t<\pi/3$. On this interval $c t^2\le a(u)\le t^2/2$ and $\sin^2t\le t^2$. Substitution $v=\sqrt\theta\,t$ bounds the integral above by $C\theta^{-3/2}$. For a lower bound integrate $0<t<\tfrac12\theta^{-1/2}$: this interval is inside the cutoff, $\sin t\ge t/2$, and $\theta a(u)\le1/8$. Integrating $t^2/4$ on it gives $c\theta^{-3/2}$. Therefore

\[
 c\theta^{-3/2}\le z(\theta,\epsilon)\le C\theta^{-3/2},\qquad
 \frac{z(\theta/2,\epsilon)}{z(\theta,\epsilon)}\le C'.
 \tag{5.2}
\]

The upper bound for the numerator does not need $(\theta/2)\epsilon^2\ge1$. This proves the half-exponent price used at SA L18736–18750. The coupling and cutoff here are real and frozen in the ordinary complex-pair envelope.

For main-step shell variables with their prescribed bounded cutoffs, the full positive mixed form $Q$ may now be retained and estimated by `sa-2.13.md`, Lemma 7.1. Its integration cost is logarithmic per stored coordinate. That lemma does not extract a creation witness: the latter still requires the complete/cut energy in Section 4. Nor do the local estimates above assert that every later multiscale substitution remains in these charts.

## 6. The action-of-averages witness on every compatible real field

Here the one-step nonlinear input of SA L18218–18279 can be rebuilt for the actual centered average. This proves an energy implication for every real field, not only critical backgrounds. It does not supply the other tests of Lemma 2.5.

Put $f_U(p)=\|\partial U(p)-1\|$ for positive plaquettes. For $\mathrm{SU}(2)$, diagonalizing its unitary plaquette matrix gives

\[
 f_U(p)^2=2a_p(U).
 \tag{6.1}
\]

For a positive coarse $\mu\nu$ plaquette based at $y$, define the positive matrix

\[
 (Pf)(y;\mu\nu)=L^{-4}\sum_{x\in B(y)}
         \sum_{r,s=0}^{L-1}f(x+r e_\mu+s e_\nu;\mu\nu).
 \tag{6.2}
\]

Its row sums are $L^2$. Each fine plaquette occurs for exactly $L^2$ choices of $(r,s)$, since $x$ is then fixed and belongs to exactly one centered block $B(y)$. Its column sum is therefore $L^{-2}$. Restricting rows or columns only lowers these numbers.

For each coarse plaquette let $D$ be the rectangle of its four corner blocks, including their connecting bonds. It has bounded size depending on $L$ alone. If all its fine plaquettes have size below a sufficiently small $\epsilon_L$, comb gauge gives link logarithms of size at most $C_L\max_D f_U$. To verify this, compare the comb to a bond's initial site followed by that bond with the comb to its final site; exchanging adjacent perpendicular steps fills the loop with at most $C_L$ plaquettes. Telescoping products of their unitary transports bounds its deviation from one by $C_L\max_D f_U$. Choose $\epsilon_L$ so this lies in the fixed logarithm ball.

On that ball the actual contour mean and outer logarithmic mean are analytic with bounded second derivatives, by the finite construction cited in Section 5. Their linearization is exactly SA (QC15):

\[
 (K_Ia)(y,y+Le_\mu)
 =\sigma_a(y)+L^{-4}\sum_{x\in B(y)}a([x,x+Le_\mu])
                       -\sigma_a(y+Le_\mu).
\]

The $\sigma$ terms telescope to zero around a coarse plaquette. The remaining four straight segments bound the $L$ by $L$ plaquette surface in (6.2). Thus its linearized curvature is the oriented version of (6.2) applied to $da$. Taylor's integral remainder is at most $C_L\|a\|_\infty^2$. Replacing each fine $da$ by its exact plaquette logarithm also costs at most $C_L\|a\|_\infty^2$, since there are only finitely many factors depending on $L$. Finally $\|\log W/i\|=\|W-1\|+O(\|W-1\|^2)$ near one, as follows from $\|W-1\|=2|\sin(t/2)|$ for its two eigenphases $\pm t$. Consequently

\[
 f_{\mathcal M U}\le P f_U+r_U,
 \qquad r_U(y;\mu\nu)=C_L\sum_{p\subset D}f_U(p)^2\ge0.
 \tag{6.3}
\]

A fine plaquette belongs to only a bounded number of these four-block rectangles: their base coarse sites lie within two coarse units in each coordinate, and there are six orientations. Hence $\|r_U\|_1\le C'_L\|f_U\|_2^2$. Constants here are maxima of continuous derivatives on fixed compact balls, finite before any depth is chosen. No machine enumeration or numerical bound is involved. Noncommutativity enters the quadratic remainder; the positive linear matrix and its counts are unchanged.

For a set $S$ of plaquettes at level $t$, take successively all ancestor rectangles needed by (6.3). Let $E_l$ be the sum of $f_{\mathcal M^lU}^2$ over the corresponding level-$l$ plaquettes. This supplies all fields needed in the argument. The two row/column bounds imply $\|P\|_{2\to2}\le1$: apply weighted Cauchy–Schwarz in each row, then sum its columns. Also $\|P\|_{1\to1}\le L^{-2}$. Iterating (6.3), and using $\|v\|_2\le\|v\|_1$ for the nonnegative remainder vectors, gives

\[
 E_l^{1/2}\le E_0^{1/2}
       +C'_L\sum_{j<l}L^{-2(l-1-j)}E_j.
 \tag{6.4}
\]

Choose

\[
 E_*^{1/2}\le\min\{\epsilon_L/4,
                         (1-L^{-2})/(8C'_L)\}.
\]

If $E_0\le E_*$, induction gives $E_l\le4E_0$ at every level. Indeed, assuming this for earlier levels, the sum in (6.4) is at most $4C'_LE_0/(1-L^{-2})\le E_0^{1/2}/2$. It follows that $E_l\le(3/2)^2E_0<4E_0$. At every step each individual plaquette is at most $2E_0^{1/2}\le\epsilon_L/2$, so the chart used to obtain the next (6.3) is actually admitted. This starts at level zero and proves, rather than assumes, all the intermediate chart conditions.

Writing $\mathcal N_0(S)$ for these ancestor plaquettes and $e_*=E_*/2$, (6.1) yields the following bound for **every** real $U$ on that neighborhood:

\[
 \sum_{p\in\mathcal N_0(S)}a_p(U)
 \ge\min\left\{\tfrac18\sum_{p'\in S}
       f_{\mathcal M^tU}(p')^2,\ e_*\right\}.
 \tag{6.5}
\]

If the left side is at most $e_*$, the induction proves the first alternative; otherwise the second gives the inequality. In particular a prescribed stored coarse plaquette of size $\varepsilon$ forces a fixed multiple of $\varepsilon^2$ at every compatible evaluation, once $\varepsilon^2\le8e_*$. Taking a fibre supremum cannot remove this cost, because compatibility fixes that coarse plaquette. A flat field with that prescribed nontrivial average is impossible by (6.5).

The remaining conversion of a failed **localized-background** plaquette test into such a coarse plaquette uses its quantitative existence/regularity theorem; totality alone is insufficient when a test fails because an object is undefined. Approximate-fluctuation tests additionally require the gauge/rigidity estimate, and fluctuation/collar tests require the actual cut lower bound. These are distinct uses: positivity of the main-step curl square $Q$ supplies none of them.

## 7. Terminal attack and recovery checkpoint

The completed statements in this continuation are (3.5)–(3.6), comparing the complex denominator directly to its actual real reference law; Lemma 3.2, transferring a uniform real derivative tail to a smaller complex chart; (4.3), the lower bound for the carrier cut from an absolute carrier moment, with the specified flat specialization (4.4); the local normalization prices (5.1)–(5.2); and the all-compatible real-field energy inequality (6.5). The full $Q$ and the field-dependent denominator have remained intact throughout. These are written arguments, not computational certificates.

The last reference attack followed Proposition 2.4 back to its proposed axial Hessian argument. The one-step pivot chart proved in `a2-curved.md` supplies local elimination; the next-fibre gap in `a2-full.md` supplies a different constrained Hessian. Neither identifies the Hessian when **all** reference-box averages are freed and only exterior averages remain fixed. A finite tree curl inequality alone does not identify that reduced Hessian. This route therefore did not construct the uniformly admitted joint reference branch needed by Section 3. On the cut side, the flat local-model expansion supplies the absolute moment, but the curved conjugation bounds in `a2-layers.md`, Section 7.2, bound the summed operator; replacing them by an absolute bound for its specified carrier series would be exactly the inference refuted by the signed-carrier example in Section 4. No violation of the literal cut was found.

For the remaining consumers, I inspected the renewed-wait argument SA L18334–18415 against `floor-screen.md`, Theorem R, and the repairs in `gates/floor-screen-gate.md`, Sections 1–5. Equation (6.5) gives its energy-of-averages input on a supplied ancestor neighborhood; it does not identify every actual stage read with that neighborhood. I also followed the healed restriction/assembly at SA L17951–17997, L18877–18943 and L19066–19111. The formal commutation argument reads disjoint **complete** read sets, including reference laws, and the normalization reads the actual identical vacuum slots. The unconditional positive-kernel mass identity would only bound by the unnormalized bare mass, so it cannot replace this step by itself. I have not claimed that the conditional forest theorem or a generic polymer expansion settles it.

**Exact remaining obligation (one paragraph).** First construct, for every admitted pair of the actual main operation, the joint critical reference chart and uniform real slice used in Lemmas 3.1–3.2; prove the complete complex-pair remainder bound $\sup_p|V_X|\le C N_0$ on the actual prepared/inner substitutions. For the stored precision, establish (4.1) for the actual curved carrier series with its gauge and pivot conventions. Then the approximate-fluctuation and renewed-mark tests still need their quantitative rigidity/admission and owned-neighborhood identifications on every compatible fibre, and hypothesis 3 still needs the exact healed restriction and formed regular-activity subtraction. These are not discharged by the smaller statements above; consequently the result is **STOPPED**, not PROVED or REFUTED for row 117.

Sources remain the pinned checkout and the single fetched outline identified in Section 1. All reads used bounded ranges; the predecessor `sa-2.13.md` was read in full as requested, together with the two required consumer Section 7s. The additional source ranges are identified beside their uses above. No independent reviewer was run, and no source theorem gains status from this note. Only `library/sa-2.13-2.md` is changed in the repository; no editable prompt file is changed. The next attack should start at the joint reference chart just specified or the curved absolute carrier moment, not repeat the forest count or the real product-ball bound.
