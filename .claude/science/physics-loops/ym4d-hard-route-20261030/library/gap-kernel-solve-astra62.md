# Repo search

This row uses the closed-folder restriction. The source check covers `Stage0.lean`, `Final.lean`, and §§1.4–1.5 of `gap-mech-direction4-fable.md` at the requested checkout. The cross-ref search and the prior-work files fall outside that restriction.

**CITED — source hits.** The ref inspected was `HEAD = 9a626d7f6cdf`. The wider refs `origin/main`, `pr/10114`, `pr/10133`, `pr/10134` and `pr/10141` were skipped under the later three-file instruction. Priority outside that scope is undetermined.

| Terms | Source | What the hit supplies |
|---|---|---|
| `RankOneAtTime`, `NeutralRankOneTest`, `MNeutralAll` | `lean/gapchain/GapChain/Stage0.lean` 70–80, 150–169 | The neutral projection averages eight centre actions. At every sufficiently large integer cutoff, on **every** cube of side $\ell L^K$, one needs a unit vector and a positive scalar with HS error at most $2/5$ at some $1\le w\le\lfloor\ell L^K/1024\rfloor$. The same positive multiple of four $\ell$ works throughout. |
| `latticeU`, `ExpClusters`, `FixedObservableWitnesses`, `betaAt` | `Stage0.lean` 208–241, 296–340 | For each finite positive-time test combination, arbitrarily late witness cutoffs must bound the truncated reflected correlation at **all** positive odd mesh times. The prefactor can depend on the test and cutoff. The rate is common. The witnesses give moment limits and $\beta_j/(K_j\log L)\to11/(3\pi^2)$. This last limit is stated along the witnesses. |
| `massGap_of_expClusters`, `su2_fixed_observable_gap_of_mNeutral` | `lean/gapchain/GapChain/Final.lean` 48–80, 84–88 | `Final` uses the proved stages. A positive clustering rate gives the reconstructed gap and a unique vacuum. An eventual neutral test gives the rate $(2/\ell)\log(2^{18}/5041)$ at the witnesses already chosen. The trusted axioms reported for the conditional export are `propext`, `Classical.choice` and `Quot.sound` (given in the task). |
| `Lemma ALG`, `(g1)`–`(g6)` | `library/gap-mech-direction4-fable.md` 180–196 | A condition constant on a class that contains a seedless product cannot both hold on that class and imply the seed. The six tests also require a law-dependent failure line, a scale and a carry through order-one coupling. |

The method terms `Dobrushin`, `Hamming`, `heat bath`, `boundary influence` and `path coupling` had zero text hits in the permitted sources.

**CITED — credit.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the fixed-observable release (`3932084a9b82` in `Stage0.lean` 9–15). Tadeusz Bałaban developed the multiscale lattice gauge method. The new deductions are paper proofs. The stated axiom report concerns the existing conditional export. No new Lean check or numerical job was run. This research note grants no audit status.

## One finite-box estimate

**PROVED below, conditional.** One estimate on two conditional Wilson measures implies `ExpClusters` at the fixed witnesses. It uses the plaquette density in a box of one length and the cost of changing one exterior link.

Use positive oriented links of the unit lattice. Write $d=4$, keeping $d$ in the counts for the tests. Let $B_R$ contain all links with source in $\{0,\ldots,R-1\}^d$. It has $dR^d$ links. Fix the exterior links to $\xi$. Denote the law of the links in the box by $\gamma_R^\xi$. Its density against product Haar is proportional to

$$
 \exp\left(\beta\sum_{p:\,p\cap B_R\ne\varnothing}
                    \tfrac12\operatorname{ReTr} U_p\right).
$$

The sum includes every plaquette with a link in the box. This is the one-geometric-plaquette convention of `Stage0.lean` 95–106. Only one layer of exterior source sites can enter the density. Write $s_R=(R+2)^d-R^d$ for its site count, including unused sites.

