# The coarse covariance bound for the retained free background

Ethan and Levent,

Your free calculation uses $`|G_{k_1}(p,q)|\le CL^{-4k_1}`$
at [YM4_1400 102278–102281][target]. The statement is already yours.
The searches in §7 found its use, but no proof of this bound for the
retained background covariance elsewhere in that file.
This note supplies that proof using your actual plaquette average
and your strong inverse.

Your CF12 at [N 5631–5634] already compares the classical blocked
precision with the coarse Maxwell form: $`E_k(a)\ge\|\mathrm da\|^2`$.
We read this as a covariance bound for the actual blocked potential law.
We then bound its diagonal on every coarse torus. Your curvature
minimizer lifts this bound and gives the fourth power of the mesh.

References marked **N** mean your [YM4_1400.tex][source] at
2bc0658f91d2d03ba44e20bf695067e0a56a2ed9.
SA and CA-II mean your older outline and complete account at 31a47c543775.
The ported results below are yours.
The free-field minimizer method is due to Tadeusz Balaban.
Your [N 100996–101032][lift] implements that method for centered blocks.
SA 26141 cites CMP **95** (1984), (1.103), Proposition 1.2 and (1.110),
and CMP **96** (1984). Those papers were not available.
We used your quotations of them.

Codex (gpt-6-astra) wrote the proof and this note. Claude (Opus 5.5) checked the proof line by line, and its repairs are applied.
This is a proposed proof for your review. It is research text, not an audit, and grants no status.
No computation discharges a proof step.

## 1. Statement, notation and inputs

Fix an odd integer $`L\ge3`$. Use the trivial flat reference, one real
colour and unit coupling. Count each positive plaquette orientation once.
Raw cochains carry the counting inner product.

Let the fine physical spacing be $`a_K=L^{-K}`$.
The level-$`j`$ block spacing is your $`a_{K-j}=L^{-(K-j)}`$.
Take a compatible periodic torus of side $`\ell=2L^m`$, $`m\ge m_0\ge0`$.
At each $`0\le j\le K`$, put

```math
n=L^j,\qquad h=\eta_j=L^{-j},\qquad
N_j=\ell/a_{K-j}=2L^{m+K-j}\ge2.                       \tag{1}
```

Every rescaled torus has the integer side required by your
[N 41668–41677][geometry], including $`j=K`$.
The parameter called $`M`$ there is $`N_j`$ here.

Use your plaquette average $`\mathsf A^{(j)}`$ and spaces

```math
E=\Omega^2_{\mathrm{ex}}=\operatorname{ran}d,\quad P=P_{\mathrm{ex}},
\quad \mathsf W_j=E\ominus(E\cap\ker\mathsf A^{(j)}).
```

Your definitions and Gaussian conditioning at [N 4325–4340][tower]
and [N 100440–100456][background] give

```math
F_j=\mathbb E[F\mid\mathsf A^{(j)}F]=P_{\mathsf W_j}F,\qquad
G_j=\operatorname{Cov}(F_j)
=P_{\mathsf W_j}=C^{\mathrm{bg}}_{K,K-j},             \tag{2}
```

where $`F`$ is standard Gaussian on $`E`$.
Here $`F_j`$ is your retained background, not the blocked coarse curvature.

**Claim.** A constant $`C_R`$, independent of $`K,j,m,p,q`$, satisfies

```math
0\le G_j(p,p)\le C_RL^{-4j},\qquad
|G_j(p,q)|\le C_RL^{-4j},\qquad 0\le j\le K.             \tag{3}
```

In particular $`G_K`$ is retained and obeys $`|G_K(p,q)|\le C_Ra_K^4`$.

The ported analytic input is your uniform strong joint inverse,
[N 41990–42038][strong], on the homogeneous periodic geometry just stated.
We use its written proof and its curvature identification,
[N 101007–101029][lift]. We also use your curvature contraction,
[N 5568–5605][contraction]. These are your results, not new claims here.

For the adjoining free tower we quote your slice estimate
at [N 4337][slice] and [N 100994][slice2]:

