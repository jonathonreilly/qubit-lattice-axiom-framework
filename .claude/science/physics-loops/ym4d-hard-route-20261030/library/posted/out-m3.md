# A reduced tagged current for the assumed layer package

Ethan and Levent,

Your account assumes the layer package in `4.21:lem-exempted-set`
([CA-I 72392–72399](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72392-L72399)). It uses the switched current rider in reduced form,
with $`P_1(\sigma)`$ and $`m_H(\sigma)`$, at [CA-I 72720–72728](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72720-L72728),
[CA-I 72831–72851](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72831-L72851) and `4.25:eq-current-partner-1`, [CA-I 111394–111399](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L111394-L111399).
It never defines these two operators at $`\sigma\ne1`$.

Your switched chart current at [CA-I 15306–15313](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L15306-L15313) is not that reduced
extension. At site (T), the exempted set is empty ([CA-I 72704](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72704)).
Work on an admitted flat torus with $`J=0`$.
Set every switch to zero and set the field datum $`j=0`$.
Every primitive walk then vanishes. In your composite formulas,
$`Q,a`$ and the identities carry no tag. Hence

```math
H_0=H^J=\widetilde G^J=q_0=q_J=0,\qquad
P_0=I,\qquad \mathsf k=-a\ell^{-1}.
```

The small fixed point gives $`A_G=X_G=\mathcal H^J=\Xi=0`$.
Your defining current therefore gives

```math
\mathfrak J(0;b)=-Q^Ta\ell^{-1}b.
```

Choose arbitrarily small $`b`$ on a nonzero averaging row so that this
value is nonzero. The reduced rider gives zero at those fields.
Also, the direct composite mass has value $`-Q^Ta\ell^{-1}`$,
whereas the locality clause requires a zero kernel because
$`Y(0)=\varnothing`$. These follow from your chart definition
([CA-I 14393–14425](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14393-L14425)) and the switch assignment ([CA-I 15266–15339](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L15266-L15339)).
Here $`Q^T=Q^*`$ denotes the physical bilinear transpose.

Your sentence at [CA-I 15450–15451](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L15450-L15451) leaves the representation identity
`4.5:eq-response-chart-a` unrestricted. Its proof, [CA-I 14455–14493](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14455-L14493), uses inverse and constraint identities that your account proves only at switches one. At zero switches one of them fails: there $`H_0=0`$, so $`QH_0B=0\ne\tilde B`$.
No proved step of yours uses that identity at $`s\ne1`$. (K10) extends (K1), (K3)–(K5) and (K8) by bounds and locality only. The (K3) proof bounds the terms listed at [CA-I 14759–14765](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14759-L14765). Your text there introduces the list through the identity, but the list is exactly the defining one at [CA-I 14406–14408](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14406-L14408). So these bounds hold without it. (K6) uses the identity at one only. Thus this is a missing definition
in an assumed package, with an over-wide sentence, not a false proved step.

Following issues #13, #14 and #19, this note defines the two missing
coefficients by complete words. Each word receives one tag on its full
read set. This includes the bare mass. We prove holomorphy, the operator
bounds (7), exact component locality, and zero current at site (T).
At switches one the current equals your reduced chart current.
On (K6)'s additional domain it equals the physical current increment.

Away from one this is a **new definition of the switched current**.
It does not repair or identify (K10)'s current there. The layer field
keeps its prescribed equation. The consumer table in §6.3 lists the
reduced formulas matched, and separates the older chart uses.
The other layer premises and admission of domains remain inputs.

All account and outline labels and lines refer to `31a47c543775`.
CA-I, CA-II and CA-III mean your three complete-account files.
The outline is your `YM4_sketch_500.tex` at that commit.
We use Balaban's papers through quotations in your account and the
linked proofs; his original papers were not available.

The walk localization follows Balaban's *Renormalization group approach
to lattice gauge field theories. II. Cluster expansions*, CMP **116**
(1988), (1.5)–(1.11). The current insertion algebra comes from his
*Propagators for lattice gauge theories in a background field*,
CMP **99** (1985), 389–434, (3.116)–(3.120), (3.130)–(3.138).
The physical current formula is (3.11), and its four-entry bound is
(3.14), in his *Renormalization group approach to lattice gauge field
theories. I. Generation of effective actions in a small field
approximation and a coupling constant renormalization in four dimensions*,
CMP **109** (1987). Your quotations used below are at [CA-I 13686–13739](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L13686-L13739),
15288–15301, 15830–15846 and 111394–111410.

Codex (gpt-6-astra) wrote the proof and this note. Claude (Opus 5.5) checked the proof and this note line by line, and its repairs are applied.
This is research text, not an audit, and grants no status.
No computation discharges a proof step.

## Inputs

The following are hypotheses of the theorem. They are stated before
any proof, including the bare-mass lemma.

1. **Theorem PI, issue #13.** Use the [posted theorem and proof](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/94df5579a/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-pi.md),
   §§2–3, 5–6 and 9. Retain its literal rows, physical measures,
   thick tower, local models, normalized smooth cutoffs, complete
   footprints, endpoint margins and identical restriction.
   Retain (S1-loc), (S2), (S2+), the supplied real gauges at a proper
   outer boundary, and all exterior coefficient reads. The group is
   fixed, $`L\ge3`$ is odd, and the torus has the room required there:
   
   $`\operatorname{side}(T_\eta)\ge \max\{2\widehat r+2,t_FM_F\}\ell_k, \qquad \widehat r=(2L+2)M_t.`$

   The background and twist radii obey the common PI/GW ceilings.
   These hypotheses do not admit your unrestricted background classes.
2. **GW, issue #14.** Use the [posted word estimates](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/9a3ad2072/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-gw.md),
   (P4), (P5), (P7), (P11)–(P15), §§4–7, and their constant order.
   Retain scalar and vector source spaces, endpoint readouts, physical
   reversed words, $`P`$ readouts, finite averaging carriers and
   current-word majorants. Retain the flat estimates and supplied-frame
   averaging hypotheses carried by that proof. In particular, use the
   density, overlap, scale and transpose estimates (2)–(3) below.
   They are the per-unit-length form of the averaging derivative.
   This averaging input is the analytic form of Balaban's *Averaging operations for lattice gauge theories*, CMP **98** (1985), Proposition 5, (156)–(157). Those bounds are for first derivatives at real backgrounds. Balaban states the analytic extension without proof (CMP 98 §E, p. 43), and your Remark `4.5:rem-averaging-analyticity`, [CA-I 13175–13196](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L13175-L13196), cites it as printed. GW, input 3, links a written proof.
   The full-word union-tag alternative in GW is used for (17).
3. **GW1, issue #19.** Use the [posted stronger word estimates](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/7198d9fa2/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-gw1.md),
   §§3.1, 3.3, 7 and 8. Use the same words with tree weight
   $`e^{2\mu t_w}`$ and junction cost $`e^{34\mu c_\iota}`$.
   The common constants include the preliminary current ceiling.
   All current series have absolute ratios at most $`1/4`$ on
   $`|J|_{(-3)}\le2j_*`$. We do not strengthen an arbitrary prior
   choice of PI constants after the fact.
4. **Geometry and transport.** The furnished decoupling partition
   covers the whole ambient read domain, including boundary reads.
   Use GW's common grid or a supplied transported copy, with the
   separation floors, complete connected footprints and wall adjacency
   specified below. Never-cut cubes and hubs remain in $`Y(s)`$.
   Any gauge, reality or lattice transport used must carry the supplied
   words, frames, grids and switch labels on admitted domains.
5. **Layer solution.** Supply the small solution of (29), with its
   prescribed tags and common analytic room. Its outer equation uses
   $`\widetilde G^J`$, as in your (K10). Retain weighted response
   bounds, graph bounds wherever consumed, small-branch uniqueness,
   restriction including full local stencils, and the zero-datum property.
   Supply the block-local gauge map and its value one at zero layer.
   The general field datum $`j`$ in (29) is a furnished extension;
   the identification with your block chart is at $`j=0`$.
6. **Local current and cutoff estimates.** Put
   $`K_W=D_1^TD_1+D_0D_0^T-\Delta_W`$. Here $`\Delta_W`$ is the
   component covariant Laplacian. Assume $`\mathsf p(W)\le1`$ and
   
   $`m_y^3|K_Wv|_y\le18d\,\mathsf p(W)m_y|v|_y, \quad m_y^3|F(W,h)|_y\le K_J(\mathsf p(W)+\Theta_0+\Theta_1)(\Theta_0+\Theta_1), \quad\Theta_0+\Theta_1\le2N_y(h).`$

   The remainder is local and holomorphic on the full stencil ball
   $`N_y(h)\le1/20`$, and $`F(W,0)=0`$. These are uniform coefficient
   hypotheses on the admitted complex domains. Use smooth response
   bumps with $`0\le\zeta\le1`$, plateau $`[-1/3,1/3]`$, support in
   $`[-2/3,2/3]`$, $`|\zeta'|\le5`$, $`|\zeta''|\le42`$.
   Your cutoff at [CA-I 111525–111527](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L111525-L111527) asks $`|\zeta''|\le5`$. With this plateau and support, $`\zeta'(1/3)=\zeta'(2/3)=0`$, so $`|\zeta''|\le5`$ allows a total drop of at most $`5/36<1`$. We therefore assume the weaker bound $`|\zeta''|\le42`$; the existence of such a bump is part of this input. The constant $`c_\zeta`$ in (33) does not change.
   The response bump is
   $`\widehat\chi_\square(x)=\prod_\nu
   \zeta((x_\nu-y_{\square,\nu})/(M\ell_\square))`$.
   Tensor mixed second derivatives are bounded by $`25`$.
   Elementary transports have norm at most $`\vartheta\le5/4`$.
   Where a commutator stencil meets the bump, assume
   $`m_y\le L\ell_\square`$, and use $`M\ge2L^2`$.
   Retain the required smallness of cut fields and all stencil reads.
