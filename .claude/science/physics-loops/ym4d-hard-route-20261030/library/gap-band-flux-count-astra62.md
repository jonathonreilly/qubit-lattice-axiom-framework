## Repo search

FINISH 1591, research at `b15ff41cd`. The target-specific prior is absent. The November 8 inventory covers thirteen UV and witness questions. The registry assigns TWO-PER to the variation of neutral purity with coupling and contains no matching short-arc row. [Prior inventory](prior/repo-search-2026-11-08.md) · [Open registry](open-registry.md)

The five search refs are `origin/main` (`8b11ae2bb`), `pr/10114` (`f76f6c649`), `pr/10133` (`89faef229`), `pr/10134` (`1e70c7211`), and `pr/10141` (`c73ad7b17`). The bounded Markdown/TeX search across all five returned no hits for literal `(N-flux)`, ambiguous Wilson arcs or bridges, exposed ambiguity, arc-sign bias, seam-sign balance, alternating Wilson pins, killed arc or bridge kernels, or disseminated bad arcs. The corresponding search outside the lane in this checkout also found no target. Broad seam-sign and flux-count searches hit unrelated staggered-model and finite-register notes. The tile inequality and common twisted interpolation led to the first two entries below. Follow-ups for isospectral seam or odd-sector examples, Schatten estimates on ambiguous arcs, noncommuting plaquette pairs, and gauge-orbit distance to a centre translate returned no hits on those five refs.

| Source | Statement and distance to the target |
|---|---|
| Main, `research/mass-gap/library/gap-crux-restate.md`, Thm F, lines 234–248 | For fixed transverse sides, the bulk-normalized odd mass obeys $v(ja,kb)\le v(a,b)^{jk}$, and the odd probability is at most $v$. The estimate needs a starting tile with $v<1$ for area decay. It concerns integrated masses, whereas (1) counts events on pinned arcs with growing transverse sides. |
| PRs 10114 and 10133, `ym4d-proof/checks/review_massgap_block_literature.md`, lines 111–121, cited on main in `research/mass-gap/library/gap-form-exercise.md`, line 329 | The Ito–Seiler discussion distinguishes flow to strong coupling from the existence of a common interpolation parameter for the twisted and ordinary partition functions. Neither obligation estimates the distribution of middle pins. |
| [Check 1585, §(v)](gap-band-direction5-check-astra62.md) | A polynomial lower tail for the number of ambiguous short arcs implies a polynomial one-axis odd/even trace bound. A conditional success probability at least $\eta\log n/m$ at every indicator history suffices. Its two-state example has small flux and zero ambiguous arcs. |
| [Row 1587](gap-band-flux-tail-astra62.md) and [check 1589, steps 2, 4, 7](gap-band-flux-tail-astra62-check-opus.md) | The lower-tail probability is at most eight times the mean squared arc bias. This upper bound is strictly stronger. At fixed pins the erasure argument leaves both freedom of the seam sign and balance of the two fixed signs unestimated in the band. |
| [Row 1588, §§2, 4.1–4.3](gap-band-flux-tail-neon.md) | The row studies one-arc marginal overlap and short-period traces, notes the possible bias from conditioning on a long failure history, and tests seam spreading and centre-coset locking. It leaves the Wilson count open. None of its estimates is assumed below. |
| [Row 1141, (3)–(4)](gap-crux2-astra62.md) and [row 1587, proof of (7)](gap-band-flux-tail-astra62.md) | Two local plaquettes displace every adjoint axis by a fixed amount with conditional probability at least one half in the stated squared-displacement test. The joint density of straight winding transports approaches one relative to product Haar in row 1587. These are different inputs for pricing a gauge match in §4. |
| Sussman and Alpoge, with Claude and Codex, supplied source snapshot `31a47c543775` | Index chunks 02–03 and the obligations point to the Wilson conditional weight at outline 2094–2110, the trace Hölder inequality for sparse contraction insertions at 2354–2381 (GL10), and the reflected Gram form and equal-slab comparison at 2862–2905 (AM5–6). CA-II 62497–62515 bounds a localized source partition function with sources strictly inside cells. The arc event here depends on both full faces. No ambiguity-count row was located in those indices. |

