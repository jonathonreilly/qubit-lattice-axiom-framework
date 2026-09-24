# Personal reconstruction of microscopic birth energy beyond one star

2026-09-24, unsealed root derivation. Reconstructs the earlier unpublished
MICROSCOPIC_BIRTH_ENERGY_PLAN rather than promoting its conjecture unchanged.
The original instrument and full fast generator remain fixed. An independent
PRE has been requested without these formulas or numerical coefficients.

Let h=W+epsilon T+epsilon² C_S, H=delta epsilon^-4 h, T=-(F+F*),
F=sum_a F_a, P=Pi0, A=Pi1 T P=-F P, M=A*A, Z=Pi2 T Pi1 T P=F²P.
C_S preserves W, is uniformly bounded at fixed graph, and has P block
C0=M+Q_S, Q_S=D_lambda/[S(S+1)] for the supplied electric family.
Let U_epsilon be the canonical direct rotation from P to the exact low Riesz
band of h. For each S it is analytic near epsilon=0, with uniform radius and
Taylor bounds because W has unit gap and T,C_S are uniformly bounded.

Parity J=(-1)^W gives h(-epsilon)=J h(epsilon) J and the same covariance of
the canonical U. Thus the P block of U* h U has only even powers:

    h_low=epsilon² Q_S+epsilon^4 H4_S+O(epsilon^6).

U P=P+epsilon F P+epsilon²[Z/2-M/2]+O(epsilon³), with the Z and M terms in
Pi2 and P respectively; there is no Pi1 second-order term. The actual mark j
low-low block is epsilon B+O(epsilon³), B=jF P=-PjA. Its first high block is

    Pi1 U* j U P = epsilon² R_j+O(epsilon^4),
    R_j=jZ/2+A B_j.

Other high blocks start Pi2 at epsilon³, Pi3 at epsilon4, etc. W-changing
selection rules and parity matter for uniform remainder estimates.

For an edge mark at A center a, different outward F_c commute with j_a and
F_a, including shared B targets: two attempted hard-core B creations vanish
in either order. F_a²=0 and j_a kills P unless a has emptied. Consequently

    R_j = -F_a j_a F_a P = -F_a B_j.                       (candidate exact identity)

This is a repeated local move at the same A center. It requires a third empty
B destination after the first transport and pair formation. Degree-two rings
therefore have zero coefficient on an all-A-full/B-empty input. That is a
counterexample to extending the star's divergent energy cost universally;
it does not say their complete microscopic energy is zero.

For any normalized psi in P and nonblocked mark with b=||B_j psi||² bounded
below, write r=||R_j psi||² and q= <B_j psi,Q_S B_j psi>. The proposed uniform
microscopic conditional moment expansion is

    mean H_after = delta epsilon^-2 (q+r)/b + O(delta),
    Var H_after  = delta² epsilon^-6 r/b + O(delta² epsilon^-4).

For fixed-field vectors Q_S B_j psi ->0, the leading mean coefficient is r/b.
For flux proportional to S the slow-band q contribution cannot be discarded.
The variance's leading high-band coefficient still has r/b because the slow
H scale is epsilon^-2 rather than epsilon^-4. Do not confuse this with the
previous effective-target high-flux variance proportional to n^4.

The full instantaneous energy derivative is entirely the dissipator acting
on H; the Hamiltonian commutator vanishes. The proposed operator expansion on
the dressed P band is

    P U* L_micro^*(H) U P
      = kappa delta epsilon^-2 [D_B^*(Q_S)+sum_j R_j*R_j]
        + O(kappa delta),
    D_B^*(Q)=sum_j B_j* Q B_j - {sum_j B_j*B_j,Q}/2.

Reason: jbar_low=epsilon B+epsilon³B3+..., h_low=epsilon²Q+epsilon4H4+...;
jbar_high=epsilon²R in Pi1 plus higher blocks. The unscaled gain is epsilon4
[B*QB+R*R]+O(epsilon6); the loss is epsilon4{Gamma_B,Q}/2+O(epsilon6).
Multiplication by kappa delta epsilon^-6 gives the displayed expression.
Parity removes an epsilon5 remainder. This is operator norm at fixed graph
uniform in S and lambda if the analytic bounds are made explicit. It avoids
needing the input to be an exact H eigenstate. Canonical dressed preparation
is supplied, not the bare P input or the old star d for all changed models.

At joint epsilon² C=delta/K, C=S(S+1), rewrite the leading derivative as
kappa K D_B^*(D_lambda)+kappa K C sum_j R_j*R_j + O(kappa delta).
The first term is the actual slow-band energy redistribution, and the second
is the microscopic high-band contribution missing from an effective-only
energy interpretation. Both can be order C at high flux.

For an all-A-plus/B-empty rotor basis word at degree d_a:

    ||B_(ab,+)||²=||B_(ab,-)||²=d_a-1,
    ||R_(ab,+)||²=2(d_a-1)(d_a-2),
    ||R_(ab,-)||²=(d_a-1)(d_a-2).

The plus amplitude has two equal histories for each unordered pair of the
other destinations. Minus histories have different final negative-charge
locations and remain orthogonal. A coherent edge mark adds orthogonal
plus/minus R outputs, so total R² is their sum. Total rotor coefficient
sum_j||R_j psi||² = sum_a 3d_a(d_a-1)(d_a-2) for either instrument.
Degree-three star gives18; cube has four A centers and gives72. Degree-two
cycle gives0. No second-pair assertion is made about the six-site cycle.

Cube high-flux finite-spin calculation to verify with fresh primitive code:
one square circulation n, two affected A centers have incident fields
(n,-n,0), two unaffected A centers have (0,0,0), all oriented A->B.
Put u=n²/C, v=n/C, a=1-u-v, b=1-u+v. For one affected center,
m=[b,a,1] are squared outward-plus shifts; p=[a,b,1] are plus birth shifts.
Summing original resolved marks gives

    R_center²=6(a²+b²+ab)=18(1-u)²+6v²,
    R_cube²=72-72u+36u²+12u/C.

The previously sealed effective D drift (dimensionless B dissipator) is
-32n²(3-3u+u²)-16n²/C. Its use requires rechecking exact source/current
word conventions and preferably reproducing from primitive shifts.
Combining would give, for lambda0,

    (d mean H/dt)/(kappa K C)
      =72-168u+132u²-32u³-4u/C+O(1/C).

For n/S->x, u->x², this tends to f(u)=72-168u+132u²-32u³. It decreases
from72 to4 on0<=u<=1, since f'=-24(4u-7)(u-1). Thus negative slow-energy
drift alone would give the wrong sign of the full leading microscopic power.
This polynomial and the exact spin R sum still need controls and independent
comparison before any claim is sealed.

For the electric family, D_lambda=(1-lambda)D+lambda E2. A birth changes
only finitely many edge fields by one, so E2 jump drift is at most O(S), hence
its value/C vanishes along n/S->x; it may have an even sharper cancellation.
The candidate high-flux leading power is therefore

    kappa K [72-72u+36u² -32(1-lambda)u(3-3u+u²)]

after division by C. It stays >=4kappa K for0<=u<=1,0<=lambda<=1.
This is a supplied-model, supplied-dressed-input initial-power statement,
not finite-time accumulated energy, heat identification or native selection.
Exact finite endpoint marks can block; normalized selected formulas require
b>0, whereas the summed derivative does not. No density-only inference is
permitted. The canonical low-band gap and parity proof are load-bearing.