7. **Readers and profiles.** Supply admitted intermediate images,
   holomorphic reader domains and bounds, and all datum and amplitude
   discs used in a composition. For a cut tail, retain the source
   profile and cutoff estimate (36), the weight and metric comparisons,
   and amplitude admission needed at that consumer. Bound (7) alone
   does not supply the two-distance profile.
8. **Identification at one.** Use your representation identity and
   reduced chart formula, [CA-I 14439–14493](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14439-L14493), only at switches one.
   For the physical interpretation retain all hypotheses of (K6),
   `4.5:prf-diagonal-exactness`, [CA-I 15669–15860](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L15669-L15860): the real background
   $`U_0=U_k(V_0)`$, its stated regularity and current ceiling,
   $`J=\mathcal J(U_0)`$, the datum polydisc and the uniqueness ball
   for the specified critical configuration. No own-current identity
   is assumed on the general independent-current domain.

## 1. Pairings and the bare mass

### 1.1 Pairings, carriers and scales

Use the literal rows and the stated domain of Theorem PI. Put
$`m=\ell`$, and let $`D_0`$ be the covariant site difference. Let $`D_1`$ be
the covariant curl. All transposes are bilinear trace transposes.
Fine sites and bonds have measure $`\eta^4`$; a coarse row $`c`$ has measure
$`m_c^4`$. In particular a transpose at complex background is not a
Hermitian adjoint.

Use the following first-order field and force norms:

```math
\|u\|_p=\sup_y\frac{\max\{m_y|u|_y,m_y^2|\nabla_Wu|_y\}}{p(y)},
\qquad |f|_{-3,p}=\sup_y\frac{m_y^3|f|_y}{p(y)}.       \tag{1}
```

The switch notations $`s`$ and $`\sigma`$ refer to the same parameter family.
Write $`N_y(u)=\max\{m_y|u|_y,m_y^2|\nabla_Wu|_y\}`$ and
$`N_y^\Delta(u)=\max\{N_y(u),m_y^3|\Delta_Wu|_y\}`$.
Let $`E_p`$ and $`F_p`$ be the spaces with the two norms in (1).
The graph bound is a separate layer input.

$`B_p`$ is the dimensionless row space with the same block-to-cell
convention. Every stencil in (1) is the full stencil. We use only
admitted positive weights, with
$`p(z)/p(y) \le  \exp(\delta d(y,z))`$. No regularity of $`p`$ is differentiated.

Write the actual averaging row as

```math
(Qu)(c)=\sum_x\eta^4 q(c,x)u(x),\qquad
(Q^*v)(x)=\sum_c m_c^4q(c,x)^T v(c).                   \tag{2}
```

Here $`x`$ includes the bond direction and color index. The finite sum
includes precisely the literal row of PI, not a point average. Denote
its complete double-block carrier by $`E_c`$. This includes the row bond,
all fine bonds in (2), contour transports, supplied averaging-frame
reads, and all background and boundary reads of their coefficients.

The following local facts are the averaging input of GW §7. There are
fixed constants $`C_Q,n_{\mathrm{av}},c_{\mathrm{av}}`$, independent of mesh and depth, such that

```math
|q(c,x)|\le C_Qm_c^{-4},\quad
\#\{c:x\in E_c\}\le n_{\rm av},\quad
L^{-1}m_c\le m_x\le Lm_c,
\quad d(x,c)\le c_{\rm av}\quad(x\in E_c).             \tag{3}
```

Enlarged output cells in (1) change only these fixed constants. A height
zero row has the same assertions, with its actual linear identity row.
The density bound in (3) is for $`Q`$, the derivative **per unit length**.
The nonlinear dimensionless averaging derivative instead has density
of order $`m_c^{-3}`$. Confusing these two densities loses one power here.
Divide the dimensionless derivative density from the supplied-frame
averaging input by $`m_c`$. Its pillar count gives $`n_{\mathrm{av}}=4d`$ before
cell enlargement; $`c_{\mathrm{av}}=4dL`$ is permissible.

Let $`h_\tau`$ be PI's real smooth partition. Its value on a row is its
value at that row's base point, and

```math
\sum_\tau h_{\tau,B}(c)^2=1.                           \tag{4}
```

Use PI's complete footprint $`F_\tau`$, of half-width
$`(2L+2)M_t m_\tau`$. If $`h_\tau(c) \ne  0`$, the entire $`E_c`$ lies in
$`F_\tau`$. Indeed the base point is within $`M_t m_\tau`$; overlapping
levels differ by at most one; the double-block extension has size at
most $`2L m_\tau`$. The remaining margin contains the boundary reads.
It also contains every tile read by the denominator defining $`h_\tau`$.
This last requirement is essential: PI §9, not just its local model
box, specifies the footprint.

Fix an admitted full decoupling partition $`\pi`$, covering the ambient
read domain, including boundary reads. The GW common-grid partition
and its supplied transported versions are admitted here. A permitted
cut family is any subfamily $`\pi_0`$ of that partition. Put the switch
equal to one on the complement. For a complete footprint $`F`$, set

```math
t_F(s)=\prod_{\Delta\in\pi_0:\,\Delta\cap F\ne\varnothing}s_\Delta,
\qquad
Y(s)=\mathsf K\cup\bigcup_{s_\Delta\ne0}\Delta .        \tag{5}
```

$`\mathsf K`$ includes every never-cut cube and any hubs prescribed by the site.
If hubs are present, they are included in the never-cut region before
taking the subfamily. Each distinct cube occurs once in (5). A wall
component uses your wall adjacency, with hubs joining incident
wall components. Full footprints have connected interior; touching at
a corner alone is not used to connect components.

### 1.2 The bare mass words

Define one finite row operator for each PI tile:

```math
(A_\tau b)(x)
=-\sum_c m_c^4 q(c,x)^T m_c^{-3}h_{\tau,B}(c)^2b(c),
\qquad F_{A_\tau}=F_\tau.                              \tag{6}
```

The summands with $`h_\tau(c)=0`$ are absent. This specifies the entire
word, including its finite physical contraction. We do not replace
its carrier by the two endpoints. Equivalently,
$`A_\tau=-Q^*a h_{\tau,B}^2\ell^{-1}`$, where $`a_c=m_c^{-2}`$.
Both scale multipliers and the coarse identity belong to this word.
Their tag is the tag of the whole word. Define

```math
A(s)=\sum_\tau t_{F_\tau}(s)A_\tau.                    \tag{8}
```

**Bare-mass lemma.** This is a holomorphic assignment of
$`-Q^* a \ell^{-1}`$. Its total at one is that operator. Every surviving
word has both legs and every averaging and coefficient read in one
component of $`Y(s)`$. It has a weighted absolute majorant

```math
\sup_x\frac{m_x^3}{p(x)}
\sum_\tau |t_{F_\tau}(s)|\sum_c
m_c^4|q(c,x)|m_c^{-3}h_{\tau,B}(c)^2|b(c)|
\le C_A e^{16\kappa_1}|b|_p,                           \tag{9}
```

where one may take $`C_A=C_Q n_{\mathrm{av}} L^3 \exp(\delta c_{\mathrm{av}})`$, with the
fixed cell-enlargement constants included. The switch condition is
$`|s_\Delta| \le  \exp(\kappa_1)`$ and GW's cube-size floor below.

*Proof.* Summing (6) at one and using (4) gives

```math
\sum_\tau A_\tau b(x)
=-\sum_c m_c^4q(c,x)^Tm_c^{-3}b(c)
=-Q^*a\ell^{-1}b(x).                                 \tag{10}
```

There is no remainder or boundary correction. Both identities in (10)
are finite sums at a fixed lattice.