```math
|\mathcal C_{(j)}(p,q)|
\le C\eta_{j-1}^4
\exp\!\left(-\delta d_{\mathbb T}(x(p),x(q))/a_{K-j+1}\right).
\tag{4}
```

It is an input, not reproved here.
The proof of (3) does not use (4).

## 2. Your strong inverse gives a summable curvature lift

Rescale a level-$`j`$ block to side one.
Let $`D_h,d_h`$ denote the physical fine gradient and curl.
Let $`d_c`$ denote the raw coarse curl, at spacing one.
Write $`d_{0,c}`$ for the coarse gradient.
Your straight row and site average at [N 41699–41703][rows] are

```math
Q_hv(y,\mu)=h^5\sum_{x\in B(y)}
\sum_{t=0}^{n-1}v_\mu(x+th e_\mu),\qquad
q\lambda(y)=h^4\sum_{x\in B(y)}\lambda(x).
```

For a raw fine potential $`w=hv`$, they give

```math
Q_hv=S_nw,\qquad dw=h^2d_hv,\qquad
\sum_p|(dw)(p)|^2=h^4\sum_p|(d_hv)(p)|^2.                \tag{5}
```

Here $`S_n`$ is your raw straight average.
The last identity uses dimension four and matches the Gaussian energy in (2).

We recall the part of your strong-inverse proof used below.
Write $`L_h=D_h^\sharp D_h`$, and distinguish the site projection $`R_g`$
from every curvature covariance:

```math
G_s=(L_h+q^\sharp q)^{-1},\quad F_s=G_sq^\sharp,\quad
\Pi_s=F_s(F_s^\sharp F_s)^{-1}F_s^\sharp,\quad R_g=I-\Pi_s,
```

```math
K_0=d_h^\sharp d_h+D_hR_gD_h^\sharp+Q_h^\sharp Q_h.
```

The transpose $`\sharp`$ uses physical fine measure $`h^4`$ and coarse
counting measure. Your site projector and smoothing are at
[N 41886–41941][smoothing].

Your homogeneous Landau gap, [N 25865–26025][gap], controls $`K_0^{-1}`$
in energy norm, uniformly in mesh and volume.
Its proof uses Bloch decomposition, trigonometric interpolation,
Rellich compactness and a zero-kernel calculation.
It uses no numerical spectral test.
Your small exponential conjugations give, for $`u=K_0^{-1}f`$,

```math
\|u\|_{2,\mathrm{cell},\infty}\le C\|f\|_\infty.
```

The factorization

```math
D_h\Pi_sD_h^\sharp
=(D_hF_s)(F_s^\sharp F_s)^{-1}(D_hF_s)^\sharp
```

maps this cell norm to the supremum norm.
The required row bounds also hold for $`Q_h,Q_h^\sharp`$.
Your flat Hodge identity therefore gives

```math
L_hu=f+D_h\Pi_sD_h^\sharp u-Q_h^\sharp Q_hu,
```

with right side bounded by $`C\|f\|_\infty`$.
Your heat argument at [N 41781–41884][heat] uses

```math
u=e^{-L_h}u+\int_0^1e^{-tL_h}L_hu\,dt,\qquad
\|D_he^{-tL_h}\|_{\infty\to\infty}\le C(t+h^2)^{-1/2}.
```

The time singularity is integrable.
Together with fixed-time smoothing, this proves the supremum and
first-derivative bounds in your [N 41943–41988][vector].
This recalls your proof; it adds no endpoint singular-integral assumption.

Set $`S_Q=Q_hK_0^{-1}Q_h^\sharp`$.
Your exact row seed $`E_Q`$, [N 41708–41779][seeds], satisfies $`Q_hE_Q=I`$
and has uniformly bounded $`K_0`$ energy. Hence

```math
\|b\|_2^2
=\langle K_0^{-1}Q_h^\sharp b,K_0E_Qb\rangle
\le C\langle b,S_Qb\rangle^{1/2}\|b\|_2.
```

