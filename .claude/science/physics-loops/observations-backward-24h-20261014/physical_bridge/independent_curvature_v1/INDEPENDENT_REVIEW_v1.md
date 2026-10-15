# Independent curvature bridge derivation and concrete checks

Reviewer /root/inertial_response_check; root remains author. No new author
physical_bridge source or code has been opened. The full reasoning, assumptions,
energy normalization, observation transform, Duhamel estimate, explicit BV
constants and frozen-response boundedness proof are in the separately frozen
PRECHECK_v1.md (SHA-256
7b471f937667fb6f2b89c5db280857a9976ed11256a44a27cd7eabe565815b95).
This report does not replace that pre-exposure derivation or confer audit status.

## Independent conclusions

The supplied source-free scalar equation on g_E=a^2 eta gives
chi=a h and chi''-Delta chi+(B-2)H^2 a^2 chi=0. The subtraction of a''/a is
essential; the frozen t=0 propagation mass is sqrt(B-2)H. The perturbation is
not assumed stationary. The spatially flat chart and its fixed initial slice
are not the static de Sitter patch or its horizon-boundary energy class.

At a(0)=1 the actual excitation energy measured by Einstein comoving unit
observers, with the supplied action's normalization, is
E_com(0)=Q integral[hprime_0^2+|grad h_0|^2+B H^2 h_0^2].
For f=chi_0=h_0, p=chi'_0=hprime_0+Hh_0,
N_0^2=2E_chi(0)=integral[p^2+|grad f|^2+(B-2)H^2 f^2].
They are different quadratic forms. The exact comparison is
lambda_- E_com/Q <= N_0^2 <= lambda_+ E_com/Q,
lambda_+/-=1-1/(2B)+/-sqrt(4B+1)/(2B).
In the opposite orientation the constants are
mu_+/-=(2B-1+/-sqrt(4B+1))/(2(B-2));
mu_-=1/lambda_+, mu_+=1/lambda_-.
The apparent inverse-orientation discrepancy is therefore not a disagreement.
Both reciprocal identities were checked symbolically. B>12 implies
2/3<lambda_- and lambda_+<5/4. Constants are long-wavelength sharp; a spatial
constant Fourier mode used to compute them is not a nonzero finite-energy
state. No vacuum/initial phase or selector is supplied by this comparison.