The cube-size floor $`M_{\mathrm{dec}} \ge  4 \widehat r+8L`$ makes every $`F_\tau`$ have
coordinate span at most half a decoupling-cube side. Thus it meets at
most two grid intervals in each coordinate, hence at most sixteen
cubes. On a torus, lift this small footprint; identified cubes only
decrease the count. Consequently $`|t_{F_\tau}|\le e^{16\kappa_1}`$.
In (9), cancel the powers as
$`m_c^4 m_c^{-4} m_c^{-3}=m_c^{-3}`$. Apply (3), the weight ratio,
and (4). At most $`n_{\mathrm{av}}`$ rows remain at $`x`$. This gives exactly (9).
It is a majorant for the absolute **word** sum, not an estimate obtained
by cancellation between tiles. The negative sign in (6) is unused.

The physical transpose is also explicit:

```math
(A_\tau^Tf)(c)=-h_{\tau,B}(c)^2m_c^{-3}
\sum_x\eta^4q(c,x)f(x).
```

There is no extra fine volume after transposing (6). The double block
has physical volume at most $`C_L m_c^4`$, and (3) bounds its density
by $`C_Q m_c^{-4}`$. Thus the absolute tagged transpose sum maps fine
value size $`m|f|/p`$ to coarse size $`m^4|A^Tf|/p`$, with constant at
most $`C_L C_Q L \exp(\delta c_{\mathrm{av}}+16\kappa_1)`$. This proves the reversed
physical majorant without exchanging a physical transpose for a
counting transpose.

If a word survives a zero wall, its tag has no zero factor. Therefore
$`F_\tau`$ meets no deleted cube. The entire connected footprint lies in
the retained union, in one wall component. It contains the output
bond, the input row and every $`E_c`$ occurring in the word. This proves
the two-leg assertion, including the coefficient reads. The tile,
partition denominator and averaging row are identical in settings
agreeing on $`F_\tau`$, by PI §9 and the averaging input. Restricted
words therefore agree as well. The finite sum is holomorphic in the
base coordinates and polynomial in the switches. This proves the
lemma. At site (T), a full all-zero family kills every word. No bare
diagonal survives. $`\square`$

The tag contains the whole averaging carrier and is polynomial in
the switches. A smooth partition was assigned before tagging. A later difference, if present
in a larger word, differentiates that smooth coefficient, not a sharp
parameter-cell indicator.

## 2. Complete words and the theorem

### 2.1 The unswitched dictionary

All expressions in this subsection generate words **at one**. They
are not identities between switched sums.

For $`r=1,3,4,5`$, use the actual PI patch words

```math
W^{(r)}_\omega=S^{(r)}_{\tau_0}
(-T^{(r)}_{\tau_1})\cdots(-T^{(r)}_{\tau_n}),
\quad
S_\tau=h_\tau M_{r,\tau}^{-1}h_\tau,
\quad T_\tau=[M_{r,\tau},h_\tau]M_{r,\tau}^{-1}h_\tau. \tag{11}
```

Local inverses, transplants, coefficient reads and Dirichlet conventions
are exactly PI §§3, 5, 6 and 9. Take their entries as follows:

```math
G'_\omega=W^{(1)}_\omega,\quad
P_\omega=[W^{(3)}_\omega]_{hh},\quad
G_{0,\omega}=[W^{(4)}_\omega]_{AA},\quad
q_{0,\omega}=-m^{-3}[W^{(5)}_\omega]_{\nu\nu}m.        \tag{12}
```

The last formula converts the counting multiplier to the physical
coarse pairing. The identity entries inside the local matrices in
(11) have the footprint of their patch word. There is no independent
untagged matrix entry after the whole word receives its tag.

For every exposed identity on a site, fine-field or row space use
$`I_v=\sum_\tau h_{\tau,v}^2 I_v`$. In particular the signed words for $`R`$
are $`h_{\tau,s}^2 I_s`$ and $`-P_\omega`$. Generate $`\Lambda`$ and its transpose
by

```math
\Lambda=G'(I_s-P)D_0^T,
\qquad \Lambda^T=D_0(I_s-P^T)G'^T.                    \tag{13}
```

Keep the literal transposes and reverse the physical contractions.
No individual word is assumed symmetric.

The local vertices $`j_J,k_J,m_J`$ are fixed by [CA-I 13689–13724](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L13689-L13724):

```math
c^{(1)}(u,\lambda)(b)
={i\over2}[\lambda(b_-)+\operatorname{Ad}_{W_b}\lambda(b_+),u(b)],
\qquad
c^{(2)}(\lambda,\lambda)(b)
={1\over2i}[\lambda(b_-),(D_0\lambda)(b)],            \tag{14}
```

Use bilinear polarisation for two scalar arguments, and define

```math
\langle\lambda,j_Ju\rangle
=\langle u,k_J\lambda\rangle
=\langle c^{(1)}(u,\lambda),J\rangle,\qquad
\langle\lambda_1,m_J\lambda_2\rangle
=2\langle c^{(2)}(\lambda_1,\lambda_2),J\rangle.
```

All pairings here use the fine physical measure. This specifies their signs, stencils and current
leaves. Their derivative allocations are GW §6's allocations; no
derivative of $`J`$ is taken.

Expand, in the indicated order,

```math
\begin{split}
\Theta'_J&=k_J\Lambda+\Lambda^Tj_J+\Lambda^Tm_J\Lambda,\\
G_\pi^J&=\sum_{n\ge0}(G_0\Theta'_J)^nG_0,\\
E_J&=q_0Q(G_\pi^J-G_0)Q^*,\qquad
q_J=\sum_{r\ge0}(-E_J)^r q_0,\\
H&=G_\pi^JQ^*q_J\ell^{-1}.                            \tag{15}
\end{split}
```

In $`E_J`$, the difference $`G_\pi^J-G_0`$ means the strictly positive
$`n\ge 1`$ tail in (15); the degree-zero term is cancelled before words
are tagged. Every occurrence in (15) is replaced by its words from
(11)–(14).
Choose a degree, a displayed branch, and each factor word; then
perform its finite physical index contractions. This is the literal
word family. Degree zero contributes the trailing $`G_0`$ or $`q_0`$,
not an empty untagged inverse word. The $`Q`$ and $`Q^*`$ vertices retain
their entire $`E_c`$. The $`H`$ words in (15) are denoted $`H_v`$ below.

Let $`\Delta'`$ be your local curvature correction, the Wilson
Hessian minus $`D_1^TD_1`$. Its full finite stencil and first-order
bound are retained. We keep this stencil as one operator, including
its cancellations. Replacing a difference by the absolute values of
its separate $`\eta^{-1}`$ entries is not the source norm in GW.

### 2.2 Two new primitives

The words for the new $`P_1`$ are

```math
B_\omega=D_0P_\omega D_0^T.   \tag{16}
```

Both differences are taken before tagging. Their complete endpoint
stencils are inside PI's endpoint margins. Equivalently one may add
these stencils to the declared footprint; they add no new read outside
that margin. Thus $`P_1(s)`$ is the tagged sum of (16), not the result
of applying differences to a pointwise tag function.

The full mass family is the following disjoint signed list:

| Branch | Word before tagging | Choices and complete reads |
|---|---|---|
| $`a`$ | $`A_\tau`$ of (6) | All its rows, scales and averaging carriers, in $`F_\tau`$. |
| $`q`$ | $`Q^* q_{J,w} \ell^{-1}`$ | Every word $`w`$ of (15), with the whole left averaging carrier. |
| $`j,+`$ | $`D_0h_{\tau,s}^2(G'_u)^Tj_JH_v`$ | Each tile $`\tau`$, site word $`u`$, lift word $`v`$, and the full vertex (14). |
| $`j,-`$ | $`-D_0(P_w)^T(G'_u)^T j_J H_v`$ | Each projection, site and lift word, with literal physical transposes. |
| $`\mathrm{curv}`$ | $`-\Delta' H_v`$ | Each lift word and the entire local curvature stencil. |

The finite contractions in a displayed word are part of that word.
If a row or local stencil varies with an internal index, its footprint
includes **all** carriers in that finite contraction. They lie within
the adjacent endpoint margins or within the fixed junction carrier.
One can instead separate these finite indices and keep the same larger
footprint; all the estimates below are unchanged.

For each word $`w`$, let $`F_w`$ be the union of its complete PI footprints,
all exposed identity footprints, and all local averaging, curvature,
current and difference carriers. Shared legs lie inside the endpoint
margins. Local junctions join their incident footprints. Thus every
nonzero word has connected interior and the full tree carrier of GW.
The index set and footprints are fixed by geometry and branch labels,
independently of the values of $`W,J,s`$. Only identically zero geometric
contractions may be omitted. Vanishing at a particular base does not
change a word or its tag. Set

```math
P_1(s)=\sum_\omega t_{F_{B_\omega}}(s)B_\omega,
\qquad m_H(s)=\sum_{w\text{ in the table}}t_{F_w}(s)M_w. \tag{17}
```

These are **new primitives**: each completed word has one union tag.
In particular (17) is not the composite
$`Q^*(q_J(s)-a)\ell^{-1}+\Lambda(s)^T j_J H(s)-\Delta'H(s)`$.
Nor is it obtained by declaring $`R(s)=I-P(s)`$. Formula (13) was used
only to generate the unswitched words.