Thus $`S_Q\ge cI`$.
Your weighted inverse and this lower bound give exponential coarse
cell decay for $`S_Q^{-1}`$, hence its supremum norm bound.
Your joint inverse at [N 42009–42038][strong] then gives

```math
H_hB=K_0^{-1}Q_h^\sharp S_Q^{-1}B,\qquad
\|d_hH_hB\|_\infty\le C_H\|B\|_\infty.                  \tag{6}
```

Fix the source Hölder exponent at $`1/2`$.
The resulting $`C_H`$ is uniform in $`h,N_j`$.
The seed construction includes $`h=1`$.
Only the first-derivative part of the strong norm is needed.

We use your curvature identification, [N 101007–101019][lift].
The zero-force saddle equation is

```math
(d_h^\sharp d_h+D_hR_gD_h^\sharp)H_hB-Q_h^\sharp\omega=0,
\qquad Q_hH_hB=B.
```

Test against $`D_h\lambda`$, with $`q\lambda=0`$.
The curl vanishes, and $`Q_hD_h\lambda=d_{0,c}q\lambda=0`$.
Your range identity
$`\operatorname{ran}R_g=L_h(\ker q)`$,
[N 25839–25854][range], makes the remaining tests span
$`\operatorname{ran}R_g`$. Thus $`R_gD_h^\sharp H_hB=0`$.
The saddle equation becomes the Euler equation for the convex curl
energy on $`Q_hv=B`$, hence gives a minimizer.

The range identity follows from your scalar algebra.
If $`q\lambda=0`$, then $`G_sL_h\lambda=\lambda`$, so
$`F_s^\sharp L_h\lambda=q\lambda=0`$.
Conversely $`F_s^\sharp\rho=0`$ implies $`qG_s\rho=0`$
and $`L_hG_s\rho=\rho`$. This proves both inclusions.

If an exact raw curvature $`f=dw`$ has
$`\mathsf A^{(j)}f=d_cB`$, then $`S_nw-B`$ is closed.
A closed coarse one-form is a gradient plus a constant:
each nonzero Fourier mode is parallel to the gradient symbol,
and the zero mode contributes the constant.
A fine constant removes the constant defect, since $`S_nc=nc`$.
A fine gradient removes the gradient defect:
$`S_nd=d_{0,c}q`$, and $`q`$ is onto by your site seed.
Both corrections preserve $`f`$.
Thus the potential fibre and prescribed-curvature fibre have the same curvature image.

The least-norm curvature is unique.
Using (5), your raw curvature minimizer is therefore

```math
\mathcal H_jB=h^2d_hH_hB.          \tag{7}
```

It depends on $`B`$ only through $`d_cB`$, as in
[N 4339–4340][tower] and [N 100989–101029][lift].

Put $`T_h=d_hH_h`$, in ordinary coordinate values.
For a fixed row $`p`$, choose coarse bond data equal to the signs
of that row. The matrix is real and these data have supremum norm
at most one. Equation (6) gives

```math
\sup_p\sum_b|T_h(p,b)|\le C_H.     \tag{8}
```

## 3. Bound the actual blocked potential variance

Write

```math
E_c=\operatorname{ran}d_c,\quad P_c=P_{E_c},\quad
\Phi_j=\mathsf A^{(j)}F,\quad
V_j=\operatorname{Cov}(\Phi_j)=\mathsf A^{(j)}P(\mathsf A^{(j)})^*.
```

Here $`\Phi_j`$ is the actual coarse curvature.
It differs from the retained fine field $`F_j`$.
Every star in this section uses counting coordinates.

Your contraction proof, [N 5568–5605][contraction], applies to this map.
Its consequence CF12, [N 5631–5634], is the precision form of (10) below.
Its nonnegative row weights sum to $`n^2`$.
Its column weights sum to $`n^{-2}`$.
Weighted Cauchy–Schwarz gives

```math
\sum_P\left|\sum_p t_{Pp}f_p\right|^2
\le\sum_P\left(\sum_pt_{Pp}\right)
\left(\sum_pt_{Pp}|f_p|^2\right)
\le n^2n^{-2}\sum_p|f_p|^2.
```

