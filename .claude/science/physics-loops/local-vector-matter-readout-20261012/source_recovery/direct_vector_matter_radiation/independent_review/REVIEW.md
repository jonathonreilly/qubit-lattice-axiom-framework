# Independent check: minimal vector matter coupling and radiation

Reviewer: `/root/direct_quantum_visibility_review`. Date: 2026-10-12.

**PASS for the stated leading nonrelativistic, slow-source and adiabatic circular calculation. No material mathematical correction is required.** This remains a conditional candidate extension, not a relativistic gravity model, complete finite-body theory, empirical test or pulsar exclusion. The original field proof is used at its stated premises, not re-audited here.

## Exact source boundary

The complete PROTOCOL, DIRECT_MATTER_RADIATION, SOURCE_LEDGER, author runner and RESULTS were inspected, together with the complete field-premise note. These bytes were copied into `pinned_source/` before independent execution and checked unchanged afterward.

| Source | SHA-256 |
|---|---|
| PROTOCOL.md | `ce1cda1413472803548599058dca8b468f897b42e569ecfc93014cafecffa43c` |
| DIRECT_MATTER_RADIATION.md | `e1d8a50b2cc448b3d4c0c994530e6fcde9fa83b2d5d3e4918ea5c2fb6097397f` |
| SOURCE_LEDGER.md | `7ea013f46a77b7a1e7c8d0c592c1918e026aeb26bb36a5fa6da32c0cc76cc802` |
| direct_radiation_check.py | `c88e590e32a308ec9012cc814a21a021aaf9d6ce78dfdf3d50f87db10634d9f8` |
| evidence_v1/RESULTS.json | `9be210deaaa05474e85517979c98bfb77deb21cab76d7c7da74fc634735beb8f` |
| LOCAL_VECTOR_HOMOGENEOUS_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md | `12a23ea9bafeac2ade4afffb1d9bd27bacc5da7915c3148543a4fc45edcf979e` |

The parent identifies the field source with frozen commit `68a7fa7890`; no Git command was used here. Its exact note hash is the operative proof-input pin. `SOURCE_PINS_v1.json` records original absolute paths, snapshots and hashes. No author file was changed.

## Energy, momentum and conservative mechanics

With `A_ji=mu partial_j u_i+beta delta_ji div(u)`, direct differentiation of the field energy gives

    partial_t h + div S = -rho phi_t,
    S_j = -u_t,i A_ji/(4 pi G).

My symbolic implementation derives this identity from the quadratic action without using the author runner. Matter power is `-J.grad(phi)`. Continuity makes the interaction-energy derivative `rho phi_t+J.grad(phi)`, so all exchanges cancel with the isolated-system boundary conditions. Static elimination gives `E_field=-1/2 integral rho phi` and total static interaction `+1/2 integral rho phi`. Positive field energy does not bound the interacting Hamiltonian below.

An independent Noether momentum check gives

    P_field,i = -alpha/(4 pi G) integral u_t,j partial_i u_j,
    dP_field/dt = +integral rho grad(phi).

The matter force cancels this. Total momentum is conserved; matter's centre of mass alone need not stay exactly inertial beyond the conservative approximation. For an extended body, its net force is the mass-profile integral. The point-force equation applies to mass elements or the exterior point limit; it is not a finite-self-energy point-body construction.

The static kernel gives the displayed even pair potential. Defining `A=N+D`, `B=N-D` and `cos(theta)=e.Rhat`, its force is

    F = -G m1 m2/(2 R^2) [(A+3 B cos^2(theta)) Rhat - 2 B cos(theta) e].

It is generally noncentral, while equal and opposite pair forces preserve translation invariance. The equatorial plane is invariant in the conservative model. Expansion yields the stated `G_eq`, circular energy and frequency, and

    nu_z^2 = G (m1+m2)(3D-N)/(2 a^3),
    nu_z^2/Omega^2 = (3D-N)/(N+D).

