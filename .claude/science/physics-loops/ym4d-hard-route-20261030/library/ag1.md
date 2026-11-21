# AG1: Uniform rarity of old large-field regions

Provenance: Pass 2 distillation by Codex at repository commit `2afa141308f85e0fb262acd684c25a49e354feb6`, from Claude's pass-1 AG1 and P-an drafts; research text, without audit or retained status. Material from the pinned Sussman–Alpoge account is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text.

This manuscript distils `ag1-draft2.md`, `ag1-tt-draft.md` and
`pan-draft.md`, with `ag1-draft.md` as context. `tp1.md` is frozen.
Theorem 12 has precisely TP1's AG-k1* conclusion. It is conditional:
the owner inputs below, and the explicitly marked outstanding interfaces,
are not proved by naming them. All proofs below are analytic arguments;
no calculation performed by a program discharges an obligation.

## 1. Definitions and hypotheses

**1.1. Scales and age.** Work on a finite four-dimensional periodic
lattice with $\mathrm{SU}(2)$ bond variables. Fix an odd block factor
$L\ge3$, microscopic spacing $a_0$,
and mesh $a_j=L^ja_0$. Write $x_j$ for the running inverse coupling,
$g_j=\theta_j^{-1/2}$, $p_j=A_0(\log\theta_j)^{p_0}$,
$\delta_j=(A_1/A_0)g_jp_j$, and

\[
 R_j=L^{\lceil\log_L[(\log\min_{t\le j}x_t)^r]\rceil},\qquad
 c_j=MR_ja_j,\qquad r_j=M^4R_j^5.                 \tag{1}
\]

Cells have side $c_j$, and adjacency means that their closures meet.
The choices below ensure $R_{j-1}/R_j\in\{1,L\}$, so the cell partitions
are nested. Sup-distance between cells is measured in cell units; between
fine bonds it is measured in the lattice units specified at that occurrence.
Distance to the empty set is $+\infty$.
For a set $D$, $D^{+s}$ and $D^{-s}$ are its closed $s$-neighbourhood
and its inner erosion in the stated units. A $w$-path has successive
cell indices at sup-distance at most $2w+1$.

$Z_j^{\rm pre}=\Lambda_j^{\rm pre,c}$ is the large-field region before
healing; $\mathcal Z_j$ is its live part after healing. Initially
$\mathcal Z_0=\varnothing$. For a component $C\subset\mathcal Z_k$,
put $\mathsf Z_k(C)=C$, and recursively let $\mathsf Z_{j-1}(C)$
be the union of the live components at $j-1$ contained in
$\mathsf Z_j(C)$. Its age is
$k-\min\{j:\mathsf Z_j(C)\ne\varnothing\}$.
$\mathfrak L_k^{\ge a}(c)$ means that $c$ belongs to a live component
of age at least $a$. This is lineage age, not label age or the age of
an earlier creation at the same place. For a level-$n$ cell $z$,

\[
 E_z^{(n)}(q)=\{z\subset\mathcal Z_j\text{ for every }n\le j\le q\}.
                                                               \tag{2}
\]

It is the sure event when $q<n$. An age-$a$ lineage has a cell of
$\mathsf Z_{k-a}(C)$ satisfying (2) through $k$: nestedness proves this
directly, including when the actual age exceeds $a$.

**(FLOW), owner IN1.** The stopped run has $|x_j-\theta_j|\le\theta_j/4$
and, for $i\le j$,

\[
 (c_f/2)(j-i)-2c_2\le x_i-x_j
       \le(c_f+1)(j-i)+2c_2.                    \tag{3}
\]

There is also an upper frame envelope $\bar B$, fixed before the final
coupling ceiling; the analogous frame bounds hold for $\theta$.
In particular $x_i\ge x_j-2c_2$, not necessarily $x_i\ge x_j$.
All estimates asserted uniformly in the coupling mean a supremum over
the entire half-line above the stated lower bound, not a check at its endpoint.

**1.2. Positive histories and tests.** Denote the law stopped at $k$ by
$\mathbb P^{(k)}$. The following are inputs from LF1 and LG1.

* **(ANC), LF1(2):** if a cell is live at levels \(j-1\) and \(j\), its live component at level \(j-1\) lies inside its live component at level \(j\). SA 23328 states this ("At every one of these levels it belongs to the lineage of the component that is live at level \(k\) and contains it"); it is not among (R0)–(R3) and is used by Lemma 1 (lines 412–413). **Outstanding** as an LF1 verification.

* **(K), (MI), LF1:** the construction is a finite adapted composition of
  positive probability kernels over the Wilson field $U$. Each possible
  decision or draw has its own independently assigned uniform variable,
  with a fixed location, and is used at most once. Reusing a recorded test
  reuses its decision, not a new uniform. When a site is reached its pass
  probability is measurable before its own uniform is exposed. Continuous
  draws are kernels too: a product of scalar point probabilities is not
  their definition. Integrating the successive kernels gives the same
  positive stopped law and its nonnegative history weights $t(dh)$.
* **(COV), LF1:** locations, schedules, kernels and recorded histories
  commute with the reflections and translations used below. Locations
  are assigned off tile faces, or assigned by a fixed covariant boundary
  convention. No uniform is assigned to two tiles.
* **(SM):** a test of normalized nonnegative size $q$ passes with weight
  $\zeta(q)$, where $\zeta=1$ on $[0,1]$,
  $\zeta(t)=5-4t$ on $[1,5/4]$, and $\zeta=0$ beyond $5/4$.
  Undefined tested values fail. Given its uniform $u$, a test is the
  sharp test $q<1+(1-u)/4$, apart from null equality events.
* **(ROOM), LF1/BG1/NL1:** all uses of passed thresholds retain their
  margins after replacing the upper threshold by $5/4$ of its old
  value. In particular approximate tests are identically one on the
  free-bond window; strip cutoffs are one there; reconstructed fields
  lie in their declared charts and hereditary domains. The collar/rim
  estimate, in Euclidean coordinates, must satisfy
  \[
  (5/4)c_N^2 C\{\Theta_1^{-1}+\theta_c e^{-c\varpi_T}
                         +e^{-cMR_j}\}\le\theta_c/8.             \tag{4}
  \]
  Here $\theta_{\rm col}=1/(4\Theta_1)\le\theta_c$, and
  $c_N^{-1}|v|\le\|v\|_B\le c_N|v|$ compares the test norm with
  Euclidean norm. These are requirements on the actual thresholds;
  monotonicity of an individual passing set does not prove them.
* **(CB), LG1(3):** for bounded nonnegative functions of distinct tiles
  in any of the aligned reflected tilings, the Wilson measure times
  the product uniform measure satisfies the chessboard inequality
  \[
  \mathbb E\prod_\beta f_\beta\le\prod_\beta\|f_\beta\|_{\rm ch},
  \quad \|f\|_{\rm ch}
       =\bigl(\mathbb E\prod_\gamma\vartheta_\gamma f\bigr)^{1/N}.
                                                               \tag{5}
  \]
  There are $N$ tiles. The input includes the permitted face planes
  and reflection of the auxiliary variables. It is not a reflection
  positivity assertion for the effective action.
  The admissible tori also satisfy the geometric alternative used here:
  they admit the proposed tiling and its 16 integer-cell shifts, or
  their side is less than twice the proposed tile side. This includes
  divisibility requirements; it is not automatic on an arbitrary torus.

**1.3. Geometry and trace masses.** A node of a lineage is a pair
$(j,C)$ with $C$ live at $j$, of weighted size $v(j,C)=r_j|C|_j$.
Write ${\rm pred}(j,C)$ for its predecessors, ${\rm Act}_{j-1}$
for the predecessors on which healing acted without removing them,
and $W$ for creations in $C$. Put

