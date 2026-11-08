# The bare constrained covariance inverse on locally controlled towers

## 1. Scope and sources

Ethan and Levent,

This note supplies a local version of the inverse bound and walk expansion used in your `4.5:rem-covariance-inverse-walks`.
It uses Balaban's literal one-contour averages, a compressed whole-action Hessian, and supplied real gauges on the complete local coefficient reads.
It does not prove your S1–S2 remark on arbitrary separated towers.
Propositions 3.2 and 3.3 concern your broadened tower class and its touching-bond convention.
They say nothing against Balaban's own class or his Theorem 3.3.

All references to your sources are at commit `31a47c543775`.
CA-I means `theorem_0_complete_account_raw_I.tex`; CA-II means `theorem_0_complete_account_raw_II.tex`; CA-III means `theorem_0_complete_account_raw_III.tex`.
Numbers after these names are source lines.
The outline means `YM4_sketch_500.tex` at the same commit.
Your target is CA-I 13142–13173.
Your tower, cube and pairing conventions are at CA-I 12671–12759, 12943–12973 and 11016–11023.

Tadeusz Balaban introduced the averages, projections, inverse operators and walk construction used here.
The paper abbreviations below refer to these works of Balaban.
Your bibliography records them at CA-III 111519–111544.

| Abbreviation | Paper and publication pages |
|---|---|
| CMP 95 | *Propagators and renormalization transformations for lattice gauge theories. I*, Communications in Mathematical Physics **95** (1984), 17–40. |
| CMP 96 | *Propagators and renormalization transformations for lattice gauge theories. II*, Communications in Mathematical Physics **96** (1984), 223–250. |
| CMP 98 | *Averaging operations for lattice gauge theories*, Communications in Mathematical Physics **98** (1985), 17–51. |
| CMP 99b | *Propagators for lattice gauge theories in a background field*, Communications in Mathematical Physics **99** (1985), 389–434. |
| CMP 116 | *Renormalization group approach to lattice gauge field theories. II. Cluster expansions*, Communications in Mathematical Physics **116** (1988), 1–22. |

The relevant formulas are rebuilt below.
Appendix A gives a self-contained proof of the flat inverse estimate used in the main proof, including its commutator estimate.
It is a proof, not an appeal to an unnamed flat estimate.

**Bare versus corrected inverse.** Balaban's first sentence on CMP 99b p. 421 concerns the bare operator.
Later on that page he renames it $`G_0`$ and defines the current-corrected $`G=G_0(I-\Delta'_\pi G_0)^{-1}`$, (3.130).
The displayed (3.132), p. 422, concerns that corrected operator and the version with $`G_1`$.
Your definition at CA-I 13150–13152 uses the bare $`G_0`$.
Theorem PI proves a bound of the scale and spatial-decay form of (3.132) for the bare inverse.
It does not identify the bare and corrected operators.

At CA-II 54617–54619 your text says: "For $`y`$, $`y'`$ in one layer $`\Lambda_{j}`$ the exponential factor in the bound of [CMP 99b, (3.132)–(3.133)] for $`C_{Q}`$ does not depend on $`d(y,y')`$;" (citation key rendered)
On CMP 99b p. 422, (3.132) reads $`|(QGQ^*)^{-1}(y,y')|\le O(1)(L^j\eta)^{-2}(L^{j'}\eta)^{-d}e^{-\delta_1d(y,y')}`$ for $`y\in\Lambda_j`$, $`y'\in\Lambda_{j'}`$.
It decays in $`d(y,y')`$ for all pairs, including pairs in one layer.
This discrepancy is separate from the bare/corrected distinction.

Balaban's displays were read from page images of the journal pages: CMP 99b and CMP 98 by Codex; CMP 99b pp. 421-422 also by Claude; CMP 95 p. 18, (1.6)-(1.7), and CMP 96 p. 231, (2.46), by Claude only. **Who wrote and checked.** The main proof was written by Claude (Opus 5.5) and checked line by line by Codex (gpt-6-astra); the repairs from that check are applied. The flat argument of Appendix A was written by Codex and checked line by line by Claude. Codex prepared this text from those two; Claude checked it line by line against them.
This records model review of research text. It is not an audit and grants no status.
No computer-assisted step discharges an assertion.

## 2. Class and conventions

We work in dimension four with $`G=SU(N)`$, for fixed $`N`$.
Write its Lie algebra as Hermitian traceless matrices, so links are $`e^{iX}`$, and write $`\mathfrak g^c=\mathfrak{sl}(N,\mathbb C)`$.
The trace is normalized by $`\operatorname{tr}1=1`$.
Use operator norms on potentials and normalized Hilbert–Schmidt norms on field coefficients.
Changing between them costs only a constant depending on $`N`$.

### 2.1 Lattices and towers

Fix odd $`L\ge3`$, $`k\ge0`$, $`\eta=L^{-k}`$, and $`\ell_j=L^j\eta`$.
Let $`T_\eta`$ be a periodic fine box whose side is a multiple of $`M_b\ell_k`$, and let $`T^{(j)}=\ell_j\mathbb Z^4\cap T_\eta`$.
Balaban's blocks are corner blocks:

```math
B^j(y)=y+\eta\{0,\ldots,L^j-1\}^4,\qquad y\in T^{(j)}.
```

This is CMP 98 p. 17, (2), and CMP 95 (1.6).
A level-$`j`$ big block has side $`M_b\ell_j`$ and corner in $`M_b\ell_j\mathbb Z^4`$, where $`M_b`$ is a power of $`L`$.
Use your towers from CA-I 12712–12724:

```math
\Omega_0\supset\cdots\supset\Omega_k,\qquad
\ell_j^{-1}\operatorname{dist}(\Omega_j^c,\Omega_{j+1})>RM_b,\quad R\ge R_1,\qquad
\Omega_n=\varnothing\quad(n>k). \tag{T}
```

Each $`\Omega_j`$ is a union of level-$`j`$ big blocks.
Distances in $`T`$ are Euclidean.
The outer region can be any such union, including $`T_\eta`$.
We do not impose Balaban's additional restriction on CMP 99b p. 396 that its big blocks lie within distance $`RM_b\eta`$ of $`\Omega_1`$.
Put $`\Lambda_j=T^{(j)}\cap(\Omega_j\setminus\Omega_{j+1})`$.
Set $`\lambda(x)=\max\{j:x\in\Omega_j\}`$ in $`\Omega_0`$, and $`\lambda(x)=0`$ outside it.

### 2.2 Tested cubes, fields and rows

Your (S1) imposes Balaban's (3.35) on the cubes of size $`O(1)\mathfrak M`$ of the class on which he imposes it (CA-I 12949–12957). We read that class as follows, from CMP 99b p. 396.
Let $`\mathcal C_j`$ consist of the aligned cubes of side $`12M_b\ell_j`$ that lie in $`\Omega_j\setminus\Omega_{j+2}`$ and meet $`\Omega_j\setminus\Omega_{j+1}`$.
Their bonds have both endpoints inside the cube, as at CA-I 11016–11023.
The number 12 is your choice at CA-I 12953–12955, following Balaban, CMP 99b p. 409.
His description on p. 396 allows a size number at least 10.
Proposition 3.2 applies to every such lower size bound; Proposition 3.1 uses size 12.

Field variables are fine bonds with at least one endpoint in $`\Omega_0`$, as at CA-I 12721–12722.
Scalar variables are sites of $`\Omega_0`$.
Extend both by zero outside their variable sets.
A field row of level $`j`$ is a positive bond $`c`$ of $`T^{(j)}`$ with an endpoint in $`\Omega_j`$ and no endpoint in $`\Omega_{j+1}`$.
At level zero these are the field bonds with no endpoint in $`\Omega_1`$.
Thus inward rows are omitted and outward rows are retained.
Its base point $`y_c`$ is its endpoint in $`\Omega_j\setminus\Omega_{j+1}`$, choosing $`c_-`$ if both endpoints lie there.
Site rows are the sites of $`\Lambda_j`$.

The Wilson Hessian is the second variation of the whole action, compressed to the field variables.
It reads every plaquette containing a field bond, including protruding plaquettes.
Your outline makes this convention explicit at line 10287.
Supply the background on the bonds of

```math
\Omega_0^+=\{x:\operatorname{dist}_\infty(x,\Omega_0)\le2\eta\}.
```

Read (S1-loc) below on the bonds of $`N(x)`$ in this domain. Every coefficient read lies there: field bonds touch $`\Omega_0`$, plaquettes through them stay within $`2\eta`$ of $`\Omega_0`$, and a row of level $`j\ge1`$ reads only bonds inside $`\Omega_0`$.

### 2.3 Real gauges and complex twists

Write $`U=e^{i\eta\mathfrak a}U_r`$, with $`U_r`$ unitary.
Your (S1), read on $`\mathcal C_j`$, asks for a unitary gauge on each tested cube with

```math
U_r^u=e^{i\eta A},\qquad \ell_j|A|<a_0,\qquad \ell_j^2|\nabla A|<a_0.
```

This is Balaban, CMP 99b p. 396, (3.35), in your normalization at CA-I 12943–12973.
Here $`\nabla`$ is the flat forward difference.
Your (S2) is $`N_{U_r}(\mathfrak a)<a_1`$, where

```math
N_{U_r}(\mathfrak a)=\max\{\sup m|\mathfrak a|,\ \sup m^2|\nabla_{U_r}\mathfrak a|\}.
```

Use the local scale $`m=\ell_{\lambda(x)}`$ at sites and the larger endpoint scale at bonds.
The norm is read on field bonds, with the difference stencils included; see CA-I 12738–12748.
On the additional background bonds of $`\Omega_0^+`$ with no endpoint in $`\Omega_0`$, impose

```math
\eta|\mathfrak a|<a_1,\qquad \eta^2|\nabla_{U_r}\mathfrak a|<a_1.
\tag{S2+}
```

These differences use bonds of $`\Omega_0^+`$.

The theorem uses the following stronger real-gauge hypothesis.
For every site $`x\in\Omega_0`$, set $`j=\lambda(x)`$ and let $`N(x)`$ be the closed sup-norm box of half-width $`r_N\ell_j`$ about $`x`$.
Assume a unitary gauge on $`N(x)`$ such that, on its bonds in $`\Omega_0^+`$,

```math
U_r^u=e^{i\eta A},\qquad
\ell_{\lambda(z)}|A|\le L^2a_0,\qquad
\ell_{\lambda(z)}^2|\nabla A|\le L^2a_0,
\tag{S1-loc}
```

at both endpoints $`z`$ of each bond of $`N(x)`$.
The level is extended by zero outside $`\Omega_0`$.
The constant $`r_N`$ is fixed in §3.3.
This is a supplied local gauge. It is not a boundary gluing conclusion.

### 2.4 Metric

Use Balaban's lattice-contour metric, CMP 96 p. 231, (2.46), with the outer region replaced by $`T_\eta`$.
On a part of a contour in layer $`j`$, the contour consists of bonds of $`T^{(j)}`$, and its length is counted in units $`\ell_j`$.
Outside $`\Omega_1`$, count in units $`\eta`$.
Take the infimum of these costs over contours between the two tops.
This defines $`d(y,y')`$ on the tops of the extended tower, including every row base point.
The exterior convention agrees with your outline at 10113–10127.
Your outline allows more continuous paths; its metric can be smaller.
All estimates below use the lattice-contour metric just defined.

## 3. Operators, constants and statements

### 3.1 Operators and pairings

For $`R(V)X=VXV^{-1}`$, put

```math
(D_U\lambda)(b)=\eta^{-1}\{R(U_b)\lambda(b_+)-\lambda(b_-)\}.
```

This is Balaban's covariant difference, CMP 99b pp. 391–392; its adjoint is his (3.8).
Let $`\Delta(U)`$ be his Wilson Hessian, (3.10), continued with $`U^{-1}`$ in place of $`U^*`$.
Its explicit plaquette formula is proved in Lemma 5.1.
Use the literal field and site rows $`Q,Q'`$ of Definition 4.3, from CMP 99b pp. 392–393, (3.13)–(3.19).

Fine pairings have weight $`\eta^4\operatorname{tr}`$; top pairings have weight $`\ell_j^4\operatorname{tr}`$ on level-$`j`$ rows.
The multiplier $`\nu`$ has counting pairing.
All transposes are bilinear, as at CA-I 12756–12759.
Write $`m=\ell_j`$ on rows, $`a=m^{-2}`$, and $`K=mQ`$, mapping into counting rows.
Then $`K^T=Q^Tm^{-3}`$, so $`K^TK=Q^TaQ`$.
Define

```math
A_s=D_U^TD_U+Q'^Tm^{-2}Q',\qquad
B_v=\Delta(U)+D_UD_U^T+Q^TaQ,
```

```math
M_5=
\begin{pmatrix}
B_v&-D_U&0&0&-K^T\\
-D_U^T&I&A_s&0&0\\
0&A_s&0&-Q'^T&0\\
0&0&-Q'&0&0\\
-K&0&0&0&0
\end{pmatrix},\qquad X=(A,h,\lambda,\mu,\nu).
```

Let $`M_4`$ be its first four rows and columns, $`M_3`$ its rows and columns 2–4, and $`M_1=A_s`$.
Every coefficient is a differential stencil or an averaging row.
When the inverses exist, put

```math
G'=A_s^{-1},\quad
P=G'Q'^T(Q'G'^2Q'^T)^{-1}Q'G',\quad R=I-P,
```

```math
\Delta_a=\Delta(U)+D_URD_U^T+Q^TaQ,\qquad
G_0=\Delta_a^{-1},\qquad q_0=(QG_0Q^T)^{-1}.
```

These are Balaban's operators, CMP 99b pp. 393–395, (3.21)–(3.27), with your mass from CA-I 13583–13595.
At real $`U`$, $`R`$ is the orthogonal projection onto $`\Delta_U\ker Q'`$.
It is independent of the positive site mass: on $`\ker Q'`$, $`(\Delta_U+Q'^T\alpha Q')\lambda=\Delta_U\lambda`$.

### 3.2 Norms

Use covariant differences at $`U_r`$, with zero extensions at Dirichlet boundaries, and physical fine $`L^2`$ norms.
Set

```math
\begin{split}
\|X\|_{\mathcal X}^2={}&\|\nabla A\|_2^2+\|m^{-1}A\|_2^2+\|h\|_2^2
+\|m^{-2}\lambda\|_2^2+\|m^{-1}D\lambda\|_2^2\\
&+\sum_{\alpha,\beta}\|D_\alpha D_\beta\lambda\|_2^2
+\|m^2\mu\|_{\rm top}^2+\|\nu\|_{\rm count}^2.
\end{split}
```

Restrict this norm to each system's variables.
For $`r=3,4,5`$, let $`\mathcal Y_r=\mathcal X_r^*`$.
For $`r=1`$, use $`M_1:H_m^2\to L^2`$, so $`\mathcal Y_1=L^2`$.
The same local formula defines the model norms.
Fields supported where the model and actual geometry agree have the same norm, including difference stencils.
In particular, for a colour block between two counting-row coordinates,

```math
|W_{\nu\nu}(c,c')|\le\|W\|_{\mathcal Y\to\mathcal X}. \tag{E}
```

