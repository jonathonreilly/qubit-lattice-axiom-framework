# Independent proof before code inspection

q=1+t gives q'=1,q''=0. psi_j has degree j+4 and is clamped because of t²(1-t)². The derivative pieces of K_j have degree at most j+4; Omega2 q²psi_j has degree j+6 with nonzero leading coefficient for Omega2>0. For j<=3 the kernel is degree<=9. Shifted P10 is orthogonal to every polynomial of degree<10 on [0,1], so all four perturbation residuals vanish for every nonzero real eta and positive Omega2.

The pointwise eliminated operator on eta P10 has degree12 from Omega2(1+t)² eta P10; all derivative terms have degree<=10. Its leading coefficient is eta Omega2 binomial(20,10), nonzero. Therefore it cannot be a homogeneous hidden-preparation change; if the baseline response satisfies the same fixed action the modified response fails its necessary differential equation.

For j=4, leading psi4 coefficient is binomial(8,4)=70. Only Omega2 q²psi4 contributes at degree10. Expand that kernel in shifted Legendre polynomials: coefficient of P10 is 70 Omega2/binomial(20,10). Since integral_0^1 P10(2t-1)² dt=1/21, detecting residual equals eta*70 Omega2/[21*binomial(20,10)]=eta*5 Omega2/277134. This is nonzero. No arbitrary hidden state or quartic choice can absorb this residual at fixed coefficients.

The result is a counterexample to sufficiency of this finite set, not to the necessary weak law. It is limited to the stated window and prescribed trajectory; it neither changes an actual record nor asserts a universal finite-measurement impossibility. q stays positive, so there is no zero-chart ambiguity involved. No defect identified before reading code.
