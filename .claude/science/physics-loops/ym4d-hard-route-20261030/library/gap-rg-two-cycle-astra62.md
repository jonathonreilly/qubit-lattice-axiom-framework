# Repo search

Lane `2f6fc4b84704`. The Markdown/TeX search covered `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). Terms included two-cycle routing/response, independent cycles, mixed plaquette, disconnected corner, normalized block, figure-eight holonomy, independent conjugations/inversions, forest/product Haar and commutator trace.

| Relevant hit | Statement and reach |
|---|---|
| PRs 10114/10133, `RD_LOG.md` 316, and PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 | The tree change of variables preserves product Haar with the anchors fixed. The single-loop product convolution dominates a positive rank-one form on the centered loop. Their conclusions concern a tree change of variables and one loop, respectively. [November 8 digest](prior/repo-search-2026-11-08.md) |
| Lane, rows 1418 and 1421 | Row 1418 constructs the Wilson site tensor and four-direction fusion. Row 1421 gives the mixed-label coefficient as its boundary weight times a Wilson expectation. Its formula (3) uses one chord per component. Its last section proposes the present test. [Row 1418](gap-rg-step-sizing-astra62.md) · [Row 1421](gap-rg-signed-inclusion-astra62.md) |
| Lane, Lemma FOREST §3.4 and row 1339 | Forest links have product Haar marginal. An isolated cycle retains its holonomy up to root conjugation. The two squares here share that root. [Forest lemma](gap-ps-disint-max.md) · [Sparse-cycle reduction](gap-solve45-astra62.md) |

The statement query on the five refs hit only apparatus graph counts in `record_attached_kernel/PROPOSAL.md` and the two `mediated_finite_cut_interface*` files. The axis-interchange/quadrupole query hit a planar $2\times2$ loop in `INDUSTRIAL_SDP_BOOTSTRAP_LATTICE_BRACKET_NOTE_2026-05-03.md` 58. The doubled-strip, relative-axis and alternating-word query returned no hits. The target-specific prior file is absent, FINISH 1424 has no separate “Repo prior work” line, and the [registry](open-registry.md) search found no competing owner.

## Row 1424. Connected two-square reading

**Reject the single-fundamental reading.** After the disconnected colour routing is removed, all four entries of the normalized two-routing matrix vanish throughout $[2,513/256]$. A rooted coordinate interchange cancels the signed term even with asymmetric exterior labels. The same cancellation holds in five dimensions. A product-of-marginals subtraction retains one scalar covariance, evaluated in (5), and still gives zero in the colour-exchange channel.

The plan saved at creation was to check prior coverage, freeze both routings and their denominator, compute the connected matrix, then test the group and dimension dependence. This is an author-only research argument and grants no status.

In the Sussman–Alpoge snapshot supplied as `31a47c543775`, SA 2195–2243 gives the character coefficient and Bessel bounds, SA 2773–2781 the quaternion half-trace, and SA 4075–4084 the all-level invariant-class obligation C4. SA 8519–8549 counts the row and column weights for classical curvature averaging. CA-I 4209–4239 quotes Bałaban's ultraviolet stability theorem with every effective coupling at or below its small ceiling. The calculation here uses the bare block at the stated intermediate coupling. Credit for the outline and account belongs to Ethan Sussman and Levent Alpoge, writing with Claude and Codex. [Index, chunks 02, 03, 04 and 08](sa-index/README.md) · [Obligations](sa-index/obligations.md) · [Bałaban quotations](lit-balaban.md)

## The two exterior routings

Use $B_d=\{0,1\}^d$, with distinct exterior bonds, and $\beta\in I=[2,513/256]$. Orient $P$ along $0,e_1,e_1+e_2,e_2,0$ and $Q$ along $0,e_3,e_3+e_4,e_4,0$. Write $H,K$ for their holonomies based at $0$, and $q(g)=\operatorname{tr}(g)/2$. Let $R_B$ be the contraction of row 1418's site tensors over all internal bonds, leaving all exterior bonds open. Its all-vacuum coefficient is $z_B$. For product probability Haar $dU$ on the internal links, row 1421 gives

$$
 w_B=\prod_{f\subset B_d}\frac{\exp(\beta q(U_f))}{A(\beta)},\qquad
 A(\beta)=\int\exp(\beta q(g))\,dg,\qquad
 z_B=\int w_B\,dU,\qquad d\mu_B=z_B^{-1}w_B\,dU .
$$

All internal faces have their full Wilson weights, including $P$ and $Q$. The positive density gives $z_B>0$. The internal character sums converge absolutely by GL4, as in row 1421. The following labels fix only exterior slots. Each occupied exterior face has spin $1/2$. Directions such as $-3$ denote $-e_3$.

| Location | Occupied faces | Intertwiners on the exterior bonds |
|---|---|---|
| The four edges of $P$ | For each edge $e$, the mixed square between $e$ and $e-e_3$ | At its three nonroot vertices use the unit bivalent tensor on the outward $-3$ bond. |
| The four edges of $Q$ | For each edge $e$, the mixed square between $e$ and $e-e_1$ | At its three nonroot vertices use the unit bivalent tensor on the outward $-1$ bond. |
| Outward bonds at $0$ | The three outward/outward faces spanned by $(-3,-1)$, $(-1,-2)$ and $(-2,-3)$ | The $-2$ bond is bivalent. Each of $-3$ and $-1$ has two mixed slots and two slots of this outward triangle. |

Every other exterior slot is zero. The mixed graph has eight edges and seven vertices, hence two independent cycles. At both boundary ends of every occupied mixed face the indicated spin agrees. The triangle gives two paths between the four-valent bonds, one direct and one through $-2$. Direct the triangle from $-3$ to $-1$, then through $-2$ back to $-3$. Direct each mixed strip along its specified base loop. Each bivalent tensor is $\delta/\sqrt2$ in its oriented $V,V^*$ slots, where $V=\mathbb C^2$. Since the SU(2) character equals its value on the inverse, each face orientation can be chosen this way, with the dual convention on its other end.

At each four-valent bond denote the two loop slots by $i,j$ and the two triangle slots by $k,l$, one incoming and one outgoing in each pair. Use the two unit invariant tensors

$$
 p_{ij;kl}=\tfrac12\delta_{ij}\delta_{kl},\qquad
 r_{ij;kl}=\tfrac12\delta_{il}\delta_{kj}.
$$

These are the singlet matchings of row 1421, here used on two outward bonds. The first closes the loop and bridge separately. The second routes the loop through the bridge. Contracting $p$ with $r$ identifies all four indices, giving $2/4=1/2$. Each self-contraction leaves two free indices and gives $4/4=1$. In an orthonormal bond basis use $p$ and $t=(2r-p)/\sqrt3$ and obtain $r$ by the displayed linear combination. With the other slots fixed, contraction against independent choices $p,r$ at the two bonds defines the $2\times2$ matrix $M$ of the tensor $R_B/z_B$. Its Wilson and bivalent prefactor is

$$
 C(\beta)=2^{-7/2}\, b(\beta)^{19/4},\qquad b(\beta)=2 I_2(\beta)/I_1(\beta).
$$

There are eight half weights from mixed plaquettes, three quarter weights from outward corners and seven unit bivalent tensors. The factors $1/2$ in $p,r$ are still inside the matrix contraction. The same definition works in $d=5$ by placing both squares at $x_5=0$ and setting the added exterior slots to zero. All fifth-direction internal plaquettes remain in $w_B$ in that case.

## The matrix and the disconnected corner

Undoing the internal Haar sums as in row 1421 leaves one fundamental matrix on each of the eight mixed edges. The three nonroot bivalent tensors on each strip multiply its four directed matrices in cyclic order, leaving $H$ or $K$ at the root. In the oriented convention above, the two root choices insert $L_p(G)=q(G)I_2$ and $L_r(G)=G/2$ on the bridge. This follows by summing $G_{ji}$ against the two displayed Kronecker tensors, with the bridge indices taken in contraction order. The two bridge paths take the trace of the product. Thus the actual normalized boundary matrix is

$$
 M=C\,\mathbb E_{\mu_B}
 \begin{pmatrix}
  2q(H)q(K) & q(H)q(K)\\
  q(H)q(K)  & q(HK)/2
 \end{pmatrix}.                                                   \tag{1}
$$

In particular, routing both loops through the bridge reads a single trace around both squares. At fixed fields this can distinguish their relative colour. The two eigenangles alone do not determine that entry.

Let $s=(1,1/2)^T$. Projecting each root choice onto its disconnected pairing $p$ has overlap $s_a=\langle p,a\rangle$. It gives the corner matrix $M_{pp}ss^T$ with the loops still sampled from their **same joint Wilson law**. Subtract it in (1). The only potentially nonzero entry is

$$
 (M-M_{pp}ss^T)_{rr}
 =\frac C2\,\mathbb E_{\mu_B}[q(HK)-q(H)q(K)] .                 \tag{2}
$$

In the orthonormal exterior basis the coefficient with the traceless routing $t$ at both bonds is

$$
 \mathcal R_d=M_{tt}=
 \frac{4M_{rr}-2M_{rp}-2M_{pr}+M_{pp}}3
 =\frac{2C}{3}\,\mathbb E_{\mu_B}[q(HK)-q(H)q(K)] .             \tag{3}
$$

This definition charges the signed exchange to a particular coefficient of $R_B/z_B$. It keeps the positive Wilson factor even when the coefficient vanishes.

**The coordinate interchange kills the exchange.** Swapping axes 1 and 2 of $B_d$ fixes $0$ and every edge of $Q$ pointwise. It takes the rooted walk defining $P$ to its reverse. This changes $(H,K)$ to $(H^{-1},K)$. Probability Haar on the internal links is preserved and the internal faces permute, with $q(g^{-1})=q(g)$. Consequently $w_B$ and $z_B$ are preserved. The external labels need no symmetry assumption here. They have already been contracted to the specific functions in (1). The SU(2) characteristic polynomial gives $H+H^{-1}=2q(H)I_2$. Averaging the two integrands related by the interchange yields

$$
 \frac{q(HK)+q(H^{-1}K)}2=q(H)q(K).
$$

With $m_d=\mathbb E_{\mu_B}[q(H)q(K)]$, the result throughout $I$ is

$$
 M=2C\,m_d\,ss^T,\qquad M-M_{pp}ss^T=0_{2\times2},\qquad
 \mathcal R_d=0 \quad(d=4,5).                                  \tag{4}
$$

The $pp$ coefficient at identity holonomies is $2C$. This also follows by counting the three free fundamental traces and the two factors $1/2$ at the four-valent bonds.

**Product subtraction using separately measured loops.** If “disconnected” means the product of the normalized one-square readings, the remaining scalar can be kept exactly. Put $m_P=\mathbb E_{\mu_B}q(H)$ and $m_Q=\mathbb E_{\mu_B}q(K)$. A single strip has coefficient $L_P=b^2 m_P/2$ or $L_Q=b^2 m_Q/2$ from its four bivalent tensors. The pure outward triangle has coefficient $T=b^{3/4}/\sqrt2$. Each of these is a reading of the same normalized block, with unused exterior slots in the vacuum. Hence $T L_P L_Q=2C\,m_Pm_Q$. With the overlaps restored, the whole connected matrix in this convention is

$$
 M-TL_P L_Q\,ss^T=2C\,(m_d-m_Pm_Q)\,ss^T .                     \tag{5}
$$

The parenthesis is an ordinary covariance of two half-traces. Equation (5) keeps it in the $pp$ entry of the orthonormal basis. Its $tt$ entry, both mixed entries in that basis and its determinant are exactly zero. The proof of (4) never factorizes the two face-angle laws.

**Exact scalar in (5).** For an integral-free expression let $p_f$ be the real part of the ordered product of four formal quaternions on the face $f$, conjugating a link quaternion when traversed backwards. Define a linear functional $\mathcal L$ on monomials in the four real coordinates of each link by multiplying the following factors over links. The factor is zero for any odd coordinate exponent. For exponents $(2k_0,\ldots,2k_3)$ with $h=\sum_i k_i$, it is

$$
 \frac{\prod_{i=0}^3 (2k_i-1)!!}{\prod_{j=0}^{h-1}(4+2j)},\qquad (-1)!!=1.
$$

These are the coordinate cases of row 1341's sphere moments. Dividing the product of four Gaussian coordinate moments by the independent radial moment gives the formula, including the empty product one. For $a,c\in\{0,1\}$ put

$$
 S_{ac}=\sum_{n=0}^{\infty}\frac{\beta^n}{n!}
   \mathcal L\!\left[p_P^a p_Q^c\left(\sum_{f\subset B_d}p_f\right)^n\right].
$$

Then $z_B=A^{-F}S_{00}$, $m_d=S_{11}/S_{00}$, and the scalar $m_d-m_Pm_Q$ in (5) is $(S_{11}S_{00}-S_{10}S_{01})/S_{00}^2$, where $F=\binom d2 2^{d-2}$. Indeed $\mathcal L$ integrates exactly against product Haar, and $|p_f|\le1$ on unit quaternions. For any $N+2>x=F(513/256)$ the absolute tail after degree $N$ in each series is at most $x^{N+1}/[(N+1)!(1-x/(N+2))]$. This follows by bounding the ratio of successive exponential-majorant terms. Jensen gives $S_{00}\ge1$ since each unweighted face has mean zero. These convergent rational-coefficient series evaluate all entries in (5) at the stated coupling. No numerical value or sign of the covariance enters the rejection. [Sphere-moment argument, row 1341](gap-blockstep-astra62.md)

## Scope of the cancellation and the dimension test

The cancellation extends to **every exterior contraction on these two squares with a single fundamental strand on at least one possible closing edge of either square**. Here the mixed-edge graph is the union of $P,Q$ with optional trees attached at single vertices and optional forest components. On its other edges allow any compatible finite list of representations, with arbitrary exterior invariant tensors and outward-only decorations. The inner measure is still the isotropic bare Wilson measure on the whole block. The assertion concerns interior colour exchange and permits scalar correlations.

To see this, delete one edge from each square to make a spanning forest, choosing the singly read edge as one of the deletions. Gauge its tree links to one with the common root frame fixed. The forest and one-cycle reduction are due to the earlier rows cited above. The two remaining matrices are now the rooted $H,K$, up to the prescribed orientations. Dualize backwards strands and interchange their index ends. The fixed exterior contraction is a linear functional of $D_{1/2}(H)\otimes D(K)$ if the singly read edge is on $P$. Dualizing its single fundamental gives the same argument. The axis interchange averages its matrix to $q(H)I_2$ while fixing $K$. The residual common root conjugation now conjugates $D(K)$ with a conjugation-invariant weight $q(H)$. In $D=\bigoplus_j V_j\otimes M_j$ this gives the operator

$$
 I_2\otimes\sum_j
 \mathbb E_{\mu_B}\!\left[q(H)\frac{\chi_j(K)}{2j+1}\right]\Pi_j ,       \tag{6}
$$

where $\Pi_j$ includes the entire multiplicity space. Indeed $D(K)$ already acts as the identity on each $M_j$ and the conjugation average on $V_j$ is its normalized trace. For a singly read edge on $Q$, interchange axes 3 and 4. With a single fundamental on each chord the operator is $m_d I_2\otimes I_2$. Thus row 1421's spectral-block formula (3) holds **on these representations** even though the graph is connected and the root conjugation acts diagonally. Every exterior functional reads that same operator. Changing a routing, a phase or a basis within this class cannot restore the discarded relative colour.

The group-independent definition of the signed response uses the exterior tensor $X=r-\langle p,r\rangle p$ at both bonds, with the same block vacuum division. In SU(2), $X=\sqrt3\,t/2$, so $M_{XX}=3\mathcal R_d/4$ equals (2). This definition also makes sense when the traceless channel has dimension zero. For compact U(1), a line of fixed charge $n$ carries the one-dimensional matrix $D_n(h)=h^n$. Its traceless part vanishes for every $h$. More explicitly, the bivalent tensors carry constant oriented charges round each strip and along the bridge. At a compatible four-slot bond the neutral invariant space is the single line spanned by $p$, regardless of the charges on that loop and the bridge. Thus $X=0$ for every allowed routing. An inadmissible charge configuration has zero coefficient. The fixed-charge response vanishes before integration, including for conjugate charges. In SU(2) it vanishes after Wilson integration by (4).

For the classical comparison, matching the quadratic action on constant curvature under a factor-two change of length gives $2^d$ fine cells per coarse cell and a squared coarse plaquette flux $2^4$ times the fine one. The inverse-coupling multiplier is $2^{d-4}$. The reflection preserves the full set of internal faces in both dimensions.

| Dimension | Internal Wilson plaquettes in the common denominator | Classical multiplier | Signed contribution $\mathcal R_d$ |
|---|---:|---:|---:|
| 4 | 24 | 1 | 0 |
| 5 | 80 | 2 | 0 |

Each count is $\binom d2 2^{d-2}$. Even differences or derivatives of (3) across the band give zero. This rejects the proposed decrement in four dimensions for the stated class. Equation (5) leaves the scalar covariance in place. The test supplies no value of the physical running stiffness. [Dimension filter, §§4.3–4.5](gap-mech-direction2-fable.md)

## Checks and the first reading outside (6)

For a hand check of the sign, take unit quaternions $H=(3/5,4/5,0,0)$ and $K=(1/3,2/3,2/3,0)$. These holonomies are realizable by setting one directed edge on each square and taking every other link to be the identity. Quaternion multiplication gives $q(H)q(K)=1/5$, $q(HK)=-1/3$ and $q(H^{-1}K)=11/15$. The two values of the integrand of $\mathcal R_d/C$ are $-16/45$ and $16/45$. The configurations have equal Wilson density under the coordinate interchange. This tests a genuinely colour-sensitive routing before the average.

A scratch trace-word checker also constructs each face from its vertices and follows the exterior index paths as a permutation. Its exact output is below. Each word is an unnormalized trace and $\operatorname{tr}(1)=2$. Multiplying each routing's trace product by $C/4$ and averaging against $\mu_B$ reproduces (1).

```text
d=4 internal=24 mixed=8 outward=3 bivalent=7
  pp -> tr(1) tr(H) tr(K)
  pr -> tr(H) tr(K)
  rp -> tr(H) tr(K)
  rr -> tr(HK)