The layer retains all its prescribed primitive and composite tags.
In particular its actual lift is still
$`H(s)=G_\pi^J(s)Q^*q_J(s)\ell^{-1}`$, with the product of its two
primitive tags. Its $`G=\widetilde G^J(s)`$, $`H_0`$, nonlinear averaging map,
seven-term $`V'_s`$, and identities in (29) are not changed by (17).
This distinction fixes the otherwise ambiguous subscript on $`m_H`$.
It indicates its unswitched value, not factorisation through $`H(s)`$.

For the furnished solution write $`h=A'-H(s)X`$, and put
$`K_W=D_1^TD_1+D_0D_0^T-\Delta_W`$. Define

```math
J^\sharp_s[1]=(\Delta_W-P_1(s)+K_W)A'-m_H(s)X+F(W,h), \tag{18}
```

```math
J^\sharp_s[\chi]=(\Delta_W-P_1(s)+K_W)(\chi A')
-\chi m_H(s)X-[D_1^TD_1,\chi]H(s)X+F(W,\chi h).       \tag{19}
```

Here the local differential terms are exactly the fixed stencils of
the rider. They are not propagator primitives. Every diagonal or
identity **inside the coefficient-word assignment** (17) has its tag;
in particular no bare $`-a`$ or exposed $`I_s-P`$ is left outside it.

### 2.3 Theorem: the reduced tagged current

On the admitted domains and under the inputs above, (17) defines linear
operators $`P_1(s):E_p \to  F_p`$ and $`m_H(s):B_p \to  F_p`$. They satisfy:

1. Joint holomorphy in the admitted base pair and switches, with locally
   uniform absolute word tails on a larger switch polydisc.
2. For every admitted $`p`$, uniformly in mesh, volume and depth,
   
   $`|P_1(s)u|_{-3,p}\le C_Pe^{16\kappa_1}\|u\|_p, \qquad |m_H(s)b|_{-3,p}\le C_Me^{16\kappa_1}|b|_p.   \qquad(7)`$

   The constants $`C_P,C_M`$ precede the switch radius. They depend on
   the fixed PI/GW, group, averaging and exponent choices.
3. For every allowed cut subfamily, both kernel arguments and every
   coefficient read of a surviving word lie in one component of $`Y(s)`$.
   Restriction is the identical complete-word construction on that
   component. The physical transpose has the same locality.
   At site (T), with all switches zero, $`P_1(0)=m_H(0)=0`$.
4. All supplied gauge, reality and transport intertwiners are preserved.
   The required endpoint decay and a positive tree reserve remain.
5. At one,
   
   $`P_1(1)=D_0(I-R)D_0^T,\qquad m_H(1)=Q^*(q_J-a)\ell^{-1}+\Lambda^Tj_JH-\Delta'H.   \qquad(20)`$

6. Equations (18)–(19), used as the current slots of the link and cut
   link, have the reduced rider's stated algebraic and analytic
   properties. They are jointly holomorphic in the base, datum, switches
   and admitted cut amplitudes. On a source-free component the link
   triple is $`(0,0,1)`$. At site (T), $`j=0,s=0`$ gives $`J_0^\sharp[1]=0`$.
   At $`j=0,s=1`$, (18) is your chart current.
   On K6's additional physical domain it is the physical current
   increment. The parameterised own-level family uses the same fixed
   operators on its affine datum. An outside multiple of the uncut
   rider stays an outside multiple, not (19).

For the full link and reader conclusions, retain the layer and reader
inputs stated above. For the quantitative cut-tail profile retain its separately
specified input. Section 6 matches the displayed consumer interfaces listed there.

## 3. Why the current coefficient receives a tag

Your [outline, 10562–10578](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L10562-L10578) separates the operator equations from
identities valid only before switching. At 10578 it keeps the diagonal
member $`-a`$ of system (II) untagged and builds the splitting around it.
That member belongs to the system being solved.

We keep the layer equation (29), its $`V'_s`$, and the prescribed
members and tags of every inverted operator. The bare mass
$`-Q^*a\ell^{-1}`$ in (6) has a different role. It is a coefficient
of the current output. It is never inverted. Your locality clause at
[CA-I 72720–72728](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72720-L72728) requires its kernel to vanish off $`Y(s)`$.
An untagged copy fails this requirement at site (T). Thus (6) tags
the current coefficient without changing the diagonal in system (II).

Your interpolation formula needs a continuously differentiable function
on the switch cube. Your analytic estimates use its holomorphic extension
and the value at one ([CA-I 72541–72545](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72541-L72545), 72945–72952).
The definition (17) supplies these properties. It does not impose an
inverse identity on switched operators. This is consistent with the
operators-as-data method of Balaban, CMP **116**, (1.5), as quoted in
your [outline 10562](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L10562).

## 4. Proof of the coefficient theorem

Section 1.2 proves the bare-mass estimate with its physical powers.
We now use that exact word family to prove the remaining claims.

### 4.1 The physical absolute algebra

Write $`S_a`$ for scalar size $`m^a |v|`$, and $`B_a`$ for the corresponding
coarse-row size. Thus the dimensionless datum space is $`B_0`$.
For each word take its norm from one normalized source cell to the
specified output-cell readout, including the physical input measure.
Denote this nonnegative number by $`k_w(y,z)`$. First-order source
fields use GW's smooth cell partition; its bounded overlap and
first-difference constants are included in $`k_w`$. We never sharply
cut a first-order field and then estimate its derivative.

The strong-reserve import supplies finite row sums with weights

```math
e^{\lambda d(y,z)}e^{2\mu t_w},       \tag{21}
```

and the required reversed physical readouts. Here $`t_w`$ is the
length of a tree meeting a representative of every cube met by the
complete footprint. Choose $`0<\lambda\le \mu/4`$ as in GW1. At a local
junction, the tree length increases by at most $`17 c_\iota`$, in
addition to the two incident lengths. The junction constant includes
$`\exp(34 \mu c_\iota)`$ and the smooth-partition multiplication constant.

For clarity, the convolution assertion used here is elementary.
If $`k_{uv}(y,z)\le C_\iota\sum_x k_u(y,x)k_v(x,z)`$, then

```math
e^{\lambda d(y,z)+2\mu t_{uv}}k_{uv}(y,z)
\le C_\iota e^{34\mu c_\iota}
\sum_x
\bigl(e^{\lambda d(y,x)+2\mu t_u}k_u(y,x)\bigr)
\bigl(e^{\lambda d(x,z)+2\mu t_v}k_v(x,z)\bigr).       \tag{22}
```

Take the output supremum and sum the nonnegative right side in $`z`$.
Its bound is the product of the two row bounds and the displayed
junction constant. Reverse the physical contractions for a required
column readout. This proves the needed algebra estimate without
cancellation or a counting transpose.

The basic physical legs are these:

| Factor | Input and output |
|---|---|
| $`\ell^{-1}`$ | $`B_0 \to  B_1`$ |
| $`q_J`$ | $`B_1 \to  B_3`$ |
| $`Q^*`$ | $`B_3 \to  F_3`$ |
| $`H`$ at one, expanded into words | $`B_0 \to  E_1`$ |
| $`j_J`$ | $`E_1 \to  S_4`$, with factor $`\lvert J\rvert_{-3}`$ |
| $`G'^T`$ | $`S_4 \to  S_2`$, including the first-derivative output |
| $`P^T`$ | $`S_2 \to  S_2`$, including the first-derivative output |
| $`D_0`$ | scalar first-order size $`S_2 \to  F_3`$ |
| $`\Delta'`$ | $`E_1 \to  F_3`$ |
| $`D_0^T`$ | $`E_1 \to  S_2`$ |

The two $`D_0`$ rows mean the bounded full first-difference readout;
they are not bounds on a derivative acting on an arbitrary bounded
scalar. For $`D_0^Tu`$, its finitely many covariant first differences
are bounded by $`m^2|\nabla_Wu|`$ and the value part of (1), with the
adjacent-scale comparison. This gives the last row with a fixed
constant $`C_{\mathrm{div}}`$. The smooth localization costs are already included.

For a $`P_1`$ word, apply this last row, the bounded-source derivative
readout for $`P_\omega=[W^{(3)}_\omega]_{hh}`$, and then $`D_0`$. GW's scalar
component has output sizes $`m^2|h|,m^3|\nabla h|`$, for source $`m^2|g_1|`$.
It therefore gives a finite (21) majorant for (16). Call its row
constant $`C_P`$. This uses only first order on the input $`u`$. It does
not require a graph bound on $`u`$.

For the $`j,+`$ branch, differentiating the identity word is harmless:

```math
(D_0(h_\tau^2v))(b)
=h_\tau(b_+)^2(D_0v)(b)
+\frac{h_\tau(b_+)^2-h_\tau(b_-)^2}{\eta}v(b_-).       \tag{23}
```

