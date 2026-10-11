# Refinement: use the proved particle stopping region for capacity coupling

Root derivation, 2026-10-11. Proposed strengthening of the earlier qubit/fluid
composition resource ceiling; the earlier complete construction is unchanged
and remains a fallback. This refinement needs its own independent check.

The particle theorem already gives a target stopping time tau such that
F_zv=n_zv/(Nw)<=2M_v strictly before tau, and P(tau<=L)<=C_prob delta^2.
Use that stopping event in the coupling to the finite-capacity averaged
process, instead of bounding every rate defect over all mass-N configurations.
No positivity or small-noise event is assumed with probability one.

Let G be the target count generator and G_K the qubit theorem's averaged
finite-capacity generator, with K>=N. They have identical transitions with
rates

    hop: (b/ell)|v_d| n_zv [1-n_(z+d),v/K],
    forward collision: (c kappa_r/(Nw)) n_i n_j (1-n_k/K)(1-n_l/K),

and the corresponding reverse collision. All rates of G_K are no larger
than the corresponding G rates. Couple them using common events at the
smaller rates until the first discrepancy; excess target events have the
rate deficit. Both processes start with the same exact multinomial count
law; K>=N makes every initial state admissible.

Before the target stopping time, direct substitution gives the uniform
hopping deficit

    sum_(z,v,d) (b|v_d|/(ell K)) n_zv n_(z+d),v
      <= (4 b N^2 w/(ell K)) sum_(v,d) |v_d| M_v^2
      = b N^2 w/(6 ell K).

The finite product weights give sum_(v,d)|v_d|M_v^2=1/24: in one dimension
sum M_1D^2=1/2 and sum |v|M_1D^2=1/18, so the three terms total
3*(1/18)*(1/2)^2=1/24.

For a reaction set p_r=M_iM_j=M_kM_l and define the fixed finite constant

    T4=sum_r kappa_r p_r (M_i+M_j+M_k+M_l).

Using 1-(1-x)(1-y)<=x+y for 0<=x,y<=1, both collision directions together
have deficit at most

    (c kappa_r/(Nw K)) [n_i n_j(n_k+n_l)+n_k n_l(n_i+n_j)]
      <= (8c kappa_r N^2 w^2/K) p_r (M_i+M_j+M_k+M_l)

in each cell. Sum over 1/w cells. Thus the stopped total rate deficit is

    Delta_local = C_local/K,
    C_local=N^2 w [ b/(6ell)+8c T4 ].                    (R1)

This uses exactly the target's pre-stop state. If a discrepancy has not
already occurred, the finite-capacity state is identical, so the same bound
applies to its coupling clock. The probability of any discrepancy before
L wedge tau is at most L Delta_local by the stopped compensator. On the
joint event of no discrepancy and tau>L, the two complete count paths agree
through L and satisfy the original particle error event. Hence

    P(finite-capacity count path fails the particle error bound)
       <= C_prob delta^2 + L Delta_local.              (R2)

The local-qubit fast-averaging path theorem still uses its global B_K and
tau_mix; no favorable-state assumption is inserted into that distinct bound.
Couple it to G_K with error at most tau_mix B_K(1+L B_K)/nu. Combining this
coupling with (R2), without counting target exit a second time, gives

    P(actual associated qubit count path error > C_path delta)
       <= C_prob delta^2 + L C_local/K
                            +tau_mix B_K(1+L B_K)/nu.  (R3)

Keep all definitions and physical scope of the first composition draft, but
choose K_req=max(N,2,ceil(2L C_local/delta^2)) before selecting S,K, and
keep nu=2 tau_mix B_K(1+L B_K)/delta^2. Then (R3) is bounded by
(C_prob+1)delta^2. Quantum finite-time joint readout equality transfers this
same event as before. There is no assertion that fast mixing itself only
visits favorable microscopic configurations.

## Refined explicit resource ceilings

Retain c_m=2pi+2, c_ell=2pi/c_m, N in [delta^-19,2delta^-19], and w<=
(2pi)^-3 delta^6. Then for b=delta^-1, c=delta^-2,

    C_local <= C_local0 delta^-35,
    C_local0=4(2pi)^-3 [1/(6c_ell)+8T4].               (R4)

The hopping term has power -35 and the collision term -34. Define

    C_req=max(2,2L C_local0+1),
    C_S=max(1152,sqrt(2(C_req+1))+1), C_K=C_S^2/2,
    D0=27c_m^3, c0=C_K(8C_S+19),
    B0=54C_K c_m^3/c_ell+K_Sigma C_K^2 c_m^6,
    T0=c0 max(2+log D0+log C_K,43),
    V0=2T0 B0(1+L B0).

The same ceiling/floor argument now gives

    K_req<=C_req delta^-37, S<=C_S delta^(-37/2),
    K<=C_K delta^-37,
    m^3 S^3<=c_m^3 C_S^3 delta^(-123/2).               (R5)

The global B_K is unchanged as a formula. Its hopping and collision powers
are respectively -46 and -69, so B_K<=B0 delta^-69. The BFS Poincare ceiling
is c_KS<=c0 delta^(-111/2). The fixed-total-number entropy bound n_*<=
2delta^-19 then gives

    tau_mix<=T0 delta^(-149/2)[1+log(1/delta)],
    nu<=V0 delta^(-429/2)[1+log(1/delta)].             (R6)

The logarithmic coefficient is 6+37=43 after enlarging delta^-19 terms;
all constants are independent of delta. Active sites and fast marks are
O(delta^-43). Individual hopping and collision rates are respectively
O(delta^-40) and O(delta^-63). These are sufficient polynomial ceilings,
with the same explicit supplied-dynamics, variable-volume, large-rate and
permanent-Record limitations as the previous construction.
