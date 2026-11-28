## Repo search

**GUIDE.** Plan for FINISH row 1169. Check the lead’s repository search and the indexed source ranges against the exact wall (W). Starting from the latest reduction, seek a selective inequality, a counterexample, or a proved obstruction to each attempted route. Record the evidence and limits of each step here.

**GUIDE.** Codex, row 1169, checkout `86c6dde27`. The target-specific prior file is absent. The November 8 digest concerns thirteen mostly ultraviolet questions. Its gap supplement identifies the nearest transfer results. I checked the one-step plaquette witness and the bare-coupling range through \(1/32\) on PR 10114 (`MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14, 106–123, 141–149). PR 10133 leaves the physical crossover open (`APPROACH_REGISTRY.md`, lines 226–228). PR 10134 contains an earlier existence interface (`GOAL.md`, lines 48–56). The estimate on PR 10141 controls a constrained field at one scale (`research/ym4d/library/fp1.md`, lines 302–314). The finite-clock Villain note on main at `8b11ae2bb9`, lines 4–12, concerns an abelian measure. The registry and open-core searches yielded no competing owner of this continuation. [Lead search](prior/repo-search-2026-11-08.md) · [Gap supplement](prior/gap-crux-prior-ym.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, derive the positive gauge-projected transfer and the torus trace at outline lines 2313–2336. At lines 31871–31882 they exhibit a clustering spectral measure reaching zero. CA-I lines 2704–2712 explicitly list “a mass gap” among the conclusions left open. The 4.12–4.19 index concerns the ultraviolet induction. Tadeusz Bałaban supplies the upstream renormalization method. Sourav Chatterjee supplies the weak-coupling free-energy method used in the preceding rows. All proofs below are research arguments at this pin. [Outline, GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2313-L2336) · [Spectral example](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31871-L31882) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**OPEN.** Fix the row-720 trajectory, with \(n=L/a_j\) on its physical grid. Let \(F\) be the ordinary periodic Wilson transfer on the full gauge-invariant spatial cube, \(U=F/\|F\|\), and \(X(v)=\operatorname{Tr}U^v\). The strict seed is \(\limsup_j[X(n/2)-1]<1/1650\) at one fixed permitted \(L\). The repaired (W) requires \(D^+(L')\le D_0\) on the dyadic grid from \(L_0\) on and \(z^-(L)>256D_0+30\) at some \(L\ge4L_0\). Here \(D^+\) is the cutoff upper limit of the symmetric torus log partition function minus its bulk log pressure times the volume. The number \(z^-\) is the lower limit of \(n\log(\lambda_0/\lambda_1)\) for the cube. Row 720 supplies the equivalence. Row 1167, whose independent check is pending at the pin, gives a two-collar criterion using neutral decorrelation and a charged sign. Its local sign estimate leaves the common sign of the parallel lines undetermined. Construction and identification of a continuum theory are additional inputs to the Jaffe–Witten target. [Wall and quantifiers](../parts/gap.md) · [Theorem ZD-c](gap-phys-seed.md) · [Row 1167, (9)–(10)](gap-solve12-astra62.md)

**GUIDE.** Equations (12) and (26) give the sharp rates for true Wilson paths that share the adjoint history. Equation (29) compares unanimous reversals under the two observations. Equations (5) and (23) bound reversals when only the two endpoint collars are shared. Equations (15) and (21) concern the neutral sector. Mack and Petkova supply the center-lift decomposition used to compare fundamental links with the same adjoint. For a physical interpretation I use \(\beta/\log n\to11/(3\pi^2)\) only under the account's flow premises. Its RF10 fixes the coefficient, RF20 controls the increments, and RF25 and RF28 give the terminal window and accumulated error. CA-I 54985–55001 states the separate stage and profile hypotheses for the preparatory boundary theorem. No numerical input enters the arguments. [Flow derivation in row 1155](gap-solve7-astra62.md) · [Outline, RF10](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L20348-L20363) · [Outline, RF28](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L20865-L20878)

## An axis transported by tangential Wilson links

**GUIDE.** Try to change the majority itself by a change of variables that preserves the observed adjoint collars. Rotate the links crossing a spatial cut. The axes will depend on tangential links, all of which the change fixes. C8 of the selective-inequality exercise already uses tree transport. B2 of the wall exercise proposes spreading a rotation. The estimate below uses many transported axes on the ordinary Wilson torus and bounds the cost after averaging its genuine spatial action. [C8 and C9](gap-invent-selective-max.md) · [B2](gap-wall-max.md) · [Earlier entropy obstruction for exogenous rotations, (25)](gap-solve9-astra62.md)

**PROVED.** Use unit quaternions and the Euclidean norm. In the ordinary rectangular Wilson law at \(\beta\ge1\), a width-one rectangle of length \(h\) shorter than its period satisfies
\[
 {\mathbb E}|1-U_{1\times h}|^2\le C h/\beta .                         \tag{1}
\]
Here and below \(C\) denotes a finite absolute constant allowed to increase. This is the checked input of row 1153, before its equation (2). In its transfer proof the rectangle expectation is the \(h\)-th moment of a nonnegative eigenvalue ratio under a probability law. Its first moment is the elementary plaquette expectation. Jensen bounds the rectangle expectation below by the \(h\)-th power of that first moment. The single-plaquette bound \({\mathbb E}(1-w_p)\le C/\beta\) then gives (1), since \(|1-U|^2=2(1-w_U)\). For the bounded range of \(\beta\) where the resulting estimate exceeds four, the chord bound suffices. We use only the ordinary untwisted measure here. [Strip proof and reference to Bachas](gap-solve6-astra62.md)

**PROVED.** Fix the hyperplane \(x_1=0\), with three tangential coordinates \(2,3,4\). For any integer \(b\ge2\) less than one eighth of each tangential period, there are random unit imaginary quaternions \(v_x\) on this plane with
\[
 {\mathbb E}|v_x-\operatorname{Ad}_{U_{xy}}v_y|^2
      \le C(b^{-2}+b/\beta)                                             \tag{2}
\]
on every tangential nearest-neighbour bond \(xy\). Each \(v_x\) uses only tangential links at distance at most \(3b\) and independent auxiliary variables. Its law is gauge covariant. No curvature or mixing assumption at a physical scale enters (2).

**PROVED.** For each \(z\) take an independent standard Gaussian \(\eta_z\) in its three-dimensional adjoint space. Let \(P_{xz}\) transport from \(z\) to \(x\) along a fixed coordinate-ordered shortest path in the local box. Use the adjoint action for this transport. Let \(w_x(z)\) be the translate of \(\prod_{i=2}^4(1-|z_i|/b)_+\), divided by its discrete \(\ell^2\) norm. The sum of its squares is one. On neighbouring translates the sum of squared differences is \(O(b^{-2})\). Indeed the unnormalized norm squared lies between \(c b^3\) and \(C b^3\), and each of at most \(C b^3\) differences is at most \(1/b\). Form \(G_x=\sum_z w_x(z)P_{xz}\eta_z\), and put \(v_x=G_x/|G_x|\) almost surely. Conditional on all the links, each \(G_x\) has covariance \(I_3\).

**PROVED.** On overlapping supports the two paths from \(z\) to neighbouring \(x,y\), closed by \(xy\), differ by at most two width-one strips. Commute the last unit edge past the later coordinate runs until it reaches its own coordinate run, then combine or cancel it there. Conjugations leave chord lengths invariant. In the adjoint representation \(\|\operatorname{Ad}_g-I\|_{\rm F}\le C|1-g|\), since \(g q g^{-1}-q=(g-1)qg^{-1}+q(g^{-1}-1)\) on each unit basis vector. Hence (1) bounds the expected squared matrix difference between the two transports by \(C b/\beta\). Independence of the \(\eta_z\)'s gives the sum of squared coefficients for the mean squared Gaussian difference. Split that sum into the change in \(w\) and the change in transport on the overlapping supports, charging the nonoverlap to the change in \(w\). The result is \(C(b^{-2}+b/\beta)\).

**PROVED.** Normalization costs only a constant. Conditional on the links, write \(G_x-\operatorname{Ad}_{U_{xy}}G_y=M G_x+E\), with \(E\) a centered Gaussian independent of \(G_x\). Take \(M\) to be the cross covariance with \(G_x\). The remaining cross covariance vanishes, which gives independence by the Gaussian characteristic function. The inequality \(|u/|u|-v/|v||\le2|u-v|/|u|\) applies almost surely. Rotational symmetry gives \({\mathbb E}|M G_x|^2/|G_x|^2=\|M\|_{\rm F}^2/3\). The radial Gaussian integral gives \({\mathbb E}|G_x|^{-2}=1\) in dimension three, by integration by parts. Thus the mean squared normalized difference is at most four times the unnormalized one. This proves (2). Gaussian integration here defines an exact trial measure.

## Reversing the common sign while fixing both observations

**PROVED.** Let \(m=n^2\) be the number of transverse spatial lines. Let the two adjoint observations \(A=(A_1,A_2)\) be disjoint time collars of the kind in row 1167, with room for a transition on each intervening arc. Draw \(U,\widetilde U\) independently from the ordinary Wilson law conditional on \(A\). At transverse vertex \(y\), form \(\theta_y\) from the four winding trace signs, as in row 1167 (17). Let \(B\) be their majority and resolve an exact tie by \(\theta_{y_0}\) for a specified \(y_0\). This rule is odd under simultaneous reversal of all \(\theta_y\). Write \(p=\Pr(B=-1)\). The following argument bounds the probability for this common bit directly, including when an additive bound on one-line decoding errors would exceed the probability under study.

**PROVED.** In the plane of (2) multiply each forward 1-link on the left by
\[
 H_x=\cos\alpha_t+v_x\sin\alpha_t .
\]
Keep every other link. Take \(\alpha=0\) on the first collar, \(\pi\) on the second, linear from \(0\) to \(\pi\) in \(w\) time steps on one arc and back in \(w\) steps on the other. Outside the ramps use the constant endpoint values. Conditional on tangential links and auxiliary randomness this map is a product of Haar translations. Its inverse uses \(-\alpha\). At the second collar it makes exactly one flat plane flip. Thus it fixes \(A\) and reverses the first path's winding sign on every line there.

**PROVED.** Denote the Wilson probability by \(\mu\). For any of these Haar-preserving maps \(\Phi\) with fixed auxiliary variables,
\[
 D(\Phi_*\mu\|\mu)=\beta\,{\mathbb E}_\mu[S(\Phi U)-S(U)],\qquad
                   S(U)=\sum_p(1-w_p).
\]
For an affected plaquette its transformed quaternion is, up to conjugation or inversion, \(G U_p\), where \(G\) is the product of the rotation at one end and the inverse rotation at the other, transported by the unchanged tangential link. Common axes would give angle \(\alpha_x-\alpha_y\). The triangle inequality on unit quaternions bounds \(|1-G|\) by \(|\alpha_x-\alpha_y|+|v_x-\operatorname{Ad}_{U_{xy}}v_y|\). On constant central parts the actual change is zero. Since \(1-\operatorname{Re}q=|1-q|^2/2\), the positive increase on a ramp face is at most \(C(|1-G|^2+|1-U_p|^2)\). Equations (1)–(2) and the \(O(mw)\) ramp faces give
\[
 {\mathbb E}_{\eta}D(\Phi_*\mu\|\mu)
 \le C m\{\beta/w+\beta w(b^{-2}+b/\beta)+w\}.                         \tag{3}
\]
With \(b,w\) of order \(\beta^{1/3}\), this is \(C m\beta^{2/3}\) for sufficiently large \(\beta\) and periods. Here the axes may be correlated with the plaquette they rotate. The estimate uses squared chords and requires no independence of those quantities.

**PROVED.** Apply the map to the first completion only. It fixes \(A\) pointwise. The joint relative entropy with respect to the original two-completion law equals the one-path relative entropy for a fixed map because, given the new first path, the conditional law of the second path is still \(\mu(\cdot\mid A)\). Recording just \(B\) gives
\[
 d(1-p\|p)=(1-2p)\log[(1-p)/p]\ \le\ {\mathbb E}_{\eta}D(\Phi_*\mu\|\mu), \tag{4}
\]
where \(d\) denotes binary relative entropy. The inequality follows by splitting the entropy integral over the two events and applying Jensen on each. For \(q=\min(p,1-p)\le1/4\), \(d(1-q\|q)\ge\tfrac12\log(1/(2q))\). Thus both majorities have probability at least \(\tfrac14\exp(-2C m\beta^{2/3})\). This estimate concerns a change of the majority in the genuine Wilson ensemble. The power of the area still permits a vanishing probability on the physical grid. A deformation using both normal directions is considered next.

## Spreading the change in both normal directions

**PROVED.** Suppose the periods and both gaps between the collars are larger than \(C\beta^{1/3}\) for a sufficiently large absolute \(C\). For the ordinary Wilson majority in (4) one has
\[
 d(1-p\|p)\le C m\beta^{1/3}\log(2+\beta).
                                                                    \tag{5}
\]
On a rectangle with the same room in directions \(1,4\), a single elementary twist in the \(14\) faces obeys
\[
             -\log(Z_{\rm tw}/Z_0)\le C m\beta^{1/3}\log(2+\beta).
                                                                    \tag{6}
\]
Here \(m\) is the area in directions \(2,3\). The proof uses the actual Wilson spatial plaquettes in bounding the cost of a field-dependent transformation.

**PROVED (profile).** In the normal \(14\) plane select a dual vertex \(o\), hence a primal face. For an integer \(R\ge2\) construct a real one-cochain \(a\) on the primal edges with
\[
 da=\pi(\mathbf1_o-\rho),\quad
 \sum\rho=1,\quad 0\le\rho\le R^{-2},\quad
 \sum_e a_e^2\le C\log(2R),\quad
 \sum_e(1+\operatorname{dist}(e,o))a_e^2\le C R .                    \tag{7}
\]
It has support in a box of side \(2R+4\). Start a dual path at \(o\). At \((i,k-i)\) in the positive quadrant take the step increasing \(i\) with probability \((i+1)/(k+2)\), otherwise increase the other coordinate. Induction gives the uniform law on the \(k+1\) positions of shell \(k\). An interior position \(i\) on the next shell receives probabilities proportional to \(i\) and \(k+1-i\), with the same conclusion at the ends. Stop at an independent uniform shell from \(R\) through \(2R-1\). Its site law is \(\rho\). The mean edge flow has divergence \(\mathbf1_o-\rho\), by cancellation of entrances and exits. Rotate it by a quarter turn with the sign giving primal curl equal to that divergence, and multiply by \(\pi\). On shell \(k\) each of at most \(2(k+1)\) edge values has magnitude at most \(\pi/(k+1)\). Summing these bounds proves (7). This flow is a finite analytic construction.

**PROVED (which links move).** For (5), first take a central multiplier \(\sigma_e=-1\) on the 1-links of the cut during the time interval containing the second collar, and \(+1\) elsewhere. Its plaquette product is \(-1\) exactly at two normal faces, on every transverse translate. Place one profile (7) at each of these faces with its entire box outside the collars and the boxes separated by at least two layers. For (6) take \(\sigma=1\) and one profile at the prescribed twist. Extend the profiles constantly in coordinates \(2,3\) and set \(a_e=0\) in those directions. Write \(\tau_p=1\) in (5), and use the prescribed central twist in (6). In either case \(\tau_p\sigma_{\partial p}\exp(i\,da_p)\) has angle modulo \(2\pi\) of magnitude at most \(\pi\rho_p\) at each \(14\) face, with the corresponding profile. Its angle is zero at every other orientation. Either sign for all \(a_e\) has this property.

**PROVED (the axes and the Jacobian).** In each profile take one reference normal vertex adjacent to \(o\). On its \(23\) sheet construct the axes \(v\) of (2) using only the two transverse coordinates. The same tent estimate and path comparison work in two dimensions, with at most one strip instead of two. For each transverse site separately, extend its axis along a coordinate-ordered comb tree in the normal box. Include a margin of two about the support, so every face affected by a noncentral rotation has all its vertices in the box. On a bond \(f=xy\) belonging to such a face at normal distance \(s\) from \(o\),
\[
 {\mathbb E}|v_x-\operatorname{Ad}_{U_f}v_y|^2
           \le C[b^{-2}+(b+s+1)/\beta].                                \tag{8}
\]
For a normal bond, slide it to its place in the comb by a width-one strip of length \(O(s+1)\). For a transverse bond, compare it with the parallel root bond by sliding the two normal path segments successively. This uses at most two such strips. Add the error of the transverse root bond from (2). The squared triangle inequality and (1) give (8). The reference roots, strip paths and boxes are deterministic.

**PROVED.** For either common sign \(\epsilon=\pm1\), set
\[
                U'_e=\sigma_e\exp(\epsilon a_e v_x)U_e
\]
on positive edges starting at \(x\). Edges outside the boxes need only their central multiplier. For fixed auxiliary Gaussians the whole map preserves product Haar. The transverse links used for the root axes are unchanged. On each oriented tree edge the original transport maps the child's axis to the parent's axis in the direction of transport toward the parent. Left rotation at the positive tail produces the same adjoint transport of that axis. Thus the reconstructed axes are unchanged. Expose tree edges starting at their parents. For a positive edge from parent to child the map is left multiplication by a known unit quaternion. For a positive edge from child to parent, \(\exp(\epsilon a_e v_x)U_e=U_e\exp(\epsilon a_e v_{\rm parent})\). This is right multiplication by a known quaternion. On remaining normal edges the axes are already known and the map is left multiplication. Conditional Haar invariance in this order proves the claim, including bijectivity by undoing the multiplications. The central factors have trivial adjoint action.

**PROVED (averaging the two rotations).** Around a face write its transformed signed holonomy as \(B_\epsilon U_p\), where \(B_\epsilon\) includes \(\tau_p\sigma_{\partial p}\). Pull the four inserted factors to the base along the original links, using the signs of the oriented edges. Their transported axes differ from the base axis by at most
\[
                 d_p=\sum_{f=xy\in\partial p}|v_x-\operatorname{Ad}_{U_f}v_y|.
\]
For a reverse edge use the path to the positive tail, including that edge. Replacing each axis by the base axis costs at most \(d_p\sum_{e\in\partial p}|a_e|\) in chord. The common-axis product has distance at most \(\pi\rho_p\) from one. Therefore \(1-\operatorname{Re}B_\epsilon\le C[\rho_p^2+d_p^2\sum_{e\in\partial p}a_e^2]\). For the imaginary part of \((B_++B_-)/2\), expand the four factors into cosines and imaginary units times sines. Only even subsets of sine factors survive. With a common axis every even product is real. Replacing the axes in each surviving product of two or four units costs at most \(4d_p\). Its sine coefficient is bounded by \(\tfrac12\sum_{e\in\partial p}a_e^2\), using any two distinct sine factors. Thus the imaginary part is bounded by \(C d_p\sum_{e\in\partial p}a_e^2\). Since \(|\operatorname{Im}U_p|^2\le2(1-w_p)\), the arithmetic mean of the two signed action increases on this face is at most
\[
 C\left[\rho_p^2+
       \left(d_p^2+1-w_p\right)\sum_{e\in\partial p}a_e^2\right].
                                                                    \tag{9}
\]
This bounds the arithmetic mean of the two differences. It need not bound the positive part for each sign separately.

**PROVED.** Sum (9), use (1), (7), (8) and the bounded number of faces incident to each edge. The mean action increase times \(\beta\), averaged over the two signs and the auxiliary axes, is at most
\[
 C m\{\beta/R^2+(\beta/b^2+b+1)\log(2R)+R\}.
\]
Choose \(b=R=\max(2,\lfloor\beta^{1/3}\rfloor)\), with an absolute adjustment for bounded \(\beta\). The transformations for (5) still reverse all lines in exactly one collar, so (4) proves (5). For (6), change variables in \(Z_{\rm tw}\) by each fixed Haar-preserving map. Jensen bounds \(-\log(Z_{\rm tw}/Z_0)\) above by the mean of \(\beta[S_\tau(U')-S(U)]\) under \(\mu\). Averaging these valid bounds gives (6). For example, in the physical box the negative logarithm of the smaller majority probability is \(o(\beta n^2)\). This holds independently of the value of the neutral heat trace. Uniform area order with a coefficient tending to zero *after division by \(\beta\)* has a different limit from the sublinear-in-side test at each fixed coupling in row 1161 (13). [Fixed-coupling consumer](gap-solve9-astra62.md)

## How much more likely a reversal is when only the collars are fixed

**PROVED.** Keep fixed positive time aspect, \(m=n^2\), and now draw the two ordinary Wilson completions conditional on *all* their common spacetime adjoint links. Denote the negative-majority probability in this experiment by \(p_{\rm all}\), with the same odd tie rule. If \(\beta/\log n\to\kappa>1/6\) is finite, then
\[
  1-\frac1{6\kappa}\ \le\
    \liminf\frac{-\log p_{\rm all}}{\beta m}
    \ \le\ \limsup\frac{-\log p_{\rm all}}{\beta m}\ \le\ 4 .          \tag{10}
\]
In the collar-only experiment (5) gives \(-\log p/(\beta m)\to0\). In particular their probabilities differ by an exponential factor on the scale \(\beta m\) under the actual Wilson laws. The one-line statistic has much larger local sign noise. Row 1167 (14) measured that one-line noise, and (20) bounded the probability of an intermediate number of negative lines in the collar experiment. [Row 1167](gap-solve12-astra62.md)

**PROVED (joint face bound used here).** Given all adjoints, the two sets of fundamental links differ by a sign one-cochain. Its mod-two curvature \(B\) is exact. For a specified set \(S\) of faces, put \(k=|S|\) and let \(d_i\) count its faces containing direction \(i\). With \(h=e^{-\beta}/z_\beta\), \(z_\beta=\int e^{-\beta(1-\operatorname{Re}u)}du\),
\[
             \Pr(S\subseteq B)\le h^{\max_i d_i},
        \qquad \max_i d_i\ge k/2,\qquad \log h=-\beta+O(\log(2+\beta)).
                                                                    \tag{11}
\]
For clarity, this use of row 1167 (1)–(2) can be verified directly. Delete specified plaquettes sharing direction \(i\) as electric faces in that time frame. The normalized one-link Wilson convolution dominates the Haar projection because it fixes constants and has nonnegative remaining Fourier multipliers, since the exponential of the fundamental character expands in tensor powers with nonnegative coefficients. Tensoring and sandwiching by the spatial half-weight and the gauge projection gives each modified normalized layer \(0\le F_s\le F\). Its Schatten norm of order the time period \(u\) is at most \((\operatorname{Tr}F^u)^{1/u}\) by eigenvalue ordering. Trace Hölder bounds the product trace by \(\operatorname{Tr}F^u\). Undoing the normalizations gives \({\mathbb E}\exp[\beta\sum_{p\in D}(1-w_p)]\le z_\beta^{-|D|}\). On disagreeing faces the two deficits sum to two. Exponential Markov and Cauchy–Schwarz applied to the two Wilson marginals on a maximizing directional subset \(D\) give (11). The Haar ball of radius \((1+\beta)^{-1/2}\) supplies \(z_\beta\ge c(1+\beta)^{-3/2}\), and \(z_\beta\le1\).

**PROVED (which components to charge).** Connect faces belonging to a common three-cube. Fix a large integer \(K\), independent of \(n\). Keep every component of \(B\) having at least \(K\) faces. Among smaller components keep only those with odd pairing with some ribbon between the two endpoint lines. Each small component is closed in the dual lattice since all incident faces in any one primal cube belong to the same component and \(dB=0\). For large \(n\) it lifts inside a box of width \(O(K)\) where its dual cycle bounds. One can fill by projecting to a coordinate hyperplane and adding the prisms swept out, repeating in each coordinate within the same box. In primal notation this gives a compactly supported one-cochain \(c\) with \(dc\) equal to this component. By Stokes, the pairing with either arc of a ribbon equals the difference of the two boundary windings of \(c\). If nonzero, the small component has a face within \(O(K)\) of an endpoint slice. It has at least six faces in direction 1. Indeed \(\sum_{x_1}c_1(x_1,y,t)\) is then one at some transverse vertex and vanishes outside the box. Its support has an entering and a leaving edge in each of three transverse coordinate lines through this vertex. Summing \(dc\) over each corresponding strip requires six distinct direction-1 faces. This is the directional count of row 1167.

**PROVED.** If the majority is negative, at least \(m/2\) parallel lines have \(\theta_y=-1\). Each of these has an odd number of relative \(14\) faces on *each* of its two complementary ribbons, by Stokes. Discarded components have zero pairing with both. The two ribbons per line and different lines have disjoint faces. Consequently the union of the kept components has \(d_1\ge m\), including at a tied count. This conclusion also covers large components that wrap the torus.

**PROVED (entropy of the possible supports).** Choose \(0<s<1-1/(6\kappa)\). Choose \(\gamma>1/(6\kappa)\) and \(\varepsilon>0\) with \(s+\gamma+\varepsilon=1\). For any specified family of disjoint kept supports its probability is bounded by
\[
       h^{s d_1}\prod_{S\ {\rm small}}h^{6\gamma}
                         \prod_{S\ {\rm large}}h^{\varepsilon |S|/2}.
\]
Indeed (11) on the *union* pays \(d_1\) for the fraction \(s+\gamma\) and half its size for the remaining fraction. This avoids any assumption about independent components. A connected set of size \(k\) at one face has at most \(C_0^k\) choices by a walk round a doubled spanning tree of the bounded-degree face graph. Small candidate supports number at most \(C_K n^3\) by endpoint proximity. For large supports one may start at any of \(C n^4\) faces. Pull out \(h^{s m}\), sum over unordered compatible families and bound the remaining sum by the unrestricted product of \(1+\) each support weight. Its logarithm is at most
\[
 C_K n^3 h^{6\gamma}
       + C n^4\sum_{k\ge K}(C_0h^{\varepsilon/2})^k=o(\beta m).
\]
In the first term \(6\gamma\kappa>1\). Choose \(K\) so large that the second term tends to zero, using \(\log h/\log n\to-\kappa\). This proves the lower limit in (10) by taking \(s\) up to its endpoint.

**PROVED (other bound in (10)).** Multiply the first path by the central cut flip on one intervening time interval without smoothing either discontinuity. This preserves *all* adjoints, reverses all the \(\theta_y\), and changes just \(2m\) plaquette signs. Its density relative to the original two-completion law lies between \(e^{-4\beta m}\) and \(e^{4\beta m}\), since each changed deficit differs by at most two. Thus \(p_{\rm all}\ge e^{-4\beta m}(1-p_{\rm all})\). This proves (10). In particular replacing the unknown collar probability by the full-adjoint one loses exponentially even when both are small. The bound \(p\ge\exp[-o(\beta m)]\) still allows \(p\to0\).

## Sharp cost of a majority reversal with the spacetime adjoints fixed

**PROVED.** The bounds in (10) can be sharpened to an exact rate. On the even spatial grid, at fixed positive time aspect, for every finite \(\kappa=\lim\beta/\log n>0\),
\[
 \boxed{\displaystyle
 \lim\frac{-\log p_{\rm all}}{\beta n^2}
          =\min\left\{1,\ \max\left(0,\,3-\frac1{2\kappa}\right)\right\}.}
                                                                    \tag{12}
\]
The same rate holds for a strict negative majority. In particular it is one at the conditional one-loop slope \(11/(3\pi^2)>1/4\). The two bounds that meet in (12) come from different Wilson fluctuations.

**PROVED (improved upper probability bound).** On each kept small component the six-face argument above gives at least four direction-1 faces of *spatial* orientations \(12,13\), in addition to its \(14\) faces. To see this, use one endpoint where its compact primitive winding is one. On that time slice each of the two transverse spatial coordinate lines through this vertex has an entrance and an exit. Their four strips require four distinct spatial faces. Also \(d_{14}\ge2\) on this component by its nonzero pairing on both arcs. Choose \(s<\min(1,3-1/(2\kappa))\), \(s>0\), and \(\varepsilon>0\) so small that \(s<1-\varepsilon\) and \(\kappa[6(1-\varepsilon)-2s]>1\). Pay \((1-\varepsilon)d_1+\varepsilon k/2\) in (11). Extract \(s d_{14}\) on every component. A kept small component has at least
\[
 (1-\varepsilon)(4+d_{14})-s d_{14}\ge 6(1-\varepsilon)-2s
\]
left. The union has \(d_{14}\ge m\). The support sum used in (10), with this new small-component exponent, again has log \(o(\beta m)\). This proves the required lower bound on the rate. If its stated value is zero, \(p_{\rm all}\le1\) suffices.

**PROVED (single-link fluctuations give the other side of the sloping branch).** Take the \(m/2\) parallel lines of one transverse checkerboard at the first endpoint. In the first path leave all their longitudinal links unexposed. No plaquette contains two of them. Given the fundamental exterior, each has an independent quaternion law proportional to \(\exp(k_e\cdot u)\), \(|k_e|\le6\beta\). Revealing its adjoint leaves just the two opposite lifts. With \(s=|k_e|\), the error of the more likely lift, averaged over the adjoint, is
\[
 q(s)=\frac{\int_{-1}^0 e^{s t}\sqrt{1-t^2}\,dt}
               {\int_{-1}^1 e^{s t}\sqrt{1-t^2}\,dt}
       \ \ge\ c\sqrt{1+s}\,e^{-s}.
\]
The numerator for \(s\ge1\) is bounded below by \(c/s\) on \([-1/(2s),0]\). The denominator is at most \(C e^s s^{-3/2}\) by setting \(v=1-t\). Exponential tilting makes \(q\) nonincreasing. After revealing all adjoints and the second path the undrawn signs still have these independent posteriors conditional on the first exterior. On each selected line the smaller parity probability is \((1-\prod_{e}a_e)/2\), where \(a_e\) is the modulus of the one-link posterior bias. The lower bound applies for every second-path template. Average the product using independence of the first path's selected adjoints conditional on its exterior. Thus
\[
  \Pr\{\theta_y=-1\text{ on all selected lines}\}
       \ge \left[\tfrac12\{1-(1-2q(6\beta))^n\}\right]^{m/2}.           \tag{13}
\]
This uses the single-link estimate of row 1157 and the conditional product argument of row 1167 for a different tail event. To force a strict majority, require one further line to be negative. Flipping one longitudinal link of that extra line leaves the selected event and all adjoints fixed and changes at most six plaquette deficits by at most two each. It costs at most a factor \(1+e^{12\beta}\) in this lower bound, by pairing the two signs. Since \(1-(1-x)^n\ge c\min(1,nx)\), (13) bounds the upper limit of the rate by \(\max(0,3-1/(2\kappa))\). [One-link posterior, (8)](gap-solve8-astra62.md)

**PROVED (a connected patch gives the flat branch).** Assume \(\kappa>1/6\). In the full-adjoint experiment \(N_-/m\to0\) in probability, where \(N_-=\#\{y:\theta_y=-1\}\). For a specified \(y\), a component of size at least \(K\) meeting its ribbon costs at most \(C n^2(C_0\sqrt h)^K=o(1)\) by (11) with \(K\) fixed sufficiently large. Any smaller component changing this line is within \(O(K)\) of one of its \(2n\) boundary links and costs \(h^6\), as proved above. The union bound \(C_K n h^6=o(1)\) gives the claim by translation and Markov.

**PROVED.** Fix \(1/2<d<1\). Take a transverse strip \(D\) consisting of \(\lceil d n\rceil\) full rows, of size \(q_D=dm+O(n)\), with boundary length \(2n\) for large \(n\). At the first endpoint select just the direction-1 link at \(x_1=0\) on each of these lines. Let \(C_D\) flip these links by the center. Construct axes on the transverse \(23\) plane by the two-dimensional version of (2), with \(b\) of order \(\beta^{1/3}\). For fixed auxiliary variables let \(J\) left-multiply every selected link by its pure imaginary unit \(v_x\). The map \(C_D J\) multiplies by \(-v_x\). Both maps preserve Haar. They induce the same bijection \(j\) on the entire adjoint field, since the axes use only transverse adjoint links that both maps fix. They act on Wilson lifts equivariantly with respect to changing *any* link sign.

**PROVED.** Write \(M=2q_D\) for the number of affected temporal plaquettes. Each contains exactly one changed link. After either map its absolute normalized trace is at most \(|\operatorname{Im}U_p|\) because the transported insertion is a pure imaginary quaternion, including after inversion. By (1) the expected change in each deficit is at most \(1+C/\sqrt\beta\). On a spatial interior face two selected links occur and the transported axes differ by mean square \(O(\beta^{-2/3})\) from (2). Equal axes would cancel. The same squared chord inequality as in (3) bounds its mean action increase by \(C(\beta^{-2/3}+\beta^{-1})\). Only \(O(n)\) spatial boundary faces contain one selected link, and each costs at most two. Consequently the relative entropies of \(J_*\mu\) and \((C_DJ)_*\mu\) against \(\mu\), each averaged over the auxiliary variables, are at most \((1+o(1))\beta M\).

**PROVED (pay for the common adjoints once).** Denote the adjoint marginal by \(\mu_V\). For *each* fixed auxiliary choice,
\[
 D(j_*\mu_V\|\mu_V)
 \ \ge\ \beta\,{\mathbb E}_{j_*\mu_V}\sum_{p\ {\rm temporal,\ affected}}(1-|w_p|)
          -\log{\mathbb E}_{\mu_V}\exp\!\left[\beta\sum_p(1-|w_p|)\right]
 \ \ge\ (1-o(1))\beta M.                                              \tag{14}
\]
In the exponential use the same \(M\) faces throughout. The first inequality follows by comparing to the exponential tilt, whose relative entropy is nonnegative by convexity. The first expectation is at least \(M(1-C/\sqrt\beta)\) by the pure-imaginary insertion. The log moment is at most \(M\log(1/z_\beta)\) by the deletion estimate in (11), since \(1-|w_p|\le1-w_p\). All errors here are uniform in the auxiliary choices.

**PROVED.** Transform the first path by \(C_DJ\) and the second by \(J\), using the same fixed auxiliary variables. Call the original joint law \(P\) and its image \(Q\). Conditional on their new common \(V\), the paths are still independent since \(j\) is invertible. Splitting the log densities into the marginal and two conditional densities gives
\[
 D(Q\|P)=D((C_DJ)_*\mu\|\mu)+D(J_*\mu\|\mu)-D(j_*\mu_V\|\mu_V).
\]
Its auxiliary average is at most \((1+o(1))\beta M\). The winding-*ratio* signs of the two paths before applying \(C_D\) are unchanged by common \(J\) since identical adjoints link by link give the same relative sign one-cochain after transformation. After \(C_D\), exactly the \(q_D\) selected entry signs \(\theta_y\) reverse. Thus \(Q(N_->m/2)\to1\), uniformly in the auxiliary choices, from \(N_-/m\to0\) under \(P\). For \(E=\{N_->m/2\}\), binary relative entropy gives \(D(Q\|P)\ge Q(E)\log(1/P(E))-\log 2\). Average over the choices, divide by \(\beta m\), and send \(d\downarrow1/2\). This supplies the upper rate one for the strict majority. Together with (13) and the component bound it proves (12).

## A neutral trace test after erasing a growing set on one slice

**PROVED.** Let \(X_+(u)\) be the heat trace in the zero electric character. Take \(0<\kappa_0\le\beta/\log n\le\kappa_1<\infty\) eventually. On each of two opposite slices omit the same \(k\le c_*\log n\) raw spatial links, no two on a common spatial face. Keep every other spatial link \(R\) on that slice. Here \(c_*>0\) depends only on \(\kappa_0,\kappa_1\). Write \(H_{+,R}(u)\) for the affinity of the resulting two-end distribution to the product of its marginals in the positive neutral kernel experiment defined below. Set \(t=2\lfloor n/4096\rfloor\). At one permitted physical size,
\[
 \begin{split}
 -\log H_{+,R}(t)=o(\sqrt n),\quad
  \liminf H_{+,R}(2t)>\sqrt{2/3}
   \quad\Longrightarrow\quad
                 \limsup X_+(2t)<3/2.                                  \tag{15}
 \end{split}
\]
Thus the neutral one-cube test of row 1161 holds at its required time, by monotonicity. The same implication holds with the full ordinary trace and its ordinary pair law throughout. The proof uses spatial staples in the true Wilson measure. The uniform cross-ratio estimate in row 1167 (11) loses its physical-time conclusion already at two omissions at the one-loop slope. Temporal collars enter the proof of (15) only as integrated variables. The observed experiment uses two single slices.

**PROVED (kernels).** Work in the vacuum Markov representation \(P=\psi^{-1}U\psi\) with probability \(\pi(dx)=\psi(x)^2dx\) on spatial links and symmetric kernel \(p_s\) for \(P^s\) against \(\pi\). Extend by vertex gauge projection on the raw spatial space. The constant is the vacuum. The projection \(E_+\) averages the eight flat flips and commutes with \(P\). For period \(2s\) the relevant nonnegative square-root kernels are \(K=p_s/\sqrt{X(2s)}\) and \(K_+=p_{+,s}/\sqrt{X_+(2s)}\), with \(p_{+,s}(x,y)\) the average of \(p_s(x,gy)\) over the flips. Each has Hilbert–Schmidt norm one. Its square pointwise, times \(\pi\otimes\pi\), defines the appropriate pair law. Observe \(R\) at each end and take the square-root affinity \(\int\sqrt{d\nu\,d(\nu_1\otimes\nu_2)}\). This defines the \(H\)'s in (15). The inequality \(X(u)\le8 X_+(u)\) follows because \(\operatorname{Tr}(E_+P^u)\) is the average of eight nonnegative twisted kernel integrals, one being \(X(u)\).

**PROVED (the shorter period).** For either kernel the elementary bound of row 1167 (21) gives \(\log X_{\rm sec}(t)\le16k\beta-2\log H_{{\rm sec},R}(t)\), with \({\rm sec}\) full or neutral. Indeed varying the \(k\) missing last links changes the final temporal Boltzmann factors by ratios between \(e^{-2k\beta}\) and \(e^{2k\beta}\) after extracting the spatial half-weight. The vacuum eigenfunction divided by the same half-weight has the same ratio bound by its one-step equation. Their quotient, hence \(p_s\), varies by at most \(e^{4k\beta}\) in one end and \(e^{8k\beta}\) in both. The flip average preserves the bound. With \(Q\) conditional expectation under \(\pi\) given \(R\), the kernel of \(QK_{\rm sec}Q\) dominates \(e^{-8k\beta}\) times the conditional root mean square of \(K_{\rm sec}\) on both fibres. Test it on the rank-one product of the square roots of the observed marginal densities, lifted to \(\pi\). Its operator norm is at most \(X_{\rm sec}(t)^{-1/2}\) at this period. This gives the logarithmic bound. Thus (15)'s first hypothesis gives \(\log X(t)=o(\sqrt n)\), using \(X\le8X_+\) when appropriate.

**PROVED (local conditional laws).** Use three successive slices \(X_{-1},X_0,X_1\) in the stationary vacuum path, retaining the temporal transporters between them. These can be sampled by the normalized projected Wilson kernel before integrating its temporal links. Write \(B\) for both neighbours and these transporters, with \(R\) the retained part of \(X_0\). Given \(B,R\), the missing quaternions \(v_e\) have product law
\[
 q_B(dv)=\prod_e\frac{\exp(\beta h_e\cdot v_e)}{\Phi(\beta h_e)}\,dv_e,
 \qquad h_e=\sum_{j=1}^6 u_{ej}.
\]
Each \(u_{ej}\) is the unit staple from one of the six incident faces. The vacuum factors are at the two outer slices. The full spatial action at \(X_0\) supplies its four spatial staples. No action face uses two missing links. Choose one spatial staple \(s_e\) at each link by a deterministic orientation rule. It is known from \(R\).

**PROVED.** Define the good event \(G\), measurable from \(B,R\), by
\[
          \beta\sum_{e,j}|u_{ej}-s_e|^2\le M,\qquad M=\eta\log n .
\]
For either ordinary thermal period \(2t+2\) or the stationary vacuum, the bad-event probability is at most \(C^k e^{-c M}\). In fact the displayed sum without \(\beta\) is bounded by \(C\sum_{p\ {\rm incident}}(1-w_p)\), by inserting the central \(v_e\) and using that \(s_e\) is one of the six staples. Row 1155 (9) bounds \({\mathbb E}\exp(c\beta\sum_D(1-w_p))\le C^{|D|}\) on any ordinary rectangle. Its proof halves the marked electric couplings in one direction at a bounded normalization cost per mark, using the ordered normalized one-link multipliers of row 1149 (16). Trace Hölder bounds the product of the modified layers, and ordinary Hölder combines four direction classes. The vacuum bound also follows by taking the long-cylinder limit at fixed spatial size. [Marked-face proof](gap-solve7-astra62.md) · [Multiplier order](gap-solve4-astra62.md)

**PROVED.** On \(G\), each \(h_e\cdot s_e=6-\frac12\sum_j|u_{ej}-s_e|^2\ge5\) if \(\eta\) is small relative to \(\kappa_0\). Let \(\ell_R\) be product probability Haar restricted to the caps \(|v_e-s_e|\le\beta^{-1/2}\), normalized on each cap. Then
\[
                   q_B\ \ge\ \delta\,\ell_R,\qquad
                    \delta=\exp[-C(k+M)].                              \tag{16}
\]
Indeed \(\Phi(\beta h_e)\le C e^{\beta |h_e|}\beta^{-3/2}\) by the polar integral, and each cap has Haar volume at least \(c\beta^{-3/2}\). On the cap \(|h_e|-h_e\cdot v_e\le \sum_j(1-u_{ej}\cdot v_e)\le C/\beta+C\sum_j|u_{ej}-s_e|^2\). Multiplication proves the claim.

**PROVED (spectral cost of the exceptional histories).** Regard \(f(x)=p_t(x,\cdot)/\sqrt{X(2t)}\) as a vector in \(L^2(\pi)\), and put \(e_t=1-X(2t+1)/X(2t)\). Then
\[
 {\mathbb E}_\pi\|f(X_0)\|^2=1,\qquad
 {\mathbb E}\|f(X_0)-f(X_1)\|^2=2e_t,\qquad
 e_t\le t^{-1}\log[X(t)/X(2t)]=o(n^{-1/2}).
\]
The first two identities follow by composing symmetric kernels. For the inequality average \(1-r\le-\log r\) over normalized eigenvalue weights \(r^{2t}/X(2t)\), then use Jensen on \(r^{-t}\). Let \(b_t={\mathbb E}[1_{G^c}\|f(X_0)\|^2]\) in the three-slice stationary experiment. It satisfies
\[
                  b_t\le C^k e^{-cM}+2\sqrt{2 e_t}.                    \tag{17}
\]
In this expectation replace the square by \(\langle f(X_{-1}),f(X_1)\rangle\) at cost at most \(2\sqrt{2e_t}\) by Cauchy–Schwarz and the preceding identities. The inserted inner product is \(p_{2t}(X_{-1},X_1)/X(2t)\). It closes the stationary segment into an ordinary period \(2t+2\), multiplying the probability of \(G^c\) there by \(X(2t+2)/X(2t)\le1\). The transporter factors on the short segment are the same Wilson factors on both sides of this identity. This step avoids assuming a density bound between thermal and vacuum slices.

**PROVED (separate channels).** Let \(\chi(x)=\Pr_\pi(G\mid X_0=x)\) in the stationary experiment. On each \(R\)-fibre take the normalized nonnegative vector proportional to \(\sqrt\chi\) in its conditional \(L^2(\pi)\), using the constant one if \(\chi\) vanishes on that fibre. Let \(D\) project onto this line on every fibre. From (16),
\[
 {\rm dist}(f,{\rm ran}(D)\otimes L^2(\pi))
           \le \sqrt{b_t}+\sqrt{2(1+\delta^{-1})e_t}.                   \tag{18}
\]
To verify it, put \(a_R=\int f(R,v)\ell_R(dv)\). Given good \(B,R\), the squared distance from the \(q_B\)-mean of \(f\) to \(a_R\) is at most \(\delta^{-1}{\rm Var}_{q_B} f\) by (16) and Jensen. The expected conditional variance is at most \({\mathbb E}\|f(X_0)-f(X_{-1})\|^2=2e_t\). Thus \({\mathbb E}\chi\|f-a_R\|^2\le2(1+\delta^{-1})e_t\). Also \(\|f-\sqrt\chi f\|_{L^2}^2\le b_t\), and \(\sqrt\chi\,a_R\) belongs to the stated range. All integrations at fixed cutoff are finite by compactness and the strictly positive continuous vacuum and kernels.

**PROVED.** Choose \(\eta>0\) so \(C\eta<1/8\) in (16) and its cap condition holds. Choose \(c_*>0\) smaller still so \(C c_*<1/8\) there and \(c_*\log C<c\eta/2\) in (17). Then \(\delta^{-1}\le n^{1/4}\) and (18) tends to zero. As an operator this says \(\|(I-D)K\|_{\rm HS}=o(1)\). Since \(K_+=\sqrt{X(2t)/X_+(2t)}\,K E_+\), the same holds for \(K_+\) with a factor at most \(\sqrt8\). By symmetry, projection on both ends costs \(o(1)\) for either kernel.

**PROVED.** Let \(l(x)\) be the nonnegative normalized vector defining \(D\) on its fibre. The square-root kernel \(B_0=l(x)l(y)\sqrt{{\mathbb E}[K_{\rm sec}^2\mid R_x,R_y]}\) fills each observed end independently from density \(l^2\) against conditional vacuum measure. Pointwise \(0\le D K_{\rm sec}D\le B_0\) by fibre Cauchy–Schwarz. Both lie in the projected tensor space, and \(\|B_0\|_{\rm HS}=1\). Orthogonality and \(\|B_0-D K_{\rm sec}D\|^2_{\rm HS}\le1-\|D K_{\rm sec}D\|_{\rm HS}^2\) give \(\|K_{\rm sec}-B_0\|_{\rm HS}=o(1)\). Test on the unit rank-one kernel formed by lifting each observed marginal square root with \(l\). The result is \(X_{\rm sec}(2t)^{-1/2}\ge H_{{\rm sec},R}(2t)-o(1)\), as required. Under (W), given any tolerance, the collar argument of row 1167 following (9) makes the cutoff limsup of the shorter full trace minus one smaller than that tolerance on a sufficiently large fixed dyadic enlargement. By eigenvalue expansion the squared Hilbert–Schmidt distance of the full normalized kernel from the constant one in vacuum coordinates is \(2-2/\sqrt{X(v)}\) at period \(v\). The corresponding neutral distance has the same formula with \(X_+\le X\). Observing \(R\) contracts Hellinger distance, as does taking either marginal. The triangle inequality then gives affinities arbitrarily close to one in these ordered limits, which supplies both necessary estimates with room.

## How many adjoint links can be left unobserved

**PROVED.** Keep both endpoint spatial slices and remove any deterministic \(r=o(n^2)\) other links from the full adjoint observation. Draw the two completions conditional on what is left. Formula (12) still holds, including for a strict negative majority. On the other hand, for *every* integer sequence \(w\to\infty\) with \(w\le\beta^{1/3}\), there is an observation omitting at most \(2n^2(w+2)\) temporal adjoint links, outside the two collars, for which
\[
                    -\log p=o(\beta n^2).                              \tag{19}
\]
Here (19) concerns the odd majority with its stated tie convention. The lower bound from a change reversing every entry applies equally to both signs of this bit.

**PROVED.** On the unobserved links assign the relative cochain sign \(+1\), whatever the two true lifts there. Take its exact coboundary on the whole torus. The parity on every endpoint winding is still the required relative sign. Every face avoiding the holes has the correct Wilson sign comparison. For a specified set of faces the bound (11) therefore loses at most \(h^{-6r}\) for the entire set, because there are at most \(6r\) faces touching a hole in four dimensions. Use this loss just once on the union in the proof of (12). Its log is \(o(\beta m)\). Geometry, including the compact fillings, applies to this formally completed binary cochain. If \(\kappa>1/6\), the same bound with threshold \(N_-\ge\epsilon m\) for any fixed \(\epsilon>0\) extracts \(h^{2s\epsilon m}\). It gives \(N_-/m\to0\), also with these holes.

**PROVED.** In the matching upper-rate construction \(J\) uses only the transverse adjoints on the first endpoint slice. It induces a bijection of the observed adjoints. Of the \(M\) temporal faces in (14), at least \(M-6r\) still have observable magnitudes. Restricting the entropy test to these faces changes its lower bound by \(o(\beta m)\). The two-completion entropy subtraction holds with this observed marginal instead of the full one. The winding-ratio signs are still unchanged by simultaneous \(J\) since both endpoint slices have the same adjoints. The conditional proof of (13) only needs the selected adjoints and the second path to be drawn conditional on the common observations. It continues to hold after revealing the full first exterior. These facts prove the stability statement.

**PROVED.** For (19), put the central slab flip used in (5) on the first path. At each of its two temporal discontinuities rotate *temporal* links only. In the spatial plane of their lower endpoints take the axis (2) with tangential directions \(1,2,3\). As a function of \(x_1\), take a real angle jumping from \(0\) to \(\pi\) at the affected face, then returning linearly to \(0\) in \(w\) steps. The jump is cancelled by the central change on that face. Central multipliers on spatial links do not change the adjoint axes. Only the temporal links in the two indicated width-\(w\) regions can change their adjoints. Conditional Haar translation on those links, and the fixed central change on spatial links, give a bijection preserving Haar. It fixes the specified observation pointwise and toggles every relative line product. The proof of (3), with roles of time and direction one exchanged on the two cuts, gives cost \(C m[\beta/w+\beta w(b^{-2}+b/\beta)+w]\), including the spatial Wilson plaquettes used by (2). With \(b\) of order \(\beta^{1/3}\) this is \(o(\beta m)\) for the stated \(w\). Inequality (4) gives (19). Thus on the physical slope a subarea number of arbitrary holes preserves the unit rate, whereas a prescribed set of area times an arbitrarily slowly diverging width can destroy it.

**PROVED (the scale of the necessary deletion).** Fix \(C_1<\infty\), \(\kappa>1/6\), and retain the two endpoint spatial slices as above. For *any* deterministic choice of at most \(C_1m\) omitted adjoint links there is \(c(C_1,\kappa)>0\) such that, for large \(n\),
\[
                         p\le e^{-c(C_1,\kappa)\beta m}.                \tag{20}
\]
Consequently destroying the positive rate in (12) requires \(r/m\to\infty\). Equation (19) attains this scale with an arbitrarily slowly diverging factor. The geometry of the holes matters for sufficiency.

**PROVED (repair inside a ribbon).** Partition the \(14\) faces by transverse spatial position \(y\), then cut each resulting two-torus at the endpoint lines. A missing normal edge belongs to just one of these tori. Choose an integer \(K>8(C_1+1)\). Fewer than \(m/8\) tori contain more than \(K\) missing normal edges. In either arc of every other torus, cover the two incident faces at each missing edge by their smallest rectangle. A missing spatial edge cannot lie on an arc boundary under our observation convention. Repeatedly merge touching rectangles by taking their bounding rectangle. At most \(K\) initial rectangles are involved. Each final side is at most \(2K+2\) because each bounding width is at most the sum of the preceding widths when the rectangles touch. The same construction lifts across the spatial period for large \(n\), since an intersecting chain of these intervals has width less than the period. The boxes stay in the arc, and their boundaries have no missing edge since both faces along every missing edge are covered together.

**PROVED.** Call such a box expensive if the sum of both paths' plaquette deficits inside is at least \(c/(K+1)^6\), for a sufficiently small absolute \(c>0\). In a cheap box the relative sign on any simple cycle of known edges has product \(+1\). Fix a tree gauge separately in each path, setting the horizontal edges of the rectangle and the vertical edges of its left side to one. Successive vertical links in a given row then differ by one plaquette, up to conjugation or inversion. Their angles to the identity are bounded by the sum of at most \(2K+2\) plaquette angles. With \(S_B\) the sum of both paths' deficits in the box, Cauchy–Schwarz and \(\theta^2\le(\pi^2/2)(1-\cos\theta)\) bound each of those link angles by \(C\sqrt{(K+1)S_B}\). A simple cycle has at most \(C(K+1)^2\) edges. The bi-invariant triangle inequality makes the two holonomy angles sum to at most \(C(K+1)^{5/2}\sqrt{S_B}<\pi\) in a cheap box. A negative relative sign would give angles adding to \(\pi\). All cycles in the graph of known edges split into simple cycles and backtracks. Hence its sign cochain is the gradient of vertex signs on each component, by integration from a root. Fill the missing signs by the gradient of those vertex values, assigning any values at isolated vertices. The resulting \(14\) curvature vanishes throughout the cheap box. Elsewhere assign arbitrary missing signs. Arc endpoints are fixed. Each normal edge is filled in just one torus, so the construction extends to a single four-dimensional binary cochain. A fixed ordering makes all choices measurable.

**PROVED.** The union of all the candidate boxes is a deterministic set of at most \(C_K m\) normal faces. If at least \(m/8\) different good tori contain an expensive box, the two paths have total deficit at least \(c_K m\) on this set. The marked-face bound used for (16), followed by Cauchy–Schwarz on the two Wilson marginals, bounds its probability by \(\exp[-c'_K\beta m+C'_K m]\). In the remaining negative-majority event at least \(m/4\) tori have a negative line and have only cheap boxes. Keep the components of the filled curvature as in (10), using a size cutoff \(K'\) to be fixed independently of the box parameter \(K\). On each of those tori the kept curvature must be odd on both arcs. Any odd witness there avoids all holes because inside a cheap box its curvature vanishes, and outside the boxes every normal edge is observed. Thus the kept union contains at least \(m/2\) *clean* \(14\) faces.

**PROVED (count despite the holes).** Call a face dirty if it touches a missing edge, and apply (11) only to the clean members of each specified union. For a small kept component avoiding all dirty faces the earlier exponent six and the endpoint rooting still apply. Small supports meeting a dirty face have at most \(C_{K'}r\) choices altogether and may be counted at weight one. Choose \(\gamma>1/(6\kappa)\), \(s>0\) with \(\gamma+s<1\), and \(\varepsilon>0\) so small that \(\gamma+s+\varepsilon\le1\) and \(3\varepsilon C_1<s/4\). Allocate the fractions \(s,\gamma\) of the clean direction-1 count to the \(m/2\) witnesses and to the small clean components. The fraction \(\varepsilon\) of half the clean total size pays half the large sizes, less at most \(3\varepsilon r\) since there are at most \(6r\) dirty faces. The common factor is at most \(h^{s m/2-3\varepsilon r}\le h^{s m/4}\). The log sum over small dirty supports is \(O_{K'}(r)\). For the small clean and large supports the same exponential product bound as in (10) has log \(o(\beta m)\) after choosing \(K'\) large enough. This proves (20). The proof allows arbitrary correlations between completions through the observed links.

## Limits of the two estimates at the physical scale

**PROVED (cost of the positive profile estimate).** Try to obtain an order-one twist probability by optimizing the real cochain in (9). For one fixed elementary center defect in each normal torus, the positive expression on the right of (9), summed and multiplied by \(\beta\), has expectation at least \(c m\log(2+\beta)\) at large \(\beta\) and normal periods much larger than \(\beta^{1/4}\). This concerns deterministic real profiles, arbitrary choices of the axes, and the positive majorant used in (9). It accounts for the possibility of changing the profile radius or shape. For the two separated defects used to switch the majority, the same argument applies in a square about either one.

**PROVED.** First \({\mathbb E}(1-w_p)\ge c/(1+\beta)\) in the actual Wilson law. Condition on all links but one edge of \(p\). The density is \(\exp(k\cdot u)/\Phi(k)\), \(|k|\le6\beta\). Its mean lies on the field axis and has magnitude increasing with \(|k|\), since the derivative of its scalar mean is a variance. Thus the expected deficit to any staple is at least the expected deficit on the field axis at \(6\beta\). Integrating \(1-\cos\theta\) over angles between \((6\beta)^{-1/2}\) and \(2(6\beta)^{-1/2}\) in the polar formula gives \(c/\beta\) at large \(\beta\), using the matching upper bound on the normalizer. For deterministic \(a_e\), the \(1-w_p\) term of (9) therefore pays \(c\sum_e a_e^2\) after multiplication by \(\beta\). It suffices to use just the normal plaquettes.

**PROVED.** In a normal plane let \(f_p\in[-\pi,\pi]\) be the residual abelian angle, so that \(da_p\) differs from \(f_p+\pi\mathbf1_o(p)\) by an integer multiple of \(2\pi\). The ideal common-axis chord squared is comparable to \(f_p^2\) on this interval. Thus (9) pays at least a fixed multiple of \(f_p^2\). If \(\beta\sum f_p^2\ge\log\beta\) the claim follows already. Otherwise, on every centered square of radius \(1\le j\le\beta^{1/4}\) about \(o\), the sum of the absolute residual angles is bounded by \(C j\sqrt{\log\beta/\beta}=o(1)\), by Cauchy–Schwarz. Discrete Stokes then gives \(|\sum_{\partial Q_j}a_e|\ge\pi/2\), since the flux of the isolated defect is odd modulo \(2\pi\). Each boundary has \(O(j)\) edges and these boundaries are disjoint. Thus \(\sum a_e^2\ge c\sum_{j\le\beta^{1/4}}1/j\ge c'\log\beta\). Summing over \(m\) planes proves the claim. Even at fixed sufficiently large \(\beta\), as the symmetric side grows, this majorant is at least \(c_\beta m\), so it also misses the fixed-coupling sublinear-in-side consumer (13) of row 1161. The resulting lower bound concerns the unsigned estimate. The signed free-energy difference still permits cancellation.

**PROVED (one-slice consequence for bounded slow modes).** In the notation of (16)–(18), for any bounded scalar slice observable \(g\),
\[
 \|(I-Q)g\|_{L^2(\pi)}^2\le
  2(1+\delta^{-1})\langle g,(I-P)g\rangle_\pi
        +4\|g\|_\infty^2 C^k e^{-cM}.                                  \tag{21}
\]
Indeed use \(\int g\,d\ell_R\) as an \(R\)-measurable approximant. The good-event variance proof in (18) holds with \(g\) in place of \(f\). On the bad histories both values have modulus at most \(\|g\|_\infty\). Conditional expectation minimizes squared error. Thus bounded slow readings with Dirichlet energy \(O(1/n)\) survive the simultaneous erasure of \(c_*\log n\) separated links in a single slice, without a shorter-period input. Equation (15) needed that input to pay for the *whole* neutral trace.

**PROVED (limitation of the common minorant).** The exponential dependence on \(k\) in (16) is unavoidable for such a minorant uniform over well aligned local staples. Keep the retained central links and the two layers of temporal links equal to one. In both neighbour slices set the spatial links corresponding to the omitted edges to \(\exp(+i/\sqrt\beta)\) in one history and \(\exp(-i/\sqrt\beta)\) in the other, using one fixed quaternion axis \(i\). All other neighbour links can be the identity. These two histories have the same \(R\). The four spatial staples are one and the two temporal staples are the specified rotations. The local squared deviation times \(\beta\) is at most two per missing link. Each history has neighbourhoods of positive vacuum cylinder measure by positivity of the Wilson kernel. For the two product conditional laws the one-link square-root affinity equals
\[
 \frac{\Phi(\beta u)}
 {\Phi(\beta\sqrt{u^2+4\sin^2\theta})},
 \qquad u=4+2\cos\theta,\quad\theta=\beta^{-1/2},
\]
with \(\Phi(s)=\int\exp(s\,\operatorname{Re}v)\,dv\). The two scalar arguments differ by \(4\beta\sin^2\theta/(\sqrt{u^2+4\sin^2\theta}+u)\to1/3\), and \((\log\Phi)'(s)\to1\) by concentration on the field axis. The affinity therefore tends to \(e^{-1/3}\). A submeasure dominated by both laws has mass at most their affinity. The product affinity is at most \(e^{-c k}\) for all large \(\beta\). Continuity gives the same obstruction in open neighbourhoods with a smaller \(c\). Any uniform truncation that still allows this fixed deviation per link therefore incurs an exponential loss. At \(k/\log n\to\infty\) it cannot be paid by the \(O(n^{-1})\) Dirichlet scale alone. The frequency of these histories under the full Wilson law is a separate question.

**PROVED (the retained links can still carry a neutral level).** The conditional reconstruction in (15) alone places no numerical lower bound on its retained affinity. For an exact comparison use the original Wilson vacuum probability on the same slice. Choose one retained spatial plaquette, whose trace has a nonatomic law by conditioning on one fundamental link. Threshold at a median to obtain a balanced sign \(h(R)\), invariant under vertex gauges and all flat flips. Against \(\pi\) take the reversible Markov kernel \(1+\lambda h(x)h(y)\), \(0<\lambda<1\). The constant, \(h\), and their orthogonal complement have eigenvalues \(1,\lambda,0\). The two-end normalized square-root kernel at time \(t\) depends only on \(R_x,R_y\), so exact reconstruction holds at both ends. Its observed single-end law is \(\pi_R\), and its affinity at period \(2t\) is \((1+\lambda^{2t})^{-1/2}\). With \(\lambda=e^{-1/n^2}\) this tends to \(1/\sqrt2\), while a fixed \(\lambda<1\) gives limit one. Both have the shorter-period lower bound in (15). This is the earlier retained-mode obstruction of rows 1161 and 1167, here applied after growing erasures. The alternative kernels test inference from reproduction of the law and are different from the Wilson transfer. [Earlier one-slice comparisons](gap-solve9-astra62.md) · [Spatial-well comparison](gap-solve12-astra62.md)

## A direct lower bound for the specified adjoint surface reading

**PROVED.** The probability \(p_R\) in row 1167 (10) uses the explicit adjoint reading \(J_R^0\), which can make a local error. It has the following unconditional lower bound on every sufficiently large ordinary torus at fixed positive aspect, with constants depending only on that aspect and the fixed reading radius:
\[
                  p_R\ \ge\ c\min\{1,n^2 e^{-C\beta}\}.                \tag{22}
\]
The same lower bound, with changed constants, holds for the probability that this reading differs from the true boundary product \(W=s_1s_2\). In particular (22) is a polynomial lower bound on the *specified* open quantity along the physical trajectory. Its mechanism concerns local errors of the explicit reading. It does not give this polynomial bound for the majority.

**PROVED (a local sign change).** In fundamental variables the section-independent reading of row 1167 (9) equals \(W\prod_{p\in R}\xi_p g_p\), where \(\xi_p=\operatorname{sgn}w_p\). Its \(g_p\) tests all six-face sets sharing a direction within face distance 12. An admitted lift has positive sum of the six normalized traces on each set. If none is admitted the rule returns \(+1\). Choose a temporal link \(e\) in the interior of \(R\), away from the collars. The only raw signs \(\xi_p\) on the ribbon that depend on it belong to its left and right \(14\) faces. Each affected \(g_q\) is centered on a ribbon face within a fixed distance of \(e\).

**PROVED.** Around all those \(q\), impose the following pattern on a finite block of *spatial* links. In every relevant time slice use spatial unit cubes of orientation \(123\) based at even spatial triples. These cubes have disjoint vertex sets on one time slice. On one oriented boundary square of each cube take four successive directed links \(\exp(i\pi/4)\), respecting reversal on positive-coordinate variables, and take its other links to be one. That face has trace sign minus, the opposite face plus, and the four side faces have positive traces. The product of the six signs on the cube is negative on an open neighbourhood of these values. This product survives every change of link lifts because each edge occurs twice. The construction uses the local frustrated cube of the earlier syndrome arguments. [Related cube-parity construction](gap-solve8-astra62.md)

**PROVED.** For every affected \(14\) face \(q\), its distance-12 neighbourhood contains all faces of at least twelve of these disjoint cubes. In fact choose two even bases within distance two of its base in each spatial coordinate, and either time of the face. These are sixteen cubes. To check the distance, move first to a \(12\) face at the original spatial base and the specified time in a common \(124\) cube. Translating a \(12\) face by one in either in-plane direction takes at most two face steps through a side face, and a perpendicular translation takes one. Moving at most two in each spatial coordinate costs at most ten steps. From the resulting \(12\) face every face of its \(123\) cube is one more step away. Include the union of all these cubes in the finite block. At least twelve distinct faces must be negative in any lift. Their directional counts sum to at least twenty-four, so six negatives share a coordinate direction in the tested neighbourhood. The default therefore gives \(g_q=+1\) throughout, independently of \(e\).

**PROVED.** At fixed spatial links the two temporal neighbours of \(e\) on its winding ribbon prescribe independently the two unit staples against which the quaternion \(u_e\) is dotted on the two \(14\) faces. This follows by multiplication by fixed unit quaternions, and inversion if needed, on each of the two distinct neighbouring temporal links. Choose those links so that the two staples are \(1\) and \(i\) at the specified spatial values. Include any additional spatial links determining these staples in the block and fix them consistently. Small open neighbourhoods suffice. Then small caps about \((1+i)/\sqrt2\) and \((-1+i)/\sqrt2\) for \(u_e\) give opposite products of the two face signs. The other raw signs and the boundary windings do not depend on \(u_e\). All affected \(g_q\)'s have just been forced constant. Thus the two caps force opposite values of the local factor in \(J_R^0\), for every exterior. The sign values from the rest of the block can be arbitrary, since they are the same in the comparison of the two caps.

**PROVED (many disjoint blocks).** Conditional on any exterior the probability of the required neighbourhoods for the spatial links and two temporal neighbours is at least \(c_0 e^{-C_0\beta}\). For a fixed finite set of \(M_0\) links its conditional density relative to product Haar is at least \(\exp(-12M_0\beta)\), by counting incident plaquettes and their oscillations. This also gives the bound when \(u_e\) has yet to be revealed, by averaging the conditional inequality with it fixed. Given all block variables except \(u_e\), each of the two final caps has conditional probability at least \(c_1e^{-12\beta}\). Hence the conditional bias of the block factor, in modulus given the exterior, is at most \(1-c_2 e^{-C_2\beta}\). This follows by conditioning first on the other block variables and bounding the modulus by one off their required neighbourhoods.

**PROVED.** Pack \(N\ge c n^2\) blocks at a sufficiently large fixed spacing along the ribbon, excluding its collars. No plaquette and no local \(g_q\) reads links of two distinct blocks. Given the exterior the Wilson block variables are independent. The expression for \(J_R^0\) is an exterior sign times one sign factor per block, so its conditional bias has modulus at most \((1-c_2 e^{-C_2\beta})^N\). This bound passes to conditioning on the two collars alone. For conditionally independent completions \(p_R=(1-{\mathbb E}{\mathbb E}[J_R^0\mid A]^2)/2\). The stated inequality follows. Since \(W\) is known on the exterior, the same product bound on \(|{\mathbb E}(WJ_R^0)|\) proves the second assertion.

**PROVED (obstruction to local-error amplification).** On \(\liminf\beta/\log n>1/3\), the actual bound of row 1167 (6),(9) gives \(\Pr(J_R^0\ne W)\le C n^2 h^6=o(1)\). For every exterior observation \(\mathcal E\) containing \(W\),
\[
 {\mathbb E}\big|{\mathbb E}(J_R^0\mid\mathcal E)\big|
          \ge {\mathbb E}(W J_R^0)=1-o(1).
\]
Even the best estimate that takes this modulus before integrating the exterior cannot yield an order-one loss. In the collar experiment the conditional mean is signed, and the common winding sign remains to be averaged there. Equation (22) controls a source of disagreement that exists on both infrared branches.

**PROVED (a reversal with agreement between different ribbons).** On \(\liminf\beta/\log n>1/3\) at fixed positive aspect and \(\beta=O(\log n)\), (5) also gives a lower bound for a coherent change seen by the *explicit* rules. For any fixed \(0<d<1/2\), in the collar-only experiment,
\[
 \Pr\{B=-1,\ J_y^0(V)J_y^0(\widetilde V)=-1
                       \text{ on at least }(1-d)m\text{ ribbons}\}
       \ge \exp[-C_d m\beta^{1/3}\log(2+\beta)]                         \tag{23}
\]
for large \(n\). Here \(J_y^0\) denotes the translated straight-ribbon rule on each line. This avoids transferring an exponentially small lower bound through an additive one-ribbon error.

**PROVED.** In the original two-completion law almost all \(\theta_y\) have one common value in probability. For each end, a relative curvature component of size at least \(\lfloor r/10\rfloor\) meeting its central slice costs \(C n^3(C_0\sqrt h)^{\lfloor r/10\rfloor}\) by (11) applied within the common adjoint collar. Use a sufficiently large fixed radius \(r\). Each remaining small component incident to the central slice is closed in a buffered box of the collar. Fill it as above. The residual spatial cochain is flat, hence its winding is common on the parallel lines. A compact filling that changes a specified line has at least six direction-1 faces and lies within \(O(r)\) of the line, giving probability \(C_r n h^6=o(1)\). This is the upper argument of row 1167 (17). It holds uniformly in the line and also compares a specified line with \(B\), by Markov on the fraction of exceptions. For each path the original realised lift passes the six-face tests near each plaquette of a specified ribbon except with probability \(C n^2 h^6=o(1)\). This follows by full directional deletion and union over the bounded number of six-sets at each face. Thus in the original pair almost all \(J_y^0(V)J_y^0(\widetilde V)\) equal \(B\). Also \(\Pr(B=+1)\ge1/2-o(1)\), since the two readings on a specified line are conditionally independent copies given the collars.

**PROVED.** For the transform in (5), fix one ribbon. Outside the fixed-radius neighbourhood of its intersections with the two profile boxes the plaquette traces of the transformed path are unchanged. The central changes there have zero curvature. Inside the intersections and their fixed margins there are \(O(R^2)\) faces per bounded set of transverse coordinates. Their total expected original deficit is \(O(R^2/\beta)=o(1)\) by (1). For either sign of the profile, the squared-chord estimate *before* the average leading to (9), summed only over these faces, bounds the expected sum of \(|1-B_\epsilon|^2\) by
\[
 C\{R^{-2}+(b^{-2}+(b+1)/\beta)\log(2R)+R/\beta\}=o(1).
\]
Here \(b=R\) as in (5). Enlarge the intersection margins by the fixed testing radius once more. The triangle inequality and Markov now give, with probability \(1-o(1)\) for this ribbon, positive transformed face traces throughout the part of its testing neighbourhoods that meet the changes, including all faces in each such neighbourhood. Outside those neighbourhoods the original admissibility tests still pass with probability \(1-o(1)\). Hence the transformed actual lift is admitted along the ribbon and the explicit rule reads its changed winding product. The estimates include the auxiliary averaging and are uniform in the ribbon. By Markov the fraction of failed ribbons tends to zero in probability. Applying the transformation to just the first completion toggles \(B\) and thus produces the event in (23) with probability at least \(1/2-o(1)\), averaged over the transformations. The relative entropy bound used for (5), followed by the binary event inequality used in (14), proves (23).

**PROVED (how much a partial disclosure can change the test).** A single noisy bit from the middle can already change \(p_R\) by an arbitrary vanishing factor while preserving the one-path Wilson law. More precisely, given \(A\), let \(b={\mathbb E}[J_R^0\mid A]\). Reveal also \(Y=J_R^0 E\), where \(E\) is an independent sign of mean \(0\le\lambda<1\). Write \(p_\lambda\) for the reading-disagreement probability of independent completions conditional on \(A,Y\). Then
\[
 p_\lambda=\frac{1-\lambda^2}{2}
      {\mathbb E}\frac{1-b^2}{1-\lambda^2 b^2},
 \qquad (1-\lambda^2)p_R\le p_\lambda\le(1-\lambda^2)/2.               \tag{24}
\]
Indeed the two probabilities of \(Y=y\) given \(A\) are \((1+y\lambda b)/2\). The posterior sign mean is \((b+y\lambda)/(1+y\lambda b)\). Average half its complementary square to obtain (24). With all adjoints already known, disclosing \(Y\) changes no lift law at all. It also leaves the unconditioned adjoint endpoint pair law unchanged. At every fixed cutoff of (22), its uniform conditional block bound gives \(|b|<1\) almost surely. Therefore \(p_\lambda/(1-\lambda^2)\to1/2\) as \(\lambda\uparrow1\) by bounded convergence, for *every* value of \(p_R\) permitted by those finite-volume laws. Extrapolating that terminal slope cannot bound the undisclosed test at \(\lambda=0\).

## All winding lines and the cost of exact unanimity

**PROVED.** Let \(N_-\) count the negative \(\theta_y\) in the two-completion experiment. Take an even spatial grid, with both time arcs of fixed positive aspect. The elementary fluctuation behind (13) bounds the probability of *any specified pattern*, uniformly over every observation \(\mathcal A\) made from the first path's adjoints. Here the second path is drawn independently conditional on \(\mathcal A\). For a deterministic subset \(S\) of transverse sites and a sign template \(a\) on it,
\[
 v_*^{|S|}\le \Pr(\theta_S=a)\le(1-v_*)^{|S|},\qquad
 v_*=\tfrac12[1-(1-2q(6\beta))^n].                                    \tag{25}
\]
On the black sites of \(S\) leave the \(n\) longitudinal bonds of the *first* endpoint undrawn. On its white sites use the *other* endpoint. No plaquette contains two selected links. Given the first path exterior and its remaining adjoints the lift posteriors are independent, and revealing the second path changes none of them. Each line probability lies between \((1-\prod_e a_e)/2\) and \((1+\prod_e a_e)/2\), with \(a_e\) the one-link bias modulus from (13). This holds for every realization of the second path. Remove that template before averaging the bounds over the first path's selected adjoints, which are independent conditional on its exterior. This proves (25). The earlier one-end sparse sampling in row 1167 (17) proves an upper bound on the probability of very few minority lines. Using the two endpoints covers all \(m=n^2\) lines simultaneously. [Earlier minority-count estimate](gap-solve12-astra62.md)

**PROVED.** The expected total variation of the conditional law of the whole sign vector from \(m\) independent fair signs, given the first adjoints and the second path, is at most \(m(1-2q(6\beta))^n/2\). With the extra first exterior exposed, couple the independent Bernoulli posteriors to independent fair signs coordinate by coordinate. The sum of the mismatch probabilities is \(\sum_y\prod_e a_e/2\). Average as in (25), then forget the extra exterior by convexity. In particular for \(0<\kappa=\lim\beta/\log n<1/6\), the genuine majority is asymptotically fair even with all adjoints shared. This strengthens the zero-rate portion of (12). The physical slope is on the other side of this threshold.

**PROVED.** With *all* adjoints shared put \(I_\kappa=\min(1,\max(0,3-1/(2\kappa)))\). For every fixed \(0<d\le1\) the complete upper tail satisfies
\[
     \lim\frac{-\log\Pr_{\rm all}(N_-\ge d m)}{\beta m}
                         =2d I_\kappa .                                 \tag{26}
\]
For the lower bound on the rate, the kept components in (12) must now have \(d_{14}\ge2d m\), by disjointness of the two ribbons for every negative line. The same allocation extracts \(2sdm\) powers of \(h\), with the same error and allowed \(s\). For the other bound require \(\lceil dm\rceil\) prescribed negatives in (25). The single-link polar integrals in (13) also give \(q(s)\le C\sqrt{1+s}\,e^{-s}\), by bounding the numerator by \(1/s\) and restricting the denominator to \(1-t\in[1/(2s),1/s]\) at \(s\ge1\). Thus \(-\log v_*/\beta\to\max(0,6-1/\kappa)\). For \(d<1\) and \(\kappa>1/6\), apply the connected-strip transformation of (14) to a fraction \(d'>d\) and use \(N_-/m\to0\) before transformation. The event in (26) then has image probability tending to one. Send \(d'\downarrow d\) to get the competing upper rate \(2d\).

**PROVED (correcting the last lines).** Under any adjoint observation, changing one first-path longitudinal link by the center at a specified endpoint reverses just one \(\theta_y\), preserves the observation, and costs at most \(e^{12\beta}\) in density ratio. For \(i=0,m\) and each integer \(0\le k\le m\), partition by the set of exceptional lines and apply the appropriate fixed flips. This gives
\[
 \Pr(N_-=i)\ \ge\
 \frac{\Pr(|N_--i|\le k)}
      {e^{12\beta k}\sum_{j=0}^k{m\choose j}} .                        \tag{27}
\]
Overlaps between changed plaquettes only decrease the upper count of \(6k\) affected faces. Taking \(i=m,\ k=\lfloor\epsilon m\rfloor\) and then \(\epsilon\downarrow0\) gives the endpoint \(d=1\) of (26), since the sum of the binomial coefficients is at most \(2^m\). This completes its proof. The same rate persists with the \(o(m)\) omissions of (19). Its component count loses at most \(6r\) faces, (25) still holds, and the common-marginal entropy test for the strip loses at most \(6r\) of its temporal faces. At \(\kappa>1/6\), conditional on a negative majority with all adjoints shared, an excess fraction \(\epsilon\in(0,1/2)\) above one half has negative log asymptotic to \(2\epsilon I_\kappa\beta m\), by dividing (26) by (12). Exact unanimous reversal costs twice the majority rate.

**PROVED.** Suppose the observation includes sufficiently wide fixed endpoint adjoint collars, and \(\beta/\log n\to\kappa>1/6\) finite. Write \(D_n=\min(N_-,m-N_-)\). The compact-fill proof in (23) gives \(\mathbb E D_n\le C_r n^3 h^6\). Indeed choose the fixed collar radius \(r\) so \(n^3(C_0\sqrt h)^{\lfloor r/10\rfloor}\le n h^6\) for large \(n\), then sum the one-line error over both endpoints and all \(m\) lines. Additional shared adjoints preserve (11) on the collars. On each line \(\Pr(\theta_y=-1)\le1/2\) by conditional independence of the two winding products. Since \(|\mathbf1_{B=-1}-N_-/m|\le D_n/m\), one has \(\Pr(B=+1)\ge1/2-o(1)\). Choose \(k=\lceil C(1+n^3 h^6)\rceil=o(m)\) with \(C\) sufficiently large. Markov gives \(\Pr(N_-\le k)\ge1/3\) for large \(n\). Equation (27) then costs \(O(k[\beta+\log(m+1)])\) in its negative log, using \(\sum_{j\le k}{m\choose j}\le(m+1)^k\).

**PROVED.** In particular, throughout \(1/6<\kappa<1/2\), for *every* such disclosure,
\[
   \frac{\log[-\log\Pr(N_-=0)]}{\log n}\ \longrightarrow\ 3-6\kappa .
                                                                         \tag{28}
\]
The preceding correction gives the upper bound on the double logarithm since \(n^3h^6=n^{3-6\kappa+o(1)}\). The lower bound follows from \((1-v_*)^m\le e^{-mv_*}\) in (25), where \(mv_*=n^{3-6\kappa+o(1)}\). This last upper bound on the probability applies to unanimous *negative* signs as well. Thus at the physical slope a proof demanding an order-one probability that every line has a common sign is obstructed even when the majority sign itself mixes. Row 1167 gave the typical power for the number of minority lines. Equation (28) gives the probability scale at zero.

**PROVED.** When only the two collars are shared, (5) reverses every \(\theta_y\) and therefore sends the event \(N_-\le k\) to \(N_-\ge m-k\). Its entropy bound and the binary event inequality following (14) give the latter event probability at least \(\exp[-C m\beta^{1/3}\log(2+\beta)]\). In (27) the correction cost just proved is \(o(m)\) at every fixed finite \(\kappa>1/6\). Consequently
\[
 -\log\Pr_{\rm collars}(N_-=m)
      \le C m\beta^{1/3}\log(2+\beta),\qquad
 -\log\Pr_{\rm all}(N_-=m)=(2I_\kappa+o(1))\beta m .                   \tag{29}
\]
This comparison concerns actual fundamental winding products on every line. On the physical trajectory (28) and (25) also force the first negative log in (29) to diverge at least as \(n^{3-6\kappa+o(1)}\). Exact unanimity cannot provide the order-one event sought in (W).

## Remaining Wilson inequalities

**PROVED.** If a disclosure retains the two fixed-width endpoint collars and omits only \(O(n^2)\) adjoint links on the whole torus, its explicit-reading disagreement tends to zero on the slope \(>1/3\). Indeed (20) bounds its negative-majority probability. The compact-fill estimate in (23) compares the majority to a specified line with error \(o(1)\), and each path's own reading differs from its true line product with probability \(O(n^2h^6)\). These bounds need only the common collars and the correct individual Wilson marginals. In the full-adjoint experiment the explicit reading is already known, while (12) concerns the residual ambiguity of the *fundamental* lines.

**OPEN.** At the endpoint-only disclosure, use period \(u=2\lfloor n/1024\rfloor\) and opposite collars of sufficiently large fixed radius as in row 1167. Write \(\nu\) for their joint adjoint law and \(\mu_A\) for one marginal. The selective estimates still needed on one permitted physical side are
\[
 \limsup_j\|\sqrt{d\nu}-\sqrt{d(\mu_A\otimes\mu_A)}\|_2<1/32,
          \qquad \liminf_j p_R>8/25 .
\]
The first can instead be approached through the observed neutral affinity in (15) and the separate charged branch condition of row 1161. Equation (22) allows the explicit reading probability to vanish. Equation (23) bounds a genuine shared reversal, but its lower bound also tends to zero. The positive deformation cost, the sharp full-adjoint rates (12) and (26), the deletion threshold (19)–(20), the disclosure formula (24) and the unanimity obstruction (28) locate the losses in the charged arguments. For the neutral arguments, (16) has an exponential-in-\(k\) limitation even for well aligned Wilson staples, and exact reconstruction allows either value of the retained affinity in the stated comparison. I have no estimate of the signed Wilson average at the two undisclosed boundaries, or of the distribution on the retained links, that reaches either strict margin.

RESULT — Row 1169. PROVED by hand, pending independent check. At the conditional one-loop slope a negative winding majority with all spacetime adjoints shared has probability \(\exp[-(1+o(1))\beta n^2]\). Reversing every line costs twice this exponent. With only the two collars shared the negative log is \(o(\beta n^2)\) even for unanimous reversal, although exact unanimity of either sign has vanishing probability. Equations (12) and (26) give the rates at every finite positive slope. Equations (19)–(20) give the deletion scale for losing a positive rate. Equation (22) gives a polynomial lower bound for the specified adjoint reading. Equation (15) permits logarithmically many spatial-link omissions in the neutral test under its two affinity hypotheses. OPEN. The order-one charged probability, the neutral upper bound, (W), and the Jaffe–Witten mass gap remain unresolved.