## Plan

1. Record the exact scope and hypotheses of the existing flux-count results, including what is still open on the Wilson seed tori.
2. Fix the arc law, the constants and the quantifiers from the source. Attack the probability of a low count directly. If a single Wilson estimate remains, test it by three distinct arguments.
3. State what follows for the three-axis flux bound, what is proved about selectivity, and what remains open for neutral purity. Use exact reasoning throughout.

## The count at the two periods

Fix the odd release factor $b$, calibration level $g_0$, and side $\ell\in1024\mathbb N$, and let $n=\ell b^K$, $u=n/512$. This note tests the **bare** Wilson law at every $\beta\in[2,3]$, at $d=n/512$ and $d=n/256$. Take $m=\lfloor\sqrt d\rfloor$ and the prescribed arc lengths $t_j\in\{\lfloor d/m\rfloor,\lceil d/m\rceil\}$ summing to $d$. All arguments below allow any order of these lengths and all sufficiently large $n$. Write $C$ for one spatial centre cut and $P_{e,o}=(I\pm C)/2$ on the gauge-invariant space. With normalized raw-slice Haar measure $dx$, the ordinary cylinder kernel $K_t$ includes the temporal gauge integration and the two spatial end actions at half weight. It is continuous, strictly positive, symmetric, and $K_t(Cx,Cy)=K_t(x,y)$.

Put $A_t(x,y)=(K_t(x,y)+K_t(x,Cy))/2$, $B_t(x,y)=(K_t(x,y)-K_t(x,Cy))/2$, $b_t=B_t/A_t$ and $Z_e(d)=\operatorname{Tr}(P_eT^d)$. The kernels $A_t$ compose to $A_{s+t}$ by the commuting projection. The even pin law is
$$
 d\mu=\frac1{Z_e(d)}\prod_{j=0}^{m-1}A_{t_j}(x_j,x_{j+1})\prod_{j=0}^{m-1}dx_j,\qquad x_m=x_0 .
$$
Let $G_j=\mathbf1_{\{|b_{t_j}(x_j,x_{j+1})|\le1/2\}}$ and $N=\sum_jG_j$. The one open Wilson lemma attacked here is
$$
 \exists c,\epsilon,C_0>0,\ n_0:\quad
 \mu(N<c\log n)\le C_0n^{-\epsilon}
 \quad(n\ge n_0,\ 2\le\beta\le3,\ d\in\{n/512,n/256\}). \tag{1}
$$
The logarithm is natural. The calibrated $\beta_K$ eventually leaves the band. The seed uses the simultaneous neutral projection $P_0=\prod_{i=1}^3[(I+C_i)/2]$. It asks for $Z_+(2u)/Z_+(u)^2\ge457/625$ at infinitely many calibrated cutoffs, with $Z_+(v)=\operatorname{Tr}(P_0T^v)$. [Check 1585, §(v)](gap-band-direction5-check-astra62.md) · [Wilson cylinder convention, row 1573](gap-band-neutral-astra62.md) · [Seed, §3.1](gap-k2-tool-design-fable.md)

## 1. Conditional independence after exposing alternate pins

Pair arcs $(0,1),(2,3),\ldots$ and set $k=\lfloor m/2\rfloor$. Reveal their outer pins. For odd $m$ this includes both ends of the single unpaired arc. Write $\mathcal A$ for this information. In a pair of lengths $s,t$ with outer pins $x,z$, the middle pin has conditional law
$$
 \nu_{x,z}^{s,t}(dy)=\frac{A_s(x,y)A_t(y,z)}{A_{s+t}(x,z)}\,dy . \tag{2}
$$
The $k$ middle pins are conditionally independent. Indeed each appears in exactly its two displayed factors of the cyclic density, and each normalizer is their integral. This holds also across the closing pin.

Write $D_s(x,y)=A_s(x,y)\mathbf1_{\{|b_s(x,y)|>1/2\}}$. The conditional probability $q_i$ that pair $i$ contributes at least one ambiguous arc is
$$
 q_i(x,z)=1-\frac{(D_sD_t)(x,z)}{A_{s+t}(x,z)},\qquad M=\sum_{i=1}^k q_i. \tag{3}