The restoring/marginal/unstable distinction at `N=3D` is correct within this fixed-direction model. The q=5 radiation inputs are prescribed trajectories in a vertically unstable plane, not stable binary examples.

## Green term, moments and positive radiation

For fixed nonzero omega,

    integral tau exp(i omega tau) d tau
      = exp(i omega tau)[tau/(i omega)+1/omega^2].

Between endpoints `r/c_L` and `r/c_T`, the absolute scalar middle term is bounded by

    (1/c_L+1/c_T)/(|omega| r^2) + 2/(omega^2 r^3).

The angular tensor factor is bounded. Thus the term is subradiative in the fixed-frequency large wave zone. At omega=0 the integral divided by r^3 is instead `(1/c_T^2-1/c_L^2)/(2r)` and contributes to the leading static field. These limits cannot be interchanged. The note correctly preserves the full retarded tensor for DC and causal support. Finite field propagation alone is not a relativistic matter or electromagnetic light-cone theorem.

The retarded density expansion is `M+n.d'/c+n_i n_j I''_ij/(2c^2)+...`. Mass conservation removes the monopole time derivative; the leading conservative centre-of-mass premise removes the density dipole contribution. The Taylor 1/2 and propagator `c^-2` give the stated `u_s=-G P_s e n_i n_j I''_ij/(2 alpha r c_s^4)`. A generic trace must remain; its derivative vanishes in the circular example. Dipole suppression is not an all-orders statement about field-coupled matter.

For the leading wave, `partial_r u_s=-u_t,s/c_s`. The traction coefficients are `alpha c_T` and `alpha c_L`. Orthogonality removes cross terms even at distinct retarded times, giving the stated positive two-square flux and mode power coefficient `G/(16 pi alpha c_s^7)`. This proves positivity for the propagating modes, not identification with observed tensor radiation.

## Independent angular and harmonic checks

I constructed the moment directly from both mass locations: `I=m_red R R^T`, with zero conservative dipole for any mass ratio. At phase zero the off-diagonal entries of `I'''` are `-4 m_red a^2 Omega^3`. Independently of the author's univariate angular integration, the sphere moments

    integral n_x^2 n_y^2 dOmega = 4 pi/15,
    integral n_x^2 n_y^2 n_z^2 dOmega = 4 pi/105

give transverse/longitudinal contracted integrals `512 pi/35` and `256 pi/105` in units `m_red^2 a^4 Omega^6`. Their power coefficients are `32/35` and `16/105`, agreeing with the author's time-averaged contraction and angular integrals.

A second implementation derives the exact prescribed-orbit density harmonics through Bessel functions. Up to a Fourier phase convention,

    rho_h = i^h [m1 J_h(h Omega r1 sin(theta)/c)
                  + (-1)^h m2 J_h(h Omega r2 sin(theta)/c)].

Equal antipodal masses have exactly zero odd harmonics. Adaptive angular quadrature and harmonics through 32 reproduce all 16 author controls, with maximum relative component difference `5.8504e-11`. This route uses neither the author's phase grid nor any author-runner import or execution. Halving speed produces approximately fourfold reduction of the leading-power correction. Unequal-mass checks retain higher odd harmonics while the leading density dipole remains zero, confirming the limited role of antipodal symmetry.

An analytic bound also controls omitted equal-mass harmonics. At `epsilon=a Omega/c_T <=2/25`, the absolute Bessel series gives `|J_n|<=b^n` with `b=(3 epsilon/4)/(1-epsilon^2/16)`. At the largest epsilon, `b=50/833`. An exact rational geometric sum over all n>=18 gives

    P_omitted/P_leading < 10^-35

for the author's q>=1 controls; its conservative value is about `5.8175e-36`. This bounds harmonic truncation, not floating Bessel/angle quadrature error. The author's high-harmonic fractions alone were numerical diagnostics.

