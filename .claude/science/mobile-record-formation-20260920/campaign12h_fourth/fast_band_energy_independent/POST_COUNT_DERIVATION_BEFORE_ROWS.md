# Additional count reconstruction before author-row exposure

2026-09-24. Written after the root's POST brief and metadata seal were
received, but before reading the released author proof, controls or numerical
rows. The brief names the proposed coefficient; the derivation below uses
this task's frozen PRE model and fast-band proof. It is not blind to the
proposed answer, and is not counted as a new PRE.

Let v=B_first Omega/sqrt(b), r=R_first Omega/sqrt(b), c=||r||^2, and
V_S(s)=exp[(-i delta D_(1,S)-kappa Gamma_(1,S)/2)s]. Retain the actual
microscopic no-further-event state, transformed by the all-cluster Hamiltonian
rotation. The PRE gives, uniformly on compact s intervals,

    chi_0=v+O(epsilon^2),
    chi_1=epsilon exp(-i delta s/epsilon^2)V_S(s)r
                                                +O(epsilon^3),
    chi_2=O(epsilon^2).

After another birth the state is in N=8. At lambda=0 its Hamiltonian and
further jumps vanish, and its canonical cluster rotation is identity.
Therefore the transformed actual future jump is j U_6. Its columns are

    (j U_6)Pi_0=epsilon B_j+O(epsilon^3),
    (j U_6)Pi_1=j Pi_1+O(epsilon^2),
    (j U_6)Pi_2=O(epsilon).

The zero order on Pi_0, and the absent linear correction on Pi_1, follow
from W parity and the fact that the physical birth vanishes except on
N=6,W=1. Thus the future-jump source on the no-event state is

    epsilon [B_j v+exp(-i delta s/epsilon^2)j V_S(s)r]
                                                 +O(epsilon^3).

The exact future-birth probability is the integrated full jump intensity:

    P_8(epsilon^2 tau)=kappa integral_0^tau
                              sum_j ||j U_6 chi(s)||^2 ds.

After division by epsilon^2 its two nonoscillating terms are

    kappa tau sum_j ||B_j v||^2
       +kappa integral_0^tau <V_S(s)r,Gamma_(1,S)V_S(s)r> ds.

The cross term has exp(-i delta s/epsilon^2) times a scalar function with
uniformly bounded value and derivative, because D_(1,S), Gamma_(1,S), B_j
and j are uniformly bounded. One integration by parts bounds its integral
by O_T(epsilon^2), uniformly in S. It must be integrated before being
discarded; no pointwise jump-rate convergence is claimed.

The PRE loss identity turns the second nonoscillating term into
c-||V_S(tau)r||^2. The remaining primitive calculation is

    sum_j ||B_j v||^2 = 8.

It uses all actual future marks on the normalized first output, including
their within-mark interference. On these zero-field paths every spin step
is 0<->+/-1, so this coefficient is exactly independent of S>=1. The exact
control below checks every first cube mark and both future instruments.

Consequently the additional full-generator statement is

    P_8(epsilon^2 tau)/epsilon^2
       =8 kappa tau+c-||V_S(tau)r||^2+O_T(epsilon^2),

and strong convergence of the bounded fast operators gives the rotor limit

    P_8(epsilon^2 tau)/epsilon^2
       -> 8 kappa tau+c-||V(tau)r||^2.

This concerns the exact actual probability under the full microscopic
generator, with the original canonical first output, in a scaling limit.
It is not an equality to that expression at finite epsilon, a statement at
fixed positive physical time, or a complete distribution of event times or
conditioned records. It concerns the cube, where N=8 is physical, not a
six-cycle whose fully occupied sector is forbidden by its charge parity.