The scalar difference in (23) is $`O(m^{-1})`$, with fixed overlap.
The two terms thus have output power $`-3`$ when $`v`$ has scalar
first-order power $`-2`$. For the $`j,-`$ branch, use the derivative
readout of the reversed $`P`$ word. Reversing $`G'`$ and $`P`$ is the
literal physical reversal provided by GW, not a symmetry assertion
about their tagged sums. These arguments bound the full $`\Lambda^T`$
word family from $`S_4`$ to $`F_3`$ in (21); call the constant $`C_\Lambda`$.

All mass branches are now matched. The $`q`$ branch has the chain
$`B_0 \to  B_1 \to  B_3 \to  F_3`$. The $`j,+`$ and $`j,-`$ branches have
$`B_0 \to  E_1 \to  S_4 \to  F_3`$. The curvature branch has
$`B_0 \to  E_1 \to  F_3`$. The local mass branch was proved in (9).
These exhaust the table in §2.2.

There is no hidden sum over unmatched scale powers. For example,
the exact two coarse legs in the $`q`$ branch read

```math
(Q^*q_J\ell^{-1}b)(x)
=\sum_{c,c'}m_c^4m_{c'}^4
q(c,x)^T q_J(c,c')m_{c'}^{-1}b(c').                    \tag{24}
```

The density of $`q_J(c,c')`$ is of order
$`m_c^{-2}m_{c'}^{-4}`$ with decay. Multiplication by the source
measure cancels $`m_{c'}^{-4}`$. The remaining scale ratio between
$`m_c^{-2}m_{c'}^{-1}`$ and output power $`m_c^{-3}`$ is the fixed
power already paid in GW's $`B_1 \to  B_3`$ estimate. Its summation
floor is imposed once. The transposed site factors instead use
$`\eta^4`$ throughout. The $`j_J`$ vertex pairs one $`m^{-1}`$ field with
one $`m^{-3}`$ current, giving scalar power $`-4`$, exactly as (14)
requires. No extra factor of $`\eta^{-1}`$ or row volume is suppressed.

The bare-mass words also have a (21) majorant. Their local endpoint
distance is bounded by $`c_{\mathrm{av}}`$; their tree length has a fixed bound
$`17D_X`$, the length-zero PI bound. Multiplying the constant in (9)
at $`s=1`$ by $`\exp(\lambda c_{\mathrm{av}}+34\mu D_X)`$ suffices. This multiplication
is independent of the future switch radius. In choosing constants
before the final rate, take its common upper bound for
$`\delta,\lambda\le \mu/4`$.

Let the constants in the following display include all the junction
costs of (22). A valid common bound for the mass family is

```math
C_M=C_A^*+C_Q^*C_q^*
+C_\Lambda C_j(2j_*)C_H^*
+C_{\Delta'}C_H^*.                              \tag{25}
```

The starred constants are the corresponding absolute (21) majorants;
$`\ell^{-1}`$ is included in $`C_q^*`$. The factor $`2j_*`$ leaves analytic
room around $`|J|\le j_*`$. Formula (25) bounds the two signed $`j`$ branches
by the sum defining $`C_\Lambda`$. No cancellation of those branches is
needed. The current Neumann degrees in (15) have geometric ratios
at most $`1/4`$ under the imported current ceiling. The finite additional
products in the mass table introduce no new Neumann denominator.

### 4.2 Tags, tails and the constants in your account

For a full word, GW's carrier construction gives

```math
n(F_w)\le16+64t_w/M_{\rm dec},\qquad
|t_{F_w}(s)|\le e^{16\kappa_1}e^{\mu t_w}              \tag{26}
```

when $`M_{\mathrm{dec}} \ge  64 \kappa_1/\mu`$. This counts the whole identity and
averaging carriers. Deleting switch variables for an exempted family
can only decrease the count. GW's proof doubles a spanning tree,
subdivides its traversal into arcs of half a cube side, and counts
at most $`2^4`$ cubes per arc. It applies to the full branched words,
not just to a path joining the two external arguments.

Combining (21) and (26) proves, for each of the two new primitives,

```math
\sup_y\sum_{w,z}|t_{F_w}(s)|k_w(y,z)
e^{\lambda d(y,z)}e^{\mu t_w}
\le C_Oe^{16\kappa_1},\quad O=P_1,m_H.                \tag{27}
```

The required physical reversed readouts follow with their own
constants from the same argument. The residual $`\exp(\mu t_w)`$
is retained in (27). Taking $`\delta\le \lambda`$ and using the weight
ratio gives (7). A smaller common $`\delta`$ is chosen below to leave
room for cut-tail weights as well.

This is your primitive corner constant sixteen. We do not
pay sixteen for each Neumann insertion. All insertions are expanded
before the one union tag is attached. In contrast the layer's retained
product-tagged lift can cost $`\exp(32 \kappa_1)`$, as in GW1 (5).
Finite layer composites have their prescribed
$`C \exp(c_K \kappa_1)`$ bounds. The two assignments are not equated.

To verify tails, first truncate the geometric degrees $`n,r`$ in (15).
Their positive majorants have tails bounded by geometric series.
At bounded degrees, there are finitely many factor positions. Truncate
their PI word lengths. The GW sums for each factor have tails tending
to zero in (21), uniformly on the specified analytic domain. Formula
(22) bounds the tail of any product by the sum of its factor tails
times the other finite majorants. This proves exhaustion by finite
word sums and convergence of the tails in (27). It also justifies
regrouping the sums at one in (20).

Each finite word is holomorphic in the base coordinates: its local
inverse is holomorphic on the imported open PI domain, the averaging
and local coefficients are holomorphic there, and the current leaves
are polynomial. Its switch factor is a monomial. Use the cube-size
floor with $`\kappa_1^+=\kappa_1+1`$; the same bounds hold on this larger
polydisc with $`\kappa_1^+`$ in place of $`\kappa_1`$. Uniform convergence
on compact subsets then gives joint holomorphy. One direct proof is
to integrate the finite-word Cauchy formulas on a small product of
circles inside that domain. Uniform convergence passes the formulas
to the limit, including each derivative on the smaller polydisc.
Thus there is actual analytic room, not a derivative estimate inferred
from values at a domain boundary.

### 4.3 Exact component restriction

Fix any cut subfamily and set the other selected switches to zero.
If a complete word meets a deleted cube, its monomial is zero. If
it survives, its connected complete footprint lies inside $`Y(s)`$.
Its two kernel arguments, all internal integration legs, every
averaging carrier, all local difference stencils, and all reads of
the cutoff denominators belong to that footprint. Its connected
interior puts them in one wall component. The endpoint margins and
the local junction carriers prevent a connection through a mere
corner contact. This proves the kernel assertion, not just a bound
on its value on the particular $`X`$ supplied by the layer.

For identical restriction, define the component construction by the
same labelled words whose **complete** footprints are in that
component. Do not recompute a smaller partition by deleting bump
denominator reads. PI §9 gives equality of tile labels, local models,
cutoffs and word values between settings agreeing on a footprint.
The supplied averaging frames and local vertices agree on their full
carriers. The scale multipliers and the finite contraction measures
therefore agree too. Conversely each word in the second setting is
the same word in the first. Tags agree because their cube incidence
sets agree. Absolute convergence proves equality of the restricted
sums. If a separately admitted component model has these same reads,
this is also equality with that model's construction.

There is no exception for a zero-degree word: (6), (12), (16) and
each degree-zero term of (15) have a nonempty footprint. Thus at
site (T), with a full family and no exempted set,

```math
P_1(0)=m_H(0)=0.              \tag{28}
```

For an exempted family, a word contained in a hub or never-cut region
may survive. The conclusion is component locality in the full $`Y`$,
not (28) with those regions incorrectly removed.

### 4.4 Intertwiners and the total at one

For a supplied gauge map, every local operator in (11) intertwines
the appropriate site, field and row actions. Its inverse intertwines
by multiplying that identity by the two inverses. Scalar cutoffs and
scale multipliers commute with the gauge action. The bilinear trace
pairing makes physical transposes intertwine with the contragredient
actions; (14) intertwines by covariance of a commutator. Each
contracted word, including (6), consequently has the required endpoint
actions. Multiplication by its scalar tag preserves the identity.
Absolute convergence passes it to (17).

For the compact real-form involution, all the original local formulas
are real on real data. Their complex extensions commute with that
involution. The cutoffs and physical measures are real, and
$`t_F(\bar s)=\overline{t_F(s)}`$. Applying the involution word by word gives
the corresponding reality relation for (17). No positivity at complex
switches is asserted.

For a supplied lattice or frame transport, carry the grids,
tile labels, bump profile, exterior convention, averaging frames and
switch labels with the data. Each physical contraction then has the
transported value. The set of cubes meeting $`F_w`$ is transported
bijectively, so the tag is transported as well. Hence every supplied
intertwiner with this labelled-word transport is preserved. This is
the scope of the local translations and termwise isometries in
your [outline 10332–10340](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L10332-L10340): the relevant grids, hull and any prescribed axial
trees must be carried, and the target must be admitted. Reversed
bonds use your $`-\operatorname{Ad}(W_b)^{-1}`$ field action; the transposed
physical contractions carry the same action.

