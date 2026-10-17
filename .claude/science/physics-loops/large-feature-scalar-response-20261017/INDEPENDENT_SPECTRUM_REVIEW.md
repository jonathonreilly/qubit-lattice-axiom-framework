# Independent C18 valley spectrum and common-gap response check

Inputs: /private/tmp/large-feature-response/model.py, root-extracted from PR9671 head16ae120ee46a1186b5ca81cd7d393396089e77d6. I inspected model.py and independently constructed the symbolic matrix directly from its supplied corner/edge/chiral geometry, using exact phases (-i)^(shift_x-shift_y+shift_z), instead of calling its floating Bloch constructor for the symbolic calculation. Flux gauge is the supplied solver's square=plaquette=tube=1,triangle=0 solution. This checks the model-conditioned spectrum, not the derivation of this Hamiltonian or flux choice.

Code: /private/tmp/large-feature-spectrum-check.py
Output: /private/tmp/large-feature-spectrum-check.json
Five grouped checks pass; max discrepancy across100 independently sampled numerical spectra is4.440892098500626e-15. Thirty full-k positive-scaling checks also pass. No repository writes.

## Exact result

At k=-(pi/2)(1,-1,1), the reconstructed Hermitian12×12 matrix has characteristic polynomial

(z²+2az−2a²−2(b+c)²)^4 ((z−2a)²−2(b−2c)²)^2.

On the branch q=sqrt2(b−2c)>0 and r=sqrt[3a²+2(b+c)²]>0 the four energies, with multiplicities, are:
E0=2a−q (2), E1=−a−r (4), E2=2a+q (2), E3=−a+r (4).

For this to be their increasing order require D1=−3a+q−r>0, q+r>−3a, and −3a+r>q (besides q>0). These are open inequalities and hold at(-1,.1,-.5). The box a∈[-1.05,-.95],b∈[.08,.12],c∈[-.52,-.48] remains on this branch: q∈[1.4707,1.6405], r∈[1.7224,1.9223], -3a∈[2.85,3.15]; these bounds themselves ensure all three inequalities. Also b+c∈[-.44,-.36]. One hundred seeded samples in this preselected box confirmed the ordered spectrum numerically.

The gaps D1,D2=2q,D3=−3a+q+r have exact inverse

a=(D2−D1−D3)/6,
q=D2/2, r=(D3−D1)/2,
v=b+c=−sqrt[(r²−3a²)/2], u=b−2c=q/sqrt2,
b=(u+2v)/3, c=(v−u)/3.

The sign of v must be fixed; eigenvalues alone retain a discrete v→−v ambiguity outside the local branch. The formula is invalid at the square-root boundary v=0 for differential inversion. In fact, the exact three-gap Jacobian is

 det ∂(D1,D2,D3)/∂(a,b,c)=−72sqrt2(b+c)/r,

which is nonzero in the chosen box. This independently verifies local invertibility.

## Response theorem and limitations

Suppose a continuous parameter curve stays in this ordered branch and all nonzero gap ratios stay fixed. Define g=D2(s)/D2(s0)>0. All three gaps then equal g times their reference values. The inverse is positively homogeneous of degree1 on the fixed square-root branch, so (a,b,c)(s)=g(s)(a,b,c)(s0). Conversely a positive parameter ray scales all gaps. At the differential level, two independent ratios being stationary implies the parameter tangent is radial; a global ray follows if that condition holds along the curve, not merely at one point.

Because the FULL Bloch matrix is linear in a,b,c, this ray gives H(k;s)=g(s)H(k;s0) at every fixed k. Every band energy and every energy difference scales g. Momentum derivatives/curvatures therefore also scale g whenever the relevant band is differentiable; at degeneracies one must use an appropriately defined effective matrix or smooth branch, not assert an ordinary scalar Hessian without justification. Eigenvectors/projectors for spectrally isolated clusters are unchanged and extrema stay at the same k for g>0.

Important for the intended scalar bridge: in fixed lattice space/time units a band inertial parameter defined as the reciprocal quadratic curvature scales1/g, whereas internal gaps scale g. This is not by itself the universal conformal matter response of physical clocks and inertial bodies. A physical metric/coordinate conversion or additional derived dynamics would be required; it must not be silently supplied. These quantities are excitation gaps and dispersion curvatures, not established physical rest masses, cosmological scalar variables, or Newton constants.

The symmetry/code alone does not force g, choose this ray, relate it to cosmological zeta, or establish screening/boundary response. Nevertheless the calculation makes an actionable test: unequal gap-ratio response or incompatible curvature response rules out the particular simple common-rescaling identification in this microscopic model.

## Preserved implementation failure

Initial exact-polynomial comparison returned false despite numerical agreement because SymPy charpoly constructs its generator without the real-symbol assumption. The original JSON is preserved as large-feature-spectrum-check.initial-symbol-mismatch.json. Explicit substitution of poly.gen into the common real symbol fixes that comparison; the independently reconstructed matrix and expected polynomial were unchanged. This was a checker-symbol mismatch, not a model failure.
