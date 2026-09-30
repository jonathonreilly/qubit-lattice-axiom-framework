# Exact local consumer and the boundary term not yet controlled

This document states a weaker local collision consumer explicitly. It does not promote the global factorial estimate to arbitrary volume.

Fix a finite A set U and its complete quantum neighborhood, and let C_U=1_(W_U>=2), W_U=sum_(a in U)w_a. The proof of factorial(F9) uses only boundedness, neutrality and the hole-corner property of its test. It therefore applies verbatim to this fixed C_U, with its support-dependent but volume-independent constant:

 <C_U(t)>-<C_U(0)> = integral_0^t <P L'^* C_U> ds
                                      +O_(U,T)(epsilon^4). (L1)

In this identity P is the W-grade average, and the state is still actual sigma. Fix the same explicit finite-range interaction decomposition of the normal-form Hamiltonian and jumps as in the source. Separate the terms whose complete A support is contained in U from the terms meeting both U and its complement. Terms disjoint from U cancel exactly. Denote the latter COMPLETE projected actions on C_U by Theta_U. It is a definite signed local boundary observable; it includes gains and both losses and the full diagonal Hamiltonian coefficients. Its leading Hamiltonian scale can be epsilon^-2. This definition does not assume a boundary flux sign.

Every interior neutral Hamiltonian commutes with W_U. Every interior jump grade r changes W_U by r. The interior negative-grade contribution to C_U is nonpositive; call its positive magnitude A_U. Its interior grade-zero contribution is zero. For r=+1, crossing W_U=1 to W_U=2 requires an already-holed input, so its exact positive injection is at most C epsilon^2 <1_(W_U>=1)>=O_(U,T)(epsilon^4). Grades>=2 give the same bound from their O(epsilon^3) jump coefficient. Consequently

 <C_U(t)>+integral_0^t <A_U> ds
   =<C_U(0)>+integral_0^t <Theta_U> ds+O_(U,T)(epsilon^4).
                                                               (L2)

The preparation costs <C_U(0)>=O_U(epsilon^4), by the pair Taylor argument. Equation(L2) keeps the complete off-grade microscopic contribution via the corrected-test error(L1); no secular ensemble is substituted. A_U is diagnostic, not an original observed count.

A sufficient extra hypothesis for a volume-uniform local collision probability of order epsilon^3 is

 sup_(t<=T) integral_0^t <Theta_U> ds <= C_(U,T) epsilon^3. (L3)

It would then give <C_U(t)><=C epsilon^3 and, using the actual spin cap S=O(epsilon^-1), a bounded epsilon^-2 weighted first-field residence restricted to holes having a second hole in this fixed U. An o(epsilon^3) bound yields vanishing of that restricted contribution. This is weaker than the full dark-residence target: the isolated-hole part and dynamic exterior propagation remain.

Neither(F2) nor the ordinary first field moment proves(L3). The direct norm/current estimate for Theta_U costs epsilon^-2 times a local one-hole probability and is O(1), much too large. Interior source creation at O(epsilon^4) is not a bound on this boundary flux. Static B components cannot be inserted: the actual same-hole and cross-hole terms change B occupation/charge.

The global factorial result succeeds because its full W count commutes with the full neutral Hamiltonian; boundary transfers cancel exactly before estimation. Its n^2 source/support price is retained. There is no proof here of a local cancellation or dispersive estimate reducing that n^2 price for arbitrary volume. No generic all-state inverse gap, independent birth law, dressed preparation substitution or assumed stationary distribution supplies it.
