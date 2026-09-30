# Local count tilt: an exact failure of bare-loss domination

This is a distinct attempted local extension of the global positive-moment argument. It does not use that theorem as a premise. Put A_theta=alpha W+theta n_b0, with alpha>theta>0, Q=exp(A_theta), and b0=(1,0,2). Every bare original birth lowers A_theta, so its adjoint dissipator is nonpositive on Q. A tempting sufficient inequality for a local source moment is

    Q^(-1/2) i[delta H2,Q] Q^(-1/2) <= c G,       (L1)

where G is the total original bare loss. With a suitable margin alpha-theta, such a bound could absorb the epsilon^-2 Hamiltonian current into the fast negative dissipative drift. The actual model violates (L1) at every theta>0 and every finite c. The violation is already inside the physical one-hole/seven-B sector; it is not the full-B example.

Use the frozen DARK_WORD source component from the earlier microscopic packet. Let h=0, c=(1,1,0), a=(1,0,1), e=(2,0,1). From bare Omega select the internal components of the actual source word:

    c -> (1,0,0); birth+(c,(0,1,0));
    a -> (0,0,1); birth+(a,e);
    h -> (0,-1,0); birth+(h,(-1,0,0)); h -> (0,0,-1).

All initial link changes are 0 to +/-1, every Gauss equation holds, and this component has nonzero coefficient in the full original mark product, including the positive-grade -F_h j F_h coefficient. Call the resulting normalized basis vector gamma. It has W=1, seven occupied B sites, every B neighbor of h occupied and G gamma=0. In particular e is occupied by a minus charge, a by plus, and b0 is vacant.

Apply the two actual hops a -> b0 and then e -> a, obtaining beta. The first link changes0 to-1; the second changes+1 to0. They have unit normalized-spin weight for every integer S>=1. Both endpoints remain physical, with W=1, seven B occupants and all six neighbors of h occupied. Hence G beta=0, for both original instruments including their actual spin factors.

For the exact same-hole fast block, the checked source identity is

    P_h(H2-Delta_S)P_h
           =P_h(F_h F_h^* - sum_(dist(a',h)=2) F_a'^* F_a')P_h.

Delta_S is diagonal. The selected two-link output is unique to -F_a^* F_a. Its compensation gate Q_a is zero because h is a hole at distance two. Thus, for every S>=1 and for the rotor,

    <beta|H2|gamma>=-1.                            (L2)

This holds with all other H2 outputs retained. There is no projection of the original instrument or replacement of a link translation by a scalar model. The uniqueness of the two changed oriented links establishes the matrix element.

On the two-dimensional span of gamma,beta, Q has eigenvalues e^alpha and e^(alpha+theta). The compression of the normalized current in(L1) is

    [[0, -2i delta sinh(theta/2)],
     [2i delta sinh(theta/2), 0]],

up to the harmless ordering of the two vectors. Its eigenvalues are +/-2delta sinh(theta/2), while the compression of G is zero. Thus the positive eigenvector violates(L1). The same argument refutes a norm bound by G^(1/2). Bare dissipative negativity cannot absorb this current because it vanishes on that entire span.

The source component is not an observed extra record, and its algebraic accessibility is not a lower bound on its probability from bare Omega. The seven-B sector is within the independently checked GLOBAL N_B<=9 absorption theorem: propagation over time can reach bright states. There is no conflict. The result rejects only direct instantaneous local-tilt absorption by bare loss, not a corrector involving H2, time-integrated observability, source-weighted cluster expansion, or the M4 local limit.

## Control price and checks

One foreground standard-library sparse test, hard CPU25 seconds, envelope<=30CPU/150MB, BLAS1, deadline and both STOP checks. Reuse the earlier author's own sparse charge/field representation with explicit provenance; no independent-check label. Reconstruct the selected original source word, both selected unit-spin paths and the complete same-hole rotor block. Test Gauss, loss zero, N_B, the offdiagonal -1, and the reverse Hermitian matrix element. An omitted compensation gate and the wrong commutator sign are analytic mutation controls: retaining a +F_a^*F_a term would cancel the witness, while reversing the actual negative term flips its sign. The latter still gives a positive eigenvalue and does not repair(L1).
