# Independent native auxiliary-Majorana algebra check

Disposition: PASS for the representation, nonstatic-link obstruction, and ordered-loop phase. No physical fermion, free-fermion solution, deconfinement, or emergent gauge dynamics is established.

Prior art: Kitaev, *Anyons in an exactly solved model and beyond*, https://arxiv.org/abs/cond-mat/0506438. That paper's static-field/free-fermion result concerns its honeycomb model. The compass-lattice conclusions below are derived directly, rather than transferred from that solvable case.

## Physical constrained representation

Take globally anticommuting Majoranas b_i^x,b_i^y,b_i^z,c_i with squares one. D_i=b_i^x b_i^y b_i^z c_i is Hermitian, squares one, and commutes with all physical sigma_i^a=i b_i^a c_i. In the D_i=+1 subspace the latter obey the physical Pauli algebra. For example b_i^x b_i^y=-b_i^z c_i=i sigma_i^z.

For an oriented a-link i->j, u_ij=i b_i^a b_j^a is Hermitian, u_ij^2=1, and u_ji=-u_ij. The native term -J_a sigma_i^a sigma_j^a equals +i J_a u_ij c_i c_j. The auxiliary Hilbert space has a local constraint; it does not add physical qubits or prove fermionic statistics of physical excitations.

## Link noncommutativity and dynamics

Two bilinears of distinct Majoranas commute if their supports are disjoint and anticommute if they share exactly one Majorana. Consequently opposite a-links incident to the same cubic-lattice site anticommute: both reuse b_i^a. Incident links of different axis types use different b Majoranas and commute. This is the crucial difference from assigning one distinct b to each incident edge on a trivalent lattice.

Every u commutes with all c_k c_l. Thus for a fixed u,

    dot(u)=i[H,u]
          =-2 sum_(links e sharing one b with u) J_e u_e u c_(e1)c_(e2)
          =+2 sum_e J_e u u_e c_(e1)c_(e2).

On a nondegenerate cubic graph those are the two neighboring collinear links, one at each endpoint. The separate Clifford monomials do not cancel identically. The link itself, being gauge charged at its endpoints, is not a physical gauge-invariant observable; this exact auxiliary equation nevertheless rules out treating all these u's as simultaneous conserved classical signs. Substituting static numerical u's would alter the model, not solve it.

## Ordered simple xy loop

Let v_0,...,v_(N-1) be distinct loop vertices, a_j the axis of v_j->v_(j+1), and define the traversal-ordered product U=u_01 u_12 ... u_(N-1,0). Orient each u along that traversal. Expanding gives i^N times

    b_(0,a0) b_(1,a0) b_(1,a1) ...
                b_(N-1,a_(N-2)) b_(N-1,a_(N-1)) b_(0,a_(N-1)).

Moving the final basepoint Majorana beside the first crosses 2N-2 other Majoranas and hence adds NO sign. At a nonbase vertex the local pair is incoming then outgoing; at the base it is outgoing then incoming. A straight pair equals one. A turned pair is b^x b^y=+i sigma^z or b^y b^x=-i sigma^z on the physical subspace. In the cyclic incoming/outgoing sequence there are m/2 turns of each kind, so their total phase is one. Reversing the basepoint pair contributes minus one precisely when the basepoint is a turn.

Since N is even,

    P_phys U P_phys
      = (-1)^(N/2 + 1_[basepoint is turn])
          product_(turn vertices) sigma_v^z P_phys.

This matches the root formula. For a nonphysical unconstrained representation the appropriate D factors remain; they must not simply be discarded before imposing D=+1. The closed loop commutes with every D_i, unlike an individual u.

A cyclic shift of the product can change its sign when it changes a straight basepoint into a turned basepoint. This is not a contradiction: a product of noncommuting links is not cyclically invariant. The representative basepoint/order and oriented-edge convention are part of its definition. This loop is therefore not an ordinary commuting static Z2 Wilson-flux label. Its projection is an existing local spin-string operator, generally not a conserved flux of the native compass Hamiltonian.

## Independent Clifford control

`/tmp/majorana_independent.py` implements multiplication of ordered Majorana monomials using bit masks and exact inversion parity, without using the loop-phase formula to perform multiplication. It compares U against the claimed phase times the physical corner-Z word times the required D factors. All basepoints pass for a four-edge square, a six-edge rectangle, and an eight-edge six-turn L loop. This checks both straight/turn basepoint changes and the concave-loop case.

No statement about physical exchange statistics follows from the anticommutation of these auxiliary variables. That would require physical excitations and their transport/exchange operators in a specified state or sector. Nor does the failure of this static-u substitution prove that every other fermionic description is impossible.
