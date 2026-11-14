# Lattice Hardy-Littlewood-Sobolev and Gehring inequalities in d = 4

Credit: the sharp form is due to G. Hardy, J. Littlewood and S. Sobolev; the short proof through the maximal function is L. Hedberg's. Higher integrability from a reverse Holder inequality is F. Gehring's, with the local form of M. Giaquinta and G. Modica; the stopping argument below is the standard one, rewritten on the lattice. Status: proved here, step by step, including the pointwise bound on the gradient of the lattice Green's function (Lemma 2b). Consumed by `parts/hard-core--independent.md`, Lemma 4.5h. Written without reading any other file of `library/` that this attempt did not author.

## 1. Maximal function on Z^4

For finitely supported f >= 0 let Mf(x) := sup_{r >= 1} avg_{B(x,r)} f, with B(x, r) the sup-norm ball.

**Lemma 1.** ||Mf||_{l^2} <= C ||f||_{l^2}.

*Proof.* Let E_t := {Mf > t}. Each x in E_t has a ball with mass above t |B|. By the Vitali covering lemma, for finitely many balls, there are disjoint balls B_i among them with the 3 B_i covering E_t. So |E_t| <= C sum_i |B_i| <= (C / t) ||f||_1. Apply this to f_t := f 1[f > t / 2], using Mf <= M f_t + t / 2: |E_t| <= (2 C / t) sum_{f > t / 2} f. Then ||Mf||_2^2 = int_0^infinity 2 t |E_t| dt <= 4 C int_0^infinity sum_{f > t / 2} f dt = 8 C ||f||_2^2.  []

## 2. Hardy-Littlewood-Sobolev by Hedberg's argument

**Lemma 2.** If |K(x, z)| <= C_K (1 + |x - z|)^{-3}, then Kf(x) := sum_z K(x, z) f(z) obeys ||Kf||_{l^4} <= C C_K ||f||_{l^2}, and, for the transpose, ||K^T f||_{l^2} <= C C_K ||f||_{l^{4/3}}.

*Proof.* Replace f by |f|. For r >= 1, sum_{|w| < r} (1 + |w|)^{-3} |f(x - w)| <= C r Mf(x), by dyadic shells, and sum_{|w| >= r} (1 + |w|)^{-3} |f(x - w)| <= (sum_{|w| >= r} |w|^{-6})^{1/2} ||f||_2 <= C r^{-1} ||f||_2. An average over a ball of volume at least one is at most the l^2 norm, so Mf(x) <= ||f||_2, and r := (||f||_2 / Mf(x))^{1/2} is at least 1. So |Kf(x)| <= C C_K Mf(x)^{1/2} ||f||_2^{1/2}. Therefore ||Kf||_4^4 <= C ||f||_2^2 ||Mf||_2^2 <= C ||f||_2^4, by Lemma 1. The second statement is the dual.  []

*Consumer's kernel.* On a box of side N, the gauge of Lemma 3 of `library/lattice_sobolev_box_gauge.md` is a' = K * f on the reflected torus, with K the gradient of the lattice Green's function, up to the reflection images: a'_T = d^* Delta^{-1} d a_T, since a_T has no harmonic part.

**Lemma 2b.** On the torus of side 2 N in Z^4, let G_T(x) := |T|^{-1} sum_{p != 0} exp(i p x) / phat^2, the mean-zero Green's function. Then |grad G_T(x)| <= C (1 + |x|)^{-3} for |x| <= N, sup-norm distance on the torus, with C absolute.

*Proof.* grad_mu G_T(x) = |T|^{-1} sum_{p != 0} m(p) exp(i p x), m(p) := (exp(i p_mu) - 1) / phat^2. Here |m(p)| <= C / |p| on the Brillouin zone. Let Delta_i be the difference in p_i by the grid step h := pi / N, on the periodic grid of p. Then |Delta^alpha m(p)| <= C_alpha h^{|alpha|} |p|^{-1 - |alpha|}, for |p| >= C h |alpha|, since m is the restriction of a function that is smooth and periodic off 0, with derivatives of that order. Fix x != 0, |x| <= N, and i with |x_i| = |x|. Take a smooth cutoff chi at |p| of order 1 / |x|, equal to 1 on |p| <= 1 / |x| and to 0 on |p| >= 2 / |x|; these are above C h, since |x| <= N. The inner part has |T|^{-1} sum_{p != 0} chi |m| <= C int_{|p| <= 2 / |x|} |p|^{-1} dp <= C |x|^{-3}. For the outer part, summation by parts five times in p_i on the periodic grid: Delta_i applied to exp(i p x) gives the factor exp(i h x_i) - 1, of modulus 2 |sin(h x_i / 2)| >= (2 / pi) h |x|, since h |x_i| <= pi. The sum becomes at most |T|^{-1} sum_{|p| >= 1 / |x|} ((2 / pi) h |x|)^{-5} C h^5 |p|^{-6} <= C |x|^{-5} int_{|p| >= 1 / |x|} |p|^{-6} dp <= C |x|^{-5} |x|^2 = C |x|^{-3}. Leibniz on chi m gives terms of the same order, since derivatives of chi are of order |x| at |p| of order 1 / |x|. For |x| = O(1) the bound is the sum of |m| over the zone, which is bounded.  []

Lemma 2 applies to the kernel on the torus, by the same proof with balls on the torus, for |x - z| <= N, and K has no mass beyond that distance on the torus.

## 3. Gehring on the lattice

