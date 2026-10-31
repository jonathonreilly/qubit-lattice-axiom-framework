# Ultralocal cluster expansion, with a self-contained proof

Credit: the ultralocal form, with localised functionals of independent fields, is the version J. Dimock attributes to T. Balaban in "The Renormalization Group According to Balaban I", arXiv:1108.1335, Appendix B, Theorem 27. The Mayer step below follows that appendix. The non-vanishing step is R. Dobrushin's inductive proof. The Mobius and maximum-principle route to the decay of H^# is written here so that no tree-graph identity is needed; it gives a weaker rate than Dimock's, as noted below. Status: proved here, labelled step by step; consumed by `parts/hard-core--independent.md`, Text 11.

## Setting

Let Lambda be a finite set of unit cubes. A polymer X is a connected union of cubes; |X| is its number of cubes and d(X) the length of a shortest tree joining them. Put c_d = 3^d, so that |X| <= c_d (1 + d(X)) when cubes are of unit side and neighbours are counted in the sup metric; and let K_0(a) be such that, for a >= a_0 = a_0(d), the sum over polymers X containing a given cube of exp(-a |X|) is at most exp(-a/2). (Lattice-animal count: the number of connected X of size n containing a given cube is at most nu^n, with nu = nu(d).)

Let mu be a product probability measure over cubes, mu = prod mu_c. Let H(X, Phi) be a function depending on Phi only in X, complex valued, measurable, with

    |H(X, Phi)| <= H_0 exp(-kappa |X|)   on the support of mu.                                                                     (1)

The hypothesis is in terms of |X|. A hypothesis in terms of d(X) with rate kappa' implies (1) with kappa = kappa' / c_d - o(1), up to a constant in H_0.

## Theorem

There are constants a_0, c_0 depending only on d such that, with a_1 := a_0 + log nu + 2 and rate r := kappa / 2 - 3 - a_1 - log 2, if r > 0 and H_0 <= c_0, then with Xi(Z) := int exp(sum_{X subset Z} H(X)) dmu,

    Xi(Z) != 0 for every set of cubes Z,     log Xi(Lambda) = sum_{Y} H^#(Y),

where H^#(Y) depends only on the H(X) with X subset Y, vanishes unless Y is connected, and

    |H^#(Y)| <= C H_0 exp(-r |Y|).                                                                                               (2)

## Proof

**Step 1: Mayer [as in Dimock].** Expanding the product of (e^{H(X)} - 1) + 1 over X subset Z and grouping into connected supports,

    exp(sum_{X subset Z} H(X)) = sum over families of disjoint connected Y_j subset Z of prod_j K(Y_j, Phi),
    K(Y, Phi) = sum over families {X_i} of distinct polymers, connected as a family, with union Y, of prod_i (e^{H(X_i)} - 1).

For H_0 <= log 2, |e^{H} - 1| <= 2 |H|. Since the family has union Y, sum_i |X_i| >= |Y|. Bound K by dropping connectivity and the union condition, and keeping half of the decay: with kappa >= 2 kappa_1,

    |K(Y, Phi)| <= exp(-kappa |Y| / 2) sum_n (1/n!) ( sum_{X subset Y} 2 H_0 exp(-kappa |X| / 2) )^n <= exp(-kappa |Y| / 2) ( exp(2 H_0 |Y|) - 1 ),

where sum_{X subset Y} exp(-kappa |X| / 2) <= |Y| when kappa / 2 >= a_0, by the animal count. Since 2 H_0 |Y| is at most 2 H_0 exp(|Y|), and exp(x) - 1 <= x exp(x),

    |K(Y, Phi)| <= 2 H_0 |Y| exp(2 H_0 |Y|) exp(-kappa |Y| / 2) <= 2 H_0 exp(-(kappa / 2 - 2) |Y|)   when H_0 <= 1/2,                  (3)

using |Y| exp(2 H_0 |Y|) <= exp(2 |Y|). Note (3) holds uniformly on the support of mu.

**Step 2: integrate.** Disjoint Y_j involve independent fields, so with z(Y) := int K(Y, Phi) dmu,

    Xi(Z) = sum over families of disjoint connected Y_j subset Z of prod_j z(Y_j),      |z(Y)| <= 2 H_0 exp(-(kappa / 2 - 2) |Y|).

