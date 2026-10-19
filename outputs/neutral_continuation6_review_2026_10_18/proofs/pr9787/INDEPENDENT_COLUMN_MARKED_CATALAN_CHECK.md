<!-- Original PR9787 source SHA256 862c7765e88f1a3e5e3eddf2b0486337cdb9dbe11a105c60f48560fe18d5fefe. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Exact winding-source path average: closed-form check

The proposed proof is valid for the periodic subset-path problem, in particular the fixed even L>4 native application. Use an auxiliary deformation parameter eta below to avoid confusing it with the physical source derivative h.

## Run identity and reversal symmetry

For every proper nonempty cyclic subset S, there are c occupied runs and c empty runs. A distance-two mismatch occurs when the two intervening nearest bonds contain exactly one domain wall. Counting these gives

    d2(S)=4c(S)-2[n1_occ(S)+n1_empty(S)].

Each singleton occupied or empty run removes two from the naive four-per-cluster count.

For an insertion permutation pi, let S_k be its first k sites, k=1,...,L-1. Reverse the permutation. Its intermediate subsets are T_k=S_(L-k)^complement. For a proper cyclic subset, c(S^complement)=c(S). Therefore the entire denominator product product_k 1/c(S_k) is unchanged under this bijection of permutations. Occupied singleton counts become empty singleton counts, with the order of partial steps reversed. The weighted expectations of their sums divided by c are exactly equal. No endpoint term from k=0 or k=L is present.

Consequently

    A_L=4(L-1)-4 E_weighted[sum_(k=1)^(L-1) n1_occ(S_k)/c(S_k)].

## Deformed factorization

Define the proper-subset recursion with denominator c(S)+eta n1_occ(S). Set f_0=1 and

    (1+eta delta_(ell,1)) f_ell
       =sum_(a=0)^(ell-1) f_a f_(ell-1-a).

Then F_eta(S)=product_(occupied runs) f_length(eta) solves the recursion exactly. Indeed, summing removal of a site within a run of length ell splits that run into a and ell-1-a, producing (1+eta delta_(ell,1)) f_ell. Summing over all runs multiplies the proposed product by c+eta n1_occ, canceling the recursion denominator. This is the required factorization proof; it does not assume independent run histories.

For f(z,eta)=sum_(ell>=0) f_ell(eta) z^ell, f_1=1/(1+eta), hence

    f=1+z f^2-eta z/(1+eta).

At eta=0, f is the Catalan generating function C. Its derivative G satisfies

    G=2z C G-z,
    G=-z/sqrt(1-4z).

Thus f_ell'(0)=-binom(2ell-2,ell-1) for ell>=1.

The last insertion has no denominator, and each full-minus-one subset has one occupied run of length L-1. Therefore

    S_L(eta)=L f_(L-1)(eta).

Differentiating the original positive path weights gives

    E_weighted[sum n1_occ/c]
      =-S_L'(0)/S_L(0)
      =L binom(2L-4,L-2)/binom(2L-2,L-1)
      =L(L-1)/[2(2L-3)].

Substitution yields the exact result

    A_L = 6(L-1)(L-2)/(2L-3).

All generating-function manipulations concern fixed coefficients and differentiation near eta=0, where the finite path denominators are nonzero. No infinite-series interchange or uniform large-L perturbation estimate is required.

Combining with the separately checked physical source derivative gives

    C_eff,offdiag^(L)
      =-gamma_L * 3(L-1)(L-2)/[J sqrt(V)(2L-3)].

This remains a formal fixed-L winding observable coefficient. The closed form does not change the earlier gauge, inelastic-readout, or growing-L remainder qualifications.