Periodic multiplicities give the same counts on every torus in (1).
Thus $`\|\mathsf A^{(j)}\|_{2\to2}\le1`$.
Its image of $`E`$ lies in $`E_c`$.
For any coarse two-form $`u`$,

```math
\langle u,V_ju\rangle
=\|P(\mathsf A^{(j)})^*P_cu\|^2\le\|P_cu\|^2.
```

Consequently

```math
0\preceq V_j\preceq P_c.      \tag{9}
```

Choose the canonical potential space
$`X_c=(\ker d_c)^\perp=\operatorname{ran}d_c^*`$.
The map $`d_c:X_c\to E_c`$ is bijective; call its inverse $`T_c`$.
Extend $`T_c`$ by zero on $`E_c^\perp`$ when acting on all coarse two-forms.
Set $`B_j=T_c\Phi_j`$ and $`S_j=\operatorname{Cov}(B_j)`$.
This chooses a representative of the actual blocked curvature.
It removes no component of that curvature.
It defines a possibly degenerate Gaussian without a gauge integral.

Taking covariance and applying (9) yields

```math
S_j\preceq T_cP_cT_c^*
=\iota_X(d_c^*d_c|_{X_c})^{-1}\iota_X^*.              \tag{10}
```

Here $`\iota_X`$ includes $`X_c`$ into the coarse one-forms.
The equality follows by inverting the bijection $`d_c|_{X_c}`$.

Use your flat Hodge identity from [N 41960–41972][vector],
at coarse spacing one:

```math
d_c^*d_c+d_{0,c}d_{0,c}^*=\Delta_c I.
```

Expanding the differences verifies it: mixed terms cancel, leaving
the scalar Laplacian on each component.
On $`X_c`$, the second term vanishes.
This space is orthogonal to constant one-forms and invariant under $`\Delta_c`$.
Thus the right side of (10) equals
$`\Delta_c^+\Pi_{X_c}\preceq\Delta_c^+I`$.
The superscript $`+`$ means inverse on the complement of the constant mode.

On a coarse torus of integer side $`N`$, the characters
$`N^{-2}e^{2\pi i k\cdot x/N}`$ are orthonormal.
Their Laplacian eigenvalues are $`4\sum_\mu\sin^2(\pi k_\mu/N)`$.
This is the unit-spacing version of your Fourier convention at
[N 124100–124139][fourier].
Each character has squared modulus $`N^{-4}`$. Hence

```math
S_j(b,b)\le g_{N_j}(0),\qquad
g_N(0)=N^{-4}\sum_{k\ne0}
\frac1{4\sum_{\mu=1}^4\sin^2(\pi k_\mu/N)}.       \tag{11}
```

Choose one representative of each frequency with $`|k_\mu|\le N/2`$.
No mass has been added; only the constant potential mode is absent.

Concavity gives $`\sin t\ge2t/\pi`$ for $`0\le t\le\pi/2`$.
Thus the denominator is at least $`16|k|^2/N^2`$.
The shell $`|k|_\infty=r`$ has at most

```math
(2r+1)^4-(2r-1)^4=64r^3+16r\le80r^3
```

integer points. Restriction to frequency representatives decreases the count.
For $`q=\lfloor N/2\rfloor`$, $`N\ge2`$, this gives the written bound

```math
g_N(0)\le\frac5{N^2}\sum_{r=1}^q r
=\frac{5q(q+1)}{2N^2}
\le\frac58+\frac5{4N}\le\frac54.                       \tag{12}
```

No machine evaluation enters this inequality.
Covariance Cauchy–Schwarz gives

```math
|S_j(b,c)|\le5/4.            \tag{13}
```

Comparison (10) proves this for the induced law.
It does not replace that law by a fresh Maxwell law.

## 4. Lift the variance and retain the terminal covariance

Your conditioning identity (2) makes $`F_j`$ the least-norm exact
fine curvature with datum $`\Phi_j`$.
Since $`d_cB_j=\Phi_j`$, (7) gives the pathwise identity

