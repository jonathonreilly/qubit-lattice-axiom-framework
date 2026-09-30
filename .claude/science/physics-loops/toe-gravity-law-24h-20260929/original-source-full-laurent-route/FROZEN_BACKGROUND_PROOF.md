# A physical flat-holonomy witness for a frozen-background subproblem

This proves the restricted target in FROZEN_BACKGROUND_CONTRACT.md. It is a new analytical exclusion for a declared class of actual H2 eigenvectors, using physical phase variables and all outgoing rows. The class can wrap every hole layer; the proof does not use slab peeling. It is not a replacement of the full many-body Hamiltonian by a one-particle model, and does not prove full Laurent observability or absorption of an initially prepared vector in this class.

## 1. Exact protected-column identity

Let L>=8 be even, n=L^3/2, and fix a B charge/vacancy pattern chi with at least one vacancy and total B charge one. All occupied A sites have charge +, with one A hole. These words have total charge n and satisfy the physical one-hole parity rule: NB=k is odd and the number of B minus charges is (k-1)/2. Denote by I_chi the fiber isometry from C^A to the physical charge-word space that places the hole at its argument. Integer tree flows exist for all these charge words.

Define F_chi to be those h in A for which:

* every B site at nearest-neighbor graph distance at most three from h is occupied;
* all six immediate B neighbors have charge +.

Write P_F for its coordinate projection. This is an explicit restriction on the support of a proposed eigenvector, not a dynamical assumption about chi or F being preserved.

Choose any physical U(1) connection A_e on the oriented A-to-B edges representing the cycle phases. Set the auxiliary geometric incidence matrix

    (K_A u)(b)=sum_(a~b) exp(i A_ab) u(a),
    T_A=K_A* K_A.                                         (1)

It is a finite matrix used to express the following proved columns. It is not a supplied substitute law on unrestricted matter configurations. Up to the diagonal charge-word gauge determined by the chosen Gauss tree section, the ACTUAL canceled H2 satisfies

    H(A) I_chi P_F = I_chi T_A P_F.                        (2)

The equality includes every outgoing row, not only compression back into F.

To verify it, use the exact original blocks

    P_h H P_h=P_h(F_h F_h* -sum_(dist(a,h)=2)F_a*F_a)P_h,
    P_a H P_h=P_a[F_a,F_h*]P_h.                           (3)

For h in F, the first hop F_a in every negative same-hole term is blocked: each B neighbor of such an a lies within distance three of h and is occupied. Refilling h from any neighbor takes a plus charge; the only empty B neighbor then available for the return is that same donor. The six diagonal returns contribute six, exactly the diagonal of T_A.

For a different A center sharing b with h, the order F_a F_h* fills h from the plus B donor and empties the plus A_a back into it. Both A and B charge patterns are restored except for moving the hole to a. Its phase is exp(i A_hb-i A_ab), the corresponding term of (1). The reverse order is blocked by the same distance-three occupancy condition. Different shared B sites add exactly as in K_A* K_A. More distant terms cancel in (3). No output with a different B pattern or a minus A occupation occurs. These statements remain true when the outgoing hole a is outside F, including when its new star is mixed or close to a vacancy. Thus they establish (2), not merely an interior approximation.

For phase bookkeeping, in tree gauge A_e=0 on tree edges, a primitive plus-charge transport has the above edge phase directly. In another gauge, changing the tree-flow representative multiplies each charge-word basis vector by a phase; on I_chi this is a diagonal unitary. Intermediate rows corresponding to removing an occupied plus B charge can be rephased similarly. Extending K_A geometrically to other B rows is harmless: K_A P_F vanishes on every row whose B charge is not plus. Hence those auxiliary rows make no contribution to T_A P_F. The physical phases in (2) are the same shared edge variables as in the original law.

## 2. Realizing a flat witness with actual cycle phases

Take the uniform flat connection

    A_(a,a+delta)=phi dot delta,   delta in {+/-e_1,+/-e_2,+/-e_3}, (4)

where delta is the local oriented unit displacement, including across a periodic seam. Every plaquette holonomy is zero and the three noncontractible holonomies are L phi_i modulo 2pi. Thus every real phi gives an allowed physical phase point; (4) is not an assignment of independent weights to configuration-graph edges. A gauge transformation puts it in the selected spanning-tree coordinates. Changes phi_i by 2pi/L only relabel the Fourier modes up to gauge.

Let k_i=2pi j_i/L. The restrictions to A of the characters exp(i k dot h) are identical precisely under

    k ~ k+(pi,pi,pi).                                    (5)

