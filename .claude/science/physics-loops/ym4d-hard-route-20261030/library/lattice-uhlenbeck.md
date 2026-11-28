# Lattice Uhlenbeck gauge at small energy, uniform in the lattice spacing

Producer: `parts/hard-core--mapped.md`, for the fill step of Props 10, 10' in `library/relative-density-bound.md`. Status: proved here, with the Sobolev inequality (S) taken from `library/lattice_sobolev_box_gauge.md`. Not reviewed.

Credit: the statement is the lattice form of Uhlenbeck's gauge theorem (1982) at critical integrability. Her proof is a continuity method. The growth one layer at a time, the exact reflection identity on the lattice, and the gauge flow below are mine. Nothing here uses the account.

## Setting

P is a lattice box with sites x, 0 <= x_mu <= n_mu, with n_mu <= 2 n_nu for all mu, nu, and d = 4. Work in lattice units; all norms below are scale invariant in d = 4 (||grad a||^2_{l^2} = ||grad A||^2_{L^2} for a = eta A). U is an SU(2) bond field on P. Write U(b) = e^{i a(b)}, |a(b)| < pi, a in su(2) with the norm in which |log| is the group distance. theta_p := log of the plaquette holonomy, based at a corner of p, and ||theta||^2 := sum_p |theta_p|^2. This is gauge invariant.