```math
F_j=\mathcal H_jB_j=h^2T_hB_j,\qquad
G_j=h^4T_hS_jT_h^*.                                   \tag{14}
```

These are identities of the fields and their covariances.
Equality of minimum energy values alone would not suffice.
All matrices in (14) use ordinary coordinate values.
The physical transpose was used only to construct $`H_h`$.

Equations (8), (13) and (14) give, at every fine plaquette,

```math
0\le G_j(p,p)
\le\frac54h^4\left(\sum_b|T_h(p,b)|\right)^2
\le\frac54C_H^2L^{-4j}.
```

Apply covariance Cauchy–Schwarz again:

```math
|G_j(p,q)|\le\sqrt{G_j(p,p)G_j(q,q)}
\le C_RL^{-4j},\qquad C_R=\frac54C_H^2.          \tag{15}
```

This proves (3) at each position, not only after averaging positions.

Fix $`L`$, dimension, the trivial reference and the source Hölder
exponent before $`K,j,m`$. Your strong bound then fixes $`C_H`$.
Equation (12) has the same constant for every $`N_j\ge2`$.
At $`j=0`$, $`G_0=P`$.
At $`j=K`$, (14) still contains the random coarse potential $`B_K`$.
It gives $`|G_K(p,q)|\le C_Ra_K^4`$, without setting $`G_K`$ to zero.

Your nested projections at [N 4332–4340][tower] already give

```math
P=\sum_{i=1}^j\mathcal C_{(i)}+G_j,\qquad
\mathcal C_{(i)}=G_{i-1}-G_i\succeq0,\qquad G_j\succeq0. \tag{16}
```

Positive semidefinite does not mean entrywise nonnegative.
Your flat-law comparison at [N 101043–101077][law] identifies these
same slices in the plain/soft-contour and straight/tree quadratic laws.
It removes closed coarse defects by fine constants and gradients.
Normalized contour integration has a constant value on each curvature fibre.
The sharp tree gauge selects one lift; constant linear Jacobians cancel.
These are your identifications, including their harmonic-mode treatment.
They concern full quadratic laws, not cutoff windows.

Together, (4), (15) and (16) supply the stated free tower.
The fixed slice-level shift is harmless:

```math
\eta_{j-1}^4=L^4\eta_j^4,\qquad a_{K-j+1}=a_{K-j}/L.
```

Changing attachment points to bare plaquette barycentres moves each
endpoint by at most $`a_K/\sqrt2`$.
It changes the slice exponential by a fixed factor.
The residual bound has no distance factor.
In density units it reads
$`|a_K^{-4}G_j(p,q)|\le C_Ra_{K-j}^{-4}`$.
Running factors $`x_i^{-1}`$ are absent throughout this proof.

## 5. What this supplies at N 102258–102291

Your telescoping half-square calculation at [N 102258–102291][consumer]
already retains the covariance subtraction.
At zero terminal field its covariance is $`G_j^\circ=G_j-G_{k_1}`$.
The free sum is $`\tfrac12(G_{k_0}-G_{k_1})(p,q)^2`$.

Equation (15) supplies precisely the coarse bound invoked there.
Retain your separated-support input
$`|G_{k_0}(p,q)|\le Ca_K^4\mathsf d^{-4}`$.
For $`A=G_{k_0}(p,q)`$, $`B=G_{k_1}(p,q)`$,

```math
\left|\tfrac12(A-B)^2-\tfrac12A^2\right|
\le |A||B|+\tfrac12|B|^2.
```

Each support has at most $`C(\mathsf d/a_K)^4`$ plaquettes.
After smearing, the error is bounded by

```math
C\left[\left(\frac{\mathsf d}{a_K}L^{-k_1}\right)^4
+\left(\frac{\mathsf d}{a_K}L^{-k_1}\right)^8\right]
\|f_1\|_\infty\|f_2\|_\infty.
```

