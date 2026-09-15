# Test the actual hybrid curvature before using it

Personal continuation of block 1. The proposed mechanism is a pointwise
Bakry-Emery estimate Gamma2(f)>=k Gamma(f), k>0, for the exact hybrid
generator in BLOCK1_POSITIVE_HYBRID_GENERATOR.md. Such a bound could support
response estimates; it has not been established. The test below targets
that sufficient criterion, not existence of a spectral gap or a field limit.

Use the actual single free four-cube, all 24 plaquettes and rank-17 exact
projection P. Keep tau=1/64 and A=I+tau DD*. The initial diagnostic sets
V_e=0 to calculate the reference exactly. Then use the actual small real
Hessian bound on V_e and its periodicity to check whether the result persists
for the supplied fixed-clock law. Do not identify this reference as the
finite-clock law by fiat.

For a face p set h=2pi sqrt(beta), z0=h e_p, q=h^2 A_pp, mu=exp(q/4),
lambda=exp(-3q/4), r=exp(-q/2). Choose a smooth compactly supported function
of z_p only. Its values at z_p/h= -1,0,1,2,3 are respectively 2,1,0,0,0.
At z_p=0,h,2h its first derivative is a0=h mu/2 and second derivative is
zero; at h its third derivative is also zero. Disjoint smooth bumps, equal
to one near these five points, realize these jets with compact support.

Evaluate Gamma=|P grad f|^2+(1/2)sum c_v(Delta_v f)^2 and
Gamma2=(1/2)L Gamma-Gamma(f,Lf) directly from the generator. Independently
derive a scalar expression using the cube's incidence and translation
symmetries. A negative value at this admissible point rejects a global
positive pointwise-curvature argument. It says nothing against an integrated
Bochner estimate, a weighted large-field argument, or another exact dynamics.

The calculation must retain changes of the p jump rate under other face
jumps; ignoring them changes Gamma2 even when f depends only on z_p.
The actual electric correction must also be bounded, not simply omitted.
