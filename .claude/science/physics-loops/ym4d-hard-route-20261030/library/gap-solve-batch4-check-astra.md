# Repo search

<!-- Work plan
1. Check the pinned checkout, prior search, ownership and task instructions.
2. Locate the external statements in the supplied indexes and read their cited ranges.
3. Check the J statements.
4. Check the L statements.
5. Check the N statements.
6. Check the S statements.
7. Check the route-closing arguments, reconcile the verdicts and append one RESULT line.
-->

Codex hand check, FINISH 1247 (gpt-6.2-astra, max), on `d9d52d534de9413b0daf05876965d3e10fac63d9`. This
research check grants no status. Claude Fable 5.2 wrote J through step 3 and all of L. Claude Opus 5.5
wrote J from step 4 and all of N and S. Line numbers below refer to this commit.

The lead’s November 8 search covered main and PRs 10114, 10133, 10134 and 10141. Its thirteen targets
concern the construction of the continuum theory. The closest soft-route hit,
`MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 on PR 10114, bounds a one-step loop correlation. Main’s
finite-clock Villain note 79–94 uses a different group. Its massive Wilson-loop curvature note 120–145
treats a determinant-weighted Dirichlet law. I checked those passages. Main’s
`research/mass-gap/library/gap-seed-limit.md` 188–202 and its check 175–190 already give the conditional
limit implication, including the totality requirement. I use that boundary below. There is no
batch-specific prior file or additional owner for this check in `library/open-registry.md`. The earlier
check of NS0 and the authors’ previously established inputs are cited where used.

Other nearby hits named by row 1218 were checked at source. Grok’s PR 10133,
`MASS_GAP_CROSSOVER_REDUCTION.md` 77–86, leaves the crossover and source estimates open. PR 10134,
`mass-gap-interface.md` 13–23, distinguishes nonempty excitations from a positive threshold. PR 10141,
`fp1.md` 299–315, controls a constrained classical field. Main’s `gap-phys-seed.md` 305–329 gives a
conditional periodic thermal criterion. None checks the four notes below.

## Published inputs

Credit for the outline and complete account at `31a47c543775` goes to Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text. From `sa-index`, chunk 02, rows 88–104, outline 2197–2231
and 2315–2335 give positive Wilson convolution coefficients at positive coupling and the gauge-projected
torus trace GL8. They supply inputs to L. Chunks 01, 03 and 29 and the corresponding obligations point to
outline 588–599, 3717–3720 and 31871–31882. Their example has spectral density reaching zero despite
decay. CA-I 2704–2711 and 3218–3222 explicitly leave the mass gap open. The “twist” in the items
4.12–4.19 index, CA-I 44875–44881, is a change of constrained minimizer. Its datum is a change of block
average. The index search located no previous check of these four notes. Row 1009 records the scope of
OpenAI’s two-dimensional $O(4)$ stiffness and positivity arguments. Jian Ding, Fenglin Huang and Pu Yang
developed the related $O(N)$ result cited in the notes.

## J · crossed twists and level flow

Source file [gap-mini-solve-j-fable.md](gap-mini-solve-j-fable.md), row 1200. Write $L$ for the side in
lattice sites.

- **Lemma M(a), 163–171 — HOLDS.** Only the double seam in plane 12 gives a nonidentity commutator. It
  equals $-1$ and cancels its flip. Plane 34 has $L^2$ uncompensated flips at cost two each. Thus the
  action is $2L^2$. At side one it is $2<4$. At side two it is $8<32(1-1/\sqrt2)$, since $1/2<9/16$. This
  is a competitor, with no claim that it minimizes among all fields.
- **Lemma M(b), 167, 173–175 — HOLDS.** In each twisted coordinate slice the abelian curls telescope.
  Including the one flip gives total angle $\pi\bmod 2\pi$. The absolute principal angles therefore have
  sum at least $\pi$. Lower them to sum $\pi$, which can only lower the cost. For $f(s)=1-\cos s$,
  replacing any pair $a,b$ by their mean saves $2\cos((a+b)/2)[1-\cos((a-b)/2)]\ge0$, since $a+b\le\pi$.
  Among minimum-cost tuples choose one minimizing the sum of squares. Averaging any unequal pair
  contradicts this choice. The cost is at least $m f(\pi/m)$, also for $m=1,2$. Sum over $L^2$ slices in
  each of planes 12 and 34 with $m=L^2$, and use nonnegativity in the mixed planes. V attains the result,
  including its constant-link extension at $L=1$.
- **Lemma M(c), 169, 177–179 — HOLDS.** Fix *any* site. If its six coordinate two-tori were defect-free,
  cut each along the two based cycles to a square. Moving a path across one face multiplies its transport
  by the central sign of that face. Sweeping the square therefore equates its boundary commutator to the
  product of its signs. The pairs 12 and 34 would anticommute and all four mixed pairs commute.
  Anticommutation makes each element conjugate to its negative, so both real parts vanish. For pure
  imaginary unit quaternions, their vanishing anticommutator makes their axes perpendicular. Their common
  centralizer is $\{1,-1\}$. The last two holonomies would be central and could not anticommute. This
  proves the stronger pointwise wording in the results table. Missing a coordinate value in every
  direction gives a site whose six tori all avoid the defect. This support statement sets no action
  threshold for a defective plaquette.
- **Lemma V(a–c), 70–79, 215–217 — HOLDS.** In each active plane the abelian curl is $\phi=\pi/L^2$,
  except for $\phi-\pi$ at the double seam. Its sign flip restores $\cos\phi$. All mixed curls vanish.
  Each active plane costs $L^4(1-\cos\phi)$, between $2$ and $\pi^2/2$ by the two chord bounds. Adding
  $c_\mu$ cancels in curls. In directions 1, 2, 3, 4 the winding angles are
  $Lc_1-\pi x_2/L,Lc_2+\pi x_1/L,Lc_3-\pi x_4/L,Lc_4+\pi x_3/L$. For each direction the traces at
  transverse coordinates 0 and 1 recover both sine and cosine of $Lc_\mu$, since $\sin(\pi/L)\ne0$ for
  $L\ge2$. This checks all four continuous parameters. Removing the second flux gives the one-plane cost.
  The M(a) seam field now has zero cost.
- **Feynman–Hellmann identity, 193–197 — HOLDS.** Fix the spatial lattice and a differentiable isolated
  level branch with positive splitting $D=E_i-E_0$. Differentiating its normalized eigenvector equation
  cancels the eigenvector derivatives. Subtract the ground-state equation, then integrate
  $d\log D=-\kappa_i\,d\beta/\beta$. The integration limits give the sign in line 197. The result
  concerns the specified Hamiltonian and a branch on the interval. An isotropic Wilson transfer energy
  requires a separate identification.

## L · transfer in the two slab directions

Source file [gap-mini-solve-l-fable.md](gap-mini-solve-l-fable.md), row 1202. Here $\beta>0$, $R_i\ge3$,
$T\ge2$, and the pin-only plaquettes are omitted.

- **Lemma 2, 73–94 — HOLDS.** Slice perpendicular to direction 1. The free direction-1 links integrate to
  the interior gauge projection $P$. The plate endpoints of that projection are fixed. The convolution
  $C$ on all slice links commutes with $P$. Its eigenvalues are products of the strictly positive GL3
  coefficients. Their multiplicity-weighted sum is finite. Thus $T_x=e^{-V/2}PCPe^{-V/2}$ is trace class
  and strictly positive as a quadratic form on $\operatorname{ran}P$. Simultaneous top right translation
  preserves $V$ and commutes with $C,P$. Only the seam changes, giving $\operatorname{Tr}(T_x^{R_1}R_h)$.
  Taking the trace on each spin multiplicity space gives $m_j\ge0$. Matrix entries of a bottom-to-top
  parallel transport are interior-gauge invariant and realize every spin, so every $m_j>0$. Absolute
  convergence follows at $h=1$. Spin $1/2$ gives strict inequality for $h\ne1$, and the original integral
  is positive. Smoothness of the finite integral gives rapidly decaying character coefficients by
  iteration of the group Laplacian. The mean of $m^2$ over $m=-j,\ldots,j$ is $j(j+1)/3$. This gives
  precisely the logarithmic stiffness. The winding functions $e^{in\theta}$ of the open line give the
  same strict positivity for each integer charge of compact $U(1)$.
- **Lemma 3, 157–169 — HOLDS.** The first two derivatives of the perturbed log weight are $-J$ and
  $-\beta\sum_x\operatorname{tr}c_x/(8R_1^2)$. Differentiation under the compact integral gives
  $-\partial_\phi^2\log R_T=D-\operatorname{Var}J$, hence the Casimir formula above. The law of total
  variance gives line 165 for the stated conditioning. In fact, for $SU(2)$ and **each** fixed exterior
  $A$, common right rotation of all $g_x$ conjugates every $c_x$ and preserves the conditional density.
  Choosing the rotation that sends $\sigma_3$ to $-\sigma_3$ gives $\mathbb E[J\mid A]=0$. This affects
  the use of Lemma 3 at line 153.
- **Proposition 5(a–d), 108–122 — HOLDS** for the full gauge-invariant box. Writing $M=e^{-W/2}$, the $T$
  vertical kernels have $T-1$ intervening factors $M^2$. The two outside factors give the vectors
  $u_b,u_t$, with $T_v^{T-2}$ between them, including the identity at $T=2$. The kernel is continuous and
  everywhere positive on the compact configuration space. The principal eigenvalue is simple, with
  strictly positive continuous eigenfunction. The pointwise eigen-equation gives
  $\langle u_\omega,\psi\rangle=\lambda e^{W(\omega)/2}\psi(\omega)$ for a real eigenfunction. For
  complex ones the diagonal bound uses $|\psi(\omega)|^2$. Removing the vacuum bounds the remainder by
  $q^{T-2}\|u_b\|\|u_t\|$, $q=\lambda_1/\lambda_0$. The flat pins have the same $W$, their vector norms
  are bounded, and the vacuum denominator is positive. Division gives line 118. For an eigenfunction at
  $\lambda_1>0$, choose any pin at which it is nonzero. The diagonal spectral weights are squares, so the
  worst rate over **all** pins is exactly $q$. Restricting to torons or to neutral states is a different
  assertion.
- **Corollary 5.1, 124 — HOLDS.** For $U(1)$,
  $e^{-\beta A\alpha^2/(2R_1T)}\le R_T(\alpha)\le1$. Fourier integration yields the unit point mass at
  $n=0$. One can also translate the transfer variables by any fixed flat abelian field, which preserves
  the kernel and its unique positive vacuum.
- **Corollary 5.2, 126 — HOLDS.** For $SU(2)$, character orthogonality and uniform convergence
  give each limiting coefficient. The uniform bound on $\mathbb E[j(j+1)]$ makes the laws tight, and
  passage to finite partial sums preserves the moment bound in the limit. Central translation of the seam
  commutes with $T_v$ and fixes the positive normalized vacuum. Thus $R_\infty(-h)=R_\infty(h)$ and the
  half-integer coefficients vanish.
- **Proposition 6(a), 132–134, 146 — HOLDS.** Independent left and right plate actions commute. Inserting
  the two seam kernels yields the double trace and independent conjugation invariance. Inverting a class
  angle has no effect on an $SU(2)$ character.
- **Proposition 6(b), 136, 146 — HOLDS** as a *matrix-valued* moment statement. With $t=T-2$, its
  representing measure is $dM_{jk}(s)=\langle v_j,E_{T_v}(ds)v_k\rangle$. Each finite compression is a
  positive matrix measure, so every quadratic form is a scalar positive moment sequence. Crossed transfer
  separately gives $m_{jk}(T)\ge0$ entrywise. Off-diagonal spectral weights can have either sign. For
  example, $\operatorname{diag}(1,1/2)$ and vectors $(1,1),(1,-1/2)$ give positive entries $1-2^{-t-1}$
  with a negative atom at $1/2$.
- **Proposition 6(c), 138, 146 — HOLDS AFTER CORRECTION.** The interior central gauge flip equals the
  product of the endpoint flips, hence $j-k\in\mathbb Z$ on every nonzero block. In the vertical channel
  the seam-center operator $C_1$ sends $u_h$ to $u_{-h}$ and $C_1v_j=(-1)^{2j}v_j$. This specifies the
  flux in direction 1 alone. Lines 138 and 148 do not project onto the other two center charges, and a
  character channel need not span its entire flux sector.
- **Proposition 6(d), 140, 146, 148 — HOLDS AFTER CORRECTION.** The vacuum projection gives the displayed
  rank-one asymptotic with the **full** $q$. Its leading factors obey $a_0>0$ and $a_j\ge0$ by entrywise
  positivity against column zero. Smoothness in $h$ gives $\sum_j d_j a_j=\langle\Omega,u_1\rangle$ by
  character expansion. The normalized joint law therefore tends to the product of the two limiting laws.
  An excited eigenfunction visible on the torons has a nonzero character coefficient, hence a nonnegative
  term of its own rate in some diagonal entry. If the first excited eigenspace has zero overlap, these
  entries can converge faster. An eigenfunction odd under reflection in direction 2, for example,
  vanishes on every one of these torons. Subtracting the trace on a reflected plaquette from that on the
  original produces a nonzero odd, gauge-invariant function. Compactness and injectivity of $T_v$ on this
  subspace then give such eigenfunctions. The unprojected entries have no bound by a center-neutral gap
  from this argument. The ratio at line 148 additionally needs nonzero leading factors.
- **Proposition 6(e), 142, 146 — HOLDS.** Independent conjugations reverse either angle separately. The
  mixed derivative vanishes. For $U(1)$ a common flat translation removes the bottom angle, giving
  $\log Z_T(\alpha_t-\alpha_b)$. The mixed derivative at zero is $\sum n^2m_n/\sum m_n>0$.
- **Proposition 6(f), 144, 146 — HOLDS AFTER CORRECTION** to the operator convention. The site
  transformation factors as an interior gauge transformation and the top endpoint transformation
  $\rho_k:g\mapsto gk^{-1}$. With the representation of line 88, its unitary action by inverse pullback
  is $R_k$. Direct substitution $f\mapsto f\circ\Gamma_s(k)$ gives $R_{k^{-1}}$. These agree with the
  respective conventions only. Differentiation splits the generator into the right action on links
  crossing the cut and simultaneous conjugations above it. In the abelian case the latter generator is
  zero.
- **Lemma 1, 65–71 — HOLDS.** Gauge invariance is an endpoint
  change of Haar variables. The top gauge $\eta^{x_1}$ takes the spread pin to the seam pin, and a pure
  gradient is gauge-equivalent to the identity.
- **Proposition 4(a), 98, 102 — HOLDS.** Average the relative Wilson term over common
  top rotations. It gives $(\cos(\phi/(2R_1))-1)\mathbb E\operatorname{tr}c_x$. Jensen,
  $|\operatorname{tr}c_x|\le2$ and $1-\cos s\le s^2/2$ give the exponent $-\beta A\phi^2/(8R_1)$ and the
  stated curvature bound.
- **Proposition 4(b), 100, 104 — HOLDS.** An abelian shift linear in height changes exactly $R_1AT$ curls by
  $\pm\alpha/(R_1T)$. Their mean sine is zero. The same Jensen inequality gives
  $-\beta A\alpha^2/(2R_1T)$. These reproduce the earlier TWIST/REM and blind bounds as the author
  credits.

## N · association and adjoint Haar moments

Source file [gap-mini-solve-n-fable.md](gap-mini-solve-n-fable.md), row 1213. The projective plane and
its Haar integral are inputs from Claude Fable 5.2, row 737, checked in row 744 (gap-skeleton-final.md
616–624). EP-NO is Claude Opus 5.5’s conditional theorem in gap-loop-eq-opus.md 118–131.

- **FKG-NO(a), 42–49 — HOLDS given NS0.** The two functions are products of nonnegative increasing
  factors. In a nonempty proper subset of the 92 faces some pair of adjacent faces straddles the subset,
  since face adjacency is connected. Their common link occurs exactly once in the retained monomial. The
  center change $U_e\mapsto-U_e$ kills its Haar mean. Consequently the empty contribution cancels in the
  covariance and the sole surviving term is $2^{-92}(-2^{-183})=-2^{-275}$.
- **FKG-NO(b) and the center-even state, 46–50 — HOLDS given the stated mixture.** The 184 support links
  meet at most $6\cdot184$ faces. With the EP-NO convention $e^{\sum_p\beta_p x_p}$, the conditional log
  weight has oscillation at most $2208\beta_{\max}$. Each of the three moments of $F',G',F'G'$ differs
  from its Haar value by at most $\delta=e^{2208\beta_{\max}}-1<2^{-278}$. Put the closing electric seam
  off the embedded surface. Inserting $P_{\rm ev}=2^{-3}\sum_e C^e$ gives the positive mixture with
  weights proportional to the twisted partition functions (gap-flux-exercise.md 421–445,
  gap-means-astra.md 277–291). The three moment bounds persist after averaging the exterior and these
  twists. For numbers in $[0,1]$, $|ab-a'b'|\le|a-a'|+|b-b'|$, so the covariance changes by at most
  $3\delta$. This proves strict negativity without averaging covariances. Line 84 writes $2\beta x_p$
  instead. Even with that convention $\delta<2^{-277}$ and $3\delta<2^{-275}$. For the compact $U(1)$
  remark at 47, 52, **HOLDS** for the stated pair. Products of cosines have nonnegative cosine
  coefficients. In the two-copy covariance integral put the angles equal to $u+v,u-v$ using Haar
  invariance under this surjective torus map. A cosine difference is $-2\sin(a\cdot u)\sin(a\cdot v)$.
  Expanding $\prod_p \exp(2\beta_p\cos(p\cdot u)\cos(p\cdot v))$ expresses the covariance of two cosines
  as a sum of squares with nonnegative coefficients.
- **PAR, 64, 76 — HOLDS for the factorization.** The invariant subspaces in tensor degrees two and three
  of the real vector representation are the lines of $\delta$ and $\epsilon$, of squared norms 3 and 6.
  Haar integration projects onto these lines. On a reversed link the transpose interchanges matrix
  indices, so each corner still identifies the two indices at the same site. Integrating the links leaves
  the product of the site contractions divided by $3^{E_2}6^{E_3}$. **Slot-order sentence, 76 — HOLDS
  AFTER CORRECTION.** An odd reordering changes both endpoint signs only at a trivalent link. At a
  bivalent link $\delta_{ij}=\delta_{ji}$, so neither sign changes. The total is invariant in both cases.
  A singly incident link gives zero by the degree-one integral, which supplies the “at most three”
  extension in line 117.
- **Surface and disc inputs, 60, 66–68 — HOLDS for the stated adjoint spin.** On a closed surface each
  site has one index cycle worth 3 and each link contributes $1/3$, giving $3^{V-E}=3^{\chi-|P|}$. On a
  disc the interior cycles contribute $3^{V_{\rm int}}$, the interior links $3^{-E_{\rm int}}$, and the
  boundary strand traces its holonomy. These give the recalled gluing rules in the required real
  representation.
- **Box with one wall, 70 — HOLDS.** The two discs of five faces each give $3^{-4}\chi(R)$. The wall adds
  $\chi(R)$ and its boundary product is Haar. Since spin one occurs once in $1\otimes1$, $\int\chi^3=1$.
  The answer is $3^{-8}$. The theta contractions in line 76 reproduce the same result.
- **Box with two walls, 72 — HOLDS.** Each of four disjoint disc interiors contributes $3^{-3}$. Fixing
  the central link and eight spokes to one leaves four independent Haar holonomies. For alternating ones
  the cubic projector gives $(\chi(x)\chi(y)-\chi(xy))/6$, by
  $\sum_a\epsilon_{aik}\epsilon_{ajl}=\delta_{ij}\delta_{kl}-\delta_{il}\delta_{kj}$. After squaring this
  numerator the three integrated terms before their binomial coefficients are $1,1/3,1/3$. Indeed
  $\chi^2=\chi_0+\chi_1+\chi_2$, so convolution with $\chi$ retains only $\chi/3$. The full integral is
  $3^{-12}(1-2/3+1/3)/36=3^{-15}/2$. PAR itself is unnecessary at the four-valent central link.
- **Pinching, 74 — HOLDS AFTER CORRECTION.** Condition on the common tree. The two sets of remaining link
  variables are independent. Each *conditional integral* is gauge invariant in its tree links and
  therefore constant, since site gauges set all tree links to one. A raw integrand can vary with a tree
  link. On a single plaquette with its other three links set to one it is $\chi(U_e)$.
- **Four-cube, 78 — HOLDS.** Three opposite-edge matchings partition the edges of $K_4$, so there are
  $3!$ proper three-edge colorings. In the stated order the representative has signs $+,-,+,-$. A global
  color permutation affects four signs and preserves their product. All 16 sites give $+6$ and all 32
  links give $1/6$. Hence $I=6^{-16}$. These three examples are strict positive moments. They impose no
  sign on all branched surfaces.

## S · a twist at the junction of a plate and the side faces

Source file [gap-mini-solve-s-opus.md](gap-mini-solve-s-opus.md), row 1228. Its cells include fully
pinned plaquettes, with the sharing weights of gap-pinned-cell-gauge-max.md 131–147. This differs from
L’s omission of pin-only plaquettes.

- **P1, 64–76 — HOLDS.** Put the site gauge equal to $g$ on the whole bottom face and to one elsewhere.
  Tangential bottom links stay trivial. Precisely the outgoing normal links acquire $g$ on the left. On
  the junction these are the new pins, and on the rest of the plate this is a Haar change of the
  integrated variables. Each trace is preserved.
- **P2(i–iii), 78–97 — HOLDS.** Extend the junction data and left-translate the free plate normals. For
  each affected face cyclicity places the two rotations next to one another. Its new real trace is
  $t_p\cos(\epsilon\Delta u)-(a\cdot s_p)\sin(\epsilon\Delta u)$. Differentiating $-\log Z$ gives the
  stated direct term minus the variance, with the weights inside the current. Two extensions differ by
  changes of integrated variables. Dropping the variance, bounding $|\beta_p t_p|\le b$ and minimizing
  yields $H_c\le bD_3$. A constant extension gives zero, even with arbitrary side pins. The argument
  supplies no nonnegativity for an arbitrary pin.
- **P3, 99–107 — HOLDS.** Translate the integrated *ring* normal links by the chosen deterministic
  extension before conditioning. Their product Haar measure is invariant. At fixed ring, each face weight
  is split so that its shares sum to the parent weight. The conditional partition function factors into
  child partition functions. Differentiating the outer integral twice gives
  $\mathbb E\sum H_{c'}-\operatorname{Var}(\sum J_{c'})$ with the covariance between different child
  currents included. Only bottom children receive shifted links. Their bottom tangential pins are trivial
  for every ring realization.
- **P5(a), 161–170, 181–193 — HOLDS AFTER CORRECTION** to the meaning of the noncompact Gaussian
  integral. For $b>0$ the minimum of the quadratic energy is well defined as printed. For $R\ge2$ a
  gauge parameter supported at one interior site gives a nonzero gradient with zero curl and zero
  tangential boundary data.
  Unrestricted Lebesgue integration along it makes the partition function infinite. Quotient the
  zero-boundary curl kernel, or fix an interior gauge. Completing the square on its orthogonal complement
  gives the pin-independent determinant and $H_c=bE_c(\dot p)$. Under subdivision one can first quotient
  the child kernels and then the remaining ring kernel. For the bound, the gauge $-u$ on the plate makes
  all tangential 1-links there equal to $\theta/R$. It cancels the prescribed normal shifts. With
  $A_1=(\theta/R)\phi(t,d_2,d_3)$ and the other components zero, all pin conditions hold, including on
  faces normal to direction 1. Each curl is a difference of $\phi$ multiplied by $\theta/R$. For the
  angular cutoff of lines 188–192, the gradient of $\arctan(s/t)$ has size $(t^2+s^2)^{-1/2}$. The
  isolated corner edge has bounded difference. At $t=0,s>0$ the first vertical difference is bounded by
  $C/(1+s)$. Shell $k=t+s$ has $O(k+1)$ edges, giving $O(1+\log R)$ in two coordinates. The spectator
  coordinate and the linear top cutoff give $D(\phi)\le CR(1+\log R)$. Summation over $x_1$ gives the
  asserted $Cb\theta^2(1+\log R)$.
- **P5(b), 171–180 — HOLDS AFTER CORRECTION** to the wall count. The flux on each selected pinned wall
  face is $\pm\theta/R$. At an intersection of two internal walls there are four quarter shares. This is
  where the count of two halves at line 179 fails. Summing *all* incident bottom cells gives weight one
  at $0<x_3<R$ and at least one half at each endpoint $x_3=0,R$. For each internal $x_2$ wall there are
  $R$ choices of $x_1$ and total transverse weight at least $(R-1)+1=R$. No face is repeated between
  distinct $x_2$ walls. The lower bound is $(L-1)b\theta^2$, including cells of side one.
- **P5(c), 173, 193–202 — HOLDS** with the same Gaussian gauge convention. Conditional Gaussian Hessians
  are independent of the actual pins. The variance is the difference between the sum of these Hessians
  and the parent Hessian by P3. Its displayed lower bound follows. For $\theta\ne0$, the surviving
  fraction is at most $\min\{1,C(1+\log R)/(L-1)\}$. Only when the second bound is small does this force
  cancellation of nearly the entire sum.

## Arguments used to close routes

### J · the twist, the topological charge and the flow of a level

- **One-loop sign and volume of the flat family, J52, 58–66, 81, 89, 156 — HOLDS AFTER CORRECTION.**
  With $L$ measured in sites the winding periods in $c_\mu$ are $2\pi/L$. The link metric multiplies their
  lengths by $L^2$, giving four lengths of order $L$. A path of equal action gives neither the transverse
  fluctuation integral nor the normalizing integral in the other sector. The one-loop arithmetic
  $16\,2^{-1/3}=2^{11/3}$ holds with the cited semiclassical inputs. For a strict gain the *total* scalar
  loss must be less than 16, or an *additional* loss less than $2^{11/3}$. The opposite signs explain why
  separate upper bounds in the cited direct calculation do not suffice. They give no general
  impossibility theorem for stiffness arguments. The determinant and zero-mode interpretation is credited
  to the authors named at J60 and J128.
- **Three attempts on (X), J85–95, 253 — HOLDS as a diagnosis of those attempts.** Time doubling squares
  each trace and multiplies it by its sector purity. Monotonicity of $(x-y)/(x+y)$ in $x/y$ gives the
  stated conditional implication if $p_e\ge p_o$. No such order follows from positivity of the two
  traces. For the spatial comparison, the flipped Wilson convolution has eigenvalues $(-1)^{2j}c_j$, of
  both signs (gap-brainstorm-max.md 652–657). The ordinary positive crossing-kernel proof thus loses its
  hypothesis. Equivariance of a selected position gives a uniform location conditional on its existence,
  with no comparison of its total weight across sizes.
- **Comparison models, J97–106 — HOLDS AFTER CORRECTION.** The four-dimensional continuum Maxwell action
  of a fixed harmonic flux is independent of size. For *compact Wilson* $U(1)$ the twist shifts the flux
  by half a flux quantum. At fixed side, M(b) in the two active planes and its one-plane version give
  $-\lim_{\beta\to\infty}\beta^{-1}\log R(L)=L^4(1-\cos(\pi/L^2))$. This follows by bounding the compact
  integral above by its maximum and below on any neighborhood of a minimizer. The displayed value
  increases strictly with $L$ by monotonicity of $\sin x/x$. Thus literal size independence at weak
  coupling, line 99, **FAILS**. An exactly constant small ratio would also meet the non-strict inequality
  with $\kappa=1$. The proposed (X) asks for $\kappa>1$ and a size-independent unsaturated gain. For the
  finite groups at line 100, the support argument in M(c) covers $L^4$ basepoints with at most $L^2$ per
  defective plaquette. Each defect costs at least the positive finite-group minimum. M(a) supplies the
  matching order $L^2$. For the five-dimensional classical comparison at line 101 the four-dimensional
  abelian field repeated in the fifth direction costs order $L$. For a lower bound on a four-slice,
  compactness and M(c)’s incompatible holonomies give some commutator at distance $\ge\eta>0$ from its
  prescribed sign at each basepoint. Sweeping its torus bounds this distance above by the sum of its
  plaquette defect angles. Cauchy–Schwarz, $1-\cos s\ge2s^2/\pi^2$, and summing over basepoints give a
  positive constant per slice. These are classical estimates. No control of fluctuation entropy uniform
  in size follows. The spectator argument at line 102 holds exactly as below.
- **Classification of index weights, J126–144, 238–239 — FAILS as an exhaustive lattice statement at 131, 138–142.**
  The self-dual deformation index counts $\dim H^1-\dim H^0-\dim H^2$. The kernel has dimension
  $\dim H^1$. A reducible abelian background on the four-torus has a parallel color in $H^0$, also giving
  obstruction forms by
  multiplication by harmonic two-forms of the appropriate chirality. Four abelian periods alone do not
  evaluate its fluctuation measure. Clover charge is center-invariant because a closed center flip
  cancels plaquette by plaquette, but clover charge is not generally integer. An admissibility condition
  or a specified charge construction is needed for exact sectors. With integer sectors and the recalled
  regular-saddle hypotheses the $\lvert Q\rvert=2$ one-loop power is $44/3$. Normalize the theta function
  as $\sum_Q e^{i\theta Q}Z_Q/\sum_Q Z_Q$. The denominator in line 142 drops the other charges. These examples
  supply no exhaustion of neutral observables or of their possible scale dependence.
- **Topological or twist weights alone versus (N-phys), J146–150, 240, 254 — HOLDS.** A decoupled,
  topologically trivial photon multiplies each sector partition function by the same factor. In a
  periodic cube its neutral one-photon energy in lattice units obeys
  $\omega=2\operatorname{arsinh}(\sin(\pi/n))\le2\pi/n$. Its contribution at $u\le n/K$ is at least
  $e^{-2\pi/K}>1/2$ for $K=512$. This already defeats the required trace bound. Row 929, gap-seam-max.md
  118–129, gives the stronger fixed-aspect lower bound in **A2**. That lower bound alone does not prove
  divergence at fixed aspect. The product tests an inference from one marginal law, without asserting a
  photon factor in pure $SU(2)$.
- **Every other neutral quantity changes only by relative $O(g^2)$, J154–159, 221–226, 241, 261 — FAILS at 154.**
  Even within the proposed one-loop reasoning, take a dimensionless neutral running coupling and form
  $f(L)=\exp[-c/g_R^2(L)]$, $c>0$. If $g_R^{-2}(2L)=g_R^{-2}(L)-2b_0\log2+O(g_R^2)$, then
  $f(2L)/f(L)\to2^{2b_0c}$. This has neither an integer-charge projection nor a zero-mode count. For a
  regular power of $g_R$ the relative $O(g_R^2)$ statement does hold after removing engineering
  dimensions. The reparametrization supplies no neutral trace estimate. Neither an exhaustive pair of
  possible proofs nor a compulsory precision for all of them follows.
- **Minimum, localization and dislocation threshold, J181–185, 245, 253, 259–260 — HOLDS for 183–184, FAILS at 185 and 259–260 for dominance.**
  The small-box competitor beats the abelian family. No global nonabelian minimum at larger $L$ is
  determined. Defects cannot be exactly localized in the sense of M(c). If one *assumes* a family with
  net weight $(L/a)^4e^{-\beta A}$ and the stated scaling relation, its exponent changes sign at
  $12\pi^2/11$. A field at action $A$ has no assigned integrated weight or positional multiplicity. There
  are explicit fields separated from the smooth family at a mixed plaquette. Multiply a single link of V
  by $\exp(i\sigma_1/4)$. Each of its six plaquettes loses at most $1-\cos(1/4)$ in signed trace, since
  the unperturbed factors are in the $\sigma_3$ torus. A mixed plaquette now has half-trace $\cos(1/4)$
  instead of one. The total action is at most $\pi^2+3/16<12\pi^2/11$ for all $L\ge3$. Thus an exclusion
  of *every* such configuration cannot be the required integrated estimate. Nor does M(a) prove that its
  particular field dominates the small-box integral.
- **“About seven”, J199–215, 219–226, 246, 255 — HOLDS AFTER CORRECTION as a conditional endpoint estimate.**
  If a positive splitting is multiplied by $B$ between fixed couplings, its logarithmic mean $\kappa$ is
  exactly $\log B/\log(\beta_{\rm entry}/\beta_{\rm exit})$. The quoted 7.3 uses the chosen $B\simeq56$,
  size ratio 100, example bare couplings and one-loop scale matching. None is forced by the definition of
  (N-phys). Its necessity $n m_{\rm ev}\ge K\log2$ follows from one term of the excited trace. Its
  sufficiency also requires state counting, as in gap-mini-neutral2-fable.md 157–164. The guide’s
  positive free-level limit allows oscillating derivatives, as $D(\beta)=1+\beta^{-1}\sin\beta$
  illustrates. A fixed positive *lower bound* on $\kappa$ all the way to $\beta=\infty$ would force
  $D\to0$ by integration, so a positive limiting splitting does rule that bound out. A
  coupling-independent oscillator has $\kappa=0$, an exactly linear energy has $\kappa=-1$, and a
  differentiable positive splitting has $\kappa=0$ at an interior minimum. These limited tests leave open
  the Wilson band estimate, the multiplicities and the match of Hamiltonians.

### L · what the plate can detect

- **The rate is the neutral gap, L140, 148, 155, 205 — FAILS.** There is a counterexample inside the
  stated Wilson geometry. Take $R_1=3$, $R_2=R_3=5$ and small positive $\beta$. Normalize the one-link
  convolution by its constant eigenvalue and put $u=I_2(\beta)/I_1(\beta)\sim\beta/4$. A link carrying
  spin $j$ costs order $\beta^{2j}$ by GL3. On this fixed finite graph the sum beyond total degree $d$ is
  $O(\beta^{d+1})$ in trace norm, by summing the multiplicities $(2j+1)^2$ against the factorial Bessel
  series on each link. A nonconstant gauge-invariant labeling has no vertex with just one occupied edge.
  Through degree three the only possibilities are the straight direction-1 triangles with spin $1/2$ on
  each edge. Their normalized loop characters $W_x$, indexed by transverse site, are orthonormal and
  $C_1$-odd. On the $C_1$-even subspace, $T_v$ is consequently rank one plus $O(\beta^4)$, since the
  bounded spatial multipliers preserve parity. Its first excited eigenvalue is $O(\beta^4)$, also after
  projection to all three even fluxes. On the odd subspace $T_v=u^3P_\triangle+O(\beta^4)$, where
  $P_\triangle$ projects onto the $W_x$. The same expansion of the endpoint kernel gives
  $v_{1/2}=u^3\sum_x W_x+O(\beta^4)$ in the common normalization, because $W_x(\omega^h)=\chi_{1/2}(h)$
  and the spatial multiplier is $1+O(\beta)$. Uniformity of the endpoint remainder follows because the
  finite product of Wilson weights has a uniform Taylor remainder on the compact field space, also after
  gauge averaging. The Rayleigh quotient on $v_{1/2}$ is thus asymptotic to $u^3$. For $t\ge1$,
  positivity and scalar Jensen give
  $\langle v,T_v^t v\rangle\ge\|v\|^2(\langle v,T_v v\rangle/\|v\|^2)^t$. The half-integer diagonal entry
  has zero vacuum term and decays more slowly than the even excited rate. Division by the common
  $\lambda_0^t$ preserves the comparison. The conclusion at L120 for unrestricted pins survives.
- **Strong-coupling tube and the thickness bound, L128, 195 — HOLDS AFTER CORRECTION.** For each *fixed*
  cross-section and all sufficiently small positive $\beta$, $P_\infty(0)<1$. Here is a remainder
  argument for that range. At fixed $T\ge4$ use the crossed, interior-gauge-projected convolution of
  Lemma 2. Grade its link representations by $D=\sum_e2j_e$. Among labelings of top spin different from
  zero, the minimum grade is three. An occupied edge arriving from a top endpoint needs an invariant
  continuation at its free endpoint. With at most three strands the only possibility is to go down, cross
  one transverse bond, and go up to a different top site. A path to the bottom requires at least four
  edges. A single higher-spin bond cannot terminate at an interior site. Each of the $2A$ unoriented
  transverse bonds therefore contributes one endpoint representation $\tfrac12\otimes\tfrac12=0\oplus1$,
  with convolution eigenvalue $u^3$. The other top-nontrivial terms have trace norm $O(\beta^4)$ by the
  same factorial bound. Multiplication by $e^{-V/2}=1+O(\beta)$ preserves top spin. On raising to the
  fixed power $R_1$, the trace error is $O(\beta^{3R_1+1})$ by telescoping the product. The normalized
  untwisted partition function is $1+O(\beta)$. It follows that

  $$
  -\log R_T(h)=2A\,u^{3R_1}\bigl(3-\chi_1(h)\bigr)+O_{R_i,T}(\beta^{3R_1+1}).
  $$

  The vertical kernel at $\beta=0$ is the constant rank-one kernel. Its finite-graph perturbation has
  operator norm $O(\beta)$, so $q=O(\beta)$. The isolated vacuum projection converges to the constant
  projection. The vectors $u_\omega$ tend uniformly to one, so the vacuum denominator stays bounded
  below. Proposition 5 gives $|R_T-R_\infty|=O(q^{T-2})$ with a bounded prefactor in
  the $T-2$ form. Choose one fixed $T>3R_1+2$ before sending $\beta$ to zero. This transfers the leading
  term to $R_\infty$. Since $3-\chi_1(h)=4-(\operatorname{tr}h)^2>0$ for a noncentral $h$, a lower bound
  tending to one as $T\to\infty$ fails already at these couplings. For finite $T$ the expansion requires
  an **additive** remainder at $h=-1$. Lemma 2 gives $R_T(-1)<1$ while the proposed leading coefficient
  vanishes. The all-positive-coupling assertion and the weak-coupling vacuum potential do not follow from
  this expansion.
- **Ward identity, thickness and conditioning, L150–155, 200, 204 — HOLDS AFTER CORRECTION.** A gradient
  change of the pinned field is a site change of variables, also with the exterior below the plate fixed.
  For cubic plates the infrared sum $|\Lambda|^{-1}\sum_{k\ne0}|k|^{-2}$ is bounded by shell counting.
  This is not uniform on the rectangular boxes of L57. At sides $(N,3,3)$ the first longitudinal mode
  alone contributes at least $N/(36\pi^2)$ with lattice momentum. The claim at 153 that the missing
  $SU(2)$ thickness gain is in $\operatorname{Var}(\mathbb E[J\mid A])$ **FAILS** because that variance
  is identically zero by Lemma 3’s conditional symmetry. The Gaussian abelian example has no such color
  cancellation. A generic interior pin has only the central stabilizer and leaves L’s two-flat-plate
  class. S’s P3 gives the different, closed family of twist-carrying bottom children. Gauge changes leave
  every bulk trace fixed, but this fact does not classify all Ward identities or all possible sources of
  variance.
- **Fourth-order response and color charge, L148, 155, 204–207 — HOLDS AFTER CORRECTION.** The mixed
  second derivative vanishes. The lowest *allowed* mixed derivative has bidegree $(2,2)$ and equals
  $\operatorname{Cov}(j(j+1),k(k+1))/9$ in the joint flux law. Its overlap with a slow eigenfunction can
  vanish. The generator identity allows field color charge above a layer. It supplies neither a screening
  rate nor a lower bound on the overlap of the toron family with the lightest neutral state.
- **Plate-anchored frame, L171–178 — HOLDS AFTER CORRECTION as a conditional bound.** The translations
  depend only on vertical links, so conditioning on those links proves unit Jacobian. In the frame
  parallel-transported from the top, a transverse link at depth $d$ is a product around a strip of $d$
  vertical plaquettes, up to parallel transports. For unit quaternions $|1-U|^2=2(1-t(U))$. The triangle
  and Cauchy–Schwarz inequalities bound the mean squared strip distance by $C d^2/\beta$, given L177’s
  local energy hypothesis. Every horizontal plaquette is a product of four such links, hence
  $\mathbb E|1-U_p|^2\le C' d^2/\beta$ as well. This second bound controls the cross term omitted at 176.
  Indeed average $a$ and $-a$ by top rotation. For $n=\operatorname{Ad}_H e$, $e$ the twist axis and $H$
  the transverse strip, the even part of the inserted commutator differs from one by a scalar of size
  $\sin^2(a)(1-e\cdot n)$ and a vector of size $\sin^2(a)|e\times n|$. The scalar costs
  $O(a^2\mathbb E|1-H|^2)$. The vector is paired with $s(U_p)$ and costs the same order by Cauchy–Schwarz
  and the two strip bounds. Temporal plaquettes depend only on the successive angle difference. Summing
  gives $C(A/R_1)\phi^2(\beta/\tau+\tau^3)$ and choosing an integer $\tau$ of order $\beta^{1/4}$ gives
  the claimed power when the slab fits. The local energy estimate, including its uniformity in depth and
  in the box, is a premise. The asserted reduction of that local premise to a single value of the vacuum
  functional is unproved at 177.

### N · what the positivity tests exclude

- **Natural order, N32–38, 54, 91–94 — HOLDS AFTER CORRECTION.** The particular increasing pair rules out
  association in that order on the stated tori and coupling range, including any all-coupling proof that
  requires it there. It does not rule out every Holley comparison or every monotone coupling. Even a
  nonassociated law has the diagonal monotone coupling with itself. Nor does the example test association
  restricted to other observables or only at large $\beta$. The need for a neutral estimate follows from
  the target. Uniqueness of positivity as a possible mechanism is a reading of the surveyed routes,
  without a mathematical exclusivity argument.
- **Signs of the Wilson adjoint marginal, N80, 84, 95 — HOLDS AFTER CORRECTION.** The projective plane
  gives a negative term of the ungrouped half-integer character expansion. The sign of a pseudoreal
  representation on a closed surface with $k$ crosscaps is $(-1)^k$. A Klein bottle has positive sign.
  The single negative term does not exclude positive regroupings. In fact, given representatives
  $\widetilde U_e$ of the $SO(3)$ links, their exact marginal density relative to projected Haar is
  proportional to

  $$
  2^{-|E|}\sum_{z_e=\pm1}\exp\!\left(\sum_p\beta_p\,x_p(\widetilde U)\prod_{e\in\partial p}z_e\right).
  $$

  Every summand is positive and a change of lift permutes them. This is not an association inequality.
  The parity criterion on local contractions applies to PAR’s two- and three-valent links. Higher link
  multiplicities require their own projectors. For the adjoint field on the projective plane itself, the
  surface rule gives $3^{1-92}=3^{-91}>0$. The sign of general adjoint Haar moments remains open.
- **Hopf frustration and the absence of a deduction of decay, N82–97, 109–113 — HOLDS for the specified route.**
  In gap-mini-solve-a-fable.md 85–108, the Fourier forms satisfy $m_{12}=m_0+m_{13}-m_{23}$. Positive
  amplitudes force zero phase on the three terms on the right, whereas the negative coefficient on the
  left would require phase $\pi$. This refutes the proposed shift to nonnegative couplings in those Hopf
  variables. It does not test arbitrary decompositions. Positive adjoint moments at Haar yield neither
  charged decay nor bounds on the Wilson law. Even a covariance inequality for adjoint variables gives
  monotonicity directly only for *adjoint* source couplings. Differentiation in a fundamental Wilson
  coupling inserts $x_p$.
- **Generating the neutral local algebra, N89, 97, 113 — FAILS on the linkwise center-blind reading used at N58.**
  Giving every link its $SO(3)$ projection loses the sign on each individual lift. For instance, all
  links equal to one and a configuration with one link equal to $-1$ have identical adjoint data, but a
  contractible fundamental plaquette through that link has opposite half-trace. This observable *is*
  invariant under the global electric center on a closed seam. Conditional on projected links, all lift
  signs have positive probability at finite $\beta$, so the loss also holds modulo null sets on an open
  set of projections. If “center-blind” means only invariance under the global electric center,
  generation is a different, open proposal. The hand calculation does not close it.

### S · the scope of the plate obstruction

- **The three proposed properties, S109–119, 151–154, 262–264 — HOLDS AFTER CORRECTION.** The bottom
  spins carry a rigid common left action, and the twist-carrying children stay in the class. A
  *relative*, nonconstant junction profile can change a gauge-invariant pinned Wilson loop. For trivial
  pins a side plaquette at the foot of the wall acquires half-trace $\cos(\epsilon\Delta u)$. Giving this
  face alone positive strength exhibits a nonzero response. The uniform group action on *all* junction
  pins is removable by exactly P1’s change of integrated variables. Thus the literal nonremovability of
  that group action in row 1016, gap-global-reform-max.md 649–655, **fails**. The candidate meets a
  relative-pins interpretation of (R-b,c). A constant profile cannot witness it. Localized spins about
  two different axes have their quaternion commutator. Row 1011’s Ward identity 184–198 also requires its
  integrated variation to vanish on fixed pins. These facts provide a bracket identity but no
  fourth-order gain.
- **Scale and logarithm, S121–139, 194–206 — HOLDS AFTER CORRECTION.** For the stated affine profile, the
  minimizing plate Dirichlet energy is of order $\theta^2R$ in four dimensions. Each of order $R^2$
  parallel length-$R$ lines spans $\theta$, and the linear extension realizes that order. This estimate
  need not hold for arbitrary boundary data of the same oscillation. The Gaussian response satisfies the
  sharper two-sided order $b\theta^2(1+\log R)$ for this profile. To verify the lower bound, use P5(a)’s
  transformed pins and write $h(y)=\sum_{x_1=0}^{R-1} A_1(x_1,y)$, $y=(t,x_2,x_3)$. The $m$-links on the
  two end faces $x_1=0,R$ have zero shifted values for $m=0,2,3$. Telescoping shows
  $\Delta_m h=\pm\sum_{x_1}(dA)_{1m}$. Since weights are at least $1/4$, the energy is at least
  $(4R)^{-1}\sum_{y,m}|\Delta_m h|^2$. The bottom trace of $h$ is $\theta$ and the side $x_2=0$ has trace
  zero for $t>0$. At fixed $x_3$, join $(t,x_2)=(0,k)$ to $(k,k)$ to $(k,0)$, for $1\le k\le R/2$. The
  paths are edge-disjoint, and each costs at least $\theta^2/(2k)$ by Cauchy–Schwarz. Sum over $k$ and
  $x_3$ to obtain the logarithm. This makes the small ratio to $bD_3$ a genuine abelian comparison. In
  the nonabelian cell the direct term contains the actual ring trace and the variance has a negative
  sign. P5 gives no comparable $SU(2)$ lower bound.
- **Uniform factor $L$ in every dimension, S133–139, 214–219, 231–233 — FAILS as stated at 215–216.** A
  uniform field through the height misses the tangential boundary layer. Take the allowed
  four-dimensional tiling $R=L$, so the children have side one. On a child a constant offset in $u$ costs
  zero. The affine variation is $\theta/L$. The finite number of fixed faces therefore costs at most
  $C b(\theta/L)^2$ per child. The sum over $L^3$ bottom children is at most $Cb\theta^2L$, and P5(b)
  gives the matching lower order. The parent costs order $b\theta^2(1+\log L)$ by the preceding
  paragraph. Their ratio has order $L/(1+\log L)$, strictly smaller in order than $L$. More generally, in
  each fixed dimension $d\ge3$ the same disjoint paths have order $R^{d-3}$ choices of spectator
  coordinates. P5’s upper trial uses one angular factor for each of the $d-2$ lateral directions. The two
  bounds give order $b\theta^2R^{d-4}(1+\log R)$. A child profile differs from a rescaled copy only by a
  removable constant. The corresponding ratio has order $L(1+\log R')/(1+\log R)$, $R'=R/L$. In $d=2$
  there is no lateral corner. The telescoping bound along height is attained by a linear $h(t)$ and the
  ratio is $L$. Nonadditivity really can grow without bound, with a dependence on shape and mesh that the
  uniform-field argument suppresses.
- **No variance method or four-dimensional port, S137–154, 195–202, 223–229, 240–255, 268–275 — FAILS as a universal exclusion.**
  P5 proves the excess in this Gaussian example for this choice of ring translation. A lower bound on the
  cancellation required by an identity places no upper bound on the accuracy of another variance
  estimate. Indeed the Gaussian current is linear after quotienting and completing the square computes
  its covariance exactly. A pure site gauge on *all* links preserves every plaquette. Proposition B of
  row 1011 concerns specified rough-pin deformations and a supremum of their costs. CEN+ of row 1016,
  lines 446–456, classifies field-independent single-link maps preserving each plaquette trace for every
  configuration. It allows gauge and closed center fields. It does not classify collective, conditional
  or field-dependent transformations, and does not require every variable of every possible construction
  to transform nontrivially. The stated engineering dimension $d-2(q+1)$ for a bulk curvature-squared
  energy with fixed integrated $q$-form twist is consistent by rescaling. It does not establish the
  proposed dichotomy at a boundary.
- **Annular and three-dimensional comparisons, S256–261 — HOLDS AFTER CORRECTION.** Lemma PC in
  gap-mini-solve-a-fable.md 178–208 concerns a *periodic* slice and a profile cohomologous to a nonzero
  constant one-form. Its key pairing kills gradients by periodicity. An annular relative-pin twist can
  itself be a gradient with different boundary values. It has no such periodic pairing. Thus “bound
  instead by Lemma PC” **fails at 257** without a new reduction. The direct three-dimensional shell count
  is only evidence about that method. In three space-time dimensions a flat plate gives a two-dimensional
  layer with nearest-neighbor right backgrounds after conditioning. Its charged estimates can be used
  only with the matching boundary/test hypotheses of the cited two-dimensional result (row 1009, pinned
  influence versus unpinned charged correlations). No neutral decay estimate for the four-dimensional
  Wilson theory follows.

RESULT: Row 1247 checked all four notes by hand at d9d52d534. J’s M and V hold. L’s full-box transfer rate can be charged, and its toron law is nontrivial at sufficiently small positive coupling on each fixed box. N’s FKG counterexample holds given NS0, and all three adjoint Haar moments agree. S’s Gaussian bounds hold with the gauge and counting corrections, and the tiling by cells of side one gives a ratio of summed cell energies to parent energy of order $L/(1+\log L)$, refuting the claimed uniform factor $L$. The proposed general route exclusions do not follow. (N-phys), (X), (BS), (W), the continuum datum and the four-dimensional SU(2) mass gap remain open.