$$
Here $D_sD_t$ denotes kernel composition. Let $J$ be the number of pairs contributing. Given $\mathcal A$, $J$ is a sum of independent Bernoulli variables with means $q_i$. In particular $J\le N\le 2J+1$. For $\alpha=1-e^{-1}$ and $a,c>0$,
$$
 \mu(N<c\log n)\le \mu(M<a\log n)+n^{\,c-\alpha a}. \tag{4}
$$
Apply Markov on $M\ge a\log n$ using $\mathbb E(e^{-J}\mid\mathcal A)=\prod_i(1-\alpha q_i)\le e^{-\alpha M}$. Conversely, if $M\le(c/8)\log n$, then $\mathbb E(N\mid\mathcal A)\le (c/4)\log n+1$. Conditional Markov gives $\mu(N<c\log n\mid\mathcal A)\ge1/2$ there for $c\log n\ge4$. Thus
$$
 \mu\big(M\le(c/8)\log n\big)\le 2\mu(N<c\log n). \tag{5}
$$

Equations (4)–(5) make the two lower tails equivalent after changing the constants. Middle-pin fluctuations can be integrated exactly, but the distribution of $M$ under the outer-pin law remains open. This equivalence leaves (1) open even when some of the $q_i$ are large.

## 2. A Wilson bound valid after any indicator history with one pin still free

For all outer pins $x,z$, all $s,t\ge1$, and a middle pin with law (2), the first arc of the pair satisfies the explicit estimate
$$
 \nu_{x,z}^{s,t}(|b_s(x,Y)|\le1/2)
 \ \ge\ p_{n,\beta}
 :=e^{-3\pi\beta n^2}\min\!\left\{1,\frac{\log3}{\pi\beta n^2}\right\}. \tag{6}
$$
The integration variable is a raw slice. Use the half-turn of the cut from row 1568. Choose any fixed unit imaginary quaternion $J$ and left-multiply each of its $a=n^2$ cut links by $\cos\theta+J\sin\theta$, leaving the other links fixed. This map $R_\theta$ preserves product Haar, and $R_{\theta+\pi}Y=CR_\theta Y$. Gauge projection is already inside $K_s$. Haar invariance on the raw slice suffices throughout the change of variables. [Cut rotation, row 1568, §1.1](gap-band-cut-covariance-neon.md)

For fixed $y$, put
$$
 L(\theta)=\log\frac{K_s(x,R_\theta y)}{K_s(x,CR_\theta y)},\qquad
 w(\theta)=A_s(x,R_\theta y)A_t(R_\theta y,z).
$$
Then $L(\theta+\pi)=-L(\theta)$, $w(\theta+\pi)=w(\theta)>0$, and ambiguity is $|L|\le\log3$. Counting the plaquettes touching the end gives two bounds uniform in the arc lengths and the other links.
$$
 |L'|\le2\beta a,\qquad |(\log w)'|\le6\beta a . \tag{7}
$$
To verify them, a varying occurrence of one cut link in a plaquette contributes at most one to the derivative of its normalized trace, since every other matrix is unitary and the generator has operator norm one. In either cylinder the end touches one temporal plaquette per cut link. Its spatial end action has four spatial incidences per cut link, all at half weight. Thus the log derivative of a cylinder is bounded by $(1+4/2)\beta a$ by differentiating the compact positive integral. An even sum has the same bound by weighted averaging. For $L$ the spatial end factor cancels *identically*, because the two boundary fields differ by $C$ and every spatial plaquette is centre-even. Only the $a$ temporal plaquettes in each integral remain. This proves (7).

Continuity and the half-turn give a zero of $L$, repeated modulo $\pi$. The proportion of the angle circle within distance $\log3/(2\beta a)$ of these zeros is at least $\min\{1,\log3/(\pi\beta a)\}$. Over one period of $w$ the shortest angular distance is at most $\pi/2$ between any two points, so $\min w/\max w\ge e^{-3\pi\beta a}$. These facts bound the $w$-weighted fraction of good angles from below by $p_{n,\beta}$. Integrating first over $\theta$ and then over $dy$ gives (6) by Haar invariance.