With $`k_1=k_0+\mathsf n`$ and
$`\hat{\mathsf d}=\mathsf d/a_{K-k_0}`$, this is your
$`C[(\hat{\mathsf d}L^{-\mathsf n})^4+
(\hat{\mathsf d}L^{-\mathsf n})^8]\prod_i\|f_i\|_\infty`$.
The note proves the coarse factor in that error.
It does not change your telescoping argument or choice of segment.

## 6. Scope

The inequality (9)–(10) is the covariance form of your CF12.
The new steps are the diagonal bound (11)–(13) and the pathwise lift (14)–(15).
The averaging map, its contraction, the strong inverse, the curvature
minimizer and the Gaussian projection algebra are yours.
Balaban supplies the underlying free-field method.
We quote the slice estimate (4). We do not reprove it, and the proof of (15) does not use it.

This note does not prove spatial decay of $`G_j`$.
It does not reprove the full-$`P`$ continuum comparison, the
separated-background estimate used in §5, or the slice estimate.
It does not handle nontrivial holonomy, layered geometries,
proper-region boundaries, nonlinear backgrounds or cutoff windows.
Your strong inverse has broader scope; we use its trivial periodic specialization.

It supplies no interacting source law, regular-source or amplitude
estimate, transfer theorem, nontriviality theorem or existence theorem.
Setting a terminal *field* to zero never sets its unconditioned
*covariance* to zero.

## 7. Search record and prior contribution

All searches below ran over the whole pinned N file.
They used the command rg -n -i -F 'PATTERN' YM4_1400.tex.
These are all matching line numbers, including false positives.

| Pattern | All hit lines |
|---|---|
| `covariance bound` | 6633, 101488, 102280, 102359, 109001, 109332, 110541 |
| `coarse covariance` | 6223, 102280, 106650 |
| `L^{-4` | 707, 3579, 3588, 3589, 3591, 3597, 3605, 3624, 4329, 4522, 4528, 4544, 4730, 4733, 4748, 4761, 4767, 5030, 5167, 5230, 5237, 5297, 5524, 6148, 6666, 8244, 8258, 8259, 8261, 8282, 8328, 10959, 10968, 17574, 18697, 18769, 18776, 18778, 18779, 22463, 22801, 23910, 27561, 27576, 34483, 34489, 34515, 42136, 42369, 42374, 42981, 43037, 54799, 68013, 70808, 72373, 74791, 75030, 75493, 75501, 77214, 79022, 81282, 81288, 81295, 84030, 84087, 84092, 96606, 96609, 96658, 98097, 98102, 100668, 100695, 101085, 101951, 101952, 101961, 102069, 102281, 102564, 103135, 104879, 104919, 105026, 105031, 105037, 105063, 106493, 106581, 106607, 108113, 108945, 110561, 110611, 110700, 110702, 110755, 110759, 110772, 124135, 124139, 124151, 124179, 124181, 124247, 124268, 124312, 124315, 124318, 124321, 124336, 124351, 124372, 124376, 124437, 130765 |
| `G_{k` | 1795, 4563, 55922, 55928, 63829, 63879, 84480, 84665, 84684, 84692, 84805, 84808, 100391, 100519, 100561, 101961, 102265, 102278, 102279, 102281, 102282, 102309, 102337, 108173 |
| `blocked covariance` | None |
| `P_{W` | 117287 |

