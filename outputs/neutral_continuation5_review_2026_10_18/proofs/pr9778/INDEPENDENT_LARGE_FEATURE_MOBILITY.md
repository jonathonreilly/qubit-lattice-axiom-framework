<!-- Original PR9778 source SHA256 277b02c401b64d676315ae94327f53618423c88866393f201dc7c4a5a293b5e9. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Threshold mobility and coefficient energetics: independent check

Disposition: PASS for the complete compact K1 coefficient graph, with parameter derivatives justified from the exact Green-function expansion as specified below. Read /tmp/neutral_threshold_mobility_root.md and reused the previously checked cavity/threshold construction. No shared/canonical edits.

## Exact longitudinal identity

For hopping magnitude 2c on either ray, sigma(E,c)=(E+sqrt(E^2-16c^2))/2 and partial_c sigma=-8c/sqrt(E^2-16c^2), with E below the ray band. Let u be the two root amplitudes in the FULL normalized eigenvector. Differentiating the eliminated equation gives a factor [||psi_host||^2-sigma_E|u|^2] in front of E_c. This is precisely the full norm, including the two rays, hence equals one. Therefore

 E_c=sigma_c |u|^2

is exact; there is no additional denominator. Equivalently it follows by summing the ray hopping Hellmann-Feynman form. Since c=cos(Qz/2), at Qz=0,

 E_zz=-E_c/4=2|u|^2/sqrt(E^2-16)>0.

For the separately established leading source vector lambda(-1,b), W_C/lambda^2=|(-1,b).u|^2. Thus the proposed ratio to the LEADING coefficient-model source weight is exact wherever the overlap is nonzero:

 E_zz/(W_C/lambda^2)=2/[sqrt(E^2-16)|(-1,b).v_E|^2].

It is not an exact identity for the fully dressed microscopic source weight including higher orders.

Using the checked threshold normalization gives E_zz~A delta log^2(1/delta), with

 A=c_log/[sqrt(Eh^2-16) sigma^2(D.v)^2].

The ratio A/W0=2/[sqrt(Eh^2-16)|(-1,b_c).v|^2] is correct and finite positive given the established nonzero threshold overlap. All these energies/curvatures are K1 coefficients; physical first-order energy curvatures carry Jz lambda.

## Derivative control and Hessian

One cannot differentiate the sole asymptotic statement log(1/delta)~constant/(b_c-b). The exact cavity construction does, however, provide the extra regularity needed here. Work in a fixed parameter neighborhood of (a,b,c)=(1,b_c,1), where a,b stay positive and the host edge stays separated below the ray edge. The free lattice Green integrals have a unique nondegenerate quadratic minimum. Splitting off a neighborhood of this minimum, applying a parameter-smooth local Morse coordinate, and expanding the fixed-displacement numerators gives a logarithmic expansion in delta with smooth parameter coefficients. Parameter derivatives of any fixed order have the same structure, and delta derivatives have the corresponding inverse powers. The nonsingular complement is analytic. The finite cavity Schur operations preserve this expansion.

With t=1/log(1/delta), the critical Birman equation consequently has the form F(theta,t)=mu_edge(theta)-1-K(theta)t+O(t^2), with a smooth extension to t=0; the remaining delta-dependent terms are exponentially flat in t. K>0. The implicit-function theorem gives a smooth t(theta), vanishing simply on the smooth critical surface. On the binding side delta=exp[-1/t(theta)]. Every fixed parameter derivative is delta times at most a finite inverse power of t, and therefore tends to zero. This supplies the derivative claim; the uniform local Green expansion, not merely the undifferentiated threshold law, is the necessary supporting argument.

It follows that E(a,b,c)=-4(a+b)-delta(a,b,c) has E_a->-4 and E_b->-4, with derivatives of delta through second order vanishing. At Qx=Qz=0 and Qy approaching the critical momentum on the binding side,

 E_xx ->1,
 E_yy ->b_c,
 E_zz >0 and E_zz~A delta log^2(1/delta).

Evenness in Qx and Qz makes all mixed second derivatives vanish on this line. Hence the Hessian is positive definite sufficiently near threshold, albeit increasingly singular in its z eigenvalue. This does not contradict the negative y curvature at the Qy=pi anchor. Also E_y->2sqrt(1-b_c^2)>0 on the positive-Qy branch, so this point is moving, not an energy minimum or stationary rest point. “Positive Hessian” should not be shortened to “local minimum.”

## Global K1 lower bound

After gauging the positive y-ray hopping negative, all edges of the graph are nonpositive for a,b,c in [0,1], and their magnitudes are monotone in these parameters. For every vector psi,

 <psi,H(a,b,c)psi> >= <|psi|,H(1,1,1)|psi|> >= -8||psi||^2.

The second inequality uses the checked all-one edge Birman criterion: its largest edge eigenvalue is 2-sqrt(3)<1, so there is no spectrum below the host bottom -8; the detached rays/frozen pieces do not lower that bottom. Thus K1>=-8 uniformly in these fibers. Widely separated host packets at the zero-momentum fiber approach -8, making the global bound sharp for this graph.

The near-critical bound branch has energy approaching -4(1+b_c), approximately -4.939, and therefore does not minimize the full N4 coefficient energy over momentum. This is a precise coefficient-sector selection limitation, not a statement that the branch cannot be prepared or contribute to response. It provides no full-H no-go, cosmological selection principle, isotropic light cone, or Lorentz-scalar interpretation.
