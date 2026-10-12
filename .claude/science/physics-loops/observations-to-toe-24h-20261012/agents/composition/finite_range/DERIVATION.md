# Independent shell derivation, before numerical profiles

The new frozen model uses the positive, normalized inverse-range measure

    dν_ell(μ)=ell exp(-ell μ)dμ,  μ≥0,  ell>0.

All mediator modes share the same material coupling vector d=(g,x,e), with positive modal weights. This is a new spectral comparison model. It is not an unnoticed substitution into the earlier exactly massless analysis.

For a thin spherical source shell of radius a and a point test at r>a, angular averaging of a single Yukawa Green function gives

    (1/2)∫[-1,1] exp(-μ sqrt(r²+a²-2ra z))
                       /sqrt(r²+a²-2ra z) dz
      = exp(-μr)/r * sinh(μa)/(μa).

The substitution u=sqrt(r²+a²-2ra z) gives the result directly. A shell of material charge q contributes its mass times this kernel; an arbitrary spherical profile is then integrated in mass coordinate.

For the exponential measure, integrate the shell kernel over μ first. With A=ell+r, the potential relative to the massless point-source GM/r has factor

    P_ell(r,a)=ell/(2a) ln[(A+a)/(A-a)].

The a=0 limit is ell/A. Its attractive radial force relative to GM/r² has factor

    F_ell(r,a)=P_ell(r,a)-r ∂P_ell(r,a)/∂r
              =ell/(2a) ln[(A+a)/(A-a)]
                +ell r/(A²-a²).

Thus F_ell(r,0)=ell(ell+2r)/(ell+r)², and both factors tend to one as ell tends to infinity. These expressions are dimensionless. They are positive for ell>0 and r≥a; ell keeps the surface endpoint nonsingular.

Define the source vectors

    W_P(r)=∫source [dM/M] P_ell(r,a) q(a),
    W_F(r)=∫source [dM/M] F_ell(r,a) q(a).

For a point test of charge α_T=q_T·d, the scalar potential is -G_*M α_T(W_P·d)/r and the attractive scalar acceleration relative to G_*M/r² is α_T(W_F·d). The source vectors include their form-factor normalization; replacing W by (1,Qme_eff,Qem_eff) requires also retaining W[0]. Annual clock modulation induced by a changing source distance differentiates the potential and therefore uses W_F, whereas a static scalar shift uses W_P. These two source rows cannot be interchanged.

For a single Yukawa mass, the exterior field factor exp(-μr)(1+μr) multiplies a source form factor independent of r. Two exterior radii therefore give proportional source rows for any fixed μ. Integrating a distribution of μ changes their relative weights with r; a composition-dependent radial source profile can then rotate the effective row. This distinguishes a distributed mediator from one fixed Yukawa mass. A point source, a spatially constant composition, or the massless limit removes this radial composition discriminator.

This is a classical, linear source-response calculation. It does not supply an instrument transfer function, dynamical solar GM calibration, Earth test-body form factor in the ephemeris, or scalar state covariance, and supports no empirical exclusion by itself.
