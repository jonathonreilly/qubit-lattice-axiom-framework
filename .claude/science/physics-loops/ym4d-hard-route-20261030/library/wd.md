# Window data at the preparatory site

Provenance: Research text begun 2026-11-05 in checkout `ce884021928a36cf1671f2efae1e5628e2792ef5`; source account by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, revision `31a47c543775`; Balaban's multiscale work is credited wherever used. This note grants no audit or retained status; computational runs may guide or refute but do not discharge proof obligations.

## Source and current checkpoint

CA-I, CA-II and CA-III mean the three `theorem_0_complete_account_raw_*.tex` files at the upstream revision above. SA means `YM4_sketch_500.tex`. The existing `/tmp/sa_*.tex` copies have the same hashes recorded in the pinned repository:

| Source | Lines | SHA-256 |
|---|---:|---|
| SA | 32992 | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | 166711 | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | 145624 | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| CA-III | 111583 | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

The retrieval log is `/tmp/wd-lane-20261105/`. Its searches cover the four requested phrases in all three account files and `sa-index/ca-full/index.tsv`. File searches and hashes are navigation only.

## The assumption actually printed

The correlation theorem, `5.1:thm-correlation-theorem`, says at CA-II:2808–2812:

> Assume further the statement on the summation of boundary terms at finer zones.
> Assume also the source-free statement on the resummation geometry at the preparatory site,
> which Definition~\ref{5.1:def-admitted-inputs} admits as a further source-free hypothesis,
> and the statement on the window data of the blocks at the preparatory site, on which the
> relative bound for the boundary-type terms depends and whose proof is outstanding.

