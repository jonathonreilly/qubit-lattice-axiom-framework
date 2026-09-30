# Why global source moments do not supply the missing conditional tail

This is a logical separation of available estimates, NOT a counterexample to the actual microscopic dynamics. No state constructed here is claimed to occur with the displayed probability under that dynamics.

Use the already checked actual one-hole occupied-island source words. For increasing R choose their torus large enough that the source does not alias. Their normalized physical basis vectors gamma_R have W=1, an occupied B component of size k_R->infinity in the distance-six B graph, total B count of the same order, and all electric coordinates in{0,+1,-1}. Their source word has the correct Gauss/record parity and a nonzero algebraic coefficient. Let n_R=|A|, with n_R and k_R comparable, and average gamma_R over all A-preserving translations on that torus. Every state in this mixture has one hole sitting beside its large occupied component.

Choose a compatible integer spin S_R so large that epsilon_R²=delta/[K S_R(S_R+1)] and q_R=n_R epsilon_R²<=exp(-k_R²). Define

    rho_R=(1-q_R)|Omega><Omega| +q_R translation_average(|gamma_R><gamma_R|).

One can retain a classical original mark word associated with each translated gamma_R; it is the actual algebraically accessible word, not a resolved internal-hop record. The probability q_R is arbitrarily supplied only for this logical test.

Then <w_a>=q_R/n_R=epsilon_R² at every A site. For every fixed m and all large R, the hole is always attached to a component of size at least m, so

    epsilon_R^-2 <w_a 1_(|C_a|>=m)> =1.                 (S1)

Thus the uniform conditional-cluster tail does NOT tend to zero. Nevertheless, for every fixed theta and every fixed positive t, with K_def=W+N_B,

    Tr(exp(theta K_def)rho_R)
        =1+q_R[exp(theta(1+N_B(gamma_R)))-1] ->1.        (S2)

It eventually satisfies any of the positive-time global bounds exp[C_theta n_R(t+epsilon_R²)] with C_theta>0. Mean holes, original mean record counts and uniform local electric moments are also harmless: the latter even have field support|E|<=1. In particular adding ordinary field moment bounds to global count bounds does not supply the missing hole-conditioned local cluster estimate.

This test does not satisfy the actual microscopic equation and does not satisfy the exact initial finite-depth seed at t=0. Those are precisely the extra dynamical/source facts that a positive-time proof must use. It does not refute M4, invalidate the global moment theorem, establish percolation, or give a lower probability for the source word. It shows why promoting a global exponential moment plus a mean-hole estimate to (I3) is a substantive gap, even when every chosen basis word is physical and source-accessible.
