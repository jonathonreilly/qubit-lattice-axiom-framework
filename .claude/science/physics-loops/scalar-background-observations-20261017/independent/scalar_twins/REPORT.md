# Independent original-equation check: scalar background twins

The two supplied witnesses pass the original homogeneous equations exactly. This is a conditional background nonidentifiability example. It is neither an observational fit nor an assertion that the two theories reproduce identical perturbative observables.

## Independent derivation

Set M=1, A=tau^s, zeta=s ln(tau), a_E=tau^(2-s), dt=d tau/A. Then

- H_E=(2-s)tau^(s-1), dot(zeta)=s tau^(s-1), ddot(zeta)=s(s-1)tau^(2s-2).
- rho_E=(1/8)tau^(4s-6).
- -2 dot(H_E)=rho_E+F dot(zeta)^2 fixes F=2(2-s)(1-s)/s^2 - tau^(2s-4)/(8s^2).
- 3 H_E^2=rho_E+F dot(zeta)^2/2+V then fixes V=(2-s)(5-2s)tau^(2s-2)-tau^(4s-6)/16.

Substitution tau=exp(zeta/s) gives exactly the two F(zeta),V(zeta) functions in the task. No scalar equation was used in reconstructing them. Independently substituting into

F ddot(zeta)+3 H_E F dot(zeta)+(F_zeta/2)dot(zeta)^2+V_zeta+rho_E=0

returns zero, as does dot(rho_E)+3H_E rho_E-dot(zeta)rho_E. The script also checks the Friedmann and Raychaudhuri residuals directly, without using a cached reduced answer.

Both have a_J=A a_E=tau^2 and rho_J=rho_E/A^4=(1/8)tau^-6. They have the same Jordan proper time and H_J=2/tau, with A(1)=1.

## Regularity and positivity on the declared interval

For s=1/2, F=6-(1/2)tau^-3 is increasing, hence F>=2 on [1/2,1]. V=6 tau^-1-(1/16)tau^-4 has derivative tau^-5(1/4-6tau^3)<0, hence V>=95/16.

For s=1/4, F=42-2tau^(-7/2) is increasing, hence F>=42-16sqrt(2)>0. V=(63/8)tau^(-3/2)-(1/16)tau^-5 has derivative tau^-6[5/16-(189/16)tau^(7/2)]<0, hence V>=125/16.

All quantities are smooth and finite on the compact interval. Positive F permits local canonical normalization chi=integral sqrt(F) d zeta; the original displayed kinetic coefficient is variable, so describing zeta itself as canonically normalized would be incorrect. Q is linear in Y.

## Are they just the same theory in different scalar or metric coordinates?

Within the declared Einstein-frame class, M=1 fixes the coefficient of R. A nonconstant conformal change away from that Einstein metric makes this coefficient nonconstant. Restoring a constant coefficient returns to the same Einstein-frame representative up to the fixed constant normalization. Coordinate changes alone do not change scalar relations at a fixed proper-time event.

A scalar relabel chi(zeta) changes the kinetic coefficient and the matter coupling together. With the matter factor specifically A=e^zeta, and A(1)=1, one cannot relabel zeta nontrivially while retaining that specified coupling. More invariantly, after canonical normalization, the squared slope of the matter coupling is

alpha^2=(d ln A/dchi)^2=1/F.

At the common normalized event A=1 this is 2/11 for s=1/2 and 1/40 for s=1/4. Scalar sign/shift conventions for a canonically normalized field do not change alpha^2 at a specified A. Also V(A=1) is 95/16 versus 125/16. Thus these are distinct action/coupling functions, not merely two names for the same scalar coordinate with the coupling transformed consistently. The potential and coupling invariants are statements about the supplied model class and fixed normalization, not measurements inferred from the common background.

The physical content that differs can also be read in the Jordan gravitational coefficient, proportional to A^-2=tau^-2s. A gravity/tensor/perturbation measurement could distinguish that coefficient. It is not fixed by equality of the expansion and dust-density histories alone. Do not claim equal all-observable universes.

## Independent test artifacts

`check.py` runs 16 exact identity checks, proves F,V positivity by monotonicity/endpoints, computes the coupling invariant, and rejects eight deliberate mistakes (scalar source sign, omitted proper-time conversion, dropped dust term in the potential, and wrong density conformal power, each for both witnesses). `result.json`, `mutations.json`, and `run.log` preserve exact expressions. No commits, pushes, or repository changes were made.