This is also a bound for the sequential experiment in check 1585. After exposing $x_0,\ldots,x_j$, the density of $x_{j+1}$ is (2) with $s=t_j$, $z=x_0$ and $t=\sum_{i>j}t_i$. For $0\le j\le m-2$ the remaining time is positive. Taking conditional expectation down to $G_0,\ldots,G_{j-1}$ keeps the same lower bound. One may omit the closing arc entirely when bounding the lower tail. Iteration gives the finite-volume Wilson estimate
$$
 \mu(N<c\log n)\le
 \min\{1,\ n^c[1-(1-e^{-1})p_{n,\beta}]^{m-1}\}. \tag{8}
$$
This argument also bounds every $q_i$ in (3) below by (6). Its first quantitative failure is explicit. Even at $\beta=2$, $(m-1)p_{n,\beta}\to0$, while a positive constant times $\log n$ is needed in (8). The cost comes from replacing the bridge's weight near a crossing of $L$ by the smallest weight on the whole orbit. Equations (6)–(8) establish accessibility for the actual Wilson pins, including after rare histories. They do not estimate the typical weight of those crossings.

## 3. Suppressing arcs in the transfer integral

Discount each ambiguous arc by a factor $e^{-1}$ in the full circle integral. Let $h=e^{-1}$, set $p_j=d/t_j$, and use the symmetric kernels $D_t$ from (3). For large $n$, $p_j\ge2$. The exact count gives
$$
 \mathbb E_\mu e^{-N}=\frac{\operatorname{Tr}\prod_j[hA_{t_j}+(1-h)D_{t_j}]}{Z_e(d)}.
$$
Each bracket has the Wilson even kernel on a bad arc and $h$ times that kernel on a good arc. These are pointwise nonnegative kernels. A restriction by an indicator need not be positive semidefinite. Use singular values in the Schatten norm $\|\cdot\|_p$. Since $\sum_j1/p_j=1$ and $\|A_{t_j}\|_{p_j}=Z_e(d)^{1/p_j}$, trace Hölder and the triangle inequality give
$$
 \mu(N<c\log n)\le n^c\prod_j[h+(1-h)z_{t_j}],
 \qquad z_t=\frac{\|D_t\|_{d/t}}{Z_e(d)^{t/d}}. \tag{9}
$$
Each bounded kernel on the finite slice measure is Hilbert–Schmidt. The Hilbert–Schmidt pairing across a cut therefore computes the cyclic trace even for the indicator restrictions. This application of Hölder accommodates both arc lengths and odd $m$. The upper bound allows a ratio $z_t$ greater than one.

For completeness, the unequal-exponent trace Hölder step has a finite-dimensional proof. For factors $V_j$ and $V=\prod_jV_j$, write $a_i=s_i(V)$, $b_i=\prod_j s_i(V_j)$ in decreasing singular-value order. Taking operator norms on the $k$th exterior power gives $\prod_{i\le k} a_i\le\prod_{i\le k} b_i$. Divide by $r^k$ and maximize over $k$, including zero. Taking logs gives $\sum_i[\log(a_i/r)]_+\le\sum_i[\log(b_i/r)]_+$, with zero singular values contributing zero. Integrate over $r>0$ to obtain $\sum_i a_i\le\sum_i b_i$. Scalar Hölder gives $\sum_i b_i\le\prod_j\|V_j\|_{p_j}$. Finite-rank compressions converge here in Hilbert–Schmidt norm, hence in each $p_j$-norm. The traces converge by pairing two Hilbert–Schmidt factors across a cut and bounding the rest in operator norm.

On an equal-length tiling with even $m=d/t$, $z_t^m=\mu(N=0)$ because $D_t$ is self-adjoint and $m$ is even. On those tilings a polynomial bound for just $\mu(N=0)$ already implies (1). Indeed, if $\mu(N=0)\le Cn^{-a}$ then $m(1-z_t)\ge (a-o(1))\log n$, by $m\asymp\sqrt n$, and (9) gives a power for any $c<(1-h)a$. The converse follows by inclusion of events. This equivalence is a diagnostic on those tilings. Replacing the specified unequal lengths by equal ones in either seed period would require a separate comparison. The outline's ordinary equal-slab inequality AM6 motivates this test. The trace argument establishes (9) on the one-axis even law.

