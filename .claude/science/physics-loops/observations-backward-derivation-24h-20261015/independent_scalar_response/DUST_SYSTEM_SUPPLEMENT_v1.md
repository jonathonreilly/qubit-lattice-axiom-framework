# Independent velocity convention and full-system supplement

This supplements the already frozen INDEPENDENT_PROOF_v1.md before any author response/matter-clock exposure. Root requested explicit velocity divergence; no author formula was supplied.

Define the irrotational coordinate velocity by a_E^2 dx^i/dt=partial_i U, so the physical peculiar velocity is v_p^i=partial_i U/a_E. Define the Fourier physical divergence theta=(1/a_E)partial_i v_p^i=-K^2 U, K=k_com/a_E. This is not the conformal-time divergence without its a factor. Let delta=delta(rho)/rho for bare proper Einstein-frame number/rest density.

Number conservation is dot(delta)=-theta+3dot(P). The particle action expanded to first perturbative order gives d[A a_E^2 dx^i/dt]/dt=-A partial_i(P+alpha chi); hence dot(U)+alpha v U=-P-alpha chi. Since dot(K^2)=-2H K^2, the equivalent divergence equation is

  dot(theta)+(2H+alpha v)theta=K^2(P+alpha chi).

The Einstein momentum constraint is

  dot(P)+HP=(v chi-rU)/(2M^2)=(v chi+r theta/K^2)/(2M^2).

The density trace is not an independent choice after satisfying the initial Hamiltonian. The dynamic spatial trace equation is

  ddot(P)+4Hdot(P)+(2dot(H)+3H^2)P
     =[v dot(chi)-v^2P-V_phi chi]/(2M^2).

Taking a time derivative of the momentum constraint and using dot(r)=(alpha v-3H)r, dot(v)=-3Hv-F, and the Euler equation reproduces this spatial-trace equation after -2M^2dot(H)=r+v^2. No quasistatic matter closure enters. The Hamiltonian constraint must also be propagated; the executable test will check it rather than treating its algebraic source elimination as sufficient dynamics.

The source-elimination identity [E] alone is not a normal-mode solution, does not determine density/velocity histories, and gives neither their boundary conditions nor a mode spectrum. On a rolling FLRW background there is no assumed time-translation invariance. The independent calculation will integrate the original scalar equation, number continuity, Euler and momentum equations with a Hamiltonian-consistent initial density, then evaluate the Hamiltonian, spatial-trace, eliminated response and matter-clock residuals. That finite trajectory checks the equations; it is not an observed background or a stability/classification theorem.
