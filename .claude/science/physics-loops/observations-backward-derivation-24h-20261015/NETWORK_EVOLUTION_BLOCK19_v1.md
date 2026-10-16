# A finite-window test has blind force directions

This is a counterexample to treating a finite collection of passing block18
weak tests as a derivation of the actual action. It does not invalidate the
necessary identity or its uncertainty bound. The finite selected test functions
must themselves be challenged.

Fix a window [0,1], a smooth imposed trajectory q(t)=1+t, and Omega2>0.
Choose the four test functions used in the numerical controls:

    psi_j=t^2*(1-t)^2*P_j(2*t-1), j=0,1,2,3,

where P_j is the ordinary Legendre polynomial. For exactly known q, the
force perturbation enters the block18 weak residual through

    integral delta_f(t)*K_j(t) dt,
    K_j=q^2*psi_j''+6*q*q'*psi_j'
        +(6*q'^2+3*q*q''+Omega2*q^2)*psi_j.

K_j is a polynomial of degree at most j+6, hence at most9 for the chosen
four functions. Set delta_f=eta*P_10(2*t-1) with any nonzero real eta.
Legendre orthogonality on [0,1] makes all four added residuals exactly zero.
Adding this smooth force to a genuine candidate response passes those
four tests with the same already-fixed candidate coefficients.

It is not a different hidden initial preparation of the same action.
The added force would need

    q^2*delta_f''-2*q*q'*delta_f'
      +(2*q'^2-q*q''+Omega2*q^2)*delta_f=0.

Its degree12 leading term from Omega2*q^2*delta_f cannot vanish; the derivative
terms have degree at most10. The original force equation with its hidden
oscillator therefore fails for this modified response.

The next test function j=4 detects the perturbation: only its
Omega2*q^2*psi_4 term has degree10, with nonzero leading coefficient, so
its projection onto P_10 is nonzero. The exact code checks both the four
blind moments and the added detecting moment.

This is not a universal limit on observations. It shows why a finite test
family is a selected probe and why passing it supplies bounded evidence,
not a unique mechanism. Reserve additional window shapes and rates, check
residuals beyond the fitted test span, and use a physically justified
bandwidth/model-error contract if seeking a finite certificate.
No actual dataset is adversarially modified here; all functions are exact
synthetic counterexamples. The measured force spectrum needed to detect
the extra component is an experimental question.