To try to bound (9) by known traces, let $\lambda$ be the largest eigenvalue of $T$ and $Z_o(v)=\operatorname{Tr}(P_oT^v)$. For any slice function $f$, $|D_tf|\le A_t|f|$, hence $\|D_t\|_{\rm op}\le\lambda^t$. Where $D_t(x,y)\ne0$ one has $A_t<2|B_t|$. Thus $\|D_t\|_2^2\le4\int |B_t(x,y)|^2dx\,dy=4Z_o(2t)$. With $p=d/t$, bounding each singular value to the power $p-2$ by $\lambda^{t(p-2)}$ gives
$$
 z_t^{\,d/t}\le \frac{4\lambda^{d-2t}Z_o(2t)}{Z_e(d)}. \tag{10}
$$
This recovers, directly on the count integral, the short-period spectral cost encountered in row 1588. A polynomial saving on the right for each relevant $t$ suffices in (9). An upper bound of $C n^{-a}$ gives $\sum_j(1-z_{t_j})\ge(a-o(1))\log n$ by $\sum t_j/d=1$ and $\max (t_j/d)\log n\to0$. There is no such Wilson estimate on file at $2\le\beta\le3$. The unknown in this attempt is how much weight the restriction in $D_t$ actually removes before one takes the bound (10).

### Test of the loss in (10) at both periods

There are two sequences of strictly positive transfer matrices with **identical even pin laws and identical even and odd spectra at every time**. In one sequence $\mu(N<c\log n)$ vanishes faster than any inverse power. In the other it tends to one, at both seed periods, for each fixed $c>0$. This tests whether the sector traces discarded any information needed to decide (1). We use the rare-block construction from row 1588 and exchange the two odd eigenspaces. [Row 1588, Prop. 1.2(3)](gap-band-flux-tail-neon.md)

Use four sites $A_\pm,B_\pm$ with counting measure and $C$ exchanging the signs in each pair. In the orthonormal even basis $(\delta_{i+}+\delta_{i-})/\sqrt2$, $i=A,B$, both matrices have block
$$
 E=E_0+\delta{\bf1}{\bf1}^{T},\qquad
 E_0=\operatorname{diag}(1,\gamma),\qquad
 \gamma=e^{-n^{-3/4}},\quad\delta=e^{-n},\quad{\bf1}=(1,1)^T.
$$
Use the corresponding difference basis in the odd sector. In model I set $O=\operatorname{diag}(1/4,\gamma^2)$ and in model II set $O=\operatorname{diag}(\gamma^2,1/4)$. For large $n$, both matrices are positive definite. The raw entries within block $i$ are $(E_{ii}\pm O_{ii})/2>0$ and between blocks they are $\delta/2>0$. At any integer time $v$ the sector traces are $\operatorname{Tr}E^v$ and $(1/4)^v+\gamma^{2v}$ in both models. The even kernel on raw sites is $(E^v)_{ij}/2$ in both.

The cyclic even pin probability that every pin lies in $A$ equals $\prod_j(E^{t_j})_{AA}/\operatorname{Tr}E^d$. The numerator is at least one since $(E^t)_{AA}\ge (E_{AA})^t\ge1$. Telescoping the difference of powers gives $\|E^d-E_0^d\|\le 2d\delta(1+2\delta)^{d-1}$, hence
$$
 \mu(\text{some pin lies in }B)
 \le\gamma^d+4d\delta(1+2\delta)^{d-1}=o(n^{-a})
 \quad\text{for every fixed }a>0. \tag{11}
$$
Here $d$ is proportional to $n$ at both aspects. On the all-$A$ event the absolute bias is $O_{AA}^{t_j}/(E^{t_j})_{AA}$. In model I it is at most $4^{-t_j}$. In model II it is at least $(\gamma^2/(1+2\delta))^{t_j}\to1$ uniformly over the two arc lengths, since $t_j=O(\sqrt n)$. Thus $N=m$ or $N=0$, respectively, except on the event bounded in (11). The distinction survives every fixed ambiguity threshold strictly between zero and one. Even supplying the whole even kernel and every sector trace does not determine the verdict on general transfer data. In fact the right side of (10) tends to $4$ in both sequences because $1\le\lambda\le1+2\delta$, $d\delta\to0$, $Z_o(2t)\to1$ and $Z_e(d)\to1$. Its proposed polynomial decay is strictly stronger than (1) on these data. This comparison supplies no counterexample for the Wilson action.

