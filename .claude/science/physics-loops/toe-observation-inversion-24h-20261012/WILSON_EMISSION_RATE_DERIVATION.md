# Wilson emission width — frozen author derivation

2026-10-12. New rate calculation before exposing it to the focused checker. The kinematic cubic/localization is now independently supported and is also known quartic LIV prior art; it is an explicit supplier here. No physical likelihood or interacting renormalization closure. Same w=1, a²=1−mu, 0<mu<1 spatial/continuous-time model. Mass and charge, canonical Fock space, transverse oscillator normalization, positive-band particle identification, squared-amplitude transition rule and golden rule are supplied.

## Exact one-photon vertex and normalization

For initial electron p, final electron q=p−k, the link-derived emission vertex is
 V_lambda(q,p)=a sum_i epsilon_i alpha_i cos((p_i+q_i)/2)
                 + beta_D sum_i epsilon_i sin((p_i+q_i)/2),
where beta_D is the Dirac matrix (not the scaling mass parameter), epsilon is a real unit polarization transverse to hat{k}_i=2 sin(k_i/2), and k is on the torus. The sine and Wilson hoppings use the same link. Its Ward identity is sum_i hat{k}_i V_i=h(p)−h(q).

Use four Euclidean Clifford matrices Gamma=(alpha_x,alpha_y,alpha_z,beta_D), d(p)=(a sin(p_i),mu+sum(1−cos p_i)), n_p=d(p)/e(p), and V=v.Gamma. With P_+(p)=(1+n_p.Gamma)/2, the sum over both initial and final spins is
 S_lambda=tr[P_+(q)V P_+(p)V]
 =|v|²(1−n_p.n_q)+2(n_p.v)(n_q.v).
This is not yet the unpolarized average: divide by2. The trace is nonnegative as a matrix squared norm, even when the dot-product expression is not termwise positive.

Let H_gamma=1/2 sum(Pi²+omega² A²), [A,Pi]=i, and the one-photon field coefficient be1/sqrt(2 omega V_box). With e_charge²=4pi alpha, the unpolarized electron rate is
 Gamma(p)=alpha/(4pi) sum_lambda integral_BZ [S_lambda/omega(k)] delta(e(p)−e(p−k)−omega(k)) d³k.
The initial-spin average is already in this prefactor; do not divide the trace again. Photon frequency is internal, unlike the fixed external-photon prefactor of pair decay. This formula is tree-level golden rule only; no independent Pauli/clover term or radiative matching is included.

## Small-momentum on-shell reduction

Fix a direction n, A=sum n_i^4<1, and p=r n, mu=b r² with fixed b>0. Define
 F_A(y)=y[(1−A)+(1−2A)y+(1−A)y²]/4,
 D(y)=F_A(y)−b².
The allowed interior interval(s) have D>0, with0<y<1. Parameterize final electron q=y r n+r² t, t.n=0, and photon k=(1−y)r n−r²t. At fixed y away from endpoints,
 Delta/r³=[(1−y)²D−|t|²]/[2y(1−y)]+O(r),
with the leading controlled limit and endpoint issues handled separately. The leading shell has |t|²=(1−y)²D.

At this scale the Wilson mass in the spinors matters: M(p)/e(p)=r(b+1/2)+O(r³), M(q)/e(q)=r(b/y+y/2)+O(r²). For a transverse basis e_lambda perpendicular to n, physical photon polarization has epsilon_lambda=e_lambda+r(t.e_lambda)n/(1−y)+O(r²). Summing the two polarizations gives
 sum_lambda S_lambda = r² M(y,t)+o(r²),
 M(y,t)=|t|²/y²+(1−y)²(b/y−1/2)²+2|t|²/[y(1−y)²].
The Wilson beta vertex begins at higher order in this transverse expansion but changes the exact Ward identity; the Wilson mass component of the spinors remains leading. Discarding that mass component would change the rate.

The measure is d³k=r^5 dy d²t, omega=r(1−y)+o(r), delta(Delta)=r^−3 delta(Delta/r³), and
 integral d²t delta([(1−y)²D−t²]/[2y(1−y)])=2pi y(1−y)
for D>0. Hence the proposed leading width is
 Gamma(rn)=alpha r³/2 integral_(D>0) I_A,b(y) dy +o(r³),
 I_A,b(y)=[(1+y²)/y]F_A(y)−2b²−b(1−y)²+y(1−y)²/4.
An explicitly positive equivalent integrand is
 I=y[(1−y)²D/y²+(1−y)²(b/y−1/2)²+2D/y].
The integral is polynomial after substituting F_A, with endpoints defined by a cubic. This is a prediction of a fixed supplied model, not a fitted formula. Endpoint uniformity at soft photons and numerical exact-shell verification remain obligations before theorem use.

## Sequential near-onset consequences, not finite-r equalities

First take the fixed-b small-r limit above, then approach onset. Let M_A=max F_A and delta=M_A−b²>0. For fixed A below the soft/hard switch A_c=(8−2sqrt2)/7, M_A=F_A(1)=(3−4A)/4 and F'_A(1)=2M_A>0. The interval is1−delta/(2M_A)<y<1 to leading order, and I~2[delta−2M_A(1−y)]. Thus
 Gamma~alpha r³ delta²/(4M_A),
 and radiated energy per unit time P~alpha r⁴ delta³/(24M_A²).

On the hard branch A_c<A<1, let y_c be the unique interior maximizer and K=−F''_A(y_c)>0. The collinear threshold spin weight is
 I_c=(1−y_c)² (b_c−y_c/2)²/y_c >0,
 since b_c=(y_c/2)sqrt[(1−y_c)/(1+3y_c)]<y_c/2.
Then Gamma~alpha r³ I_c sqrt(2delta/K). At the crossover both soft and hard onset tie in the leading kinematics; the hard contribution dominates this sequential small-delta width. Finite-r threshold shifts, crossover tie splitting and joint-limit uniformity are not established by these formulas. At an exactly axial incoming momentum the channel never opens in the free law, so this rate reduction is not applied there.

## Needed checks and residuals

Derive the link vertex directly, check finite-matrix projectors and independent eigenspinor sums, verify the canonical coefficient with an independently normalized finite-volume/Fock calculation, compare the exact lattice shell integral at decreasing r and independently check the soft endpoint/power law. A permitted channel is not automatically a calibrated astronomical attenuation bound. Emission changes the particle trajectory; detector/source distributions, finite magnetic fields, propagation and interacting speed/mass/Pauli matching remain uncomputed. Do not transplant the first milestone's eight-species multiplicity: this Wilson light cone is unique.
