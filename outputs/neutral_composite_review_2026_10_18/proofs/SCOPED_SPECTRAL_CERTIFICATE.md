# A scoped spectral certificate for the supplied neutral channel

This is a conditional mathematical result for the stored candidate, not an exclusion of one-qubit-per-site physics or a conclusion from observed data. The supplied Hamiltonian remains a development input.

At total momentum Q=(pi,pi,pi), the bilinear Liouvillian is multiplication by the Hermitian144-dimensional matrix

    L_Q(k)=I tensor h(k+Q) - h(k)^T tensor I

in column-major vectorization. Its characteristic polynomial is monic of degree144. No common root exists between the characteristic polynomials at the two rational unit-circle momentum triples stored in probes/exact_no_flat_transition.json.

## Exact certificate

Every decimal literal in data/collective_corner_response/candidate.json is interpreted as the exact rational it spells. Exact hopping-pair Hermiticity is checked. Unit-circle phases (a+i b)/c satisfy a²+b²=c² exactly. All matrices at the selected points therefore have entries in Q(i).

Reduce the coefficient ring Z[i,1/D], for the finite set of denominators involved, modulo prime p with a chosen square root of -1. This is a ring reduction, not a field embedding of Q(i). Neither prime1009 nor1013 divides the denominators. The two characteristic polynomials have gcd1 after reduction, independently for both primes. Hence their reduced resultant is nonzero. The exact resultant cannot be zero, so their exact characteristic polynomials are coprime over Q(i), and have no common complex root.

The primary calculation uses trace convolution of the two12-dimensional Hamiltonians and Newton identities. An independent checker constructs the144-dimensional matrix entry by entry and uses similarity to Hessenberg form and its characteristic-polynomial recurrence. All145 coefficients match at both momenta for both primes. Additional direct determinant evaluations provide controls. One successful prime would suffice; the second is redundancy.

Controls are sensitive to real changes: replacing Q by0 gives a common polynomial factor of degree12 (conserved bilinears), and replacing the Hamiltonian by0 gives degree144. No empirical fit or chosen scalar interaction enters this certificate.

## Scope

This live fragment retains the exact finite characteristic-polynomial calculation. The original infinite-volume no-atom consequence, perturbation-neighborhood inference and higher-degree application are preserved as deferred scientific source; their N1 packet is incomplete. See the source-package recovery map.