## 4. Trying to make both arcs ambiguous by matching a pin to its centre translate

A pin $y$ would suffice for both its incident arcs, at arbitrary neighbours and lengths, if one could match $Cy$ to $y$ cheaply by a vertex gauge. On positive spatial edges $e=(v,w)$ write $c_e=-1$ on the cut and $+1$ elsewhere. With unit-quaternion chord distance set
$$
 H(y)=\min_{g\in{\rm SU}(2)^{n^3}}\sum_{e=(v,w)}
 \big|g_v y_e g_w^{-1}-c_e y_e\big| .
$$
Compactness gives the minimum. The spatial boundary actions of $g\cdot y$ and $Cy$ agree exactly. For a common cylinder interior, the difference of the log weights at that end is at most $\beta$ times the displayed sum. Each boundary link enters one end temporal plaquette, and multiplication by fixed unit quaternions and inversion preserve chord distance. Taking the positive integrals and using vertex gauge invariance of $K_s$ gives
$$
 \left|\log\frac{K_s(x,y)}{K_s(x,Cy)}\right|\le\beta H(y).
$$
The same holds at a starting pin by symmetry. Count the pins with $\beta H(y)\le\log3$. Each certifies at least its own outgoing $G_j=1$. This is a test about the pins of the actual Wilson circle, with no condition on preceding indicators. Its probability can be bounded explicitly on the band.

Use the existing two-plaquette estimate (4) of [row 1141](gap-crux2-astra62.md). Check 1556 used a different local witness, a centre-frustrated cube, to exclude everywhere-removable plaquette signs. [Check 1556, §(vi)](gap-mech-direction4-check-astra62.md)

On the transverse $23$-torus of the cut at each pin, take base sites $(x_2,x_3)=(4i,4j)$. There are $L=n^2/16$ of them. At each base take the north-east and south-west unit plaquettes based there, with holonomies $U,V$. Different pairs have disjoint supports. Define
$$
 \Delta(U,V)=\min_{|v|=1}\bigl(|v-\operatorname{Ad}U\,v|^2+|v-\operatorname{Ad}V\,v|^2\bigr)
$$
on unit imaginary quaternions. This is gauge invariant, and the minimum permits the axis to depend on the fields. In the band, conditional on the exterior of a pair, the probability of $\Delta\ge1/152$ is at least $1/2$. To apply row 1141 at a pin, expand each $A_t$ into its two centre labels and include the cylinder interiors. At fixed labels the full spatial plaquette weight at the common end is the product of the half weights. The twist only changes signs of temporal seam terms. Fixing all links but one leaves the one-link density $e^{h\cdot U}/Z$ with $|h|\le6\beta$, including for signed staples. These are precisely the hypotheses of row 1141's one-link estimate (3) and its proof of (4) by revealing one link of either plaquette. Its lower threshold $1/[8(1+6\beta)]$ is at least $1/152$. The bound persists when one averages over interiors and labels, also conditional on the other pins.

Let $R_j$ count base sites satisfying $\Delta\ge1/152$ at pin $j$. Reveal the disjoint pairs successively. The preceding conditional bound and exponential Markov give, with $\kappa=(1-e^{-1})/2-1/4>0$,
$$
 \mu\{\text{some pin }j\text{ has }R_j<L/4\}\le m e^{-\kappa L}. \tag{12}
$$
Indeed each conditional factor for $e^{-R_j}$ is at most $1-(1-e^{-1})/2$. Multiply $L$ factors and take a union bound over pins.

Fix a gauge choice and denote its edge errors in the definition of $H$ by $d_e$. On a loop based at $a$ with winding sign $\chi$ and holonomy $W$, telescoping unit-quaternion products gives
$$
 \sum_{e\ {\rm on\ loop}}d_e\ge |g_a-\chi Wg_aW^{-1}|.