Between different tori this argument applies on matching complete
reads with matching parameter-cell labels. It is not a global
covering-quotient assertion that identifies distinct switch labels.
Such identification need not commute with a union tag.
The displayed interfaces in §6.3 do not require that extra identity.
A same-grid restriction theorem alone does not give termwise isometry
covariance. The existing
transport premise must furnish that family on the transport's domain;
the new assignment then preserves it by the calculation above.

At one, all tags in (17) equal one. Sum (16) to obtain $`D_0PD_0^T`$.
Sum the mass branches to obtain

```math
-Q^*a\ell^{-1}+Q^*q_J\ell^{-1}
+D_0(I_s-P^T)G'^Tj_JH-\Delta'H.
```

By the unswitched definition (13), its middle composite is
$`\Lambda^T j_J H`$. This proves (20), using $`P=I-R`$ only at one.
All sums were justified by §4.2. This completes the coefficient
part of the theorem. $`\square`$

## 5. The current of the actual layer

### 5.1 The assignment is made after solving the prescribed equation

Keep the layer inputs stated above. Explicitly its outer field solves

```math
A'=-j+H_0b+G\Theta_J(-j+H_0b)-GV'_s(A'),
\quad G=\widetilde G^J(s),\quad
X=C_s(SA'-SH(s)X).                                    \tag{29}
```

Here $`S:A \to  \ell A`$, and $`C_s`$ is the nonlinear averaging remainder.
The seven-term $`V'_s`$ and its tags are the prescribed ones of your chart.
At $`j=0`$ it is K10's $`\widetilde G`$ fixed point. Define the new link to be

```math
\mathcal R^{\rm red}(s)
=(e^{i\eta h(s)}W,\ J+J_s^\sharp[1]),             \tag{30}
```

with its existing block-local gauge map. Equations (17)–(18) now
specify its second slot without a missing coefficient. For a field
cut use $`(e^{i \eta \chi h}W,J+J_s^\sharp[\chi])`$. For a datum-affine
family use (18) with $`A'+\tau \delta A'`$, $`X+\tau \delta X`$, and
$`h+\tau \delta h`$. For the outside-multiple convention use
$`(e^{i \eta \chi h}W,J+\chi J_s^\sharp[1])`$.

These choices define the current in your later assumed reduced package.
They replace K10's current away from one where that package uses (30).
They do not change your earlier definition. In particular we
do not assert that subtracting K10's old formula at nontrivial
switches gives (18). Your inverse proof cannot do that.

The word definitions and the following estimates specify this extension.
The agreement with your chart is restricted to switches one.

### 5.2 Bounds, locality and source-free components

Holomorphy of the furnished solution and §4.2 imply holomorphy of
(18)–(19) in base, datum, switches and admitted amplitudes. The local
nonlinear remainder and gauge map use their supplied open domains.
Intermediate images must lie in the stated reader domain; this
separate admission is not inferred from holomorphy.

At a fixed base and switches, linearity gives

```math
\delta J^\sharp[1]
=\Delta_W\delta A'-P_1(s)\delta A'+K_W\delta A'
-m_H(s)\delta X+F(W,h_1)-F(W,h_2).               \tag{31}
```

Under the local current hypothesis and $`N_y(h_i)\le 1/40`$, the remainder
difference costs at most $`9K_J N_y(\delta h)`$ in current units.
Here is the estimate. Put $`D=N_y(h_1-h_2)`$. If $`D=0`$, locality gives
zero difference. Otherwise the disc $`h_2+z(h_1-h_2)`$,
$`|z|\le 1/(40D)`$, lies in the $`1/20`$ ball. The input bounds the
remainder by $`0.11K_J`$ and its difference from the centre by $`0.22K_J`$.
If the radius is at least one, the Schwarz estimate at $`z=1`$ gives
$`0.22K_J(40D)=8.8K_JD`$. If it is smaller, the two endpoint bounds
give $`0.22K_J<8.8K_JD`$. Both are at most $`9K_JD`$.
The four linear terms in (31) contribute $`3+18d`$ times the maximum
of the four entries. For $`K_W \delta A'`$, use
$`N_y(\delta A')\le N_y^\Delta(\delta A')`$. Your proof at [CA-I 111436–111439](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L111436-L111439) writes $`N_y(\delta\mathbb H)`$ in this bound. The bound on $`K_W`$ applies to $`\delta A'`$, so we use $`N_y(\delta A')`$. The entries and the constant $`3+18d`$ do not change. Thus

```math
m_y^3|\delta J^\sharp[1]|_y
\le(3+18d+9K_J)
\max\{N_y^\Delta(\delta A'),N_y(\delta h),
m_y^3|P_1(s)\delta A'|_y,
m_y^3|m_H(s)\delta X|_y\}.                \tag{32}
```

If the layer's weighted bounds are $`\|\delta A'\|_p\le K_A D`$ and
$`|\delta X|_p\le K_X D`$, (7) gives the last two entries with constants
$`C_P \exp(16\kappa_1)K_A`$ and $`C_M \exp(16\kappa_1)K_X`$.
The first two entries use the layer's separate graph and response
inputs. This proves the required weighted datum-Lipschitz use at
every admitted $`p`$; it does not assert a Laplacian bound for $`H(s)`$.

For (19), the noncommutator terms satisfy the same argument on the
cut entries. The remaining term is local and uses the **unchanged**
$`H(s)X`$. The cutoff and transport inputs give

```math
m_y^3|[D_1^TD_1,\chi]H(s)X|_y
\le c_\zeta|\tau|N_y(H(s)X)
\mathbf1[\widetilde\Delta(y)\cap\square\ne\varnothing],
\quad c_\zeta=2(2+4\vartheta)(d-1).                   \tag{33}
```

Here $`\chi=t+\tau\widehat\chi_\square`$, with the supplied smooth bump,
$`\vartheta\le 5/4`$, the collar geometry and the scale floor stated above.
For completeness, let $`T_\mu`$ be covariant translation and set
$`\nabla_\mu=(T_\mu-I)/\eta`$,
$`\nabla_\mu^T=(T_\mu^{-1}-I)/\eta`$.
The trace pairing gives this transpose also at complex links.
With $`f_\alpha=\partial_\alpha\chi`$,
$`g_\mu=\partial^-_\mu\chi`$, direct multiplication gives

```math
[\nabla_\mu^T\nabla_\alpha,\chi]B
=f_\alpha\nabla_\mu^TT_\alpha B
-(\partial^-_\mu f_\alpha)T_\mu^{-1}T_\alpha B
-g_\mu T_\mu^{-1}\nabla_\alpha B.
```

Use $`\nabla_\mu^TT_\mu=-\nabla_\mu`$ and
$`\nabla_\mu^TT_\nu=T_\mu^{-1}\nabla_\nu+\nabla_\mu^T-\nabla_\nu`$.
In component $`\nu`$, sum the curl terms over $`\mu\ne\nu`$.
For each such $`\mu`$, the gradient coefficient is
$`(1+\vartheta)+(1+3\vartheta)=2+4\vartheta`$.
The value coefficient is $`1+\vartheta^2\le2+4\vartheta`$.
Thus, if $`s_1,s_2`$ bound scalar first and second differences,

```math
m_y^3|[D_1^TD_1,\chi]B|_y
\le(2+4\vartheta)(d-1)(m_ys_1+m_y^2s_2)N_y(B).
```

The supplied bump has
$`s_1\le5|\tau|/(M\ell_\square)`$,
$`s_2\le42|\tau|/(M\ell_\square)^2`$.
On its commutator stencils, the input geometry and $`M\ge2L^2`$ give

```math
m_ys_1+m_y^2s_2
\le|\tau|\left(\frac5{2L}+\frac{42}{4L^2}\right)
\le2|\tau|\qquad(L\ge3).
```

Off those stencils the commutator is zero. This proves (33).

Equations (32)–(33) give the four-entry and five-entry estimates with the constants in your account.
The mass term remains $`\chi m_H(s)X`$. No commutator of $`m_H`$ with
$`\chi`$, and no equality $`m_H(s)X=D_1^TD_1H(s)X`$, was used.

At a zero-wall component, the imported layer, its full local stencil
reads and the base pair depend only on that component. Section 4.3
proves the same assertion for the two nonlocal coefficient terms.
Thus (18), and (19) on its prescribed stencil domain, depend only on
the component. If both datum slots vanish there, the furnished
$`A',X,h`$ vanish there. Their required full stencils vanish as part
of the layer locality input. Each linear term is then zero and
$`F(W,0)=0`$. The gauge-map input gives the third entry equal to one.
The link triple is consequently $`(0,0,1)`$ on a source-free component.
Kernel locality alone would not justify dropping a missing local
stencil condition; that condition is retained explicitly here.

At site (T), set the full switch family to zero and take $`j=0`$.
Equation (29) gives $`A'=X=h=0`$, by the furnished small branch.
Equation (28) and $`F(W,0)=0`$ give $`J_0^\sharp[1]=0`$. This verifies
the zero-switch claim. Your K10 formula instead gives
$`-Q^*a \ell^{-1}b`$, as shown at the start of this note. Thus the two switched definitions differ.

