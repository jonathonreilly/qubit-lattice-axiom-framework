# Exact covariance and a texture parametrization

Use the supplied symmetric-phase walker model with three light-corner labels c, three spatial axes a and separate nonmixing scalar carriers. The one-loop tensor has the stipulated contraction form

T_L(c,a)=sum_(s,t) Re(eta_s conjugate(eta_t)) I_st(c,a)+sum_(c'!=c) w_cc' K(c,c',a).

The right-handed version uses transposed weights and its stated multiplicities. The first sum is an ordered sum, including both off-diagonal pairs. The coefficient Gram data and carrier weights are premises; equality of a few Yukawa moduli alone does not make the whole diagonal Gram matrix invariant.

Assume all data and kernels transform under the full simultaneous S3 action on corner and axis labels. There are exactly two orbits of ordered pairs(c,a): c=a and c!=a. Hence

T(c,a)=alpha+beta delta_ca.

Define iso=mean_(c,a)T=alpha+beta/3 and tet=mean_c[T(c,c)-mean_(a!=c)T(c,a)]=beta. Then the counterterm-subtracted tensor

r(c,a)=T(c,a)-iso-tet(delta_ca-1/3)

is identically zero. This algebra needs full S3 data; C3 invariance alone permits distinct oriented off-diagonal orbits. It neither evaluates the flawed historical off-diagonal strain integrand nor needs those numerical tables.

For general r define rho_c=mean_a r(c,a), so sum rho_c=0. A normalized mass-eigenstate column W_ci gives isotropic residual sum_c(|W_ci|²-1/3)rho_c. A flat column gives zero for every rho. This is a conditional projection identity, not a statement that all physical columns can be chosen flat.

An exact texture family is Y=A Z with Z_cc=exp(r), Z_cc'=exp(i phi_cc') for c!=c. A,r are real scale parameters and the six oriented phases are independent. It has equal complex diagonal entries and common off-diagonal modulus by construction. Using on-site diagonal Higgs data and equal nonmixing carrier weights supplies the full invariant one-loop data above. Additional selective-symbol data must satisfy the full Gram condition separately. The original fitting procedure selects numerical parameters within this ansatz; rounded saved matrices are not exact certificates of cancellations below their rounding scale. No empirical fit, arbitrary-target surjectivity, FCNC safety or two-loop cancellation is promoted here.

The elementary3x3 complex-Hadamard step is also retained: after row/column rephasing a flat unitary has first row and column all1/sqrt3. Orthogonality requires1+a+b=0 with |a|=|b|=1, forcing{a,b}={omega,omega²}; the third row has the opposite ordering. Thus every3x3 flat unitary is monomially equivalent to the Fourier matrix. Products of two such matrices are circulant-equivalent, with rephasings and permutations retained. This is an algebraic characterization, not a numerical exclusion using recalled CKM data.
