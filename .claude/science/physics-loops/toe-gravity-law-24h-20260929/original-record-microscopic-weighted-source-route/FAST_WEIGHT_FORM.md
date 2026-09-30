# Exact leading-fast weighted field form

Author analytic calculation; not independently checked. This file establishes a relative form, not common-positive-time microscopic convergence. The full original normalized spin words and compensation gates are used. The rotor version is a finite-support quadratic-form calculation only unless a domain closure is supplied separately.

Let f(a,e)=2^(-d(a,a(e))), Phi_a=2756+sum_e f(a,e)E_e² and X=sum_a w_a Phi_a, exactly as in WORKING_01. Let

    D2=C_S+[F,F*],  F=sum_a F_a,
    C_S=sum_a(F_a*F_a+D_el,a/[S(S+1)])Q_gate,a.

All operators in this note are finite matrices on an even torus at finite integer spin. The claim is the uniform two-sided form inequality

    -210000 X <= i[D2,X] <= 210000 X.                 (F1)

It is compatible with a nonzero current on a zero-loss subspace. It does not dominate the current by loss.

## Exact row classification

Expanding the actual coefficient gives

    D2=sum_a F_a F_a* +sum_a F_a*F_a(Q_gate,a-1)
          +sum_(a!=c)[F_a,F_c*]+diagonal electric term. (F2)

In the cross sum the second product is obtained by interchanging dummy indices in F*F. Stars with no common B site commute. Both factors in each remaining product use the same shared B vertex; all other edge pairs cancel in the commutator. The diagonal electric coefficient commutes with X.

There are exactly three types of offdiagonal elementary two-hop paths, with absolute coefficient at most1 for each path, including all spin-boundary zeros:

1. F_h F_h* acts only when h is an A hole. It leaves the A mask fixed and reshuffles at most two B sites/links in that star. At most36 elementary paths leave a basis input per h.
2. F_a*F_a(Q_gate,a-1) acts only when a is occupied and a different hole h lies at A-distance two from a. It leaves the A mask fixed. Assign the term to one such hole, for example the lexicographically first in a fixed torus coordinate system. There are18 possible a per assigned h and at most36 elementary paths per a, hence648 paths per h. This assignment is only a counting proof and changes no operator.
3. [F_a,F_c*] can act only when c is an A hole and a is occupied; it moves the hole from c to a. Their distance is two. A pair of distinct A sites has at most two common B neighbors; there are18 possible a per c. Two product orders give at most72 elementary paths per input hole c. In an occupied shared B state its charge may change, which is allowed and does not change this count.

The norm bound on each path uses the actual normalized integer-spin raising/lowering coefficient, at most1. A specified occupied matter site has a single charge, so a given edge contributes no extra sign multiplicity to an input row. Cancellations between paths can only lower the absolute row estimate. Thus at most756 paths are assigned to each input hole. No bound on total B count or static B component is used.

## Weight change per path

Every changed link has its A endpoint at distance at most two from the assigned input hole h; at most two links change, each by a unit. A transfer of the hole itself is at most distance two. For fixed unchanged fields,

    |Phi_a-Phi_h| <= 3 Phi_h  whenever d(a,h)<=2.

Indeed f(a,e)/f(h,e) lies between1/4 and4, and the constants in Phi cancel. After the hole-mask change, the coefficient of E_e² in X is sum_(occupied holes u)f(u,e)<=27. For either unit shift,

    |2sigma E_e+1| <= E_e²+2 <= 5 Phi_h,

since f(h,e)>=1/4 and Phi_h>=2756. Therefore the total field contribution to the change of X is at most270 Phi_h, and the optional hole-position contribution is at most3 Phi_h:

    |X(output)-X(input)| <=273 Phi_h(input).          (F3)

The fields in Phi_h on the right are the input fields. In the field step the coefficient sum is evaluated after changing the hole mask; it is still bounded by27. No commutation of a field shift through an unbounded weight is hidden.

For every physical basis input alpha, combine (F2)-(F3) to obtain

    sum_beta |(D2)_(alpha,beta)| |X_beta-X_alpha|
        <=756*273 X_alpha=206388 X_alpha.            (F4)

Terms returning to the same X value contribute zero. The matrix i[D2,X] is Hermitian and has symmetric absolute entries. Thus 2|psi_alpha psi_beta|<=|psi_alpha|²+|psi_beta|² turns (F4) into (F1), with the deliberately rounded210000. This proof is valid on the full carrier and on its Gauss restriction, and is unaffected by a reference ancilla.

## Actual leading-fast consequence

For the exact leading-fast GKSL generator

    B2*=i delta[D2,.]+kappa sum_mu D[j_mu]*,

the previously derived original-jump form(J3) and(F1) imply

    B2* X +(kappa/4)A_Phi <=210000 delta X,
    A_Phi=sum_(a,mu at a)j_mu* Phi_a j_mu.            (F5)

The coherent-edge version uses the original unnormalized coherent mark; the cross terms vanish in this diagonal weight because the two final A charges are orthogonal. No new sign or grade measurement is introduced.

At leading-fast time u (physical time t=epsilon²u), its actual CP ensemble obeys

    <X>_u <= exp(210000 delta u)<X>_0,
    (kappa/4)integral_0^u <A_Phi>_v dv
       <=exp(210000 delta u)<X>_0.                   (F6)

The second bound follows directly by multiplying(F5) by the integrating factor, or by integrating(F5) and the first bound. It does not need a loss gap. The constants are intentionally very loose. These are statements about the complete original leading-fast law, not the full microscopic law; normal-form remainders, actual preparation and return of physical weights still need to be handled for that extension. In particular exp(C t/epsilon²) is not a uniform common-positive-time estimate.

## Evidence scope

The geometry count18 comes from the six axial distance-two and twelve diagonal distance-two A neighbors. Two common B sites is the diagonal maximum; axial pairs have one. The proof above is analytic and includes boundary zeros. The earlier actual circulation-seeded zero-loss current is compatible with(F1) because X is positive there. No fresh numerical run is claimed for this form. A microscopic initial-layer extension is being investigated separately and is not a premise of(F1)-(F6).
