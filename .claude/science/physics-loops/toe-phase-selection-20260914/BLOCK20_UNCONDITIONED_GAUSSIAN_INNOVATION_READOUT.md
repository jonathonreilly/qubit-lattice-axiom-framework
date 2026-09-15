# Unconditioned Gaussian innovation readout and its locality cost

Personal follow-on, 2026-09-15. Private proof candidate, not independently
reviewed or proposed retained. This revisits the campaign's proper Gaussian
likelihood construction and avoids confusing a selected posterior with the
unconditional law of its original roots. The action and Gaussian noise law
remain supplied; no Born rule, empirical identification or native selection
is obtained.

## 1. Exact readout instead of selecting an observation window

Use the proper complex Gaussian convention CN(0,C). Let L have full column
rank, let the observation covariance N be positive definite, and define
Q0=L* N^-1 L>0. The earlier likelihood model supplies independent

 psi~CN(0,alpha^-1 I), eta~CN(0,N), Y=L psi+eta,
 C_alpha=(Q0+alpha I)^-1, alpha>0.

The previously derived conditional distribution is
psi|Y=y ~CN(C_alpha L* N^-1 y,C_alpha). It is not necessary to accept only
y near zero if the DESIRED OBSERVABLE is explicitly changed to the innovation

 Z_alpha=psi-C_alpha L* N^-1 Y
        =alpha C_alpha psi-C_alpha L* N^-1 eta.          (1)

Indeed, all these variables are jointly proper complex Gaussian, and

 Cov(Z_alpha)=alpha C_alpha^2+C_alpha Q0 C_alpha=C_alpha,
 Cov(Z_alpha,Y)=C_alpha L*-C_alpha L*=0.

Thus Z_alpha~CN(0,C_alpha) is INDEPENDENT of Y. This is an unconditioned
readout of the joint data; no observation window is selected and no
acceptance probability is spent. Gaussian independence is essential to that
last conclusion, not merely vanishing covariance of arbitrary variables.

The original root psi still has its independent prior law. Equation(1)
does not relabel psi itself as a correlated field. It replaces the observable
by a declared linear function of the recorded root and observation values.
Whether this readout is a physical observable is an additional bridge.

## 2. A proper noise-only form at alpha=0

If Q0 remains strictly positive, no improper root prior is needed at all.
Draw only eta~CN(0,N), and define

 Z0=-Q0^-1 L* N^-1 eta.                                 (2)

Then Cov(Z0)=Q0^-1 exactly. On a coupling psi_alpha=alpha^-1/2 xi with
xi~CN(0,I) independent of eta, the first term in(1) is
sqrt(alpha) C_alpha xi and vanishes in L2 as alpha->0 for fixed dimension
and Q0>=m I>0. The second term converges to(2). This is a limit of readouts
of proper laws and also a direct proper-noise construction in its own right.

If L is square and invertible, Q0^-1 L* N^-1=L^-1, so(2) is simply
Z0=-L^-1 eta. This is the ordinary Gaussian linear-solve sampler. The
observation noise need not be called a microscopic quantum state. It is a
supplied classical Record payload law, consistent with the existing causal
codec only if its own formation conditions are satisfied.

## 3. Uniform approximation by finite-range readouts when the source is massive

Suppose on a family of finite or infinite bounded-degree slot graphs,
Q0 has range r0 and m I<=Q0<=M I with fixed0<m<=M. Let
A=Q0+alpha I, a=m+alpha, b=M+alpha, P=I-A/b,

 C_K=b^-1 sum_(j=0)^K P^j, rho=1-a/b<1.

C_K has range at most K r0, and C=A^-1=b^-1 sum_(j>=0)P^j.
Write omega=alpha psi-L* N^-1 eta, so Cov(omega)=A and Z=C omega.
The truncated readout Z_K=C_K omega satisfies the exact error identity

 Cov(Z-Z_K)=A^-1 P^(2K+2)<=rho^(2K+2)/a I.              (3)

This follows because C-C_K=A^-1 P^(K+1), and A,P commute. For n requested
complex components, E||Z-Z_K||^2<=n rho^(2K+2)/a, uniformly in total volume.
For alpha=0, omega=-L* N^-1 eta and the same statement holds with a=m,b=M.
To call omega local, L* N^-1 itself must have bounded range; diagonal N and
bounded-range L, as in the earlier supplied circuit, suffice.

This is a quantitative, exponentially decaying readout tail, not an exact
fixed-radius readout. A requested mean-square accuracy epsilon^2 for n
components is guaranteed when

 K+1 >= log[n/(a epsilon^2)] / [-2 log rho],             (4)

when0<rho<1 and the right side is positive. If rho=0, the zeroth term is
already exact. The bound depends on the supplied source gap m. It does not
stay uniform as a massless thermodynamic gap tends to zero. A massless
construction needs a separate infrared existence and locality estimate.

