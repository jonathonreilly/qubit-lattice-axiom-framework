# GW1: the first-order current-corrected word family

**Research text by Codex; not checked.**

Provenance: FINISH row 464, GW1. Repository source revision
`0ec6a547f9dc7701c1e275ca8fd4b7d5fab90c6b`. Account and outline source
revision: `31a47c543775`, in `/Users/jonreilly/ym4d-lead/sa/`.
All source line numbers below refer to those revisions.
This is a written port of the account's (J7), conditional on the named
PI and GW imports. It is research text, not an audit or a status grant.
No computation discharges a step.

Credit Tadeusz Balaban for the operators and the propagator and walk
method. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their account, for the free-current construction and
the argument being ported. Published-source information here comes
from their account and the repository's quotations, not a fresh reading
of Balaban's papers.

The prior-work brief is `prior/gw1.md`, read in full. The registry assigns
this residual to GW1. The true-current precision problem and the general
layer/current assignment remain with B99-W and LAYER-THM.

## 1. The theorem and its assignment

Use PI's literal corner rows, physical pairings, no-inward boundary
convention, compressed whole-action Hessian and complete coefficient
reads. Assume (S1-loc), (S2), (S2+) on those reads. Use the common choice
of constants in GW, including its flat and actual separation floors,
torus room, supplied averaging frames and endpoint source spaces.
This does not replace those hypotheses by the account's unrestricted
(S1)--(S2) class.

Write \(m=\ell\), \(D=D_U\), and \(Q^*=Q^T\). Every transpose is
bilinear and uses the physical measures: \(\eta^4\) on fine variables,
\(m_c^4\) on coarse rows. At complex backgrounds a transpose is not a
Hermitian adjoint. Fix \(0<\beta _0<1\), and set

\[
 \epsilon=\tfrac12(1-\beta _0),\qquad
 \alpha_\beta=\beta+\epsilon\le\tfrac12(1+\beta _0)<1.
 \tag{1}
\]

At switches one, use precisely the account's definitions

\[
\begin{aligned}
 \Lambda&=G'RD^*,& \Pi&=I-D\Lambda,\\
 K_J&=\Theta'_J+\Pi^T\Theta_J\Pi,&
 \langle A,\Theta_J A\rangle&=
             2\langle C^{(2)}(\ell A),H^{J,T}J\rangle,\\
 G_1^J&=\sum_{n\ge0}(G_0K_J)^nG_0,&
 q_{1,J}&=(QG_1^JQ^*)^{-1},\\
 H_1^J&=G_1^JQ^*q_{1,J}\ell^{-1}.
\end{aligned}                                                  \tag{2}
\]

