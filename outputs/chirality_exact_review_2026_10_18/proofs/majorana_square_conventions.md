# Majorana square conventions and the finite endpoint boundary

Let gamma_i be Hermitian Majorana generators with {gamma_i,gamma_j}=2 delta_ij. For a real antisymmetric coefficient matrix A, write B(A)=i sum_{i<j} A_ij gamma_i gamma_j. Expanding in the ordered Clifford basis gives

B(A)^2 = sum_{i<j} A_ij^2 I - 2 sum_{i<j<k<l} (A_ij A_kl - A_ik A_jl + A_il A_jk) gamma_i gamma_j gamma_k gamma_l.

Indeed, identical pairs contribute the positive scalar. Distinct pairs sharing one index cancel between the two orders. Disjoint pairs commute, and sorting their four indices supplies the three alternating signs. Consequently every individual square has only grades zero and four. An identity between sums of these squares requires equality of the scalar coefficient and every ordered grade-four coefficient; sampled quartic components alone do not establish it. The scalar terms may cancel in a signed combination, but that cancellation must be checked explicitly.

The source conventions differ. SIGN1 uses B=psi^T(E tensor N)psi, whereas QMC uses Bh=B/2. Therefore Q_QMC=-(Bh^2+h.c.)/4=Q_SIGN1/16. The QMC Pe is the original pairing matrix divided by two. Coefficients cannot be transferred between these conventions without these factors and the channel normalization. A claimed finite endpoint identity will be promoted only after the accompanying primary exhausts all Clifford coefficients in the stated finite representation.

This algebra supplies no spectral gap, interacting symmetric mass generation phase, determinant positivity away from the stated endpoint, or extension to a larger coupling cone. Those require additional arguments. At present this source promotes the exact square expansion and convention conversion, while the endpoint channel decomposition remains pending the complete authored coefficient check.

## Explicit endpoint coefficient construction

The companion primary now constructs the original real symmetric Cl(9) representation by a deterministic search over four-letter real Pauli words, checking every anticommutator. Write P+=(I+G9)/2 and P-=I-P+. In the QMC convention set Bh_a=psi^T(E tensor N_a)psi/2, N=(G1,...,G9,iI). For each g=G1,...,G8 and tau=E (singlet) or E sigma_j (three triplets), set T=tau tensor(P+ g P-) and M=(T-T^T)/2, P_e=psi^T M psi. The finite coefficient identity is

sum_a Bh_a² = (3/2) sum_singlet P_e² - (1/2) sum_triplet P_e².

The proof is finite exhaustive coefficient comparison: the ordered coefficient of psi_i psi_j psi_k psi_l is eight times M_ij M_kl-M_ik M_jl+M_il M_jk, and the primary enumerates all C(32,4)=35960 such coefficients using exact dyadic entries. It then independently multiplies the sparse 64-generator Clifford representations of both sides of Q=-(sum Bh_a²+h.c.)/4, checking scalar and quadratic grades as well as grade four. There are 8 singlet and 24 triplet pairings, yielding 64 Hermitian Re/Im channels. Their coefficients are -kappa/2 and +kappa/2. The explicit antiunitary Majorana map O=diag(E tensor I16,-E tensor I16) squares to -I; the primary verifies each channel is even for a negative coefficient and odd for a positive one. All primary assertions are required before capture PASS; no execution has yet been asserted by this author package.

This closes the local coefficient-check obligation named above when the finite primary passes. A sign-free lattice determinant additionally requires invariant kinetic factors, the chosen particle-hole/d-frame, appropriate boundary conditions and a specified auxiliary-field factorization. Those global ingredients, a spectral gap and the nonzero-lambda1 cone are not promoted by this local identity.
