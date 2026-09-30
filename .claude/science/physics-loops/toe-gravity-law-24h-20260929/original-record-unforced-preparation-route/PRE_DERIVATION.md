# Derivation checkpoint before new controls

2026-09-30. No new science computation has been run. This is the author's own first derivation, not an independent receipt.

The complete checked fast-defect receipt4d9a9d35 has now been read. It supports necessary local stationarity/darkness only and is not needed to prove the present initial-term bound. The parent suggested checking the coloring issue; the translation average below arose in resolving that issue. The earlier initial-layer, initial-cluster, normal-form, finite-spin-response and connected-source arguments are known prior work, not undisclosed independent discoveries here.

Let E_S(u)=exp(u K_S). The exact identities [H2,W]=0 and [W,j]=-j imply E_S*W<=W, W covariance and E_S*(w_a)P0=0. In the W1/NB1 rotor sector every hole has at least five vacant B neighbors, so G>=10 and the no-event norm is at most exp(-5 kappa u). The complete checked one-hole operator comparison can be specialized to this strict loss; its weighted proof then needs no large-torus height lemma. On the one-hop source Q=1+sum|E| equals2, and terminal spin error is O(1/[S(S+1)]) times the source norm.

For a logarithmic fast time u*, local Lindblad locality replaces E_S*(w_a) by a ball observable with error e^(v u*-D) times a quadratic shell factor. Enlarge the ball by the fixed circuit cone. Delete only circuit gates outside that enlarged cone, obtaining an exact unitary Y_D. Initial expectations of the truncated observable coincide exactly. A SECOND locality comparison returns to the complete fast generator with initial vector Y_D Omega. Absorption is never inferred for an artificially cut boundary generator.

If m is the number of retained gates, real-parameter unitarity gives

    Y_D Omega = Omega + epsilon v_D + r_D,
    ||r_D|| <= C epsilon² m²,  ||v_D|| <= C m.

Every first-derivative gate is an elementary -F+F* term. Hence v_D lies exactly in W1/NB1, has only plus occupied charges, and Q v_D=2v_D. It is a coherent sum, not a mixture. Higher sectors remain in r_D. Positivity and the zero P0 block imply

    <Y_D Omega,E_S*(w_a)Y_D Omega>
       <=2epsilon² ||Z_S(u)v_D||²+2||r_D||².

Thus no O(epsilon³) cross-term loss is necessary. With u*=2 log(1/epsilon)/(5kappa), D>=v u*+8 log(1/epsilon)+10, m<=C(1+log(1/epsilon))³, and the coupled spin scaling, every site's hole expectation at u* is at most C epsilon4(1+log(1/epsilon))12, uniformly in volume. This uses a LOCAL expansion only, even when the full preparation has extensive excitation number.

An arbitrary coloring is not translation covariant. The safe late-time consequence of W monotonicity alone is a density bound. A fixed-period choice gives an individual local bound on compatible tori, at the cost of the fixed number of A sites in its period cell. For all tori let Y_z=T_z Y T_z* over the A-preserving translation group. The first diagonal coefficient is the same H2 for each z: elementary outward hops commute, so first-order gate ordering contributes only a neutral second-order gauge. Every exact microscopic Duhamel identity can be conjugated by Y_z and then averaged. The averaged REFERENCE initial state is translation invariant; this does not change the actual physical state on the left side. A z-dependent bounded hole-corner test is bounded by a common local hole projection before averaging. This closes the averaged initial term, but proves no late local assertion for a single arbitrary coloring.

For physical time t, the interval before epsilon²u* costs O(epsilon² log(1/epsilon)) in the epsilon^-2 integrated hole functional. Later times cost O(T epsilon² log(1/epsilon)^12). Continuous forcing R_(epsilon,z) sigma_z(s) in the exact Duhamel formula is signed, contains off-grade original-mark interference, and is not bounded by this argument. Extending the preparation estimate to that forcing would require new state/source control and must not be obtained by naming it another initial state.