The unit source at $`c'`$ has dual norm one, and a $`\nu`$-component is bounded by the output norm.

### 3.3 Order of constants

Fix the constants in this order. They depend only on $`N,L`$.

1. The flat inverse lemma in §4.4 and Appendix A supplies a block size $`M_F`$, gap $`\rho_F`$, inverse bound $`B_F\ge1`$, commutator constant $`C_{\rm com}`$, and cutoff multiplier bound $`c_h\ge1`$, covering all four systems on corner blocks. Put $`\rho'_F=M_F\lceil\rho_F/M_F\rceil`$.
2. Lemma 4.4 supplies $`e_R,C_R`$, with $`r_1=1/(500L)`$. Lemma 5.1 supplies $`e_C\le e_R/L,C_C`$; Lemma 5.2 supplies $`C_S\ge2`$. Put $`C_K=3C_{\rm com}`$ and $`D_*=3(20L)^4`$.
3. Fix one power $`M_t`$ of $`L`$, divisible by $`LM_F`$, such that

```math
M_t\ge\max\{2\rho'_F,4L\},\qquad
\theta=\frac{3B_Fc_h^2C_K}{M_t}\le(4D_*)^{-4}.
```

4. Put $`r_N=7M_t`$, $`\widehat r=(2L+2)M_t`$, and $`D_X=24L^2M_t`$.
5. Put $`\delta_q=\log(1/\theta)/(7D_X)>0`$.
6. Take $`M_b`$ to be a power of $`L`$, divisible by $`M_t`$, and impose

```math
2r_NL+1\le11M_b,\quad R_1\ge24,\quad
R_1M_b\ge\max\{\rho'_F,\ 4L(\widehat r+L)+1,\ 3\log L/\delta_q\}.
```

7. Put

```math
e_L=\min\{e_C,(8B_FC_C)^{-1},C_{\rm com}/(2c_hC_CM_t)\}.
```

Choose $`a_0^*,a_1^*\in(0,1]`$ with $`C_S(L^2a_0^*+a_1^*)\le e_L`$.
8. Put $`C_q=4D_*B_Fc_h^2L\theta^{-1/2}`$.

A different tile size requires recomputing all later constants.
There is no assertion of a radius uniform in $`M_t`$ or $`N`$.
Constants are uniform in depth, mesh, volume, tower and background.
Before applying your kernel algebra, also impose all its shell floors at the common rate used, CA-I 13413–13428.
The scale-ratio floor in item 6 alone is not that whole list.

### 3.4 Theorem PI

A tile of level $`j`$ is a cube of side $`M_t\ell_j`$, with corner in $`M_t\ell_j\mathbb Z^4`$, contained in $`\Omega_j\setminus\Omega_{j+1}`$.
An exterior tile is a level-zero tile disjoint from $`\Omega_0`$ that contains the initial point of a field bond.
Its level is zero.
The centre $`x_\tau`$ is the centre of the run of fine sites in the tile; it is a site because $`M_tL^j`$ is odd.
Let $`F_\tau`$ be the closed sup-norm cube of half-width $`\widehat r\ell_{j_\tau}`$ about $`x_\tau`$.
A walk is $`\omega=(\tau_0,\ldots,\tau_n)`$, with $`n=|\omega|\ge0`$, whose consecutive boxes of half-width $`r_N\ell_{j_\tau}`$ meet.
The same symbol $`|\omega|`$ denotes its footprint $`F_{\tau_0}\cup\cdots\cup F_{\tau_n}`$ when it occurs as a set.

A setting $`s=(\text{tower},U)`$ uses the fixed box and grids above and supplies $`U`$ on $`\Omega_0^+`$.
Two settings agree on $`W`$ if their regions have the same intersection with $`W`$ at every level, and their backgrounds agree on every bond with both endpoints in $`W`$ in their common background domain.
The coefficients compared in §9 read this common domain inside the footprint.

**Theorem PI.** Fix the constants of §3.3. Let $`k\ge0`$, let $`T_\eta`$ be a periodic fine box of side at least $`\max\{(2\widehat r+2)\ell_k,t_FM_F\ell_k\}`$, let the tower satisfy §2.1 with $`R\ge R_1`$, and let $`U=e^{i\eta\mathfrak a}U_r`$ satisfy (S1-loc) with $`a_0\le a_0^*`$, and (S2), (S2+) with $`a_1\le a_1^*`$. The rows are Balaban's literal rows of Definition 4.3.

(a) *Existence and identification.* $`M_1=A_s,M_3,M_4,M_5`$ are invertible. Hence $`Q'G'^2Q'^T,R,\Delta_a,G_0,q_0`$ exist;

```math
q_0=-m^{-3}[M_5^{-1}]_{\nu\nu}m,\qquad q_0^T=q_0.
```

Each is holomorphic in $`\mathfrak a`$ on the set where the hypotheses hold, for fixed $`U_r`$. For $`\mathfrak a`$ with values in $`\mathfrak g`$, so $`U`$ is $`G`$-valued, each is the operator of CMP 99b §3 built with Balaban's averaging, the conventions of §2 and the mass $`a=\ell^{-2}`$ of CA-I 13585.

(b) *Bound of the form of (3.132).* For field rows $`c,c'`$ of levels $`j,j'`$, respectively,

```math
|q_0(c,c')|\le C_q\ell_j^{-2}\ell_{j'}^{-4}e^{-\delta_qd(y_c,y_{c'})},
```

as a density for the top pairing. For $`f`$ supported on rows with base point $`y'`$,

```math
\sup_{\text{rows at }y}|q_0f|\le 2\cdot4C_q\ell_j^{-2}e^{-\delta_qd(y,y')}\sup|f|.
```

(c) *Walk expansion at a fixed setting.* $`q_0=\sum_\omega q_\omega`$, absolutely at each $`(c,c')`$. Each $`q_\omega`$ is holomorphic in $`\mathfrak a`$ and depends on $`U`$ only through
$`X(\omega)=X_{\tau_0}\cup\cdots\cup X_{\tau_n}`$, where $`X_\tau\subset F_\tau`$ is the model's read set in §5.2.
The term vanishes unless $`y_c\in\operatorname{supp}h_{\tau_0}`$ and $`y_{c'}\in\operatorname{supp}h_{\tau_n}`$.
For a nonzero term,

```math
d(\omega,y_c,y_{c'})\le D_X(|\omega|+1),\qquad
|q_\omega(c,c')|\le C_q\ell_j^{-2}\ell_{j'}^{-4}\theta^{|\omega|/2}
e^{-3\delta_qD_X(|\omega|+1)}.
```

Here $`d(\omega,\cdot,\cdot)`$ is the distance of Balaban's CMP 99b p. 410, (3.93): take the infimum of the sum of consecutive $`d`$-distances through intermediate tops in $`F_{\tau_m}`$.

(d) *Majorants.* Split $`\theta^{|\omega|/2}=\theta^{|\omega|/4}\theta^{|\omega|/4}`$.
For each tile, the sum of the first factor over walks starting there, or over walks ending there, is at most $`4/3`$.
The second factor is at most $`(4D_*)^{-|\omega|}`$ and is spare.
For every $`\Lambda\le D_X(|\omega|+1)`$,

```math
e^{-3\delta_qD_X(|\omega|+1)}\le
e^{-\delta_qd(\omega,y_c,y_{c'})}e^{-2\delta_q\Lambda}.
```

This is a geometric walk majorant at the one fixed size $`M_t`$, with two spare exponentials.

(e) *Setting-compatible assignment.* Let $`s,s'`$ satisfy the hypotheses, and let $`\omega`$ be a walk of $`s`$.
If they agree on its footprint, then $`\omega`$ is a walk of $`s'`$ and $`q_\omega^s=q_\omega^{s'}`$.
Thus, on every closed $`W`$ where they agree, the restricted sums
$`q_0^W=\sum_{|\omega|\subset W}q_\omega`$ have the same index set and terms.
The support of $`q_\omega`$ lies at sup-norm distance at least $`(2L+1)M_t\ell_{j_{\tau_0}}`$ from the boundary of its footprint at the first end, and at least $`(2L+1)M_t\ell_{j_{\tau_n}}`$ at the last.
Support here means the base-point coordinates of the kernel, as in (b)–(c).
If support includes an entire row bond, subtract its length from the corresponding margin.

Part (a) does not use a walk decay bound. Parts (c)–(d) imply (b).
Part (e) enlarges the tower read, not the background read $`X(\omega)`$.
It compares settings on fixed grids; it does not assert termwise lattice covariance.

### 3.5 The relation to S1

**Proposition 3.1.** Suppose every $`\Omega_i`$ is a union of cells of a grid aligned with the level-$`i`$ big-block grid, of spacing $`s_i`$, where $`s_i`$ is a multiple of $`M_b\ell_i`$ and $`s_i\ge12M_b\ell_i`$.
With the constants of §3.3, (S1) implies (S1-loc) at every $`x\in\Omega_0`$ with $`N(x)\subset\Omega_0`$.
In particular it does so everywhere if $`\Omega_0=T_\eta`$.
The thickness hypothesis remains in that case.
At boundary points, (S1-loc) remains an additional hypothesis.

**Proposition 3.2.** Let $`G=SU(2)`$. Read the tested cube class as in §2.2, or with any size number at least 10 in place of 12.
Suppose $`\Omega_0`$ contains a finger $`F`$ of $`w\times w\times w\times l`$ level-zero big blocks, with $`w\le9`$, $`l\ge200`$, attached at one end to the rest of $`\Omega_0`$.
Assume $`\Omega_0`$ equals $`F`$ within distance $`31M_b\eta`$ of its middle cross-section, and every point of $`F`$ is more than $`(R+24)M_b\eta`$ from $`\Omega_1`$.
There is a real $`U`$, with $`\mathfrak a=0`$, satisfying (S1) and (S2), at which $`\Delta_a`$ is singular.
Thus $`G_0`$ and $`q_0`$ do not exist there.
There is also such a real $`U'`$ with $`|\partial U'-1|=2`$ on six plaquettes.
It violates the bound at CA-I 12968–12973 when $`a_0+a_1<1/2`$.

**Proposition 3.3.** Let $`G=SU(2)`$ and $`\varnothing\ne\Omega_0\ne T_\eta`$, with §2.2–§2.3's conventions. Require $`T_\eta`$ to have side at least $`\max\{(2\widehat r+2)\ell_k,t_FM_F\ell_k\}`$.
There is a real $`U`$, with $`\mathfrak a=0`$, satisfying (S1) and (S2), at which $`\Delta_a`$ is singular.
It differs from 1 only on one field bond with an endpoint outside $`\Omega_0`$.
By the box hypothesis and Theorem PI, (S1-loc) with $`a_0\le a_0^*`$ must fail at a site whose box contains that bond.

Both constructions also satisfy (S2+).
Proposition 3.2 uses a region excluded by Balaban's restriction on CMP 99b p. 396.
Proposition 3.3 uses touching field bonds, internal tested-cube bonds, and the compressed whole-action Hessian.
Its mechanism does not apply if both fields and plaquettes are restricted to those inside $`\Omega_0`$.
The proofs are in §10.

## 4. Balaban's literal averaging rows

The following construction is Balaban's CMP 98 pp. 23–24, (42)–(43), pp. 27–29, (58)–(63), (89)–(92), and p. 36, (124)–(125).
CMP 99b pp. 392–393, (3.13)–(3.19), uses these rows at the successive averaged backgrounds.
They use one contour per site on corner blocks.
They are not the symmetric contour-family rows used in parts of your outline.

### 4.1 Elementary analytic estimates

**Lemma 4.1.** For matrices in operator norm:

(i) $`|e^X-1|\le e^{|X|}-1\le2|X|`$ if $`|X|\le1`$.

(ii) If $`|H|\le1/2`$, the series $`\log(1+H)=\sum_{n\ge1}(-1)^{n+1}H^n/n`$ converges absolutely, has norm at most $`2|H|`$, and exponentiates to $`1+H`$.
If $`|X|\le1/4`$, then $`\log(e^X)=X`$.
If also $`|gHg^{-1}|\le1/2`$, then $`\log(1+gHg^{-1})=g\log(1+H)g^{-1}`$.

(iii) $`|X_1\cdots X_n-1|\le\prod_i(1+|X_i-1|)-1`$.

(iv) If $`f`$ is holomorphic and bounded by $`K`$ on the radius-$`r`$ ball, then, for $`|z|\le r/2`$,

```math
|f(z)-f(0)|\le2K|z|/r,\qquad
|f(z)-f(0)-Df(0)z|\le2K|z|^2/r^2.
```

If $`f(z,w)`$ is bounded by $`K`$ on the product of two radius-$`r`$ balls, then

```math
|D_wf(z,0)w-D_wf(0,0)w|\le2K|z||w|/r^2.
```

*Proof.* Compare the absolutely convergent power series for (i)–(iii).
The identities in (ii) hold in the commutative algebra generated by the one matrix.
Conjugation commutes term by term with the logarithm series.
For (iv), set $`s=|z|`$ and $`g(t)=f(tz/s)`$.
Cauchy's estimate on $`|t|<r`$ bounds the coefficient of $`t^n`$ by $`Kr^{-n}`$.
Sum the first and second tails at $`t=s\le r/2`$.
For the mixed assertion, apply Cauchy first in $`u`$ to $`f(tz/s,uw/|w|)`$.
Its $`u`$-derivative at zero is bounded by $`K/r`$; apply the first estimate in $`t`$.
The zero-vector cases follow by continuity. $`\square`$

### 4.2 One step

Work from level $`m`$ to $`m+1`$ in units $`\ell_m=1`$.
Let $`c`$ be a coarse positive bond in direction $`\mu`$, let $`D(c)=B(c_-)\cup B(c_+)`$, and let $`E(c)`$ be the fine bonds with both endpoints in $`D(c)`$.
The axial contour $`\Gamma_{y,x}`$ changes coordinates in order $`4,3,2,1`$.
For $`x\in B(c_-)`$, put $`x(c)=x+Le_\mu`$ and concatenate

```math
\Gamma_{c,x}=\Gamma_{c_-,x}\cup[x,x(c)]\cup\Gamma_{x(c),c_+}.
```

Write $`W(c)`$ for the product on the straight coarse-bond path, and $`W(\Gamma)`$ for an ordered contour product.
These are Balaban's contours, CMP 98 pp. 19, 24, following CMP 95 (1.7).
Use $`W_b^g=g(b_-)W_bg(b_+)^{-1}`$ and bondwise multiplication $`V_1V_0`$.

**Definition 4.2.** Balaban's absolute and relative averages are

```math
\begin{aligned}
\mathcal A(W)_c&=\exp\!\left[\sum_{x\in B(c_-)}L^{-4}\log\{W(\Gamma_{c,x})W(c)^{-1}\}\right]W(c),\\
z_W(y)&=\exp\!\left[\sum_{x\in B(y)}L^{-4}\log W(\Gamma_{y,x})\right],\\
v(y)&=\exp\!\left[-\sum_{x\in B(y)}L^{-4}
\log\{(V_1V_0)(\Gamma_{y,x})V_0(\Gamma_{y,x})^{-1}\}\right],\\
\mathcal R(V_0;V_1)_c&=v(c_-)\mathcal A(V_1V_0)_cv(c_+)^{-1}\mathcal A(V_0)_c^{-1}.
\end{aligned}
```

