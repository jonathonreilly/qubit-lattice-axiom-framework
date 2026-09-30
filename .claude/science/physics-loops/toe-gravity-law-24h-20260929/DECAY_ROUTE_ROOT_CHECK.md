# Focused coordinator derivation check of the decay extension

Checked the complete decay-symbol-route/REPORT.md after its independent route
finished, against the finite-support TT proof. This is a mathematical selective
check, not formal review or audit. No author code was imported or executed.

The noncommuting residual elimination was reconstructed directly. With
R0=DF+FD#-mu0F and RA=[D,X]F+DA+AD#-mu0A-mu1F,
D#=F^-1R0+mu0I-F^-1DF gives
(RA-AF^-1R0)F^-1=[D,X]+[D,AF^-1]-mu1I. In the convention S↔exp(ik),
[D,X]=-iD'. Periodicity therefore fixes averaged finite matrix trace to
-2mu1. The operator trace inequality and normalized measure prove the stated
Lp lower bound; no positivity or commutation was inserted. Uniform inverse
norm is needed for the absolute residual bound. Near-zero kinetic normalization
alone does not bound its ultraviolet inverse.

For the smooth scalar-matrix construction, A=-if'/2 satisfies A-A#=-if',
and the symmetrized lapse density (NF+FN)/2 has exactly this affine offset.
D=id gives uniform residual zero and affine residual (d'-1)f. Because d=k
on a neighborhood of supp f, this is exactly zero. The positive regularization
f_epsilon=(f+epsilon)/(1+epsilon) gives the displayed epsilon residual. This
checks a real reduced-pair escape, not arbitrary-smearing completion.

Re-derived SLAC coefficients and their compact-field commutator. For r!=0,
rD_r=-(-1)^r, and the r=0 coefficient is zero. Consequently [D,X]-I
is -v v^T as a quadratic form on compact profiles, v_x=(-1)^x. The bracket
defect is precisely minus half the squared alternating sum, including both TT
components. A smooth Fourier-support domain away from the seam removes that
form; ordinary nonlinear products need not preserve that domain.

The weighted-kernel domain argument was inspected separately. Differentiating
a degree-at-least-two term leaves a compactly supported field factor that
anchors its density center. An affine smearing costs one relative-offset
moment; the derivative's output-site sum introduces no second moment. Uniform
ell1 gradient bounds and dominated convergence pair with the O(1/R) fixed-seed
cutoff derivatives. All smearing offsets must be included in the kernel norm.
This justifies the necessary two reduced equations, without asserting global
Hamiltonian flow or compact-support preservation. A only inherits ell1, while
D and F have first moments; that regularity is enough for the trace proof.

Dense invertibility is essential for extending the trace equation by continuity.
Exponential kinetic decay makes the determinant analytic and nonzero at zero,
so its zeros cannot contain a real interval or an accumulation point on the
circle. Smooth decay alone lacks this implication; the bump explicitly tests
it. The author's scope statements and IR/full-zone distinction are justified.

This selective derivation check supports the route's claimed mathematical
boundaries. The source's prior-art reading coverage is its own record; the
coordinator separately read the actual Sep14 stencil/analytic-band sections.
Neither this check nor its finite controls grants retained framework status.