So Xi is the partition function of a hard-core polymer gas.

**Step 3: non-vanishing with a complex scale (Dobrushin).** For complex t put z_t(Y) = z(Y) t^{|Y|}, Xi_t(Z) the gas with these activities. Let b := kappa / 2 - 2 - a_1. Claim: for |t| <= e^{b}, Xi_t(Z) != 0 and, for every cube c in Z,

    | log( Xi_t(Z) / Xi_t(Z \\ c) ) | <= a(c) := 1.                                                                                (4)

By construction and (3), for |t| <= e^b: |z_t(Y)| <= 2 H_0 exp(-a_1 |Y|). Induct on |Z|. Xi_t(Z) = Xi_t(Z \\ c) + sum_{Y containing c, Y subset Z} z_t(Y) Xi_t(Z \\ Y), so

    Xi_t(Z) / Xi_t(Z \\ c) = 1 + sum_{Y containing c, Y subset Z} z_t(Y) Xi_t(Z \\ Y) / Xi_t(Z \\ c).

Removing the cubes of Y \\ {c} from Z \\ c one at a time and applying (4) at each stage (for smaller sets), |Xi_t(Z \\ Y) / Xi_t(Z \\ c)| <= exp(|Y| - 1). So the sum is at most sum_{Y containing c} |z_t(Y)| exp(|Y|) <= 2 H_0 sum_{Y containing c} exp(-(a_1 - 1) |Y|), which is at most 1/2 for a_1 - 1 >= a_0 and c_0 small. Therefore Xi_t(Z) / Xi_t(Z \\ c) lies in the disc of radius 1/2 about 1, whose logarithm is at most log 2 <= 1. The base case Z empty has Xi = 1. This proves (4), and hence the claim, for all Z. In addition, the same display gives the sharper bound

    | log( Xi_t(Z) / Xi_t(Z \\ c) ) | <= 2 * (sum above) <= C H_0.                                                                  (5)

**Step 4: Mobius definition of H^#.** For a connected or disconnected set of cubes Y, put H^#(Y; t) := sum_{Z subset Y} (-1)^{|Y \\ Z|} log Xi_t(Z). This is analytic in |t| < e^b by Step 3. Mobius inversion gives log Xi_t(Lambda) = sum_{Y subset Lambda} H^#(Y; t). It depends only on the H(X) with X subset Y, since Xi_t(Z) depends only on H(X) for X subset Z.

If Y = Y_1 u Y_2 with no polymer meeting both, then log Xi_t(Z) = log Xi_t(Z n Y_1) + log Xi_t(Z n Y_2), and the alternating sum vanishes. So H^#(Y) = 0 for Y not connected.

**Step 5: decay by the maximum principle.** Telescoping (5) over the cubes of Z, |log Xi_t(Z)| <= C H_0 |Z| for |t| <= e^b. So |H^#(Y; t)| <= 2^{|Y|} C H_0 |Y| on |t| = e^b. Next, H^#(Y; t) vanishes at t = 0 to order at least |Y|. Indeed log Xi_t(Z) is a convergent power series in the z_t of its polymers, and in the alternating sum over Z subset Y every monomial whose polymers do not cover all of Y cancels, because such a monomial appears in log Xi_t(Z) for all Z containing its union with equal coefficient. A monomial covering Y has t-degree at least |Y|. By the Schwarz lemma applied to t -> H^#(Y; t) t^{-|Y|},

    |H^#(Y; 1)| <= exp(-b |Y|) sup_{|t| = e^b} |H^#(Y; t)| <= C H_0 |Y| 2^{|Y|} exp(-b |Y|) <= C' H_0 exp(-(b - log 2 - 1) |Y|).

Since b - log 2 - 1 = r, this is (2). []

## Variant for local functions without a sup bound

Steps 3 to 5 use only the gas form of Step 2 and the bound on z(Y). So if Xi(Z) = sum over families of disjoint connected Y_j subset Z of prod_j z(Y_j), with |z(Y)| <= 2 H_0 exp(-(kappa / 2 - 2) |Y|) for any reason, the conclusions (2) hold. This is what `parts/hard-core--independent.md`, Text 4.6, uses for cubes where H is not small and for hard cuts.