The product of transported $`V_1`$'s in CMP 98 p. 27, (58), telescopes to $`(V_1V_0)(\Gamma)V_0(\Gamma)^{-1}`$.
Thus $`v`$ is (62).
The last two factors in (63) obey
$`R(\mathcal A(V_0)_c)v(c_+)^{-1}=\mathcal A(V_0)_cv(c_+)^{-1}\mathcal A(V_0)_c^{-1}`$, giving the displayed multiplication order.
For $`z=z_{e^{ib}}`$, define

```math
F(b)_c=\frac1i\log\{z(c_-)^{-1}\mathcal A(e^{ib})_cz(c_+)\},\qquad
\Phi(b,a)_c=\frac1i\log\mathcal R(e^{ib};e^{ia})_c.
```

Let

```math
(Sb)_c=L^{-4}\sum_{x\in B(c_-)}\sum_{t=0}^{L-1}b_\mu(x+te_\mu).
```

**Lemma 4.2.** Put $`r_1=1/(500L)`$ and suppose $`|b|,|a|<r_1`$ on $`E(c)`$.

(i) All logarithm arguments above lie within $`1/2`$ of 1.
The maps are holomorphic, $`|F|,|\Phi|\le1`$, and $`|z^{\pm1}-1|\le1/50`$.

(ii) $`F(0)=0`$, $`z(0)=1`$, $`\Phi(b,0)=0`$, $`\Phi(0,a)=F(a)`$, and $`DF(0)=D_a\Phi(0,0)=S`$.

(iii) For a unitary gauge $`g`$, or a complex gauge with $`|g^{\pm1}-1|\le1/10`$,

```math
\mathcal A(W^g)_c=g(c_-)\mathcal A(W)_cg(c_+)^{-1},\qquad
\mathcal R(V_0^g;\operatorname{Ad}_gV_1)_c
=g(c_-)\mathcal R(V_0;V_1)_cg(c_-)^{-1}.
```

The adjoint action on a bond is at its initial point.

(iv) For $`|b|\le r_1/2`$,

```math
|F(b)-Sb|\le2|b|^2/r_1^2,\qquad |z^{\pm1}-1|\le|b|/r_1.
```

Every entry of $`Q^{\rm ang}(e^{ib}):=D_a\Phi(b,0)`$ differs from the corresponding entry of $`S`$ by at most $`2|b|/r_1^2`$.

(v) $`S`$ has row sum $`L`$ and column sum $`L^{-3}`$.
A row of $`Q^{\rm ang}`$ reads at most $`8L^4`$ bonds, and a bond is read by at most 16 rows.

(vi) $`\mathcal A,F,\Phi`$ read only $`E(c)`$, and $`z(y)`$ reads only the bonds inside $`B(y)`$.

*Proof.* The two axial paths have at most $`4(L-1)`$ bonds each.
Together with the two straight paths, the absolute-loop argument has at most $`10L`$ factors $`e^{\pm ib}`$.
Lemma 4.1 bounds its error by $`e^{1/50}-1<0.021`$, its logarithm by $`0.042`$, and $`|\mathcal A(e^{ib})-1|`$ by $`e^{0.042}e^{Lr_1}-1<0.046`$.
The relative-contour arguments have at most $`12L`$ factors of the two types, with bound $`e^{24Lr_1}-1<0.05`$.
Consequently $`|v^{\pm1}-1|<0.11`$ and $`|\mathcal A(e^{ia}e^{ib})-1|<0.09`$.
Thus

```math
|\mathcal R-1|<(1.11)^2(1.09)(1.046)-1<0.41,\qquad |\Phi|<0.82.
```

For $`z`$, the $`4L`$-factor estimate gives $`|z^{\pm1}-1|<e^{0.018}-1<1/50`$.
The argument defining $`F`$ differs from 1 by less than $`(1.02)^2(1.046)-1<0.09`$, so $`|F|<0.18`$.
These decimal bounds follow by comparing the exponential series with geometric tails; no numerical enclosure is used.
Finite compositions of the convergent series are holomorphic.

At $`V_1=1`$, $`v=1`$ and the relative average is 1.
At $`V_0=1`$, $`v=z_{V_1}^{-1}`$, so $`\Phi(0,a)=F(a)`$.
At first order the exponent of $`z(c_-)^{-1}\mathcal A z(c_+)`$ is $`iL^{-4}`$ times

```math
\sum_{x\in B(c_-)}\{-b(\Gamma_{c_-,x})+b(\Gamma_{c_-,x})
+b([x,x(c)])-b(\Gamma_{c_+,x(c)})\}
+\sum_{x'\in B(c_+)}b(\Gamma_{c_+,x'}).
```

The first endpoint factors cancel the first axial paths.
The map $`x\mapsto x(c)`$ is a bijection of the two blocks, so the other endpoint factors cancel the last axial paths.
The remainder is $`iSb`$.

For covariance, every logarithm involved is the logarithm of a closed relative contour.
It is conjugated at its starting point under $`g`$.
Unitary conjugation preserves its norm.
The stated complex gauges cost at most $`(11/10)^2`$; even the largest margin obeys
$`(41/100)(121/100)=4961/10000<1/2`$.
Lemma 4.1 therefore moves $`g`$ through each logarithm and exponential.
Multiplying the endpoint factors gives (iii).
This argument does not require transformed links themselves to remain in the original potential ball.

Apply Lemma 4.1(iv) to $`F`$, $`z^{\pm1}-1`$, and $`\Phi(b,uw e_{b'})`$ for $`|w|\le1`$ to obtain (iv).
For (v), the row sum is $`L^{-4}L^4L=L`$.
A fixed parallel fine bond lies in exactly $`L`$ translated straight segments, giving column sum $`L^{-3}`$.
The double block has at most $`4\cdot2L^4`$ positive bonds.
A bond belongs to at most $`2\cdot2\cdot4`$ double blocks.
All displayed formulas read only the stated contours, proving (vi). $`\square`$

### 4.3 Iteration and comparison

**Definition 4.3.** Put $`\bar U^0=U`$, $`\bar U^{m+1}=\mathcal A(\bar U^m)`$, and

```math
\mathcal R^0(U;V_1)=V_1,\qquad
\mathcal R^{m+1}(U;V_1)=\mathcal R(\bar U^m;\mathcal R^m(U;V_1)).
```

For a level-$`j`$ field row, $`j\ge1`$, define

```math
(Q_j(U)A)_c=\ell_j^{-1}\left.\frac d{ds}\right|_{s=0}
\frac1i\log\mathcal R^j(U;e^{is\eta A})_c,\qquad Q_0=I.
```

For a site row $`y`$, let $`x_m`$ be the corner of the level-$`m`$ block containing $`x`$, with $`x_j=y`$, and set

```math
\begin{split}
U(\Gamma^{(j)}_{y,x})&=\bar U^{j-1}(\Gamma_{x_j,x_{j-1}})\cdots
\bar U^1(\Gamma_{x_2,x_1})U(\Gamma_{x_1,x}),\\
(Q'_j(U)\lambda)(y)&=L^{-4j}\sum_{x\in B^j(y)}R(U(\Gamma^{(j)}_{y,x}))\lambda(x),\qquad Q'_0=I.
\end{split}
```

These are CMP 98 pp. 28–29, (89)–(92) and its contour variables, and CMP 99b pp. 392–393, (3.13)–(3.19).
Since $`\mathcal R(V_0;1)=1`$, the chain rule gives Balaban's (3.15):

```math
Q_j(U)=L^{-j}Q^{\rm ang}(\bar U^{j-1})\cdots Q^{\rm ang}(U).
```

In potential normalization each flat one-step factor is $`L^{-1}S`$, as in CMP 98 p. 36, (124)–(125).

**Lemma 4.4.** There are $`e_R\in(0,r_1/3]`$ and $`C_R`$, depending only on $`N,L`$, with the following properties.
Let $`c`$ have level $`j\ge1`$, let $`D=B^j(c_-)\cup B^j(c_+)`$, and let $`E`$ be its internal fine bonds.
Suppose $`U=(e^{i\eta B})^u`$ on $`E`$, with $`u`$ unitary and $`\epsilon=\ell_j\max_E|B|\le e_R`$.

(i) All row logarithms have arguments within $`1/2`$ of 1.
The rows are holomorphic in $`B`$.
A field row reads only $`E`$; a site row reads only its block.

(ii) $`Q_j(U^g)=\operatorname{Ad}_gQ_j(U)\operatorname{Ad}_g^{-1}`$ and $`Q'_j(U^g)=\operatorname{Ad}_gQ'_j(U)\operatorname{Ad}_g^{-1}`$ for unitary $`g`$.
Use initial points for fields and field rows, and sites for scalar components.

(iii) At identity,

```math
Q_j(1)A_c=L^{-5j}\sum_{x\in B^j(c_-)}\sum_{t=0}^{L^j-1}A_\mu(x+t\eta e_\mu),\qquad
Q'_j(1)\lambda(y)=L^{-4j}\sum_{x\in B^j(y)}\lambda(x).
```

(iv) For $`u=1`$, both row error sums are at most $`C_R\epsilon`$.
For a family of level-$`j`$ rows controlled by one $`B`$ on their union of reads, the corresponding column error sums are at most $`C_R\epsilon(\eta/\ell_j)^4`$.
Entry norms are operator norms between normalized Hilbert–Schmidt colour spaces.

*Proof.* Lemma 4.2(iii) and induction give covariance of $`\bar U^m`$ and $`\mathcal R^m`$.
Differentiation gives the field-row formula.
The contour products telescope under a gauge to $`g(y)U(\Gamma^{(j)}_{y,x})g(x)^{-1}`$, giving the site formula.
Unitary conjugation preserves the logarithm margins, so it remains to work with $`u=1`$.

Normalize $`\ell_j=1`$ and put $`s_m=L^{m-j}`$, $`b_0=\eta B`$.
Define

```math
b_{m+1}=F(b_m),\quad z_m=z_{e^{ib_m}},\quad t_0=1,\quad t_{m+1}=t_mz_m,\qquad
C_F=4/(Lr_1^2),\quad P_m=\prod_{i<m}(1+C_F\epsilon s_i).
```

Choose $`e_R`$ so that

```math
e_R\le r_1/3,\quad C_Fe_R\le(L-1)\log(3/2),\quad e_R\le r_1(L-1)/30.
```

We claim, for $`0\le m\le j`$,

```math
|b_m|\le\epsilon s_mP_m,\quad P_m\le3/2,\quad
|t_m^{\pm1}-1|\le3\epsilon/[r_1(L-1)]\le1/10,\quad
\bar U^m=(e^{ib_m})^{t_m}.
```

The claim holds at zero.
If it holds at $`m`$, Lemma 4.2 and the row sum of $`S`$ give

```math
|b_{m+1}|\le L|b_m|\left(1+\frac{2|b_m|}{Lr_1^2}\right)
\le\epsilon s_{m+1}P_m(1+C_F\epsilon s_m).
```

Since $`\sum_{m<j}s_m<1/(L-1)`$, $`P_{m+1}\le3/2`$.
Also $`|z_i^{\pm1}-1|\le(3/2)\epsilon s_i/r_1`$; the product bound gives the stated estimate on $`t_{m+1}`$.
Covariance under this small complex gauge gives

```math
\bar U^{m+1}=\mathcal A((e^{ib_m})^{t_m})
=((e^{ib_{m+1}})^{z_m})^{t_m}=(e^{ib_{m+1}})^{t_mz_m}.
```

This closes the induction and keeps every logarithm inside its margin.

For field rows, the middle factors cancel exactly as $`t_m^{-1}t_{m-1}=z_{m-1}^{-1}`$ on level-$`m`$ sites.
Thus

```math
L^jQ_j(U)=\operatorname{Ad}_{t_{j-1}}A_{j-1}\cdots A_0,\qquad
A_m=Q^{\rm ang}(e^{ib_m})\operatorname{Ad}_{z_{m-1}^{-1}},\quad A_0=Q^{\rm ang}(e^{ib_0}).
```

Lemma 4.2 gives, for a fixed $`C_1=C_1(N,L)`$,

```math
\|A_m-S\|_{\rm row}\le C_1L\epsilon s_m,\qquad
\|A_m-S\|_{\rm col}\le C_1L^{-3}\epsilon s_m.
```

Both matrix norms are submultiplicative.
Choose also $`C_1e_R\le(L-1)\log(3/2)`$.
The telescoping product identity then bounds the row error before the $`L^{-j}`$ factor by

```math
\sum_{q<j}\tfrac32L^{j-q-1}C_1L\epsilon s_qL^q
\le\frac{3C_1\epsilon L^j}{2(L-1)}.
```

The column calculation has $`L^{-3j}`$ in place of $`L^j`$.
The endpoint conjugation adds at most $`C_N6\epsilon/[r_1(L-1)]`$ times the product norm.
After multiplication by $`L^{-j}`$, these are the claimed $`C_R\epsilon`$ and $`C_R\epsilon L^{-4j}`$ bounds.
The same calculation on a union of read sets proves the family column assertion.

At zero background the straight means compose to the long straight mean.
Indeed each starting site has a unique coarse offset and fine offset; the successive path offsets $`t'L^m+t`$ run once through $`0,\ldots,L^{m+1}-1`$.
The averaging weights multiply. This proves (iii).

For site rows write $`W_m=e^{ib_m}(\Gamma_{x_{m+1},x_m})`$.
The contour variable is

```math
t_{j-1}(y)W_{j-1}z_{j-2}(x_{j-1})^{-1}W_{j-2}\cdots z_0(x_1)^{-1}W_0.
```

Each $`W_m`$ has at most $`4L`$ factors, so $`|W_m-1|\le12L\epsilon s_m`$.
The geometric sum in $`s_m`$ bounds the whole product's error by $`C\epsilon`$.
The adjoint error is at most $`C_N`$ times that error on a smaller fixed ball.
The weights in one block sum to one; each fine site belongs to one block at a given level.
These facts give the site row and column bounds.
Shrink $`e_R`$ to meet this last smallness condition and enlarge $`C_R`$ to cover all bounds. $`\square`$

### 4.4 Flat inverse and coordinates

**Lemma 4.5.** Put $`h_j=(L^j-1)\eta(1,1,1,1)/2`$.
Translate fine sites and fine bonds by $`-h_k`$.
Separately relabel a level-$`j`$ site row, or both endpoints of a field row, by

```math
y\longmapsto y'=y+h_j-h_k
=y-\ell_j\frac{L^{k-j}-1}{2}(1,1,1,1).
```

This relabelling preserves the level-$`j`$ row grid.
The translated corner block is the centred block about $`y'`$.
These separate permutations conjugate the flat mixed matrices and preserve their inverse bounds.

*Proof.* Oddness makes $`(L^{k-j}-1)/2`$ an integer, and

```math
(L^k-1)/2=L^j(L^{k-j}-1)/2+(L^j-1)/2.
```

Therefore

```math
B^j(y)-h_k=y'+\eta\{-(L^j-1)/2,\ldots,(L^j-1)/2\}^4.
```

