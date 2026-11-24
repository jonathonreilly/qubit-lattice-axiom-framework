# Repo search

At checkout `9fa325418462` the target-specific prior file is absent. I searched Markdown and TeX on `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). The terms `gap-k2-nonlinear-pin`, `gap-k2-integrated-activity`, “staggered Cartan”, “Cartan stripe”, “nonlinear pin”, the radicand and the quartic-residual patterns returned no target hits. Method searches included “soft Hessian”, “pinned Hessian”, tree-gauge coercivity, two-block Poincaré and “384-contour”.

- **Pinned lane.** Row 1468 §3.2 defines Q2. Row 1479 Proposition L gives a finite-torus minimizer near identity by the implicit function theorem. Row 1480 gives the exact stripe transports, the restricted minimum and the integrated quartic. Row 1488 checks the coefficient and shows that the stripe energy covers the old lower bound. It explicitly leaves transverse stability open. Registry row CR concerns a prescribed layered datum outside an admissible box. I found no competing owner for this pin. [Q2](gap-k2-tool-design-fable.md) · [Proposition L](gap-k2-signed-readout-fable.md) · [Row 1480, (4)–(8)](gap-k2-integrated-activity-astra62.md) · [Row 1488, remark for 1490](gap-k2-activity-interface-check-opus.md) · [Registry](open-registry.md)
- **PRs 10114 and 10133.** In `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`, `MANUSCRIPT_RG.md` §§4.9–4.10, 4.20 gives the flat tree-gauge gap (F3–F4), small-cap nonlinear coercivity (F10–F12) and a fixed-torus soft minimizer (GS4–GS5) for the centred kernel. `UNIFORM_SOFT_MINIMIZER_ASTRA.md` §§1, 5 bounds the neutral stationary fourth derivative at identity for odd $L\ge3$. `LARGE55.md` §5.4 argues small-background positivity. All three file blobs agree across these two refs. These results supply the flat comparison and the perturbation method. The explicit side-two stripe and its stability at the test angle require the calculation below.
- **Main, PR 10141 and the November 8 digest.** Main’s `.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/full-connected-four-response.md` 365–386 bounds a fixed-terminal numerator. The digest, §§8 and 12, identifies `pr/10141:research/ym4d/library/out-mu.md` 8–32, 69–82, which gives a unique regular axial minimizer and holomorphic nesting for Bałaban’s hard averages on admitted data. In this lane `ref-chart.md` Lemma P bounds tree-fixed variables by curls with fixed exterior edges. Here the face variables remain free and a finite-strength pin controls their means. [Prior search](prior/repo-search-2026-11-08.md) · [Tree estimate](ref-chart.md)

## Result for row 1490

**Proved by hand.** For $a=\kappa/x=1$ and $|t|\le\arcsin(1/4)$, the Cartan stripe is the unique minimum of the exact classical phase on an explicit tree-gauge block neighbourhood. Its Hessian at the minimum is at least $1/108900$ in the unscaled link counting norm, for all colours and all allowed torus sizes. The source interval includes row 1480’s $t=1/8$ and reaches coarse plaquette chord $1/2$. For every fixed $a>0$ a volume-independent interval about zero also works. The minimum per block is $8+a-\sqrt{64+a^2+16a\cos t}$. Its local extraction cancels the integrated $19h^4/(729x)$ term, as expressed in (7). The Kotecký–Preiss estimate for the full integration domain remains open.

### Plan saved at creation

1. Identify the phase, block neighbourhood, gauge and the scope of earlier results.
2. Test the exact Cartan minimizer against admissible colour and spatial variations. Seek either a volume-independent Hessian bound with a local background energy or an explicit competing field or zero mode.
3. Check the decisive calculation, state its hypotheses and proof status, and give the next two rows.

### Published scope

The supplied Sussman–Alpoge bundle is identified as `31a47c543775`. The outline defines its odd-block logarithmic mean by QC1 (7945–7979). Its flat precision comparison uses a plain constraint and a soft internal gauge. A2 requires coercivity on the actual nonflat fibres (3835–3863), and A4 requires control of the change of averages there (3898–3906). The flat minimum is identified with a background Hessian conditional on a differentiable stationary lift (8590–8604, 9047–9054). CA-I 35144–35198 cites Bałaban’s CMP 102b, Theorem 1, for a minimal regular orbit. CA-II 85845–85871 prescribes the block averages of that orbit. CA-III 35577–35606 describes the higher variation bounds (189)–(190) as “printed without proof”. These are references for the method. The estimates here are proved for the arithmetic quaternion mean of Q2. [Outline index](sa-index/README.md) · [Indexed obligations](sa-index/obligations.md) · [Bałaban quotations](lit-balaban.md)

## The full stationary equation

**Proved.** Work on a finite periodic coarse four-torus with even period in direction 1 and all periods at least four, as in row 1480. Put $\epsilon_y=(-1)^{y_1}$, $V_{y2}=\exp(I\epsilon_y t)$ and $V_{y\mu}=1$ otherwise, with $I$ a unit imaginary quaternion. Fix $a=\kappa/x>0$. In fine units the exact classical phase is
$$
S_t(W)=\sum_p(1-\operatorname{Re}W_p)+
a\sum_c\bigl(|M_c|-\operatorname{Re}(M_cV_c^{-1})\bigr).
$$
Here $M_c$ averages the 384 labelled paths from the tail base to the head base. Each uses an ordered offset leg, two forward steps and the reverse translated offset leg. This is precisely the phase in the exact factorization of row 1480, line 165. The remaining radial pin factor and the Haar density are amplitudes.

Take the field of row 1480, lines 137–145, with $2u=v$. In its tree representative every internal link is one. Every face link in direction 2 is $\exp(I\epsilon_y v)$, every face link in direction 1 is $\exp(I\epsilon_y(2\xi_2-1)v/2)$, and the others are one. Here $\xi$ is the bit vector of the tail of the crossing link. Choose the branch through zero
$$
v=\arg(8+a e^{it}),\qquad 8\sin v+a\sin(v-t)=0.
$$
For $|t|<\pi/2$, $v$ lies between $0$ and $t$ (with endpoints exchanged for negative $t$), and $\cos(v/2)>0$. The direction-1 mean is $\cos(v/2)$, the direction-2 mean is $\exp(I\epsilon_y v)$, and the two remaining means are one. The energy per block is the stripe value $N_a(t)=8+a-|8+a e^{it}|$ established in rows 1480 and 1488.

For a Cartan perturbation $I z_e$ let $Qz$ be the averaged signed path sum. At an aligned nonzero mean $M_c=r V_c$, the derivative of the pin with respect to $M_c$ vanishes. On a direction-2 bond all 384 unperturbed path products coincide. Differentiating the pin there gives $a\epsilon_y\sin(v-t)(Qz)_{y2}$. In the signed sum over $y$ the offset legs cancel by translation through $2e_2$, which preserves $\epsilon_y$. The two middle steps each sum to $1/16$ of the staggered sum over direction-2 fine links. The Wilson variation is $\sin v$ times that same fine sum. Indeed the only nonzero oriented plaquette angles are $-\epsilon_y v$ on the odd direction-1 layer of the $(1,2)$ plaquettes. Their backward direction-1 difference in the adjoint curl gives $+\epsilon_y\sin v$ on both layers' direction-2 links, and the direction-2 difference vanishes. Thus the first variation is
$$
\left(\sin v+\tfrac a8\sin(v-t)\right)
\sum_n\epsilon_{\lfloor n/2\rfloor} z_2(n)=0 .
$$
Conjugation by $I$ fixes every background and source link and negates both perpendicular colours on every link. The differential therefore vanishes on every transverse perturbation as well. The argument applies to localized perturbations and restricts to the descending-tree slice. It proves stationarity in the full real tangent space for this source.

## Coordinates for a quantitative Hessian bound

**Proved.** From here through the quantitative bound take $a=1$ and $|t|\le t_c=\arcsin(1/4)$. This is the component through zero of the coarse plaquette cut $|1-V_p|\le1/2$. Since $\cos t\ge\sqrt{15}/4>15/16$ and $|\tan v|=|\sin t|/(8+\cos t)$,
$$
|v|\le1/35,\quad |u|\le1/70,\quad
s_0:=|\sin(t-v)|=8|\sin v|\le8/35 .
$$
Also $q:=1-\cos(t-v)=s_0^2/(1+\cos(t-v))\le(8/35)^2/(1+15/16)<1/36$, since $|t-v|\le|t|$. In particular $q+s_0<13/50$.

Use left variations $W_e(s)=e^{s z_e}W_e^*$ about the displayed stripe. A root-fixed infinitesimal gauge adds $\psi_n-\operatorname{Ad}_{W_e^*}\psi_{n+e_\mu}$ to $z_e$. The phase is invariant under these gauges. At a critical point its second derivative depends only on the resulting tangent class. Indeed one can transform the entire path by the gauge $e^{s\psi_n}$, and the acceleration correction in replacing it by an exponential path with the same velocity is paired with the zero differential.

Inside each block all background links equal one. Choose the root-zero potential so that the internal velocities $b$ are orthogonal to all internal gradients in the counting inner product. This is ordinary orthogonal projection onto the complement of the gradient space of a connected finite cube. Write $c_{y\mu}(z)$ for the eight crossing velocities, $z\in\{0,1\}^3$, and $m_{y\mu}=\frac18\sum_z c_{y\mu}(z)$. Use the norms
$$
A^2=\sum_{\rm internal}|b|^2,\quad C_\mu^2=\sum_{y,z}|c_{y\mu}(z)|^2,\quad
C^2=\sum_\mu C_\mu^2,\quad B^2=\sum_{y,\mu}|m_{y\mu}|^2 .
$$
All sums use counting measure except for the indicated face and contour averages.

**Internal curl. Proved.** $\sum_{p\ {\rm internal}}|db(p)|^2\ge4A^2$. Expand the direction-$j$ internal bonds in the characters $\chi_R(\xi)=(-1)^{\sum_{i\in R}\xi_i}$ of the three other bits. Group coefficients as $w_j\chi_{S\setminus\{j\}}$, $j\in S$, for each nonempty $S\subset\{1,2,3,4\}$. Gradients of $\chi_S$ give the coefficient $-2$ in every such direction, hence $\sum_{j\in S}w_j=0$. Its squared bond norm is $8\sum_j |w_j|^2$. Its squared curl norm is $16\sum_{i<j\in S}|w_i-w_j|^2=16|S|\sum_j|w_j|^2$. Each pair has four locations, and its curl coefficient is $\pm2(w_i-w_j)$. Distinct characters are orthogonal. The one-index components vanish, which gives the bound for all three colours.

**Pin paths. Proved.** Every contour crosses its assigned face exactly once, with velocity $c(z)$. Its two offset legs and exactly one of the two middle steps use internal links. For a fixed direction $\mu$ let $L_\gamma$ be the sum of the lengths of all the *internal velocities* along a labelled contour, counting repeated occurrences. Use counting measure on $y$ and probability $1/384$ on its labels. Then
$$
\|L_\gamma\|_2\le(2+1/\sqrt8)A\le K A,\qquad K=12/5,\qquad
\||c(z)|\|_2=C_\mu/\sqrt8 .
$$
For a single ordered offset path the probability of using a specified edge is at most $1/4$. For an edge leaving the root the probability is $(15/16)/4$ by permutation symmetry. Any other edge requires the traversed bit and at least one specified earlier bit to be one. The path length is at most four, so the squared sum of velocity lengths is at most four times the sum of their squares. Averaging and applying the edge probability bound gives at most the squared internal bond norm of that block. This applies to the translated leg as well. The internal middle step reads a specified $\mu$-edge with weight $1/16$ from the tail block and $1/16$ from the head block after summing in $y$. The triangle inequality gives the stated estimate.

For each block, the *signed vector sum* of $b$ along the random forward offset leg has mean zero. Its expected edge weights depend only on the number of set bits at the edge's tail, by permutation symmetry. Such weights form the gradient of a function of that number (choose its successive differences to be the weights). Likewise, the mean sum on the optional internal $\mu$-step at either end is zero, since the constant unit $\mu$-edge field is the gradient of $\xi_\mu$. For a face with crossing matrix $R$ constant in $z$, the two internal mean contributions to $M'_c R^{-1}$ thus vanish separately, even after rotating the head sum by $\operatorname{Ad}_R$. The crossing contribution is exactly $m_{y\mu}$. This applies in directions 2, 3 and 4 for arbitrary colours on the two blocks.

## The Wilson and pin second variations

**Wilson bound. Proved.** Moving all exponential insertions to the left in a path product writes it as $(\prod_i e^{sX_i})P$, where $P$ is the unperturbed product. Inverses introduce a minus sign and conjugation preserves each velocity length. Its second derivative at zero is
$$
\left(-\Big|\sum_i X_i\Big|^2+2\sum_{i<j}X_i\times X_j\right)P.
$$
This follows by multiplying the first two Taylor coefficients, using $XY=-X\cdot Y+X\times Y$ for imaginary quaternions. Write $T=\sum_{i=1}^4 X_i$, $Z_i=X_i-T/4$. A flat plaquette contributes $|T|^2$. On a plaquette of angle $\pm v$ the extra signed term has magnitude at most $|\sin v|\,|2\sum_{i<j}X_i\times X_j|$.

For the four centred vectors, $\sum Z_i=0$ gives
$$
\sum_{i<j} Z_i\times Z_j=(Z_1+Z_2)\times(Z_2+Z_3),\qquad
|Z_1+Z_2|^2+|Z_2+Z_3|^2=\sum_i|Z_i|^2-|Z_1+Z_3|^2.
$$
The mixed part of $2\sum_{i<j}X_i\times X_j$ is $(3Z_1+Z_2-Z_3-3Z_4)\times T/2$. Cauchy–Schwarz bounds the whole cross-product term before the sine factor by $\|Z\|^2+\sqrt5\|Z\||T|$, with $\|Z\|^2=\sum_i|Z_i|^2\le\sum_i|X_i|^2$. Writing $s=|\sin v|$, spend $|T|^2/4$ to bound $s\sqrt5\|Z\||T|$ by $|T|^2/4+5s^2\|Z\|^2$. The scalar part of the Wilson Hessian is $\cos v\,|T|^2$. Since $s+5s^2\le8/245<1/30$ and $\cos v-1/4>7/10$, the full nonflat contribution is at least $(7/10)|T|^2-(1/30)\sum_i|X_i|^2$.

Let $F^2$ be the sum of $|\sum X_i|^2$ over plaquettes crossing exactly one block face. For each, start at the lower transverse position on the tail block and cross the face first, as in the formula for $Y$ below. This fixes the convention for $F$. The Wilson summand is invariant under reorienting or rebasing a plaquette for every field. Only the odd-layer $(1,2)$ plaquettes have nonzero angle. Each direction-1 crossing link lies in two of these, and each fine direction-2 link in one. All other fine links lie in none. Keeping the internal curl bound and the single-face square terms gives
$$
H_{\rm W}\ \ge\ 4A^2+\tfrac7{10}F^2
              -\tfrac1{15}C_1^2-\tfrac1{30}(C_2^2+A^2).
\tag{1}
$$

**Pin bound. Proved.** Set $B_\mu^2=\sum_y|m_{y\mu}|^2$. The pins in directions 3 and 4 contribute $B_3^2+B_4^2$. Indeed the Hessian of $|M|-\langle M,V\rangle$ at $M=rV$ is $|P_{V^\perp}M'|^2/r$, with the real Euclidean inner product of quaternions. In direction 1, $r=\cos u$, $V=1$. Replacing each crossing matrix $R_z=e^{\pm Iu}$ by 1 in the first derivative changes a contour's derivative by at most $|u|(|c(z)|+L_\gamma)$. All its factors except the single crossing are identity at the background, and $|R_z-1|\le |u|$. With the replacement the averaged derivative is $m_{y1}$. Jensen's inequality and the path estimates give $\|\operatorname{Im} M'_1-m_1\|_2\le(C_1/\sqrt8+K A)/70$. Since $1/r\ge1$ and $|m+e|^2\ge(9/10)|m|^2-9|e|^2$, the direction-1 Hessian satisfies
$$
H_1\ge\tfrac9{10} B_1^2-C_1^2/2000-A^2/40 .
\tag{2}
$$
Here $9\|e\|^2\le(18/70^2)(C_1^2/8+K^2 A^2)$.

In direction 2 every individual contour product equals the same matrix $R$ at its bond. Then $M'R^{-1}=m_{y2}$, so the second differential of the norm contributes $|m_{y2}|^2$. Its first differential minus that of $\langle M,V\rangle$, applied to $M''$, contributes $-q$ times the mean of $|\sum X_i|^2$ and a signed cross-product term. The latter has absolute value bounded by $s_0$ times the mean of $2|c(z)|L_\gamma+L_\gamma^2$, since there is only one crossing. Thus
$$
H_2\ge B_2^2
 -q C_2^2/8
 -(q+s_0)\big(2K C_2 A/\sqrt8+K^2 A^2\big)
 \ \ge\ B_2^2-19C_2^2/288-231A^2/100 .
\tag{3}
$$
For the last inequality, $q/8\le1/288$, $(13/50)K^2<3/2$ and $(13/50)2K/\sqrt8<9/20$ (use $\sqrt8>14/5$). The mixed term is bounded by $(9/20)C_2 A\le C_2^2/16+81A^2/100$.

**Control of crossing links. Proved.** For one face write $z'=z+e_\nu$, $z_\nu=0$, $\nu\ne\mu$. Orient its single-face plaquette by crossing at $z$, moving in direction $\nu$ on the head block, crossing back at $z'$ and returning on the tail block. Write $b',b$ for the two internal velocities. Its sum of transported insertions is
$$
Y=c_z+\operatorname{Ad}_{R_z}b'
       -\operatorname{Ad}_{P}c_{z'}-\operatorname{Ad}_{P}b,
\qquad P=R_zR_{z'}^{-1}.
$$
The squared lengths of these $Y$ sum to $F^2$. The squared norm of the two internal terms in this whole list is at most $6A^2$, since each internal edge meets one face for each of its three transverse directions. The error $(\operatorname{Ad}_P-1)c_{z'}$ occurs only on direction-1 faces with $\nu=2$, and each such $c_{z'}$ occurs at most once. Quaternion conjugation by $e^{\pm Iv}$ rotates the perpendicular plane by $\pm2v$, so the error norm is at most $2|\sin v|C_1\le 2C/35$. Consequently
$$
\|\nabla_{\rm face}c\|_2\le F+\sqrt6 A+2C/35 .
$$
Each face is a three-dimensional cube with eight sites. On a character of a nonempty subset $S$ of the three bits, the gradient norm squared divided by the site norm squared is $2|S|$. Taking the sum over faces yields
$$
C^2-8B^2\le\tfrac12\|\nabla_{\rm face}c\|_2^2
\le\tfrac32 F^2+9A^2+6C^2/1225,
\qquad
C^2\le\tfrac{81}{10}B^2+2F^2+10A^2 .
\tag{4}
$$

**Full Hessian on the tree slice. Proved.** From (1)–(3), including directions 3 and 4,
$$
H\ge\tfrac85 A^2+\tfrac7{10}F^2+\tfrac9{10} B^2-\tfrac1{10}C^2.
$$
Indeed $1/15+1/2000<1/10$ and $1/30+19/288=143/1440<1/10$ apply to distinct directions. By (4), $(11/100)C^2\le(891/1000)B^2+(22/100)F^2+(11/10)A^2$. Substitution leaves at least $A^2/2+C^2/100$ on the right. To return to a tangent vector $z$ on the descending-tree slice, reconstruct the change of gauge from its internal tree edges. Each root-to-site path has at most four edges. Thus $|\psi_n|\le2\|b\|_{2,B(n)}$ and $\sum_n|\psi_n|^2\le64A^2$. The gauge correction over all fine bonds has squared norm at most $16\sum_n|\psi_n|^2$ by the degree-eight incidence count and orthogonality of conjugation. It follows that $\|z\|_2\le33\sqrt{A^2+C^2}$. In particular,
$$
D^2 S_t(W^*)[z,z]\ge \lambda\|z\|_2^2,
\qquad \lambda=\frac1{100\cdot33^2}=\frac1{108900}.
\tag{5}
$$
This holds for the complete colour space and all the stated tori, with torus holonomies still allowed.

## A volume-independent block neighbourhood

**Proved.** In the tree slice use relative coordinates $W_e=e^{Z_e}W_e^*(t)$ on the free bonds, and put $\|Z\|_\infty=\max_e|Z_e|$. Each local term reads at most two blocks for a pin or four for a plaquette. A fine bond belongs to the supports of at most six plaquettes and eight pins, the latter being the coarse bonds incident to its block for an internal link and only its own face for a crossing link.

Here are explicit differentiability bounds for this chart. A product along a path of length $l$ has derivatives of orders $j=1,2,3$ bounded by $l^j\prod_i\|w_i\|_\infty$ on its support. For a link exponential the ordered-integral formula for the $j$ insertions is a sum over $j!$ orders on a simplex of volume $1/j!$. Each remaining exponential is unitary. This formula follows by expanding the exponential series, or by differentiating the integral formula for its first derivative. Applying the product rule distributes the $j$ labelled insertions among $l$ occurrences. The same bound covers inverses and repeated edges. Each contour has $l\le10$. If $\|Z\|_\infty\le1/40$, telescoping from the centre gives $|M_c|\ge\cos(1/70)-10/40>1/2$. A Wilson term has third derivative bound $4^3$. For $r=|M|\ge1/2$ the norm function has derivative bounds $1,1/r,6/r^2$ through order three, from $Dr[h]=\langle M/r,h\rangle$ and $D(M/r)[h]=P_{M^\perp}h/r$. In the pin term the third-order chain rule therefore gives at most $a(24+3\cdot2+2)10^3\prod_i\|w_i\|_\infty$.

Put $D_a=\max(64,32000a)$. By using the local maximum for the first direction and the local squared bond norm for the two test directions, and then the incidence count 14, one gets
$$
\big| (D_Z^2 S_t(Z)-D_Z^2 S_t(0))[w,w]\big|
 \le 14D_a\|Z\|_\infty\|w\|_2^2 .
$$
At $a=1$ take $\rho=\min(1/40,\lambda/(28D_1))=1/97{,}574{,}400{,}000$. Throughout the closed product $\|Z\|_\infty\le\rho$ the coordinate Hessian is at least $\lambda/2$. Integrating twice on the straight segment from zero proves
$$
S_t(e^Z W^*)\ge N_b N_1(t)+\tfrac{\lambda}{4}\|Z\|_2^2,
\qquad |t|\le t_c ,
\tag{6}
$$
where $N_b$ counts coarse sites. Equality at the minimum forces $Z=0$. This includes all real, spatially inhomogeneous and transverse-colour perturbations in the product. Its plaquettes obey the cold cut since their chord is at most $|v|+4\rho<1/2$.

**Arbitrary fixed pin ratio. Proved near zero source.** At $t=0$ the identity-point Hessian is $\|dz\|^2+a\|Qz\|^2$ in tree coordinates (row 1480). Thus it is at least $\lambda_a I$, $\lambda_a=\min(1,a)\lambda$. This is also the flat-gap comparison of F3–F4 in the repo search, here with the explicit side-two bound (5). In *identity-centred* coordinates $W_e=e^{Y_e}$, $\|Y\|_\infty\le1/40$ ensures $|M_c|\ge1-10/40$. Use the same third derivative bound. Varying $t$ at fixed $Y$ costs at most $100a$ per pin in the mixed derivative $\partial_t D_Y^2 S_t$ in local maximum norms, since $|V'_c|\le1$ and $\|D^2M_c\|\le10^2$. Choose
$$
r_a=\min\{1/40,\,\lambda_a/[28(D_a+100a)]\}.
$$
For $\|Y\|_\infty\le r_a$ and $|t|\le r_a/2$ the Hessian is at least $\lambda_a/2$. The stationary stripe lies in the interior since its link angles are at most $|v|\le |t|$. It is the unique minimum on that whole gauge-fixed product, with energy $N_b N_a(t)$. All radii are independent of $x$ at fixed $a$ and of the torus periods. The much larger source interval in (6) uses the separate transverse calculation at $a=1$.

## The local background energy and the integrated residual

**Proved on the stated sources.** The coarse $(1,2)$ plaquette based at $y$ has real part $s=\cos(2t)$, and the other five positive plaquettes there have real part one. For $|t|<\pi/2$ define
$$
n_a(s)=8+a-\sqrt{64+a^2+16a\sqrt{(1+s)/2}},\qquad
d_a(s)=\frac{a}{8+a}(\arccos s)^2-n_a(s).
$$
Both functions vanish at one and are real analytic there. For the squared inverse cosine this follows by inverting the analytic function $z\mapsto1-\cos\sqrt z$ at zero, where its derivative is $1/2$. The sum of $n_a(\operatorname{Re}V_p)$ over the six positive coarse plaquettes based at $y$ equals exactly the minimizing energy $N_a(t)$ per block in (6) or its small-source generalization. This is a gauge-invariant local density on the tested family. The corresponding sum of $d_a$ is $G_a(t)-N_a(t)$, where $G_a(t)=4at^2/(8+a)$ is row 1480's extracted Gaussian action per block.

At $a=1$ the exact difference is
$$
G_1(t)-N_1(t)=\tfrac49 t^2-9+\sqrt{65+16\cos t}
             =\tfrac{19}{729}t^4+O(t^6).
$$
Row 1488 checked this coefficient. In row 1480's joint normalization, replace the extracted $e^{-xG_1(t)}$ by $e^{-xN_1(t)}$ for each block. Multiply the two unshifted local weights $e^{-P_x}f_{B,C}$ and $e^{-P_x}f_{B,H}$ by $e^{-x(G_1-N_1)}$, before subtracting 1 to define the cold mark. Their sum times the extracted action is exactly the original block factor. This change has zero constant and quadratic log terms at $t=0$, so row 1480's vacuum and Hessian subtraction is preserved. Its renormalized cold singleton then satisfies
$$
1+\widetilde z_{B,C}(t)
   =e^{-x(G_1(t)-N_1(t))}(1+z_{B,C}(t)),\qquad
\lim_{x\to\infty}x\,\widetilde z_{B,C}(h/\sqrt{x})=0
\quad(h\in\mathbb R\ \text{fixed}).
\tag{7}
$$
Indeed $x(G_1-N_1)(h/\sqrt{x})=19h^4/(729x)+O_h(x^{-2})$, and row 1480, (8), gives $xz_{B,C}(h/\sqrt{x})\to19h^4/729$. Equation (7) uses the original marked expectation at fixed volume. A bound uniform in $h$ or on the full activity requires further estimates.

**Proved for the exact integral restricted to (6).** Let $Z_{\rho,x}(t)$ integrate the Wilson density times the exact pin kernels divided by their flat bond factors over that tree-gauge product, with normalized Haar measure on free links. The radial amplitude for a bond of mean length $r$ is $h(\kappa)/h(\kappa r)$, $h(k)=\int_{S^3}\exp[-k(1-q_0)]\,dq$. It lies between $h(\kappa)$ and 1. For each $\varepsilon>0$, $h(\kappa)\ge e^{-\kappa\varepsilon}\Pr_{\rm Haar}(q_0>1-\varepsilon)$, so its logarithm divided by $x$ tends to zero at fixed $a$. Equation (6) bounds the integral above by $e^{-xN_bN_1(t)}$. Conversely, every sufficiently small open neighbourhood of the minimizer inside the product has positive Haar measure, and continuity bounds the phase there by $N_bN_1(t)+\varepsilon$. Applying the radial bound to its finitely many coarse bonds and then letting $\varepsilon\downarrow0$ gives
$$
-\lim_{x\to\infty}\frac{1}{xN_b}\log Z_{\rho,x}(t)=N_1(t).
$$
This limit is taken on each fixed torus. Control of the integral outside the product, the fluctuation determinant, and the normalized hot and mixed activities are separate open estimates.

**Provenance.** Written proof by Codex at the supplied pin, awaiting a separate reader. The bounds use quaternion multiplication, finite-cube character orthogonality and hand-checkable rational inequalities. An auxiliary exact rational check verified the numerical margins and enumerated the 384 contour labels. The proof uses the written identities and bounds throughout. Lean was not run. Credit Tadeusz Bałaban for the gauge-fixed variational method, and Ethan Sussman and Levent Alpoge, with Claude and Codex, for the outline, complete account and contour-kernel construction adapted in Q2. This is research text and grants no scientific or audit status.

## Next two rows and their decisive outcomes

1. **Normalized activities at the nonlinear centre (sketched).** Carry forward row 1480's second follow-up. Expand in the coordinates of (6), retaining the individual block linear terms until their sum vanishes. Retain the Gaussian determinant, Haar and radial amplitudes, the cold complement and the joint hot denominator of row 1480, (10). For $a=1$, $x\ge100$ and the stated stripe interval, a decisive outcome is a common rooted Kotecký–Preiss majorant for the cold, hot and mixed marks on the actual integration domain, or an explicit normalized activity exceeding its rooted budget.
2. **Background response to a local change of source (sketched).** Perturb individual coarse bonds near the tested stripe, including both colours perpendicular to $I$. Determine the spatial dependence of the minimized energy after the coarse data vary independently. A decisive outcome is a volume-independent source neighbourhood with an exponentially decaying bound on mixed derivatives of that energy, sufficient to assign its local terms with a summable tail, or an explicit perturbation for which the branch loses stability or the required decay fails. This would determine how far the stripe extraction can be used on the general small-field domain.