### 5.3 Agreement at one

At $`j=0,s=1`$, (29) is your chart equation. The named
small-branch uniqueness identifies its $`A',X,h`$ with the chart's
$`A_G,X_G,\mathcal H^J(B)`$. By (20), the linear coefficient in (18) is

```math
\Delta_W+K_W-P_1(1)
=D_1^TD_1+D_0RD_0^T
=\Delta_a-Q^*aQ-\Delta'.                            \tag{34}
```

Its mass coefficient is exactly $`\mathcal K_1`$ of [CA-I 14447–14452](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14447-L14452).
Your proved reduction [CA-I 14439–14493](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14439-L14493) therefore
identifies (18) with its definitional chart current, for the admitted
independent-current base at one.

On K6's additional own-current domain, its identities give
$`RD_0^T A_G=0`$ and $`m_H(1)X=D_1^TD_1(H(1)X)`$.
Substitution into (18) gives

```math
J_1^\sharp[1]=D_1^TD_1h+F(W,h)
=\mathcal J(e^{i\eta h}W)-\mathcal J(W),   \tag{35}
```

the last equality being the CMP 109 identity quoted and used at
[CA-I 15830–15844](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L15830-L15844). K6 permits the datum continuation and datum-direction
derivatives stated there. For its affine family the operators and
base are fixed; differentiating (34) and its mass identity in the
datum direction gives the same linear part on $`h+\tau \delta h`$.
With $`F(W,h+\tau \delta h)`$ this is K6's parameterised current.

Neither argument continues in the switches. There is no assertion
of physical stationarity, an averaging constraint, a switched inverse
identity, or a physical current increment at $`s \ne  1`$. Nor is a
field-cut triple claimed to solve a new layer equation. A general
nonzero first datum $`j`$ has only the furnished general-field meaning;
the block-chart identification above is stated at $`j=0`$.

## 6. Matching the consumers

### 6.1 Cut tails and amplitudes

The new assignment retains the exponential row majorant in (27).
Here is its precise use for a product profile, when the separate
layer and profile hypotheses hold. Suppose an admitted positional
weight $`p`$ satisfies the ratio bound at rate $`\delta_w`$. Suppose

```math
N_z(A')\le Bp(z),\qquad
N_z(\widehat\chi_\square A')
\le C_\chi Bp(z)\mathbf1[z\in S],                \tag{36}
```

where $`S`$ includes every source cell and full cutoff stencil used
by the smooth localization. Use the consumer's enlarged response
cube $`\square^\zeta`$ for such an $`S`$. For
$`\delta_w+\delta_P\le \lambda`$, (27) gives

```math
m_y^3|P_1(s)(\widehat\chi_\square A')|_y
\le C_\chi C_Pe^{16\kappa_1}B\,
p(y)e^{-\delta_Pd(y,S)}.             \tag{37}
```

Indeed for $`z\in S`$, $`d(y,S)\le d(y,z)`$ and
$`p(z)/p(y)\le \exp(\delta_w d(y,z))`$. Multiply the summand of the
cell majorant by $`\exp(\delta_P d(y,S))`$; it is then bounded by
its $`\exp((\delta_w+\delta_P)d(y,z))`$ majorant. Summing proves (37).
The localization cells and their enlargement are included in (36),
so no unsupported pointwise sharp cutoff was inserted.

For [CA-II 610–633](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L610-L633), instead use
$`q_\square(y)=\sup_{z\in S}p_s(z)e^{-2\delta_Pd_{\mathfrak B_s}(y,z)}`$, with $`S=\square^\zeta`$.
The triangle inequality gives
$`q_\square(z)\le e^{2\delta_Pd_{\mathfrak B_s}(y,z)}q_\square(y)`$.
Retain input 7's metric comparison so this also holds with $`d(y,z)`$.
Thus this weight has variation rate $`\delta_w=2\delta_P\le\lambda`$.
On $`S`$, choosing the same cell in the supremum gives $`q_\square(z)\ge p_s(z)`$.
The supplied cut clause of (36) at $`p_s`$ therefore holds at $`q_\square`$, with the same $`C_\chi B`$.
This needs the full cutoff stencils inside $`S`$, as stipulated in (36).
The uncut clause need not hold globally at $`q_\square`$; the proof of (37) uses only the cut clause.
Apply that proof with extra decay rate zero and multiply by $`|\tau|`$.
It gives $`m_y^3|\tau P_1(s)(\widehat\chi_\square A')|_y\le C_\chi C_Pe^{16\kappa_1}B|\tau|q_\square(y)`$, with no extra factor.
To read this as $`20K_\chi|\tau|q_\square(y)`$, retain the consumer's cutoff and constant input
$`C_\chi C_Pe^{16\kappa_1}B\le20K_\chi`$.
The weight change proves no layer bound or constant comparison.
Reading (37) at $`p_s`$ gives only the weaker middle bound of `5.2:eq-three-sites-c`.

If the source-location input is
$`p_s(y)\le a_s \exp(-\delta_P d^\wedge(y,F))`$, (37) has **both** that
factor and $`\exp(-\delta_P d(y,\square^\zeta))`$.
For this exponential weight use $`2\delta_P\le\lambda`$, as allowed in §7.
Their product is not
replaced by a minimum. This supplies the $`P_1`$ operator part of
[CA-II 20821–20828](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L20821-L20828) and 21125–21144 with the furnished $`A'`$ profile.
Passing to the $`\eta_p f(y) U_L`$ form at [CA-I 112621–112624](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L112621-L112624) also needs
that consumer's metric comparison, reader location and amplitude
admission. They remain its named profile premises. In particular
(7) alone is not a proof of those premises.

On a receding reader stencil disjoint from the support of the bump,
all local occurrences of $`\chi=t+\tau\widehat\chi`$ are independent of
$`\tau`$. This includes $`\chi m_H(s)X`$: the output multiplier is local
even though the kernel is not. The commutator in (19) is also
independent of $`\tau`$ there. The only remaining dependence is

```math
-P_1(s)(\chi A')=-tP_1(s)A'-\tau P_1(s)(\widehat\chi A'). \tag{38}
```

Thus the receding current slot is affine, with exactly the tail
specified in your account. At a touching stencil, use (32)–(33).
On an enlarged amplitude disc, (37) is multiplied by its actual
$`|\tau|`$; it is not asserted without the disc's room conditions.

### 6.2 Readers, brackets and differentiation

Each reduced link now has the actual second slot (30). A bracket
uses these same formulas at its own furnished base, switches and
datum. The coefficient construction is uniform in those admitted
choices. Finite compositions are holomorphic on their admitted
product domains by substitution. Their current components are
your sums of the individual furnished riders, with each
base and transport kept at the place specified by that bracket.
No operator is silently moved to another base.

On a fixed retained component, §5.2 proves independence of data and
switches on the other components. If a reader sees no part of one
component, its composition is independent of that component's
switches. If a component is source-free, its triple is $`(0,0,1)`$
for all its active switch values. A switch derivative on either
unread component therefore annihilates the composition. This is
an identity on the switch subspace with the other walls fixed at
zero, not just a statement at one point. For the source-cell
argument of [CA-II 21950–22082](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L21950-L22082), a source-free read component also has
both summands in (38) zero. Its amplitude derivative vanishes.
Never-cut regions and hubs remain in $`Y`$ throughout this argument.

For derivative estimates, take a reader bound $`M_F`$ on its admitted
product domain. Cauchy's formula on interior circles of radii $`r_i`$
gives $`|\partial^\alpha(F\circ\mathcal R)|\le\alpha!M_F\prod_i r_i^{-\alpha_i}`$.
For distinct switches on $`[0,1]`$, one may use
$`r_i=\exp(\kappa_1)-1`$ in the enlarged domain. At $`\kappa_1\ge 1`$ this
is at least $`\exp(\kappa_1-1)`$, giving your
$`M_F \exp(-(\kappa_1-1)|S|)`$ bound. Integration over $`[0,1]^S`$
preserves it. Mixed datum or amplitude derivatives use the same
argument on their own smaller discs. No differentiated inverse
identity is needed. Reader norm bounds and admitted intermediate
images remain inputs; a general stored reader need not factor as
a product over components.

At own level $`\ell`$, hold the base and switches fixed and replace
$`A'_\ell,X_\ell`$ by their affine datum families in (18). This gives
exactly [CA-II 39320–39332](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L39320-L39332). Boundedness of (17) allows the limits of
datum difference quotients to pass through both operators. Apply
(7) to the quotients and take their limits to obtain the two operator
entries in [CA-II 39638–39647](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L39638-L39647). The other graph and averaging entries
remain the separately furnished layer and datum estimates.

### 6.3 Use-by-use record

This table matches the displayed interfaces at the cited lines. Claude's checks read your text for all 18 rows: `gates/out-m3-check.md` and `gates/out-m3-rows-check.md`. No downstream consumer proof was reread one by one. The table gives conditional
matches, with the layer, graph, profile and admission inputs retained.