For O[h] in the assignment the exact transformed weights are
Wtilde=W/a and C=[c+(1-|u|^2)(a'/a)(W.u)]/a.
The additional direct-clock term is positive and cannot generically be
omitted. All time derivatives, window integrals, Fourier momenta and paths
here are conformal-coordinate quantities. Proper clocks and their endpoint
Jacobians still use a sqrt(1-|u|^2), and the reference body equation includes
Hubble drag -(1-|u|^2)(a'/a)u. The M6 endpoint algebra can be reused only
with those curved reference coefficients. The result does not identify a
coordinate force with an accelerometer or derive actual instrument weights.

After the exact integration by parts, with P=(1-|u|^2)Wtilde,
J=-P.u, A=C-J' and Bvec=P-u(P.u), each Fourier readout is
integral exp(i k.x)(A-i k.Bvec)v_k dt. Compact continuous W supplies the
zero endpoint term. BV c and W' plus the stated smooth timelike path make
A BV and Bvec continuous with BV derivative. The precheck includes endpoint
jumps in the total-variation requirements, rather than discarding them.

For the same arbitrary initial data, compare the time-dependent potential
V=M^2 a^2 to frozen V(0)=M^2, M=sqrt(B-2)H. Variation of constants gives
D=integral_0^T(V-V0)dt=M^2 H T^2/(1-HT).
Positive monotone mode energy gives |v_k|<=N_k/omega, with
omega=sqrt(|k|^2+M^2), uniformly in initial phase. A low-momentum direct
bound and a high-momentum nonstationary-phase BV integration give, for every
cut K>0,
 ||O_V-O_0||_H0^2 <= 1/(2pi^2) {
 K^3 [D(A1/M^2+B1/(2M))]^2/3
 +D^2[S_B^2/K+S_A S_B/K^2+S_A^2/(3K^3)] }.
All constants are defined explicitly in the precheck from transformed weights,
the subluminal margin and path acceleration variation. This proves a finite
observation error operator, not just separate per-mode agreement. A second
BV integration proves the frozen functional itself bounded, so the true
functional extends to the same massive H1 x L2 energy completion by density.
The conservative constants may be large and deteriorate near t=1/H. There is
no unstated small-curvature assumption. A physical energy-error bound further
needs E_com(0) and the lambda_+/Q conversion, which remain supplied inputs.

For multiple paths the initial Fourier data are shared. Sum path readouts
before taking their norm; triangle bounds on the constants are permitted,
but their energy budgets are not independent. No statement about exact
positive-mass accelerated Gram dominance follows. This result compares a
specific de Sitter variable potential with its positive frozen value, not
with massless propagation. Any additional frozen-mass-to-massless comparison
needs its own proof and its own initial-energy convention.

## Independent executed controls

The script curvature_controls_v1.py was authored from the precheck and run
once with /usr/local/bin/python3. The run completed successfully in about
0.591 seconds: 209 recorded conditions passed, zero failed. It includes
symbolic field, curvature-shift, energy-derivative, reciprocal-eigenvalue and
weight identities; six independent h/chi ODE solution comparisons; 24
momentum/direction response rows spanning q=0 through50; pointwise mode-energy
bounds; direct Duhamel field/derivative checks and two swapped-Duhamel
observation checks; and a genuine displaced-path coherent cross term.
No author suite or author curvature code was executed or consulted.

The synthetic fixture fixes H=1/10, B=16, T=1,
x=(t/10+t^2/40)e1, W=16t^2(1-t)^2 e1 and
c=(2/5)16t^2(1-t)^2. Its transformed coefficients are exact rational
polynomials. Absolute coefficient sums give conservative analytic sup, L1
and variation bounds for the proof; samples only check their implementation.
The display-cut K=2 gives the smallest of the six displayed analytic bounds,
epsilon<=0.8241059002009096 for the normalized computational energy. This
is deliberately conservative and is not an empirical discrepancy estimate.

The largest original-h versus transformed-chi or integrated-weight numerical
discrepancy was 7.78e-16. The largest direct/swapped Duhamel discrepancy was
2.21e-15. The largest quadrature-reported local error was 2.83e-14. Omitting
the induced transformed clock term changed a sampled response row by up to
0.0174744428. A displaced second path produced a nonzero shared-field cross
term 8.3228521e-8, ruling out the tested independent-budget replacement.
Those finite Fourier probes are operator diagnostics; individually they are
not finite global-energy fields. The analytic Fourier bounds and density
argument, rather than the sample count or quadrature accuracy, carry the
infinite-dimensional statement. ODE/quadrature computations are not interval
certificates. No execution failed and no attempted failing result was removed.

## Exposure and scope record

Before this work I knew the supplied curved-action note and M6 source, whose
exact hashes are recorded. The new precheck was frozen before any root
curvature content was disclosed. After the precheck and initial control
source were written, root sent a status message mentioning an exact
four-endpoint massless-propagation Gram and 20 author controls. That formula
was not used in this oracle, its expectations, tolerances or calculations;
the four-endpoint construction belongs to another checker. Root also flagged
an apparent orientation difference in energy constants; I independently
verified their exact reciprocal equivalence. New author files remain unopened
at this freeze. The identity records this distinction rather than claiming
there was no message exposure of any kind.

The action, stationary vacuum, de Sitter background, free scalar channel,
physical conformal coupling, external dynamics when used, reference paths,
clock/link model, normalization Q and all actual measurement inputs remain
conditional. This bridge supplies no initial-state choice, stationarity of
perturbations, cosmological-state derivation, retarded-source convergence,
observed scalar residual, fitted parameter or energy upper budget. No network,
raw observation, canonical source/index/branch/lock/state/publication change,
other agent or formal audit was used. Root can now request comparison with
its exact frozen author source; that will be a separate source-bound supplement.
