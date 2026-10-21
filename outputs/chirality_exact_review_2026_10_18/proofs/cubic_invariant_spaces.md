# Proper-cubic invariant spaces for the supplied light-corner representation

The three light corners are pi e_c, c=1,2,3, each with a two-component spinor. A proper signed-permutation rotation R acts as U_R=P_R tensor u_R, where P_R permutes the unoriented coordinate axes and u_R sigma_a u_R†=sum_b R_ba sigma_b. Its irrelevant spin-lift sign cancels in conjugation. These matrices, rather than every possible cubic representation, define the calculation.

Expand a Hermitian6x6 matrix in corner matrix units and I,sigma_x,sigma_y,sigma_z. The spin-conjugation representation is the real representation1+R. The full corner-matrix representation has character f(R)², where f is the number of unoriented axes fixed by the permutation P_R. Exact unit translations restrict the corner matrix to its diagonal subspace, whose character is f(R). In the BCC residual translation lattice all corner matrix entries are allowed in this supplied light sector.

The invariant projector is the group average. Therefore the exact dimensions are

constant: (1/24)sum_R f(R)^p [1+tr R],
linear momentum: (1/24)sum_R f(R)^p [1+tr R] tr R,

where p=2 for the full corner-matrix space and p=1 for the diagonal restriction. Complexification has the same invariant dimension as the Hermitian real form because conjugation preserves that form. Enumerating all24 determinant-one signed permutations yields constant dimensions2 and1, and linear dimensions5 and2, respectively. This is an exact integer character computation, independent of a singular-value tolerance.

The BCC character calculation itself is elementary: requiring exp(i pi(n_y+n_z))=exp(i pi(n_x+n_z))=exp(i pi(n_x+n_y))=1 gives n_x=n_y=n_z mod2. Its corner characters split into even and odd Hamming parity. The body-diagonal translation labels the corner chiralities only at these corner momenta; it is not a full-zone chirality projector.

These dimensions count allowed operators. They do not force their coefficients, select a condensate, certify a gap or determine experimental velocity bounds. The original loop/naturalness/phenomenology claims remain separate supplied-model calculations and require their reported corrections before numerical reuse.