Straight paths translate to those of the relabelled row, and block means have the same correspondence.
Translate regions as unions of blocks.
Layer membership and outward-row membership are preserved under these identifications.
Fine and row pairings are unchanged, and differential operators translate on fine coordinates.
This proves the conjugacy.
The fine translation alone need not preserve the coarse grids. $`\square`$

**Flat inverse lemma.** There are $`M_F,\rho_F,t_F`$ and $`B_F\ge1`$, depending only on $`L`$, and for each $`C_\varphi`$ there are $`c_h\ge1`$ and $`C_{\rm com}`$, depending only on $`L`$ and $`C_\varphi`$, such that the following holds.
Let the periodic box have side at least $`t_FM_F\ell_k`$.
Let $`\Omega'_0\supset\cdots\supset\Omega'_k`$ be nested unions of blocks of side $`M_F\ell_n`$ in a nested block grid, with

```math
\ell_n^{-1}\operatorname{dist}((\Omega'_n)^c,\Omega'_{n+1})\ge\rho_F.
```

Use §2's rows, corner blocks and Dirichlet conventions, with empty terminal regions allowed.
Then $`M_r(1)`$, $`r\in\{1,3,4,5\}`$, is invertible and

```math
\|M_r(1)^{-1}\|_{\mathcal Y_r\to\mathcal X_r}\le B_F.
```

Its vector Schur complement is positive and controls the squared energy norm.
Let $`M\ge1`$ and $`0\le n\le k`$, and let $`h`$ take values in $`[0,1]`$, with $`|Dh|\le C_\varphi/(M\ell_n)`$, $`|D^2h|\le C_\varphi/(M\ell_n)^2`$, and local scale at most $`L\ell_n`$ on the read closure of $`\operatorname{supp}h`$.
Then multiplication by $`h`$ has norm at most $`c_h`$ on $`\mathcal X_r`$ and on $`\mathcal Y_r`$, and

```math
\|[M_r(1),h]X\|_{\mathcal Y_r}\le(C_{\rm com}/M)\|X\|_{\mathcal X_r}.
```

Appendix A proves this statement.
It rebuilds Balaban's one-scale and two-scale arguments and his partition-of-unity construction: CMP 95, Proposition 1.1, (1.89)–(1.90); CMP 96, (2.95)–(2.141), Propositions 2.5–2.6.
The paper page ranges are CMP 95 pp. 17–40 and CMP 96 pp. 239–248; the block-face calculation is on CMP 96 pp. 244–246, (2.123)–(2.128).
Read the straight average directly on corner blocks.
The cutoff argument uses oscillation across a double block, so it also permits the row reference point at the corner.
Choose its constants for that convention before §3.3's choices.
Lemma 4.5 gives the alternative transfer of the inverse bound from centred coordinates.

## 5. Local models

### 5.1 Coefficient comparison

On a flat-admitted geometry let $`B`$ be a complex potential on the full coefficient read, and put

```math
e(B)=\max\{m|B|+m^2|\partial B|\}.
```

Here $`\partial`$ is the flat difference and $`m\le\ell_k=1`$.

**Lemma 5.1.** There are $`e_C>0,C_C`$, depending only on $`N,L`$, such that, if $`e(B)\le e_C`$, every coefficient of $`M_r(e^{i\eta B})`$ is defined and holomorphic, and

```math
\|M_r(e^{i\eta B})-M_r(1)\|_{\mathcal X^0\to\mathcal Y^0}\le C_Ce(B),\qquad r\in\{1,3,4,5\}.
```

The superscript zero denotes flat differences.
If $`A'`$ is real and $`e(A')\le e_C`$, its covariant norms lie between $`(1+C_Ce(A'))^{-1}`$ and $`1+C_Ce(A')`$ times the flat norms.

*Proof.* A level-$`j`$ field row reads only its double block, in layers $`j-1,j`$, where $`m\ge\ell_j/L`$.
Lemma 4.4 applies with $`\epsilon=Le(B)`$ if $`Le_C\le e_R`$.
For $`T=Q(U)-Q(1)`$, Cauchy–Schwarz in its absolute entry weights gives

```math
\begin{split}
\sum_c\ell_j^2|(Tv)_c|_2^2
&\le\ell_j^2\|T\|_{\rm row}\sum_{b'}\left(\sum_c|T(c,b')|\right)|v_{b'}|_2^2\\
&\le(C_RLe)^2\ell_j^2(\eta/\ell_j)^4\sum_{b'}|v_{b'}|_2^2
\le(C_RLe)^2\|m^{-1}v\|_2^2.
\end{split}
```

Only two adjacent row heights read a fine bond, which costs a fixed factor.
The same calculation for site rows gives

```math
\|m^{-2}(Q'(U)-Q'(1))\lambda\|_{\rm top}\le C_RLe\|m^{-2}\lambda\|_2.
```

The flat row counts and Jensen bound $`K(1)`$ by $`C\|m^{-1}v\|_2`$.
In each mass block replace both factors:

```math
K(U)^TK(U)-K(1)^TK(1)
=(K(U)-K(1))^TK(U)+K(1)^T(K(U)-K(1)).
```

The site mass has the same decomposition.
Duality bounds the transposes.
Site means and their transposes are also bounded in the weighted $`L^2`$ spaces used by the strong $`A_s`$ block.
Level-zero rows are identities and do not vary.

For differences,

```math
(D_U-D_1)\lambda(b)=c_b\lambda(b_+),\qquad
c_b=\eta^{-1}(\operatorname{Ad}e^{i\eta B_b}-1).
```

The exponential series gives $`|c_b|\le Ce/m`$ and $`|\partial c_b|\le Ce/m^2`$.
Neighbouring scales differ by at most $`L`$.
The first- and second-difference product rules therefore imply

```math
\|(D_U^TD_U-D_1^TD_1)\lambda\|_2
\le Ce(\|m^{-2}\lambda\|_2+\|m^{-1}D\lambda\|_2).
```

They also give the $`Ce\|v\|_E\|w\|_E`$ form bound for $`D_UD_U^T-D_1D_1^T`$, and the corresponding mixed-block bounds.
Here $`\|v\|_E^2=\|\nabla v\|_2^2+\|m^{-1}v\|_2^2`$.

For the Hessian, use Balaban's plaquette expansion, CMP 99b pp. 391–392, (3.10).
Let $`P=U(\partial p)`$, transport the four signed field values $`v'_a`$ to its base point, and put $`X_v=\sum_a v'_a`$.
Expand $`\operatorname{tr}(2-W-W^{-1})/2`$ with $`W=E(s)P`$, where $`E(s)`$ is the ordered product of $`e^{is\eta v'_a}`$.
The second derivative and its polarization are

```math
\Psi_p(v,v)=\frac{\eta^2}{2}\operatorname{tr}\!\left[X_v^2(P+P^{-1})
+\sum_{a<b}[v'_a,v'_b](P-P^{-1})\right],
```

```math
\Psi_p(v,w)=\frac{\eta^2}{4}\operatorname{tr}\!\left[(X_vX_w+X_wX_v)(P+P^{-1})
+\sum_{a<b}([v'_a,w'_b]+[w'_a,v'_b])(P-P^{-1})\right].
```

At identity this is $`\eta^2\operatorname{tr}(X_v^1X_w^1)=\eta^4\operatorname{tr}((dv)(p)(dw)(p))`$.
Now $`P+P^{-1}=2+(P-1)^2P^{-1}`$, and the product expansion around a plaquette gives

```math
|P-1|\le C\eta^2(|\partial B|+|B|^2)\le C\eta^2e/m^2.
```

The raw remainder is bounded by $`C|P-1|\eta^2|v||w|`$, hence by $`Ce\eta^4m^{-2}|v||w|`$.
Transports differ from 1 by at most $`C\eta e/m`$, so
$`|X_v-X_v^1|\le C\eta e m^{-1}|v|`$, while $`|X_v^1|=\eta|(dv)(p)|`$.
Sum over plaquettes; each bond belongs to six.
This gives the required Hessian form bound, including its curvature term.
At the boundary use zero extensions; protruding plaquettes read the supplied background on $`\Omega_0^+`$.

Adding the finitely many blocks proves the operator bound.
The first- and second-difference comparison at real $`A'`$ proves the norm equivalence.
Holomorphy follows from Lemma 4.4 for rows and from finite products of $`e^{\pm i\eta B}`$ for the other coefficients. $`\square`$

### 5.2 Tiles, cutoffs and reads

The construction follows Balaban's local-model and walk method, CMP 99b pp. 409–416, (3.87)–(3.108).
We specify the footprints separately because the normalization of a cutoff reads neighbouring tiles.

**Tiles and exterior anchors.** Divisibility of $`M_b`$ by $`M_t`$ tiles each layer with the cubes of §3.4.
For each exterior tile choose the first field bond with initial point there, in a fixed lexicographic order of initial points and directions.
Let $`z_\tau`$ be its interior endpoint.
Then

```math
|z_\tau-x_\tau|_\infty\le(M_t-1)\eta/2+\eta.
```

Its model is entirely bare by the first gap.
Use the gauge supplied at $`z_\tau`$, not a gauge at the exterior centre.

**Cutoffs.** Fix a smooth $`\phi:\mathbb R^4\to[0,1]`$, equal to one on $`[-1/2,1/2]^4`$ and supported in $`[-1,1]^4`$.
Set

```math
b_\tau(x)=\phi\!\left(\frac{x-x_\tau}{M_t\ell_{j_\tau}}\right),\qquad
h_\tau(x)=\frac{b_\tau(x)}{(\sum_\sigma b_\sigma(x)^2)^{1/2}}.
```

Evaluate at initial points for fine bonds, at sites for scalars, and at base points for rows.
Every active reference point belongs to a tile where its bump is one.
The denominator is therefore at least one, and $`\sum h_\tau^2=1`$ on every component.
If overlapping bumps had heights differing by two, $`T`$ would put their tiles farther apart than the reach of the bumps.
Thus only adjacent heights overlap.
Differentiating the normalized smooth functions gives

```math
|Dh_\tau|\le C_L/(M_t\ell_{j_\tau}),\qquad
|D^2h_\tau|\le C_L/(M_t\ell_{j_\tau})^2.
```

Only active coordinates need the denominator; use extensions for unused coordinates.

**Two levels.** Let $`F_\tau^+`$ have half-width $`(\widehat r+L)\ell_{j_\tau}`$.
It meets at most two adjacent levels, say $`i,i+1`$, and $`j_\tau\in\{i,i+1\}`$.
A point of level at most $`j_\tau-2`$ lies outside $`\Omega_{j_\tau-1}`$, more than $`RM_b\ell_{j_\tau}/L`$ from the centre.
A point of level at least $`j_\tau+2`$ lies in $`\Omega_{j_\tau+2}`$, more than $`RM_b\ell_{j_\tau+1}`$ away.
Both exceed the Euclidean radius $`2(\widehat r+L)\ell_{j_\tau}`$.
Levels $`j_\tau-1`$ and $`j_\tau+1`$ are separated by more than the diameter $`4(\widehat r+L)\ell_{j_\tau}`$.
The floor in §3.3 guarantees these inequalities.
The exterior case uses the extended level zero and the same exclusion of higher levels.

**Models.** Let $`N_\tau`$ have half-width $`r_N\ell_{j_\tau}`$, and let $`i_\tau`$ be the least level it meets.
Take the smallest cube $`C_\tau`$, aligned with the $`M_F\ell_{i_\tau+1}`$ grid, containing the half-width $`4M_t\ell_{j_\tau}`$ box.
Rounding adds at most $`M_F\ell_{i_\tau+1}\le M_t\ell_{j_\tau}`$.
For $`n\ge i_\tau+1`$, put $`K_n=C_\tau`$.
For $`n\le i_\tau`$, enlarge $`C_\tau`$ on every side by $`\sum_{p=n}^{i_\tau}\rho'_F\ell_p\le2\rho'_F\ell_{j_\tau}\le M_t\ell_{j_\tau}`$.
Set

```math
\Omega_n^\tau=\Omega_n\cap K_n.
```

These are nested unions of the blocks required by the flat inverse lemma.
For $`n\le i_\tau`$, their gap is at least
$`\min\{RM_b,\rho'_F\}\ell_n\ge\rho_F\ell_n`$; all levels $`n\ge i_\tau+2`$ are empty.
Thus the model is admitted.

Build $`M_{r,\tau}(U)`$ on this geometry, with its actual rows and zero extensions.
Its read set $`X_\tau`$ consists of its field bonds, the bonds of plaquettes through them, and the double blocks of its rows.
These lie within half-width

```math
(6M_t+2L+2)\ell_{j_\tau}\le7M_t\ell_{j_\tau}=r_N\ell_{j_\tau}.
```

For an exterior tile the read is within $`6M_t\eta+2\eta`$ of $`x_\tau`$.
It lies in $`N(z_\tau)`$, since $`6M_t+2+M_t/2+1\le7M_t`$.

**Agreement.** On $`C_\tau`$, model and actual levels agree.
They therefore have the same coefficients on the box $`A_\tau`$ of half-width $`3M_t\ell_{j_\tau}`$, whenever the full stencil or row read lies there.
Membership of a row reads its endpoints; its value reads its double block.
Every read meeting $`\operatorname{supp}h_\tau`$ lies within half-width $`(M_t+2L)\ell_{j_\tau}\le3M_t\ell_{j_\tau}`$.
Thus agreement includes the entire commutator read.

**Diameter.** For any two tops $`p,p'\in F_\tau`$,

```math
d(p,p')\le D_X=24L^2M_t.
```

Only levels $`i,i+1`$ occur in $`F_\tau^+`$.
Move a level-$`i`$ top to the corner of its containing level-$`(i+1)`$ block along at most $`4(L-1)`$ level-$`i`$ bonds.
That block lies in the lower layer because it contains a point outside $`\Omega_{i+1}`$.
Leave a level-$`(i+1)`$ top fixed.
Do this at both ends, then join the resulting corners by a level-$`(i+1)`$ coordinate staircase.
In the lower layer split each such bond into $`L`$ level-$`i`$ bonds.
This is an admissible contour inside $`F_\tau^+`$.
Its cost is at most

```math
8(L-1)+4L(2\widehat r+1)
\le16L(L+1)M_t+12L\le24L^2M_t.
```

**Overlap and intersection.** If $`N_\sigma\cap N_\tau\ne\varnothing`$, their heights differ by at most one and
$`|x_\sigma-x_\tau|_\infty\le7M_t(\ell_{j_\sigma}+\ell_{j_\tau})`$.
The possible centres per coordinate number at most $`29`$, $`15+14/L`$, and $`14L+15`$ at equal, larger and smaller height, respectively.
Each is at most $`20L`$.
Hence at most $`D_*=3(20L)^4`$ such tiles occur, and a point belongs to at most $`D_*`$ boxes $`N_\tau`$.
For consecutive footprints, each coordinate intersection length is at least

```math
\min\{2\widehat r\min(\ell_{j_\tau},\ell_{j_\sigma}),
(\widehat r-r_N)(\ell_{j_\tau}+\ell_{j_\sigma})\}.
```

Both entries are at least $`M_t\ell_i`$, with $`\ell_i`$ the smaller tile scale.
Since $`M_t\ge L`$, the intersection contains a level-$`(i+1)`$ grid point.
It is a top in one of the two layers.
In particular consecutive footprints have a positive-volume overlap.

