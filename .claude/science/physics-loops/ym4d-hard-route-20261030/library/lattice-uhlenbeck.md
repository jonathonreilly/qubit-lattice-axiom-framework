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

## Consumer

The fill step of Prop 10 in `library/relative-density-bound.md`, on patches, for U and for the trial. There a := eta A, and the interpolation chi a + (1 - chi) a^tr has plaquette angle controlled by the terms in Step 3: ||d chi ^ a||_{l^2} <= C N^-1 ||a||_{l^2} <= C ||theta||, with chi at the scale N, and products in l^4.
