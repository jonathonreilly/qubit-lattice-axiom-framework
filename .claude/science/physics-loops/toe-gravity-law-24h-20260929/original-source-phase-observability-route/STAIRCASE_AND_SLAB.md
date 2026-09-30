# Exact charge monodromy and a partial phase unique-continuation result

Author proof under SLAB_CONTRACT0adf800b, awaiting focused reconstruction. This is NOT the requested full torus observability theorem. It excludes a persistent dark eigenvector confined to a proper hole slab, and hence excludes continuations confined to the known B-strip family. A dark projection of an initially local source could extend over the entire torus; this proof does not exclude it.

## 1. Actual blocks and physical fibers

Take even L>=8, n=L³/2, global W1, odd N_B=k<=n-1 and total matter charge n. There are M=n-1+k occupied sites and r=(k-1)/2 negative charges. Use every charge assignment and every B mask, not a symmetric-charge subspace. The supplied original rotor coefficient and loss are

 H=C+[F,F*], C=sum_a F_a*F_a Q_gate,a,
 G=sum_mu j_mu*j_mu=2*(empty B neighbors of the A hole).

Both original instruments have this loss; their marked outputs remain distinct. The complete canceled hole blocks are the checked actual identities

 P_h H P_h=P_h(F_hF_h* -sum_(a:dist(a,h)=2) F_a*F_a)P_h,
 P_a H P_h=P_a[F_a,F_h*]P_h, a!=h.                       (1)

In the off-diagonal block, distinct-B paths cancel. For a DARK input all six neighboring B sites of h are occupied. The negative shared-B path F_h*F_a is then blocked on its first outward hop. Thus each surviving hole move h->a through shared B site b consists exactly of filling h from b and then moving the charge at a back into b. Its B mask is unchanged, its charges are permuted, and its two integer field shifts are retained. Same-hole B reshuffles in the first line(1) are NOT dropped; they will be absent only from the particular output rows used below.

Choose a spanning tree. Each physical field is its charge-dependent integer tree flow plus d=4n+1=2L³+1 independent integer cycle currents. At each cycle phase theta, the above blocks are finite matrices with unit-modulus charge-dependent hop phases. Every allowed elementary charge move is a bijective unitary between the corresponding fixed-occupancy charge fibers, of common dimension binomial(M,r). All estimates below are in these full fibers.

For clarity one may specify a connection by phases on all oriented graph edges and then gauge its tree phases to1. The resulting chord holonomies are the physical cycle phases. This is a unitary change of the finite charge-fiber basis, not a change in H, G or the original marks.

## 2. The two-matching map on a fully occupied staircase ring

Fix x and a layer j of y+z modulo L, with parity chosen so the sites h_l are A. Set

 h_l=(x,y0-l,z0+l),
 b_l=h_l+e_z=h_(l+1)+e_y,          l modulo L.            (2)

These are 2L distinct vertices on an alternating A/B cycle. Suppose all b_l are occupied and exactly one h_l is the global A hole; all other A sites are occupied automatically. Let U_z map an A hole h_l to the intermediate B hole b_l by the actual inward hop b_l->h_l. Let U_y do the same using b_(l-1)=h_l+e_y. Each is a unitary matching between the direct sums of A-hole and B-hole charge fibers, including its exact field phase. The two-path map is

 K=U_y+U_z=U_y(I+W),  W=U_y*U_z.                         (3)

W fills h_l from b_l and then empties h_(l+1) into b_l. Thus it moves the A hole one step around(2), using the actual two primitive hops. After L steps the hole returns and the 2L-1 charges on the remaining ring vertices are cyclically permuted by one place. After

 N_c=L(2L-1)

steps all charges return to their original positions. Every charge has traversed every cycle edge once, in the same hole-opposite orientation. Consequently the total field displacement is Q_c times the oriented cycle circulation, where

 Q_c=sum_(occupied ring vertices) q_x

is an ODD integer, with 1<=|Q_c|<=2L-1. This holds for every charge assignment, not only for its average. In the exact Gauss fiber this gives

 W^(N_c)=exp(i Q_c Phi_c),                               (4)

as a diagonal multiplication operator on the matter labels. Phi_c is the Wilson phase of the oriented geometric cycle. Q_c is preserved by W. The sign of Phi_c depends on the chosen cycle orientation; the conclusions below do not.

Because L is even, N_c is even. The finite geometric identity is

 [I-W+W²-...-W^(N_c-1)](I+W)=I-W^(N_c).                 (5)

All W powers are unitary on the physical phase torus, so (4)-(5) imply

 ||K v||>=d_c(theta)/N_c ||v||,
 d_c(theta)=min_(odd q,1<=|q|<=2L-1)|1-exp(i q Phi_c)|.  (6)

This is an exact full-charge bound. It does not treat the q_x as independent classical variables. A charge-dependent phase vector may be arbitrarily coherent, and(4) still applies to its diagonal charge operator.

There is a simultaneous physical witness with d_c=2 for ALL staircase cycles(2): put edge phase -1 on every link crossing the periodic z cut and +1 elsewhere. Its only flat holonomy is pi in the z direction. Every staircase cycle winds once in z, so exp(i Phi_c)=-1, and every odd charge gives W^(N_c)=-I. Tree-gauging this connection gives an actual point of the physical cycle torus. No scalar-charge surrogate is involved.

## 3. Missing B sites and broken rings

