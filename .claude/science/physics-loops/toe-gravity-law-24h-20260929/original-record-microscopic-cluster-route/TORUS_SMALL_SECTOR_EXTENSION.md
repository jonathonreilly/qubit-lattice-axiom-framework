# Bounded periodic-sector geometry extension, secondary attempt

This is a small extension of the already checked one-hole absorption argument, not the primary result or a proposed source milestone. During this derivation root notified us that a separate author had claimed all-finite-k absorption on Z3 by a clipped-height method, with a periodic obstruction near saturation; that proof has not been read or imported here and its independent check is ongoing. The present result only concerns even cubic TORI L>=6, actual ROTOR coefficient, W=1 and GLOBAL N_B<=12. Physical Gauss/record parity makes the newly added physical odd case k=11. It gives no local sparse-background theorem or finite-spin uniform transfer.

## Complete source and row argument

Use H=C+[F,F^*], C=sum F_a^*F_a Q_a, and the exact original loss G=2 times the number of vacant B neighbors of the hole. Both actual instruments have this loss; their labeled recycling maps remain different and are retained in the absorbing output. The checked same-hole and off-hole block identities give

    P_h H P_h= P_h[F_hF_h^* - sum_(dist(a,h)=2)F_a^*F_a]P_h,
    P_a H P_h=P_a[F_a,F_h^*]P_h.

With ||F_a||<=6, the same-hole norm is at most19*36=684. Six axial and twelve diagonal neighbor centers give30 shared-B paths; each commutator path has norm<=2. Schur row and column bounds therefore give ||H||<=M=744 on the COMPLETE one-hole rotor sector, uniformly in volume, charge and electric fields. Also0<=G<=12. No electric cutoff is taken.

Let D=1_(G=0). A dark hole h requires all six vertices N(h) occupied. Any three distinct cubic A stars have union at least13. Indeed a disjoint pair gives union>=18-2-2=14. If one nonempty pair overlap is one, total pair overlaps are at most5, giving union>=13. If all three pair overlaps are two, set h=0 and c=(1,1,0) by a signed permutation. The third center can only be (1,0,+/-1) or (0,1,+/-1), and the three stars share a B vertex. Inclusion-exclusion again gives13. The local classification is unchanged on L>=6. Thus a mask of at most12 occupied B vertices has at most TWO possible dark A centers.

For a fixed dark h consider its six axial centers c=h+/-2e_i. Each N(c) contains exactly one B vertex in N(h); the remaining set E_c has size5. Distinct E_c have intersection at most one: normally zero, with an opposite-axis one-site alias on L6. There are at most6 occupied B vertices outside N(h). Two axial outputs with at least5 occupied neighbors would each need at least4 occupied vertices in E_c, requiring at least4+4-1=7 extras. Therefore at most one axial output has5 or6 occupied neighbors. The other at least5 have G>=4.

The only OTHER possible dark A center h' can be distance two from at most TWO of the six axial centers c. This is the elementary intersection of the six radius-two center neighborhoods, excluding h itself. In the unwrapped lattice the maximum is attained by a face-diagonal h'; finite L6 and L8 aliases also have maximum two. The attached exact control enumerates every candidate in those exceptional periods, while L>=10 has the unwrapped local classification. Hence at least THREE of the axial outputs have G>=4 and no competing dark source center.

For each such selected row, refilling h from its unique shared B and emptying c into that B is the +1 rotor matrix element of [F_c,F_h^*]. The reversed same-B order is blocked. It defines a charge/field isometry with a unique inverse, including Gauss. A hole-changing term preserves the B mask, so no other dark center can feed the selected row. A same-hole term can move at most ONE B particle; a dark input with hole already at c would have six occupied neighbors and can leave at least five. It therefore cannot feed this output, which has at most four. This excludes interference from different B masks as well as different hole centers.

Project onto the union R of these selected output ranges. The ranges of different selected source rows are disjoint, and any selected output has its unique source. Thus

    ||RH psi_D||²>=3||psi_D||²,
    ||G^(1/2)H psi_D||²>=12||psi_D||².                  (T1)

R is only a proof projection, not a new observation. For arbitrary psi put x=||G^(1/2)psi||, y=||G^(1/2)Hpsi||. Since G>=2 on the bright subspace,

    sqrt(12)||Dpsi||<=y+sqrt(6)M x,
    ||psi||²<=y²/6+(M²+1/2)x².

Consequently

    G+HGH>=c0 I,       c0=2/(2M²+1)=2/1107073.        (T2)

## Explicit absorbing evolution consequence

Let Z(u)=exp[u(-i delta H-kappa G/2)]. The earlier independently checked elementary bounded-operator observability proof applies with precisely the new M,c0; it can be restated by the following constants:

    c_delta=min(1,delta²)c0,
    R0=delta² sqrt(12) M²/2,
    tau=min(1,sqrt(5c_delta)/(8R0)),
    c_U=c_delta tau³/64,
    a0=min(1/2,kappa c_U/(1+6kappa tau)²),
    C0=exp(a0/2), gamma=a0/(2tau).

For U(u)=exp(-i delta Hu), Taylor expansion of G^(1/2)U(u)psi through degree one has remainder norm<=R0 u²||psi||. The Gram matrix of1,u on[0,tau] has smallest eigenvalue>=tau³/16. Using(T2) and the remainder bound gives integral_0^tau||G^(1/2)U(u)psi||²du>=c_U||psi||². Duhamel U-Z and the Volterra integration norm<=tau transfer this to Z with denominator(1+6kappa tau)². The exact norm-loss identity then yields ||Z(tau)||²<=1-a0, and iteration gives

    ||Z(u)||<=C0 exp(-gamma u), u>=0.                  (T3)

All constants are positive and independent of torus size and actual rotor fields. Their numerical smallness is not a practical resource assertion. The original absorbing stack sqrt(kappa)j_m Z(u) is retained with its actual labels; it is not identified with the complete later-birth microscopic process.

The earlier checked electric-weight argument also transfers: H has bandwidth two in Q=1+sum|E| and norm<=M. Taking alpha=(1/2)log[1+gamma/(10C0 delta M)] perturbs the five-band conjugated generator by at most gamma/(2C0). Duhamel yields ||e^(alpha Q) Z(u)e^(-alpha Q)||<=C0 e^(-gamma u/2). The original jump stack has bandwidth one and norm<=sqrt(12); its three-band bound is3 e^alpha sqrt(12). The resulting integrated absorbed exponential-field norm is at most108 kappa e^(2alpha) C0²/gamma times the input exponential-field norm squared. This still REQUIRES that weighted input and concerns only the stated rotor sector.

## Control and scope

check_absorption_extension.py exhausts the relevant local geometry for Z3 and L6,8,10:153 nearby pairs per case, all66/81/84 possible competing centers, three-star minimum13, extra-set overlap0 or1, competing axial-row maximum2, and at least3 selected rows. Runtime0.079164CPU seconds/19,841,024 RSS bytes. This is geometry evidence; the operator identities, quantum injectivity, evolution and domain arguments above are analytic. The existing source-accessible seven-B dark word is inside the sector and poses no contradiction.

The result advances only a fixed GLOBAL-particle periodic case. On growing tori, the actual process has extensive N_B at positive time. One cannot substitute a sparse local neighborhood for this global hypothesis. Finite-spin high-field boundary zeros, local large-cluster source weights, multiple holes and marked microscopic comparison remain separate. This secondary extension is not used to close any of those gaps.