d=5 internal=80 mixed=8 outward=3 bivalent=7
  pp -> tr(1) tr(H) tr(K)
  pr -> tr(H) tr(K)
  rp -> tr(H) tr(K)
  rr -> tr(HK)
```

The executable source is `/tmp/ym4d-row1424.p5KOf0x1/route_words.py`. This is a combinatorial check of the wiring. The proof uses the written tensor contractions, the SU(2) trace identity and a measure-preserving coordinate permutation. It requires no computed premise. No Lean executable was on PATH and no kernel certificate or independent review is claimed.

There is a concrete way to leave the rejected class while keeping every exterior spin at $1/2$. Put two mixed strips on each square. Use outward bonds $A=-3,C'=-4$ for the two copies of $P$ and $B=-1,D=-2$ for the two copies of $Q$. At the origin take the outward faces of the ring $A B C' D A$ or $A C' B D A$ and put $t$ at all four bonds. All other occupied exterior bonds are bivalent. Denote the two normalized coefficients by $Y_{\rm alt},Y_{\rm grp}$. The common prefactor is $C_2=b^9/64$ from sixteen mixed faces, four outward corners and twelve bivalent tensors. Each $t$ inserts $(G-q(G)I)/\sqrt3$. Write $\mathbf h,\mathbf k$ for the vector parts of the unit quaternions $H,K$. The alternating word in the vector parts has trace $2[2(\mathbf h\cdot\mathbf k)^2-|\mathbf h|^2|\mathbf k|^2]$, because their quaternion product has scalar part $-\mathbf h\cdot\mathbf k$ and vector part $\mathbf h\times\mathbf k$. The grouped word has trace $2|\mathbf h|^2|\mathbf k|^2$. Consequently the relative orientation of the two loops enters the normalized coefficient

$$
 Y_{\rm alt}+\tfrac13Y_{\rm grp}
 =\frac{4C_2}{9}\,
 \mathbb E_{\mu_B}\!\left[(\mathbf h\cdot\mathbf k)^2
                    -\tfrac13|\mathbf h|^2|\mathbf k|^2\right].           \tag{7}
$$

The subtraction inside (7) removes the independently conjugated orientations at the *same two angles*. A uniform rotation has second moment $|\mathbf k|^2 I_3/3$ by isotropy and trace. Both inversions preserve the remaining integrand. It takes opposite signs on parallel and perpendicular nonzero vector parts. Thus (4) rejects the single-strand reading and leaves the Wilson sign of (7) open. Squaring the integrand of (3) before integration also requires extra strands.

## Next two rows

1. **Determine the sign and size of (7) for the Wilson block.** Freeze the outgoing response and the sign with which (7) enters it before evaluating the two rings. Keep their relative coefficient, the common denominator and the internal spin tail. A pass requires a strict, uniform decrement on $I$, its zero at fixed U(1) charges and its five-dimensional comparison against $2$. A proof of cancellation or the wrong sign rejects this channel. An interval crossing zero leaves it open. Any inequality supplied by computation needs a Lean-kernel replay and a stated trusted base.
2. **Attempt one four-direction inclusion only with a surviving response.** Fix the cross-bond rearrangement, prove that it preserves the required closed contractions and fix the input/output centres. Accept one interval only with entry for every bare input in $I$, a positive vacuum lower bound, a rational sector vector $v>0$ and componentwise bounds $M_I(0)\le v/16$ and $M_I(v)-M_I(0)\le15v/16$, including the tail. A certified excess rejects those centres. Record the measured cost and the trusted base of any arithmetic certificate. Row 1424 supplies no signed decrement for this inclusion.