For a fixed B mask S, delete any b_l not in S. An input dark A hole must have both neighboring b_l occupied, so its amplitude vanishes at the two ends adjacent to each deleted B. The map from these allowed A holes to occupied intermediate B holes is a direct sum of alternating finite chains, plus full cycles if none were deleted.

On a chain with r occupied B sites, there are at most r-1 allowed A-hole variables. Each endpoint B row contains only one variable, and all edge maps are unitaries between the full charge fibers. Eliminate successively from that row. If v=Kx, the jth variable obeys ||x_j||<=sum_(i<=j)||v_i||, hence ||x||<=r||v||. Thus the map is injective, with lower bound at least1/L. Further dark restrictions only reduce its input space.

The reverse map needed below, from occupied intermediate B holes into ALL A holes on the next plane, has r variables and r+1 rows on such a chain. The same endpoint elimination gives the same1/L bound. For a full cycle its adjoint has the same lower singular value as the square invertible map(3).

These comparisons use a separate proof-space tag for the ORIGINAL B mask S. It prevents identifying intermediate W0 words that happened to arise from different masks. This tag is never an observed mark, a changed physical Hilbert space, or an assumed invariant mask. It is simply a direct-sum factorization of the already canceled off-diagonal block(1), which preserves S. Taking the global F* map instead would incorrectly mix those tagged intermediates and reintroduce the previously exposed failed factorization.

## 4. An injective highest-layer block of the actual H

Let P_j project onto A holes with y+z=j modulo L, and D=1_(G=0). A two-hop move changes this layer by at most2. To move from j to j+2, both steps must be transverse positive y/z steps, and their shared B lies on layer j+1. For each fixed mask S, (1) on a dark input factors exactly as

 P_(j+2) H D P_j=K_out* K_in D P_j.                      (7)

K_in is the two-matching map from plane j to occupied B intermediates on j+1. K_out maps A holes on plane j+2 into those same tagged intermediates, using negative y/z directions. Both split into the staircase rings and broken chains above. No other input/output path has this layer change. In particular, the compensation and same-hole B reshuffles do not contribute to(7).

Let eta(theta) be the minimum of1/L and every d_c(theta)/N_c needed for these finitely many rings, over all x,j and the two matching orientations. Then

 ||P_(j+2) H D P_j v||>=eta(theta)^2 ||D P_j v||.         (8)

The inequality is over arbitrary superpositions of masks and charges: (7) preserves S and its original S output summands are orthogonal. The proof-space tag is removed on that output. It is not an assumption that H itself preserves S at other hole layers.

The exceptional set eta=0 is contained in the finite union

 q Phi_c=0 modulo2pi,  q odd, 1<=|q|<=2L-1.              (9)

Each Phi_c is a nontrivial integer cycle character. This union has Haar measure zero; alternatively its defining Laurent product is nonzero at the simultaneous pi-z witness above. Thus eta>0 for almost every physical phase. At that explicit witness eta>=2/[L(2L-1)].

## 5. Slab-confined dark eigenvectors are excluded

Suppose a fiber vector satisfies

 H(theta)psi=lambda psi,  Gpsi=0,
 P_j psi=0 outside one interval of at most L-4
 consecutive y+z layers.                               (10)

This statement permits arbitrary B-mask and charge superpositions. Rotate the layer origin so the interval is0,...,w with w<=L-5, and take the largest j with P_j psi nonzero. The output layer j+2 is outside its support. No lower occupied layer can reach j+2 by wrapping around the periodic cut: the omitted gap has at least FOUR layers and the hopping range in this coordinate is2. Thus the entire output eigenvalue equation at that layer is

 0=P_(j+2)(H-lambda)psi=P_(j+2)H D P_j psi.

Equation(8) forces P_j psi=0, a contradiction. Repeating the same argument is equivalent to peeling the maximal layer. Therefore(10) has no nonzero solution away from(9).

The gap of four layers is deliberate. Merely two omitted layers would allow an opposite-side two-hop contribution into the same output row and would not justify the argument. No Euclidean-ball or unaliased-height shortcut is being used.

For the known seven-layer strip plus one parity B site, every dark hole lies in the five inner layers. An A hole on either adjacent layer has two distinct outward B neighbors beyond the strip, and the single parity site can fill at most one. Further exterior holes also have an empty neighbor. For L>=16 these five layers satisfy(10). Hence no dark eigenbranch confined to that B-support family persists at almost every phase, even if its charge coefficients and allowed masks depend on phase. The exact flat-phase plane remains possible at the exceptional set(9), consistently with the old construction.

## 6. Why this is not source stability

The full phase problem allows eigenvectors with hole support spanning the torus and B masks extending outside the strip. Equation(10) does not cover them. An eigenbranch through an exceptional flat-phase vector could leave the strip support as its phase changes; that possibility is not excluded. Nor does absence of a slab-supported eigenvector imply that a slab-supported INITIAL source has zero projection onto a spatially extended dark spectral subspace. Linear combinations of extended eigenvectors may be local at one instant.

Thus the result supplies a literal full-charge magnetic continuation test and a necessary spatial property of any persistent dark eigenbranch. It is not full almost-everywhere observability, strong absorption of the actual positive source, a source probability estimate, a finite-spin theorem or a bound on the checked crossover mass. Those claims remain open. A separate exact monodromy control may corroborate the primitive charge/field identity; it cannot replace the all-charge argument(4), the canceled block(7), or the missing global observability proof.