| Account consumer | Matching argument for this assignment |
|---|---|
| [CA-I 72392–72399](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72392-L72399) | The package there is assumed. Sections 1–5 supply the reduced current conditionally; the remaining layer premises stay inputs. |
| [CA-I 72714–72728](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72714-L72728) | Use (30) as the reduced link. Equations (17), (18) and §4.3 give exactly its second slot and its two-leg kernel locality. |
| [CA-I 72754–72783](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72754-L72783); 72823–72860 | Section 5.2 gives component dependence and $`(0,0,1)`$ on a source-free component. Section 6.2 gives bounded holomorphic reader composition on the admitted product domain. |
| [CA-I 72918–72979](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L72918-L72979) | Section 6.2 proves the component derivative zeros and the Cauchy bounds with analytic room. |
| [CA-I 111391–111486](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L111391-L111486) | Subtraction is at one fixed operator pair. Equation (31), then (32), supplies the rider estimate; (7) supplies its operator entries from layer response bounds. |
| [CA-I 111512–111580](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L111512-L111580) | Formula (19) is the cut definition. Equation (33) uses the unchanged lift and the cutoff of input 6. The same $`K_{\mathsf j}=3+18d+9K_J`$ and $`c_\zeta`$ apply. |
| [CA-I 112072–112104](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L112072-L112104); 112181–112194 | Datum-affine families use (18); field cuts use (19). Linearity gives the third entry's split in (38). The fourth splits because $`\chi`$ stays outside $`m_H`$. |
| [CA-I 112587–112625](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L112587-L112625) | At (T), (7) and the layer's admitted weighted differences give both operator entries. At (L), retain the distinct product-profile input; (36)–(37) prove its operator transfer when its source profile is supplied. |
| [CA-I 112708–112740](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L112708-L112740); 115389–115407 | Use that same product bound on the enlarged amplitude disc after `(e3)^+`, which step (i) derives from (A)–(E) in the remark and the list at 115387 assumes. Local cut entries and (33) retain their supplied stencil bounds. |
| [CA-II 610–633](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L610-L633) | The standing profile must dominate the new four entries. Section 6.1 applies (37) at $`q_\square`$, with variation rate $`2\delta_P\le\lambda`$, extra decay zero and only the cut clause of (36). This gives the $`\tau`$-member at most $`20K_\chi\vert \tau\vert q_\square(y)`$, under the stated cutoff, metric and constant inputs. At $`p_s`$, (37) gives only the middle bound of `5.2:eq-three-sites-c`. The remaining profile and datum constants stay inputs. |
| [CA-II 20794–20828](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L20794-L20828); 21125–21144 | Equation (38) proves the unique nonlocal amplitude term. Equation (37) preserves the two distance factors for the admitted source profile. |
| [CA-II 21950–22082](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L21950-L22082) | Section 4.3 holds for every cut subfamily; §6.2 proves the switch and amplitude derivative zeros, keeping the never-cut set and hubs. |
| [CA-II 23160–23169](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L23160-L23169); 23993–24005 | Each bracket uses (19) or (18) as specified. Finite composition and the current sum use §6.2 and the same admission inputs. |
| [CA-II 39312–39335](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L39312-L39335); 39622–39650 | The own-level affine formula and its two operator derivative entries are proved in §6.2. No switch derivative is confused with $`\partial_\tau`$. |
| Outside multiple, [CA-II 13888–14105](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L13888-L14105) | Keep $`\chi J^\sharp[1]`$. Multiplication preserves holomorphy and the local dependence on $`\chi`$. Its entry bounds multiply the uncut bounds by the supplied multiplier bounds. It is not replaced by (19). For the current, this proof uses its general-$`\chi`$ hypotheses (a), (c) only at $`\chi=1`$; this note proves cut bounds only for $`\chi=t+\tau\widehat\chi_\square`$. |
| [CA-I 94980–94995](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L94980-L94995) | At switches one, (20), (34) and the furnished layer estimates give the two operator entries in this reduced-current use. The identification $`A'=H^C`$ remains a separate layer premise. |
| Native $`P_1`$ at [CA-I 14720–14727](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14720-L14727), 14797–14800 | At one, (16) sums to the same $`D_0PD_0^T`$. Bound (7) is a first-order-to-current bound for that operator, as required here. |
| Older chart formulations [CA-I 19637–19685](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L19637-L19685); 29381–29412 | On your uncut chart at one, §5.3's first paragraph identifies the current at each admitted datum, hence along $`B(t)+t_\square v`$ and in its first variation. Your native K10 functions away from one remain as defined. This note does not rename those functions or claim equality with (30). Any use of your F5 assertion for the new reduced family must use the explicit local-current, graph, profile and admission hypotheses above. |

The last row retains your older chart functions. The displayed reduced
identities use an analytic current and its stated entries. They do not
require equality with K10's current away from one. Such an additional
requirement would fail the zero-switch test. Equation (29) at
$`j=0,s=0`$ has $`A'=X=h=0`$, so every linear reduced rider
has zero current, whereas K10 gives $`-Q^*a \ell^{-1}b \ne  0`$ for some
arbitrarily small $`b`$. No choice of the two linear coefficients can
repair that equality. The compatible statement is precisely the
separate extension (17)–(30), with agreement at one.

## 7. Constant order

All choices below are written existence choices. They require no
numerical evaluation or machine enumeration.

1. Fix the group, odd $`L\ge 3`$, the Hölder ceiling and the fixed positive
   exponent gap used by GW. Fix its finite collection of source and
   output spaces, literal averaging and boundary conventions.
2. Make the common PI/GW choices through the flat estimates,
   comparison constants, cutoff constants, tile size $`M_t`$, model
   radius, footprint radius, $`D_X`$, $`\theta_Z`$ and $`\mu`$. Retain all
   separation and torus floors, including `(S2+)` reads.
3. Fix the physical averaging constants (3), identity-word constants
   and full junction range $`c_\iota`$. Whole PI identity footprints
   count as pieces. Charge $`\exp(34\mu c_\iota)`$ to each local junction.
   GW1 §3.1 gives finite strong-reserve constants for these same
   words. Choose the common background and averaging radii as there.
4. Fix the preliminary positive current ceiling with the GW/GW1
   absolute Neumann ratios at most $`1/4`$ on $`|J|\le 2j_*`$.
   Define the finite constants in (25) and the $`P`$ readout constant.
   The new mass has only finitely many outer branches, so it needs
   no further inverse or switch-dependent current smallness.
5. Choose $`\lambda>0`$ below all the retained endpoint rates, with
   $`\lambda\le \mu/4`$. Choose final weight and tail rates small enough
   that $`\delta_w+\delta_P\le \lambda`$, for example each at most
   $`\lambda/4`$. Impose GW's scale-summation and separation floors
   at these rates. The majorant constants used earlier have common
   upper bounds above these floors, as in GW's constant order.
6. Only now prescribe $`\kappa_1`$, put $`\kappa_1^+=\kappa_1+1`$, and choose
   the decoupling side with the required divisibility and
   
   $`M_{\rm dec}\ge \max\{4\widehat r+8L,\ c_\iota,\ 64\kappa_1^+/\mu\}. \qquad(39)`$

   Thus (7) has the requested $`\exp(16\kappa_1)`$ factor, while there
   is room for holomorphy beyond that closed polydisc.
7. Use the layer's prescribed composite constants on the enlarged
   $`\kappa_1^+`$ domain.
   Lower its datum radius for the common contraction, local-current smallness,
   cut amplitudes and reader-image admission. Its radii may depend
   on $`\kappa_1`$. They are chosen before any final coupling ceiling.
   The independent-current ceiling in step 4 does not depend on it.

No claim is made uniformly in group rank or as the Hölder ceiling
approaches one. Constants are uniform in mesh, volume, depth and
the admitted tower and weight, with the fixed choices above.

## 8. Scope and remaining inputs

Equations (6), (16) and (17) define the two reduced current coefficients.
The proof establishes their holomorphy, bounds (7), complete component
locality and agreement at one. Equations (18)–(19) then give the current
slots, conditionally on the layer and local-current inputs.
No switched inverse identity, post-tag identity $`R=I-P`$, or
continuation from the single switch value one is used.

This does not prove the remaining premises of the layer theorem.
In particular, it does not supply the layer's existence on all requested
domains, its graph estimates, field-datum estimates, nonlinear averaging
admission, gauge-map estimates, reader room, or intermediate-domain
admission. It does not prove a product profile without its source,
cutoff and metric hypotheses. It does not admit arbitrary partitions
or add transport identities beyond the supplied word families.

This is not a repair of K10's current away from one or of the
unrestricted sentence at [CA-I 15450–15451](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L15450-L15451). The physical-current
interpretation is confined to K6's domain at switches one.
The table matches the cited reduced interfaces; the downstream uses
in your proof of Theorem 0 have not been reread one by one.