This paragraph supplies neither a label nor a displayed mathematical statement for the last antecedent. CA-II:2376–2384 gives its intended consumer: the relative theorem for the boundary terms born at an operation \(\mathbf R\), with bound
\[
 \mathfrak N^{A,\mathbb C}(\mathbf B'(A))
 \le e^{\lambda_\theta}c_1^\flat
       e^{-(1+\beta_s/4)\kappa d_k(A)}.
\]
Its stated route uses the window lemma, own-level membership, the remainder theorem, and closure of paired charts. The distinct geometric resummation antecedent is retained.

Two precise readings must be kept separate. CA-I `4.21:def-datum-hypothesis`, 68420–68484, asks for an inherited-data factor bounded at **every** block, for values and differences. Its Route isolates residual blocks reached by the fivefold enlargement but not the probe. CA-II `5.5:not-interpolated-box-field`, 42622–42748, also reads analytic admission of the windowed minimiser and a contour-smallness bound from the unlabelled window statement. A proof of a numerical factor alone cannot silently supply these domain assertions.

## Comparison before proof

| Existing text | What it supplies | What remains for this item |
|---|---|---|
| [P6](port/p6-correlation.md), C-preparation and W5 | The correlation implication and the weight-lemma deductions on their admitted window/source domains. | C-preparation explicitly retains the outstanding antecedent. W5(a1) starts by reading a defining source-domain clause. |
| [PDA](pda.md) | Geometric admission (A1) of the prepared nest, including one-layer gaps. | No analytic admission of the source or of a windowed minimiser. |
| [GEOH](geoh.md) | History, waiting and counting implications under its stated selectors and quarantine conventions. | No field-domain theorem. Its own Result retains analytic realization and stage matching. |
| CA-I `4.18:thm-preparatory-boundary`, 54985 onward | Transfer of the stage bounds with profile compensation. | It assumes Balaban's stage theorem, including its spaces and analytic bounds; it does not establish this missing window input. |

The additional comparison with [MU](mu.md), §§7–8 and its frozen scope, is important. It supplies the literal-frame minimizer identity on its admitted complex input polydisc, including all determining rows. It does not check the other data radii used at CA-II:35714. Its restriction identity preserves the actual inner averages; it does not say that these averages are independent of the outer datum. Its separate qualification about the port of CMP 98 Proposition 4 is also retained.

Two later passages of the account do not close this gap either. CA-I 4.29:prop-window-minimiser, 148788–148871, assumes regularity, restriction, and real-point membership, and requires the **whole** window to lie in the top stratum of its truncated tower. CA-I 4.28:prop-kernel-membership, 144962–145138, assumes regularity of the extended box configuration in hypothesis (I). Its proof of (b), 145152–145182, expressly uses (I) by statement. Neither passage supplies an independent proof of that regularity for the windows at issue.

## The precise inherited-data statement and its consumers

Here is the closest labelled statement, in the account's notation, rather than a replacement by a single-scale statement. The account itself identifies it as an input of the correlation theorem at CA-I:68455–68459.

At stage \(n\) of \(\mathbf R_k\), let \(R_n\) be the current collar and let
\[
 D_\square=d^\wedge(\square,R_n),\qquad
 s(\square)=\max_{\Delta\cap\tilde\square^5\ne\varnothing}\mathsf r_0(\Delta),
 \qquad \mathsf l^2(\square)=L_\circ^{6s(\square)}\mathfrak d(\square).
 \tag{1}
\]
All these objects, and the two readings of \(\mathfrak d\), are those of CA-I 4.21:def-local-data-factor, 68168–68246. Specifically, for one expansion the comparison quantity is
\[
 L_\circ^{6s(\square)}\mathfrak n_0
   \{\vartheta(\square)+\mathfrak p_j{\bf1}_{\square\text{ meets }R_n}\},
 \qquad
 \mathfrak n_0=c_\alpha C_R(E_0+1)e^{C_2\kappa_1}.
 \tag{2}
\]
For a difference of two expansions on one scaffold it is the same expression with
\[
 \mathfrak n_0|_1=c_\alpha C_Re^{C_2\kappa_1}
 \tag{3}
\]
in place of \(\mathfrak n_0\), multiplied by the **difference-size constant** specified there, a member of \(\mathsf l_{n+1}\). This is not a bound obtained by adding the sizes of the two expansions. When that size is zero the assertion is read in its undivided form. If \(\tilde\square^5\cap\mathcal W=\varnothing\), the definition sets \(\mathfrak d=1\).

**Exact labelled target, CA-I 4.21:def-datum-hypothesis, 68420–68453.** There is \(C_{\rm dat}\ge C_{\rm dat,pr}\), fixed before \(\gamma\), such that, at every stage of every \(\mathbf R_k\), and at every block of the cover,
\[
 \boxed{\quad
 \mathfrak d_v(\square),\ \mathfrak d_{\delta v}(\square)
 \ \le\ 1+C_{\rm dat}e^{\delta_PD_\square/8}.
 \quad}                                                    \tag{WD}
\]
The subscripts merely distinguish the two readings of the account's letter \(\mathfrak d\). The second is for
\(\delta v=v^{\mathsf B}-v^{\mathsf A}\) on a common scaffold, with normalization (3). The constant cannot depend on \(k,n,K\), the volume, the ages of arrests, or the particular machines.

For the analytic reading fix the next stage, put
\(\mathfrak B=\mathbb B_k^{(n)}\), \(\mathfrak B^+=\mathbb B_k^{(n+1)}\), and
\(\square_0=\tilde\square^5\). CA-II:42622–42658 reads the source through its arrangement as
\[
 (\mathbb U,\mathbb J,b,\sigma)\in
 \mathfrak G(\mathfrak B^+)\subset\mathfrak G(\mathfrak B)
 \subset\mathfrak K_P,\qquad
 a_\flat(\mathbb U)\le\gamma_0^{(k)}\le\gamma_0^\top ,
 \tag{A}
\]
where the first two classes carry the auxiliary coordinates, and the last membership concerns the configuration pair. Here
\(\mathfrak K_P=\mathfrak K_{109}(\mathfrak B;\gamma_0^{(k)})\) is the account's kernel class,
\(\gamma_0^\top=\bar\gamma_0(\mathsf t_\gamma)\),
\(|\sigma(\Delta)|\le e^{\kappa_1}\), and
\(\|b\|_\infty\le1.1C_1\delta'_{\mathsf j}\).
It then uses \((\mathbb W,\mathbb J)\in\mathfrak K_P\) for the box minimizer extended by \(\mathbb U\) outside \(\square_0\). The inclusions supplied by the source-arrangement statement are retained as that statement's input; neither the missing kernel admission nor the minimizer's complex admission is proved by the scalar inequality (WD).

The use of (WD) is pointwise in blocks, **before** summing them. It is not enough to prove an integrated estimate, an estimate only away from exceptional blocks, or one with a different normalization. The following records the literal occurrences of its definition/equation labels, grouped by their use; the defining passage and Route are included above.

| CA-I lines | Use of the inherited-datum hypothesis |
|---|---|
| 68486–68561 | 4.21:cor-near-group-weight consumes (WD), for both readings, to retain decay \(e^{-3\delta_PD_\square/8}\). |
| 68697–68806, 68957–69002 | 4.21:lem-datum-depth-shares distinguishes its assumed block form from its sufficient discounted form, and proves the latter implies (WD). |
| 69004–69167 | The residual-configuration remark keeps the level-\(k\) exception and explains why a discount on responding terms is not yet a discount on hypothesis data. |
| 69172–69185 | \(C_{\rm dat}\) enters the small-field constant \(\mathfrak s_J\). |
| 69594–69690 | The group-total proposition assumes both readings; its old-block constant includes the inherited factor even when \(s=0\). |
| 69816–69820, 69890–69964 | The one-anchor sum uses (WD) at old blocks and at window blocks; the latter include exceptional blocks. |
| 70260–70277 | The per-point total uses the near-group corollary with \(1+C_{\rm dat}\). |
| 70537–70585 | The machine-difference lemma assumes the difference reading. It explicitly declines to infer linearity of the near-group total from linearity of the later weight sums. |
| 70950–70968, 71071–71081 | Format invariance assumes (WD) in (iii) and carries it into its first substitution. |

The grep for the definition and equation labels has no occurrences in CA-II or CA-III. Their prose window assumptions remain as recorded above. In particular the data-factor majorant in CA-II:13655–13895 is a deduction under membership, remainder and paired-chart inputs. Its numerical factor is not identified by definition with (1); using it as a proof of those inputs would reverse the implication.

## What the stated Route already proves

This subsection ports the reductions of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; it is not a new proof of their lemma. Balaban supplies the underlying regularity and blocking construction.

For \(\Delta\in\mathcal W\), let \(t(\Delta)\) be its raiser's step and \(\mathsf r(\Delta)\) its frozen raise. CA-I 4.21:def-arrested-attempts, 64796–64969, gives
\[
 \operatorname{lev}\Delta\le t(\Delta),\qquad
 \mathsf r_0(\Delta)=0.
 \tag{4}
\]
Put \(w=M/M_1\), \(\rho=1+D_\square/w\), and \(n_0=\operatorname{zone}(\square)\).
The scope clause of 4.21:lem-datum-depth-shares gives, whenever the large window meets \(\mathcal W\),
\[
 \rho\ge\check R_k-4,\qquad k-n_0+1\le N_*+\rho.              \tag{5}
\]
This includes a block at \(n_0=k\) over a sibling exiting at the last stage. The account's proof, CA-I:68876–68915, checks this exception explicitly.

Write \(p=6r_{\rm pr}\) and \(c_u=\log(1+3\lambda u+2c_2)\). The same lemma supplies the share bound
\[
 L_\circ^{6\mathsf r(\Delta)}
 \le L^{12}\{\check{\mathsf T}_k+3+c_{k-t(\Delta)}\}^{p}.
 \tag{6}
\]
For \(t(\Delta)\ge n_0-2\), its part (ii) pays this share from (5). Its constant, denoted \(C^{\mathtt a}_{\rm pr}\) there, is
\[
 \begin{split}
 C_{\rm pr}&=\sup_{\rho\ge1}
  L^{12}\{\rho+7+c_{\mathsf n(\rho)}\}^{p}e^{2-\rho},\\
 \mathsf n(\rho)&=C_N2^{r_{\rm pr}}(\rho+4)+\rho+4 .
 \end{split}                                               \tag{7}
\]
It is the \(C_{\rm dat,pr}\) referred to in the target. Finiteness and \(C_{\rm pr}\ge1\) are part of the source calculation.

There is a qualification in the Route that must survive the port. Parts (ii)–(iii) turn share estimates into an estimate on the actual \(\mathfrak d\) **under their block-form assumption**
\[
 \mathsf l^2(\square)=
 \max\{L_\circ^{6s(\square)},
       \max_{\Delta\in\mathcal W,\ \Delta\cap\tilde\square^5\ne\varnothing}
                L_\circ^{6\mathsf r(\Delta)}\}.             \tag{8}
\]
The lemma is not an unconditional analytic proof of (8). Thus even the nonresidual conclusion must retain this qualification if one uses that version of the Route.

The residual shares have \(t(\Delta)\le n_0-3\). Such a cell misses the probe \(\tilde\square\); its age \(n_0-t(\Delta)\) has no upper bound from (5). The account's residual discussion, CA-I:69004–69167, places the responding terms inside \(\tilde\square^2\) and says that only the larger hypothesis cube reaches the older structure. This is a statement about the carriers of the terms, not independence of the minimizer from its boundary data.

The already-proved sufficient route is part (iv):
\[
 \mathsf l^2(\square)\le
 2\max\left\{1,\quad
    \max_{\Delta\cap\tilde\square^5\ne\varnothing}
    L_\circ^{6\mathsf r(\Delta)}
        L^{-a(n_0-\operatorname{lev}\Delta)_+}\right\},
 \qquad a>0\text{ fixed before }\gamma.                    \tag{9}
\]
Under (9), the account proves (WD) with
\[
 C_{\rm dat}=1+2^{p+1}(1+\mathfrak w_a)C_{\rm pr},
 \qquad \mathfrak w_a=\sup_{u\ge0}c_u^pL^{-au}<\infty .
 \tag{10}
\]
Its displayed \(L^{4(i-\ell)}(s_\ell/s_i)^{4+\alpha'}
=L^{-\alpha'(i-\ell)}\) pays a **term** of level \(\ell\).
CA-I:69046–69059 explicitly leaves unproved the transfer of this discount to an old cell occurring only in the hypothesis cube. That transfer is not made here by a change of notation.

## A weaker sufficient estimate

Here is a new, conditional reduction used in the attacks below. It weakens the geometric discount requested by (9) to a logarithmic age discount. It does not assert that actual window data obey it.

For an inherited cell put
\[
 u_\Delta=(n_0-t(\Delta))_+,\qquad
 F(u)=(1+c_u)^{-p}.
 \tag{11}
\]
Suppose that, for the two normalized local data factors separately, the actual window construction satisfies
\[
 \boxed{\quad
 \mathsf l^2(\square)\le K_{\rm win}
 \max\left\{L_\circ^{6s(\square)},\quad
   \max_{\substack{\Delta\in\mathcal W\\
                         \Delta\cap\tilde\square^5\ne\varnothing}}
        L_\circ^{6\mathsf r(\Delta)}F(u_\Delta)\right\},
 \quad}                                                    \tag{S}
\]
with the maximum over an empty set omitted and \(K_{\rm win}\ge1\) fixed before \(\gamma\). Then (WD) follows with
\[
                 C_{\rm dat}=K_{\rm win}C_{\rm pr}.         \tag{12}
\]

**Proof of this implication.** If the window misses \(\mathcal W\), use the defining \(\mathfrak d=1\). Otherwise set
\[
 A=\check{\mathsf T}_k+3+c_{k-n_0}\ge1.
\]
The elementary inequality
\[
 1+3\lambda(a+b)+2c_2
 \le(1+3\lambda a+2c_2)(1+3\lambda b+2c_2)
\]
gives \(c_{a+b}\le c_a+c_b\). Since \(k-t(\Delta)\le k-n_0+u_\Delta\), (6) gives
\[
 L_\circ^{6\mathsf r(\Delta)}F(u_\Delta)
 \le L^{12}\left(\frac{A+c_{u_\Delta}}{1+c_{u_\Delta}}\right)^p
 \le L^{12}A^p.                                           \tag{13}
\]
The last inequality follows from \(A+c\le A(1+c)\) for \(A\ge1,c\ge0\). By (5) and the source computation in part (iv), CA-I:68985–68994,
\[
 L^{12}A^p\le C_{\rm pr}e^{\delta_PD_\square/8}.             \tag{14}
\]
Divide (S) by \(L_\circ^{6s}\ge1\). Equations (13)–(14), \(C_{\rm pr}\ge1\), and \(D_\square\ge0\) give
\[
 \mathfrak d(\square)
 \le K_{\rm win}C_{\rm pr}e^{\delta_PD_\square/8}
 \le1+C_{\rm dat}e^{\delta_PD_\square/8}.
\]
This proof applies to the difference only if (S) holds in normalization (3); it does not infer that premise from the value estimate. No enlargement of a complex domain is part of this argument. \(\square\)

This really asks for less screening than (9). For every fixed \(a>0\),
\[
 H_a:=\sup_{u\ge0}(1+c_u)^pL^{-au}<\infty.
 \tag{15}
\]
Indeed \(1+c_u\le C(1+u)\), and an exponential dominates this fixed polynomial, as follows directly from its power series using an integer power greater than \(p\). Equation (4) therefore bounds every inherited term in (9) by \(H_a\) times its term in (S); every noninherited term is at most \(L_\circ^{6s}\). Thus (9) implies (S) with \(K_{\rm win}=2\max(1,H_a)\). Recent shares have \(u_\Delta\le2\), so the proposed new discount on those shares costs only a fixed factor. The new work demanded by (S) is screening the arbitrarily old residual datum, in the correct norm and on the correct domain.

## Three attacks on the actual window estimate

These are attempts to establish the missing analytic estimate, rather than three re-runs of the account's share algebra. Each was taken far enough to identify an explicit unproved step. None produces a counterexample to Yang–Mills window data.

### Attack 1: absorb the frozen weight into the running smallness envelope

The account gives, CA-I:61664–61673 and CA-II:585–610,
\[
 \gamma_0^{(k)}=5\max_{j\le k}w_*(j)\bar\alpha_j
 \le5(1+\beta_0)^2\Psi(\mathsf T_k),
 \quad
 \Psi(T)=L^2(L+1)C_\Psi T^{r_{\rm pr}+q}e^{-T/2}.
 \tag{16}
\]
This is a useful absolute bound, including arbitrarily old radii. The attempted proof was to use (16) before taking the cubic near-group bound, thereby replacing the age-dependent factor in (6) by a universal small constant.

The normalization prevents that step. If an estimate has the form
\[
 |z|\le w_*(t)\bar\alpha_t,
\]
then the normalized cubic datum is bounded by \(w_*(t)^3\) when divided by \(\bar\alpha_t^3\). Replacing the right side first by \(\gamma_0^{(k)}/5\) instead gives
\[
 \frac{|z|^3}{\bar\alpha_t^3}
 \le \left(\frac{\gamma_0^{(k)}}{5\bar\alpha_t}\right)^3,
 \tag{17}
\]
which supplies no age discount. A bound on a product is not a bound on its dimensionless weight: for example \(w(T)=T^b\), \(\alpha(T)=T^q e^{-T/2}\), with \(b>0\), have \(w(T)\alpha(T)\to0\) but \(w(T)^3\to\infty\). This example tests the inference, not the account's actual fields.

A second version retained the best of the crude share estimate (6) and the smallness estimate (17). It still needs a relation between the normalized response at the **receiving** block and the old datum; neither scalar bound contains one. The denominator in (2) is prescribed and cannot be replaced by a uniform \(\gamma_0^3\) without changing (WD).

Nor can the age be absorbed by choosing \(\gamma\) again. At a fixed \(\check{\mathsf T}_k\) and fixed depth \(\rho\), the upper majorant in (6) grows with \(c_{k-t}\), whereas the proposed right side in (WD) is fixed. This shows that this majorant cannot itself prove the claim; it is not a lower bound on \(\mathfrak d\) and is not a counterexample. A finite-history choice \(\gamma=\gamma(k-t)\) would violate the order of choice.

**Failure point:** (16) proves absolute smallness but provides no factor \(F(u)\) in the normalized near-group estimate (S). The relevant missing fact is spatial transfer of data, not finiteness of the scalar supremum defining the absolute ceiling.

### Attack 2: remove the old cells from the hypothesis window

Since the responding terms miss the old cells, try replacing the large hypothesis cube by smaller cubes around their carriers, applying Balaban's Lemma 4 there, and identifying the local minimizers by MU. This attempts to prove an estimate stronger than (S), with no old contribution.

The account already proves a useful **conditional** local calculation in CA-II:35624–35827: a read unit with \(\nu\ge3\) can be put into a cube \(Q_v\) of at most seven cubes a side at level \(n-1\), with its one-layer enlargement using at most nine a side. Its data are controlled by the local weight \(w^\vee(y)\). This is why a uniform supremum over \(\tilde\square^5\) is unnecessary *after* the source/minimizer admission has been supplied. P6 ports this calculation; it is not redone here.

There are two ways to try supplying the admission, and their precise limitations differ.

First, apply the native-window theorem of CA-I 4.29. At a residual cell,
\[
 \operatorname{lev}\Delta\le t(\Delta)\le n_0-3.
 \tag{18}
\]
Consequently \(\tilde\square^5\not\subset\Omega_{n_0}\). The whole-window top-stratum hypothesis of 4.29:prop-window-minimiser fails for that proposed application. Lowering the native scale to the least level \(m\) met by the window repairs this particular inclusion, but introduces scale conversions: a layer estimate
\[
 \ell_m|A|\le a_m,\qquad \ell_m^2|\nabla A|\le a_m
\]
only gives, in the block's units,
\[
 \ell_{n_0}|A|\le L^{n_0-m}a_m,\qquad
 \ell_{n_0}^2|\nabla A|\le L^{2(n_0-m)}a_m.                \tag{19}
\]
Thus this conversion alone supplies losses, not (S). It must be supplemented by a response estimate. The single-scale glued-window proposition, CA-I:16992–17187, likewise assumes its rim regularity statement and its whole-window small gauge; (19) does not verify those hypotheses uniformly.

Second, use the restriction identity directly. In its valid domain it identifies the restriction of the large minimizer with a smaller minimizer **at the averages of that restriction**. It does not identify those averages with data independent of the excluded old cells. This distinction already occurs for a strictly convex quadratic problem. For
\[
 E(x,y)=\tfrac12(2x^2-2xy+2y^2),
\]
holding the exterior datum \(y\) fixed gives the unique interior minimizer \(x=y/2\). The observable \(x\) has interior support, while its minimized value depends on the exterior datum. This exact hand calculation refutes only the proposed support-to-independence inference. It is not a Yang–Mills counterexample.

The relevant complex-domain test reaches the same point. The proof of W5(a1), CA-II:35543–35569, reads a defining source clause; W5(a2), 35607–35613, then uses \((\mathbb W,\mathbb J)\in\mathfrak K_P\). The membership of the glued field is precisely one of the assertions read from the window statement at CA-II:42724–42735. Using these paragraphs to establish the antecedent would assume it.

**Failure point:** no established identity replaces the actual inner averages by controlled independent local data on the full filed complex domains. Restriction and local cube geometry alone do not give either this independence or the quantitative weakened replacement (S).

### Attack 3: interpolate the old datum and use decay of the constrained response

This attack retains the actual dependence and tries to estimate it. Work first in a fixed gauge chart in which the constraints are \(Q(x)=q\) and the action is \(S(x)\). If \(x(z)\) is a regular constrained critical point at datum \(q(z)\), with multiplier \(\lambda(z)\), differentiation gives
\[
 \begin{pmatrix}
 D_x^2(S+\langle\lambda,Q\rangle)&DQ(x)^{\mathsf T}\\
 DQ(x)&0
 \end{pmatrix}
 \begin{pmatrix}\dot x\\\dot\lambda\end{pmatrix}
 =
 \begin{pmatrix}0\\\dot q\end{pmatrix}.
 \tag{20}
\]
This follows by differentiating stationarity and the constraint, with the gauge modes removed. It is a finite-dimensional hand identity, not an assertion that this matrix is uniformly invertible for the actual window.

The attempted path is \(q(z)=q_{\rm ref}+z(q_{\rm old}-q_{\rm ref})\), where the reference removes the excess old datum in a buffer outside the responding carriers while keeping the actual local determining rows. If this path and its required complex thickening belong to one uniform admissible chart, the account's response machinery is the appropriate tool: CA-I 4.5:prf-chart-variation-decay, 14803–14870, gives exponentially decaying first variations **for admitted backgrounds and block data**, and CA-II 5.8:prop-local-decay and 5.8:lem-critical-stability give the corresponding weighted estimates under their regularity and size hypotheses.

The desired benefit can be quantified without claiming those hypotheses. Suppose the transported normalized contribution of an old cell were at most its share times \(C e^{-\mu u_\Delta}\), for fixed \(C,\mu>0\). Then
\[
 C e^{-\mu u}\le
 C\left[\sup_{v\ge0}(1+c_v)^p e^{-\mu v}\right]F(u),
 \tag{21}
\]
and the bracket is finite by the argument for (15). Thus even the much weaker (S) would follow from a summable, uniformly admitted response comparison, with the appropriate block/cell counting. Merely writing a pointwise kernel estimate is insufficient: one must retain its powers of the source and receiving length scales, its cell measures, and the sum over the changed rows.

The missing step is construction and admission of this interpolation. The actual means are nonlinear group averages with determining rows that can straddle the proposed buffer. Zeroing an exterior potential is not a mean-preserving operation. A correction requires a right inverse of the linearized averaging map and the nonlinear constraint correction; the account's bounds for those maps are on an already admitted background. No argument above supplies a uniform common chart for this proposed reference and the actual glued minimizer.

The problem is not remedied by continuity at each fixed history. The account's layered domains have margins proportional to \(2^{-h}\) at depth \(h\). For example the direct comparison discussed at CA-I:10057–10085 would have to pay a displacement \(cC_H\alpha_{1,m}\) from a margin
\[
 (1-\theta)\beta\,2^{-(k+1-m)}\alpha_{0,m}.                \tag{22}
\]
A bound without the same depth factor cannot do this uniformly: at any fixed positive ratio \(\alpha_{1,m}/\alpha_{0,m}\), the right-to-left ratio tends to zero as \(k+1-m\to\infty\). This disproves that bootstrap estimate, not the existence of a better one. Analytic continuation of an equality within a common domain cannot establish existence or a uniform radius for that domain.

Finally (20) along one machine's datum path does not establish the difference estimate between two machines. The latter requires the same admitted paired chart and the account's difference-size normalization. The triangle inequality gives the sum of the two value sizes, which need not vanish as the input difference size tends to zero. CA-I:70583 makes this distinction explicitly.

**Failure point:** the required history-uniform, mean-compatible complex interpolation and its normalized weighted response estimate have not been established. The published decay estimates can be applied once this admission is proved; applying them along the unverified path would assume the missing window regularity. This remains the failure even after weakening geometric screening to the logarithmic screening in (S).

## Constants, source checks, and endpoint

The order is the account's CA-II:2412–2442 and 2814–2863: first \(\theta_S,L,\delta\) and the early \((d,L)\)-constants; the coupling-comparison constants and exponents; then \(\kappa,\kappa_1,B_H,M_1,M\), the stated rim constants, \(\mathsf a,C_{\rm far}\), and the later analysis radii and constants; \(\gamma\) comes last. The small blocking constant is fixed after \(L\), with \(L_\circ^2\le L/3\). No proposed estimate sends a new condition back to \(L,M\), or \(\kappa_1\).

For the conditional implication (S) \(\Rightarrow\) (WD), \(p,\lambda,c_2,L\) and hence \(C_{\rm pr}\) are fixed already. A proof of the window estimate must supply \(K_{\rm win}\) from its preceding analysis constants, independently of \(C_{\rm dat}\), before the final \(\gamma\), uniformly over histories. Then choose (12), and impose the existing later small-coupling conditions at that value. This is a requirement on the open analytic lemma, not an established choice of \(K_{\rm win}\). Taking a supremum only over finitely many stages or selecting a new ceiling for each age is not allowed.

The source roles have been kept separate:

- The exact correlation assumption, its boundary-term consumer, the inherited-datum statement, its Route, the share reductions, and their normalization are from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at the pinned revision.
- Balaban's CMP 109 Lemma 4 and the minimizer/propagator results are used only in the hypotheses and scope stated by the account and MU. The available CMP 109 text at lines 1610–1620 confirms the Lemma 4 input-space requirement and analyticity conclusion. Its OCR equations are damaged; no formula in this note is transcribed from that OCR.
- The reduction (11)–(15), the attempted transfers, the quadratic diagnostic, and identity (20) are this note's hand arguments. They prove only the explicitly conditional implication and the stated limitations of those attempts.

The outline index was consulted before source excerpts; the nearby outline restriction sketch (SA:9770–9792) and history/window discussion (SA:17415–17449) do not replace the account's domain hypotheses. The more detailed CA-I index for 4.12–4.19 leads to the geometric PDA and preparatory-boundary statements compared above. No index label saying “PROVED” was used to remove a hypothesis printed in the corresponding statement.

Checkpoint for continuation: the exact target is (WD), with the additional analytic readings at CA-II:42622–42748. The three failed transfers are absolute-smallness normalization, local replacement by restriction, and interpolated response without a proved common domain. The next decisive task is the single window lemma below. Its analytic assertion must be proved on the actual filed source, and its estimate must be proved in both normalizations; a real-point calculation or a new summation of already-admitted terms does not suffice.

The source hashes at the start fix the evidence. Searches and source extraction are navigation; no computer-assisted calculation was used to discharge a mathematical step. This note changes no audit, claim, ledger, prompt, or status file.

## Result

**Open lemma**

**Uniform analytic window admission and screened inherited datum.** Use the construction and source domains of CA-I 4.21 and CA-II:42622–42718, with the correlation theorem's standing inputs and parameter order, without assuming its outstanding preparatory-window statement. Retain the source-arrangement statement as an input. Results whose hypotheses include window admission, own-level membership, or paired-domain closure are available only as implications; their domain conclusions are not additional premises of this lemma. At every stage of every \(\mathbf R_k\), for every block \(\square\) of zone \(n_0\), and every actual filed source
\((\mathbb U,\mathbb J,b,\sigma)\in
\tilde U_k^{(n+1)c,\Sigma\flat}(\hat X)\), \(\hat X\supset\tilde\square^5\), the window configuration
\[
 \mathbb W=U\!\left(\mathfrak B^+(\tilde\square^5),
                              M^\cdot(\mathbb U)\right),
 \qquad \mathbb W=\mathbb U\ \text{off }\tilde\square^5 ,
\]
has single-valued holomorphic dependence throughout the specified source domains, with
\[
 (\mathbb U,\mathbb J),(\mathbb W,\mathbb J)\in\mathfrak K_P,
 \qquad a_\flat(\mathbb U)\le\gamma_0^{(k)}\le\gamma_0^\top ,
\]
in the notation and at the radii of (A). On those domains, including the common-scaffold paired readings, its near-group local data factors satisfy (S), both for one expansion and for a difference normalized as in (3), with one \(K_{\rm win}\ge1\) fixed before \(\gamma\), independent of \(C_{\rm dat}\), and independent of stage, volume, cutoff depth, and arrest age.

This is one sufficient window lemma, with an analytic admission clause and a bound for the same window construction. Its estimate implies the exact labelled target (WD) by (11)–(14), with \(C_{\rm dat}=K_{\rm win}C_{\rm pr}\), including the level-\(k\) exceptional band. Its admission clause supplies the glued-window membership used by the subsequent response arguments; their other printed hypotheses remain in force. It is **not proved here**. No counterexample to the account's statement has been obtained, and no proof of the correlation theorem's full window antecedent or of T0 is claimed.
