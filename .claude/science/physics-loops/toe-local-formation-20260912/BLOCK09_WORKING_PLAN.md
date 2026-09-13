# Constraint reduction and positive tensor transfer: derivation plan

2026-09-13. Provisional dependency: Block7 exact Hessian identity, same-author
checked but not independently reviewed. This block may compose in the same
coherent candidate; it cannot confer retention on that dependency. Block8's
hyperdiagonal nonlinear constraint is kept separate and is not erased by a
linear quantum construction.

Target: explicitly solve the linear scalar/vector constraints at every nonzero
spatial momentum, then construct a positive transfer operator on the two tensor
coordinates. This could replace the corrected main note's isolated diagonal
kinetic tests with a complete conditional linear reduction. It will not choose
a physical clock, Regge action, matter source or nonlinear completion.

Let p=(r e_3,t), r>0. Split H into spatial TT tensor, transverse trace tau,
longitudinal spatial sigma, vectors v_a=H_a3, shifts b_a=H_a0,b_3=H_30,
and lapse a=H_00. A manual expansion of F_p gives

F_TT=(r^2+t^2) tr(H_TT^2),
F_vector=2 sum_(a=1,2)(t v_a-r b_a)^2,
F_scalar=-(r^2+t^2)tau^2/2
         -2tau(r^2 a+t^2 sigma-2rt b_3).

Varying lapse imposes tau=0. Varying shifts makes the vector combinations zero.
Their gauge directions remove v_a; longitudinal/time gauge removes sigma,b_3,
and the tau equation fixes the remaining lapse combination. Thus only two TT
coordinates propagate. These statements must be checked as full mixed forms,
not inferred from zero diagonal entries.

For the explicitly chosen orientation -S_R and positive overall normalization,
the quadratic TT action is F_TT/8. Rescale each orthonormal TT amplitude H=2X,
to obtain the ordinary real scalar time-lattice action
1/2 sum_n[(X_(n+1)-X_n)^2+r^2 X_n^2].
Its transfer kernel is
K(x,y)=(2pi)^(-1/2) exp[-(x-y)^2/2-r^2(x^2+y^2)/4].
It factors as M exp(partial_x^2/2) M, M=exp(-r^2x^2/4), hence is positive
and self-adjoint. For r>0 it is trace class. Direct Gaussian integration gives
frequency E=2asinh(r/2), oscillator width a=sinh E, and eigenvalues
exp[-E(n+1/2)]. Ground covariance is exp(-E|n|)/(2sinh E), whose time Fourier
transform is 1/[r^2+4sin^2(k_t/2)].

Prove reflection positivity for the reduced tensor histories using the positive
transfer, with the real momentum-pair convention and zero-spatial-mode exclusion
explicit. This defines a reduced linear quantization. Do not claim convergence
of the full unconstrained Euclidean Regge integral or positivity of its conformal
sector. A finite physical qubit realization and native matter source remain open.


Keep the otherwise free hypercoordinate as an explicitly fixed section of the
linear model, not a vertex gauge mode. The TT quantization will describe only
the reduced tensor observables and will not prove that every tensor tangent
extends nonlinearly. For the first finite theorem take odd spatial periods,
exclude spatial k0, and use real conjugate momentum pairs; this avoids silently
assuming a real polarization frame at self-inverse Nyquist momenta. Time is an
independent supplied integer coordinate. Site and link reflection positivity
follow from the positive normalized transfer. No full conformal-field path
integral is defined by this reduced construction.