For a bond field a on P: (d a)_p := a_mu(x) + a_nu(x + e_mu) - a_mu(x + e_nu) - a_nu(x); (delta a)(x) := sum_mu (a_mu(x) - a_mu(x - e_mu)), with bonds outside P read as 0;

    ||grad a||^2 := sum over parallel neighbouring bonds in P of |a(b) - a(b')|^2  +  sum_mu sum over normal bonds b at the two faces of P, in direction mu, of |a(b)|^2.

The second sum is the natural boundary term.

## Lemma U

There are epsilon_0, C_U > 0, absolute, such that if ||theta||_P <= epsilon_0 there is a gauge on P with

    delta a = 0,    ||grad a||^2 <= 4 ||theta||^2,    ||a||_{l^4(P)} + N^-1 ||a||_{l^2(P)} <= C_U ||theta||,    sup |a| <= C_U ||theta||,

N := max n_mu, with no dependence on N.

## Step 1. Exact identity by reflection

For any bond field a on P, ||d a||^2 + ||delta a||^2 = ||grad a||^2.

*Proof.* Reflect in the mid-planes x_mu = -1/2 and x_mu = n_mu + 1/2, as an invariant 1-form: a_nu is even in x_mu for nu != mu, a_mu(x) = -a_mu(r x - e_mu), and the bonds crossing a mid-plane carry 0, which is forced by the symmetry. This gives a field on the torus with periods 2 (n_mu + 1). On the torus ||d a||^2 + ||delta a||^2 = ||grad a||^2 by Fourier: at each q, |q-hat ^ a-hat|^2 + |q-hat . a-hat|^2 = |q-hat|^2 |a-hat|^2, with q-hat_mu := e^{i q_mu} - 1. A plaquette with one crossing bond has d a = 0 by the symmetry: a_nu(0) - a_nu(-1) = 0. So the torus sum of |d a|^2 is 2^4 times the sum over P. delta a at a site of P is the delta a of the box, since the crossing bond carries 0. A gradient across a mid-plane vanishes for nu != mu, and for the normal component it is |a_mu(boundary bond)|: this is the natural boundary term. QED

## Step 2. Sobolev on the reflected torus

(S) For f on a torus with comparable periods about N, and zero mean: ||f||_{l^2} <= C N ||grad f||_{l^2} and ||f||_{l^4} <= C ||grad f||_{l^2}.

The first is Fourier. The second is Lemma 1 and Corollary 2 of `library/lattice_sobolev_box_gauge.md`, which is written line by line there, after Gagliardo, Nirenberg, Loomis and Whitney. That note was written by another attempt in this loop, and I read only its Section 1 and the statement of its Lemma 3, for this inequality. Its periods are comparable, as here.

Consequences. Each component a_mu is odd under the reflection in its own direction, so it has zero mean on the torus. Hence ||a||_{l^4(P)} <= C_S ||grad a||, and N^-1 ||a||_{l^2(P)} <= C_S ||grad a||. Trivially sup |a| <= ||a||_{l^4}. For a site function w, even under all reflections, with delta grad w = f: ||grad grad w||_{l^2} = ||f||_{l^2}, exactly, by Fourier on the torus (the case of d = 0 in Step 1), and each grad_nu w is odd in nu, so ||grad w||_{l^4} <= C_S ||f||_{l^2}. So w exists whenever the mean of f vanishes, and delta a always has mean zero.

## Step 3. A priori bound

If sup |a| <= 1, then |theta_p - (d a)_p| <= C sum_{b in p} |a(b)|^2, by Baker-Campbell-Hausdorff for four factors. So ||d a|| <= ||theta|| + C ||a||^2_{l^4} <= ||theta|| + C_1 ||grad a||^2. With Step 1, for X := ||grad a||:

    X^2 <= (||theta|| + C_1 X^2)^2 + ||delta a||^2.     (A)

## Step 4. Gauge flow

Let a(t) follow an infinitesimal gauge transformation by iw(t), with delta grad w = delta a: U(b) -> e^{i s w(x)} U(b) e^{-i s w(x + e)}. Writing w(x + e) = w(x) + grad w, the exact derivative is

    d a/dt = [w(x), a] - J(a) grad w,        |J(a) - 1| <= C |a|, for |a| <= 1,

the first term a rotation, J the Jacobian of the group logarithm. theta is gauge covariant, so ||theta|| is constant. Then with [. , .] the bracket scaled to be antisymmetric for the norm:

    d/dt delta a = [w, delta a] - delta a + (sum_mu [grad_mu w, a_mu]) - delta ((J - 1) grad w).

The first term is orthogonal to delta a. So

    (1/2) d/dt ||delta a||^2 <= - ||delta a||^2 + ||delta a|| ( ||grad w||_{l^4} ||a||_{l^4} + ||delta((J - 1) grad w)||_{l^2} ).

With W := (J - 1) grad w: |delta W| <= C ( |a| |grad grad w| + |grad a| |grad w| ), read at neighbouring bonds. So ||delta W||_{l^2} <= C ( sup |a| ||grad grad w||_{l^2} + ||grad a||_{l^4} ||grad w||_{l^4} ) <= C ( ||a||_{l^4} + ||grad a||_{l^2} ) ||delta a||. The last step uses ||.||_{l^4} <= ||.||_{l^2} on a lattice, which costs nothing here and is where the exponential's correction is seen to be of higher order. So, as long as X is at most a small absolute X_0:

    d/dt ||delta a||^2 <= - ||delta a||^2.     (D)

From (A) and (D), by continuity in t: if X(0) <= X_0/2 and ||theta|| + ||delta a(0)|| <= X_0/8, with C_1 X_0 <= 1/8, then X(t) <= 2 (||theta|| + ||delta a(0)||) for all t, and ||delta a(t)|| -> 0 exponentially. Since ||d a/dt||_{l^2} is at most C ||grad w||_{l^2} + (rotation), and the rotation preserves |a(b)|, a(t) converges along a subsequence on the finite-dimensional compact set. Its limit has delta a = 0, the same ||theta||, and by (A) X <= 2 ||theta||, given C_1 X_0 small.

## Step 5. Growth

Order boxes P_0, P_1, ..., each adding one layer of sites in one direction, sides remaining comparable, from a single site to P. The claim for P_m: there is a gauge with delta a = 0, X <= 2 ||theta||_{P_m}.

Base: no bonds. Step: given a on P_m, extend the gauge to the new layer by making each new normal bond trivial. A new tangential bond then satisfies |a^new_nu(x) - a_nu(x - e_mu)| <= C |theta_p|, for the plaquette p between them, since sup |a| is small and the two normal sides are, respectively, trivial. So on P_{m+1}:

- normal components: the new normal bonds carry 0, and the old boundary term |a_mu|^2 at the former face is now the gradient to the new 0. The new face has boundary term 0. No change.
- tangential components: the gradient across the new layer is at most C |theta_p|. The gradient within the new layer is at most the gradient within the old face layer plus C |theta| on the neighbouring plaquettes.
- delta a: at the old face sites it is unchanged, since the new bond carries 0. On the new layer, delta a = sum_nu grad_nu a^new_nu, at most the tangential divergence at the old face plus C |theta|; and by delta a = 0 at the old face, that divergence equals a term in a_mu, at most the old boundary term.

So X(0)^2 <= 3 ||grad a||^2_{P_m} + C ||theta||^2 <= C_2 ||theta||^2_{P_{m+1}}, and ||delta a(0)|| <= C_2 ||theta||_{P_{m+1}}. For epsilon_0 small in terms of C_2, X_0, Step 4 applies and gives the claim on P_{m+1}. *The bound resets at each layer to 2 ||theta||, because (A) has no memory of the path, so nothing accumulates over the N layers.* QED

## Hostile check

1. *Does the flow leave the chart?* It stays in sup |a| <= C X_0 < 1, so log is smooth and there is no cut locus.
2. *Unbounded w.* w itself has no sup bound in d = 4; it enters only through a rotation, which is an isometry, and through grad w, in l^4. Checked in (D): the term [w, delta a] drops by antisymmetry. The argument is at the infinitesimal level for this reason. A Newton step with a finite e^{i w} would need sup |w| small, and I first tried it: Ad_w delta a does not cancel delta a when w is large. That route is dropped.
3. *Patching by L-adic induction,* tried before this: transitions lie only in W^{1,4} in d = 4, with no sup control. Dropped.
4. *Is the lattice term really harmless?* ||grad a||_{l^4} <= ||grad a||_{l^2} is true on a lattice with no constant. In continuum variables this term carries a positive power of eta. No uniformity in eta is lost.
5. *Comparable sides* are needed only for (S). The steps keep the sides within a factor 2.
6. *Non-smooth points of the problem.* None: finite-dimensional ODE with smooth right side on the chart. w is defined up to a constant, which is fixed by mean zero; a constant only rotates a.
7. *What is not computed.* Step 5's list is at the level of each term, with constants not computed.

## Lemma F (fill across a shell). Derived; not reviewed.

Let Q_r be the cube of radius r about a point, in lattice units, and S := Q_{2r} \ Q_r. There are epsilon_1, C_f > 0, absolute, such that if ||theta(U)||_{L^2(S)} <= epsilon_1, there is a field U-hat on the bonds of Q_{2r} with U-hat = U off Q_{(7/4) r}, flat on Q_r, and ||theta(U-hat)||^2_{Q_{2r}} <= C_f ||theta(U)||^2_S.

*Why not simply interpolate patch by patch.* Prop 9' Step A' of `library/relative-density-bound.md` replaced a field by a target on one patch after another, and claimed that the final band is a gauge transform of the target, "up to overlaps' constants". That is wrong as written: a later patch's interpolation annulus overwrites part of an earlier patch's core, with a field between two different gauges, so the band is not exactly a gauge transform of anything, and nothing closes. Below, a gauge on each patch is chosen so that the earlier flat part stays exactly flat.

*Proof.* Cover the band S' := Q_{(7/4) r} \ Q_{(5/4) r} by boxes P_1, ..., P_n in S, of side comparable to r, n absolute, in an order for which O_j := P_j cap (cores of P_1, ..., P_{j-1}) is box-like for j < n, and O_n is a frame: P_n minus an inner box B. Let core(P_j) be the middle part of P_j. Inductively the current field F_{j-1} equals U outside the patches used, is flat on the union of cores so far, and ||theta(F_{j-1})||^2_{P_j} <= C_{j-1} ||theta(U)||^2_S.

*What the interpolation needs.* For a field e^{i a'} on P_j and chi at scale r: theta(e^{i chi a'}) = chi (d a') + d chi ^ a' + O(|a'|^2), and by Step 3, chi d a' = chi (theta - O(|a'|^2)). So ||theta(e^{i chi a'})||_{l^2} <= ||theta||_{l^2} + C r^-1 ||a'||_{l^2} + C ||a'||^2_{l^4}, and r^-1 ||a'||_{l^2} <= C ||a'||_{l^4} on a patch of side r. *Only ||a'||_{l^4} and sup |a'| <= ||a'||_{l^4} are read, no second difference of a gauge.* But then ||theta||-small needs ||a'||_{l^4} <= C ||theta||, which Lemma U supplies in its own gauge, and a gauge change costs only ||grad t||_{l^4}.

Step j, j < n. Lemma U gives a on P_j, Landau, ||a||_{l^4} <= C ||theta||. On O_j the field is flat and O_j is simply connected, so e^{i a(b)} = t(x) t(x + e)^-1 for a single-valued t on sites of O_j, and |grad t| = |a| in the group distance, exactly. So ||grad t||_{l^4(O_j)} = ||a||_{l^4(O_j)}. Extend t to P_j by reflection across the faces of O_j: group valued, ||grad t-tilde||_{l^4(P_j)} <= C ||a||_{l^4}. A kink at the faces does no harm, since only first differences are read. Put a' := the gauge transform of a by t-tilde^-1. Then a' = 0 on O_j, and ||a'||_{l^4} <= C ||theta||, as Ad is an isometry. In this gauge put e^{i chi a'}, chi = 0 on the core, chi = 1 near the boundary of P_j. So ||theta(e^{i chi a'})||^2_{P_j} <= C_e ||theta(F_{j-1})||^2_{P_j}, with C_e absolute, and the field is unchanged on O_j, and flat on O_j and on the core of P_j.

*The covering, displayed (derived).* In units of r, the band is {5/4 <= |x|_inf <= 7/4}. Take the 8 patches P(i, sigma) := { sigma x_i in [5/4, 7/4], |x_l| <= 7/4 for l != i }, in the order (1,+), (2,+), (3,+), (4,+), (4,-), (3,-), (2,-), (1,-), with cores slightly smaller, overlapping so that they cover a shell. O_j is P_j cut with the earlier cores. For (2,+): a box. For (3,+), (4,+): a union of boxes meeting along a face, contractible. For (4,-), (3,-), (2,-): P_j minus a box reaching one face of P_j, in the three coordinates other than x_i: a cup, contractible. For the last, (1,-): P_j minus a box reaching two opposite faces, in the x_1 direction: (shell of a 3-cube) x interval, homotopic to S^2, so simply connected. So t is single-valued on every O_j. Each O_j is one of finitely many shapes, up to scale, a finite union of boxes, so the reflection extension has an absolute constant.

*Lemma M (lattice Morrey on a 3-dimensional surface). Proved here.* Let Sigma be a finite union of at most n_0 lattice cuboids of dimension 3 and sides comparable to N, connected through shared faces. For f on the sites of Sigma with values in a metric space embedded isometrically up to a factor 2 in R^4 (as SU(2) is, by its chord distance), osc_Sigma f <= C(n_0) N^{1/4} ||grad f||_{l^4(Sigma)}. *Proof.* On one cuboid Q, scalar f first. L^1 Poincare on a cube q of side l: sum_{z in q} |f(z) - avg_q f| <= |q|^-1 sum_{z, z'} sum_{b in path(z, z')} |grad_b f| <= C l sum_{b in q} |grad_b f|, with axis-ordered paths, as each bond lies on at most C l^4 of them. For x in Q take cubes q_0 = {x}, q_1, ..., q_m = Q (a cuboid of comparable sides), with q_i of side 2^i containing x. Then |avg_{q_i} f - avg_{q_{i+1}} f| <= |q_i|^-1 sum_{z in q_{i+1}} |f(z) - avg_{q_{i+1}} f| <= C 2^{-2 i} sum_{q_{i+1}} |grad f| <= C 2^{-2 i} (2^{3 i})^{3/4} ||grad f||_{l^4} = C 2^{i/4} ||grad f||_{l^4}. Summing over i: |f(x) - avg_Q f| <= C N^{1/4} ||grad f||_{l^4(Q)}. For a metric-valued f, apply this to each coordinate. Neighbouring cuboids share a face, so their averages differ by at most twice the bound; a chain has at most n_0 of them. QED

*A correction to "frame".* In d = 4 the band is S^3 x I. Decomposing it by patches, the last patch is P_n = D^3 x I, and it meets the earlier cores in O_n = (D^3 \ D'^3) x I', homotopic to S^2. So B := D'^3 x I' is an inner box in the three directions of D^3 only, and it may reach two faces of P_n. Sigma_rho := (boundary of D_rho^3) x I', a union of cuboids as in Lemma M, simply connected as O_n is. Radial projection is in the D^3 coordinates. The counts below are unchanged, as there are about N concentric Sigma_rho in the frame.

Step n. O_n is a frame, and t is defined on it, with ||grad t||_{l^4(frame)} <= C ||theta||. Extend t into B. By pigeonhole over the concentric box boundaries in the frame, of which there are about N, there is a 3-dimensional lattice surface Sigma with ||grad t||^4_{l^4(Sigma)} <= C N^-1 ||grad t||^4_{l^4(frame)}. The lattice Morrey inequality on Sigma, of diameter about N, in dimension 3 with exponent 4, gives osc_Sigma t <= C N^{1/4} ||grad t||_{l^4(Sigma)} <= C ||grad t||_{l^4(frame)} <= C epsilon_1. So t = t-bar e^{i w} on Sigma, with sup |w| small. Inside Sigma put t-tilde := t-bar exp(i psi w o pi), with pi the radial projection onto Sigma, and psi a cutoff at scale r equal to 1 at Sigma, and 0 well inside. Then ||grad t-tilde||_{l^4} <= C (||grad w||_{l^4(Sigma)} N^{1/4} + r^-1 N^{1/4 + 3/4} ... ), that is, in scale-invariant counts, at most C (N^{1/4} ||grad t||_{l^4(Sigma)} + sup |w|) <= C ||grad t||_{l^4(frame)}. Here I use the exact bound: sup|w| is itself bounded by a constant times ||grad t||_{l^4(frame)}, not merely small. The rest of the step is as for j < n.

End. The band S'' := the union of cores contains a shell, the field on it is flat, and the shell is simply connected in d = 4. So it is a pure gauge there: the field equals t_0 trivial t_0^-1 for a single-valued t_0 on sites of the shell. On a lattice t_0 extends to all sites of Q_r arbitrarily. Put U-hat := the gauge transform by t_0 of the trivial field on Q_r. No degree obstruction arises on a lattice, and none is needed. Then ||theta(U-hat)||^2 <= C_e^n ||theta(U)||^2_S on Q_{2r}, and U-hat = U off Q_{(7/4) r}. QED

*Status of parts.* |grad t| = |a| is exact. The Morrey inequality on a 3-dimensional lattice surface is Lemma M above, proved. The interior extension's count: ||grad (w o pi)||^4_{l^4} <= C N ||grad w||^4_{l^4(Sigma)}, as each fibre of pi has about N sites, and the pigeonhole gives N ||grad t||^4_{l^4(Sigma)} <= C ||grad t||^4_{l^4(frame)}; the cutoff term is N^-4 sup |w|^4 N^4, with sup |w| <= C ||grad t||_{l^4(frame)} from Lemma M. An earlier version of this proof asked second differences of t, which an even reflection would not have preserved; the interpolation does not read them. The bounds are at the level of each term, with constants not computed.

*Consumer.* Prop 10, with target flat in place of the trial. Near a cell of Z the trial's energy is negligible, so nothing is lost, and the bump carries the parent's data. At a dropped box the bump, of amplitude about f, is what restores the parent's flux, at a cost C f^2 per box, included in K.

## Lemma RF (relative fill across a band of any shape). Derived 2026-10-31, level of each term; not reviewed.

*Why.* Lemma F fills a cube, since its last step reads that a shell is simply connected. A long dense cluster has a band with non-contractible loops, and these may carry holonomy (gate `gates/theorem-z-repaired-60036ba4d.md`, D1). If the target has the same parents as the field on the band, the holonomy is not an obstruction: parents read it, and the target carries the same value.

*Statement.* Let S be a union of level-(k+1) blocks, side L in level-k cells, separating Omega_in from Omega_out, at least 8 blocks wide. Let U_1, U_2 be fine fields on S with the same level-(k+1) data V on the bonds read in S, U_1 possibly with excluded lines, a fraction f per parent with f (log L)^{3/4} <= 1 (a non-dense box has f <= C (m_* S_*/L)^3), and energy at most eps_1^2 on each cube of 4 blocks. Then there is a field U-hat on S, equal to U_1 near Omega_out, gauge equivalent to U_2 near Omega_in by a site function, and

    || theta(U-hat) ||^2_S <= C_f ( || theta(U_1) ||^2_S + || theta(U_2) ||^2_S ),

with eps_1, C_f absolute, free of L, of the size of S and of its topology. Its level-(k+1) data differ from V on bonds in S by s(b'), |s(b')| <= C (|| theta(U_1) ||_{N(b')} + || theta(U_2) ||_{N(b')}), once the energies are small in L, which T small in L gives.

*Proof.* Cover S by patches P, cubes of 4 blocks, cores the middle blocks, with n_c colours: patches of one colour are disjoint and n_c is absolute. Process colour by colour, not by a sweep: a sweep would have depth the length of S and the constant would grow with it. Let F be the current field, equal to U_1 off the processed patches and to U_2^h on the cores W so far, h a site function on W.

*Step 1: gauges.* On P take Lemma U gauges: F^{g_F} = e^{i a_F}, and for the target U_2^{h-hat}, h-hat any extension of h to P, g_2 with a_2. Then t := g_F g_2^-1 is single-valued on the sites of P, **by construction and with no topological input**. On O := P cap W the two fields coincide, so ||grad t||_{l^4(O)} <= ||a_F||_{l^4} + ||a_2||_{l^4} <= C eps_P, with eps_P^2 the energy of F and of the target on P. O is a union of whole blocks, one of finitely many patterns; it may have several components, or be an annulus. On P off O there is no bound on grad t: F may be any gauge transform of U_2 there.

*Step 2: the constant, from the parents.* This replaces simple connectivity. For a gauge g with field e^{i a}, let c-bar_g(y) be the log-average over x in B(y) of the contour from the centre y to x, and G(y) := g(y) e^{i c-bar_g(y)}. The contours enter a parent bond only through c-bar at its two ends, so |log V^G(b')| <= avg over lines of the sum of |a| along the line, plus second order, <= L^-3 (L^4)^{3/4} ||a||_{l^4} + C (log L)^{3/2} eps^2 <= C eps_P. No log L at first order: |c-bar| itself can be (log L)^{3/4} eps, by Hoelder on the contours' weights, which fall as r^-3, and it has been absorbed in G. Excluded lines: a bond's surviving average differs from c-bar by at most f (log L)^{3/4} eps, which is why f is small in the hypothesis and not merely below 1/2. The same V is read in the two frames, so tau(y) := G_F(y) G_2(y)^-1 has |log tau(y) tau(y')^-1| <= C eps_P on adjacent centres, so every tau(y), y in P, is within C eps_P of one tau-bar. (If F has some blocks with V^h in place of V, h is near 1 at centres by the same bound one colour earlier. The depth is n_c, so no accumulation along S.)

*Step 3: t on O is near tau-bar.* On a block B(y) in O, F is the target, so tau(y) is the average of t over B(y) up to C ||grad t||_{l^4(B)}, by Poincare in L^1, which is scale invariant at this exponent. So ||t - tau-bar||_{l^4(O)}/L <= C eps_P, on every component of O.

*Step 4: extension.* Extend t by reflection across the faces of O, up to a band of width about L around O. By pigeonhole on about L concentric 3-dimensional surfaces in that band, and Lemma M, there is a surface Sigma with osc_Sigma t <= C eps_P, and by Step 3 tau-bar^-1 t = e^{i w} on Sigma, sup |w| <= C eps_P. Past Sigma put t-tilde := tau-bar exp(i psi w o pi), radial projection, cut-off at scale L, as in Step n of Lemma F. So t-tilde is group valued on P, equals t on O, equals tau-bar on the rest of P, and ||grad t-tilde||_{l^4(P)} <= C eps_P.

*Step 5: interpolation.* g' := t-tilde^-1 g_F. Then F^{g'} = e^{i a'}, ||a'||_{l^4} <= C eps_P, and on O, g' = g_2 and a' = a_2 exactly. Put e^{i (chi a' + (1 - chi) a_2)}, chi = 1 near the boundary of P and chi = 0 on the core, and transform back by g'^-1. Near the boundary of P this is F. On O it is the target. On the rest of the core it is the target up to the site function g_2 g'^-1, which extends h. By the count in "What the interpolation needs" above, its energy on P is at most C_e eps_P^2. Gauge transformations by site functions preserve every plaquette, so **no bound on h is read for the energy**.

*End.* After n_c colours the cores contain a band separating Omega_in from Omega_out, and the field there is U_2^h. Take h-bar := h on W, 1 near Omega_out, any value between, and transform: this is U-hat. For parents on S: by Steps 2 and 5 the field on each patch is small in the frames G, in which V is small, so with h-bar chosen at centres by those frames the mismatch is as stated. QED at this level; constants not computed.

*What it reads.* Lemma U on patches, Lemma M, the kernel's log-average with lines through hulls excluded; that closed-loop holonomies in a patch have small angle, by energy at most C K T^2 and T small in L. *Hostile.* (1) *Is a closing loop really no problem?* Take U_1 a thin sheet with holonomy -1 and V flat at parents around it. That is not an allowed pair: V reads the holonomy on the parents around the sheet, so a class V there carries flux pi through a disc of at least pi/T_2 level-(k+1) plaquettes, and the trial has it. If the disc does not exist, V is not class and the band lies in a tube, where the target is a fill and U_1 is not used. (2) *Two components of O whose h differ:* h is near 1 at centres on both, in the frames G, as parents are read at bounded distance only. (3) *C_f against K:* C_f is the constant J and K are chosen after, as in Prop 10, and it does not read L. Second-order terms with log L are small by T small in L, which comes after. (4) *Lemma F is not superseded for a cube at a non-dense cell:* a flat target has zero energy on the core, and there the parents do not agree on the shell's scale. The target's energy on a small cube is small in either case.

## Consumer

The fill step of Prop 10 in `library/relative-density-bound.md`, on patches, for U and for the trial. There a := eta A, and the interpolation chi a + (1 - chi) a^tr has plaquette angle controlled by the terms in Step 3: ||d chi ^ a||_{l^2} <= C N^-1 ||a||_{l^2} <= C ||theta||, with chi at the scale N, and products in l^4.
