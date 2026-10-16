# Conformal exchange and an exact shared physical background

Root candidate, frozen before executable controls. Status: conditional-support.
This is an explicit construction inside a supplied scalar/conformal class. It
does not derive that class, claim a new reconstruction method, or establish a
global observational degeneracy. Its purpose is to test a proposed inference
from physical matter conservation to the missing conformal coupling.

## Exchange identity

Let gJ be a supplied physical metric, TJ_ab a symmetric physical stress, and
chi any smooth function. Define gE_ab=exp(-2chi)gJ_ab and the matter stress of
the conformally transformed matter action by TE_ab=exp(2chi)TJ_ab. Hence
TE^a_b=exp(4chi)TJ^a_b and TE=exp(4chi)TJ. The connection difference is

    GammaE^a_bc-GammaJ^a_bc
      =-delta^a_b chi_c-delta^a_c chi_b+gJ_bc chi^a.

In four dimensions, direct index contraction gives

    nablaE_a TE^a_b
      =exp(4chi) nablaJ_a TJ^a_b + TE chi_b.

The derivative of exp(4chi) cancels the contracted connection difference;
the two remaining symmetric-stress contractions cancel each other, leaving
the trace term. This identity needs no scalar or Einstein equation. Where
physical matter is conserved and its trace is nonzero, the proposed ratio
nablaE TE / TE equals dchi for every chosen chi. It therefore cannot select
chi when the Einstein metric and stress were defined using that same chi.
If an independent Einstein metric and matter stress split were already
available, the relation would instead be a legitimate consistency condition.
For traceless matter, dividing by TE is undefined and supplies no clock.

## Full-action shared-background construction

Take physical data gJ=-d tau^2+dx^2 and homogeneous pressureless matter with
constant physical rest density rho>0, at rest in these coordinates. This is
a deliberately simple supplied background, not a model fitted to the sky.
For every positive constant nu choose chi=nu tau, A(chi)=exp(chi), and

    dtE=exp(-chi)d tau, aE=exp(-chi),
    HE=-nu exp(chi), chi_dot=nu exp(chi),
    chi_ddot=nu^2 exp(2chi), rhoE=rho exp(4chi),
    Xchi=chi_dot^2/2=nu^2 exp(2chi)/2.

Here dots use Einstein proper time. In the explicit action

    S=int sqrt(-gE)[M^2 RE/2+K_nu(chi)Xchi-V_nu(chi)]
        +Sm[exp(2chi)gE],

select the functions

    K_nu(chi)=2M^2-(rho/nu^2)exp(2chi),
    V_nu(chi)=2M^2 nu^2 exp(2chi)-(rho/2)exp(4chi).

Then the scalar density and pressure are

    rho_chi=3M^2 nu^2 exp(2chi)-rho exp(4chi),
    p_chi=-M^2 nu^2 exp(2chi).

Substitution must satisfy all of

    3M^2 HE^2=rhoE+rho_chi,
    -2M^2 HE_dot=rhoE+K_nu chi_dot^2,
    rhoE_dot+3HE rhoE=chi_dot rhoE,
    K_nu(chi_ddot+3HE chi_dot)
      +(K_nu,chi/2)chi_dot^2+V_nu,chi+rhoE=0.

The last source sign follows Tm=-rhoE and the scalar variation convention
div(P_X grad chi)+P_chi+Tm=0. Physical dust conservation also holds directly.
The Einstein equation is not omitted or replaced by an adjustable external
stress in this construction.

The scalar principal coefficient is K_nu, so on any local patch satisfying
rho exp(2chi)<2M^2 nu^2 it is positive, nondegenerate and luminal. Such patches
exist simultaneously around tau=0 for, e.g., M=rho=1 and nu=1 or2. A canonical
coordinate psi=int sqrt(K_nu)dchi exists there. This coordinate change does
not turn the selected potential or conformal history into a derived one.
The candidate has a finite-patch positivity condition, not global stability,
past completeness or an ultraviolet completion.

These backgrounds have identical supplied gJ and TJ and the same local
scalar principal speed, while chi(tau), the functions K,V and Einstein
geometry differ. No equality of their complete perturbative response,
effective local Newton constant, nonlinear wave mixing or all physical
observations is claimed. In particular, a calibrated tidal/slip perturbation
or force response can potentially distinguish them. This positive family
isolates the specific missing information in the exchange-ratio shortcut;
it is not a general impossibility statement about observational inversion.

## Predeclared checks and next decision

Verify the exchange identity by full index contraction for an arbitrary
symmetric four-dimensional stress and arbitrary chi gradient. Independently
check both conformal metric curvature components and all homogeneous action
equations for the family; use exact rational local examples for positivity,
physical-metric equality and different coupling histories. A wrong exchange
sign and a wrong potential coefficient must fail. Preserve failures before
repair. No observational array is used, and no known single-metric inverse
reconstruction is counted as a new result.

If the construction checks, move to observations that add a genuinely
independent scalar response or state-space direction rather than using
conservation to select a conformal frame by definition.
