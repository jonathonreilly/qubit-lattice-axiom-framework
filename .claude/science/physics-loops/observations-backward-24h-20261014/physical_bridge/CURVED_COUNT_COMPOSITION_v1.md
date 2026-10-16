# Exact curved-count Gram and explicit propagation-error suppliers

Date: 2026-10-15. Working companion to CURVED_COUNT_WORKING_v1.md. Root
personally computed these results; independent final-source checks are pending.

For L=3/5, t_i=7/5+i, gamma=(-1,3,-3,1), the derived transformed weights
give the following exact massless-propagation Gram:

    G0(H)=(646969 H^2-454020 H+98700)/(16200 pi).       (G1)

This is the reference propagation Gram with the CORRECT curved-background
count weights. It is not the actual curved/massive Gram and not a replacement
for curved proper-time labels. The curve is synthetic, with 0<=H<5/22 so
all four endpoints remain inside the displayed conformal chart interval.

For completeness, set d(t)=1-Ht and z=n.e1. The common-arrival kernel is

    H_z(tau)=sum_i gamma_i {
       [d(t_i-2L)+z d(tau)] 1_(tau<t_i-2L)
       +[-d(t_i)+z d(tau)] 1_(tau<t_i)
       -2z d(tau+Lz) 1_(tau<t_i-L-Lz) }.

The two station terms and spacecraft term are summed before squaring. The
outer pieces cancel by the exact gamma moments. All interval endpoints are
affine in z and all coefficients are affine in tau. Their ordering changes
only at z=-2/3,2/3. Exact polynomial time integration followed by exact
polynomial angular integration on[-1,-2/3],[-2/3,2/3],[2/3,1] gives G1 from
G0=(4pi)^(-1) integral dz integral H_z(tau)^2 d tau.

At H=0, G0=329/(54pi), precisely the norm of the difference of the two M6
coherent-count channels. Separate direct interval quadrature and direct
perturbed orbit/clock ODE evaluation support the implementation. The maximum
ODE-versus-weight response error in the declared synthetic cases is
2.16e-10; changing the arbitrary initial orbit/clock data changes the contrast
by at most3.83e-10 numerically. The exact initial-data cancellations follow
from the polynomial proof, not those floating tolerances.

## Conservative analytic suppliers for one actual count contrast

Use the initial conformal epoch0 for every comparison and T=22/5. Let
0<H<1/T, B>12, mu0=sqrt(B-2)H. In this stationary comoving reference beta=0.
The following uniform suppliers require no sampled supremum or field data:

    C0=|integral c_s|=0,
    C=||c_s||1 <=16L+8HL Delta =48/5+(24/5)H,
    Wsum=||W_s||1+||W_b||1 <=24 Delta^2=24,
    Wp=||W_s'||1+||W_b'||1 <=16 Delta=16,
    V_F=TV(W_s')+TV(W_b') <=32+16H Delta=32+16H.

To obtain C, write c_s=sum gamma_i d(t_i)[1_(s<t_i-2L)-1_(s<t_i)]
+2HL sum gamma_i 1_(s<t_i-2L). The first term has L1 bound16L; the
second uses integral|sum gamma_i 1_(s<t_i-a)|=4Delta. For each F_a^H,
its derivative is -d(s) times that step function. Hence ||F'||1<=4Delta
and TV(F')<=8+4HDelta, retaining outer/internal jumps. Because F is compact
with support length3Delta and both endpoint traces zero,
||F||1<=(3Delta/2)||F'||1<=6Delta^2. The sums for W_s,W_b introduce a factor4.

The cancellation-aware mass bound uses

    D_mass+M <=2T C+Wsum,
    E_mass <=T Wsum,
    epsilon_mass <= [(2T C+Wsum)sqrt((pi/2-4/3)mu0^3)
                     +2mu0 sqrt(T Wsum V_F)]/(sqrt(2)pi).             (G2)

The clock sits at the chosen spatial origin, so its spatial moment is zero.
This uses the same initial epoch0 as the time-varying-potential comparison.

For the potential error, the stationary suppliers reduce to

    G_F<=Wp, V_R<=Wp, R_L<=Wsum,
    C_F=2R[V_F+2(U0/mu0)Wp
                     +(U1/mu0+U0+U0^2/mu0^2)Wsum],
    epsilon_U <= [R S C sqrt(pi/(4mu0))
                     +2sqrt(R S Wsum(C_F+V_F))]/(sqrt(2)pi),          (G3)

where S,U0,U1,R are derived from the exact de Sitter V in the first note.
Thus the actual fixed-background field response has norm at most
sqrt(G0(H))+epsilon_mass+epsilon_U. These deliberately loose suppliers can
be improved by exact weight moments, but no improvement is needed for validity.

The endpoint coefficient dependence on H is explicit. This construction
does not establish a measured H, B, Q, residual, error budget or upper field
energy. It also does not assert that a flat-chart approximation controls
nonlinear or sourced scalar histories. The radio/clock readout, ideal coherent
hardware and candidate action still need empirical validation.