\[
 e(j,C)=(|{\rm pred}|-1)_++|{\rm pred}\cap{\rm Act}_{j-1}|
                          +\sum_{W\subset C}(d'_j(W)+1).        \tag{6}
\]

Here $d'_j(W)$ is a tree size which bounds $|W|_j-1$.
The following are **LF1(2) inputs**, rather than consequences of an
unproved age lemma in the complete account:

* **(R0):** every node has at most one successor; a node with no
  predecessor contains a creation.
* **(R1):** with $A,C_N\ge1$ and $\lambda\le1/6$,
  $v(j,C)\le\lambda\sum_{{\rm pred}}v+
  Ar_j(|{\rm pred}|+\sum_W(d'_j(W)+1))$.
* **(R2):** a maximal consecutive chain of nodes with $e=0$, whose
  first predecessor is $P$ and whose first level is $s$, has length
  at most $C_N(R_s+\log(2+|P|))$.
* **(R3):** healing acts only on components and stored sections of
  diameter at most a fixed $C_R$ cells; new creations remain live.

For a lineage $l$, define its event cost

\[
 {\rm EC}(l)=\sum_{(j,W)\in l}p_j(d'_j(W)+1)
       +\sum_{(j,C)\in l}p_{j-1}|{\rm pred}(j,C)\cap{\rm Act}_{j-1}|.
                                                               \tag{7}
\]

**(LT), owner LF1(3).** Let $\mathcal M_D$ consist of all terminal
live lineages and the distinct lineages healed by $k$ which contain a
designated cell of $D$ at its designated level. Assume

\[
 \mathbb E^{(k)}\exp\{\tfrac14\sum_{l\in\mathcal M_D}{\rm EC}(l)\}
   \le\exp\{B_k|\mathbb T^{(k)}|+C_D|D|\},\qquad
 B_k\le C_B(1+\log x_k).                        \tag{8}
\]

The $1/4$ reserve, the arbitrary stopping level, and designated healed
lineages are all part of this input. The separate source statements
about terminal marks and healed masses do not by themselves establish (8).

**1.4. Two-run interface (QL′).** The needed local comparison is stated
precisely here to separate it from its unresolved construction details.
Choose fixed geometric constants $b_1,w=b_1+3,R_*=14+b_1,m_0$, a
background rate $\delta>0$, and a sufficiently large odd power $n$
of $L$. A tile has side $nc_k$; its core has side $3nc_k/4$.
Complete its bare field by the identity and its exterior uniforms by
$1/2$, and run the same construction. This is the *local run*.

For $i\le k$ put $Q=2L^{13}$, $V_T=n^4(MR_k)^4$, and

\[
 \begin{split}
 v_k&=\delta nMR_k/512,\\
 K_i&=N_\tau n^4(MR_k)^4L^{4(k-i)}(C_R+1)^4(MR_i)^4
                                       L^{8(R_i+2)},\\
 \epsilon_i&=e^{-v_k}Q^{-(k-i)}/(2K_i),\\
 D_i&={2\over\delta}
       [v_k+(k-i)\log Q+\log(16C_qK_i^2/\kappa_T)],\quad
       \kappa_T=1/4.                            \tag{9}
 \end{split}
\]

$N_\tau,C_q\ge1$ bound the schedule and normalized test comparisons.
Let $s_*=4R_*+20$, $H=(8R_*+43)^4$,
$e_*=8H(2w+1)+1$. Increase the fixed erosion constant $m_0$ to
accommodate $e_*$. The interface consists of the following assertions.

* The tile has nested comparison regions with total removed width at
  most $c_1+\sum_{i\le k}(m_0c_i+2D_ia_i)\le nc_k/8$.
* At level $i$, a window event $W_i$ is the union, over at most
  $K_i$ **visited** background-dependent tests of the local run, of
  $|u_\tau-p_\tau|\le\epsilon_i$. There are two other local events
  $O_i,Z_i$. Until the first occurrence of $W_i\cup O_i\cup Z_i$,
  the two runs have the same regions, current and stored block fields,
  recorded decisions and component histories in the surviving interior.
  Equality of background-relative fluctuation fields is not asserted.
* At a first $O_i$, or a first $Z_i$ with $W_i,O_i$ excluded,
  the true run has, inside the tile, a $w$-path of at least
  \[
  N_i=\left\lceil{D_i/(2MR_i)+e_*-1\over2w+1}\right\rceil       \tag{10}
  \]
  distinct cells. Each is within $R_*$ cells of a live cell at $i$
  or the hull of one at $i-1$, or contains a deep trigger as defined
  below. The path and its designation neighbourhoods are inside the
  tile. They can be chosen away from other tiles' designation
  neighbourhoods. The agreement also identifies survival of any
  cell deep in the tile up to the preceding level.

The advertised owners are **(RS), LF1(2)**, finite local read sets and
the list of background-dependent tests; and **(BGL), BG1(1)**, exponential
comparison of backgrounds with common data on the constructed collared
regions. Rounding/boxing and **(R3)** are also needed.
The initial determining domain must be the collared first region
$\Omega_0=\Omega_1^\sim$, with the construction's local admission
conditions. A regularity requirement on the entire bare torus is
incompatible with this interface; SA 23265 explains that obstruction.

**Outstanding — deriving this interface from (RS) and (BGL).** R2's
two-run induction uses a comparison region intersected with the original
domain $\Omega_0$. The quoted background theorem requires its collars
to lie in single layers and does not automatically establish that the
new inner boundaries have this property. One needs that version of BGL,
with its gauges and domains. All later tests which read stored
background-relative values also need their actual threshold-normalized
Lipschitz bounds; a lower bound comparable to $\delta$ cannot be
silently used for a sharper stage threshold. Equations (9)–(10) specify
what must be obtained. Theorem 12 assumes this interface; it does not
claim that the source sketch or the present reading proves it.

**1.5. Conditional analytic law (CL), owners NL1 and LF1.** At step
$i$, let $I$ be the free bonds in $\Lambda_i^{\rm pre}$, excluding
the pivot bonds of the linearized constraint. Write $Y\in(\mathbb R^3)^I$
and let $R$ denote the retained variables (distinct from the radius
$R_j$). For almost every retained datum under each positive history
weight, require the exact conditional law

\[
 \nu_R(dy)=Z_R^{-1}{\bf1}_{\mathcal W}(y)e^{-H(y)}dy,
 \quad H(y)=\tfrac12 yAy+F\cdot y-P(y),\quad
 \mathcal W=\prod_{b\in I}K_b.                  \tag{11}
\]

Set $\ell=\log\theta_{i-1}$, $\mathfrak b=A_1\ell^{p_0}$,
$r_{\rm in}=\theta_c\mathfrak b/c_N$, $r_{\rm out}=5c_N\mathfrak b/4$.
Every $K_b$ is bounded, convex, centrally symmetric, and contains the
Euclidean ball of radius $r_{\rm in}$, while lying in the ball of
radius $r_{\rm out}$. The windows test free bonds only. Require

\[
 \begin{gathered}
 A=A^*,\quad A\ge a_-I>0,\quad
 \|A(b,b')\|\le a_+e^{-c_A d(b,b')},\\
 |F_b|\le C_h\mathfrak b e^{-c_h d(b,\Lambda_i^{\rm pre,c})},\qquad
 \|-A^{-1}F\|_\infty\le r_{\rm in}/8,\\
 |\nabla_bP|\le p_1,\quad
 \|\nabla^2P\|_{2\to2}\le p_2\le a_-/4.         \tag{12}
 \end{gathered}
\]

$P$ is real and $C^2$ near the closed window. All constants are
independent of history, volume and level. The physical readout is

\[
 \mathcal A_{i-1}(b')=g_{i-1}\{\ell_{b'}Y+\rho_{b'}(Y)\},
 \quad \|\rho_{b'}\|_B\le C_\rho g_{i-1}r_{\rm out}^2.           \tag{13}
\]

Each row $\ell_{b'}$ has at most $J$ free-bond blocks in a fixed
range, and operator norm at most $C_2$. Thus its sup-to-Euclidean norm
is at most $C_\infty=\sqrt J C_2$; these two norms must not be identified.
Separated deep cells below have disjoint readout supports.

**(CL0), exact elimination, LF1/NL1.** Under each fixed positive history
weight, the state $S_i$ after step $i$ is a function of its retained
datum $R_i$, and $(Y_i,R_i)$ is obtained from $S_{i-1}$. Conditional
integration of $Y_i$ given $R_i$ is exactly (11), including every
factor of that history. Later trigger indicators are functions of
$S_i$. These assertions allow successive conditional integration with
any nonnegative multiplier depending on $S_i$.

**Outstanding — identification of (11).** Product windows and a
Gaussian extraction do not identify the full fixed-history density.
In particular the healed-family sum used in Lemma 3 below is an
exterior-conditioned sum, whereas CL0 fixes a history. Its replacement
by a logarithm must be compatible with precisely the sigma-algebra in
CL0, or the remaining individual factors must be treated separately.
Neither positivity alone nor the clean-box theorem of CA supplies this
identification for arbitrary histories. Pivot-bond nonlinear tests
cannot be added to (11) without a new convex-window argument.

**1.6. Analytic input (L), owner NL1.** The part $P$ of the exponent
has, up to a constant, the following form for a finite family $\mathcal F$:
$\sum_{f\in\mathcal F}[F_f(\mathbf1,y)-f_0]$.
The seven kinds of $f$ are Wilson/Jacobian/profile remainders, strip
terms, constraint-normalization terms, regular $E,R$ terms, boundary
terms, kept quadratic forms, and standing-island exponents. Each has a
connected read hull $X_f$ of $M$-cubes. With switches fixed to one on
$X_f$, $F_f(s,z)$ is holomorphic for $|s_\Delta|<e^{\bar\kappa}$
elsewhere and $|z|_\infty<R_f$, where $R_f\ge R_{\rm an}=\ell^q$.
Here $|z|_\infty$ is the maximum complex Euclidean block norm;
$\mathcal T_\rho$ is the union of such open block balls of radius
$\rho$ about points of the real window.
It is real on real arguments, and $F_f(s,0)=f_0\in\mathbb R$
independently of $s$. Its value reads only the connected component of
$X_f\cup\operatorname{supp}s$ containing $X_f$. This locality includes
the pair map and stored transports, not just a formal support label.
Require either $|F_f|\le\omega_f/2$, or
$\Re F_f\le f_0+\omega_f$, throughout the domain.

Write $d_c$ for cube distance and define

\[
 N^\natural(\ell)=\sup_{\Delta\text{ meeting }I}
 \sum_f\omega_f{R_{\rm an}\over R_f}
 \exp\{\kappa_P\operatorname{diam}_cX_f
                   -\tfrac12\bar\kappa d_c(\Delta,X_f)\}.       \tag{14}
\]

The ordinary size inputs **(L-W),(L-S),(L-Z),(L-reg)** require
$\sup_\Delta\sum_{f:X_f\ni\Delta}\omega_fe^{\kappa|X_f|}
\le C_0^{\rm loc}+C_W^{\rm loc}e^{-\ell/2}\ell^{3q+r}$.
Here the fixed local multiplicities, including the Wilson plaquette
count, are included in the constants. **(L-B),(N-B)** require
$\omega_f\le2\mathsf B e^{-\kappa d_f^\natural}$ and
$\sup_\Delta\sum_{f:X_f\ni\Delta}e^{-\kappa d_f^\natural/2}
\le C_B^{\rm ent}\ell^{\tau_B}$, with fixed $\tau_B\ge0$.
Their read hull is a connected contracted tree of ordinary cubes
$T_f$ and exempt island hulls, with
$|T_f|\le C_{\rm tr}(d_f^\natural+1)$.
This specifies the conversion from tree length to cube count, including
its fixed geometric constant; the two numbers are not set equal.

The geometry inputs require each island hull to have diameter at most
$C_0^{\rm isl}LR_i+2$, distinct hulls to be at distance at least
$R_i$, and their distance from a cube meeting $I$ to be at least
$10LR_i-2$. For sufficiently small fixed $\kappa_P>0$ and large
$\bar\kappa$, Lemma 2 also proves that the ordinary and boundary
contributions to (14) are at most

\[
 C_{\rm ord}\ell^{\tau_B}
                 +C_W e^{-\ell/2}\ell^{3q+r}.                 \tag{15}
\]

This includes a count of boundary slots and the exempt-island geometry;
an exponential bound in exempt tree length alone is insufficient.
**(G-gap),(G-isl),(G-sep),(S),(sep)** name the domain/gap, island-size,
separation, response and layer-separation inputs in PAN §4. Their
required analytic consequences are (L), the bounds just stated, and the
screened-radius input and old-object sum specified in §3 below. No additional spatial
decay through an exempt island is presumed.

## 2. Lineage volume and the marked bound

**Lemma 1 (volume paid by events; MB).** Under (R0)–(R2), set

\[
 C_1={6A\over5}C_N[1+\log(2+12AC_N)],\qquad
 C_G={60\over47}(4A+C_1).
\]

Every lineage satisfies

\[
 \sum_{(j,C)}r_j|C|_j\le C_G\sum_{(j,C)}r_j(R_j+1)e(j,C).       \tag{16}
\]

If $4c_aC_Gr_j(R_j+1)\le p_j/4$ at every level, (LT) implies,
for designated cells $z_t$ surviving over intervals $[n_t,q_t]\subset[1,k]$,

\[
 \mathbb P^{(k)}\Bigl(\bigcap_tE_{z_t}^{(n_t)}(q_t)\Bigr)
 \le\exp\{B_k|\mathbb T^{(k)}|+C_Dm
                  -2c_a\sum_t\sum_{j=n_t}^{q_t}r_j\}.          \tag{MB}
\]

Here the designated ancestor cells must be distinct at each paid level.

*Proof.* A free node has one predecessor. Along a free chain starting
above $P$, iterate (R1) and sum the geometric series. Its volume is
at most

\[
 v(P)/5+(6A/5)C_Nr_s[R_s+\log(2+|P|)]
 \le 3v(P)/10+C_1r_{j(P)}(R_{j(P)}+1).
\]

The second inequality uses $r_s\le r_{j(P)}$, $R_s\le R_{j(P)}$
and $\log(2+y)\le\varepsilon y+\log(2+1/\varepsilon)$ with
$\varepsilon=(12AC_N)^{-1}$. Every chain starts above an event node,
and no node starts two chains. At event nodes, (R1) gives
$v\le\lambda\sum_{{\rm pred}}v+3Are$. If $V$ is total volume,
then
$V\le(13/10)\lambda V+(39A/10+C_1)\sum r(R+1)e$, proving (16).

Order the children at each merger. Charge each non-first child to the
leftmost leaf below it. These leaves are distinct: a leftmost path can
first become a non-first child only once before it ceases to be the
leftmost path. Weights $r_j(R_j+1)$ decrease along the tree, and every
leaf has a creation. Thus merger costs are bounded by one extra copy
of creation costs. Acted predecessors are charged at their own level.
Consequently $2c_a\sum r_j|C|_j\le{\rm EC}(l)/4$.

Every designated surviving cell is counted by a terminal or a designated
healed lineage, once at each paid level. Distinctness prevents charging
one cell twice. Apply Markov's inequality and (8) to obtain (MB).
The coupling floor exists since $p_0>6r$, (3), and
$R_j\le L(\log x_j)^r$; comparisons with the stopping coupling use
$x_j\ge x_k-2c_2$. ∎

The numerical derivation of (R1) in R2 is not imported. Its one-pass
boxing estimate does not account for newly merged components in
iterated boxing. A safe elementary bound is
$\operatorname{bx}(B)\subset B^{+b_1}$: each newly filled small box
belongs to a component containing an original cell of $B$. This gives
$|\operatorname{bx}(B)|\le(2b_1+1)^4|B|$, with a larger contraction
constant and a correspondingly larger floor on $L$, if $b_1$ is
fixed before that floor. (R1), including its parameter order, remains
the stated LF1 input.

## 3. The analytic input and its remaining size obligation

**Lemma 2 (size summation, localization, and Cauchy estimates).** Assume
(L), $r_*\le R_{\rm an}/2$, and $\bar\kappa\ge\max\{2,4\kappa_P\}$.
For (15), also assume the size and geometry inputs of §1.6, with
the rate choices made in its proof below.
On the block polydisc $|z|_\infty<r_*$, the recentered sum has a
finite local decomposition $P=\sum_XP_X$ with

\[
 \sum_{X\ni b,b'}\sup|P_X|
 \le 4e^{\bar\kappa}{4r_*\over R_{\rm an}}
        N^\natural(\ell)e^{-\kappa_Pd_c(\Delta_b,\Delta_{b'})}.
                                                               \tag{17}
\]

If the right side is at most
$C_\pi e^{-c_P d(b,b')}$ on a tube of block radius $\rho$
about the real window, then (12)'s derivative bounds hold with

\[
 p_1={\sqrt3 C_\pi\over\rho},\qquad
 p_2={12C_\pi S_d(c_P)\over\rho^2},\quad
 S_d(c)=\sup_b\sum_{b'}e^{-cd(b,b')}.             \tag{18}
\]

*Proof.* First verify (15). For ordinary terms use
$\operatorname{diam}_cX_f\le|X_f|-1$ and
$e^{-t d_c(\Delta,X_f)}\le\sum_{x\in X_f}e^{-t d_c(\Delta,x)}$.
Exchanging the sums bounds their contribution by a fixed lattice Schur
sum times the stated local norm.

For a boundary hull, a simple path meets at most
$1+|T_f|/(R_i-1)$ exempt hulls. Its length is at most
$A_g|T_f|+C_0^{\rm isl}LR_i+4$, for a fixed
$A_g=4+2C_0^{\rm isl}L$ and $R_i\ge3$.
If there is an exempt hull, start at a point of $X_f$ closest to
$\Delta$ and stop at the **first** hull along a path to one.
Before that first hull the path uses only ordinary tree cubes.
The gap therefore gives
$10LR_i-2\le d_c(\Delta,X_f)+|T_f|+2$.
Combining these inequalities, and treating a hull with no exempt
object directly, gives
$\operatorname{diam}_cX_f\le c_g(d_f^\natural+1)
 +(C_0^{\rm isl}/10)d_c(\Delta,X_f)$ for a fixed $c_g$.
Choose $\kappa_P\le\kappa/(2c_g)$ and
$\bar\kappa\ge4\kappa_PC_0^{\rm isl}$. Multiplying by the size
$2\mathsf B e^{-\kappa d_f^\natural}$ leaves at most a fixed constant
times $e^{-\kappa d_f^\natural/2}
e^{-(\bar\kappa/4)d_c(\Delta,X_f)}$.
Convolution with (N-B) proves (15). This repairs the use of an
arbitrary, possibly far, exempt hull in PAN's gap argument.

On a radial complex disc, let
$\phi=F_f(s,z)-f_0$. In the one-sided case
$\phi/(2\omega_f-\phi)$ maps the disc to the unit disc and vanishes
at its centre. Schwarz's lemma gives
$|\phi|\le2\omega_ft/(1-t)\le4t\omega_f$,
$t=|z|_\infty/R_f\le1/2$. If $\omega_f=0$, the real-part maximum
principle gives $\phi=0$. In the two-sided case, apply Schwarz to
the difference from its centre, bounded by $\omega_f$.

Let $N_j(X_f)$ be the $j$-cube neighbourhood. Telescope the switches:
$g_{-1}=F_f(1_{X_f},z)-f_0$ and
$g_j=F_f(1_{N_{j+1}},z)-F_f(1_{N_j},z)$, $j\ge0$, stopping when
the neighbourhood fills the torus. Locality assigns $g_j$ to
$N_{j+1}$. With one common switch variable in each separating shell,
the difference vanishes when any of the $j$ inner shell variables
is zero. Iterated Schwarz on their discs of radius $e^{\bar\kappa}$
therefore gives

\[
 |g_{-1}|\le o_f,\quad |g_j|\le2o_fe^{-\bar\kappa j},\qquad
 o_f={4r_*\over R_{\rm an}}\omega_f{R_{\rm an}\over R_f}.
\]

Terms whose support contains no free bond vanish. If
$m=\max\{d_c(\Delta_b,X_f),d_c(\Delta_{b'},X_f)\}$, only shells
with $j+1\ge m$ can contain both bonds. Their sum is bounded by
$4e^{\bar\kappa}o_fe^{-\bar\kappa m}$. The triangle inequality
$d_c(\Delta_b,\Delta_{b'})\le2m+\operatorname{diam}_cX_f$, and
$\bar\kappa\ge4\kappa_P$, give (17) after summing over $f$.

For (18), apply Cauchy on coordinate discs in the block tube. First
derivatives cost $1/\rho$. Second derivatives cost at most
$4/\rho^2$, using half-radius discs for two coordinates of the same
block; the block operator norm costs a further factor three. The Schur
bound over bonds gives (18). The larger constant avoids identifying a
Euclidean block ball with a coordinate polydisc. ∎

**Lemma 3 (healed-region bound, including (d)).** Assume **(H-Mayer)**:
after summing the healed internal histories at fixed exterior datum
$e$, the remaining factor is a hard-core polymer partition function
$\Xi(e)$, with
$z_\gamma(e)=\int u_\gamma(\xi,e)\,\mu_\gamma(d\xi)$.
The integrands are Borel in $\xi$, holomorphic in $e$, real on
real arguments, and have integrable Borel majorants on the common
complex exterior domain. Assume **(KP-h)**: uniformly on this domain,
$|z_\gamma|\le\widehat z_\gamma$ and

\[
 \sum_{\eta\not\sim\gamma}\widehat z_\eta e^{a(\eta)}\le a(\gamma),
 \quad \sum_{\gamma\ni\Delta}\widehat z_\gamma e^{a(\gamma)}<\infty.
                                                               \tag{19}
\]

Then (a) the activities are holomorphic; (b) $\Xi\ne0$, with a
holomorphic logarithm given by its connected series; (c) the terms
grouped by union of read supports $Y$ obey
$\sum_{Y\ni\Delta}\sup|R'_\sharp(Y)|\le
\sum_{\gamma\ni\Delta}\widehat z_\gamma e^{a(\gamma)}$;
(d) the healed contributions are two-sided bounded holomorphic
exterior activities. No separate logarithm of an individual healed
factor is needed in this resummed representation.

*Proof.* Dominated integration of a Cauchy formula proves (a). The
hard-core connected-series theorem, including its tree inequality,
is the analytic input proved in SA 1270–1347. Its rooted estimate can
be seen by iterating
$T_\gamma^{(0)}=1$,
$T_\gamma^{(h+1)}=\exp\sum_{\eta\not\sim\gamma}
\widehat z_\eta T_\eta^{(h)}\le e^{a(\gamma)}$.
The tree inequality bounds the absolute connected root series by its
limit. Rooting a cluster at any polymer containing $\Delta$ gives
(c). The bounds imply normal convergence. The formal identity
$e^{\log\Xi}=\Xi$, initially near zero activity, extends by scaling
all activities by $t$, $|t|<1$, and then by continuity to $t=1$.
This proves (b) without selecting an arbitrary branch on an arbitrary
domain. The series is real at real data. Grouping it by actual read
supports proves (d); carrying these terms to a later step still requires
the pair-map locality and admission in (L). ∎

The owners are LF1 for the healed-history representation and mass
reserve, and NL1/IN1 for its common complex domain and integrable
majorants. SA 17648–17653 and 17959–17997 place the resulting terms
in regular or boundary columns. They do not prove compatibility with
CL0's fixed history. The two assertions must be checked together.

**Lemma 4 (island centre and the capped radius).** Assume **(L-I)**
and **(Q)**, with the latter required at every real centre being used:
an island formed at $m$ has

\[
 \Psi_0=-q_X/2+V,\quad |V|\le C_VV^\circ,\quad
 \Re\Psi\le C_\Psi V^\circ,\quad
 q_X\le C_QR_m^4N_Xp_m^2+2,\quad
 V^\circ\le N_X\le C_{\rm cls}M^4R_m^5.
\]

Then its one-sided oscillation size is

\[
 \omega_X=C_\Psi V^\circ-\Psi_0
      \le C_I(\log\theta_m)^{\tau_I},\qquad \tau_I=2p_0+9r.    \tag{20}
\]

If a single integrated positive factor $M_X(p)=\int e^{\Phi(\xi,p)}d\mu$
were retained, assume $\mu$ is positive, $\Phi(\xi,p_*)$ is real,
$0<M_X(p_*)<\infty$, and $\Phi-\Psi$ is independent of $p$.
Require that $\Psi(\xi,\cdot)$ is holomorphic on the pair polydisc
of radius $R_X$ about $p_*$, with the stated one-sided bound there,
and that $\Gamma_X=\sup_\xi(C_\Psi V^\circ-\Psi(\xi,p_*))<\infty$.
Then $M_X$ is
zero-free on the pair polydisc of radius
$R_X/(8\Gamma_X+2)$, and its logarithmic ratio to its centre has
absolute value at most $1/2$.

For live-attached objects the permitted screening input is **NL1
Proposition S**, with its (V1)–(V6), source/chart/levelling ceilings,
and the definitions in `nl1-L-draft.md` §6.2. In its notation,

\[
 R_f^{\rm scr}=\min\{R_{\rm an}e^{\mu D_f/4},R_{\rm cap}\},\quad
 R_{\rm cap}={c_{\rm cap}\over c_T^{\rm src}C_Ae^{\bar\kappa}g},
 \quad {R_{\rm an}\over R_f^{\rm scr}}
 \le e^{-\mu D_f/4}+{c_T^{\rm src}C_Ae^{\bar\kappa}g\ell^q\over c_{\rm cap}}.
                                                               \tag{21}
\]

$c_T^{\rm src}$ is a source-map constant, not the trigger-tail
constant. All constants in the positive cap are fixed before the
coupling ceiling; equivalently that part of the input supplies a fixed
$c_*>0$ with $R_{\rm cap}=c_*/g$. For
$D_f\ge10LMR_i-C'$, the right side is at most

\[
 \varepsilon_{\rm scr}(\ell)=e^{\mu C'/4}e^{-(5/2)\mu LMR_i}
                                                +g\ell^q/c_* . \tag{22}
\]

*Proof.* Substitute the lower bound for the real centre into
$C_\Psi V^\circ-\Psi_0$, and use $R_m\le C(\log\theta_m)^r$.
The largest power is $2p_0+9r$, proving (20). Lemma 2 on the pair
disc gives an exponent difference at most
$2\Gamma_X/(8\Gamma_X+1)\le1/4$. Normalize the positive integrand
at $p_*$ to a probability measure. The ratio $M_X(p)/M_X(p_*)$
is its expectation of $e^{\Delta\Psi}$. The integrable centre density
times $e^{1/4}$ dominates the continued integrand, so Cauchy integration
also proves its holomorphy on the smaller disc. The ratio lies within
$e^{1/4}-1\le1/3$ of one. Its logarithm is holomorphic and has size
at most $\sum_{n\ge1}(1/3)^n\le1/2$. The inequality
$e^{1/4}\le(1-1/4)^{-1}$ follows termwise from the exponential
series; no numerical evaluation is needed. Finally (21) is the
reciprocal of a minimum, bounded by the sum of the reciprocals. The
stated lower bound on $D_f$ gives (22). ∎

Proposition S's admission conclusion is used with (L) and its same
size bound on the capped radius. The source/chart ceiling must ensure
$R_f^{\rm scr}\ge R_{\rm an}$; a radius formula alone is not a
holomorphy or size theorem.

The quadratic bound (Q) is an owner input, not inferred from a one-sided
bound on $\Psi$. PAN's real-pair calculation also uses **(BX)**,
BG1's plaquette estimate, and LF1's real cancellation remainder. In
its last-window estimate, $R_j\le R_m$ must be replaced by
$R_j\le LR_m$ for sufficiently large inverse couplings, using (3) over the
$O(R_m)$ levels. This enlarges $C_Q$ by a fixed power of $L$;
it does not change $\tau_I$. Extension to all other real centres
remains precisely (Q).

**Outstanding — old-object summation after capping.** Equations
(20)–(22) do **not** give PAN Lemmas 7.5–7.6. The cap removes their
factor $(\ell/\ell_m)^q$. They leave
$\varepsilon_{\rm scr}(\ell)\ell_m^{2p_0}$ for a kept form and
$\varepsilon_{\rm scr}(\ell)\ell_m^{\tau_I}$ for an island, with
$\ell_m=\log\theta_m$ potentially unbounded at fixed current
$\ell$. Superpolynomial decay in current $\ell$ cannot alone
bound that supremum. This is a failure of the claimed inference, not
a counterexample to rarity. NL1's sentence following Proposition S
does not supply the missing formation-level estimate.

The kept-form size input **(L-K)** is
$\omega_f\le2C_Kp_m^2e^{-\kappa d_f^\natural}$, with the analogue
of (N-B) for its slots. This controls formation-level size, not current
size. Partition all terms between (15) and the live-attached sum below;
the latter includes carried constraint factors whenever they do not
satisfy the ordinary local norm.

For a precise conditional version of Theorem P, name the added
obligation **(OS)**: the contributions of kept forms and islands to
(14), using their capped radii, satisfy uniformly over histories

\[
 N_{K,I}^{\natural}(\ell)\le
 [C_K\ell^{2p_0+\tau_B}+C_I'\ell^{\tau_I}]
                                      \varepsilon_{\rm scr}(\ell). \tag{23}
\]

This is an additional analytic summation input. A proof could use an
oscillation estimate in the target pair variable retaining the layer
loss, rather than enlarging the source disc beyond its cap. No such
estimate is asserted here as a consequence of (21).

**Theorem 5 (conditional P-an, with corrected $\ell_3$).** Assume
(L), (15), the actual-density identification of §1.5, the hypotheses
of Lemmas 3–4 for the terms to which they apply, and (OS). Let
$\sigma=\tau_B+1$, $q_1=q-\sigma>p_0$, and
$\rho=\ell^{q_1}/8$. Require also $q\ge\tau_I$.
Then above a level-independent inverse-coupling floor, $P=\sum_XP_X$ on
the tube of radius $\rho$ about the window, with

\[
 \sum_{X\ni b,b'}\sup_{\mathcal T_\rho}|P_X|
       \le e^{-\kappa_P d_c(\Delta_b,\Delta_{b'})}
       \le e^{\kappa_P}e^{-(\kappa_P/M)d(b,b')}.                \tag{P-an}
\]

The last metric comparison is required in the chosen cube/bond
convention; changing representatives merely enlarges its fixed prefactor.

*Proof.* Choose $\ell_1,\ell_2$ so that
$r_{\rm out}+\rho\le R_{\rm an}/4$ and
$4(r_{\rm out}+\rho)/R_{\rm an}\le\ell^{-\sigma}$ for every
$\ell\ge\max(\ell_1,\ell_2)$. These choices are possible because
$q-p_0>\sigma$. **Redefine $\ell_3>C_*+1$** to be any value such that
for every $u\ge\ell_3$,

\[
 C_We^{-u/2}u^{3q+r}
 +[C_Ku^{2p_0+\tau_B}+C_I'u^{\tau_I}]
   \left[e^{\mu C'/4}e^{-(5/2)\mu LM(u-C_*)^r}
                         +c_*^{-1}e^{-u/2}u^q\right]\le2.     \tag{24}
\]

Here $C_*$ is a fixed frame comparison constant such that
$R_i\ge(\ell-C_*)^r$ for large $\ell$. It follows from the
running minimum and (3), also comparing adjacent frames. Both terms
inside brackets tend to zero faster than every power, so (24) has a
finite solution **under (23)**. With
$C_N^{\rm an}=C_{\rm ord}+2$, (14) is at most
$C_N^{\rm an}\ell^{\tau_B}$. For
$\ell\ge4e^{\bar\kappa}C_N^{\rm an}$, Lemma 2 proves (P-an).
For instance take
$X_P=(5/4)\exp\max\{\ell_1,\ell_2,\ell_3,4e^{\bar\kappa}C_N^{\rm an}\}$,
and use $\theta_{i-1}\ge4x_{i-1}/5$. ∎

Without (OS), replace the second term in (24) by the actual supremum
of $N_{K,I}^{\natural}$ over histories at $u$. Finiteness of such
an $\ell_3$ is **Outstanding**. The theorem must not be read as
proving it from the uncorrected PAN input list.

## 4. Concentration and trigger tails

**Lemma 6 (linear concentration on a convex window).** Let
$d\nu=Z^{-1}1_W e^{-H}dy$, where $W$ is bounded and convex with
nonempty interior, $H$ is $C^2$ near its closure, and
$\nabla^2H\ge\lambda I>0$. Then for every real linear functional $v$,

\[
 \nu\exp[t\langle v,Y-\nu Y\rangle]
       \le \exp[t^2|v|^2/(2\lambda)].            \tag{25}
\]

*Proof.* The integration fact needed here has a direct proof. If
$h((1-t)x+ty)\ge f(x)^{1-t}g(y)^t$ on the line, normalize $f,g$
to masses $F,G$, and use their increasing quantile transport $T$.
Almost everywhere $T'=fG/(Fg(T))$, and
$(1-t)+tT'\ge(T')^t$. Change variables by $(1-t)x+tT(x)$
and integrate to get $\int h\ge F^{1-t}G^t$. Exhaust the interiors
of the interval supports to include their boundaries. Applying this
one coordinate at a time proves the same assertion in higher dimension
and proves that an integral of a jointly log-concave function is
log-concave. This is the transport argument in SA 27149–27212.

Rotate a unit vector $v$ to the first axis and write $Y=(u,z)$.
The marginal of $u$ is proportional to
$e^{-\lambda u^2/2}\int 1_W e^{-H+\lambda u^2/2}dz$.
The integrand is log-concave, since its potential is
$H-\lambda|Y|^2/2+\lambda|z|^2/2$. The integration fact shows that
the marginal has potential $\psi$ with $\psi''\ge\lambda$.
If its mean is $m$, integration by parts on its support interval
gives

\[
 \lambda\operatorname{Var}(u)
 \le\nu[(u-m)(\psi'(u)-\psi'(m))]
 =1-[(u-m)e^{-\psi(u)}]_{\rm left}^{\rm right}/Z\le1.
\]

Both endpoint contributions have the indicated nonnegative sign.
Convex nonsmooth potentials follow by convex smoothing on compact
subintervals and exhaustion; the bounded-window moments converge.
The same argument applies after adding any linear tilt. Thus the
second derivative of the log moment-generating function is at most
$1/\lambda$; integrate twice from zero, and rescale $v$, to obtain
(25). ∎

**Lemma 7 (the mean stays inside the window).** Under (11)–(12), put
$\lambda=3a_-/4$. There are constants $\mu,K_\infty,C_m>0$,
depending only on the displayed operator and force constants, such that

\[
 \|A^{-1}(b,b')\|\le(2/a_-)e^{-\mu d(b,b')},\quad
 \sup_b\sum_{b'}\|A^{-1}(b,b')\|\le K_\infty,
 \quad |(-A^{-1}F)_b|\le C_m\mathfrak b e^{-\mu' d(b,\Lambda^{\rm pre,c})},
                                                               \tag{26}
\]

with $\mu'=\min(\mu,c_h)/2$. Set
$G=a_+S_d(c_A)r_{\rm out}+C_h\mathfrak b+p_1$ and

\[
 \varepsilon_W=6(G+16/r_{\rm in})e^{-\lambda r_{\rm in}^2/24}.
\]

If $K_\infty(p_1+\varepsilon_W)\le r_{\rm in}/16$, then

\[
 |\nu Y_b-(-A^{-1}F)_b|\le K_\infty(p_1+\varepsilon_W),
 \qquad |\nu Y|_\infty\le3r_{\rm in}/16.        \tag{27}
\]

*Proof.* Conjugate $A$ by the diagonal weight
$e^{\mu d(b,b_0)}$. The Schur norm of its difference from $A$
is at most
$a_+\sup_b\sum_{b'}e^{-c_A d}(e^{\mu d}-1)$, which tends to
zero uniformly as $\mu\downarrow0$. Choose it at most $a_-/2$.
The inverse of the conjugated operator has norm at most $2/a_-$,
giving (26) entrywise and then in row sum. Convolution with the force
bound, using the triangle inequality for distance to the boundary,
gives its last assertion. These are finite-matrix arguments with
volume-independent Schur sums.

For a block $b$, take a smooth cutoff $\chi_b$ equal to one on
$|y_b|\le3r_{\rm in}/4$, zero for $|y_b|\ge7r_{\rm in}/8$,
and with gradient at most $16/r_{\rm in}$. Integration by parts
has no boundary term, because this ball lies inside $K_b$. It gives

\[
 \nu\nabla_bH=\nu[(1-\chi_b)\nabla_bH+\nabla_b\chi_b].
\]

If $|\nu Y_b|\le r_{\rm in}/4$, (25) in the six coordinate
directions bounds the probability of $|Y_b|\ge3r_{\rm in}/4$
by $6e^{-\lambda r_{\rm in}^2/24}$. Since
$|\nabla_bH|\le G$, this proves $|\nu\nabla_bH|\le\varepsilon_W$.
The identity $A\nu Y+F=\nu\nabla H+\nu\nabla P$ proves (27)
provided the preliminary mean bound holds.

To remove that proviso, use $F_s=sF$ and
$P_s(y)=\tfrac{1+s}{2}P(y)+\tfrac{1-s}{2}P(-y)$, $0\le s\le1$.
The Hessian, force and derivative bounds hold uniformly. At $s=0$
the density and window are even, so the mean is zero. As long as the
mean is within $r_{\rm in}/4$, the preceding argument improves the
bound to $r_{\rm in}/8+r_{\rm in}/16$. Means depend continuously
on $s$ on the bounded finite-dimensional window. A first-exit
argument therefore prevents exit for all $s\le1$. ∎

**Theorem 8 (TT from CL).** A *deep trigger* at a bond $b'$ of
level $i-1$ is the event

\[
 b'\in\Lambda_i^{\rm pre},\quad
 \mathfrak d_i(b')^{+2}\cap Z_i^{\rm pre}=\varnothing,\quad
 \|\mathcal A_{i-1}(b')\|_B>\theta_{\rm col}\delta_{i-1}.       \tag{28}
\]

Assume (CL0), (11)–(13), and
$K_\infty(p_1+\varepsilon_W)\le r_{\rm in}/16$ as in Lemma 7.
At each level the designated trigger cells have
disjoint two-cell enlargements and disjoint readout supports. Let
$d_*$ be the smallest depth of any free bond read by such a trigger;
require $d_*\ge LMR_i$, after subtracting the fixed readout range.
Set $t=\theta_{\rm col}\mathfrak b/(2c_N)$, and impose the coupling ceilings

\[
 \begin{split}
 C_\rho g_{i-1}r_{\rm out}^2&\le\theta_{\rm col}\mathfrak b/2,\\
 C_\infty[C_m\mathfrak b e^{-\mu'd_*}+K_\infty(p_1+\varepsilon_W)]
                                    &\le t/(2\sqrt3),\\
 p_{i-1}&\ge p_i/2 .                            \tag{29}
 \end{split}
\]

For any collection $\mathcal B$ of such designated bonds, and every
fixed positive history weight,

\[
 t(dh;\ \bigcap_{b'\in\mathcal B}{\rm Trig}_{i(b')}(b'))
 \le t(dh)\prod_{b'\in\mathcal B}6e^{-c_Tp_{i(b')}^2},\qquad
 c_T={\lambda\theta_{\rm col}^2(A_1/A_0)^2\over384c_N^2C_2^2}.
                                                               \tag{TT}
\]

Together with Lemma 1, this gives

\[
 \begin{split}
 &\mathbb P^{(k)}(\bigcap_tE_{z_t}^{(n_t)}(q_t)
                                      \cap\bigcap_{b'\in\mathcal B}{\rm Trig}(b'))\\
 &\quad\le\exp\{B_k|\mathbb T^{(k)}|+C_Dm
       -2c_a\sum_t\sum_{j=n_t}^{q_t}r_j
       +|\mathcal B|\log6-c_T\sum_{b'\in\mathcal B}p_{i(b')}^2\}.
                                                        \tag{MB+T}
 \end{split}
\]

*Proof.* Fix one level and its retained datum. Equations (13), (28)
and the first line of (29) imply $|\ell_{b'}Y|>t$. By (27) and
the second line of (29), $|\ell_{b'}\nu Y|\le t/(2\sqrt3)$.
Each trigger therefore gives one of six signed coordinates of
$\ell_{b'}(Y-\nu Y)$ exceeding $t/(2\sqrt3)$.
For $m$ simultaneous choices their sum is one linear functional
of squared norm at most $mC_2^2$, because the readout supports are
disjoint. Chernoff's inequality and (25) bound its probability by
$\exp[-\lambda mt^2/(24C_2^2)]$. Sum over the $6^m$ choices
and use $p_{i-1}\ge p_i/2$ to obtain the stated $c_T$.

To combine levels, eliminate $Y_1,Y_2,\ldots$ in construction
order under the fixed-history disintegration. When eliminating
$Y_i$, all later indicators are functions of $S_i$, hence of
$R_i$. The one-level estimate applies with that nonnegative
multiplier. Iteration proves (TT), with no independence assumption
between levels. Multiply by any nonnegative history-measurable
quantity and integrate in $h$; in particular the volume mark and
survival indicators in Lemma 1 give (MB+T). ∎

If Theorem 5 supplies $P$, (18) gives $p_1=O(\ell^{-q_1})$
and $p_2=O(\ell^{-2q_1})$. Thus the smallness assumptions in
Lemmas 7–8 follow by a final coupling ceiling: $q_1>p_0$,
$r_{\rm in}\asymp\ell^{p_0}$, $R_i\gtrsim\ell^r$, and
$g_{i-1}=e^{-\ell/2}$. The *global* Gaussian mean bound in (12)
still comes from the collar/rim room (4). A small Hessian alone does
not control a translated mean near a window boundary.

## 5. Local witnesses and ages

**Lemma 9 (margins, fresh windows and cluster payment).** Assume the
two-run interface of §1.4. Its numerical erosion budget is compatible
with choices of $n,M$ before the final coupling ceiling. Put

\[
 \eta_i=e^{-v_k}Q^{-(k-i)},\quad
 \chi_i=\min\{2c_ar_i-C_D,\ c_Tp_i^2-\log6\},\quad
 D_{\rm path}=(4w+3)^4,
 \quad D_{\rm des}=4(2R_*+3)^4L^4(MR_i)^4.
\]

Suppose, at all $i\le k$,

\[
 \begin{gathered}
 16B_kV_T+C_D\le c_ar_k,\quad
 c_ar_k\ge v_k+\log(2Q),\\
 \chi_i\ge c_ar_k,\quad
 \chi_i\ge8[H\log D_{\rm path}+\log D_{\rm des}],\quad
 \chi_i\ge32\delta(2w+1)HMR_i.                 \tag{30}
 \end{gathered}
\]

Then $\mathbb P(W_{\beta,i}\mid\mathcal F_{i-1})\le\eta_i$,
where $\mathcal F_{i-1}$ contains $U$ and all earlier-level
uniforms. These local-run window events are conditionally independent
in distinct tiles. If copies of an anchor $z$ at level $h$
survive to $i-1$ and a path as in (10) occurs in every tile, (MB+T)
bounds their joint probability by

\[
 \left[e^{-c_ar_k(i-h)_+}e^{-2v_k}Q^{-2(k-i)}\right]^N.         \tag{31}
\]

*Proof.* To check the budget, set $s=k-i$. From (3), for sufficiently
large $x_k$,

\[
 {R_i\over R_k}\le2^rL[1+\log(1+B_{\rm early}(s+1))]^r.
\]

$B_{\rm early}=c_f+1+2c_2$ is fixed before the final ceiling. The
sum of this bound times $L^{-s}$, denoted $C_L$, is finite.
Thus $\sum c_i/c_k\le C_L$. Choose
$n\ge64(m_0+1)C_L$. The $v_k$ part of
$\sum2D_ia_i/c_k$ is at most
$n/[128(1-L^{-1})]<n/64$. The $R_i\log L$ part of
$\log K_i$ is bounded by a constant times $C_L\log L/M$;
choose $M$ to make this contribution at most $n/64$. The remaining
logarithms and the terms proportional to $s$ have a summable
$L^{-s}$ factor and, after division by $MR_k$, tend to zero.
A coupling floor makes them at most $n/64$. These bounds leave the
required $n/8$ budget. This arithmetic does not establish the
geometric comparison assertion marked Outstanding in §1.4.

For windows, expose the within-level tests in their adapted order.
At a visited test its own uniform is fresh, giving conditional
probability at most $2\epsilon_i$. Sum over at most $K_i$
visits. This proves the bound without conditioning on all other
uniforms, which might encode the choice of the visited component.
Distinct local runs use disjoint current-level uniforms, proving the
conditional independence.

For (31), keep the first $N_i$ cells of each path and select cells
greedily with pairwise sup-separation at least $s_*=4R_*+20$.
Each selection excludes at most $H$ path cells, so the number
$N''\ge N_i/H\ge8$. If $i>h$, discard those within $R_*+3$
of the anchor's level-$i$ cell. At most one is discarded, since
the diameter of that neighbourhood is less than $s_*$. If $i\le h$
there is no earlier survival charge and no discard is needed.
At least $7N''/8$ remain. Designate for each either a live cell at
$i$, one at $i-1$, or a trigger bond. Their ancestors and trigger
read sets are distinct, including across tiles and from the paid anchor.

There are at most $n^4L^{4(k-i)}$ starting cells,
$D_{\rm path}^{N_i}$ paths, and $D_{\rm des}^{N''}$ designations.
The selection is deterministic from a path, and $N_i\le HN''$.
Using (MB+T), the entropy and these designations contribute at most

\[
 n^4L^{4(k-i)}\exp\{N''(H\log D_{\rm path}+\log D_{\rm des}
                                      -7\chi_i/8)\}
 \le n^4L^{4(k-i)}e^{-3N''\chi_i/4}
\]

per tile. The volume factor and a possible anchor cost are bounded by
$\exp[B_kV_T+C_D-2c_a\sum_{j=h}^{i-1}r_j]$.
For $i>h$, (30) leaves $e^{-c_ar_k(i-h)}$. For $i\le h$,
spend at most $N''\chi_i/8$ on this factor. In either case there
remains at least $N''\chi_i/8\ge\delta D_i$, by (10) and (30).
Finally

\[
 n^4L^{4(k-i)}e^{-\delta D_i}
 =e^{-2v_k}Q^{-2(k-i)}n^4L^{4(k-i)}
                   [\kappa_T/(16C_qK_i^2)]^2
 \le e^{-2v_k}Q^{-2(k-i)}.
\]

This proves (31). All conditions in (30) follow from one sufficiently
large coupling floor, after the fixed constants are chosen:
$B_kV_T/r_k=O((1+\log x_k)/R_k)\to0$,
$v_k/r_k\to0$, $p_i^2/r_i\to\infty$, and
$r_i/(MR_i)\to\infty$. These comparisons are uniform in $i\le k$
by (3); they do not require an upper bound on the age or the volume. ∎

**Theorem 10 (F″, survival witnesses).** Under Lemma 9, (K), (MI),
(COV), (CB) and the two-run interface, if $z$ is deep in a tile
and has level $h\le k$, then

\[
 \mathbb P^{(k)}(E_z^{(h)}(k))\le\alpha_kQ^{-(k-h)},\qquad
 \alpha_k=10e^{-v_k}.                           \tag{32}
\]

If $c_1',\ldots,c_m'$ are deep level-$k$ cells in distinct
other tiles of this same tiling, then

\[
 \mathbb P^{(k)}(E_z^{(h)}(k)\cap\bigcap_{t=1}^m
                                      \{c_t'\subset\mathcal Z_k\})
       \le\alpha_kQ^{-(k-h)}\alpha_k^m.         \tag{33}
\]

*Proof.* Let $G_{<i}$ mean that the local run has had no bad event
before $i$. Use four types of tile functions: good survival through
$k$; survival through $i-1$ and $G_{<i}\cap W_i$; survival
through $i-1$ and $G_{<i}\cap O_i$; and survival through $i-1$
and $G_{<i}\cap[Z_i\setminus(W_i\cup O_i)]$.
The first bad level, or absence of one, covers true survival by their
sum, because the two runs agree up to that level. Each function is
bounded by one and depends only on the tile data. Covariance identifies
its reflected copies with the corresponding local runs.

For good survival, (MB) on all copies and (30) give chessboard norm
at most $e^{-c_ar_k(k-h+1)}$. For windows, condition on
$\mathcal F_{i-1}$, use Lemma 9, and pay the already-surviving
anchors by (MB). The norm is at most
$\eta_i e^{-c_ar_k(i-h)_+}$. For either cluster type, (31)
gives the same upper bound. Taking roots is legitimate because
$|\mathbb T^{(k)}|=NV_T$, and the copied cells are distinct at
every paid level.

Their summed norms are at most

\[
 e^{-v_k}Q^{-(k-h)}
 \left[\tfrac12+3\sum_{s\ge0}Q^{-s}
                    +3\sum_{s\ge1}(Qe^{-c_ar_k})^s\right]
 \le10e^{-v_k}Q^{-(k-h)}.
\]

Apply (5) with all other tile functions equal to one to prove (32).
For (33), multiply the domination in distinct tiles, expand, apply
(5) to each product, and sum the products of norms. ∎

**Lemma 11 (anchors, the age sum, and small tori).** Suppose
(32)–(33) and

\[
 160n^4\alpha_k^{1/512}\le1/2.                  \tag{34}
\]

Then on tori carrying these tilings,

\[
 \mathbb P^{(k)}(\mathfrak L_k^{\ge a}(c))
       \le Cn^8e^{-v_k}L^{4a}Q^{-a},\qquad
 \sum_{a\ge0}L^{8a}\sup_c\mathbb P^{(k)}(\mathfrak L_k^{\ge a}(c))
       \le C_Fn^8e^{-v_k}.                      \tag{35}
\]

The second assertion holds also on smaller tori using (MB) and (30).

*Proof.* An age-$a$ lineage provides an anchor of level $k-a$
surviving to $k$, in the component containing $c$. A level-$k$
cell contains at most $L^{4a}$ cells of level $k-a$, since
$R_{k-a}\ge R_k$. Thus a tile contains at most $n^4L^{4a}$
anchors. For nearby anchor tiles a union bound and (32) suffice.

For a far anchor, the connected live component contains a simple
path of adjacent reference boxes from its box to that of $c$.
For a path of length $m\ge512$, consider the 16 tilings with
coordinate shifts $\pm\lfloor n/4\rfloor$ relative to a corner
of the anchor's containing level-$k$ cell. With $n\ge32$, the
anchor is deep in all of them and every level-$k$ cell is deep
in at least one. One tiling therefore serves at least $m/16$
selected live cells. Since a shifted tile meets at most 16 reference
boxes, these use at least $m/256$ tiles, of which at least
$m/512$ differ from the anchor tile.

There are at most $80^m$ paths, at most $n^{4(m+1)}$ choices
of cells, at most $2^m$ choices of the served subset, and 16
choices of tiling. Equation (33) and (34) therefore give an extra
summable $C n^4 2^{-m}$ over the anchor's factor
$\alpha_kQ^{-a}$. Summing box shells, whose counts are at most
$(2m+3)^4$, and then their anchors proves the first bound in (35).
For $a>k-1$ the event is empty. Finally
$L^{8a}L^{4a}Q^{-a}=(2L)^{-a}$, proving the age series.

If a torus is too small for a reflected tiling, its side is less
than twice the proposed tile side, so its level-$k$ volume is
less than $16V_T$, and it has at most $16n^4L^{4a}$ anchors.
Directly from (MB) and (30), each anchor costs at most
$e^{-c_ar_k(a+1)}\le e^{-v_k}Q^{-a}$.
The same geometric age sum proves (35). The case $k=0$ is empty
by definition. This is a separate argument; a chessboard root on a
nonexistent tiling is not used. ∎

## 6. Main theorem and constant order

Choose the constants in this order. Quantitative owner contracts at
each step must have this same one-sided dependence.

1. Fix the group, dimension, $r\ge2$, $p_0>6r$, the boundary
   counting degree $\tau_B$, and
   $q>\max\{p_0+\tau_B+1,\ 2p_0+9r\}$, together with the
   remaining class exponents and fixed threshold fractions. The age
   weight is fixed here to eight; no constant is required to cover
   all age weights simultaneously.
2. Choose $L$ and the early geometry/background constants
   $(M_1,R_1,b_1,C_R,\delta,m_0)$, including (R1)'s contraction.
   Use the early flow envelope in Lemma 9 to choose $n\ge32$
   as an odd power of $L$. This choice does not use a later
   coupling-dependent $B_\sharp$.
3. Choose the class decay rates $\kappa,\bar\kappa,\kappa_1$,
   $M_1',M_2$, the collar constants $\Theta_1,\varpi_T$, and
   $M$, in that order. Choose $\kappa_P>0$ small enough for
   the boundary geometry and $\bar\kappa\ge4\kappa_P$.
   Enforce the erosion floor in Lemma 9 and the owner's collar and
   separation floors. The boundary geometry/slot count in (15)
   must retain its stated degree $\tau_B$.
4. Choose the source and domain parameters, including $A_1,A_0$
   with $A_0/A_1$ sufficiently large, the hereditary radii and
   their prefactors, and the regular and boundary size constants.
   Impose (ROOM), NL1's domain-admission floors and the fixed
   positive cap $c_*$. Fix all constants in (L), (CL), (LT),
   and (OS), if that analytic route is used.
5. Choose a preliminary coupling ceiling for the owner constructions.
   Choose $c_a>0$, at least any owner floor for the fixed age
   weight eight. Only then choose an auxiliary floor $X_0$ large
   enough for (16)'s payment, Theorem 5 when used, (18),
   $K_\infty(p_1+\varepsilon_W)\le r_{\rm in}/16$,
   (29), (30), (34), the erosion estimate, all source/chart
   ceilings and $x\ge4c_2$, $\log(x/2)\ge1$. Every displayed
   asymptotic comparison is imposed for **all** $x\ge X_0$.
   Set $X_*=2X_0+4c_2$; then every earlier inverse coupling is
   at least $X_0$ whenever the stopping inverse coupling is at least
   $X_*$. This leaves room for the bounded backward drift.
   Run parameters, cutoff and volume are chosen afterwards.

These choices leave **(QL′), (CL0), (LT), (Q), (L)** and the
old-object obligation **(OS)** as hypotheses; making a coupling small
does not supply a missing identity, domain theorem or summation bound.

**Theorem 12 (AG-k1*, in the form used by TP1).** Suppose the stopped
positive run satisfies (FLOW), (K), (MI), (COV), (SM) with
$\kappa_T=1/4$, (ROOM), (R0)–(R3), (LT), (CB), and the two-run
interface (QL′) of §1.4, with its (RS)/(BGL) owners. Suppose (CL0)
and (CL), including the derivative bounds and readout in (12)–(13),
hold uniformly for that **same** history law. These analytic bounds
may either be supplied directly by NL1 with
$p_1\le C\ell^{-q_1}$ and $p_2\le C\ell^{-2q_1}$ for some fixed
$q_1>p_0$, or by Theorem 5 under all its named inputs,
**including (OS)**. Choose constants as above.
There are $C_{\rm AG},c_{\rm AG}>0$, independent of cutoff,
volume, level and cell, such that whenever $x_j\ge X_*$,

\[
 \boxed{\displaystyle
 \sum_{a\ge0}L^{8a}\,
 \mathbb P^{(j)}(\mathfrak L_j^{\ge a}(c))
       \le C_{\rm AG}\exp[-c_{\rm AG}(\log x_j)^2].}           \tag{AG-k1*}
\]

One may take $C_{\rm AG}=C_Fn^8$ after enlarging the fixed constant
for small tori, and $c_{\rm AG}=\delta nM/2048$.

*Proof.* Lemma 1 and Theorem 8 give (MB+T). Lemma 9, Theorem 10 and
Lemma 11 give (35). The missing running-minimum step in R2 is

\[
 \min_{i\le j}x_i\ge x_j-2c_2\ge x_j/2,
 \quad R_j\ge[\log(x_j/2)]^r
       \ge[\log(x_j/2)]^2\ge\tfrac14(\log x_j)^2.             \tag{36}
\]

The last two inequalities use $r\ge2$, $\log(x_j/2)\ge1$,
and $x_j\ge4$. Insert (36) into $v_j=\delta nMR_j/512$.
This proves the estimate, including $j=0$. ∎

TP1 may use this estimate to pay its $L^{8a}$ age weight. It does
not turn the live-field amplitude $L^{CR_j}$ in the source class
into a polylogarithm. TP1's separate amplitude hypothesis remains
separate. The conclusion also supplies no estimate in seed age.

## 7. Source check and definitions supplied

All external references below are to commit `31a47c543775` of Ethan
Sussman and Levent Alpoge's account, with Claude and Codex as the
authors of their text. The outline index `sa-index/README.md`, its
relevant chunk rows and neighbours, and `sa-index/obligations.md`
were used before reading the bounded source passages. The CA-I
references use `sa-index/ca-4.12-4.19/`. Source statements are
paraphrased; a source's conditional or incomplete statement is not
promoted to a proved input here.

| Source and checked lines | Use and limit |
|---|---|
| [SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), 17317–17407; 17471–17564; 17575–17610 | Regions, tests, rounds, positive moves, lineage age and small-component class. These give the architecture; (R1), (R2), the exact read contract and reserves remain named inputs. |
| SA 9783–9789 | Background comparison on the specified collared regions, including gauges and single-layer collars. It does not establish the new inner-boundary geometry used by QL′. |
| SA 6185–6212; 17800–17831 | Boundary slots, exempt tree length, island exponent and mass bounds. Exempt length supplies no decay inside an exempt island. |
| SA 17642–17664; 17841–17920; 17959–17997 | Retained standing operations, real cancellation, response localization, and the exterior-conditioned healed-family sum. These support the distinction between Lemma 3 and CL0. |
| SA 1270–1347 | The rooted hard-core cluster theorem used in Lemma 3, with a uniform complex majorant. Its criterion and domain hypotheses are retained. |
| SA 19459–19497 | Threshold margins, parameter order, and the early frame envelope that avoids a coupling-ceiling cycle. |
| SA 23250–23340 | The rarity/age architecture, lineage trace masses, chessboard witnesses and anchors. The opening paragraph identifies the witness obligation; these pages are not a substitute for QL′, LT or TT. |
| SA 27149–27212; 28207–28224 | The transport proof for marginal log-concavity, and the explicit limitation concerning the full interacting conditional density. Lemma 6 rebuilds the needed argument; CL is not inferred from the Gaussian case. |
| [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex), 49495–49546; 54985–55011 | Gauge-domain supply lies outside the operator theorem; the preparatory boundary theorem assumes a stage theorem and profile-class hypotheses. These do not supply NL1/LF1's missing interfaces. |
| [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex), 79847–80060 | Its reading of Balaban's conditional integral, free-bond window, Gaussian part and nonlinear readout. It is an attributed reading of the cited Balaban papers, not an independent verification of those papers here. |
| CA-II 84948–85075 | The class-membership proposition assumes (a)–(j) and clean histories and conditions on a frozen exterior. It is not the full-history CL0 used here. |
| CA-II 113200–113235; 126214–126220; 126262–126282 | Conditional healed-lineage bounds, consistency of runs, logarithmic volume exponent, and the stated age allowance. They do not establish the combined reserve (8). |
| CA-II 127294–127316; [CA-III](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_III.tex), 111180–111205 and 111418–111436 | Uniform old-region rarity is explicitly outstanding; several related history and age results are listed as incomplete. None is used as a completed proof. |
| [YM3](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), 52576–52590 | Switch products over coefficient/string hulls in a three-dimensional conditional Gaussian. This illustrates localization; it does not prove the four-dimensional composition (L). |

The downloaded files were read in excerpts, never as complete accounts.
They are `/tmp/sa_ym4.tex`, `/tmp/sa_ca_I.tex`, `/tmp/sa_ca_II.tex`,
`/tmp/sa_ca_III.tex`, and `/tmp/sa_YM3_I.tex`. Their SHA-256 identities,
in that order, are:

```text
d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f
4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93
6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f
7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d
248959db554e4678aa88e92c9fe98372cd54b45719bb70bf43c47547d0c9f443
```

The definitions supplied or made operational in this distillation are:

* The distinction between mesh, cell size, rounded radius and volume
  weight in (1); the distance, erosion and path conventions; and the
  empty-survival and level-zero conventions.
* Kernel composition for continuous draws, the filtration of exposed
  uniforms, visited-test windows, and the admissible-torus alternative.
* The exact QL′ interface, including its erosion budget, the corrected
  separation $s_*$, exclusion count $H$, path length $N_i$, and
  designation entropy. It is a required interface, not a new claim
  that the construction satisfies it.
* CL0's retained sigma-algebra and elimination identity; free-bond
  windows, block versus coordinate norms, readout support count $J$,
  $C_\infty$, the nonlinear remainder, and the depth $d_*$ needed
  for a trigger. The scalar sizes $\mathfrak b,t$ are separate from bond labels.
* The read hulls and their actual dependency meaning, the cube-count
  conversion $C_{\rm tr}$ for exempt trees, the effective size
  $\omega_fR_{\rm an}/R_f$, and the norm $N^\natural$. The ordinary versus
  live-attached partition exhausts the exponent, including carried
  constraint factors.
* The cap constant $c_*$, corrected screening function (22), explicit
  old-object summation obligation (OS), corrected supremum definition
  of $\ell_3$, and the island centre loss $\Gamma_X$.
* The constants used to make the arguments quantitative: $C_G$,
  $S_d$, $K_\infty$, $\varepsilon_W$, $c_T$, $Q$, $\chi_i$,
  $\alpha_k$, $X_*$, $C_{\rm AG}$ and $c_{\rm AG}$. Their dependencies
  and choices are specified where introduced and in §6.

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/ag1-gate.md` (Claude fresh session). First failing step: Lemma 1, lines 412-413, repairable.
1. Reading of the event: AG1's "c belongs to a live component" is aligned with TP1's "a live component meets c" by a union over at most 81 neighbouring cells, so C_AG is multiplied by 81 where TP1's reading is used.
2. **(ANC)** added as a named LF1(2) input (SA 23328, read by the lead); this repairs the first failing step. Outstanding as an LF1 verification.
3. "Proposition S" of the draft is Lemma 5 of [nl1-L.md](nl1-L.md) (frozen). The distance bound D_f >= 10 L M R_i - C for the full source, which NL1 marks outstanding, is used by (22)-(24) through (OS) and is now named here as Outstanding.
4. (OS) is stated for the whole live-attached sum, including the carried constraint factors that Theorem 5's proof places there, not only kept forms and islands.
5. Theorem 12 holds above the coupling floor x_j >= X_* and on the tori the chessboard input admits; TP1 uses it only at k_1 in its large-x regime, so TP1 is unaffected.
6. The tree inequality is at SA 1225-1269 (not 1270-1347).
7. Gamma_X uses Re Psi, since Psi(xi, p_*) need not be real.
8. In (MB), m = |D|.
9. c_f is IN1's c_0. The running minimum is taken in x, as in TP1 and SA; IN1's theta-form is equivalent up to the coupling relation. The letters delta and R_1 carry two meanings; read them from context (to be renamed at hardening).
10. The designation count D_des requires the designated live cell at level i-1 to lie within R_* + 1 cells; this is part of the interface.

**Status: frozen**, as a conditional theorem. Outstanding inputs, all named: (ANC), (OS) for the whole live-attached sum, NL1's full-source distance bound, the QL' domain/threshold verification, and the fixed-history density identification. Reopens only on a `wrong` signal or when an import it reads changes.

## Result

The distilled AG1 proves the implication **Theorem 12**: the stated
positive stopped law, trace reserve, two-run interface and exact
conditional analytic law give TP1's uniform lineage-age series
(AG-k1*). It also proves the convex-window trigger bound, the
conditional analytic localization theorem, the healed-family
holomorphic bound (d), and the corrected single-factor zero-free
estimate. These are conditional mathematical results about the
specified objects, not a construction of the required Yang–Mills run.

The imports are IN1's flow and class/domain control; LF1's positive
history construction, read/geometry rules, trace reserve and real
island/healed-family estimates; BG1's correctly gauged comparison and
plaquette bounds; LG1(3)'s chessboard inequality; NL1's exact
conditional law, readout and (L), including Proposition S's admission
hypotheses; and the explicitly quantified ordinary/boundary size
inputs. The analytic route through PAN additionally needs **(OS)**.
Its proof is outstanding. So are the indicated QL′ domain/threshold
verification and the identification of the full fixed-history density
with the proposed resummed analytic presentation. The imported (LT),
(R2), (Q), and (L) are not established by this manuscript.

Corrections made during distillation:

1. Inserted the running-minimum comparison (36), and used the bounded
   backward drift wherever R2 had assumed monotone couplings. The
   resulting rate is $\delta nM/2048$.
2. Retained the island centre value $-\Psi_0$, including $q_X/2$.
   The zero-free radius loses $\ell_m^{2p_0+9r}$; the logarithmic
   bound is proved with rational bounds instead of a decimal estimate.
3. Replaced PAN's uncapped screened radius by NL1 Proposition S,
   including its reduced decay rate and source/chart cap. Redefined
   $\ell_3$ by (24), and exposed the lost formation-level factor as
   the outstanding obligation (OS).
4. Kept healed-family resummation distinct from conditioning on a
   complete history. A proof for the former is not asserted to identify
   the latter. Free-bond convex windows and (CL0) are explicit.
5. Separated the readout's Euclidean operator norm from its sup norm,
   retained the factor $\sqrt J$, and used conservative block Cauchy
   constants. The global mean room is the stronger inequality (4).
6. Defined windows at adapted visited tests; removed the unjustified
   conditioning on every other uniform for an adaptively selected
   potential test. Continuous draws are composed as kernels.
7. Enlarged path separation and entropy constants so deleting the
   neighbourhood of an anchor really removes at most one selected
   point. All resulting numerical floors are reimposed.
8. Did not reuse the one-pass bound for iterated boxing. Stated a safe
   enlargement bound and retained the actual contraction as (R1).
9. In the exempt-hull argument, stopped the path at the first island
   and kept a tree-length-to-cube-count constant. In the real island
   estimate, replaced $R_j\le R_m$ by $R_j\le LR_m$ in the recent
   formation window.
10. Proved the small-torus case separately with its factor 16 in the
    volume ceiling; fixed the age weight before choosing constants;
    used the early flow envelope when choosing the tile size.
11. Preserved source qualifications: the CA clean-box theorem, its
    outstanding uniform-rarity statement, and its incomplete history
    claims do not discharge the named owner inputs. TP1's separate
    amplitude assumption is unchanged.

Only `library/ag1.md` is changed. The pass-1 drafts, NL1 draft and
frozen `tp1.md` remain unchanged. The text is **not yet refereed** and
grants no audit, retained or publication status.


*Referee status (lead, 2026-11-05): refereed line by line by a fresh Claude session; see the change log above and `gates/ag1-gate.md` (st1-r4: `gates/st1-r4-gate.md`). The "not yet refereed" sentence in the Result above predates that check.*