The case-insensitive G_{k} prefix also matches running couplings.
The literal P_{W misses the typeset projection; its sole hit is
a Schwartz seminorm at 117287. We therefore searched the actual notation.
These searches used case-sensitive rg -n -F:

| Pattern | All hit lines |
|---|---|
| `P_{\mathsf{W}` | 4332, 4335, 4336, 4340 |
| `C^{\mathrm{bg}}` | 100443, 100444, 100445, 100448, 100451, 100452, 102259, 102303 |
| `C^{\rm bg}` | None |
| `G_j` | 16443, 66517, 66525, 69593, 76558, 76591, 76600, 76739, 77565, 77570, 77982, 96274, 96386, 102259, 102265, 102275, 109458, 109464, 115535, 118980, 118995, 118997, 118999, 119023, 119039, 119062, 119083, 136077 |
| `G_{j}` | None |
| `background covariance` | 110355, 110372 |
| `coarse variance` | None |
| `\eta_j^4` | 108049 |

We also searched the literal $`\eta_j^2`$ factor.
Its relevant minimizer hits are 100993 and 101028.
The $`\eta_j^4`$ hit at 108049 concerns a Wilson action on a regular layer.

The candidate passages were read in bounded source ranges:

| Passage | What it supplies |
|---|---|
| 4325–4340; 100440–100456 | Defines $`P_{\mathsf W_j}`$ through projections and states the slice estimate. Projection algebra alone gives no $`L^{-4j}`$ diagonal bound. |
| 5568–5605 | Proves the actual curvature contraction used in (9). |
| 5605–5634; 6522–6528 | CF11–CF12: $`E_k(a)\ge\Vert \mathrm da\Vert ^2`$. The precision form of (10). Used there for the fluctuation gap, not for the background covariance. |
| 6208–6240 | FX7 is an auxiliary Feynman potential covariance in Fourier coordinates, not the retained bare curvature covariance. |
| 6629–6639 | A first-step curved Hessian bound; explicitly not an iterated result. |
| 25865–26025; 41659–42061; 100989–101032 | Proves the homogeneous strong inverse and curvature-lift bound. These are ported suppliers, not a proof there of (9)–(15). |
| 101043–101085 | Identifies flat slice laws and estimates the fluctuation complement. The finite slice sum leaves the terminal covariance. |
| 101475–101502; 102359–102389 | Local reference covariance and interacting-source bookkeeping, not an all-level retained-background estimate. |
| 102258–102291 | States the target at 102280–102281 and uses it in the error. No numbered supplier accompanies that sentence. |
| 106469–106499; 106635–106657 | A deterministic top-field estimate, then a later use of the free calculation's omitted coarse covariance error. |
| 108983–109023; 109305–109332 | Fixed-step curvature projections and their limits; expressly not an all-depth unweighted covariance bound. |
| 110353–110378 | Background projection identity, explicitly separated from decay and law-identification requirements. |
| 110522–110566; 110681–110709; 110741–110779 | Finite-segment determinant, top-field errors and uses of the coarse-edge factor. No separate proof of the retained covariance bound. |
| 124100–124139; 124360–124376 | Full exact-curvature Fourier kernel and the end of its continuum comparison. This concerns $`P`$, not $`G_j`$. |

The matching older account estimate is already explicit:
[CA-II 69958–69965][ca-bound] states

```math
|C^{\mathrm{bg}}(p,q)|
\le C_u\eta^4(1+|x_p-x_q|)^{-4}.
```

Its [hypothesis (h1), 69927–69929][ca-input], cites minimizer estimates
and the free-current operator theorem.
The [proof at 70002–70016][ca-proof] assigns the displayed bounds to that hypothesis.
We do not claim the estimate itself is new.
The present proof derives the weaker bound (15) from the written
N suppliers, without assuming that stronger covariance estimate.

**Finding.** These searches and supplier passages did not locate
a proof of (3) elsewhere in N under another name.
They located its assertion, later uses, and the ported results needed here.
This is a finding about the pinned text.
It is not a claim about later revisions or all published work.

[source]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex
[target]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L102278-L102281
[consumer]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L102258-L102291
[tower]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L4325-L4340
[background]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L100440-L100456
[geometry]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L41668-L41677
[rows]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L41699-L41703
[seeds]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L41708-L41779
[heat]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L41781-L41884
[smoothing]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L41886-L41941
[vector]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L41943-L41988
[strong]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L41990-L42038
[gap]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L25865-L26025
[range]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L25839-L25854
[lift]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L100989-L101032
[contraction]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L5568-L5605
[slice]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L4337
[slice2]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L100994
[law]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L101043-L101077
[fourier]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L124100-L124139
[ca-bound]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L69958-L69965
[ca-input]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L69927-L69929
[ca-proof]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L70002-L70016

