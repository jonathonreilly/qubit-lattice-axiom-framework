# Conditional local-derivative continuation target

This is a small analytical probe, not an accepted descendant or a separate PR.
The root uniform analytic spectral-evolution proof is still under independent
check. Do not use this file as proof that its bootstrap/convergence is sound.

The exact augmentation and first-order formula in that candidate only require
skew-adjoint D. Its derivative-loss bound uses |d_J(k)|<=|k|; the nonlinear
Wiener algebra estimates come from the grid product itself. This suggests
replacing spectral ik by the explicit local centered symbol

 d_(a),j(k)=i sin(a k_j)/a,   a=2pi/(2J+1),
 D_(a),j f(x)=[f(x+a e_j)-f(x-a e_j)]/(2a).

Define the Hamiltonian afresh by the same literal Christoffel formula using
this D. This is a collocated continuous-metric law with finite spatial range,
NOT preservation of block112's staggered derivative/face-timed seed and NOT
an exact finite first-class algebra. Low-band or analytic input restrictions
do not delete high canonical variables.

Before any numerical test: freeze the discrimination as a bound for the actual
finite Hamiltonian evolution and true scalar/momentum densities. The prospective
rate is O(a^2) over a positive time independent of J in smaller analytic norms,
with separately controlled sampling aliases. Because
|sin(a k_j)/a-k_j|<=a^2 |k_j|^3/6,
the consistency of the derivative on analytic functions has a bound of size
 a^2 [3/(e delta)]^3/6
plus an exponentially small alias tail, for a radius reserve delta>0.
All subsequent estimates would need actual verification under this changed D.
The central symbol's ultraviolet zeros/near-zeros and extra finite-grid modes
are retained; no all-zone mode purity or smooth-data numerical stability follows.

If true, this would distinguish finite-range EXACT closure obstruction from
a controlled finite-range continuum approximation. It still imports continuous
canonical geometry, selected law/initial analytic regime, and a refinement/time
normalization. It does not select a physical qubit law or record clock.
First next action, only after the parent check: verify the full residual bound
with aliases and the exact local Hamiltonian support, then run one priced
Kasner control through a separately specified local derivative. Avoid a new
milestone from changing one knob; compose it into the same coherent nonlinear
approximation unit if it adds the declared locality information.