For an infinite massive periodic source, the same operator series converges
in norm. Define each row's Gaussian linear functional from independent noise
in L2; its variance and the truncation error follow from(3). This constructs
a consistent unconditioned Gaussian readout field with covariance Q0^-1,
conditional on the supplied massive source and local noise model. It does
not by itself give local operators that generate a physical quantum phase.

## 4. Determinant branch weights are not obtained by this trick

If a source label j is sampled with prior probability p_j and(1) or(2) is
performed conditionally on j, then P(j)=p_j remains unchanged. The marginal
field is sum_j p_j CN(0,C_j). It does not acquire weights proportional to
det(C_j), which arose in the earlier likelihood model from conditioning.

For example, take complex dimension2, Q1=I, Q2=4I and equal prior labels.
Noise-only readout gives the two labels weights1/2,1/2. Weights proportional
to the Gaussian raw masses det(Q_j)^-1 are16/17,1/17. They are different.
A determinant-weighted source selection still needs its own derivation or
supplied rule. The innovation construction removes a rare-event cost only
for the fixed-source Gaussian readout law, not for every target of the prior
likelihood protocol.

## 5. Relation to permanence and the history-resource check

The readout in(1) is a function of already recorded payloads and supplied
coefficients; it does not overwrite them. Its inverse matrix is generally
nonlocal. Equation(3) gives a controlled local approximation in the massive
case, while exact finite-radius output or a local autonomous write of every
Z value is a different task. The native nearest-neighbor generative circuit
for eta and the physical readout of Z have separate locality contracts.

The history-capacity calculation in block19 is not contradicted. This
construction produces a field on the supplied spatial slot graph; it does
not identify a full four-dimensional set of independently recorded events
with bounded resources in three native dimensions. Neither classical Gaussian
sampling nor a global change of observable supplies physical measurement,
unitary evolution, charged matter or a native-law selection principle.

The strongest follow-up is to choose an actual observable class first, then
prove its noise-to-Record readout and causal formation costs with constants
uniform in the required physical limit. A new generic nonselection witness
would add less than completing that concrete bridge. The present source
shows a positive alternative to rare selection for one fixed Gaussian field,
with its nonlocality and branch-weight boundaries explicit.

No public PR, axiom/primitive change or formal audit status is requested for
this private checkpoint. The block5 likelihood result remains correct with
its original root/conditioning scope; the new construction changes the
observable and does not retroactively change that earlier claim.

## 6. Exact fixed-radius scope and primary-source disposition

For independent site noise, any deterministic readout whose value at x
uses only the noise in B_R(x) is independent of its value at y whenever
dist(x,y)>2R. This conclusion allows nonlinear measurable readouts; the
independent ancestor sets, rather than linearity, imply independence.

In contrast, on a connected nearest-neighbor regular lattice the massive
scalar source Q=m I+Delta, m>0, has strictly positive inverse entries at
every pair of vertices. Indeed, writing Delta=2d I-A_adj gives

 Q^-1=(m+2d)^-1 sum_(j>=0) [A_adj/(m+2d)]^j.

Every summand has nonnegative entries, the series converges in operator
norm, and a finite path gives a strictly positive summand for each pair.
Thus no deterministic uniformly fixed-radius function of independent site
noise gives this particular Gaussian field exactly on arbitrarily large
connected lattices. This elementary statement does not cover random coding
radii, correlated input noise, extra shared randomness, or a long local
evolution. In particular it does not turn the approximate construction(3)
into an axiom contradiction or a general impossibility for local formation.

The Gaussian residual mechanism is established sampling mathematics.
Hoffman and Ribak, *Constrained realizations of Gaussian fields: A simple
algorithm*, ApJ380,L5-L8(1991), DOI10.1086/186160, was personally read in
full, all four rendered pages. Their equations(2)-(4) give the conditional
mean, residual covariance and mean-plus-residual construction. Here the
joint field includes the supplied observation noise, so the same Gaussian
orthogonal-projection mechanism yields(1). Their assertion of a one-to-one
map between unconstrained and constrained realizations is not used: a
projection imposing a nontrivial exact constraint is generally noninjective.

Primary copy: https://articles.adsabs.harvard.edu/pdf/1991ApJ...380L...5H
Local PDF SHA256:
c39881aa8878035fa443419f3ed1916fae903e547006befff829930f27a5b918.
The NASA copy was downloaded and rendered after the web screenshot route
failed. No result depends on that web-rendering failure.

Disposition: preserve this supporting calculation on the campaign branch.
It does not yet justify another standalone theorem PR. The next substantive
target is a physical-observable bridge for the fixed-law compact model,
rather than another generic Gaussian sampler.
