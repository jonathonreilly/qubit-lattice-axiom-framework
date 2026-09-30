# Analytic spectral evolution target contract

This contract is frozen after an initial applicability reconnaissance and
before implementation, full quantitative proof or any trajectory computation.
It is the next residual after independently checked spectral nonlinear jets.
It does not claim the initial ideas below are already a theorem.

Keep the FULL odd-grid canonical metric carrier, spectral derivative, grid
products and Christoffel-defined sampled ADM C[N], G[X] of spectral-nonlinear-route.
Take the explicit Hamiltonian H_J=C_J[1], with zero shift, a,K>0. No constraint
projection or penalty, smoothing, changed Poisson structure or hidden continuum
field equation may replace this finite Hamiltonian. All six canonical entries
remain; an invariant axial diagonal diagnostic may be justified separately.
Continuum comparison means the identical functional with ordinary derivatives.
Initial metric g0=I+h0 and momentum are real periodic analytic data. Require
an explicit analytic Wiener norm bound ||h0||_(2sigma0)<=1/8, sigma0>0, and
finite corresponding momentum norm. Other analytic data are not automatically
covered. Constants/time may depend on these bounds,a,K,sigma0, but must NOT
deteriorate with grid cutoff J. The original finite-range seed/timing and actual
walker/record mechanism remain changed or absent as already declared.

Target: (1) a positive time T independent of J with uniform shrinking-radius
analytic bounds for the actual finite Hamiltonian evolution; (2) convergence
to a continuum ADM solution in a smaller analytic norm with a stated rate;
(3) corresponding discrete constraint-density errors when the continuum
initial data satisfy all constraints. The theorem must not mistake finite-ODE
existence, a fixed-data Cauchy remainder, or weakly hyperbolic Sobolev stability
for a uniform estimate. Any unsolved step is an explicit target-equivalent or
strictly-weaker lemma, not a completed continuum construction.

Proposed approach family: augment coordinates by their spectral derivatives
and derivatives of B(g)=sqrt(det g)g^-1, use exact summation by parts to express
the finite Hamiltonian variation as a first-order analytic system, then use
analytic Wiener estimates with decreasing radius. This avoids assuming a
false discrete chain/product rule. Projection/sampling commutators must be
bounded for every operation. Standard abstract analytic Cauchy theory is
literature context until its hypotheses are actually checked. A self-contained
Fourier majorant/existence proof is preferred if feasible.

The invariants to verify explicitly are q=Dg and r=D B(g); these are redundant
analysis variables, not new canonical degrees of freedom. Their preservation
must follow from exact time differentiation. Any physical interpretation of
coordinate time as a record clock is withheld. Even success gives only a
local-in-time, supplied continuous/nonlocal approximation. It will not prove
exact finite first-class closure or smooth-data numerical stability.

Diagnostic plan, only after proof of its full-carrier invariant restriction:
1D-dependent diagonal metric, all six canonical components still accounted
for by transverse reflection symmetry. Compare the exact sampled curvature
Hamiltonian gradient with the independently varied augmented expression.
Use a pulled-back Kasner solution with exponents(-1/3,2/3,2/3), x mapped to
x+eta sin(x), |eta| small, t starting at1. Compute finite trajectory and true
C/J density errors versus J. A numerical convergence trend is diagnostic,
not the general theorem. Keep main-grid equations intact and preserve actual
failure cases, alias effects and floating precision limits.

Compute price: first symbolic/local-gradient plus small 1D full-carrier check
<=30CPU seconds, <=150MB, threads1; no 3D dense carrier, no long evolution,
no unpriced exponential coefficient enumeration. Check runtime deadline and
STOP_REQUESTED before each calculation; no unmanaged workers.