### 5.3 Local inversion

**Lemma 5.2.** Under (S1-loc), (S2), (S2+) with $`L^2a_0,a_1\le1/8`$, use the gauge at $`z=x_\tau`$, or at $`z=z_\tau`$ for an exterior tile.
On $`X_\tau`$, write $`U_r^u=e^{i\eta A}`$ and

```math
U^u=e^{i\eta B},\qquad
B=(i\eta)^{-1}\log(e^{i\eta\mathfrak a^u}e^{i\eta A}),\quad
\mathfrak a^u(b)=\operatorname{Ad}_{u(b_-)}\mathfrak a(b).
```

With the model scale,

```math
e(B)\le C_S(L^2a_0+a_1),\qquad e(A)\le2L^2a_0. \tag{5.4}
```

*Proof.* Gauge covariance gives $`U^u=e^{i\eta\mathfrak a^u}U_r^u`$.
The model scale never exceeds the actual extended scale: they agree on $`C_\tau`$, decrease on its collar, and equal $`\eta`$ outside $`\Omega_0`$.
Thus $`m|A|,m^2|\partial A|\le L^2a_0`$ and
$`m|\mathfrak a^u|,m^2|\nabla_{e^{i\eta A}}\mathfrak a^u|<a_1`$.
The flat difference of the twist is bounded by its covariant difference plus $`C|A||\mathfrak a^u|`$.
The analytic remainder $`\rho(X,Y)=\log(e^Xe^Y)-X-Y`$ vanishes on both axes.
Its convergent series, or Lemma 4.1 on its partial derivatives, gives

```math
|\rho(X,Y)|\le C|X||Y|,\quad
|\rho(X',Y')-\rho(X,Y)|\le C(|X'-X||Y'|+|X||Y'-Y|).
```

Apply this to $`X=i\eta\mathfrak a^u,Y=i\eta A`$, divide by $`\eta`$, and multiply the value and difference bounds by $`m,m^2`$.
Use $`\eta\le m`$. This gives (5.4). $`\square`$

**Lemma 5.3.** Under Theorem PI's hypotheses, all $`M_{r,\tau}(U)`$ are invertible and

```math
\|M_{r,\tau}(U)^{-1}\|_{\mathcal Y_\tau\to\mathcal X_\tau}\le3B_F.
```

Their entries are holomorphic in $`\mathfrak a`$, and read only $`U|_{X_\tau}`$ and the model geometry, which is fixed by the tower on $`N_\tau`$.

*Proof.* Let $`\mathcal U`$ act by the chosen unitary gauge on every component at its initial point or site.
Balaban's finite differential and Hessian formulas are covariant, CMP 99b pp. 394–395, (3.28)–(3.32).
Lemma 4.4 gives the row covariance.
Thus $`M_{r,\tau}(U^u)=\mathcal U M_{r,\tau}(U)\mathcal U^{-1}`$.
The gauge is an isometry between the corresponding real-background norms.
Lemma 5.2 and §3.3 give $`e(B)\le e_L`$.
The flat inverse lemma and Lemma 5.1 give

```math
\|M_{r,\tau}(1)^{-1}\|\le B_F,\qquad
\|M_{r,\tau}(e^{i\eta B})-M_{r,\tau}(1)\|\le1/(8B_F).
```

The Neumann series gives flat inverse norm at most $`(8/7)B_F`$.
Both norm conversions cost at most $`9/8`$, so the bound is at most
$`(9/8)^2(8/7)B_F=(81/56)B_F<3B_F`$.
Conjugate back.
The coefficients themselves define the inverse, independently of the gauge used to estimate it.
They are holomorphic and the determinant never vanishes; Cramer's rule proves holomorphy throughout the stated ball. $`\square`$

## 6. Assembly and walk terms

Fix $`r\in\{1,3,4,5\}`$ and suppress it in this section.
Transplant fields supported in $`A_\tau`$ between the model and global spaces.
Agreement gives equality of their norms there.
This is Balaban's partition-of-unity method, CMP 96 pp. 247–248, (2.141), and CMP 99b pp. 409–416, (3.87)–(3.108), applied to the local mixed system.

**Lemma 6.1.** The commutator $`[M_\tau(U),h_\tau]Y`$ is supported in $`A_\tau`$ and reads only the complete read closure of $`\operatorname{supp}h_\tau`$.
It equals $`[M(U),h_\tau]\widetilde Y`$ when $`\widetilde Y`$ agrees with $`Y`$ on $`A_\tau`$, and

```math
\|[M_\tau(U),h_\tau]Y\|_{\mathcal Y_\tau}\le(C_K/M_t)\|Y\|_{\mathcal X_\tau}.
```

*Proof.* The support and read statements follow by subtracting $`M_\tau(h_\tau Y)-h_\tau M_\tau Y`$ and using Agreement.
Conjugate by the gauge of Lemma 5.3.
The scalar cutoff commutes with that gauge.
Write the commutator as its flat part plus $`[V,h]`$, where $`V=M_\tau(e^{i\eta B})-M_\tau(1)`$.
Appendix A bounds the flat part by $`C_{\rm com}/M_t`$.
Lemma 5.1 gives

```math
\|[V,h]Y\|\le2c_hC_Ce_L\|Y\|\le(C_{\rm com}/M_t)\|Y\|.
```

The norm conversions cost $`(9/8)^2`$, and $`2(9/8)^2<3`$.
This proves the assertion with $`C_K=3C_{\rm com}`$. $`\square`$

**Lemma 6.2.** Define the transplanted operators

```math
S_\tau=h_\tau M_\tau^{-1}h_\tau,\qquad
T_\tau=[M_\tau,h_\tau]M_\tau^{-1}h_\tau,\qquad
\mathrm{Par}=\sum_\tau S_\tau,\quad\mathrm{Res}=\sum_\tau T_\tau.
```

Then

```math
M\,\mathrm{Par}=I+\mathrm{Res},\quad
\|S_\tau\|\le3B_Fc_h^2,\quad\|T_\tau\|\le\theta,\quad
\|\mathrm{Res}\|\le D_*\theta\le1/2.
```

Consequently $`M^{-1}=\mathrm{Par}\sum_{n\ge0}(-\mathrm{Res})^n`$, in operator norm.

*Proof.* For $`Z=M_\tau^{-1}h_\tau F`$, Agreement gives

```math
M(h_\tau Z)=h_\tau^2F+[M_\tau,h_\tau]Z.
```

Sum and use $`\sum h_\tau^2=1`$.
Cutoff multiplication and Lemma 5.3 bound $`S_\tau`$.
For $`T_\tau`$, pair with a test field and insert a smooth cutoff $`\chi_\tau`$, equal to one on the commutator read and supported in $`A_\tau`$.
It has the same multiplier bound $`c_h`$.
Lemmas 6.1 and 5.3 give the bound defining $`\theta`$.
For the sum, bounded overlap gives

```math
\sum_\tau\|\chi_\tau Y'\|^2\le c_h^2D_*\|Y'\|^2,\qquad
\sum_\tau\|h_\tau F\|^2\le c_h^2D_*\|F\|^2.
```

For dual sources, the second assertion follows by transposing smooth synthesis.
Explicitly choose $`Z_\tau`$ with norm $`t_\tau=\|h_\tau F\|`$ and pairing $`\langle F,h_\tau Z_\tau\rangle=t_\tau^2`$.
Then

```math
\sum t_\tau^2=\left\langle F,\sum h_\tau Z_\tau\right\rangle
\le\|F\|c_hD_*^{1/2}(\sum t_\tau^2)^{1/2}.
```

Cauchy–Schwarz in $`\tau`$ now gives $`\|\mathrm{Res}\|\le D_*\theta`$.
No sharp characteristic multiplier on $`H^2`$ is used.
The Neumann series gives a right inverse of a finite square matrix, hence its inverse. $`\square`$

**Lemma 6.3.** For a tile sequence $`\omega=(\tau_0,\ldots,\tau_n)`$, put

```math
W_\omega=S_{\tau_0}(-T_{\tau_1})\cdots(-T_{\tau_n}).
```

The sum of these terms is $`M^{-1}`$.
A term vanishes unless consecutive cutoff supports and read closures meet; in particular it vanishes unless $`\omega`$ is a walk.
Moreover

```math
\|W_\omega\|_{\mathcal Y\to\mathcal X}\le3B_Fc_h^2\theta^n.
```

Its output is supported in $`\operatorname{supp}h_{\tau_0}`$, and its source read is in $`\operatorname{supp}h_{\tau_n}`$.
It is holomorphic and reads only $`U|_{X(\omega)}`$, its model geometries and its cutoffs.

*Proof.* Expand the finite sums in $`\mathrm{Par}(-\mathrm{Res})^n`$.
The cutoff at the right of each preceding factor must meet the next commutator output.
These sets lie in the corresponding $`N`$-boxes, giving the walk condition.
Multiply the individual norm bounds for the estimate.
The endpoint cutoffs give the support statement.
Each local inverse and each coefficient in a commutator has the stated read and holomorphy by Lemma 5.3. $`\square`$

The systems $`r=4`$ and $`r=3`$ also give local expansions for the vector inverse and scalar projection in their energy norms.
These do not give the pointwise or Hölder vector estimates of CMP 99b pp. 397–399, (3.42)–(3.47).

## 7. Schur complements and identification

**Lemma 7.1.** If $`A_s,M_3,M_4,M_5`$ are invertible and $`G'=A_s^{-1}`$, then

```math
\begin{gathered}
Q'G'^2Q'^T\text{ is invertible},\qquad [M_3^{-1}]_{hh}=P,\\
T:=B_v-D_UPD_U^T=\Delta_a\text{ is invertible},\qquad T^{-1}=[M_4^{-1}]_{AA},\\
\Gamma:=KT^{-1}K^T\text{ is invertible},\qquad\Gamma^{-1}=-[M_5^{-1}]_{\nu\nu},\\
QG_0Q^T=m^{-1}\Gamma m^3,\qquad q_0=-m^{-3}[M_5^{-1}]_{\nu\nu}m.
\end{gathered}
```

*Proof.* For a block matrix with invertible lower-right block $`W`$, factor

```math
\begin{pmatrix}X_{11}&X_{12}\\X_{21}&W\end{pmatrix}
=\begin{pmatrix}I&X_{12}W^{-1}\\0&I\end{pmatrix}
\begin{pmatrix}X_{11}-X_{12}W^{-1}X_{21}&0\\0&W\end{pmatrix}
\begin{pmatrix}I&0\\W^{-1}X_{21}&I\end{pmatrix}.
```

This proves the Schur criterion and its inverse-block formula.
For $`M_3`$, a source $`(g,0,0)`$ gives
$`h+A_s\lambda=g`$, $`A_sh-Q'^T\mu=0`$, $`Q'\lambda=0`$.
If $`Q'G'^2Q'^T\mu_0=0`$ with $`\mu_0\ne0`$, then
$`(G'Q'^T\mu_0,-G'^2Q'^T\mu_0,\mu_0)`$ is a nonzero null vector of $`M_3`$.
Thus the Gram matrix is invertible.
Solving gives $`\mu=(Q'G'^2Q'^T)^{-1}Q'G'g`$ and $`h=Pg`$.
The Schur complement of $`M_3`$ in $`M_4`$ is $`B_v-D_UPD_U^T`$.
The Schur complement of $`M_4`$ in $`M_5`$, with the last variable first, is $`-KT^{-1}K^T`$.
Finally $`K=mQ`$ and $`K^T=Q^Tm^{-3}`$ give the two conversions. $`\square`$

*Proof of PI(a).* Every global coefficient belongs to the agreement region of a tile whose cutoff covers its reference point.
Its row or stencil is therefore defined by Lemmas 4.4 and 5.2.
Lemma 6.2 gives all four mixed inverses; Lemma 7.1 gives the remaining inverses and formulas.
Holomorphy follows from Cramer's rule, or from the uniformly convergent expansion.
Bilinear symmetry of $`\Delta(U),D_URD_U^T,Q^TaQ`$ gives $`q_0^T=q_0`$.

At real data every coefficient is Balaban's coefficient by its defining finite formula: CMP 99b (3.8), (3.10), (3.13)–(3.19), using CMP 98 (42)–(43), (58)–(63), (89)–(92).
The site mass does not change $`R`$, as observed in §3.1.
Thus the Schur complement is the bare operator of CMP 99b pp. 394–395, (3.26)–(3.27), with $`a=\ell^{-2}`$.
At complex data these same formulas give the extension stated on CMP 99b p. 393.
They are holomorphic on the whole fixed twist ball, with (S2+) included.
Any holomorphic continuation from its real slice agrees there by the identity theorem, which is the continuation used at CA-I 13552–13571.
No identification of different curved averaging rules is involved. $`\square`$

## 8. Density, decay and spare factors

For levels $`j,j'`$, the row density of the walk term is

```math
q_\omega(c,c')=-\ell_j^{-3}\ell_{j'}^{-3}(W_\omega^{(5)})_{\nu\nu}(c,c'). \tag{8.1}
```

Indeed $`m^{-3}\Gamma^{-1}m`$ has counting entry $`\ell_j^{-3}\Gamma^{-1}(c,c')\ell_{j'}`$.
Divide by the source-cell measure $`\ell_{j'}^4`$ to get (8.1).

**Scale-distance estimate.** If $`|j-j'|\ge1`$, then

```math
d(y,y')\ge RM_b(|j-j'|-1). \tag{8.2}
```

Suppose $`j'\ge j+2`$.
For each $`j<n<j'`$, a contour leaves $`\Omega_n^c`$ for the last time before it reaches $`\Omega_{n+1}`$.
The intervening segment is in $`\Omega_n\setminus\Omega_{n+1}`$, has length greater than $`RM_b\ell_n`$, and costs more than $`RM_b`$.
These segments are disjoint.
The exterior convention also covers endpoints outside $`\Omega_0`$.
This proves (8.2).

For a nonzero term, choose intermediate tops in consecutive footprint intersections.
The diameter bound in §5.2 gives

```math
d(y_c,y_{c'})\le d(\omega,y_c,y_{c'})\le D_X(n+1).
```

Equations $`E`$, (8.1), and Lemma 6.3 bound its absolute value by
$`3B_Fc_h^2\ell_j^{-3}\ell_{j'}^{-3}\theta^n`$.
Write the scale factor as $`\ell_j^{-2}\ell_{j'}^{-4}(\ell_{j'}/\ell_j)`$.
By (8.2) and the floor on $`RM_b`$,

```math
\ell_{j'}/\ell_j\le L\exp\!\left(\frac{\log L}{RM_b}d(y_c,y_{c'})\right)
\le L e^{(\delta_q/3)D_X(n+1)}.
```

Also

```math
\theta^n=\theta^{-1/2}\theta^{n/2}\theta^{(n+1)/2},\qquad
\theta^{(n+1)/2}=e^{-(7/2)\delta_qD_X(n+1)}.
```

Consequently

```math
|q_\omega(c,c')|\le3B_Fc_h^2L\theta^{-1/2}
\ell_j^{-2}\ell_{j'}^{-4}\theta^{n/2}e^{-3\delta_qD_X(n+1)}. \tag{8.3}
```

