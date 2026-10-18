# Focused range-two Airy/Bessel check

Disposition: PASS for the stated coefficient model and its fixed analytic outgoing boundary self-energy hypotheses. This is a focused mathematical check, not a formal audit or a full-native pole theorem.

## Bessel equation, sign, and normalization

The recurrence J_(k-1)(z)+J_(k+1)(z)=2k J_k(z)/z gives exactly (-T+f(n+2))u=Eu for u_n=J_(n+nu)(2/f), nu=2-E/f. The physical endpoint equation with +Sigma P1 requires u_0=-Sigma u_1, hence the displayed determinant has the correct plus sign.

Put epsilon=f^(1/3), z=2 epsilon^-3 and E=-2+2 epsilon^3+A epsilon^2. Then nu=z-A/epsilon. The standard transition expansion is

J_nu(nu+a nu^(1/3)) = 2^(1/3)nu^(-1/3) Ai(-2^(1/3)a) + O(nu^-1),

uniformly on compact turning-point parameter sets, with holomorphic remainders in the complex parameters in question. Here 2^(1/3)nu^(-1/3)=epsilon[1+O(epsilon^2)] and -2^(1/3)a=-A+O(epsilon^2). Replacing nu by nu+1 changes the Airy argument to -A+epsilon+O(epsilon^2). Consequently

J_nu(z)=epsilon[Ai(-A)+O(epsilon^2)],
J_(nu+1)(z)=epsilon[Ai(-A+epsilon)+O(epsilon^2)].

There is no missing power of two. The Ai-prime term in the full Bessel expansion is absolute O(nu^-1)=O(epsilon^3), precisely within the indicated remainder. Complex nu lies in a fixed admissible sector since arg(nu)=O(epsilon^2).

Primary references: [DLMF 10.19.8](https://dlmf.nist.gov/10.19.E8), including its complex-order sector, and [DLMF 10.20 uniform large-order expansions](https://dlmf.nist.gov/10.20). Uniformity is needed on a fixed compact complex turning neighborhood, not merely pointwise for real order.

After division by epsilon the frozen-boundary determinant is

(1+Sigma0)Ai(-A)+epsilon Sigma0 Ai'(-A)+O(epsilon^2).

At the first positive Airy zero alpha1, Ai'(-alpha1) is nonzero. Uniform analytic remainder bounds and Rouche, followed by expansion of this simple root, give

A=alpha1+epsilon Sigma0/(1+Sigma0)+O(epsilon^2).

Thus the root energy error is uniformly O(epsilon^4), as claimed. Constants may depend on a fixed lower bound for |1+Sigma0| and the chosen complex neighborhood; this is not uniform as Sigma0 approaches -1. “Analytic” refers to the scaled complex spectral parameter and boundary parameter. It need not assert a convergent power series at epsilon=0.

The same uniform argument differentiated in the boundary parameter gives dE/dSigma=O(epsilon^3). Since Sigma(E)-Sigma0=O(epsilon^2), freezing Sigma changes the NN root by O(epsilon^5). Merely multiplying the determinant's generic O(epsilon^2) coefficient variation would give a weaker estimate: the extra cancellation here follows from the root being within O(epsilon) of the Airy zero, or from this derivative estimate.

## Perturbation and physical remainder consistency

The supplied contour argument is consistent with these scalings: a fixed Airy-scale circle avoids the Dirichlet spectrum by order epsilon^2; the endpoint resolvent-vector norm is O(epsilon^-1/2), while the full resolvent norm is O(epsilon^-2). For nonreal Sigma, the left endpoint row as well as the right endpoint column needs this estimate; the rank-one formula supplies both uniformly when 1+Sigma stays away from zero. The projection difference has rank at most two, so its O(epsilon) operator-norm bound also controls the trace pairing with bounded V.

With lambda^2=8 epsilon^3, bounded perturbation theory gives a second-order error O(lambda^4/epsilon^2)=O(epsilon^4). Dirichlet endpoint suppression and <T>=2-O(epsilon^2) give <V>=d+2a+2b+O(epsilon^2); replacing the Dirichlet projection by the frozen-boundary projection incurs O(epsilon), sufficient after multiplication by lambda^2. Direct arithmetic gives c=109/96.

The localized endpoint projection correction has size lambda^2 times contour length epsilon^2 times squared endpoint-vector bound epsilon^-1, namely O(epsilon^4); additional Neumann terms gain O(epsilon). This supports the stated O(epsilon^3) endpoint derivative and restoration of analytic Sigma(E). These checks are conditional on the stated fixed bounded endpoint perturbation F and the fixed analytic continuation of Sigma; they do not construct that continuation for a microscopic model.

Finally lambda^2 epsilon^4 is O(lambda^(14/3)). Since Im[ Sigma0/(1+Sigma0) ]=Im(Sigma0)/|1+Sigma0|^2<0, the physical width is positive and equals

Gamma = [-Im(a0)/4] Jz lambda^4 + O(Jz lambda^(14/3)).

This is an absolute width error, or a relative O(lambda^(2/3)) error when the fixed leading imaginary coefficient is nonzero. No residue accuracy, exact real-axis spectral atom, or full-native resonance follows from this argument.

## Source identity

Root proof SHA256: 42a2412a8085d586fed6a8525dd556070f3021384755e35284208b59ae1329b4

No repository files changed. Review used direct recurrence/algebra, primary Bessel asymptotics, and contour-scale consistency checks; no empirical input.
