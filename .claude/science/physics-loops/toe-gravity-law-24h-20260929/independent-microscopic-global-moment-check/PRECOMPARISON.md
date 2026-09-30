# Independent precomparison: original microscopic global moment

Frozen before reading the new GLOBAL_MOMENT_LEMMA proof or its runner.
Exposure: author brief supplied the proposed S_loss formula, commutator
cancellation,72-state result and global claimed shape. Root has independently
checked the prior normal form/mean-defect proof and reread it in full here.
This is a focused different analytic derivation, not blind rediscovery.

Let Kd=W+NB. Bare j commutes with Kd; J=j+epsilon j1+O(epsilon²).
For any f(Kd), the cross dissipator is
Dcross*f=1/2[f,X], X=sum(j* j1-j1* j), anti-Hermitian.
The first W grades of j1 are0,-2; those of X are+/-1, so I_W X is
Hermitian. With S_loss=i kappa/(2delta) I_W X, conjugation by
exp(epsilon³ S_loss) gives H correction -i kappa X/(2epsilon).
Its Heisenberg commutator cancels +kappa[f,X]/(2epsilon).
No grade-zero part of X is hidden here. All retained W-diagonal normal-form
Hamiltonians preserve NB by the same charge/record-number symmetry, hence Kd.

For Vtheta=exp(theta Kd/2), conjugating a bounded local term by Vtheta
costs at most exp(theta times its bounded Kd support capacity), independent
of spin dimension and volume. After the displayed pole cancellation the
weighted generator is a sum of O(1) bounded local terms. Thus a candidate
operator inequality is L* exp(theta Kd) <= Ctheta N exp(theta Kd).
It needs the exact finite-circuit, not a formal divergent unitary series.
The additional loss circuit shifts H D2 at order epsilon, and shifts the
jump drift at order epsilon; these are bounded, so do not recreate a pole.

Bare preparation requires a quadratic epsilon cost. A crude global
||U-I|| or weighted norm bound gives an excessive linear cost. Instead for
a local near-identity gate and an extra positive tilt eta, split its local
space into Kd=0 and Kd>=1. In the sandwich by exp(-(theta+eta)Kd/2),
the unperturbed positive-weight matrix has eigenvalue1 on the zero sector
and a dimension-independent gap1-exp(-eta) on its complement. The zero
block changes only O(epsilon²), the cross block O(epsilon), and a Schur
bound gives U*exp(theta Kd)U <= exp(Cepsilon²)exp((theta+eta)Kd).
Apply this to disjoint gates within each of finitely many layers, spending
one tilt increment per layer, not per site. The product Omega has Kd=0.
The same inequality returns from the dressed to physical observable.
Together these mechanisms should yield exp[Ctheta N(t+epsilon²)].
Check the exact gate hypotheses, support overlap, zero-block estimate,
and all original labels against the author proof before adopting it.

For a small time t0 with Ctheta(t0+epsilon²)<theta/2, Markov gives a
full-B tail exp(-theta N/2). The physical mean-hole bound independently
gives P(fullB,W=2)<=Cepsilon²N. Optimizing their minimum over N gives
O(epsilon² log(1/epsilon)). This inference is small-time only unless
additional information is proved. It does not bound integrated fast
activity, local islands, conditional hazards, electric moments or M4.

No new computation has run for this independent check at this freeze.