$$
Reversing an edge preserves its error. For each of the $R_j$ counted bases take its direction-1 winding line and its two transverse plaquettes. On the line $\chi=-1$, so its sum is at least $2|\operatorname{Re}g_a|$. For the plaquettes $\chi=+1$. Their two sums together are at least $|\operatorname{Im}g_a|\sqrt{\Delta(U,V)}$, by testing the direction of $\operatorname{Im}g_a$ in the minimum and using the sum of the two norms to bound their Euclidean combination. If $\operatorname{Im}g_a=0$ the latter bound is automatic. The line and plaquette edges used at distinct bases are disjoint. Since $|\operatorname{Re}g_a|+|\operatorname{Im}g_a|\ge1$, minimization over gauges gives
$$
 \frac{R_j}{\sqrt{152}}\ \le\ H(x_j)\ \le\ 2n^2. \tag{13}
$$
The identity gauge gives the upper bound. Thus except on a set of probability at most $m e^{-\kappa n^2/16}$, **every pin** has $H(x_j)\ge n^2/(64\sqrt{152})$. In particular the chance that even one pin qualifies for the $\log3$ test is at most that exponential for all large $n$. This refutes this specific sufficient way of producing the count in Wilson throughout $[2,3]$. The lower bound in (13) is on a sum of edge discrepancies. Taking a log *after* integrating a Wilson cylinder can give a small log ratio even at such pins. Indeed the same obstruction holds at any fixed $0<\beta<2/9$, where the on-file Dobrushin bound makes every arc ambiguous for all sufficiently large $n$. [Row 1568, Thm E](gap-band-cut-covariance-neon.md) · [Check 1572](gap-band-cut-covariance-neon-check-opus.md)

There is a second check of the area scale using only winding traces. For the $n^2$ disjoint direction-1 lines, the two endpoint products are $g_aWg_a^{-1}$ and $-W$. Their real parts differ by $2\operatorname{Re}W$, so the edge errors on each line sum to at least $2|\operatorname{Re}W|$. The joint density comparison in the proof of row 1587 (7), checked in 1589 step 5, bounds the density of their transports at a pin by $2$ relative to product Haar for all sufficiently large $n$ on the band. Set $p_H=\Pr_{\rm Haar}(|\operatorname{Re}U|\ge1/2)>0$. Under product Haar the number of lines passing this test is binomial with parameters $n^2,p_H$. The same exponential Markov argument therefore yields
$$
 \mu\{\exists j:\ H(x_j)<p_H n^2/2\}
 \le 2m\exp[-(1/2-e^{-1})p_H n^2]. \tag{14}
$$
This uses single winding characters on disjoint lines. The local two-plaquette argument in (13) does not use their distribution. [Joint density estimate preceding (7)](gap-band-flux-tail-astra62.md) · [Check 1589, step 5](gap-band-flux-tail-astra62-check-opus.md)

In the opposite direction, a disproof of (1) supported on the event that some pin has $R_j<L/4$ also fails by (12), even if every history in that event had $N=0$. A reducible slice has $\Delta=0$ at every base. The open part is the probability of $\{N<c\log n,\ R_j\ge L/4\ \text{for every }j\}$. Row 1587 tests the inference from (12) to the arc count. Its comparison kernel on the same raw slice space has even pin law product Haar and $|b_t|=e^{-t/n^2}$ almost surely. Its Haar pins obey (12) by the same local test with zero staple, yet $N=0$ eventually. [Row 1587 and the detoured winding circuit](gap-band-flux-tail-astra62.md) · [Check 1589, step 5](gap-band-flux-tail-astra62-check-opus.md)

## The flux consequence and the remaining Wilson estimate

Let $\rho_i(d)=\operatorname{Tr}(P_{o,i}T^d)/\operatorname{Tr}(P_{e,i}T^d)$ for axis $i$. The odd kernels compose around the circle just as the even ones do. Dividing their integrated product by $Z_e(d)$ yields check 1585's $\rho_i(d)=\mathbb E_\mu\prod_j b_{t_j}$. For $p=\mu(N<c\log n)$ this gives
$$
 \rho_i(d)\le p+(1-p)n^{-c\log2}. \tag{15}
