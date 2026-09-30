# Finite-excitation absorption on sufficiently large periodic tori

This narrowly extends the provisional height proof in frozen REPORT.md f0947fc42415ad732c4485ae67881a4337bc0fcd2b61fb4d5629669646a55f56. The report, its controls, source identities and FREEZE.json are unchanged. The extension contract was separately frozen before its controls. No formal review/audit or microscopic closure is asserted; independent checking of both the main proof and this refinement is pending.

**Claim.** On the actual even periodic cubic rotor torus, W=1, fixed physical odd k>=7 and side L>=4k, the original no-event semigroup has a bound of the form (13) of the report, uniform over all such L, positions, charges and electric states. In those formulas replace

    n_k=floor(5k/3)+1

by

    n_k,per=floor(20k/7)+1.                            (P1)

All other definitions of M,R_k,c_k,a_k,T_k,b_k,C_k,gamma_k are unchanged. The original marked and polynomial-field output estimates follow at the same declared scope. For physical k<=5, the direct loss G>=2(6-k) supplies absorption without this height construction. This statement does not cover arbitrary L or extensive positive density.

The proof retains the complete physical Gauss/charge/electric carrier. Finite side L>=4k>=28 ensures that all radius-two star geometry in the exact operator identity (3) is nonaliased. In particular the selected +x axial two-hop path is unitary on its basis domain, injective, and has coefficient+1. Every other dark input to a selected output still belongs to one of the three categories used in the report: a different hole with the same B mask; a same-hole B reshuffle of graph length at most two; or the spectral term. No finite electric truncation is involved.

Define a continuous periodic function of period L by

    chi_L(s)=s,                              -5<=s<=5,
    chi_L(s)=5-sigma*(s-5),                  5<=s<=L-5,
    sigma=10/(L-10),

and extend it periodically. Both endpoint definitions agree modulo L. It has range [-5,5], derivative either1 or -sigma almost everywhere, and is one-Lipschitz in the circle metric because L>=28 gives sigma<=1. Set

    Phi_L(h,S)=sum_(b in S) chi_L(h_x-b_x),
    -5k<=Phi_L<=5k.                                    (P2)

The height is independent of choices of coordinate representatives. Unlike the failed minimum-image clipped height in the report, chi_L has a slow continuous return along the rest of the circle.

For any real x and d>=0, integrating the lower derivative bound along the positive arc gives

    chi_L(x+d)-chi_L(x)>=-sigma*d.                      (P3)

For the original six occupied star sites and a shift d in {1,2,3,4}, the initial relative x values are -1,+1,0,0,0,0 and every interval stays inside [-5,5]. Their exact total increase is6d. The other k-6 particles each obey (P3). Furthermore L>=4k gives

    sigma*(k-6)=10(k-6)/(L-10)<=5/2.                   (P4)

Thus another hole-moving source in the exact reverse row raises (P2) by at least

    d*(6-sigma*(k-6)) >= (7/2)*d.                      (P5)

The relevant d is well-defined as the short positive displacement from h to the other possible input center: the eighteen neighbors of c=h+2e_x have d=0,1,2,3,4; d=0 is uniquely the selected inverse center h. This use of a local displacement does not assign a global ordering to the torus.

A same-hole source starts at c. Shifting h to c adds at least12-2*sigma*(k-6). A single B reshuffle moves its coordinate by circle distance at most two; one-Lipschitz continuity bounds the possible decrease of the height by two. Its net increase is therefore at least

    10-2*sigma*(k-6)>=5.                              (P6)

The spectral term has no reshuffle and raises it by at least7. Charge changes and electric translations are carried by the exact selected isometry and all other H entries; the height need not distinguish them to order the reverse rows.

Writing the same exact operator identity V†(H-lambda)D=I_D+U_lambda, every nonidentity block now has source height at least7/2 above its row height. This works even though (P2) takes rational rather than integer values. By (P2), n successive decreases are impossible once (7/2)n>10k, giving (P1) and U_lambda^(n_k,per)=0. There is no iteration with a torus-cut discontinuity.

The finite Neumann inverse with ||U_lambda||<=2M+1 is now identical to the report's argument. Its real-frequency inequality, Fourier sine window and original-loss Duhamel comparison require only this inverse and the same M/G bounds, so they give the stated explicit decay. At fixed delta,kappa the inverse rate and each fixed polynomial weighted-output constant remain at most exp(O(k)), uniformly in every even L>=4k. All moment/domain qualifications in report section4 remain in force.

check_periodic_height.py is a new exact integer-numerator implementation, independent of the earlier H builder. It checks all piecewise-linear corners and periodic wraps on189 even sides L=28,...,404, 4,560 allowed odd-k/side pairs, 163,296 point increments and 204,120 possible short B-coordinate moves. It verifies the star increment, (P3)-(P6), range and nilpotency arithmetic with no floating tolerance. Runtime was0.531468 CPU seconds,0.532138 wall seconds and19,218,432 bytes peak RSS under the30 CPU second guard and one-thread environment. PERIODIC_RESULTS.json binds the runner. These controls corroborate the analytic inequalities; they do not substitute for the complete reverse-row classification above.

This refinement closes the particular gap between the Z³ finite-global-k theorem and **arbitrarily large periodic volumes at that fixed k**. It allows all positions of the k occupied B sites, including arbitrarily separated spectators. The side restriction is L>=4k, not a density condition k/L³ small independently of L. An extensive k proportional to volume violates it, even at arbitrarily small positive density. The fixed L8,k255 approximate-dark sequence remains a counterexample to unconditional periodic uniformity.

No source ensemble decomposition, positive-density absorption, multiple-hole control, finite-spin transfer, or microscopic local-output limit is inferred. The source-weight and many-body localization obligations in report section7 are unchanged.
