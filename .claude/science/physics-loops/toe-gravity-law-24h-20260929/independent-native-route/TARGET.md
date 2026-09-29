# Native collective pair test

Source sweep: current main e75578f7136401d4bd750131671aed9212c06291; PR9363 fd51a1f4c7f38c124d6f0f7dde396198eadf8b36; targeted open PR9285 and PR9287 actual notes.

Target: construct five local collective pair operators from exactly one M2 factor per cubic site, with cubic E+T2 covariance, and calculate their exact nonperturbative two-particle propagation and a full-carrier stability discriminator for a supplied quartic interaction. No elementary tensor slot, rotor or oscillator is allowed. The law, number axis, vacuum, tensor readout and physical identification are separately supplied/open, not derived.

Define b_x=|0><1| and n_x=b_x* b_x. Around x use d_i=b_(x+ei)b_(x-ei) and a_i=b_(x+ei)-b_(x-ei). Q_E=(d1-d2)/sqrt2,(d1+d2-2d3)/sqrt6 and Q_Tij=a_i a_j/2. Test the translation-overlap Gram of Q_A*|Omega>, the exact two-particle Hamiltonian for H=mu sum n -gE sum Q_E*Q_E -gT sum Q_T*Q_T, and the full filled/checkerboard product-state energies. Inspect critical tuning as a consequence of the calculated symbol. Do not assume that five pair channels yield a stable lightlike or TT-only spectrum.

Completion witness: exact finite Laurent Gram, covariance under all24 proper cube rotations, analytic spectrum from that Gram, and a full-carrier state or positivity proof testing the inferred pair threshold. If this fails, preserve the precise failure and live interacting/record alternatives. No all-native-qubit impossibility follows.