Indeed A is the index-two even-parity subgroup of the periodic vertex group, and its annihilator consists of zero and this simultaneous pi shift. Choosing one representative per class gives n orthogonal characters on A. Normalize them as u_k(h)=n^(-1/2)exp(i k dot h). Direct substitution, including the seam terms, gives

    K_phi u_k = g_k(phi) times the corresponding B character,
    T_phi u_k = lambda_k(phi) u_k,
    g_k(phi)=2 sum_(i=1)^3 cos(k_i-phi_i),
    lambda_k(phi)=g_k(phi)^2.                            (6)

The simultaneous pi shift changes g to -g, so lambda is well-defined on (5).

The squared frequencies for two DIFFERENT classes are not identical analytic functions. If g_k^2-g_l^2 vanished identically, the product (g_k-g_l)(g_k+g_l) would be zero in the Laurent-polynomial ring in exp(i phi_i). That ring has no zero divisors, so g_l=s g_k for one common sign s=+1 or -1. Comparing coefficients of exp(i phi_i) gives

    exp(-i l_i)=s exp(-i k_i) for every i.                (7)

For s=+ this is the same k; for s=- it is exactly the simultaneous pi shift. Both contradict distinctness of the classes. Therefore the finite union of pair-degeneracy zero sets has measure zero. A nonzero real trigonometric polynomial has a Haar-null zero set, as follows by one-variable root counting and induction/Fubini on its coefficients. In particular there exists a physical flat phi for which ALL n eigenvalues in (6) are distinct. No numerical sample or independently weighted matrix is needed.

Every Fourier eigenvector has a nonzero component at every A vertex. It follows already that no T_phi eigenvector can have support in a proper subset of A at this witness point.

## 3. An actual nonzero Laurent observation minor

Choose a vacant B site v and any adjacent A site a_0. Then a_0 is outside F. Form the n-by-n matrix

    O_(a_0)(A) = rows [e_(a_0)* T_A^r],   r=0,...,n-1.     (8)

At a nondegenerate flat witness, multiply (8) by the Fourier unitary. Its kth column is u_k(a_0)(1,lambda_k,...,lambda_k^(n-1))^T. Its determinant is nonzero: apart from the Fourier-unitary determinant it is

    product_k u_k(a_0) times product_(k<l)(lambda_l-lambda_k). (9)

Both factors are nonzero. In tree gauge the entries of K_A and T_A, and hence det O_(a_0), are Laurent polynomials in the ACTUAL independent cycle variables. Physical adjoint phases become inverse monomials in this algebra. Equation (9) is an explicit existence proof of a nonzero Laurent polynomial at an allowed physical phase point. Consequently O_(a_0)(theta) has full rank for almost every cycle phase theta.

Now suppose an actual H(theta) eigenvector psi=I_chi u has support u=P_F u. Equation (2) and the isometry imply

    T_theta u=lambda u.                                 (10)

This uses all outgoing charge-word rows: no discarded boundary condition is imposed by hand. Since a_0 is outside F, u(a_0)=0. Thus every row of (8) vanishes on u by (10). At phases where (8) is invertible, u=0. This proves:

For each declared fixed pattern chi, almost every physical cycle phase admits no nonzero actual H2 eigenvector confined to I_chi Ran P_F. Equivalently, there is no nonzero H2-invariant subspace entirely confined to this class, because a finite-dimensional self-adjoint invariant subspace contains an eigenvector. The exceptional set can be chosen from (8); it is not inferred from a sampled rank.

At fixed finite torus there are only finitely many patterns and vertices. If desired, the null sets can be united to make this statement simultaneous for every separately considered chi and choice of a_0. This statement still concerns eigenvectors confined to one fixed background; it is not a claim about coherent cancellation between unrestricted background sectors.

## 4. What this new minor does and does not settle

The hole support F may wrap every y+z layer, so this restricted result is not a rephrasing of the proper-slab theorem. The flat-phase aligned line in ALIGNED_FIBER_PROOF.md is consistent with it: zero holonomy is a degenerate exceptional point, while (6)-(9) choose generic flat holonomies and then certify an almost-everywhere property on the full physical phase torus.

The observation matrix here has size n, for the exactly proved frozen-background column problem. It is NOT the complete observation matrix of dimension d_f for all one-hole masks and charges. Formula (2) cannot be extended to unprotected columns merely because (1) is bounded or local. In particular the negative same-hole reshuffles return when a vacancy lies within distance three; mixed A charges change outgoing charge words. An eigenvector with components in such sectors can cancel its outgoing rows against those of a protected component. No bound on the projection of an initial protected vector onto an extended invariant dark module follows.

The actual continuously generated source, its local input-image density, the generic full dark module, its source overlap and quantitative late survival remain unresolved. No finite-spin, microscopic-time or energy inference follows from this restricted eigenvector exclusion. The calculation retains the original G and marks in its scope; it adds no phase distribution or observed background measurement.
