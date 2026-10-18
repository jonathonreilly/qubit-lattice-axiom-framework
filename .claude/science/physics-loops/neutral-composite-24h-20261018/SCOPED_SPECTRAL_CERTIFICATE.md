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

## Consequence in the infinite-volume bilinear space

For any real frequency omega, det(L_Q(k)-omega I) is a real-analytic function on the connected momentum torus. If its zero set had positive Lebesgue measure, it would vanish identically. Then omega would be a common root at the two certificate points, contradiction. Thus each frequency level set has measure zero.

For square-integrable bilinear source coefficients, the spectral measure is obtained by integrating finite-matrix spectral projections against momentum Lebesgue measure. A frequency atom would require positive-measure support on the corresponding level set. There are therefore no frequency atoms in this fixed-Q bilinear space. The same inference holds with absolutely-continuous positive thermal weights; it does not cover singular state measures or delta-function probes.

Combining this with the residual/source-overlap bound in NEUTRAL_FEATURE_DERIVATION.md shows: at fixed infinite-volume operator, metric and normalized source, any normalized bilinear sequence whose frequency residual tends to zero at a fixed omega must have source overlap tending to zero. Arbitrarily extending a bilinear feature does not evade this statement. Generalized single-transition delta functions are outside the square-integrable domain. Finite boxes still have discrete transition lines.

## What this does and does not settle

This closes the exact flat-transition exception for the supplied fixed-Q bilinear channel. It does not establish a smooth spectral density, a rate of overlap loss, a dispersion law, a higher-composite obstruction, or an absence theorem for all one-qubit Hamiltonians. The supplied mass source is a pseudoscalar upstream, so this result cannot be relabelled as a general scalar-field theorem.

The original parameter values and intended unrounded construction are not silently identified with their stored decimals. A separately checked exact rational residual enclosure gives cross-spectrum separation greater than 8.241208801e-7 at the same two momenta. The property persists when every complex hopping entry changes in modulus by less than 2.4527407145e-9, provided hopping-pair Hermiticity is preserved. The bound follows from seven12-dimensional hopping blocks: each Hamiltonian changes by at most84epsilon in operator norm, and the separation of two transition spectra can fall by at most336epsilon. This is a certified neighborhood, not an identification of any particular unrounded upstream construction.

The research decision is to keep the constructive approximate excitations as useful conditional evidence and move toward symmetry-correct channels and genuinely higher composites. The source, dynamics, background state and physical measurement bridge still need derivation.