The coefficient is at most $`C_q`$, proving PI(c), with locality and holomorphy from Lemma 6.3.
This reproduces the scale and spatial-decay form used by Balaban in CMP 99b p. 422, (3.132), for the bare operator here.

At most $`D_*^n`$ walks of length $`n`$ start at a fixed tile.
Since $`D_*\theta^{1/4}\le1/4`$, their summation factor sums to at most $`\sum_{n\ge0}4^{-n}=4/3`$.
The same count holds backwards.
The other fourth-power factor is at most $`(4D_*)^{-n}`$.
The distance bound and $`\Lambda\le D_X(n+1)`$ give PI(d)'s exponential split.
This provides reserves of the kind in Balaban's CMP 99b p. 413, (3.98)–(3.99), and p. 416, (3.108), at our fixed tile size.

At most $`D_*`$ possible first tiles cover $`y_c`$.
In (8.3) replace $`e^{-3\delta_qD_X(n+1)}`$ by $`e^{-3\delta_qd(y_c,y_{c'})}`$ and sum.
The coefficient is
$`D_*(4/3)3B_Fc_h^2L\theta^{-1/2}=C_q`$.
Weaken the rate from $`3\delta_q`$ to $`\delta_q`$ to obtain PI(b).
The convergence is absolute and uniform on the twist ball.
For a source at one base point, at most eight field rows contribute.
Multiplication by their cell measure cancels $`\ell_{j'}^{-4}`$, giving the stated $`8C_q`$ bound.
Thus $`q_0\in\mathcal K_{-2}`$, in your CA-I 13402–13410 notation, with constant $`8C_q`$, once your additional shell floors are imposed. $`\square`$

## 9. Equality between settings

Fix the grids, profile $`\phi`$, rule for the model cubes, and order for selecting exterior anchors once.
A walk's footprint is the union of its full cubes $`F_\tau`$, including portions where its coefficients read no background.
Consecutive cubes have a positive-volume overlap.
The footprint is therefore the closure of its connected interior, as required at CA-I 5126–5130.

*Proof of PI(e).* Suppose two settings agree on a walk's footprint.
First, whether $`\tau`$ is a level-$`j`$ tile is determined by the tower on $`\tau`$.
Exterior membership and the choice of $`z_\tau`$ read only the tile and its one-bond neighbourhood.
All these data lie in $`F_\tau`$.
The walk condition itself is geometric.
Thus the same tile sequence is a walk in the second setting.

Second, on $`\operatorname{supp}b_\tau`$, only tiles whose bumps meet $`b_\tau`$ contribute to the denominator of $`h_\tau`$.
Their heights differ by at most one, and their centres are within
$`(L+1)M_t\ell_{j_\tau}`$ of $`x_\tau`$.
Each whole neighbouring tile lies within half-width
$`(L+1+L/2)M_t\ell_{j_\tau}<\widehat r\ell_{j_\tau}`$.
Its one-bond exterior-membership test also lies inside the remaining margin.
Thus both settings choose the same contributing bumps and the same denominator.

Third, $`i_\tau`$ is determined on $`N_\tau\subset F_\tau`$.
The cubes $`C_\tau,K_n`$ then follow from fixed rules, and $`\Omega_n^\tau=\Omega_n\cap K_n`$ is the same in both settings.
All model coefficients read the common background domain in $`X_\tau\subset F_\tau`$.
Their inverses therefore agree.

Fourth, the global components in $`A_\tau`$, their transplants, and the coefficients near $`\operatorname{supp}h_\tau`$ are fixed by these same data.
Hence the kernels $`S_\tau,T_\tau`$, and then $`W_\omega,q_\omega`$, agree.
Apply the argument in both directions to a closed $`W`$ to get the same restricted index set and sum.
Finally, $`\operatorname{supp}h_\tau`$ has half-width $`M_t\ell_{j_\tau}`$, while $`F_\tau`$ has half-width $`(2L+2)M_t\ell_{j_\tau}`$.
Their difference is the base-point margin in PI(e).
Including an entire row bond reduces it by the bond length. $`\square`$

This proves the same-grid locality, support and convergence clauses for the $`q_0`$ entry in your ordered-word construction, CA-I 5293–5470.
Your C1 clause also requires termwise covariance under lattice transformations, CA-I 5664–5669 and 5725.
The fixed-grid comparison above does not prove that property.
Identification with your full covariant one-family hypothesis remains an input.

## 10. Proofs of the three propositions

*Proposition 3.1.* Fix $`x`$ with $`N=N(x)\subset\Omega_0`$, and put $`j=\lambda(x)`$.
Every point of $`N`$ is within Euclidean distance $`2r_N\ell_j`$ of $`x`$.
The gap inequalities exclude levels at most $`j-2`$ and at least $`j+2`$.
They also prevent $`N`$ from meeting both $`j-1`$ and $`j+1`$.
Thus its levels lie in $`\{i,i+1\}`$, for some $`i\in\{j-1,j\}`$, where $`i`$ is the least level met.

Now $`N\subset\Omega_i`$ and its side is at most $`2r_NL\ell_i<11M_b\ell_i<s_i`$.
It meets at most two $`s_i`$-cells per coordinate.
Every such cell lies in $`\Omega_i`$, so their product box contains $`N`$ and lies in $`\Omega_i`$.
Round each left endpoint of the projection of $`N`$ down to the $`M_b\ell_i`$ grid, and take an interval of length $`12M_b\ell_i`$.
The rounding costs less than $`M_b\ell_i`$, while the projection length is at most $`(11M_b-1)\ell_i`$.
If that interval passes the cell box's right endpoint, use the aligned interval ending there.
It still contains the projection and lies in the cell box.
Their product $`Q`$ therefore satisfies $`N\subset Q\subset\Omega_i`$.

The cube $`Q`$ contains a level-$`i`$ point outside $`\Omega_{i+1}`$.
Its distance from $`\Omega_{i+2}`$ is greater than $`RM_b\ell_{i+1}\ge24M_b\ell_i`$, the Euclidean diameter of $`Q`$.
Thus $`Q\cap\Omega_{i+2}=\varnothing`$, and $`Q\in\mathcal C_i`$.
Apply (S1), Balaban's CMP 99b p. 396, (3.35), on $`Q`$.
At a point $`z\in N`$, $`\ell_{\lambda(z)}\le L\ell_i`$; the value and derivative losses are at most $`L,L^2`$.
This is (S1-loc). $`\square`$

*Proposition 3.2.* Choose a bond $`b_0`$ in the middle cross-section whose six plaquettes lie in $`F`$.
Let $`p`$ be any endpoint of a bond in these plaquettes.
It is within $`2\eta`$ of that cross-section.
If a tested level-zero cube of side $`s\ge10M_b\eta`$ contained $`p`$, its transverse line through $`p`$ would contain a segment of length
$`\min\{s,30M_b\eta\}\ge10M_b\eta`$, containing $`p`$ and lying within $`30M_b\eta`$ of it.
This segment lies in $`\Omega_0`$ within $`31M_b\eta`$ of the cross-section, hence in $`F`$.
But the transverse run of $`F`$ is shorter than $`wM_b\eta\le9M_b\eta`$.
This is impossible.
Higher tested cubes lie in $`\Omega_1`$, far from these bonds.

Set $`U_t(b_0)=e^{i\pi t\sigma_3}`$, $`0\le t\le1`$, and set every other positive link to 1, with reversed links their inverses.
Take $`U_r=U_t`$ and $`\mathfrak a=0`$.
Every tested cube sees the identity, so (S1), (S2), (S2+) hold.
Higher field and site rows read only the unchanged region near $`\Omega_1`$; level-zero rows are identities.
For each $`t`$,

```math
\langle\lambda,A_s(U_t)\lambda\rangle
=\|D_{U_t}\lambda\|_2^2+\|m^{-1}Q'\lambda\|_{\rm top}^2.
```

A null vector vanishes on level-zero sites and propagates as zero along bonds, with the zero extension, on every component.
Thus $`A_s(U_t)>0`$.
The disjoint site blocks and invertible transports make $`Q'`$ onto.
Hence $`Q'G'^2Q'^T>0`$, and $`R(U_t)`$ is a continuous orthogonal projection.
At $`t=0`$, the flat inverse lemma gives $`\Delta_a(1)>0`$ on a box with the room of the flat inverse lemma.

At $`t=1`$, take $`A=\alpha\sigma_3`$ on $`b_0`$, zero elsewhere, so $`\|A\|_2^2=\eta^4\alpha^2`$.
Each of its six plaquettes has holonomy $`-I`$.
The exact plaquette formula in Lemma 5.1 gives $`-\eta^{-2}\|A\|_2^2`$ per plaquette; there is no commutator term for this one-bond field.
Also

```math
\langle A,D_URD_U^TA\rangle\le\|D_U^TA\|_2^2=2\eta^{-2}\|A\|_2^2,\qquad
\langle A,Q^TaQA\rangle=\eta^{-2}\|A\|_2^2.
```

No higher row reads $`b_0`$.
Therefore $`\langle A,\Delta_a(U_1)A\rangle\le-3\eta^{-2}\|A\|_2^2<0`$.
The least eigenvalue of the real symmetric finite matrix is continuous.
Define $`t_*=\min\{t:\lambda_{\min}(\Delta_a(U_t))\le0\}`$.
It vanishes there, giving the asserted singular field without computing $`t_*`$.
Finally $`U'=U_1`$ has $`|\partial U'-1|=2`$ on the six plaquettes, whereas your level-zero bound is $`4(a_0+a_1)<2`$. $`\square`$

*Proposition 3.3.* The periodic lattice is connected and $`\varnothing\ne\Omega_0\ne T_\eta`$.
Choose a crossing bond $`b_0`$ with one endpoint $`x_0\in\Omega_0`$ and the other outside.
The first gap makes it a level-zero row and excludes all higher-row carriers.
No tested cube contains this bond, since its bonds must have both endpoints inside $`\Omega_0`$.
Use the same path $`U_t`$ and zero twist.
The preceding positivity and continuity argument for the scalar operators still applies.
At $`t=1`$, all six whole-action plaquettes through $`b_0`$ have holonomy $`-I`$.
Only the interior endpoint contributes to the compressed divergence, so

```math
\|D_U^TA\|_2^2=\eta^{-2}\|A\|_2^2,\qquad
\langle A,\Delta_a(U_1)A\rangle\le(-6+1+1)\eta^{-2}\|A\|_2^2<0.
```

The same first-crossing construction gives singularity.
By the box hypothesis, $`T_\eta`$ has side at least $`(2\widehat r+2)\ell_k`$. Then by Theorem PI, (S1-loc) with $`a_0\le a_0^*`$ must fail at a site whose box contains that bond.
The twist is zero throughout, including on the exterior read.
This proves failure of boundary real-gauge control from S1–S2; it does not refute an assertion about the exterior twist alone. $`\square`$

## 11. Uses in your account and limits

Every supplied entry below uses the literal rows, the compressed whole-action Hessian, (S1-loc), (S2), and (S2+).
For a nonempty proper outer region, boundary real-gauge control remains a premise.
Use a common decay rate no greater than $`\min\{\delta_0,\delta_q\}`$, with any further reduction stated below.
Choose later shell floors, current ceilings and decoupling sizes at that rate.
These entries supply inverse inputs, not whole consumer theorems.

| Your source and lines | What this note supplies |
|---|---|
| CA-I 13142–13173 | The bare inverse bound and local walk expansion under the stronger local hypotheses. The unrestricted S1–S2 remark is not supplied; Propositions 3.2 and 3.3 show the failures on the stated reading. |
| CA-I 13589, 13624–13627 | $`q_0\in\mathcal K_{-2}`$ and an actual complex walk expansion. Impose all the floors at 13413–13428. |
| CA-I 13640–13665 | The inverse, transpose, constraint and projection algebra for $`H_0,P_0,\widetilde{\mathfrak G}_0`$. |
| CA-I 13675 | Only the $`q_0`$ input. The pointwise and Hölder bounds for $`G_0`$ and the resulting lift bounds remain inputs. |
| CA-I 13683; 19583–19600 | The specified $`q_0`$ inverse input on this local domain. Every other hypothesis remains. |
| CA-I 13766, 13899–13909, J3 | The order-$`-2`$ inverse factor in the current perturbation series. The kernel algebra and current ceiling still have to be applied at the common rate. |
| CA-I 13787–13798, 13966–13979, J8 | The $`q_0`$ walk family, its holomorphy, locality, absolute majorant and reserves. The other primitive families and differentiated vector bounds remain inputs. |
| CA-I 13915–13923, J4 | The $`q_0`$ factor. The separate $`H_0`$ bound remains an input. |
| CA-I 14377–14476 | The inverse factors and representation algebra. Chart existence and fixed-point estimates remain inputs. |
| CA-I 14655 | Holomorphy on the whole PI twist ball, including its exterior restriction. The consumer radius must place its domain inside that ball. |
| CA-I 14715–14774, K3 | The inverse contribution to $`\Vert Q^T(q_0-a)\widetilde B\Vert _{(-3)}\le C\Vert \widetilde B\Vert _{(-1)}`$, using Lemma 4.4's physical column bound and your weighted kernel algebra. This does not prove the rest of K3. |
| CA-I 14831 | The inverse factor in the first variation at weight rate $`\kappa\le\delta_q/2`$, after the common-rate and shell choices. |
| CA-I 15266–15490, K10 | The $`q_0`$ contribution with full footprints, the decoupling-size floor below, and anchored-tree reserve rate at most $`\delta_q/17`$. The other operators and nonlinear equations remain inputs. |
| CA-I 15770–15796 | $`P_0^T\Delta_a=\Delta_a-Q^Tq_0Q`$. Real minimizer identification, chart uniqueness and continuation in the datum remain separate. |
| CA-I 19744–19750 | Only the inverse inputs listed here. This does not prove J2–J8 or K10 in full. |
| CA-I 5293–5470, 5702–5725 | Same-grid locality, support and convergence for the $`q_0`$ entry. The full one-family hypothesis, including termwise lattice covariance C1 on its domains, remains an input. |
| CA-I 13323 | A dependency attribution only. This note does not construct the near-bound frame. |
| CA-II 54464–54635 | The bare $`C_Q=q_0`$ bound under PI's hypotheses, with $`8\delta_1\le\delta_q`$ and the other common-rate restrictions. No bound for the other listed operators is supplied. |
| CA-II 60313 | The bare bound of the form (3.132). The lift estimate (3.133) still needs the pointwise vector bounds. |
| CA-III 36352–36370 | Not supplied. This uses the current-corrected $`G_1`$ inverse and requires its own perturbation argument and hypotheses. |
| CA-I 166593–166594; CA-III 111329 | These are status lists. This research note changes no status. |

**The K10 geometry.** Follow Balaban's decoupling rule in CMP 116 pp. 1–22, (1.6)–(1.11), as quoted in your CA-I 15266–15490.
Assign the full $`F_\tau`$'s as localization domains.
Require each decoupling cube side to exceed the corresponding footprint side $`2\widehat r\ell`$.
A footprint then meets at most $`2^4`$ decoupling cubes.
Choose a representative in each intersection and join them with the consecutive-footprint joining points and endpoint anchors.
This requires at most $`17(n+1)`$ links of bounded layer length.
If a thin intersection has no top, choose a top in its decoupling cube within $`\ell_{i+1}`$ of it.
It lies in $`F_\tau^+`$.
The staircase construction of §5.2 extends to these endpoints with bound