Here \(H^J,G_\pi^J,q_J,\Theta'_J\) are the already constructed GW
families. No new construction of those families is claimed.

**Theorem GW1.** After decreasing GW's positive current ceiling by a
fixed amount, there are \(j_*>0,\delta>0,C<\infty\) with the following
properties. These constants precede the switch radius. They are uniform
in mesh, depth, volume and the admitted tower.

For \(j=|J|_{(-3)}\le j_*\), (2) exists and has the following bounds.

1. \(G_1^J\) has the value, gradient, local gradient-Hölder and
   differentiated-source members of (J2). In normalized notation,
   \(G_1^J:F_3\to E_1^\beta\), \(0\le\beta\le\beta _0\).
   For a differentiated source, \(G_1^J\nabla^*g\in E_1^0\) for
   \(g\in C_2^\epsilon\), and it belongs to \(E_1^\beta\) for
   \(g\in C_2^{\alpha_\beta}\). The positive gap (1) is retained.
   There is no Laplacian assertion for \(G_1^J\).
2. \(q_{1,J}\in\mathcal K_{-2}\). Its density for the coarse physical
   pairing satisfies
   \[
    |q_{1,J}(c,c')|
       \le C m_c^{-2}m_{c'}^{-4}e^{-\delta d(c,c')}.
    \tag{3}
   \]
   The absolute word sums have both physical row and column majorants.
3. \(H_1^J\in\mathcal K_{-1}\), with the (J4) value, gradient and
   gradient-Hölder readouts, including their weighted versions.
   Its physical transpose maps \(F_3\) to coarse weight \(-4\).
   At one, \(\ell QH_1^J=I\) and
   \((\Delta_a-K_J)H_1^J=Q^*q_{1,J}\ell^{-1}\).
4. The words are analytic on complete local reads. Their nonnegative
   endpoint and branch majorants are absolutely summable with spare
   tree decay. Restricted sums agree on common complete footprints.
   At zero switches, these families separate into the retained
   components.

For the switch statement, expand (2) **at one**, including every current
weight, scalar branch and coarse correction. Give each resulting
\(G_1^J\) or \(q_{1,J}\) primitive word one tag per distinct cube met by
its complete footprint. With GW's notation, assume

\[
 M_{\rm dec}\ge
 \max\{4\widehat r+8L,\ c_\iota,\ 64\kappa _1/\mu\},
 \qquad |s(\Delta)|\le e^{\kappa _1},                    \tag{4}
\]

with the grid divisibility required there. The primitive bounds above,
including the density and physical column bounds, are then at most
\(Ce^{16\kappa _1}\). The ceiling \(j_*\) is independent of
\(\kappa _1\).

There is an assignment distinction for the lift. CA-I 15306--15308
defines \(H_1^J(s)\) as the **composite**

\[
       H_1^J(s)=G_1^J(s)Q^*q_{1,J}(s)\ell^{-1}.          \tag{5}
\]

Thus its two primitive tags remain a product. Its bounds are
\(Ce^{32\kappa _1}\), a permissible \(Ce^{c_{\mathbb K}\kappa _1}\)
in the account. Giving an entire lift word a single union tag instead
gives a \(Ce^{16\kappa _1}\) bound, but defines another switched lift.
Both equal (2) at one. The theorem identifies (5), and does not identify
these two assignments away from one.

## 2. Named imports and local norms

The mathematical imports are the following restricted statements.

* **PI:** `print-inverse-r2.md`, §§2--3, especially Theorem PI at
  322--365. This supplies the literal operators, the \(q_0\) words,
  their physical normalization and complete-footprint compatibility.
  Its repaired local scope and boundary reads are retained.
* **GW:** `walks-gw.md`, (P5), (P7), (P11)--(P15), §§5--8 and its
  constant-order table. We use its actual PI words in the stronger
  source spaces, their reversed words, scalar divergence estimates,
  vector Hölder-source estimates, \(P\) readouts, physical averaging
  rows, and the already constructed \(G_\pi^J,q_J,H^J,\Theta'_J\)
  majorants. Its §7 uses the supplied-frame averaging result of
  `b98p5.md`, §§2.1--2.4; that premise stays in force.
* **B99:** `b99.md`, B15 at 1594--1799, and B16 through 1934, already
  construct the real true-current corrected operators and their
  energy estimates on their admitted boundary class. Their formula
  reconstruction fixes the per-length quadratic coefficient.
  `b99-w.md`, Lemma 3.3 at 262--285, identifies the corresponding
  unfolded blocks. These are reused for the matched true-current
  identification, not reproved or extended to precision/root families.
  The later repaired W result supersedes the old open-W summary in
  `b99.md`; see `b99-w.md`, 796--876, and
  `gates/b99w-gate.md`, 169--194.
* **Account:** CA-I 12739--12761 fixes norms and physical transposes;
  13579--13637 fixes \(G_0,q_0,\Lambda\); 13681--13980 gives
  `4.5:lem-free-current-operators`, particularly (J1)--(J4) and
  the (J7) reduction at 13944--13955. CA-I 15266--15340 fixes
  primitive union tags and subsequent composites.

Outline navigation used `sa-index/README.md`, the neighbouring
operator rows in chunks 10 and 11, and `obligations.md` 523--550,
627--640. SA 10139--10161, 10307--10342 and 11687--11715 were then read.
The latter passage gives the ordered current route and expressly leaves
the species and derivative allocation to be checked. It excludes the
Laplacian member. The published route, as quoted in `lit-balaban.md`
§3 and the account, is CMP 99b (3.130)--(3.138), followed by CMP 116's
walk tagging. The omitted inverse-walk proof is not treated as a new
unconditional input: PI supplies the bare words on the stated class.

Here are the norms used in the proof. On a scale cell \(y\), including
its fixed enlargement and endpoint stencils, put

\[
\begin{split}
 |u|_{V_r,y}&=m_y^r\sup|u|,\\
 |u|_{C_r^\alpha,y}&=m_y^r\sup|u|
                           +m_y^{r+\alpha}[u]_\alpha,\\
 |A|_{E_r^\beta,y}&=m_y^r\sup|A|+
       m_y^{r+1}\sup|\nabla A|+
       m_y^{r+1+\beta}[\nabla A]_\beta .
\end{split}                                                   \tag{6}
\]

For \(\beta=0\), omit the last term. Write \(E=E_1^0\),
\(F_3=V_3\), and \(B_r\) for the coarse norm \(m_c^r|b(c)|\).
The fine and scalar versions of \(V_r,C_r^\alpha\) are distinguished
by their arguments. Hölder comparisons use the local frames and
distances specified in GW, with the account's local range restriction.
All statements allow weights \(p\) satisfying
\(p(y)/p(z)\le e^{\delta d(y,z)}\). We never differentiate \(p\)
or the piecewise scale \(m\).

For the left scalar branch use the source space

\[
 \mathcal D_\alpha=
 \{f+D\varphi:f\in V_3,\ \varphi\in C_2^\alpha\},\qquad
 \|v\|_{\mathcal D_\alpha}
 =\inf_{v=f+D\varphi}
       (\|f\|_{V_3}+\|\varphi\|_{C_2^\alpha}).           \tag{7}
\]

A gradient here is one of the differentiated sources allowed by GW.
The general \(\nabla^*g\) member uses its corresponding tensor source.
First-order and Hölder inputs are localized by GW's smooth partitions.
The full zero-extension Hölder norm is used. A sharp cell indicator
is never differentiated.

## 3. The first hard step: all branches of the insertion

We prove the termwise bound before constructing a new inverse.
Some care with the word “column” is necessary. \(G_0\Pi^T\Theta_J\Pi\)
acts on \(E\); its physical transpose need not map bounded forces to
bounded forces. Its natural output is (7). We prove that typed column
bound explicitly. Completed inverse chains have a bare inverse at
both ends; their reversed chains then have the full first-order
endpoint bounds. No bounded-data bound for an isolated order-zero
singular integral is assumed.

### 3.1 The absolute algebra, including the extra tree reserve

For each localized word take its norm from a normalized input cell
to the indicated output readouts. This gives a nonnegative cell
majorant. Physical input measures are included before taking the norm.
Use the maximum of the row sum and column sum of these majorants,
with weights \(e^{\lambda d(y,z)}e^{2\mu t_w}\).
Here \(t_w\) is the complete-footprint tree length used in GW, and
\(0<\lambda\le\mu/4\). The same convention applies to a rooted side
branch, with its other endpoint summed. Reversed readouts are included
as separate, physically transposed majorants.

This extra reserve follows from GW's written (P14), not from a bound
on a summed operator. For a bare word of length \(n\),

\[
 k_w(y,z)e^{2\mu t_w+\lambda d(y,z)}
    \le C\theta_Z^{n/2}e^{-(\mu-\lambda)d(y,z)}.         \tag{8}
\]

There are at most \(D_*^n\) words from either end and a fixed number
of endpoint cells for each end tile. Since
\(D_*\theta_Z^{1/4}\le1/4\), these sums and their tails converge.
This also applies to the normalized \(\nu\nu\) block giving \(q_0\).
The reversed-word estimate in GW §4 is used at the other end.
Identity pieces have bounded overlap and bounded tree length; they
also have finite majorants in this norm.

When two factors are joined, insert the smooth partition of unity
at their matched leg. The new kernel is bounded by the convolution
of the two nonnegative cell kernels, times the fixed multiplication
constant of that partition. The triangle inequality gives
\(e^{\lambda d(y,z)}\le e^{\lambda d(y,x)}e^{\lambda d(x,z)}\).
GW's carrier construction gives

\[
 t_{uv}\le t_u+t_v+17c_\iota
 \quad\hbox{at each local junction}.                   \tag{9}
\]

Charge \(e^{34\mu c_\iota}\), and the partition constant, to that
junction. Row and column convolution then prove submultiplicativity.
Each internal physical measure and scale factor cancels with the
matching leg. This is a nonnegative-kernel proof; it uses no
cancellation between different words.

The larger insertion constants are fixed now. Reuse GW §6's already
constructed current families with these constants in its majorant
inequalities. Decrease its preliminary current ceiling so those
inequalities still have ratios at most \(1/4\). This is a finite
reweighting of that same proof and assignment: (8) supplies the
stronger bare norms, and only the fixed junction costs have changed.
No local model, tile size or background radius is chosen again.
The resulting \(H^J\) side-branch constant is finite and independent
of the later \(\kappa _1\).

The following norms and inequalities always include these costs.
Their constants can be bounded uniformly for \(\lambda\le\mu/4\)
above GW's summation floors. Fixed changes of physical scale powers
use GW (P5); they do not occur once for every factor in a chain.

### 3.2 The current vertex with its physical measures

Expand \(w=H^{J,T}J\) into its existing GW words. A term rooted at
coarse row \(c\), with current leaf in cell \(u\), has majorant

\[
 h_\gamma(c,u)=m_c^4
       \sum_{b\in u}\eta^4
       |H^J_\gamma(b,c)|m_u^{-3}.                       \tag{10}
\]

Thus \(m_c^4|w_{c,\gamma,u}|\le h_\gamma(c,u)j\).
The sum of \(h_\gamma(c,u)\) over \(\gamma,u\), with its entire
tree weight, is at most \(H_T^*\). Hence the corresponding sum
of \(m_c^4|w_{c,\gamma,u}|\) is at most \(H_T^*j\).
This is the physical transpose estimate of GW §6, reweighted as
in (8)--(9). All reads from that branch remain attached to the row \(c\).

Let \(V_c(A,B)\) be the polarized quadratic coefficient
\(C^{(2)}(\ell A)(c)\). Its two fine legs lie in the complete
double-block carrier of \(c\). The one-leg density estimate imported
in GW §7 says that, with the other normalized leg bounded,

\[
 |D_A V_c(A,B)(x)|_{\rm density}
       \le C m_c^{1-4}\,\|B\|_{V_1,\operatorname{car}(c)}.
 \tag{11}
\]

The two legs can be interchanged: this is the polarization of a
quadratic Taylor coefficient. It holds for each fixed \(c\) and each
fixed weight \(w_{c,\gamma,u}\), also at complex backgrounds.
Multiplying (11) by the coarse pairing measure and this weight gives

\[
 m_c^4|w_{c,\gamma,u}|\,C m_c^{-3}\|B\|_{V_1}
 \le C h_\gamma(c,u)j\,m_c^{-3}\|B\|_{V_1}.            \tag{12}
\]

A fine bond belongs to only a bounded number of these adjacent-height
carriers. Their scales are comparable with its scale, with constants
depending on \(L\). Thus (12), summed over the relevant carriers,
is a termwise \(V_1\to V_3\) bound. Interchanging the two fine legs
gives its physical column bound. The current side branch is unchanged
by this interchange; it is not discarded or transposed into a new
current. The norm of this vertex family is therefore

\[
                  \vartheta^*\le C_{\rm av}H_T^*j.      \tag{13}
\]

The local vertex, its two carriers and the entire branch (10) are
included in (9). Formula (12) displays the scale cancellation:
the induced weight has size \(m_c^{-4}\), not \(m_c^{-3}\).
No derivative of \(w\), hence no derivative of \(J\), was used.

### 3.3 The scalar branches and every identity

Use the actual smooth identity words

\[
 I_f=\sum_\tau h_{\tau,f}^{\,2}I_f,\qquad
 I_s=\sum_\tau h_{\tau,s}^{\,2}I_s,
 \qquad R=I_s-P.                                      \tag{14}
\]

The component cutoffs are PI's cutoffs. Each term carries its full
PI footprint, including the cutoffs' coefficient reads. The identities
in (14) are equalities at one. After tagging, no untagged identity is
substituted for either sum. The product rule and the cutoff estimates
bound these multipliers in \(E_r^0\), \(V_r\) and \(C_r^\alpha\).

Define three families of words

\[
 B_0=I_f,\qquad B_1=D G'I_sD^*,\qquad B_2=D G'PD^*,
 \qquad (\sigma_0,\sigma_1,\sigma_2)=(1,-1,1).          \tag{15}
\]

Every occurrence of \(G'\), \(P\), or an identity in this display is
expanded. The subscript on \(B_a\) is a branch index, not GW's bare
constrained inverse. Then \(\Pi=\sum_{a=0}^2\sigma_a B_a\).
Put \(L_a=G_0B_a^T\). In particular,

\[
 L_0=G_0 I_f,\quad
 L_1=G_0D I_s^T G'^T D^*,\quad
 L_2=G_0D P^T G'^T D^*.                               \tag{16}
\]

Keeping the transposes in (16) is essential. A transposed PI word
is its reversed word, not the original right-parametrix word.
At one the summed \(P,G'\) are symmetric, and (16) is exactly
the account's \(G_0D RG'D^*\) decomposition.

Here is the complete allocation of scales and derivatives:

| Part of a branch | Input | Output | Reason |
|---|---|---|---|
| \(D^*A\) in \(B_1,B_2\) | \(E_1^0\) | scalar \(V_2\) | the existing first derivative of \(A\) |
| \(I_s,P\) on this leg | scalar \(V_2\) | scalar \(V_2\) | cutoff multiplier; GW \(P\) word bound |
| \(G'\), then \(D\) | scalar \(V_2\) | scalar value and gradient of powers \(0,1\), then fine \(V_1\) | GW ordinary scalar source, power \(a=0\) |
| \(G'^TD^*f\) in \(L_1,L_2\) | fine \(V_3\) | scalar \(C_2^{\alpha_\beta}\) | GW scalar divergence source, power \(a=2\) |
| \(I_s^T,P^T\) on this leg | scalar \(C_2^{\alpha_\beta}\) | scalar \(C_2^{\alpha_\beta}\) | smooth multiplier; bounded-source first-derivative bound for reversed \(P\) |
| \(G_0D\) | scalar \(C_2^{\alpha_\beta}\) | fine \(E_1^\beta\) | GW vector Hölder-source word, gap \(\alpha_\beta-\beta=\epsilon\) |
| \(G_0I_f\) | fine \(V_3\) | fine \(E_1^\beta\) | GW ordinary vector source |

All scalar columns use GW's reversed scalar estimates. In particular,
the differentiated scalar column is an ordinary-source gradient of the
reversed scalar inverse. It is not obtained by dualizing a Hölder
seminorm.

The estimates are uniform over the requested exponents. The scalar
exponent satisfies \(\epsilon\le\alpha_\beta\le1-\epsilon\);
the vector loss is \(\alpha_\beta-\beta=\epsilon\).
Thus the exponent margins in GW's (P7) remain bounded below by
this one fixed positive number. No limiting estimate at exponent
zero or one is imported.

For explicit constants, let \(d_*,g_s,g_d,g_v,p_0,p_\alpha,i_0,i_\alpha\)
bound, respectively, the first row's derivative, \(DG'\),
\(G'^TD^*\), \(G_0D\), \(P\) on \(V_2\), \(P^T\) into
\(C_2^{\alpha_\beta}\), and the indicated identity multipliers.
Let \(g_0\) bound \(G_0:V_3\to E_1^\beta\). Increase these finitely
many constants to include their reversed versions and all allowed
exponents. Admissible branch constants are

\[
\begin{array}{c|ccc}
 a&0&1&2\\ \hline
 r_a:\ B_a:E\to V_1&i_0&g_s i_0d_*&g_s p_0d_*\\
 l_a:\ L_a:V_3\to E_1^\beta&g_0i_0&g_v i_\alpha g_d&g_v p_\alpha g_d\\
 u_a:\ B_a^T:V_3\to\mathcal D_{\alpha_\beta}
       &i_0&i_\alpha g_d&p_\alpha g_d
\end{array}                                                   \tag{17}
\]

No derivative is applied to the bounded force in the last two rows.
For example, the second entry in the last row means the representation
\(D(I_s^TG'^TD^*f)\) in (7), not a pointwise estimate of that derivative.
GW's source localization product rule includes the terms with
\(\nabla h\); their complete reads and constants are included here.

### 3.4 The nine terms and their physical columns

With each current vertex from (10)--(12) expanded, the exact insertion is

\[
 T_J:=G_0\Pi^T\Theta_J\Pi
   =\sum_{a,b=0}^2\sigma_a\sigma_b L_a\Theta_J B_b.
 \tag{18}
\]

This contains one identity/identity term, four terms with a scalar
branch on one side, and four with scalar branches on both sides.
There is no remaining \(R\), \(\Pi\), or unexpanded current weight
in a word of (18).

For a particular triple of words and particular vertex branch, its
row kernel is bounded by the convolution

\[
 k_{a,\gamma,b}(y,z)\le
  \sum_{x,v} k_{L_a}(y,x)
       k_{\Theta,\gamma}(x,v)k_{B_b}(v,z).              \tag{19}
\]

The vertex kernel includes its current leaf and physical measure.
The junction constants of (9) are understood in (19). Its absolute
algebra norm is at most \(l_a\vartheta^*r_b\).

The literal physical transpose is

\[
       (L_a\Theta_\gamma B_b)^T
          =B_b^T\Theta_\gamma^T B_aG_0^T.              \tag{20}
\]

Read it from the right. GW sends \(V_3\) by \(G_0^T\) to \(E\);
\(B_a\) sends this to \(V_1\); (12) sends it to \(V_3\);
the last row of (17) sends it to \(\mathcal D_{\alpha_\beta}\).
This proves a column bound \(u_b\vartheta^*r_a g_0\), with exactly
the same current branch and footprint. On a scale cell the physical
pairings are scale neutral:

\[
 m^4(m^{-1})(m^{-3})=1,\qquad
 m^4(m^{-2})(m^{-2})=1.                                \tag{21}
\]

The second identity is the pairing after transferring \(D\) to the
test field. Thus (20) is a physical column estimate, not a counting
transpose of the fine kernel. Its output in (7) defines a bounded
functional on the local \(E\) space. This does not assert a bound
on arbitrary inputs from the dual of a Hölder space. The forward
and reversed normalized cell majorants each have both Schur sums,
by (8)--(9) and (17).

Consequently, for a finite constant \(C_\Pi\) depending only on the
fixed imports and choices,

\[
 \begin{split}
  \|T_J\|_{\rm abs,\ E\to E_1^\beta}&\le C_\Pi j,\\
  \|T_J^T\|_{\rm abs,\ V_3\to\mathcal D_{\alpha_\beta}}
                                                   &\le C_\Pi j.
 \end{split}                                                   \tag{22}
\]

In particular, for the forward \(E\)-to-\(E_1^\beta\) cell
majorants \(k_w\), the two sums meant here are

\[
 \sup_y\sum_{w,z}k_w(y,z)e^{\lambda d(y,z)+2\mu t_w},
 \qquad
 \sup_z\sum_{w,y}k_w(y,z)e^{\lambda d(y,z)+2\mu t_w}
       \ \le C_\Pi j .
\]

The physical transpose readout is separately specified by the
second line of (22); these two notions of column are not conflated.

For example take \(C_\Pi\) to dominate
\(C_{\rm av}H_T^*(\sum l_a)(\sum r_b)\) and
\(C_{\rm av}H_T^*g_0(\sum u_b)(\sum r_a)\).
It already includes all carrier and tree costs. The normalized
row readout is \(m_y|T_JA|+m_y^2|\nabla T_JA|+
m_y^{2+\beta}[\nabla T_JA]_\beta\), for an input normalized by
\(m_z|A|+m_z^2|\nabla A|\). The column has force weight \(3\)
and scalar divergence weight \(2\), as (7), (20)--(21) show.

For a completed chain \(G_0\Pi^T\Theta_J\Pi G_0\), reversing
puts a bare inverse on the left again. The same table, with reversed
bare words and \(a,b\) interchanged, gives \(V_3\to E_1^\beta\)
at that endpoint too. It also applies when several insertions occur.
No symmetry of an individual word is used.

This proves the requested first step term by term. The right derivative
uses the input field's first derivative. The derivative next to the
rough current on the left stays on \(G'^T\) through its divergence
source estimate. The last derivative stays on \(G_0\). Each insertion
regains \(C^{\alpha_\beta}\) from a bounded force, so the Hölder gap
is not spent repeatedly along a chain. No bound on \(\nabla J\) or
on a Hölder norm of \(J\) has entered.

## 4. The unswitched inverse and the J2 readouts

GW §6 supplies the absolute \(E\to E_1^\beta\) estimate for
\(G_0\Theta'_J\), including the reversed completed chains. Combine it
with (22). Choose \(C_K\) to cover both orientations, and write

\[
 A_J=G_0K_J,\qquad
 \|A_J\|_{\rm abs,\ E\to E_1^\beta}\le C_Kj=:a .
 \tag{23}
\]

Use the norm of \(E_1^\beta\) to continue a chain; its inclusion in
\(E\) has norm at most one. Fix a positive ceiling with \(a\le1/4\).
The series

\[
 G_1^J=\sum_{n\ge0} A_J^nG_0,\qquad
 \|G_1^J\|_{\rm abs,\ F_3\to E_1^\beta}
       \le \frac{g_0}{1-a},\qquad
 \|G_1^J-G_0\|_{\rm abs}
       \le \frac{a g_0}{1-a}                            \tag{24}
\]

converges in the algebra of §3.1. A term of \(A_J^nG_0\) is a
sequence of \(n+1\) bare field words, with each intervening insertion
expanded either by GW's \(\Theta'_J\) formula or by (18).
The current leaves of (10), all scalar inverse words, the \(P\)
words and all the identity labels of (14) remain in that term.
Its bound is a product of nonnegative majorants. Summing the
insertion choices gives at most \(a^n g_0\), with the tree reserve
already included. There is no estimate of a resummed insertion at
nontrivial switches.

For a differentiated-source member, the rightmost bare word has
the GW bound

\[
 G_0\nabla^*:C_2^\epsilon\longrightarrow E,\qquad
 G_0\nabla^*:C_2^{\alpha_\beta}\longrightarrow E_1^\beta .
 \tag{25}
\]

Replace only \(g_0\) in (24) by the corresponding constant in (25).
Every further insertion is bounded by (23). The source exponent is
therefore needed once at the initial endpoint. Formula (1) is the
same fixed gap at every later scalar branch. This proves the
differentiated-source members, without asking for \(C^\beta\)
regularity of the independent current.

For clarity, the physical powers in the bounded-source members can
also be read without normalized notation. If \(f\) is supported in
a cell of scale \(m_z\), the three bounds in cell \(y\) are

\[
 C e^{-\lambda d(y,z)}m_z^3
       (m_y^{-1},\,m_y^{-2},\,m_y^{-2-\beta})\sup|f|.
 \tag{26}
\]

At equal scales these are the powers \(m_y^2,m_y,m_y^{1-\beta}\)
of (J2). A fixed scale ratio is absorbed by a fixed decrease of
decay. For (25), replace \(m_z^3\sup|f|\) by the normalized
\(C_2^\epsilon\) or \(C_2^{\alpha_\beta}\) source norm.
This gives the corresponding value and gradient powers.

The transpose of a particular completed chain is the reverse chain,
with each bare word replaced by its literal transpose. Its two
endpoint inverses remain present. Equations (17)--(20) give the
estimates for every new insertion in this orientation; GW §6 does
so for \(\Theta'_J\). Reindexing a finite product by reversal
therefore proves the same version of (24) for the physical columns.
This is a termwise estimate, not an inference from the symmetry
of the summed \(G_1^J\).

The equality with the inverse in the account is an unswitched
algebraic consequence. On a finite lattice,

\[
 \Delta_a-K_J=\Delta_a(I-G_0K_J),\qquad
 (\Delta_a-K_J)^{-1}=(I-G_0K_J)^{-1}G_0=G_1^J.          \tag{27}
\]

The inverse of \(I-G_0K_J\) exists by (23). These are finite operator
identities; no uniform second-derivative bound is extracted by
multiplying (24) by \(\Delta_a\). In particular (27) does not
assert a Laplacian member for the corrected inverse.

## 5. The coarse inverse, with both physical scale factors

The following normalization avoids accumulating scale ratios.
For a coarse operator with density \(q(c,c')\), define

\[
 \widehat q(c,c')=m_c^3m_{c'}^3q(c,c').
 \tag{28}
\]

This is its matrix between normalized \(B_1\) input and \(B_3\)
output coordinates. Indeed the density acts with measure \(m_{c'}^4\),
so
\(m_c^3\sum_{c'}m_{c'}^4q(c,c')m_{c'}^{-1}b(c')
=\sum_{c'}\widehat q(c,c')b(c')\).
PI's exact formula \(q_0=-m^{-3}[M_5^{-1}]_{\nu\nu}m\) consequently
gives

\[
 \widehat q_0(c,c')=-[M_5^{-1}]_{\nu\nu}(c,c').          \tag{29}
\]

The \(\nu\) pairing is counting. Thus (8) directly supplies both
row and column word majorants for (29), without a change from
physical to counting transposes on the fine fields.

The other matched legs are

\[
 Q:E_1^0\to B_1,\qquad Q^*:B_3\to F_3,\qquad
 q_0:B_1\to B_3.                                     \tag{30}
\]

The physical row and column estimates of GW give (30). Every
averaging carrier is retained when a word is joined. Put

\[
 E_J=q_0Q(G_1^J-G_0)Q^*,\qquad
 \widehat E_J=m^3 E_J^{\rm count}m^{-3}.                \tag{31}
\]

Here \(E_J^{\rm count}(c,c')=m_{c'}^4E_J(c,c')\).
Equations (24), (29)--(30) give

\[
 e:=\|\widehat E_J\|_{\rm abs}
       \le C_{\rm comp}\frac{a}{1-a}.                 \tag{32}
\]

The finite constant \(C_{\rm comp}\) includes \(g_0\), \(q_0\),
both averaging legs and their junction costs. It is chosen before
the final current ceiling. Take that ceiling so the right side
of (32) is at most \(1/4\).

This is also a column estimate. One can either reverse each complete
chain with the matching powers, or use the two Schur sums of the
forward normalized convolution in (31). For the latter, the exact
normalization is decisive:
the physical transpose of \(E_J:B_3\to B_3\), acting on \(B_1\),
has normalized matrix \(\widehat E_J^T\). The powers follow from
\(m_c^4(m_c^{-3})(m_c^{-1})=1\).
Each word of \(\widehat E_J\) is a finite coarse matrix, bounded
entrywise by that convolution. Transposing the majorant exchanges
its two already bounded Schur sums. This proves the physical
column estimate without asserting symmetry of a word or dualizing
a Hölder norm.

At one,

\[
 QG_1^JQ^*=q_0^{-1}(I+E_J).
 \tag{33}
\]

It follows that

\[
 q_{1,J}=\sum_{r\ge0}(-E_J)^r q_0,\qquad
 \widehat q_{1,J}
      =\sum_{r\ge0}(-\widehat E_J)^r\widehat q_0,
 \qquad
 \|\widehat q_{1,J}\|_{\rm abs}
       \le \frac{q_*}{1-e},                           \tag{34}
\]

where \(q_*\) is the majorant of (29). The coefficients in
\(G_1^J-G_0\) in each \(E_J\) are expanded by (24).
Thus a coarse word contains every one of its current and scalar
branches. The \(r=0\) term is a \(q_0\) word; there is no
empty-footprint primitive identity term.

We spell out the conversion of (34) to (3). With \(\rho\) the
actual layer separation in local units, GW's level barrier gives

\[
 (m_{c'}/m_c)^b
   \le L^{|b|}\exp\!\left(\frac{|b|\log L}{\rho}
                                      d(c,c')\right).
 \tag{35}
\]

Choose the common floors so that \(8\log L/\rho\le\lambda/4\),
and take \(0<\delta\le\lambda/4\). A single entry of (34) is
bounded by \(Ce^{-\lambda d(c,c')}\). Therefore

\[
 \begin{split}
 |q_{1,J}(c,c')|
 &\le C m_c^{-3}m_{c'}^{-3}e^{-\lambda d(c,c')}\\
 &=C m_c^{-2}m_{c'}^{-4}
          (m_{c'}/m_c)e^{-\lambda d(c,c')}
 \le C' m_c^{-2}m_{c'}^{-4}e^{-\delta d(c,c')}.
 \end{split}                                                   \tag{36}
\]

More than an entry bound follows. If \(q_w\) denotes an individual
coarse density word, (34)--(35) give

\[
 \begin{split}
 \sup_c\sum_{w,c'}m_c^2m_{c'}^4|q_w(c,c')|
                e^{\delta d(c,c')}e^{2\mu t_w}&\le C,\\
 \sup_{c'}\sum_{w,c}m_{c'}^2m_c^4|q_w(c,c')|
                e^{\delta d(c,c')}e^{2\mu t_w}&\le C.
 \end{split}                                                   \tag{37}
\]

The two extra ratios relative to (28) are \(m_{c'}/m_c\)
and \(m_c/m_{c'}\). Each is paid only at the final endpoints.
There is no scale-ratio cost raised to the number of corrections.
The first line gives \(\mathcal K_{-2}\) and its weighted versions;
the second is the physical column bound. The bare and current
word tails obey the same inequalities with bounds tending to zero.

## 6. The lift and its physical transpose

At one expand

\[
 H_1^J=G_1^JQ^*q_{1,J}\ell^{-1}
 \tag{38}
\]

using the words just constructed. The successive spaces, read from
right to left, are

\[
 B_0\xrightarrow{\ell^{-1}}B_1
 \xrightarrow{q_{1,J}}B_3
 \xrightarrow{Q^*}F_3
 \xrightarrow{G_1^J}E_1^\beta .                        \tag{39}
\]

No scale mismatch occurs. Submultiplicativity gives an absolute
majorant at most \(C g_0q_*/[(1-a)(1-e)]\), with the same tree
reserve. If \(h_w(b,c)\) is a lift density word, define its cell
majorant \(k_w(y,c)\) to include all three quantities

\[
 m_c^4\left(
  m_y\sup_{b\in y}|h_w(b,c)|+
  m_y^2\sup_{b\in y}|\nabla_bh_w(b,c)|+
  m_y^{2+\beta}[\nabla_bh_w(\,\cdot\,,c)]_{\beta,y}
 \right).                                                    \tag{40}
\]

The source column \(B(c)=v\), \(|v|=1\), is a normalized \(B_0\)
datum. Applying (39) to it proves (40), including its row and
column sums with weights. In particular,

\[
 |H_1^J(b,c)|\le
       C m_y^{-1}m_c^{-4}e^{-\delta d(y,c)},\qquad b\in y.
 \tag{41}
\]

This is \(\mathcal K_{-1}\). The other readouts in (40) give
\(N_\beta(H_1^JB)\le C|B|\), and the weighted version follows by
multiplying the endpoint majorant by \(p(y)/p(c)\).

The physical transpose can be checked directly, without a dual
Hölder claim. For \(f\in F_3\), each word gives

\[
 \begin{split}
 m_c^4|(h_w^Tf)(c)|
 &\le \sum_y\sum_{b\in y}\eta^4
       m_c^4|h_w(b,c)|\,m_y^{-3}\|f\|_{F_3,y}\\
 &\le C\sum_y k_w(y,c)\|f\|_{F_3,y}.
 \end{split}                                                   \tag{42}
\]

The last inequality uses the cell volume bound
\(\sum_{b\in y}\eta^4\le C m_y^4\).
The factors \(m_y^{-1}\), \(m_y^{-3}\) and \(m_y^4\)
cancel exactly. Sum (42) using the column majorant in (40).
It proves \(H_1^{J,T}:F_3\to B_4\), including arbitrary admitted
weights and absolute word tails.

The identities in item 3 of the theorem now follow from (27), (33)
and (38). They are used only at switches one. On the intersection
with B99's admitted true-current class, with the same rows and
Hessian, the account and B99 formulas identify these total operators
with Balaban's corrected operators. B99's unscaled lift equals
\(H_1^J\ell\); thus its induced-current weight \(-3\) corresponds
to weight \(-4\) in (42). B99's existing true-current proof is not
replaced by this port.

## 7. Words, switches and exact restriction

### 7.1 The words before switching

For \(G_1^J\), first choose the number of insertions in (24).
For each insertion choose its GW \(\Theta'_J\) branch or one of
the nine branches in (18). Choose every bare inverse, projection,
identity and current-leaf word. The word is the resulting finite
composition, including its finite physical index sums.
For \(q_{1,J}\), choose the number of factors in (34), expand
each factor by this rule and include all compression rows.
For the lift, use (38). These rules specify the assignment; an
unfolded inverse with the same total is not substituted.

Every word is analytic in the background on its full local PI read.
It is polynomial in its finitely many current leaves. This includes
the expansion of \(H^{J,T}J\), since GW constructs \(H^J\) by
current Neumann words before it is inserted in (10). A word needs
no background or current value outside the union of these reads.

For each primitive the outer geometric tail is bounded by
\(\sum_{n>N}a^n\) or \(\sum_{r>R}e^r\).
At fixed outer degrees, the finitely many factor families have
absolutely summable tails. Their products also have tails tending
to zero: first truncate the outer degree, then truncate each factor.
The positive majorants justify both steps and any regrouping.
The same bounds hold on compact subsets of the analytic domain.
Uniform convergence of analytic finite words therefore proves
analyticity of the sums. We can, and do, impose the inequalities
on \(j\le2j_*\), leaving an open neighbourhood of \(j\le j_*\).

### 7.2 Union tags and the spare tree exponential

For a primitive word \(w\), let \(F_w\) be its entire footprint,
including all branches and the identities of (14). Set

\[
 s_w=\prod_{\Delta:\,\Delta\cap F_w\ne\varnothing}s(\Delta).
 \tag{43}
\]

A cube occurs once in this product, regardless of multiplicity.
GW §5 constructs a tree through a representative in every cube
met by \(F_w\). Its Euler traversal, subdivided into arcs of
length at most half a cube side, gives

\[
 \#\{\Delta:\Delta\cap F_w\ne\varnothing\}
       \le16+64t_w/M_{\rm dec}.
 \tag{44}
\]

Each local insertion contributes its full carrier to this tree,
and each attached current branch is traversed as well. The cost
of joining those carriers is exactly the cost allowed in (9).
The identity words have their complete PI trees. On a torus,
lifting the traversal only overcounts cubes, as in GW.

Equations (4), (43)--(44) give

\[
 |s_w|\le e^{16\kappa _1}e^{\mu t_w}.
 \tag{45}
\]

The algebra was bounded with \(e^{2\mu t_w}\).
Consequently all its endpoint row and column estimates imply

\[
 \sup_y\sum_{w,z}|s_w|\,k_w(y,z)
               e^{\delta d(y,z)}e^{\mu t_w}
       \le C e^{16\kappa _1},                          \tag{46}
\]

and the corresponding supremum over the other endpoint. This
leaves a positive tree exponential after paying for the switches.
It also proves absolute switched tails and local uniform
holomorphy in \(s\). For each fixed lattice the monomials (43)
have finitely many switch variables; (46) is uniform in that
number. The same convergence argument as above proves the
claimed background and current analyticity.

This proves the \(Ce^{16\kappa _1}\) bounds for the two new
primitives. In the account lift (5), multiply the two primitive
majorants. The fixed averaging carrier is charged once. This
gives \(Ce^{32\kappa _1}\), including (40)--(42).
For the alternative single-union lift assignment, apply
(44)--(46) to the whole word of (38) to obtain
\(Ce^{16\kappa _1}\). Only the product assignment is (5).

At no point was \(QG_1^J(s)Q^*\) inverted. Nor was
\(I-G_0(s)K_J(s)\) inverted. The convergent series at one
generate the words; (43) then defines the new primitive sums.
Thus no factor \(e^{16\kappa _1}\) is paid once per Neumann
insertion, and the current ceiling is not coupled to \(\kappa _1\).

### 7.3 Common footprints and zero components

Suppose two admitted settings agree on a closed set \(W\), including
the current and every coefficient read there. For a word with
\(F_w\subset W\), PI gives the same local inverse words, cutoff
coefficients and local indices in both settings. The finite
averaging and current vertices agree on their complete carriers.
This also fixes every identity label in (14), each scale
multiplier and every branch attachment. Hence the word and its
tag are identical in both settings. Applying the converse
comparison gives equality of the restricted index sets.
Absolute convergence then gives equality of the restricted sums.

Every nonzero primitive word has a connected footprint: its
inverse pieces are joined at their shared leg or insertion
carrier, and each side branch attaches at that carrier.
If switches vanish outside a retained collection, a surviving
word meets only retained cubes. Its endpoints therefore lie in
one retained component. Its coefficient reads also stay in that
component. This proves separation for \(G_1^J\) and \(q_{1,J}\).

For (5), the untagged \(Q^*\) must also be accounted for.
Every coarse word in (34) starts and ends with a \(q_0\) word.
PI's endpoint margin is \((2L+1)M_t m_c\) in base-point
coordinates. It contains the full averaging carrier at \(c\):
the latter has fixed double-block extent, and \(M_t\ge4L\).
Thus any fine point coupled to \(c\) by the intervening \(Q^*\)
lies in that same retained component. The other primitive
cannot then connect it to another component. Multiplication by
\(\ell^{-1}\) does not change the component. This proves
separation for (5) and its physical transpose too.

In particular, if all switches vanish, every new primitive and
the lift vanish. There is no surviving empty primitive term.
This argument proves primitive and lift locality only. It does
not use the chart's representation identity at nontrivial
switches, and does not supply the chart current's missing local
diagonal assignment described by M3.

## 8. Constant order

All choices are existence choices through the displayed inequalities.
None requires numerical evaluation.

1. Fix \(N,L,\beta _0\), the gap \(\epsilon\) in (1), and GW's
   finite collection of ordinary, scalar divergence and vector
   Hölder-source spaces. Fix its flat tile, flat gap, flat
   estimates and torus room.
2. Make GW's common enlargement of PI's flat, comparison and
   cutoff constants before choosing \(M_t\). Retain the resulting
   \(M_t,r_N,\widehat r,D_X,\theta_Z,\mu\), coefficient reads and
   the background and averaging radii. No enlargement of the
   admitted background class is made.
3. Use (8) for the stronger tree reserve \(2\mu\). Fix the identity,
   smooth-partition and carrier constants, with junction cost
   \(e^{34\mu c_\iota}\). Recompute the finite GW majorant constants
   with that cost and choose a preliminary positive current
   ceiling for its existing \(H^J\) family.
4. Fix \(H_T^*,C_{\rm av}\), the constants in (17),
   \(C_\Pi,C_K,q_*,C_{\rm comp}\). They have uniform upper bounds
   for \(0<\lambda\le\mu/4\) above the required geometry floors.
   Choose \(j_*>0\), with \(2j_*\) below the preliminary ceiling, so that
   for \(0\le j\le2j_*\)
   \[
        C_Kj\le\tfrac14,\qquad
        C_{\rm comp}\frac{C_Kj}{1-C_Kj}\le\tfrac14 .
   \]
5. Choose a positive common \(\lambda\le\mu/4\) below the retained
   GW endpoint rates, then \(0<\delta\le\lambda/4\). Impose GW
   (P5) at every rate used, the scale-ratio floor of (35), and
   PI's separation, divisibility and torus floors. As in GW's
   order, the majorants used before this step are uniform above
   those floors. The floors do not change the preceding constants.
6. Only now give \(\kappa _1\) and choose the decoupling cube side
   satisfying (4). The finite junction range \(c_\iota\) includes
   the carriers used in this port; whole PI identity footprints
   are paid as pieces, not as an unbounded local junction.

The final \(j_*\) precedes \(\kappa _1\). The increased carrier
costs in step 3, not a later switch-dependent current reduction,
pay for the extra tree reserve. Constants depend on the fixed
group, \(L\), the exponent gap and the common PI/GW choices.
There is no claim uniform in \(N\), or as \(\beta _0\uparrow1\).
This completes the proof of Theorem GW1 as a corollary of the
specified PI/GW word algebra. \(\square\)

## 9. Scope and account lines supplied

This port supplies the remaining first-order/coarse-kernel branch.
It proves neither a Laplacian estimate for \(G_1^J\) nor the
general nonlinear layer's stronger graph assertion. It does not
prove physical positivity at arbitrary independent current, a
precision or root family, admission of an arbitrary account
domain, all-torus covariance of a different assignment, or
equality with prescribed sheets merely from equality at one.

The B99 true-current result and its boundary qualifications are
retained. The new word estimates do not discharge B99-W's further
independent-current precision and accretivity obligations. They
also do not repair M3 or define \(P_1(s),m_H(s)\) for the general
layer. The M3 source passages are `layer-thm-part.md` 1440--1461
and `gates/layer-part-ref.md` 187--274. No representation,
constraint or inverse identity is carried through switching.

The account supplied here is **a written restricted port**, not an
assertion that its conditional (J7) proof was absent:

| CA-I lines | Portion supplied on the admitted PI/GW class |
|---|---|
| 13758--13771, as invoked by (J7) at 13783--13784 | The J2 readouts, J3 coarse inverse and J4 lift for \(G_1^J,q_{1,J},H_1^J\), preserving the Laplacian exclusion. |
| 13850--13874 and 13944--13955 | The left/right derivative allocation and fixed Hölder gap for the additional \(\Pi^T\Theta_J\Pi\) insertion, with complete termwise row and physical column accounting. |
| 13896--13920, as invoked by 13954--13955 | The small coarse compression, its inverse series, density normalization and lift construction for the new branch. |
| 13957--13977 | The new branch's analytic local words, all side branches, absolute convergence and coarse-inverse concatenations. |
| 15278--15314 | Expansion at one, primitive union tags, and the account's subsequent product assignment for \(H_1^J(s)\). |
| 15322--15324 | \(Ce^{16\kappa _1}\) for the new primitives, with the composite lift bound stated separately. |
| 15333--15337 | Component separation and equality at one for these primitives and their lift. No general chart-current separation is inferred. |

This derivation has not received an independent mathematical check.
