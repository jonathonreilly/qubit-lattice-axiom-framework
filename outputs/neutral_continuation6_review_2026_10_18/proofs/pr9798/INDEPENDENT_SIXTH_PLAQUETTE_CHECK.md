<!-- Original PR9798 source SHA256 5b903d62ba3c8fe5b32e606abb55ebca51e8be4e04e4a624f607d728922896b2. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Independent sixth-order single-plaquette renormalization

The proposed coefficient is confirmed by an independent exact multivariate energy recursion, as well as by checking the fold signs and connected-support classification. This checks the fixed-height-six vacuum diagonal coefficient; it does not certify a four-flux pole or the complete dynamical block.

## Independent computation

Created `/tmp/neutral_sixth_plaquette_independent.py` and its JSON output. Unlike the root path-sum implementation, this uses the intermediate-normalization Rayleigh–Schrödinger recursion for every multidegree up to the target monomial. For alpha>0, the vacuum component gives E_alpha from V psi_(alpha-e_b), and the nonvacuum components obey

psi_alpha(s) = [sum_b V_b psi_(alpha-e_b)(s)
 -sum_(0<beta<alpha) E_beta psi_(alpha-beta)(s)] / (-E_s).

All arithmetic is rational. Physical spin coordinates and vertical wall energies are constructed independently. Target exponents are one on each plaquette edge and two additional occurrences of b; when b is already a plaquette edge its exponent is three, not two distinct copies. Thus permutation multiplicities and folded energy corrections are handled automatically.

For the twelve transverse bonds incident to the plaquette's four columns at each tested layer, the exact summed coefficients were:

- Same layer: 7/2048.
- Either neighboring longitudinal layer: -11/4608.
- Separation two: zero.

These match the root outputs. Their sum is -25/18432 per plaquette layer, and multiplying by six gives -25/3072.

## Fold formula

Let the proper self-energy return functions be Sigma_2(E), Sigma_4(E), Sigma_6(E), with resolvents (E-H0)^-1. The target plaquette-plus-doubled-bond monomial at order six has

E6 = Sigma6(0)+E2_b Sigma4_loop'(0)+E4_loop Sigma2_b'(0).

Other compositions of lower returns have even edge exponents or exceed order six, so cannot produce this monomial. Since d(E-E_s)^-1/dE=-(E-E_s)^-2, the derivative of a four-step path is minus its amplitude times the sum of its three inverse denominators. Thus the supplied weighted-loop sum +5/2048 means Sigma4_loop'=-5/2048. Also Sigma2_b'=-1/64. Using E2_b=-1/8 and E4_loop=-1/128 gives

E2_b Sigma4_loop'+E4_loop Sigma2_b'
 =5/16384+2/16384=7/16384.

Accordingly raw6+7/16384 has the correct sign and normalization, including b equal to an original loop edge. This is not a factorial-labeled bond enumeration; the root unique-permutation convention and the independent multivariate recursion agree.

## Exhaustion and height-six scope

The previously checked modulo-two Eulerian classification says a sixth-order single-plaquette diagonal term must have exactly its four edges at one layer plus one doubled transverse bond. A doubled bond with no endpoint in a plaquette column is dynamically disconnected under the vertical H0: all corresponding cross energy coefficients cancel. If it touches those columns but lies beyond neighboring longitudinal layers, the local wall energy likewise separates between the two sets of flips; the same connected cancellation applies. At height six only the same layer and the two adjacent layers contribute. Separations two, three and four have no connecting vertical bond between the supports; separation five is the other adjacent layer. This explains why enumerating separation two is a control rather than an assumption that other separations are identical by sampling.

The same-layer incident-bond set includes four loop edges and eight outgoing edges, so no repeated-edge multiplicity is missing. The background-dependent factor is exactly the original plaquette P: squared insertions do not add a new odd X/Y incidence. Translation along z makes all six loop layers equivalent. The other sixth-order diagonal family is the separately computed simple rectangle; the two families have different edge-multidegree parity and must not be combined or counted twice.

Within the N=0 block the coefficients before order six are diagonal (order-two scalar, order-four plaquette), while the height-six winding is first off-diagonal at order six. Consequently this formal energy calculation determines the stated diagonal coefficient without requiring a choice of a nondegenerate actual N=0 eigenstate. It is not claiming that an aligned background itself is an eigenstate after the winding term is retained.

Therefore, for a periodic height-six slab with transverse periods excluding short wrap cycles, the single-plaquette part includes

-J[(6/128) lambda^4+(25/3072) lambda^6] sum_p P_p,

alongside scalar terms, the -18 J lambda^6/8192 adjacent-plaquette term, and the separately retained winding kinetic term. Any absolute center of a dynamical four-flux level also requires those other terms and the appropriate vacuum subtraction; this coefficient alone is not that center.