## Variant with activities in an anchored Banach algebra

Let G range over a commutative algebra of formal power series in some parameters, with a family of norms ||.||_A, one per set of cubes A, such that ||G H||_A <= ||G||_A ||H||_A, ||1||_A = 1, ||G||_{A'} <= ||G||_A for A in A', and ||G||_c <= exp(b_0 |Y|) ||G||_Y for a connected set Y and a cube c in it. Let H(X, Phi) take values there, measurably in Phi, with ||H(X, Phi)||_X <= H_0 exp(-kappa |X|), and read the integral over Phi coefficient by coefficient. Then the Theorem holds, with |.| replaced by ||.||_Y in (2), and with r replaced by r' := r - b_0 - log 2.

*Proof.* The Steps go through line by line with the norm in place of the modulus. Step 1: ||e^G - 1||_A <= e^{||G||_A} - 1, and ||H(X)||_Y <= ||H(X)||_X for X in Y. Step 2: a norm of an integral is at most the integral of the norm, coefficient by coefficient. Step 3: let R(Z, c) := Xi_t(Z) Xi_t(Z \\ c)^{-1}, by induction an invertible series, with ||R(Z, c) - 1||_c <= 1/2, so ||R(Z, c)^{-1}||_c <= 2. In the display of Step 3, Xi_t(Z \\ Y) Xi_t(Z \\ c)^{-1} is a product of |Y| - 1 factors R(Z_j, c_j)^{-1} with c_j in Y, so its norm at the anchor Y is at most 2^{|Y| - 1}, and then ||z_t(Y) Xi_t(Z \\ Y) Xi_t(Z \\ c)^{-1}||_c <= exp(b_0 |Y|) 2^{|Y|} ||z_t(Y)||_Y. So the sum over Y containing c is at most 1/2, provided a_1 is raised by b_0 + log 2, and that is what r' records. Steps 4 and 5: log R := sum_n (-1)^{n + 1} (R - 1)^n / n, so ||log R(Z, c)||_c <= C H_0, and log Xi_t(Z) is the sum of these along an order of Z, independent of the order, as formal series. At the anchor Y it is at most C H_0 |Z| for Z in Y. The Schwarz lemma holds for functions of t with values in a Banach space.  []

Sets that are not connected: if H(X) is given for arbitrary sets X of cubes, with a bound in the length tau(X) of the shortest tree joining X, choose for each X one connected Z(X) containing X with |Z(X)| = tau(X) + 1, and use H~(Z) := sum over X with Z(X) = Z of H(X). It depends on Phi in Z only, and sum_Z H~(Z) = sum_X H(X), and (1) holds for H~ with kappa lowered by log 2. Sparse sets need no separate treatment, **but they do need the bound in tau(X): a bound in |X| alone would not do**, which is the error found in the first use of this library in `parts/hard-core--independent.md`, Text 4.6.

## Remarks and limits

- The rate in (2) is a fixed fraction of kappa in |Y|, and so a smaller fraction of it in d(Y), namely by c_d. Dimock's tree-graph version keeps kappa - O(1) in d. If a consumer needs the sharper rate, it must rebuild that. In this project each level uses the expansion once, on freshly generated decay, so a loss of a fixed factor is paid by taking M large.
- Complex values of H are allowed, which is what analyticity in spectator fields needs: H^# is analytic in any parameter in which the H(X) are analytic with (1) holding uniformly.
- Unit cubes here stand for M-cubes in the application; mu is the white-noise measure with a cut, a product over cubes after grouping.

## Hostile check

(a) In Step 1 the sum over families bound uses "sum_{X subset Y}" with |Y| as a crude count. I checked the exponent: exp(2 H_0 |Y|) is harmless since H_0 <= 1/2 and it is absorbed in the rate. (b) In Step 3, the induction uses (4) for Z \\ c and for sets obtained from it by removing cubes, all smaller than Z. Correct. (c) The vanishing order in Step 5 uses the formal expansion of log Xi_t in the activities, valid for small t where it converges. It is enough to know the order at t = 0, since Xi_t is a polynomial in t on a finite lattice and log Xi_t is analytic near 0. (d) Constants are not optimised and a_0 is not explicit. Nothing consumes an explicit value.
