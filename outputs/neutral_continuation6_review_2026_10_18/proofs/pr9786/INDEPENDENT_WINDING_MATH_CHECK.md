<!-- Original PR9786 source SHA256 4cc868e10a51ab3ac250b7b1f3dd1290592fc62ec888515f5156b6105bce13bc. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# First native periodic-column winding coefficient: independent check

Disposition: PASS for fixed even longitudinal circumference L>4, in the native word-preserving reduction to the full N=0 block. The gauge qualification below is necessary. Read the appended section of /tmp/neutral_whole_column_root.md. No repository edits.

Layer parity makes the number of flipped complete columns even. Any nontrivial N=0 transition therefore flips at least 2L individual spins. Each native transverse insertion flips two sites, so its order is at least L. Equality permits no repeated site flip: precisely two columns are reversed and every site is flipped once. The two columns must be adjacent, since at each z their two sites must be joined by one native transverse bond. The word consists of that same transverse bond at all L heights, each once. This assumes distinct transverse nearest-neighbor bonds, as in the specified large transverse boxes; degenerate tiny transverse periods need separate multiplicities.

For a proper nonempty subset S of rungs on the longitudinal cycle, each cyclic connected cluster creates two broken longitudinal bonds in each of the two columns. A broken bond costs 2Jz, so the intermediate energy is exactly 8Jz c(S), independently of the aligned background column signs. Every proper subset has positive cost and no N=0 return. “P0 return” here should mean return to the full N=0 perturbative block, not only its lower plaquette-ground subspace.

Define F(empty)=1 and F(S)=[sum_(i in S)F(S\{i})]/c(S) for proper nonempty S. If the clusters have lengths l_1,...,l_c, induction gives F(S)=product_a C_(l_a). Removing one site in a cluster of length l splits it into lengths j,l-1-j, including empty pieces. Summing over its l sites gives sum_(j=0)^(l-1) C_j C_(l-1-j)=C_l. Each of the c clusters therefore contributes one copy of the same total product; division by c establishes the induction. The complete-cycle final step has no denominator, giving

 S_L=sum_(last rung i)F(all\{i})=L C_(L-1)=binomial(2L-2,L-1).

For XX, the product of L numerator signs and L-1 negative resolvent denominators is negative, at any L. For YY the numerator at each untouched rung is +Jz lambda s_i s_j. The aligned column signs are constant in z, so at even L their product is +1. The L-1 negative denominators then also give a negative result. No Pauli ordering phase is hidden because the squarefree rung operators have disjoint sites. At odd L the orientation-dependent YY sign would remain; the stated even-L hypothesis is essential.

Thus the first off-diagonal term in the full aligned-column block is

 -gamma_L sum_(nearest transverse pairs i,j) Xbar_i Xbar_j,
 gamma_L=Jz lambda^L binomial(2L-2,L-1)/8^(L-1).

This is the periodic-cycle coefficient. It should not be confused with the different open-longitudinal-chain tunneling coefficient. The stated formal large-L coefficient estimate follows directly from the central-binomial asymptotic:

 gamma_L~2Jz(lambda/2)^L/sqrt(pi(L-1)).

Folded/normalization terms cannot modify this first native off-diagonal coefficient: any nontrivial returning subword consumes insertions, leaving fewer than L insertions for the required 2L site flips. Equivalently any factorization into a lower-order off-diagonal block coefficient vanishes. This argument applies to reductions whose coefficients are formed from native insertion words with diagonal H0 projectors/resolvents (and their folded combinations), preserving flip-count grading. In this class every lower-order block coefficient and gauge coefficient is diagonal in the aligned-column basis, so lower diagonal gauge commutators do not change the result.

It is not a statement invariant under an arbitrary externally imposed, nonlocal lambda-dependent unitary within N=0. Such a unitary could rotate the lower-order plaquette diagonal term and manufacture off-diagonal entries. Fix the native word-preserving gauge, or transform the effective column observables along with any additional gauge change. Subject to that explicit convention, the minimal coefficient is sound.

All conclusions are fixed-L Taylor statements. The binomial asymptotic describes the coefficient itself, not uniform dominance of this term in a joint L~lambda^-p limit. No convergent resummation, actual exponentially small gap, transport rate, or exponential lifetime has been established by this calculation.