Let Q_s be the adapted ball of radius s R about a fixed centre, within a region that is a finite union of cells of side N with lattice faces. *Adapted balls.* For r <= N / 4, B(x, r) is the union of the cubes of side r / 4 that meet the intrinsic ball of radius r about x, in a grid aligned with the faces nearest to x; for larger r it is one of a finite list of unions of cells and parts of cells. Such a B is comparable to the intrinsic ball, it has volume comparable to r^4, doubling holds with a constant from the finite list, and it is a union of boundedly many cubes joined by faces. **A sup-norm ball cut by the region will not do:** at a re-entrant corner it can have a thin tentacle, joined to the rest along its short side, with a Poincare constant that blows up with the aspect ratio. The intrinsic distance is what the covering arguments below use. Let g, h >= 0 and 1 <= q < 2.

**Lemma 3.** Suppose that for all balls with B(x, 2 r) in Q_1, r >= 1,

    avg_{B(x,r)} g^2 <= b ( avg_{B(x,2r)} g^q )^{2/q} + avg_{B(x,2r)} h^2.

Then there are eta > 0, C depending only on b, q and the volume-comparison constant with

    ( avg_{Q_{1/2}} g^{2 + eta} )^{1 / (2 + eta)} <= C ( avg_{Q_1} g^2 )^{1/2} + C ( avg_{Q_1} h^{2 + eta} )^{1 / (2 + eta)}.

*Proof.* Let 1/2 <= s < s' <= 1, rho := (s' - s) R. Put t_0^2 := A (R / rho)^4 avg_{Q_1} g^2, with A large. Let t >= t_0 and x in Q_s with g(x) > t. Then avg_{B(x,1)} g^2 >= c t^2, and for r >= rho / 20 the average is below c t^2, by the choice of t_0. So there is a largest r_x in [1, rho / 20) with avg_{B(x, r_x)} g^2 >= c t^2. The Vitali lemma gives disjoint balls 2 B_i, B_i = B(x_i, r_i), with the 10 B_i covering E_s(t) := Q_s n {g > t}. Since 10 r_i > r_i, avg_{10 B_i} g^2 <= c t^2 or the bound at scale rho / 20 applies, so

    int_{E_s(t)} g^2 <= sum_i int_{10 B_i} g^2 <= C t^2 sum_i |B_i|.

By the hypothesis on B_i, either avg_{2 B_i} h^2 >= c t^2 / 2, or avg_{2 B_i} g^q >= (2 delta t)^q, with delta depending only on b and c. In the second case, splitting g at the level delta t gives |B_i| t^q <= C int_{2 B_i n {g > delta t}} g^q. In the first case, in the same way, |B_i| t^2 <= C int_{2 B_i n {h > delta t}} h^2. Since the 2 B_i are disjoint and in Q_{s'},

    int_{Q_s n {g > t}} g^2 <= C t^{2 - q} int_{Q_{s'} n {g > delta t}} g^q + C int_{Q_{s'} n {h > delta t}} h^2.

Multiply by t^{eta - 1} and integrate over t >= t_0. The left side is at least (1 / eta) ( int_{Q_s} g^{2 + eta} - t_0^eta int_{Q_s} g^2 ). In the first term on the right, int_0^{g / delta} t^{1 - q + eta} dt <= C g^{2 - q + eta}, with C uniform for eta <= 1, since 2 - q > 0. So with Phi(s) := int_{Q_s} g^{2 + eta},

    Phi(s) <= C_1 eta Phi(s') + t_0^eta int_{Q_1} g^2 + C int_{Q_1} h^{2 + eta},

and all of this is finite, on a finite lattice. Take eta with C_1 eta <= 1/2. The middle term is A' ((s' - s)^{-4 eta}) (avg_{Q_1} g^2)^{eta / 2} int_{Q_1} g^2. Iterate over s_j := 1/2 + (1 - 2^{-j}) / 2, with s_{j+1} - s_j = 2^{-j-2}: Phi(1/2) <= sum_j 2^{-j} ( A'' 2^{4 eta j} X + Y ), with X := (avg_{Q_1} g^2)^{eta / 2} int_{Q_1} g^2 and Y := C int_{Q_1} h^{2 + eta}. The series converges for 4 eta < 1, and this is the claim after dividing by the volume, since 2^{-j} Phi(s_j) -> 0.  []

## 4. Consequence used

**Corollary 4.** If in addition avg_{Q_1} g^2 <= G^2 and h <= G, then for any subset S of Q_{1/2}, int_S g^2 <= C |Q_1| G^2 ( |S| / |Q_1| )^{eta / (2 + eta)}, by Holder. In particular a ball of radius rho R, or a layer of thickness rho R, carries at most a fraction C rho^{a} of the energy, a > 0. []

## Hostile check

(a) At scale r = 1 the hypothesis is a trivial bound, since g^2 at a point is at most a constant times (avg g^q)^{2/q} at unit scale, so there is no lattice problem at the bottom of the stopping argument. (b) The region may have re-entrant corners: only adapted balls, the Vitali covering for the intrinsic metric, and volume comparison are used. A region made of cells with a thin connection could violate volume comparison at scales near the cell size, but only up to a constant depending on the finite list of local patterns. (c) The consumer must supply the reverse Holder inequality, including up to a free boundary, from Caccioppoli and Lemma 2; the potential on a ball intersected with a pattern comes from Lemma 7 of `library/lattice_sobolev_box_gauge.md` only at cell scales, and at smaller scales the ball meets a bounded number of boxes, and Lemma 6 there applies. (d) The exponent eta is not explicit, and nothing consumes an explicit value.