The author fixes `G=Omega=M=1` and independently chooses small a. These are prescribed-source radiation controls, not solutions of the conservative orbital relation. That is adequate for their normalization/convergence purpose. I separately chose q=2, masses .3 and .7, and `a Omega/c_T=.03`, with `a=3333.3333333` and `Omega=6.36396103e-6` satisfying the circular relation. Orbital compactness is `.0009`; leading binding-energy loss per orbit is about `7.93e-8`. This demonstrates compatible slow/weak/adiabatic orbital inputs, not a coupled self-force evolution or internal-body solution.

## Comparator and physical interpretation

Using the expressly supplied GR quadrupole comparator, independent contraction of the trace-free circular tensor gives `32 m_red^2 a^4 Omega^6`. Substitution of `alpha D c_L^2=1`, `c_T=c_L/sqrt(q)` and the same `G_eq` yields

    P_vec/P_GR = (c_EM/c_L)^5 (6 q^(7/2)+1)/(21(q+1)).

With the additional calibration `c_L=c_EM`, q=1 gives 1/6. The derivative numerator `15q^(7/2)+21q^(5/2)-1` is positive for q>=1. Independent rational bisection of `6x^7-21x^2-20` gives a bracket strictly inside the author's exact sign bracket. The unique root implies

    q = 1.9368726097956006,
    c_T/c_L = .7185375538936453,
    polar/equatorial potential ratio = 1.3190034891778315,
    nu_z^2/Omega^2 = .361993021644337.

It lies below the vertical-instability threshold. Matching one supplied comparator consumes calibration and fixes these linked predictions; none is an observational fit. The period relation follows from the static circular energy and `P_orb proportional a^(3/2)` under adiabatic quasi-circular energy balance. Radiation reaction, persistence of circularity, relativistic proper time, timing delays and pulse arrival times are not derived.

The universal matter coupling is a new supplied physical premise. Reuse must retain constant coefficients/direction, motion slow relative to both field speeds, a wave zone beyond both wavelengths, weak damping and the stated source/clock interpretation. Smooth profiles regularize fields but do not supply internal stresses, inertial-mass matching, compact-body sensitivities or a strong-self-gravity limit. Finite-body matching is needed before these source parameters can represent compact stars. The strict D>0 field domain also excludes a D=0/infinite-speed limit.

The [Weisberg-Huang primary paper](https://arxiv.org/html/1606.02744v1) uses relativistic timing, fitted parameters and a Galactic correction; its reported corrected ratio agrees with the ledger. No timing files were downloaded or fitted here. The [Peters-Mathews abstract](https://journals.aps.org/pr/abstract/10.1103/PhysRev.131.435) was read; the PDF request returned an internal error. No unread PDF was proof evidence. The circular GR expression is an explicit comparator. An eccentric, strongly self-gravitating pulsar system is outside this weak circular calculation, so no empirical or sigma exclusion follows.

## Execution and disposition

Five independent families passed: energy/momentum; mechanics/multipoles/sphere moments; Green asymptotics/flux; Bessel harmonics; calibration. There were no scientific check failures or warnings. Full execution is preserved in `RAW_EXECUTION_v1.json`, structured results in `CHECKS_v1.json`, and the supplementary rational tail bound in `HARMONIC_TAIL_BOUND_v1.json`. Source hashes were guarded before and after execution.

The author's three labelled mutations are deliberately incorrect formula comparisons, not source-mutated executions. They test the specified discrepancies without establishing exhaustive mutation coverage. Its exclusive RESULTS write requires a fresh copy for a repeat; no in-place author execution was attempted. These are operational/testing boundaries, not mathematical defects.

An initial report-writing command failed before execution because the notation `I'''` terminated a Python triple-single-quoted string. Its raw diagnostic is preserved in `REPORT_WRITE_FAILURE_v1.txt`; the corrected write changes no scientific result. The independent check output remains immutable.

This conditional unit can support further author development within its premises. Finite-body completion, a relativistic clock/light bridge, nonlinear background, timing likelihood and empirical tests remain open. Only this `independent_review` directory was written. No Git operation, author edit, AI worker, model change, PR action, formal audit or landing occurred. The original campaign deadline remains unchanged.
