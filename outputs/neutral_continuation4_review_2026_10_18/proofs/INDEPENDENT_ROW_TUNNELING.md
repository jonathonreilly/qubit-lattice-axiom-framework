<!-- Owning original: PR9760; source SHA256 09ab7c70b99e4a8d424053fabe49bd8947323c07b234f65757b707666f4c3955. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Row/column tunneling in the plaquette coefficient model

Checked 2026-10-18. Model Hcol=-K sum_square P_square -t sum_nearest XX on an even M by M transverse torus, M>=4. Assume K>0 and t>0, and use small t/K at fixed M. This is a coefficient-model calculation, not a uniform-in-M convergence statement or a full native all-order theorem.

## Minimal processes and signs

The P=+1 configurations have signs s_xy=a_x b_y. Any nontrivial change between them flips at least M sites; the sets of size M are exactly single rows or columns for M>=4. Since an XX edge flips two sites, at least n=M/2 operations are required. At this minimal order no site can be flipped twice: the edges form a perfect matching of the target row/column. The even cycle has exactly two such matchings. Vertical edges cannot contribute to a row target at minimal order because they would flip sites outside it.

For a proper subset of one matching, let r be its number of occupied runs in the cyclic dimer order. Each run has two row endpoints, and each endpoint changes two neighboring plaquettes. Thus there are4r bad plaquettes, with energy cost8Kr. Every proper nonempty subset has r>=1 and lies outside P+. The numerator is (-t)^n and there are n-1 negative resolvent denominators. Every path therefore contributes negatively. No folded correction contributes to this FIRST nonzero offdiagonal transition: a proper return would require a lower-order nontrivial ground-manifold transition, which does not exist.

## All-n run sum

For one matching define W_n=sum_permutations product_(k=1..n-1)1/r(S_k). Map occupied dimers to spins on an n-site cycle; their domain walls are2r. Each dimer flip toggles its two adjacent domain-wall bits. This is exactly the unsigned all-X distinct-edge cycle problem with elementary defect cost d=4K. Its coefficient can be evaluated by the linked time integral with two insertions per domain-wall site:

    U_n = integral(domega/2pi) [2/(1+omega^2)]^n
        = binom(2n-2,n-1)/2^(n-1).

Since the denominator count uses2r rather than r, W_n=2^(n-1) U_n=binom(2n-2,n-1). The n=2 case consists of two parallel dual edges and directly gives W_2=2, agreeing with the same formula. No Gaussian premise is needed for the distinct-edge coefficient: each dual site receives exactly two insertions and proper subsets have nonzero domain walls.

Independent exact Fraction subset recursion for n=2 through10 gives2,6,20,70,252,924,3432,12870,48620, matching the closed expression. Thus including both matchings,

    tau_M=2 binom(2n-2,n-1) t^n/(8K)^(n-1),

and the offdiagonal row/column amplitude is -tau_M as proposed.

## Ground characters and the local readout

The leading nonconstant effective operator is

    -tau_M (sum_rows R_y + sum_columns C_x).

All generators commute and satisfy product_rows R_y product_columns C_x=I. On the P+ manifold they form the regular representation of Z2^(2M-1), so each allowed character occurs once. For positive tau_M the all-plus character is the unique ground state of this leading operator. An excitation must flip an even number of characters; the first allowed cost is4tau_M. This is a leading small-t/K conclusion at fixed M, not proof of an exact gap with no higher corrections.

A single local Z_xy commutes with plaquette projectors and anticommutes with exactly R_y and C_x. It therefore maps the all-plus character to the corresponding two-negative character with norm one. In the leading effective model the longitudinal Z spectral response has one such transition at4tau_M with residue1, and <Z_xy>=0. Degenerate excited character states can be chosen in their character basis; the norm-one result is unaffected by the degeneracy.

This operator is CHARGED under the row/column symmetries. Its transition is not a neutral response and does not contradict the neutral restricted-gap/static-locality result. A physical longitudinal spin may map to this logical Z within the aligned-column coefficient construction, but the original longitudinal separation-two diagnostic maps to identity in that manifold at leading order; it does not automatically inherit this residue. Transverse X or Y takes a state out of the plaquette ground manifold at leading projection, so 'longitudinal only' is appropriate for this leading low-energy single-spin response, not a universal statement about all observables.

## Limitations

The combinatorial coefficient is exact at its first nonzero order. Higher orders can generate corrections and multi-generator terms; controlling them uniformly as M grows requires additional bounds. If t has another sign, the sign of t^n matters and the all-plus ground assertion needs revision. Small periodic M=2 is excluded because its bond/plaquette multiplicities differ. The native column height, derivation of K and t, and suppression of other native terms remain separate premises of embedding this coefficient model.

Conclusion: minimal matching count, denominator run sum, negative tunneling amplitude, character gap4tau_M, and leading charged-Z residue1 check under these stated conditions.
