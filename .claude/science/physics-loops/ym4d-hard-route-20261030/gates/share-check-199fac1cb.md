# Row 75: share-check at 199fac1cb
Provenance: OpenAI Codex; local configuration says model `gpt-6-astra`, effort `low` (read from `/Users/jonreilly/.codex/config.toml`; runtime overrides and backend identity are not exposed, so execution at row 75's requested `xhigh` is not certified); repository `199fac1cbf3a6a22aae818c020bede2e1a3c433a`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, granting no status. One Codex reader: (a) and (b) check Claude-authored notes; (d) checks Codex-authored examples and is not independent in model.

| Item | Research verdict | What can be shared |
|---|---|---|
| (a) Quadratic seam | ADVANCE | SHAREABLE: the flat unrestricted-fibre curvature competitor, with absolute constants |
| (b) Example E / Theorem R | ADVANCE after the units repair; literal unrescaled bound WRONG; actual curved consumer CORRECT-NO-ADVANCE | SHAREABLE only for the repaired E and defined-operator implication; E is not a Landau-pair counterexample |
| (c) Box gauge | ADVANCE with a local starting-box repair | SHAREABLE: real Lemma U at small total energy, not the later fill claims |
| (d) Old floor | CORRECT-NO-ADVANCE | SHAREABLE AS A QUESTION; no violating admissible history constructed |
| (e) Reference normalization | ADVANCE for the missing-reference finding and conditional positivity; CORRECT-NO-ADVANCE for all-support admission | SHAREABLE as the precise correction and a support-admission question |

Credit: the outline examined here is Ethan Sussman and Levent Alpoge's `YM4_sketch_500.tex`, with Claude and Codex as the authors of their text. Its constructions and terminology below are attributed to that source. Balaban's programme is background, not a checked imported theorem here.

Scope: queue row 75(a)–(e), including both research verdicts (ADVANCE, CORRECT-NO-ADVANCE, WRONG) and the row's sharing verdicts. All mathematical checks below are written hand arguments. Text search, retrieval and source bookkeeping supply no mathematical discharge. The outline was fetched once into `/tmp/sa_ym4.tex` using the specified pinned URL. Only this report is edited in the repository. The workflow file is absent from the sparse working tree but present in the pinned Git object; it was recovered read-only with `git show` and read in bounded ranges. Its research-gate/no-status rules agree with this task; the explicit one-file scope overrides its broader workflow options.

The report was saved section by section. All five requested comparisons are now recorded; their unresolved proof obligations remain explicit below.

## (a) Quadratic seam and absolute constants

**ADVANCE; SHAREABLE**, precisely as a flat, linear, unrestricted-fibre curvature competitor theorem on the whole lattice or compatible periodic tori, with the kernel and constants below. The fine gauge correction is unrestricted; no frozen-boundary or logarithm-chart condition is asserted. This does not establish A3 or Propositions 2.8/2.10 of the outline.

Source checked: `library/seam-quadratic-c.md`, lines 39–418 and 482–528. Its author is Claude Opus 5.5/max, not Codex. The following reconstructs the proof rather than using its discharge labels or numerical section.

1. **Actual constraint, lines 90–157.** Put $B=L^n$. The $L^4$ centred blocks of side $L^k$ partition the centred block of side $L^{k+1}$: in one coordinate their consecutive integer endpoints are $-(L^{k+1}-1)/2,\ldots,(L^{k+1}-1)/2$. Concatenating the $L$ fine segments before averaging proves composition of the path maps. The endpoint sum gives $Qd=d'r$, whereas the straight segment gives $Q_{\rm path}d=d'\operatorname{Av}$. Thus
   \[
   Q_n=Q_{\rm path}^{(B)}-d'\Phi_n,
   \quad\Phi_{k+1}=\operatorname{Av}_L\Phi_k+\Phi^{(k+1)}Q_k,
   \quad d'Q_n=C_Bd.
   \]
   No small-field estimate is used. Translation covariance of the chosen contour family is necessary. For $Q_{\rm path}Z=0$, adding $dE\Phi_n Z$, where $r_nE=I$, cancels exactly the coarse gradient. Conversely, for $Q_nW=0$, subtract $dT_0\Phi_nW$, where $\operatorname{Av}_BT_0=I$. Its path average vanishes and its curvature is still $dW$. This proves equality of the two sets of attainable curvatures, including coarse harmonic sectors; it is not a bound on the correcting gauge.

2. **One-dimensional inverse, lines 159–224.** With $B=2m+1$, the average of the centred hat is $1-m(m+1)/B^2=1-2g_1$, its two neighbouring averages are $g_1=m(m+1)/(2B^2)$, and other averages vanish. The supported hat $\beta$ has average one in its own block and zero elsewhere, so the added second difference cancels those two off-diagonal averages exactly. Hence $R^0T^0=I$. Shifting the index in that second difference proves reproduction of both $1$ and $x$. Differencing the cumulative sum of the hats gives the displayed $\eta_c$, so $dT^0=T^1d'$. Telescoping a segment proves $R^1d=d'R^0$. These imply $R^1T^1=I$ on gradients. On a circle its remaining constant mode is also fixed, since affine reproduction on the cover gives $T^1 1=1/B$ and $R^1(1/B)=1$.

   For any primitive $d\varphi=a$ on the cover, the displayed path-sum formula for $h$ equals $\varphi-T^0R^0\varphi$. Consequently $hd=I-\Pi^0$, $dh=I-\Pi^1$, and $R^0h=0$. Additive constants cancel; a quasiperiodic primitive has its affine increment reproduced, so $ha$ descends to a circle. This checks the potentially dangerous harmonic case, rather than presuming exactness of every periodic one-form.

3. **Norms and locality, lines 190–224.** The absolute row/column sums are respectively $1,1/B$ for $R^0$, and $B,1$ for $R^1$. For $T^0$ they are below $2,3B/2$: $g_1<1/8$, $c_B<2$, and the hats partition unity. For $T^1$, $|\Delta\beta|<4/B$ and total variation $2c_B$ give $3/B,2$. The $h$ path has length below $2B$, so its row sum is below $4B$; a fixed bond meets at most four contributing coarse sites, each of absolute mass below $3B/2$, giving column sum below $6B$. Schur's inequality follows directly by weighted Cauchy–Schwarz and gives exactly the six stated squared-norm bounds, including $\|h\|^2\le24B^2$. Every input lies within $2B$. Periodizing cannot increase these absolute-sum bounds.

4. **Tensor signs and primitive, lines 226–284.** In $d\widehat H_i+\widehat H_i d$, each $j\ne i$ term cancels because passing the differential across the degree-lowering slot flips one Koszul sign. The $j=i$ term is $\Pi_{<i}(I-\Pi_i)$; summing telescopes to $I-TR$. Also $R\widehat H_i=0$ because its $i$-slot is $R^0h$. Thus closed $G$ with $C_BG=0$ has $H=hG$, $dH=G$, $Q_{\rm path}H=0$. The six component bounds give
   \[
   c_H=24(222+32\sqrt6+24\sqrt2)<8024,
   \qquad\|T_2\|^2\le(6/B)^2(3B)^2=324.
   \]
   This arithmetic does not depend on the note's rounded table: $\sqrt6<24495/10000$, $\sqrt2<14143/10000$, as is checked by squaring, give $c_H<8023.8528<8024$. Restricting the input to the $2B$ neighbourhood of the output set gives the stated local estimate; closedness is not needed for this norm estimate on the truncated input.

5. **Competitor and shell, lines 286–374.** For $G=dA_t-dA_*$, the preceding kernel condition follows from equality of the actual parents. Set $Z=(I-T_1Q_{\rm path})(\chi H)$ and add the pure gauge in step 1. Applying $Q_n$ gives $v$, and applying $d$ gives
   \[
   dX_D=(1-\chi)dA_*+\chi dA_t+
   [d,\chi]H-T_2d'Q_{\rm path}(\chi H).
   \]
   The product rule here really uses the shifted bond values $H_\nu(z+e_\mu)$, not unshifted values. The cutoff difference is bounded by (2/(rB)). In the second term use $Q_{\rm path}H=0$ to subtract $\chi(c_*)$ from every row. Each row has mass $B$, column mass $B^{-3}$, and read radius below one top unit about its midpoint. Its cutoff difference is below $2/r$. It can be nonzero only within $1+1/B$ of the transition set; all its input bonds are within $2+1/B<3$. The coarse curl and $T_2$ put its output within four top units of that set. Reading $hG$ adds less than two units, giving input set $N_5$. A point of $N_5$ is within $r+5$ of $D$; if it were in $D^{-(r+5)}$, the nearby transition point would be in $D^{-r}$, a contradiction. This proves the shell containment, including irregular $D$. Empty/full $D$ reduce to zero/constant cutoff and zero defect.

   Each fine bond appears in at most three commutator plaquettes; each coarse plaquette has four edges and each coarse edge lies in six plaquettes. Thus
   \[
   \|R\|^2\le\frac{48+2\cdot324\cdot24\cdot4}{r^2B^2}
       \|H\|_{A_2}^2
   \le\frac{62256c_H}{r^2}\|G\|_{N_5}^2.
   \]
   Finally $|G|^2\le2(|dA_*|^2+|dA_t|^2)$. In particular $c_R=62256c_H<499542144<5\cdot10^8$. No empirical norm or numerical search enters.

6. **Energy and rate, lines 376–418.** Minimality compares $A_*$ with this admissible competitor. Cancel the unchanged exterior, use the exact trial curvature in $D^{-(r+5)}$, and use convexity plus Young's inequality on the shell. Adding back $D\setminus D^{-(r+5)}$ gives coefficient $(1+\epsilon)+(1+1/\epsilon)C_{\rm seam}$, minimized at $\epsilon=\sqrt{C_{\rm seam}}$. Therefore
   \[
   A_s=(1+\sqrt{2c_R}/r)^2,\quad K=\delta_0,\quad M_*=1.
   \]
   At $r=\sqrt{2c_R}$, $A_s=4$ and the stated rate condition is precisely $8\sinh(\nu(r+5))<1$. Since $r+5<31628$, and
   $\operatorname{arsinh}(1/8)=\int_0^{1/8}(1+t^2)^{-1/2}dt>1/\sqrt{65}>31/250$, one obtains $\nu_0>3.9\cdot10^{-6}$ by rational arithmetic. All constants precede the choices of $L,n$ and volume. The further invocation of `excess-seam.md` for WAM is not a checked downstream theorem here.

**Bearing on their route.** A3, outline lines 3864–3897, asks for kernels and first/Hölder differences of actual nonlinear response and conditional inverses over the enlarged complex domain and layered geometry. Our result bounds energy of one explicit flat competitor, without even bounding the node-restoring gauge. It is useful as a flat seam comparison and as a check that contour gradients need not create a curvature loss; it is no substitute for A3. The action cancellation of 2.8 at lines 17854–17899 uses criticality, signed shell weights, nonlinear Taylor remainders and changes of determining sets. The healed-component sum of 2.10 at lines 17961–18010 also needs a common component measure, deletion compatibility and paid masses. None follows from this quadratic competitor. The outline already records flat classical kernel results at lines 3881–3888, so sharing this should identify its particular constructive shell estimate, not claim to supply their missing flat theory or their large-field route.

## (b) Example E, Theorem R, and the Landau pair

| Step | Research verdict | Sharing verdict |
|---|---|---|
| Example E at the flat linear level, with the normalization specified below | ADVANCE | SHAREABLE: a fixed-gauge critical-norm obstruction, removable by gauge |
| The unrescaled contour bound with the earlier operator applied literally to H | WRONG | NOT SHAREABLE; use the explicit H/B convention below |
| Theorem R for the explicitly summed, transported contour operator | ADVANCE as an implication | SHAREABLE with that definition and an assumed annular bound |
| Theorem R as a supplier for the actual curved recursive operator in (REL-Phi) | CORRECT-NO-ADVANCE | NOT SHAREABLE as a proved supplier; SHAREABLE AS A QUESTION about the operator comparison |
| Example E as a counterexample to their Landau-pair Theorems 3/4 | WRONG | NOT SHAREABLE; the displayed example is outside the slice |

Read and checked: `library/rel-phi-c.md` lines 46–81, 109–232, 257–312, 383–459 and 544–557. The run tables are not proof. The nonlinear extension in (C1), the capacity construction of Section 4, and the other (REL) clauses of Section 6 are not gated here.

**Normalization must be explicit.** The note first defines $\Phi_n$ on link logarithms $\theta$, then writes $\Phi_n^{(T)}H$ with $H=B\theta$, while Example E uses $\Psi=\Phi_n\theta$. Literally applying the earlier linear operator to $H$ multiplies the answer by $B$. In this report the normalized operator is $\Psi(H):=\Phi_n(H/B)$. The proof and all numerical constants below apply to this convention. This is a local notation repair, not a license to equate two different curved operators.

There is a direct hand discriminator for that units error. On a compatible torus put a scalar potential equal to t away from the top centres and zero at every centre, and set H equal to B times its gradient in one fixed Lie-algebra direction. The eight incident bonds at a centre carry the entire local fourth norm, so the annular sum in top units is $8^{1/4}t$, independently of depth. The exact gauge identity gives the earlier, unrescaled operator applied to H as $Bt(1-B^{-4})$ at that centre. No constant depending only on L bounds that by the annular sum as B grows. Dividing the operator's input by B fixes this failure. This tests the stated operator/norm identification; it does not assert that a zero-curvature endpoint has a positive curvature-energy budget or refute the existential physical (REL) statement.

**Reconstruction of the flat contour identity and annular estimate.** On a gradient, a staircase from $y$ to $x$ gives $\lambda(x)-\lambda(y)$. Substitution of $Q_k=Q_{{\rm path},L^k}-d\Phi_k$ into the recursion cancels the two block-average terms and leaves
\[
\Phi_{k+1}=r\Phi_k+\Phi^{(k+1)}Q_{{\rm path},L^k}.
\]
Centres nest, so iteration gives the sum of one-step contours all starting at the same top centre. Applying this to $d\lambda$ and using the exact tiling of centred blocks telescopes to
\[
\Phi_n(d\lambda)(y)=\operatorname{Av}_B\lambda(y)-\lambda(y).
\]
The path-average kernel at scale $s$ is at most $s^{-3}$ on at most $2s^4$ bonds. Hölder therefore gives $2^{3/4}\|\theta\|_{\ell^4(S(c))}$. The total absolute staircase weight is $4m(m+1)/L<L$. A staircase's incident bonds at its starting point carry total weight $1-L^{-4}<1$.

For annulus $A_j$, the terms of scales $k=j,j+1$ contribute at most $2\cdot2^{3/4}L\|\theta\|_{\ell^4(A_j)}$. For $k\ge j+2$, a path support meeting the inner region can only be one of the eight bonds incident at $y$: its transverse coarse coordinates must be zero, and its longitudinal coordinate must be $-s$ or $0$. There are at most $64L^{4j}$ fine bonds in $R_j$. Its contribution is bounded by
\[
64^{3/4}L^{-3(k-1-j)}\|\theta\|_{\ell^4(A_j)}.
\]
The remaining geometric sum is at most $16\sqrt2/(L^3-1)<1$, and $2\cdot2^{3/4}<3.4$, proving $C_A(L)=3.4L+1$. These comparisons follow by squaring/fourth powers, not numerical kernel norms. Hölder on the $n$ annuli gives exactly the $n^{3/4}$ loss. Arbitrary orthogonal transports do not change this absolute-kernel estimate for the explicitly summed operator.

**Example E, line by line.** Write $\ell=\log(1+R)$, $R=\lfloor(B-1)/4\rfloor\ge2$, and take the radial scalar profile in the note times one fixed unit Lie-algebra vector.

* E1: balls of radius $R<B/2$ around top centres are disjoint; the profile is zero at every centre and constant outside the balls. Thus its exponential is an allowed node-fixed gauge.
* E2: $dd\lambda=0$ and $Q_nd\lambda=d'r_n\lambda=0$. In the single commuting subgroup the exponentiated links telescope as well, so their plaquette holonomies are exactly the identity. This does not require a global small bound on $\lambda$.
* E3: the exact number of outward unoriented bonds from radius $r$ to $r+1$ is $8(2r+1)^3$. For $r\ge1$ it is bounded by the note's $256r^3+64r$: the difference is $192r^3-96r^2+16r-8>0$. At $r=0$ there are eight bonds. Each nonzero increment is at most $a/((1+r)\ell)$. Hence the fourth-power sum is bounded by
  \[
  a^4\ell^{-4}\left(8(\log2)^4+320\sum_{r=1}^{R-1}(r+1)^{-1}\right)
  \le322a^4\ell^{-3}.
  \]
  For completeness $\log2=2\sum_{k\ge0}((2k+1)3^{2k+1})^{-1}<56/81+1/540=1123/1620$; its fourth power times eight is below $1.85$. Also $\sum_{r=1}^{R-1}(r+1)^{-1}\le\log R<\ell$ and $\ell>1$. Since $4.25^4>322$, E3 follows with its stated constant.
* E4: the same count with squared increments gives $B^{-2}a^2(3.9+160R^2)/\ell^2$. The constant term follows from $8(\log2)^2<3.9$; the rest follows by bounding each summand by $320r$. Since $B\ge4R+1$, the coefficient is below 11.
* E5: the only deficit from the constant value $a$ lies in the ball of at most $(2R+1)^4$ sites. For $B\ge9$, $(2R+1)/B\le5/9$, whose fourth power is below $0.2$. The gauge identity gives $|\Psi(y)|\ge0.8a$, at every centre.

Taking $a=t\ell^{3/4}/4.25$ proves $\|H\|_4\le t$, $\|H\|_2\le0.8t\ell^{-1/4}$, and $|\Psi|\ge0.18t\ell^{3/4}$. For $B\ge81$, $\ell\ge\log(B/4)\ge(2/3)\log B$, which gives the stated weaker $0.1t(\log B)^{3/4}$ lower bound. Thus a depth-uniform fixed-gauge bound by the fourth norm is false. A statement with energy identically zero on its right must not be inferred: this pure gauge is a norm obstruction, and the note's comparison with a positive energy budget requires that budget separately. Undoing the gauge removes the example exactly. No nonlinear curved extension of this comparison is established here.

**Theorem R.** For the normalized, explicitly summed transported operator, Lemma A applied to (REL-D) immediately gives the implication. If the convolution weight has the stated shift comparison, the sum over the $3^4$ neighbouring top cubes is at most $3^4e^{2\delta}$ times the central value; its square root supplies $9e^\delta$. This is a conditional implication, not a construction of the required gauge or a proof of (REL-D). For the actual curved recursive map the flat cancellation used above need not hold: parallel transports around a plaquette differ by its curvature, and substitution in the recursion leaves curvature times intermediate contour averages. The note explicitly leaves this difference unbounded at lines 177–182 and 551–554. Bounds only on annuli at final top centres do not automatically bound the intermediate-centre sums. No verified estimate permits insertion of the advertised factor $1+Cf$ for that different operator. This is the load-bearing limitation in Theorem R, not a counterexample to its correctly defined flat implication.

**Does their Landau pair avoid E? Yes, this particular example is excluded.** The outline's slice is defined at lines 7187–7197 and 9646; (1b) Theorem 3 at 9693–9732 fixes both the slice and the node factor, and Theorem 4 at 9734–9752 differentiates that chosen pair. On the uniform flat torus used in E, $Q'$ is block averaging and $R$ projects onto $\Delta\ker Q'$. Periodicity of E's repeated profile makes $Q'\lambda=c$ the same constant on every block. Therefore $\lambda-c\in\ker Q'$ and $\Delta\lambda\in\Delta\ker Q'$. For $A=d\lambda$, up to the immaterial divergence sign,
\[
RD^*A=D^*d\lambda\ne0.
\]
Indeed a nonconstant scalar on a connected finite torus cannot have zero Laplacian, since its pairing with that Laplacian is $\|d\lambda\|^2$. E is therefore not an allowed perturbation of the Landau potential even at the flat level. In their base representative, flat identity data give the zero potential; the node-fixed pure gauge has already been removed. Their pointwise scale bounds, if proved, are also stronger than the critical fourth-norm hypothesis. This checks why E is not a counterexample; it does **not** verify the existence, analytic continuation, uniqueness or nonlinear response estimates asserted in Theorems 3/4.

## (c) The lattice small-energy box gauge

**ADVANCE for Lemma U, with the finite starting-box repair below; SHAREABLE** as a real SU(2) small-total-energy gauge on a comparable-sided contractible box. It is uniform in the number of lattice sites. No claim is made here for an arbitrary retained boundary, a parent-preserving gauge, complex gauges, or the shell-filling lemmas later in the file.

Checked: `library/lattice-uhlenbeck.md` lines 7–85, using only Section 1 of `library/lattice_sobolev_box_gauge.md` (lines 5–17) as its Sobolev input. Lines 87–141 of the former were read to identify the consumers; their F/RF assertions are not included in this verdict. In particular an extension over unions of patches is a separate assertion, not a consequence of the box result by its label.

1. **Boundary identity, lines 25–29.** Reflect tangential components evenly and the normal one oddly across the half-integer faces; the crossing normal bonds are zero. On the reflected torus write $z_i=e^{iq_i}-1$. The correct complex-symbol identity is
   \[
   \sum_{i<j}|z_i a_j-z_j a_i|^2+
   \left|\sum_i\overline z_i a_i\right|^2
       =\left(\sum_i|z_i|^2\right)\left(\sum_i|a_i|^2\right).
   \]
   Thus the divergence uses the conjugate symbol (the shorthand dot in the note must be read this way). Each interior curl and site divergence has sixteen reflected copies. Plaquettes through the reflection face have zero curl, because the two tangential values agree and the normal crossing values vanish. In the gradient sum, tangential crossing differences vanish, and normal differences from a boundary bond to zero reproduce exactly the stated normal boundary term, with the same multiplicity sixteen. Dividing gives $X^2=\|da\|_2^2+\|\delta a\|_2^2$. It would be false with that boundary term omitted.

2. **Sobolev, lines 31–37 and its cited proof.** The discrete product inequality used there can be proved without an external black box: in dimension $d$, first sum the last coordinate and apply Hölder to the $d-1$ dependent factors; then apply Hölder with exponents $d-1,(d-1)/(d-2)$ to the remaining sum, and use the same product inequality in dimension $d-1$. At $d=2$ it is just separation of the two sums. Applying this with the one-coordinate telescoping bounds on $w$ gives $\|w\|_{4/3}\le\prod_i\|d_iw\|_1^{1/4}$. For $w=|u|^3$,
   \[
   \|d_iw\|_1\le3\|u\|_4^2\|d_i u\|_2,
   \quad \|u\|_4\le3\prod_i\|d_i u\|_2^{1/4}
       \le\tfrac32\|\nabla u\|_2.
   \]
   The zero function is handled before dividing by its norm. A cutoff on three period cells per direction gives the torus inequality with the extra $N^{-1}\|u\|_2$. The nonzero Fourier eigenvalues are bounded below by $cN^{-2}$, since $\sin t\ge2t/\pi$ on $[0,\pi/2]$; comparable periods preserve an absolute $c$. Mean zero absorbs the extra term. Each reflected $a_\mu$ has mean zero by oddness, proving both the fourth-norm and $N^{-1}$ second-norm bounds. The even Neumann solution of $\delta dw=f$ exists for mean-zero $f$; reflection and the same symbol identity give $\|\nabla dw\|_2=\|f\|_2$ with the boundary convention above, and hence $\|dw\|_4\le C\|f\|_2$. Summing the box divergence shows its mean is zero.

3. **Nonlinear a priori estimate, lines 39–43.** On a sufficiently small fixed ball of link logarithms, the matrix product followed by its logarithm is analytic, has linear term the oriented curl, and has a uniformly bounded second derivative. The Taylor formula with an integral remainder therefore gives $|\theta_p-(da)_p|\le C\sum_{b\subset p}|a_b|^2$. Four edges per plaquette and six plaquettes per edge give $\|da\|_2\le\|\theta\|_2+C\|a\|_4^2$. Together with step 2 and the exact boundary identity this is (A). Only existence of fixed finite-dimensional Taylor constants is used. The argument chooses $X_0$ so small that the chart stays strictly inside this ball; the broader displayed cutoff $|a|\le1$ is not needed.

4. **Flow and the unbounded gauge parameter, lines 45–63.** Infinitesimal gauge transformation is conjugation at the tail followed by multiplication with the increment $w(x+e)-w(x)$. Differentiating the local logarithm gives a skew rotation $[w(x),a]$ plus $-J(a)dw$, with $J(0)=I$ and $J-I$ Lipschitz of size $C|a|$. Choose $\delta dw=\delta a=f$. Expanding the divergence of the rotation at incoming bonds gives $[w(x),f(x)]$ plus products of $dw$ with shifted $a$. The first term has zero inner product with $f$. The remaining two errors obey
   \[
   \|[dw,a]\|_2\le C\|dw\|_4\|a\|_4,
   \quad
   \|\delta((J-I)dw)\|_2
      \le C\bigl(\|a\|_\infty\|\nabla dw\|_2
                +\|\nabla a\|_4\|dw\|_4\bigr).
   \]
   The boundary differences are obtained by the same reflections; zero crossing gradients introduce no omitted flux. Counting measure gives $\|\nabla a\|_4\le\|\nabla a\|_2$, so the right side is $CX\|f\|_2$. Choose $X_0$ with $CX_0\le1/2$. Then $d\|f\|_2^2/dt\le-\|f\|_2^2$, after reducing this fixed threshold if necessary. There is no use of a volume-uniform supremum bound on $w$.

   The small component of (A) cannot cross $X=X_0$: at a first crossing, $\|\theta\|+\|f(0)\|\le X_0/8$ and $C_1X_0\le1/8$ make its right side strictly smaller than $X_0^2$. On this component, taking a square root gives $X\le\|\theta\|+\|f\|+C_1X^2$, and hence $X\le2(\|\theta\|+\|f(0)\|)$. This also checks the small-root selection, which cannot follow from (A) alone. For each fixed finite box the mean-zero inverse Laplacian is a bounded finite matrix (its bound may depend on the box); $w$ therefore decays with $f$. Alternatively compactness of the finite gauge orbit gives a convergent subsequence. The limiting field is on the same orbit, remains in the chart, has $\delta a=0$, and obeys $X\le2\|\theta\|$. No size-dependent constant enters that final estimate.

5. **Growth, lines 65–75: the needed local repair.** Literally one cannot grow from a single site by one-coordinate layers while satisfying $n_\mu\le2n_\nu$: an intermediate side is zero while another is positive. Start instead with the unit four-cube. Use the coordinate-ordered tree from its origin. For any edge, comparing its tree paths reorders at most three coordinate steps; its gauged holonomy is a product of at most three conjugated elementary plaquettes. The group triangle inequality gives $|a_b|\le3\|\theta\|$. There are only 32 edges, so $X(0)+\|\delta a(0)\|\le C_{\rm seed}\|\theta\|$, with an absolute finite constant. Choose the energy threshold to meet step 4 and obtain the required seed. The all-zero box is separately trivial. These are all degenerate boxes allowed by the stated comparability condition.

   Grow by increasing a shortest unfinished side. Side ratios stay at most two: an unfinished shorter side is increased first, and a finished shortest side is already at least half every final side. Gauge the new normal links to the identity. Every new tangential link differs from the old face link by a plaquette factor, so smoothness of the logarithm gives difference at most $C|\theta_p|$. The old normal boundary term becomes the identical difference to a new zero link. A new tangential difference is the old face difference plus two plaquette errors; each occurs a dimension-bounded number of times. The new tangential boundary terms satisfy the same estimate. Thus $X(0)^2\le3X_{\rm old}^2+C\|\theta\|^2$, enlarging the absolute error constant if necessary. At old sites the divergence is unchanged. At new sites it is the old tangential divergence plus plaquette errors; the former equals the old normal boundary value because the old divergence was zero. This gives $\|\delta a(0)\|\le C\|\theta\|$. A single choice of $\epsilon_0$ now meets the flow's initial conditions at every stage. The flow resets the coefficient to two, rather than multiplying it by the number of layers.

The result is exactly $\|\nabla a\|^2\le4\|\theta\|^2$, $\|a\|_4+N^{-1}\|a\|_2\le C_U\|\theta\|$, and $\sup|a|\le\|a\|_4$, with absolute constants. This is an existence argument with an explicit order of threshold choices, not a numerical ODE proof.

**Where it could help their text.** `sa-map.md` Section 3's comparison is accurate only for this limited distinction. Outline Proposition 1a.3.8 (lines 7724–7740) and the local part of (1b) Theorem 2 (9684–9691) use pointwise curvature/current hypotheses, a bound proportional to the box side $M$ or $m$, and control derivatives and Hölder norms not supplied by U. U could supply a real initial logarithm gauge on a *small-total-energy* box, or the elementary cutoff estimate
\[
\|\theta(e^{i\chi a})\|_2
 \le C\bigl(\|\theta\|_2+N^{-1}\|a\|_2+\|a\|_4^2\bigr)
 \le C\|\theta\|_2,
\]
when the cutoff has gradient $O(N^{-1})$. This is relevant to real box continuation near Proposition 2.4 $17658 onward$ or an unspent low-energy window in the floor argument $18343 onward$, **provided the box energy hypothesis is actually proved**. Pointwise small plaquettes in a large box do not imply it: the energy sums over all its plaquettes. U does not preserve their tree gauge, multilevel data or seam boundary, does not supply the holomorphic response, and cannot be applied to an arbitrary old floor. It therefore does not replace those propositions or close their hardest item.

## (d) Can the heavy-wall examples sit in the old floor?

**CORRECT-NO-ADVANCE for using these examples to settle their floor-screening step; SHAREABLE AS A QUESTION.** Compact heavy pairs can be placed inside a sufficiently large geometric floor without changing their coarse averages. Neither note constructs an admissible history of the outline with those fields, its waiting collar and a failed renewed test. The long frustrated-boundary example cannot simply be transplanted with its proof intact. Neither is a checked counterexample to lines 18334–18415.

**The concrete mathematics rechecked.** In `heavy-wall.md` lines 8–39, two opposite direction-one links separated by two transverse spacings meet disjoint sets of six plaquettes. Their total squared-angle energy is $12a^2$, and their Wilson action is $e_A=12(1-\cos a)$. At $a=T/8$, Taylor's integral bounds give
\[
\frac{11}{24}a^2\le1-\cos a\le\frac12a^2,
\quad\frac{11}{128}T^2\le e_A\le\frac{3}{32}T^2.
\]
The lower bound follows from $1-\cos a\ge a^2/2-a^4/24$ and $a\le1$. Thus arbitrarily many disjoint copies have arbitrarily large fine energy. This is not a claim that one fixed finite box holds infinitely many copies: its depth must grow to fit them.

For the parent calculation, take the small-angle branch of the outline's actual map, lines 7063–7084. In a commuting subgroup the mean solving $\sum\log(V_iV^{-1})=0$ is exactly the exponential of the arithmetic mean of the angles, when all differences are within that branch. Averaging the closed paths and then multiplying by (U[c]) cancels the (-U[c]) angle, giving the straight-path mean plus the two endpoint contour means. Transverse reflection pairs the opposite links and all the contour orders, so both the straight contribution and the averaged contour contributions cancel. Choose $a$ also small enough for $\varpi_c<cL^{-2}$, or use only the verified small-angle regime; this extra condition matters when identifying our kernel with theirs. The first parents are identity and their further iterates are identity. This checks compatibility of the local cancellation with the outline's **mean** contours, not just with one staircase convention.

The shell arithmetic in `heavy-wall.md` is also valid: with $B_0=(K+1)T^2$, $n_k=\lceil2^kB_0/e_A\rceil$ gives $2^kB_0\le b_k<2^kB_0+e_A$. Summing through $m$, and using $(m+1)/2^{m+1}\le1/2$, gives
\[
\frac{a_i}{E_i}\ge\frac1{1+e_A/(2B_0)}\ge\frac{64}{67}>\frac12.
\]
This defeats that note's specified light-shell selection. It does not defeat all replacements: deleting whole isolated pairs preserves the identity parents and saves their entire action. Likewise $12Ma^2>\epsilon_0^2$ defeats an application of Lemma U to a patch containing $M$ copies, rather than the existence of every possible gauge. The conditional rough-seed construction in `heavy-wall.md` lines 51–59 still imports its compact lift and dropped-parent convention; those are not supplied for the outline by this check.

For `hw-fine.md` lines 28–55, deleting one of the two adjacent opposite-link pairs creates two plaquettes of action $1-\cos a$, but the total action drops from $20(1-\cos a)$ to $12(1-\cos a)$. Thus positive mixed cost is compatible with net payment. In its noncommuting square, $X^2=Y^2=-I$, $XY=-YX$ give $\frac12\operatorname{tr}(ABA^{-1}B^{-1})=1-2\sin^4t$. That shows a genuine interaction cost, but does not construct exact zero-parent factors at different levels. These two tests must not be upgraded to an obstruction to their R operation.

The stronger `hw-fine.md` example, lines 71–201, has a different boundary mechanism. With $d_x=f(x+1)-f(x)\in\{-1,0,1\}$, the gauge $g=\exp(f(x)s(y)Z)$ removes the direction-one links and produces only direction-two angles (f(x)(s(y)-s(y+1))). These are at most $\alpha=\pi/m$. The gauge is identity at first block centres. Averaging $f$ gives zero, and reflection cancels the contour means, so the first parents, then all parents, are identity. Increasing $m$ makes the outline's small-angle branch condition hold as well. Each endpoint has the same plaquette action, while $4m^4/L$ active plaquettes in a top cube give
\[
\frac{4m^4}{L}(1-\cos(\pi/m))\ge\frac{8m^2}{L}.
\]
Here $\sin t\ge2t/\pi$ gives the inequality directly.

Its minimizer claim can be checked against all SU(2) competitors, not merely diagonal ones. Identify SU(2) with the unit sphere in $\mathbb R^4$, so $\tfrac12\operatorname{Re}\operatorname{tr}(rq^{-1})=r\cdot q$. Put $q_y=\cos(y\alpha)e_0+\sin(y\alpha)e_3$, $\phi_y=\sin(y\alpha)$, and $\delta_y=r_y-q_y$, with endpoints fixed to $e_0,-e_0$. Expanding the energy and using $2q_y\cdot\delta_y=-|\delta_y|^2$ gives
\[
E(r)-E(q)=\cos\alpha\sum_{y=1}^{m-1}|\delta_y|^2
                 -\sum_{y=1}^{m-2}\delta_y\cdot\delta_{y+1}.
\]
Expansion of
\[
\tfrac12\sum_{y=1}^{m-2}\phi_y\phi_{y+1}
\left|\frac{\delta_{y+1}}{\phi_{y+1}}-\frac{\delta_y}{\phi_y}\right|^2
\]
gives exactly the same expression, by $\phi_{y-1}+\phi_{y+1}=2\cos\alpha\,\phi_y$ and the two zero endpoint values. All coefficients are positive. Retaining every transverse link as identity separates the longitudinal chains, and the other plaquette actions are nonnegative. Both endpoints attain the common lower bound, hence have zero removable excess with **those retained fine data**.

At $i=m/3,j=2m/3$, replacing one chain's value at $i$ by the target and retaining its value at $j$ forces the ratio $\delta/\phi$ to change from $-2e_3$ to zero. Weighted Cauchy–Schwarz gives a squared-difference sum at least $4/(4m/9)=9/m$, since $\phi_y\phi_{y+1}\ge3/4$ throughout that interval. Its energy cost is therefore at least $9/(2m)>0$. The displayed interpolation with slopes $-\alpha,3\alpha,\alpha$ is an admissible nonempty partial fibre and still has identity parents. A coherent gauge preserving all the transverse identity links is constant on each $x$-plane; the retained longitudinal identity links at $y=0$ make it globally constant, and the retained noncentral link at $y=m+1$ makes it commute with (Z). Thus that allowed gauge cannot identify the two endpoints. The obstruction is checked for this specified boundary problem.

**Comparison with the floor, line by line.** The outline's floor is the collection of level-$m_\flat$ cells of $\Omega_{m_\flat}^c\cap X$ not touching $\Omega_{m_\flat}$ (18335–18341). It is not the entire frozen side of an arbitrary fine boundary. The component must also be small, quiet, unjoined and quarantined for the preparation window (17575–17583); the prepared boxes are nonwrapping and separated. Its compatible field must obey the determining bonds and the actual recorded tests, with the special last-test exception, and its inner islands must belong to their real domains (18131–18165).

| Required identification | Heavy isolated pairs | Frustrated long-chain example |
|---|---|---|
| Fine field with small pointwise curvature, large total action and identity coarse averages | Yes, by the preceding hand calculation | Yes, by the preceding hand calculation |
| Put the unchanged local field inside a geometric floor with room to spare | Yes for finitely many compact pairs, if that floor contains their full blocks and read neighbourhoods | A finite restriction can be placed there, but the original periodic example and its boundary problem do not thereby embed |
| Produce that floor from the outline's creations, quiet waiting and quarantine | Not supplied; the small-field pair chain alone has no large-field component | Not supplied; identity parents and small fine plaquettes alone do not produce its required history |
| Retain exactly the data on which the obstruction depends | Pair deletion needs no frustrated retained faces | Essential thin slab faces throughout the example are not the thick nested boundary/determining set supplied by the outline |
| Violate a renewed test with unspent energy below its threshold | No such tested background is constructed | No such tested background is constructed |

In particular, restricting the periodic chain example to a nonwrapping box or cutting it off in the transverse directions changes its retained links and adds plaquettes. Its equality-of-minima and zero-excess calculation must then be redone; it does not survive by an assertion that the floor is arbitrary. Conversely, releasing those fine constraints permits the identity field, so the old positive minimum is no longer locked. Nor does the outline require a local replacement paid solely by removable excess: it keeps $e^{-A(x_i''\phi_c,U''(\xi))}$ as a full real inner Wilson weight (18060–18076). This is a different payment mechanism.

At 18343–18352 the outline bounds *unspent* window energy and infers small stored data; at 18353–18367 it then asserts the background screening bound; at 18369–18401 it uses shell surfaces, tree matching and chart admission to make each renewed test pass; at 18403–18415 it allocates the resulting witness only in the later containing component. The examples above address none of those last three identifications. They do show why replacing the hypothesis by “the coarse field is small, therefore the entire fine patch satisfies Lemma U” would fail. That replacement is not what the cited paragraph says.

**The exact shareable question:** for (floor-screening), what two admitted determining sets and data are compared, which boundary values are kept, and which regular-pair response estimate applies when the old floor is arbitrary? Give the support identity showing that all unbounded floor dependence lies behind the waiting collar, and show that the renewed test reads only the screened quantities. This is a request for the missing application, not a claim that either example refutes it. Checking the shell surface construction, the entire history admission, the response estimate on those domains and the witness allocation remains open here. Our upper chain cannot use their large-field route on the strength of these examples or their absence of a counterexample.

## (e) The reference normalizer and the missing positivity paragraph

| Step | Research verdict | Sharing verdict |
|---|---|---|
| The literal cross-reference at line 17508 has no target in (2e) | ADVANCE: checked textual defect | SHAREABLE, with the pinned location |
| Proposition 4.5 supplies the missing support/positive-measure argument | WRONG as an inference | NOT SHAREABLE as a justification; it is a different statement |
| Positivity and finiteness of the displayed reference law on an admitted real box | ADVANCE as the conditional hand argument below | SHAREABLE with the admission hypotheses |
| Those hypotheses have been verified on every required history support | CORRECT-NO-ADVANCE | SHAREABLE AS A QUESTION; not established here |

**What the text actually contains.** Line 17508 says that a normalizer outside $(0,\infty)$ causes a drop-out, and then says that this case does not occur on the supports, referring to `(2e), “Reality and positivity”`. The actual (2e) runs from 19408 to the module end at 19525. Its topics are the class, Theorem 2.11, the order of constants and closure; there is no such paragraph. A whole-file search for that title finds the reference and Proposition 4.5 at 22602, whose title expressly restricts it to real sources. Reading that proposition confirms that it concerns real exponents and nonnegative history measures, not an open set of free variables for the reference denominator. The small-ball lower bound at 18734–18750 is for the truncated **gauge** normalizer $z(\theta,\epsilon)$, not for $\mathsf s_X$'s background-dependent Wilson denominator. The read-region discussion at 18877–18905 includes the reference normalizer as data; it does not prove its positivity.

The strongest accurate answer to “supplied anywhere” is therefore: **the direct support proof asserted at the cited destination is absent; the defining formula and the real box-background statement provide ingredients for a conditional proof.** No separate proof identifying a positive-measure admitted set for every required support was located by the reference-law/normalizer/denominator/positivity searches and the associated excerpts read here. This is not a claim to have checked all 33,000 lines or every implicit consequence of the manuscript.

**Hand proof of the local conditional statement.** At 17604–17608 the denominator is, with its tree and frame fixed,
\[
D_X=\int dV'\,\delta_{\rm ax}(V')\,
  1_{\{|\log V'_b|<M_0\varepsilon_k\}}
  \exp\{-\theta_k A(\phi_X,U_{k,X}(V'V_\Lambda))\}.
\]
Here $\theta_k$ denotes the real choice of coupling used by the kernel; in the unsourced run in that display it is $x_k$. This notation does not replace a complex running action by its real part. Line 17508 and the opening of (2e) distinguish the real frame, which determines the reference law, from the density and sources.

Assume (i) the real critical configuration $V_\Lambda$ exists with the specified exterior and tree representative; (ii) its tested curvature is strictly inside the real continuation class of Proposition 2.4; (iii) the entire integration cutoff is in the domain where $U_{k,X}$ exists and is real, or the integrand has a specified bounded nonnegative definition on its remainder. These are genuine hypotheses, not consequences of positivity. The constants $a_\Lambda,M_0$ are chosen before the coupling ceiling in the order at 19469–19472. If the bound of Proposition 2.4 holds and the exterior has the stated $O(\varepsilon_k)$ size, lowering that ceiling can give both the strict margin in (ii) and (iii), because $M_0\varepsilon_k\to0$. The present check does not rederive that background theorem or the assertion that every history supplies its hypotheses.

After using the tree delta functions, let $q$ be the number of remaining SU(2) bonds. Haar invariance makes the product tree elimination have Jacobian one; the external tree bond removes the residual constant gauge, as specified at 17598 and 17604. The measure is product Haar on these free bonds, not a positive measure assigned to the tree slice inside the original full-dimensional Haar space.

Let $\mu=a_\Lambda-\max_p|\partial V_\Lambda(p)-1|>0$ on the relevant plaquettes. Choose
\[
0<\rho<\min\{M_0\varepsilon_k/2,\ \mu/8,\ \rho_{\rm chart}/2,\ 1/4\},
\]
where $\rho_{\rm chart}>0$ is a real domain radius about $V'=1$. On each free bond put $V'_b=\exp(i h_b)$, $|h_b|<\rho$, and put the tree bonds at identity. This is a nonempty open product set in the free coordinates, and every cutoff equals one. A telescoping product of four unitary factors bounds the change of a plaquette by $4\rho$, so the continuation class remains strict. Haar measure has positive density in this identity chart: in the SU(2) coordinates $\cos|h|+i\sin|h|\widehat h\cdot\sigma$, its density is a positive constant times $(\sin|h|/|h|)^2$, positive for $|h|<\rho$. Hence this product set has positive measure. If $q=0$, its measure is the unit mass of the empty product, and the same argument applies.

For a real background, every Wilson plaquette action lies in $[0,2]$. Consequently, with $C_X=2|\theta_k|\sum_p|\phi_X(p)|<\infty$,
\[
e^{-C_X}\le\exp\{-\theta_k A(\phi_X,U_{k,X})\}\le e^{C_X}.
\]
The lower bound on the open product set proves $D_X>0$. Hypothesis (iii), the upper bound and finite Haar volume prove $D_X<\infty$. No uniform lower bound in volume, cutoff or coupling has been proved or needed for this elementary conclusion. If a later estimate needs a quantitative price for $D_X^{-1}$, this existence proof is not that estimate.

**Why the source distinction matters.** A positive real exponential alone does not imply a strictly positive integral: its admitted set might have zero measure or be empty. Proposition 4.5 does not answer that issue. Conversely, the reference kernels are fixed positive draws independent of $w$, even when the bare measure is complex (17500–17508). Therefore “4.5 is only at real sources, so the complex-source reference denominator cannot be positive” is also an invalid inference. The missing application is the real admission and positive-measure support statement. Analytic nonvanishing of a *source-dependent* partition function would be a different obligation.

The default drop-out rule makes the abstract move total even before the stronger claim is proved. It does not prove that no extra drop-outs occur on the intended supports, nor that all formula-level cancellations and rarity gains for those histories apply. The conditional argument above is a concrete repair candidate for the missing paragraph, with its remaining input stated; it grants no closure of Package C.

## Defects and limits in our notes

1. **Curved operator identification, `rel-phi-c.md:177` and `:551`.** Theorem R's hand estimate controls the explicitly summed transported operator. The comparison with the curved recursion is left unbounded, so its advertised use by that consumer is not established. Repair remains unproved: bound the curvature-weighted intermediate-centre remainder on the actual determining sets, or state the theorem only for the defined summed operator. This is the consequential open defect, not a refutation of the annular Hölder estimate.
2. **Input units, `rel-phi-c.md:67` and `:73`–`:80`, compared with `:276`.** The earlier operator takes link logarithms, whereas the (REL) notation feeds it the top-normalized field. The displayed Example E uses the former. Section (b) gives an explicit eight-bond counterexample to the literal unrescaled operator/norm bound and fixes the convention as the operator applied to H/B. This repair must accompany any sharing of the precise bound; the intended rescaled implication survives.
3. **Induction seed, `lattice-uhlenbeck.md:67`.** A single-site box cannot be enlarged one direction at a time while all side ratios stay within two. Section (c) gives a finite unit-cube seed, with a hand spanning-tree estimate, before the comparable-box growth. The N-inverse norm assertion concerns N at least one; the bondless point is just a trivial initial object. This is a local repaired proof defect, not a counterexample to Lemma U.

## Coverage and recovery point

The source revision is the pinned checkout, not current remote main. The outline is the single downloaded copy of `YM4_sketch_500.tex` at `31a47c543775`, SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. The repository source identities are fixed by `199fac1cbf3a6a22aae818c020bede2e1a3c433a`; all seven library files used here were unchanged at the final source check.

Read first: GOAL and FINISH lines 177–209 and queue row 75. The pinned `docs/ai_methodology/SCIENCE_WORKFLOW.md` was also read through `git show` in ranges 1–110, 111–203 and 204–end, without checking it out. The task's scientific reads are identified in each section. In addition to the complete relevant arguments of (a)–(c), the outline excerpts cover A3 (3820–3907), its averaging/gauge definitions (7050–7085, 7100–7156, 7187–7197, 9610–9658), the local box gauges (7715–7762, 9680–9691), the Landau pair and response statements (9693–9752), the operation and reference law (17490–17524, 17558–17690), action cancellation and healed sums (17838–18185), the complete cited floor paragraph (18334–18415), gauge-normalizer and restriction passages (18726–18759, 18854–18905), the complete (2e) in separate bounded ranges (19408–19528), and Proposition 4.5 with its nearby context (22583–22630). Source searches located other normalization occurrences; they did not provide a replacement proof of all-support admission. `sa-map.md` Sections 1 and 3 were comparison aids, not evidence for the outline's assertions. Only the relevant bounded excerpts of those sections were read.

Not checked: the outline's complete A1–A4 derivations, complex/hereditary-domain closure, the ten signed terms needed for 2.8, the full 2.10 cluster expansion and measure identities, admission of an actual counterexample history, the shell spanning-surface construction in the floor paragraph, the complete support induction, or Theorem 0. In our notes, F/RF filling, Lemma CAP, nonlinear (REL), nonlinear GLUE-E, WAM and the upper-chain consumers are not certified. The independent papers of Balaban, Uhlenbeck and others were not imported as proved premises. No runner, floating-point evaluation, enumeration, audit or subagent contributed mathematical evidence.

The recovery decisions are therefore concrete: preserve the flat seam proof and the repaired real box gauge; do not replace the actual curved contour map by its flat/summed proxy; do not send either wall example as a refutation of the old-floor route; ask for the actual floor-screening/admission application; and distinguish the elementary real positive-integral argument from its unverified universal support premise. No other lane or file was advanced.

## Findings in the outline

1. **Broken proof reference for support positivity.**
   - **File:** Ethan Sussman and Levent Alpoge's `YM4_sketch_500.tex`, with Claude and Codex as authors of their text.
   - **Commit:** `31a47c543775`.
   - **Line:** **17508**; claimed destination `(2e)` is at **19408–19525**; the similarly named Proposition 4.5 is at **22602**.
   - **Claim:** the reference normalizer never fails to lie in `(0,infinity)` on the supports, with proof attributed to a paragraph called “Reality and positivity” in (2e).
   - **Checked defect:** that paragraph is absent from (2e). Proposition 4.5 is about reality and positivity at real sources; it does not exhibit the admitted positive-measure set for this denominator.
   - **Explicit failure:** following the cited proof edge reaches class assumptions and closure/order-of-constants text, not a proof of a nonempty open set of free reference variables on each relevant support. Positivity of the exponential is insufficient by itself: an integral over an empty or measure-zero admitted set is zero. The source-independent reference law avoids a supposed complex-source sign objection, but not this admission obligation.
   - **Disposition:** the cross-reference is wrong. The normalization conclusion is **not refuted**. Section (e) supplies a conditional local repair and lists the remaining hypotheses. This finding does not invalidate the abstract total-kernel construction, which has an explicit drop-out fallback, and does not prove that a bad normalizer actually occurs.

No checked counterexample to A3, Theorems 3/4, Propositions 2.8/2.10, or the old-floor estimate is reported. Open or unverified obligations have not been relabelled as false statements.