```math
16L(L+1)M_t+8L^2+12L\le24L^2M_t=D_X
\qquad(L\ge3, M_t\ge4L).
```

The gap floor keeps the larger staircase box within two heights.
The anchored tree therefore has length at most $`17D_X(n+1)`$.
Apply PI(d) with $`\Lambda`$ equal to this length divided by 17.
Each of the two spare exponentials has rate $`\delta_q/17`$; choose subsequent constants at that rate.
A word surviving zero switches has its full connected footprint in the retained union, so it cannot join distinct components.
At switch value one its original sum is recovered.
This proves the inverse contribution only.

**Not proved.** The S1–S2 remark on arbitrary towers; the current-corrected $`G_1`$ inverse; the pointwise and Hölder bounds for $`G_0`$; a boundary gauge-gluing lemma; and termwise lattice covariance $`C1`$ remain outside this result.
The note also supplies neither a radius independent of tile size nor the other analytic averaging-derivative assertions of CMP 98 §E.
The two counterexamples retain their class and boundary conventions.
They assert nothing against Balaban's own tower class or his Theorem 3.3.

## Appendix A. Proof of the flat inverse lemma

We give the flat argument in full at the energy and mixed-system level used above.
We do not need flat pointwise or Hölder estimates.
Balaban's sources for this method are CMP 95 (1984), pp. 17–40, Proposition 1.1, (1.89)–(1.90); CMP 96 (1984), pp. 223–250, (2.17), (2.95)–(2.141), Propositions 2.5–2.6; and CMP 99b pp. 394–399, (3.25)–(3.27) and Theorems 3.1–3.3.
The proof below makes no appeal to those inverse bounds.
Write $`D`$ for the scalar gradient, $`C`$ for the field curl, and $`\Delta_s=D^TD`$.
At real flat data the bilinear transposes have the usual real Hilbert-space interpretation.
All estimates apply componentwise to the colour variables.

### A.1 Rows, scalar control and the scalar Gram matrix

For a row of length $`s=n\eta`$, the physical straight average is

```math
Q_cA=n^{-5}\sum_{v\in B(c_-)}\sum_{t=0}^{n-1}A_\mu(v+t\eta e_\mu),\qquad K_c=sQ_c.
\tag{A.1}
```

This is the flat value of Balaban's CMP 98 p. 36, (124)–(125), composed through the levels.
Each starting site decomposes uniquely into successive block offsets, and its straight segments concatenate.
Thus (A.1) holds at every height, as also proved in Lemma 4.4(iii).
The row sum of $`K`$ is $`s`$.
At a fixed fine bond the possible starts of the translated segments partition the $`n`$ longitudinal offsets.
The transverse block is unique.
Hence, at one height,

```math
\sum_c|K(c,b)|=\eta n^{-3}=\eta^4s^{-3}.
```

Deleting rows decreases the sum.
Every contributing row scale satisfies $`s\ge m(b)`$: an inward row is absent, and its two endpoint blocks outside the next region cannot read a bond endpoint assigned a larger pillar.
Therefore

```math
\sum_c s_c|K(c,b)|\le\frac{\eta^4m(b)^{-2}}{1-L^{-2}},\qquad
\|KA\|_{\rm count}^2\le\frac{\|m^{-1}A\|_2^2}{1-L^{-2}}. \tag{A.2}
```

The last step is Jensen followed by summing columns.
This calculation includes the physical fine measure.

A straight average of a gradient telescopes to the difference of endpoint block means divided by $`s`$.
At an outward row, the outer block is a union of complete finer pillars.
At a bare row both endpoints are bare sites.
It follows that

```math
QD\lambda=0\quad\text{whenever }Q'\lambda=0. \tag{A.3}
```

This is the no-inward identity underlying Balaban's gauge change in CMP 96 (2.28)–(2.34).
No omitted inward mass is reinserted in this proof.

On a pillar of side $`s`$,

```math
\|u-\operatorname{Av}u\|_2\le Cs\|Du\|_2.
\tag{A.4}
```

For completeness, in one coordinate write
$`\sum_x|u_x-\bar u|^2=(2n)^{-1}\sum_{x,y}|u_x-u_y|^2`$.
Telescope each difference along the interval, then apply Cauchy–Schwarz to at most $`n`$ differences.
Each edge occurs in at most $`n^2`$ ordered endpoint pairs.
This gives a constant times $`n^2`$ times the squared unscaled difference norm.
Iterate the conditional mean in the four coordinates and use the triangle inequality.
Restoring the mesh gives (A.4).
Summing pillars yields the scalar energy bound with the actual means.
On a periodic one- or two-scale model normalized to have $`1\le m\le L`$, it gives a uniform gap for
$`A_s=\Delta_s+Q'^Tm^{-2}Q'`$.
The mass term is bounded on $`L^2`$, so the equation $`\Delta_sS f=f-Q'^Tm^{-2}Q'Sf`$, $`S=A_s^{-1}`$, and the Fourier identity

```math
\sum_{\alpha,\beta}\|D_\alpha D_\beta u\|_2^2=\|\Delta_su\|_2^2
```

give $`S:L^2\to H^2`$, uniformly in fine mesh and periodic volume.
Transposition gives $`S:H^{-2}\to L^2`$.

We also need a lower bound for $`J_s=Q'S^2Q'^T`$, not just its invertibility.
In each non-bare pillar choose a sampled smooth bump supported in the middle half, normalized to mean one.
Its first two differences are bounded by $`Cs^{-1},Cs^{-2}`$, by integrating ordinary derivatives over mesh intervals.
For at least 33 sites per side, a fixed interior subcube gives a positive lower bound on the sampled mean.
For smaller pillars use the central point field times the number of sites.
Their side-to-mesh ratio is below 33, so the same estimates hold with a larger absolute constant because each second-difference stencil has at most four entries.
For a bare pillar use the point field.
Pillars and the one-step enlargements of these bumps have bounded overlap.
Their sum $`F_b`$, with coefficients $`b_y`$, satisfies

```math
Q'F_b=b,\qquad \|A_sF_b\|_2\le C\Big(\sum_y|b_y|^2\Big)^{1/2}. \tag{A.5}
```

Pair $`SQ'^T\chi`$ with $`A_sF_b`$ and take the supremum over counting-unit vectors $`b`$.
The top pairing has weight $`m_y^4`$, so

```math
\langle\chi,J_s\chi\rangle_{\rm top}
=\|SQ'^T\chi\|_2^2\ge c\sum_y m_y^8|\chi_y|^2. \tag{A.6}
```

The scalar inverse and row bounds give the matching upper bound on a normalized one- or two-scale model.
Thus $`N=J_s^{-1}`$ has the uniform bound in the weighted top spaces needed by the scalar saddle system.
This is the smooth-lift duality argument behind Balaban's scalar inverse construction, CMP 96 (2.17) and CMP 99b pp. 398–399, (3.48)–(3.49).

### A.2 Uniform one-scale vector form

This rebuilds the energy argument of Balaban, CMP 95 p. 33, Proposition 1.1, (1.89)–(1.90).
Normalize the row scale to one and put $`h=1/n`$, $`n=L^j`$.
The Bloch transform on the coarse periodic lattice has momenta $`\vartheta\in[-\pi,\pi]^4`$ and fine aliases $`p_\ell=\vartheta+2\pi\ell`$ in the fine Brillouin zone.
Set

```math
d_\mu(p)=\frac{e^{ihp_\mu}-1}{h},\quad
\omega(p)=\sum_\mu|d_\mu(p)|^2,\quad d_{c,\mu}=e^{i\vartheta_\mu}-1,\quad
q_\ell=n^{-4}\sum_{x\in B}e^{ip_\ell\cdot x}.
```

Summing the path in (A.1) gives the vector coefficients

```math
q_{\mu,\ell}=q_\ell\frac{d_{c,\mu}}{d_\mu(p_\ell)}, \tag{A.7}
```

with the finite geometric sum at a removable zero.
Parseval for the normalized block indicator, the sine quotient in each coordinate, and $`1-\cos t\le t^2/2`$ give

```math
\sum_\ell|q_\ell|^2=1,\quad |q_0|\ge(2/\pi)^4,\quad
\sum_{\ell\ne0}|q_\ell|^2\le C|\vartheta|^2,\quad \|Q\|_{2\to2}\le1. \tag{A.8}
```

For the last inequality use Jensen and the complementary longitudinal tents in the column count, with physical cell volumes.
Also $`c|p|^2\le\omega(p)\le|p|^2`$ on the fine Brillouin zone, and $`\omega(p_\ell)\ge c`$ for $`\ell\ne0`$.

For $`\vartheta\ne0`$, put $`v_\ell=\bar q_\ell/\omega(p_\ell)`$, $`B=\sum|v_\ell|^2`$, and $`g_\ell=d(p_\ell)v_\ell`$.
The scalar projection $`P`$ is the rank-one projection onto $`v`$: solving $`(\Delta_s+aQ'^TQ')SQ'^T=Q'^T`$ leaves its range equal to that of $`\Delta_s^{-1}Q'^T`$.
Let $`W`$ be multiplication by $`\omega(p_\ell)`$ on vector components.
The vector form is

```math
E(A)=\|W^{1/2}A\|^2-\frac{|\langle g,A\rangle|^2}{B}+a\|QA\|^2. \tag{A.9}
```

Here the dimensionless $`a>0`$ is fixed; the theorem uses $`a=1`$.
The first two terms are nonnegative since $`\|W^{-1/2}g\|^2=B`$.
Their null direction is $`z_\ell=d(p_\ell)\bar q_\ell/\omega(p_\ell)^2`$, with

```math
\|W^{1/2}z\|^2=B,\qquad Qz=d_cB,\qquad |d_c|^2B\ge c>0. \tag{A.10}
```

The lower bound uses the zero-alias term, (A.8), $`\omega(p_0)\le|\vartheta|^2`$, and $`|d_c|^2\ge(4/\pi^2)|\vartheta|^2`$, with $`|\vartheta|\le2\pi`$.

If $`|\vartheta|\ge t_0>0`$, split $`A=\alpha z+A_\perp`$ orthogonally in the $`W`$-inner product.
The first two terms of (A.9) equal $`\|W^{1/2}A_\perp\|^2`$.
Since $`W\ge ct_0^2`$, $`\|QA_\perp\|\le C_{t_0}\|W^{1/2}A_\perp\|`$.
Use $`\alpha Qz=QA-QA_\perp`$ and (A.10) to bound $`|\alpha|\sqrt B`$ by $`C_{t_0}E(A)^{1/2}`$.
This controls $`\|A\|^2+\|W^{1/2}A\|^2`$.

For $`0<|\vartheta|<t_0`$, split $`A=A_0+A_h`$ into the low alias and the others.
The high part of $`W^{-1/2}g/\sqrt B`$ has squared norm at most $`C|\vartheta|^6`$.
Its numerator is at most $`C|\vartheta|^2`$, while $`B\ge c|\vartheta|^{-4}`$.
Expand the rank-one square and use $`2ab\le a^2/4+4b^2`$.
After reducing $`t_0`$,

```math
E(A)\ge\tfrac12\|W^{1/2}A_h\|^2-C|\vartheta|^8|A_0|^2+a\|QA\|^2.
```

The low-alias coefficients $`q_{\mu,0}`$ are bounded away from zero by (A.7)–(A.8), so
$`|A_0|^2\le C(\|QA\|^2+\|A_h\|^2)`$.
Choose $`t_0`$ smaller to absorb the negative term.
At $`\vartheta=0`$, $`P`$ projects onto the constant scalar alias, $`DP=0`$, and $`Q`$ reads exactly the constant vector alias.
The same bound follows directly.
Parseval gives

```math
\|A\|_2^2+\|\nabla A\|_2^2\le C E(A), \tag{A.11}
```

uniformly in mesh and volume.
No frequency grid is enumerated.

The same sine quotient gives $`|q_{\mu,0}|\ge(2/\pi)^5`$ on the whole coarse Brillouin zone.
For prescribed $`B_\mu`$, use $`A_{\mu,0}=B_\mu/q_{\mu,0}`$ and set all high aliases to zero.
This is a right inverse of $`Q`$ with $`H^1`$ norm at most $`C\|B\|_2`$.
Minimize $`E`$ with $`QA=B`$.
Variations $`D\lambda`$, $`Q'\lambda=0`$, preserve curl and rows by (A.3).
Their stationarity gives $`RD^TA=0`$.
The minimizing lift $`HB`$ therefore obeys

```math
QHB=B,\qquad RD^THB=0,\qquad\|HB\|_{H^1}\le C\|B\|_2. \tag{A.12}
```

It also minimizes curl energy on this slice, since the row mass is fixed.

### A.3 A two-scale interface with outward rows

This is Balaban's two-scale reduction, CMP 96 (2.95)–(2.129), with the row convention fixed above.
Use a unit intermediate lattice; its underlying fine mesh can still be arbitrarily small.
Let $`q,q'`$ be its uniform field and site means.
Mark an arbitrary union of complete blocks of side $`L`$ on the intermediate lattice.
Let $`P_s`$ retain outside sites and average each marked block.
Let $`U`$ retain bare outside bonds with neither endpoint marked, together with interior and outward length-$`L`$ rows.
Then the mixed rows are $`Q=Uq`$ and $`Q'=P_sq'`$.

Let $`R_s`$ project onto $`\Delta_s\ker q'`$, and $`R`$ onto $`\Delta_s\ker(P_sq')`$.
Let $`H'\omega`$ minimize $`\|\Delta_s\lambda\|_2^2`$ subject to $`q'\lambda=\omega`$.
The constraint fixes the constant; $`\Delta_s`$ is injective on $`\ker q'`$ by (A.4).
The variational equation makes $`\Delta_sH'\omega`$ orthogonal to $`\Delta_s\ker q'`$.
Decompose every $`\lambda\in\ker(P_sq')`$ as $`\lambda-H'q'\lambda+H'q'\lambda`$.
This gives

```math
R=R_s+R_+,\quad \operatorname{ran}R_+=\Delta_sH'(\ker P_s),\quad R_sR_+=0. \tag{A.13}
```

For a field $`A`$, solve $`\Delta_s\lambda_s=R_sD^TA`$, $`q'\lambda_s=0`$, and put

```math
A=HB+a+D\lambda_s,\qquad B=qA,\quad qa=0,\quad R_sD^Ta=0. \tag{A.14}
```

Pillar Poincaré and $`\|\nabla D\lambda_s\|_2=\|\Delta_s\lambda_s\|_2`$ give
$`\|D\lambda_s\|_{H^1}\le C\|R_sD^TA\|_2`$.
Stationarity of $`HB`$ gives $`CHB\perp Ca`$, and (A.11) on $`a`$ gives $`\|a\|_{H^1}\le C\|Ca\|_2`$.

The uniform coarse curl is a contraction:

```math
\|C_1qA\|_2\le\|CA\|_2. \tag{A.15}
```

