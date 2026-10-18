# First native aligned-column winding coefficient

Focused independent check of the appended winding section in `/tmp/neutral_whole_column_root.md`. The result is correct as the first off-diagonal coefficient of the native N=0 effective Hamiltonian in a word-derived canonical/local perturbative gauge, at fixed even periodic longitudinal length L>4.

## 1. Exhaustion of order-L words

Every transverse native insertion flips precisely two spins in one z plane. Between distinct N=0 configurations, each changed column must be flipped at every one of its L sites. The parity of the number of flips in each z plane is even, so at least two columns change. The required Hamming distance is therefore at least 2L, giving an insertion-count lower bound L.

At equality there is no repeated flip: all 2L spin flips are used on the final changed sites. Hence exactly two columns change, and each insertion must join those two columns within its own z layer. They must be transverse nearest neighbors, and the same transverse bond is used once at each z. No mixed-edge path, spectator flip, non-neighbor pair, or four-column endpoint can occur at this order. The argument applies to arbitrary aligned-column backgrounds, not only all-up.

Every proper nonempty subset of these L insertions leaves longitudinal walls. There is no intermediate return to N=0. Folded/subtraction terms contributing to an off-diagonal matrix element at order L would require a lower-order off-diagonal N=0 factor, which the same counting excludes. Lower-order diagonal terms do not change this conclusion. This reasoning is for a perturbative construction built from the native insertions; an arbitrary nonlocal change of basis within N=0 could of course change the matrix representation and is not constrained by the word-count argument.

## 2. Costs and signs

A proper subset S of flipped rungs has c(S) cyclic clusters. Each cluster has two boundaries in each of the two columns, hence four broken z bonds. With cost 2J per broken bond the excitation cost is 8J c(S). Every resolvent denominator is consequently -1/[8J c(S)].

For XX the Hamiltonian amplitude is -J lambda at each rung. For YY, on original aligned-column spins s_i,s_j in {+1,-1}, the Hamiltonian amplitude is +J lambda s_i s_j. Since no rung is revisited, all YY phases refer to those original spins; the total product is (J lambda)^L(s_i s_j)^L. At even L this is positive and equals the XX product. The L-1 negative denominators leave an overall minus sign in both directions. All paths have the same sign, so no cancellation is possible.

The result is

    H_eff,offdiag^(L) = -gamma_L sum_(nearest xy i,j) Xbar_i Xbar_j,
    gamma_L = J lambda^L binom(2L-2,L-1)/8^(L-1).

The transverse periodic graph should count each physical nearest-neighbor bond once; the stated L>4 cube avoids short-period duplicate-edge conventions.

## 3. Exact all-length path sum

For proper S define F(empty)=1 and F(S)=sum_(i in S) F(S\{i})/c(S). If its cluster lengths are l_1,...,l_c, then

    F(S)=product_a Catalan(l_a).

To prove this, removing one site from a cluster of length l splits it into lengths u and l-1-u. Summing over the removed position gives sum_u Catalan(u)Catalan(l-1-u)=Catalan(l). Each of the c clusters therefore contributes the entire proposed product; division by c completes the induction. The last insertion has no denominator, giving

    S_L=sum_i F(full\{i})=L Catalan(L-1)=binom(2L-2,L-1).

An independent exact-rational subset recursion reproduced this for L=4,5,6,7,8,10,12; output is `/private/tmp/neutral_winding_path_check.json`. The proof does not depend on those samples. Stirling gives gamma_L~2J(lambda/2)^L/sqrt(pi(L-1)), with the stated normalization.

## 4. Plane symmetries

On aligned columns at even L, an X plane acts as a product of Xbar on its transverse row. A Y plane reduces, up to a configuration-independent phase, to the corresponding product of Xbar on its transverse column: the potential spin-dependent factors occur to the even power L. A physical Z plane acts as the product of logical Zbar over all transverse columns. The proposed adjacent Xbar_i Xbar_j commutes with all these actions. Thus it respects the exact native plane symmetries, rather than introducing a forbidden tunneling process.

This is an N=0 term, not automatically a term within the all-plaquette-positive ground manifold P0. An adjacent pair flip can create plaquette defects. Further projection to a particular low pattern family requires its own energy-denominator and symmetry analysis.

## 5. What the coefficient does not establish

The calculation takes lambda->0 at fixed L. It proves a nonzero formal leading winding coefficient and its exact sign. It supplies no uniform remainder estimate when L~lambda^(-p), where the order itself diverges. The factorial/order-dependent bounds of a fixed-order normal form cannot simply be evaluated at n=L. The coefficient therefore does not yet give a controlled actual hopping rate, a band dispersion, or an exponential lifetime for the growing-volume light rectangles.

There is no conflict with all-algebraic freezing/readout darkness obtained at each prescribed fixed order: for sufficiently small lambda the first winding order L lies beyond that order. Neither result alone establishes a nonperturbative kinetic law.

The draft's separate longitudinal-momentum observation is also consistent: all N=0 aligned-column configurations have Tz=1. If the chosen normal-form unitary preserves translation, nonzero-Qz states lie in N>=1 in its frame; the order-one positive wall bound and small global remainder exclude them from the stated low-energy interval. This uses the spectral lower bound, not the exponentially small winding formula.