$$
Thus (1) would imply $\rho_i(d)\le R_n=C_0n^{-\epsilon}+n^{-c\log2}$. The odd thermal probability on that axis equals $\rho_i/(1+\rho_i)$. The three commuting centre parities admit a joint distribution with masses $\operatorname{Tr}(P_\chi T^d)/Z^0(d)$. Summing the three single-axis probabilities bounds the probability of any nonzero flux. Spatial cubic symmetry gives the same estimate on each axis, so at $d=2v$, $v\in\{u/2,u\}$,
$$
 f(d):=1-\frac{Z_+(d)}{Z^0(d)}
 \ \le\ \frac{3R_n}{1+R_n}
 =O\big(v^{-\min(\epsilon,c\log2)}\big).
$$
This is (N-flux) on the band, conditional on (1). The Wilson estimates proved here supply no decay rate for $f(d)$. [Flux weights, row 1566, parts (f)–(g)](gap-band-cut-covariance-fable.md)

**Model tests.** At the same aspects in weak 4D compact U(1), row 1565 and check 1571 give an odd probability at least $\eta>0$ for all sufficiently large fixed Wilson $\beta_W$ and for Villain $\beta\ge2000$. Equation (15) forces $p\ge[\eta/(1-\eta)-n^{-c\log2}]/[1-n^{-c\log2}]$. This locates the failure of the count at weak compact U(1) coupling. For the pin-matching test specifically, in U(1) the winding-line error for each line is at least $|g_a+Wg_aW^{-1}|=2$, so $H(y)=2n^2$ identically. The local axis defect used in (12) is a non-Abelian effect. In 5D SU(2) the same two plaquettes can be placed at order $n^3$ disjoint bases on the three-dimensional cut, with eight incident plaquettes per link. The proof of (12)–(13) carries over with $6\beta$ replaced by $8\beta$ in the local estimate. The integral and transfer inequalities also hold in five dimensions. An odd thermal fraction bounded away from zero along an unbounded sequence there would violate the count by (15). I have no proof of that fraction or of a failure of the count for interacting 5D SU(2). [Weak compact U(1), eq. (7)](gap-band-cut-covariance-astra62.md) · [Check 1571](gap-band-cut-covariance-astra62-check-opus.md)

**Purity.** For a neutral spectator with positive kernel $S$, $C$ acts as $C\otimes I$ and both arc kernels acquire the same factor $S^t$. All $b_j$ and their joint law are unchanged after integrating the independent spectator pins. Both the untwisted purity $\Pi=Z^0(2u)/Z^0(u)^2$ and the neutral purity acquire the factor $\operatorname{Tr}S^{2u}/(\operatorname{Tr}S^u)^2$. For example on $q$ sites take $S=rI+(1-r)P_{\rm const}$, $r=e^{-1/n^2}$. The factor tends to $1/q$. Even a count with $N=m$ everywhere therefore supplies no positive uniform lower bound for $\Pi$. Conversely the two-state transfer example in check 1585 has a one-dimensional even sector, neutral purity one, and $N=0$ eventually. These separations concern transfer data. At a common coupling the exact relation is $P=\Pi[1-f(2u)]/[1-f(u)]^2$. Neither a bound on $\Pi$ nor a carry to the calibrated $\beta_K$ follows here. [Check 1585, §(v)](gap-band-direction5-check-astra62.md) · [Seed, §3.1](gap-k2-tool-design-fable.md)

The remaining lemma is (1) for the full Wilson pins. Angle integration loses the weight at sign crossings, the restricted transfer integral loses the odd eigenfunctions when bounded by traces, and individual pins cannot supply the count via cheap gauge matching. Equations (4)–(5) give an equivalent location of the missing estimate in the alternating-pin law. The new estimates are hand arguments. They have not undergone a Lean or cross-provider check.

RESULT — OPEN for the Wilson count on $[2,3]$. The probability that any pin passes the sufficient gauge-matching test $\beta H\le\log3$ is at most $2m e^{-(1/2-e^{-1})p_H n^2}$ for large $n$. The count itself is neither proved nor refuted. Its implication for (N-flux) remains conditional, and it gives no bound on $\Pi$ or (PUR-io).