To prove it, telescope the four averaged paths around a coarse plaquette.
Internal edges cancel, leaving the mean of the fine plaquettes in the translated spanning rectangles, divided by their area.
Its coefficients are nonnegative and sum to one.
At a fixed fine plaquette, the longitudinal tents in both plaquette directions partition the weights; transverse blocks partition the remaining directions.
After multiplying by coarse volume, the column sum is the fine volume.
Jensen and summation prove (A.15).

On every marked block use the coordinate tree to integrate $`B`$ from its root, obtaining $`t(x)`$.
Set $`\omega=t-\operatorname{Av}t`$ there and zero outside.
Then $`P_s\omega=0`$, and $`B_{\rm ax}=B-D_1\omega`$ vanishes on marked tree edges.
The endpoint-mean identity gives $`UB_{\rm ax}=UB`$.
We next prove

```math
\|B_{\rm ax}\|_2^2\le C_L(\|C_1B\|_2^2+M_U(B)), \tag{A.16}
```

where $`M_U`$ is exactly the mixed mass: bare outside bonds and $`L^2|Q_LB|^2`$ on retained coarse rows.

The block-face argument is Balaban's CMP 96 pp. 244–246, (2.123)–(2.128), Lemma 2.4.
For an internal marked bond, its value equals the circulation of that bond with its two root paths.
Cancel common coordinate segments and sweep the remaining bond through later coordinate segments.
At most $`3(L-1)`$ plaquettes occur, each with coefficient of magnitude one.
Cauchy–Schwarz bounds its square by $`4L`$ times the block curl norm squared.
There are at most $`4L^4`$ such bonds per block.

For a face bond, compare the root-to-root path through that bond with the root-to-root path through a translated straight segment from $`x`$ to $`x+Le_\mu`$.
The difference is a rectilinear closed loop in the double block with at most $`4d+2`$ coordinate segments.
Project it successively to the lower coordinate faces of the rectangle.
Each projection sweeps one rectangle per segment; connector edges cancel.
There are at most $`d(4d+2)`$ rectangles, each of area at most $`4L^2`$, and every plaquette has multiplicity at most $`d(4d+2)`$.
Weighted Cauchy–Schwarz bounds the squared circulation by $`C_dL^2`$ times the double-block curl norm squared.
Average over $`x`$ and use Jensen.
The averaged straight-path integral is $`K_cB=LQ_cB`$, so

```math
|B_{\rm ax}(b)-K_cB_{\rm ax}|^2\le C_dL^2\sum_{p\text{ in the double block}}|C_1B(p)|^2.
```

There are $`L^{d-1}`$ face bonds, and a block meets at most $`2d`$ such double blocks.
Use $`|u+v|^2\le2|u|^2+2|v|^2`$ and sum.
If the neighbouring block is unmarked, its root paths need not vanish.
Each has at most $`dL`$ retained bare bonds, whose squared path integral is bounded by $`dL`$ times their squared norm.
The face sum costs at most $`C_dL^d`$ times that bare norm, with bounded block overlap.
Bonds with neither endpoint marked are retained bare bonds; there $`B_{\rm ax}=B`$, and their squared norm is part of $`M_U(B)`$.
These are all possible faces, proving (A.16).
This argument is discrete Stokes with explicit finite bounds, not machine enumeration.

The identity

```math
HD_1\omega=DH'\omega \tag{A.17}
```

follows by uniqueness of the one-scale minimizer: the right side has mean $`D_1\omega`$, curl zero, and vanishing $`R_sD^T`$ by the defining orthogonality of $`H'`$.
Put $`A''=HB_{\rm ax}+a`$.
Equations (A.12), (A.14)–(A.16) bound its $`H^1`$ norm by $`C_LE_{\rm mix}(A)^{1/2}`$, where

```math
E_{\rm mix}(A)=\|CA\|_2^2+\|RD^TA\|_2^2+M_U(qA).
```

Equations (A.13)–(A.14) and (A.17) give

```math
\Delta_sH'\omega=R_+D^T(A-A''),\qquad
\|\Delta_sH'\omega\|_2\le C_LE_{\rm mix}(A)^{1/2}.
```

Since $`P_sq'H'\omega=0`$, (A.4) on pillars of side at most $`L`$ gives
$`\|H'\omega\|_2\le C_L\|DH'\omega\|_2`$.
Pair with $`\Delta_sH'\omega`$ to bound $`DH'\omega`$ in $`L^2`$, then use the full-lattice second-difference identity to bound its first gradient.
Returning to (A.14) proves

```math
\|A\|_2^2+\|\nabla A\|_2^2\le C_LE_{\rm mix}(A). \tag{A.18}
```

The local scale is 1 or $`L`$, so this is equivalent to the weighted energy estimate.
Restoring the smaller row scale rescales both sides equally.
The level-zero interface is included by making the underlying fine spacing equal to that smaller scale.

We also need a right inverse of the mixed field rows.
On the intermediate unit lattice first assign the prescribed data to every retained bare bond.
Each remaining coarse row has a central face pivot omitted from the bare rows.
Its coefficient in $`K_c=LQ_c`$ is $`L^{-3}`$, and no other coarse row reads that pivot: neighbouring longitudinal tents vanish at that crossing, transverse blocks are disjoint, and other components differ.
Set the pivot to $`L^3`$ times the remaining discrepancy, and set other unassigned bonds to zero.
The row and column counts at fixed $`L`$ give an intermediate field of norm at most $`C_L\|b\|_{\rm count}`$.
Lift it to the fine lattice with (A.12).
The resulting lift $`T_b`$ satisfies

```math
KT_b=b,\qquad\|T_b\|_E\le C_L\|b\|_{\rm count}. \tag{A.19}
```

This is the local elimination mechanism of Balaban, CMP 96 pp. 249–250, (2.152)–(2.157).
The one-scale case uses (A.12) directly.
In a bare boundary model take $`T_b=b/\eta`$; its energy norm has exactly the required four-dimensional scaling.

Let $`G`$ be the inverse of the local positive vector form and $`\Gamma=KGK^T`$.
Completing the square shows that the constrained minimum at $`KA=b`$ is $`\langle b,\Gamma^{-1}b\rangle`$.
The trial lift (A.19) gives $`\Gamma\ge c_LI`$.
Equation (A.18) and (A.2) give $`\Gamma\le C_LI`$.
Thus the field Gram inverse is uniformly bounded on local models.

### A.4 The local mixed inverses

Use the four-block system $`M_4`$ of §3.1 at identity, with $`B_v=C^TC+DD^T+Q^TaQ`$.
Its scalar elimination is Balaban's projection formula, CMP 99b p. 394, (3.25), written as a local saddle system.
For general sources $`(f,g_1,g_2,g_3)`$, its scalar equations give

```math
\begin{aligned}
\mu&=N\{Q'S(g_1+D^TA)+g_3-Q'S^2g_2\},\\
h&=Sg_2+SQ'^T\mu=PD^TA+h_0,\\
\lambda&=S(g_1+D^TA-h),\\
(C^TC+DRD^T+Q^TaQ)A&=f+Dh_0.
\end{aligned} \tag{A.20}
```

The scalar bounds in A.1 imply

```math
\|h_0\|_2\le C_L(\|g_1\|_2+\|g_2\|_{H^{-2}}+\|g_3\|_{\rm top})
```

on a normalized one- or two-scale periodic model.
Apply (A.18) to the last equation, then the other three equations successively.
Restoring scale gives $`M_4^{-1}:\mathcal X_4^*\to\mathcal X_4`$ with a constant depending only on $`L`$.
The scalar subsystem gives the same bound for $`M_3^{-1}`$.
The strong scalar estimate in A.1 gives $`M_1^{-1}:L^2\to H_m^2`$.
Adjoining the counting multiplier $`\nu`$ produces $`M_5`$.
Its last Schur complement is $`-KGK^T=-\Gamma`$.
Equation (A.19) and the two-sided Gram bound give its inverse with the counting norm of $`\nu`$.
The block factorization in Lemma 7.1 is a finite algebraic identity; it does not require the main inverse theorem.
Thus all four local mixed inverses have uniform bounds.

Near the outer Dirichlet boundary the model is entirely bare.
Here $`Q'=I`$, $`R=0`$, the field row mass is $`\eta^{-2}I`$, and the vector form is

```math
\|CA\|_2^2+\eta^{-2}\|A\|_2^2.
```

For zero extensions, $`\|\nabla A\|_2\le C\eta^{-1}\|A\|_2`$, so this controls the energy norm for every shape.
Also $`\|\lambda\|_{H_m^2}`$ is equivalent to $`\eta^{-2}\|\lambda\|_2`$ on this bare space.
The scalar inverse, (A.20), and $`K=\eta I`$ give all four inverse bounds there as well.
No regularity theorem for an artificial coarse Dirichlet corner is used.

### A.5 Assembly on an arbitrary admitted tower

This is Balaban's partition-of-unity argument, CMP 96 pp. 247–248, (2.141), Proposition 2.6.
Choose a large power $`M`$ of $`L`$, to be fixed after the local constants above.
Tile each layer with cubes of side $`M\ell_j`$, taking the tower's block size to be a divisible power at least $`M`$.
Include the bare exterior tiles needed for initial points of crossing field bonds.
Normalize sampled smooth bumps by the square root of their summed squares, as in §5.2.
On every active coordinate the denominator is at least one.
They obey

```math
\sum_i h_i^2=1,\quad |Dh_i|\le C_L/(M\ell_i),\quad
|D^2h_i|\le C_L/(M\ell_i)^2. \tag{A.21}
```

Take the separation larger than the fixed $`L`$-dependent multiple of $`M`$ needed for all read enlargements.
Reaching a layer two heights away crosses a collar of width at least $`\rho\ell_i/L`$, whereas an enlarged tile has radius at most $`C_LM\ell_i`$.
Thus an enlargement meets at most two adjacent heights.
Counting their grids gives overlap bounded by a constant depending on $`L`$, independent of $`M`$, depth and volume.
The first gap makes boundary enlargements bare.

For an interior tile, copy the actual one- or two-scale pattern, including every complete pillar and double block meeting the cutoff read, into a larger periodic box.
Insert a collar of width $`C_LM\ell_i`$, extend by the smaller row scale in a further collar, and make it periodic.
The larger blocks remain a union of complete blocks.
This is exactly a two-scale model of A.3, for any shape of the copied interface.
Its dimensions are fixed multiples of $`M\ell_i`$, and its cutoff vanishes before the edge.
For a boundary tile, copy the actual bare boundary and use zero extension at the edge of its enlarged model.
The torus-room choice embeds the needed reads.
If a whole periodic component is itself used as the local model, the same periodic estimates apply.
All local inverse constants in A.4 are independent of the size of these model boxes.

Let $`M_i`$ denote any one of the four local systems.
Its coefficients agree with the global $`M`$ on the support and full read closure of $`h_i`$.
The following identities are exact after transplantation:

```math
\mathbb B=\sum_i h_iM_i^{-1}h_i,\qquad
M\mathbb B=I+\mathbb R,\qquad
\mathbb R=\sum_i[M_i,h_i]M_i^{-1}h_i. \tag{A.22}
```

We prove the commutator estimate block by block.
For $`A_s:H_m^2\to L^2`$, the product rule gives terms $`(Dh_i)D\lambda`$ and $`(D^2h_i)\lambda`$, bounded by $`C_LM^{-1}\|\lambda\|_{H_m^2}`$.
The site mass commutator has the same bound because the cutoff oscillation within a pillar is at most $`C_L/M`$.
Transpose to obtain the corresponding $`L^2\to(H_m^2)^*`$ block.
For a first-order block the commutator is a shifted multiplication by $`Dh_i`$; the weighted zeroth-order energy term bounds it by $`C_L/M`$.
For the vector second-order block integrate one difference by parts.
Every remaining term has a cutoff difference and one field or field difference, hence form bound $`C_LM^{-1}\|A\|_E\|B\|_E`$.
For its row mass, insert the cutoff value at the row reference point.
The error is bounded by its double-block oscillation, $`C_L/M`$, and the physical counts (A.2) bound the row norms.
For the scalar constraint block,

```math
Q'(h_i\lambda)-h_i(\text{row})Q'\lambda
```

is bounded by $`C_L/M`$ times the average of $`|\lambda|`$.
Cauchy–Schwarz on each pillar pairs its $`m^{-2}`$ norm with the $`m^2\mu`$ norm.
For the added field constraint block, use
$`K(h_iA)-h_i(\text{row})KA`$ and the same double-block oscillation with (A.2).
The identity block commutes.
These are all nonzero blocks, so

```math
\|[M_i,h_i]X\|_{\mathcal Y}\le(C_L/M)\|X\|_{\mathcal X_i,\rm read}. \tag{A.23}
```

The argument works with the row reference point at the corner.
The product rule also bounds cutoff multiplication on $`\mathcal X`$ and $`\mathcal Y`$, uniformly in $`M`$.

For clarity, dual localization uses smooth synthesis.
The map $`(X_i)_i\mapsto\sum_i h_iX_i`$ is bounded from the direct sum of local spaces to the global space, by the product rule and overlap.
Its transpose sends $`F`$ to $`(h_iF)_i`$ with the same bound.
Pairing (A.23) with a global test field and using Cauchy–Schwarz and overlap bounds the map
$`(X_i)_i\mapsto\sum_i[M_i,h_i]X_i`$ by $`C_L/M`$.
Compose these maps with the direct sum of the uniformly bounded local inverses.
This gives

```math
\|\mathbb B\|_{\mathcal Y\to\mathcal X}\le C_L,\qquad
\|\mathbb R\|_{\mathcal Y\to\mathcal Y}\le C_L/M. \tag{A.24}
```

This includes the strong $`M_1`$ system and the second-order dual sources of the other systems.
It uses no sharp pillar cutoff on $`H^2`$.

Choose one power $`M_F=M`$ with $`C_L/M<1/2`$, then choose $`\rho_F`$ and the torus room $`t_F`$ for its reads.
The local constants were fixed before the box size, so the order is noncircular.
For each $`r\in\{1,3,4,5\}`$,

```math
M_r(1)^{-1}=\mathbb B\sum_{n\ge0}(-\mathbb R)^n,\qquad
\|M_r(1)^{-1}\|_{\mathcal Y_r\to\mathcal X_r}\le2C_L.
```

Choose $`B_F`$ to cover these four bounds and $`C_{\rm com},c_h`$ to cover (A.23) and cutoff multiplication for all four systems.
No constant depends on depth, fine mesh, volume or the admitted region shapes.

Finally the scalar saddle inverse gives the actual projection $`R`$, and elimination gives the actual vector Schur complement
$`T=C^TC+DRD^T+Q^TaQ`$.
It is a sum of nonnegative forms and is invertible, so it is positive definite.
If $`J_E`$ is the matrix of the squared energy norm, the inverse bound says
$`\|J_E^{1/2}T^{-1}J_E^{1/2}\|\le C_L`$.
Invert this positive matrix to obtain

```math
\langle A,TA\rangle\ge C_L^{-1}(\|\nabla A\|_2^2+\|m^{-1}A\|_2^2).
```

This proves the flat inverse lemma and the positivity used by the two singularity constructions. $`\square`$
