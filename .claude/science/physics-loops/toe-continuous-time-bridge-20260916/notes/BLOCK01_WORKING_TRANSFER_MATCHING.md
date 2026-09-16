# Working transfer matching: Fourier coefficients before phase transport

Exploration, no theorem or phase claim yet. Let delta>0, g>0. For a rotor with T=(g²/2)sum E² and V=g^(-2)sum[1-cos curl theta], the symmetric transfer is exp(-delta V/2) exp(-delta T) exp(-delta V/2). The exact temporal kernel with normalized Haar measure is phi_(1/(g²delta))(theta'-theta), where phi_beta(theta)=sum_n exp[-n²/(2beta)] exp(i n theta).

A normalized spatial Villain factor is W_beta(theta)=phi_beta(theta)/phi_beta(0). Put q=exp[-1/(2beta)]. At q small, W=1+2q(cos theta-1)+O(q²). The induced potential -delta^-1 log W therefore has leading coefficient2q/delta. Supplying beta_s=delta/g² makes this coefficient exponentially small in1/delta rather than1/g². To match the cosine coefficient, q_s must instead satisfy q_s/delta ->1/(2g²), e.g. beta_s=[2log(2g²/delta)]^-1. Prove uniform-in-angle remainder and track its volume dependence; do not silently linearize one winding image.

Finite-clock complication: sampling the temporal heat kernel on N angles and normalizing its row sum gives character eigenvalue

    lambda_r(delta,N) = sum_m exp[-a(r+mN)²] / sum_m exp[-a(mN)²],
    a=delta g²/2.

At fixed N and delta->0, this tends to1 with exponentially small generator, by the angle-space Poisson form. It is not automatically exp[-delta g² principal(r)²/2]. Under N->infinity and J=aN² fixed, expansion suggests an effective low-mode coefficient

    (g²/2) r² D(J),
    D(J)=1-2J E_J[m²]
        =(2pi²/J) E_(pi²/J)[k²],

with the expectations over normalized integer Gaussians. The limits should be D(0)=0 and D(infinity)=1. Derive all limits, signs, remainder control and physical-sector witness independently. A logarithmic temporal beta scaling at fixed N can instead approach a nearest-neighbor clock kinetic operator; current main's qutrit transfer is related prior art, not a new general principle.

The unresolved phase step is still a uniform anisotropic compact-defect estimate in the matched law. These matching observations alone do not supply it.

## Prior-art correction and new target

Current main COMPACT_DETERMINANT_CURRENTS_SIGNED_SECTORS_AND_FINITE_CYCLIC_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-14.md PartIII already proves both logarithmic temporal and inverse-logarithmic spatial matching, including the frozen fixed-N rotor-scaling counterexample and the finite-box generator. These are prior results, not new accomplishments of this campaign. The new target is the joint clock/time crossover and a variance-calibrated transfer valid along every delta->0,N->infinity path.

Write the exact normalized clock kernel as Q_x=E_x X^K with integer-Gaussian probability proportional to x^(K²). Let sigma²(x)=E_x K². It is continuous strictly increasing from0 toinfinity. Choose x=x(delta,N) by

    sigma²(x)=delta g² N²/(4pi²).

The low Fourier character has angle h=2pi r/N. If the fourth moment obeys mu4<=C(sigma²+sigma4), the cosine remainder and logarithm yield

    | -delta^-1 log lambda_r - (g²/2)r² |
       <= C r4 [g²/N²+delta g4]

for delta g²r² sufficiently small. This would remove the order restriction for fixed low modes. It is a matching choice for a supplied coupling, not a physical value derived from axioms.

A full fixed-volume proof may use the actual positive symmetric transfer, an O(delta²+delta/N²) consistency estimate on finite Fourier polynomials, and the common-Hilbert positive operator A_delta,N=(I-T_delta,N)/delta. Core convergence gives strong resolvent convergence by a direct resolvent identity; scalar comparison between T^n and exp[-n(I-T)] gives the product limit. This could include bounded gauge-compatible matter and exact mod-N Gauss projection. All details remain to be established, including uniform integer-Gaussian moment constants and source conventions.