For two laws on the box, let $W_H$ be the infimum, over all couplings, of the expected number of unequal links. Let $Q_R(\beta)$ be the supremum of $W_H(\gamma_R^\xi,\gamma_R^{\xi'})$ over exterior data that differ on just one link. All the data in this supremum fit in a finite box. The cost concerns a **joint** coupling of the interior links.

**GUESSED — the one open estimate (E).** At the given witnesses put $k_j=K(j)$, $a_j=L^{-k_j}$ and $\beta_j=\mathrm{betaAt}(L,M,k_j,g_0)$. There exists an integer $b\ge1$ such that, for arbitrarily large $j$,

$$
 R_j=bL^{k_j},\qquad Q_{R_j}(\beta_j)\ \le\ \frac{R_j^4}{4\big((R_j+2)^4-R_j^4\big)}. \tag{E}
$$

The right side grows as $R_j/32$. Thus a bounded change at the boundary may cause a growing number of disagreements. The estimate asks for their total cost. The same $b$ must work at all the chosen cutoffs. It may depend on the calibrated theory.

**CITED — method.** The block comparison uses the total influence of one changed variable under coupled updates. This is the Dobrushin–Shlosman criterion in the form discussed by Dror Weitz, *Combinatorial criteria for uniqueness of Gibbs measures*, Random Structures & Algorithms **27** (2005), 445–475, Definition 2.6 and Theorem 2.7. The proof here gives the constants and the correlation rate for compact link variables. [Weitz, full text](https://www.ias.edu/sites/default/files/math/csdm/04-05/dweitz_combinatorial_criteria_for_uniqueness.pdf)

## From the box to odd-time clustering

**PROVED — finite-volume comparison.** Work on a periodic lattice with side greater than $2R+2$ and $V$ sites. Write $\mu$ for its Wilson law. Suppose $s_R Q_R/R^d\le1/4$. For bounded local functions $F,G$, let $A,Y$ be the sets of source sites of their links. For nonempty supports, in lattice units,

$$
 |\mu(FG)-\mu(F)\mu(G)|
 \ \le\ 8dR^d |Y|\,\|F\|_\infty\|G\|_\infty\,
            2^{-\operatorname{dist}_\infty(A,Y)/R}. \tag{1}
$$

Constant functions give zero covariance. Distances on the torus use the periodic metric.

*Proof.* Let $P_D$ average over the links in a translate $D$ of the box, conditional on the exterior. Let $P=V^{-1}\sum_D P_D$. Give a link with source $x$ weight $u_x=2^{-\operatorname{dist}_\infty(x,A)/R}$. Use the sum of these weights over unequal links as a distance. Write ${\rm Lip}_u$ for its Lipschitz seminorm. One-link changes suffice to bound the seminorm. Change the unequal links one at a time.

Start two configurations with a single difference of weight $u_x$. Exactly $R^d$ translates contain that link. In each, an identical draw erases it. For a translate with $x$ beyond both the box and its shell, the inside draws can also agree. At most $s_R$ remaining translates can spread the change. Every link there has weight at most $2u_x$. The definition of $Q_R$ bounds the added expected weight by $2u_x Q_R$, taking the infimum over joint draws. The old difference persists in the exterior. Hence

$$
 {\rm Lip}_u(PH)\le q\,{\rm Lip}_u(H),\qquad
 q=1-\frac{R^d-2s_RQ_R}{V}\le1-\frac{R^d}{2V}. \tag{2}
$$

The finite torus has finite weighted diameter. Equation (2) and invariance of $\mu$ give uniform convergence of $P^hF$ to $\mu(F)$. Telescope $F-\mu(F)=\sum_{h\ge0}(I-P)P^hF$. In the covariance, the term for a box disjoint from the links of $G$ has zero integral by conditional expectation. At most $|Y|R^d$ translates remain. In each, the sum of the interior weights is at most $2dR^d 2^{-\operatorname{dist}_\infty(A,Y)/R}$. Multiply this by ${\rm Lip}_u(P^hF)\|G\|_\infty$. Use ${\rm Lip}_u(F)\le2\|F\|_\infty$ and $\sum_h q^h/V\le2/R^d$. This proves (1), also for complex functions.

**PROVED — boundary conditions in the comparison tests.** On a torus of side $T$, change the interactions only at the seam to obtain a free box. Let $Y_T$ include all source sites of the changed interactions. For the new law $\tilde\mu$, form its update $\tilde P$. The same telescoping sum for $\tilde\mu(F)-\mu(F)$ now contains $\tilde\mu((\tilde P-P)P^hF)$, since $\tilde\mu\tilde P=\tilde\mu$. The two updates agree for blocks away from $Y_T$. The preceding oscillation bound gives an error at most $8dR^d|Y_T|\|F\|_\infty 2^{-\operatorname{dist}_\infty(A,Y_T)/R}$. For fixed $R,A$, place the seam a distance of order $T$ away. Its size is $O(T^{d-1})$, so the error tends to zero. Thus (1) also holds in local limits with free boundary. Fixed exterior data likewise change only interactions at the edge of the box. The error bound is uniform in those data.

**PROVED — use at the release witnesses.** Fix a good $j$ in (E). Bound (1) is uniform in the torus side. Pass it to the infinite-volume Wilson limit $\nu_j$ for fixed continuous cylinder functions. Their integrals and the integral of their product pass to that limit. This uses `Inputs.isLimit` before taking any continuum limit.

At fixed mesh, a compactly supported smeared action density is a bounded continuous function of finitely many plaquettes. A centred insertion subtracts its $\nu_j$-mean. For each list in $Z$, take the product of these insertions. Take their finite linear combination with coefficients $z_X$. In `latticeU`, the left list is reflected with conjugate coefficients and the right list is translated. Taking the real part of their covariance gives the pair’s real part in `Stage0.lean` 214–221 minus $|\mathrm{mean}|^2$. Indeed, the Wilson law preserves lattice translations and reflections. A reflection carries a scalar plaquette action to the action on the reflected plaquette, since reversal preserves the real trace. These symmetries pass from the tori to the limit. The link mirror and the parallel site mirror differ by one lattice translation in the reflected argument. At odd mesh times the shift is integral. Thus the two one-sided means multiply to the required $|\mathrm{mean}|^2$.

For this $Z,j$, the supports in (1) have distance at least $t/a_j-h_{Z,j}$, with a fixed finite allowance $h_{Z,j}$ for the test supports, plaquette links and mirror. Translation by $(2n+1)a_j$ preserves their sizes and sup norms. Since $a_jR_j=b$, (1) gives at every $n\ge0$

$$
 \mathrm{latticeU}(\nu_j,Z,(2n+1)a_j)
 \le C_{Z,j}\exp[-(\log 2)(2n+1)a_j/b]. \tag{3}
$$

The factor $2^{h_{Z,j}/R_j}$ belongs to $C_{Z,j}$, as do the fixed-cutoff smearing factors. The bound also covers overlapping supports at small times. The unbounded set of good $j$'s works for every $Z$. This proves $(E)\Rightarrow\mathrm{ExpClusters}(L,K,\nu,(\log 2)/b)$ with the required quantifiers.

## The first step at the target coupling

**PROVED — one class of boundary links costs at most seven.** Take a vertex $v$ in the source cube with exactly one coordinate zero. Let $f$ be the incoming link from outside on that axis. It is the only exterior link incident on $v$. If its value changes from $u$ to $u'$, apply the vertex gauge transformation with $h=(u')^{-1}u$ at $v$, and identity elsewhere. With the convention $U_{xy}\mapsto h_xU_{xy}h_y^{-1}$, this sends $u$ to $u'$. It fixes all other exterior links. It preserves each plaquette trace and product Haar measure. Draw from $\gamma_R^\xi$ and apply this map. The second draw has exactly law $\gamma_R^{\xi'}$. The draws differ on at most $2d-1$ interior links. In four dimensions this covers $4(R-1)^3$ boundary links at cost at most seven, at every $\beta$ and for every exterior assignment. The right side of (E) eventually exceeds seven.

**PROVED — what remains in the box.** An exterior link in no plaquette touching the box costs zero. For each remaining change at $f$, write $h_p=\tfrac12\operatorname{ReTr}U_p$ and keep the interior variable $U$ fixed. The exact first change of density is

$$
 \Delta_f(U)=\beta\!\sum_{p\ni f,\,p\cap B_R\ne\varnothing}
        [h_p(U,\xi')-h_p(U,\xi)],\qquad
 \gamma_R^{\xi'}(dU)=\frac{e^{\Delta_f(U)}}{\gamma_R^\xi(e^{\Delta_f})}\gamma_R^\xi(dU). \tag{4}
$$

Cancel the common plaquette weights and normalize. Write $\delta=\|f'-f\|_{\rm op}$ for the distance between the old and new link matrices. Each real half-trace in (4) changes by at most $\delta$, since every other factor is unitary. At most $2(d-1)$ plaquettes enter. The two densities have common mass at least $e^{-4(d-1)\beta\delta}$. Couple their common part identically. This costs at most $4d(d-1)R^d\beta\delta$. Thus, at the target coupling itself, all changes with $16d(d-1)\beta s_R\delta\le1$ meet (E)'s threshold.

**PROVED — a tangential change that alters holonomy.** Choose $v=(0,1,\ldots,1)$ and $R\ge3$. The exterior link in direction $d$ from $v-e_1$ belongs to exactly one plaquette that touches the box. Write $a,b_1$ for the two fixed links entering the lower face, $f$ for the exterior tangential link and $u$ for the parallel interior link from $v$. This plaquette has transport $a u b_1^{-1} f^{-1}$. In (4) the likelihood ratio therefore depends only on $u$. If its marginal is $\rho$, the new marginal is $e^{\Delta_f(u)}\rho/\rho(e^{\Delta_f})$. Both laws have exactly the same conditional distribution on the rest of the box given $u$. Coupling the two marginals first gives identical interiors whenever the two $u$'s agree. A change from identity to a nonidentity $f$, with the other exterior links identity, changes an exterior loop trace. A vertex gauge change preserves that trace. The open part of (E) includes the transport of the conditional interiors when the two $u$'s differ.

**PROVED — a regime where the full box estimate holds.** Put $D=6(d-1)$ and $p_\beta=1-e^{-4\beta}$. Each link has at most $D$ neighbours that share a plaquette. When one neighbour changes, just one plaquette in the one-link conditional density changes. Its log weight changes by at most $2\beta$. Normalization gives a density ratio at least $e^{-4\beta}$. Couple the common part of the densities identically. The probability of a mismatch is at most $p_\beta$. A sequence of one-neighbour changes gives the sum of these bounds by the triangle inequality for total variation.

Take two box laws with the single exterior mismatch. Start with any coupling of them. Resample one uniform interior link in both copies with a maximal coupling of its two conditional laws. Each marginal stays stationary. If $H$ is the old number of mismatches and $N=dR^d$, the expected new count, conditional on the two old configurations, is at most

$$
 \left(1-\frac{1-Dp_\beta}{N}\right) H + \frac{Dp_\beta}{N}.
$$

Indeed, resampling erases the old mismatch at the chosen link. Each internal mismatch and the one exterior mismatch can enter at most $D$ new conditional bounds. Iterate and take the infimum over couplings. If $Dp_\beta<1$, then $Q_R\le Dp_\beta/(1-Dp_\beta)$, uniformly in $R$. Hence all large boxes meet the threshold. This calculation covers strong coupling. The witnesses have $\beta_j\to\infty$.

For the circle Villain weight defined below, divide by its Haar average. Its Fourier series is $1+2\sum_{k\ge1}e^{-k^2/(2\beta)}\cos(ks)$. Integrating the wrapped Gaussian over one period unfolds each coefficient to the Gaussian integral on the line. The series tends uniformly to one as $\beta\downarrow0$. Thus the one-neighbour conditional density ratios tend uniformly to one. The same recursion applies with a mismatch bound that tends to zero.

## Obstruction for sums of one-link influences

**PROVED — scope of the negative.** In every fixed $d\ge3$, consider certificates of the following form. For adjacent links $e,g$ the weight is at least $c_{eg}$, the supremum of the one-link total variation at $e$ when only $g$ changes in the conditioning data. Start a message of size one at the changed exterior link. Propagate by adding nonnegative incoming messages times their weights. Allow clipping to one at each link. Use the sum of endpoint messages as an upper bound for the expected mismatch count. It suffices that the certificate includes the monotone paths below. This covers summing all self-avoiding paths with these weights and grouping such positive sums into longer steps.

For Wilson $SU(q)$, $q\ge2$, and Wilson or Villain $U(1)$, there are constants $\beta_{d,G},R_d,c_d'>0$ such that for every $\beta\ge\beta_{d,G}$ and $R\ge R_d$, each such certificate charges at least $c_d'R^{d-1}$ for one specified exterior link. This is true both for the incoming link just treated and for a tangential link that can change exterior holonomy.

*Proof, local weight.* Set all conditioning links to the identity. A tested link sees $p=2(d-1)$ identity staples. A staple is the three-link path around the rest of a plaquette. Change one neighbour so that exactly one staple becomes $V=\operatorname{diag}(e^{i\theta},e^{-i\theta},1,\dots,1)$, with $0<\theta<\pi/4$. For $U(1)$ take $V=e^{i\theta}$. An inverse amounts to changing the sign of $\theta$. Up to a common positive factor and additive constants, the two log densities are $\operatorname{ReTr}(U pI)$ and $\operatorname{ReTr}(U[(p-1)I+V])$. For a diagonal matrix with nonzero entries $z_i$, the upper bound $\sum|z_i|$ requires $U_{ii}=\bar z_i/|z_i|$ for all $i$. This gives a unique maximizer, in $SU(q)$ here. The two maximizers differ. As $\beta\to\infty$, the probability outside any neighbourhood of a maximizer tends to zero. Compare its weight with a smaller neighbourhood on which the exponent is strictly larger. Thus $c_{eg}\to1$, also for a pair of perpendicular links.

For Villain $U(1)$ use $w_\beta(s)=\sum_{n\in\mathbb Z}\exp[-\beta(s-2\pi n)^2/2]$. For $\beta\ge1$, the nearest Gaussian term bounds $w_\beta$ below and a constant times that term bounds it above, uniformly in $s$. On $[-\pi,\pi]$, the terms with $|n|\ge2$ have relative size at most $e^{-2\pi^2|n|(|n|-1)}$. The initial conditional concentrates at angle zero. After the change the rate function, up to a constant factor, is $(p-1)\operatorname{dist}(s,0)^2+\operatorname{dist}(s,\theta)^2$ on the circle. Its value at $\theta/p$ is smaller than its value at zero. The minimizing set is compact and excludes zero. The same disjoint-neighbourhood argument gives $c_{eg}\to1$.

**PROVED from a CITED bound — heat-kernel Villain $SU(2)$.** Use unit quaternions with their round metric and plaquette weight $K_t(U)$ at $t=1/(2\beta)$. Uniformly on the group, $-4t\log K_t(U)\to\operatorname{dist}(I,U)^2$. This follows from A. Nowak, P. Sjögren and T. Z. Szarek, *Sharp estimates of the spherical heat kernel*, J. Math. Pures Appl. **129** (2019), 23–33, Theorem 1 on $S^3$. Its prefactors contribute $O(t|\log t|)$ after multiplying the logarithm by $t$. After one staple changes, the rate function is $(p-1)\operatorname{dist}(U,I)^2+\operatorname{dist}(U,V)^2$, choosing the orientation of $V$. At the point a fraction $1/p$ along a shortest geodesic from $I$ to $V$, its value is $(1-1/p)\operatorname{dist}(I,V)^2$. This is less than its value at $I$. The same concentration proof gives $c_{eg}\to1$ and hence the path obstruction below. [Nowak, Sjögren and Szarek, Theorem 1](https://arxiv.org/pdf/1802.09385)

*Proof, path count.* Put $v=(0,1,\ldots,1)$ and start the interior paths at $e=(v,d)$, the link along axis $d$. Either exterior link $f=(v-e_1,1)$ or $f=(v-e_1,d)$ shares a plaquette with $e$. Here $e_i$ denotes the unit step on axis $i$. The second $f$ belongs to a loop entirely in the exterior face $x_1=-1$. Fix $c=2^{-1/(2d)}$. The local proof gives every required weight at least $c$ for all sufficiently large $\beta$. The initial interior message is at least $c$.

Keep links parallel to axis $d$ and move in the $p'=d-1$ positive transverse directions. Each unit move crosses one plaquette. A step of length $d$ takes one unit on each transverse axis and an extra unit on a chosen axis $i$. There are two internally disjoint paths with these endpoints. On one, take both $i$-moves first. On the other, take both last. A message $u\in[0,1]$ therefore gives an endpoint message at least $\min(1,2c^d u)$, even with clipping at every intermediate link. Since $2c^d=\sqrt2>1$, after a fixed number $k_d$ of such steps every reachable endpoint is charged one.

After $k$ steps the endpoint has transverse displacement $(k+n_1,\ldots,k+n_{p'})$, where the $n_i$ are nonnegative and sum to $k$. Each such endpoint occurs. Different $k$'s have different total displacement. All paths stay in the box for $2k\le R-2$. Thus the charged count is at least

$$
 \sum_{k=k_d}^{\lfloor(R-2)/2\rfloor}\binom{k+d-2}{d-2}.
 \tag{5}
$$

For fixed $d$ this grows as a positive constant times $R^{d-1}$. The allowable cost $R^d/(4s_R)$ is at most $R/(8d)$ by the binomial theorem. In four dimensions (5) grows cubically. For the incoming link its exact transport costs at most seven. For the tangential link (5) rules out the same certificate after the incoming links have been removed from the task. The optimal transport for that tangential link stays open. Since both $R_j$ and $\beta_j$ diverge, (5) applies along every sufficiently late witness for each fixed $b$.

**PROVED — an order-one check on the single-link method.** At $\beta=1$ the scalar Dobrushin row sum already exceeds one for four-dimensional Wilson $SU(2)$. Fix a link and any one of its 18 neighbours. The five other staples use disjoint conditioning links. Give three staples the diagonal phases $1,e^{2\pi i/3},e^{-2\pi i/3}$ in one matrix entry and the conjugates in the other. Give the last two staples values $I,-I$. Their matrix sum is zero. Flip the tested staple from $I$ to $-I$ by changing only the chosen neighbour. The two conditional densities are proportional to $e^{h}$ and $e^{-h}$, with $h=\operatorname{Tr}U/2$. Haar symmetry gives their total variation as $\int |\sinh h|/\int\cosh h$, with both integrals under Haar. It exceeds $1/8$. Indeed $|\sinh h|\ge h^2$, $\cosh h\le\cosh 1<2$, and $\int h^2=1/4$ since $h$ is one of four equal-variance coordinates of a uniform unit quaternion. The row sum exceeds $18/8$. This check concerns the scalar row sum. The clipped-path theorem (5) has its own large-$\beta$ range.

## Why (E) is a stronger input

**PROVED — no converse from action-density clustering.** Here is a four-dimensional, axis-symmetric example with positive local weights. It tests the logic of the reduction. On each coordinate line put an independent zero-field Ising chain for links parallel to that line. At mesh $a\downarrow0$ take $\tanh J_a=e^{-a^2}$. Choose the spin at the origin uniformly. The successive bond signs in both directions are independent, with mean $\tanh J_a$. To see this, normalize the transition weights $e^{J_a ss'}$ over $s'=\pm1$. The distribution of the sign $ss'$ is independent of $s$. The local actions depend only on these bond signs. All their compactly supported test products therefore factor at disjoint bond supports. Their truncated time correlations meet the analogue of (3) at any fixed positive rate. On a finite circle, condition the product of the bond signs to be one. Its effect on a fixed finite set tends to zero as $(\tanh J_a)^{T-O(1)}$ for side $T\to\infty$.

Two spins $n$ links apart on one line have covariance $(\tanh J_a)^n=e^{-a^2 n}$. For any fixed $b$, (1) with $R=b/a$ would bound this by a finite cutoff-dependent constant times $e^{-(a\log2)n/b}$. Take $a<(\log2)/b$ and then send $n$ to infinity. This is impossible. Here all four axes have the same law and the local energy is nonconstant. If one keeps only the spatial chains, time slices are independent and the time transfer is an outer product. The same spatial contradiction applies. One can also adjoin independent Haar $SU(2)$ links and take the Ising variables to be gauge singlets. Disjoint local action tests still factor and the two-spin covariance is unchanged. These examples establish strictness for local models. Applying (E) to pure isotropic Wilson $SU(2)$ is the open step.

## Six tests

- **(g1) PROVED from a CITED input.** In weak four-dimensional compact $U(1)$, the failure line for the box threshold is (1). It gives one positive rate, in all directions, for every bounded local observable at that lattice spacing. In a reflection-positive state, a centred local vector with positive transfer spectral weight above $2^{-1/R}$ would violate (1) at large even time. A closed interval above that threshold with positive spectral weight gives a lower exponential bound with a slower rate. Local vectors are dense in the reconstruction. This excludes a massless photon. In the Villain representation with a plaquette integer, the conditional mean of the lifted field at a plaquette is $-\beta^{-1}(\log w_\beta)'$, a bounded local function of the compact angle. Integers at distinct plaquettes are conditionally independent. Its separated field covariances equal those of the bounded conditional means. The massless phase is the input in §1.5(g1), as proved by J. Fröhlich and T. Spencer, *Massless phases and symmetry restoration in abelian gauge theories and spin systems*, Commun. Math. Phys. **83** (1982), 411–454. The one-link certificate itself fails at (5) for both Wilson and Villain actions. [Fröhlich and Spencer](https://link.springer.com/article/10.1007/BF01213610)
- **(g2) ARGUED for the box, PROVED for the certificate.** In five-dimensional weak $SU(2)$, (1) would again exclude local gapless modes. Their existence is a belief in §1.5(g2), so failure of the box threshold there stays open. The proof of (5) does apply. It gives a fourth power of $R$ in five dimensions and a third power in four. This dimensional dependence rejects the one-link method in both models.
- **(g3) PROVED for the coupling comparison.** For Wilson and Villain $U(1)$ in four dimensions and Wilson $SU(2)$ in five, the small-$\beta$ coupling above makes all sufficiently large boxes pass. For weak three-dimensional Villain $U(1)$, line (5) charges at least a constant times $R^2$. It therefore fires on the gapped twin specified in §1.5(g3). The path failure thus occurs on both sides of the phase comparison. The primary three-dimensional result includes a positive string tension at every coupling and a massive scalar scaling limit. M. Göpfert and G. Mack, *Proof of confinement of static quarks in 3-dimensional U(1) lattice gauge theory for all values of the coupling constant*, Commun. Math. Phys. **82** (1982), 545–606. [Göpfert and Mack](https://link.springer.com/article/10.1007/BF01961240)
- **(g4) PROVED for the product, ARGUED for the other examples.** Change just a massless spectator link in a decoupled product. Project any joint box coupling to this factor. Its expected Hamming cost can only decrease. Thus the product's $Q_R$ is at least the spectator's, for the same box, and (g1) excludes the product. This is the law-dependent failure required by Lemma ALG. For the K7 endpoint and the adjoint-Higgs Coulomb example, the corresponding exclusion by (1) depends on a gapless local sector for the full law. Section 1.5(g4) labels those inputs beliefs. Their test verdict remains conditional.
- **(g5) PROVED.** The block side in lattice links is $N(\beta_j)=bL^{k_j}=\exp[(3\pi^2/11+o(1))\beta_j]$, by `Stage0.lean` 303–309. At any fixed torus side the required box eventually cannot fit. In physical units its side is the fixed $b$. This scale statement is along the named witness cutoffs.
- **(g6) PROVED for the implication and its loss, OPEN (GUESSED) for the box coupling.** The input $Q$ is joint one-link boundary influence in a box. The consumer $C$ is the translated block heat bath (2) followed by (3). Weighting a crossing costs a factor of two. The threshold leaves at least $R^d/(2V)$ contraction per update and gives the physical rate $(\log 2)/b$. The Ising-line example disproves a general converse. Gauge transport proves the seven-link bound at every bare coupling. The $\beta=1$ row-sum check also concerns the bare Wilson law. Control of the remaining boundary changes through an order-one blocked action stays open. The local maximizer and path proofs include Wilson $SU(3)$, circle Villain and heat-kernel Villain $SU(2)$. Each has the same obstruction at weak coupling. This is a conditional reduction and a negative result for the specified certificates.

RESULT: PROVED (E) implies ExpClusters at rate (log 2)/b, seven-link transport for one boundary class, and a lower bound proportional to R³ for the specified positive one-link path sums in 4D. The first open estimate is (E) for the remaining finite boundary changes at calibrated SU(2). g1 excludes weak U(1), g2 is conditional for 5D, g3 rejects the path test on a gapped twin, g4 excludes the massless product with the other endpoints conditional, g5 passes at exponential scale, and g6 has a proved consumer with the order-one carry open.
