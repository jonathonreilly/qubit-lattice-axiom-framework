# Independent finite-state ladder diagnostic check

Reviewed `/private/tmp/neutral_ladder_probe.py` and its JSON. The spectral-window calculation is correctly indexed relative to E0, but its interpretation needs the following precise restrictions.

## What is filtered

Let the selected normalized state m have energy E_m=E0+Delta, and define v=(C−<m|C|m>)m. The Lanczos spectral variable in the code is lambda=E_n−E0, not the transition frequency from m. The transition frequency is omega_nm=lambda−Delta. Therefore the reported quantities are

W_upper(w)=sum_n |<n|v>|² exp[−((lambda_n−2Delta)/w)²],
W_lower(w)=sum_n |<n|v>|² exp[−(lambda_n/w)²].

These are squared norms for AMPLITUDE filters exp[−(omega_nm−Delta)²/(2w²)] and exp[−(omega_nm+Delta)²/(2w²)], respectively. The Gaussian weight has standard deviation w/sqrt(2), so “width” must retain this explicit convention rather than being called a Gaussian sigma without qualification.

The two numbers are separate branch-filter norms. Adding the corresponding operators produces a Hermitian two-sided filter, but its squared norm has cross terms from overlapping Gaussian tails; the current code does not include those cross terms. This is harmless if the separate branch definition is retained. Centering removes the m component before filtering; it does not generally remove every state degenerate with m.

The lower weight agrees with |<g|C|m>|², as expected from Hermiticity and a window containing the ground line. This is a useful internal check, not proof of global spectral completeness.

## Conditional harmonic comparison

For a single canonical oscillator H=E0+Delta a†a, vacuum g=|0>, selected m=|1>, and a LINEAR source C=c0 I+c(a+a†), the transition weights are

|<0|C|1>|²=|c|²=Z01,
|<2|C|1>|²=2|c|²=2Z01,

and the upper state is at E0+2Delta. Those are the correct targets for the proposed test. An independent six-level oscillator matrix with the reported Delta and Z01 reproduces lower=0.003524947756927933 and upper=0.007049895513855866 for every supplied width (Gaussian remote-tail corrections are negligible here).

IMPORTANT NORMALIZATION: the JSON key `upper_over_2Z` already divides by 2Z01. Its harmonic target is ONE, not two. At width 0.1 the value 1.93503026025 means 1.935 times the harmonic upper weight, equivalently 3.87006 times Z01. Neither choosing this width nor tuning another width to any desired ratio is an independent test. At width 0.02 the estimated ratio is 3.674394741e−8.

The comparison assumes the selected transition corresponds to the first quantum of that oscillator and that this C acts as its linear coordinate. For multiple unresolved modes, even a harmonic model can put additional creation weight in the same window. For an interacting scalar, finite-volume two-particle energies need not equal exactly 2Delta. For a nonlinear or composite observable, matrix-element ratios need not be 1:2 even for an underlying harmonic oscillator. For example, number-dependent raising terms can alter |1> to |2> while leaving |0> to |1> unchanged. Thus failure tests the specific isolated linear harmonic realization through C, not all bosonic/scalar realizations.

## Numerical scope

The agreement between 128 and 256 iterations is strong consistency evidence for these window estimates. It is not a rigorous quadrature/error certificate or proof of no exact or very weak line at 2Delta. The three-term recurrence does not fully reorthogonalize; eigenvector residual checks and the proposed reconstructed Ritz checks are appropriate follow-ups. The code subtracts m from recurrence vectors, so identifying the calculation with the full-H spectrum also depends on m being an adequately accurate eigenstate; its residual is not explicitly checked in this script. The gap computed here is a Rayleigh quotient, not by itself an eigenvalue certificate. The source file's selection as “lowest visible” requires its separate existing evidence.

If a window weight W were independently certified, positivity would give a useful exact bound: the total spectral weight within |lambda−2Delta|<=delta is at most exp[(delta/w)²] W. This conditional bound illustrates what a tiny Gaussian-window result would constrain, but the present approximate W should not be promoted to a rigorous bound without numerical error control.

The calculation retains the supplied finite native Hamiltonian and chosen stationary state. It neither adds a new interaction nor derives a scalar coupling; it does not exclude an emergent interacting scalar in another volume, state, observable, or spectral regime.
