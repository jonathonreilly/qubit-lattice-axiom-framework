# First joint spin/epsilon correction on a closed square

Exploratory author derivation, not a uniform spectral theorem or empirical prediction. Sources: common-field and local-pair notes dated2026-09-24, current main e37967e326c2bdb429bd3106d34158bd5420e9c0. Supplied compensated Hamiltonian, two positive records, kappa=0 separately supplied, integer spin S, zero offset charge. Let C=S(S+1), x=epsilon²=delta/(K C), K,delta>0 fixed. No resonator or physical parameter identification.

Orient edges (0,1),(0,3),(2,1),(2,3), A={0,2}. For occupancy q with two records, every physical integer electric field is
E=(n,q0-1-n,-q1-n,q2-1+q1+n).
Retain only fields in [-S,S]^4. A legal outward hop subtracts1 from its edge field and has amplitude sqrt(1-E(E-1)/C). This supplies a finite exact matrix, not a truncated fixed-spin field approximation.

Only W=0 has nonzero compensation: all B are empty and F_a*F_a is diagonal there, so C_S=4P. On W=1 the other-A occupancy gate vanishes; on W=2 no A is occupied. In W0,W1,W2 blocks the bracket Hamiltonian is

    [4x I, sqrt(x) A*, 0;
     sqrt(x) A, I, sqrt(x) B*;
     0, sqrt(x) B, 2I].

Here A and B include the negative hop sign; Z=BA has positive two-hop amplitudes. Eliminating W2 and W1 at dimensionless energy lambda gives the exact (where inverse exists) energy-dependent P equation

 lambda psi = [4x I - x A* ((1-lambda)I - x B*B/(2-lambda))^(-1) A] psi.

For fixed finite-support P vectors away from the spin boundary, M=A*A=4I-4n²/C exactly. Also

 Z|n> = 2[a_n |n-1> + b_n |n>],
 a_n=1-n(n-1)/C, b_n=1-n(n+1)/C.

Thus N=Z*Z has diagonal4(a_n²+b_n²) and upper/lower adjacent entry4[1-n(n+1)/C]². Expand N=N0+x N1+O(x²) on fixed support:
N0 diagonal8, adjacent4;
N1 diagonal -16(K/delta)n², adjacent -8(K/delta)n(n+1).
In the rotor limit BB*=4I on W2, so R0=A*(B*B)²A=4N0.

For low lambda=x² e, the Schur equation through x³ is

 lambda psi = [4xI-xM - x² N/2 - x lambda M - x³ R0/4] psi + higher orders.

The energy dependence gives (I+4x)lambda at this order; its metric is scalar through O(x), hence normalization introduces no noncommuting first-order term. Formally in physical energies delta lambda/x²:

 H0 = 4K n² - 4delta I - 2delta(U+U*),
 H1 diagonal = 8delta - 8K n²,
 H1(n+1,n) = 4delta + 4K n(n+1),
 H_eff = H0 + x H1 + O(x²).

This is a fixed-support expansion plus a low-energy formal expansion. Uniform remainder bounds for low eigenvalues as S grows remain open; the large-energy spin boundary cannot be covered merely by Taylor expanding at fixed n. Full finite matrices give numerical evidence: at K=delta=1 and S12,20,32,50,80,120 the largest six-gap error after first-order perturbation falls from.03323 to.00000405. At delta/K31.607246 it falls from19.29 to.00968; for S50,80,120 the error/x² is1934,2014,2043. At K=delta=1 the S120 floating residual~7e-7 limits the finest trend. These are convergence diagnostics, not certified asymptotic constants. The ratio31.607246 is an approximate device-like diagnostic scale, not a new empirical fit or independently predicted microscopic input.

The pure-rotor fiber previously gave +20delta x² cos(2phi). The joint limit already supplies a field-dependent kinetic/hopping correction at order x. Consequently importing only that harmonic into the transmon comparator would omit a larger-order term. This does not show whether the complete correction matches observations. x remains uncalibrated; optimizing it on f03/f04/f05 would reuse the evaluation data. Next: independently check the coefficient and derive a controlled low-spectrum remainder, then determine how much of H1 can be absorbed by the four allowed calibration coordinates before any new empirical comparison.
